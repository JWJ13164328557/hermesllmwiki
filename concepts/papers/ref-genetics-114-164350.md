title: fastSTRUCTURE: variational inference of population structure in large SNP data s
created: 2026-05-28
type: concept
tags: [#methods-tools, papers]
doi: 10.1534/genetics.114.164350
confidence: medium
aliases: ["fastSTRUCTURE: variational inference of population structure in large SNP data s"]
status: draft
updated: "2026-05-29"

# fastSTRUCTURE: variational inference of population structure in large SNP data s




**期刊**: 
**DOI**: [10.1534/genetics.114.164350](https://doi.org/10.1534/genetics.114.164350)
**作者**: 

## 摘要
Tools for estimating population structure from genetic data are now used in a wide variety of applications in population genetics. However, inferring population structure in large modern data sets imposes severe computational challenges. Here, we develop efficient algorithms for approximate inference of the model underlying the STRUCTURE program using a variational Bayesian framework. Variational methods pose the problem of computing relevant posterior distributions as an optimization problem, allowing us to build on recent advances in optimization theory to develop fast inference tools. In addition, we propose useful heuristic scores to identify the number of populations represented in a data set and a new hierarchical prior to detect weak population structure in the data. We test the variational algorithms on simulated data and illustrate using genotype data from the CEPH-Human Genome Diversity Panel. The variational algorithms are almost two orders of magnitude faster than STRUCTURE and achieve accuracies comparable to those of ADMIXTURE. Furthermore, our results show that the heuristic scores for choosing model complexity provide a reasonable range of values for the number of populations represented in the data, with minimal bias toward detecting structure when it is very weak. Our algorithm, fastSTRUCTURE, is freely available online at http://pritchardlab.stanford.edu/structure.html.


## 全文 (PMC)

### PERMALINK

Available freely online through the author-supported open access option. Supporting information is available online athttp://www.genetics.org/lookup/suppl/doi:10.1534/genetics.114.164350/-/DC1. Corresponding author: Stanford University, 300 Pasteur Dr., Alway Bldg., M337, Stanford, CA 94305. E-mail:rajanil@stanford.edu Received 2013 Dec 2; Accepted 2014 Mar 25; Issue date 2014 Jun. Available freely online through the author-supported open access option. Tools for estimating population structure from genetic data are now used in a wide variety of applications in population genetics. However, inferring population structure in large modern data sets imposes severe computational challenges. Here, we develop efficient algorithms for approximate inference of the model underlying the STRUCTURE program using a variational Bayesian framework. Variational methods pose the problem of computing relevant posterior distributions as an optimization problem, allowing us to build on recent advances in optimization theory to develop fast inference tools. In addition, we propose useful heuristic scores to identify the number of populations represented in a data set and a new hierarchical prior to detect weak population structure in the data. We test the variational algorithms on simulated data and illustrate using genotype data from the CEPH–Human Genome Diversity Panel. The variational algorithms are almost two orders of magnitude faster than STRUCTURE and achieve accuracies comparable to those of ADMIXTURE. Furthermore, our results show that the heuristic scores for choosing model complexity provide a reasonable range of values for the number of populations represented in the data, with minimal bias toward detecting structure when it is very weak. Our algorithm, fastSTRUCTURE, is freely available online athttp://pritchardlab.stanford.edu/structure.html. Keywords:variational inference, population structure IDENTIFYING the degree of admixture in individuals and inferring the populatio

### Anil Raj

Available freely online through the author-supported open access option. Supporting information is available online athttp://www.genetics.org/lookup/suppl/doi:10.1534/genetics.114.164350/-/DC1. Corresponding author: Stanford University, 300 Pasteur Dr., Alway Bldg., M337, Stanford, CA 94305. E-mail:rajanil@stanford.edu Received 2013 Dec 2; Accepted 2014 Mar 25; Issue date 2014 Jun. Available freely online through the author-supported open access option.

### 

Available freely online through the author-supported open access option. Supporting information is available online athttp://www.genetics.org/lookup/suppl/doi:10.1534/genetics.114.164350/-/DC1. Corresponding author: Stanford University, 300 Pasteur Dr., Alway Bldg., M337, Stanford, CA 94305. E-mail:rajanil@stanford.edu Received 2013 Dec 2; Accepted 2014 Mar 25; Issue date 2014 Jun. Available freely online through the author-supported open access option.

### 

Communicating editor: M. K. Uyenoyama


**OA PDF**: https://www.genetics.org/content/genetics/197/2/573.full.pdf


## 相关文献

- [[aba-biosynthesis-stress]]
- [[alfalfa-anther-sc-atlas]]
- [[arabidopsis-root-sc-atlas-plantcell]]
- [[arabidopsis-root-sc-atlas-review]]
- [[arabidopsis-sam-scrna]]
- [[b3--bs1tAYpaCxa0fWZ49R6kw]]
- [[b3-9WavxKoXaOzbDzGmHSgUqw]]



## PMC 全文


**来源类型**: PMC全文
**PMC ID**: PMC4063916

### Abstract
Tools for estimating population structure from genetic data are now used in a wide variety of applications in population genetics. However, inferring population structure in large modern data sets imposes severe computational challenges. Here, we develop efficient algorithms for approximate inference of the model underlying the STRUCTURE program using a variational Bayesian framework. Variational methods pose the problem of computing relevant posterior distributions as an optimization problem, allowing us to build on recent advances in optimization theory to develop fast inference tools. In addition, we propose useful heuristic scores to identify the number of populations represented in a data set and a new hierarchical prior to detect weak population structure in the data. We test the variational algorithms on simulated data and illustrate using genotype data from the CEPH–Human Genome Diversity Panel. The variational algorithms are almost two orders of magnitude faster than STRUCTURE and achieve accuracies comparable to those of ADMIXTURE. Furthermore, our results show that the heuristic scores for choosing model complexity provide a reasonable range of values for the number of populations represented in the data, with minimal bias toward detecting structure when it is very weak. Our algorithm, fastSTRUCTURE, is freely available online at http://pritchardlab.stanford.edu/structure.html .
Keywords: variational inference, population structure
IDENTIFYING the degree of admixtu

### Discussion
Our analyses on simulated and natural data sets demonstrate that fastSTRUCTURE estimates approximate posterior distributions on ancestry proportions 2 orders of magnitude faster than STRUCTURE, with ancestry estimates and prediction accuracies that are comparable to those of ADMIXTURE. Posing the problem of inference in terms of an optimization problem allows us to draw on powerful tools in convex optimization and plays an important role in the gain in speed achieved by variational inference schemes, when compared to the Gibbs sampling scheme used in STRUCTURE. In addition, the flexible logistic prior enables us to resolve subtle structure underlying a data set. The considerable improvement in runtime with comparable accuracies allows the application of these methods to large genotype data sets that are steadily becoming the norm in studies of population history, genetic association with disease, and conservation biology.
The choice of model complexity, or the number of populations required to explain structure in a data set, is a difficult problem associated with the inference of population structure. Unlike in maximum-lik