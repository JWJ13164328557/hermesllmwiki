title: "PlantRegMap ：绘制工厂中的功能监管图。"
created: 2026-05-28
type: concept
tags: [#methods-tools, papers]
doi: 10.1093/nar/gkz1020
confidence: medium
aliases: ["PlantRegMap ：绘制工厂中的功能监管图。"]
status: draft
updated: "2026-05-29"

# PlantRegMap ：绘制工厂中的功能监管图。




**期刊**: 
**DOI**: [10.1093/nar/gkz1020](https://doi.org/10.1093/nar/gkz1020)
**作者**: 

## 摘要
With the goal of charting plant transcriptional regulatory maps (i.e. transcription factors (TFs), cis-elements and interactions between them), we have upgraded the TF-centred database PlantTFDB (http://planttfdb.cbi.pku.edu.cn/) to a plant regulatory data and analysis platform PlantRegMap (http://plantregmap.cbi.pku.edu.cn/) over the past three years. In this version, we updated the annotations for the previously collected TFs and set up a new section, 'extended TF repertoires' (TFext), to allow users prompt access to the TF repertoires of newly sequenced species. In addition to our regular TF updates, we are dedicated to updating the data on cis-elements and functional interactions between TFs and cis-elements. We established genome-wide conservation landscapes for 63 representative plants and then developed an algorithm, FunTFBS, to screen for functional regulatory elements and interactions by coupling the base-varied binding affinities of TFs with the evolutionary footprints on their binding sites. Using the FunTFBS algorithm and the conservation landscapes, we further identified over 20 million functional TF binding sites (TFBSs) and two million functional interactions for 21 346 TFs, charting the functional regulatory maps of these 63 plants. These resources are publicly available at PlantRegMap (http://plantregmap.cbi.pku.edu.cn/) and a cloud-based mirror (http://plantregmap.gao-lab.org/), providing the plant research community with valuable resources for decoding plant transcriptional regulatory systems.


## 全文 (PMC)

### PERMALINK

To whom correspondence should be addressed. Tel: +86 10 6275 5206; Fax: +86 10 6275 5206; Email:gaog@mail.cbi.pku.edu.cn Correspondence may also be addressed to Jinpu Jin. Email:jinjp@mail.cbi.pku.edu.cn The authors wish it to be known that, in their opinion, the first two authors should be regarded as Joint First Authors. Accepted 2019 Oct 21; Revised 2019 Oct 17; Received 2019 Aug 29; Issue date 2020 Jan 8. This is an Open Access article distributed under the terms of the Creative Commons Attribution Non-Commercial License (http://creativecommons.org/licenses/by-nc/4.0/), which permits non-commercial re-use, distribution, and reproduction in any medium, provided the original work is properly cited. For commercial re-use, please contactjournals.permissions@oup.com With the goal of charting plant transcriptional regulatory maps (i.e. transcription factors (TFs),cis-elements and interactions between them), we have upgraded the TF-centred database PlantTFDB (http://planttfdb.cbi.pku.edu.cn/) to a plant regulatory data and analysis platform PlantRegMap (http://plantregmap.cbi.pku.edu.cn/) over the past three years. In this version, we updated the annotations for the previously collected TFs and set up a new section, ‘extended TF repertoires’ (TFext), to allow users prompt access to the TF repertoires of newly sequenced species. In addition to our regular TF updates, we are dedicated to updating the data oncis-elements and functional interactions between TFs andcis-elements. We established genome-wide conservation landscapes for 63 representative plants and then developed an algorithm, FunTFBS, to screen for functional regulatory elements and interactions by coupling the base-varied binding affinities of TFs with the evolutionary footprints on their binding sites. Using the FunTFBS algorithm and the conservation landscapes, we further identified over 20 million functional TF binding sites (TFBSs) and two million functional interactions for 21 346 TFs, charting the funct

### Feng Tian

To whom correspondence should be addressed. Tel: +86 10 6275 5206; Fax: +86 10 6275 5206; Email:gaog@mail.cbi.pku.edu.cn Correspondence may also be addressed to Jinpu Jin. Email:jinjp@mail.cbi.pku.edu.cn The authors wish it to be known that, in their opinion, the first two authors should be regarded as Joint First Authors. Accepted 2019 Oct 21; Revised 2019 Oct 17; Received 2019 Aug 29; Issue date 2020 Jan 8. This is an Open Access article distributed under the terms of the Creative Commons Attribution Non-Commercial License (http://creativecommons.org/licenses/by-nc/4.0/), which permits non-commercial re-use, distribution, and reproduction in any medium, provided the original work is properly cited. For commercial re-use, please contactjournals.permissions@oup.com

### 

To whom correspondence should be addressed. Tel: +86 10 6275 5206; Fax: +86 10 6275 5206; Email:gaog@mail.cbi.pku.edu.cn Correspondence may also be addressed to Jinpu Jin. Email:jinjp@mail.cbi.pku.edu.cn The authors wish it to be known that, in their opinion, the first two authors should be regarded as Joint First Authors. Accepted 2019 Oct 21; Revised 2019 Oct 17; Received 2019 Aug 29; Issue date 2020 Jan 8. This is an Open Access article distributed under the terms of the Creative Commons Attribution Non-Commercial License (http://creativecommons.org/licenses/by-nc/4.0/), which permits non-commercial re-use, distribution, and reproduction in any medium, provided the original work is properly cited. For commercial re-use, please contactjournals.permissions@oup.com


**OA PDF**: https://academic.oup.com/nar/article-pdf/48/D1/D1104/31697811/gkz1020.pdf


## 相关文献

- [[aba-biosynthesis-stress]]
- [[alfalfa-anther-sc-atlas]]
- [[arabidopsis-sam-scrna]]
- [[b3-BGiBJfPQalD0XaTAW6WgjQ]]
- [[b3-G2N-JJNNVwoyPpAiZEWa8w]]
- [[b4-4h7J0H3OPFzzltwSkI6mtg]]
- [[b4-5L8yUIeARXqlhtyk-pgTZw]]



## PMC 全文


**来源类型**: PMC全文
**PMC ID**: PMC7145545

### INTRODUCTION
Transcription factors (TFs) control gene expression by binding to specific cis -elements, which play essential roles in plant development and stress responses. Systematic identification of TFs, regulatory elements and functional interactions between them would greatly facilitate further mechanistic investigation ( 1 , 2 ). In the past decade, we have been dedicated to constructing a plant TF knowledge base (PlantTFDB) through identifying and annotating the genomic TF repertoires of 165 species covering the main lineages of green plants ( 3–6 ), and this resource has been widely used by the community. With TF binding motifs throughout the genome determined by experiments in plants ( 7 , 8 ) and in silico -mapped in 156 plants ( 6 ), directly scanning the TF binding motifs in the promoters of putative target genes is becoming a promising option. As prediction from direct scanning yields a rather high false positive rate, additional data such as DNase-seq footprints ( 9 , 10 ) and conserved elements ( 11–16 ) have been incorporated to screen for functional TFBSs. However, these data are available in only a few model plants ( 10 , 17 ), and conserved-element-based methods are still confounded by evolutionary constraints on other functional elements other than TF binding ( 18 ), hindering the systematic charting of transcriptional regulatory maps across the plant kingdom.
Comparisons of multiple related genomes with substantial divergence are widely used to detect evolutionary con

## 深度提炼

**物种**: Arabidopsis thaliana, Oryza sativa, Glycine max, Ficus carica
**方法**: genomics, ChIP-seq/qPCR, phylogenetics
**来源**: DOI:10.1093/nar/gkz1020
**来源类型**: PDF全文 (10.1093_nar_gkz1020.pdf)

### 核心发现
1. By browsing our functional TFBSs, we found a TF (AT5G67580) that could bind to that position, and an A to T substitution would weaken its binding (Figure 5A), shedding light on the pu- tative molecular mechanism.
2. With TF binding mo- tifs throughout the genome determined by experiments in plants (7,8) and in silico-mapped in 156 plants (6), directly scanning the TF binding motifs in the promoters of puta- tive target genes is becoming a promising option.
3. Our algorithm showed the highest percentage of TFs and their targets coexisting in the two indexes (20– 22% and 20–39% increases compared with the other two methods, respectively) (Supplementary Figures S7 and S8), further confirming the superiority of FunTFBS in screening for functional regulatory interactions.
4. (A and B) An eQTL (A to T substitution, highlighted in green) located in the TFBS of AT5G67580 predicted by FunTFBS (A) and the significant difference in expression of its target gene (B) (Wilcoxon rank sum test, *** P-value < 0.001).
5. (C) The transcriptional regulatory network consisting of AT3G22830 and its target genes predicted by FunTFBS.
6. (D) Enriched GO terms for the target genes of AT3G22830.
7. Download individual files via HTTP Batch download via FTP http://plantregmap.cbi.pku.edu.cn/ download.php ftp://ftp.cbi.pku.edu.cn/pub/database/ PlantRegMap/ For example, the target genes of a TF (AT3G22830) (Fig- ure 5C) are enriched in ‘response to heat’ (Figure 5D), a bi- ological process that corresponds well to the reported ‘heat stress response’ function of the TF (AT3G22830) (37).
8. expert-curated de- scription) is crucial for users to become familiar with the research status of TFs of interest and provides impor- tant clues for further study.