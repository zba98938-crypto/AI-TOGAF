# -*- coding: utf-8 -*-
"""Read generated case artifacts and append evidence-based independent review.

This module does not generate artifacts or change the shared skill/pipeline.
"""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
GEN = HERE / 'generated'


def read(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ev(path, needle):
    text = path.read_text()
    assert needle in text, (str(path), needle)
    return {'path': str(path.relative_to(ROOT)),
            'line': text[:text.index(needle)].count('\n') + 1,
            'quote': needle, 'sha256': sha(path)}


def item(items, identifier):
    return next(x for x in items if x['id'] == identifier)


def augment(result):
    names = ('baseline', 'offline-change', 'shared-object-change')
    models = {n: read(GEN / n / 'model.json') for n in names}
    artifacts = {n: read(GEN / n / 'artifacts/role-assignment.json') for n in names}
    inputs = {n: models[n]['analyses'][0]['inputs'] for n in names}
    coverage = {n: read(GEN / n / 'artifacts/role-assignment.coverage.json') for n in names}
    analyses = {n: read(GEN / n / 'role-assessment.json')['result'] for n in names}
    summary = read(GEN / 'summary.json')
    impact = read(GEN / 'change-impact.json')
    local = read(HERE / 'role-skill-inputs.json')
    changed = models['offline-change']
    entity = {x['id']: x for x in changed['entities']}
    role_path = GEN / 'offline-change/artifacts/role-assignment.json'
    role_md = GEN / 'offline-change/artifacts/role-assignment.md'
    assessment_path = GEN / 'offline-change/role-assessment.json'
    history_path = HERE / 'review-history/before-f08-fix.json'
    cover_path = GEN / 'offline-change/artifacts/role-assignment.coverage.json'
    skill_path = GEN / 'offline-change/artifacts/skill-matrix.md'
    development_path = GEN / 'offline-change/artifacts/development-plan.json'
    roadmap_path = GEN / 'offline-change/artifacts/transition-roadmap.json'
    delivery_path = GEN / 'offline-change/artifacts/delivery-notebook.json'
    source_path = HERE / 'role-skill-inputs.json'
    impact_path = GEN / 'change-impact.json'
    shared_path = GEN / 'shared-object-change/shared-object-projections.json'

    # These assertions establish the particular reviewed snapshot, not business acceptance.
    for name in names:
        expected_subjects = {'ROLE-CHIEF','ROLE-EA','ROLE-SEG','ROLE-SOL','TASK-CH','TASK-EA','TASK-SEG','TASK-SOL','ASSIGN-A','EVIDENCE-A','EVIDENCE-EXPERT'}
        assert set(artifacts[name]['view']['entity_ids']) == expected_subjects
        assert len(artifacts[name]['view']['relationship_ids']) == 7
        assert set(coverage[name]['represented_entity_ids']) == expected_subjects
        assert len(coverage[name]['represented_relationship_ids']) == 7
        assert coverage[name]['errors'] == []
        assert analyses[name]['assignment_reviews'][0]['approval'] == 'not-granted'
        assert analyses[name]['assignment_reviews'][0]['capacity_state'] == 'unresolved'
        main_table = (GEN / name / 'artifacts/role-assignment.md').read_text()
        assert sum(line.startswith('| ROLE-') for line in main_table.splitlines()) == 4
        assert sum(line.startswith('| TASK-') for line in main_table.split('## 任务技能目标')[0].splitlines()) == 4
        assert '| ASSIGN-A / PERSON-A |' in main_table
        assert 'EVIDENCE-A / OBS-A' in main_table and 'EVIDENCE-EXPERT / OBS-EXPERT' in main_table
        assert 'approval not-granted' in main_table
    expert = item(inputs['offline-change']['assessments'], 'OBS-EXPERT')
    assert expert['proficiency'] is None and expert['assessment_state'] == 'evidence_insufficient'
    assert expert['prior_claim']['proficiency'] == 4
    assert analyses['offline-change']['assignment_reviews'][0]['support_reviews'][0]['state'] == 'expert-evidence-unproven'
    assert entity['DEV-A']['attributes']['end'] == '2026-11-30'
    assert entity['WP-OFFLINE']['attributes']['end'] == '2026-12-04'
    assert item(inputs['offline-change']['assignments'], 'ASSIGN-A')['valid_until'] == '2026-11-30'
    assert any(g['id'] == 'GAP-ASSIGNMENT-PERIOD' for g in changed['gaps'])
    expected_impact = {'ROLE-CHIEF', 'ROLE-EA', 'ROLE-SEG', 'ROLE-SOL', 'DEV-A', 'DELIVERY-NOTE', 'SKILL-4'}
    assert expected_impact <= {c['id'] for c in impact['candidates']}
    assert all(c['confirmation'] == '待逐项确认' for c in impact['candidates'])
    assert {c['id'] for c in entity['DELIVERY-NOTE']['attributes']['controls']} == {'CTRL-LOCAL-DURABILITY', 'CTRL-CENTRAL-REPLAY'}
    for n in names:
        for table in ('catalog', 'capability_application_matrix', 'roadmap'):
            entries = [x for x in read(GEN / n / 'shared-object-projections.json')[table] if x['capability_id'] == 'CAP-RESERVE']
            assert entries
            current = item(models[n]['entities'], 'CAP-RESERVE')
            assert all(x['name'] == current['name'] and x['definition'] == current['attributes']['definition'] for x in entries)

    fixes = {
        'F01': ('corrected-to-unknown-evidence-gap-remains',
                '本地修订将当前专家等级保留为null/evidence_insufficient，原4级仅作未证实的历史声明；生成分析为expert-evidence-unproven。未自动降为3级，也未认证专家支持能力。',
                [ev(skill_path, '| OBS-EXPERT |'), ev(assessment_path, '"state": "expert-evidence-unproven"')]),
        'F02': ('corrected-in-local-copy',
                'ROLE-EA与TASK-EA已恢复订单、库存、物流分段责任，门店另列为渠道及运营参与者；生成的角色协作和技能矩阵保持同一ROLE-EA。',
                [ev(source_path, '跨订单、库存、物流分段；门店作为渠道与运营参与者'), ev(skill_path, '| ROLE-EA |')]),
        'F03': ('authority-gap-explicitly-retained',
                '本地委托记录已写明经营负责人只委托分析，具体决定人、库存风险接受者和审批机制待确认；未凭架构委员会名称补造权限。',
                [ev(source_path, '经营负责人委托分析；具体决定人、库存风险接受者及审批机制待确认'), ev(role_md, '具体决定人、库存风险接受者和审批机制仍待确认')]),
        'F04': ('explicit-gap-remains-open',
                'GAP-ASSIGNMENT-PERIOD已进入所有相关生成制品。ASSIGN-A和DEV-A仍到11月30日，离线工作包到12月4日；这并不证明培训必须持续至交付最后一天，但尚无证据证明12月1日至4日的续任、交接、复评或替代覆盖。不得为消除日期差异而自动延长。',
                [ev(development_path, '"end": "2026-11-30"'), ev(roadmap_path, '"end": "2026-12-04"'), ev(delivery_path, '"id": "GAP-ASSIGNMENT-PERIOD"')]),
        'F05': ('scope-corrected-verification-still-pending',
                '本地持久化与中央接收/重放已分为CTRL-LOCAL-DURABILITY、CTRL-CENTRAL-REPLAY，分别指向门店记录与中央恢复边界；控制仍为candidate，责任和故障验证仍未完成。',
                [ev(delivery_path, '"id": "CTRL-LOCAL-DURABILITY"'), ev(delivery_path, '"id": "CTRL-CENTRAL-REPLAY"')]),
        'F06': ('case-dependencies-added-general-capability-unproven',
                '新增CHANGE-DECISIONS、CHANGE-ROLE、CHANGE-DEVELOPMENT及配置关系后，图影响有39个候选，包括4角色、4任务、ASSIGN-A、两份证据状态、技能、DEV-A和DELIVERY-NOTE，全部待逐项确认。它证明本案例显式依赖可被遍历，尚不证明任意自然语言需求能自动发现或更新任务/技能/复评。',
                [ev(impact_path, '"id": "DEV-A"'), ev(impact_path, '"id": "ROLE-CHIEF"'), ev(impact_path, '"id": "DELIVERY-NOTE"')]),
        'F07': ('tailoring-improved-project-adoption-not-business-approval',
                '四个3级目标已分别补投入取舍、跨分段互操作、库存运行数据、接口与恢复细节的采用理由，并说明困难情形仍需支持。adopted仅表示虚构教学场景中的目标状态；真实组织认可、行为证据与可用容量均未证实。',
                [ev(skill_path, '| REQ-SKILL-CH |'), ev(skill_path, '| REQ-SKILL-EA |'), ev(skill_path, '| REQ-SKILL-SEG |'), ev(skill_path, '| REQ-SKILL-SOL |')]),
    }
    for f in result['findings']:
        status, observation, evidence = fixes[f['id']]
        f['generated_resolution'] = {'status': status, 'observation_zh': observation, 'evidence': evidence}

    result['findings'].extend([
        {'id': 'F08', 'priority': 'P1', 'kind': 'artifact-semantic-completeness-gap', 'status': 'fixed-in-local-case-self-checked',
         'title_zh': '角色分配主视图遗漏角色、任务与配置主体，空表仍获零覆盖错误',
         'observation_zh': '修复前，三组role-assignment视图只选择G249-ASSESSMENT-CONTEXT、0关系，Markdown主表为空；coverage仅检查所选上下文仍给零错误。该首次观察已归档，旧输出哈希只代表历史快照。当前修复结果见下方复核，不把旧问题描述当成当前状态。',
         'impact_zh': '目录不能直接回答谁负责什么、需具备什么证据、配置何时有效；选错主体仍可获得形式覆盖通过，不能据此宣称已生成可用的角色配置制品。',
         'recommendation_zh': '保持本地表达契约及缺主体拒绝机制；共享skills尚未采用该修复，不能推广为所有角色制品已解决。真实项目仍需确认任务、目标、能力、容量、期间及授权。',
         'evidence': [ev(history_path, '角色分配主视图遗漏角色、任务与配置主体，空表仍获零覆盖错误')],
         'generated_resolution': {'status':'local-case-fixed-regenerated-self-checked',
            'observation_zh':'本地模型增加4任务、ASSIGN-A和2证据状态对象；主视图现含11个主体与7条关系，主Markdown显式呈现角色/任务/目标/配置/人员证据/发展/11项缺口。SVG和Mermaid可编辑，缺少任何必需主体时本地契约拒绝生成。ASSIGN-A仍至11月30日，12月1日至4日覆盖缺口和未批准状态保留。该复核包含修复作者自检，新增结果需由另一审阅者核验；不授予业务批准。',
            'evidence':[ev(role_md,'| ROLE-CHIEF |'),ev(role_md,'| TASK-SOL |'),ev(role_md,'| ASSIGN-A / PERSON-A |'),ev(role_md,'| EVIDENCE-EXPERT / OBS-EXPERT |'),ev(cover_path,'"semantic_subject_counts": {'),ev(role_md,'期间缺口 GAP-ASSIGNMENT-PERIOD')] }},
        {'id': 'F09', 'priority': 'P2', 'kind': 'shared-object-change-evidence-boundary', 'status': 'projection-consistent-semantic-impact-unreviewed',
         'title_zh': '共享对象变更验证只证明引用同步，未证明业务影响已分析',
         'observation_zh': 'shared-object-change沿用CAP-RESERVE，只变名称和定义；实体、分析输入及上下文副本同步，目录/能力应用矩阵/路线图均引用同一ID。接口契约、风险、工作包、接受标准和批准仍维持原状态；该分支未运行图形渲染。',
         'impact_zh': '名称与定义投影一致有助于避免多份对象分叉，但不能据此判定架构语义变化对接口和运营没有影响。',
         'recommendation_zh': '先判断变更是编辑性重命名还是承诺/业务政策含义变化，再据显式依赖逐项复核接口、风险、工作包、接受条件及决定记录。此案例应标为稳定ID投影验证完成、业务语义影响待审，不把自动同步当业务接受。',
         'evidence': [ev(shared_path, '"capability_id": "CAP-RESERVE"'), ev(shared_path, '"name": "库存预占（共享对象变更验证）"'), ev(shared_path, '"definition": "变更验证：按已确认业务政策协调可售库存；政策本身仍待业务确认"'), ev(GEN / 'summary.json', '"rendered": false')]},
    ])

    gchecks = [
        {'id': 'G01', 'topic': '人员证据、项目目标与配置批准分离', 'status': 'consistent-with-explicit-gaps',
         'observation_zh': '两个人员观察均为证据不足，专家4级历史声明未转为现有能力。ASSIGN-A维持needs-evidence、capacity unresolved、approval not-granted；DEV-A未推断等级提升。',
         'evidence': [ev(assessment_path, '"capacity_state": "unresolved"'), ev(assessment_path, '"approval": "not-granted"'), ev(assessment_path, '"rating_change": "not-inferred"')]},
        {'id': 'G02', 'topic': '离线约束已传播，通用自动分析能力仍有限', 'status': 'case-specific-propagation-observed',
         'observation_zh': '断连版相较修复后基线新增6实体，保留35原实体与在线接口；离线行为进入TASK-SOL、REQ-SKILL-SOL、DEV-A。显式图依赖可达4角色、4任务、配置、证据、技能、发展与决策记录；所有候选待确认。',
         'evidence': [ev(skill_path, '评审断连、重连、幂等重放和库存冲突的恢复设计'), ev(impact_path, '"relationship_path": [\n        "CHANGE-DEVELOPMENT"'), ev(impact_path, '"confirmation": "待逐项确认"')]},
        {'id': 'G03', 'topic': '角色分配主目录已修复为显式主体', 'status': 'local-implementation-self-checked',
         'observation_zh': 'role-collaboration有4角色/5关系，skill-matrix有4角色+4技能/7关系。role-assignment有4角色+4任务+1配置+2证据状态/7关系；主表直接列出任务、目标、容量、期限与缺口，context只保留在分析执行模型。见F08。',
         'evidence': [ev(GEN / 'offline-change/artifacts/role-collaboration.json', '"relationship_ids": ['), ev(role_md, '| ROLE-CHIEF |'), ev(role_md, '| TASK-SOL |'),ev(cover_path,'"semantic_subject_counts": {')]},
        {'id': 'G04', 'topic': '配置期间与发展计划覆盖', 'status': 'explicitly-unresolved',
         'observation_zh': '发展和复评到11月30日，离线工作包到12月4日；日期差异本身不证明培训设计错误，但人员续任/交接与后续复评支持未证实。GAP-ASSIGNMENT-PERIOD已准确保留；见F04。',
         'evidence': [ev(development_path, '"due_on": "2026-11-30"'), ev(roadmap_path, '"end": "2026-12-04"'), ev(delivery_path, '"id": "GAP-ASSIGNMENT-PERIOD"')]},
        {'id': 'G05', 'topic': '共享对象多视图一致性', 'status': 'stable-id-projection-consistent',
         'observation_zh': 'CAP-RESERVE的名称和定义同步至catalog、capability_application_matrix和roadmap，应用仍APP-STOCK，工作包仍WP-ONLINE/WP-OFFLINE；这项检查仅证明稳定ID投影，语义影响未审，见F09。',
         'evidence': [ev(shared_path, '"capability_application_matrix": ['), ev(shared_path, '"roadmap": ['), ev(shared_path, '"work_package_id": "WP-OFFLINE"')]},
        {'id': 'G06', 'topic': '物流与门店/中央数据边界', 'status': 'consistent-with-candidate-design',
         'observation_zh': '生成状态迁移仍由ORDER-CONFIRMED进入ORDER-FULFIL；本地受理不自动承诺。门店持久化与中央去重/对账控制已分开，并保留责任、数据丢失和恢复指标的未知。',
         'evidence': [ev(GEN / 'offline-change/artifacts/order-states.md', '| ORDER-TO-FULFIL |'), ev(delivery_path, '"id": "CTRL-LOCAL-DURABILITY"'), ev(delivery_path, '"id": "CTRL-CENTRAL-REPLAY"')]},
        {'id':'G07','topic':'缺主体反例与生成证据完整性','status':'implementation-self-check-passed',
         'observation_zh':'删除任一必需角色、任务、人员配置、专家证据对象或配置证据关系时，本地表达契约拒绝生成。三分支共242项manifest输出哈希匹配；每份主目录4角色/4任务/1配置/2证据状态，11项分析缺口和未批准状态保持。',
         'evidence':[ev(GEN/'assignment-verification.json','"status": "passed"'),ev(GEN/'assignment-verification.json','"incomplete_views_rejected": [')]},
    ]
    snapshot_paths = [HERE / 'role-skill-inputs.json', HERE / 'run.py', HERE / 'base_build.py', HERE / 'assignment_expression.py', HERE / 'verify_assignment.py', GEN / 'assignment-verification.json', GEN / 'summary.json', GEN / 'execution-provenance.json', impact_path]
    snapshot_paths += [GEN / n / f for n in names for f in ('model.json', 'role-assessment.json', 'shared-object-projections.json', 'artifacts/role-assignment.json', 'artifacts/role-assignment.coverage.json', 'artifacts/role-assignment.md')]
    result['scope_zh'] = '先独立审阅三份只读原教学材料和已生成制品。随后在togaf-standard-10th-ai本地案例内修复F08、重跑三组生成并自检；未修改skills目录。原独立观察与修复作者自检分开记录，schema/表达覆盖通过不作为业务内容充分性验收。'
    result['overall_status'] = 'local-artifact-fixed-business-evidence-gaps-remain'
    result['generated_artifact_review'] = {
        'status': 'local-F08-fixed-self-checked-with-business-evidence-gaps',
        'post_fix_review_kind': 'implementation-self-check-independent-followup-required',
        'path': str(GEN.relative_to(ROOT)),
        'generation_summary': summary,
        'source_snapshots': [{'path': str(p.relative_to(ROOT)), 'sha256': sha(p)} for p in snapshot_paths],
        'checks': gchecks,
        'role_assignment_observation': {n: {'selected_entity_ids': artifacts[n]['view']['entity_ids'], 'selected_relationship_ids': artifacts[n]['view']['relationship_ids'], 'represented_entity_ids': coverage[n]['represented_entity_ids'], 'coverage_errors': coverage[n]['errors'], 'coverage_warnings': coverage[n]['warnings'], 'main_role_table_rows': 4,'main_task_table_rows':4,'assignment_subjects':1,'evidence_subjects':2} for n in names},
        'impact_candidate_count': len(impact['candidates']),
        'impact_candidate_ids': [x['id'] for x in impact['candidates']],
        'limits_zh': '已复核保存的模型、JSON、Markdown、覆盖登记、来源哈希和变更投影；F08本地修复后的主表、PNG与可编辑SVG/Mermaid由修复作者自检，另一审阅者复核待完成。未逐张目视验收其它视图，也未执行shared-object-change PNG渲染。角色分配主体缺失已修复，不等于真实任务、人员行为、容量或组织批准获证实；共享skills尚未采纳本地适配。',
    }
    return result
