title: Measuring cell identity in noisy biological systems.
created: 2026-05-28
type: concept
tags: [#single-cell-spatial, papers]
doi: 10.1093/nar/gkr591
confidence: medium
aliases: ["Measuring cell identity in noisy biological systems."]
status: draft
updated: "2026-05-29"

# Measuring cell identity in noisy biological systems.




**期刊**: 
**DOI**: [10.1093/nar/gkr591](https://doi.org/10.1093/nar/gkr591)
**作者**: 

## 摘要
Global gene expression measurements are increasingly obtained as a function of cell type, spatial position within a tissue and other biologically meaningful coordinates. Such data should enable quantitative analysis of the cell-type specificity of gene expression, but such analyses can often be confounded by the presence of noise. We introduce a specificity measure Spec that quantifies the information in a gene's complete expression profile regarding any given cell type, and an uncertainty measure dSpec, which measures the effect of noise on specificity. Using global gene expression data from the mouse brain, plant root and human white blood cells, we show that Spec identifies genes with variable expression levels that are nonetheless highly specific of particular cell types. When samples from different individuals are used, dSpec measures genes' transcriptional plasticity in each cell type. Our approach is broadly applicable to mapped gene expression measurements in stem cell biology, developmental biology, cancer biology and biomarker identification. As an example of such applications, we show that Spec identifies a new class of biomarkers, which exhibit variable expression without compromising specificity. The approach provides a unifying theoretical framework for quantifying specificity in the presence of noise, which is widely applicable across diverse biological systems.


## 全文 (PMC)

### PERMALINK

*To whom correspondence should be addressed. Tel: +1 212 998 7663; Fax: +1 212 995 3691; Email:edo.kussell@nyu.edu Received 2011 Apr 25; Revised 2011 Jun 30; Accepted 2011 Jul 1; Issue date 2011 Nov; Collection date 2011 Nov. This is an Open Access article distributed under the terms of the Creative Commons Attribution Non-Commercial License (http://creativecommons.org/licenses/by-nc/3.0), which permits unrestricted non-commercial use, distribution, and reproduction in any medium, provided the original work is properly cited. Global gene expression measurements are increasingly obtained as a function of cell type, spatial position within a tissue and other biologically meaningful coordinates. Such data should enable quantitative analysis of the cell-type specificity of gene expression, but such analyses can often be confounded by the presence of noise. We introduce a specificity measure Spec that quantifies the information in a gene's complete expression profile regarding any given cell type, and an uncertainty measure dSpec, which measures the effect of noise on specificity. Using global gene expression data from the mouse brain, plant root and human white blood cells, we show that Spec identifies genes with variable expression levels that are nonetheless highly specific of particular cell types. When samples from different individuals are used, dSpec measures genes’ transcriptional plasticity in each cell type.Our approach is broadly applicable to mapped gene expression measurements in stem cell biology, developmental biology, cancer biology and biomarker identification. As an example of such applications, we show that Spec identifies a new class of biomarkers, which exhibit variable expression without compromising specificity. The approach provides a unifying theoretical framework for quantifying specificity in the presence of noise, which is widely applicable across diverse biological systems. Multicellular organisms have evolved a diversity of cell types, which

### Kenneth D Birnbaum

*To whom correspondence should be addressed. Tel: +1 212 998 7663; Fax: +1 212 995 3691; Email:edo.kussell@nyu.edu Received 2011 Apr 25; Revised 2011 Jun 30; Accepted 2011 Jul 1; Issue date 2011 Nov; Collection date 2011 Nov. This is an Open Access article distributed under the terms of the Creative Commons Attribution Non-Commercial License (http://creativecommons.org/licenses/by-nc/3.0), which permits unrestricted non-commercial use, distribution, and reproduction in any medium, provided the original work is properly cited.

### 

*To whom correspondence should be addressed. Tel: +1 212 998 7663; Fax: +1 212 995 3691; Email:edo.kussell@nyu.edu Received 2011 Apr 25; Revised 2011 Jun 30; Accepted 2011 Jul 1; Issue date 2011 Nov; Collection date 2011 Nov. This is an Open Access article distributed under the terms of the Creative Commons Attribution Non-Commercial License (http://creativecommons.org/licenses/by-nc/3.0), which permits unrestricted non-commercial use, distribution, and reproduction in any medium, provided the original work is properly cited.


**OA PDF**: https://academic.oup.com/nar/article-pdf/39/21/9093/16778478/gkr591.pdf


## 深度提炼

**物种**: Plant (unspecified)
**方法**: molecular biology / biochemistry
**来源**: DOI:10.1093/nar/gkr591
**来源类型**: PDF全文 (10.1093_nar_gkr591.pdf)

### 核心发现
1. Interestingly, in both organisms, we found that certain functional categories of genes tended to have similar domain sizes even if they were ex- pressed in different cell types (Supplementary Tables S2 and S3).
2. Using global gene expression data from the mouse brain, plant root and human white blood cells, we show that Spec identifies genes with variable expression levels that are none- theless highly specific of particular cell types.
3. As an example of such applications, we show that Spec identifies a new class of biomarkers, which exhibit variable expression without compromising specificity.
4. Gene B’s proﬁle exhibits inherently more variability among target cells, giving it reduced speciﬁcity even though its mean expression level is the same as gene A.
5. At a target intensity of 250, we determined empirically, using known markers, that a hybridization value of 50 represented a reliable ex- pression signal.
6. The test set contained treated samples for 13 hormones or hormone inhibitors, with no controls included (since the 12 other classes served as background or non-target classes).
7. Both methods capture highly speciﬁc markers with consistently high expression in the target class and low expression in the non-target class, although we note this is a relatively small percentage of the known markers.
8. Interestingly, its noise within the auxin data is relatively high and it is not likely to be identiﬁed as an auxin marker using traditional statistical methods.

## 相关文献

- [[alfalfa-anther-sc-atlas]]
- [[arabidopsis-root-sc-atlas-plantcell]]
- [[arabidopsis-root-sc-atlas-review]]
- [[arabidopsis-sam-scrna]]
- [[b3--bs1tAYpaCxa0fWZ49R6kw]]
- [[b3-9WavxKoXaOzbDzGmHSgUqw]]
- [[b3-BGiBJfPQalD0XaTAW6WgjQ]]



## PMC 全文


**来源类型**: PMC全文
**PMC ID**: PMC3241637

### INTRODUCTION
Multicellular organisms have evolved a diversity of cell types, which attain their distinct identity and function through differential gene activity. An understanding of the global regulation of genes within specialized cells addresses fundamental biological questions, such as how different cell types carry out distinct functions, how new cell types evolve, and which genes are the best diagnostic markers for cancer cells ( 1–3 ). Recent studies have characterized genome-wide transcription of cell types within an organ, such as in mouse brain ( 4 ), the Arabidopsis root ( 5 , 6 ) and other complex tissues ( 7 , 8 ). A theoretical basis for analyzing such data is needed to address questions about the global structure of gene expression within an organism, e.g . which components of the genome are dedicated to the specialization of single cell types? How is gene expression at the genome level partitioned and reused among specialized cells?
While the concept of cell specificity is fundamental in developmental biology, the field lacks a measure that quantifies the biological concept of specificity. The need for a quantitative description of specificity arises from the inherent variability of gene expression within cells and cell types ( 9–12 ). For example, Figure 1 a depicts three idealized genes whose distributions represent their biological variance in gene expression within three cell-type populations. Gene A varies in a narrow range in each cell type. Gene B's profile exhibits

### DISCUSSION
We have described a rigorous approach that uses information theory to formalize the concept of specificity in gene expression and to quantify cell identity in the presence of noise. More generally, the approach is applicable when biological measurements x (e.g. mRNA expression levels, protein abundances, epigenetic modifications, etc.) are mapped onto a biological organization y (e.g. cell types, spatial structure, treatments, disease states, etc.)—and the mapping is given by a probability distribution P ( x | y ). Information-based approaches in developmental biology have previously focused on transmission of information within developmental regulatory circuits ( 38 , 39 ). Our application of Spec here addresses a novel question, namely how much information does a gene's expression level provide about a cell's identity. As such, Spec provides both a unifying conceptual framework and a measurement tool in the study of cell identity, and with it the ability to quantify on a genome-wide scale this central concept of developmental biology.
The formulation presented here makes it possible to distinguish nois