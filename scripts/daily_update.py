#!/usr/bin/env python3
"""
每日植物学文献自动检索与完整导入
用法: python3 daily_update.py [--days 1] [--import]
"""

import urllib.parse, subprocess, json, xml.etree.ElementTree as ET, os, re, sys
from datetime import datetime, timedelta

# JCR 2024 植物/农学/相关期刊权威白名单 (502 期刊, 从 journal_rankings_2024 CSV 生成)
# 用于期刊过滤的精确匹配层——JCR 收录的植物/农学期刊直接放行(最终仍由 is_plant 内容校验兜底)
try:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from jcr_whitelist import JOURNAL_JCR_PLANT_LOWER, journal_in_jcr
    HAS_JCR_WHITELIST = True
except ImportError:
    HAS_JCR_WHITELIST = False
    def journal_in_jcr(journal_name):
        return False

BASE = '/mnt/g/hermes_obsidian/hermes'
CONCEPTS_DIR = f'{BASE}/concepts/papers'  # SCHEMA: papers/
METHODS_DIR = f'{BASE}/concepts/methods'   # SCHEMA: methods/

PLANT_SPECIES = '"plant"[Title/Abstract] OR "Arabidopsis"[Title/Abstract] OR "rice"[Title/Abstract] OR "wheat"[Title/Abstract] OR "maize"[Title/Abstract] OR "soybean"[Title/Abstract] OR "tomato"[Title/Abstract] OR "poplar"[Title/Abstract] OR "cotton"[Title/Abstract] OR "tobacco"[Title/Abstract] OR "potato"[Title/Abstract] OR "grape"[Title/Abstract] OR "tea"[Title/Abstract] OR "alfalfa"[Title/Abstract] OR "Medicago"[Title/Abstract] OR "Brassica"[Title/Abstract] OR "barley"[Title/Abstract] OR "cassava"[Title/Abstract] OR "Marchantia"[Title/Abstract] OR "Physcomitrium"[Title/Abstract] OR "sunflower"[Title/Abstract] OR "peanut"[Title/Abstract] OR "chrysanthemum"[Title/Abstract] OR "Salvia"[Title/Abstract] OR "Artemisia"[Title/Abstract] OR "Panax"[Title/Abstract] OR "Andrographis"[Title/Abstract]'

SEARCH_QUERIES = [
    # ⭐ FOCUS 1: Plant single-cell omics
    f'(("single-cell"[Title/Abstract] OR "scRNA-seq"[Title/Abstract] OR "single nucleus"[Title/Abstract] OR "snRNA-seq"[Title/Abstract] OR "scATAC-seq"[Title/Abstract] OR "single cell atlas"[Title/Abstract] OR "cell atlas"[Title/Abstract]) AND ({PLANT_SPECIES}))',
    # ⭐ FOCUS 2: Plant spatial transcriptomics
    f'(("spatial transcriptom"[Title/Abstract] OR "Stereo-seq"[Title/Abstract] OR "Visium"[Title/Abstract] OR "Xenium"[Title/Abstract] OR "MERFISH"[Title/Abstract] OR "spatial multi-omics"[Title/Abstract] OR "spatially resolved"[Title/Abstract] OR "spatial gene expression"[Title/Abstract]) AND ({PLANT_SPECIES}))',
    # ⭐ FOCUS 3: Light signaling & photosynthesis
    f'(("light signaling"[Title/Abstract] OR "photomorphogenesis"[Title/Abstract] OR "phytochrome"[Title/Abstract] OR "photoreceptor"[Title/Abstract] OR "blue light"[Title/Abstract] OR "red light"[Title/Abstract] OR "far-red"[Title/Abstract] OR "shade avoidance"[Title/Abstract] OR "photosynthesis"[Title/Abstract] OR "chloroplast"[Title/Abstract] OR "stomatal"[Title/Abstract] OR "guard cell"[Title/Abstract] OR "circadian"[Title/Abstract] OR "photoperiod"[Title/Abstract] OR "light quality"[Title/Abstract]) AND ({PLANT_SPECIES}))',
    # ⭐ FOCUS 4: Plant development
    f'(("plant development"[Title/Abstract] OR "root development"[Title/Abstract] OR "shoot apical"[Title/Abstract] OR "flower development"[Title/Abstract] OR "seed development"[Title/Abstract] OR "vascular development"[Title/Abstract] OR "wood formation"[Title/Abstract] OR "secondary growth"[Title/Abstract] OR "xylem"[Title/Abstract] OR "phloem"[Title/Abstract] OR "meristem"[Title/Abstract] OR "organogenesis"[Title/Abstract] OR "embryogenesis"[Title/Abstract] OR "cell differentiation"[Title/Abstract] OR "cambium"[Title/Abstract]) AND ({PLANT_SPECIES}))',
    # Supplementary: ATAC / multi-omics
    f'(("ATAC-seq"[Title/Abstract] OR "multi-omics"[Title/Abstract] OR "snATAC"[Title/Abstract] OR "CUT&Tag"[Title/Abstract]) AND ({PLANT_SPECIES}))',
    # Supplementary: regeneration
    f'(("callus"[Title/Abstract] OR "regeneration"[Title/Abstract] OR "somatic embryo"[Title/Abstract] OR "de novo organogenesis"[Title/Abstract] OR "reprogramming"[Title/Abstract]) AND ({PLANT_SPECIES}))',
    # Supplementary: stress & immunity
    f'(("salt stress"[Title/Abstract] OR "drought stress"[Title/Abstract] OR "cold stress"[Title/Abstract] OR "heat stress"[Title/Abstract] OR "heavy metal"[Title/Abstract] OR "pathogen"[Title/Abstract] OR "immunity"[Title/Abstract] OR "defense"[Title/Abstract] OR "herbivory"[Title/Abstract]) AND ({PLANT_SPECIES}))',
    # Supplementary: metabolism
    f'(("flavonoid"[Title/Abstract] OR "anthocyanin"[Title/Abstract] OR "terpenoid"[Title/Abstract] OR "alkaloid"[Title/Abstract] OR "tanshinone"[Title/Abstract] OR "artemisinin"[Title/Abstract] OR "metabolic engineering"[Title/Abstract] OR "biosynthesis"[Title/Abstract]) AND ({PLANT_SPECIES}))',
    # Supplementary: epigenetics
    f'(("histone"[Title/Abstract] OR "chromatin"[Title/Abstract] OR "DNA methylation"[Title/Abstract] OR "H3K27"[Title/Abstract] OR "epigenetic"[Title/Abstract]) AND ({PLANT_SPECIES}))',
    # Supplementary: hormone signaling
    f'(("auxin"[Title/Abstract] OR "gibberellin"[Title/Abstract] OR "abscisic acid"[Title/Abstract] OR "jasmonic acid"[Title/Abstract] OR "salicylic acid"[Title/Abstract] OR "ethylene"[Title/Abstract] OR "brassinosteroid"[Title/Abstract] OR "strigolactone"[Title/Abstract] OR "cytokinin"[Title/Abstract]) AND ({PLANT_SPECIES}))',
]

# Expanded journal whitelist (2026-05-31 V2) — 极度放宽，覆盖所有植物/农业/方法/微生物相关
JOURNAL_EXACT = {
    # Tier 1: CNS + top multidisciplinary
    'Nature', 'Science', 'Cell',
    'Nature Plants', 'Nature Communications', 'Nature Methods', 'Nature Genetics', 'Nature Biotechnology',
    'Nature Reviews Molecular Cell Biology', 'Nature Cell Biology', 'Nature Reviews Genetics',
    'Proceedings of the National Academy of Sciences',
    # Tier 2: top plant journals
    'The Plant Cell', 'Molecular Plant', 'Plant Biotechnology Journal', 'New Phytologist',
    'Plant Communications', 'The Plant Journal', 'Plant Physiology', 'Plant, Cell & Environment',
    'Journal of Integrative Plant Biology', 'Journal of Experimental Botany',
    'Current Opinion in Plant Biology', 'Trends in Plant Science', 'Annual Review of Plant Biology',
    'Horticulture Research', 'The Crop Journal', 'Journal of Advanced Research',
    'Plant Physiology and Biochemistry', 'Plant Molecular Biology', 'Planta', 'Planta Medica',
    'Phytochemistry', 'Plant and Cell Physiology', 'Annals of Botany', 'Plant Reproduction',
    'BMC Plant Biology', 'Plant Direct', 'Stress Biology',
    'Molecular Plant Pathology', 'Theoretical and Applied Genetics',
    # Tier 3: general biology
    'Genome Biology', 'Current Biology', 'Developmental Cell', 'eLife',
    'EMBO Journal', 'EMBO Reports', 'Cell Reports', 'Science Advances',
    'Communications Biology', 'Advanced Science',
    'Nucleic Acids Research', 'Bioinformatics', 'Genome Research', 'Nature Computational Science',
    # Tier 4: broad plant/agriculture (V2 addition)
    'Frontiers in Plant Science', 'Scientific Reports', 'BMC Genomics', 'BMC Biology',
    'Plant Methods', 'Plant Phenomics', 'Plant Diversity',
    'Physiologia Plantarum', 'Environmental and Experimental Botany',
    'Frontiers in Genetics', 'Genes', 'International Journal of Molecular Sciences',
    'Biology', 'Development', 'Cell Research', 'Molecular Biology and Evolution',
    'iScience', 'Plant Science', 'Frontiers in Microbiology',
    'Computational and Structural Biotechnology Journal',
    'Briefings in Bioinformatics', 'GigaScience',
    'Nature Protocols', 'STAR Protocols',
    'bioRxiv', 'Research Square',
    # V2 additions — previously filtered journals
    'Plant Disease', 'Molecular Biotechnology', 'AMB Express',
    'Journal of Applied Genetics', 'The ISME Journal', 'Bio-protocol',
    'International Journal of Phytoremediation', 'Nanoscale',
    'Journal of Chemical Information and Modeling',
    'Brazilian Journal of Biology', 'Veterinary Research Communications',
    'BMC Microbiology', 'Microbiome', 'Environmental Microbiology',
    'mSystems', 'Applied and Environmental Microbiology',
    'Food Chemistry', 'Journal of Agricultural and Food Chemistry',
    'Plant Foods for Human Nutrition', 'Agronomy',
    'Crop Science', 'Field Crops Research', 'European Journal of Agronomy',
    'Industrial Crops and Products', 'Postharvest Biology and Technology',
    'Scientia Horticulturae', 'Tree Physiology', 'Forests',
    'AoB Plants', 'Plant Biology', 'Functional Plant Biology',
    'Journal of Plant Physiology', 'Plant Growth Regulation',
    'Plant Cell Reports', 'Plant Biotechnology Reports',
    'Transgenic Research', 'GM Crops & Food',
    'Metabolomics', 'Proteomics', 'Journal of Proteome Research',
    'Molecular & Cellular Proteomics', 'Analytical Chemistry',
    'Nature Food', 'Nature Sustainability', 'Nature Ecology & Evolution',
    'Ecology Letters', 'Global Change Biology', 'New Forests',
    'BMC Research Notes', 'Data in Brief', 'Scientific Data',
    'F1000Research', 'PeerJ', 'PLOS ONE', 'PLOS Genetics', 'PLOS Biology',
    'eLife', 'Open Biology', 'Royal Society Open Science',
    'ACS Synthetic Biology', 'Synthetic Biology', 'Metabolic Engineering',
    'Biotechnology for Biofuels', 'Biotechnology Advances',
    'Current Opinion in Biotechnology', 'Trends in Biotechnology',
    'ACS Omega', 'RSC Advances', 'Heliyon',
    'Cell Reports Methods', 'Cell Systems', 'Cell Host & Microbe',
    'Molecular Systems Biology', 'Science Signaling',
    'Journal of Biological Chemistry', 'Molecular Biology of the Cell',
    'Journal of Cell Biology', 'Journal of Cell Science',
    'Development', 'Developmental Biology',
    'Plant Signaling & Behavior', 'Plant Biotechnology',
    'Phytopathology', 'Virology Journal', 'Viruses',
    # Methods / protocols
    'Cold Spring Harbor Protocols', 'Methods in Molecular Biology',
    'Journal of Visualized Experiments', 'Current Protocols',
    # Preprint servers
    'bioRxiv', 'Research Square', 'ResearchGate',
    'arXiv',
}
# Case-insensitive exact match set for fast lookup
JOURNAL_EXACT_LOWER = {j.lower() for j in JOURNAL_EXACT}
# Broad keyword match — any journal name containing these keywords is automatically accepted
# NOTE: is_plant check still filters to plant-relevant papers only
JOURNAL_KEYWORDS = [
    # Plant/agriculture core
    'plant', 'botany', 'botanical', 'crop', 'agri', 'hortic', 'flora',
    'forest', 'tree', 'wood', 'xylem', 'phloem', 'phytochem', 'phyto',
    'weed', 'seed', 'fruit', 'veget', 'grain', 'breed', 'cultiv',
    'farm', 'soil', 'fertil', 'pest', 'herb', 'nemat',
    # Biology broad
    'bio', 'biolog', 'molecul', 'cellular', 'biochem', 'protein',
    'genom', 'genet', 'transcriptom', 'proteom', 'metabolom',
    'epigen', 'bioinform', 'computational biology',
    'rna', 'dna', 'gene express', 'phenotyp',
    # Omics / single-cell / spatial
    'single cell', 'single-cell', 'single nucleus', 'spatial',
    'omics', 'multi-omics', 'atac', 'rna-seq', 'scrna',
    # Microbiology / microbiome
    'microbiol', 'microbiom', 'mycolog', 'virol', 'bacteriol',
    'fung', 'isme', 'pathogen', 'symbios',
    # Biotechnology / methods
    'biotechnol', 'synth', 'metabolic', 'engin',
    'protocol', 'method', 'techniq', 'technol',
    'imag', 'sensor', 'spectro', 'chromatograph', 'mass spec',
    # Development / physiology
    'development', 'growth', 'reproduction', 'differentiation',
    'morphogen', 'organogen', 'embryo',
    # Photosynthesis / light
    'photosynth', 'chloroplast', 'mitochond', 'light',
    'circadian', 'photoperiod', 'photomorphogen',
    # Stress / immunity
    'immunity', 'defense', 'stress', 'resist', 'antioxid',
    'drought', 'salt', 'cold', 'heat', 'heavy metal',
    # Environment / ecology
    'environment', 'ecology', 'ecosystem', 'climate',
    'atmospher', 'carbon', 'nitrogen', 'water',
    # Chemistry / food
    'chem', 'food', 'nutri', 'pharma', 'toxic', 'nano',
    'natural product', 'metabolit',
    # General science / broad journals
    'scien', 'nature', 'research', 'advanc', 'frontier',
    'progress', 'review', 'report', 'communication',
    'proceedings', 'annals', 'journal of', 'international',
    'america', 'europe', 'china', 'royal society',
    # Open access / specific publishers
    'plos', 'peerj', 'elife', 'f1000', 'biorxiv', 'arxiv',
    'mdpi', 'frontiers', 'bmc', 'springer', 'wiley',
    # Data / computation
    'data', 'comput', 'informatic', 'algorithm',
    # Edge cases from previously filtered journals
    'express', 'acs', 'mater', 'appl',
]


def get_existing_dois():
    dois = set()
    for fname in os.listdir(f"{BASE}/concepts"):
        if not fname.endswith('.md'): continue
        with open(f"{BASE}/concepts/{fname}",'r',encoding='utf-8') as f:
            for m in re.finditer(r'doi:\s*(10\.\d{4,}/[^\s\n]+)', f.read(), re.I):
                dois.add(m.group(1).strip())
    return dois

def search_pubmed(query, days=1, max_results=10):
    from_date = (datetime.now() - timedelta(days=days)).strftime('%Y/%m/%d')
    full_query = f'({query}) AND ("{from_date}"[Date - Publication] : "3000"[Date - Publication])'
    encoded = urllib.parse.quote(full_query[:500])
    proc = subprocess.run(['curl','-sL','--connect-timeout','10',
        f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={encoded}&retmax={max_results}&sort=date&retmode=json'],
        capture_output=True, text=True, timeout=15)
    data = json.loads(proc.stdout)
    return data.get('esearchresult',{}).get('idlist',[])

def fetch_full_paper(pmid):
    """Fetch COMPLETE paper metadata from PubMed"""
    proc = subprocess.run(['curl','-sL','--connect-timeout','10',
        f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml'],
        capture_output=True, text=True, timeout=15)
    try:
        root = ET.fromstring(proc.stdout)
    except (ET.ParseError, Exception) as e:
        # PubMed may return malformed XML for some records
        print(f"  ⚠ XML parse error for PMID:{pmid}: {e}", file=sys.stderr)
        return None
    art = root.find('.//PubmedArticle')
    if art is None: return None
    
    title = art.find('.//ArticleTitle').text or ''
    journal_el = art.find('.//Journal/Title')
    journal = journal_el.text if journal_el is not None else ''
    year_el = art.find('.//PubDate/Year')
    year = year_el.text if year_el is not None else ''
    
    # Full structured abstract
    abstract_parts = []
    for s in art.findall('.//AbstractText'):
        label = s.get('Label','')
        txt = s.text or ''
        if txt: abstract_parts.append(f"{label}: {txt}" if label else txt)
    abstract = '\n\n'.join(abstract_parts) if abstract_parts else ''
    if not abstract:
        abs_el = art.find('.//AbstractText')
        if abs_el is not None: abstract = abs_el.text or ''
    
    # DOI and PMCID
    doi = ''
    pmcid = ''
    for aid in art.findall('.//ArticleId'):
        t = aid.get('IdType','')
        if t == 'doi': doi = aid.text or ''
        elif t == 'pmc': pmcid = aid.text or ''
    
    # Authors
    authors = art.findall('.//Author')
    author_list = []
    for a in authors[:10]:
        l = a.find('LastName'); f = a.find('ForeName')
        author_list.append(f"{f.text if f is not None else ''} {l.text if l is not None else ''}")
    first_author = author_list[0] if author_list else ''
    
    # MeSH keywords
    meshes = art.findall('.//MeshHeading/DescriptorName')
    keywords = [m.text for m in meshes[:10] if m.text]
    
    # Check if plant species is in title/abstract (validate it's really a plant paper)
    is_plant = any(sp in (title + abstract).lower() for sp in 
        ['plant','arabidopsis','rice','wheat','maize','soybean','tomato','poplar','cotton',
         'tobacco','potato','grape','tea','alfalfa','barley','marchantia','brassica',
         'cassava','sorghum','sunflower','peanut','chrysanthemum','salvia','artemisia',
         'panax','andrographis','physcomitrium','cucumber','watermelon','spinach','capsicum'])
    
    return {
        'pmid': pmid, 'pmcid': pmcid, 'doi': doi, 'title': title,
        'journal': journal, 'year': year, 'first_author': first_author,
        'authors': author_list, 'abstract': abstract, 'keywords': keywords,
        'is_plant': is_plant
    }

def main():
    # Parse args (handle both --days=1 and --days 1, --max 50)
    days = 1
    max_results = 10
    auto_import = '--import' in sys.argv
    for i, arg in enumerate(sys.argv):
        if arg == '--days' and i+1 < len(sys.argv):
            days = int(sys.argv[i+1])
        elif arg.startswith('--days='):
            days = int(arg.split('=')[1])
        elif arg == '--max' and i+1 < len(sys.argv):
            max_results = int(sys.argv[i+1])
        elif arg.startswith('--max='):
            max_results = int(arg.split('=')[1])
    
    print(f"🔍 检索最近 {days} 天植物学文献...")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    existing_dois = get_existing_dois()
    all_pmids = set()
    
    for q in SEARCH_QUERIES:
        pmids = search_pubmed(q, days=days, max_results=max_results)
        all_pmids.update(pmids)
    
    print(f"📊 PubMed 候选: {len(all_pmids)} 篇")
    
    new_papers = []
    for pmid in sorted(all_pmids)[:max(100, max_results * len(SEARCH_QUERIES))]:
        p = fetch_full_paper(pmid)
        if not p or not p['doi']: continue
        
        if p['doi'] in existing_dois:
            continue
        
        # Journal filter (case-insensitive + keyword-based)
        journal_lower = p['journal'].lower()
        journal_ok = False
        # 0) JCR 2024 植物/农学权威名单精确匹配 (highest priority, additive)
        if journal_in_jcr(p['journal']):
            journal_ok = True
        # 1) exact case-insensitive match
        elif journal_lower in JOURNAL_EXACT_LOWER:
            journal_ok = True
        # 2) keyword-based match (e.g. "Plant phenomics (Washington, D.C.)")
        if not journal_ok:
            for kw in JOURNAL_KEYWORDS:
                if kw in journal_lower:
                    journal_ok = True
                    break
        if not journal_ok:
                continue
        
        # Must be plant-related
        if not p['is_plant']:
            continue
        
        # ── 主题相关性双重重判 (2026-08-25 防污染防线): 拦截人类/动物医学/能源/社科 ──
        try:
            from theme_filter import is_relevant_plant_paper
            ok, why = is_relevant_plant_paper(p['title'], p['abstract'], p['journal'])
            if not ok:
                print(f"     ⛔ 主题过滤拒绝 (非植物): {why} | {p['title'][:45]}")
                continue
        except ImportError:
            pass
        
        new_papers.append(p)
        ab_preview = p['abstract'][:100].replace('\n',' ')
        print(f"  ✅ {p['title'][:65]}")
        print(f"     {p['journal']} ({p['year']}) | PMID:{p['pmid']} | {p['first_author']}")
        print(f"     {ab_preview}...")
    
    print(f"\n📋 待导入: {len(new_papers)} 篇")
    
    if auto_import and new_papers:
        print("\n📥 导入完整论文...")
        imported = 0
        for p in new_papers:
            slug = f"daily-{p['pmid']}"
            
            # Full concept page
            content = f"""---
title: {p['title'][:80]}
created: {datetime.now().strftime('%Y-%m-%d')}
type: concept
tags: [papers]
pmid: {p['pmid']}
doi: {p['doi']}
confidence: high
---

# {p['title']}

## 论文信息
- **期刊**: {p['journal']} ({p['year']})
- **PMID**: [{p['pmid']}](https://pubmed.ncbi.nlm.nih.gov/{p['pmid']}/)
- **DOI**: [{p['doi']}](https://doi.org/{p['doi']})
- **第一作者**: {p['first_author']}
- **作者**: {', '.join(p['authors'][:8])}

## 摘要
{p['abstract'][:3000]}

## 关键词
{', '.join(p['keywords']) if p['keywords'] else '—'}

## 深度提炼

**物种**: {'plant' if p['is_plant'] else '—'}
**来源**: PMID:{p['pmid']} | DOI:{p['doi']}
"""
            with open(f"{BASE}/concepts/{slug}.md",'w',encoding='utf-8') as f:
                f.write(content)
            
            # Raw article
            with open(f"{BASE}/raw/articles/{slug}.md",'w',encoding='utf-8') as f:
                f.write(f"---\ningested: {datetime.now().strftime('%Y-%m-%d')}\npmid: {p['pmid']}\ndoi: {p['doi']}\n---\n\n# {p['title']}\n\n{p['abstract']}")
            imported += 1
        
        print(f"✅ 导入: {imported} 篇")
        
        # Update index
        idx_path = f'{BASE}/index.md'
        if os.path.exists(idx_path):
            with open(idx_path,'r',encoding='utf-8') as f:
                lines = f.readlines()
            for i, line in enumerate(lines):
                if '## Comparisons' in line:
                    for j, p in enumerate(new_papers):
                        slug = f"daily-{p['pmid']}"
                        lines.insert(i+j, f"- [[{slug}]] — {p['title'][:55]} ({p['journal']} {p['year']})\n")
                    break
            with open(idx_path,'w',encoding='utf-8') as f:
                f.writelines(lines)
    
    # Report
    with open(f"{BASE}/daily_report.md",'w',encoding='utf-8') as f:
        f.write(f"# 每日文献更新报告\n\n{datetime.now().strftime('%Y-%m-%d')}\n\n")
        f.write(f"检索: {len(all_pmids)} 篇\n导入: {len(new_papers)} 篇\n\n")
        for p in new_papers:
            f.write(f"- {p['title']} ({p['journal']} {p['year']}) PMID:{p['pmid']}\n")
    
    print(f"\n📄 报告: {BASE}/daily_report.md")

if __name__ == '__main__':
    main()
