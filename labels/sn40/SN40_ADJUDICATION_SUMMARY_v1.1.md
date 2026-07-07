# SN40 Adjudication Summary v1.1

Input file: `clinveritas_sn40_labelled_FIXED.csv`  
Output file: `clinveritas_sn40_labelled_ADJUDICATED_v1_1.csv`  
Guideline amendment: `GUIDELINES_AMENDMENT_v1.1.md`

## What changed

- Resolved all 8 `PENDING_ADJUDICATION` rows using v1.1 amendments A1–A5.
- No pending-row labels flipped; the labels were kept and converted to `FINAL_ADJUDICATED_v1.1`.
- Row 37 remains `EXCLUDE_OR_RESCOPE` and is not counted in final SN40 stats.
- Rows 28 and 39 remain label-usable and are included in stats, but their source packet/extraction notes need cleanup before public release.

## Final count, excluding row 37

| Label | Count |
|---|---:|
| S | 20 |
| S* | 3 |
| I | 7 |
| C | 9 |
| **Included total** | 39 |
| Excluded/rescope-needed | 1 |

## C/I severity breakdown, excluding row 37

| Label | Severity | Count |
|---|---|---:|
| C | benign (a) / relevant (b) | 1 |
| C | relevant | 6 |
| C | treatment-changing | 2 |
| I | benign | 3 |
| I | relevant | 4 |

## Rows adjudicated

| Row | Encounter | Final label | Amendment | Decision |
|---:|---|---|---|---|
| 4 | day1_consultation05 | C | A1 | FINAL_KEEP_C |
| 8 | day1_consultation09 | I | A1 | FINAL_KEEP_I |
| 17 | day2_consultation07 | I | A3 | FINAL_KEEP_I |
| 21 | day3_consultation03 | C | A2 | FINAL_KEEP_C |
| 22 | day3_consultation04 | S | A1 | FINAL_KEEP_S |
| 23 | day3_consultation05 | C | A5 | FINAL_KEEP_C |
| 32 | day5_consultation04 | C | A3 | FINAL_KEEP_C |
| 35 | day5_consultation07 | C | A4 | FINAL_KEEP_C |
| 37 | day5_consultation09 | EXCLUDE_OR_RESCOPE | RESCOPE | EXCLUDED_PENDING_RESCOPE |

## Commit recommendation

Commit these three files under `labels/sn40/` or equivalent:

- `clinveritas_sn40_labelled_ADJUDICATED_v1_1.csv`
- `SN40_ADJUDICATION_SUMMARY_v1.1.md`
- `GUIDELINES_AMENDMENT_v1.1.md`

Suggested commit message: `Adjudicate SN40 labels under guidelines v1.1`.
