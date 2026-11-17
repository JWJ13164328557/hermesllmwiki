---
title: "Hypotheses: Epigenetics & Gene Regulation"
title_zh: "表观遗传与基因调控：可证伪假说"
type: hypothesis
topic: "epigenetics-gene-regulation"
theme_basis: "tag"
total_evidence: 139
total_papers: 40
total_hypotheses: 3
specificity_domain: 3
specificity_generic: 0
auto_generated: true
generator: "batch_hypotheses.py (evidence-grounded, 2026-11-02)"
updated: 2026-11-03
---

# 💡 Epigenetics & Gene Regulation — 可证伪假说（3 条）

> 生成口径：主题内 139 条证据 / 40 篇独立论文（主题归属依据：证据标签）。
> 每条假说只在"≥3 条证据且 ≥2 篇独立论文"时生成，并附证据 ID 与证伪条件。
> 本页是**机器生成的候选清单**，不是经同行评议的结论；引用前须回原文核对。

## 主题覆盖概览

| 项目 | 值 |
|---|---|
| 主题 | Epigenetics & Gene Regulation |
| 证据条目 | 139 |
| 独立论文 | 40 |
| 生成假说 | 3 |
| 其中主题专用方案 | 3 |
| 其中缺省回退方案（需改写） | 0 |
| 主题归属依据 | 证据标签 |

### H1：GCN5 → 根生长（共同上游排除）

**假说**：GCN5 与根生长在本主题的多项研究中被同时报道，但二者目前只是表达层面的共变。判别性检验：阻断 GCN5，看根生长是否随之改变，而非二者共受上游驱动。

**为什么值得做（证据缺口）**

- 全部支撑证据来自单一物种（Arabidopsis thaliana），跨物种保守性未知
- 仅 2 篇独立论文支撑，复现性未经第三方验证
- 现有证据以表达/关联为主，缺少遗传操纵的因果证据
- 缺少蛋白—DNA 或蛋白—蛋白互作证据，调控是直接还是间接未知
- 缺少细胞类型/空间分辨率，无法判定效应发生在哪类细胞

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 同组织、同发育期的染色质图谱 + 转录组，生物学重复 >=2 |
| 操纵或比较变量 | 目标因子扰动（敲除/诱导降解）或修饰酶抑制剂 |
| 对照 | 输入对照（input/IgG）与非靶向对照 sgRNA |
| 读出 | 峰质量与分布、差异可及性、H3K27me3/H3K4me3 富集、靶基因表达（至少两项独立读出交叉验证） |
| 若假说为真 | 阻断 GCN5 后根生长发生可测变化，而共同上游因子的活性或丰度未同步改变 |
| 若假说为假 | 阻断 GCN5 后根生长不变，或共同上游因子改变时两者同步变化（提示平行而非上下游） |

**证据基础**：5 条证据 / 2 篇独立论文（置信度：低）
- `ref-j-bbrc-2016-12-086-f2`
- `ref-s42003-019-0646-5-f2`
- `ref-j-bbrc-2016-12-086-f1`
- `ref-j-bbrc-2016-12-086-f5`
- `ref-j-bbrc-2016-12-086-f7`

**领域特异性**：领域特异读出梯度：峰质量与分布、差异可及性、H3K27me3/H3K4me3 富集、靶基因表达

**原始断言（摘自证据页，供核对）**
> Indeed, H3K14 acetylation by GCN5 is mechanistically coupled to H3 serine10 phosphorylation and is required for the expression of a subset of genes in yeast [32,33] 253 In order to evaluate the transcriptional effect of MB-3, we evaluated the expression of several known targets of GCN5 in 12 days-old seedlings durin…
> <sub>来源：`ref-j-bbrc-2016-12-086-f2`</sub>


### H2：HDA6 → 非生物胁迫响应（共同上游排除）

**假说**：HDA6 与非生物胁迫响应在本主题的多项研究中被同时报道，但二者目前只是表达层面的共变。判别性检验：阻断 HDA6，看非生物胁迫响应是否随之改变，而非二者共受上游驱动。

**为什么值得做（证据缺口）**

- 仅 2 篇独立论文支撑，复现性未经第三方验证
- 现有证据以表达/关联为主，缺少遗传操纵的因果证据
- 缺少细胞类型/空间分辨率，无法判定效应发生在哪类细胞

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 同组织、同发育期的染色质图谱 + 转录组，生物学重复 >=2 |
| 操纵或比较变量 | 目标因子扰动（敲除/诱导降解）或修饰酶抑制剂 |
| 对照 | 输入对照（input/IgG）与非靶向对照 sgRNA |
| 读出 | 峰质量与分布、差异可及性、H3K27me3/H3K4me3 富集、靶基因表达（至少两项独立读出交叉验证） |
| 若假说为真 | 阻断 HDA6 后非生物胁迫响应发生可测变化，而共同上游因子的活性或丰度未同步改变 |
| 若假说为假 | 阻断 HDA6 后非生物胁迫响应不变，或共同上游因子改变时两者同步变化（提示平行而非上下游） |

**证据基础**：4 条证据 / 2 篇独立论文（置信度：低）
- `daily-42968200-f5`
- `ref-erq154-f6`
- `ref-erq154-f1`
- `ref-erq154-f8`

**领域特异性**：领域特异读出梯度：峰质量与分布、差异可及性、H3K27me3/H3K4me3 富集、靶基因表达

**原始断言（摘自证据页，供核对）**
> The histone acetyltransferase IDM1 is required for the DNA demethylase ROS1 to remove DNA methylation in some genomic regions [, ]; histone deacetylase 6 (HDA6) interacts with MET1, which methylates DNA [, ]; alterations in other histone marks (including H3K36me3, H3K27me1, H3K4me3, and H3K27me3) do not have a notab…
> <sub>来源：`daily-42968200-f5`</sub>


### H3：MYB（家族冗余）

**假说**：MYB家族在本主题内有 2 个成员（MYB36、MYB44）分别被提名参与同一过程；在 6 条相关证据中仅 0 条涉及双/多突变，家族内功能冗余与剂量补偿因此未被定量刻画（受检索覆盖限制，需系统检索复核）。判别性检验：构建双突变与三突变体，比较单突变与多突变的表型强度，并测定单突变体中同源成员的表达补偿。

**为什么值得做（证据缺口）**

- 成员证据分散在不同论文，6 条中仅 0 条做过双/多突变
- 家族成员间的表达补偿缺少同遗传背景下的并行测定

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 原报道物种，同遗传背景、同生育期 |
| 操纵或比较变量 | 家族成员的敲除/敲低，单突变 vs 双/多突变 |
| 读出 | 定量表型效应量与同源成员表达水平 |
| 若假说为真 | 多突变体表型显著强于单突变，且单突变体中同源成员表达上调（补偿成立） |
| 若假说为假 | 多突变体与单突变表型相当、同源成员表达不变，说明成员功能已分化 |

**证据基础**：6 条证据 / 2 篇独立论文（置信度：低）
- `ref-journal-pgen-1010473-f3`
- `ref-journal-pgen-1010473-f2`
- `ref-journal-pgen-1010473-f1`
- `ref-Chapter-Three---Defining-the-P-f5`
- `ref-journal-pgen-1010473-f8`
- `ref-journal-pgen-1010473-f6`

**领域特异性**：领域特异读出梯度：峰质量与分布、差异可及性、H3K27me3/H3K4me3 富集、靶基因表达

**原始断言（摘自证据页，供核对）**
> In the presence of drought stress, the upregulation of MYB44 and the downregulation of HDT4 lead to an elevation of histone acetylation and therefore the activation of target gene expression.
> <sub>来源：`ref-journal-pgen-1010473-f3`</sub>





## 使用方式

1. 先按"证据缺口"排序：单一物种、单篇论文、缺因果证据的假说优先补验证；
2. 每条假说的"若假说为假"一栏即为**止损条件**，实验设计阶段就应确定样本量；
3. 证据 ID 可直接在 `evidence/` 下打开原文摘要核对，禁止跳过核对直接引用。

---
*由 Phase 8 生成于 2026-11-03；生成器版本 2026-11-02-evidence-grounded*
