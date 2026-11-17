# -*- coding: utf-8 -*-
"""修复 themes 里混入标题残段的页面（可证明，不猜）。

破损形态（pdf_scan / dPDF 导入器把含 <i>...</i> 的标题按逗号切错）：
    title: '"<i>EMF2</i>'
    themes: '[developmental-biology, ...] deficiency disrupts ... in Arabidopsis"'

两种方向，各有可验证的等式：
  A 标题被截断、残段落在 themes 尾巴：
        bare(title + ' ' + tail) == bare(alias)   -> title := title + ' ' + tail
  B 标题本身完整、themes 尾巴只是标题的片段：
        bare(tail) in bare(title)                 -> themes := [tag]

等式不成立就 SKIP，留给人工。默认 dry-run。
"""
import argparse
import pathlib
import re
import unicodedata

DASH = dict.fromkeys(map(ord, "\u2010\u2011\u2012\u2013\u2014\u2212"), "-")
DQ = chr(34)
SQ = chr(39)


def norm(s):
    s = unicodedata.normalize("NFKC", s).translate(DASH)
    return re.sub(r"\s+", " ", s).strip().strip(SQ + DQ).strip()


def bare(s):
    s = re.sub(r"<[^>]+>", "", norm(s))
    return re.sub(r"[^0-9A-Za-z\u4e00-\u9fff]+", "", s).lower()


def get(fm, key):
    m = re.search(r"^%s:[ \t]*(.*)$" % key, fm, re.M)
    return m.group(1) if m else ""


def alias_item(fm):
    """取 aliases 的第一条，兼容 flow / block / 过度引号三种写法。"""
    raw = get(fm, "aliases").strip()
    if raw:
        items = re.findall(DQ + r"((?:[^" + DQ + r"\\]|\\.)*)" + DQ, raw)
        if items:
            return items[0]
        return raw.strip(SQ).strip(DQ).strip("[]").strip()
    m = re.search(r"^aliases:[ \t]*\n((?:[ \t]*-[ \t]*.*\n?)+)", fm, re.M)
    if not m:
        return ""
    for line in m.group(1).splitlines():
        v = re.sub(r"^[ \t]*-[ \t]*", "", line).strip()
        if v:
            return v.strip(SQ).strip(DQ)
    return ""


def yaml_scalar(value):
    """安全写法的 YAML 双引号标量（标题里常见 ': ' 与 <i> 标签）。"""
    out = value.replace("\\", "\\\\").replace(DQ, "\\" + DQ)
    return DQ + out + DQ


def plan(fm):
    """返回 (新 fm, 说明) 或 (None, 原因)。只在等式成立时给改写。"""
    themes_raw = get(fm, "themes")
    title_raw = get(fm, "title")
    th_probe = themes_raw.strip()
    if "]" not in themes_raw or not th_probe.startswith((SQ + "[", DQ + "[", "[")):
        return None, "themes 不是 [tags]+尾巴 形态"
    th = th_probe.strip(SQ).strip(DQ)
    head, tail = th.split("]", 1)
    tag = head.strip().strip("[").strip()
    tail = tail.strip().strip(SQ).strip(DQ)
    if not tail:
        return None, "themes 无尾巴"
    if not tag:
        return None, "tag 为空"

    # B：尾巴是标题的片段（重复复制）
    if bare(tail) and bare(tail) in bare(title_raw):
        return fm.replace(themes_raw, "[" + tag + "]", 1), (
            "B: themes 尾巴是标题片段，删尾巴", "themes=" + tag)

    # A：标题被截断，尾巴是剩余部分
    cand = norm(title_raw) + " " + norm(tail)
    ab = bare(alias_item(fm))
    if ab and bare(cand) == ab:
        new_fm = fm.replace(title_raw, yaml_scalar(cand), 1)
        new_fm = new_fm.replace(themes_raw, "[" + tag + "]", 1)
        return new_fm, ("A: title+tail==alias 还原标题", cand[:80])

    return None, "两个等式都不成立（title+tail != alias 且 tail 不在 title 内）"


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="/mnt/g/hermes_obsidian/hermes")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)
    root = pathlib.Path(args.base) / "concepts" / "papers"
    n = 0
    for p in sorted(root.glob("*.md")):
        text = p.read_text(encoding="utf-8", errors="replace")
        parts = text.split("---", 2)
        if len(parts) < 3:
            continue
        fm = parts[1]
        th = get(fm, "themes")
        if "]" not in th or not th.split("]", 1)[1].strip():
            continue          # 正常 flow 列表，无尾巴

        new_fm, note = plan(fm)
        if new_fm is None:
            print("SKIP", p.name, "|", note)
            continue
        n += 1
        print(("WOULD FIX " if not args.apply else "FIXED ") + p.name,
              "|", note[0], "|", note[1][:90])
        if args.apply:
            p.write_text("---" + new_fm + "---" + parts[2],
                         encoding="utf-8", newline="\n")
    print(("%s %d pages" % ("WOULD FIX" if not args.apply else "FIXED", n)))


if __name__ == "__main__":
    main()
