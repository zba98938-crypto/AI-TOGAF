#!/usr/bin/env python3
"""Plan and check an iterative ADM cycle against existing project model records.

This tool records no approvals, supplies no business facts, and never advances phases.
The executable contract is a project convention based on the local TOGAF guides.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import sys

import jsonschema
from requirements_trace import REQUIREMENT_TYPES
from strict_json import load as load_json

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / 'references' / 'adm-phases.json'
SCHEMA_PATH = ROOT / 'schemas' / 'adm-cycle.schema.json'
COLLECTIONS = ('entities', 'relationships', 'views', 'deliverables', 'analyses')


def load(path):
    return load_json(path)


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                    separators=(',', ':')).encode()).hexdigest()


def contracts():
    return {p['id']: p for p in load(CONTRACT_PATH)['phases']}


def model_projection(model, refs, include_incident=True):
    """Resolve selected records, their explicit ID references and incident edges.

    Incident edges are collected once for the explicitly selected entity closure;
    this does not recursively absorb the entire architecture through shared goals.
    Global project version/progress is deliberately not semantic phase input.
    """
    groups = (*COLLECTIONS, 'sources', 'states', 'scopes', 'scales', 'comparisons')
    index = {(group, record['id']): record for group in groups for record in model.get(group, [])}
    by_id = {identity: group for group, identity in index}

    def explicit_closure(selected):
        pending = list(selected)
        while pending:
            key = pending.pop()
            record = index.get(key)
            if record is None:
                continue
            def visit(value):
                if isinstance(value, dict):
                    for field, child in value.items():
                        if field != 'id':
                            visit(child)
                elif isinstance(value, list):
                    for child in value:
                        visit(child)
                elif isinstance(value, str) and value in by_id:
                    target = (by_id[value], value)
                    if target not in selected:
                        selected.add(target)
                        pending.append(target)
            visit(record)
        return selected

    selected = explicit_closure({(ref['collection'], ref['id']) for ref in refs})
    if include_incident:
        entity_ids = {identity for group, identity in selected if group == 'entities'}
        incident = {('relationships', edge['id']) for edge in model.get('relationships', [])
                    if edge['source'] in entity_ids or edge['target'] in entity_ids}
        selected = explicit_closure(selected | incident)
    project = model['project']
    return {'project': {key: project.get(key) for key in ('id', 'context', 'is_example')},
            'extensions': model.get('extensions', {}),
            'records': [{'collection': group, 'id': identity, 'record': index.get((group, identity))}
                        for group, identity in sorted(selected)]}


def iteration_fingerprint(model, iteration, scope):
    return digest({'scope': scope,
                   'binding': {key: iteration[key] for key in ('id', 'input_refs', 'output_refs', 'depends_on')},
                   'model': model_projection(
        model, iteration['input_refs'] + iteration['output_refs'])})


def requirements_fingerprint(model, cycle, phase):
    entities={e['id']:e for e in model['entities']}
    # A new version admitted by an explicitly scoped change does not rewrite the
    # immutable old baseline for unaffected phases. Editing an existing baseline
    # record still invalidates every review that used it.
    deferred=set()
    for change in cycle['requirements']['changes']:
        if phase in change['affected_phases'] or change.get('decision',{}).get('status')!='accepted':continue
        for identity in change['requirement_ids']:
            e=entities.get(identity,{})
            old=entities.get(e.get('attributes',{}).get('supersedes_id'),{})
            if old and old.get('concept_id') and old.get('concept_id')==e.get('concept_id') and old['id'] in cycle['requirements']['baseline_ids']:
                try:newer=int(e.get('version','0'))>int(old.get('version','0'))
                except (ValueError,TypeError):newer=False
                if newer:deferred.add(identity)
    refs = [{'collection': 'entities', 'id': identity} for identity in cycle['requirements']['baseline_ids'] if identity not in deferred]
    return digest({'scope': cycle['scope'], 'baseline': model_projection(model, refs, include_incident=True),
                   'changes': [change for change in cycle['requirements']['changes']
                               if phase in change['affected_phases']]})


def pending_decision():
    return {'status': 'pending', 'authority': '', 'authority_role': 'stakeholder',
            'rationale': '', 'evidence': []}


def source_coverage_template(definition):
    """Draft only: no step is performed or tailored merely by initialization."""
    return [{'source_step_id': step['id'], 'disposition': 'pending',
             'rationale': '', 'evidence': [], 'context_sha256': '',
             'source_step_sha256': digest(step)}
            for step in definition.get('source_step_records', [])]


def requirements_context(model, cycle):
    req = cycle['requirements']
    return digest({'scope': cycle['scope'], 'changes': req['changes'],
                   'baseline': model_projection(model, [
                       {'collection': 'entities', 'id': i} for i in req['baseline_ids']])})


def new_iteration(phase, number, reason):
    return {'id': f'{phase}-{number}', 'status': 'planned', 'reason': reason,
            'owner': '', 'input_refs': [], 'output_refs': [], 'depends_on': [],
            'criteria': {key: {'status': 'pending', 'rationale': '', 'evidence': []}
                         for key in contracts()[phase]['criteria']},
            'decision': pending_decision(), 'model_sha256': '', 'contract_sha256': '',
            'source_step_coverage': source_coverage_template(contracts()[phase])}


def initialize(model, cycle_id, scope):
    return {'schema_version': 'adm-cycle-1.0', 'id': cycle_id,
            'project_id': model['project']['id'], 'is_example': model['project']['is_example'],
            'scope': scope, 'phases': [
                {'phase': key, 'applicability': 'execute', 'tailoring_reason': '',
                 'tailoring_decision': pending_decision(),
                 'iterations': [new_iteration(key, 1, '本周期首次工作；范围及复用情况待确认')]}
                for key in contracts()],
            'requirements': {'owner': '', 'baseline_ids': [e['id'] for e in model['entities']
                             if e['type'] in REQUIREMENT_TYPES], 'no_requirements_reason': '',
                             'changes': [], 'reviews': [],
                             'source_step_coverage': source_coverage_template(
                                 load(CONTRACT_PATH)['requirements_management'])}}


def schema_issues(cycle):
    return [{'code': 'cycle-schema', 'id': '/'.join(map(str, e.absolute_path)),
             'message': e.message}
            for e in jsonschema.Draft202012Validator(load(SCHEMA_PATH)).iter_errors(cycle)]


def check_cycle(cycle, model, evidence_root):
    """Read-only. A complete result means consistent recorded evidence, not certification."""
    definitions = contracts()
    model_hash, contract_hash = digest(model), digest(load(CONTRACT_PATH))
    errors = schema_issues(cycle)
    project = model.get('project', {}) if isinstance(model, dict) else {}
    result = {'schema_version': 'adm-check-1.0', 'cycle_id': cycle.get('id') if isinstance(cycle, dict) else None,
              'model_sha256': model_hash, 'is_example': project.get('is_example') if isinstance(project, dict) else None,
              'errors': errors, 'phases': [], 'recorded_cycle_complete': False,
              'foundation_source_coverage_complete': False,
              'limit': '检查记录、引用、文件指纹与信息依赖；不验证签名真实性，不替代业务判断或正式批准。'}
    if errors:
        return result
    if not isinstance(model, dict):
        error = {'code': 'model-invalid', 'id': '', 'message': '共享模型必须是 JSON 对象。'}
        errors.append(error)
        return result

    def error(code, identity, message):
        errors.append({'code': code, 'id': identity, 'message': message})

    from validate import validate
    model_issues = validate(model)
    for issue in model_issues:
        if issue['level'] == 'error':
            error('model-invalid', issue['id'], issue['message'])
    result['model_warnings'] = [i for i in model_issues if i['level'] == 'warning']
    if any(e['code'] == 'model-invalid' for e in errors):
        return result
    if cycle['project_id'] != model['project']['id']:
        error('project-mismatch', cycle['id'], '周期与共享模型不属于同一项目。')
    if cycle['is_example'] != model['project']['is_example']:
        error('example-mismatch', cycle['id'], '周期必须继承共享模型的虚构示例身份。')
    indexes = {name: {r['id']: r for r in model.get(name, [])} for name in COLLECTIONS}

    def reference_issues(refs):
        return [f"引用不存在：{r['collection']}/{r['id']}" for r in refs
                if r['id'] not in indexes[r['collection']]]

    def evidence_issues(records):
        reasons = []
        if not records:
            return ['缺少带定位和当前哈希的证据文件']
        for record in records:
            path = Path(record['path'])
            path = path if path.is_absolute() else Path(evidence_root) / path
            try:
                if hashlib.sha256(path.read_bytes()).hexdigest() != record['sha256']:
                    reasons.append('证据文件已变化：' + record['path'])
            except OSError:
                reasons.append('证据文件不可读取：' + record['path'])
        return reasons

    def decision_issues(decision, accepted=True):
        reasons = []
        if accepted and decision['status'] != 'accepted':
            reasons.append('尚无实际接受决定')
        if decision['status'] != 'pending':
            if not decision['authority'].strip() or not decision['rationale'].strip():
                reasons.append('决定缺少决策权人或理由')
            reasons += evidence_issues(decision['evidence'])
            if decision['authority_role'] == 'delegate':
                reasons += evidence_issues(decision.get('delegation_evidence', []))
        return reasons

    def source_coverage(definition, records, context, identity):
        expected = {s['id']: s for s in definition.get('source_step_records', [])}
        provided = {}
        for record in records:
            sid = record['source_step_id']
            if sid in provided:
                error('source-step-duplicate', identity, '来源步骤重复：' + sid)
            if sid not in expected:
                error('source-step-unknown', identity, '来源步骤不属于本阶段：' + sid)
            provided[sid] = record
        gaps, resolved = [], []
        for sid, step in expected.items():
            record = provided.get(sid)
            reasons = []
            if not record or record['disposition'] == 'pending':
                reasons.append('来源步骤尚未处置')
            else:
                if not record['rationale'].strip():
                    reasons.append('执行、复用或裁剪缺少具体理由')
                reasons += evidence_issues(record['evidence'])
                if record['source_step_sha256'] != digest(step):
                    reasons.append('来源步骤契约已变化')
                if record['context_sha256'] != context:
                    reasons.append('本次模型或需求语境已变化，步骤证据需要复核')
            if reasons:
                gaps.append({'source_step_id': sid, 'name_en': step['name_en'],
                             'reasons': reasons})
            else:
                resolved.append(sid)
        return {'expected_count': len(expected), 'resolved_count': len(resolved),
                'complete': bool(expected) and not gaps and not (provided.keys() - expected.keys()),
                'current_context_sha256': context, 'gaps': gaps,
                'limit': '逐步骤记录检查；裁剪可用，脚本不判定专业分析充分性或授予批准。'}

    phases = {p['phase']: p for p in cycle['phases']}
    if len(phases) != len(definitions) or set(phases) != set(definitions):
        error('phase-identity', cycle['id'], 'Preliminary 和 A–H 必须各有且仅有一个阶段记录。')
        return result
    iterations = {}
    for phase in cycle['phases']:
        for iteration in phase['iterations']:
            if iteration['id'] in iterations:
                error('iteration-id', iteration['id'], '迭代 ID 重复。')
            iterations[iteration['id']] = (phase, iteration)
            for reason in reference_issues(iteration['input_refs'] + iteration['output_refs']):
                error('model-reference', iteration['id'], reason)
            if set(iteration['criteria']) != set(definitions[phase['phase']]['criteria']):
                error('criteria-contract', iteration['id'], '退出判据必须完整匹配当前阶段合同；裁剪用 not-applicable 加理由与证据。')
    for _, iteration in iterations.values():
        for dependency in iteration['depends_on']:
            if dependency not in iterations:
                error('dependency-reference', iteration['id'], '依赖迭代不存在：' + dependency)

    req = cycle['requirements']
    requirement_ids = {e['id'] for e in model['entities'] if e['type'] in REQUIREMENT_TYPES}
    if set(req['baseline_ids']) != requirement_ids:
        error('requirement-baseline', cycle['id'], '需求基线须覆盖本次模型的普通、安全和分析需求；先裁剪模型范围，勿静默漏项。')
    requirements_gaps = []
    if not req['owner'].strip():
        requirements_gaps.append('持续需求管理缺少责任人')
    if not requirement_ids and not req['no_requirements_reason'].strip():
        requirements_gaps.append('未捕获需求；须收集需求或说明本范围无需求的依据')
    for identity in requirement_ids:
        item = indexes['entities'][identity]
        attrs = item.get('attributes', {})
        if not attrs.get('owner') or not attrs.get('acceptance') or not item.get('evidence'):
            requirements_gaps.append('需求缺少责任人、可验证验收或来源：' + identity)
    changes = {}
    for change in req['changes']:
        if change['id'] in changes:
            error('change-id', change['id'], '需求变更 ID 重复。')
        changes[change['id']] = change
        for identity in change['requirement_ids']:
            if identity not in requirement_ids:
                error('change-requirement', change['id'], '需求不存在：' + identity)
        for reason in reference_issues(change['affected_refs']):
            error('change-reference', change['id'], reason)
        for reason in decision_issues(change['decision'], accepted=False):
            error('change-decision', change['id'], reason)
    reviews = {}
    for review in req['reviews']:
        identity = review['iteration_id']
        if identity in reviews:
            error('review-id', identity, '同一迭代重复需求复核；保留历史时使用新迭代 ID。')
        reviews[identity] = review
        if identity not in iterations:
            error('review-iteration', identity, '需求复核引用的迭代不存在。')
        if set(review['change_ids']) - set(changes):
            error('review-change', identity, '需求复核引用的变更不存在。')

    cache, visiting = {}, set()

    def iteration_gaps(identity):
        if identity in cache:
            return cache[identity]
        if identity in visiting:
            return ['退出信息依赖成环；应拆分可复用的信息版本或新迭代']
        visiting.add(identity)
        phase, it = iterations[identity]
        reasons = list(requirements_gaps)
        if not it['owner'].strip():
            reasons.append('阶段迭代缺少责任人')
        if it['model_sha256'] != iteration_fingerprint(model, it, cycle['scope']) or it['contract_sha256'] != contract_hash:
            reasons.append('模型或阶段合同未绑定/已变化，需要重审当前输入')
        if not it['input_refs'] or not it['output_refs']:
            reasons.append('须绑定实际输入与输出模型记录；交付物清单仅为建议')
        reasons += reference_issues(it['input_refs'] + it['output_refs'])
        for key in definitions[phase['phase']]['criteria']:
            record = it['criteria'].get(key)
            if not record or record['status'] == 'pending':
                reasons.append('退出判据待处理：' + key)
                continue
            if not record['rationale'].strip():
                reasons.append('退出判据缺少判断理由：' + key)
            reasons += [key + '：' + r for r in evidence_issues(record['evidence'])]
        review = reviews.get(identity)
        if not review:
            reasons.append('缺少本迭代的需求复核')
        else:
            if review['model_sha256'] != requirements_fingerprint(model, cycle, phase['phase']):
                reasons.append('需求复核已过期')
            reasons += evidence_issues(review['evidence'])
        for change in changes.values():
            if phase['phase'] not in change['affected_phases']:
                continue
            if change['decision']['status'] in ('pending', 'deferred'):
                reasons.append('受影响的需求变更尚未处置：' + change['id'])
            if not review or change['id'] not in review['change_ids']:
                reasons.append('需求变更后须复核/重开本阶段：' + change['id'])
        reasons += decision_issues(it['decision'])
        for dependency in it['depends_on']:
            if dependency not in iterations:
                reasons.append('依赖迭代不存在：' + dependency)
                continue
            if iterations[dependency][1]['status'] != 'completed' or iteration_gaps(dependency):
                reasons.append('所依赖信息未形成有效完成记录：' + dependency)
        visiting.remove(identity)
        cache[identity] = list(dict.fromkeys(reasons))
        return cache[identity]

    a = phases['A']['iterations'][-1]
    a_ready = a['status'] == 'completed' and not iteration_gaps(a['id']) and phases['A']['applicability'] != 'not-applicable'
    for key in definitions:
        phase = phases[key]
        current = phase['iterations'][-1]
        if phase['applicability'] == 'not-applicable':
            gaps = decision_issues(phase['tailoring_decision'])
            if current['model_sha256'] != iteration_fingerprint(model, current, cycle['scope']) or current['contract_sha256'] != contract_hash:
                gaps.append('裁剪适用的模型或阶段合同已变化，须重新判断不适用')
            if not phase['tailoring_reason'].strip():
                gaps.append('不适用裁剪缺少理由')
            if key == 'A':
                gaps.append('架构项目必须完成或复用阶段 A 的启动与目标设置，不能整体跳过')
            affected = [c for c in changes.values() if key in c['affected_phases']]
            if affected:
                review = reviews.get(current['id'])
                if not review or review['model_sha256'] != requirements_fingerprint(model, cycle, key):
                    gaps.append('需求变更后，须以当前模型重新复核不适用的范围依据')
                else:
                    gaps += evidence_issues(review['evidence'])
                for change in affected:
                    if (change['decision']['status'] in ('pending', 'deferred') or not review
                            or change['id'] not in review['change_ids']):
                        gaps.append('裁剪尚未处置/复核需求变更：' + change['id'])
            status = 'tailored-out' if not gaps else 'blocked'
        else:
            gaps = iteration_gaps(current['id'])
            if phase['applicability'] == 'reuse':
                if not phase['tailoring_reason'].strip():
                    gaps.append('复用缺少适用性及时效性说明')
                gaps += decision_issues(phase['tailoring_decision'])
            if key not in ('Preliminary', 'A') and not a_ready:
                gaps.append('阶段 A 的启动/授权记录尚不满足退出条件；可继续并行探索，但不可声明本阶段完成')
            status = ('recorded-complete' if current['status'] == 'completed' and not gaps else
                      'ready-for-recording' if not gaps else 'incomplete')
            if current['status'] == 'completed' and gaps:
                error('unsupported-completion', current['id'], '已声明完成但存在未解决退出条件。')
        result['phases'].append({'phase': key, 'name': definitions[key]['name'],
                                 'iteration_id': current['id'], 'status': status,
                                 'current_input_sha256': iteration_fingerprint(model, current, cycle['scope']),
                                 'current_requirements_sha256': requirements_fingerprint(model, cycle, key),
                                 'applicability': phase['applicability'], 'gaps': list(dict.fromkeys(gaps)),
                                 'owner_skills': definitions[key]['owners'],
                                 'suggested_deliverables': definitions[key]['deliverables']})
        result['phases'][-1]['source_step_coverage'] = source_coverage(
            definitions[key], current.get('source_step_coverage', []),
            iteration_fingerprint(model, current, cycle['scope']), current['id'])
    result['requirements_source_step_coverage'] = source_coverage(
        load(CONTRACT_PATH)['requirements_management'], req.get('source_step_coverage', []),
        requirements_context(model, cycle), 'Requirements')
    result['foundation_source_coverage_complete'] = not errors and all(
        p['source_step_coverage']['complete'] for p in result['phases']) and result[
            'requirements_source_step_coverage']['complete']
    result['recorded_cycle_complete'] = not errors and all(
        p['status'] in ('recorded-complete', 'tailored-out') for p in result['phases'])
    return result


def markdown_report(result):
    lines = ['# ADM 周期执行检查', '', f"周期：{result['cycle_id']}",
             f"模型指纹：`{result['model_sha256']}`", '', result['limit'], '',
             '虚构示例。' if result['is_example'] else '项目记录；真实批准由所引用的决策证据决定。', '',
             '| 阶段 | 迭代 | 记录状态 | 未闭合项 |', '| --- | --- | --- | --- |']
    for phase in result['phases']:
        lines.append(f"| {phase['phase']} {phase['name']} | {phase['iteration_id']} | {phase['status']} | {len(phase['gaps'])} |")
    lines += ['', '基础标准逐步骤记录：' + ('完整' if result.get('foundation_source_coverage_complete') else '存在缺口'),
              '项目退出记录与来源步骤覆盖分别计算；完整记录仍须实际语义评审。']
    for error in result['errors']:
        lines += ['', f"- 配置/一致性错误 `{error['code']}` ({error['id']})：{error['message']}"]
    if 'delivery_check' in result:
        from architecture_delivery import markdown
        lines += ['', markdown(result['delivery_check'])]
        if result.get('delivery_unmapped_phase_ids'):
            lines += ['', '周期内尚未建立成果工作映射的适用阶段：' + '、'.join(result['delivery_unmapped_phase_ids'])]
    for phase in result['phases']:
        lines += ['', '## ' + phase['phase'] + ' ' + phase['name'], '',
                  '主责技能：' + '、'.join(phase['owner_skills']), '',
                  '候选交付物（按关注点选择）：' + '、'.join(phase['suggested_deliverables']), '']
        lines += ['- ' + gap for gap in phase['gaps']] or ['当前所录证据和信息依赖一致；不代表脚本授予批准。']
        for gap in phase.get('source_step_coverage', {}).get('gaps', []):
            lines.append('- 来源步骤 '+gap['name_en']+'：'+'；'.join(gap['reasons']))
    for gap in result.get('requirements_source_step_coverage', {}).get('gaps', []):
        lines.append('- 持续需求管理 '+gap['name_en']+'：'+'；'.join(gap['reasons']))
    return '\n'.join(lines) + '\n'


def write_new(path, value):
    """Never overwrite a cycle, decision, or prior report accidentally."""
    with Path(path).open('x', encoding='utf-8') as stream:
        stream.write(value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest='command', required=True)
    init = subs.add_parser('init', help='创建未批准、未完成的 ADM 周期草稿')
    init.add_argument('--model', required=True)
    init.add_argument('--id', required=True)
    init.add_argument('--scope', required=True)
    init.add_argument('--out', required=True)
    flow = subs.add_parser('flow', help='生成完整ADM框架、制品映射与可编辑流程图')
    flow.add_argument('--out', required=True)
    flow.add_argument('--cycle', help='可选：实际周期文件；须同时提供 --model')
    flow.add_argument('--model', help='可选：与实际周期配套的共享模型')
    flow.add_argument('--render', action='store_true', help='复用本地渲染器保存PNG')
    for command in ('check', 'report', 'bind', 'iterate'):
        sub = subs.add_parser(command)
        sub.add_argument('--cycle', required=True)
        if command != 'iterate':
            sub.add_argument('--model', required=True)
        sub.add_argument('--out', required=command in ('bind', 'iterate'))
        if command in ('bind', 'iterate'):
            sub.add_argument('--phase', choices=list(contracts()), required=True)
        if command == 'iterate':
            sub.add_argument('--reason', required=True)
        if command == 'check':
            sub.add_argument('--require-complete', action='store_true', help='未闭合草稿也返回非零')
            sub.add_argument('--require-source-coverage', action='store_true', help='基础标准步骤证据未闭合返回非零')
        if command in ('check', 'report'):
            sub.add_argument('--delivery-plan', help='核对本次关注点、判据及成果工作映射')
            sub.add_argument('--products', help='generate.py 实际生成目录；配合 --delivery-plan')
    args = parser.parse_args()
    try:
        if args.command == 'flow':
            from adm_flow import generate_flow
            result = generate_flow(args.out, load(args.cycle) if args.cycle else None,
                                   load(args.model) if args.model else None,
                                   Path(args.cycle).resolve().parent if args.cycle else None,
                                   args.render)
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return int(result['status'] != 'passed')
        if args.command == 'init':
            write_new(args.out, initialize(load(args.model), args.id, args.scope))
            return 0
        cycle = load(args.cycle)
        invalid = schema_issues(cycle)
        if invalid:
            print(json.dumps({'errors': invalid}, ensure_ascii=False, indent=2))
            return 1
        if args.command in ('bind', 'iterate'):
            original_parent = Path(args.cycle).resolve().parent
            if Path(args.out).resolve().parent != original_parent:
                raise ValueError('副本须保存在原周期目录，以保持相对证据路径；跨目录迁移请显式重写并核查路径。')
            phase = next(p for p in cycle['phases'] if p['phase'] == args.phase)
            current = phase['iterations'][-1]
            if args.command == 'iterate':
                if not args.reason.strip():
                    raise ValueError('新迭代需要说明原因。')
                new = new_iteration(args.phase, len(phase['iterations']) + 1, args.reason)
                new['input_refs'] = copy.deepcopy(current['output_refs'])
                phase['iterations'].append(new)
            else:
                if (current['status'] == 'completed' or current['decision']['status'] != 'pending'
                        or phase['tailoring_decision']['status'] != 'pending') or any(
                        c['status'] != 'pending' for c in current['criteria'].values()):
                    raise ValueError('不得给已有判断/决定重新盖输入指纹；先创建新迭代，再核对证据。')
                model = load(args.model)
                if model['project']['id'] != cycle['project_id']:
                    raise ValueError('周期与模型项目不匹配。')
                current['model_sha256'] = iteration_fingerprint(model, current, cycle['scope'])
                current['contract_sha256'] = digest(load(CONTRACT_PATH))
            write_new(args.out, cycle)
            return 0
        report = check_cycle(cycle, load(args.model), Path(args.cycle).resolve().parent)
        if args.products and not args.delivery_plan:
            raise ValueError('--products 需要 --delivery-plan')
        if args.delivery_plan:
            from architecture_delivery import check as check_delivery
            delivery = check_delivery(load(args.delivery_plan), load(args.model), cycle,
                                      Path(args.cycle).resolve().parent, args.products)
            report['delivery_check'] = delivery
            selected = {p['phase'] for p in delivery['phases']}
            report['delivery_unmapped_phase_ids'] = [p['phase'] for p in cycle['phases']
                if p['applicability'] != 'not-applicable' and p['phase'] not in selected]
            if delivery['errors']:
                report['errors'].append({'code': 'delivery-plan-invalid', 'id': cycle['id'],
                                         'message': '架构成果计划有无效引用或身份冲突。'})
            if report['delivery_unmapped_phase_ids'] or not (delivery['structurally_linked'] and delivery['products_current']
                    and delivery['selected_adm_records_complete']):
                report['recorded_cycle_complete'] = False
        output = markdown_report(report) if args.command == 'report' else json.dumps(report, ensure_ascii=False, indent=2) + '\n'
        if args.out:
            write_new(args.out, output)
        print(output, end='')
        return int(bool(report['errors']) or (getattr(args, 'require_complete', False) and not report['recorded_cycle_complete'])
                   or (getattr(args, 'require_source_coverage', False) and not report['foundation_source_coverage_complete']))
    except (OSError, ValueError, KeyError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
