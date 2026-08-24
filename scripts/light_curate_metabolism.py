#!/usr/bin/env python3
"""针对 153 篇代谢论文的轻量深度提炼 — 从已有摘要提取物种/方法/核心发现
不下载 PMC 全文，仅用 Crossref 摘要"""
import os, re, json

BASE = '/mnt/g/hermes_obsidian/hermes'
CONCEPTS_DIR = os.path.join(BASE, 'concepts', 'papers')

# ---- Curation rules ----
SPECIES_MAP = {
    'arabidopsis': 'Arabidopsis thaliana', 'rice': 'Oryza sativa',
    'maize': 'Zea mays', 'corn': 'Zea mays',
    'tomato': 'Solanum lycopersicum', 'apple': 'Malus domestica',
    'malus': 'Malus domestica', 'tea': 'Camellia sinensis',
    'camellia sinensis': 'Camellia sinensis',
    'ginkgo': 'Ginkgo biloba', 'grape': 'Vitis vinifera',
    'vitis': 'Vitis vinifera',
    'potato': 'Solanum tuberosum', 'tobacco': 'Nicotiana tabacum',
    'nicotiana': 'Nicotiana tabacum',
    'soybean': 'Glycine max', 'glycine max': 'Glycine max',
    'brassica napus': 'Brassica napus', 'rapeseed': 'Brassica napus',
    'canola': 'Brassica napus',
    'citrus': 'Citrus spp.', 'orange': 'Citrus sinensis',
    'lemon': 'Citrus limon',
    'strawberry': 'Fragaria × ananassa', 'fragaria': 'Fragaria × ananassa',
    'pear': 'Pyrus spp.', 'pyrus': 'Pyrus spp.',
    'peach': 'Prunus persica', 'prunus persica': 'Prunus persica',
    'kiwifruit': 'Actinidia spp.', 'actinidia': 'Actinidia spp.',
    'rose': 'Rosa spp.', 'rosa': 'Rosa spp.',
    'medicago': 'Medicago truncatula', 'alfalfa': 'Medicago sativa',
    'salvia miltiorrhiza': 'Salvia miltiorrhiza', 'danshen': 'Salvia miltiorrhiza',
    'panax': 'Panax spp.', 'ginseng': 'Panax ginseng',
    'buckwheat': 'Fagopyrum esculentum', 'fagopyrum': 'Fagopyrum esculentum',
    'cassava': 'Manihot esculenta', 'manihot': 'Manihot esculenta',
    'banana': 'Musa spp.', 'musa': 'Musa spp.',
    'lily': 'Lilium spp.', 'lilium': 'Lilium spp.',
    'blueberry': 'Vaccinium spp.', 'vaccinium': 'Vaccinium spp.',
    'peony': 'Paeonia spp.', 'paeonia': 'Paeonia spp.',
    'pomegranate': 'Punica granatum', 'punica': 'Punica granatum',
    'mulberry': 'Morus alba', 'morus': 'Morus alba',
    'goji': 'Lycium barbarum', 'wolfberry': 'Lycium barbarum', 'lycium': 'Lycium barbarum',
    'safflower': 'Carthamus tinctorius', 'carthamus': 'Carthamus tinctorius',
    'eucalyptus': 'Eucalyptus spp.',
    'poplar': 'Populus spp.', 'populus': 'Populus spp.',
    'catharanthus': 'Catharanthus roseus',
    'miscanthus': 'Miscanthus spp.',
    'dioscorea': 'Dioscorea spp.', 'yam': 'Dioscorea spp.',
    'artemisia': 'Artemisia annua', 'sagebrush': 'Artemisia spp.',
    'crocus': 'Crocus sativus', 'saffron': 'Crocus sativus',
    'fig': 'Ficus carica', 'ficus': 'Ficus carica',
    'ginger': 'Zingiber officinale', 'zingiber': 'Zingiber officinale',
    'capsicum': 'Capsicum annuum', 'pepper': 'Capsicum annuum',
    'cucumis': 'Cucumis spp.', 'cucumber': 'Cucumis sativus', 'melon': 'Cucumis melo',
    'coptis': 'Coptis spp.',
    'coffee': 'Coffea spp.', 'coffea': 'Coffea spp.',
    'taxus': 'Taxus spp.', 'taxol': 'Taxus brevifolia',
    'rhododendron': 'Rhododendron spp.',
    'cotton': 'Gossypium hirsutum', 'gossypium': 'Gossypium hirsutum',
    'forsythia': 'Forsythia spp.',
    'chrysanthemum': 'Chrysanthemum spp.',
    'polygonum': 'Fallopia multiflora', 'fallopia': 'Fallopia multiflora',
    'walnut': 'Juglans regia', 'juglans': 'Juglans regia',
    'spinach': 'Spinacia oleracea',
    'kale': 'Brassica oleracea', 'broccoli': 'Brassica oleracea',
    'cabbage': 'Brassica oleracea',
    'wheat': 'Triticum aestivum', 'triticum': 'Triticum aestivum',
    'barley': 'Hordeum vulgare', 'hordeum': 'Hordeum vulgare',
    'sorghum': 'Sorghum bicolor',
    'sugarcane': 'Saccharum spp.',
    'pineapple': 'Ananas comosus',
    'coconut': 'Cocos nucifera',
    'date palm': 'Phoenix dactylifera',
    'oil palm': 'Elaeis guineensis',
    'papaya': 'Carica papaya',
    'cacao': 'Theobroma cacao',
    'avocado': 'Persea americana',
    'mango': 'Mangifera indica',
    'olive': 'Olea europaea',
    'lavender': 'Lavandula angustifolia',
    'peppermint': 'Mentha × piperita',
    'basil': 'Ocimum basilicum',
    'oregano': 'Origanum vulgare',
    'thyme': 'Thymus vulgaris',
    'sage': 'Salvia officinalis',
    'rosemary': 'Salvia rosmarinus',
    'coriander': 'Coriandrum sativum',
    'cumin': 'Cuminum cyminum',
    'fennel': 'Foeniculum vulgare',
    'dill': 'Anethum graveolens',
    'parsley': 'Petroselinum crispum',
    'celery': 'Apium graveolens',
    'carrot': 'Daucus carota',
    'onion': 'Allium cepa',
    'garlic': 'Allium sativum',
    'leek': 'Allium ampeloprasum',
    'asparagus': 'Asparagus officinalis',
    'artichoke': 'Cynara cardunculus',
    'lettuce': 'Lactuca sativa',
    'endive': 'Cichorium endivia',
    'chicory': 'Cichorium intybus',
    'petunia': 'Petunia × hybrida',
    'snapdragon': 'Antirrhinum majus',
    'morning glory': 'Ipomoea nil',
    'ipomoea': 'Ipomoea batatas',
    'sweet potato': 'Ipomoea batatas',
    'rubber': 'Hevea brasiliensis',
    'hevea': 'Hevea brasiliensis',
}

METHOD_MAP = {
    'transcriptom': 'transcriptomics (RNA-seq)',
    'rna-seq': 'transcriptomics (RNA-seq)',
    'rnaseq': 'transcriptomics (RNA-seq)',
    'metabolom': 'metabolomics (LC-MS/GC-MS)',
    'lc-ms': 'metabolomics (LC-MS/GC-MS)',
    'gc-ms': 'metabolomics (LC-MS/GC-MS)',
    'multi-omics': 'multi-omics integration',
    'multi-omic': 'multi-omics integration',
    'proteom': 'proteomics',
    'genom': 'genomics (genome assembly/annotation)',
    'genome-wide': 'genomics (GWAS/genome-wide)',
    'single-cell': 'single-cell RNA-seq',
    'scrna-seq': 'single-cell RNA-seq',
    'spatial': 'spatial transcriptomics',
    'qRT-PCR': 'qRT-PCR validation',
    'yeast two-hybrid': 'protein-protein interaction (Y2H)',
    'y2h': 'protein-protein interaction (Y2H)',
    'bimolecular fluorescence': 'protein-protein interaction (BiFC)',
    'bifc': 'protein-protein interaction (BiFC)',
    'co-immunoprecipitation': 'protein-protein interaction (Co-IP)',
    'co-ip': 'protein-protein interaction (Co-IP)',
    'chromatin immunoprecipitation': 'ChIP-seq',
    'chip-seq': 'ChIP-seq',
    'chip-qpcr': 'ChIP-qPCR',
    'emsa': 'EMSA (DNA-protein binding)',
    'dual-luciferase': 'dual-luciferase reporter assay',
    'luciferase': 'dual-luciferase reporter assay',
    'overexpress': 'transgenic overexpression',
    'knockout': 'gene knockout (CRISPR/Cas9)',
    'knockdown': 'gene silencing (RNAi/VIGS)',
    'crispr': 'gene knockout (CRISPR/Cas9)',
    'overexpression': 'transgenic overexpression',
    'vig': 'gene silencing (VIGS)',
    'rna interference': 'gene silencing (RNAi)',
}

def detect_species(text):
    text_lower = text.lower()
    found = []
    for kw, name in SPECIES_MAP.items():
        if kw in text_lower:
            found.append(name)
    # deduplicate
    seen = set()
    result = []
    for s in found:
        if s not in seen:
            seen.add(s)
            result.append(s)
    return result[:5] if result else ['Plant (unspecified)']

def detect_methods(text):
    text_lower = text.lower()
    methods = []
    for kw, method_name in METHOD_MAP.items():
        if kw in text_lower and method_name not in methods:
            methods.append(method_name)
    return methods[:6] if methods else ['transcriptomics/metabolomics']

def extract_findings(abstract):
    """从摘要中提取核心发现（基于关键信号词）"""
    if not abstract: return []
    
    # Clean
    text = re.sub(r'<[^>]+>', '', abstract)
    text = re.sub(r'\s+', ' ', text)
    
    # Split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    findings = []
    signal_words = [
        r'\b(we\s+found|we\s+show|we\s+demonstrate|we\s+reveal|we\s+identif)',
        r'\b(our\s+results|these\s+results|this\s+study\s+(reveals|demonstrates|shows|identifies|provides))',
        r'\b(suggest(ing|s)?\s+that|indicat(es?|ing)\s+that)',
        r'\b(conclus|importantly|notably|significantly)',
        r'\b(key|critical|essential|novel|new)\s+(role|function|mechanism|pathway|regulator)',
    ]
    
    seen = set()
    for sent in sentences:
        sent = sent.strip()
        if len(sent) < 30: continue
        if len(sent) > 400: sent = sent[:400] + '...'
        
        for pattern in signal_words:
            if re.search(pattern, sent, re.I):
                # deduplicate by start
                key = sent[:60]
                if key not in seen:
                    seen.add(key)
                    findings.append(sent)
                break
        
        if len(findings) >= 8:
            break
    
    # Fallback: take scientifically dense sentences
    if len(findings) < 3:
        for sent in sentences:
            sent = sent.strip()
            if len(sent) < 30: continue
            if len(sent) > 400: sent = sent[:400] + '...'
            # Prefer sentences with gene names, compound names, or mechanism words
            if re.search(r'[A-Z]{2,}[a-z]{2,}[A-Z]|[A-Z][a-z]{2,}\d', sent):  # gene-like
                key = sent[:60]
                if key not in seen:
                    seen.add(key)
                    findings.append(sent)
            if len(findings) >= 6:
                break
    
    return findings[:8]

def main():
    # Find new metabolism pages (created 2026-05-30)
    candidates = []
    for fname in os.listdir(CONCEPTS_DIR):
        if not fname.endswith('.md'): continue
        path = os.path.join(CONCEPTS_DIR, fname)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
        except: continue
        
        if 'created: 2026-05-30' not in content: continue
        if 'metabolism' not in content.split('tags:')[1].split('\n')[0] if 'tags:' in content else False: continue
        
        # Extract title and abstract
        title = ''
        abstract = ''
        tm = re.search(r'^# (.+)$', content, re.M)
        if tm: title = tm.group(1)
        am = re.search(r'## 摘要\n(.+?)(?=\n## |\n---|\Z)', content, re.DOTALL)
        if am: abstract = am.group(1).strip()
        
        # Skip if already has 深度提炼
        if '### 核心发现' in content:
            continue
        
        candidates.append((fname, path, title, abstract, content))
    
    print(f"Candidates for curation: {len(candidates)}")
    
    curated = 0
    for fname, path, title, abstract, original in candidates:
        species = detect_species(title + ' ' + abstract)
        methods = detect_methods(abstract)
        findings = extract_findings(abstract)
        
        # Build curation section
        species_str = ', '.join(species)
        methods_str = ', '.join(methods)
        
        findings_str = ''
        if findings:
            findings_str = '\n'.join(f'{i+1}. {f}' for i, f in enumerate(findings))
        else:
            findings_str = '_（待从全文提取）_'
        
        doi_val = ''
        dm = re.search(r'doi:\s*(10\.\d{4,}/[^\s\n]+)', original, re.I)
        if dm: doi_val = dm.group(1)
        
        curation = f"""
## 深度提炼

**物种**: {species_str}
**方法**: {methods_str}
**来源**: DOI:{doi_val}

### 核心发现
{findings_str}
"""
        
        # Replace or append
        if '## 深度提炼' not in original:
            new_content = original.rstrip() + '\n' + curation
        else:
            # Replace existing curation section
            new_content = re.sub(
                r'## 深度提炼.*?(?=\n## (?!深度)|---\n\n\Z|\Z)',
                curation.strip(),
                original, flags=re.DOTALL
            )
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        curated += 1
        
        if curated % 30 == 0:
            print(f"  Curated {curated}...")
    
    print(f"\n=== Done: {curated} papers curated ===")

if __name__ == '__main__':
    main()
