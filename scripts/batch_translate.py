#!/usr/bin/env python3
"""批量翻译英文标题为中文，并更新concept pages"""
import os, re, time

base = '/mnt/g/hermes_obsidian/hermes'

# Read titles needing translation
with open(f'{base}/titles_to_translate.txt','r',encoding='utf-8') as f:
    all_titles = [line.strip().split('|||') for line in f if '|||' in line]

# Only process ones not yet translated
to_translate = []
for slug, title in all_titles:
    found = False
    for fname in os.listdir(f'{base}/concepts'):
        if fname.replace('.md','') == slug:
            with open(f'{base}/concepts/{fname}','r',encoding='utf-8') as f:
                c = f.read()
            # Check if already has Chinese heading
            first_line = c.split('\n')[0]
            if '---' in first_line:
                body = c.split('---\n')[-1]
                first_content = body.split('\n')[0]
            else:
                first_content = first_line
            if re.search(r'[\u4e00-\u9fff]{3,}', first_content):
                found = True
            break
    if not found:
        to_translate.append((slug, title))

print(f"Remaining to translate: {len(to_translate)}")

if len(to_translate) == 0:
    print("All done!")
    exit()

try:
    from deep_translator import GoogleTranslator
    translator = GoogleTranslator(source='en', target='zh-CN')
    translated = 0
    
    for slug, title in to_translate:
        try:
            zh = translator.translate(title[:150])
            if not zh or len(zh) < 2: continue
            
            # Update concept page
            for fname in os.listdir(f'{base}/concepts'):
                if fname.replace('.md','') == slug:
                    path = f'{base}/concepts/{fname}'
                    with open(path,'r',encoding='utf-8') as f: c = f.read()
                    
                    # Replace English heading with Chinese
                    lines = c.split('\n')
                    in_body = False
                    new_lines = []
                    for line in lines:
                        if line.startswith('# ') and not in_body:
                            new_lines.append(f'# {zh}')
                            in_body = True
                        else:
                            new_lines.append(line)
                    
                    with open(path,'w',encoding='utf-8') as f:
                        f.write('\n'.join(new_lines))
                    translated += 1
                    break
            
            time.sleep(0.05)
            if translated % 20 == 0:
                print(f'  {translated}/{len(to_translate)}')
        except:
            pass
    
    print(f'Translated: {translated}')
    
except ImportError:
    # Fallback: use free translate API
    import urllib.parse, json, subprocess
    translated = 0
    for slug, title in to_translate:
        try:
            encoded = urllib.parse.quote(title[:100])
            proc = subprocess.run(['curl','-s','--connect-timeout','5',
                f'https://api.mymemory.translated.net/get?q={encoded}&langpair=en|zh-CN'],
                capture_output=True, text=True, timeout=10)
            data = json.loads(proc.stdout)
            zh = data.get('responseData',{}).get('translatedText','')
            if zh and len(zh) > 2:
                for fname in os.listdir(f'{base}/concepts'):
                    if fname.replace('.md','') == slug:
                        path = f'{base}/concepts/{fname}'
                        with open(path,'r',encoding='utf-8') as f: c = f.read()
                        lines = c.split('\n')
                        new_lines = []
                        in_body = False
                        for line in lines:
                            if line.startswith('# ') and not in_body:
                                new_lines.append(f'# {zh}')
                                in_body = True
                            else:
                                new_lines.append(line)
                        with open(path,'w',encoding='utf-8') as f:
                            f.write('\n'.join(new_lines))
                        translated += 1
                        break
                time.sleep(0.1)
        except: pass
        if translated % 20 == 0:
            print(f'  {translated}/{len(to_translate)}')
    
    print(f'Translated (fallback): {translated}')
