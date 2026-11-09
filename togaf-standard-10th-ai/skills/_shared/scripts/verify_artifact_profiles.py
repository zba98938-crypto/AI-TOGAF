#!/usr/bin/env python3
"""Profile-by-profile engineering checks, not visual/business/source-equivalence acceptance.

Uses declared profile examples as input and independent invariants as oracles.
No expected result is populated from a render/check return value. Aliases do not
add coverage. Each output is a bounded focus view, not a whole-repository graph.
"""
import argparse
import copy
import hashlib
import json
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

from profile_render import ROOT, render_profile
from registry import load
from table_expression import render_table_expression
from view_semantics import check_view

LAYOUTS = ('reference', 'adaptive')
CLASSIFIERS = {'category', 'block', 'component', 'dimension', 'perspective', 'quadrant',
               'layer', 'direction', 'status', 'existence', 'scale', 'scope', 'reference_row',
               'reference_column', 'parent_id', 'lane', 'lane_id', 'phase', 'kind', 'pattern',
               'integration_pattern', 'option', 'type', 'level', 'state', 'state_id',
               'target_state', 'assessment_type', 'solution_part', 'deployment_model',
               'ingestion_mode', 'inference_type', 'scope_id', 'capability_id', 'stage_id', 'instance_id',
               'start', 'end', 'start_date', 'end_date', 'date', 'record_kind', 'origin',
               'factor_category', 'change_kind','unit_kind','ADM_phase','mapping_status','concept_key','phase_code'}


def table(headers, rows):
    def cell(v):
        return str(v).replace('|', '\\|').replace('\n', '<br>')
    return '| ' + ' | '.join(map(cell, headers)) + ' |\n| ' + ' | '.join('---' for _ in headers) + ' |\n' + ''.join('| ' + ' | '.join(map(cell, row)) + ' |\n' for row in rows)


def canonical_profiles(profiles):
    return [p for p in profiles.values() if not p.get('alias_of')]


def inputs(profile):
    model = copy.deepcopy(profile['example'])
    view = model.pop('view')
    view['_is_example'] = True
    if len(view['entity_ids']) > 60:
        raise ValueError(profile['id'] + ': example exceeds 60 entities; supply a concern slice, not a whole-library graph')
    return model, view


def express(model, view, profile, layout):
    if profile.get('output_kind', 'diagram') == 'table':
        content, report = render_table_expression(model, view, profile, table)
    else:
        content, report = render_profile(model, view, profile, layout)
        ET.fromstring(content)
    report['errors'].extend(check_view(model, view, profile))
    return content, report


def visible_text(content, profile):
    return ''.join(ET.fromstring(content).itertext()) if profile.get('output_kind', 'diagram') == 'diagram' else content


def expected_ids(model, view):
    """Input-based expectation. Never consume a renderer's represented IDs."""
    return set(view['entity_ids']), set(view['relationship_ids'])


def check_expression(model, view, profile, content, report):
    failures = []
    entities, relationships = expected_ids(model, view)
    for key, expected in [('represented_entity_ids', entities), ('represented_relationship_ids', relationships)]:
        if set(report[key]) != expected:
            failures.append({'code': 'identity-coverage', 'field': key,
                             'missing': sorted(expected - set(report[key])), 'extra': sorted(set(report[key]) - expected)})
    if report['errors']:
        failures.append({'code': 'expression-errors', 'errors': report['errors']})
    if report.get('coverage_contract')=='expression-locations/2':
        from expression_details import location_failures
        failures.extend(location_failures(content,report.get('companion_html',''),report['expression_locations'],report['companion_file']))
    selected = {e['id']: e for e in model['entities'] if e['id'] in entities}
    for identity, e in selected.items():
        missing = set(e.get('attributes', {})) - set(report['represented_attributes'].get(identity, []))
        if missing:
            failures.append({'code': 'attribute-coverage', 'id': identity, 'missing': sorted(missing)})
    for r in model['relationships']:
        if r['id'] not in relationships:
            continue
        required = set(r.get('attributes', {}))
        if 'codes' in r:
            required.add('codes')
        required.update('cardinality.' + k for k in r.get('cardinality', {}))
        missing = required - set(report['represented_relationship_attributes'].get(r['id'], []))
        if missing:
            failures.append({'code': 'relationship-attribute-coverage', 'id': r['id'], 'missing': sorted(missing)})
    # Check actual output IDs independently of the report ledger.
    if profile.get('output_kind', 'diagram') == 'diagram':
        from expression_details import identity_failures, location_failures
        failures.extend(identity_failures(content,report.get('companion_html',''),entities,relationships))
    return failures


def substantive_change(model, view):
    """Change an existing business field, never just title, name, ID or legend."""
    selected = set(view['entity_ids'])
    token = 'VERIFY' + hashlib.sha256(view['id'].encode()).hexdigest()[:8]
    preferred = ['definition', 'description', 'detail', 'statement', 'owner', 'text', 'value_item', 'purpose', 'responsibility', 'acceptance','function']
    candidates = [(e, k) for e in model['entities'] if e['id'] in selected
                  for k, v in e.get('attributes', {}).items() if isinstance(v, str) and k not in CLASSIFIERS]
    candidates.sort(key=lambda pair: preferred.index(pair[1]) if pair[1] in preferred else len(preferred))
    if candidates:
        e, key = candidates[0]
        before = e['attributes'][key]
        e['attributes'][key] = token
        return {'entity_id': e['id'], 'field': key, 'before': before, 'after': token, 'expected_text': token}
    # The sustainability canvas has structured decisions, not free scalar fields.
    for e in model['entities']:
        if e['id'] in selected:
            assessment = e.get('attributes', {}).get('assessment_inputs', {})
            if isinstance(assessment, dict) and isinstance(assessment.get('scope'), str):
                before = assessment['scope']
                assessment['scope'] = token
                return {'entity_id': e['id'], 'field': 'assessment_inputs.scope',
                        'before': before, 'after': token, 'expected_text': token}
            for i, decision in enumerate(e.get('attributes', {}).get('decisions', [])):
                if 'explanation' in decision:
                    before = decision['explanation'];decision['explanation'] = token
                    return {'entity_id': e['id'], 'field': 'decisions.' + str(i) + '.explanation',
                            'before': before, 'after': token, 'expected_text': token}
    return None


def negative_cases(model, view, profile):
    """Concrete missing-contract-field and applicable notation cases; explicit N/A otherwise."""
    cases = []
    requirement = profile.get('required_attributes', {})
    for e in model['entities']:
        if e['id'] not in view['entity_ids']:
            continue
        fields = requirement.get(e['type'], []) + requirement.get('*', []) if isinstance(requirement, dict) else requirement
        key = next((k for k in fields if k != 'name' and k in e.get('attributes', {})), None)
        if key:
            mutated = copy.deepcopy(model)
            target = next(x for x in mutated['entities'] if x['id'] == e['id'])
            del target['attributes'][key]
            code = 'missing-required-attribute' if profile.get('output_kind') == 'table' else 'missing-profile-attribute'
            cases.append({'id': 'required-field', 'entity_id': e['id'], 'field': key,
                          'model': mutated, 'view': copy.deepcopy(view), 'expected_code': code})
            break
    selected = [r for r in model['relationships'] if r['id'] in view['relationship_ids']]
    renderer = profile.get('renderer')
    if renderer == 'matrix':
        rowtypes = profile.get('template', {}).get('row_types', [])
        if rowtypes:
            removed = {e['id'] for e in model['entities'] if e['type'] in rowtypes}
            v = copy.deepcopy(view)
            v['entity_ids'] = [i for i in v['entity_ids'] if i not in removed]
            v['relationship_ids'] = [r['id'] for r in selected if r['source'] not in removed and r['target'] not in removed]
            cases.append({'id': 'missing-row-axis', 'model': copy.deepcopy(model), 'view': v, 'expected_code': 'missing-matrix-axes'})
    for r in selected:
        required = profile.get('required_relationship_attributes', {})
        fields = required.get(r['type'], []) + required.get('*', [])
        field = next((k for k in fields if k in r.get('attributes', {})), None)
        code = 'missing-relationship-attribute'
        if renderer == 'sequence' and 'order' in r.get('attributes', {}):field = 'order';code = 'missing-message-order'
        if renderer == 'causal' and 'polarity' in r.get('attributes', {}):field = 'polarity';code = 'missing-causal-polarity'
        if field:
            mutated = copy.deepcopy(model)
            next(x for x in mutated['relationships'] if x['id'] == r['id'])['attributes'].pop(field)
            if profile.get('output_kind') == 'table':code = 'missing-required-relationship-attribute'
            cases.append({'id': 'relationship-field', 'relationship_id': r['id'], 'field': field,
                          'model': mutated, 'view': copy.deepcopy(view), 'expected_code': code})
            break
        if renderer == 'er' and r['type'] in {'data_association', 'logical_association', 'information_association'} and r.get('cardinality'):
            mutated = copy.deepcopy(model)
            next(x for x in mutated['relationships'] if x['id'] == r['id']).pop('cardinality')
            cases.append({'id': 'missing-end-cardinality', 'relationship_id': r['id'], 'model': mutated,
                          'view': copy.deepcopy(view), 'expected_code': 'missing-er-cardinality'})
            break
    applicability = {'required_field': 'applicable' if any(c['id'] == 'required-field' for c in cases) else 'not-applicable: profile declares no present required business field',
                     'relationship_negative': 'applicable' if any('relationship_id' in c for c in cases) else 'not-applicable: no selected relationship' if not selected else 'not-applicable: no encoded required relationship-field/cardinality rule for this notation'}
    return cases, applicability


def verify_profile(profile, out=None):
    model, view = inputs(profile)
    result = {'profile_id': profile['id'], 'artifact_id': profile['artifact_id'],
              'output_kind': profile.get('output_kind', 'diagram'), 'failures': [], 'layouts': [],
              'notice': 'Engineering checks only; human visual/business acceptance and source equivalence remain unverified.'}
    outputs = []
    modified = copy.deepcopy(model)
    change = substantive_change(modified, view)
    result['substantive_change'] = change
    if change is None:result['failures'].append({'code': 'no-substantive-change-case'})
    negatives, applicability = negative_cases(model, view, profile)
    result['negative_applicability'] = applicability
    result['negative_cases'] = [{k: v for k, v in c.items() if k not in {'model', 'view'}} for c in negatives]
    for layout in LAYOUTS:
        content, report = express(model, view, profile, layout)
        errors = check_expression(model, view, profile, content, report)
        result['failures'].extend({'layout': layout, 'case': 'valid', **e} for e in errors)
        result['layouts'].append({'layout': layout, 'warnings': report['warnings'], 'valid': not errors})
        outputs.append((profile['id'] + '-' + layout, content, report))
        if change:
            changed, changed_report = express(modified, view, profile, layout)
            changed_errors = check_expression(modified, view, profile, changed, changed_report)
            if change['expected_text'] not in visible_text(changed, profile)+changed_report.get('companion_html',''):changed_errors.append({'code': 'substantive-change-not-visible'})
            if changed == content and changed_report.get('companion_html')==report.get('companion_html'):changed_errors.append({'code': 'substantive-change-no-output-delta'})
            result['failures'].extend({'layout': layout, 'case': 'modified', **e} for e in changed_errors)
            outputs.append((profile['id'] + '-' + layout + '-modified', changed, changed_report))
        for case in negatives:
            _, negative_report = express(case['model'], case['view'], profile, layout)
            if case['expected_code'] not in {e['code'] for e in negative_report['errors']}:
                result['failures'].append({'layout': layout, 'case': case['id'], 'code': 'negative-not-detected', 'expected_code': case['expected_code']})
    if out:
        out = Path(out);out.mkdir(parents=True, exist_ok=True)
        for index, (identity, content, report) in enumerate(outputs):
            if report.get('companion_html'):
                filename=identity+'.details.html'
                content=content.replace(report['companion_file'],filename)
                report['companion_file']=filename
                from expression_details import locations
                report['expression_locations']=locations(content,report['companion_html'],filename)
                (out/filename).write_text(report['companion_html'])
            (out / (identity + ('.svg' if result['output_kind'] == 'diagram' else '.md'))).write_text(content)
            (out / (identity + '.coverage.json')).write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
            outputs[index] = (identity, content, report)
        (out / (profile['id'] + '.case.json')).write_text(json.dumps({'input': model, 'view': view, 'result': result}, ensure_ascii=False, indent=2) + '\n')
    return result, outputs


def render_outputs(svgs, out, oversized_policy):
    from generate import subset_font
    font = subset_font(''.join(content for _, content in svgs), out / 'font-subset.ttf')
    jobs = []
    for identity, content in svgs:
        content = content.replace('>', '><defs><style>@font-face{font-family:TogafCJK;src:url(data:font/ttf;base64,' + font + ')}</style></defs>', 1)
        (out / (identity + '.svg')).write_text(content)
        jobs.append({'id': identity, 'kind': 'svg', 'source': identity + '.svg', 'svg': identity + '.svg', 'png': identity + '.png'})
    jobfile = out / 'render-jobs.json'
    jobfile.write_text(json.dumps({'font': 'font-subset.ttf', 'oversized_policy': oversized_policy,
                                  'jobs': jobs}, ensure_ascii=False, indent=2) + '\n')
    completed = subprocess.run(['node', str(ROOT / 'scripts/render.mjs'), str(jobfile.resolve())])
    return 'passed' if completed.returncode == 0 else 'blocked' if completed.returncode == 3 else 'failed'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profile', action='append', default=[])
    parser.add_argument('--all', action='store_true', help='main-session full acceptance only')
    parser.add_argument('--out', required=True)
    parser.add_argument('--render', action='store_true', help='actually export PNG as well as SVG using existing resvg dependency')
    parser.add_argument('--oversized-policy', choices=['block','tile'], default='block',
                        help='Explicitly allow original-resolution PNG tiles for oversized SVGs')
    args = parser.parse_args()
    artifacts, _, profiles, _ = load()
    if not args.all and not args.profile:parser.error('select --profile (repeatable), or --all explicitly')
    unknown = set(args.profile) - set(profiles)
    if unknown:parser.error('unknown profiles: ' + ', '.join(sorted(unknown)))
    selected = canonical_profiles(profiles) if args.all else list({profiles[pid].get('alias_of', pid): profiles[profiles[pid].get('alias_of', pid)] for pid in args.profile}.values())
    out = Path(args.out)
    if out.exists():parser.error('use a new output directory; historical runs are immutable')
    out.mkdir(parents=True, exist_ok=False)
    results = [];svgs = []
    for profile in selected:
        try:
            result, outputs = verify_profile(profile, out)
            if profile.get('output_kind', 'diagram') == 'diagram':svgs.extend((identity, content) for identity, content, _ in outputs)
        except Exception as error:
            result = {'profile_id': profile['id'], 'failures': [{'code': 'case-exception', 'message': str(error)}]}
        results.append(result)
    render_status = 'not-requested'
    render_error = None
    if args.render and svgs:
        try:
            render_status = render_outputs(svgs, out, args.oversized_policy)
        except (ImportError, FileNotFoundError) as error:
            render_status, render_error = 'blocked', str(error)
        except Exception as error:
            render_status, render_error = 'failed', str(error)
    failed_profiles = sum(bool(r['failures']) for r in results)
    status = 'failed' if failed_profiles or render_status == 'failed' else 'blocked' if render_status == 'blocked' else 'passed'
    summary = {'status': status, 'independent_profiles_checked': len(results),
               'artifact_families_checked': len({p['artifact_id'] for p in selected}),
               'registered_artifact_families': len(artifacts),
               'unselected_artifact_families': sorted(set(artifacts)-{p['artifact_id'] for p in selected}),
               'output_kinds_checked': {kind: sum(p.get('output_kind','diagram')==kind for p in selected) for kind in ['diagram','table']},
               'aliases_not_counted': {p['id']: p['alias_of'] for p in profiles.values() if p.get('alias_of')},
               'failed_profiles': failed_profiles, 'png_export_requested': args.render,
               'render_status': render_status, 'render_error': render_error, 'oversized_policy': args.oversized_policy,
               'review_status': 'generated-awaiting-human-review', 'results': results}
    (out / 'verification.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: v for k, v in summary.items() if k not in {'results','unselected_artifact_families'}}, ensure_ascii=False))
    return 1 if summary['failed_profiles'] or render_status == 'failed' else 3 if render_status == 'blocked' else 0


if __name__ == '__main__':
    raise SystemExit(main())
