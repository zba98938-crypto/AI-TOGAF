"""Shared observation parsing; no implicit score, scale, aggregation or truth claim."""
PALETTE = ['#e2edf8', '#e7f1e9', '#fff0d8', '#efe7f7', '#e3f1f2', '#f8e6e6']


def parse_evaluation(item, template=None, scales=None):
    template = template or {}
    scales = scales or {}
    attrs = item.get('attributes', {})
    dimension = attrs.get('dimension', template.get('dimension'))
    candidates = [m for m in item.get('measurements', []) if not dimension or m.get('dimension') == dimension]
    errors = []
    warnings = []
    field = template.get('score_field', 'score')
    direct = field in attrs or 'rating' in attrs
    if len(candidates) > 1 and not direct:
        errors.append({'code': 'ambiguous-heatmap-observation', 'id': item['id'],
                       'message': '多个评价需按维度或视图切片，不能默认取第一项。'})
    measurement = candidates[0] if len(candidates) == 1 and not direct else {}
    value = attrs.get(field, attrs.get('rating', measurement.get('value')))
    dimension = attrs.get('dimension', measurement.get('dimension', template.get('dimension')))
    existence = attrs.get('existence', measurement.get('existence'))
    status = attrs.get('status', measurement.get('status'))
    status = 'future-absent' if existence == 'future-absent' else 'unknown' if status in {'unknown', 'unmeasured'} or (value is None and (direct or measurement)) else 'measured' if value is not None else 'missing'
    scale_id = attrs.get('scale_id', measurement.get('scale_id'))
    scale = attrs.get('scale', measurement.get('scale', scales.get(scale_id, template.get('scale'))))
    colors = {}
    values = []
    if isinstance(scale, dict):
        anchors = scale.get('anchors', [])
        values = scale.get('values', [a['value'] for a in anchors if 'value' in a])
        colors.update({str(a['value']): a['color'] for a in anchors if 'value' in a and 'color' in a})
        colors.update(scale.get('colors', {}))
    elif isinstance(scale, list):
        values = scale
    colors.update(template.get('colors', {}))
    colors.update(attrs.get('colors', {}) if isinstance(attrs.get('colors'), dict) else {})
    colors = {str(k): v for k, v in colors.items()}
    if values and not colors:
        colors = {str(v): PALETTE[i % len(PALETTE)] for i, v in enumerate(values)}
    scale_present = bool(scale) or bool(colors)
    if status not in {'future-absent', 'missing'}:
        if not dimension or not scale_present:
            errors.append({'code': 'missing-heatmap-scale', 'id': item['id'],
                           'message': '评价需要明确维度和量表；未知值不会默认记分。'})
        if status == 'measured' and (values or colors) and str(value) not in {str(v) for v in values} | set(colors):
            errors.append({'code': 'heatmap-value-outside-scale', 'id': item['id'], 'value': value})
    if status == 'measured' and not colors:
        warnings.append('热力量表无明确颜色规则；保留原值并用中性色，不推断高低：' + str(dimension))
    fill = '#d8c6ed' if status == 'future-absent' else '#edf0f3' if status in {'unknown', 'missing'} else colors.get(str(value), '#edf0f3')
    label = '未来不存在（不是零分或退役）' if status == 'future-absent' else '未知（不记分）' if status == 'unknown' else '未记录评价' if status == 'missing' else str(dimension or '维度未记录') + ' = ' + str(value)
    return {'observed': status != 'missing', 'status': status, 'value': value,
            'dimension': dimension, 'scale': scale, 'scale_id': scale_id, 'colors': colors,
            'fill': fill, 'label': label, 'errors': errors, 'warnings': warnings,
            'measurement': measurement}


def is_evaluation_field_satisfied(item, field, template=None, scales=None):
    """Measurement/future absence are alternatives to legacy score fields, not defaults."""
    if field not in {'score', 'rating', 'dimension', 'scale'}:
        return False
    parsed = parse_evaluation(item, template, scales)
    return parsed['observed'] and not parsed['errors']


def stage_capability_errors(entities, relationships):
    stages = {e['id']: e for e in entities if e['type'] in {'value_stage', 'value_stream_stage', 'stage', 'customer_journey_stage'}}
    caps = {e['id'] for e in entities if e['type'] == 'capability'}
    orders = {identity: e.get('attributes', {}).get('order', e.get('attributes', {}).get('ordinal')) for identity, e in stages.items()}
    errors = []
    for identity, order in orders.items():
        if order is not None and type(order) not in {int, float}:
            errors.append({'code': 'invalid-stage-order', 'id': identity})
    for r in relationships:
        if r['type'] == 'enabled_by' and (r['source'] not in stages or r['target'] not in caps):
            errors.append({'code': 'invalid-stage-enablement-direction', 'id': r['id'],
                           'message': '阶段×能力热力使能必须显式连接阶段→能力；实例映射应另列关注点视图。'})
        if r['type'] == 'precedes' and r['source'] in stages and r['target'] in stages:
            a, b = orders[r['source']], orders[r['target']]
            if type(a) in {int, float} and type(b) in {int, float} and a >= b:
                errors.append({'code': 'stage-order-conflicts-with-precedence', 'id': r['id']})
    return errors
