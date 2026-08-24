#!/usr/bin/env python3
"""批量获取 DOI 元数据：Crossref + PubMed E-utils
输出 metadata_batch.json，支持断点续传"""
import csv, json, subprocess, time, os, sys, re

CSV_PATH = '/mnt/g/hermes_obsidian/hermes/raw/papers/metabolism/doi_survey.csv'
OUT_JSON = '/mnt/g/hermes_obsidian/hermes/raw/papers/metabolism/metadata_batch.json'

def curl_get(url, timeout=15):
    try:
        r = subprocess.run(['curl', '-sL', '--connect-timeout', '10', '--max-time', str(timeout), url],
                          capture_output=True, text=True, timeout=timeout+5)
        return r.stdout
    except: return ''

def crossref_metadata(doi):
    """从 Crossref API 获取论文元数据"""
    url = f'https://api.crossref.org/works/{doi}'
    raw = curl_get(url, timeout=15)
    if not raw: return None
    try:
        data = json.loads(raw)
        msg = data.get('message', {})
        title_list = msg.get('title', [''])
        title = title_list[0] if title_list else ''
        journal = msg.get('container-title', [''])[0] if msg.get('container-title') else ''
        year = msg.get('published-print', {}).get('date-parts', [[None]])[0][0]
        if not year:
            year = msg.get('created', {}).get('date-parts', [[None]])[0][0]
        authors = []
        for a in msg.get('author', [])[:10]:
            family = a.get('family', '')
            given = a.get('given', '')
            if family: authors.append(f'{given} {family}'.strip())
        abstract = msg.get('abstract', '')
        # Strip HTML tags from abstract
        abstract = re.sub(r'<[^>]+>', '', abstract) if abstract else ''
        abstract = re.sub(r'\s+', ' ', abstract).strip()
        return {'title': title, 'journal': journal, 'year': str(year) if year else '',
                'authors': authors, 'abstract': abstract[:5000]}
    except Exception as e:
        return {'error': str(e)}

def pubmed_pmid(doi):
    """从 PubMed E-utils 获取 PMID"""
    url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={doi}[doi]&retmode=json'
    raw = curl_get(url, timeout=10)
    if not raw: return ''
    try:
        data = json.loads(raw)
        ids = data.get('esearchresult', {}).get('idlist', [])
        return ids[0] if ids else ''
    except: return ''

def load_existing():
    if os.path.exists(OUT_JSON):
        try:
            with open(OUT_JSON, 'r') as f:
                return json.load(f)
        except: pass
    return {}

def load_dois():
    """读取CSV，去重，返回唯一DOI列表及文件名映射"""
    doi_map = {}  # doi -> [filenames]
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['status'] != 'NEW': continue
            doi = row['doi'].strip()
            fname = row['filename'].strip()
            if not doi: continue
            if doi not in doi_map:
                doi_map[doi] = []
            doi_map[doi].append(fname)
    return doi_map

def main():
    doi_map = load_dois()
    print(f"总唯一DOI: {len(doi_map)}")
    
    existing = load_existing()
    print(f"已获取: {len(existing)}")
    
    todo = {k: v for k, v in doi_map.items() if k not in existing}
    print(f"待获取: {len(todo)}")
    
    for i, (doi, fnames) in enumerate(todo.items()):
        print(f"[{i+1}/{len(todo)}] {doi[:50]}...", end=' ', flush=True)
        
        # Crossref metadata
        meta = crossref_metadata(doi)
        if not meta or 'error' in meta:
            print("Crossref FAIL, retrying once...", end=' ', flush=True)
            time.sleep(2)
            meta = crossref_metadata(doi)
        
        pmid = ''
        if meta and 'error' not in meta:
            pmid = pubmed_pmid(doi)
        
        result = {
            'doi': doi,
            'pmid': pmid,
            'title': meta.get('title', '') if meta else '',
            'journal': meta.get('journal', '') if meta else '',
            'year': meta.get('year', '') if meta else '',
            'authors': meta.get('authors', []) if meta else [],
            'abstract': meta.get('abstract', '') if meta else '',
            'filenames': fnames,
            'error': meta.get('error', '') if meta and 'error' in meta else ''
        }
        
        existing[doi] = result
        
        # 每10篇保存一次
        if (i + 1) % 10 == 0:
            with open(OUT_JSON + '.tmp', 'w', encoding='utf-8') as f:
                json.dump(existing, f, ensure_ascii=False, indent=2)
            os.replace(OUT_JSON + '.tmp', OUT_JSON)
            print(f"[SAVED {len(existing)}]")
        else:
            status = 'OK' if not result.get('error') else f"ERR:{result['error'][:30]}"
            pmid_flag = f" PMID:{pmid}" if pmid else ''
            print(f"{status}{pmid_flag}")
        
        time.sleep(0.6)  # rate limit
    
    # 最终保存
    with open(OUT_JSON + '.tmp', 'w', encoding='utf-8') as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
    os.replace(OUT_JSON + '.tmp', OUT_JSON)
    
    # 统计
    ok = sum(1 for v in existing.values() if not v.get('error'))
    with_pmid = sum(1 for v in existing.values() if v.get('pmid'))
    print(f"\n=== 完成 ===")
    print(f"总数: {len(existing)}")
    print(f"成功: {ok}")
    print(f"有PMID: {with_pmid}")
    print(f"输出: {OUT_JSON}")

if __name__ == '__main__':
    main()
