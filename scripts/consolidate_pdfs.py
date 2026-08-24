#!/usr/bin/env python3
"""
知识库 raw/papers/ PDF 结构整理 (2026-08-24)
==========================================
把散落在多个批次目录的 PDF 按 DOI 去重汇总到 raw/papers/all_pdfs/，
其余非 PDF 文件保留, 空目录移至 raw/papers/.trash_cleanup/ (可恢复)。

去重策略: 按文件名(DOI)分组, 保留文件字节数最大的副本。
映射文件 (*.json/*.csv) 从原批次目录集中到 raw/papers/maps/。

用法:
  /usr/bin/python3 -u scripts/consolidate_pdfs.py --dry-run   # 预览不执行
  /usr/bin/python3 -u scripts/consolidate_pdfs.py             # 执行
"""
import os, re, sys, shutil, argparse
from collections import defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPERS = f'{BASE}/raw/papers'
ALL = f'{PAPERS}/all_pdfs'
MAPS = f'{PAPERS}/maps'
TRASH = f'{PAPERS}/.trash_cleanup'
# 顶层直接处理的批次子目录 (不递归 nested)
BATCH_DIRS = ['dPDF', 'fill_missing', 'metabolism', 'new_batch_20260530',
              'openalex_batch', 'scihub_batch', 'scihub_v3', 'selenium_batch']
# 保留在原地/集中的映射文件扩展名
MAP_EXTS = ('.json', '.csv')

def plan():
    """返回 (pdf_moves, map_moves, empties)."""
    # 收集所有 PDF: name -> [(src_path, size)]
    pdfs = defaultdict(list)
    for bd in BATCH_DIRS:
        d = os.path.join(PAPERS, bd)
        if not os.path.isdir(d):
            continue
        for f in os.listdir(d):
            fp = os.path.join(d, f)
            if os.path.isfile(fp) and f.lower().endswith('.pdf'):
                pdfs[f].append((fp, os.path.getsize(fp)))
    # root 目录的 PDF (raw/papers/*.pdf)
    for f in os.listdir(PAPERS):
        fp = os.path.join(PAPERS, f)
        if os.path.isfile(fp) and f.lower().endswith('.pdf'):
            pdfs[f].append((fp, os.path.getsize(fp)))

    # 去重: 每文件名保留最大
    pdf_moves = []  # (keep_src, dest, dropped_count)
    for f, copies in pdfs.items():
        keep = max(copies, key=lambda x: x[1])
        dest = os.path.join(ALL, f)
        pdf_moves.append((keep[0], dest, len(copies) - 1))

    # 映射文件集中
    map_moves = []
    for bd in BATCH_DIRS:
        d = os.path.join(PAPERS, bd)
        if not os.path.isdir(d):
            continue
        for f in os.listdir(d):
            if f.lower().endswith(MAP_EXTS):
                map_moves.append((os.path.join(d, f), os.path.join(MAPS, f)))

    # 空目录(移动后无 pdf/映射 = 空壳)
    empties = []
    for bd in BATCH_DIRS:
        d = os.path.join(PAPERS, bd)
        if not os.path.isdir(d):
            continue
        remaining = [x for x in os.listdir(d)]
        if not remaining:
            empties.append(d)
    return pdf_moves, map_moves, empties

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    pdf_moves, map_moves, empties = plan()
    total_pdf = len(pdf_moves)
    total_files = sum(c[2] for c in pdf_moves)
    print(f'PDF 汇总: {total_pdf} 唯一文件 (丢弃冗余副本 {total_files} 个)')
    print(f'映射文件集中: {len(map_moves)}')
    print(f'空目录待清: {len(empties)} -> {empties}')

    if args.dry_run:
        print('\n[dry-run] 仅预览, 不执行. 示例移动:')
        for src, dest, dropped in pdf_moves[:5]:
            print(f'  MOVE {src} -> {dest} (丢{dropped})')
        return

    for src, dest, _ in pdf_moves:
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        if os.path.abspath(src) != os.path.abspath(dest):
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            shutil.move(src, dest)

    for src, dest in map_moves:
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.move(src, dest)

    # 移空目录到 .trash
    if empties:
        os.makedirs(TRASH, exist_ok=True)
        for d in empties:
            if not os.listdir(d):  # 确认真空
                shutil.move(d, os.path.join(TRASH, os.path.basename(d)))
                print(f'  → 移空目录到 .trash: {d}')

    print(f'\n完成: {total_pdf} PDF 汇总到 {ALL}, 映射文件到 {MAPS}')

if __name__ == '__main__':
    main()
