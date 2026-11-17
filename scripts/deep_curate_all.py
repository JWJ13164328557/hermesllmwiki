#!/usr/bin/env python3
"""全量深度提炼：扫描 raw/ 所有 PDF → 匹配概念页 → 提取物种/方法/发现 → 更新概念页"""
import io, os, re, sys, subprocess

from kb_paths import BASE  # 统一根目录解析: KB_BASE/APP_DIR 环境变量优先
from species_patterns import order_species  # 物种识别唯一权威表（规范名+同义写法）
import article_kind
import themes as theme_mod
CONCEPTS_DIR = os.path.join(BASE, 'concepts', 'papers')
RAW_DIR = os.path.join(BASE, 'raw')

METHOD_PATTERNS = [
    (r'\b(RNA-seq|RNAseq|transcriptom(ic|e)\s+(analysis|profiling|sequenc))\b', 'transcriptomics (RNA-seq)'),
    (r'\b(metabolom(ic|e)\s+(analysis|profiling)|LC-MS|GC-MS|UPLC-MS|HPLC-MS)\b', 'metabolomics (LC-MS/GC-MS)'),
    (r'\b(multi-omics|multiomics|integrated\s+omics|integrative\s+omics)\b', 'multi-omics integration'),
    (r'\b(proteom(ic|e)\s+(analysis|profiling))\b', 'proteomics'),
    (r'\b(whole-genome\s+sequenc|genome\s+assembly|genome\s+annotation|genome-wide\s+analysis)\b', 'genomics'),
    (r'\b(single-cell\s+RNA|scRNA-seq|single\s+nucleus\s+RNA|snRNA-seq)\b', 'single-cell RNA-seq'),
    (r'\b(spatial\s+transcriptom|Stereo-seq|Visium|MERFISH|spatial\s+omics)\b', 'spatial transcriptomics'),
    (r'\b(ATAC-seq|scATAC-seq|single-cell\s+ATAC)\b', 'ATAC-seq'),
    (r'\b(ChIP-seq|ChIP-qPCR|chromatin\s+immunoprecipitation)\b', 'ChIP-seq/qPCR'),
    (r'\b(qRT-PCR|qPCR|real-time\s+PCR|quantitative\s+PCR)\b', 'qRT-PCR validation'),
    (r'\b(Y2H|yeast\s+two-hybrid|yeast\s+2-hybrid)\b', 'Y2H'),
    (r'\b(BiFC|bimolecular\s+fluorescence)\b', 'BiFC'),
    (r'\b(Co-IP|co-immunoprecipitation|coimmunoprecipitation)\b', 'Co-IP'),
    (r'\b(EMSA|electrophoretic\s+mobility\s+shift)\b', 'EMSA'),
    (r'\b(dual-luciferase|dual\s+luciferase|luciferase\s+reporter|LUC\s+assay)\b', 'dual-luciferase reporter'),
    (r'\b(CRISPR|Cas9|gene\s+editing|genome\s+editing)\b', 'CRISPR/Cas9'),
    (r'\b(RNAi|RNA\s+interference|gene\s+silencing|VIGS|virus-induced\s+gene\s+silencing)\b', 'RNAi/VIGS'),
    (r'\b(overexpression|over-expression|transgenic\s+overexpression)\b', 'overexpression'),
    (r'\b(knockout|knock-out|mutant\s+analysis|T-DNA\s+insertion)\b', 'knockout/mutant'),
    (r'\b(Western\s+blot|immunoblot|protein\s+blot)\b', 'Western blot'),
    (r'\b(subcellular\s+localization|GFP\s+fusion|fluorescent\s+protein)\b', 'subcellular localization'),
    (r'\b(promoter\s+assay|GUS\s+staining|GUS\s+reporter)\b', 'promoter-GUS assay'),
    (r'\b(phylogenetic\s+analysis|evolutionary\s+analysis|phylogeny)\b', 'phylogenetics'),
    (r'\b(GWAS|genome-wide\s+association)\b', 'GWAS'),
    (r'\b(QTL|quantitative\s+trait\s+locus)\b', 'QTL mapping'),
]


def clean_pdf_text(text):
    """PDF 抽取后的最小清洗：修断词、并接被换行切断的句子。

    2026-11-03：回灌的全文直接进了「核心发现」，于是正文里出现
    "over- lapped"、"pro- moters" 这类断词，以及 "> <sub>" 之类的
    行尾残留。证据是要被引用进综述的，断词会污染行内引文。
    """
    if not text:
        return text
    # 1) 行尾连字符断词：alphabet-\nbeta -> alphabetbeta
    text = re.sub(r'([A-Za-z])-\s*\n\s*([a-z])', r'\1\2', text)
    # 2) 软换行：句中断行（下一行不是大写开头/编号/图注）-> 空格
    text = re.sub(r'(?<=[a-z,;])\s*\n\s*(?=[a-z(])', ' ', text)
    # 2b) PDF 抽取残留控制字符（0x01-0x08）：PyYAML 直接拒解析，
    #     写进 title 会让整页 frontmatter 失效（2026-11-03 实测 29 页）
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', ' ', text)
    # 3) 多余空白
    text = re.sub(r'[ \t]{2,}', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text


def extract_fulltext(pdf_path):
    """取全文：PDF 走 pymupdf（前 15 页），.txt 走纯文本（Europe PMC JATS 转写）。

    2026-11-02：Europe PMC 的两个 PDF 端点对脚本请求返回 403，PDF 通道当日
    0/37；同一篇文献的 fullTextXML 仍可取到，转成 .txt 后由本函数读取。
    """
    if str(pdf_path).lower().endswith('.txt'):
        try:
            with open(pdf_path, encoding='utf-8', errors='ignore') as fh:
                text = fh.read()
            if len(text.strip()) > 200:
                return text[:50000]
        except Exception as e:
            print(f"  ⚠ extract failed: {os.path.basename(pdf_path)[:50]}: {e}",
                  file=sys.stderr)
        return ''
    try:
        import fitz
        doc = fitz.open(pdf_path)
        text = ''
        for page in doc[:15]:
            text += page.get_text()
        doc.close()
        if len(text.strip()) > 200:
            return clean_pdf_text(text)[:50000]
    except Exception as e:
        print(f"  ⚠ extract failed: {os.path.basename(pdf_path)[:50]}: {e}", file=sys.stderr)
    return ''


def extract_findings(text):
    """Extract key findings from full text"""
    sentences = re.split(r'(?<=[.!?])\s+', text)
    signal_patterns = [
        (r'\b(we\s+(found|show|demonstrat|reveal|identif|discover|observ|confirm|conclude|report|uncover))\b', 5),
        (r'\b(our\s+(results|data|findings|study|analysis)\s+(show|demonstrat|reveal|indicat|suggest|confirm|support))\b', 5),
        (r'\b(these\s+(results|data|findings)\s+(show|demonstrat|reveal|indicat|suggest|confirm))\b', 4),
        (r'\b(this\s+study\s+(reveals|demonstrates|shows|identifies|provides|uncovers|establishes))\b', 4),
        (r'\b((importantly|notably|interestingly|surprisingly|strikingly|remarkably)\s*,)', 3),
        (r'\b((taken\s+together|in\s+conclusion|in\s+summary|collectively)\s*,)', 4),
        (r'\b((is|are|was|were)\s+(required|necessary|essential|critical|crucial|sufficient|key)\s+(for|to))\b', 3),
        (r'\b((plays?\s+a\s+(critical|crucial|key|essential|important|pivotal|central)\s+role))\b', 4),
        (r'\b((directly|specifically|strongly|significantly)\s+(regulates|controls|modulates|activates|inhibits|suppresses|promotes|enhances))\b', 4),
        (r'\b((encodes|functions\s+as|acts\s+as)\s+a\s+(key|critical|novel|important))\b', 3),
        (r'\b((interacts?\s+with|binds?\s+to|phosphorylates?|ubiquitinates?|targets?)\s+[A-Z])', 4),
        (r'\b((overexpression|knockout|knockdown|silencing)\s+of\s+[A-Z].*?(resulted|led|increased|decreased|enhanced|reduced|promoted|inhibited))\b', 4),
        (r'\b((upregulation|downregulation|up-regulation|down-regulation)\s+of)\b', 2),
        (r'\b((provides?\s+(novel|new|important|critical)\s+(insights?|evidence|understanding)))\b', 3),
    ]
    scored = []
    for sent in sentences:
        sent = sent.strip()
        if len(sent) < 40 or len(sent) > 500:
            continue
        if re.match(r'^\s*(Figure|Fig|Table|Supplementary|et al|http|doi)', sent):
            continue
        if re.search(r'(et al\.?\s*,?\s*\d{4})', sent) and len(sent) < 100:
            continue
        score = 0
        for pattern, weight in signal_patterns:
            if re.search(pattern, sent, re.I):
                score += weight
        if score >= 3:
            clean = re.sub(r'\s+', ' ', sent).strip()
            # 去掉句首残留的引用编号/编号列表标记（"33 20 , Notably, ..."）
            clean = re.sub(r'^[\d\s,;:\[\]\.]+(?=[A-Z])', '', clean).strip()
            if '## ' in clean or len(clean) < 40:
                continue
            scored.append((score, clean[:400]))
    scored.sort(key=lambda x: -x[0])
    seen = set()
    findings = []
    for score, sent in scored:
        key = sent[:80]
        if key not in seen:
            seen.add(key)
            findings.append(sent)
        if len(findings) >= 8:
            break
    return findings


def _file_mentions_doi(path, doi, max_bytes=200000):
    """确认文件确实属于该 DOI（防 glob 误配）。"""
    try:
        if path.lower().endswith('.txt'):
            with open(path, encoding='utf-8', errors='ignore') as fh:
                head = fh.read(max_bytes)
        else:
            import fitz
            doc = fitz.open(path)
            head = ''
            for page in doc[:3]:
                head += page.get_text()
            doc.close()
    except Exception:
        return False
    norm = lambda x: re.sub(r'\s+', '', x).lower()
    return norm(doi) in norm(head)


def _frontmatter(text):
    if not text.startswith('---'):
        return ''
    end = text.find('\n---', 3)
    return text[3:end] if end > 0 else ''


def _fm_set(fm, key, value):
    pat = re.compile(r'^%s\s*:.*$' % re.escape(key), re.M)
    line = '%s: %s' % (key, value)
    return pat.sub(line, fm, count=1) if pat.search(fm) else fm.rstrip('\n') + '\n' + line + '\n'


def _fm_get(fm, key):
    m = re.search(r'^%s\s*:\s*(.*)$' % re.escape(key), fm, re.M)
    return m.group(1).strip().strip('"') if m else ''


def main():
    # Parse --dois argument: comma-separated or file path
    target_dois = None
    args = sys.argv[1:]
    if '--dois' in args:
        idx = args.index('--dois')
        if idx + 1 < len(args):
            dois_arg = args[idx + 1]
            if os.path.exists(dois_arg):
                with open(dois_arg) as f:
                    target_dois = set(line.strip().rstrip('./') for line in f if line.strip())
            else:
                target_dois = set(d.strip().rstrip('./') for d in dois_arg.split(',') if d.strip())

    # --pdf-map FILE : TSV  doi<TAB>page<TAB>pdf
    # 2026-11-03：回灌通道此前把「已解析好的 PDF→页面」三元组丢掉，交给
    # 本脚本再猜一次文件名，63 个目标只猜中 7 个（其余因前缀/后缀差异漏配）。
    # 现在由调用方直接给出确定的映射，本脚本不再二次解析。
    pdf_map_rows = None
    page_override = {}
    if '--pdf-map' in args:
        idx = args.index('--pdf-map')
        if idx + 1 < len(args):
            rows = []
            with io.open(args[idx + 1], encoding='utf-8') as fh:
                for line in fh:
                    parts = line.rstrip("\n").split("\t")
                    if len(parts) < 3:
                        continue
                    doi, page, pdf = parts[0].strip(), parts[1].strip(), parts[2].strip()
                    if not doi or not pdf or not os.path.exists(pdf):
                        continue
                    key = doi.rstrip('./')
                    page_override[key] = page
                    rows.append((pdf, key))
            pdf_map_rows = rows
            print("  -> %d pairs from --pdf-map" % len(rows), file=sys.stderr)
    
    # Build DOI → concept mapping (scan BOTH concepts/ and concepts/papers/, dedup)
    print("Building DOI → concept mapping...", file=sys.stderr)
    # 2026-09-14: 补回/每日导入的概念页写在 concepts/ 顶层, 而此前只扫 concepts/papers/.
    # 两处都扫描: 顶层 + papers/ 子目录.
    scan_dirs = [CONCEPTS_DIR]
    top_dir = os.path.join(BASE, 'concepts')
    if os.path.isdir(top_dir) and os.path.abspath(top_dir) != os.path.abspath(CONCEPTS_DIR):
        scan_dirs.append(top_dir)
    doi_to_concept = {}
    for sdir in scan_dirs:
        if not os.path.isdir(sdir):
            continue
        for fname in os.listdir(sdir):
            if not fname.endswith('.md'):
                continue
            path = os.path.join(sdir, fname)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read(3000)
                dm = re.search(r'doi:\s*"?\s*(10\.\d{4,}/[^\s\n"\]\]]+)', content, re.I)
                if dm:
                    doi_to_concept.setdefault(dm.group(1).rstrip('/'), path)
            except:
                pass
    print(f"  → {len(doi_to_concept)} concept pages with DOI", file=sys.stderr)

    # Filter to target DOIs if specified
    if target_dois:
        # Normalize: strip trailing slashes/dots for matching
        normalized_targets = set(d.rstrip('./') for d in target_dois)
        doi_to_concept = {k: v for k, v in doi_to_concept.items() 
                          if k.rstrip('./') in normalized_targets}
        print(f"  → filtered to {len(doi_to_concept)} targets", file=sys.stderr)

    import glob as _glob

    matched = []
    if pdf_map_rows is not None:
        matched = pdf_map_rows
    elif target_dois:
        # Fast path: direct filename lookup per target DOI
        print(f"  -> fast lookup for {len(doi_to_concept)} target DOIs", file=sys.stderr)
        for doi in doi_to_concept:
            doi_clean = doi.rstrip('./')
            doi_slug = doi_clean.replace('/', '_')
            candidates = [doi_slug, doi_slug.replace('(', '').replace(')', '')]
            # journal abbreviation fix
            doi_abbrev = re.sub(
                r'/(pp|tpc|tpj|pbi|pcp|hr|nar|bib|nph|jxb|dev|jcs|ppl|pgen|pcbi|acel|jipb|genetics|fpls|fgene)_(\d)',
                r'/\1.\2', doi_slug)
            if doi_abbrev != doi_slug:
                candidates.append(doi_abbrev)

            # 2026-11-03：DOI 后缀容错。Annual Reviews 等期刊的页面 DOI 带
            # 文章号（...-042817-040549），而 PDF 常以短前缀命名
            # （10.1146_annurev-arplant-042817.pdf）。逐个剥掉末尾
            # `-segment` 生成候选，命中后仍由 _file_mentions_doi 校验。
            for extra in range(1, 4):
                parts = doi_slug.rsplit('-', extra)
                if len(parts) > 1:
                    cand = parts[0]
                    if cand not in candidates:
                        candidates.append(cand)

            found = None
            for fname in candidates:
                # 2026-08-24: PDF 已汇总到 papers/all_pdfs/，加入定位目录
                for subdir in ['', 'papers/', 'papers/metabolism/', 'papers/all_pdfs/']:
                    path = os.path.join(RAW_DIR, subdir, fname + '.pdf')
                    if os.path.exists(path):
                        found = path
                        break
                if not found:
                    # Europe PMC JATS 转写的全文（PDF 端点被 403 时的主通道）
                    for subdir in ['papers/fulltext/', 'papers/fulltext_trial/', '']:
                        path = os.path.join(RAW_DIR, subdir, fname + '.txt')
                        if os.path.exists(path):
                            found = path
                            break
                if found:
                    if _file_mentions_doi(found, doi_clean) or len(candidates) <= 2:
                        break
                    found = None
            if not found:
                # glob fallback（2026-11-03 修复）：旧实现把 slug 截到 50 字符，
                # 长 DOI 会命中**别的**论文的 PDF。现在用完整 slug，且命中后
                # 校验文件内确实出现该 DOI，否则丢弃。
                for pat in [f'**/*{doi_slug}*.pdf',
                            f'**/*{doi_slug.replace(".", "-")}*.pdf',
                            f'**/*{doi_slug}*.txt']:
                    hits = _glob.glob(os.path.join(RAW_DIR, pat), recursive=True)
                    ok = None
                    for h in hits:
                        if _file_mentions_doi(h, doi_clean):
                            ok = h
                            break
                    if ok:
                        found = ok
                        break
            if found:
                matched.append((found, doi))
        print(f"  -> {len(matched)} PDFs matched via fast lookup", file=sys.stderr)
    else:
        # Full scan (no --dois filter)
        # 2026-11-03: 全量扫描此前只收 .pdf，Europe PMC JATS 转写的
        # papers/fulltext/*.txt 全部漏掉——这类全文已有 1500+ 份，是当前
        # 深度提炼最容易回收的增量。这里把 .txt 一并纳入（跳过 _index.txt
        # 等下划线开头的索引/日志文件）。
        pdf_files = []
        for root, dirs, files in os.walk(RAW_DIR):
            for f in files:
                if f.startswith('_'):
                    continue
                if f.endswith('.pdf'):
                    pdf_files.append(os.path.join(root, f))
                elif f.endswith('.txt') and 'fulltext' in root.replace(os.sep, '/'):
                    pdf_files.append(os.path.join(root, f))
        print(f"  -> {len(pdf_files)} fulltext files found", file=sys.stderr)

        def doi_from_fname(fname):
            doi = fname.rsplit('.', 1)[0].replace('_', '/')
            doi = re.sub(
                r'/(pp|tpc|tpj|pbi|pcp|hr|nar|bib|nph|jxb|dev|jcs|ppl|pgen|pcbi|acel|jipb|genetics|fpls|fgene)/(\d)',
                r'/\1.\2', doi)
            return doi if re.match(r'10\.\d{4,}/', doi) else None

        for pdf_path in pdf_files:
            doi = doi_from_fname(os.path.basename(pdf_path))
            if doi and doi in doi_to_concept:
                matched.append((pdf_path, doi))
                continue
            try:
                import fitz
                doc = fitz.open(pdf_path)
                for page_num in range(min(3, len(doc))):
                    m = re.search(r'10\.\d{4,}/[^\s"\n\r\t]+', doc[page_num].get_text())
                    if m:
                        doi = m.group(0).rstrip('.,;:)')
                        if doi in doi_to_concept:
                            matched.append((pdf_path, doi))
                            break
                doc.close()
            except:
                pass

    print(f"  → {len(matched)} PDFs matched to concepts", file=sys.stderr)

    # 2026-11-03: 同一 DOI 可能同时有 PDF 和 JATS .txt，若都送去提炼，
    # 后一轮会用另一个来源覆盖前一轮，结果随 os.walk 顺序漂移。
    # 这里按 DOI 去重，优先 PDF（原始版面，含图表与正文主体）。
    _seen_doi = {}
    _ordered = []
    for _p, _d in matched:
        _k = _d.rstrip('./')
        _is_pdf = str(_p).lower().endswith('.pdf')
        if _k in _seen_doi:
            _prev_p = _seen_doi[_k]
            if _is_pdf and not str(_prev_p).lower().endswith('.pdf'):
                _ordered = [((_p, _d) if _d.rstrip('./') == _k else _x) for _x in _ordered]
                _seen_doi[_k] = _p
            continue
        _seen_doi[_k] = _p
        _ordered.append((_p, _d))
    if len(_ordered) != len(matched):
        print("  -> deduped to %d sources by DOI" % len(_ordered), file=sys.stderr)
    matched = _ordered

    # Deep curate
    curated = 0
    no_text = 0
    skipped_nonresearch = 0
    nonresearch_pages = 0
    for pdf_path, doi in matched:
        fulltext = extract_fulltext(pdf_path)
        if not fulltext:
            no_text += 1
            continue

        key = doi.rstrip('./')
        concept_path = page_override.get(key) or doi_to_concept.get(key)
        if not concept_path:
            print('  ! no concept page for', doi, file=sys.stderr)
            continue
        # 2026-11-03 修复：必须先读页面正文，再做标题/摘要判定。
        # 旧实现把 content 的读取放在判定之后，实际复用了上一轮（乃至 DOI
        # 索引循环）遗留的 content，导致物种与摘要张冠李戴。
        with open(concept_path, 'r', encoding='utf-8', errors='ignore') as fh:
            content = fh.read()

        fm = _frontmatter(content)
        page_title = ''
        tm = re.search(r'^# (.+)$', content, re.M)
        if tm:
            page_title = tm.group(1).strip()
        # 概念页正文（深度提炼之前的部分）通常就是这篇文献的中文摘要
        summary = content.split('## 深度提炼')[0]
        if len(summary) > 4000:
            summary = summary[:4000]
        journal = _fm_get(fm, 'journal')

        kind = article_kind.kind_of(fm)
        if kind == 'research':
            kind, _reasons = article_kind.classify(
                title=page_title, doi=doi, journal=journal, body=summary)
        eligible = article_kind.is_evidence_eligible(kind)

        # 2026-11-03 第18轮：物种字段曾被全文污染——一篇大豆疫霉(Phytophthora
        # sojae)论文仅因正文讨论提到 citrus，**物种** 行就多出 Citrus spp.，
        # 自检判为"文献描述与实际不符"。研究物种的判据应是题目/摘要；全文只在
        # 摘要判不出任何物种时兜底取最高频的单个物种。此口径与 evidence 层
        # primary_species（batch_evidence_objects 用 fulltext=''）保持一致。
        species = order_species(title=page_title, abstract=summary,
                                fulltext='', limit=5)
        # 摘要判不出物种时**不再**回退到全文 top-1：实测 6 例回退里 4 例错
        # （纳米银综述→Citrus、火星植树→Pinus、菊花多倍体→Citrus），错误物种
        # 会污染下游 primary_species 与假说。宁可留空并如实标注，也不猜。
        primary = species[0] if species and species != ['Plant (unspecified)'] else 'Plant'

        methods = []
        for pat, name in METHOD_PATTERNS:
            if re.search(pat, fulltext, re.I):
                methods.append(name)
        methods = list(dict.fromkeys(methods))[:8]
        if not methods:
            methods = ['molecular biology / biochemistry']

        if eligible:
            findings = extract_findings(fulltext)
            findings_str = ('\n'.join(f'{i+1}. {f}' for i, f in enumerate(findings))
                            if findings else '_（无显著信号句）_')
            body_block = '### 核心发现\n%s' % findings_str
        else:
            # 非研究页（更正/撤稿/社论/会员表/目录页）：不产出"核心发现"，
            # 只记录变更对象——这正是"提炼内容与文献实体不符"的根治点。
            findings = []
            nonresearch_pages += 1
            body_block = ('### 文献变更要点\n'
                          '文献类型为 `%s`，不属于可作证据的研究/综述，'
                          '不产出机制性发现。\n\n- 标题: %s\n- DOI: %s\n'
                          % (kind, page_title or '（缺）', doi))

        species_str = ', '.join(species) if species else '—'
        methods_str = ', '.join(methods)
        curation_new = f"""## 深度提炼

**主要物种**: {primary}
**物种**: {species_str}
**方法**: {methods_str}
**来源**: DOI:{doi}
**来源类型**: {('XML全文' if str(pdf_path).lower().endswith('.txt') else 'PDF全文')} ({os.path.basename(pdf_path)[:60]})

{body_block}
"""

        if '## 深度提炼' in content:
            content = re.sub(
                r'## 深度提炼.*?(?=\n## (?!深度)|## 相关文献|---\s*\n\Z|\Z)',
                lambda _m: curation_new.strip(),
                content, flags=re.DOTALL
            )
        else:
            ref_pos = content.find('## 相关文献')
            if ref_pos > 0:
                content = content[:ref_pos] + curation_new + '\n' + content[ref_pos:]
            else:
                content = content.rstrip() + '\n\n' + curation_new

        # 主题归属：用"标题 + 摘要 + 核心发现"作上下文，写规范 themes
        ctx = page_title + '\n' + summary + '\n' + ' '.join(findings[:4])
        tset, tbasis = theme_mod.assign_themes(
            _fm_get(fm, 'tags').strip('[]').split(','), ctx)
        tset = theme_mod.filter_supported_themes(tset, ctx)
        tset = set(list(tset)[:theme_mod.MAX_THEMES_PER_EVIDENCE])

        fm2 = _frontmatter(content)
        if fm2:
            end = content.find('\n---', 3)
            if tset:
                fm2 = _fm_set(fm2, 'themes', '[%s]' % ', '.join(sorted(tset)))
                fm2 = _fm_set(fm2, 'theme_status', 'mapped')
            elif _fm_get(fm2, 'themes') in ('', '[other]', 'other'):
                fm2 = _fm_set(fm2, 'themes', '[other]')
                fm2 = _fm_set(fm2, 'theme_status', 'out-of-scope')
            fm2 = _fm_set(fm2, 'theme_basis', tbasis or 'none')
            if not article_kind.is_evidence_eligible(article_kind.kind_of(fm2)):
                fm2 = _fm_set(fm2, 'article_kind', kind)
            content = '---' + fm2 + content[end:]

        with open(concept_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)

        curated += 1
        if curated % 100 == 0:
            print(f"  [{curated}/{len(matched)}] {primary}: {len(findings)} findings",
                  file=sys.stderr)

    print(f"\n=== DONE ===")
    print(f"Matched PDFs: {len(matched)}")
    print(f"Curated: {curated}")
    print(f"  of which non-research (no findings): {nonresearch_pages}")
    print(f"No text: {no_text}")


if __name__ == '__main__':
    main()
