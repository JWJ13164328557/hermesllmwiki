title: "MultiQC ：在单个报告中汇总多个工具和样品的分析结果。"
created: 2026-05-28
type: concept
tags: [#methods-tools, papers]
doi: 10.1093/bioinformatics/btw354
confidence: medium
aliases: ["MultiQC ：在单个报告中汇总多个工具和样品的分析结果。"]
status: draft
updated: "2026-05-29"

# MultiQC ：在单个报告中汇总多个工具和样品的分析结果。




**期刊**: 
**DOI**: [10.1093/bioinformatics/btw354](https://doi.org/10.1093/bioinformatics/btw354)
**作者**: 

## 摘要
<h4>Motivation</h4>Fast and accurate quality control is essential for studies involving next-generation sequencing data. Whilst numerous tools exist to quantify QC metrics, there is no common approach to flexibly integrate these across tools and large sample sets. Assessing analysis results across an entire project can be time consuming and error prone; batch effects and outlier samples can easily be missed in the early stages of analysis.<h4>Results</h4>We present MultiQC, a tool to create a single report visualising output from multiple tools across many samples, enabling global trends and biases to be quickly identified. MultiQC can plot data from many common bioinformatics tools and is built to allow easy extension and customization.<h4>Availability and implementation</h4>MultiQC is available with an GNU GPLv3 license on GitHub, the Python Package Index and Bioconda. Documentation and example reports are available at http://multiqc.info<h4>Contact</h4>phil.ewels@scilifelab.se.


## 全文 (PMC)

### PERMALINK

*To whom correspondence should be addressed. Associate Editor: Jonathan Wren Received 2016 Apr 30; Revised 2016 Apr 30; Accepted 2016 May 29; Issue date 2016 Oct 1. This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited. Motivation:Fast and accurate quality control is essential for studies involving next-generation sequencing data. Whilst numerous tools exist to quantify QC metrics, there is no common approach to flexibly integrate these across tools and large sample sets. Assessing analysis results across an entire project can be time consuming and error prone; batch effects and outlier samples can easily be missed in the early stages of analysis. Results:We present MultiQC, a tool to create a single report visualising output from multiple tools across many samples, enabling global trends and biases to be quickly identified. MultiQC can plot data from many common bioinformatics tools and is built to allow easy extension and customization. Availability and implementation:MultiQC is available with an GNU GPLv3 license on GitHub, the Python Package Index and Bioconda. Documentation and example reports are available athttp://multiqc.info Contact:phil.ewels@scilifelab.se Advances in next-generation sequencing are leading to an avalanche of data. Whilst opening doors to new analysis types and experimental designs, expanding sample numbers make studies increasingly vulnerable to confounding batch effects (Leeket al.,2010;Meyer and Liu 2014;Taubet al.,2010). Such biases are often subtle and difficult to detect and require careful quality control measures. Most bioinformatics programs produce logs detailing their results. Dedicated QC tools such as FastQC (http://www.bioinformatics.babraham.ac.uk/projects/fastqc), Qualimap (Okonechnikovet al., 2015) and RSeQ

### Philip Ewels

*To whom correspondence should be addressed. Associate Editor: Jonathan Wren Received 2016 Apr 30; Revised 2016 Apr 30; Accepted 2016 May 29; Issue date 2016 Oct 1. This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited.

### 

*To whom correspondence should be addressed. Associate Editor: Jonathan Wren Received 2016 Apr 30; Revised 2016 Apr 30; Accepted 2016 May 29; Issue date 2016 Oct 1. This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited.


**OA PDF**: https://academic.oup.com/bioinformatics/article-pdf/32/19/3047/25072524/btw354.pdf


## 相关文献

- [[alfalfa-cadmium-sc-multiomics]]
- [[andrographis-msi-sc-spatial]]
- [[arabidopsis-root-regeneration-sc-multi]]
- [[arabidopsis-root-sc-atlas-review]]
- [[arabidopsis-sam-scrna]]
- [[artemisinin-scrna-glandular-trichomes]]
- [[b3--bs1tAYpaCxa0fWZ49R6kw]]



## PMC 全文


**来源类型**: PMC全文
**PMC ID**: PMC5039924

### Abstract
Motivation: Fast and accurate quality control is essential for studies involving next-generation sequencing data. Whilst numerous tools exist to quantify QC metrics, there is no common approach to flexibly integrate these across tools and large sample sets. Assessing analysis results across an entire project can be time consuming and error prone; batch effects and outlier samples can easily be missed in the early stages of analysis.
Results: We present MultiQC, a tool to create a single report visualising output from multiple tools across many samples, enabling global trends and biases to be quickly identified. MultiQC can plot data from many common bioinformatics tools and is built to allow easy extension and customization.
Availability and implementation: MultiQC is available with an GNU GPLv3 license on GitHub, the Python Package Index and Bioconda. Documentation and example reports are available at

### 1 Introduction
Advances in next-generation sequencing are leading to an avalanche of data. Whilst opening doors to new analysis types and experimental designs, expanding sample numbers make studies increasingly vulnerable to confounding batch effects ( Leek et al., 2010 ; Meyer and Liu 2014 ; Taub et al., 2010 ). Such biases are often subtle and difficult to detect and require careful quality control measures.
Most bioinformatics programs produce logs detailing their results. Dedicated QC tools such as FastQC ( http://www.bioinformatics.babraham.ac.uk/projects/fastqc ), Qualimap ( Okonechnikov et al. , 2015 ) and RSeQC ( Wang et al. , 2012 ) are excellent at highlighting potential problems in data. However, nearly all of these logs and reports are produced on a per-sample basis, requiring the user to find and compile QC results. This process is time consuming, repetitive and complex, making it prone to errors.
MultiQC addresses this problem by scanning given analysis directories for log files and QC reports, creating a single summary report visualizing results across all samples. Collecting data within a single report provides a fast way to scan key statistics quickly and easily ( Fig. 1 ). Shared plots allow accurate comparison between samples, allowing detection of subtle differences not noticeable when switching between different files. Data visualization aids batch effect detection and minimizes the risk of confounding factors affecting the results of the study. MultiQC is the first too

## 深度提炼

**物种**: Medicago spp.
**方法**: computational method
**来源**: DOI:10.1093/bioinformatics/btw354
**来源类型**: PMC全文
**文本来源**: NCBI PMC HTML (cleaned)

### 核心发现
1. Motivation: Fast and accurate quality control is essential for studies involving next-generation sequencing data.