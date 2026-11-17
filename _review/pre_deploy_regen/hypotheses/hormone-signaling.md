---
title: "Hypotheses: Hormone Signalling"
title_zh: "激素与信号转导：可证伪假说"
type: hypothesis
topic: "hormone-signaling"
theme_basis: "tag"
total_evidence: 141
total_papers: 52
total_hypotheses: 5
specificity_domain: 5
specificity_generic: 0
auto_generated: true
generator: "batch_hypotheses.py (evidence-grounded, 2026-11-02)"
updated: 2026-11-03
---

# 💡 Hormone Signalling — 可证伪假说（5 条）

> 生成口径：主题内 141 条证据 / 52 篇独立论文（主题归属依据：证据标签）。
> 每条假说只在"≥3 条证据且 ≥2 篇独立论文"时生成，并附证据 ID 与证伪条件。
> 本页是**机器生成的候选清单**，不是经同行评议的结论；引用前须回原文核对。

## 主题覆盖概览

| 项目 | 值 |
|---|---|
| 主题 | Hormone Signalling |
| 证据条目 | 141 |
| 独立论文 | 52 |
| 生成假说 | 5 |
| 其中主题专用方案 | 5 |
| 其中缺省回退方案（需改写） | 0 |
| 主题归属依据 | 证据标签 |

### H1：BIN2（剂量—效应）

**假说**：BIN2 已有 43 项独立研究；但其中仅 1 条给出不同表达/活性水平的梯度或剂量—响应参数，效应量随水平变化的定量关系无法从现有文献取得（受检索覆盖限制，需系统检索复核）。判别性检验：构建梯度表达系并做定量表型曲线。

**为什么值得做（证据缺口）**

- 现有证据以表达/关联为主，缺少遗传操纵的因果证据
- 缺少细胞类型/空间分辨率，无法判定效应发生在哪类细胞

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 同物种、同生育期突变体与野生型；外源激素处理梯度 |
| 操纵或比较变量 | BIN2 的敲除/敲低、过表达，或受体/激酶活性突变体 |
| 对照 | 野生型 + 空载体；溶剂 mock 处理 |
| 读出 | 激素含量、响应元件驱动报告基因、磷酸化状态、剂量—响应 EC50（至少两项独立读出交叉验证） |
| 若假说为真 | 表型随 BIN2 表达或活性单调变化，半数效应点可在独立实验室复现 |
| 若假说为假 | 表型与表达量无单调关系（阈值型或非单调），提示存在缓冲或旁路 |

**证据基础**：54 条证据 / 43 篇独立论文（置信度：高）
- `dpdf-10-1146-annurev-arplant-083123073106-f11`
- `ms-10-67693_bjcr-3jqlrcre-f7`
- `ms-10-1007_s44372-026-00844-1-f7`
- `gibberellin-biosynthesis-is-required-for-cppu-induced-f2`
- `ref-pnas-0709559105-f3`
- `ms-10-1038_s41467-026-77029-7-f8`

**领域特异性**：领域特异读出梯度：激素含量、响应元件驱动报告基因、磷酸化状态、剂量—响应 EC50（本条正文命中：剂量）

**原始断言（摘自证据页，供核对）**
> Simultaneously, kinases of the shaggylike kinase family such as BRASSINOSTEROID-INSENSITIVE 2 (BIN2, also known as ASK7), which are connected to brassinosteroid (BR) signaling, also target and downregulate SPCH protein (Gudesblat et al., 2012).
> <sub>来源：`ref-jcs-228551-f2`</sub>


### H2：CLV1 → 激素响应（共同上游排除）

**假说**：CLV1 与激素响应在本主题的多项研究中被同时报道，但二者目前只是表达层面的共变。判别性检验：阻断 CLV1，看激素响应是否随之改变，而非二者共受上游驱动。

**为什么值得做（证据缺口）**

- 现有证据以表达/关联为主，缺少遗传操纵的因果证据
- 缺少细胞类型/空间分辨率，无法判定效应发生在哪类细胞

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 同物种、同生育期突变体与野生型；外源激素处理梯度 |
| 操纵或比较变量 | CLV1 的敲除/敲低、过表达，或受体/激酶活性突变体 |
| 对照 | 野生型 + 空载体；溶剂 mock 处理 |
| 读出 | 激素含量、响应元件驱动报告基因、磷酸化状态、剂量—响应 EC50（至少两项独立读出交叉验证） |
| 若假说为真 | 阻断 CLV1 后激素响应发生可测变化，而共同上游因子的活性或丰度未同步改变 |
| 若假说为假 | 阻断 CLV1 后激素响应不变，或共同上游因子改变时两者同步变化（提示平行而非上下游） |

**证据基础**：6 条证据 / 3 篇独立论文（置信度：中）
- `ref-tpc-110-073924-f1`
- `ref-j-pbi-2010-08-001-f1`
- `ref-j-pbi-2010-08-001-f4`
- `10-1146-annurev-arplant-042817-f5`
- `10-1146-annurev-arplant-042817-f6`
- `10-1146-annurev-arplant-042817-f7`

**领域特异性**：领域特异读出梯度：激素含量、响应元件驱动报告基因、磷酸化状态、剂量—响应 EC50

**原始断言（摘自证据页，供核对）**
> CLV3 is active as a 13–amino acid arabinosylated peptide that diffuses until it binds to its receptors: the LRR receptor kinase CLV1, the receptor-like kinase CLV2, and the Ser-Thr kinase CORYNE (Rojo et al., 2002;
> <sub>来源：`ref-tpc-110-073924-f1`</sub>


### H3：ERF（家族冗余）

**假说**：ERF家族在本主题内有 3 个成员（ERF1、ERF109、ERF115）分别被提名参与同一过程；在 6 条相关证据中仅 0 条涉及双/多突变，家族内功能冗余与剂量补偿因此未被定量刻画（受检索覆盖限制，需系统检索复核）。判别性检验：构建双突变与三突变体，比较单突变与多突变的表型强度，并测定单突变体中同源成员的表达补偿。

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

**证据基础**：6 条证据 / 4 篇独立论文（置信度：中）
- `ref-pnas-2003346117-f5`
- `ref-science-1086391-f6`
- `ref-ncomms6833-f1`
- `ref-s41477-019-0408-x-f2`
- `ref-s41477-019-0408-x-f3`
- `ref-s41477-019-0408-x-f7`

**领域特异性**：领域特异读出梯度：激素含量、响应元件驱动报告基因、磷酸化状态、剂量—响应 EC50（本条正文命中：剂量、突变体）

**原始断言（摘自证据页，供核对）**
> Here we show in the root that the major growth hormone auxin is specifically activated in wound-adjacent cells, regulating cell expansion, cell division rates, and regenerationinvolved transcription factor ERF115.
> <sub>来源：`ref-pnas-2003346117-f5`</sub>


### H4：auxin（剂量—效应）

**假说**："auxin" 在本主题 28 篇论文、13 个主要研究物种中被报道，其中 17 条证据来自 Arabidopsis thaliana；37 条证据中仅 1 条报告了浓度梯度或剂量—响应参数，因此剂量—响应关系的定量可比性不足（受检索覆盖限制，需系统检索复核）。判别性检验：外源施加 ≥5 个浓度梯度并配合合成抑制剂，拟合剂量—响应曲线与 EC50，再在受体突变体中检验曲线是否右移。

**为什么值得做（证据缺口）**

- 37 条证据中仅 1 条给出浓度梯度或 EC50
- 缺少跨物种统一施加方式与统一读出，无法比较响应阈值

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 原报道物种 + 一个独立物种；同遗传背景、同生育期 |
| 操纵或比较变量 | 外源施加的浓度梯度（≥5 个剂量）± 合成抑制剂；受体突变体作对照 |
| 读出 | 剂量—响应曲线、EC50、下游响应的动态范围 |
| 若假说为真 | 同一响应在两个物种中给出方向一致、EC50 差异 <1 个数量级的剂量—响应曲线，且受体突变体中曲线右移 |
| 若假说为假 | EC50 跨物种相差 >2 个数量级，或受体突变体中曲线不移位，说明该激素的响应阈值由谱系特异的受体组成决定 |

**证据基础**：37 条证据 / 28 篇独立论文（置信度：高）
- `dpdf-10-1146-annurev-arplant-083123073106-f11`
- `ms-10-67693_bjcr-3jqlrcre-f7`
- `gibberellin-biosynthesis-is-required-for-cppu-induced-f2`
- `ref-pnas-0709559105-f3`
- `root-cluster-hormone-response-patterns`
- `ref-tpc-114-133496-f1`

**领域特异性**：领域特异读出梯度：激素含量、响应元件驱动报告基因、磷酸化状态、剂量—响应 EC50（本条正文命中：浓度梯度、突变体）

**原始断言（摘自证据页，供核对）**
> Elaeocarpus grandiflorus callus cultures exhibited differential growth responses on MS medium supplemented with varying concentrations of plant growth regulators.The study demonstrated that optimization of auxin and cytokinin levels is essential for enhancing callus proliferation, providing valuable insights for In…
> <sub>来源：`ms-10-67693_bjcr-3jqlrcre-f7`</sub>


### H5：cytokinin（剂量—效应）

**假说**："cytokinin" 在本主题 20 篇论文、10 个主要研究物种中被报道，其中 13 条证据来自 Arabidopsis thaliana；28 条证据中仅 1 条报告了浓度梯度或剂量—响应参数，因此剂量—响应关系的定量可比性不足（受检索覆盖限制，需系统检索复核）。判别性检验：外源施加 ≥5 个浓度梯度并配合合成抑制剂，拟合剂量—响应曲线与 EC50，再在受体突变体中检验曲线是否右移。

**为什么值得做（证据缺口）**

- 28 条证据中仅 1 条给出浓度梯度或 EC50
- 缺少跨物种统一施加方式与统一读出，无法比较响应阈值

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 原报道物种 + 一个独立物种；同遗传背景、同生育期 |
| 操纵或比较变量 | 外源施加的浓度梯度（≥5 个剂量）± 合成抑制剂；受体突变体作对照 |
| 读出 | 剂量—响应曲线、EC50、下游响应的动态范围 |
| 若假说为真 | 同一响应在两个物种中给出方向一致、EC50 差异 <1 个数量级的剂量—响应曲线，且受体突变体中曲线右移 |
| 若假说为假 | EC50 跨物种相差 >2 个数量级，或受体突变体中曲线不移位，说明该激素的响应阈值由谱系特异的受体组成决定 |

**证据基础**：28 条证据 / 20 篇独立论文（置信度：高）
- `dpdf-10-1146-annurev-arplant-083123073106-f11`
- `ms-10-67693_bjcr-3jqlrcre-f7`
- `ref-pnas-0709559105-f3`
- `ms-10-47191_ijmra_v9-i7-41-f3`
- `ref-science-aay4970-f5`
- `ref-science-aay4970-f6`

**领域特异性**：领域特异读出梯度：激素含量、响应元件驱动报告基因、磷酸化状态、剂量—响应 EC50（本条正文命中：浓度梯度、突变体）

**原始断言（摘自证据页，供核对）**
> We found a total of four cytokinin-responsive transcriptional activators (B type ARRs), four cytokinin signaling inhibitors (A type ARRs), six auxin response factors (ARFs), and seven auxin/ indole-3-acetic acid inducible genes (Aux/IAAs) whose expression was well correlated with the largest cell-specific response c…
> <sub>来源：`ref-pnas-0709559105-f3`</sub>





## 使用方式

1. 先按"证据缺口"排序：单一物种、单篇论文、缺因果证据的假说优先补验证；
2. 每条假说的"若假说为假"一栏即为**止损条件**，实验设计阶段就应确定样本量；
3. 证据 ID 可直接在 `evidence/` 下打开原文摘要核对，禁止跳过核对直接引用。

---
*由 Phase 8 生成于 2026-11-03；生成器版本 2026-11-02-evidence-grounded*
