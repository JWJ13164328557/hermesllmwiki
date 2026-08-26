#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
journal_focus_search.py — 白名单期刊 × 主题 双重限定检索 (2026-08-26)
=========================================================================
解决检索架构问题: 现有每日更新是"主题词全网搜索 + 事后期刊过滤", 期刊白名单只做
放行门槛不做检索范围来源。本脚本提供**第二通道**:

    白名单期刊 [Journal] ∩ 主题词 → 检索

即在 PubMed 用期刊名做 [Journal] 字段限定 + 主题关键词 AND, 只抓植物/农学
白名单期刊中与主题相关的文献, 天然排除医学/能源/社科污染。

用法(独立):
    /usr/bin/python3 scripts/journal_focus_search.py --days 365 --max 10 [--core-only] [--dry-run]

接入 daily_full_pipeline.py Phase 3 后, 与现有全网主题检索结果合并去重。

设计(2026-08-26 用户要求):
- 期刊: 100 本核心刊(分子植物/组学/遗传育种/胁迫/农作物/园艺), 既做 [Journal] 检索范围
  也作为该通道的来源白名单。默认 --core-only 用这 100 本; 不传则用 JCR 全部 502 本子集。
- 主题: 14 组(原 10 组 + 新增 分子机理 / 遗传育种 / 基因组 / 胁迫), 胁迫主题已含 stress。
- 每本刊 × 主题 → 一个 esearch。100刊×14主题=1400 次(限速 ~0.25s → ~6min)。
"""
import urllib.parse, urllib.request, json, sys, os, time
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    from jcr_whitelist import JOURNAL_JCR_PLANT
except Exception:
    JOURNAL_JCR_PLANT = []

# ══════════════════════════════════════════════════════════════
# 100 本核心植物/农学期刊 (双通道的期刊范围来源)
# 覆盖: 分子细胞生物学/单细胞空间组学/基因组/遗传育种/胁迫/农作物/园艺/方法
# ══════════════════════════════════════════════════════════════
CORE_JOURNALS = [
    # ── 分子/细胞植物学 + 组学 (核心)
    'Molecular Plant','Nature Plants','Plant Communications','The Plant Cell','Plant Biotechnology Journal',
    'Journal of Integrative Plant Biology','New Phytologist','Plant Physiology','Trends in Plant Science',
    'Annual Review of Plant Biology','Horticulture Research','The Plant Journal','Plant, Cell & Environment',
    'Journal of Experimental Botany','Genome Biology','Plant Methods','Plant Phenomics','Plant Science',
    'Frontiers in Plant Science','BMC Plant Biology','Molecular Plant Pathology','Theoretical and Applied Genetics',
    'Plant Cell Reports','Plant Cell and Environment','Plant Physiology and Biochemistry','Journal of Advanced Research',
    'Stress Biology','BMC Genomics','Plant Biotechnology','Plant Molecular Biology',
    'Critical Reviews in Plant Sciences','Environmental and Experimental Botany','Tree Physiology',
    'Journal of Plant Physiology','Functional Plant Biology','Plant Cell, Tissue and Organ Culture','Plant Biology',
    'Plant and Soil','AoB Plants','Plant Reproduction','Physiologia Plantarum','Plant Diversity',
    'Plant Signaling & Behavior','Plant Direct','Molecular Plant-Microbe Interactions','Plant Pathology','Phytopathology',
    'Frontiers in Microbiology','Annals of Botany','Planta','New Forests','Industrial Crops and Products','Crop Science',
    'Field Crops Research','European Journal of Agronomy','Agronomy','Journal of Agronomy and Crop Science',
    'Journal of Cereal Science','Rice','Rice Science','Journal of Plant Growth Regulation','Plant Growth Regulation',
    'Plant Genetic Resources','Genetic Resources and Crop Evolution','Euphytica','Breeding Science','Molecular Breeding',
    'Plant Breeding','Journal of Cotton Research','The Crop Journal','Cereal Research Communications',
    'Scientia Horticulturae','Horticulturae','Fruit Research','Vegetable Research','Annual Review of Phytopathology',
    'Current Opinion in Plant Biology','Plant Stress','GM Crops & Food','Current Plant Biology','Plant Disease',
    'Plants-Basel','Plant And Cell Physiology','Plant Genome','Plant Foods for Human Nutrition','Phytopathology Research',
    'Physiological and Molecular Plant Pathology','Physiology and Molecular Biology of Plants','Journal of Plant Interactions',
    'Botanical Studies','Journal of Soil Science and Plant Nutrition','Botanical Review','South African Journal of Botany',
    'American Journal of Botany','Plant Nano Biology','Plant Signaling and Behavior','Journal of Applied Genetics',
    'Plant Reproduction Biology','Crop Design','Plant Phenomics Research',
    # ── 生物信息学/计算生物学专业刊 (2026-08-27 新增, 供"生物信息"主题检索)
    'Bioinformatics','Nucleic Acids Research','Briefings in Bioinformatics','Genome Research','BMC Bioinformatics',
    'PLOS Computational Biology','Database','GigaScience','Nature Methods','Nature Biotechnology',
    'Frontiers in Genetics','Journal of Molecular Biology','BioData Mining','PeerJ',
]

def get_journals(core_only=False):
    """期刊集: core_only=True 用 100 本核心; False 用 JCR 全部 502 本中植物/组学相关子集。"""
    if core_only:
        return CORE_JOURNALS
    import re
    return [j for j in JOURNAL_JCR_PLANT
            if re.search(r'plant|botan|crop|agron|hortic|forest|genome|genetic|breed|transcript|mol|cell|patholog|physiolog', j, re.I)
            and len(j) < 50]

# ══════════════════════════════════════════════════════════════
# 14 组主题关键词 (与 daily_update 对齐 + 2026-08-26 新增3组 + 2026-08-27 新增生物信息)
# 胁迫原本就是主题7(胁迫与免疫), 未新增主题组, 仅在关键词补泛化 stress
# ══════════════════════════════════════════════════════════════
TOPICS = [
    # 1 单细胞组学 (核心)
    'single-cell OR scRNA-seq OR single nucleus OR snRNA-seq OR scATAC-seq OR single cell atlas OR cell atlas',
    # 2 空间转录组 (核心)
    'spatial transcriptom OR Stereo-seq OR Visium OR Xenium OR MERFISH OR spatial multi-omics OR spatially resolved',
    # 3 光信号与光合
    'light signaling OR photomorphogenesis OR phytochrome OR photoreceptor OR blue light OR red light OR shade avoidance OR photosynthesis OR chloroplast OR stomatal OR circadian OR photoperiod',
    # 4 植物发育
    'plant development OR root development OR shoot apical OR flower development OR seed development OR vascular development OR wood formation OR xylem OR phloem OR meristem OR organogenesis OR cambium OR embryogenesis',
    # 5 ATAC / 多组学
    'ATAC-seq OR multi-omics OR snATAC OR CUT&Tag',
    # 6 愈伤 / 再生
    'callus OR regeneration OR somatic embryo OR reprogramming OR de novo organogenesis',
    # 7 胁迫与免疫 (原有主题, 2026-08-26 关键词补泛化 stress/tolerance)
    'stress OR salt stress OR drought stress OR cold stress OR heat stress OR water stress OR osmotic stress OR heavy metal OR stress tolerance OR immunity OR pathogen OR defense OR disease resistance',
    # 8 代谢与天然产物
    'flavonoid OR anthocyanin OR terpenoid OR alkaloid OR metabolic engineering OR biosynthesis OR secondary metabolism OR specialized metabolite',
    # 9 表观遗传
    'histone OR chromatin OR DNA methylation OR H3K27 OR epigenetic OR non-coding RNA OR small RNA',
    # 10 激素信号
    'auxin OR gibberellin OR abscisic acid OR jasmonic acid OR salicylic acid OR ethylene OR brassinosteroid OR strigolactone OR cytokinin',
    # 11 分子机理 (2026-08-26 新增)
    'gene regulation OR transcription factor OR regulatory network OR signaling pathway OR molecular mechanism OR protein-protein interaction OR post-translational modification OR kinase OR receptor',
    # 12 遗传育种 (2026-08-26 新增)
    'genome-wide association OR quantitative trait locus OR GWAS OR marker-assisted selection OR genome editing OR CRISPR OR breeding OR genetic diversity OR QTL mapping OR molecular marker OR genomic selection',
    # 13 基因组 (2026-08-26 新增)
    'genome assembly OR pan-genome OR pangenome OR comparative genomics OR genomic variation OR structural variant OR gene family OR homeolog OR whole genome',
    # 14 生物信息学 (2026-08-27 新增, 偏向植物生信方法/工具/数据库)
    'plant bioinformatics OR bioinformatics pipeline OR computational tool OR sequence analysis OR transcriptome assembly OR gene expression analysis OR machine learning OR deep learning OR network analysis OR pathway analysis OR ortholog OR phylogenetic analysis OR functional annotation OR genomic database OR single-cell bioinformatics OR spatial analysis tool OR de novo assembly OR variant calling OR gene ontology OR database resource',
]

def search_pubmed_term(term, days, max_results):
    from_date = (datetime.now() - timedelta(days=days)).strftime('%Y/%m/%d')
    full = f'({term}) AND ("{from_date}"[Date - Publication] : "3000"[Date - Publication])'
    url = ('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term='
           + urllib.parse.quote(full) + f'&retmax={max_results}&sort=date&retmode=json')
    try:
        d = json.loads(urllib.request.urlopen(url, timeout=20).read())
        return d.get('esearchresult', {}).get('idlist', [])
    except Exception as e:
        print(f'  ⚠ {str(e)[:40]}')
        return []


# ══════════════════════════════════════════════════════════════
# 检索核心: 每主题一次 [Journal] OR 大查询 (2026-08-26 优化)
# 原设计 100刊×13主题=1300 次串行 esearch, PubMed 限流下极慢(~25min未完成)。
# 现改为: 全部期刊用 [Journal] OR 组合成一次查询 × 13 主题 = 13 次。
# 100 刊 OR ≈ 3758 字符 < PubMed 4800 上限, 无需分组。
# 13 次查询 ≈ 15-30s, 提升 ~100 倍。
# ══════════════════════════════════════════════════════════════
def journal_or_clause(journals):
    """把期刊列表构造成 [Journal] OR 子句。"""
    return '(' + ' OR '.join(f'"{j}"[Journal]' for j in journals) + ')'

def search_topic_in_journals(journals, topic, days, max_results):
    """在给定期刊组内按主题词检索一次, 返回 PMID 列表。"""
    from_date = (datetime.now() - timedelta(days=days)).strftime('%Y/%m/%d')
    jc = journal_or_clause(journals)
    full = f'({jc}) AND ({topic}) AND ("{from_date}"[Date - Publication] : "3000"[Date - Publication])'
    url = ('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term='
           + urllib.parse.quote(full) + f'&retmax={max_results}&sort=date&retmode=json')
    try:
        d = json.loads(urllib.request.urlopen(url, timeout=20).read())
        return d.get('esearchresult', {}).get('idlist', [])
    except Exception as e:
        print(f'  ⚠ {str(e)[:40]}')
        return []

# 兼容旧单刊查询(保留)
def search_pubmed_term(term, days, max_results):  # noqa: F811 (保留, main及外部调用)
    from_date = (datetime.now() - timedelta(days=days)).strftime('%Y/%m/%d')
    full = f'({term}) AND ("{from_date}"[Date - Publication] : "3000"[Date - Publication])'
    url = ('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term='
           + urllib.parse.quote(full) + f'&retmax={max_results}&sort=date&retmode=json')
    try:
        d = json.loads(urllib.request.urlopen(url, timeout=20).read())
        return d.get('esearchresult', {}).get('idlist', [])
    except Exception as e:
        print(f'  ⚠ {str(e)[:40]}')
        return []

def import_pmids(pmids):
    """把 PMID 清单导入为概念页(与 daily_update 过滤链一致), 返回导入数。"""
    import daily_update as du
    import theme_filter
    from daily_full_pipeline import is_plant_content  # 复用多源校验

    existing_dois = du.get_existing_dois()
    imported = 0
    for pmid in sorted(pmids):
        p = du.fetch_full_paper(pmid)
        if not p or not p.get('doi'):
            continue
        if p['doi'] in existing_dois:
            continue
        # 期刊校验: JCR → 精确 → 关键词 (与 daily_update 一致)
        from daily_update import journal_in_jcr as _jcr, JOURNAL_EXACT_LOWER, JOURNAL_KEYWORDS
        jl = (p.get('journal') or '').lower()
        jok = _jcr(p.get('journal') or '')
        if not jok:
            jok = jl in JOURNAL_EXACT_LOWER
        if not jok:
            jok = any(kw in jl for kw in JOURNAL_KEYWORDS)
        if not jok:
            continue
        # 主题过滤双保险
        try:
            ok, why = theme_filter.is_relevant_plant_paper(p.get('title',''), p.get('abstract',''), p.get('journal',''))
            if not ok:
                print(f'  ⛔ 主题过滤拒绝: {why[:25]} | {p["title"][:45]}')
                continue
        except ImportError:
            pass
        if not is_plant_content(p.get('title','') + ' ' + p.get('abstract','')):
            continue
        # 创建概念页 (与 daily_update 相同格式)
        from datetime import datetime as _dt
        slug = f"daily-{pmid}"
        base = '/mnt/g/hermes_obsidian/hermes'
        content = f"""---
title: {p['title'][:80]}
created: {_dt.now().strftime('%Y-%m-%d')}
type: concept
tags: [papers]
pmid: {pmid}
doi: {p['doi']}
confidence: high
---

# {p['title']}

## 论文信息
- **期刊**: {p.get('journal','')} ({p.get('year','')})
- **PMID**: [{pmid}](https://pubmed.ncbi.nlm.nih.gov/{pmid}/)
- **DOI**: [{p['doi']}](https://doi.org/{p['doi']})
- **第一作者**: {p.get('first_author','')}
- **作者**: {', '.join(p.get('authors',[])[:8])}

## 摘要
{p.get('abstract','')[:3000]}

## 深度提炼

**物种**: {'plant' if p.get('is_plant') else '—'}
**来源**: PMID:{pmid} | DOI:{p['doi']}
"""
        fp = f"{base}/concepts/{slug}.md"
        if os.path.exists(fp):
            continue
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        existing_dois.add(p['doi'])
        imported += 1
        print(f'  📥 导入 {slug} | {p["title"][:55]}')
    return imported

def main():
    days = 365
    maxr = 10
    core_only = '--core-only' in sys.argv
    dry = '--dry-run' in sys.argv
    do_import = '--import' in sys.argv
    for i, a in enumerate(sys.argv):
        if a == '--days' and i+1 < len(sys.argv): days = int(sys.argv[i+1])
        if a == '--max' and i+1 < len(sys.argv): maxr = int(sys.argv[i+1])

    journals = get_journals(core_only)
    print(f'期刊数: {len(journals)} (core_only={core_only}), 主题数: {len(TOPICS)}, 天数: {days}')
    # 2026-08-26 优化: 全部期刊 OR 太大触发 414; 按组批量 OR。
    # 每 20 刊一组 × 13 主题 = 65 次查询 (URL ~1365 字符安全)
    GROUP = 20
    import math
    jgroups = [journals[i:i+GROUP] for i in range(0, len(journals), GROUP)]
    total_q = len(jgroups) * len(TOPICS)
    print(f'计划检索 {total_q} 次 ({len(jgroups)}组 × {len(TOPICS)}主题, 每20刊OR), 预计 ~{total_q*0.5/60:.1f} 分钟')

    all_ids = set()
    for jg in jgroups:
        for topic in TOPICS:
            if dry:
                continue
            ids = search_topic_in_journals(jg, topic, days, maxr)
            if ids:
                print(f'  [{jg[0][:14]}... +{len(jg)-1}刊, {topic.split(" OR ")[0][:16]}] {len(ids)} hits')
            all_ids.update(ids)
            time.sleep(0.5)  # 限速防 429

    if dry:
        print(f'[dry-run] 将检索 {total_q} 次 ({len(jgroups)}组×{len(TOPICS)}主题)')
        jc = journal_or_clause(jgroups[0])
        print(f'  示例: ({jc[:150]}...) AND ({TOPICS[0][:50]}...)')
        print(f'  胁迫主题含 stress: TOPICS[6] 含 "stress"')
        return

    print(f'\n去重后 PMID 总数: {len(all_ids)}')
    out = 'journal_focus_search.ids'
    with open(out, 'w') as f:
        f.write('\n'.join(sorted(all_ids)))
    print(f'已写入 {out}')

    if do_import:
        print(f'\n导入阶段: 处理 {len(all_ids)} 个 PMID ...')
        n = import_pmids(all_ids)
        print(f'导入完成: {n} 篇新增概念页')

if __name__ == '__main__':
    main()
