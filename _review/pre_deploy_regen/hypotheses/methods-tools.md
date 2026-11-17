---
title: "Hypotheses: Methods & Tools"
title_zh: "方法与工具：可证伪假说"
type: hypothesis
topic: "methods-tools"
theme_basis: "tag"
total_evidence: 81
total_papers: 31
total_hypotheses: 4
specificity_domain: 4
specificity_generic: 0
auto_generated: true
generator: "batch_hypotheses.py (evidence-grounded, 2026-11-02)"
updated: 2026-11-03
---

# 💡 Methods & Tools — 可证伪假说（4 条）

> 生成口径：主题内 81 条证据 / 31 篇独立论文（主题归属依据：证据标签）。
> 每条假说只在"≥3 条证据且 ≥2 篇独立论文"时生成，并附证据 ID 与证伪条件。
> 本页是**机器生成的候选清单**，不是经同行评议的结论；引用前须回原文核对。

## 主题覆盖概览

| 项目 | 值 |
|---|---|
| 主题 | Methods & Tools |
| 证据条目 | 81 |
| 独立论文 | 31 |
| 生成假说 | 4 |
| 其中主题专用方案 | 4 |
| 其中缺省回退方案（需改写） | 0 |
| 主题归属依据 | 证据标签 |

### H1：差异表达统计（方法敏感性）

**假说**：在差异表达统计组内，limma-voom、DESeq2 都被用于支撑本主题结论，但在本知识库 3 条相关证据中，仅 0 条在同一断言内同时比较了两种以上实现；结论对实现选择的敏感性因此在现有文献中无法判定（受检索覆盖限制，需系统检索复核）。判别性检验：固定输入数据与预处理，只替换实现，比较效应量与显著性排名，并报告实现间分歧。

**为什么值得做（证据缺口）**

- 本主题 3 条证据涉及该组工具，其中 0 条做过多实现对照
- 缺少统一数据与预注册指标，无法区分分歧来自数据还是实现

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 同一输入数据 + 同一预处理，仅替换待比较的实现 |
| 操纵或比较变量 | 实现（唯一变量）：组内各工具/平台版本 |
| 读出 | 效应量、显著性排名、关键对象方向的一致性 |
| 若假说为真 | 两种实现在留出数据上方向一致，关键对象的排名相关性高于预注册阈值 |
| 若假说为假 | 两种实现的关键结论方向相反，或排名相关性低于阈值，说明原结论依赖实现 |

**证据基础**：3 条证据 / 2 篇独立论文（置信度：低）
- `deseq2-lfc-shrinkage`
- `ref-s13059-019-1850-9-f4`
- `ref-s13059-019-1850-9-f3`

**领域特异性**：领域特异读出梯度：基准指标（准确率/F1/AUC）、运行时间与内存、消融前后差值（本条正文命中：版本）

**原始断言（摘自证据页，供核对）**
> Surprisingly, limma had a high score (> 0.99), which is comparable to other leading methods while its performance measured by other metrics was poor.
> <sub>来源：`ref-s13059-019-1850-9-f4`</sub>


### H2：序列比对（方法敏感性）

**假说**：在序列比对组内，STAR、HISAT2、Bowtie2 都被用于支撑本主题结论，但在本知识库 3 条相关证据中，仅 1 条在同一断言内同时比较了两种以上实现；结论对实现选择的敏感性因此在现有文献中无法判定（受检索覆盖限制，需系统检索复核）。判别性检验：固定输入数据与预处理，只替换实现，比较效应量与显著性排名，并报告实现间分歧。

**为什么值得做（证据缺口）**

- 本主题 3 条证据涉及该组工具，其中 1 条做过多实现对照
- 缺少统一数据与预注册指标，无法区分分歧来自数据还是实现

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 同一输入数据 + 同一预处理，仅替换待比较的实现 |
| 操纵或比较变量 | 实现（唯一变量）：组内各工具/平台版本 |
| 读出 | 效应量、显著性排名、关键对象方向的一致性 |
| 若假说为真 | 两种实现在留出数据上方向一致，关键对象的排名相关性高于预注册阈值 |
| 若假说为假 | 两种实现的关键结论方向相反，或排名相关性低于阈值，说明原结论依赖实现 |

**证据基础**：3 条证据 / 3 篇独立论文（置信度：中）
- `ref-s41587-019-0201-4-f2`
- `ref-978-1-4939-3572-7_13-f1`
- `star-speed-50x-faster`

**领域特异性**：领域特异读出梯度：基准指标（准确率/F1/AUC）、运行时间与内存、消融前后差值（本条正文命中：版本）

**原始断言（摘自证据页，供核对）**
> We found that HISAT2 with its Nature Biotechnology | VOL 37 | AUGUST 2019 | 907–915 | www.nature.com/naturebiotechnology 914 Articles NATuRe BIoTecHnoLogy graph genome of common SNPs was able to identify more known SNPs of the NA12878 genome (99.4%) than Bowtie2 and BWA (98.9–99.1%) (Supplementary Note 1 and Supplem…
> <sub>来源：`ref-s41587-019-0201-4-f2`</sub>


### H3：数据整合（方法敏感性）

**假说**：在数据整合组内，Harmony、Seurat CCA/RPCA 都被用于支撑本主题结论，但在本知识库 4 条相关证据中，仅 0 条在同一断言内同时比较了两种以上实现；结论对实现选择的敏感性因此在现有文献中无法判定（受检索覆盖限制，需系统检索复核）。判别性检验：固定输入数据与预处理，只替换实现，比较效应量与显著性排名，并报告实现间分歧。

**为什么值得做（证据缺口）**

- 本主题 4 条证据涉及该组工具，其中 0 条做过多实现对照
- 缺少统一数据与预注册指标，无法区分分歧来自数据还是实现

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 同一输入数据 + 同一预处理，仅替换待比较的实现 |
| 操纵或比较变量 | 实现（唯一变量）：组内各工具/平台版本 |
| 读出 | 效应量、显著性排名、关键对象方向的一致性 |
| 若假说为真 | 两种实现在留出数据上方向一致，关键对象的排名相关性高于预注册阈值 |
| 若假说为假 | 两种实现的关键结论方向相反，或排名相关性低于阈值，说明原结论依赖实现 |

**证据基础**：4 条证据 / 2 篇独立论文（置信度：低）
- `seurat-v2-cca-pbmc-alignment`
- `harmony-pancreatic-islet-integration`
- `harmony-cross-modality-spatial`
- `harmony-scalability`

**领域特异性**：领域特异读出梯度：基准指标（准确率/F1/AUC）、运行时间与内存、消融前后差值（本条正文命中：版本）

**原始断言（摘自证据页，供核对）**
> Harmony integrates scRNA-seq data from five independent pancreatic islet studies (generated with different protocols: inDrop, CEL-Seq2, Smart-seq2, SMARTer, Fluidigm C1) into a unified low-dimensional embedding where cells cluster by cell type rather than by study of origin.
> <sub>来源：`harmony-pancreatic-islet-integration`</sub>


### H4：组装连续性

**假说**：本主题 5 篇论文的组装相关结论依赖各自的组装版本；7 条相关证据中仅 0 条对组装连续性本身做过敏感性分析。把同一份染色体级组装人工打断到 contig 级后，基因家族拷贝数、共线性区块与旁系同源分组是否稳定，现有文献无法判定（受检索覆盖限制，需系统检索复核）。判别性检验：对同一组装做梯度碎片化，重跑注释与家族推断，比较结论。

**为什么值得做（证据缺口）**

- 组装类结论分散在 5 篇论文中，但无统一的碎片化敏感性测试
- 缺少"同一数据、不同连续性"的对照，无法区分生物学信号与组装伪影

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 同一份染色体级组装 + 梯度碎片化版本（contig/scaffold 级） |
| 操纵或比较变量 | 组装连续性（唯一变量），注释与家族推断流程保持不变 |
| 读出 | 基因家族拷贝数、共线性区块数、旁系同源分组的一致性 |
| 若假说为真 | 梯度碎片化后基因家族拷贝数与共线性区块保持稳定，仅边界精度下降 |
| 若假说为假 | 碎片化后拷贝数或共线性结论发生系统性改变，说明原结论依赖组装质量 |

**证据基础**：7 条证据 / 5 篇独立论文（置信度：中）
- `ref-s41576-019-0145-z-f3`
- `ref-btaa997-f1`
- `ref-s41576-019-0145-z-f1`
- `ref-s13059-019-1850-9-f4`
- `ref-s41576-019-0145-z-f6`
- `ref-s11104-023-06301-2-f1`

**领域特异性**：领域特异读出梯度：基准指标（准确率/F1/AUC）、运行时间与内存、消融前后差值（本条正文命中：敏感性分析、版本）

**原始断言（摘自证据页，供核对）**
> B | The 3ʹ end processing complex is composed of four subcomplexes (cleavage and polyadenylation (poly(A)) factor (CPSF), cleavage factor I (CFI), CFII and cleavage stimulation factor (CSTF)), as well as other proteins, many of which interact with the carboxy-terminal domain (CTD) of RNAP II.
> <sub>来源：`ref-s41576-019-0145-z-f3`</sub>





## 使用方式

1. 先按"证据缺口"排序：单一物种、单篇论文、缺因果证据的假说优先补验证；
2. 每条假说的"若假说为假"一栏即为**止损条件**，实验设计阶段就应确定样本量；
3. 证据 ID 可直接在 `evidence/` 下打开原文摘要核对，禁止跳过核对直接引用。

---
*由 Phase 8 生成于 2026-11-03；生成器版本 2026-11-02-evidence-grounded*
