#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""topic_gate.py — 八个核心主题的准入门（2026-11-03）。

为什么需要第二道门
------------------
`theme_filter` / `purity_gate` 回答的是“研究对象是不是植物”。
它们挡不住“植物是研究对象，但科学问题不属于本库八个主题”的论文，例如：

  * 鲜食微生物与沙门氏菌（植物是食品基质，不是植物生物学问题）
  * 茶多酚抑制金黄色葡萄球菌（植物提取物是药物来源）
  * 苹果汁保鲜 / 碳量子点包装膜（材料与食品工程）
  * 酸性矿山废水 / 污泥修复（环境工程）
  * 肉鸡生产性能（动物营养）

本模块只做“主题相关性”判定，不替代纯度闸门。策略是**窄拒绝**：
只有在命中明确的非主题语境，且缺少两个以上核心主题锚点时拒收。
宁可漏放，不可把植物免疫、作物代谢等正当论文误杀。
"""
from __future__ import annotations

import re

# 明确的非八主题语境。每条都要求上下文词，避免单词误杀。
OFF_TOPIC = (
    ('food-safety', re.compile(
        r"(food safety|foodborne|food preservation|shelf[- ]life|"
        r"apple juice|fruit juice|fresh[- ]cut|fresh produce|ready[- ]to[- ]eat|"
        r"food matrix|food processing|food microbiology|"
        r"salmonella|listeria|escherichia coli o157|staphylococcus aureus|"
        r"bacillus cereus|campylobacter|yersinia|bacteriophage)", re.I)),
    ('environmental-engineering', re.compile(
        r"(acid mine drainage|mine drainage|mine tailings|wastewater treatment|"
        r"activated sludge|soil remediation|phytoremediation|constructed wetland|"
        r"sediment remediation|industrial effluent)", re.I)),
    ('materials-engineering', re.compile(
        r"(carbon dots?|nanoplastic|microplastic|hydrogel|food packaging|"
        r"packaging film|wound dressing|4d printing|tissue engineering|"
        r"photocatalys|adsorption isotherm|nanocomposite)", re.I)),
    # 2026-11-03：非科学领域也要显式拒收。实证：一篇题为
    # "Comparative Analysis on post-Covid Digital Competency Frameworks"
    # 的教育学论文穿过全部上游闸门进库（only 因为没有任何已知坏桶命中）。
    ('non-science', re.compile(
        r"(digital competenc|digital literacy|curricul|pedagog|"
        r"education(al)? (policy|reform|system|technology)|"
        r"teaching (method|strategy|approach)|student (learning|achievement)|"
        r"teacher training|blended learning|e-learning platform|"
        r"bibliometric analysis of|scientometric|research evaluation policy|"
        r"questionnaire survey of farmers)",
        re.I)),
    ('animal-production', re.compile(
        r"(broiler|poultry|livestock|dairy cow|piglet|aquafeed|fish meal|"
        r"feed efficiency|growth performance|nutrient retention)", re.I)),
)

# 八个核心主题的强锚点。只在命中 >=2 个不同锚点时，才允许抵消非主题语境。
CORE_ANCHORS = (
    ('single-cell', re.compile(
        r"(single[- ]cell|scrna[- ]?seq|snrna[- ]?seq|spatial transcript|"
        r"stereo[- ]?seq|merfish|visium|cell atlas)", re.I)),
    ('development', re.compile(
        r"(meristem|organogenesis|embryogenesis|primordium|stem cell niche|"
        r"somatic embryogenesis|root development|flower development|"
        r"vascular development|cambium|xylem|phloem)", re.I)),
    ('metabolism', re.compile(
        r"(biosynthesis|secondary metabolite|flavonoid|anthocyanin|terpenoid|"
        r"alkaloid|phenylpropanoid|lignin biosynthesis|metabolic engineering)", re.I)),
    ('hormone', re.compile(
        r"(auxin|cytokinin|gibberellin|brassinosteroid|abscisic acid|"
        r"jasmonic acid|salicylic acid|ethylene signaling|strigolactone)", re.I)),
    ('stress-immunity', re.compile(
        r"(drought stress|salt stress|cold stress|heat stress|plant immunity|"
        r"effector-triggered|nlr|ros burst|defense response|pathogen resistance)", re.I)),
    ('epigenetics', re.compile(
        r"(histone|chromatin|dna methylation|h3k27|h3k4|atac[- ]seq|"
        r"chip[- ]seq|enhancer|transcription factor binding)", re.I)),
    ('genomics', re.compile(
        r"(genome assembly|pangenome|polyploid|phylogenom|synteny|"
        r"comparative genomic|gene family expansion|domestication)", re.I)),
    ('methods', re.compile(
        r"(benchmark|workflow|pipeline|algorithm|software|toolkit|"
        r"database|web server|normalization method|imputation)", re.I)),
)


def _off_topic_label(text):
    for label, rx in OFF_TOPIC:
        m = rx.search(text)
        if m:
            return label, m.group(1)
    return '', ''


def _core_hits(text):
    return [name for name, rx in CORE_ANCHORS if rx.search(text)]


def is_core_topic(title, abstract='', journal=''):
    """返回 (ok, reason)。

    ok=False 仅表示“明显不属于八个主题”，调用方应拒收并写入审计日志。
    方法学论文不受此门限制：它们是其他主题的工具，不是食品/材料/环境论文。
    """
    text = ' '.join([title or '', abstract or '', journal or ''])
    # 文本过短时无法判定主题，不能默认放行（2026-11-03 修复 fail-open）。
    if len(text.strip()) < 30 and not _core_hits(text):
        return False, 'insufficient-text'
    label, token = _off_topic_label(text)
    if not label:
        return True, ''
    core = _core_hits(text)
    if len(core) >= 2:
        return True, 'core-anchors=' + ','.join(core[:3])
    if label == 'animal-production':
        return False, 'off-topic:animal-production:%s' % token
    return False, 'off-topic:%s:%s (core=%s)' % (label, token, ','.join(core) or 'none')


if __name__ == '__main__':
    cases = [
        ('Tea polyphenols inhibit Staphylococcus aureus in vitro', ''),
        ('Microbiota of fresh produce and Salmonella survival', ''),
        ('Bacteriophage against Yersinia enterocolitica in food', ''),
        ('Carbon dots from apple juice for packaging film', ''),
        ('Acid mine drainage remediation by constructed wetland', ''),
        ('Broiler performance under dietary supplementation', ''),
        ('Arabidopsis immunity to Pseudomonas syringae effectors', ''),
        ('Single-cell atlas of rice root meristem', ''),
        ('Flavonoid biosynthesis in maize under drought stress', ''),
        ('Chromosome-level genome assembly and pangenome of rice', ''),
    ]
    for t, a in cases:
        print(('OK ' if is_core_topic(t, a)[0] else 'NO '), is_core_topic(t, a)[1], t)
