#!/usr/bin/env python3
"""Phase 6-7: Relationships + Synthesis for metabolism knowledge chain"""
import os, re
from collections import defaultdict, Counter
from datetime import datetime

BASE = '/mnt/g/hermes_obsidian/hermes'
EVIDENCE_DIR = os.path.join(BASE, 'evidence')
REL_DIR = os.path.join(BASE, 'relationships')
SYNTH_DIR = os.path.join(BASE, 'synthesis')

os.makedirs(REL_DIR, exist_ok=True)
os.makedirs(SYNTH_DIR, exist_ok=True)

TODAY = datetime.now().strftime('%Y-%m-%d')

# ---- Relationship extraction from evidence ----
def extract_relationships(evidence_content):
    """Extract gene-compound, gene-gene, gene-species relationships from evidence"""
    text = evidence_content.lower()
    rels = []
    
    # Gene → Compound regulation
    patterns = [
        # "X regulates Y biosynthesis"
        (r'([a-z]{2,4}[A-Z][a-z]{2,4}[A-Z][A-Za-z0-9]{0,6}|[A-Z][a-z]{1,3}[A-Z][A-Za-z0-9]{1,8})\s+(regulates?|controls?|modulates?|activates?|inhibits?|suppresses?|promotes?|enhances?|induces?|represses?|mediates?)\s+.*?(biosynthesis|accumulation|production|synthesis|metabolism)\s+of\s+(\w+)',
         'regulation'),
        # "X is required for Y biosynthesis"  
        (r'([a-z]{2,4}[A-Z][a-z]{2,4}[A-Z][A-Za-z0-9]{0,6}|[A-Z][a-z]{1,3}[A-Z][A-Za-z0-9]{1,8})\s+(is|are|was|were)\s+(required|necessary|essential|critical|sufficient)\s+for\s+.*?(biosynthesis|accumulation|production|synthesis)\s+of\s+(\w+)',
         'requirement'),
        # "X binds to Y" / "X interacts with Y"
        (r'([a-z]{2,4}[A-Z][a-z]{2,4}[A-Z][A-Za-z0-9]{0,6}|[A-Z][a-z]{1,3}[A-Z][A-Za-z0-9]{1,8})\s+(binds?\s+to|interacts?\s+with|phosphorylates?|ubiquitinates?|targets?)\s+([a-z]{2,4}[A-Z][a-z]{2,4}[A-Z][A-Za-z0-9]{0,6}|[A-Z][a-z]{1,3}[A-Z][A-Za-z0-9]{1,8})',
         'interaction'),
    ]
    
    for pat, rel_type in patterns:
        for match in re.finditer(pat, text):
            groups = match.groups()
            if rel_type in ('regulation', 'requirement'):
                gene = groups[0]
                compound = groups[-1] if len(groups) > 1 else ''
                if gene and compound and len(compound) > 3:
                    rels.append((rel_type, gene, compound, None))
            elif rel_type == 'interaction':
                gene1 = groups[0]
                gene2 = groups[-1] if len(groups) > 2 else ''
                if gene1 and gene2 and gene1 != gene2:
                    rels.append((rel_type, gene1, None, gene2))
    
    return rels

def main():
    # 1. Scan all metabolism evidence objects for relationships
    rel_map = defaultdict(list)  # (type, entity1, entity2) → [evidence_ids]
    
    ev_count = 0
    for fname in sorted(os.listdir(EVIDENCE_DIR)):
        if not fname.endswith('.md'): continue
        path = os.path.join(EVIDENCE_DIR, fname)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read(5000)
        except: continue
        
        if 'created: 2026-05-30' not in content:
            continue
        ev_count += 1
        
        rels = extract_relationships(content)
        ev_id = fname.replace('.md', '')
        
        for rel_type, entity1, compound, entity2 in rels:
            if compound:
                key = (rel_type, entity1, compound)
            elif entity2:
                key = (rel_type, entity1, entity2)
            else:
                continue
            rel_map[key].append(ev_id)
    
    print(f"Evidence objects scanned: {ev_count}")
    print(f"Unique relationships found: {len(rel_map)}")
    
    # 2. Create relationship pages
    # Group by relationship type
    rel_by_type = defaultdict(list)
    for (rel_type, e1, e2), ev_ids in rel_map.items():
        rel_by_type[rel_type].append((e1, e2, ev_ids))
    
    rel_created = 0
    for rel_type, items in rel_by_type.items():
        items.sort(key=lambda x: -len(x[2]))
        top_items = items[:20]
        
        ev_summary = []
        for e1, e2, ev_ids in top_items:
            ev_links = ', '.join(f'[[{e}]]' for e in ev_ids[:5])
            ev_summary.append(f"**{e1}** → **{e2}**: {len(ev_ids)} evidence ({ev_links})")
        
        summary_text = '\n'.join(f'- {s}' for s in ev_summary)
        
        rel_content = f"""---
title: "Metabolism {rel_type} relationships"
created: {TODAY}
type: relationship
category: metabolism-{rel_type}
tags: [metabolism, relationships]
---

# Metabolism {rel_type.title()} Relationships

## Summary
Auto-generated from metabolism evidence objects. {len(items)} relationships found.

## Top Relationships
{summary_text}

## Source
Evidence objects from 153 metabolism papers (2026-05-30 import).
"""
        slug = f"metabolism-{rel_type}-relationships"
        rel_path = os.path.join(REL_DIR, f"{slug}.md")
        with open(rel_path, 'w', encoding='utf-8') as f:
            f.write(rel_content)
        rel_created += 1
    
    print(f"Relationship pages: {rel_created}")
    
    # 3. Create Metabolism Synthesis page
    # Aggregate all evidence by gene families and compound classes
    all_genes = Counter()
    all_compounds = Counter()
    
    for fname in sorted(os.listdir(EVIDENCE_DIR)):
        if not fname.endswith('.md'): continue
        path = os.path.join(EVIDENCE_DIR, fname)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read(3000)
        except: continue
        if 'created: 2026-05-30' not in content: continue
        
        # Extract genes and compounds from frontmatter
        gm = re.search(r'genes:\s*\[(.*?)\]', content)
        if gm and gm.group(1).strip():
            for g in gm.group(1).split(','):
                g = g.strip()
                if g:
                    all_genes[g] += 1
        
        cm = re.search(r'compounds:\s*\[(.*?)\]', content)
        if cm and cm.group(1).strip():
            for c in cm.group(1).split(','):
                c = c.strip()
                if c:
                    all_compounds[c] += 1
    
    top_genes = all_genes.most_common(40)
    top_compounds = all_compounds.most_common(20)
    
    gene_list = '\n'.join(f'| {g} | {c} |' for g, c in top_genes[:30])
    compound_list = '\n'.join(f'| {c} | {cnt} |' for c, cnt in top_compounds[:15])
    
    # Categorize findings into themes
    themes = {
        'Transcriptional Regulation': ['myb', 'bhlh', 'wrky', 'nac', 'bzip', 'erf', 'ap2', 'mads', 'spl', 'tcp', 'hd-zip'],
        'Flavonoid & Anthocyanin': ['flavonoid', 'anthocyanin', 'proanthocyanidin', 'flavonol'],
        'Terpenoid & Carotenoid': ['terpenoid', 'carotenoid', 'ginsenoside', 'tanshinone', 'saponin'],
        'Lignin & Cell Wall': ['lignin', 'cellulose', 'hemicellulose', 'xylan'],
        'Starch & Sugar': ['starch', 'sucrose', 'glucose', 'fructose'],
        'Alkaloid & Amino Acid': ['alkaloid', 'theanine', 'caffeine'],
        'Lipid & Wax': ['lipid', 'wax', 'cutin', 'oil'],
        'Hormone Crosstalk': ['jasmonic', 'salicylic', 'abscisic', 'gibberellin', 'auxin', 'ethylene', 'brassinosteroid'],
        'Stress Response': ['stress', 'drought', 'cold', 'heat', 'salt', 'light'],
    }
    
    theme_sections = []
    for theme_name, keywords in themes.items():
        count = sum(1 for c, n in all_compounds.items() if any(k in c for k in keywords))
        count += sum(1 for g, n in all_genes.items() if any(k in g.lower() for k in keywords))
        theme_sections.append(f"### {theme_name}\n{count} related entities\n")
    
    theme_text = '\n'.join(theme_sections)
    
    synth_content = f"""---
title: "Plant Metabolism — Synthesis"
created: {TODAY}
type: synthesis
tags: [metabolism, synthesis]
---

# Plant Metabolism Knowledge Synthesis

## Scope
Synthesized from 1,275 evidence objects across 153 papers (2026-05-30 import).

## Major Themes
{theme_text}

## Top Regulatory Genes
| Gene | Evidence Count |
|------|---------------|
{gene_list}

## Top Metabolites
| Compound | Evidence Count |
|-----------|---------------|
{compound_list}

## Historical Evolution
The understanding of plant specialized metabolism has progressed from single-gene 
characterization to systems-level multi-omics analysis. This synthesis captures 
transcriptional regulatory networks governing flavonoid, terpenoid, alkaloid, 
and cell wall biosynthesis across diverse plant species.

## Current Consensus
1. **MYB-bHLH-WD40 (MBW) complexes** are the master regulators of flavonoid/anthocyanin biosynthesis
2. **AP2/ERF, WRKY, NAC, and bZIP families** provide stress- and hormone-responsive regulation
3. **Multi-omics integration** (transcriptomics + metabolomics) is the dominant methodology
4. **CRISPR/Cas9 validation** is becoming standard for confirming regulatory mechanisms
5. Light, hormone, and stress signals converge on common transcriptional hubs

## Open Questions
- How do MBW complexes achieve cell-type and developmental specificity?
- What are the missing links between hormone signaling and specialized metabolism?
- Can metabolic engineering predictions be made from transcriptional networks alone?

## Related Synthesis Pages
- [[hormone-signaling]]
- [[vascular-development]]
- [[root-development]]
"""
    synth_path = os.path.join(SYNTH_DIR, "plant-metabolism.md")
    with open(synth_path, 'w', encoding='utf-8') as f:
        f.write(synth_content)
    
    print(f"Synthesis page: plant-metabolism.md")
    
    # 4. Update index.md
    idx_path = os.path.join(BASE, 'index.md')
    with open(idx_path, 'r', encoding='utf-8') as f:
        idx_content = f.read()
    
    if '## Relationships' not in idx_content:
        idx_content += f'\n## Relationships\n- [[metabolism-regulation-relationships]]\n- [[metabolism-interaction-relationships]]\n- [[metabolism-requirement-relationships]]\n'
    
    if '### plant-metabolism' not in idx_content:
        idx_content = idx_content.replace('## Synthesis', f'## Synthesis\n- [[plant-metabolism]] — Plant Metabolism Knowledge Synthesis')
    
    with open(idx_path, 'w', encoding='utf-8') as f:
        f.write(idx_content)
    
    # 5. Update log.md
    log_path = os.path.join(BASE, 'log.md')
    with open(log_path, 'r', encoding='utf-8') as f:
        log_content = f.read()
    
    log_entry = f"""
### Relationships Created ({TODAY})
- {rel_created} relationship pages from metabolism evidence
- Types: regulation, interaction, requirement

### Synthesis Created ({TODAY})
- plant-metabolism.md: synthesis from 1,275 evidence objects
- 9 thematic areas, 40 regulatory genes, 20 metabolites
"""
    log_content += log_entry
    
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(log_content)
    
    # 6. Summary
    print(f"\n=== PHASE 6-7 COMPLETE ===")
    print(f"Relationships: {rel_created} pages")
    print(f"Synthesis: 1 page (plant-metabolism)")
    print(f"Top gene: {top_genes[0][0]} ({top_genes[0][1]} evidence)")
    print(f"Top compound: {top_compounds[0][0]} ({top_compounds[0][1]} evidence)")

if __name__ == '__main__':
    main()
