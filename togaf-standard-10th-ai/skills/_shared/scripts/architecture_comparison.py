"""Compare architecture versions without inventing lifecycle or measurement facts.

This is the project operational implementation of baseline/target comparison,
not an official TOGAF gap classification or an approval decision.
"""
import json


def _canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))


def compare_architectures(model, baseline_state=None, target_state=None, scope_id=None):
    entities = {e['id']: e for e in model['entities']}
    states = {s['id']: s for s in model.get('states', [])}
    default_evolution = model['project']['context']['evolution']

    def evolution(entity):
        return states.get(entity.get('state_id'), {}).get(
            'evolution', entity.get('evolution', entity.get('context', {}).get('evolution', default_evolution)))

    def state(entity):
        return entity.get('state_id', evolution(entity))

    def scope(entity):
        return entity.get('scope_id', states.get(entity.get('state_id'), {}).get('scope_id'))

    known_states = set(states) | {state(e) for e in entities.values()}
    for selector in (baseline_state, target_state):
        if selector is not None and selector not in known_states:
            raise ValueError('未知比较状态：' + selector + '；不能将状态拼写错误解释为架构增删。')
    if baseline_state is not None and baseline_state == target_state:
        raise ValueError('比较两端必须选择不同状态。')
    known_scopes = {s['id'] for s in model.get('scopes', [])} | {scope(e) for e in entities.values()}
    if scope_id is not None and scope_id not in known_scopes:
        raise ValueError('未知比较范围：' + scope_id)

    def endpoint(identity):
        entity = entities[identity]
        # A reused concept in another segment or domain is not the same endpoint.
        return {'concept_id': entity.get('concept_id', identity),
                'scope_id': scope(entity), 'type': entity['type']}

    def edges(entity):
        result = {}
        for edge in model['relationships']:
            if entity['id'] not in (edge['source'], edge['target']):
                continue
            # Version links describe the comparison itself, not a changed dependency.
            if edge['type'] == 'transitions_to':
                continue
            if edge.get('state_id') and edge['state_id'] != state(entity):
                continue
            payload = {'source': endpoint(edge['source']), 'type': edge['type'],
                       'target': endpoint(edge['target']), 'codes': sorted(edge.get('codes', [])),
                       'label': edge['label'], 'attributes': edge.get('attributes', {}),
                       'cardinality': edge.get('cardinality', {}), 'scope_id': edge.get('scope_id')}
            result.setdefault(_canonical(payload), []).append(edge)
        return result

    def legacy_edge(key):
        payload = json.loads(key)
        # Preserve the established tuple projection for callers. The structured
        # relationship_changes records retain the full scope/type identity.
        return [payload['source']['concept_id'], payload['type'], payload['target']['concept_id'],
                payload['codes'], _canonical({k: payload[k] for k in ('label', 'attributes', 'cardinality')})]

    def edge_details(keys, mapping):
        return [{'relationship_ids': sorted(edge['id'] for edge in mapping[key]),
                 'semantic_content': json.loads(key),
                 'evidence': sorted({sid for edge in mapping[key] for sid in edge.get('evidence', [])})}
                for key in sorted(keys)]

    groups = {}
    unaligned = []
    for entity in model['entities']:
        if scope_id is not None and scope(entity) != scope_id:
            continue
        if not entity.get('concept_id'):
            unaligned.append(entity['id'])
            continue
        groups.setdefault((entity['concept_id'], scope(entity)), []).append(entity)

    changes = []
    for (concept_id, entity_scope), versions in sorted(groups.items(), key=lambda item: str(item[0])):
        before = [e for e in versions if (state(e) == baseline_state if baseline_state else evolution(e) == 'baseline')]
        after = [e for e in versions if (state(e) == target_state if target_state else evolution(e) == 'target')]
        record = {'concept_id': concept_id, 'scope_id': entity_scope,
                  'versions': [{'id': e['id'], 'state_id': state(e), 'evolution': evolution(e),
                                'version': e.get('version')} for e in versions],
                  'transition_versions': [e['id'] for e in versions if evolution(e) == 'transition']}
        if len(before) > 1 or len(after) > 1:
            record.update(kind='ambiguous-comparison', notice='比较端存在多个版本；选择具体命名状态或核对概念标识，不任意选取。')
        elif not before or not after:
            record.update(kind='addition-candidate' if after else 'removal-candidate' if before else 'transition-only',
                          notice='缺少对应记录仅是候选差距；先核对范围完整性、生命周期与采集缺口。')
        else:
            before, after = before[0], after[0]
            record.update(baseline_id=before['id'], target_id=after['id'])
            if before['type'] != after['type']:
                record.update(kind='incompatible-comparison', baseline_type=before['type'], target_type=after['type'],
                              notice='同一 concept_id 在两端的对象类型不同；先确认身份或替换关系，不按同一对象直接比较。')
                changes.append(record)
                continue
            attributes = {}
            for field in sorted(set(before['attributes']) | set(after['attributes'])):
                b_present, t_present = field in before['attributes'], field in after['attributes']
                b_value, t_value = before['attributes'].get(field), after['attributes'].get(field)
                if b_present != t_present or _canonical(b_value) != _canonical(t_value):
                    attributes[field] = {'baseline': b_value, 'target': t_value}
                    if b_present != t_present:
                        attributes[field].update(baseline_present=b_present, target_present=t_present)
            b_edges, t_edges = edges(before), edges(after)
            added, removed = set(t_edges) - set(b_edges), set(b_edges) - set(t_edges)
            # Measurements carry scales, units, periods and methods. Do not subtract
            # unlike observations or manufacture a numeric quality improvement.
            b_measurements, t_measurements = before.get('measurements', []), after.get('measurements', [])
            measurement_change = sorted(map(_canonical, b_measurements)) != sorted(map(_canonical, t_measurements))
            record.update(name_change=before['name'] != after['name'], attributes=attributes,
                          measurements_changed=measurement_change,
                          relations_added=[legacy_edge(key) for key in sorted(added)],
                          relations_removed=[legacy_edge(key) for key in sorted(removed)],
                          relationship_changes={'added': edge_details(added, t_edges),
                                                'removed': edge_details(removed, b_edges)})
            if measurement_change:
                record['measurements'] = {'baseline': b_measurements, 'target': t_measurements,
                                          'notice': '观察记录发生变化；量表、单位、方法、期间及质量优劣需另行评审，不自动换算或打分。'}
            record['kind'] = 'changed' if attributes or record['name_change'] or added or removed or measurement_change else 'unchanged'
            record['evidence'] = {'baseline': before.get('evidence', []), 'target': after.get('evidence', [])}
        changes.append(record)
    return {'notice': '按概念、范围与具体状态比较模型事实；差距候选需核对完整性和来源，再映射需求、工作包与过渡检查。',
            'selection': {'baseline_state': baseline_state, 'target_state': target_state, 'scope_id': scope_id},
            'unaligned_entity_ids': sorted(unaligned), 'changes': changes}
