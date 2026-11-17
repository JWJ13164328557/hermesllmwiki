#!/usr/bin/env python3
"""P4a: 跨论文 Synthesis 生成 — 自动主题发现 + 从 Evidence Objects 提炼共识/争议/空白"""
import io, os, re, json, math, sys
from collections import Counter, defaultdict
from datetime import date
from itertools import combinations

from kb_paths import BASE, REPO_ROOT  # 统一根目录解析: KB_BASE/APP_DIR 环境变量优先
import themes as th  # 主题↔标签的唯一契约（2026-11-02）
from organism_scope import (evidence_verdict, evidence_in_theme,
                            paper_scope_table)
PAPERS_DIR = os.path.join(BASE, 'concepts', 'papers')
EVIDENCE_DIR = os.path.join(BASE, 'evidence')
SYNTHESIS_DIR = os.path.join(BASE, 'synthesis')
os.makedirs(SYNTHESIS_DIR, exist_ok=True)

# 单一时钟：页面上的 updated / 生成日期一律取运行日，禁止硬编码
TODAY = date.today().isoformat()

# ============================================================
# Soybean relevance keywords for scoring
# ============================================================
SOYBEAN_KEYWORDS = [
    'soybean', 'glycine', 'legume', 'internode', 'cambium', 'vascular',
    'light quality', 'shade', 'phytochrome', 'photomorphogen',
    'stem', 'wood', 'xylem', 'phloem', 'secondary growth',
    'auxin', 'gibberellin', 'brassinosteroid', 'cell wall',
]

# ============================================================
# Phase 1: Load all evidence with tags
# ============================================================
def _non_evidence_sources():
    """返回 article_kind 为更正/撤稿/社论/会员表等的论文页 slug 集合。

    2026-11-03：分层标签此前只有 batch_evidence_objects 与 batch_hypotheses
    在消费，synthesis 完全没读 —— 于是"会员表"页面里的错配提炼照常进入
    主题统计与综述页。证据页本身不带 article_kind，必须回到来源页判定。
    """
    import article_kind
    bad = set()
    for d in (os.path.join(BASE, 'concepts', 'papers'), os.path.join(BASE, 'concepts')):
        if not os.path.isdir(d):
            continue
        for fn in os.listdir(d):
            if not fn.endswith('.md'):
                continue
            try:
                head = io.open(os.path.join(d, fn), encoding='utf-8', errors='ignore').read(2000)
            except OSError:
                continue
            m = re.search(r'^article_kind:\s*"?([a-z\-]+)', head, re.M)
            kind = m.group(1) if m else 'research'
            if not article_kind.is_evidence_eligible(kind):
                bad.add(fn[:-3])
    return bad


def load_all_evidence():
    """Load evidence objects, extract tags and claims"""
    all_evidence = []
    _bad_src = _non_evidence_sources()
    for f in sorted(os.listdir(EVIDENCE_DIR)):
        if not f.endswith('.md'): continue
        fpath = os.path.join(EVIDENCE_DIR, f)
        with open(fpath, 'r', encoding='utf-8', errors='replace') as fh:
            content = fh.read()
        
        # Extract claim
        claim_m = re.search(r'(?:^claim:\s*"?(.+?)"?\n|## Claim\n(.+?)(?=\n##|\Z))', content, re.DOTALL)
        claim = ''
        if claim_m:
            claim = (claim_m.group(1) or claim_m.group(2) or '').strip()[:500]
        
        _ttl_m = re.search(r'^title:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
        _title = _ttl_m.group(1).strip().strip('"') if _ttl_m else ''
        # 与 batch_hypotheses.load_evidence 保持一致：主题归属必须用同一段文本。
        # 上面提取的 claim 是 front-matter 里的一句话版，
        # 而正文 ## Claim 段落通常更长、关键词更多，
        # 两边用不同文本去 assign_themes 会让同一主题数出
        # 不同的证据数（实测 metabolism 348 vs 343）。
        _body_claim = ''
        _bm = re.search(r'^##\s*Claim\s*\n(.+?)(?=\n##|\Z)', content, re.S | re.M)
        if _bm:
            _body_claim = _bm.group(1)
        # 必须用与 batch_hypotheses 完全相同的清洗函数：PDF 抽取的
        # "deacety\xad lation" / "enhanc\xad ers" 若只做空白合并，会变成
        # "deacety lation"，关键词 "deacetylation" 命中不了。
        _theme_text = (_title + ' ' + th.normalize_claim(_body_claim or claim))
        all_evidence_theme_text = _theme_text

        # Extract tags (inline format: tags: [a, b, c])
        tags = []
        tag_m = re.search(r'^tags:\s*\[(.+?)\]', content, re.MULTILINE)
        if tag_m:
            tags = [t.strip().strip('"').strip("'") for t in tag_m.group(1).split(',')]
        
        # For older format without tags, derive from claim_type + species + tissue
        if not tags:
            # Derive tags from structured fields
            claim_type_m = re.search(r'^claim_type:\s*(.+)', content, re.MULTILINE)
            species_m = []
            tissue_m = []
            sp_match = re.search(r'^species:\s*\n((?:\s{2}-.+\n?)+)', content, re.MULTILINE)
            if sp_match:
                species_m = re.findall(r'^\s{2}-\s*(.+)', sp_match.group(1))
            ti_match = re.search(r'^tissue:\s*\n((?:\s{2}-.+\n?)+)', content, re.MULTILINE)
            if ti_match:
                tissue_m = re.findall(r'^\s{2}-\s*(.+)', ti_match.group(1))
            
            if claim_type_m:
                ct = claim_type_m.group(1).strip()
                ct_map = {
                    'methodological': 'method', 'method': 'method',
                    'observation': 'observation',
                    'functional': 'functional',
                }
                tags.append(ct_map.get(ct, ct))
            tags.extend(species_m[:3])
            tags.extend(tissue_m[:2])
        
        # 2026-11-02 删除"按 claim 关键词硬塞主题标签"的富化块。
        # 它会给任意含 auxin/drought/development 字样的证据追加
        # hormone-signaling/stress/development 标签，绕过了 themes.py 的
        # 别名表与 MAX_THEMES_PER_EVIDENCE 约束，导致同一主题在
        # batch_synthesis 里数出 848 条、在 batch_hypotheses 里只有 272 条。
        # 现在主题归属唯一来源是 themes.assign_themes()。

        # Extract metadata
        pmid_m = re.search(r'pmid:\s*"?(\d+)"?', content)
        doi_m = re.search(r'doi:\s*"?([^\s"]+)"?', content)
        source_m = re.search(r'source:\s*"?(.+?)"?\n', content)
        quality_m = re.search(r'quality:\s*(\w+)', content)
        _et_m = re.search(r'^evidence_type:\s*"?([^"\n]+)"?', content, re.M)
        _conf_m = re.search(r'^evidence_type_confidence:\s*"?([a-z]+)"?', content, re.M)

        # 与 batch_hypotheses.load_evidence 同源解析：领域判定的证据级兜底
        # 要用 primary_species / species。缺这两个字段时，同一批非植物词证据
        # 在综述层被判 nonplant、在假说层被判 plant（species 自证），
        # 于是出现"hyp 比 syn 多 1 条"这类只有一行之差的不一致。
        _ps_m = re.search(r'^primary_species:\s*"?(.*?)"?\s*$', content, re.M)
        _sp_m = re.search(r'^species:\s*\[(.*?)\]', content, re.M)
        _species = ([x.strip().strip('"\'') for x in _sp_m.group(1).split(',') if x.strip()]
                    if _sp_m else [])
        
        # 与 batch_hypotheses.load_evidence 的证据池卫生门一致：
        # 没有 DOI 的页面不是"某篇论文的一条证据"，
        # 不能进入主题统计。否则两个脚本的证据数永远差一条。
        if not (doi_m.group(1) if doi_m else ''):
            continue

        # 论断角色闸门（rule-v4，2026-11-03）：背景铺垫与方法描述不是证据。
        # 它们进综述只会产出"多篇核心文献表明"这类空话，故在装载层统一剔除，
        # 而不是让每个综述脚本各写一份过滤条件。
        _role_m = re.search(r'^claim_role:\s*"?(\w+)"?', content, re.M)
        _role = _role_m.group(1) if _role_m else 'finding'
        if _role in ('method', 'background'):
            continue

        # 来源页是非研究类型（更正/撤稿/社论/会员表）→ 不进主题统计
        _src_slug = ''
        _sm2 = re.search(r'source:\s*"?\[\[([^\]]+)\]\]', content)
        if _sm2:
            _src_slug = _sm2.group(1).strip()
        if _src_slug in _bad_src:
            continue

        # 主题归属优先级（2026-11-03 第 14 轮）：frontmatter 的 themes:
        # 是权威来源（由源论文继承 + claim 守卫），assign_themes 只做历史页兜底。
        # 只走 tags/关键词会让 12291 条证据里 87% 判成"无主题"，
        # 而它们的源论文大多已有主题——这是"证据有、主题无"的假象来源。
        _decl_m = re.search(r'^themes:\s*\[(.*?)\]', content, re.M)
        _declared = ([x.strip().strip('"\'') for x in _decl_m.group(1).split(',') if x.strip()]
                     if _decl_m else [])
        _decl_set = None
        if _decl_m is not None:
            # 字段存在即权威：即使为空数组（claim 守卫拦下）也不回退关键词，
            # 否则守卫拦掉的污染会从兜底路径重新长回来。
            _decl_set = set()
            for _t in th.normalize_tags(_declared):
                _tid = th.THEME_TAG_ALIASES.get(_t)
                if _tid:
                    _decl_set.add(_tid)

        all_evidence.append({
            'id': f.replace('.md', ''),
            'claim': claim,
            'title': _title,
            '_theme_text': _theme_text,
            'themes': _decl_set,
            'theme_basis': 'declared' if _decl_set is not None else None,
            'tags': tags,
            'pmid': pmid_m.group(1) if pmid_m else '',
            'doi': doi_m.group(1) if doi_m else '',
            'source': source_m.group(1) if source_m else '',
            'quality': quality_m.group(1) if quality_m else 'medium',
            'evidence_type': _et_m.group(1).strip() if _et_m else '',
            'evidence_type_confidence': _conf_m.group(1).strip() if _conf_m else '',
            'claim_role': _role,
            'primary_species': _ps_m.group(1).strip() if _ps_m else '',
            'species': _species,
            'full_content': content,
        })
    
    return all_evidence

# ============================================================
# Phase 2: Tag co-occurrence graph + community detection
# ============================================================
def build_tag_graph(all_evidence):
    """Build tag co-occurrence graph from evidence objects"""
    tag_cooccur = defaultdict(Counter)
    tag_freq = Counter()
    
    for ev in all_evidence:
        tags = ev['tags']
        for t in tags:
            tag_freq[t] += 1
        # Co-occurrence
        for t1, t2 in combinations(sorted(set(tags)), 2):
            tag_cooccur[t1][t2] += 1
            tag_cooccur[t2][t1] += 1
    
    return tag_cooccur, tag_freq

def community_detection(tag_cooccur, tag_freq, min_tag_freq=3):
    """Connected-component clustering on tag co-occurrence graph with Jaccard threshold"""
    # Filter rare and stop tags
    STOP_TAGS = {'paper', 'pmc'}
    active_tags = {t for t in tag_freq if tag_freq[t] >= min_tag_freq and t not in STOP_TAGS}
    
    # Build adjacency: edge exists if Jaccard >= threshold
    threshold = 0.08
    edges = set()
    for t1 in active_tags:
        for t2, co in tag_cooccur[t1].items():
            if t2 not in active_tags or t2 <= t1:
                continue
            jaccard = co / (tag_freq[t1] + tag_freq[t2] - co)
            if jaccard >= threshold:
                edges.add((t1, t2))
    
    # Connected components (union-find)
    parent = {t: t for t in active_tags}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    
    for t1, t2 in edges:
        union(t1, t2)
    
    # Collect communities
    communities_map = defaultdict(set)
    for t in active_tags:
        communities_map[find(t)].add(t)
    
    communities = sorted(communities_map.values(), key=lambda c: -sum(tag_freq[t] for t in c))
    
    # Filter: keep only communities with meaningful biological tags (≥3 non-generic)
    meaningful = []
    for comm in communities:
        if len(comm) >= 2:
            meaningful.append(comm)
    
    # Add significant orphan tags as singleton communities
    # (tags that are biologically specific but don't co-occur strongly enough)
    clustered_tags = set().union(*meaningful) if meaningful else set()
    orphans = [t for t in active_tags if t not in clustered_tags 
               and tag_freq[t] >= 30
               and t not in ('observation', 'functional', 'method', 'development',
                             'arabidopsis', 'arabidopsis thaliana')]
    for t in orphans:
        meaningful.append({t})
    
    return meaningful

def name_community(community, tag_freq, all_evidence):
    """Generate a human-readable name for a tag community"""
    # Skip generic hub tags for naming
    GENERIC_NAMING = {'metabolism', 'transcriptomics', 'metabolomics', 'genomics', 
                      'arabidopsis', 'secondary-metabolism', 'multi-omics'}
    specific = [t for t in community if t not in GENERIC_NAMING]
    if not specific:
        specific = sorted(community, key=lambda t: -tag_freq[t])[:3]
    
    top_tags = sorted(specific, key=lambda t: -tag_freq[t])[:5]
    
    # Count evidence objects in this community
    n_evidence = sum(1 for ev in all_evidence 
                     if any(t in community for t in ev['tags']))
    
    emoji_map = {
        'root': '🌱', 'development': '🌱',
        'flavonoid': '🍇', 'anthocyanin': '🍇', 'phenylpropanoid': '🌸',
        'terpenoid': '🌿', 'alkaloid': '💊', 'lipid': '🧈',
        'starch-sugar': '🍬',
        'stress': '⚡', 'immunity': '🛡️', 'defense': '🛡️',
        'hormone': '🧪', 'signaling': '🧪',
        'single-cell': '🔬', 'spatial': '🗺️', 'spatial-transcriptomics': '🗺️',
        'regeneration': '🔄', 'epigenetic': '🧬',
        'leaf': '🍃', 'shoot': '🌿', 'rice': '🌾', 'maize': '🌽',
        'method': '💻', 'protocol': '📋',
    }
    emoji = next((emoji_map.get(t, '📄') for t in top_tags), '📄')
    
    main_topics = top_tags[:3]
    title = ' & '.join(t.title() for t in main_topics)
    slug = '-'.join(re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-') for t in main_topics[:2])
    
    # Add all tags as a richer description
    all_tags_sorted = sorted(community, key=lambda t: -tag_freq[t])
    
    return {
        'slug': slug or 'untitled',
        'title': title,
        'emoji': emoji,
        'tags': all_tags_sorted[:8],  # Keep top 8 for evidence matching
        'n_evidence': n_evidence,
        'description': f'自动发现主题 — 核心: {", ".join(main_topics)} | 全部标签: {", ".join(all_tags_sorted)}',
    }

def score_soybean_relevance(community, all_evidence):
    """Score how relevant this topic is to soybean internode light quality project"""
    community_evidence = [ev for ev in all_evidence 
                          if any(t in community for t in ev['tags'])]
    
    score = 0
    for ev in community_evidence:
        text = (ev['claim'] + ' ' + ' '.join(ev['tags'])).lower()
        for kw in SOYBEAN_KEYWORDS:
            if kw in text:
                score += 1
    
    n = max(len(community_evidence), 1)
    density = score / n
    
    if density > 2.0:
        return '高 — 直接关联大豆节间光质响应'
    elif density > 1.0:
        return '中 — 部分方法/机制可借鉴'
    elif density > 0.3:
        return '低 — 可提供背景知识'
    else:
        return '低 — 间接关联'

def auto_discover_clusters(all_evidence):
    """Main auto-discovery: tag graph → communities → named clusters"""
    tag_cooccur, tag_freq = build_tag_graph(all_evidence)
    communities = community_detection(tag_cooccur, tag_freq, min_tag_freq=2)
    
    print(f"  Tags total: {len(tag_freq)}")
    print(f"  Communities detected: {len(communities)}")
    
    clusters = {}
    for i, comm in enumerate(communities):
        info = name_community(comm, tag_freq, all_evidence)
        info['relevance_to_soybean'] = score_soybean_relevance(comm, all_evidence)
        clusters[info['slug']] = info
        print(f"    [{i+1}] {info['title']} ({info['n_evidence']} evidence, {len(comm)} tags) — {info['relevance_to_soybean']}")
    
    return clusters

# ============================================================
# Phase 3: Classify evidence into auto-discovered clusters
# ============================================================
_PAPER_SCOPE = None


def _paper_scope():
    global _PAPER_SCOPE
    if _PAPER_SCOPE is None:
        _PAPER_SCOPE = paper_scope_table(PAPERS_DIR)
    return _PAPER_SCOPE


def classify_evidence(evidence_list, theme_id):
    """按 themes.py 的唯一定义归属证据（2026-11-02 重写）。

    旧实现用 "与主题标签集重合 >=2 个" 判定，而主题标签集是各脚本自带的
    一份手写列表，与证据页真实标签并不对齐（例如 synthesis 页写
    tags:[hormone, signaling, synthesis]，证据页写 hormone-signaling），
    导致同一主题在不同脚本里数出 197 / 108 / 9 三个数字。
    现在标签归一化 + 别名表 + 关键词兜底全部收敛到 themes.py。
    """
    matched = []
    for ev in evidence_list:
        # 领域纯度：唯一判定来自 organism_scope.evidence_in_theme
        # （2026-11-03）。三个消费方（综述/假说/正文重建）一律调用它，
        # 不再各自维护一份规则——之前 methods-tools 实测同时存在
        # 80 / 81 / 84 三个数，全部源于边界情形分歧。'非植物但方法可迁移’
        # 的论文只能进 methods-tools；勘误/撤稿页任何主题都不收。
        ok, verdict, _why = evidence_in_theme(ev, theme_id, _paper_scope())
        if not ok:
            continue
        tset = ev.get('themes')
        if tset is None:
            # 与 batch_hypotheses.load_evidence 使用完全相同的文本，
            # 否则"标题里带主题关键词"的证据只在一边被计入，同一主题
            # 会在两份报告里给出不同的证据数（实测 metabolism 348 vs 343）。
            tset, basis = th.assign_themes(
                ev.get('tags') or [],
                ev.get('_theme_text') or ((ev.get('title') or '') + ' ' + (ev.get('claim') or '')))
            ev['themes'] = tset
            ev['theme_basis'] = basis
        tset = th.filter_supported_themes(tset, ev.get('_theme_text') or '')
        if theme_id in tset:
            matched.append(ev)
    return matched

# ============================================================
# Phase 4: Find consensus from evidence cluster
# ============================================================
def find_consensus(evidence_cluster):
    """Group similar claims and identify consensus patterns"""
    phrase_counter = Counter()
    claim_groups = defaultdict(list)
    
    for ev in evidence_cluster:
        claim = ev['claim']
        phrases = re.findall(r'([A-Z][a-z]+ [a-z]+ (?:development|differentiation|signaling|regulation|expression|formation|biosynthesis))', claim)
        for p in phrases:
            phrase_counter[p] += 1
            claim_groups[p].append(ev)
    
    consensus = []
    for phrase, count in phrase_counter.most_common(20):
        if count >= 2:
            supporting_ev = claim_groups[phrase][:5]
            unique_sources = len(set(e['pmid'] or e['doi'] for e in supporting_ev if e['pmid'] or e['doi']))
            if unique_sources >= 2:
                consensus.append({
                    'pattern': phrase,
                    'paper_count': unique_sources,
                    'evidence_count': count,
                    'sample_claims': [e['claim'][:200] for e in supporting_ev[:3]],
                    'sample_sources': [e['source'][:60] for e in supporting_ev[:3]],
                })
    
    return consensus[:10]

def find_contradictions(evidence_cluster):
    """Find potentially contradictory claims"""
    contradictions = []
    opposing_pairs = [
        (r'\bactivates?\b', r'\binhibits?\b|represses?'),
        (r'\bpromotes?\b', r'\bsuppresses?\b'),
        (r'\bupregulat', r'\bdownregulat'),
        (r'\bincreases?\b', r'\bdecreases?\b'),
    ]
    
    claims_by_gene = defaultdict(list)
    for ev in evidence_cluster:
        genes = set(re.findall(r'\b([A-Z]{2,5}\d{1,2}[A-Z]?)\b', ev['claim']))
        for g in genes:
            claims_by_gene[g].append(ev)
    
    for gene, claims in claims_by_gene.items():
        if len(claims) < 2: continue
        for pair in opposing_pairs[:2]:
            has_pos = any(re.search(pair[0], c['claim'], re.I) for c in claims)
            has_neg = any(re.search(pair[1], c['claim'], re.I) for c in claims)
            if has_pos and has_neg:
                contradictions.append({
                    'gene': gene,
                    'type': 'regulation direction dispute',
                    'sources': [c['source'][:60] for c in claims[:3]],
                })
                break
    
    return contradictions[:5]

# ============================================================
# Phase 5: Generate Synthesis Page
# ============================================================
AUTO_START = '<!-- AUTO-EVIDENCE-STRENGTH:START -->'
AUTO_END = '<!-- AUTO-EVIDENCE-STRENGTH:END -->'


def _species_of(ev):
    sp = ev.get('species') or []
    if isinstance(sp, str):
        sp = [sp]
    return [s for s in sp if s]


def evidence_strength_section(cluster_evidence):
    """生成"证据覆盖与强度"段落：全部数字来自同一次统计，可复算。

    存在的意义：综述正文是人工撰写的，读者无法判断"这句话有多少证据托底"。
    这一段把可量化的覆盖度（物种/证据类型/顶刊集中度/证据 ID）摆在正文前面，
    让"哪里证据薄"一眼可见，而不是靠读者相信作者。
    """
    from collections import Counter
    n_ev = len(cluster_evidence)
    keys = {paper_key(e) for e in cluster_evidence if paper_key(e)}
    n_papers = len(keys)

    species = Counter()
    etypes = Counter()
    journals = Counter()
    for e in cluster_evidence:
        for s in _species_of(e):
            species[s] += 1
        t = (e.get('evidence_type') or '').strip() or '未标注'
        etypes[t] += 1
        src = (e.get('source') or '').strip()
        if src:
            journals[src] += 1

    per_page = n_ev / float(n_papers) if n_papers else 0.0
    single_paper_share = 0.0
    if n_ev:
        by_paper = Counter(paper_key(e) for e in cluster_evidence if paper_key(e))
        single_paper_share = sum(1 for v in by_paper.values() if v == 1) / float(len(by_paper) or 1)

    sp_lines = '、'.join('%s(%d)' % (k, v) for k, v in species.most_common(6)) or '未标注'
    et_lines = '；'.join('%s %d' % (k, v) for k, v in etypes.most_common(6)) or '未标注'

    lines = [
        AUTO_START,
        '',
        '## 证据覆盖与强度（自动统计，可复算）',
        '',
        '| 指标 | 值 | 读法 |',
        '|---|---|---|',
        '| 证据条目 | %d | 本主题归属的证据对象数 |' % n_ev,
        '| 独立论文 | %d | 去重后的 PMID/DOI 数 |' % n_papers,
        '| 平均每篇证据数 | %.2f | <1.0 说明多数论文只贡献 1 条结论 |' % per_page,
        '| 单条证据论文占比 | %.0f%% | 越高说明"每篇论文一个结论"，系统性弱 |' % (single_paper_share * 100),
        '| 主要物种 | %s | 物种过度集中则外推性受限 |' % sp_lines,
        '| 证据类型 | %s | 表达/关联类居多时，因果结论需打折扣 |' % et_lines,
        '',
        '> 归属依据：`themes.py` 标签别名表（高置信）+ 关键词兜底（低置信）。'
        '本段由脚本生成，不构成结论；结论性文字须回原文核对。',
        '',
    ]

    def _bad_claim(text):
        t = ' '.join((text or '').split())
        if len(t) < 60:
            return True
        if len(re.findall(r'[A-Za-z\u4e00-\u9fff]', t)) < 0.6 * len(t):
            return True
        return bool(re.search(
            r'(©|all rights reserved|copyright|https?://|doi\.org|^\d{3,4}\s*,|'
            r'^(figure|table|fig\.)\s*\d|^\(?keywords?[:：]|\.{4,}|downloaded from|license)',
            t, re.I))

    causal_rank = {'genetic perturbation': 0, 'protein interaction': 1,
                   'DNA binding/regulation': 2}
    top = sorted([e for e in cluster_evidence if not _bad_claim(e.get('claim'))],
                 key=lambda e: (causal_rank.get((e.get('evidence_type') or ''), 3),
                                -len(e.get('claim') or '')))[:12]
    if top:
        lines += ['### 可复核证据索引（前 12 条，按断言长度）', '',
                  '| 证据 ID | DOI | 断言（截断） |', '|---|---|---|']
        for e in top:
            claim = ' '.join((e.get('claim') or '').split())[:90]
            doi = e.get('doi') or ''
            lines.append('| `%s` | %s | %s |' % (e['id'], doi, claim.replace('|', '/')))
        lines.append('')
    # 证据语义分层：把“能支持什么强度的推断”直接写进页面，避免把
    # omics/co-occurrence 与 genetic perturbation 当成同权证据。
    type_order = [
        ('genetic perturbation', '遗传因果（扰动后表型/表达改变）'),
        ('protein interaction', '物理互作（Co-IP/Y2H/BiFC/pull-down）'),
        ('DNA binding/regulation', '直接调控（ChIP/EMSA/启动子报告）'),
        ('expression/regulation', '表达相关（转录组/qPCR，不能单独推因果）'),
        ('phenotypic/association', '表型关联（GWAS/QTL/自然变异/田间）'),
        ('omics/co-occurrence', '组学共现（单细胞簇/共表达网络，非调控）'),
        ('descriptive/observational', '描述性/背景陈述（未报告可核验的实验设计）'),
    ]
    lines += ['### 证据语义分层', '',
              '| 证据类型 | 条目数 | 可支持的推断强度 |',
              '|---|---:|---|']
    for key, meaning in type_order:
        if etypes.get(key):
            lines.append('| %s | %d | %s |' % (key, etypes[key], meaning))
    missing_type = etypes.get('未标注', 0)
    if missing_type:
        lines.append('| 未标注 | %d | 不得用于机制推断，需回原文补标 |' % missing_type)
    lines += ['',
              '> 读法：`genetic perturbation` / `protein interaction` / `DNA binding/regulation` '
              '可支持因果或直接调控；`expression/regulation` 与 `omics/co-occurrence` '
              '只能提出假说，不能单独证明调控或因果。', '']

    strong = [e for e in cluster_evidence
              if (e.get('evidence_type') or '') == 'genetic perturbation'
              and (e.get('evidence_type_confidence') or 'high') == 'high'
              and not _bad_claim(e.get('claim'))]
    if strong:
        lines += ['### 遗传扰动类证据（仅高置信规则命中，前 5 条；仍须回原文核实）', '',
                  '| 证据 ID | DOI | 断言（截断） |', '|---|---|---|']
        for e in sorted(strong, key=lambda x: -len(x.get('claim') or ''))[:5]:
            claim = ' '.join((e.get('claim') or '').split())[:100]
            lines.append('| `%s` | %s | %s |' % (
                e['id'], e.get('doi') or '', claim.replace('|', '/')))
        lines.append('')

    lines += ['### 正文状态', '',
              '> frontmatter 标记 `body_status: rebuilt-*` 的页面，其子主题正文由 '
              '`rebuild_synthesis_body.py` 按本页证据确定性重建；本自动段是该快照的'
              '统计摘要。未标记的页面保留历史正文，机制性表述须逐条回原文核对，'
              '不得仅凭本页引用。', '']
    lines.append(AUTO_END)
    return '\n'.join(lines)


def refresh_auto_sections(content, cluster_evidence):
    """在成对标记之间整体替换自动段；首次运行时插到正文第一个 H2 之前。"""
    block = evidence_strength_section(cluster_evidence)
    if AUTO_START in content and AUTO_END in content:
        pre, rest = content.split(AUTO_START, 1)
        _, post = rest.split(AUTO_END, 1)
        return pre + block + post
    m = re.search(r'^## ', content, re.M)
    if not m:
        return content.rstrip() + '\n\n' + block + '\n'
    return content[:m.start()] + block + '\n\n' + content[m.start():]


def write_if_changed(path, content):
    """内容一致就不落盘：返回 True 表示确实写入。与 batch_evidence_objects 同一约定。"""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            if f.read() == content:
                return False
    except OSError:
        pass
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
    return True


def paper_key(ev):
    """Stable identity of the source paper (PMID preferred, DOI as fallback)."""
    return ev.get('pmid') or ev.get('doi') or ''


def compute_stats(cluster_evidence, consensus, contradictions):
    """SINGLE SOURCE OF TRUTH for every count printed on a synthesis page.

    Both the full-generation path and the --update path must call this, so the
    frontmatter, the 统计 block and the References footer can never drift apart.
    """
    return {
        'total_papers': len({paper_key(e) for e in cluster_evidence if paper_key(e)}),
        'total_evidence': len(cluster_evidence),
        'consensus_findings': len(consensus),
        'contradictions': len(contradictions),
    }


def top_papers_md(cluster_evidence, n=10):
    """Markdown list of the papers carrying the most evidence objects."""
    by_paper = {}
    for e in cluster_evidence:
        key = paper_key(e)
        if not key:
            continue
        rec = by_paper.setdefault(key, {'n': 0, 'claim': '', 'doi': e.get('doi', ''), 'pmid': e.get('pmid', '')})
        rec['n'] += 1
        claim = ' '.join((e.get('claim') or '').split())
        if len(claim) > len(rec['claim']):
            rec['claim'] = claim
    ranked = sorted(by_paper.items(), key=lambda kv: (-kv[1]['n'], kv[0]))[:n]
    if not ranked:
        return '> 本主题暂无可识别的论文标识（PMID/DOI），无法排序。'
    lines = []
    for i, (key, rec) in enumerate(ranked, 1):
        ident = f'DOI:{rec["doi"]}' if rec['doi'] else f'PMID:{rec["pmid"]}'
        claim = rec['claim'][:120] + ('…' if len(rec['claim']) > 120 else '')
        lines.append(f'{i}. **{ident}** — 支撑 {rec["n"]} 条证据 · {claim}')
    return '\n'.join(lines)


def fix_literal_newlines(content):
    """把误写进正文的字面量反斜杠n还原成真换行。

    2026-11-02：4 个 synthesis 页出现 "\n> ..." "\n- ..." 这样的转义错误
    （字符串拼接时 escaped newline 被当成普通字符写盘）。只处理后面紧跟
    Markdown 结构符的情形，避免误伤正文里合法出现的说明文字。
    """
    out = re.sub(r'\\n(?=[>\-*#| ])', '\n', content)
    out = re.sub(r'\\n(?=\n)', '\n', out)
    # PDF/历史拼接残留：连续中文句号、无引用的“多篇核心文献”占位
    out = re.sub(r'。{2,}', '。', out)
    out = re.sub(r'^多篇核心文献\s*$',
                 '> 以下为历史条目，未附行内引用；引用前须回原文核对。',
                 out, flags=re.M)
    # 历史正文里的非植物条目：保留位置并明确标记，不静默改写事实。
    out = re.sub(r'^.*(?:Ursus maritimus|polar bear|北极熊).*$',
                 '> [已移除历史条目：非植物研究对象，待按植物证据重写]',
                 out, flags=re.M | re.I)
    return out


def rewrite_scope_counts(content, ev_count, paper_count, today):
    """把"综合自 N 条证据，覆盖 M 篇文献（…更新）。"改写为与 stats 一致的表述。

    2026-11-02：--update 只刷新 frontmatter，正文这句老话一直是旧数字
    （genomics-evolution 正文 334/50 vs frontmatter 71/14），导致一致性检查 8/8 报错。
    这里不"把数字改小冒充重写"，而是明确标注增量更新的口径。
    """
    new = ('本页当前登记 %d 条证据对象、%d 篇文献（统计于 %s；'
           '子主题正文为历史人工/LLM 文本，未由本次证据重建）。'
           % (ev_count, paper_count, today))
    # 2026-11-02: 线上真实写法不止一种，原正则只认
    #   "综合自 N 条证据，覆盖 M 篇文献（…）。"
    # 漏掉了下面两类，导致 --update 后正文与 frontmatter 长期打架：
    #   "综合自 370 条证据对象，覆盖 47 篇论文（截至 2026-09-17）。"
    #   "基于 309 条证据对象，覆盖 108 篇文献（2026-06-01 导入），涵盖…"
    pats = [
        # 2026-11-02（第 24 轮）：优先匹配本函数自己写出的格式，否则二次运行
        # 永远刷不到它 —— 实测 hormone-signaling 正文冻结在 197/82，
        # 而 frontmatter 已是 141/52。幂等性是刷新逻辑的底线。
        re.compile(r'本页当前登记\s*\d+\s*条证据对象、?\s*\d+\s*篇文献'
                   r'（[^）]{0,80}）'),
        re.compile(r'综合自\s*\d+\s*条证据(?:对象)?\s*[，,]?\s*覆盖\s*\d+\s*篇(?:文献|论文)'
                   r'（[^）]{0,60}）。'),
        re.compile(r'综合自\s*\d+\s*条证据(?:对象)?\s*[，,]?\s*覆盖\s*\d+\s*篇(?:文献|论文)。'),
        re.compile(r'基于\s*\d+\s*条证据(?:对象)?\s*[，,]\s*覆盖\s*\d+\s*篇(?:文献|论文)'
                   r'（[^）]{0,60}）\s*[，,]?'),
    ]
    for pat in pats:
        if pat.search(content):
            return pat.sub(new, content, count=1)
    return content


def page_consistency_issues(content):
    """Return human-readable list of internal number/artefact inconsistencies."""
    issues = []
    fm_ev = re.search(r'^total_evidence:\s*(\d+)', content, re.M)
    fm_pa = re.search(r'^total_papers:\s*(\d+)', content, re.M)
    if not fm_ev:
        issues.append('frontmatter 缺少 total_evidence')
    if not fm_pa:
        issues.append('frontmatter 缺少 total_papers')
    body_ev = (
        re.findall(r'证据条目[:：]\s*(\d+)', content)
        + re.findall(r'本文档基于\s*(\d+)\s*条证据对象', content)
        + re.findall(r'综合自\s*(\d+)\s*条证据', content)
        + re.findall(r'(\d+)\s*条证据[，,]\s*覆盖', content)
        # 「本页当前登记 N 条证据对象、M 篇文献」是 rewrite_scope_counts 的产物，
        # 不纳入检查等于放行 —— 实测 8/8 页正文与 frontmatter 打架却报 OK。
        + re.findall(r'本页当前登记\s*(\d+)\s*条证据对象', content)
    )
    body_pa = (
        re.findall(r'涵盖论文[:：]\s*~?(\d+)', content)
        + re.findall(r'覆盖\s*(\d+)\s*篇文献', content)
        + re.findall(r'本页当前登记\s*\d+\s*条证据对象、?\s*(\d+)\s*篇文献', content)
    )
    tail_ev = []
    if fm_ev:
        for v in body_ev + tail_ev:
            if v != fm_ev.group(1):
                issues.append(f'正文证据条数 {v} ≠ frontmatter {fm_ev.group(1)}')
    if fm_pa:
        for v in body_pa:
            if v != fm_pa.group(1):
                issues.append(f'正文论文数 {v} ≠ frontmatter {fm_pa.group(1)}')
    if '待补充' in content:
        issues.append('残留占位符 <!-- 待补充 -->')
    ph = re.findall(r'(?<!\[)\[(?:[a-z][a-z /\-]{2,30})\](?!\])', content)
    if ph:
        issues.append('残留方括号占位符: %s' % ', '.join(sorted(set(ph))[:5]))
    if '\\n>' in content or '\\n-' in content:
        issues.append('正文出现字面量 \\n（转义错误）')
    if len(re.findall(r'^title:', content, re.M)) > 1:
        issues.append('疑似多个 frontmatter 块被拼接（多个 title:）')
    if len(re.findall(r'^# ', content, re.M)) > 1:
        issues.append('疑似多个页面被拼接（多个 H1）')
    # 2026-11-04：一页里有两个"证据类型"统计块 —— 顶部「证据覆盖与强度」由
    # batch_synthesis 生成，「## 1. 主题概览」由 rebuild_synthesis_body 生成。
    # 实测 rule-v5 重标后只重跑了前者，后者仍写 descriptive(832)/总数 1280 的旧值，
    # 于是同一页出现两套互相矛盾的证据构成。这里强制两者逐项相等，
    # 任一生成步骤漏跑都会在 --check 与自检里暴露，而不是靠人眼比对。
    comps = []
    for m in re.finditer(r'^\|\s*证据类型(?:构成)?\s*\|\s*([^|]+?)\s*\|', content, re.M):
        d = {}
        # 两处统计块的写法不同：顶部是 "descriptive/observational 1391；protein
        # interaction 309"（空格分隔），第 1 节是 "descriptive/observational(1391)、
        # protein interaction(309)"（括号 + 顿号）。只按括号解析会漏掉前半，
        # 于是"两处不一致"永远不触发——这正是上一版守卫没抓到实测污染的原因。
        for chunk in re.split(r'[；;、,，]', m.group(1)):
            mm = re.match(r'^\s*([a-zA-Z][a-zA-Z /\-]*?)\s*[\(（]?(\d+)[\)）]?\s*$', chunk)
            if mm:
                d[mm.group(1).strip()] = int(mm.group(2))
        if d:
            comps.append(d)
    # 两块的**展示阈值**不同：顶部块是 etypes.most_common(6)（只列前 6 类），
    # 第 1 节列全部非零类型。所以只在"两块都出现的类型"上比较数值——
    # 这样才能抓到真正的数字漂移（descriptive 832 vs 1391），
    # 又不会把"第 7 类没进前 6"当成矛盾。
    if len(comps) > 1:
        a = comps[0]
        for b in comps[1:]:
            shared = set(a) & set(b)
            drift = [k for k in shared if a[k] != b[k]]
            if drift:
                worst = max(drift, key=lambda k: abs(a[k] - b[k]))
                issues.append('两处证据类型统计不一致（%s: %d vs %d），'
                              '说明只重跑了其中一个生成步骤'
                              % (worst, a[worst], b[worst]))
                break
    return list(dict.fromkeys(issues))  # 去重但保持首次出现的顺序


def generate_synthesis(cluster_id, cluster_def, cluster_evidence, consensus, contradictions):
    stats = compute_stats(cluster_evidence, consensus, contradictions)
    papers_md = top_papers_md(cluster_evidence)
    
    consensus_md = ""
    for i, c in enumerate(consensus):
        sample_lines = []
        for claim, src in zip(c['sample_claims'], c['sample_sources']):
            sample_lines.append(f"> *{claim[:150]}...*  ")
            sample_lines.append(f"> — {src}")
        sample_text = '\n'.join(sample_lines)
        consensus_md += f"""\n### C{i+1}: {c['pattern']}\n\n**支持论文数**: {c['paper_count']} | **证据条目数**: {c['evidence_count']}\n\n{sample_text}\n\n"""
    
    contradictions_md = ""
    if contradictions:
        for i, c in enumerate(contradictions):
            contradictions_md += f"""\n### ⚠️ D{i+1}: {c['gene']} — {c['type']}\n\n不同研究对{c['gene']}的调控方向存在分歧:\n{chr(10).join(f'- {src}' for src in c['sources'])}\n\n> **需要进一步验证**: 差异可能源于不同物种、组织或实验条件\n"""
    else:
        contradictions_md = "\n> 当前证据簇中未检测到明显矛盾，需人工审查确认。\n"
    
    gaps = [
        "跨物种保守性: 多数发现来自拟南芥，作物中的功能验证不足",
        "空间维度: 缺乏空间转录组级别的发育轨迹分析",
        "时间分辨率: 发育过程的高时间分辨率采样不足",
        "功能验证: 单细胞表达模式的功能验证有限",
        "多组学整合: 转录组与表观组/代谢组的整合分析不足",
    ]
    gaps_md = '\n'.join(f"- {g}" for g in gaps[:3])
    
    return f"""---
title: "Synthesis: {cluster_def['title']}"
type: synthesis
topics: [{', '.join(cluster_def['tags'])}]
total_evidence: {stats['total_evidence']}
total_papers: {stats['total_papers']}
relevance_soybean: "{cluster_def.get('relevance_to_soybean') or '待评估'}"
auto_discovered: true
cluster_size: {len(cluster_def['tags'])} tags
status: auto-generated
body_status: auto-generated
updated: {TODAY}
---

# {cluster_def.get('emoji', '📄')} Synthesis: {cluster_def['title']}

## Domain Overview

{cluster_def['description']}

**统计**:
- 涵盖论文: ~{stats['total_papers']} 篇
- 证据条目: {stats['total_evidence']} 条
- 共识发现: {stats['consensus_findings']} 项
- 潜在争议: {stats['contradictions']} 项
- 核心标签: {', '.join(cluster_def['tags'])}

**与大豆项目的关联**: {cluster_def.get('relevance_to_soybean') or '待评估'}

---

## Consensus Findings (跨论文共识)

{consensus_md}

---

## Contradictions & Controversies (争议与矛盾)

{contradictions_md}

---

## Knowledge Gaps (知识空白)

{gaps_md}

---

## Key Papers (关键文献)

以下按支撑证据条目数排序:

{papers_md}

---

## Hypotheses Emerging from This Synthesis

基于以上共识、争议和空白，可提出以下假设:

<!-- 待 P4b Hypotheses 阶段生成 -->

---

## References

本文档基于 {stats['total_evidence']} 条证据对象自动生成。
所有声明可追溯至具体论文的 Evidence Object。
主题通过标签共现网络自动发现 (不需要人工预定义)。

*自动生成于 {TODAY} | 需人工审查*
"""

# ============================================================
# 8 Core Themes (FIXED — do not add without explicit user request)
# ============================================================
_THEME_EMOJI = {
    'single-cell-spatial-omics': '🧫',
    'developmental-biology': '🌱',
    'metabolism-natural-products': '🧪',
    'hormone-signaling': '📡',
    'stress-immunity': '🛡️',
    'epigenetics-gene-regulation': '🧬',
    'methods-tools': '🔧',
    'genomics-evolution': '🧭',
}

# 与大豆（Glycine max）项目的关联说明：按主题写死一句可核对的定位描述，
# 不再依赖 score_soybean_relevance 在"新建页面"时缺失的字段。
_THEME_SOYBEAN = {
    'single-cell-spatial-omics': '为大豆节间单细胞与空间转录组提供细胞类型注释与轨迹分析方法',
    'developmental-biology': '节间伸长、维管发育与株型建成属于同一发育程序，可直接迁移到大豆株高调控',
    'metabolism-natural-products': '大豆异黄酮、皂苷与种子营养成分的合成路径解析',
    'hormone-signaling': '光质通过激素信号调控大豆节间伸长，是本项目的主线机制',
    'stress-immunity': '大豆胞囊线虫、疫霉与逆境耐受的候选基因来源',
    'epigenetics-gene-regulation': '光/温诱导的表观标记能否稳定遗传，决定设施栽培的可塑性',
    'methods-tools': '单细胞、空间组学与多组学整合方法的可用性评估',
    'genomics-evolution': '大豆基因家族扩张、驯化选择与共线性分析的方法与结论来源',
}


def _theme_def(theme_id):
    """主题定义由 themes.py 派生，禁止在本脚本里另写一份标签表。"""
    aliases = sorted(t for t, m in th.THEME_TAG_ALIASES.items() if m == theme_id)
    return {
        'title': th.display_title(theme_id),
        'title_zh': th.display_title(theme_id, 'zh'),
        'tags': aliases,
        'description': th.THEME_KEYWORDS.get(theme_id, [])[:6],
        'emoji': _THEME_EMOJI.get(theme_id, '📄'),
        'relevance_to_soybean': _THEME_SOYBEAN.get(
            theme_id, '暂无明确的大豆关联证据，需人工补充评估'),
    }


CORE_THEMES = {t: _theme_def(t) for t in th.THEMES}

# ============================================================
# Phase: Update existing 8 core synthesis pages only
# ============================================================
def update_core_synthesis(all_evidence):
    """Update existing 8 core synthesis pages with latest evidence counts.
    Does NOT create new themes. 8 themes are fixed."""
    updated = 0
    
    for theme_id, theme_def in CORE_THEMES.items():
        fpath = os.path.join(SYNTHESIS_DIR, f"{theme_id}.md")
        
        # Match evidence by the single shared taxonomy (themes.py)
        cluster_evidence = classify_evidence(all_evidence, theme_id)
        ev_count = len(cluster_evidence)
        
        if not os.path.exists(fpath):
            # Create new synthesis page only for the 8 core themes
            consensus = find_consensus(cluster_evidence)
            contradictions = find_contradictions(cluster_evidence)
            synthesis = generate_synthesis(theme_id, theme_def, cluster_evidence, consensus, contradictions)
            write_if_changed(fpath, synthesis)
            updated += 1
            print(f"  ✓ Created: {theme_id} ({ev_count} evidence)")
        else:
            # Update existing page: refresh evidence count in frontmatter
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            consensus = find_consensus(cluster_evidence)
            contradictions = find_contradictions(cluster_evidence)
            stats = compute_stats(cluster_evidence, consensus, contradictions)
            ev_count = stats['total_evidence']
            paper_count = stats['total_papers']

            # 所有计数来自同一个 stats，且 frontmatter / 统计块 / References 尾注一并改写
            content = re.sub(r'^total_evidence:\s*\d+', f'total_evidence: {ev_count}', content, flags=re.M)
            content = re.sub(r'^total_papers:\s*\d+', f'total_papers: {paper_count}', content, flags=re.M)
            content = re.sub(r'^updated:\s*\S+', f'updated: {TODAY}', content, flags=re.M)
            if not re.search(r'^body_status:', content, re.M):
                # 已有 8 页是历史正文：明确标注，禁止把自动统计当成正文重建。
                content = re.sub(r'^(type: synthesis\s*)$',
                                 r'\1\nbody_status: legacy-prose', content, count=1, flags=re.M)
            content = re.sub(r'证据条目[:：]\s*\d+', f'证据条目: {ev_count}', content)
            content = re.sub(r'涵盖论文[:：]\s*~?\d+', f'涵盖论文: ~{paper_count}', content)
            content = re.sub(r'本文档基于\s*\d+\s*条证据对象', f'本文档基于 {ev_count} 条证据对象', content)
            content = re.sub(r'自动生成于\s*\d{4}-\d{2}-\d{2}', f'自动生成于 {TODAY}', content)
            content = content.replace('<!-- 待补充: 基于 citation 和 evidence 数量的排名 -->',
                                      top_papers_md(cluster_evidence))
            content = rewrite_scope_counts(content, ev_count, paper_count, TODAY)
            content = refresh_auto_sections(content, cluster_evidence)
            content = fix_literal_newlines(content)

            for issue in page_consistency_issues(content):
                print(f"  ! {theme_id}: {issue}")
            
            changed = write_if_changed(fpath, content)
            updated += 1
            mark = '' if changed else ' (unchanged)'
            print(f"  ✓ Updated: {theme_id} ({ev_count} evidence, ~{paper_count} papers){mark}")
    
    return updated

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else '--update'
    
    print("Phase 1: Loading evidence...")
    all_evidence = load_all_evidence()
    print(f"  Loaded {len(all_evidence)} evidence objects")
    # 2026-11-04：0 证据必须硬退出。实测事故——脚本在没设 KB_BASE 时把 BASE 退回
    # 仓库根（kb_paths.py 的兜底），evidence 目录不存在 → 加载 0 条，却仍然
    # "✓ Created" 了 8 个只有统计空壳的合成页。若不是立刻发现并删除，下一次
    # 部署就会用空页覆盖知识库里的真综述。宁可失败，不可静默清空。
    if not all_evidence:
        sys.stderr.write(
            "ERROR: 加载到 0 条证据，拒绝写入。\n"
            "       当前 BASE=%s\n"
            "       请检查 KB_BASE 是否指向知识库根（应含 evidence/ 目录），\n"
            "       而不是仓库根 %s。\n" % (BASE, REPO_ROOT))
        return 4  # 4 = 拒写（空库），与正常返回的"更新页数"区分开
    
    if mode == '--check':
        # 只读体检：报告数字不一致 / 占位符残留 / 拼接损坏
        bad = 0
        for theme_id in CORE_THEMES:
            fpath = os.path.join(SYNTHESIS_DIR, f'{theme_id}.md')
            if not os.path.exists(fpath):
                print(f'  ? {theme_id}: 缺失（未生成）')
                continue
            with open(fpath, encoding='utf-8') as f:
                content = f.read()
            issues = page_consistency_issues(content)
            if issues:
                bad += 1
                print(f'  ✗ {theme_id}')
                for it in issues:
                    print(f'      - {it}')
            else:
                print(f'  ✓ {theme_id}')
        print(f'\nDONE: {bad}/{len(CORE_THEMES)} synthesis 页面存在一致性问题')
        return 1 if bad else 0

    if mode == '--discover':
        # ⚠️ Opt-in only: auto-discover new themes (NOT default)
        # This mode should only be used with explicit user instruction
        print("\n⚠️  --discover mode: Auto-discovering themes (user-requested)")
        clusters = auto_discover_clusters(all_evidence)
        print(f"  Discovered {len(clusters)} topics")
        
        for cluster_id, cluster_def in clusters.items():
            cluster_evidence = classify_evidence(all_evidence, set(cluster_def['tags']))
            consensus = find_consensus(cluster_evidence)
            contradictions = find_contradictions(cluster_evidence)
            synthesis = generate_synthesis(cluster_id, cluster_def, cluster_evidence, consensus, contradictions)
            fpath = os.path.join(SYNTHESIS_DIR, f"{cluster_id}.md")
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(synthesis)
        
        print(f"\nDONE: {len(clusters)} Synthesis pages (auto-discovered)")
    else:
        # Default: update existing 8 core themes only (do NOT create new themes)
        print(f"\nPhase 2: Updating 8 core synthesis pages (fixed themes, no new discovery)...")
        updated = update_core_synthesis(all_evidence)
        print(f"\nDONE: {updated}/8 core themes updated")

if __name__ == '__main__':
    sys.exit(main() or 0)
