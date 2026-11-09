"""Concern-specific source structures, separate from calendar roadmaps."""
import math

from source_shape_semantics import LAYERS, check_source_shape


def factor_layers(d, es, rs):
    from profile_render import esc
    d.errors.extend(check_source_shape(es, rs, d.profile))
    x, y = 180, 660
    radii = (170, 320, 470)
    colors = ('#72c796', '#56c7e5', '#f4b564')
    names = ('基础 / Foundational', '影响 / Impact', '持续 / Sustaining')
    d.text(30, 110, '定性因素层级：三类企业是评估情形，层级与射线均无数值刻度。', 17)
    for i in (2, 1, 0):
        radius = radii[i]
        d.parts.append(f'<path data-factor-layer="{LAYERS[i]}" d="M{x},{y} L{x},{y-radius} A{radius},{radius} 0 0 1 {x+radius},{y} Z" fill="{colors[i]}" stroke="white"/>')
        d.text(x-10, y-radius+25, names[i], 14, anchor='end')
    d.line(x, y, x, y-500, arrow=True)
    d.line(x, y, x+510, y, arrow=True)
    d.text(x, y+35, '普及度与采用速度 / Ubiquity & Velocity →', 15)
    d.text(30, 150, 'DTRA 因素层级 ↑', 15)
    # The direction indicates increasing conduciveness only; it is not a score.
    d.line(x, y, x+350, y-350, dashed=True, color='#607986')
    d.text(x+240, y-365, '就绪度有利程度递增 ↗', 14)
    for case in [e for e in es if e['type'] == 'assessment_result']:
        category = case.get('attributes', {}).get('organization_type')
        if type(category) is not int or category not in (1, 2, 3):
            continue
        angle = (.18, .40, .66)[category-1]
        radius = radii[category-1]-15
        px, py = x+math.cos(angle)*radius, y-math.sin(angle)*radius
        d.parts.append(f'<g data-entity-id="{esc(case["id"])}">')
        d.line(x, y, round(px, 2), round(py, 2), color='#203d49')
        # Read each caption beyond its ray endpoint, clear of the diagonal
        # trend indicator; angles and lengths remain qualitative layout only.
        label_x, anchor = px+10, 'start'
        d.text(label_x, py-12, f'类型 {category} / Type {category}', 14, anchor=anchor)
        d.parts.append('</g>')
    # Details remain visible and mutable. The three cases are an explanatory
    # source model; a project's classification needs its own assessment evidence.
    d.text(730, 150, '因素层与行动证据', 19)
    yy = 180
    factors = sorted([e for e in es if e['type'] == 'readiness_factor'],
                     key=lambda e: LAYERS.index(e.get('attributes', {}).get('factor_category'))
                     if e.get('attributes', {}).get('factor_category') in LAYERS else 99)
    for e in factors:
        category = e.get('attributes', {}).get('factor_category')
        color = colors[LAYERS.index(category)] if category in LAYERS else '#eee'
        yy += d.card(e, 730, yy, 510, fill=color)+20
    bottom = max(yy+30, 760)
    for i, e in enumerate([e for e in es if e not in factors]):
        d.card(e, 30+i*420, bottom, 400)
    d.text(30, d.height+25, '关系追溯（表内箭头为类型→满足的因素层；射线角度与长度仅用于排版）', 15)
    for r in rs:
        # Trace membership is encoded in the table, not as a chronological edge.
        d.parts.append(f'<g data-relationship-id="{esc(r["id"])}">')
        d.text(30, d.height+12, f'{r["source"]} → {r["target"]}：{r.get("label", r["type"])} [{r["type"]}]', 13, units=150)
        d.parts.append('</g>')
        d.relation_ids.add(r['id'])


def application_changes(d, es, rs):
    from profile_render import esc
    findings = check_source_shape(es, rs, d.profile)
    d.errors.extend(findings)
    if any(e['code'] == 'change-parent-cycle' for e in findings):
        return
    byid = {e['id']: e for e in es}
    children = {e['id']: [] for e in es}
    roots = []
    for e in es:
        parent = e.get('attributes', {}).get('parent_id')
        if isinstance(parent, str) and parent in byid:
            children[parent].append(e)
        else:
            roots.append(e)
    colors = {'capability': '#f4e2b4', 'application': '#b9edf0', 'data_entity': '#fff5bd',
              'gap': '#daf5d5', 'event': '#f9dadd', 'deliverable_component': '#d2e6bd',
              'work_package': '#e3dcf2'}

    def height(e, width):
        return d.card_height(e, width)+sum(height(c, width-40)+25 for c in children[e['id']])+30

    def draw(e, x, y, width):
        h = height(e, width)
        d.card(e, x, y, width, h, fill=colors.get(e['type'], '#edf2f5'))
        if e['type'] == 'gap':
            d.parts.append(f'<path data-gap-notation="{esc(e["id"])}" d="M{x},{y+h-12} Q{x+width/4},{y+h+6} {x+width/2},{y+h-12} T{x+width},{y+h-12}" fill="none" stroke="#527c56" stroke-width="2"/>')
        elif e['type'] == 'event':
            d.text(x+width-12, y+h-8, '事件 / Event', 11, anchor='end')
        elif e['type'] == 'deliverable_component':
            d.parts.append(f'<path d="M{x+12},{y+h} L{x},{y+h+10} L{x+width},{y+h+10} L{x+width-12},{y+h}" fill="#b2cc9b" stroke="#8298aa"/>')
        cy = y+d.card_height(e, width)+15
        for c in children[e['id']]:
            draw(c, x+20, cy, width-40)
            cy += height(c, width-40)+25

    d.text(30, 110, '嵌套表示明确归属；差距、退役事件与交付物分开建模。依赖箭头指向前置工作。', 16)
    colheight = [150]*3
    for e in roots:
        col = min(range(3), key=lambda i: colheight[i])
        draw(e, 30+col*610, colheight[col], 560)
        colheight[col] += height(e, 560)+70
    d.network_routing = True
    for r in rs:
        d.edge(r, byid)


RENDERERS = {'dtra-factor-layers': factor_layers,
             'application-change-topology': application_changes}
