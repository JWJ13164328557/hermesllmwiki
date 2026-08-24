#!/bin/bash
# 全量补齐缺失 PDF — 第二轮 (2026-08-24) 输出到 all_pdfs/
# 复用 fill_missing_pdfs.py, Sci-Hub 默认开, 断点续传由 all_pdfs 已有 PDF 保证
BASE=/mnt/g/hermes_obsidian/hermes
cd "$BASE"

BATCH=400
START=$(date +%H:%M:%S)
echo "=== 全量补齐(轮2, 缺失2658)开始 $(date) ===" | tee -a /tmp/fill_all2.log

for ((off=0; off<=2600; off+=BATCH)); do
  stamp=$(date +%H:%M:%S)
  echo "[$stamp] === 批次 offset=$off (limit=$BATCH) ===" | tee -a /tmp/fill_all2.log
  /usr/bin/python3 -u scripts/fill_missing_pdfs.py \
      --from-file missing_dois.txt \
      --offset "$off" --limit "$BATCH" \
      --workers 4 --scihub --skip-deep \
      --outdir raw/papers/all_pdfs 2>&1 | tee -a /tmp/fill_all2.log
  done_pdf=$(ls raw/papers/all_pdfs/*.pdf 2>/dev/null | wc -l)
  echo "[$(date +%H:%M:%S)] 批次完成, 累计 all_pdfs PDF: $done_pdf" | tee -a /tmp/fill_all2.log
done

echo "=== 全量补齐(轮2)完成 $(date), 总耗时 $(( $(date +%s) - $(date -d "$START" +%s) ))s ===" | tee -a /tmp/fill_all2.log
