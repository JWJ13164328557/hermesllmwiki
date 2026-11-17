#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify_identifiers.py — DOI/PMID 与页面标题的语义一致性核验（默认只读）。

问题背景（2026-11-02 线上实测）：
  7701 页中检出 48 页 DOI 字段指向另一篇论文（PMID 正确），另有 3 页 xr-* 的
  DOI 与 PMID 成对错位到"同一期相邻论文"。这类错误用格式校验、DOI 唯一性
  校验都查不出来——只有把 DOI 解析成真实标题，再和页面标题比对才能发现。

判定链（三级证据，缺一不改）：
  1) OpenAlex 按 DOI / PMID 批量解析出 title/year/journal
  2) Europe PMC 按 PMID 再解析一次，得到独立的 title + DOI
  3) 页面标题与两处标题的相似度均 >= 阈值，且 OpenAlex 与 EPMC 给出的 DOI 一致

只有 1+2+3 全部满足才允许 --apply 改写；否则只进 review 清单，绝不臆造。

用法:
    python3 scripts/verify_identifiers.py --fetch          # 建/更新缓存（联网）
    python3 scripts/verify_identifiers.py                  # 只读核验 + 打印统计
    python3 scripts/verify_identifiers.py --report out.md  # 导出人工复核清单
    python3 scripts/verify_identifiers.py --apply          # 写入三级确证的修复

退出码: 0 无严重问题 / 1 存在待人工复核项 / 2 环境或缓存错误
"""
import argparse, collections, difflib, html, json, os, re, sys, time, unicodedata
import urllib.parse, urllib.request

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)
import kb_paths

try:
    import yaml
except ImportError:
    sys.exit('[verify_identifiers] 需要 PyYAML')

OPENALEX = 'https://api.openalex.org/works'
EPMC = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search'
UA = {'User-Agent': 'plantSciKB-verify (mailto:kb@example.org)'}
CJK = re.compile(r'[\u4e00-\u9fff]')
PLACEHOLDER_DOI = re.compile(r'^10\.\d{4,9}/\S*$')


# ---------- 文本规范化与相似度 ----------
def clean(text):
    s = unicodedata.normalize('NFKC', str(text or ''))
    s = s.replace('\u00ad', '')
    s = re.sub(r'</?[a-zA-Z][^>]*>', ' ', s)
    s = html.unescape(s)
    s = re.sub(r'[\u2010-\u2015\u2212]', '-', s)
    return re.sub(r'\s+', ' ', s).strip()


def norm(text):
    s = clean(text).lower()
    s = re.sub(r'[^a-z0-9\u4e00-\u9fff]+', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


def ascii_norm(text):
    s = clean(text).lower()
    s = re.sub(r'[^a-z0-9]+', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


def sim(a, b):
    """标题相似度。必须容忍：硬截断的标题、Unicode 连字符、软连字符、HTML 标签。"""
    na, nb = norm(a), norm(b)
    if not na or not nb:
        return 0.0
    if na == nb:
        return 1.0
    lo, hi = (na, nb) if len(na) <= len(nb) else (nb, na)
    if len(lo) >= 12 and hi.startswith(lo):          # 截断标题
        return 0.88 + 0.12 * len(lo) / len(hi)
    ta, tb = set(na.split()), set(nb.split())
    jac = len(ta & tb) / len(ta | tb)
    seq = difflib.SequenceMatcher(None, na, nb).ratio()
    # 第二道：去掉所有分隔符再比一次。用来吃掉
    #   - 排版式字母间隔（"A uxin R esponse F actor"）
    #   - HTML 实体/尖括号残留（"&amp;nbsp;"、"<em>"）
    #   - 硬截断落在单词中间（"...ubiquitin-dependent degrada"）
    ca, cb = re.sub(r'[^a-z0-9\u4e00-\u9fff]', '', na), re.sub(r'[^a-z0-9\u4e00-\u9fff]', '', nb)
    if ca and cb:
        lo2, hi2 = (ca, cb) if len(ca) <= len(cb) else (cb, ca)
        if len(lo2) >= 12 and hi2.startswith(lo2):
            seq = max(seq, 0.9)
        else:
            seq = max(seq, difflib.SequenceMatcher(None, ca, cb).ratio() * 0.95)
    return max(jac, seq * 0.97)


def is_placeholder_title(title):
    tc = clean(title)
    return len(tc) < 3 or bool(PLACEHOLDER_DOI.match(tc.lower()))


# ---------- 页面读取 ----------
def read_page(path):
    with open(path, encoding='utf-8', errors='ignore') as fh:
        raw = fh.read()
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', raw, re.S)
    if not m:
        return None, None, raw
    try:
        fm = yaml.safe_load(m.group(1))
    except Exception:
        return None, None, raw
    if not isinstance(fm, dict):
        return None, None, raw
    return fm, m.group(1), raw


def iterate_pages():
    for sub in ('papers', 'methods'):
        d = os.path.join(kb_paths.BASE, 'concepts', sub)
        if not os.path.isdir(d):
            continue
        for name in sorted(os.listdir(d)):
            if not name.endswith('.md'):
                continue
            path = os.path.join(d, name)
            fm, _, _ = read_page(path)
            if fm is None:
                continue
            yield '%s/%s' % (sub, name), path, fm


# ---------- 缓存与联网 ----------
def http_json(url, timeout=45):
    req = urllib.request.Request(url, headers=UA)
    return json.load(urllib.request.urlopen(req, timeout=timeout))


def load_cache(path):
    if not os.path.exists(path):
        return {'doi': {}, 'pmid': {}}
    with open(path, encoding='utf-8') as fh:
        data = json.load(fh)
    data.setdefault('doi', {})
    data.setdefault('pmid', {})
    return data


def save_cache(path, cache):
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as fh:
        json.dump(cache, fh, ensure_ascii=False)
    os.replace(tmp, path)


def fetch_missing(cache, dois, pmids, cache_path, batch=40):
    todo_d = [d for d in dict.fromkeys(dois) if d and d not in cache['doi']]
    todo_p = [p for p in dict.fromkeys(pmids) if p and p not in cache['pmid']]
    print('[fetch] doi %d / pmid %d 待解析' % (len(todo_d), len(todo_p)))
    select = 'select=doi,title,publication_year,ids,primary_location'
    for kind, todo in (('doi', todo_d), ('pmid', todo_p)):
        for i in range(0, len(todo), batch):
            chunk = todo[i:i + batch]
            url = '%s?per-page=50&%s&filter=%s' % (
                OPENALEX, select,
                urllib.parse.quote(kind + ':' + '|'.join(chunk), safe=':|./-_'))
            for attempt in range(4):
                try:
                    for w in http_json(url).get('results', []):
                        key = (w.get('doi') or '').split('doi.org/')[-1].lower()
                        rec = {
                            'title': w.get('title'),
                            'year': w.get('publication_year'),
                            'pmid': (w.get('ids', {}).get('pmid') or '').split('/')[-1] or None,
                            'journal': ((w.get('primary_location') or {}).get('source') or {}).get('display_name'),
                            'doi': key,
                        }
                        if key:
                            cache['doi'][key] = rec
                        if rec['pmid']:
                            cache['pmid'][rec['pmid']] = rec
                    break
                except Exception as exc:
                    print('  retry %s %d: %s' % (kind, i, str(exc)[:70]))
                    time.sleep(2 + 3 * attempt)
            save_cache(cache_path, cache)
            time.sleep(0.12)


def epmc_by_pmid(pmid):
    url = '%s?%s' % (EPMC, urllib.parse.urlencode({
        'query': 'EXT_ID:%s AND SRC:MED' % pmid,
        'format': 'json', 'resultType': 'core', 'pageSize': '3'}))
    try:
        res = http_json(url).get('resultList', {}).get('result', [])
    except Exception:
        return None
    if not res:
        return None
    r = res[0]
    info = r.get('journalInfo') or {}
    return {'title': r.get('title') or '', 'doi': (r.get('doi') or '').lower(),
            'journal': (info.get('journal') or {}).get('title') or '',
            'year': info.get('yearOfPublication')}


# ---------- 分类 ----------
def classify(fm, cache, threshold):
    title = str(fm.get('title') or '')
    ten = str(fm.get('title_en') or '')
    doi = str(fm.get('doi') or '').strip().lower()
    pmid = str(fm.get('pmid') or '').strip()
    rd = cache['doi'].get(doi) if doi else None
    rp = cache['pmid'].get(pmid) if pmid else None
    ref = ten or title

    if is_placeholder_title(title):
        if rd and len(ascii_norm(rd.get('title'))) >= 10:
            return 'empty_title_fixable', {'proposed_title': clean(rd['title'])}
        return 'empty_title_norecord', {}
    if CJK.search(title) and not ten:
        return 'cjk_unverifiable', {'candidate': clean(rd['title'])[:120] if rd else ''}
    sd = sim(ref, rd['title']) if rd else None
    sp = sim(ref, rp['title']) if rp else None
    if rd is None and rp is None:
        return 'no_record', {}
    if sd is not None and sd >= threshold:
        return 'ok', {}
    if sp is not None and sp >= threshold:
        return 'doi_wrong_pmid_ok', {'proposed_doi': rp.get('doi'), 'proposed_title': clean(rp['title'])[:120]}
    return 'mismatch', {'sd': None if sd is None else round(sd, 2),
                        'sp': None if sp is None else round(sp, 2),
                        'doi_rec_title': clean(rd['title'])[:110] if rd else '',
                        'pmid_rec_title': clean(rp['title'])[:110] if rp else ''}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cache', default=os.path.expanduser('~/.cache/plantscikb/oa_cache.json'))
    ap.add_argument('--fetch', action='store_true', help='联网补齐缓存（否则只用已有缓存）')
    ap.add_argument('--apply', action='store_true', help='写入三级确证的修复')
    ap.add_argument('--report', default='', help='导出 Markdown 人工复核清单')
    ap.add_argument('--threshold', type=float, default=0.75)
    ap.add_argument('--limit-epmc', type=int, default=60, help='单次最多向 EPMC 核实多少条待修项')
    args = ap.parse_args()

    os.makedirs(os.path.dirname(args.cache), exist_ok=True)
    cache = load_cache(args.cache)
    pages = list(iterate_pages())
    if not pages:
        print('[verify] 未找到概念页，检查 KB_BASE=%s' % kb_paths.BASE)
        return 2

    if args.fetch:
        fetch_missing(cache,
                      [str(fm.get('doi') or '').strip().lower() for _, _, fm in pages],
                      [str(fm.get('pmid') or '').strip() for _, _, fm in pages],
                      args.cache)

    buckets = collections.defaultdict(list)
    for rel, path, fm in pages:
        kind, extra = classify(fm, cache, args.threshold)
        buckets[kind].append((rel, path, fm, extra))

    total = len(pages)
    ok = len(buckets['ok'])
    print('页面 %d | 标题-标识符一致 %d (%.1f%%)' % (total, ok, 100.0 * ok / total))
    for kind in ('doi_wrong_pmid_ok', 'mismatch', 'empty_title_fixable', 'empty_title_norecord',
                 'no_record', 'cjk_unverifiable'):
        if buckets[kind]:
            print('  %-22s %5d' % (kind, len(buckets[kind])))

    fixed = 0
    if args.apply:
        pending = buckets['doi_wrong_pmid_ok'][:args.limit_epmc]
        for rel, path, fm, extra in pending:
            pmid = str(fm.get('pmid') or '').strip()
            confirm = epmc_by_pmid(pmid) if pmid else None
            if not confirm or not confirm.get('doi'):
                continue
            if confirm['doi'] != str(extra.get('proposed_doi') or '').lower():
                continue  # 两个数据源不一致 -> 交人工
            if sim(fm.get('title_en') or fm.get('title'), confirm['title']) < args.threshold:
                continue
            fm2 = dict(fm)
            fm2['doi_fixed_from'] = str(fm.get('doi') or '')
            fm2['doi'] = confirm['doi']
            fm2['metadata_source'] = 'europepmc+openalex'
            fm2['metadata_verified'] = time.strftime('%Y-%m-%d')
            if confirm.get('journal') and str(fm2.get('journal') or '').lower() in ('', 'unknown'):
                fm2['journal'] = confirm['journal']
            if confirm.get('year') and not fm2.get('year'):
                fm2['year'] = confirm['year']
            fm, raw_fm, raw = read_page(path)
            body = raw.split('---\n', 2)[-1].lstrip('\n')
            with open(path, 'w', encoding='utf-8') as fh:
                fh.write('---\n' + yaml.safe_dump(fm2, allow_unicode=True, sort_keys=False,
                                                  default_flow_style=False, width=1000) + '---\n\n' + body)
            fixed += 1
            time.sleep(0.2)
        print('[apply] 三级确证并写入 %d 页' % fixed)

    if args.report:
        with open(args.report, 'w', encoding='utf-8') as fh:
            fh.write('# 标识符待人工复核清单\n\n')
            fh.write('阈值 %.2f；生成于 %s\n\n' % (args.threshold, time.strftime('%Y-%m-%d %H:%M')))
            for kind in ('mismatch', 'doi_wrong_pmid_ok', 'empty_title_norecord', 'no_record'):
                rows = buckets[kind]
                if not rows:
                    continue
                fh.write('## %s (%d)\n\n' % (kind, len(rows)))
                for rel, _, fm, extra in rows:
                    fh.write('- `%s`\n  - 页面标题: %s\n  - 现 DOI: `%s` / PMID: `%s`\n'
                             % (rel, str(fm.get('title'))[:110], fm.get('doi') or '',
                                fm.get('pmid') or ''))
                    for key in ('doi_rec_title', 'pmid_rec_title', 'proposed_doi'):
                        if extra.get(key):
                            fh.write('  - %s: %s\n' % (key, extra[key]))
                fh.write('\n')
        print('[report] -> %s' % args.report)

    serious = len(buckets['mismatch']) + len(buckets['doi_wrong_pmid_ok'])
    return 1 if serious else 0


if __name__ == '__main__':
    sys.exit(main())