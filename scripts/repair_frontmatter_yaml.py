#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""repair_frontmatter_yaml.py - 修复非法 frontmatter（孤儿列表项 + 控制字符）。

两类真实故障，都会让 Obsidian/Dataview 静默丢掉整段字段：

A. 孤儿列表项。键行是 inline 值 `themes: [x]` 或 `tags: []`，其后却残留
   顶格 `- item`（序列项没有所属键），YAML 非法。
   成因：repair_theme_tags._set_field / repair_pubmed_doi._set_field 用
   `^key\\s*:.*$` 只替换键行，原块列表续行被留在原地。

B. 控制字符。PDF 抽取把 0x01-0x08 原样写进 title，PyYAML 抛
   ReaderError: unacceptable character，整页不可解析。

C. 围栏粘连（2026-11-04 新增）。frontmatter.set_field 旧实现丢掉前导换行，
   调用方拼出 '---scope_status: nonplant'，Obsidian 里整页属性失效；但 YAML
   把分隔符之后当映射，旧版 split()/自检都判 OK，直到自检补上"围栏独占一行"
   才暴露。

D. 冒号标量（2026-11-04 新增）。excluded_reason 里直接拼论文标题，
   标题中的 ': ' 让 YAML 认为是嵌套映射。

处理：先剔控制字符，再把孤儿项并回上方那个 inline 标量键（去重；
themes 键上的 `other`/别名归一后丢弃），合并后重新 yaml.safe_load 校验。
仍不合法的页面不写，进 candidates TSV 人工看。

用法：
    python3 repair_frontmatter_yaml.py --dry-run
    python3 repair_frontmatter_yaml.py --apply
"""
import argparse
import collections
import io
import os
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb_paths import BASE  # noqa: E402
import frontmatter as F  # noqa: E402
import themes as th  # noqa: E402

SUBDIRS = ('concepts/papers', 'concepts/methods', 'evidence', 'entities',
           'relationships', 'synthesis', 'hypotheses', 'research-programs')
REPORT = os.path.join(BASE, '_review', 'frontmatter_repair.tsv')


def theme_norm(item):
    t = th.normalize_tag(item)
    if not t or t == 'other':
        return None
    return th.THEME_TAG_ALIASES.get(t, t)


def iter_files():
    for sub in SUBDIRS:
        d = os.path.join(BASE, sub)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if fn.endswith('.md'):
                yield os.path.join(d, fn)


def yaml_ok(fm):
    try:
        return isinstance(yaml.safe_load(fm), dict)
    except Exception:
        return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()
    dry = not args.apply

    stats = collections.Counter()
    rows = []
    for path in iter_files():
        try:
            raw = io.open(path, encoding='utf-8', errors='ignore').read()
        except OSError:
            stats['unreadable'] += 1
            continue
        unfenced = F.unfence(raw)
        glued = unfenced != raw
        if glued:
            stats['glued_fence'] += 1
            raw = unfenced
        fm, body = F.split(raw)
        if not fm:
            stats['no_frontmatter'] += 1
            continue
        if yaml_ok(fm) and not glued:
            stats['already_ok'] += 1
            continue
        clean = F.sanitize_ctrl(fm)
        if clean != fm:
            stats['ctrl_stripped'] += 1
        clean, junk = F.clean_inline_lists(clean)
        if junk:
            stats["junk_items"] += junk
        new_fm, merged = F.repair_orphans(clean, themes_norm=theme_norm)
        new_fm, quoted = F.quote_broken_scalars(new_fm)
        if quoted:
            stats['quoted_scalars'] += len(quoted)
        if not yaml_ok(new_fm):
            stats['still_broken'] += 1
            rows.append((os.path.relpath(path, BASE), 'still_broken', merged))
            continue
        if new_fm == fm:
            stats['broken_but_unchanged'] += 1
            rows.append((os.path.relpath(path, BASE), 'unchanged', 0))
            continue
        stats['repaired'] += 1
        stats['merged_items'] += merged
        rows.append((os.path.relpath(path, BASE), 'repaired', merged))
        if dry:
            continue
        tmp = path + '.tmp'
        with io.open(tmp, 'w', encoding='utf-8', newline='\n') as fh:
            fh.write('---' + new_fm + body)
        os.replace(tmp, path)

    os.makedirs(os.path.dirname(REPORT), exist_ok=True)
    with io.open(REPORT, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write('file\tstatus\tmerged\n')
        for r in rows:
            fh.write('%s\t%s\t%d\n' % r)

    print(('[dry-run] ' if dry else '[apply] ') +
          ' '.join('%s=%d' % kv for kv in sorted(stats.items())))
    print('report:', REPORT)
    return 0 if stats['still_broken'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())