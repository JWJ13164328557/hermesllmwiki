#!/usr/bin/env python3
"""P2: DOI-only 论文 → 5-section 精简 Paper Spec + Evidence (通过 Crossref API)"""
import os, re, json, subprocess, time, sys, urllib.request, urllib.parse

BASE = '/mnt/g/hermes_obsidian/hermes'
PAPERS_DIR = os.path.join(BASE, 'concepts', 'papers')
EVIDENCE_DIR = os.path.join(BASE, 'evidence')
PRIORITY_FILE = '/tmp/doi_high_priority.json'

os.makedirs(EVIDENCE_DIR, exist_ok=True)

def doi_to_pmid(doi):
    """Convert DOI to PMID via NCBI"""
    try:
        encoded = urllib.parse.quote(f'{doi}[doi]', safe='')
        url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={encoded}&retmode=json'
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.load(resp)
        ids = data.get('esearchresult', {}).get('idlist', [])
        return ids[0] if ids else None
    except:
        return None

def crossref_metadata(doi):
    """Get metadata from Crossref API"""
    try:
        url = f'https://api.crossref.org/works/{urllib.parse.quote(doi)}'
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.load(resp)
        
        msg = data.get('message', {})
        
        # Title
        title_list = msg.get('title', [])
        title = title_list[0] if title_list else ''
        
        # Abstract
        abstract = msg.get('abstract', '')
        # Clean HTML tags from abstract
        abstract = re.sub(r'<[^>]+>', '', abstract)
        abstract = re.sub(r'\s+', ' ', abstract).strip()
        
        # Journal
        journal = ''
        container = msg.get('container-title', [])
        if container:
            journal = container[0]
        
        # Year
        year = ''
        issued = msg.get('issued', {})
        date_parts = issued.get('date-parts', [[None]])[0]
        if date_parts and date_parts[0]:
            year = str(date_parts[0])
        
        # Authors
        authors = []
        for author in msg.get('author', [])[:5]:
            given = author.get('given', '')
            family = author.get('family', '')
            authors.append(f"{given} {family}".strip())
        
        return {
            'title': title,
            'abstract': abstract[:3000],
            'journal': journal,
            'year': year,
            'authors': authors,
            'doi': doi,
        }
    except Exception as e:
        print(f"  Crossref error: {e}")
        return None

def extract_species_methods_topics(text):
    """Extract species, methods, topics from text"""
    species = []
    species_pats = [
        ('Arabidopsis thaliana', r'arabidopsis'),
        ('Oryza sativa', r'\brice\b|oryza'),
        ('Zea mays', r'\bmaize\b|zea'),
        ('Glycine max', r'\bsoybean\b|glycine'),
        ('Triticum aestivum', r'\bwheat\b|triticum'),
        ('Populus', r'\bpoplar\b|populus'),
    ]
    for name, pat in species_pats:
        if re.search(pat, text.lower()):
            species.append(name)
    
    methods = []
    method_pats = {
        'scRNA-seq': r'scrna[\s-]*seq|single[\s-]*cell[\s-]*rna',
        'spatial': r'spatial[\s-]*transcriptom|stereo[\s-]*seq|visium',
        'snRNA-seq': r'snrna[\s-]*seq|single[\s-]*nucleus',
    }
    for name, pat in method_pats.items():
        if re.search(pat, text.lower()):
            methods.append(name)
    
    topics = []
    topic_pats = {
        'development': r'\bdevelop|morphogenesis|embryo|meristem',
        'root': r'\broot\b',
        'leaf': r'\bleaf\b',
        'stress': r'\bstress|salt|drought',
    }
    for name, pat in topic_pats.items():
        if re.search(pat, text.lower()):
            topics.append(name)
    
    return species if species else ['plant'], methods if methods else ['not detected'], topics if topics else ['general']

def generate_compact_spec(meta, filename):
    """Generate 5-section compact Paper Spec"""
    text = (meta.get('title', '') + ' ' + meta.get('abstract', ''))
    species, methods, topics = extract_species_methods_topics(text)
    
    # Extract key sentences
    sentences = re.split(r'[.!?]\s+', meta.get('abstract', ''))
    key_sentences = [s.strip() for s in sentences if len(s.strip()) > 40][:5]
    
    doi = meta.get('doi', '')
    
    spec = f"""---
title: "{meta.get('title', 'Unknown')}"
doi: "{doi}"
journal: "{meta.get('journal', '')}"
year: "{meta.get('year', '')}"
authors: "{', '.join(meta.get('authors', [])[:4])}"
type: paper
tags: [{', '.join(topics)}]
species: [{', '.join(species)}]
methods: [{', '.join(methods)}]
status: curated
curation_depth: "Crossref摘要"
source_file: "{filename}"
updated: 2026-05-30
---

## 1. Scientific Context

{meta.get('abstract', '')[:600]}

**研究领域**: {', '.join(topics)}
**物种**: {', '.join(species)}
**期刊**: {meta.get('journal', 'unknown')} ({meta.get('year', '')})
**DOI**: [{doi}](https://doi.org/{doi})

## 2. Research Questions

基于摘要分析，本文主要关注:
1. {species[0] if species else '植物'}中{topics[0] if topics else '生物学过程'}的分子机制
2. {"单细胞/空间转录组" if any(m in str(methods) for m in ['scRNA-seq','spatial']) else "转录调控"}分析

> ⚠️ 本节基于Crossref摘要自动化分析，需人工审查

## 3. Key Findings (from abstract)

{chr(10).join(f"{i+1}. {s}" for i, s in enumerate(key_sentences)) if key_sentences else '> 摘要内容不足，需获取全文补充'}

## 4. Evidence Summary

| # | 声明 | 证据类型 | 置信度 |
|---|------|---------|--------|
{chr(10).join(f"| E{i+1} | {s[:100]}... | 待审查 | 中 |" for i, s in enumerate(key_sentences[:5])) if key_sentences else "| - | 待提取 | - | - |"}

## 5. Critical Assessment & Next Steps

**知识库价值**:
- 相关性: {"高" if any(m in str(methods) for m in ['scRNA-seq','spatial']) else "中"}
- 主要贡献: {', '.join(methods) if methods else '待确定'}

**下一步**:
- VPN下载全文后可升级为完整9-section Paper Spec
- 提取详细证据对象
- 交叉引用到相关实体页面

---
*自动生成于2026-05-30 | 基于Crossref摘要 | 需人工审查*
"""
    return spec, key_sentences, species, methods, topics

def save_evidence(doi, meta, sentences):
    """Create evidence objects"""
    created = []
    doi_slug = re.sub(r'[^a-z0-9]', '-', doi.lower())[:30]
    for i, s in enumerate(sentences[:4]):
        ev_id = f"ev-doi-{doi_slug}-{i+1:02d}"
        content = f"""---
title: "Evidence: {s[:80]}..."
evidence_id: "{ev_id}"
doi: "{doi}"
source: "{meta.get('journal', '')} ({meta.get('year', '')})"
type: evidence
status: auto-generated
quality: medium
updated: 2026-05-30
---

# {ev_id}

## Claim
{s[:500]}

## Source
{meta.get('title', '')[:200]}
DOI: {doi}
Journal: {meta.get('journal', '')}

## Evidence Quality
**自动评级**: 中等 (基于Crossref摘要提取)

## Next
- 获取全文后升级评估
"""
        fpath = os.path.join(EVIDENCE_DIR, f"{ev_id}.md")
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        created.append(ev_id)
    return created

def main():
    with open(PRIORITY_FILE, 'r', encoding='utf-8') as f:
        papers = json.load(f)
    
    # Deduplicate by title (first 60 chars)
    seen_titles = set()
    unique_papers = []
    for p in papers:
        title_key = p['title'][:60].lower()
        if title_key not in seen_titles:
            seen_titles.add(title_key)
            unique_papers.append(p)
    
    print(f"Processing {len(unique_papers)} unique papers (from {len(papers)} total)")
    print("=" * 60)
    
    stats = {'success': 0, 'fail': 0, 'evidence': 0, 'pmid_found': 0}
    
    for i, paper in enumerate(unique_papers):
        filename = paper['file']
        fpath = os.path.join(PAPERS_DIR, filename)
        
        # Extract DOI from file
        with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read(5000)
        doi_m = re.search(r'doi:\s*(\S+)', content)
        if not doi_m:
            print(f"[{i+1}/{len(unique_papers)}] {filename[:50]}: NO DOI FOUND")
            stats['fail'] += 1
            continue
        
        doi = doi_m.group(1).strip()
        print(f"\n[{i+1}/{len(unique_papers)}] {filename[:50]}")
        print(f"  DOI: {doi[:60]}")
        
        # Try PMID conversion first
        pmid = doi_to_pmid(doi)
        if pmid:
            print(f"  ✓ PMID found: {pmid} (will process in P1 pipeline)")
            stats['pmid_found'] += 1
            # Update file with PMID
            new_content = content.replace(f'doi: {doi}', f'doi: {doi}\npmid: "{pmid}"')
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            continue
        
        # Get Crossref metadata
        meta = crossref_metadata(doi)
        if not meta:
            print(f"  ✗ Crossref metadata failed")
            stats['fail'] += 1
            continue
        
        print(f"  Journal: {meta.get('journal','?')[:40]}")
        print(f"  Abstract: {len(meta.get('abstract',''))} chars")
        
        # Generate compact spec
        spec, sentences, species, methods, topics = generate_compact_spec(meta, filename)
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(spec)
        stats['success'] += 1
        print(f"  ✓ 5-section spec written ({len(spec)} chars)")
        
        # Evidence
        if sentences:
            ev_ids = save_evidence(doi, meta, sentences)
            stats['evidence'] += len(ev_ids)
        
        time.sleep(1.5)  # Rate limiting for Crossref
    
    print("\n" + "=" * 60)
    print(f"COMPLETE: {len(unique_papers)} papers")
    print(f"  5-section spec: {stats['success']}")
    print(f"  PMID found (deferred to P1): {stats['pmid_found']}")
    print(f"  Failed: {stats['fail']}")
    print(f"  Evidence objects: {stats['evidence']}")

if __name__ == '__main__':
    main()
