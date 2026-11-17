#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""phase9: 为概念页补充中文标题别名（安全版，2026-11-02 重写）。

旧实现（被替换）有三个会造成不可逆损坏的缺陷，均已线上复现：

1. 覆盖 H1。旧代码 `re.sub(r"^# .+$\n\n", f"# {zh}\n\n> {en}\n\n", content)`
   把页面一级标题换成中文；而 zh 来自 simple_translate —— 一个逐词替换的
   词语沙拉生成器，于是 H1 变成
     "A 全面 分析 of transcriptome and phenolic compound profiles …"
   原文英文标题从 H1 消失。实测 335 页 H1 含中文，其中 144 页是这类沙拉。
2. 盲字符串替换。`content.replace("aliases:", f'aliases: ["{zh}"]\naliases_extra:')`
   会在正文里替换所有出现处，并且每跑一次就多造一个 aliases_extra 键
   （PyYAML 重复键静默覆盖，校验查不出）。实测 84 页因此带两个 aliases_extra。
3. 不校验译文。MyMemory 配额耗尽时把错误说明放进 translatedText 且
   responseStatus=200，旧代码只判 len>5，于是
     "MYMEMORY WARNING: YOU USED ALL AVAILABLE FREE TRANSLATIONS FOR TODAY…"
   被当成中文别名写入。实测 711 条。

本版行为：
- 只往 frontmatter 的 aliases 里追加中文标题，绝不改动正文与 H1；
- 译文必须通过 text_utils.looks_translated()（含 CJK、非报错串、非原文回显）；
- 失败则跳过并计入 failed，不再用词语沙拉兜底；
- 写入走 text_utils.add_alias_to_frontmatter()，YAML 双引号转义、不重复建键。
"""
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime

from kb_paths import BASE
from text_utils import add_alias_to_frontmatter, looks_translated, is_translation_noise

CONCEPTS_DIR = os.path.join(BASE, "concepts", "papers")

CJK = re.compile(r"[\u4e00-\u9fff]")


def translate_mymemory(text, timeout=15):
    """调 MyMemory。返回 None 表示失败或结果不可信。"""
    try:
        import urllib.parse
        encoded = urllib.parse.quote(text[:500])
        url = ("https://api.mymemory.translated.net/get?q=%s&langpair=en|zh" % encoded)
        r = subprocess.run(["curl", "-sL", "--connect-timeout", "10", url],
                           capture_output=True, text=True, timeout=timeout)
        if r.returncode != 0:
            return None
        data = json.loads(r.stdout)
        status = data.get("responseStatus")
        result = (data.get("responseData") or {}).get("translatedText", "") or ""
        if status not in (200, "200", None):
            return None
        if not looks_translated(result, source=text):
            return None
        return result.strip()
    except Exception:
        return None


def page_created(path):
    """读取概念页 frontmatter 中的 created 日期（YYYY-MM-DD），缺失返回空串。"""
    try:
        with open(path, encoding="utf-8", errors="ignore") as f:
            head = f.read(1500)
    except Exception:
        return ""
    m = re.search(r"^created:\s*(\d{4}-\d{2}-\d{2})", head, re.M)
    return m.group(1) if m else ""


def parse_date_filter(argv):
    if "--today" in argv:
        return datetime.now().strftime("%Y-%m-%d")
    for i, a in enumerate(argv):
        if a == "--date" and i + 1 < len(argv):
            return argv[i + 1]
        if a.startswith("--date="):
            return a.split("=", 1)[1]
    return None


def frontmatter_and_body(text):
    if not text.startswith("---"):
        return None, None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, None
    return parts[1], parts[2]


def title_of(fm):
    m = re.search(r"^title:\s*(.+)$", fm, re.M)
    if not m:
        return ""
    return m.group(1).strip().strip("\"\'")


def main():
    date_filter = parse_date_filter(sys.argv[1:])
    dry = "--dry-run" in sys.argv[1:]
    if date_filter:
        print("仅处理 created=%s 的概念页" % date_filter)

    todo = []
    for fname in sorted(os.listdir(CONCEPTS_DIR)):
        if not fname.endswith(".md"):
            continue
        path = os.path.join(CONCEPTS_DIR, fname)
        if date_filter and page_created(path) != date_filter:
            continue
        try:
            with open(path, encoding="utf-8") as f:
                text = f.read()
        except Exception:
            continue
        fm, _ = frontmatter_and_body(text)
        if fm is None:
            continue
        title = title_of(fm)
        # 只处理英文学术标题；已有 CJK 标题说明是中文来源页，跳过
        if not title or CJK.search(title) or len(title) < 15:
            continue
        # 已在 aliases/aliases_extra 里出现过中文的，跳过，避免重复翻译
        if re.search(r"[\u4e00-\u9fff]", fm):
            continue
        todo.append((fname, title))

    print("Files to translate: %d" % len(todo))
    if dry:
        for fname, title in todo[:20]:
            print("  would translate:", fname, "|", title[:80])
        return 0

    translated = failed = 0
    for fname, en_title in todo:
        zh = translate_mymemory(en_title)
        if not zh:
            failed += 1
            time.sleep(0.3)
            continue
        path = os.path.join(CONCEPTS_DIR, fname)
        with open(path, encoding="utf-8") as f:
            text = f.read()
        fm, body = frontmatter_and_body(text)
        if fm is None:
            continue
        new_fm = add_alias_to_frontmatter(fm, zh, key="aliases")
        if new_fm == fm:
            continue
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write("---\n" + new_fm + "\n---" + body)
        translated += 1
        if translated % 20 == 0:
            print("  Translated %d..." % translated)
        time.sleep(0.3)

    print("\nTranslated: %d/%d (failed %d)" % (translated, len(todo), failed))
    return 0


if __name__ == "__main__":
    sys.exit(main())
