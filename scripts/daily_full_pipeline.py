#!/usr/bin/env python3
"""
每日文献全流水线 — Phase 3→8 增量自动化
Phase 3:  概念页创建 (daily_update.py + 多源检索)
Phase 4:  全文下载 (Europe PMC → OpenAlex → Sci-Hub)
Phase 5:  增量深度提炼 (仅今日新增 → deep_curate_all.py --dois)
Phase 6:  Evidence Objects + Entity (增量更新)
Phase 7:  Synthesis 增量整合 (新证据 → 已有框架)
Phase 8:  整合后整理 (Hypothesis + Research Program)
"""

import os, sys, subprocess, json, re, glob
from datetime import datetime, timedelta

# JCR 2024 植物/农学/相关期刊权威白名单 (防多源导入引入非植物期刊污染)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scripts'))
try:
    from jcr_whitelist import journal_in_jcr
except ImportError:
    def journal_in_jcr(journal_name):
        return False

# 植物物种关键词 (is_plant 内容校验, 多源导入的二次防线)
PLANT_TERMS = ['arabidopsis','thaliana','rice','oryza','maize','zea','wheat','triticum',
               'soybean','glycine','tomato','solanum','barley','hordeum','sorghum','cassava',
               'potato','cucumber','pepper','capsicum','melon','rapeseed','brassica','sunflower',
               'cotton','gossypium','sugarcane','tobacco','nicotiana','medicago','lotus','phaseolus',
               'pea','vigna','poplar','populus','eucalyptus','pine','pinus','spruce','moss',
               'marchantia','physcomitrella','fern','algae','chlamydomonas','grape','vitis',
               'citrus','malus','pear','banana','strawberry','tea','camellia','orchid','bamboo',
               'ginger','garlic','onion','plant','crop','seedling','leaf','root','inflorescence',
               'xylem','phloem','chlorophyll','photosynth','chloroplast','phytochrome','flower',
               'pollen','anther','seed','fruit','floral']

def is_plant_content(text):
    """标题+摘要是否有植物物种词。"""
    t = (text or '').lower()
    return any(p in t for p in PLANT_TERMS)


BASE = '/mnt/g/hermes_obsidian/hermes'
SCRIPTS = f'{BASE}/scripts'
CONCEPTS = f'{BASE}/concepts/papers'
EVIDENCE = f'{BASE}/evidence'

def run(cmd, timeout=300):
    """运行命令，返回 (success, output)"""
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout, cwd=BASE)
        return r.returncode == 0, r.stdout[-2000:] + r.stderr[-1000:]
    except subprocess.TimeoutExpired:
        return False, "TIMEOUT"

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

def main():
    today = datetime.now().strftime('%Y-%m-%d')
    log(f"=== 每日全流水线 {today} ===")
    
    # ── Phase 3: 多源检索 + 概念页创建 (PubMed + OpenAlex + Crossref) ──
    log("Phase 3: 多源检索 (PubMed + OpenAlex + Crossref)")
    ok, out = run(f'python3 {SCRIPTS}/daily_update.py --days=1095 --import --max=50')
    print(out[-500:] if out else "no output")
    
    ok2, out2 = run(f'python3 {SCRIPTS}/multi_source_search.py --days=365 --max=20 --skip-s2 --skip-web', timeout=120)
    if ok2:
        # Import new DOI candidates not already covered by PubMed
        candidates_file = f'{SCRIPTS}/multi_source_candidates.json'
        if os.path.exists(candidates_file):
            with open(candidates_file) as f:
                candidates = json.load(f)
            # Get existing DOIs
            existing_dois = set()
            for fp in glob.glob(f'{CONCEPTS}/*.md') + glob.glob(f'{BASE}/concepts/daily-*.md'):
                try:
                    with open(fp, 'r') as fh:
                        content = fh.read(2000)
                    m = re.search(r'doi:\s*(10\.\d{4,}/[^\s\n]+)', content, re.I)
                    if m:
                        existing_dois.add(m.group(1).strip().rstrip('./'))
                except:
                    pass
            
            imported = 0
            for paper in candidates.get('candidates', []):
                doi = paper.get('doi', '')
                if not doi or doi in existing_dois:
                    continue
                # ── 期刊/植物过滤 (防污染) ──
                journal = paper.get('journal', '')
                title = paper.get('title', '') or ''
                abstract = paper.get('abstract', '') or ''
                jl = (journal or '').lower()
                # ① JCR 植物/农学权威名单放行 (最高优先级, additive)
                if journal_in_jcr(journal):
                    pass
                else:
                    # ②③ 主题相关性综合校验 (植物/非植物双重重判, 2026-08-25 防污染防线)
                    try:
                        from theme_filter import is_relevant_plant_paper
                        ok, why = is_relevant_plant_paper(title, abstract, journal)
                        if not ok:
                            log(f"   ⛔ 主题过滤拒绝 (非植物): {why} | {title[:50]}")
                            continue
                    except ImportError:
                        # 回退: 旧的双线过滤
                        NONPLANT_J = ['oncol','cancer','medic','med ','hepat','cardiol','diabet',
                                      'immunolog','drug','fuel','energy','mater','chem eng','nuclear',
                                      'virol','surg','psych','dermat','neurol','pharm','toxic']
                        if any(np in jl for np in NONPLANT_J):
                            if not any(pw in jl for pw in ['plant','botan','crop','agron','hortic','phyt','forest','agri']):
                                continue
                        if not is_plant_content(title + ' ' + abstract):
                            continue
                # Create concept page from multi-source metadata
                slug = f"ms-{doi.replace('/', '_').replace('.', '-')[:60]}"
                fp = f'{CONCEPTS}/{slug}.md'
                if os.path.exists(fp):
                    continue
                
                year = paper.get('year', '')
                authors = paper.get('authors', [])
                if isinstance(authors, list) and authors and isinstance(authors[0], dict):
                    author_names = [a.get('name', '') for a in authors[:5]]
                else:
                    author_names = [str(a) for a in authors[:5]] if authors else []
                
                source = paper.get('source', 'unknown')
                concepts = ', '.join(paper.get('concepts', [])) if paper.get('concepts') else ''
                
                with open(fp, 'w', encoding='utf-8') as fh:
                    fh.write(f"""---
title: {title[:80]}
created: {today}
type: concept
tags: [papers]
doi: {doi}
confidence: moderate
source: {source}
---

# {title}

## 论文信息
- **期刊**: {journal} ({year})
- **DOI**: [{doi}](https://doi.org/{doi})
- **作者**: {', '.join(author_names[:5]) if author_names else '—'}
- **来源**: {source}
{"- **概念**: " + concepts if concepts else ""}

## 摘要
{abstract[:3000] if abstract else '（摘要需从原文获取）'}

## 深度提炼

**物种**: —
**来源**: {source} | DOI:{doi}
""")
                existing_dois.add(doi)
                imported += 1
            
            log(f"  多源导入: {imported} 篇 (总候选 {candidates.get('total', 0)})")
            print(out2[-500:] if out2 else "no output")
    
    # 检测今天新增的论文 (三层检测，覆盖 git tracked + untracked + mtime)
    today_pages = set()
    
    # 方法1: git diff -- 已跟踪的新增文件
    try:
        r = subprocess.run(
            'git diff --name-only --diff-filter=A HEAD~1 HEAD -- concepts/papers/',
            shell=True, capture_output=True, text=True, cwd=BASE, timeout=30
        )
        for f in r.stdout.strip().split('\n'):
            if f.endswith('.md'):
                today_pages.add(os.path.join(BASE, f))
    except:
        pass
    
    # 方法2: git ls-files --others -- 未跟踪文件（本次运行创建但未提交的）
    try:
        r = subprocess.run(
            'git ls-files --others --exclude-standard -- concepts/papers/',
            shell=True, capture_output=True, text=True, cwd=BASE, timeout=30
        )
        for f in r.stdout.strip().split('\n'):
            if f.endswith('.md'):
                fp = os.path.join(BASE, f)
                if os.path.exists(fp):
                    today_pages.add(fp)
    except:
        pass
    
    # 方法3: mtime 回退 (扩大扫描范围到200个文件)
    if not today_pages:
        candidates = sorted(glob.glob(f'{CONCEPTS}/*.md'))[:200]
        for f in candidates:
            mtime = datetime.fromtimestamp(os.path.getmtime(f))
            if mtime.strftime('%Y-%m-%d') == today:
                today_pages.add(f)
    
    if not today_pages:
        log("无新论文，流水线终止")
        return
    
    log(f"今日新增: {len(today_pages)} 篇")
    
    # ── Phase 4: Full-text Download (多通道含 Sci-Hub, 2026-08-24 改造) ──
    dois = set()
    for fp in today_pages:
        with open(fp, 'r') as fh:
            content = fh.read()
        m = re.search(r'doi:\s*(10\.\d{4,}/[^\s\n]+)', content, re.I)
        if m:
            dois.add(m.group(1).strip().rstrip('./'))
    
    log(f"Phase 4: 全文下载 ({len(dois)} 篇，多通道 + Sci-Hub 兜底)")
    
    # 写今日新增 DOI 到临时文件 → 复用 fill_missing_pdfs.py 完整多通道下载
    if dois:
        tmp_dois = f'{BASE}/.phase4_today_dois.txt'
        with open(tmp_dois, 'w') as fh:
            fh.write('\n'.join(sorted(dois)))
        ok, out = run(
            f'/usr/bin/python3 -u {SCRIPTS}/fill_missing_pdfs.py '
            f'--from-file {tmp_dois} --workers 4 --scihub --skip-deep '
            f'--outdir raw/papers/daily_new',
            timeout=2400
        )
        # 统计下载成功数(从报告读取)
        dl = 0
        rep = f'{BASE}/raw/papers/daily_new/fill_missing_report.csv'
        if os.path.exists(rep):
            import csv as _csv
            try:
                for row in _csv.DictReader(open(rep, encoding='utf-8-sig')):
                    if row.get('status') == 'ok':
                        dl += 1
            except Exception:
                pass
        log(f"Phase 4 完成: 获取 {dl}/{len(dois)} 篇 PDF")
    
    # ── Phase 5: 增量深度提炼 (仅今日新增论文) ──
    log(f"Phase 5: 增量深度提炼 ({len(today_pages)} 篇新论文)")
    
    # Extract DOIs from today's new pages
    new_dois = []
    for fp in today_pages:
        with open(fp, 'r') as fh:
            content = fh.read(3000)
        m = re.search(r'doi:\s*(10\.\d{4,}/[^\s\n]+)', content, re.I)
        if m:
            new_dois.append(m.group(1).strip().rstrip('./'))
    
    if new_dois:
        # Write DOIs to temp file for deep_curate_all.py
        dois_file = f'{BASE}/.temp_new_dois.txt'
        with open(dois_file, 'w') as fh:
            fh.write('\n'.join(new_dois))
        
        ok, out = run(
            f'python3 -u {SCRIPTS}/deep_curate_all.py --dois {dois_file}',
            timeout=1800
        )
        log(f"deep_curate_all: {out[-300:] if out else 'no output'}")
    
    # Count today's curation success + total
    curated_new = 0
    for fp in today_pages:
        try:
            with open(fp, 'r') as fh:
                content = fh.read()
            if '**物种**:' in content and '### 核心发现' in content:
                curated_new += 1
        except:
            pass
    
    curated_total = 0
    for fp in glob.glob(f'{CONCEPTS}/*.md') + glob.glob(f'{BASE}/concepts/daily-*.md'):
        try:
            with open(fp, 'r') as fh:
                content = fh.read()
            if '**物种**:' in content and '### 核心发现' in content:
                curated_total += 1
        except:
            pass
    log(f"今日提炼: {curated_new}/{len(today_pages)} 篇 → 累计 {curated_total} 篇已深度提炼")
    
    # ── Phase 6: 增量 Evidence Objects (仅从今日新evidence创建/更新) ──
    log(f"Phase 6: 增量 Evidence Objects + Entity + Relationships")
    ok, out = run(f'python3 {SCRIPTS}/batch_evidence_objects.py', timeout=600)
    log(f"Evidence: {out[:200]}")
    
    # ── Phase 7: 增量综合推理 (Synthesis — 整合新证据到已有框架) ──
    log(f"Phase 7: 增量综合推理 (Synthesis — 整合新证据)")
    ok, out = run(f'python3 -u {SCRIPTS}/batch_synthesis.py --update', timeout=600)
    log(f"Synthesis: {out[:200]}")
    
    # ── Phase 8: 证据整合后整理 (Hypothesis + Research Program 基于全量整合) ──
    log(f"Phase 8: 整合后整理 (Hypothesis + Research Program)")
    ok, out = run(f'python3 -u {SCRIPTS}/batch_hypotheses.py', timeout=600)
    log(f"Hypotheses/Programs: {out[:200]}")
    
    # ── 收尾 ──
    log("收尾: 翻译 + 交叉引用")
    run(f'python3 {SCRIPTS}/batch_translate_metabolism.py --today', timeout=120)
    
    # Git
    log("Git commit")
    run(f'cd {BASE} && git add concepts/ evidence/ entities/ synthesis/ hypotheses/ research-programs/ && git commit -m "daily: {today} — {len(today_pages)} new papers, {curated_total} curated, full hierarchy updated"', timeout=30)
    run(f'cd {BASE} && git push', timeout=60)
    
    log(f"=== 完成: {len(today_pages)} 导入, {curated_total} 提炼 ===")

if __name__ == '__main__':
    main()
