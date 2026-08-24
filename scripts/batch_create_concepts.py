#!/usr/bin/env python3
"""从 metadata_batch.json 批量创建概念页"""
import json, os, re, textwrap
from datetime import datetime
from collections import Counter

JSON_PATH = '/mnt/g/hermes_obsidian/hermes/raw/papers/metabolism/metadata_batch.json'
CONCEPTS_DIR = '/mnt/g/hermes_obsidian/hermes/concepts/papers'

# Tag mapping based on content keywords
TAG_KEYWORDS = {
    'flavonoid': ['flavonoid', 'anthocyanin', 'proanthocyanidin', 'flavonol', 'flavanone', 'isoflavone', 'flavan-3-ol'],
    'terpenoid': ['terpenoid', 'terpene', 'carotenoid', 'ginsenoside', 'tanshinone', 'artemisinin', 'saponin', 'monoterpene', 'sesquiterpene'],
    'alkaloid': ['alkaloid', 'caffeine', 'theanine', 'nicotine', 'theobromine', 'morphine'],
    'phenylpropanoid': ['phenylpropanoid', 'lignin', 'lignan', 'coumarin', 'phenolic acid'],
    'lipid': ['lipid', 'oil', 'fatty acid', 'triacylglycerol', 'wax', 'cuticle', 'cutin'],
    'starch-sugar': ['starch', 'sugar', 'sucrose', 'glucose', 'fructose', 'carbohydrate', 'cellulose', 'hemicellulose'],
}

SPECIES_KEYWORDS = {
    'Arabidopsis thaliana': ['arabidopsis', 'arabidopsis thaliana'],
    'Oryza sativa': ['rice', 'oryza sativa'],
    'Zea mays': ['maize', 'corn', 'zea mays'],
    'Solanum lycopersicum': ['tomato', 'solanum lycopersicum'],
    'Malus domestica': ['apple', 'malus domestica', 'malus × domestica'],
    'Camellia sinensis': ['tea', 'camellia sinensis'],
    'Ginkgo biloba': ['ginkgo', 'ginkgo biloba'],
    'Vitis vinifera': ['grape', 'vitis vinifera'],
    'Solanum tuberosum': ['potato', 'solanum tuberosum'],
    'Nicotiana tabacum': ['tobacco', 'nicotiana tabacum'],
    'Glycine max': ['soybean', 'glycine max'],
    'Brassica napus': ['rapeseed', 'brassica napus', 'canola'],
    'Citrus': ['citrus', 'orange', 'lemon'],
    'Fragaria': ['strawberry', 'fragaria'],
    'Pyrus': ['pear', 'pyrus'],
    'Prunus persica': ['peach', 'prunus persica'],
    'Actinidia': ['kiwifruit', 'actinidia'],
    'Rosa': ['rose', 'rosa'],
    'Medicago': ['medicago', 'alfalfa'],
    'Salvia miltiorrhiza': ['salvia miltiorrhiza', 'danshen', '丹参'],
    'Panax': ['panax', 'ginseng'],
    'Fagopyrum': ['buckwheat', 'fagopyrum'],
    'Manihot esculenta': ['cassava', 'manihot'],
    'Musa': ['banana', 'musa'],
    'Lilium': ['lily', 'lilium'],
    'Vaccinium': ['blueberry', 'vaccinium'],
    'Paeonia': ['peony', 'paeonia'],
    'Punica granatum': ['pomegranate', 'punica'],
    'Morus': ['mulberry', 'morus'],
    'Lycium': ['goji', 'wolfberry', 'lycium'],
    'Carthamus': ['safflower', 'carthamus'],
    'Eucalyptus': ['eucalyptus'],
    'Populus': ['poplar', 'populus'],
    'Catharanthus': ['catharanthus'],
    'Miscanthus': ['miscanthus'],
    'Dioscorea': ['dioscorea', 'yam'],
    'Artemisia': ['artemisia', 'sagebrush'],
    'Crocus': ['crocus', 'saffron'],
    'Ficus': ['fig', 'ficus'],
    'Zingiber': ['ginger', 'zingiber'],
    'Capsicum': ['pepper', 'capsicum'],
    'Cucumis': ['cucumber', 'melon', 'cucumis'],
    'Coptis': ['coptis'],
    'Coffea': ['coffee', 'coffea'],
    'Taxus': ['taxus', 'taxol', 'paclitaxel'],
    'Rhododendron': ['rhododendron'],
}

METHOD_KEYWORDS = {
    'transcriptomics': ['transcriptom', 'rna-seq', 'rnaseq', 'transcriptome'],
    'metabolomics': ['metabolom', 'lc-ms', 'gc-ms', 'metabolite profil'],
    'multi-omics': ['multi-omics', 'multi-omic', 'integrated omics'],
    'genomics': ['genom', 'genome assembly', 'whole-genome'],
    'single-cell': ['single-cell', 'scrna-seq', 'single nucleus'],
    'spatial': ['spatial', 'stereo-seq', 'visium', 'msi'],
}

def detect_tags(title, abstract, journal):
    text = (title + ' ' + abstract).lower()
    tags = ['metabolism']
    for tag, kw_list in TAG_KEYWORDS.items():
        for kw in kw_list:
            if kw in text:
                tags.append(tag)
                break
    # Additional tags
    for tag, kw_list in METHOD_KEYWORDS.items():
        for kw in kw_list:
            if kw in text:
                tags.append(tag)
                break
    if not any(t in ['flavonoid', 'terpenoid', 'alkaloid', 'phenylpropanoid', 'lipid', 'starch-sugar'] for t in tags):
        tags.append('secondary-metabolism')
    return tags

def detect_species(title, abstract):
    text = (title + ' ' + abstract).lower()
    species = []
    for sp, kws in SPECIES_KEYWORDS.items():
        for kw in kws:
            if kw in text:
                species.append(sp)
                break
    return species if species else ['Plant (unspecified)']

def make_slug(title, doi):
    """Create a clean filename slug"""
    if not title:
        # Use DOI as fallback
        return doi.replace('/', '-').replace('.', '-')[:50]
    # Take first 4-5 words, replace spaces/specials
    words = re.sub(r'[^\w\s-]', '', title).strip().split()[:6]
    slug = '-'.join(words).lower()
    if len(slug) > 60:
        slug = slug[:60].rstrip('-')
    return slug

def main():
    with open(JSON_PATH, 'r') as f:
        data = json.load(f)
    
    # Only process entries with good data
    good = {k: v for k, v in data.items() if v.get('title') and not v.get('error')}
    
    # Check existing concepts to avoid duplicates
    existing_slugs = set()
    for fname in os.listdir(CONCEPTS_DIR):
        if fname.endswith('.md'):
            existing_slugs.add(fname.replace('.md', ''))
    
    # Also check DOI presence in existing concepts
    existing_dois = set()
    for fname in os.listdir(CONCEPTS_DIR):
        if not fname.endswith('.md'): continue
        try:
            with open(os.path.join(CONCEPTS_DIR, fname), 'r', encoding='utf-8') as f:
                content = f.read(2000)
            for m in re.finditer(r'doi:\s*(10\.\d{4,}/[^\s\n]+)', content, re.I):
                existing_dois.add(m.group(1).strip().rstrip('/'))
        except: pass
    
    created = 0
    skipped = 0
    today = datetime.now().strftime('%Y-%m-%d')
    
    for doi, meta in good.items():
        # Clean DOI (remove trailing /DCSupplemental etc)
        clean_doi = re.sub(r'/-.*$', '', doi)
        if clean_doi in existing_dois:
            skipped += 1
            continue
        
        title = meta['title']
        # Strip HTML tags from title
        title_clean = re.sub(r'<[^>]+>', '', title)
        title_clean = ' '.join(title_clean.split())
        
        slug = make_slug(title_clean, doi)
        # Ensure uniqueness
        base_slug = slug
        counter = 1
        while slug in existing_slugs:
            slug = f"{base_slug}-{counter}"
            counter += 1
        existing_slugs.add(slug)
        
        tags = detect_tags(title_clean, meta.get('abstract', ''), meta.get('journal', ''))
        species = detect_species(title_clean, meta.get('abstract', ''))
        
        authors_str = ', '.join(meta['authors'][:6]) if meta.get('authors') else ''
        pmid = meta.get('pmid', '')
        journal = meta.get('journal', '')
        year = meta.get('year', '')
        abstract = meta.get('abstract', '')
        
        content = f"""---
title: "{title_clean[:120]}"
created: {today}
type: concept
tags: [{', '.join(tags)}]
doi: {clean_doi}
pmid: {pmid or ''}
confidence: medium
---

# {title_clean}

## 论文信息
- **期刊**: {journal} ({year})
- **DOI**: [{clean_doi}](https://doi.org/{clean_doi})
{f'- **PMID**: [{pmid}](https://pubmed.ncbi.nlm.nih.gov/{pmid}/)' if pmid else ''}
- **作者**: {authors_str}

## 物种
{', '.join(species)}

## 摘要
{abstract[:3000]}

## 深度提炼

**来源**: DOI:{clean_doi}{' | PMID:' + pmid if pmid else ''}
**PDF**: raw/papers/metabolism/

"""
        filepath = os.path.join(CONCEPTS_DIR, f"{slug}.md")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        created += 1
        
        if created % 20 == 0:
            print(f"  Created {created} pages...")
    
    print(f"\n=== Phase 2 Complete ===")
    print(f"Created: {created}")
    print(f"Skipped (duplicate): {skipped}")
    print(f"Total in concepts/papers/: {len(os.listdir(CONCEPTS_DIR)) - sum(1 for f in os.listdir(CONCEPTS_DIR) if not f.endswith('.md'))} MD files")

if __name__ == '__main__':
    main()
