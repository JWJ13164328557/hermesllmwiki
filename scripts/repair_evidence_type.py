#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""repair_evidence_type.py — 证据语义类型回填与纠偏。

背景（2026-11-03）
------------------
旧分类器把无法识别的 claim 一律写成 expression/regulation，导致 85% 的
证据都是同一类型，下游无法区分表达相关、遗传因果、物理互作、表型关联
与组学共现。本脚本只做两件事：

1. 缺失 evidence_type 的证据：按 claim 关键词保守回填；
2. 明确标为 keyword-heuristic 的旧证据：重新分类，允许从
   expression/regulation 降级为 descriptive/observational，或升级为
   更强的 genetic perturbation / protein interaction / DNA binding。

不做的事：不改 claim，不改 DOI，不删除证据，不把启发式标签伪装成人工结论。

用法：
  python3 scripts/repair_evidence_type.py --dry-run
  python3 scripts/repair_evidence_type.py --apply
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import batch_evidence_objects as be  # noqa: E402

FM = re.compile(r'^---\n(.*?)\n---\n', re.S)
FIELD = re.compile(r'^evidence_type:\s*"?(.*?)"?\s*$', re.M)
BASIS = re.compile(r'^quality_basis:\s*"?(.*?)"?\s*$', re.M)


def claim_of(text):
    m = re.search(r'^## Claim\s*\n(.+?)(?=\n## |\Z)', text, re.S | re.M)
    return re.sub(r'\s+', ' ', m.group(1)).strip() if m else ''


def current_type(front):
    m = FIELD.search(front)
    return (m.group(1).strip() if m else '')


def replace_or_insert(front, key, value):
    pat = re.compile(r'^%s:.*$' % re.escape(key), re.M)
    if pat.search(front):
        return pat.sub('%s: "%s"' % (key, value), front, count=1)
    # 插在 quality_basis 之后，保持 YAML 可读
    q = re.search(r'^quality_basis:.*$', front, re.M)
    if q:
        return front[:q.end()] + '\n%s: "%s"' % (key, value) + front[q.end():]
    return front + '\n%s: "%s"' % (key, value)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--evidence-dir', default='/mnt/g/hermes_obsidian/hermes/evidence')
    ap.add_argument('--out', default='/mnt/g/hermes_obsidian/hermes/_review/evidence_type_backfill.json')
    args = ap.parse_args()
    if args.apply and args.dry_run:
        raise SystemExit('choose --apply or --dry-run, not both')
    apply = args.apply
    root = Path(args.evidence_dir)
    before = collections.Counter()
    after = collections.Counter()
    changed = []
    missing = 0
    for f in sorted(root.glob('*.md')):
        try:
            text = f.read_text(encoding='utf-8', errors='replace')
        except OSError:
            continue
        m = FM.match(text)
        if not m:
            continue
        front = m.group(1)
        old = current_type(front)
        before[old or '(empty)'] += 1
        if not old:
            missing += 1
        claim = claim_of(text)
        new, quality = be.classify(claim)
        basis = BASIS.search(front)
        auto = bool(basis and 'keyword-heuristic' in basis.group(1))
        # 只回填空值，或纠偏明确为关键词启发式的旧默认值。
        if old and not (auto and old == 'expression/regulation'):
            after[old] += 1
            continue
        if old and new == old:
            after[old] += 1
            continue
        # 保守纠偏：旧默认值只在能识别出更强证据设计时改写。
        # 识别不出的 claim 保持原标签，避免把 4000+ 条证据一次性降级为
        # descriptive/observational 而丢失已有的分诊信息。
        if old == 'expression/regulation' and new == 'descriptive/observational':
            after[old] += 1
            continue
        changed.append({'file': f.name, 'old': old or '(empty)',
                        'new': new, 'quality': quality, 'claim': claim[:220]})
        after[new] += 1
        if not apply:
            continue
        front = replace_or_insert(front, 'evidence_type', new)
        front = replace_or_insert(front, 'evidence_type_basis', 'keyword-heuristic')
        front = replace_or_insert(front, 'evidence_type_confidence', quality)
        new_text = FM.sub('---\n%s\n---\n' % front, text, count=1)
        new_text = re.sub(r'^- 证据类型:.*$', '- 证据类型: %s' % new, new_text, count=1, flags=re.M)
        f.write_text(new_text, encoding='utf-8', newline='\n')
    report = {'mode': 'apply' if apply else 'dry-run', 'total': sum(before.values()),
              'missing_before': missing, 'changed': len(changed),
              'before': dict(before), 'after': dict(after),
              'samples': changed[:30]}
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({k: report[k] for k in ('mode', 'total', 'missing_before', 'changed')}, ensure_ascii=False))
    print('before', dict(before))
    print('after ', dict(after))
    print('report', out)


if __name__ == '__main__':
    main()
