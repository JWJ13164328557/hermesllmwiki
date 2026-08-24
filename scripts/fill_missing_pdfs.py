#!/usr/bin/env python3
"""
增量补齐缺失 PDF 脚本 (2026-08-24)
==================================
全库 PDF 完整性核查 + 缺失自动补齐 + 下载后深度提炼。

流程:
  1. 重新扫描概念页 DOI → 生成当前缺失清单 (调用 check_pdf_coverage.py)
  2. 复用最强多通道下载逻辑 (import download_pdf_batch 的 download_one):
       UnPaywall → OpenAlex → Europe PMC/PMC → Semantic Scholar → [Sci-Hub 可选]
  3. %PDF 魔数校验, 失败自动降级到下一通道
  4. 断点续传: 已有有效 PDF 直接跳过, 仅处理当前缺失
  5. 下载完成后对新增 PDF 走增量深度提炼 (deep_curate_all.py --dois)

用法 (必须用绝对路径 python3, 见技能陷阱):
  cd /mnt/g/hermes_obsidian/hermes
  # 只做核查 (不下载)
  /usr/bin/python3 -u scripts/fill_missing_pdfs.py --scan-only

  # 核查 + 补齐 (UnPaywall/OpenAlex/EPMC/S2, 无 Sci-Hub)
  /usr/bin/python3 -u scripts/fill_missing_pdfs.py --outdir raw/papers/fill_missing \
      --workers 8 --limit 200 2>&1 | tee /tmp/fill_missing.log

  # 小批量验证: 先跑 50 篇看成功率
  /usr/bin/python3 -u scripts/fill_missing_pdfs.py --outdir raw/papers/fill_missing \
      --limit 50 2>&1 | tee /tmp/fill_test.log

  # 启用 Sci-Hub 闭源兜底 (合规需人工确认)
  /usr/bin/python3 -u scripts/fill_missing_pdfs.py --outdir raw/papers/fill_missing \
      --scihub --workers 4 2>&1 | tee /tmp/fill_scihub.log
"""
import os, sys, re, csv, glob, time, argparse, concurrent.futures

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = f'{BASE}/scripts'

def log(msg):
    print(f'[{time.strftime("%H:%M:%S")}] {msg}', flush=True)

def load_module(name):
    """导入同目录脚本模块 (download_pdf_batch 等)."""
    sys.path.insert(0, SCRIPTS)
    import importlib
    return importlib.import_module(name)

def run_scan(out_csv):
    """调用 check_pdf_coverage.py 生成缺失清单, 返回缺失 DOI 列表."""
    import subprocess
    r = subprocess.run(
        [sys.executable, f'{SCRIPTS}/check_pdf_coverage.py', '--out', out_csv],
        capture_output=True, text=True, timeout=900, cwd=BASE
    )
    # 打印扫描概要
    for line in (r.stdout or '').splitlines()[-8:]:
        log(f'  scan> {line}')
    if r.returncode != 0:
        log(f'  ⚠ 扫描返回码 {r.returncode}: {r.stderr[-500:]}')
    # 读取缺失 DOI
    dois = []
    if os.path.exists(out_csv):
        with open(out_csv, encoding='utf-8-sig') as f:
            for row in csv.DictReader(f):
                d = (row.get('doi') or '').strip()
                if d.startswith('10.'):
                    dois.append(d)
    return dois

def find_valid_pdf_dois(outdir):
    """统计 outdir 下已有有效 PDF 的 DOI (断点续传)."""
    have = set()
    if not os.path.isdir(outdir):
        return have
    for f in os.listdir(outdir):
        if not f.endswith('.pdf'):
            continue
        fp = os.path.join(outdir, f)
        try:
            with open(fp, 'rb') as fh:
                if fh.read(4) == b'%PDF':
                    # DOI下划线文件名 -> DOI
                    d = f[:-4].replace('_', '/')
                    have.add(d)
        except Exception:
            continue
    return have

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--outdir', default='raw/papers/fill_missing',
                    help='PDF 输出目录 (相对 BASE)')
    ap.add_argument('--limit', type=int, default=0, help='只处理前 N 条缺失 DOI (验证用)')
    ap.add_argument('--offset', type=int, default=0, help='跳过前 N 条缺失 DOI (分批推进)')
    ap.add_argument('--workers', type=int, default=8)
    ap.add_argument('--scihub', dest='scihub', action='store_true', default=True,
                    help='启用 Sci-Hub 闭源兜底 (默认开启)')
    ap.add_argument('--no-scihub', dest='scihub', action='store_false',
                    help='禁用 Sci-Hub 兜底 (仅用免费通道)')
    ap.add_argument('--scan-only', action='store_true', help='只核查, 不下载')
    ap.add_argument('--skip-deep', action='store_true', help='下载后跳过深度提炼 (默认提炼)')
    ap.add_argument('--scan-out', default='/tmp/coverage_scan.csv',
                    help='覆盖率扫描输出 CSV 路径')
    ap.add_argument('--from-file', help='直接从缺失DOI列表文件读取 (跳过重新扫描, 默认读 missing_dois.txt)')
    args = ap.parse_args()

    outdir = args.outdir if os.path.isabs(args.outdir) else os.path.join(BASE, args.outdir)

    # ── 1. 核查缺失 ──
    log('=== 步骤 1: 全库 PDF 完整性核查 ===')
    missing = []
    if args.from_file is not None:
        src = args.from_file if os.path.isabs(args.from_file) else os.path.join(BASE, args.from_file)
        for ln in open(src, encoding='utf-8', errors='ignore'):
            d = ln.strip()
            if d.startswith('10.'):
                missing.append(d)
        log(f'从文件读取 {len(missing)} 个 DOI ({src})')
    else:
        missing = run_scan(args.scan_out)
        log(f'缺失 PDF 总数: {len(missing)}')

    # ── 1.5 DOI 清洗: 去除非 ASCII / 污染后缀 ──
    def clean_doi(d):
        d = re.sub(r'[^\x00-\x7F].*$', '', d)          # 去中文及之后
        d = re.sub(r'status:.*$', '', d)
        d = d.strip().rstrip('.,;/')
        return d
    cleaned = []
    seen = set()
    for d in missing:
        d = clean_doi(d)
        if not re.match(r'^10\.\d{4,9}/', d):
            continue
        if len(d) > 80 or d in seen:
            continue
        seen.add(d); cleaned.append(d)
    removed = len(missing) - len(cleaned)
    if removed:
        log(f'DOI 清洗: 剔除 {removed} 个污染/重复条目, 剩余 {len(cleaned)}')
    missing = cleaned

    # ── 2. 断点续传: 已有有效 PDF 跳过 ──
    have = find_valid_pdf_dois(outdir)
    if have:
        before = len(missing)
        missing = [d for d in missing if d not in have]
        log(f'断点续传: outdir 已有 {len(have)} 篇, 待下载 {len(missing)} (此前 {before})')

    if args.scan_only or not missing:
        log('scan_only 或无需下载, 结束.')
        return

    if args.offset:
        missing = missing[args.offset:]
        log(f'--offset {args.offset}: 跳过前 {args.offset} 篇, 剩余 {len(missing)}')
    if args.limit:
        missing = missing[:args.limit]
        log(f'--limit {args.limit}: 本次仅处理前 {len(missing)} 篇')

    os.makedirs(outdir, exist_ok=True)

    # ── 3. 多通道下载 (复用 download_pdf_batch) ──
    log(f'=== 步骤 3: 多通道下载 ({len(missing)} 篇, workers={args.workers}, '
        f'scihub={args.scihub}) ===')
    dmod = load_module('download_pdf_batch')
    results = []
    if args.workers > 1 and len(missing) > 1:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as ex:
            futs = {ex.submit(dmod.download_one, d, outdir, args.scihub): d for d in missing}
            done = 0
            for fu in concurrent.futures.as_completed(futs):
                results.append(fu.result())
                done += 1
                if done % 50 == 0:
                    log(f'  进度 {done}/{len(missing)}')
    else:
        for d in missing:
            results.append(dmod.download_one(d, outdir, args.scihub))

    ok = [r for r in results if r[1] != 'FAIL']
    fail = [r for r in results if r[1] == 'FAIL']
    log(f'下载完成: ✅ {len(ok)} 成功 / ❌ {len(fail)} 失败 / 共 {len(results)}')

    # 写统计报告
    rep = os.path.join(outdir, 'fill_missing_report.csv')
    with open(rep, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=['doi', 'status', 'method', 'path'])
        w.writeheader()
        for doi, how, dest in ok:
            w.writerow({'doi': doi, 'status': 'ok', 'method': how, 'path': dest})
        for doi, _, _ in fail:
            w.writerow({'doi': doi, 'status': 'fail', 'method': '', 'path': ''})
    log(f'报告: {rep}')

    if args.skip_deep or not ok:
        if not ok:
            log('本轮无新增 PDF (全失败或已存在), 跳过深度提炼.')
        return

    # ── 4. 增量深度提炼新增 PDF ──
    new_ok_dois = [r[0] for r in ok]
    dois_file = f'{BASE}/.fill_new_dois.txt'
    with open(dois_file, 'w') as fh:
        fh.write('\n'.join(new_ok_dois))
    log(f'=== 步骤 4: 增量深度提炼 {len(new_ok_dois)} 篇新增 PDF ===')
    import subprocess
    r = subprocess.run(
        [sys.executable, '-u', f'{SCRIPTS}/deep_curate_all.py', '--dois', dois_file],
        capture_output=True, text=True, timeout=3600, cwd=BASE
    )
    log(f'deep_curate_all 完成 (返回码 {r.returncode})')
    for line in (r.stdout or '').splitlines()[-15:]:
        log(f'  curate> {line}')
    if r.stderr:
        log(f'  stderr tail: {r.stderr[-500:]}')

    log('=== fill_missing_pdfs 完成 ===')

if __name__ == '__main__':
    main()
