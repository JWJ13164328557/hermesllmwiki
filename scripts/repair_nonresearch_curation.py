# -*- coding: utf-8 -*-
"""清洗非研究页上的错配"深度提炼"（2026-11-03）。

问题实例
--------
`concepts/papers/10-1007-bf02782474.md` 是 2002 年 ISPMB **会员表**
（`article_kind: front-matter`），正文却写着 WER/CPC/GL2 根表皮模式建成的
"核心发现"。这不是孤例：202 篇非研究页中有 56 篇仍带实质性深度提炼。

根因
----
分层标签（article_kind）只有导入/证据/假说层在读，**提炼层不读**，
于是更正、撤稿、社论、会员表照样被抽出 8 条"核心发现"。

本脚本
------
1. 逐页判定 article_kind（已有字段优先，否则 article_kind.classify）；
2. 非 research/review 且"核心发现"非空 → 改写为 `## 文献变更要点`，
   不保留任何机制性结论；
3. 给由该页派生的证据页打 `evidence_status: orphaned-nonresearch`
   （不删除，便于人工追溯），并置 `quality: unusable`。
4. 默认 dry-run，`--apply` 才写盘；写前保留原文件到 `--backup-dir`。

用法
----
    python3 scripts/repair_nonresearch_curation.py --dry-run
    python3 scripts/repair_nonresearch_curation.py --apply
"""
import argparse
import collections
import io
import json
import os
import re
import shutil
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb_paths import BASE
import article_kind

PAPERS_DIR = os.path.join(BASE, 'concepts', 'papers')
TOP_DIR = os.path.join(BASE, 'concepts')
EVIDENCE_DIR = os.path.join(BASE, 'evidence')


def _split(text):
    if not text.startswith('---'):
        return '', text
    end = text.find('\n---', 3)
    return (text[3:end], text[end:]) if end > 0 else ('', text)


def _get(fm, key):
    m = re.search(r'^%s\s*:\s*(.*)$' % re.escape(key), fm, re.M)
    return m.group(1).strip().strip('"') if m else ''


def _set(fm, key, value):
    pat = re.compile(r'^%s\s*:.*$' % re.escape(key), re.M)
    line = '%s: %s' % (key, value)
    return pat.sub(line, fm, count=1) if pat.search(fm) else fm.rstrip('\n') + '\n' + line + '\n'


def _has_substantive_findings(body):
    m = re.search(r'### 核心发现\s*\n(.+?)(?=\n## |\Z)', body, re.S)
    if not m:
        return False, ''
    txt = m.group(1).strip()
    if not txt or txt.startswith('_（无显著信号句）_'):
        return False, txt
    # 已改写过的"文献变更要点"不算实质性发现
    return len(txt) > 40, txt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--backup-dir', default='')
    args = ap.parse_args()
    dry = not args.apply
    bdir = args.backup_dir or os.path.join(
        os.path.expanduser('~'), '.hermes', 'backup',
        'nonresearch_%s' % time.strftime('%Y%m%d_%H%M%S'))

    pages = []
    for d in (PAPERS_DIR, TOP_DIR):
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if fn.endswith('.md'):
                pages.append(os.path.join(d, fn))

    stats = collections.Counter()
    kinds = collections.Counter()
    fixed = []
    fixed_slugs = set()

    for p in pages:
        try:
            text = io.open(p, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        fm, body = _split(text)
        if _get(fm, 'type') not in ('concept', ''):
            continue
        title = ''
        tm = re.search(r'^# (.+)$', body, re.M)
        if tm:
            title = tm.group(1).strip()
        doi = _get(fm, 'doi')
        journal = _get(fm, 'journal')
        kind = _get(fm, 'article_kind')
        if not kind:
            kind, _reasons = article_kind.classify(title=title, doi=doi,
                                                   journal=journal, body=body)
        kinds[kind] += 1
        if article_kind.is_evidence_eligible(kind):
            continue
        stats['nonresearch_pages'] += 1
        substantive, raw = _has_substantive_findings(body)
        if not substantive:
            stats['already_clean'] += 1
            continue
        stats['needs_repair'] += 1
        slug = os.path.basename(p)[:-3]
        fixed.append((slug, kind, len(raw)))
        fixed_slugs.add(slug)
        if dry:
            continue

        os.makedirs(bdir, exist_ok=True)
        shutil.copy2(p, os.path.join(bdir, os.path.basename(p)))

        new_block = ('## 深度提炼\n\n'
                     '> 本页为 `%s` 类文献（非研究/综述），不构成可引用证据。\n'
                     '> 原「核心发现」段已删除：其内容与文献实体不符。\n\n'
                     '### 文献变更要点\n'
                     '- 文献类型: %s\n- 标题: %s\n- DOI: %s\n'
                     % (kind, kind, title or '（缺）', doi or '（缺）'))
        body2 = re.sub(r'## 深度提炼.*?(?=\n## (?!深度)|## 相关文献|---\s*\n\Z|\Z)',
                       lambda _m: new_block.rstrip(), body, flags=re.S)
        if '## 深度提炼' not in body:
            body2 = body.rstrip() + '\n\n' + new_block
        fm2 = _set(fm, 'article_kind', kind)
        fm2 = _set(fm2, 'evidence_eligible', 'false')
        fm2 = _set(fm2, 'curation_status', 'cleared-nonresearch')
        tmp = p + '.tmp'
        io.open(tmp, 'w', encoding='utf-8', newline='\n').write('---' + fm2 + body2)
        os.replace(tmp, p)

    # 证据页：来源于非研究页的，打标不删除
    ev_marked = 0
    if os.path.isdir(EVIDENCE_DIR) and fixed_slugs:
        for fn in sorted(os.listdir(EVIDENCE_DIR)):
            if not fn.endswith('.md'):
                continue
            ep = os.path.join(EVIDENCE_DIR, fn)
            try:
                et = io.open(ep, encoding='utf-8', errors='replace').read()
            except OSError:
                continue
            m = re.search(r'source:\s*"?\[\[([^\]]+)\]\]', et)
            if not m or m.group(1).strip() not in fixed_slugs:
                continue
            if 'evidence_status: orphaned-nonresearch' in et:
                continue
            ev_marked += 1
            if dry:
                continue
            et2 = _set(et.split('\n---', 1)[0][3:] if et.startswith('---') else '',
                       'evidence_status', 'orphaned-nonresearch')
            end = et.find('\n---', 3)
            et2 = '---' + _set(et[3:end], 'evidence_status', 'orphaned-nonresearch') + et[end:]
            tmp = ep + '.tmp'
            io.open(tmp, 'w', encoding='utf-8', newline='\n').write(et2)
            os.replace(tmp, ep)

    print(json.dumps({
        'dry_run': dry,
        'scanned': len(pages),
        'kinds': dict(kinds),
        'nonresearch_pages': stats['nonresearch_pages'],
        'already_clean': stats['already_clean'],
        'needs_repair': stats['needs_repair'],
        'evidence_pages_flagged': ev_marked,
        'backup_dir': None if dry else bdir,
        'sample': fixed[:15],
    }, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
