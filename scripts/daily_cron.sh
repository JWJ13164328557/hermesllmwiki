#!/bin/bash
# 知识库完整更新流水线
# 初次运行: ./daily_cron.sh --backfill  (检索3年)
# 日常运行: cron每天8:00自动 (检索1天)

set -e
WIKI="/mnt/g/hermes_obsidian/hermes"
LOG="$WIKI/scripts/daily_cron.log"
PYTHON="/home/jiwj/miniconda3/bin/python"

# 参数: --backfill 表示全量回填3年
DAYS=1
MODE="daily"
if [ "$1" = "--backfill" ]; then
    DAYS=1095  # 3年
    MODE="backfill"
fi

echo "========================================" >> "$LOG"
echo "$(date '+%Y-%m-%d %H:%M:%S') 开始 [$MODE] 检索最近${DAYS}天" >> "$LOG"

cd "$WIKI"

# 1. git pull
echo "1. git pull..." >> "$LOG"
git pull origin main 2>&1 >> "$LOG" || echo "pull failed" >> "$LOG"

# 2. PubMed API检索 (11组策略, 覆盖全部知识库主题)
echo "2. PubMed检索 (${DAYS}天)..." >> "$LOG"
if [ "$MODE" = "backfill" ]; then
    $PYTHON scripts/daily_update.py --days "$DAYS" --import --max 50 2>&1 >> "$LOG"
else
    $PYTHON scripts/daily_update.py --days "$DAYS" --import 2>&1 >> "$LOG"
fi

# 3. PMC全文下载 + PubMed元数据爬取 (完整论文)
echo "3. 完整论文下载..." >> "$LOG"
$PYTHON scripts/pubmed_fulltext.py --enrich-all 2>&1 >> "$LOG"

# 4. 基于完整正文深度提炼
echo "4. 深度提炼..." >> "$LOG"
$PYTHON scripts/deep_curate_fulltext.py 2>&1 >> "$LOG"

# 5. 语义交叉引用重建
echo "5. 语义交叉引用..." >> "$LOG"
$PYTHON -c "
import os,re
from collections import defaultdict
base='$WIKI'
pages={}
for fn in os.listdir(f'{base}/concepts'):
    if not fn.endswith('.md') or fn.startswith('ref'): continue
    slug=fn.replace('.md','')
    with open(f'{base}/concepts/{fn}') as f: c=f.read()
    if '## 相关文献' in c: c=re.sub(r'\n\n## 相关文献\n\n.*$','',c,flags=re.DOTALL)
    with open(f'{base}/concepts/{fn}','w') as f: f.write(c)
    tm=re.search(r'(?:^# |title:\s*)(.+)',c)
    title=tm.group(1)[:60] if tm else slug
    sp=set(); mtd=set()
    ct=re.search(r'\*\*物种\*\*:\s*(.+)',c)
    if ct:
        for s in re.split(r'[,，]',ct.group(1)): sp.add(s.strip())
    cm=re.search(r'\*\*方法\*\*:\s*(.+)',c)
    if cm:
        for m in re.split(r'[,，]',cm.group(1)): mtd.add(m.strip())
    pages[slug]={'title':title,'species':sp,'methods':mtd,'path':f'{base}/concepts/{fn}'}
modified=0
for slug,info in pages.items():
    cand=[]
    for o,oi in pages.items():
        if slug==o: continue
        sc=len(info['species']&oi['species'])*5 + len(info['methods']&oi['methods'])*3
        if sc>=3: cand.append((o,sc,oi['title'],oi['species']))
    cand.sort(key=lambda x:-x[1])
    top=cand[:6]
    if not top: continue
    links='\n\n## 相关文献\n\n'
    for osl,sc,ot,osp in top:
        sh=info['species']&osp
        tag=f' 🌱{\",\".join(sorted(sh)[:2])}' if sh else ''
        links+=f'- [[{osl}]]{tag}\n'
    with open(info['path'],'a') as f: f.write(links)
    modified+=1
print(f'Links: {modified} pages rebuilt')
" 2>&1 >> "$LOG"

# 6. 统计 + 提交
CHANGES=$(git status --short | wc -l)
echo "6. 变更: $CHANGES 文件" >> "$LOG"

if [ "$CHANGES" -gt 0 ]; then
    git add -A
    git commit -m "[$MODE] $(date '+%Y-%m-%d') — 自动更新 (${DAYS}天范围)" 2>&1 >> "$LOG"
    git push origin main 2>&1 >> "$LOG" || echo "push failed" >> "$LOG"
    echo "✅ 完成: $CHANGES 文件变更" >> "$LOG"
else
    echo "⏭ 无变更" >> "$LOG"
fi

echo "$(date '+%Y-%m-%d %H:%M:%S') 结束 [$MODE]" >> "$LOG"
echo "" >> "$LOG"
