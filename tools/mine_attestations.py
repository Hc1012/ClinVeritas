#!/usr/bin/env python3
"""ClinVeritas attestation locator pass (Labelling Guidelines v1, R1-compliant).

Locates candidate consent-attestation and safety-netting lines in gold clinical
notes and pre-fetches candidate evidence utterances from the paired transcripts.
This tool LOCATES candidates only — it never assigns labels (Rule R1).
Label, severity, and tag columns are emitted empty for human annotation.

Usage:
  python mine_attestations.py \
      --aci-dir path/to/aci-bench \
      --primock-dir path/to/primock57 \
      --primock-transcripts-dir path/to/converted_transcripts \
      --out attestation_labelling_worksheet.csv

primock57 ships transcripts as TextGrids; convert once with the dataset's own
script (primock57/scripts/textgrid_to_transcript.py) before running this.

Stdlib only. Python >= 3.8.
"""
import argparse, csv, glob, json, os, re, sys

# --- Locator patterns (frozen alongside Guidelines v1; changing these breaks
# --- reproducibility of the committed worksheet) ---
CONSENT_NOTE = re.compile(r'(understands? and agrees?|agree(s|able)? (with|to)|questions? (were |was )?answered|risks? and benefits?|verbaliz|consent)', re.I)
SAFETYNET_NOTE = re.compile(r'(safety.?net|\bSN\b|(if|should).{0,60}(wors|unwell|persist|not improv|deteriorat|develop|recur)|(return|seek|call|contact|come back|see|review|follow.?up|f/u).{0,50}(if|sooner|earlier|urgent|999|111|emergency|A&E|\bED\b)|(999|111|A&E|emergency).{0,40}if)', re.I)
AGREE_TX = re.compile(r"(sounds? (good|great|fine|reasonable)|that sounds|i agree|happy with (that|the plan)|plan.{0,20}clear|works for me|agree with (that|the plan)|(yes|yeah).{0,15}(clear|agree))", re.I)
SN_TX = re.compile(r'(come back|see you (again|sooner)|call (us|the office|911|999|111)|(if|should).{0,50}(worse|wors|unwell|not (better|improve)|persist)|emergency|sooner|earlier if)', re.I)

DEFAULT_ACI_SPLITS = ['train', 'valid', 'clinicalnlp_taskB_test1', 'clinicalnlp_taskC_test2', 'clef_taskC_test3']

def sentences(text):
    text = re.sub(r'\s+', ' ', text)
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+|\n', text) if s.strip()]

def load_encounters(aci_dir, primock_dir, primock_tx_dir, aci_splits):
    encounters, skipped = [], 0
    for f in aci_splits:
        path = os.path.join(aci_dir, 'data', 'challenge_data_json', f'{f}.json')
        if not os.path.exists(path):
            sys.exit(f"ERROR: missing ACI-Bench split file: {path}")
        for i, d in enumerate(json.load(open(path))['data']):
            encounters.append({'dataset': 'aci-bench', 'id': f"{f}-{d.get('file', i)}",
                               'note': d['tgt'], 'tx': d['src']})
    note_files = sorted(glob.glob(os.path.join(primock_dir, 'notes', '*.json')))
    if not note_files:
        sys.exit(f"ERROR: no primock57 notes found under {primock_dir}/notes")
    for nf in note_files:
        d = json.load(open(nf))
        base = os.path.basename(nf).replace('.json', '')
        txp = os.path.join(primock_tx_dir, f'{base}.txt')
        if not os.path.exists(txp):
            skipped += 1
            continue
        encounters.append({'dataset': 'primock57', 'id': base,
                           'note': d['note'] or '', 'tx': open(txp).read()})
    if skipped:
        print(f"WARNING: skipped {skipped} primock57 notes with no converted transcript in "
              f"{primock_tx_dir} — run primock57/scripts/textgrid_to_transcript.py first.", file=sys.stderr)
    return encounters

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--aci-dir', required=True, help='path to cloned aci-bench repo')
    ap.add_argument('--primock-dir', required=True, help='path to cloned primock57 repo')
    ap.add_argument('--primock-transcripts-dir', required=True, help='path to converted primock57 .txt transcripts')
    ap.add_argument('--out', required=True, help='output worksheet CSV path')
    ap.add_argument('--aci-splits', nargs='+', default=DEFAULT_ACI_SPLITS,
                    help='ACI-Bench encounter-level splits to include (default: the five canonical splits; '
                         'section-level variant files are intentionally excluded to avoid duplicate encounters)')
    args = ap.parse_args()

    encounters = load_encounters(args.aci_dir, args.primock_dir, args.primock_transcripts_dir, args.aci_splits)

    rows, stats = [], {}
    for e in encounters:
        ds = stats.setdefault(e['dataset'], {'n': 0, 'consent': 0, 'sn': 0, 'consent_txhit': 0, 'sn_txhit': 0})
        ds['n'] += 1
        c_lines = [s for s in sentences(e['note']) if CONSENT_NOTE.search(s)]
        s_lines = [s for s in sentences(e['note']) if SAFETYNET_NOTE.search(s) and not CONSENT_NOTE.search(s)]
        tx_agree = [s for s in sentences(e['tx']) if AGREE_TX.search(s)][:3]
        tx_sn = [s for s in sentences(e['tx']) if SN_TX.search(s)][:3]
        if c_lines:
            ds['consent'] += 1
            if tx_agree: ds['consent_txhit'] += 1
            rows.append([e['dataset'], e['id'], 'consent',
                         ' | '.join(c_lines)[:300], ' | '.join(tx_agree)[:400], '', '', '', ''])
        if s_lines:
            ds['sn'] += 1
            if tx_sn: ds['sn_txhit'] += 1
            rows.append([e['dataset'], e['id'], 'safety-netting',
                         ' | '.join(s_lines)[:300], ' | '.join(tx_sn)[:400], '', '', '', ''])

    out_dir = os.path.dirname(os.path.abspath(args.out))
    os.makedirs(out_dir, exist_ok=True)
    with open(args.out, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['dataset', 'encounter_id', 'candidate_type',
                    'note_lines(CANDIDATE)', 'transcript_locator_hits(EVIDENCE CANDIDATES - NOT LABELS)',
                    'label(S/C/I)', 'severity(benign/relevant/treatment-changing)', 'tags', 'rater_notes'])
        w.writerows(rows)

    for k, v in stats.items():
        print(f"{k}: {v['n']} notes | consent attestation in {v['consent']} "
              f"({100*v['consent']/v['n']:.0f}%), of which {v['consent_txhit']} have candidate agreement "
              f"utterances in transcript | safety-netting line in {v['sn']} ({100*v['sn']/v['n']:.0f}%), "
              f"of which {v['sn_txhit']} have candidate SN utterances")
    print(f"\nTotal worksheet rows for labelling: {len(rows)}")
    print(f"Wrote: {args.out}")

if __name__ == '__main__':
    main()
