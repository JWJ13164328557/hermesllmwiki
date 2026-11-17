# -*- coding: utf-8 -*-
"""claim_role 判别力审计。

问题：17386/18239（95.3%）的证据被标成 finding，claim_role 实际没有分层能力。
本脚本回答：这些 finding 里，有多少其实是**目的/推测/展望/教科书背景/定义/方法**？
做法与 audit_evidence_discrimination 一致，不循环论证：
  1. 上界探针：用"非发现信号"家族扫描 finding 池，得到漏判**上界**；
  2. 强发现信号反证：句子里同时有明确结果标记（we found / results show /
     directly binds / significantly）的，不算漏判；
  3. 抽样裁定：命中候选与随机对照写入 TSV，供人工/模型裁定。

用法：
  python scripts/audit_claim_role.py                  # 统计 + 抽样
  python scripts/audit_claim_role.py --sample 60
  python scripts/audit_claim_role.py --json /tmp/r.json
"""
import argparse
import glob
import io
import json
import os
import random
import re
import sys

BASE = os.environ.get('KB_BASE', '/mnt/g/hermes_obsidian/hermes')
EV = os.path.join(BASE, 'evidence')
TODAY = '20261104'

# 强发现信号：出现即认定"这是一条结果"，不再算漏判。
# 2026-11-04：这里原本自带一份 PROBES/STRONG_FINDING 正则副本。副本与规则本体
# 一定会漂移——实测 "The results demonstrate that …" 在规则里属强结果句，
# 在副本里不属，于是它被当成"漏判"进了抽样池，把上界算虚高。审计必须用被审计
# 对象自己的尺子，所以直接 import 规则家族。
import batch_evidence_objects as _be

STRONG_FINDING = _be._ROLE_STRONG_FINDING
PROBES = {}
for _kind, _rx in _be._NONFINDING_ORDER:
    PROBES.setdefault(_kind, _rx)


def load_claims():
    out = []
    for p in glob.glob(os.path.join(EV, '*.md')):
        try:
            txt = io.open(p, encoding='utf-8', errors='ignore').read()
        except OSError:
            continue
        m = re.search(r'^claim_role:\s*"?(\w+)"?', txt, re.M)
        role = m.group(1) if m else ''
        if role != 'finding':
            continue
        i = txt.find('## Claim')
        if i < 0:
            continue
        body = txt[i + 9:]
        j = body.find('## ')
        claim = (body[:j] if j > 0 else body).strip()
        claim = re.sub(r'\s+', ' ', claim)
        if not claim:
            continue
        doi = re.search(r'^doi:\s*"?\s*(10\.\d{4,}/[^\s\n"]+)', txt, re.M)
        out.append({'file': os.path.basename(p), 'claim': claim,
                    'doi': doi.group(1) if doi else ''})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--sample', type=int, default=40)
    ap.add_argument('--json', default='')
    # 2026-11-04：抽样文件是"人工裁定过的地面真值"，默认路径每天固定，
    # 重跑一次就把前一版裁定覆盖掉（本轮就发生过）。默认改为不覆盖：
    # 目标文件已存在且未显式 --sample-out 时，追加序号。
    ap.add_argument('--sample-out', default='')
    args = ap.parse_args()

    rows = load_claims()
    total = len(rows)
    fam = {}
    cand = []
    for r in rows:
        t = r['claim']
        hits = [k for k, rx in PROBES.items() if rx.search(t)]
        if not hits:
            continue
        for k in hits:
            fam[k] = fam.get(k, 0) + 1
        strong = bool(STRONG_FINDING.search(t))
        r['families'] = hits
        r['strong'] = strong
        if not strong:
            cand.append(r)

    share = 100.0 * len(cand) / max(1, total)
    print(json.dumps({
        'finding_total': total,
        'probe_hit': sum(1 for r in rows if PROBES and any(
            rx.search(r['claim']) for rx in PROBES.values())),
        'upper_bound_mislabel': len(cand),
        'upper_bound_share_pct': round(share, 2),
        'family_hits': dict(sorted(fam.items(), key=lambda x: -x[1])),
    }, ensure_ascii=False, indent=1))

    random.seed(20261104)
    pick = random.sample(cand, min(args.sample, len(cand)))
    ctrl = random.sample([r for r in rows if r not in cand], min(10, total))
    outdir = os.path.join(BASE, '_review')
    os.makedirs(outdir, exist_ok=True)
    if args.sample_out:
        path = args.sample_out
    else:
        base = os.path.join(outdir, 'claim_role_sample_%s.tsv' % TODAY)
        path, k = base, 2
        while os.path.exists(path):
            path = base[:-4] + '_r%d.tsv' % k
            k += 1
    with io.open(path, 'w', encoding='utf-8') as fh:
        fh.write('group\tlabel\tfamilies\tsuggested\tclaim\tsource\n')
        for r in pick:
            fh.write('probe\t\t%s\t\t%s\t%s\n' % (
                ','.join(r['families']), r['claim'][:400], r['file']))
        for r in ctrl:
            fh.write('control\t\t\t\t%s\t%s\n' % (r['claim'][:400], r['file']))
    print('sample_file', path)

    if args.json:
        with io.open(args.json, 'w', encoding='utf-8') as fh:
            json.dump({'upper_bound': len(cand), 'total': total}, fh)


if __name__ == '__main__':
    main()
