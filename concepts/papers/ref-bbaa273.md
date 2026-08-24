title: "scAPAtrap ：从单细胞R中鉴定和定量替代性聚腺苷酸化位点"
created: 2026-05-28
type: concept
tags: [#methods-tools, papers]
doi: 10.1093/bib/bbaa273
confidence: medium
aliases: ["scAPAtrap ：从单细胞R中鉴定和定量替代性聚腺苷酸化位点"]
status: draft
updated: "2026-05-29"

# scAPAtrap ：从单细胞R中鉴定和定量替代性聚腺苷酸化位点




**期刊**: 
**DOI**: [10.1093/bib/bbaa273](https://doi.org/10.1093/bib/bbaa273)
**作者**: 

## 摘要
Alternative polyadenylation (APA) generates diverse mRNA isoforms, which contributes to transcriptome diversity and gene expression regulation by affecting mRNA stability, translation and localization in cells. The rapid development of 3' tag-based single-cell RNA-sequencing (scRNA-seq) technologies, such as CEL-seq and 10x Genomics, has led to the emergence of computational methods for identifying APA sites and profiling APA dynamics at single-cell resolution. However, existing methods fail to detect the precise location of poly(A) sites or sites with low read coverage. Moreover, they rely on priori genome annotation and can only detect poly(A) sites located within or near annotated genes. Here we proposed a tool called scAPAtrap for detecting poly(A) sites at the whole genome level in individual cells from 3' tag-based scRNA-seq data. scAPAtrap incorporates peak identification and poly(A) read anchoring, enabling the identification of the precise location of poly(A) sites, even for sites with low read coverage. Moreover, scAPAtrap can identify poly(A) sites without using priori genome annotation, which helps locate novel poly(A) sites in previously overlooked regions and improve genome annotation. We compared scAPAtrap with two latest methods, scAPA and Sierra, using scRNA-seq data from different experimental technologies and species. Results show that scAPAtrap identified poly(A) sites with higher accuracy and sensitivity than competing methods and could be used to explore APA dynamics among cell types or the heterogeneous APA isoform expression in individual cells. scAPAtrap is available at https://github.com/BMILAB/scAPAtrap.



⚠️ 全文需VPN/机构访问


## 相关文献

- [[alfalfa-anther-sc-atlas]]
- [[arabidopsis-root-sc-atlas-plantcell]]
- [[arabidopsis-root-sc-atlas-review]]
- [[arabidopsis-sam-scrna]]
- [[b3--bs1tAYpaCxa0fWZ49R6kw]]
- [[b3-9WavxKoXaOzbDzGmHSgUqw]]
- [[b3-BGiBJfPQalD0XaTAW6WgjQ]]


## 深度提炼

**物种**: Plant (unspecified)
**方法**: transcriptomics (RNA-seq), genomics, single-cell RNA-seq
**来源**: DOI:10.1093/bib/bbaa273
**来源类型**: PDF全文 (10.1093_bib_bbaa273.pdf)

### 核心发现
1. These results suggest that scAPAtrap detects much more poly(A) sites with higher confidence and locates poly(A) sites more precisely than other two tools.
2. Therefore, more sophisticated and cost-efficient approaches are necessary for profiling the landscape of APA at the single-cell level.
3. Notably, up to 1307 3′ UTR poly(A) sites identified by scAPAtrap were exclusively found in the mouse sperm single-cell data, whereas they were not annotated in existing poly(A) site annotations from bulk data (cutoff = 100 bp).
4. An example of 3′ UTR event detected by scAPAtrap is the Arl2bp gene, encoding the ADP- ribosylation factor-like 2 binding protein, which is required for the structural maintenance of the sperm flagellum and thus is essential for motility and fertility [50].
5. Surprisingly, a considerable number of DE poly(A) sites were found among cell types (1669–4614) (Figure S8), reflecting a high degree of heterogeneity of root cells as observed in previous studies [20, 53, 54].
6. Notably, peak calling and poly(A) read anchoring are two independent steps in scAPAtrap and both steps can be used for poly(A) site identification.