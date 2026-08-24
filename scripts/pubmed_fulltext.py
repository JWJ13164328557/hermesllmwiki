#!/usr/bin/env python3
"""
PubMed 完整论文爬虫 — 下载PMC全文 + 期刊OA全文
用法: python3 pubmed_fulltext.py --enrich-all
"""
import os, re, subprocess, json, time, random, sys
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import requests

BASE = '/mnt/g/hermes_obsidian/hermes'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120',
    'Accept-Language': 'en-US,en;q=0.5',
}

def get_pmcid(pmid):
    """Get PMCID from PubMed"""
    try:
        proc = subprocess.run(['curl','-sL','--connect-timeout','8',
            f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml'],
            capture_output=True, text=True, timeout=12)
        root = ET.fromstring(proc.stdout)
        for aid in root.findall('.//ArticleId'):
            if aid.get('IdType') == 'pmc':
                return aid.text
    except: pass
    return None

def download_pmc_fulltext(pmcid):
    """Download COMPLETE full text from PMC as structured sections"""
    try:
        url = f'https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/?report=classic'
        resp = requests.get(url, headers=HEADERS, timeout=30)
        html = resp.text
        if len(html) < 5000: return None
        
        soup = BeautifulSoup(html, 'html.parser')
        
        # Find all sections
        sections = []
        for sec_div in soup.find_all('div', class_=lambda c: c and ('tsec' in c or 'sec' in c)):
            # Section title
            title_el = sec_div.find(['h2','h3','h4','strong'])
            sec_title = title_el.get_text(strip=True) if title_el else ''
            
            # Section paragraphs
            paras = []
            for p in sec_div.find_all('p'):
                txt = p.get_text(strip=True)
                if len(txt) > 30:
                    paras.append(txt)
            
            if paras:
                sections.append({
                    'title': sec_title,
                    'text': ' '.join(paras)
                })
        
        return sections if sections else None
    except:
        return None

def scrape_pubmed_metadata(pmid):
    """Scrape PubMed page for metadata"""
    url = f'https://pubmed.ncbi.nlm.nih.gov/{pmid}/'
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(resp.text, 'html.parser')
        
        title_el = soup.find('h1', class_='heading-title')
        title = title_el.text.strip() if title_el else ''
        
        authors = [a.text.strip() for a in soup.find_all('a', class_='full-name')]
        
        abs_el = soup.find('div', class_='abstract-content selected')
        abstract = abs_el.text.strip() if abs_el else ''
        
        cite_el = soup.find('span', class_='cit')
        cite = cite_el.text.strip() if cite_el else ''
        
        # DOI
        doi = ''
        for meta in soup.find_all('meta'):
            if meta.get('name') == 'citation_doi':
                doi = meta.get('content','')
        
        return {
            'title': title, 'authors': authors, 'abstract': abstract,
            'cite': cite, 'doi': doi, 'pmid': pmid
        }
    except:
        return None

def enrich_with_fulltext():
    """Download full text for ALL papers, create complete concept pages"""
    concepts_dir = f'{BASE}/concepts'
    ft_count = 0
    ab_count = 0
    
    for fname in sorted(os.listdir(concepts_dir)):
        if not fname.endswith('.md') or fname.startswith('ref') or fname.startswith('xr'):
            continue
        slug = fname.replace('.md','')
        path = f'{concepts_dir}/{fname}'
        
        with open(path,'r',encoding='utf-8') as f:
            cc = f.read()
        
        pm = re.search(r'pmid:\s*(\d+)', cc, re.I)
        if not pm: continue
        pmid = pm.group(1)
        
        # Skip if already has full text
        if '## 全文' in cc and len(cc) > 5000:
            continue
        
        print(f"  [{slug[:30]}] PMID:{pmid}...", end=' ')
        
        # 1. Get metadata from PubMed HTML
        meta = scrape_pubmed_metadata(pmid)
        if not meta:
            print("✗ metadata failed")
            continue
        
        # 2. Try PMC full text
        pmcid = get_pmcid(pmid)
        fulltext_sections = None
        if pmcid:
            fulltext_sections = download_pmc_fulltext(pmcid)
        
        doi = meta['doi']
        title = meta['title']
        
        # 3. Build comprehensive content
        content = f"""---
title: {title[:80]}
created: 2026-05-28
updated: {time.strftime('%Y-%m-%d')}
type: concept
tags: [papers]
pmid: {pmid}
doi: {doi}
confidence: high
---

# {title}

## 论文信息
- **引用**: {meta['cite']}
- **PMID**: [{pmid}](https://pubmed.ncbi.nlm.nih.gov/{pmid}/)
- **DOI**: [{doi}](https://doi.org/{doi})
- **作者**: {', '.join(meta['authors'][:10])}
"""
        
        # Add full text if available
        if fulltext_sections:
            content += "\n## 全文 (PMC)\n\n"
            for s in fulltext_sections[:15]:
                title_str = f"### {s['title']}\n\n" if s['title'] else ''
                content += f"{title_str}{s['text'][:3000]}\n\n"
            content += f"\n*PMC全文: [{pmcid}](https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/)*\n"
        else:
            content += f"""
## 摘要
{meta['abstract'][:3000]}

> ⚠️ 全文需通过VPN从期刊官网下载 (非OA)
"""
        
        # Add abstract section for completeness
        if fulltext_sections:
            content += f"""
## 摘要
{meta['abstract'][:2000]}
"""
        
        with open(path,'w',encoding='utf-8') as f:
            f.write(content)
        
        if fulltext_sections:
            ft_count += 1
            print(f"PMC全文 ✓ ({len(fulltext_sections)} sections)")
        else:
            ab_count += 1
            print("摘要 (需VPN)")
        
        time.sleep(random.uniform(0.3, 1.0))
    
    return ft_count, ab_count

if __name__ == '__main__':
    print("📚 下载完整论文全文...")
    ft, ab = enrich_with_fulltext()
    print(f"\n✅ 全文: {ft}篇 | 摘要: {ab}篇 (需VPN)" )
