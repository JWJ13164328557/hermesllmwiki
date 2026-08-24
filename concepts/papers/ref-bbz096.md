title: "单细胞RNA测序数据集的单细胞分类器的评估。"
created: 2026-05-28
type: concept
tags: [#methods-tools, papers]
doi: 10.1093/bib/bbz096
confidence: medium
aliases: ["单细胞RNA测序数据集的单细胞分类器的评估。"]
status: draft
updated: "2026-05-29"

# 单细胞RNA测序数据集的单细胞分类器的评估。




**期刊**: 
**DOI**: [10.1093/bib/bbz096](https://doi.org/10.1093/bib/bbz096)
**作者**: 

## 摘要
Single-cell RNA sequencing (scRNA-seq) has been rapidly developing and widely applied in biological and medical research. Identification of cell types in scRNA-seq data sets is an essential step before in-depth investigations of their functional and pathological roles. However, the conventional workflow based on clustering and marker genes is not scalable for an increasingly large number of scRNA-seq data sets due to complicated procedures and manual annotation. Therefore, a number of tools have been developed recently to predict cell types in new data sets using reference data sets. These methods have not been generally adapted due to a lack of tool benchmarking and user guidance. In this article, we performed a comprehensive and impartial evaluation of nine classification software tools specifically designed for scRNA-seq data sets. Results showed that Seurat based on random forest, SingleR based on correlation analysis and CaSTLe based on XGBoost performed better than others. A simple ensemble voting of all tools can improve the predictive accuracy. Under nonideal situations, such as small-sized and class-imbalanced reference data sets, tools based on cluster-level similarities have superior performance. However, even with the function of assigning 'unassigned' labels, it is still challenging to catch novel cell types by solely using any of the single-cell classifiers. This article provides a guideline for researchers to select and apply suitable classification tools in their analysis workflows and sheds some lights on potential direction of future improvement on classification tools.


## 全文 (PMC)

### PERMALINK

Corresponding author: Xiao Sun, State Key Laboratory of Bioelectronics, Biomedical Engineering School, Southeast University, Nanjing 210096, P. R. China. Tel.: +86-025-83792349; Fax: +86-025-83792349. E-mail:xsun@seu.edu.cn Corresponding author: Jue Fan, Singleron Biotechnologies, Nanjing 211800, P. R. China, Tel.: +86-025-58165529; Fax: +86-025-58165529. E-mail:fanjue@singleronbio.com Received 2019 Apr 2; Revised 2019 Jul 6; Accepted 2019 Jul 8; Collection date 2020 Sep. This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited. Single-cell RNA sequencing (scRNA-seq) has been rapidly developing and widely applied in biological and medical research. Identification of cell types in scRNA-seq data sets is an essential step before in-depth investigations of their functional and pathological roles. However, the conventional workflow based on clustering and marker genes is not scalable for an increasingly large number of scRNA-seq data sets due to complicated procedures and manual annotation. Therefore, a number of tools have been developed recently to predict cell types in new data sets using reference data sets. These methods have not been generally adapted due to a lack of tool benchmarking and user guidance. In this article, we performed a comprehensive and impartial evaluation of nine classification software tools specifically designed for scRNA-seq data sets. Results showed that Seurat based on random forest, SingleR based on correlation analysis and CaSTLe based on XGBoost performed better than others. A simple ensemble voting of all tools can improve the predictive accuracy. Under nonideal situations, such as small-sized and class-imbalanced reference data sets, tools based on cluster-level similarities have superior performance. However, even with t

### Xinlei Zhao

Corresponding author: Xiao Sun, State Key Laboratory of Bioelectronics, Biomedical Engineering School, Southeast University, Nanjing 210096, P. R. China. Tel.: +86-025-83792349; Fax: +86-025-83792349. E-mail:xsun@seu.edu.cn Corresponding author: Jue Fan, Singleron Biotechnologies, Nanjing 211800, P. R. China, Tel.: +86-025-58165529; Fax: +86-025-58165529. E-mail:fanjue@singleronbio.com Received 2019 Apr 2; Revised 2019 Jul 6; Accepted 2019 Jul 8; Collection date 2020 Sep. This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited.

### 

Corresponding author: Xiao Sun, State Key Laboratory of Bioelectronics, Biomedical Engineering School, Southeast University, Nanjing 210096, P. R. China. Tel.: +86-025-83792349; Fax: +86-025-83792349. E-mail:xsun@seu.edu.cn Corresponding author: Jue Fan, Singleron Biotechnologies, Nanjing 211800, P. R. China, Tel.: +86-025-58165529; Fax: +86-025-58165529. E-mail:fanjue@singleronbio.com Received 2019 Apr 2; Revised 2019 Jul 6; Accepted 2019 Jul 8; Collection date 2020 Sep. This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited.


**OA PDF**: https://academic.oup.com/bib/article-pdf/21/5/1581/36543433/bbz096.pdf


## 相关文献

- [[b3--bs1tAYpaCxa0fWZ49R6kw]]
- [[b3-9WavxKoXaOzbDzGmHSgUqw]]
- [[b3-Lj9ToIUf0z9y77oj4ELKlQ]]
- [[b4-4h7J0H3OPFzzltwSkI6mtg]]
- [[b4-78WuUWiztOxRe4n5MS2Pag]]
- [[b4-_igXoh0eWZRAu9l6Lg-fJg]]
- [[b4-ys8H9kH4cFVbPEuMHCg4nA]]



## PMC 全文


**来源类型**: PMC全文
**PMC ID**: PMC7947964

### Abstract
Single-cell RNA sequencing (scRNA-seq) has been rapidly developing and widely applied in biological and medical research. Identification of cell types in scRNA-seq data sets is an essential step before in-depth investigations of their functional and pathological roles. However, the conventional workflow based on clustering and marker genes is not scalable for an increasingly large number of scRNA-seq data sets due to complicated procedures and manual annotation. Therefore, a number of tools have been developed recently to predict cell types in new data sets using reference data sets. These methods have not been generally adapted due to a lack of tool benchmarking and user guidance. In this article, we performed a comprehensive and impartial evaluation of nine classification software tools specifically designed for scRNA-seq data sets. Results showed that Seurat based on random forest, SingleR based on correlation analysis and CaSTLe based on XGBoost performed better than others. A simple ensemble voting of all tools can improve the predictive accuracy. Under nonideal situations, such as small-sized and class-imbalanced reference data sets, tools based on cluster-level similarities have superior performance. However, even with the function of assigning ‘unassigned’ labels, it is still challenging to catch novel cell types by solely using any of the single-cell classifiers. This article provides a guideline for researchers to select and apply suitable classification tools in th

### Introduction
Categorizing cell identity is an essential step to have a comprehensive knowledge of the composition of human organs and tissues, which is also the foundation to further explore the cell basis of human diseases. Conventionally, techniques such as immunohistochemistry [ 1 ], fluorescence-activated cell sorting (FACS) [ 2 , 3 ] and morphological methods [ 4 ] are used to identify cell types. With the rapid development of single-cell separation and sequencing technologies [ 5–11 ], researchers can now easily obtain a large scale of gene expression profiles of ind