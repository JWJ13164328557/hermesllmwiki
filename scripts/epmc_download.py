#!/usr/bin/env python3
"""Europe PMC 批量下载 OA 全文"""
import os, re, json, subprocess, time, sys

BASE = '/mnt/g/hermes_obsidian/hermes'
CONCEPTS_DIR = os.path.join(BASE, 'concepts', 'papers')

def curl(url):
    try:
        r = subprocess.run(['curl', '-sL', '--connect-timeout', '8', '--max-time', '20', url],
                          capture_output=True, text=True, timeout=25)
        return r.stdout if r.returncode == 0 and r.stdout.strip() else None
    except: return None

def download_pmc(pmcid):
    url = f'https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/?report=classic'
    html = curl(url)
    if not html: return None
    sections = {}
    cur = ''
    lines = []
    for line in html.split('\n'):
        m = re.search(r'<h[234][^>]*>(.+?)</h[234]>', line, re.I)
        if m:
            if lines and cur:
                sections[cur] = '\n'.join(lines[-40:])
            cur = re.sub(r'<[^>]+>', '', m.group(1)).strip()
            lines = []
            continue
        clean = re.sub(r'<[^>]+>', ' ', line)
        clean = re.sub(r'&[a-z]+;', ' ', clean)
        clean = re.sub(r'\s+', ' ', clean).strip()
        if clean and len(clean) > 20:
            lines.append(clean)
    if lines and cur:
        sections[cur] = '\n'.join(lines[-40:])
    return sections if len(sections) >= 2 else None

# Get papers
papers = []
for fname in sorted(os.listdir(CONCEPTS_DIR)):
    if not fname.endswith('.md'): continue
    path = os.path.join(CONCEPTS_DIR, fname)
    slug = fname.replace('.md', '')
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read(8000)
    except: continue
    if re.search(r'\*\*来源类型\*\*:\s*PDF全文', content): continue
    if re.search(r'PMC全文|PMC ID|pmcid:', content, re.I): continue
    dm = re.search(r'doi:\s*(10\.\d{4,}/[^\s\n]+)', content, re.I)
    if not dm: continue
    papers.append({'slug': slug, 'doi': dm.group(1).rstrip('/'), 'path': path})

print(f"Papers: {len(papers)}", flush=True)

checked = oa_found = downloaded = paywall = 0
for i, p in enumerate(papers):
    raw = curl(f'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:{p["doi"]}&format=json&resultType=core')
    checked += 1
    if not raw: continue
    try:
        r = json.loads(raw).get('resultList', {}).get('result', [])
        if not r: continue
        r = r[0]
    except: continue
    
    if r.get('isOpenAccess') != 'Y' or not r.get('pmcid'):
        paywall += 1
        continue
    oa_found += 1
    
    sections = download_pmc(r['pmcid'])
    if not sections:
        continue
    
    with open(p['path'], 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Build PMC section - just key sections
    ft_parts = []
    for want in ['Abstract', 'Introduction', 'Results', 'Discussion', 'Conclusion']:
        for k, v in sections.items():
            if want.lower() in k.lower():
                ft_parts.append(f'### {k}\n{v[:1500]}')
                break
    if not ft_parts:
        for k, v in list(sections.items())[:3]:
            ft_parts.append(f'### {k}\n{v[:1000]}')
    
    block = f"""
## PMC 全文

**PMC ID**: {r['pmcid']}

{chr(10).join(ft_parts)}
"""
    if '## 深度提炼' in content:
        content = content.split('## 深度提炼', 1)
        content = content[0] + block + '\n## 深度提炼' + content[1]
    else:
        content = content.rstrip() + '\n' + block
    
    with open(p['path'], 'w', encoding='utf-8') as f:
        f.write(content)
    downloaded += 1
    
    if checked % 25 == 0:
        print(f"  [{checked}/{len(papers)}] OA:{oa_found} DL:{downloaded} PW:{paywall}", flush=True)
    time.sleep(0.25)

print(f"\n=== DONE: checked={checked} OA={oa_found} DL={downloaded} PW={paywall} ===")
