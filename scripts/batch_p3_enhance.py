#!/usr/bin/env python3
"""P3: 无PMID/DOI论文 → Enhanced Frontmatter + 结构化摘要"""
import os, re, json, time

BASE = '/mnt/g/hermes_obsidian/hermes'
PAPERS_DIR = os.path.join(BASE, 'concepts', 'papers')

def extract_metadata(content, filename):
    """Extract what we can from existing content"""
    meta = {'file': filename}
    
    # Existing frontmatter
    fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if fm_match:
        fm = fm_match.group(1)
        for key in ['title', 'journal', 'year', 'tags', 'species', 'type', 'status']:
            m = re.search(rf'{key}:\s*(.+?)(?:\n|$)', fm)
            if m:
                meta[key] = m.group(1).strip()
    
    # Extract body content (after frontmatter)
    body = content[fm_match.end():] if fm_match else content
    
    # Try to extract title from body
    if 'title' not in meta or not meta.get('title'):
        title_m = re.search(r'(?:标题|Title|题目)[：:]\s*(.+?)(?:\n|$)', body)
        if title_m:
            meta['title'] = title_m.group(1).strip()
        else:
            # Use first meaningful line
            for line in body.split('\n'):
                line = line.strip()
                if len(line) > 20 and not line.startswith('#') and not line.startswith('>'):
                    meta['title'] = line[:200]
                    break
    
    # Species detection
    species_patterns = [
        ('Arabidopsis thaliana', r'arabidopsis|拟南芥'),
        ('Oryza sativa', r'\brice\b|水稻|oryza'),
        ('Zea mays', r'\bmaize\b|玉米|zea'),
        ('Glycine max', r'\bsoybean\b|大豆|glycine'),
        ('Triticum aestivum', r'\bwheat\b|小麦|triticum'),
        ('Populus', r'\bpoplar\b|杨树|populus'),
        ('Solanum lycopersicum', r'\btomato\b|番茄|solanum'),
        ('Gossypium', r'\bcotton\b|棉花|gossypium'),
        ('Nicotiana', r'\btobacco\b|烟草|nicotiana'),
        ('Brassica', r'\bbrassica\b|油菜|白菜'),
        ('Medicago', r'\bmedicago\b|苜蓿'),
        ('Cunninghamia', r'\bcunninghamia\b|杉木'),
        ('Marchantia', r'\bmarchantia\b|地钱|liverwort'),
        ('Physcomitrium', r'\bphyscomit\w*\b|小立碗藓|moss'),
    ]
    detected_species = []
    text_lower = body.lower()
    for name, pat in species_patterns:
        if re.search(pat, text_lower, re.IGNORECASE):
            detected_species.append(name)
    
    # Topic detection
    topics = []
    topic_pats = [
        ('development', r'发育|development|morphogenesis'),
        ('stress', r'胁迫|stress|salt|drought|cold|heat'),
        ('hormone', r'激素|hormone|auxin|gibberellin|aba'),
        ('signaling', r'信号|signal|phosphorylation|kinase'),
        ('gene-regulation', r'转录因子|transcription.*factor|调控'),
        ('metabolism', r'代谢|metabol|biosynthesis'),
        ('single-cell', r'单细胞|single.cell|scrna'),
        ('spatial', r'空间|spatial|stereo.seq'),
        ('epigenetics', r'表观|epigen|chromatin|甲基化'),
        ('regeneration', r'再生|regenerat|callus'),
        ('flowering', r'开花|flower|floral'),
    ]
    for topic, pat in topic_pats:
        if re.search(pat, text_lower, re.IGNORECASE):
            topics.append(topic)
    
    meta['species'] = detected_species if detected_species else ['plant']
    meta['topics'] = topics if topics else ['general']
    
    return meta

def generate_enhanced_content(meta, existing_body):
    """Generate enhanced frontmatter + structured summary"""
    
    title = meta.get('title', 'Untitled')
    species_str = ', '.join(meta.get('species', ['plant']))
    topics_str = ', '.join(meta.get('topics', ['general']))
    journal = meta.get('journal', 'unknown')
    year = meta.get('year', '')
    
    enhanced = f"""---
title: "{title}"
journal: "{journal}"
year: "{year}"
type: paper
tags: [{topics_str}]
species: [{species_str}]
status: frontmatter-enhanced
curation_depth: "基础整理"
updated: 2026-05-30
---

## 摘要

{existing_body[:800] if existing_body.strip() else '> 内容待补充'}

## 关键信息

- **物种**: {species_str}
- **研究主题**: {topics_str}
- **期刊**: {journal} ({year})

## 待升级

> ⚠️ 本文缺少 PMID/DOI，无法自动获取全文。
> 建议:
> 1. 补充 DOI 或 PMID 后可升级为 5-section 精简 Paper Spec
> 2. 提供 PDF 后可人工转换为 9-section 完整 Paper Spec
> 3. 对于非学术来源（微信公众号等），保持当前格式即可

---
*P3 自动增强于 2026-05-30 | 需人工审查*
"""
    return enhanced

def main():
    all_files = sorted([f for f in os.listdir(PAPERS_DIR) if f.endswith('.md')])
    
    # Find papers without PMID or DOI
    no_id_papers = []
    for f in all_files:
        fpath = os.path.join(PAPERS_DIR, f)
        with open(fpath, 'r', encoding='utf-8', errors='replace') as fh:
            content = fh.read()
        
        has_pmid = 'pmid:' in content[:2000]
        has_doi = 'doi:' in content[:2000]
        
        if not has_pmid and not has_doi:
            size = os.path.getsize(fpath)
            # Skip already enhanced (>2KB)
            if size < 2000:
                no_id_papers.append((f, content))
    
    print(f"Papers to enhance (no PMID/DOI, <2KB): {len(no_id_papers)}")
    print("=" * 60)
    
    stats = {'enhanced': 0, 'skipped_small': 0, 'errors': 0}
    
    for i, (filename, content) in enumerate(no_id_papers):
        if i % 50 == 0:
            print(f"  [{i}/{len(no_id_papers)}]...")
        
        try:
            # Extract existing body
            fm_match = re.search(r'^---\n.*?\n---', content, re.DOTALL)
            if fm_match:
                body = content[fm_match.end():].strip()
            else:
                body = content.strip()
            
            # Check if body is too sparse
            if len(body) < 30 and len(content) < 500:
                stats['skipped_small'] += 1
                continue
            
            meta = extract_metadata(content, filename)
            enhanced = generate_enhanced_content(meta, body)
            
            fpath = os.path.join(PAPERS_DIR, filename)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(enhanced)
            stats['enhanced'] += 1
            
        except Exception as e:
            stats['errors'] += 1
            if stats['errors'] <= 5:
                print(f"  ERROR {filename[:50]}: {e}")
    
    print(f"\n{'='*60}")
    print(f"DONE: {len(no_id_papers)} papers scanned")
    print(f"  Enhanced: {stats['enhanced']}")
    print(f"  Skipped (too small): {stats['skipped_small']}")
    print(f"  Errors: {stats['errors']}")

if __name__ == '__main__':
    main()
