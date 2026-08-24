#!/usr/bin/env python3
"""Phase 8: 全量 Hypothesis + Research Program 自动生成
从 Synthesis → 证据聚类 → 假说 → 研究计划"""
import os, re, json
from collections import defaultdict, Counter
from datetime import datetime

BASE = '/mnt/g/hermes_obsidian/hermes'
SYNTHESIS_DIR = os.path.join(BASE, 'synthesis')
EVIDENCE_DIR = os.path.join(BASE, 'evidence')
HYPOTHESES_DIR = os.path.join(BASE, 'hypotheses')
PROGRAMS_DIR = os.path.join(BASE, 'research-programs')

os.makedirs(HYPOTHESES_DIR, exist_ok=True)
os.makedirs(PROGRAMS_DIR, exist_ok=True)

TODAY = datetime.now().strftime('%Y-%m-%d')

SOYBEAN_KEYWORDS = [
    'soybean', 'glycine', 'legume', 'internode', 'cambium', 'vascular',
    'light quality', 'shade', 'phytochrome', 'photomorphogen',
    'stem', 'wood', 'xylem', 'phloem', 'secondary growth',
    'auxin', 'gibberellin', 'brassinosteroid', 'cell wall',
]

SPECIES_ABBREV = {
    'Arabidopsis thaliana': 'At', 'Oryza sativa': 'Os', 'Zea mays': 'Zm',
    'Glycine max': 'Gm', 'Solanum lycopersicum': 'Sl', 'Nicotiana tabacum': 'Nt',
    'Populus spp.': 'Pt', 'Medicago spp.': 'Mt', 'Triticum aestivum': 'Ta',
    'Brassica napus': 'Bn', 'Vitis vinifera': 'Vv', 'Gossypium hirsutum': 'Gh',
}


def load_evidence():
    """Load all evidence objects with claims and tags"""
    evidence = []
    for fname in sorted(os.listdir(EVIDENCE_DIR)):
        if not fname.endswith('.md'): continue
        fpath = os.path.join(EVIDENCE_DIR, fname)
        try:
            with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
        except:
            continue

        # Extract claim
        claim = ''
        cm = re.search(r'## Claim\n(.+?)(?=\n##|\Z)', content, re.DOTALL)
        if cm:
            claim = cm.group(1).strip()[:500]

        # Extract tags
        tags = []
        tm = re.search(r'tags:\s*\[(.+?)\]', content)
        if tm:
            tags = [t.strip().strip('"\'') for t in tm.group(1).split(',')]

        # Extract quality
        quality = 'unknown'
        qm = re.search(r'\*\*Level\*\*:\s*(.+)', content)
        if qm:
            quality = qm.group(1).strip()

        evidence.append({
            'id': fname.replace('.md', ''),
            'claim': claim,
            'tags': tags,
            'quality': quality,
        })

    return evidence


def load_synthesis():
    """Load all synthesis pages"""
    synth = []
    for fname in sorted(os.listdir(SYNTHESIS_DIR)):
        if not fname.endswith('.md'): continue
        fpath = os.path.join(SYNTHESIS_DIR, fname)
        try:
            with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
        except:
            continue

        # Extract frontmatter
        title = ''
        tm = re.search(r'title:\s*"(.+?)"', content)
        if tm: title = tm.group(1)

        topics = []
        topm = re.search(r'topics:\s*\[(.+?)\]', content)
        if topm:
            topics = [t.strip().strip('"\'') for t in topm.group(1).split(',')]
        if not topics:
            # Fallback: topic field
            topm2 = re.search(r'topic:\s*"(.+?)"', content)
            if topm2:
                topics = [topm2.group(1)]

        total_ev = 0
        tem = re.search(r'total_evidence:\s*(\d+)', content)
        if tem: total_ev = int(tem.group(1))

        papers = 0
        pm = re.search(r'total_papers:\s*(\d+)', content)
        if pm: papers = int(pm.group(1))

        soy_relevance = ''
        sm = re.search(r'relevance_soybean:\s*"(.+?)"', content)
        if sm: soy_relevance = sm.group(1)

        synth.append({
            'name': fname.replace('.md', ''),
            'title': title,
            'topics': topics,
            'total_evidence': total_ev,
            'total_papers': papers,
            'soy_relevance': soy_relevance,
            'path': fpath,
        })

    return synth


def group_claims_by_similarity(claims, min_overlap=3):
    """Simple keyword-cooccurrence clustering of claims"""
    # Extract keywords from each claim
    keywords_list = []
    for claim in claims:
        words = set(re.findall(r'[A-Za-z]{4,}', claim.lower()))
        # Filter out stopwords
        stopwords = {'that', 'this', 'with', 'from', 'have', 'been', 'were', 'also',
                     'into', 'more', 'after', 'such', 'than', 'while', 'over', 'both'}
        keywords = words - stopwords
        keywords_list.append(keywords)

    # Build similarity graph
    n = len(claims)
    if n <= 1:
        return [list(range(n))] if n == 1 else []

    # Simple connected components based on keyword overlap
    groups = []
    visited = [False] * n
    for i in range(n):
        if visited[i]:
            continue
        group = [i]
        visited[i] = True
        for j in range(i + 1, n):
            if visited[j]:
                continue
            overlap = len(keywords_list[i] & keywords_list[j])
            if overlap >= min_overlap:
                group.append(j)
                visited[j] = True
        groups.append(group)

    return groups


def formulate_hypothesis(cluster_claims):
    """Formulate a hypothesis from a cluster of related claims"""
    # Pick the strongest claim as the core
    core = cluster_claims[0] if cluster_claims else "unknown mechanism"

    # Extract genes mentioned
    genes = list(set(re.findall(r'\b[A-Z]{2,5}\d{0,2}\b', ' '.join(cluster_claims))))
    genes = [g for g in genes if len(g) >= 3 and g not in
             {'THE', 'AND', 'FOR', 'DNA', 'RNA', 'ATP', 'PCR', 'GFP', 'GUS', 'LUC', 'YFP'}]

    # Identify action verbs
    actions = []
    for pat in [r'(regulates?|controls?|modulates?|activates?|inhibits?|suppresses?|promotes?|enhances?|induces?|represses?)',
                r'(interacts?\s+with|binds?\s+to|phosphorylates?|ubiquitinates?|targets?)',
                r'(is\s+(required|necessary|essential|critical|sufficient)\s+(for|to))',
                r'(plays?\s+a\s+(critical|crucial|key|essential)\s+role)']:
        m = re.search(pat, core, re.I)
        if m:
            actions.append(m.group(1))

    action = actions[0] if actions else 'regulates'

    # Build hypothesis statement
    if genes:
        h = f"{genes[0]} {action} {' and '.join(genes[1:3]) if len(genes) > 1 else 'downstream targets'} to control [process]"
        h = h[:200]
    else:
        h = f"[Key factor] {action} [process] via [mechanism]"

    # Evidence summary
    support = f"Supported by {len(cluster_claims)} independent evidence objects"

    return {
        'statement': h,
        'core_claim': core[:200],
        'genes': genes[:5],
        'action': action,
        'support_count': len(cluster_claims),
        'evidence_summary': support,
    }


def generate_hypothesis_page(synth, hypotheses, evidence_count):
    """Generate hypothesis page content"""
    topic = synth['name']
    title = synth['title'] or f"Hypotheses: {topic}"

    h_list = []
    for i, h in enumerate(hypotheses):
        h_list.append(f"""### Hypothesis {i+1}: {h['genes'][0] if h['genes'] else 'Key mechanism'}

**Statement**: {h['statement']}

**Core Evidence**: {h['core_claim'][:150]}

**Support**: {h['evidence_summary']}
- Genes involved: {', '.join(h['genes']) if h['genes'] else 'unknown'}
- Action: {h['action']}
""")

    h_body = '\n'.join(h_list)

    soy_note = ''
    if synth.get('soy_relevance', '').startswith('高') or synth.get('soy_relevance', '').startswith('中'):
        soy_note = f"""
## 大豆项目关联

**关联度**: {synth['soy_relevance']}

该主题与大豆节间光质响应研究{'直接相关' if '高' in synth.get('soy_relevance', '') else '可提供机制参考'}。
"""

    return f"""---
title: "{title}"
type: hypothesis
topic: "{topic}"
total_evidence: {evidence_count}
total_hypotheses: {len(hypotheses)}
auto_generated: true
updated: {TODAY}
---

# 💡 {title}

## Overview
从 {evidence_count} 条证据中自动发现 {len(hypotheses)} 条假说。

{soy_note}
## Hypotheses

{h_body}

## Validation Strategy

1. **遗传验证**: CRISPR/Cas9 敲除关键基因，表型分析
2. **生化验证**: Co-IP / BiFC 确认蛋白互作，ChIP-qPCR 确认 DNA 结合
3. **时空验证**: 启动子-GUS 报告基因定位表达模式
4. **跨物种保守性**: 在其他模式植物中验证功能保守性

---
*Auto-generated by Phase 8 pipeline on {TODAY}*
"""


def generate_program_page(synth, hypotheses, evidence_count):
    """Generate research program page content"""
    topic = synth['name']
    title = synth['title'] or f"Research Program: {topic}"

    title_short = title.replace(': ', '-').replace(' ', '-')[:60] if title else topic

    aims = []
    for i, h in enumerate(hypotheses):
        genes = h.get('genes', [])
        gene_target = genes[0] if genes else '[target gene]'
        aims.append(f"""### Aim {i+1}: Test {gene_target} function

**Hypothesis**: {h['statement']}

**Experimental Design**:
1. Generate {gene_target} overexpression and CRISPR knockout lines in [model species]
2. Phenotype analysis: [trait measurement], microscopy, histochemical staining
3. RNA-seq of WT vs mutant to identify downstream targets
4. Subcellular localization: {gene_target}-GFP fusion

**Expected Outcomes**: {'Enhanced' if 'promotes' in h.get('action', '') else 'Reduced'} [phenotype] in overexpression lines; opposite in mutants.

**Validation**: Complementation test, tissue-specific expression analysis.
""")

    aims_body = '\n'.join(aims)

    return f"""---
title: "{title}"
type: research-program
topic: "{topic}"
total_evidence: {evidence_count}
total_aims: {len(hypotheses)}
auto_generated: true
updated: {TODAY}
---

# 🔬 {title}

## Program Overview
基于 {evidence_count} 条证据生成的 {len(hypotheses)} 个实验目标。

## Research Aims

{aims_body}

## Timeline & Resources

| Aim | Duration | Key Resources |
|-----|----------|---------------|
"""
    + '\n'.join(f"| {i+1} | 12-18 months | Constructs, phenotyping, RNA-seq |" for i in range(len(hypotheses))) + f"""

## Expected Deliverables

- {len(hypotheses)} research papers / preprints
- Validated gene function data
- RNA-seq datasets (submitted to GEO/SRA)
- Genetic materials available upon request

---
*Auto-generated by Phase 8 pipeline on {TODAY}*
"""


def main():
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else '--update'
    
    # 8 core themes (FIXED — do not add without explicit user request)
    CORE_THEME_IDS = {
        'single-cell-spatial-omics', 'developmental-biology', 'metabolism-natural-products',
        'hormone-signaling', 'stress-immunity', 'epigenetics-gene-regulation',
        'methods-tools', 'genomics-evolution',
    }
    
    print("Phase 8: Hypothesis + Research Program Generation")
    print("=" * 60)

    # Load data
    evidence = load_evidence()
    synth_pages = load_synthesis()
    
    # Filter to 8 core themes only (unless --discover mode)
    if mode != '--discover':
        synth_pages = [s for s in synth_pages if s['name'] in CORE_THEME_IDS]
    
    print(f"Evidence objects: {len(evidence)}")
    print(f"Synthesis pages: {len(synth_pages)} (8 core themes only)")


    # Build tag → evidence index
    tag_to_ev = defaultdict(list)
    for ev in evidence:
        for tag in ev['tags']:
            tag_to_ev[tag].append(ev)

    # Process each synthesis page
    h_count = 0
    p_count = 0
    for synth in synth_pages:
        topic = synth['name']
        tags = synth['topics']
        if not tags:
            print(f"  SKIP {topic}: no tags")
            continue

        # Collect all evidence for this topic's tags
        topic_evidence = []
        seen_ids = set()
        for tag in tags:
            for ev in tag_to_ev.get(tag, []):
                if ev['id'] not in seen_ids:
                    topic_evidence.append(ev)
                    seen_ids.add(ev['id'])

        # Also match by topic name in synthesis tags
        for ev in evidence:
            if topic.replace('-', '') in ''.join(ev['tags']).replace('-', ''):
                if ev['id'] not in seen_ids:
                    topic_evidence.append(ev)
                    seen_ids.add(ev['id'])

        if len(topic_evidence) < 5:
            print(f"  SKIP {topic}: only {len(topic_evidence)} evidence (need ≥5)")
            continue

        # Extract claims
        claims = [ev['claim'] for ev in topic_evidence if len(ev['claim']) > 30]
        if len(claims) < 5:
            print(f"  SKIP {topic}: only {len(claims)} valid claims")
            continue

        # Cluster claims into hypothesis groups
        groups = group_claims_by_similarity(claims, min_overlap=4)
        if not groups:
            print(f"  SKIP {topic}: no clusters found")
            continue

        # Take top 5 clusters with most claims
        groups.sort(key=len, reverse=True)
        top_groups = groups[:5]

        # Formulate hypotheses
        hypotheses = []
        for grp in top_groups:
            cluster_claims = [claims[i] for i in grp]
            h = formulate_hypothesis(cluster_claims)
            hypotheses.append(h)

        # Write hypothesis page
        h_page = generate_hypothesis_page(synth, hypotheses, len(claims))
        h_path = os.path.join(HYPOTHESES_DIR, f"{topic}.md")
        with open(h_path, 'w', encoding='utf-8') as f:
            f.write(h_page)
        h_count += 1

        # Write research program page
        p_page = generate_program_page(synth, hypotheses, len(claims))
        p_path = os.path.join(PROGRAMS_DIR, f"{topic}.md")
        with open(p_path, 'w', encoding='utf-8') as f:
            f.write(p_page)
        p_count += 1

        print(f"  ✓ {topic}: {len(hypotheses)} hypotheses, {len(claims)} evidence")

    print(f"\n=== DONE ===")
    print(f"Hypothesis pages: {h_count}")
    print(f"Research Program pages: {p_count}")


if __name__ == '__main__':
    main()
