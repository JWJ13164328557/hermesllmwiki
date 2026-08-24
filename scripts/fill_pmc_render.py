#!/usr/bin/env python3
"""修复版 PMC 渲染 PDF 下载器
优先 europepmc.org/articles/{PMCID}?pdf=render (requests 可穿透的真实 PDF 通道)
用法: python3 scripts/fill_pmc_render.py --from-file missing_pdfs_OA.txt --limit 300 --workers 6
"""
import os, re, sys, requests, argparse, time, urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = '/mnt/g/hermes_obsidian/hermes'
OUT = os.path.join(BASE, 'raw/papers/all_pdfs')
UA = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

def curl(url, timeout=40):
    for attempt in range(2):
        try:
            r = requests.get(url, headers=UA, timeout=timeout, allow_redirects=True)
            return r
        except Exception:
            time.sleep(0.5)
    return None

def is_valid_pdf(path):
    try:
        return open(path, 'rb').read(4) == b'%PDF'
    except Exception:
        return False

def get_pmcid(doi):
    u = ('https://www.ebi.ac.uk/europepmc/webservices/rest/search'
         f'?query=DOI:{urllib.parse.quote(doi, safe="")}&format=json&pageSize=1')
    r = curl(u, timeout=25)
    if not r or r.status_code != 200:
        return None
    try:
        res = r.json().get('resultList', {}).get('result', [])
        if res:
            return res[0].get('pmcid')
    except Exception:
        return None
    return None

def dl_one(doi):
    doi = doi.strip().rstrip('./')
    if not re.match(r'^10\.\d{4,9}/', doi) or len(doi) > 80:
        return doi, 'skip'
    dest = os.path.join(OUT, doi.replace('/', '_') + '.pdf')
    if os.path.exists(dest) and is_valid_pdf(dest):
        return doi, 'have'
    pmcid = get_pmcid(doi)
    if not pmcid:
        return doi, 'no-pmc'
    # 优先 Europe PMC 渲染服务
    urls = [
        f'https://europepmc.org/articles/{pmcid}?pdf=render',
        f'https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextPDF',
    ]
    for u in urls:
        r = curl(u, timeout=45)
        if r and r.status_code == 200 and r.content[:4] == b'%PDF' and len(r.content) > 8000:
            with open(dest, 'wb') as f:
                f.write(r.content)
            return doi, f'OK {len(r.content)//1024}KB'
    return doi, 'fail'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--from-file', default=os.path.join(BASE, 'missing_pdfs_OA.txt'))
    ap.add_argument('--limit', type=int, default=0)
    ap.add_argument('--workers', type=int, default=6)
    args = ap.parse_args()
    dois = [l.strip() for l in open(args.from_file) if l.strip() and re.match(r'^10\.', l.strip())]
    if args.limit:
        dois = dois[:args.limit]
    print(f'待查: {len(dois)}')
    ok = fail = nopmc = 0
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futs = {pool.submit(dl_one, d): d for d in dois}
        done = 0
        for fut in as_completed(futs):
            doi, res = fut.result()
            done += 1
            if res.startswith('OK') or res == 'have': ok += 1
            elif res == 'no-pmc': nopmc += 1
            else: fail += 1
            if done % 50 == 0:
                print(f'  [{done}/{len(dois)}] ok={ok} fail={fail} nopmc={nopmc} {(time.time()-t0):.0f}s')
    print(f'DONE ok={ok} fail={fail} nopmc={nopmc} total={done} time={(time.time()-t0)/60:.1f}min')

if __name__ == '__main__':
    main()
