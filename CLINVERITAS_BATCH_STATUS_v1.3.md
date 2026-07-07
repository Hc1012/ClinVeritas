# ClinVeritas — Batch Status v1.3

Date: 06 Jul 2026 (status note); repo now public.

This status note summarises the three committed single-rater adjudicated batches. It is an
internal project-status document, **not** a benchmark release and **not** κ evidence. (The
repository is now public; treat everything here as work-in-progress, not a final dataset.)

## Current labelled batches

| Batch | Version | Candidate rows | Included rows | Excluded rows | S | S* | I | C | Status |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SN40 primock57 safety-netting | v1.1 | 40 | 39 | 1 | 20 | 3 | 7 | 9 | adjudicated single-rater; κ pending |
| Consent121 ACI-Bench consent | v1.2 | 121 | 121 | 0 | 86 | 0 | 35 | 0 | adjudicated single-rater; κ pending |
| ACISN75 ACI-Bench safety-netting | v1.3 | 75 | 59 | 16 | 47 | 4 | 2 | 6 | adjudicated single-rater; κ pending |

## Totals across included rows

| Included rows | S | S* | I | C |
|---:|---:|---:|---:|---:|
| 219 | 153 | 7 | 44 | 15 |

Candidate rows screened: **236**
Rows excluded/retyped/rescope-needed: **17**
Included labelled rows: **219**

These 219 rows are the E1 evaluation set (see `README_E1_DATASET_v2.md`).

## Interpretation guardrails

- These are **single-rater adjudicated labels**, not final benchmark labels.
- The next credibility step is a seeded, batch-stratified second-rater κ study.
- Locator rows are candidates, not findings. Excluded/retyped rows demonstrate why candidate
  mining must be separated from human labelling.
- ACISN75 v1.3 excludes 16 pure retype / locator-false-positive rows from safety-netting headline
  statistics.
- SN40 v1.1 excludes/rescopes 1 contaminated source row.
- Consent121 v1.2 includes all 121 candidate rows.

## Recommended next step

Create a second-rater packet using a seeded, batch-stratified subsample across all three batches:

- SN40: sample from 39 included rows.
- Consent121: sample from 121 included rows.
- ACISN75: sample from 59 included rows.
- Keep gold labels hidden from rater 2 (rater 2 works from a packet, does not browse this repo).
- Commit the seed and sampling script before rater 2 labels.
