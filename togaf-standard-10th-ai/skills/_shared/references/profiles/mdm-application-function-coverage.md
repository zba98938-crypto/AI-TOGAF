# C-MDM应用功能参考覆盖

`profile_id`: mdm-application-function-coverage；`artifact_id`: customer-mdm-model；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G21B §5.2.2表5-4。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-operations-1。

{
  "id": "mdm-application-function-coverage",
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
  "raw_input": "examples/addenda/operations/mdm-application-function-coverage/raw-brief.md",
  "analysis_path": "examples/addenda/operations/mdm-application-function-coverage/analysis.md",
  "sources": [
    {
      "id": "case-source",
      "kind": "example",
      "description": "海岚没有C-MDM功能运行证据；管家提出取消合并需求，但还未演练。38应用功能均为参考条目。推送事件第三操作有本地“定义”与图标签Delete冲突，不能据此直接承诺删除传播或修写原材料。",
      "locator": "raw-brief.md"
    }
  ],
  "entities": [
    {
      "id": "MDMC-A-G21B-T5-4-01",
      "type": "ops:functional_coverage",
      "name": "创建主数据（Create Master Data）",
      "attributes": {
        "reference_id": "G21B-T5-4-01",
        "reference_kind": "application_function",
        "reference_name": "创建主数据（Create Master Data）",
        "reference_definition": "创建新的客户主记录，并分配唯一的内部组织键。",
        "reference_group": "A. 采集——用户界面或服务（Acquisition – User Interface or Services）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L677",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-02",
      "type": "ops:functional_coverage",
      "name": "更新主数据（Update Master Data）",
      "attributes": {
        "reference_id": "G21B-T5-4-02",
        "reference_kind": "application_function",
        "reference_name": "更新主数据（Update Master Data）",
        "reference_definition": "更新已有的客户主记录。",
        "reference_group": "A. 采集——用户界面或服务（Acquisition – User Interface or Services）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L678",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-03",
      "type": "ops:functional_coverage",
      "name": "管理主实体与其他业务对象之间的链接（Manage Links between Master Entities and Other Business Objects）",
      "attributes": {
        "reference_id": "G21B-T5-4-03",
        "reference_kind": "application_function",
        "reference_name": "管理主实体与其他业务对象之间的链接（Manage Links between Master Entities and Other Business Objects）",
        "reference_definition": "创建、更新和删除参与方之间的链接，以及参与方与其他对象（如合同、报价中的角色等）之间的链接——这些对象在 C-MDM 中作为副本管理。删除操作必须谨慎执行，以免破坏完整性或产生孤立记录。",
        "reference_group": "A. 采集——用户界面或服务（Acquisition – User Interface or Services）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L679",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-04",
      "type": "ops:functional_coverage",
      "name": "导入数据集/批量采集（Import Data Set, Mass Acquisition）",
      "attributes": {
        "reference_id": "G21B-T5-4-04",
        "reference_kind": "application_function",
        "reference_name": "导入数据集/批量采集（Import Data Set, Mass Acquisition）",
        "reference_definition": "对多个参与方进行数据采集（计划批处理集成，或通过用户界面人工采集等）。",
        "reference_group": "A. 采集——用户界面或服务（Acquisition – User Interface or Services）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L680",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-05",
      "type": "ops:functional_coverage",
      "name": "以技术与业务元数据增强数据（尤其是数据血缘）（Enhance Data with Technical and Business Metadata）",
      "attributes": {
        "reference_id": "G21B-T5-4-05",
        "reference_kind": "application_function",
        "reference_name": "以技术与业务元数据增强数据（尤其是数据血缘）（Enhance Data with Technical and Business Metadata）",
        "reference_definition": "数据集成时管理元数据，如客户数据实例的版本、更新/创建的来源、最后更新日期。",
        "reference_group": "A. 采集——用户界面或服务（Acquisition – User Interface or Services）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L681",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-06",
      "type": "ops:functional_coverage",
      "name": "管理业务校验与工作流（Manage Business Validation and Workflows）",
      "attributes": {
        "reference_id": "G21B-T5-4-06",
        "reference_kind": "application_function",
        "reference_name": "管理业务校验与工作流（Manage Business Validation and Workflows）",
        "reference_definition": "在相关时提供支持主数据校验流程的功能。",
        "reference_group": "B. 质量管理（Quality Management）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L687",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-07",
      "type": "ops:functional_coverage",
      "name": "管理与应用属性值质量规则（Manage & Apply Attribute Value Quality Rules）",
      "attributes": {
        "reference_id": "G21B-T5-4-07",
        "reference_kind": "application_function",
        "reference_name": "管理与应用属性值质量规则（Manage & Apply Attribute Value Quality Rules）",
        "reference_definition": "增加、更新和删除属性值规则，以确保质量，并发现格式、一致性与业务问题。",
        "reference_group": "B. 质量管理（Quality Management）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L688",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-08",
      "type": "ops:functional_coverage",
      "name": "管理语法、格式与规范化规则（Manage Syntax, Format, Normalization Rules）",
      "attributes": {
        "reference_id": "G21B-T5-4-08",
        "reference_kind": "application_function",
        "reference_name": "管理语法、格式与规范化规则（Manage Syntax, Format, Normalization Rules）",
        "reference_definition": "管理格式校验，并设置规范化规则（如基于规范化代码/类别列表）或标准化规则（基于标准格式）。",
        "reference_group": "B. 质量管理（Quality Management）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L689",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-09",
      "type": "ops:functional_coverage",
      "name": "管理一致性与业务规则（Manage Consistency and Business Rules）",
      "attributes": {
        "reference_id": "G21B-T5-4-09",
        "reference_kind": "application_function",
        "reference_name": "管理一致性与业务规则（Manage Consistency and Business Rules）",
        "reference_definition": "管理一致性规则（如两个属性值之间的一致性）与业务规则。",
        "reference_group": "B. 质量管理（Quality Management）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L690",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-10",
      "type": "ops:functional_coverage",
      "name": "管理准确性（Manage Accuracy）",
      "attributes": {
        "reference_id": "G21B-T5-4-10",
        "reference_kind": "application_function",
        "reference_name": "管理准确性（Manage Accuracy）",
        "reference_definition": "管理准确性水平/置信度评分（如基于与外部数据源的比较）。",
        "reference_group": "B. 质量管理（Quality Management）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L691",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-11",
      "type": "ops:functional_coverage",
      "name": "管理唯一性规则（Manage Uniqueness Rules）",
      "attributes": {
        "reference_id": "G21B-T5-4-11",
        "reference_kind": "application_function",
        "reference_name": "管理唯一性规则（Manage Uniqueness Rules）",
        "reference_definition": "用于检测重复、并提出最佳去重方式的一组功能。",
        "reference_group": "B. 质量管理（Quality Management）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L692",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-12",
      "type": "ops:functional_coverage",
      "name": "确定性流程去重（De-duplicate with Determinist Process）",
      "attributes": {
        "reference_id": "G21B-T5-4-12",
        "reference_kind": "application_function",
        "reference_name": "确定性流程去重（De-duplicate with Determinist Process）",
        "reference_definition": "通过设计好的、带规则的自动化工作流去重。",
        "reference_group": "B. 质量管理（Quality Management）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L693",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-13",
      "type": "ops:functional_coverage",
      "name": "概率/统计流程去重（De-duplicate with Probabilist/Statistic Process）",
      "attributes": {
        "reference_id": "G21B-T5-4-13",
        "reference_kind": "application_function",
        "reference_name": "概率/统计流程去重（De-duplicate with Probabilist/Statistic Process）",
        "reference_definition": "基于纯统计比较去重。",
        "reference_group": "B. 质量管理（Quality Management）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L694",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-14",
      "type": "ops:functional_coverage",
      "name": "推荐合并以供仲裁（匹配）（Recommend Merges to Arbitrate）",
      "attributes": {
        "reference_id": "G21B-T5-4-14",
        "reference_kind": "application_function",
        "reference_name": "推荐合并以供仲裁（匹配）（Recommend Merges to Arbitrate）",
        "reference_definition": "基于确定性或统计流程，系统推荐潜在的合并供仲裁（非 100% 置信）。",
        "reference_group": "B. 质量管理（Quality Management）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L695",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-15",
      "type": "ops:functional_coverage",
      "name": "人工合并仲裁（Manual Merge Arbitrage）",
      "attributes": {
        "reference_id": "G21B-T5-4-15",
        "reference_kind": "application_function",
        "reference_name": "人工合并仲裁（Manual Merge Arbitrage）",
        "reference_definition": "合并决定由授权人员通过用户界面确认。",
        "reference_group": "B. 质量管理（Quality Management）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L696",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-16",
      "type": "ops:functional_coverage",
      "name": "取消合并（Unmerge）",
      "attributes": {
        "reference_id": "G21B-T5-4-16",
        "reference_kind": "application_function",
        "reference_name": "取消合并（Unmerge）",
        "reference_definition": "支持人工取消合并。",
        "reference_group": "B. 质量管理（Quality Management）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L697",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "planned",
        "implementation_ref": "UNMERGE-proposal",
        "evidence_detail": "虚构管家提出取消合并需求，尚无系统演练",
        "gap_action": "在允许实际合并前验证原值/键映射和消费者恢复",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-17",
      "type": "ops:functional_coverage",
      "name": "生成唯一主数据技术键（Generate Unique Master Technical Key）",
      "attributes": {
        "reference_id": "G21B-T5-4-17",
        "reference_kind": "application_function",
        "reference_name": "生成唯一主数据技术键（Generate Unique Master Technical Key）",
        "reference_definition": "管理唯一技术键的分配。",
        "reference_group": "B. 质量管理（Quality Management）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L698",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-18",
      "type": "ops:functional_coverage",
      "name": "人工删除（Manual Deletion）",
      "attributes": {
        "reference_id": "G21B-T5-4-18",
        "reference_kind": "application_function",
        "reference_name": "人工删除（Manual Deletion）",
        "reference_definition": "人工搜索并删除数据（该功能的可访问性应受到严格限制）。",
        "reference_group": "C. 数据隐私管理（Data Privacy Management）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L704",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-19",
      "type": "ops:functional_coverage",
      "name": "按规则自动删除（Automated Deletion with Rules）",
      "attributes": {
        "reference_id": "G21B-T5-4-19",
        "reference_kind": "application_function",
        "reference_name": "按规则自动删除（Automated Deletion with Rules）",
        "reference_definition": "基于既定规则自动删除，或提出删除建议。",
        "reference_group": "C. 数据隐私管理（Data Privacy Management）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L705",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-20",
      "type": "ops:functional_coverage",
      "name": "掩码（Masking）",
      "attributes": {
        "reference_id": "G21B-T5-4-20",
        "reference_kind": "application_function",
        "reference_name": "掩码（Masking）",
        "reference_definition": "按隐私要求对数据作掩码处理。",
        "reference_group": "C. 数据隐私管理（Data Privacy Management）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L706",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-21",
      "type": "ops:functional_coverage",
      "name": "搜索（Search）",
      "attributes": {
        "reference_id": "G21B-T5-4-21",
        "reference_kind": "application_function",
        "reference_name": "搜索（Search）",
        "reference_definition": "按不同条件搜索个人。条件可基于属性（如业务键、名、姓、联系方式等），也可基于相关对象属性（如保单号、理赔号等）。",
        "reference_group": "D. 分发——用户界面或服务（Distribution – User Interface or Service）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L712",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-22",
      "type": "ops:functional_coverage",
      "name": "读取数据（Read Data）",
      "attributes": {
        "reference_id": "G21B-T5-4-22",
        "reference_kind": "application_function",
        "reference_name": "读取数据（Read Data）",
        "reference_definition": "读取给定个人的数据值。",
        "reference_group": "D. 分发——用户界面或服务（Distribution – User Interface or Service）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L713",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-23",
      "type": "ops:functional_coverage",
      "name": "提取数据（Extract Data）",
      "attributes": {
        "reference_id": "G21B-T5-4-23",
        "reference_kind": "application_function",
        "reference_name": "提取数据（Extract Data）",
        "reference_definition": "按批或人工提取某一范围个人的数据值（如基于筛选条件）。",
        "reference_group": "D. 分发——用户界面或服务（Distribution – User Interface or Service）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L714",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-24",
      "type": "ops:functional_coverage",
      "name": "推送事件（创建、更新、定义、合并）（Push Events）",
      "attributes": {
        "reference_id": "G21B-T5-4-24",
        "reference_kind": "application_function",
        "reference_name": "推送事件（创建、更新、定义、合并）（Push Events）",
        "reference_definition": "推送数据演进事件，并配置事件向相关消费方的分发（如让目标系统在本地更新数据，或在运营流程中生成待处理告警）。",
        "reference_group": "D. 分发——用户界面或服务（Distribution – User Interface or Service）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L715",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "本地表事件项写定义，图标签写Delete",
        "gap_action": "保留冲突，核实英文后决定项目事件契约",
        "source_uncertainty": "本地表写创建/更新/定义/合并，但图内对照写Create/Update/Delete/Merge；事件第三操作待英文核实"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-25",
      "type": "ops:functional_coverage",
      "name": "按情境设定数据可见性与提供值（Contextualize Data Visibility & Provided Values）",
      "attributes": {
        "reference_id": "G21B-T5-4-25",
        "reference_kind": "application_function",
        "reference_name": "按情境设定数据可见性与提供值（Contextualize Data Visibility & Provided Values）",
        "reference_definition": "为每个画像/角色配置数据可见性规则；并按消费方对所给值作情境化处理（如多语言环境下对消费主数据的管理）。",
        "reference_group": "D. 分发——用户界面或服务（Distribution – User Interface or Service）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L716",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-26",
      "type": "ops:functional_coverage",
      "name": "设计主数据模型（Design Master Data Model）",
      "attributes": {
        "reference_id": "G21B-T5-4-26",
        "reference_kind": "application_function",
        "reference_name": "设计主数据模型（Design Master Data Model）",
        "reference_definition": "提供工具管理数据模型的物理设计，以满足 C-MDM 要求。",
        "reference_group": "E. 管理（Administration）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L722",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-27",
      "type": "ops:functional_coverage",
      "name": "管理数据历史化与版本规则（Manage Data Historization and Versioning Rules）",
      "attributes": {
        "reference_id": "G21B-T5-4-27",
        "reference_kind": "application_function",
        "reference_name": "管理数据历史化与版本规则（Manage Data Historization and Versioning Rules）",
        "reference_definition": "配置数据历史化的方式，管理主数据的版本，并在相关时清除旧数据。",
        "reference_group": "E. 管理（Administration）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L723",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-28",
      "type": "ops:functional_coverage",
      "name": "全库版本化（Full Database Versioning）",
      "attributes": {
        "reference_id": "G21B-T5-4-28",
        "reference_kind": "application_function",
        "reference_name": "全库版本化（Full Database Versioning）",
        "reference_definition": "对整个数据库（结构与内容）做版本化，并对版本作历史化。",
        "reference_group": "E. 管理（Administration）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L724",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-29",
      "type": "ops:functional_coverage",
      "name": "管理角色（Manage Roles）",
      "attributes": {
        "reference_id": "G21B-T5-4-29",
        "reference_kind": "application_function",
        "reference_name": "管理角色（Manage Roles）",
        "reference_definition": "配置用户（人或系统）的角色。",
        "reference_group": "E. 管理（Administration）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L725",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-30",
      "type": "ops:functional_coverage",
      "name": "管理访问权限（Manage Access Rights）",
      "attributes": {
        "reference_id": "G21B-T5-4-30",
        "reference_kind": "application_function",
        "reference_name": "管理访问权限（Manage Access Rights）",
        "reference_definition": "管理并应用对数据和对操作（创建、更新、合并等）的访问权限。",
        "reference_group": "E. 管理（Administration）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L726",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-31",
      "type": "ops:functional_coverage",
      "name": "管理日志（Manage Logging）",
      "attributes": {
        "reference_id": "G21B-T5-4-31",
        "reference_kind": "application_function",
        "reference_name": "管理日志（Manage Logging）",
        "reference_definition": "管理 C-MDM 系统记录各类事件的方式。",
        "reference_group": "E. 管理（Administration）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L727",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-32",
      "type": "ops:functional_coverage",
      "name": "生成审计数据演进报表（Generate Audit Data Evolution Reports）",
      "attributes": {
        "reference_id": "G21B-T5-4-32",
        "reference_kind": "application_function",
        "reference_name": "生成审计数据演进报表（Generate Audit Data Evolution Reports）",
        "reference_definition": "生成报表，以便在给定人员范围与时间范围内清晰理解数据演进（如按数据生产系统、按角色、按人员给出的指标等）。",
        "reference_group": "F. 仪表盘与报表（Dashboards & Reports）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L733",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-33",
      "type": "ops:functional_coverage",
      "name": "生成数据质量仪表盘（Generate Data Quality Dashboards）",
      "attributes": {
        "reference_id": "G21B-T5-4-33",
        "reference_kind": "application_function",
        "reference_name": "生成数据质量仪表盘（Generate Data Quality Dashboards）",
        "reference_definition": "生成关于当前质量及数据质量演进（完整性、准确性等）的仪表盘。",
        "reference_group": "F. 仪表盘与报表（Dashboards & Reports）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L734",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-34",
      "type": "ops:functional_coverage",
      "name": "生成使用情况仪表盘（Generate Usages Dashboard）",
      "attributes": {
        "reference_id": "G21B-T5-4-34",
        "reference_kind": "application_function",
        "reference_name": "生成使用情况仪表盘（Generate Usages Dashboard）",
        "reference_definition": "生成仪表盘以了解 C-MDM 的使用方式（如使用频率、分发出去的更新事件数量等）。",
        "reference_group": "F. 仪表盘与报表（Dashboards & Reports）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L735",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-35",
      "type": "ops:functional_coverage",
      "name": "输入属性转码（Input Attributes Transcoding）",
      "attributes": {
        "reference_id": "G21B-T5-4-35",
        "reference_kind": "application_function",
        "reference_name": "输入属性转码（Input Attributes Transcoding）",
        "reference_definition": "管理从输入属性值到标准化 MDM 值的转码规则。",
        "reference_group": "G. 参考数据管理（Reference Data Management）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L741",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-36",
      "type": "ops:functional_coverage",
      "name": "管理参考列表（Manage Reference List）",
      "attributes": {
        "reference_id": "G21B-T5-4-36",
        "reference_kind": "application_function",
        "reference_name": "管理参考列表（Manage Reference List）",
        "reference_definition": "管理参考规范化列表（如国家列表、状态列表等）。",
        "reference_group": "G. 参考数据管理（Reference Data Management）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L742",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-37",
      "type": "ops:functional_coverage",
      "name": "管理客户键映射（Manage Customer Key Mapping）",
      "attributes": {
        "reference_id": "G21B-T5-4-37",
        "reference_kind": "application_function",
        "reference_name": "管理客户键映射（Manage Customer Key Mapping）",
        "reference_definition": "管理键之间的映射（如运营应用客户 ID 与主客户 ID 的映射）。",
        "reference_group": "G. 参考数据管理（Reference Data Management）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L743",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MDMC-A-G21B-T5-4-38",
      "type": "ops:functional_coverage",
      "name": "输出属性转码（Output Attributes Transcoding）",
      "attributes": {
        "reference_id": "G21B-T5-4-38",
        "reference_kind": "application_function",
        "reference_name": "输出属性转码（Output Attributes Transcoding）",
        "reference_definition": "管理从标准化 MDM 属性值到消费应用属性值的转码规则。",
        "reference_group": "G. 参考数据管理（Reference Data Management）",
        "reference_level": "child-in-source-group",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G21B 表5-4 L744",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "原始访谈未覆盖此项；不存在实现证据",
        "gap_action": "访谈负责团队并获取实际范围和运行证据",
        "source_uncertainty": "none"
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
    "id": "v-mdm-application-function-coverage",
    "artifact_id": "customer-mdm-model",
    "profile_id": "mdm-application-function-coverage",
    "title": "C-MDM应用功能参考覆盖",
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
      "MDMC-A-G21B-T5-4-01",
      "MDMC-A-G21B-T5-4-02",
      "MDMC-A-G21B-T5-4-03",
      "MDMC-A-G21B-T5-4-04",
      "MDMC-A-G21B-T5-4-05",
      "MDMC-A-G21B-T5-4-06",
      "MDMC-A-G21B-T5-4-07",
      "MDMC-A-G21B-T5-4-08",
      "MDMC-A-G21B-T5-4-09",
      "MDMC-A-G21B-T5-4-10",
      "MDMC-A-G21B-T5-4-11",
      "MDMC-A-G21B-T5-4-12",
      "MDMC-A-G21B-T5-4-13",
      "MDMC-A-G21B-T5-4-14",
      "MDMC-A-G21B-T5-4-15",
      "MDMC-A-G21B-T5-4-16",
      "MDMC-A-G21B-T5-4-17",
      "MDMC-A-G21B-T5-4-18",
      "MDMC-A-G21B-T5-4-19",
      "MDMC-A-G21B-T5-4-20",
      "MDMC-A-G21B-T5-4-21",
      "MDMC-A-G21B-T5-4-22",
      "MDMC-A-G21B-T5-4-23",
      "MDMC-A-G21B-T5-4-24",
      "MDMC-A-G21B-T5-4-25",
      "MDMC-A-G21B-T5-4-26",
      "MDMC-A-G21B-T5-4-27",
      "MDMC-A-G21B-T5-4-28",
      "MDMC-A-G21B-T5-4-29",
      "MDMC-A-G21B-T5-4-30",
      "MDMC-A-G21B-T5-4-31",
      "MDMC-A-G21B-T5-4-32",
      "MDMC-A-G21B-T5-4-33",
      "MDMC-A-G21B-T5-4-34",
      "MDMC-A-G21B-T5-4-35",
      "MDMC-A-G21B-T5-4-36",
      "MDMC-A-G21B-T5-4-37",
      "MDMC-A-G21B-T5-4-38"
    ],
    "relationship_ids": [],
    "analysis": "依据raw-brief.md的虚构材料，按analysis.md人工分析；生成器转换已审查模型。",
    "legend": "参考功能行不是实际部署；计划和未知不计已实现。本表不声明来源图视觉通过。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile mdm-application-function-coverage --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile mdm-application-function-coverage --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
