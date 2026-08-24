#!/usr/bin/env python3
"""从 PDF 全文深度提炼 153 篇代谢论文"""
import os, re, json, subprocess, time
from collections import defaultdict

BASE = '/mnt/g/hermes_obsidian/hermes'
PDF_DIR = os.path.join(BASE, 'raw', 'papers', 'metabolism')
CONCEPTS_DIR = os.path.join(BASE, 'concepts', 'papers')
META_JSON = os.path.join(BASE, 'raw', 'papers', 'metabolism', 'metadata_batch.json')

# ---- Species detection (from full text, case-insensitive) ----
SPECIES_PATTERNS = [
    (r'\bArabidopsis\s+thaliana\b', 'Arabidopsis thaliana'),
    (r'\bOryza\s+sativa\b|\brice\b', 'Oryza sativa'),
    (r'\bZea\s+mays\b|\bmaize\b|\bcorn\b', 'Zea mays'),
    (r'\bSolanum\s+lycopersicum\b|\btomato\b', 'Solanum lycopersicum'),
    (r'\bMalus\s+(domestica|x\s+domestica)\b|\bapple\b', 'Malus domestica'),
    (r'\bCamellia\s+sinensis\b|\btea\s+plant\b', 'Camellia sinensis'),
    (r'\bGinkgo\s+biloba\b', 'Ginkgo biloba'),
    (r'\bVitis\s+vinifera\b|\bgrapevine\b|\bgrape\b', 'Vitis vinifera'),
    (r'\bNicotiana\s+(tabacum|benthamiana)\b|\btobacco\b', 'Nicotiana tabacum'),
    (r'\bGlycine\s+max\b|\bsoybean\b', 'Glycine max'),
    (r'\bBrassica\s+napus\b|\brapeseed\b|\bcanola\b', 'Brassica napus'),
    (r'\bCitrus\s+(sinensis|reticulata|clementina)\b|\b(citrus|orange)\b', 'Citrus spp.'),
    (r'\bFragaria\b|\bstrawberry\b', 'Fragaria × ananassa'),
    (r'\bPyrus\b|\bpear\b', 'Pyrus spp.'),
    (r'\bPrunus\s+persica\b|\bpeach\b', 'Prunus persica'),
    (r'\bActinidia\b|\bkiwifruit\b', 'Actinidia spp.'),
    (r'\bRosa\s+(hybrida|rugosa|chinensis)\b|\brose\b', 'Rosa spp.'),
    (r'\bMedicago\s+(truncatula|sativa)\b|\balfalfa\b', 'Medicago spp.'),
    (r'\bSalvia\s+miltiorrhiza\b|\bdanshen\b', 'Salvia miltiorrhiza'),
    (r'\bPanax\s+(ginseng|notoginseng|quinquefolius)\b|\bginseng\b', 'Panax spp.'),
    (r'\bFagopyrum\b|\bbuckwheat\b', 'Fagopyrum esculentum'),
    (r'\bManihot\s+esculenta\b|\bcassava\b', 'Manihot esculenta'),
    (r'\bMusa\s+(acuminata|balbisiana)\b|\bbanana\b', 'Musa spp.'),
    (r'\bVaccinium\b|\bblueberry\b|\bcranberry\b', 'Vaccinium spp.'),
    (r'\bPaeonia\b|\bpeony\b', 'Paeonia spp.'),
    (r'\bPunica\s+granatum\b|\bpomegranate\b', 'Punica granatum'),
    (r'\bMorus\b|\bmulberry\b', 'Morus alba'),
    (r'\bLycium\b|\bgoji\b|\bwolfberry\b', 'Lycium barbarum'),
    (r'\bCarthamus\b|\bsafflower\b', 'Carthamus tinctorius'),
    (r'\bPopulus\b|\bpoplar\b', 'Populus spp.'),
    (r'\bCatharanthus\s+roseus\b|\bperiwinkle\b', 'Catharanthus roseus'),
    (r'\bMiscanthus\b', 'Miscanthus spp.'),
    (r'\bDioscorea\b|\byam\b', 'Dioscorea spp.'),
    (r'\bArtemisia\s+annua\b|\bsweet\s+wormwood\b', 'Artemisia annua'),
    (r'\bCrocus\s+sativus\b|\bsaffron\b', 'Crocus sativus'),
    (r'\bFicus\s+carica\b|\bfig\b', 'Ficus carica'),
    (r'\bZingiber\s+officinale\b|\bginger\b', 'Zingiber officinale'),
    (r'\bCapsicum\s+annuum\b|\bpepper\b', 'Capsicum annuum'),
    (r'\bCucumis\s+(sativus|melo)\b|\b(cucumber|melon)\b', 'Cucumis spp.'),
    (r'\bIpomoea\s+batatas\b|\bsweet\s+potato\b', 'Ipomoea batatas'),
    (r'\bTriticum\s+aestivum\b|\bwheat\b', 'Triticum aestivum'),
    (r'\bHordeum\s+vulgare\b|\bbarley\b', 'Hordeum vulgare'),
    (r'\bSorghum\s+bicolor\b|\bsorghum\b', 'Sorghum bicolor'),
    (r'\bGossypium\b|\bcotton\b', 'Gossypium hirsutum'),
    (r'\bAnanas\s+comosus\b|\bpineapple\b', 'Ananas comosus'),
    (r'\bJuglans\s+regia\b|\bwalnut\b', 'Juglans regia'),
    (r'\bFallopia\s+multiflora\b', 'Fallopia multiflora'),
    (r'\bDracaena\b', 'Dracaena spp.'),
    (r'\bLilium\b|\blily\b', 'Lilium spp.'),
    (r'\bCryptotaenia\b', 'Cryptotaenia japonica'),
    (r'\bTaxus\b|\byew\b', 'Taxus spp.'),
    (r'\bCoptis\b', 'Coptis spp.'),
    (r'\bRubus\b|\b(blackberry|raspberry)\b', 'Rubus spp.'),
    (r'\bCoffea\b|\bcoffee\b', 'Coffea spp.'),
    (r'\bLactuca\s+sativa\b|\blettuce\b', 'Lactuca sativa'),
    (r'\bSpinacia\s+oleracea\b|\bspinach\b', 'Spinacia oleracea'),
    (r'\bDaucus\s+carota\b|\bcarrot\b', 'Daucus carota'),
    (r'\bAllium\s+(cepa|sativum)\b|\b(onion|garlic)\b', 'Allium spp.'),
    (r'\bPetunia\b', 'Petunia hybrida'),
    (r'\bHevea\s+brasiliensis\b|\brubber\b', 'Hevea brasiliensis'),
    (r'\bCrocus\b', 'Crocus sativus'),
]

METHOD_PATTERNS = [
    (r'\b(RNA-seq|RNAseq|transcriptom(ic|e)\s+(analysis|profiling|sequenc))\b', 'transcriptomics (RNA-seq)'),
    (r'\b(metabolom(ic|e)\s+(analysis|profiling)|LC-MS|GC-MS|UPLC-MS|HPLC-MS)\b', 'metabolomics (LC-MS/GC-MS)'),
    (r'\b(multi-omics|multiomics|integrated\s+omics|integrative\s+omics)\b', 'multi-omics integration'),
    (r'\b(proteom(ic|e)\s+(analysis|profiling))\b', 'proteomics'),
    (r'\b(whole-genome\s+sequenc|genome\s+assembly|genome\s+annotation|genome-wide\s+analysis)\b', 'genomics'),
    (r'\b(single-cell\s+RNA|scRNA-seq|single\s+nucleus\s+RNA|snRNA-seq)\b', 'single-cell RNA-seq'),
    (r'\b(spatial\s+transcriptom|Stereo-seq|Visium|MERFISH)\b', 'spatial transcriptomics'),
    (r'\b(qRT-PCR|qPCR|real-time\s+PCR|quantitative\s+PCR)\b', 'qRT-PCR validation'),
    (r'\b(Y2H|yeast\s+two-hybrid|yeast\s+2-hybrid)\b', 'Y2H'),
    (r'\b(BiFC|bimolecular\s+fluorescence)\b', 'BiFC'),
    (r'\b(Co-IP|co-immunoprecipitation|coimmunoprecipitation)\b', 'Co-IP'),
    (r'\b(ChIP-seq|ChIP-qPCR|chromatin\s+immunoprecipitation)\b', 'ChIP-seq/qPCR'),
    (r'\b(EMSA|electrophoretic\s+mobility\s+shift)\b', 'EMSA'),
    (r'\b(dual-luciferase|dual\s+luciferase|luciferase\s+reporter|LUC\s+assay)\b', 'dual-luciferase reporter'),
    (r'\b(CRISPR|Cas9|gene\s+editing|genome\s+editing)\b', 'CRISPR/Cas9'),
    (r'\b(RNAi|RNA\s+interference|gene\s+silencing|VIGS|virus-induced\s+gene\s+silencing)\b', 'RNAi/VIGS'),
    (r'\b(overexpression|over-expression|transgenic\s+overexpression)\b', 'overexpression'),
    (r'\b(knockout|knock-out|mutant\s+analysis|T-DNA\s+insertion)\b', 'knockout/mutant'),
    (r'\b(Western\s+blot|immunoblot|protein\s+blot)\b', 'Western blot'),
    (r'\b(subcellular\s+localization|GFP\s+fusion|fluorescent\s+protein)\b', 'subcellular localization'),
    (r'\b(promoter\s+assay|GUS\s+staining|GUS\s+reporter)\b', 'promoter-GUS assay'),
]

def extract_fulltext(pdf_path):
    """用 pdftotext 提取 PDF 全文"""
    try:
        r = subprocess.run(['pdftotext', '-layout', '-nopgbrk', pdf_path, '-'],
                          capture_output=True, text=True, timeout=60)
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout[:50000]  # first 50K chars enough
    except: pass
    # fallback: try pymupdf
    try:
        import fitz
        doc = fitz.open(pdf_path)
        text = ''
        for page in doc[:15]:  # first 15 pages
            text += page.get_text()
        doc.close()
        if text.strip():
            return text[:50000]
    except: pass
    return ''

def extract_findings_fulltext(text):
    """从全文提取核心发现 — 找 Results/Discussion 区域的结论性句子"""
    # Split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    # Signal patterns for scientific findings (weighted)
    signal_patterns = [
        (r'\b(we\s+(found|show|demonstrat|reveal|identif|discover|observ|confirm|conclude|report|uncover))\b', 5),
        (r'\b(our\s+(results|data|findings|study|analysis)\s+(show|demonstrat|reveal|indicat|suggest|confirm|support))\b', 5),
        (r'\b(these\s+(results|data|findings)\s+(show|demonstrat|reveal|indicat|suggest|confirm))\b', 4),
        (r'\b(this\s+study\s+(reveals|demonstrates|shows|identifies|provides|uncovers|establishes))\b', 4),
        (r'\b((importantly|notably|interestingly|surprisingly|strikingly|remarkably)\s*,)', 3),
        (r'\b((taken\s+together|in\s+conclusion|in\s+summary|collectively)\s*,)', 4),
        (r'\b(therefore\s*,?\s+(our|these|this|the))\b', 3),
        (r'\b((is|are|was|were)\s+(required|necessary|essential|critical|crucial|sufficient|key)\s+(for|to))\b', 3),
        (r'\b((plays?\s+a\s+(critical|crucial|key|essential|important|pivotal|central)\s+role))\b', 4),
        (r'\b((directly|specifically|strongly|significantly)\s+(regulates|controls|modulates|activates|inhibits|suppresses|promotes|enhances))\b', 4),
        (r'\b((encodes|functions\s+as|acts\s+as)\s+a\s+(key|critical|novel|important))\b', 3),
        (r'\b((interacts?\s+with|binds?\s+to|phosphorylates?|ubiquitinates?|targets?)\s+[A-Z])', 4),
        (r'\b((overexpression|knockout|knockdown|silencing)\s+of\s+[A-Z].*?(resulted|led|increased|decreased|enhanced|reduced|promoted|inhibited))\b', 4),
        (r'\b((upregulation|downregulation|up-regulation|down-regulation)\s+of)\b', 2),
        (r'\b((provides?\s+(novel|new|important|critical)\s+(insights?|evidence|understanding)))\b', 3),
    ]
    
    scored_sentences = []
    for sent in sentences:
        sent = sent.strip()
        if len(sent) < 40 or len(sent) > 500:
            continue
        # Skip citations, figure refs, etc.
        if re.match(r'^\s*(Figure|Fig|Table|Supplementary|et al|http|doi)', sent):
            continue
        if re.search(r'(et al\.?\s*,?\s*\d{4})', sent) and len(sent) < 100:
            continue  # pure citation
        
        score = 0
        for pattern, weight in signal_patterns:
            if re.search(pattern, sent, re.I):
                score += weight
        
        if score >= 3:
            # Clean up
            clean = re.sub(r'\s+', ' ', sent).strip()
            scored_sentences.append((score, clean[:400]))
    
    scored_sentences.sort(key=lambda x: -x[0])
    
    # Deduplicate by content similarity
    seen = set()
    findings = []
    for score, sent in scored_sentences:
        key = sent[:80]
        if key not in seen:
            seen.add(key)
            findings.append(sent)
        if len(findings) >= 10:
            break
    
    return findings

def main():
    # Load DOI→PDF mapping
    with open(META_JSON, 'r') as f:
        meta = json.load(f)
    
    # Build DOI→concept file mapping
    doi_to_concept = {}
    for fname in os.listdir(CONCEPTS_DIR):
        if not fname.endswith('.md'): continue
        path = os.path.join(CONCEPTS_DIR, fname)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read(2000)
            dm = re.search(r'doi:\s*(10\.\d{4,}/[^\s\n]+)', content, re.I)
            if dm:
                doi = dm.group(1).rstrip('/')
                doi_to_concept[doi] = (fname, path)
        except: pass
    
    # Process PDFs
    pdf_files = [f for f in os.listdir(PDF_DIR) if f.endswith('.pdf')]
    print(f"PDFs: {len(pdf_files)}")
    
    # Build DOI → PDF mapping from metadata
    doi_to_pdf = defaultdict(list)
    for doi, info in meta.items():
        for fname in info.get('filenames', []):
            if fname in pdf_files:
                doi_to_pdf[doi].append(fname)
                break
    
    curated = 0
    skipped = 0
    for doi, pdf_names in doi_to_pdf.items():
        if doi not in doi_to_concept:
            skipped += 1
            continue
        
        concept_fname, concept_path = doi_to_concept[doi]
        pdf_name = pdf_names[0]
        pdf_path = os.path.join(PDF_DIR, pdf_name)
        
        # Extract full text
        fulltext = extract_fulltext(pdf_path)
        if not fulltext:
            print(f"  SKIP (no text): {pdf_name[:50]}")
            skipped += 1
            continue
        
        # Extract species, methods, findings
        text_lower = fulltext.lower()
        species = []
        for pat, name in SPECIES_PATTERNS:
            if re.search(pat, fulltext, re.I):
                species.append(name)
        species = list(dict.fromkeys(species))[:5]  # deduplicate
        if not species:
            species = ['Plant (unspecified)']
        
        methods = []
        for pat, name in METHOD_PATTERNS:
            if re.search(pat, fulltext, re.I):
                methods.append(name)
        methods = list(dict.fromkeys(methods))[:8]
        if not methods:
            methods = ['molecular biology / biochemistry']
        
        findings = extract_findings_fulltext(fulltext)
        
        # Update concept page
        with open(concept_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        species_str = ', '.join(species)
        methods_str = ', '.join(methods)
        findings_str = '\n'.join(f'{i+1}. {f}' for i, f in enumerate(findings)) if findings else '_（无显著信号句）_'
        
        curation_new = f"""## 深度提炼

**物种**: {species_str}
**方法**: {methods_str}
**来源**: DOI:{doi}
**来源类型**: PDF全文 ({pdf_name[:60]})

### 核心发现
{findings_str}
"""
        
        # Replace existing curation (from abstract-based) with full-text-based
        if '## 深度提炼' in content:
            content = re.sub(
                r'## 深度提炼.*?(?=\n## (?!深度)|## 相关文献|---\s*\n\Z|\Z)',
                curation_new.strip(),
                content, flags=re.DOTALL
            )
        else:
            # Insert before ## 相关文献 or at end
            ref_pos = content.find('## 相关文献')
            if ref_pos > 0:
                content = content[:ref_pos] + curation_new + '\n' + content[ref_pos:]
            else:
                content = content.rstrip() + '\n\n' + curation_new
        
        with open(concept_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        curated += 1
        if curated % 20 == 0:
            n_findings = len(findings)
            print(f"  [{curated}] {species[0]}: {n_findings} findings | {pdf_name[:40]}...")
    
    print(f"\n=== DONE ===")
    print(f"Curated: {curated}")
    print(f"Skipped: {skipped}")

if __name__ == '__main__':
    main()
