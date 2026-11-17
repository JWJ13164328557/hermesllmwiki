#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""repair_nonplant_import.py — 回抓导入层的非植物坏数据（2026-11-02）

问题
----
领域纯度闸门是第 24 轮才接到证据导入层的（batch_evidence_objects.py）。
在此之前入库的论文，其证据对象仍留在 evidence/ 里：它们不进综述、不进假说
（主题层已过滤），但会让
  * 孤儿证据统计虚高（本来"不该存在"的对象被算作"没人引用"）
  * 人工浏览 KB 时看到肉鸡/结肠炎/4D 打印的断言
  * 实体页与关系表继续携带这些断言衍生的实体

处理原则
--------
1. 只处理"论文级判定为 nonplant 且方法不可迁移"的 DOI（drop 类）。
   method 类（概念页 themes 含 methods-tools）保留 —— 方法可迁移是设计内的例外。
2. 证据对象 → 移入 _review/archive/nonplant_<date>/evidence/，文件名不变。
3. 概念页 → 不移动（避免一次性打断大量链接），改为打标：
   frontmatter 增 scope_status: excluded-nonplant / excluded_reason，正文顶部加横幅。
4. 移动后必须按序执行（否则 relationships/ 与 synthesis/ 会留死链）：
      python3 scripts/fix_dangling_links.py --apply
      python3 scripts/batch_synthesis.py && python3 scripts/batch_hypotheses.py

性能
----
概念页索引一次性构建（DOI -> 路径）。早期实现把线性扫描放在循环里，
256 条证据 × 6889 个概念页 ⇒ 干跑 3 分钟仍未结束，属于必须避免的模式。

用法
----
    python3 scripts/repair_nonplant_import.py                # dry-run（默认）
    python3 scripts/repair_nonplant_import.py --apply
    python3 scripts/repair_nonplant_import.py --apply --limit 20   # 先小批试跑
"""
import argparse
import datetime as _dt
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb_paths import BASE
from organism_scope import paper_scope_table

EVIDENCE_DIR = os.path.join(BASE, 'evidence')
CONCEPTS_DIR = os.path.join(BASE, 'concepts', 'papers')
REVIEW_DIR = os.path.join(BASE, '_review')
DOI_RE = re.compile(r'^doi:\s*"?([^"\n]+?)"?\s*$', re.M)
FM_RE = re.compile(r'^---\n(.*?)\n---\n', re.S)
BANNER = ('> [!warning] 已排除（非植物研究对象）\n'
          '> 本文研究对象为动物/临床/工业体系，其生物学断言不得进入植物学主题。\n'
          '> 保留本页仅为追溯 DOI 与排除理由；证据对象已归档。\n\n')


def yaml_scalar(value, limit=None):
    """把任意文本写成安全的 YAML 双引号标量。

    实测：excluded_reason 里带论文标题（"… heterogeneity: insights from …"），
    未加引号时冒号让 YAML 认为这是嵌套映射，整页 frontmatter 解析失败。
    用 JSON 转义（YAML 是 JSON 的超集）最省事，也不怕引号与换行。
    """
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', ' ', str(value or ''))
    text = re.sub(r'\s+', ' ', text).strip()
    if limit:
        text = text[:limit]
    return json.dumps(text, ensure_ascii=False)

def load_drop_set():
    table = paper_scope_table(CONCEPTS_DIR)
    return {d: r for d, r in table.items()
            if r.get('label') == 'nonplant' and not r.get('method')}


def build_concept_index():
    """DOI(小写) -> 概念页路径。一次性构建，供标记阶段 O(1) 查询。"""
    idx = {}
    for name in os.listdir(CONCEPTS_DIR):
        if not name.endswith('.md'):
            continue
        p = os.path.join(CONCEPTS_DIR, name)
        try:
            head = open(p, encoding='utf-8', errors='replace').read(1500)
        except OSError:
            continue
        m = DOI_RE.search(head)
        if m:
            idx.setdefault(m.group(1).strip().lower(), p)
    return idx


def scan_evidence(drop):
    hits = []
    for name in sorted(os.listdir(EVIDENCE_DIR)):
        if not name.endswith('.md'):
            continue
        path = os.path.join(EVIDENCE_DIR, name)
        try:
            head = open(path, encoding='utf-8', errors='replace').read(2000)
        except OSError:
            continue
        m = DOI_RE.search(head)
        if not m:
            continue
        doi = m.group(1).strip().lower()
        if doi in drop:
            hits.append((name[:-3], doi, path))
    return hits


def stamp_concept(path, reason, apply=False):
    if not path:
        return False
    text = open(path, encoding='utf-8').read()
    if 'scope_status: excluded-nonplant' in text:
        return True
    fm = FM_RE.match(text)
    if not fm:
        return False
    new_fm = (fm.group(1).rstrip('\n')
              + '\nscope_status: excluded-nonplant\nexcluded_reason: '
              + yaml_scalar(reason) + '\n')
    body = text[fm.end():]
    if not body.lstrip().startswith('> [!warning] 已排除'):
        body = BANNER + body.lstrip('\n')
    if apply:
        open(path, 'w', encoding='utf-8').write('---\n' + new_fm + '\n---\n' + body)
    return True


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true', help='真正写盘（默认只报告）')
    ap.add_argument('--limit', type=int, default=0, help='最多处理前 N 条，便于小批试跑')
    ap.add_argument('--date', default=_dt.date.today().strftime('%Y%m%d'))
    args = ap.parse_args(argv)

    drop = load_drop_set()
    hits = scan_evidence(drop)
    if args.limit:
        hits = hits[:args.limit]
    print('drop 类论文: %d 篇；待归档证据对象: %d 条' % (len(drop), len(hits)))
    if not hits:
        print('无需处理。')
        return 0

    cidx = build_concept_index()
    arch = os.path.join(REVIEW_DIR, 'archive', 'nonplant_%s' % args.date, 'evidence')
    manifest = os.path.join(REVIEW_DIR, 'nonplant_import_%s.tsv' % args.date)
    if args.apply:
        os.makedirs(arch, exist_ok=True)

    rows = []
    stamped = set()
    missing = set()
    for ev, doi, path in hits:
        reason = 'nonplant|%s' % (drop[doi].get('title') or '')[:80]
        rows.append((ev, doi, 'archive', reason))
        if args.apply:
            dst = os.path.join(arch, os.path.basename(path))
            if os.path.exists(dst):
                os.remove(dst)
            shutil.move(path, dst)
        if doi in stamped:
            continue
        cpath = cidx.get(doi)
        if stamp_concept(cpath, reason, apply=args.apply):
            stamped.add(doi)
        else:
            missing.add(doi)

    for doi in sorted(missing):
        rows.append(('', doi, 'concept-missing', 'no concept page for doi'))

    print('涉及论文: %d 篇；概念页已标记: %d；缺概念页: %d'
          % (len({d for _, d, _ in hits}), len(stamped), len(missing)))
    if args.apply:
        # 2026-11-02 线上缺陷：同名日期清单用 'w' 覆盖，当日第二次运行
        # （7 篇 / 48 条）把先前 227 条审计记录整段抹掉，事后无法追溯哪批
        # 证据被哪一次运行移走。改为**追加式**并加 run 列（精确到秒），
        # 使同一天多次运行各自成段、互不覆盖。
        run_id = _dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        need_header = not os.path.exists(manifest) or os.path.getsize(manifest) == 0
        with open(manifest, 'a', encoding='utf-8') as fh:
            if need_header:
                fh.write('run\tevidence_id\tdoi\taction\treason\n')
            for r in rows:
                fh.write('\t'.join((run_id,) + tuple(r)) + '\n')
        print('审计清单（追加，run=%s）：%s' % (run_id, manifest))
        print('已归档到: %s' % arch)
        print('\n下一步（必须按序执行，否则留死链）：')
        print('  python3 scripts/fix_dangling_links.py --apply')
        print('  python3 scripts/batch_synthesis.py')
        print('  python3 scripts/batch_hypotheses.py')
    else:
        for ev, doi, _, reason in rows[:15]:
            print('  [dry-run] %-50s %s' % (ev, doi))
        print('  ... 共 %d 条证据（--apply 才写盘）' % len(hits))
    return 0


if __name__ == '__main__':
    sys.exit(main())
