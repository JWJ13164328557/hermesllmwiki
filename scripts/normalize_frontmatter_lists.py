# -*- coding: utf-8 -*-
"""规范化 frontmatter 的列表型键：合并重复键、清除翻译服务垃圾、保序去重。

解决三类真实缺陷：
1. 重复顶层键 —— PyYAML 静默「后者覆盖前者」，任何 yaml.safe_load 校验都查不出，
   但数据已经丢了（本轮实测 alfalfa 页 aliases 被吞掉 2 条）。
2. 翻译服务报错串被写进 aliases —— 例如
   "MYMEMORY WARNING: YOU USED ALL AVAILABLE FREE TRANSLATIONS FOR TODAY..."，
   实测 711 条，散布 246 页。
3. 列表内重复项。

安全约束（每条都有对应的回归测试）：
- 标量型取值（species: Arabidopsis thaliana、tags: xxx）一律原样保留，绝不视为空列表删除。
- 未命中上述缺陷的块逐字节原样输出，保证小 diff。
- 默认 dry-run，--apply 才写盘。
"""
import argparse
import json
import pathlib
import re
import sys

LIST_KEYS = {
    "aliases", "aliases_extra", "merged_from",
    "tags", "themes", "methods", "species", "keywords",
}
KEY_RE = re.compile(r"^([A-Za-z_][\w-]*):(.*)$")
ITEM_RE = re.compile(r"^\s*[-*]\s+(.*)$")

# 翻译服务 / 配额报错串。这些不是别名，是故障留下的噪声。
SERVICE_NOISE = [
    re.compile(r"MYMEMORY", re.I),
    re.compile(r"GOOGLE TRANSLATE", re.I),
    re.compile(r"TRANSLATIONS? FOR TODAY", re.I),
    re.compile(r"\bDEEPL\b", re.I),
    re.compile(r"TRANSLATED\.NET", re.I),
    re.compile(r"QUOTA (EXCEEDED|EXHAUSTED)", re.I),
    re.compile(r"INVALID API KEY", re.I),
]


def is_noise(value):
    return any(p.search(value) for p in SERVICE_NOISE)


def unquote(s):
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        return s[1:-1]
    return s


# 早期修复脚本把 flow 列表多套了一层引号和冒号，写成
#   aliases_extra: ': ["a", "b"]'
# 值本身仍是合法 YAML 标量，所以任何 yaml.safe_load 校验都不会报错。
QUOTE_CHARS = chr(34) + chr(39)
OVERQUOTED_FLOW = re.compile(
    r"^\s*[" + QUOTE_CHARS + r"]\s*:\s*(\[.*\])\s*[" + QUOTE_CHARS + r"]\s*$"
)
# 同一类缺陷的变体：没有多余的冒号，只是整条 flow 列表被一层引号包住，
# 于是 YAML 把它当标量（不是列表）读。实测 3 页（pdf-nph-71298 等）。
OVERQUOTED_FLOW2 = re.compile(
    r"^\s*[" + QUOTE_CHARS + r"]\s*(\[.*\])\s*[" + QUOTE_CHARS + r"]\s*$"
)

# 占位符：这些值不是数据。species: — / methods: — 实测 24 页。
PLACEHOLDER = re.compile(r"^[\s\u2010-\u2015\u2212*?.]*$")


def split_flow_items(inner):
    """只做顶层逗号切分，尊重引号内的逗号。"""
    items, buf, quote = [], [], None
    for ch in inner:
        if quote:
            buf.append(ch)
            if ch == quote:
                quote = None
        elif ch in QUOTE_CHARS:
            quote = ch
            buf.append(ch)
        elif ch == ",":
            items.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    items.append("".join(buf))
    return [unquote(x) for x in items if unquote(x)]


def parse_flow(rest):
    """返回 (items, overquoted)；非列表返回 None。

    overquoted=True 表示该行被早期脚本多套了一层引号，
需要重写成标准 block 列表。
    """
    r = rest.strip()
    m = OVERQUOTED_FLOW.match(r) or OVERQUOTED_FLOW2.match(r)
    overquoted = bool(m)
    if m:
        r = m.group(1)
    if not (r.startswith("[") and r.endswith("]")):
        return None
    inner = r[1:-1].strip()
    if not inner:
        return [], overquoted
    return split_flow_items(inner), overquoted


def parse_block(body):
    """- a\n- b -> ([a, b], True)；没有任何列表项则返回 ([], False)。"""
    items = []
    for ln in body:
        m = ITEM_RE.match(ln)
        if m:
            v = unquote(m.group(1))
            if v:
                items.append(v)
    return items, bool(items)


class Block:
    __slots__ = ("key", "header", "rest", "body", "kind", "items")

    def __init__(self, key, header, rest):
        self.key = key
        self.header = header
        self.rest = rest
        self.body = []
        self.kind = "scalar"
        self.items = []


def split_blocks(fm):
    blocks = []
    cur = None
    preamble = []
    for ln in fm.splitlines():
        m = KEY_RE.match(ln)
        if m:
            cur = Block(m.group(1), ln, m.group(2))
            blocks.append(cur)
        elif cur is not None:
            cur.body.append(ln)
        else:
            preamble.append(ln)
    for b in blocks:
        flow = parse_flow(b.rest)
        if flow is not None:
            items, overquoted = flow
            b.kind = "flow_overquoted" if overquoted else "flow"
            b.items = items
            continue
        items, has_items = parse_block(b.body)
        if has_items:
            b.kind, b.items = "block", items
        elif not b.rest.strip() and not b.body:
            b.kind, b.items = "empty", []
        # 其余情况（有内容但不是列表）保持 scalar
    return preamble, blocks


def render_list(key, items):
    return [key + ":"] + ["- " + json.dumps(i, ensure_ascii=False) for i in items]


def _has_notes(notes):
    """notes 是否含有需要人看的信息（即使这一段文本没有改动）。

    2026-11-02 修复：此前无文本变更时直接 return fm, {}，把 scalar_conflict
    这类「没改但必须复核」的计数吞掉，导致 CLI 报 pages_with_scalar_conflict: 0，
    而库里有 54 页 species/methods 把逗号列表塞进标量。指标是假绿。
    """
    return bool(notes.get("merged_keys") or notes.get("noise_dropped")
                or notes.get("dup_items") or notes.get("empty_dropped")
                or notes.get("scalar_conflict") or notes.get("placeholder_value"))


def normalize(fm):
    """返回 (新 fm, 变更说明 dict)。无变更时原样返回 fm。"""
    preamble, blocks = split_blocks(fm)
    if not blocks:
        return fm, {}

    by_key = {}
    for b in blocks:
        by_key.setdefault(b.key, []).append(b)

    notes = {"merged_keys": [], "noise_dropped": 0, "dup_items": 0,
             "empty_dropped": [], "scalar_conflict": [],
             "placeholder_value": []}
    planned = {}  # id(block) -> lines to emit, or None to skip

    for key, group in by_key.items():
        if key not in LIST_KEYS:
            if len(group) > 1:
                notes["scalar_conflict"].append(key)
                planned[id(group[0])] = [group[0].header] + group[0].body
                for extra in group[1:]:
                    planned[id(extra)] = None
            continue

        listy = [b for b in group if b.kind in ("flow", "flow_overquoted", "block", "empty")]
        scalars = [b for b in group if b.kind == "scalar"]
        for b in scalars:
            if PLACEHOLDER.match(unquote(b.rest)) and unquote(b.rest).strip():
                notes["placeholder_value"].append(key)
        if scalars:
            # 同名键既有标量又有列表：无法安全自动判定，原样保留并报告
            notes["scalar_conflict"].append(key)
            for b in group:
                planned[id(b)] = [b.header] + b.body
            continue

        merged = []
        for b in listy:
            for it in b.items:
                if is_noise(it):
                    notes["noise_dropped"] += 1
                    continue
                if it in merged:
                    notes["dup_items"] += 1
                    continue
                merged.append(it)

        touched = len(group) > 1 or any(is_noise(i) for b in listy for i in b.items)
        touched = touched or any(b.kind == "flow_overquoted" for b in listy)
        touched = touched or any(
            len(b.items) != len(set(b.items)) for b in listy)
        if not touched:
            continue

        first = group[0]
        if len(group) > 1:
            notes["merged_keys"].append("%s x%d" % (key, len(group)))
        if not merged:
            planned[id(first)] = None
            for extra in group[1:]:
                planned[id(extra)] = None
            notes["empty_dropped"].append(key)
            continue
        planned[id(first)] = render_list(key, merged)
        for extra in group[1:]:
            planned[id(extra)] = None

    if not any(planned.values()) and not any(v is None for v in planned.values()):
        return fm, (notes if _has_notes(notes) else {})

    out = []
    out.extend(preamble)
    for b in blocks:
        if id(b) in planned:
            emit = planned[id(b)]
            if emit is not None:
                out.extend(emit)
        else:
            out.append(b.header)
            out.extend(b.body)
    new = "\n".join(out)
    # 保持原件的结尾换行：写回时是 "---" + fm + "---"，少一个 \n 就把闭合围栏
    # 粘到最后一行（实测 3 页变成 `authors: ..., Liu Chang---`，YAML 直接坏掉）。
    if fm.endswith("\n") and not new.endswith("\n"):
        new += "\n"
    if new.strip() == fm.strip():
        return fm, (notes if _has_notes(notes) else {})
    return new, notes


def iter_targets(base):
    seen = set()
    for d in ("concepts/papers", "concepts/methods", "concepts"):
        root = base / d
        if not root.is_dir():
            continue
        for p in sorted(root.glob("*.md")):
            if p not in seen:
                seen.add(p)
                yield p


def split_page(text):
    """'---\n<fm>\n---\n<body>' -> (fm, body)；不可解析返回 (None, None)。

    契约：join_page(split_page(t)) == t。2026-11-02 修：旧实现在写回时用
    "---\n" + fm 拼接，而 fm 本身以换行开头，于是每改一页就多插一个空行
    （实测 3 页首行变成 '---\n\ntitle:'）。
    """
    if not text.startswith("---"):
        return None, None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, None
    return parts[1], parts[2]


def join_page(fm, body):
    return "---" + fm + "---" + body


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="/mnt/g/hermes_obsidian/hermes")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args(argv)
    base = pathlib.Path(args.base)

    changed = noise = flagged = 0
    merged_key_pages = empty_pages = conflict_pages = 0
    placeholder_pages = 0
    for p in iter_targets(base):
        text = p.read_text(encoding="utf-8", errors="replace")
        fm, body = split_page(text)
        if fm is None:
            continue
        new_fm, notes = normalize(fm)
        if not notes:
            continue
        if new_fm == fm:
            flagged += 1          # 只报告，不改写
        else:
            changed += 1
        noise += notes["noise_dropped"]
        if notes["merged_keys"]:
            merged_key_pages += 1
        if notes["empty_dropped"]:
            empty_pages += 1
        if notes["scalar_conflict"]:
            conflict_pages += 1
        if notes["placeholder_value"]:
            placeholder_pages += 1
        if args.verbose or changed <= 5:
            if new_fm == fm:
                tag = "FLAG  "
            else:
                tag = "WOULD FIX " if not args.apply else "FIXED "
            print(tag + str(p.relative_to(base)) + " "
                  + json.dumps(notes, ensure_ascii=False))
        if args.apply:
            p.write_text(join_page(new_fm, body),
                         encoding="utf-8", newline="\n")

    print(json.dumps({
        "mode": "apply" if args.apply else "dry-run",
        "pages_changed": changed,
        "pages_flagged_no_change": flagged,
        "noise_items_dropped": noise,
        "pages_with_merged_dup_keys": merged_key_pages,
        "pages_with_emptied_list": empty_pages,
        "pages_with_scalar_conflict": conflict_pages,
        "pages_with_placeholder_value": placeholder_pages,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
