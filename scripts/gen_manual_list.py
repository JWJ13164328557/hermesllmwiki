#!/usr/bin/env python3
"""生成手动/VPN 下载清单: 从 missing 列表匹配概念页元数据, 输出可读 CSV/Markdown"""
import os, re, csv, sys, glob

BASE = '/mnt/g/hermes_obsidian/hermes'

# 读 missing DOIs
def read_dois(path):
    dois = []
    if not os.path.exists(path): return dois
    for line in open(path):
        doi = line.strip()
        if doi and not doi.startswith('#'):
            dois.append(doi)
    return dois

missing_dois = read_dois(f'{BASE}/missing_dois.txt')
nonoa = set(read_dois(f'{BASE}/missing_pdfs_nonOA.txt'))
oa   = set(read_dois(f'{BASE}/missing_pdfs_OA.txt'))

# 构建 DOI -> (title, journal, year) 从 concepts 页
def concept_meta(doi):
    di = doi.replace('/', '_')
    for dirn in ['papers', '']:
        for pat in [f'{BASE}/concepts/{dirn}/*{di}*.md', f'{BASE}/concepts/{dirn}/*.md']:
            pass
    # 直接遍历找匹配
    return None

# 快速: 建立 doi 索引 (一次读全部前三行)
doi_meta = {}
for fp in glob.glob(f'{BASE}/concepts/papers/*.md') + glob.glob(f'{BASE}/concepts/daily-*.md'):
    try:
        head = open(fp, 'r', encoding='utf-8', errors='ignore').read(2500)
        m = re.search(r'doi:\s*"?\s*(10\.\d{4,}/[^\s\n"]+)', head, re.I)
        if not m: continue
        d = m.group(1).strip().rstrip('./')
        tm = re.search(r'^title:\s*"?([^"\n]+)"?', head, re.M|re.I)
        jm = re.search(r'^journal:\s*"?([^"\n]+)"?', head, re.M|re.I)
        ym = re.search(r'^year:\s*"?(\d{4})', head, re.M)
        doi_meta[d] = (tm.group(1).strip() if tm else '', jm.group(1).strip() if jm else '', ym.group(1) if ym else '')
    except Exception:
        continue

rows = []
seen = set()
for d in missing_dois:
    if d in seen: continue
    seen.add(d)
    t, j, y = doi_meta.get(d, ('', '', ''))
    rows.append({'doi': d, 'title': t, 'journal': j, 'year': y,
                 'type': 'nonOA(需VPN)' if d in nonoa else ('OA(可免费)' if d in oa else '未知')})

rows.sort(key=lambda r: (r['type']!='OA(可免费)', r['year']))

with open(f'{BASE}/manual_download_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=['type','doi','title','journal','year'])
    w.writeheader()
    for r in rows: w.writerow(r)

oac = sum(1 for r in rows if r['type']=='OA(可免费)')
noac = sum(1 for r in rows if r['type'].startswith('nonOA'))
print(f'总缺失: {len(rows)} | OA可免费重试: {oac} | nonOA需VPN: {noac}')
print(f'已生成: {BASE}/manual_download_list.csv')
