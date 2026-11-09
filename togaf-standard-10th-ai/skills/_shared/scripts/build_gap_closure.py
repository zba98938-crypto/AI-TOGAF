#!/usr/bin/env python3
"""Build the 2026-11-05 standard-gap closure package from specs, tables and executed examples.

Writes (relative to _shared):
  capability-addenda/standard-gap-closure.json          addenda package for apply_capability_addenda.py
  capability-addenda/deliverable-bindings-standard-gaps.json
  references/capability-addenda/<work-product>.md       method, rules, executed example, counterexample
  references/source-tables/standard-gap-closure.json    source tables used by the calculators
  references/adm-phases.json                            adds guide_usage (other keys untouched)
Analysis results in the docs come from running the calculators on the fictional examples.
"""
import copy, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import gap_closure_examples as EX
import gap_closure_tables as T
from gap_closure_specs import SPECS, MEANINGS, ORIGIN, RULE, METHOD_NAMES, BINDINGS
from analyze import evaluate

CTX = {'domains': ['business', 'data', 'application', 'technology'], 'landscape': 'segment',
       'purpose': 'project', 'abstraction': 'logical', 'evolution': 'target'}
POLICY = '关键输入缺失时生成带ID的草稿与缺口，不计算无依据数值，不伪造批准或事实；结构错误直接拒绝。'

def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def semantics(fields):
    return {f: {'meaning': MEANINGS.get(f, f), 'value_rule': RULE, 'definition_origin': ORIGIN} for f in fields}

def specs_for(item, types, extra_checks=()):
    out = [{'id': 'checks-%d' % i, 'text': t, 'mode': 'review', 'source': 'checks'} for i, t in enumerate(item['checks'], 1)]
    out += [{'id': 'semantic_checks-%d' % i, 'text': t, 'mode': 'review', 'source': 'semantic_checks'} for i, t in enumerate(item.get('semantic_checks', []), 1)]
    if types:
        out.append({'id': 'typed-required-fields', 'text': '必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性）',
                    'mode': 'machine', 'source': 'field-contract', 'executor': 'field-values', 'code': 'field-contract-value',
                    'applies_to': {'entity_types': sorted(types)}})
    return out

def example_model(spec):
    sources, entities, build = getattr(EX, spec['example'])()
    aid = spec['id'] + '-analysis'
    view = {'id': spec['id'] + '-baseline', 'artifact_id': spec['id'], 'profile_id': spec['id'] + '-default',
            'title': spec['name'] + '／虚构星河零售', 'context': CTX, 'entity_ids': [e['id'] for e in entities], 'relationship_ids': [],
            'analysis': '从随包虚构原料提取字段，执行' + spec['method'] + '；规则为项目操作约定。',
            'legend': '虚构示例；同一ID在修改前后代表同一对象；嵌套记录按表可见。', 'attributes': {'analysis_ids': [aid]}}
    analysis = {'id': aid, 'method_id': spec['method'], 'inputs': build(entities)}
    return {'notice': '虚构星河零售教学案例；规则不是TOGAF规定，不代表批准。', 'sources': sources, 'entities': entities,
            'relationships': [], 'view': view, 'analyses': [analysis]}, build

def run(spec, entities, build):
    return evaluate({'id': 'x', 'method_id': spec['method'], 'inputs': build(entities)})['result']

def work_product(spec, example):
    fields = [f for fs in spec['types'].values() for f in fs]
    fields = ['name'] + list(dict.fromkeys(fields + spec['optional']))
    attrs = {k: v for k, v in semantics(fields[1:]).items()}
    misreadings = ['名称、来源表格和成功输出不等于业务结论已核实'] + spec['checks']
    status = {'definition': 'local-body-read; english-pdf-spot-checked; official-verification-separate', 'model': 'baseline-example-schema-valid',
              'analysis': 'calculator-executed-on-fictional-case', 'generation': 'two-layout-table-executed', 'modification': 'executed-with-result-change',
              'review': 'rule-checks-only; independent-business-review-pending', 'visual': 'not-applicable-table'}
    return {'id': spec['id'], 'artifact_id': spec['id'], 'name': spec['name'], 'name_zh': spec['name'], 'name_en': spec['en'],
            'owner': spec['owner'], 'kind': spec['kind'], 'renderer': 'catalog', 'notation': 'table', 'source_refs': spec['refs'],
            'definition_status': 'guide-work-product-with-project-operational-contract', 'decision': spec['decision'],
            'stakeholders': ['该范围业务负责人', '架构师', '评审及治理负责人'], 'concerns': [spec['decision'], '来源、范围与适用性'],
            'required_inputs': [{'id': f, 'meaning': MEANINGS.get(f, f), 'origin': 'source-purpose-plus-project-contract'} for f in fields[1:]],
            'optional_inputs': ['既有模型及历史结论'], 'missing_input_policy': POLICY,
            'entity_types': sorted(spec['types']), 'relationship_types': [], 'fields': fields,
            'required_attributes': copy.deepcopy(spec['types']), 'attribute_semantics': attrs,
            'analysis': spec['steps'], 'analysis_steps': spec['steps'], 'checks': spec['checks'], 'semantic_checks': spec['checks'],
            'misreadings': misreadings, 'output': ['范围及依据', '逐条结果与理由', '缺口、下一步与责任', '版本和来源引用'],
            'related_deliverables': spec['deliverables'], 'applicable_adm': spec['adm'], 'example': example,
            'implementation_status': status, 'method_reference': 'references/capability-addenda/' + spec['id'] + '.md',
            'case_ref': 'references/capability-addenda/' + spec['id'] + '.md',
            'counterexample': spec['_counter'], 'modification_example': spec['_modify']}

def profile(spec, example):
    pid = spec['id'] + '-default'
    return {'id': pid, 'artifact_id': spec['id'], 'name': spec['name'], 'name_zh': spec['name'], 'owner': spec['owner'], 'version': '1.0',
            'source_refs': spec['refs'], 'renderer': 'catalog', 'output_kind': 'table', 'entity_types': sorted(spec['types']),
            'relationship_types': [], 'required_attributes': copy.deepcopy(spec['types']),
            'checks': ['对象、关系、必要属性均可追溯并得到表达', '参考内容不自动成为项目事实；未知项保持显式'] + spec['checks'],
            'definition_status': 'source-derived-project-operational-contract',
            'template': {'id': pid, 'version': '1.0', 'source_verified': False, 'layout_notes': '按工作产品字段组织的记录表；来源无对应原图。',
                         'structure_basis': '正文定义的工作产品；记录表是项目操作表示法，不冒充来源原图'},
            'example': example, 'table_orientation': 'records', 'missing_input_policy': POLICY, 'analysis_steps': spec['steps'],
            'method_reference': 'references/capability-addenda/' + spec['id'] + '.md',
            'evidence_class': 'source-text', 'evidence_class_reason': 'source_refs 含正文锚点：' + '；'.join(spec['refs'])}

def method(spec):
    m = {'id': spec['method'], 'name': METHOD_NAMES[spec['method']], 'owner': spec['owner'], 'source_refs': spec['refs'],
         'required_inputs': [{'id': f, 'meaning': MEANINGS.get(f, f), 'origin': 'source-purpose-plus-project-contract'}
                             for fs in spec['types'].values() for f in fs],
         'missing_input_policy': POLICY, 'analysis_steps': spec['steps'], 'output_work_products': [spec['id']],
         'calculator_id': spec['method'], 'checks': spec['checks'], 'definition_status': 'source-purpose-with-explicit-project-operational-review',
         'implementation_status': 'calculator-executed-validation-pending', 'calculator_status': 'project-rule-implementation',
         'reference_document': 'references/capability-addenda/' + spec['id'] + '.md',
         'counterexample': spec['_counter']}
    m['check_specs'] = specs_for(m, ())
    return m

def attr(entities, ident):
    return next(e for e in entities if e['id'] == ident)['attributes']

# spec id -> (counterexample text, mutate, modification text, modify)
CASES = {
 'architecture-role-catalog': ('角色关系引用不存在的角色', lambda es: attr(es, 'ROLE-SOL').update(relationships=[{'id': 'REL-BROKEN', 'type': 'architecture_guidance', 'target': 'ROLE-NONE', 'scope': '示例', 'evidence': ['ROLE-R1']}]),
     '把首席架构师满意度KPI改为企业批准目标4/5并附证据', lambda es: attr(es, 'ROLE-CHIEF')['kpis'][0].update(target='4/5', target_origin='project-adopted', evidence=['ROLE-R2'])),
 'solution-delivery-notebook': ('规格S-1追溯到不存在的需求R-NONE', lambda es: attr(es, 'SDN-WP7')['specifications'][0].update(requirement_id='R-NONE'),
     '删除控制C-1', lambda es: attr(es, 'SDN-WP7').update(controls=[])),
 'product-constraint-register': ('待办B-3引用另一产品的约束', lambda es: attr(es, 'PCC-REG')['backlog_items'][0].update(product_id='P-ORDER'),
     '为B-3补记有证据的豁免D-1', lambda es: attr(es, 'PCC-REG')['backlog_items'][0].update(dispensation_id='D-1')),
 'domain-architecture-alignment': ('安全关注点引用不存在的领域', lambda es: attr(es, 'DOM-SEC').update(treated_as='concern', referenced_domain_ids=['DOM-NONE']),
     '数据领域改为服务EA-2027的OBJ-1并引用共享对象', lambda es: attr(es, 'DOM-DATA').update(project_id='EA-2027', objective_ids=['OBJ-1'], shared_entity_ids=['data-order'])),
 'incident-architecture-adjustment': ('需求变更引用不存在的目标', lambda es: attr(es, 'INC-31-ADJ')['requirement_changes'][0].update(objective_id='OBJ-NONE'),
     '只保留变更目标一种选项', lambda es: attr(es, 'INC-31-ADJ').update(options=[o for o in attr(es, 'INC-31-ADJ')['options'] if o['kind'] == 'change-target'])),
 'dtra-adm-phase-alignment': ('文化评分写为9', lambda es: attr(es, 'DAP-SUM')['factor_ratings'].update(culture=9),
     '删除阶段B的文化行动', lambda es: attr(es, 'DAP-B').update(actions=[{'id': 'ACT-B0', 'factor_ids': [], 'action': '仅记录含义'}])),
 'business-scenario-checklist-record': ('清单项状态写为passed', lambda es: attr(es, 'BSC-PLAN')['responses'].update({'plan-01': {'status': 'passed'}}),
     '删除规划阶段的角色分配', lambda es: attr(es, 'BSC-PLAN').update(role_assignments=[])),
 'smart-objective-assessment': ('目的O-1追溯到不存在的目标', lambda es: attr(es, 'O-1').update(goal_id='G-NONE'),
     '为O-2补负责人、行动、现实性证据与截止日期', lambda es: attr(es, 'O-2').update(baseline=10, action='录制标准操作视频', realism_rationale='试点门店验证',
                                                                     realism_evidence=['SMART-R2'], due='2027-03-31')),
}

def execute_cases(spec, example, build):
    counter, mutate, change, modify = CASES[spec['id']]
    base = run(spec, example['entities'], build)
    es = copy.deepcopy(example['entities']); mutate(es)
    try:
        run(spec, es, build); rejection = None
    except ValueError as error:
        rejection = str(error)
    if rejection is None:
        raise ValueError(spec['id'] + ': counterexample was not rejected')
    es = copy.deepcopy(example['entities']); modify(es)
    changed = run(spec, es, build)
    if changed == base:
        raise ValueError(spec['id'] + ': modification produced no result change')
    code = rejection.split(' ')[0]
    spec['_counter'] = {'input': counter, 'expected': code, 'why': rejection}
    spec['_modify'] = {'change': change, 'expected': '分析结果变化：' + delta(base, changed)}
    return base, changed, rejection

def delta(a, b):
    ga, gb = {g['id'] for g in a.get('gaps', [])}, {g['id'] for g in b.get('gaps', [])}
    parts = []
    if gb - ga: parts.append('新增缺口' + ','.join(sorted(gb - ga)))
    if ga - gb: parts.append('关闭缺口' + ','.join(sorted(ga - gb)))
    for key in ('blocked_item_ids', 'option_kinds', 'attention_factor_ids', 'open_item_ids'):
        if a.get(key) != b.get(key): parts.append(key + '：' + json.dumps(a.get(key), ensure_ascii=False) + '→' + json.dumps(b.get(key), ensure_ascii=False))
    if a.get('rows') != b.get('rows') and not parts: parts.append('逐行状态变化')
    return '；'.join(parts) or '结果结构变化'

RULES_BY_SPEC = {'architecture-role-catalog': T.ROLE_RULES, 'solution-delivery-notebook': T.NOTEBOOK_RULES,
                 'dtra-adm-phase-alignment': T.DTRA_RULES}

def doc(spec, example, base, changed, rejection):
    j = lambda v: '```json\n' + json.dumps(v, ensure_ascii=False, indent=2) + '\n```\n'
    t = '# ' + spec['name'] + '（' + spec['en'] + '）\n\n'
    t += '工作产品 `' + spec['id'] + '` · 视图 `' + spec['id'] + '-default` · 方法 `' + spec['method'] + '` · 主责 [' + spec['owner'] + '](../../../' + spec['owner'] + '/SKILL.md) · 常用ADM：' + spec['adm'] + '。\n\n'
    t += '来源：' + '；'.join(spec['refs']) + '。本地中文正文已逐节阅读，英文PDF已抽查对应段落。字段、规则与计算是项目操作约定，不冒充TOGAF强制规则；官方来源等价、专业充分性与业务批准另行评审。\n\n'
    t += '## 决策问题\n\n' + spec['decision'] + '\n\n## 字段\n\n'
    for typ, fs in spec['types'].items():
        t += '- `' + typ + '` 必填：' + '、'.join('`' + f + '`（' + MEANINGS.get(f, f) + '）' for f in fs) + '\n'
    if spec['optional']:
        t += '- 可选：' + '、'.join('`' + f + '`（' + MEANINGS.get(f, f) + '）' for f in spec['optional']) + '\n'
    t += '\n## 步骤\n\n' + ''.join('%d. %s\n' % (i, s) for i, s in enumerate(spec['steps'], 1))
    rules = RULES_BY_SPEC.get(spec['id'])
    if rules:
        t += '\n## 来源要点\n\n' + ''.join('- ' + r[1] + '（' + r[2] + '）\n' for r in rules)
    t += '\n## 判定\n\n结构错误（未知ID、追溯断裂、非法取值等）直接拒绝并返回错误码；缺输入或证据记为带ID的缺口，草稿仍可输出。角色关系依实际类型与明确采用的项目策略检查，位置或层级本身不证明人事汇报。检查要点：\n\n' + ''.join('- ' + c + '\n' for c in spec['checks'])
    t += '\n## 调用\n\n```sh\n"$TOGAF_SHARED/.venv/bin/python" "$TOGAF_SHARED/scripts/analyze.py" model.json --evaluate ' + spec['id'] + '-analysis\n'
    t += '"$TOGAF_SHARED/.venv/bin/python" "$TOGAF_SHARED/scripts/generate.py" model.json --profile ' + spec['id'] + '-default --out output\n```\n\n'
    t += '分析写在 `model.analyses`，由视图 `attributes.analysis_ids` 引用；`inputs.source_ids` 须列出所用来源。\n'
    t += '\n## 虚构案例（星河零售）\n\n原料：\n\n' + ''.join('- `' + s['id'] + '`：' + s['description'] + '\n' for s in example['sources'])
    t += '\n基线结果（实际执行计算器所得）：\n\n' + j(base)
    t += '\n修改：' + spec['_modify']['change'] + '。' + spec['_modify']['expected'] + '。修改后结果：\n\n' + j(changed)
    t += '\n反例：' + spec['_counter']['input'] + '。实际拒绝：`' + rejection + '`\n'
    t += '\n完整模型片段见 [能力注册](../capabilities/' + spec['id'] + '.md)。以上全部为虚构教学材料，不代表真实企业事实或批准。\n'
    return t

def patches():
    areas = [a[1] for a in T.QUESTION_AREAS]
    return [
     {'group': 'analysis_methods', 'id': 'scenario-elicitation', 'add': {
        'source_refs': ['G176 §7.1–7.2', 'G176 §8'],
        'analysis_steps': ['按G176 §7.2七个问题领域访谈：' + '；'.join(areas), '标记问题陈述是“做什么”还是“如何做”；过于具体或模糊时追问并记录追问',
                           '按G176 §8把主要发现放正文、细节放附录，模型编号并保持简洁'],
        'checks': ['问题陈述为“如何做”或不可行动时须有追问记录，不直接转为需求'],
        'check_specs': [{'id': 'checks-gap-closure-1', 'text': '问题陈述为“如何做”或不可行动时须有追问记录，不直接转为需求', 'mode': 'review', 'source': 'checks'}]}},
     {'group': 'work_products', 'id': 'business-scenario-document', 'add': {
        'source_refs': ['G176 §7–§11'],
        'analysis_steps': ['用business-scenario-checklist-record跟踪各步骤清单与角色', '用smart-objective-assessment把目的做成SMART'],
        'checks': ['业务场景各步骤清单和SMART目的分别记录，勾选完成不等于场景被接受'],
        'semantic_checks': ['业务场景各步骤清单和SMART目的分别记录，勾选完成不等于场景被接受'],
        'check_specs': [{'id': 'checks-gap-closure-1', 'text': '业务场景各步骤清单和SMART目的分别记录，勾选完成不等于场景被接受', 'mode': 'review', 'source': 'checks'},
                        {'id': 'semantic_checks-gap-closure-1', 'text': '业务场景各步骤清单和SMART目的分别记录，勾选完成不等于场景被接受', 'mode': 'review', 'source': 'semantic_checks'}]}},
    ]

def extend_overlays(patch_list):
    """field-contracts overlays replace check_specs wholesale; append the new specs there idempotently."""
    wanted = {(p['group'], p['id']): p['add']['check_specs'] for p in patch_list}
    for path in sorted((ROOT / 'capability-addenda').glob('field-contracts-*.json')):
        data = json.loads(path.read_text()); changed = False
        for p in data.get('patches', []):
            specs = wanted.get((p['group'], p['id']))
            if specs and 'check_specs' in p['set']:
                have = {s['id'] for s in p['set']['check_specs']}
                for s in specs:
                    if s['id'] not in have:
                        p['set']['check_specs'].append(copy.deepcopy(s)); changed = True
        if changed:
            path.write_text(patch_per_line(data) if path.read_text().startswith('{"') else
                            json.dumps(data, ensure_ascii=False, indent=2) + '\n')

def patch_per_line(data):
    """Keep the one-patch-per-line layout used by some field-contract overlay files."""
    head = json.dumps({k: v for k, v in data.items() if k != 'patches'}, ensure_ascii=False)[:-1]
    rows = ',\n'.join(json.dumps(p, ensure_ascii=False) for p in data['patches'])
    return head + ', "patches": [\n' + rows + '\n]}\n'

def write_guide_usage(path):
    """Set the guide_usage key textually so the hand-formatted rest of adm-phases.json is untouched."""
    text = path.read_text(); marker = ',\n  "guide_usage": '
    body = json.dumps(guide_usage(), ensure_ascii=False)
    if marker in text:
        text = text[:text.index(marker)] + '\n}\n'
    stripped = text.rstrip()
    require_close = stripped.endswith('}')
    if not require_close:
        raise ValueError('adm-phases.json does not end with an object')
    path.write_text(stripped[:-1].rstrip() + marker + body + '\n}\n')
    json.loads(path.read_text())

def guide_usage():
    return [{'guide_ref': g, 'phase': ph, 'usage': u, 'artifact_ids': a, 'method_ids': m,
             'basis': 'guide-statement; candidate use, not a mandatory phase output'} for g, ph, u, a, m in T.GUIDE_USAGE]

def main():
    package = {'package_id': 'standard-gap-closure-2026-11-05', 'version': '1.0', 'work_products': [], 'profiles': [],
               'analysis_methods': [], 'entity_definitions': {}, 'default_profiles': {}, 'candidate_resolutions': [], 'patches': patches()}
    existing_types = json.loads((ROOT / 'metamodel.json').read_text())['entity_types']
    for spec in SPECS:
        example, build = example_model(spec)
        base, changed, rejection = execute_cases(spec, example, build)
        package['work_products'].append(work_product(spec, example))
        package['profiles'].append(profile(spec, example))
        package['analysis_methods'].append(method(spec))
        for typ in spec['types']:
            # A changed review question must not redefine an existing entity
            # vocabulary. New workflow semantics live in its explicit contract.
            package['entity_definitions'][typ] = copy.deepcopy(existing_types.get(typ, {'meaning': spec['decision'], 'definition_origin': '/'.join(spec['refs']) + ' source-guided project work-product vocabulary'}))
        package['default_profiles'][spec['id']] = spec['id'] + '-default'
        package['candidate_resolutions'].append({'candidate_id': spec['id'], 'status': 'implemented-pending-independent-acceptance',
            'work_product_ids': [spec['id']], 'profile_ids': [spec['id'] + '-default'], 'analysis_method_ids': [spec['method']],
            'reason': '2026-11-05对标审查发现的未转化来源内容；工作产品与可执行审查，不是新TOGAF标准制品族'})
        (ROOT / 'references/capability-addenda' / (spec['id'] + '.md')).write_text(doc(spec, example, base, changed, rejection))
    for w in package['work_products']:
        w['check_specs'] = specs_for(w, w['required_attributes'])
    extend_overlays(package['patches'])
    dump(ROOT / 'capability-addenda/standard-gap-closure.json', package)
    dump(ROOT / 'capability-addenda/deliverable-bindings-standard-gaps.json', {'identity': 'explicit-conditional-bindings; never global selection', 'mappings': BINDINGS})
    dump(ROOT / 'references/source-tables/standard-gap-closure.json', {
        'notice': T.NOTICE, 'scenario_stages': T.SCENARIO_STAGES, 'scenario_roles': T.SCENARIO_ROLES, 'role_items': T.ROLE_ITEMS,
        'goal_categories': T.GOAL_CATEGORIES, 'smart_criteria': T.SMART_CRITERIA, 'question_areas': T.QUESTION_AREAS,
        'dtra_categories': T.DTRA_CATEGORIES, 'dtra_phases': T.DTRA_PHASES, 'dtra_rules': T.DTRA_RULES,
        'role_tiers': T.ROLE_TIERS, 'role_tier_notes': T.ROLE_TIER_NOTES, 'role_rules': T.ROLE_RULES,
        'notebook_sections': T.NOTEBOOK_SECTIONS, 'notebook_rules': T.NOTEBOOK_RULES, 'guide_usage': guide_usage()})
    write_guide_usage(ROOT / 'references/adm-phases.json')
    adm = json.loads((ROOT / 'references/adm-phases.json').read_text())
    print(json.dumps({'work_products': len(package['work_products']), 'methods': len(package['analysis_methods']),
                      'patches': len(package['patches']), 'guide_usage': len(adm['guide_usage'])}, ensure_ascii=False))

def sync_assembly():
    """After registration: add assembly metadata and optional bindings for the new profiles only.

    Same logic as sync_deliverable_profiles.py, scoped so unrelated profile metadata is not refreshed.
    """
    cap = json.loads((ROOT / 'capabilities.json').read_text())
    path = ROOT / 'capability-addenda/deliverable-assembly-rules.json'; rules = json.loads(path.read_text())
    profiles = {p['id']: p for p in cap['profiles']}; deliverables = {d['id']: d for d in rules['deliverables']}
    for spec in SPECS:
        pid = spec['id'] + '-default'; p = profiles[pid]
        rules['default_profiles'][spec['id']] = pid
        rules['profile_metadata'][pid] = {'version': p.get('version', '2.0'), 'template_id': p['template']['id'], 'template_version': p['template']['version'],
                                          'required_attributes': p['required_attributes'], 'relationship_requirements': {},
                                          'required_identity_fields': {}, 'source_refs': p['source_refs']}
    for pid, entries in BINDINGS.items():
        for did, title, focus in entries:
            d = deliverables[did]
            require_title = next(s for s in d['sections'] if s['title'] == title)
            gid = 'optional-' + did + '-' + pid
            group = next((g for g in d['conditional_groups'] if g['id'] == gid), None)
            if group is None:
                group = {'id': gid, 'profile_ids': [pid], 'artifact_ids': [], 'section_titles': [], 'content_focus': [],
                         'applicability': '仅项目显式选择该视图或声明该条件组时适用', 'activation': 'selected-explicit-profile-or-assembly.active_groups'}
                d['conditional_groups'].append(group)
            for key, value in (('section_titles', require_title['title']), ('content_focus', focus)):
                if value not in group[key]:
                    group[key].append(value)
    dump(path, rules)
    print(json.dumps({'assembly_profiles_added': len(SPECS), 'binding_entries': sum(len(v) for v in BINDINGS.values())}))

if __name__ == '__main__':
    sync_assembly() if '--assembly' in sys.argv else main()
