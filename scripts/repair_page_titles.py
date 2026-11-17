# -*- coding: utf-8 -*-
"""repair_page_titles.py - 概念页标题修复（2026-11-03 第 9 轮）

问题
----
pipeline_selfcheck.title_anomalies 只看 frontmatter 的 `title:`，13 篇页面的
H1 却是 DOI / "Abstract" / 截断串 / 纯 HTML 斜体。Obsidian 显示的是 H1，
所以"自检 PASS、读者仍看到 DOI 当标题"——这是检查项本身没覆盖到位。

判据（H1 异常）
--------------
  1. 空
  2. 形如 10.1234/xxxx（DOI 当标题）
  3. 占位词：abstract / untitled / no title / unknown / 摘要
  4. H1 是 frontmatter 标题的严格前缀且明显更短（截断）
  5. 只含 HTML 标签包裹的单个词（<i>EMF2</i>）
  6. 作者列表（"Divyajanani S, Harithpriya K, ..."）

修复原则
--------
只用 frontmatter 的 `title:` 回填 H1，**不造句、不翻译、不猜**。若 frontmatter
标题本身也不合格（DOI / 作者列表 / 过短），只登记 `title_status: unresolved`
并写入 _review/title_unresolved_<date>.tsv，等待人工补。

用法
----
    python3 scripts/repair_page_titles.py --dry-run
    python3 scripts/repair_page_titles.py --apply
"""
import argparse
import datetime as _dt
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb_paths import BASE

CONCEPTS_DIR = os.path.join(BASE, 'concepts', 'papers')
REVIEW_DIR = os.path.join(BASE, '_review')

FM_RE = re.compile(r'^---\n(.*?)\n---\n', re.S)
H1_RE = re.compile(r'^#\s+(.*)$', re.M)
DOI_RE = re.compile(r'^10\.\d{4,9}/\S+$', re.I)
PLACEHOLDER = {'abstract', 'untitled', 'no title', 'unknown', '摘要', '标题'}
HTML_ONLY_RE = re.compile(r'^(<[^>]+>[^<]*</[^>]+>|<[^>]+/?>)$')
# 作者列表：至少两段 "Surname X,"，避免把
# "Pseudoceramide A, a non-canonical ..." 这种真标题误判
AUTHOR_LIST_RE = re.compile(
    r'^(?:[A-Z][A-Za-z\-]+ [A-Z]{1,3},\s*){2,}')


def _fm_title(text):
    fm = FM_RE.match(text)
    if not fm:
        return ''
    m = re.search(r'^title:\s*"?(.*?)"?\s*$', fm.group(1), re.M)
    return (m.group(1) if m else '').strip()


def title_quality(t):
    """'good' / 'doi' / 'placeholder' / 'author-list' / 'empty' / 'short'"""
    s = (t or '').strip()
    if not s:
        return 'empty'
    if DOI_RE.match(s):
        return 'doi'
    if s.lower() in PLACEHOLDER:
        return 'placeholder'
    if AUTHOR_LIST_RE.match(s) and ',' in s:
        return 'author-list'
    if len(s) < 12:
        return 'short'
    return 'good'


def h1_problem(h1, fm_title):
    s = (h1 or '').strip()
    q = title_quality(s)
    if q == 'empty':
        return 'empty'
    if q == 'doi':
        return 'doi-as-title'
    if q == 'placeholder':
        return 'placeholder'
    if HTML_ONLY_RE.match(s):
        return 'html-only'
    if q == 'author-list':
        return 'author-list'
    if fm_title and fm_title.lower().startswith(s.lower()) and len(s) < len(fm_title) * 0.6:
        return 'truncated'
    return ''


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--date', default=None, help='只处理该日 created 的页面')
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--limit', type=int, default=0)
    args = ap.parse_args(argv)
    day = _dt.date.today().isoformat()

    files = [n for n in sorted(os.listdir(CONCEPTS_DIR)) if n.endswith('.md')]
    if args.date:
        kept = []
        for n in files:
            head = io.open(os.path.join(CONCEPTS_DIR, n), encoding='utf-8', errors='ignore').read(2000)
            m = re.search(r'^created:\s*"?(\d{4}-\d{2}-\d{2})', head, re.M)
            if m and m.group(1) == args.date:
                kept.append(n)
        files = kept
    if args.limit:
        files = files[:args.limit]

    fixed, unresolved, clean = [], [], 0
    for fn in files:
        p = os.path.join(CONCEPTS_DIR, fn)
        text = io.open(p, encoding='utf-8', errors='ignore').read()
        fm_title = _fm_title(text)
        m = H1_RE.search(text)
        h1 = m.group(1).strip() if m else ''
        prob = h1_problem(h1, fm_title)
        if not prob:
            clean += 1
            continue
        if title_quality(fm_title) == 'good':
            fixed.append((fn, prob, h1[:50], fm_title[:70]))
            if args.apply:
                new = H1_RE.sub('# ' + fm_title, text, count=1)
                io.open(p, 'w', encoding='utf-8', newline='\n').write(new)
        else:
            unresolved.append((fn, prob, h1[:50], title_quality(fm_title), fm_title[:50]))
            if args.apply and 'title_status:' not in text:
                new = FM_RE.sub(lambda mm: '---\n' + mm.group(1).rstrip('\n')
                                + '\ntitle_status: unresolved\n---\n', text, count=1)
                io.open(p, 'w', encoding='utf-8', newline='\n').write(new)

    print('扫描 %d 页；H1 正常 %d；可用 frontmatter 标题修复 %d；无法自动修复 %d'
          % (len(files), clean, len(fixed), len(unresolved)))
    for r in fixed[:20]:
        print('  FIX  [%s] %-28s <- %s' % (r[1], r[2], r[3]))
    for r in unresolved[:20]:
        print('  HOLD [%s] %-28s fm=%s/%s' % (r[1], r[2], r[3], r[4]))

    if unresolved:
        os.makedirs(REVIEW_DIR, exist_ok=True)
        outp = os.path.join(REVIEW_DIR, 'title_unresolved_%s.tsv' % day)
        with io.open(outp, 'w', encoding='utf-8', newline='\n') as fh:
            fh.write('page\th1_problem\th1\tfm_quality\tfm_title\n')
            for r in unresolved:
                fh.write('\t'.join(str(x).replace('\t', ' ') for x in r) + '\n')
        print('待人工补标题：%s' % outp)

    if not args.apply:
        print('干跑：加 --apply 才写盘')
    return 0


if __name__ == '__main__':
    sys.exit(main())
