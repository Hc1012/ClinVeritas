# ClinVeritas Guidelines Amendment v1.3 — ACI-Bench Safety-Netting (ACISN)

Date: 06 Jul 2026
Scope: ratified before labelling of the ACI-Bench safety-netting batch (ACISN75). ACISN-A1 applies batch-wide to all current and future batches. ACISN-A2 applies to all safety-netting batches. ACISN-A3's practical scope is ACI-Bench transcripts (see structural note). This amendment does not replace Labelling Guidelines v1, Amendment v1.1, or Amendment v1.2; it extends them.

## ACISN-A1 — Mixed-row ordering generalised batch-wide

The row-level label used in summary counts is the strongest unsupported/contradicted clinically relevant component, ordered:

**C > I > S* > S**

This generalises Consent-A4 beyond the consent batch to all batches. All sub-claim labels are preserved in `component_decomposition`; the ordering governs only the row-level aggregate.

**Relabelling impact check (performed 06 Jul 2026):** none.
- SN40: 16 mixed-component rows machine-checked against the ordering; 0 violations.
- consent121: ordering was the batch's native rule (Consent-A4); the 2 rows using labelled `(a)=X; (b)=Y` component notation machine-checked; 0 violations. Remaining `component_decomposition` entries are free-prose evidence commentary without per-component labels and are not affected by this amendment.

## ACISN-A2 — Safety-netting claim-class tags

Every safety-netting claim (and each component of a mixed row) carries exactly one class tag:

- **[patient-directed safety-netting]** — advice given to the patient about when/how to seek help (e.g. call/return/seek help if worse).
- **[clinician contingency plan]** — the clinician's stated future plan conditional on an event (e.g. if pain doesn't improve, recommend injection).

The grounding question differs by class: for patient-directed safety-netting, whether the advice was **given** to the patient; for a clinician contingency plan, whether the contingency was **stated/discussed**. Headline safety-netting statistics are reported **overall and split by claim class**.

Naming: these v1.3 tag strings supersede the interim README strings `[patient-directed SN]` and `[contingency-plan]`; only the v1.3 strings are valid in labelled data.

**Relabelling impact:** ACISN75 unlabelled at ratification — none. **Open decision (logged):** optional retro-tagging of SN40's 39 included rows (tags only; labels and severities untouched) would enable the cross-dataset class split; until decided, the class-split statistic is reported for ACI-Bench only.

## ACISN-A3 — Transcript diarisation errors and speaker attribution

Where speaker tags are manifestly inconsistent with conversational role (e.g. a "[doctor]" turn reporting the speaker's own symptoms), attribute utterances by role/context and tag the row **[transcript diarisation error]**. R9 rankings and all speaker-dependent rules (P2, R5, Consent-A2 uptake judgements) follow the **true role**, never the printed tag.

If the intended speaker cannot be determined with confidence, do **not** guess: label conservatively on the available evidence and set `ADJUDICATION_QUEUE` in `rater_notes`.

Tag scoping convention (operational): **[transcript diarisation error]** is the specific tag for speaker-swap defects. **[source integrity flag]** is the general family tag for other source-data defects (note contamination, body duplication, field misalignment — the SN40 rows 37/28/39 classes) and may co-occur with the specific tag where multiple defects apply.

Structural note: primock57 transcripts derive from separate per-speaker TextGrid files, so speaker attribution there is reliable by construction; diarisation error is an ACI-Bench-transcript phenomenon. Known instance at ratification: ASN019 (`train-D2N057-aci`), opening tags swapped.

**Relabelling impact:** none on committed batches — primock57 is structurally unaffected, and no diarisation-driven labels were flagged during consent121 QC.
