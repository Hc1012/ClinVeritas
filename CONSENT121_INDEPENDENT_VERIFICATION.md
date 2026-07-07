# CONSENT121 — Independent Verification Note

Date: 06 Jul 2026
Verified file: `consent121_ADJUDICATED_v1_2.csv` (121 rows)
Method: automated consistency verification and derived statistics, performed by the assisting LLM against the committed file and the original locator worksheet.

**This is not a second-rater pass.** It provides no inter-rater evidence and does not substitute for the planned κ study. It verifies arithmetic, internal consistency, and anchor-case fidelity, and computes locator-instrument statistics that require final labels.

## 1. Count verification — PASS

| Check | Summary claims | File shows | Status |
|---|---|---|---|
| Total rows | 121 | 121 | ✅ |
| Included in final stats | 121 (none excluded) | 121, `include_in_final_stats=YES` on all | ✅ |
| S | 86 | 86 | ✅ |
| S* | 0 | 0 | ✅ |
| I | 35 | 35 | ✅ |
| C | 0 | 0 | ✅ |

## 2. Internal consistency — PASS

- No invalid primary labels (all ∈ {S, S*, I, C}).
- All 35 I-rows carry severity; distribution: 35 × `relevant` (consistent with Consent-A2's default).
- `qc_status = ADJUDICATED_v1.2_FINAL` uniformly; no packaging/contamination statuses (consistent with the summary's claim that no SN40-row-37 analogue was found).
- `component_decomposition` used on 72/121 rows — mixed-claim rows were the norm, consistent with failure pattern 4 in the adjudication summary.
- Anchor case C005 confirmed: `label_primary = S`, claim text "All questions were answered.", rater note records the v1.2 QC correction (narrow question-answer standard, per Consent-A1).

SN40 passed the equivalent verification on 05 Jul 2026 (39 included; C 9 / S 20 / I 7 / S* 3; severity breakdown matched).

## 3. Locator-instrument statistics (first computable with final labels)

Join: committed labels × original mining-pass locator status (candidate agreement utterance present/absent per encounter).

| | Final S | Final I | Total |
|---|---:|---:|---:|
| Locator hit | 62 | 10 | 72 |
| Locator no-hit | 24 | 25 | 49 |
| Total | 86 | 35 | 121 |

Read as a naive classifier (hit→Supported, no-hit→Insufficient), the lexical locator scores **71.9% accuracy (87/121)** with errors in both directions:

- **Paraphrase gap (false Insufficient): 24/49 no-hit rows (49%) were in fact Supported** — agreement expressed colloquially or by paraphrase that keyword patterns cannot see (the "you got it" class). This is the first quantified estimate of the paraphrase gap predicted at guideline development (R1's origin).
- **Generic-acknowledgement gap (false Supported): 10/72 hit rows (14%) were in fact Insufficient** — an agreement-shaped utterance was present but did not constitute plan uptake (the Consent-A2 class).

Consequence for method discipline: had the mining-pass ceilings been reported as findings, ungrounded consent would have been overstated at 49/121 (40.5%) versus the human-labelled **35/121 (28.9%)** — a ~40% relative inflation. The "candidates, not findings" rule prevented a materially wrong headline in both magnitude and composition.

Forward relevance: these two error directions are the concrete floor for E2's lexical-baseline comparison — any semantic verifier must beat 71.9% on this batch to justify itself, and its gains should come specifically from the paraphrase and generic-acknowledgement cells.

## 4. Caveats

Single-rater labels throughout; all figures pending the κ study. The locator statistics characterise one specific regex instrument (frozen with Guidelines v1) and are not a general claim about lexical methods beyond this corpus.
