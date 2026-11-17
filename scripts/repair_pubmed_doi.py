#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""用 PubMed 权威元数据修复被参考文献 DOI 覆盖的页面。

根因：2026-11-03 前 daily_update.parse_pubmed_article 用 .//ArticleId，
会递归到 ReferenceList，把最后一条参考文献的 DOI 写成文章 DOI。
本脚本按 PMID 重新 efetch，仅在标题与页面一致时替换 DOI/PMCID。

用法：
    python3 repair_pubmed_doi.py --dry-run
    python3 repair_pubmed_doi.py --apply
"""
import argparse
import glob
import os
import re
import subprocess
import sys
import time
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb_paths import BASE  # noqa: E402
import daily_update as du  # noqa: E402

EFETCH = ('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'
          '?db=pubmed&id=%s&retmode=xml')
AUDIT = os.path.join(BASE, '_review', 'pubmed_doi_repair.tsv')


def _norm(s):
    return re.sub(r'[^a-z0-9]+', ' ', (s or '').lower()).strip()


def _similar(a, b):
    ta = set(_norm(a).split())
    tb = set(_norm(b).split())
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / float(len(ta | tb))


def _pages():
    for sub in ('concepts/papers', 'concepts'):
        for f in glob.glob(os.path.join(BASE, sub, '*.md')):
            s = open(f, encoding='utf-8', errors='ignore').read()
            m = re.search(r'^pmid:\s*(\d+)', s, re.M)
            if m:
                yield f, m.group(1), s


def _fetch(ids):
    url = EFETCH % ','.join(ids)
    proc = subprocess.run(['curl', '-sL', '--connect-timeout', '15',
                           '--max-time', '90', url],
                          capture_output=True, text=True, timeout=120)
    if not proc.stdout.strip():
        return {}
    root = ET.fromstring(proc.stdout.encode('utf-8', 'replace'))
    out = {}
    for art in root.findall('.//PubmedArticle'):
        pmid = (art.findtext('./MedlineCitation/PMID') or '').strip()
        if not pmid:
            continue
        raw = '<PubmedArticleSet>' + ET.tostring(art, encoding='unicode') + '</PubmedArticleSet>'
        rec = du.parse_pubmed_article(raw, pmid)
        if rec:
            out[pmid] = rec
    return out


def _set_field(text, key, value):
    """在 frontmatter 中设置字段；不存在则插入。"""
    m = re.match(r'^---\n(.*?)\n---', text, re.S)
    if not m or not value:
        return text
    head = m.group(1)
    if re.search(r'^%s:' % re.escape(key), head, re.M):
        head = re.sub(r'^%s:.*$' % re.escape(key),
                      '%s: %s' % (key, value), head, count=1, flags=re.M)
    elif re.search(r'^doi:', head, re.M):
        head = re.sub(r'^(doi:.*)$', r'\1\n%s: %s' % (key, value),
                      head, count=1, flags=re.M)
    elif re.search(r'^created:', head, re.M):
        head = re.sub(r'^(created:.*)$', r'\1\n%s: %s' % (key, value),
                      head, count=1, flags=re.M)
    else:
        head += '\n%s: %s' % (key, value)
    return text[:m.start(1)] + head + text[m.end(1):]


def _replace_doi(text, old, new):
    if not old or not new or old == new:
        return text
    return text.replace(old, new)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--limit', type=int, default=0)
    ap.add_argument('--suspect-only', action='store_true',
                    help='只处理 DOI 内年份与页面年份相差 >1 的页面')
    args = ap.parse_args()
    dry = not args.apply

    pages = list(_pages())
    if args.suspect_only:
        keep = []
        for path, pmid, text in pages:
            dm = re.search(r'^doi:\s*(\S+)', text, re.M)
            ym = re.search(r'\*\*期刊\*\*:.*?\((\d{4})\)', text)
            if not dm or not ym:
                continue
            y = int(ym.group(1))
            yrs = [int(x) for x in re.findall(r'(19\d{2}|20\d{2})', dm.group(1))]
            if yrs and all(abs(y - x) > 1 for x in yrs):
                keep.append((path, pmid, text))
        pages = keep
    by_pmid = {}
    for path, pmid, text in pages:
        by_pmid.setdefault(pmid, []).append((path, text))
    pmids = sorted(by_pmid)
    if args.limit:
        pmids = pmids[:args.limit]

    stats = {'checked': 0, 'missing': 0, 'title_mismatch': 0,
             'doi_changed': 0, 'pmcid_changed': 0, 'unchanged': 0, 'error': 0}
    rows = []
    for i in range(0, len(pmids), 40):
        chunk = pmids[i:i + 40]
        try:
            recs = _fetch(chunk)
        except Exception as exc:
            stats['error'] += len(chunk)
            print('fetch error: %s' % exc, file=sys.stderr)
            time.sleep(2)
            continue
        for pmid in chunk:
            rec = recs.get(pmid)
            if not rec:
                stats['missing'] += 1
                continue
            for path, text in by_pmid[pmid]:
                stats['checked'] += 1
                cur_title = re.search(r'^title:\s*"?(.*?)"?\s*$', text, re.M)
                cur_title = cur_title.group(1) if cur_title else ''
                if _similar(cur_title, rec.get('title', '')) < 0.45:
                    stats['title_mismatch'] += 1
                    rows.append((pmid, os.path.basename(path), 'TITLE_MISMATCH',
                                 cur_title[:80], rec.get('title', '')[:80], ''))
                    continue
                cur_doi = re.search(r'^doi:\s*(\S+)', text, re.M)
                cur_doi = cur_doi.group(1) if cur_doi else ''
                new_doi = (rec.get('doi') or '').strip()
                cur_pmc = re.search(r'^pmcid:\s*(\S+)', text, re.M)
                cur_pmc = cur_pmc.group(1) if cur_pmc else ''
                new_pmc = (rec.get('pmcid') or '').strip()
                if not new_doi:
                    stats['missing'] += 1
                    continue
                if cur_doi == new_doi and (not new_pmc or cur_pmc == new_pmc):
                    stats['unchanged'] += 1
                    continue
                label = 'DOI_CHANGE' if new_doi != cur_doi else 'PMCID_CHANGE'
                rows.append((pmid, os.path.basename(path), label,
                             cur_doi, new_doi, cur_pmc + '->' + new_pmc))
                if new_doi != cur_doi:
                    stats['doi_changed'] += 1
                    text = _replace_doi(text, cur_doi, new_doi)
                    text = _set_field(text, 'doi', new_doi)
                if new_pmc and cur_pmc != new_pmc:
                    stats['pmcid_changed'] += 1
                    text = _replace_doi(text, cur_pmc, new_pmc)
                    text = _set_field(text, 'pmcid', new_pmc)
                if not dry:
                    with open(path, 'w', encoding='utf-8') as fh:
                        fh.write(text)
        time.sleep(0.4)

    os.makedirs(os.path.dirname(AUDIT), exist_ok=True)
    if not dry and rows:
        with open(AUDIT, 'a', encoding='utf-8') as fh:
            for r in rows:
                fh.write('\t'.join(str(x) for x in r) + '\n')

    print('\n=== PubMed DOI 修复 (%s) ===' % ('DRY-RUN' if dry else 'APPLY'))
    for k, v in stats.items():
        print('  %-14s %d' % (k, v))
    print('  审计: %s' % AUDIT)
    return 0


if __name__ == '__main__':
    sys.exit(main())
