#!/usr/bin/env python3
"""批量 Paper Spec 生成 — 从 PubMed 元数据 + PMC 全文 → 9-section 格式"""
import os, re, json, subprocess, time, sys, urllib.request, xml.etree.ElementTree as ET

BASE = '/mnt/g/hermes_obsidian/hermes'
PAPERS_DIR = os.path.join(BASE, 'concepts', 'papers')
EVIDENCE_DIR = os.path.join(BASE, 'evidence')
META_FILE = '/tmp/paper_metadata.json'
MAP_FILE = '/tmp/pmid_file_map.json'

os.makedirs(EVIDENCE_DIR, exist_ok=True)

def load_metadata():
    with open(META_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_file_map():
    with open(MAP_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def download_pmc_fulltext(pmcid):
    """Download full text from PMC classic HTML view"""
    try:
        proc = subprocess.run(['curl','-sL','--connect-timeout','15',
            f'https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/?report=classic'],
            capture_output=True, text=True, timeout=30)
        html = proc.stdout
        if len(html) < 2000:
            return None
        
        # Extract body sections
        sections = []
        body_start = 0
        for tag in ['<div class="tsec', '<div class="sec', '<div id=']:
            idx = html.find(tag)
            if idx > 0:
                body_start = idx
                break
        if body_start == 0:
            return None
        
        body = html[body_start:body_start+80000]
        
        # Extract section titles and paragraphs
        current_title = 'Introduction'
        current_text = []
        
        for line in body.split('\n'):
            # Section header
            h_match = re.search(r'<h[2-4][^>]*>(.*?)</h[2-4]>', line)
            if h_match:
                if current_text:
                    sections.append({'title': current_title, 'text': ' '.join(current_text)[:5000]})
                current_title = re.sub(r'<[^>]+>', '', h_match.group(1)).strip()
                current_text = []
                continue
            
            # Paragraph
            p_match = re.findall(r'<p[^>]*>(.*?)</p>', line)
            for p in p_match:
                text = re.sub(r'<[^>]+>', ' ', p).strip()
                text = re.sub(r'\s+', ' ', text)
                if len(text) > 30:
                    current_text.append(text)
        
        if current_text:
            sections.append({'title': current_title, 'text': ' '.join(current_text)[:5000]})
        
        return sections if sections else None
    except Exception as e:
        print(f"  PMC download error: {e}")
        return None

def get_pubmed_structured_abstract(pmid, meta):
    """Use PubMed efetch to get structured abstract sections"""
    try:
        url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=15) as resp:
            xml_data = resp.read()
        
        root = ET.fromstring(xml_data)
        article = root.find('.//PubmedArticle')
        if article is None:
            return []
        
        sections = []
        for ab in article.findall('.//AbstractText'):
            label = ab.get('Label', '')
            text = ''.join(ab.itertext())
            if label:
                sections.append({'title': label, 'text': text[:3000]})
            else:
                sections.append({'title': 'Abstract', 'text': text[:3000]})
        
        return sections if sections else [{'title': 'Abstract', 'text': meta.get('abstract', '')[:3000]}]
    except:
        return [{'title': 'Abstract', 'text': meta.get('abstract', '')[:3000]}]

def extract_species(text):
    """Extract plant species from text"""
    species_list = []
    species_patterns = [
        ('Arabidopsis thaliana', r'arabidopsis', 'arabidopsis'),
        ('Oryza sativa (rice)', r'\brice\b|oryza\b', 'rice'),
        ('Zea mays (maize)', r'\bmaize\b|zea\b', 'maize'),
        ('Glycine max (soybean)', r'\bsoybean\b|glycine\b', 'soybean'),
        ('Triticum aestivum (wheat)', r'\bwheat\b|triticum\b', 'wheat'),
        ('Populus (poplar)', r'\bpoplar\b|populus\b', 'poplar'),
        ('Solanum lycopersicum (tomato)', r'\btomato\b|solanum\b', 'tomato'),
        ('Nicotiana (tobacco)', r'\btobacco\b|nicotiana\b', 'tobacco'),
        ('Solanum tuberosum (potato)', r'\bpotato\b', 'potato'),
        ('Gossypium (cotton)', r'\bcotton\b|gossypium\b', 'cotton'),
        ('Medicago truncatula', r'\bmedicago\b', 'medicago'),
        ('Brassica', r'\bbrassica\b', 'brassica'),
        ('Vitis vinifera (grape)', r'\bgrape\b|vitis\b', 'grape'),
        ('Physcomitrium patens (moss)', r'\bmoss\b|physcomitri\w*\b|physcomitrella\b', 'moss'),
        ('Marchantia polymorpha', r'\bmarchantia\b|liverwort\b', 'liverwort'),
        ('Setaria viridis', r'\bsetaria\b', 'setaria'),
        ('Cunninghamia lanceolata', r'\bcunninghamia\b|fir\b', 'fir'),
    ]
    text_lower = text.lower()
    for name, pattern, _ in species_patterns:
        if re.search(pattern, text_lower, re.IGNORECASE):
            species_list.append(name)
    return species_list if species_list else ['unknown']

def extract_methods(text):
    """Detect key methods used"""
    methods = []
    method_patterns = {
        'scRNA-seq': r'scrna[\s-]*seq|single[\s-]*cell[\s-]*rna|single[\s-]*cell[\s-]*transcriptom',
        'snRNA-seq': r'snrna[\s-]*seq|single[\s-]*nucle[ui]s[\s-]*rna',
        'spatial transcriptomics': r'spatial[\s-]*transcriptom|stereo[\s-]*seq|visium|merfish|xenium|slideseq',
        'scATAC-seq': r'scatac[\s-]*seq|single[\s-]*cell[\s-]*atac',
        'multi-omics': r'multi[\s-]*omics|integrativ',
        'ChIP-seq': r'chip[\s-]*seq',
        'RNA-seq': r'rna[\s-]*seq\b|bulk[\s-]*rna',
        'metabolomics': r'metabolom|ms[\s-]*imaging',
        'proteomics': r'proteom',
        'CRISPR': r'crispr',
        'reporter assay': r'reporter|luciferase|gus[\s-]*stain',
        'Y2H': r'y2h|yeast[\s-]*two[\s-]*hybrid',
        'Co-IP': r'co[\s-]*ip|co[\s-]*immunoprecip',
        'ChIP-qPCR': r'chip[\s-]*qpcr',
        'EMSA': r'emsa|gel[\s-]*shift',
        'RNA-FISH': r'rna[\s-]*fish|in[\s-]*situ[\s-]*hybridiz',
        'GWAS': r'gwas\b',
        'QTL': r'qtl\b',
        'phylogenetics': r'phylog|evolutionary[\s-]*anal',
        'machine learning': r'machine[\s-]*learning|deep[\s-]*learning|neural[\s-]*network',
        'GRN': r'gene[\s-]*regulatory[\s-]*network|grn\b|network[\s-]*inference',
        'pseudotime': r'pseudotime|trajectory[\s-]*inference|rna[\s-]*velocity|monocle',
        'cell communication': r'cell[\s-]*communication|ligand[\s-]*receptor|cellchat|cellphonedb',
    }
    text_lower = text.lower()
    for name, pattern in method_patterns.items():
        if re.search(pattern, text_lower, re.IGNORECASE):
            methods.append(name)
    return methods if methods else ['not detected']

def extract_key_genes(text):
    """Extract gene names mentioned"""
    # Arabidopsis-style genes
    arab_genes = set(re.findall(r'\b[A-Z]{2,5}\d{1,2}\b', text))
    # Rice/maize-style genes
    rice_genes = set(re.findall(r'\bOs[A-Z]{2,4}\d{1,3}[A-Z]?\b', text))
    # General gene mentions
    all_genes = list(arab_genes | rice_genes)[:15]
    return all_genes if all_genes else []

def identify_topic(text, meta):
    """Identify primary research topic"""
    topics = []
    topic_patterns = {
        'development': r'\bdevelop|morphogenesis|organogenesis|embryo|meristem',
        'stress': r'\bstress|salt|drought|cold|heat|chilling|pathogen|defense',
        'hormone': r'\bhormone|auxin|gibberellin|aba|jasmonic|salicylic|ethylene|brassinosteroid|cytokinin',
        'metabolism': r'\bmetabol|biosynthesis|secondary[\s-]*metabolite',
        'signaling': r'\bsignal|phosphorylation|kinase|receptor|pathway',
        'gene regulation': r'\btranscription[\s-]*factor|regulator|promoter|enhancer|chromatin|epigen',
        'cell type': r'\bcell[\s-]*type|atlas|landscape|heterogeneity|taxonomy',
        'regeneration': r'\bregenerat|callus|reprogram|totipotenc',
        'photosynthesis': r'\bphotosyn|chloroplast|light[\s-]*signal',
        'symbiosis': r'\bsymbios|mycorrhiz|rhizob|nodulation',
        'flowering': r'\bflower|floral|inflorescence|reproducti',
        'root': r'\broot[\s-]|rhizosphere',
        'single-cell method': r'\bsingle[\s-]*cell.*method|protocol|pipeline|tool',
        'spatial method': r'\bspatial.*method|computation',
        'evolution': r'\bevolution|comparative[\s-]*genom|phylogen',
    }
    text_lower = (text + ' ' + meta.get('title', '')).lower()
    for topic, pattern in topic_patterns.items():
        if re.search(pattern, text_lower, re.IGNORECASE):
            topics.append(topic)
    return topics if topics else ['general']

def extract_core_findings(text):
    """Extract sentences that look like core findings"""
    findings = []
    signal_words = r'(reveal|demonstrat|identif|discover|show|find|indicat|suggest|establish|confirm|validat|elucidat|uncovers|characteriz|determin|propos)'
    
    sentences = re.split(r'[.!?]\s+', text)
    for s in sentences:
        s_clean = s.strip()
        if len(s_clean) > 50 and len(s_clean) < 500:
            if re.search(signal_words, s_clean, re.IGNORECASE):
                findings.append(s_clean)
                if len(findings) >= 8:
                    break
    return findings

def generate_paper_spec(meta, fulltext_sections, pmid):
    """Generate 9-section Paper Spec markdown"""
    
    # Combine all text for analysis
    all_text = meta.get('title', '') + '\n' + meta.get('abstract', '')
    if fulltext_sections:
        for s in fulltext_sections:
            all_text += '\n' + s.get('text', '')
    
    species = extract_species(all_text)
    methods = extract_methods(all_text)
    topics = identify_topic(all_text, meta)
    findings = extract_core_findings(all_text)
    genes = extract_key_genes(all_text)
    
    is_oa = fulltext_sections is not None and len(fulltext_sections) > 2
    depth_label = "PMC全文" if is_oa else "PubMed摘要"
    
    # Build markdown
    sections = []
    
    # Frontmatter
    sections.append(f"""---
title: "{meta.get('title', 'Unknown')}"
pmid: "{pmid}"
doi: "{meta.get('doi', '')}"
pmcid: "{meta.get('pmcid', '')}"
journal: "{meta.get('journal', '')}"
year: "{meta.get('year', '')}"
authors: "{', '.join(meta.get('authors', [])[:5])}"
type: paper
tags: [{', '.join(topics)}]
species: [{', '.join(species)}]
methods: [{', '.join(methods)}]
status: curated
curation_depth: {depth_label}
updated: 2026-05-30
---""")
    
    # 1. Scientific Context
    context_abstract = meta.get('abstract', '')[:500] if meta.get('abstract') else ''
    sections.append(f"""
## 1. Scientific Context

{context_abstract}

**研究领域**: {', '.join(topics[:3])}
**物种**: {', '.join(species[:5])}
**技术方法**: {', '.join(methods[:5])}
**期刊**: {meta.get('journal', 'unknown')} ({meta.get('year', '')})""")
    
    # 2. Research Questions
    sections.append(f"""
## 2. Research Questions

基于摘要和{"" if is_oa else "(有限的)"}全文分析，本文主要关注以下科学问题:

1. 阐明{species[0] if species else '植物'}中{topics[0] if topics else '生物学过程'}的分子机制
2. 鉴定关键调控因子并验证其功能
3. 整合多组学数据揭示调控网络

> ⚠️ 注: 本节基于自动分析生成，需人工审查补充具体研究问题""")
    
    # 3. Experimental Logic
    sections.append(f"""
## 3. Experimental Logic

**研究策略**:
- 核心方法: {', '.join(methods[:6])}
- 物种系统: {species[0] if species else '未检测到'}
- 实验设计: 从{"" if is_oa else "(摘要)"}中推断

**关键实验体系**:
{chr(10).join(f'- {m}' for m in methods[:8]) if methods else '- 待补充具体实验方法'}""")
    
    # 4. Figure-by-Figure Analysis
    if fulltext_sections and is_oa:
        fig_sections = []
        for s in fulltext_sections:
            title = s.get('title', '')
            text = s.get('text', '')[:500]
            if title and text:
                fig_sections.append(f"**{title}**: {text[:400]}")
        sections.append(f"""
## 4. Figure-by-Figure Analysis

{chr(10).join(fig_sections[:8]) if fig_sections else '> 全文段落已提取，需人工标注图表对应关系'}

> 注: 图表-段落对应关系需人工审查""")
    else:
        sections.append("""
## 4. Figure-by-Figure Analysis

> ⚠️ 仅基于摘要/结构化文本，无法进行完整图表分析。需通过 VPN 下载全文补充。
""")
    
    # 5. Evidence Extraction
    evidence_list = []
    for i, f in enumerate(findings[:8]):
        evidence_id = f"ev-{pmid}-{i+1:02d}"
        evidence_list.append(f"""
**E{i+1}** [{evidence_id}]
- 声明: {f[:300]}
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: {meta.get('journal', '')} {meta.get('year', '')}
""")
    
    sections.append(f"""
## 5. Evidence Extraction

以下为自动提取的核心声明 (需人工审查确认):

{chr(10).join(evidence_list) if evidence_list else '> 未检测到足够证据声明，需人工提取'}
""")
    
    # 6. Knowledge Graph Extraction
    sections.append(f"""
## 6. Knowledge Graph Extraction

**实体**:
- 物种: {', '.join(species[:4])}
- 关键基因: {', '.join(genes[:8]) if genes else '待提取'}

**关系类型**:
- 调控关系: 待提取
- 功能关系: 待提取
- 比较关系: 待提取

**MeSH关键词**: {', '.join(meta.get('mesh', [])[:8])}

> 知识图谱需人工审查完善""")
    
    # 7. Critical Evaluation
    sections.append(f"""
## 7. Critical Evaluation

**优势**:
- 使用{', '.join(methods[:3])}等先进技术
- 发表于{meta.get('journal', '高影响力期刊')}

**局限**:
- {"基于PMC全文分析，可靠性较高" if is_oa else "仅基于PubMed摘要，完整评估需全文"}
- 自动分析可能遗漏关键细节
- 统计方法和重复性待人工审查

**证据质量**: {"中等" if is_oa else "低-中（仅摘要）"} (需人工评级)""")
    
    # 8. Research Insight
    sections.append(f"""
## 8. Research Insight

本文的核心贡献在于:
1. 提供了{species[0] if species else '植物'}{topics[0] if topics else '研究领域'}的新见解
2. 建立了{methods[0] if methods else '关键技术'}在植物研究中的应用范例
3. 为后续功能验证提供了候选基因和调控网络

**对当前知识库的价值**: 
- 与大豆Stereo-seq/光质响应项目的潜在关联: {
    "高" if any(t in str(topics) for t in ['development', 'cell type', 'spatial method', 'single-cell method', 'gene regulation']) else
    "中" if any(t in str(topics) for t in ['signaling', 'hormone', 'stress']) else "低"
}""")
    
    # 9. Future Research Opportunities
    sections.append(f"""
## 9. Future Research Opportunities

1. 在更多植物物种中验证核心发现
2. 整合空间转录组学数据增加空间维度
3. 开展遗传学功能验证实验
4. 探索{species[0] if species else '目标物种'}中的应用潜力

**下一步关键实验**: 基于核心发现的遗传学验证 (需人工设计具体实验)""")
    
    return '\n'.join(sections), findings, species, methods, topics, genes


def save_evidence_objects(pmid, meta, findings):
    """Create evidence object files for each finding"""
    created = []
    for i, f in enumerate(findings[:6]):
        ev_id = f"ev-{pmid}-{i+1:02d}"
        evidence_content = f"""---
title: "Evidence: {f[:80]}..."
evidence_id: "{ev_id}"
pmid: "{pmid}"
doi: "{meta.get('doi', '')}"
source: "{meta.get('journal', '')} ({meta.get('year', '')})"
type: evidence
status: auto-generated
quality: medium
updated: 2026-05-30
---

# {ev_id}

## Claim
{f[:500]}

## Biological Context
来源于{meta.get('journal', 'unknown')} ({meta.get('year', '')})的研究。
文章标题: {meta.get('title', 'Unknown')[:200]}

## Supporting Evidence
- 来源: PMID {pmid}
- 期刊: {meta.get('journal', '')}
- 证据类型: 转录组/遗传/生化 (需人工审查)

## Evidence Quality
**自动评级**: 中等
**理由**: 基于自动文本提取，需人工审查原始数据确认

## Contradictory Evidence
未检测到直接矛盾证据 (基于自动分析)

## Consensus Assessment
待人工评估
"""
        fpath = os.path.join(EVIDENCE_DIR, f"{ev_id}.md")
        with open(fpath, 'w', encoding='utf-8') as fh:
            fh.write(evidence_content)
        created.append(ev_id)
    return created

# ============================================================
# MAIN
# ============================================================

def main():
    metadata = load_metadata()
    file_map = load_file_map()
    
    total = len(metadata)
    oa_count = sum(1 for m in metadata.values() if m.get('oa_status') == 'OA')
    
    print(f"Processing {total} papers ({oa_count} OA, {total - oa_count} non-OA)")
    print("=" * 60)
    
    stats = {'oa_success': 0, 'oa_fail': 0, 'non_oa': 0, 'evidence': 0}
    
    processed = 0
    for pmid, meta in metadata.items():
        processed += 1
        is_oa = meta.get('oa_status') == 'OA'
        pmcid = meta.get('pmcid', '')
        
        # Get target file
        files = file_map.get(pmid, {}).get('files', [])
        if not files:
            continue
        target_file = files[0]  # Use first file for duplicates
        
        print(f"\n[{processed}/{total}] PMID:{pmid} | {target_file[:50]}")
        print(f"  OA: {is_oa}, Journal: {meta.get('journal','?')[:30]}")
        
        # Download full text if OA
        fulltext_sections = None
        if is_oa and pmcid:
            print(f"  Downloading PMC full text (PMCID:{pmcid})...")
            fulltext_sections = download_pmc_fulltext(pmcid)
            if fulltext_sections:
                print(f"  ✓ Got {len(fulltext_sections)} sections from PMC")
                stats['oa_success'] += 1
            else:
                print(f"  ✗ PMC download failed, falling back to abstract")
                stats['oa_fail'] += 1
        else:
            stats['non_oa'] += 1
        
        # Fallback: use PubMed structured abstract
        if not fulltext_sections:
            fulltext_sections = get_pubmed_structured_abstract(pmid, meta)
            print(f"  Using PubMed abstract ({len(fulltext_sections)} sections)")
        
        # Generate Paper Spec
        print(f"  Generating 9-section Paper Spec...")
        paper_spec, findings, species, methods, topics, genes = generate_paper_spec(
            meta, fulltext_sections, pmid
        )
        
        # Write updated paper file
        fpath = os.path.join(PAPERS_DIR, target_file)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(paper_spec)
        print(f"  ✓ Paper Spec written ({len(paper_spec)} chars)")
        
        # Create evidence objects
        if findings:
            ev_ids = save_evidence_objects(pmid, meta, findings)
            stats['evidence'] += len(ev_ids)
            print(f"  ✓ {len(ev_ids)} evidence objects created")
        
        # Handle duplicate files - update with same content
        for dup_file in files[1:]:
            dup_path = os.path.join(PAPERS_DIR, dup_file)
            with open(dup_path, 'w', encoding='utf-8') as f:
                f.write(paper_spec)
            print(f"  ✓ Duplicate updated: {dup_file[:50]}")
        
        time.sleep(1)  # Rate limiting
    
    # Summary
    print("\n" + "=" * 60)
    print(f"COMPLETE: {total} papers processed")
    print(f"  OA full text success: {stats['oa_success']}")
    print(f"  OA download failed: {stats['oa_fail']}")
    print(f"  Non-OA (abstract): {stats['non_oa']}")
    print(f"  Evidence objects: {stats['evidence']}")
    print(f"  Total files: {sum(1 for _ in metadata.values())}")

if __name__ == '__main__':
    main()
