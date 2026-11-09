"""Evidence contracts for G249 task, role, competence and assignment reasoning.

G249 supplies human-role guidance and reference proficiency levels. The record
schema, workflow and checks here are explicit project conventions, not TOGAF
mandates. This reviewer never infers a person's rating or grants authorization.
"""
from datetime import date
import json
from pathlib import Path

from numeric_contracts import finite_number, stable_id

ROOT = Path(__file__).resolve().parents[1]
OFFICIAL_SCALE = 'G249-table5-1'
METHOD_ID = 'architecture-role-skill-assessment'


def skill_routes():
    return json.loads((ROOT / 'references/g249/skill-task-map.json').read_text())


def _require(condition, code, identity, message):
    if not condition:
        raise ValueError(f'{code} [{identity}]: {message}')


class Review:
    def __init__(self, data):
        self.data, self.gaps = data, []
        self.sources = set(self.ids(data.get('source_ids', []), 'source_ids'))
        self.mapping = {r['skill_id']: r for r in skill_routes()['skills']}
        self.as_of = self.day(data.get('as_of'), 'as_of')
        self.roles = self.records('roles')
        self.tasks = self.records('tasks')
        self.requirements = self.records('requirements')
        self.assessments = self.records('assessments')
        self.assignments = self.records('assignments')
        self.development = self.records('development')
        self.scales = self.records('scales')
        self.interpretations = self.records('interpretations')
        self.required(data, ['scope', 'as_of'], 'context')

    def gap(self, identity, reason, action):
        item = {'id': identity, 'reason': reason, 'action': action}
        self.gaps.append(item)

    def required(self, record, fields, identity):
        for field in fields:
            if record.get(field) in (None, '', [], {}):
                self.gap(identity + ':' + field, 'missing-input', '补充 ' + field + ' 的事实、责任或规则；保留草稿。')

    def ids(self, values, identity):
        _require(isinstance(values, list), 'G249-SHAPE', identity, 'Expected a list of IDs')
        for value in values:
            stable_id(value, identity)
        _require(len(values) == len(set(values)), 'G249-ID', identity, 'Duplicate reference')
        return values

    def records(self, field):
        records = self.data.get(field, [])
        _require(isinstance(records, list), 'G249-SHAPE', field, 'Expected a list of records')
        result = {}
        for row in records:
            _require(isinstance(row, dict), 'G249-SHAPE', field, 'Expected an object')
            identity = row.get('id')
            stable_id(identity, field + '.id')
            _require(identity not in result, 'G249-ID', identity, 'Duplicate record ID')
            result[identity] = row
        return result

    def refs(self, row, field, known, required=True):
        values = self.ids(row.get(field, []), row['id'] + ':' + field)
        for value in values:
            _require(value in known, 'G249-REF', row['id'], f'{field} references unknown ID: {value}')
        if required and not values:
            self.gap(row['id'] + ':' + field, 'missing-reference', '补充可追溯的 ' + field)
        return values

    def evidence(self, row, identity=None):
        identity = identity or row.get('id', 'evidence')
        refs = self.ids(row.get('evidence', []), identity + ':evidence')
        _require(set(refs) <= self.sources, 'G249-EVIDENCE', identity, 'Evidence absent from source_ids')
        if not refs:
            self.gap(identity + ':evidence', 'missing-evidence', '提供可定位的原始材料；不从头衔、证书或培训出席推定能力。')
        return bool(refs)

    def day(self, value, identity):
        if value in (None, ''):
            return None
        _require(isinstance(value, str), 'G249-DATE', identity, 'Expected ISO date')
        try:
            return date.fromisoformat(value)
        except ValueError as exc:
            raise ValueError(f'G249-DATE [{identity}]: Invalid ISO date') from exc

    def period(self, row):
        self.required(row, ['valid_from', 'valid_until'], row['id'])
        start, end = (self.day(row.get(f), row['id'] + ':' + f) for f in ['valid_from', 'valid_until'])
        if start and end:
            _require(start <= end, 'G249-DATE', row['id'], 'valid_until precedes valid_from')
        if self.as_of and ((start and self.as_of < start) or (end and self.as_of > end)):
            self.gap(row['id'] + ':period', 'outside-validity-period', '本次时点不在授权/分配有效期间，重新确认。')

    def skill(self, row):
        sid = row.get('skill_id')
        if sid is None:
            self.gap(row['id'] + ':skill_id', 'missing-input', '明确对应的 G249 技能 ID。')
        else:
            _require(sid in self.mapping, 'G249-SKILL', row['id'], 'Unknown G249 skill ID')
        return sid

    def proficiency(self, row):
        value = row.get('proficiency')
        if value is not None:
            _require(type(value) is int and 1 <= value <= 4, 'G249-LEVEL', row['id'], 'Proficiency must be an integer 1..4 or null')
        sid = row.get('scale_id')
        if sid is None:
            self.gap(row['id'] + ':scale_id', 'missing-scale', '声明 G249-table5-1 或带版本的项目量表；相同数字不表示同一锚点。')
        elif sid != OFFICIAL_SCALE:
            _require(isinstance(sid, str) and sid.startswith('project-') and '-v' in sid, 'G249-SCALE', row['id'], 'Custom scale requires project-<name>-v<version>')
            if sid not in self.scales:
                self.gap(row['id'] + ':scale_id', 'missing-scale-definition', '提供项目四级行为锚点及采用证据。')
            else:
                scale = self.scales[sid]
                anchors = scale.get('anchors', [])
                _require(isinstance(anchors, list) and len(anchors) == 4 and all(isinstance(a, dict) for a in anchors)
                         and {a.get('value') for a in anchors} == {1, 2, 3, 4}
                         and all(type(a.get('value')) is int and a.get('meaning') for a in anchors),
                         'G249-SCALE', sid, 'Custom scale requires four explicit {value,meaning} anchors')
                self.evidence(scale)
        elif sid in self.scales:
            official = json.loads((ROOT / 'references/source-tables/g249-skill-proficiency.json').read_text())
            _require(self.scales[sid].get('anchors') == official['anchors'], 'G249-SCALE', row['id'], 'Official scale cannot be redefined under its source ID')
        return value

    def mandate_review(self):
        mandate = self.data.get('mandate', {})
        _require(isinstance(mandate, dict), 'G249-SHAPE', 'mandate', 'Expected mandate object')
        self.required(mandate, ['id', 'scope', 'decision_owner'], 'mandate')
        if mandate.get('id'):
            stable_id(mandate['id'], 'mandate.id')
        self.evidence(mandate, 'mandate')
        return mandate

    def role_reviews(self):
        result = {}
        for row in self.roles.values():
            start = len(self.gaps)
            self.required(row, ['name', 'tier', 'scope'], row['id'])
            if row.get('tier') is not None:
                _require(row['tier'] in {'chief', 'enterprise', 'segment', 'solution', 'specialist'},
                         'G249-ROLE', row['id'], 'Unknown role category; categories are not personnel ranks')
            self.evidence(row)
            result[row['id']] = {'id': row['id'], 'state': 'needs-input' if len(self.gaps) > start else 'role-scope-recorded'}
        return result

    def task_reviews(self):
        result = []
        model_views = self.data.get('model_views')
        if model_views is not None:
            _require(isinstance(model_views, list) and all(isinstance(v, dict) for v in model_views),
                     'G249-SHAPE', 'model_views', 'Expected a list of selected model view snapshots')
        registry = json.loads((ROOT / 'capabilities.json').read_text())
        method_ids = {r['id'] for r in registry['analysis_methods']}
        artifact_ids = {r['id'] for r in registry['work_products']}
        artifact_ids |= {r['id'] for r in json.loads((ROOT / 'artifacts.json').read_text())['artifacts']}
        for task in self.tasks.values():
            start = len(self.gaps)
            self.required(task, ['scope', 'decision', 'outcome'], task['id'])
            self.evidence(task)
            self.refs(task, 'role_refs', self.roles)
            skills = self.refs(task, 'required_skill_ids', self.mapping)
            self.refs(task, 'method_ids', method_ids)
            intended_artifacts = self.refs(task, 'artifact_ids', artifact_ids)
            if model_views is not None:
                for artifact in intended_artifacts:
                    if not any(v.get('artifact_id') == artifact for v in model_views):
                        self.gap(task['id'] + ':' + artifact + ':view', 'task-artifact-view-missing',
                                 '任务声明的制品尚未选入当前模型视图；补视图或由责任方明确调整任务输出，不能用制品注册存在代替实际选择。')
            elif self.data.get('model_binding'):
                self.gap(task['id'] + ':model_views', 'artifact-view-selection-unverified',
                         '补当前模型中任务所需制品的视图快照，才能核对任务输出是否实际选入。')
            routes = []
            for sid in skills:
                route = self.mapping[sid]
                interpretation = next((r for r in self.interpretations.values() if r.get('skill_id') == sid), None)
                if route['definition_status'] == 'source-name-unresolved':
                    if not interpretation:
                        self.gap(task['id'] + ':' + sid, 'source-definition-unresolved', '保留原名；补专业定义及项目采用证据，不自动解释为并发控制等特定技术。')
                    else:
                        self.required(interpretation, ['definition', 'adopted_by'], interpretation['id'])
                        self.evidence(interpretation)
                requirements = [r['id'] for r in self.requirements.values()
                                if r.get('task_ref') == task['id'] and r.get('skill_id') == sid]
                if not requirements:
                    self.gap(task['id'] + ':' + sid + ':target', 'missing-task-skill-requirement', '从本任务结果推导角色要求并记录裁剪依据。')
                routes.append({'skill_id': sid, 'requirement_refs': requirements,
                               'suggested_method_ids': route['method_ids'], 'suggested_artifact_ids': route['artifact_ids'],
                               'definition_status': route['definition_status'], 'mapping_origin': 'project-derived-routing'})
            result.append({'id': task['id'], 'routes': routes, 'state': 'needs-input' if len(self.gaps) > start else 'task-demands-recorded'})
        if not self.tasks:
            self.gap('tasks', 'missing-work-demand', '先识别需完成的架构任务和决策；不能只凭岗位名制定目标。')
        return result

    def requirement_reviews(self):
        result = {}
        for row in self.requirements.values():
            start = len(self.gaps)
            sid = self.skill(row)
            self.proficiency(row)
            for field, known in [('task_ref', self.tasks), ('role_ref', self.roles)]:
                if row.get(field) is not None:
                    _require(row[field] in known, 'G249-REF', row['id'], 'Unknown ' + field)
                else:
                    self.required(row, [field], row['id'])
            task = self.tasks.get(row.get('task_ref'), {})
            if task and sid:
                _require(sid in task.get('required_skill_ids', []), 'G249-DEMAND', row['id'], 'Requirement skill absent from task demands')
                _require(row.get('role_ref') in task.get('role_refs', []), 'G249-DEMAND', row['id'], 'Requirement role absent from task')
            kind, state = row.get('assessment_kind'), row.get('assessment_state')
            if kind is not None:
                _require(kind in {'source_reference_target', 'tailored_target'}, 'G249-KIND', row['id'], 'Requirements cannot contain observed personal ratings')
            if kind == 'source_reference_target':
                _require(state in (None, 'reference'), 'G249-STATE', row['id'], 'Source target state must be reference')
                source_role = row.get('reference_role_ref')
                if not source_role:
                    self.gap(row['id'] + ':reference_role_ref', 'missing-reference-cell', '明确来源角色列，不能从本地角色头衔推定原表目标。')
                elif sid:
                    values = self.mapping[sid]['official']['reference_proficiencies']
                    _require(source_role in values, 'G249-REF', row['id'], 'Unknown source role column')
                    _require(row.get('proficiency') == values[source_role] and row.get('scale_id') == OFFICIAL_SCALE,
                             'G249-SOURCE-TARGET', row['id'], 'Source reference differs from the official matrix cell/scale')
                self.gap(row['id'] + ':adoption', 'reference-not-adopted', '参考矩阵不是已采用的项目目标，需结合任务裁剪。')
            elif kind == 'tailored_target':
                _require(state in (None, 'proposed', 'adopted'), 'G249-STATE', row['id'], 'Unknown target state')
                if state != 'adopted':
                    self.gap(row['id'] + ':adoption', 'target-not-adopted', '明确目标采用责任与证据后再判断人员配置。')
                self.required(row, ['tailoring_reason'], row['id'])
            self.required(row, ['assessment_kind', 'assessment_state', 'proficiency', 'behavioral_criteria'], row['id'])
            criteria = self.ids(row.get('behavioral_criteria', []), row['id'] + ':behavioral_criteria')
            self.evidence(row)
            result[row['id']] = {'id': row['id'], 'task_ref': row.get('task_ref'), 'role_ref': row.get('role_ref'),
                                 'skill_id': sid, 'proficiency': row.get('proficiency'), 'scale_id': row.get('scale_id'),
                                 'behavioral_criteria': criteria, 'state': 'needs-input' if len(self.gaps) > start else 'adopted-requirement-recorded'}
        return result

    def assessment_reviews(self):
        result = {}
        for row in self.assessments.values():
            start = len(self.gaps)
            sid, level = self.skill(row), self.proficiency(row)
            if row.get('assessment_kind') is not None:
                _require(row['assessment_kind'] == 'observed_assessment', 'G249-KIND', row['id'], 'Source targets are not observations about people')
            state = row.get('assessment_state')
            _require(state in (None, 'unassessed', 'evidence_insufficient', 'assessed', 'superseded'), 'G249-STATE', row['id'], 'Unknown observed assessment state')
            if state in ('unassessed', 'evidence_insufficient'):
                _require(level is None, 'G249-STATE', row['id'], 'Unassessed/insufficient evidence requires null proficiency')
            self.required(row, ['assessment_kind', 'assessment_state', 'person_ref', 'observed_on'], row['id'])
            self.refs(row, 'task_refs', self.tasks)
            observed = self.day(row.get('observed_on'), row['id'] + ':observed_on')
            if observed and self.as_of:
                _require(observed <= self.as_of, 'G249-DATE', row['id'], 'Observation is after analysis as_of')
            if state in ('assessed', 'superseded'):
                self.required(row, ['proficiency', 'behavioral_evidence', 'assessor'], row['id'])
            self.evidence(row)
            behaviors = row.get('behavioral_evidence', [])
            _require(isinstance(behaviors, list), 'G249-SHAPE', row['id'], 'behavioral_evidence must be a list')
            demonstrated = []
            seen = set()
            for index, behavior in enumerate(behaviors):
                identity = row['id'] + ':behavior:' + str(index)
                _require(isinstance(behavior, dict), 'G249-SHAPE', identity, 'Expected behavior object')
                self.required(behavior, ['criterion'], identity)
                criterion = behavior.get('criterion')
                _require(criterion not in seen, 'G249-ID', identity, 'Duplicate behavioral criterion')
                seen.add(criterion)
                _require(type(behavior.get('demonstrated')) is bool, 'G249-BEHAVIOR', identity, 'demonstrated must be explicit boolean')
                has_evidence = self.evidence(behavior, identity)
                evidence_kind = behavior.get('evidence_kind')
                if evidence_kind in {'training-attendance', 'course-completion', 'self-declaration'}:
                    self.gap(identity, 'behavior-not-demonstrated-by-learning-record', '培训出席、课程完成或自述不能单独证明已达到任务行为；补实作及专业评审。')
                elif has_evidence and behavior['demonstrated']:
                    demonstrated.append(criterion)
            if state != 'assessed':
                self.gap(row['id'] + ':assessment', 'competence-not-currently-evidenced', '保留未评估、证据不足或历史状态；不赋最低级也不自动升级。')
            result[row['id']] = {'id': row['id'], 'skill_id': sid, 'person_ref': row.get('person_ref'),
                                 'demonstrated_criteria': demonstrated,
                                 'state': 'evidence-contract-complete' if len(self.gaps) == start else 'needs-evidence'}
        return result

    def assignment_reviews(self, mandate, targets, observations):
        result = []
        for row in self.assignments.values():
            start = len(self.gaps)
            self.required(row, ['person_ref', 'role_ref', 'mandate_ref', 'authority'], row['id'])
            if row.get('role_ref') is not None:
                _require(row['role_ref'] in self.roles, 'G249-REF', row['id'], 'Unknown assignment role')
            if row.get('mandate_ref'):
                _require(row['mandate_ref'] == mandate.get('id'), 'G249-AUTHORITY', row['id'], 'Assignment mandate does not match declared mandate')
            self.period(row)
            self.evidence(row)
            tasks = self.refs(row, 'task_refs', self.tasks)
            period_state = 'covered-for-declared-task-periods'
            assignment_start = self.day(row.get('valid_from'), row['id'] + ':valid_from')
            assignment_end = self.day(row.get('valid_until'), row['id'] + ':valid_until')
            for tid in tasks:
                period = self.tasks[tid].get('work_period')
                if not isinstance(period, dict) or not period.get('start') or not period.get('end'):
                    if period_state != 'not-covered':
                        period_state = 'unresolved'
                    self.gap(row['id'] + ':' + tid + ':work_period', 'task-period-unresolved', '补任务工作期间；当前时点有效不证明完整任务期均有人员覆盖。')
                    continue
                task_start = self.day(period['start'], tid + ':work_period.start')
                task_end = self.day(period['end'], tid + ':work_period.end')
                _require(task_start <= task_end, 'G249-DATE', tid, 'Task work period end precedes start')
                if not assignment_start or not assignment_end:
                    if period_state != 'not-covered':
                        period_state = 'unresolved'
                elif assignment_start > task_start or assignment_end < task_end:
                    period_state = 'not-covered'
                    self.gap(row['id'] + ':' + tid + ':coverage', 'assignment-period-not-covered', '人员配置期间没有完整覆盖任务；明确续任、交接或替代，不能自动延长。')
            requirements = self.refs(row, 'requirement_refs', targets)
            assessments = self.refs(row, 'assessment_refs', observations)
            expected = {r['id'] for r in self.requirements.values() if r.get('task_ref') in tasks and r.get('role_ref') == row.get('role_ref')}
            for missing in sorted(expected - set(requirements)):
                self.gap(row['id'] + ':' + missing, 'assignment-requirement-omitted', '分配评审必须覆盖该角色在所选任务中的全部已声明要求。')
            checks, deficiency = [], False
            for rid in requirements:
                target = self.requirements[rid]
                _require(target.get('task_ref') in tasks and target.get('role_ref') == row.get('role_ref'), 'G249-ASSIGNMENT', row['id'], 'Requirement is outside assigned task/role')
                candidates = [self.assessments[aid] for aid in assessments if self.assessments[aid].get('skill_id') == target.get('skill_id')]
                _require(len(candidates) <= 1, 'G249-AMBIGUOUS', row['id'], 'Choose one current assessment per skill explicitly')
                status, missing = 'unproven', list(target.get('behavioral_criteria', []))
                if candidates:
                    observation = candidates[0]
                    _require(observation.get('person_ref') == row.get('person_ref'), 'G249-ASSIGNMENT', row['id'], 'Assessment belongs to another person')
                    if target.get('task_ref') not in observation.get('task_refs', []):
                        self.gap(row['id'] + ':' + rid + ':scope', 'assessment-scope-unconfirmed', '确认历史能力证据适用于当前任务，不能跨语境直接沿用。')
                    elif target.get('scale_id') != observation.get('scale_id'):
                        self.gap(row['id'] + ':' + rid + ':scale', 'incomparable-scales', '不同量表不得直接比较数字，需在目标量表下重新评审。')
                    elif targets[rid]['state'] == 'adopted-requirement-recorded' and observations[observation['id']]['state'] == 'evidence-contract-complete':
                        missing = sorted(set(target.get('behavioral_criteria', [])) - set(observations[observation['id']]['demonstrated_criteria']))
                        # Ordinal comparison only; no averaging or size-of-gap arithmetic.
                        if observation['proficiency'] < target['proficiency'] or missing:
                            status, deficiency = 'development-needed', True
                            self.gap(row['id'] + ':' + rid, 'behavioral-requirement-gap', '补足缺失行为/已记录等级要求，并设计有产出证据的实践与复评。')
                        else:
                            status = 'evidenced-for-declared-task'
                if status == 'unproven':
                    self.gap(row['id'] + ':' + rid, 'assignment-competence-unproven', '补完整、当前、同量表且适用本任务的能力证据。')
                checks.append({'requirement_ref': rid, 'state': status, 'missing_behavioral_criteria': missing})
            capacity = 'unresolved'
            available = row.get('available_hours')
            if available is not None:
                finite_number(available, row['id'] + ':available_hours', minimum=0)
            workload = [self.tasks[t].get('workload_hours') for t in tasks]
            for t, value in zip(tasks, workload):
                if value is not None:
                    finite_number(value, t + ':workload_hours', minimum=0)
            if available is not None and tasks and all(value is not None for value in workload):
                capacity = 'sufficient-for-declared-workload' if available >= sum(workload) else 'insufficient'
                if capacity == 'insufficient':
                    self.gap(row['id'] + ':capacity', 'capacity-insufficient', '增加投入或调整任务范围；容量不足不降低技能等级。')
            else:
                self.gap(row['id'] + ':capacity', 'capacity-unresolved', '补同一分配期间的可用小时与任务工作量，未知不等于不足或足够。')
            support = row.get('support')
            support_checks = []
            if support:
                _require(isinstance(support, dict), 'G249-SHAPE', row['id'], 'support must be an object')
                self.required(support, ['provider', 'mode', 'requirement_refs', 'assessment_refs', 'available_hours'], row['id'] + ':support')
                self.evidence(support, row['id'] + ':support')
                support_record = {**support, 'id': row['id'] + ':support'}
                sr = self.refs(support_record, 'requirement_refs', targets)
                sa = self.refs(support_record, 'assessment_refs', observations)
                if support.get('available_hours') is not None:
                    finite_number(support['available_hours'], support_record['id'] + ':available_hours', minimum=0)
                for rid in sr:
                    _require(rid in requirements, 'G249-SUPPORT', row['id'], 'Support requirement is outside assignment')
                    target = self.requirements[rid]
                    matched = [self.assessments[aid] for aid in sa if self.assessments[aid].get('skill_id') == target.get('skill_id')]
                    _require(len(matched) <= 1, 'G249-SUPPORT', row['id'], 'Select one current expert assessment per skill')
                    proven = False
                    if matched:
                        expert = matched[0]
                        _require(expert.get('person_ref') == support.get('provider'), 'G249-SUPPORT', row['id'], 'Support evidence belongs to another provider')
                        proven = (observations[expert['id']]['state'] == 'evidence-contract-complete'
                                  and expert.get('scale_id') == target.get('scale_id')
                                  and target.get('proficiency') is not None and expert.get('proficiency') is not None
                                  and expert['proficiency'] >= target['proficiency']
                                  and target.get('task_ref') in expert.get('task_refs', [])
                                  and set(target.get('behavioral_criteria', [])) <= set(observations[expert['id']]['demonstrated_criteria']))
                    support_checks.append({'requirement_ref': rid, 'state': 'expert-evidence-recorded' if proven else 'expert-evidence-unproven'})
                    if not proven:
                        self.gap(support_record['id'] + ':' + rid, 'support-competence-unproven', '补本任务适用的专家能力证据；专家头衔不是行为证据。')
                self.gap(row['id'] + ':support', 'support-requires-owner-review', '核查专家/导师能力、容量、协作方式和责任；支持方案不自动提高被支持人员等级。')
            state = 'development-needed' if deficiency else 'needs-evidence' if len(self.gaps) > start else 'ready-for-owner-review'
            result.append({'id': row['id'], 'state': state, 'requirements': checks, 'capacity_state': capacity, 'period_state': period_state,
                           'approval': 'not-granted', 'support': support, 'support_reviews': support_checks})
        return result

    def development_reviews(self):
        result = []
        for row in self.development.values():
            start = len(self.gaps)
            self.skill(row)
            self.required(row, ['person', 'role', 'skill_id', 'scale_id', 'target_proficiency', 'behavioral_gap', 'action', 'owner', 'due', 'success_criteria'], row['id'])
            task_refs = self.refs(row, 'task_refs', self.tasks)
            refs = self.refs(row, 'requirement_refs', self.requirements)
            success = set(self.ids(row.get('success_criteria', []), row['id'] + ':success_criteria'))
            reassessment = row.get('reassessment', {})
            _require(isinstance(reassessment, dict), 'G249-SHAPE', row['id'], 'reassessment must be object')
            review_criteria = set(self.ids(reassessment.get('criteria', []), row['id'] + ':reassessment.criteria'))
            versions = row.get('requirement_versions', {})
            _require(isinstance(versions, dict), 'G249-SHAPE', row['id'], 'requirement_versions must map linked requirement IDs to reviewed versions')
            _require(set(versions) <= set(refs), 'G249-REF', row['id'], 'Version references must belong to linked requirements')
            for rid in refs:
                target = self.requirements[rid]
                _require(target.get('skill_id') == row.get('skill_id') and target.get('role_ref') == row.get('role'), 'G249-DEVELOPMENT', row['id'], 'Development does not match requirement skill/role')
                _require(target.get('task_ref') in task_refs, 'G249-DEVELOPMENT', row['id'], 'Development task scope does not include requirement')
                if row.get('target_proficiency') is not None:
                    _require(row['target_proficiency'] == target.get('proficiency') and row.get('scale_id') == target.get('scale_id'), 'G249-DEVELOPMENT', row['id'], 'Development target differs from adopted requirement')
                current_criteria = set(self.ids(target.get('behavioral_criteria', []), rid + ':behavioral_criteria'))
                for field, planned in [('success_criteria', success), ('reassessment.criteria', review_criteria)]:
                    missing = sorted(current_criteria - planned)
                    if missing:
                        self.gap(row['id'] + ':' + rid + ':' + field, 'development-criteria-outdated',
                                 '发展计划未显式覆盖当前要求的行为判据：' + '；'.join(missing)
                                 + '。由责任方复核并更新计划；不推断不同文字等价，不自动改写。')
                version = target.get('version', target.get('requirement_version'))
                if version is not None and versions.get(rid) != version:
                    self.gap(row['id'] + ':' + rid + ':version', 'development-requirement-version-unconfirmed',
                             '要求版本已提供但发展计划未确认相同版本；复核要求与计划后更新 requirement_versions。')
            for key in ['current_proficiency', 'target_proficiency']:
                value = row.get(key)
                if value is not None:
                    _require(type(value) is int and 1 <= value <= 4, 'G249-LEVEL', row['id'], key + ' must be 1..4 or null')
            self.day(row.get('due'), row['id'] + ':due')
            self.evidence(row)
            self.required(reassessment, ['assessor', 'due_on', 'criteria', 'status'], row['id'] + ':reassessment')
            self.day(reassessment.get('due_on'), row['id'] + ':reassessment.due_on')
            state = reassessment.get('status', 'planned')
            _require(state in ('planned', 'completed'), 'G249-STATE', row['id'], 'Unknown reassessment status')
            if state == 'completed':
                self.evidence(reassessment, row['id'] + ':reassessment')
                ref = reassessment.get('assessment_ref')
                if not ref:
                    self.gap(row['id'] + ':reassessment.assessment_ref', 'missing-reassessment', '完成发展须关联新的行为评审；培训完成不能替代能力证据。')
                else:
                    _require(ref in self.assessments, 'G249-REF', row['id'], 'Unknown reassessment')
                    observed = self.assessments[ref]
                    _require(observed.get('person_ref') == row.get('person') and observed.get('skill_id') == row.get('skill_id'), 'G249-DEVELOPMENT', row['id'], 'Reassessment person/skill differs')
                    demonstrated = {b.get('criterion') for b in observed.get('behavioral_evidence', []) if b.get('demonstrated') is True and b.get('evidence')}
                    proven = (observed.get('assessment_state') == 'assessed' and observed.get('scale_id') == row.get('scale_id')
                              and observed.get('proficiency') is not None and row.get('target_proficiency') is not None
                              and observed['proficiency'] >= row['target_proficiency']
                              and set(row.get('success_criteria', [])) <= demonstrated
                              and set(reassessment.get('criteria', [])) <= demonstrated
                              and self.assessment_result[ref]['state'] == 'evidence-contract-complete')
                    if not proven:
                        self.gap(row['id'] + ':outcome', 'development-outcome-unproven', '完成活动不表示达到目标；在目标量表下复核新证据。')
                if not row.get('history'):
                    self.gap(row['id'] + ':history', 'missing-assessment-history', '保留原评级、证据与日期，不覆盖旧记录。')
            history = row.get('history', [])
            _require(isinstance(history, list), 'G249-SHAPE', row['id'], 'history must be a list')
            for index, entry in enumerate(history):
                _require(isinstance(entry, dict), 'G249-SHAPE', row['id'], 'history record must be object')
                self.evidence(entry, row['id'] + ':history:' + str(index))
            result.append({'id': row['id'], 'state': 'needs-input' if len(self.gaps) > start else 'reassessment-recorded' if state == 'completed' else 'development-planned',
                           'rating_change': 'not-inferred'})
        return result

    def run(self):
        mandate = self.mandate_review()
        role_rows = self.role_reviews()
        task_rows = self.task_reviews()
        targets = self.requirement_reviews()
        observations = self.assessment_reviews()
        self.assessment_result = observations
        assignments = self.assignment_reviews(mandate, targets, observations)
        for task in self.tasks.values():
            for role in task.get('role_refs', []):
                if not any(task['id'] in a.get('task_refs', []) and a.get('role_ref') == role for a in self.assignments.values()):
                    self.gap(task['id'] + ':' + role + ':assignment', 'task-role-unassigned', '角色需求已有记录，具体人员、有效期和配置方案仍待明确。')
        development = self.development_reviews()
        # Upstream gaps must prevent an apparently ready downstream assignment.
        upstream = [g for g in self.gaps if g['id'].startswith(('mandate', 'context', 'tasks'))]
        task_states = {r['id']: r['state'] for r in task_rows}
        for row in assignments:
            declared_tasks = self.assignments[row['id']].get('task_refs', [])
            role_state = role_rows.get(self.assignments[row['id']].get('role_ref'), {}).get('state')
            if (upstream or role_state != 'role-scope-recorded' or any(task_states[t] == 'needs-input' for t in declared_tasks)) and row['state'] == 'ready-for-owner-review':
                row['state'] = 'needs-evidence'
        return {'schema_version': 'g249-reasoning/1', 'rule_origin': 'project-operational-contract-derived-from-G249',
                'task_routes': task_rows, 'role_reviews': list(role_rows.values()), 'requirement_reviews': list(targets.values()),
                'assessment_reviews': list(observations.values()), 'assignment_reviews': assignments,
                'development_reviews': development, 'gaps': self.gaps,
                'notice': '只核验已声明的任务、规则、证据与追溯；不代评行为真假，不自动认证、批准分配或实施晋升，不将序数相减/平均。'}


def review_role_skills(data):
    _require(isinstance(data, dict), 'G249-SHAPE', 'inputs', 'Expected an input object')
    return Review(data).run()
