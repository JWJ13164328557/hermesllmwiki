---

title: "发育生物学 — Synthesis"
created: 2026-06-01
total_evidence: 224
total_papers: 48
library_papers: 779  # 全库按themes归类该主题文献数
type: synthesis
body_status: rebuilt-2026-11-03
tags: [synthesis, development]


soybean_relevance: ⭐高
legacy_archive: _review/synthesis_legacy_20261103/developmental-biology.md
rebuild_rule: evidence-fields-only; no-cross-evidence-inference

---
# 植物发育生物学 知识综合（证据重建版）

<!-- AUTO-EVIDENCE-STRENGTH:START -->

## 证据覆盖与强度（自动统计，可复算）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据条目 | 224 | 本主题归属的证据对象数 |
| 独立论文 | 48 | 去重后的 PMID/DOI 数 |
| 平均每篇证据数 | 4.67 | <1.0 说明多数论文只贡献 1 条结论 |
| 单条证据论文占比 | 25% | 越高说明"每篇论文一个结论"，系统性弱 |
| 主要物种 | Arabidopsis thaliana(186)、Oryza sativa(95)、Zea mays(73)、Nicotiana tabacum(44)、Citrus spp.(32)、Solanum lycopersicum(21) | 物种过度集中则外推性受限 |
| 证据类型 | expression/regulation 172；protein interaction 21；genetic perturbation 19；DNA binding/regulation 6；omics/co-occurrence 5；phenotypic/association 1 | 表达/关联类居多时，因果结论需打折扣 |

> 归属依据：`themes.py` 标签别名表（高置信）+ 关键词兜底（低置信）。本段由脚本生成，不构成结论；结论性文字须回原文核对。

### 可复核证据索引（前 12 条，按断言长度）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `ref-s13007-019-0417-9-f4` | 10.1186/s13007-019-0417-9 | Focusing on the TA zone data (positions 2–15), we found significant differences in tissue- |
| `ref-s13059-021-02537-2-f5` | 10.1186/s13059-021-02537-2 | We found that the suberin biosynthetic gene, ASFT (ALIPHATIC SUBERIN FERULOYL TRANSFERASE) |
| `ref-j-molp-2026-03-005-f3` | 10.1016/j.molp.2026.03.005 | Molecular Plant 19, 1019–1035, May 4 2026 1021 WIND1 controls cell fate transition Molecul |
| `ref-tab-0120-f2` | 10.1199/tab.0120 | Overexpression of CDC6 or CDT1, E2F targets encoding subunits of the pre-replication compl |
| `ref-s41586-018-0839-y-f2` | 10.1038/s41586-018-0839-y | Our data establish that during root procambial development there exists a network in which |
| `ref-15592324-2020-1820681-f1` | 10.1080/15592324.2020.1820681 | Combination of 0.5 µM TSA and 200 µM SB had no apparent effect on wheat regeneration effic |
| `ms-10-3390_cells15121049-f1` | 10.3390/cells15121049 | The sex-specific maternally or paternally inherited DNA marks at imprinted genes are essen |
| `ref-j-pbi-2019-09-003-f2` | 10.1016/j.pbi.2019.09.003 | CYCD6;1 is required for the division of cortex/endodermis initial cells and their progenit |
| `ref-science-1146265-f1` | 10.1126/science.1146265 | With a computational pipeline we developed to analyze this immense data set, we show the o |
| `ref-ppl-13651-f2` | 10.1111/ppl.13651 | The role of ROS, particularly in signal transduction under drought stress, is well studied |
| `ref-j-pbi-2011-10-008-f7` | 10.1016/j.pbi.2011.10.008 | Function of WUS in stem cell homeostasis: molecular perspective WUS-mediated transcription |
| `ref-j-tig-2017-05-002-f6` | 10.1016/j.tig.2017.05.002 | While it has been shown that SHR-SCR can bind to JACKDAW and MAGPIE (and may be required t |

### 证据语义分层

| 证据类型 | 条目数 | 可支持的推断强度 |
|---|---:|---|
| genetic perturbation | 19 | 遗传因果（扰动后表型/表达改变） |
| protein interaction | 21 | 物理互作（Co-IP/Y2H/BiFC/pull-down） |
| DNA binding/regulation | 6 | 直接调控（ChIP/EMSA/启动子报告） |
| expression/regulation | 172 | 表达相关（转录组/qPCR，不能单独推因果） |
| phenotypic/association | 1 | 表型关联（GWAS/QTL/自然变异/田间） |
| omics/co-occurrence | 5 | 组学共现（单细胞簇/共表达网络，非调控） |

> 读法：`genetic perturbation` 才是因果证据；`expression/regulation` 与 `omics/co-occurrence` 只能提出假说，不能证明调控或因果。

### 遗传扰动类证据（关键词命中，前 5 条；需回原文核实实验设计）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `ref-tab-0120-f2` | 10.1199/tab.0120 | Overexpression of CDC6 or CDT1, E2F targets encoding subunits of the pre-replication complex are suf |
| `ref-ppl-13651-f3` | 10.1111/ppl.13651 | The coexpression network analysis between OsERF48 and root-specific overexpression of ERF48 root RNA |
| `ref-nrm3790-f4` | 10.1038/nrm3790 | Inducible overexpression of PLT1 or PLT2 is sufficient for the formation of ectopic root stem cell n |
| `ref-pnas-2201350119-f8` | 10.1073/pnas.2201350119 | Consistent with this, our transcriptome analysis identified that ROS homeostasis and cell wall-modif |
| `ref-j-pbi-2013-11-011-f1` | 10.1016/j.pbi.2013.11.011 | Expression of both PIN1 and DR5 diminishes in lfy mutant floral primordia, increases after inducible |

### 正文状态

> 本页子主题正文为历史人工/LLM 文本，**未由本次证据重建**；只有本自动段与 frontmatter 计数反映当前证据快照。正文中的机制性表述须逐条回到原始研究核对，不得仅凭本页引用。

<!-- AUTO-EVIDENCE-STRENGTH:END -->

> 本页正文于 2026-11-03 由 `rebuild_synthesis_body.py` 从 **224 条证据对象 / 48 篇文献**确定性重建：所有陈述均可回溯到下列证据页；英文为原文摘录，未经改写；不含跨证据的推测性归纳。历史人工正文已归档至 `_review/synthesis_legacy_20261103`，不再作为本页结论来源。
>
> 阅读约定：`遗传扰动` / `蛋白互作` / `DNA 结合` 三类证据才支持“因果”或“直接调控”的表述；`表达相关` 与 `组学共现` 只能提出关联性假说。

## 1. 主题概览（自动统计）

| 指标 | 值 |
|---|---|
| 证据对象 | 224 |
| 独立文献（DOI/PMID 去重） | 48 |
| 平均每篇证据数 | 4.67 |
| 证据类型构成 | expression/regulation(172)、protein interaction(21)、genetic perturbation(19)、DNA binding/regulation(6)、omics/co-occurrence(5)、phenotypic/association(1) |
| 主要物种 | Arabidopsis thaliana(186)、Oryza sativa(95)、Zea mays(73)、Nicotiana tabacum(44)、Citrus spp.(32)、Solanum lycopersicum(21) |
| 子主题覆盖 | 7 个（其中证据 <5 条的 1 个） |

因果级证据共 **46 条**，占本主题证据的 **20.5%**。这一比例决定本主题哪些结论可以写成机制，哪些只能写成相关性。

## 2. 子主题分解（按证据重建）

> 一条证据可同时命中多个子主题（共 32 条跨组），因此各子主题计数之和大于总证据数。

### 2.1 分生组织维持与干细胞稳态

**规模**：40 条证据 / 21 篇文献。**证据构成**：expression/regulation(32)、protein interaction(3)、genetic perturbation(3)、phenotypic/association(1)、DNA binding/regulation(1)。

**形态判断**：以表达相关为主（80%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：含 7 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 33 条仅支持关联。

**主要物种**：Arabidopsis thaliana(37)、Oryza sativa(18)、Citrus spp.(14)、Solanum lycopersicum(10)、Zea mays(9)。

**代表断言（原文摘录，未改写）**

- “Inducible overexpression of PLT1 or PLT2 is sufficient for the formation of ectopic root stem cell niches106,107, which indicates that the auxin–PLT/BBM readout provides a mechanis…” — [[ref-nrm3790-f4]]（`10.1038/nrm3790`，genetic perturbation）
- “This genetic pathway de®nes a mechanism for differentiating between stem cells and organ founder cells within the shoot apical meristem and demonstrates that genes expressed in org…” — [[ref-35050091-f5]]（`10.1038/35050091`，protein interaction）
- “It has been found that the RBR-E2F-CYCD pathway is crucial for maintaining root stem cells since removal of RBR in root meristems or CYCD overexpression more but not faster dividin…” — [[ref-j-pbi-2009-11-001-f2]]（`10.1016/j.pbi.2009.11.001`，genetic perturbation）

### 2.2 细胞分裂与细胞周期

**规模**：12 条证据 / 4 篇文献。**证据构成**：expression/regulation(9)、genetic perturbation(2)、protein interaction(1)。

**形态判断**：以表达相关为主（75%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：含 3 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 9 条仅支持关联。

**主要物种**：Nicotiana tabacum(8)、Arabidopsis thaliana(7)、Solanum lycopersicum(5)、Zea mays(5)、Oryza sativa(3)。

**代表断言（原文摘录，未改写）**

- “Overexpression of CDC6 or CDT1, E2F targets encoding subunits of the pre-replication complex are sufficient to increase ploidy level in trichomes (Castellano et al., 2001; Castella…” — [[ref-tab-0120-f2]]（`10.1199/tab.0120`，genetic perturbation）
- “Since RBR regulates E2F and is itself a well-known target of CDK-cyclin D activity (Figure 2), the question for the molecular origin of differentiation defects extends to CYCD or E…” — [[ref-j-pbi-2009-11-001-f6]]（`10.1016/j.pbi.2009.11.001`，genetic perturbation）
- “We found that the cell cycle was indeed sped up in the presence of light, with a median of 12.57 h in the TA zone (Additional file 16), showing that the on-stage growth system allo…” — [[ref-s13007-019-0417-9-f5]]（`10.1186/s13007-019-0417-9`，expression/regulation）

### 2.3 细胞命运决定与分化

**规模**：30 条证据 / 20 篇文献。**证据构成**：expression/regulation(27)、protein interaction(1)、genetic perturbation(1)、phenotypic/association(1)。

**形态判断**：以表达相关为主（90%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：含 2 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 28 条仅支持关联。

**主要物种**：Arabidopsis thaliana(26)、Oryza sativa(10)、Zea mays(9)、Populus(5)、Solanum lycopersicum(4)。

**代表断言（原文摘录，未改写）**

- “This genetic pathway de®nes a mechanism for differentiating between stem cells and organ founder cells within the shoot apical meristem and demonstrates that genes expressed in org…” — [[ref-35050091-f5]]（`10.1038/35050091`，protein interaction）
- “Since RBR regulates E2F and is itself a well-known target of CDK-cyclin D activity (Figure 2), the question for the molecular origin of differentiation defects extends to CYCD or E…” — [[ref-j-pbi-2009-11-001-f6]]（`10.1016/j.pbi.2009.11.001`，genetic perturbation）
- “Molecular Plant 19, 1019–1035, May 4 2026 1021 WIND1 controls cell fate transition Molecular Plant Notably, XVE:WIND1 seedlings continued to form true leaves around the shoot apica…” — [[ref-j-molp-2026-03-005-f3]]（`10.1016/j.molp.2026.03.005`，expression/regulation）

### 2.4 器官发生与形态建成

**规模**：21 条证据 / 17 篇文献。**证据构成**：expression/regulation(16)、genetic perturbation(3)、protein interaction(2)。

**形态判断**：以表达相关为主（76%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：含 5 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 16 条仅支持关联。

**主要物种**：Arabidopsis thaliana(17)、Oryza sativa(10)、Citrus spp.(7)、Zea mays(6)、Solanum lycopersicum(4)。

**代表断言（原文摘录，未改写）**

- “Overexpression of CDC6 or CDT1, E2F targets encoding subunits of the pre-replication complex are sufficient to increase ploidy level in trichomes (Castellano et al., 2001; Castella…” — [[ref-tab-0120-f2]]（`10.1199/tab.0120`，genetic perturbation）
- “The coexpression network analysis between OsERF48 and root-specific overexpression of ERF48 root RNA-seq data showed that calmodulinlike protein genes, OsCML16, is a direct target …” — [[ref-ppl-13651-f3]]（`10.1111/ppl.13651`，genetic perturbation）
- “This genetic pathway de®nes a mechanism for differentiating between stem cells and organ founder cells within the shoot apical meristem and demonstrates that genes expressed in org…” — [[ref-35050091-f5]]（`10.1038/35050091`，protein interaction）

### 2.5 激素与发育信号整合

**规模**：25 条证据 / 17 篇文献。**证据构成**：expression/regulation(18)、genetic perturbation(3)、protein interaction(2)、DNA binding/regulation(2)。

**形态判断**：以表达相关为主（72%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：含 7 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 18 条仅支持关联。

**主要物种**：Arabidopsis thaliana(25)、Oryza sativa(10)、Zea mays(5)、Citrus spp.(5)、Nicotiana tabacum(4)。

**代表断言（原文摘录，未改写）**

- “Inducible overexpression of PLT1 or PLT2 is sufficient for the formation of ectopic root stem cell niches106,107, which indicates that the auxin–PLT/BBM readout provides a mechanis…” — [[ref-nrm3790-f4]]（`10.1038/nrm3790`，genetic perturbation）
- “3.4 / Ethylene interacts with ABA signaling to regulate RSA Evidently, ethylene is produced in response to multiple abiotic and biotic stresses, suggesting it acts as a bridge betw…” — [[ref-ppl-13651-f1]]（`10.1111/ppl.13651`，protein interaction）
- “Remarkably, CYCD3;1 appears to be also the target of cytokinin signaling and triple mutants for all three CYCD3 subfamily members in Arabidopsis showed a reduced shoot branching re…” — [[ref-j-pbi-2009-11-001-f1]]（`10.1016/j.pbi.2009.11.001`，genetic perturbation）

### 2.6 表观调控与发育可塑性

**规模**：4 条证据 / 4 篇文献。**证据构成**：expression/regulation(3)、protein interaction(1)。

**形态判断**：以表达相关为主（75%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：含 1 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 3 条仅支持关联。

**主要物种**：Arabidopsis thaliana(4)、Solanum lycopersicum(1)、Petunia hybrida(1)、Oryza sativa(1)、Nicotiana tabacum(1)。

**代表断言（原文摘录，未改写）**

- “[1] use chromatin immunoprecipitation and electrophoretic mobility shift experiments to show that the ARR1 protein interacts with the SHY2 promoter in vivo and with a GATC-containi…” — [[ref-gb-2009-10-2-210-f2]]（`10.1186/gb-2009-10-2-210`，protein interaction）
- “Consistent with a role in transcriptional repression, tpl-1 was suppressed by mutation of HAG1 (histone acetyltransferase, HAT, which promotes expression of target genes) and enhan…” — [[ref-j-pbi-2007-07-001-f6]]（`10.1016/j.pbi.2007.07.001`，expression/regulation）
- “However, while the developmental plasticity of plant cells has been demonstrated 1 , it is not known whether the stem cell niche is required for organogenesis.” — [[ref-nature07597-f3]]（`10.1038/nature07597`，expression/regulation）

### 2.7 再生与愈伤组织形成

**规模**：11 条证据 / 8 篇文献。**证据构成**：expression/regulation(10)、protein interaction(1)。

**形态判断**：以表达相关为主（91%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：含 1 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 10 条仅支持关联。

**主要物种**：Arabidopsis thaliana(9)、Zea mays(3)、Oryza sativa(3)、Ficus carica(2)、Solanum lycopersicum(2)。

**代表断言（原文摘录，未改写）**

- “Applied Biological Chemistry (2026) 69:32 ​Introduction Human dermal papilla cells (hDPCs) play a pivotal role in hair follicle morphogenesis and cyclic regeneration by regulating …” — [[ms-10-1186_s13765-026-01102-4-f3]]（`10.1186/s13765-026-01102-4`，protein interaction）
- “Combination of 0.5 µM TSA and 200 µM SB had no apparent effect on wheat regeneration efficiency According to the above experiment data, we found that 0.5 µM TSA increased the embry…” — [[ref-15592324-2020-1820681-f1]]（`10.1080/15592324.2020.1820681`，expression/regulation）
- “Using a root-tip regeneration system in Arabidopsis to track the molecular and functional recovery of cell fates, we show that re-specification of lost cell identities begins withi…” — [[ref-nature07597-f1]]（`10.1038/nature07597`，expression/regulation）

## 3. 可直接引用的因果级证据（自动筛选）

以下 46 条证据的实验设计属于扰动或直接互作，可作为机制论断的一手依据；引用时须核对原文的物种、组织与处理条件。

| 证据页 | DOI | 类型 | 断言（摘录） |
|---|---|---|---|
| [[ms-10-1186_s13765-026-01102-4-f3]] | `10.1186/s13765-026-01102-4` | protein interaction | Applied Biological Chemistry (2026) 69:32 ​Introduction Human dermal papilla cells (hDPCs) play a pivotal role in hair f… |
| [[ref-35050091-f1]] | `10.1038/35050091` | protein interaction | In contrast, several other genes known to interact with STM, including the CLV genes, WUS and CUC2 (refs 23, 24, 25), ar… |
| [[ref-35050091-f2]] | `10.1038/35050091` | genetic perturbation | Here we show that the Arabidopsis mutant asymmetric leaves1 (as1) disrupts this process. |
| [[ref-35050091-f3]] | `10.1038/35050091` | genetic perturbation | Given that the two genes are expressed in complementary domains, and that the expression pattern of STM does not change … |
| [[ref-35050091-f5]] | `10.1038/35050091` | protein interaction | This genetic pathway de®nes a mechanism for differentiating between stem cells and organ founder cells within the shoot … |
| [[ref-gb-2009-10-2-210-f2]] | `10.1186/gb-2009-10-2-210` | protein interaction | [1] use chromatin immunoprecipitation and electrophoretic mobility shift experiments to show that the ARR1 protein inter… |
| [[ref-gb-2009-10-2-210-f3]] | `10.1186/gb-2009-10-2-210` | protein interaction | The SHY2-2 protein does not interact with the auxin receptor http://genomebiology.com/2009/10/2/210 Genome Biology 2009,… |
| [[ref-j-pbi-2007-07-001-f3]] | `10.1016/j.pbi.2007.07.001` | genetic perturbation | Instead, RBR appears to be a downstream target of SCR: RBR expression increased in the scr mutant and loss of RBR rescue… |
| [[ref-j-pbi-2009-11-001-f1]] | `10.1016/j.pbi.2009.11.001` | genetic perturbation | Remarkably, CYCD3;1 appears to be also the target of cytokinin signaling and triple mutants for all three CYCD3 subfamil… |
| [[ref-j-pbi-2009-11-001-f2]] | `10.1016/j.pbi.2009.11.001` | genetic perturbation | It has been found that the RBR-E2F-CYCD pathway is crucial for maintaining root stem cells since removal of RBR in root … |
| [[ref-j-pbi-2009-11-001-f6]] | `10.1016/j.pbi.2009.11.001` | genetic perturbation | Since RBR regulates E2F and is itself a well-known target of CDK-cyclin D activity (Figure 2), the question for the mole… |
| [[ref-j-pbi-2011-10-008-f4]] | `10.1016/j.pbi.2011.10.008` | genetic perturbation | Current Opinion in Plant Biology 2012, 15:10–16 www.sciencedirect.com silencing of ARR7 and ARR15 resulted in an increme… |
| [[ref-j-pbi-2011-10-008-f8]] | `10.1016/j.pbi.2011.10.008` | protein interaction | Protein-protein interaction analysis has demonstrated that c-terminal part of WUS interacts with WD40 domain containing … |
| [[ref-j-pbi-2013-11-011-f1]] | `10.1016/j.pbi.2013.11.011` | genetic perturbation | Expression of both PIN1 and DR5 diminishes in lfy mutant floral primordia, increases after inducible LFY overexpression … |
| [[ref-j-pbi-2013-11-011-f3]] | `10.1016/j.pbi.2013.11.011` | genetic perturbation | The level of miR394, which targets the mRNA of the F-Box protein LCR, is critical for normal leaf development, causing d… |

（另有 31 条未列出，可在 `evidence/` 按 evidence_type 过滤。）

## 4. 张力与矛盾（自动检测）

检测规则：同一基因/蛋白符号在证据中出现方向相反的作用词（激活 vs 抑制、促进 vs 抑制、上调 vs 下调）。命中不等于真实矛盾——可能来自物种、组织或处理条件差异，须回原文核对。

- **CLV3**：regulation direction dispute
  - [[ref-j-pbi-2013-11-011]]
  - [[ref-nrm3790]]
  - [[ref-nrm3790]]

## 5. 覆盖缺口（由证据分布直接导出）

- **证据单薄的子主题 1 个**：表观调控与发育可塑性 4 条（各 <5 条，单篇论文即可左右结论）。
- **未能归入任何子主题的证据 120 条**：多为方法描述或跨领域摘录，已计入主题总量但未参与分组。

## 6. 历史正文说明

本页 2026-11-03 之前的正文为人工/LLM 撰写，未与证据逐条对齐，含不可核的行内断言缺引用、格式残留与跨主题内容混入。该正文已原样归档至 `_review/synthesis_legacy_20261103`，保留供追溯，**不得再作为结论来源**。原“与大豆项目关联”的定性判断保留在 frontmatter 的 `soybean_relevance` 字段，其论证过程同样需重新取证。
