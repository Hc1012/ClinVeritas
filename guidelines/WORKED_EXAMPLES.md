# ClinVeritas — Worked Examples (final labels under Guidelines v1)
Rater-training document. Both encounters fully decomposed; labels reflect adjudicated precedents P1–P3.

## Example 1 — ACI-Bench train-01 ("Martha Collins", annual exam, US)
Polished reference note. 32 atomic claims.

Key rows (full table logic identical to v0 doc, labels unchanged by adjudication):
| Claim | Label | Rule/Precedent |
|---|---|---|
| Received COVID-19 vaccine ("my vaccine… safer about traveling", pandemic-era context) | S* [world-knowledge inference] | R4 — passes unique-completion |
| "Continued utilizing her medications" (patient forgets BP meds) | split per R2 → CHF meds S; blanket claim S* [scope ambiguity] | R2 |
| Denies suicidal/homicidal ideation ("wanting to harm yourself or hurt others?" / "no, nothing like that") | S [paraphrase] | R1 anchor |
| Denies chest pain/SOB/leg swelling ("not that I've noticed") | S [hedge flattening], below action threshold | R6 |
| Echo "demonstrates" EF 45% (last year's echo, Results-section present tense) | S [temporal displacement] — timing implied, not stated | R3 |
| Lipid: "elevated cholesterol" ("a tiny bit high… wasn't too, too bad… last year") | S [temporal displacement][hedge flattening] | R3, R6 |
| "Patient understands and agrees with the recommended medical treatment plan" | **I** [template attestation], severity: relevant | R7 |
**Tally: 31 S · 0 C · 1 I.**

## Example 2 — primock57 day1_consultation01 (gastroenteritis, UK GP)
Live-written clinician note. 30 atomic claims (UK shorthand expanded).

| Claim | Label | Rule/Precedent |
|---|---|---|
| 3/7 hx diarrhoea, mainly watery; no blood in stool | S | — |
| Opening bowels ×6/day ("six or seven times") | S [range narrowing] | R8 |
| LLQ pain, crampy, intermittent | S | — |
| Nil radiation ("no, just maybe my stomach") | S [hedge flattening] | R6 |
| **Vomiting — mainly bilious** ("just normal food colour… normal vomit") | **C [clinical-specific contradiction]**, severity: relevant | **P1** |
| No blood in vomit | S | — |
| **Fever on first day, nil since** (unmeasured; "felt just a bit hot… when the symptoms started") | **S\* [subjective symptom inference][hedge flattening][temporal compression]** | **P2** |
| Lethargic and weak since | S | — |
| Takeaway 4/7 ago (patient: "four days"; doctor recap: "three days") | S [intra-transcript conflict — patient outranks on history] | R9 |
| Chinese restaurant | S | — |
| One child vomiting | S (split) | R2 |
| **Wife unwell with vomiting** ("no one else in the family") | **C**, severity: relevant | R2 |
| **Children (both) vomiting** (one of two) | **C**, severity: benign | R2 |
| Family: no diarrhoea; no other unwell contacts | S | — |
| PMH asthma; DH inhalers only; SH accountant, lives with wife and children; ADLs affected; nil smoking/EtOH | S | — |
| Imp: gastroenteritis | S | — |
| Plan: conservative mgmt, rest; push fluids; paracetamol if feverish; OTC Dioralyte | S | — |
| **Review in 3–5d if not improving** (doctor: "three to four days") | **C [range violation]**, severity: benign-to-relevant | **P3** |
| **To be seen earlier if feeling more unwell** (no such advice in transcript) | **I [template attestation — safety-netting]**, severity: **treatment-changing** (medicolegal audit trail asserting advice never given) | R7 |
**Tally: 24 S · 4 C · 1 I** — in a gold, clinician-written note.

## The instructive symmetry
- ACI-Bench-01's note **contains** a consent attestation; its transcript **lacks** any agreement utterance → I.
- primock57-01's transcript **contains** explicit agreement ("How's that sound?" / "That sounds great" … "is the treatment plan clear?" / "yes, very clear") but its note **omits** the attestation entirely — while fabricating the safety-netting line instead.
Documentation practice and conversational reality are uncorrelated in both directions. This motivates the corpus-wide attestation cross-tab (note-has-attestation × transcript-has-support).
