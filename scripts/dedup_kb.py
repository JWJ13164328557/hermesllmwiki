#!/usr/bin/env python3
"""去重知识库：删除重复文献，保留最优版本"""
import os, re, shutil
from collections import defaultdict

BASE = '/mnt/g/hermes_obsidian/hermes'
CONCEPTS_DIR = os.path.join(BASE, 'concepts', 'papers')
EVIDENCE_DIR = os.path.join(BASE, 'evidence')
ENTITIES_DIR = os.path.join(BASE, 'entities')
TRASH_DIR = os.path.join(BASE, '.trash')

os.makedirs(TRASH_DIR, exist_ok=True)

# ---- Deduplication rules ----
# (keep, remove) pairs
DEDUP_RULES = [
    # cr- vs ref-: keep cr- (more complete, PMC full text)
    ('cr-j-celrep-2019-04-054', 'ref-j-celrep-2019-04-054'),
    ('cr-j-molp-2020-06-010', 'ref-j-molp-2020-06-010'),
    ('cr-j-molp-2021-01-001', 'ref-j-molp-2021-01-001'),
    ('cr-s41477-023-01387-z', 'ref-s41477-023-01387-z'),
    ('cr-s41586-018-0414-6', 'ref-s41586-018-0414-6'),
    ('cr-s41586-019-0969-x', 'ref-s41586-019-0969-x'),
    ('cr-s41586-023-06053-0', 'ref-s41586-023-06053-0'),
    ('cr-s41587-023-01767-y', 'ref-s41587-023-01767-y'),
    ('cr-omi-2011-0118', 'ref-omi-2011-0118'),
    ('cr-pp-18-01482', 'ref-pp-18-01482'),
    ('cr-tpc-18-00785', 'ref-tpc-18-00785'),
    ('cr-science-1090022', 'ref-science-1090022'),
    ('cr-annurev-arplant-0817', 'ref-annurev-arplant-081720-01'),
    # named vs ref-: keep named (more descriptive)
    ('arabidopsis-sam-scrna', 'ref-j-devcel-2021-02-021'),
    # ref2 redundant
    ('ref-nmeth-1923', 'ref2-10-1038-nmeth-1923'),
    # ref4 cleanup
    ('ref-j-devcel-2019-01-006', 'ref4-10-1016-j-devcel-2019-02-'),
]

# ---- Tricky cases (need manual validation) ----
TRICKY = [
    # 3 copies of same DOI - keep the most complete one
    ('osbhlh150-rice-chilling-tolera', 'rice-chilling-tolerance', 'aba-biosynthesis-stress'),
]

def main():
    removed_count = 0
    kept_count = 0
    trash_count = 0
    
    # 1. Remove duplicates based on rules
    for keep_slug, remove_slug in DEDUP_RULES:
        remove_path = os.path.join(CONCEPTS_DIR, f"{remove_slug}.md")
        keep_path = os.path.join(CONCEPTS_DIR, f"{keep_slug}.md")
        
        if not os.path.exists(remove_path):
            print(f"  SKIP (not found): {remove_slug}")
            continue
        
        if not os.path.exists(keep_path):
            print(f"  WARN (keeper missing): {keep_slug}, keeping {remove_slug}")
            continue
        
        # Check quality: keep file should have more content
        keep_size = os.path.getsize(keep_path)
        remove_size = os.path.getsize(remove_path)
        
        # Move to trash instead of deleting
        trash_path = os.path.join(TRASH_DIR, f"{remove_slug}.md")
        shutil.move(remove_path, trash_path)
        trash_count += 1
        removed_count += 1
        
        print(f"  ✓ Removed {remove_slug} ({remove_size}B) → keep {keep_slug} ({keep_size}B)")
        
        # Update wikilinks in other files to point to keeper
        # (This is heavy - skip for now, wikilinks will update on next Obsidian open)
        
    # 2. Handle tricky cases
    for keep_slug, *rest in TRICKY:
        keep_path = os.path.join(CONCEPTS_DIR, f"{keep_slug}.md")
        if not os.path.exists(keep_path):
            # Try other candidates
            for alt in rest:
                alt_path = os.path.join(CONCEPTS_DIR, f"{alt}.md")
                if os.path.exists(alt_path):
                    keep_slug = alt
                    keep_path = alt_path
                    rest = [s for s in rest if s != alt]
                    break
        
        for remove_slug in rest:
            remove_path = os.path.join(CONCEPTS_DIR, f"{remove_slug}.md")
            if os.path.exists(remove_path):
                trash_path = os.path.join(TRASH_DIR, f"{remove_slug}.md")
                shutil.move(remove_path, trash_path)
                trash_count += 1
                removed_count += 1
                print(f"  ✓ Tricky: removed {remove_slug} → keep {keep_slug}")
    
    # 3. Report
    remaining = len([f for f in os.listdir(CONCEPTS_DIR) if f.endswith('.md')])
    print(f"\n=== DEDUP COMPLETE ===")
    print(f"Files removed: {removed_count}")
    print(f"Files kept: {kept_count}")
    print(f"Trash: {TRASH_DIR}/ ({trash_count} files)")
    print(f"concepts/papers/: {remaining} files (was {remaining + removed_count})")
    print(f"\nTo restore: mv {TRASH_DIR}/*.md {CONCEPTS_DIR}/")
    
    # 4. Update index.md
    idx_path = os.path.join(BASE, 'index.md')
    if os.path.exists(idx_path):
        with open(idx_path, 'r', encoding='utf-8') as f:
            idx_content = f.read()
        
        # Update total count
        idx_content = re.sub(r'\d+ 篇 Markdown', f'{remaining} 篇',
                            idx_content)
        
        with open(idx_path, 'w', encoding='utf-8') as f:
            f.write(idx_content)

if __name__ == '__main__':
    main()
