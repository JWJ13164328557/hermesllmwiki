#!/usr/bin/env python3
"""
剩余缺失 PDF 的 OA 拆分 (2026-08-24)
OpenAlex 并发查询缺失 DOI 的 OA 状态，生成 OA(可免费下载)/nonOA(闭源) 两个清单。
"""
import os, json, csv, re, urllib.request, urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = '/mnt/g/hermes_obsidian/hermes'
UA = {'User-Agent': 'mailto:jiwj_hermes_kb@gmail.com', 'Accept': 'application/json'}

def query_oa(doi):
    try:
        url = f'https://api.openalex.org/works/doi:{urllib.parse.quote(doi, safe="")}?select=doi,open_access'
        req = urllib.request.Request(url, headers=UA)
        resp = urllib.request.urlopen(req, timeout=15)
        d = json.loads(resp.read())
        oa = d.get('open_access', {})
        return doi, bool(oa.get('is_oa')), oa.get('oa_status', 'closed'), oa.get('oa_url', '')
    except Exception as e:
        return doi, False, 'error', str(e)[:60]

def main():
    # 读缺失 DOI
    dois = []
    with open(f'{BASE}/missing_dois.txt') as f:
        for ln in f:
            d = ln.strip()
            if re.match(r'^10\.\d{4,9}/', d):
                dois.append(d)
    print(f'缺失 DOI: {len(dois)}')

    oa_rows, nonoa_rows = [], []
    done = 0
    with ThreadPoolExecutor(max_workers=10) as pool:
        futs = {pool.submit(query_oa, d): d for d in dois}
        for fut in as_completed(futs):
            doi, isoa, status, url = fut.result()
            done += 1
            row = {'doi': doi, 'oa': 'YES' if isoa else 'NO', 'status': status, 'url': url}
            (oa_rows if isoa else nonoa_rows).append(row)
            if done % 200 == 0 or done == len(dois):
                print(f'  {done}/{len(dois)} ({100*done//len(dois)}%)')

    # 写 OA 清单
    with open(f'{BASE}/missing_pdfs_OA.txt', 'w') as f:
        for r in oa_rows:
            f.write(r['doi'] + '\n')
    with open(f'{BASE}/missing_pdfs_nonOA.txt', 'w') as f:
        for r in nonoa_rows:
            f.write(r['doi'] + '\n')
    print(f'拆分完成: OA {len(oa_rows)} ({100*len(oa_rows)/max(len(dois),1):.0f}%), 非OA {len(nonoa_rows)}')

if __name__ == '__main__':
    main()
