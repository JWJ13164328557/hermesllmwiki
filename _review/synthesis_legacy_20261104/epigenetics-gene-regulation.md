---

title: "表观与基因调控 — Synthesis"
created: 2026-06-01
total_evidence: 2068
total_papers: 316
library_papers: 381  # 全库按themes归类该主题文献数
type: synthesis
body_status: rebuilt-2026-11-03
tags: [epigenetic, gene-regulation, synthesis]
legacy_archive: _review/synthesis_legacy_20261103/epigenetics-gene-regulation.md
rebuild_rule: evidence-fields-only; no-cross-evidence-inference
rebuild_version: v3

---
# 表观遗传与基因调控 知识综合（证据重建版 v3）

<!-- AUTO-EVIDENCE-STRENGTH:START -->

## 证据覆盖与强度（自动统计，可复算）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据条目 | 2068 | 本主题归属的证据对象数 |
| 独立论文 | 316 | 去重后的 PMID/DOI 数 |
| 平均每篇证据数 | 6.54 | <1.0 说明多数论文只贡献 1 条结论 |
| 单条证据论文占比 | 2% | 越高说明"每篇论文一个结论"，系统性弱 |
| 主要物种 | Arabidopsis thaliana(670)、Oryza sativa(610)、Nicotiana tabacum(399)、Zea mays(372)、Solanum lycopersicum(346)、Glycine max(216) | 物种过度集中则外推性受限 |
| 证据类型 | descriptive/observational 1228；protein interaction 292；expression/regulation 210；genetic perturbation 124；DNA binding/regulation 101；omics/co-occurrence 65 | 表达/关联类居多时，因果结论需打折扣 |

> 归属依据：`themes.py` 标签别名表（高置信）+ 关键词兜底（低置信）。本段由脚本生成，不构成结论；结论性文字须回原文核对。

### 可复核证据索引（前 12 条，按断言长度）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `daily-42228685-f1` | 10.1371/journal.pbio.3003811 | When we introduced intact or mutated HIPP19 at the miR408-5p target site with a GFP tag dr |
| `daily-42137983-f1` | 10.1093/nar/gkag476 | Using custom-made antibodies specific to the rice H2A.X variant, we show that it repressed |
| `daily-42432473-f6` | 10.1186/s12870-026-09489-4 | For instance, overexpression of Glycine max GATA58 in the Arabidopsis gnc ( AtGATA21 ) los |
| `daily-42285947-f1` | 10.1038/s41467-026-74024-w | In summary, overexpression of GbNAC072 C in combination with knockout of GhDEAH12 signific |
| `the-slgras9slzhd17-transcriptional-cascade-regulates-chlorop-f2` | 10.1111/nph.19530 | We show that SlGRAS9 is highly expressed in tomato fruit and knockout or downregulation of |
| `integrated-metabolomic-and-transcriptomic-analysis-reveals-f5` | 10.3390/ijms22168751 | In summary, EsMYB90 could strikingly increase the level of flavonoid metabolites via modul |
| `ref-journal-pgen-1010473-f7` | 10.1371/journal.pgen.1010473 | We then obtained HDT4 T-DNA insertion line (hdt4-1) and explored its drought phenotype (S5 |
| `ccnfyb3ccmate35-and-lncrna-ccltcscccs-modules-jointly-f3` | 10.1111/pbi.14179 | In our experiments, we found the double RNAi line exhibited a further increase in callose  |
| `daily-42216279-f4` | 10.1111/nph.71305 | The use of CRISPR/Cas for promoter editing in wheat was first demonstrated by multiplexed  |
| `daily-42773404-f5` | 10.1111/nph.71592 | Overexpression of ZmSPL12 suppresses maize root growth under normal, wellwatered (WW) cond |
| `ref-nrm-2016-116-f2` | 10.1038/nrm.2016.116 | Although knockdown of RBBP6 leads to global 3ʹ UTR lengthening, RBBP6 also appears to be i |
| `daily-42514481-f4` | 10.3390/plants15142113 | To target mutations, more and more evidence indicates that changes in gene copy number, ex |

### 证据语义分层

| 证据类型 | 条目数 | 可支持的推断强度 |
|---|---:|---|
| genetic perturbation | 124 | 遗传因果（扰动后表型/表达改变） |
| protein interaction | 292 | 物理互作（Co-IP/Y2H/BiFC/pull-down） |
| DNA binding/regulation | 101 | 直接调控（ChIP/EMSA/启动子报告） |
| expression/regulation | 210 | 表达相关（转录组/qPCR，不能单独推因果） |
| phenotypic/association | 48 | 表型关联（GWAS/QTL/自然变异/田间） |
| omics/co-occurrence | 65 | 组学共现（单细胞簇/共表达网络，非调控） |
| descriptive/observational | 1228 | 描述性/背景陈述（未报告可核验的实验设计） |

> 读法：`genetic perturbation` / `protein interaction` / `DNA binding/regulation` 可支持因果或直接调控；`expression/regulation` 与 `omics/co-occurrence` 只能提出假说，不能单独证明调控或因果。

### 遗传扰动类证据（仅高置信规则命中，前 5 条；仍须回原文核实）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `daily-42228685-f1` | 10.1371/journal.pbio.3003811 | When we introduced intact or mutated HIPP19 at the miR408-5p target site with a GFP tag driven by th |
| `daily-42137983-f1` | 10.1093/nar/gkag476 | Using custom-made antibodies specific to the rice H2A.X variant, we show that it repressed the depos |
| `daily-42432473-f6` | 10.1186/s12870-026-09489-4 | For instance, overexpression of Glycine max GATA58 in the Arabidopsis gnc ( AtGATA21 ) loss-of-funct |
| `daily-42285947-f1` | 10.1038/s41467-026-74024-w | In summary, overexpression of GbNAC072 C in combination with knockout of GhDEAH12 significantly enha |
| `the-slgras9slzhd17-transcriptional-cascade-regulates-chlorop-f2` | 10.1111/nph.19530 | We show that SlGRAS9 is highly expressed in tomato fruit and knockout or downregulation of this gene |

### 正文状态

> frontmatter 标记 `body_status: rebuilt-*` 的页面，其子主题正文由 `rebuild_synthesis_body.py` 按本页证据确定性重建；本自动段是该快照的统计摘要。未标记的页面保留历史正文，机制性表述须逐条回原文核对，不得仅凭本页引用。

<!-- AUTO-EVIDENCE-STRENGTH:END -->

> 本页正文于 2026-11-03 由 `rebuild_synthesis_body.py` 从 **1396 条证据对象 / 225 篇文献**确定性重建：所有陈述均可回溯到下列证据页；英文为原文摘录，未经改写；不含跨证据的推测性归纳。历史人工正文已归档至 `_review/synthesis_legacy_20261103`，不再作为本页结论来源。
>
> 阅读约定：`遗传扰动` / `蛋白互作` / `DNA 结合` 三类证据才支持“因果”或“直接调控”的表述；`表达相关` 与 `组学共现` 只能提出关联性假说。

## 0. 综述提要（受控生成）

本主题当前纳入 **1396 条证据 / 225 篇文献**。规则判定为因果或直接调控的 **351 条（25.1%）**；剔除方法描述、相关性措辞与无基因实体标注的条目后，可用于提要的 **189 条**。可判定程度最高的结论集中在CsMYB5a、PpbZIP44、SlAP2c：For example, ectopic overexpression of CsMYB5a in tobacco increased the PA content in flowers and inhibited anthocyanin accumulation; overex…（[[a-novel-r2r3myb-transcription-factor-famyb5-f7]]）；Overexpression of PpbZIP44 decreased the TCA cycle intermediate contents (e.g.（[[a-pear-s1-bzip-transcription-factor-ppbzip44-f6]]）；Knockout of SlAP2c in both the “MicroTom” and “Ailsa Craig” backgrounds resulted in greater lycopene accumulation, whereas overexpression of…（[[a-transcriptional-cascade-mediated-by-two-f6]]）。研究重心位于“表观遗传与发育/逆境可塑性”（237 条证据，占 17%）。证据的物种分布以 Arabidopsis thaliana 为首（607 条，43%）。七类证据均有覆盖，主要瓶颈从“类型缺失”转为“同一结论的独立复现不足”。阅读时须区分两类陈述：因果级证据支撑的“已证机制”，以及表达/组学/描述性证据提示的“候选关联”；后者不得改写成调控或因果。

> 提要由脚本按证据类型与实体计数生成，不含跨证据的机制外推；逐条依据见第 2–3 节。

## 1. 主题概览（自动统计）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据对象 | 1396 | 本主题归属的证据条目数 |
| 独立文献（DOI/PMID 去重） | 225 | 去重后的论文数 |
| 平均每篇证据数 | 6.20 | 接近 1.0 说明每篇论文只贡献一条结论，系统性弱 |
| 单条证据论文占比 | 6%（14/225） | 越高说明证据碎片化越严重 |
| 证据类型构成 | descriptive/observational(829)、protein interaction(187)、expression/regulation(150)、genetic perturbation(82)、DNA binding/regulation(82)、omics/co-occurrence(52)、phenotypic/association(14) | 描述性占多数时机制结论需打折扣 |
| 类型标注置信度 | low(885)、medium(394)、high(117) | 低置信度标注须回原文核对 |
| 主要物种 | Arabidopsis thaliana(607)、Oryza sativa(527)、Nicotiana tabacum(369)、Zea mays(360)、Solanum lycopersicum(267)、Triticum aestivum(172) | 物种过度集中则外推性受限 |
| 子主题覆盖 | 7/7（证据 <5 条的 0 个） | 覆盖缺口见第 7 节 |
| 未命中任何子主题的证据 | 760（54%） | 占比高说明子主题词表或证据文本需扩表 |

因果级证据共 **351 条**，占本主题证据的 **25.1%**。这一比例决定本主题哪些结论可以写成机制，哪些只能写成相关性。

物种主导度：**Arabidopsis thaliana** 出现在 607 条证据（43%）。分布较分散，单物种主导风险较低，但需注意各物种证据层级是否可比。

## 2. 子主题分解（按证据重建）

> 一条证据可同时命中多个子主题（共 156 条跨组），因此各子主题计数之和大于总证据数。物种×类型交叉表只统计已标注字段，空单元格表示该组合无证据，不等于不存在相应生物学过程。凡“因果层 0 条”的子主题，其代表断言只能读作相关性，不得改写为调控或因果。

### 2.1 DNA 甲基化与去甲基化

**规模** 26 条证据 / 12 篇文献；**构成** descriptive/observational(19)、protein interaction(4)、expression/regulation(3)；**因果层** 4 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Solanum lycopersicum、Zea mays，反复出现的实体为ROS1、CpGs；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-40972239-f4]]；[[daily-40972239-f6]]；[[daily-40972239-f7]]）。
- **证据层级的张力**：4 条属于遗传扰动/蛋白互作/DNA 结合，22 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-42968200-f5]]；[[daily-42968200-f6]]）。
- **可检验缺口**：遗传扰动、DNA 结合、表型关联、组学共现在本组缺证据；在补齐这些设计前，ROS1、CpGs 与“DNA 甲基化与去甲基化”的方向性关系应作为待检验命题（[[daily-40972239-f4]]；[[daily-40972239-f6]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 蛋白互作 | 表达相关 | 描述性 | 合计 |
|---|---|---|---|---|
| Oryza sativa | 1 | 1 | 6 | 8 |
| Solanum lycopersicum | 3 | 1 | 4 | 8 |
| Zea mays | 0 | 1 | 5 | 6 |
| Triticum aestivum | 0 | 0 | 5 | 5 |
| Nicotiana tabacum | 3 | 0 | 2 | 5 |

**基因实体（自动标注，前 5）**：ROS1(2)、CpGs(2)、IBM1(1)、CMT3(1)、CMT2(1)（标注覆盖 8/26）。

**代表断言（原文摘录，未改写）**

- “The histone acetyltransferase IDM1 is required for the DNA demethylase ROS1 to remove DNA methylation in some genomic regions [, ]; histone deacetylase 6 (HDA6) interacts with MET1…” — [[daily-42968200-f5]]（`10.1186/s43897-026-00250-x`，protein interaction）
- “These proteins bind to DNA methylation monitoring sequence regions through DNA methylation-dependent mechanisms and interact with putative transcriptional activators that contain t…” — [[daily-42657324-f2]]（`10.1093/hr/uhag152`，protein interaction）
- “Simultaneously, the AGO complex interacts with target DNA molecules in the nucleus, causing transcriptional repression via DNA methylation at the 5′ untranslated region (5′UTR), wh…” — [[pdf-ijms24065608-f4]]（`10.3390/ijms24065608`，protein interaction）

### 2.2 组蛋白修饰与染色质状态

**规模** 112 条证据 / 44 篇文献；**构成** descriptive/observational(51)、expression/regulation(24)、protein interaction(22)、omics/co-occurrence(6)、genetic perturbation(5)、DNA binding/regulation(4)；**因果层** 31 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Oryza sativa、Nicotiana tabacum，反复出现的实体为PRC2、AtGCN5、anthocyanin、carotenoid；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[a-transcriptional-cascade-mediated-by-two-f2]]；[[a-transcriptional-cascade-mediated-by-two-f3]]；[[daily-40972239-f7]]）。
- **证据层级的张力**：31 条属于遗传扰动/蛋白互作/DNA 结合，81 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-42231887-f2]]；[[daily-42231887-f3]]；[[daily-41971346-f2]]）。
- **可检验缺口**：表型关联在本组缺证据；在补齐这些设计前，PRC2、AtGCN5、anthocyanin 与“组蛋白修饰与染色质状态”的方向性关系应作为待检验命题（[[a-transcriptional-cascade-mediated-by-two-f2]]；[[a-transcriptional-cascade-mediated-by-two-f3]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|
| Arabidopsis thaliana | 3 | 12 | 4 | 13 | 3 | 35 | 70 |
| Oryza sativa | 3 | 11 | 0 | 8 | 2 | 15 | 39 |
| Nicotiana tabacum | 3 | 8 | 1 | 4 | 1 | 17 | 34 |
| Zea mays | 2 | 5 | 1 | 3 | 0 | 10 | 21 |
| Solanum lycopersicum | 1 | 5 | 1 | 3 | 1 | 7 | 18 |

**基因实体（自动标注，前 5）**：PRC2(5)、AtGCN5(5)、GCN5(4)、BPC1(3)、HDA9(3)（标注覆盖 55/112）。

**化合物实体（自动标注，前 5）**：anthocyanin(3)、carotenoid(1)、lycopene(1)、xylan(1)、xyloglucan(1)（标注覆盖 6/112）。

**代表断言（原文摘录，未改写）**

- “Using custom-made antibodies specific to the rice H2A.X variant, we show that it repressed the deposition of active H3K4me3 marks over gene bodies and transposable elements (TEs), …” — [[daily-42137983-f1]]（`10.1093/nar/gkag476`，genetic perturbation）
- “By performing histone pull-down assays using the OBE1 and OBE2 mixture, we found that OBE2 enhanced the binding affinity of OBE1 with H3K4me1/2/3 peptides and that OBE1 enhanced th…” — [[ref-embj-2023113639-f5]]（`10.15252/embj.2023113639`，protein interaction）
- “Thebromodomain binds to acetylated histone lysine motifs (Zeng and Zhou, 2002), and therefore can be considered as a reader of histoneacetylationmarkers.T-DNAinsertionsingcn5-1andg…” — [[ref-ssq018-f8]]（`10.1093/mp/ssq018`，protein interaction）

### 2.3 染色质重塑与三维构象

**规模** 133 条证据 / 100 篇文献；**构成** descriptive/observational(65)、protein interaction(29)、expression/regulation(16)、DNA binding/regulation(8)、omics/co-occurrence(7)、genetic perturbation(4)；**因果层** 41 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Arabidopsis thaliana、Zea mays，反复出现的实体为AP2、ChIPseq、anthocyanin、starch；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[a-novel-r2r3myb-transcription-factor-famyb5-f1]]；[[a-transcriptional-cascade-mediated-by-two-f4]]；[[b5-iZzyxHmz_WpXAsbrHTBStw-f4]]）。
- **证据层级的张力**：41 条属于遗传扰动/蛋白互作/DNA 结合，92 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[b5-iZzyxHmz_WpXAsbrHTBStw-f4]]；[[b5-kf00Og92ayHkmDBpso75bw-f7]]；[[daily-41971346-f2]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[b5-iZzyxHmz_WpXAsbrHTBStw-f4]]；[[b5-kf00Og92ayHkmDBpso75bw-f7]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Oryza sativa | 1 | 12 | 3 | 6 | 2 | 5 | 24 | 53 |
| Arabidopsis thaliana | 1 | 9 | 3 | 7 | 2 | 2 | 26 | 50 |
| Zea mays | 3 | 8 | 2 | 3 | 2 | 3 | 22 | 43 |
| Nicotiana tabacum | 2 | 9 | 3 | 4 | 2 | 0 | 18 | 38 |
| Solanum lycopersicum | 2 | 6 | 2 | 2 | 1 | 0 | 13 | 26 |

**基因实体（自动标注，前 5）**：AP2(2)、ChIPseq(2)、HY5(2)、GmPHD3(2)、MYC2(2)（标注覆盖 79/133）。

**化合物实体（自动标注，前 5）**：anthocyanin(8)、starch(2)、auxin(2)、flavonoid(2)、proanthocyanidin(1)（标注覆盖 18/133）。

**标注一致性提示**：本组 2 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[daily-42231887-f6]]。

**代表断言（原文摘录，未改写）**

- “Found that the reason for white appearance of ‘Jinba’ at the blooming stage was that the R3 MYB transcription factor CmMYB#7, which can interact with CmbHLH2, disrupted the MBW pro…” — [[cmnac25-targets-cmmyb6-to-positively-regulate-f2]]（`10.1186/s12915-023-01719-7`，protein interaction）
- “The mechanistic spine runs through the JAZ-MYC2 module: under drought, ABA-activated SnRK2 kinases phosphorylate transcription factors that induce JA-biosynthesis genes, elevating …” — [[daily-42689139-f3]]（`10.3389/fpls.2026.1924558`，protein interaction）
- “Our previous studies preliminarily identified a HTH-responsive transcription factor, GmPHD3, which interacts with the key HTH stress regulator GmSBH1 and exhibits distinct expressi…” — [[daily-42588879-f5]]（`10.3390/plants15152376`，protein interaction）

### 2.4 非编码 RNA 与转录沉默

**规模** 51 条证据 / 24 篇文献；**构成** descriptive/observational(38)、genetic perturbation(4)、expression/regulation(4)、protein interaction(4)、phenotypic/association(1)；**因果层** 8 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Nicotiana tabacum、Arabidopsis thaliana，反复出现的实体为CcMATE35、CcNFYB3、flavonol、auxin；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[biology-and-function-of-mir159-in-f5]]；[[ccnfyb3ccmate35-and-lncrna-ccltcscccs-modules-jointly-f2]]；[[ccnfyb3ccmate35-and-lncrna-ccltcscccs-modules-jointly-f3]]）。
- **证据层级的张力**：8 条属于遗传扰动/蛋白互作/DNA 结合，43 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-42317260-f3]]；[[daily-42368270-f6]]；[[cmnac25-targets-cmmyb6-to-positively-regulate-f5]]）。
- **可检验缺口**：DNA 结合、组学共现在本组缺证据；在补齐这些设计前，CcMATE35、CcNFYB3、flavonol 与“非编码 RNA 与转录沉默”的方向性关系应作为待检验命题（[[biology-and-function-of-mir159-in-f5]]；[[ccnfyb3ccmate35-and-lncrna-ccltcscccs-modules-jointly-f2]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | 表达相关 | 表型关联 | 描述性 | 合计 |
|---|---|---|---|---|---|---|
| Oryza sativa | 1 | 1 | 2 | 1 | 15 | 20 |
| Nicotiana tabacum | 1 | 1 | 1 | 0 | 14 | 17 |
| Arabidopsis thaliana | 2 | 1 | 1 | 0 | 12 | 16 |
| Solanum lycopersicum | 2 | 1 | 0 | 0 | 11 | 14 |
| Zea mays | 3 | 1 | 0 | 0 | 8 | 12 |

**基因实体（自动标注，前 5）**：CcMATE35(2)、CcNFYB3(2)、OsSPL9(2)、MiRNAs(2)、CcLTCS(1)（标注覆盖 17/51）。

**化合物实体（自动标注，前 5）**：flavonol(1)、auxin(1)、chlorophyll(1)（标注覆盖 3/51）。

**标注一致性提示**：本组 3 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[ccnfyb3ccmate35-and-lncrna-ccltcscccs-modules-jointly-f2]]。

**代表断言（原文摘录，未改写）**

- “In our experiments, we found the double RNAi line exhibited a further increase in callose concentration and a decrease in citrate release compared to the CcMATE35-RNAi and CcNFYB3-…” — [[ccnfyb3ccmate35-and-lncrna-ccltcscccs-modules-jointly-f3]]（`10.1111/pbi.14179`，genetic perturbation）
- “RISC uses these siRNAs to specifically interact with homologous RNA in the cell, thereby leading to endo-nucleolytic cleavage and the translational inhibition of the cognate target…” — [[pdf-ijms24065608-f3]]（`10.3390/ijms24065608`，protein interaction）
- “In soybean, GmDFB1—another ARM repeat protein—was reported to interact with GmSK17 and participate in siRNA suppression by blocking GmAGO1-mediated mRNA cleavage, ultimately leadin…” — [[daily-42317260-f3]]（`10.3389/fgene.2026.1850332`，protein interaction）

### 2.5 转录因子与顺式调控元件

**规模** 219 条证据 / 125 篇文献；**构成** descriptive/observational(96)、DNA binding/regulation(48)、protein interaction(48)、expression/regulation(12)、omics/co-occurrence(8)、genetic perturbation(5)；**因果层** 101 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Oryza sativa、Nicotiana tabacum，反复出现的实体为ChIP、VviERF003、anthocyanin、auxin；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[a-pear-s1-bzip-transcription-factor-ppbzip44-f7]]；[[a-transcriptional-cascade-mediated-by-two-f1]]；[[a-transcriptional-cascade-mediated-by-two-f3]]）。
- **证据层级的张力**：101 条属于遗传扰动/蛋白互作/DNA 结合，118 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[a-pear-s1-bzip-transcription-factor-ppbzip44-f7]]；[[a-transcriptional-cascade-mediated-by-two-f1]]；[[daily-41971346-f3]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[a-pear-s1-bzip-transcription-factor-ppbzip44-f7]]；[[a-transcriptional-cascade-mediated-by-two-f1]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Arabidopsis thaliana | 3 | 23 | 24 | 5 | 0 | 3 | 42 | 100 |
| Oryza sativa | 3 | 22 | 17 | 3 | 1 | 2 | 32 | 80 |
| Nicotiana tabacum | 4 | 15 | 17 | 2 | 1 | 1 | 32 | 72 |
| Zea mays | 0 | 13 | 16 | 3 | 1 | 1 | 28 | 62 |
| Solanum lycopersicum | 1 | 11 | 15 | 0 | 1 | 1 | 21 | 50 |

**基因实体（自动标注，前 5）**：ChIP(5)、VviERF003(5)、VviGT14(5)、PSY1(3)、CmMYB6(3)（标注覆盖 140/219）。

**化合物实体（自动标注，前 5）**：anthocyanin(13)、auxin(3)、carotenoid(2)、melatonin(2)、flavonoid(2)（标注覆盖 27/219）。

**标注一致性提示**：本组 1 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[sel-j-pbi-2017-09-005-f8]]。

**代表断言（原文摘录，未改写）**

- “Our results showed that GoHSFA4a directly binds to the detected HSF binding motifs in the promoter regions of the MVA pathway gene HMGS and the gossypol pathway gene CYP736A196 (Fi…” — [[ref-j-molp-2023-10-008-f6]]（`10.1016/j.molp.2023.10.008`，protein interaction）
- “An MBW complex formed by the CmMYB6-CmbHLH2 protein complex is crucial for activating anthocyanin accumulation in chrysanthemum, we have known that CmNAC25 directly binds to the pr…” — [[cmnac25-targets-cmmyb6-to-positively-regulate-f1]]（`10.1186/s12915-023-01719-7`，DNA binding/regulation）
- “When we introduced intact or mutated HIPP19 at the miR408-5p target site with a GFP tag driven by the native HIPP19 promoter (named HIPP19 and HIPP19m, respectively) into rice (Fig…” — [[daily-42228685-f1]]（`10.1371/journal.pbio.3003811`，genetic perturbation）

### 2.6 表观遗传与发育/逆境可塑性

**规模** 237 条证据 / 111 篇文献；**构成** descriptive/observational(153)、expression/regulation(35)、genetic perturbation(17)、protein interaction(15)、omics/co-occurrence(9)、DNA binding/regulation(6)；**因果层** 38 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Arabidopsis thaliana、Nicotiana tabacum，反复出现的实体为HDA9、WIND1、anthocyanin、auxin；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[a-novel-r2r3myb-transcription-factor-famyb5-f2]]；[[a-pear-s1-bzip-transcription-factor-ppbzip44-f4]]；[[alfalfa-cadmium-sc-multiomics-f1]]）。
- **证据层级的张力**：38 条属于遗传扰动/蛋白互作/DNA 结合，199 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[alfalfa-cadmium-sc-multiomics-f3]]；[[daily-40898604-f4]]；[[a-pear-s1-bzip-transcription-factor-ppbzip44-f4]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[alfalfa-cadmium-sc-multiomics-f3]]；[[daily-40898604-f4]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Oryza sativa | 9 | 8 | 3 | 16 | 1 | 5 | 74 | 116 |
| Arabidopsis thaliana | 7 | 5 | 2 | 15 | 1 | 3 | 71 | 104 |
| Nicotiana tabacum | 7 | 6 | 3 | 7 | 0 | 0 | 40 | 63 |
| Zea mays | 4 | 4 | 3 | 11 | 0 | 2 | 37 | 61 |
| Glycine max | 4 | 3 | 1 | 6 | 1 | 1 | 32 | 48 |

**基因实体（自动标注，前 5）**：HDA9(4)、WIND1(4)、BRC1(3)、HDA6(3)、CcMATE35(2)（标注覆盖 106/237）。

**化合物实体（自动标注，前 5）**：anthocyanin(2)、auxin(2)、starch(2)、melatonin(1)、chlorophyll(1)（标注覆盖 11/237）。

**标注一致性提示**：本组 1 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[ccnfyb3ccmate35-and-lncrna-ccltcscccs-modules-jointly-f2]]。

**代表断言（原文摘录，未改写）**

- “The enhanced tolerance of idr1–1 mutant seedlings to osmotic stress may stem from marked changes in DEG profiles at the early and middle stages of osmotic stress, especially at the…” — [[daily-42211481-f3]]（`10.3389/fpls.2026.1815995`，genetic perturbation）
- “A conserved regulatory framework involves the MYB–bHLH–WD40 (MBW) complex, in which R2R3-MYB and bHLH transcription factors interact with WD40 proteins to activate (or repress) ant…” — [[daily-42299342-f2]]（`10.3389/fgene.2026.1797093`，protein interaction）
- “This speculation is supported by studies on homologous PHD proteins in soybean: GmPHD2 upregulates eight stress-responsive genes including peroxidases; GmPHD5 binds to promoters of…” — [[daily-42588879-f1]]（`10.3390/plants15152376`，DNA binding/regulation）

### 2.7 表观编辑与工程化改造

**规模** 34 条证据 / 22 篇文献；**构成** descriptive/observational(20)、DNA binding/regulation(6)、genetic perturbation(4)、expression/regulation(2)、protein interaction(2)；**因果层** 12 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Nicotiana tabacum、Arabidopsis thaliana、Oryza sativa，反复出现的实体为BPC1、PRC2、anthocyanin、flavonoid；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[combined-analysis-of-the-metabolome-and-f5]]；2021 [[comparative-transcriptomic-analyses-of-glucosinolate-metabol-f3]]；2021 [[comparative-transcriptomic-analyses-of-glucosinolate-metabol-f5]]）。
- **证据层级的张力**：12 条属于遗传扰动/蛋白互作/DNA 结合，22 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-42231887-f2]]；[[daily-42231887-f3]]；[[daily-42211481-f2]]）。
- **可检验缺口**：表型关联、组学共现在本组缺证据；在补齐这些设计前，BPC1、PRC2、anthocyanin 与“表观编辑与工程化改造”的方向性关系应作为待检验命题（[[combined-analysis-of-the-metabolome-and-f5]]；2021 [[comparative-transcriptomic-analyses-of-glucosinolate-metabol-f3]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 描述性 | 合计 |
|---|---|---|---|---|---|---|
| Nicotiana tabacum | 3 | 1 | 2 | 2 | 7 | 15 |
| Arabidopsis thaliana | 1 | 1 | 4 | 1 | 6 | 13 |
| Oryza sativa | 1 | 0 | 3 | 1 | 7 | 12 |
| Zea mays | 2 | 1 | 3 | 0 | 5 | 11 |
| Malus domestica | 0 | 1 | 2 | 1 | 3 | 7 |

**基因实体（自动标注，前 5）**：BPC1(2)、PRC2(2)、HY5(2)、CcDFR(2)、CcLDOX(2)（标注覆盖 21/34）。

**化合物实体（自动标注，前 5）**：anthocyanin(8)、flavonoid(2)、phenolic(1)、xyloglucan(1)、chlorophyll(1)（标注覆盖 13/34）。

**标注一致性提示**：本组 6 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[daily-42244154-f5]]。

**代表断言（原文摘录，未改写）**

- “We show that SlGRAS9 is highly expressed in tomato fruit and knockout or downregulation of this gene via CRISPR/Cas9 genome editing and RNA interference approaches, respectively, r…” — [[the-slgras9slzhd17-transcriptional-cascade-regulates-chlorop-f2]]（`10.1111/nph.19530`，genetic perturbation）
- “HY5 directly regulates multiple regulatory and structural genes in the anthocyanin biosynthetic pathway Having established that BPC1 represses anthocyanin pathway genes through PRC…” — [[daily-42231887-f3]]（`10.3389/fpls.2026.1826058`，DNA binding/regulation）
- “We further validated CURE student-identified gRNAs with an URA that assessed target gene expression and phenotypic outcomes in stable transgenic lines expressing synthetic transcri…” — [[daily-42293129-f2]]（`10.1093/synbio/ysag007`，genetic perturbation）

## 3. 跨子主题实体枢纽（自动统计）

下列实体在 **≥2 个子主题**中被独立证据提及。它们本身**不构成机制结论**，但说明该实体是本主题多条研究线的交叉点，值得优先核对证据层级。

| 基因 | 命中子主题数 | 证据条数 | 涉及子主题 |
|---|---|---|---|
| BRC1 | 5 | 8 | 染色质重塑与三维构象、组蛋白修饰与染色质状态、表观编辑与工程化改造、表观遗传与发育/逆境可塑性、转录因子与顺式调控元件 |
| HDA9 | 4 | 10 | 染色质重塑与三维构象、组蛋白修饰与染色质状态、表观遗传与发育/逆境可塑性、转录因子与顺式调控元件 |
| WIND1 | 4 | 10 | 染色质重塑与三维构象、组蛋白修饰与染色质状态、表观遗传与发育/逆境可塑性、转录因子与顺式调控元件 |
| PRC2 | 4 | 9 | 组蛋白修饰与染色质状态、表观编辑与工程化改造、表观遗传与发育/逆境可塑性、转录因子与顺式调控元件 |
| GCN5 | 4 | 8 | 染色质重塑与三维构象、组蛋白修饰与染色质状态、表观遗传与发育/逆境可塑性、转录因子与顺式调控元件 |
| HY5 | 4 | 8 | 染色质重塑与三维构象、组蛋白修饰与染色质状态、表观编辑与工程化改造、转录因子与顺式调控元件 |
| BPC1 | 4 | 7 | 染色质重塑与三维构象、组蛋白修饰与染色质状态、表观编辑与工程化改造、转录因子与顺式调控元件 |
| HDA6 | 4 | 7 | DNA 甲基化与去甲基化、染色质重塑与三维构象、组蛋白修饰与染色质状态、表观遗传与发育/逆境可塑性 |
| RPD3 | 4 | 6 | 染色质重塑与三维构象、组蛋白修饰与染色质状态、表观遗传与发育/逆境可塑性、转录因子与顺式调控元件 |
| WD40 | 4 | 4 | 染色质重塑与三维构象、组蛋白修饰与染色质状态、表观遗传与发育/逆境可塑性、转录因子与顺式调控元件 |

| 化合物 | 命中子主题数 | 证据条数 | 涉及子主题 |
|---|---|---|---|
| anthocyanin | 5 | 34 | 染色质重塑与三维构象、组蛋白修饰与染色质状态、表观编辑与工程化改造、表观遗传与发育/逆境可塑性、转录因子与顺式调控元件 |
| auxin | 4 | 8 | 染色质重塑与三维构象、表观遗传与发育/逆境可塑性、转录因子与顺式调控元件、非编码 RNA 与转录沉默 |
| flavonoid | 3 | 6 | 染色质重塑与三维构象、表观编辑与工程化改造、转录因子与顺式调控元件 |
| starch | 3 | 5 | 染色质重塑与三维构象、表观编辑与工程化改造、表观遗传与发育/逆境可塑性 |
| melatonin | 3 | 4 | 染色质重塑与三维构象、表观遗传与发育/逆境可塑性、转录因子与顺式调控元件 |
| chlorophyll | 3 | 3 | 表观编辑与工程化改造、表观遗传与发育/逆境可塑性、非编码 RNA 与转录沉默 |

### 3.1 跨子主题受控叙述

- **交叉实体**：BRC1、HDA9、WIND1、PRC2、GCN5 等实体在 ≥2 个子主题中重复出现；这只能说明多条研究线指向同一候选，不能说明同一机制（[[a-novel-r2r3myb-transcription-factor-famyb5-f1]]；[[a-novel-r2r3myb-transcription-factor-famyb5-f2]]）。
- **层级不均**：因果层证据在子主题间分布不均，最高为“转录因子与顺式调控元件”（101 条），最低为“DNA 甲基化与去甲基化”（4 条）；跨子主题比较结论强度前须先对齐这一差异。
- **共同缺口**：七类证据齐全，瓶颈是同一结论的独立复现与条件分层，而非证据类型。

## 4. 研究设计缺口矩阵（子主题 × 证据类型）

> 单元格为证据条数，`—` 表示该组合在本主题无证据。最后一列之后按行读：一行里若前三列全为 `—`，该子主题**没有任何因果层证据**。

| 子主题 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 |
|---|---|---|---|---|---|---|---|
| DNA 甲基化与去甲基化 | — | 4 | — | 3 | — | — | 19 |
| 组蛋白修饰与染色质状态 | 5 | 22 | 4 | 24 | — | 6 | 51 |
| 染色质重塑与三维构象 | 4 | 29 | 8 | 16 | 4 | 7 | 65 |
| 非编码 RNA 与转录沉默 | 4 | 4 | — | 4 | 1 | — | 38 |
| 转录因子与顺式调控元件 | 5 | 48 | 48 | 12 | 2 | 8 | 96 |
| 表观遗传与发育/逆境可塑性 | 17 | 15 | 6 | 35 | 2 | 9 | 153 |
| 表观编辑与工程化改造 | 4 | 2 | 6 | 2 | — | — | 20 |

所有已有证据的子主题都至少含 1 条因果/直接互作级证据，机制表述具备最低限度的实验托底。

## 5. 可直接引用的因果级证据（自动筛选）

以下 351 条证据的实验设计属于扰动或直接互作，可作为机制论断的一手依据；引用时须核对原文的物种、组织与处理条件。

| 证据页 | DOI | 类型 | 断言（摘录） |
|---|---|---|---|
| [[a-novel-r2r3myb-transcription-factor-famyb5-f5]] | `10.1111/pbi.14024` | protein interaction | The strawberry FaEGL3 and FaLWD1/FaLWD1-like interact with the R2R3-FaMYB5 to form an MYB- bHLH-WD40 complex (MBW), enha… |
| [[a-novel-r2r3myb-transcription-factor-famyb5-f6]] | `10.1111/pbi.14024` | protein interaction | The R2R3- FaMYB5 protein could interact with FaBT2 and was degraded through the ubiquitin/26 S proteasome pathway. |
| [[a-novel-r2r3myb-transcription-factor-famyb5-f7]] | `10.1111/pbi.14024` | genetic perturbation | For example, ectopic overexpression of CsMYB5a in tobacco increased the PA content in flowers and inhibited anthocyanin … |
| [[a-novel-r2r3myb-transcription-factor-famyb5-f8]] | `10.1111/pbi.14024` | genetic perturbation | Overexpression of PgMYB5-like in tobacco leaves only promoted the accumulation of the individual intermediate in the fla… |
| [[a-pear-s1-bzip-transcription-factor-ppbzip44-f6]] | `10.1093/hr/uhad140` | genetic perturbation | Overexpression of PpbZIP44 decreased the TCA cycle intermediate contents (e.g. |
| [[a-pear-s1-bzip-transcription-factor-ppbzip44-f7]] | `10.1093/hr/uhad140` | DNA binding/regulation | PpbZIP44 directly binds to the promoters of PpSDH9, PpADT, PpProDH1, and PpF3H To understand how bZIP44 regulates the ex… |
| [[a-transcriptional-cascade-mediated-by-two-f1]] | `10.1111/jipb.13650` | DNA binding/regulation | The transcription factor SlBBX20 directly binds to the Gbox 2 motif in the PSY1 promoter and regulates lycopene accumula… |
| [[a-transcriptional-cascade-mediated-by-two-f2]] | `10.1111/jipb.13650` | protein interaction | These results suggest that SlAP2c represses lycopene biosynthesis by interacting with the TPL2/4HDA1/3 complex, thus mod… |
| [[a-transcriptional-cascade-mediated-by-two-f5]] | `10.1111/jipb.13650` | protein interaction | The EAR motifcontaining transcription factor MaERF11 was also shown to directly interact with MaHDA1 and repress the exp… |
| [[a-transcriptional-cascade-mediated-by-two-f6]] | `10.1111/jipb.13650` | genetic perturbation | Knockout of SlAP2c in both the “MicroTom” and “Ailsa Craig” backgrounds resulted in greater lycopene accumulation, where… |
| [[a-transcriptional-cascade-mediated-by-two-f7]] | `10.1111/jipb.13650` | DNA binding/regulation | HY5 directly binds to the promoters of PSY1, ZISO, CRTISO, LCYE, and LCYB to regulate carotenoid biosynthesis (Wang et a… |
| [[a-transcriptional-cascade-mediated-by-two-f8]] | `10.1111/jipb.13650` | DNA binding/regulation | In this study, we demonstrated that SlAP2c, a homolog of SlAP2a, is a direct target of SlAP2a and that SlAP2a and SlAP2c… |
| [[alfalfa-cadmium-sc-multiomics-f3]] | `10.1093/hr/uhag117` | genetic perturbation | The results revealed that 356 overexpression of MsMT2A in yeast significantly increased tolerance to Cd stress (Fig. |
| [[antagonistic-madsbox-transcription-factors-seedstick-and-f2]] | `10.1111/jipb.13606` | protein interaction | In summary, these results imply that STK interacts with SEP3 in vivo and in vitro. |
| [[antagonistic-madsbox-transcription-factors-seedstick-and-f4]] | `10.1111/jipb.13606` | protein interaction | Another MADSbox TF of SEPALLATA3 (SEP3) was identified, consistent with the previous result that STK interacts with SEP3… |
| [[antagonistic-madsbox-transcription-factors-seedstick-and-f5]] | `10.1111/jipb.13606` | protein interaction | STK's ability to bind to them was not altered when an empty MBP was added, whereas incubation of STK together with SEP3 … |
| [[b5-iZzyxHmz_WpXAsbrHTBStw-f1]] | `10.1111/pbi.70348` | protein interaction | Collectively, these results demonstrate that GmERFA physically interacts with GmNFYA for possible regulation of seed oil… |
| [[b5-iZzyxHmz_WpXAsbrHTBStw-f3]] | `10.1111/pbi.70348` | genetic perturbation | Knocking out GmERFA and its homologue by genome editing increased seed total fatty acid content, while overexpression of… |
| [[b5-iZzyxHmz_WpXAsbrHTBStw-f4]] | `10.1111/pbi.70348` | protein interaction | GmERFA interacts with GmNFYA to inhibit its transcriptional activation of GmbZIP123 and GmZF392, both of which promotes … |
| [[b5-iZzyxHmz_WpXAsbrHTBStw-f5]] | `10.1111/pbi.70348` | DNA binding/regulation | The GmERFA also directly binds to the promoter regions of GmbZIP123 and GmZF392 and represses their gene expression. |

（另有 331 条未列出，可在 `evidence/` 按 evidence_type 过滤。）

## 6. 证据间的张力与矛盾（自动筛查）

自动筛查发现 2 组“同一基因、方向相反”的表述。这类冲突通常来自物种、组织或处理条件不同，**不宜简单判定一方错误**，而应作为条件分层实验的设计依据。

| 基因 | 冲突类型 | 涉及来源（截断） |
|---|---|---|
| BRC1 | regulation direction dispute | [[ms-10-1038_s41467-026-77029-7]]；[[ms-10-1038_s41467-026-77029-7]]；[[ms-10-1038_s41467-026-77029-7]] |
| TB1 | regulation direction dispute | [[ms-10-1038_s41467-026-77029-7]]；[[ms-10-1038_s41467-026-77029-7]] |

> 筛查规则为“激活/抑制”等对立动词共现，属关键词启发式，可能误报；每条冲突都必须回原文核对实验条件后才能采信。

## 7. 覆盖与代表性缺口

- **760 条证据（54%）未命中任何子主题**：说明子主题词表覆盖不足，这部分证据目前无法进入结构性讨论。
- **证据类型以摘要级断言为主**：本知识库对多数文献仅收录摘要/图表级断言，无法支撑实验条件比较与因果推断；全文覆盖率是当前深度的上限约束。
- **文献元数据不全**：论文页 `year` / `journal` 字段覆盖率极低，因此本页不给出发表年份分布，也无法用年份评估时效性；frontmatter 的 `library_papers` 为历史手写值，与 tags 归一化统计相差数倍，**不可引用**。

## 8. 历史正文说明

本页 2026-11-03 之前的正文为人工/LLM 撰写，未与证据逐条对齐，含不可核的行内断言缺引用、格式残留与跨主题内容混入。该正文已原样归档至 `_review/synthesis_legacy_20261103`，保留供追溯，**不得再作为结论来源**。原“与大豆项目关联”的定性判断保留在 frontmatter 的 `soybean_relevance` 字段，其论证过程同样需重新取证。

## 9. 行内引用密度自检

本页正文 4781 个中文字符，行内证据链接 111 处，密度 **11.6 处/500 字**（目标 ≥1）。链接指向证据页，不直接指向出版社；引用前须沿证据页回到原文核对。
