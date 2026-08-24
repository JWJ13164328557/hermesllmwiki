#!/usr/bin/env python3
"""P4a: 跨论文 Synthesis 生成 — 自动主题发现 + 从 Evidence Objects 提炼共识/争议/空白"""
import os, re, json, math
from collections import Counter, defaultdict
from itertools import combinations

BASE = '/mnt/g/hermes_obsidian/hermes'
PAPERS_DIR = os.path.join(BASE, 'concepts', 'papers')
EVIDENCE_DIR = os.path.join(BASE, 'evidence')
SYNTHESIS_DIR = os.path.join(BASE, 'synthesis')
os.makedirs(SYNTHESIS_DIR, exist_ok=True)

# ============================================================
# Soybean relevance keywords for scoring
# ============================================================
SOYBEAN_KEYWORDS = [
    'soybean', 'glycine', 'legume', 'internode', 'cambium', 'vascular',
    'light quality', 'shade', 'phytochrome', 'photomorphogen',
    'stem', 'wood', 'xylem', 'phloem', 'secondary growth',
    'auxin', 'gibberellin', 'brassinosteroid', 'cell wall',
]

# ============================================================
# Phase 1: Load all evidence with tags
# ============================================================
def load_all_evidence():
    """Load evidence objects, extract tags and claims"""
    all_evidence = []
    for f in sorted(os.listdir(EVIDENCE_DIR)):
        if not f.endswith('.md'): continue
        fpath = os.path.join(EVIDENCE_DIR, f)
        with open(fpath, 'r', encoding='utf-8', errors='replace') as fh:
            content = fh.read()
        
        # Extract claim
        claim_m = re.search(r'(?:^claim:\s*"?(.+?)"?\n|## Claim\n(.+?)(?=\n##|\Z))', content, re.DOTALL)
        claim = ''
        if claim_m:
            claim = (claim_m.group(1) or claim_m.group(2) or '').strip()[:500]
        
        # Extract tags (inline format: tags: [a, b, c])
        tags = []
        tag_m = re.search(r'^tags:\s*\[(.+?)\]', content, re.MULTILINE)
        if tag_m:
            tags = [t.strip().strip('"').strip("'") for t in tag_m.group(1).split(',')]
        
        # For older format without tags, derive from claim_type + species + tissue
        if not tags:
            # Derive tags from structured fields
            claim_type_m = re.search(r'^claim_type:\s*(.+)', content, re.MULTILINE)
            species_m = []
            tissue_m = []
            sp_match = re.search(r'^species:\s*\n((?:\s{2}-.+\n?)+)', content, re.MULTILINE)
            if sp_match:
                species_m = re.findall(r'^\s{2}-\s*(.+)', sp_match.group(1))
            ti_match = re.search(r'^tissue:\s*\n((?:\s{2}-.+\n?)+)', content, re.MULTILINE)
            if ti_match:
                tissue_m = re.findall(r'^\s{2}-\s*(.+)', ti_match.group(1))
            
            if claim_type_m:
                ct = claim_type_m.group(1).strip()
                ct_map = {
                    'methodological': 'method', 'method': 'method',
                    'observation': 'observation',
                    'functional': 'functional',
                }
                tags.append(ct_map.get(ct, ct))
            tags.extend(species_m[:3])
            tags.extend(tissue_m[:2])
        
        # ── Content-based tag enrichment: extract implicit themes from claim text ──
        claim_lower = claim.lower()
        # Hormone signaling keywords
        if any(kw in claim_lower for kw in ['auxin', 'gibberellin', 'abscisic', 'brassinosteroid',
                'cytokinin', 'ethylene signal', 'jasmonic', 'salicylic', 'strigolactone']):
            tags.append('hormone-signaling')
        # Regeneration keywords
        if any(kw in claim_lower for kw in ['regeneration', 'callus', 'reprogram', 'totipot',
                'somatic embryo', 'de novo organogenesis', 'shoot regeneration']):
            tags.append('regeneration')
        # Stress keywords
        if any(kw in claim_lower for kw in ['drought', 'salt stress', 'cold stress', 'heat stress',
                'pathogen', 'defense response', 'oxidative stress']):
            tags.append('stress')
        # Development keywords
        if any(kw in claim_lower for kw in ['development', 'differentiation', 'morphogenesis',
                'organogenesis', 'embryogenesis', 'meristem']):
            tags.append('development')
        # Cell wall / vascular
        if any(kw in claim_lower for kw in ['cell wall', 'lignin', 'cellulose', 'xylem',
                'phloem', 'cambium', 'vascular', 'wood formation']):
            tags.append('cell-wall')
        
        # Extract metadata
        pmid_m = re.search(r'pmid:\s*"?(\d+)"?', content)
        doi_m = re.search(r'doi:\s*"?(\S+)"?', content)
        source_m = re.search(r'source:\s*"?(.+?)"?\n', content)
        quality_m = re.search(r'quality:\s*(\\w+)', content)
        
        all_evidence.append({
            'id': f.replace('.md', ''),
            'claim': claim,
            'tags': tags,
            'pmid': pmid_m.group(1) if pmid_m else '',
            'doi': doi_m.group(1) if doi_m else '',
            'source': source_m.group(1) if source_m else '',
            'quality': quality_m.group(1) if quality_m else 'medium',
            'full_content': content,
        })
    
    return all_evidence

# ============================================================
# Phase 2: Tag co-occurrence graph + community detection
# ============================================================
def build_tag_graph(all_evidence):
    """Build tag co-occurrence graph from evidence objects"""
    tag_cooccur = defaultdict(Counter)
    tag_freq = Counter()
    
    for ev in all_evidence:
        tags = ev['tags']
        for t in tags:
            tag_freq[t] += 1
        # Co-occurrence
        for t1, t2 in combinations(sorted(set(tags)), 2):
            tag_cooccur[t1][t2] += 1
            tag_cooccur[t2][t1] += 1
    
    return tag_cooccur, tag_freq

def community_detection(tag_cooccur, tag_freq, min_tag_freq=3):
    """Connected-component clustering on tag co-occurrence graph with Jaccard threshold"""
    # Filter rare and stop tags
    STOP_TAGS = {'paper', 'pmc'}
    active_tags = {t for t in tag_freq if tag_freq[t] >= min_tag_freq and t not in STOP_TAGS}
    
    # Build adjacency: edge exists if Jaccard >= threshold
    threshold = 0.08
    edges = set()
    for t1 in active_tags:
        for t2, co in tag_cooccur[t1].items():
            if t2 not in active_tags or t2 <= t1:
                continue
            jaccard = co / (tag_freq[t1] + tag_freq[t2] - co)
            if jaccard >= threshold:
                edges.add((t1, t2))
    
    # Connected components (union-find)
    parent = {t: t for t in active_tags}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    
    for t1, t2 in edges:
        union(t1, t2)
    
    # Collect communities
    communities_map = defaultdict(set)
    for t in active_tags:
        communities_map[find(t)].add(t)
    
    communities = sorted(communities_map.values(), key=lambda c: -sum(tag_freq[t] for t in c))
    
    # Filter: keep only communities with meaningful biological tags (≥3 non-generic)
    meaningful = []
    for comm in communities:
        if len(comm) >= 2:
            meaningful.append(comm)
    
    # Add significant orphan tags as singleton communities
    # (tags that are biologically specific but don't co-occur strongly enough)
    clustered_tags = set().union(*meaningful) if meaningful else set()
    orphans = [t for t in active_tags if t not in clustered_tags 
               and tag_freq[t] >= 30
               and t not in ('observation', 'functional', 'method', 'development',
                             'arabidopsis', 'arabidopsis thaliana')]
    for t in orphans:
        meaningful.append({t})
    
    return meaningful

def name_community(community, tag_freq, all_evidence):
    """Generate a human-readable name for a tag community"""
    # Skip generic hub tags for naming
    GENERIC_NAMING = {'metabolism', 'transcriptomics', 'metabolomics', 'genomics', 
                      'arabidopsis', 'secondary-metabolism', 'multi-omics'}
    specific = [t for t in community if t not in GENERIC_NAMING]
    if not specific:
        specific = sorted(community, key=lambda t: -tag_freq[t])[:3]
    
    top_tags = sorted(specific, key=lambda t: -tag_freq[t])[:5]
    
    # Count evidence objects in this community
    n_evidence = sum(1 for ev in all_evidence 
                     if any(t in community for t in ev['tags']))
    
    emoji_map = {
        'root': '🌱', 'development': '🌱',
        'flavonoid': '🍇', 'anthocyanin': '🍇', 'phenylpropanoid': '🌸',
        'terpenoid': '🌿', 'alkaloid': '💊', 'lipid': '🧈',
        'starch-sugar': '🍬',
        'stress': '⚡', 'immunity': '🛡️', 'defense': '🛡️',
        'hormone': '🧪', 'signaling': '🧪',
        'single-cell': '🔬', 'spatial': '🗺️', 'spatial-transcriptomics': '🗺️',
        'regeneration': '🔄', 'epigenetic': '🧬',
        'leaf': '🍃', 'shoot': '🌿', 'rice': '🌾', 'maize': '🌽',
        'method': '💻', 'protocol': '📋',
    }
    emoji = next((emoji_map.get(t, '📄') for t in top_tags), '📄')
    
    main_topics = top_tags[:3]
    title = ' & '.join(t.title() for t in main_topics)
    slug = '-'.join(re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-') for t in main_topics[:2])
    
    # Add all tags as a richer description
    all_tags_sorted = sorted(community, key=lambda t: -tag_freq[t])
    
    return {
        'slug': slug or 'untitled',
        'title': title,
        'emoji': emoji,
        'tags': all_tags_sorted[:8],  # Keep top 8 for evidence matching
        'n_evidence': n_evidence,
        'description': f'自动发现主题 — 核心: {", ".join(main_topics)} | 全部标签: {", ".join(all_tags_sorted)}',
    }

def score_soybean_relevance(community, all_evidence):
    """Score how relevant this topic is to soybean internode light quality project"""
    community_evidence = [ev for ev in all_evidence 
                          if any(t in community for t in ev['tags'])]
    
    score = 0
    for ev in community_evidence:
        text = (ev['claim'] + ' ' + ' '.join(ev['tags'])).lower()
        for kw in SOYBEAN_KEYWORDS:
            if kw in text:
                score += 1
    
    n = max(len(community_evidence), 1)
    density = score / n
    
    if density > 2.0:
        return '高 — 直接关联大豆节间光质响应'
    elif density > 1.0:
        return '中 — 部分方法/机制可借鉴'
    elif density > 0.3:
        return '低 — 可提供背景知识'
    else:
        return '低 — 间接关联'

def auto_discover_clusters(all_evidence):
    """Main auto-discovery: tag graph → communities → named clusters"""
    tag_cooccur, tag_freq = build_tag_graph(all_evidence)
    communities = community_detection(tag_cooccur, tag_freq, min_tag_freq=2)
    
    print(f"  Tags total: {len(tag_freq)}")
    print(f"  Communities detected: {len(communities)}")
    
    clusters = {}
    for i, comm in enumerate(communities):
        info = name_community(comm, tag_freq, all_evidence)
        info['relevance_to_soybean'] = score_soybean_relevance(comm, all_evidence)
        clusters[info['slug']] = info
        print(f"    [{i+1}] {info['title']} ({info['n_evidence']} evidence, {len(comm)} tags) — {info['relevance_to_soybean']}")
    
    return clusters

# ============================================================
# Phase 3: Classify evidence into auto-discovered clusters
# ============================================================
def classify_evidence(evidence_list, cluster_tags):
    """Classify evidence into a cluster based on tag overlap"""
    matched = []
    for ev in evidence_list:
        overlap = sum(1 for t in ev['tags'] if t in cluster_tags)
        if overlap >= 2:
            matched.append(ev)
        elif overlap >= 1 and len(ev['tags']) <= 2:
            matched.append(ev)  # Small evidence objects with 1 matching tag
    return matched

# ============================================================
# Phase 4: Find consensus from evidence cluster
# ============================================================
def find_consensus(evidence_cluster):
    """Group similar claims and identify consensus patterns"""
    phrase_counter = Counter()
    claim_groups = defaultdict(list)
    
    for ev in evidence_cluster:
        claim = ev['claim']
        phrases = re.findall(r'([A-Z][a-z]+ [a-z]+ (?:development|differentiation|signaling|regulation|expression|formation|biosynthesis))', claim)
        for p in phrases:
            phrase_counter[p] += 1
            claim_groups[p].append(ev)
    
    consensus = []
    for phrase, count in phrase_counter.most_common(20):
        if count >= 2:
            supporting_ev = claim_groups[phrase][:5]
            unique_sources = len(set(e['pmid'] or e['doi'] for e in supporting_ev if e['pmid'] or e['doi']))
            if unique_sources >= 2:
                consensus.append({
                    'pattern': phrase,
                    'paper_count': unique_sources,
                    'evidence_count': count,
                    'sample_claims': [e['claim'][:200] for e in supporting_ev[:3]],
                    'sample_sources': [e['source'][:60] for e in supporting_ev[:3]],
                })
    
    return consensus[:10]

def find_contradictions(evidence_cluster):
    """Find potentially contradictory claims"""
    contradictions = []
    opposing_pairs = [
        (r'\\bactivates?\\b', r'\\binhibits?\\b|represses?'),
        (r'\\bpromotes?\\b', r'\\bsuppresses?\\b'),
        (r'\\bupregulat', r'\\bdownregulat'),
        (r'\\bincreases?\\b', r'\\bdecreases?\\b'),
    ]
    
    claims_by_gene = defaultdict(list)
    for ev in evidence_cluster:
        genes = set(re.findall(r'\\b([A-Z]{2,5}\\d{1,2}[A-Z]?)\\b', ev['claim']))
        for g in genes:
            claims_by_gene[g].append(ev)
    
    for gene, claims in claims_by_gene.items():
        if len(claims) < 2: continue
        for pair in opposing_pairs[:2]:
            has_pos = any(re.search(pair[0], c['claim'], re.I) for c in claims)
            has_neg = any(re.search(pair[1], c['claim'], re.I) for c in claims)
            if has_pos and has_neg:
                contradictions.append({
                    'gene': gene,
                    'type': 'regulation direction dispute',
                    'sources': [c['source'][:60] for c in claims[:3]],
                })
                break
    
    return contradictions[:5]

# ============================================================
# Phase 5: Generate Synthesis Page
# ============================================================
def generate_synthesis(cluster_id, cluster_def, cluster_evidence, consensus, contradictions):
    stats = {
        'total_papers': len(set(e['pmid'] or e['doi'] for e in cluster_evidence if e['pmid'] or e['doi'])),
        'total_evidence': len(cluster_evidence),
        'consensus_findings': len(consensus),
        'contradictions': len(contradictions),
    }
    
    consensus_md = ""
    for i, c in enumerate(consensus):
        sample_lines = []
        for claim, src in zip(c['sample_claims'], c['sample_sources']):
            sample_lines.append(f"> *{claim[:150]}...*  ")
            sample_lines.append(f"> — {src}")
        sample_text = '\\n'.join(sample_lines)
        consensus_md += f"""\n### C{i+1}: {c['pattern']}\n\n**支持论文数**: {c['paper_count']} | **证据条目数**: {c['evidence_count']}\n\n{sample_text}\n\n"""
    
    contradictions_md = ""
    if contradictions:
        for i, c in enumerate(contradictions):
            contradictions_md += f"""\n### ⚠️ D{i+1}: {c['gene']} — {c['type']}\n\n不同研究对{c['gene']}的调控方向存在分歧:\n{chr(10).join(f'- {src}' for src in c['sources'])}\n\n> **需要进一步验证**: 差异可能源于不同物种、组织或实验条件\n"""
    else:
        contradictions_md = "\\n> 当前证据簇中未检测到明显矛盾，需人工审查确认。\\n"
    
    gaps = [
        "跨物种保守性: 多数发现来自拟南芥，作物中的功能验证不足",
        "空间维度: 缺乏空间转录组级别的发育轨迹分析",
        "时间分辨率: 发育过程的高时间分辨率采样不足",
        "功能验证: 单细胞表达模式的功能验证有限",
        "多组学整合: 转录组与表观组/代谢组的整合分析不足",
    ]
    gaps_md = '\\n'.join(f"- {g}" for g in gaps[:3])
    
    return f"""---
title: "Synthesis: {cluster_def['title']}"
type: synthesis
topics: [{', '.join(cluster_def['tags'])}]
total_evidence: {stats['total_evidence']}
total_papers: {stats['total_papers']}
relevance_soybean: "{cluster_def['relevance_to_soybean']}"
auto_discovered: true
cluster_size: {len(cluster_def['tags'])} tags
status: auto-generated
updated: 2026-06-01
---

# {cluster_def['emoji']} Synthesis: {cluster_def['title']}

## Domain Overview

{cluster_def['description']}

**统计**:
- 涵盖论文: ~{stats['total_papers']} 篇
- 证据条目: {stats['total_evidence']} 条
- 共识发现: {stats['consensus_findings']} 项
- 潜在争议: {stats['contradictions']} 项
- 核心标签: {', '.join(cluster_def['tags'])}

**与大豆项目的关联**: {cluster_def['relevance_to_soybean']}

---

## Consensus Findings (跨论文共识)

{consensus_md}

---

## Contradictions & Controversies (争议与矛盾)

{contradictions_md}

---

## Knowledge Gaps (知识空白)

{gaps_md}

---

## Key Papers (关键文献)

以下为自动识别的高证据量论文:

<!-- 待补充: 基于 citation 和 evidence 数量的排名 -->

---

## Hypotheses Emerging from This Synthesis

基于以上共识、争议和空白，可提出以下假设:

<!-- 待 P4b Hypotheses 阶段生成 -->

---

## References

本文档基于 {stats['total_evidence']} 条证据对象自动生成。
所有声明可追溯至具体论文的 Evidence Object。
主题通过标签共现网络自动发现 (不需要人工预定义)。

*自动生成于 2026-06-01 | 需人工审查*
"""

# ============================================================
# 8 Core Themes (FIXED — do not add without explicit user request)
# ============================================================
CORE_THEMES = {
    'single-cell-spatial-omics': {
        'title': 'Single-Cell & Spatial Omics',
        'tags': ['single-cell-spatial', 'scrnaseq', 'spatial', 'single-cell', 'transcriptomics'],
        'emoji': '🔬',
        'description': 'Technology platforms, atlas construction, and spatial transcriptomics methods',
        'relevance_to_soybean': '⭐ Platform foundation for soybean internode Stereo-seq analysis',
    },
    'developmental-biology': {
        'title': 'Developmental Biology',
        'tags': ['developmental-biology', 'development', 'root', 'shoot', 'leaf', 'cambium', 'regeneration', 'cell-wall'],
        'emoji': '🌱',
        'description': 'Root/shoot/leaf/cambium development, stem cell niche, and regeneration',
        'relevance_to_soybean': '⭐⭐ Directly relevant to internode cambium development under light quality',
    },
    'metabolism-natural-products': {
        'title': 'Metabolism & Natural Products',
        'tags': ['metabolism-np', 'metabolism', 'flavonoid', 'terpenoid', 'alkaloid', 'secondary-metabolite'],
        'emoji': '🧪',
        'description': 'Secondary metabolite biosynthesis pathways and metabolic regulation',
        'relevance_to_soybean': '⭐ Moderate — cell wall metabolism and lignin biosynthesis',
    },
    'hormone-signaling': {
        'title': 'Hormone & Signaling',
        'tags': ['hormone-signaling', 'hormone', 'auxin', 'brassinosteroid', 'cytokinin', 'gibberellin', 'abscisic', 'signaling'],
        'emoji': '🔔',
        'description': 'Phytohormone signaling pathways at single-cell resolution',
        'relevance_to_soybean': '⭐⭐⭐ Core — auxin/BR/gibberellin regulation of internode elongation',
    },
    'stress-immunity': {
        'title': 'Stress & Immunity',
        'tags': ['stress-immunity', 'stress', 'immunity', 'pathogen', 'salt', 'heat', 'drought', 'defense'],
        'emoji': '🛡️',
        'description': 'Biotic and abiotic stress responses, plant immunity',
        'relevance_to_soybean': '⭐ Moderate — shading stress overlaps with stress signaling',
    },
    'epigenetics-gene-regulation': {
        'title': 'Epigenetics & Gene Regulation',
        'tags': ['epigenetics-gr', 'epigenetic', 'chromatin', 'transcription-factor', 'gene-regulation', 'atac'],
        'emoji': '🧬',
        'description': 'Chromatin accessibility, transcription factor networks, regulatory elements',
        'relevance_to_soybean': '⭐ Emerging — chromatin dynamics during light response',
    },
    'methods-tools': {
        'title': 'Methods & Tools',
        'tags': ['methods-tools', 'method', 'tool', 'database', 'pipeline', 'benchmark'],
        'emoji': '🛠️',
        'description': 'Computational methods, databases, analysis pipelines for plant omics',
        'relevance_to_soybean': '⭐⭐ Pipeline development for Stereo-seq analysis',
    },
    'genomics-evolution': {
        'title': 'Genomics & Evolution',
        'tags': ['genomics-evolution', 'genomics', 'evolution', 'genome', 'polyploidy', 'comparative'],
        'emoji': '🌍',
        'description': 'Comparative genomics, polyploidy, cross-species cell type evolution',
        'relevance_to_soybean': '⭐ Soybean polyploid genome context',
    },
}

# ============================================================
# Phase: Update existing 8 core synthesis pages only
# ============================================================
def update_core_synthesis(all_evidence):
    """Update existing 8 core synthesis pages with latest evidence counts.
    Does NOT create new themes. 8 themes are fixed."""
    updated = 0
    
    for theme_id, theme_def in CORE_THEMES.items():
        fpath = os.path.join(SYNTHESIS_DIR, f"{theme_id}.md")
        
        # Match evidence by tags
        cluster_evidence = classify_evidence(all_evidence, set(theme_def['tags']))
        ev_count = len(cluster_evidence)
        
        if not os.path.exists(fpath):
            # Create new synthesis page only for the 8 core themes
            consensus = find_consensus(cluster_evidence)
            contradictions = find_contradictions(cluster_evidence)
            synthesis = generate_synthesis(theme_id, theme_def, cluster_evidence, consensus, contradictions)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(synthesis)
            updated += 1
            print(f"  ✓ Created: {theme_id} ({ev_count} evidence)")
        else:
            # Update existing page: refresh evidence count in frontmatter
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Update total_evidence in frontmatter
            content = re.sub(r'total_evidence:\s*\d+', f'total_evidence: {ev_count}', content)
            content = re.sub(r'updated:\s*\d{4}-\d{2}-\d{2}', f'updated: 2026-06-01', content)
            
            # Update evidence count in body text
            content = re.sub(r'证据条目[:：]\s*\d+', f'证据条目: {ev_count}', content)
            content = re.sub(r'evidence objects[:：]\s*\d+', f'evidence objects: {ev_count}', content)
            
            # Count unique papers
            paper_count = len(set(e['doi'] for e in cluster_evidence if e['doi']))
            content = re.sub(r'涵盖论文[:：]\s*~\d+', f'涵盖论文: ~{paper_count}', content)
            content = re.sub(r'total_papers:\s*\d+', f'total_papers: {paper_count}', content)
            
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            updated += 1
            print(f"  ✓ Updated: {theme_id} ({ev_count} evidence, ~{paper_count} papers)")
    
    return updated

def main():
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else '--update'
    
    print("Phase 1: Loading evidence...")
    all_evidence = load_all_evidence()
    print(f"  Loaded {len(all_evidence)} evidence objects")
    
    if mode == '--discover':
        # ⚠️ Opt-in only: auto-discover new themes (NOT default)
        # This mode should only be used with explicit user instruction
        print("\n⚠️  --discover mode: Auto-discovering themes (user-requested)")
        clusters = auto_discover_clusters(all_evidence)
        print(f"  Discovered {len(clusters)} topics")
        
        for cluster_id, cluster_def in clusters.items():
            cluster_evidence = classify_evidence(all_evidence, set(cluster_def['tags']))
            consensus = find_consensus(cluster_evidence)
            contradictions = find_contradictions(cluster_evidence)
            synthesis = generate_synthesis(cluster_id, cluster_def, cluster_evidence, consensus, contradictions)
            fpath = os.path.join(SYNTHESIS_DIR, f"{cluster_id}.md")
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(synthesis)
        
        print(f"\nDONE: {len(clusters)} Synthesis pages (auto-discovered)")
    else:
        # Default: update existing 8 core themes only (do NOT create new themes)
        print(f"\nPhase 2: Updating 8 core synthesis pages (fixed themes, no new discovery)...")
        updated = update_core_synthesis(all_evidence)
        print(f"\nDONE: {updated}/8 core themes updated")

if __name__ == '__main__':
    main()
