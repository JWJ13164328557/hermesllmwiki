
# -*- coding: utf-8 -*-
"""证据类型判别力审计（rule-v4+）。

目的：回答一个具体问题——被标成 descriptive/observational 的 claim 里，
有多少其实包含可推理的因果/互作/结合陈述？也就是 rule 的**漏判率**。

方法（不循环论证）：
  1. 上界探针：用一组"强因果信号"正则扫描 descriptive 池，得到漏判的**上界**
     （探针只用于筛候选，不直接改判定）。
  2. 抽样裁定：对命中探针的候选与随机对照各抽 N 条，输出到 TSV 供人工/模型裁定。
  3. 汇总：输出命中率、按探针家族的分布，指向具体缺失的谓词家族。

用法：
  python scripts/audit_evidence_discrimination.py                # 统计 + 抽样到 _review/
  python scripts/audit_evidence_discrimination.py --sample 60
  python scripts/audit_evidence_discrimination.py --json /tmp/a.json
"""
import argparse
import io
import json
import os
import random
import re
import sys

BASE = os.environ.get('KB_BASE', '/mnt/g/hermes_obsidian/hermes')
EVIDENCE_DIR = os.path.join(BASE, 'evidence')
TODAY = '20261104'

# 强因果/互作信号家族。每个家族独立统计，避免"命中即算漏判"的粗放结论。
PROBES = {
    # 结合/互作（当前 _V3_INTERACTION_PRED 已覆盖多数，这里只放"易漏"变体）
    'interaction_variant': re.compile(
        r'\b(associates?\s+with|binds?|bounded|complexes?\s+with|'
        r'partner(?:s|ed)?\s+with|co-?purif\w*|co-?sediment\w*|'
        r'competes?\s+with\s+\S+\s+for|displac\w+\s+\S+\s+from)\b', re.I),
    # 翻译后修饰
    'ptm': re.compile(
        r'\b(phosphorylat\w*|dephosphorylat\w*|ubiquitinylat\w*|'
        r'acetyl\w*|sumoylat\w*|glycosylat\w*|nitrosylat\w*|'
        r'kinase\s+activity|phosphatase\s+activity)\b', re.I),
    # 遗传因果（"X 导致 Y"但不写 mutant/CRISPR 字样）
    'causal_verb': re.compile(
        r'\b(caus(?:es|ed|ing)|lead(?:s|ing)?\s+to|led\s+to|result(?:s|ed|ing)?\s+in|'
        r'attribut\w+\s+to|drives?|driven\s+by|is\s+responsible\s+for|'
        r'accounts?\s+for|underlies?|underlie|mediates?|is\s+mediated\s+by)\b', re.I),
    # 必要性/充分性（当前只在 _V3_FUNCTIONAL 认 is required for）
    'necessity': re.compile(
        r'\b(essential\s+for|indispensable\s+for|necessary\s+and\s+sufficient|'
        r'sufficient\s+to|required\s+to\s+maintain|depend(?:s|ent)?\s+on|'
        r'relies?\s+on|relied\s+on)\b', re.I),
    # 扰动（用词不在当前名词表里）
    'perturb_variant': re.compile(
        r'\b(perturb\w*|ablat\w*|deplet\w*|depletion|repress\w+\s+by\s+dCas|'
        r'crisp\w*|base\s+editing|prime\s+editing|talen|zfn|'
        r'dominant[- ]negative|amiRNA|artificial\s+microRNA|'
        r'conditional\s+knockout|inducible\s+\w+\s+line)\b', re.I),
    # 直接调控（不写 promoter）
    'direct_regulation': re.compile(
        r'\b(directly\s+(?:up|down)-?regulat\w*|directly\s+target\w*|'
        r'is\s+a\s+direct\s+target|direct\s+transcriptional\s+target|'
        r'recruits?\s+\w+\s+to\s+the\s+\w+|'
        r'chromatin\s+(?:looping|accessibility)\s+\w*)\b', re.I),
    # 定量因果效应（"elevated/reduced X in Y" 但无 mutant 词）
    'quant_effect': re.compile(
        r'\b(elevat\w+|augment\w+|diminish\w+|attenuat\w+|'
        r'impair\w+|abolish\w+|restor\w+|rescue[sd]?|'
        r'\d+(?:\.\d+)?\s*-?\s*fold)\b', re.I),
}

# 明确"不是发现"的信号——用于排除假阳性候选（背景/方法/展望）
NON_FINDING = re.compile(
    r'\b(we\s+(?:used|performed|conducted|carried\s+out)|'
    r'were\s+(?:analy[sz]ed|measured|collected|extracted|purified|incubated)|'
    r'according\s+to\s+the\s+manufacturer|sds-?page|coomassie|'
    r'is\s+critical\s+to|remains?\s+(?:unclear|unknown|elusive)|'
    r'future\s+(?:studies|work)|little\s+is\s+known|'
    r'has\s+(?:long\s+)?been\s+(?:recognized|known)|'
    r'we\s+(?:hypothesi[sz]e|propose\s+to))\b', re.I)


def _iter(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames.sort()
        if '_orphan' in dirpath:
            continue
        for fn in sorted(filenames):
            if fn.endswith('.md'):
                yield os.path.join(dirpath, fn)


def load():
    rows = []
    for path in _iter(EVIDENCE_DIR):
        try:
            text = io.open(path, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        m = re.search(r'^evidence_type:\s*"?([^"\n]+)"?', text, re.M)
        etype = (m.group(1).strip() if m else '') or '未标注'
        cm = re.search(r'^## Claim\s*\n(.+?)(?=\n## |\Z)', text, re.M | re.S)
        claim = re.sub(r'\s+', ' ', cm.group(1)).strip() if cm else ''
        dm = re.search(r'^doi:\s*"?\s*(10\.\d{4,}/[^\s\n"]+)', text, re.M)
        rows.append({'path': path, 'type': etype, 'claim': claim,
                     'doi': dm.group(1).rstrip('/.') if dm else ''})
    return rows


def probe_hits(claim):
    return [name for name, rx in PROBES.items() if rx.search(claim)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--sample', type=int, default=60)
    ap.add_argument('--seed', type=int, default=20261104)
    ap.add_argument('--json', default='')
    ap.add_argument('--outdir', default=os.path.join(BASE, '_review'))
    args = ap.parse_args()

    rows = load()
    desc = [r for r in rows if r['type'] == 'descriptive/observational']
    total = len(rows)

    fam = {k: 0 for k in PROBES}
    any_hit = 0
    hit_not_finding = 0
    candidates = []
    for r in desc:
        c = r['claim']
        if not c:
            continue
        hits = probe_hits(c)
        if not hits:
            continue
        for h in hits:
            fam[h] += 1
        any_hit += 1
        if NON_FINDING.search(c):
            hit_not_finding += 1
            continue
        candidates.append(dict(r, probes=','.join(hits)))

    stats = {
        'total_evidence': total,
        'descriptive': len(desc),
        'descriptive_share': round(len(desc) / max(total, 1), 4),
        'probe_any_hit': any_hit,
        'probe_any_hit_share_of_descriptive': round(any_hit / max(len(desc), 1), 4),
        'probe_hit_but_non_finding': hit_not_finding,
        'upper_bound_mislabel': any_hit - hit_not_finding,
        'upper_bound_share_of_total': round((any_hit - hit_not_finding) / max(total, 1), 4),
        'family_hits': fam,
    }

    rnd = random.Random(args.seed)
    cand = candidates[:]
    rnd.shuffle(cand)
    picked = cand[:args.sample]
    ctrl_pool = [r for r in desc if r['claim'] and not probe_hits(r['claim'])]
    rnd.shuffle(ctrl_pool)
    ctrl = ctrl_pool[:max(10, args.sample // 3)]

    os.makedirs(args.outdir, exist_ok=True)
    out = os.path.join(args.outdir, 'discrimination_sample_%s.tsv' % TODAY)
    with io.open(out, 'w', encoding='utf-8', newline='\n') as f:
        f.write('arm\tprobes\tevidence_type\tdoi\tpath\tclaim\tverdict\n')
        for r in picked:
            f.write('probe\t%s\t%s\t%s\t%s\t%s\t\n' % (
                r['probes'], r['type'], r['doi'], r['path'], r['claim'][:500]))
        for r in ctrl:
            f.write('control\t-\t%s\t%s\t%s\t%s\t\n' % (
                r['type'], r['doi'], r['path'], r['claim'][:500]))

    stats['sample_file'] = out
    stats['sampled_probe'] = len(picked)
    stats['sampled_control'] = len(ctrl)
    print(json.dumps(stats, ensure_ascii=False, indent=1))
    if args.json:
        io.open(args.json, 'w', encoding='utf-8').write(
            json.dumps(stats, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
