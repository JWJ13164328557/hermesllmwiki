---
title: "Research Program: Soybean Internode Light Quality Spatiotemporal Response"
type: research-program
status: draft
hypotheses: [H1, H2, H3, H4, H5]
evidence_basis: 486 evidence objects, 5 syntheses, 4 entity hubs
updated: 2026-05-30
---

# 📋 Research Program: 大豆节间光质时空响应

## Central Question

**不同光质（WL/LBL/LRFR）如何通过时空特异的转录重编程调控大豆节间维管发育？**

---

## Program Structure

```
H1: 激素调控 (Aim 1)
H2: 细胞异质性 (Aim 2)
        ↓
H4: 整合分析 (Aim 3)
        ↓
H3: 标记保守性 (Aim 4)
H5: 通路分化 (Aim 5)
```

---

## Aim 1: 空间转录组揭示维管细胞类型的光质响应图谱

**检验假设**: H1, H2

**实验设计**:
- 样本: 大豆第三节点，WL/LBL/LRFR 各 3 个生物学重复
- 技术: Stereo-seq (空间转录组) + scRNA-seq (单细胞转录组)
- 分辨率: bin50 空间分析 + 单细胞聚类

**分析流程**:
```
Raw data → QC → Normalization → Clustering → Cell type annotation
    → Spatial mapping (RCTD/cell2location)
    → Cell-type-specific DEG (pseudo-bulk)
    → GO/KEGG enrichment
    → Hormone pathway analysis (auxin, GA, ABA)
```

**产出**:
- 大豆节间空间细胞类型图谱
- 形成层/木质部/韧皮部光质响应差异基因列表
- 激素信号通路活性空间分布图

**里程碑**: 定义维管细胞类型的空间分布和光质响应模式

---

## Aim 2: 细胞类型特异的光质响应异质性

**检验假设**: H2

**分析**:
1. 对 Stereo-seq 数据聚类后注释形成层、木质部前体、韧皮部前体
2. 计算每个亚群的"光质响应得分"
3. 比较不同细胞类型对同一光质的响应差异

**关键比较**:
- 形成层: WL vs LBL vs LRFR
- 木质部: 分化梯度如何变化
- 韧皮部: 相对木质部的差异响应

**产出**:
- 细胞类型 × 光质 DEG 热图
- 细胞类型特异性通路富集
- 响应异质性统计检验

---

## Aim 3: 空间+单细胞整合分析

**检验假设**: H4

**方法**:
- Stereo-seq: 提供空间坐标和 spot 水平表达
- scRNA-seq: 提供单细胞分辨率参考
- 整合: RCTD 空间反卷积 → 单细胞空间映射

**验证**:
- 比较整合分析 vs 单一 Stereo-seq 的 DEG 检出率
- 评估空间精度提升程度

---

## Aim 4: 大豆维管标记基因鉴定与跨物种比较

**检验假设**: H3

**分析**:
1. 从 Stereo-seq 数据中识别大豆形成层/木质部/韧皮部标记基因
2. 与拟南芥已知标记进行同源比较
3. 计算保守率和分歧率

**产出**:
- 大豆维管细胞类型标记基因集
- 跨物种保守性/分歧分析
- 大豆特异标记候选列表

---

## Aim 5: LBL vs LRFR 通路分化分析

**检验假设**: H5

**分析**:
1. WL vs LBL 和 WL vs LRFR 的 DEG 比较
2. 共享 vs 特异 DEG 的 GO 富集
3. 光受体和下游通路基因的表达模式

**产出**:
- 蓝光特异响应通路
- 远红光特异响应通路
- 共享通路（核心光质响应模块）

---

## Timeline

| 阶段 | 内容 | 预计时间 |
|------|------|---------|
| Phase 1 | Stereo-seq + scRNA-seq 数据处理 | 2-3 周 |
| Phase 2 | 细胞类型注释 + 空间映射 | 1-2 周 |
| Phase 3 | 差异分析 + 通路富集 | 1 周 |
| Phase 4 | 整合分析 + 跨物种比较 | 1 周 |
| Phase 5 | 假设检验 + 论文写作 | 2-3 周 |

---

## Expected Results & Risk Assessment

### 预期结果

| 假设 | 预期 | 风险 |
|------|------|------|
| H1 | 形成层区域生长素/GA 信号差异 | 低 — 经典知识支持 |
| H2 | 不同维管细胞类型差异响应 | 低 — 拟南芥已有先例 |
| H3 | ≥50% 标记基因不保守 | 中 — 需足够统计效力 |
| H4 | 整合分析显著改善分辨率 | 低 — 方法学成熟 |
| H5 | LBL 和 LRFR 通路部分独立 | 中 — 交叉可能高于预期 |

### 备选方案

- 若 Stereo-seq 分辨率不足 → 补充 LCM + RNA-seq
- 若细胞类型注释困难 → 使用 cross-species reference mapping
- 若通路分化不显著 → 聚焦时间和空间维度差异

---

## Deliverables

1. **Figure 1**: 大豆节间空间细胞类型图谱
2. **Figure 2**: 形成层光质响应 DEG 和通路
3. **Figure 3**: 细胞类型特异的光质响应异质性
4. **Figure 4**: Stereo-seq + scRNA-seq 整合分析
5. **Figure 5**: 大豆维管标记基因鉴定
6. **Figure 6**: LBL vs LRFR 通路分化模型

---

## Knowledge Base Integration

本方案基于知识库:
- 486 Evidence Objects
- 5 Synthesis Pages (Root, Vascular, Methods, Hormone, Regeneration)
- 4 Entity Hubs (Soybean, Vascular, Methods, Root)
- 3 Relationship Matrices

所有假设可追溯至具体证据对象。

---
*基于完整知识链生成 | 可执行研究方案*
