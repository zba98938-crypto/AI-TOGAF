#!/usr/bin/env python3
"""Generate four complete reference-row overlays from new fictional materials.

The source identity fields come from the registered reference rows. All local
judgments come from the separately authored supplement, including the missing
and changed evidence variants. This is a model-to-artifact run, not a blind
Agent method execution, application rehearsal or business acceptance.
"""
import argparse
import copy
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHARED = ROOT / 'skills/_shared'
MATERIALS = SHARED / 'references/method-case-materials/procedural-supplements'
sys.path.insert(0, str(SHARED / 'scripts'))
from generate import generate
from profile_examples import normalize_example

PROFILES = {
    'bi-business-function-coverage': (54, 'G238-T4-2-04'),
    'bi-application-function-coverage': (59, 'G238-T4-3-20'),
    'mdm-business-function-coverage': (29, 'G21B-T5-3-02'),
    'mdm-application-function-coverage': (38, 'G21B-T5-4-16'),
}
STATES = ('evidenced-in-example', 'planned', 'unknown', 'out-of-scope-with-reason')
EXPECTED = {
    'bi-business-function-coverage': {'sufficient': [1, 1, 52, 0], 'missing': [0, 0, 54, 0], 'changed': [0, 1, 53, 0]},
    'bi-application-function-coverage': {'sufficient': [1, 0, 58, 0], 'missing': [0, 0, 59, 0], 'changed': [0, 0, 59, 0]},
    'mdm-business-function-coverage': {'sufficient': [1, 0, 28, 0], 'missing': [0, 0, 29, 0], 'changed': [0, 0, 29, 0]},
    'mdm-application-function-coverage': {'sufficient': [1, 0, 37, 0], 'missing': [0, 0, 38, 0], 'changed': [0, 0, 38, 0]},
}
CHANGES = {
    'bi-business-function-coverage': '撤回U1/U2合格用途审核记录；清单存在不能支持合格用途维护判断',
    'bi-application-function-coverage': '当前范围改为新的三馆试点；旧两城库存夜批记录保留为历史但不能证明新范围批交换',
    'mdm-business-function-coverage': '撤回管家接受与BAU活动记录；所有者愿任不能证明本范围所有者与管家均已吸纳',
    'mdm-application-function-coverage': '人工取消合并演练缺少恢复后的两来源键映射；只有请求和原始误合并记录不足',
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def candidate_model(profile, supplement, variant):
    model = normalize_example(profile)
    pid = profile['id']
    model['project'].update(id='supplement-' + pid + '-' + variant,
                            name='本轮独立虚构教学：' + profile['name'] + ' / ' + variant,
                            version='20261108-' + variant)
    rows = {r['reference_id']: copy.deepcopy(r) for r in supplement['candidate_records']}
    reference = {r['entity_id']: r['reference_attributes'] for r in supplement['reference_rows']}
    inputs = copy.deepcopy(supplement['fictional_input_records'])
    if variant == 'missing':
        inputs = []
        for row in rows.values():
            row.update(coverage_status='unknown', implementation_ref='unknown', evidence_ids=[],
                       project_evidence='本变体未提供匹配该源行定义的材料；不能推出功能不存在')
    if variant == 'changed':
        rid = PROFILES[pid][1]
        rows[rid].update(coverage_status='unknown', implementation_ref='unknown', evidence_ids=[],
                         project_evidence=CHANGES[pid])
        # Historical records are retained, with an explicit current-scope restriction.
        record = next(r for r in inputs if r['id'] == 'SUP-' + rid)
        record['current_judgment_restriction'] = CHANGES[pid]
    model['sources'] = [{'id': 'SUP-input', 'kind': 'example',
                         'description': '2026-11-08新增虚构材料；未知不等于不存在；本生成仅执行候选模型的表达。',
                         'locator': str((MATERIALS / (pid + '-method.json')).relative_to(ROOT))}]
    model['sources'] += [{'id': r['id'], 'kind': 'example',
                          'description': json.dumps(r, ensure_ascii=False),
                          'locator': 'fictional_input_records/' + r['id']} for r in inputs]
    for entity in model['entities']:
        attrs = copy.deepcopy(reference[entity['id']])
        row = rows[attrs['reference_id']]
        attrs.update(project_scope=row['project_scope'], coverage_status=row['coverage_status'],
                     implementation_ref=row['implementation_ref'], evidence_detail=row['project_evidence'],
                     gap_action=row['gap_action'], proposed_owner=row['proposed_owner'], next_review=row['next_review'])
        if row['coverage_status'] == 'planned':
            attrs.update(plan_owner=row['plan_owner'], plan_date=row['plan_date'], plan_acceptance=row['plan_acceptance'])
        if row.get('scope_status'):
            attrs['scope_status'] = row['scope_status']
        entity.update(attributes=attrs, evidence=['SUP-input'] + row['evidence_ids'], certainty='assumed',
                      approval_status='candidate', implementation_status='unknown')
    view = model['views'][0]
    view.update(title='本轮新增虚构材料逐行覆盖 / ' + variant,
                analysis='采用补充JSON的参考身份与独立候选判断；生成完整行式制品，不授业务能力、原文等价或应用运行验收。',
                legend='已见仅指新增虚构材料中的匹配观察；计划/未知/范围外分别保存，不计算成熟度。')
    return model


def run(out):
    registry = {p['id']: p for p in json.loads((SHARED / 'capabilities.json').read_text())['profiles']}
    result = {'scope': 'four complete reference-row overlays, three authored evidence variants each',
              'accepted': False, 'blind_agent_method_execution': 'not-run',
              'application_execution': 'not-run', 'business_acceptance': 'not-accepted', 'runs': []}
    for pid, (total, _) in PROFILES.items():
        path = MATERIALS / (pid + '-method.json')
        supplement = json.loads(path.read_text())
        for variant in ('sufficient', 'missing', 'changed'):
            record = {'profile_id': pid, 'method_id': pid + '-method', 'variant': variant,
                      'supplement_sha256': sha(path), 'expected_state_counts': dict(zip(STATES, EXPECTED[pid][variant])),
                      'approval_status': 'candidate', 'accepted': False}
            try:
                model = candidate_model(registry[pid], supplement, variant)
                counts = Counter(e['attributes']['coverage_status'] for e in model['entities'])
                if len(model['entities']) != total or [counts[s] for s in STATES] != EXPECTED[pid][variant]:
                    raise ValueError('authored input transformation differs from the independent declared expectation')
                destination = out / pid / variant
                generate(model, destination, all_items=True, strict=True, render=False)
                manifest = json.loads((destination / 'manifest.json').read_text())
                artifact_path = destination / 'artifacts' / (model['views'][0]['id'] + '.md')
                content = artifact_path.read_text()
                if any(e['id'] not in content or e['attributes']['reference_id'] not in content for e in model['entities']):
                    raise ValueError('generated table omitted a reference/entity identity')
                if variant == 'changed' and CHANGES[pid] not in content:
                    raise ValueError('changed evidence restriction missing from generated table')
                record.update(passed=True, observed_state_counts=dict(zip(STATES, [counts[s] for s in STATES])),
                              generator_run_id=manifest['run_id'], generated_output=str(destination),
                              model_sha256=sha(destination / 'model.json'), artifact_sha256=sha(artifact_path),
                              manifest_sha256=sha(destination / 'manifest.json'),
                              executed_operation='strict common-model validation and full table generation')
            except (OSError, ValueError, KeyError, TypeError) as exc:
                record.update(passed=False, error=str(exc))
            result['runs'].append(record)
    result['passed'] = all(r['passed'] for r in result['runs'])
    out.mkdir(parents=True, exist_ok=True)
    (out / 'summary.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    result = run(parser.parse_args().out.resolve())
    print(json.dumps({'passed': result['passed'], 'runs': len(result['runs']),
                      'failed': [r for r in result['runs'] if not r['passed']], 'accepted': False}, ensure_ascii=False))
    return int(not result['passed'])


if __name__ == '__main__':
    raise SystemExit(main())
