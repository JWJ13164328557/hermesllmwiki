# -*- coding: utf-8 -*-
"""PDF 全文回灌：把"磁盘上有全文、页面却没提炼"的文献补进知识库。

背景（2026-11-03 体检）
----------------------
* 磁盘 2469 份 PDF / raw 9.4G，但只有 1221 页标了 PDF 全文（17%）；
* 存在约 1000+ 份"已下载但从未被提炼"的本地全文 —— 这是最便宜的增量；
* 根因不是 PDF 缺失，而是提炼阶段的可达性：`deep_curate_all.py` 的
  DOIs 过滤按字符串精确匹配，Annual Reviews 这类"页面 DOI 带文章号、
  PDF 用短前缀"的文献全部漏掉。

做法
----
1. 复用 check_pdf_coverage.collect_pdf_records() 解析全部 PDF 的 DOI；
2. DOI 与概念页做「精确 + 前缀容错」匹配；
3. 判定页面是否已提炼（有 `**来源类型**` 且 `### 核心发现`）；
4. 输出清单 TSV；`--apply` 时写 DOI 清单并调用 deep_curate_all.py
   （同一套提炼代码，避免两套逻辑再次分叉）。

用法
----
    python3 scripts/backfill_pdf_curation.py --dry-run
    python3 scripts/backfill_pdf_curation.py --apply --out /tmp/backfill_dois.txt
"""
import argparse
import collections
import io
import json
import os
import re
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb_paths import BASE
from check_pdf_coverage import collect_pdf_records

CONCEPTS_DIR = os.path.join(BASE, 'concepts', 'papers')
TOP_DIR = os.path.join(BASE, 'concepts')
SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'deep_curate_all.py')


def build_index():
    """DOI -> 页面路径；同时建前缀索引用于容错。"""
    exact, prefix = {}, collections.defaultdict(list)
    dirs = [CONCEPTS_DIR, TOP_DIR]
    seen = set()
    for d in dirs:
        if not os.path.isdir(d):
            continue
        for fn in os.listdir(d):
            if not fn.endswith('.md'):
                continue
            p = os.path.join(d, fn)
            if p in seen:
                continue
            seen.add(p)
            try:
                head = io.open(p, encoding='utf-8', errors='ignore').read(3000)
            except OSError:
                continue
            m = re.search(r'doi:\s*"?\s*(10\.\d{4,}/[^\s\n"\]\]]+)', head, re.I)
            if not m:
                continue
            doi = m.group(1).rstrip('/.')
            exact.setdefault(doi.lower(), p)
            prefix[doi.lower()].append(p)
    return exact


def resolve(doi, exact):
    """精确 → 剥后缀（PDF 常用短前缀）→ 加后缀（PDF 比页面更长）三步。"""
    d = (doi or '').lower().rstrip('/.')
    if not d:
        return None
    if d in exact:
        return exact[d]
    parts = d.split('-')
    for i in range(1, min(3, len(parts))):
        cand = '-'.join(parts[:-i])
        if cand in exact:
            return exact[cand]
    for key in exact:
        if key.startswith(d + '-'):
            return exact[key]
    return None


def is_curated(path):
    try:
        t = io.open(path, encoding='utf-8', errors='ignore').read()
    except OSError:
        return False
    # 2026-11-03：非研究页（更正/撤稿/社论/会员表）按设计只写
    # `### 文献变更要点`，不写 `### 核心发现`。旧判定把它们永远当作
    # "未提炼"，于是每轮回灌都会重复处理同一批页面。两种块都算已提炼。
    if '**来源类型**' not in t:
        return False
    return ('### 核心发现' in t) or ('### 文献变更要点' in t)


DOI_IN_TEXT = re.compile(r'10\.\d{4,9}/[-._;()/:A-Za-z0-9]+')
_TAG_RE = re.compile(r'[^a-z0-9 ]+')


def _pdf_head_text(path, pages=2):
    try:
        import fitz
        doc = fitz.open(path)
        txt = ''.join(doc[i].get_text() for i in range(min(pages, len(doc))))
        doc.close()
        return txt
    except Exception:
        return ''


def _page_title(path):
    try:
        head = io.open(path, encoding='utf-8', errors='ignore').read(4000)
    except OSError:
        return ''
    m = re.search(r'^title:\s*"??([^"\n]+)', head, re.M)
    if m:
        return m.group(1)
    m = re.search(r'^#\s+(.+)$', head, re.M)
    return m.group(1) if m else ''


def _title_supported(concept_page, pdf_text_norm):
    """标题词命中法：PDF 首页文本里能找到概念页标题的一半以上实词。

    防的是"从正文参考文献里抓到别人的 DOI"这类假匹配 —— 那种情况下
    PDF 首页不会出现概念页的标题。
    """
    words = [w for w in _TAG_RE.sub(' ', _page_title(concept_page).lower()).split()
             if len(w) > 4][:6]
    if not words:
        return False
    hit = sum(1 for w in words if w in pdf_text_norm)
    return hit >= max(2, len(words) // 2)


def deep_resolve(unmatched, exact, stats, limit=0):
    """对文件名没解析出 DOI（或解析出但无页面）的 PDF，回退到正文首两页。

    背景（2026-11-03 体检）：全库 726 份 PDF 未匹配到概念页，其中 253 份
    其实**页面是存在的**，只是 PDF 以文章号/PII/中文标题命名，文件名里
    没有可解析的 DOI。这批全文此前从未进入提炼，是纯粹的沉没成本。
    """
    targets, still = [], []
    seen_pages = set()
    for rec in unmatched:
        txt = _pdf_head_text(rec['path'])
        stats['deep_text_read'] += 1
        if len(txt.strip()) < 100:
            stats['deep_no_text'] += 1
            still.append(rec)
            continue
        norm = _TAG_RE.sub(' ', txt.lower())
        hit = None
        for m in DOI_IN_TEXT.finditer(txt[:8000]):
            doi = m.group(0).rstrip('.,;:)]')
            if doi.lower().endswith('.pdf'):
                doi = doi[:-4]
            page = resolve(doi, exact)
            if not page:
                continue
            if is_curated(page):
                stats['deep_already_curated'] += 1
                break
            if _title_supported(page, norm):
                hit = (doi, page, rec['path'])
                break
        if hit and hit[1] in seen_pages:
            stats['deep_duplicate_page'] += 1
            continue
        if hit:
            seen_pages.add(hit[1])
            targets.append(hit)
            stats['deep_matched'] += 1
        else:
            still.append(rec)
        if limit and len(targets) >= limit:
            break
    return targets, still


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--out', default='')
    ap.add_argument('--limit', type=int, default=0)
    ap.add_argument('--deep', action='store_true',
                    help='对匹配失败的 PDF 回退到正文首两页找 DOI（标题词校验）')
    args = ap.parse_args()
    dry = not args.apply

    exact = build_index()
    records = collect_pdf_records()
    stats = collections.Counter()
    targets = []          # (doi, page, pdf)
    unresolved = []
    unmatched = []        # 未能匹配到页面的 PDF（供 --deep 复筛）

    for rec in records:
        stats['pdf_seen'] += 1
        doi = rec.get('doi')
        if doi:
            doi = re.sub(r'\.pdf$', '', str(doi), flags=re.I).rstrip('.-')
        if not doi:
            stats['pdf_no_doi'] += 1
            unmatched.append(rec)
            continue
        page = resolve(doi, exact)
        if not page:
            stats['page_missing'] += 1
            unresolved.append((doi, rec['path']))
            unmatched.append(rec)
            continue
        stats['matched'] += 1
        if is_curated(page):
            stats['already_curated'] += 1
            continue
        stats['needs_curation'] += 1
        targets.append((doi, page, rec['path']))

    if args.deep and unmatched:
        deep_targets, _still = deep_resolve(unmatched, exact, stats,
                                            limit=args.limit)
        targets.extend(deep_targets)

    # 同一页面多份 PDF 只保留一份
    uniq = {}
    for doi, page, pdf in targets:
        uniq.setdefault(page, (doi, page, pdf))
    targets = list(uniq.values())
    stats['unique_pages_to_curate'] = len(targets)

    out = args.out or os.path.join(tempfile.gettempdir(), 'backfill_dois.txt')
    map_out = ''
    if not dry and targets:
        # 2026-11-03：同时写 TSV(doi, page, pdf)。旧实现只传 DOI 清单，
        # 让 deep_curate_all.py 重新按文件名猜 PDF，63 个目标只猜中 7 个。
        # 这里把已经确定的映射直接交给下游，全程只有一次解析。
        map_out = out + '.tsv'
        with io.open(out, 'w', encoding='utf-8', newline='\n') as fh:
            for doi, _page, _pdf in targets:
                fh.write(doi + '\n')
        with io.open(map_out, 'w', encoding='utf-8', newline='\n') as fh:
            for doi, page, pdf in targets:
                fh.write('%s\t%s\t%s\n' % (doi, page, pdf))

    print(json.dumps({
        'dry_run': dry,
        'stats': dict(stats),
        'out_doi_list': None if dry else out,
        'out_pdf_map': None if dry else map_out,
        'unresolved_sample': unresolved[:10],
    }, ensure_ascii=False, indent=1))

    if not dry and targets:
        lim = ['--pdf-map', map_out]
        rc = subprocess.call([sys.executable, SCRIPT] + lim)
        print('deep_curate_all exit:', rc)


if __name__ == '__main__':
    main()
