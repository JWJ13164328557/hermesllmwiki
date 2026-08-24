#!/usr/bin/env python3
"""基于PubMed完整摘要的深度提炼"""
import os, re

BASE = '/mnt/g/hermes_obsidian/hermes'
concepts_dir = f'{BASE}/concepts'

curated = 0
for fname in sorted(os.listdir(concepts_dir)):
    if not fname.endswith('.md') or fname.startswith('ref') or fname.startswith('xr') or fname.startswith('cr-'):
        continue
    path = f'{concepts_dir}/{fname}'
    with open(path,'r',encoding='utf-8') as f:
        content = f.read()
    
    # Remove old 深度提炼 if shallow
    cur = re.search(r'## 深度提炼\n\n(.*?)(?=\n## |\n---|\Z)', content, re.DOTALL)
    is_shallow = cur and len(cur.group(1)) < 300
    if is_shallow or '## 深度提炼' not in content:
        pass  # will replace
    else:
        continue  # already deep
    
    # Get abstract
    ab = re.search(r'## 摘要\n\n(.+?)(?=\n## |\Z)', content, re.DOTALL)
    if not ab: continue
    abstract = ab.group(1).strip()
    if len(abstract) < 100: continue
    
    # Title
    tm = re.search(r'(?:^# |title:\s*)(.+)', content, re.M)
    title = tm.group(1).strip()[:80] if tm else fname
    
    # Species detection
    species = set()
    sp_map = {
        'Arabidopsis': ['arabidopsis','拟南芥'],
        'rice': ['rice','水稻','Oryza'],
        'wheat': ['wheat','小麦','Triticum'],
        'maize': ['maize','玉米','Zea mays'],
        'soybean': ['soybean','大豆','Glycine'],
        'tobacco': ['tobacco','烟草','Nicotiana'],
        'poplar': ['poplar','杨树','Populus'],
        'grape': ['grape','葡萄','Vitis'],
        'potato': ['potato','马铃薯'],
        'tomato': ['tomato','番茄'],
        'cotton': ['cotton','棉花','Gossypium'],
    }
    text_lower = (title + ' ' + abstract).lower()
    for sp, kws in sp_map.items():
        if any(kw.lower() in text_lower for kw in kws):
            species.add(sp)
    
    # Method detection from abstract
    methods = []
    m_map = {
        'scRNA-seq': ['single.cell','scrna.seq','single cell rna'],
        'snRNA-seq': ['single.nucleus','snrna'],
        'Spatial transcriptomics': ['spatial transcriptom','stereo.seq','visium'],
        'ATAC-seq': ['atac.seq'],
        'ChIP-seq': ['chip.seq'],
        'CRISPR': ['crispr'],
        'GWAS': ['gwas','genome.wide association'],
        'Proteomics': ['proteom'],
        'Metabolomics': ['metabolom'],
    }
    for m, kws in m_map.items():
        if any(kw.lower().replace('-','.') in text_lower.replace('-','.') for kw in kws):
            methods.append(m)
    
    # Key findings extraction
    findings = []
    sentences = re.split(r'(?<=[.。!?])\s+', abstract)
    for s in sentences:
        s = s.strip()
        if len(s) < 40: continue
        
        score = 0
        s_lower = s.lower()
        
        # High-value verbs
        for v in ['reveal','demonstrat','show','identif','discover','uncover','elucidat',
                  'establish','confirm','validat','provid evidence']:
            if v in s_lower: score += 2
        # Medium verbs
        for v in ['suggest','indicat','implicat','contribut','mediat','regulat']:
            if v in s_lower: score += 1
        # Key concepts
        for c in ['mechanism','pathway','signaling','cascade','network','module',
                  'transcription factor','phosphorylat','interaction','binding',
                  'biosynthesis','development','differentiation','stress','immun',
                  'tolerance','resistance','regeneration','senescence','metabolism',
                  'epigenetic','chromatin','degradation','transport','gradient']:
            if c in s_lower: score += 1
        
        if score >= 2:
            s_clean = re.sub(r'\s+',' ',s)[:200]
            findings.append(s_clean)
    
    # Build curation
    curation = "\n## 深度提炼\n"
    if species:
        curation += f"\n**物种**: {', '.join(sorted(species))}\n"
    if methods:
        curation += f"**方法**: {', '.join(methods)}\n"
    
    curation += "\n### 核心发现\n\n"
    if findings:
        for f in findings[:10]:
            curation += f"- {f}\n"
    else:
        curation += f"- {abstract[:300]}\n"
    
    # Source
    pmid = re.search(r'pmid:\s*(\d+)', content, re.I)
    doi = re.search(r'doi:\s*(10\.\d{4,}/[^\s\n]+)', content, re.I)
    p = pmid.group(1) if pmid else ''
    d = doi.group(1).strip() if doi else ''
    curation += f"\n**来源**: {'PMID:'+p if p else ''} {'DOI:'+d if d else ''}\n"
    
    # Update file
    if '## 深度提炼' in content:
        content = re.sub(r'\n## 深度提炼.*$', '', content, flags=re.DOTALL)
    with open(path,'w',encoding='utf-8') as f:
        f.write(content + curation)
    curated += 1

print(f"Deep curated: {curated} papers")
