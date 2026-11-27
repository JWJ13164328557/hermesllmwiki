---
title: "代谢与天然产物 — Synthesis"
created: 2026-06-01
total_evidence: 2796
total_papers: 594
library_papers: 858  # 全库按themes归类该主题文献数
type: synthesis
body_status: rebuilt-2026-11-26
tags: [synthesis, metabolism]


soybean_relevance: ⭐中
legacy_archive: _review/synthesis_legacy_20261126/metabolism-natural-products.md
rebuild_rule: evidence-fields-only; no-cross-evidence-inference
rebuild_version: v3

---
# 代谢与天然产物 知识综合（证据重建版 v3）

<!-- AUTO-EVIDENCE-STRENGTH:START -->

## 证据覆盖与强度（自动统计，可复算）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据条目 | 2796 | 本主题归属的证据对象数 |
| 独立论文 | 594 | 去重后的 PMID/DOI 数 |
| 平均每篇证据数 | 4.71 | <1.0 说明多数论文只贡献 1 条结论 |
| 单条证据论文占比 | 10% | 越高说明"每篇论文一个结论"，系统性弱 |
| 主要物种 | Oryza sativa(626)、Arabidopsis thaliana(557)、Nicotiana tabacum(461)、Solanum lycopersicum(448)、Zea mays(429)、Glycine max(289) | 物种过度集中则外推性受限 |
| 证据类型 | descriptive/observational 1871；protein interaction 240；expression/regulation 198；phenotypic/association 163；genetic perturbation 141；omics/co-occurrence 104 | 表达/关联类居多时，因果结论需打折扣 |

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
| genetic perturbation | 141 | 遗传因果（扰动后表型/表达改变） |
| protein interaction | 240 | 物理互作（Co-IP/Y2H/BiFC/pull-down） |
| DNA binding/regulation | 79 | 直接调控（ChIP/EMSA/启动子报告） |
| expression/regulation | 198 | 表达相关（转录组/qPCR，不能单独推因果） |
| phenotypic/association | 163 | 表型关联（GWAS/QTL/自然变异/田间） |
| omics/co-occurrence | 104 | 组学共现（单细胞簇/共表达网络，非调控） |
| descriptive/observational | 1871 | 描述性/背景陈述（未报告可核验的实验设计） |

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

> 本页正文于 2026-11-26 由 `rebuild_synthesis_body.py` 从 **2789 条证据对象 / 593 篇文献**确定性重建：所有陈述均可回溯到下列证据页；英文为原文摘录，未经改写；不含跨证据的推测性归纳。历史人工正文已归档至 `_review/synthesis_legacy_20261126`，不再作为本页结论来源。
>
> 阅读约定：`遗传扰动` / `蛋白互作` / `DNA 结合` 三类证据才支持“因果”或“直接调控”的表述；`表达相关` 与 `组学共现` 只能提出关联性假说。

## 0. 综述提要（受控生成）

本主题当前纳入 **2789 条证据 / 593 篇文献**。规则判定为因果或直接调控的 **459 条（16.5%）**；剔除方法描述、相关性措辞与无基因实体标注的条目后，可用于提要的 **241 条**。可判定程度最高的结论集中在CsMYB5a、PpbZIP44、SlAP2c：For example, ectopic overexpression of CsMYB5a in tobacco increased the PA content in flowers and inhibited anthocyanin accumulation; overex…（[[a-novel-r2r3myb-transcription-factor-famyb5-f7]]）；Overexpression of PpbZIP44 decreased the TCA cycle intermediate contents (e.g.（[[a-pear-s1-bzip-transcription-factor-ppbzip44-f6]]）；Knockout of SlAP2c in both the “MicroTom” and “Ailsa Craig” backgrounds resulted in greater lycopene accumulation, whereas overexpression of…（[[a-transcriptional-cascade-mediated-by-two-f6]]）。研究重心位于“次生代谢物生物合成途径”（460 条证据，占 16%）。证据的物种分布以 Oryza sativa 为首（630 条，23%）。七类证据均有覆盖，主要瓶颈从“类型缺失”转为“同一结论的独立复现不足”。阅读时须区分两类陈述：因果级证据支撑的“已证机制”，以及表达/组学/描述性证据提示的“候选关联”；后者不得改写成调控或因果。

> 提要由脚本按证据类型与实体计数生成，不含跨证据的机制外推；逐条依据见第 2–3 节。

## 1. 主题概览（自动统计）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据对象 | 2789 | 本主题归属的证据条目数 |
| 独立文献（DOI/PMID 去重） | 593 | 去重后的论文数 |
| 平均每篇证据数 | 4.70 | 接近 1.0 说明每篇论文只贡献一条结论，系统性弱 |
| 单条证据论文占比 | 10%（62/593） | 越高说明证据碎片化越严重 |
| 证据类型构成 | descriptive/observational(1868)、protein interaction(239)、expression/regulation(196)、phenotypic/association(163)、genetic perturbation(141)、omics/co-occurrence(103)、DNA binding/regulation(79) | 描述性占多数时机制结论需打折扣 |
| 类型标注置信度 | low(1922)、medium(683)、high(156)、未标(28) | 低置信度标注须回原文核对 |
| 主要物种 | Oryza sativa(630)、Arabidopsis thaliana(562)、Nicotiana tabacum(465)、Solanum lycopersicum(451)、Zea mays(433)、Glycine max(290) | 物种过度集中则外推性受限 |
| 子主题覆盖 | 7/7（证据 <5 条的 0 个） | 覆盖缺口见第 7 节 |
| 未命中任何子主题的证据 | 1699（61%） | 占比高说明子主题词表或证据文本需扩表 |

因果级证据共 **459 条**，占本主题证据的 **16.5%**。这一比例决定本主题哪些结论可以写成机制，哪些只能写成相关性。

物种主导度：**Oryza sativa** 出现在 630 条证据（23%）。分布较分散，单物种主导风险较低，但需注意各物种证据层级是否可比。

## 2. 子主题分解（按证据重建）

> 一条证据可同时命中多个子主题（共 304 条跨组），因此各子主题计数之和大于总证据数。物种×类型交叉表只统计已标注字段，空单元格表示该组合无证据，不等于不存在相应生物学过程。凡“因果层 0 条”的子主题，其代表断言只能读作相关性，不得改写为调控或因果。

### 2.1 次生代谢物生物合成途径

**规模** 460 条证据 / 256 篇文献；**构成** descriptive/observational(289)、expression/regulation(38)、protein interaction(37)、genetic perturbation(27)、phenotypic/association(25)、omics/co-occurrence(23)；**因果层** 85 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Nicotiana tabacum、Oryza sativa，反复出现的实体为HY5、PbrARF13、flavonoid、anthocyanin；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[a-novel-r2r3myb-transcription-factor-famyb5-f1]]；[[a-novel-r2r3myb-transcription-factor-famyb5-f8]]；[[a-pear-s1-bzip-transcription-factor-ppbzip44-f1]]）。
- **证据层级的张力**：85 条属于遗传扰动/蛋白互作/DNA 结合，375 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[a-transcriptional-cascade-mediated-by-two-f7]]；[[acbhlh144-transcription-factor-negatively-regulates-phenolic-f4]]；[[artemisinin-scrna-glandular-trichomes-f6]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[a-transcriptional-cascade-mediated-by-two-f7]]；[[acbhlh144-transcription-factor-negatively-regulates-phenolic-f4]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Arabidopsis thaliana | 11 | 16 | 8 | 15 | 6 | 2 | 85 | 143 |
| Nicotiana tabacum | 12 | 10 | 6 | 7 | 3 | 6 | 73 | 117 |
| Oryza sativa | 8 | 11 | 3 | 8 | 4 | 4 | 59 | 97 |
| Solanum lycopersicum | 5 | 11 | 6 | 5 | 7 | 4 | 46 | 84 |
| Malus domestica | 2 | 5 | 6 | 7 | 1 | 3 | 41 | 65 |

**基因实体（自动标注，前 5）**：HY5(5)、PbrARF13(4)、PbrNSC(4)、IbWRKY24(4)、OsESV1(4)（标注覆盖 174/460）。

**化合物实体（自动标注，前 5）**：flavonoid(95)、anthocyanin(44)、phenylpropanoid(23)、lignin(15)、terpenoid(14)（标注覆盖 257/460）。

**标注一致性提示**：本组 2 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[integrated-analysis-of-the-metabolome-and-f5]]。

**代表断言（原文摘录，未改写）**

- “Transgenic plants expressing miR858 target mimics effectively blocked miR858 activity, leading to the upregulation of its target gene expression, including genes encoding flavonoid…” — [[daily-42410657-f1]]（`10.1186/s43897-026-00238-7`，genetic perturbation）
- “SlBEL11 cannot bind to the promoters of flavonoid biosynthesis genes directly but binds to the SlMYB111 promoter To ascertain the specific target genes regulated by SlBEL11, we emp…” — [[slbel11-regulates-flavonoid-biosynthesis-thus-finetuning-f5]]（`10.1111/jipb.13627`，DNA binding/regulation）
- “Overexpression of NtMYB1 and NtMYB1 / NtbZIP53 in transgenic narcissus upregulated the expression of upstream genes NtKS1 and NtGA20ox in the GA biosynthesis pathway; however, NtMY…” — [[daily-42967137-f2]]（`10.1093/hr/uhag234`，genetic perturbation）

### 2.2 转录调控与代谢工程

**规模** 270 条证据 / 116 篇文献；**构成** descriptive/observational(115)、protein interaction(65)、DNA binding/regulation(34)、genetic perturbation(23)、expression/regulation(21)、omics/co-occurrence(6)；**因果层** 122 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Nicotiana tabacum、Arabidopsis thaliana、Malus domestica，反复出现的实体为MYB75、MYB30、anthocyanin、flavonoid；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[a-novel-r2r3myb-transcription-factor-famyb5-f1]]；[[a-novel-r2r3myb-transcription-factor-famyb5-f3]]；[[a-novel-r2r3myb-transcription-factor-famyb5-f4]]）。
- **证据层级的张力**：122 条属于遗传扰动/蛋白互作/DNA 结合，148 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[a-novel-r2r3myb-transcription-factor-famyb5-f5]]；[[a-novel-r2r3myb-transcription-factor-famyb5-f7]]；[[b5-hcZHAUCBBvNTdU5-NTHtmg-f5]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[a-novel-r2r3myb-transcription-factor-famyb5-f5]]；[[a-novel-r2r3myb-transcription-factor-famyb5-f7]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Nicotiana tabacum | 14 | 25 | 9 | 3 | 2 | 2 | 39 | 94 |
| Arabidopsis thaliana | 4 | 28 | 11 | 9 | 1 | 3 | 37 | 93 |
| Malus domestica | 4 | 17 | 14 | 2 | 3 | 1 | 27 | 68 |
| Oryza sativa | 3 | 21 | 6 | 5 | 1 | 2 | 29 | 67 |
| Solanum lycopersicum | 1 | 16 | 8 | 2 | 2 | 2 | 19 | 50 |

**基因实体（自动标注，前 5）**：MYB75(7)、MYB30(7)、VvMYBA1(6)、FaMYB5(5)、OfWRKY48(5)（标注覆盖 213/270）。

**化合物实体（自动标注，前 5）**：anthocyanin(51)、flavonoid(24)、lignin(8)、ethylene(7)、carotenoid(6)（标注覆盖 110/270）。

**标注一致性提示**：本组 3 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[a-novel-r2r3myb-transcription-factor-famyb5-f3]]。

**代表断言（原文摘录，未改写）**

- “This domain enables bZIP transcription factors to specifically recognize and bind to particular DNA sequences, thereby regulating the expression of downstream genes., With the incr…” — [[daily-40523045-f3]]（`10.1080/21645698.2025.2510715`，protein interaction）
- “KEY WORDS: Arabidopsis thaliana, Cell detachment, Cell wall, NAC transcription factor, Root cap INTRODUCTION The root cap has unique functions that facilitate root growth through t…” — [[ref-dev-142331-f5]]（`10.1242/dev.142331`，protein interaction）
- “An MBW complex formed by the CmMYB6-CmbHLH2 protein complex is crucial for activating anthocyanin accumulation in chrysanthemum, we have known that CmNAC25 directly binds to the pr…” — [[cmnac25-targets-cmmyb6-to-positively-regulate-f1]]（`10.1186/s12915-023-01719-7`，DNA binding/regulation）

### 2.3 代谢物运输与储存

**规模** 243 条证据 / 165 篇文献；**构成** descriptive/observational(140)、genetic perturbation(33)、phenotypic/association(20)、expression/regulation(20)、protein interaction(13)、omics/co-occurrence(11)；**因果层** 52 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Nicotiana tabacum、Oryza sativa、Arabidopsis thaliana，反复出现的实体为IbWRKY24、OpAVT1、anthocyanin、flavonoid；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[a-novel-r2r3myb-transcription-factor-famyb5-f2]]；[[a-novel-r2r3myb-transcription-factor-famyb5-f7]]；[[a-novel-r2r3myb-transcription-factor-famyb5-f8]]）。
- **证据层级的张力**：52 条属于遗传扰动/蛋白互作/DNA 结合，191 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[a-novel-r2r3myb-transcription-factor-famyb5-f7]]；[[a-transcriptional-cascade-mediated-by-two-f1]]；[[daily-42204669-f1]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[a-novel-r2r3myb-transcription-factor-famyb5-f7]]；[[a-transcriptional-cascade-mediated-by-two-f1]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Nicotiana tabacum | 16 | 5 | 5 | 3 | 2 | 3 | 21 | 55 |
| Oryza sativa | 5 | 3 | 0 | 9 | 3 | 1 | 33 | 54 |
| Arabidopsis thaliana | 9 | 5 | 1 | 2 | 2 | 2 | 28 | 49 |
| Solanum lycopersicum | 12 | 1 | 1 | 4 | 6 | 0 | 25 | 49 |
| Zea mays | 6 | 3 | 0 | 6 | 2 | 1 | 25 | 43 |

**基因实体（自动标注，前 5）**：IbWRKY24(4)、OpAVT1(4)、LhWRKY44(3)、SlBEL11(3)、EfCGT1(2)（标注覆盖 103/243）。

**化合物实体（自动标注，前 5）**：anthocyanin(31)、flavonoid(20)、chlorophyll(14)、starch(13)、phenolic(10)（标注覆盖 118/243）。

**代表断言（原文摘录，未改写）**

- “For instance, overexpression of Glycine max GATA58 in the Arabidopsis gnc ( AtGATA21 ) loss-of-function mutant rescued the chlorophyll-deficient phenotype, while overexpression in …” — [[daily-42432473-f6]]（`10.1186/s12870-026-09489-4`，genetic perturbation）
- “We show that SlGRAS9 is highly expressed in tomato fruit and knockout or downregulation of this gene via CRISPR/Cas9 genome editing and RNA interference approaches, respectively, r…” — [[the-slgras9slzhd17-transcriptional-cascade-regulates-chlorop-f2]]（`10.1111/nph.19530`，genetic perturbation）
- “The WT accumulated much higher anthocyanin under blue light than the other light treatments, while the cry1 mutants abolished the anthocyanin accumulation under blue light (Figure …” — [[blue-light-photoreceptor-cryptochrome-1-promotes-f1]]（`10.1111/pce.14866`，genetic perturbation）

### 2.4 品质形成与营养成分

**规模** 309 条证据 / 161 篇文献；**构成** descriptive/observational(199)、protein interaction(30)、genetic perturbation(20)、phenotypic/association(17)、expression/regulation(16)、omics/co-occurrence(14)；**因果层** 63 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Solanum lycopersicum、Zea mays，反复出现的实体为OsESV1、OsLESV、anthocyanin、starch；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[a-novel-r2r3myb-transcription-factor-famyb5-f1]]；[[a-novel-r2r3myb-transcription-factor-famyb5-f2]]；[[a-novel-r2r3myb-transcription-factor-famyb5-f3]]）。
- **证据层级的张力**：63 条属于遗传扰动/蛋白互作/DNA 结合，246 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[a-novel-r2r3myb-transcription-factor-famyb5-f7]]；[[auxin-inhibits-lignin-and-cellulose-biosynthesis-f7]]；[[daily-41922966-f2]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[a-novel-r2r3myb-transcription-factor-famyb5-f7]]；[[auxin-inhibits-lignin-and-cellulose-biosynthesis-f7]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Oryza sativa | 2 | 13 | 2 | 6 | 2 | 2 | 45 | 72 |
| Solanum lycopersicum | 6 | 4 | 0 | 5 | 8 | 2 | 37 | 62 |
| Zea mays | 6 | 9 | 4 | 5 | 2 | 1 | 29 | 56 |
| Nicotiana tabacum | 9 | 8 | 7 | 2 | 1 | 1 | 25 | 53 |
| Arabidopsis thaliana | 7 | 10 | 7 | 1 | 3 | 2 | 23 | 53 |

**基因实体（自动标注，前 5）**：OsESV1(8)、OsLESV(8)、HY5(5)、MYB75(4)、MdbZIP44(4)（标注覆盖 105/309）。

**化合物实体（自动标注，前 5）**：anthocyanin(104)、starch(41)、flavonoid(13)、chlorophyll(10)、sucrose(7)（标注覆盖 169/309）。

**标注一致性提示**：本组 3 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[a-novel-r2r3myb-transcription-factor-famyb5-f3]]。

**代表断言（原文摘录，未改写）**

- “It has bee demonstrated that TiO 2 nanoparticles improved the thermal stability of the composite films not only because the nanoparticles were thermally stable and could endure hig…” — [[daily-42502873-f2]]（`10.1016/j.fochx.2026.104204`，protein interaction）
- “Found that the reason for white appearance of ‘Jinba’ at the blooming stage was that the R3 MYB transcription factor CmMYB#7, which can interact with CmbHLH2, disrupted the MBW pro…” — [[cmnac25-targets-cmmyb6-to-positively-regulate-f2]]（`10.1186/s12915-023-01719-7`，protein interaction）
- “A conserved regulatory framework involves the MYB–bHLH–WD40 (MBW) complex, in which R2R3-MYB and bHLH transcription factors interact with WD40 proteins to activate (or repress) ant…” — [[daily-42299342-f2]]（`10.3389/fgene.2026.1797093`，protein interaction）

### 2.5 酶学与催化机制

**规模** 109 条证据 / 83 篇文献；**构成** descriptive/observational(75)、expression/regulation(10)、protein interaction(9)、genetic perturbation(5)、phenotypic/association(5)、DNA binding/regulation(3)；**因果层** 17 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Glycine max、Arabidopsis thaliana，反复出现的实体为CYP93C、MdbZIP44、starch、chlorophyll；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[analysis-of-lncrna43234-associated-cerna-network-reveals-f2]]；[[artemisinin-scrna-glandular-trichomes-f6]]；[[b4-B6ORjNkH1VSkcVpnv9C7xQ-f3]]）。
- **证据层级的张力**：17 条属于遗传扰动/蛋白互作/DNA 结合，92 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[cmnac25-targets-cmmyb6-to-positively-regulate-f6]]；[[daily-42243644-f6]]；[[artemisinin-scrna-glandular-trichomes-f6]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[cmnac25-targets-cmmyb6-to-positively-regulate-f6]]；[[daily-42243644-f6]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Oryza sativa | 1 | 3 | 1 | 1 | 0 | 1 | 11 | 18 |
| Glycine max | 0 | 0 | 1 | 1 | 1 | 0 | 15 | 18 |
| Arabidopsis thaliana | 0 | 1 | 1 | 1 | 0 | 1 | 14 | 18 |
| Solanum lycopersicum | 2 | 0 | 1 | 2 | 1 | 0 | 10 | 16 |
| Zea mays | 0 | 3 | 1 | 1 | 0 | 0 | 8 | 13 |

**基因实体（自动标注，前 5）**：CYP93C(2)、MdbZIP44(2)、OsESV1(2)、OsLESV(2)、CmDFR(1)（标注覆盖 30/109）。

**化合物实体（自动标注，前 5）**：starch(7)、chlorophyll(4)、sucrose(3)、anthocyanin(2)、phenolic(2)（标注覆盖 28/109）。

**代表断言（原文摘录，未改写）**

- “Activated ethylene signaling can also reduce levels of bioactive GAs by inhibiting GA biosynthesis enzymes such as GA20ox (Achard et al., 2007), and the ethylene-regulated transcri…” — [[ms-10-3389_fpls-2026-1905836-f3]]（`10.3389/fpls.2026.1905836`，protein interaction）
- “Specifically, AtNAP, a well-characterized NAC transcription factor, can directly bind to the promoter of AAO3 (ALDEHYDE OXIDASE 3), a key enzyme in ABA biosynthesis, thereby enhanc…” — [[ms-10-1186_s43897-026-00236-9-f5]]（`10.1186/s43897-026-00236-9`，DNA binding/regulation）
- “These compounds mainly belong to the classes of flavonols, phenolic acids, and isoflavonoids, all known for their high antioxidant activity and ability to interact with biological …” — [[ms-10-1007_s11101-026-10261-7-f1]]（`10.1007/s11101-026-10261-7`，protein interaction）

### 2.6 多组学解析代谢网络

**规模** 90 条证据 / 73 篇文献；**构成** omics/co-occurrence(65)、descriptive/observational(15)、genetic perturbation(4)、expression/regulation(2)、protein interaction(2)、DNA binding/regulation(1)；**因果层** 7 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Nicotiana tabacum、Oryza sativa、Triticum aestivum，反复出现的实体为AtAAP6、OpAVT1、anthocyanin、flavonoid；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[b4-B6ORjNkH1VSkcVpnv9C7xQ-f5]]；[[daily-42135064-f5]]；[[daily-42135625-f3]]）。
- **证据层级的张力**：7 条属于遗传扰动/蛋白互作/DNA 结合，83 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-42410657-f2]]；[[daily-42481951-f6]]；[[b4-B6ORjNkH1VSkcVpnv9C7xQ-f5]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[daily-42410657-f2]]；[[daily-42481951-f6]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Nicotiana tabacum | 0 | 0 | 0 | 1 | 0 | 10 | 7 | 18 |
| Oryza sativa | 0 | 0 | 0 | 0 | 0 | 15 | 1 | 16 |
| Triticum aestivum | 0 | 0 | 0 | 0 | 0 | 12 | 1 | 13 |
| Arabidopsis thaliana | 0 | 2 | 1 | 0 | 0 | 6 | 3 | 12 |
| Glycine max | 1 | 0 | 0 | 1 | 0 | 8 | 2 | 12 |

**基因实体（自动标注，前 5）**：AtAAP6(2)、OpAVT1(2)、SlNOR(1)、SeNPs(1)、OsBBX13(1)（标注覆盖 15/90）。

**化合物实体（自动标注，前 5）**：anthocyanin(4)、flavonoid(4)、carotenoid(2)、alkaloid(2)、cutin(1)（标注覆盖 20/90）。

**标注一致性提示**：本组 1 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[ms-10-3389_fpls-2026-1827862-f5]]。

**代表断言（原文摘录，未改写）**

- “Reported that overexpression of AhALDH3H1 enhanced saline-alkali tolerance in transgenic soybean by scavenging toxic aldehydes and MDA, and integrated transcriptomic and metabolomi…” — [[daily-42668836-f1]]（`10.7717/peerj.21642`，genetic perturbation）
- “These DEG-DEP pairs were not randomly downregulated but showed tight co-expression patterns, and PPI network analysis revealed that several of these photosynthesis-related DEPs (e.…” — [[daily-42274512-f4]]（`10.3390/biology15110861`，protein interaction）
- “In conclusion, integrating metabolomics, mutant phenotyping, and enzymology allowed the identification and functional characterization of a complete DMS catabolic pathway in a terr…” — [[daily-42286912-f6]]（`10.1093/ismejo/wrag149`，genetic perturbation）

### 2.7 逆境代谢重编程

**规模** 5 条证据 / 5 篇文献；**构成** descriptive/observational(2)、omics/co-occurrence(1)、phenotypic/association(1)、protein interaction(1)；**因果层** 1 条（可支撑有限机制表述）。

> 本组仅 1 条因果级证据，机制表述只在该证据覆盖的物种与条件下成立，不可外推到其余 4 条。

**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Glycine max、Oryza sativa、Solanum lycopersicum，反复出现的实体为SeNPs、phenylpropanoid；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-42216058-f6]]；[[daily-42452267-f8]]；[[ms-10-1007_s11084-026-09761-5-f3]]）。
- **证据层级的张力**：1 条属于遗传扰动/蛋白互作/DNA 结合，4 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（；[[daily-42216058-f6]]）。
- **可检验缺口**：遗传扰动、DNA 结合、表达相关在本组缺证据；在补齐这些设计前，SeNPs、phenylpropanoid 与“逆境代谢重编程”的方向性关系应作为待检验命题（[[daily-42216058-f6]]；[[daily-42452267-f8]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 蛋白互作 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|
| Glycine max | 1 | 0 | 1 | 0 | 2 |
| Oryza sativa | 1 | 1 | 0 | 0 | 2 |
| Solanum lycopersicum | 1 | 0 | 0 | 0 | 1 |
| Fragaria × ananassa | 0 | 0 | 0 | 1 | 1 |
| Daucus carota | 0 | 0 | 0 | 1 | 1 |

**基因实体（自动标注，前 5）**：SeNPs(1)（标注覆盖 1/5）。

**化合物实体（自动标注，前 5）**：phenylpropanoid(1)（标注覆盖 1/5）。

**代表断言（原文摘录，未改写）**

- “Microbial elicitors molecules secreted by bacteria and fungi bind to plant cell receptors and trigger signaling pathways that induce synthesis of terpenoids, pheno lic acids, and f…” — [[ms-10-1007_s11084-026-09761-5-f3]]（`10.1007/s11084-026-09761-5`，protein interaction）
- “Application of Nanoparticles in Callus Culture The use of callus cells, i.e., undifferentiated totipotent cells, cultivated on various nutrient media supplemented with growth regul…” — [[daily-42452267-f8]]（`10.3390/plants15132071`，phenotypic/association）
- “In conclusion, these findings uncover a potential explanation on the elicitor strategies to induce an increased accumulation of specific phenylpropanoid in P.” — [[ms-10-25081_jp-2026-v18-9950-f4]]（`10.25081/jp.2026.v18.9950`，descriptive/observational）

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
| CsMYB1 | 4 | 7 | 代谢物运输与储存、品质形成与营养成分、多组学解析代谢网络、转录调控与代谢工程 |
| VvSBP8 | 4 | 7 | 代谢物运输与储存、品质形成与营养成分、次生代谢物生物合成途径、转录调控与代谢工程 |

| 化合物 | 命中子主题数 | 证据条数 | 涉及子主题 |
|---|---|---|---|
| anthocyanin | 6 | 236 | 代谢物运输与储存、品质形成与营养成分、多组学解析代谢网络、次生代谢物生物合成途径、转录调控与代谢工程、酶学与催化机制 |
| flavonoid | 6 | 158 | 代谢物运输与储存、品质形成与营养成分、多组学解析代谢网络、次生代谢物生物合成途径、转录调控与代谢工程、酶学与催化机制 |
| phenolic | 6 | 35 | 代谢物运输与储存、品质形成与营养成分、多组学解析代谢网络、次生代谢物生物合成途径、转录调控与代谢工程、酶学与催化机制 |
| phenylpropanoid | 6 | 33 | 代谢物运输与储存、品质形成与营养成分、次生代谢物生物合成途径、转录调控与代谢工程、逆境代谢重编程、酶学与催化机制 |
| carotenoid | 6 | 29 | 代谢物运输与储存、品质形成与营养成分、多组学解析代谢网络、次生代谢物生物合成途径、转录调控与代谢工程、酶学与催化机制 |
| sucrose | 6 | 24 | 代谢物运输与储存、品质形成与营养成分、多组学解析代谢网络、次生代谢物生物合成途径、转录调控与代谢工程、酶学与催化机制 |

### 3.1 跨子主题受控叙述

- **交叉实体**：CmNAC25、IbWRKY24、LhWRKY44、RcMYB1、EsMYB90 等实体在 ≥2 个子主题中重复出现；这只能说明多条研究线指向同一候选，不能说明同一机制（[[a-comprehensive-analysis-of-transcriptome-and-f1]]；[[a-novel-r2r3myb-transcription-factor-famyb5-f1]]）。
- **层级不均**：因果层证据在子主题间分布不均，最高为“转录调控与代谢工程”（122 条），最低为“逆境代谢重编程”（1 条）；跨子主题比较结论强度前须先对齐这一差异。
- **共同缺口**：七类证据齐全，瓶颈是同一结论的独立复现与条件分层，而非证据类型。

## 4. 研究设计缺口矩阵（子主题 × 证据类型）

> 单元格为证据条数，`—` 表示该组合在本主题无证据。最后一列之后按行读：一行里若前三列全为 `—`，该子主题**没有任何因果层证据**。

| 子主题 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 |
|---|---|---|---|---|---|---|---|
| 次生代谢物生物合成途径 | 27 | 37 | 21 | 38 | 25 | 23 | 289 |
| 转录调控与代谢工程 | 23 | 65 | 34 | 21 | 6 | 6 | 115 |
| 代谢物运输与储存 | 33 | 13 | 6 | 20 | 20 | 11 | 140 |
| 品质形成与营养成分 | 20 | 30 | 13 | 16 | 17 | 14 | 199 |
| 酶学与催化机制 | 5 | 9 | 3 | 10 | 5 | 2 | 75 |
| 多组学解析代谢网络 | 4 | 2 | 1 | 2 | 1 | 65 | 15 |
| 逆境代谢重编程 | — | 1 | — | — | 1 | 1 | 2 |

所有已有证据的子主题都至少含 1 条因果/直接互作级证据，机制表述具备最低限度的实验托底。

## 5. 可直接引用的因果级证据（自动筛选）

以下 459 条证据的实验设计属于扰动或直接互作，可作为机制论断的一手依据；引用时须核对原文的物种、组织与处理条件。

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
| [[a-transcriptional-cascade-mediated-by-two-f4]] | `10.1111/jipb.13650` | DNA binding/regulation | A recent study showed that the AP2aDWARFBZR1 module positively regulates lycopene biosynthesis (Sang et al., 2022); howe… |
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

（另有 439 条未列出，可在 `evidence/` 按 evidence_type 过滤。）

## 6. 证据间的张力与矛盾（自动筛查）

自动筛查发现 2 组“同一基因、方向相反”的表述。这类冲突通常来自物种、组织或处理条件不同，**不宜简单判定一方错误**，而应作为条件分层实验的设计依据。

| 基因 | 冲突类型 | 涉及来源（截断） |
|---|---|---|
| BZR1 | regulation direction dispute | [[a-transcriptional-cascade-mediated-by-two]]；[[daily-42665660]]；[[daily-42665660]] |
| BIN2 | regulation direction dispute | [[daily-42665660]]；[[daily-42665660]]；[[daily-42665660]] |

> 筛查规则为“激活/抑制”等对立动词共现，属关键词启发式，可能误报；每条冲突都必须回原文核对实验条件后才能采信。

## 7. 覆盖与代表性缺口

- **1699 条证据（61%）未命中任何子主题**：说明子主题词表覆盖不足，这部分证据目前无法进入结构性讨论。
- **证据类型以摘要级断言为主**：本知识库对多数文献仅收录摘要/图表级断言，无法支撑实验条件比较与因果推断；全文覆盖率是当前深度的上限约束。
- **文献元数据不全**：论文页 `year` / `journal` 字段覆盖率极低，因此本页不给出发表年份分布，也无法用年份评估时效性；frontmatter 的 `library_papers` 为历史手写值，与 tags 归一化统计相差数倍，**不可引用**。

## 8. 历史正文说明

本页 2026-11-03 之前的正文为人工/LLM 撰写，未与证据逐条对齐，含不可核的行内断言缺引用、格式残留与跨主题内容混入。该正文已原样归档至 `_review/synthesis_legacy_20261126`，保留供追溯，**不得再作为结论来源**。原“与大豆项目关联”的定性判断保留在 frontmatter 的 `soybean_relevance` 字段，其论证过程同样需重新取证。

## 9. 行内引用密度自检

本页正文 4840 个中文字符，行内证据链接 110 处，密度 **11.4 处/500 字**（目标 ≥1）。链接指向证据页，不直接指向出版社；引用前须沿证据页回到原文核对。
