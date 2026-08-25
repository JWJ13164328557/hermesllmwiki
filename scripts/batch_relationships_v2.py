#!/usr/bin/env python3
"""Phase 6 v2: Extract relationships from evidence frontmatter genes/compounds fields"""
import os, re
from collections import defaultdict, Counter
from datetime import datetime

BASE = '/mnt/g/hermes_obsidian/hermes'
EVIDENCE_DIR = os.path.join(BASE, 'evidence')
REL_DIR = os.path.join(BASE, 'relationships')

os.makedirs(REL_DIR, exist_ok=True)
TODAY = datetime.now().strftime('%Y-%m-%d')

def main():
    # Build gene→compound relationships from evidence frontmatter
    gene_compound = defaultdict(Counter)  # gene → {compound: count}
    gene_gene = defaultdict(Counter)      # gene → {gene2: count}
    gene_evidence = defaultdict(list)     # gene → [evidence_ids]
    
    ev_processed = 0
    for fname in sorted(os.listdir(EVIDENCE_DIR)):
        if not fname.endswith('.md'): continue
        path = os.path.join(EVIDENCE_DIR, fname)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read(5000)
        except: continue
        
        if 'created: 2026-05-30' not in content:
            # 2026-08-25 修复: 原硬编码只处理 2026-05-30 创建的证据(反模式),
            # 导致后续 evidence 全被跳过 → relationships 层一直为空(审稿 B4 发现)
            pass  # 移除日期硬编码过滤, 处理全部 evidence
        
        ev_slug = fname.replace('.md', '')
        ev_processed += 1
        
        # Extract genes from frontmatter
        gm = re.search(r'genes:\s*\[(.*?)\]', content)
        genes = []
        if gm and gm.group(1).strip():
            genes = [g.strip() for g in gm.group(1).split(',') if g.strip()]
        
        # Extract compounds from frontmatter
        cm = re.search(r'compounds:\s*\[(.*?)\]', content)
        compounds = []
        if cm and cm.group(1).strip():
            compounds = [c.strip() for c in cm.group(1).split(',') if c.strip()]
        
        # Build relationships
        for g in genes:
            gene_evidence[g].append(ev_slug)
            for c in compounds:
                gene_compound[g][c] += 1
            for g2 in genes:
                if g != g2:
                    gene_gene[g][g2] += 1
    
    print(f"Evidence processed: {ev_processed}")
    print(f"Unique genes: {len(gene_evidence)}")
    print(f"Gene-compound pairs: {sum(len(v) for v in gene_compound.values())}")
    
    # 1. Create gene→compound relationship page
    gc_rows = []
    for gene, compounds in sorted(gene_compound.items(), key=lambda x: -sum(x[1].values()))[:30]:
        top_compounds = compounds.most_common(5)
        ev_ids = gene_evidence.get(gene, [])[:5]
        ev_links = ', '.join(f'[[{e}]]' for e in ev_ids)
        comp_str = ', '.join(f'{c}({n})' for c, n in top_compounds)
        gc_rows.append(f'| [[{gene.lower()}]] | {comp_str} | {sum(compounds.values())} | {ev_links} |')
    
    gc_table = '\n'.join(gc_rows)
    
    gc_content = f"""---
title: "Gene-Compound Regulatory Relationships (Metabolism)"
created: {TODAY}
type: relationship
category: metabolism-gene-compound
tags: [metabolism, relationships]
---

# Gene → Compound Regulatory Relationships

## Summary
{len(gene_compound)} genes linked to compounds across {ev_processed} evidence objects.

## Top Gene-Compound Pairs
| Gene | Compounds | Evidence | Source |
|------|-----------|----------|--------|
{gc_table}

## Notes
- Generated from metabolism evidence (2026-05-30 import)
- Compound association strength = co-occurrence in evidence
"""
    with open(os.path.join(REL_DIR, 'metabolism-gene-compound.md'), 'w', encoding='utf-8') as f:
        f.write(gc_content)
    
    # 2. Create gene co-occurrence network page
    gg_rows = []
    for gene, partners in sorted(gene_gene.items(), key=lambda x: -sum(x[1].values()))[:30]:
        top_partners = partners.most_common(5)
        partner_str = ', '.join(f'{p}({n})' for p, n in top_partners if sum(partners.values()) > 1)
        if partner_str:
            ev_ids = gene_evidence.get(gene, [])[:3]
            ev_links = ', '.join(f'[[{e}]]' for e in ev_ids)
            gg_rows.append(f'| [[{gene.lower()}]] | {partner_str} | {ev_links} |')
    
    gg_table = '\n'.join(gg_rows[:25])
    
    gg_content = f"""---
title: "Gene Co-occurrence Network (Metabolism)"
created: {TODAY}
type: relationship
category: metabolism-gene-gene
tags: [metabolism, relationships, network]
---

# Gene Co-occurrence Network

## Summary
Genes frequently mentioned together in the same evidence objects — suggesting 
functional association in metabolic pathways.

| Gene | Co-occurring Genes | Source |
|------|--------------------|--------|
{gg_table}

## Notes
- Co-occurrence does not imply direct interaction
- Generated from {ev_processed} metabolism evidence objects
"""
    with open(os.path.join(REL_DIR, 'metabolism-gene-network.md'), 'w', encoding='utf-8') as f:
        f.write(gg_content)
    
    rel_created = 2
    print(f"Relationship pages: {rel_created}")
    
    # 3. Top genes summary
    top_genes = sorted(gene_evidence.items(), key=lambda x: -len(x[1]))[:30]
    print(f"\nTop genes:")
    for g, evs in top_genes[:15]:
        n_compounds = len(gene_compound.get(g, {}))
        print(f"  {g}: {len(evs)} evidence, {n_compounds} compounds")
    
    # 4. Update index.md
    idx_path = os.path.join(BASE, 'index.md')
    with open(idx_path, 'r', encoding='utf-8') as f:
        idx_content = f.read()
    
    relationships_section = '\n## Relationships\n- [[metabolism-gene-compound]] — Gene-Compound Regulatory Relationships\n- [[metabolism-gene-network]] — Gene Co-occurrence Network\n'
    if '## Relationships' not in idx_content:
        idx_content += relationships_section
    else:
        # replace existing
        idx_content = re.sub(r'## Relationships.*?(?=\n## |\Z)', relationships_section.strip(), idx_content, flags=re.DOTALL)
    
    with open(idx_path, 'w', encoding='utf-8') as f:
        f.write(idx_content)
    
    # 5. Log
    log_path = os.path.join(BASE, 'log.md')
    with open(log_path, 'r', encoding='utf-8') as f:
        log_content = f.read()
    
    log_content += f"""
### Relationships ({TODAY})
- metabolism-gene-compound: {len(gene_compound)} gene-compound pairs
- metabolism-gene-network: gene co-occurrence from {ev_processed} evidence
- Top gene: {top_genes[0][0]} ({len(top_genes[0][1])} evidence)
"""
    
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(log_content)
    
    print(f"\n=== DONE ===")
    print(f"Relationships: 2 pages")
    print(f"Gene-compound pairs: {sum(len(v) for v in gene_compound.values())}")
    print(f"Genes with evidence: {len(gene_evidence)}")

if __name__ == '__main__':
    main()
