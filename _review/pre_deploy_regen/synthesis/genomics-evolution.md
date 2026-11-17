---

title: "基因组与进化 — Synthesis"
created: 2026-06-01
total_evidence: 15
total_papers: 11
library_papers: 520  # 全库按themes归类该主题文献数
type: synthesis
body_status: rebuilt-2026-11-03
tags: [synthesis, genomics, evolution, genome-assembly, comparative-genomics, GWAS, polyploidization, domestication]


soybean_relevance: ⭐中高
legacy_archive: _review/synthesis_legacy_20261103/genomics-evolution.md
rebuild_rule: evidence-fields-only; no-cross-evidence-inference

---
# 基因组学与演化 知识综合（证据重建版）

<!-- AUTO-EVIDENCE-STRENGTH:START -->

## 证据覆盖与强度（自动统计，可复算）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据条目 | 15 | 本主题归属的证据对象数 |
| 独立论文 | 11 | 去重后的 PMID/DOI 数 |
| 平均每篇证据数 | 1.36 | <1.0 说明多数论文只贡献 1 条结论 |
| 单条证据论文占比 | 64% | 越高说明"每篇论文一个结论"，系统性弱 |
| 主要物种 | Arabidopsis thaliana(8)、Oryza sativa(7)、Ficus carica(3)、Capsicum annuum(2)、Lactuca sativa(2)、Triticum aestivum(2) | 物种过度集中则外推性受限 |
| 证据类型 | expression/regulation 12；phenotypic/association 1；protein interaction 1；omics/co-occurrence 1 | 表达/关联类居多时，因果结论需打折扣 |

> 归属依据：`themes.py` 标签别名表（高置信）+ 关键词兜底（低置信）。本段由脚本生成，不构成结论；结论性文字须回原文核对。

### 可复核证据索引（前 12 条，按断言长度）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `ref-s41589-023-01327-0-f3` | 10.1038/s41589-023-01327-0 | Here we report how state-of-the-art omics methods not only accelerate gene discovery throu |
| `full-length-sequencing-of-ginkgo-biloba-l-f1` | 10.1016/j.indcrop.2021.113714 | Our findings confirm the advantages of SMRT, which facilitated the construction a rich tra |
| `elucidation-of-the-biochemical-pathways-involved-f3` | 10.1016/j.postharvbio.2021.111753 | White bars indicate the positions of QTL mapped from data from trials 5 and 7 for the qRT- |
| `ms-10-1038_s41467-026-76979-2-f1` | 10.1038/s41467-026-76979-2 | Here, we report a chromosome-level genome assembly of Streptochaeta spicata, which represe |
| `the-first-chromosome-level-fallopia-multiflora-genome-f5` | 10.1093/hr/uhad047 | Multiflora remains lagging behind, and the lack of genomic data seriously hinders the cons |
| `ref-gb-2008-9-9-r137-f6` | 10.1186/gb-2008-9-9-r137 | Background The determination of the 'cistrome', the genome-wide set of in vivo cis-element |
| `pdf-pbi-70695-f1` | 10.1111/pbi.70695 | Our work on comparative genomics, including analyses of TE composition, collinearity, orth |
| `the-first-chromosome-level-fallopia-multiflora-genome-f3` | 10.1093/hr/uhad047 | In conclusion, we assembled a high-quality chromosomal-level genome for a member of the fa |
| `ref-pp-19-00943-f6` | 10.1104/pp.19.00943 | APA Conservation The conservation information of APA sites across species is crucial for u |
| `ms-10-5091_plecevo-189916-f3` | 10.5091/plecevo.189916 | Broader phylogenetic analyses with expanded Anatolian sampling are required to clarify the |
| `elucidation-of-the-biochemical-pathways-involved-f1` | 10.1016/j.postharvbio.2021.111753 | QRT-PCR Primers were designed for target transcripts from sequences located on the lettuce |
| `ref-s41589-023-01327-0-f1` | 10.1038/s41589-023-01327-0 | Here we show how a state-of-the-art genome assembly, Hi-C chromosome conformation capture  |

### 证据语义分层

| 证据类型 | 条目数 | 可支持的推断强度 |
|---|---:|---|
| protein interaction | 1 | 物理互作（Co-IP/Y2H/BiFC/pull-down） |
| expression/regulation | 12 | 表达相关（转录组/qPCR，不能单独推因果） |
| phenotypic/association | 1 | 表型关联（GWAS/QTL/自然变异/田间） |
| omics/co-occurrence | 1 | 组学共现（单细胞簇/共表达网络，非调控） |

> 读法：`genetic perturbation` 才是因果证据；`expression/regulation` 与 `omics/co-occurrence` 只能提出假说，不能证明调控或因果。

### 正文状态

> 本页子主题正文为历史人工/LLM 文本，**未由本次证据重建**；只有本自动段与 frontmatter 计数反映当前证据快照。正文中的机制性表述须逐条回到原始研究核对，不得仅凭本页引用。

<!-- AUTO-EVIDENCE-STRENGTH:END -->

> 本页正文于 2026-11-03 由 `rebuild_synthesis_body.py` 从 **15 条证据对象 / 11 篇文献**确定性重建：所有陈述均可回溯到下列证据页；英文为原文摘录，未经改写；不含跨证据的推测性归纳。历史人工正文已归档至 `_review/synthesis_legacy_20261103`，不再作为本页结论来源。
>
> 阅读约定：`遗传扰动` / `蛋白互作` / `DNA 结合` 三类证据才支持“因果”或“直接调控”的表述；`表达相关` 与 `组学共现` 只能提出关联性假说。

## 1. 主题概览（自动统计）

| 指标 | 值 |
|---|---|
| 证据对象 | 15 |
| 独立文献（DOI/PMID 去重） | 11 |
| 平均每篇证据数 | 1.36 |
| 证据类型构成 | expression/regulation(12)、phenotypic/association(1)、protein interaction(1)、omics/co-occurrence(1) |
| 主要物种 | Arabidopsis thaliana(8)、Oryza sativa(7)、Ficus carica(3)、Capsicum annuum(2)、Lactuca sativa(2)、Triticum aestivum(2) |
| 子主题覆盖 | 6 个（其中证据 <5 条的 6 个） |

因果级证据共 **1 条**，占本主题证据的 **6.7%**。这一比例决定本主题哪些结论可以写成机制，哪些只能写成相关性。

## 2. 子主题分解（按证据重建）

> 一条证据可同时命中多个子主题（共 6 条跨组），因此各子主题计数之和大于总证据数。

### 2.1 基因组组装与注释

**规模**：3 条证据 / 3 篇文献。**证据构成**：expression/regulation(2)、omics/co-occurrence(1)。

**形态判断**：以表达相关为主（67%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：本组全部为表达/关联/描述级证据，**不支持因果或直接调控结论**；任何“X 调控 Y”的写法都必须补做扰动实验。

**主要物种**：Arabidopsis thaliana(3)、Triticum aestivum(1)、Citrus spp.(1)、Zea mays(1)、Oryza sativa(1)。

**代表断言（原文摘录，未改写）**

- “Our findings confirm the advantages of SMRT, which facilitated the construction a rich transcript data-set for research on the development of ginkgo seeds, enriching the annotation…” — [[full-length-sequencing-of-ginkgo-biloba-l-f1]]（`10.1016/j.indcrop.2021.113714`，expression/regulation）
- “Here, we report a chromosome-level genome assembly of Streptochaeta spicata, which represents the lineage without typical spikelets and the sister to the rest of Poaceae, and perfo…” — [[ms-10-1038_s41467-026-76979-2-f1]]（`10.1038/s41467-026-76979-2`，expression/regulation）
- “Here we show how a state-of-the-art genome assembly, Hi-C chromosome conformation capture and single-cell transcriptomics datasets empowered discoveries in the C.” — [[ref-s41589-023-01327-0-f1]]（`10.1038/s41589-023-01327-0`，omics/co-occurrence）

### 2.2 比较基因组与共线性

**规模**：3 条证据 / 3 篇文献。**证据构成**：expression/regulation(3)。

**形态判断**：以表达相关为主（100%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：本组全部为表达/关联/描述级证据，**不支持因果或直接调控结论**；任何“X 调控 Y”的写法都必须补做扰动实验。

**主要物种**：Zea mays(2)、Oryza sativa(2)、Arabidopsis thaliana(2)、Plant(1)。

**代表断言（原文摘录，未改写）**

- “Here, we report a chromosome-level genome assembly of Streptochaeta spicata, which represents the lineage without typical spikelets and the sister to the rest of Poaceae, and perfo…” — [[ms-10-1038_s41467-026-76979-2-f1]]（`10.1038/s41467-026-76979-2`，expression/regulation）
- “Our work on comparative genomics, including analyses of TE composition, collinearity, orthologs and phylogenies, strongly reveals an AABBBB subgenome structure derived from ancestr…” — [[pdf-pbi-70695-f1]]（`10.1111/pbi.70695`，expression/regulation）
- “In summary, the phylogenetic classification and synteny analysis are highly consistent and mutually supportive.” — [[ms-10-3389_fpls-2026-1880971-f6]]（`10.3389/fpls.2026.1880971`，expression/regulation）

### 2.3 群体遗传与选择信号

**规模**：1 条证据 / 1 篇文献。**证据构成**：expression/regulation(1)。

**形态判断**：以表达相关为主（100%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：本组全部为表达/关联/描述级证据，**不支持因果或直接调控结论**；任何“X 调控 Y”的写法都必须补做扰动实验。

**主要物种**：Solanum lycopersicum(1)、Oryza sativa(1)、Vitis vinifera(1)。

**代表断言（原文摘录，未改写）**

- “Multiflora remains lagging behind, and the lack of genomic data seriously hinders the construction of the pathway, as genomic data are crucial for advancing our understanding of st…” — [[the-first-chromosome-level-fallopia-multiflora-genome-f5]]（`10.1093/hr/uhad047`，expression/regulation）

### 2.4 多倍化与亚基因组演化

**规模**：2 条证据 / 2 篇文献。**证据构成**：expression/regulation(2)。

**形态判断**：以表达相关为主（100%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：本组全部为表达/关联/描述级证据，**不支持因果或直接调控结论**；任何“X 调控 Y”的写法都必须补做扰动实验。

**主要物种**：Triticum aestivum(1)、Citrus spp.(1)、Ficus carica(1)、Plant(1)。

**代表断言（原文摘录，未改写）**

- “Our work on comparative genomics, including analyses of TE composition, collinearity, orthologs and phylogenies, strongly reveals an AABBBB subgenome structure derived from ancestr…” — [[pdf-pbi-70695-f1]]（`10.1111/pbi.70695`，expression/regulation）
- “Broader phylogenetic analyses with expanded Anatolian sampling are required to clarify the relationships between the two Aegean polyploids and eastern representatives of A.” — [[ms-10-5091_plecevo-189916-f3]]（`10.5091/plecevo.189916`，expression/regulation）

### 2.5 转座子与基因组可塑性

**规模**：14 条证据 / 11 篇文献。**证据构成**：expression/regulation(11)、phenotypic/association(1)、protein interaction(1)、omics/co-occurrence(1)。

**形态判断**：以表达相关为主（79%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：含 1 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 13 条仅支持关联。

**主要物种**：Arabidopsis thaliana(8)、Oryza sativa(6)、Ficus carica(3)、Capsicum annuum(2)、Lactuca sativa(2)。

**代表断言（原文摘录，未改写）**

- “The regulatory role of Pcf11-similar-4 (PCFS4) in Arabidopsis development by genome-wide physical interactions with target loci.” — [[ref-gr-210757-116-f6]]（`10.1101/gr.210757.116`，protein interaction）
- “Here we report how state-of-the-art omics methods not only accelerate gene discovery through the high-resolution spatial resolution of gene expression but also how complementary om…” — [[ref-s41589-023-01327-0-f3]]（`10.1038/s41589-023-01327-0`，expression/regulation）
- “Our findings confirm the advantages of SMRT, which facilitated the construction a rich transcript data-set for research on the development of ginkgo seeds, enriching the annotation…” — [[full-length-sequencing-of-ginkgo-biloba-l-f1]]（`10.1016/j.indcrop.2021.113714`，expression/regulation）

### 2.6 进化发育与性状起源

**规模**：3 条证据 / 3 篇文献。**证据构成**：expression/regulation(3)。

**形态判断**：以表达相关为主（100%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：本组全部为表达/关联/描述级证据，**不支持因果或直接调控结论**；任何“X 调控 Y”的写法都必须补做扰动实验。

**主要物种**：Zea mays(1)、Oryza sativa(1)、Arabidopsis thaliana(1)、Triticum aestivum(1)、Citrus spp.(1)。

**代表断言（原文摘录，未改写）**

- “Our work on comparative genomics, including analyses of TE composition, collinearity, orthologs and phylogenies, strongly reveals an AABBBB subgenome structure derived from ancestr…” — [[pdf-pbi-70695-f1]]（`10.1111/pbi.70695`，expression/regulation）
- “Broader phylogenetic analyses with expanded Anatolian sampling are required to clarify the relationships between the two Aegean polyploids and eastern representatives of A.” — [[ms-10-5091_plecevo-189916-f3]]（`10.5091/plecevo.189916`，expression/regulation）
- “In summary, the phylogenetic classification and synteny analysis are highly consistent and mutually supportive.” — [[ms-10-3389_fpls-2026-1880971-f6]]（`10.3389/fpls.2026.1880971`，expression/regulation）

### 2.7 泛基因组与作物改良

**本知识库当前无归属证据**（子主题已定义但未被任何证据命中）。这是覆盖缺口，不是“该方向不重要”。

## 3. 可直接引用的因果级证据（自动筛选）

以下 1 条证据的实验设计属于扰动或直接互作，可作为机制论断的一手依据；引用时须核对原文的物种、组织与处理条件。

| 证据页 | DOI | 类型 | 断言（摘录） |
|---|---|---|---|
| [[ref-gr-210757-116-f6]] | `10.1101/gr.210757.116` | protein interaction | The regulatory role of Pcf11-similar-4 (PCFS4) in Arabidopsis development by genome-wide physical interactions with targ… |

## 4. 张力与矛盾（自动检测）

在当前证据集上未检出方向性冲突。注意：这只说明“没有互相矛盾的摘录”，不说明领域内不存在争议——多数争议需要全文级的实验条件比对才能发现。

## 5. 覆盖缺口（由证据分布直接导出）

- **未被覆盖的子主题 1 个**：泛基因组与作物改良。这些方向在本库中没有可引用证据，任何涉及它们的论述都必须另行检索。
- **证据单薄的子主题 5 个**：基因组组装与注释 3 条、比较基因组与共线性 3 条、群体遗传与选择信号 1 条、多倍化与亚基因组演化 2 条、进化发育与性状起源 3 条（各 <5 条，单篇论文即可左右结论）。
- **因果级证据占比 6.7%**：机制结论的可信度受限于此，建议对排名靠前的子主题定向补做扰动实验或查找已有突变体表型数据。

## 6. 历史正文说明

本页 2026-11-03 之前的正文为人工/LLM 撰写，未与证据逐条对齐，含不可核的行内断言缺引用、格式残留与跨主题内容混入。该正文已原样归档至 `_review/synthesis_legacy_20261103`，保留供追溯，**不得再作为结论来源**。原“与大豆项目关联”的定性判断保留在 frontmatter 的 `soybean_relevance` 字段，其论证过程同样需重新取证。
