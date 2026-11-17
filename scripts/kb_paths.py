#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""kb_paths.py — 知识库根目录的唯一解析入口。

解析优先级（从高到低）：
  1. 环境变量 KB_BASE
  2. 环境变量 APP_DIR（向后兼容）
  3. 由本文件位置推导：scripts/ 的父目录即仓库根

所有脚本必须从本模块导入 BASE，不得再写死绝对路径。
"""
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
_ENV_VARS = ('KB_BASE', 'APP_DIR')


def _resolve_base():
    for var in _ENV_VARS:
        raw = os.environ.get(var, '').strip()
        if not raw:
            continue
        path = os.path.abspath(os.path.expanduser(raw))
        if not os.path.isdir(path):
            raise SystemExit('[kb_paths] %s=%s 不存在或不是目录' % (var, path))
        return path
    return REPO_ROOT


BASE = _resolve_base()
LEGACY_CONCEPTS_DIR = os.path.join(BASE, 'concepts')          # 历史遗留：顶层 daily-*.md
CONCEPTS_DIR = os.path.join(BASE, 'concepts', 'papers')       # SCHEMA: 论文概念页唯一归属
METHODS_DIR = os.path.join(BASE, 'concepts', 'methods')
EVIDENCE_DIR = os.path.join(BASE, 'evidence')
ENTITIES_DIR = os.path.join(BASE, 'entities')
RELATIONSHIPS_DIR = os.path.join(BASE, 'relationships')
SYNTHESIS_DIR = os.path.join(BASE, 'synthesis')
HYPOTHESES_DIR = os.path.join(BASE, 'hypotheses')
PROGRAMS_DIR = os.path.join(BASE, 'research-programs')
RAW_DIR = os.path.join(BASE, 'raw')
PDF_DIR = os.path.join(RAW_DIR, 'papers', 'all_pdfs')
STATE_DIR = os.path.join(BASE, '.pipeline_state')
LOG_DIR = os.path.join(BASE, 'logs', 'pipeline')


def paper_path(slug):
    """论文概念页的标准写入路径（concepts/papers/<slug>.md）。"""
    return os.path.join(CONCEPTS_DIR, slug + '.md')


def find_paper(slug):
    """查找已存在的论文页：先新 schema，再兼容旧顶层位置。找不到返回 None。"""
    for base in (CONCEPTS_DIR, LEGACY_CONCEPTS_DIR):
        p = os.path.join(base, slug + '.md')
        if os.path.isfile(p):
            return p
    return None


def page_dir(slug):
    """新页应写入的目录（保证目录存在）。"""
    os.makedirs(CONCEPTS_DIR, exist_ok=True)
    return CONCEPTS_DIR


def ensure_runtime_dirs():
    """建立运行期目录（不触碰知识内容）。"""
    for path in (STATE_DIR, LOG_DIR):
        os.makedirs(path, exist_ok=True)
