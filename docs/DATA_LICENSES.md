# Data licences & attribution

ClinVeritas builds on two source datasets, both licensed **Creative Commons Attribution 4.0 International (CC BY 4.0)**: https://creativecommons.org/licenses/by/4.0/

## Sources

**ACI-Bench** — Wen-wai Yim, Yujuan Fu, Asma Ben Abacha, Neal Snider, Thomas Lin, Meliha Yetisgen. *Aci-bench: a novel ambient clinical intelligence dataset for benchmarking automatic visit note generation.* Scientific Data (2023).
Repository: https://github.com/wyim/aci-bench — data published under CC BY 4.0 (see that repository's License section). Per the dataset's terms, the paper above should be cited for use of the full dataset **or any subset**.

**PriMock57** — Alex Papadopoulos Korfiatis, Francesco Moramarco, Radmila Sarac, Aleksandar Savkov. *PriMock57: A Dataset of Primary Care Mock Consultations.* Proceedings of ACL (2022).
Repository: https://github.com/babylonhealth/primock57 — licensed CC BY 4.0 (LICENSE.md in that repository).

## What ClinVeritas redistributes from these sources

- Excerpts of consultation transcripts and clinician notes (worksheet candidate/evidence columns; worked-example tables)
- Derived claim decompositions of notes into atomic claims
- Human annotation labels, severity ratings, and tags attached to that material

**Not redistributed:** primock57 audio recordings; primock57 consultation checklists (the actor case cards) — the latter are additionally excluded from the labelling evidence universe by protocol (Guidelines v1, Rule R10).

## Changes made (per CC BY 4.0 §3(a)(1)(B))

- Excerpting and truncation of note and transcript text
- Conversion of primock57 TextGrid transcripts to plain text using the dataset's own `textgrid_to_transcript.py`
- Segmentation of notes into atomic claims
- Addition of annotation labels, severity ratings, tags, and rater notes (ClinVeritas annotations)

## Licences within this repository

- **Code** (`mine_attestations.py` and pipeline scripts): MIT
- **Data excerpts, claim decompositions, and annotations**: CC BY 4.0, attributing the sources above

If you use ClinVeritas, please cite this repository and both source datasets (ACI-Bench citation is required by its terms for any subset use).
