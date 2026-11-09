# C-MDM业务功能参考覆盖

`profile_id`: mdm-business-function-coverage；`artifact_id`: customer-mdm-model；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G21B §5.2.1表5-3。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-operations-1。

{
  "id": "mdm-business-function-coverage",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "结构化表格，含完整属性、方向和证据；不是来源图模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：ops:functional_coverage。关系类型：。

```json
{
  "entities": {
    "ops:functional_coverage": [
      "reference_id",
      "reference_kind",
      "reference_name",
      "reference_definition",
      "reference_group",
      "reference_level",
      "reference_scope",
      "source_locator",
      "reference_identity",
      "project_scope",
      "coverage_status",
      "implementation_ref",
      "evidence_detail",
      "gap_action",
      "source_uncertainty"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 源表ID全集覆盖且不重复
- 已见必须有具体实现/证据，计划不算已实现
- 不适用必须有范围理由
- 参考表行不是软件组件或独立制品
- 保留本地翻译不确定

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构完整案例；手工分析、表格操作语义，不冒称源图复刻。",
  "raw_input": "examples/addenda/operations/mdm-business-function-coverage/raw-brief.md",
  "analysis_path": "examples/addenda/operations/mdm-business-function-coverage/analysis.md",
  "sources": [
    {
      "id": "case-source",
      "kind": "example",
      "description": "海岚客户数据只做本次自有记录试点。服务主管愿任数据所有者但管家未指派，外部数据采购不在试点范围。其余业务活动尚未收证。按29参考功能完整登记，不能把参考模型当组织已成熟。",
      "locator": "raw-brief.md"
    }
  ],
  "entities": [
    {
      "id": "MDMC-B-G21B-T5-3-01",
      "type": "ops:functional_coverage",
      "name": "定义 C-MDM 目标与路线图",
      "attributes": {
        "reference_id": "G21B-T5-3-01",
        "reference_kind": "business_function",
        "reference_name": "定义 C-MDM 目标与路线图",
        "reference_definition": "定义 C-MDM 能力的转型步骤，明确各步骤目标及实现计划。",
        "reference_group": "A. C-MDM 能力管理与治理",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L570",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-02",
      "type": "ops:functional_coverage",
      "name": "定义并吸纳数据所有者与数据管家",
      "attributes": {
        "reference_id": "G21B-T5-3-02",
        "reference_kind": "business_function",
        "reference_name": "定义并吸纳数据所有者与数据管家",
        "reference_definition": "在常态化运营（BAU）中识别并吸纳业务数据所有者，聚焦内核客户数据。",
        "reference_group": "A. C-MDM 能力管理与治理",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L571",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "planned",
        "implementation_ref": "GOV-owner",
        "evidence_detail": "虚构客户服务主管愿任客户数据所有者，管家未指派",
        "gap_action": "补正式职责和管家可用容量",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-03",
      "type": "ops:functional_coverage",
      "name": "定义并运行数据治理原则",
      "attributes": {
        "reference_id": "G21B-T5-3-03",
        "reference_kind": "business_function",
        "reference_name": "定义并运行数据治理原则",
        "reference_definition": "定义客户主数据的数据治理原则，并建立组织与机构（如委员会）运行这些原则。",
        "reference_group": "A. C-MDM 能力管理与治理",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L572",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-04",
      "type": "ops:functional_coverage",
      "name": "协调决策与优先级",
      "attributes": {
        "reference_id": "G21B-T5-3-04",
        "reference_kind": "business_function",
        "reference_name": "协调决策与优先级",
        "reference_definition": "建立并运转数据治理委员会，确保 C-MDM 路线图在实体内有效实施，保证客户数据决策一致，并评审关键仲裁。",
        "reference_group": "A. C-MDM 能力管理与治理",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L573",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-05",
      "type": "ops:functional_coverage",
      "name": "定义团队服务并运营 SLA",
      "attributes": {
        "reference_id": "G21B-T5-3-05",
        "reference_kind": "business_function",
        "reference_name": "定义团队服务并运营 SLA",
        "reference_definition": "定义 C-MDM 团队服务目录、潜在用户与服务接口（工单工具、电话、集中邮箱等），为每项服务定义并遵守 SLA。",
        "reference_group": "A. C-MDM 能力管理与治理",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L574",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-06",
      "type": "ops:functional_coverage",
      "name": "设计客户数据模型",
      "attributes": {
        "reference_id": "G21B-T5-3-06",
        "reference_kind": "business_function",
        "reference_name": "设计客户数据模型",
        "reference_definition": "设计并记录客户主数据模型（信息模型、数据库模型、属性定义与类型等）。",
        "reference_group": "B. C-MDM 设计",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L580",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-07",
      "type": "ops:functional_coverage",
      "name": "设计 C-MDM 架构原则并确保数据方案一致性",
      "attributes": {
        "reference_id": "G21B-T5-3-07",
        "reference_kind": "business_function",
        "reference_name": "设计 C-MDM 架构原则并确保数据方案一致性",
        "reference_definition": "定义客户主数据需求（存储、传输、发布、转换、归档、元数据、质量、主/参考数据管理等）并符合合规标准；定义数据架构框架；参与 IT 路线图与投资评估；确保关键数据符合合规与安全标准。",
        "reference_group": "B. C-MDM 设计",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L581",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-08",
      "type": "ops:functional_coverage",
      "name": "支持客户数据管理实施",
      "attributes": {
        "reference_id": "G21B-T5-3-08",
        "reference_kind": "business_function",
        "reference_name": "支持客户数据管理实施",
        "reference_definition": "提供资源，确保 C-MDM 系统与团队持续满足要求；按路线图分步实施。",
        "reference_group": "B. C-MDM 设计",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L582",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-09",
      "type": "ops:functional_coverage",
      "name": "形式化客户主数据校验工作流、质量与业务规则",
      "attributes": {
        "reference_id": "G21B-T5-3-09",
        "reference_kind": "business_function",
        "reference_name": "形式化客户主数据校验工作流、质量与业务规则",
        "reference_definition": "形式化业务规则与数据管家工作流，保证既有数据质量提升，并确保新数据更新流程设计合理。",
        "reference_group": "B. C-MDM 设计",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L583",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-10",
      "type": "ops:functional_coverage",
      "name": "帮助业务调整流程以确保数据质量",
      "attributes": {
        "reference_id": "G21B-T5-3-10",
        "reference_kind": "business_function",
        "reference_name": "帮助业务调整流程以确保数据质量",
        "reference_definition": "在纳入新数据范围或新用例时，帮助业务调整受影响流程；变革管理投入不可低估。",
        "reference_group": "B. C-MDM 设计",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L584",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-11",
      "type": "ops:functional_coverage",
      "name": "定义并运行数据访问模型",
      "attributes": {
        "reference_id": "G21B-T5-3-11",
        "reference_kind": "business_function",
        "reference_name": "定义并运行数据访问模型",
        "reference_definition": "按安全、隐私/合规与价值分类定义数据访问画像，并通过 C-MDM 运行这些访问模型。",
        "reference_group": "B. C-MDM 设计",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L585",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-12",
      "type": "ops:functional_coverage",
      "name": "定义、维护并共享客户数据文档",
      "attributes": {
        "reference_id": "G21B-T5-3-12",
        "reference_kind": "business_function",
        "reference_name": "定义、维护并共享客户数据文档",
        "reference_definition": "在共享存储库中维护与主数据对象相关的规则；维护数据字典与术语表；资本化并共享信息与数据模型；记录消费点、采集点与数据流；记录数据管家流程（谁在何时、如何对客户数据负责）。",
        "reference_group": "B. C-MDM 设计",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L586",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-13",
      "type": "ops:functional_coverage",
      "name": "定义、遵循并监控数据保留规则",
      "attributes": {
        "reference_id": "G21B-T5-3-13",
        "reference_kind": "business_function",
        "reference_name": "定义、遵循并监控数据保留规则",
        "reference_definition": "保留规则是数据生命周期的一部分，明确各类数据的保留期限（因隐私删除或因税务保留）。",
        "reference_group": "B. C-MDM 设计",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L587",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-14",
      "type": "ops:functional_coverage",
      "name": "接收并管理客户数据相关请求（GDPR 等）",
      "attributes": {
        "reference_id": "G21B-T5-3-14",
        "reference_kind": "business_function",
        "reference_name": "接收并管理客户数据相关请求（GDPR 等）",
        "reference_definition": "接收所服务业务方提出的请求（如经纪人/代理提出的数据更正请求、客户关于其数据的请求、运营服务上报的质量问题），并将其路由给正确的人员/数据管家。",
        "reference_group": "C. C-MDM 运营",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L593",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-15",
      "type": "ops:functional_coverage",
      "name": "评估并管理客户主数据质量问题",
      "attributes": {
        "reference_id": "G21B-T5-3-15",
        "reference_kind": "business_function",
        "reference_name": "评估并管理客户主数据质量问题",
        "reference_definition": "检测并管理数据质量问题，属于 MDM 运营的一部分（区别于质量度量）。",
        "reference_group": "C. C-MDM 运营",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L594",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-16",
      "type": "ops:functional_coverage",
      "name": "纠正数据问题",
      "attributes": {
        "reference_id": "G21B-T5-3-16",
        "reference_kind": "business_function",
        "reference_name": "纠正数据问题",
        "reference_definition": "恢复真相并据此更新数据。",
        "reference_group": "C. C-MDM 运营",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L595",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-17",
      "type": "ops:functional_coverage",
      "name": "校验客户合并",
      "attributes": {
        "reference_id": "G21B-T5-3-17",
        "reference_kind": "business_function",
        "reference_name": "校验客户合并",
        "reference_definition": "人工仲裁两个客户的合并：核验这两个客户，使其成为同一个人并最终合并。",
        "reference_group": "C. C-MDM 运营",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L596",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-18",
      "type": "ops:functional_coverage",
      "name": "确保运营业务流程获得适当的 C-MDM 数据与服务",
      "attributes": {
        "reference_id": "G21B-T5-3-18",
        "reference_kind": "business_function",
        "reference_name": "确保运营业务流程获得适当的 C-MDM 数据与服务",
        "reference_definition": "确保运营业务用户（消费者或生产者）拥有适当的界面，以最优方式支撑其流程；了解业务需求与痛点。",
        "reference_group": "C. C-MDM 运营",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L597",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-19",
      "type": "ops:functional_coverage",
      "name": "支持数据生产方应用的新集成",
      "attributes": {
        "reference_id": "G21B-T5-3-19",
        "reference_kind": "business_function",
        "reference_name": "支持数据生产方应用的新集成",
        "reference_definition": "该活动属于常态化运营（BAU）。对数据生产方应用新集成的支持方式管理良好，以新客户群体可持续扩展 C-MDM 范围的流程已得到掌控。",
        "reference_group": "D. C-MDM 范围与用途扩展（Extension of C-MDM Scope and Usages）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L603",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-20",
      "type": "ops:functional_coverage",
      "name": "支持数据消费方应用的新集成",
      "attributes": {
        "reference_id": "G21B-T5-3-20",
        "reference_kind": "business_function",
        "reference_name": "支持数据消费方应用的新集成",
        "reference_definition": "该活动属于常态化运营（BAU）。对数据消费方应用新集成的支持方式管理良好；新的数据消费有清晰定义的用例作为语境。",
        "reference_group": "D. C-MDM 范围与用途扩展（Extension of C-MDM Scope and Usages）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L604",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-21",
      "type": "ops:functional_coverage",
      "name": "支持新的外部数据源集成",
      "attributes": {
        "reference_id": "G21B-T5-3-21",
        "reference_kind": "business_function",
        "reference_name": "支持新的外部数据源集成",
        "reference_definition": "该活动属于常态化运营（BAU）。在 C-MDM 生态中集成新外部数据源的方式管理良好。",
        "reference_group": "D. C-MDM 范围与用途扩展（Extension of C-MDM Scope and Usages）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L605",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-22",
      "type": "ops:functional_coverage",
      "name": "沟通 C-MDM 价值与当前用途",
      "attributes": {
        "reference_id": "G21B-T5-3-22",
        "reference_kind": "business_function",
        "reference_name": "沟通 C-MDM 价值与当前用途",
        "reference_definition": "就用 KPI 沟通 C-MDM 能力的价值（降低成本/复杂度、带来的定性/定量收益、客户数据使用者的满意度评分等）。",
        "reference_group": "E. 沟通（Communication）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L611",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-23",
      "type": "ops:functional_coverage",
      "name": "沟通客户数据团队服务目录",
      "attributes": {
        "reference_id": "G21B-T5-3-23",
        "reference_kind": "business_function",
        "reference_name": "沟通客户数据团队服务目录",
        "reference_definition": "向这些服务的潜在内部用户沟通客户数据团队的服务目录。",
        "reference_group": "E. 沟通（Communication）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L612",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-24",
      "type": "ops:functional_coverage",
      "name": "沟通客户数据质量",
      "attributes": {
        "reference_id": "G21B-T5-3-24",
        "reference_kind": "business_function",
        "reference_name": "沟通客户数据质量",
        "reference_definition": "向运营或高层利益相关者沟通质量仪表盘。",
        "reference_group": "E. 沟通（Communication）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L613",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-25",
      "type": "ops:functional_coverage",
      "name": "构建并交付客户数据质量与演进的报告",
      "attributes": {
        "reference_id": "G21B-T5-3-25",
        "reference_kind": "business_function",
        "reference_name": "构建并交付客户数据质量与演进的报告",
        "reference_definition": "与高管、业务方、业务数据所有者及数据管家共同设计质量仪表盘，并按他们的要求实现质量仪表盘。",
        "reference_group": "F. 数据质量与业务价值度量（Data Quality and Business Value Measurement）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L619",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-26",
      "type": "ops:functional_coverage",
      "name": "报告 C-MDM 业务价值",
      "attributes": {
        "reference_id": "G21B-T5-3-26",
        "reference_kind": "business_function",
        "reference_name": "报告 C-MDM 业务价值",
        "reference_definition": "与业务方（包括 IT 团队）共同识别并实施相关的 KPI。",
        "reference_group": "F. 数据质量与业务价值度量（Data Quality and Business Value Measurement）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L620",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-27",
      "type": "ops:functional_coverage",
      "name": "分析数据市场并识别机会",
      "attributes": {
        "reference_id": "G21B-T5-3-27",
        "reference_kind": "business_function",
        "reference_name": "分析数据市场并识别机会",
        "reference_definition": "分析围绕提供参与方/联系人数据的市场（潜在伙伴或数据供应商）；管理并转化这些机会，以发展改进客户数据质量的新方式。",
        "reference_group": "G. 外部客户数据获取（External Customer Data Acquisition）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L626",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-28",
      "type": "ops:functional_coverage",
      "name": "建立数据伙伴关系",
      "attributes": {
        "reference_id": "G21B-T5-3-28",
        "reference_kind": "business_function",
        "reference_name": "建立数据伙伴关系",
        "reference_definition": "建立伙伴关系，或将现有伙伴关系扩展到某种数据交换，以借助这些外部数据源改进数据质量；随时间在运营层面管理数据伙伴关系。",
        "reference_group": "G. 外部客户数据获取（External Customer Data Acquisition）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L627",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-B-G21B-T5-3-29",
      "type": "ops:functional_coverage",
      "name": "采购外部客户数据",
      "attributes": {
        "reference_id": "G21B-T5-3-29",
        "reference_kind": "business_function",
        "reference_name": "采购外部客户数据",
        "reference_definition": "统一管理联系人/参与方数据的采购，并把此外部数据集成到客户数据管理流程中。",
        "reference_group": "G. 外部客户数据获取（External Customer Data Acquisition）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-3 L628",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "out-of-scope-with-reason",
        "implementation_ref": "none",
        "evidence_detail": "试点仅合法自有客户记录，没有已批准外部数据用例",
        "gap_action": "若引入外部数据重新评估采购、用途和质量责任",
        "source_uncertainty": "英语原版/原图未在本例复核；只据本地正文表"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    }
  ],
  "relationships": [],
  "extensions": {
    "relationship_types": {}
  },
  "states": [],
  "view": {
    "id": "v-mdm-business-function-coverage",
    "artifact_id": "customer-mdm-model",
    "profile_id": "mdm-business-function-coverage",
    "title": "C-MDM业务功能参考覆盖",
    "context": {
      "domains": [
        "business",
        "data",
        "application",
        "technology"
      ],
      "landscape": "capability",
      "purpose": "project",
      "abstraction": "logical",
      "evolution": "target"
    },
    "entity_ids": [
      "MDMC-B-G21B-T5-3-01",
      "MDMC-B-G21B-T5-3-02",
      "MDMC-B-G21B-T5-3-03",
      "MDMC-B-G21B-T5-3-04",
      "MDMC-B-G21B-T5-3-05",
      "MDMC-B-G21B-T5-3-06",
      "MDMC-B-G21B-T5-3-07",
      "MDMC-B-G21B-T5-3-08",
      "MDMC-B-G21B-T5-3-09",
      "MDMC-B-G21B-T5-3-10",
      "MDMC-B-G21B-T5-3-11",
      "MDMC-B-G21B-T5-3-12",
      "MDMC-B-G21B-T5-3-13",
      "MDMC-B-G21B-T5-3-14",
      "MDMC-B-G21B-T5-3-15",
      "MDMC-B-G21B-T5-3-16",
      "MDMC-B-G21B-T5-3-17",
      "MDMC-B-G21B-T5-3-18",
      "MDMC-B-G21B-T5-3-19",
      "MDMC-B-G21B-T5-3-20",
      "MDMC-B-G21B-T5-3-21",
      "MDMC-B-G21B-T5-3-22",
      "MDMC-B-G21B-T5-3-23",
      "MDMC-B-G21B-T5-3-24",
      "MDMC-B-G21B-T5-3-25",
      "MDMC-B-G21B-T5-3-26",
      "MDMC-B-G21B-T5-3-27",
      "MDMC-B-G21B-T5-3-28",
      "MDMC-B-G21B-T5-3-29"
    ],
    "relationship_ids": [],
    "analysis": "依据raw-brief.md的虚构材料，按analysis.md人工分析；生成器转换已审查模型。",
    "legend": "参考功能行不是实际部署；计划和未知不计已实现。本表不声明来源图视觉通过。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile mdm-business-function-coverage --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile mdm-business-function-coverage --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
