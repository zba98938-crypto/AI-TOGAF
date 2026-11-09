"""Persist inspectable three-level schedules and independent strict-mode failures."""
import argparse
import copy
import json
from datetime import date
from pathlib import Path
from generate import generate
from registry import load
from schedule_semantics import hierarchy, check_schedule


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def run(out, render=True):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=False)
    profile = load()[2]['architecture-project-schedule-default']
    model = copy.deepcopy(profile['example'])
    view = model.pop('view')
    model.pop('notice', None)
    context = {'domains': ['business', 'data', 'application', 'technology'],
               'landscape': 'segment', 'purpose': 'project', 'abstraction': 'logical',
               'evolution': 'target'}
    model.update(schema_version='2.0', project={'id': 'focused-schedule',
        'name': '模拟三层ADM候选排期', 'version': '1', 'context': context,
        'is_example': True, 'approval_status': 'candidate',
        'implementation_status': 'not-started'}, deliverables=[], gaps=[])
    template = model['entities'][0]
    rows = [('root', '项目汇总', '2026-11-01', '2026-11-30', None, False),
            ('mid', '阶段与跨域分析', '2026-11-02', '2026-11-20', 'root', False),
            ('leaf', '接口与时标验证', '2026-11-03', '2026-11-05', 'mid', False),
            ('gate', '候选评审门禁', '2026-11-06', '2026-11-06', 'mid', True)]
    entities = []
    for i, (identity, name, start, end, parent, milestone) in enumerate(rows):
        entity = copy.deepcopy(template)
        entity.update(id=identity, name=name)
        entity['attributes'].update(start=start, end=end, parent_id=parent,
            milestone=milestone if milestone else '完成接口分析后提交候选评审（说明文字）',
            duration=(date.fromisoformat(end)-date.fromisoformat(start)).days,
            duration_unit='elapsed-calendar-days', order=i+1,
            resource='虚构分析与评审角色；实际排班未知', predecessor='见显式层级与门禁')
        entities.append(entity)
    model.update(entities=entities, relationships=[], views=[view])
    view.update(id='three-level-schedule', entity_ids=[e['id'] for e in entities],
                relationship_ids=[], context=context,
                title='三层排期、持续任务与同日里程碑／模拟设计')
    save(out/'valid-model.json', model)
    checks = {'schedule_errors': check_schedule(entities),
              'expected_depths': [0, 1, 2, 2],
              'actual_depths': [depth for _, depth in hierarchy(entities)[0]]}
    for layout in ['reference', 'adaptive']:
        manifest = generate(model, out/layout, all_items=True, render=render,
                            layout=layout, strict=True)
        assert all(a['status'] != 'draft-with-gaps' for a in manifest['artifacts'])
    mutations = [
        ('orphan', 'schedule-parent-missing', lambda es: es[2]['attributes'].update(parent_id='absent')),
        ('cycle', 'schedule-parent-cycle', lambda es: es[0]['attributes'].update(parent_id='leaf')),
        ('outside', 'schedule-child-outside-parent', lambda es: es[2]['attributes'].update(end='2026-12-01')),
        ('date', 'missing-or-invalid-schedule', lambda es: es[2]['attributes'].update(start='2026-02-30')),
        ('milestone', 'schedule-milestone-duration', lambda es: es[3]['attributes'].update(end='2026-11-07'))]
    negatives = []
    for name, expected, mutate in mutations:
        changed = copy.deepcopy(model)
        mutate(changed['entities'])
        folder = out/'negatives'/name
        save(folder/'input.json', changed)
        diagnostics = check_schedule(changed['entities'])
        rejected = False
        try:
            generate(changed, folder/'strict', all_items=True, strict=True)
        except ValueError:
            rejected = True
        draft = generate(changed, folder/'draft', all_items=True)
        row = {'name': name, 'expected_diagnostic': expected, 'diagnostics': diagnostics,
               'strict_rejected': rejected,
               'draft_disclosed': all(a['status']=='draft-with-gaps' for a in draft['artifacts'])}
        save(folder/'result.json', row)
        negatives.append(row)
    checks['negatives'] = negatives
    checks['passed'] = not checks['schedule_errors'] and checks['actual_depths']==checks['expected_depths'] and all(
        r['strict_rejected'] and r['draft_disclosed'] and r['expected_diagnostic'] in {d['code'] for d in r['diagnostics']}
        for r in negatives)
    save(out/'summary.json', checks)
    return checks


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out', required=True)
    p.add_argument('--no-render', action='store_true')
    a = p.parse_args()
    raise SystemExit(0 if run(a.out, not a.no_render)['passed'] else 1)
