#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
del_concept_cascade.py — 强制级联删除概念页及其 evidence (2026-08-25 审稿建议)
================================================================================
用法:
    /usr/bin/python3 scripts/del_concept_cascade.py <slug-or-doi...> [--trash DIR]
    /usr/bin/python3 scripts/del_concept_cascade.py --from-file list.txt
    /usr/bin/python3 scripts/del_concept_cascade.py --list-orphans   # 列出断链evidence

设计: 删除任意概念页时【必须】连带删除所有 source 指向它的 evidence,
否则破坏可追溯性(A1 教训: 上次删污染概念页遗留 11 条断链 evidence)。
- 全部移到 .trash (可恢复), 不物理删除
- 默认 .trash_del_concept_YYYYMMDD/
默认检查: 删除后重新扫描 evidence, 报告残留断链。
"""
import os, re, glob, sys, shutil, argparse
from datetime import datetime

BASE = '/mnt/g/hermes_obsidian/hermes'
CONCEPTS = f'{BASE}/concepts/papers'


def find_concept(slugs, dois):
    """按 slug 或 doi 找到概念页文件"""
    found = []
    for fp in glob.glob(f'{CONCEPTS}/*.md'):
        slug = os.path.basename(fp).replace('.md','')
        c = open(fp, encoding='utf-8', errors='ignore').read(1500)
        dm = re.search(r'^doi:\s*"?\s*(10\.\d{4,}/[^\s"\n`]+)', c, re.M)
        doi = dm.group(1).strip().rstrip('./').lower() if dm else ''
        if slug in slugs or (doi and doi in dois):
            found.append(fp)
    return found


def orphan_evidences():
    """扫描 evidence 断链(指向不存在概念页的), 返回 {ev_id: broken_source_slug}"""
    slugs = {os.path.basename(f).replace('.md','') for f in glob.glob(f'{CONCEPTS}/*.md')}
    slugs |= {os.path.basename(f).replace('.md','') for f in glob.glob(f'{BASE}/concepts/methods/*.md')}
    orphans = {}
    for fp in glob.glob(f'{BASE}/evidence/*.md'):
        c = open(fp, encoding='utf-8', errors='ignore').read(800)
        for m in re.finditer(r'source:\s*"?\[\[([^\]|#]+)', c):
            if m.group(1) not in slugs:
                orphans[os.path.basename(fp)] = m.group(1)
    return orphans


def cascade_delete(target_fps, trash_dir):
    """删除概念页 + 连带删其 evidence(site指向该概念页)"""
    os.makedirs(trash_dir + '/concepts', exist_ok=True)
    os.makedirs(trash_dir + '/evidence', exist_ok=True)
    target_slugs = {os.path.basename(f).replace('.md','') for f in target_fps}
    # 移动概念页
    for fp in target_fps:
        shutil.move(fp, f'{trash_dir}/concepts/{os.path.basename(fp)}')
    # 连带删 evidence (source 指向这些 slug 的)
    ev_moved = 0
    for fp in glob.glob(f'{BASE}/evidence/*.md'):
        c = open(fp, encoding='utf-8', errors='ignore').read(800)
        for m in re.finditer(r'source:\s*"?\[\[([^\]|#]+)', c):
            if m.group(1) in target_slugs:
                shutil.move(fp, f'{trash_dir}/evidence/{os.path.basename(fp)}')
                ev_moved += 1
                break
    # 检查残留断链
    orphans = orphan_evidences()
    return len(target_fps), ev_moved, orphans


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('slugs', nargs='*', help='concept slug 或 DOI')
    ap.add_argument('--from-file', help='每行一个slug/doi')
    ap.add_argument('--list-orphans', action='store_true', help='只列出断链evidence')
    ap.add_argument('--trash', default=None)
    args = ap.parse_args()

    if args.list_orphans:
        o = orphan_evidences()
        print(f"断链 evidence: {len(o)}")
        for k, v in sorted(o.items())[:50]: print(f"  {k} → [[{v}]]")
        return

    slugs, dois = set(), set()
    items = list(args.slugs)
    if args.from_file:
        items += [l.strip() for l in open(args.from_file) if l.strip()]
    for it in items:
        (dois if it.lower().startswith('10.') else slugs).add(it.strip())

    target = find_concept(slugs, dois)
    if not target:
        print("未找到匹配概念页"); return
    trash = args.trash or f'{BASE}/.trash_del_concept_{datetime.now():%Y%m%d}'
    n, ev, orphans = cascade_delete(target, trash)
    print(f"删除概念页 {n} 个 → {trash}/concepts/")
    print(f"连带删除 evidence {ev} 个 → {trash}/evidence/")
    print(f"删除后残留断链: {len(orphans)}")
    for k, v in list(orphans.items())[:10]: print(f"  ⚠️ {k} → [[{v}]]")


if __name__ == '__main__':
    main()
