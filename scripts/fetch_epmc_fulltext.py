#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Europe PMC 全文（JATS XML）抓取 -> 纯文本。

为什么需要这个通道（2026-11-02 线上实证，不是推测）：
  当日 149 篇新增中 37 篇在 Europe PMC 有 PMC 编号，但
    https://europepmc.org/articles/PMCxxx?pdf=render
    https://europepmc.org/backend/ptpmcrender.fcgi?accid=PMCxxx&blobtype=pdf
  两个 PDF 端点对脚本请求一律返回 403（机器人拦截），PDF 成功率 0/37。
  于是 phase5 深度提炼 0/149，整天的产出退化为只有摘要的概念页。
  同一天 REST 的 fullTextXML 端点仍是 200（实测 167 KB JATS），
  所以全文获取改走 XML，再转成带小节标题的纯文本。

输出：<outdir>/<doi_slug>.txt，小节以 "## 标题" 开头，段落按空行分隔；
      同时维护 <outdir>/_index.txt（每行 "doi<TAB>pmcid"），供增量查重。
deep_curate_all.extract_fulltext() 直接读 .txt，不需要重新造 PDF。

用法：
    python3 fetch_epmc_fulltext.py --from-file dois.txt
    python3 fetch_epmc_fulltext.py --all-missing
    python3 fetch_epmc_fulltext.py --all-missing --max 50 --dry-run

2026-11-03: 页面 frontmatter 已回填 pmcid，--all-missing 直接按 pmcid
取 fullTextXML，省掉 DOI->PMCID 的 search 往返（search 是 429 的主要来源）。
    python3 fetch_epmc_fulltext.py --from-file dois.txt --dry-run
"""
import argparse
import json
import os
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

from kb_paths import BASE

SEARCH = ('https://www.ebi.ac.uk/europepmc/webservices/rest/search'
          '?query=DOI:%s&format=json&pageSize=1')
FULLTEXT = 'https://www.ebi.ac.uk/europepmc/webservices/rest/%s/fullTextXML'
UA = 'hermes-kb-fulltext/1.0 (mailto:dev@example.com)'

MIN_CHARS = 1200      # 低于此长度视为不足以支撑深度提炼
MIN_SECTIONS = 2
MIN_PARA_CHARS = 40    # 单段最短字符数；JATS 常把正文切成短段，60 会误杀


def _strip_doctype(raw):
    """去掉 DOCTYPE（其中有外部 DTD 声明），否则 ET 可能因实体解析报错。"""
    return re.sub(rb'<!DOCTYPE[^>]*>', b'', raw, count=1)


# 这些元素里的文本不是正文：xref 是文献引用编号（会变成 "33 20 , Notably"），
# label 是图表编号，fn 是脚注。
_DROP_TAGS = frozenset((
    'xref', 'label', 'fn', 'table-wrap', 'supplementary-material',
    # 行内图形：Elsevier/JATS 会把矢量图标成 <svg>（内含 potrace 路径数据），
    # 不剔除就会把 "M0 440 l0 -40 480 0..." 整段路径写进正文。2026-11-02 实证。
    'svg', 'graphic', 'inline-graphic', 'media', 'inline-formula',
))

# 兜底：XML 标签一旦漏网（未预料到的行内元素），在成文后再剥一层。
_RESIDUAL_TAG = re.compile(r'</?[A-Za-z][A-Za-z0-9:._-]*(?:\s[^<>]{0,2000})?/?>')


def _text_of(elem):
    """取元素下的正文文本；跳过引用编号等非正文节点，合并空白。"""
    parts = []

    def walk(node):
        tag = node.tag.rsplit('}', 1)[-1] if isinstance(node.tag, str) else ''
        if tag in _DROP_TAGS:
            # 关键：被丢弃节点的 tail 属于父级行文（例如 <label>Figure 1</label>Plants grew
            # faster... 里的后半句），丢掉 tail 会让整段正文消失。2026-11-02 单测暴露。
            if node.tail:
                parts.append(node.tail)
            return
        if node.text:
            parts.append(node.text)
        for child in node:
            walk(child)
        if node.tail:
            parts.append(node.tail)

    walk(elem)
    s = ' '.join(parts)
    s = s.replace(chr(160), ' ')
    s = re.sub(r'\s+', ' ', s)      # JATS 源码里的换行不能带进正文
    s = re.sub(r'\s+([,.;:])', r'\1', s)
    return s.strip()


def _local(tag):
    return tag.rsplit('}', 1)[-1]


def jats_to_text(raw):
    """JATS XML -> (title, text)。只保留摘要与正文小节，丢弃参考文献与图表题注。"""
    try:
        root = ET.fromstring(_strip_doctype(raw))
    except ET.ParseError as exc:
        raise ValueError('xml-parse: %s' % exc)

    title = ''
    for node in root.iter():
        if _local(node.tag) == 'article-title':
            title = _text_of(node)
            break

    blocks = []
    for node in root.iter():
        if _local(node.tag) == 'abstract':
            body = re.sub(r'^ABSTRACT\s+', '', _text_of(node), flags=re.I)
            if len(body) > 60:
                blocks.append(('Abstract', body))
            break

    for body in root.iter():
        if _local(body.tag) != 'body':
            continue
        for sec in body:
            if _local(sec.tag) != 'sec':
                continue
            heading = ''
            paras = []
            subs = []            # 先收子节，父节正文放在它前面，读起来才顺
            for node in sec:
                tag = _local(node.tag)
                if tag == 'title':
                    heading = _text_of(node)
                elif tag == 'p':
                    t = _text_of(node)
                    if len(t) >= MIN_PARA_CHARS:
                        paras.append(t)
                elif tag == 'sec':
                    sub, sub_paras = '', []
                    for sub_node in node:
                        if _local(sub_node.tag) == 'title':
                            sub = _text_of(sub_node)
                        elif _local(sub_node.tag) == 'p':
                            t = _text_of(sub_node)
                            if len(t) >= MIN_PARA_CHARS:
                                sub_paras.append(t)
                    if sub_paras:
                        name = ('%s / %s' % (heading, sub)) if heading else sub
                        subs.append((name or 'Section', '\n\n'.join(sub_paras)))
            if paras:
                blocks.append((heading or 'Section', '\n\n'.join(paras)))
            blocks.extend(subs)
        break

    text = '\n\n'.join('## %s\n\n%s' % (name, body) for name, body in blocks)
    text = _RESIDUAL_TAG.sub(' ', text)
    text = re.sub(r'[ \t]{2,}', ' ', text)
    text = re.sub(r'\s+([,.;:])', r'\1', text)
    return title, text


def epmc_pmcid(doi, timeout=20):
    req = urllib.request.Request(SEARCH % urllib.parse.quote(doi),
                                 headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        payload = json.loads(resp.read().decode('utf-8', 'replace'))
    results = payload.get('resultList', {}).get('result') or []
    if not results:
        return None
    return results[0].get('pmcid') or None


def fetch_xml(pmcid, timeout=90):
    req = urllib.request.Request(FULLTEXT % pmcid,
                                 headers={'User-Agent': UA,
                                          'Accept': 'application/xml,text/xml,*/*'})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        if resp.status != 200:
            raise ValueError('http-%s' % resp.status)
        return resp.read()


def _retry(fn, *args, retries=3, backoff=2.0, once_codes=(), **kwargs):
    """对 403/429/5xx 与网络错误做指数退避重试；其余错误立即上抛。"""
    last = None
    for attempt in range(retries + 1):
        try:
            return fn(*args, **kwargs)
        except urllib.error.HTTPError as exc:
            code = getattr(exc, 'code', 0)
            limit = 1 if code in once_codes else retries
            if code not in (403, 429, 500, 502, 503, 504) or attempt >= limit:
                raise
            last = exc
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            if attempt >= retries:
                raise
            last = exc
        time.sleep(backoff * (2 ** attempt))
    if last is not None:
        raise last


def _log_failure(outdir, doi, stage, exc):
    """失败可诊断：把 DOI、阶段、错误写入 outdir/_epmc_xml_fail.log。"""
    try:
        os.makedirs(outdir, exist_ok=True)
        with open(os.path.join(outdir, '_epmc_xml_fail.log'), 'a',
                  encoding='utf-8') as fh:
            fh.write('%s\t%s\t%s\t%s\n' % (
                time.strftime('%Y-%m-%d %H:%M:%S'), doi, stage, str(exc)[:300]))
    except OSError:
        pass


FAIL_CACHE = '_epmc_failed.tsv'


def load_failed(outdir):
    '''已判定为永久失败的 DOI 集合（默认跳过，--retry-failed 可强制重试）。'''
    have = {}
    path = os.path.join(outdir, FAIL_CACHE)
    if os.path.isfile(path):
        with open(path, encoding='utf-8', errors='ignore') as fh:
            for line in fh:
                parts = line.rstrip('\n').split('\t')
                if len(parts) >= 2 and parts[0]:
                    have[parts[0].lower()] = parts[1]
    return have


def mark_failed(outdir, doi, reason):
    try:
        os.makedirs(outdir, exist_ok=True)
        with open(os.path.join(outdir, FAIL_CACHE), 'a', encoding='utf-8') as fh:
            fh.write('%s\t%s\t%s\n' % (doi, reason, time.strftime('%Y-%m-%d')))
    except OSError:
        pass

def doi_slug(doi):
    return doi.rstrip('./').replace('/', '_')


def _index_path(outdir):
    return os.path.join(outdir, '_index.txt')


def load_index(outdir):
    """已抓取的 DOI 集合（小写）。索引缺失时退回按文件名反推。"""
    have = set()
    path = _index_path(outdir)
    if os.path.isfile(path):
        with open(path, encoding='utf-8', errors='ignore') as fh:
            for line in fh:
                doi = line.split('\t')[0].strip()
                if doi:
                    have.add(doi.lower())
    if os.path.isdir(outdir):
        for name in os.listdir(outdir):
            if name.endswith('.txt') and not name.startswith('_'):
                have.add(name[:-4].replace('_', '/').lower())
    return have


def append_index(outdir, doi, pmcid):
    with open(_index_path(outdir), 'a', encoding='utf-8') as fh:
        fh.write('%s\t%s\n' % (doi, pmcid))


def _iter_paper_pages():
    for sub in ('concepts/papers', 'concepts'):
        d = os.path.join(BASE, sub)
        if not os.path.isdir(d):
            continue
        for name in os.listdir(d):
            if name.endswith('.md'):
                yield os.path.join(d, name)


def _doi_of(head):
    m = re.search(r'^doi:\s*"?\s*(10\.\d{4,}/[^\s"\n`]+)', head, re.M)
    return m.group(1).rstrip('./') if m else None


def _pmcid_of(head):
    m = re.search(r'^pmcid:\s*"?\s*(PMC\d+)', head, re.M | re.I)
    return m.group(1).upper() if m else None


def _pdf_dois():
    """all_pdfs 下已有的 PDF DOI（PMC 命名的文件反推不出 DOI，故只做补充）。"""
    have = set()
    d = os.path.join(BASE, 'raw', 'papers', 'all_pdfs')
    if not os.path.isdir(d):
        return have
    for name in os.listdir(d):
        if not name.endswith('.pdf'):
            continue
        m = re.search(r'(10\.\d{4,}[^\s/]+)', name)
        if m:
            have.add(m.group(1).replace('_', '/').rstrip('.').lower())
    return have


def collect_gaps(outdir):
    """库内概念页有 DOI、但 fulltext/ 与 all_pdfs/ 都没有对应全文的缺口。

    返回 [{'doi':..., 'pmcid':...|None}]。页面 frontmatter 有 pmcid 时可直接
    取 fullTextXML，避免一次 search 调用（search 端点限流更严）。
    """
    have = load_index(outdir) | _pdf_dois()
    seen = set()
    out = []
    for path in _iter_paper_pages():
        try:
            with open(path, encoding='utf-8', errors='ignore') as fh:
                head = fh.read(2000)
        except OSError:
            continue
        doi = _doi_of(head)
        if not doi:
            continue
        key = doi.lower()
        if key in have or key in seen:
            continue
        seen.add(key)
        out.append({'doi': doi, 'pmcid': _pmcid_of(head)})
    return sorted(out, key=lambda item: item['doi'])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--from-file', help='DOI 列表文件，每行一个')
    ap.add_argument('--all-missing', action='store_true',
                    help='扫描库内缺全文的概念页 DOI')
    ap.add_argument('--outdir', default='raw/papers/fulltext')
    ap.add_argument('--sleep', type=float, default=0.3)
    ap.add_argument('--retries', type=int, default=3,
                    help='403/429/5xx 与网络错误的重试次数')
    ap.add_argument('--retry-backoff', type=float, default=2.0,
                    help='首次重试等待秒数，之后指数翻倍')
    ap.add_argument('--max', type=int, default=0, help='最多尝试的条数')
    ap.add_argument('--pmcid-only', action='store_true',
                    help='只处理页面已有 pmcid 的条目，跳过 DOI->PMCID 检索')
    ap.add_argument('--order', choices=('doi', 'shuffle'), default='doi',
                    help='shuffle: 固定随机种子打散，避免失败条目按 DOI 聚簇')
    ap.add_argument('--seed', type=int, default=20261103)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--workers', type=int, default=1,
                    help='并发抓取线程数；Europe PMC 对 2-4 并发尚可')
    ap.add_argument('--retry-failed', action='store_true',
                    help='忽略失败缓存，重试已判定为永久失败的条目')
    args = ap.parse_args()

    outdir = os.path.join(BASE, args.outdir)
    failed_cached = {} if args.retry_failed else load_failed(outdir)

    if args.all_missing:
        items = collect_gaps(outdir)
    elif args.from_file:
        with open(args.from_file, encoding='utf-8') as fh:
            items = [{'doi': ln.strip(), 'pmcid': None}
                     for ln in fh if ln.strip().startswith('10.')]
    else:
        print('需 --from-file 或 --all-missing', file=sys.stderr)
        return 2

    if args.pmcid_only:
        items = [it for it in items if it.get('pmcid')]
    if args.order == 'shuffle':
        import random
        random.Random(args.seed).shuffle(items)
    if not items:
        print('没有待补条目：请确认 KB_BASE 指向知识库根（当前 BASE=%s）'
              % BASE, file=sys.stderr)
        return 1

    if not args.dry_run:
        os.makedirs(outdir, exist_ok=True)

    stats = {'input': len(items), 'skip_failed': 0, 'pmcid_direct': 0, 'ok': 0,
             'skip_exists': 0, 'no_pmc': 0, 'no_xml': 0, 'thin': 0,
             'error': 0}
    reasons = {}
    _lock = threading.Lock()

    def _record(key, reason=None):
        with _lock:
            stats[key] += 1
            if reason:
                reasons[reason] = reasons.get(reason, 0) + 1

    def run_one(item):
        """单条抓取。副作用只写本 DOI 自己的文件，线程间不共享状态。"""
        doi = item['doi']
        target = os.path.join(outdir, doi_slug(doi) + '.txt')
        if os.path.exists(target) and os.path.getsize(target) > MIN_CHARS:
            return 'skip_exists', False, None
        pmcid = item.get('pmcid')
        direct = bool(pmcid)
        if not pmcid:
            try:
                pmcid = _retry(epmc_pmcid, doi, retries=args.retries,
                               backoff=args.retry_backoff)
            except Exception as exc:
                _log_failure(outdir, doi, 'search', exc)
                time.sleep(args.sleep)
                return 'error', direct, 'search:' + type(exc).__name__
        if not pmcid:
            mark_failed(outdir, doi, 'no_pmc')
            time.sleep(args.sleep)
            return 'no_pmc', direct, 'no_pmc'
        try:
            raw = _retry(fetch_xml, pmcid, retries=args.retries,
                         backoff=args.retry_backoff, once_codes=(500,))
        except Exception as exc:
            key = 'xml:' + str(getattr(exc, 'code', type(exc).__name__))
            _log_failure(outdir, doi, 'xml', exc)
            mark_failed(outdir, doi, key)
            time.sleep(args.sleep)
            return 'no_xml', direct, key
        try:
            title, text = jats_to_text(raw)
        except ValueError as exc:
            _log_failure(outdir, doi, 'parse', exc)
            time.sleep(args.sleep)
            return 'no_xml', direct, str(exc)[:26]
        sections = text.count('\n## ') + (1 if text.startswith('## ') else 0)
        if len(text) < MIN_CHARS or sections < MIN_SECTIONS:
            mark_failed(outdir, doi, 'thin')
            time.sleep(args.sleep)
            return 'thin', direct, 'thin:%d chars' % (len(text) // 1000)
        header = '# %s\n\n<!-- source: Europe PMC %s | %s -->\n\n' % (
            title or doi, pmcid, doi)
        if not args.dry_run:
            tmp = target + '.tmp'
            with open(tmp, 'w', encoding='utf-8') as fh:
                fh.write(header + text + '\n')
            os.replace(tmp, target)
            append_index(outdir, doi, pmcid)
        time.sleep(args.sleep)
        return 'ok', direct, None

    todo = []
    for item in items:
        if item['doi'].lower() in failed_cached and not args.retry_failed:
            stats['skip_failed'] += 1
            continue
        if args.max and len(todo) >= args.max:
            break
        todo.append(item)

    done = [0]

    def task(item):
        try:
            status, direct, reason = run_one(item)
        except Exception:
            status, direct, reason = 'error', False, 'unhandled'
        if direct:
            _record('pmcid_direct')
        _record(status, reason)
        with _lock:
            done[0] += 1
            n = done[0]
        if n % 10 == 0:
            print('  ...%d ok=%d thin=%d no_pmc=%d'
                  % (n, stats['ok'], stats['thin'], stats['no_pmc']),
                  file=sys.stderr, flush=True)
        return status

    workers = max(1, args.workers)
    if workers > 1:
        print('  并发线程: %d' % workers, file=sys.stderr, flush=True)
        with ThreadPoolExecutor(max_workers=workers) as ex:
            list(ex.map(task, todo))
    else:
        for item in todo:
            task(item)

    print('\n=== Europe PMC 全文(XML) 抓取 ===')
    for key in ('input', 'skip_failed', 'pmcid_direct', 'ok', 'skip_exists', 'no_pmc',
                'no_xml', 'thin', 'error'):
        print('  %-12s %d' % (key, stats[key]))
    if reasons:
        print('  失败原因分布:')
        for key, cnt in sorted(reasons.items(), key=lambda kv: -kv[1]):
            print('    %-28s %d' % (key, cnt))
    print('  输出目录: %s' % outdir)
    return 0


if __name__ == '__main__':
    sys.exit(main())
