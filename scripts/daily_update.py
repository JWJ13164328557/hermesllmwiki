#!/usr/bin/env python3
"""
每日植物学文献自动检索与完整导入
用法: python3 daily_update.py [--days 1] [--import]
"""

import urllib.parse, subprocess, json, xml.etree.ElementTree as ET, os, re, sys, time
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

from kb_paths import BASE, paper_path  # 统一根目录解析: KB_BASE/APP_DIR 环境变量优先
from text_utils import xml_text, yaml_str, clip_sentences
CONCEPTS_DIR = f'{BASE}/concepts/papers'  # SCHEMA: papers/
METHODS_DIR = f'{BASE}/concepts/methods'   # SCHEMA: methods/

# ══════════════════════════════════════════════════════════════
# 物种限定 — 统一来源 species_registry.py (2026-08-26 重整)
# 原 :28 种硬编码; 现:153 种(检索) 由权威注册表提供, 消除与
#     multi_source_search / daily_full_pipeline / theme_filter 的漂移.
#     PLANT_SPECIES 保留为检索 AND 子句 (主题词 AND 物种)。
# ══════════════════════════════════════════════════════════════
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from species_registry import build_search_and_clause

def _assign_themes_or_empty(title, abstract, keywords=None):
    """入库主题归属；themes 模块不可用时退化为 out-of-scope（不伪造主题）。"""
    try:
        import themes as _th
        return _th.assign_for_import(title, abstract, keywords)
    except Exception:
        return set(), 'out-of-scope', None


def _audit_out_of_scope(rows):
    """out-of-scope 入库记审计表：覆盖率分子分母都要对得上（2026-11-03）。"""
    if not rows:
        return
    path = os.path.join(BASE, '_review', 'out_of_scope_intake.tsv')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    new = not os.path.exists(path)
    with open(path, 'a', encoding='utf-8', newline='\n') as fh:
        if new:
            fh.write('date\tdoi\tpmid\ttitle\n')
        for r in rows:
            fh.write('%s\t%s\t%s\t%s\n' % (
                datetime.now().strftime('%Y-%m-%d'),
                r.get('doi', ''), r.get('pmid', ''),
                (r.get('title', '') or '').replace('\t', ' ')))
PLANT_SPECIES = build_search_and_clause()

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
    """扫描概念层全部页面（concepts/*.md 与 concepts/papers/*.md）。

    2026-11-01 修复: 原来只扫 concepts/*.md，漏掉 concepts/papers/ 下的 2717 篇
    主库页面 → 同一 DOI 被重复建页。线上实测有 60 个 DOI 同时存在于两个目录。
    """
    dois = set()
    for root, _dirs, files in os.walk(f"{BASE}/concepts"):
        for fname in files:
            if not fname.endswith('.md'):
                continue
            try:
                with open(os.path.join(root, fname), 'r', encoding='utf-8', errors='ignore') as f:
                    head = f.read(4000)
            except OSError:
                continue
            # [ \t]* 而非 \s*：空 doi 行不能吞掉换行，否则会把下一行 key 当 DOI。
            m = re.search(r'^doi:[ \t]*["\']?([^\s"\'\n]+)', head, re.I | re.M)
            if m:
                dois.add(m.group(1).strip().rstrip('.').rstrip('/'))
    return dois

def search_pubmed(query, days=1, max_results=10):
    from_date = (datetime.now() - timedelta(days=days)).strftime('%Y/%m/%d')
    full_query = f'({query}) AND ("{from_date}"[Date - Publication] : "3000"[Date - Publication])'
    # 2026-08-26 修复: 原 [:500] 会把长查询截断 → 153 物种的限定子句被静默丢弃.
    # NCBI esearch 支持长 term, quote 后完整传递; 日期子句放末尾, 即使截断也不影响核心检索.
    # 2026-09-14 修复: NCBI esearch 用 GET + 超长 term(153 物种限定, ~4700+ 编码后字符)会触发
    # HTTP 414 URI Too Long → 返回 HTML 错误页而非 JSON → json.loads 失败 → 候选 0.
    # 改为 POST, 把 term 放请求体(--data-urlencode), 避开 URL 长度限制.
    proc = subprocess.run(['curl','-sL','--connect-timeout','10',
        '--data-urlencode', f'db=pubmed',
        '--data-urlencode', f'term={full_query}',
        '--data-urlencode', f'retmax={max_results}',
        '--data-urlencode', 'sort=date',
        '--data-urlencode', 'retmode=json',
        '-X','POST',
        'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'],
        capture_output=True, text=True, timeout=25)
    try:
        data = json.loads(proc.stdout)
    except (json.JSONDecodeError, ValueError):
        print(f"  ⚠ esearch JSON 解析失败 (query len={len(full_query)})", file=sys.stderr)
        return []
    return data.get('esearchresult',{}).get('idlist',[])

def fetch_full_paper(pmid):
    """Fetch COMPLETE paper metadata from PubMed"""
    proc = subprocess.run(['curl','-sL','--connect-timeout','10',
        f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml'],
        capture_output=True, text=True, timeout=25)
    return parse_pubmed_article(proc.stdout, pmid)


def parse_pubmed_article(xml_bytes, pmid=''):
    """把 PubMed efetch XML 解析为论文元数据（纯函数，便于测试）。

    2026-11-01 修复（线上实测的根因）: 旧实现用 `el.text` 取标题/摘要，
    只会返回**第一个行内子元素之前**的文字。PubMed 用 <i>/<sup>/<sub>
    标注物种名、基因名、单位，于是标题被切成 "…Biosynthesis of Cellulase by "
    （3422 篇中 239 篇标题尾部带空格、155 篇以介词结尾），摘要被切成
    "…cellulase production using "（679 篇不足 700 字符）。
    现统一用 text_utils.xml_text()（itertext）取全部文字。
    """
    if isinstance(xml_bytes, str):
        xml_bytes = xml_bytes.encode('utf-8', 'replace')
    try:
        root = ET.fromstring(xml_bytes)
    except Exception as e:
        print(f"  ⚠ XML parse error for PMID:{pmid}: {e}", file=sys.stderr)
        return None
    art = root.find('.//PubmedArticle')
    if art is None:
        return None

    title = xml_text(art.find('.//ArticleTitle'))
    journal = xml_text(art.find('.//Journal/Title'))
    year = xml_text(art.find('.//PubDate/Year'))
    
    # Full structured abstract (itertext, keeps inline-marked species/gene names)
    abstract_parts = []
    for node in art.findall('.//AbstractText'):
        label = node.get('Label', '')
        txt = xml_text(node)
        if txt:
            abstract_parts.append(f"{label}: {txt}" if label else txt)
    abstract = '\n\n'.join(abstract_parts)
    
    # DOI and PMCID —— 只读本文的 PubmedData/ArticleIdList。
    # 2026-11-03 根因修复：旧实现用 .//ArticleId 会递归到 ReferenceList，
    # 把参考文献里的 DOI 覆盖成文章的 DOI（今日 9/69 页 DOI 与年份不符即由此而来）。
    doi = ''
    pmcid = ''
    id_list = art.find('./PubmedData/ArticleIdList')
    if id_list is not None:
        for aid in id_list.findall('./ArticleId'):
            t = aid.get('IdType', '')
            if t == 'doi':
                doi = (aid.text or '').strip()
            elif t == 'pmc':
                pmcid = (aid.text or '').strip()
    if not doi:
        for el in art.findall('./MedlineCitation/Article/ELocationID'):
            if el.get('EIdType') == 'doi':
                doi = (el.text or '').strip()
                break
    
    # Authors
    authors = art.findall('.//Author')
    author_list = []
    for a in authors[:10]:
        name = xml_text(a.find('LastName'))
        given = xml_text(a.find('ForeName'))
        author_list.append((' '.join(x for x in (given, name) if x)).strip())
    first_author = author_list[0] if author_list else ''
    
    # MeSH keywords
    meshes = art.findall('.//MeshHeading/DescriptorName')
    keywords = [t for t in (xml_text(m) for m in meshes[:10]) if t]
    
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


def _read_frontmatter(path, max_bytes=65536):
    """只读起始到第二个 '---' 的 frontmatter，不按固定字节数截断。

    2026-11-03：此前固定 read(800)，title 字段被整段参考文献污染成多行后，
    created: 被挤到 800 字符之外 → 当日计数少 1（69 vs 68）。改为按分隔符读。
    """
    buf = []
    total = 0
    try:
        with open(path, encoding='utf-8', errors='ignore') as fh:
            for line in fh:
                buf.append(line)
                total += len(line)
                if len(buf) > 1 and line.strip() in ('---', '...'):
                    break
                if total >= max_bytes:
                    break
    except OSError:
        raise
    return ''.join(buf)


def _count_pages_created_today():
    """当日 created 字段等于今天的页面数（唯一可复核的"实际新增"口径）。

    2026-11-03：此前日报只报"本次导入 imported"，而 multisource 导入的页面
    不在这个计数里，于是日报 96 / 页面 69 这类对不上无法自证。改为写报告时
    重新盘点磁盘事实，并显式给出与 imported 的差额。
    """
    day = datetime.now().strftime('%Y-%m-%d')
    n = 0
    try:
        names = os.listdir(CONCEPTS_DIR)
    except OSError:
        return 0
    for name in names:
        if not name.endswith('.md'):
            continue
        try:
            head = _read_frontmatter(os.path.join(CONCEPTS_DIR, name))
        except OSError:
            continue
        m = re.search(r'^created:\s*"?(\d{4}-\d{2}-\d{2})', head, re.M)
        if m and m.group(1) == day:
            n += 1
    return n


def main():
    # Parse args (handle both --days=1 and --days 1, --max 50)
    days = 1
    max_results = 10
    budget = 0          # 秒；0 = 不设上限（CLI 显式传入才会设限）
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
        elif arg == '--budget' and i+1 < len(sys.argv):
            budget = int(sys.argv[i+1])
        elif arg.startswith('--budget='):
            budget = int(arg.split('=')[1])

    started_at = time.time()

    def budget_left():
        return 0 if budget <= 0 else budget - (time.time() - started_at)
    
    print(f"🔍 检索最近 {days} 天植物学文献...")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    existing_dois = get_existing_dois()
    all_pmids = set()
    
    for q in SEARCH_QUERIES:
        pmids = search_pubmed(q, days=days, max_results=max_results)
        all_pmids.update(pmids)
    
    print(f"📊 PubMed 候选: {len(all_pmids)} 篇")
    
    new_papers = []
    _purity_rejects = []   # 被纯度闸门拒收的候选（写入日报，可追溯）
    _purity_suspects = []  # 导入但信号冲突，进日报待审
    _topic_rejects = []    # 不属于八个核心主题的候选
    # ── 漏斗对账 (2026-11-03) ────────────────────────────────────────────
    # 此前 4 处 continue 静默丢弃候选（无DOI/抓取失败/期刊不符/非植物），
    # 日报只剩"检索 86 → 候选 1"，无法解释 85 篇去了哪里。线上实测
    # 2026-11-03 11:17 那次正是 86→1。现在每个 PMID 必须落入且仅落入
    # 一个桶，sum(buckets) == 检索数，否则日报显式报 INCONSISTENT。
    _funnel = {'fetch_failed': 0, 'no_doi': 0, 'dup_existing': 0,
               'journal_reject': 0, 'not_plant': 0, 'theme_filter_reject': 0,
               'topic_reject': 0, 'purity_reject': 0,
               'cap_unprocessed': 0, 'budget_unprocessed': 0}
    _journal_rejects = {}  # 期刊名 -> 被拒次数（诊断白名单缺口）
    imported = 0
    imported_papers = []
    skipped_papers = []
    _oos_rows = []  # out-of-scope 入库审计（2026-11-03）
    exhausted = False
    _cap = max(100, max_results * len(SEARCH_QUERIES))
    candidate_pmids = sorted(all_pmids)[:_cap]
    _funnel['cap_unprocessed'] = len(all_pmids) - len(candidate_pmids)
    for idx, pmid in enumerate(candidate_pmids):
        # 软超时：接近预算就停止抓取，并把已有结果正常落盘 + 明确标记 PARTIAL，
        # 避免被外层 timeout 直接杀掉后"看起来什么都没发生"（线上 41/50 次如此）。
        if budget > 0 and budget_left() <= 5:
            exhausted = True
            _funnel['budget_unprocessed'] = len(candidate_pmids) - idx
            print(f"⚠ PARTIAL: 预算 {budget}s 用尽，已处理 {idx}/{len(candidate_pmids)} 篇候选", flush=True)
            break
        p = fetch_full_paper(pmid)
        if not p:
            _funnel['fetch_failed'] += 1
            continue
        if not p['doi']:
            _funnel['no_doi'] += 1
            continue

        if p['doi'] in existing_dois:
            _funnel['dup_existing'] += 1
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
            _funnel['journal_reject'] += 1
            _j = (p.get('journal') or '?').strip() or '?'
            _journal_rejects[_j] = _journal_rejects.get(_j, 0) + 1
            continue
        
        # Must be plant-related
        if not p['is_plant']:
            _funnel['not_plant'] += 1
            continue
        
        # ── 主题相关性双重重判 (2026-08-25 防污染防线): 拦截人类/动物医学/能源/社科 ──
        try:
            from theme_filter import is_relevant_plant_paper
            ok, why = is_relevant_plant_paper(p['title'], p['abstract'], p['journal'])
            if not ok:
                print(f"     ⛔ 主题过滤拒绝 (非植物): {why} | {p['title'][:45]}")
                _funnel['theme_filter_reject'] += 1
                continue
        except ImportError:
            pass

        # ── 八主题相关性闸门 (2026-11-03): 植物对象不等于八个核心主题 ──
        try:
            from topic_gate import is_core_topic
            core_ok, core_why = is_core_topic(p['title'], p['abstract'], p['journal'])
            if not core_ok:
                print(f"     ⛔ 主题相关性拒收: {core_why} | {p['title'][:45]}")
                _topic_rejects.append({'pmid': p.get('pmid'), 'title': p['title'],
                                       'journal': p.get('journal'), 'reasons': [core_why]})
                _funnel['topic_reject'] += 1
                continue
        except ImportError:
            pass

        # ── 领域纯度闸门 (2026-11-02): 判定"研究对象"而非关键词黑名单 ──
        # theme_filter 对"植物提取物治人/动物病"完全无效（植物只是药物来源）。
        # 这里按研究对象判定：nonplant 拒收；suspect 导入但记入待审清单。
        try:
            from purity_gate import classify as _purity_classify
            verdict, preasons = _purity_classify(
                p['title'], p['abstract'], p['journal'], p.get('doi'))
            if verdict == 'nonplant':
                print(f"     ⛔ 纯度闸门拒收 (研究对象非植物): {','.join(preasons[:3])} | {p['title'][:45]}")
                _purity_rejects.append({'pmid': p.get('pmid'), 'title': p['title'],
                                        'journal': p.get('journal'), 'reasons': preasons})
                _funnel['purity_reject'] += 1
                continue
            if verdict == 'suspect':
                print(f"     ⚠ 纯度待审 (信号冲突): {','.join(preasons[:3])} | {p['title'][:45]}")
                _purity_suspects.append({'pmid': p.get('pmid'), 'title': p['title'],
                                         'journal': p.get('journal'), 'reasons': preasons})
        except ImportError:
            pass
        
        new_papers.append(p)
        ab_preview = p['abstract'][:100].replace('\n',' ')
        print(f"  ✅ {p['title'][:65]}")
        print(f"     {p['journal']} ({p['year']}) | PMID:{p['pmid']} | {p['first_author']}")
        print(f"     {ab_preview}...")
    
    # ── 漏斗对账：每个检索到的 PMID 必须恰好落一个桶 ──
    _funnel_passed = len(new_papers)
    _funnel_sum = sum(_funnel.values()) + _funnel_passed
    _funnel_ok = (_funnel_sum == len(all_pmids))
    print("📐 漏斗: 检索=%d | " % len(all_pmids)
          + " ".join("%s=%d" % (k, v) for k, v in _funnel.items() if v)
          + " passed=%d | 合计=%d %s"
          % (_funnel_passed, _funnel_sum, 'OK' if _funnel_ok else 'INCONSISTENT'))
    if _journal_rejects:
        _top = sorted(_journal_rejects.items(), key=lambda kv: -kv[1])[:12]
        print("📰 期刊被拒 TOP: " + "; ".join("%s×%d" % (k[:40], v) for k, v in _top))

    print(f"\n📋 待导入: {len(new_papers)} 篇")
    
    if auto_import and new_papers:
        print("\n📥 导入完整论文...")
        imported = 0
        for p in new_papers:
            slug = f"daily-{p['pmid']}"
            # 2026-11-03：入库即写主题。此前这里只写 tags: [papers]，
            # 新论文 100% 无主题，全靠事后回填 —— 回填脚本的 _set_field
            # 又把 1189 页 frontmatter 写坏。入口一次算对，不再欠账。
            _tset, _tstat, _tbasis = _assign_themes_or_empty(
                p['title'], p['abstract'], p.get('keywords'))
            if _tstat != 'mapped':
                _oos_rows.append({'doi': p.get('doi'), 'pmid': p.get('pmid'),
                                  'title': p.get('title')})
            
            _themes_fm = '[%s]' % ', '.join(sorted(_tset)) if _tset else '[]'
            # Full concept page
            content = f"""---
title: {yaml_str(p['title'])}
created: {datetime.now().strftime('%Y-%m-%d')}
type: concept
tags: [papers]
themes: {_themes_fm}
theme_status: {_tstat}
theme_basis: {_tbasis}
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
{p['abstract']}

## 关键词
{', '.join(p['keywords']) if p['keywords'] else '—'}

## 深度提炼

**物种**: {'plant' if p['is_plant'] else '—'}
**来源**: PMID:{p['pmid']} | DOI:{p['doi']}
"""
            target = paper_path(slug)
            if os.path.exists(target):
                # 幂等保护：已有页面（可能已深度提炼）不得被摘要级模板覆盖
                print(f"     skip existing: {slug}")
                skipped_papers.append(p)
                continue
            with open(target, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Raw article
            with open(f"{BASE}/raw/articles/{slug}.md",'w',encoding='utf-8') as f:
                f.write(f"---\ningested: {datetime.now().strftime('%Y-%m-%d')}\npmid: {p['pmid']}\ndoi: {p['doi']}\ntitle: {yaml_str(p['title'])}\n---\n\n# {p['title']}\n\n{p['abstract']}")
            imported += 1
            imported_papers.append(p)
        
        _audit_out_of_scope(_oos_rows)
        print(f"✅ 导入: {imported} 篇（其中 out-of-scope {len(_oos_rows)} 篇，已入审计表）")
        print(f"SUMMARY imported={imported} candidates={len(new_papers)} "
              f"pmids={len(candidate_pmids)} partial={int(exhausted)}")
        
        # Update index
        idx_path = f'{BASE}/index.md'
        if os.path.exists(idx_path):
            with open(idx_path,'r',encoding='utf-8') as f:
                lines = f.readlines()
            for i, line in enumerate(lines):
                if '## Comparisons' in line:
                    for j, p in enumerate(imported_papers):
                        slug = f"daily-{p['pmid']}"
                        lines.insert(i+j, f"- [[{slug}]] — {clip_sentences(p['title'], 90)} ({p['journal']} {p['year']})\n")
                    break
            with open(idx_path,'w',encoding='utf-8') as f:
                f.writelines(lines)
    
    # Report —— 2026-11-03 修订：同日多次运行不再互相覆盖。
    # 旧行为每天只留最后一份 daily_report.md，上午的 69 篇在被晚间小规模重跑
    # 覆盖后从报告里"消失"，看起来像数字造假。现在：
    #   1) 每次运行落盘 _review/daily_runs/<date>_<HHMMSS>.md（不可变审计底账）
    #   2) daily_report.md 由当日全部运行合并生成（最新在前，含每次的计数）
    _buf = []
    _buf.append(f"# 每日文献更新报告\n\n{datetime.now().strftime('%Y-%m-%d')}\n\n")
    _buf.append(f"检索: {len(all_pmids)} 篇\n")
    _buf.append(f"候选（通过过滤）: {len(new_papers)} 篇\n")
    # 漏斗对账表（2026-11-03）：候选数与检索数的差额必须逐项可解释
    _buf.append("\n### 检索漏斗\n\n")
    _buf.append("| 环节 | 篇数 |\n|---|---:|\n")
    _buf.append(f"| 检索命中 | {len(all_pmids)} |\n")
    for _k, _lbl in (('cap_unprocessed', '超出单轮上限未处理'),
                     ('budget_unprocessed', '预算用尽未处理'),
                     ('fetch_failed', '抓取失败/空记录'),
                     ('no_doi', '无 DOI'),
                     ('dup_existing', '库里已存在'),
                     ('journal_reject', '期刊不在植物/农学名单'),
                     ('not_plant', '非植物判定'),
                     ('theme_filter_reject', '非植物主题过滤'),
                     ('topic_reject', '不属于八主题'),
                     ('purity_reject', '纯度闸门（研究对象非植物）')):
        if _funnel.get(_k):
            _buf.append(f"| {_lbl} | {_funnel[_k]} |\n")
    _buf.append(f"| **通过并待导入** | **{_funnel_passed}** |\n")
    _buf.append(f"| 合计 | {_funnel_sum} |\n\n")
    if not _funnel_ok:
        _buf.append(f"⚠ **漏斗对账不平**：合计 {_funnel_sum} ≠ 检索 {len(all_pmids)}，"
                    f"差额 {len(all_pmids) - _funnel_sum} 篇无归属，需排查。\n\n")
    else:
        _buf.append("漏斗对账：合计等于检索数，每一篇都有归属。\n\n")
    if _journal_rejects:
        _top = sorted(_journal_rejects.items(), key=lambda kv: -kv[1])[:12]
        _buf.append("**期刊被拒 TOP（白名单缺口诊断）**\n\n")
        for _j, _n in _top:
            _buf.append(f"- {_j} ×{_n}\n")
        _buf.append("\n")
    if auto_import:
        _buf.append(f"实际新增页面: {imported} 篇\n")
        _buf.append(f"跳过已存在页面: {len(skipped_papers)} 篇\n")
        created_today = _count_pages_created_today()
        _buf.append(f"全库当日 created 页面（含 multisource/其他通道）: {created_today} 篇\n")
        if created_today != imported:
            _buf.append(f"差额: {created_today - imported} 篇（由其他导入通道写入，"
                        f"本脚本 imported 只统计本通道）\n")
            if created_today < imported:
                _buf.append("⚠ 磁盘新增少于导入计数：可能有页面写入失败或 created 字段异常。\n")
    else:
        _buf.append("实际新增页面: 未执行（未启用 --import）\n")
    _buf.append("\n## 本次实际新增\n\n")
    if imported_papers:
        for p in imported_papers:
            _buf.append(f"- {p['title']} ({p['journal']} {p['year']}) PMID:{p['pmid']}\n")
    else:
        _buf.append("（无）\n")
    if skipped_papers:
        _buf.append("\n## 已存在而跳过（未新增）\n\n")
        for p in skipped_papers:
            _buf.append(f"- {p['title']} ({p['journal']} {p['year']}) PMID:{p['pmid']}\n")
    if _topic_rejects:
        _buf.append("\n## 八主题相关性拒收\n\n")
        for r in _topic_rejects:
            _buf.append(f"- {r['title']} ({r['journal']}) PMID:{r['pmid']} — {', '.join(r['reasons'][:2])}\n")
    if _purity_rejects:
        _buf.append("\n## 纯度闸门拒收（研究对象非植物）\n\n")
        for r in _purity_rejects:
            _buf.append(f"- {r['title']} ({r['journal']}) PMID:{r['pmid']} — {', '.join(r['reasons'][:3])}\n")
    if _purity_suspects:
        _buf.append("\n## 纯度待审（信号冲突，导入后复核）\n\n")
        _buf.append("> 这些条目的信号互相矛盾，已先行导入以便人工判断；"
                    "若其页面随后被 phase5_5/phase5_6 隔离，会从 concepts/papers 移出，"
                    "并在报告的「当日隔离与回抓」一节登记。\n\n")
        for r in _purity_suspects:
            _buf.append(f"- {r['title']} ({r['journal']}) PMID:{r['pmid']} — {', '.join(r['reasons'][:3])}\n")

    # 未启用 --import 的运行是演练/排障，不属于当日生产底账：
    # 落 _review/daily_runs_dry/，且不并入 daily_report.md。
    # （2026-11-03 实测：一次 --max 3 的排障运行把"检索 19 篇"写进了生产日报，
    #   日报当天变成 3 次运行，其中一次根本没导入任何文献。）
    _write_and_merge_report(BASE, ''.join(_buf), rehearsal=not auto_import)

    print(f"\n📄 报告: {BASE}/daily_report.md")
    print(f"PURITY rejected={len(_purity_rejects)} suspect={len(_purity_suspects)}")


def _write_and_merge_report(base, body, rehearsal=False):
    """落盘单次运行底账，并把当日所有运行合并成 daily_report.md。

    单次底账：_review/daily_runs/<date>_<HHMMSS>.md（只增不改，可审计）
    合并报告：daily_report.md（最新运行在最前，每次运行独立成节）

    rehearsal=True（未 --import 的演练运行）落 _review/daily_runs_dry/，
    不参与 daily_report.md 合并 —— 生产日报只统计真正写入文献的运行。
    """
    import glob
    runs_dir = os.path.join(base, '_review',
                            'daily_runs_dry' if rehearsal else 'daily_runs')
    os.makedirs(runs_dir, exist_ok=True)
    stamp = datetime.now().strftime('%Y-%m-%d_%H%M%S')
    run_path = os.path.join(runs_dir, stamp + '.md')
    # 同一秒内二次调用（重试/测试）不能覆盖上一次的底账。
    n = 1
    while os.path.exists(run_path):
        n += 1
        run_path = os.path.join(runs_dir, '%s_%d.md' % (stamp, n))
    with open(run_path, 'w', encoding='utf-8') as fh:
        fh.write(body)

    if rehearsal:
        print(f"🧪 演练运行（未导入），底账已存 {run_path}，不并入 daily_report.md")
        return

    today = datetime.now().strftime('%Y-%m-%d')
    runs = sorted(glob.glob(os.path.join(runs_dir, today + '_*.md')), reverse=True)
    parts = ['# 每日文献更新报告\n\n',
             '%s\n\n' % today,
             '> 本日共 %d 次运行，按时间倒序合并；每次运行单独成节，互不覆盖。\n' % len(runs)]
    for rp in runs:
        txt = open(rp, encoding='utf-8').read()
        # 去掉单次底账自带的 H1 与日期行，避免合并后出现多个一级标题
        txt = re.sub(r'^# 每日文献更新报告\s*\n\s*\n?\d{4}-\d{2}-\d{2}\s*\n', '', txt, count=1)
        hhmmss = os.path.basename(rp).split('_', 1)[1][:-3]
        parts.append('\n## 运行 %s:%s:%s\n\n' % (hhmmss[:2], hhmmss[2:4], hhmmss[4:6]))
        parts.append(txt.rstrip() + '\n')
    with open(os.path.join(base, 'daily_report.md'), 'w', encoding='utf-8') as fh:
        fh.write(''.join(parts))


if __name__ == '__main__':
    main()
