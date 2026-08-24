#!/usr/bin/env python3
"""精确按 DOI 批量下载 OA 全文 PDF —— Unpaywall 主通道 + Semantic Scholar 备用。
命名 raw/papers/{doi_slug}.pdf 供 deep_curate_all.py 匹配。
用法: python3 download_oa_today.py [--limit N] [--range S:E]
"""
import os, re, json, subprocess, time, sys, argparse

BASE = '/mnt/g/hermes_obsidian/hermes'
CONCEPTS_DIR = os.path.join(BASE, 'concepts', 'papers')
RAW_DIR = os.path.join(BASE, 'raw', 'papers')
os.makedirs(RAW_DIR, exist_ok=True)

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36'
REFERER = 'https://scholar.google.com/'

def curl(url, timeout=30, head=False):
    cmd = ['curl', '-s'+('I' if head else 'L'), '--max-time', str(timeout),
           '-A', UA, '--connect-timeout', '10', '-H', f'Referer: {REFERER}']
    if head:
        cmd += ['-H', 'Accept: application/pdf']
    cmd.append(url)
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout+10)
        if r.returncode == 0:
            return r.stdout
    except Exception:
        pass
    return None

def is_valid_pdf(raw):
    """HEAD 判断是否真 PDF 且体积足够"""
    code = '?'; ctype = ''; clen = 0; loc = ''
    for l in raw.split('\n'):
        if l.startswith('HTTP'):
            parts = l.split()
            if len(parts) > 1:
                code = parts[1]
        low = l.lower()
        if low.startswith('content-type'):
            ctype = l.split(':', 1)[1].strip() if ':' in l else ''
        if low.startswith('content-length'):
            try: clen = int(l.split(':', 1)[1].strip())
            except: pass
        if low.startswith('location'):
            loc = l.split(':', 1)[1].strip() if ':' in l else ''
    return code == '200' and 'pdf' in ctype and clen > 100000

def unpaywall_urls(doi):
    """Unpaywall：返回全部候选 PDF/landing URL（按可用性排序）。"""
    r = subprocess.run(['curl', '-s', '--max-time', '20',
                        f'https://api.unpaywall.org/v2/{doi}?email=research@hermes.local'],
                       capture_output=True, text=True)
    try:
        d = json.loads(r.stdout)
    except Exception:
        return []
    best = d.get('best_oa_location') or {}
    locs = [best] + (d.get('oa_locations') or [])
    OUT, BAD = [], ['wiley', 'sciencedirect', 'elsevier.com', 'linkinghub']
    pdfs, landings = [], []
    for l in locs:
        if not l: continue
        pf = (l.get('url_for_pdf') or '').strip()
        lu = (l.get('url') or '').strip()
        if pf and pf not in pdfs:
            pdfs.append(pf)
        if lu and lu not in landings and not any(x in lu for x in BAD):
            landings.append(lu)
    # pdf 优先，landing 次之
    out = pdfs + landings
    return out

def download(url, dest):
    """带法式下载，HTTP 失败返回 False。若落地是 HTML 则尝试从其提取 PDF 链接再下。"""
    def _curl(u, out):
        r = subprocess.run(['curl', '-sL', '--max-time', '60', '-A', UA,
                            '--connect-timeout', '10', '-H', f'Referer: {REFERER}',
                            '-o', out, '-w', '%{http_code} %{content_type}',
                            u], capture_output=True, text=True, timeout=75)
        return r.stdout.strip()
    meta = _curl(url, dest)
    for attempt in range(3):
        try:
            code = meta.split()[0]
        except Exception:
            code = '?'
        if code == '200' and os.path.exists(dest) and os.path.getsize(dest) > 50000:
            try:
                with open(dest, 'rb') as f:
                    head = f.read(4)
                if head == b'%PDF':
                    return True
            except Exception:
                pass
        # HTML? 尝试提取 PDF 链接
        try:
            html = open(dest, 'rb').read().decode('utf-8', 'ignore')
        except Exception:
            html = ''
        pdfm = None
        if html:
            # citation_pdf_url 最可靠
            m = re.search(r'citation_pdf_url"\s+content="([^"]+)"', html)
            if m: pdfm = m.group(1)
            else:
                m = re.search(r'href="([^"]+\.pdf[^"]*)"', html)
                if m: pdfm = m.group(1)
            if pdfm and not pdfm.startswith('http'):
                from urllib.parse import urljoin
                pdfm = urljoin(('http://' if url.startswith('http://') else 'https://')
                               + url.split('://')[1].split('/')[0], pdfm)
            if pdfm:
                meta = _curl(pdfm, dest)
                continue
        return False
    return False

def ss_pdf(doi):
    r = subprocess.run(['curl', '-s', '--max-time', '15',
                        f'https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}?fields=openAccessPdf'],
                       capture_output=True, text=True)
    try:
        d = json.loads(r.stdout)
        return (d.get('openAccessPdf') or {}).get('url', '') or None
    except Exception:
        return None

def try_download(doi, dest):
    """四通道候选 URL 逐一尝试下载：Unpaywall → OpenAlex(alt loc) → Semantic Scholar → Sci-Hub。"""
    candidates = []
    try: candidates += unpaywall_urls(doi)
    except Exception: pass
    try: candidates += openalex_pdf_urls(doi)
    except Exception: pass
    try:
        u = ss_pdf(doi)
        if u: candidates.append(u)
    except Exception: pass
    if not any('sci-hub' in c for c in candidates):
        try:
            u = scihub_pdf_url(doi)
            if u: candidates.append(u)
        except Exception: pass
    seen, src = set(), None
    for u in candidates:
        if u in seen: continue
        seen.add(u)
        if any(x in u for x in ['wiley.com', 'sciencedirect', 'linkinghub.elsevier', 'sci-hub']):
            continue
        if download(u, dest):
            return True, ('Sci-Hub' if 'sci-hub' in u else 'UP')
    return False, None

def scihub_available():
    """快速探测 Sci-Hub 是否真可用（非挑战页）。挑战页/被墙则整体返回 False。"""
    for base in ['https://sci-hub.wf/', 'https://sci-hub.se/', 'https://sci-hub.ru/']:
        r = subprocess.run(['curl', '-s', '-A', UA, '--max-time', '10',
                            '--connect-timeout', '5', base],
                           capture_output=True, text=True)
        h = r.stdout
        if h and 'Checking your browser' not in h and 'captcha' not in h and len(h) > 3000:
            return True
    return False

_SCI_HUB_OK = None
def scihub_pdf_url(doi):
    """Sci-Hub：抓 landing HTML，提取内嵌 PDF 链接。多镜像依次尝试。"""
    global _SCI_HUB_OK
    if _SCI_HUB_OK is None:
        _SCI_HUB_OK = scihub_available()
    if not _SCI_HUB_OK:
        return None
    mirrors = ['https://sci-hub.wf/', 'https://sci-hub.se/', 'https://sci-hub.ru/', 'https://sci-hub.st/']
    for base in mirrors:
        r = subprocess.run(['curl', '-sL', '-A', UA, '--max-time', '25',
                            '--connect-timeout', '8', f'{base}{doi}'],
                           capture_output=True, text=True)
        html = r.stdout
        if not html:
            continue
        # 1) <embed src="...pdf">
        m = re.search(r'<embed[^>]+src="([^"]*?"?[^"]*\.pdf[^"]*)"', html)
        if m and 'sci-hub' not in m.group(1):
            return m.group(1)
        # 2) #pdf iframe
        m = re.search(r'<iframe[^>]+id="pdf"[^>]+src="([^"]+)"', html)
        if m:
            return m.group(1)
        # 3) onclick src 提取
        m = re.search(r'location\.href\s*=\s*[\'"]([^\'"]+\.pdf[^\'"]*)[\'"]', html)
        if m:
            return m.group(1)
    return None

def openalex_pdf_urls(doi):
    """OpenAlex：从 locations 收集 pdf_url + landing_page_url（过滤反爬/付费墙域）。"""
    r = subprocess.run(['curl', '-s', '--max-time', '20',
                        'https://api.openalex.org/works/doi:' + doi],
                       capture_output=True, text=True)
    try:
        d = json.loads(r.stdout)
    except Exception:
        return []
    urls = []
    BAD = ['wiley', 'sciencedirect', 'linkinghub', 'elsevier']
    for loc in d.get('locations') or []:
        for k in ('pdf_url', 'landing_page_url'):
            u = (loc.get(k) or '').strip()
            if u and not any(x in u for x in BAD) and u not in urls:
                urls.append(u)
    return urls

def get_today_dois():
    """取最新 commit 新增的概念页 DOI"""
    out = subprocess.run('git diff --name-only --diff-filter=A HEAD~1 HEAD -- concepts/papers/',
                         shell=True, capture_output=True, text=True, cwd=BASE).stdout
    files = [l.strip() for l in out.split('\n') if l.strip()]
    dois = {}
    for f in files:
        p = os.path.join(BASE, f)
        if not os.path.exists(p): continue
        try:
            c = open(p, encoding='utf-8').read(8000)
        except: continue
        m = re.search(r'doi:\s*(10\.\d{4,}/[^\s\n]+)', c, re.I)
        if m:
            slug = f.replace('.md', '').split('/')[-1]
            dois[slug] = m.group(1).rstrip('./')
    return dois

def doi_slug(doi):
    return doi.replace('/', '_').replace('(', '_').replace(')', '_')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--limit', type=int, default=0)
    ap.add_argument('--range', default='')
    ap.add_argument('--start', type=int, default=0)
    args = ap.parse_args()

    papers = get_today_dois()
    items = list(papers.items())
    if args.start:
        items = items[args.start:]
    if args.range and ':' in args.range:
        s, e = args.range.split(':')
        items = items[int(s):int(e) if e else None]
    if args.limit:
        items = items[:args.limit]
    print(f"[{time.strftime('%H:%M:%S')}] 待处理: {len(items)} 篇")
    sys.stdout.flush()

    ok = 0; fail = 0; skip = 0; src = {}
    for i, (slug, doi) in enumerate(items, 1):
        dest = os.path.join(RAW_DIR, f'{slug}.pdf')
        if os.path.exists(dest) and os.path.getsize(dest) > 100000:
            skip += 1
            continue
        # 四通道：Unpaywall → OpenAlex(alt loc) → Semantic Scholar → Sci-Hub
        got, got_src = try_download(doi, dest)
        if got:
            ok += 1; src[got_src] = src.get(got_src, 0) + 1
            print(f"  [{time.strftime('%H:%M:%S')}] #{i} OK[{got_src}]  {slug}")
            sys.stdout.flush()
            continue
        fail += 1
        print(f"  [{time.strftime('%H:%M:%S')}] #{i} FAIL {doi}")
        sys.stdout.flush()
        time.sleep(1)
    print(f"\n=== DONE === OK={ok} FAIL={fail} SKIP={skip} 共{len(items)} 来源={src}")

if __name__ == '__main__':
    main()
