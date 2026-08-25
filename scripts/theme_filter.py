# -*- coding: utf-8 -*-
"""
theme_filter.py — 知识库主题相关性校验（防污染防线）
======================================================
用法（供 daily_update / daily_full_pipeline / multi_source_search 等共用）：

    from theme_filter import is_relevant_plant_paper, NONPLANT_JOURNAL_BLACKLIST

    ok = is_relevant_plant_paper(title, abstract, journal)
    # ok=False → 拒绝导入（医学/物理/能源/社科/纯动物等非植物内容）

设计原则（2026-08-25 三层清理沉淀的经验）：
  1. JCR 植物/农学权威期刊白名单放行（由调用方优先生效，见 jcr_whitelist）
  2. 期刊名黑名单（增强）：医学/免疫/肿瘤/内分泌/药理/细胞死亡/兽医/神经/物理/能源/法学/社科等
  3. 内容"人类/动物医学强词"反向拦截（标题+摘要含 cancer patient / clinical trial /
     drug delivery / neuronal / cardiovascular / serum / renal 等 → 拒绝）
  4. 内容"植物强词"正向判定（arabidopsis / chloroplast / flavonoid / xylem 等 → 放行）
  判定逻辑：
    - 若标题+摘要含"人类/动物医学强词" 且 不含"植物强词" → 拒绝（防医学混入）
    - 若期刊名命中黑名单（期刊本身几乎不可能发植物）→ 必须靠内容植物自证，否则拒绝
    - 其余 → 由调用方用 is_plant_content 正向判断（默认放行植物词匹配的）
"""

# ── ① 增强的非植物期刊黑名单（2026-08-25 清理积累，覆盖本次发现的 400+ 污染期刊）──
NONPLANT_JOURNAL_BLACKLIST = [
    # 医学・肿瘤・血液
    'oncol','cancer','carcin','tumor','tumour','carcinoma','leukem','lymphom','sarcoma',
    'melanoma','metastas','oncogene','neoplas','malign',
    # 医学・免疫（人）・炎症
    'immunology','immunotherapy','allerg','inflamm','cell death',
    # 医学・内分泌・代谢・营养（人）
    'endocrinology','diabet','obesity','nutrition','metabolic syndr','thyroid',
    # 医学・心脑血管
    'cardiology','cardiovascular','cardiac','hypertension','circulation','vascular','atheroscl','thrombo',
    # 医学・肝/肾/胃肠/呼吸
    'hepat','gastroenterol','nephrol','renal','kidney','pulmon','respir','intensive care',
    'critical care','emergency','transplant',
    # 医学・神经/精神/心理
    'neurology','neurosci','psychiatry','psycholog','neurodegener','alzheimer','parkinson',
    'autism','addiction','behavioral','cerebrospinal',
    # 医学・生殖/妇儿/老年/皮
    'gynecol','obstetr','pediatr','geriatr','dermat','ophthalm','otorhinolaryng','stomat','dental',
    'urology','orthop','surg','rehabil','physiotherap','podiatr','androl',
    # 医学・药/毒/疫苗/临床
    'pharmacolog','pharmaceu','drug','toxicol','vaccin','clinical','medicine','biomedical',
    'biomedic','molecular medicine','gene therapy','regenerative medicine',
    'public health','epidemiolog','hospital','medical','dentistry',
    # 医学・血液/感染/法医
    'hematolog','blood','infectious disease','virology','forensic',
    'legal medicine','biomarker','liquid biopsy',
    # 兽医/动物/水产
    'veterinary','livestock','aquaculture','fisheries','poultry','zoolog','zool','entomolog (med',
    # 物理/化学/材料/工程/能源/核
    'physics','nuclear','fuel','petroleum','electrical','mechanical engineering','civil engineering',
    'aerospace','automotive','robotic','combustion','semiconductor','chemical engineering',
    'materials science','cataly (eng','electrochem','high energy','applied physics','power',
    # 法学/社科/经济/人文
    'law','legal','sociolog','anthropolog','political','economic','finance','banking','business',
    'marketing','human resource','accounting','criminal','litigation','history','philosophy',
    'geography','urban','transport','education (social','media','linguistic','theology','journalism',
    # 明确杂项/造假期刊
    'preprints','research square','ssrn','cureus','open mind','porn',
]

# ── ② 内容"人类/动物医学强词"（标题+摘要命中即强烈提示非植物）──
HUMAN_ANIMAL_TERMS = [
    'cancer patient','patient survival','clinical trial','clinical outcome','drug delivery',
    'pharmacokinetic','therapeutic target','immune checkpoint','t cell therapy','antibody (human',
    'patient-derived','prostate cancer','breast cancer','lung cancer','colorectal cancer',
    'hepatocellular carcinoma','leukemia','lymphoma','tumor microenviron',
    'serum level','plasma level','blood pressure','renal function','kidney injury',
    'cardiovascular disease','myocardial','neuronal','neurodegener','alzheimer','parkinson',
    'depression','schizophren','autism','psychiatric','maternal','neonatal','fetal','prenatal',
    'obesity (human','diabetes (human','clinical (diagnos','hospital','surgical',
    'human cell line','hela','hek293','ipsc','embryonic stem cell (human','t cell','b cell (human',
    'macrophage (human','mammalian','mouse model (human','rat model (human','zebrafish (nonplant',
    'postpartum','menstrual','menopause','gestational','hematopoietic','bone marrow (human',
    'vaccine (human','immunotherapy (human','stroke (human','ischemic','thrombosis',
    'pyrolysis','gasification','syngas','biochar (energy','liquefaction','torrefaction',
    'power plant','combustion (energy','biofuel (energy','biodiesel (energy','hydrogen production',
    'quantum','particle physics','nuclear reactor','distillation',
    'legislation','constitutional','litigation','separation of powers','economic growth',
    'stock market','marketing strategy','urban planning','real estate','pornography',
]

# ── ③ 植物"研究性"强词（证明是植物生物学研究，而非仅含物种名的工程/医学）──
#     用于黑名单期刊（Fuel/医学/能源等）的放行门槛：光有 rice/soybean 物种名不够，
#     必须证明是生物学机理/组学研究（transcript/meta/climat/photosynthesis 等）。
STUDY_PLANT_TERMS = [
    'transcript','scrna','snrna','atac','single-cell','cell atlas','metabolom','proteom',
    'genome-wide','biosynth','chloroplast','photosynth','flavonoid','anthocyanin','lignin',
    'xylem','phloem','meristem','stomata','trichome','hormone','kinase','transcription factor',
    'abiotic stress','drought','salt stress','osmotic','cold acclimation','heat stress',
    'immune response (plant','pathogen','effector','cell wall (plant','secondary metab',
    'signal transduction','regulatory network','expression profile','somatic embry','crispr',
    'genome editing','breeding','qtl','association study','phenotyp','genome assembly',
    'chlorophyll','photosynth','flowering','vernalization','photoperiod','gravitrop',
]

# ── 植物"物种/组织"宽词（含这些词 → 放行非黑名单期刊；黑名单期刊不考虑）──
SPECIES_PLANT_TERMS = [
    'arabidops','thaliana','oryza','rice','wheat','triticum','maize','sorghum','soybean','glycine',
    'tobacco','nicotiana','tomato','solanum','potato','barley','hordeum','cassava','cucumber',
    'pepper','capsicum','brassica','sunflower','cotton','gossypium','moss','marchantia','fern',
    'grape','vitis','citrus','malus','poplar','eucalyptus','pine','orchid','banana','strawberry',
    'tea (plant','camellia','medicago','lotus','phaseolus','pea','vigna','plant','crop',
    'seedling','leaf','root ','flower','pollen','anther','seed ','floral','inflorescence',
    'grain','chlorophyll','leaf senescence','canopy','rootstock','scion',
]


def _hit(text, terms):
    """text 是否命中任一 term（子串匹配，小写）。"""
    t = (text or '').lower()
    return [k for k in terms if k in t]


def is_relevant_plant_paper(title, abstract, journal):
    """
    综合判定一篇论文是否应进入植物知识库。
    返回 (ok: bool, reason: str)
    """
    title = title or ''
    abstract = abstract or ''
    journal = journal or ''
    jl = journal.lower()
    text = (title + ' ' + abstract).lower()

    # ── A. 期刊黑名单 / 期刊含植物词 ──
    journal_hit = _hit(jl, NONPLANT_JOURNAL_BLACKLIST)
    jrn_has_plant_word = any(k in jl for k in
        ['plant','botan','phyt','crop','agron','hortic','forest','agri','breeding','genome','genetic'])
    blacklisted = bool(journal_hit) and not jrn_has_plant_word

    # ── 内容信号 ──
    human_hit  = _hit(text, HUMAN_ANIMAL_TERMS)
    study_hit  = _hit(text, STUDY_PLANT_TERMS)   # 生物学研究强词
    species_hit= _hit(text, SPECIES_PLANT_TERMS) # 物种/组织宽词

    # 1) 强人类医学（无植物研究自证）→ 拒绝
    if human_hit and not study_hit and not species_hit:
        return False, f'human/medical: {human_hit[0]}'

    # 2) 黑名单期刊（Fuel/医学/能源/物理等）：
    #    必须有植物"研究性"强词才放行（rice 物种名不足以证明是植物研究，可能是气化/能源）
    if blacklisted:
        if study_hit and not human_hit:
            return True, f'jrn-blacklist+plant-study:{journal_hit[0]}'
        return False, f'journal-blacklist: {journal_hit[0] if journal_hit else "?"}'

    # 3) 非黑名单期刊 → 有物种宽词即放行；无则交给调用方 is_plant 判定
    if species_hit and not human_hit:
        return True, 'plant-species'
    return True, 'ok'


if __name__ == '__main__':
    tests = [
        ('Cancer patient survival in metastatic breast carcinoma', '', 'Journal of Clinical Oncology'),
        ('Flavonoid biosynthesis in Arabidopsis under drought', '', 'Horticulture Research'),
        ('Enhanced syngas from rice husk gasification for power plant', '', 'Fuel'),
        ('Single-cell transcriptome atlas of rice roots', '', 'Frontiers in Plant Science'),
        ('Neuronal activity and depression in maternal rats', '', 'Frontiers in Psychology'),
        ('Chloroplast genome of soybean chloroplast', '', 'Genomics'),
    ]
    for t, a, j in tests:
        ok, why = is_relevant_plant_paper(t, a, j)
        print(f"{'OK ' if ok else 'NO '} [{why}] {t[:55]}")
