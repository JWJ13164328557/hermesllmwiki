#!/usr/bin/env python3
"""
缺失 PDF 补充 — Europe PMC 全文批量下载 (2026-08-24)
对缺失清单跑 Europe PMC, 对有 fullTextUrl PDF 的论文直接下载 (PMC/OA)。
补充 UnPaywall/OpenAlex 漏掉的 PMC 全文。
"""
import os, re, sys, requests, time, urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = '/mnt/g/hermes_obsidian/hermes'
OUT = f'{BASE}/raw/papers/all_pdfs'
UA = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0'}

def curl(url, timeout=20):
    try:
        r = requests.get(url, headers=UA, timeout=timeout, allow_redirects=True)
        return r
    except Exception:
        return None

def is_valid_pdf(path):
    try:
        with open(path, 'rb') as f:
            return f.read(4) == b'%PDF'
    except Exception:
        return False

def epmc_pdf_url(doi):
    """Europe PMC 查 fullTextUrlList 里的 PDF 直链."""
    url = (f'https://www.ebi.ac.uk/europepmc/webservices/rest/search'
           f'?query=DOI:{urllib.parse.quote(doi, safe="")}&format=json&resultType=core')
    r = curl(url)
    if not r or r.status_code != 200:
        return None
    try:
        res = r.json().get('resultList', {}).get('result', [])
        if not res:
            return None
        rec = res[0]
        # 优先 fullTextUrlList 里的 pdf
        for x in rec.get('fullTextUrlList', {}).get('fullTextUrl', []) or []:
            if x.get('documentStyle') == 'pdf' and x.get('url'):
                return x['url']
        pmcid = rec.get('pmcid')
        if pmcid and rec.get('isOpenAccess') == 'Y':
            return f'https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/pdf/'
    except Exception:
        return None
    return None

def download_one(doi):
    safe = doi.replace('/', '_').replace(':', '_')
    dest = os.path.join(OUT, safe + '.pdf')
    if os.path.exists(dest) and is_valid_pdf(dest):
        return (doi, 'already')
    u = epmc_pdf_url(doi)
    if not u:
        return (doi, 'no-pmc')
    try:
        r = curl(u, timeout=40)
        if r and r.status_code == 200 and len(r.content) > 5000 and r.content[:4] == b'%PDF':
            with open(dest, 'wb') as f:
                f.write(r.content)
            return (doi, f'OK {len(r.content)//1024}KB')
        return (doi, 'not-pdf')
    except Exception as e:
        return (doi, f'err:{type(e).__name__}')

def main():
    dois = [l.strip() for l in open(f'{BASE}/missing_dois.txt') if re.match(r'^10\.', l.strip())]
    print(f'缺失 DOI: {len(dois)}')
    ok, fail = [], []
    done = 0
    with ThreadPoolExecutor(max_workers=10) as pool:
        futs = {pool.submit(download_one, d): d for d in dois}
        for fut in as_completed(futs):
            doi, res = fut.result()
            if res.startswith('OK') or res == 'already':
                ok.append(res)
            else:
                fail.append(res)
            done += 1
            if done % 200 == 0:
                print(f'  {done}/{len(dois)}')
    print(f'\n完成: 成功/已有 {len(ok)}, 失败 {len(fail)}')

if __name__ == '__main__':
    main()
