"""Source-specific invariants for qualitative factor layers and application change.

These checks prove the model can express the concern; they do not approve an
enterprise's readiness, a proposed change, or a standards-equivalence claim.
"""

LAYERS = ('foundational', 'impact', 'sustaining')


def category_of(entity):
    value = entity.get('attributes', {}).get('factor_category')
    return value if isinstance(value, str) else None


def check_source_shape(es, rs, profile):
    mode = profile.get('template', {}).get('semantic_layout')
    errors = []
    byid = {e['id']: e for e in es}

    def need(ok, code, identity, message):
        if not ok:
            errors.append({'code': code, 'id': identity, 'message': message})

    if mode == 'dtra-factor-layers':
        factors = [e for e in es if e['type'] == 'readiness_factor']
        categories = {category_of(e) for e in factors}
        need(categories == set(LAYERS), 'dtra-factor-layers-incomplete', profile['id'],
             '完整因素递进视图须分别表达基础、影响、持续三层；不得从日期或顺序推断。')
        cases = [e for e in es if e['type'] == 'assessment_result']
        for case in cases:
            attrs = case.get('attributes', {})
            category = attrs.get('organization_type')
            valid = type(category) is int and category in (1, 2, 3)
            need(valid, 'dtra-organization-type-invalid', case['id'], '类型必须为 1、2、3；不表示步骤或分数。')
            if valid:
                need(attrs.get('fulfilled_layers') == list(LAYERS[:category]),
                     'dtra-prerequisite-layers', case['id'], '类型 2/3 必须同时满足内侧因素层。')
                targets = {category_of(byid[r['target']])
                           for r in rs if r['source'] == case['id'] and r['target'] in byid
                           and byid[r['target']]['type'] == 'readiness_factor'
                           and r['type'] == 'traces_to'}
                need(targets == set(LAYERS[:category]), 'dtra-layer-trace-gap', case['id'],
                     '就绪类型声明须显式追溯其满足的因素层。')
        need({e.get('attributes', {}).get('organization_type') for e in cases
              if type(e.get('attributes', {}).get('organization_type')) is int} == {1, 2, 3},
             'dtra-types-incomplete', profile['id'], '完整参考视图需要三种就绪情形，不能冒充同一企业的三个实施步骤。')
        for e in es:
            need(not any(k in e.get('attributes', {}) for k in ('start', 'end', 'start_date', 'end_date')),
                 'dtra-schedule-confusion', e['id'], '因素递进图不承载排期；实施日期应置于独立工作包路线图。')
    elif mode == 'application-change-topology':
        for e in es:
            parent = e.get('attributes', {}).get('parent_id')
            if parent:
                if not isinstance(parent, str):
                    need(False, 'change-parent-invalid', e['id'], '归属必须为单个对象ID；多个维度需分别建关系。')
                    continue
                need(parent in byid, 'change-parent-missing', e['id'], '变化归属须在当前视图中。')
                seen = {e['id']}
                while isinstance(parent, str) and parent in byid:
                    if parent in seen:
                        need(False, 'change-parent-cycle', e['id'], '变化归属不允许循环。')
                        break
                    seen.add(parent)
                    parent = byid[parent].get('attributes', {}).get('parent_id')
        applications = [e for e in es if e['type'] == 'application']
        for e in applications:
            change = e.get('attributes', {}).get('change_kind')
            need(change in ('create', 'consolidate', 'retire', 'optimize', 'retain'),
                 'application-change-kind', e['id'], '明确新增、整合、退役、优化或保留；日期不是变化类型。')
            if change == 'retire':
                need(any(c['type'] == 'event' and c.get('attributes', {}).get('parent_id') == e['id']
                         and c.get('attributes', {}).get('event_kind') == 'retirement' for c in es),
                     'retirement-event-missing', e['id'], '退役以事件表达，不能以差距对象替代事件。')
        for gap in [e for e in es if e['type'] == 'gap']:
            need(bool(gap.get('attributes', {}).get('parent_id')) or
                 any(r['source'] == gap['id'] or r['target'] == gap['id'] for r in rs),
                 'unbound-application-gap', gap['id'], '差距须绑定受影响的应用、能力或交付物。')
        need(bool(applications) and any(e['type'] == 'gap' for e in es),
             'application-change-content-missing', profile['id'], '应用变化图需要应用及明确差距。')
    return errors
