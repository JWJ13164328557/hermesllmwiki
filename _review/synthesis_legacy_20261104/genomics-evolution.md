---

title: "基因组与进化 — Synthesis"
created: 2026-06-01
total_evidence: 606
total_papers: 298
library_papers: 520  # 全库按themes归类该主题文献数
type: synthesis
body_status: rebuilt-2026-11-03
tags: [synthesis, genomics, evolution, genome-assembly, comparative-genomics, GWAS, polyploidization, domestication]


soybean_relevance: ⭐中高
legacy_archive: _review/synthesis_legacy_20261103/genomics-evolution.md
rebuild_rule: evidence-fields-only; no-cross-evidence-inference
rebuild_version: v3

---
# 基因组学与演化 知识综合（证据重建版 v3）

<!-- AUTO-EVIDENCE-STRENGTH:START -->

## 证据覆盖与强度（自动统计，可复算）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据条目 | 606 | 本主题归属的证据对象数 |
| 独立论文 | 298 | 去重后的 PMID/DOI 数 |
| 平均每篇证据数 | 2.03 | <1.0 说明多数论文只贡献 1 条结论 |
| 单条证据论文占比 | 46% | 越高说明"每篇论文一个结论"，系统性弱 |
| 主要物种 | Oryza sativa(189)、Zea mays(113)、Arabidopsis thaliana(107)、Triticum aestivum(97)、Glycine max(72)、Solanum lycopersicum(52) | 物种过度集中则外推性受限 |
| 证据类型 | descriptive/observational 449；phenotypic/association 92；expression/regulation 35；omics/co-occurrence 15；protein interaction 8；genetic perturbation 5 | 表达/关联类居多时，因果结论需打折扣 |

> 归属依据：`themes.py` 标签别名表（高置信）+ 关键词兜底（低置信）。本段由脚本生成，不构成结论；结论性文字须回原文核对。

### 可复核证据索引（前 12 条，按断言长度）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `multiomicsdriven-advances-in-the-understanding-of-f6` | 10.1111/tpj.16545 | Homozygous mutations in single and/or double allele(s) of GmFAD2-1A and GmFAD2-1B in soybe |
| `daily-42137983-f1` | 10.1093/nar/gkag476 | Using custom-made antibodies specific to the rice H2A.X variant, we show that it repressed |
| `ref-science-1086391-f3` | 10.1126/science.1086391 | Although there were no effects of G C content on T-DNA integration sites observed at the g |
| `daily-42429570-f5` | 10.1128/spectrum.00381-26 | The inability to recover escape mutants further suggests that systems like DRT11 may targe |
| `daily-42713468-f7` | 10.3389/fpls.2026.1902159 | Compared with conventional CRISPR/Cas9-mediated editing, PE substantially reduces the risk |
| `daily-40523045-f3` | 10.1080/21645698.2025.2510715 | This domain enables bZIP transcription factors to specifically recognize and bind to parti |
| `daily-42670212-f3` | 10.1111/pbi.70748 | In contrast to the hQTL Integrated_GY_hQTL121 on chromosome 4A which interacts with many r |
| `ms-10-1371_journal-pgen-1012287-f7` | 10.1371/journal.pgen.1012287 | At the start of this circuit, the transcription factor proteins Circadian Locomotor Output |
| `daily-42413033-f7` | 10.1093/plphys/kiag473 | TFs are DNA-binding proteins that can selectively bind to cis-regulatory elements (CREs) i |
| `daily-42283811-f1` | 10.1007/s00248-026-02803-5 | ICE dynamics in these bacteria often interact with other components of the mobilome, inclu |
| `daily-42514528-f2` | 10.3390/plants15142160 | It binds to the expression product of VirA, activating other Vir genes, resulting in the c |
| `daily-42243690-f4` | 10.1186/s12870-026-09148-8 | The phylogenetic patterns observed in PQS frequency raise the question of what biological  |

### 证据语义分层

| 证据类型 | 条目数 | 可支持的推断强度 |
|---|---:|---|
| genetic perturbation | 5 | 遗传因果（扰动后表型/表达改变） |
| protein interaction | 8 | 物理互作（Co-IP/Y2H/BiFC/pull-down） |
| DNA binding/regulation | 2 | 直接调控（ChIP/EMSA/启动子报告） |
| expression/regulation | 35 | 表达相关（转录组/qPCR，不能单独推因果） |
| phenotypic/association | 92 | 表型关联（GWAS/QTL/自然变异/田间） |
| omics/co-occurrence | 15 | 组学共现（单细胞簇/共表达网络，非调控） |
| descriptive/observational | 449 | 描述性/背景陈述（未报告可核验的实验设计） |

> 读法：`genetic perturbation` / `protein interaction` / `DNA binding/regulation` 可支持因果或直接调控；`expression/regulation` 与 `omics/co-occurrence` 只能提出假说，不能单独证明调控或因果。

### 遗传扰动类证据（仅高置信规则命中，前 5 条；仍须回原文核实）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `multiomicsdriven-advances-in-the-understanding-of-f6` | 10.1111/tpj.16545 | Homozygous mutations in single and/or double allele(s) of GmFAD2-1A and GmFAD2-1B in soybean, which  |
| `daily-42137983-f1` | 10.1093/nar/gkag476 | Using custom-made antibodies specific to the rice H2A.X variant, we show that it repressed the depos |
| `ref-science-1086391-f3` | 10.1126/science.1086391 | Although there were no effects of G C content on T-DNA integration sites observed at the genome scal |
| `daily-42429570-f5` | 10.1128/spectrum.00381-26 | The inability to recover escape mutants further suggests that systems like DRT11 may target infectio |
| `daily-42713468-f7` | 10.3389/fpls.2026.1902159 | Compared with conventional CRISPR/Cas9-mediated editing, PE substantially reduces the risk of large  |

### 正文状态

> frontmatter 标记 `body_status: rebuilt-*` 的页面，其子主题正文由 `rebuild_synthesis_body.py` 按本页证据确定性重建；本自动段是该快照的统计摘要。未标记的页面保留历史正文，机制性表述须逐条回原文核对，不得仅凭本页引用。

<!-- AUTO-EVIDENCE-STRENGTH:END -->

> 本页正文于 2026-11-03 由 `rebuild_synthesis_body.py` 从 **290 条证据对象 / 148 篇文献**确定性重建：所有陈述均可回溯到下列证据页；英文为原文摘录，未经改写；不含跨证据的推测性归纳。历史人工正文已归档至 `_review/synthesis_legacy_20261103`，不再作为本页结论来源。
>
> 阅读约定：`遗传扰动` / `蛋白互作` / `DNA 结合` 三类证据才支持“因果”或“直接调控”的表述；`表达相关` 与 `组学共现` 只能提出关联性假说。

## 0. 综述提要（受控生成）

本主题当前纳入 **290 条证据 / 148 篇文献**。规则判定为因果或直接调控的 **7 条（2.4%）**；剔除方法描述、相关性措辞与无基因实体标注的条目后，可用于提要的 **1 条**。可判定程度最高的结论集中在GmFAD2：Homozygous mutations in single and/or double allele(s) of GmFAD2-1A and GmFAD2-1B in soybean, which are created by transcription activator-l…（[[multiomicsdriven-advances-in-the-understanding-of-f6]]）。研究重心位于“转座子与基因组可塑性”（221 条证据，占 76%）。证据的物种分布以 Oryza sativa 为首（112 条，39%）。目前完全缺失的证据类型是DNA 结合；凡涉及这些推断的表述，本页只能写成待检验命题。阅读时须区分两类陈述：因果级证据支撑的“已证机制”，以及表达/组学/描述性证据提示的“候选关联”；后者不得改写成调控或因果。

> 提要由脚本按证据类型与实体计数生成，不含跨证据的机制外推；逐条依据见第 2–3 节。

## 1. 主题概览（自动统计）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据对象 | 290 | 本主题归属的证据条目数 |
| 独立文献（DOI/PMID 去重） | 148 | 去重后的论文数 |
| 平均每篇证据数 | 1.96 | 接近 1.0 说明每篇论文只贡献一条结论，系统性弱 |
| 单条证据论文占比 | 51%（75/148） | 越高说明证据碎片化越严重 |
| 证据类型构成 | descriptive/observational(226)、phenotypic/association(35)、expression/regulation(15)、omics/co-occurrence(7)、protein interaction(5)、genetic perturbation(2) | 描述性占多数时机制结论需打折扣 |
| 类型标注置信度 | low(237)、medium(50)、high(3) | 低置信度标注须回原文核对 |
| 主要物种 | Oryza sativa(112)、Arabidopsis thaliana(90)、Zea mays(75)、Triticum aestivum(51)、Glycine max(38)、Solanum lycopersicum(36) | 物种过度集中则外推性受限 |
| 子主题覆盖 | 7/7（证据 <5 条的 1 个） | 覆盖缺口见第 7 节 |
| 未命中任何子主题的证据 | 37（13%） | 占比高说明子主题词表或证据文本需扩表 |

因果级证据共 **7 条**，占本主题证据的 **2.4%**。这一比例决定本主题哪些结论可以写成机制，哪些只能写成相关性。

物种主导度：**Oryza sativa** 出现在 112 条证据（39%）。分布较分散，单物种主导风险较低，但需注意各物种证据层级是否可比。

## 2. 子主题分解（按证据重建）

> 一条证据可同时命中多个子主题（共 115 条跨组），因此各子主题计数之和大于总证据数。物种×类型交叉表只统计已标注字段，空单元格表示该组合无证据，不等于不存在相应生物学过程。凡“因果层 0 条”的子主题，其代表断言只能读作相关性，不得改写为调控或因果。

### 2.1 基因组组装与注释

**规模** 19 条证据 / 15 篇文献；**构成** descriptive/observational(11)、phenotypic/association(6)、expression/regulation(1)、omics/co-occurrence(1)；**因果层** 0 条（仅关联/描述，不得写因果）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Arabidopsis thaliana、Triticum aestivum，反复出现的实体为rhAmpSeq；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-42413033-f1]]；[[daily-42488439-f2]]；[[daily-42557532-f6]]）。
- **证据层级的张力**：本组 0 条因果级证据，全部 19 条为表达、组学或描述性；任何“调控/导致”表述都必须降级为待检验命题（[[daily-42413033-f1]]；[[daily-42488439-f2]]）。
- **可检验缺口**：遗传扰动、DNA 结合、蛋白互作在本组缺证据；在补齐这些设计前，rhAmpSeq 与“基因组组装与注释”的方向性关系应作为待检验命题（[[daily-42413033-f1]]；[[daily-42488439-f2]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|
| Oryza sativa | 0 | 3 | 0 | 5 | 8 |
| Arabidopsis thaliana | 1 | 0 | 1 | 5 | 7 |
| Triticum aestivum | 1 | 1 | 0 | 3 | 5 |
| Solanum lycopersicum | 0 | 1 | 0 | 2 | 3 |
| Catharanthus roseus | 0 | 0 | 1 | 2 | 3 |

**基因实体（自动标注，前 5）**：rhAmpSeq(2)（标注覆盖 2/19）。

**代表断言（原文摘录，未改写）**

- “ARTICLE IN PRESS ARTICLE IN PRESS A telomere-to-telomere genome reveals arachidonic acid as a key regulator of hepatic lipid metabolism during hibernation Abstract Elucidating the …” — [[ms-10-1038_s42003-026-10625-x-f6]]（`10.1038/s42003-026-10625-x`，descriptive/observational）
- “Our findings confirm the advantages of SMRT, which facilitated the construction a rich transcript data-set for research on the development of ginkgo seeds, enriching the annotation…” — [[full-length-sequencing-of-ginkgo-biloba-l-f1]]（`10.1016/j.indcrop.2021.113714`，descriptive/observational）
- “Our results show that sequence-to-expression models are a viable tool for gaining biological insight and generating novel hypotheses in any species of interest, even complex polypl…” — [[daily-42413033-f1]]（`10.1093/plphys/kiag473`，expression/regulation）

### 2.2 比较基因组与共线性

**规模** 4 条证据 / 4 篇文献；**构成** descriptive/observational(3)、expression/regulation(1)；**因果层** 0 条（仅关联/描述，不得写因果）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Oryza sativa、Zea mays；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-42262904-f6]]；[[ms-10-1038_s41467-026-76979-2-f1]]；[[ref-msb-2010-53-f6]]）。
- **证据层级的张力**：本组 0 条因果级证据，全部 4 条为表达、组学或描述性；任何“调控/导致”表述都必须降级为待检验命题（[[daily-42262904-f6]]；[[ms-10-1038_s41467-026-76979-2-f1]]）。
- **可检验缺口**：遗传扰动、DNA 结合、蛋白互作、表型关联、组学共现在本组缺证据；在补齐这些设计前，目标实体 与“比较基因组与共线性”的方向性关系应作为待检验命题（[[daily-42262904-f6]]；[[ms-10-1038_s41467-026-76979-2-f1]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 表达相关 | 描述性 | 合计 |
|---|---|---|---|
| Arabidopsis thaliana | 1 | 3 | 4 |
| Oryza sativa | 0 | 3 | 3 |
| Zea mays | 0 | 2 | 2 |
| Vitis vinifera | 1 | 0 | 1 |
| Solanum lycopersicum | 1 | 0 | 1 |

**代表断言（原文摘录，未改写）**

- “In conclusion, these results reflect how several rounds of gene duplication (Sterck et al, 2007) allowed the evolution of a large set of cyclin paralogs and a myriad of regulators,…” — [[ref-msb-2010-53-f6]]（`10.1038/msb.2010.53`，descriptive/observational）
- “In the current study, we found that four pairs of paralogous genes developed through segmental duplication, whereas no evidence of tandem duplication was detected for any gene pair…” — [[ref-s12864-017-4082-y-f2]]（`10.1186/s12864-017-4082-y`，descriptive/observational）
- “Here, we report a chromosome-level genome assembly of Streptochaeta spicata, which represents the lineage without typical spikelets and the sister to the rest of Poaceae, and perfo…” — [[ms-10-1038_s41467-026-76979-2-f1]]（`10.1038/s41467-026-76979-2`，descriptive/observational）

### 2.3 群体遗传与选择信号

**规模** 64 条证据 / 47 篇文献；**构成** descriptive/observational(44)、phenotypic/association(19)、expression/regulation(1)；**因果层** 0 条（仅关联/描述，不得写因果）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Zea mays、Triticum aestivum，反复出现的实体为SPL9、SAG9；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-42110912-f5]]；[[daily-42203863-f3]]；[[daily-42204246-f2]]）。
- **证据层级的张力**：本组 0 条因果级证据，全部 64 条为表达、组学或描述性；任何“调控/导致”表述都必须降级为待检验命题（[[daily-42110912-f5]]；[[daily-42203863-f3]]）。
- **可检验缺口**：遗传扰动、DNA 结合、蛋白互作、组学共现在本组缺证据；在补齐这些设计前，SPL9、SAG9 与“群体遗传与选择信号”的方向性关系应作为待检验命题（[[daily-42110912-f5]]；[[daily-42203863-f3]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 表达相关 | 表型关联 | 描述性 | 合计 |
|---|---|---|---|---|
| Oryza sativa | 0 | 6 | 19 | 25 |
| Zea mays | 0 | 5 | 17 | 22 |
| Triticum aestivum | 0 | 5 | 11 | 16 |
| Arabidopsis thaliana | 0 | 0 | 10 | 10 |
| Glycine max | 0 | 2 | 7 | 9 |

**基因实体（自动标注，前 5）**：SPL9(1)、SAG9(1)、HAC1(1)、PermGWAS2(1)、OsNAC14(1)（标注覆盖 6/64）。

**代表断言（原文摘录，未改写）**

- “GWAS scans a large number of single-nucleotide polymorphisms (SNPs) across the genome in a population to identify genetic loci significantly associated with target phenotypes, ther…” — [[ms-10-1007_s42995-026-00409-x-f2]]（`10.1007/s42995-026-00409-x`，phenotypic/association）
- “We conclude by outlining a practical roadmap that couples long-term field trials with targeted genomic tools to support earlier selection ages, guide restoration planning and assis…” — [[ms-10-1007_s11676-026-02117-9-f1]]（`10.1007/s11676-026-02117-9`，descriptive/observational）
- “Compared with previous studies focused on global diversity panels or historical germplasm collections (Wang et al., 2020; Li et al., 2022), our study specifically targets contempor…” — [[daily-42500473-f5]]（`10.3389/fpls.2026.1872682`，descriptive/observational）

### 2.4 多倍化与亚基因组演化

**规模** 14 条证据 / 11 篇文献；**构成** descriptive/observational(12)、expression/regulation(2)；**因果层** 0 条（仅关联/描述，不得写因果）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Medicago spp.、Glycine max、Arabidopsis thaliana，反复出现的实体为PHY15；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[chromosome-level-genome-assemblies-of-musa-ornata-f1]]；[[chromosome-scale-genome-together-with-transcriptome-and-f6]]；[[daily-42204246-f3]]）。
- **证据层级的张力**：本组 0 条因果级证据，全部 14 条为表达、组学或描述性；任何“调控/导致”表述都必须降级为待检验命题（[[chromosome-level-genome-assemblies-of-musa-ornata-f1]]；[[chromosome-scale-genome-together-with-transcriptome-and-f6]]）。
- **可检验缺口**：遗传扰动、DNA 结合、蛋白互作、表型关联、组学共现在本组缺证据；在补齐这些设计前，PHY15 与“多倍化与亚基因组演化”的方向性关系应作为待检验命题（[[chromosome-level-genome-assemblies-of-musa-ornata-f1]]；[[chromosome-scale-genome-together-with-transcriptome-and-f6]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 表达相关 | 描述性 | 合计 |
|---|---|---|---|
| Medicago spp. | 0 | 6 | 6 |
| Glycine max | 0 | 5 | 5 |
| Arabidopsis thaliana | 1 | 3 | 4 |
| Phaseolus vulgaris | 0 | 4 | 4 |
| Oryza sativa | 0 | 3 | 3 |

**基因实体（自动标注，前 5）**：PHY15(1)（标注覆盖 1/14）。

**代表断言（原文摘录，未改写）**

- “In the context of common bean, our results suggest that induced polyploidization functions primarily as a generator of phenotypic dispersion rather than a directional improvement s…” — [[daily-42654866-f2]]（`10.3390/plants15162464`，descriptive/observational）
- “However, firm inference of the timing of ρ-WGD and the mode of polyploidization depends on the evolutionary relationships of Streptochaeta and Anomochloa; while conserved target ca…” — [[ms-10-1038_s41467-026-76979-2-f5]]（`10.1038/s41467-026-76979-2`，descriptive/observational）
- “These results not only broaden our understanding of phytochrome-mediated light percep tion in complex polyploid species but also identify Fxa PHY15 as a promising genetic target fo…” — [[ms-10-1186_s12870-026-08649-w-f6]]（`10.1186/s12870-026-08649-w`，descriptive/observational）

### 2.5 转座子与基因组可塑性

**规模** 221 条证据 / 131 篇文献；**构成** descriptive/observational(168)、phenotypic/association(29)、expression/regulation(13)、protein interaction(5)、omics/co-occurrence(4)、genetic perturbation(2)；**因果层** 7 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Arabidopsis thaliana、Zea mays，反复出现的实体为rhAmpSeq、StCOMT、flavonol；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[b4-ys8H9kH4cFVbPEuMHCg4nA-f7]]；[[b4-ys8H9kH4cFVbPEuMHCg4nA-f8]]；[[chromosome-scale-genome-together-with-transcriptome-and-f6]]）。
- **证据层级的张力**：7 条属于遗传扰动/蛋白互作/DNA 结合，214 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[multiomicsdriven-advances-in-the-understanding-of-f6]]；[[daily-42079767-f6]]）。
- **可检验缺口**：DNA 结合在本组缺证据；在补齐这些设计前，rhAmpSeq、StCOMT、flavonol 与“转座子与基因组可塑性”的方向性关系应作为待检验命题（[[b4-ys8H9kH4cFVbPEuMHCg4nA-f7]]；[[b4-ys8H9kH4cFVbPEuMHCg4nA-f8]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|
| Oryza sativa | 1 | 2 | 3 | 8 | 0 | 68 | 82 |
| Arabidopsis thaliana | 1 | 2 | 9 | 1 | 1 | 57 | 71 |
| Zea mays | 1 | 2 | 0 | 6 | 0 | 49 | 58 |
| Triticum aestivum | 0 | 1 | 2 | 8 | 0 | 32 | 43 |
| Solanum lycopersicum | 0 | 0 | 1 | 4 | 2 | 22 | 29 |

**基因实体（自动标注，前 5）**：rhAmpSeq(2)、StCOMT(1)、SPL9(1)、CmGRX(1)、GmGID(1)（标注覆盖 26/221）。

**化合物实体（自动标注，前 5）**：flavonol(1)（标注覆盖 1/221）。

**标注一致性提示**：本组 3 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[daily-42495169-f7]]。

**代表断言（原文摘录，未改写）**

- “Homozygous mutations in single and/or double allele(s) of GmFAD2-1A and GmFAD2-1B in soybean, which are created by transcription activator-like effector nucleases (TALENs) that tar…” — [[multiomicsdriven-advances-in-the-understanding-of-f6]]（`10.1111/tpj.16545`，genetic perturbation）
- “This domain enables bZIP transcription factors to specifically recognize and bind to particular DNA sequences, thereby regulating the expression of downstream genes., With the incr…” — [[daily-40523045-f3]]（`10.1080/21645698.2025.2510715`，protein interaction）
- “At the start of this circuit, the transcription factor proteins Circadian Locomotor Output Cycles Kaput (Clock) and Aryl hydrocarbon receptor nuclear translocator-like (Arntl, also…” — [[ms-10-1371_journal-pgen-1012287-f7]]（`10.1371/journal.pgen.1012287`，protein interaction）

### 2.6 进化发育与性状起源

**规模** 35 条证据 / 30 篇文献；**构成** descriptive/observational(30)、expression/regulation(4)、protein interaction(1)；**因果层** 1 条（可支撑有限机制表述）。

> 本组仅 1 条因果级证据，机制表述只在该证据覆盖的物种与条件下成立，不可外推到其余 34 条。

**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Oryza sativa、Zea mays，反复出现的实体为GPM1、PsDAM；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[b4-ys8H9kH4cFVbPEuMHCg4nA-f7]]；[[daily-42239855-f3]]；[[daily-42243690-f4]]）。
- **证据层级的张力**：1 条属于遗传扰动/蛋白互作/DNA 结合，34 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（；[[daily-42656881-f6]]）。
- **可检验缺口**：遗传扰动、DNA 结合、表型关联、组学共现在本组缺证据；在补齐这些设计前，GPM1、PsDAM 与“进化发育与性状起源”的方向性关系应作为待检验命题（[[b4-ys8H9kH4cFVbPEuMHCg4nA-f7]]；[[daily-42239855-f3]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 蛋白互作 | 表达相关 | 描述性 | 合计 |
|---|---|---|---|---|
| Arabidopsis thaliana | 1 | 1 | 13 | 15 |
| Oryza sativa | 0 | 0 | 8 | 8 |
| Zea mays | 0 | 0 | 8 | 8 |
| Glycine max | 0 | 0 | 5 | 5 |
| Gossypium hirsutum | 0 | 1 | 4 | 5 |

**基因实体（自动标注，前 5）**：GPM1(1)、PsDAM(1)、PshDAM1(1)、PshDAM6(1)、DcMYB1(1)（标注覆盖 4/35）。

**代表断言（原文摘录，未改写）**

- “The phylogenetic patterns observed in PQS frequency raise the question of what biological machinery might interact with these structures in the chloroplast context.” — [[daily-42243690-f4]]（`10.1186/s12870-026-09148-8`，protein interaction）
- “Several studies suggest that changes in gene expression linked to environmental variability may play a crucial role in adaptive evolution [23], based on observed genotype-by-enviro…” — [[ms-10-1038_s41598-026-56462-0-f1]]（`10.1038/s41598-026-56462-0`，expression/regulation）
- “Their co-occurrence across several phylogenetic branches supports the hypothesis that these loci have been co-maintained, potentially due to their location on homeologous chromosom…” — [[daily-42275315-f3]]（`10.1371/journal.pone.0349201`，descriptive/observational）

### 2.7 泛基因组与作物改良

**规模** 43 条证据 / 34 篇文献；**构成** descriptive/observational(36)、phenotypic/association(6)、expression/regulation(1)；**因果层** 0 条（仅关联/描述，不得写因果）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Zea mays、Triticum aestivum，反复出现的实体为HAC1；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-41261851-f1]]；[[daily-42079767-f6]]；[[daily-42079772-f1]]）。
- **证据层级的张力**：本组 0 条因果级证据，全部 43 条为表达、组学或描述性；任何“调控/导致”表述都必须降级为待检验命题（[[daily-41261851-f1]]；[[daily-42079767-f6]]）。
- **可检验缺口**：遗传扰动、DNA 结合、蛋白互作、组学共现在本组缺证据；在补齐这些设计前，HAC1 与“泛基因组与作物改良”的方向性关系应作为待检验命题（[[daily-41261851-f1]]；[[daily-42079767-f6]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 表达相关 | 表型关联 | 描述性 | 合计 |
|---|---|---|---|---|
| Oryza sativa | 1 | 1 | 20 | 22 |
| Zea mays | 0 | 1 | 17 | 18 |
| Triticum aestivum | 0 | 0 | 10 | 10 |
| Glycine max | 0 | 0 | 6 | 6 |
| Arabidopsis thaliana | 1 | 0 | 4 | 5 |

**基因实体（自动标注，前 5）**：HAC1(2)（标注覆盖 2/43）。

**代表断言（原文摘录，未改写）**

- “While yield is known to be a polygenic trait ( ), this study provides field-based evidence of how specific genomic regions contribute to increased yield under heat stress and how t…” — [[daily-42724109-f2]]（`10.3389/fpls.2026.1919895`，descriptive/observational）
- “The identification of QTLs that overlap with previous studies and are located near genes with either strong literature support or a plausible functional link to the measured traits…” — [[daily-42639039-f4]]（`10.3389/fpls.2026.1895808`，descriptive/observational）
- “Our findings reveal how subfunctionalization and domestication help shape the HAC regulatory network in soybean, highlighting wild germplasm as a valuable reservoir for recovering …” — [[daily-42410509-f1]]（`10.1186/s12870-026-09449-y`，descriptive/observational）

## 3. 跨子主题实体枢纽（自动统计）

下列实体在 **≥2 个子主题**中被独立证据提及。它们本身**不构成机制结论**，但说明该实体是本主题多条研究线的交叉点，值得优先核对证据层级。

| 基因 | 命中子主题数 | 证据条数 | 涉及子主题 |
|---|---|---|---|
| OsNAC14 | 3 | 3 | 群体遗传与选择信号、转座子与基因组可塑性、进化发育与性状起源 |
| rhAmpSeq | 2 | 4 | 基因组组装与注释、转座子与基因组可塑性 |
| HAC1 | 2 | 3 | 泛基因组与作物改良、群体遗传与选择信号 |
| NLR8 | 2 | 2 | 群体遗传与选择信号、转座子与基因组可塑性 |
| PHY15 | 2 | 2 | 多倍化与亚基因组演化、转座子与基因组可塑性 |
| PermGWAS2 | 2 | 2 | 群体遗传与选择信号、转座子与基因组可塑性 |
| PsDAM | 2 | 2 | 转座子与基因组可塑性、进化发育与性状起源 |
| PshDAM1 | 2 | 2 | 转座子与基因组可塑性、进化发育与性状起源 |
| PshDAM6 | 2 | 2 | 转座子与基因组可塑性、进化发育与性状起源 |
| SAG9 | 2 | 2 | 群体遗传与选择信号、转座子与基因组可塑性 |

### 3.1 跨子主题受控叙述

- **交叉实体**：OsNAC14、rhAmpSeq、HAC1、NLR8、PHY15 等实体在 ≥2 个子主题中重复出现；这只能说明多条研究线指向同一候选，不能说明同一机制（[[b4-ys8H9kH4cFVbPEuMHCg4nA-f5]]；[[b4-ys8H9kH4cFVbPEuMHCg4nA-f7]]）。
- **层级不均**：因果层证据在子主题间分布不均，最高为“转座子与基因组可塑性”（7 条），最低为“基因组组装与注释”（0 条）；跨子主题比较结论强度前须先对齐这一差异。
- **共同缺口**：全主题缺失 DNA 结合；涉及这些推断的跨子主题归纳只能写成待检验命题。

## 4. 研究设计缺口矩阵（子主题 × 证据类型）

> 单元格为证据条数，`—` 表示该组合在本主题无证据。最后一列之后按行读：一行里若前三列全为 `—`，该子主题**没有任何因果层证据**。

| 子主题 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 |
|---|---|---|---|---|---|---|---|
| 基因组组装与注释 | — | — | — | 1 | 6 | 1 | 11 |
| 比较基因组与共线性 | — | — | — | 1 | — | — | 3 |
| 群体遗传与选择信号 | — | — | — | 1 | 19 | — | 44 |
| 多倍化与亚基因组演化 | — | — | — | 2 | — | — | 12 |
| 转座子与基因组可塑性 | 2 | 5 | — | 13 | 29 | 4 | 168 |
| 进化发育与性状起源 | — | 1 | — | 4 | — | — | 30 |
| 泛基因组与作物改良 | — | — | — | 1 | 6 | — | 36 |

**零因果层子主题（5/7）**：基因组组装与注释、比较基因组与共线性、群体遗传与选择信号、多倍化与亚基因组演化、泛基因组与作物改良。

这些子主题目前只能产出相关性假说；若研究方案把它们写成“X 调控 Y”，属于超越证据的表达，须在方案中降级为待验证命题。

## 5. 可直接引用的因果级证据（自动筛选）

以下 7 条证据的实验设计属于扰动或直接互作，可作为机制论断的一手依据；引用时须核对原文的物种、组织与处理条件。

| 证据页 | DOI | 类型 | 断言（摘录） |
|---|---|---|---|
| [[daily-40523045-f3]] | `10.1080/21645698.2025.2510715` | protein interaction | This domain enables bZIP transcription factors to specifically recognize and bind to particular DNA sequences, thereby r… |
| [[daily-42243690-f4]] | `10.1186/s12870-026-09148-8` | protein interaction | The phylogenetic patterns observed in PQS frequency raise the question of what biological machinery might interact with … |
| [[daily-42413033-f7]] | `10.1093/plphys/kiag473` | protein interaction | TFs are DNA-binding proteins that can selectively bind to cis-regulatory elements (CREs) in the genome based on sequence… |
| [[ms-10-1007_s10142-026-01908-x-f4]] | `10.1007/s10142-026-01908-x` | protein interaction | 1 3 Page 5 of 16 133 Functional & Integrative Genomics (2026) 26:133 Bimolecular fluorescence complementation (BiFC) ana… |
| [[ms-10-1371_journal-pgen-1012287-f7]] | `10.1371/journal.pgen.1012287` | protein interaction | At the start of this circuit, the transcription factor proteins Circadian Locomotor Output Cycles Kaput (Clock) and Aryl… |
| [[multiomicsdriven-advances-in-the-understanding-of-f6]] | `10.1111/tpj.16545` | genetic perturbation | Homozygous mutations in single and/or double allele(s) of GmFAD2-1A and GmFAD2-1B in soybean, which are created by trans… |
| [[ref-science-1086391-f3]] | `10.1126/science.1086391` | genetic perturbation | Although there were no effects of G C content on T-DNA integration sites observed at the genome scale, we found a positi… |

## 6. 证据间的张力与矛盾（自动筛查）

未筛查到方向相反的表述。注意：这**不等于**结论一致——多数证据只报告单一方向的观察，缺少反证不等于已被重复验证。

## 7. 覆盖与代表性缺口

- **因果级证据占比仅 2.4%**：机制结论的可信度受限于此，建议对排名靠前的子主题定向补做扰动实验或查找已有突变体表型数据。
- **5 个子主题完全没有因果层证据**（基因组组装与注释、比较基因组与共线性、群体遗传与选择信号、多倍化与亚基因组演化…）：这些方向目前只能写相关性。
- **单篇证据物种 8 个**（Selaginella spp.、Chlamydomonas reinhardtii、Petunia hybrida、Azolla、Dioscorea spp.…）：跨物种外推缺乏支撑。
- **37 条证据（13%）未命中任何子主题**：说明子主题词表覆盖不足，这部分证据目前无法进入结构性讨论。
- **证据类型以摘要级断言为主**：本知识库对多数文献仅收录摘要/图表级断言，无法支撑实验条件比较与因果推断；全文覆盖率是当前深度的上限约束。
- **文献元数据不全**：论文页 `year` / `journal` 字段覆盖率极低，因此本页不给出发表年份分布，也无法用年份评估时效性；frontmatter 的 `library_papers` 为历史手写值，与 tags 归一化统计相差数倍，**不可引用**。

## 8. 历史正文说明

本页 2026-11-03 之前的正文为人工/LLM 撰写，未与证据逐条对齐，含不可核的行内断言缺引用、格式残留与跨主题内容混入。该正文已原样归档至 `_review/synthesis_legacy_20261103`，保留供追溯，**不得再作为结论来源**。原“与大豆项目关联”的定性判断保留在 frontmatter 的 `soybean_relevance` 字段，其论证过程同样需重新取证。

## 9. 行内引用密度自检

本页正文 3953 个中文字符，行内证据链接 80 处，密度 **10.1 处/500 字**（目标 ≥1）。链接指向证据页，不直接指向出版社；引用前须沿证据页回到原文核对。
