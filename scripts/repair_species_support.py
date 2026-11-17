#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按“论文文本是否支持该物种”清理物种标注（2026-11-02）。

为什么需要
----------
1. `species_patterns.py` 曾用 `\\bfig\\b`（大小写不敏感）匹配 Ficus carica，
   PDF 图注 "Fig. 1" 全部命中；"orange" 也把颜色词计入 Citrus。上一轮只修了
   `primary_species`，`species:` 列表与概念页 `## 深度提炼` 里的 **物种** 行仍是脏的。
2. 早期写手把正文片段写进 frontmatter，出现
   `Ficus carica **方法**: transcriptomics (RNA-seq)` 这种非物种条目。

判定口径（可逐条复核，不做 LLM 推断）
------------------------------------
对一条“物种声明”S（证据页 species 列表项 / 深度提炼 **物种** 行），
取论文标题 + 正文摘要（**排除** `## 深度提炼` 块，防止自证循环）：
  * 用 species_patterns.SPECIES_PATTERNS 把 S 映射回其同义正则；
  * 正则命中 → 保留；未命中 → 删除；
  * 标题+摘要长度 < 300 字符（无摘要页）→ 无法判定，保持原样并计数。

默认 dry-run；`--apply` 写盘前自动 tar 备份。
"""
from __future__ import annotations

import argparse
import datetime
import os
import re
import subprocess
import sys

from kb_paths import BASE, CONCEPTS_DIR, EVIDENCE_DIR
from species_patterns import SPECIES_PATTERNS

GENERIC = ('Plant', 'Plant (unspecified)', '未识别', 'plant', '—', '')
PAT_BY_NAME = {name: pat for pat, name in SPECIES_PATTERNS}
NAME_ALIASES = {
    'Populus': 'Populus spp.', 'Citrus sinensis': 'Citrus spp.',
    'Citrus reticulata': 'Citrus spp.', 'Medicago sativa': 'Medicago spp.',
    'Medicago truncatula': 'Medicago spp.', 'Musa acuminata': 'Musa spp.',
    'Nicotiana benthamiana': 'Nicotiana tabacum',
}
COMMON_NAMES = frozenset("""
maize rice wheat soybean tomato tobacco cotton potato barley sorghum grape apple
citrus poplar alfalfa cassava sugarcane banana tea moss fern
""".split())
TAXON_RES = (
    re.compile(r"^[A-Z][a-zA-Z\-]+$"),
    re.compile(r"^[A-Z][a-zA-Z\-]+\s+[a-z][a-zA-Z\-]+$"),
    re.compile(r"^[A-Z][a-zA-Z\-]+\s+(?:spp\.|sp\.)$"),
    re.compile(r"^[A-Z][a-zA-Z\-]+\s+×\s*[a-z][a-zA-Z\-]+$"),
)
MIN_TEXT = 300
# 已知正则伪影（"Fig."/"orange" 误匹配）：无论论文类型，只要论文文本不支持就删。
ARTIFACT_SPECIES = frozenset(["Ficus carica", "Citrus spp.", "Citrus sinensis"])
# 综述/进展类论文本就覆盖多物种，不能按"摘要是否点名"删减物种表。
REVIEW_RE = re.compile(
    r"\b(review|advances?|progress|overview|perspective|prospects?|"
    r"current\s+understanding|recent\s+developments?|a\s+survey|"
    r"mechanisms?\s+and\s+applications?)\b", re.I)


def parse_list_field(content, key):
    m = re.search(r"^%s:\s*\[(.*?)\]" % re.escape(key), content, re.M | re.S)
    if m:
        return [x.strip().strip("\"'") for x in m.group(1).split(",") if x.strip()]
    m = re.search(r"^%s:\s*\n((?:[ \t]*-[ \t]*.+\n?)+)" % re.escape(key), content, re.M)
    if m:
        return [x.strip().lstrip("-").strip().strip("\"'")
                for x in m.group(1).splitlines() if x.strip()]
    return []


def str_field(content, key):
    m = re.search(r"^%s:\s*\"?(.*?)\"?\s*$" % re.escape(key), content, re.M)
    return m.group(1).strip() if m else ""


def paper_text(content):
    """标题 + 正文摘要；显式剔除 深度提炼 元数据块。"""
    title = str_field(content, "title")
    body = content.split("## 深度提炼")[0]
    m = re.search(r"^##\s*(?:摘要|Abstract)\s*\n(.+?)(?=\n##|\Z)", body, re.S | re.M)
    abstract = m.group(1) if m else ""
    return title + " " + abstract


def is_wellformed(x):
    x = (x or "").strip()
    if not x:
        return False
    if x in GENERIC or x.lower() in COMMON_NAMES:
        return True
    return any(rx.match(x) for rx in TAXON_RES)


def supported(name, text):
    """论文文本是否支持该物种声明。返回 True/False；无法判定时由调用方处理。"""
    key = NAME_ALIASES.get(name, name)
    pat = PAT_BY_NAME.get(key)
    if pat:
        return bool(re.search(pat, text, re.I))
    genus = name.split()[0]
    return bool(re.search(r"\b%s\b" % re.escape(genus), text))


def load_concepts():
    out = {}
    for f in os.listdir(CONCEPTS_DIR):
        if f.endswith(".md"):
            out[f[:-3]] = open(os.path.join(CONCEPTS_DIR, f),
                               encoding="utf-8", errors="replace").read()
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--only", choices=["evidence", "concepts"], default=None)
    args = ap.parse_args()

    concepts = load_concepts()
    changed = []
    undecidable = 0

    if args.only in (None, "evidence"):
        for fname in sorted(os.listdir(EVIDENCE_DIR)):
            if not fname.endswith(".md"):
                continue
            path = os.path.join(EVIDENCE_DIR, fname)
            c = open(path, encoding="utf-8", errors="replace").read()
            sp = parse_list_field(c, "species")
            if not sp:
                continue
            src = str_field(c, "source").strip("\"'").strip("[]").strip()
            pc = concepts.get(src)
            if not pc:
                undecidable += 1
                continue
            text = paper_text(pc)
            if len(text.strip()) < MIN_TEXT:
                undecidable += 1
                continue
            review = bool(REVIEW_RE.search(str_field(pc, "title")))
            keep = []
            for s in sp:
                if not is_wellformed(s):
                    continue
                if s in ARTIFACT_SPECIES:
                    # 伪影物种：只在论文文本确实提到时保留
                    if supported(s, text):
                        keep.append(s)
                    continue
                if s in GENERIC or supported(s, text) or review:
                    keep.append(s)
            if not keep:
                prim = str_field(c, "primary_species")
                keep = [prim] if prim and prim not in GENERIC else ["Plant (unspecified)"]
            if keep != sp:
                changed.append((path, sp, keep))

    if args.only in (None, "concepts"):
        for slug, c in concepts.items():
            m = re.search(r"^##\s*深度提炼\s*\n(.+?)(?=\n##\s|\Z)", c, re.S | re.M)
            if not m:
                continue
            blk = m.group(1)
            line_m = re.search(r"^\*\*物种\*\*:\s*(.+)$", blk, re.M)
            if not line_m:
                continue
            raw = [x.strip() for x in line_m.group(1).split(",") if x.strip()]
            text = paper_text(c)
            if len(text.strip()) < MIN_TEXT or REVIEW_RE.search(str_field(c, "title")):
                undecidable += 1
                continue
            # 概念页侧只做“保守去除”：删掉结构性脏值，以及已知正则伪影
            # （Ficus carica 来自 "Fig." 图注）且论文完全不提 fig 的条目；
            # 其余物种不动——深度提炼的物种表本就是论文级概览，不能按摘要点名删。
            keep = []
            for x in raw:
                if not is_wellformed(x):
                    continue
                if x == "Ficus carica" and not supported(x, text):
                    continue
                keep.append(x)
            if not keep:
                keep = [x for x in raw if is_wellformed(x)] or raw
            if keep == raw:
                continue
            newblk = blk.replace(line_m.group(0),
                                 "**物种**: %s" % (", ".join(keep) or "—"))
            path = os.path.join(CONCEPTS_DIR, slug + ".md")
            changed.append((path, ["深度提炼:" + "|".join(raw)],
                            ["深度提炼:" + "|".join(keep)], newblk, line_m.group(0)))

    print("待修页面：%d（无法判定而跳过：%d）" % (len(changed), undecidable))
    for item in changed[:8]:
        print("  %s: %s -> %s" % (os.path.basename(item[0]), item[1], item[2]))
    if not args.apply:
        print("（dry-run，未写盘）")
        return 0

    bak = os.path.expanduser("~/bak_species_support_%s.tgz"
                             % datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))
    rel = [os.path.relpath(i[0], BASE) for i in changed]
    if rel:
        subprocess.run(["tar", "-czf", bak, "-C", BASE] + rel, check=True)
        print("备份：%s" % bak)

    n = 0
    for item in changed:
        path = item[0]
        c = open(path, encoding="utf-8", errors="replace").read()
        if len(item) == 3:  # evidence
            new = "species: [%s]" % ", ".join(item[2])
            c2, cnt = re.subn(r"^species:\s*\[.*?\]", new, c, count=1,
                              flags=re.M | re.S)
        else:  # concept 深度提炼
            old_line, newblk = item[4], item[3]
            newline = re.search(r"^\*\*物种\*\*:.*$", newblk, re.M).group(0)
            c2, cnt = re.subn(re.escape(old_line), newline, c, count=1)
        if cnt:
            open(path, "w", encoding="utf-8").write(c2)
            n += 1
    print("已改写：%d 页；回滚：tar -xzf %s -C %s" % (n, bak, BASE))
    return 0


if __name__ == "__main__":
    sys.exit(main())
