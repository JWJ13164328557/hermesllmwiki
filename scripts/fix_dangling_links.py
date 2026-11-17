#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fix_dangling_links.py — 修复 [[wikilink]] 悬空引用（2026-11-02）

背景
----
级联删除非植物概念页后，实体页/关系表里的 [[evidence-id]] 变成死链；
历史上还有一批 [[entity]] 指向从未创建过的实体页。两者处理方式不同：

  * evidence / concept 的 id（形如 xxx-f3 或 10-xxxx-...）→ 直接删掉这个 token，
    因为 id 本身没有可读语义，保留只是噪音；
  * 实体名（wrky33、pbrnsc …）→ 去掉方括号保留文字，信息不丢。

表格行（relationships/）在删 token 后若「Source」列空了，整行删除。

用法
----
    python3 scripts/fix_dangling_links.py            # dry-run，只报告
    python3 scripts/fix_dangling_links.py --apply    # 真正写盘
"""
import os, re, glob, argparse, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb_paths import BASE

LINK_RE = re.compile(r'\[\[([^\]\|#]+)((?:\|[^\]]*)?)\]\]')
ID_LIKE = re.compile(r'^(?:.*-f\d+|(?:cr|ms|dpdf|pdf|ref|daily|b\d)-.*|\d{2}-\d{4}-.*)$')


def build_index():
    """全库可解析目标集合。

    必须排除 _review/、archive/、.trash/：这些是被隔离/归档的副本，
    曾是"隔离了却仍被判为有效目标"的漏报来源（2026-11-02 实测）。
    """
    idx = set()
    for p in glob.glob(f'{BASE}/**/*.md', recursive=True):
        rel = os.path.relpath(p, BASE).replace(os.sep, '/')
        if rel.startswith(('_review/', 'archive/', '.trash')):
            continue
        idx.add(os.path.basename(p)[:-3])
    return idx


def is_path_like(tok):
    """`sources/OsbHLH150水稻耐冷` 这类误抓的本地路径，没有修复价值，按死链丢弃。"""
    return '/' in tok or '\\' in tok


def is_id_like(tok):
    return bool(ID_LIKE.match(tok.strip()))


def is_citation_marker(tok):
    """PMC 全文里残留的 [[4],[5]] 引文标记：纯数字/逗号，不是 wikilink。"""
    return bool(re.match(r'^[\d,\s]+$', tok.strip()))


def fix_text(text, idx):
    """返回 (new_text, dropped_tokens, unwrapped_tokens)"""
    dropped, unwrapped = [], []

    def repl(m):
        tok = m.group(1).strip()
        if is_citation_marker(tok) or tok in idx:
            return m.group(0)
        if is_id_like(tok) or is_path_like(tok):
            dropped.append(tok)
            return '\x00'          # 占位，稍后清理分隔符
        unwrapped.append(tok)
        return tok

    new = LINK_RE.sub(repl, text)

    # 未闭合的 [[slug（行尾截断）单独处理
    def repl_eol(m):
        tok = m.group(1).strip()
        if not tok or is_citation_marker(tok):
            return m.group(0)
        if is_id_like(tok):
            dropped.append(tok)
            return '\x00'
        unwrapped.append(tok)
        return tok

    new = re.sub(r'\[\[([^\]\n|#]+)[ \t]*$', repl_eol, new, flags=re.M)
    if dropped:
        # 清理 token 删除后遗留的分隔符：", \x00" / "\x00, " / "| \x00" / "\x00 |"
        for _ in range(3):
            new = re.sub(r'[ \t]*\x00[ \t]*,[ \t]*', '', new)
            new = re.sub(r'[ \t]*,[ \t]*\x00[ \t]*', '', new)
            new = re.sub(r'\|[ \t]*\x00[ \t]*(?=\||$)', '', new, flags=re.M)
            new = re.sub(r'[ \t]*\x00', '', new)
        # 表格行：Source 列（最后一个 | 之后）为空 → 删整行
        out = []
        for line in new.split('\n'):
            if re.match(r'^\s*-\s*$', line):
                continue
            if line.startswith('|') and line.rstrip().endswith('|'):
                cells = [c.strip() for c in line.strip().strip('|').split('|')]
                if len(cells) >= 4 and not cells[-1]:
                    continue                      # 丢整行
            out.append(line)
        new = '\n'.join(out)
    new = new.replace('\x00', '')
    # 唯一引用被删后留下的空括号：学术写作里"无引用支撑"必须显式可见，
    # 直接留 （） 等于把缺陷藏起来（2026-11-02 实测踩到）。
    new = re.sub(r'（\s*[，,、;；\s]*\s*）', '（源待补）', new)
    new = re.sub(r'\(\s*[，,、;；\s]*\s*\)', '（源待补）', new)
    return new, dropped, unwrapped


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--show', type=int, default=12)
    args = ap.parse_args()

    idx = build_index()
    # 默认只处理内容目录：archive/（已隔离）、_review/（人工复核）、.trash 与
    # 根目录的说明文档（SKILL.md / SOP.md …）不属于知识图谱，一律不动。
    # synthesis/ 长期不在扫描范围，导致 31 条失效引用从未被报出（2026-11-02 修）
    SCOPE = ('concepts/', 'entities/', 'relationships/', 'themes/', 'evidence/',
             'synthesis/')
    tot_d = tot_u = files = 0
    details = []
    for p in sorted(glob.glob(f'{BASE}/**/*.md', recursive=True)):
        if '/.trash' in p or '/_review/' in p:
            continue
        try:
            txt = open(p, encoding='utf-8').read()
        except Exception:
            continue
        if '[[' not in txt:
            continue
        rel = os.path.relpath(p, BASE)
        if not rel.startswith(SCOPE):
            continue
        new, dropped, unwrapped = fix_text(txt, idx)
        if not dropped and not unwrapped:
            continue
        files += 1
        tot_d += len(dropped)
        tot_u += len(unwrapped)
        details.append((rel, len(dropped), len(unwrapped)))
        if args.apply and new != txt:
            open(p, 'w', encoding='utf-8').write(new)

    print(f'{"APPLIED" if args.apply else "DRY-RUN"}: 受影响文件 {files} | 删除死链 {tot_d} | 解绑实体链 {tot_u}')
    for rel, d, u in details[:args.show]:
        print(f'  {rel:60s} drop={d:3d} unwrap={u:3d}')
    if len(details) > args.show:
        print(f'  ... 其余 {len(details)-args.show} 个文件')
    return 0


if __name__ == '__main__':
    sys.exit(main())
