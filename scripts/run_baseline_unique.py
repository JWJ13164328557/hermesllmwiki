#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Table V1 修订: unique entities vs raw mentions (回应审稿人口径追问)
关键改进:
1. unique entities/relations per paper (去重), 不只 raw mentions
2. 明确计数边界: 报告是否含 references/methods/figure captions
   并给出"剔除参考文献段"后的版本(若解析能定位)
3. 基因/细胞类型/关系的 unique 计数
"""
import os, re, sys

sys.path.insert(0, '/mnt/g/hermes_obsidian/hermes/scripts')
BASE = '/mnt/g/hermes_obsidian/hermes'
papers_dir = f'{BASE}/concepts/papers'

from deep_curate_all import extract_findings, extract_fulltext

# PDF 映射
pdf_paths = {}
for r, d, fnames in os.walk(f'{BASE}/raw'):
    for fn in fnames:
        if fn.lower().endswith('.pdf'):
            pdf_paths[os.path.splitext(fn)[0]] = os.path.join(r, fn)

def has_pdf(doi):
    d2 = doi.replace('/', '_')
    for cn in [doi, d2, doi.rsplit('/', 1)[-1]]:
        if cn in pdf_paths:
            return pdf_paths[cn]
    return None

# 基因名模式(植物基因: 常见 大写字母+数字 混合, 或 OsXX/AtXX)
GENE_RE = re.compile(r'\b(?:Os|At|Sl|Zm|Ta|Hv|Mt|Gm|Pt|Cs|Md|Gh|Nt|Br|St|Sb|Gh|Vv|Csi|Ca|Sp|Sly)?[A-Z][A-Za-z0-9]*\d+[A-Za-z0-9]*\b')
# 细胞类型词表
CELL_TERMS = ['cortex','endodermis','xylem','phloem','epidermis','meristem','guard cell','trichome',
              'parenchyma','companion cell','procambium','quiescent','columella','cap cell','pericycle',
              'stele','syncytium','root hair','hypodermis','mesophyll','bundle sheath','companion',
              'phloem pole','lateral root','primary root','shoot apical','root apical','columella',
              'cambium','fibroblast-like','subsidiary cell']
# 组织词
TISSUE_TERMS = ['root','shoot','leaf','stem','flower','seed','fruit','embryo','cotyledon','petal','pollen','anther']
# 关系动词
REL_PAT = re.compile(r'(regulat|control|activates|inhibits|suppresses|promotes|binds? to|interacts with|phosphorylat|ubiquitinat|acetyl?at|methylat)', re.I)

def strip_references(text):
    """尝试剔除参考文献区段(启发式: 从 'References'/'References:' 起截断)"""
    m = re.search(r'\n\s*(References|Bibliography|REFERENCES)\s*\n', text)
    if m:
        return text[:m.start()]
    return text

def analyse(text):
    """返回 unique 和 raw 计数 (全文本体; 说明是否含参考文献)"""
    body = text
    body_no_ref = strip_references(text)
    tl = body.lower()
    tl_nr = body_no_ref.lower()
    genes = set(GENE_RE.findall(body))
    genes_nr = set(GENE_RE.findall(body_no_ref))
    cells = {t for t in CELL_TERMS if t in tl}
    cells_nr = {t for t in CELL_TERMS if t in tl_nr}
    tissues = {t for t in TISSUE_TERMS if t in tl}
    rels = set(REL_PAT.findall(body))
    rels_nr = set(REL_PAT.findall(body_no_ref))
    marker_ment = len(re.findall(r'\bmarker\b', tl))
    marker_nr = len(re.findall(r'\bmarker\b', tl_nr))
    return {
        'raw_len': len(body), 'no_ref_len': len(body_no_ref),
        'uniq_genes': len(genes), 'uniq_genes_nr': len(genes_nr),
        'uniq_cells': len(cells), 'uniq_cells_nr': len(cells_nr),
        'uniq_tissues': len(tissues),
        'uniq_rels': len(rels), 'uniq_rels_nr': len(rels_nr),
        'marker_raw': marker_ment, 'marker_nr': marker_nr,
    }

samples = []
for fn in os.listdir(papers_dir):
    if not fn.endswith('.md') or len(samples) >= 60:
        continue
    c = open(os.path.join(papers_dir, fn), encoding='utf-8', errors='ignore').read()
    dm = re.search(r'doi:\s*(10\.[^\s\]"#]+)', c)
    if not dm: continue
    doi = dm.group(1).strip().rstrip('.')
    pdf = has_pdf(doi)
    if not pdf: continue
    m = re.search(r'## 摘要\s*\n(.*?)(\n## |\Z)', c, re.S)
    abstract = m.group(1).strip() if m else ''
    if len(abstract) < 200: continue
    try:
        ft = extract_fulltext(pdf)
    except Exception:
        ft = ''
    if not ft or len(ft) < 1500: continue
    samples.append({'abstract': abstract, 'fulltext': ft})

n = len(samples)
print(f'样本: n={n}')
# 累加器
def agg():
    return {'uniq_genes':0,'uniq_genes_nr':0,'uniq_cells':0,'uniq_cells_nr':0,'uniq_tissues':0,
            'uniq_rels':0,'uniq_rels_nr':0,'marker_raw':0,'marker_nr':0}
abs_a, ft_a = agg(), agg()
for s in samples:
    a, f = analyse(s['abstract']), analyse(s['fulltext'])
    for k in abs_a: 
        abs_a[k]+=a[k]; ft_a[k]+=f[k]

print(f'\n===== Table V1 修订: unique entities per paper (n={n}) =====')
print(f"{'指标(每篇)':<28}{'摘要':<9}{'全文':<9}{'倍率'}")
def show(label, k, is_pct=False):
    av, fv = abs_a[k]/n, ft_a[k]/n
    r = fv/av if av>0 else float('inf')
    print(f'{label:<26}{av:<9.2f}{fv:<9.2f}{r:<6.1f}x')
show('Unique genes (全文含引用)', 'uniq_genes')
show('Unique genes (剔除参考文献)', 'uniq_genes_nr')
show('Unique cell types', 'uniq_cells')
show('Unique cell types (剔Refs)', 'uniq_cells_nr')
show('Unique tissues', 'uniq_tissues')
show('Unique relations (含Refs)', 'uniq_rels')
show('Unique relations (剔Refs)', 'uniq_rels_nr')
show('Marker mentions raw', 'marker_raw')
show('Marker mentions (剔Refs)', 'marker_nr')
# 参考文献占比
print(f'\n全文平均长度(字符): {round(ft_a["raw_len"]/n)}  剔除引用后: {round(ft_a["no_ref_len"]/n)}')
print(f'参考文献区约占全文比例: {(ft_a["raw_len"]-ft_a["no_ref_len"])/ft_a["raw_len"]*100:.0f}%')
