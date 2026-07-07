# ClinVeritas Consent121 — Adjudication Summary v1.2

Batch: ACI-Bench consent-attestation candidates (`consent121`).

Input: `consent121_ALL_WORKING_PASS.csv`  
Output: `consent121_ADJUDICATED_v1_2.csv`

## What changed in QC

Only one label changed during adjudication:

| Row | Working label | Final label | Reason |
|---|---:|---:|---|
| C005 | I | S | The note claim is only `All questions were answered`. The transcript shows the patient asked whether tramadol was okay with digoxin, the clinician answered, then the patient denied further questions. The earlier working pass wrongly applied the stronger global-agreement standard to a narrow question-answer claim. |

No rows were excluded. No packaging contamination analogous to SN40 row 37 was found in this batch during the label-level QC pass.

## Final included counts

| Label | Count |
|---|---:|
| S | 86 |
| S* | 0 |
| I | 35 |
| C | 0 |
| Total | 121 |

Final headline for this batch:

**35 / 121 ACI-Bench consent-attestation candidates are Insufficient under the v1.2 consent rules.**

These are still single-rater labels until a second-rater/κ pass is completed.

## Main adjudication rule added

The batch forced a consent-specific distinction:

- `All questions were answered` is a narrow question-answer claim and can be Supported without proving whole-plan agreement.
- `Patient understands and agrees with the recommended medical treatment plan` is a broad consent/agreement attestation and needs clear plan uptake, not merely generic `okay`, `thanks`, or `no questions`.

This is codified in `GUIDELINES_AMENDMENT_v1.2_CONSENT.md`.

## Failure pattern

All final failures are **Insufficient**, not Contradicted. They cluster around:

1. generic acknowledgements used to support broad `understands/agrees` template language;
2. rows where questions were answered but whole-plan agreement was not established;
3. broad risk/benefit or signed-consent attestations not grounded in the transcript;
4. mixed rows where supported sub-claims coexist with unsupported consent components.

## Files to commit

Recommended folder:

```text
labels/consent121/
```

Files:

- `consent121_ADJUDICATED_v1_2.csv`
- `GUIDELINES_AMENDMENT_v1.2_CONSENT.md`
- `CONSENT121_ADJUDICATION_SUMMARY_v1.2.md`

Suggested commit message:

```text
Adjudicate ACI-Bench consent121 labels under guidelines v1.2
```
