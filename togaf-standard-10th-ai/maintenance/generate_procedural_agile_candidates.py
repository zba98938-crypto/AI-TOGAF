#!/usr/bin/env python3
"""Actually generate two layouts for current and next-cycle agile candidates.

Existing example entities/relationships are preserved byte-for-byte in canonical
JSON form; a fourth sprint is appended. The next-cycle option remains an
unauthorized candidate. Raster generation and encoded invariants are engineering
evidence, not historical sprint execution or human acceptance.
"""
import argparse
import copy
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHARED = ROOT / 'skills/_shared'
SUPPLEMENT = SHARED / 'references/method-case-materials/procedural-supplements/agile-collaboration-selection-switch.json'
sys.path.insert(0, str(SHARED / 'scripts'))
from generate import generate
from profile_examples import normalize_example


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def build(profile, data):
    model = normalize_example(profile)
    prefix = 'solution' if profile['id'] == 'agile-solution-collaboration' else 'functional'
    old = copy.deepcopy({'entities': model['entities'], 'relationships': model['relationships']})
    model['project'].update(id='procedural-' + prefix, name='独立虚构候选：第4轮与未授权周期切换', version='20261108')
    for source in model['sources']:
        if source['id'] == 'raw-agile':
            source['locator'] = 'skills/_shared/references/method-cases/agile-collaboration-selection-switch.md'
            source['description'] = '当前保存的R01–R08虚构资料；它是候选计划历史，不证明真实冲刺已执行。'
    model['sources'].append({'id': 'SUP-SWITCH', 'kind': 'example',
                             'description': json.dumps(data, ensure_ascii=False),
                             'locator': str(SUPPLEMENT.relative_to(ROOT))})
    additions = []
    for original in old['entities']:
        if original['id'].endswith('3'):
            row = copy.deepcopy(original)
            row['id'] = row['id'][:-1] + '4'
            row['name'] = row['name'].replace('冲刺…（本例3）', '冲刺4').replace('DORP3', 'DORP4')
            attrs = row['attributes']
            if row['type'] == 'guide:agile_sprint':
                attrs.update(order=4, goal='无障碍确认（验收待补）', display_label='冲刺4')
            else:
                attrs['sprint_ref'] = prefix + '-s4'
            if row['type'] == 'guide:dorp_gate':
                attrs['outputs'] = [{'id': prefix + '-MVP4', 'kind': 'MVP',
                                     'lane': 'solution' if prefix == 'solution' else 'mixed',
                                     'necessity': 'optional', 'meaning': '新增候选演示；验收待补，不宣称完成'}]
                attrs['unfinished_return'] = 'B-BOOK/B-CANCEL/G-PRIV及未完成无障碍项保持ID回到待办'
            if row['type'] == 'guide:agile_activity':
                attrs.update(work='第4轮无障碍确认候选工作；验收、隐私与委员会授权均待补',
                             selection_basis='SUP两队范围限定材料；跨职能仅下一周期候选，授权pending')
            row['evidence'] = ['SUP-SWITCH']
            additions.append(row)
    model['entities'].extend(additions)
    edges = []
    for original in old['relationships']:
        if original['id'].endswith('2') and original['type'] == 'guide:agile_continues':
            row = copy.deepcopy(original)
            row.update(id=row['id'][:-1] + '3', source=row['source'][:-1] + '3', target=row['target'][:-1] + '4', evidence=['SUP-SWITCH'])
            edges.append(row)
        if original['id'].endswith('3') and original['type'] == 'guide:agile_collaborates':
            row = copy.deepcopy(original)
            row.update(id=row['id'][:-1] + '4', source=row['source'][:-1] + '4', target=row['target'][:-1] + '4', evidence=['SUP-SWITCH'])
            edges.append(row)
    model['relationships'].extend(edges)
    view = model['views'][0]
    view['entity_ids'].extend(row['id'] for row in additions)
    view['relationship_ids'].extend(row['id'] for row in edges)
    view.update(title='第4轮与周期切换候选：' + profile['name'],
                analysis='新增范围限定的两队六份能力材料，委员会授权pending；当前保留解决方案协作，跨职能为下一周期候选。第4轮可独立扩展，旧候选历史不改。',
                legend=view['legend'] + '；切换未授权，第四轮验收未取得；两布局不等于原图等价或真实冲刺已执行。')
    model['gaps'] = [{'id': 'SUP-AUTH', 'description': '委员会授权pending及G-PRIV隐私缺口',
                      'impact': '下一周期跨职能选项不能成为已授权模式', 'needed_input': '具体范围的委员会复核与授权记录'},
                     {'id': 'SUP-ACCEPT4', 'description': '第4轮无障碍确认验收未取得',
                      'impact': '候选工作不得声明完成', 'needed_input': '业务责任人定义并验证无障碍确认退出条件'}]
    if digest({'entities': model['entities'][:len(old['entities'])], 'relationships': model['relationships'][:len(old['relationships'])]}) != digest(old):
        raise ValueError('old candidate history changed')
    if any(o['kind'] in ('MVA', 'MVP', 'MVBD') for e in model['entities'] if e['id'] == prefix + '-dorp0' for o in e['attributes']['outputs']):
        raise ValueError('sprint zero has an invented increment')
    return model, digest(old)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    out = parser.parse_args().out.resolve()
    caps = {p['id']: p for p in json.loads((SHARED / 'capabilities.json').read_text())['profiles']}
    data = json.loads(SUPPLEMENT.read_text())
    result = {'accepted': False, 'scope': 'two layouts for current/next-cycle candidate plans with appended sprint4',
              'blind_agent_method_execution': 'not-run', 'real_sprint_execution': 'not-run', 'business_acceptance': 'not-accepted', 'runs': []}
    for pid in ('agile-solution-collaboration', 'agile-cross-functional'):
        model, history_hash = build(caps[pid], data)
        for layout in ('reference', 'adaptive'):
            row = {'profile_id': pid, 'layout': layout, 'accepted': False, 'old_candidate_history_sha256': history_hash,
                   'supplement_sha256': hashlib.sha256(SUPPLEMENT.read_bytes()).hexdigest()}
            try:
                destination = out / pid / layout
                generate(model, destination, all_items=True, strict=True, layout=layout, render=True)
                vid = model['views'][0]['id']
                report = json.loads((destination / 'artifacts' / (vid + '.coverage.json')).read_text())
                if set(report['represented_entity_ids']) != set(model['views'][0]['entity_ids']) or set(report['represented_relationship_ids']) != set(model['views'][0]['relationship_ids']):
                    raise ValueError('layout omitted an input entity or relationship')
                png = destination / 'artifacts' / (vid + '.png')
                if not png.is_file() or not png.stat().st_size:
                    raise ValueError('actual PNG absent')
                row.update(passed=True, generated_output=str(destination),
                           svg_sha256=hashlib.sha256((destination / 'artifacts' / (vid + '.svg')).read_bytes()).hexdigest(),
                           png_sha256=hashlib.sha256(png.read_bytes()).hexdigest(),
                           manifest_sha256=hashlib.sha256((destination / 'manifest.json').read_bytes()).hexdigest(),
                           actual_operation='strict candidate generation and SVG-to-PNG rasterization')
            except (OSError, ValueError, KeyError, TypeError) as exc:
                row.update(passed=False, error=str(exc))
            result['runs'].append(row)
    result['passed'] = all(r['passed'] for r in result['runs'])
    out.mkdir(parents=True, exist_ok=True)
    (out / 'summary.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'passed': result['passed'], 'runs': len(result['runs']),
                      'failed': [r for r in result['runs'] if not r['passed']], 'accepted': False}, ensure_ascii=False))
    return int(not result['passed'])


if __name__ == '__main__':
    raise SystemExit(main())
