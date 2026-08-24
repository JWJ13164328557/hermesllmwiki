#!/usr/bin/env python3
"""修复 metadata_batch.json 中损坏的条目"""
import json, subprocess, time, re, os

JSON_PATH = '/mnt/g/hermes_obsidian/hermes/raw/papers/metabolism/metadata_batch.json'

def curl(url, timeout=20):
    try:
        r = subprocess.run(['curl', '-sL', '--connect-timeout', '8', '--max-time', str(timeout), url],
                          capture_output=True, text=True, timeout=timeout+5)
        if r.returncode != 0 or not r.stdout.strip():
            return None
        return r.stdout
    except: return None

def get_meta(doi):
    result = {'doi': doi, 'pmid': '', 'title': '', 'journal': '', 'year': '',
              'authors': [], 'abstract': '', 'error': ''}
    # Crossref - try up to 3 times
    for attempt in range(3):
        raw = curl(f'https://api.crossref.org/works/{doi}')
        if raw:
            break
        time.sleep(1)
    if not raw:
        result['error'] = 'crossref_unreachable_x3'
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
        result['error'] = f'parse:{e}'
        return result
    # PubMed PMID
    raw = curl(f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={doi}[doi]&retmode=json', timeout=10)
    if raw:
        try:
            ids = json.loads(raw).get('esearchresult', {}).get('idlist', [])
            result['pmid'] = ids[0] if ids else ''
        except: pass
    return result

def main():
    with open(JSON_PATH, 'r') as f:
        data = json.load(f)
    
    broken = {k: v for k, v in data.items() if v.get('error') or not v.get('title')}
    print(f"Broken entries: {len(broken)}/{len(data)}")
    
    for i, (doi, old) in enumerate(broken.items()):
        print(f"[{i+1}/{len(broken)}] {doi[:55]}", end=' ', flush=True)
        new = get_meta(doi)
        # Preserve filenames from old
        new['filenames'] = old.get('filenames', [])
        data[doi] = new
        
        if new.get('error'):
            print(f"STILL_BROKEN: {new['error'][:40]}")
        else:
            print(f"FIXED | {new['title'][:50]} | PMID:{new['pmid']}")
        
        if (i + 1) % 20 == 0:
            with open(JSON_PATH + '.tmp', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            os.replace(JSON_PATH + '.tmp', JSON_PATH)
            print(f"  [SAVED]")
        
        time.sleep(0.5)
    
    with open(JSON_PATH + '.tmp', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(JSON_PATH + '.tmp', JSON_PATH)
    
    ok = sum(1 for v in data.values() if not v.get('error') and v.get('title'))
    print(f"\nFINAL: {ok}/{len(data)} good")

if __name__ == '__main__':
    main()
