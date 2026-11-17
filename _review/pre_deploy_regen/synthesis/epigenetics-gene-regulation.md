---

title: "表观与基因调控 — Synthesis"
created: 2026-06-01
total_evidence: 139
total_papers: 40
library_papers: 381  # 全库按themes归类该主题文献数
type: synthesis
body_status: rebuilt-2026-11-03
tags: [epigenetic, gene-regulation, synthesis]
legacy_archive: _review/synthesis_legacy_20261103/epigenetics-gene-regulation.md
rebuild_rule: evidence-fields-only; no-cross-evidence-inference

---
# 表观遗传与基因调控 知识综合（证据重建版）

<!-- AUTO-EVIDENCE-STRENGTH:START -->

## 证据覆盖与强度（自动统计，可复算）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据条目 | 139 | 本主题归属的证据对象数 |
| 独立论文 | 40 | 去重后的 PMID/DOI 数 |
| 平均每篇证据数 | 3.48 | <1.0 说明多数论文只贡献 1 条结论 |
| 单条证据论文占比 | 40% | 越高说明"每篇论文一个结论"，系统性弱 |
| 主要物种 | Arabidopsis thaliana(79)、Nicotiana tabacum(48)、Oryza sativa(36)、Solanum lycopersicum(16)、Ficus carica(16)、Zea mays(13) | 物种过度集中则外推性受限 |
| 证据类型 | expression/regulation 91；protein interaction 14；DNA binding/regulation 13；genetic perturbation 12；omics/co-occurrence 6；descriptive/observational 2 | 表达/关联类居多时，因果结论需打折扣 |

> 归属依据：`themes.py` 标签别名表（高置信）+ 关键词兜底（低置信）。本段由脚本生成，不构成结论；结论性文字须回原文核对。

### 可复核证据索引（前 12 条，按断言长度）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `ref-genetics-104-033142-f5` | 10.1534/genetics.104.033142 | Changes in histone acetylation are detected within the gate the role of a specific histone |
| `ms-10-3389_fpls-2026-1845669-f3` | 10.3389/fpls.2026.1845669 | Stress-responsive transcription factors from the MYB, WRKY, bZIP, AP2/ERF, NAC and basic h |
| `ref-j-bbrc-2016-12-086-f2` | 10.1016/j.bbrc.2016.12.086 | Indeed, H3K14 acetylation by GCN5 is 251 mechanistically coupled to H3 serine10 phosphoryl |
| `daily-42968200-f5` | 10.1186/s13059-022-02768-x | The histone acetyltransferase IDM1 is required for the DNA demethylase ROS1 to remove DNA  |
| `ms-10-1007_s00418-026-02500-x-f7` | 10.1007/s00418-026-02500-x | (2012) shows that the lack of H3K56 acetylation causes a significant delay in the completi |
| `ref-s42003-019-0646-5-f2` | 10.1038/s42003-019-0646-5 | Inhibition of HISTONE ACETYLTRANSFERASE OF THE GNAT/MYST SUPERFAMILY 1/GENERAL CON- TROL N |
| `ref-nature08682-f5` | 10.1038/nature08682 | A genetic analysis showed that TMM is epistatic to STOMAGEN (At4g12970), suggesting that s |
| `ref-ssq018-f8` | 10.1093/mp/ssq018 | Thebromodomain binds to acetylated histone lysine motifs (Zeng and Zhou, 2002), and theref |
| `ref-journal-pgen-1010473-f7` | 10.1371/journal.pgen.1010473 | We then obtained HDT4 T-DNA insertion line (hdt4-1) and explored its drought phenotype (S5 |
| `ref-s41467-023-37263-9-f6` | 10.1038/s41467-023-37263-9 | Collectively, these results suggest that TRB- ZFs can recruit JMJ14 to regions with low or |
| `differential-accessibility-regulates-cell-type-expression` | 10.1016/j.molp.2021.01.001 | Integrative analysis of snATAC-seq and scRNA-seq data demonstrates that cell-type-specific |
| `ref-ssq018-f6` | 10.1093/mp/ssq018 | Either AtGCN5 has several target lysine residues or synergistic interaction between differ |

### 证据语义分层

| 证据类型 | 条目数 | 可支持的推断强度 |
|---|---:|---|
| genetic perturbation | 12 | 遗传因果（扰动后表型/表达改变） |
| protein interaction | 14 | 物理互作（Co-IP/Y2H/BiFC/pull-down） |
| DNA binding/regulation | 13 | 直接调控（ChIP/EMSA/启动子报告） |
| expression/regulation | 91 | 表达相关（转录组/qPCR，不能单独推因果） |
| phenotypic/association | 1 | 表型关联（GWAS/QTL/自然变异/田间） |
| omics/co-occurrence | 6 | 组学共现（单细胞簇/共表达网络，非调控） |
| descriptive/observational | 2 | 描述性观察（无扰动/互作/关联设计） |

> 读法：`genetic perturbation` 才是因果证据；`expression/regulation` 与 `omics/co-occurrence` 只能提出假说，不能证明调控或因果。

### 遗传扰动类证据（关键词命中，前 5 条；需回原文核实实验设计）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `ref-journal-pgen-1010473-f7` | 10.1371/journal.pgen.1010473 | We then obtained HDT4 T-DNA insertion line (hdt4-1) and explored its drought phenotype (S5B–S5D Fig) |
| `a-transcriptional-cascade-mediated-by-two-f8` | 10.1111/jipb.13650 | Knockout of SlAP2c in two tomato cultivars resulted in greater accumulation of carotenoids, particul |
| `ref-nrm-2016-116-f2` | 10.1038/nrm.2016.116 | Although knockdown of RBBP6 leads to global 3ʹ UTR lengthening, RBBP6 also appears to be important s |
| `ref-nature08682-f6` | 10.1038/nature08682 | Other STOMAGENsilenced lines made with another artificial microRNA (12 independent T2 lines) and dou |
| `ref-j-jplph-2015-12-006-f6` | 10.1016/j.jplph.2015.12.006 | Clf swn doubleand emf2 single-mutants have reduced capability for forming calli from leaf explants ( |

### 正文状态

> 本页子主题正文为历史人工/LLM 文本，**未由本次证据重建**；只有本自动段与 frontmatter 计数反映当前证据快照。正文中的机制性表述须逐条回到原始研究核对，不得仅凭本页引用。

<!-- AUTO-EVIDENCE-STRENGTH:END -->

> 本页正文于 2026-11-03 由 `rebuild_synthesis_body.py` 从 **139 条证据对象 / 40 篇文献**确定性重建：所有陈述均可回溯到下列证据页；英文为原文摘录，未经改写；不含跨证据的推测性归纳。历史人工正文已归档至 `_review/synthesis_legacy_20261103`，不再作为本页结论来源。
>
> 阅读约定：`遗传扰动` / `蛋白互作` / `DNA 结合` 三类证据才支持“因果”或“直接调控”的表述；`表达相关` 与 `组学共现` 只能提出关联性假说。

## 1. 主题概览（自动统计）

| 指标 | 值 |
|---|---|
| 证据对象 | 139 |
| 独立文献（DOI/PMID 去重） | 40 |
| 平均每篇证据数 | 3.48 |
| 证据类型构成 | expression/regulation(91)、protein interaction(14)、DNA binding/regulation(13)、genetic perturbation(12)、omics/co-occurrence(6)、descriptive/observational(2)、phenotypic/association(1) |
| 主要物种 | Arabidopsis thaliana(79)、Nicotiana tabacum(48)、Oryza sativa(36)、Solanum lycopersicum(16)、Ficus carica(16)、Zea mays(13) |
| 子主题覆盖 | 6 个（其中证据 <5 条的 1 个） |

因果级证据共 **39 条**，占本主题证据的 **28.1%**。这一比例决定本主题哪些结论可以写成机制，哪些只能写成相关性。

## 2. 子主题分解（按证据重建）

> 一条证据可同时命中多个子主题（共 33 条跨组），因此各子主题计数之和大于总证据数。

### 2.1 DNA 甲基化与去甲基化

**规模**：5 条证据 / 2 篇文献。**证据构成**：expression/regulation(4)、protein interaction(1)。

**形态判断**：以表达相关为主（80%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：含 1 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 4 条仅支持关联。

**主要物种**：Solanum lycopersicum(3)、Marchantia polymorpha(3)、Brassica napus(3)、Pisum sativum(2)、Oryza sativa(2)。

**代表断言（原文摘录，未改写）**

- “The histone acetyltransferase IDM1 is required for the DNA demethylase ROS1 to remove DNA methylation in some genomic regions [, ]; histone deacetylase 6 (HDA6) interacts with MET1…” — [[daily-42968200-f5]]（`10.1186/s13059-022-02768-x`，protein interaction）
- “We demonstrate that transcriptional activation of representative FOD genes requires the heterotrimeric Nuclear Factor Y (NF-Y) complex, which establishes active chromatin states at…” — [[ms-10-1038_s41467-026-77029-7-f5]]（`10.1038/s41467-026-77029-7`，expression/regulation）

### 2.2 组蛋白修饰与染色质状态

**规模**：59 条证据 / 26 篇文献。**证据构成**：expression/regulation(39)、DNA binding/regulation(9)、protein interaction(6)、genetic perturbation(3)、omics/co-occurrence(1)、descriptive/observational(1)。

**形态判断**：以表达相关为主（66%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：含 18 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 41 条仅支持关联。

**主要物种**：Arabidopsis thaliana(40)、Nicotiana tabacum(25)、Oryza sativa(18)、Zea mays(11)、Solanum lycopersicum(7)。

**代表断言（原文摘录，未改写）**

- “Changes in histone acetylation are detected within the gate the role of a specific histone modification in the expression of target gene in Ws, heterozygous, and homovicinity of pr…” — [[ref-genetics-104-033142-f5]]（`10.1534/genetics.104.033142`，DNA binding/regulation）
- “Stress-responsive transcription factors from the MYB, WRKY, bZIP, AP2/ERF, NAC and basic helix-loop-helix families may recruit histone deacetylases to target promoters, where the r…” — [[ms-10-3389_fpls-2026-1845669-f3]]（`10.3389/fpls.2026.1845669`，DNA binding/regulation）
- “The histone acetyltransferase IDM1 is required for the DNA demethylase ROS1 to remove DNA methylation in some genomic regions [, ]; histone deacetylase 6 (HDA6) interacts with MET1…” — [[daily-42968200-f5]]（`10.1186/s13059-022-02768-x`，protein interaction）

### 2.3 染色质重塑与三维构象

**规模**：14 条证据 / 10 篇文献。**证据构成**：expression/regulation(9)、protein interaction(2)、DNA binding/regulation(2)、genetic perturbation(1)。

**形态判断**：以表达相关为主（64%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：含 5 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 9 条仅支持关联。

**主要物种**：Arabidopsis thaliana(6)、Nicotiana tabacum(5)、Ficus carica(4)、Solanum lycopersicum(3)、Oryza sativa(3)。

**代表断言（原文摘录，未改写）**

- “Stress-responsive transcription factors from the MYB, WRKY, bZIP, AP2/ERF, NAC and basic helix-loop-helix families may recruit histone deacetylases to target promoters, where the r…” — [[ms-10-3389_fpls-2026-1845669-f3]]（`10.3389/fpls.2026.1845669`，DNA binding/regulation）
- “The histone acetyltransferase IDM1 is required for the DNA demethylase ROS1 to remove DNA methylation in some genomic regions [, ]; histone deacetylase 6 (HDA6) interacts with MET1…” — [[daily-42968200-f5]]（`10.1186/s13059-022-02768-x`，protein interaction）
- “2001) that MAPK Hog1 recruits RPD3-SIN3 and targets to the promoter of osmotic responsive genes leading to may be involved in the modification of some specific lysine residues (e.g…” — [[ref-genetics-104-033142-f6]]（`10.1534/genetics.104.033142`，DNA binding/regulation）

### 2.4 非编码 RNA 与转录沉默

**规模**：5 条证据 / 2 篇文献。**证据构成**：expression/regulation(4)、genetic perturbation(1)。

**形态判断**：以表达相关为主（80%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：含 1 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 4 条仅支持关联。

**主要物种**：Arabidopsis thaliana(5)、Zea mays(1)、Oryza sativa(1)。

**代表断言（原文摘录，未改写）**

- “Overexpression of HDA19 in 35S:HDA19 plants decreased histone acetylation levels, whereas downregulation of HDA19 in HDA19-RNA interference (RNAi) plants increased histone acetylat…” — [[ref-tpc-104-028514-f2]]（`10.1105/tpc.104.028514`，genetic perturbation）
- “A recent study showed that APA isoform expression influences about 10% of targeting by miRNAs between any two cell types analysed and, importantly, that the accuracy of target pred…” — [[ref-nrm-2016-116-f1]]（`10.1038/nrm.2016.116`，expression/regulation）

### 2.5 转录因子与顺式调控元件

**规模**：26 条证据 / 17 篇文献。**证据构成**：DNA binding/regulation(12)、protein interaction(7)、expression/regulation(4)、omics/co-occurrence(2)、genetic perturbation(1)。

**形态判断**：以DNA 结合为主（46%），该子主题的机制表述有一手实验支撑，但结论边界受物种与处理条件限制。

**推断上限**：含 20 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 6 条仅支持关联。

**主要物种**：Nicotiana tabacum(13)、Arabidopsis thaliana(13)、Oryza sativa(9)、Solanum lycopersicum(4)、Citrus spp.(4)。

**代表断言（原文摘录，未改写）**

- “Changes in histone acetylation are detected within the gate the role of a specific histone modification in the expression of target gene in Ws, heterozygous, and homovicinity of pr…” — [[ref-genetics-104-033142-f5]]（`10.1534/genetics.104.033142`，DNA binding/regulation）
- “Stress-responsive transcription factors from the MYB, WRKY, bZIP, AP2/ERF, NAC and basic helix-loop-helix families may recruit histone deacetylases to target promoters, where the r…” — [[ms-10-3389_fpls-2026-1845669-f3]]（`10.3389/fpls.2026.1845669`，DNA binding/regulation）
- “Knockout of SlAP2c in two tomato cultivars resulted in greater accumulation of carotenoids, particularly lycopene, while overexpression of SlAP2c driven by the ripening‐ speciﬁc pr…” — [[a-transcriptional-cascade-mediated-by-two-f8]]（`10.1111/jipb.13650`，genetic perturbation）

### 2.6 表观遗传与发育/逆境可塑性

**规模**：27 条证据 / 13 篇文献。**证据构成**：expression/regulation(18)、genetic perturbation(4)、DNA binding/regulation(2)、phenotypic/association(1)、omics/co-occurrence(1)、protein interaction(1)。

**形态判断**：以表达相关为主（67%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：含 7 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 20 条仅支持关联。

**主要物种**：Arabidopsis thaliana(17)、Nicotiana tabacum(14)、Oryza sativa(13)、Plant(5)、Solanum lycopersicum(5)。

**代表断言（原文摘录，未改写）**

- “Stress-responsive transcription factors from the MYB, WRKY, bZIP, AP2/ERF, NAC and basic helix-loop-helix families may recruit histone deacetylases to target promoters, where the r…” — [[ms-10-3389_fpls-2026-1845669-f3]]（`10.3389/fpls.2026.1845669`，DNA binding/regulation）
- “We then obtained HDT4 T-DNA insertion line (hdt4-1) and explored its drought phenotype (S5B–S5D Fig) Fig We found that hdt4-1 was more drought tolerant than Col-0 (Fig 5D), and HDT…” — [[ref-journal-pgen-1010473-f7]]（`10.1371/journal.pgen.1010473`，genetic perturbation）
- “Other STOMAGENsilenced lines made with another artificial microRNA (12 independent T2 lines) and double-stranded RNA (dsRNA; four independent T2 lines)exhibitedthesamephenotype(Sup…” — [[ref-nature08682-f6]]（`10.1038/nature08682`，genetic perturbation）

### 2.7 表观编辑与工程化改造

**本知识库当前无归属证据**（子主题已定义但未被任何证据命中）。这是覆盖缺口，不是“该方向不重要”。

## 3. 可直接引用的因果级证据（自动筛选）

以下 39 条证据的实验设计属于扰动或直接互作，可作为机制论断的一手依据；引用时须核对原文的物种、组织与处理条件。

| 证据页 | DOI | 类型 | 断言（摘录） |
|---|---|---|---|
| [[a-transcriptional-cascade-mediated-by-two-f2]] | `10.1111/jipb.13650` | protein interaction | Taken together, these results suggest that SlAP2c represses lycopene bi- osynthesis by interacting with the TPL2/4‐HDA1/… |
| [[a-transcriptional-cascade-mediated-by-two-f3]] | `10.1111/jipb.13650` | DNA binding/regulation | Taken together, these results suggest that SlAP2c recruits the TPL2/4–HDA1/3 transcrip- tional repressive complex to rep… |
| [[a-transcriptional-cascade-mediated-by-two-f8]] | `10.1111/jipb.13650` | genetic perturbation | Knockout of SlAP2c in two tomato cultivars resulted in greater accumulation of carotenoids, particularly lycopene, while… |
| [[alfalfa-cadmium-sc-multiomics-f3]] | `10.1093/hr/uhag117` | genetic perturbation | The results revealed that 356 overexpression of MsMT2A in yeast significantly increased tolerance to Cd stress (Fig. |
| [[csmyb73-negatively-regulates-theanine-accumulation-mediated-f2]] | `10.1093/hr/uhae012` | protein interaction | CsMYB73 was confirmed to act as a nucleus-localized transcription factor (TF), directly interacts with the CsGGT2 and Cs… |
| [[csmyb73-negatively-regulates-theanine-accumulation-mediated-f3]] | `10.1093/hr/uhae012` | DNA binding/regulation | CsMYB73 targets and differentially regulates the promoters of CsGGT2 and CsGGT4 In general, MYBRs present in target gene… |
| [[csmyb73-negatively-regulates-theanine-accumulation-mediated-f4]] | `10.1093/hr/uhae012` | protein interaction | To understand how CsGGT2 and CsGGT4 were transcriptionally regulated, we explored the potential for CsMYB73 to physicall… |
| [[daily-42968200-f5]] | `10.1186/s13059-022-02768-x` | protein interaction | The histone acetyltransferase IDM1 is required for the DNA demethylase ROS1 to remove DNA methylation in some genomic re… |
| [[ms-10-1007_s44372-026-00856-x-f1]] | `10.1007/s44372-026-00856-x` | DNA binding/regulation | These transcription factors bind specific cis-regulatory elements (ABRE, DRE/CRT, and MYBRC) in target gene promoters to… |
| [[ms-10-1186_s43897-026-00261-8-f2]] | `10.1186/s43897-026-00261-8` | protein interaction | The transcription factor RcMYC2 interacts with Mediator subunit RcMED25 and recruits histone deacetylase RcHDA8 to repre… |
| [[ms-10-3389_fpls-2026-1845669-f2]] | `10.3389/fpls.2026.1845669` | DNA binding/regulation | Histone deacetylation can repress gene expression by reducing histone acetylation, promoting nucleosome compaction and l… |
| [[ms-10-3389_fpls-2026-1845669-f3]] | `10.3389/fpls.2026.1845669` | DNA binding/regulation | Stress-responsive transcription factors from the MYB, WRKY, bZIP, AP2/ERF, NAC and basic helix-loop-helix families may r… |
| [[pdf-ijms24065608-f1]] | `10.3390/ijms24065608` | genetic perturbation | We showed how VIGS-induced gene silencing can be used to characterize transgenerational gene function(s) and altered epi… |
| [[pdf-tpj-70959-f2]] | `10.1111/tpj.70959` | protein interaction | This insight into the composite nature of the complex provides clues about how the polymerase interacts with transcripti… |
| [[ref-Chapter-Three---Defining-the-P-f1]] | `10.1016/bs.ctdb.2015.12.002` | protein interaction | After initially interacting with another transcription factor, SCARECROW (SCR), together they activate a D-type cyclin, … |

（另有 24 条未列出，可在 `evidence/` 按 evidence_type 过滤。）

## 4. 张力与矛盾（自动检测）

在当前证据集上未检出方向性冲突。注意：这只说明“没有互相矛盾的摘录”，不说明领域内不存在争议——多数争议需要全文级的实验条件比对才能发现。

## 5. 覆盖缺口（由证据分布直接导出）

- **未被覆盖的子主题 1 个**：表观编辑与工程化改造。这些方向在本库中没有可引用证据，任何涉及它们的论述都必须另行检索。
- **未能归入任何子主题的证据 42 条**：多为方法描述或跨领域摘录，已计入主题总量但未参与分组。

## 6. 历史正文说明

本页 2026-11-03 之前的正文为人工/LLM 撰写，未与证据逐条对齐，含不可核的行内断言缺引用、格式残留与跨主题内容混入。该正文已原样归档至 `_review/synthesis_legacy_20261103`，保留供追溯，**不得再作为结论来源**。原“与大豆项目关联”的定性判断保留在 frontmatter 的 `soybean_relevance` 字段，其论证过程同样需重新取证。
