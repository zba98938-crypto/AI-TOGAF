"""Independent production, delivery, integrity and scale regression scenarios."""
import ast
import copy
import hashlib
import importlib.util
import json
import shutil
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SHARED = REPO / 'togaf-standard-10th-ai/skills/_shared'
sys.path.insert(0, str(SHARED / 'scripts'))
from profile_examples import DEFAULT_CONTEXT, normalize_example
from proficiency_semantics import OFFICIAL_SCALE
from registry import load


def save(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + '\n')


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def source_hashes():
    result = {}
    for folder in (REPO / 'togaf-standard-10th-ai/skills', REPO / 'tests'):
        for path in folder.rglob('*'):
            if path.is_file() and not {'.venv', 'node_modules', '__pycache__', '.DS_Store'} & set(path.parts):
                result[str(path.relative_to(REPO))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def syntax_check(out):
    checked = []
    for name in source_hashes():
        if name.endswith('.py'):
            ast.parse((REPO / name).read_text(), filename=name)
            checked.append(name)
    save(out / 'syntax.json', {'checked': checked})
    return {'python_files': len(checked)}


def production_profiles(out):
    from generate import generate
    from validate import validate
    from architecture_delivery import output_check
    profiles = load()[2]
    rows = []
    for pid, profile in profiles.items():
        if profile.get('alias_of'):
            continue
        if 'example' not in profile:
            rows.append({'profile_id': pid, 'errors': [], 'layouts': [], 'status': 'blocked',
                         'reason': 'No embedded business fixture; use dedicated foundation/case verification.'})
            continue
        model = normalize_example(profile)
        errors = [i for i in validate(model) if i['level'] == 'error']
        row = {'profile_id': pid, 'errors': errors, 'layouts': []}
        if not errors:
            for layout in ('reference', 'adaptive'):
                destination = out / 'production' / pid / layout
                try:
                    manifest = generate(model, destination, all_items=True, strict=True, layout=layout)
                    _, issues = output_check(destination, model)
                    require(not issues, issues)
                    row['layouts'].append({'layout': layout, 'status': 'pass', 'files': len(manifest['output_sha256'])})
                except Exception as exc:
                    row['layouts'].append({'layout': layout, 'status': 'fail', 'error': str(exc)})
        rows.append(row)
        if len(rows) % 25 == 0:
            print('production profiles checked: ' + str(len(rows)), flush=True)
    save(out / 'production-profiles.json', rows)
    failed = [r for r in rows if r.get('status') != 'blocked' and
              (r['errors'] or len(r['layouts']) != 2 or any(x['status'] != 'pass' for x in r['layouts']))]
    require(not failed, [r['profile_id'] for r in failed])
    blocked = [r['profile_id'] for r in rows if r.get('status') == 'blocked']
    return {'profiles': len(rows), 'layouts': sum(len(r['layouts']) for r in rows),
            'missing_business_fixtures': blocked, '_status': 'blocked' if blocked else 'pass'}


GROUPS = ('sources', 'entities', 'relationships', 'views', 'states', 'scopes', 'scales', 'analyses')
# Only identity/reference fields are rewritten. Enum values and free prose are literal.
REFERENCE_FIELDS = {'id', 'source', 'target', 'from', 'parent', 'evidence', 'evidence_refs',
                    'rule_evidence', 'method_evidence', 'node_ids', 'raw_record_ids',
                    'source_refs', 'business_case_ref', 'processes',
                    'context_ref', 'policy_context_ref', 'model_object_refs', 'role_ref', 'role_refs',
                    'task_ref', 'task_refs', 'requirement_refs', 'assessment_ref', 'assessment_refs',
                    'person_ref', 'person', 'role'}
LITERAL_IDS = {'artifact_id', 'profile_id', 'method_id', 'calculator_id', 'deliverable_id',
               'source_function_id', 'feature_id', 'source_check_id'}


def namespace_model(model, prefix):
    model = copy.deepcopy(model)
    identities = {row['id']: prefix + row['id'] for group in GROUPS for row in model.get(group, [])
                  if row['id'] != OFFICIAL_SCALE}
    def rewrite(value, key=''):
        reference = key not in LITERAL_IDS and (key in REFERENCE_FIELDS or key.endswith(('_id', '_ids', '_evidence', '_evidence_refs')))
        if isinstance(value, str):
            return identities.get(value, value) if reference else value
        if isinstance(value, list):
            return [rewrite(item, key) for item in value]
        if isinstance(value, dict):
            if key == 'requirement_versions':
                return {identities.get(name, name): item for name, item in value.items()}
            if key == 'categories':
                return {name: rewrite(item, 'entity_ids') for name, item in value.items()}
            if key == 'score_evidence':
                return {name: rewrite(item, 'evidence') for name, item in value.items()}
            return {name: rewrite(item, name) for name, item in value.items()}
        return value
    result = rewrite(model)
    # Scenario uses named endpoint fields rather than generic *_id names.
    for analysis in result.get('analyses', []):
        if analysis['method_id'] == 'scenario-traceability-review':
            for row in analysis['inputs'].get('associations', []):
                row['process'] = identities.get(row['process'], row['process'])
            for row in analysis['inputs'].get('painpoint_outcomes', []):
                for field in ('problem', 'outcome'):
                    row[field] = identities.get(row[field], row[field])
    # Metadata diagnostic IDs are explicitly assessment:asset:facet composites.
    for entity in result.get('entities', []):
        if entity['type'] == 'g234:function-coverage':
            for gap in entity.get('attributes', {}).get('analysis_result', {}).get('gaps', []):
                gap['id'] = ':'.join(identities.get(part, part) for part in gap['id'].split(':'))
    return result


def bind_direct_delivery_fixture(model, delivery, rule, ordinal):
    """Fictional implementation records exercise direct chapter selectors."""
    if rule['id'] != 'implementation-governance-model':
        return
    source = 'd%s-governance-input' % ordinal
    model['sources'].append({'id': source, 'kind': 'user',
                            'description': '虚构实施治理输入；仅候选，不表示真实任命、批准或实施。',
                            'locator': 'synthetic:delivery-regression:implementation-governance'})
    records = {
        '治理过程': ('decision', '虚构异常处置流程', {
            'workflow': ['交付方提供检查结果', '架构协调人核对偏离', '失败暂停并升级', '授权责任人复核恢复'],
            'decision': '不满足门禁则保持停止；没有有效豁免不解除偏离。'}),
        '治理组织结构': ('actor', '虚构项目治理小组', {
            'organization': '项目采用的候选治理接口，不产生雇佣汇报线',
            'interfaces': ['业务责任人', '架构协调人', '交付负责人', '运营负责人']}),
        '治理角色与责任': ('role', '虚构交付负责人', {
            'responsibility': '组织检查、保留结果、提交偏离与交接材料',
            'authority': '无真实授权；不能单方接受架构偏离', 'skill': '证据核对与异常升级'}),
        '治理检查点与成功失败准则': ('milestone', '虚构交接门禁', {
            'success_criteria': ['检查证据齐全', '偏离已关闭或具有有效且适用的豁免', '运营责任人完成情景核对'],
            'failure_action': '停止交接并保留缺口', 'status': 'candidate-not-executed'}),
    }
    require(set(records) == {section['title'] for section in rule['sections']},
            'direct governance fixture must cover the current chapter contract')
    for number, section in enumerate(rule['sections']):
        kind, name, attrs = records[section['title']]
        require(kind in section['entity_types'], 'direct fixture type does not match its chapter')
        identity = 'd%s-governance-section-%s' % (ordinal, number)
        model['entities'].append({'id': identity, 'type': kind, 'name': name,
                                  'attributes': attrs, 'evidence': [source], 'certainty': 'assumed',
                                  'approval_status': 'candidate', 'implementation_status': 'not-started'})
        delivery['assembly']['section_bindings'][section['title']] = {'entity_ids': [identity]}


def delivery_cases(out):
    from deliverable_assembly import assemble, load_rules
    from generate import generate
    from validate import validate
    from architecture_delivery import output_check
    _, deliveries, profiles, _ = load()
    rules = load_rules()
    rows = []
    for ordinal, rule in enumerate(rules['deliverables']):
        did = rule['id']
        selected = []
        for request in rule.get('core_requirements', []) + rule['sections']:
            candidates = [pid for pid in request.get('profile_ids', []) if pid in profiles]
            if not candidates:
                candidates = [p['id'] for p in profiles.values() if p['artifact_id'] in request.get('artifact_ids', []) and not p.get('alias_of')]
            if candidates and candidates[0] not in selected:
                selected.append(candidates[0])
        model = {'schema_version': '2.0', 'project': {'id': 'delivery-regression', 'name': '虚构交付物回归',
                 'version': '1', 'context': copy.deepcopy(DEFAULT_CONTEXT), 'is_example': True,
                 'approval_status': 'candidate', 'implementation_status': 'not-started'},
                 'sources': [], 'entities': [], 'relationships': [], 'views': [], 'deliverables': [], 'gaps': []}
        for number, pid in enumerate(selected):
            sample = namespace_model(normalize_example(profiles[pid]), 'd%sp%s-' % (ordinal, number))
            states = {s['id']: s for s in sample.get('states', [])}
            for entity in sample['entities']:
                context = copy.deepcopy(sample['project']['context'])
                context['evolution'] = states.get(entity.get('state_id'), {}).get('evolution', entity.get('evolution', context['evolution']))
                entity.setdefault('context', context)
            for group in GROUPS:
                if sample.get(group):
                    target = model.setdefault(group, [])
                    for item in sample[group]:
                        existing = next((row for row in target if row['id'] == item['id']), None)
                        if group == 'scales' and item['id'] == OFFICIAL_SCALE and existing:
                            require({k: v for k, v in existing.items() if k != 'evidence'} ==
                                    {k: v for k, v in item.items() if k != 'evidence'},
                                    'conflicting official proficiency scale')
                            existing['evidence'] = list(dict.fromkeys(existing.get('evidence', []) + item.get('evidence', [])))
                        else:
                            target.append(item)
            for key, values in sample.get('extensions', {}).items():
                if isinstance(values, dict):
                    target = model.setdefault('extensions', {}).setdefault(key, {})
                    for name, value in values.items():
                        require(name not in target or target[name] == value, 'conflicting extension ' + name)
                        target[name] = value
        delivery = {'id': 'delivery-' + did, 'deliverable_id': did, 'title': '虚构：' + deliveries[did]['name_zh'],
                    'view_ids': [v['id'] for v in model['views']], 'entity_ids': [], 'sections': {},
                    'approval_status': 'candidate', 'implementation_status': 'not-started',
                    'assembly': {'rules_version': '1.0', 'mode': 'strict', 'analysis_ids': [], 'active_groups': [], 'section_bindings': {}}}
        bind_direct_delivery_fixture(model, delivery, rule, ordinal)
        model['deliverables'] = [delivery]
        dest = out / 'deliverables' / did
        save(dest / 'model.json', model)
        row = {'deliverable_id': did, 'selected_profiles': selected,
               'direct_section_bindings': copy.deepcopy(delivery['assembly']['section_bindings'])}
        try:
            errors = [i for i in validate(model) if i['level'] == 'error']
            require(not errors, errors)
            result = assemble(model, delivery, deliveries[did], rules)
            save(dest / 'assembly.json', result)
            require(result['status'] == 'assembled-awaiting-review', result.get('gaps'))
            require(not result.get('unbound_section_titles'), result.get('unbound_section_titles'))
            generate(model, dest / 'generated', deliverable_ids=[did], strict=True)
            _, issues = output_check(dest / 'generated', model)
            require(not issues, issues)
            empty = copy.deepcopy(model)
            for group in GROUPS:
                empty[group] = []
            negative = copy.deepcopy(delivery)
            negative['view_ids'] = []
            blocked = assemble(empty, negative, deliveries[did], rules)
            require(blocked['status'] == 'blocked', 'empty strict delivery accepted')
            negative['assembly']['mode'] = 'draft'
            draft = assemble(empty, negative, deliveries[did], rules)
            require(draft['status'] == 'draft-with-gaps', 'empty draft lost gaps')
            row.update(status='pass', sections=len(result['section_blocks']))
        except Exception as exc:
            row.update(status='fail', error=str(exc))
        rows.append(row)
        print('deliverable: ' + did + ' ' + row['status'], flush=True)
    save(out / 'deliverables.json', rows)
    require(all(r['status'] == 'pass' for r in rows), [r for r in rows if r['status'] != 'pass'])
    require(set(deliveries) == {r['deliverable_id'] for r in rows}, 'delivery registry coverage')
    return {'deliverables': len(rows), 'sections': sum(r['sections'] for r in rows)}


def integrity_and_adm(out):
    from adm import initialize, schema_issues, check_cycle
    from architecture_delivery import output_check
    from generate import generate
    model = normalize_example(load()[2]['risk-appetite-default'])
    dest = out / 'integrity' / 'pristine'
    manifest = generate(model, dest, all_items=True, strict=True)
    _, errors = output_check(dest, model)
    require(not errors, errors)
    altered = out / 'integrity' / 'tampered'
    shutil.copytree(dest, altered)
    target = altered / manifest['artifacts'][0]['path']
    target.write_text(target.read_text() + '\nTAMPERED\n')
    _, tampered = output_check(altered, model)
    require(any(e.startswith('output-file-stale:') for e in tampered), tampered)
    changed = copy.deepcopy(model)
    changed['project']['version'] = 'changed'
    _, stale = output_check(dest, changed)
    require('output-model-stale' in stale, stale)
    cycle = initialize(model, 'regression-cycle', 'synthetic concern')
    require(not schema_issues(cycle), schema_issues(cycle))
    checked = check_cycle(cycle, model, out)
    require(not checked['errors'], checked['errors'])
    require(len(cycle['phases']) == 9 and len(checked['phases']) == 9, 'ADM phase inventory')
    require(checked['recorded_cycle_complete'] is False, 'initialized cycle cannot be complete')
    require(any(p['gaps'] for p in checked['phases']), 'initialized cycle must retain pending evidence')
    save(out / 'integrity-adm.json', {'tampered': tampered, 'stale_model': stale, 'cycle': cycle, 'check': checked})
    return {'output_tamper_rejected': True, 'stale_model_rejected': True, 'adm_phases': len(cycle['phases'])}


def scale_cases(out, orders):
    base = SHARED / 'examples/million-enterprise'
    def module(name):
        spec = importlib.util.spec_from_file_location('core_' + name, base / (name + '.py'))
        result = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(result)
        return result
    builder, auditor, derive = [module(n) for n in ('build_dataset', 'audit_dataset', 'derive_facts')]
    dest = out / 'scale'
    dest.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='raw-', dir=dest) as temporary:
        root = Path(temporary)
        dataset = root / 'dataset'
        builder.build(dataset, orders, 20261104)
        report = auditor.audit(dataset / 'enterprise.sqlite')
        require(report['counts']['orders'] == orders, 'generated SQL order count differs from requested scale')
        negative = auditor.negatives(dataset / 'enterprise.sqlite')
        derive.derive(dataset, dest / 'derived-facts.json')
        save(dest / 'oracle-report.json', report)
        save(dest / 'negative-cases.json', negative)
        for path in dataset.glob('*.json'):
            shutil.copyfile(path, dest / path.name)
        require(report['passed'] and negative['passed'], 'SQL reconciliation or negative mutation failed')
        hashes = []
        for number in range(2):
            sample = root / ('repeat-' + str(number))
            builder.build(sample, 1000, 20261104)
            hashes.append(hashlib.sha256((sample / 'enterprise.sqlite').read_bytes()).hexdigest())
        require(hashes[0] == hashes[1], 'same-seed dataset differs')
        save(dest / 'determinism.json', {'orders': 1000, 'seed': 20261104, 'hashes': hashes, 'passed': True})
    return {'orders': report['counts']['orders'], 'sql_checks': len(report['checks']), 'negative_cases': len(negative['cases']),
            'deterministic': True, 'raw_databases': 'temporary; removed after checks'}
