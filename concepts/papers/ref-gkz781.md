title: Cell-type-specific analysis of alternative polyadenylation using single-cell tra
created: 2026-05-28
type: concept
tags: [#single-cell-spatial, papers]
doi: 10.1093/nar/gkz781
confidence: medium
aliases: ["Cell-type-specific analysis of alternative polyadenylation using single-cell tra"]
status: draft
updated: "2026-05-29"

# Cell-type-specific analysis of alternative polyadenylation using single-cell tra




**期刊**: 
**DOI**: [10.1093/nar/gkz781](https://doi.org/10.1093/nar/gkz781)
**作者**: 

## 摘要
Alternative polyadenylation (APA) is emerging as an important layer of gene regulation because the majority of mammalian protein-coding genes contain multiple polyadenylation (pA) sites in their 3' UTR. By alteration of 3' UTR length, APA can considerably affect post-transcriptional gene regulation. Yet, our understanding of APA remains rudimentary. Novel single-cell RNA sequencing (scRNA-seq) techniques allow molecular characterization of different cell types to an unprecedented degree. Notably, the most popular scRNA-seq protocols specifically sequence the 3' end of transcripts. Building on this property, we implemented a method for analysing patterns of APA regulation from such data. Analyzing multiple datasets from diverse tissues, we identified widespread modulation of APA in different cell types resulting in global 3' UTR shortening/lengthening and enhanced cleavage at intronic pA sites. Our results provide a proof-of-concept demonstration that the huge volume of scRNA-seq data that accumulates in the public domain offers a unique resource for the exploration of APA based on a very broad collection of cell types and biological conditions.


## 全文 (PMC)

### PERMALINK

To whom correspondence should be addressed. Tel: +972 36409865; Email:ranel@tauex.tau.ac.il Correspondence may also be addressed to Eldad Shulman.eldadshulman@mail.tau.ac.il Accepted 2019 Sep 1; Revised 2019 Aug 27; Received 2019 May 5; Issue date 2019 Nov 4. This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited. Alternative polyadenylation (APA) is emerging as an important layer of gene regulation because the majority of mammalian protein-coding genes contain multiple polyadenylation (pA) sites in their 3′ UTR. By alteration of 3′ UTR length, APA can considerably affect post-transcriptional gene regulation. Yet, our understanding of APA remains rudimentary. Novel single-cell RNA sequencing (scRNA-seq) techniques allow molecular characterization of different cell types to an unprecedented degree. Notably, the most popular scRNA-seq protocols specifically sequence the 3′ end of transcripts. Building on this property, we implemented a method for analysing patterns of APA regulation from such data. Analyzing multiple datasets from diverse tissues, we identified widespread modulation of APA in different cell types resulting in global 3′ UTR shortening/lengthening and enhanced cleavage at intronic pA sites. Our results provide a proof-of-concept demonstration that the huge volume of scRNA-seq data that accumulates in the public domain offers a unique resource for the exploration of APA based on a very broad collection of cell types and biological conditions. The maturation of mRNA 3′ ends is a two-step process, termedcleavage and polyadenylation, that involves endonucleolytic cleavage of the nascent RNA followed by synthesis of a poly(A) tail at the 3′ terminus of the cleaved product (1). Cleavage and polyadenylation sites (pA sites) are defined by adjac

### Eldad David Shulman

To whom correspondence should be addressed. Tel: +972 36409865; Email:ranel@tauex.tau.ac.il Correspondence may also be addressed to Eldad Shulman.eldadshulman@mail.tau.ac.il Accepted 2019 Sep 1; Revised 2019 Aug 27; Received 2019 May 5; Issue date 2019 Nov 4. This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited.

### 

To whom correspondence should be addressed. Tel: +972 36409865; Email:ranel@tauex.tau.ac.il Correspondence may also be addressed to Eldad Shulman.eldadshulman@mail.tau.ac.il Accepted 2019 Sep 1; Revised 2019 Aug 27; Received 2019 May 5; Issue date 2019 Nov 4. This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited.


**OA PDF**: https://academic.oup.com/nar/article-pdf/47/19/10027/30314322/gkz781.pdf


## 相关文献

- [[alfalfa-anther-sc-atlas]]
- [[alfalfa-cadmium-sc-multiomics]]
- [[andrographis-msi-sc-spatial]]
- [[arabidopsis-root-regeneration-sc-multi]]
- [[arabidopsis-root-sc-atlas-plantcell]]
- [[arabidopsis-root-sc-atlas-review]]
- [[arabidopsis-sam-scrna]]



## PMC 全文


**来源类型**: PMC全文
**PMC ID**: PMC6821429

### INTRODUCTION
The maturation of mRNA 3′ ends is a two-step process, termed cleavage and polyadenylation , that involves endonucleolytic cleavage of the nascent RNA followed by synthesis of a poly(A) tail at the 3′ terminus of the cleaved product ( 1 ). Cleavage and polyadenylation sites (pA sites) are defined by adjacent RNA sequence cis -elements, with a key role involving the AAUAAA signal (called the polyadenylation signal ( PAS )), typically located ∼20 nt upstream of the pA site. There are 10 weaker variants of this canonical PAS, the main one being AUUAAA ( 2 ). Auxiliary elements include upstream U-rich and UGUA motifs and downstream U-rich and GU-rich elements. The strength of a pA site is determined by these elements in a combinatorial manner ( 3 ).
Over the last decade, several deep-sequencing techniques were developed for the precise mapping of the 3′ ends of transcripts ( 4 ). Importantly, these transcriptome-wide methods revealed that the majority of human protein-coding genes contain more than one 3′ untranslated region (3′ UTR) pA site, indicating alternative polyadenylation ( APA ) as a widespread regulatory layer that generates transcript isoforms with alternative 3′ ends ( 1 , 5 , 6 ). APA in the 3′ UTR typically generates mRNA isoforms with markedly different 3′ UTR lengths. For example, it was observed that for mouse, the median 3′ UTR lengths of shortest and longest APA isoforms differ ∼7-fold, at 250 nt and 1770 nt, respectively ( 1 , 6 ). As 3′ UTRs contain cis -elem

### DISCUSSION
In this study, we provide a strong demonstration for the utility of scRNA-seq data generated by 3′ tag-based methods for the analysis of APA, despite it not being intentionally developed for the study of this regulatory layer. By analysing single-cell (SC) data, from T cells we detected the global 3′ UTR shortening that is associated with the proliferative state, and by analyzing SC data from spermatogenesis we delineated the drastic 3′ UTR shortening that accompanies this developmental trajectory. The analysis of SC data from the brain pinpointed neurons as the cell type that is characterized as having the greatest incidence of longer isoforms, whereas the analysis of a lung tumour showed global aberration of APA in cancer cells, manifested by enhanced cleavage at both proximal 3′ UTR and intronic pA sites.
By comparison of different cell types or different biological conditions, analysis of 3′ tag-based transcriptomic data globally delineates changes in the relative expression of short versus long gene isoforms. Such changes can stem in principle from either differential activity of the APA machinery that alters the balance between usage of proximal and distal pA sites or from the differential activity of factors that regulate mRNA stab