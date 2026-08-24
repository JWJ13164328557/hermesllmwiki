title: The dynamics and regulators of cell fate decisions are revealed by pseudotempora
created: 2026-05-28
type: concept
tags: [#methods-tools, papers]
doi: 10.1038/nbt.2859
confidence: medium
aliases: ["The dynamics and regulators of cell fate decisions are revealed by pseudotempora"]
status: draft
updated: "2026-05-29"

# The dynamics and regulators of cell fate decisions are revealed by pseudotempora




**期刊**: 
**DOI**: [10.1038/nbt.2859](https://doi.org/10.1038/nbt.2859)
**作者**: 

## 摘要
Defining the transcriptional dynamics of a temporal process such as cell differentiation is challenging owing to the high variability in gene expression between individual cells. Time-series gene expression analyses of bulk cells have difficulty distinguishing early and late phases of a transcriptional cascade or identifying rare subpopulations of cells, and single-cell proteomic methods rely on a priori knowledge of key distinguishing markers. Here we describe Monocle, an unsupervised algorithm that increases the temporal resolution of transcriptome dynamics using single-cell RNA-Seq data collected at multiple time points. Applied to the differentiation of primary human myoblasts, Monocle revealed switch-like changes in expression of key regulatory factors, sequential waves of gene regulation, and expression of regulators that were not known to act in differentiation. We validated some of these predicted regulators in a loss-of function screen. Monocle can in principle be used to recover single-cell gene expression kinetics from a wide array of cellular processes, including differentiation, proliferation and oncogenic transformation.


## 全文 (PMC)

### PERMALINK

Correspondence should be addressed to: John Rinn (john_rinn@harvard.edu) Users may view, print, copy, and download text and data-mine the content in such documents, for the purposes of academic research, subject always to the full Conditions of use:http://www.nature.com/authors/editorial_policies/license.html#terms Single-cell expression profiling by RNA-Seq promises to exploit cell-to-cell variation in gene expression to reveal regulatory circuitry governing cell differentiation and other biological processes. Here, we describe Monocle, a novel unsupervised algorithm for ordering cells by progress through differentiation that dramatically increases temporal resolution of expression measurements in a model of skeletal muscle differentiation. This reordering unmasks switch-like changes in expression of key regulatory factors, reveals sequentially organized waves of gene regulation, and exposes novel regulators of cell differentiation. A loss-of function screen revealed that many of these inhibitors act through regulatory elements also used by pro-myogenic factors to activate downstream genes. This study demonstrates that single-cell expression analysis by Monocle can uncover novel regulatory interactions governing differentiation. Cell differentiation is governed by a vast and complex gene regulatory program. During differentiation, each cell makes fate decisions independently by integrating a wide array of signals from other cells, executing a complex choreography of gene regulatory changes. Recently, several studies carried out at single-cell resolution have revealed high cell-to-cell variation in most genes during differentiation1–5, even among key developmental regulators. Although high variability complicates analysis of such experiments6, it might define biological progression between cellular states, revealing regulatory modules of genes that co-vary in expression across individual cells7. Prior studies have used approaches from computational geometry8,9and su

### Cole Trapnell

Correspondence should be addressed to: John Rinn (john_rinn@harvard.edu) Users may view, print, copy, and download text and data-mine the content in such documents, for the purposes of academic research, subject always to the full Conditions of use:http://www.nature.com/authors/editorial_policies/license.html#terms

### 

Correspondence should be addressed to: John Rinn (john_rinn@harvard.edu) Users may view, print, copy, and download text and data-mine the content in such documents, for the purposes of academic research, subject always to the full Conditions of use:http://www.nature.com/authors/editorial_policies/license.html#terms

### Data and software accessibility

Data and software accessibilityAll sequencing reads are available through GEO accessionGSE52529. Monocle is available athttp:// http://monocle-bio.sourceforge.net/ Author contributionsCT and DC conceived the strategy of ordering individual cells by developmental progress. CT designed and wrote Monocle and performed the computational analysis. DC, CT, JG, PP, SL, and MM performed the experiments. DC, CT and JR designed the study. CT, DC, JG, NL, KL, TM, and JR wrote the manuscript.


**OA PDF**: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4122333


## 相关文献

- [[b3-L7GZnhJuEotGMug-3oD2oA]]
- [[b3-hec2f2m1kP9Y-33yozL7Bg]]
- [[b3-lAocrXAzQRs_pNTy-8Ac1g]]
- [[b4-A4eRtTpTuVLrP6mvHWMndA]]
- [[b5-I9J_3tEggQGIGk7z9SmwOw]]
- [[cr-btt656]]
- [[cr-s13059-014-0550-8]]



## PMC 全文

**PMC ID**: PMC4122333

### PERMALINK
class="usa-button pmc-sidenav__container__open usa-button--unstyled width-auto display-flex"
aria-label="Open article navigation"
data-extra-class="is-visible-in-page"
data-ga-category="actions"
data-ga-action="open"
data-ga-label="article_nav_mobile"
As a library, NLM provides access to scientific literature. Inclusion in an NLM database does not imply endorsement of, or agreement with,
the contents by NLM or the National Institutes of Health.
class="usa-layout-docs__main usa-layout-docs grid-col-12 pmc-layout pmc-prose padding-0"
Nat Biotechnol . Author manuscript; available in PMC: 2014 Oct 1.
Published in final edited form as: Nat Biotechnol. 2014 Mar 23;32(4):381–386. doi: 10.1038/nbt.2859
Pseudo-temporal ordering of individual cells reveals dynamics and regulators of cell fate decisions
### Cole Trapnell
1 Department of Stem Cell and Regenerative Biology, Harvard University, Cambridge, Massachusetts, USA
2 The Broad Institute of MIT and Harvard, Cambridge, Massachussetts, USA
Find articles by Cole Trapnell
1, 2, # , Davide Cacchiarelli
### Davide Cacchiarelli
1 Department of Stem Cell and Regenerative Biology, Harvard University, Cambridge, Massachusetts, USA
2 The Broad Institute of MIT and Harvard, Cambridge, Massachussetts, USA
3 Harvard Stem Cell Institute, Harvard University, Cambridge, MA
Find articles by Davide Cacchiarelli
1, 2, 3, # , Jonna Grimsby

## 深度提炼

**物种**: Ficus carica
**方法**: transcriptomics (RNA-seq), single-cell RNA-seq, qRT-PCR validation, RNAi/VIGS, overexpression
**来源**: DOI:10.1038/nbt.2859
**来源类型**: PDF全文 (10.1038_nbt.2859.pdf)

### 核心发现
1. Our results suggest that USF1 may repress a broad array of targets via E-box competition.
2. A similar analysis of microRNA target sites identified miR-1, miR-206, miR-133 and many others as regulators of genes activated during myogenesis (Supplementary Fig.
3. Of these, only miR-1 and miR-206 target sites were significantly enriched among genes found to be transiently upregu­ lated and then sharply downregulated.
4. Knockdown of XBP1, USF1, ZIC1 and MZF1 enhanced myotube formation, with larger myotubes containing a higher fraction of total nuclei than mock shRNA controls (Fig.
5. Together, these results confirm that the transcription factors identified as possible regulators in fact influence myoblast differentiation, and demonstrate the power of Monocle for identifying key differentiation genes.
6. This study demonstrates that Monocle can exploit the inherent temporal variability during differentiation to order individual cells according to progress without relying on known markers.
7. For example, the enrichment of transiently upregulated genes for common miRNA target sites raises the question of whether those miRNAs are expressed later, curtailing what would have been higher levels of expression.
8. CUX1 represses targets in several developmental contexts through binding site competition24.