title: Single-Cell Alternative Splicing Analysis with Expedition Reveals Splicing Dynam
created: 2026-05-28
type: concept
tags: [#methods-tools, papers]
doi: 10.1016/j.molcel.2017.06.003
confidence: medium
aliases: ["Single-Cell Alternative Splicing Analysis with Expedition Reveals Splicing Dynam"]
status: draft
updated: "2026-05-29"

# Single-Cell Alternative Splicing Analysis with Expedition Reveals Splicing Dynam




**期刊**: 
**DOI**: [10.1016/j.molcel.2017.06.003](https://doi.org/10.1016/j.molcel.2017.06.003)
**作者**: 

## 摘要
Alternative splicing (AS) generates isoform diversity for cellular identity and homeostasis in multicellular life. Although AS variation has been observed among single cells, little is known about the biological or evolutionary significance of such variation. We developed Expedition, a computational framework consisting of outrigger, a de novo splice graph transversal algorithm to detect AS; anchor, a Bayesian approach to assign modalities; and bonvoyage, a visualization tool using non-negative matrix factorization to display modality changes. Applying Expedition to single pluripotent stem cells undergoing neuronal differentiation, we discover that up to 20% of AS exons exhibit bimodality. Bimodal exons are flanked by more conserved intronic sequences harboring distinct cis-regulatory motifs, constitute much of cell-type-specific splicing, are highly dynamic during cellular transitions, preserve reading frame, and reveal intricacy of cell states invisible to conventional gene expression analysis. Systematic AS characterization in single cells redefines our understanding of AS complexity in cell biology.


## 全文 (PMC)

### PERMALINK

Correspondence tobe addressed togeneyeo@ucsd.edu Present address: Human Longevity Institute These authors contributed equally. Alternative splicing (AS) generates isoform diversity for cellular identity and homeostasis in multicellular life. Although AS variation has been observed among single cells, little is known about the biological or evolutionary significance of such variation. We developedExpedition, a computational framework consisting ofoutrigger, ade novosplice graph transversal algorithm to detect AS;anchor, a Bayesian approach to assign modalities andbonvoyage, a visualization tool using non-negative matrix factorization to display modality changes. ApplyingExpeditionto single pluripotent stem cells undergoing neuronal differentiation, we discover that up to 20% of AS exons exhibit bimodality. Bimodal exons are flanked by more conserved intronic sequences harboring distinctcis-regulatory motifs, constitute much of cell-type specific splicing, are highly dynamic during cellular transitions, preserve reading frame and reveal intricacy of cell states invisible to conventional gene expression analysis. Systematic AS characterization in single cells redefines our understanding of AS complexity in cell biology. Over 90% of multi-exon human genes undergo alternative splicing (AS) (Johnson et al., 2003;Pan et al., 2008;Takeda et al., 2010;Wang et al., 2008). Transcriptome profiling by sequencing (RNA-seq) is a powerful means to detect and quantify AS in tissue or cell populations (Barbosa-Morais et al., 2012;Merkin et al., 2012;Wang et al., 2008). Advances in single-cell RNA-seq (scRNA-seq) now enables the detection of AS at the single cell level. Previous studies that investigated AS in single cells were limited to a few exons (Shalek et al., 2013;Waks et al., 2011) or focused on discovering novel splice junctions (Marinov et al., 2014). However, the complexity of AS in single cells remains unappreciated. There is an urgent need to develop robust computational 

### Yan Song

Correspondence tobe addressed togeneyeo@ucsd.edu Present address: Human Longevity Institute These authors contributed equally.

### Correspondence to

Correspondence tobe addressed togeneyeo@ucsd.edu Present address: Human Longevity Institute These authors contributed equally.

### Publisher's Disclaimer:

Publisher's Disclaimer:This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final citable form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain. DATA AND SOFTWARE AVAILABILITY All Python code in the form of Jupyter notebooks is available athttps://github.com/YeoLab/singlecell_pnm, and the Expedition suite is available here:https://github.com/YeoLab/Expedition, with individual outrigger, (https://github.com/YeoLab/outrigger), anchor (https://github.com/YeoLab/anchor), and bonvoyage (https://github.com/YeoLab/bonvoyage) packages available separately. Methods S1 in the Supplemental Informationdetails three protocols. Protocol 1 describes the procedure of single cell capture and RNA-sequencing library preparation. Protocol 2 describes the procedure of single cell capture for qPCR. Protocol 3 describes single molecule RNA-FISH. Y.S., O.B.B. and G.W.Y. conceived and designed experiments; Y.S. and J.L.X. performed the experiments; O.B.B. wrote theExpeditionsuite and performed computational analysis; P.L., M.T.L. and B.K. assisted with computational analysis; Y.S. performed and analyzed the sc-qPCR and RNA-FISH data; Y.S., O.B.B. and G.W.Y. wrote the manuscript. Competing Financial Interests The authors declare no competing financial interests.


**OA PDF**: https://europepmc.org/articles/pmc5540791?pdf=render


## 相关文献

- [[b3-L7GZnhJuEotGMug-3oD2oA]]
- [[b3-hec2f2m1kP9Y-33yozL7Bg]]
- [[b3-lAocrXAzQRs_pNTy-8Ac1g]]
- [[b4-A4eRtTpTuVLrP6mvHWMndA]]
- [[b5-I9J_3tEggQGIGk7z9SmwOw]]
- [[cr-btt656]]
- [[cr-s13059-014-0550-8]]


## 深度提炼

**物种**: Ficus carica
**方法**: transcriptomics (RNA-seq), single-cell RNA-seq, qRT-PCR validation
**来源**: DOI:10.1016/j.molcel.2017.06.003
**来源类型**: PDF全文 (10.1016_j.molcel.2017.06.003.pdf)

### 核心发现
1. Applying Expe- dition to single pluripotent stem cells undergoing neuronal differentiation, we discover that up to 20% of AS exons exhibit bimodality.
2. Repetitive elements such as Alu are known to be stochas- tically exonized (Stower, 2013), and we found Alu elements are more enriched within excluded exons, are fewer within bimodal exons, and are almost absent from AS events in the included modality (Figure S3D).
3. We conclude that bimodal and multimodal events are enriched for longer ﬂanking introns with higher conservation, present in recently evolved genes, and have orthologs in mammals that are also subject to AS.
4. We found that introns ﬂanking exons that exhibit bimodal and included modalities are enriched for U-rich and G-rich motifs, respectively, regardless of the cell types.
5. Together, our results reveal that exons with highly variant AS events have sequence and evolutionary attri- butes distinct from other modalities.
6. To our surprise, we found that only 20% of AS events shared between pluripotent stem cells and the neuronal derivatives exhibit a change in modality (q < 10100, hypergeometric test, corrected for multiple hypothesis testing).
7. (B) During the differentiation from iPSCs to MNs or from iPSCs to NPCs, we found that 1,586 (17.6%) or 1,029 (18.1%) AS events switched modality, respectively.
8. Among properties investigated, we found that MNs favor splicing that generates more disordered and basic proteins, such as the AS events in RPS24 (ribosomal subunit pro- tein S24) and ZNF207/BuGZ (Figures 7A and 7B).