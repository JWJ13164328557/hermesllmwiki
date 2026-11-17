---

title: "基因组与进化 — Synthesis"
created: 2026-06-01
total_evidence: 521
total_papers: 273
library_papers: 520  # 全库按themes归类该主题文献数
type: synthesis
body_status: rebuilt-2026-11-07
tags: [synthesis, genomics, evolution, genome-assembly, comparative-genomics, GWAS, polyploidization, domestication]


soybean_relevance: ⭐中高
legacy_archive: _review/synthesis_legacy_20261107/genomics-evolution.md
rebuild_rule: evidence-fields-only; no-cross-evidence-inference
rebuild_version: v3

---
# 基因组学与演化 知识综合（证据重建版 v3）

<!-- AUTO-EVIDENCE-STRENGTH:START -->

## 证据覆盖与强度（自动统计，可复算）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据条目 | 521 | 本主题归属的证据对象数 |
| 独立论文 | 273 | 去重后的 PMID/DOI 数 |
| 平均每篇证据数 | 1.91 | <1.0 说明多数论文只贡献 1 条结论 |
| 单条证据论文占比 | 47% | 越高说明"每篇论文一个结论"，系统性弱 |
| 主要物种 | Oryza sativa(167)、Zea mays(102)、Arabidopsis thaliana(97)、Triticum aestivum(84)、Glycine max(64)、Solanum lycopersicum(45) | 物种过度集中则外推性受限 |
| 证据类型 | descriptive/observational 400；phenotypic/association 78；omics/co-occurrence 14；expression/regulation 13；protein interaction 8；genetic perturbation 6 | 表达/关联类居多时，因果结论需打折扣 |

> 归属依据：`themes.py` 标签别名表（高置信）+ 关键词兜底（低置信）。本段由脚本生成，不构成结论；结论性文字须回原文核对。

### 可复核证据索引（前 12 条，按断言长度）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `multiomicsdriven-advances-in-the-understanding-of-f6` | 10.1111/tpj.16545 | Homozygous mutations in single and/or double allele(s) of GmFAD2-1A and GmFAD2-1B in soybe |
| `daily-42137983-f1` | 10.1093/nar/gkag476 | Using custom-made antibodies specific to the rice H2A.X variant, we show that it repressed |
| `daily-42317260-f4` | 10.3389/fgene.2026.1850332 | The results showed that a total of 16 QTLs associated with pod number, notably, overlappin |
| `ref-science-1086391-f3` | 10.1126/science.1086391 | Although there were no effects of G C content on T-DNA integration sites observed at the g |
| `daily-42429570-f5` | 10.1128/spectrum.00381-26 | The inability to recover escape mutants further suggests that systems like DRT11 may targe |
| `daily-42713468-f7` | 10.3389/fpls.2026.1902159 | Compared with conventional CRISPR/Cas9-mediated editing, PE substantially reduces the risk |
| `daily-40523045-f3` | 10.1080/21645698.2025.2510715 | This domain enables bZIP transcription factors to specifically recognize and bind to parti |
| `daily-42670212-f3` | 10.1111/pbi.70748 | In contrast to the hQTL Integrated_GY_hQTL121 on chromosome 4A which interacts with many r |
| `ms-10-1371_journal-pgen-1012287-f7` | 10.1371/journal.pgen.1012287 | At the start of this circuit, the transcription factor proteins Circadian Locomotor Output |
| `daily-42413033-f7` | 10.1093/plphys/kiag473 | TFs are DNA-binding proteins that can selectively bind to cis-regulatory elements (CREs) i |
| `daily-42283811-f1` | 10.1007/s00248-026-02803-5 | ICE dynamics in these bacteria often interact with other components of the mobilome, inclu |
| `daily-42514528-f2` | 10.3390/plants15142160 | It binds to the expression product of VirA, activating other Vir genes, resulting in the c |

### 证据语义分层

| 证据类型 | 条目数 | 可支持的推断强度 |
|---|---:|---|
| genetic perturbation | 6 | 遗传因果（扰动后表型/表达改变） |
| protein interaction | 8 | 物理互作（Co-IP/Y2H/BiFC/pull-down） |
| DNA binding/regulation | 2 | 直接调控（ChIP/EMSA/启动子报告） |
| expression/regulation | 13 | 表达相关（转录组/qPCR，不能单独推因果） |
| phenotypic/association | 78 | 表型关联（GWAS/QTL/自然变异/田间） |
| omics/co-occurrence | 14 | 组学共现（单细胞簇/共表达网络，非调控） |
| descriptive/observational | 400 | 描述性/背景陈述（未报告可核验的实验设计） |

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

> 本页正文于 2026-11-07 由 `rebuild_synthesis_body.py` 从 **521 条证据对象 / 273 篇文献**确定性重建：所有陈述均可回溯到下列证据页；英文为原文摘录，未经改写；不含跨证据的推测性归纳。历史人工正文已归档至 `_review/synthesis_legacy_20261107`，不再作为本页结论来源。
>
> 阅读约定：`遗传扰动` / `蛋白互作` / `DNA 结合` 三类证据才支持“因果”或“直接调控”的表述；`表达相关` 与 `组学共现` 只能提出关联性假说。

## 0. 综述提要（受控生成）

本主题当前纳入 **521 条证据 / 273 篇文献**。规则判定为因果或直接调控的 **15 条（2.9%）**；剔除方法描述、相关性措辞与无基因实体标注的条目后，可用于提要的 **3 条**。可判定程度最高的结论集中在GmFAD2、BSMT1、KNAT1：Homozygous mutations in single and/or double allele(s) of GmFAD2-1A and GmFAD2-1B in soybean, which are created by transcription activator-l…（[[multiomicsdriven-advances-in-the-understanding-of-f6]]）；Using an integrated approach combining biosynthetic pathway elucidation, regulatory mechanism dissection, evolutionary analysis, and field t…（[[daily-42384783-f1]]）；Recent genome-wide binding analysis via ChIP-seq has further verified that the STM protein can directly bind to the promoter regions of othe…（[[daily-42514495-f3]]）。研究重心位于“转座子与基因组可塑性”（416 条证据，占 80%）。证据的物种分布以 Oryza sativa 为首（167 条，32%）。七类证据均有覆盖，但DNA 结合各仅 1–2 条；主要瓶颈从“类型缺失”转为“同一结论的独立复现不足”。阅读时须区分两类陈述：因果级证据支撑的“已证机制”，以及表达/组学/描述性证据提示的“候选关联”；后者不得改写成调控或因果。

> 提要由脚本按证据类型与实体计数生成，不含跨证据的机制外推；逐条依据见第 2–3 节。

## 1. 主题概览（自动统计）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据对象 | 521 | 本主题归属的证据条目数 |
| 独立文献（DOI/PMID 去重） | 273 | 去重后的论文数 |
| 平均每篇证据数 | 1.91 | 接近 1.0 说明每篇论文只贡献一条结论，系统性弱 |
| 单条证据论文占比 | 47%（129/273） | 越高说明证据碎片化越严重 |
| 证据类型构成 | descriptive/observational(401)、phenotypic/association(78)、omics/co-occurrence(14)、expression/regulation(13)、protein interaction(8)、genetic perturbation(5)、DNA binding/regulation(2) | 描述性占多数时机制结论需打折扣 |
| 类型标注置信度 | 未标(519)、medium(1)、low(1) | 低置信度标注须回原文核对 |
| 主要物种 | Oryza sativa(167)、Zea mays(102)、Arabidopsis thaliana(98)、Triticum aestivum(84)、Glycine max(64)、Solanum lycopersicum(45) | 物种过度集中则外推性受限 |
| 子主题覆盖 | 7/7（证据 <5 条的 0 个） | 覆盖缺口见第 7 节 |
| 未命中任何子主题的证据 | 53（10%） | 占比高说明子主题词表或证据文本需扩表 |

因果级证据共 **15 条**，占本主题证据的 **2.9%**。这一比例决定本主题哪些结论可以写成机制，哪些只能写成相关性。

物种主导度：**Oryza sativa** 出现在 167 条证据（32%）。分布较分散，单物种主导风险较低，但需注意各物种证据层级是否可比。

## 2. 子主题分解（按证据重建）

> 一条证据可同时命中多个子主题（共 197 条跨组），因此各子主题计数之和大于总证据数。物种×类型交叉表只统计已标注字段，空单元格表示该组合无证据，不等于不存在相应生物学过程。凡“因果层 0 条”的子主题，其代表断言只能读作相关性，不得改写为调控或因果。

### 2.1 基因组组装与注释

**规模** 27 条证据 / 23 篇文献；**构成** descriptive/observational(16)、phenotypic/association(9)、expression/regulation(1)、omics/co-occurrence(1)；**因果层** 0 条（仅关联/描述，不得写因果）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Arabidopsis thaliana、Triticum aestivum，反复出现的实体为rhAmpSeq、MKK3；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-41358539-f1]]；[[daily-42283206-f2]]；[[daily-42292955-f1]]）。
- **证据层级的张力**：本组 0 条因果级证据，全部 27 条为表达、组学或描述性；任何“调控/导致”表述都必须降级为待检验命题（[[daily-41358539-f1]]；[[daily-42283206-f2]]）。
- **可检验缺口**：遗传扰动、DNA 结合、蛋白互作在本组缺证据；在补齐这些设计前，rhAmpSeq、MKK3 与“基因组组装与注释”的方向性关系应作为待检验命题（[[daily-41358539-f1]]；[[daily-42283206-f2]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|
| Oryza sativa | 0 | 4 | 0 | 4 | 8 |
| Arabidopsis thaliana | 1 | 0 | 1 | 4 | 6 |
| Triticum aestivum | 1 | 1 | 0 | 2 | 4 |
| Glycine max | 0 | 1 | 0 | 2 | 3 |
| Nicotiana tabacum | 0 | 1 | 0 | 2 | 3 |

**基因实体（自动标注，前 5）**：rhAmpSeq(2)、MKK3(1)（标注覆盖 3/27）。

**代表断言（原文摘录，未改写）**

- “Genetic diversity and private haplotype analysis identified multiple regions with high diversity (the Yellow River, the middle and Yangtze River and the Pearl River basin) where th…” — [[daily-42555919-f4]]（`10.1093/aob/mcag248`，phenotypic/association）
- “Our findings confirm the advantages of SMRT, which facilitated the construction a rich transcript data-set for research on the development of ginkgo seeds, enriching the annotation…” — [[full-length-sequencing-of-ginkgo-biloba-l-f1]]（`10.1016/j.indcrop.2021.113714`，descriptive/observational）
- “Our results show that sequence-to-expression models are a viable tool for gaining biological insight and generating novel hypotheses in any species of interest, even complex polypl…” — [[daily-42413033-f1]]（`10.1093/plphys/kiag473`，expression/regulation）

### 2.2 比较基因组与共线性

**规模** 14 条证据 / 13 篇文献；**构成** descriptive/observational(13)、expression/regulation(1)；**因果层** 0 条（仅关联/描述，不得写因果）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Zea mays、Arabidopsis thaliana，反复出现的实体为HaALS、OsPRTs；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-42079765-f5]]；[[daily-42210059-f7]]；[[daily-42221884-f7]]）。
- **证据层级的张力**：本组 0 条因果级证据，全部 14 条为表达、组学或描述性；任何“调控/导致”表述都必须降级为待检验命题（[[daily-42079765-f5]]；[[daily-42210059-f7]]）。
- **可检验缺口**：遗传扰动、DNA 结合、蛋白互作、表型关联、组学共现在本组缺证据；在补齐这些设计前，HaALS、OsPRTs 与“比较基因组与共线性”的方向性关系应作为待检验命题（[[daily-42079765-f5]]；[[daily-42210059-f7]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 表达相关 | 描述性 | 合计 |
|---|---|---|---|
| Oryza sativa | 0 | 7 | 7 |
| Zea mays | 1 | 5 | 6 |
| Arabidopsis thaliana | 0 | 4 | 4 |
| Glycine max | 0 | 2 | 2 |
| Nicotiana tabacum | 0 | 2 | 2 |

**基因实体（自动标注，前 5）**：HaALS(2)、OsPRTs(1)、CCA1(1)、ELF3(1)、LWD1(1)（标注覆盖 5/14）。

**代表断言（原文摘录，未改写）**

- “In conclusion, these results reflect how several rounds of gene duplication (Sterck et al, 2007) allowed the evolution of a large set of cyclin paralogs and a myriad of regulators,…” — [[ref-msb-2010-53-f6]]（`10.1038/msb.2010.53`，descriptive/observational）
- “By integrating genome-wide family characterization with genotype-resolved expression profiling under imazethapyr treatment, this study provides a framework for understanding HaALS …” — [[daily-42514481-f7]]（`10.3390/plants15142113`，expression/regulation）
- “In the current study, we found that four pairs of paralogous genes developed through segmental duplication, whereas no evidence of tandem duplication was detected for any gene pair…” — [[ref-s12864-017-4082-y-f2]]（`10.1186/s12864-017-4082-y`，descriptive/observational）

### 2.3 群体遗传与选择信号

**规模** 107 条证据 / 82 篇文献；**构成** descriptive/observational(71)、phenotypic/association(33)、expression/regulation(2)、omics/co-occurrence(1)；**因果层** 0 条（仅关联/描述，不得写因果）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Zea mays、Triticum aestivum，反复出现的实体为SPL9、OsPRTs、auxin、phenolic；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-41829717-f1]]；[[daily-42079765-f6]]；[[daily-42203863-f3]]）。
- **证据层级的张力**：本组 0 条因果级证据，全部 107 条为表达、组学或描述性；任何“调控/导致”表述都必须降级为待检验命题（[[daily-41829717-f1]]；[[daily-42079765-f6]]）。
- **可检验缺口**：遗传扰动、DNA 结合、蛋白互作在本组缺证据；在补齐这些设计前，SPL9、OsPRTs、auxin 与“群体遗传与选择信号”的方向性关系应作为待检验命题（[[daily-41829717-f1]]；[[daily-42079765-f6]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|
| Oryza sativa | 0 | 9 | 1 | 25 | 35 |
| Zea mays | 0 | 7 | 1 | 17 | 25 |
| Triticum aestivum | 0 | 5 | 1 | 14 | 20 |
| Glycine max | 0 | 5 | 0 | 11 | 16 |
| Gossypium hirsutum | 1 | 9 | 0 | 5 | 15 |

**基因实体（自动标注，前 5）**：SPL9(1)、OsPRTs(1)、SAG9(1)、AhLOG(1)、GhTOFD06(1)（标注覆盖 14/107）。

**化合物实体（自动标注，前 5）**：auxin(1)、phenolic(1)、flavonoid(1)（标注覆盖 3/107）。

**代表断言（原文摘录，未改写）**

- “Collectively, these lines of evidence challenge the conventional single-centre model and point instead to a diffuse process, in which peach domestication unfolded concurrently acro…” — [[daily-42555919-f3]]（`10.1093/aob/mcag248`，descriptive/observational）
- “Concurrently, SB has been combined with marker-assisted selection (MAS), genomic selection (GS), and genome-editing technologies, allowing breeders to shorten not only the time nee…” — [[daily-42588892-f1]]（`10.3390/plants15152389`，descriptive/observational）
- “Collectively, the highquality resequencing data, robust SNP dataset, transitionbiased substitution patterns, heterogeneous SNP density, moderate nucleotide diversity, and structure…” — [[daily-42609053-f2]]（`10.1002/tpg2.70289`，descriptive/observational）

### 2.4 多倍化与亚基因组演化

**规模** 32 条证据 / 23 篇文献；**构成** descriptive/observational(26)、phenotypic/association(3)、omics/co-occurrence(2)、expression/regulation(1)；**因果层** 0 条（仅关联/描述，不得写因果）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Nicotiana tabacum、Glycine max，反复出现的实体为GlyPDF、HaALS、sucrose；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[chromosome-level-genome-assemblies-of-musa-ornata-f1]]；[[chromosome-scale-genome-together-with-transcriptome-and-f6]]；[[daily-42204246-f3]]）。
- **证据层级的张力**：本组 0 条因果级证据，全部 32 条为表达、组学或描述性；任何“调控/导致”表述都必须降级为待检验命题（[[chromosome-level-genome-assemblies-of-musa-ornata-f1]]；[[chromosome-scale-genome-together-with-transcriptome-and-f6]]）。
- **可检验缺口**：遗传扰动、DNA 结合、蛋白互作在本组缺证据；在补齐这些设计前，GlyPDF、HaALS、sucrose 与“多倍化与亚基因组演化”的方向性关系应作为待检验命题（[[chromosome-level-genome-assemblies-of-musa-ornata-f1]]；[[chromosome-scale-genome-together-with-transcriptome-and-f6]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|
| Arabidopsis thaliana | 1 | 0 | 1 | 5 | 7 |
| Nicotiana tabacum | 0 | 1 | 1 | 5 | 7 |
| Glycine max | 0 | 1 | 0 | 5 | 6 |
| Medicago spp. | 0 | 1 | 0 | 5 | 6 |
| Oryza sativa | 0 | 0 | 0 | 6 | 6 |

**基因实体（自动标注，前 5）**：GlyPDF(1)、HaALS(1)、PHY15(1)（标注覆盖 3/32）。

**化合物实体（自动标注，前 5）**：sucrose(1)（标注覆盖 1/32）。

**标注一致性提示**：本组 1 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[daily-42716490-f8]]。

**代表断言（原文摘录，未改写）**

- “In the context of common bean, our results suggest that induced polyploidization functions primarily as a generator of phenotypic dispersion rather than a directional improvement s…” — [[daily-42654866-f2]]（`10.3390/plants15162464`，descriptive/observational）
- “However, firm inference of the timing of ρ-WGD and the mode of polyploidization depends on the evolutionary relationships of Streptochaeta and Anomochloa; while conserved target ca…” — [[ms-10-1038_s41467-026-76979-2-f5]]（`10.1038/s41467-026-76979-2`，descriptive/observational）
- “These results not only broaden our understanding of phytochrome-mediated light percep tion in complex polyploid species but also identify Fxa PHY15 as a promising genetic target fo…” — [[ms-10-1186_s12870-026-08649-w-f6]]（`10.1186/s12870-026-08649-w`，descriptive/observational）

### 2.5 转座子与基因组可塑性

**规模** 416 条证据 / 241 篇文献；**构成** descriptive/observational(313)、phenotypic/association(67)、omics/co-occurrence(11)、expression/regulation(10)、protein interaction(8)、genetic perturbation(5)；**因果层** 15 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Zea mays、Arabidopsis thaliana，反复出现的实体为HaALS、LuGRAS、anthocyanin、sucrose；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[b4-ys8H9kH4cFVbPEuMHCg4nA-f7]]；[[b4-ys8H9kH4cFVbPEuMHCg4nA-f8]]；[[chromosome-scale-genome-together-with-transcriptome-and-f6]]）。
- **证据层级的张力**：15 条属于遗传扰动/蛋白互作/DNA 结合，401 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-42384783-f1]]；[[daily-42514495-f3]]；[[daily-42226631-f1]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[daily-42384783-f1]]；[[daily-42514495-f3]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Oryza sativa | 3 | 1 | 1 | 1 | 19 | 3 | 100 | 128 |
| Zea mays | 2 | 2 | 0 | 2 | 13 | 1 | 65 | 85 |
| Arabidopsis thaliana | 1 | 2 | 0 | 3 | 6 | 2 | 68 | 82 |
| Triticum aestivum | 1 | 3 | 0 | 2 | 10 | 2 | 51 | 69 |
| Glycine max | 1 | 1 | 0 | 1 | 11 | 0 | 37 | 51 |

**基因实体（自动标注，前 5）**：HaALS(3)、LuGRAS(2)、PpSAP(2)、OsPRTs(2)、ZmSET(2)（标注覆盖 72/416）。

**化合物实体（自动标注，前 5）**：anthocyanin(1)、sucrose(1)、auxin(1)、phenolic(1)、flavonoid(1)（标注覆盖 5/416）。

**标注一致性提示**：本组 4 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[daily-42713468-f4]]。

**代表断言（原文摘录，未改写）**

- “Using an integrated approach combining biosynthetic pathway elucidation, regulatory mechanism dissection, evolutionary analysis, and field trials, we show that the rice MYC2-JAMYB …” — [[daily-42384783-f1]]（`10.1126/sciadv.aeg6081`，DNA binding/regulation）
- “Homozygous mutations in single and/or double allele(s) of GmFAD2-1A and GmFAD2-1B in soybean, which are created by transcription activator-like effector nucleases (TALENs) that tar…” — [[multiomicsdriven-advances-in-the-understanding-of-f6]]（`10.1111/tpj.16545`，genetic perturbation）
- “This domain enables bZIP transcription factors to specifically recognize and bind to particular DNA sequences, thereby regulating the expression of downstream genes., With the incr…” — [[daily-40523045-f3]]（`10.1080/21645698.2025.2510715`，protein interaction）

### 2.6 进化发育与性状起源

**规模** 54 条证据 / 49 篇文献；**构成** descriptive/observational(53)、protein interaction(1)；**因果层** 1 条（可支撑有限机制表述）。

> 本组仅 1 条因果级证据，机制表述只在该证据覆盖的物种与条件下成立，不可外推到其余 53 条。

**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Oryza sativa、Zea mays，反复出现的实体为OsPRT、OsPRTs、flavonoid；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[b4-ys8H9kH4cFVbPEuMHCg4nA-f7]]；[[daily-41358539-f7]]；[[daily-42210059-f1]]）。
- **证据层级的张力**：1 条属于遗传扰动/蛋白互作/DNA 结合，53 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（）。
- **可检验缺口**：遗传扰动、DNA 结合、表达相关、表型关联、组学共现在本组缺证据；在补齐这些设计前，OsPRT、OsPRTs、flavonoid 与“进化发育与性状起源”的方向性关系应作为待检验命题（[[b4-ys8H9kH4cFVbPEuMHCg4nA-f7]]；[[daily-41358539-f7]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 蛋白互作 | 描述性 | 合计 |
|---|---|---|---|
| Arabidopsis thaliana | 1 | 16 | 17 |
| Oryza sativa | 0 | 11 | 11 |
| Zea mays | 0 | 7 | 7 |
| Glycine max | 0 | 6 | 6 |
| Triticum aestivum | 0 | 5 | 5 |

**基因实体（自动标注，前 5）**：OsPRT(1)、OsPRTs(1)、GPM1(1)、ZmSET(1)、PsDAM(1)（标注覆盖 7/54）。

**化合物实体（自动标注，前 5）**：flavonoid(2)（标注覆盖 2/54）。

**代表断言（原文摘录，未改写）**

- “The phylogenetic patterns observed in PQS frequency raise the question of what biological machinery might interact with these structures in the chloroplast context.” — [[daily-42243690-f4]]（`10.1186/s12870-026-09148-8`，protein interaction）
- “We conclude by outlining a practical roadmap that couples long-term field trials with targeted genomic tools to support earlier selection ages, guide restoration planning and assis…” — [[ms-10-1007_s11676-026-02117-9-f1]]（`10.1007/s11676-026-02117-9`，descriptive/observational）
- “Both trajectories provide adaptive cassettes for stress responses and plant interactions, reflecting distinct ecological strategies within the genus Taken together, the Xanthomonas…” — [[daily-42283811-f8]]（`10.1007/s00248-026-02803-5`，descriptive/observational）

### 2.7 泛基因组与作物改良

**规模** 65 条证据 / 52 篇文献；**构成** descriptive/observational(52)、phenotypic/association(11)、expression/regulation(2)；**因果层** 0 条（仅关联/描述，不得写因果）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Zea mays、Triticum aestivum，反复出现的实体为AhLOG、HAC1、phenolic、flavonoid；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-41358539-f4]]；[[daily-42079772-f1]]；[[daily-42222012-f1]]）。
- **证据层级的张力**：本组 0 条因果级证据，全部 65 条为表达、组学或描述性；任何“调控/导致”表述都必须降级为待检验命题（[[daily-41358539-f4]]；[[daily-42079772-f1]]）。
- **可检验缺口**：遗传扰动、DNA 结合、蛋白互作、组学共现在本组缺证据；在补齐这些设计前，AhLOG、HAC1、phenolic 与“泛基因组与作物改良”的方向性关系应作为待检验命题（[[daily-41358539-f4]]；[[daily-42079772-f1]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 表达相关 | 表型关联 | 描述性 | 合计 |
|---|---|---|---|---|
| Oryza sativa | 0 | 2 | 24 | 26 |
| Zea mays | 1 | 4 | 20 | 25 |
| Triticum aestivum | 0 | 1 | 11 | 12 |
| Glycine max | 0 | 0 | 8 | 8 |
| Arabidopsis thaliana | 0 | 2 | 5 | 7 |

**基因实体（自动标注，前 5）**：AhLOG(2)、HAC1(2)、HaALS(2)、TriFAs(1)、InDels(1)（标注覆盖 8/65）。

**化合物实体（自动标注，前 5）**：phenolic(1)、flavonoid(1)（标注覆盖 2/65）。

**标注一致性提示**：本组 1 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[ms-10-14719_pst-15098-f2]]。

**代表断言（原文摘录，未改写）**

- “Compared with previous studies focused on global diversity panels or historical germplasm collections (Wang et al., 2020; Li et al., 2022), our study specifically targets contempor…” — [[daily-42500473-f5]]（`10.3389/fpls.2026.1872682`，descriptive/observational）
- “Together, the QTL regions identified in this study provide a foundation for the investigation of candidate genes regulating phenolic acid accumulation in maize kernels and represen…” — [[daily-42682625-f7]]（`10.3389/fpls.2026.1876404`，phenotypic/association）
- “Accordingly, candidate loci prioritised by pangenomes must be integrated with multiomic and experimental approaches to establish biological function and refine engineering targets,…” — [[daily-42643124-f6]]（`10.1111/pbi.70749`，descriptive/observational）

## 3. 跨子主题实体枢纽（自动统计）

下列实体在 **≥2 个子主题**中被独立证据提及。它们本身**不构成机制结论**，但说明该实体是本主题多条研究线的交叉点，值得优先核对证据层级。

| 基因 | 命中子主题数 | 证据条数 | 涉及子主题 |
|---|---|---|---|
| HaALS | 4 | 8 | 多倍化与亚基因组演化、比较基因组与共线性、泛基因组与作物改良、转座子与基因组可塑性 |
| OsPRTs | 4 | 5 | 比较基因组与共线性、群体遗传与选择信号、转座子与基因组可塑性、进化发育与性状起源 |
| AhLOG | 3 | 4 | 泛基因组与作物改良、群体遗传与选择信号、转座子与基因组可塑性 |
| MKK3 | 3 | 4 | 基因组组装与注释、群体遗传与选择信号、转座子与基因组可塑性 |
| GlyPDF | 3 | 3 | 多倍化与亚基因组演化、比较基因组与共线性、转座子与基因组可塑性 |
| InDels | 3 | 3 | 泛基因组与作物改良、群体遗传与选择信号、转座子与基因组可塑性 |
| OsNAC14 | 3 | 3 | 群体遗传与选择信号、转座子与基因组可塑性、进化发育与性状起源 |
| TriFAs | 3 | 3 | 泛基因组与作物改良、群体遗传与选择信号、转座子与基因组可塑性 |
| rhAmpSeq | 2 | 4 | 基因组组装与注释、转座子与基因组可塑性 |
| HAC1 | 2 | 3 | 泛基因组与作物改良、群体遗传与选择信号 |

| 化合物 | 命中子主题数 | 证据条数 | 涉及子主题 |
|---|---|---|---|
| flavonoid | 4 | 5 | 泛基因组与作物改良、群体遗传与选择信号、转座子与基因组可塑性、进化发育与性状起源 |
| phenolic | 3 | 3 | 泛基因组与作物改良、群体遗传与选择信号、转座子与基因组可塑性 |
| auxin | 2 | 2 | 群体遗传与选择信号、转座子与基因组可塑性 |
| sucrose | 2 | 2 | 多倍化与亚基因组演化、转座子与基因组可塑性 |

### 3.1 跨子主题受控叙述

- **交叉实体**：HaALS、OsPRTs、AhLOG、MKK3、GlyPDF 等实体在 ≥2 个子主题中重复出现；这只能说明多条研究线指向同一候选，不能说明同一机制（[[b4-ys8H9kH4cFVbPEuMHCg4nA-f5]]；[[b4-ys8H9kH4cFVbPEuMHCg4nA-f7]]）。
- **层级不均**：因果层证据在子主题间分布不均，最高为“转座子与基因组可塑性”（15 条），最低为“基因组组装与注释”（0 条）；跨子主题比较结论强度前须先对齐这一差异。
- **共同缺口**：七类证据齐全，瓶颈是同一结论的独立复现与条件分层，而非证据类型。

## 4. 研究设计缺口矩阵（子主题 × 证据类型）

> 单元格为证据条数，`—` 表示该组合在本主题无证据。最后一列之后按行读：一行里若前三列全为 `—`，该子主题**没有任何因果层证据**。

| 子主题 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 |
|---|---|---|---|---|---|---|---|
| 基因组组装与注释 | — | — | — | 1 | 9 | 1 | 16 |
| 比较基因组与共线性 | — | — | — | 1 | — | — | 13 |
| 群体遗传与选择信号 | — | — | — | 2 | 33 | 1 | 71 |
| 多倍化与亚基因组演化 | — | — | — | 1 | 3 | 2 | 26 |
| 转座子与基因组可塑性 | 5 | 8 | 2 | 10 | 67 | 11 | 313 |
| 进化发育与性状起源 | — | 1 | — | — | — | — | 53 |
| 泛基因组与作物改良 | — | — | — | 2 | 11 | — | 52 |

**零因果层子主题（5/7）**：基因组组装与注释、比较基因组与共线性、群体遗传与选择信号、多倍化与亚基因组演化、泛基因组与作物改良。

这些子主题目前只能产出相关性假说；若研究方案把它们写成“X 调控 Y”，属于超越证据的表达，须在方案中降级为待验证命题。

## 5. 可直接引用的因果级证据（自动筛选）

以下 15 条证据的实验设计属于扰动或直接互作，可作为机制论断的一手依据；引用时须核对原文的物种、组织与处理条件。

| 证据页 | DOI | 类型 | 断言（摘录） |
|---|---|---|---|
| [[daily-40523045-f3]] | `10.1080/21645698.2025.2510715` | protein interaction | This domain enables bZIP transcription factors to specifically recognize and bind to particular DNA sequences, thereby r… |
| [[daily-41829717-f5]] | `10.3390/plants15050685` | protein interaction | The eukaryotic translation initiation factor 4E (eIF4E) interacts with viral genomic RNA to facilitate viral RNA transla… |
| [[daily-42137983-f1]] | `10.1093/nar/gkag476` | genetic perturbation | Using custom-made antibodies specific to the rice H2A.X variant, we show that it repressed the deposition of active H3K4… |
| [[daily-42243690-f4]] | `10.1186/s12870-026-09148-8` | protein interaction | The phylogenetic patterns observed in PQS frequency raise the question of what biological machinery might interact with … |
| [[daily-42283811-f1]] | `10.1007/s00248-026-02803-5` | protein interaction | ICE dynamics in these bacteria often interact with other components of the mobilome, including plasmids and genomic isla… |
| [[daily-42384783-f1]] | `10.1126/sciadv.aeg6081` | DNA binding/regulation | Using an integrated approach combining biosynthetic pathway elucidation, regulatory mechanism dissection, evolutionary a… |
| [[daily-42413033-f7]] | `10.1093/plphys/kiag473` | protein interaction | TFs are DNA-binding proteins that can selectively bind to cis-regulatory elements (CREs) in the genome based on sequence… |
| [[daily-42429570-f5]] | `10.1128/spectrum.00381-26` | genetic perturbation | The inability to recover escape mutants further suggests that systems like DRT11 may target infection steps that are bot… |
| [[daily-42514495-f3]] | `10.3390/plants15142127` | DNA binding/regulation | Recent genome-wide binding analysis via ChIP-seq has further verified that the STM protein can directly bind to the prom… |
| [[daily-42514528-f2]] | `10.3390/plants15142160` | protein interaction | It binds to the expression product of VirA, activating other Vir genes, resulting in the cleavage, transfer, and eventua… |
| [[daily-42670212-f3]] | `10.1111/pbi.70748` | protein interaction | In contrast to the hQTL Integrated_GY_hQTL121 on chromosome 4A which interacts with many regions across the genome, the … |
| [[daily-42713468-f7]] | `10.3389/fpls.2026.1902159` | genetic perturbation | Compared with conventional CRISPR/Cas9-mediated editing, PE substantially reduces the risk of large genomic rearrangemen… |
| [[ms-10-1371_journal-pgen-1012287-f7]] | `10.1371/journal.pgen.1012287` | protein interaction | At the start of this circuit, the transcription factor proteins Circadian Locomotor Output Cycles Kaput (Clock) and Aryl… |
| [[multiomicsdriven-advances-in-the-understanding-of-f6]] | `10.1111/tpj.16545` | genetic perturbation | Homozygous mutations in single and/or double allele(s) of GmFAD2-1A and GmFAD2-1B in soybean, which are created by trans… |
| [[ref-science-1086391-f3]] | `10.1126/science.1086391` | genetic perturbation | Although there were no effects of G C content on T-DNA integration sites observed at the genome scale, we found a positi… |

## 6. 证据间的张力与矛盾（自动筛查）

未筛查到方向相反的表述。注意：这**不等于**结论一致——多数证据只报告单一方向的观察，缺少反证不等于已被重复验证。

## 7. 覆盖与代表性缺口

- **因果级证据占比仅 2.9%**：机制结论的可信度受限于此，建议对排名靠前的子主题定向补做扰动实验或查找已有突变体表型数据。
- **5 个子主题完全没有因果层证据**（基因组组装与注释、比较基因组与共线性、群体遗传与选择信号、多倍化与亚基因组演化…）：这些方向目前只能写相关性。
- **单篇证据物种 7 个**（Pyrus spp.、Spinacia oleracea、Salvia miltiorrhiza、Azolla、Ficus carica…）：跨物种外推缺乏支撑。
- **53 条证据（10%）未命中任何子主题**：说明子主题词表覆盖不足，这部分证据目前无法进入结构性讨论。
- **证据类型以摘要级断言为主**：本知识库对多数文献仅收录摘要/图表级断言，无法支撑实验条件比较与因果推断；全文覆盖率是当前深度的上限约束。
- **文献元数据不全**：论文页 `year` / `journal` 字段覆盖率极低，因此本页不给出发表年份分布，也无法用年份评估时效性；frontmatter 的 `library_papers` 为历史手写值，与 tags 归一化统计相差数倍，**不可引用**。

## 8. 历史正文说明

本页 2026-11-03 之前的正文为人工/LLM 撰写，未与证据逐条对齐，含不可核的行内断言缺引用、格式残留与跨主题内容混入。该正文已原样归档至 `_review/synthesis_legacy_20261107`，保留供追溯，**不得再作为结论来源**。原“与大豆项目关联”的定性判断保留在 frontmatter 的 `soybean_relevance` 字段，其论证过程同样需重新取证。

## 9. 行内引用密度自检

本页正文 4334 个中文字符，行内证据链接 92 处，密度 **10.6 处/500 字**（目标 ≥1）。链接指向证据页，不直接指向出版社；引用前须沿证据页回到原文核对。
