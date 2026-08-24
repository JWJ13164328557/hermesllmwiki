#!/usr/bin/env python3
"""批量翻译代谢论文标题为中文，并建立语义交叉引用
使用 MyMemory API (免费) 和内置回退"""
import os, re, json, subprocess, time
from pathlib import Path

CONCEPTS_DIR = '/mnt/g/hermes_obsidian/hermes/concepts/papers'
BASE = '/mnt/g/hermes_obsidian/hermes'

def translate_mymemory(text):
    """MyMemory API 翻译"""
    try:
        import urllib.parse, urllib.request
        encoded = urllib.parse.quote(text[:500])
        url = f'https://api.mymemory.translated.net/get?q={encoded}&langpair=en|zh'
        r = subprocess.run(['curl', '-sL', '--connect-timeout', '10', url],
                          capture_output=True, text=True, timeout=15)
        if r.returncode != 0: return None
        data = json.loads(r.stdout)
        result = data.get('responseData', {}).get('translatedText', '')
        if result and len(result) > 5:
            return result
    except: pass
    return None

def simple_translate(title):
    """Simple keyword-based Chinese translation as fallback"""
    replacements = [
        ('transcriptom', '转录组'),
        ('metabolom', '代谢组'),
        ('genome', '基因组'),
        ('proteom', '蛋白质组'),
        ('analysis', '分析'),
        ('reveals', '揭示'),
        ('reveal', '揭示'),
        ('regulates', '调控'),
        ('regulation', '调控'),
        ('biosynthesis', '生物合成'),
        ('identification', '鉴定'),
        ('characterization', '鉴定'),
        ('integration', '整合'),
        ('integrated', '整合'),
        ('comprehensive', '全面'),
        ('comparative', '比较'),
        ('functional', '功能'),
        ('molecular', '分子'),
        ('mechanism', '机制'),
        ('pathway', '途径'),
        ('accumulation', '积累'),
        ('profile', '图谱'),
        ('profiling', '分析'),
        ('insight', '深入'),
        ('insights', '深入'),
        ('role', '作用'),
        ('response', '响应'),
        ('stress', '胁迫'),
        ('development', '发育'),
        ('expression', '表达'),
        ('novel', '新的'),
        ('key', '关键'),
        ('underlying', '潜在'),
        ('associated', '相关的'),
        ('involved', '参与的'),
        ('mediated', '介导的'),
        ('through', '通过'),
        ('during', '过程中'),
        ('high-quality', '高质量'),
        ('assembly', '组装'),
        ('sequencing', '测序'),
        ('network', '网络'),
        ('module', '模块'),
        ('target', '靶标'),
        ('promotes', '促进'),
        ('inhibits', '抑制'),
        ('induces', '诱导'),
        ('activates', '激活'),
        ('represses', '抑制'),
        ('modulates', '调节'),
        ('controls', '控制'),
        ('provides', '提供了'),
        ('elucidat', '阐明'),
        ('generation', '生成'),
        ('evolution', '进化'),
        ('diversity', '多样性'),
        ('dynamic', '动态'),
        ('landscape', '全景'),
        ('dissection', '解析'),
        ('unveil', '揭示'),
        ('decipher', '解析'),
        ('decoding', '解析'),
        ('based on', '基于'),
        ('into', ''),
        ('and', '和'),
        ('of', '的'),
        ('in', '中'),
        ('to', ''),
        ('from', ''),
        ('the', ''),
        ('a ', ''),
        (' an ', ''),
        ('for ', ''),
        ('with ', ''),
    ]
    result = title
    for en, zh in replacements:
        result = re.sub(r'\b' + en + r'\b', zh, result, flags=re.I)
    # Clean up
    result = re.sub(r'\s+', ' ', result).strip()
    result = re.sub(r'</?[a-z]+>', '', result)  # strip XML tags
    return result

def main():
    # Find metabolism pages created today
    today_files = []
    for fname in os.listdir(CONCEPTS_DIR):
        if not fname.endswith('.md'): continue
        path = os.path.join(CONCEPTS_DIR, fname)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read(2000)
            # Check if it's a metabolism paper with English title
            if 'metabolism' in content.lower() and '# ' in content:
                title_match = re.search(r'^# (.+)$', content, re.M)
                if title_match:
                    title = title_match.group(1)
                    # Skip if already has Chinese title (contains CJK)
                    if not re.search(r'[\u4e00-\u9fff]', title):
                        today_files.append((fname, title))
        except: pass
    
    print(f"Files to translate: {len(today_files)}")
    
    translated = 0
    for fname, en_title in today_files:
        # Try MyMemory first
        zh = translate_mymemory(en_title[:200])
        if not zh:
            zh = simple_translate(en_title)
        
        if zh and len(zh) > 3:
            # Update the concept page with Chinese title
            path = os.path.join(CONCEPTS_DIR, fname)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Add Chinese title as heading alias
            new_heading = f'# {zh}\n\n> {en_title}\n\n'
            content = re.sub(r'^# .+$\n\n', new_heading, content, count=1)
            
            # Add/update aliases in frontmatter
            if 'aliases:' in content:
                if zh not in content:
                    content = content.replace('aliases:', f'aliases: ["{zh}"]\naliases_extra:')
                    content = content.replace('aliases_extra:\n', '')
            else:
                # Add aliases before ---
                content = content.replace('\n---\n', f'\naliases: ["{zh}"]\n---\n', 1)
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            translated += 1
            
            if translated % 20 == 0:
                print(f"  Translated {translated}...")
        
        time.sleep(0.3)
    
    print(f"\nTranslated: {translated}/{len(today_files)}")

if __name__ == '__main__':
    main()
