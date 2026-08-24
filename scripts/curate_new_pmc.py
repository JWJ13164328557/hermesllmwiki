#!/usr/bin/env python3
"""对 103 篇新获 PMC 全文的论文跑全流程：深度提炼 + Evidence + 标签"""
import os, re
from collections import Counter, defaultdict
from datetime import datetime

BASE = '/mnt/g/hermes_obsidian/hermes'
CONCEPTS_DIR = os.path.join(BASE, 'concepts', 'papers')
EVIDENCE_DIR = os.path.join(BASE, 'evidence')
TODAY = datetime.now().strftime('%Y-%m-%d')

# ---- Species patterns ----
SPECIES_PATTERNS = [
    (r'\bArabidopsis\s+thaliana\b', 'Arabidopsis thaliana'),
    (r'\bOryza\s+sativa\b|\brice\b', 'Oryza sativa'),
    (r'\bZea\s+mays\b|\bmaize\b|\bcorn\b', 'Zea mays'),
    (r'\bSolanum\s+lycopersicum\b|\btomato\b', 'Solanum lycopersicum'),
    (r'\bNicotiana\s+(tabacum|benthamiana)\b|\btobacco\b', 'Nicotiana tabacum'),
    (r'\bGlycine\s+max\b|\bsoybean\b', 'Glycine max'),
    (r'\bTriticum\s+aestivum\b|\bwheat\b', 'Triticum aestivum'),
    (r'\bHordeum\s+vulgare\b|\bbarley\b', 'Hordeum vulgare'),
    (r'\bPopulus\b|\bpoplar\b', 'Populus spp.'),
    (r'\bMedicago\b|\balfalfa\b', 'Medicago spp.'),
    (r'\bGossypium\b|\bcotton\b', 'Gossypium hirsutum'),
    (r'\bSorghum\s+bicolor\b|\bsorghum\b', 'Sorghum bicolor'),
    (r'\bBrassica\b|\brapeseed\b', 'Brassica spp.'),
    (r'\bMarchantia\b|\bliverwort\b', 'Marchantia polymorpha'),
    (r'\bPhyscomitrium|Physcomitrella\b', 'Physcomitrium patens'),
    (r'\bSelaginella\b', 'Selaginella spp.'),
    (r'\bPinus\b|\bpine\b', 'Pinus spp.'),
    (r'\bPicea\b|\bspruce\b', 'Picea spp.'),
    (r'\bAmborella\b', 'Amborella trichopoda'),
    (r'\bSetaria\b|\bfoxtail\s+millet\b', 'Setaria spp.'),
    (r'\bSolanum\s+tuberosum\b|\bpotato\b', 'Solanum tuberosum'),
    (r'\bCamellia\s+sinensis\b|\btea\b', 'Camellia sinensis'),
]

METHOD_PATTERNS = [
    (r'\b(scRNA-seq|single-cell\s+RNA|single\s+nucleus\s+RNA|snRNA-seq|10x\s+Genomics|Drop-seq)\b', 'scRNA-seq'),
    (r'\b(snATAC-seq|single-cell\s+ATAC|single\s+nucleus\s+ATAC)\b', 'snATAC-seq'),
    (r'\b(spatial\s+transcriptom|Stereo-seq|Visium|MERFISH|spatial\s+gene\s+expression)\b', 'spatial transcriptomics'),
    (r'\b(RNA-seq|RNAseq|transcriptom(ic|e)\s+profiling|bulk\s+RNA)\b', 'transcriptomics (RNA-seq)'),
    (r'\b(metabolom|LC-MS|GC-MS|mass\s+spectrometry)\b', 'metabolomics'),
    (r'\b(CRISPR|Cas9|gene\s+editing|genome\s+editing)\b', 'CRISPR/Cas9'),
    (r'\b(RNAi|RNA\s+interference|gene\s+silencing|VIGS)\b', 'RNAi/VIGS'),
    (r'\b(overexpression|transgenic|knockout|mutant)\b', 'genetic perturbation'),
    (r'\b(ChIP-seq|ChIP-qPCR|chromatin\s+immunoprecipitation)\b', 'ChIP-seq'),
    (r'\b(ATAC-seq|accessible\s+chromatin)\b', 'ATAC-seq'),
    (r'\b(Y2H|yeast\s+two-hybrid|BiFC|Co-IP|coimmunoprecipitation)\b', 'protein interaction assay'),
    (r'\b(EMSA|electrophoretic\s+mobility|luciferase\s+reporter|dual-luciferase)\b', 'DNA binding/reporter assay'),
    (r'\b(Western\s+blot|immunoblot|immunofluorescence|immunohistochemistry)\b', 'protein detection'),
    (r'\b(confocal|microscopy|imaging|GFP|YFP|RFP|fluorescent)\b', 'microscopy/imaging'),
    (r'\b(GWAS|QTL|genome-wide\s+association|quantitative\s+trait)\b', 'GWAS/QTL'),
    (r'\b(phylogenetic|phylogeny|evolutionary\s+analysis)\b', 'phylogenetics'),
    (r'\b(computational|pipeline|algorithm|software|tool|package|benchmark)\b', 'computational method'),
]

FINDING_SIGNALS = [
    (r'\b(we\s+(found|show|demonstrat|reveal|identif|discover|observ|confirm|conclude))\b', 5),
    (r'\b(our\s+(results|data|findings|study|analysis)\s+(show|demonstrat|reveal|indicat|suggest))\b', 5),
    (r'\b(this\s+study\s+(reveals|demonstrates|shows|identifies|provides))\b', 4),
    (r'\b((importantly|notably|interestingly|surprisingly|strikingly)\s*,)', 3),
    (r'\b((taken\s+together|in\s+conclusion|in\s+summary|collectively)\s*,)', 4),
    (r'\b((is|are|was|were)\s+(required|necessary|essential|critical|sufficient|key)\s+(for|to))\b', 3),
    (r'\b((plays?\s+a\s+(critical|crucial|key|essential|pivotal)\s+role))\b', 4),
    (r'\b((directly|specifically|strongly|significantly)\s+(regulates|controls|modulates|activates|inhibits))\b', 4),
    (r'\b((overexpression|knockout|knockdown|silencing)\s+of\s+[A-Z].*?(resulted|led|increased|decreased))\b', 4),
]

def extract_findings(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    scored = []
    for sent in sentences:
        sent = sent.strip()
        if len(sent) < 30 or len(sent) > 500: continue
        if re.match(r'^\s*(Figure|Fig|Table|Supplementary|et al|http)', sent): continue
        score = sum(w for p, w in FINDING_SIGNALS if re.search(p, sent, re.I))
        if score >= 3:
            clean = re.sub(r'\s+', ' ', sent).strip()[:400]
            scored.append((score, clean))
    scored.sort(key=lambda x: -x[0])
    seen = set()
    findings = []
    for s, t in scored:
        k = t[:60]
        if k not in seen:
            seen.add(k)
            findings.append(t)
        if len(findings) >= 10: break
    return findings

def detect_species(text):
    found = []
    for pat, name in SPECIES_PATTERNS:
        if re.search(pat, text, re.I):
            found.append(name)
    return list(dict.fromkeys(found))[:5] or ['Plant (unspecified)']

def detect_methods(text):
    found = []
    for pat, name in METHOD_PATTERNS:
        if re.search(pat, text, re.I):
            found.append(name)
    return list(dict.fromkeys(found))[:8] or ['molecular biology']

def extract_genes(text):
    genes = set()
    for m in re.finditer(r'\b([A-Z][a-z]{1,3}[A-Z][A-Za-z0-9]{1,8}|[a-z]{2,4}[A-Z][a-z]{2,4}[A-Z][A-Za-z0-9]{0,6})\b', text):
        g = m.group(1)
        if g.lower() not in ('the','and','for','was','were','with','that','this','from','have','been','also'):
            genes.add(g)
    return list(genes)[:5]

def main():
    # Step 1: Find PMC-enriched papers
    candidates = []
    for fname in sorted(os.listdir(CONCEPTS_DIR)):
        if not fname.endswith('.md'): continue
        path = os.path.join(CONCEPTS_DIR, fname)
        slug = fname.replace('.md', '')
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read(30000)
        except: continue
        
        if not re.search(r'PMC全文|PMC ID:\s*PMC\d+', content): continue
        if re.search(r'\*\*来源类型\*\*:\s*PDF全文', content): continue  # skip metabolism batch
        
        # Already curated?
        if '### 核心发现' in content:
            depth = re.search(r'### 核心发现\n(.+?)(?=\n## |\n---|\Z)', content, re.DOTALL)
            if depth and re.search(r'^\d+\.\s', depth.group(1), re.M):
                continue  # already has numbered findings
        
        candidates.append((slug, path, content))
    
    print(f"Papers to curate: {len(candidates)}")

    # Step 2: Deep curation + Evidence generation
    curated = 0
    ev_created = 0

    for slug, path, content in candidates:
        # Extract PMC text sections
        pmc_sections = []
        for m in re.finditer(r'### (Abstract|Introduction|Results|Discussion|Conclusion|Methods|Background)[^\n]*\n(.*?)(?=\n### |\Z)', content, re.DOTALL):
            pmc_sections.append(m.group(2))
        pmc_text = '\n'.join(pmc_sections)
        
        if not pmc_text or len(pmc_text) < 500:
            # Fallback: use abstract
            am = re.search(r'## 摘要\n(.+?)(?=\n## )', content, re.DOTALL)
            if am: pmc_text = am.group(1)
        
        # Extract metadata
        species = detect_species(pmc_text + content[:3000])
        methods = detect_methods(pmc_text + content[:3000])
        findings = extract_findings(pmc_text)
        genes = extract_genes(pmc_text)
        
        doi = ''
        dm = re.search(r'doi:\s*(10\.\d{4,}/[^\s\n]+)', content, re.I)
        if dm: doi = dm.group(1).rstrip('/')
        
        title = ''
        tm = re.search(r'^# (.+)$', content, re.M)
        if tm: title = tm.group(1)
        
        # Build curation block
        species_str = ', '.join(species)
        methods_str = ', '.join(methods)
        findings_str = '\n'.join(f'{i+1}. {f}' for i, f in enumerate(findings)) if findings else '_（信号句不足）_'
        
        curation = f"""
## 深度提炼

**物种**: {species_str}
**方法**: {methods_str}
**来源**: DOI:{doi}
**来源类型**: PMC全文
**基因**: {', '.join(genes) if genes else '—'}

### 核心发现
{findings_str}
"""
        
        # Insert into page
        if '## 深度提炼' in content:
            content = re.sub(
                r'## 深度提炼.*?(?=\n## (?!深度)|## 相关|---\s*\n\Z|\Z)',
                curation.strip(), content, flags=re.DOTALL)
        else:
            ref_pos = content.find('## 相关文献')
            if ref_pos > 0:
                content = content[:ref_pos] + curation + '\n' + content[ref_pos:]
            else:
                content = content.rstrip() + '\n\n' + curation
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        curated += 1
        
        # Generate Evidence Objects
        tags_str = 'pmc'
        if findings:
            for idx, finding in enumerate(findings):
                ev_id = f'{slug}-pmc-f{idx+1}'
                ev_content = f"""---
title: "{finding[:100]}"
created: {TODAY}
type: evidence
tags: [{tags_str}]
source: "[[{slug}]]"
doi: "{doi}"
species: [{species_str}]
evidence_type: "expression/functional"
quality: "medium"
genes: [{', '.join(genes)}]
---

# {finding[:100]}

## Claim
{finding}

## Source
[[{slug}]]
"""
                ev_path = os.path.join(EVIDENCE_DIR, f'{ev_id}.md')
                with open(ev_path, 'w', encoding='utf-8') as f:
                    f.write(ev_content)
                ev_created += 1
        
        if curated % 20 == 0:
            print(f"  [{curated}/{len(candidates)}] species={len(species)} findings={len(findings)} ev={ev_created}")

    # Step 3: List papers still without full text
    still_without = []
    for fname in sorted(os.listdir(CONCEPTS_DIR)):
        if not fname.endswith('.md'): continue
        path = os.path.join(CONCEPTS_DIR, fname)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                c = f.read(5000)
        except: continue
        if re.search(r'\*\*来源类型\*\*:\s*PDF全文|PMC全文|PMC ID', c): continue
        dm = re.search(r'doi:\s*(10\.\d{4,}/[^\s\n]+)', c, re.I)
        if not dm: continue
        tm = re.search(r'^# (.+)$', c, re.M)
        title = tm.group(1)[:100] if tm else ''
        still_without.append(f"{title}|{dm.group(1).rstrip('/')}")

    still_path = os.path.join(BASE, 'reports', 'papers_still_without_fulltext.csv')
    with open(still_path, 'w', encoding='utf-8-sig') as f:
        f.write("title,doi\n")
        for line in still_without:
            f.write('"' + line.replace('|', '","') + '"\n')

    print(f"\n=== DONE ===")
    print(f"Curation: {curated}/{len(candidates)}")
    print(f"Evidence: {ev_created}")
    print(f"Still without fulltext: {len(still_without)}")
    print(f"List: {still_path}")

if __name__ == '__main__':
    main()
