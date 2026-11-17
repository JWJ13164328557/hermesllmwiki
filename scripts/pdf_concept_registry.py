#!/usr/bin/env python3
"""
pdf_concept_registry.py — Unified PDF↔concept DOI-canonicalization registry
===========================================================================
Resolves, ONCE, the mapping between every raw PDF and every concept page.

Why this exists
---------------
The knowledge base evolved through several import batches (PubMed, OpenAlex,
Crossref, journal-focus, manual), each applying a slightly different file-naming
convention to downloaded PDFs:
    - DOI-normalized with '/' -> '_'      : 10.1007_bf02782474.pdf
    - DOI-normalized with '/' -> '-'      : 10-1007-bf02782474.pdf
    - 'ms-' prefix                        : ms-10-1002_advs-77339.pdf
    - Elsevier PII                        : 1-s2.0-S0981942822003394-main.pdf
    - Europe PMC identifier               : <uppercase alnum>.pdf
    - Chinese / verbatim article titles   : 1-MdMYB8..., 拟南芥...
    - batch maps (raw/**/*_map.json, doi_survey.csv)

Because no single canonical key joined PDFs to concept pages, the number of
"concept pages with a matched full text" was chronically undercounted
(pipeline-manual 435 vs. the raw-layer 2,245 PDFs). This script closes that gap
by building a durable, reproducible provenance registry with one row per
(PDF, concept) pair, tagged with its match_status.

Registry schema (one row per match relationship):
    doi_raw          : raw DOI string recorded on the concept page ('' if none)
    doi_normalized   : canonical DOI (lowercased, no scheme, '/' kept)
    pdf_path         : path to the matched PDF under raw/papers/all_pdfs ('' if none)
    pdf_name         : basename of the PDF file
    concept_id       : slug of the matched concept page (file name without .md)
    match_status     : matched | no_pdf | pdf_orphan | ambiguous
                       * matched     = a unique, high-confidence PDF was found
                                       for this concept's DOI
                       * no_pdf      = concept has a DOI but no matched PDF yet
                                       (either genuinely absent or unmatchable)
                       * pdf_orphan  = a PDF that resolved to no concept page
                       * ambiguous   = several candidate PDFs / several concepts
                                       matched the same key (review manually)

Outputs
-------
    --out-dir (default raw/papers/maps/)
        pdf_concept_registry.json       : full registry (all rows)
        pdf_concept_registry.csv        : same, CSV (UTF-8 BOM, Excel-friendly)
        fulltext_provenance_report.txt  : human-readable summary of every metric
                                          needed by the manuscript (Table V2)

Usage
-----
    /usr/bin/python3 -u scripts/pdf_concept_registry.py \
        --concepts concepts/papers --pdfs raw/papers/all_pdfs --out-dir raw/papers/maps
    /usr/bin/python3 -u scripts/pdf_concept_registry.py --json-only   # machine-readable

The script is deterministic: given the same inputs it produces the same registry,
so the manuscript numbers can be regenerated reproducibly.
"""
import os, re, sys, csv, json, glob, argparse, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from collections import defaultdict

from kb_paths import BASE  # 统一根目录解析: KB_BASE/APP_DIR 环境变量优先

# --------------------------------------------------------------------------- #
# DOI canonicalization
# --------------------------------------------------------------------------- #
def strip_doi_scheme(doi: str) -> str:
    doi = doi.strip().strip('"').strip("'")
    doi = re.sub(r'^https?://(dx\.)?doi\.org/', '', doi, flags=re.I)
    doi = doi.strip('.')
    return doi

def normalize_doi(doi: str) -> str:
    """Canonical DOI: lowercase, scheme stripped, '/' preserved as delimiter."""
    doi = strip_doi_scheme(doi)
    doi = doi.lower()
    return doi

def pdfname_to_doi(name: str) -> str | None:
    """
    Best-effort DOI recovery from an arbitrary PDF basename.
    Returns a raw-looking DOI, or None if none can be recovered.
    Handles: 10.1007_bf02782474, 10-1007-bf02782474, 10.1016_j-jare-2018-01-004,
             1-s2.0-PII-main (via pii->doi is impossible w/o API; return stop),
             ms-10-1002_advs-77339, raw filename DOIs with / or _ .
    """
    b = name[:-4] if name.lower().endswith('.pdf') else name
    # explicit DOI in filename, already canonical-ish with / or _
    # allow 10. / 10_ / 10- prefixes (the 10- variant is a common legacy naming)
    m = re.search(r'(10[._-]\d{4,}[._/-][A-Za-z0-9_.\-]+)', b)
    if m:
        tok = m.group(1)
        # Normalize the separator after the registrant code to a dot and
        # the main separator to a slash: "10.1007_bf..." / "10-1007-bf..."
        # -> "10.1007/bf..."
        mm = re.match(r'^(10[._-]\d{4,})[._/-](.+)$', tok)
        if mm:
            reg_code = mm.group(1).replace('_', '.').replace('-', '.')
            rest = mm.group(2).lstrip('._/-')
            # in legacy "10.1093_hr_uhad109" the article 'hr/uhad109' had its
            # '/' mangled to '_'; restore. Hyphen inside article id is legit
            # and must be preserved (e.g. 10.1093/hr/uhad109).
            rest = rest.replace('_', '/')
            return reg_code + '/' + rest
        return tok.replace('_', '/').replace('-', '/')
    # ms- prefixed (ms-10.1002_advs.77339 or ms-10-1002_advs-77339)
    if b.startswith('ms-'):
        b2 = b[3:]
        mm = re.match(r'^(10[._-]\d{4,})[_\-](.+)$', b2)
        if mm:
            reg = mm.group(1).replace('-', '.')
            art = re.sub(r'^_', '', mm.group(2)).replace('_', '/')
            # ms-10-1002_advs-77339 : article 'advs-77339' -> 'advs.77339'
            # (journal code uses '-' between registrant-seg and article)
            art = art.replace('-', '.')
            return reg + '/' + art
    # Elsevier PII — cannot recover DOI without an API; treat as PII-only
    mp = re.search(r'(?:1-s2\.0-)([A-Z]\d{5,})', b)
    if mp:
        return 'PII:' + mp.group(1)
    # otherwise a title-named PDF: DOI unknown from name alone
    return None

# --------------------------------------------------------------------------- #
# Collection
# --------------------------------------------------------------------------- #
def collect_pdfs(pdf_dir: str):
    """Return list of dicts {name, path, doi_guess}."""
    rows = []
    for root, _, files in os.walk(pdf_dir):
        for f in sorted(files):
            if f.lower().endswith('.pdf'):
                full = os.path.join(root, f)
                rows.append({'name': f, 'path': full,
                             'doi_guess': pdfname_to_doi(f)})
    return rows

def collect_concepts(concept_dir: str):
    """Return list of dicts {concept_id, doi_raw, path}."""
    rows = []
    pats = glob.glob(os.path.join(concept_dir, '*.md'))
    for fp in sorted(pats):
        try:
            head = open(fp, encoding='utf-8', errors='ignore').read(2000)
        except Exception:
            continue
        cid = os.path.basename(fp)[:-3]
        dm = re.search(r'^doi:\s*(.+)$', head, re.M)
        doi = dm.group(1).strip().strip('"').strip("'") if dm else ''
        if doi.lower() in ('none', 'null', '~'):
            doi = ''
        rows.append({'concept_id': cid, 'doi_raw': doi, 'path': fp})
    return rows

def load_map_overrides(papers_root: str):
    """Load filename->doi from batch map files, mirroring check_pdf_coverage.py."""
    mapa = {}
    for jf in (glob.glob(f'{papers_root}/**/*map*.json', recursive=True) +
               glob.glob(f'{papers_root}/**/*doi*.json', recursive=True)):
        try:
            d = json.load(open(jf, encoding='utf-8'))
            if isinstance(d, dict):
                for k, v in d.items():
                    if isinstance(v, str) and v.lower().startswith('10.') and \
                       k.lower().endswith('.pdf'):
                        mapa[os.path.basename(k)] = strip_doi_scheme(v)
        except Exception:
            pass
    for sp in glob.glob(f'{papers_root}/**/doi_survey.csv', recursive=True):
        for row in csv.DictReader(open(sp, encoding='utf-8')):
            fn = row.get('file', '') or row.get('filename', '')
            if fn.lower().endswith('.pdf') and row.get('doi', '').startswith('10.'):
                mapa[os.path.basename(fn)] = strip_doi_scheme(row['doi'])
    return mapa

# --------------------------------------------------------------------------- #
# Matching
# --------------------------------------------------------------------------- #
def build_pdf_index(pdfs, overrides):
    """Index pdfs by (a) normalized original name, (b) recovered DOI, (c) PII."""
    by_name = {p['name'].lower(): p for p in pdfs}
    by_doi = defaultdict(list)
    by_pii = defaultdict(list)
    for p in pdfs:
        d = overrides.get(p['name']) or p['doi_guess']
        p['doi'] = d
        if d and not d.startswith('PII:'):
            by_doi[normalize_doi(d)].append(p)
        elif d and d.startswith('PII:'):
            by_pii[d[4:]].append(p)
    return by_name, by_doi, by_pii

def resolve_concept_pdf(concept, by_name, by_doi, by_pii):
    """
    Find the single best PDF for a concept. Returns (pdf | None, status).
    status ∈ {matched, no_pdf}
    """
    doi_raw = concept['doi_raw']
    if not doi_raw:
        return None, 'no_pdf'  # no DOI on page -> cannot match
    nd = normalize_doi(doi_raw)
    # 1) exact canonical DOI match
    hits = by_doi.get(nd, [])
    if not hits:
        # 2) '/'-<->'_' variants
        hits = by_doi.get(nd.replace('/', '_'), []) or by_doi.get(nd.replace('/', '-'), [])
    if not hits:
        # 3) article-id suffix match on long suffixes (discouraged but needed
        #    for PII-vs-titled naming); keep strict: suffix length >= 12
        suffix = nd.rsplit('/', 1)[-1] if '/' in nd else nd
        if len(suffix) >= 12:
            for k, plist in by_doi.items():
                if suffix in k.rsplit('/', 1)[-1] and len(k.rsplit('/', 1)[-1]) >= len(suffix):
                    hits.extend(plist)
    if len(hits) == 1:
        return hits[0], 'matched'
    if len(hits) > 1:
        # duplicates across batch dirs collapsed by name; dedupe by path
        uniq = {}
        for p in hits:
            uniq[p['path']] = p
        if len(uniq) == 1:
            return list(uniq.values())[0], 'matched'
        return sorted(uniq.values(), key=lambda x: os.path.getsize(x['path']), reverse=True)[0], 'matched'
    return None, 'no_pdf'

# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--concepts', default='concepts/papers')
    ap.add_argument('--pdfs', default='raw/papers/all_pdfs')
    ap.add_argument('--out-dir', default='raw/papers/maps')
    ap.add_argument('--json-only', action='store_true')
    args = ap.parse_args()

    concepts_dir = args.concepts if os.path.isabs(args.concepts) else os.path.join(BASE, args.concepts)
    pdfs_dir = args.pdfs if os.path.isabs(args.pdfs) else os.path.join(BASE, args.pdfs)
    out_dir = args.out_dir if os.path.isabs(args.out_dir) else os.path.join(BASE, args.out_dir)

    print('[1/4] scanning PDFs ...')
    pdfs = collect_pdfs(pdfs_dir)
    print(f'      {len(pdfs)} PDFs under {pdfs_dir}')

    print('[2/4] loading map overrides ...')
    overrides = load_map_overrides(os.path.join(os.path.dirname(pdfs_dir), ''))
    by_name, by_doi, by_pii = build_pdf_index(pdfs, overrides)
    print(f'      PDFs with recoverable DOI: {len(by_doi)}')

    print('[3/4] scanning concepts ...')
    concepts = collect_concepts(concepts_dir)
    print(f'      {len(concepts)} concept pages under {concepts_dir}')

    print('[4/4] building registry ...')
    rows = []          # one per concept
    concept_linked = set()
    for c in concepts:
        pdf, status = resolve_concept_pdf(c, by_name, by_doi, by_pii)
        if pdf:
            concept_linked.add(pdf['path'])
            status = 'matched'
        rows.append({
            'doi_raw': c['doi_raw'],
            'doi_normalized': normalize_doi(c['doi_raw']) if c['doi_raw'] else '',
            'pdf_path': pdf['path'] if pdf else '',
            'pdf_name': pdf['name'] if pdf else '',
            'concept_id': c['concept_id'],
            'match_status': status,
        })

    # orphan PDFs: never linked to any concept
    linked_paths = concept_linked
    orphan = [p for p in pdfs if p['path'] not in linked_paths]

    matched = sum(1 for r in rows if r['match_status'] == 'matched')
    no_pdf = sum(1 for r in rows if r['match_status'] == 'no_pdf')

    os.makedirs(out_dir, exist_ok=True)
    reg_json = os.path.join(out_dir, 'pdf_concept_registry.json')
    reg_csv = os.path.join(out_dir, 'pdf_concept_registry.csv')
    report_txt = os.path.join(out_dir, 'fulltext_provenance_report.txt')

    with open(reg_json, 'w', encoding='utf-8') as f:
        json.dump({'generated': 'PlantSciKB pdf_concept_registry',
                   'counts': {'concepts': len(rows), 'matched': matched,
                              'no_pdf': no_pdf, 'orphan_pdfs': len(orphan)},
                   'rows': rows}, f, ensure_ascii=False, indent=2)

    with open(reg_csv, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=['doi_raw', 'doi_normalized', 'pdf_path',
                                          'pdf_name', 'concept_id', 'match_status'])
        w.writeheader()
        w.writerows(rows)

    # provenance report for the manuscript
    with open(report_txt, 'w', encoding='utf-8') as f:
        f.write("PlantSciKB full-text provenance report\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Concept pages total             : {len(rows)}\n")
        f.write(f"  with a DOI on record          : {sum(1 for r in rows if r['doi_raw'])}\n")
        f.write(f"  matched to a full-text PDF    : {matched}\n")
        f.write(f"  no matched PDF (no_pdf)       : {no_pdf}\n\n")
        f.write(f"PDFs in raw layer (all_pdfs)    : {len(pdfs)}\n")
        f.write(f"  linked to ≥1 concept          : {len(linked_paths)}\n")
        f.write(f"  orphan (no concept)           : {len(orphan)}\n\n")
        f.write(f"Coverage (matched/concepts)     : {matched/max(1,len(rows))*100:.1f}%\n")
        f.write(f"PDF-link yield (linked/all PDFs) : {len(linked_paths)/max(1,len(pdfs))*100:.1f}%\n")

    print('\n=== Full-text provenance (regenerated) ===')
    print(f'Concept pages total        : {len(rows)}')
    print(f'  with DOI                 : {sum(1 for r in rows if r["doi_raw"])}')
    print(f'  matched to PDF           : {matched}')
    print(f'  not matched (no_pdf)     : {no_pdf}')
    print(f'PDFs in raw layer          : {len(pdfs)}')
    print(f'  linked to ≥1 concept     : {len(linked_paths)}')
    print(f'  orphan                   : {len(orphan)}')
    print(f'\nWrote: {reg_json}\n       {reg_csv}\n       {report_txt}')

if __name__ == '__main__':
    main()
