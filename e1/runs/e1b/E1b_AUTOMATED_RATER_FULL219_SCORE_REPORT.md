# E1b Automated-Rater Full-219 Score Report

## File selection

| Expected range | Selected file | Candidate files found |
|---|---|---:|
| 001-020 | E1b_OUTPUT_ROWS_001_020(1).jsonl | 1 |
| 021-040 | E1b_OUTPUT_ROWS_021_040(1).jsonl | 1 |
| 041-060 | E1b_OUTPUT_ROWS_041_060(1).jsonl | 1 |
| 061-080 | E1b_OUTPUT_ROWS_061_080(1).jsonl | 1 |
| 081-100 | E1b_OUTPUT_ROWS_081_100(1).jsonl | 1 |
| 101-120 | E1b_OUTPUT_ROWS_101_120(1).jsonl | 1 |
| 121-140 | E1b_OUTPUT_ROWS_121_140(1).jsonl | 1 |
| 141-160 | E1b_OUTPUT_ROWS_141_160(1).jsonl | 1 |
| 161-180 | E1b_OUTPUT_ROWS_161_180(1).jsonl | 1 |
| 181-200 | E1b_OUTPUT_ROWS_181_200(1).jsonl | 1 |
| 201-219 | E1b_OUTPUT_ROWS_201_219(1).jsonl | 1 |

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

## Overall strict 4-way score

- Scored rows: 219 / 219
- Accuracy: 0.776
- Macro-F1: 0.541
- Gold label counts: {'C': 15, 'S': 153, 'I': 44, 'S*': 7}
- Prediction label counts: {'C': 12, 'S': 193, 'I': 13, 'S*': 1}

## Comparison with E1 original automated-rater run

| Run | Accuracy | Macro-F1 | Prediction counts |
|---|---:|---:|---|
| E1 original prompt | 0.475 | 0.452 | {'I': 52, 'C': 6, 'S*': 94, 'S': 67} |
| E1b prompt-controlled | 0.776 | 0.541 | {'C': 12, 'S': 193, 'I': 13, 'S*': 1} |

## Per-label metrics

| Label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| S | 0.772 | 0.974 | 0.861 | 153 |
| S* | 1.000 | 0.143 | 0.250 | 7 |
| I | 0.846 | 0.250 | 0.386 | 44 |
| C | 0.750 | 0.600 | 0.667 | 15 |
| Macro | — | — | 0.541 | — |

## Confusion matrix

Rows = gold label, columns = predicted label.

| Gold \ Pred | S | S* | I | C |
|---|---:|---:|---:|---:|
| S | 149 | 0 | 1 | 3 |
| S* | 6 | 1 | 0 | 0 |
| I | 33 | 0 | 11 | 0 |
| C | 5 | 0 | 1 | 9 |

## Collapsed grounded-vs-ungrounded score

- Grounded = `S` or `S*`
- Ungrounded = `I` or `C`

- Binary accuracy: 0.808
- Binary macro-F1: 0.691

| Binary label | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| grounded | 0.804 | 0.975 | 0.881 | 160 |
| ungrounded | 0.840 | 0.356 | 0.500 | 59 |

## Chunk scores

| Chunk | Scored | Accuracy | Gold counts | Prediction counts |
|---|---:|---:|---|---|
| 001-020 | 20 | 0.900 | {'C': 5, 'S': 6, 'I': 7, 'S*': 2} | {'C': 5, 'S': 8, 'I': 6, 'S*': 1} |
| 021-040 | 20 | 0.650 | {'C': 4, 'S': 14, 'S*': 1, 'I': 1} | {'S': 18, 'C': 1, 'I': 1} |
| 041-060 | 20 | 0.800 | {'S': 15, 'I': 5} | {'S': 19, 'I': 1} |
| 061-080 | 20 | 0.700 | {'S': 13, 'I': 7} | {'S': 19, 'I': 1} |
| 081-100 | 20 | 0.850 | {'S': 17, 'I': 3} | {'S': 20} |
| 101-120 | 20 | 0.650 | {'S': 12, 'I': 8} | {'S': 19, 'I': 1} |
| 121-140 | 20 | 0.800 | {'S': 16, 'I': 4} | {'S': 20} |
| 141-160 | 20 | 0.600 | {'I': 7, 'S': 13} | {'S': 19, 'I': 1} |
| 161-180 | 20 | 0.800 | {'S': 17, 'C': 3} | {'S': 17, 'C': 3} |
| 181-200 | 20 | 0.900 | {'S': 16, 'S*': 2, 'I': 1, 'C': 1} | {'S': 18, 'I': 1, 'C': 1} |
| 201-219 | 19 | 0.895 | {'S': 14, 'I': 1, 'C': 2, 'S*': 2} | {'S': 16, 'I': 1, 'C': 2} |

## Batch scores

| Batch | N | Accuracy | Gold counts | Prediction counts |
|---|---:|---:|---|---|
| acisn75 | 59 | 0.864 | {'S': 47, 'C': 6, 'S*': 4, 'I': 2} | {'S': 51, 'C': 6, 'I': 2} |
| consent121 | 121 | 0.727 | {'I': 35, 'S': 86} | {'S': 117, 'I': 4} |
| sn40 | 39 | 0.795 | {'C': 9, 'S': 20, 'I': 7, 'S*': 3} | {'C': 6, 'S': 25, 'I': 7, 'S*': 1} |

## Candidate-type scores

| Candidate type | N | Accuracy | Gold counts | Prediction counts |
|---|---:|---:|---|---|
| consent | 121 | 0.727 | {'I': 35, 'S': 86} | {'S': 117, 'I': 4} |
| safety-netting | 98 | 0.837 | {'C': 15, 'S': 67, 'I': 9, 'S*': 7} | {'C': 12, 'S': 76, 'I': 9, 'S*': 1} |

## Main disagreement patterns

| Gold → Pred | Count |
|---|---:|
| I → S | 33 |
| S* → S | 6 |
| C → S | 5 |
| S → C | 3 |
| C → I | 1 |
| S → I | 1 |
