"""Explicitly authored scenario additions; never imports a profile example factory."""
from pathlib import Path
import copy
import hashlib
import json

HERE = Path(__file__).resolve().parent
BASE = HERE.parent


def save(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def authored_material():
    m = json.loads((BASE / 'adm-delivery-materials.json').read_text())
    m['notice'] += ' 本轮新增 R1–R4 关系投影及 V2 候选边界见 full_closure/business-supplement.md；reviewer-turned-remediator 不自授独立接受。'
    m['supplement'] = {'path': 'business-supplement.md', 'sha256': hashlib.sha256((HERE / 'business-supplement.md').read_bytes()).hexdigest(),
                       'author_role': 'reviewer-turned-remediator', 'independent_review': 'pending'}
    objects = {x['id']: x for x in m['objects']}

    def obj(identity, typ, name, phase, **attributes):
        record = {'id': identity, 'type': typ, 'name': name, 'source_phase': phase, 'attributes': attributes}
        if identity in objects:
            objects[identity].update(record)
        else:
            m['objects'].append(record)
            objects[identity] = record

    roles = [('', '业务政策所有者', '政策与风险决定', 'Preliminary'),
             ('-BOARD', '情景委员会', '约束及实验例外治理', 'Preliminary'),
             ('-ARCH', '情景架构团队', '跨域设计与证据维护', 'Preliminary'),
             ('-DELIVERY', '情景交付负责人', '隔离实验交付和测试', 'G'),
             ('-OPS', '情景运营负责人', '异常接管和回退核对', 'G')]
    for suffix, actor, role, phase in roles:
        obj('OM-ACTOR'+suffix, 'actor', actor, phase, boundary='设计与隔离实验职责；真实任命未知', owner='情景发起人')
        obj('OM-ROLE'+suffix, 'role', role, phase, responsibility=role, authority='原材料给定情景职责；无真实授权', skill='依据本任务职责；真实人员资格另审')
    obj('OM-ACTOR-STORE', 'actor', '情景门店运营参与者', 'B', boundary='门店断连受理与人工异常', owner='情景门店运营责任方')
    obj('OM-DATA', 'data_entity', '订单身份与状态', 'C', definition='order_id关联本地待确认副本与中央确认记录', owner='情景数据责任方', classification='真实分级未知', purpose='追踪受理、确认与异常')
    for suffix, name, definition in [('EVENT', '受理事件', 'event_id标识事件，accepted_at及policy_version不可缺少'), ('RESERVATION', '中央预占凭证', 'reservation_id仅由中央原子预占成功产生'), ('POLICY', '版本化受理政策', 'policy_version标识受理时采用的候选限制')]:
        obj('OM-DATA-'+suffix, 'data_entity', name, 'C', definition=definition, owner='情景数据责任方', classification='真实分级未知', purpose='恢复去重、确认及审计')
    obj('OM-DATACOMP-CENTRAL', 'data_component', '中央确认记录', 'C', classification='真实分级未知', owner='情景中央库存责任方', purpose='保存中央确认与预占凭证')
    obj('OM-DATACOMP-PAPER', 'data_component', '基线纸面受理记录', 'C', classification='真实分级未知', owner='情景门店运营责任方', purpose='迁移时补齐身份并逐笔核对')
    obj('OM-TECHNOLOGY-CENTRAL', 'technology', '中央原子预占技术职责', 'D', responsibility='原子核验与预占，中央权威不变', standard='真实技术标准待提供', product='未指定', version='逻辑设计', owner='情景技术责任方', lifecycle='候选逻辑职责，非部署证明', support_end='未知')
    obj('OM-TECH-SERVICE', 'technology_service', '持久恢复技术服务', 'D', responsibility='持久受理、认证重放和隔离', standard='候选接口约束；实现待验证')
    obj('OM-SERVICE-CONFIRM', 'business_service', '中央库存确认服务', 'B', responsibility='仅中央预占成功后确认')
    obj('OM-SERVICE-RECOVER', 'business_service', '断连受理与恢复服务', 'B', responsibility='持久待确认与人工异常接管')
    for suffix, name in [('ONLINE', '中央确认与物流门槛成果'), ('OFFLINE', '持久恢复与人工接管成果')]:
        obj('OM-OUTCOME-'+suffix, 'outcome', name, 'E', owner='情景交付负责人', status='候选工作包成果；非实际生产交付')
    obj('OM-MEASURE', 'measure', '在线最终确认延迟', 'G', owner='情景交付负责人', metric='online_confirmation_p95', target='≤300；给定V1观察160', unit='ms', measurement_window='V1给定11月17至30日实验；非本轮实测')
    obj('OM-MEASURE-RECOVERY', 'measure', '30分钟恢复比例', 'G', owner='情景交付负责人', metric='completed_within_30min / queue_population', target='≥0.95；给定V1观察96/100', unit='ratio', measurement_window='V1给定11月17至30日实验；非本轮实测')
    obj('OM-MEASURE-H', 'measure', 'H期离线确认比例', 'H', owner='情景运营负责人', metric='confirmed / offline_received', target='无数值目标；给定V1观察118/120', unit='ratio', measurement_window='12月1至4日；人工异常不算自动确认')
    for suffix, name in [('ORDER', '订单职责分段'), ('STOCK', '库存职责分段'), ('LOGISTICS', '物流职责分段')]:
        obj('OM-ORG-'+suffix, 'organization', name, 'B', boundary=name+'的情景职责边界', category='职责分段，非法律组织证明', owner='情景'+name+'责任方')
    m['relationships'] = []

    def rel(identity, typ, source, target, label, phase, **attrs):
        m['relationships'].append({'id': identity, 'type': typ, 'source': source, 'target': target, 'label': label,
                                   'source_phase': phase, 'attributes': {'origin': 'explicit-R1-R4-candidate-projection', **attrs}})
    for suffix, _, role, phase in roles:
        rel('FC-PLAYS'+(suffix or '-OWNER'), 'plays', 'OM-ACTOR'+suffix, 'OM-ROLE'+suffix, role+'；不是人事汇报', phase)
    rel('FC-DRIVER-GOAL', 'motivates', 'OM-DRIVER', 'OM-GOAL', '缺统一确认语义促使改进目标', 'A')
    rel('FC-GOAL-OBJECTIVE', 'refines', 'OM-GOAL', 'OM-OBJECTIVE', '目标细化为限定实验目的', 'A')
    for name in ['CONFIRM', 'RECOVER']:
        rel('FC-OBJECTIVE-'+name, 'served_by', 'OM-OBJECTIVE', 'OM-SERVICE-'+name, '由候选业务服务支撑', 'B')
    for suffix in ['ONLINE', 'OFFLINE']:
        rel('FC-WP-'+suffix, 'delivers', 'WP-'+suffix, 'OM-OUTCOME-'+suffix, '候选工作包交付成果', 'E')
        rel('FC-BENEFIT-'+suffix, 'enables_benefit', 'OM-OUTCOME-'+suffix, 'OM-BENEFIT', '候选使能假设；未证实因果或财务收益', 'E')
    rel('FC-BENEFIT-OBJECTIVE', 'contributes_to', 'OM-BENEFIT', 'OM-OBJECTIVE', '限定价值贡献；幅度未知', 'H')
    for suffix in ['', '-RECOVERY']:
        rel('FC-CONTRACT-MEASURE'+suffix, 'measured_by', 'OM-CONTRACT', 'OM-MEASURE'+suffix, '实验合同采用独立指标', 'G')
        rel('FC-OBJECTIVE-MEASURE'+suffix, 'measured_by', 'OM-OBJECTIVE', 'OM-MEASURE'+suffix, '对应实验目的指标', 'G')
    rel('FC-BENEFIT-MEASURE', 'measured_by', 'OM-BENEFIT', 'OM-MEASURE-H', '观察口径，非收益因果证明', 'H')
    rel('FC-EVENT-ORDER', 'data_association', 'OM-DATA-EVENT', 'OM-DATA', '同事件只对应一个订单；冲突隔离', 'C', source_cardinality='0..*', target_cardinality='1')
    rel('FC-ORDER-RESERVATION', 'data_association', 'OM-DATA', 'OM-DATA-RESERVATION', '中央确认关联预占凭证；完整基数未给定', 'C')
    rel('FC-EVENT-POLICY', 'data_association', 'OM-DATA-EVENT', 'OM-DATA-POLICY', '受理记录携带政策版本；完整基数未给定', 'C')
    for identity, target, label in [('OM-DATA-EVENT', 'OM-DATACOMP', '本地持久事件'), ('OM-DATA', 'OM-DATACOMP', '本地待确认副本'), ('OM-DATA', 'OM-DATACOMP-CENTRAL', '中央确认权威记录'), ('OM-DATA-RESERVATION', 'OM-DATACOMP-CENTRAL', '中央预占凭证')]:
        rel('FC-STORE-'+identity+'-'+target, 'stored_in', identity, target, label, 'C')
    for identity in ['OM-DATA', 'OM-DATA-EVENT', 'OM-DATACOMP', 'OM-DATACOMP-CENTRAL']:
        rel('FC-PROTECT-'+identity, 'protected_by', identity, 'OM-CONTROL', '幂等、隔离和确认门槛；不代表权限齐备', 'G')
    rel('FC-MIGRATE-IN', 'migration_flow', 'OM-DATACOMP-PAPER', 'OM-MIGRATION', '录入身份并逐笔核对，失败转人工', 'F')
    rel('FC-MIGRATE-OUT', 'migration_flow', 'OM-MIGRATION', 'OM-DATACOMP', '持久待确认，不能自动确认', 'F')
    for tech in ['OM-TECHNOLOGY', 'OM-TECHNOLOGY-CENTRAL']:
        rel('FC-CONTAIN-'+tech, 'contains', 'OM-PLATFORM', tech, '逻辑技术职责组成；不表示同机部署', 'D')
    rel('FC-REALIZE-RECOVERY', 'realizes', 'OM-TECHNOLOGY', 'OM-TECH-SERVICE', '候选持久恢复技术职责', 'D')
    for suffix, cap in [('ORDER', 'CAP-ORDER'), ('STOCK', 'CAP-RESERVE'), ('LOGISTICS', 'CAP-LOGISTICS')]:
        rel('FC-OWNER-'+suffix, 'owned_by', cap, 'OM-ORG-'+suffix, '情景职责分段承担能力责任', 'B', code='accountable-scenario')
    for identity in ['APP-ORDER', 'APP-STORE', 'APP-STOCK', 'OM-ORGANIZATION', *['OM-ACTOR'+x[0] for x in roles], 'OM-ACTOR-STORE']:
        rel('FC-SCOPE-'+identity, 'in_scope', 'OM-PROJECT', identity, '设计与隔离实验范围；真实授权另审', 'A')
    for app, cap in [('APP-ORDER', 'CAP-ORDER'), ('APP-STOCK', 'CAP-RESERVE'), ('APP-STORE', 'CAP-ORDER')]:
        rel('FC-SUPPORT-'+app, 'supports_capability', app, cap, '候选应用职责支撑能力', 'C')
    rel('FC-STORE-USE', 'uses_application', 'OM-ACTOR-STORE', 'APP-STORE', '门店受理使用；不是数据访问授权', 'B')
    rel('FC-STORE-RUNS', 'runs_on', 'APP-STORE', 'OM-TECHNOLOGY', '候选持久日志支撑', 'D')
    rel('FC-STOCK-RUNS', 'runs_on', 'APP-STOCK', 'OM-TECHNOLOGY-CENTRAL', '中央原子预占职责支撑', 'D')
    for app, wp in [('APP-ORDER', 'WP-ONLINE'), ('APP-STOCK', 'WP-ONLINE'), ('APP-STORE', 'WP-OFFLINE')]:
        rel('FC-MIGRATED-'+app, 'migrated_by', app, wp, '候选改造与联调工作包；非生产切换', 'F')
    rel('FC-CHANGE-REQ', 'changes', 'OM-CHANGE', 'REQ-OFFLINE', 'V2改变新受理限量与等待门槛', 'H')
    rel('FC-CHANGE-WP', 'affects', 'OM-CHANGE', 'WP-OFFLINE', '重新设计并验证混合版本恢复', 'H')
    rel('FC-REQ-WP', 'traces_to', 'REQ-OFFLINE', 'WP-OFFLINE', '工作包追踪受理与恢复需求', 'E')
    m['view_selections']['application-migration-diagram'] = {'entity_ids': ['APP-ORDER', 'APP-STOCK', 'APP-STORE', 'WP-ONLINE', 'WP-OFFLINE'], 'rationale': '只排已有实验工作包窗口；应用为改造映射，不虚构逐应用生产日期。'}
    m['view_selections']['actor-role-matrix'] = {'entity_ids': ['OM-ACTOR'+x[0] for x in roles] + ['OM-ROLE'+x[0] for x in roles], 'rationale': 'R1把原材料五类独立职责显式配对；不是人事汇报。'}
    m['business_rules'] = {'candidate_origin': 'business-supplement.md#V2', 'quota_scope': 'store-sku-pending-total', 'expiry_operator': '>=', 'existing_record_policy': 'captured-policy-version', 'unknown_policy': 'manual-isolation', 'duplicate': 'same-event-and-order-idempotent', 'conflict': 'same-event-different-order-isolation', 'stock_authority': 'central-atomic-reservation-only', 'rollback': 'stop-new-preserve-existing-and-reconcile', 'real_approval': 'not-granted'}
    m['business_rules']['policies'] = {'v1': {'item_limit': 2, 'pending_hours': 24}, 'v2': {'item_limit': 1, 'pending_hours': 8}}
    m['active_version'] = 'v1'
    return m


if __name__ == '__main__':
    v1 = authored_material()
    save(HERE/'materials-v1.json', v1)
    v2 = copy.deepcopy(v1)
    v2['active_version'] = 'v2'
    v2['policy']['baseline'] = {'version': 'V2-candidate', 'offline_max_items': 1, 'pending_hours': 8}
    for row in v2['deliverables']:
        # Retain V1 historical observations and add a targeted V2 revision explicitly.
        if row['deliverable_id'] in v2['policy_sensitive_deliverables'] or row['deliverable_id'] in ['architecture-contract', 'compliance-assessment', 'implementation-governance-model', 'statement-of-work']:
            for chapter in row['sections']:
                chapter['conclusion'] += ' 【V2候选修订】新受理采用1件/8小时；既有V1记录按受理时版本2件/24小时处理，未知版本隔离；达到门槛转人工。中央确认与物流规则不变。旧文中的V1观察及11月实验日期仅为历史，V2性能、排班和实际实施尚未给定。'
            row['unknowns'] = list(dict.fromkeys(row['unknowns']+['V2真实实施排期、独立性能观察与生产接受未提供']))
    save(HERE/'materials-v2.json', v2)
