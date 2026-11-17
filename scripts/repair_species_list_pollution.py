#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""清理证据页 species 列表中的“正则误标”残留（2026-11-02）。

背景
----
`species_patterns.py` 曾用 `\\bfig\\b` 匹配 Ficus carica，而 `re.I` 下
"Fig. 1"/"Fig. 2" 图注全部命中；"orange" 也把颜色词计入 Citrus。
上一轮只修了 `primary_species`，`species:` 列表里的污染值仍在（实测 970 页
带 Ficus carica，其中 949 页标题+断言完全不提 fig）。

规则（逐条可核验，不做统计推断）
--------------------------------
对每个受污染值（species -> 必要条件关键词组）：
  取证据页 source 指向的概念页，拼 title + 摘要；
  若关键词组一条都不出现 → 该值从 species 列表删除；
  若删除后列表为空 → 保留 primary_species（若非泛称）或写 Plant (unspecified)。

默认 dry-run，`--apply` 才写盘，并自动打包备份被改文件。
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys

from kb_paths import BASE, CONCEPTS_DIR, EVIDENCE_DIR

# species 值 -> 必须能在论文文本中找到的证据（任一命中即保留）
POLLUTION_RULES = {
    'Ficus carica': re.compile(r'\bficus\b|\bfig\b|\bfigs\b|\bfig\s+tree\b', re.I),
    'Citrus spp.': re.compile(r'\bcitrus\b', re.I),
    'Citrus sinensis': re.compile(r'\bcitrus\b|\bsweet\s+orange\b|\bnavel\s+orange\b', re.I),
}

GEN_PLACEHOLDER = ('Plant', 'Plant (unspecified)', '未识别', '')

# 合法物种名：属名（可带种加词 / spp. / × 杂种），或常见英文俗名。
# 其余（含 "**方法**: …"、"metabolomics (LC-MS/GC-MS)" 这类正文泄漏）视为脏值。
COMMON_NAMES = frozenset("""
maize rice wheat soybean tomato tobacco cotton potato barley sorghum grape apple
citrus poplar alfalfa cassava sugarcane banana tea moss fern
""".split())

TAXON_RES = (
    re.compile(r"^[A-Z][a-zA-Z\-]+$"),
    re.compile(r"^[A-Z][a-zA-Z\-]+\s+[a-z][a-zA-Z\-]+$"),
    re.compile(r"^[A-Z][a-zA-Z\-]+\s+(?:spp\.|sp\.)$"),
    re.compile(r"^[A-Z][a-zA-Z\-]+\s+×\s*[a-z][a-zA-Z\-]+$"),
)


def is_valid_species(x):
    x = (x or "").strip()
    if not x:
        return False
    if x in GEN_PLACEHOLDER or x.lower() in COMMON_NAMES:
        return True
    return any(rx.match(x) for rx in TAXON_RES)


def parse_list_field(content, key):
    m = re.search(r'^%s:\s*\[(.*?)\]' % re.escape(key), content, re.M | re.S)
    if m:
        return [x.strip().strip('"\'') for x in m.group(1).split(',') if x.strip()]
    m = re.search(r'^%s:\s*\n((?:[ \t]*-[ \t]*.+\n?)+)' % re.escape(key),
                  content, re.M)
    if m:
        return [x.strip().lstrip('-').strip().strip('"\'')
                for x in m.group(1).splitlines() if x.strip()]
    m = re.search(r'^%s:\s*"?([^"\n]+)"?\s*$' % re.escape(key), content, re.M)
    if m:
        v = m.group(1).strip().strip('"\'')
        return [v] if v else []
    return []


def str_field(content, key):
    m = re.search(r'^%s:\s*"?(.*?)"?\s*$' % re.escape(key), content, re.M)
    return m.group(1).strip() if m else ''


def abstract_of(content):
    m = re.search(r'^##\s*摘要\s*\n(.+?)(?=\n##|\Z)', content, re.S | re.M)
    if not m:
        m = re.search(r'^##\s*Abstract\s*\n(.+?)(?=\n##|\Z)', content, re.S | re.M)
    return m.group(1) if m else ''


def load_papers():
    out = {}
    if not os.path.isdir(CONCEPTS_DIR):
        return out
    for f in os.listdir(CONCEPTS_DIR):
        if not f.endswith('.md'):
            continue
        try:
            c = open(os.path.join(CONCEPTS_DIR, f), encoding='utf-8',
                     errors='replace').read()
        except OSError:
            continue
        out[f[:-3]] = (str_field(c, 'title') + ' ' + abstract_of(c))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--limit', type=int, default=0)
    args = ap.parse_args()

    papers = load_papers()
    changed = []      # (path, old_list, new_list)
    skipped_no_paper = 0
    for fname in sorted(os.listdir(EVIDENCE_DIR)):
        if not fname.endswith('.md'):
            continue
        path = os.path.join(EVIDENCE_DIR, fname)
        try:
            c = open(path, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        sp = parse_list_field(c, 'species')
        # 1) 结构性脏值：不像物种名的条目直接剔除（正文泄漏进 frontmatter）
        sp_clean = [x for x in sp
                    if is_valid_species(x)]
        hits = [s for s in sp_clean if s in POLLUTION_RULES]
        if not hits and sp_clean == sp:
            continue
        src = str_field(c, 'source').strip('"').strip('[]').strip()
        ptxt = papers.get(src)
        if not ptxt:
            skipped_no_paper += 1
            continue
        keep = list(sp_clean)
        for s in hits:
            if POLLUTION_RULES[s].search(ptxt):
                continue
            keep = [x for x in keep if x != s]
        if keep == sp:
            continue
        if not keep:
            prim = str_field(c, 'primary_species')
            keep = [prim] if prim and prim not in GEN_PLACEHOLDER else ['Plant (unspecified)']
        changed.append((path, sp, keep))
        if args.limit and len(changed) >= args.limit:
            break

    print('证据页待修改：%d（source 概念页缺失而跳过：%d）'
          % (len(changed), skipped_no_paper))
    for path, old, new in changed[:10]:
        print('  %s: %s -> %s' % (os.path.basename(path), old, new))
    if not args.apply:
        print('（dry-run，未写盘；加 --apply 执行）')
        return 0

    bak = os.path.expanduser('~/bak_species_list_%s.tgz' % __import__('datetime').date.today())
    rel = [os.path.relpath(p, BASE) for p, _, _ in changed]
    if rel:
        subprocess.run(['tar', '-czf', bak, '-C', BASE] + rel, check=True)
        print('备份：%s' % bak)
    n = 0
    for path, old, new in changed:
        c = open(path, encoding='utf-8', errors='replace').read()
        repl = 'species: [%s]' % ', '.join(new)
        c2, cnt = re.subn(r'^species:\s*\[.*?\]', repl, c, count=1, flags=re.M | re.S)
        if not cnt:
            continue
        open(path, 'w', encoding='utf-8').write(c2)
        n += 1
    print('已改写：%d 页；回滚：tar -xzf %s -C %s' % (n, bak, BASE))
    return 0


if __name__ == '__main__':
    sys.exit(main())
