#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""species_patterns.py — 物种识别的唯一权威表（规范名 + 同义写法）。

为什么单独成模块
----------------
历史上 deep_curate_all.py 自带一份物种正则，species_registry.py 另有一份
检索/防污染词表，两者口径漂移。本模块只负责一件事：
把文本里出现的物种映射为可展示的规范学名，并按「标题 > 摘要 > 全文」排序。

它与 species_registry 的分工：
  * species_registry.SEARCH_SPECIES  -> 检索式里的物种限定词
  * species_registry.CONTENT_SPECIES -> 防污染判定的通用词干（arabidops / rice ...）
  * species_patterns.SPECIES_PATTERNS -> 本模块：正则 -> 规范学名（用于页面展示）

排序为何重要
------------
旧实现按下表顺序扫描全文并取前 3 个，导致「引言里提到拟南芥」的香蕉论文被标成
Arabidopsis thaliana。物种顺序应反映研究对象的实际重要性，因此改为按出现位置加权
（标题 10 分 / 摘要 5 分 / 全文 1 分；同一文本内的重复出现也计入分数），
同分再按规范名字母序，保证跨进程、跨运行完全确定。
"""
import re

SPECIES_PATTERNS = [
    (r'\bArabidopsis\s+thaliana\b', 'Arabidopsis thaliana'),
    (r'\bOryza\s+sativa\b|\brice\b', 'Oryza sativa'),
    (r'\bZea\s+mays\b|\bmaize\b|\bcorn\b', 'Zea mays'),
    (r'\bSolanum\s+lycopersicum\b|\btomato\b', 'Solanum lycopersicum'),
    (r'\bMalus\s+(domestica|x\s+domestica)\b|\bapple\b', 'Malus domestica'),
    (r'\bGlycine\s+max\b|\bsoybean\b', 'Glycine max'),
    (r'\bNicotiana\s+(tabacum|benthamiana)\b|\btobacco\b', 'Nicotiana tabacum'),
    (r'\bBrassica\s+napus\b|\brapeseed\b|\bcanola\b', 'Brassica napus'),
    (r'\bTriticum\s+aestivum\b|\bwheat\b', 'Triticum aestivum'),
    (r'\bHordeum\s+vulgare\b|\bbarley\b', 'Hordeum vulgare'),
    (r'\bPopulus\b|\bpoplar\b', 'Populus spp.'),
    (r'\bMedicago\s+(truncatula|sativa)\b|\balfalfa\b', 'Medicago spp.'),
    (r'\bVitis\s+vinifera\b|\bgrapevine\b|\bgrape\b', 'Vitis vinifera'),
    (r'\bCitrus\s+(sinensis|reticulata|clementina|maxima|limon|aurantium)\b|\b(citrus|sweet\s+orange|navel\s+orange|blood\s+orange|mandarin|tangerine|clementine|pomelo|grapefruit|lemon)\b', 'Citrus spp.'),
    (r'\bFragaria\b|\bstrawberry\b', 'Fragaria × ananassa'),
    (r'\bGossypium\b|\bcotton\b', 'Gossypium hirsutum'),
    (r'\bSorghum\s+bicolor\b|\bsorghum\b', 'Sorghum bicolor'),
    (r'\bMusa\s+(acuminata|balbisiana)\b|\bbanana\b', 'Musa spp.'),
    (r'\bManihot\s+esculenta\b|\bcassava\b', 'Manihot esculenta'),
    (r'\bHelianthus\s+annuus\b|\bsunflower\b', 'Helianthus annuus'),
    (r'\bTheobroma\s+cacao\b|\bcacao\b|\bcocoa\b', 'Theobroma cacao'),
    (r'\bCoffea\b|\bcoffee\b', 'Coffea spp.'),
    (r'\bCamellia\s+sinensis\b|\btea\s+plant\b', 'Camellia sinensis'),
    (r'\bPinus\b|\bpine\b', 'Pinus spp.'),
    (r'\bPicea\b|\bspruce\b', 'Picea spp.'),
    (r'\bEucalyptus\b', 'Eucalyptus spp.'),
    (r'\bQuercus\b|\boak\b', 'Quercus spp.'),
    (r'\bSetaria\s+(viridis|italica)\b|\bfoxtail\s+millet\b', 'Setaria spp.'),
    (r'\bPhaseolus\s+vulgaris\b|\bcommon\s+bean\b', 'Phaseolus vulgaris'),
    (r'\bCicer\s+arietinum\b|\bchickpea\b', 'Cicer arietinum'),
    (r'\bPisum\s+sativum\b|\bpea\b', 'Pisum sativum'),
    (r'\bBeta\s+vulgaris\b|\bsugar\s+beet\b|\bbeetroot\b', 'Beta vulgaris'),
    (r'\bBrachypodium\s+distachyon\b', 'Brachypodium distachyon'),
    (r'\bSelaginella\b', 'Selaginella spp.'),
    (r'\bPhyscomitrium\s+patens\b|\bPhyscomitrella\b', 'Physcomitrium patens'),
    (r'\bMarchantia\s+polymorpha\b', 'Marchantia polymorpha'),
    (r'\bChlamydomonas\s+reinhardtii\b', 'Chlamydomonas reinhardtii'),
    (r'\bAmborella\s+trichopoda\b', 'Amborella trichopoda'),
    (r'\bCeratopteris\s+richardii\b|\bfern\b', 'Ceratopteris richardii'),
    (r'\bDaucus\s+carota\b|\bcarrot\b', 'Daucus carota'),
    (r'\bSolanum\s+tuberosum\b|\bpotato\b', 'Solanum tuberosum'),
    (r'\bCucumis\s+(sativus|melo)\b|\b(cucumber|melon)\b', 'Cucumis spp.'),
    (r'\bCapsicum\s+annuum\b|\bpepper\b', 'Capsicum annuum'),
    (r'\bAllium\s+(cepa|sativum)\b|\b(onion|garlic)\b', 'Allium spp.'),
    (r'\bSpinacia\s+oleracea\b|\bspinach\b', 'Spinacia oleracea'),
    (r'\bLactuca\s+sativa\b|\blettuce\b', 'Lactuca sativa'),
    (r'\bPrunus\s+persica\b|\bpeach\b', 'Prunus persica'),
    (r'\bPyrus\b|\bpear\b', 'Pyrus spp.'),
    (r'\bPanax\s+(ginseng|notoginseng|quinquefolius)\b|\bginseng\b', 'Panax spp.'),
    (r'\bTaxus\b|\byew\b', 'Taxus spp.'),
    (r'\bArtemisia\s+annua\b|\bsweet\s+wormwood\b', 'Artemisia annua'),
    (r'\bSalvia\s+miltiorrhiza\b|\bdanshen\b', 'Salvia miltiorrhiza'),
    (r'\bGinkgo\s+biloba\b', 'Ginkgo biloba'),
    (r'\bCatharanthus\s+roseus\b|\bperiwinkle\b', 'Catharanthus roseus'),
    (r'\bHevea\s+brasiliensis\b|\brubber\b', 'Hevea brasiliensis'),
    (r'\bJuglans\s+regia\b|\bwalnut\b', 'Juglans regia'),
    (r'\bAnanas\s+comosus\b|\bpineapple\b', 'Ananas comosus'),
    (r'\bMorus\b|\bmulberry\b', 'Morus alba'),
    (r'\bFicus\s+carica\b|\bcommon\s+fig\b|\bedible\s+fig\b', 'Ficus carica'),
    (r'\bPunica\s+granatum\b|\bpomegranate\b', 'Punica granatum'),
    (r'\bActinidia\b|\bkiwifruit\b', 'Actinidia spp.'),
    (r'\bVaccinium\b|\bblueberry\b|\bcranberry\b', 'Vaccinium spp.'),
    (r'\bRubus\b|\b(blackberry|raspberry)\b', 'Rubus spp.'),
    (r'\bFagopyrum\b|\bbuckwheat\b', 'Fagopyrum esculentum'),
    (r'\bIpomoea\s+batatas\b|\bsweet\s+potato\b', 'Ipomoea batatas'),
    (r'\bDioscorea\b|\byam\b', 'Dioscorea spp.'),
    (r'\bRosa\s+(hybrida|rugosa|chinensis)\b|\brose\b', 'Rosa spp.'),
    (r'\bZingiber\s+officinale\b|\bginger\b', 'Zingiber officinale'),
    (r'\bCrocus\b|\bsaffron\b', 'Crocus sativus'),
    (r'\bLilium\b|\blily\b', 'Lilium spp.'),
    (r'\bPetunia\b', 'Petunia hybrida'),
    (r'\bCoptis\b', 'Coptis spp.'),
    (r'\bFallopia\s+multiflora\b', 'Fallopia multiflora'),
    (r'\bDracaena\b', 'Dracaena spp.'),
    (r'\bLycium\b|\bgoji\b|\bwolfberry\b', 'Lycium barbarum'),
    (r'\bPaeonia\b|\bpeony\b', 'Paeonia spp.'),
    (r'\bCarthamus\b|\bsafflower\b', 'Carthamus tinctorius'),
    (r'\bCryptotaenia\b', 'Cryptotaenia japonica'),
    (r'\bMiscanthus\b', 'Miscanthus spp.'),
]

def _count(pat, text):
    return len(re.findall(pat, text, re.I)) if text else 0


def score_species(title='', abstract='', fulltext=''):
    """给每个规范学名打分，返回 [(canonical_name, score), ...]，分数降序、名称升序。"""
    scored = []
    for pat, name in SPECIES_PATTERNS:
        s = 10 * _count(pat, title) + 5 * _count(pat, abstract) + _count(pat, fulltext)
        if s:
            scored.append((name, s))
    scored.sort(key=lambda x: (-x[1], x[0]))
    return scored


def order_species(title='', abstract='', fulltext='', limit=5):
    """按重要性排序的规范学名列表；无命中返回 ['Plant (unspecified)']。"""
    names = [n for n, _s in score_species(title, abstract, fulltext)][:limit]
    return names or ['Plant (unspecified)']


def primary_species(title='', abstract='', fulltext=''):
    return order_species(title, abstract, fulltext, limit=1)[0]


def canonical_names():
    """表中所有规范名（去重、保序）。供文档与人工核对使用；测试见 tests/test_kb_quality.py。"""
    seen = []
    for _pat, name in SPECIES_PATTERNS:
        if name not in seen:
            seen.append(name)
    return seen
