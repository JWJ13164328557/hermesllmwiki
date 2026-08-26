#!/usr/bin/env python3
"""
物种权威注册表 — 植物单细胞/空间组学知识库 统一物种名单
==========================================================
背景:
  原三处脚本各自维护物种名单, 互相漂移且缺失知识库高频物种
  (苹果/梨/柑橘/蔷薇/豌豆/苜蓿/无花果/银杏等均未进 PubMed 检索),
  导致"兜底校验有这些词、检索入口却没有"——检索行为与预期不符。

本模块作为唯一权威来源, 供以下脚本共享, 消除漂移:
  - daily_update.py            (PubMed 检索: AND 限定物种)
  - multi_source_search.py     (多源检索: 同样 AND 限定)
  - daily_full_pipeline.py     (多源导入 is_plant_content 校验)
  - theme_filter.py            (防污染三重门 SPECIES_PLANT_TERMS)

名单口径(2026-08-26 重整):
  ① 知识库 concepts/papers 实际高频物种(≥10篇命中)
  ② 植物单细胞/空间组学领域公认的模式 + 主要经济/园艺物种
  ③ 代表药用/次生代谢物种(丹参/青蒿/人参/穿心莲/银杏等)
  ④ 保留旧名单已有但低频的物种, 不擅自删除(宁多勿漏, 靠主题过滤兜底防污染)

两类词表(用途不同, 共同维护):
  SEARCH_TERMS  : PubMed/多源 检索 AND 限定 —— 用官方通用名+关键学名, 供 eutils 查询
  CONTENT_TERMS : 内容校验(是/否植物) —— 词根/属名变体, 尽可能全, 供子串匹配
"""
import os

# ══════════════════════════════════════════════════════════════
# 一、检索限定词表 (SEARCH)
#    用于 construction of PubMed / OpenAlex / Crossref 查询, 与 AND 拼接
#    形式: "物种名"[Title/Abstract]  —— 官方通用名 + 部分学名(提高召回)
# ══════════════════════════════════════════════════════════════
SEARCH_SPECIES = [
    # ── 模式植物 (单细胞/空间组学主要体系)
    "Arabidopsis", "Marchantia", "Physcomitrium", "moss", "fern",
    # ── 主粮/大田作物
    "rice", "Oryza", "wheat", "Triticum", "maize", "Zea", "sorghum",
    "soybean", "Glycine", "barley", "Hordeum", "millet", "Setaria",
    "oat", "rye", "cassava", "Manihot", "potato", "Solanum tuberosum",
    "sweet potato", "Ipomoea",
    # ── 油料/蛋白作物
    "rapeseed", "canola", "Brassica", "sunflower", "Helianthus",
    "peanut", "Arachis", "sesame", "pea", "Pisum", "chickpea", "Cicer",
    "common bean", "Phaseolus", "mung bean", "vigna", "alfalfa", "Medicago",
    "clover", "Trifolium",
    # ── 经济作物/纤维
    "cotton", "Gossypium", "tobacco", "Nicotiana", "sugarcane", "Saccharum",
    "jute", "kenaf",
    # ── 果蔬
    "tomato", "cucumber", "cucumis", "melon", "watermelon", "Citrullus",
    "pepper", "Capsicum", "pumpkin", "squash", "eggplant", "aubergine",
    "carrot", "Daucus", "onion", "Allium", "garlic", "ginger", "radish",
    "cabbage", "cauliflower", "broccoli", "spinach", "celery", "lettuce",
    "strawberry", "Fragaria",
    # ── 果树/热带/木本
    "apple", "Malus", "pear", "Pyrus", "citrus", "orange", "grapefruit",
    "grape", "Vitis", "banana", "Musa", "kiwifruit", "Actinidia",
    "peach", "apricot", "plum", "cherry", "blueberry", "mango", "papaya",
    "litchi", "longan", "pineapple", "avocado", "date palm", "olive",
    "fig", "Ficus",
    # ── 经济林/用材/观赏
    "poplar", "Populus", "eucalyptus", "pine", "Pinus", "spruce", "Picea",
    "willow", "Salix", "beech", "rubber tree", "Hevea", "oil palm", "Elaeis",
    "orchid", "rose", "Rosa", "chrysanthemum", "bamboo", "ginkgo", "Ginkgo",
    # ── 茶/咖啡/饮料
    "tea", "Camellia", "coffee", "Coffea", "cocoa", "Theobroma",
    # ── 药用/次生代谢
    "Salvia", "Artemisia", "Panax", "Andrographis", "licorice", "Glycyrrhiza",
    "Coptis", "Taxus", "yew",
    # ── 藻类/模式微藻
    "Chlamydomonas", "Chlorella", "microalgae", "seaweed", "kelp", "Laminaria",
    "Porphyra", "seaweed",
]

# ══════════════════════════════════════════════════════════════
# 二、内容校验词表 (CONTENT)
#    判断一篇文献是否与植物相关 —— 词根/属名/变体, 子串匹配, 尽量收全
#    含旧名单全部词 + 新增高频物种 + 常用词根
# ══════════════════════════════════════════════════════════════
CONTENT_SPECIES = [
    # 模式植物
    'arabidops', 'thaliana', 'marchantia', 'physcomitrium', 'physcomitrella',
    'moss', 'fern', 'liverwort',
    # 主粮/大田 (含属名)
    'oryza', 'rice', 'triticum', 'wheat', 'zea', 'maize', 'sorghum',
    'glycine', 'soybean', 'hordeum', 'barley', 'setaria', 'millet',
    'avena', 'oat', 'secale', 'rye', 'manihot', 'cassava',
    'solanum', 'potato', 'tuberosum', 'ipomoea', 'sweet potato',
    # 油料/蛋白
    'brassica', 'rapeseed', 'canola', 'helianthus', 'sunflower',
    'arachis', 'peanut', 'sesamum', 'sesame', 'pisum', 'pea',
    'cicer', 'chickpea', 'phaseolus', 'bean', 'vigna', 'mung',
    'medicago', 'alfalfa', 'trifolium', 'clover',
    # 经济作物
    'gossypium', 'cotton', 'nicotiana', 'tobacco', 'saccharum', 'sugarcane',
    'corchorus', 'jute', 'hibiscus', 'kenaf',
    # 果蔬
    'lycopersicum', 'tomato', 'cucumis', 'cucumber', 'melon', 'citrullus',
    'watermelon', 'capsicum', 'pepper', 'cucurbita', 'pumpkin', 'squash',
    'aubergine', 'eggplant', 'daucus', 'carrot', 'allium', 'onion', 'garlic',
    'zingiber', 'ginger', 'raphanus', 'radish', 'brassica oleracea', 'cabbage',
    'cauliflower', 'broccoli', 'spinach', 'apium', 'celery', 'lactuca', 'lettuce',
    'fragaria', 'strawberry',
    # 果树/热带/木本
    'malus', 'apple', 'pyrus', 'pear', 'citrus', 'orange', 'grapefruit',
    'vitis', 'grape', 'musa', 'banana', 'actinidia', 'kiwi',
    'prunus', 'peach', 'apricot', 'plum', 'cherry', 'vaccinium', 'blueberry',
    'mangifera', 'mango', 'carica', 'papaya', 'litchi', 'longan',
    'ananas', 'pineapple', 'persea', 'avocado', 'phoenix', 'date palm',
    'olea', 'olive', 'ficus', 'fig',
    # 经济林/用材/观赏
    'populus', 'poplar', 'eucalyptus', 'pinus', 'pine', 'picea', 'spruce',
    'salix', 'willow', 'fagus', 'beech', 'hevea', 'rubber', 'elaeis', 'oil palm',
    'orchid', 'rosa', 'rose', 'chrysanthemum', 'bamboo', 'ginkgo', 'lotus', 'nelumbo',
    # 茶/咖啡/饮料
    'camellia', 'tea', 'coffea', 'coffee', 'theobroma', 'cocoa',
    # 药用/次生代谢
    'salvia', 'artemisia', 'panax', 'ginseng', 'andrographis', 'glycyrrhiza',
    'licorice', 'coptis', 'taxus', 'yew', 'tanshinone', 'artemisinin',
    # 藻类/微藻
    'chlamydomonas', 'chlorella', 'microalga', 'seaweed', 'kelp', 'laminaria',
    'porphyra', 'phaeophyceae', 'rhodophyta',
    # 通用植物/组织词 (兜底, 与主题过滤协同)
    'plant', 'crop', 'seedling', 'leaf', 'root', 'inflorescence', 'xylem',
    'phloem', 'chlorophyll', 'photosynth', 'chloroplast', 'phytochrome',
    'flower', 'pollen', 'anther', 'seed', 'fruit', 'floral', 'grain',
    'leaf senescence', 'canopy', 'rootstock', 'scion', 'stomata', 'trichome',
    'meristem', 'guard cell', 'photoperiod', 'circadian',
]

# 供 content 匹配的"纯物种词"(不含 plant/crop 等极泛词) — 用于排除纯通用词误判
SPECIES_ONLY = [t for t in CONTENT_SPECIES if t not in {
    'plant', 'crop', 'seedling', 'leaf', 'root', 'inflorescence', 'xylem',
    'phloem', 'chlorophyll', 'photosynth', 'chloroplast', 'phytochrome',
    'flower', 'pollen', 'anther', 'seed', 'fruit', 'floral', 'grain',
    'leaf senescence', 'canopy', 'rootstock', 'scion', 'stomata', 'trichome',
    'meristem', 'guard cell', 'photoperiod', 'circadian', 'flower',
    'bean',
}]


def has_plant_species(text):
    """判断 text(标题+摘要) 是否命中任一物种词。"""
    t = (text or '').lower()
    return any(term in t for term in CONTENT_SPECIES)


def build_search_and_clause():
    """构造 PubMed 检索用 AND 物种限定子句 (与外部查询串拼接)。"""
    return '(' + ' OR '.join(f'"{s}"[Title/Abstract]' for s in SEARCH_SPECIES) + ')'


def build_search_or_clause_plain():
    """构造多源(非PubMed)检索用纯 OR 物种限定 (不含[Title/Abstract])。"""
    return '(' + ' OR '.join(f'"{s}"' for s in SEARCH_SPECIES) + ')'


# 向后兼容旧引用别名
PLANT_SPECIES_LEGACY = SEARCH_SPECIES
PLANT_TERMS_LEGACY = CONTENT_SPECIES
SPECIES_PLANT_TERMS = CONTENT_SPECIES

if __name__ == '__main__':
    print(f"检索物种 SEARCH: {len(SEARCH_SPECIES)} 项")
    print(f"内容物种 CONTENT: {len(CONTENT_SPECIES)} 项")
    print("检索子句示例:", build_search_and_clause()[:200] + "...")
