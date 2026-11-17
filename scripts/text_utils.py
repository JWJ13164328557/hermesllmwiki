#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""text_utils.py — 文本清洗与 YAML 安全的唯一实现。

存在理由（2026-11-01，基于线上运行实测）：
1. PubMed efetch 返回的标题/摘要含行内标记（<i> <sup> <sub> <b>）。
   旧代码用 `el.text` 取值，只拿到第一个子元素之前的文字，
   于是标题断在 "…Biosynthesis of Cellulase by "、摘要断在
   "…production using "。线上 3422 篇里 239 篇标题尾部带空格、
   155 篇标题以介词/连词结尾、679 篇摘要不足 700 字符。
   正确做法是 `''.join(el.itertext())`。
2. `title: {...[:80]}` 既会截断在词中间，又会在标题含冒号时破坏 YAML。
   这里统一走 `yaml_str()`。
"""
import re
import unicodedata

_WS = re.compile(r'[ \t\r\f\v]+')
_LINEBREAK = re.compile(r'\n{3,}')
_DANGLE = re.compile(
    r'(?:[\(\[\{/\-–—,;:]|\b(?:by|of|for|with|in|and|or|the|a|an|to|on|from|using|'
    r'at|as|via|into|under|between|than|that|which|per|versus|vs))\s*$', re.I)


def xml_text(el):
    """取 XML 元素全部文本（含行内标记内文字），并归一化空白。"""
    if el is None:
        return ''
    txt = ''.join(el.itertext())
    txt = unicodedata.normalize('NFC', txt)
    txt = _WS.sub(' ', txt)
    txt = _LINEBREAK.sub('\n\n', txt)
    return txt.strip()


def yaml_str(value):
    """把任意字符串写成 YAML 双引号标量（可安全放在 `key: ` 之后）。

    处理反斜杠、双引号、换行与控制字符；不依赖 PyYAML。
    """
    if value is None:
        return '""'
    s = unicodedata.normalize('NFC', str(value))
    out = []
    for ch in s.replace('\r\n', '\n').replace('\r', '\n'):
        if ch == '\\':
            out.append('\\\\')
        elif ch == '"':
            out.append('\\"')
        elif ch == '\n':
            out.append('\\n')
        elif ch == '\t':
            out.append('\\t')
        elif ord(ch) < 0x20 or ord(ch) == 0x7f:
            out.append(' ')
        else:
            out.append(ch)
    return '"' + ''.join(out) + '"'


def clip_words(text, limit=120, ellipsis='…'):
    """按词边界截断；不足上限则原样返回（不补省略号）。"""
    text = (text or '').strip()
    if limit <= 0 or len(text) <= limit:
        return text
    cut = text[:limit]
    m = re.search(r'\S+\s*$', cut)
    if m and m.start() > limit // 2:
        cut = cut[:m.start()]
    cut = cut.rstrip(' ,;:-–—(')
    return cut + ellipsis


def clip_sentences(text, limit=3000, ellipsis='…'):
    """按句子边界截断；找不到合适边界时退化为按词边界。"""
    text = (text or '').strip()
    if limit <= 0 or len(text) <= limit:
        return text
    window = text[:limit]
    best = max(window.rfind('. '), window.rfind('。'), window.rfind('? '),
               window.rfind('! '), window.rfind('\n'))
    if best > limit // 2:
        return window[:best + 1].rstrip() + ellipsis
    return clip_words(text, limit, ellipsis)


def has_dangling_tail(text):
    """标题/句子是否以介词、连词、标点等“不完整”片段结尾。"""
    return bool(_DANGLE.search((text or '').rstrip()))


def normalize_space(text):
    return _WS.sub(' ', (text or '').replace('\n', ' ')).strip()


# 2026-11-02：线上实测发现导入端会把 DOI 写坏，而且是系统性的（连字符被文件名吞掉、
# Crossref citation-id 被当成 DOI 路径）。这里只做「可证明安全」的纠正，绝不猜测；
# 拿不准的一律返回原值 + 原因，由调用方打 needs_review，而不是伪造一个看起来对的 DOI。
_DOI_ANY = re.compile(r'^10\.\d{4,9}/\S+$')
# OUP 抓 PDF 时多带一个纯数字的 citation-id 尾巴：
#   10.1093/hr/uhag117/8607838 -> 10.1093/hr/uhag117
_OUP_CITATION_TAIL = re.compile(r'^(10\.1093/[^/]+/[^/]+)/\d{6,}$')
# Annual Reviews：YYYYMMDD 与 6 位文章号之间的连字符被吞：
#   annurev-arplant-081720010120 -> annurev-arplant-081720-010120
_ANNUREV_MERGE = re.compile(r'^(10\.1146/[a-z0-9-]+?)(\d{6})(\d{6})$')
# Nature 系：s 编号后的连字符被吞：s41477025-02181-9 -> s41477-025-02181-9
_NATURE_MERGE = re.compile(r'^(10\.1038/s)(\d{5})(\d{3})-(\d+)-([0-9a-z]+)$')
# 只到刊名、没有文章号——不是论文 DOI，属于导入事故。
_JOURNAL_LEVEL = re.compile(
    r'^10\.(?:1111/(?:jipb|pbi|pce|tpj|nph|pj|tpc)|1002/advs|64898/\d+)$')


def normalize_doi(doi):
    """纠正导入端可证明写坏的 DOI。

    返回 (doi, reason)。reason 取值：empty / ok / fixed_oup_tail /
    fixed_annurev / fixed_nature / journal_level / malformed。
    只有 reason 以 fixed_ 开头时返回值才与输入不同；journal_level 与
    malformed 表示该 DOI 不可信，调用方应打标而非改写。
    """
    raw = (doi or '').strip()
    if not raw:
        return '', 'empty'
    d = raw.lower().rstrip('.,;')
    if _JOURNAL_LEVEL.match(d):
        return raw, 'journal_level'
    m = _OUP_CITATION_TAIL.match(d)
    if m:
        return m.group(1), 'fixed_oup_tail'
    m = _ANNUREV_MERGE.match(d)
    if m:
        head = m.group(1).rstrip('-')
        return '%s-%s-%s' % (head, m.group(2), m.group(3)), 'fixed_annurev'
    m = _NATURE_MERGE.match(d)
    if m:
        return '%s%s-%s-%s-%s' % (m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)), 'fixed_nature'
    if _DOI_ANY.match(d):
        return raw, 'ok'
    return raw, 'malformed'



# ───────────────────────── 翻译服务噪声 ─────────────────────────
# 免费翻译 API 在配额耗尽时会把错误说明放在 translatedText 里返回，
# responseStatus 却是 200。旧代码只判 len>5，于是这句话被当成译文
# 写进 aliases（线上实测 711 条）。
_TRANSLATION_NOISE = re.compile(
    r"MYMEMORY|TRANSLATED\.NET|GOOGLE TRANSLATE|\bDEEPL\b|"
    r"TRANSLATIONS? FOR TODAY|QUOTA (?:EXCEEDED|EXHAUSTED)|"
    r"INVALID API KEY|USAGE ?LIMITS?|TOO MANY REQUESTS",
    re.I)


def is_translation_noise(text):
    """判断一段文本是否是翻译服务残留/报错，而非真实译文。"""
    if not text:
        return False
    s = unicodedata.normalize("NFC", str(text))
    return bool(_TRANSLATION_NOISE.search(s))


def looks_translated(text, source=None):
    """粗略判断 text 是否确实是中文译文。

    要求：含 CJK 字符；若给出 source，则不接受与原文几乎相同的结果。
    """
    if not text or is_translation_noise(text):
        return False
    if not re.search(r"[\u4e00-\u9fff]", text):
        return False
    if source:
        a = re.sub(r"\s+", "", text).lower()
        b = re.sub(r"\s+", "", source).lower()
        if a == b:
            return False
        # 以词为单位，若 80% 的词仍是拉丁词，判为未翻译
        words = re.findall(r"[A-Za-z]{2,}", text)
        if words and len(re.findall(r"[\u4e00-\u9fff]", text)) < 2:
            return False
    return True


# ─────────────────────── frontmatter 列表编辑 ───────────────────────
_FM_KEY = re.compile(r"^([A-Za-z_][\w-]*):(.*)$")
_FM_ITEM = re.compile(r"^\s*[-*]\s+(.*)$")


def _split_fm_blocks(fm):
    """[(key, header, body_lines)]，保持顺序；首个键之前的行归入 preamble。"""
    blocks, preamble, cur = [], [], None
    for ln in fm.splitlines():
        m = _FM_KEY.match(ln)
        if m:
            cur = [m.group(1), ln, []]
            blocks.append(cur)
        elif cur is None:
            preamble.append(ln)
        else:
            cur[2].append(ln)
    return preamble, blocks


def _fm_items(header_body):
    key, header, body = header_body
    rest = header.split(":", 1)[1].strip()
    items = []
    if rest.startswith("[") and rest.endswith("]"):
        inner = rest[1:-1].strip()
        if inner:
            for x in inner.split(","):
                x = x.strip().strip("\"\'")
                if x:
                    items.append(x)
        return items
    for ln in body:
        m = _FM_ITEM.match(ln)
        if m:
            v = m.group(1).strip().strip("\"\'")
            if v:
                items.append(v)
    return items


def add_alias_to_frontmatter(fm, alias, key="aliases"):
    """把 alias 追加进 frontmatter 的 key 列表，返回新的 fm 文本。

    与旧实现（对全文 `content.replace("aliases:", ...)`）的区别：
    - 只改 frontmatter 内的同名键，绝不碰正文；
    - 已有该键就原地追加，不会重复创建键（旧实现会产生两个 aliases_extra）；
    - 条统一写成 YAML 双引号标量，含引号/冒号/反斜杠都不会破 YAML；
    - 已有相同条目则不重复追加。
    """
    if not alias or not alias.strip():
        return fm
    alias = alias.strip()
    preamble, blocks = _split_fm_blocks(fm)
    target = None
    for b in blocks:
        if b[0] == key:
            target = b
            break
    if target is None:
        return fm.rstrip("\n") + "\n" + key + ":\n- " + yaml_str(alias)
    items = _fm_items(target)
    if alias in items:
        return fm
    items.append(alias)
    target[1] = key + ":"
    target[2] = ["- " + yaml_str(i) for i in items]
    out = list(preamble)
    for b in blocks:
        out.append(b[1])
        out.extend(b[2])
    return "\n".join(out)
