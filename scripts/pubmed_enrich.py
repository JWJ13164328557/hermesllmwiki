#!/usr/bin/env python3
"""
PubMed 爬虫 — 知识库集成版
用法: python3 pubmed_enrich.py --enrich-all     # 补全知识库所有论文
      python3 pubmed_enrich.py --keyword "..."  # 搜索新论文
"""
import requests, os, re, json, time, random, sys
from bs4 import BeautifulSoup

BASE = '/mnt/g/hermes_obsidian/hermes'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120',
    'Accept-Language': 'en-US,en;q=0.5',
}

def extract_identifiers(soup):
    ids = {'DOI': '', 'PMID': '', 'PMCID': ''}
    for meta in soup.find_all('meta'):
        name = meta.get('name','')
        if name == 'citation_doi': ids['DOI'] = meta.get('content','')
        elif name == 'citation_pmid': ids['PMID'] = meta.get('content','')
    # PMC link
    pmc_link = soup.find('a', href=lambda h: h and 'pmc/articles' in h)
    if pmc_link:
        m = re.search(r'PMC(\d+)', pmc_link.get('href',''))
        if m: ids['PMCID'] = f'PMC{m.group(1)}'
    return ids

def scrape_pubmed_page(pmid):
    """Scrape a single PubMed article page for complete metadata"""
    url = f'https://pubmed.ncbi.nlm.nih.gov/{pmid}/'
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
        
        # Title
        title_el = soup.find('h1', class_='heading-title')
        title = title_el.text.strip() if title_el else ''
        
        # Authors
        authors = [a.text.strip() for a in soup.find_all('a', class_='full-name')]
        
        # Abstract
        abs_el = soup.find('div', class_='abstract-content selected')
        if not abs_el:
            abs_el = soup.find('div', {'id': 'eng-abstract'})
        abstract = abs_el.text.strip() if abs_el else ''
        
        # Keywords
        keywords = []
        kw_section = soup.find('div', class_='keywords')
        if kw_section:
            keywords = [k.text.strip() for k in kw_section.find_all('button') if k.text.strip()]
        
        # Journal info
        cite_el = soup.find('span', class_='cit')
        cite = cite_el.text.strip() if cite_el else ''
        
        # Identifiers
        ids = extract_identifiers(soup)
        
        return {
            'title': title, 'authors': authors, 'abstract': abstract,
            'keywords': keywords, 'cite': cite,
            'doi': ids['DOI'], 'pmid': ids['PMID'] or pmid,
            'pmcid': ids['PMCID']
        }
    except Exception as e:
        return None

def enrich_knowledge_base():
    """Update all existing concept pages with scraped PubMed data"""
    concepts_dir = f'{BASE}/concepts'
    updated = 0
    
    for fname in sorted(os.listdir(concepts_dir)):
        if not fname.endswith('.md') or fname.startswith('ref') or fname.startswith('xr'):
            continue
        slug = fname.replace('.md','')
        path = f'{concepts_dir}/{fname}'
        
        with open(path,'r',encoding='utf-8') as f:
            cc = f.read()
        
        # Get PMID
        pm = re.search(r'pmid:\s*(\d+)', cc, re.I)
        if not pm: continue
        pmid = pm.group(1)
        
        # Skip if already has full content
        if len(cc) > 3000 and 'Keywords' in cc:
            continue
        
        print(f"  Scraping PMID:{pmid}...")
        paper = scrape_pubmed_page(pmid)
        if not paper:
            print(f"    ✗ Failed")
            continue
        
        doi = paper['doi'] or re.search(r'doi:\s*(10\.\d{4,}/[^\s\n]+)', cc, re.I)
        if doi and not isinstance(doi, str): doi = doi.group(1) if doi else ''
        
        # Build full content
        content = f"""---
title: {paper['title'][:80]}
created: 2026-05-28
updated: {time.strftime('%Y-%m-%d')}
type: concept
tags: [papers]
pmid: {paper['pmid']}
doi: {doi}
confidence: high
---

# {paper['title']}

## 论文信息
- **引用**: {paper['cite']}
- **PMID**: [{paper['pmid']}](https://pubmed.ncbi.nlm.nih.gov/{paper['pmid']}/)
- **DOI**: {doi}
- **作者**: {', '.join(paper['authors'][:10])}

## 摘要
{paper['abstract'][:3000]}

## 关键词
{', '.join(paper['keywords']) if paper['keywords'] else '—'}

## 深度提炼

**来源**: PMID:{paper['pmid']} | DOI:{doi}
"""
        with open(path,'w',encoding='utf-8') as f:
            f.write(content)
        updated += 1
        print(f"    ✓ {paper['title'][:50]}")
        
        time.sleep(random.uniform(0.5, 1.5))
    
    return updated

def search_and_crawl(keyword, max_articles=20, output_dir=None):
    """Search PubMed and crawl results"""
    if not output_dir:
        output_dir = f'{BASE}/pubmed_crawl/{keyword.replace(" ","_")[:50]}'
    os.makedirs(output_dir, exist_ok=True)
    
    url = f'https://pubmed.ncbi.nlm.nih.gov/?term={requests.utils.quote(keyword)}&size=50'
    resp = requests.get(url, headers=HEADERS, timeout=15)
    soup = BeautifulSoup(resp.text, 'html.parser')
    
    article_links = [a['href'] for a in soup.find_all('a', class_='docsum-title')][:max_articles]
    print(f"Found {len(article_links)} articles for '{keyword}'")
    
    crawled = 0
    for link in article_links:
        pmid = re.search(r'/(\d+)/', link)
        if not pmid: continue
        
        paper = scrape_pubmed_page(pmid.group(1))
        if not paper: continue
        
        # Save JSON
        fname = re.sub(r'[^\w\s]', '_', paper['title'])[:80]
        with open(f'{output_dir}/{fname}.json','w',encoding='utf-8') as f:
            json.dump(paper, f, ensure_ascii=False, indent=2)
        
        # Also create wiki concept page
        slug = f"crawl-{paper['pmid']}"
        content = f"""---
title: {paper['title'][:80]}
created: {time.strftime('%Y-%m-%d')}
type: concept
tags: [papers]
pmid: {paper['pmid']}
doi: {paper['doi']}
confidence: high
---

# {paper['title']}

- **作者**: {', '.join(paper['authors'][:8])}
- **PMID**: {paper['pmid']} | DOI: {paper['doi']}
- {paper['cite']}

## 摘要
{paper['abstract'][:2000]}

## 关键词
{', '.join(paper['keywords']) if paper['keywords'] else '—'}
"""
        with open(f'{BASE}/concepts/{slug}.md','w',encoding='utf-8') as f:
            f.write(content)
        crawled += 1
        print(f"  ✓ {paper['title'][:55]}")
        time.sleep(random.uniform(0.5, 1.5))
    
    return crawled

if __name__ == '__main__':
    if '--enrich-all' in sys.argv:
        print("📚 补全知识库所有论文...")
        n = enrich_knowledge_base()
        print(f"✅ 更新: {n} 篇")
    elif '--keyword' in sys.argv:
        idx = sys.argv.index('--keyword')
        kw = sys.argv[idx+1] if idx+1 < len(sys.argv) else 'Spatial Transcriptomics plant'
        n = search_and_crawl(kw)
        print(f"✅ 爬取: {n} 篇")
    else:
        print("用法: python3 pubmed_enrich.py --enrich-all")
        print("      python3 pubmed_enrich.py --keyword 'Spatial Transcriptomics plant'")
