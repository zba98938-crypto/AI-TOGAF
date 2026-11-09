#!/usr/bin/env python3
"""New-run-only synthetic inventory scale rehearsal, NOT production benchmarking.

Historical random attributes are retained only as inventory pressure. New registered
types get explicitly marked example-derived synthetic supplements, never historical
enterprise facts. Professional contract acceptance is never inferred. T0 is an exact T1
subset; T2 counts are derived from the live demand/volume contract. A small,
explicitly authored arithmetic fixture is repeated across six synthetic sites.
"""
import argparse
from collections import Counter, defaultdict
import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import random
import shutil
import time

from build_data_volume_model import build as build_volume
from scale_oracle import audit

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / 'examples/qianlin-synthetic'
MUTATIONS = {'material': 'product_p2o5_t', 'energy': 'electric_kwh',
             'amount': 'invoice_cny', 'inventory': 'closing_product_t',
             'byproduct': 'closing_gypsum_t'}


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + '\n')


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def build_inventories(dataset_dir=None):
    dataset_dir = Path(dataset_dir or CASE / "dataset")
    original = []
    for path in sorted((dataset_dir / 'context').glob('*.json')):
        original.extend(json.loads(path.read_text())['entities'])
    if not original:
        raise ValueError('empty-context-inventory')
    by_type = defaultdict(list)
    for entity in original:
        by_type[entity['type']].append(entity)
    volume = build_volume()
    # Keep every archived entity byte-for-byte. Do not retrofit new types into
    # historical source files; supplement the new run from declared examples.
    caps = json.loads((ROOT / 'capabilities.json').read_text())
    seeds = {}
    for profile in caps['profiles']:
        for entity in profile.get('example', {}).get('entities', []):
            seeds.setdefault(entity['type'], (entity, profile['id']))
    for row in volume['records']:
        kind = row['entity_type']
        shortfall = max(0, row['instances']['T0'] - len(by_type[kind]))
        if shortfall and kind not in seeds:
            raise ValueError('No explicit registered example for supplemental scale type: ' + kind)
        for n in range(shortfall):
            seed, profile_id = seeds[kind]
            entity = copy.deepcopy(seed)
            entity['id'] = 'SCALE-SUPPLEMENT-' + kind.replace(':', '_') + '-' + str(n + 1)
            entity['concept_id'] = 'CONCEPT-' + entity['id']
            entity.setdefault('attributes', {}).update(
                scale_inventory_origin='current-registry-synthetic-supplement',
                scale_example_profile=profile_id, scale_example_id=seed['id'])
            entity['certainty'] = 'assumed'
            entity['evidence'] = ['SCALE-CURRENT-REGISTRY']
            entity['evolution'] = 'baseline'
            entity['context'] = {**copy.deepcopy(original[0]['context']),
                                 **entity.get('context', {}), 'evolution': 'baseline'}
            original.append(entity)
            by_type[kind].append(entity)
    small, large = [], []
    for row in volume['records']:
        kind = row['entity_type']
        pool = by_type[kind]
        if len(pool) < row['instances']['T0']:
            raise ValueError('T1 inventory cannot support exact T0 subset: ' + kind)
        small.extend(copy.deepcopy(pool[:row['instances']['T0']]))
        for n in range(row['instances']['T2']):
            e = copy.deepcopy(pool[n % len(pool)])
            e['id'] = 'SCALE-' + kind.replace(':', '_') + '-' + str(n + 1)
            e['concept_id'] = 'CONCEPT-' + e['id']
            e['attributes']['scale_site'] = 'SYN-SITE-' + str(n % 6 + 1)
            e['attributes']['scale_origin_id'] = pool[n % len(pool)]['id']
            large.append(e)
    return {'T0': small, 'T1': original, 'T2': large}, volume


def activities(sites, seed):
    """Literal independently specified output fixture, not a balance-solving generator."""
    rng = random.Random(seed)
    inputs, outputs = [], []
    for site in range(1, sites + 1):
        # Unequal site populations preserve a simple long tail.
        for batch in range(max(1, 12 // site)):
            m = rng.choice([1, 2, 3])
            identity = f'SYN-{site}-{batch}'
            a = {'id': identity, 'site': f'SYN-SITE-{site}', 'feed_t': 100*m,
                 'feed_assay': 0.30, 'product_assay': 0.54, 'tail_assay': 0.06,
                 'power_kw': 10*m, 'hours': 8, 'heat_input_kwh': 200*m,
                 'measured_loss_kwh': 40*m, 'shipped_t': 50*m,
                 'price_cny_per_t': 200, 'tax_rate': 0.13,
                 'opening_product_t': 20*m, 'gypsum_weighed_t': 80*m,
                 'opening_gypsum_t': 10*m, 'gypsum_dispatched_t': 60*m}
            o = {'id': identity, 'site': a['site'], 'product_t': 50*m, 'tail_t': 50*m,
                 'product_p2o5_t': 27*m, 'tail_p2o5_t': 3*m, 'electric_kwh': 80*m,
                 'useful_kwh': 240*m, 'invoice_cny': 11300*m, 'closing_product_t': 20*m,
                 'gypsum_produced_t': 80*m, 'closing_gypsum_t': 30*m}
            inputs.append(a)
            outputs.append(o)
    return inputs, outputs


def inventory_model(entities, relationships, model_path=None):
    old = json.loads(Path(model_path or CASE / 'projection/model.json').read_text())
    model = {k: copy.deepcopy(old[k]) for k in ('schema_version', 'project', 'sources')}
    model['extensions'] = {'entity_types': {
        'guide:architecture_domain': '指南中的架构域类别，不是企业组织或部署容器',
        'guide:metamodel_entity': '来源内容元模型的实体类型，不是项目实体实例'},
        'relationship_types': {}}
    if any(e.get('attributes', {}).get('scale_inventory_origin') ==
           'current-registry-synthetic-supplement' for e in entities):
        model['sources'].append({'id': 'SCALE-CURRENT-REGISTRY', 'kind': 'example',
            'description': '当前注册示例的合成压力补充，不是历史千林事实或专业证据。',
            'locator': 'contracts/capabilities.json'})
    model.update(entities=copy.deepcopy(entities), relationships=relationships,
                 views=[], deliverables=[], gaps=[])
    return model


def focus_model(model):
    """Two authored application versions; explicitly separate from random inventory."""
    result = copy.deepcopy(model)
    selected = [e for e in result['entities'] if e['type'] == 'application'][:2]
    for i, e in enumerate(selected):
        e['concept_id'] = 'SYN-LEDGER'
        e['version'] = str(i + 1)
        e['evolution'] = ['baseline', 'target'][i]
        e['context']['evolution'] = e['evolution']
        e['name'] = ['合成库存台账基线', '合成库存台账候选'][i]
        e['attributes'] = {'owner': '虚构库存负责人', 'lifecycle': 'candidate',
                           'criticality': '仅合成算例', 'cost': 100 + 20*i,
                           'boundary': '合成库存记账', 'responsibility': '记录合成物料数量',
                           'version': str(i + 1)}
    result['entities'] = selected
    result['relationships'] = []
    result['views'] = [{'id': 'scale-inventory-concern', 'artifact_id': 'application-portfolio-catalog',
                        'profile_id': 'compat-application-portfolio-catalog',
                        'title': '关注点：合成库存台账成本变化（非经营证据）',
                        'context': result['project']['context'],
                        'entity_ids': [e['id'] for e in selected], 'relationship_ids': [],
                        'allow_mixed_evolution': True,
                        'analysis': '仅检验两个手写版本的可追溯差异；不批准方案、不展示全库。',
                        'legend': '虚构项目约定；非官方来源图。'}]
    return result


def check_repeat(current, previous):
    comparisons = {}
    for tier in ('T0', 'T1', 'T2'):
        for filename in ('inventory.json', 'activities.json', 'outputs.json'):
            relative = Path(tier) / filename
            hashes = [hashlib.sha256((Path(p) / relative).read_bytes()).hexdigest()
                      for p in (current, previous)]
            comparisons[str(relative)] = {'current': hashes[0], 'previous': hashes[1],
                                          'equal': hashes[0] == hashes[1]}
    return {'previous_run': str(Path(previous).resolve()), 'files': comparisons,
            'equal': all(row['equal'] for row in comparisons.values()),
            'excluded': 'Timestamps, runtime manifests and timings are intentionally not deterministic.'}


def preflight(dataset_dir):
    dataset_dir = Path(dataset_dir)
    problems = []
    model_path = dataset_dir.parent / 'projection/model.json'
    try:
        template = json.loads(model_path.read_text())
        if (not isinstance(template, dict) or not all(k in template for k in ('schema_version', 'project', 'sources'))
                or not isinstance(template['project'], dict) or not isinstance(template['sources'], list)):
            raise ValueError('projection template requires schema_version, project and sources')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        problems.append('projection-template-unavailable: ' + str(exc))
    files = sorted((dataset_dir / 'context').glob('*.json'))
    if not files:
        problems.append('missing-context-inventory')
    entities = []
    for path in files:
        try:
            values = json.loads(path.read_text())['entities']
            if not isinstance(values, list): raise ValueError('entities must be a list')
            entities.extend(values)
        except (OSError, ValueError, KeyError, TypeError) as exc:
            problems.append(str(path)+': '+str(exc))
    if files and not entities: problems.append('empty-context-inventory')
    if entities and any(not isinstance(e, dict) or not all(k in e for k in ('id','type','context','attributes')) for e in entities):
        problems.append('malformed-context-entity')
    relation_path = dataset_dir / 'relationships.json'
    try:
        relations = json.loads(relation_path.read_text())
        relations = relations['relationships'] if isinstance(relations, dict) else relations
        if not isinstance(relations, list): raise ValueError('relationships must be a list')
        ids = {e.get('id') for e in entities if isinstance(e, dict)}
        if any(not isinstance(r, dict) or not all(k in r for k in ('id','source','target')) or r['source'] not in ids or r['target'] not in ids for r in relations):
            problems.append('malformed-or-dangling-relationship')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        problems.append('relationships-unavailable: '+str(exc))
    return problems


def run(out, seed, repeat_of=None, dataset_dir=None):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=False)
    dataset_dir = Path(dataset_dir or CASE / 'dataset').resolve()
    missing = preflight(dataset_dir)
    if missing:
        report = {'schema_version': 'scale-verification/2', 'status': 'blocked', 'checks_passed': False,
                  'dataset_dir': str(dataset_dir), 'missing_requirements': missing, 'tiers': {},
                  'limit': 'Requires explicit architecture inventories and relationships; an SQL order-volume fixture does not substitute for T0/T1/T2.'}
        write_json(out / 'report.json', report)
        return report
    from validate import validate
    from analyze import impact, compare
    from generate import generate
    tiers, volume = build_inventories(dataset_dir)
    write_json(out / 'volume-model.json', volume)
    write_json(out / 'current-type-supplements.json', [e for e in tiers['T1']
        if e.get('attributes', {}).get('scale_inventory_origin') == 'current-registry-synthetic-supplement'])
    # Copy source data byte-for-byte; old reports and historical outputs remain untouched.
    shutil.copytree(dataset_dir, out / 'raw-historical-T1')
    for name in ('capabilities.json', 'deliverables.json', 'capability-addenda/deliverable-assembly-rules.json',
                 'metamodel.json', 'artifacts.json', 'schemas/model.schema.json',
                 'scripts/build_data_volume_model.py', 'scripts/verify_scale_cases.py', 'scripts/scale_oracle.py'):
        target = out / 'contracts' / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / name, target)
    rel_data = json.loads((dataset_dir / 'relationships.json').read_text())
    original_rels = rel_data['relationships'] if isinstance(rel_data, dict) else rel_data
    report = {'seed': seed, 'professional_contract_acceptance': False,
              'production_benchmark': False, 'tiers': {},
              'limits': ['Random inventory attributes are not professional evidence.',
                         'T1 retains historical inventory plus separately marked current-type example supplements.',
                         'T2 repeats historical or explicitly supplemental example entities; counts reflect current contracts.',
                         'Arithmetic fixture is not a phosphorus plant process simulation.',
                         'Generation is bounded to two authored applications, not the full inventory.',
                         'Full-inventory compare is baseline-only candidate enumeration; focus compare has two authored versions.',
                         'Historical T1 orders/events are archived, not certified by the new oracle.',
                         'Timing is one local execution, not production load testing.']}
    for tier, entities in tiers.items():
        start = time.perf_counter()
        directory = out / tier
        write_json(directory / 'inventory.json', entities)
        ids = {e['id'] for e in entities}
        if tier == 'T2':
            # Repeat only explicit historical edges within the same replica index.
            origins = defaultdict(list)
            for e in entities:
                origins[e['attributes']['scale_origin_id']].append(e['id'])
            rels = []
            for r in original_rels:
                for i, (source, target) in enumerate(zip(origins[r['source']], origins[r['target']])):
                    edge = copy.deepcopy(r)
                    edge.update(id=f'SCALE-{r["id"]}-{i}', source=source, target=target)
                    rels.append(edge)
        else:
            rels = [r for r in original_rels if r['source'] in ids and r['target'] in ids]
        model = inventory_model(entities, rels, dataset_dir.parent / 'projection/model.json')
        write_json(directory / 'model.json', model)
        times = {}
        for operation, fn in [('validate', lambda: validate(model)),
                              ('impact', lambda: impact(model, [rels[0]['source'] if rels else entities[0]['id']], 2)),
                              ('compare', lambda: compare(model))]:
            tick = time.perf_counter()
            value = fn()
            write_json(directory / (operation + '.json'), value)
            times[operation] = time.perf_counter() - tick
        issues = json.loads((directory / 'validate.json').read_text())
        focus = focus_model(model)
        write_json(directory / 'focus-model.json', focus)
        write_json(directory / 'focus-compare.json', compare(focus))
        tick = time.perf_counter()
        generate(focus, directory / 'concern', view_ids=['scale-inventory-concern'])
        times['concern_generate'] = time.perf_counter() - tick
        site_count = {'T0': 1, 'T1': 3, 'T2': 6}[tier]
        inputs, outputs = activities(site_count, seed)
        write_json(directory / 'activities.json', inputs)
        write_json(directory / 'outputs.json', outputs)
        oracle = audit(directory)
        write_json(directory / 'oracle.json', oracle)
        negatives = {}
        for category, field in MUTATIONS.items():
            negative = directory / 'mutations' / category
            changed = copy.deepcopy(outputs)
            changed[0][field] += 1
            write_json(negative / 'activities.json', inputs)
            write_json(negative / 'outputs.json', changed)
            observed = audit(negative)
            write_json(negative / 'oracle.json', observed)
            negatives[category] = not observed['passed'] and category in {v['category'] for v in observed['violations']}
        repeated = activities(site_count, seed)
        report['tiers'][tier] = {'entities': len(entities), 'types': len({e['type'] for e in entities}),
                                'relationships': len(rels), 'activities': len(inputs), 'sites': site_count,
                                'type_counts': dict(Counter(e['type'] for e in entities)),
                                'oracle_passed': oracle['passed'], 'mutations_rejected': negatives,
                                'validation_errors': sum(i['level'] == 'error' for i in issues),
                                'validation_warnings': sum(i['level'] == 'warning' for i in issues),
                                'repeat_seed_equal': digest(repeated) == digest((inputs, outputs)),
                                'seconds': times, 'total_seconds': time.perf_counter() - start}
    report['exact_T0_subset'] = all(e in tiers['T1'] for e in tiers['T0'])
    report['checks_passed'] = report['exact_T0_subset'] and all(
        r['oracle_passed'] and r['repeat_seed_equal'] and r['validation_errors'] == 0 and all(r['mutations_rejected'].values())
        for r in report['tiers'].values())
    if repeat_of is not None:
        report['persisted_repeat'] = check_repeat(out, repeat_of)
        report['checks_passed'] = report['checks_passed'] and report['persisted_repeat']['equal']
    report['source_sha256'] = {str(p.relative_to(out)): hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in sorted((out / 'contracts').rglob('*')) if p.is_file()}
    write_json(out / 'report.json', report)
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=ROOT.parents[1] / 'output/scale-runs' / datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'))
    parser.add_argument('--dataset-dir', type=Path, help='External dataset folder containing context/*.json and relationships.json')
    parser.add_argument('--seed', type=int, default=20261104)
    parser.add_argument('--repeat-of', type=Path, help='Compare nine deterministic persisted inputs/outputs with a prior run')
    args = parser.parse_args()
    result = run(args.out, args.seed, args.repeat_of, args.dataset_dir)
    print(json.dumps({'status': result.get('status', 'passed' if result['checks_passed'] else 'failed'), 'out': str(args.out), 'checks_passed': result['checks_passed'],
                      'tiers': {k: {f: v[f] for f in ('entities', 'activities', 'validation_errors', 'total_seconds')}
                                for k, v in result['tiers'].items()}}, ensure_ascii=False))
    raise SystemExit(3 if result.get('status') == 'blocked' else 0 if result['checks_passed'] else 1)
