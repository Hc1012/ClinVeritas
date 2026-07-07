# E1 Automated-Rater Full-219 Score Report

## File selection

| Expected range | Selected file | Candidate files found |
|---|---|---:|
| 001-020 | E1_OUTPUT_ROWS_001_020(1).jsonl | 1 |
| 021-040 | E1_OUTPUT_ROWS_021_040(1).jsonl | 1 |
| 041-060 | E1_OUTPUT_ROWS_041_060(1).jsonl | 1 |
| 061-080 | E1_OUTPUT_ROWS_061_080(1).jsonl | 1 |
| 081-100 | E1_OUTPUT_ROWS_081_100(1).jsonl | 1 |
| 101-120 | E1_OUTPUT_ROWS_101_120(1).jsonl | 1 |
| 121-140 | E1_OUTPUT_ROWS_121_140(1).jsonl | 1 |
| 141-160 | E1_OUTPUT_ROWS_141_160(1).jsonl | 1 |
| 161-180 | E1_OUTPUT_ROWS_161_180(1).jsonl | 1 |
| 181-200 | E1_OUTPUT_ROWS_181_200(1).jsonl | 1 |
| 201-219 | E1_OUTPUT_ROWS_201_219(1).jsonl | 1 |

## Validation

- Expected chunks: 11
- Missing chunk ranges: 0
- Parsed prediction rows total: 219
- JSON parse errors: 0
- Global duplicate eval IDs: 0
- Missing expected eval IDs: 0
- Extra eval IDs: 0
- Invalid labels: 0

### Per-file validation

| Range | Rows | JSON errors | Missing IDs | Extra IDs | Duplicate IDs | Invalid labels |
|---|---:|---:|---:|---:|---:|---:|
| 001-020 | 20 | 0 | 0 | 0 | 0 | 0 |
| 021-040 | 20 | 0 | 0 | 0 | 0 | 0 |
| 041-060 | 20 | 0 | 0 | 0 | 0 | 0 |
| 061-080 | 20 | 0 | 0 | 0 | 0 | 0 |
| 081-100 | 20 | 0 | 0 | 0 | 0 | 0 |
| 101-120 | 20 | 0 | 0 | 0 | 0 | 0 |
| 121-140 | 20 | 0 | 0 | 0 | 0 | 0 |
| 141-160 | 20 | 0 | 0 | 0 | 0 | 0 |
| 161-180 | 20 | 0 | 0 | 0 | 0 | 0 |
| 181-200 | 20 | 0 | 0 | 0 | 0 | 0 |
| 201-219 | 19 | 0 | 0 | 0 | 0 | 0 |

## Overall score

- Scored rows: 219 / 219
- Accuracy: 0.475
- Macro-F1: 0.452
- Majority-S baseline accuracy: 0.699
- Majority-S baseline macro-F1: 0.206
- Gold label counts: {'C': 15, 'S': 153, 'I': 44, 'S*': 7}
- Prediction label counts: {'I': 52, 'C': 6, 'S*': 94, 'S': 67}

## Per-label metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| S | 0.925 | 0.405 | 0.564 | 153 |
| S* | 0.032 | 0.429 | 0.059 | 7 |
| I | 0.654 | 0.773 | 0.708 | 44 |
| C | 0.833 | 0.333 | 0.476 | 15 |
| Macro | — | — | 0.452 | — |

## Confusion matrix

Rows = gold label, columns = predicted label.

| Gold \ Pred | S | S* | I | C |
|---|---:|---:|---:|---:|
| S | 62 | 78 | 12 | 1 |
| S* | 2 | 3 | 2 | 0 |
| I | 1 | 9 | 34 | 0 |
| C | 2 | 4 | 4 | 5 |

## Chunk scores

| Chunk | Scored | Accuracy | Gold counts | Prediction counts |
|---|---:|---:|---|---|
| 001-020 | 20 | 0.750 | {'C': 5, 'S': 6, 'I': 7, 'S*': 2} | {'I': 7, 'C': 3, 'S*': 5, 'S': 5} |
| 021-040 | 20 | 0.450 | {'C': 4, 'S': 14, 'S*': 1, 'I': 1} | {'C': 1, 'S*': 7, 'S': 10, 'I': 2} |
| 041-060 | 20 | 0.350 | {'S': 15, 'I': 5} | {'S*': 11, 'S': 4, 'I': 5} |
| 061-080 | 20 | 0.350 | {'S': 13, 'I': 7} | {'S*': 13, 'I': 5, 'S': 2} |
| 081-100 | 20 | 0.350 | {'S': 17, 'I': 3} | {'S*': 13, 'S': 5, 'I': 2} |
| 101-120 | 20 | 0.400 | {'S': 12, 'I': 8} | {'S*': 12, 'S': 1, 'I': 7} |
| 121-140 | 20 | 0.400 | {'S': 16, 'I': 4} | {'S*': 11, 'I': 5, 'S': 4} |
| 141-160 | 20 | 0.350 | {'I': 7, 'S': 13} | {'I': 9, 'S*': 9, 'S': 2} |
| 161-180 | 20 | 0.550 | {'S': 17, 'C': 3} | {'S': 12, 'S*': 4, 'C': 1, 'I': 3} |
| 181-200 | 20 | 0.750 | {'S': 16, 'S*': 2, 'I': 1, 'C': 1} | {'S': 14, 'S*': 3, 'I': 2, 'C': 1} |
| 201-219 | 19 | 0.526 | {'S': 14, 'I': 1, 'C': 2, 'S*': 2} | {'S*': 6, 'I': 5, 'S': 8} |

## Batch scores

| Batch | N | Accuracy | Gold counts | Prediction counts |
|---|---:|---:|---|---|
| acisn75 | 59 | 0.610 | {'S': 47, 'C': 6, 'S*': 4, 'I': 2} | {'S': 34, 'S*': 13, 'C': 2, 'I': 10} |
| consent121 | 121 | 0.364 | {'I': 35, 'S': 86} | {'S*': 70, 'S': 18, 'I': 33} |
| sn40 | 39 | 0.615 | {'C': 9, 'S': 20, 'I': 7, 'S*': 3} | {'I': 9, 'C': 4, 'S*': 11, 'S': 15} |

## Candidate-type scores

| Candidate type | N | Accuracy | Gold counts | Prediction counts |
|---|---:|---:|---|---|
| consent | 121 | 0.364 | {'I': 35, 'S': 86} | {'S*': 70, 'S': 18, 'I': 33} |
| safety-netting | 98 | 0.612 | {'C': 15, 'S': 67, 'I': 9, 'S*': 7} | {'I': 19, 'C': 6, 'S*': 24, 'S': 49} |

## Main disagreement patterns

| Gold → Pred | Count |
|---|---:|
| S → S* | 78 |
| S → I | 12 |
| I → S* | 9 |
| C → I | 4 |
| C → S* | 4 |
| C → S | 2 |
| S* → S | 2 |
| S* → I | 2 |
| I → S | 1 |
| S → C | 1 |
