#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""purity_scan.py — 全库领域纯度扫描与离线隔离（历史坏数据回抓）

2026-11-02：纯度闸门此前只存在于下载层，历史页面从未按"研究对象"复核过。
本脚本对 concepts/papers/*.md 全量跑 purity_gate，并**只移动不删除**地隔离
高置信非植物页面。

关键约束：**引用感知**
  直接搬走被 evidence 引用的页面会制造新的孤儿证据。所以只隔离"没有任何
  evidence 引用"的页面；被引用的列为人工分诊候选（附引用计数），不动。

用法
----
    python3 purity_scan.py                        # 只扫描出报告（默认）
    python3 purity_scan.py --quarantine --dry-run  # 预演隔离
    python3 purity_scan.py --quarantine            # 真正隔离
    python3 purity_scan.py --since 2026-10-01      # 只看某日之后创建的页
    python3 purity_scan.py --show 40               # 打印前 N 条明细

产物
----
    <KB>/_review/purity_scan_<ts>.json                    扫描报告
    <KB>/_review/offtopic/<date>/papers/*.md              已隔离页面
    <KB>/_review/offtopic/<date>/manifest.tsv             隔离清单
    <KB>/_review/offtopic/candidates_<date>.tsv           被引用、待人工分诊
"""
import argparse
import collections
import datetime as dt
import json
import os
import re
import shutil
import sys

_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _here)

from purity_gate import classify_page, parse_page  # noqa: E402


def kb_base():
    try:
        from kb_paths import BASE
        return BASE
    except Exception:
        return os.environ.get('KB_BASE', '/mnt/g/hermes_obsidian/hermes')


def read_created(content):
    m = re.search(r'^created:\s*(\S+)', content, re.M)
    return m.group(1).strip().strip('"\'') if m else ''


def collect_references(base):
    """扫描全库（evidence/relationships/entities/hypotheses/synthesis/根目录 md）
    的 [[wikilink]]，返回 Counter{被引用 slug: 引用次数}。

    2026-11-02：隔离前只查 evidence 会漏掉 synthesis / relationships / index.md
    里的引用，搬走页面会造成成片断链。这里改成全库一遍扫描。
    """
    refs = collections.Counter()
    rx = re.compile(r'\[\[([^\]|#]+)')
    scan_dirs = ['evidence', 'relationships', 'entities', 'hypotheses', 'synthesis',
                 'research-programs', 'concepts']
    roots = [base]
    for d in scan_dirs:
        p = os.path.join(base, d)
        if os.path.isdir(p):
            roots.append(p)
    seen = set()
    for root in roots:
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [x for x in dirnames if not x.startswith('.')]
            if dirpath.count(os.sep) - base.count(os.sep) > 3:
                continue
            for name in filenames:
                if not name.endswith('.md'):
                    continue
                fp = os.path.join(dirpath, name)
                if fp in seen:
                    continue
                seen.add(fp)
                try:
                    with open(fp, encoding='utf-8', errors='ignore') as fh:
                        body = fh.read()
                except Exception:
                    continue
                for slug in rx.findall(body):
                    refs[slug.strip()] += 1
    return refs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--quarantine', action='store_true', help='真正移动 nonplant 页面')
    ap.add_argument('--dry-run', action='store_true', help='与 --quarantine 同用则只报告')
    ap.add_argument('--since', default='', help='只处理 created >= 该日期的页面')
    ap.add_argument('--show', type=int, default=20, help='打印前 N 条明细')
    ap.add_argument('--out', default='', help='报告 JSON 路径')
    args = ap.parse_args()

    base = kb_base()
    papers = os.path.join(base, 'concepts', 'papers')
    if not os.path.isdir(papers):
        print('!! 找不到 %s' % papers)
        return 2

    names = sorted(n for n in os.listdir(papers) if n.endswith('.md'))
    counts = {'plant': 0, 'suspect': 0, 'nonplant': 0}
    nonplants, suspects = [], []
    by_journal = collections.Counter()
    for n in names:
        path = os.path.join(papers, n)
        try:
            content = open(path, encoding='utf-8', errors='ignore').read()
        except Exception:
            continue
        created = read_created(content)
        if args.since and created and created < args.since:
            counts['plant'] += 1
            continue
        verdict, reasons = classify_page(path)
        counts[verdict] += 1
        if verdict == 'plant':
            continue
        title, _abs, journal = parse_page(content)
        row = {'file': n, 'created': created, 'verdict': verdict,
               'title': title, 'journal': journal, 'reasons': reasons}
        by_journal[journal or '?'] += 1
        (nonplants if verdict == 'nonplant' else suspects).append(row)

    ts = dt.datetime.now().strftime('%Y%m%d_%H%M%S')
    report = {'scanned': len(names), 'counts': counts,
              'by_journal': dict(by_journal.most_common(50)),
              'nonplant': nonplants, 'suspect': suspects, 'since': args.since}
    out = args.out or os.path.join(base, '_review', 'purity_scan_%s.json' % ts)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as fh:
        json.dump(report, fh, ensure_ascii=False, indent=1)

    print('扫描 %d 页 | plant=%d suspect=%d nonplant=%d'
          % (len(names), counts['plant'], counts['suspect'], counts['nonplant']))
    print('报告: %s' % out)
    if by_journal:
        print('\n-- nonplant/suspect 的来源期刊（前 20）--')
        for j, c in by_journal.most_common(20):
            print('  %4d  %s' % (c, j))
    print('\n-- 前 %d 条 nonplant --' % args.show)
    for r in nonplants[:args.show]:
        print('  [%s] %s | %s' % (r['created'] or '-', r['file'], r['title'][:70]))
        print('        %s' % ','.join(r['reasons'][:3]))

    refs = safe = blocked = None
    if args.quarantine:
        refs = collect_references(base)
        safe = [r for r in nonplants if r['file'][:-3] not in refs]
        blocked = [r for r in nonplants if r['file'][:-3] in refs]
        print('\n引用感知：可安全隔离 %d 页；被 evidence 引用 %d 页 → 仅列候选'
              % (len(safe), len(blocked)))

    if not args.quarantine or args.dry_run:
        if args.quarantine:
            print('')
            print('[dry-run] 未移动任何文件。去掉 --dry-run 执行隔离。')
        return 0

    day = dt.date.today().isoformat()
    dest_dir = os.path.join(base, '_review', 'offtopic', day)
    dest_papers = os.path.join(dest_dir, 'papers')
    os.makedirs(dest_papers, exist_ok=True)
    manifest = os.path.join(dest_dir, 'manifest.tsv')
    cand = os.path.join(base, '_review', 'offtopic', 'candidates_%s.tsv' % day)

    moved = 0
    with open(manifest, 'w', encoding='utf-8') as mf:
        mf.write('file\tverdict\tjournal\ttitle\treasons\n')
        for r in safe:
            s_ = os.path.join(papers, r['file'])
            d_ = os.path.join(dest_papers, r['file'])
            if not os.path.exists(s_) or os.path.exists(d_):
                continue
            shutil.move(s_, d_)
            mf.write('%s\t%s\t%s\t%s\t%s\n' % (
                r['file'], r['verdict'], r['journal'],
                r['title'].replace('\t', ' '), ','.join(r['reasons'][:3])))
            moved += 1
    with open(cand, 'w', encoding='utf-8') as cf:
        cf.write('file\trefs\tverdict\tjournal\ttitle\treasons\n')
        for r in blocked:
            cf.write('%s\t%d\t%s\t%s\t%s\t%s\n' % (
                r['file'], refs[r['file'][:-3]], r['verdict'], r['journal'],
                r['title'].replace('\t', ' '), ','.join(r['reasons'][:3])))

    print('\n已隔离 %d 页 → %s' % (moved, dest_papers))
    print('隔离清单: %s' % manifest)
    print('人工分诊候选: %s' % cand)
    print('回滚: for f in %s/*.md; do mv "$f" %s/; done' % (dest_papers, papers))
    return 0


if __name__ == '__main__':
    sys.exit(main())
