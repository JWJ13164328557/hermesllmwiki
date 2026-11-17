# -*- coding: utf-8 -*-
"""quarantine_offtopic_pages.py - 主题越界页回抓（2026-11-03 第 9 轮）

背景
----
pipeline_selfcheck.today_pages_scope 判定"当日越界"依赖两条:
  A. organism_scope.import_decision(...)[0] == 'drop'    (研究对象非植物)
  B. topic_gate.is_core_topic(...) == False               (研究对象是植物, 但问题不属于八主题)

旧 quarantine_nonplant_pages.py 只覆盖 A 且只认 A-nonplant 硬判据,
B(主题越界)与 A 的软判据都没有回抓动作. 因此自检长期 FAIL.

本脚本按**与自检完全一致**的判据扫描概念页, 命中即隔离(移动, 不删除):
  * 概念页 -> _review/archive/topic_<date>/papers/
  * 对应 evidence -> _review/archive/topic_<date>/evidence/
  * 审计 -> _review/topic_quarantine_<date>.tsv

设计约束
--------
1. 判据单一来源: 直接 import organism_scope / topic_gate, 不再复制正则,
   避免"脚本判 A、自检判 B"的二次漂移.
2. 移动而非删除: 目录结构保持, 可整目录回滚.
3. 默认干跑; --apply 才写盘.
4. 不触碰历史页: 默认只扫 --date(缺省今天)创建的页; --all 需显式给出.
5. 证据先移后移页: 若证据移动失败则整篇跳过, 保证不留"有页无据"或
   "有据无页"的半状态.

用法
----
    python3 scripts/quarantine_offtopic_pages.py --date 2026-11-03            # 干跑
    python3 scripts/quarantine_offtopic_pages.py --date 2026-11-03 --apply    # 执行
    python3 scripts/quarantine_offtopic_pages.py --all --dry-run --limit 50
"""
import argparse
import datetime as _dt
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb_paths import BASE

CONCEPTS_DIR = os.path.join(BASE, 'concepts', 'papers')
EVIDENCE_DIR = os.path.join(BASE, 'evidence')
REVIEW_DIR = os.path.join(BASE, '_review')
CREATED_RE = re.compile(r'^created:\s*"?(\d{4}-\d{2}-\d{2})', re.M)


def _read(path):
    try:
        with open(path, encoding='utf-8', errors='ignore') as fh:
            return fh.read()
    except OSError:
        return ''


def _created(path):
    head = _read(path)[:2000]
    m = CREATED_RE.search(head)
    return m.group(1) if m else None


def pages_on(day):
    if not os.path.isdir(CONCEPTS_DIR):
        return []
    out = []
    for fn in sorted(os.listdir(CONCEPTS_DIR)):
        if fn.endswith('.md'):
            p = os.path.join(CONCEPTS_DIR, fn)
            if _created(p) == day:
                out.append(p)
    return out


def judge(path):
    """与 pipeline_selfcheck.today_pages_scope 同一判据。返回 (bad, detail)。"""
    import organism_scope as OS
    from topic_gate import is_core_topic

    text = _read(path)
    f = OS.page_fields(text)
    org = OS.import_decision(f['title'], f['abstract'], f['journal'],
                             f['species'], f['themes'], f['tags'])[0]
    topic_ok, why = is_core_topic(f['title'], f['abstract'], f['journal'])
    if org == 'drop':
        return True, 'organism=drop'
    if not topic_ok:
        return True, 'topic=%s' % (why or 'off-topic')
    return False, ''


# evidence 的 source 字段形如  source: "[[10-1146-annurev-arplant-042817]]"
def evidence_index():
    idx = {}
    if not os.path.isdir(EVIDENCE_DIR):
        return idx
    for fn in sorted(os.listdir(EVIDENCE_DIR)):
        if not fn.endswith('.md'):
            continue
        head = _read(os.path.join(EVIDENCE_DIR, fn))[:1200]
        m = re.search(r'^source:\s*"?\[\[([^\]\|#]+)', head, re.M)
        if m:
            idx.setdefault(m.group(1).strip().split('/')[-1], []).append(fn)
    return idx


def _stem(path):
    return os.path.basename(path)[:-3]


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--date', default=None)
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--limit', type=int, default=0)
    args = ap.parse_args(argv)
    day = args.date or _dt.date.today().isoformat()

    if args.all:
        pages = [os.path.join(CONCEPTS_DIR, fn)
                 for fn in sorted(os.listdir(CONCEPTS_DIR)) if fn.endswith('.md')]
    else:
        pages = pages_on(day)
    if args.limit:
        pages = pages[:args.limit]

    print('检查范围: %s (%d 页)' % ('全库' if args.all else day, len(pages)))
    ev_idx = evidence_index()
    rows = []
    for p in pages:
        try:
            bad, detail = judge(p)
        except Exception as exc:
            print('  !! %s: %s' % (os.path.basename(p), exc))
            continue
        if not bad:
            continue
        stem = _stem(p)
        evs = ev_idx.get(stem, [])
        rows.append(dict(page=os.path.basename(p), stem=stem, detail=detail,
                         n_ev=len(evs), evs=evs))

    print('命中越界: %d 页 (证据 %d 条)'
          % (len(rows), sum(r['n_ev'] for r in rows)))
    for r in rows[:80]:
        print('  %-58s %-40s ev=%d' % (r['page'], r['detail'], r['n_ev']))
    if len(rows) > 80:
        print('  ... 其余 %d 条见 TSV' % (len(rows) - 80))

    os.makedirs(REVIEW_DIR, exist_ok=True)
    tsv = os.path.join(REVIEW_DIR, 'topic_quarantine_%s.tsv' % day)
    with open(tsv, 'w', encoding='utf-8') as fh:
        fh.write('page\tdetail\tn_evidence\tstem\n')
        for r in rows:
            fh.write('%s\t%s\t%d\t%s\n'
                     % (r['page'], r['detail'], r['n_ev'], r['stem']))
    print('清单: %s' % tsv)

    if not args.apply:
        print('干跑: 加 --apply 才移动文件.')
        return 0
    if not rows:
        return 0

    arch = os.path.join(REVIEW_DIR, 'archive', 'topic_%s' % day)
    pdir = os.path.join(arch, 'papers')
    edir = os.path.join(arch, 'evidence')
    os.makedirs(pdir, exist_ok=True)
    os.makedirs(edir, exist_ok=True)

    moved_p = moved_e = skipped = 0
    for r in rows:
        src_p = os.path.join(CONCEPTS_DIR, r['page'])
        if not os.path.exists(src_p):
            continue
        ok = True
        for fn in r['evs']:
            src_e = os.path.join(EVIDENCE_DIR, fn)
            try:
                if os.path.exists(src_e):
                    shutil.move(src_e, os.path.join(edir, fn))
                    moved_e += 1
            except OSError as exc:
                print('  !! 证据移动失败 %s: %s' % (fn, exc))
                ok = False
                break
        if not ok:
            skipped += 1
            continue
        try:
            shutil.move(src_p, os.path.join(pdir, r['page']))
            moved_p += 1
        except OSError as exc:
            print('  !! 页面移动失败 %s: %s' % (r['page'], exc))
            skipped += 1
    print('已隔离: 概念页 %d, 证据 %d, 跳过 %d -> %s'
          % (moved_p, moved_e, skipped, arch))
    return 0


if __name__ == '__main__':
    sys.exit(main())
