#!/usr/bin/env python3
"""批量获取DOI元数据 - 分批模式，每30篇保存"""
import csv, json, subprocess, time, os, re, sys

CSV_PATH = '/mnt/g/hermes_obsidian/hermes/raw/papers/metabolism/doi_survey.csv'
OUT_JSON = '/mnt/g/hermes_obsidian/hermes/raw/papers/metabolism/metadata_batch.json'

def curl(url, timeout=20):
    try:
        r = subprocess.run(['curl', '-sL', '--connect-timeout', '8', '--max-time', str(timeout), url],
                          capture_output=True, text=True, timeout=timeout+5)
        if r.returncode != 0 or not r.stdout.strip():
            return None
        return r.stdout
    except: return None

def get_meta(doi):
    """合并 Crossref + PubMed"""
    result = {'doi': doi, 'pmid': '', 'title': '', 'journal': '', 'year': '',
              'authors': [], 'abstract': '', 'filenames': [], 'error': ''}
    # Crossref
    raw = curl(f'https://api.crossref.org/works/{doi}')
    if not raw:
        result['error'] = 'crossref_unreachable'
        return result
    try:
        msg = json.loads(raw).get('message', {})
        result['title'] = (msg.get('title', ['']) or [''])[0]
        result['journal'] = (msg.get('container-title', ['']) or [''])[0]
        dates = msg.get('published-print') or msg.get('published-online') or msg.get('created') or {}
        yp = dates.get('date-parts', [[None]])[0]
        result['year'] = str(yp[0]) if yp and yp[0] else ''
        result['authors'] = [f"{a.get('given','')} {a.get('family','')}".strip() 
                            for a in msg.get('author', [])[:8] if a.get('family')]
        ab = msg.get('abstract', '')
        if ab:
            ab = re.sub(r'<[^>]+>', '', ab)
            ab = re.sub(r'\s+', ' ', ab).strip()
        result['abstract'] = ab[:4000]
    except Exception as e:
        result['error'] = f'crossref_parse:{e}'
    # PubMed PMID
    if not result['error']:
        raw = curl(f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={doi}[doi]&retmode=json', timeout=10)
        if raw:
            try:
                ids = json.loads(raw).get('esearchresult', {}).get('idlist', [])
                result['pmid'] = ids[0] if ids else ''
            except: pass
    return result

def main():
    # 读 CSV 并去重
    doi_map = {}
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            if row['status'] != 'NEW': continue
            d = row['doi'].strip()
            if d:
                doi_map.setdefault(d, []).append(row['filename'].strip())
    
    # 加载已有
    existing = {}
    if os.path.exists(OUT_JSON):
        with open(OUT_JSON, 'r') as f:
            existing = json.load(f)
    
    todo = [(d, fs) for d, fs in doi_map.items() if d not in existing]
    total = len(todo)
    print(f"待处理: {total}/{len(doi_map)} (已有 {len(existing)})")
    
    for i, (doi, fnames) in enumerate(todo):
        print(f"[{i+1}/{total}] {doi[:55]}", end=' ', flush=True)
        result = get_meta(doi)
        result['filenames'] = fnames
        existing[doi] = result
        
        ok = 'OK' if not result['error'] else f"ERR:{result['error'][:30]}"
        pmid = f" PMID:{result['pmid']}" if result['pmid'] else ''
        print(f"{ok} | {result['title'][:50]}{pmid}")
        
        # 每30篇保存
        if (i + 1) % 30 == 0:
            with open(OUT_JSON + '.tmp', 'w', encoding='utf-8') as f:
                json.dump(existing, f, ensure_ascii=False, indent=2)
            os.replace(OUT_JSON + '.tmp', OUT_JSON)
            print(f"  [SAVED {len(existing)} records]")
        
        time.sleep(0.4)
    
    # 最终保存
    with open(OUT_JSON + '.tmp', 'w', encoding='utf-8') as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
    os.replace(OUT_JSON + '.tmp', OUT_JSON)
    
    ok = sum(1 for v in existing.values() if not v.get('error'))
    with_pmid = sum(1 for v in existing.values() if v.get('pmid'))
    print(f"\n=== DONE === Total:{len(existing)} OK:{ok} WithPMID:{with_pmid}")

if __name__ == '__main__':
    main()
