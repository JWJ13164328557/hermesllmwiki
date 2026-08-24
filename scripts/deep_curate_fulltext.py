#!/usr/bin/env python3
"""下载PMC全文 + 基于完整正文的深度提炼"""
import os, re, subprocess, json, time, sys

BASE = '/mnt/g/hermes_obsidian/hermes'

def get_pmcid(pmid):
    """Get PMCID from PubMed"""
    try:
        proc = subprocess.run(['curl','-sL','--connect-timeout','8',
            f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml'],
            capture_output=True, text=True, timeout=12)
        import xml.etree.ElementTree as ET
        root = ET.fromstring(proc.stdout)
        for aid in root.findall('.//ArticleId'):
            if aid.get('IdType') == 'pmc':
                return aid.text
    except: pass
    return None

def doi_to_pmid(doi):
    """Convert DOI to PMID via NCBI E-utilities"""
    from urllib.parse import quote
    try:
        encoded_doi = quote(f'{doi}[doi]', safe='')
        proc = subprocess.run(['curl','-sL','--connect-timeout','8',
            f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={encoded_doi}&retmode=json'],
            capture_output=True, text=True, timeout=12)
        data = json.loads(proc.stdout)
        id_list = data.get('esearchresult',{}).get('idlist',[])
        return id_list[0] if id_list else None
    except: pass
    return None

def download_pmc_fulltext(pmcid):
    """Download full text from PMC (classic HTML view)"""
    try:
        proc = subprocess.run(['curl','-sL','--connect-timeout','15',
            f'https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/?report=classic'],
            capture_output=True, text=True, timeout=30)
        html = proc.stdout
        if len(html) < 2000: return None
        
        body_start = html.find('<div class="tsec')
        if body_start < 0: body_start = html.find('<div class="sec')
        if body_start < 0: return None
        
        sections = []
        for m in re.finditer(r'<(?:div|h[2-4])[^>]*class="[^"]*(?:tsec|sec|section)[^"]*"[^>]*>(.*?)(?=<(?:div|h[2-4])[^>]*class="[^"]*(?:tsec|sec|section))', html[body_start:body_start+50000], re.DOTALL):
            text = m.group(1)
            title_m = re.search(r'<(?:h[2-4]|strong)[^>]*>(.*?)</(?:h[2-4]|strong)>', text, re.DOTALL)
            sec_title = re.sub(r'<[^>]+>','',title_m.group(1)).strip() if title_m else ''
            paras = re.findall(r'<p[^>]*>(.*?)</p>', text, re.DOTALL)
            para_texts = [re.sub(r'<[^>]+>',' ',p).strip() for p in paras]
            para_texts = [re.sub(r'\s+',' ',p) for p in para_texts if len(p)>20]
            
            if para_texts:
                sections.append({
                    'title': sec_title,
                    'text': ' '.join(para_texts[:3000])
                })
        
        if sections:
            return sections
    except: pass
    return None

def deep_curate_from_fulltext(slug, path, title, abstract, fulltext_sections):
    """Generate deep curation from full text"""
    all_text = title + ' ' + abstract
    if fulltext_sections:
        all_text += ' ' + ' '.join([s['text'] for s in fulltext_sections])
    text_lower = all_text.lower()
    
    # Species
    species = set()
    sp_map = {
        'Arabidopsis thaliana': 'Arabidopsis', 'Oryza sativa': 'rice', 'Triticum aestivum': 'wheat',
        'Zea mays': 'maize', 'Glycine max': 'soybean', 'Nicotiana': 'tobacco',
        'Populus': 'poplar', 'Vitis': 'grape', 'Solanum tuberosum': 'potato',
        'Solanum lycopersicum': 'tomato', 'Gossypium': 'cotton', 'Camellia': 'tea',
        'Medicago': 'alfalfa', 'Manihot': 'cassava', 'Marchantia': 'Marchantia',
    }
    for sp, label in sp_map.items():
        if sp.lower() in text_lower: species.add(label)
    cn_map = {'拟南芥':'Arabidopsis','水稻':'rice','小麦':'wheat','玉米':'maize','大豆':'soybean',
              '烟草':'tobacco','杨树':'poplar','葡萄':'grape'}
    for cn, en in cn_map.items():
        if cn in all_text[:3000]: species.add(en)
    
    # Methods
    methods = []
    m_map = {
        'scRNA-seq': ['scrna.seq','single.cell rna','10x genomics','drop.seq'],
        'snRNA-seq': ['snrna','single.nucleus','nuclei isolation'],
        'Spatial transcriptomics': ['spatial transcriptom','stereo.seq','visium','slide.seq'],
        'ATAC-seq': ['atac.seq','transposase.accessible'],
        'ChIP-seq': ['chip.seq','chromatin immunoprecipitation'],
        'CRISPR/Cas9': ['crispr','cas9','gene editing','knockout'],
        'RNA-seq': ['rna.seq','transcriptom','differential expression'],
        'Proteomics': ['proteom','mass spectrom','lc.ms'],
        'Metabolomics': ['metabolom','lc.ms','gc.ms','metabolite profil'],
        'Microscopy': ['confocal','electron microscopy','tem','sem','fluorescent','gfp'],
    }
    for m, kws in m_map.items():
        if any(kw.lower().replace('-','.').replace(' ','.') in text_lower.replace('-','.').replace(' ','.') for kw in kws):
            methods.append(m)
    
    # Core findings
    findings = []
    search_text = abstract
    if fulltext_sections:
        for s in fulltext_sections:
            if any(kw in s.get('title','').lower() for kw in ['result','discuss','conclus','finding']):
                search_text += ' ' + s['text'][:2000]
    
    garbage_patterns = [
        r'author\s*contribut', r'performed\s+.*\s+experiment', r'conceived\s+the',
        r'correspondence\s*(to|should)', r'competing\s+(financial\s+)?interest',
        r'publisher.*disclaimer', r'this\s+is\s+(a\s+PDF|an\s+open)',
        r'reprints?\s+and\s+permissions', r'rights?\s+reserved',
        r'supplementary\s+(information|data|material)', r'users?\s+may\s+view',
        r'creative\s+commons', r'\xa9\s+the\s+author', r'collection\s+date',
        r'^[A-Z][.][A-Z][.]\s',
        r'To\s+whom\s+correspondence', r'correspondence:', r'email:',
    ]
    
    sentences = re.split(r'(?<=[.。])\s+', search_text)
    for s in sentences:
        s = s.strip()
        if len(s) < 30 or len(s) > 300: continue
        sl = s.lower()
        
        if any(re.search(p, sl) for p in garbage_patterns):
            continue
        
        score = 0
        for v in ['reveal','demonstrat','show','identif','discover','uncover','elucidat',
                  'establish','confirm','validat','provid','characteriz']:
            if v in sl: score += 3
        for v in ['suggest','indicat','implicat','contribut','mediat','regulat','modulat']:
            if v in sl: score += 2
        for c in ['mechanism','pathway','signaling','cascade','network','module',
                  'transcription factor','phosphorylat','interaction','binding',
                  'biosynthesis','development','differentiation','stress','immun',
                  'tolerance','resistance','regeneration','senescence','metabolism',
                  'cell type','trajector','atlas','lineage','marker gene',
                  'single.cell','sequenc','genome']:
            if c in sl: score += 1
        
        if score >= 3:
            s_clean = re.sub(r'\s+',' ',s)[:200]
            findings.append(s_clean)
    
    curation = "\n## 深度提炼\n\n"
    if species:
        curation += f"**物种**: {', '.join(sorted(species))}\n\n"
    if methods:
        curation += f"**方法**: {', '.join(methods[:6])}\n\n"
    
    curation += "### 核心发现\n\n"
    if findings:
        for f in findings[:12]:
            curation += f"- {f}\n"
    elif abstract:
        curation += f"- {abstract[:500]}\n"
    
    curation += f"\n**全文来源**: {'PMC全文' if fulltext_sections else 'PubMed摘要'}\n"
    
    with open(path,'r',encoding='utf-8') as f:
        content = f.read()
    
    if '## 深度提炼' in content:
        content = re.sub(r'\n## 深度提炼.*$', '', content, flags=re.DOTALL)
    
    if '## 全文 (PMC)' in content:
        content = re.sub(r'\n## 全文 \(PMC\).*$', '', content, flags=re.DOTALL)
    
    if fulltext_sections:
        ft_section = "\n\n## 全文 (PMC)\n\n"
        for s in fulltext_sections[:8]:
            if s['title']:
                ft_section += f"### {s['title']}\n\n{s['text'][:1500]}\n\n"
        content += ft_section
    
    with open(path,'w',encoding='utf-8') as f:
        f.write(content + curation)
    
    return len(findings), bool(fulltext_sections)

# Main — scan both papers/ and methods/ subdirectories
concepts_dir = f'{BASE}/concepts'
papers_dir = f'{BASE}/concepts/papers'
methods_dir = f'{BASE}/concepts/methods'
ft_count = 0
ab_count = 0

for subdir in [papers_dir, methods_dir]:
    if not os.path.isdir(subdir):
        continue
    for fname in sorted(os.listdir(subdir)):
        if not fname.endswith('.md') or fname.startswith('ref'):
            continue
        slug = fname.replace('.md','')
        path = f'{subdir}/{fname}'
        
        with open(path,'r',encoding='utf-8') as f:
            content = f.read()
        
        # PROTECTION: skip files with high-quality curation
        curation_section = re.search(r'## 深度提炼\n\n(.*?)(?=\n## (?!深度)|$)', content, re.DOTALL)
        if curation_section:
            cur_text = curation_section.group(1)
            if re.search(r'\*\*期刊\*\*:', cur_text):
                continue
            has_species = re.search(r'\*\*物种\*\*:\s*\S', cur_text)
            has_method = re.search(r'\*\*方法\*\*:\s*\S', cur_text)
            findings_count = len(re.findall(r'^- .{10,}', cur_text, re.MULTILINE))
            if has_species and has_method and findings_count >= 3:
                continue
        
        # Get PMID
        pm = re.search(r'pmid:\s*(\d+)', content, re.I)
        doi_fallback = False
        if pm:
            pmid = pm.group(1)
        else:
            doi_m = re.search(r'doi:\s*(10\.[^\s\n]+)', content, re.I)
            if doi_m:
                doi = doi_m.group(1).strip()
                pmid = doi_to_pmid(doi)
                if pmid:
                    doi_fallback = True
                else:
                    continue
            else:
                continue
        
        tm = re.search(r'(?:^# |title:\s*)(.+)', content, re.M)
        title = tm.group(1).strip()[:80] if tm else slug
        
        ab = re.search(r'## 摘要\n\n(.+?)(?=\n## |\Z)', content, re.DOTALL)
        abstract = ab.group(1).strip() if ab else ''
        
        fulltext = None
        existing_ft = re.search(r'## 全文 \(PMC\)\n\n(.+?)(?=\n## (?!全文)|$)', content, re.DOTALL)
        if existing_ft:
            ft_text = existing_ft.group(1)
            sections = []
            for sec in re.split(r'\n### ', ft_text):
                sec = sec.strip()
                if not sec: continue
                if '\n' in sec:
                    title_part, body = sec.split('\n', 1)
                    sections.append({'title': title_part.strip(), 'text': body.strip()})
                else:
                    sections.append({'title': '', 'text': sec})
            fulltext = sections
            print(f"  [{slug[:30]}] {pmid} (复用已有PMC全文, {len(fulltext)} sections)")
        else:
            print(f"  [{slug[:30]}] {pmid}...", end=' ')
            pmcid = get_pmcid(pmid)
            if pmcid:
                fulltext = download_pmc_fulltext(pmcid)
                if fulltext:
                    print(f"PMC:{pmcid} OK ({len(fulltext)} sections)")
                else:
                    print(f"PMC:{pmcid} (no fulltext)")
            else:
                print("no PMC")
        
        n_findings, has_ft = deep_curate_from_fulltext(slug, path, title, abstract, fulltext)
        if has_ft:
            ft_count += 1
        else:
            ab_count += 1
        time.sleep(0.3)

print(f"\nFinished — Full text: {ft_count} | Abstract only: {ab_count}")
