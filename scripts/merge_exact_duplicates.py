#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""merge_exact_duplicates.py — 合并"同一篇文献的两个概念页"（默认 dry-run）。

判重规则（两条，都可解释）
--------------------------
1. **严格同 DOI**：frontmatter 的 doi 去空白/小写后完全相同。
2. **下划线变体**：A 的 doi 含下划线，把最后一段的下划线换成斜杠后与 B 相同。
   这是历史抓取器把 10.1093/bib/bbaa097 写成 10.1093/bib_bbaa097 的产物；
   下划线写法在库里查不到对应文献，等于给同一篇建了第二个页面。
   ⚠ 只在"斜杠写法确实存在于库内"时才合并——Springer 图书章节 DOI
   （10.1007/978-1-4020-6754-9_3761）本来就带下划线，不能被误改成斜杠。

做法
----
* keeper = 字节数更大的那个（内容更完整）；平局时取文件名排序靠前者，保证确定性。
* loser 移入 archive/duplicates/，**不删除**。
* keeper 的 frontmatter 追加 merged_from 与 alias，正文末尾追加一行来源说明。
* 有入链的 loser 不合并（避免断链），进报告。

用法：
    python3 merge_exact_duplicates.py              # 预览
    python3 merge_exact_duplicates.py --apply      # 执行
    python3 merge_exact_duplicates.py --report _review/dup_report.md
"""
import argparse
import collections
import os
import re
import shutil
import sys

from kb_paths import BASE

PAPERS = os.path.join(BASE, 'concepts', 'papers')
ARCHIVE = os.path.join(BASE, 'archive', 'duplicates')


def read_page(path):
    with open(path, encoding='utf-8', errors='replace') as f:
        return f.read()


def page_doi(text):
    m = re.search(r'^doi:[ \t]*["\u0027]?([^\s"\u0027\n]+)', text, re.M)
    return m.group(1).strip().lower().rstrip('.') if m else ''


def slash_variant(doi):
    """仅当下划线出现在最后一段、且下划线前是纯字母期刊缩写时，返回斜杠写法。

    历史抓取器把 10.1093/bib/bbaa097 写成了 10.1093/bib_bbaa097，这是唯一
    应当纠正的下划线情形。反例：Springer 图书章节
    10.1007/978-1-4020-6754-9_3761 的下划线是书目号的一部分（数字与连字符），
    10.4103/ijdr.ijdr_724 的下划线前带点号——它们都是真 DOI，绝不能换成斜杠。
    """
    if '_' not in doi:
        return None
    head, _, last = doi.rpartition('_')
    if '/' not in head:
        return None
    abbr = head.rsplit('/', 1)[1]
    if not abbr.isalpha():
        return None
    return head + '/' + last


def collect():
    pages = {}
    for name in sorted(os.listdir(PAPERS)):
        if not name.endswith('.md'):
            continue
        path = os.path.join(PAPERS, name)
        text = read_page(path)
        pages[name] = {'path': path, 'text': text, 'doi': page_doi(text),
                       'size': len(text.encode('utf-8'))}
    groups = []

    by_doi = collections.defaultdict(list)
    for name, info in pages.items():
        if info['doi']:
            by_doi[info['doi']].append(name)
    for doi, names in sorted(by_doi.items()):
        if len(names) > 1:
            groups.append(('exact', doi, names))

    for name, info in pages.items():
        v = slash_variant(info['doi'])
        if v and v in by_doi and name not in by_doi[v]:
            groups.append(('slash', v, [name] + by_doi[v]))
    return pages, groups


def inbound(targets):
    hits = collections.Counter()
    link_re = re.compile(r'\[\[([^\]\|#]+)')
    skip = {'.git', '.obsidian', 'archive', 'tmp', 'raw', 'mnt', 'scripts',
            'queries', 'logs', '.pipeline_state'}
    for root, dirs, files in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in skip]
        for fn in files:
            if not fn.endswith('.md'):
                continue
            try:
                with open(os.path.join(root, fn), encoding='utf-8',
                          errors='replace') as f:
                    text = f.read()
            except OSError:
                continue
            for m in link_re.finditer(text):
                k = m.group(1).strip()
                if k in targets:
                    hits[k] += 1
    return hits


def apply_group(kind, doi, names, pages):
    ranked = sorted(names, key=lambda n: (-pages[n]['size'], n))
    keeper, losers = ranked[0], ranked[1:]
    kh = pages[keeper]
    text = kh['text']
    if 'merged_from:' not in text:
        add = ''.join('- %s\n' % l[:-3] for l in losers)
        if re.search(r'^---\s*$', text, re.M):
            parts = text.split('---', 2)
            fm = parts[1]
            am = re.search(r'^aliases:[ \t]*$(.*?)(?=^[A-Za-z_][\w-]*:|\Z)', fm, re.M | re.S)
            if am:
                fm = fm[:am.end(1)] + add + fm[am.end(1):]
            else:
                fm = fm.rstrip('\n') + '\naliases:\n' + add
            fm = fm.rstrip('\n') + '\nmerged_from:\n' + add
            parts[1] = fm
            text = '---'.join(parts)
        else:
            text = 'merged_from:\n' + add + 'aliases:\n' + add + text
    note = ('\n\n> 合并说明：本页与 %s 指向同一 DOI（%s），已将重复页移入 '
            'archive/duplicates/。\n' % (', '.join(l[:-3] for l in losers), doi))
    if '合并说明' not in text:
        text = text.rstrip('\n') + note
    with open(kh['path'], 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)
    os.makedirs(ARCHIVE, exist_ok=True)
    for lose in losers:
        shutil.move(pages[lose]['path'], os.path.join(ARCHIVE, lose))
    return keeper, losers


def main():
    ap = argparse.ArgumentParser(description='merge duplicate concept pages')
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--report')
    args = ap.parse_args()

    pages, groups = collect()
    print('等价组: %d' % len(groups))
    if not groups:
        return 0
    loser_names = set()
    for kind, doi, names in groups:
        ranked = sorted(names, key=lambda n: (-pages[n]['size'], n))
        loser_names.update(ranked[1:])
    hits = inbound({n[:-3] if n.endswith('.md') else n for n in loser_names})
    if hits:
        print('  入链明细: ' + ', '.join('%s(%d)' % (k, v) for k, v in hits.items()))
    print('被入链的待淘汰页: %d（这些组跳过）' % len(hits))

    report = ['# 重复概念页合并报告', '',
              '规则：严格同 DOI；下划线写法的 DOI 且其斜杠写法在库内存在。', '']
    planned = skipped = 0
    for kind, doi, names in groups:
        ranked = sorted(names, key=lambda n: (-pages[n]['size'], n))
        losers = ranked[1:]
        blocked = [l for l in losers if l in hits]
        report.append('- %s  doi=%s' % (kind, doi))
        for n in ranked:
            report.append('  - %s  %d B%s' % (n, pages[n]['size'],
                                              '  (keeper)' if n == ranked[0] else ''))
        if blocked:
            skipped += 1
            report.append('  - **跳过**：%s 有入链 %s'
                          % (', '.join(blocked), [hits[b] for b in blocked]))
            continue
        planned += 1
        if args.apply:
            keeper, removed = apply_group(kind, doi, names, pages)
            report.append('  - 已合并 -> %s（移走 %s）'
                          % (keeper, ', '.join(removed)))

    print('可合并 %d 组 / 跳过 %d 组' % (planned, skipped))
    if args.report:
        os.makedirs(os.path.dirname(os.path.join(BASE, args.report)) or BASE,
                    exist_ok=True)
        with open(os.path.join(BASE, args.report), 'w', encoding='utf-8',
                  newline='\n') as f:
            f.write('\n'.join(report) + '\n')
        print('报告: %s' % args.report)
    if not args.apply:
        print('[dry-run] 未改动任何文件。加 --apply 执行。')
    return 0


if __name__ == '__main__':
    sys.exit(main())
