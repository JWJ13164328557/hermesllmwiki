#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
download_epmc.py — 用 Europe PMC 批量下载 PDF (稳定 OA 通道，成功率 ~70-90%)
=================================================================================
用法:
    /usr/bin/python3 scripts/download_epmc.py --from-file <dois.txt> [--outdir raw/papers/daily_new]
    /usr/bin/python3 scripts/download_epmc.py --all-missing            # 概念页缺PDF的(默认all_pdfs)
选项:
    --all-missing   扫描 concepts/papers/ 里所有缺 PDF 的概念页 DOI
    --from-file F   从文本文件读 DOI(每行一个)
    --outdir DIR    输出目录(默认 raw/papers/all_pdfs)
为什么用 Europe PMC: OpenAlex 给的 best_oa_location 大多返回 HTML 付费墙(反爬)，
但 Europe PMC 的 ?pdf=render 对 PMC 收录文献可稳定返回 %PDF (>70% 成功率)。

流程: DOI → Europe PMC REST 查 PMC ID → europepmc.org/articles/PMCxxx?pdf=render 下载 → 验证 %PDF
"""
import os, re, json, sys, time, glob, argparse, urllib.request, urllib.parse

BASE = '/mnt/g/hermes_obsidian/hermes'
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"


def norm_doi(doi):
    return doi.rstrip('/').replace('/', '_').replace('.', '-')


# 已知非植物期刊 DOI 前缀（防盗污染；主过滤靠 theme_filter，这里是硬黑名单兜底）
# Springer 等医学/水产/物理/材料期刊：`10.1007/s10803-*` 等
NONPLANT_DOI_PREFIX = [
    # 医学
    '10.1007/s10803','10.1007/s00125','10.1007/s00247','10.1007/s00330','10.1007/s00431',
    '10.1007/s00415','10.1007/s00134','10.1007/s00520','10.1007/s00787','10.1007/s00439',
    '10.1007/s00262','10.1007/s10620','10.1007/s00464','10.1007/s00391','10.1007/s00823',
    # 水产/珊瑚/海洋动物
    '10.1007/s12562','10.1007/s00338','10.1007/s00227','10.1007/s10152','10.1007/s10228',
    # 物理/材料(植物提取物做材料不算植物生信)
    '10.1007/s10971','10.1007/s10853','10.1007/s00339',
    # 结构/膜生物化学
    '10.1007/s00232',
    # 2026-08-26 增量: 本次污染清理(糖尿病/医学/掠夺刊/流行病)发现的非植物前缀
    '10.51601',        # IJSE 掠夺刊(糖尿病SVM)
    '10.1253',         # Circ Reports 循环医学
    '10.5114',         # Archives of Medical Science 医学
    '10.15167',        # 意大利医学刊
    '10.5281/zenodo',  # Zenodo 归档(病毒/医学预印, HAA哲学)
    '10.3389/fepid',   # Frontiers in Epidemiology 流行病
    '10.1016/j.toxrep',# Toxicology Reports
]


def is_plant_doi(doi):
    """检查 DOI 是否命中非植物期刊黑名单前缀（硬拦截，快速）"""
    dl = doi.lower()
    return not any(dl.startswith(p) for p in NONPLANT_DOI_PREFIX)


def epmc_pmcid(doi):
    """DOI → Europe PMC PMC ID (None 若无)"""
    try:
        url = ('https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:'
               + urllib.parse.quote(doi) + '&format=json&pageSize=1')
        req = urllib.request.Request(url, headers={'User-Agent':'hermes-kb (mailto:dev@example.com)'})
        with urllib.request.urlopen(req, timeout=15) as r:
            d = json.loads(r.read().decode())
        res = d.get('resultList', {}).get('result', [])
        return res[0]['pmcid'] if res and res[0].get('pmcid') else None
    except Exception:
        return None


def download_pdf(pmcid, outdir):
    """下载 Europe PMC PDF, 验证 %PDF 头, 返回 (ok, filename)"""
    num = pmcid.replace('PMC', '')
    url = f'https://europepmc.org/articles/PMC{num}?pdf=render'
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': UA, 'Accept': 'application/pdf,*/*'})
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
        if data[:4] != b'%PDF':
            return False, 'not-pdf'
        fn = f'PMC{num}.pdf'
        with open(os.path.join(outdir, fn), 'wb') as f:
            f.write(data)
        return True, fn
    except Exception as e:
        return False, f'ERR {str(e)[:30]}'


def collect_missing_dois():
    """扫描概念页 void 有 DOI 但 all_pdfs 无 PDF 的"""
    pdf_doi = set()
    for f in os.listdir(f'{BASE}/raw/papers/all_pdfs'):
        if f.endswith('.pdf'):
            m = re.search(r'(10\.\d{4,}[^\s/]+)', f)
            if m:
                pdf_doi.add(m.group(1).replace('_', '/').rstrip('.').replace('.pdf', '').lower())
    missing = []
    for fp in glob.glob(f'{BASE}/concepts/papers/*.md'):
        c = open(fp, encoding='utf-8', errors='ignore').read(1500)
        dm = re.search(r'^doi:\s*"?\s*(10\.\d{4,}/[^\s"\n`]+)', c, re.M)
        if dm:
            d = dm.group(1).strip().rstrip('./')
            if d.lower() not in pdf_doi:
                missing.append(d)
    return sorted(set(missing))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--from-file', help='DOI 列表文件(每行一个)')
    ap.add_argument('--all-missing', action='store_true', help='扫描缺PDF的概念页DOI')
    ap.add_argument('--outdir', default='raw/papers/all_pdfs')
    args = ap.parse_args()

    if args.all_missing:
        dois = collect_missing_dois()
    elif args.from_file:
        dois = [l.strip() for l in open(args.from_file) if l.strip() and l.startswith('10.')]
    else:
        print("需 --from-file 或 --all-missing"); sys.exit(1)

    outdir = f'{BASE}/{args.outdir}'
    os.makedirs(outdir, exist_ok=True)

    # 跳过已存在(PDF格式)
    existing = set()
    for f in os.listdir(outdir):
        if f.endswith('.pdf'):
            m = re.search(r'(10\.\d{4,}[^\s/]+)', f)
            if m: existing.add(m.group(1).replace('_','/').rstrip('.').replace('.pdf','').lower())

    todo = [d for d in dois if d.lower() not in existing]
    # ⚠️ 防污染: 过滤非植物期刊(医学/水产/物理等) — 2026-08-25 审稿发现引入自闭症/水产PDF
    # is_plant_doi 用 DOI 前缀硬黑名单快速拦截(主过滤 theme_filter 在概念页导入层做)
    before = len(todo)
    clean = [d for d in todo if is_plant_doi(d)]
    skipped_pollution = before - len(clean)
    todo = clean
    if skipped_pollution:
        print(f"  ⛔ 跳过 {skipped_pollution} 个非植物期刊 DOI (防污染)")
    # 但 Europe PMC 下载的用 PMC 文件名, 也用 PMC ID 检查是否已有
    print(f"输入 DOI: {before}, 过滤后待处理: {len(todo)}")

    ok = fail = pmc_none = 0
    fail_log = []
    for i, doi in enumerate(todo, 1):
        # 检查是否已有(PMC编号文件)
        pmc = epmc_pmcid(doi)
        if not pmc:
            pmc_none += 1
            if i % 30 == 0:
                print(f"  ...{i}/{len(todo)} OK={ok} FAIL={fail} noPMC={pmc_none}", flush=True)
            time.sleep(0.12)
            continue
        # 已有同PMC文件则跳过
        out_fp = os.path.join(outdir, f'PMC{pmc[3:]}.pdf')
        if os.path.exists(out_fp):
            ok += 1
            time.sleep(0.1)
            continue
        done, res = download_pdf(pmc, outdir)
        if done:
            ok += 1
        else:
            fail += 1; fail_log.append((doi, pmc, res))
        if i % 30 == 0:
            print(f"  ...{i}/{len(todo)} OK={ok} FAIL={fail} noPMC={pmc_none}", flush=True)
        time.sleep(0.2)

    print(f"\n=== Europe PMC 下载完成 ===")
    print(f"  有PMC可下且成功: {ok}")
    print(f"  下载失败: {fail}")
    print(f"  无PMC(不走此通道): {pmc_none}")
    print(f"  → 待其他通道(OpenAlex/Sci-Hub)处理: {fail + pmc_none}")
    if fail_log:
        with open(f'{BASE}/.epmc_fail.log', 'w') as fh:
            for d, p, r in fail_log: fh.write(f"{d}\t{p}\t{r}\n")
    return ok


if __name__ == '__main__':
    main()
