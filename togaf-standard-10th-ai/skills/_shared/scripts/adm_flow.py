#!/usr/bin/env python3
"""Derive complete, editable ADM flow views from current contracts and records.

The overview is a reading order, not an enforced waterfall. Registry candidates,
actual cycle evidence and professional acceptance remain distinct.
"""
import base64
import hashlib
import html
import json
from pathlib import Path
import re
import subprocess

from adm import ROOT, check_cycle, load, schema_issues
from architecture_delivery import catalog
from registry import load as registry

NOTICE = '项目解释图；实线为常见信息流，虚线为需求反馈与迭代；阶段可并行、复用和裁剪。'
TITLES = {'Preliminary': '预备阶段 · 架构能力', 'A': 'A · 架构愿景',
          'B': 'B · 业务架构', 'C': 'C · 信息系统架构（数据＋应用）',
          'D': 'D · 技术架构', 'E': 'E · 机会与解决方案', 'F': 'F · 迁移规划',
          'G': 'G · 实施治理', 'H': 'H · 架构变更管理',
          'Requirements': '持续需求管理（不是 Phase I）'}
PURPOSE = {'Preliminary': '谁授权，怎样建立与治理架构实践？', 'A': '范围、价值和架构工作是否可接受？',
           'B': '业务能力、价值交付和业务过程怎样改变？', 'C': '数据与应用怎样协调支撑业务？',
           'D': '技术服务、平台及运营约束怎样落实？', 'E': '怎样整合差距、工作包与过渡架构？',
           'F': '怎样排序投资、资源、依赖与迁移？', 'G': '实际实施是否符合，偏离怎样处置？',
           'H': '效果和变化要求维护、重开或新周期吗？'}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def dump(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def source_refs(binding):
    return [{k: r[k] for k in ('document_id', 'section_id', 'anchor', 'title_en', 'path') if k in r}
            for r in (binding or {}).get('refs', [])]


def build_mapping(cycle=None, model=None, evidence_root=None):
    """Keep all registry candidates and their provenance; never call them outputs."""
    if (cycle is None) != (model is None):
        raise ValueError('--cycle 与 --model 必须同时提供')
    definition = load(ROOT / 'references/adm-phases.json')
    arts, dels, profiles, _ = registry()
    routes = catalog([*TITLES, 'Review'])
    review_route = routes['phases'][-1]
    phases = []
    for route in routes['phases'][:-1]:
        key = route['phase']
        contract = (definition['requirements_management'] if key == 'Requirements'
                    else next(p for p in definition['phases'] if p['id'] == key))
        relevant = [d for d in dels.values() if key in d.get('adm', '').split()
                    or d['id'] in contract['deliverables']]
        phases.append({'id': key, 'title': TITLES[key], 'inputs': contract.get('inputs', []),
                       'activities': contract['steps'], 'criteria': contract.get('criteria', {}),
                       'owners': contract['owners'], 'source_refs': contract['source_refs'],
                       'source_step_ids': [s['id'] for s in contract.get('source_step_records', [])],
                       'source_steps': [{k:s[k] for k in ('id','name_en','text_en','explanation_zh',
                                                        'responsibility_column','interpretation_kind') if k in s}
                                        for s in contract.get('source_step_records', [])],
                       'source_sections': source_refs(contract.get('foundation_binding')),
                       'deliverables': [{'id': d['id'], 'name': d['name_zh'],
                            'role': ('phase-contract-output-candidate' if d['id'] in contract['deliverables']
                                     else 'registry-phase-context'),
                            'condition': next((c['condition_en'] for c in contract.get('conditional_deliverables', [])
                                               if c['id'] == d['id']), None),
                            'artifact_ids': d['artifact_ids'],
                            'source_sections': source_refs(d.get('foundation_binding'))} for d in relevant],
                       'artifacts': route['artifact_candidates']})
    mapping = {'schema_version': 'adm-flow-1.0', 'notice': NOTICE,
               'phase_candidate_notice': '候选交付物不是强制输出；registry-phase-context仅为注册表的适用语境。',
               'content_chain': ['利益相关者关注点', '视点选择', '共享对象与关系', '目录／矩阵／图',
                                 '交付物章节与证据', '评审与实际接受决定', '治理记录与存储库'],
               'phases': phases,
               'cross_cutting_review': {'id': 'Review', 'activities': review_route['activities'],
                   'artifacts': review_route['artifact_candidates'], 'source_refs': review_route['source_refs']},
               'deliverable_catalog': [
                   {'id': d['id'], 'name': d['name_zh'], 'adm': d.get('adm', ''),
                    'artifact_ids': d['artifact_ids'], 'source_sections': source_refs(d.get('foundation_binding'))}
                   for d in dels.values()],
               'artifact_catalog': [{'id': a['id'], 'name': a['name_zh'], 'kind': a['kind'],
                    'profile_ids': [p['id'] for p in profiles.values() if p['artifact_id'] == a['id']],
                    'phase_ids': ([r['id'] for r in phases if any(c['id'] == a['id'] for c in r['artifacts'])]
                                  + (['Review'] if any(c['id']==a['id'] for c in review_route['artifact_candidates']) else []))}
                   for a in arts.values()]}
    if cycle is not None:
        invalid = schema_issues(cycle)
        if invalid:
            raise ValueError('ADM周期格式无效：' + json.dumps(invalid, ensure_ascii=False))
        actual = check_cycle(cycle, model, evidence_root or '.')
        if any(e['code'] in ('model-invalid', 'phase-identity', 'iteration-id', 'dependency-reference',
                             'model-reference', 'project-mismatch', 'example-mismatch') for e in actual['errors']):
            raise ValueError('无法为无效周期引用绘图：' + json.dumps(actual['errors'], ensure_ascii=False))
        names = {(group, r['id']): r.get('name', r.get('title', r['id']))
                 for group in ('entities', 'relationships', 'views', 'deliverables', 'analyses')
                 for r in model.get(group, [])}
        result_by_phase = {p['phase']: p for p in actual['phases']}
        rows = []
        for p in cycle['phases']:
            for it in p['iterations']:
                rows.append({'id': it['id'], 'phase': p['phase'], 'applicability': p['applicability'],
                             'recorded_status': it['status'], 'decision_status': it['decision']['status'],
                             'current_phase_check': result_by_phase[p['phase']],
                             'reason': it['reason'], 'depends_on': it['depends_on'],
                             'input_refs': [{**r, 'name': names[(r['collection'], r['id'])]} for r in it['input_refs']],
                             'output_refs': [{**r, 'name': names[(r['collection'], r['id'])]} for r in it['output_refs']]})
        mapping['cycle'] = {'id': cycle['id'], 'project_id': cycle['project_id'], 'is_example': cycle['is_example'],
                            'scope': cycle['scope'], 'previous_cycle_id': cycle.get('previous_cycle_id'),
                            'iterations': rows, 'requirements': cycle['requirements'], 'check': actual,
                            'notice': '依赖箭头只来自实际depends_on；已填写completed与当前有效完成分别显示。'}
    return mapping


def wrapped(text, width, size=20):
    # Conservative CJK/Latin widths, with line breaks retained.
    lines = []
    for paragraph in str(text).split('\n'):
        current, units = '', 0
        for c in paragraph:
            n = size if ord(c) > 255 else size * .59
            if current and units + n > width:
                lines.append(current)
                current, units = '', 0
            current += c
            units += n
        lines.append(current)
    return lines


class Canvas:
    def __init__(self, title, width, height, status='方法框架 / 候选映射'):
        self.width, self.height = width, height
        self.items = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
                      '<defs><style>__FONT__ text{font-family:TogafCJK,sans-serif}</style>',
                      '<marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="#52677f"/></marker></defs>',
                      f'<rect width="{width}" height="{height}" fill="#f8fafc"/>']
        self.text(38, 45, title, 28, '#18334a')
        self.text(38, 77, status, 17, '#52677f')
        self.text(38, height - 26, NOTICE, 17, '#52677f')

    def text(self, x, y, value, size=20, color='#18334a'):
        self.items.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}">{html.escape(str(value))}</text>')

    def box(self, x, y, w, h, title, rows, color='#eaf2fa', size=19):
        self.items.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{color}" stroke="#cad6e2"/>')
        title_lines = wrapped(title, w - 36, 21)
        for i, line in enumerate(title_lines):
            self.text(x + 18, y + 32 + i*34, line, 21)
        yy = y + 65 + (len(title_lines)-1)*34
        for row in rows:
            for line in wrapped(row, w - 36, size):
                self.text(x + 18, yy, line, size)
                yy += size + 8
            yy += 8
        if yy - 16 > y + h:
            raise ValueError('流程图文字超出卡片：' + title)

    def arrow(self, points, dashed=False):
        coords = ' '.join(f'{x},{y}' for x, y in points)
        dash = ' stroke-dasharray="7 6"' if dashed else ''
        self.items.append(f'<polyline points="{coords}" fill="none" stroke="#52677f" stroke-width="2"{dash} marker-end="url(#arrow)"/>')

    def finish(self):
        return ''.join(self.items) + '</svg>'


def framework_svg(mapping):
    c = Canvas('ADM完整架构流程 · 从能力建立到持续变更', 1700, 2050)
    c.box(40, 105, 270, 1845, '持续需求管理\n不是 Phase I',
          ['捕获并存储需求', '维护来源与版本基线', '把需求送入各阶段', '记录阶段排序与决定',
           '评估变化影响与冲突', '更新影响评估和存储库', '复核旧阶段与跨周期变化',
           '需求处置与优先级由相关阶段决定；需求管理负责过程与记录。'], '#e8f4ef')
    for i, p in enumerate(mapping['phases'][:-1]):
        y = 105 + i * 205
        outputs = '、'.join(d['name'] + ('（if any）' if d['condition'] else '')
                            for d in p['deliverables'] if d['role'] == 'phase-contract-output-candidate')
        c.box(365, y, 1040, 177, p['title'],
              [PURPOSE[p['id']], '候选工作产品：' + outputs], size=20)
        c.arrow([(310, y + 70), (365, y + 70)], True)
        c.arrow([(365, y + 120), (310, y + 120)], True)
        if i < 8:
            c.arrow([(885, y + 177), (885, y + 205)])
    c.arrow([(1405, 1875), (1650, 1875), (1650, 398), (1405, 398)], True)
    c.text(1460, 300, 'H → A / 新周期', 18)
    c.arrow([(1405, 808), (1510, 808), (1510, 603), (1405, 603)], True)
    c.text(1440, 670, 'C反馈B', 18)
    c.arrow([(1405, 1013), (1460, 1013), (1460, 808), (1405, 808)], True)
    c.text(1440, 1080, 'D反馈C', 18)
    for target_y in (603, 808, 1013):
        c.arrow([(1405, 1218), (1570, 1218), (1570, target_y), (1405, target_y)], True)
    c.text(1440, 950, 'E反馈B/C/D', 18)
    for target_y in (1218, 1423):
        c.arrow([(1405, 1675), (1610, 1675), (1610, target_y), (1405, target_y)], True)
    c.text(1440, 1550, 'G偏离反馈E/F', 18)
    c.text(365, 1989, '治理门：评审当前需求、跨域影响、阶段判据和真实证据；接受或重开由授权决策者记录。', 19)
    return c.finish()


def box_height(rows, width=282, size=19):
    return 78 + sum(len(wrapped(r, width - 36, size)) * (size + 8) + 8 for r in rows)


def phase_svg(p):
    outputs = [d['name'] + ('（if any）' if d['condition'] else '')
               for d in p['deliverables'] if d['role'] == 'phase-contract-output-candidate']
    output_art_ids = {a for d in p['deliverables'] for a in d['artifact_ids']}
    selected = [a for a in p['artifacts'] if a['id'] in output_art_ids]
    kinds = {'catalog': '目录', 'matrix': '矩阵', 'diagram': '图', 'table': '表'}
    rows = [[*p['inputs']], [f'{i + 1}. {s}' for i, s in enumerate(p['activities'])],
            [f'{kinds.get(a["kind"],a["kind"])}：{a["name"]}' for a in selected],
            outputs + ['语境输入／复用：' + d['name'] for d in p['deliverables']
                       if d['role'] != 'phase-contract-output-candidate'],
            list(p['criteria'].values()) + ['记录依据、决策权人与接受／重开决定']]
    if not rows[2]:
        rows[2] = ['按关注点选择目录、矩阵和图；完整候选见阶段说明']
    h = max(box_height(r) for r in rows)
    c = Canvas(p['title'] + ' · 输入—工作—制品—交付物—治理门', 1640, h + 245)
    labels = ['输入与已知约束', '阶段分析工作', '表达制品（示例）', '候选交付物', '评审与退出判据']
    for i, (label, content) in enumerate(zip(labels, rows)):
        x = 30 + i * 322
        c.box(x, 118, 282, h, label, content, color='#e8f4ef' if i == 4 else '#eaf2fa')
        if i < 4:
            c.arrow([(x + 282, 153), (x + 322, 153)])
    c.arrow([(1460, 118 + h), (1460, 155 + h), (495, 155 + h), (495, 118 + h)], True)
    c.text(585, h + 182, '未满足／需求变化 → 记录缺口并迭代；有效输出按版本交给后续工作', 18)
    return c.finish()


def requirements_svg(p):
    rows = [['来自Preliminary、A–H和旧周期的需求、冲突与变化', '来源、责任人、验收条件、适用范围及版本'],
            [f'{i+1}. {s}' for i, s in enumerate(p['activities'])],
            ['架构需求规格', '需求影响评估（版本n+1）', '架构需求存储库', '各阶段的实际排序与处置决定'],
            ['复核当前与以前阶段的影响', '决定当前实现或后续周期处理', '更新基线、追溯与存储库',
             '受影响阶段追加迭代、重做评审证据']]
    h = max(box_height(r, 350) for r in rows)
    c = Canvas(TITLES['Requirements'] + ' · 跨阶段反馈循环', 1640, h + 260)
    for i, (title, content) in enumerate(zip(['捕获', '过程与记录', '工作产品', '反馈与阶段决定'], rows)):
        x = 30 + i * 404
        c.box(x, 115, 350, h, title, content, '#e8f4ef')
        if i < 3:
            c.arrow([(x+350, 150), (x+404, 150)])
    c.arrow([(1420, h+115), (1420, h+155), (205, h+155), (205, h+115)], True)
    c.text(405, h+182, '10个来源步骤的完整责任分列见requirements.md；需求管理不独立授予优先级或批准。', 18)
    return c.finish()


def content_svg(mapping):
    c = Canvas('架构内容关系 · 从关注点到受评审工作产品', 1700, 790)
    c.box(40, 115, 350, 255, '关注点与共享架构模型', ['明确决策、范围与利益相关者', '选择视点与建模约束', '共享稳定对象ID、关系及状态'])
    c.box(455, 115, 450, 255, '制品：三种表达', ['目录：识别对象、属性与责任', '矩阵：核对关系与覆盖', '图：表达结构、行为、交互或演进'])
    c.box(970, 115, 330, 255, '交付物：组织工作产品', ['章节组织多个制品与证据', '明确范围、结论及追溯', '版本化评审与实际接受'])
    c.box(1360, 115, 300, 255, '治理与资料库', ['记录决定、偏离与豁免', '存储基线与可复用资产', '变化反馈到需求和阶段'])
    for a,b in [(390,455),(905,970),(1300,1360)]:
        c.arrow([(a,240),(b,240)])
    c.box(455, 430, 500, 225, 'ABB · 架构构建块', ['需要的功能、服务与能力', '需求、接口及质量约束', '制品描述ABB；并非每个方框都是ABB'])
    c.box(1050, 430, 500, 225, 'SBB · 解决方案构建块', ['具体实现组成及运营配置', '依据ABB与约束建立实现映射', '选定产品不等于实际实施符合'])
    c.arrow([(705,370),(705,430)])
    c.arrow([(955,530),(1050,530)])
    c.text(970,505,'约束实现',18)
    c.text(40,715,f'当前映射：{len(mapping["deliverable_catalog"])}交付物，{len(mapping["artifact_catalog"])}制品族；逐项清单与阶段依据见README / mapping.json。',21)
    return c.finish()


def mermaid_framework(mapping):
    text = ['flowchart TB', '  RM["持续需求管理：捕获、基线、影响与反馈；不是Phase I"]']
    phases = [p['id'] for p in mapping['phases'] if p['id'] != 'Requirements']
    for p in phases:
        text.append(f'  {p}["{TITLES[p]}"]')
        text.extend([f'  RM -.需求与版本.-> {p}', f'  {p} -.变化与处置记录.-> RM'])
    for a,b in zip(phases, phases[1:]):
        text.append(f'  {a} -->|常见信息流| {b}')
    text.extend(['  C -.数据应用发现修正业务.-> B', '  D -.可行性反馈.-> C',
                 '  E -.整合差距后迭代.-> B', '  G -.实施偏离反馈.-> E', '  H -.重开或新周期.-> A'])
    return '\n'.join(text) + '\n'


def mermaid_phase(p):
    def safe(value):
        return html.escape(str(value), quote=True).replace('\n', '<br/>')
    groups = ['输入：' + '；'.join(p.get('inputs', []) or ['各阶段需求与变化']),
              '分析：' + '；'.join(p['activities']),
              '制品：按关注点选择目录、矩阵与图',
              '候选交付物：' + '；'.join(d['name'] + ('（if any）' if d['condition'] else '') for d in p['deliverables']),
              '治理门：' + '；'.join(p['criteria'].values())]
    lines = ['flowchart LR']
    for i,g in enumerate(groups):
        lines.append(f'  N{i}["{safe(g)}"]')
        if i:
            lines.append(f'  N{i-1} --> N{i}')
    lines.extend(['  N4 -.未满足或需求变化.-> N1', '  RM["持续需求管理"]', '  RM -.版本与反馈.-> N1', '  N4 -.处置记录.-> RM'])
    return '\n'.join(lines) + '\n'


def cycle_views(cycle):
    rows = cycle['iterations']
    lines = ['flowchart TB']
    c = Canvas('实际ADM周期 · ' + cycle['id'], 1720, 205 + len(rows) * 205,
               ('虚构案例 / ' if cycle['is_example'] else '项目记录 / ') + '已记录状态与当前检查分别显示')
    ids = {r['id']: 'I'+str(i) for i,r in enumerate(rows)}
    for i,row in enumerate(rows):
        check = row['current_phase_check']
        state = '当前状态：' + str(check.get('status', '未判定'))
        label = row['id'] + ' · ' + TITLES[row['phase']] + ' / 记录：' + row['recorded_status'] + ' / ' + state
        lines.append(f'  {ids[row["id"]]}["{html.escape(label,quote=True)}"]')
        for dep in row['depends_on']:
            lines.append(f'  {ids[dep]} -->|实际信息依赖| {ids[row["id"]]}')
        c.box(200, 110+i*205, 1482, 175, row['id'] + ' · ' + TITLES[row['phase']],
              ['记录：' + row['recorded_status'] + '；决定：' + row['decision_status'] + '；' + state,
               '实际依赖：' + ('、'.join(row['depends_on']) or '未记录')], size=20)
        c.text(220, 265+i*205, '完整输入／输出对象与缺口见cycle-records.md和mapping.json',17)
    positions={r['id']:i for i,r in enumerate(rows)}
    for i,row in enumerate(rows):
        for j,dep in enumerate(row['depends_on']):
            x=60+(positions[dep]%4)*28+j*12
            c.arrow([(200,155+positions[dep]*205),(x,155+positions[dep]*205),
                     (x,200+i*205),(200,200+i*205)])
    return c.finish(), '\n'.join(lines)+'\n'


def phase_markdown(p):
    lines = ['# '+p['title'], '', '本页由当前阶段合同和注册表派生。候选产品可复用、补充和升版；接受须有实际证据。', '',
             '## 输入', '', *['- '+s for s in p['inputs']], '', '## 工作与治理门', '']
    lines += [f'{i+1}. {s}' for i,s in enumerate(p['activities'])]
    lines += ['', *['- '+key+'：'+s for key,s in p['criteria'].items()], '', '## 候选交付物与制品', '',
              '|交付物ID|名称|关系依据|所含制品ID|', '|---|---|---|---|']
    lines += ['|'+d['id']+'|'+d['name']+('（if any）' if d['condition'] else '')+'|'+d['role']+'|'+', '.join(d['artifact_ids'])+'|'
              for d in p['deliverables']]
    lines += ['', '## 完整制品候选路由', '', '|制品ID|名称|表达|阶段依据|Profiles|', '|---|---|---|---|---|']
    lines += ['|'+a['id']+'|'+a['name']+'|'+a['kind']+'|'+a['phase_basis']+'|'+', '.join(a['profile_ids'])+'|'
              for a in p['artifacts']]
    lines += ['', '## 完整来源步骤与责任', '', '|步骤ID|原名|责任|来源绑定中文解释|', '|---|---|---|---|']
    for step in p['source_steps']:
        explanation=step.get('explanation_zh',[])
        if isinstance(explanation,list):
            explanation='；'.join(explanation)
        lines.append('|'+step['id']+'|'+step['name_en']+'|'+step.get('responsibility_column','本阶段')+'|'+
                     str(explanation).replace('|','\\|').replace('\n','<br/>')+'|')
    lines += ['',
              '来源摘要：'+ '；'.join(p['source_refs']), '', '具体原文节与定位保留在mapping.json及adm-phases.json。', '']
    return '\n'.join(lines)


def html_index(out, mapping, diagrams, rendered):
    """A standalone reader: embedded previews, native keyboard navigation."""
    labels = {'adm-framework':'ADM总览', 'content-chain':'架构内容与ABB／SBB',
              'requirements':'持续需求管理', 'cycle-iterations':'实际周期与信息依赖'}
    labels.update({'phase-'+p['id']:p['title'] for p in mapping['phases'] if p['id']!='Requirements'})
    links=[]
    panels=[]
    for i,(name,_,_) in enumerate(diagrams):
        label=labels[name]
        escaped=html.escape(label)
        status=('虚构案例 / 记录检查' if mapping.get('cycle',{}).get('is_example') else '项目周期 / 记录检查') if name=='cycle-iterations' else '方法框架 / 候选映射'
        svg=base64.b64encode((out/(name+'.svg')).read_bytes()).decode()
        links.append(f'<a href="#panel-{name}">{escaped}</a>')
        files=[f'<a href="{name}.svg" target="_blank" rel="noopener">打开SVG原图</a>',
               f'<a href="{name}.mmd" download>下载Mermaid源码</a>']
        if rendered:
            files.append(f'<a href="{name}.png" download>下载PNG</a>')
        doc='cycle-records' if name=='cycle-iterations' else name
        if (out/(doc+'.md')).is_file():
            files.append(f'<a href="{doc}.md">查看完整阶段说明</a>')
        panels.append(f'<details id="panel-{name}"'+(' open' if i==0 else '')+'>'+
                      f'<summary><span>{escaped}</span><small>{html.escape(status)}</small></summary>'+
                      '<div class="panel"><div class="files">'+' '.join(files)+'</div>'+
                      f'<img src="data:image/svg+xml;base64,{svg}" alt="{escaped}：中文架构流程图" loading="lazy">'+
                      '</div></details>')
    counts=f'{len(mapping["phases"])}个工作域 · 94个来源步骤 · {len(mapping["deliverable_catalog"])}项交付物 · {len(mapping["artifact_catalog"])}个制品族'
    actual=''
    if 'cycle' in mapping:
        c=mapping['cycle']
        actual='<p class="cycle">当前案例：'+html.escape(c['id'])+' · 周期记录检查：'+('闭合' if c['check']['recorded_cycle_complete'] else '仍有缺口')+'。记录状态与当前证据检查在实际周期图中分别显示。</p>'
    return '''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>ADM框架与完整架构流程图</title><style>
:root{color-scheme:light;--ink:#18334a;--muted:#52677f;--line:#ccd8e3;--green:#e8f4ef}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#f5f8fb;color:var(--ink);font:16px/1.7 system-ui,-apple-system,"PingFang SC","Microsoft YaHei",sans-serif}
a{color:#175586;text-underline-offset:4px}a:focus-visible,summary:focus-visible{outline:3px solid #2477b4;outline-offset:4px}.skip{position:absolute;top:-60px;left:20px;padding:10px;background:#fff;z-index:10}.skip:focus{top:8px}
main{max-width:1480px;margin:auto;padding:44px 28px 80px}.eyebrow{font-size:14px;letter-spacing:.08em;color:var(--muted);margin:0}h1{font-size:clamp(28px,4vw,42px);line-height:1.25;margin:12px 0 18px;font-weight:650}header p{max-width:1080px;margin:12px 0}.counts{font-weight:600}.cycle{background:var(--green);border-left:4px solid #7da996;padding:12px 18px;border-radius:6px}
nav{display:flex;flex-wrap:wrap;gap:9px;margin:28px 0}nav a{background:white;border:1px solid var(--line);border-radius:20px;padding:7px 14px;text-decoration:none;font-size:14px}nav a:hover{background:#eaf2fa}
details{margin:16px 0;border:1px solid var(--line);border-radius:12px;background:#fff;overflow:hidden;scroll-margin-top:20px}summary{cursor:pointer;padding:18px 22px;font-size:20px;font-weight:600}summary small{display:inline-block;margin-left:18px;color:var(--muted);font-size:14px;font-weight:400}.panel{border-top:1px solid var(--line);padding:18px}.files{display:flex;flex-wrap:wrap;gap:18px;margin:0 0 16px;font-size:14px}.panel img{display:block;width:100%;height:auto;background:#f8fafc}footer{margin-top:32px;color:var(--muted);font-size:14px}footer a{margin-right:20px}
@media(max-width:640px){main{padding:28px 14px 50px}summary{padding:16px;font-size:18px}summary small{display:block;margin:5px 0 0}.panel{padding:10px}.files{gap:10px 18px}nav{gap:7px}nav a{padding:5px 10px}}
</style></head><body><a class="skip" href="#diagrams">跳转到流程图</a><main>
<header><p class="eyebrow">TOGAF · ARCHITECTURE DEVELOPMENT METHOD</p><h1>ADM框架与完整架构流程图</h1>
<p>从架构能力建立、愿景和跨域分析，到迁移、实施治理与持续变更。展开阶段查看中文图，打开原图核对细节；完整候选与来源步骤保留在阶段说明中。</p>
<p class="counts">'''+html.escape(counts)+'''</p><p>读图：实线表示常见信息流，虚线表示需求反馈与迭代。B／C／D可以并行协调；持续需求管理贯穿周期。候选交付物可跨阶段复用，阶段退出依据当前判据、实际证据与授权决定。</p>'''+actual+'''</header>
<nav aria-label="流程图导航">'''+''.join(links)+'''</nav><section id="diagrams" aria-label="ADM完整流程图">'''+''.join(panels)+'''</section>
<footer><a href="README.md">完整阅读说明</a><a href="mapping.json">阶段与制品映射</a><a href="coverage.json">覆盖验证</a><a href="manifest.json">文件与输入指纹</a><p>本页预览已嵌入中文SVG，可离线打开。原图、源码与阶段说明链接使用同目录保存的交付文件。</p></footer>
</main><script>
function openPanel(hash,focus){const panel=document.getElementById(hash.slice(1));if(panel&&panel.tagName==='DETAILS'){panel.open=true;if(focus)panel.querySelector('summary').focus({preventScroll:true});panel.scrollIntoView({behavior:'smooth',block:'start'});}}
document.querySelectorAll('nav a').forEach(link=>link.addEventListener('click',event=>{event.preventDefault();openPanel(link.hash,true);history.replaceState(null,'',link.hash);}));
if(location.hash)openPanel(location.hash,false);
</script></body></html>'''


def generate_flow(out, cycle=None, model=None, evidence_root=None, render=False):
    out = Path(out).resolve()
    if out.exists():
        raise ValueError('流程图输出目录已存在；使用新目录保留历史证据')
    mapping = build_mapping(cycle, model, evidence_root)
    out.mkdir(parents=True)
    dump(out/'mapping.json', mapping)
    diagrams = [('adm-framework', framework_svg(mapping), mermaid_framework(mapping)),
                ('content-chain', content_svg(mapping),
                 'flowchart LR\n  C["关注点与共享模型"] --> A["目录／矩阵／图"] --> D["交付物与章节证据"] --> G["评审决定与治理记录"]\n  A --> B["ABB：能力及约束"] --> S["SBB：具体实现"]\n  G -.变化反馈.-> C\n')]
    for p in mapping['phases']:
        name = 'requirements' if p['id'] == 'Requirements' else 'phase-'+p['id']
        diagrams.append((name, requirements_svg(p) if p['id']=='Requirements' else phase_svg(p), mermaid_phase(p)))
        (out/(name+'.md')).write_text(phase_markdown(p))
    if 'cycle' in mapping:
        svg,mmd = cycle_views(mapping['cycle'])
        diagrams.append(('cycle-iterations',svg,mmd))
        text = ['# 实际周期对象、状态与依赖', '', mapping['cycle']['notice'], '',
                '当前检查仍有缺口时保留其原状态；图不覆盖、签署或推进周期。', '']
        for it in mapping['cycle']['iterations']:
            text += ['## '+it['id'], '', '记录状态：'+it['recorded_status']+'；决定：'+it['decision_status'], '',
                     '当前阶段检查：`'+str(it['current_phase_check'].get('status'))+'`', '',
                     '依赖：'+', '.join(it['depends_on']), '',
                     *[kind+'：'+r['collection']+'/'+r['id']+' · '+r['name']
                       for kind,key in [('输入','input_refs'),('输出','output_refs')] for r in it[key]], '']
        (out/'cycle-records.md').write_text('\n'.join(text))
    from generate import subset_font
    font_b64 = subset_font(''.join(svg for _,svg,_ in diagrams), out/'font-subset.ttf')
    jobs=[]
    for name,svg,mmd in diagrams:
        svg = svg.replace('__FONT__', '@font-face{font-family:TogafCJK;src:url(data:font/ttf;base64,'+font_b64+')}')
        (out/(name+'.svg')).write_text(svg)
        (out/(name+'.mmd')).write_text(mmd)
        jobs.append({'id':name,'kind':'svg','source':name+'.svg','svg':name+'.svg','png':name+'.png'})
    dump(out/'render-jobs.json', {'font':'font-subset.ttf','oversized_policy':'tile','jobs':jobs})
    if render:
        result=subprocess.run(['node', str(ROOT/'scripts/render.mjs'), str(out/'render-jobs.json')], capture_output=True, text=True)
        (out/'render.log').write_text(result.stdout+result.stderr)
        if result.returncode:
            raise ValueError('ADM流程图渲染失败；已保留来源和render-report.json：'+result.stderr)
    coverage = {'status':'passed','scope':'contract-and-record-projection',
                'phase_ids':[p['id'] for p in mapping['phases']],
                'source_step_count':sum(len(p['source_step_ids']) for p in mapping['phases']),
                'deliverable_count':len(mapping['deliverable_catalog']),
                'artifact_family_count':len(mapping['artifact_catalog']),
                'unmapped_deliverable_ids':[d['id'] for d in mapping['deliverable_catalog'] if not any(d['id']==x['id'] for p in mapping['phases'] for x in p['deliverables'])],
                'unmapped_artifact_ids':[a['id'] for a in mapping['artifact_catalog'] if not a['phase_ids']],
                'diagram_ids':[d[0] for d in diagrams], 'rendered':render,
                'professional_acceptance':'not-granted-by-flow-generation'}
    if coverage['unmapped_deliverable_ids'] or coverage['unmapped_artifact_ids']:
        coverage['status']='failed'
    dump(out/'coverage.json',coverage)
    readme=['# ADM框架、架构制品与完整架构流程图', '', NOTICE, '',
            '从当前阶段合同、23项交付物和制品注册派生；完整目录和来源定位见[mapping.json](mapping.json)。', '',
            '总览实线给出阅读顺序，实际退出依赖以周期`depends_on`为准。B/C/D可并行协调；C同时分析数据与应用。', '',
            '阶段细图列出工作、制品示例和治理门；Markdown保留全部候选目录／矩阵／图。条件输出保留if any。', '',
            '## 图形入口', '', '|范围|SVG向量图|可编辑源码|'+('PNG|' if render else '渲染状态|'), '|---|---|---|---|']
    for name,_,_ in diagrams:
        readme.append('|'+name+'|['+name+'.svg]('+name+'.svg)|['+name+'.mmd]('+name+'.mmd)|'+('['+name+'.png]('+name+'.png)' if render else '尚未请求渲染')+'|')
    readme += ['', '## 逐阶段资料', '', *['- ['+p['title']+']('+('requirements' if p['id']=='Requirements' else 'phase-'+p['id'])+'.md)' for p in mapping['phases']], '',
               '## 交付物全表', '', '|交付物ID|名称|阶段语境|制品ID|', '|---|---|---|---|']
    readme += ['|'+d['id']+'|'+d['name']+'|'+d['adm']+'|'+', '.join(d['artifact_ids'])+'|' for d in mapping['deliverable_catalog']]
    readme += ['', '## 贯穿阶段的制品评审', '', 'Review为贯穿阶段的工作路由，不是新增ADM阶段。', '',
               *['- '+a['name']+'（'+a['id']+'）：'+', '.join(a['profile_ids'])
                 for a in mapping['cross_cutting_review']['artifacts']]]
    readme += ['', '## 可复现生成', '', '```sh', 'python3 -B /path/to/skills/_shared/scripts/adm.py flow --out /new/adm-flow --render',
               '# 实际周期另加 --cycle /path/adm-cycle.json --model /path/model.json', '```', '',
               '输出目录必须不存在。生成操作只读当前合同和周期，不产生批准、业务事实或阶段退出。', '',
               '[投影覆盖结果](coverage.json)核对阶段／来源步骤／交付物／制品路由；图形渲染和实际专业验收分别取证。', '']
    if 'cycle' in mapping:
        readme += ['[实际周期的全部输入／输出、依赖及状态](cycle-records.md)。', '']
    readme.insert(4,'[离线中文导航与图形预览](index.html)（SVG预览嵌入单页，原图与源码可打开／下载）。')
    (out/'README.md').write_text('\n'.join(readme))
    (out/'index.html').write_text(html_index(out,mapping,diagrams,render))
    dependencies = ['references/adm-phases.json','artifacts.json','deliverables.json','capabilities.json',
                    'scripts/adm.py','scripts/adm_flow.py','scripts/architecture_delivery.py',
                    'scripts/render.mjs','scripts/generate.py','assets/fonts/NotoSansSC.ttf']
    manifest = {'schema_version':'adm-flow-manifest-1.0', 'input_sha256':{n:sha(ROOT/n) for n in dependencies},
                'output_sha256':{str(p.relative_to(out)):sha(p) for p in sorted(out.iterdir()) if p.is_file()},
                'rendered':render,'coverage_status':coverage['status']}
    if cycle is not None:
        manifest['cycle_sha256'] = hashlib.sha256(json.dumps(cycle, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
        manifest['model_sha256'] = hashlib.sha256(json.dumps(model, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    dump(out/'manifest.json',manifest)
    return coverage
