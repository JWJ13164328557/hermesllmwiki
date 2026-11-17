#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""quarantine_orphan_evidence.py — 把「不再被任何概念页引用」的 evidence 对象
移出 evidence/，放进 evidence/_orphan/（默认 dry-run，--apply 才动文件）。

为什么需要这一步
----------------
旧命名方案（<paper-slug>.md）与页面改写/重提炼会留下大量证据对象，它们：
  * 不再出现在任何概念页的「核心发现」里；
  * 却仍然计入 index.md 的 "Evidence Objects" 总数、出现在 Obsidian 图谱里；
  * 让"知识库有多少证据"这个数字长期虚高（实测 11070 文件 / 6803 活跃）。

安全约束（三条，缺一不可）
--------------------------
1. **有入链的绝不移动**：knowledge base 的不变量是 0 broken links，所以先扫全库
   的 [[...]] 引用，任何被引用的对象都留在原地。
2. **只移动，不删除**：目标目录 evidence/_orphan/，并写 JSON 清单记录
   (文件名 → 原标题/DOI/source)，可一条命令原样搬回。
3. **默认 dry-run**：不带 --apply 时只打印统计。

用法
----
    python3 quarantine_orphan_evidence.py                    # 预览
    python3 quarantine_orphan_evidence.py --apply            # 执行
    python3 quarantine_orphan_evidence.py --restore          # 全部搬回
"""
import argparse
import json
import os
import re
import shutil
import sys

from kb_paths import BASE

EVIDENCE_DIR = os.path.join(BASE, 'evidence')
ORPHAN_DIR = os.path.join(EVIDENCE_DIR, '_orphan')
MANIFEST = os.path.join(BASE, '.pipeline_state', 'orphan_manifest.json')
SKIP_DIRS = {'.git', '.obsidian', 'archive', 'tmp', 'raw', 'mnt', 'scripts',
             'queries', 'logs', '.pipeline_state', '_review'}


def load_orphans(path):
    if not os.path.exists(path):
        raise SystemExit('缺少孤儿清单：%s（先用 batch_evidence_objects.py '
                         '--report-orphans 生成）' % path)
    out = []
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            if line.startswith('- '):
                out.append(line[2:].strip())
    return out


def inbound_links(orphan_ids):
    """扫描全库（跳过 evidence/ 自身）找出对孤儿对象的外部引用。"""
    targets = set(orphan_ids)
    hits = {}
    link_re = re.compile(r'\[\[([^\]\|#]+)')
    for root, dirs, files in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        if os.path.abspath(root).startswith(EVIDENCE_DIR):
            continue
        for name in files:
            if not name.endswith('.md'):
                continue
            path = os.path.join(root, name)
            try:
                with open(path, encoding='utf-8', errors='replace') as f:
                    text = f.read()
            except OSError:
                continue
            for m in link_re.finditer(text):
                key = m.group(1).strip()
                if key in targets:
                    hits.setdefault(key, []).append(os.path.relpath(path, BASE))
    return hits


def snapshot(path):
    try:
        with open(path, encoding='utf-8', errors='replace') as f:
            head = f.read(500)
    except OSError:
        head = ''
    def grab(key):
        m = re.search(r'^%s:\s*"?([^"\n]*)"?' % key, head, re.M)
        return m.group(1).strip() if m else ''
    return {'source': grab('source'), 'doi': grab('doi')}


def do_apply(orphans, hits):
    movable = [o for o in orphans if o not in hits]
    os.makedirs(ORPHAN_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(MANIFEST), exist_ok=True)
    manifest = {}
    if os.path.exists(MANIFEST):
        try:
            with open(MANIFEST, encoding='utf-8') as f:
                manifest = json.load(f)
        except ValueError:
            manifest = {}
    moved = missing = 0
    for ev in movable:
        src = os.path.join(EVIDENCE_DIR, ev + '.md')
        if not os.path.exists(src):
            missing += 1
            continue
        manifest[ev] = dict(snapshot(src), moved_to='evidence/_orphan/' + ev + '.md')
        shutil.move(src, os.path.join(ORPHAN_DIR, ev + '.md'))
        moved += 1
    with open(MANIFEST, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write('\n')
    return moved, missing, len(orphans) - len(movable)


def do_restore():
    if not os.path.exists(MANIFEST):
        raise SystemExit('没有清单，无法恢复：%s' % MANIFEST)
    with open(MANIFEST, encoding='utf-8') as f:
        manifest = json.load(f)
    back = 0
    for ev in manifest:
        src = os.path.join(ORPHAN_DIR, ev + '.md')
        dst = os.path.join(EVIDENCE_DIR, ev + '.md')
        if os.path.exists(src):
            shutil.move(src, dst)
            back += 1
    os.remove(MANIFEST)
    return back


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--orphan-list',
                    default=os.path.join(BASE, '_review', 'orphan_evidence.txt'))
    ap.add_argument('--apply', action='store_true', help='真正移动文件')
    ap.add_argument('--restore', action='store_true', help='按清单全部搬回')
    args = ap.parse_args()

    if args.restore:
        n = do_restore()
        print('已恢复 %d 个 evidence 对象到 evidence/' % n)
        return 0

    orphans = load_orphans(args.orphan_list)
    print('孤儿对象: %d' % len(orphans))
    hits = inbound_links(orphans)
    print('其中被全库其他页面引用: %d（保持原地，避免断链）' % len(hits))
    movable = len(orphans) - len(hits)
    print('可安全隔离: %d' % movable)
    if not args.apply:
        print('\n[dry-run] 未移动任何文件。加 --apply 执行。')
        return 0
    moved, missing, kept = do_apply(orphans, hits)
    print('\n已移入 evidence/_orphan/: %d（缺失 %d，保留原地 %d）'
          % (moved, missing, kept))
    print('清单: %s（--restore 可原样搬回）' % MANIFEST)
    return 0


if __name__ == '__main__':
    sys.exit(main())
