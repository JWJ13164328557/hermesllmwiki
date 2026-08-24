#!/bin/bash
# OA 论文补齐 — 免费通道批量下载 (2026-08-24, Sci-Hub 已失效)
# 对 missing_pdfs_OA.txt (1911 篇 OA) 用免费 4 通道下载到 all_pdfs/
BASE=/mnt/g/hermes_obsidian/hermes
cd "$BASE"

BATCH=400
START=$(date +%H:%M:%S)
echo "=== OA 补齐(1911篇,免费通道)开始 $(date) ===" | tee -a /tmp/fill_oa.log

for ((off=0; off<=1600; off+=BATCH)); do
  stamp=$(date +%H:%M:%S)
  echo "[$stamp] === 批次 offset=$off (limit=$BATCH) ===" | tee -a /tmp/fill_oa.log
  /usr/bin/python3 -u scripts/fill_missing_pdfs.py \
      --from-file missing_pdfs_OA.txt \
      --offset "$off" --limit "$BATCH" \
      --workers 8 --no-scihub --skip-deep \
      --outdir raw/papers/all_pdfs 2>&1 | tee -a /tmp/fill_oa.log
  done_pdf=$(ls raw/papers/all_pdfs/*.pdf 2>/dev/null | wc -l)
  echo "[$(date +%H:%M:%S)] 批次完成, 累计 all_pdfs PDF: $done_pdf" | tee -a /tmp/fill_oa.log
done

echo "=== OA 补齐完成 $(date), 总耗时 $(( $(date +%s) - $(date -d "$START" +%s) ))s ===" | tee -a /tmp/fill_oa.log
