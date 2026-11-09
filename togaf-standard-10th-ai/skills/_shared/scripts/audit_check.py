#!/usr/bin/env python3
"""Check full-text and figure review records for completeness before they are merged.

Passing proves that every indexed locator has one structured disposition from a
known vocabulary; it does not prove that the disposition or finding is correct.
"""
import argparse
import json
import sys
from pathlib import Path
from build_corpus_registry import guide_code, text_inventory

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT.parents[1]/'togaf-standard-10th-zh'
TEXT_DIR = ROOT/'reviews/full-text-reading'
FIGURE_DIR = ROOT/'reviews/figure-verification'
SECTION_DISPOSITIONS = {'capability-definition', 'method-procedure', 'rule-or-constraint', 'reference-model-content',
                        'worked-example', 'adm-mapping', 'context-or-rationale', 'navigation-heading',
                        'front-back-matter', 'glossary-or-index'}
CAPABILITY_BEARING = {'capability-definition', 'method-procedure', 'rule-or-constraint'}
TABLE_DISPOSITIONS = {'capability-content', 'method-scale-or-rules', 'reference-catalog', 'example-data',
                      'figure-label-table', 'glossary-or-abbreviation', 'document-list', 'other'}
ASSET_VERDICTS = {'faithful', 'minor-deviation', 'major-deviation', 'wrong-figure', 'incomplete', 'unreadable', 'not-applicable'}
JSON_VERDICTS = {'accurate', 'minor-errors', 'major-errors', 'not-verifiable'}
ROLES = {'architecture-view-source', 'method-illustration', 'reference-model-or-taxonomy', 'example-instance',
         'notation-or-legend', 'screenshot-or-photo', 'table-image', 'duplicate-of-other-figure', 'context-only'}

def known_ids():
    ids = {a['id'] for a in json.loads((ROOT/'artifacts.json').read_text())['artifacts']}
    ids |= {d['id'] for d in json.loads((ROOT/'deliverables.json').read_text())['deliverables']}
    cap = json.loads((ROOT/'capabilities.json').read_text())
    for key in ['work_products', 'profiles', 'analysis_methods']:ids |= {x['id'] for x in cap[key]}
    return ids

def guide_file(code):
    return next(p for p in CORPUS.glob('G*.md') if guide_code(p) == code)

def text_parts(code):
    parts, errors = [], []
    for path in sorted((TEXT_DIR/code).glob('part-*.json')):
        try:parts.append((path.name, json.loads(path.read_text())))
        except json.JSONDecodeError as error:errors.append({'file': path.name, 'error': 'invalid JSON: '+str(error)})
    return parts, errors

def check_text(code, start=1, end=None):
    inventory = text_inventory(guide_file(code), CORPUS);end = end or inventory['line_count'];ids = known_ids()
    all_s = {s['id'] for s in inventory['sections']};all_t = {t['id'] for t in inventory['tables']}
    expected_s = {s['id'] for s in inventory['sections'] if start <= s['line'] <= end}
    expected_t = {t['id'] for t in inventory['tables'] if start <= t['lines'][0] <= end}
    parts, errors = text_parts(code);seen = {}
    candidates = {c.get('candidate_id') for _, part in parts for c in part.get('new_capability_candidates', [])}
    def refs_ok(identity, refs):
        for ref in refs:
            if ref not in ids and ref not in candidates:errors.append({'id': identity, 'error': 'unknown capability ref '+str(ref)})
    for name, part in parts:
        for s in part.get('sections', []):
            seen.setdefault(str(s.get('id')), []).append(name)
            if s.get('disposition') not in SECTION_DISPOSITIONS:errors.append({'id': s.get('id'), 'error': 'section disposition'})
            if s.get('disposition') in CAPABILITY_BEARING and not s.get('capability_refs'):
                errors.append({'id': s.get('id'), 'error': 'capability-bearing section lacks capability_refs'})
            refs_ok(s.get('id'), s.get('capability_refs', [])+s.get('secondary_refs', []))
        for t in part.get('tables', []):
            seen.setdefault(str(t.get('id')), []).append(name)
            if t.get('disposition') not in TABLE_DISPOSITIONS:errors.append({'id': t.get('id'), 'error': 'table disposition'})
            refs_ok(t.get('id'), t.get('capability_refs', []))
        refs_ok('capability_evidence', [e.get('capability_id') for e in part.get('capability_evidence', [])])
        for c in part.get('new_capability_candidates', []):
            if not str(c.get('candidate_id', '')).startswith('new:'):errors.append({'id': c.get('candidate_id'), 'error': 'candidate id must start with new:'})
    report = {'guide': code, 'range': [start, end],
              'missing_sections': sorted(expected_s-seen.keys()), 'missing_tables': sorted(expected_t-seen.keys()),
              'duplicates': sorted(i for i, files in seen.items() if len(files) > 1),
              'unexpected_ids': sorted(seen.keys()-all_s-all_t), 'errors': errors}
    report['complete'] = not any(report[k] for k in ['missing_sections', 'missing_tables', 'duplicates', 'unexpected_ids', 'errors'])
    return report
def source_figures(code=None):
    result = {}
    for path in sorted((CORPUS/'figs/ai').glob('G*/*.json')):
        d = json.loads(path.read_text())
        if code is None or d['doc']['code'] == code:result[d['id']] = d
    return result

def image_assets(d):
    return {a['path'].split('#')[0] for a in d.get('assets', []) if a.get('path', '').split('#')[0].lower().endswith(('.png', '.svg'))}

def check_figures(code=None):
    errors, missing, records = [], [], {};ids = known_ids()
    for fid, d in source_figures(code).items():
        path = FIGURE_DIR/(fid.replace('/', '-')+'.json')
        if not path.exists():missing.append(fid);continue
        try:r = json.loads(path.read_text())
        except json.JSONDecodeError as error:errors.append({'id': fid, 'error': 'invalid JSON: '+str(error)});continue
        records[fid] = r
        if r.get('figure_id') != fid:errors.append({'id': fid, 'error': 'figure_id mismatch'})
        if not r.get('opened'):errors.append({'id': fid, 'error': 'opened list empty'})
        if d.get('figure', {}).get('en_location', {}).get('pages') and not (r.get('ground_truth') or {}).get('description_zh'):
            errors.append({'id': fid, 'error': 'ground_truth description missing'})
        verdicts = {a.get('path'): a for a in r.get('assets', [])}
        for asset in sorted(image_assets(d)-verdicts.keys()):errors.append({'id': fid, 'error': 'no verdict for asset '+asset})
        for a in verdicts.values():
            if a.get('verdict') not in ASSET_VERDICTS:errors.append({'id': fid, 'error': 'asset verdict for '+str(a.get('path'))})
        if (r.get('json_interpretation') or {}).get('verdict') not in JSON_VERDICTS:errors.append({'id': fid, 'error': 'json verdict'})
        if r.get('role') not in ROLES:errors.append({'id': fid, 'error': 'role'})
        for ref in (r.get('capability_mapping') or {}).get('existing_ids', []):
            if ref not in ids:errors.append({'id': fid, 'error': 'unknown capability id '+str(ref)})
    return {'guide': code, 'figures': len(records)+len(missing), 'missing': missing, 'errors': errors,
            'complete': not missing and not errors}

def main():
    p = argparse.ArgumentParser(description=__doc__);sub = p.add_subparsers(dest='mode', required=True)
    t = sub.add_parser('text');t.add_argument('guide');t.add_argument('--start', type=int, default=1);t.add_argument('--end', type=int)
    f = sub.add_parser('figures');f.add_argument('guide', nargs='?')
    a = p.parse_args()
    report = check_text(a.guide, a.start, a.end) if a.mode == 'text' else check_figures(a.guide)
    print(json.dumps(report, ensure_ascii=False, indent=1))
    return int(not report['complete'])

if __name__ == '__main__':sys.exit(main())
