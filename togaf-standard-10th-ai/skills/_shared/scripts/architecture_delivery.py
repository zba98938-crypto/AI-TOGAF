#!/usr/bin/env python3
"""Connect ADM decisions, stakeholder concerns and current generated products.

All routing and structural checks are project conventions based on local guides.
No command creates facts, evaluates professional adequacy or grants acceptance.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

import jsonschema
from adm import (ROOT, check_cycle, contracts, load,
                 schema_issues, write_new)
from evidence_integrity import safe_path, sha
from registry import load as registry
from requirements_trace import REQUIREMENT_TYPES, audit as trace_audit

SCHEMA = ROOT / 'schemas/architecture-delivery.schema.json'


def catalog(phase_ids=None):
    """Offer relevant capabilities, not mandatory phase deliverables."""
    arts, dels, profiles, methods = registry()
    definitions = contracts()
    selected = phase_ids or list(definitions) + ['Requirements', 'Review']
    usage = load(ROOT / 'references/adm-phases.json').get('guide_usage', [])
    rows = []
    for key in selected:
        if key == 'Requirements':
            definition = load(ROOT / 'references/adm-phases.json')['requirements_management']
        elif key == 'Review':
            definition = {'owners': ['togaf-artifact-review'], 'source_refs': ['G186 §§3.3, 6.2', 'G248 §§3–6'],
                          'steps': ['核对关注点及视点选择', '评审制品语义、追溯、跨视图一致性与视觉可读性',
                                    '区分目标接受、实施符合性及价值判断'], 'deliverables': []}
        else:
            definition = definitions[key]
        owners = set(definition['owners'])
        rows.append({
            'phase': key, 'source_refs': definition['source_refs'],
            'foundation_binding': definition.get('foundation_binding'),
            'source_steps': definition.get('source_step_records', []),
            'owner_skills': sorted(owners), 'activities': definition['steps'],
            'criteria': definition.get('criteria', {}),
            'suggested_deliverable_ids': definition['deliverables'],
            'conditional_deliverables': definition.get('conditional_deliverables', []),
            'deliverable_definitions': [{'id': did, 'foundation_binding': dels[did].get('foundation_binding'),
                                        'phase_applicability': dels[did].get('phase_applicability', [])}
                                       for did in definition['deliverables'] if did in dels],
            'guide_usage': [u for u in usage if u['phase'] == key],
            'artifact_candidates': [
                {'id': a['id'], 'name': a['name_zh'], 'kind': a['kind'],
                 'owner': a['owner'], 'question': a.get('question', a.get('decision')),
                 'foundation_binding': a.get('foundation_binding'),
                 'foundation_phase_suggestions': a.get('foundation_phase_suggestions', []),
                 'phase_basis': ('source-artifact-phase-list' if key in a.get('foundation_phase_suggestions', [])
                                 else 'project-owner-routing-candidate'),
                 'profile_ids': [p['id'] for p in profiles.values() if p['artifact_id'] == a['id']],
                 'definition': 'references/' + ('artifacts/' if (ROOT / 'references/artifacts' / (a['id'] + '.md')).is_file()
                                                else 'capabilities/') + a['id'] + '.md'}
                for a in arts.values() if a['owner'] in owners or key in a.get('foundation_phase_suggestions', [])],
            'method_candidates': [
                {'id': m['id'], 'name': m['name'], 'source_refs': m.get('source_refs', []),
                 'definition': 'references/analysis-methods/' + m['id'] + '.md'}
                for m in methods if m['owner'] in owners]})
    return {'schema_version': 'architecture-delivery-catalog-1.0',
            'counts': {'artifact_families': len(arts), 'profile_entries': len(profiles),
                       'methods': len(methods), 'deliverables': len(dels)},
            'notice': 'phase_basis区分C220制品阶段列表与项目主责路由；条件交付物保留if any。可跨阶段复用，不构成强制输出或批准。',
            'phases': rows}


def initialize(model, cycle, phase_ids=None):
    invalid = schema_issues(cycle)
    if invalid:
        raise ValueError(json.dumps(invalid, ensure_ascii=False))
    if cycle['project_id'] != model['project']['id'] or cycle['is_example'] != model['project']['is_example']:
        raise ValueError('周期与模型的项目/示例身份不一致')
    requested = set(phase_ids or [p['phase'] for p in cycle['phases']
                                 if p['applicability'] != 'not-applicable'])
    if requested - contracts().keys() or not requested:
        raise ValueError('必须选择存在且适用的 ADM 阶段')
    work = []
    for p in cycle['phases']:
        if p['phase'] not in requested:
            continue
        if p['applicability'] == 'not-applicable':
            raise ValueError('所选阶段被裁剪为不适用：' + p['phase'])
        work.append({'phase': p['phase'], 'iteration_id': p['iterations'][-1]['id'],
                     'items': [{'id': p['phase'] + '-' + key, 'criterion_ids': [key],
                                'concern_ids': [], 'view_ids': [], 'deliverable_ids': [],
                                'method_ids': [], 'rationale': ''}
                               for key in contracts()[p['phase']]['criteria']]})
    return {'schema_version': 'architecture-delivery-1.0',
            'project_id': model['project']['id'], 'is_example': model['project']['is_example'],
            'cycle_id': cycle['id'], 'concerns': [], 'phase_work': work}


def output_check(folder, model):
    """Verify saved bytes, model and executable dependencies, including tables."""
    from runtime_provenance import fingerprints
    errors = []
    try:
        manifest = load(Path(folder) / 'manifest.json')
        expected = hashlib.sha256(json.dumps(model, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
        if manifest.get('model_sha256') != expected or load(safe_path(folder, 'model.json')) != model:
            errors.append('output-model-stale')
        if (manifest.get('project', {}).get('id') != model['project']['id']
                or manifest.get('project', {}).get('is_example') != model['project']['is_example']):
            errors.append('output-project-mismatch')
        current = fingerprints(ROOT)
        if (not manifest.get('runtime_stable') or manifest.get('implementation_dependencies_sha256') != current
                or manifest.get('runtime_after_sha256') != current):
            errors.append('output-runtime-stale')
        for field, path in {
            'generator_sha256': 'scripts/generate.py', 'renderer_sha256': 'scripts/profile_render.py',
            'table_renderer_sha256': 'scripts/table_expression.py', 'metamodel_sha256': 'metamodel.json',
            'artifacts_sha256': 'artifacts.json', 'deliverables_sha256': 'deliverables.json',
            'assembly_renderer_sha256': 'scripts/deliverable_assembly.py',
            'assembly_rules_sha256': 'capability-addenda/deliverable-assembly-rules.json',
            'capabilities_sha256': 'capabilities.json'}.items():
            if manifest.get(field) != sha(ROOT / path):
                errors.append('output-contract-stale:' + field)
        hashes = manifest.get('output_sha256', {})
        required = {'model.json', 'validation.json', 'index.md', 'expression-coverage.json', 'analysis-results.json'}
        for group, identity in [('artifacts', 'view_id'), ('deliverables', 'instance_id')]:
            entries = manifest.get(group, [])
            identities = [e.get(identity) for e in entries]
            if None in identities or len(identities) != len(set(identities)):
                errors.append('output-duplicate-or-missing-identity:' + group)
            for entry in entries:
                for field in ('path', 'json') + (('coverage',) if group == 'artifacts' else ()):
                    if not entry.get(field):
                        errors.append('output-file-reference-missing:' + str(entry.get(identity)) + ':' + field)
                required.update(entry[k] for k in ('path', 'json', 'coverage', 'svg', 'png', 'appendix', 'tile_manifest', 'tile_viewer') if entry.get(k))
                required.update(entry.get('tile_pngs', []))
                if entry.get('raster_mode') == 'tiles':
                    if (not entry.get('tile_manifest') or not entry.get('tile_viewer')
                            or not entry.get('tile_pngs') or entry.get('png')
                            or entry.get('monolithic_capacity_claimed') is not False):
                        errors.append('output-tile-contract-invalid:' + str(entry.get(identity)))
                    else:
                        tile_manifest = safe_path(folder, entry['tile_manifest'])
                        tile_data = load(tile_manifest)
                        actual_tiles = [str((tile_manifest.parent / row['png']).relative_to(Path(folder).resolve()))
                                        for row in tile_data['tiles']]
                        required.update(actual_tiles)
                        if (actual_tiles != entry['tile_pngs'] or tile_data.get('scale') != 1
                                or tile_data.get('monolithic_capacity_claimed') is not False
                                or tile_data.get('source_sha256') != sha(safe_path(folder, entry['svg']))):
                            errors.append('output-tile-contract-invalid:' + str(entry.get(identity)))
        for name in sorted(required - hashes.keys()):
            errors.append('output-hash-missing:' + name)
        for name, value in hashes.items():
            if sha(safe_path(folder, name)) != value:
                errors.append('output-file-stale:' + name)
        return manifest, errors
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as exc:
        return {}, errors + ['output-unreadable:' + str(exc)]


def check(plan, model, cycle, evidence_root, output=None):
    errors, gaps = [], []
    result = {'schema_version': 'architecture-delivery-check-1.0', 'errors': errors, 'gaps': gaps,
              'phases': [], 'structurally_linked': False, 'products_current': False,
              'selected_adm_records_complete': False, 'business_acceptance': 'not-assessed',
              'method_execution': 'not-assessed-by-registration',
              'limit': '结构映射、来源、生成完整性与阶段记录分别检查；语义充分性、视觉质量及批准仍需实际评审。'}

    def issue(target, code, identity, message):
        target.append({'code': code, 'id': identity, 'message': message})

    for err in jsonschema.Draft202012Validator(load(SCHEMA)).iter_errors(plan):
        issue(errors, 'plan-schema', '/'.join(map(str, err.absolute_path)), err.message)
    if errors:
        return result
    adm = check_cycle(cycle, model, evidence_root)
    result['adm_errors'] = adm['errors']
    if adm['errors']:
        issue(errors, 'adm-invalid', cycle.get('id', ''), '周期/模型记录无效；先处理 adm check 返回的错误')
        return result
    for field in ('project_id', 'is_example'):
        if plan[field] != cycle[field]:
            issue(errors, 'plan-identity', field, '计划与周期项目/示例身份不一致')
    if plan['cycle_id'] != cycle['id']:
        issue(errors, 'plan-cycle', plan['cycle_id'], '计划引用另一 ADM 周期')
    entities = {e['id']: e for e in model['entities']}
    indexes = {k: {r['id']: r for r in model.get(k, [])} for k in ('views', 'deliverables')}
    arts, dels, profiles, methods = registry()
    method_ids = {m['id'] for m in methods}
    traces = {r['requirement_id']: r for r in trace_audit(model)['rows']}
    concerns = {}
    for c in plan['concerns']:
        if c['id'] in concerns:
            issue(errors, 'concern-duplicate', c['id'], '关注点 ID 重复')
        concerns[c['id']] = c
        if not c['question'].strip() or not c['stakeholder_ids']:
            issue(gaps, 'concern-incomplete', c['id'], '需要决策问题和实际利益相关者引用')
        for key, allowed in [('stakeholder_ids', {'stakeholder'}), ('requirement_ids', REQUIREMENT_TYPES)]:
            for identity in c[key]:
                if identity not in entities or entities[identity]['type'] not in allowed:
                    issue(errors, 'concern-reference', c['id'], key + ' 类型/引用错误：' + identity)
    manifest, output_errors = output_check(output, model) if output else ({}, [])
    for reason in output_errors:
        issue(gaps, 'output-integrity', str(output), reason)
    generated = {
        'views': {e['view_id']: e for e in manifest.get('artifacts', []) if e.get('view_id')},
        'deliverables': {e['instance_id']: e for e in manifest.get('deliverables', []) if e.get('instance_id')}}
    phase_index = {p['phase']: p for p in cycle['phases']}
    adm_index = {p['phase']: p for p in adm['phases']}
    seen_phases, seen_items, used_concerns = set(), set(), set()
    for work in plan['phase_work']:
        key = work['phase']
        if key in seen_phases:
            issue(errors, 'phase-duplicate', key, '每阶段只选当前迭代一次')
        seen_phases.add(key)
        phase = phase_index[key]
        iteration = phase['iterations'][-1]
        if work['iteration_id'] != iteration['id'] or phase['applicability'] == 'not-applicable':
            issue(errors, 'iteration-stale', key, '阶段已重开或裁剪；保留旧计划并更新本次工作映射')
        mapped = set()
        products = set()
        for item in work['items']:
            identity = item['id']
            if identity in seen_items:
                issue(errors, 'item-duplicate', identity, '工作项 ID 重复')
            seen_items.add(identity)
            mapped.update(item['criterion_ids'])
            if set(item['criterion_ids']) - contracts()[key]['criteria'].keys():
                issue(errors, 'criterion-unknown', identity, '退出判据不属于本阶段')
            if (not item['criterion_ids'] or not item['concern_ids'] or not item['rationale'].strip()
                    or not (item['view_ids'] or item['deliverable_ids'])):
                issue(gaps, 'item-unplanned', identity, '补齐判据、关注点、实际视图/交付物和选择理由')
            if set(item['method_ids']) - method_ids:
                issue(errors, 'method-unknown', identity, '分析方法 ID 未登记')
            support_views = set(item['view_ids'])
            for did in item['deliverable_ids']:
                support_views.update(indexes['deliverables'].get(did, {}).get('view_ids', []))
                support_views.update(generated['deliverables'].get(did, {}).get('view_ids', []))
            for group, ids in [('views', sorted(support_views)), ('deliverables', item['deliverable_ids'])]:
                for pid in ids:
                    products.add((group, pid))
                    if pid not in indexes[group]:
                        issue(errors, 'product-unknown', identity, group + '/' + pid)
                        continue
                    bound = {'collection': group, 'id': pid} in iteration['output_refs']
                    if group == 'views' and not bound:
                        bound = any({'collection': 'deliverables', 'id': did} in iteration['output_refs']
                                    and pid in (set(indexes['deliverables'].get(did, {}).get('view_ids', []))
                                        | set(generated['deliverables'].get(did, {}).get('view_ids', [])))
                                    for did in item['deliverable_ids'])
                    if not bound:
                        issue(gaps, 'phase-output-unbound', identity, group + '/' + pid)
                    entry = generated[group].get(pid)
                    if not output or not entry:
                        issue(gaps, 'product-not-generated', pid, '所选成果尚无本次实际生成记录')
                    elif group == 'views':
                        view = indexes[group][pid]
                        expected_profile = view.get('profile_id') or arts[view['artifact_id']]['default_profile_id']
                        if entry.get('id') != view['artifact_id'] or entry.get('profile_id') != expected_profile:
                            issue(gaps, 'product-identity-mismatch', pid, '生成条目制品族或规范与视图不一致')
                        if entry.get('profile_version') != profiles[expected_profile].get('version', '2.0'):
                            issue(gaps, 'product-identity-mismatch', pid, '生成规范版本不一致')
                        if entry.get('status') != 'generated-awaiting-review':
                            issue(gaps, 'product-expression-gaps', pid, '制品仍有表达缺口')
                        try:
                            coverage = load(safe_path(output, entry['coverage']))
                            if (coverage.get('errors') or coverage.get('unrepresented_entity_ids')
                                    or coverage.get('unrepresented_relationship_ids')
                                    or set(view['entity_ids']) - set(coverage.get('represented_entity_ids', []))
                                    or set(view['relationship_ids']) - set(coverage.get('represented_relationship_ids', []))):
                                issue(gaps, 'product-expression-gaps', pid, '实际表达报告仍有错误或对象/关系遗漏')
                            if entry.get('output_kind') == 'diagram' and not (entry.get('png') and manifest.get('rendered')):
                                issue(gaps, 'product-not-generated', pid, '图形尚未完成 PNG 渲染')
                        except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
                            issue(gaps, 'product-expression-gaps', pid, '表达证据不可读取：' + str(exc))
                    elif (entry.get('id') != indexes[group][pid]['deliverable_id']
                          or entry.get('assembly_status') != 'assembled-awaiting-review'
                          or entry.get('unbound_section_titles')):
                        issue(gaps, 'deliverable-unassembled', pid, '交付物身份、动态组装或章节绑定尚未完整')
                    if group == 'deliverables' and entry:
                        try:
                            payload = load(safe_path(output, entry['json']))
                            assembly = payload.get('assembly') or {}
                            if (payload.get('deliverable') != indexes[group][pid]
                                    or payload.get('contract_id') != indexes[group][pid]['deliverable_id']
                                    or assembly.get('status') != 'assembled-awaiting-review'
                                    or not assembly.get('section_blocks') or assembly.get('unbound_section_titles')):
                                issue(gaps, 'deliverable-unassembled', pid, '保存交付物的实际组装/章节内容不支持完整状态')
                        except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
                            issue(gaps, 'deliverable-unassembled', pid, '交付证据不可读取：' + str(exc))
            selected_views = support_views
            covered_entities = set()
            for did in item['deliverable_ids']:
                d = indexes['deliverables'].get(did, {})
                selected_views.update(d.get('view_ids', []))
                covered_entities.update(d.get('entity_ids', []))
            for vid in selected_views:
                covered_entities.update(indexes['views'].get(vid, {}).get('entity_ids', []))
            for cid in item['concern_ids']:
                used_concerns.add(cid)
                concern = concerns.get(cid)
                if not concern:
                    issue(errors, 'concern-unknown', identity, cid)
                    continue
                for rid in concern['requirement_ids']:
                    trace = traces.get(rid, {})
                    if (rid not in covered_entities
                            and not set(trace.get('architecture_ids', [])).intersection(covered_entities)):
                        issue(gaps, 'concern-requirement-unlinked', identity, cid + '：需求未出现在成果或有类型、同语境的设计分配中：' + rid)
        required = {k for k, v in iteration['criteria'].items() if v['status'] != 'not-applicable'}
        for missing in sorted(required - mapped):
            issue(gaps, 'criterion-unmapped', key, missing)
        result['phases'].append({'phase': key, 'iteration_id': iteration['id'],
                                 'adm_status': adm_index[key]['status'], 'adm_gaps': adm_index[key]['gaps'],
                                 'mapped_criteria': sorted(mapped),
                                 'products': [{'collection': g, 'id': i} for g, i in sorted(products)],
                                 'work_items': [dict(item, questions=[concerns[c]['question']
                                                for c in item['concern_ids'] if c in concerns]) for item in work['items']],
                                 'next_activities': contracts()[key]['steps']})
    for cid in concerns.keys() - used_concerns:
        issue(gaps, 'concern-unaddressed', cid, '关注点没有对应阶段工作项及成果')
    if not concerns:
        issue(gaps, 'concerns-missing', '', '先识别利益相关者关注点，再选择制品')
    product_codes = {'output-integrity', 'product-not-generated', 'product-expression-gaps',
                     'deliverable-unassembled', 'product-identity-mismatch'}
    result['structurally_linked'] = not errors and not any(g['code'] not in product_codes for g in gaps)
    result['products_current'] = (bool(output) and not errors and any(p['products'] for p in result['phases'])
                                  and not any(g['code'] in product_codes for g in gaps))
    result['selected_adm_records_complete'] = bool(result['phases']) and not errors and all(
        p['adm_status'] == 'recorded-complete' for p in result['phases'])
    return result


def markdown(result):
    lines = ['# ADM 架构成果工作检查', '', result['limit'], '',
             '| 阶段 | 迭代 | ADM 记录 | 判据映射 | 成果 |', '| --- | --- | --- | --- | --- |']
    for p in result['phases']:
        lines.append(f"| {p['phase']} | {p['iteration_id']} | {p['adm_status']} | {len(p['mapped_criteria'])} | {len(p['products'])} |")
    lines += ['', '结构关联：' + str(result['structurally_linked']),
              '成果当前有效：' + str(result['products_current']),
              '所选 ADM 记录闭合：' + str(result['selected_adm_records_complete']),
              '业务接受：not-assessed', '']
    for e in result['errors'] + result['gaps']:
        lines.append(f"- `{e['code']}` {e['id']}：{e['message']}")
    for p in result['phases']:
        lines += ['', '## ' + p['phase'] + ' 下一步', '']
        for item in p['work_items']:
            lines += ['- 工作项 `' + item['id'] + '`：' + '；'.join(item['questions']),
                      '  - 选择理由：' + (item['rationale'] or '待确定'),
                      '  - 成果：' + '、'.join(item['view_ids'] + item['deliverable_ids']),
                      '  - 方法候选：' + ('、'.join(item['method_ids']) or '按相关领域技能执行；未声明独立计算方法')]
        lines.extend('- ' + step for step in p['next_activities'])
        lines.extend('- 阶段待办：' + gap for gap in p['adm_gaps'])
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['catalog', 'init', 'check', 'report'])
    parser.add_argument('--model')
    parser.add_argument('--cycle')
    parser.add_argument('--plan')
    parser.add_argument('--phase', action='append', choices=[*contracts(), 'Requirements', 'Review'])
    parser.add_argument('--products', help='generate.py 生成目录，检查当前模型、依赖和保存文件')
    parser.add_argument('--out')
    parser.add_argument('--strict', action='store_true', help='结构/成果缺口或所选阶段记录未闭合时返回非零')
    args = parser.parse_args()
    try:
        if args.command == 'catalog':
            value = catalog(args.phase)
        else:
            if not args.model or not args.cycle:
                parser.error('init/check/report 需要 --model 和 --cycle')
            model, cycle = load(args.model), load(args.cycle)
            if args.command == 'init':
                if not args.out:
                    parser.error('init 需要 --out')
                value = initialize(model, cycle, args.phase)
            else:
                if not args.plan:
                    parser.error('check/report 需要 --plan')
                value = check(load(args.plan), model, cycle, Path(args.cycle).resolve().parent, args.products)
        output = markdown(value) if args.command == 'report' else json.dumps(value, ensure_ascii=False, indent=2) + '\n'
        if args.out:
            write_new(args.out, output)
        print(output, end='')
        return int(bool(value.get('errors')) or (args.strict and (
            bool(value.get('gaps')) or not value.get('selected_adm_records_complete', False))))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
