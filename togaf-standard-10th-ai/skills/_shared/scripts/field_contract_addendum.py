"""Reproducible, project-authored operational definitions for missing fields.

Meanings reuse the existing guide-summary profiles where present. The rules below
are explicit project constraints, not claims of normative TOGAF field syntax.
This module returns data; it never writes registries or touches source knowledge.
"""
import copy

# S nonblank text; A stable ID list; D structured record; T text or structured
# record; L text or list; R record list; N nonnegative quantity; I positive integer; B boolean.
# Every row is an explicit field rule, not a keyword-to-assertion mapping.
RULES = '''
ABF|S|单一原子业务功能；写清业务结果和边界，不能以服务名代替功能
analysis_result|D|确定性审查结果与带ID缺口；由本方法明确输入重算，输出存在不等于治理批准
raw_material_refs|A|完整原始业务材料ID列表；须能检索随包原料，不以分析结果循环充当业务事实
ADM_phase|L|ADM阶段标识；同一服务可跨阶段，项目支持活动不宣称原图唯一归属
CRUD_ownership|T|按主数据对象或属性列C/R/U/D操作责任；冲突权威须保留待裁决
action|T|补证或改进行动；记录责任方、触发或期限及未关闭事项
answer|S|逐题文字回答；未知和不适用须有理由，不转换为默认零分
applies|S|交付特征的适用判断；仅yes/no/unknown，观察不充分选unknown
architecture_state_ref|S|相关架构状态的外部引用；不能自动视作当前实体state_id或已实现状态
assessment|T|本轮方案假设的检验结果；区分观察、推论和未验证内容
asset_id|S|风险资产稳定标识；同一范围唯一，重命名不改变身份
authority|T|有权作出本项决定的责任主体；列授权范围，不能把执行者当批准方
availability_need|T|资产可用性需求；列服务时段、允许中断与恢复依据，不预设统一等级
boundary_id|S|环境核算边界标识；同一比较或汇总须引用同一边界定义
budget|T|经费额度或未知状态；已知金额须币种、周期和批准依据，不以缺失当零
business_case_ref|S|本业务属性对应的业务论证引用；应可定位价值、风险或成本依据
business_objects|L|支撑BI用途的业务对象；先写业务身份与粒度，不直接替换为技术表名
business_purpose|S|本数据价值链层服务的业务用途；不能仅写存储产品或技术动作
business_use|T|分析模型服务的业务决策与消费者；注明人工建议或自动执行边界
capacity|T|范围内资源容量；数值须单位、时段、需求口径及来源，不推算未给资源
claim|T|分析模型结果主张；已测、计划和假设分开，示例试验不冒充生产价值
companion_sheet|T|配套BI需求表的取得和阅读状态；未取得不能声明已覆盖官方全集
competency|S|来源胜任力名称；运营与运营管理变体保留原行来源，不擅自合并
completeness_claim|S|需求集合覆盖边界；区分项目局部、示例与经核实配套全集
component_role|S|组件在产品结构中的职责；不把部署位置或组织职责当作组件身份
confidentiality_need|T|资产保密需求；说明受限信息、可访问角色及泄露影响的分类依据
conflicting_features|A|冲突交付特征的来源ID集合；只能引用已评估特征，不能按多数票消除冲突
consequence|T|诊断回答对C-MDM运营和决策的影响；与改进行动分列
consumers|T|逐消费者的供数与切换安排；保留旧供数、双供数和验证状态，不以平台已建代替切换
context|S|服务的DPBoK组织语境；独立于成熟度、审批状态和TOGAF架构域
context_kind|S|胜任力语境的分类依据；说明为组织规模语境而不是评分或成熟度级别
control_ref|L|实现控制目标的控制记录引用；控制目标不等同控制已执行
controls|T|微服务治理可执行控制；逐项列控制活动、责任和验证证据，政策声明不能代替执行
corrective_action_trigger|T|业务属性纠正触发条件；以偏差、发生频率或成本阈值关联明确处置
cost_and_return|T|微服务成本与收益依据；缺成本、收益或时间窗时保留未知，不计算ROI
cost_basis|T|BI阶段成本的项目依据；双份存储不推出总成本翻倍，未计费用须列缺口
coverage_status|S|参考功能覆盖结论；区别证据覆盖、计划、未知和附理由的不适用
criteria_scores|D|选项逐准则评分；每项须量表与依据，不适用于SBCE或交付风格定性判断
criticality|T|对象对业务连续性的关键程度；声明量表和损失依据，不无来源赋高低分
current_evidence|T|现有胜任力的实际观察；培训计划不能当已具备能力的证据
customer_segment|L|子运营模型服务的客户细分；给出业务身份与排除边界
data_access|T|BI用途数据的访问与隐私约束；注明角色、使用目的及限制，不能默认公开
data_flows|T|各BI态源到目标的数据流；标清清洗后、原始流和元数据，方向不能由排版推出
data_quality|T|模型训练与生产数据的质量及语义；样本、时间窗和缺测分开记录
date|S|决策记录日期；使用ISO 8601日历日期，不能以计划日期冒充已决定日期
dbrm_domain|S|DBRM域名称；数字、战略、结构、运营独立于TOGAF四架构域
dbrm_domain_id|S|DBRM参考域稳定ID；同名域仍按来源ID区分
decision|T|待作或已作的业务决定；写问题、选项与结果边界，建议不自动成为批准
decision_consequence|T|微服务准备度判断对采用或试点的限制；补证前不得把候选判断当就绪
decision_owner|S|本轮SBCE保留、淘汰或重开决定的责任人；不推定拥有正式批准权
decision_reason|S|淘汰或重开的明确原因；须关联本轮新增证据，不允许无理由恢复被淘汰方案
decision_status|S|决定的业务状态；candidate/planned/pending/approved/rejected/unknown，approved另需授权证据
definition|S|参考节点的完整业务定义；保留排除边界，不由标签扩展原文含义
dependencies|L|本地职责映射的项目依赖；参考目录父子层级不自动形成执行依赖
dependency|L|里程碑前置依赖ID；列清外部依赖与未满足条件，不能把时间相邻当依赖
dpbok_context|S|DPBoK I–IV语境标识；不是成熟度分数，不以规模断言能力已具备
due_date|S|里程碑计划到期日；使用ISO 8601日历日期，变更须保持依赖与退出条件一致
element|S|DBRM原要素名称；保留参考身份，不直接当本地已部署组件
element_id|S|DBRM参考要素稳定ID；与域ID一起定位，不能按名称合并异义要素
emergence|S|EA服务在语境中的出现或加深；N首次/P此前/D加深，未引入另明确记录
end|S|项目计划结束日期；使用ISO 8601日历日期，与start的顺序须人工复核
equipment_class|S|设备业务或技术分类；引用分类规则，不以设备名称自行推断分类
event_time|S|威胁事件发生时点或窗口；区分已观察、推测和未知时间，不伪造事件记录
evidence|L|威胁事件支持证据的来源引用；不能以风险评估结论循环证明事件事实
evidence_detail|T|实际观察的证据定位与时点；缺证据明确未知，摘要不能冒充真实批准
evidence_ref|L|控制测试证据的稳定引用；须可定位记录，测试计划不能代替执行结果
evidence_refs|A|本项判断使用的来源ID集合；至少一项，引用存在性不证明内容正确
evolution_kind|S|架构演进种类；仅baseline/transition/target，与审批和实施状态独立
exit_criteria|T|里程碑退出条件；列可核实结果、验收责任与证据，日期到达不等于满足
feature_id|S|来源交付特征的稳定ID；逐原表特征评估，不按名称匹配新增评分项
feedback|T|治理持续监督与纠偏；注明观察信号、反馈对象、责任及后续行动
frequency_or_cost_threshold|T|偏差频率或处置成本阈值；数值须周期、币种或单位及项目批准口径
function|S|BI需求涉及的功能子系统；不是泛指整套技术系统，必须明确功能边界
gap|T|未覆盖或未验证事项；记录影响与后续补证，不把未知写成已通过
gap_action|T|参考功能覆盖不足或不适用的处置；保留原因、责任方及下一步
generated_tonnage|N|核算期内磷石膏产生量；单位吨、非负，期初堆存不得计为当期产生
goal|S|本轮SBCE共同业务目标；方案比较必须使用同一目标和约束范围
goal_reference|T|BI用途关联的参考目标ID与源行；参考目标不证明本地目标已实现
golden_record|T|黄金记录的可信范围与用途；分析可用不等于运营写回已授权
historical_policy|T|历史主数据的保留与解释规则；历史用途和当前真值分离，不能无痕改写
holder_ref|L|技能持有人或角色的稳定引用；未评估人员不能据此视为已具备能力
hypothesis|S|本轮候选方案的可检验假设；说明期待结果和检验边界，不以结论替代假设
impact_scope|T|参考裁剪或映射变更影响的本地范围；跨组织影响不得隐去
implementation_ref|L|参考功能对应的本地实现或计划引用；unknown不是已实现证据
implication|T|本子运营模型选择对关联模型的影响；逐依赖说明，不能按表邻接推断
incremental_benefit|T|BI当前阶段相对前态新增的业务收益；候选价值与已观测收益分开
input_refs|A|本数据价值链层的输入ID；外部输入注明出处，不能凭连线猜数据来源
integrity_need|T|资产完整性需求；列容许误差、修改权限和损坏影响的判断依据
iteration|I|SBCE评审轮次；正整数，同一option_id每轮唯一，按轮次保留历史
judgment|S|微服务准备度定性判断；记录理由和未知，不自动映射成熟度分数
key_comparison|T|候选主数据记录的键和属性比较；未知与冲突保留，禁止仅凭相似名称合并
known_gap|T|BI阶段尚存能力或运营缺口；双系统代价与不可运营条件须显式保留
layer_kind|S|BI价值链语义层；source/raw/prepared/information/business-view，不是强制物理部署
legacy_requirement_coverage|D|逐旧需求ID登记覆盖验证状态；verified才表示已核实，计划、保留旧服务、未知均不支持退役
lifecycle|T|用途或模型从设计到维护的生命周期；列业务和技术责任，发布计划不能当实际运行
likelihood_scale|T|威胁事件可能性量表与锚点；没有数据不填概率，业务影响不能替代发生可能性
lineage|T|数据、特征、模型、消费者和观测的血缘；区分版本，不能仅用名称串联
linked_submodels|A|显式相互约束的运营子模型ID集合；不代表组织层级或自动生成关系
local_depth|T|EA服务在D语境增加的活动或范围；不能仅重复“加深”而无本地说明
local_evidence|L|本地业务材料或观察的稳定引用；参考表行不能证明本地实施存在
local_mapping|T|参考节点到本地职责的候选映射；未评审保持候选，不当作组织事实
local_mapping_status|S|本地映射状态；候选、未评估、已核实须区分，与源表转录核实独立
local_object_ids|A|本地对象稳定ID集合；允许多对多，不能由参考分类自动创造本地对象
local_roles|A|胜任力对应的本地责任角色ID集合；来源胜任力不是岗位已配齐证据
maintenance_plan_ref|L|设备维护计划引用；关联版本与有效期，未执行计划不当作设备可用证据
manual_arbitration|T|匹配冲突的人工裁决办法；谁核对哪些证据并如何作决定须明确
mapping_origin|S|映射来源身份；区分project-observation/project-proposal/source-verified，后者须独立原文核实
mapping_type|S|政府参考裁剪映射类型；覆盖、排除与未知分开，排除须写理由
mastership|T|按对象、属性与业务范围声明主控系统；跨源冲突须记录权威及例外
matching_basis|T|主数据匹配推理依据；引用比较结果及规则，评分值本身不是匹配真值
meaning|S|EA服务N/P/D符号的解释；N首次/P此前/D加深，不解释为成熟度分数
measure|T|模型运营度量定义；列单位、时间窗、阈值来源、观测与缺测，未给阈值不授予通过
measure_period|T|数据质量测量时间窗；明确起止与时区或采样周期，不能混合不同窗口结果
measurement_approach|T|业务属性度量方法；定义样本、算法、单位、周期与观察来源，不任意加权
measures|T|运营子模型成本、前置时间、质量、灵活性、敏捷性度量；各有独立依据，不合成无来源总分
merge_lineage|T|主数据合并血缘；保留源ID、黄金记录ID、版本和实际或候选操作，必须可追溯回原值
metadata_lineage|T|数据、规则、作业与业务用途的元数据血缘；保留方向和版本，不当作系统部署链
method_ref|S|评估结果采用的方法引用；与评分口径及版本可定位关联
metric|T|业务用途度量；列定义、单位、周期、基线、目标和实际观测，未知不作为零值
model_ref|T|分析模型与版本引用；同名不同版本分开，模型存在不等于已发布运行
monitoring|T|分析模型监控安排；覆盖准确性、漂移、技术、安全与使用信号，并注明缺口
needed_competency|T|本地工作需要的胜任力；与已有证据区分，避免把培训需求写成能力事实
new_evidence_refs|A|本轮淘汰或重开使用的新增证据ID；不能只重用旧结论而无新证据
next_review|T|胜任力复评日期或触发事件；未安排须标缺口，不默认持续有效
next_trigger|T|主数据下一演进态的触发条件；不是凭时间到期自动迁移
objective_statement|S|控制目标要实现的安全结果；不是产品清单或已执行控制声明
observation|T|范围内实际观察或明确未取得材料；事实、推论和行动不得混写
organization_type|I|采用就绪类型1/2/3；解释性类别，表示满足列明因素层，不是实施步骤或已批准企业评定
fulfilled_layers|L|该评估情形已声明满足的因素层；仅foundational/impact/sustaining，类型2须含基础与影响，类型3还须含持续
interpretation|S|评估结果的业务解释与排除边界；须说明不是项目步骤、分数或已批准评定
official_requirement_id|S|经核实配套资料的官方需求ID；未取得该资料时只写unknown，不自造官方编号
operating_capability|T|产品对运营能力的要求；说明功能如何支持结果，不能直接推定组织能力已具备
operating_exit_gate|T|BI态可运营和旧平台退出条件；授权退役时须结构化accepted、authority、evidence_refs，不以目标态代替验收
operating_gate|T|主数据本态投入运营的验证条件；包括责任、可运行用例和恢复限制，未满足不称就绪
operation|S|接口操作的业务含义；说明调用方向、前置条件与结果，不能仅写传输协议
option_id|S|候选方案稳定ID；跨轮次保持身份，同ID不允许更换子系统
options_considered|L|决策审议过的选项集合；至少保留候选与被拒原因，不事后只记选中项
origin_locator|S|BI需求具体来源定位；项目访谈、本地补例和配套源分别可回查
overlap_group|S|环境措施潜在重叠效益分组；同组措施汇总前须消除双计，不等同自动互斥
owner|S|本记录、行动或计划的责任方；给出可识别角色或人员，责任不自动意味着批准权
pain|S|BI用户的业务痛点；应来自业务材料，不用技术平台不足替代实际决策问题
period|T|结果或核算记录的时间窗；注明起止、周期口径，不混合不同期间的值
period_kind|S|环境核算期间类型；区分瞬时、期间与累计口径，不跨口径直接相加
pillar|S|数字使能五支柱之一的来源标签；保留源表归属，不按名称推断本地职责
priority_rationale|T|BI用途优先级理由；说明价值、复杂性或数据可得性及证据，未知不计零
priority_rule|T|项目明确的BI排序规则及出处；未给权重不计算加权分，不冒称TOGAF默认算法
product|S|产品稳定标识；功能、组件和接口均按同一产品身份追溯，不用版本号代替身份
proficiency_level|T|技能熟练度及量表锚点；须注明评估方式，未评估不赋最低分
skill_id|S|带版本与类别的技能稳定ID；同名跨类别条目不得合并
scale_id|S|熟练度量表ID；G249-table5-1或显式项目量表，不与G198或Open CA认证直接换算
assessment_kind|S|原文参考目标source_reference_target、裁剪目标tailored_target或人员观察observed_assessment
assessment_state|S|与评级语义一致的状态；未评估或证据不足保留null，不赋最低级
task_refs|A|本技能评价或发展行动对应的任务ID；角色名称不能替代任务范围
requirement_refs|A|本次发展行动回应的角色任务要求ID；目标不得由当前人员表现倒推
behavioral_gap|T|尚未证明的具体行为及业务影响；不能只写目标减现状的数字
success_criteria|L|学习或实践完成的可观察判据；培训出席不等于技能提升
reassessment|D|复评责任人、期限、行为判据与状态；完成须引用人员实测评价
history|R|保留历史评级、时点与证据；新评价不能无痕覆盖旧事实或角色目标；首次评价可显式空数组
project_activity|T|EA服务在指定ADM阶段支持的本地活动；项目观察不能冒充来源图唯一映射
project_scope|T|功能覆盖评估的项目范围与时点；范围外须明确理由，不能默认为未覆盖
propagation|T|主数据传播方向与机制；记录同步或异步、版本、重试与冲突策略
proposal|S|主数据匹配建议；do-not-merge/manual-review/merge-candidate，候选不直接执行合并
protection_controls|T|BI层访问、隐私和保留控制；写明责任与用途限制，不默认公开或无限保留
quality_controls|T|BI层质量校验与失败处理；说明规则、阈值来源和不合格流向
question|S|待回答的完整业务问题；保留原问题上下文，不以结论或简称替代
question_number|I|MDM来源附录A.2问题编号；1至10逐项保留，不跳题合并
rationale|T|本次选择的理由与依据；解释与备选的区别，不循环引用选择结果作证据
raw_and_metadata|T|BI当前态的原始数据和元数据覆盖；区分完整、局部、缺失及来源，不推定已打通
raw_cells|D|来源表原始单元格；空白和破折号按原样保留，解释填入resolved_cells
reason|T|参考裁剪或映射的具体依据；写明适用性与排除边界，不因名称相似自动匹配
receiver_ref|S|接口接收组件稳定ID；与sender_ref共同定义请求方向，不由图形位置推出
record_refs|A|待匹配的各源主数据记录ID集合；保留来源身份，不提前当作同一黄金记录
reference_definition|S|来源参考行完整业务含义；不以简写标签替代定义和排除边界
reference_description|S|政府参考目录节点含义；参考分类不等于本地组织职责
reference_group|S|来源参考分组；仅用于来源组织，不当作强制部署边界
reference_id|S|可携带来源行稳定ID；不能改写成本地实现ID或按名称去重
reference_identity|T|参考身份声明及来源定位；参考对象不能冒充项目实现或已满足需求
reference_kind|S|参考节点种类；按来源业务/应用功能或sector/function/service分层，不跨体系混用
reference_level|S|参考节点原始粒度；保留宏观、高层、组内子功能或目录层次，不自行压平
reference_name|S|来源参考行原始名称；同名异义必须保留完整ID与路径
reference_path|L|来源参考节点完整上级路径；同名节点不得丢父级而合并
reference_scope|T|来源参考分组适用边界；未说明处保留未知，不由名称暗推范围
reference_version|S|本地参考正文版本或sha256；文件摘要不表示官方版本已审定
relationship_boundary|T|DBRM关系使用边界；不能从图线、相邻或颜色推断未核实关系
request|T|接口请求数据与业务语义；列必要字段、约束和失败前置条件，不以报文名代替契约
requirement|T|产品功能需求与期待结果；保持可验证边界，不能混同已实现功能
requirement_origin|S|BI需求来源分类；项目输入、本地译注补例、经核实配套源明确分开
resolved_cells|D|来源表延续单元格解释；保留原始单元格并注明继承依据，不变造源标签
resources|T|交付EA服务所需责任、技能、容量和未满足资源；目录存在不等于可交付
response|T|接口返回结果与异常语义；区分成功、失败和补偿，不默认所有调用成功
result_value|T|评估结果值及尺度；原始分项与聚合分开，无方法依据不得算总分
retirement_authorized|B|旧BI平台退役授权标志；只能布尔，true还须全部旧用途验证与退出验收，目标态不是授权
review_action|T|来源或本地映射的后续核查行动；记录待确认点与责任，不把待核实写成通过
roles|T|微服务治理五类角色的职责与授权边界；不能把角色列举当作各方已接受任命
rollback|T|主数据演进的可操作恢复办法；说明恢复ID、原值、版本和消费者关联及未决限制
rule|T|本地明确规则及来源；匹配规则与跨方案兼容约束按实体类型分别解释，不默认加权评分
rule_expression|S|可执行或可复核的数据质量规则表达式；注明字段、判定条件及未知值处理
schedule_basis|T|BI阶段时间安排的项目依据；无工期数据不套用指南中的参考年限
scope|T|本记录的组织、业务或技术边界和时点；注明排除内容，不能默认覆盖全企业
scope_id|S|交付风格决策范围稳定ID；不同范围可选不同或嵌套风格，不能一次定全企业
scoring|T|明确评分模型与依据或none/null；没有来源和项目授权不合成成熟度总分
security|T|产品接口认证、授权与安全约束；列调用方权限及拒绝处理，不以采用微服务等同安全
sender_ref|S|接口发送组件稳定ID；与receiver_ref共同定义请求方向，响应不改变请求方身份
service|S|EA服务目录稳定ID或完整名称；跨语境同服务保持身份，不由名称推定资源已就绪
service_status|S|微服务目录项的计划或实际状态；存在于目录不表示已部署、运行或产生价值
skill_name|S|技能的业务名称；保留来源技能类别，不能用持有人岗位名称替代技能
source_cell_status|S|原图对应单元格核实状态；本地服务演进观察不能让来源格自动变成已核实
source_guidance|T|交付特征的原指南提示与定位；一般画像不当作项目强制选择或评分阈值
source_locator|S|来源章节、表和具体行定位；不以笼统指南名称代替可回查出处
source_mapping|T|来源参考态或原图映射与本地裁剪的对应；未知不标成不适用或原文已核实
source_mapping_status|S|来源表映射核实状态；local-body-mapping/not-specified/project-only，与本地映射结论独立
source_option_id|S|SBCE兼容约束源方案ID；必须是迭代历史中的方案，不由图表顺序推断
source_refs|A|业务属性定义和观察的来源ID或定位集合；至少一项，不伪造原文强制字段
source_row_id|S|来源表稳定行ID；项目补充行必须另标身份，不能套用官方行号
source_table|S|来源表ID；不同表轴各自独立，不因同名标签合并表结构
source_uncertainty|T|来源缺失、译注或解释的不确定性；不把本地补充写成原文核实结论
sponsor|S|项目或BI用途的业务/IT赞助责任方；尚未接受职责须明确候选而非默认授权
start|S|项目计划开始日期；使用ISO 8601日历日期，计划存在不代表已获开工授权
state_ref|S|命名架构状态的稳定引用；baseline/transition/target另填，状态不授予批准
status|S|本类型的业务处置状态；方案保留/淘汰与约束满足/违背分别使用专属枚举
stockpiled_tonnage|N|核算期末磷石膏堆存量；单位吨、非负，库存不是当期新增量
styles|A|交付风格集合；仅rapid/agile/robust，可按范围嵌套，不以匹配项最多自动选择
subject_ref|S|评估对象的稳定引用；与范围、方法和期间一起确定结果适用对象
submodel|S|运营子模型类型；posture/service/organization/resource四类之一，不是组织上下级
subsystem|S|SBCE方案所属子系统稳定名称或ID；同option_id跨轮次保持相同子系统
tailoring|T|冲突交付特征的项目裁剪说明；说明范围与取舍，不把风格画像当强制阈值
tailoring_reason|T|本地参考裁剪选择理由；结合实际材料说明保留或排除，不抹去参考身份
target_option_id|S|SBCE兼容约束目标方案ID；必须存在于迭代历史，源/目标用于明确耦合而非时间顺序
technical_component|T|产品技术组件或运行环境；版本与未知边界须保留，不把候选技术当已部署事实
test_result|T|控制目标测试的实际结果；区分通过、失败、未执行，须关联方法、时间与证据
threat_actor_ref|S|威胁主体的引用；未知主体明确unknown，不凭事件后果臆造攻击者
tolerable_deviation|T|业务属性可容忍偏差；列单位、上下界和业务依据，不能无来源假设统一百分比
tradeoff|T|候选方案的取舍；逐项列牺牲、收益及受影响方，不把最高分当自动批准
transformation_rule|T|价值链层的技术、业务或语义转换规则及版本；保持输入输出粒度和失败处理
unit|S|评估结果的单位或量表标识；不可将不同单位结果直接相加
unmerge_plan|T|主数据撤销合并方案；恢复ID、原值、版本及消费者关联，不能只说可回滚
use_cases|L|主数据当前态可实际运行的业务用例；计划用例与已验证运营能力分开
user|L|BI实际业务用户或角色；不能只写技术系统，不把候选用户当已采用人数
utilisation_rate|N|磷石膏当期综合利用率；采用utilised/generated的0至1比例，分母为零不计算
utilised_tonnage|N|核算期内磷石膏利用量；单位吨、非负，历史堆存利用须标明口径避免误算当期率
validation_criteria|T|BI需求验收标准；清晰、原子、唯一且可验证，与测试步骤和设计细节区分
value_basis|S|环境量值口径；实测、估算或假设明确区分，估算须方法与来源，不当作实测
version|S|产品功能、组件或接口独立版本；版本更新不自动授予批准或部署状态
waiver|T|微服务控制豁免的请求、状态和决定；批准时须scope/expiry/authority/evidence_refs，申请不视为批准
work_center_ref|S|设备归属工作中心的稳定引用；位置相近不自动表示归属或产线依赖
work_package_ref|S|资源目录关联工作包的外部引用；工作包存在不表示已授权或实际实施
'''


def schemas():
    s = {'type': 'string', 'minLength': 1, 'pattern': r'\S'}
    a = {'type': 'array', 'minItems': 1, 'uniqueItems': True, 'items': s}
    d = {'type': 'object', 'minProperties': 1}
    return {'S': s, 'A': a, 'D': d, 'T': {'anyOf': [s, d]}, 'R': {'type': 'array', 'items': d},
            'L': {'anyOf': [s, a]}, 'N': {'type': 'number', 'minimum': 0},
            'I': {'type': 'integer', 'minimum': 1}, 'B': {'type': 'boolean'}}


ENUMS = {
    'applies': ['yes', 'no', 'unknown'],
    'evolution_kind': ['baseline', 'transition', 'target'],
    'layer_kind': ['source', 'raw', 'prepared', 'information', 'business-view'],
    'submodel': ['posture', 'service', 'organization', 'resource'],
    'proposal': ['do-not-merge', 'manual-review', 'merge-candidate'],
}

NON_CALCULATOR_METHODS = {
    'mdm-operational-ten-questions-method': '逐十问核对观察、证据、运营后果和行动责任；不能由yes比例推出成熟度',
    'mdm-match-merge-arbitration-method': '按业务键、来源和冲突证据提出匹配候选；人工仲裁及可取消合并验证，不按交付风格判断',
    'technical-debt-register-method': '专业判断债务范围、原因、影响和EA介入理由；关闭须修复、验证和复核，不用变更画像计算器',
    'dorp-record-method': '按同一冲刺目标核对Demo/Outcome/Retrospective/Planning；完成证据和回顾不能由项目高亮报告代判',
    'decision-delegation-register-method': '人工核对决策权、参与方式、可逆性和回滚证据；授权不从项目管理策略或等级推导',
    'architecture-description-formality-review-method': '针对指定决策分别判断充分性与正式控制；不以EA观点覆盖或批准状态替代正式度评审',
}


def make_package(caps):
    table = {row.split('|', 2)[0]: row.split('|', 2)[1:]
             for row in RULES.strip().splitlines()}
    types = schemas()
    prior = {}
    for profile in caps['profiles']:
        for kind, fields in profile.get('required_attributes', {}).items():
            for field in fields:
                sem = profile.get('attribute_semantics', {}).get(field)
                meaning = sem.get('meaning') if isinstance(sem, dict) else sem
                if meaning:
                    prior[kind, field] = meaning
    patches = []
    for group in ('work_products', 'analysis_methods'):
        for item in caps[group]:
            scoped = copy.deepcopy(item.get('entity_attribute_semantics', {}))
            if group == 'work_products':
                for kind, fields in item.get('required_attributes', {}).items():
                    for field in fields:
                        legacy = item.get('attribute_semantics', {}).get(field, {})
                        if all(legacy.get(k) for k in ('meaning', 'value_rule', 'definition_origin')) and field not in scoped.get(kind, {}):
                            continue
                        token, rule = table[field]
                        value_schema = copy.deepcopy(types[token])
                        if field in ENUMS:
                            value_schema = {'type': 'string', 'enum': ENUMS[field]}
                        if field in ('start', 'end', 'due_date', 'date'):
                            value_schema['format'] = 'date'
                        if field == 'question_number':
                            value_schema['maximum'] = 10
                        if field == 'utilisation_rate':
                            value_schema['maximum'] = 1
                        if field == 'styles':
                            value_schema['items'] = {'enum': ['rapid', 'agile', 'robust']}
                        if field == 'new_evidence_refs':
                            value_schema['minItems'] = 0
                        if field == 'scoring':
                            value_schema = {'anyOf': [value_schema, {'type': 'null'}]}
                        if field == 'result_value':
                            value_schema = {'anyOf': [value_schema, {'type': 'number'}]}
                        if field == 'legacy_requirement_coverage':
                            value_schema['additionalProperties'] = {'enum': [
                                'verified', 'verified-in-example', 'legacy-service-retained',
                                'planned', 'unknown', 'not-covered', 'out-of-scope-with-reason']}
                        if field == 'status' and kind == 'guide:sbce_iteration':
                            value_schema = {'enum': ['retain', 'eliminate', 'selected', 'reopen']}
                            rule = '本轮方案处置；retain/eliminate/selected/reopen，淘汰和重开须原因及新增证据，selected不是正式批准'
                        if field == 'status' and kind == 'guide:sbce_constraint':
                            value_schema = {'enum': ['satisfied', 'violated', 'unknown']}
                            rule = '跨子系统方案兼容验证；satisfied/violated/unknown，所选集合存在violated或unknown不能称兼容'
                        if field == 'rule' and kind == 'guide:sbce_constraint':
                            rule = '两方案间显式兼容约束；写清耦合、方向和判定条件，非优先级或加权分，不得忽略未验证耦合'
                        scoped.setdefault(kind, {})[field] = {
                            'meaning': prior.get((kind, field), rule.split('；')[0]),
                            'value_rule': rule, 'definition_origin': 'project-operational-convention',
                            'value_schema': value_schema, 'source_refs': item.get('source_refs', [])}
            specs = []
            for source in ('checks', 'semantic_checks'):
                for index, text in enumerate(item.get(source, []), 1):
                    specs.append({'id': f'{source}-{index}', 'text': text,
                                  'mode': 'review', 'source': source})
            required = item.get('required_attributes', {})
            if required and group == 'work_products':
                specs.append({'id': 'typed-required-fields', 'text': '必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性）',
                              'mode': 'machine', 'source': 'field-contract', 'executor': 'field-values',
                              'code': 'field-contract-value', 'applies_to': {'entity_types': list(required)}})
            for kind, executor, code, text in [
                ('guide:bi_operating_state', 'bi-retirement', 'bi-retirement-not-ready', '申请退役时，旧用途逐项已验证且退出验收有权威与证据'),
                ('ops:msa_governance', 'msa-authorization', 'msa-authorization-evidence-gap', '声称治理决定或豁免已批准时具备范围内授权与决定证据')]:
                if kind in required and group == 'work_products':
                    specs.append({'id': executor, 'text': text, 'mode': 'machine', 'source': 'domain-contract',
                                  'executor': executor, 'code': code, 'applies_to': {'entity_types': [kind]}})
            if 'guide:sbce_iteration' in required and group == 'work_products':
                specs.append({'id': 'sbce-contract', 'text': '按轮次保留方案身份、淘汰/重开证据及显式所选集合兼容约束；未建模耦合仍需人工评审',
                              'mode': 'machine', 'source': 'domain-contract', 'executor': 'sbce-contract',
                              'code': 'sbce-contract-violation', 'applies_to': {
                                  'entity_types': ['guide:sbce_iteration', 'guide:sbce_constraint']}})
            updates = {'check_specs': specs}
            if item['id'] in NON_CALCULATOR_METHODS and group == 'analysis_methods':
                updates.update({
                    'calculator_id': None,
                    'calculator_status': 'no-deterministic-calculator',
                    'calculation_policy': 'professional-procedural-review; no deterministic score or substitute calculator',
                    'implementation_status': 'professional-review-with-separate-structural-checks',
                    'execution_mode': 'manual-evidence-review; field-contracts-only-check-observable-structure',
                    'professional_review': NON_CALCULATOR_METHODS[item['id']],
                    'structural_check_path': {
                        'module': 'scripts/field_contracts.py', 'function': 'run_check',
                        'check_spec_id': 'typed-required-fields',
                        'work_product_ids': item.get('output_work_products', []),
                        'limit': '仅校验输出实体必填值及登记类型约束；不执行专业方法、不授予验收'},
                    'review_reference': item.get('reference_document'),
                })
            if scoped:
                updates['entity_attribute_semantics'] = scoped
            # Legacy name was omitted in nine new products; first-class property.
            if group == 'work_products' and 'name' in item.get('fields', []) and not item.get('attribute_semantics', {}).get('name'):
                flat = {}
                flat['name'] = {'meaning': '工作产品对象的业务名称', 'value_rule': '使用范围内可识别的业务名称；身份由稳定ID确定，不以同名合并对象',
                                'definition_origin': 'project-operational-convention', 'value_schema': types['S']}
                updates['attribute_semantics'] = flat
            patches.append({'group': group, 'id': item['id'], 'set': updates})
    return {'schema_version': 'capability-addenda/1', 'id': 'field-contracts',
            'status': 'registered-not-accepted', 'owner': 'togaf-architecture-workbench',
            'notice': '项目操作契约；复用现有指南摘要，不表示TOGAF官方语义验收。旧检查显式保留为专业review；机器断言仅限绑定的真实执行器。',
            'patches': patches}
