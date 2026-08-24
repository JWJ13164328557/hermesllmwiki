title: Near-optimal probabilistic RNA-seq quantification.
created: 2026-05-28
type: concept
tags: [#genomics-evolution, papers]
doi: 10.1038/nbt.3519
confidence: medium
aliases: ["Near-optimal probabilistic RNA-seq quantification."]
status: draft
updated: "2026-05-29"

# Near-optimal probabilistic RNA-seq quantification.




**期刊**: 
**DOI**: [10.1038/nbt.3519](https://doi.org/10.1038/nbt.3519)
**作者**: 

## 摘要
We present kallisto, an RNA-seq quantification program that is two orders of magnitude faster than previous approaches and achieves similar accuracy. Kallisto pseudoaligns reads to a reference, producing a list of transcripts that are compatible with each read while avoiding alignment of individual bases. We use kallisto to analyze 30 million unaligned paired-end RNA-seq reads in <10 min on a standard laptop computer. This removes a major computational bottleneck in RNA-seq analysis.



⚠️ 全文需VPN/机构访问


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
**方法**: transcriptomics (RNA-seq), genomics, qRT-PCR validation
**来源**: DOI:10.1038/nbt.3519
**来源类型**: PDF全文 (10.1038_nbt.3519.pdf)

### 核心发现
1. For each simulation, we report the accuracy as the median relative difference in the estimated read count of each transcript.
2. While it is expected that the variance on abundance estimates should increase approximately linearly with abundance13, our results show that there is high variability in uncertainty of estimates as a result of the complex structure of similarity among transcripts, especially multiple isoforms of genes.
3. Notably, the simulation was based on RSEM, for generating both the parameters and then the data using them.
4. Only the k-mer length and the mean of the fragment length distribution are required for quantification.