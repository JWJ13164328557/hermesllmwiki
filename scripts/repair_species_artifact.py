#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""repair_species_artifact.py — 清理 **物种** 行里的正则伪影物种（2026-11-03 第 17 轮）。

背景
----
提炼层曾用裸子串匹配 'fig' / 'orange'，把 "Fig. 1"、颜色词、configuration 都算成
Ficus carica / Citrus。已修的匹配逻辑不会再生新污染，但历史页面仍是脏的。

规则（两态，可逐条复核）
------------------------
对每个页面 **物种** 行中的伪影物种（Ficus carica / Citrus spp. / Citrus sinensis）：
  * 摘要存在（>=1 字符）→ 在「标题 + 摘要」里按整词/中文同义词查找支持；
      无支持 → 从 **物种** 行删除（这是可判定的错标）。
  * 摘要缺失 → 不可判定，**不删**，在 frontmatter 写 species_status: unverified，
      保留原值供人工核对。宁可漏放不可误杀。

此外处理同一根因的第二类伪影（class-B）：物种的英文俗名以**子串**形式出现、却从不以整词出现。实测 price/matrices → rice、tricornutum/Cronobacter/cornerstone → corn、appear → pear。判据要求「有子串命中」且「无整词命中」，因此不会因为综述摘要没提某物种就删它。不做统计推断，不改任何其他字段。默认 dry-run。
"""
from __future__ import annotations
import argparse, io, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb_paths import CONCEPTS_DIR

ART = {
    'Ficus carica': re.compile(
        r'\bficus\b|\bcommon\s+fig\b|\bedible\s+fig\b|\bfig\s+tree\b|'
        r'\bfigs?\b(?!\s*[.\-]?\s*\d)|无花果', re.I),
    'Citrus spp.': re.compile(r'\bcitrus\b|柑橘|柑|橘|橙|柚|\borange\b|\blemon\b', re.I),
    'Citrus sinensis': re.compile(
        r'\bcitrus\b|\bsweet\s+orange\b|\bnavel\s+orange\b|柑橘|脐橙|甜橙', re.I),
}
SP_RE = re.compile(r'^\*\*物种\*\*:\s*(.+)$', re.M)

# class-B：俗名只会以子串误命中的物种。值为（子串证据, 整词支持）
SUBS = {
    'Oryza sativa': (r'rice', r'\brice\b|\boryza\b'),
    'Zea mays': (r'corn', r'\bcorn\b|\bmaize\b|\bzea\b'),
    'Pyrus spp.': (r'pear', r'\bpear\b|\bpyrus\b'),
    'Capsicum annuum': (r'pepper', r'\bpepper\b|\bcapsicum\b'),
    'Zingiber officinale': (r'ginger', r'\bginger\b|\bzingiber\b'),
    'Cucumis spp.': (r'melon', r'\bmelon\b|\bcucumis\b|\bcucumber\b'),
    'Beta vulgaris': (r'beet', r'\bbeet\b|\bbeta\b'),
    'Pisum sativum': (r'pea', r'\bpea\b|\bpeas\b|\bpisum\b'),
    'Pinus spp.': (r'pine', r'\bpine\b|\bpinus\b'),
    'Quercus spp.': (r'oak', r'\boak\b|\bquercus\b'),
    'Malus domestica': (r'apple', r'\bapple\b|\bapples\b|\bmalus\b'),
}


def substring_only(names, text):
    """返回「子串命中但无整词支持」的物种名（class-B 伪影）。"""
    out = []
    for n in names:
        if n not in SUBS:
            continue
        sub, whole = SUBS[n]
        if re.search(sub, text, re.I) and not re.search(whole, text, re.I):
            out.append(n)
    return out


def support_text(text):
    body = text.split('## 深度提炼')[0]
    m = re.search(r'^title:\s*"?(.*?)"?\s*$', body, re.M)
    title = m.group(1) if m else ''
    m = re.search(r'^##\s*(?:摘要|Abstract)\s*\n(.+?)(?=\n##|\Z)', body, re.S | re.M)
    return title + ' ' + (m.group(1) if m else ''), (m.group(1).strip() if m else '')


def set_flag(text, key, value):
    if re.search(r'^%s:' % re.escape(key), text, re.M):
        return re.sub(r'^%s:.*$' % re.escape(key), '%s: %s' % (key, value), text, count=1, flags=re.M)
    m = re.search(r'^---\n(.*?)\n---', text, re.S)
    if not m:
        return text
    return text[:m.end(1)] + '\n%s: %s' % (key, value) + text[m.end(1):]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    a = ap.parse_args()
    removed = flagged = 0
    samples = []
    for fn in sorted(os.listdir(CONCEPTS_DIR)):
        if not fn.endswith('.md'):
            continue
        p = os.path.join(CONCEPTS_DIR, fn)
        text = io.open(p, encoding='utf-8', errors='replace').read()
        m = SP_RE.search(text)
        if not m:
            continue
        names = [x.strip() for x in re.split(r'[;；,/、]', m.group(1)) if x.strip()]
        sup, abstract = support_text(text)
        bad = [n for n in names if n in ART and not ART[n].search(sup)]
        # class-B 只在有摘要时执行：无摘要无法确认子串是否真是伪影
        if abstract:
            for n in substring_only(names, sup):
                if n not in bad:
                    bad.append(n)
        if not bad:
            continue
        if abstract:
            keep = [n for n in names if n not in bad]
            new = '**物种**: %s' % (', '.join(keep) if keep else '—')
            text = text.replace(m.group(0), new, 1)
            removed += 1
            if len(samples) < 5:
                samples.append('%s: -%s' % (fn, ','.join(bad)))
        else:
            text = set_flag(text, 'species_status', 'unverified')
            flagged += 1
        if a.apply:
            tmp = p + '.tmp'
            io.open(tmp, 'w', encoding='utf-8', newline='\n').write(text)
            os.replace(tmp, p)
    print(json_dump := '{"removed": %d, "flagged_unverified": %d, "apply": %s}'
          % (removed, flagged, 'true' if a.apply else 'false'))
    for s in samples:
        print('  ', s)


if __name__ == '__main__':
    main()
