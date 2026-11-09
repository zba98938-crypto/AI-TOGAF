#!/usr/bin/env python3
"""Compare the local TOGAF guide suite to current capability entrypoints.

Appendix name coverage, routing and source semantics remain separate conclusions.
"""
import argparse
from collections import Counter
import re
import unicodedata
from pathlib import Path
import json

from adm import ROOT, contracts, load, write_new
from architecture_delivery import catalog
from evidence_integrity import sha
from registry import load as registry


def normalized(value):
    return re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKC', value).lower())


def compare(source_root):
    source_root = Path(source_root)
    source = source_root / 'togaf-standard-10th-zh/G248e_构建块的选择方法.md'
    text = source.read_text(encoding='utf-8')
    arts, dels, profiles, methods = registry()
    base = {a['id']: a for a in load(ROOT / 'artifacts.json')['artifacts']}
    rows = []
    for appendix, following, candidates, kind in [('A', 'B', base, 'artifact'), ('B', 'C', dels, 'deliverable')]:
        body = text.split('## 附录 ' + appendix + '：', 1)[1].split('## 附录 ' + following + '：', 1)[0]
        index = {normalized(a['name_en']): a['id'] for a in candidates.values()}
        # The local table uses a shortened English name; its Chinese row explicitly
        # includes "for Enterprise Architecture". Preserve the alias as an observation.
        if kind == 'deliverable':
            index[normalized('Organization Model')] = 'organization-model'
        for line in body.splitlines():
            if not line.startswith('|'):
                continue
            match = re.search(r'（([^（）]*[A-Za-z][^（）]*)）\s*\|$', line)
            if not match:
                continue
            name = match.group(1)
            identity = index.get(normalized(name))
            record = candidates.get(identity, {})
            rows.append({'kind': kind, 'source_name': name, 'source_row': line,
                         'source_locator': 'G248 Appendix ' + appendix,
                         'id': identity, 'owner': record.get('owner'),
                         'definition_exists': bool(identity and (ROOT / 'references' /
                             ('artifacts' if kind == 'artifact' else 'deliverables') / (identity + '.md')).is_file()),
                         'conclusion': 'name-mapped-definition-not-certified' if identity else 'unmapped'})
    suite = []
    for path in sorted((source_root / 'togaf-standard-10th-zh').glob('G*.md')):
        guide = path.name.split('e_', 1)[0]
        linked = {a['id']: a for group in (list(arts.values()), list(profiles.values()), methods)
                  for a in group if any(guide in str(ref) for ref in a.get('source_refs', a.get('sources', [])))}
        pdf = source_root / 'togaf-standard-10th' / (guide + 'e.pdf')
        suite.append({'id': guide, 'path': str(path.relative_to(source_root)), 'sha256': sha(path),
                      'english_pdf_present': pdf.is_file(),
                      'english_pdf_sha256': sha(pdf) if pdf.is_file() else None,
                      'capability_ids': sorted(linked),
                      'owner_skills': sorted({a['owner'] for a in linked.values()})})
    errors = [r for r in rows if not r['id'] or not r['definition_exists']]
    for kind, expected in [('artifact', set(base)), ('deliverable', set(dels))]:
        mapped = {r['id'] for r in rows if r['kind'] == kind and r['id']}
        if mapped != expected:
            errors.append({'kind': kind, 'source_only': sorted(mapped - expected),
                           'registry_only': sorted(expected - mapped)})
    return {'schema_version': 'togaf-delivery-comparison-1.0',
            'source_sha256': sha(source), 'counts': catalog()['counts'],
            'registry_sha256': {name: sha(ROOT / name) for name in
                               ('artifacts.json', 'deliverables.json', 'capabilities.json', 'references/adm-phases.json')},
            'comparison_script_sha256': sha(Path(__file__)),
            'source_guide_count': len(suite), 'appendix_rows': len(rows),
            'unique_appendix_items': dict(Counter(kind for kind, identity in
                {(r['kind'], r['id']) for r in rows if r['id']})),
            'errors': errors, 'appendix_comparison': rows, 'guide_routing': suite,
            'adm_contracts': contracts(),
            'limitations': ['名称覆盖不是逐字段定义等价或源图视觉通过。',
                           '本地套件是 Series Guides；未提供 C220 基础标准完整正文。',
                           'ADM 合同和路由是有来源依据的项目实现约定，按关注点裁剪。',
                           '机器检查不授予专业质量、利益相关者批准或生产收益。']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', required=True)
    parser.add_argument('--out')
    args = parser.parse_args()
    result = compare(args.source_root)
    output = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if args.out:
        write_new(args.out, output)
    print(output, end='')
    return int(bool(result['errors']))


if __name__ == '__main__':
    raise SystemExit(main())
