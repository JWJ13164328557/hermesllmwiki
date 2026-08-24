#!/usr/bin/env python3
"""全量深度提炼：扫描 raw/ 所有 PDF → 匹配概念页 → 提取物种/方法/发现 → 更新概念页"""
import os, re, sys, subprocess

BASE = '/mnt/g/hermes_obsidian/hermes'
CONCEPTS_DIR = os.path.join(BASE, 'concepts', 'papers')
RAW_DIR = os.path.join(BASE, 'raw')

SPECIES_PATTERNS = [
    (r'\bArabidopsis\s+thaliana\b', 'Arabidopsis thaliana'),
    (r'\bOryza\s+sativa\b|\brice\b', 'Oryza sativa'),
    (r'\bZea\s+mays\b|\bmaize\b|\bcorn\b', 'Zea mays'),
    (r'\bSolanum\s+lycopersicum\b|\btomato\b', 'Solanum lycopersicum'),
    (r'\bMalus\s+(domestica|x\s+domestica)\b|\bapple\b', 'Malus domestica'),
    (r'\bGlycine\s+max\b|\bsoybean\b', 'Glycine max'),
    (r'\bNicotiana\s+(tabacum|benthamiana)\b|\btobacco\b', 'Nicotiana tabacum'),
    (r'\bBrassica\s+napus\b|\brapeseed\b|\bcanola\b', 'Brassica napus'),
    (r'\bTriticum\s+aestivum\b|\bwheat\b', 'Triticum aestivum'),
    (r'\bHordeum\s+vulgare\b|\bbarley\b', 'Hordeum vulgare'),
    (r'\bPopulus\b|\bpoplar\b', 'Populus spp.'),
    (r'\bMedicago\s+(truncatula|sativa)\b|\balfalfa\b', 'Medicago spp.'),
    (r'\bVitis\s+vinifera\b|\bgrapevine\b|\bgrape\b', 'Vitis vinifera'),
    (r'\bCitrus\s+(sinensis|reticulata|clementina)\b|\b(citrus|orange)\b', 'Citrus spp.'),
    (r'\bFragaria\b|\bstrawberry\b', 'Fragaria × ananassa'),
    (r'\bGossypium\b|\bcotton\b', 'Gossypium hirsutum'),
    (r'\bSorghum\s+bicolor\b|\bsorghum\b', 'Sorghum bicolor'),
    (r'\bMusa\s+(acuminata|balbisiana)\b|\bbanana\b', 'Musa spp.'),
    (r'\bManihot\s+esculenta\b|\bcassava\b', 'Manihot esculenta'),
    (r'\bHelianthus\s+annuus\b|\bsunflower\b', 'Helianthus annuus'),
    (r'\bTheobroma\s+cacao\b|\bcacao\b|\bcocoa\b', 'Theobroma cacao'),
    (r'\bCoffea\b|\bcoffee\b', 'Coffea spp.'),
    (r'\bCamellia\s+sinensis\b|\btea\s+plant\b', 'Camellia sinensis'),
    (r'\bPinus\b|\bpine\b', 'Pinus spp.'),
    (r'\bPicea\b|\bspruce\b', 'Picea spp.'),
    (r'\bEucalyptus\b', 'Eucalyptus spp.'),
    (r'\bQuercus\b|\boak\b', 'Quercus spp.'),
    (r'\bSetaria\s+(viridis|italica)\b|\bfoxtail\s+millet\b', 'Setaria spp.'),
    (r'\bPhaseolus\s+vulgaris\b|\bcommon\s+bean\b', 'Phaseolus vulgaris'),
    (r'\bCicer\s+arietinum\b|\bchickpea\b', 'Cicer arietinum'),
    (r'\bPisum\s+sativum\b|\bpea\b', 'Pisum sativum'),
    (r'\bBeta\s+vulgaris\b|\bsugar\s+beet\b|\bbeetroot\b', 'Beta vulgaris'),
    (r'\bBrachypodium\s+distachyon\b', 'Brachypodium distachyon'),
    (r'\bSelaginella\b', 'Selaginella spp.'),
    (r'\bPhyscomitrium\s+patens\b|\bPhyscomitrella\b', 'Physcomitrium patens'),
    (r'\bMarchantia\s+polymorpha\b', 'Marchantia polymorpha'),
    (r'\bChlamydomonas\s+reinhardtii\b', 'Chlamydomonas reinhardtii'),
    (r'\bAmborella\s+trichopoda\b', 'Amborella trichopoda'),
    (r'\bCeratopteris\s+richardii\b|\bfern\b', 'Ceratopteris richardii'),
    (r'\bDaucus\s+carota\b|\bcarrot\b', 'Daucus carota'),
    (r'\bSolanum\s+tuberosum\b|\bpotato\b', 'Solanum tuberosum'),
    (r'\bCucumis\s+(sativus|melo)\b|\b(cucumber|melon)\b', 'Cucumis spp.'),
    (r'\bCapsicum\s+annuum\b|\bpepper\b', 'Capsicum annuum'),
    (r'\bAllium\s+(cepa|sativum)\b|\b(onion|garlic)\b', 'Allium spp.'),
    (r'\bSpinacia\s+oleracea\b|\bspinach\b', 'Spinacia oleracea'),
    (r'\bLactuca\s+sativa\b|\blettuce\b', 'Lactuca sativa'),
    (r'\bPrunus\s+persica\b|\bpeach\b', 'Prunus persica'),
    (r'\bPyrus\b|\bpear\b', 'Pyrus spp.'),
    (r'\bPanax\s+(ginseng|notoginseng|quinquefolius)\b|\bginseng\b', 'Panax spp.'),
    (r'\bTaxus\b|\byew\b', 'Taxus spp.'),
    (r'\bArtemisia\s+annua\b|\bsweet\s+wormwood\b', 'Artemisia annua'),
    (r'\bSalvia\s+miltiorrhiza\b|\bdanshen\b', 'Salvia miltiorrhiza'),
    (r'\bGinkgo\s+biloba\b', 'Ginkgo biloba'),
    (r'\bCatharanthus\s+roseus\b|\bperiwinkle\b', 'Catharanthus roseus'),
    (r'\bHevea\s+brasiliensis\b|\brubber\b', 'Hevea brasiliensis'),
    (r'\bJuglans\s+regia\b|\bwalnut\b', 'Juglans regia'),
    (r'\bAnanas\s+comosus\b|\bpineapple\b', 'Ananas comosus'),
    (r'\bMorus\b|\bmulberry\b', 'Morus alba'),
    (r'\bFicus\s+carica\b|\bfig\b', 'Ficus carica'),
    (r'\bPunica\s+granatum\b|\bpomegranate\b', 'Punica granatum'),
    (r'\bActinidia\b|\bkiwifruit\b', 'Actinidia spp.'),
    (r'\bVaccinium\b|\bblueberry\b|\bcranberry\b', 'Vaccinium spp.'),
    (r'\bRubus\b|\b(blackberry|raspberry)\b', 'Rubus spp.'),
    (r'\bFagopyrum\b|\bbuckwheat\b', 'Fagopyrum esculentum'),
    (r'\bIpomoea\s+batatas\b|\bsweet\s+potato\b', 'Ipomoea batatas'),
    (r'\bDioscorea\b|\byam\b', 'Dioscorea spp.'),
    (r'\bRosa\s+(hybrida|rugosa|chinensis)\b|\brose\b', 'Rosa spp.'),
    (r'\bZingiber\s+officinale\b|\bginger\b', 'Zingiber officinale'),
    (r'\bCrocus\b|\bsaffron\b', 'Crocus sativus'),
    (r'\bLilium\b|\blily\b', 'Lilium spp.'),
    (r'\bPetunia\b', 'Petunia hybrida'),
    (r'\bCoptis\b', 'Coptis spp.'),
    (r'\bFallopia\s+multiflora\b', 'Fallopia multiflora'),
    (r'\bDracaena\b', 'Dracaena spp.'),
    (r'\bLycium\b|\bgoji\b|\bwolfberry\b', 'Lycium barbarum'),
    (r'\bPaeonia\b|\bpeony\b', 'Paeonia spp.'),
    (r'\bCarthamus\b|\bsafflower\b', 'Carthamus tinctorius'),
    (r'\bCryptotaenia\b', 'Cryptotaenia japonica'),
    (r'\bMiscanthus\b', 'Miscanthus spp.'),
]

METHOD_PATTERNS = [
    (r'\b(RNA-seq|RNAseq|transcriptom(ic|e)\s+(analysis|profiling|sequenc))\b', 'transcriptomics (RNA-seq)'),
    (r'\b(metabolom(ic|e)\s+(analysis|profiling)|LC-MS|GC-MS|UPLC-MS|HPLC-MS)\b', 'metabolomics (LC-MS/GC-MS)'),
    (r'\b(multi-omics|multiomics|integrated\s+omics|integrative\s+omics)\b', 'multi-omics integration'),
    (r'\b(proteom(ic|e)\s+(analysis|profiling))\b', 'proteomics'),
    (r'\b(whole-genome\s+sequenc|genome\s+assembly|genome\s+annotation|genome-wide\s+analysis)\b', 'genomics'),
    (r'\b(single-cell\s+RNA|scRNA-seq|single\s+nucleus\s+RNA|snRNA-seq)\b', 'single-cell RNA-seq'),
    (r'\b(spatial\s+transcriptom|Stereo-seq|Visium|MERFISH|spatial\s+omics)\b', 'spatial transcriptomics'),
    (r'\b(ATAC-seq|scATAC-seq|single-cell\s+ATAC)\b', 'ATAC-seq'),
    (r'\b(ChIP-seq|ChIP-qPCR|chromatin\s+immunoprecipitation)\b', 'ChIP-seq/qPCR'),
    (r'\b(qRT-PCR|qPCR|real-time\s+PCR|quantitative\s+PCR)\b', 'qRT-PCR validation'),
    (r'\b(Y2H|yeast\s+two-hybrid|yeast\s+2-hybrid)\b', 'Y2H'),
    (r'\b(BiFC|bimolecular\s+fluorescence)\b', 'BiFC'),
    (r'\b(Co-IP|co-immunoprecipitation|coimmunoprecipitation)\b', 'Co-IP'),
    (r'\b(EMSA|electrophoretic\s+mobility\s+shift)\b', 'EMSA'),
    (r'\b(dual-luciferase|dual\s+luciferase|luciferase\s+reporter|LUC\s+assay)\b', 'dual-luciferase reporter'),
    (r'\b(CRISPR|Cas9|gene\s+editing|genome\s+editing)\b', 'CRISPR/Cas9'),
    (r'\b(RNAi|RNA\s+interference|gene\s+silencing|VIGS|virus-induced\s+gene\s+silencing)\b', 'RNAi/VIGS'),
    (r'\b(overexpression|over-expression|transgenic\s+overexpression)\b', 'overexpression'),
    (r'\b(knockout|knock-out|mutant\s+analysis|T-DNA\s+insertion)\b', 'knockout/mutant'),
    (r'\b(Western\s+blot|immunoblot|protein\s+blot)\b', 'Western blot'),
    (r'\b(subcellular\s+localization|GFP\s+fusion|fluorescent\s+protein)\b', 'subcellular localization'),
    (r'\b(promoter\s+assay|GUS\s+staining|GUS\s+reporter)\b', 'promoter-GUS assay'),
    (r'\b(phylogenetic\s+analysis|evolutionary\s+analysis|phylogeny)\b', 'phylogenetics'),
    (r'\b(GWAS|genome-wide\s+association)\b', 'GWAS'),
    (r'\b(QTL|quantitative\s+trait\s+locus)\b', 'QTL mapping'),
]


def extract_fulltext(pdf_path):
    """Extract text from PDF via pymupdf (first 15 pages)"""
    try:
        import fitz
        doc = fitz.open(pdf_path)
        text = ''
        for page in doc[:15]:
            text += page.get_text()
        doc.close()
        if len(text.strip()) > 200:
            return text[:50000]
    except Exception as e:
        import sys
        print(f"  ⚠ extract failed: {os.path.basename(pdf_path)[:50]}: {e}", file=sys.stderr)
    return ''


def extract_findings(text):
    """Extract key findings from full text"""
    sentences = re.split(r'(?<=[.!?])\s+', text)
    signal_patterns = [
        (r'\b(we\s+(found|show|demonstrat|reveal|identif|discover|observ|confirm|conclude|report|uncover))\b', 5),
        (r'\b(our\s+(results|data|findings|study|analysis)\s+(show|demonstrat|reveal|indicat|suggest|confirm|support))\b', 5),
        (r'\b(these\s+(results|data|findings)\s+(show|demonstrat|reveal|indicat|suggest|confirm))\b', 4),
        (r'\b(this\s+study\s+(reveals|demonstrates|shows|identifies|provides|uncovers|establishes))\b', 4),
        (r'\b((importantly|notably|interestingly|surprisingly|strikingly|remarkably)\s*,)', 3),
        (r'\b((taken\s+together|in\s+conclusion|in\s+summary|collectively)\s*,)', 4),
        (r'\b((is|are|was|were)\s+(required|necessary|essential|critical|crucial|sufficient|key)\s+(for|to))\b', 3),
        (r'\b((plays?\s+a\s+(critical|crucial|key|essential|important|pivotal|central)\s+role))\b', 4),
        (r'\b((directly|specifically|strongly|significantly)\s+(regulates|controls|modulates|activates|inhibits|suppresses|promotes|enhances))\b', 4),
        (r'\b((encodes|functions\s+as|acts\s+as)\s+a\s+(key|critical|novel|important))\b', 3),
        (r'\b((interacts?\s+with|binds?\s+to|phosphorylates?|ubiquitinates?|targets?)\s+[A-Z])', 4),
        (r'\b((overexpression|knockout|knockdown|silencing)\s+of\s+[A-Z].*?(resulted|led|increased|decreased|enhanced|reduced|promoted|inhibited))\b', 4),
        (r'\b((upregulation|downregulation|up-regulation|down-regulation)\s+of)\b', 2),
        (r'\b((provides?\s+(novel|new|important|critical)\s+(insights?|evidence|understanding)))\b', 3),
    ]
    scored = []
    for sent in sentences:
        sent = sent.strip()
        if len(sent) < 40 or len(sent) > 500:
            continue
        if re.match(r'^\s*(Figure|Fig|Table|Supplementary|et al|http|doi)', sent):
            continue
        if re.search(r'(et al\.?\s*,?\s*\d{4})', sent) and len(sent) < 100:
            continue
        score = 0
        for pattern, weight in signal_patterns:
            if re.search(pattern, sent, re.I):
                score += weight
        if score >= 3:
            clean = re.sub(r'\s+', ' ', sent).strip()
            scored.append((score, clean[:400]))
    scored.sort(key=lambda x: -x[0])
    seen = set()
    findings = []
    for score, sent in scored:
        key = sent[:80]
        if key not in seen:
            seen.add(key)
            findings.append(sent)
        if len(findings) >= 8:
            break
    return findings


def main():
    # Parse --dois argument: comma-separated or file path
    target_dois = None
    args = sys.argv[1:]
    if '--dois' in args:
        idx = args.index('--dois')
        if idx + 1 < len(args):
            dois_arg = args[idx + 1]
            if os.path.exists(dois_arg):
                with open(dois_arg) as f:
                    target_dois = set(line.strip().rstrip('./') for line in f if line.strip())
            else:
                target_dois = set(d.strip().rstrip('./') for d in dois_arg.split(',') if d.strip())
    
    # Build DOI → concept mapping
    print("Building DOI → concept mapping...", file=sys.stderr)
    doi_to_concept = {}
    for fname in os.listdir(CONCEPTS_DIR):
        if not fname.endswith('.md'):
            continue
        path = os.path.join(CONCEPTS_DIR, fname)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read(3000)
            dm = re.search(r'doi:\s*"?\s*(10\.\d{4,}/[^\s\n"\]]+)', content, re.I)
            if dm:
                doi_to_concept[dm.group(1).rstrip('/')] = path
        except:
            pass
    print(f"  → {len(doi_to_concept)} concept pages with DOI", file=sys.stderr)

    # Filter to target DOIs if specified
    if target_dois:
        # Normalize: strip trailing slashes/dots for matching
        normalized_targets = set(d.rstrip('./') for d in target_dois)
        doi_to_concept = {k: v for k, v in doi_to_concept.items() 
                          if k.rstrip('./') in normalized_targets}
        print(f"  → filtered to {len(doi_to_concept)} targets", file=sys.stderr)

    import glob as _glob

    matched = []
    if target_dois:
        # Fast path: direct filename lookup per target DOI
        print(f"  -> fast lookup for {len(doi_to_concept)} target DOIs", file=sys.stderr)
        for doi in doi_to_concept:
            doi_clean = doi.rstrip('./')
            doi_slug = doi_clean.replace('/', '_')
            candidates = [doi_slug, doi_slug.replace('(', '').replace(')', '')]
            # journal abbreviation fix
            doi_abbrev = re.sub(
                r'/(pp|tpc|tpj|pbi|pcp|hr|nar|bib|nph|jxb|dev|jcs|ppl|pgen|pcbi|acel|jipb|genetics|fpls|fgene)_(\d)',
                r'/\1.\2', doi_slug)
            if doi_abbrev != doi_slug:
                candidates.append(doi_abbrev)

            found = None
            for fname in candidates:
                # 2026-08-24: PDF 已汇总到 papers/all_pdfs/，加入定位目录
                for subdir in ['', 'papers/', 'papers/metabolism/', 'papers/all_pdfs/']:
                    path = os.path.join(RAW_DIR, subdir, fname + '.pdf')
                    if os.path.exists(path):
                        found = path
                        break
                if found:
                    break
            if not found:
                # glob fallback
                for pat in [f'**/*{doi_slug[:50]}*.pdf', f'**/*{doi_slug[:50].replace(".", "-")}*.pdf']:
                    hits = _glob.glob(os.path.join(RAW_DIR, pat), recursive=True)
                    if hits:
                        found = hits[0]
                        break
            if found:
                matched.append((found, doi))
        print(f"  -> {len(matched)} PDFs matched via fast lookup", file=sys.stderr)
    else:
        # Full scan (no --dois filter)
        pdf_files = []
        for root, dirs, files in os.walk(RAW_DIR):
            for f in files:
                if f.endswith('.pdf'):
                    pdf_files.append(os.path.join(root, f))
        print(f"  -> {len(pdf_files)} PDFs found", file=sys.stderr)

        def doi_from_fname(fname):
            doi = fname.rsplit('.', 1)[0].replace('_', '/')
            doi = re.sub(
                r'/(pp|tpc|tpj|pbi|pcp|hr|nar|bib|nph|jxb|dev|jcs|ppl|pgen|pcbi|acel|jipb|genetics|fpls|fgene)/(\d)',
                r'/\1.\2', doi)
            return doi if re.match(r'10\.\d{4,}/', doi) else None

        for pdf_path in pdf_files:
            doi = doi_from_fname(os.path.basename(pdf_path))
            if doi and doi in doi_to_concept:
                matched.append((pdf_path, doi))
                continue
            try:
                import fitz
                doc = fitz.open(pdf_path)
                for page_num in range(min(3, len(doc))):
                    m = re.search(r'10\.\d{4,}/[^\s"\n\r\t]+', doc[page_num].get_text())
                    if m:
                        doi = m.group(0).rstrip('.,;:)')
                        if doi in doi_to_concept:
                            matched.append((pdf_path, doi))
                            break
                doc.close()
            except:
                pass

    print(f"  → {len(matched)} PDFs matched to concepts", file=sys.stderr)

    # Deep curate
    curated = 0
    no_text = 0
    for pdf_path, doi in matched:
        fulltext = extract_fulltext(pdf_path)
        if not fulltext:
            no_text += 1
            continue

        # Extract species
        species = []
        for pat, name in SPECIES_PATTERNS:
            if re.search(pat, fulltext, re.I):
                species.append(name)
        species = list(dict.fromkeys(species))[:5]
        if not species:
            species = ['Plant (unspecified)']

        # Extract methods
        methods = []
        for pat, name in METHOD_PATTERNS:
            if re.search(pat, fulltext, re.I):
                methods.append(name)
        methods = list(dict.fromkeys(methods))[:8]
        if not methods:
            methods = ['molecular biology / biochemistry']

        # Extract findings
        findings = extract_findings(fulltext)

        # Update concept page
        concept_path = doi_to_concept[doi]
        with open(concept_path, 'r', encoding='utf-8') as f:
            content = f.read()

        species_str = ', '.join(species)
        methods_str = ', '.join(methods)
        findings_str = '\n'.join(f'{i+1}. {f}' for i, f in enumerate(findings)) if findings else '_（无显著信号句）_'

        curation_new = f"""## 深度提炼

**物种**: {species_str}
**方法**: {methods_str}
**来源**: DOI:{doi}
**来源类型**: PDF全文 ({os.path.basename(pdf_path)[:60]})

### 核心发现
{findings_str}
"""

        if '## 深度提炼' in content:
            content = re.sub(
                r'## 深度提炼.*?(?=\n## (?!深度)|## 相关文献|---\s*\n\Z|\Z)',
                curation_new.strip(),
                content, flags=re.DOTALL
            )
        else:
            ref_pos = content.find('## 相关文献')
            if ref_pos > 0:
                content = content[:ref_pos] + curation_new + '\n' + content[ref_pos:]
            else:
                content = content.rstrip() + '\n\n' + curation_new

        with open(concept_path, 'w', encoding='utf-8') as f:
            f.write(content)

        curated += 1
        if curated % 100 == 0:
            print(f"  [{curated}/{len(matched)}] {species[0]}: {len(findings)} findings", file=sys.stderr)

    print(f"\n=== DONE ===")
    print(f"Matched PDFs: {len(matched)}")
    print(f"Curated: {curated}")
    print(f"No text: {no_text}")


if __name__ == '__main__':
    main()
