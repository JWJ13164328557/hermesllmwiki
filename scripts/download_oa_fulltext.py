#!/usr/bin/env python3
"""通过 Semantic Scholar + Europe PMC 检查 OA 状态并下载全文"""
import os, re, json, subprocess, time, csv
from datetime import datetime

BASE = '/mnt/g/hermes_obsidian/hermes'
CONCEPTS_DIR = os.path.join(BASE, 'concepts', 'papers')
TODAY = datetime.now().strftime('%Y-%m-%d')

def curl(url, timeout=20):
    try:
        r = subprocess.run(['curl', '-sL', '--connect-timeout', '8', '--max-time', str(timeout), url],
                          capture_output=True, text=True, timeout=timeout+5)
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout
    except: pass
    return None

def check_semantic_scholar(doi):
    """检查 Semantic Scholar OA 状态"""
    url = f'https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}?fields=isOpenAccess,openAccessPdf,externalIds,title'
    raw = curl(url, timeout=15)
    if not raw:
        return None
    try:
        data = json.loads(raw)
        is_oa = data.get('isOpenAccess', False)
        pdf_url = data.get('openAccessPdf', {}).get('url', '') if data.get('openAccessPdf') else ''
        pmid = data.get('externalIds', {}).get('PubMed', '')
        return {
            'is_oa': is_oa,
            'pdf_url': pdf_url,
            'pmid': pmid,
            'title': data.get('title', '')
        }
    except:
        return None

def check_europe_pmc(doi):
    """检查 Europe PMC OA 状态"""
    url = f'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:{doi}&format=json&resultType=core'
    raw = curl(url, timeout=15)
    if not raw:
        return None
    try:
        data = json.loads(raw)
        results = data.get('resultList', {}).get('result', [])
        if not results:
            return None
        r = results[0]
        pmcid = r.get('pmcid', '')
        is_oa = r.get('isOpenAccess', '') == 'Y'
        has_fulltext = r.get('hasFullText', '') == 'Y'
        return {
            'pmcid': pmcid,
            'is_oa': is_oa,
            'has_fulltext': has_fulltext,
            'title': r.get('title', '')
        }
    except:
        return None

def download_pmc_fulltext(pmcid):
    """下载 PMC 全文"""
    url = f'https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/?report=classic'
    html = curl(url, timeout=20)
    if not html:
        return None
    
    # Extract sections
    sections = {}
    current_section = 'Full Text'
    section_text = []
    
    for line in html.split('\n'):
        # Detect section headers
        sec_match = re.search(r'<h[23][^>]*>(.*?)</h[23]>', line, re.I)
        if sec_match:
            if section_text:
                sections[current_section] = '\n'.join(section_text)
            current_section = re.sub(r'<[^>]+>', '', sec_match.group(1)).strip()
            section_text = []
            continue
        
        # Clean text
        clean = re.sub(r'<[^>]+>', ' ', line)
        clean = re.sub(r'\s+', ' ', clean).strip()
        if clean and len(clean) > 30:
            section_text.append(clean)
    
    if section_text:
        sections[current_section] = '\n'.join(section_text)
    
    return sections if len(sections) > 1 else None

def get_papers_without_fulltext():
    """获取所有无全文的论文"""
    papers = []
    for fname in sorted(os.listdir(CONCEPTS_DIR)):
        if not fname.endswith('.md'): continue
        path = os.path.join(CONCEPTS_DIR, fname)
        slug = fname.replace('.md', '')
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read(10000)
        except: continue
        
        # Check for fulltext
        has_pdf = bool(re.search(r'\*\*来源类型\*\*:\s*PDF全文', content))
        has_pmc = bool(re.search(r'(pmcid:|PMC全文|全文\s*\(PMC\))', content, re.I))
        if has_pdf or has_pmc:
            continue
        
        doi = ''
        dm = re.search(r'doi:\s*(10\.\d{4,}/[^\s\n]+)', content, re.I)
        if dm: doi = dm.group(1).rstrip('/')
        if not doi:
            continue
        
        title = ''
        tm = re.search(r'^# (.+)$', content, re.M)
        if tm: title = tm.group(1)[:120]
        
        pmid = ''
        pim = re.search(r'pmid:\s*"?(\d+)"?', content, re.I)
        if pim: pmid = pim.group(1)
        
        papers.append({
            'slug': slug, 'doi': doi, 'title': title, 'pmid': pmid, 'path': path
        })
    
    return papers

def main():
    papers = get_papers_without_fulltext()
    print(f"Papers without fulltext: {len(papers)}")
    
    # Step 1: Check OA status via Semantic Scholar + Europe PMC
    oa_papers = []
    checked = 0
    oa_count = 0
    
    for p in papers:
        checked += 1
        
        # Try Semantic Scholar first
        ss = check_semantic_scholar(p['doi'])
        ep = check_europe_pmc(p['doi'])
        
        is_oa = False
        pmcid = ''
        pdf_url = ''
        
        if ss and ss['is_oa']:
            is_oa = True
            pdf_url = ss['pdf_url']
            if ss['pmid'] and not p['pmid']:
                p['pmid'] = ss['pmid']
        
        if ep:
            if ep['is_oa']:
                is_oa = True
            if ep['pmcid']:
                pmcid = ep['pmcid']
            if not p['pmid']:
                # Europe PMC might have PMID too
                pass
        
        if is_oa:
            oa_count += 1
            oa_papers.append({**p, 'pmcid': pmcid, 'pdf_url': pdf_url})
        
        if checked % 50 == 0:
            print(f"  Checked {checked}/{len(papers)}, OA found: {oa_count}")
    
    print(f"\n=== OA Status Check Complete ===")
    print(f"Total checked: {checked}")
    print(f"Open Access: {oa_count} ({100*oa_count//checked if checked else 0}%)")
    print(f"Paywalled/Unknown: {checked - oa_count}")
    
    # Step 2: Try to download full text for OA papers
    downloaded = 0
    for i, p in enumerate(oa_papers):
        slug = p['slug']
        path = p['path']
        sections = None
        
        # Try PMC download
        if p['pmcid']:
            sections = download_pmc_fulltext(p['pmcid'])
        
        if sections:
            # Found full text - update concept page
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Build full text section
            ft_sections = []
            for sec_name, sec_text in sections.items():
                ft_sections.append(f'### {sec_name}\n{sec_text[:2000]}')
            ft_content = '\n\n'.join(ft_sections)
            
            fulltext_block = f"""
## PMC 全文

**来源**: PMC {p['pmcid']}
**下载日期**: {TODAY}

{ft_content}
"""
            # Add after ## 摘要 or before ## 深度提炼
            if '## 摘要' in content:
                parts = content.split('## 深度提炼')
                if len(parts) == 2:
                    content = parts[0] + fulltext_block + '\n## 深度提炼' + parts[1]
                else:
                    content += fulltext_block
            else:
                content += fulltext_block
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            downloaded += 1
            
            if downloaded % 10 == 0:
                print(f"  Downloaded {downloaded}...")
        
        time.sleep(0.3)
    
    # Step 3: Save OA list
    oa_csv = os.path.join(BASE, 'reports', 'oa_papers_for_download.csv')
    os.makedirs(os.path.dirname(oa_csv), exist_ok=True)
    with open(oa_csv, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'doi', 'pmid', 'pmcid', 'pdf_url'])
        writer.writeheader()
        for p in oa_papers:
            writer.writerow({k: p.get(k, '') for k in ['title', 'doi', 'pmid', 'pmcid', 'pdf_url']})
    
    print(f"\n=== DONE ===")
    print(f"OA papers identified: {oa_count}")
    print(f"Full text downloaded (PMC): {downloaded}")
    print(f"Remaining (OA but no PMC): {oa_count - downloaded}")
    print(f"OA list: {oa_csv}")

if __name__ == '__main__':
    main()
