---
title: "Hypotheses: Single-Cell & Spatial Omics"
title_zh: "单细胞与空间组学：可证伪假说"
type: hypothesis
topic: "single-cell-spatial-omics"
theme_basis: "tag"
total_evidence: 79
total_papers: 41
total_hypotheses: 1
specificity_domain: 1
specificity_generic: 0
auto_generated: true
generator: "batch_hypotheses.py (evidence-grounded, 2026-11-02)"
updated: 2026-11-03
---

# 💡 Single-Cell & Spatial Omics — 可证伪假说（1 条）

> 生成口径：主题内 79 条证据 / 41 篇独立论文（主题归属依据：证据标签）。
> 每条假说只在"≥3 条证据且 ≥2 篇独立论文"时生成，并附证据 ID 与证伪条件。
> 本页是**机器生成的候选清单**，不是经同行评议的结论；引用前须回原文核对。

## 主题覆盖概览

| 项目 | 值 |
|---|---|
| 主题 | Single-Cell & Spatial Omics |
| 证据条目 | 79 |
| 独立论文 | 41 |
| 生成假说 | 1 |
| 其中主题专用方案 | 1 |
| 其中缺省回退方案（需改写） | 0 |
| 主题归属依据 | 证据标签 |

### H1：表皮细胞身份（注释一致性）

**假说**：“表皮”在本主题的 4 篇论文（2 个主要研究物种）中都被独立注释，但各研究使用不同的标记基因集与聚类参数，同一身份是否指向同一细胞群体未知。判别性检验：以其中一套标记集为参照，对另一数据集做标签转移，再用独立标记与空间位置做正交验证。

**为什么值得做（证据缺口）**

- 4 篇论文各自定义 表皮，缺少共享标记集与统一聚类参数
- 同名身份的跨数据集一致性缺少定量评估；4 条证据中仅 0 条涉及标签转移或整合

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 至少两个独立数据集（不同物种或不同平台），同一组织部位 |
| 操纵或比较变量 | 注释方案（参照标记集 vs 目标数据集自有注释），唯一变量 |
| 读出 | 标签转移一致率、独立标记阳性率、空间位置吻合度 |
| 若假说为真 | 标签转移后 表皮 与参照注释高度重合，且被独立标记与空间位置共同支持 |
| 若假说为假 | 标签转移后 表皮 与参照注释大面积错配，说明同名身份实为不同细胞群体 |

**证据基础**：4 条证据 / 4 篇独立论文（置信度：中）
- `ref-j-tplants-2019-10-008-f6`
- `ref-s13059-015-0580-x-f2`
- `rice-root-cell-types-10x`
- `ref-erae107-f1`

**领域特异性**：领域特异读出梯度：细胞类型比例、标记基因特异度、聚类稳定性（ARI/NMI）、空间共定位（本条正文命中：标签转移、标记基因）

**原始断言（摘自证据页，供核对）**
> However, current methods do allow the capture and identification of QC cells [9,10], highlighting the sensitivity of scRNA-seq in resolving distinct cell states whose differences might be mild across a cell-type file but that are essential to steer the incremental transition of stem cells (e.g., epidermis initials)…
> <sub>来源：`ref-j-tplants-2019-10-008-f6`</sub>



## 证据不足声明（自动判定，不是敷衍）

本主题当前只能支撑 **1 条**可证伪假说（目标 3 条）。脚本不会为了凑数而降低门槛，因此如实报告缺口：

| 项目 | 值 |
|---|---|
| 主题内证据 | 79 |
| 独立论文 | 41 |
| 形成的证据簇 | 4 |
| 最大簇规模 | 5 |

| 未成假说的原因 | 簇数 |
|---|---|
| 主语是泛化术语，不构成因果假说（已拒绝编造） | 3 |
| 仅单篇论文支撑（无法构成独立证据） | 1 |

### 为什么会出现这种局面

本主题证据中 `evidence_type` 高度集中于表达/关联类断言，且同一机制的证据分散在不同论文的不同表述里，缺少"同一基因 × 同一表型"的重复测量。要生成更多假说，缺的不是算法，而是**可比的重复证据**。

### 补齐证据的具体做法（可直接落到检索式）

1. 对每个候选机制追加检索式：`"<基因名>" AND ("mutant" OR "knockout" OR "overexpression" OR "CRISPR")`，把表达关联升级为遗传证据；
2. 强制要求同一机制至少 2 篇独立论文（不同实验室或不同物种）；
3. 方法学/工具类主题应改按"工具名 + benchmark + comparison"检索，而不是按生物学关键词，否则会把大量表达研究误并入该主题；
4. 补采后在下一轮自动重算；本页会随证据增长自动升级。

### 待复现清单（单篇论文独占的断言，优先补重复）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `ref-science-aaa6090-f3` | 10.1126/science.aaa6090 | Here, we report multiplexed error-robust FISH (MERFISH), a highly multiplexed smFISH imaging method that… |
| `ref-science-aaa6090-f1` | 10.1126/science.aaa6090 | Here, we report multiplexed errorrobust FISH (MERFISH), a single-molecule imaging method that allows… |
| `ref-science-aaa6090-f2` | 10.1126/science.aaa6090 | Here, we report multiplexed error-robust fluorescence in situ hybridization (MERFISH), a single-molecule… |


## 使用方式

1. 先按"证据缺口"排序：单一物种、单篇论文、缺因果证据的假说优先补验证；
2. 每条假说的"若假说为假"一栏即为**止损条件**，实验设计阶段就应确定样本量；
3. 证据 ID 可直接在 `evidence/` 下打开原文摘要核对，禁止跳过核对直接引用。

---
*由 Phase 8 生成于 2026-11-03；生成器版本 2026-11-02-evidence-grounded*
