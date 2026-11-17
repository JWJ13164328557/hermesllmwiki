#!/usr/bin/env python3
"""Phase 6 v2: Extract relationships from evidence frontmatter genes/compounds fields"""
import os, re
from collections import defaultdict, Counter
from datetime import datetime

from kb_paths import BASE  # 统一根目录解析: KB_BASE/APP_DIR 环境变量优先
EVIDENCE_DIR = os.path.join(BASE, 'evidence')
REL_DIR = os.path.join(BASE, 'relationships')

os.makedirs(REL_DIR, exist_ok=True)
TODAY = datetime.now().strftime('%Y-%m-%d')

def main():
    # Build gene→compound relationships from evidence frontmatter
    gene_compound = defaultdict(Counter)  # gene → {compound: count}
    gene_gene = defaultdict(Counter)      # gene → {gene2: count}
    gene_evidence = defaultdict(list)     # gene → [evidence_ids]
    ev_paper = {}                         # evidence_id → 论文键(pmid/doi)
    
    ev_processed = 0
    for fname in sorted(os.listdir(EVIDENCE_DIR)):
        if not fname.endswith('.md'): continue
        path = os.path.join(EVIDENCE_DIR, fname)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read(5000)
        except: continue
        
        if 'created: 2026-05-30' not in content:
            # 2026-08-25 修复: 原硬编码只处理 2026-05-30 创建的证据(反模式),
            # 导致后续 evidence 全被跳过 → relationships 层一直为空(审稿 B4 发现)
            pass  # 移除日期硬编码过滤, 处理全部 evidence
        
        # 与 batch_synthesis / batch_hypotheses 同一卫生门：无 DOI 的条目不是
        # "某篇论文的一条证据"，不参与统计。此前 relationships 扫 5741 条而
        # synthesis 只认 5740 条，差的就是这一条无 DOI 文件。
        if not re.search(r'^doi:\s*\S', content, re.M):
            continue

        ev_slug = fname.replace('.md', '')
        ev_processed += 1
        _pm = re.search(r'^pmid:\s*(\S+)', content, re.M)
        _dm = re.search(r'^doi:\s*(\S+)', content, re.M)
        ev_paper[ev_slug] = (_pm.group(1) if _pm else '') or (_dm.group(1).strip('"') if _dm else '')
        
        # Extract genes from frontmatter
        gm = re.search(r'genes:\s*\[(.*?)\]', content)
        genes = []
        if gm and gm.group(1).strip():
            genes = [g.strip() for g in gm.group(1).split(',') if g.strip()]
        
        # Extract compounds from frontmatter
        cm = re.search(r'compounds:\s*\[(.*?)\]', content)
        compounds = []
        if cm and cm.group(1).strip():
            compounds = [c.strip() for c in cm.group(1).split(',') if c.strip()]
        
        # Build relationships
        for g in genes:
            gene_evidence[g].append(ev_slug)
            for c in compounds:
                gene_compound[g][c] += 1
            for g2 in genes:
                if g != g2:
                    gene_gene[g][g2] += 1
    
    print(f"Evidence processed: {ev_processed}")
    print(f"Unique genes: {len(gene_evidence)}")
    print(f"Gene-compound pairs: {sum(len(v) for v in gene_compound.values())}")
    
    # 1. Create gene→compound relationship page
    gc_rows = []
    for gene, compounds in sorted(gene_compound.items(), key=lambda x: -sum(x[1].values()))[:30]:
        top_compounds = compounds.most_common(5)
        ev_ids = gene_evidence.get(gene, [])[:5]
        ev_links = ', '.join(f'[[{e}]]' for e in ev_ids)
        comp_str = ', '.join(f'{c}({n})' for c, n in top_compounds)
        n_papers = len({ev_paper.get(e, e) for e in gene_evidence.get(gene, [])})
        gc_rows.append(f'| [[{gene.lower()}]] | {comp_str} | {sum(compounds.values())} | {n_papers} | {ev_links} |')
    
    gc_table = '\n'.join(gc_rows)
    gc_pair_count = sum(len(v) for v in gene_compound.values())
    
    gc_content = f"""---
title: "Gene-Compound Co-occurrence (Metabolism)"
created: {TODAY}
type: relationship
category: metabolism-gene-compound
tags: [metabolism, relationships]
relationship_kind: "co-occurrence"
evidence_basis: "shared-evidence-object"
causal_claim: false
used_for: "navigation-only"
---

# Gene–Compound Co-occurrence (Metabolism)

## Summary
Scanned {ev_processed} evidence objects; {len(gene_compound)} genes were co-mentioned with compounds, {gc_pair_count} gene-compound pairs retained.

> **语义边界**：本页只统计“同一证据对象中同时出现”，即共现，不是调控，也不是因果。共现强度不能用来推断基因控制该化合物的合成或积累。

## Top Gene-Compound Pairs
| Gene | Compounds | Evidence | 独立论文 | Source |
|------|-----------|----------|----------|--------|
{gc_table}

> `独立论文` 列是这套统计里最重要的质量控制：同一篇论文的 10 条证据只算 1 篇。
> 若“Evidence”很大而“独立论文”很小，说明该关联由单篇论文反复描述，不能当独立复现。

## 使用限制（机器可读）
- `relationship_kind: co-occurrence`
- `causal_claim: false`
- 本页只用于缩小人工核查范围；下游 synthesis / hypotheses 不得把本页当作调控或因果证据。

## Notes
- 生成范围：全库代谢主题证据（{TODAY} 重算）
- 关联强度 = 同一证据对象中的共现次数，**不是调控强度**
- 候选排序用途：用于缩小人工核查范围，不得直接写入机制结论
"""
    with open(os.path.join(REL_DIR, 'metabolism-gene-compound.md'), 'w', encoding='utf-8') as f:
        f.write(gc_content)
    
    # 2. Create gene co-occurrence network page
    gg_rows = []
    for gene, partners in sorted(gene_gene.items(), key=lambda x: -sum(x[1].values()))[:30]:
        top_partners = partners.most_common(5)
        partner_str = ', '.join(f'{p}({n})' for p, n in top_partners if sum(partners.values()) > 1)
        if partner_str:
            ev_ids = gene_evidence.get(gene, [])[:3]
            ev_links = ', '.join(f'[[{e}]]' for e in ev_ids)
            n_papers = len({ev_paper.get(e, e) for e in gene_evidence.get(gene, [])})
            gg_rows.append(f'| [[{gene.lower()}]] | {partner_str} | {n_papers} | {ev_links} |')
    
    gg_table = '\n'.join(gg_rows[:25])
    
    gg_content = f"""---
title: "Gene Co-occurrence Network (Metabolism)"
created: {TODAY}
type: relationship
category: metabolism-gene-gene
tags: [metabolism, relationships, network]
relationship_kind: "co-occurrence"
evidence_basis: "shared-evidence-object"
causal_claim: false
used_for: "navigation-only"
---

# Gene–Gene Co-occurrence Network (Metabolism)

## Summary
Genes frequently mentioned together in the same evidence objects.

> **语义边界**：共现只提示“可能相关”，不是调控，也不是物理互作、遗传上位或同一通路因果。

| Gene | Co-occurring Genes | 独立论文 | Source |
|------|--------------------|----------|--------|
{gg_table}

## 使用限制（机器可读）
- `relationship_kind: co-occurrence`
- `causal_claim: false`
- 本页只用于缩小人工核查范围；下游 synthesis / hypotheses 不得把本页当作调控或因果证据。

## Notes
- 共现不是调控，也不等于直接互作或因果
- 生成范围：{ev_processed} 个代谢主题证据对象（{TODAY} 重算）
- 仅用于候选排序与人工核查
"""
    with open(os.path.join(REL_DIR, 'metabolism-gene-network.md'), 'w', encoding='utf-8') as f:
        f.write(gg_content)
    
    rel_created = 2
    print(f"Relationship pages: {rel_created}")
    
    # 3. Top genes summary
    top_genes = sorted(gene_evidence.items(), key=lambda x: -len(x[1]))[:30]
    print(f"\nTop genes:")
    for g, evs in top_genes[:15]:
        n_compounds = len(gene_compound.get(g, {}))
        print(f"  {g}: {len(evs)} evidence, {n_compounds} compounds")
    
    # 4. Update index.md
    idx_path = os.path.join(BASE, 'index.md')
    with open(idx_path, 'r', encoding='utf-8') as f:
        idx_content = f.read()
    
    relationships_section = '\n## Relationships\n- [[metabolism-gene-compound]] — Gene–Compound Co-occurrence (not regulation)\n- [[metabolism-gene-network]] — Gene Co-occurrence Network\n'
    if '## Relationships' not in idx_content:
        idx_content += relationships_section
    else:
        # replace existing
        idx_content = re.sub(r'## Relationships.*?(?=\n## |\Z)', relationships_section.strip(), idx_content, flags=re.DOTALL)
    
    with open(idx_path, 'w', encoding='utf-8') as f:
        f.write(idx_content)
    
    # 5. Log
    log_path = os.path.join(BASE, 'log.md')
    with open(log_path, 'r', encoding='utf-8') as f:
        log_content = f.read()
    
    log_content += f"""
### Relationships ({TODAY})
- metabolism-gene-compound: {len(gene_compound)} genes / {gc_pair_count} pairs
- metabolism-gene-network: gene co-occurrence from {ev_processed} evidence
- Top gene: {top_genes[0][0]} ({len(top_genes[0][1])} evidence)
"""
    
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(log_content)
    
    print(f"\n=== DONE ===")
    print(f"Relationships: 2 pages")
    print(f"Gene-compound pairs: {sum(len(v) for v in gene_compound.values())}")
    print(f"Genes with evidence: {len(gene_evidence)}")

if __name__ == '__main__':
    main()
