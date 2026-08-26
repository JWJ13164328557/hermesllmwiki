#!/usr/bin/env python3
"""
多源文献检索 — 整合 5 个来源到每日知识库更新
用法: python3 multi_source_search.py [--days 30] [--max 20]
输出: multi_source_candidates.json (统一格式)
"""

import urllib.parse, subprocess, json, os, sys, re, time
from datetime import datetime, timedelta

BASE = '/mnt/g/hermes_obsidian/hermes'
OUTPUT = f'{BASE}/scripts/multi_source_candidates.json'

# ══════════════════════════════════════════════════════════════
# 物种限定 — 统一来源 species_registry.py (2026-08-26 重整)
# 原:仅 plant/Arabidopsis/rice 3种硬编码, 导致多源通道检索召回远小于
#    PubMed 通道(大豆/玉米/番茄等作物完全未覆盖). 现: 153 种, 与
#    daily_update.py / daily_full_pipeline.py / theme_filter.py 同源.
# ══════════════════════════════════════════════════════════════
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from species_registry import build_search_or_clause_plain
PLANT_SPECIES = build_search_or_clause_plain()

# 10 search queries — same as daily_update.py (物种限定统一来自 registry)
SEARCH_QUERIES = [
    # ⭐ FOCUS 1: Plant single-cell omics
    f'("single-cell" OR "scRNA-seq" OR "single nucleus" OR "snRNA-seq" OR "scATAC-seq" OR "single cell atlas" OR "cell atlas") AND {PLANT_SPECIES}',
    # ⭐ FOCUS 2: Plant spatial transcriptomics
    f'("spatial transcriptom" OR "Stereo-seq" OR "Visium" OR "Xenium" OR "MERFISH" OR "spatial multi-omics" OR "spatially resolved") AND {PLANT_SPECIES}',
    # ⭐ FOCUS 3: Light signaling & photosynthesis
    f'("light signaling" OR "photomorphogenesis" OR "phytochrome" OR "photoreceptor" OR "blue light" OR "red light" OR "far-red" OR "shade avoidance" OR "photosynthesis" OR "chloroplast" OR "stomatal" OR "circadian" OR "light quality") AND {PLANT_SPECIES}',
    # ⭐ FOCUS 4: Plant development
    f'("plant development" OR "root development" OR "shoot apical" OR "flower development" OR "seed development" OR "vascular development" OR "wood formation" OR "secondary growth" OR "xylem" OR "phloem" OR "meristem" OR "organogenesis" OR "embryogenesis" OR "cambium") AND {PLANT_SPECIES}',
    # Supplementary: ATAC / multi-omics
    f'("ATAC-seq" OR "multi-omics" OR "snATAC" OR "CUT&Tag") AND {PLANT_SPECIES}',
    # Supplementary: regeneration
    f'("callus" OR "regeneration" OR "somatic embryo" OR "de novo organogenesis" OR "reprogramming") AND {PLANT_SPECIES}',
    # Supplementary: stress & immunity
    f'("salt stress" OR "drought stress" OR "cold stress" OR "heat stress" OR "heavy metal" OR "pathogen" OR "immunity" OR "defense" OR "herbivory") AND {PLANT_SPECIES}',
    # Supplementary: metabolism
    f'("flavonoid" OR "anthocyanin" OR "terpenoid" OR "alkaloid" OR "tanshinone" OR "artemisinin" OR "metabolic engineering" OR "biosynthesis") AND {PLANT_SPECIES}',
    # Supplementary: epigenetics
    f'("histone" OR "chromatin" OR "DNA methylation" OR "H3K27" OR "epigenetic") AND {PLANT_SPECIES}',
    # Supplementary: hormone signaling
    f'("auxin" OR "gibberellin" OR "abscisic acid" OR "jasmonic acid" OR "salicylic acid" OR "ethylene" OR "brassinosteroid" OR "strigolactone" OR "cytokinin") AND {PLANT_SPECIES}',
]

def http_get(url, timeout=15, retries=2):
    """Simple HTTP GET with retries for rate limiting"""
    for attempt in range(retries + 1):
        try:
            import urllib.request
            req = urllib.request.Request(url, headers={'User-Agent': 'HermesKB/2.0 (mailto:jwj@example.com)'})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read())
        except Exception as e:
            if '429' in str(e) and attempt < retries:
                wait = 2 ** attempt * 2
                print(f"  ⚠ Rate limited, retry in {wait}s...", file=sys.stderr)
                time.sleep(wait)
                continue
            if attempt == retries:
                print(f"  ⚠ HTTP error: {e}", file=sys.stderr)
    return None


def pubmed_to_plain(query):
    """Convert PubMed query syntax to plain keyword text for non-PubMed APIs"""
    # Remove field specifiers like [Title/Abstract], [All Fields]
    plain = re.sub(r'\[[^\]]+\]', '', query)
    # Remove excessive parentheses
    plain = plain.replace('(', ' ').replace(')', ' ')
    # Unquote double-quoted terms
    plain = plain.replace('"', '')
    # Normalize spaces
    plain = ' '.join(plain.split())
    return plain[:500]


###############################################################################
# SOURCE 1: PubMed (already implemented, kept for consistency)
###############################################################################
def search_pubmed(query, days=30, max_results=30):
    from_date = (datetime.now() - timedelta(days=days)).strftime('%Y/%m/%d')
    encoded = urllib.parse.quote(f'({query}) AND ("{from_date}"[Date - Publication] : "3000"[Date - Publication])')
    url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={encoded}&retmax={max_results}&sort=date&retmode=json'
    data = http_get(url)
    return data.get('esearchresult', {}).get('idlist', []) if data else []


###############################################################################
# SOURCE 2: Semantic Scholar — semantic search + citation-aware
###############################################################################
def search_semantic_scholar(query, days=30, limit=20):
    """Semantic Scholar search — returns papers with DOI, title, year, abstract, OA status"""
    papers = []
    plain = pubmed_to_plain(query)  # Convert PubMed syntax to plain text
    encoded = urllib.parse.quote(plain[:300])
    fields = 'title,authors,year,abstract,externalIds,publicationVenue,openAccessPdf,isOpenAccess,publicationDate'
    url = f'https://api.semanticscholar.org/graph/v1/paper/search?query={encoded}&limit={limit}&fields={fields}'
    
    data = http_get(url, timeout=20, retries=3)  # Retry up to 3x for 429
    if not data:
        return papers
    
    cutoff = (datetime.now() - timedelta(days=days))
    for paper in data.get('data', []):
        pub_date = paper.get('publicationDate') or ''
        try:
            if pub_date:
                pd = datetime.strptime(pub_date[:10], '%Y-%m-%d')
                if pd < cutoff:
                    continue
        except:
            pass
        
        doi = (paper.get('externalIds') or {}).get('DOI', '')
        if not doi:
            continue
        
        venue = paper.get('publicationVenue') or {}
        papers.append({
            'source': 'semantic_scholar',
            'doi': doi,
            'title': paper.get('title', '') or '',
            'journal': venue.get('name', '') or '',
            'year': str(paper.get('year', '')),
            'abstract': paper.get('abstract', '') or '',
            'authors': [a.get('name', '') for a in (paper.get('authors') or [])[:5]],
            'is_oa': paper.get('isOpenAccess', False),
            'oa_pdf': (paper.get('openAccessPdf') or {}).get('url', ''),
        })
    return papers


###############################################################################
# SOURCE 3: OpenAlex — author/institution/concept expansion
###############################################################################
def search_openalex(query, days=30, limit=20):
    """OpenAlex search — rich metadata: authors, institutions, concepts"""
    papers = []
    plain = pubmed_to_plain(query)  # Convert PubMed syntax
    encoded = urllib.parse.quote(plain[:500])
    from_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
    url = (f'https://api.openalex.org/works?search={encoded}'
           f'&filter=from_publication_date:{from_date},type:article,is_paratext:false'
           f'&per_page={limit}&sort=publication_date:desc')
    
    data = http_get(url, timeout=20)
    if not data:
        return papers
    
    for work in data.get('results', []):
        doi = work.get('doi', '')
        if not doi:
            continue
        # Clean doi prefix
        doi_fixed = doi.replace('https://doi.org/', '')
        
        # Authors with institutions
        authors = []
        for a in (work.get('authorships') or [])[:5]:
            author_info = a.get('author', {})
            insts = [i.get('display_name', '') for i in (a.get('institutions') or [])[:2]]
            authors.append({
                'name': author_info.get('display_name', ''),
                'institutions': insts
            })
        
        # Primary location (journal)
        loc = work.get('primary_location') or {}
        source = loc.get('source') or {}
        
        # Concepts/topics
        concepts = [c.get('display_name', '') for c in (work.get('concepts') or [])[:5]]
        
        papers.append({
            'source': 'openalex',
            'doi': doi_fixed,
            'title': work.get('title', ''),
            'journal': source.get('display_name', ''),
            'year': str(work.get('publication_year', '')),
            'abstract': '',  # OpenAlex doesn't include abstracts in search results
            'authors': authors,
            'concepts': concepts,
            'is_oa': (work.get('open_access') or {}).get('is_oa', False),
            'cited_by': work.get('cited_by_count', 0),
        })
    return papers


###############################################################################
# SOURCE 4: PubMed/PMC (Core) — already primary via search_pubmed + fetch_full_paper
###############################################################################


###############################################################################
# SOURCE 5: Crossref — DOI/metadata verification, supplementary discovery
###############################################################################
def search_crossref(query, days=30, limit=20):
    """Crossref search — good for catching papers not in PubMed/OpenAlex"""
    papers = []
    encoded = urllib.parse.quote(query[:500])
    from_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
    
    # Crossref REST API
    url = (f'https://api.crossref.org/works?query={encoded}'
           f'&filter=from-pub-date:{from_date},type:journal-article'
           f'&rows={limit}&sort=published&order=desc'
           f'&mailto=hermes-kb@example.com')
    
    data = http_get(url, timeout=20)
    if not data:
        return papers
    
    for item in data.get('message', {}).get('items', []):
        doi = item.get('DOI', '')
        if not doi:
            continue
        
        authors = []
        for a in (item.get('author') or [])[:5]:
            authors.append(f"{a.get('given', '')} {a.get('family', '')}".strip())
        
        # Journal name
        journal = ''
        container = item.get('container-title', [])
        if container:
            journal = container[0]
        
        # Abstract
        abstract = item.get('abstract', '')
        # Crossref abstracts sometimes have HTML tags
        if abstract:
            abstract = re.sub(r'<[^>]+>', '', abstract)
        
        papers.append({
            'source': 'crossref',
            'doi': doi,
            'title': ' '.join(item.get('title', [''])),
            'journal': journal,
            'year': str(item.get('published-print', {}).get('date-parts', [[None]])[0][0] or ''),
            'abstract': abstract[:3000],
            'authors': authors,
        })
    return papers


###############################################################################
# SOURCE 6: Web search — preprints, GitHub, project pages, supplementary info
###############################################################################
def search_web(query, limit=5):
    """
    Web search for non-traditional sources: bioRxiv/arXiv preprints, GitHub repos,
    project pages, supplementary data.
    Uses DuckDuckGo HTML (no API key needed).
    """
    papers = []
    encoded = urllib.parse.quote(f'site:biorxiv.org OR site:arxiv.org OR site:github.com {query}')
    url = f'https://html.duckduckgo.com/html/?q={encoded}'
    
    try:
        import urllib.request as req
        hdrs = {'User-Agent': 'Mozilla/5.0 (compatible; HermesKB/2.0)'}
        rq = req.Request(url, headers=hdrs)
        with req.urlopen(rq, timeout=15) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        
        # Parse DuckDuckGo HTML results
        from html.parser import HTMLParser
        
        class DDParser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.results = []
                self.in_result = False
                self.in_link = False
                self.current = {}
                self.text_buf = []
                self.link_url = ''
            def handle_starttag(self, tag, attrs):
                attrs = dict(attrs)
                if tag == 'div' and 'result' in attrs.get('class', ''):
                    self.in_result = True
                    self.current = {'source': 'web'}
                    self.text_buf = []
                if self.in_result and tag == 'a' and 'result__a' in attrs.get('class', ''):
                    self.in_link = True
                    self.link_url = attrs.get('href', '')
            def handle_data(self, data):
                if self.in_link:
                    self.current['title'] = data.strip()
                    self.current['url'] = self.link_url
                elif self.in_result:
                    self.text_buf.append(data.strip())
            def handle_endtag(self, tag):
                if tag == 'a':
                    self.in_link = False
                if tag == 'div' and self.in_result:
                    self.in_result = False
                    self.current['snippet'] = ' '.join(self.text_buf)[:500]
                    if self.current.get('title') and self.current.get('url'):
                        self.results.append(self.current.copy())
        
        parser = DDParser()
        parser.feed(html)
        
        for r in parser.results[:limit]:
            papers.append({
                'source': 'web',
                'doi': '',  # web results typically don't have DOI
                'title': r.get('title', ''),
                'url': r.get('url', ''),
                'snippet': r.get('snippet', ''),
            })
    except Exception as e:
        print(f"  ⚠ Web search error: {e}", file=sys.stderr)
    
    return papers


###############################################################################
# MAIN: Multi-source aggregation
###############################################################################
def main():
    days = 30
    max_results = 20
    skip_s2 = '--skip-s2' in sys.argv
    skip_web = '--skip-web' in sys.argv
    for i, arg in enumerate(sys.argv):
        if arg == '--days' and i+1 < len(sys.argv):
            days = int(sys.argv[i+1])
        elif arg.startswith('--days='):
            days = int(arg.split('=')[1])
        elif arg == '--max' and i+1 < len(sys.argv):
            max_results = int(sys.argv[i+1])
        elif arg.startswith('--max='):
            max_results = int(arg.split('=')[1])
    
    print(f"🔍 Multi-source literature search: {days} days, {len(SEARCH_QUERIES)} queries")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    
    all_candidates = {}  # doi -> paper dict
    
    for qi, query in enumerate(SEARCH_QUERIES):
        qname = query.split(' AND ')[0].strip('("')[:50]
        print(f"\n{'='*60}")
        print(f"Q{qi+1}: {qname}...")
        print(f"{'='*60}")
        
        # --- PubMed (primary) ---
        pmids = search_pubmed(query, days=days, max_results=max_results)
        print(f"  PubMed: {len(pmids)} candidates")
        
        # --- Semantic Scholar ---
        if not skip_s2:
            s2_papers = search_semantic_scholar(query, days=days, limit=max_results)
            print(f"  Semantic Scholar: {len(s2_papers)} papers")
            for p in s2_papers:
                doi = p['doi']
                if doi not in all_candidates:
                    all_candidates[doi] = p
                else:
                    existing = all_candidates[doi]
                    if p.get('abstract') and not existing.get('abstract'):
                        existing['abstract'] = p['abstract']
                    existing['sources'] = existing.get('sources', [existing.get('source', '')]) + ['semantic_scholar']
        
        # --- OpenAlex ---
        oa_papers = search_openalex(query, days=days, limit=max_results)
        print(f"  OpenAlex: {len(oa_papers)} papers")
        for p in oa_papers:
            doi = p['doi']
            if doi not in all_candidates:
                all_candidates[doi] = p
            else:
                existing = all_candidates[doi]
                existing['concepts'] = existing.get('concepts', []) + p.get('concepts', [])
                existing['sources'] = existing.get('sources', [existing.get('source', '')]) + ['openalex']
        
        # --- Crossref ---
        cr_papers = search_crossref(query, days=days, limit=max_results)
        print(f"  Crossref: {len(cr_papers)} papers")
        for p in cr_papers:
            doi = p['doi']
            if doi not in all_candidates:
                all_candidates[doi] = p
            else:
                existing = all_candidates[doi]
                if p.get('abstract') and not existing.get('abstract'):
                    existing['abstract'] = p['abstract']
                if p.get('journal') and not existing.get('journal'):
                    existing['journal'] = p['journal']
                existing['sources'] = existing.get('sources', [existing.get('source', '')]) + ['crossref']
        
        # --- Web search (only on first 3 queries, skippable) ---
        if not skip_web and qi < 3:
            web_papers = search_web(query, limit=3)
            print(f"  Web (bioRxiv/arXiv/GitHub): {len(web_papers)} results")
            for p in web_papers:
                # Web results don't have DOI, use URL as unique key
                key = p.get('url', '')
                if key and key not in all_candidates:
                    all_candidates[key] = p
        
        time.sleep(1)  # Rate limiting
    
    # --- Output ---
    print(f"\n{'='*60}")
    print(f"📊 TOTAL unique candidates: {len(all_candidates)}")
    
    # Separate into DOI-based papers (for import) vs web results
    doi_papers = {k: v for k, v in all_candidates.items() if v.get('doi')}
    web_results = {k: v for k, v in all_candidates.items() if not v.get('doi')}
    
    print(f"   DOI papers: {len(doi_papers)}")
    print(f"   Web results: {len(web_results)}")
    
    # Source breakdown
    sources = {}
    for p in all_candidates.values():
        sources[p['source']] = sources.get(p['source'], 0) + 1
    print(f"   By source: {sources}")
    
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        json.dump({
            'date': datetime.now().strftime('%Y-%m-%d'),
            'days': days,
            'total': len(all_candidates),
            'doi_papers': len(doi_papers),
            'web_results': len(web_results),
            'candidates': list(all_candidates.values())
        }, f, indent=2, ensure_ascii=False)
    
    print(f"\n📄 Output: {OUTPUT} ({os.path.getsize(OUTPUT)} bytes)")


if __name__ == '__main__':
    main()
