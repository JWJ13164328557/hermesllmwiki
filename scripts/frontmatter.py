#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""frontmatter.py - 知识库 YAML frontmatter 的唯一读写契约。

2026-11-03 事故：repair_theme_tags._set_field 用 `^key\\s*:.*$` 只替换键行，
当原 frontmatter 是块列表时

    themes:
    - other

替换后变成

    themes: [developmental-biology]
    - other        <-- 孤儿列表项，frontmatter 整体 YAML 非法

导致 1189 个论文页在 Dataview/Obsidian 里字段全部读不出来（静默失效）。
本模块的 set_field 会连带清除该键的续行（缩进项或 `- ` 项），
dump_list 统一输出 inline 列表，从写入口杜绝再次出现块列表被就地覆盖。
"""
import re

_KEY_RE = re.compile(r'^([A-Za-z_][A-Za-z0-9_-]*)\s*:(.*)$')
_ITEM_RE = re.compile(r'^\s*-\s+(.*)$')


_GLUED_FENCE_RE = re.compile(r'^---(?=[A-Za-z_][A-Za-z0-9_-]*\s*:)')
_SCALAR_SAFE_KEYS = None


def unfence(text):
    """修复"围栏粘连"：把 '---title: x' 还原成 '---\ntitle: x'。

    2026-11-04 事故：set_field 在被替换键是首个键时会丢掉前导换行，调用方
    '---' + fm 于是拼出 '---scope_status: nonplant'。这种页在 Obsidian 里整段
    属性失效，但 YAML 解析器把分隔符之后当映射，**自检当年判 PASS**（14 页）。
    """
    if text and _GLUED_FENCE_RE.match(text):
        return '---\n' + text[3:]
    return text


def quote_broken_scalars(fm):
    """把解析失败的顶层单行标量改写成 JSON 风格双引号字符串。

    实测：excluded_reason 直接拼论文标题（'nonplant|SCENIC: single-cell ...'），
    冒号让 YAML 认为是嵌套映射，整页 frontmatter 解析失败（3 页）。
    只动"确实解析失败"的键，其他键原样保留。返回 (new_fm, fixed_keys)。
    """
    import json
    try:
        import yaml
    except ImportError:  # pragma: no cover
        return fm, []
    try:
        yaml.safe_load(fm)
        return fm, []
    except Exception:
        pass
    lines = fm.split('\n')
    out, fixed = [], []
    i = 0
    while i < len(lines):
        m = _KEY_RE.match(lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue
        key = m.group(1)
        block = [lines[i]]
        j = i + 1
        while j < len(lines) and (lines[j].startswith(' ') or lines[j].startswith('- ')):
            block.append(lines[j])
            j += 1
        if len(block) > 1:
            # 多行块（续行/列表项）属于 repair_orphans 的职责。这里若把它压成
            # 一个带引号的字符串，会把列表语义改成字符串，比原问题更糟。
            out.extend(block)
            i = j
            continue
        try:
            yaml.safe_load('\n'.join(block))
            out.extend(block)
        except Exception:
            raw = '\n'.join([m.group(2).strip()] + [b.strip() for b in block[1:]]).strip()
            if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in ('"', "'"):
                raw = raw[1:-1]
            out.append('%s: %s' % (key, json.dumps(raw, ensure_ascii=False)))
            fixed.append(key)
        i = j
    return '\n'.join(out), fixed


def split(text):
    """返回 (frontmatter_without_fences, body_with_leading_newline)。"""
    if not text.startswith('---'):
        return '', text
    end = text.find('\n---', 3)
    if end < 0:
        return '', text
    return text[3:end], text[end:]


def get(fm, key, default=''):
    m = re.search(r'^%s\s*:\s*(.*)$' % re.escape(key), fm, re.M)
    return m.group(1).strip() if m else default


def has(fm, key):
    return re.search(r'^%s\s*:' % re.escape(key), fm, re.M) is not None


def parse_list(raw):
    """解析 inline `[a, b]` 或标量；返回去引号后的列表。"""
    raw = (raw or '').strip()
    if not raw or raw in ('[]', '~', 'null'):
        return []
    if raw.startswith('[') and raw.endswith(']'):
        raw = raw[1:-1]
    return [x.strip().strip('"\'') for x in raw.split(',') if x.strip()]


def dump_list(items):
    return '[%s]' % ', '.join(str(i) for i in items if str(i).strip())


def _list_end(fm, key):
    """给定键行在 fm 中的位置，返回该键块结束的偏移（不含）。

    只有块的"值"是块列表时才吞掉续行；inline 标量后面若出现顶格
    `- x`，那本来就是损坏残留，同样吞掉并交由 repair 归并。
    """
    m = re.search(r'^%s\s*:(.*)$' % re.escape(key), fm, re.M)
    if not m:
        return None, None
    start = m.start()
    inline = m.group(1).strip()  # noqa: F841  (保留以说明"块值/标量"语义)
    pos = m.end()
    end = pos
    n = len(fm)
    # 2026-11-03 第 15 轮修死循环：旧实现 `nl = fm.find(chr(10), pos)` 而
    # `pos = nl`，当键行下面紧跟空行时 nl == pos，line 恒为空串，
    # pos 不再前进 —— 整个写入路径（set_field）会 100% CPU 无限自旋。
    # 真实后果：repair_theme_tags / clean_nonresearch_theme_tags 掐在
    # 某一页不动 20+ 分钟，前台看起来就是"卡住"。必须从 pos+1 起找换行。
    while pos < n:
        nl = fm.find('\n', pos + 1)
        if nl < 0:
            end = n
            break
        line = fm[pos + 1:nl]
        if not line.strip():
            end = nl
            pos = nl
            continue
        if _ITEM_RE.match(line) or line.startswith(' ') or line.startswith('\t'):
            end = nl
            pos = nl
            continue
        break
    return start, end


def set_field(fm, key, value):
    """写入/替换一个键，连带删除它遗留的续行（缩进项与顶格短横项）。

    2026-11-04 事故：split() 返回的 fm 以换行开头；当被替换的键是 frontmatter
    的第一个键时，旧实现 head == 空串，返回 "key: v" 丢掉前导换行，调用方再拼
    "---" + fm 就得到 "---key: v"，整页 frontmatter 不再是围栏块（14 页实测）。
    这里保留原文的前导换行，让 "---" + fm 的拼接契约成立。
    """
    lead = '\n' if fm.startswith('\n') else ''
    line = '%s: %s' % (key, value)
    m = re.search(r'^%s\s*:(.*)$' % re.escape(key), fm, re.M)
    if not m:
        body = fm.rstrip('\n')
        return (body + '\n' + line + '\n') if body else (lead + line + '\n')
    start, end = _list_end(fm, key)
    if end is None:
        end = m.end()
    head = fm[:start].rstrip('\n')
    tail = fm[end:].lstrip('\n')
    out = (head + '\n' + line + '\n') if head else (lead + line + '\n')
    return out + tail if tail else out

def repair_orphans(fm, themes_norm=None):
    """把顶格 `- x` 孤儿项并回它上方那个 inline 标量键。

    themes_norm: 可选 callable(item) -> 归一后的主题名或 None（丢弃）。
    返回 (new_fm, merged_count)。
    """
    lines = fm.split('\n')
    out = []
    owner = None  # (index_in_out, key, value_str)
    merged = 0
    for line in lines:
        m = _KEY_RE.match(line)
        if m:
            owner = [len(out), m.group(1), m.group(2).strip()]
            out.append(line)
            continue
        im = _ITEM_RE.match(line)
        if im:
            item = im.group(1).strip().strip('"\'')
            if owner is None or not owner[2]:
                out.append(line)  # 合法的块列表项，保留
                continue
            idx, key, val = owner
            cur = parse_list(val)
            if themes_norm is not None and key == 'themes':
                norm = themes_norm(item)
                if norm is None:
                    merged += 1
                    continue
                item = norm
            if item not in cur:
                cur.append(item)
            out[idx] = '%s: %s' % (key, dump_list(cur))
            owner[2] = dump_list(cur)
            merged += 1
            continue
        if not line.strip():
            out.append(line)
            continue
        out.append(line)
    return '\n'.join(out), merged
_CTRL_RE = re.compile(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]')


def sanitize_ctrl(text):
    """剔除 YAML 解析器拒绝的控制字符（PDF 抽取残留 0x01..0x08）。

    2026-11-03：29 个证据页的 title 里带 0x01-0x08，PyYAML 抛
    ReaderError "unacceptable character"，整段 frontmatter 不可读。
    """
    if not text:
        return text
    return _CTRL_RE.sub(' ', text)
def clean_inline_lists(fm):
    """丢弃 inline 列表里混入的抓取垃圾（含 `**` 的整段正文）。

    2026-11-03 实例：species 从概念页 `**物种**:` 行尾递归吃到整段
    `**方法**: ... **来源类型**: PDF全文 (...)`，写进 `species: [...]`
    后变成非法 YAML。只在该页已经解析失败时调用。
    """
    lines = fm.split('\n')
    out = []
    changed = 0
    for line in lines:
        m = re.match(r'^([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*\[(.*)\]\s*$', line)
        if not m:
            out.append(line)
            continue
        key, inner = m.group(1), m.group(2)
        items = [x.strip() for x in inner.split(',') if x.strip()]
        kept = [x for x in items if '**' not in x]
        if len(kept) != len(items):
            changed += 1
            out.append('%s: %s' % (key, dump_list(kept)))
        else:
            out.append(line)
    return '\n'.join(out), changed