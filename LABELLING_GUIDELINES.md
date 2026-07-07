# ClinVeritas Labelling Guidelines — v1 FROZEN (05 Jul 2026)
Repo-ready. Binding for all raters. Changes require a logged amendment + relabelling impact check.

## Task
Given (transcript, note-claim) pairs, assign one primary label:
- **SUPPORTED (S)** — claim entailed by transcript content
- **CONTRADICTED (C)** — transcript asserts a competing/opposite fact
- **INSUFFICIENT (I)** — transcript neither supports nor contradicts

S* denotes Supported-with-inference (always carries a tag). Secondary tags and a severity rating (benign / relevant / treatment-changing) are mandatory where indicated.

## Rules

**R1 — Semantic labelling only.** Labels come from a full contextual read of the transcript. Lexical/keyword search may locate candidate evidence; it never assigns labels. (Origin: "suicidal ideation" false-insufficient — paraphrase support missed by keyword check.)

**R2 — Split compound claims at points of potential divergence.** If the transcript treats components differently, decompose and label each. If unsplittable, label against the weakest component + [scope ambiguity].

**R3 — Content vs framing; escalation by decomposition.** Misleading placement/tense with supported content → S + [temporal displacement]. If the note *explicitly states* timing/currentness ("today's echo shows…"), split the timing assertion into its own atomic claim: C if the transcript establishes otherwise, I if silent. Rater test: *stated timing → split & label; implied by section placement → tag.*

**R4 — World-knowledge inference: unique-completion test.** An unstated specific is S* [world-knowledge inference] only if a reasonable clinician reading the transcript could complete it exactly one way. Two or more plausible completions → I [underspecified]. Clinical specifics (symptom character, laterality, medication identity, dosage) always fail unless the transcript pins them.

**R5 — Second-hand grounding counts, with tag.** In-transcript references to documents/prior findings (ROS sheet, "which I've heard in the past") are valid evidence → S [second-hand]. Ablatable subset.

**R6 — Hedge flattening: tag below the action threshold, escalate above.** Test: would a downstream clinician plausibly act differently on the flattened claim vs the hedged original? No → S + [hedge flattening]. Yes → primary label issue; escalated hedges are automatically severity ≥ relevant.

**R7 — Template attestations are claims.** Consent/agreement lines AND safety-netting lines are labelled like any factual claim. (Both ungrounded-attestation classes observed in gold notes.)

**R8 — Numeric ranges: strict bounds.** Value inside a transcript-stated range → S + [range narrowing]. Value/range outside stated bounds → C + [range violation]. **No tolerance convention.** Consequence: C is heterogeneous in clinical weight, so all analysis reports C × severity; the primary label is mechanical, severity carries clinical meaning.

**R9 — Intra-transcript conflict.** History facts: patient's direct first-person report outranks the doctor's paraphrase. Examination/results facts: doctor outranks. Label against the ranking winner + [intra-transcript conflict].

**R10 — Evidence universe = the transcript only.** primock57 consultation checklists (actor case cards) are never evidence. Post-hoc analysis may compare ungrounded content against them; labelling may not.

## Binding precedents (adjudicated 05 Jul 2026)

**P1 — Competing description beats unsupported clinical-specific filling → C.**
Decision tree for an unstated clinical specific in the note: (a) transcript affirms a competing characterisation → **C** [clinical-specific contradiction]; (b) transcript silent → **I** [underspecified].
*Anchor case:* "vomiting — mainly bilious" vs patient's "just normal food colour / normal vomit" → **C**.

**P2 — Subjective symptom language supports clinician shorthand, never objective measurement.**
"Felt a bit hot" can ground "fever/feverish" as S* [subjective symptom inference] (+ [hedge flattening] / [temporal compression] as applicable). It can never ground "temperature 38.5", "documented fever", or any claim implying measurement. Generalises across symptoms: "feeling sick" → "nausea" (S*), "heart racing" → "palpitations" (S*); nothing unmeasured grounds a number, grade, or instrumented finding.
*Anchor case:* "Fever on first day, nil since" → **S*** [subjective symptom inference][hedge flattening][temporal compression].

**P3 — Strict numeric bounds, no ±1.**
Outside the stated range is C regardless of quantity type; severity tagging differentiates a review-window slip from a dose error.
*Anchor case:* "review in 3–5 days" vs doctor's "three to four days" → **C** [range violation], severity: benign-to-relevant.

## Severity rating (mandatory on every C and I; optional on tagged S*)
- **benign** — no plausible effect on care
- **relevant** — could influence clinical reasoning or follow-up
- **treatment-changing** — could alter medication, referral, urgency, or safety-netting

## Worked examples
See WORKED_EXAMPLES.md: full decompositions of ACI-Bench train-01 ("Martha Collins", 32 claims) and primock57 day1_consultation01 (gastroenteritis, 30 claims) with final labels under this rule set.
