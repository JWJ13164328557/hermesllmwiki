---
title: "代谢与天然产物 — Synthesis"
created: 2026-06-01
total_evidence: 3218
total_papers: 595
library_papers: 858  # 全库按themes归类该主题文献数
type: synthesis
body_status: rebuilt-2026-11-03
tags: [synthesis, metabolism]


soybean_relevance: ⭐中
legacy_archive: _review/synthesis_legacy_20261103/metabolism-natural-products.md
rebuild_rule: evidence-fields-only; no-cross-evidence-inference
rebuild_version: v3

---
# 代谢与天然产物 知识综合（证据重建版 v3）

<!-- AUTO-EVIDENCE-STRENGTH:START -->

## 证据覆盖与强度（自动统计，可复算）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据条目 | 3218 | 本主题归属的证据对象数 |
| 独立论文 | 595 | 去重后的 PMID/DOI 数 |
| 平均每篇证据数 | 5.41 | <1.0 说明多数论文只贡献 1 条结论 |
| 单条证据论文占比 | 7% | 越高说明"每篇论文一个结论"，系统性弱 |
| 主要物种 | Oryza sativa(748)、Arabidopsis thaliana(642)、Nicotiana tabacum(509)、Solanum lycopersicum(509)、Zea mays(502)、Glycine max(339) | 物种过度集中则外推性受限 |
| 证据类型 | descriptive/observational 2106；expression/regulation 336；protein interaction 268；phenotypic/association 169；genetic perturbation 144；omics/co-occurrence 114 | 表达/关联类居多时，因果结论需打折扣 |

> 归属依据：`themes.py` 标签别名表（高置信）+ 关键词兜底（低置信）。本段由脚本生成，不构成结论；结论性文字须回原文核对。

### 可复核证据索引（前 12 条，按断言长度）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `daily-42410657-f1` | 10.1186/s43897-026-00238-7 | Transgenic plants expressing miR858 target mimics effectively blocked miR858 activity, lea |
| `multiomicsdriven-advances-in-the-understanding-of-f6` | 10.1111/tpj.16545 | Homozygous mutations in single and/or double allele(s) of GmFAD2-1A and GmFAD2-1B in soybe |
| `daily-42204464-f2` | 10.1186/s12870-026-09098-1 | Overexpression of DRO1 significantly enhances root downward growth, thereby improving wate |
| `daily-42967137-f2` | 10.1093/hr/uhag234 | Overexpression of NtMYB1 and NtMYB1 / NtbZIP53 in transgenic narcissus upregulated the exp |
| `daily-42432473-f6` | 10.1186/s12870-026-09489-4 | For instance, overexpression of Glycine max GATA58 in the Arabidopsis gnc ( AtGATA21 ) los |
| `daily-42204672-f5` | 10.1186/s12870-026-09089-2 | 1C), the changes in the scopoletin content of the four overexpression-positive lines were  |
| `daily-42319077-f1` | 10.1093/plcell/koag190 | Overexpression of the GhPsbO protein, driven by a constitutive promoter, significantly enh |
| `the-slgras9slzhd17-transcriptional-cascade-regulates-chlorop-f2` | 10.1111/nph.19530 | We show that SlGRAS9 is highly expressed in tomato fruit and knockout or downregulation of |
| `blue-light-photoreceptor-cryptochrome-1-promotes-f1` | 10.1111/pce.14866 | The WT accumulated much higher anthocyanin under blue light than the other light treatment |
| `daily-42967137-f7` | 10.1093/hr/uhag234 | The tiny-plant phenotype of the oeNtMYB1 narcissus bulb and Arabidopsis partially recovere |
| `integrated-metabolomic-and-transcriptomic-analysis-reveals-f5` | 10.3390/ijms22168751 | In summary, EsMYB90 could strikingly increase the level of flavonoid metabolites via modul |
| `daily-42668836-f1` | 10.7717/peerj.21642 | Reported that overexpression of AhALDH3H1 enhanced saline-alkali tolerance in transgenic s |

### 证据语义分层

| 证据类型 | 条目数 | 可支持的推断强度 |
|---|---:|---|
| genetic perturbation | 144 | 遗传因果（扰动后表型/表达改变） |
| protein interaction | 268 | 物理互作（Co-IP/Y2H/BiFC/pull-down） |
| DNA binding/regulation | 81 | 直接调控（ChIP/EMSA/启动子报告） |
| expression/regulation | 336 | 表达相关（转录组/qPCR，不能单独推因果） |
| phenotypic/association | 169 | 表型关联（GWAS/QTL/自然变异/田间） |
| omics/co-occurrence | 114 | 组学共现（单细胞簇/共表达网络，非调控） |
| descriptive/observational | 2106 | 描述性/背景陈述（未报告可核验的实验设计） |

> 读法：`genetic perturbation` / `protein interaction` / `DNA binding/regulation` 可支持因果或直接调控；`expression/regulation` 与 `omics/co-occurrence` 只能提出假说，不能单独证明调控或因果。

### 遗传扰动类证据（仅高置信规则命中，前 5 条；仍须回原文核实）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `daily-42410657-f1` | 10.1186/s43897-026-00238-7 | Transgenic plants expressing miR858 target mimics effectively blocked miR858 activity, leading to th |
| `multiomicsdriven-advances-in-the-understanding-of-f6` | 10.1111/tpj.16545 | Homozygous mutations in single and/or double allele(s) of GmFAD2-1A and GmFAD2-1B in soybean, which  |
| `daily-42204464-f2` | 10.1186/s12870-026-09098-1 | Overexpression of DRO1 significantly enhances root downward growth, thereby improving water-use effi |
| `daily-42967137-f2` | 10.1093/hr/uhag234 | Overexpression of NtMYB1 and NtMYB1 / NtbZIP53 in transgenic narcissus upregulated the expression of |
| `daily-42432473-f6` | 10.1186/s12870-026-09489-4 | For instance, overexpression of Glycine max GATA58 in the Arabidopsis gnc ( AtGATA21 ) loss-of-funct |

### 正文状态

> frontmatter 标记 `body_status: rebuilt-*` 的页面，其子主题正文由 `rebuild_synthesis_body.py` 按本页证据确定性重建；本自动段是该快照的统计摘要。未标记的页面保留历史正文，机制性表述须逐条回原文核对，不得仅凭本页引用。

<!-- AUTO-EVIDENCE-STRENGTH:END -->

> 本页正文于 2026-11-03 由 `rebuild_synthesis_body.py` 从 **2525 条证据对象 / 485 篇文献**确定性重建：所有陈述均可回溯到下列证据页；英文为原文摘录，未经改写；不含跨证据的推测性归纳。历史人工正文已归档至 `_review/synthesis_legacy_20261103`，不再作为本页结论来源。
>
> 阅读约定：`遗传扰动` / `蛋白互作` / `DNA 结合` 三类证据才支持“因果”或“直接调控”的表述；`表达相关` 与 `组学共现` 只能提出关联性假说。

## 0. 综述提要（受控生成）

本主题当前纳入 **2525 条证据 / 485 篇文献**。规则判定为因果或直接调控的 **442 条（17.5%）**；剔除方法描述、相关性措辞与无基因实体标注的条目后，可用于提要的 **234 条**。可判定程度最高的结论集中在CsMYB5a、PpbZIP44、SlAP2c：For example, ectopic overexpression of CsMYB5a in tobacco increased the PA content in flowers and inhibited anthocyanin accumulation; overex…（[[a-novel-r2r3myb-transcription-factor-famyb5-f7]]）；Overexpression of PpbZIP44 decreased the TCA cycle intermediate contents (e.g.（[[a-pear-s1-bzip-transcription-factor-ppbzip44-f6]]）；Knockout of SlAP2c in both the “MicroTom” and “Ailsa Craig” backgrounds resulted in greater lycopene accumulation, whereas overexpression of…（[[a-transcriptional-cascade-mediated-by-two-f6]]）。研究重心位于“次生代谢物生物合成途径”（453 条证据，占 18%）。证据的物种分布以 Oryza sativa 为首（820 条，32%）。七类证据均有覆盖，主要瓶颈从“类型缺失”转为“同一结论的独立复现不足”。阅读时须区分两类陈述：因果级证据支撑的“已证机制”，以及表达/组学/描述性证据提示的“候选关联”；后者不得改写成调控或因果。

> 提要由脚本按证据类型与实体计数生成，不含跨证据的机制外推；逐条依据见第 2–3 节。

## 1. 主题概览（自动统计）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据对象 | 2525 | 本主题归属的证据条目数 |
| 独立文献（DOI/PMID 去重） | 485 | 去重后的论文数 |
| 平均每篇证据数 | 5.21 | 接近 1.0 说明每篇论文只贡献一条结论，系统性弱 |
| 单条证据论文占比 | 11%（51/485） | 越高说明证据碎片化越严重 |
| 证据类型构成 | descriptive/observational(1719)、protein interaction(262)、expression/regulation(260)、genetic perturbation(111)、omics/co-occurrence(80)、DNA binding/regulation(69)、phenotypic/association(24) | 描述性占多数时机制结论需打折扣 |
| 类型标注置信度 | low(1871)、medium(526)、high(128) | 低置信度标注须回原文核对 |
| 主要物种 | Oryza sativa(820)、Arabidopsis thaliana(720)、Zea mays(526)、Solanum lycopersicum(498)、Nicotiana tabacum(497)、Glycine max(287) | 物种过度集中则外推性受限 |
| 子主题覆盖 | 7/7（证据 <5 条的 0 个） | 覆盖缺口见第 7 节 |
| 未命中任何子主题的证据 | 1563（62%） | 占比高说明子主题词表或证据文本需扩表 |

因果级证据共 **442 条**，占本主题证据的 **17.5%**。这一比例决定本主题哪些结论可以写成机制，哪些只能写成相关性。

物种主导度：**Oryza sativa** 出现在 820 条证据（32%）。分布较分散，单物种主导风险较低，但需注意各物种证据层级是否可比。

## 2. 子主题分解（按证据重建）

> 一条证据可同时命中多个子主题（共 276 条跨组），因此各子主题计数之和大于总证据数。物种×类型交叉表只统计已标注字段，空单元格表示该组合无证据，不等于不存在相应生物学过程。凡“因果层 0 条”的子主题，其代表断言只能读作相关性，不得改写为调控或因果。

### 2.1 次生代谢物生物合成途径

**规模** 453 条证据 / 239 篇文献；**构成** descriptive/observational(303)、protein interaction(45)、expression/regulation(45)、genetic perturbation(19)、omics/co-occurrence(19)、DNA binding/regulation(18)；**因果层** 82 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Nicotiana tabacum、Oryza sativa，反复出现的实体为HY5、GmMYB4、flavonoid、anthocyanin；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[a-novel-r2r3myb-transcription-factor-famyb5-f1]]；[[a-novel-r2r3myb-transcription-factor-famyb5-f8]]；[[a-pear-s1-bzip-transcription-factor-ppbzip44-f1]]）。
- **证据层级的张力**：82 条属于遗传扰动/蛋白互作/DNA 结合，371 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[a-transcriptional-cascade-mediated-by-two-f7]]；[[acbhlh144-transcription-factor-negatively-regulates-phenolic-f4]]；[[artemisinin-scrna-glandular-trichomes-f6]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[a-transcriptional-cascade-mediated-by-two-f7]]；[[acbhlh144-transcription-factor-negatively-regulates-phenolic-f4]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Arabidopsis thaliana | 8 | 23 | 10 | 21 | 0 | 3 | 100 | 165 |
| Nicotiana tabacum | 13 | 8 | 5 | 11 | 0 | 7 | 83 | 127 |
| Oryza sativa | 7 | 14 | 5 | 12 | 1 | 3 | 85 | 127 |
| Solanum lycopersicum | 4 | 13 | 7 | 8 | 2 | 4 | 59 | 97 |
| Zea mays | 5 | 11 | 4 | 9 | 1 | 1 | 48 | 79 |

**基因实体（自动标注，前 5）**：HY5(5)、GmMYB4(5)、PbrARF13(4)、PbrNSC(4)、IbWRKY24(4)（标注覆盖 178/453）。

**化合物实体（自动标注，前 5）**：flavonoid(92)、anthocyanin(49)、phenylpropanoid(25)、auxin(14)、phenolic(13)（标注覆盖 243/453）。

**标注一致性提示**：本组 3 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[daily-42231887-f6]]。

**代表断言（原文摘录，未改写）**

- “It can interact with other secondary metabolic pathways and work together with them to provide resistance to factors such as diseases, pests, cold, drought, UV, and nutrient stress…” — [[integration-of-metabolomics-and-transcriptomics-reveals-f8]]（`10.1093/hr/uhad277`，protein interaction）
- “SlBEL11 cannot bind to the promoters of flavonoid biosynthesis genes directly but binds to the SlMYB111 promoter To ascertain the specific target genes regulated by SlBEL11, we emp…” — [[slbel11-regulates-flavonoid-biosynthesis-thus-finetuning-f5]]（`10.1111/jipb.13627`，DNA binding/regulation）
- “Overexpression of NtMYB1 and NtMYB1 / NtbZIP53 in transgenic narcissus upregulated the expression of upstream genes NtKS1 and NtGA20ox in the GA biosynthesis pathway; however, NtMY…” — [[daily-42967137-f2]]（`10.1093/hr/uhag234`，genetic perturbation）

### 2.2 转录调控与代谢工程

**规模** 263 条证据 / 110 篇文献；**构成** descriptive/observational(121)、protein interaction(77)、DNA binding/regulation(29)、genetic perturbation(15)、expression/regulation(14)、omics/co-occurrence(5)；**因果层** 121 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Nicotiana tabacum、Oryza sativa，反复出现的实体为MYB75、MYB30、anthocyanin、flavonoid；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[a-novel-r2r3myb-transcription-factor-famyb5-f1]]；[[a-novel-r2r3myb-transcription-factor-famyb5-f3]]；[[a-novel-r2r3myb-transcription-factor-famyb5-f4]]）。
- **证据层级的张力**：121 条属于遗传扰动/蛋白互作/DNA 结合，142 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[a-novel-r2r3myb-transcription-factor-famyb5-f5]]；[[a-novel-r2r3myb-transcription-factor-famyb5-f7]]；[[cmnac25-targets-cmmyb6-to-positively-regulate-f5]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[a-novel-r2r3myb-transcription-factor-famyb5-f5]]；[[a-novel-r2r3myb-transcription-factor-famyb5-f7]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Arabidopsis thaliana | 3 | 38 | 13 | 9 | 0 | 2 | 45 | 110 |
| Nicotiana tabacum | 12 | 26 | 9 | 2 | 0 | 2 | 46 | 97 |
| Oryza sativa | 3 | 27 | 10 | 4 | 0 | 2 | 39 | 85 |
| Malus domestica | 5 | 23 | 13 | 2 | 1 | 0 | 29 | 73 |
| Solanum lycopersicum | 1 | 23 | 7 | 3 | 1 | 2 | 22 | 59 |

**基因实体（自动标注，前 5）**：MYB75(7)、MYB30(7)、GmMYB4(6)、MYB46(6)、MYC2(6)（标注覆盖 212/263）。

**化合物实体（自动标注，前 5）**：anthocyanin(52)、flavonoid(26)、lignin(10)、ethylene(7)、auxin(5)（标注覆盖 110/263）。

**标注一致性提示**：本组 3 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[a-novel-r2r3myb-transcription-factor-famyb5-f3]]。

**代表断言（原文摘录，未改写）**

- “KEY WORDS: Arabidopsis thaliana, Cell detachment, Cell wall, NAC transcription factor, Root cap INTRODUCTION The root cap has unique functions that facilitate root growth through t…” — [[ref-dev-142331-f5]]（`10.1242/dev.142331`，protein interaction）
- “An MBW complex formed by the CmMYB6-CmbHLH2 protein complex is crucial for activating anthocyanin accumulation in chrysanthemum, we have known that CmNAC25 directly binds to the pr…” — [[cmnac25-targets-cmmyb6-to-positively-regulate-f1]]（`10.1186/s12915-023-01719-7`，DNA binding/regulation）
- “Mechanistically, the SnRK2 (SNF1-related kinase 2) family plays a pivotal role in transducing ABA signals and these kinases phosphorylate downstream substrates, including ABA-respo…” — [[ms-10-1186_s43897-026-00236-9-f1]]（`10.1186/s43897-026-00236-9`，protein interaction）

### 2.3 代谢物运输与储存

**规模** 202 条证据 / 138 篇文献；**构成** descriptive/observational(124)、genetic perturbation(27)、expression/regulation(20)、protein interaction(16)、omics/co-occurrence(9)、DNA binding/regulation(4)；**因果层** 47 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Nicotiana tabacum、Oryza sativa、Arabidopsis thaliana，反复出现的实体为IbWRKY24、CcMYB17、anthocyanin、flavonoid；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[a-novel-r2r3myb-transcription-factor-famyb5-f2]]；[[a-novel-r2r3myb-transcription-factor-famyb5-f7]]；[[a-novel-r2r3myb-transcription-factor-famyb5-f8]]）。
- **证据层级的张力**：47 条属于遗传扰动/蛋白互作/DNA 结合，155 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[a-novel-r2r3myb-transcription-factor-famyb5-f7]]；[[a-transcriptional-cascade-mediated-by-two-f1]]；[[b4-lBokIY101sor8t2t3d1CRQ-f6]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[a-novel-r2r3myb-transcription-factor-famyb5-f7]]；[[a-transcriptional-cascade-mediated-by-two-f1]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Nicotiana tabacum | 17 | 7 | 4 | 4 | 0 | 3 | 28 | 63 |
| Oryza sativa | 5 | 6 | 0 | 7 | 0 | 0 | 39 | 57 |
| Arabidopsis thaliana | 6 | 7 | 1 | 6 | 0 | 3 | 32 | 55 |
| Solanum lycopersicum | 11 | 3 | 1 | 3 | 2 | 0 | 24 | 44 |
| Zea mays | 5 | 5 | 0 | 5 | 0 | 0 | 26 | 41 |

**基因实体（自动标注，前 5）**：IbWRKY24(4)、CcMYB17(3)、GmERF109(3)、LhWRKY44(3)、SlBEL11(3)（标注覆盖 98/202）。

**化合物实体（自动标注，前 5）**：anthocyanin(23)、flavonoid(19)、starch(9)、chlorophyll(8)、sucrose(7)（标注覆盖 92/202）。

**代表断言（原文摘录，未改写）**

- “We show that SlGRAS9 is highly expressed in tomato fruit and knockout or downregulation of this gene via CRISPR/Cas9 genome editing and RNA interference approaches, respectively, r…” — [[the-slgras9slzhd17-transcriptional-cascade-regulates-chlorop-f2]]（`10.1111/nph.19530`，genetic perturbation）
- “The WT accumulated much higher anthocyanin under blue light than the other light treatments, while the cry1 mutants abolished the anthocyanin accumulation under blue light (Figure …” — [[blue-light-photoreceptor-cryptochrome-1-promotes-f1]]（`10.1111/pce.14866`，genetic perturbation）
- “Activated SnRK2s phosphorylate downstream transcription factors, including ABF/AREB (ABA-responsive element binding factors) thereby promoting the transcription of ABA-responsive g…” — [[ms-10-3389_fpls-2026-1903199-f3]]（`10.3389/fpls.2026.1903199`，protein interaction）

### 2.4 品质形成与营养成分

**规模** 248 条证据 / 121 篇文献；**构成** descriptive/observational(156)、protein interaction(31)、expression/regulation(19)、genetic perturbation(18)、DNA binding/regulation(11)、omics/co-occurrence(9)；**因果层** 60 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Malus domestica、Nicotiana tabacum，反复出现的实体为OsESV1、OsLESV、anthocyanin、starch；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[a-novel-r2r3myb-transcription-factor-famyb5-f1]]；[[a-novel-r2r3myb-transcription-factor-famyb5-f2]]；[[a-novel-r2r3myb-transcription-factor-famyb5-f3]]）。
- **证据层级的张力**：60 条属于遗传扰动/蛋白互作/DNA 结合，188 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[a-novel-r2r3myb-transcription-factor-famyb5-f7]]；[[auxin-inhibits-lignin-and-cellulose-biosynthesis-f7]]；[[daily-42231887-f5]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[a-novel-r2r3myb-transcription-factor-famyb5-f7]]；[[auxin-inhibits-lignin-and-cellulose-biosynthesis-f7]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Oryza sativa | 1 | 13 | 2 | 8 | 0 | 1 | 41 | 66 |
| Malus domestica | 7 | 12 | 6 | 3 | 0 | 1 | 37 | 66 |
| Nicotiana tabacum | 11 | 8 | 5 | 4 | 0 | 1 | 36 | 65 |
| Zea mays | 5 | 11 | 4 | 4 | 0 | 1 | 34 | 59 |
| Arabidopsis thaliana | 6 | 13 | 7 | 3 | 0 | 2 | 24 | 55 |

**基因实体（自动标注，前 5）**：OsESV1(8)、OsLESV(8)、MYB75(4)、BPC1(4)、HY5(4)（标注覆盖 109/248）。

**化合物实体（自动标注，前 5）**：anthocyanin(95)、starch(32)、flavonoid(12)、chlorophyll(9)、sucrose(8)（标注覆盖 146/248）。

**标注一致性提示**：本组 4 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[a-novel-r2r3myb-transcription-factor-famyb5-f3]]。

**代表断言（原文摘录，未改写）**

- “Found that the reason for white appearance of ‘Jinba’ at the blooming stage was that the R3 MYB transcription factor CmMYB#7, which can interact with CmbHLH2, disrupted the MBW pro…” — [[cmnac25-targets-cmmyb6-to-positively-regulate-f2]]（`10.1186/s12915-023-01719-7`，protein interaction）
- “A conserved regulatory framework involves the MYB–bHLH–WD40 (MBW) complex, in which R2R3-MYB and bHLH transcription factors interact with WD40 proteins to activate (or repress) ant…” — [[daily-42299342-f2]]（`10.3389/fgene.2026.1797093`，protein interaction）
- “Specifically, MdNAC1 enhances anthocyanin production by interacting with the basic leucine zipper (bZIP) family member MdbZIP23 to form the MdNAC1–MdbZIP23 complex that significant…” — [[the-aba-induced-nac-transcription-factor-mdnac1-f7]]（`10.1093/hr/uhad049`，protein interaction）

### 2.5 酶学与催化机制

**规模** 98 条证据 / 74 篇文献；**构成** descriptive/observational(68)、expression/regulation(11)、protein interaction(11)、omics/co-occurrence(3)、genetic perturbation(3)、DNA binding/regulation(2)；**因果层** 16 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Oryza sativa、Solanum lycopersicum，反复出现的实体为MdbZIP44、OsESV1、starch、sucrose；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[analysis-of-lncrna43234-associated-cerna-network-reveals-f2]]；[[artemisinin-scrna-glandular-trichomes-f6]]；[[b4-B6ORjNkH1VSkcVpnv9C7xQ-f3]]）。
- **证据层级的张力**：16 条属于遗传扰动/蛋白互作/DNA 结合，82 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[b5-kf00Og92ayHkmDBpso75bw-f8]]；[[cmnac25-targets-cmmyb6-to-positively-regulate-f6]]；[[artemisinin-scrna-glandular-trichomes-f6]]）。
- **可检验缺口**：表型关联在本组缺证据；在补齐这些设计前，MdbZIP44、OsESV1、starch 与“酶学与催化机制”的方向性关系应作为待检验命题（[[analysis-of-lncrna43234-associated-cerna-network-reveals-f2]]；[[artemisinin-scrna-glandular-trichomes-f6]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|
| Arabidopsis thaliana | 0 | 3 | 1 | 4 | 1 | 18 | 27 |
| Oryza sativa | 0 | 4 | 1 | 2 | 2 | 15 | 24 |
| Solanum lycopersicum | 2 | 2 | 1 | 1 | 0 | 12 | 18 |
| Zea mays | 0 | 4 | 1 | 2 | 0 | 10 | 17 |
| Glycine max | 0 | 1 | 0 | 2 | 0 | 12 | 15 |

**基因实体（自动标注，前 5）**：MdbZIP44(2)、OsESV1(2)、OsLESV(2)、CUT1(1)、LTPG1(1)（标注覆盖 28/98）。

**化合物实体（自动标注，前 5）**：starch(6)、sucrose(4)、chlorophyll(3)、anthocyanin(2)、phenylpropanoid(2)（标注覆盖 27/98）。

**代表断言（原文摘录，未改写）**

- “This could be attributed to the following reasons: the active components in SBO compromise the integrity of bacterial cell membranes, leading to the leakage of intracellular conten…” — [[daily-42500044-f5]]（`10.1016/j.fochx.2026.104224`，protein interaction）
- “Activated ethylene signaling can also reduce levels of bioactive GAs by inhibiting GA biosynthesis enzymes such as GA20ox (Achard et al., 2007), and the ethylene-regulated transcri…” — [[ms-10-3389_fpls-2026-1905836-f3]]（`10.3389/fpls.2026.1905836`，protein interaction）
- “Specifically, AtNAP, a well-characterized NAC transcription factor, can directly bind to the promoter of AAO3 (ALDEHYDE OXIDASE 3), a key enzyme in ABA biosynthesis, thereby enhanc…” — [[ms-10-1186_s43897-026-00236-9-f5]]（`10.1186/s43897-026-00236-9`，DNA binding/regulation）

### 2.6 多组学解析代谢网络

**规模** 51 条证据 / 45 篇文献；**构成** omics/co-occurrence(38)、descriptive/observational(11)、protein interaction(1)、DNA binding/regulation(1)；**因果层** 2 条（可支撑有限机制表述）。

> 本组仅 2 条因果级证据，机制表述只在该证据覆盖的物种与条件下成立，不可外推到其余 49 条。

**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Zea mays、Nicotiana tabacum，反复出现的实体为AtAAP6、OpAVT1、flavonoid、anthocyanin；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[b4-B6ORjNkH1VSkcVpnv9C7xQ-f5]]；[[daily-42135064-f5]]；[[daily-42135625-f3]]）。
- **证据层级的张力**：2 条属于遗传扰动/蛋白互作/DNA 结合，49 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[ethylene-responsive-vvierf003-modulates-glycosylated-monoter-f4]]；[[b4-B6ORjNkH1VSkcVpnv9C7xQ-f5]]）。
- **可检验缺口**：遗传扰动、表达相关、表型关联在本组缺证据；在补齐这些设计前，AtAAP6、OpAVT1、flavonoid 与“多组学解析代谢网络”的方向性关系应作为待检验命题（[[b4-B6ORjNkH1VSkcVpnv9C7xQ-f5]]；[[daily-42135064-f5]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 蛋白互作 | DNA 结合 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|
| Oryza sativa | 0 | 0 | 11 | 1 | 12 |
| Zea mays | 1 | 1 | 9 | 1 | 12 |
| Nicotiana tabacum | 0 | 0 | 7 | 4 | 11 |
| Arabidopsis thaliana | 1 | 1 | 5 | 3 | 10 |
| Triticum aestivum | 0 | 0 | 9 | 1 | 10 |

**基因实体（自动标注，前 5）**：AtAAP6(1)、OpAVT1(1)、SlNOR(1)、HTN188(1)、PC1(1)（标注覆盖 7/51）。

**化合物实体（自动标注，前 5）**：flavonoid(4)、anthocyanin(2)、salicylic acid(1)、glucose(1)、auxin(1)（标注覆盖 10/51）。

**标注一致性提示**：本组 1 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[ms-10-3389_fpls-2026-1827862-f5]]。

**代表断言（原文摘录，未改写）**

- “These DEG-DEP pairs were not randomly downregulated but showed tight co-expression patterns, and PPI network analysis revealed that several of these photosynthesis-related DEPs (e.…” — [[daily-42274512-f4]]（`10.3390/biology15110861`，protein interaction）
- “Result VviERF003 and VviGT14 exhibit co-expression patterns Our prior research indicated that VviERF003 binds to the promoter of VviGT14 under DNA pull-down [27].” — [[ethylene-responsive-vvierf003-modulates-glycosylated-monoter-f4]]（`10.1093/hr/uhae065`，DNA binding/regulation）
- “Based on the analysis of the relationships of targeting and coexpression, we found that NAC (evm.model.group1.695) could potentially target 4CLs and CCoAOMT, that HD-Zip (evm.model…” — [[transcriptomic-proteomic-and-metabolic-profiles-of-f5]]（`10.3389/fpls.2021.704262`，omics/co-occurrence）

### 2.7 逆境代谢重编程

**规模** 9 条证据 / 8 篇文献；**构成** descriptive/observational(6)、expression/regulation(2)、protein interaction(1)；**因果层** 1 条（可支撑有限机制表述）。

> 本组仅 1 条因果级证据，机制表述只在该证据覆盖的物种与条件下成立，不可外推到其余 8 条。

**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Malus domestica、Nicotiana tabacum，反复出现的实体为MeJA、OsLAC11、phenolic、phenylpropanoid；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-42433895-f3]]；[[daily-42483518-f3]]；[[ms-10-1007_s11084-026-09761-5-f3]]）。
- **证据层级的张力**：1 条属于遗传扰动/蛋白互作/DNA 结合，8 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（；[[ms-10-1007_s11084-026-09761-5-f8]]）。
- **可检验缺口**：遗传扰动、DNA 结合、表型关联、组学共现在本组缺证据；在补齐这些设计前，MeJA、OsLAC11、phenolic 与“逆境代谢重编程”的方向性关系应作为待检验命题（[[daily-42433895-f3]]；[[daily-42483518-f3]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 蛋白互作 | 表达相关 | 描述性 | 合计 |
|---|---|---|---|---|
| Oryza sativa | 1 | 2 | 1 | 4 |
| Malus domestica | 0 | 0 | 2 | 2 |
| Nicotiana tabacum | 0 | 0 | 2 | 2 |
| Fragaria × ananassa | 0 | 0 | 2 | 2 |
| Glycine max | 1 | 1 | 0 | 2 |

**基因实体（自动标注，前 5）**：MeJA(1)、OsLAC11(1)（标注覆盖 2/9）。

**化合物实体（自动标注，前 5）**：phenolic(1)、phenylpropanoid(1)（标注覆盖 2/9）。

**代表断言（原文摘录，未改写）**

- “Microbial elicitors molecules secreted by bacteria and fungi bind to plant cell receptors and trigger signaling pathways that induce synthesis of terpenoids, pheno lic acids, and f…” — [[ms-10-1007_s11084-026-09761-5-f3]]（`10.1007/s11084-026-09761-5`，protein interaction）
- “The OsLAC11 plays a critical role in lignification, helps maintain cell wall structure and mechanical strength, supports plant responses to environmental stressors and defense mech…” — [[daily-42483518-f3]]（`10.3389/fpls.2026.1809531`，descriptive/observational）
- “Collectively, these studies establish exogenous MeJA as a potent elicitor of betalain synthesis, although its mode of action varies across species and tissues, and the upstream and…” — [[daily-42433895-f3]]（`10.3389/fpls.2026.1865544`，descriptive/observational）

## 3. 跨子主题实体枢纽（自动统计）

下列实体在 **≥2 个子主题**中被独立证据提及。它们本身**不构成机制结论**，但说明该实体是本主题多条研究线的交叉点，值得优先核对证据层级。

| 基因 | 命中子主题数 | 证据条数 | 涉及子主题 |
|---|---|---|---|
| CmNAC25 | 5 | 7 | 代谢物运输与储存、品质形成与营养成分、次生代谢物生物合成途径、转录调控与代谢工程、酶学与催化机制 |
| IbWRKY24 | 4 | 13 | 代谢物运输与储存、多组学解析代谢网络、次生代谢物生物合成途径、转录调控与代谢工程 |
| LhWRKY44 | 4 | 13 | 代谢物运输与储存、品质形成与营养成分、次生代谢物生物合成途径、转录调控与代谢工程 |
| RcMYB1 | 4 | 12 | 代谢物运输与储存、品质形成与营养成分、次生代谢物生物合成途径、转录调控与代谢工程 |
| EsMYB90 | 4 | 9 | 代谢物运输与储存、品质形成与营养成分、次生代谢物生物合成途径、转录调控与代谢工程 |
| CmbHLH2 | 4 | 8 | 代谢物运输与储存、品质形成与营养成分、次生代谢物生物合成途径、转录调控与代谢工程 |
| VvBBX44 | 4 | 8 | 代谢物运输与储存、品质形成与营养成分、次生代谢物生物合成途径、转录调控与代谢工程 |
| CmMYB6 | 4 | 7 | 代谢物运输与储存、品质形成与营养成分、次生代谢物生物合成途径、转录调控与代谢工程 |
| MdMYB10 | 4 | 7 | 代谢物运输与储存、品质形成与营养成分、次生代谢物生物合成途径、转录调控与代谢工程 |
| VvSBP8 | 4 | 7 | 代谢物运输与储存、品质形成与营养成分、次生代谢物生物合成途径、转录调控与代谢工程 |

| 化合物 | 命中子主题数 | 证据条数 | 涉及子主题 |
|---|---|---|---|
| anthocyanin | 6 | 223 | 代谢物运输与储存、品质形成与营养成分、多组学解析代谢网络、次生代谢物生物合成途径、转录调控与代谢工程、酶学与催化机制 |
| flavonoid | 6 | 155 | 代谢物运输与储存、品质形成与营养成分、多组学解析代谢网络、次生代谢物生物合成途径、转录调控与代谢工程、酶学与催化机制 |
| phenylpropanoid | 6 | 35 | 代谢物运输与储存、品质形成与营养成分、次生代谢物生物合成途径、转录调控与代谢工程、逆境代谢重编程、酶学与催化机制 |
| phenolic | 6 | 27 | 代谢物运输与储存、品质形成与营养成分、次生代谢物生物合成途径、转录调控与代谢工程、逆境代谢重编程、酶学与催化机制 |
| lignin | 5 | 31 | 代谢物运输与储存、品质形成与营养成分、多组学解析代谢网络、次生代谢物生物合成途径、转录调控与代谢工程 |
| auxin | 5 | 28 | 代谢物运输与储存、多组学解析代谢网络、次生代谢物生物合成途径、转录调控与代谢工程、酶学与催化机制 |

### 3.1 跨子主题受控叙述

- **交叉实体**：CmNAC25、IbWRKY24、LhWRKY44、RcMYB1、EsMYB90 等实体在 ≥2 个子主题中重复出现；这只能说明多条研究线指向同一候选，不能说明同一机制（[[a-comprehensive-analysis-of-transcriptome-and-f1]]；[[a-novel-r2r3myb-transcription-factor-famyb5-f1]]）。
- **层级不均**：因果层证据在子主题间分布不均，最高为“转录调控与代谢工程”（121 条），最低为“逆境代谢重编程”（1 条）；跨子主题比较结论强度前须先对齐这一差异。
- **共同缺口**：七类证据齐全，瓶颈是同一结论的独立复现与条件分层，而非证据类型。

## 4. 研究设计缺口矩阵（子主题 × 证据类型）

> 单元格为证据条数，`—` 表示该组合在本主题无证据。最后一列之后按行读：一行里若前三列全为 `—`，该子主题**没有任何因果层证据**。

| 子主题 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 |
|---|---|---|---|---|---|---|---|
| 次生代谢物生物合成途径 | 19 | 45 | 18 | 45 | 4 | 19 | 303 |
| 转录调控与代谢工程 | 15 | 77 | 29 | 14 | 2 | 5 | 121 |
| 代谢物运输与储存 | 27 | 16 | 4 | 20 | 2 | 9 | 124 |
| 品质形成与营养成分 | 18 | 31 | 11 | 19 | 4 | 9 | 156 |
| 酶学与催化机制 | 3 | 11 | 2 | 11 | — | 3 | 68 |
| 多组学解析代谢网络 | — | 1 | 1 | — | — | 38 | 11 |
| 逆境代谢重编程 | — | 1 | — | 2 | — | — | 6 |

所有已有证据的子主题都至少含 1 条因果/直接互作级证据，机制表述具备最低限度的实验托底。

## 5. 可直接引用的因果级证据（自动筛选）

以下 442 条证据的实验设计属于扰动或直接互作，可作为机制论断的一手依据；引用时须核对原文的物种、组织与处理条件。

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
| [[acbhlh144-transcription-factor-negatively-regulates-phenolic-f1]] | `10.1093/hr/uhad185` | protein interaction | Based on the different binding modes, bHLHs can be divided into three categories: some bind to the E-box/G-box (CANNTG),… |
| [[acbhlh144-transcription-factor-negatively-regulates-phenolic-f3]] | `10.1093/hr/uhad185` | DNA binding/regulation | CES (a bHLH) binds to the promoter of GA2ox7 to enhance its expression in response to brassinosteroid [28]. |
| [[acbhlh144-transcription-factor-negatively-regulates-phenolic-f4]] | `10.1093/hr/uhad185` | genetic perturbation | Overexpression of AcbHLH144 decreased phenolic accumulation in pineapple To check whether AcbHLH144 TF functions in regu… |
| [[acbhlh144-transcription-factor-negatively-regulates-phenolic-f5]] | `10.1093/hr/uhad185` | DNA binding/regulation | AcbHLH144 directly regulates expression of Ac4CL5 To further characterize the role of AcbHLH144 in regulating biosynthes… |
| [[analysis-of-lncrna43234-associated-cerna-network-reveals-f3]] | `10.1021/acs.jafc.3c00993` | genetic perturbation | Overexpression of lncRNA43234 increased the content of crude protein in seeds, decreased the content of oleic acid, and … |
| [[analysis-of-lncrna43234-associated-cerna-network-reveals-f6]] | `10.1021/acs.jafc.3c00993` | protein interaction | The miRNAs predicted to interact with these targeted protein-coding genes showed upregulated expression levels. |
| [[analysis-of-lncrna43234-associated-cerna-network-reveals-f7]] | `10.1021/acs.jafc.3c00993` | protein interaction | The lncRNAs MSTRG.33053 and targeted protein-coding genes showed upregulated expression levels, and the miRNAs that were… |
| [[auxin-inhibits-lignin-and-cellulose-biosynthesis-f4]] | `10.1111/pbi.14046` | protein interaction | PbrNSC was shown to bind to an auxin response factor, PbrARF13. |

（另有 422 条未列出，可在 `evidence/` 按 evidence_type 过滤。）

## 6. 证据间的张力与矛盾（自动筛查）

自动筛查发现 3 组“同一基因、方向相反”的表述。这类冲突通常来自物种、组织或处理条件不同，**不宜简单判定一方错误**，而应作为条件分层实验的设计依据。

| 基因 | 冲突类型 | 涉及来源（截断） |
|---|---|---|
| BZR1 | regulation direction dispute | [[a-transcriptional-cascade-mediated-by-two]]；[[daily-42514610]]；[[daily-42665660]] |
| HY5 | regulation direction dispute | [[a-transcriptional-cascade-mediated-by-two]]；[[daily-42231887]]；[[daily-42231887]] |
| BIN2 | regulation direction dispute | [[daily-42665660]]；[[daily-42665660]]；[[daily-42665660]] |

> 筛查规则为“激活/抑制”等对立动词共现，属关键词启发式，可能误报；每条冲突都必须回原文核对实验条件后才能采信。

## 7. 覆盖与代表性缺口

- **单篇证据物种 5 个**（Carthamus tinctorius、Ficus carica **方法**: metabolomics (LC-MS/GC-MS)、qRT-PCR validation **来源**: DOI:10.1016/j.foodchem.2023.137788 **来源类型**: PDF全文 (64 整合转录组、挥发性和非挥发性代谢物图谱揭示了香椿的香气形成特征.p、metabolomics (LC-MS/GC-MS)、alfalfa…）：跨物种外推缺乏支撑。
- **1563 条证据（62%）未命中任何子主题**：说明子主题词表覆盖不足，这部分证据目前无法进入结构性讨论。
- **证据类型以摘要级断言为主**：本知识库对多数文献仅收录摘要/图表级断言，无法支撑实验条件比较与因果推断；全文覆盖率是当前深度的上限约束。
- **文献元数据不全**：论文页 `year` / `journal` 字段覆盖率极低，因此本页不给出发表年份分布，也无法用年份评估时效性；frontmatter 的 `library_papers` 为历史手写值，与 tags 归一化统计相差数倍，**不可引用**。

## 8. 历史正文说明

本页 2026-11-03 之前的正文为人工/LLM 撰写，未与证据逐条对齐，含不可核的行内断言缺引用、格式残留与跨主题内容混入。该正文已原样归档至 `_review/synthesis_legacy_20261103`，保留供追溯，**不得再作为结论来源**。原“与大豆项目关联”的定性判断保留在 frontmatter 的 `soybean_relevance` 字段，其论证过程同样需重新取证。

## 9. 行内引用密度自检

本页正文 4879 个中文字符，行内证据链接 112 处，密度 **11.5 处/500 字**（目标 ≥1）。链接指向证据页，不直接指向出版社；引用前须沿证据页回到原文核对。
