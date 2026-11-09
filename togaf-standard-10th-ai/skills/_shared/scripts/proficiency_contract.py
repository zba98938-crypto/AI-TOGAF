"""Reproducible G249 profiles; explicit project contracts built on source tables."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OWNER = 'togaf-organization-roles'
SCALE = 'G249-table5-1'
DEVELOPMENT_FIELDS = ['person', 'role', 'skill_id', 'scale_id', 'task_refs', 'requirement_refs',
                      'current_proficiency', 'target_proficiency', 'behavioral_gap', 'action',
                      'success_criteria', 'reassessment', 'history', 'evidence']
RELATION_FIELDS = ['proficiency', 'assessment_kind', 'assessment_state', 'scale_id']


def scale():
    table = json.loads((ROOT / 'references/source-tables/g249-skill-proficiency.json').read_text())
    return {'id': SCALE, 'name': 'G249 Table 5-1 人的技能熟练度',
            'anchors': table['anchors'], 'evidence': ['g249-table-source']}


def sources():
    return [{'id': 'g249-table-source', 'kind': 'official',
             'description': 'G249 §5 Tables 5-1/5-2：参考等级与量表；不证明任何人员已具备能力',
             'locator': 'corpus/sources/pdf/G249e.pdf#page=27'},
            {'id': 'example-source', 'kind': 'example',
             'description': '虚构项目要求、辅导应用记录与复评计划；非实际人员评价'}]


def entity(identity, kind, name, **attrs):
    return {'id': identity, 'type': kind, 'name': name, 'attributes': attrs,
            'evidence': ['example-source'], 'certainty': 'assumed'}


def fragment(profile, entities, relationships):
    return {'notice': '虚构案例；原文参考、项目目标与个人观察独立记录，生成不等于评审通过。',
            'sources': sources(), 'scales': [scale()], 'entities': entities, 'relationships': relationships,
            'view': {'id': 'v-' + profile['id'], 'artifact_id': profile['artifact_id'],
                     'profile_id': profile['id'], 'title': profile['name'] + '／虚构案例',
                     'entity_ids': [e['id'] for e in entities],
                     'relationship_ids': [r['id'] for r in relationships],
                     'analysis': '目标与人员证据逐项比较；未知不赋低分；目标不由个人现状倒推。',
                     'legend': '原文参考≠项目目标≠人员观察；四级技能熟练度≠组织成熟度≠Open CA三级认证。'}}


def specialize(profile):
    """Return None for unrelated profiles, without altering their contract."""
    if profile.get('artifact_id') not in {'architecture-skill-matrix', 'architecture-development-plan'}:
        return None
    pid = profile['id']
    skill_id = 'G249:skill:business:business-scenario'
    role_id = 'G249:role:enterprise-architect'
    if profile['artifact_id'] == 'architecture-skill-matrix':
        profile.update(entity_types=['skill', 'architecture_role', 'guide:architecture-role'], relationship_types=['supports_role'],
                       required_attributes={'skill': ['skill_id', 'category', 'subskill'],
                                            'architecture_role': ['definition'],
                                            'guide:architecture-role': ['tier', 'scope', 'primary_responsibility']},
                       source_refs=['G249 §5 Tables 5-1 and 5-2'],
                       source_table_refs=['G249/table5-1', 'G249/table5-2'], source_structure_refs=[])
        profile['template'].update(source_figure=None, row_types=['skill'], column_types=['architecture_role', 'guide:architecture-role'],
                                   cell_meaning='按assessment_kind分别显示原文目标、项目目标与个人观察；值由属性生成',
                                   empty_meaning='未记录/待评估；不是1级、零分或不适用',
                                   layout_notes='同一技能角色单元可保留多个有语义和证据的评级记录')
        profile['checks'] = ['原文参考目标绑定原始技能与六个角色列；Chief和通用Segment不得伪造列',
                             '评级必须绑定量表和语义；未评价保留null，非法等级报错',
                             '项目目标保留任务和裁剪理由；个人观察保留正向行为证据与时点']
        s = entity(pid + '-skill', 'skill', '业务场景分析', skill_id=skill_id, category='Business', subskill='Business Scenario')
        role = entity(pid + '-role', 'architecture_role', '企业架构角色', definition='本项目将业务场景结果用于跨域架构决策', reference_role_id=role_id)
        relationships = []
        records = [
            ('source', 'source_reference_target', 'reference', 3, {'reference_role_id': role_id, 'source_locator': 'G249 Table 5-2 Business Scenario / Enterprise Architect'}),
            ('target', 'tailored_target', 'proposed', 3, {'tailoring_reason': '本次需形成可用于决策的业务场景；采用原文参考等级，限本任务范围',
                                                       'task_refs': ['TASK-SCENARIO'], 'behavioral_criteria': ['能依据业务证据形成场景、识别冲突并说明决策依据；困难情形寻求专家']}),
            ('observed', 'observed_assessment', 'assessed', 2, {'person_ref': 'PERSON-A', 'task_refs': ['TASK-SCENARIO'], 'assessor': 'REVIEWER-A', 'observed_on': '2026-11-05',
                                                              'behavioral_evidence': [{'criterion': '在专家支持下处理场景中的冲突', 'demonstrated': True, 'evidence': ['example-source']}]}),
        ]
        for suffix, kind, state, value, extra in records:
            relationships.append({'id': pid + '-' + suffix, 'type': 'supports_role', 'source': s['id'], 'target': role['id'],
                                  'label': {'source': '原文参考目标', 'target': '项目目标', 'observed': '人员观察'}[suffix],
                                  'attributes': dict(proficiency=value, assessment_kind=kind, assessment_state=state, scale_id=SCALE, **extra),
                                  'evidence': ['g249-table-source' if suffix == 'source' else 'example-source'], 'certainty': 'assumed'})
        profile['example'] = fragment(profile, [s, role], relationships)
    else:
        profile.update(entity_types=['skill_development'], relationship_types=['traces_to'],
                       required_attributes={'skill_development': DEVELOPMENT_FIELDS},
                       source_refs=['G249 §5–6（发展计划字段与判据为项目约定）'])
        profile['checks'] = ['每项发展行动绑定技能、任务要求和量表，目标与当前证据分开',
                             '完成培训不自动提升评级；复评完成须引用实测评价和行为证据',
                             '历史证据不覆盖；目标不随观察值变化；未证明高级不自动降为低级']
        shared = dict(person='PERSON-A', role=role_id, skill_id=skill_id, scale_id=SCALE,
                      task_refs=['TASK-SCENARIO'], requirement_refs=['REQ-SCENARIO'], current_proficiency=2,
                      target_proficiency=3, behavioral_gap='缺少能据详细业务证据作决策并解释困难情况专家介入的观察',
                      evidence=['example-source'], history=[{'observed_on': '2026-11-05', 'proficiency': 2,
                                                            'evidence': ['example-source'], 'status': 'assessed',
                                                            'rationale': '在专家主持下实际完成场景冲突分析；不是由未达到3级反推'}])
        first = entity(pid + '-practice', 'skill_development', '共同主持并形成决策记录', **copy.deepcopy(shared),
                       action='与导师共同处理两个业务场景冲突，形成证据与决策理由',
                       success_criteria=['记录冲突、依据、备选及专家支持点'], order=1, start='2026-11-09', end='2026-11-13',
                       reassessment={'assessor': 'REVIEWER-A', 'due_on': '2026-11-13', 'criteria': ['检查共同实践产出'], 'status': 'planned'})
        second = entity(pid + '-reassess', 'skill_development', '完成任务并按行为证据复评', **copy.deepcopy(shared),
                        action='主导后续场景分析；评审实际决策理由、异议处理及必要的专家介入',
                        success_criteria=['足够细节支持有效决策', '困难情形及时寻求专家，保留依据'],
                        order=2, start='2026-11-16', end='2026-11-20',
                        reassessment={'assessor': 'REVIEWER-B', 'due_on': '2026-11-20', 'criteria': ['按任务行为证据核对G249三级含义'], 'status': 'planned'})
        rel = {'id': pid + '-dependency', 'type': 'traces_to', 'source': second['id'], 'target': first['id'],
               'label': '复评使用共同实践记录；培训出席不代替行为证据', 'evidence': ['example-source'], 'certainty': 'assumed'}
        profile['example'] = fragment(profile, [first, second], [rel])
    return profile['example']


def collaboration_profile():
    pid = 'architecture-role-collaboration'
    profile = {'id': pid, 'artifact_id': 'architecture-role-catalog', 'name': '架构角色协作与指导关系',
               'name_zh': '架构角色协作与指导关系', 'owner': OWNER, 'renderer': 'network',
               'source_refs': ['G249 §4 Figure 4-1（角色协作语义；图示不等于本地人事汇报）'],
               'source_structure_refs': ['references/source-structures/G249-fig4-1.json'], 'required_attributes': {'guide:architecture-role': ['tier', 'scope', 'primary_responsibility']},
               'entity_types': ['guide:architecture-role'], 'definition_status': 'source-derived-view-with-project-construction-rules',
               'template': {'source_verified': False, 'source_figure': 'G249/fig4-1', 'layout_notes': '角色关系按明示类型表达；专业指导、人事汇报、特化、协作与交接分开'},
               'checks': ['Chief是Enterprise角色特化，不从布局推导人事汇报', '每条关系需范围与证据；handoff需交付物与验收条件']}
    roles = [entity(pid + '-' + tier, 'guide:architecture-role', name, tier=tier, scope='本次订单履约架构工作', primary_responsibility=responsibility)
             for tier, name, responsibility in [('chief', '首席架构角色', '架构实践方向和跨域协调'), ('enterprise', '企业架构角色', '企业目标与架构约束对齐'),
                                                ('segment', '分段架构角色', '领域模型与演进安排'), ('solution', '解决方案架构角色', '在约束下设计交付方案')]]
    ids = {e['attributes']['tier']: e['id'] for e in roles}
    rows = [('specialization', 'chief', 'enterprise', '首席是企业架构角色的特化'),
            ('architecture_guidance', 'enterprise', 'segment', '专业指导，不表示雇佣汇报'),
            ('architecture_constraint', 'segment', 'solution', '架构约束及适用边界'),
            ('collaborates_with', 'solution', 'segment', '方案与域架构协作'),
            ('handoff', 'segment', 'solution', '交接经说明的接口约束和未决事项')]
    rels = []
    definitions = {}
    for index, (kind, start, end, label) in enumerate(rows):
        typ = 'g249:' + kind
        definitions[typ] = {'source_types': ['guide:architecture-role'], 'target_types': ['guide:architecture-role'], 'meaning': label}
        attrs = {'semantic_type': kind, 'scope': '订单履约架构任务'}
        if kind == 'handoff':
            attrs.update(deliverable_ref='DEL-INTERFACE', acceptance_criteria=['接口范围、约束、未决项及接收方均可追溯'])
        rels.append({'id': pid + '-relation' + str(index), 'type': typ, 'source': ids[start], 'target': ids[end],
                     'label': label, 'attributes': attrs, 'evidence': ['example-source'], 'certainty': 'assumed'})
    # reports_to is an available explicit relation, never synthesized from guidance.
    definitions['g249:reports_to'] = {'source_types': ['guide:architecture-role'], 'target_types': ['guide:architecture-role'], 'meaning': '仅在有明确组织授权证据时记录人事汇报'}
    profile['relationship_types'] = list(definitions)
    profile['example'] = fragment(profile, roles, rels)
    profile['example']['extensions'] = {'relationship_types': definitions}
    profile['example']['view']['legend'] = '指导/约束/协作/特化/交接分别按边类型读取；未画reports_to表示未声明，不能由纵向布局推断。'
    return profile


def assignment_profile():
    """Reuse the single maintained integration scenario, not a second runtime fixture."""
    import importlib.util
    path = ROOT / 'examples/g249-omnichannel/build.py'
    spec = importlib.util.spec_from_file_location('g249_profile_scenario', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    model = module.build(False)
    views = model.pop('views')
    view = next(v for v in views if v['profile_id'] == 'architecture-work-assignment-review')
    model['supporting_views'] = [v for v in views if v['id'] != view['id']]
    for key in ('schema_version', 'project', 'deliverables', 'gaps'):
        model.pop(key, None)
    model['view'] = view
    return {'id': 'architecture-work-assignment-review', 'artifact_id': 'architecture-role-catalog',
            'name': '架构工作与人员配置证据审查', 'name_zh': '架构工作与人员配置证据审查',
            'owner': OWNER, 'renderer': 'catalog', 'source_refs': ['G249 §3–6；操作输入与审查规则为项目约定'],
            'required_attributes': {'guide:g249-assessment-context': ['assessment_inputs']},
            'entity_types': ['guide:g249-assessment-context'], 'relationship_types': [],
            'analysis_methods': ['architecture-role-skill-assessment'],
            'definition_status': 'project-operational-view',
            'template': {'source_verified': False, 'layout_notes': '同一架构模型的任务、要求、人员证据、容量与发展计划的确定性审查'},
            'checks': ['完整输入绑定共享模型快照；模型变更需重评', '缺证据输出未决项；不将文件生成成功视为业务批准'],
            'example': model}


def method_contract(method):
    if method['id'] != 'architecture-role-skill-assessment':
        return
    method.update(source_refs=['G249 §3–6；G198仅用于历史对照，不合并量表'],
                  execution_method='architecture-role-skill-assessment',
                  calculator_id='architecture-role-skill-assessment',
                  calculation_policy='calculator_id为既有确定性执行器分发字段；本方法核对证据和约束，不计算人员合格分或认证等级。',
                  required_inputs=['架构实践委托与范围', '任务、角色与可观察要求', '绑定版本的量表', '人员行为证据', '独立的人力需求及可用容量'],
                  analysis_steps=['从实践委托确定任务与角色范围', '保留原文参考并明确裁剪目标及行为判据',
                                  '逐项核对人员正向行为证据；未知不评级', '区分技能差距与容量缺口',
                                  '将发展行动绑定任务、判据、复评与历史', '保持证据、职责、移交与授权边界'],
                  output_work_products=['architecture-role-catalog', 'architecture-skill-matrix', 'architecture-development-plan', 'ea-team-capacity-plan'],
                  implementation_status='deterministic-evidence-review-with-human-judgement-boundaries',
                  checks=['技能等级、组织成熟度、Open CA认证与人员容量分别记录', '不由缺少高级证据自动赋低级',
                          '原文目标、项目目标和人员观察不能互相覆盖'])
