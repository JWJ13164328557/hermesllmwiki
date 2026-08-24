title: "SMNN ：通过监督相互最近邻对单细胞RNA-seq数据的批量效应校正"
created: 2026-05-28
type: concept
tags: [#single-cell-spatial, papers]
doi: 10.1093/bib/bbaa097
confidence: medium
aliases: ["SMNN ：通过监督相互最近邻对单细胞RNA-seq数据的批量效应校正"]
status: draft
updated: "2026-05-29"

# SMNN ：通过监督相互最近邻对单细胞RNA-seq数据的批量效应校正




**期刊**: 
**DOI**: [10.1093/bib/bbaa097](https://doi.org/10.1093/bib/bbaa097)
**作者**: 

## 摘要
Batch effect correction has been recognized to be indispensable when integrating single-cell RNA sequencing (scRNA-seq) data from multiple batches. State-of-the-art methods ignore single-cell cluster label information, but such information can improve the effectiveness of batch effect correction, particularly under realistic scenarios where biological differences are not orthogonal to batch effects. To address this issue, we propose SMNN for batch effect correction of scRNA-seq data via supervised mutual nearest neighbor detection. Our extensive evaluations in simulated and real datasets show that SMNN provides improved merging within the corresponding cell types across batches, leading to reduced differentiation across batches over MNN, Seurat v3 and LIGER. Furthermore, SMNN retains more cell-type-specific features, partially manifested by differentially expressed genes identified between cell types after SMNN correction being biologically more relevant, with precision improving by up to 841.0%.



⚠️ 全文需VPN/机构访问


## 相关文献

- [[arabidopsis-root-sc-atlas-review]]
- [[arabidopsis-sam-scrna]]
- [[b3--bs1tAYpaCxa0fWZ49R6kw]]
- [[b3-BGiBJfPQalD0XaTAW6WgjQ]]
- [[b3-Ke_NSLIGVqOSAUr7v-xJ6A]]
- [[b3-MweGEIei1VoObhk3boSJog]]
- [[b3-Q__01uAq9RU85RON6eeUaQ]]


## 深度提炼

**物种**: Plant (unspecified)
**方法**: transcriptomics (RNA-seq), single-cell RNA-seq, knockout/mutant
**来源**: DOI:10.1093/bib/bbaa097
**来源类型**: PDF全文 (10.1093_bib_bbaa097.pdf)

### 核心发现
1. We show t- SNE plot for each cell type before and after MNN and SMNN cor- rection under both the orthogonal and non-orthogonal scenar- ios.
2. These results suggest that SMNN provides improved batch effect correction over MNN under both orthogonal and non-orthogonal scenarios.
3. These results suggest improved batch effect correction by SMNN, compared with unsupervised correction methods.
4. These results suggest that SMNN can eliminate the overcor- rection between different cell types and thus maintains more biological features in corrected data than MNN.
5. In summary, extensive simulation and real data benchmark- ing suggest that our SMNN can not only better rescue biolog- ical features and thereof provide improved cluster results but also facilitate the identification of biologically relevant DEGs.
6. Controlling for confounding effects in single cell RNA sequencing studies using both control and target genes.
7. Notably, all four methods can substantially mitigate discrepancy between the two datasets.
8. More importantly, the wrongly matched cell pairs may wipe out the distinguishing features of cell types.