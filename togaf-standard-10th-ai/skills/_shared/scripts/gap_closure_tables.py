"""Source tables for the 2026-11-05 standard-gap closure (G176/G186/G212/G249 and ADM-usage chapters).

Items are short project paraphrases with locators into the local guides; they are not
verbatim copies. Figure-derived mappings are marked as figure interpretations. Nothing
here is an enterprise fact, an approval, or proof of source equivalence.
"""

NOTICE = ('项目转述的来源要点，附本地定位；不是原文全文。图示推断项单列标记。'
          '勾选、评分或映射本身不构成批准或来源等价。')

# ---- G176 §11: business scenario checklists (English PDF pp.31-35; zh L699-892) ----
# kind: item | any-of (at least one child done) | all-of (each child done or n/a with reason)
# condition: optional; 'workshop' means the item applies only when a workshop is used.
SCENARIO_STAGES = [
    {'id': 'premise', 'name': '前提形成', 'locator': 'G176 §11.1', 'items': [
        ('premise-01', '有一个简单的前提', 'item', []),
        ('premise-02', '有初始顶点问题（capstone question）', 'item', []),
        ('premise-03', '有候选发起人', 'item', []),
        ('premise-04', '存在一个或多个触发因素', 'any-of', [
            ('premise-04a', '对业务需求缺乏清晰理解'), ('premise-04b', '问题在找解决方案'),
            ('premise-04c', '解决方案在找问题'), ('premise-04d', '技术话语主导'),
            ('premise-04e', '目标市场未识别'), ('premise-04f', '“不知道如何开始”')]),
        ('premise-05', '已识别目标买方参与者', 'item', []),
        ('premise-06', '已识别目标客户方参与者', 'item', []),
        ('premise-07', '已接触目标供方参与者', 'item', []),
        ('premise-08', '已接触目标客户方参与者', 'item', [])]},
    {'id': 'plan', 'name': '规划', 'locator': 'G176 §11.2', 'items': [
        ('plan-01', '已指定项目经理', 'item', []),
        ('plan-02', '已指定业务场景顾问', 'item', []),
        ('plan-03', '已选择数据收集机制', 'item', []),
        ('plan-04', '已设定项目约束', 'all-of', [
            ('plan-04a', '时间'), ('plan-04b', '人员'), ('plan-04c', '资金')]),
        ('plan-05', '参与活动已配置资源', 'item', []),
        ('plan-06', '后勤活动已配置资源（来源清单此项出现两次，合并为一项并展开子项）', 'all-of', [
            ('plan-06a', '会议与工作坊后勤'), ('plan-06b', '演练会议'), ('plan-06c', '场地布置'),
            ('plan-06d', '应急安排'), ('plan-06e', '后续跟进'), ('plan-06f', '润滑协调'),
            ('plan-06g', '感谢信')]),
        ('plan-07', '其他角色已配置资源', 'item', []),
        ('plan-08', '已召开首次团队会议', 'item', []),
        ('plan-09', '已建立依赖关系', 'item', []),
        ('plan-10', '已建立合理时间线', 'item', []),
        ('plan-11', '已记录在项目计划中', 'item', [])]},
    {'id': 'gather', 'name': '收集', 'locator': 'G176 §11.3', 'items': [
        ('gather-01', '问题已拟定', 'item', []),
        ('gather-02', '已收集公开可用数据', 'item', []),
        ('gather-03', '已预处理公开可用数据', 'item', []),
        ('gather-04', '已形成关键要素的稻草人', 'item', []),
        ('gather-05', '数据收集材料已准备', 'item', []),
        ('gather-06', '参与者已确定', 'item', []),
        ('gather-07', '参与者已参与', 'item', []),
        ('gather-08', '已采取措施保持期望的匿名性', 'item', []),
        ('gather-09', '已考虑收集方式', 'any-of', [
            ('gather-09a', '工作坊'), ('gather-09b', '问卷'), ('gather-09c', '访谈'),
            ('gather-09d', '焦点小组'), ('gather-09e', '市场研究等')]),
        ('gather-w1', '有议程', 'item', [], 'workshop'),
        ('gather-w2', '工作坊已编写脚本并演练', 'all-of', [
            ('gather-w2a', '引导者与东道主'), ('gather-w2b', '问者与记录员')], 'workshop'),
        ('gather-w3', '场地已准备（视情况）', 'all-of', [
            ('gather-w3a', '白板纸'), ('gather-w3b', 'U形桌'), ('gather-w3c', '白板'),
            ('gather-w3d', '会议接入')], 'workshop'),
        ('gather-w4', '邀请与说明已发送给领域专家', 'item', [], 'workshop'),
        ('gather-w5', '已准备以电子方式记录全部信息', 'item', [], 'workshop'),
        ('gather-w6', '已考虑分设买方与供方两场工作坊', 'item', [], 'workshop')]},
    {'id': 'analyze', 'name': '分析', 'locator': 'G176 §11.4', 'items': [
        ('analyze-01', '所有数据集中一处并锁定为只读', 'item', []),
        ('analyze-02', '已为每个要素准备文本分析工作表', 'item', []),
        ('analyze-03', '已为每个要素准备可计算数据工作表', 'item', []),
        ('analyze-04', '工作表已填入原始数据', 'item', []),
        ('analyze-05', '文本已转换为归一化、分类清单', 'item', []),
        ('analyze-06', '已完成计算', 'item', []),
        ('analyze-07', '已准备连接全部关键要素的统一矩阵', 'item', []),
        ('analyze-08', '已评估完整性与正确性', 'all-of', [
            ('analyze-08a', '每个痛点至少有一个成果')]),
        ('analyze-09', '已生成一组业务与技术能力', 'item', []),
        ('analyze-10', '已起草所收集数据的模型', 'item', []),
        ('analyze-11', '已起草结果文本', 'item', [])]},
    {'id': 'document', 'name': '文档化', 'locator': 'G176 §11.5', 'items': [
        ('document-01', '已指定主作者（本应在规划步骤完成）', 'item', []),
        ('document-02', '已指定编辑（本应在规划步骤完成）', 'item', []),
        ('document-03', '已起草文档', 'item', []),
        ('document-04', '文档中已以图形纳入模型', 'item', []),
        ('document-05', '已以文本描述模型', 'item', []),
        ('document-06', '图已编号', 'item', []),
        ('document-07', '使用了建模语言（来源举例ArchiMate）', 'item', []),
        ('document-08', '已阐明业务导向的问题与期望成果', 'item', []),
        ('document-09', '有“那又怎样（so what）”', 'item', []),
        ('document-10', '有“以便（so that）”', 'item', []),
        ('document-11', '已开展非正式内部内容评审', 'item', []),
        ('document-12', '已更新草稿与模型', 'item', []),
        ('document-13', '已从业务人员视角校对编辑', 'item', [])]},
    {'id': 'review', 'name': '评审', 'locator': 'G176 §11.6', 'items': [
        ('review-01', '已指定内部评审人', 'item', []),
        ('review-02', '已指定外部评审人', 'item', []),
        ('review-03', '已为特定评审人分配特定章节', 'item', []),
        ('review-04', '已向评审人提供正式说明', 'item', []),
        ('review-05', '已正式管理变更请求', 'item', []),
        ('review-06', '已就前进路径征询利益相关者意见', 'item', []),
        ('review-07', '已为发布更新文档与模型', 'item', []),
        ('review-08', '已将文档送入发布流程', 'item', []),
        ('review-09', '已向参与者发送发布状态与感谢信', 'item', [])]},
]

# ---- G176 §10: twelve roles; staffing is done in the Plan step ----
SCENARIO_ROLES = [
    ('project-manager', '项目经理', '规划、执行并监控，使场景按时按预算形成文档并评审'),
    ('business-scenario-consultant', '业务场景顾问', '引导项目朝高质量场景推进'),
    ('business-scenario-analyst', '业务场景分析师', '用收集与分析技术形成对场景要素的共识'),
    ('business-scenario-author', '业务场景作者', '对场景作忠实、客观的叙述'),
    ('business-scenario-editor', '业务场景编辑', '把草稿加工为可发布文档'),
    ('business-scenario-facilitator', '业务场景引导者', '主持会议与工作坊'),
    ('sme-contributor', '领域专家贡献者', '就前提相关主题提供专家意见与内容'),
    ('sme-reviewer', '领域专家评审者', '评审场景文档并提出客观建议'),
    ('host', '东道主', '提供开放、受欢迎的参与环境'),
    ('sponsor', '发起人', '代表高管买方说明重要性并承诺跟进'),
    ('workshop-questioner', '工作坊主问者与次问者', '提出计划好的探询性问题与追问'),
    ('workshop-recorder', '工作坊记录员', '忠实记录问题答案与笔记'),
]
# Checklist items that name a role; the role must be assigned in the Plan stage.
ROLE_ITEMS = {'plan-01': 'project-manager', 'plan-02': 'business-scenario-consultant',
              'document-01': 'business-scenario-author', 'document-02': 'business-scenario-editor'}

# ---- G176 §9.3: thirteen goal categories (examples, not a closed list) ----
GOAL_CATEGORIES = [
    ('business-process-performance', '改善业务流程绩效', 'G176 §9.3.1'),
    ('reduce-costs', '降低成本', 'G176 §9.3.2'),
    ('business-operations', '改善业务运营', 'G176 §9.3.3'),
    ('management-efficacy', '提高管理效能', 'G176 §9.3.4'),
    ('reduce-risk', '降低风险', 'G176 §9.3.5'),
    ('it-effectiveness', '提高IT组织有效性', 'G176 §9.3.6'),
    ('user-productivity', '提高用户生产率', 'G176 §9.3.7'),
    ('portability-scalability', '提高可移植性与可扩展性', 'G176 §9.3.8'),
    ('interoperability', '提高互操作性', 'G176 §9.3.9'),
    ('vendor-independence', '提高供应商独立性', 'G176 §9.3.10'),
    ('lifecycle-costs', '降低生命周期成本', 'G176 §9.3.11'),
    ('security', '提高安全性', 'G176 §9.3.12'),
    ('manageability', '提高可管理性', 'G176 §9.3.13'),
]
SMART_CRITERIA = [('specific', '具体'), ('measurable', '可度量'), ('actionable', '可行动'),
                  ('realistic', '现实'), ('time-bound', '有时限')]
# G176 §7.2 question areas used by scenario elicitation.
QUESTION_AREAS = [
    ('problems', '识别、记录并排序问题：问“需要完成什么”而非“如何做”，并问清何处、何时与成本', 'G176 §7.2.1'),
    ('environment', '识别业务与技术环境：关键流程、内外部位置规模、业务规则法规、技术组件、约束与原则', 'G176 §7.2.2'),
    ('objectives', '识别并记录目标：为“做什么”要可度量的理由（回报、扩展、性能、标准、易用）', 'G176 §7.2.3'),
    ('human-actors', '识别人的参与者及其在业务模型中的位置，从开发、维护、运维、管理和用户视角询问', 'G176 §7.2.4'),
    ('computer-actors', '识别计算机参与者及其在技术模型中的位置', 'G176 §7.2.5'),
    ('roles-measures', '记录角色、职责、成功度量与所需脚本', 'G176 §7.2.6'),
    ('fitness', '检查适用性：是否足以识别谁能满足需求、何时与多频繁', 'G176 §7.2.7'),
]

# ---- G212 §6, Table 6-1 and Figure 6-1 (English PDF pp.28-30) ----
DTRA_CATEGORIES = {
    'foundational': ['vision', 'sponsorship-direction', 'it-capability', 'culture', 'scope-scale',
                     'business-rationale', 'implementation-approach'],
    'impact': ['business-model-adaptability', 'skills-competence', 'technology-maturity', 'ecosystem',
               'governance-compliance'],
    'sustaining': ['value-realization', 'policy-regulations', 'funding-resources']}
# Table 6-1 implications (paraphrased). zone_factors: Figure 6-1 co-location, implicit, unreviewed.
DTRA_PHASES = [
    ('Preliminary', '理解企业能力、所用架构框架与治理框架中驱动数字采用的因素；定义架构原则；确定组织期望的、聚焦数字技术的架构能力',
     ['vision', 'sponsorship-direction']),
    ('A', '捕获目标状态高层愿景；识别利益相关者及业务驱动和关注点并开展就绪度评估；依评估输出选择架构路径',
     ['vision', 'sponsorship-direction']),
    ('B', '开发支撑愿景的目标业务架构；开展详细能力评估及业务驱动与目标分析',
     ['business-rationale', 'scope-scale', 'business-model-adaptability', 'culture', 'funding-resources']),
    ('C', '开发目标数据与应用架构；开展能力评估、数据与应用驱动分析、差距分析与沟通计划；因素侧重数据与应用方面的组织能力',
     ['value-realization', 'policy-regulations', 'governance-compliance', 'skills-competence', 'ecosystem']),
    ('D', '分析技术架构差距；用技术原则使技术架构与数字采用对齐；因素侧重组织技术能力',
     ['it-capability', 'technology-maturity', 'governance-compliance', 'skills-competence', 'ecosystem']),
    ('E', '在各域差距外整体判断组织数字采用现状；给出使关键因素就绪的方法；用关键因素差距推导中间与目标状态',
     ['implementation-approach']),
    ('F', '使实施与迁移规划同数字转型方法和愿景对齐；分解实施与迁移战略和实施计划',
     ['implementation-approach']),
    ('G', '通过合规与评审确保遵循实施计划、符合目标架构；此处治理指实施方法是否恰当，不是“治理与合规”因素',
     ['implementation-approach']),
    ('H', '随成熟度与全景演进维护架构变更周期，管理数字采用带来的架构变更', []),
    ('Requirements', '需求管理贯穿所有阶段；需求变更经需求影响评估处理，并在下一周期的相关阶段实施', []),
]
DTRA_RULES = [
    ('start-in-A', 'DTRA应在架构愿景阶段启动，以了解组织现状', 'G212 §6 正文'),
    ('reassess', '可在ADM周期结束或下一周期愿景阶段重新评估', 'G212 §6 正文'),
    ('attention', '复核评分不是“非常同意”或“同意”的因素', 'G212 §7、附录A'),
    ('foundational-first', '未满足基础因素时评估影响与持续因素无意义，应逐步推进', 'G212 §5.4'),
    ('phase-g-not-factor', '阶段G的治理指实施方法恰当性，不要与C/D的“治理与合规”因素混淆', 'G212 表6-1 注'),
]
LIKERT_AGREE = 6  # G212 Table A-1: 7=Strongly Agree, 6=Agree; lower scores need review.

# ---- G249 §4 role categories; the numbers below are display order only. ----
ROLE_TIERS = {'chief': 0, 'enterprise': 1, 'segment': 2, 'solution': 3, 'specialist': 4}
ROLE_TIER_NOTES = {
    'chief': '企业架构师的特例；把EA视图纳入更广泛的战略与运营语境，偏政治、协作与说服，不据此推断人事职级',
    'enterprise': '跨多个分段创建变革路线图，定义塑造全景的原则与政策，监督架构变更治理',
    'segment': '负责一个或多个业务或技术分段（如业务、应用、数据、技术域）的能力、组件与路线图',
    'solution': '基于特定需求塑造并治理解决方案，经一系列过渡架构交付',
    'specialist': '业务/数据/应用/技术专家，接受分段架构师领导，补充细节知识',
}
ROLE_RULES = [
    ('min-three-levels', '指南示例区分企业、分段、解决方案，依第3、6章按企业需要裁剪，非所有组织的强制职级', 'G249 §4（书页7；PDF页17）'),
    ('chief-special-case', '首席架构师是企业架构师的特例，不是另一个并列层级', 'G249 §4'),
    ('kpi-placeholder', 'KPI中的“3/5满意度”“（xxx）四分位”是示例或占位，需企业自行设定目标', 'G249 §4.1–4.4'),
    ('role-vs-job', '岗位、角色、任务是不同概念；一人可承担多个角色，多人可承担同一角色', 'G249 §4'),
]

# ---- G186 Appendix D, Table D-1: Solution Delivery Notebook (English PDF pp.138-139) ----
NOTEBOOK_SECTIONS = [
    ('solution-summary', '解决方案摘要', ['solution-concept-diagram', 'stakeholder-catalog', 'risk-catalog', 'gap-catalog']),
    ('specification-summary', '规格摘要', ['implementation-strategy', 'architecture-specification', 'control']),
    ('architecture-description-summary', '架构描述摘要（仅供参考）',
     ['business', 'information', 'application', 'infrastructure', 'security', 'other-domain']),
]
NOTEBOOK_RULES = [
    ('spec-traces-requirement', '规格可适用于架构任何事物，但始终追溯到某项需求', 'G186 表D-1 架构规格'),
    ('control-traces-risk', '控制可适用于架构任何事物，但始终追溯到某项风险', 'G186 表D-1 控制'),
    ('two-pairs', '规格符合性按需求/规格配对与风险/控制配对测试', 'G186 表D-1 规格摘要'),
    ('gap-scope', '差距目录标明本工作包处理范围；未处理的差距要明确标出', 'G186 表D-1 差距目录'),
    ('description-reference', '架构描述摘要仅供参考，用图、目录、矩阵概述目标架构', 'G186 表D-1 架构描述摘要'),
]

# ---- "Using with the ADM" chapters: guide-stated phase usage (not mandatory outputs) ----
GUIDE_USAGE = [
    ('G190 §6', 'A', '查找已有信息地图及其与业务能力地图等核心制品的关系', ['information-map', 'business-capability-map'], []),
    ('G190 §6', 'B', '按范围构建信息概念、关系及与其他业务制品要素的关联', ['information-map'], []),
    ('G190 §6', 'C', '可能时把信息转为数据模型，并捕获与应用、技术服务和逻辑属性的关系', ['information-map', 'conceptual-data-diagram', 'logical-data-diagram'], []),
    ('G190 §6', 'D', '捕获信息与技术服务及驱动设计的逻辑属性的关系', ['information-map'], []),
    ('G190 §6', 'E', '更新业务架构时同步更新信息地图', ['information-map'], []),
    ('G206 §6', 'A', '查找并使用已有组织描述，哪怕只是传统组织架构图', ['organization-map', 'organization-decomposition-diagram'], []),
    ('G206 §6', 'B', '构建组织地图，补充理解业务需求所需细节及与能力、信息等视图的关系；识别解决方案利益相关者', ['organization-map', 'capability-organization-matrix', 'stakeholder-catalog'], []),
    ('G211 §6', 'Preliminary', '定义EA团队与组织时引入能力，确定现有企业与业务能力', ['business-capabilities-catalog', 'business-capability-map'], ['capability-decomposition-method']),
    ('G211 §6', 'A', '识别落实战略优先级所需能力，并用能力地图形成基线与目标高层视图', ['business-capability-map', 'strategy-capability-matrix'], []),
    ('G211 §6', 'B', '用热力映射（成熟度、有效性、绩效、价值或成本）评估能力差距；把能力映射到组织、价值流、信息系统与战略计划', ['business-capability-map', 'capability-organization-matrix', 'value-stream-capability-matrix'], []),
    ('G21I §4–5', 'Preliminary', '评估MSA组织与生命周期就绪度及治理安排', [], ['msa-readiness-evidence-method', 'msa-federated-governance-process-method']),
    ('G21I §4、§6', 'A', '在愿景中识别微服务适用范围与候选边界', [], ['microservice-boundary-method']),
    ('G21I §4、§7', 'B', '在业务架构中细化微服务对应的业务边界', [], ['microservice-boundary-method']),
    ('G21I §4、§11', 'F', '迁移规划中核对微服务业务价值与开发运营资源', [], ['msa-value-resource-evidence-method']),
    ('G21I §4、§8', 'C', '面向MSA的数据分布与应用契约设计', ['application-communication-diagram', 'data-dissemination-diagram'], ['msa-contract-consumer-evidence-method', 'msa-data-distribution-conditions-method']),
    ('G21I §4、§9', 'D', '面向MSA的部署与执行单元技术架构', ['software-distribution-diagram', 'platform-decomposition-diagram'], ['msa-source-deployment-execution-method']),
    ('G21I §4、§12', 'G', '双轨治理与豁免过程', [], ['msa-federated-governance-process-method']),
    ('G212 §6', 'A', '在架构愿景阶段启动DTRA，并按表6-1在各阶段考虑相关因素', [], ['dtra-readiness-method', 'dtra-adm-phase-alignment-review']),
    ('G186 §12.1', 'G', '敏捷对齐落在阶段G：架构定义企业待办、产品边界与产品负责人约束', [], ['product-constraint-conformance-review']),
    ('G186 §12.2', 'B', '领域架构须融入整体EA；安全按关注点贯穿其他域', [], ['domain-architecture-alignment-review']),
    ('G186 §12.3', 'H', '事件改变风险偏好即需求变更；就目标与工作变更提供建议', [], ['incident-architecture-adjustment-review']),
    ('G186 附录D', 'G', '用解决方案交付笔记本把架构传达给交付团队', [], ['solution-delivery-notebook-review']),
    ('G249 §4', 'Preliminary', '建立架构实践时定义架构角色、职责与KPI', [], ['architecture-role-catalog-review']),
    ('G176 §9–11', 'A', '开发业务场景时按清单推进各步骤并把目的做成SMART', [], ['business-scenario-checklist-review', 'smart-objective-review']),
]
