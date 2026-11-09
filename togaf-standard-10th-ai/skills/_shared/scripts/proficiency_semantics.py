"""Evidence and scale checks for G249 skill assessments and development plans.

These are project modelling rules, not a personnel rating algorithm. Missing
legacy draft fields produce gaps; an explicit impossible value or contradictory
claim is an error. No lower rating is inferred from missing higher-level proof.
"""
import json
from pathlib import Path

SOURCE_TABLE = Path(__file__).resolve().parents[1] / 'references/source-tables/g249-skill-proficiency.json'
OFFICIAL_SCALE = 'G249-table5-1'
KINDS = {'source_reference_target', 'tailored_target', 'observed_assessment'}
STATES = {
    'source_reference_target': {'reference'},
    'tailored_target': {'proposed', 'adopted'},
    'observed_assessment': {'unassessed', 'evidence_insufficient', 'assessed', 'superseded'},
}


def is_explicit_unknown_current(entity, field):
    """An explicit unknown is an observation state, not an absent contract field."""
    attrs = entity.get('attributes') or {}
    state = attrs.get('current_assessment_state')
    return (entity.get('type') == 'skill_development' and field == 'current_proficiency'
            and field in attrs and attrs[field] is None
            and isinstance(state, str) and state in {'unassessed', 'evidence_insufficient'})


def check(model):
    issues = []
    entities = {e['id']: e for e in model.get('entities', [])}
    sources = {s['id']: s for s in model.get('sources', [])}
    scales = {s['id']: s for s in model.get('scales', [])}
    source_table = json.loads(SOURCE_TABLE.read_text())

    def issue(code, identity, message, level='warning'):
        issues.append({'level': level, 'code': code, 'id': identity, 'message': message})

    def missing(attrs, names, identity, code='proficiency-context-gap'):
        absent = [n for n in names if attrs.get(n) in (None, '', [], {})]
        if absent:
            issue(code, identity, '待补明确字段：' + ', '.join(absent))
        return absent

    def evidence_refs(value, identity, field):
        if not isinstance(value, list) or not value or any(not isinstance(v, str) for v in value):
            issue('proficiency-evidence-gap', identity, field + ' 须列来源ID；文字结论不能替代行为证据。')
            return []
        absent = [v for v in value if v not in sources]
        if absent:
            issue('dangling-reference', identity, field + ' 引用不存在：' + ', '.join(absent), 'error')
        return [sources[v] for v in value if v in sources]

    def rating(value, identity, field, scale_id):
        if value is None:
            return
        if isinstance(value, bool) or not isinstance(value, int) or value not in range(1, 5):
            issue('proficiency-value', identity, field + ' 必须为四级量表的整数1至4；未知用null并声明状态。', 'error')
            return
        if scale_id and not isinstance(scale_id, str):
            issue('proficiency-scale', identity, 'scale_id须为已声明量表的稳定ID。', 'error')
        elif scale_id and scale_id != OFFICIAL_SCALE:
            scale = scales.get(scale_id)
            if scale is None:
                issue('proficiency-scale-gap', identity, '项目量表须在model.scales显式定义：' + str(scale_id))
            elif value not in [a['value'] for a in scale.get('anchors', [])]:
                issue('proficiency-scale-value', identity, field + ' 不属于引用量表的锚点。', 'error')

    if OFFICIAL_SCALE in scales and scales[OFFICIAL_SCALE].get('anchors') != source_table['anchors']:
        issue('source-scale-redefinition', OFFICIAL_SCALE, '不得在G249原量表ID下替换锚点；项目细化须另设ID并保留来源。', 'error')

    for edge in model.get('relationships', []):
        if edge.get('type') != 'supports_role':
            continue
        attrs = edge.get('attributes') or {}
        identity = edge['id']
        scale_id = attrs.get('scale_id')
        value = attrs.get('proficiency')
        kind, state = attrs.get('assessment_kind'), attrs.get('assessment_state')
        rating(value, identity, 'proficiency', scale_id)
        missing(attrs, ['assessment_kind', 'assessment_state', 'scale_id'], identity)
        if kind is not None and (not isinstance(kind, str) or kind not in KINDS):
            issue('proficiency-kind', identity, '评级语义必须区分原文参考目标、项目裁剪目标和人员实测。', 'error')
            kind = None
        if state is not None and (not isinstance(state, str) or state not in set().union(*STATES.values())):
            issue('proficiency-state', identity, '未知评级状态：' + str(state), 'error')
            state = None
        elif kind in STATES and state is not None and state not in STATES[kind]:
            issue('proficiency-state', identity, '评级语义与状态不一致。', 'error')
        if state in {'unassessed', 'evidence_insufficient'}:
            if value is not None:
                issue('unassessed-proficiency', identity, '未评估或证据不足不能赋最低等级，也不能保留未获证实的新评级。', 'error')
        elif value is None:
            issue('proficiency-value-gap', identity, '评级值未提供；空格表示待补，不能默认为1。')
        if kind == 'source_reference_target':
            if scale_id and scale_id != OFFICIAL_SCALE:
                issue('source-proficiency-scale', identity, 'G249表5-2原值须绑定G249表5-1；裁剪量表改用tailored_target。', 'error')
            missing(attrs, ['reference_role_id', 'source_locator'], identity)
            role = entities.get(edge.get('target'), {})
            role_id = attrs.get('reference_role_id') or (role.get('attributes') or {}).get('reference_role_id')
            if (role.get('attributes') or {}).get('tier') in {'chief', 'segment'}:
                issue('source-role-column', identity, 'Chief和通用Segment没有表5-2独立列；应保留项目裁剪要求。', 'error')
            if role_id and role_id not in source_table['role_ids']:
                issue('source-role-column', identity, 'G249表5-2只有六个明示列；Chief、通用Segment及其他岗位不能伪造官方等级列。', 'error')
            skill = entities.get(edge.get('source'), {})
            skill_id = (skill.get('attributes') or {}).get('skill_id')
            values = source_table['skills'].get(skill_id) if isinstance(skill_id, str) else None
            if not values:
                issue('source-skill-gap', identity, '原文目标须绑定已定位的G249技能ID，不能由名称猜测。')
            elif role_id in source_table['role_ids'] and value is not None:
                expected = values[source_table['role_ids'].index(role_id)]
                if value != expected:
                    issue('source-proficiency-mismatch', identity, '声明为原文参考值但与表5-2不符；裁剪须保留原值并改用tailored_target。', 'error')
            evidence_refs(edge.get('evidence'), identity, 'source evidence')
        elif kind == 'tailored_target':
            missing(attrs, ['tailoring_reason', 'task_refs', 'behavioral_criteria'], identity)
            evidence_refs(edge.get('evidence'), identity, 'target evidence')
        elif kind == 'observed_assessment':
            missing(attrs, ['person_ref', 'task_refs'], identity)
            if state in {'assessed', 'superseded'}:
                missing(attrs, ['assessor', 'observed_on', 'behavioral_evidence'], identity)
                observed_sources = evidence_refs(edge.get('evidence'), identity, 'observed evidence')
                if observed_sources and all(s.get('kind') in {'official', 'local-translation', 'figure-interpretation'} for s in observed_sources):
                    issue('proficiency-observation-source', identity, '参考标准或图表只说明要求，不能证明某个人已表现出该级行为。', 'error')
                observations = attrs.get('behavioral_evidence')
                if isinstance(observations, list):
                    for observation in observations:
                        if not isinstance(observation, dict):
                            issue('proficiency-evidence-gap', identity, '行为证据须为带criterion/demonstrated/evidence的记录。')
                            continue
                        missing(observation, ['criterion'], identity)
                        if observation.get('demonstrated') is not True:
                            issue('proficiency-positive-evidence-gap', identity, '已评级条目须有该级行为的正向证据；不能由不满足更高级推导本级。')
                        evidence_refs(observation.get('evidence'), identity, 'behavioral evidence')

    for entity in entities.values():
        if entity.get('type') != 'skill_development':
            continue
        attrs, identity = entity.get('attributes') or {}, entity['id']
        missing(attrs, ['skill_id', 'scale_id', 'task_refs', 'requirement_refs', 'behavioral_gap',
                        'success_criteria', 'reassessment'], identity, 'development-contract-gap')
        if 'history' not in attrs:
            issue('development-contract-gap', identity, '须显式保留history；首次评价可以为空数组。')
        for field in ('current_proficiency', 'target_proficiency'):
            rating(attrs.get(field), identity, field, attrs.get('scale_id'))
        current_state = attrs.get('current_assessment_state')
        if current_state is not None and (not isinstance(current_state, str) or current_state not in STATES['observed_assessment']):
            issue('proficiency-state', identity, 'current_assessment_state必须使用人员观察状态。', 'error')
        elif current_state in {'unassessed', 'evidence_insufficient'} and attrs.get('current_proficiency') is not None:
            issue('unassessed-proficiency', identity, '未评估或证据不足的当前熟练度须为null，不能赋数字。', 'error')
        if 'current_proficiency' not in attrs:
            issue('development-current-proficiency-gap', identity, '须显式填写current_proficiency；未知应为null并声明current_assessment_state。')
        elif attrs['current_proficiency'] is None and not is_explicit_unknown_current(entity, 'current_proficiency'):
            issue('development-current-proficiency-gap', identity, '当前熟练度为null时须声明unassessed或evidence_insufficient状态。')
        for field in ('task_refs', 'requirement_refs'):
            if field in attrs and (not isinstance(attrs[field], list) or not attrs[field]):
                issue('development-reference-gap', identity, field + ' 须为非空任务/要求ID列表。')
        review = attrs.get('reassessment')
        if isinstance(review, dict):
            missing(review, ['assessor', 'due_on', 'criteria', 'status'], identity, 'development-reassessment-gap')
            if review.get('status') == 'completed':
                observed = review.get('assessment_ref')
                assessment = next((r for r in model.get('relationships', []) if r['id'] == observed), None)
                if not assessment or (assessment.get('attributes') or {}).get('assessment_kind') != 'observed_assessment' or (assessment.get('attributes') or {}).get('assessment_state') != 'assessed':
                    issue('development-reassessment-unproven', identity, '复评完成须引用有实测状态的observed_assessment；培训出席和计划不构成评级提升。', 'error')
                else:
                    a = assessment['attributes']
                    skill = entities.get(assessment.get('source'), {}).get('attributes', {}).get('skill_id')
                    if a.get('scale_id') != attrs.get('scale_id') or skill != attrs.get('skill_id') or a.get('person_ref') != attrs.get('person'):
                        issue('development-assessment-mismatch', identity, '复评必须针对同一人员、技能和量表。', 'error')
                    if not a.get('behavioral_evidence') or not assessment.get('evidence'):
                        issue('development-reassessment-unproven', identity, '完成复评须有实际行为证据；不能仅设置状态。', 'error')
                    elif any(not isinstance(b, dict) or b.get('demonstrated') is not True or not b.get('evidence') for b in a['behavioral_evidence']):
                        issue('development-reassessment-unproven', identity, '复评完成需要本级行为的正向证据；未达到更高级不证明当前级。', 'error')
        elif review is not None:
            issue('development-reassessment-gap', identity, 'reassessment须包含责任人、期限、判据和状态。')
        history = attrs.get('history')
        if history is not None and not isinstance(history, list):
            issue('development-history', identity, '历史评价记录须为数组，保留旧证据而不覆盖。', 'error')
        elif isinstance(history, list):
            for record in history:
                if not isinstance(record, dict):
                    issue('development-history', identity, '历史评价每项须为带时点与证据的记录。', 'error')
                    continue
                missing(record, ['observed_on', 'status', 'rationale'], identity, 'development-history-gap')
                rating(record.get('proficiency'), identity, 'history.proficiency', record.get('scale_id', attrs.get('scale_id')))
                evidence_refs(record.get('evidence'), identity, 'history evidence')
    return issues
