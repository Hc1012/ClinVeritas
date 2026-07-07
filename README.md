# ClinVeritas

ClinVeritas is a work-in-progress clinical claim-grounding dataset and labelling protocol for transcript-grounded note verification, focused on Supported / Contradicted / Insufficient decisions.

It is intended to become a benchmark after second-rater reliability and held-out evaluation; the current public release is single-rater and pre-κ.

AI medical scribes are the largest current deployment wave of clinical AI. Their documented failure mode is not fluency but *grounding*: notes that assert things the consultation never established. The dangerous cases are rarely wild fabrications, they are plausible clinical specifics filled in where the transcript was silent or hedged. Detecting "this claim cannot be verified from the encounter" is exactly the judgement human reviewers are currently paid to make, and exactly the class frontier models handle worst.

ClinVeritas is the clinical sibling of [RepoVeritas](https://github.com/Hc1012/RepoVeritas) ("FEVER for code"): given a (consultation transcript, note-claim) pair, label it **SUPPORTED**, **CONTRADICTED**, or **INSUFFICIENT**, under a frozen human labelling protocol with binding precedents and a planned inter-rater reliability study.

> **Status: work in progress, single-rater.** 219 candidate rows across three batches have been human-labelled and adjudicated under a frozen protocol (guidelines v1 + amendments v1.1–v1.3). An automated-rater prompt-sensitivity study (E1/E1b/E1c) has been run over these rows. **Not yet done and required before this is a benchmark:** a second-rater inter-rater-reliability (κ) study, and Stage-2 model-generated-note rows. All labels are single-rater author adjudicated. Numbers below are reproducible from committed artifacts; none should be quoted as a final benchmark result.

## Reviewer path

For a quick technical review, inspect:

- `README.md` — project overview and status
- `guidelines/LABELLING_GUIDELINES.md` — frozen labelling protocol
- `guidelines/WORKED_EXAMPLES.md` — worked examples and precedents
- `labels/*/*ADJUDICATED*.csv` — current single-rater adjudicated labels
- `e1/runs/e1/E1_RESULTS_AUTOMATED_RATER_PILOT.md` — automated-rater pilot
- `e1/runs/e1b/E1_E1b_PROMPT_SENSITIVITY_SUMMARY.md` — prompt-sensitivity finding
- `RUN_PROVENANCE.md` — AI/provenance caveats

---

## Why an abstention class

Three way grounding forces a model to distinguish *"the transcript contradicts this"* from *"the transcript simply never said this."* In [RepoVeritas](https://github.com/Hc1012/RepoVeritas), frontier models nearly solve supported/contradicted while remaining far weaker on insufficient. In the clinical domain, the insufficient class is where the safety-relevant errors live: unverifiable consent attestations, fabricated safety netting advice, clinical specifics supplied from priors rather than from the patient. **Insufficient-F1 is therefore the headline metric of this project**, not overall accuracy.

## What guideline development surfaced (worked examples, single-rater, pre-κ)

Two encounters were fully decomposed to develop the protocol (see [guidelines/WORKED_EXAMPLES.md](guidelines/WORKED_EXAMPLES.md)). Both are **gold, human-written notes** — no AI involved — and both contain ungrounded content:

- A US reference note (ACI-Bench) closes with *"Patient understands and agrees with the recommended medical treatment plan"* — no agreement utterance exists anywhere in the transcript. → INSUFFICIENT [template attestation]
- A UK GP note (primock57) documents *"vomiting — mainly bilious"* where the patient said *"just normal food colour… normal vomit"* (→ CONTRADICTED, clinical-specific filling); *"wife and children also unwell with vomiting"* where the transcript states *"no one else in the family… one child was vomiting"* (→ CONTRADICTED, scope expansion); and *"to be seen earlier if feeling more unwell"* — safety-netting advice never given in the consultation (→ INSUFFICIENT, severity: treatment-changing).

The working hypothesis: **ungrounded documentation is not an AI defect but a documentation-culture defect that AI scribes inherit and scale.** ClinVeritas measures it in gold notes and (planned) in model-generated ones.

## Label schema

| Primary label | Meaning |
|---|---|
| **S** | Claim entailed by transcript content (S\* = supported via a tagged inference) |
| **C** | Transcript asserts a competing/opposite fact |
| **I** | Transcript neither supports nor contradicts |

`S*` is a bookkeeping distinction, not a separate capability; in evaluation, **S and S\* are collapsed into "grounded" and the primary task is three-way (Grounded / Insufficient / Contradicted)**. Secondary tags capture fidelity phenomena without polluting the primary task: [temporal displacement], [hedge flattening], [range narrowing]/[range violation], [world-knowledge inference], [second-hand grounding], [scope ambiguity], [intra-transcript conflict], [template attestation], [patient-directed safety-netting], [clinician contingency plan], [transcript diarisation error], [source integrity flag]. Every C and I carries a **severity** rating: *benign / relevant / treatment-changing*.

## Labelling protocol

Ten rules and three adjudicated binding precedents, frozen 05 Jul 2026, extended by three logged amendments — see [guidelines/LABELLING_GUIDELINES.md](guidelines/LABELLING_GUIDELINES.md), amendments [v1.1](guidelines/GUIDELINES_AMENDMENT_v1.1.md), [v1.2](guidelines/GUIDELINES_AMENDMENT_v1.2_CONSENT.md), [v1.3](guidelines/GUIDELINES_AMENDMENT_v1.3_ACISN.md). Highlights:

- **R1 — semantic labelling only.** Keyword search may *locate* candidate evidence; it never *assigns* labels. (Origin: a paraphrase-supported psychiatric denial was falsely flagged ungrounded by keyword matching during development.)
- **R4 — unique-completion test** for world-knowledge inference; clinical specifics always fail unless the transcript pins them.
- **P1** — a competing transcript description beats unsupported clinical-specific filling → C.
- **P2** — subjective symptom language can ground clinician shorthand (S\* + tags), never objective/measured claims.
- **P3** — strict numeric bounds, no tolerance conventions.

The locator candidate worksheet produced by the mining pass is committed at [labels/attestation_labelling_worksheet.csv](labels/attestation_labelling_worksheet.csv) and is exactly regenerable from the source datasets via [tools/mine_attestations.py](tools/mine_attestations.py) (locates candidates only; assigns nothing).

## Current labelled data — three batches (219 rows, single-rater)

| Batch | Rows | S | S\* | I | C | Guidelines |
|---|---:|---:|---:|---:|---:|---|
| SN40 — primock57 safety-netting | 39 | 20 | 3 | 7 | 9 | v1.1 |
| Consent121 — ACI-Bench consent | 121 | 86 | 0 | 35 | 0 | v1.2 |
| ACISN75 — ACI-Bench safety-netting | 59 | 47 | 4 | 2 | 6 | v1.3 |
| **Total** | **219** | 153 | 7 | 44 | 15 | |

See [docs/CLINVERITAS_BATCH_STATUS_v1.3.md](docs/CLINVERITAS_BATCH_STATUS_v1.3.md) and each batch's adjudication summary under [labels/](labels/). Consent121 additionally has an [independent arithmetic-verification note](labels/consent121/CONSENT121_INDEPENDENT_VERIFICATION.md) (not a second rater).

### One headline the human labels already support

Human-labelled, protocol-governed: of the safety-netting and consent candidate lines in gold clinical notes, a substantial fraction are **not** cleanly supported by the transcript (Insufficient or Contradicted) — e.g. 16/39 in the primock57 safety-netting batch. These are single-rater figures pending κ, but they are labels, not locator ceilings.

## Experiments

- **E1 (done, pilot)** — automated-rater over the 219 rows; 3-way accuracy 0.840, **insufficient-F1 0.708**. See [e1/runs/e1/E1_RESULTS_AUTOMATED_RATER_PILOT.md](e1/runs/e1/E1_RESULTS_AUTOMATED_RATER_PILOT.md).
- **E1b (done, prompt-sensitivity)** — a prompt tweak fixed an S/S\* labelling artefact but *regressed* insufficient-F1 to 0.386; a cautionary result about coarse metrics. See [E1b results](e1/runs/e1b/E1b_RESULTS_PROMPT_CONTROLLED_AUTOMATED_RATER.md) and the [E1→E1b summary](e1/runs/e1b/E1_E1b_PROMPT_SENSITIVITY_SUMMARY.md).
- **E1c (done, 20-row pilot)** — a consent-specific rule repairs E1b's regression on a consent-heavy slice (in-sample tuned). See [E1c results](e1/runs/e1c/E1c_RESULTS_CONSENT_STRESS_PILOT.md).
- **E2 (planned)** — ISR verifier transfer from [ntkmirror](https://arxiv.org/abs/2509.11208) / [isr-code-grounding](https://github.com/Hc1012/isr-code-grounding) to clinical text.
- **E3 (planned)** — dispersion-as-groundedness signal from [order-dispersion-scaling](https://github.com/Hc1012/order-dispersion-scaling); does it detect negation reversals?
- **E4 (planned)** — error/verifier performance by note section.

> **Run provenance:** the E1/E1b/E1c rater was **OpenAI ChatGPT via its chat interface** (not a pinned-version API run), with blind chunked inputs in sessions separate from gold-label analysis; account-level memory effects cannot be ruled out. These are prompt-sensitivity experiments, not a controlled multi-model benchmark and not κ. Full details, including exactly what these runs may and may not be reported as: [RUN_PROVENANCE.md](RUN_PROVENANCE.md).

All E1 numbers are reproducible from the repo root: `python tools/recompute_e1_metrics.py` (add `--by-batch` for per-batch insufficient-F1).

## Data & licensing

Source datasets, both **CC BY 4.0**:
- **ACI-Bench** — Yim et al., *Aci-bench: a novel ambient clinical intelligence dataset for benchmarking automatic visit note generation*, Nature Scientific Data (2023). Cited per the dataset's terms for any subset use.
- **primock57** — Papadopoulos Korfiatis et al., *PriMock57: A Dataset of Primary Care Mock Consultations*, ACL (2022).

This repository redistributes excerpts and derived claim decompositions under the same CC BY 4.0 terms, with modifications noted — see [docs/DATA_LICENSES.md](docs/DATA_LICENSES.md). primock57 consultation checklists are excluded from the evidence universe by protocol (R10). Related: Asgari et al., npj Digital Medicine (2025) on AI-scribe error taxonomy; FEVER (Thorne et al., 2018) for the three-way framing.

**Evaluation-set contamination note:** the 219-row blind and gold files are committed publicly. This means the set has a contamination shelf-life (it may be ingested by future training runs). A genuine held-out slice is kept unpublished for out-of-sample evaluation, and the κ second rater works only from a packet, not this repo.

## Repository layout

```
README.md · LICENSE · CITATION.cff · RUN_PROVENANCE.md · .gitignore

guidelines/   frozen protocol v1 (R1–R10, P1–P3), amendments v1.1–v1.3, worked examples
labels/       the 219 single-rater adjudicated rows
  sn40/         primock57 safety-netting (FIXED + ADJUDICATED CSVs, changelog, summary)
  consent121/   ACI-Bench consent (CSV, summary, independent verification note)
  acisn75/      ACI-Bench safety-netting (CSV, summary)
  attestation_labelling_worksheet.csv   locator candidate worksheet (mining output)
e1/           the E1 evaluation
  clinveritas_E1_model_input_BLIND_WITH_TEXT.jsonl   send to models (no labels)
  clinveritas_E1_gold_labels_WITH_TEXT.jsonl         answer key (public; never include in model inputs)
  clinveritas_E1_index.csv · README_E1_DATASET_v2.md
  prompts/      the three verbatim prompts (E1, E1b, E1c)
  runs/e1|e1b|e1c/   per-run predictions, score reports, results docs
  baselines/    majority-S sanity baseline
tools/        mine_attestations.py · score_E1_predictions.py ·
              make_majority_baseline_predictions.py · recompute_e1_metrics.py
docs/         project scope · batch status · data licences
```

## Provenance & AI-assistance disclosure

**All gold labels, adjudications, and precedent decisions are human-assigned by the author** under the frozen protocol; a second-rater κ study is planned before release. The committed `*_PREDICTIONS_*.jsonl` files are **model outputs under evaluation, not ground truth** — no benchmark gold label is model-assigned. LLM assistance (Claude, Anthropic) was used for pipeline scaffolding, candidate *location* (per R1, locators never assign labels), audit assistance, and document drafting; the E1/E1b/E1c automated rater was ChatGPT (see [RUN_PROVENANCE.md](RUN_PROVENANCE.md)).

## Part of a research line

[ntkmirror-isr-calibration](https://github.com/Hc1012/ntkmirror-isr-calibration) → [order-dispersion-scaling](https://github.com/Hc1012/order-dispersion-scaling) → [isr-code-grounding](https://github.com/Hc1012/isr-code-grounding) → [RepoVeritas](https://github.com/Hc1012/RepoVeritas) → [ntk-scaling-experiments](https://github.com/Hc1012/ntk-scaling-experiments) → **ClinVeritas**

## Citation

See [CITATION.cff](CITATION.cff). Cite this repository and both source datasets (ACI-Bench citation is required by its terms for any subset use).

## License

Code: MIT. Data excerpts and annotations: CC BY 4.0 (inherited from and attributing ACI-Bench and primock57).
