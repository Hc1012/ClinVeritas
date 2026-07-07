# ClinVeritas SN40 fixed file changelog

Output file: `clinveritas_sn40_labelled_FIXED.csv`

## Definite fix applied
- Row 37 (`day5_consultation09`): changed `label_primary` from `S` to `EXCLUDE_OR_RESCOPE`; cleared severity; replaced tags with `[packaging-contamination][exclude-from-stats]`; added QC notes. This row must not be counted until the packet/worksheet is regenerated or the correct claim is rescoped.

## Pending adjudication rows flagged, labels not changed
These labels remain as originally assigned but are marked `PENDING_ADJUDICATION` and should not be treated as final until the rule gap is resolved:
- Rows 4, 8, 22 — vague temporal quantifiers vs strict R8 bounds.
- Rows 17, 32 — plan-vs-completed-action attestation rule.
- Row 21 — doctor-vs-doctor instruction conflict.
- Row 23 — R6 escalated hedge/threshold-flattening destination label.
- Row 35 — note-side typo / literal-string policy.

## Packaging notes flagged, labels not changed
- Row 28 — duplicated note body in packet/extraction.
- Row 39 — presenting-complaint header mismatch in packet/extraction.

## Out-of-scope observations flagged, labels not changed
- Row 20 — transcript gap; current tag retained.
- Row 26 — paracetamol issue is outside safety-netting row scope.
- Row 38 — naproxen issue is outside safety-netting row scope.

## Fixed-file label counts
- S: 20
- S*: 3
- I: 7
- C: 9
- EXCLUDE_OR_RESCOPE: 1

## QC status counts
- OK: 26
- OK_WITH_TRANSCRIPTION_GAP_NOTE: 1
- OK_WITH_OUT_OF_SCOPE_OBSERVATION: 2
- PACKAGING_FIX_ONLY: 2
- PENDING_ADJUDICATION: 8
- EXCLUDE_OR_RESCOPE: 1
