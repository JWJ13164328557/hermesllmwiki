#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""abstract vs full-text baseline 对比: 用真实PDF+概念页跑提取统计"""
import os, re, sys, glob

sys.path.insert(0, '/mnt/g/hermes_obsidian/hermes/scripts')
BASE = '/mnt/g/hermes_obsidian/hermes'
papers_dir = f'{BASE}/concepts/papers'

from deep_curate_all import extract_findings, extract_fulltext

# ---- 概念页DOI -> PDF 映射 ----
pdf_paths = {}
for r, d, fnames in os.walk(f'{BASE}/raw'):
    for fn in fnames:
        if fn.lower().endswith('.pdf'):
            pdf_paths[os.path.splitext(fn)[0]] = os.path.join(r, fn)

def norm_doi(d):
    return d.replace('/', '_')

def has_pdf(doi):
    for cn in [doi, norm_doi(doi), doi.rsplit('/', 1)[-1]]:
        if cn in pdf_paths:
            return pdf_paths[cn]
    return None

# ---- 收集样本: 概念页 有摘要 + 有PDF + 可提取全文 ----
samples = []
for fn in os.listdir(papers_dir):
    if not fn.endswith('.md') or len(samples) >= 60:
        continue
    fp = os.path.join(papers_dir, fn)
    c = open(fp, encoding='utf-8', errors='ignore').read()
    dm = re.search(r'doi:\s*(10\.[^\s\]"#]+)', c)
    if not dm:
        continue
    doi = dm.group(1).strip().rstrip('.')
    pdf = has_pdf(doi)
    if not pdf:
        continue
    # 摘要在概念页 '## 摘要' 后
    m = re.search(r'## 摘要\s*\n(.*?)(\n## |\Z)', c, re.S)
    abstract = m.group(1).strip() if m else ''
    if len(abstract) < 200:  # 需要够长的摘要
        continue
    # 全文
    try:
        ft = extract_fulltext(pdf)
    except Exception:
        ft = ''
    if not ft or len(ft) < 1500:
        continue
    samples.append({'fn': fn, 'doi': doi, 'abstract': abstract, 'fulltext': ft})

print(f'有效样本(有摘要+有全文): {len(samples)}')

# ---- 统计函数: 在给定文本中计数各信息类型 ----
def count_entities(text):
    tl = text.lower()
    res = {}
    # 物种 (关键词)
    spec_terms = ['arabidops', 'oryza', 'rice', 'maiz', 'zea mays', 'tomato', 'solanum',
                  'wheat', 'triticum', 'barley', 'hordeum', 'soybean', 'glycine',
                  'poplar', 'populus', 'medicago', 'cotton', 'gossypium', 'pea', 'pisum']
    res['species_mentions'] = sum(1 for t in spec_terms if t in tl)
    # 细胞类型/组织 (常见植物细胞类型词)
    cell_terms = ['root', 'shoot', 'leaf', 'cortex', 'endodermis', 'xylem', 'phloem',
                  'epidermis', 'meristem', 'guard cell', 'trichome', 'parenchyma',
                  'companion cell', 'procambium', 'quiescent', 'columella', 'cap cell']
    res['celltype_mentions'] = sum(1 for t in cell_terms if t in tl)
    # marker 明示
    res['marker_mentions'] = len(re.findall(r'marker', tl))
    # 关系 / 调控动词
    reg_pat = re.compile(r'(regulat|control|activates|inhibits|suppresses|promotes|binds? to|interacts with|phosphorylat)')
    res['regulation_mentions'] = len(reg_pat.findall(tl))
    # 物种学名计数(拉丁二名法)
    binom_pat = re.compile(r'[A-Z][a-z]+ [a-z]+')
    res['latin_binomials'] = len(binom_pat.findall(text))
    return res

# ---- findings 提取(信号句) ----
# 汇总
agg_abs = {'species_mentions':0,'celltype_mentions':0,'marker_mentions':0,'regulation_mentions':0,'latin_binomials':0}
agg_ft  = dict(agg_abs)
abs_finding_count = 0
ft_finding_count = 0
with_findings_abs = 0
with_findings_ft = 0

for s in samples:
    a = count_entities(s['abstract'])
    f = count_entities(s['fulltext'])
    for k in agg_abs:
        agg_abs[k] += a[k]
        agg_ft[k] += f[k]
    # findings
    nf_abs = len(extract_findings(s['abstract']))
    nf_ft  = len(extract_findings(s['fulltext']))
    abs_finding_count += nf_abs
    ft_finding_count += nf_ft
    if nf_abs > 0: with_findings_abs += 1
    if nf_ft > 0:  with_findings_ft += 1

n = len(samples)
print(f'\n===== abstract vs full-text baseline (n={n} 篇, 同批论文) =====')
print(f"{'指标(每篇均值)':<24}{'摘要':<10}{'全文':<10}{'倍率':<6}")
per_abs = {k: v/n for k,v in agg_abs.items()}
per_ft  = {k: v/n for k,v in agg_ft.items()}
labels = {'species_mentions':'物种提及','celltype_mentions':'细胞类型/组织提及',
          'marker_mentions':'marker提及','regulation_mentions':'调控/关系动词','latin_binomials':'拉丁学名二名法'}
for k,lab in labels.items():
    ratio = per_ft[k]/per_abs[k] if per_abs[k] > 0 else float('inf')
    print(f'{lab:<22}{per_abs[k]:<10.2f}{per_ft[k]:<10.2f}{ratio:<6.1f}x')
label_kf = '关键finding信号句(均值)'
abs_avg = abs_finding_count / n
ft_avg = ft_finding_count / n
kf_ratio = ft_finding_count / abs_finding_count if abs_finding_count > 0 else float('inf')
print('{:<22}{:<10.2f}{:<10.2f}{:<6.1f}x'.format(label_kf, abs_avg, ft_avg, kf_ratio))
print(f'含≥1 finding的论文占比:  摘要 {100*with_findings_abs/n:.0f}%  全文 {100*with_findings_ft/n:.0f}%')

print(f'\n输出: 样本 {n}', file=open('/tmp/baseline_result.txt','w'))
