"""article_kind.py — 文献类型分层（不删除、不移动页面）。

目的：把"更正/撤稿/社论/勘误/会议纪要/目录页/网页复制残留"从研究证据池里
分层隔离，同时保留页面本体供人工追溯与引用核对。

设计要点
  1. 只写 frontmatter 的 `article_kind` 字段，不动正文；
  2. 只给"非 research"写标签，research 是默认值（避免对 7000+ 页做猜测性写入）；
  3. 下游一律通过 `kind_of()` / `is_evidence_eligible()` 读取，禁止各脚本自写规则；
  4. 分类依据全部可复核：标题前缀、期刊名、DOI 残留字符。
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

# 可作为研究证据的文献类型
EVIDENCE_KINDS = frozenset({"research", "review"})

# 不进入证据池（但页面保留）
NON_EVIDENCE_KINDS = frozenset({
    "corrigendum", "erratum", "retraction", "expression-of-concern",
    "editorial", "commentary", "letter", "news", "meeting-report",
    "book-review", "front-matter", "non-article", "publisher-note",
})

CJK = re.compile(r"[\u4e00-\u9fff]")

_PATTERNS = [
    ("retraction", re.compile(r"^\s*\(?(retraction|retracted|withdrawal)\b", re.I)),
    ("retraction", re.compile(r"^\s*retraction (notice|note)\b", re.I)),
    ("corrigendum", re.compile(r"^\s*\(?(corrigendum|corrigenda)\b", re.I)),
    ("corrigendum", re.compile(r"^\s*correction to\b", re.I)),
    ("erratum", re.compile(r"^\s*\(?erratum\b", re.I)),
    ("expression-of-concern", re.compile(r"^\s*expression of concern\b", re.I)),
    ("editorial", re.compile(r"^\s*editorial\b", re.I)),
    ("commentary", re.compile(r"^\s*commentary\b", re.I)),
    ("letter", re.compile(r"^\s*(letter to (the )?editor|correspondence)\b", re.I)),
    ("news", re.compile(r"^\s*(news|in brief|research highlights?|press release)\b", re.I)),
    ("meeting-report", re.compile(r"(meeting report|conference report|a summary of the \d{4}|proceedings of the \d+)", re.I)),
    ("front-matter", re.compile(r"(membership (form|application)|table of contents|editorial board|author index|subject index|front matter|back matter|instructions to authors|call for papers|masthead|cover image)", re.I)),
    ("front-matter", re.compile(r"^\s*(index|contents)\s*$", re.I)),
    ("publisher-note", re.compile(r"^\s*(publisher'?s note|publisher correction)\b", re.I)),
]

_REVIEW_HINTS = re.compile(
    r"(\breview\b|\boverview\b|advances in|progress in|perspectives? on|state of the art|"
    r"current (status|understanding)|a survey of|recent developments)", re.I)

_PLANT_JOURNAL = re.compile(
    r"(plant|phytopath|botan|phytolog|flora|forest|tree|crop|agron|hortic|weed|"
    r"photosynth|planta|protoplasma|annurev-arplant|j\.? exp\.? bot)", re.I)


def kind_of(fm_or_dict):
    """从 dict 或 frontmatter 文本读取 article_kind（缺省 research）。"""
    if isinstance(fm_or_dict, dict):
        v = fm_or_dict.get("article_kind")
    else:
        m = re.search(r"^article_kind:\s*\"?([a-z\-]+)", fm_or_dict or "", re.M)
        v = m.group(1) if m else ""
    v = (v or "").strip().lower()
    return v if v in EVIDENCE_KINDS | NON_EVIDENCE_KINDS else "research"


def is_evidence_eligible(kind):
    return (kind or "research") in EVIDENCE_KINDS


def classify(title="", doi="", journal="", body=""):
    """返回 (kind, reasons)。reasons 为可复核的判定依据列表。"""
    t = (title or "").strip()
    reasons = []

    if CJK.search(doi or ""):
        return "non-article", ["doi-contains-cjk=web-copy-artifact"]
    if not t:
        return "non-article", ["empty-title"]

    for kind, pat in _PATTERNS:
        if pat.search(t):
            reasons.append("title-prefix=%s" % kind)
            return kind, reasons

    # "Review: X" 只有在非植物期刊上才是书评（植物学刊里 Review: 是综述标题的一部分）
    if re.match(r"^\s*review\s*:", t, re.I):
        if journal and not _PLANT_JOURNAL.search(journal):
            return "book-review", ["review-prefix+non-plant-journal"]
        return "review", ["review-prefix"]

    if _REVIEW_HINTS.search(t):
        return "review", ["title-hint=review"]

    return "research", ["default"]


def audit_page(path):
    """读取页面，返回 (kind, reasons, current_kind)。"""
    with open(path, encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    fm, body = text, ""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end > 0:
            fm, body = text[3:end], text[end + 4:]
    m = re.search(r'^title:\s*"?(.*?)"?\s*$', fm, re.M)
    title = m.group(1) if m else ""
    m2 = re.search(r"^title:\s*(.+?)\n(?=[A-Za-z_]+:)", fm, re.M | re.S)
    if m2 and len(m2.group(1)) > len(title):
        title = m2.group(1)
    title = re.sub(r"<[^>]+>", " ", title)
    title = re.sub(r"\s+", " ", title).strip().strip("\"'")
    # 回退到正文 H1（2026-11-03）：相当一批概念页的标题只写在
    # `# ...` 一级标题里，frontmatter 没有 title 字段。之前直接按空标题
    # 判 non-article，把正常论文归入了非研究页。
    if not title and body:
        mh = re.search(r"^#\s+(.+)$", body, re.M)
        if mh:
            title = re.sub(r"<[^>]+>", " ", mh.group(1))
            title = re.sub(r"\s+", " ", title).strip().strip("\"'")

    m = re.search(r'^doi:\s*"?([^"\s]+)', fm, re.M)
    doi = m.group(1) if m else ""
    m = re.search(r"^journal:\s*\"?(.+?)\"?\s*$", fm, re.M)
    journal = m.group(1).strip() if m else ""
    if not journal:
        m = re.search(r"^\s*-\s*\*\*期刊\*\*:\s*(.+?)$", body or fm, re.M)
        journal = m.group(1).strip() if m else ""

    kind, reasons = classify(title, doi, journal, body)
    return kind, reasons, kind_of(fm), title, fm, body


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="/mnt/g/hermes_obsidian/hermes/concepts/papers")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--audit", default="")
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()

    files = sorted(f for f in os.listdir(a.dir) if f.endswith(".md"))
    rows, changed = [], []
    for f in files:
        kind, reasons, cur, title, fm, body = audit_page(os.path.join(a.dir, f))
        if kind == "research" and cur == "research":
            continue
        if a.limit and len(rows) >= a.limit:
            break
        rows.append((f, kind, cur, "|".join(reasons), title[:90].replace("\t", " ")))
        if a.apply and kind != "research" and kind != cur:
            newfm = fm
            if re.search(r"^article_kind\s*:", newfm, re.M):
                newfm = re.sub(r"^article_kind\s*:.*$", "article_kind: %s" % kind, newfm, count=1, flags=re.M)
            else:
                newfm = newfm.rstrip("\n") + "\narticle_kind: %s\n" % kind
            with open(os.path.join(a.dir, f), "w", encoding="utf-8") as fh:
                fh.write("---" + newfm + "\n---" + body)
            changed.append(f)

    if a.audit:
        with open(a.audit, "w", encoding="utf-8") as fh:
            fh.write("page\tarticle_kind\tprevious\treasons\ttitle\n")
            for r in rows:
                fh.write("\t".join(r) + "\n")

    from collections import Counter
    c = Counter(r[1] for r in rows)
    print(json.dumps({"scanned": len(files), "non_research": len(rows),
                      "applied": len(changed), "by_kind": dict(c)}, ensure_ascii=False))
    for k, v in sorted(c.items(), key=lambda x: -x[1]):
        print("  %-24s %d" % (k, v))


if __name__ == "__main__":
    main()
