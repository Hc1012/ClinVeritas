# ClinVeritas Guidelines Amendment v1.1 — SN40 adjudication

Date: 05 Jul 2026  
Scope: resolves the five amendment-queue issues raised during the primock57 safety-netting batch. These amendments are binding for SN40 finalisation and future safety-netting rows unless superseded by a logged later amendment.

## Summary of amendments

### A1 — Vague temporal quantifiers under R8

R8 remains strict for crisp numeric ranges. When the transcript uses a vague temporal phrase, apply a conventional-bounds test before labelling: (1) if local context or ordinary clinical English gives a narrow conventional range, values inside that range are S/S* with [range narrowing] or [temporal compression]; values outside all reasonable completions are C [range violation]; (2) if the phrase cannot be bounded enough for a unique completion, the note's specific value is I [underspecified temporal] unless another transcript utterance pins it. Operational convention for this batch: "a few days" = approximately 2–4 days unless local context narrows it; "end of this week" is context-dependent and does not by itself pin an exact day.

**Rows resolved:** Rows 4, 8, 22. Final rulings: row 4 C; row 8 I; row 22 S.

### A2 — Doctor-vs-doctor instruction conflicts

When the doctor gives conflicting safety-netting instructions for the same trigger, prefer the more specific, rationale-backed, safety-critical instruction over a later generic catch-all summary. If the note follows the generic instruction while suppressing the specific urgent pathway, label the affected component C and set severity according to clinical effect.

**Rows resolved:** Row 21. Final ruling: C, treatment-changing.

### A3 — Plan versus completed-action attestations

Attested completed actions are factual claims. If the note says an action was completed/booked/handed over but the transcript only establishes intention or plan, label I. If the transcript establishes a different mechanism or non-completion, label C. This extends R3's timing/currentness principle to completion state.

**Rows resolved:** Rows 17 and 32. Final rulings: row 17 I; row 32 C, treatment-changing.

### A4 — Note-side surface errors and apparent typos

Do not silently repair note text during labelling. Label the literal clinical proposition written in the note. If an apparent typo reverses or materially changes the safety-netting condition, label the literal claim on its merits and use tags such as [negation artefact] or [note-side typo]. Severity carries the clinical weight. Obvious non-clinical typos that do not alter the proposition may be ignored in notes, but not corrected into a different medical claim.

**Rows resolved:** Row 35. Final ruling: C via the literal 'not worse' condition; the separate 'up to a month' bound remains I within the decomposition.

### A5 — R6 destination label for escalated hedge/threshold flattening

When hedge flattening or threshold broadening crosses the action threshold, assign the primary label by whether the transcript asserts a competing trigger. If the transcript gives a narrower/specific trigger and the note broadens or changes it enough to alter the action pathway, label C [threshold flattening]/[clinical-specific threshold]. If the transcript is merely silent about the threshold, label I. Direction of clinical risk is captured in severity.

**Rows resolved:** Row 23. Final ruling: C, relevant.

## Row 37 exclusion/rescope note

Row 37 (`day5_consultation09`) is not an adjudication issue; it is a packaging/extraction issue. It remains excluded from final SN40 statistics until the packet/worksheet is regenerated or the correct claim is re-scoped against the correct encounter.

## Final SN40 labels after v1.1

The v1.1 adjudication did not flip any of the eight pending labels; it converted them from pending to final by adding explicit rule coverage. Row 37 remains excluded/rescope-needed.
