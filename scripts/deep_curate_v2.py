#!/usr/bin/env python3
"""QUICK FIX: inline extraction, no import of deep_curate_all"""
import os, re, sys, subprocess

BASE = '/mnt/g/hermes_obsidian/hermes'
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
        doi_to_concept[dm.group(1).rstrip('/')] = path

# Find all PDFs
pdf_files = []
for root, dirs, files in os.walk(RAW_DIR):
    for f in files:
        if f.endswith('.pdf'):
            pdf_files.append(os.path.join(root, f))
print(f"PDFs: {len(pdf_files)}, DOI→concept: {len(doi_to_concept)}")

# Match PDFs by filename-DOI
def doi_from_fname(fname):
    doi = fname.rsplit('.', 1)[0].replace('_', '/')
    return doi if re.match(r'10\.\d{4,}/', doi) else None

matched = []
for pdf_path in pdf_files:
    doi = doi_from_fname(os.path.basename(pdf_path))
    if doi and doi in doi_to_concept:
        matched.append((pdf_path, doi))

# Also match by PDF content extraction
for pdf_path in pdf_files:
    basename = os.path.basename(pdf_path)
    doi = doi_from_fname(basename)
    if doi and doi in doi_to_concept:
        continue  # already matched
    try:
        import fitz
        doc = fitz.open(pdf_path)
        for page_num in range(min(3, len(doc))):
            m = re.search(r'10\.\d{4,}/[^\s"\n\r\t]+', doc[page_num].get_text())
            if m:
                doi = m.group(0).rstrip('.,;:)')
                if doi in doi_to_concept:
                    matched.append((pdf_path, doi))
                    break
        doc.close()
    except:
        pass

print(f"Matched: {len(matched)}")

# Deep curate
species_patterns = [(r'\bArabidopsis\s+thaliana\b', 'Arabidopsis thaliana')]  # short version
curated = 0
for pdf_path, doi in matched:
    # Extract fulltext
    fulltext = ''
    try:
        import fitz
        doc = fitz.open(pdf_path)
        text = ''
        for page in doc[:15]:
            text += page.get_text()
        doc.close()
        if len(text.strip()) > 200:
            fulltext = text[:50000]
    except Exception as e:
        print(f"  FITZ ERROR on {os.path.basename(pdf_path)[:50]}: {e}")
    
    if not fulltext:
        if curated < 3:
            print(f"  [NO TEXT] {os.path.basename(pdf_path)[:50]}")
        curated += 0  # still count but don't skip
        continue
    
    # Quick species extraction
    species = []
    for pat, name in species_patterns:
        if re.search(pat, fulltext, re.I):
            species.append(name)
    
    if curated < 3:
        print(f"  [OK] {os.path.basename(pdf_path)[:50]}: {len(fulltext)} chars, species={species}")
    curated += 1

print(f"\nDONE: extracted={curated}/{len(matched)}")
