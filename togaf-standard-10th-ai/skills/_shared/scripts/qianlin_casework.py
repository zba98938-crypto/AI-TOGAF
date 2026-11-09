#!/usr/bin/env python3
"""Build evidence-bounded Qianlin casework without overwriting historical runs.

Inventory size is not semantic coverage. Only hand-authored concepts may enter
chapter dependencies; generated inventory fields never become business evidence.
No renderer/contract fingerprint batch is produced by this development runner.
"""
import argparse
import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / 'examples/qianlin-synthetic'
RUN = CASE / 'runs/semantic-closure-20261104'
STATES = ['QL-baseline', 'QL-transition-1', 'QL-transition-2', 'QL-target']
EVOLUTION = ['baseline', 'transition', 'transition', 'target']
SCOPE = 'QL-enterprise'
CTX = {'domains': ['business', 'data', 'application', 'technology'],
       'landscape': 'capability', 'purpose': 'project', 'abstraction': 'logical', 'evolution': 'baseline'}


def load(path):
    return json.loads(Path(path).read_text())


def materials():
    spec = importlib.util.spec_from_file_location('qianlin_authored_materials', CASE / 'case_materials.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.MATERIALS, module.CHAPTERS, module.EVIDENCE_GAPS


def specifications():
    """Minimal real attributes for selected concepts, not name-pattern fillers."""
    return {
      'driver': ('driver', '交期压力与质量追溯约束', 'strategy',
        {'statement': '缩短批次等待不得牺牲质量证据', 'owner': '虚构销售与质量联席', 'metric': '签发等待与追溯完整性分列', 'target': '候选300分钟；非承诺', 'deadline': '试点影子评审时，日期未知'}),
      'goal': ('goal', '可追溯批次与可核算流向', 'strategy',
        {'statement': '批次来源、方法版本与裁决责任可还原', 'owner': '虚构质量负责人', 'metric': '串行流前置时间', 'target': '候选300分钟', 'deadline': '待真实试点授权', 'perspective': '内部运营；与环境流量分列', 'definition': '从取样登记至质量签发的证据可追溯，不是发货时效'}),
      'objective': ('objective', '减少新增磷石膏堆存的候选目标', 'governance',
        {'statement': '同年同边界按产生减利用核对新增堆存', 'owner': '虚构环境台账负责人', 'metric': '新增堆存t/年', 'target': 405000, 'deadline': '候选完整年度，年份未批准'}),
      'capability': ('capability', '批次质量证据治理', 'flow',
        {'definition': '维护批次身份、检验版本和撤销裁决', 'level': 2, 'category': '质量运营能力', 'score': '未作成熟度评分；流程数据不可代替能力量尺', 'operating_mode': '人工覆盖旧结果；无法完整回放'}),
      'value_stream': ('value_stream', '取得可信批次放行证据', 'flow',
        {'trigger': '批次取样请求', 'stakeholder': '质量角色与后续使用批次的生产岗位', 'value': '取得可复核且可撤销的放行证据，不是化验步骤列表'}),
      'value_stage': ('value_stage', '确认批次可判定性', 'flow',
        {'entry': '已收到批次及样本身份', 'exit': '身份及方法版本无未决冲突，可进入质量裁决', 'value': '使后续裁决使用同一批次语义', 'enabling_capability': '批次质量证据治理'}),
      'organization': ('organization', '候选集团数据治理办公室', 'delivery',
        {'boundary': '只负责物料映射治理，不接管检验和工艺', 'category': '候选治理职能', 'owner': '尚无真实任命'}),
      'role': ('role', '候选质量裁决角色', 'delivery',
        {'responsibility': '裁决检验解释、撤销和待签发批次', 'authority': '仅scenario-authority设定；无真实任命', 'skill': '检验方法版本、冲突裁决、撤销审计'}),
      'actor': ('actor', '虚构江口质量员', 'delivery',
        {'boundary': '质量签发，不修改传输程序', 'owner': '候选质量负责人'}),
      'stakeholder': ('stakeholder', '虚构质量与销售联席', 'strategy',
        {'concern': '交期改善不牺牲质量追溯', 'influence': '候选业务风险裁决，不表示实际授权', 'impact': '质量误签发影响批次放行，交期延后影响销售', 'quadrant': '候选重点协作；尚无访谈量化，不宣称正式象限评分', 'engagement': '拟每周异常批次评审', 'owner': '待真实任命'}),
      'data': ('data_entity', '跨基地物料映射', 'data',
        {'definition': '按基地、原编码及生效版本解释物料，不因同名A-17自动合并', 'owner': '候选数据管理员', 'classification': '内部主数据，分类待真实确认', 'purpose': '使批次指向正确物料语义', 'identity_rule': '本地编码A-17；手工对照且不保留映射版本'}),
      'batch': ('data_entity', '生产批次', 'data',
        {'definition': '一次可追溯生产批次，关联物料映射而不等同于物料', 'owner': '候选生产与质量联席', 'classification': '内部生产信息', 'purpose': '质量裁决对应明确生产对象', 'identity_rule': '本地批次号；跨基地可能重号'}),
      'sample': ('data_entity', '检验样本及方法版本', 'data',
        {'definition': '批次的取样与检验版本，允许同一批次多个样本及撤销', 'owner': '候选实验室质量角色', 'classification': '内部质量信息', 'purpose': '保留检验原始证据及撤销历史', 'version_rule': '保留最后结果，旧值被覆盖'}),
      'application': ('application', '江口MES批次运行', 'data',
        {'owner': '候选MES运维', 'boundary': '持批次状态，不持检验方法权威', 'responsibility': '消费质量事件维护待签发，不直接操作DCS', 'version': '情景基线-v1', 'lifecycle': '既有系统，假设继续使用', 'criticality': '批次运行关键；未量化', 'cost': '未知，未获报价', 'result_handling': '首次结果覆盖式回写；不支持撤销回放'}),
      'lims': ('application', '江口LIMS检验管理', 'data',
        {'owner': '候选实验室系统运维', 'boundary': '检验样本、方法、结果及撤销权威', 'responsibility': '保存检验版本；不直接改变生产批次状态', 'version': '情景基线-v1', 'lifecycle': '既有系统，假设继续使用', 'criticality': '质量证据关键；未量化', 'cost': '未知，未获报价', 'event_mode': '首次合格回传，撤销未成事件'}),
      'mdm': ('application', '候选集团MDM映射治理', 'data',
        {'owner': '候选数据治理办公室', 'boundary': '只治理物料映射，不持检验结论', 'responsibility': '管理生效版本、合并和撤销血缘', 'version': '未建设的候选设计', 'lifecycle': '候选；未实施', 'criticality': '跨基地语义协调；未评定', 'cost': '未知，未获报价', 'mapping_mode': '基线不存在集团权威映射服务'}),
      'interface': ('interface', 'LIMS至MES批次检验事件', 'data',
        {'protocol': '候选HTTPS事件投递，经隔离区代理', 'payload': '批次号、首次合格结果', 'version': '1', 'idempotency': '未定义；首次回写假设'}),
      'technology': ('technology', '候选隔离区消息代理', 'data',
        {'responsibility': '只转发检验事件，不下发DCS命令', 'standard': '项目事件版本契约；非认证', 'product': '未选型消息代理', 'version': '未选型', 'owner': '候选双系统运维', 'lifecycle': '候选', 'support_end': '未知，采购后核实', 'retention': '首次消息短暂保留；尚无回放偏移治理'}),
      'req': ('requirement', '批次签发证据可追溯', 'governance',
        {'statement': '每次签发关联批次及首次合格结果', 'priority': 'must（情景选择）', 'owner': '候选质量负责人', 'acceptance': '拟按批次查得首次结果；未执行'}),
      'constraint': ('constraint', '安全控制及范围禁入边界', 'strategy',
        {'category': '硬边界', 'rationale': '本轮不改电炉DCS联锁、矿山储量和工资', 'owner': '候选架构负责人', 'source': '全虚构strategy.boundary', 'expiry': '范围变更须另行真实授权'}),
      'principle': ('principle', '权威性按职责而非单库定义', 'data',
        {'statement': 'MDM持映射，LIMS持检验版本，MES持批次状态', 'rationale': '避免同名物料误合并及专业证据覆盖', 'implications': '冲突需人工裁决，变更保留版本和撤销血缘', 'owner': '候选数据治理办公室'}),
      'abb': ('abb', '批次身份与证据协调ABB', 'data',
        {'responsibility': '协调身份、版本、撤销与人工裁决', 'boundary': '逻辑服务，不接管专业检验或联锁', 'interfaces': ['检验事件输入', '批次状态与证据查询'], 'quality': '重放不重复签发，撤销可还原', 'definition': '独立于实现产品的批次证据协调能力', 'abstraction': 'logical', 'service': '身份校验、证据回放、撤销冻结', 'requirements': ['签发证据可追溯', '撤销与跨日幂等'], 'realization': '候选隔离区事件适配器SBB；未实现', 'owner': '候选架构负责人'}),
      'sbb': ('sbb', '隔离区事件适配器SBB', 'data',
        {'responsibility': '实现样本版本幂等、撤销事件和待签发冻结', 'implementation': '候选适配器及版本映射库，未采购', 'lifecycle': 'candidate；not-started'}),
      'risk': ('risk', '撤销重传造成误签发', 'governance',
        {'impact': '错误批次可能再次进入待发货状态', 'owner': '候选质量风险责任人', 'likelihood': '情景序数3，不是发生概率', 'asset': '待签发批次状态及检验版本', 'threat': '跨日重传或撤销乱序', 'vulnerability': '覆盖旧结果且无幂等键', 'residual_risk': '未知；没有运行控制有效性证据，不将固有风险12自动下调', 'treatment': '版本幂等、冻结、人工裁决；尚未验证'}),
      'control': ('control', '版本幂等及撤销冻结', 'data',
        {'classification': '预防及可追溯恢复控制', 'owner': '候选质量与运维联席', 'purpose': '禁止重复签发；撤销后冻结待签发状态', 'effectiveness': '未知，尚无实际验证'}),
      'gap': ('gap', '撤销回放及映射裁决差距', 'governance',
        {'description': '基线覆盖旧值且未定义跨日幂等，目标需可撤销事件和权威映射', 'owner': '候选架构负责人', 'resolution': 'WP-1身份规则与WP-2影子演练'}),
      'wp': ('work_package', 'WP-2 江口影子对账及异常演练', 'delivery',
        {'owner': '候选双系统项目组', 'duration_days': 20, 'depends_on': ['WP-1'], 'scope': '首次检验回写对账；尚无撤销场景'}),
      'wp1': ('work_package', 'WP-1 批次身份与隔离适配', 'delivery',
        {'owner': '候选数据及运维组', 'duration_days': 15, 'depends_on': [], 'scope': '稳定批次键、版本和隔离通道；未执行'}),
      'wp3': ('work_package', 'WP-3 六基地映射试点', 'delivery',
        {'owner': '候选数据治理办公室', 'duration_days': 30, 'depends_on': ['WP-2'], 'scope': '过渡一门禁后才提请六基地物料映射治理；未执行'}),
      'migration': ('migration_step', '可撤销的双系统过渡', 'delivery',
        {'transformation': '保留本地编码并增加版本映射，不覆盖原始结果', 'reconciliation': '按批次、样本、版本核对；情景0.5%三日触发评审', 'rollback': '停止消费者写入、冻结、核对偏移、旧账只读与逐批裁决'}),
      'milestone': ('milestone', '过渡一至过渡二的候选门禁', 'delivery',
        {'criterion': '连续3个影子批次无重复签发且撤销可追溯，才提出评审', 'status': '未执行；不是已通过', 'owner': '待真实指定门禁责任人'}),
      'benefit': ('benefit', '批次等待缩短与少堆存的候选收益', 'governance',
        {'owner': '候选经营与环境责任人', 'metric': '等待分钟与新增堆存t/年分列', 'target': '候选300分钟、405000t/年，非已实现', 'attribution': '信息证据贡献；物理利用设施与市场独立', 'waiting_assumption': '仅首次合格结果；不含撤销裁决'}),
      'measure': ('measure', '影子批次证据与串行流度量', 'flow',
        {'owner': '候选质量负责人', 'metric': '前置时间、加工时间、首次完整准确率', 'target': '候选300分钟；99%×99%×99%', 'unit': 'minute；百分比另列', 'measurement_window': '20个影子批次，尚未执行'}),
      'change': ('change_request', 'CR-01 撤销与跨日重传', 'governance',
        {'reason': '首次合格假设遗漏撤销和重传', 'impact': '需求、数据、接口、隔离区留存、回退、WP-2和收益假设；工资/储量/DCS不变', 'severity': '质量风险，情景优先', 'owner': '候选质量负责人', 'decision': 'scenario-authority仅授权分析；待真实评审'}),
      'decision': ('decision_record', 'DR-01 候选隔离区适配而非全面替换', 'governance',
        {'decision': '仅候选，非采购或实施批准', 'rationale': '显式偏好权重支持可回放适配；报价未知', 'owner': '候选架构评审人'}),
      'contract': ('contract', '候选质量事件交换条款', 'governance',
        {'owner': '真实缔约双方未知', 'target': '重放不重复签发且撤销可追溯', 'unit': '逐影子批次判定', 'measurement_window': '候选20批次，未执行', 'signature': '无签署；scenario-authority不是法律授权'}),
      'project': ('project', '江口批次追溯虚构工作请求', 'strategy',
        {'scope': '江口两基地先行，六基地映射后续，不含DCS/工资/储量', 'authorization': 'scenario-authority；无真实预算或上线授权'}),
      'standard': ('standard', '项目事件版本和隔离约定', 'data',
        {'category': '项目技术约定；非认证', 'version': 'scenario-v2', 'disposition': '候选', 'rationale': '版本幂等、撤销独立事件、无DCS命令', 'exception_process': '质量及架构联合评审；无真实批准'}),
      'repository': ('repository_asset', '黔磷情景资产索引', 'governance',
        {'inventory_use': '1632条214类库存仅规模夹具，不支撑业务结论', 'versioning': '概念ID+状态+版本；保留旧run', 'owner': '真实资产管理员未任命'})
    }


# Behaviorally motivated deltas: never append arbitrary "目标态修订".
DELTAS = {
 'capability': [
  {'operating_mode': '江口影子批次可重放，质量角色人工裁决'},
  {'operating_mode': '六基地映射版本治理，争议进入人工队列'},
  {'operating_mode': '批次、检验、流向证据贯通；质量责任仍独立'}],
 'data': [
  {'identity_rule': '江口两基地按基地+原编码明确A-17冲突，保留原始映射候选'},
  {'identity_rule': '基地+原编码+生效版本；六基地映射合并可撤销'},
  {'identity_rule': '稳定物料映射关联批次与流向；证据版本不可覆盖'}],
 'batch': [
  {'identity_rule': '基地+装置+批次号；绑定样本与检验版本'},
  {'identity_rule': '批次持物料映射生效版本，争议批次标记待裁决'},
  {'identity_rule': '批次与流向证据关联，撤销后禁止自动恢复待发货'}],
 'sample': [
  {'version_rule': '样本号+方法版本+事件版本；撤销独立事件不覆盖旧值'},
  {'version_rule': '样本引用批次物料映射版本，保留争议裁决证据'},
  {'version_rule': '检验、撤销与最终批次签发之间可端到端回放'}],
 'application': [
  {'version': 'scenario-v2', 'result_handling': '消费LIMS独立撤销事件，冻结待签发并保留偏移'},
  {'version': 'scenario-v3', 'result_handling': '消费MDM版本映射，副本标记延迟'},
  {'version': 'scenario-v4', 'result_handling': '检验撤销与流向证据一致可回放；不自动放行'}],
 'lims': [
  {'version': 'scenario-v2', 'event_mode': '按样本及方法版本发送检验、撤销事件'},
  {'version': 'scenario-v3', 'event_mode': '检验事件附物料映射生效版本供争议追溯'},
  {'version': 'scenario-v4', 'event_mode': '保留检验全历史供批次及流向证据回放'}],
 'mdm': [
  {'version': 'scenario-design-v1', 'mapping_mode': '江口冲突人工清单，尚未集中自动合并'},
  {'version': 'scenario-design-v2', 'mapping_mode': '候选六基地版本映射，合并撤销由人工裁决'},
  {'version': 'scenario-design-v3', 'mapping_mode': '权威映射服务与批次和流向引用关联；仍未实际实施'}],
 'interface': [
  {'payload': '批次键、样本键、方法版本、结果、撤销标记', 'version': '2', 'idempotency': '样本键+方法版本+事件版本；跨日重放不新增签发'},
  {'payload': '检验事件+物料映射生效版本', 'version': '3', 'idempotency': '映射变更保留原键及可撤销血缘'},
  {'payload': '检验事件+映射版本+流向证据引用', 'version': '4', 'idempotency': '全链保留偏移与撤销，不覆盖历史'}],
 'technology': [
  {'retention': '隔离区保留事件版本和消费者偏移；留存期限待批准'},
  {'retention': '六基地映射事件分区，副本延迟显式标记'},
  {'retention': '批次和流向审计索引；容量及保留期限仍待真实验证'}],
 'req': [
  {'statement': '签发关联批次、样本、方法和事件版本；撤销独立留痕且跨日重传不重复签发', 'acceptance': '拟以20影子批次验证重复/撤销/跨日/断网；尚未执行'},
  {'statement': '保留过渡一签发证据及跨日幂等，增加六基地物料映射按生效版本消费且合并可撤销', 'acceptance': '拟逐项核对错码A-17与合并撤销血缘；未执行'},
  {'statement': '签发与流向可追溯到原始检验及映射版本，岗位裁决仍独立', 'acceptance': '拟结合批次、检验和流向证据端到端回放；未执行'}],
 'wp': [
  {'scope': 'WP-2增加撤销、重复、跨日及断网影子演练；保持WP-1依赖'},
  {'scope': 'WP-2提供版本回放与裁决记录作为WP-3映射试点的前置输入；未执行'},
  {'scope': 'WP-2演练资产进入候选运行手册，实际上线与收益仍需独立接受'}],
 'benefit': [
  {'waiting_assumption': '候选300分钟包含人工签发；撤销异常工时仍未知'},
  {'waiting_assumption': '映射争议等待独立计量，不沿用江口单流程目标'},
  {'waiting_assumption': '等待与堆存指标分别核验，实际收益未观察'}]
}


def analyses(raw):
    result = []
    for suffix in ['baseline', 'target']:
        steps = [{'id': f'step-{i}', 'lead_time': {'value': lt, 'unit': 'minute'},
                  'process_time': {'value': pt, 'unit': 'minute'}, 'complete_accurate_percent': q,
                  'evidence': ['QL-CASE-flow']} for i, (_, lt, pt, q) in enumerate(raw['flow'][suffix], 1)]
        result.append({'id': 'QL-A-flow-'+suffix, 'method_id': 'lean-serial-flow', 'evidence': ['QL-CASE-flow'],
          'inputs': {'boundary': '江口单条串行批次；'+suffix+'全虚构；无并行返工',
            'aggregation_rule': 'serial-conditional-first-pass', 'rule_evidence': ['QL-CASE-flow'], 'steps': steps}})
    option_rule = raw['governance']['option_rule']
    risk_rule = raw['governance']['risk_rule']
    result.append({'id': 'QL-A-options', 'method_id': 'weighted-normalized-decision',
      'evidence': ['QL-CASE-governance'], 'inputs': {
        'rule_evidence': ['QL-CASE-governance'],
        'criteria': [{'id': key, 'direction': direction, 'weight': option_rule['weights'][key], 'min': 1, 'max': 5}
                     for key,direction in [('recoverability','maximize'),('disruption','minimize')]],
        'options': [{'id': key, 'scores': copy.deepcopy(scores)} for key,scores in option_rule['scores'].items()]+[
                    {'id': 'overwrite-only', 'eligible': False, 'reason': option_rule['excluded']}]}})
    result.append({'id': 'QL-A-risk', 'method_id': 'risk-explicit-rule', 'evidence': ['QL-CASE-governance'],
      'inputs': {'formula': risk_rule['formula'], 'rule_evidence': ['QL-CASE-governance'],
        'likelihood': {'value': risk_rule['likelihood'], 'scale': risk_rule['scale'], 'evidence': ['QL-CASE-governance']},
        'impact': {'value': risk_rule['impact'], 'scale': risk_rule['scale'], 'evidence': ['QL-CASE-governance']}}})
    result.append({'id': 'QL-A-environment', 'method_id': 'environmental-delta', 'evidence': ['QL-CASE-governance'],
      'inputs': {'boundary': '同年磷石膏产生-利用=新增堆存；不折算CO2或现金',
        'method_evidence': ['QL-CASE-governance'], 'rows': [
          {'id': 'baseline-stock', 'added': 1350000, 'retired': 837000, 'unit': 't/年', 'scope': '虚构六基地流量', 'period': '虚构基线年度', 'evidence': ['QL-CASE-governance']},
          {'id': 'target-stock', 'added': 1350000, 'retired': 945000, 'unit': 't/年', 'scope': '虚构六基地流量', 'period': '候选目标年度', 'evidence': ['QL-CASE-governance']}]}})
    return result


def build_case(run=RUN):
    raw, chapters, evidence_gaps = materials()
    inventory = [e for p in sorted((CASE/'dataset/context').glob('*.json')) for e in load(p)['entities']]
    model = {'schema_version': '2.0', 'project': {'id': 'qianlin-casework', 'name': '全虚构黔磷端到端证据案例',
      'version': 'semantic-closure-1', 'is_example': True, 'approval_status': 'candidate',
      'implementation_status': 'not-started', 'context': CTX}, 'entities': [], 'relationships': [], 'views': [],
      'deliverables': [], 'analyses': analyses(raw), 'gaps': [],
      'sources': [{'id': 'QL-INVENTORY', 'kind': 'example', 'description': '全虚构固定种子库存，仅规模夹具，不是业务证据',
        'locator': 'examples/qianlin-synthetic/dataset/manifest.json'}] + [
        {'id': 'QL-CASE-'+key, 'kind': 'example', 'description': '全虚构scenario-authority手写材料：'+key,
         'locator': str(run.relative_to(ROOT))+'/materials.json#/'+key} for key in raw],
      'extensions': {'entity_types': {'project:section_evidence': '项目章节证据记录；不是官方TOGAF类型',
          'guide:architecture_domain': '指南中的架构域类别，不是企业组织或部署容器',
          'guide:metamodel_entity': '来源内容元模型的实体类型，不是项目实体实例'},
        'relationship_types': {'project:case_trace': {'source_types': ['*'], 'target_types': ['*'],
          'meaning': '情景作者明确论证的跨域依赖，不表示实际因果或已批准实现'}}}}
    for e in inventory:
        e = copy.deepcopy(e)
        e.update(state_id=STATES[0], scope_id=SCOPE, evidence=['QL-INVENTORY'])
        model['entities'].append(e)
    # Preserve only the fixture's structural instance ownership cardinality.
    # These links stay inventory evidence and never satisfy chapter support.
    for r in load(CASE/'dataset/relationships.json')['relationships']:
        if r['type']=='instance_of':
            r = copy.deepcopy(r)
            r['evidence'] = ['QL-INVENTORY']
            model['relationships'].append(r)
    selected = {}
    for key, (kind, name, source, attrs) in specifications().items():
        e = next((e for e in model['entities'] if e['type']==kind and e['id'] not in selected.values()), None)
        if e is None:
            e = {'id': 'QL-CASE-'+key, 'type': kind}
            model['entities'].append(e)
        e.update(name=name, attributes=copy.deepcopy(attrs), evidence=['QL-CASE-'+source], certainty='assumed',
                 concept_id=e.get('concept_id', 'QL-CONCEPT-'+key), version='1', evolution='baseline',
                 state_id=STATES[0], scope_id=SCOPE, context=copy.deepcopy(CTX),
                 approval_status='candidate', implementation_status='not-started')
        selected[key] = e['id']
    versions = {key: [eid] for key, eid in selected.items()}
    entities = {e['id']:e for e in model['entities']}
    for key, deltas in DELTAS.items():
        original = entities[selected[key]]
        attrs = copy.deepcopy(original['attributes'])
        for i, delta in enumerate(deltas, 1):
            attrs.update(copy.deepcopy(delta))
            e = copy.deepcopy(original)
            e.update(id=original['id']+'-case-v'+str(i+1), attributes=copy.deepcopy(attrs), version=str(i+1),
                     state_id=STATES[i], evolution=EVOLUTION[i], context={**CTX, 'evolution': EVOLUTION[i]})
            model['entities'].append(e)
            versions[key].append(e['id'])
    # Curated dependency chain is distinct from random scale edges. The original
    # relationship fixture remains on disk and is intentionally not imported.
    links = [
      ('driver','goal','交期与质量双重压力驱动可追溯目标'),
      ('goal','capability','达成目标需要批次证据治理能力，非仅采购平台'),
      ('capability','organization','映射治理职责候选归数据治理办公室'),
      ('organization','role','办公室协调映射，质量角色独立裁决检验语义'),
      ('capability','data','证据治理需要保留原编码及物料映射版本'),
      ('data','application','MES批次状态引用已解释的物料映射版本'),
      ('application','interface','MES从检验接口消费版本化事件'),
      ('interface','technology','跨安全边界交换经隔离区消息代理'),
      ('technology','risk','代理重传或乱序若无版本幂等可能造成误签发'),
      ('risk','gap','误签发风险暴露基线覆盖旧值和不可回放的差距'),
      ('gap','abb','批次身份与证据协调ABB负责补足版本及撤销契约'),
      ('abb','sbb','逻辑证据契约由候选隔离区适配器实现，不等于已经实现'),
      ('sbb','wp','WP-2以影子批次检验适配器的重复、撤销及断网行为'),
      ('wp','milestone','WP-2演练回执是过渡门禁评审的必要输入'),
      ('milestone','benefit','门禁仅允许检验收益假设，不证明等待或堆存已经改善'),
      ('benefit','measure','收益需等待时标和流量证据分别核验，不混为现金ROI'),
      ('measure','change','撤销额外工时未知，需在CR-01中重新审查等待目标'),
      ('change','req','CR-01将首次结果假设扩展为撤销与跨日幂等要求'),
      ('req','data','追溯要求约束物料映射生效版本不可覆盖'),
      ('control','risk','版本幂等与冻结针对误签发；控制有效性未验证'),
      ('migration','wp','双系统写入和恢复安排约束WP-2演练计划'),
      ('contract','req','候选事件交换条款引用可追溯和幂等需求，不是已签合同'),
      ('value_stream','value_stage','可信放行价值流先取得批次可判定性，非直接罗列化验步骤'),
      ('value_stage','capability','可判定性阶段由批次证据治理能力支撑'),
      ('wp','wp1','WP-2依赖WP-1稳定批次键和隔离通道'),
      ('wp3','wp','WP-3六基地映射依赖WP-2门禁输入，不以日期自动越过'),
      ('batch','data','生产批次引用物料映射版本，不与物料合并成一个对象'),
      ('sample','batch','同一批次可有多个样本；样本版本和撤销分别留痕'),
      ('lims','sample','LIMS是检验样本及方法版本的权威，不是MES'),
      ('lims','interface','LIMS通过接口发布检验和撤销事件'),
      ('interface','application','MES消费事件后维护冻结和待签发状态'),
      ('mdm','data','MDM治理映射和可撤销血缘，不持检验结论'),
      ('application','batch','MES维护生产批次状态，质量裁决责任仍独立')]
    for i, (a,b,label) in enumerate(links, 1):
        model['relationships'].append({'id': f'QL-TRACE-{i:02}', 'type': 'project:case_trace',
          'source': versions[a][-1], 'target': versions[b][-1], 'label': label,
          'attributes': {'authority': 'scenario-authority'}, 'evidence': ['QL-CASE-governance'], 'certainty': 'assumed'})
    model['states'] = [{'id': sid, 'name': name, 'evolution': evo, 'scope_id': SCOPE, 'version': str(i+1),
      'evidence': ['QL-CASE-delivery'], **({'operating_conditions': {
        'operations': raw['delivery']['operations'], 'data_consistency': raw['data']['identity'],
        'dependencies': '先WP-1身份和隔离，再WP-2影子对账，后WP-3六基地映射',
        'controls': raw['delivery']['gate'], 'rollback': raw['delivery']['rollback']}} if evo=='transition' else {})}
      for i,(sid,name,evo) in enumerate(zip(STATES, ['基线覆盖旧值','过渡一江口影子回放','过渡二六基地映射','目标批次及流向证据治理'], EVOLUTION))]
    rules = load(ROOT/'capability-addenda/deliverable-assembly-rules.json')
    caps = load(ROOT/'capabilities.json')
    profiles = {p['id']:p for p in caps['profiles']}
    needed_families = {a for r in rules['deliverables'] for s in r['sections']+r.get('core_requirements',[]) for a in s.get('artifact_ids',[])}
    needed_profiles = {p for r in rules['deliverables'] for s in r['sections'] for p in s.get('profile_ids',[])}
    for family in needed_families:
        p = next((p for p in caps['profiles'] if p['artifact_id']==family and p['id'].startswith('compat-')), None)
        if p:
            needed_profiles.add(p['id'])
    entity_index = {e['id']:e for e in model['entities']}
    for pid in sorted(needed_profiles):
        p = profiles.get(pid)
        if not p:
            continue
        ids = [versions[k][-1] for k in selected if entity_index[versions[k][-1]]['type'] in p.get('entity_types',[])]
        if not ids:
            continue
        rs = [r['id'] for r in model['relationships'] if {r['source'], r['target']} <= set(ids)
              and r['type'] in p.get('relationship_types',[])]
        model['views'].append({'id': 'qlv-'+pid, 'artifact_id': p['artifact_id'], 'profile_id': pid,
          'title': p['artifact_id']+'／全虚构语义选集', 'context': {**CTX, 'evolution': 'target'},
          'entity_ids': ids, 'relationship_ids': rs, 'scope_id': SCOPE, 'state_ids': STATES,
          'allow_mixed_evolution': True, 'analysis': '仅选择手写材料支持的概念；保留基线及目标职责边界，未知与真实接受另行评审。',
          'legend': '全虚构；状态和版本明确；库存不进入选集。'})
    for rule in rules['deliverables']:
        did = rule['id']
        rows = chapters[did]
        if [r[0] for r in rows] != [s['title'] for s in rule['sections']]:
            raise ValueError('章节契约已变，请重新人工审查：'+did)
        d = {'id': 'QL-DLV-'+did, 'deliverable_id': did, 'title': did+'／全虚构证据案例',
          'view_ids': [], 'entity_ids': [], 'sections': {}, 'approval_status': 'candidate', 'implementation_status': 'not-started',
          'assembly': {'rules_version': rules['rules_version'], 'mode': 'draft', 'scope_id': SCOPE,
            'state_ids': STATES, 'section_bindings': {}}}
        for number, (title, question, conclusion, tradeoff, unknown, keys, analysis) in enumerate(rows, 1):
            eid = f'QL-CHAPTER-{did}-{number:02}'
            refs = [versions[k][0 if analysis=='flow-baseline' else -1] for k in keys.split()]
            if 'capability' in keys.split():
                refs += [versions[k][-1] for k in ['value_stream','value_stage']]
            if 'wp' in keys.split():
                refs += [versions[k][-1] for k in ['wp1','wp3']]
            if 'data' in keys.split():
                refs += [versions[k][0 if analysis=='flow-baseline' else -1] for k in ['batch','sample']]
            if 'application' in keys.split():
                refs += [versions[k][0 if analysis=='flow-baseline' else -1] for k in ['lims','mdm']]
            aids = ['QL-A-'+analysis]
            if 'benefit' in keys.split() or '堆存' in question or '70%' in question:
                aids.append('QL-A-environment')
            evidence = sorted({sid for ref in refs for sid in entity_index[ref]['evidence']})
            record = {'id': eid, 'type': 'project:section_evidence', 'name': title+'／针对性证据论证',
              'scope_id': SCOPE, 'state_id': STATES[-1], 'certainty': 'assumed', 'evidence': evidence,
              'attributes': {'record_contract': 'scenario-section/2', 'deliverable_id': did, 'section_title': title,
                'question': question, 'conclusion': conclusion, 'decision': conclusion,
                'scope': raw['strategy']['boundary'], 'owner': '候选质量与架构联席；无真实任命',
                'acceptance': {'flow-baseline': raw['flow']['basis']+'；以真实批次时标及完整性记录另行核实，未执行。',
                  'flow-target': raw['flow']['acceptance'],
                  'options': '核对硬约束、偏好锚点和权重敏感性；报价未知，不以排名授予采购或上线批准。',
                  'risk': '拟注入重复、撤销乱序和隔离区断网，逐批核对冻结及人工裁决；无实际执行回执。'}[analysis],
                'status': 'scenario-proposal', 'authority': 'scenario-authority', 'tradeoffs': [tradeoff],
                'unknowns': [unknown], 'model_refs': refs, 'analysis_refs': list(dict.fromkeys(aids)),
                'evidence_gaps': evidence_gaps.get((did,title), [])}}
            record['attributes']['relationship_refs'] = [r['id'] for r in model['relationships']
              if {r['source'],r['target']} <= set(refs)]
            model['entities'].append(record)
            sr = next(s for s in rule['sections'] if s['title']==title)
            # A named profile is a narrower selector, never satisfy it by family.
            selected_views = [v['id'] for v in model['views'] if (v['profile_id'] in sr['profile_ids']
                if sr.get('profile_ids') else v['artifact_id'] in sr.get('artifact_ids',[]))]
            d['assembly']['section_bindings'][title] = {'entity_ids': [eid], 'view_ids': selected_views}
            d['view_ids'].extend(selected_views)
        for req in rule.get('core_requirements',[]):
            v = next((v for v in model['views'] if v['artifact_id'] in req.get('artifact_ids',[])
                      or v['profile_id'] in req.get('profile_ids',[])), None)
            if v:
                d['view_ids'].append(v['id'])
        d['view_ids'] = sorted(set(d['view_ids']))
        model['deliverables'].append(d)
    model['scopes'] = [{'id': SCOPE, 'description': '全虚构六基地背景，江口两基地先行；不含DCS/工资/矿山储量变更',
      'included_ids': [e['id'] for e in model['entities']], 'excluded_ids': []}]
    model['comparisons'] = [{'id': 'QL-COMPARE', 'baseline_state_id': STATES[0], 'target_state_id': STATES[-1],
      'scope_id': SCOPE, 'state_ids': STATES, 'baseline_ids': [versions[k][0] for k in DELTAS],
      'target_ids': [versions[k][-1] for k in DELTAS], 'gap_ids': [selected['gap']],
      'basis': '仅比较手写概念四态版本；非选择库存未建目标态不意味着删减',
      'transition_checks': model['states'][1]['operating_conditions']}]
    return model, raw, {'inventory_entities': len(inventory), 'inventory_types': len({e['type'] for e in inventory}),
      'curated_concepts': len(selected), 'four_state_concepts': len(DELTAS), 'selected_ids': selected, 'versions': versions,
      'notice': '不导入随机关系，不随机修订目标属性；非选择库存仅作规模背景。'}


def write_run(out):
    from analyze import evaluate, compare
    from deliverable_assembly import assemble
    from validate import DELS, validate
    out = Path(out).resolve()
    if CASE.resolve() not in out.parents or out.exists():
        raise ValueError('输出必须为黔磷专属尚不存在的新run目录；拒绝覆写历史')
    model, raw, inventory = build_case(out)
    out.mkdir(parents=True)
    def save(name, value):
        (out/name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')
    save('materials.json', raw)
    save('model.json', model)
    save('inventory-boundary.json', inventory)
    save('analysis-results.json', [evaluate(a, model) for a in model['analyses']])
    comparison = compare(model, STATES[0], STATES[-1], SCOPE)
    entities = {e['id']:e for e in model['entities']}
    compared = {entities[inventory['versions'][key][0]]['concept_id'] for key in DELTAS}
    comparison['changes'] = [row for row in comparison['changes'] if row['concept_id'] in compared]
    comparison['boundary_notice'] = '仅比较显式四态概念；未为库存构造目标态不表示删除；工资、矿山储量和DCS联锁无本情景改动。'
    save('comparison.json', comparison)
    issues = validate(model)
    save('validation.json', issues)
    (out/'deliverables').mkdir()
    results = []
    for d in model['deliverables']:
        result = assemble(model, d, DELS[d['deliverable_id']])
        strict = copy.deepcopy(d)
        strict['assembly']['mode'] = 'strict'
        strict_result = assemble(model, strict, DELS[d['deliverable_id']])
        text = '# '+d['title']+'\n\n全虚构；scenario-authority；不是实际批准、签署、实现或业务接受。\n\n'
        import re
        text += '\n\n'.join('## '+b['title']+'\n\n'+re.sub(
            r'\[([^\]]+)\]\(\.\./artifacts/[^)]+\)', r'\1（组装预览；完整制品链接由generate.py生成）',
            b['markdown']) for b in result['section_blocks'])
        (out/'deliverables'/(d['deliverable_id']+'.md')).write_text(text)
        results.append({'deliverable_id': d['deliverable_id'], 'draft_status': result['status'],
          'strict_status': strict_result['status'], 'gaps': result['gaps'], 'section_coverage': result['section_coverage'],
          'required_view_ids': result['required_view_ids'], 'required_analysis_ids': result['required_analysis_ids'],
          'direct_entity_ids': result['direct_entity_ids']})
    save('assembly-development.json', {'final_fingerprint_batch': False, 'business_accepted': False,
      'notice': '并行规则/渲染改动期间的开发组装；main集成后需重新生成正式批次。', 'deliverables': results})
    return {'out': str(out), 'deliverables': len(results), 'chapters': sum(len(d['section_coverage']) for d in results),
      'validation_errors': sum(i['level']=='error' for i in issues), 'assembly_gaps': sum(len(d['gaps']) for d in results)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=RUN)
    print(json.dumps(write_run(parser.parse_args().out), ensure_ascii=False))
