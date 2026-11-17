# -*- coding: utf-8 -*-
"""还原被旧 phase9 覆盖的一级标题。

旧 batch_translate_metabolism.py 执行
    re.sub(r"^# .+$\n\n", f"# {zh}\n\n> {en}\n\n", content, count=1)
把 H1 换成中文（zh 是 simple_translate 生成的词语沙拉），并把原英文标题降级成
紧随其后的一行引用 `> {en}`。因此对「H1 中英混杂 + 下一段是纯英文引用」的页面，
把 H1 换回该引用行原文、再删掉这行引用，等价于精确撤销那次变换。

不做的事：不猜测没有引用行的页面（那些是别的破损形态），也不动本身就是
中文来源的页面（微信/博客，H1 本来就是中文）。
"""
import argparse
import pathlib
import re
import sys

CJK = re.compile(r"[\u4e00-\u9fff]")
LATIN = re.compile(r"[A-Za-z]{3,}")
H1 = re.compile(r"^# (.+)$", re.M)


def restore(text):
    """返回 (新文本, 说明)。没有可还原项时原样返回。"""
    m = H1.search(text)
    if not m:
        return text, None
    h1 = m.group(1)
    if not (CJK.search(h1) and LATIN.search(h1)):
        return text, None

    after = text[m.end():]
    lines = after.split("\n")
    # after 以 H1 行尾的换行开始，lines[0] == ""
    idx = None
    for i, ln in enumerate(lines):
        if ln.strip() == "":
            continue
        idx = i
        break
    if idx is None:
        return text, None
    quote = lines[idx]
    if not quote.startswith(">"):
        return text, None
    en = quote[1:].strip()
    if not en or CJK.search(en) or len(en) < 15:
        return text, None

    # 引用行之后的内容（跳过引用行本身与其后的空行）
    rest_lines = lines[idx + 1:]
    while rest_lines and rest_lines[0].strip() == "":
        rest_lines.pop(0)
    new_text = text[:m.start()] + "# " + en + "\n\n" + "\n".join(rest_lines)
    return new_text, {"old_h1": h1, "new_h1": en}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="/mnt/g/hermes_obsidian/hermes")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)
    root = pathlib.Path(args.base) / "concepts" / "papers"

    changed = 0
    for p in sorted(root.glob("*.md")):
        text = p.read_text(encoding="utf-8", errors="replace")
        new_text, note = restore(text)
        if not note:
            continue
        changed += 1
        if changed <= 5:
            print(("WOULD FIX " if not args.apply else "FIXED ") + p.name)
        if args.apply:
            p.write_text(new_text, encoding="utf-8", newline="\n")
    print(("WOULD FIX" if not args.apply else "FIXED") + " %d pages" % changed)


if __name__ == "__main__":
    main()
