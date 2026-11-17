---
title: "Hypotheses: Genomics & Evolution"
title_zh: "基因组学与演化：可证伪假说"
type: hypothesis
topic: "genomics-evolution"
theme_basis: "tag"
total_evidence: 15
total_papers: 11
total_hypotheses: 1
specificity_domain: 1
specificity_generic: 0
auto_generated: true
generator: "batch_hypotheses.py (evidence-grounded, 2026-11-02)"
updated: 2026-11-03
---

# 💡 Genomics & Evolution — 可证伪假说（1 条）

> 生成口径：主题内 15 条证据 / 11 篇独立论文（主题归属依据：证据标签）。
> 每条假说只在"≥3 条证据且 ≥2 篇独立论文"时生成，并附证据 ID 与证伪条件。
> 本页是**机器生成的候选清单**，不是经同行评议的结论；引用前须回原文核对。

## 主题覆盖概览

| 项目 | 值 |
|---|---|
| 主题 | Genomics & Evolution |
| 证据条目 | 15 |
| 独立论文 | 11 |
| 生成假说 | 1 |
| 其中主题专用方案 | 1 |
| 其中缺省回退方案（需改写） | 0 |
| 主题归属依据 | 证据标签 |

### H1：组装连续性

**假说**：本主题 5 篇论文的组装相关结论依赖各自的组装版本；6 条相关证据中仅 0 条对组装连续性本身做过敏感性分析。把同一份染色体级组装人工打断到 contig 级后，基因家族拷贝数、共线性区块与旁系同源分组是否稳定，现有文献无法判定（受检索覆盖限制，需系统检索复核）。判别性检验：对同一组装做梯度碎片化，重跑注释与家族推断，比较结论。

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

**证据基础**：6 条证据 / 5 篇独立论文（置信度：中）
- `full-length-sequencing-of-ginkgo-biloba-l-f1`
- `elucidation-of-the-biochemical-pathways-involved-f3`
- `ms-10-1038_s41467-026-76979-2-f1`
- `the-first-chromosome-level-fallopia-multiflora-genome-f3`
- `elucidation-of-the-biochemical-pathways-involved-f1`
- `ref-s41589-023-01327-0-f1`

**领域特异性**：领域特异读出梯度：contig NG50/BUSCO/LAI、共线性区块、Fst/pi/Tajima D、分化时间（本条正文命中：组装连续性、共线性、拷贝数）

**原始断言（摘自证据页，供核对）**
> Here, we report a chromosome-level genome assembly of Streptochaeta spicata, which represents the lineage without typical spikelets and the sister to the rest of Poaceae, and perform comparative genomic analyses across major grass lineages.
> <sub>来源：`ms-10-1038_s41467-026-76979-2-f1`</sub>



## 证据不足声明（自动判定，不是敷衍）

本主题当前只能支撑 **1 条**可证伪假说（目标 3 条）。脚本不会为了凑数而降低门槛，因此如实报告缺口：

| 项目 | 值 |
|---|---|
| 主题内证据 | 15 |
| 独立论文 | 11 |
| 形成的证据簇 | 0 |
| 最大簇规模 | 0 |

### 为什么会出现这种局面

本主题证据中 `evidence_type` 高度集中于表达/关联类断言，且同一机制的证据分散在不同论文的不同表述里，缺少"同一基因 × 同一表型"的重复测量。要生成更多假说，缺的不是算法，而是**可比的重复证据**。

### 补齐证据的具体做法（可直接落到检索式）

1. 对每个候选机制追加检索式：`"<基因名>" AND ("mutant" OR "knockout" OR "overexpression" OR "CRISPR")`，把表达关联升级为遗传证据；
2. 强制要求同一机制至少 2 篇独立论文（不同实验室或不同物种）；
3. 方法学/工具类主题应改按"工具名 + benchmark + comparison"检索，而不是按生物学关键词，否则会把大量表达研究误并入该主题；
4. 补采后在下一轮自动重算；本页会随证据增长自动升级。


## 使用方式

1. 先按"证据缺口"排序：单一物种、单篇论文、缺因果证据的假说优先补验证；
2. 每条假说的"若假说为假"一栏即为**止损条件**，实验设计阶段就应确定样本量；
3. 证据 ID 可直接在 `evidence/` 下打开原文摘要核对，禁止跳过核对直接引用。

---
*由 Phase 8 生成于 2026-11-03；生成器版本 2026-11-02-evidence-grounded*
