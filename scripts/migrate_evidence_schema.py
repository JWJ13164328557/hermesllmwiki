#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""migrate_evidence_schema.py — 把历史 Evidence 对象迁移到诚实的 schema。

只做四件事，且**只改 evidence/*.md**：
  1. 删除 "## Contradictory Evidence / _None identified_" 与空的 "## Open Questions"
     —— 这两段从未真正检索过，留着会让人误以为核对过。
  2. 补 primary_species（旧文件按正则表顺序取前 3，看不出谁是研究对象）。
  3. 补 quality_basis: "keyword-heuristic"，说明质量等级是关键词推断。
  4. 补一段"自动标注，引用前请核对"的说明。

默认 dry-run，只报告将要发生什么；--apply 才落盘。内容无变化的文件不会被重写。

用法:
    python3 scripts/migrate_evidence_schema.py            # 预演
    python3 scripts/migrate_evidence_schema.py --apply    # 执行
    python3 scripts/migrate_evidence_schema.py --limit 20 --verbose
"""
import argparse
import os
import re
import sys

from kb_paths import BASE
from species_patterns import primary_species

EVIDENCE_DIR = os.path.join(BASE, 'evidence')
CONCEPTS_DIR = os.path.join(BASE, 'concepts', 'papers')

NOTE = """
## 标注信息

> 本页的基因/化合物/物种与质量等级均由正则自动标注（quality_basis: keyword-heuristic），
> 可能漏标或误标；引用前请回原文核对。
"""

PLACEHOLDER_BLOCKS = [
    re.compile(r'\n## Contradictory Evidence\n\s*_None identified_\s*(?=\n## |\n---|\Z)'),
    re.compile(r'\n## Contradictory Evidence\n\s*-\s*(?=\n## |\n---|\Z)'),
    re.compile(r'\n## Open Questions\n\s*-\s*(?=\n## |\n---|\Z)'),
]


def concept_title_summary():
    """slug -> (title, summary)，用于在缺少"主要物种"字段时推断主物种。"""
    out = {}
    if not os.path.isdir(CONCEPTS_DIR):
        return out
    for fname in sorted(os.listdir(CONCEPTS_DIR)):
        if not fname.endswith('.md'):
            continue
        try:
            with open(os.path.join(CONCEPTS_DIR, fname), encoding='utf-8', errors='replace') as f:
                text = f.read()
        except OSError:
            continue
        m = re.search(r'^# (.+)$', text, re.M)
        out[fname[:-3]] = (m.group(1) if m else fname[:-3], text.split('## 深度提炼')[0])
    return out


def migrate_text(text, slug, ctx):
    changed = []
    original = text

    for pat in PLACEHOLDER_BLOCKS:
        new = pat.sub('', text)
        if new != text:
            changed.append('removed-placeholder')
            text = new

    if not re.search(r'^primary_species:', text, re.M):
        title, summary = ctx.get(slug, ('', ''))
        species_field = re.search(r'^species:\s*\[(.*?)\]', text, re.M)
        if species_field:
            first = species_field.group(1).split(',')[0].strip()
        else:
            first = ''
        # 有"主要物种"字段就信它；否则按标题/摘要重新排序，别沿用旧的三物种顺序
        ps = first if first and first != 'Plant' else primary_species(title=title, abstract=summary)
        text = re.sub(r'^(species:.*)$', r'\1\nprimary_species: "%s"' % ps, text, count=1, flags=re.M)
        changed.append('added-primary-species')

    if 'quality_basis:' not in text and re.search(r'^quality:', text, re.M):
        text = re.sub(r'^(quality:.*)$', r'\1\nquality_basis: "keyword-heuristic"', text, count=1, flags=re.M)
        changed.append('added-quality-basis')

    if '## 标注信息' not in text:
        text = text.rstrip('\n') + '\n' + NOTE
        changed.append('added-note')

    return text, changed, text != original


def main():
    ap = argparse.ArgumentParser(description='Evidence schema 迁移（默认 dry-run）')
    ap.add_argument('--apply', action='store_true', help='真正写入（默认只预演）')
    ap.add_argument('--limit', type=int, default=5, help='verbose 时列出的样例数')
    ap.add_argument('--verbose', action='store_true')
    args = ap.parse_args()

    if not os.path.isdir(EVIDENCE_DIR):
        print(f'[ERROR] 找不到 {EVIDENCE_DIR}', file=sys.stderr)
        return 2

    ctx = concept_title_summary()
    total = would_change = 0
    tally = {}
    samples = []

    for fname in sorted(os.listdir(EVIDENCE_DIR)):
        if not fname.endswith('.md'):
            continue
        total += 1
        path = os.path.join(EVIDENCE_DIR, fname)
        try:
            with open(path, encoding='utf-8') as f:
                text = f.read()
        except OSError:
            continue
        slug = ''
        m = re.search(r'^source:\s*"\[\[(.+?)\]\]"', text, re.M)
        if m:
            slug = m.group(1)

        new_text, changed, differs = migrate_text(text, slug, ctx)
        if not differs:
            continue
        would_change += 1
        for c in changed:
            tally[c] = tally.get(c, 0) + 1
        if args.verbose and len(samples) < args.limit:
            samples.append((fname, changed))
        if args.apply:
            with open(path, 'w', encoding='utf-8', newline='\n') as f:
                f.write(new_text)

    print(f'BASE   = {BASE}')
    print(f'扫描   = {total} 个证据文件')
    print(f'将修改 = {would_change} 个')
    for k, v in sorted(tally.items(), key=lambda kv: -kv[1]):
        print(f'  - {k}: {v}')
    for fname, changed in samples:
        print(f'  样例 {fname}: {", ".join(changed)}')
    print('模式   =', 'APPLY（已写入）' if args.apply else 'DRY-RUN（未改动任何文件）')
    return 0


if __name__ == '__main__':
    sys.exit(main())