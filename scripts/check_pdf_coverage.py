#!/usr/bin/env python3
"""
全库 PDF 完整性检查脚本
=======================
扫描知识库所有概念页的 DOI，与 raw/ 下实际存在的 PDF 交叉比对，
判定每篇文献是否已有完整 PDF。输出缺失清单 CSV (UTF-8 BOM, 兼容 Windows Excel)。

判定"有 PDF"的方式（按优先级）：
  1. 概念页 frontmatter 的 doi 与 PDF 文件名 DOI 完全匹配（含 / -> _ 变体）
  2. PDF 文件名中含该 DOI 的部分文章ID（如后缀）
  3. 各批次映射文件（raw/**/*_map.json 中 filename->doi）
  4. PDF 内部文本提取的 DOI（可选，需 pdftotext，默认关闭，慢）

用法:
  python3 scripts/check_pdf_coverage.py [--out missing_pdfs.csv] [--with-text]
"""
import os, re, sys, csv, json, glob, argparse

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def ms_to_doi(fn_base):
    """解析 ms- 命名 PDF（ms-10-1002_advs-77339.pdf）-> DOI 10.1002/advs.77339.
    规则: 去 'ms-' 前缀; '10-<registrant>_' 的 '-'/'_' 转 '.'/'/';
    其余 '_' -> '/', 其余 '-' -> '.'."""
    b = fn_base[:-4] if fn_base.lower().endswith('.pdf') else fn_base
    if b.startswith('ms-'):
        b = b[3:]
    m = re.match(r'^(10)-(\d{3,})_(.+)$', b)
    if not m:
        return None
    rest = m.group(3).replace('-', '.')
    return f'{m.group(1)}.{m.group(2)}/{rest}'

def collect_pdf_records():
    """返回 list of {path, doi_guess} 所有 raw 下 PDF。"""
    records = []
    pat = re.compile(r'(10[._]\d{4,}/?[0-9]+[^\s._]*|[1-9][0-9]+\s*\([0-9]+\))')
    for root, dirs, files in os.walk(f'{BASE}/raw'):
        for f in files:
            if not f.lower().endswith('.pdf'):
                continue
            full = os.path.join(root, f)
            rec = {'file': f, 'path': full, 'doi': None, 'pii': None}
            # DOI in filename
            m = re.search(r'(10[._]\d{4,}[._/][A-Za-z0-9_.\-]+)', f)
            if m:
                rec['doi'] = m.group(1).replace('_', '/')
            # ms- 命名回退 (2026-08-24): ms-10-1002_advs-77339.pdf
            if not rec['doi'] and f.startswith('ms-'):
                rec['doi'] = ms_to_doi(f)
            # PII in filename: 1-s2.0-XXXX-main
            mp = re.search(r'(?:1-s2\.0-)([A-Z]\d{5,})(?:-main)?', f)
            if mp:
                rec['pii'] = mp.group(1)
            records.append(rec)

    # 各 done：加载 *map.json / doi 映射
    mapa = {}  # filename -> doi
    for jf in glob.glob(f'{BASE}/raw/**/*map*.json', recursive=True) + \
             glob.glob(f'{BASE}/raw/**/*doi*.json', recursive=True):
        try:
            d = json.load(open(jf, encoding='utf-8'))
            if isinstance(d, dict):
                for k, v in d.items():
                    if isinstance(v, str) and v.lower().startswith('10.') and k.lower().endswith('.pdf'):
                        mapa[os.path.basename(k)] = v
        except Exception:
            pass
    for rec in records:
        rec['doi'] = rec['doi'] or mapa.get(rec['file'])

    # doi_survey.csv (中文命名 PDF 的 filename->doi 映射)
    # 2026-08-24: 结构整理后移到 maps/，兼容新/旧路径
    for sp in [f'{BASE}/raw/papers/maps/doi_survey.csv',
               f'{BASE}/raw/papers/metabolism/doi_survey.csv']:
        if not os.path.exists(sp):
            continue
        for row in csv.DictReader(open(sp, encoding='utf-8')):
            fn = row.get('file', '') or row.get('filename', '')
            if fn.lower().endswith('.pdf') and row.get('doi', '').startswith('10.'):
                mapa[os.path.basename(fn)] = row['doi'].strip()
    for rec in records:
        if not rec['doi']:
            rec['doi'] = mapa.get(rec['file'])
    return records

def collect_concepts():
    """概念页 -> {doi, title, source, file}"""
    out = []
    for fp in sorted(glob.glob(f'{BASE}/concepts/papers/*.md')) + \
             sorted(glob.glob(f'{BASE}/concepts/daily-*.md')):
        try:
            c = open(fp, encoding='utf-8', errors='ignore').read(4000)
        except Exception:
            continue
        dm = re.search(r'^doi:\s*(10\.\d{4,}/[^\s\n]+)', c, re.M | re.I)
        if not dm:
            continue
        doi = dm.group(1).strip().rstrip('./')
        src = re.search(r'^source:\s*(.+)', c, re.M | re.I)
        tt = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', c, re.M | re.I)
        out.append({'doi': doi,
                    'title': (tt.group(1).strip() if tt else doi)[:120],
                    'source': (src.group(1).strip() if src else ''),
                    'file': os.path.basename(fp)})
    return out

def has_pdf(doi, pdf_records):
    """判断 doi 是否已有 PDF。"""
    doi_lower = doi.lower()
    # exact + variants
    variants = {doi_lower, doi_lower.replace('/','_')}
    # 连字符/点号归一化 (ms- 解析 PDF 用 '.'，概念页可能用 '-'，2026-08-24)
    norm = doi_lower.replace('-', '.')
    for r in pdf_records:
        if not r['doi']:
            continue
        d = r['doi'].lower()
        if d in variants:
            return True
        # partial article-id match (doi suffix)
        suffix = doi_lower.rsplit('/', 1)[-1] if '/' in doi_lower else doi_lower
        if suffix and len(suffix) >= 10 and suffix in d:
            return True
        # 归一化部分匹配: 期刊号.文章号 的 '-'/'.' 变体
        d_norm = d.replace('-', '.')
        if norm and len(norm) >= 12 and norm in d_norm:
            return True
    return False

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default='missing_pdfs.csv')
    ap.add_argument('--with-text', action='store_true', help='用pdftotext提取PDF DOI(慢)')
    args = ap.parse_args()

    print('[1/3] 收集 raw/ 下所有 PDF...')
    pdfs = collect_pdf_records()
    print(f'      共 {len(pdfs)} 个 PDF；可识别DOI的: {sum(1 for r in pdfs if r["doi"])}')
    if args.with_text:
        # 对无DOI文件名PDF做内容提取(慢,可选)
        import subprocess
        for r in pdfs:
            if r['doi']:
                continue
            p = subprocess.run(['pdftotext', r['path'], '-'], capture_output=True, text=True, timeout=60)
            m = re.search(r'10\.\d{4,}/[A-Za-z0-9_.\-]+', p.stdout)
            if m:
                r['doi'] = m.group(0)

    print('[2/3] 收集概念页 DOI...')
    concepts = collect_concepts()
    print(f'      共 {len(concepts)} 个有 DOI 的概念页')

    print('[3/3] 比对缺失...')
    have, missing = [], []
    for c in concepts:
        (have if has_pdf(c['doi'], pdfs) else missing).append(c)

    cov = len(have) / len(concepts) * 100 if concepts else 0
    print(f'\n覆盖率: {len(have)}/{len(concepts)} = {cov:.1f}%\n缺失: {len(missing)}')

    out = args.out if os.path.isabs(args.out) else os.path.join(BASE, args.out)
    with open(out, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=['doi', 'title', 'source', 'file'])
        w.writeheader()
        w.writerows(missing)
    print(f'缺失清单已写入: {out}')

    # 同步输出纯 DOI 列表(供下载脚本用)
    doi_txt = os.path.join(BASE, 'missing_dois.txt')
    with open(doi_txt, 'w') as f:
        for c in missing:
            f.write(c['doi'] + '\n')
    print(f'缺失DOI列表: {doi_txt} ({len(missing)} 行)')

if __name__ == '__main__':
    main()
