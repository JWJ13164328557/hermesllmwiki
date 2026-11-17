#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
oa_locate.py — 非 PMC 论文的开放获取全文定位（Unpaywall + OpenAlex）
=====================================================================
背景
----
phase4 原先只有 Europe PMC 一条通道。2026-11-06 / 11-07 连续两天
"全文获取 0/31、0/21"，根因不是下载逻辑坏了，而是当日 21 篇 DOI 全部
`no_pmc`——订阅制期刊没有 PMC 版本，而 "待其他通道(OpenAlex/Sci-Hub)处理"
只是日志里的一句打印，两个通道**从未实现**。

本脚本补上这个缺口：
    1) Unpaywall  /v2/{doi}?email=...   -> oa_locations[].url_for_pdf
    2) OpenAlex   /works/doi:{doi}      -> best_oa_location.pdf_url
逐个候选 URL 试下载，验证 %PDF 文件头与体积后落盘。

设计约束
--------
* **不接 Sci-Hub**：来源合法性不可控，且会让证据链无法对外说明。
* **只走开放获取**：Unpaywall/OpenAlex 返回的都是出版商或仓储的 OA 链接。
* **结果缓存**：一次查询落盘，重复运行不重复打 API（这些 API 有速率限制）。
* **失败可诊断**：每个 DOI 记录 no_oa / not_pdf / http_<code> / net_<err>。
* **幂等**：已存在全文（PDF 或 TXT）的 DOI 直接跳过。

用法
----
    python oa_locate.py --from-file dois.txt --outdir raw/papers/all_pdfs
    python oa_locate.py --from-file dois.txt --dry-run      # 只查不下载
"""
import argparse
import io
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb_paths import BASE  # noqa: E402

try:
    from download_epmc import is_plant_doi  # 复用同一个非植物前缀黑名单
except Exception:  # pragma: no cover
    def is_plant_doi(doi):
        return True

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
DEFAULT_MAILTO = 'hermes-kb@example.org'
MIN_PDF_BYTES = 20000


def slug(doi):
    """与 fetch_epmc_fulltext 的命名保持一致（只替换 '/'）。"""
    return doi.rstrip('./').replace('/', '_')


def norm_doi_key(x):
    return x.lower().replace('_', '/').rstrip('.')


def pdf_index(outdir):
    """已存在的 PDF 里抽出规范化 DOI，用于跳过重复下载。"""
    keys = set()
    try:
        names = os.listdir(outdir)
    except OSError:
        return keys
    for name in names:
        if not name.lower().endswith('.pdf'):
            continue
        m = re.search(r'(10\.\d{4,}[A-Za-z0-9._\-/]+)', name)
        if m:
            keys.add(norm_doi_key(m.group(1)))
    return keys


def text_index():
    """已存在的 JATS 纯文本全文（raw/papers/fulltext/*.txt）。"""
    d = os.path.join(BASE, 'raw', 'papers', 'fulltext')
    keys = set()
    try:
        names = os.listdir(d)
    except OSError:
        return keys
    for name in names:
        if name.endswith('.txt') and not name.startswith('_'):
            keys.add(norm_doi_key(name[:-4]))
    return keys


def http_json(url, timeout=25, retries=1):
    """GET JSON，带一次退避重试。

    2026-11-07 实测：22 个 DOI 连查时 OpenAlex 出现 14 个 404，而单独复查
    同一 DOI 可以正常返回——说明是瞬时限流被网关映射成 404，不是真的未收录。
    对 404/429/5xx 退避重试一次，避免把限流误记成"无 OA 版本"。
    """
    last = None
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': UA, 'Accept': 'application/json'})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode('utf-8', 'replace'))
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (404, 429, 500, 502, 503) and attempt < retries:
                time.sleep(2.0 * (attempt + 1))
                continue
            raise
        except Exception as e:
            last = e
            if attempt < retries:
                time.sleep(1.5)
                continue
            raise
    raise last


def unpaywall_candidates(doi, mailto):
    """返回 (candidates, reason)。candidates 为 None 表示查询本身失败。"""
    url = 'https://api.unpaywall.org/v2/%s?email=%s' % (
        urllib.parse.quote(doi, safe=''), urllib.parse.quote(mailto))
    try:
        d = http_json(url)
    except urllib.error.HTTPError as e:
        return None, 'unpaywall_http_%s' % e.code
    except Exception as e:
        return None, 'unpaywall_net_%s' % type(e).__name__
    if not d.get('is_oa'):
        return [], 'no_oa'
    out = []
    best = (d.get('best_oa_location') or {}).get('url_for_pdf')
    if best and best.startswith('http'):
        out.append({'url': best, 'kind': 'pdf', 'source': 'unpaywall:best'})
    for loc in d.get('oa_locations') or []:
        u_pdf = (loc.get('url_for_pdf') or '').strip()
        u_any = (loc.get('url') or '').strip()
        host = loc.get('host_type') or 'oa'
        if u_pdf.startswith('http'):
            out.append({'url': u_pdf, 'kind': 'pdf', 'source': 'unpaywall:%s' % host})
        elif u_any.startswith('http'):
            # 只有落地页：不含 PDF 直链。记为 landing，后续用 citation_pdf_url 解析。
            out.append({'url': u_any, 'kind': 'landing', 'source': 'unpaywall:%s' % host})
    return out, ('' if out else 'no_pdf_url')


def openalex_candidates(doi, mailto):
    url = 'https://api.openalex.org/works/doi:%s?mailto=%s' % (
        urllib.parse.quote(doi, safe=''), urllib.parse.quote(mailto))
    try:
        d = http_json(url)
    except urllib.error.HTTPError as e:
        return None, 'openalex_http_%s' % e.code
    except Exception as e:
        return None, 'openalex_net_%s' % type(e).__name__
    out = []
    best = (d.get('best_oa_location') or {}).get('pdf_url')
    if best and best.startswith('http'):
        out.append({'url': best, 'kind': 'pdf', 'source': 'openalex:best'})
    for loc in d.get('locations') or []:
        u = (loc.get('pdf_url') or '').strip()
        if u.startswith('http') and u != best:
            out.append({'url': u, 'kind': 'pdf', 'source': 'openalex:location'})
    if not out and (d.get('open_access') or {}).get('oa_url'):
        out.append({'url': d['open_access']['oa_url'], 'kind': 'landing',
                    'source': 'openalex:oa_url'})
    return out, ('' if out else 'no_oa')


_META_PDF = re.compile(
    r'<meta[^>]+(?:name|property)=["\'](?:citation_pdf_url|bepress_citation_pdf_url)["\'][^>]*'
    r'content=["\']([^"\']+)', re.I)
_META_PDF_REV = re.compile(
    r'<meta[^>]+content=["\']([^"\']+)["\'][^>]*'
    r'(?:name|property)=["\'](?:citation_pdf_url|bepress_citation_pdf_url)["\']', re.I)
_LINK_PDF = re.compile(
    r'<link[^>]+type=["\']application/pdf["\'][^>]*href=["\']([^"\']+)', re.I)
_LINK_PDF_REV = re.compile(
    r'<link[^>]+href=["\']([^"\']+)["\'][^>]*type=["\']application/pdf["\']', re.I)
_ANCHOR_PDF = re.compile(r'href=["\']([^"\']+\.pdf(?:\?[^"\']*)?)["\']', re.I)


def resolve_landing_pdf(url, timeout=30):
    """从落地页 HTML 里找 PDF 直链。

    只用确定性的元数据位置（Highwire/PRISM 的 citation_pdf_url、link[type=pdf]、
    以 .pdf 结尾的 href），不做启发式猜测，避免把广告/预览图当成全文。
    """
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': UA, 'Accept': 'text/html,application/xhtml+xml'})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read(600000)
            final = r.geturl()
    except Exception as e:
        return '', 'landing_net_%s' % type(e).__name__
    html = raw.decode('utf-8', 'replace')
    for rx in (_META_PDF, _META_PDF_REV, _LINK_PDF, _LINK_PDF_REV, _ANCHOR_PDF):
        m = rx.search(html)
        if m:
            cand = urllib.parse.urljoin(final, m.group(1).strip())
            if cand.startswith('http'):
                return cand, ''
    return '', 'landing_no_pdf_link'


def fetch_pdf(url, timeout=45):
    """下载并校验 PDF 头。返回 (bytes|None, reason)。"""
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': UA,
            'Accept': 'application/pdf,application/octet-stream;q=0.9,*/*;q=0.5'})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = r.read()
    except urllib.error.HTTPError as e:
        return None, 'http_%s' % e.code
    except Exception as e:
        return None, 'net_%s' % type(e).__name__
    if not data or data[:4] != b'%PDF':
        head = (data[:200] or b'').lstrip()
        if head[:1] == b'<':
            return None, 'not_pdf(html)'
        return None, 'not_pdf'
    if len(data) < MIN_PDF_BYTES:
        return None, 'too_small(%d)' % len(data)
    return data, ''


def load_cache(path):
    try:
        with io.open(path, encoding='utf-8') as fh:
            return json.load(fh)
    except Exception:
        return {}


def save_cache(path, cache):
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    tmp = path + '.tmp'
    with io.open(tmp, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(cache, fh, ensure_ascii=False, indent=1, sort_keys=True)
    os.replace(tmp, path)


def main():
    ap = argparse.ArgumentParser(description='OA 全文定位（Unpaywall + OpenAlex）')
    ap.add_argument('--from-file', required=True, help='DOI 列表文件（每行一个）')
    ap.add_argument('--outdir', default='raw/papers/all_pdfs')
    ap.add_argument('--mailto', default=DEFAULT_MAILTO, help='API 联系邮箱（礼貌标识）')
    ap.add_argument('--cache', default='raw/papers/maps/oa_locate_cache.json')
    ap.add_argument('--limit', type=int, default=0, help='最多处理 N 篇（0=不限）')
    ap.add_argument('--sleep', type=float, default=0.6)
    ap.add_argument('--dry-run', action='store_true', help='只查候选，不下载')
    a = ap.parse_args()

    outdir = os.path.join(BASE, a.outdir)
    os.makedirs(outdir, exist_ok=True)
    cache_path = os.path.join(BASE, a.cache)
    cache = load_cache(cache_path)

    dois = [l.strip() for l in io.open(a.from_file, encoding='utf-8')
            if l.strip().startswith('10.')]
    have_pdf = pdf_index(outdir)
    have_txt = text_index()
    todo = []
    skipped = 0
    for d in dict.fromkeys(dois):
        key = norm_doi_key(d)
        if key in have_pdf or key in have_txt:
            skipped += 1
            continue
        if not is_plant_doi(d):
            skipped += 1
            continue
        todo.append(d)
    if a.limit:
        todo = todo[:a.limit]

    print('输入 DOI: %d, 已有全文/越界跳过: %d, 待定位: %d' % (len(dois), skipped, len(todo)))

    stats = {'ok': 0, 'no_oa': 0, 'not_pdf': 0, 'failed': 0, 'cached': 0}
    reasons = {}
    hits_uw = hits_oa = 0
    for i, doi in enumerate(todo, 1):
        key = norm_doi_key(doi)
        rec = cache.get(key) or {}

        cands = []
        if not rec.get('unpaywall_checked'):
            uw, why = unpaywall_candidates(doi, a.mailto)
            rec['unpaywall_checked'] = True
            rec['unpaywall_reason'] = why
            if uw:
                hits_uw += 1
                cands.extend(uw)
            time.sleep(a.sleep)
        oa, why2 = openalex_candidates(doi, a.mailto)
        if oa:
            hits_oa += 1
            cands.extend(oa)
        time.sleep(a.sleep)

        # 去重候选：同一 URL 不重复下载
        seen, uniq = set(), []
        for c in cands:
            if c['url'] not in seen:
                seen.add(c['url'])
                uniq.append(c)

        if not uniq:
            rec.update({'status': 'no_oa',
                        'reason': why2 or rec.get('unpaywall_reason') or 'no_oa'})
            cache[key] = rec
            stats['no_oa'] += 1
            reasons[rec['reason']] = reasons.get(rec['reason'], 0) + 1
            if i % 20 == 0:
                print('  ...%d/%d ok=%d no_oa=%d' % (i, len(todo), stats['ok'], stats['no_oa']),
                      flush=True)
            continue

        if a.dry_run:
            rec.update({'status': 'candidate', 'source': uniq[0]['source'],
                        'url': uniq[0]['url'], 'n_candidates': len(uniq)})
            cache[key] = rec
            print('  [dry] %s -> %s' % (doi, uniq[0]['url'][:110]))
            continue

        got = None
        landing_tries = 0
        for cand in uniq[:8]:
            target = cand['url']
            if cand.get('kind') == 'landing':
                # 落地页最多解析 2 个，避免为同一篇文献反复抓 HTML。
                if landing_tries >= 2:
                    continue
                landing_tries += 1
                resolved, why_l = resolve_landing_pdf(target)
                if not resolved:
                    rec.setdefault('attempts', []).append(
                        {'url': target, 'reason': why_l})
                    continue
                target = resolved
            data, why3 = fetch_pdf(target)
            if data:
                got = (data, cand)
                break
            rec.setdefault('attempts', []).append({'url': target, 'reason': why3})

        if got:
            data, cand = got
            fn = slug(doi) + '.pdf'
            tmp = os.path.join(outdir, fn + '.tmp')
            with open(tmp, 'wb') as fh:
                fh.write(data)
            os.replace(tmp, os.path.join(outdir, fn))
            rec.update({'status': 'ok', 'url': cand['url'], 'source': cand['source'],
                        'bytes': len(data), 'file': fn})
            stats['ok'] += 1
        else:
            last = (rec.get('attempts') or [{}])[-1].get('reason', 'failed')
            rec.update({'status': 'failed', 'reason': last})
            if last.startswith('not_pdf'):
                stats['not_pdf'] += 1
            else:
                stats['failed'] += 1
            reasons[last] = reasons.get(last, 0) + 1
        cache[key] = rec
        if i % 20 == 0:
            print('  ...%d/%d ok=%d no_oa=%d fail=%d' % (
                i, len(todo), stats['ok'], stats['no_oa'], stats['failed']), flush=True)

    save_cache(cache_path, cache)
    print('\n=== OA 定位完成 ===')
    print('  Unpaywall 有 OA 记录: %d' % hits_uw)
    print('  OpenAlex 有 OA 记录  : %d' % hits_oa)
    print('  下载成功             : %d' % stats['ok'])
    print('  无开放获取版本       : %d' % stats['no_oa'])
    print('  拿到链接但非 PDF     : %d' % stats['not_pdf'])
    print('  下载失败             : %d' % stats['failed'])
    if reasons:
        print('  失败原因分布:')
        for k, v in sorted(reasons.items(), key=lambda x: -x[1])[:6]:
            print('    %-28s %d' % (k, v))
    print('  → 仍无全文: %d（需机构订阅或人工获取）' % (
        stats['no_oa'] + stats['not_pdf'] + stats['failed']))
    return 0


if __name__ == '__main__':
    sys.exit(main())
