---
title: "Hypotheses: Genomics & Evolution"
title_zh: "基因组学与演化：可证伪假说"
type: hypothesis
topic: "genomics-evolution"
theme_basis: "tag"
total_evidence: 521
total_papers: 273
total_hypotheses: 6
specificity_domain: 6
specificity_generic: 0
auto_generated: true
generator: "batch_hypotheses.py (evidence-grounded, 2026-11-02)"
updated: 2026-11-17
---

# 💡 Genomics & Evolution — 可证伪假说（6 条）

> 生成口径：主题内 521 条证据 / 273 篇独立论文（主题归属依据：证据标签）。
> 每条假说只在"≥3 条证据且 ≥2 篇独立论文"时生成，并附证据 ID 与证伪条件。
> 本页是**机器生成的候选清单**，不是经同行评议的结论；引用前须回原文核对。

## 主题覆盖概览

| 项目 | 值 |
|---|---|
| 主题 | Genomics & Evolution |
| 证据条目 | 521 |
| 独立论文 | 273 |
| 生成假说 | 6 |
| 其中主题专用方案 | 6 |
| 其中缺省回退方案（需改写） | 0 |
| 主题归属依据 | 证据标签 |

### H1：MaGELP81 → （共同上游排除）

**假说**：MaGELP81 与 （responses） 在本主题的多项研究中被同时报道，但二者目前只是表达层面的共变。判别性检验：阻断 MaGELP81，看 （responses） 是否随之改变，而非二者共受上游驱动。

**为什么值得做（证据缺口）**

- 现有证据以表达/关联为主，缺少遗传操纵的因果证据
- 缺少细胞类型/空间分辨率，无法判定效应发生在哪类细胞

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 同物种 >=2 份独立组装/重测序数据，含近缘外类群 |
| 操纵或比较变量 | 组装连续性、注释流程、或群体分组（唯一变量） |
| 对照 | 不同组装版本互为对照；群体结构作协变量 |
| 读出 | contig NG50/BUSCO/LAI、共线性区块、Fst/pi/Tajima D、分化时间（至少两项独立读出交叉验证） |
| 若假说为真 | 阻断 MaGELP81 后 （responses） 发生可测变化，而共同上游因子的活性或丰度未同步改变 |
| 若假说为假 | 阻断 MaGELP81 后 （responses） 不变，或共同上游因子改变时两者同步变化（提示平行而非上下游） |

**证据基础**：25 条证据 / 23 篇独立论文（置信度：高）
- `ms-10-3389_fpls-2026-1880971-f1`
- `daily-42666449-f4`
- `daily-42514481-f7`
- `ms-10-1186_s12870-026-08649-w-f1`
- `daily-42239855-f1`
- `daily-42200200-f1`

**领域特异性**：领域特异读出：contig NG50/BUSCO/LAI、共线性区块、Fst/pi/Tajima D、分化时间

**原始断言（摘自证据页，供核对）**
> Conclusion Collectively, this study provides a comprehensive view of the composition and evolutionary features of the banana GELP family, elucidates their potential roles in responses to Foc TR4 stress, and pinpoints MaGELP81 as a key candidate gene.
> <sub>来源：`daily-42436383-f1`</sub>


### H2：MKK3（剂量—效应）

**假说**：MKK3 已有 18 项独立研究；但其中仅 0 条给出不同表达/活性水平的梯度或剂量—响应参数，效应量随水平变化的定量关系无法从现有文献取得（受检索覆盖限制，需系统检索复核）。判别性检验：构建梯度表达系并做定量表型曲线。

**为什么值得做（证据缺口）**

- 现有证据以表达/关联为主，缺少遗传操纵的因果证据
- 缺少细胞类型/空间分辨率，无法判定效应发生在哪类细胞

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 同物种 >=2 份独立组装/重测序数据，含近缘外类群 |
| 操纵或比较变量 | 组装连续性、注释流程、或群体分组（唯一变量） |
| 对照 | 不同组装版本互为对照；群体结构作协变量 |
| 读出 | contig NG50/BUSCO/LAI、共线性区块、Fst/pi/Tajima D、分化时间（至少两项独立读出交叉验证） |
| 若假说为真 | 表型随 MKK3 表达或活性单调变化，半数效应点可在独立实验室复现 |
| 若假说为假 | 表型与表达量无单调关系（阈值型或非单调），提示存在缓冲或旁路 |

**证据基础**：19 条证据 / 18 篇独立论文（置信度：高）
- `daily-42486906-f2`
- `daily-42222012-f1`
- `daily-42491363-f2`
- `daily-42654846-f1`
- `daily-42654846-f7`
- `daily-42210059-f1`

**领域特异性**：领域特异读出：contig NG50/BUSCO/LAI、共线性区块、Fst/pi/Tajima D、分化时间

**原始断言（摘自证据页，供核对）**
> Our analysis provides new insights into MKK3 evolution and the geographic distribution of MKK3 haplotypes associated with low dormancy.
> <sub>来源：`daily-42681565-f7`</sub>


### H3：qtl → 可重复性（组装稳健性）

**假说**："qtl" 相关结论主要来自有限物种与有限组装质量的数据。判别性检验：在新增独立基因组中复检，并检验信号是否随组装碎片化而消失。

**为什么值得做（证据缺口）**

- 现有证据以表达/关联为主，缺少遗传操纵的因果证据
- 缺少细胞类型/空间分辨率，无法判定效应发生在哪类细胞

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 同物种 >=2 份独立组装/重测序数据，含近缘外类群 |
| 操纵或比较变量 | 组装连续性、注释流程、或群体分组（唯一变量） |
| 对照 | 不同组装版本互为对照；群体结构作协变量 |
| 读出 | contig NG50/BUSCO/LAI、共线性区块、Fst/pi/Tajima D、分化时间（至少两项独立读出交叉验证） |
| 若假说为真 | 新增独立基因组中检出方向一致的信号，且与组装质量指标无关 |
| 若假说为假 | 新增基因组中信号消失，或完全可由组装碎片化解释 |

**证据基础**：14 条证据 / 11 篇独立论文（置信度：高）
- `daily-42682625-f7`
- `daily-42357205-f8`
- `daily-42174430-f1`
- `daily-42581095-f5`
- `daily-42682625-f6`
- `daily-42278485-f2`

**领域特异性**：领域特异读出：contig NG50/BUSCO/LAI、共线性区块、Fst/pi/Tajima D、分化时间（本条正文命中：组装质量）

**原始断言（摘自证据页，供核对）**
> Together, the QTL regions identified in this study provide a foundation for the investigation of candidate genes regulating phenolic acid accumulation in maize kernels and represent actionable targets for marker-assisted selection in breeding programs aimed at improving cell wall quality and biotic stress resistance…
> <sub>来源：`daily-42682625-f7`</sub>


### H4：polyploid → 可重复性（组装稳健性）

**假说**："polyploid" 相关结论主要来自有限物种与有限组装质量的数据。判别性检验：在新增独立基因组中复检，并检验信号是否随组装碎片化而消失。

**为什么值得做（证据缺口）**

- 现有证据以表达/关联为主，缺少遗传操纵的因果证据
- 缺少细胞类型/空间分辨率，无法判定效应发生在哪类细胞

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 同物种 >=2 份独立组装/重测序数据，含近缘外类群 |
| 操纵或比较变量 | 组装连续性、注释流程、或群体分组（唯一变量） |
| 对照 | 不同组装版本互为对照；群体结构作协变量 |
| 读出 | contig NG50/BUSCO/LAI、共线性区块、Fst/pi/Tajima D、分化时间（至少两项独立读出交叉验证） |
| 若假说为真 | 新增独立基因组中检出方向一致的信号，且与组装质量指标无关 |
| 若假说为假 | 新增基因组中信号消失，或完全可由组装碎片化解释 |

**证据基础**：10 条证据 / 10 篇独立论文（置信度：高）
- `daily-42588882-f5`
- `daily-42231893-f6`
- `daily-42656797-f3`
- `daily-42639691-f6`
- `daily-42481944-f5`
- `daily-42644387-f2`

**领域特异性**：领域特异读出：contig NG50/BUSCO/LAI、共线性区块、Fst/pi/Tajima D、分化时间（本条正文命中：组装质量）

**原始断言（摘自证据页，供核对）**
> Analogous to the extensive remodeling of seed oil metabolic networks previously documented during allopolyploidization ( ), our findings suggest that the observed network divergence is consistent with transcriptional remodeling accompanying polyploid evolution.
> <sub>来源：`daily-42656797-f3`</sub>


### H5：PhCBP60b（剂量—效应）

**假说**：PhCBP60b 已有 8 项独立研究；但其中仅 0 条给出不同表达/活性水平的梯度或剂量—响应参数，效应量随水平变化的定量关系无法从现有文献取得（受检索覆盖限制，需系统检索复核）。判别性检验：构建梯度表达系并做定量表型曲线。

**为什么值得做（证据缺口）**

- 现有证据以表达/关联为主，缺少遗传操纵的因果证据
- 缺少细胞类型/空间分辨率，无法判定效应发生在哪类细胞

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 同物种 >=2 份独立组装/重测序数据，含近缘外类群 |
| 操纵或比较变量 | 组装连续性、注释流程、或群体分组（唯一变量） |
| 对照 | 不同组装版本互为对照；群体结构作协变量 |
| 读出 | contig NG50/BUSCO/LAI、共线性区块、Fst/pi/Tajima D、分化时间（至少两项独立读出交叉验证） |
| 若假说为真 | 表型随 PhCBP60b 表达或活性单调变化，半数效应点可在独立实验室复现 |
| 若假说为假 | 表型与表达量无单调关系（阈值型或非单调），提示存在缓冲或旁路 |

**证据基础**：8 条证据 / 8 篇独立论文（置信度：高）
- `daily-42687324-f2`
- `daily-42656797-f1`
- `daily-42436371-f7`
- `daily-42200200-f8`
- `daily-42642721-f1`
- `daily-42278485-f1`

**领域特异性**：领域特异读出：contig NG50/BUSCO/LAI、共线性区块、Fst/pi/Tajima D、分化时间

**原始断言（摘自证据页，供核对）**
> In summary, this study establishes a direct regulatory link from PhCBP60b to its cognate target genes PhSWEET11 and PhUGT74E2, supported by genome-wide binding and expression data.
> <sub>来源：`daily-42642721-f1`</sub>


### H6：CL249（必要性检验）

**假说**：CL249 在 7 项研究中被提名参与本主题，但本簇证据中未见在统一背景下检验其必要性的操纵实验（受检索覆盖限制，需回溯原文复核）。判别性检验：获得功能缺失等位基因，做表型、回补与组织特异性验证。

**为什么值得做（证据缺口）**

- 现有证据以表达/关联为主，缺少遗传操纵的因果证据
- 缺少细胞类型/空间分辨率，无法判定效应发生在哪类细胞

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 同物种 >=2 份独立组装/重测序数据，含近缘外类群 |
| 操纵或比较变量 | 组装连续性、注释流程、或群体分组（唯一变量） |
| 对照 | 不同组装版本互为对照；群体结构作协变量 |
| 读出 | contig NG50/BUSCO/LAI、共线性区块、Fst/pi/Tajima D、分化时间（至少两项独立读出交叉验证） |
| 若假说为真 | 功能缺失等位基因产生稳定、可回补的表型缺陷 |
| 若假说为假 | 功能缺失无表型，或表型不可回补（提示脱靶或冗余基因补偿） |

**证据基础**：7 条证据 / 7 篇独立论文（置信度：高）
- `daily-42410345-f4`
- `ms-10-3389_fpls-2026-1806063-f4`
- `daily-42625245-f2`
- `daily-42429570-f4`
- `daily-42488439-f6`
- `daily-42514591-f6`

**领域特异性**：领域特异读出：contig NG50/BUSCO/LAI、共线性区块、Fst/pi/Tajima D、分化时间

**原始断言（摘自证据页，供核对）**
> Collectively, these results indicate that nitrilases associated with UG5, UG1, CL249, and CL285 constitute a single, well-supported evolutionary group whose diversification does not partition into discrete monophyletic families.
> <sub>来源：`daily-42429570-f4`</sub>





## 使用方式

1. 先按"证据缺口"排序：单一物种、单篇论文、缺因果证据的假说优先补验证；
2. 每条假说的"若假说为假"一栏即为**止损条件**，实验设计阶段就应确定样本量；
3. 证据 ID 可直接在 `evidence/` 下打开原文摘要核对，禁止跳过核对直接引用。

---
*由 Phase 8 生成于 2026-11-17；生成器版本 2026-11-02-evidence-grounded*
