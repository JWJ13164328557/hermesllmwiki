#!/bin/bash
# 全量补齐缺失 PDF — 逐批串行推进 (2026-08-24)
# 每批 400 篇, 含 Sci-Hub 兜底, 断点续传由 outdir 已有 PDF 保证
# 用法: bash scripts/fill_all_batches.sh
BASE=/mnt/g/hermes_obsidian/hermes
cd "$BASE"

BATCH=400
OFFSET=400   # batch1 已处理前 400
START=$(date +%H:%M:%S)
echo "=== 全量补齐开始 $(date) ===" | tee -a /tmp/fill_all.log

# 逐批推进 (offset 跳过已处理; 每批启动时 outdir 已有的会再被断点续传跳过)
for ((off=OFFSET; off<=3515; off+=BATCH)); do
  stamp=$(date +%H:%M:%S)
  echo "[$stamp] === 批次 offset=$off (limit=$BATCH) ===" | tee -a /tmp/fill_all.log
  /usr/bin/python3 -u scripts/fill_missing_pdfs.py \
      --from-file missing_dois.txt \
      --offset "$off" --limit "$BATCH" \
      --workers 4 --scihub --skip-deep \
      --outdir raw/papers/fill_missing 2>&1 | tee -a /tmp/fill_all.log
  done_pdf=$(ls raw/papers/fill_missing/*.pdf 2>/dev/null | wc -l)
  echo "[$(date +%H:%M:%S)] 批次完成, 累计下载 PDF: $done_pdf" | tee -a /tmp/fill_all.log
done

echo "=== 全量补齐完成 $(date), 总耗时 $(( $(date +%s) - $(date -d "$START" +%s) ))s ===" | tee -a /tmp/fill_all.log
