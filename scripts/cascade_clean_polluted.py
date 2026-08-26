#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cascade_clean_polluted.py — 级联清理已移入 .trash 的污染概念页的关联数据
================================================================================
背景: 用修复后的 theme_filter 扫描出 194 个存量污染概念页, 已 git mv 到
      .trash/polluted/. 但与其关联的 evidence 和 raw/articles 还在原位,
      需级联清理防止断链/污染残留 (对应 del_concept_cascade 的级联原则)。

用法:
    /usr/bin/python3 scripts/cascade_clean_polluted.py --manifest .trash/polluted_manifest_20260826.txt [--dry-run]
        --manifest : 污染概念页清单(每行: rel_path \t reason \t title; # 开头为注释)
        --dry-run  : 只打印将处理的对象, 不实际移动
输出: 统计移动的 evidence / raw 数量, 并重新扫描残留断链。
"""
import os, re, shutil, argparse, glob
from datetime import datetime

BASE = '/mnt/g/hermes_obsidian/hermes'
EVIDENCE = f'{BASE}/evidence'
RAW = f'{BASE}/raw/articles'
TRASH = f'{BASE}/.trash/polluted_cascade_{datetime.now():%Y%m%d}'

def read_slugs(manifest):
    """从 manifest 读 slug 列表(相对路径最后一段去 .md)。"""
    slugs = set()
    with open(manifest, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            rel = line.split('\t')[0]
            base = os.path.basename(rel).replace('.md', '')
            if base:
                slugs.add(base)
    return slugs

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--manifest', required=True, help='污染清单文件路径')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    slugs = read_slugs(args.manifest)
    print(f'污染概念页 slug 数: {len(slugs)}')

    # ── 1) evidence 级联: source: [[slug]] 指向污染概念页的 → 移动 ──
    ev_targets = []
    for fp in glob.glob(f'{EVIDENCE}/*.md'):
        try:
            c = open(fp, encoding='utf-8', errors='ignore').read(800)
        except Exception:
            continue
        for m in re.finditer(r'source:\s*"?\[\[([^\]|#]+)', c):
            if m.group(1).strip() in slugs:
                ev_targets.append(fp)
                break
    print(f'关联 evidence: {len(ev_targets)} 个')

    # ── 2) raw/articles 对应: <slug>.md → 移动 ──
    raw_targets = []
    for s in slugs:
        rp = f'{RAW}/{s}.md'
        if os.path.exists(rp):
            raw_targets.append(rp)
    print(f'关联 raw/articles: {len(raw_targets)} 个')

    if args.dry_run:
        print('[dry-run] 不实际移动')
        for fp in ev_targets[:10]: print(f'  evidence: {os.path.basename(fp)}')
        for fp in raw_targets[:10]: print(f'  raw: {os.path.basename(fp)}')
        return

    # ── 实际移动 ──
    os.makedirs(f'{TRASH}/evidence', exist_ok=True)
    os.makedirs(f'{TRASH}/raw_articles', exist_ok=True)
    for fp in ev_targets:
        shutil.move(fp, f'{TRASH}/evidence/{os.path.basename(fp)}')
    for fp in raw_targets:
        shutil.move(fp, f'{TRASH}/raw_articles/{os.path.basename(fp)}')
    print(f'已移动 evidence {len(ev_targets)} 个, raw {len(raw_targets)} 个 → {TRASH}/')

    # ── 3) 断链复检 ──
    # 现有概念页 slug (papers + 顶层 daily)
    existing = {os.path.basename(f).replace('.md','') for f in glob.glob(f'{BASE}/concepts/papers/*.md')}
    existing |= {os.path.basename(f).replace('.md','') for f in glob.glob(f'{BASE}/concepts/*.md')}
    existing |= {os.path.basename(f).replace('.md','') for f in glob.glob(f'{BASE}/concepts/methods/*.md')}
    orphans = {}
    for fp in glob.glob(f'{EVIDENCE}/*.md'):
        try:
            c = open(fp, encoding='utf-8', errors='ignore').read(800)
        except Exception:
            continue
        for m in re.finditer(r'source:\s*"?\[\[([^\]|#]+)', c):
            if m.group(1).strip() not in existing:
                orphans[os.path.basename(fp)] = m.group(1)
                break
    print(f'清理后残留断链 evidence: {len(orphans)}')
    for k, v in list(orphans.items())[:15]:
        print(f'  ⚠️ {k} → [[{v}]]')

if __name__ == '__main__':
    main()
