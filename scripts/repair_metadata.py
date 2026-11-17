#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""repair_metadata.py — 按 PMID 回抓 PubMed 元数据，修复历史页面里被截断的标题与摘要。

背景（2026-11-01 线上实测）：旧版 daily_update.py 用 el.text 取
ArticleTitle / AbstractText，遇到 <i>/<sup>/<sub> 就停，于是
标题断在 "...Biosynthesis of Cellulase by "，摘要断在 "Maize ("；
frontmatter 的 title 另有 [:80] 硬截断。已落盘的内容不会因修代码而自愈。

本脚本只做一件事：重新取 PubMed 记录，若新值严格更好则替换
frontmatter 的 title、正文 H1、以及 "## 摘要" 段 / raw 文章正文。
不做提炼、不改证据、不动综合页。

用法:
    python3 scripts/repair_metadata.py                 # 预演（默认）
    python3 scripts/repair_metadata.py --apply         # 写入（先打包备份）
    python3 scripts/repair_metadata.py --limit 50 --apply
    python3 scripts/repair_metadata.py --report /tmp/x.json

退出码: 0 正常（含无需修改）/ 1 有 PMID 抓取失败 / 2 参数或环境错误
"""
import argparse
import glob
import io
import html
import json
import os
import re
import subprocess
import sys
import tarfile
import time
import xml.etree.ElementTree as ET
from datetime import datetime
from urllib.parse import quote

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from kb_paths import BASE  # noqa: E402
from text_utils import xml_text, has_dangling_tail, yaml_str  # noqa: E402

EUTILS = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'
ESEARCH = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'
EUROPEPMC = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search'
BATCH = 100
SLEEP = 0.4
SHORT_ABSTRACT = 700
_TITLE_CAP_HINT = 78

FM_TITLE = re.compile(r'^title:[ \t]*(.*)$', re.M)
FM_PMID = re.compile(r'^pmid:[ \t]*["\']?(\d+)', re.M)
FM_DOI = re.compile(r'^doi:[ \t]*["\']?([^\s"\'\n]+)', re.M)
H1 = re.compile(r'^#[ \t]+(.*)$', re.M)
ABSTRACT_SECTION = re.compile(r'(^##[ \t]*摘要[ \t]*\n)(.*?)(?=\n##[ \t]|\Z)', re.M | re.S)
_WS = re.compile(r'\s+')
SENT_END = '.!?\u3002\uff01\uff1f"\u201d\u2019\uff09)\u300d'
NEED_QUOTE_HEAD = set('[]{}*&!|>%@#`~')


# ─────────────────────────── 抓取 ───────────────────────────
def parse_efetch(xml_bytes):
    """返回 {pmid: {'title':…, 'abstract':…}}。空摘要记为空串。"""
    out = {}
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError:
        return out
    for art in root.findall('.//PubmedArticle'):
        pmid = xml_text(art.find('.//PMID'))
        if not pmid:
            continue
        titles = art.findall('.//ArticleTitle')
        title = xml_text(titles[0]) if titles else ''
        parts = []
        for node in art.findall('.//AbstractText'):
            txt = xml_text(node)
            if txt:
                label = (node.get('Label') or '').strip()
                parts.append('%s: %s' % (label, txt) if label else txt)
        doi = ''
        for node in art.findall('.//ArticleIdList/ArticleId'):
            if (node.get('IdType') or '').lower() == 'doi':
                doi = xml_text(node).strip().lower()
                break
        out[pmid] = {'title': title, 'abstract': '\n\n'.join(parts), 'doi': doi}
    return out


def fetch(pmids, tries=2):
    got, failed = {}, []
    for i in range(0, len(pmids), BATCH):
        chunk = pmids[i:i + BATCH]
        url = '%s?db=pubmed&retmode=xml&id=%s' % (EUTILS, ','.join(chunk))
        parsed = {}
        for attempt in range(tries):
            try:
                proc = subprocess.run(['curl', '-sS', '--max-time', '90', url],
                                      capture_output=True)
                if proc.returncode == 0 and proc.stdout:
                    parsed = parse_efetch(proc.stdout)
            except Exception:
                parsed = {}
            if parsed:
                break
            time.sleep(1.5 * (attempt + 1))
        got.update(parsed)
        failed.extend([p for p in chunk if p not in parsed])
        time.sleep(SLEEP)
    return got, failed


def _curl_json(url, tries=2):
    for attempt in range(tries):
        try:
            proc = subprocess.run(['curl', '-sS', '--max-time', '60', url],
                                  capture_output=True)
            if proc.returncode == 0 and proc.stdout:
                return json.loads(proc.stdout.decode('utf-8', 'ignore'))
        except Exception:
            pass
        time.sleep(1.5 * (attempt + 1))
    return {}


_TAG = re.compile(r'<[^>]+>')


def _plain(s):
    """Europe PMC 的 abstractText 含 <h4>/<i>/&lt; 等标记，先转纯文本。"""
    if not s:
        return ''
    s = re.sub(r'(?i)</h4>\s*<h4>', ' ', s)
    s = _TAG.sub(' ', s)
    s = html.unescape(s)
    return _WS.sub(' ', s).strip()


def parse_epmc(data):
    """解析 Europe PMC search 的 JSON，返回 {doi_lower: {title, abstract, doi}}。"""
    out = {}
    rows = ((data or {}).get('resultList') or {}).get('result') or []
    for row in rows:
        doi = (row.get('doi') or '').strip().lower()
        if not doi:
            continue
        title = _plain(row.get('title'))
        abs_ = _plain(row.get('abstractText'))
        if not title and not abs_:
            continue
        out[doi] = {'title': title, 'abstract': abs_, 'doi': doi}
    return out


def fetch_epmc(dois, per_query=25, tries=2):
    """Europe PMC 按 DOI 取标题/摘要，覆盖 PubMed 未收录的期刊与预印本。"""
    dois = list(dois)
    found, miss = {}, []
    for i in range(0, len(dois), per_query):
        chunk = dois[i:i + per_query]
        q = ' OR '.join('DOI:"%s"' % d for d in chunk)
        url = '%s?query=%s&format=json&resultType=core&pageSize=100' % (
            EUROPEPMC, quote(q, safe=''))
        local = parse_epmc(_curl_json(url, tries))
        time.sleep(SLEEP)
        for d in chunk:
            hit = local.get(d.lower())
            if hit:
                found[d.lower()] = hit
            else:
                miss.append(d)
    return found, miss


def resolve_dois(dois, per_query=20, tries=2):
    """DOI -> PMID（经 esearch + efetch 回读 ArticleIdList，避免错配）。

    返回 ({doi_lower: pmid}, [未命中 doi])。只用 PubMed 的精确 [AID] 检索，
    再用 efetch 返回的 DOI 反查，双重确认后才认定命中。
    """
    dois = list(dois)
    found, unresolved = {}, []
    for i in range(0, len(dois), per_query):
        chunk = dois[i:i + per_query]
        term = ' OR '.join('"%s"[AID]' % d for d in chunk)
        url = '%s?db=pubmed&retmode=json&retmax=%d&term=%s' % (
            ESEARCH, max(20, len(chunk) * 3), quote(term, safe=''))
        data = _curl_json(url, tries)
        ids = ((data.get('esearchresult') or {}).get('idlist') or [])
        time.sleep(SLEEP)
        if not ids:
            unresolved.extend(chunk)
            continue
        meta, _failed = fetch([str(x) for x in ids])
        local = {}
        for pmid, rec in meta.items():
            if rec.get('doi'):
                local[rec['doi']] = pmid
        for d in chunk:
            hit = local.get(d.lower())
            if hit:
                found[d.lower()] = hit
            else:
                unresolved.append(d)
    return found, unresolved


# ─────────────────────────── 页面读写 ───────────────────────────
def split_frontmatter(text):
    if not text.startswith('---'):
        return None, text
    end = text.find('\n---', 3)
    if end < 0:
        return None, text
    return text[3:end], text[end + 4:]


def get_pmid(fm, name):
    m = FM_PMID.search(fm or '')
    if m:
        return m.group(1)
    m = re.match(r'^daily-(\d+)\.md$', name)
    return m.group(1) if m else None


def page_doi(fm):
    m = FM_DOI.search(fm or '')
    return m.group(1).strip().lower().rstrip('.') if m else ''


def read_title(fm):
    """返回 (标题值, 是否带引号)。无 title 行时返回 ('', False)。"""
    m = FM_TITLE.search(fm or '')
    if not m:
        return '', False
    raw = m.group(1).rstrip()
    if len(raw) >= 2 and raw[0] == '"' and raw[-1] == '"':
        try:
            return json.loads(raw), True
        except Exception:
            return raw[1:-1].replace('\\"', '"'), True
    return raw.strip(), False


def render_title(value, quoted):
    value = _WS.sub(' ', value).strip()
    if quoted:
        return yaml_str(value)
    if value[:1] in NEED_QUOTE_HEAD or ': ' in value or ' #' in value:
        return yaml_str(value)
    return value


def set_title(text, new_title, only_h1=False):
    """替换 frontmatter title 与首个 H1。only_h1=True 时只改 H1（raw 文章无 title 字段）。"""
    fm, body = split_frontmatter(text)
    if fm is None:
        return text, False
    orig_fm, orig_body = fm, body
    value = _WS.sub(' ', new_title).strip()
    old_val, quoted = read_title(fm)
    if not only_h1 and _WS.sub(' ', old_val).strip() != value:
        rendered = render_title(new_title, quoted)
        m = FM_TITLE.search(fm)
        if m:
            fm = fm[:m.start(0)] + 'title: ' + rendered + fm[m.end(0):]
        else:
            fm = fm.rstrip('\n') + '\ntitle: ' + rendered
    m2 = H1.search(body)
    if m2 and m2.group(1).strip() != value:
        body = body[:m2.start(1)] + value + body[m2.end(1):]
    if fm == orig_fm and body == orig_body:
        return text, False
    return '---' + fm + '\n---' + body, True


def set_abstract(text, new_abs):
    m = ABSTRACT_SECTION.search(text)
    if not m:
        return text, False
    old = m.group(2).strip()
    if _norm(old) == _norm(new_abs):
        return text, False
    return text[:m.start(2)] + new_abs.strip() + '\n' + text[m.end(2):], True


def set_raw_body(text, new_abs):
    """raw/articles/daily-*.md: frontmatter 之后是 H1 + 摘要正文。"""
    fm, body = split_frontmatter(text)
    if fm is None:
        return text, False
    m = H1.search(body)
    if not m:
        return text, False
    head = body[:m.end(0)]
    old = body[m.end(0):].strip()
    if _norm(old) == _norm(new_abs):
        return text, False
    return '---' + fm + '\n---' + head + '\n\n' + new_abs.strip() + '\n', True


# ─────────────────────────── 判定 ───────────────────────────
def _norm(s):
    return _WS.sub(' ', (s or '')).strip()


def is_prefix(old, new):
    o, n = _norm(old), _norm(new)
    return bool(o) and n.startswith(o)


_LABEL_RE = re.compile(r'^(?:[A-Za-z][A-Za-z0-9 \-/&]{1,40}:)\s*')
# PubMed 常见分段标签，可能出现在行首，也可能被上游拼到句中。
_INLINE_LABEL = re.compile(
    r'\b(?:background|objectives?|aims?|purpose|introduction|methods?(?:\s+and\s+results)?'
    r'|results?|conclusions?|significance|discussion|summary)\b\s*:\s*', re.I)


def strip_labels(text):
    """去掉结构化摘要的 "BACKGROUND:" 之类标签，只留正文，便于比对。"""
    lines = [_LABEL_RE.sub('', ln.strip()) for ln in (text or '').split('\n')]
    return _norm(_INLINE_LABEL.sub(' ', ' '.join(lines)))


def is_prefix_abs(old, new):
    """正文级前缀判断：忽略分段标签与空白差异。"""
    o, n = strip_labels(old), strip_labels(new)
    return bool(o) and n.startswith(o)


def better_title(old, new):
    old, new = _norm(old), _norm(new)
    if not new or new == old:
        return False
    if has_dangling_tail(new):
        return False
    return len(new) > len(old)


def better_abstract(old, new):
    old, new = _norm(old), _norm(new)
    if not new or new == old:
        return False
    if is_prefix_abs(old, new) and len(new) > len(old):
        return True
    if len(new) >= SHORT_ABSTRACT and len(old) < SHORT_ABSTRACT:
        return True
    return len(new) > len(old) * 1.15


def title_needs_repair(title):
    if not title:
        return True
    if title != title.rstrip():
        return True
    if has_dangling_tail(title):
        return True
    if len(title) >= _TITLE_CAP_HINT and title[-1] not in SENT_END:
        return True
    return False


def abstract_needs_repair(abs_old):
    if not abs_old:
        return True
    if len(abs_old) < SHORT_ABSTRACT:
        return True
    return abs_old[-1] not in SENT_END


# ─────────────────────────── 备份 ───────────────────────────
def make_backup(paths):
    """写入前把候选文件打成 tar.gz，返回 (备份路径, 错误信息)。"""
    stamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    dest = os.path.expanduser('~/kb_metadata_repair_%s.tar.gz' % stamp)
    try:
        with tarfile.open(dest, 'w:gz') as tf:
            for p in paths:
                tf.add(p, arcname=os.path.relpath(p, BASE))
        return dest, None
    except Exception as exc:
        return None, str(exc)


# ─────────────────────────── 主流程 ───────────────────────────
def main():
    ap = argparse.ArgumentParser(description='按 PMID 回抓并修复截断的标题/摘要')
    ap.add_argument('--apply', action='store_true', help='写入（默认只预演）')
    ap.add_argument('--limit', type=int, default=0, help='最多处理多少个文件')
    ap.add_argument('--report', help='把结果写成 JSON')
    ap.add_argument('--skip-raw', action='store_true', help='不处理 raw/articles/')
    ap.add_argument('--resolve-doi', action='store_true',
                    help='对无 PMID 但有 DOI 的页面，先按 DOI 解析 PMID 再回抓')
    ap.add_argument('--europepmc', action='store_true',
                    help='PubMed 无命中时，再用 Europe PMC 按 DOI 取摘要（需配合 --resolve-doi）')
    args = ap.parse_args()

    patterns = [os.path.join(BASE, 'concepts', '*.md'),
                os.path.join(BASE, 'concepts', 'papers', '*.md')]
    if not args.skip_raw:
        patterns.append(os.path.join(BASE, 'raw', 'articles', 'daily-*.md'))
    targets = []
    for pattern in patterns:
        targets.extend(sorted(glob.glob(pattern)))
    if args.limit:
        targets = targets[:args.limit]

    pages, pmids = [], []
    for path in targets:
        try:
            text = io.open(path, encoding='utf-8', errors='ignore').read()
        except OSError:
            continue
        fm, body = split_frontmatter(text)
        pmid = get_pmid(fm, os.path.basename(path))
        doi = page_doi(fm)
        if not pmid and not (args.resolve_doi and doi):
            continue
        is_raw = (os.sep + 'raw' + os.sep) in path
        title, _q = read_title(fm)
        abs_old = ''
        am = ABSTRACT_SECTION.search(text)
        if am:
            abs_old = am.group(2).strip()
        elif is_raw:
            h = H1.search(body)
            abs_old = body[h.end(0):].strip() if h else ''
        if title_needs_repair(title) or abstract_needs_repair(abs_old):
            pages.append({'path': path, 'pmid': pmid, 'doi': doi, 'is_raw': is_raw,
                          'title': title, 'abstract': abs_old})
            pmids.append(pmid)

    doi_pages = [p for p in pages if not p['pmid']]
    if doi_pages:
        dois = sorted({p['doi'] for p in doi_pages})
        print('无 PMID 待修 %d 页，尝试按 DOI 解析（%d 个唯一 DOI）'
              % (len(doi_pages), len(dois)))
        mapping, unresolved = resolve_dois(dois)
        print('DOI 命中 %d，未命中 %d' % (len(mapping), len(unresolved)))
        for p in doi_pages:
            hit = mapping.get(p['doi'])
            if hit:
                p['pmid'] = hit
                p['via_doi'] = True
        rest = sorted({p['doi'] for p in doi_pages if not p['pmid']})
        if rest and args.europepmc:
            print('PubMed 未收录 %d 个 DOI，转 Europe PMC' % len(rest))
            epmc, miss = fetch_epmc(rest)
            print('Europe PMC 命中 %d，仍未命中 %d' % (len(epmc), len(miss)))
            for p in doi_pages:
                if p['pmid']:
                    continue
                rec = epmc.get(p['doi'])
                if rec:
                    p['pmid'] = 'epmc:' + p['doi']
                    p['via_epmc'] = True
    pages = [p for p in pages if p['pmid']]
    pmids = [p['pmid'] for p in pages]
    uniq = sorted({x for x in pmids if not x.startswith('epmc:')})
    print('待检查文件 %d，涉及 PMID %d' % (len(pages), len(uniq)))
    meta, failed = {}, []
    if uniq:
        meta, failed = fetch(uniq)
    for p in pages:
        if p.get('via_epmc'):
            meta[p['pmid']] = epmc.get(p['doi']) or {}
    if not pages:
        return 0
    print('抓取成功 %d，失败 %d' % (len(meta), len(failed)))

    backup = None
    if args.apply:
        backup, err = make_backup([p['path'] for p in pages])
        if not backup:
            print('备份失败，已中止写入: %s' % err, file=sys.stderr)
            return 2
        print('已备份 %d 个文件 -> %s' % (len(pages), backup))

    changed, skipped = [], []
    for p in pages:
        rec = meta.get(p['pmid'])
        if not rec:
            skipped.append({'path': p['path'], 'why': 'fetch-failed'})
            continue
        text = io.open(p['path'], encoding='utf-8', errors='ignore').read()
        did_title = did_abs = False
        new_title = _norm(rec['title'])
        if better_title(p['title'], new_title):
            text, did_title = set_title(text, new_title, only_h1=p['is_raw'])
        new_abs = rec['abstract']
        if new_abs and better_abstract(p['abstract'], new_abs):
            if p['is_raw']:
                # 仅当旧正文确为截断片段时才整段替换，避免覆盖全文
                if is_prefix_abs(p['abstract'], new_abs) or (
                        len(_norm(p['abstract'])) < SHORT_ABSTRACT
                        and len(_norm(new_abs)) >= SHORT_ABSTRACT):
                    text, did_abs = set_raw_body(text, new_abs)
            else:
                text, did_abs = set_abstract(text, new_abs)
        if did_title or did_abs:
            changed.append({'path': p['path'], 'title': did_title, 'abstract': did_abs,
                            'via': ('epmc' if p.get('via_epmc') else
                                    ('doi' if p.get('via_doi') else 'pmid')),
                            'old_title': p['title'], 'new_title': new_title,
                            'old_abs_len': len(_norm(p['abstract'])),
                            'new_abs_len': len(_norm(new_abs))})
            if args.apply:
                io.open(p['path'], 'w', encoding='utf-8', newline='\n').write(text)
        else:
            skipped.append({'path': p['path'], 'why': 'no-better-value'})

    fix_t = sum(1 for c in changed if c['title'])
    fix_a = sum(1 for c in changed if c['abstract'])
    print('可修复 %d（标题 %d，摘要 %d），跳过 %d'
          % (len(changed), fix_t, fix_a, len(skipped)))
    for c in changed[:5]:
        print('  · %s' % os.path.relpath(c['path'], BASE))
        print('      - %s' % (c['old_title'][:70] or '(空)'))
        print('      + %s' % c['new_title'][:70])

    if args.apply and changed:
        stamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        marker = os.path.join(BASE, '.metadata_repair_%s' % stamp)
        io.open(marker, 'w', encoding='utf-8').write('\n'.join(c['path'] for c in changed))
        print('已写入 %d 个文件；清单: %s' % (len(changed), marker))
        print('回滚: tar xzf "%s" -C "%s"' % (backup, BASE))

    if args.report:
        io.open(args.report, 'w', encoding='utf-8').write(json.dumps(
            {'changed': changed, 'skipped': skipped, 'failed_pmids': failed},
            ensure_ascii=False, indent=2))
        print('报告: %s' % args.report)
    if not args.apply:
        print('\n（预演模式，未写入。加 --apply 执行）')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())