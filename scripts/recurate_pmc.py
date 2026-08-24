#!/usr/bin/env python3
"""重新提炼 103 篇 PMC 论文——加强文本清洗和信号句提取"""
import os, re

BASE = '/mnt/g/hermes_obsidian/hermes'
CONCEPTS_DIR = os.path.join(BASE, 'concepts', 'papers')

FINDING_SIGNALS = [
    (r'\b(we\s+(found|show|demonstrat|reveal|identif|discover|observ|confirm|conclude|report|uncover))\b', 5),
    (r'\b(our\s+(results|data|findings|study|analysis)\s+(show|demonstrat|reveal|indicat|suggest|confirm|support))\b', 5),
    (r'\b(these\s+(results|data|findings)\s+(show|demonstrat|reveal|indicat|suggest|confirm))\b', 4),
    (r'\b(this\s+study\s+(reveals|demonstrates|shows|identifies|provides|uncovers|establishes))\b', 4),
    (r'\b((importantly|notably|interestingly|surprisingly|strikingly|remarkably)\s*,)', 3),
    (r'\b(therefore\s*,?\s+(our|these|the))\b', 3),
    (r'\b((taken\s+together|in\s+conclusion|in\s+summary|collectively)\s*,)', 4),
    (r'\b((is|are|was|were)\s+(required|necessary|essential|critical|crucial|sufficient|key)\s+(for|to))\b', 3),
    (r'\b((plays?\s+a\s+(critical|crucial|key|essential|important|pivotal|central)\s+role))\b', 4),
    (r'\b((directly|specifically|strongly|significantly)\s+(regulates|controls|modulates|activates|inhibits|suppresses|promotes|enhances))\b', 4),
    (r'\b((encodes|functions\s+as|acts\s+as)\s+a\s+(key|critical|novel|important))\b', 3),
    (r'\b((interacts?\s+with|binds?\s+to|phosphorylates?|ubiquitinates?|targets?)\s+[A-Z])', 4),
    (r'\b((overexpression|knockout|knockdown|silencing)\s+of\s+[A-Z].*?(resulted|led|increased|decreased|enhanced|reduced|promoted|inhibited))\b', 4),
    (r'\b((upregulation|downregulation|up-regulation|down-regulation)\s+of)\b', 2),
    (r'\b((provides?\s+(novel|new|important|critical)\s+(insights?|evidence|understanding)))\b', 3),
    (r'\b(thus\s*,?\s+[A-Z])', 3),
    (r'\b(consistent\s+with\s+(the|a)\s+(role|function|model|hypothesis))\b', 3),
    (r'\b(we\s+(propose|hypothesize|suggest)\s+that)\b', 4),
    (r'\b((to\s+our\s+knowledge|for\s+the\s+first\s+time)\s*,)', 3),
    (r'\b(highlights?\s+the\s+(importance|role|need|potential))\b', 3),
]

SPECIES_PATTERNS = [
    (r'\bArabidopsis\s+thaliana\b', 'Arabidopsis thaliana'),
    (r'\bOryza\s+sativa\b|\brice\b', 'Oryza sativa'),
    (r'\bZea\s+mays\b|\bmaize\b|\bcorn\b', 'Zea mays'),
    (r'\bSolanum\s+lycopersicum\b|\btomato\b', 'Solanum lycopersicum'),
    (r'\bTriticum\s+aestivum\b|\bwheat\b', 'Triticum aestivum'),
    (r'\bHordeum\s+vulgare\b|\bbarley\b', 'Hordeum vulgare'),
    (r'\bGlycine\s+max\b|\bsoybean\b', 'Glycine max'),
    (r'\bPopulus\b|\bpoplar\b', 'Populus spp.'),
    (r'\bNicotiana\s+(tabacum|benthamiana)\b|\btobacco\b', 'Nicotiana tabacum'),
    (r'\bMedicago\b|\balfalfa\b', 'Medicago spp.'),
    (r'\bGossypium\b|\bcotton\b', 'Gossypium hirsutum'),
    (r'\bSorghum\s+bicolor\b|\bsorghum\b', 'Sorghum bicolor'),
    (r'\bBrassica\b|\brapeseed\b|\bcanola\b', 'Brassica spp.'),
    (r'\bMarchantia\b', 'Marchantia polymorpha'),
    (r'\bPhyscomitrium|Physcomitrella\b', 'Physcomitrium patens'),
    (r'\b(single-cell|scRNA-seq|single\s+nucleus|snRNA-seq|10x\s+Genomics|Drop-seq|spatial\s+transcriptom|Stereo-seq|Visium|ATAC-seq)\b', None),
]

METHOD_PATTERNS = [
    (r'\b(scRNA-seq|single-cell\s+RNA|single\s+nucleus\s+RNA|snRNA-seq|10x\s+Genomics|Drop-seq|single\s+cell\s+transcriptom)\b', 'scRNA-seq'),
    (r'\b(spatial\s+transcriptom|Stereo-seq|Visium|MERFISH|spatial\s+gene)\b', 'spatial transcriptomics'),
    (r'\b(snATAC-seq|single-cell\s+ATAC|single\s+nucleus\s+ATAC)\b', 'snATAC-seq'),
    (r'\b(RNA-seq|RNAseq|transcriptom(ic|e)\s+(profiling|analysis|sequencing))\b', 'transcriptomics (RNA-seq)'),
    (r'\b(metabolom|LC-MS|GC-MS|mass\s+spectrometry\s+imaging)\b', 'metabolomics'),
    (r'\b(CRISPR|Cas9|gene\s+editing|genome\s+editing)\b', 'CRISPR/Cas9'),
    (r'\b(RNAi|RNA\s+interference|gene\s+silencing|VIGS)\b', 'RNAi/VIGS'),
    (r'\b(overexpression|transgenic|knockout|knock-down|mutant)\b', 'genetic perturbation'),
    (r'\b(ChIP-seq|ChIP-qPCR|chromatin\s+immunoprecipitation)\b', 'ChIP-seq'),
    (r'\b(Y2H|yeast\s+two-hybrid|BiFC|Co-IP|coimmunoprecipitation)\b', 'protein interaction assay'),
    (r'\b(luciferase\s+reporter|dual-luciferase|EMSA|electrophoretic\s+mobility)\b', 'DNA binding/reporter'),
    (r'\b(confocal|microscopy|imaging|GFP|YFP|RFP|fluorescent)\b', 'microscopy/imaging'),
    (r'\b(GWAS|QTL|genome-wide\s+association)\b', 'GWAS/QTL'),
    (r'\b(computational|pipeline|algorithm|software|tool|benchmark)\b', 'computational method'),
]

def clean_pmc_text(raw_text):
    """Aggressive HTML artifact removal"""
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', raw_text)
    # Remove CSS/js artifacts
    text = re.sub(r'\{[^}]*\}', ' ', text)
    text = re.sub(r'@\w+[^{]*\{[^}]*\}', ' ', text)
    # Remove navigation text
    text = re.sub(r'(Go\s+to|Previous|Next|Back\s+to|Jump\s+to|Navigate|Skip\s+to)\s*\w*', ' ', text)
    # Remove reference/citation artifacts
    text = re.sub(r'\[\d+(?:[,-]\d+)*\]', ' ', text)
    # Remove URLs
    text = re.sub(r'https?://\S+', ' ', text)
    # Normalize
    text = re.sub(r'&[a-z]+;', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_findings(text):
    """Extract scientific findings from cleaned text"""
    sentences = re.split(r'(?<=[.!?])\s+', text)
    scored = []
    for sent in sentences:
        sent = sent.strip()
        if len(sent) < 40 or len(sent) > 500: continue
        if re.match(r'^\s*(Figure|Fig|Table|Supplementary|et al|http|doi|PMID|PMC|Copyright|Published|Received|Accepted|Correspondence|Funding|Conflict|License|Creative|This\s+article|The\s+author)', sent): continue
        score = 0
        for pat, w in FINDING_SIGNALS:
            if re.search(pat, sent, re.I):
                score += w
        if score >= 3:
            clean = re.sub(r'\s+', ' ', sent).strip()[:400]
            scored.append((score, clean))
    scored.sort(key=lambda x: -x[0])
    seen = set()
    findings = []
    for s, t in scored:
        k = t[:60].lower()
        if k not in seen:
            seen.add(k)
            findings.append(t)
        if len(findings) >= 10: break
    return findings

def detect_species(text):
    found = []
    for pat, name in SPECIES_PATTERNS:
        if name and re.search(pat, text, re.I):
            found.append(name)
    return list(dict.fromkeys(found))[:5] or ['Plant (unspecified)']

def detect_methods(text):
    found = []
    for pat, name in METHOD_PATTERNS:
        if re.search(pat, text, re.I):
            found.append(name)
    return list(dict.fromkeys(found))[:8] or ['molecular biology']

def main():
    papers = []
    for fname in sorted(os.listdir(CONCEPTS_DIR)):
        if not fname.endswith('.md'): continue
        path = os.path.join(CONCEPTS_DIR, fname)
        slug = fname.replace('.md', '')
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read(50000)
        except: continue
        
        # Must have PMC full text and 来源类型: PMC全文
        if '**来源类型**: PMC全文' not in content and '**PMC ID**' not in content:
            continue
        
        # Extract PMC text sections
        pmc_text = ''
        for m in re.finditer(r'### (Abstract|Introduction|Results|Discussion|Methods|Conclusion|Background|Summary)[^\n]*\n(.*?)(?=\n### |\n## |\Z)', content, re.DOTALL):
            pmc_text += m.group(2) + '\n\n'
        
        if not pmc_text or len(pmc_text) < 200:
            continue
        
        papers.append((slug, path, content, pmc_text))
    
    print(f"PMC papers to re-curate: {len(papers)}")
    
    curated = 0
    total_findings = 0
    for slug, path, original, pmc_text in papers:
        # Clean text
        clean_text = clean_pmc_text(pmc_text)
        
        # Extract
        species = detect_species(clean_text + original[:5000])
        methods = detect_methods(clean_text + original[:5000])
        findings = extract_findings(clean_text)
        total_findings += len(findings)
        
        doi = ''
        dm = re.search(r'doi:\s*(10\.\d{4,}/[^\s\n]+)', original, re.I)
        if dm: doi = dm.group(1).rstrip('/')
        
        species_str = ', '.join(species)
        methods_str = ', '.join(methods)
        findings_str = '\n'.join(f'{i+1}. {f}' for i, f in enumerate(findings)) if findings else '_（全文信号句不足）_'
        
        curation = f"""## 深度提炼

**物种**: {species_str}
**方法**: {methods_str}
**来源**: DOI:{doi}
**来源类型**: PMC全文
**文本来源**: NCBI PMC HTML (cleaned)

### 核心发现
{findings_str}
"""
        
        # Replace existing curation
        if '## 深度提炼' in original:
            new_content = re.sub(
                r'## 深度提炼.*?(?=\n## (?!深度)|## 相关|---\s*\n\Z|\Z)',
                curation.strip(), original, flags=re.DOTALL)
        else:
            ref_pos = original.find('## 相关文献')
            if ref_pos > 0:
                new_content = original[:ref_pos] + curation + '\n' + original[ref_pos:]
            else:
                new_content = original.rstrip() + '\n\n' + curation
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        curated += 1
        
        if curated % 20 == 0:
            avg = total_findings / curated
            print(f"  [{curated}/{len(papers)}] avg {avg:.1f} findings/paper")
    
    avg = total_findings / curated if curated else 0
    print(f"\n=== DONE: {curated} papers, {total_findings} findings, avg {avg:.1f}/paper ===")

if __name__ == '__main__':
    main()
