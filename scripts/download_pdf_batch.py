#!/usr/bin/env python3
"""
增强版批量 PDF 下载脚本（多通道整合）
====================================
按 DOI 批量下载论文全文 PDF。整合多条自动通道，任一成功即得真实 PDF。

通道优先级（每条都做 %PDF 魔数校验，失败自动降级到下一通道）:
  1. UnPaywall API  (新)   — 聚合 gold/bronze/hybrid/green OA, 免key, 直链最可靠
  2. OpenAlex API   (新)   — open_access.pdf_url 检测
  3. Europe PMC     (已有) — isOpenAccess + pmcid 全文
  4. Semantic Scholar      — openAccessPdf
  5. Sci-Hub        (兜底) — citation_pdf_url 提取 (默认关闭, 连通/合规需人工确认)

校验: 所有下载物必须通过 head -c4 == %PDF 校验；HTML/Cloudflare 页判为失败。
并发: ThreadPoolExecutor, 默认 --workers 8。

用法:
  python3 scripts/download_pdf_batch.py --dois missing_dois.txt --out raw/papers/openalex_batch
  python3 scripts/download_pdf_batch.py --doi "10.1093/bib/bbz062"
  python3 scripts/download_pdf_batch.py --dois list.txt --limit 100   # 先小批量验证
"""
import os, re, sys, requests, argparse, concurrent.futures, time

UA = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                    '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
EMAIL = os.environ.get('UNPAYWALL_EMAIL', 'jiwj_hermes_kb@gmail.com')  # UnPaywall 要求的联系邮箱

def curl_get(url, timeout=25, stream=False, headers=None):
    h = dict(UA)
    if headers:
        h.update(headers)
    try:
        r = requests.get(url, headers=h, timeout=timeout, stream=stream, allow_redirects=True)
        r.raise_for_status()
        return r
    except Exception:
        return None

def is_valid_pdf(path):
    try:
        with open(path, 'rb') as f:
            return f.read(4) == b'%PDF'
    except Exception:
        return False

def save(session, url, dest, max_bytes=80_000_000, stream_timeout=60):
    """下载 url 到 dest, 返回 (ok, msg)。max_bytes/stream_timeout 防慢publisher/大文件卡死。"""
    try:
        r = curl_get(url, stream=True, headers={'Referer': 'https://doi.org/'})
        if r is None:
            return False, 'req-fail'
        os.makedirs(os.path.dirname(dest) or '.', exist_ok=True)
        wrote = 0
        t0 = time.time()
        with open(dest, 'wb') as f:
            for chunk in r.iter_content(chunk_size=65536):
                f.write(chunk)
                wrote += len(chunk)
                if wrote > max_bytes:
                    f.close(); os.remove(dest)
                    return False, 'too-big'
                if time.time() - t0 > stream_timeout:
                    f.close(); os.remove(dest)
                    return False, 'stream-timeout'
        if is_valid_pdf(dest):
            return True, f'PDF {r.status_code}'
        try:
            os.remove(dest)
        except OSError:
            pass
        return False, f'not-pdf ct={r.headers.get("Content-Type","")}'
    except Exception as e:
        try:
            os.remove(dest)
        except OSError:
            pass
        return False, f'err {type(e).__name__}'

# ---------------- 通道实现 ----------------
def channel_unpaywall(doi):
    url = f'https://api.unpaywall.org/v2/{requests.utils.quote(doi, safe="")}?email={EMAIL}'
    r = curl_get(url)
    if not r:
        return None
    try:
        d = r.json()
    except Exception:
        return None
    loc = d.get('best_oa_location') or {}
    return loc.get('url_for_pdf') or loc.get('url')

def channel_openalex(doi):
    url = f'https://api.openalex.org/works/doi:{requests.utils.quote(doi, safe="")}'
    r = curl_get(url)
    if not r:
        return None
    try:
        d = r.json()
    except Exception:
        return None
    if not d.get('open_access', {}).get('is_oa'):
        return None
    # 收集所有 pdf_url
    for loc in d.get('locations', []) or []:
        u = loc.get('pdf_url')
        if u:
            return u
    pl = (d.get('primary_location') or {}).get('pdf_url')
    return pl

def channel_europepmc(doi):
    url = ('https://www.ebi.ac.uk/europepmc/webservices/rest/search'
           f'?query=DOI:{requests.utils.quote(doi, safe="")}&format=json')
    r = curl_get(url)
    if not r:
        return None
    try:
        res = r.json().get('resultList', {}).get('result', [])
        if not res:
            return None
        rec = res[0]
        pmcid = rec.get('pmcid')
        # 优先 Europe PMC 渲染 PDF 服务 — 返回真实裸 PDF, requests 可穿透 (2026-08-24 实测)
        # 比出版社反爬链接(HTML) 和 NCBI /pdf/ (HTML) 都可靠
        if pmcid:
            return f'https://europepmc.org/articles/{pmcid}?pdf=render'
        if rec.get('isOpenAccess') != 'Y':
            return None
        fl = rec.get('fullTextUrlList', {}).get('fullTextUrl', []) or []
        for x in fl:
            if x.get('documentStyle') == 'pdf' and x.get('url'):
                return x['url']
    except Exception:
        return None
    return None

def channel_semanticscholar(doi):
    url = (f'https://api.semanticscholar.org/graph/v1/paper/DOI:{requests.utils.quote(doi, safe="")}'
           '?fields=openAccessPdf,isOpenAccess')
    r = curl_get(url)
    if not r:
        return None
    try:
        d = r.json()
        if d.get('openAccessPdf') and d['openAccessPdf'].get('url'):
            return d['openAccessPdf']['url']
    except Exception:
        pass
    return None

def channel_scihub(doi, session):
    """Sci-Hub: 首页取 citation_pdf_url, 再用登录 cookie 拉存储域 PDF。"""
    for domain in ('https://sci-hub.cat/', 'https://sci-hub.ru/', 'https://sci-hub.st/'):
        try:
            r = session.get(domain + doi, headers=UA, timeout=20)
            if r.status_code != 200:
                continue
            m = re.search(r'citation_pdf_url"\s+content="([^"]+)"', r.text) or \
                re.search(r'<meta name="citation_pdf_url" content="([^"]+)"', r.text)
            if m:
                return m.group(1)
        except Exception:
            continue
    return None

# ---------------- 下载单个 DOI ----------------
def download_one(doi, outdir, use_scihub):
    safe = doi.replace('/', '_').replace(':', '_')
    dest = os.path.join(outdir, safe + '.pdf')
    if os.path.exists(dest) and is_valid_pdf(dest):
        return (doi, 'already-have', dest)

    # 1. UnPaywall
    u = channel_unpaywall(doi)
    if u:
        ok, msg = save(None, u, dest)
        if ok:
            return (doi, f'unpaywall {msg}', dest)

    # 2. OpenAlex
    u = channel_openalex(doi)
    if u:
        ok, msg = save(None, u, dest)
        if ok:
            return (doi, f'openalex {msg}', dest)

    # 3. Europe PMC / PMC
    u = channel_europepmc(doi)
    if u:
        ok, msg = save(None, u, dest)
        if ok:
            return (doi, f'europepmc {msg}', dest)

    # 4. Semantic Scholar
    u = channel_semanticscholar(doi)
    if u:
        ok, msg = save(None, u, dest)
        if ok:
            return (doi, f's2 {msg}', dest)

    # 5. Sci-Hub
    if use_scihub:
        try:
            s = requests.Session()
            u = channel_scihub(doi, s)
            if u:
                ok, msg = save(s, u, dest)
                if ok:
                    return (doi, f'scihub {msg}', dest)
        except Exception:
            pass

    return (doi, 'FAIL', None)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--doi', help='单个 DOI')
    ap.add_argument('--dois', help='DOI 列表文件 (每行一个)')
    ap.add_argument('--out', default='raw/papers/openalex_batch')
    ap.add_argument('--limit', type=int, default=0, help='只处理前 N 条')
    ap.add_argument('--workers', type=int, default=8)
    ap.add_argument('--scihub', action='store_true', help='启用 Sci-Hub 闭源兜底')
    args = ap.parse_args()

    if args.doi:
        dois = [args.doi]
    elif args.dois:
        dois = []
        for l in open(args.dois):
            m = re.match(r'(10\.\d{4,9}/[0-9A-Za-z._()\-/:]+)', l.strip())
            if m:
                d = m.group(1).rstrip('.,;')
                if d not in dois and len(d) < 80:
                    dois.append(d)
    else:
        print('需提供 --doi 或 --dois'); sys.exit(1)
    if args.limit:
        dois = dois[:args.limit]

    outdir = args.out if os.path.isabs(args.out) else os.path.join(os.getcwd(), args.out)
    os.makedirs(outdir, exist_ok=True)

    t0 = time.time()
    results = []
    if args.workers > 1 and len(dois) > 1:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as ex:
            futs = {ex.submit(download_one, d, outdir, args.scihub): d for d in dois}
            for fu in concurrent.futures.as_completed(futs):
                results.append(fu.result())
    else:
        for d in dois:
            results.append(download_one(d, outdir, args.scihub))

    ok = [r for r in results if r[1] != 'FAIL']
    fail = [r for r in results if r[1] == 'FAIL']
    print(f'\n===== 结果 {len(ok)} 成功 / {len(fail)} 失败 / 共 {len(results)} (耗时 {time.time()-t0:.0f}s) =====')
    for doi, how, dest in ok:
        print(f'  OK  [{how:20s}] {doi}')
    print('\n--- 失败 ---')
    for doi, _, _ in fail:
        print(f'  FAIL  {doi}')

    # 写统计
    with open(os.path.join(outdir, 'download_report.csv'), 'w', newline='', encoding='utf-8-sig') as f:
        w = __import__('csv').DictWriter(f, fieldnames=['doi', 'status', 'method', 'path'])
        w.writeheader()
        for doi, how, dest in ok:
            w.writerow({'doi': doi, 'status': 'ok', 'method': how, 'path': dest})
        for doi, how, _ in fail:
            w.writerow({'doi': doi, 'status': 'fail', 'method': how, 'path': ''})
    print(f'\n报告: {os.path.join(outdir, "download_report.csv")}')

if __name__ == '__main__':
    main()
