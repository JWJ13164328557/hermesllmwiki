#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修正物种别名的歧义命中 + 定向重算 primary_species。

问题一：SPECIES_PATTERNS 里 `\\bfig\\b` 在 re.I 下命中 "Fig. 1"，
`\\borange\\b` 命中颜色词。摘要里图注多，导致 1802 条证据被标成
Ficus carica（实测 alfalfa 单细胞论文被标成无花果）。

问题二：旧回退逻辑从 `species:` 列表把污染值捡回来，810 条修不掉。

问题三：证据页的 claim 只是一句被截断的摘要，物种常常不在其中，
直接用 claim 重算会把大量页面降级为"未识别"。

本版做法：证据页 -> source: [[slug]] -> concepts/papers/<slug>.md 的完整摘要，
用「概念页 title + 摘要」重算，再用证据页 species 列表兜底（排除污染值）。

用法：python3 repair_species_mislabel.py [--apply]
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kb_paths
from species_patterns import primary_species

EV = kb_paths.EVIDENCE_DIR
SP = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'species_patterns.py')

FIXES = [
    (r"(r'\bFicus\s+carica\b|\bfig\b', 'Ficus carica'),",
     r"(r'\bFicus\s+carica\b|\bcommon\s+fig\b|\bedible\s+fig\b', 'Ficus carica'),"),
    (r"(r'\bCitrus\s+(sinensis|reticulata|clementina)\b|\b(citrus|orange)\b', 'Citrus spp.'),",
     r"(r'\bCitrus\s+(sinensis|reticulata|clementina)\b|\b(citrus|sweet\s+orange|navel\s+orange|blood\s+orange)\b', 'Citrus spp.'),"),
]

SUSPECT = ('Ficus carica', 'Citrus spp.')
GENERIC = ('Plant', 'Plant (unspecified)', '未识别', '')


def read(p):
    with io.open(p, 'r', encoding='utf-8') as f:
        return f.read()


def write(p, s):
    with io.open(p, 'w', encoding='utf-8') as f:
        f.write(s)


def patch_patterns():
    src = read(SP)
    state = []
    for old, new in FIXES:
        if new in src:
            state.append('already')
        elif old in src:
            src = src.replace(old, new, 1)
            state.append('patched')
        else:
            state.append('missing')
    write(SP, src)
    return state


def body_text(text):
    if text.startswith('---'):
        parts = text.split('---', 2)
        return parts[2] if len(parts) > 2 else text
    return text


def field(text, name):
    m = re.search(r'^%s:\s*"?(.*?)"?\s*$' % re.escape(name), text, re.M)
    return m.group(1).strip() if m else ''


def concept_abstract(slug):
    """从概念页取 (title, abstract)；找不到返回 ('','')。"""
    for base in (kb_paths.CONCEPTS_DIR, kb_paths.LEGACY_CONCEPTS_DIR):
        p = os.path.join(base, slug + '.md')
        if not os.path.isfile(p):
            continue
        t = read(p)
        mt = re.search(r'^title:\s*"?(.*?)"?\s*$', t, re.M)
        title = mt.group(1) if mt else ''
        ma = re.search(r'^##\s*摘要\s*\n(.+?)(?=\n##|\Z)', t, re.S | re.M)
        abstract = ' '.join(ma.group(1).split()) if ma else ''
        return title, abstract
    return '', ''


def main(argv):
    apply = '--apply' in argv
    print('species_patterns.py:', ', '.join(patch_patterns()))

    changed, from_concept, from_claim, still_unknown = [], 0, 0, 0
    for fn in sorted(os.listdir(EV)):
        if not fn.endswith('.md'):
            continue
        p = os.path.join(EV, fn)
        text = read(p)
        old = field(text, 'primary_species')
        if old not in SUSPECT:
            continue
        body = body_text(text)
        mt = re.search(r'^title:\s*"?(.*?)"?\s*$', text, re.M)
        title = mt.group(1) if mt else ''
        mc = re.search(r'^##\s*Claim\s*\n(.+?)(?=\n##|\Z)', body, re.S | re.M)
        claim = ' '.join(mc.group(1).split()) if mc else ''

        msrc = re.search(r'^source:\s*"?\[\[(.+?)\]\]"?\s*$', text, re.M)
        slug = msrc.group(1) if msrc else ''
        ctitle, cabstract = concept_abstract(slug) if slug else ('', '')

        new = ''
        if cabstract:
            new = primary_species(title=ctitle, abstract=cabstract, fulltext='')
            if new not in SUSPECT and new not in GENERIC:
                from_concept += 1
            else:
                new = ''
        if not new:
            new = primary_species(title=title, abstract=claim, fulltext='')
            if new in SUSPECT:
                new = ''
            elif new not in GENERIC:
                from_claim += 1
        if not new:
            ms = re.search(r'^species:\s*\[(.*?)\]', text, re.M)
            lst = [x.strip().strip('"\'') for x in ms.group(1).split(',')] if ms else []
            lst = [x for x in lst if x not in SUSPECT and x not in GENERIC]
            new = lst[0] if lst else 'Plant (unspecified)'
            if new == 'Plant (unspecified)':
                still_unknown += 1
        if new == old:
            continue
        changed.append((fn, old, new))
        if apply:
            text = re.sub(r'^(primary_species:\s*)"?[^"\n]*"?\s*$',
                          lambda m: m.group(1) + '"%s"' % new, text, count=1, flags=re.M)
            ms = re.search(r'^(species:\s*)\[(.*?)\]\s*$', text, re.M)
            if ms:
                items = [x.strip().strip('"\'') for x in ms.group(2).split(',')]
                items = [x for x in items if x not in SUSPECT]
                if not items:
                    items = [new]
                if new not in items:
                    items.insert(0, new)
                seen, uniq = set(), []
                for x in items:
                    if x not in seen:
                        seen.add(x)
                        uniq.append(x)
                text = (text[:ms.start()] + ms.group(1) + '['
                        + ', '.join(uniq) + ']' + text[ms.end():])
            text = re.sub(r'^(- 主要物种:\s*).*$', lambda m: m.group(1) + new,
                          text, count=1, flags=re.M)
            write(p, text)

    print('changed: %d (from concept abstract: %d, from claim: %d, unknown: %d)'
          % (len(changed), from_concept, from_claim, still_unknown))
    for fn, o, n in changed[:12]:
        print('   %s: %s -> %s' % (fn, o, n))
    if not apply:
        print('DRY-RUN: nothing written.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
