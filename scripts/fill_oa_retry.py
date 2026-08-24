#!/usr/bin/env python3
"""
增强 OA 重试: 对缺失文献中 OpenAlex 标记为 OA 的 DOI,
收集全部 location 的所有 pdf_url + UnPaywall url_for_pdf,
逐个尝试下载直到成功 (不因第一个死链而放弃).
用法:
  python3 scripts/fill_oa_retry.py --limit 200 --workers 8
  python3 scripts/fill_oa_retry.py --limit 200 --workers 8 --from-file missing_pdfs_OA.txt
"""
import os, re, sys, requests, argparse, concurrent.futures, time

BASE = '/mnt/g/hermes_obsidian/hermes'
OUTDIR = os.path.join(BASE, 'raw/papers/all_pdfs')
UA = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
EMAIL = os.environ.get('UNPAYWALL_EMAIL', 'jiwj_hermes_kb@gmail.com')
CHECKPOINT = os.path.join(BASE, '.fill_oa_retry_progress.txt')

def curl_get(url, timeout=25, stream=False):
    try:
        r = requests.get(url, headers=UA, timeout=timeout, stream=stream, allow_redirects=True)
        r.raise_for_status()
        return r
    except Exception:
        return None

def is_valid_pdf(path):
    try:
        return open(path, 'rb').read(4) == b'%PDF'
    except Exception:
        return False

def save(url, dest, max_bytes=80_000_000, stream_timeout=45):
    try:
        r = requests.get(url, headers={**UA, 'Referer': 'https://doi.org/'}, timeout=25,
                         stream=True, allow_redirects=True)
        r.raise_for_status()
        os.makedirs(os.path.dirname(dest) or '.', exist_ok=True)
        wrote = 0; t0 = time.time()
        with open(dest, 'wb') as f:
            for chunk in r.iter_content(65536):
                f.write(chunk); wrote += len(chunk)
                if wrote > max_bytes or time.time() - t0 > stream_timeout:
                    f.close(); os.remove(dest); return False, 'too-big/timeout'
        if is_valid_pdf(dest):
            return True, f'PDF {r.status_code}'
        os.remove(dest)
        return False, f'not-pdf'
    except Exception as e:
        try: os.remove(dest)
        except OSError: pass
        return False, type(e).__name__

def collect_urls(doi):
    """收集该 DOI 所有候选 PDF URL (OpenAlex 全部 locations + UnPaywall)"""
    urls = []
    # OpenAlex
    try:
        r = requests.get(f'https://api.openalex.org/works/doi:{requests.utils.quote(doi, safe="")}', headers=UA, timeout=25)
        d = r.json()
        if d.get('open_access', {}).get('is_oa'):
            for loc in d.get('locations', []) or []:
                pl = loc.get('pdf_url')
                if pl and pl not in urls:
                    urls.append(pl)
                hl = loc.get('landing_page_url') or loc.get('url')
                if hl and hl not in urls:
                    urls.append(hl)  # 出版社页面也可能直接给 PDF
    except Exception:
        pass
    # UnPaywall
    try:
        r = requests.get(f'https://api.unpaywall.org/v2/{requests.utils.quote(doi, safe="")}?email={EMAIL}', headers=UA, timeout=25)
        d = r.json()
        loc = d.get('best_oa_location') or {}
        for k in ('url_for_pdf', 'url'):
            v = loc.get(k)
            if v and v not in urls:
                urls.append(v)
    except Exception:
        pass
    return urls

def dl_one(doi):
    doi_clean = doi.strip().rstrip('./')
    if not re.match(r'^10\.\d{4,9}/', doi_clean) or len(doi_clean) > 80:
        return doi, 'skip-bad-doi', None
    dest = os.path.join(OUTDIR, doi_clean.replace('/', '_') + '.pdf')
    if os.path.exists(dest) and is_valid_pdf(dest):
        return doi, 'have', None
    urls = collect_urls(doi_clean)
    if not urls:
        return doi, 'no-urls', None
    for u in urls:
        if not u.startswith('http'):
            continue
        # pnas/nature/cell 出版社页, 尝试追加 PDF 参数或直接抓
        ok, msg = save(u, dest)
        if ok:
            return doi, 'ok', u
        # 尝试专门吸引出版社 HTML 回退: 有的 pdf_url 是 HTML, 加 &download=1 或替换
    return doi, 'fail', ', '.join(urls[:2])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--limit', type=int, default=200)
    ap.add_argument('--workers', type=int, default=8)
    ap.add_argument('--offset', type=int, default=0)
    ap.add_argument('--from-file', default=os.path.join(BASE, 'missing_pdfs_OA.txt'))
    args = ap.parse_args()

    dois = [l.strip() for l in open(args.from_file) if l.strip()]
    # 过滤已存在
    todo = []
    for d in dois:
        if not re.match(r'^10\.\d{4,9}/', d) or len(d) > 80: continue
        dest = os.path.join(OUTDIR, d.replace('/', '_') + '.pdf')
        if not (os.path.exists(dest) and is_valid_pdf(dest)):
            todo.append(d)
    todo = todo[args.offset: args.offset + args.limit]
    print(f'待下载: {len(todo)}')

    ok = 0; fail = 0
    t0 = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(dl_one, d): d for d in todo}
        for i, fut in enumerate(concurrent.futures.as_completed(futs), 1):
            doi, st, url = fut.result()
            if st == 'ok':
                ok += 1
            elif st == 'have':
                ok += 1
            else:
                fail += 1
            if i % 25 == 0:
                el = time.time() - t0
                print(f'  [{i}/{len(todo)}] ok={ok} fail={fail} {(time.time()-t0):.0f}s')
    print(f'DONE ok={ok} fail={fail} total={ok+fail} time={(time.time()-t0)/60:.1f}min')

if __name__ == '__main__':
    main()
