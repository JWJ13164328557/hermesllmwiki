#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""triage_identifier_review.py — 把"标识符待人工复核清单"变成可执行的分类报告。

背景
----
verify_identifiers.py 用"页面标题 ≈ 记录标题"做相似度判定，阈值 0.75。
它把两类东西混在同一个 mismatch 桶里：
  * 真正绑错了 DOI/PMID 的页面；
  * 只是标题被截断 / 未解码 HTML 实体 / 被翻译成中文的**同一篇**文献。
后者若当成错误去"修"，反而会把正确的 DOI 改坏。所以这里做机械三分：

  A. 归一化缺陷（截断 / HTML 实体 / 非拉丁语言 / 撤稿声明）→ 不该改 DOI
  B. 疑似真错配（标题词元与记录词元几乎不重叠）→ 需人工定值
  C. 表述差异（重叠高但相似度低于阈值）→ 阈值问题

输出：_review/ids_review.md（分类清单 + 处置建议），不写任何概念页。
"""
import argparse
import os
import re
import sys

from kb_paths import BASE

ENTITY_FIX = {'&amp;': '&', '&lt;': '<', '&gt;': '>', '&nbsp;': ' ',
              '&quot;': '"', '&#39;': "'"}


def norm(s):
    s = (s or '').lower()
    for k, v in ENTITY_FIX.items():
        s = s.replace(k, v)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = re.sub(r'[^0-9a-z\u4e00-\u9fff]+', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


def has_entity(s):
    return bool(re.search(r'&(amp|lt|gt|nbsp|quot|#39);|<[a-z]+>', s or '', re.I))


def has_cjk(s):
    return bool(re.search(r'[\u4e00-\u9fff]', s or ''))


def has_nonlatin(s):
    return bool(re.search(r'[^\x00-\x7f]', s or ''))


def tokens(s):
    return set(t for t in norm(s).split() if len(t) > 2)


def jaccard(a, b):
    ta, tb = tokens(a), tokens(b)
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / float(len(ta | tb))


def classify(page_title, rec_title):
    p = (page_title or '').strip()
    r = (rec_title or '').strip()
    if not r:
        return 'D', '抓取侧没有可比对的记录（多为无 PMCID/未被索引的页面），无法自动判定'
    if re.search(r'statement of removal|retraction|withdraw', r, re.I):
        return 'A', '记录为撤稿/移除声明，原文已不可引用；页面应改绑或归档'
    if has_entity(p) or has_entity(r):
        return 'A', 'HTML 实体/标签未解码导致语义比对失败，不是 DOI 错误'
    if has_cjk(p) or has_nonlatin(r) or has_nonlatin(p):
        return 'A', '语言不同（原文/译文），同一文献；不应据相似度改 DOI'
    np, nr = norm(p), norm(r)
    if np and nr and (nr.startswith(np) or np.startswith(nr)):
        return 'A', '标题被截断（一方是另一方的前缀），不是 DOI 错误'
    j = jaccard(p, r)
    if j < 0.35:
        return 'B', '词元重叠 %.2f：标题与记录几乎无关，疑似真错配' % j
    return 'C', '词元重叠 %.2f：同一文献的不同表述，属阈值问题' % j


def parse(path):
    bt = chr(96)
    items = []
    cur = None
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            m = re.match(r'^## (\S+) \((\d+)\)', line)
            if m:
                continue
            if line.startswith('- ' + bt):
                cur = {'id': line[3:].strip(bt + ' '), 'page': '', 'doi': '',
                       'pmid': '', 'rec': '', 'proposed': ''}
                items.append(cur)
                continue
            if cur is None:
                continue
            s = line.strip()
            if s.startswith('- 页面标题:'):
                cur['page'] = s.split(':', 1)[1].strip()
            elif s.startswith('- 现 DOI:'):
                body = s.split(':', 1)[1].strip()
                parts = body.split('/ PMID:')
                cur['doi'] = parts[0].strip().strip(bt + ' ')
                if len(parts) > 1:
                    cur['pmid'] = parts[1].strip().strip(bt + ' ')
            elif s.startswith('- proposed_doi:'):
                cur['proposed'] = s.split(':', 1)[1].strip()
            elif s.startswith('- doi_rec_title:'):
                cur['rec'] = s.split(':', 1)[1].strip()
            elif s.startswith('- pmid_rec_title:') and not cur['rec']:
                cur['rec'] = s.split(':', 1)[1].strip()
    return items


def main():
    ap = argparse.ArgumentParser(description='identifier review triage')
    ap.add_argument('--input', default='/home/jiwj/review_ids.md')
    ap.add_argument('--output', default=os.path.join(BASE, '_review', 'ids_review.md'))
    args = ap.parse_args()

    items = parse(args.input)
    if not items:
        raise SystemExit('未解析到任何条目，检查输入格式：%s' % args.input)
    buckets = {'A': [], 'B': [], 'C': [], 'D': []}
    for it in items:
        code, why = classify(it['page'], it['rec'])
        it['code'], it['why'] = code, why
        buckets[code].append(it)

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, 'w', encoding='utf-8', newline='\n') as f:
        f.write('# 标识符复核清单（分类版）\n\n')
        f.write('输入：%s；共 %d 条：A 归一化缺陷 %d / B 疑似真错配 %d / '
                'C 表述差异 %d / D 无可比对记录 %d。\n\n'
                % (os.path.basename(args.input), len(items), len(buckets['A']),
                   len(buckets['B']), len(buckets['C']), len(buckets['D'])))
        f.write('> 处置原则：**A 类不改标识符**（修标题解码/补全或补 title_en）；\n'
                '> B 类必须人工用原始数据库定值后再改；C 类先修标题再重跑核验。\n\n')
        for code, title in (('B', 'B 疑似真错配（优先人工）'),
                            ('C', 'C 表述差异（先修标题）'),
                            ('A', 'A 归一化缺陷（不是 DOI 错误）'),
                            ('D', 'D 无可比对记录（不计入错配）')):
            f.write('## %s\n\n' % title)
            if not buckets[code]:
                f.write('_（无）_\n\n')
                continue
            for it in buckets[code]:
                f.write('- %s\n' % it['id'])
                if it['page']:
                    f.write('  - 页面标题：%s\n' % it['page'])
                if it['doi'] or it['pmid']:
                    f.write('  - 当前：DOI %s / PMID %s\n' % (it['doi'], it['pmid']))
                if it.get('proposed'):
                    f.write('  - 建议 DOI：%s（**未自动应用**）\n' % it['proposed'])
                if it['rec']:
                    f.write('  - 记录标题：%s\n' % it['rec'])
                f.write('  - 判定：%s\n' % it['why'])
            f.write('\n')
    print('写入 %s（A=%d B=%d C=%d D=%d）' % (args.output, len(buckets['A']),
                                              len(buckets['B']), len(buckets['C']),
                                              len(buckets['D'])))
    return 0


if __name__ == '__main__':
    sys.exit(main())
