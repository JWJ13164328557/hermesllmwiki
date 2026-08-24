---
title: "Hypothesis Portfolio: Soybean Internode Light Quality Response"
type: hypothesis
evidence_basis: [synthesis-vascular-development, entity-soybean, entity-vascular]
status: draft
updated: 2026-05-30
---

# 🔬 Hypothesis Portfolio

> 基于 486 条证据和 5 篇 Synthesis 自动推导的可检验假设。
> 每个假设标注证据来源、检验方法和可证伪条件。

---

## H1: 光质通过生长素-赤霉素信号调控形成层活性

**假设**: 不同光质（WL/LBL/LRFR）通过差异调控生长素和赤霉素信号通路，改变大豆节间形成层细胞增殖和分化速率。

**证据基础**:
- 生长素和赤霉素是维管形成层的主要调控因子（Synthesis: Hormone Signaling）
- SHR 调控原生韧皮部/木质部发育的跨物种保守性（Evidence: ev-* 维管证据）
- 光质影响植物茎伸长的经典知识

**检验方法**:
1. Stereo-seq 空间转录组分析 WL/LBL/LRFR 处理的大豆节间
2. 形成层区域差异表达基因的 GO 富集（重点关注 auxin/GA 相关通路）
3. 原位杂交验证关键激素信号基因的空间表达模式

**可证伪条件**: 形成层区域激素信号基因在三种光质间无显著差异表达。

**优先级**: 🔴 最高 — 直接回答核心科学问题

---

## H2: 光质响应在不同维管细胞类型间具有异质性

**假设**: WL/LBL/LRFR 处理对形成层、木质部前体、韧皮部前体的转录影响不同，不同细胞类型对光质的响应具有特异性。

**证据基础**:
- 拟南芥根 scRNA-seq 揭示胁迫响应的细胞类型异质性（Synthesis: Root Development C4）
- 维管系统包含多种功能不同的细胞类型（Entity: Vascular System）
- 单细胞分辨率可检测细胞类型特异性响应

**检验方法**:
1. 对 Stereo-seq 数据进行无监督聚类，注释形成层、木质部、韧皮部亚群
2. 比较各亚群在三种光质间的 DEG 数量和通路
3. 计算各细胞类型的"光质响应指数"

**可证伪条件**: 三种光质处理下各维管细胞类型的表达谱高度相似（相关性 >0.95）。

**优先级**: 🔴 最高

---

## H3: 大豆维管发育的细胞类型标记与拟南芥不保守

**假设**: 大豆形成层和维管细胞类型的转录标记基因与拟南芥差异显著，需要定义大豆特异标记。

**证据基础**:
- 拟南芥根细胞类型标记已完善（Synthesis: Root Development C1）
- 作物与拟南芥的基因调控网络存在分歧（Relationship: Gene×Function）
- 大豆单细胞图谱揭示独特细胞类型（Entity: Soybean）

**检验方法**:
1. 将已知拟南芥维管标记基因映射到大豆同源基因
2. 在大豆 Stereo-seq 数据中检查同源基因的表达特异性
3. 计算拟南芥标记在大豆中的保守率

**可证伪条件**: ≥70% 拟南芥维管标记基因的同源基因在大豆中保持细胞类型特异性。

**优先级**: 🟡 高

---

## H4: 空间转录组 + scRNA-seq 整合优于单一技术

**假设**: 单独使用 Stereo-seq（空间但非单细胞分辨率）或单独使用 scRNA-seq（单细胞但无空间信息）均不足以完整解析光质响应，整合分析是关键。

**证据基础**:
- 单细胞方法学共识: 空间整合是领域方向（Synthesis: Single-cell Methods C4）
- 空间转录组 spot 包含多细胞混合信号（Entity: Methods）
- 多组学整合可提高分辨率

**检验方法**:
1. 对大豆节间同时进行 Stereo-seq 和 scRNA-seq
2. 使用 RCTD/cell2location 进行空间反卷积
3. 比较整合分析 vs 单一技术的 DEG 检出率和空间精度

**可证伪条件**: 单一 Stereo-seq 分析（不做整合）与整合分析的生物学结论一致。

**优先级**: 🟡 高

---

## H5: LBL 和 LRFR 通过不同通路调控节间伸长

**假设**: 蓝光缺失（LBL）通过抑制光受体-PIF通路影响节间细胞伸长，而远红光（LRFR）通过 phyB-PIF 通路影响形成层分裂，两条通路部分独立。

**证据基础**:
- 光受体信号通路在植物发育中的已知功能
- 不同光质对细胞伸长 vs 细胞分裂的差异化影响
- 激素信号通路的细胞类型特异性响应（Synthesis: Hormone Signaling）

**检验方法**:
1. 比较高表达基因在 LBL vs WL 和 LRFR vs WL 的 Venn 分析
2. GO 富集区分"伸长相关"vs"分裂相关"通路
3. 免疫组化验证细胞伸长（细胞长度）和分裂（细胞数量）表型

**可证伪条件**: LBL 和 LRFR 的 DEG 重叠 >80% 且功能通路无区分。

**优先级**: 🟡 高

---

## Hypothesis × Evidence Traceability

| 假设 | 证据来源 | 检验可行性 | 发表价值 |
|------|---------|-----------|---------|
| H1: 激素调控 | Synthesis × 2 | 高 | 高 |
| H2: 细胞异质性 | Synthesis × 2 | 高 | 高 |
| H3: 标记不保守 | Entity × 2 | 中 | 中 |
| H4: 整合优势 | Methods consensus | 高 | 中 |
| H5: 通路分化 | Literature | 中 | 高 |

## Next Steps

1. 优先检验 H1 和 H2（核心科学问题）
2. H4 作为分析方法选择的理论依据
3. H3 和 H5 可作为补充分析

---
*基于 486 条证据自动生成 | 需实验验证*
