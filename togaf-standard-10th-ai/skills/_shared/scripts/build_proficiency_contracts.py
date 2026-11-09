#!/usr/bin/env python3
"""Refresh only G249 proficiency/development profiles and their owned references.

Reads the current registry before merging these records, preserving other agents'
capability work. Broad regeneration is intentionally not part of this command.
"""
import json
from pathlib import Path
from proficiency_contract import specialize, collaboration_profile, assignment_profile, method_contract

ROOT = Path(__file__).resolve().parents[1]


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def classify_checks(item, specs):
    """Keep existing machine assertions; register new professional review text."""
    for source in ('checks', 'semantic_checks'):
        for index, text in enumerate(item.get(source, [])):
            if not any(s.get('text') == text and s.get('source') == source for s in specs):
                identity = 'g249-' + source + '-' + str(index)
                specs[:] = [s for s in specs if s.get('id') != identity]
                specs.append({'id': identity, 'text': text, 'mode': 'review', 'source': source})
    return specs


def profile_text(profile):
    text = '# ' + profile['name'] + '\n\n'
    text += '`profile_id`: ' + profile['id'] + '；`artifact_id`: ' + profile['artifact_id'] + '。\n\n'
    text += '来源：' + '；'.join(profile['source_refs']) + '。字段与运行时检查为项目约定。\n\n'
    text += '表示族：`' + profile['renderer'] + '`。' + profile['template']['layout_notes'] + '。\n\n'
    text += '## 必需模型内容\n\n```json\n' + json.dumps(profile['required_attributes'], ensure_ascii=False, indent=2) + '\n```\n\n'
    if profile['artifact_id'] == 'architecture-skill-matrix':
        text += ('关系 `supports_role` 的属性须分别声明 `assessment_kind`、`assessment_state`、`scale_id`、`proficiency`；'
                 '原文目标另需 `reference_role_id`、`source_locator`；项目目标另需 `task_refs`、`tailoring_reason`、`behavioral_criteria`；'
                 '已评价个人另需 `person_ref`、`task_refs`、`assessor`、`observed_on`、`behavioral_evidence`。证据引用保留在关系 `evidence`。\n\n'
                 '原文目标状态为 `reference`；项目目标为 `proposed/adopted`；个人观察为 `unassessed/evidence_insufficient/assessed/superseded`。'
                 '未评估及证据不足使用null；缺新字段的旧草稿产生gap，非法值及语义矛盾报error。G249四级锚点不能作为agent权限或Open CA三级认证。\n\n')
    text += '## 检查\n\n' + '\n'.join('- ' + c for c in profile['checks']) + '\n\n'
    text += '## 完整示例片段\n\n示例不代表真实人员评价、业务批准或原图复刻。\n\n```json\n' + json.dumps(profile['example'], ensure_ascii=False, indent=2) + '\n```\n'
    return text


def main():
    meta_path = ROOT / 'metamodel.json'
    meta = json.loads(meta_path.read_text())
    targets = meta['relationships']['supports_role']['target_types']
    if 'guide:architecture-role' not in targets:
        targets.append('guide:architecture-role')
        save(meta_path, meta)
    path = ROOT / 'capabilities.json'
    caps = json.loads(path.read_text())
    changed = []
    for profile in caps['profiles']:
        if specialize(profile) is not None:
            changed.append(profile)
    for fresh in [collaboration_profile(), assignment_profile()]:
        previous = next((p for p in caps['profiles'] if p['id'] == fresh['id']), None)
        if previous is None:
            caps['profiles'].append(fresh)
        else:
            previous.update(fresh)
            fresh = previous
        changed.append(fresh)
    for work_product in caps['work_products']:
        if work_product['id'] not in {'architecture-skill-matrix', 'architecture-development-plan'}:
            continue
        default = next(p for p in changed if p['id'] == work_product['id'] + '-default')
        for key in ('required_attributes', 'entity_types', 'relationship_types', 'source_refs', 'example'):
            work_product[key] = default[key]
        work_product['fields'] = list(dict.fromkeys(f for fs in default['required_attributes'].values() for f in fs))
        work_product['semantic_checks'] = default['checks']
        from build_capabilities import attribute_contract
        from field_contract_addendum import RULES, schemas
        rules = {r.split('|', 2)[0]: r.split('|', 2)[1:] for r in RULES.strip().splitlines()}
        for field in work_product['fields']:
            sem = attribute_contract(field)
            if field in rules:
                typ, meaning = rules[field]
                sem.update(meaning=meaning, value_rule=meaning, value_schema=schemas()[typ])
            work_product.setdefault('attribute_semantics', {})[field] = sem
        text = '# ' + work_product['name_zh'] + '\n\n'
        text += '来源：' + '；'.join(default['source_refs']) + '。字段与流程为项目操作约定。\n\n'
        text += '使用[' + default['name'] + '视图契约](../profiles/' + default['id'] + '.md)；'
        text += '以[角色技能评估方法](../analysis-methods/architecture-role-skill-assessment.md)核对证据。\n\n'
        text += '\n'.join('- ' + c for c in default['checks']) + '\n'
        (ROOT / 'references/capabilities' / (work_product['id'] + '.md')).write_text(text)
    method = next(m for m in caps['analysis_methods'] if m['id'] == 'architecture-role-skill-assessment')
    method_contract(method)
    owned = {'architecture-skill-matrix', 'architecture-development-plan', 'architecture-role-skill-assessment'}
    items = {item['id']: item for group in ('work_products', 'analysis_methods') for item in caps[group] if item['id'] in owned}
    for item in items.values():
        classify_checks(item, item.setdefault('check_specs', []))
    overlay = ROOT / 'capability-addenda/field-contracts.json'
    for filename in json.loads(overlay.read_text())['packages']:
        package_path = overlay.parent / filename
        package = json.loads(package_path.read_text())
        touched = False
        for patch in package['patches']:
            if patch['id'] in items and 'check_specs' in patch['set']:
                classify_checks(items[patch['id']], patch['set']['check_specs'])
                touched = True
        if touched:
            save(package_path, package)
    save(path, caps)
    for profile in changed:
        (ROOT / 'references/profiles' / (profile['id'] + '.md')).write_text(profile_text(profile))
    text = '# 角色技能差距评估\n\n方法ID：`architecture-role-skill-assessment`。当前依据G249 §3–6；G198仅用于历史对照。\n\n'
    text += '步骤与输入结构为项目操作约定；执行器只检查显式证据和规则，不能授予任职、治理授权或认证。\n\n'
    text += '## 输入与步骤\n\n' + '\n'.join(str(i) + '. ' + step for i, step in enumerate(method['analysis_steps'], 1)) + '\n\n'
    text += '输入包括：' + '；'.join(method['required_inputs']) + '。\n\n'
    text += '## 执行与验收\n\n`analyses[].method_id` 使用 `architecture-role-skill-assessment`；通过 `analyze.py model.json --evaluate <analysis-id>` 执行。\n\n'
    text += '未知保留null或带ID缺口；非法等级拒绝；原文、裁剪与观察三种记录分别保留；四级技能熟练度不转换为Open CA三级认证或agent权限。\n\n'
    text += '[任务与共享模型绑定示例](../profiles/architecture-work-assignment-review.md)展示完整输入；[角色技能矩阵](../profiles/ea-skill-role-proficiency.md)、[人员发展计划](../profiles/architecture-development-plan-default.md)给出输出契约。\n\n'
    text += '字段、证据与复评约束见[G249运行时契约](../g249/runtime-contract.md)。\n\n'
    text += '[区分人员熟练度、角色目标与团队容量](../method-cases/architecture-role-skill-assessment.md)演练项目行为锚点与证据不足；项目锚点不得冒充G249逐字定义。\n'
    (ROOT / 'references/analysis-methods/architecture-role-skill-assessment.md').write_text(text)
    print(json.dumps({'profiles': [p['id'] for p in changed], 'method': method['id']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
