"""Loss-aware, typed matrix projection shared by SVG and field tables."""
from collections import defaultdict
from functools import lru_cache


@lru_cache(maxsize=None)
def artifact_matrix(artifact_id):
    if not artifact_id:
        return {}
    from registry import load
    return load()[0].get(artifact_id, {}).get('matrix', {})


def matrix_options(profile):
    return {**artifact_matrix(profile.get('artifact_id')), **profile.get('template', {})}


def project_matrix(entities, relationships, options):
    byid = {e['id']: e for e in entities}
    rowtypes = options.get('row_types', [])
    coltypes = options.get('column_types', [])
    rows = [e for e in entities if e['type'] in rowtypes] if rowtypes else [byid[i] for i in dict.fromkeys(r['source'] for r in relationships) if i in byid]
    cols = [e for e in entities if e['type'] in coltypes] if coltypes else [byid[i] for i in dict.fromkeys(r['target'] for r in relationships) if i in byid]
    rowids = {e['id'] for e in rows};colids = {e['id'] for e in cols}
    cells = defaultdict(list)
    outside = []
    for r in relationships:
        if r['source'] in rowids and r['target'] in colids:
            cells[(r['source'], r['target'])].append((r, '行→列'))
        elif r['target'] in rowids and r['source'] in colids:
            cells[(r['target'], r['source'])].append((r, '列→行'))
        else:
            outside.append(r['id'])
    return rows, cols, cells, outside


def cell_label(relation, direction):
    if relation.get('type') == 'supports_role':
        attrs = relation.get('attributes') or {}
        kinds = {'source_reference_target': '原文参考目标', 'tailored_target': '项目目标',
                 'observed_assessment': '人员观察'}
        value = attrs.get('proficiency')
        state = attrs.get('assessment_state', '语义待补')
        shown = '待补/未评级' if value is None else str(value)
        return (direction + ' · ' + kinds.get(attrs.get('assessment_kind'), '评级语义待补')
                + ' ' + shown + ' · ' + state + ' · ' + attrs.get('scale_id', '量表待补')
                + ' [' + relation['type'] + ']')
    return direction + ' · ' + (', '.join(relation.get('codes', [])) or relation.get('label', relation['type'])) + ' [' + relation['type'] + ']'
