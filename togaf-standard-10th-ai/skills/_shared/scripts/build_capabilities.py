# -*- coding: utf-8 -*-
"""Maintainer: build reviewed, source-located operational capability contracts.

This is a project registry, not an assertion that every row is an official
TOGAF artifact type. Source definitions and implementation evidence are separate.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = {
 'security':'togaf-security-risk','ea':'togaf-ea-capability','vision':'togaf-vision-scenarios',
 'strategy':'togaf-strategy-capabilities','value':'togaf-value-streams','org':'togaf-organization-roles',
 'business':'togaf-business-models-processes','data':'togaf-information-data','app':'togaf-application-architecture',
 'tech':'togaf-technology-architecture','gap':'togaf-gap-solutions','migration':'togaf-migration-roadmap',
 'requirements':'togaf-requirements','governance':'togaf-implementation-governance','change':'togaf-change-value',
 'workbench':'togaf-architecture-workbench','review':'togaf-artifact-review'}

# Field meanings are explicit project conventions, not asserted verbatim standard definitions.
FIELD_LABELS = dict(item.strip().split(':',1) for item in '''
scope:适用组织、业务及架构边界|
impact_scale:影响评价尺度及锚点|
likelihood_scale:可能性评价尺度及锚点|
acceptance_boundary:风险可接受范围及超限判据|
approval_authority:拥有批准权限的责任方|
business_process:受影响的业务流程引用|
loss_type:业务损失或收益的类型|
impact:业务影响及其依据|
criticality:相对业务关键性及判据|
time_horizon:分析覆盖的时间窗口|
role:承担职责的角色|
authority:决策或数据权威及授权范围|
capacity:可投入的资源容量|
availability:指定期间可用资源|
engagement:参与方式与节奏|
concern:利益相关者的具体关注点|
principle:适用原则引用|
risk:风险对象引用|
service:服务对象引用|
definition:业务含义和排除边界|
metric:度量方法和计算定义|
unit:度量单位|
target:期望结果或目标值|
owner:对对象负责的责任方|
accountability:最终问责关系|
policy_level:政策在治理结构中的层级|
review_cycle:复核周期|
policy_authority:安全域内的政策制定与执行权威|
classification:安全分类标签|
assets:受该政策或域管辖的资产引用|
boundary:内外边界的含义|
federation:跨组织联邦范围和协议|
business_basis:信任所依据的业务关系|
legal_basis:信任所依据的法律协议|
direction:有向或双向关系的明确读法|
conditions:关系或规则成立的条件|
asset:风险资产引用|
threat:威胁主体或事件|
vulnerability:可被利用的脆弱性|
likelihood:已声明尺度下的事件可能性|
treatment:选定风险处置及理由|
residual_risk:处置后的剩余风险及评价依据|
jurisdiction:适用司法辖区|
version:来源或规范版本|
applicability:适用性判据与判断理由|
business_function:业务功能引用|
data_scope:受条款影响的数据范围|
selection_reason:选择该方案或框架的理由|
mandatory_controls:必须满足的控制要求|
certification:所需认证及适用范围|
objective:服务或控制所实现的目的|
operations:运行与维护要求|
consumers:服务消费者|
implementation:实现对象或实施证据|
classification_scheme:分类规则与版本|
criteria:评价准则及尺度|
requirements:架构要求引用|
dataset:被评价或使用的数据集|
dimension:评价维度|
threshold:判定边界及依据|
evidence_period:证据采集期间|
action:拟采取的具体行动|
due_date:行动计划完成日期|
control:控制措施引用|
expected_residual:预期剩余风险及假设|
state_id:具体架构状态的稳定标识|
migration_activity:迁移活动引用|
mitigation:降低风险的措施|
trigger:触发事件或判据|
decision_owner:有权作出该决策的责任方|
prerequisite:可执行该项的前置条件|
data_recovery:数据恢复与一致性规则|
sequence:执行次序及其依据|
verification:验证方法与验收证据|
change:待评估变更引用|
affected_asset:经分析受影响的资产|
requirement:需求对象引用|
decision:决策结果、理由和状态|
criterion:单项判断准则|
evidence:本条观察的证据描述或引用|
result:评估结果及不确定性|
deviation:偏离要求的内容与处置|
audience:培训受众与角色|
competency:所需知识技能和行为|
activity:实施或学习活动|
review:复核方法及责任|
element:成熟度要素|
level:所用模型下的层级|
description:级别或特征的描述|
evidence_rule:判断达成所需的证据规则|
weight:明确声明的聚合权重|
assessment_date:评估日期|
assessor:评价人或评价角色|
confidence:判断可信度及理由|
ubiquity:数字技术采用的普及广度|
velocity:数字技术采用的速度|
rationale:分析或选择的理由|
tradeoffs:已考虑的权衡|
factor:就绪度因素|
category:所声明分类体系下的分类|
statement:原子陈述或问题|
scale_anchor:量表级别的含义|
respondent:问卷回答者或角色|
question_ids:参与评价的问题标识|
rating:声明量表下的评价值|
anchor:评价值对应的量表锚点|
attention:需要管理关注的原因|
primary_consequence:因素缺失的主要后果|
business_effect:对本地业务的影响解释|
factor_category:基础、影响或持续因素分类|
readiness_evidence:就绪条件的证据|
problem:待解决问题及其业务证据|
environment:业务与技术环境|
objectives:期望业务结果及可衡量目的|
human_actors:人的参与者与角色|
computer_actors:计算机参与者与责任|
process:业务流程或行为引用|
stakeholder:利益相关者引用|
human_actor:人的参与者引用|
computer_actor:计算机参与者引用|
goal:业务目标引用|
option:候选方案|
score:所声明量表下的评分|
feasibility:可行性判断及依据|
capability_type:被实例化的能力类型标识|
stage:价值流阶段引用|
application:支撑应用引用|
information:被使用或修改的信息引用|
instance:能力实例标识|
change_kind:保留、优化、整合、新建或退役等变化类型|
baseline:比较基线及状态|
gap:基线目标之间的差距引用|
metadata_category:业务、技术或运营元数据类别|
domain:属性允许的值域或业务域|
source:该条内容的输入来源|
quality:所需或观察到的数据质量|
user_role:使用数据的角色|
purpose:数据使用目的|
access_condition:访问允许条件|
retention:数据保留规则|
lawful_basis:数据使用的法规或政策依据|
rule:可验证规则陈述|
validation:校验条件与方法|
exception:例外及其治理方式|
symptom:可观察的数据问题症状|
business_impact:对业务的影响|
root_cause:已验证根因或明确标记的候选根因|
status:该条记录的工作状态|
business_meaning:业务概念的含义|
technical_locator:技术资产定位符|
community:元数据贡献或使用社区|
model:所采用数据模型|
integration:与其他系统的集成约定|
governance:治理责任及变更规则|
attributes:实体的属性定义清单|
identifier:对象标识与唯一性规则|
management_dimension:文档化、参考数据、治理等管理维度|
coverage:所需范围的覆盖判断|
actor:执行活动的主体|
input:活动必需输入|
output:活动输出|
order:明确次序号|
integration_style:集中、混合或统一等组织方式|
contract:数据或元数据交换契约|
synchronization:同步方向、时效和一致性条件|
mechanism:手工、推送或拉取等机制|
responsibility:各方责任及边界|
frequency:执行或交换频率|
protocol:交互协议|
security:安全要求与处理|
cost:成本及估算边界|
data_structure:结构化、半结构化或非结构化类别|
schema_access:所需数据模式访问|
content_access:是否及如何访问实际内容|
business_identity:业务身份定义|
matching:匹配与合并规则|
ownership:数据所有权及责任|
style:选定集成风格|
collaboration:协同维护机制|
pattern:交换模式及来源定义|
producer:数据或消息提供方|
consumer:数据或消息消费方|
consistency:一致性与时效要求|
inbound:入站信息流|
outbound:出站信息流|
storage:数据存储责任与位置|
coexistence:新旧状态共存条件|
priority:优先级及排序依据|
constraint:适用约束|
cohesion:候选边界内聚性及判断依据|
coupling:边界之间的耦合与代价|
interface:公开接口与契约|
data_responsibility:数据读写与所有权责任|
standard:适用标准和版本|
value:度量值或业务价值陈述，依语境声明|
planned_state:已实现或计划等实现状态|
development_resources:开发资源投入|
operations_resources:运营资源投入|
goals:用户群体或业务目标|
touchpoint:客户与服务交互触点|
experience:观察或期望体验|
pain_point:有证据的体验痛点|
outcome:业务或客户成果|
segment:客户或业务分群|
behaviors:观察到的行为|
needs:用户需求|
assumptions:待验证假设|
adm_phase:适用 ADM 阶段|
service_level:服务水准与度量|
parties:交互各方|
interaction:跨方交互及其目的|
business_outcome:企业业务成果|
measure:衡量贡献的指标|
contribution:贡献解释或假设|
skill:技能项或类别|
demand:指定期间的资源需求|
allocation:资源分配|
period:分析期间|
subskill:具体技能子项|
proficiency:四级技能量表下的熟练度|
person:人员或匿名人员标识|
current_proficiency:当前熟练度及证据|
target_proficiency:目标熟练度|
deliverable:架构交付物引用|
work_package:工作包引用|
effort:投入估算及单位|
dependency:依赖对象及方向|
acceptance:验收准则|
duration:活动持续时间及单位|
resource:所需资源|
predecessor:前置活动|
start:计划或实际开始时间|
end:计划或实际结束时间|
milestone:里程碑定义|
reviewer:评审责任人或角色|
year:环境核算年度|
object:核算或分析对象|
lifecycle_stage:资产生命周期阶段|
business_contribution:业务对环境目标的贡献类型|
increase:新增环境影响|
decrease:退役或减少的环境影响|
net:同一边界下的净影响|
selection:措施或选项的选择状态|
reason:接受或处置的理由|
remediation:消除债务的措施|
review_date:计划复评日期|
options:被比较的备选方案|
environmental_criteria:环境评价准则|
tradeoff:环境与其他质量的权衡|
sector:参考政府部门分类|
function:参考功能或实际功能映射|
local_owner:本地责任部门或角色|
reference_domain:参考模型域|
local_mapping:参考概念与本地概念的映射|
abstraction:语境、概念、逻辑或物理层次|
realization:构建块的实现关系与候选|
operating_conditions:可运营状态的明确条件|
work_packages:实现该状态的工作包|
dependencies:实现及运行依赖|
controls:必须持续有效的控制|
rollback:回退条件与方案
'''.strip().split('|'))

def attribute_contract(field):
    number={'weight','score','value','proficiency','current_proficiency','target_proficiency','year','order','level','capacity','availability','demand','allocation','effort','duration','increase','decrease','net'}
    return {'meaning':('对象在本业务范围内的明确名称' if field=='name' else FIELD_LABELS.get(field,'在本工作产品范围中明确定义的 '+field+' 属性')),
            'value_rule':'保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。' if field in number else '使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。',
            'definition_origin':'project-operational-convention-guided-by-cited-source'}

# id | Chinese / English | owner | source locator | kind/renderer | entity | fields | decision | method | misconception
ROWS = r'''
risk-appetite|风险偏好 / Risk Appetite|security|G152 §5.1.3|assessment/assessment|risk_appetite|scope,impact_scale,likelihood_scale,acceptance_boundary,approval_authority|承担多大风险才能实现业务结果？|界定风险范围和风险所有者；记录影响与可能性尺度；定义可接受边界及超限处置；用真实业务场景检验边界|风险偏好不是一条任意高低分线，批准状态需要证据
business-impact-analysis|业务影响分析 / Business Impact Analysis|security|G152 §5.1.4|assessment/assessment|impact_scenario|business_process,loss_type,impact,criticality,time_horizon|安全不足会使哪些业务结果受损？|从关键业务结果识别中断或损失场景；记录影响类型与时间范围；确认关键风险领域；把结果交给风险评估|业务影响分析不定义事件发生的可能性
security-resource-plan|安全资源计划 / Security Resource Plan|security|G152 §5.1.5|report/catalog|security_resource|role,authority,capacity,availability,engagement|架构工作需要哪些安全与风险人员？|从范围和高风险关注点识别能力需求；比较现有安全支持与专职投入；明确角色授权；安排参与与能力缺口措施|资源计划不等于把所有安全职责交给一位架构师
security-blueprint|安全蓝图 / Security Blueprint|security|G152 §5.2|diagram/deployment|security_component|concern,principle,risk,service,scope|愿景如何使利益相关者确信风险可接受？|收集安全关注点；建立业务风险和原则语境；选择高层安全服务与边界；追溯到后续阶段细化要求|愿景蓝图不等于已完成的技术方案或已运行控制
business-attribute-profile|业务属性画像 / Business Attribute Profile|security|G152 §5.2|assessment/assessment|business_attribute|definition,metric,unit,target,owner|安全架构以什么业务价值衡量？|从利益相关者关注点提炼业务属性；定义度量及期望；关联风险和安全需求；检验安全价值主张|采用 SABSA 画像作为起点不表示所有参考属性都适用
security-policy-architecture|安全策略架构 / Security Policy Architecture|security|G152 §5.3.1|diagram/nested-map|security_policy|scope,authority,accountability,policy_level,review_cycle|安全政策如何分层及分配责任？|识别业务安全政策；区分治理层级和领域；明确政策权威与问责；检查政策冲突和连续性联系|政策架构不是防火墙规则列表
security-domain-model|安全域模型 / Security Domain Model|security|G152 §5.3.2|diagram/deployment|security_domain|policy_authority,classification,assets,boundary,federation|哪些资产受同一安全策略管辖？|按相同安全属性与政策分组资产；界定域内政策权威；识别外部责任交换；评估联邦合同与共同对象|视觉容器只有经定义后才能表示安全域，组织部门不自动等于安全域
trust-framework|信任框架 / Trust Framework|security|G152 §5.3.3|diagram/network|trust_party|business_basis,legal_basis,direction,conditions,scope|谁基于什么条件信任谁？|识别业务关系各方；记录业务法律与政策依据；声明单向双向或不存在的信任；限定条件与责任|数字证书可以传递既有信任，不能创造业务信任
business-risk-register|业务风险模型／风险登记册 / Business Risk Register|security|G152 §5.3.4–5.3.5|catalog/catalog|risk|asset,threat,vulnerability,likelihood,impact,owner,treatment,residual_risk|哪些风险需要处置并由谁负责？|识别资产与失败场景；关联威胁脆弱性和损失；按声明方法评估；比较风险偏好；记录处置和剩余风险|业务风险模型和风险登记册是同一工作产品的表达，不重复计数
applicable-legislation-register|适用法律法规登记册 / Applicable Legislation Register|security|G152 §5.3.6|catalog/catalog|legal_obligation|jurisdiction,version,applicability,business_function,data_scope,owner|哪些法规适用于本次架构范围？|识别功能数据和司法辖区；记录适用条款与版本；关联架构要求和责任；安排法规变化复核|法规适用不能仅由系统部署地推断
applicable-control-framework-register|适用控制框架登记册 / Applicable Control Framework Register|security|G152 §5.3.7|catalog/catalog|control_framework|version,selection_reason,scope,mandatory_controls,certification|采用哪些控制框架来应对风险？|从监管认证和风险要求形成候选；比较框架覆盖；界定必须与建议控制；记录选择依据和版本|历史引用的框架版本不是当前项目自动适用的版本
security-services-catalog|安全服务目录 / Security Services Catalog|security|G152 §5.4|catalog/catalog|security_service|definition,objective,owner,operations,consumers,implementation|哪些安全服务实现安全目标？|从控制目标定义安全服务；标识可复用构建块；记录使用与运营信息；连接需求控制和实施|控制框架包含要求，安全服务描述实现安全目标的构建块
security-classification-scheme|安全分类方案 / Security Classification Scheme|security|G152 §5.4|catalog/catalog|security_classification|classification_scheme,criteria,requirements,owner,scope|资产分类将触发哪些安全要求？|声明分类方案；按资产特征分类；映射访问保密和可用性要求；核查资产所有者责任|分类适用于业务能力服务信息和技术等多种资产
data-quality-assessment|数据质量评估 / Data Quality Assessment|data|G152 §5.4；G234 §4.2|assessment/assessment|data_quality_measure|dataset,dimension,metric,unit,threshold,owner,evidence_period|数据质量能否支持业务与风险目标？|确定数据集与质量责任；选定相关维度和可计算定义；使用日志或样本评估；关联业务影响和改进措施|不同质量维度不能无依据地加总成一个精确分数
risk-mitigation-plan|风险缓解计划 / Risk Mitigation Plan|security|G152 §5.6|report/roadmap|risk_treatment|risk,action,owner,due_date,control,expected_residual|如何把风险降至可接受水平？|比较提高控制转移规避延迟补偿等选项；评价新架构带来的风险；安排责任与验证；复评剩余风险|计划中的控制不能被写成已经有效运行
transition-risk-assessment|过渡范围风险评估 / Transition Risk Assessment|security|G152 §5.7|assessment/assessment|transition_risk|state_id,migration_activity,impact,likelihood,mitigation,owner|迁移过程本身会带来什么风险？|界定过渡状态和迁移活动；分析生产环境风险；关联缓解与回退；检查可运营性和控制连续性|目标架构安全不等于迁移过程安全
rollback-plan|回退计划 / Rollback Plan|migration|G152 §5.7|report/roadmap|rollback_step|trigger,decision_owner,prerequisite,data_recovery,sequence,verification|迁移失败时如何恢复可运营状态？|确定回退触发与授权；分析可逆点和数据一致性；排列步骤与依赖；定义恢复验证和演练证据|回退不是仅写恢复备份，应说明业务与数据恢复条件
security-impact-analysis|安全影响分析 / Security Impact Analysis|security|G152 §5.7、5.9|assessment/assessment|security_impact|change,affected_asset,requirement,control,risk,decision|架构变更怎样改变安全与风险？|定位变化对象；沿已知关系查找安全需求控制和风险；区分候选与确认影响；提出复评或新 ADM 迭代建议|图可达只是候选影响，不能自动认定所有对象受损
security-audit-record|安全审计记录 / Security Audit Record|governance|G152 §5.8|report/catalog|audit_finding|criterion,implementation,evidence,result,deviation,owner|实现是否遵循安全政策与要求？|确定评审对象与判据；获取设计配置代码和测试证据；区分符合偏离证据不足；追踪纠正措施|生成审计表不能证明渗透测试或控制运行已经完成
security-training-plan|安全培训与意识计划 / Security Training and Awareness Plan|security|G152 §5.8|report/catalog|training_need|audience,control,competency,activity,evidence,review|哪些人员需要掌握控制的正确使用？|从控制部署配置运营识别技能需要；区分用户与特权人员；安排培训和验证；保存实际记录|计划中的培训不等于完成或达到熟练度
architecture-maturity-model|架构成熟度模型 / Architecture Maturity Model|ea|G203 §2.1–2.3|assessment/matrix|maturity_criterion|element,level,description,evidence_rule,weight|用什么可解释标准评价 EA 能力？|声明选定模型和适用范围；定义要素与级别特征；规定证据及权重；校准评审者理解|ACMM 六级九要素是指南示例，不是所有 TOGAF 项目的统一评级
architecture-maturity-scorecard|架构成熟度评分卡 / Architecture Maturity Scorecard|ea|G203 §2.2–2.3|assessment/assessment|maturity_observation|element,level,evidence,assessment_date,assessor,confidence|当前 EA 实践达到哪些成熟度特征？|按要素获取证据；逐特征评价达成；记录争议和未知；分别报告加权级别与逐级达成比例|加权等级与各级达成百分比是互补结果，不能互相替代
digital-adoption-position|数字技术采用定位 / Digital Adoption Position|ea|G212 §5.1；图5-2|diagram/quadrant|adoption_option|ubiquity,velocity,rationale,scope,tradeoffs|选择怎样的数字技术采用方式？|明确普及度与采用速度；比较 ABCD 四种方式；阐明选择理由和范围；与就绪度结果结合|ABCD 不是由低到高的优劣或成熟度等级
digital-readiness-questionnaire|数字技术就绪度问卷 / Digital Readiness Questionnaire|ea|G212 §5.2、附录A|assessment/catalog|readiness_question|factor,category,statement,scale_anchor,respondent,evidence|如何取得可比较的就绪度观察？|按因素选择问题；声明七级李克特锚点；邀请关键领导者作答并讨论共识；保留原始答复与证据|问卷答案不是客观测量值，需说明参与者与共识过程
digital-readiness-assessment|数字技术就绪度评估 / Digital Readiness Assessment|ea|G212 §5.2–5.4|assessment/assessment|readiness_factor|category,question_ids,rating,anchor,evidence,attention|哪些采用因素需要管理关注？|逐因素汇总有依据的问卷结果；按来源规则识别关注因素；分析其主要后果；形成改进建议|没有来源或用户规则时不创建统一总分合格线
readiness-consequence-analysis|就绪度因素后果分析 / Readiness Consequence Analysis|ea|G212 §5.3；图5-3|diagram/matrix|readiness_consequence|factor,primary_consequence,business_effect,owner,action|缺失因素会如何影响采用结果？|识别不足因素；对照其主要后果；分析多个后果相互作用；指定管理行动及责任|背景重复因素列表不表示全连接依赖，后果未自带概率和严重度
adoption-factor-progression|采用因素递进路线 / Adoption Factor Progression|ea|G212 §5.4；图5-4|diagram/roadmap|adoption_step|factor_category,prerequisite,action,state_id,readiness_evidence|怎样逐步补齐采用短板？|区分基础影响持续三类因素；识别就绪条件；排列措施和责任；记录混合采用路径理由|射线长度和角度不是定量评分，因素层次不等于 ADM 阶段
business-scenario-document|业务场景文档 / Business Scenario Document|vision|G176 §3–4|report/catalog|scenario|problem,environment,objectives,human_actors,computer_actors,requirements|架构究竟为谁解决什么业务问题？|形成并验证前提；采集归一化问题目标参与者环境；建立业务与技术模型；反复评审并记录需求|业务场景不能由单张用例图替代，也不能预设技术答案
scenario-traceability-matrix|业务场景关联矩阵 / Business Scenario Traceability Matrix|vision|G176 §3.2.3|diagram/matrix|scenario_concern|process,stakeholder,human_actor,computer_actor,problem,goal|流程与各关键场景要素是否一致？|以流程为关联焦点；关联相关群体人与计算机参与者问题目标；检查孤立和冲突；反查原始陈述|矩阵关联不等于流程控制顺序或 CRUD
options-decision-matrix|备选方案决策矩阵 / Options Decision Matrix|gap|G176 §12.8|assessment/matrix|option_score|option,criterion,score,weight,evidence,feasibility|哪项候选方案更适合业务问题？|归一化候选方案；比较成本资源贡献和可行性；声明一至五分的优劣方向；必要时加权并检查敏感性|成本原值不能直接当越高越好的评分，权重必须显式
capability-instance-model|能力实例组成模型 / Capability Instance Model|strategy|G233 §6.4；图6-3|diagram/stage-map|capability_instance|capability_type,stage,role,process,application,information|某阶段由什么具体组成实现能力？|从价值阶段识别能力使用语境；引用能力类型；描述实例的人员流程应用和对象；校核跨实例信息流|同一能力的多个实例不等于多个新能力或子能力
capability-increment-analysis|能力增量分析 / Capability Increment Analysis|gap|G233 §7.1–7.2；图7-1、7-2|assessment/stage-map|capability_change|instance,change_kind,baseline,target,rationale,gap|能力实例需要优化整合新建还是退役？|对齐实例基线目标；分类具体变化及理由；聚合应用和业务差距；形成可交付增量|绿色不等于已实现或高成熟度，新建改进退役标签与颜色分开记录
metadata-dictionary|元数据字典 / Metadata Dictionary|data|G234 §3、§5.1|catalog/catalog|metadata_asset|metadata_category,definition,domain,owner,source,quality|元数据资产究竟表示什么？|界定业务技术运营范围；定义条目和域；指定所有权；关联业务需求与技术资产|资产名称相同不保证含义相同，字典不是所有数据值的副本
data-usage-documentation|数据使用文档 / Data Usage Documentation|data|G234 §3、§5.1|report/catalog|data_usage|dataset,user_role,purpose,access_condition,retention,lawful_basis|谁为何在什么条件下使用数据？|从用例识别使用者和目的；记录访问与生命周期条件；关联政策和业务流程；检查用途冲突|存在使用关系不等于已获访问授权
metadata-policy-documentation|元数据规则与政策文档 / Metadata Rule and Policy Documentation|data|G234 §3、§5.1|report/catalog|metadata_policy|scope,rule,authority,validation,exception,version|怎样保证元数据被一致维护？|收集监管和业务规则；形式化验证条件；明确维护责任和例外流程；与质量需求对齐|政策描述与可执行验证规则需分别标识
data-issue-register|数据问题文档／登记册 / Data Issue Register|data|G234 §3、§4.2|catalog/catalog|data_issue|dataset,symptom,business_impact,root_cause,status,owner|哪些数据问题应优先解决？|记录可观察症状与证据；关联受影响数据和用例；分析候选根因；追踪处置和效果|未经验证的根因只能标为假设
business-technical-asset-mapping|业务与技术资产关联 / Business-Technical Asset Mapping|data|G234 §3、§4.3|diagram/network|metadata_asset|metadata_category,business_meaning,technical_locator,owner,source|业务概念落在哪些技术资产上？|识别业务与技术资产身份；定义关联类型与粒度；记录源头和转换；验证覆盖与多义映射|概念相近不等于同一资产，关联不是自动实现关系
metadata-repository-design|元数据存储库设计 / Metadata Repository Design|data|G234 §4.1、§4.3|diagram/deployment|metadata_repository|scope,community,authority,model,integration,governance|元数据如何存储治理和供不同社区使用？|确定用户与元数据范围；比较集中专用与集成存储；设计概念逻辑模型；定义变更校验与交换契约|部署一个存储库不自动建立数据治理
metadata-model|元数据模型 / Metadata Model|data|G234 §4.3；图4-5、4-6|diagram/er|metadata_asset|metadata_category,definition,attributes,identifier,domain,owner|哪些元数据对象和关系足以支撑需求？|从业务需求识别关键资产；建立业务技术运营分类；细化属性域和标识；核查资产关联与生命周期|图4-5的参考资产不是每个项目必须全选的模型
metadata-asset-coverage|元数据资产覆盖矩阵 / Metadata Asset Coverage Matrix|data|G234 §4.3；图4-5|diagram/matrix|metadata_asset|metadata_category,management_dimension,definition,owner,coverage|所需元数据范围是否覆盖管理关注点？|确定三类元数据和四个管理维度；归置资产；检查业务需求所需但缺失的条目；记录裁剪|参考图空格不表示禁止、不存在或无需管理
metadata-validation-workflow|元数据校验工作流 / Metadata Validation Workflow|data|G234 §4.2.2、§4.3|diagram/sequence|metadata_activity|actor,action,input,validation,output,order|谁在何时保证元数据质量？|比较规范式与协作式质量方法；明确创建校验发布变更角色；规定异常和回路；对应质量目标|协作式的最终一致性不等于没有治理
metadata-integration-model|元数据集成模型 / Metadata Integration Model|data|G234 §4.3；图4-7、4-8|diagram/deployment|metadata_repository|integration_style,authority,scope,contract,synchronization,owner|多个元数据源如何协作并避免孤岛？|比较集中混合统一模型；明确各库主次权威；定义交换契约；检查一致性和社区协作|集成组织方式与手工推送拉取采集方式是两个独立维度
metadata-ingestion-options|元数据采集备选方案 / Metadata Ingestion Options|data|G234 §4.3；图4-9|diagram/network|metadata_component|mechanism,responsibility,frequency,protocol,security,cost|选择手工、推送还是拉取元数据？|识别源系统与采集责任；区分控制命令和回传信息；比较人工API代理机制；权衡时效负担安全|三种机制是备选方案，不是三个固定先后阶段
metadata-inference-design|技术元数据推断方案 / Technical Metadata Inference Design|data|G234 §4.3；图4-10|diagram/deployment|inference_source|data_structure,schema_access,content_access,cost,risk,scope|抽取技术元数据需要访问什么？|区分结构化半结构化非结构化；确定可用模式与稳定性；判断是否必须扫描内容；评估成本隐私和风险|采集模式不必然需要读取实际业务数据
customer-mdm-model|客户主数据模型 / Customer Master Data Model|data|G21B §4–5|diagram/er|master_data|business_identity,identifier,source,matching,ownership,quality|怎样形成可复用的客户主数据？|确定客户内核与业务语境；分析源记录身份匹配；定义质量和责任；建立模型与分发关系|统一客户标识不等于无条件合并不同业务语境
mdm-integration-style|主数据集成风格 / MDM Integration Style|data|G21B §5；附录B|diagram/deployment|master_repository|style,authority,collaboration,consumers,synchronization|整合、协作还是集中管理主数据？|比较权威与协作需要；选择整合协作集中风格；明确读写和同步责任；评估演进与迁移|参考集成风格不是指定厂商产品
mdm-exchange-pattern|主数据交换模式 / MDM Exchange Pattern|data|G21B 附录B|diagram/sequence|master_exchange|pattern,authority,producer,consumer,consistency,trigger|主数据交换由哪些应用与责任控制？|声明 PoA 与 PoC 等来源术语；识别权威提供方与消费方；建模请求更新和通知；核对一致性边界|缩写必须随来源定义，不凭名称猜测语义
bi-transition-architecture|BI 与分析演进架构 / BI and Analytics Transition Architecture|data|G238 §3；图3-1–3-4|diagram/deployment|analytics_component|state_id,role,inbound,outbound,storage,coexistence|如何从现有数仓演进到目标分析平台？|描述基线和目标；设计多个可运营过渡；区分入站出站和回写；安排数据及应用迁移依赖|不同状态是同一架构的演进视图，不机械当成独立制品种类
bi-requirements-profile|BI 与分析需求规格 / BI and Analytics Requirements Profile|requirements|G238 §4|report/catalog|analytics_requirement|business_function,statement,verification,priority,source,constraint|分析平台需要满足什么可验证业务要求？|从业务功能识别需求；拆成原子独立陈述；定义验证方式；分离产品约束与业务要求|未取得外部完整需求电子表格时不能声称覆盖其全部条目
microservice-decomposition-method|微服务应用分解方法 / Microservice Decomposition Method|app|G21I §6–7|report/nested-map|service_boundary|business_function,ownership,cohesion,coupling,interface,data_responsibility|应用应按什么边界拆分？|从业务功能和质量目标确定候选边界；检查职责与数据所有权；比较耦合和独立部署代价；记录分解原则和过渡|小服务数量不是微服务架构成功指标
microservice-technical-guidance|微服务技术指南 / Microservice Technical Guidance|tech|G21I §6–7|report/catalog|microservice_guideline|concern,standard,rationale,applicability,verification,exception|哪些技术约束保障微服务实现？|从目标质量选择指南；定义接口运行与治理约束；说明适用与例外；关联合规验证|外部实践补充必须标项目约定，不能冒充指南原文
microservice-value-catalog|微服务价值与资源目录 / Microservice Value and Resource Catalog|app|G21I §7|catalog/catalog|microservice|business_function,value,planned_state,development_resources,operations_resources,owner|已实现和计划服务贡献什么价值？|盘点服务及状态；关联业务功能与价值；记录开发运营资源；评估重复与持续收益|计划服务不能标为已交付，服务数量不等于业务价值
customer-journey|客户旅程 / Customer Journey|business|G20F §5–6|diagram/stage-map|journey_stage|actor,goal,touchpoint,experience,pain_point,outcome|客户如何经历服务并取得价值？|确定客户语境与目标；识别触点和体验阶段；记录证据痛点与期望；连接业务运营和改进|客户旅程不是内部流程图，体验陈述需证据
customer-persona|客户画像 / Customer Persona|business|G20F §5–6|report/canvas|persona|segment,goals,behaviors,needs,evidence,assumptions|为谁设计业务和产品体验？|从研究划分相关群体；归纳目标行为需求；区分观察和假设；检验代表性并链接旅程|虚构人物叙述不能冒充真实用户研究结果
ea-service-catalog|企业架构服务目录 / Enterprise Architecture Service Catalog|ea|G217 附录B–C|catalog/catalog|ea_service|consumer,decision,output,adm_phase,owner,service_level|EA 团队应提供哪些决策支持服务？|选择候选服务；明确消费者决策和成果；映射 ADM 与能力；核对团队容量与服务约定|候选服务不是每个 EA 团队必须提供的服务清单
interoperability-assessment|互操作性评估 / Interoperability Assessment|tech|G217 附录B；G186 附录|assessment/assessment|interoperability_issue|parties,interaction,information,protocol,constraint,evidence|跨系统和组织交换能否满足业务要求？|界定交互各方及业务目的；检查信息含义接口协议；分析组织与技术约束；提出证据支持的改进|网络连通不能证明语义和业务互操作
ea-value-map|EA 与企业价值地图 / EA Value Map|ea|G184 §13|diagram/network|ea_value|service,consumer,business_outcome,measure,contribution,evidence|EA 服务如何为企业创造价值？|明确 EA 服务和业务受益者；建立贡献假设；选择度量与反馈；检查业务周期对齐|相关性或贡献假设不能直接断言为确定收益因果
ea-team-capacity-plan|EA 团队容量计划 / EA Team Capacity Plan|ea|G184 §13|report/roadmap|ea_capacity|role,skill,demand,availability,allocation,period|团队容量能否支撑所选架构服务？|估计服务需求与参与节奏；盘点角色技能和可用量；比较供需；安排招聘发展或裁剪|人数不等于可用容量，技能熟练度不等于工时
architecture-skill-matrix|架构技能／角色矩阵 / Architecture Skill Role Matrix|org|G249 §5；G198 §6|diagram/matrix|skill|category,subskill,role,proficiency,scale_anchor,evidence|每种架构角色需要什么熟练度？|识别相关技能分类；按角色确定目标等级；评价人员证据；形成培训与配置建议|G249 四级熟练度不等于组织成熟度，参考等级可以裁剪
architecture-development-plan|架构人员发展计划 / Architecture Development Plan|org|G249 §5–6|report/roadmap|skill_development|person,role,skill_id,scale_id,task_refs,requirement_refs,current_proficiency,target_proficiency,behavioral_gap,action,success_criteria,reassessment,history,evidence|怎样弥补人员技能缺口？|对齐目标角色与当前技能；区分背景认知通晓专家；选择实践培训或辅导；安排效果验证|参加培训不自动提升为专家等级
architecture-project-wbs|架构项目工作分解 / Architecture Project WBS|workbench|G188 §3.2|diagram/nested-map|architecture_task|deliverable,work_package,owner,effort,dependency,acceptance|怎样把架构成果分解为可管理工作？|明确范围与排除项；按成果分解工作；核对遗漏和重复；指定责任估算与验收|架构项目在该指南限 A–F，不代表所有架构工作都限于 A–F
architecture-project-schedule|架构项目资源与进度 / Architecture Project Resource and Schedule|workbench|G188 §3.2.6–3.2.7|diagram/roadmap|architecture_activity|duration,resource,predecessor,start,end,milestone|架构工作在资源约束下怎样安排？|确定活动依赖与估算依据；比较资源可用量；形成里程碑和滚动计划；分析关键路径与缓冲|没有依赖和工期证据不能宣称算出关键路径
architecture-acceptance-criteria|架构成果验收准则 / Architecture Acceptance Criteria|review|G188 §3.1–3.5|catalog/catalog|acceptance_criterion|deliverable,criterion,verification,reviewer,evidence,status|怎样判断架构成果足以支持决策？|从目标与关注点定义准则；指定检验和评审责任；记录证据及未决项；区分移交批准和生成完成|工件不要求各自成为独立文档，数量不是验收目标
environmental-is-assessment|信息系统年度环境评估 / Annual IS Environmental Assessment|change|G242 §3.7；图3-10|assessment/assessment|environment_measure|year,scope,object,lifecycle_stage,unit,value,allocation,evidence|信息系统的环境影响从何而来？|界定核算边界与生命周期；分对象年度和Scope采集；保留分摊与估算依据；比较多年变化|抵消单列，不能把不同边界和单位直接相加
sustainability-review-canvas|可持续性架构评审画布 / Sustainability Architecture Review Canvas|review|G242 §3.8–3.9；图3-14|diagram/canvas|sustainability_action|business_contribution,year,scope,increase,decrease,net,selection,rationale|方案的环境贡献与措施是否一致？|说明三类业务环境贡献；分别记录新增退役净值；评价措施与选择理由；核对印刷或计算差异|图3-14存在数值疑点，应保留来源值与差异，不能强行消解
environmental-debt-register|环境债务日志 / Environmental Debt Register|change|G242 §4|catalog/catalog|environmental_debt|decision,impact,reason,owner,remediation,review_date|哪些环境代价被推迟处理？|识别设计运营中的环境债务；记录接受理由与影响；安排消除措施；按证据复评|环境债务不是仅有碳排总量，责任和决策也需记录
environmental-decision-log|环境决策日志 / Environmental Decision Log|governance|G242 §3.8–4|catalog/catalog|environmental_decision|options,environmental_criteria,evidence,tradeoff,decision,authority|环境标准怎样进入架构决策？|明确备选与评价边界；比较环境及其他质量属性；记录权衡和决策依据；追溯执行与复评|低环境影响方案是否采用仍取决于明确权衡，不能伪造批准
government-reference-tailoring|政府参考模型裁剪 / Government Reference Model Tailoring|business|G21D §1–12|report/nested-map|government_service|sector,function,service,scope,applicability,local_owner|怎样把政府参考分类映射到实际职责？|区分部门功能服务；选择适用范围并映射本地服务；识别跨部门共享；记录偏差与理由|参考部门分类不是实际组织架构，版本中的部门计数应核对
digital-business-reference-tailoring|数字业务参考模型裁剪 / Digital Business Reference Model Tailoring|business|G21H §2–6|report/nested-map|digital_business_function|reference_domain,function,local_mapping,scope,gap,decision|哪些数字业务功能适用于目标企业？|明确企业目的与参考域；映射现有目标能力；记录缺口与不适用；连接战略分段能力全景|参考模型裁剪不表示全量采用，也不等于最终技术架构
building-block-description|构建块描述 / Building Block Description|gap|G248 §2–3|report/network|abb|definition,abstraction,service,requirements,realization,owner|构建块定义和选择怎样追溯到需求与实现？|描述所需架构服务与边界；区分ABB和SBB；比较候选实现；记录要求、接口与选择依据|ABB不是一个指定技术产品，SBB不能仅按图中的相邻位置推断实现
transition-architecture-model|过渡架构模型 / Transition Architecture Model|gap|G248 §2；图2-2|diagram/roadmap|transition_architecture|state_id,operating_conditions,work_packages,dependencies,controls,rollback|变革中间状态是否可运营且衔接目标？|命名基线过渡目标；描述每个状态的运营条件；关联工作包及实现；检查依赖控制数据一致性和回退|过渡架构不是仅有交付日期的里程碑
'''.strip()

def source_refs(text):
    return [x.strip() for x in text.split('；')]

def base_example(identity, name, etype, fields):
    sample={'scope':'虚构星河零售：在线下单至仓库发运','owner':'虚构订单业务负责人','role':'虚构安全架构师',
            'definition':'在线零售客户订单相关的'+name,'business_process':'订单确认与发运','loss_type':'订单不可用造成履约中断',
            'impact':'高峰时段无法履约，影响当日发运承诺','criticality':'关键：订单在一个工作日内发运','time_horizon':'2026年度迁移期间',
            'impact_scale':'低／中／高，按履约中断与合同影响判断','likelihood_scale':'罕见／可能／频繁，需事故与测试证据支持',
            'acceptance_boundary':'不接受无责任归属且无恢复方案的高履约影响风险','approval_authority':'虚构风险委员会，当前未批准',
            'asset':'客户订单信息','threat':'未授权访问导致订单被修改','vulnerability':'管理访问缺少独立复核','likelihood':'可能（本例假设）',
            'treatment':'采用多因素认证与高权限操作复核','residual_risk':'需在控制验证后复评，当前未知','control':'访问认证和操作审计',
            'state_id':'transition-2026-q4','migration_activity':'在线订单迁移到新履约平台','trigger':'订单一致性校验失败时暂停切换',
            'decision_owner':'虚构发布经理','prerequisite':'保留旧平台可写能力并完成对账','data_recovery':'核对切换窗口内订单与付款记录后恢复',
            'sequence':'停止新写入→订单对账→恢复旧平台→验证订单履约','verification':'复演两笔虚构订单并核对库存付款和发运状态',
            'requirement':'订单不得丢失且一天内发运','rationale':'满足履约连续性与可追溯要求','conditions':'仅限有合同与明确用途的订单处理',
            'classification':'内部受限：包含客户与订单信息','policy_authority':'虚构信息安全负责人','boundary':'企业内订单服务与外部承运商接口',
            'business_basis':'承运商受托履行配送合同','legal_basis':'虚构配送与数据处理协议','direction':'零售商向承运商传递受限订单数据',
            'jurisdiction':'虚构项目适用辖区，需责任方核实','version':'示例2026.1','applicability':'本例订单功能处理客户联系信息',
            'selection_reason':'覆盖订单访问与连续性风险','objective':'保护订单完整性并维持履约','operations':'每日核查审计与备份状态',
            'dataset':'虚构在线订单集','dimension':'完整性','metric':'已确认订单中包含履约必填项的比例','unit':'百分比',
            'threshold':'示例期望100%，需业务方确认','evidence_period':'2026年10月虚构抽样','action':'补齐订单与发运追溯并演练回退',
            'due_date':'2026-12-15','expected_residual':'待演练和控制验证后重新评价','result':'候选，尚未业务验收','evidence':'虚构场景说明，非实测证据',
            'element':'架构治理','level':2,'description':'本例已形成部分书面职责，但证据覆盖尚不完整',
            'assessment_date':'2026-11-01','assessor':'虚构评审小组','confidence':'示例推演，不代表实测结论',
            'ubiquity':'先覆盖在线订单业务线','velocity':'采用逐步迁移以保留回退能力','factor':'变更问责','category':'基础因素',
            'statement':'业务负责人明确承担数字采用的问责','scale_anchor':'七级李克特：按问卷声明解释','respondent':'虚构业务负责人',
            'rating':'同意（虚构回答）','attention':'需补充承运商一侧的责任证据','primary_consequence':'决策缺少问责会导致变更无法落地',
            'factor_category':'基础因素','problem':'订单信息割裂使发运状态无法及时通知客户','environment':'虚构在线商店、仓库和承运商',
            'objectives':'一个工作日内完成发运并通知客户','human_actors':'客户、仓库操作员、客服','computer_actors':'在线商店、订单应用、仓库应用',
            'process':'核对订单并发运','stakeholder':'虚构订单业务负责人','human_actor':'仓库操作员','computer_actor':'仓库应用',
            'goal':'提高履约可靠性','option':'采用分阶段集成方案','score':4,'weight':1,'feasibility':'可利用现有仓库接口，需验证吞吐量',
            'capability_type':'订单履约能力','stage':'发运产品','application':'虚构仓库应用','information':'订单和发运信息','instance':'在线订单发运场景中的履约能力实例',
            'change_kind':'改进','baseline':'人工汇总订单后通知仓库','target':'订单应用自动向仓库推送已确认订单','gap':'缺少订单状态接口及对账控制',
            'metadata_category':'业务元数据','domain':'订单状态：已确认／已发运／已取消','source':'虚构业务场景与需求材料',
            'quality':'定义明确并由业务所有者维护','purpose':'履行客户订单','access_condition':'角色授权且仅访问其职责所需订单',
            'retention':'由本地业务与法规责任方确定，本例未批准','rule':'已发运订单必须有关联发运记录','validation':'校验订单与发运标识对应关系',
            'symptom':'客户看到已付款但无法查询发运状态','business_impact':'客服需人工查询，增加处理时间','root_cause':'候选：订单与发运标识未统一，待核实',
            'business_meaning':'客户购买的产品、数量及履约承诺','technical_locator':'虚构订单应用的订单实体（示意）','community':'订单业务与数据管理团队',
            'model':'订单元数据概念模型','integration':'通过受控接口交换定义和质量规则','governance':'业务所有者批准定义，数据管家维护记录',
            'identifier':'本例以订单业务标识作为候选唯一标识','management_dimension':'文档化','coverage':'本例订单状态已记录；其他范围待评估',
            'actor':'数据管家','input':'待更新订单状态定义','output':'经过校验并发布的新定义','order':1,
            'integration_style':'混合式：业务定义由中央库负责，技术模式保留源权威','mechanism':'源系统推送','responsibility':'源应用维护模式，元数据团队校验接收',
            'frequency':'每日一次及重要变更时','protocol':'项目约定的受控API','security':'认证、最小授权及审计','cost':'需估算连接器维护与源系统负载',
            'data_structure':'结构化订单表','schema_access':'只读取表结构与字段定义','content_access':'本例不需要读取客户订单实际内容',
            'business_identity':'在明确业务语境内识别同一客户','matching':'先按经验证的标识匹配；冲突人工处理','ownership':'虚构客户数据所有者',
            'style':'协作式','collaboration':'客户主数据与销售应用按契约协同维护','pattern':'以本地存储和时效要求选择交换模式',
            'producer':'虚构客户主数据服务','consumer':'虚构订单应用','consistency':'关键身份更新需确认，批量副本单独标记时效',
            'inbound':'订单应用向分析平台提交已完成订单','outbound':'分析平台向业务报表提供聚合结果','storage':'原始订单历史留存于受控分析存储',
            'coexistence':'过渡期间旧数仓与新平台并行，对账后切换报表','business_function':'订单履约分析','priority':'高：支撑当前履约决策',
            'cohesion':'订单确认和状态维护职责内聚','coupling':'库存和付款通过明确接口协作','interface':'确认订单与查询发运状态接口',
            'data_responsibility':'订单服务负责订单状态，仓库服务负责发运状态','concern':'订单完整性与履约连续性','standard':'项目选定标准及版本待核实',
            'planned_state':'计划，尚未交付','value':'降低人工对账并改善客户通知，需后续度量','development_resources':'虚构跨职能团队一组',
            'operations_resources':'虚构运营责任人，容量待估算','touchpoint':'客户查询发运状态页面','experience':'客户能理解订单当前状态与下一步',
            'pain_point':'状态迟延导致重复询问','outcome':'客户收到准确发运通知','segment':'虚构线上零售客户群','goals':'按承诺收到商品',
            'behaviors':'本例假设客户会在发货前查询订单','needs':'准确且可理解的履约信息','assumptions':'该行为尚需真实用户研究验证',
            'adm_phase':'B、C、E','service_level':'在决策节点前提供足够架构证据','business_outcome':'提高履约可靠性',
            'contribution':'架构通过明确信息责任和迁移约束提供贡献，因果待验证','skill':'数据与应用架构追溯','period':'2026年第四季度',
            'subskill':'跨域接口与数据模型分析','proficiency':3,'person':'虚构架构师甲','current_proficiency':2,'target_proficiency':3,
            'deliverable':'本例架构定义文档','work_package':'订单接口与对账控制工作包','effort':20,'duration':10,
            'dependency':'先完成订单身份与状态定义','predecessor':'业务与数据定义评审','start':'2026-11-02','end':'2026-11-13',
            'milestone':'完成候选接口和控制评审','reviewer':'虚构业务与架构评审组','year':2026,'object':'订单相关应用与服务器',
            'lifecycle_stage':'使用阶段','allocation':'按已声明的订单工作负载比例分摊','increase':120,'decrease':100,'net':20,
            'selection':'候选，需结合业务和环境证据作决策','reason':'保障履约同时逐步消除重复处理','remediation':'完成迁移后退役重复任务',
            'review_date':'2027-01-15','sector':'参考模型中的共享服务分类','function':'订单业务与数据支持',
            'local_mapping':'将参考功能映射到本地实际职责并登记不适用项','abstraction':'逻辑','realization':'候选SBB方案，尚未选定',
            'operating_conditions':'新旧订单流可对账且控制持续有效','dependencies':'订单标识、接口和运行责任已明确','rollback':'按回退计划恢复旧订单写入并对账'}
    attrs={f:sample.get(f,'虚构订单案例中需验证的'+FIELD_LABELS.get(f,f)) for f in fields}
    attrs.update({'definition':name+'的虚构零售企业示例','owner':'虚构业务负责人'})
    for field in ['value','weight','score','proficiency','duration','effort','availability','demand']:
        if field in attrs:attrs[field]=2
    for field in ['year']: 
        if field in attrs:attrs[field]=2026
    e={'id':identity+'-example','type':etype,'name':'虚构零售企业：'+name,'attributes':attrs,'evidence':['example-source'],'certainty':'assumed'}
    return {'notice':'虚构示例；字段为项目操作示范，未表示真实项目结论。',
            'sources':[{'id':'example-source','kind':'example','description':'虚构零售企业验收案例'}],
            'entities':[e],'relationships':[],
            'view':{'id':'v-'+identity,'artifact_id':identity,'title':name+'示例','entity_ids':[e['id']],
                    'relationship_ids':[],'analysis':'根据虚构业务材料建立候选结果；待责任人验证输入证据。','legend':'虚构示例／候选；待验证值不作为实际事实。'}}

def build_work_products():
    from additional_capabilities import append_rows
    result=[]
    for row in append_rows(ROWS).splitlines():
        values=row.split('|');assert len(values)==10,(len(values),row)
        identity,names,owner,source,kr,etype,field_text,decision,steps,misreading=values
        zh,en=names.split(' / ',1);kind,renderer=kr.split('/');fields=field_text.split(',')
        w={'id':identity,'artifact_id':identity,'name':zh,'name_zh':zh,'name_en':en,'owner':SKILLS[owner],
           'kind':kind,'renderer':renderer,'notation':renderer,'source_refs':source_refs(source),
           'definition_status':'guide-work-product-with-project-operational-contract','decision':decision,
           'stakeholders':['业务或领域责任人','架构工作利益相关者','相关实施与治理人员'],
           'concerns':[decision,'结论的来源、范围与可验证性'],
           'required_inputs':['范围与五维语境','相关原始业务材料及其定位',*fields[:3]],
           'optional_inputs':['现有架构模型','历史评估或决策','组织特定量表和裁剪规则'],
           'missing_input_policy':'关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。',
           'entity_types':[etype],'relationship_types':['traces_to'],'fields':['name',*fields],
           'attribute_semantics':{f:attribute_contract(f) for f in ['name',*fields]},
           'required_attributes':{etype:fields},'relation_semantics':'traces_to 只表示有说明的追溯；对象含义与更具体关系应依本工作产品定义。',
           'analysis':steps.split('；'),'analysis_steps':steps.split('；'),
           'output':['范围及决策问题','对象／属性／关系','分析结果与理由','来源、假设、未决项','相关制品与交付物引用'],
           'semantic_checks':[misreading,'必需属性具有明确值或被登记为阻断缺口','来源与项目事实、参考内容、假设保持可区分','结论回应本规范的决策问题并可追溯'],
           'checks':[misreading],'misreadings':[misreading],
           'related_deliverables':delivery_for(owner),'example':base_example(identity,zh,etype,fields),
           'implementation_status':{'definition':'source-located','model':'requires-validation','analysis':'method-specified',
                                    'generation':'requires-execution','modification':'requires-execution','review':'requires-execution','visual':'not-evaluated'}}
        result.append(w)
    return result

def delivery_for(owner):
    return {'security':['architecture-definition-document','architecture-requirements-specification'],
            'ea':['organization-model','tailored-architecture-framework','capability-assessment'],
            'vision':['architecture-vision','statement-of-work'],'strategy':['capability-assessment','architecture-roadmaps'],
            'gap':['architecture-roadmaps','solution-building-blocks'],'migration':['implementation-migration-plan'],
            'data':['architecture-definition-document','architecture-requirements-specification'],
            'app':['architecture-definition-document'],'tech':['architecture-definition-document'],
            'requirements':['architecture-requirements-specification'],'business':['architecture-definition-document'],
            'value':['architecture-definition-document','capability-assessment'],
            'org':['organization-model'],'workbench':['statement-of-work'],
            'change':['change-request','capability-assessment'],'governance':['compliance-assessment'],
            'review':['compliance-assessment']}[owner]

PROFILE_ROWS = r'''
capability-classification|business-capability-map|能力分类地图|strategy|nested-map|G211/fig3-2|category,level,definition|战略、核心、支持分类带独立；带内位置不表示顺序
capability-decomposition|business-capability-map|能力分解地图|strategy|nested-map|G211/fig3-3|level,parent,definition|使用明确分解层级；能力不能分解为流程或应用
capability-gap-heatmap|business-capability-map|能力差距热力图|strategy|heatmap|G211/fig5-1|score,scale,target,category|颜色有评价维度和量表；未来不存在能力单独表示
capability-strategy-overlay|business-footprint-diagram|能力与战略足迹|strategy|network|G211 §4|definition,strategic_contribution|战略贡献必须关联实际业务目标及理由
value-stream-definition|value-stream-map|价值流阶段定义图|value|stage-map|G178/fig4-1|order,entry_condition,exit_condition,value_item|有受益者、触发与结果；阶段价值不等于活动清单
value-stream-enabling-capabilities|value-stream-map|价值流阶段与使能能力|value|stage-map|G178/fig4-3|order,level,definition|阶段横向有序；同一能力可支持多个阶段
value-stream-capability-heatmap|value-stream-map|价值流能力差距叠加|value|heatmap|G178/fig4-4|order,score,scale,target|阶段关系与热力评价分别保留
porter-value-chain|value-chain-diagram|主要与支持活动价值链|value|value-chain|G178/figA-1|category,definition,contribution|四类支持活动覆盖五类主要活动；Margin不表示最后阶段
information-concept-network|information-map|信息概念关系网络|data|network|G190/fig2-1|definition,owner|信息概念是业务语义；关系名称必须明确
information-capability-use-modify|information-map|能力使用与修改信息|data|network|G190/fig4-1|definition,operation|能力到信息为修改；信息到能力为使用，图例需保留
information-aggregation-generalization|information-map|信息聚合组合泛化|data|er|G190/figA-1|definition,relationship_kind|关联、聚合、组合和泛化不可仅以相同箭头代替
information-bounded-cardinality|conceptual-data-diagram|有界基数概念关系|data|er|G190/figA-4|definition|每端基数分别保存；1..2不降为任意多个
logical-data-identifiers|logical-data-diagram|逻辑实体属性与标识|data|er|G190/figA-3|attributes,key,domain|属性、标识、可选性、基数明确，物理实现另行追溯
organization-work-network|organization-map|组织工作网络|org|network|G206/fig3-2|category,boundary,definition|内部外部与团队区别；工作联系不推断为汇报关系
organization-capability-overlay|organization-map|组织能力叠加地图|org|network|G206/fig7-2|category,boundary,definition|能力不参与组织汇报层级，映射线不表示弱汇报
business-model-canvas|business-model-diagram|九块业务模式画布|business|canvas|G18A/figA-1|block,detail|保留九块空间结构；多条目及同一对象复用不强行合并
business-model-baseline-target|business-model-diagram|业务模式基线目标比较|business|canvas|G18A/fig7-1|block,detail,state_id|逐块比较变化，状态与批准状态分开
capability-instance-composition|capability-instance-model|能力实例组成图|strategy|stage-map|G233/fig6-3|capability_type,stage,role,process,application,information|实例组成、能力类型、阶段顺序与跨实例信息流分开
capability-change-overlay|capability-increment-analysis|能力变更叠加图|gap|stage-map|G233/fig7-1|instance,change_kind,rationale|新建改进退役与配色是不同属性；必须回链详细模型
application-gap-dependency|application-migration-diagram|应用差距与迁移依赖|gap|roadmap|G233/fig7-2|state_id,change_kind,dependency|工作包与应用变化关联，依赖方向为依赖方到前置方
metadata-business-function-map|functional-decomposition-diagram|元数据业务功能分解|data|nested-map|G234/fig5-1|level,parent,definition|功能嵌套不是流程顺序，角色映射独立表达
metadata-category-coverage|metadata-asset-coverage|元数据资产分类覆盖|data|matrix|G234/fig4-5|metadata_category,management_dimension,definition|三类元数据与四管理维度保留，空格只表示参考图未列
metadata-three-part-solution|metadata-repository-design|元数据方案三要素|data|deployment|G234/fig4-4|scope,model,governance|技术、数据模型与流程共同支撑业务需求；当前本地英文PNG错图
metadata-central-hybrid-unified|metadata-integration-model|元数据集成组织备选|data|deployment|G234/fig4-7|integration_style,authority,scope|集成风格与采集方式两个独立维度
metadata-manual-push-pull|metadata-ingestion-options|元数据采集三种模式|data|network|G234/fig4-9|mechanism,responsibility,frequency,protocol|控制调用与回传信息分开，不把备选机制串成步骤
metadata-inference-structure|metadata-inference-design|技术元数据推断架构|data|deployment|G234/fig4-10|data_structure,schema_access,content_access|结构化模式抽取不必访问真实数据，非结构化扫描需评价风险
risk-security-traceability|business-risk-register|风险与安全追溯模型|security|network|G152/fig5-2|asset,threat,vulnerability,likelihood,impact|保留威胁、损失、风险、控制目标、需求、实施和资产追溯
security-cross-domain|security-blueprint|跨域安全关注点|security|deployment|G152/fig4-1|concern,principle,risk,scope|风险与安全横贯业务数据应用技术，不作为第五个互斥架构域
dtra-adoption-quadrant|digital-adoption-position|ABCD 采用定位象限|ea|quadrant|G212/fig5-2|ubiquity,velocity,rationale|横轴普及度纵轴速度；四种方式不表示优劣等级
dtra-factor-consequence|readiness-consequence-analysis|因素与主要后果矩阵|ea|matrix|G212/fig5-3|factor,primary_consequence|每个缺失因素对应主要后果，背景重复列表不形成全连接
dtra-factor-progression|adoption-factor-progression|因素递进采用路线|ea|roadmap|G212/fig5-4|factor_category,prerequisite,action|基础影响持续因素分层，射线不作精确评分
acmm-elements-levels|architecture-maturity-model|ACMM 要素级别矩阵|ea|matrix|G203 §2.2–2.3|element,level,description|六级九要素示例，权重与达成规则显式
acmm-scorecard|architecture-maturity-scorecard|ACMM 证据评分卡|ea|assessment|G203 §2.2–2.3|element,level,evidence|分别报告加权等级与达成比例，不能自造权重
mdm-consolidation-collaboration-central|mdm-integration-style|客户主数据集成风格|data|deployment|G21B/fig6-1|style,authority,collaboration|整合协作集中描述主记录与应用职责，不是强制技术路线
bi-baseline-transition-target|bi-transition-architecture|BI 基线多过渡与目标|data|deployment|G238/fig3-1|state_id,role,inbound,outbound|四个状态分别表达且可运营，入站出站回写区分
ea-skill-role-proficiency|architecture-skill-matrix|技能角色熟练度矩阵|org|matrix|G249 §5表5-1、5-2|category,subskill,role,proficiency|四级熟练度含锚点；不能与成熟度等级混淆
annual-environmental-accounting|environmental-is-assessment|年度环境评估模板|change|assessment|G242/fig3-10|year,scope,object,unit,value,allocation|六类核算对象、生命周期、Scope与抵消分开，比较2–3年
sustainability-architecture-canvas|sustainability-review-canvas|环境架构评审画布|review|environmental-review|G242/fig3-14|block|逐项表达业务判断、两年Scope碳表和五项措施；保留原始数值与印刷差异
sustainability-causal-loop|environmental-is-assessment|数字增长因果回路|change|causal|G242/fig1-2|polarity,loop_type,definition|正负号表示变化方向，强化与平衡回路不能混淆
sustainability-culture-quadrant|environmental-decision-log|数字节制文化四维图|change|quadrant|G242/fig3-2|category,definition|无坐标轴、无高低，无序并列四维围绕共同目标
transition-building-block-trace|transition-architecture-model|过渡架构与工作包追溯|gap|roadmap|G248/fig2-2|state_id,definition,dependency|目标可成为下一轮基线；每端基数和反向读法独立
building-block-content-model|building-block-description|构建块内容元模型|gap|network|G248/fig3-1|definition,abstraction,realization|视觉包含不自动成为组成，逻辑物理与ABB/SBB实现分开
'''.strip()

def profile_example(p, products):
    from capability_examples import specialize
    return specialize(p, products, base_example)

def build_profiles(products):
    profiles=[]
    for w in products:
        p={'id':w['id']+'-default','artifact_id':w['id'],'name':w['name_zh'],'name_zh':w['name_zh'],'owner':w['owner'],
           'renderer':w['renderer'],'source_refs':w['source_refs'],'required_attributes':w['required_attributes'],
           'checks':w['semantic_checks'],'definition_status':'project-operational-view',
           'template':{'source_verified':False,'layout_notes':'按工作产品属性组织；来源无直接对应图时为项目补充模板。'}}
        p['example']=profile_example(p,products);profiles.append(p)
    for row in PROFILE_ROWS.splitlines():
        pid,artifact,name,owner,renderer,source,attrs,check=row.split('|')
        p={'id':pid,'artifact_id':artifact,'name':name,'name_zh':name,'owner':SKILLS[owner],'renderer':renderer,
           'source_refs':[source],'required_attributes':attrs.split(','),'checks':[check],
           'decision':'以'+name+'支持业务决策并保留来源表达的关键语义。',
           'template':{'source_verified':False,'source_figure':source if '/' in source else None,'layout_notes':check,
                       'review_status':'source-located-awaiting-template-validation'},
           'definition_status':'source-derived-view-with-project-construction-rules'}
        if renderer=='canvas':p['template']['blocks']=['关键伙伴','关键活动','关键资源','价值主张','客户关系','渠道','客户细分','成本结构','收入来源'] if 'business-model' in pid else ['业务贡献','环境核算','架构措施']
        if renderer=='nested-map':p['template']['bands']=['战略','核心','支持']
        p['example']=profile_example(p,products);profiles.append(p)
    from proficiency_contract import collaboration_profile, assignment_profile
    profiles.extend([collaboration_profile(), assignment_profile()])
    return profiles

METHOD_ROWS = r'''
scenario-elicitation|业务场景前提验证与归一化|vision|G176 §3.2–3.3|business-scenario-document|前提、访谈与问题材料|拆分陈述；亲和归类；保持原始到归一化映射；验证前提；形成需求|前提未经检验时不能当业务事实
option-weighted-decision|备选方案评价|gap|G176 §12.8|options-decision-matrix|候选方案、准则、分值、显式权重|按1最差5最佳校准分值；记录证据；计算加权比较；检查权重敏感性|成本量不能直接当越高越好的分值
business-risk-assessment|业务风险评估|security|G152 §5.3.4–5.3.5|business-risk-register|资产、威胁、脆弱性、影响及可能性依据|建立风险场景；声明定性或定量规则；与风险偏好比较；关联处置|概率未知不能自行代入统一乘法
business-impact-method|业务影响分析|security|G152 §5.1.4|business-impact-analysis|业务结果、关键活动、损失类型及时间范围|识别失败影响；评价业务关键性；形成风险领域；供风险评估使用|影响不含事件发生可能性
acmm-maturity-assessment|ACMM 成熟度评价|ea|G203 §2|architecture-maturity-scorecard|模型、要素特征、证据、权重或达成规则|按六级九要素示例裁剪；逐特征评价；分别报告加权等级与级别达成比例|无显式权重与规则不计算统一总分
dtra-readiness-method|DTRA 就绪度评价与后果|ea|G212 §5、附录A|digital-readiness-assessment|七级问卷、因素、参与者与共识证据|逐因素评估；识别管理关注；分析主要后果；安排因素递进|不自造统一总分通过线，采用类型不是成熟度
capability-decomposition-method|能力定义与分解|strategy|G211 §3|business-capabilities-catalog|业务对象、结果、范围及既有能力|稳定命名；分同层粒度；检验分解覆盖；保持组织和实现独立|流程步骤不作为子能力
capability-instance-gap-method|能力实例增量分析|gap|G233 §6–7|capability-increment-analysis|阶段、能力实例、基线目标与实现组成|对齐类型实例；比较人员流程应用数据；分类优化整合新建退役；组织可交付增量|名称相同不等于同一实例
value-stream-definition-method|价值流定义与能力使能|value|G178 §3–4|value-stream-map|受益者、触发、阶段和价值成果|确定最终价值；定义阶段进入退出；关联使能能力；识别阶段差距|价值链与价值流用途和结构不同
metadata-requirement-method|元数据需求与范围分析|data|G234 §4.2–4.3|metadata-model|法规、用例、数据问题和数据集|自上而下或自下而上引出需求；定义类别质量；限定资产范围；形成概念逻辑模型|参考资产清单不是强制全选
metadata-integration-tradeoff|元数据集成与采集权衡|data|G234 §4.3|metadata-integration-model|权威源、社区、时效、安全和资源限制|比较集中混合统一；独立比较手工推送拉取；定义协作契约；评估代价|组织模型和采集机制不能混为一维
mdm-identity-analysis|客户主数据身份与集成分析|data|G21B §4–5、附录B|customer-mdm-model|客户源记录、业务身份、权威与质量要求|分析内核客户概念；明确匹配合并；选择集成风格；定义交换和治理|统一客户视图不是无条件合并所有记录
bi-transition-method|BI 与分析演进规划|data|G238 §3|bi-transition-architecture|现有平台、目标需求、数据流与迁移约束|对齐状态；设计多过渡共存；区分入站出站回写；验证运营与迁移依赖|参考目标平台不直接指定厂商
microservice-boundary-method|微服务边界与价值分析|app|G21I §6–7|microservice-decomposition-method|业务功能、质量目标、数据所有权与运营约束|比较边界；评价独立性和耦合；定义技术指南；记录服务价值与资源|更多更小服务不自动提供价值
architecture-role-skill-assessment|角色技能差距评估|org|G249 §5；G198 §6|architecture-skill-matrix|角色目标、四级锚点、人员能力证据|按技能角色比较目标与现状；识别差距；规划配置发展；验证效果|熟练度、团队容量和组织成熟度分开
architecture-project-scheduling|架构项目分解与排程|workbench|G188 §3.2|architecture-project-schedule|成果范围、活动、依赖、工期与资源|按成果分解；估算活动；安排资源和里程碑；在完整输入下分析关键路径|不完整依赖不能支持确定关键路径
environment-lifecycle-accounting|信息系统环境评估|change|G242 §3.7；图3-10|environmental-is-assessment|年度对象、生命周期、Scope、单位、分摊和因子|建立边界；分别核算；保留估算不确定性；比较多年变化|抵消与新增退役净值不能混算
sustainability-option-review|可持续性方案评审|review|G242 §3.8–4|sustainability-review-canvas|业务贡献、环境数据、措施与评价规则|记录新增退役与净值；比较措施；保留权衡；记录债务和复评|原图印刷矛盾保留证据，不静默改数
reference-model-tailoring|参考模型裁剪|workbench|G21D §1；G21H §6；G248 §2|government-reference-tailoring|本地范围、参考分类、职责与约束|识别适用结构；映射本地概念；记录不适用与缺口；定义后续验证|参考分类不是项目实际组织或部署事实
'''.strip()

def build_methods():
    methods=[]
    for row in METHOD_ROWS.splitlines():
        mid,name,owner,source,product,inputs,steps,check=row.split('|')
        methods.append({'id':mid,'name':name,'owner':SKILLS[owner],'source_refs':source_refs(source),
                        'required_inputs':inputs.split('、'),'analysis_steps':steps.split('；'),'output_work_products':[product],
                        'checks':[check],'missing_input_policy':'记录阻断缺口；无明确规则不计算数值或形成确定结论。',
                        'definition_status':'source-method-with-project-operational-steps','implementation_status':'specified-awaiting-behavioral-validation'})
    calculators={'option-weighted-decision':'preference-weighted-decision','dtra-readiness-method':'dtra-factor-review',
                 'acmm-maturity-assessment':'maturity-weighted','business-risk-assessment':'risk-explicit-rule',
                 'environment-lifecycle-accounting':'environmental-delta'}
    for method in methods:
        if method['id'] in calculators:
            method['calculator_id']=calculators[method['id']]
            method['implementation_status']='operational-steps-with-explicit-input-calculator'
        from proficiency_contract import method_contract
        method_contract(method)
    return methods

def main():
    products=build_work_products();profiles=build_profiles(products);methods=build_methods()
    from building_block_contract import apply_contract
    apply_contract(products,profiles)
    relation_registry={**json.loads((ROOT/'relationships.json').read_text())['relationships'],
                       **json.loads((ROOT/'metamodel.json').read_text()).get('relationships',{})}
    for w in products:
        related=[p for p in profiles if p['artifact_id']==w['id']]
        default=next(p for p in related if p['id']==w['id']+'-default')
        w['example']=default['example']
        w['required_attributes']=default['required_attributes']
        w['fields']=list(dict.fromkeys(w['fields']+[f for fs in w['required_attributes'].values() for f in fs]))
        w['attribute_semantics']={f:attribute_contract(f) for f in w['fields']}
        w['entity_types']=sorted(set(w['entity_types']) | {e['type'] for p in related for e in p['example']['entities']})
        w['relationship_types']=sorted(set(w['relationship_types']) | {r['type'] for p in related for r in p['example']['relationships']})
        w['relationship_definitions']={r:relation_registry[r] for r in w['relationship_types'] if r in relation_registry}
        w['relation_semantics']='使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。'
    data={'schema_version':'2.0','notice':'原70项名称与新增指南工作产品、视图变体和分析方法分别登记；数量不得相加为正式TOGAF制品总数。',
          'work_products':products,'profiles':profiles,'analysis_methods':methods,'figure_profiles':[]}
    (ROOT/'capabilities.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    refs=ROOT/'references/capabilities';refs.mkdir(parents=True,exist_ok=True)
    for w in products:
        text='# '+w['name_zh']+' / '+w['name_en']+'\n\n'
        text+='本规范的用途来自指南；字段、模型及输出结构是项目操作约定，不能替代缺失的正式标准定义。\n\n'
        text+='来源：'+ '；'.join(w['source_refs'])+'。主责：'+w['owner']+'。\n\n'
        for heading,key in [('决策与关注点','decision'),('必需输入','required_inputs'),('可选输入','optional_inputs'),('信息不足处理','missing_input_policy'),('对象与属性','fields'),('分析方法','analysis_steps'),('输出结构','output'),('质量检查与常见误读','semantic_checks'),('交付物组装','related_deliverables')]:
            value=w[key];text+='## '+heading+'\n\n'+('\n'.join('- '+str(v) for v in value) if isinstance(value,list) else value)+'\n\n'
        text+='## 元素及关系语义\n\n主体类型：'+', '.join(w['entity_types'])+'。'+w['relation_semantics']+'\n\n'
        text+='|属性|含义|值规则|\n|---|---|---|\n'
        for field,rule in w['attribute_semantics'].items():text+='|'+field+'|'+rule['meaning']+'|'+rule['value_rule']+'|\n'
        text+='\n按对象类型应用的必需属性（附加字段不强制适用于全部参与对象）：\n\n```json\n'+json.dumps(w['required_attributes'],ensure_ascii=False,indent=2)+'\n```\n\n'
        text+='|关系|起点类型|终点类型|含义|\n|---|---|---|---|\n'
        for relation,rule in w['relationship_definitions'].items():
            text+='|'+relation+'|'+', '.join(rule['source_types'])+'|'+', '.join(rule['target_types'])+'|'+rule['meaning']+'|\n'
        text+='\n'
        text+='## 完整可编辑示例片段\n\n示例需要宿主模型提供五维 context；所有对象与关系在片段中完整引用，来源为虚构 example。\n\n```json\n'+json.dumps(w['example'],ensure_ascii=False,indent=2)+'\n```\n'
        (refs/(w['id']+'.md')).write_text(text)
    profile_refs=ROOT/'references/profiles';profile_refs.mkdir(exist_ok=True)
    for p in profiles:
        text='# '+p['name']+'\n\n'
        text+='规范 ID：'+p['id']+'。制品族：'+p['artifact_id']+'。主责：'+p['owner']+'。\n\n'
        text+='来源：'+'；'.join(p['source_refs'])+'。来源结构模板尚未完成全面核验，source_verified=false。\n\n'
        text+='## 构图与语义\n\n构图族：'+p['renderer']+'。'+p['template']['layout_notes']+'\n\n'
        text+='reference 保留来源可证实的关键结构，adaptive 适配本地业务；两者均须检查对象、关系、属性和图例的表达完整性。\n\n'
        text+='## 质量检查\n\n'+'\n'.join('- '+c for c in p['checks'])+'\n\n'
        text+='## 属性要求\n\n```json\n'+json.dumps(p['required_attributes'],ensure_ascii=False,indent=2)+'\n```\n\n'
        text+='## 完整可编辑示例片段\n\n本片段为虚构业务示范；由宿主模型提供五维context，生成不表示业务评审通过。\n\n```json\n'+json.dumps(p['example'],ensure_ascii=False,indent=2)+'\n```\n'
        (profile_refs/(p['id']+'.md')).write_text(text)
    method_refs=ROOT/'references/analysis-methods';method_refs.mkdir(exist_ok=True)
    for m in methods:
        text='# '+m['name']+'\n\n'
        text+='方法 ID：'+m['id']+'。主责：'+m['owner']+'。来源：'+'；'.join(m['source_refs'])+'。步骤与输出结构是本技能的操作约定。\n\n'
        text+='## 输入\n\n'+'\n'.join('- '+v for v in m['required_inputs'])+'\n\n'
        text+='## 实际分析步骤\n\n'+'\n'.join(str(i+1)+'. '+v for i,v in enumerate(m['analysis_steps']))+'\n\n'
        text+='每一步保留输入、转换与结果的追溯。先进行业务判断并记录理由，再把对象和关系写入模型；脚本只在已给出完整规则时计算。\n\n'
        if m.get('calculator_id'):
            text+='## 显式规则计算入口\n\n模型 `analyses` 条目的 `method` 使用 `'+m['calculator_id']+'`，并提供相应规则、量尺和输入引用。执行 `python scripts/analyze.py model.json --evaluate <analysis-id>`；该命令相对于共享工具目录。计算器只执行已声明规则，不代替证据、方案权衡或批准。输入结构与完整虚构案例见 [analysis_cases.py](../../tests/analysis_cases.py) 和 [评价操作手册](../assessment-handbook.md)。\n\n'
        text+='## 输出与评审\n\n'
        for product in m['output_work_products']:
            w=next((w for w in products if w['id']==product),None)
            if w:text+='- ['+w['name_zh']+'](../capabilities/'+product+'.md)\n'
            else:text+='- '+product+'（见既有覆盖索引）\n'
        text+='\n'+'\n'.join('- '+v for v in m['checks'])+'\n\n'+m['missing_input_policy']+'\n\n'
        text+='修改分析时保留范围、模型版本和稳定 ID，并对输入变化重算或重评。评审分别核对事实证据、方法适用性、运算及结论，不能仅检查文件生成成功。\n'
        (method_refs/(m['id']+'.md')).write_text(text)
    print(json.dumps({'new_work_products':len(products),'view_profiles':len(profiles),'analysis_methods':len(methods)},ensure_ascii=False))

if __name__=='__main__':main()
