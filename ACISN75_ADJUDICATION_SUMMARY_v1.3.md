# ACISN75 — Adjudication Summary v1.3

Date: 06 Jul 2026  
Batch: ACI-Bench safety-netting candidates, ASN001–ASN075  
Input file: `acisn75_ALL_WORKING_PASS.csv`  
Output file: `acisn75_ADJUDICATED_v1_3.csv`

## Status

QC/adjudication pass complete under ClinVeritas Guidelines v1 plus Amendments v1.1, v1.2, and v1.3.

No primary S/C/I/S* labels were changed during adjudication. The working-pass labels were internally consistent with v1.3. The main adjudication action was candidate-type cleanup: pure locator false positives were retained in the file but excluded from the ACISN75 safety-netting headline statistics.

## v1.3 rules applied

- Mixed-row aggregate ordering: **C > I > S* > S**.
- Safety-netting class tags:
  - `[patient-directed safety-netting]`
  - `[clinician contingency plan]`
- Diarisation/speaker-swap handling:
  - use role/context attribution when clear
  - tag affected rows with `[transcript diarisation error]`

## Candidate-type adjudication

The packet contained 75 locator candidate rows. Human review found 16 pure retype/false-positive rows that are valid supported note claims but are not safety-netting claims.

These rows are excluded from ACISN75 safety-netting headline statistics and retained for locator false-positive analysis:

`ASN002, ASN004, ASN006, ASN012, ASN014, ASN017, ASN020, ASN030, ASN037, ASN041, ASN045, ASN051, ASN053, ASN055, ASN058, ASN061`

Two mixed rows that contain both non-safety-netting material and genuine safety-netting components remain included:

`ASN008`, `ASN015`

## Final ACISN75 safety-netting statistics

Included safety-netting rows: **59**  
Excluded pure retype candidates: **16**

| Label | Count |
|---|---:|
| S | 47 |
| S* | 4 |
| I | 2 |
| C | 6 |
| Total included | 59 |

Ungrounded/failed rows under S/C/I framing:

- **I:** 2/59
- **C:** 6/59
- **C + I:** 8/59

All C/I rows carry severity.

## Candidate-level locator audit counts

If all 75 locator candidates are counted regardless of candidate-type validity, the working label distribution is:

| Label | Count |
|---|---:|
| S | 63 |
| S* | 4 |
| I | 2 |
| C | 6 |
| Total candidates | 75 |

Interpretation: the safety-netting locator produced 16 pure false-positive candidate rows that should not inflate supported safety-netting counts.

## C and I rows

### Contradicted

| Row | Severity | Short reason |
|---|---|---|
| ASN021 | relevant | Trigger broadened from worsening swelling/if needed to non-improvement. |
| ASN023 | relevant | Possible MRI if needed becomes definite MRI. |
| ASN024 | relevant | Possible future x-ray becomes definite future order. |
| ASN050 | relevant | Follow-up route/sooner clause differs from transcript. |
| ASN062 | treatment-changing | ED escalation threshold compressed from multi-dose nitroglycerin protocol to one short interval. |
| ASN063 | relevant | MRI trigger broadened from worsening/call-office pathway to non-improvement with immobilizer. |

### Insufficient

| Row | Severity | Short reason |
|---|---|---|
| ASN036 | relevant | Next-year follow-up is supported, but renal ultrasound at follow-up is not pinned. |
| ASN057 | relevant | PT/more aggressive treatment is supported, but x-ray as the next contingency is not pinned. |

## S* rows

| Row | Reason |
|---|---|
| ASN033 | Minor temporal generalisation. |
| ASN042 | Steroid injection → cortisone injection synonym/world-knowledge inference. |
| ASN065 | Minor scope generalisation. |
| ASN074 | Scope narrowing. |

## Integrity flags

Rows tagged `[transcript diarisation error]`:

`ASN009`, `ASN019`, `ASN037`, `ASN041`, `ASN047`

Rows ASN037 and ASN041 are also pure retype candidates and therefore excluded from headline safety-netting statistics.

No source-contamination analogue to SN40 row 37 was adjudicated as requiring exclusion on safety-netting evidence grounds in the included rows.

## Caveats

- This is still a single-rater batch. It is not a κ study and does not substitute for second-rater reliability.
- Class-split reporting by `[patient-directed safety-netting]` vs `[clinician contingency plan]` is preserved in tags, but mixed rows require component-level aggregation for a publication-ready class-specific table.
- SN40 retro-tagging remains a future cleanup task if cross-dataset safety-netting class splits are desired.
