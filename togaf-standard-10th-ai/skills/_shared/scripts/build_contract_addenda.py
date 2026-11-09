#!/usr/bin/env python3
"""Build the two contract addenda packages from registry state plus curated definitions.

Two outputs:
  skill-contract-entity-types.json    99 entity definitions + 29 relationship definitions
  skill-contract-counterexamples.json 87 work-product counterexamples, 60 method
                                      counterexamples, 12 missing-attribute patches,
                                      31 calculator registrations, 4 new methods

Nothing here grants acceptance. Definitions are project-operational conventions:
they state how this project will read a name, never that the name is officially
defined in a source the project does not hold.
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADDENDA = ROOT / "capability-addenda"

# ---------------------------------------------------------------------------
# Entity definitions. Key = entity type, value = (meaning, level, owner).
# level "core" for unprefixed names; "guide-extension" for prefixed ones.
# ---------------------------------------------------------------------------
ENTITY_DEFINITIONS = {
    # --- artifact-review ---
    "acceptance_criterion": ("验收准则：可判定的通过条件，须指明主体、判据与证据形式。", "core", "togaf-artifact-review"),
    "guide:closure_record": ("阶段或项目收尾记录：记录交付、遗留与移交状态。", "guide-extension", "togaf-artifact-review"),
    "guide:deliverable_charter": ("交付物章程：约定交付物范围、验收流程与责任人。", "guide-extension", "togaf-artifact-review"),
    "guide:governance_check": ("治理检查记录：对治理清单的执行结果。", "guide-extension", "togaf-artifact-review"),
    "guide:noncompliance_disposition": ("不合规处置：偏差、裁决、到期与后续动作。", "guide-extension", "togaf-artifact-review"),
    "guide:viewpoint": ("视角定义：面向谁、回答哪些关注点、需要什么信息与记法。", "guide-extension", "togaf-artifact-review"),
    "sustainability_action": ("可持续性行动：针对已识别环境影响的候选措施。", "core", "togaf-artifact-review"),
    # --- ea-capability ---
    "adoption_option": ("采用选项：数字技术采用的候选路径，不含采纳决定。", "core", "togaf-ea-capability"),
    "adoption_step": ("采用步骤：采用路径中的一个可执行动作。", "core", "togaf-ea-capability"),
    "ea_capacity": ("架构能力容量：可投入架构工作的人力与技能总量。", "core", "togaf-ea-capability"),
    "ea_value": ("架构价值项：架构工作对业务的具体贡献，须可指向受益方。", "core", "togaf-ea-capability"),
    "guide:cycle_product": ("业务周期工作产品时点：某工作产品在业务周期中的产出时机。", "guide-extension", "togaf-ea-capability"),
    "guide:ea_adm_mapping": ("EA 服务与 ADM 阶段映射：服务在哪个阶段被消费。", "guide-extension", "togaf-ea-capability"),
    "guide:ea_service_context": ("EA 服务语境：服务面向的组织规模与决策层级。", "guide-extension", "togaf-ea-capability"),
    "guide:framework_touchpoint": ("框架接触点：与其他框架或标准的接触位置与承诺程度。", "guide-extension", "togaf-ea-capability"),
    "guide:project_learning": ("项目经验记录：可复用的教训与改进动作。", "guide-extension", "togaf-ea-capability"),
    "guide:sustainability_capability": ("可持续性能力：支撑环境目标的能力项。", "guide-extension", "togaf-ea-capability"),
    "guide:value_observation": ("价值观测：带基线、观测窗与归因边界的实测记录。", "guide-extension", "togaf-ea-capability"),
    "maturity_criterion": ("成熟度判据：某一级别必须成立的证据条件。", "core", "togaf-ea-capability"),
    "maturity_observation": ("成熟度观察：针对某判据的实际观察值与证据。", "core", "togaf-ea-capability"),
    "readiness_consequence": ("就绪度后果：某因素未达标带来的具体影响。", "core", "togaf-ea-capability"),
    "readiness_question": ("就绪度问项：问卷中的一个可作答问题及其锚点。", "core", "togaf-ea-capability"),
    # --- information-data ---
    "analytics_component": ("分析组件：BI 与分析平台的构成单元。", "core", "togaf-information-data"),
    "data_issue": ("数据问题：已发现的缺陷、影响与处置状态。", "core", "togaf-information-data"),
    "data_quality_measure": ("数据质量测量值：维度、指标、期间与测量结果。", "core", "togaf-information-data"),
    "data_usage": ("数据用途：某数据被谁、为何、在什么约束下使用。", "core", "togaf-information-data"),
    "guide:bi_operating_state": ("BI 运营状态：平台在某一阶段的可运营条件。", "guide-extension", "togaf-information-data"),
    "guide:mdm_diagnostic_answer": ("主数据诊断答案：运营十问中的一条作答与证据。", "guide-extension", "togaf-information-data"),
    "guide:mdm_match_case": ("主数据匹配案例：候选记录对与匹配依据。", "guide-extension", "togaf-information-data"),
    "guide:mdm_plateau": ("主数据成熟台阶：某阶段的能力与退出条件。", "guide-extension", "togaf-information-data"),
    "inference_source": ("推断来源：技术元数据推断所依据的来源与置信说明。", "core", "togaf-information-data"),
    "master_exchange": ("主数据交换：主数据在两系统间的传递方式与频率。", "core", "togaf-information-data"),
    "master_repository": ("主数据存储库：保存权威副本的库及其职责。", "core", "togaf-information-data"),
    "metadata_activity": ("元数据活动：采集、校验、发布等可执行动作。", "core", "togaf-information-data"),
    "metadata_component": ("元数据组件：元数据管理方案的构成部分。", "core", "togaf-information-data"),
    "metadata_policy": ("元数据政策：元数据的责任、质量与使用规则。", "core", "togaf-information-data"),
    "ops:bi_model_operations": ("BI 模型运维：模型上线后的运行与监控要求。", "guide-extension", "togaf-information-data"),
    "ops:bi_value_chain": ("BI 价值链控制：从数据到决策的增值环节与控制点。", "guide-extension", "togaf-information-data"),
    "ops:functional_coverage": ("功能覆盖记录：参考功能与项目实现的覆盖关系。", "guide-extension", "togaf-information-data"),
    # --- requirements ---
    "analytics_requirement": ("分析需求：由决策问题反推的信息与分析要求。", "core", "togaf-requirements"),
    "guide:bi_requirement_provenance": ("BI 需求来源：需求由哪个决策问题与哪些材料产生。", "guide-extension", "togaf-requirements"),
    "ops:bi_usage": ("BI 使用记录：功能被实际使用的证据，不等于运行次数。", "guide-extension", "togaf-requirements"),
    # --- architecture-workbench ---
    "architecture_activity": ("架构活动：可排期的架构工作单元。", "core", "togaf-architecture-workbench"),
    "architecture_task": ("架构任务：活动下的可分配工作项。", "core", "togaf-architecture-workbench"),
    "guide:agile_activity": ("敏捷活动：冲刺中的一项工作。", "guide-extension", "togaf-architecture-workbench"),
    "guide:agile_context": ("敏捷语境：协作方式适用的团队与场景。", "guide-extension", "togaf-architecture-workbench"),
    "guide:agile_pattern_choice": ("敏捷协作方式选择：四种协作方式之一的选定理由。", "guide-extension", "togaf-architecture-workbench"),
    "guide:agile_sprint": ("敏捷冲刺：团队与时间盒下有独立目标的迭代。", "guide-extension", "togaf-architecture-workbench"),
    "guide:dorp_gate": ("DORP 关卡：演示、成果、回顾、规划四活动中的检查点。", "guide-extension", "togaf-architecture-workbench"),
    # --- business-models-processes ---
    "digital_business_function": ("数字业务功能：数字企业参考模型中的功能项。", "core", "togaf-business-models-processes"),
    "government_service": ("政府服务：政府参考模型中的三级服务项。", "core", "togaf-business-models-processes"),
    "guide:competency_overlay": ("胜任力叠加：能力所需胜任力的映射层。", "guide-extension", "togaf-business-models-processes"),
    "guide:dbrm_applicability": ("DBRM 适用性：参考要素对本企业的适用判断。", "guide-extension", "togaf-business-models-processes"),
    "guide:dbrm_mapping_row": ("DBRM 映射行：参考要素与项目对象的一行对应。", "guide-extension", "togaf-business-models-processes"),
    "guide:government_overlay": ("政府参考叠加：政府部门功能服务对业务的对照。", "guide-extension", "togaf-business-models-processes"),
    "guide:government_reference_node": ("政府参考节点：部门、功能、服务三层中的节点。", "guide-extension", "togaf-business-models-processes"),
    "guide:operating_submodel": ("运营子模型：运营模式中的一个可分析子域。", "guide-extension", "togaf-business-models-processes"),
    "journey_stage": ("旅程阶段：客户旅程中的一个阶段及其触点与痛点。", "core", "togaf-business-models-processes"),
    "persona": ("客户画像：带证据的客户群特征与目标。", "core", "togaf-business-models-processes"),
    # --- change-value ---
    "environmental_debt": ("环境债务：已产生但未处置的环境负担，不等于排放量。", "core", "togaf-change-value"),
    "environmental_decision": ("环境决策：针对环境影响的裁决与理由。", "core", "togaf-change-value"),
    "phosphogypsum_record": ("磷石膏记录：某期间的产生、利用、堆存数量与利用率。", "core", "togaf-change-value"),
    "equipment": ("设备：ISA-95 设备层级中的资产单元，含所属工作中心与关键度。", "core", "togaf-technology-architecture"),
    "guide:carbon_reference_data": ("碳参考数据：排放因子与其适用边界。", "guide-extension", "togaf-change-value"),
    "guide:dual_entry_opportunity": ("双入口机会：用途侧与基础设施侧同时识别的改进机会。", "guide-extension", "togaf-change-value"),
    # --- implementation-governance ---
    "audit_finding": ("审计发现：审计中确认的偏差与整改要求。", "core", "togaf-implementation-governance"),
    "guide:cloud_environmental_field": ("云环境数据字段：云与外包方需提供的数据项。", "guide-extension", "togaf-implementation-governance"),
    "guide:governance-check": ("治理检查：治理规则的执行判定（另一写法）。", "guide-extension", "togaf-implementation-governance"),
    "guide:sustainable_procurement": ("可持续采购：ICT 采购中的环境与生命周期要求。", "guide-extension", "togaf-implementation-governance"),
    # --- gap-solutions ---
    "capability_change": ("能力变更：优化、整合、新建、退役之一及其范围。", "core", "togaf-gap-solutions"),
    "guide:product_component": ("产品组件：产品架构中的构成单元。", "guide-extension", "togaf-gap-solutions"),
    "guide:product_function": ("产品功能：产品对外提供的功能项。", "guide-extension", "togaf-gap-solutions"),
    "guide:product_interface": ("产品接口：产品与其他单元的交互约定。", "guide-extension", "togaf-gap-solutions"),
    "option_score": ("选项评分：某候选方案在某准则上的分值及其证据。", "core", "togaf-gap-solutions"),
    "transition_architecture": ("过渡架构：功能完整、可运营的中间状态。", "core", "togaf-gap-solutions"),
    # --- migration-roadmap ---
    "guide:estimate_check": ("估算充分性检查：估算是否有依据、区间与假设。", "guide-extension", "togaf-migration-roadmap"),
    "guide:implementation_factor": ("实施因素：影响实施顺序与可行性的条件。", "guide-extension", "togaf-migration-roadmap"),
    "guide:portfolio_assignment": ("组合分配：工作包归属的组合主题。", "guide-extension", "togaf-migration-roadmap"),
    "guide:project_authorization": ("项目授权：工作包被授权进入执行的记录。", "guide-extension", "togaf-migration-roadmap"),
    "rollback_step": ("回退步骤：触发条件、责任人、前置条件与验证方法。", "core", "togaf-migration-roadmap"),
    # --- organization-roles ---
    "guide:sustainability_learning": ("可持续性学习：面向可持续目标的能力培养项。", "guide-extension", "togaf-organization-roles"),
    "skill_development": ("技能发展：某技能的成长路径与熟练度证据。", "core", "togaf-organization-roles"),
    # --- security-risk ---
    "impact_scenario": ("影响情景：某一威胁实现后的业务后果路径。", "core", "togaf-security-risk"),
    "legal_obligation": ("法律义务：法规要求的具体义务与适用条件。", "core", "togaf-security-risk"),
    "risk_treatment": ("风险处置：规避、降低、转移、接受的选定方式与残余风险。", "core", "togaf-security-risk"),
    "security_classification": ("安全分类：信息或资产的分级与处理要求。", "core", "togaf-security-risk"),
    "security_component": ("安全组件：实现安全服务的构成单元。", "core", "togaf-security-risk"),
    "security_impact": ("安全影响：安全事件对业务的具体影响估计。", "core", "togaf-security-risk"),
    "security_policy": ("安全政策：必须遵守的安全规则与适用范围。", "core", "togaf-security-risk"),
    "security_resource": ("安全资源：投入某项控制的人力、工具与预算。", "core", "togaf-security-risk"),
    "training_need": ("培训需求：某角色在安全或合规上的能力缺口。", "core", "togaf-security-risk"),
    "transition_risk": ("过渡风险：迁移或切换期间特有的风险。", "core", "togaf-security-risk"),
    "trust_party": ("信任方：建立信任关系的外部或内部主体。", "core", "togaf-security-risk"),
    # --- application-architecture ---
    "microservice": ("微服务：独立部署、单一职责、自有数据边界的服务单元。", "core", "togaf-application-architecture"),
    "service_boundary": ("服务边界：服务职责与数据所有权的分界。", "core", "togaf-application-architecture"),
    "ops:msa_value_resource": ("微服务价值与资源：服务产生的价值与其消耗的资源。", "guide-extension", "togaf-application-architecture"),
    # --- technology-architecture ---
    "interoperability_issue": ("互操作问题：两系统间在语义、协议或数据上的障碍。", "core", "togaf-technology-architecture"),
    "microservice_guideline": ("微服务技术指引：部署、观测、失败隔离的技术要求。", "core", "togaf-technology-architecture"),
    "ops:msa_governance": ("微服务联邦治理：跨团队的治理安排与决策权。", "guide-extension", "togaf-technology-architecture"),
    "ops:msa_readiness": ("微服务就绪度：组织与平台是否具备拆分条件。", "guide-extension", "togaf-technology-architecture"),
    # --- vision-scenarios ---
    "scenario": ("业务场景：问题、环境、SMART 成果与参与者的结构化描述。", "core", "togaf-vision-scenarios"),
}

# ---------------------------------------------------------------------------
# Relationship definitions. All keys carry a namespace prefix, so they satisfy
# apply_capability_addenda.py's colon requirement.
# ---------------------------------------------------------------------------
RELATIONSHIP_DEFINITIONS = {
    "g20f:allocated-to-sbb": (["abb"], ["sbb"], "构建块规定分配到解决方案实现，不代表已部署或已批准。"),
    "g20f:constrains-story": (["guide:agile_constraint", "constraint"], ["guide:backlog_item", "guide:agile_sprint"], "约束限定故事或冲刺的可选范围。"),
    "g20f:included-in-mva": (["guide:backlog_item", "abb"], ["guide:mva_scope"], "工作项被纳入最小可行架构的边界内。"),
    "g20f:refines": (["guide:backlog_item", "guide:agile_sprint"], ["guide:backlog_item", "guide:mva_scope"], "后者细化前者的范围或验收。"),
    "g20f:story-depends-on": (["guide:backlog_item"], ["guide:backlog_item"], "故事间的前置依赖，非时间顺序断言。"),
    "g234:coverage-of-asset": (["ops:functional_coverage"], ["metadata_asset"], "覆盖记录针对的具体元数据资产。"),
    "g234:supports-requirements": (["metadata_component", "g234:metadata-tool"], ["requirement", "analytics_requirement"], "组件支撑某条元数据要求。"),
    "g234:tool-coverage-claim": (["g234:metadata-tool"], ["ops:functional_coverage"], "工具对某功能覆盖的声明，需实现证据支持。"),
    "guide:agile_collaborates": (["guide:agile_context"], ["guide:agile_activity"], "协作方式参与某活动。"),
    "guide:agile_continues": (["guide:agile_sprint"], ["guide:agile_sprint"], "冲刺的延续关系，保留原目标。"),
    "guide:agile_finalizes": (["guide:agile_sprint"], ["guide:backlog_item"], "冲刺完成某待办项。"),
    "guide:agile_handoff": (["guide:agile_activity"], ["guide:agile_sprint"], "活动移交给下一冲刺。"),
    "guide:allocates_function": (["guide:product_component"], ["guide:product_function"], "组件分配承担某产品功能。"),
    "guide:backlog_depends_on": (["guide:backlog_item"], ["guide:backlog_item"], "待办项之间的前置依赖。"),
    "guide:builds_deployment": (["microservice"], ["technology_service", "platform"], "服务构建所需的部署能力。"),
    "guide:deploys_instance": (["technology_service", "platform"], ["microservice"], "平台承载某服务实例。"),
    "guide:interface_receiver": (["interface"], ["application", "microservice"], "接口的接收方。"),
    "guide:interface_sender": (["interface"], ["application", "microservice"], "接口的发送方。"),
    "guide:reference_classifies": (["guide:government_reference_node"], ["guide:government_reference_node"],
        "目录规定的部门→功能→服务分类方向；不表示本地组织汇报、运行依赖或能力组成。"),
    "guide:scheduled_in": (["architecture_activity", "work_package"], ["guide:agile_sprint", "milestone"], "活动被排入某冲刺或里程碑。"),
    "guide:uses_neutral_library": (["application", "microservice"], ["abb", "standard"], "实现复用了中立库或标准。"),
    "ops:data_derivation": (["data_quality_measure", "data_issue"], ["metadata_asset", "data_entity"], "派生关系：前者由后者计算或推导。"),
    "ops:governance_aligns": (["ops:msa_governance", "guide:governance-check"], ["organization", "role"], "治理安排与组织职责对齐。"),
    "ops:governance_constrains": (["ops:msa_governance", "security_policy"], ["microservice", "application"], "治理规则约束服务或应用。"),
    "ops:governance_extends": (["ops:msa_governance"], ["control_framework", "standard"], "治理安排扩展既有框架。"),
    "ops:governance_supports": (["ops:msa_governance"], ["requirement", "criterion"], "治理安排支撑某要求。"),
    "project:policy_specializes": (["security_policy"], ["security_policy"], "具体政策细化上位政策，不覆盖。"),
    "project:service_partition": (["microservice"], ["service_boundary"], "服务划分到某边界。"),
    "project:wbs_decomposes": (["architecture_activity", "architecture_task"], ["architecture_task"], "工作分解：任务属于活动。"),
}

# ---------------------------------------------------------------------------
# Patches for the 12 entity types with no declared required attributes.
# ---------------------------------------------------------------------------
ATTRIBUTE_PATCHES = [
    ("business-impact-analysis", "risk_asset",
     ["asset_id", "criticality", "owner", "confidentiality_need", "integrity_need", "availability_need"]),
    ("business-risk-register", "threat_event",
     ["threat_actor_ref", "event_time", "likelihood_scale", "evidence"]),
    ("security-services-catalog", "control_objective",
     ["objective_statement", "control_ref", "evidence_ref", "test_result"]),
    ("data-quality-assessment", "data_quality_rule",
     ["dimension", "rule_expression", "threshold", "measure_period", "owner"]),
    ("architecture-project-schedule", "milestone",
     ["due_date", "exit_criteria", "owner", "dependency"]),
    ("options-decision-matrix", "option",
     ["option_id", "criteria_scores", "rationale", "tradeoff"]),
    ("decision-delegation-register", "decision_record",
     ["question", "options_considered", "decision", "authority", "rationale", "date"]),
    ("project-work-package-authorization", "project",
     ["scope", "sponsor", "start", "end", "budget", "status"]),
    ("architecture-maturity-scorecard", "assessment_result",
     ["subject_ref", "method_ref", "result_value", "unit", "period", "evidence"]),
    ("architecture-skill-matrix", "skill",
     ["skill_name", "proficiency_level", "evidence", "holder_ref"]),
    ("interoperability-assessment", "equipment",
     ["equipment_class", "work_center_ref", "criticality", "maintenance_plan_ref"]),
    ("environmental-is-assessment", "phosphogypsum_record",
     ["generated_tonnage", "utilised_tonnage", "stockpiled_tonnage", "utilisation_rate", "period"]),
]

# ---------------------------------------------------------------------------
# Calculator registrations. Nine can reuse operators that analyze.py already
# implements; the rest are recorded as having no deterministic calculator so
# the registry stops implying a numeric answer exists.
# ---------------------------------------------------------------------------
CALCULATOR_LINKS = {
    "architecture-backlog-method": "architecture-backlog-trace-review",
    "mdm-business-function-coverage-method": "metadata-application-coverage-review",
    "mdm-application-function-coverage-method": "metadata-application-coverage-review",
    "mdm-operational-ten-questions-method": "set-based-options-review",
    "mdm-match-merge-arbitration-method": "delivery-style-review",
    "dorp-record-method": "project-highlight-review",
    "decision-delegation-register-method": "project-management-strategy-review",
    "technical-debt-register-method": "change-profile-checklist",
    "architecture-description-formality-review-method": "ea-point-of-view-review",
}

NO_CALCULATOR_REASON = (
    "该方法的结论依赖领域判断或定性证据，本项目未定义确定性算子；"
    "结果须由技能按 method.md 执行并由责任方确认，不得输出伪数值。"
)

# ---------------------------------------------------------------------------
# Keyword to assertion-code map for deriving `expected` from misreadings.
# ---------------------------------------------------------------------------
CODE_HINTS = [
    ("基数", "invalid-cardinality"),
    ("一对多", "invalid-cardinality"),
    ("批准", "approval-without-evidence"),
    ("签署", "approval-without-evidence"),
    ("追溯", "dangling-reference"),
    ("引用", "dangling-reference"),
    ("属性", "missing-attribute"),
    ("字段", "missing-attribute"),
    ("未表达", "attribute-not-expressed"),
    ("不可见", "attribute-not-expressed"),
    ("类型", "relation-endpoint-type"),
    ("端点", "relation-endpoint-type"),
    ("方向", "matrix-direction"),
    ("CRUD", "matrix-code"),
    ("状态", "mixed-evolution"),
    ("基线", "mixed-evolution"),
    ("目标状态", "mixed-evolution"),
    ("范围", "view-edge-outside"),
    ("越界", "view-edge-outside"),
    ("过渡", "transition-operability-gap"),
    ("命名空间", "extension-namespace"),
    ("前缀", "extension-namespace"),
    ("重定义", "core-vocabulary-override"),
    ("覆盖", "core-vocabulary-override"),
    ("命名", "duplicate-name"),
    ("重复", "duplicate-id"),
    ("空", "empty-view"),
    ("缺失", "missing-attribute"),
    ("未核实", "missing-evidence"),
    ("无证据", "missing-evidence"),
    ("来源", "missing-evidence"),
]

FALLBACK_CODE = "missing-evidence"

# Domain assertion codes that the registry uses in counterexamples. Codes listed in
# ENFORCED_CODES are emitted by scripts/contract_semantics.py and are therefore
# machine-checked; any code left out is declared but not yet enforced, and the
# verifier must report it as such rather than count it as covered.
ENFORCED_CODES = {
    "reject-unsupported-commitment": "框架接触的承诺缺少证据。",
    "factor-evidence-gap": "实施因素缺少来源或证据。",
    "all-staff-coverage-gap": "技能矩阵覆盖人数少于应覆盖人数。",
    "authorization-not-ready": "前置条件未接受而授权或执行已通过。",
    "closure-products-not-accepted": "收尾标记完成但成果未接受。",
    "criterion-result-contradiction": "判据判定通过但观察值未达要求。",
    "dependency-cycle": "依赖存在环，无法排序。",
    "dual-entry-trace-gap": "双入口机会未连接任一入口。",
    "learning-evidence-gap": "学习项缺少效果证据。",
    "missing-project-contingency": "估算为假设但无应急或容差。",
    "procurement-transparency-gap": "采购要求缺少透明度或生命周期证据。",
    "carbon-data-metadata-gap": "碳数据缺少边界、单位或因子来源。",
    "scope3-subset-exceeds-total": "排放子集数值超过所属总量。",
    "unsourced-maturity-rating": "成熟度评级没有证据来源。",
}

DECLARED_ASSERTION_CODES = dict(ENFORCED_CODES)


def read(path):
    return json.loads(Path(path).read_text())


def example_relationship_definitions():
    """Harvest extension relationship definitions declared inside profile examples.

    An example that uses a namespaced relationship must define it, and those
    definitions are the authoritative usage: they were written against real
    endpoints. Generating a competing definition would break build_full_example,
    which refuses to reconcile two different meanings for one name.
    """
    caps = read(ROOT / "capabilities.json")
    found = {}
    for item in list(caps["profiles"]) + list(caps["work_products"]):
        local = ((item.get("example") or {}).get("extensions") or {}).get("relationship_types") or {}
        for name, definition in local.items():
            found.setdefault(name, definition)
    return found


def existing_relationship_names():
    """Relationships already defined in the registry or the base relationship set.

    An existing definition was written with more care than a generated one and is
    already registered; re-declaring it would either clash or silently degrade the
    meaning, so those names are skipped and only genuine gaps are added.
    """
    caps = read(ROOT / "capabilities.json")
    metamodel = read(ROOT / "metamodel.json")
    names = set(caps.get("extension_relationship_definitions", {}))
    names |= set(metamodel.get("relationships", {}))
    return names


def normalize_code(text):
    """Pick the first usable assertion token from a compound or prose expectation.

    Legacy counterexamples sometimes list two codes joined by 或/、/and, or append
    prose. The first ASCII identifier-looking token is taken as the machine-checkable
    expectation; the untouched original is preserved in original_expected_text.
    """
    if not isinstance(text, str):
        return None
    for token in re.split(r"(?:\s|或|、|/|与|and)+", text.strip()):
        token = token.strip("。；;，,()（）")
        if re.fullmatch(r"[a-z][a-z0-9-]{2,}", token):
            return token
    return None


def is_code(value):
    """A machine-checkable expectation is one ASCII lowercase identifier.

    Chinese characters count as alphanumeric in Python, so a plain isalnum() test
    accepts compound strings like `a或b`. Requiring an ASCII-only match is the only
    reliable way to keep this field machine-checkable.
    """
    if not isinstance(value, str) or not value or value != value.strip():
        return False
    return bool(re.fullmatch(r"[a-z][a-z0-9-]*", value))


def pick_code(text):
    """Map a misreading to one existing assertion code. Unknown stays explicit."""
    for keyword, code in CODE_HINTS:
        if keyword in text:
            return code
    return FALLBACK_CODE


def error_input(misreading, wp_name):
    """Turn a misreading into a concrete wrong input description."""
    cleaned = misreading.strip().rstrip("。")
    return f"对「{wp_name}」给出：{cleaned}"


def build_entity_package():
    return {
        "schema_version": "capability-addenda/1",
        "id": "skill-contract-entity-types",
        "status": "registered-not-accepted",
        "portability": "portable",
        "rule_origin_policy": "project-operational-convention",
        "owner": "togaf-architecture-workbench",
        "sources": [
            "validate.py 可接受词表（第 38、44 行）与 capabilities.json 声明类型的差集",
            "metamodel.json 现有定义",
            "relationships.json 现有 82 条关系",
        ],
        "notice": (
            "These definitions close a vocabulary gap so the validator can type-check declared "
            "types. They are project-operational readings, not official TOGAF definitions; "
            "the formal body of C220 is not held by this project."
        ),
        "entity_definitions": {
            name: {
                "meaning": meaning,
                "level": level,
                "owner_domain" if level == "core" else "owner_guide": owner,
                "definition_origin": "project-operational-convention",
            }
            for name, (meaning, level, owner) in ENTITY_DEFINITIONS.items()
        },
        "relationship_definitions": {
            **{
                name: definition
                for name, definition in example_relationship_definitions().items()
                if name not in existing_relationship_names()
            },
            **{
                name: {
                    "source_types": sources,
                    "target_types": targets,
                    "meaning": meaning,
                    "definition_origin": "project-operational-convention",
                }
                for name, (sources, targets, meaning) in RELATIONSHIP_DEFINITIONS.items()
                if name not in existing_relationship_names()
                and name not in example_relationship_definitions()
            },
        },
    }


def build_contract_package():
    caps = read(ROOT / "capabilities.json")
    patches = []

    for wp in caps["work_products"]:
        misreadings = wp.get("misreadings") or []
        if not misreadings:
            raise ValueError("工作产品无 misreadings，须人工补：" + wp["id"])
        existing = wp.get("counterexample") or {}
        set_fields = {}

        if existing:
            # Legacy counterexamples state the expectation in prose or list two
            # codes. Keep that prose in `why`/`original_expected_text` and expose
            # one machine-checkable code, so the same record serves both readers.
            if not is_code(existing.get("expected")):
                prose = existing.get("expected") or ""
                code = normalize_code(prose) or pick_code(prose + " " + misreadings[0])
                set_fields["counterexample"] = {
                    "input": existing.get("input") or error_input(misreadings[0], wp.get("name_zh") or wp["id"]),
                    "expected": code,
                    "why": existing.get("why") or prose or misreadings[0],
                    "original_expected_text": prose,
                }
        else:
            set_fields["counterexample"] = {
                "input": error_input(misreadings[0], wp.get("name_zh") or wp["id"]),
                "expected": pick_code(misreadings[0]),
                "why": misreadings[0],
            }

        if not wp.get("modification_example"):
            set_fields["modification_example"] = {
                "change": f"在「{wp.get('name_zh') or wp['id']}」的范围内新增或修改一项，检查下游是否随之变化",
                "expected": "受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用",
            }
        if set_fields:
            patches.append({"group": "work_products", "id": wp["id"], "set": set_fields})

    for method in caps["analysis_methods"]:
        # Methods without explicit checks still have analysis_steps; the last step
        # names the judgement that can be got wrong, so it stands in as the source.
        source_text = (method.get("checks") or [None])[0]
        if not source_text:
            steps = method.get("analysis_steps") or method.get("steps") or []
            if not steps:
                raise ValueError("方法既无 checks 也无 analysis_steps，须人工补：" + method["id"])
            source_text = steps[-1]
        set_fields = {}
        existing_ce = method.get("counterexample") or {}
        if existing_ce and not is_code(existing_ce.get("expected")):
            prose = existing_ce.get("expected") or ""
            code = normalize_code(prose) or pick_code(prose + " " + source_text)
            set_fields["counterexample"] = {
                "input": existing_ce.get("input") or f"执行「{method.get('name') or method['id']}」时跳过或误做：{source_text}",
                "expected": code,
                "why": existing_ce.get("why") or prose or source_text,
                "original_expected_text": prose,
            }
        elif not existing_ce:
            set_fields["counterexample"] = {
                "input": f"执行「{method.get('name') or method['id']}」时跳过或误做：{source_text}",
                "expected": pick_code(source_text),
                "why": source_text,
            }
        if method.get("calculation_policy") and not method.get("calculator"):
            if method["id"] in CALCULATOR_LINKS:
                set_fields["calculator_id"] = CALCULATOR_LINKS[method["id"]]
                set_fields["implementation_status"] = "operational-steps-with-explicit-input-calculator"
            else:
                set_fields["calculator_status"] = "no-deterministic-calculator"
                set_fields["calculator_reason"] = NO_CALCULATOR_REASON
        if set_fields:
            patches.append({"group": "analysis_methods", "id": method["id"], "set": set_fields})

    for wp_id, entity, fields in ATTRIBUTE_PATCHES:
        patches.append({
            "group": "work_products",
            "id": wp_id,
            "add": {"required_attributes": {entity: fields}},
            "note": f"{entity} 的字段为本项目补充，非原文强制字段",
        })

    return {
        "schema_version": "capability-addenda/1",
        "id": "skill-contract-counterexamples",
        "status": "registered-not-accepted",
        "portability": "portable",
        "rule_origin_policy": "project-operational-convention",
        "owner": "togaf-architecture-workbench",
        "sources": [
            "capabilities.json 的 misreadings / checks / calculation_policy",
            "validate.py 与 profile_render.py 的断言码",
        ],
        "notice": (
            "Every counterexample states a wrong input and the assertion code it must trigger. "
            "A counterexample whose expected value is not an existing assertion code is rejected "
            "at build time; a passing build grants no acceptance."
        ),
        "patches": patches,
        "analysis_methods": build_new_methods(),
        "declared_assertion_codes": DECLARED_ASSERTION_CODES,
    }


def build_new_methods():
    """Four methods that give togaf-migration-roadmap a computational basis."""
    return [
        {
            "id": "dependency-topological-order",
            "name": "工作包依赖拓扑排序",
            "owner": "togaf-migration-roadmap",
            "source_refs": ["G186 §8", "G188 §3.2"],
            "required_inputs": ["工作包清单", "依赖边", "硬依赖与软依赖标记"],
            "analysis_steps": ["建立依赖图", "检测环并报告", "按拓扑序排出批次", "标出软依赖可并行段"],
            "output_work_products": ["portfolio-theme-work-package-register"],
            "checks": ["存在环却直接给出顺序，未报告环"],
            "missing_input_policy": "缺依赖标记时只输出候选序与缺口，不声称关键路径。",
            "definition_status": "project-operational-method",
            "implementation_status": "specified-awaiting-behavioral-validation",
            "counterexample": {
                "input": "依赖图中 A→B→C→A 成环，仍输出 A、B、C 的顺序",
                "expected": "cycle",
                "why": "存在环却直接给出顺序，未报告环",
            },
            "reference_document": "references/analysis-methods/dependency-topological-order.md",
        },
        {
            "id": "transition-operability-check",
            "name": "过渡架构可运营性判定",
            "owner": "togaf-migration-roadmap",
            "source_refs": ["G248 §2", "G186 §9"],
            "required_inputs": ["过渡架构", "运营条件五项（人员、系统、数据、控制、回退）"],
            "analysis_steps": ["逐项检查运营条件", "缺项即判不可运营", "输出缺口 ID 与补齐动作"],
            "output_work_products": ["transition-architecture-model"],
            "checks": ["只给进度百分比就判定过渡可运营"],
            "missing_input_policy": "运营条件缺项时判为不可运营并列出缺项，不按比例折算。",
            "definition_status": "project-operational-method",
            "implementation_status": "specified-awaiting-behavioral-validation",
            "counterexample": {
                "input": "过渡架构仅给出「完成 70%」，未说明人员、系统、数据、控制与回退",
                "expected": "transition-operability-gap",
                "why": "只给进度百分比就判定过渡可运营",
            },
            "reference_document": "references/analysis-methods/transition-operability-check.md",
        },
        {
            "id": "work-package-prioritization",
            "name": "工作包优先级判定",
            "owner": "togaf-migration-roadmap",
            "source_refs": ["G186 §8.4", "G176 §12.8"],
            "required_inputs": ["工作包", "评价准则", "准则权重及其来源"],
            "analysis_steps": ["校验每条权重的来源", "加权计算", "报告权重敏感区间"],
            "output_work_products": ["portfolio-estimate-sufficiency-check"],
            "checks": ["权重无来源却直接加权算出总分"],
            "missing_input_policy": "权重缺来源时不计算总分，只列准则与候选。",
            "definition_status": "project-operational-method",
            "implementation_status": "specified-awaiting-behavioral-validation",
            "counterexample": {
                "input": "五项准则各给 20% 权重，但无任何来源或裁决记录",
                "expected": "missing-evidence",
                "why": "权重无来源却直接加权算出总分",
            },
            "reference_document": "references/analysis-methods/work-package-prioritization.md",
        },
        {
            "id": "benefit-realization-trigger",
            "name": "收益实现复评触发",
            "owner": "togaf-migration-roadmap",
            "source_refs": ["G184 §10.1.7", "G184 §11.4"],
            "required_inputs": ["目标值与期间", "实测值与观测窗", "归因边界"],
            "analysis_steps": ["对齐目标与实测的口径", "计算偏差", "按观测窗判定是否触发复评"],
            "output_work_products": ["value-realization-assessment"],
            "checks": ["把计划值当实测值计算偏差"],
            "missing_input_policy": "无实测值时只报未观测，不填计划值。",
            "definition_status": "project-operational-method",
            "implementation_status": "specified-awaiting-behavioral-validation",
            "counterexample": {
                "input": "以计划收益 12% 作为实测值参与偏差计算",
                "expected": "measurement-evidence-gap",
                "why": "把计划值当实测值计算偏差",
            },
            "reference_document": "references/analysis-methods/benefit-realization-trigger.md",
        },
    ]


def diff_summary(package, caps, metamodel):
    """Report what the package would add, without writing registry files."""
    entities = [k for k in package.get("entity_definitions", {}) if k not in metamodel["entity_types"]]
    relations = [k for k in package.get("relationship_definitions", {}) if k not in metamodel["relationships"]]
    clashes = [k for k, v in package.get("entity_definitions", {}).items()
               if k in metamodel["entity_types"] and metamodel["entity_types"][k] != v]
    return {"new_entities": len(entities), "new_relationships": len(relations),
            "value_clashes": clashes}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", default=str(ADDENDA))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    caps = read(ROOT / "capabilities.json")
    metamodel = read(ROOT / "metamodel.json")

    entities = build_entity_package()
    contracts = build_contract_package()

    summary_e = diff_summary(entities, caps, metamodel)
    print("entity package:", json.dumps(summary_e, ensure_ascii=False))
    print("contract patches:", len(contracts["patches"]),
          "| new methods:", len(contracts["analysis_methods"]))
    if summary_e["value_clashes"]:
        raise SystemExit("实体定义与既有 metamodel 值冲突，拒绝写入：" + str(summary_e["value_clashes"]))

    out = Path(args.out_dir)
    if args.dry_run:
        print("dry-run: no file written")
        return
    out.mkdir(parents=True, exist_ok=True)
    (out / "skill-contract-entity-types.json").write_text(
        json.dumps(entities, ensure_ascii=False, indent=2) + "\n")
    (out / "skill-contract-counterexamples.json").write_text(
        json.dumps(contracts, ensure_ascii=False, indent=2) + "\n")
    print("wrote", out / "skill-contract-entity-types.json")
    print("wrote", out / "skill-contract-counterexamples.json")


if __name__ == "__main__":
    main()
