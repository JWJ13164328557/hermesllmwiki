#!/usr/bin/env python3
"""DEBUG: test extract_fulltext on first 10 matched PDFs"""
import os, re, sys

BASE = '/mnt/g/hermes_obsidian/hermes'
sys.path.insert(0, os.path.join(BASE, 'scripts'))
from deep_curate_all import (
    extract_doi_from_filename, extract_doi_from_pdf, extract_fulltext
)

CONCEPTS_DIR = os.path.join(BASE, 'concepts', 'papers')
RAW_DIR = os.path.join(BASE, 'raw')

# Build DOI→concept
doi_to_concept = {}
for fname in os.listdir(CONCEPTS_DIR):
    if not fname.endswith('.md'): continue
    path = os.path.join(CONCEPTS_DIR, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read(3000)
    dm = re.search(r'doi:\s*(10\.\d{4,}/[^\s\n]+)', content, re.I)
    if dm:
        doi = dm.group(1).rstrip('/')
        doi_to_concept[doi] = path

# Find PDFs and match
pdf_files = []
for root, dirs, files in os.walk(RAW_DIR):
    for f in files:
        if f.endswith('.pdf'):
            pdf_files.append(os.path.join(root, f))

print(f"PDFs: {len(pdf_files)}, DOI→concept: {len(doi_to_concept)}")

count = 0
for pdf_path in pdf_files:
    basename = os.path.basename(pdf_path)
    doi = extract_doi_from_filename(basename) or extract_doi_from_pdf(pdf_path)
    if not doi or doi not in doi_to_concept:
        continue
    
    if count >= 10:
        break
    
    fulltext = extract_fulltext(pdf_path)
    exists = os.path.exists(pdf_path)
    fsize = os.path.getsize(pdf_path)
    print(f"[{count}] {basename[:50]} | exists={exists} | size={fsize} | text_len={len(fulltext)}")
    
    # Also test inline
    text2 = ''
    try:
        import fitz
        doc = fitz.open(pdf_path)
        for page in doc[:15]:
            text2 += page.get_text()
        doc.close()
    except Exception as e:
        text2 = f'ERROR: {e}'
    
    print(f"       inline fitz: {len(text2) if isinstance(text2, str) else text2}")
    count += 1
