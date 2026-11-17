#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""标签别名归一化：把历史遗留的主题 ID 收敛到规范 ID。

2026-11-03 体检发现同一主题在库里有两套 ID 并存：

    single-cell-spatial(193 证据/121 论文) vs single-cell-spatial-omics
    metabolism-np      (144/144)           vs metabolism-natural-products
    epigenetics-gr      (96/33)            vs epigenetics-gene-regulation

外加一批带井号的脏标签（#metabolism-np 57 条、#stress-immunity 7 条、
#epigenetics-gr 4 条），它们让 themes_from_tags 之外的任何脚本都数不准。

本脚本只做两件事，且都可逆、可 dry-run：
  1. 去掉标签的 '#' 前缀与多余引号；
  2. 把三个历史主题 ID 替换成规范 ID，去重并保持原顺序。

**不做**的事（避免制造新的语义损失）：
  * 不把 metabolism / papers 这类泛化桶强转成主题（见 themes.py GENERIC_TAGS）；
  * 不改 starch-sugar / terpenoid / scrnaseq 这类关键词标签（它们是检索价值，
    主题归属由 THEME_TAG_ALIASES 在读取时归一）；
  * 不改 theme_status、不改正文。

用法
----
    python3 scripts/repair_tag_aliases.py --dry-run
    python3 scripts/repair_tag_aliases.py --apply
"""
import argparse
import collections
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb_paths import BASE, CONCEPTS_DIR, EVIDENCE_DIR

LEGACY_TO_CANONICAL = {
    'single-cell-spatial': 'single-cell-spatial-omics',
    'metabolism-np': 'metabolism-natural-products',
    'epigenetics-gr': 'epigenetics-gene-regulation',
}

LIST_FIELD = re.compile(r'^(tags|themes)\s*:\s*(\[.*\])\s*$', re.M)


def _split(text):
    if not text.startswith('---'):
        return None, text
    end = text.find('\n---', 3)
    if end < 0:
        return None, text
    return text[3:end], text[end:]


def _parse(raw):
    raw = raw.strip()
    if raw.startswith('[') and raw.endswith(']'):
        raw = raw[1:-1]
    return [x.strip().strip('"\'') for x in raw.split(',') if x.strip()]


def _clean_tag(tag):
    """去井号/引号/空白，保留大小写以外的一切语义。"""
    t = tag.strip().strip('"\'')
    while t.startswith('#'):
        t = t[1:].strip()
    return t


def normalize_list(tags):
    """返回 (新列表, 是否有改动)。"""
    out, seen, changed = [], set(), False
    for t in tags:
        c = _clean_tag(t)
        if c != t:
            changed = True
        c = LEGACY_TO_CANONICAL.get(c.lower(), c)
        if c != _clean_tag(t):
            changed = True
        key = c.lower()
        if not c or key in seen:
            changed = True
            continue
        seen.add(key)
        out.append(c)
    if out != list(tags):
        changed = True
    return out, changed


def process(path, stats, dry):
    try:
        text = io.open(path, encoding='utf-8', errors='replace').read()
    except OSError:
        stats['unreadable'] += 1
        return False
    fm, body = _split(text)
    if fm is None:
        stats['no_frontmatter'] += 1
        return False
    new_fm, any_change = fm, False
    for m in list(LIST_FIELD.finditer(fm)):
        key = m.group(1)
        old = _parse(m.group(2))
        new, changed = normalize_list(old)
        if not changed:
            continue
        any_change = True
        if len(new) != len(old):
            stats['deduped'] += len(old) - len(new)
        line = '%s: [%s]' % (key, ', '.join(new))
        new_fm = new_fm[:m.start()] + line + new_fm[m.end():]
        for t in old:
            c = _clean_tag(t)
            if c != t:
                stats['hash_stripped'] += 1
            if LEGACY_TO_CANONICAL.get(c.lower()):
                stats['alias_mapped'] += 1
    if not any_change:
        stats['unchanged'] += 1
        return False
    stats['changed'] += 1
    if dry:
        return True
    # 先拼完整内容再写临时文件，最后原子替换——绝不在计算过程中截断原文。
    payload = '---' + new_fm + body
    tmp = path + '.tmp'
    io.open(tmp, 'w', encoding='utf-8', newline='\n').write(payload)
    os.replace(tmp, path)
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()
    dry = not args.apply
    stats = collections.Counter()
    dirs = [d for d in (EVIDENCE_DIR, CONCEPTS_DIR) if os.path.isdir(d)]
    for d in dirs:
        for fn in sorted(os.listdir(d)):
            if fn.endswith('.md'):
                process(os.path.join(d, fn), stats, dry)
    mode = 'DRY-RUN' if dry else 'APPLY'
    print('[%s] 扫描目录 %s' % (mode, ', '.join(dirs)))
    print('  变更文件 %d；未变 %d；去重标签 %d；去井号 %d；别名归一 %d；无 frontmatter %d'
          % (stats['changed'], stats['unchanged'], stats['deduped'],
             stats['hash_stripped'], stats['alias_mapped'], stats['no_frontmatter']))


if __name__ == '__main__':
    main()
