#!/usr/bin/env python3
"""为 153 篇代谢论文生成 Evidence Objects + Entity 更新"""
import os, re, json
from collections import defaultdict, Counter
from datetime import datetime

BASE = '/mnt/g/hermes_obsidian/hermes'
CONCEPTS_DIR = os.path.join(BASE, 'concepts', 'papers')
EVIDENCE_DIR = os.path.join(BASE, 'evidence')
ENTITIES_DIR = os.path.join(BASE, 'entities')

# Ensure directories exist
os.makedirs(EVIDENCE_DIR, exist_ok=True)
os.makedirs(ENTITIES_DIR, exist_ok=True)

TODAY = datetime.now().strftime('%Y-%m-%d')

def slugify(text):
    """Create URL-friendly slug from text"""
    s = re.sub(r'[^\w\s-]', '', text.lower())
    s = re.sub(r'\s+', '-', s.strip())
    return s[:80].rstrip('-')

def extract_gene_compounds(text):
    """Extract gene symbols and compound names from finding text"""
    genes = set()
    compounds = set()
    
    # Gene patterns
    gene_patterns = [
        r'\b([A-Z][a-z]{1,3}[A-Z][A-Za-z0-9]{1,8})\b',  # Standard gene: AtMYB2, OsNAC1
        r'\b([a-z]{2,4}[A-Z][a-z]{2,4}[A-Z][A-Za-z0-9]{0,6})\b',  # SlBZR1, MdBT2
    ]
    for pat in gene_patterns:
        for match in re.finditer(pat, text):
            gene = match.group(1)
            # Filter out common non-gene words
            if gene.lower() not in ('the', 'and', 'for', 'was', 'were', 'with', 'that', 'this', 'from', 'have', 'been', 'also', 'into', 'more', 'after', 'such', 'than', 'while', 'over', 'both', 'each', 'most', 'some', 'many', 'between', 'these', 'those', 'other', 'which', 'their', 'about', 'could', 'would', 'should', 'during', 'within', 'through', 'however', 'furthermore', 'moreover', 'therefore', 'because', 'although', 'typically', 'including', 'whereas'):
                genes.add(gene)
    
    # Compound patterns (names that appear in metabolism context)
    compound_patterns = [
        r'\b(flavonoid|flavonol|anthocyanin|proanthocyanidin|carotenoid)\b',
        r'\b(terpenoid|monoterpene|sesquiterpene|diterpene|triterpene)\b',
        r'\b(alkaloid|caffeine|theanine|nicotine)\b',
        r'\b(lignin|cellulose|hemicellulose|xylan|xyloglucan)\b',
        r'\b(starch|sucrose|glucose|fructose|maltose)\b',
        r'\b(phenylpropanoid|phenolic|coumarin)\b',
        r'\b(ginsenoside|tanshinone|artemisinin|taxol|saponin)\b',
        r'\b(wax|cutin|suberin)\b',
        r'\b(jasmonic acid|salicylic acid|abscisic acid|gibberellin|auxin|ethylene|brassinosteroid|strigolactone)\b',
        r'\b(melatonin|serotonin|dopamine)\b',
        r'\b(ascorbic acid|tocopherol|vitamin)\b',
        r'\b(chlorophyll|carotene|lycopene|zeaxanthin)\b',
    ]
    for pat in compound_patterns:
        for match in re.finditer(pat, text, re.I):
            compounds.add(match.group(1).lower())
    
    return list(genes)[:5], list(compounds)[:5]

def extract_findings_from_concept(content):
    """Extract numbered findings from the 深度提炼 section"""
    depth_sec = re.search(r'### 核心发现\n(.+?)(?=\n## (?!###)|## 相关|\n---|\Z)', content, re.DOTALL)
    if not depth_sec:
        return []
    
    findings = []
    for line in depth_sec.group(1).split('\n'):
        line = line.strip()
        if re.match(r'^\d+\.\s', line):
            finding = re.sub(r'^\d+\.\s*', '', line)
            if len(finding) > 30:
                findings.append(finding)
    return findings

def generate_evidence_id(paper_slug, finding_idx):
    """Generate unique evidence ID"""
    return f"{paper_slug}-f{finding_idx+1}"

def main():
    # 1. Scan all metabolism papers for findings
    papers_findings = []
    for fname in sorted(os.listdir(CONCEPTS_DIR)):
        if not fname.endswith('.md'): continue
        path = os.path.join(CONCEPTS_DIR, fname)
        try:
            with open(path, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
        except: continue
        
        # Process ALL papers that have deep curation findings
        if '### 核心发现' not in content:
            continue
        
        # Extract slug and title
        slug = fname.replace('.md', '')
        title_m = re.search(r'^# (.+)$', content, re.M)
        title = title_m.group(1) if title_m else slug
        
        # Extract species and tags
        species = []
        sm = re.search(r'\*\*物种\*\*:\s*(.+?)$', content, re.M)
        if sm: species = [s.strip() for s in sm.group(1).split(',')]
        
        tags = []
        tm = re.search(r'tags:\s*\[(.*?)\]', content)
        if tm: tags = [t.strip() for t in tm.group(1).split(',')]
        
        # Extract DOI
        doi = ''
        dm = re.search(r'doi:\s*(10\.\d{4,}/[^\s\n]+)', content, re.I)
        if dm: doi = dm.group(1).rstrip('/')
        
        findings = extract_findings_from_concept(content)
        if findings:
            papers_findings.append({
                'slug': slug, 'title': title, 'species': species,
                'tags': tags, 'doi': doi, 'findings': findings,
                'path': path
            })
    
    print(f"Papers with findings: {len(papers_findings)}")
    total_findings = sum(len(p['findings']) for p in papers_findings)
    print(f"Total findings: {total_findings}")
    
    # 2. Create evidence objects
    evidence_created = 0
    entity_genes = defaultdict(list)    # gene → [evidence_ids]
    entity_compounds = defaultdict(list) # compound → [evidence_ids]
    
    for paper in papers_findings:
        for idx, finding in enumerate(paper['findings']):
            ev_id = generate_evidence_id(paper['slug'], idx)
            genes, compounds = extract_gene_compounds(finding)
            
            # Track entities
            for g in genes:
                entity_genes[g].append((ev_id, finding[:100]))
            for c in compounds:
                entity_compounds[c].append((ev_id, finding[:100]))
            
            # Create evidence page
            species_str = ', '.join(paper['species'][:3]) if paper['species'] else 'Plant'
            tags_str = ', '.join(paper['tags'][:4]) if paper['tags'] else 'metabolism'
            
            # Evidence quality assessment
            quality = 'medium'
            evidence_type = 'expression/regulation'
            if re.search(r'(knockout|knockdown|mutant|crispr|overexpression)', finding, re.I):
                quality = 'high'
                evidence_type = 'genetic perturbation'
            elif re.search(r'(co-ip|y2h|bifc|pull-down|interact)', finding, re.I):
                evidence_type = 'protein interaction'
            elif re.search(r'(chip|emsa|luciferase|reporter|promoter)', finding, re.I):
                evidence_type = 'DNA binding/regulation'
            
            ev_content = f"""---
title: "{finding[:100]}"
created: {TODAY}
type: evidence
tags: [{tags_str}]
source: "[[{paper['slug']}]]"
doi: "{paper['doi']}"
species: [{species_str}]
evidence_type: "{evidence_type}"
quality: "{quality}"
genes: [{', '.join(genes)}]
compounds: [{', '.join(compounds)}]
---

# {finding[:100]}

## Claim
{finding}

## Biological Context
{paper['title'][:200]}

## Supporting Evidence
*Source: [[{paper['slug']}]]*

## Evidence Quality
**Type**: {evidence_type}
**Level**: {quality}

## Contradictory Evidence
_None identified_

## Open Questions
-
"""
            ev_path = os.path.join(EVIDENCE_DIR, f"{ev_id}.md")
            with open(ev_path, 'w', encoding='utf-8') as f:
                f.write(ev_content)
            evidence_created += 1
    
    print(f"Evidence objects created: {evidence_created}")
    
    # 3. Create/update Entity pages for top genes
    gene_counter = Counter({k: len(v) for k, v in entity_genes.items()})
    top_genes = [g for g, c in gene_counter.most_common(30) if c >= 2]
    
    entity_created = 0
    for gene in top_genes:
        ev_list = entity_genes[gene]
        gene_slug = gene.lower().replace(' ', '-')
        
        # Build evidence table
        ev_rows = []
        for ev_id, snippet in ev_list[:10]:
            ev_rows.append(f"| [[{ev_id}]] | {snippet[:80]} |")
        ev_table = '\n'.join(ev_rows)
        
        gene_content = f"""---
title: "{gene}"
created: {TODAY}
type: entity
entity_type: gene
tags: [metabolism, gene]
---

# {gene}

## Evidence Summary
**Total evidence objects**: {len(ev_list)}

## Evidence Table
| Evidence | Finding |
|----------|---------|
{ev_table}

## Functional Roles
_（待从证据深入提炼）_

## Expression Pattern
-

## Species Distribution
-

## Regulatory Network
_（见 relationships/）_

## Open Questions
-
"""
        gene_path = os.path.join(ENTITIES_DIR, f"{gene_slug}.md")
        with open(gene_path, 'w', encoding='utf-8') as f:
            f.write(gene_content)
        entity_created += 1
    
    print(f"Entity pages created/updated: {entity_created}")
    
    # 4. Create compound entity pages
    compound_counter = Counter({k: len(v) for k, v in entity_compounds.items()})
    top_compounds = [c for c, cnt in compound_counter.most_common(15) if cnt >= 3]
    
    for compound in top_compounds:
        ev_list = entity_compounds[compound]
        comp_slug = slugify(compound)
        
        ev_rows = []
        for ev_id, snippet in ev_list[:10]:
            ev_rows.append(f"| [[{ev_id}]] | {snippet[:80]} |")
        ev_table = '\n'.join(ev_rows)
        
        comp_content = f"""---
title: "{compound}"
created: {TODAY}
type: entity
entity_type: compound
tags: [metabolism, compound]
---

# {compound}

## Evidence Summary
**Total evidence objects**: {len(ev_list)}

## Evidence Table
| Evidence | Finding |
|----------|---------|
{ev_table}

## Biosynthetic Pathway
-

## Regulatory Genes
-

## Species Distribution
-
"""
        comp_path = os.path.join(ENTITIES_DIR, f"{comp_slug}.md")
        with open(comp_path, 'w', encoding='utf-8') as f:
            f.write(comp_content)
        entity_created += 1
    
    # 5. Update index.md
    idx_path = os.path.join(BASE, 'index.md')
    with open(idx_path, 'r', encoding='utf-8') as f:
        idx_content = f.read()
    
    # Update evidence count
    ev_count = len([f for f in os.listdir(EVIDENCE_DIR) if f.endswith('.md')])
    idx_content = re.sub(r'Evidence Objects.*?\n', 
                         f'Evidence Objects — {ev_count} total (incl. {evidence_created} from metabolism)\n',
                         idx_content)
    
    with open(idx_path, 'w', encoding='utf-8') as f:
        f.write(idx_content)
    
    # 6. Update log.md
    log_path = os.path.join(BASE, 'log.md')
    with open(log_path, 'r', encoding='utf-8') as f:
        log_content = f.read()
    log_entry = f"""
### Evidence Created ({TODAY})
- Papers with findings: {len(papers_findings)}
- Evidence objects: {evidence_created}
- Top genes: {', '.join(top_genes[:10])}...
- Top compounds: {', '.join(top_compounds[:10])}...
- Entity pages: {entity_created} (genes + compounds)
"""

    log_content += log_entry

    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(log_content)

    # 7. Summary
    print(f"\n=== PHASE 6 COMPLETE ===")
    print(f"Papers with findings: {len(papers_findings)}")
    print(f"Evidence objects: {evidence_created}")
    print(f"Entity pages: {entity_created}")
    print(f"  - Top genes: {len(top_genes)}")
    print(f"  - Top compounds: {len(top_compounds)}")
    print(f"Total evidence/: {len(os.listdir(EVIDENCE_DIR))}")

if __name__ == '__main__':
    main()
