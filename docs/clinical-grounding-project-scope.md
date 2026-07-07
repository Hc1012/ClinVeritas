# ClinVeritas — Clinical Note Grounding Benchmark & Verifier Study
## Project Scope v1 (feasibility verified 05 Jul 2026)

**One-line pitch:** A three-way claim-grounding benchmark for AI-generated clinical notes (supported / contradicted / insufficient), plus a scale study of whether ISR-style verification signals detect the error types that actually harm patients. "RepoVeritas for clinical notes."

**Series position:** Repo 6 in the grounding research line:
isr-calibration → order-dispersion-scaling → isr-code-grounding → RepoVeritas → ntk-scaling-experiments → **clinical transfer**

---

## 1. Feasibility check — DONE (results from tonight)

### ACI-Bench (github.com/wyim/aci-bench) ✅
- **207 encounters** total: 67 train / 20 valid / 3 × 40 test splits
- Format: clean JSON, `src` = full doctor–patient dialogue transcript, `tgt` = structured SOAP note (Chief Complaint, HPI, ROS, Physical Exam, Results, Assessment & Plan)
- Section-level variants provided (subjective / objective_exam / objective_results / assessment_and_plan) — the Plan section is where published research found 21% of major hallucinations concentrate, and ACI-Bench already isolates it
- License: research-friendly, widely used in MEDIQA shared tasks

### primock57 (github.com/babylonhealth/primock57) ✅
- **57 mock GP consultations, UK clinicians, UK note style** (PMH/DH/SH shorthand, "3/7 hx of diarrhoea") — this is the NHS-relevant half of the benchmark
- Clinician-authored notes in JSON with a `highlights` field (clinician-marked important terms → free importance weighting for error severity)
- Transcripts in TextGrid format with a provided `textgrid_to_transcript.py` conversion script
- **Audio included** → future extension: does ASR degradation increase hallucination rates? (Known real-world failure source: noise, masks, mic distance)

### Critical validation finding
In ACI-Bench train example 1, the gold reference note states **"denies suicidal or homicidal ideation"** — but no form of the word "suicid*" appears anywhere in the transcript. The most clinically sensitive line in the note is **ungrounded in the source dialogue, in the human-written gold standard**.

Implications:
1. The "insufficient" (abstention) class is not synthetic — it occurs naturally, even in reference notes
2. Any benchmark that only labels AI-generated notes misses this; labelling gold notes too gives a human baseline for ungrounded documentation
3. This single example is the demo/talk opener: "the gold standard itself contains unverifiable psychiatric claims"

Also verified: specific claims trace cleanly to transcript spans (edema ✓, murmur ✓, vaccine ✓, medication non-adherence ✓), so claim-level decomposition works.

---

## 2. Benchmark design

### Unit of annotation
(transcript, note-claim) pairs. Notes decomposed into atomic claims (one clinical assertion each). Target: **~1,500–2,500 labelled claims** across both datasets (comparable scale to RepoVeritas's 294 items but claims are cheaper to label than code items).

### Label taxonomy (three-way, matching RepoVeritas)
- **SUPPORTED** — claim entailed by transcript content
- **CONTRADICTED** — transcript asserts the opposite (the negation-reversal class: "stopped metformin" → "continue metformin")
- **INSUFFICIENT** — transcript neither supports nor contradicts (fabricated exam findings, unstated denials, filled-in template language)

### Secondary tags (cheap to add, high analysis value)
- Note section (HPI / ROS / Exam / Results / Plan) — tests the "Plan concentrates hallucinations" finding
- Error mechanism for negatives: fabrication / negation reversal / contextual / causality (maps to the published Asgari et al. taxonomy: 43% / 30% / 17% / 10%)
- Clinical severity: benign / relevant / treatment-changing (primock57 highlights help here)

### Hard negative construction (your BM25 playbook from isr-code-grounding)
1. **Natural negatives**: generate notes from transcripts with small open models (Qwen2.5 0.5B–3B produce plentiful genuine hallucinations); label what actually comes out
2. **Constructed negatives**: programmatic negation flips ("denies" ↔ "endorses", "stopped" ↔ "continue"), medication/dosage swaps, cross-transcript claim transplants (claim true for patient A inserted into patient B's note — the "cloned template" failure auditors look for)
3. **Gold-note audit**: label the reference notes themselves → human ungrounded-claim baseline

### Inter-rater reliability
Same protocol as RepoVeritas (κ = 0.80 there). Second rater on a 15–20% subsample. This is what makes it a *benchmark* rather than a dataset dump.

---

## 3. Experiments (the verifier study)

**E1 — Frontier eval (the headline):** How do frontier models (Claude, GPT, Gemini) do at three-way clinical claim grounding? RepoVeritas prediction: near-ceiling on supported/contradicted, poor on insufficient (0.657 F1 in code). If insufficient-F1 is similarly weak on *clinical* claims, that's the finding: **current models cannot reliably abstain on unverifiable clinical claims — the exact class human review is being paid to catch.**

**E2 — ISR verifier transfer:** Run ntkmirror's ISR sufficiency verifier on the benchmark across Qwen2.5 0.5B → 7B. Does the 1.5B lexical-baseline crossover from code reappear in clinical text? Same plot, new domain — direct extension of isr-code-grounding.

**E3 — Dispersion as clinical groundedness signal:** Does the dispersion signal (order-dispersion-scaling) separate grounded from ungrounded clinical claims, and does the wrong-sign penalty at small scales reappear? Critically: **does dispersion detect negation reversals specifically?** Negation reversal is 30% of real scribe errors and the scariest class; if dispersion catches it, that's a safety-relevant result.

**E4 — Section analysis:** Error rates and verifier performance by note section. Tests whether the Plan-section concentration replicates and whether verifiers are weakest exactly where errors concentrate.

**Stretch (repo 7 material, don't scope-creep):** ASR-noise robustness using primock57 audio; severity-weighted metrics.

---

## 4. Build order (each stage ships something)

| Stage | Deliverable | Est. effort |
|---|---|---|
| 1 | Data pipeline: parse both datasets, convert TextGrids, claim decomposition prompt + manual QA on 3 encounters | 1–2 evenings |
| 2 | Generate notes with small Qwen models; collect natural hallucinations | 1 evening (Colab T4) |
| 3 | Labelling pass 1 (~800 claims, ACI-Bench first) + constructed negatives | 1–2 weeks part-time |
| 4 | E1 frontier eval + writeup v0 | 2–3 evenings |
| 5 | E2 + E3 verifier study | 1 week (T4 sufficient at these scales) |
| 6 | Second rater, κ, full writeup, GitHub Pages report, repo release | 1 week |

Total: **5–7 weeks part-time.** Same shape and cadence as the ntkmirror arc.

### Division of labour (honesty framework applies)
- **You:** all labelling decisions, all experiment runs, the writeup voice, the κ study recruitment (Leon or a clinician contact as rater 2?)
- **Claude:** pipeline code assistance, prompt engineering for decomposition, analysis scaffolding, editing
- The human labels ARE the contribution — nobody can say the benchmark isn't yours

---

## 5. Honest theory of "big"

What this project realistically earns, in order of likelihood:
1. **Research credibility** — a UK-relevant clinical-safety benchmark with IRR and a frontier eval is workshop-paper shaped (ML4H, CHIL, MEDIQA community). Directly strengthens AiTASHA-type applications and the Leon collaboration (it's another ISR domain-transfer result for ntkmirror).
2. **Vendor attention** — scribe companies (UK: Tandem, Heidi, Accurx-adjacent) have hallucination as a procurement-blocking issue; NHS deployments require DCB0129/0160 safety cases. A public benchmark that exposes the abstention gap is the kind of thing their ML leads notice and cite. That's how conversations start — not cold pitches.
3. **NHS-world visibility** — Digital Health Rewired, London Tech Week health fringe, NHS AI communities. A benchmark travels because everyone can run it and compare.

What it does NOT do: hospitals do not "sponsor" benchmarks or individuals — NHS money moves through procurement frameworks to registered suppliers with safety cases. The path to being paid is: benchmark → credibility → role or consulting engagement or vendor collaboration → then products. Skipping to "hospitals fund me" is not a real step and chasing it will burn months.

---

## 6. Immediate next actions
1. Confirm project name (ClinVeritas / NoteVeritas / other) and create the repo
2. Stage 1: run `textgrid_to_transcript.py` on primock57, parse ACI-Bench JSON, pick 3 encounters, hand-decompose one note into claims to lock the claim-granularity rules
3. Write the labelling guideline doc BEFORE labelling at scale (RepoVeritas lesson: taxonomy decisions made mid-labelling force relabelling)
