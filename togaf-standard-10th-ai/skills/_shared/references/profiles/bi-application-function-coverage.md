# BI应用功能参考覆盖

`profile_id`: bi-application-function-coverage；`artifact_id`: bi-requirements-profile；主责：[togaf-requirements](../../../togaf-requirements/SKILL.md)。

来源：G238 §2.3、表4-3、§4.4。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-operations-1。

{
  "id": "bi-application-function-coverage",
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
  "raw_input": "examples/addenda/operations/bi-application-function-coverage/raw-brief.md",
  "analysis_path": "examples/addenda/operations/bi-application-function-coverage/analysis.md",
  "sources": [
    {
      "id": "case-source",
      "kind": "example",
      "description": "海岚提供每晚库存文件批交换RUN-11，未提供端到端秒级测量。没有完整供应商功能证据。用59参考子功能逐行评估；只给批交换本用例证据，其余未知。详细表10组与高层9组粒度不同。",
      "locator": "raw-brief.md"
    }
  ],
  "entities": [
    {
      "id": "BIC-A-G238-T4-3-01",
      "type": "ops:functional_coverage",
      "name": "资源管理",
      "attributes": {
        "reference_id": "G238-T4-3-01",
        "reference_kind": "application_function",
        "reference_name": "资源管理",
        "reference_definition": "BI 与分析的资源管理。",
        "reference_group": "管理",
        "reference_level": "child-in-source-group",
        "reference_scope": "（支撑 BI 与分析能力所需的管理任务，如访问管理、数据处理调度等；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L567",
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
      "id": "BIC-A-G238-T4-3-02",
      "type": "ops:functional_coverage",
      "name": "访问管理",
      "attributes": {
        "reference_id": "G238-T4-3-02",
        "reference_kind": "application_function",
        "reference_name": "访问管理",
        "reference_definition": "身份与访问管理，主要包括面向用户与管理员的认证与授权服务。",
        "reference_group": "管理",
        "reference_level": "child-in-source-group",
        "reference_scope": "（支撑 BI 与分析能力所需的管理任务，如访问管理、数据处理调度等；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L568",
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
      "id": "BIC-A-G238-T4-3-03",
      "type": "ops:functional_coverage",
      "name": "调度",
      "attributes": {
        "reference_id": "G238-T4-3-03",
        "reference_kind": "application_function",
        "reference_name": "调度",
        "reference_definition": "作业调度器管理。",
        "reference_group": "管理",
        "reference_level": "child-in-source-group",
        "reference_scope": "（支撑 BI 与分析能力所需的管理任务，如访问管理、数据处理调度等；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L569",
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
      "id": "BIC-A-G238-T4-3-04",
      "type": "ops:functional_coverage",
      "name": "服务恢复",
      "attributes": {
        "reference_id": "G238-T4-3-04",
        "reference_kind": "application_function",
        "reference_name": "服务恢复",
        "reference_definition": "灾难后服务恢复。",
        "reference_group": "管理",
        "reference_level": "child-in-source-group",
        "reference_scope": "（支撑 BI 与分析能力所需的管理任务，如访问管理、数据处理调度等；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L570",
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
      "id": "BIC-A-G238-T4-3-05",
      "type": "ops:functional_coverage",
      "name": "实验与生产环境管理",
      "attributes": {
        "reference_id": "G238-T4-3-05",
        "reference_kind": "application_function",
        "reference_name": "实验与生产环境管理",
        "reference_definition": "管理生产、测试、开发等不同环境。",
        "reference_group": "管理",
        "reference_level": "child-in-source-group",
        "reference_scope": "（支撑 BI 与分析能力所需的管理任务，如访问管理、数据处理调度等；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L571",
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
      "id": "BIC-A-G238-T4-3-06",
      "type": "ops:functional_coverage",
      "name": "搜索数据访问",
      "attributes": {
        "reference_id": "G238-T4-3-06",
        "reference_kind": "application_function",
        "reference_name": "搜索数据访问",
        "reference_definition": "通过搜索引擎直接在 BI 与分析存储上搜索数据。",
        "reference_group": "面向工程与数据管理的数据访问",
        "reference_level": "child-in-source-group",
        "reference_scope": "（为高级数据管家、数据工程师、数据科学家、数据管理员等提供对 BI 与分析数据的直接访问；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L572",
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
      "id": "BIC-A-G238-T4-3-07",
      "type": "ops:functional_coverage",
      "name": "数据可视化",
      "attributes": {
        "reference_id": "G238-T4-3-07",
        "reference_kind": "application_function",
        "reference_name": "数据可视化",
        "reference_definition": "直接在 BI 与分析存储上可视化数据。",
        "reference_group": "面向工程与数据管理的数据访问",
        "reference_level": "child-in-source-group",
        "reference_scope": "（为高级数据管家、数据工程师、数据科学家、数据管理员等提供对 BI 与分析数据的直接访问；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L573",
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
      "id": "BIC-A-G238-T4-3-08",
      "type": "ops:functional_coverage",
      "name": "SQL 数据访问",
      "attributes": {
        "reference_id": "G238-T4-3-08",
        "reference_kind": "application_function",
        "reference_name": "SQL 数据访问",
        "reference_definition": "直接在 BI 与分析存储上执行结构化查询语言（SQL）查询。",
        "reference_group": "面向工程与数据管理的数据访问",
        "reference_level": "child-in-source-group",
        "reference_scope": "（为高级数据管家、数据工程师、数据科学家、数据管理员等提供对 BI 与分析数据的直接访问；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L574",
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
      "id": "BIC-A-G238-T4-3-09",
      "type": "ops:functional_coverage",
      "name": "元数据探索",
      "attributes": {
        "reference_id": "G238-T4-3-09",
        "reference_kind": "application_function",
        "reference_name": "元数据探索",
        "reference_definition": "探索 BI 与分析的元数据。",
        "reference_group": "面向工程与数据管理的数据访问",
        "reference_level": "child-in-source-group",
        "reference_scope": "（为高级数据管家、数据工程师、数据科学家、数据管理员等提供对 BI 与分析数据的直接访问；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L575",
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
      "id": "BIC-A-G238-T4-3-10",
      "type": "ops:functional_coverage",
      "name": "集成开发环境（IDE）开发",
      "attributes": {
        "reference_id": "G238-T4-3-10",
        "reference_kind": "application_function",
        "reference_name": "集成开发环境（IDE）开发",
        "reference_definition": "面向数据工程师或数据科学家的 IDE。",
        "reference_group": "数据工程与数据科学开发",
        "reference_level": "child-in-source-group",
        "reference_scope": "（适用于开发者工作站的能力）",
        "source_locator": "G238 表4-3 L576",
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
      "id": "BIC-A-G238-T4-3-11",
      "type": "ops:functional_coverage",
      "name": "数据整理与数据发现工具",
      "attributes": {
        "reference_id": "G238-T4-3-11",
        "reference_kind": "application_function",
        "reference_name": "数据整理与数据发现工具",
        "reference_definition": "面向数据工程师或数据科学家的数据准备工具。",
        "reference_group": "数据工程与数据科学开发",
        "reference_level": "child-in-source-group",
        "reference_scope": "（适用于开发者工作站的能力）",
        "source_locator": "G238 表4-3 L577",
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
      "id": "BIC-A-G238-T4-3-12",
      "type": "ops:functional_coverage",
      "name": "交互式类 Notebook 开发",
      "attributes": {
        "reference_id": "G238-T4-3-12",
        "reference_kind": "application_function",
        "reference_name": "交互式类 Notebook 开发",
        "reference_definition": "面向数据科学家、数据工程师的 Notebook 环境（用于早期探索阶段的数据分析、算法比较），以及数据的图形化呈现。",
        "reference_group": "数据工程与数据科学开发",
        "reference_level": "child-in-source-group",
        "reference_scope": "（适用于开发者工作站的能力）",
        "source_locator": "G238 表4-3 L578",
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
      "id": "BIC-A-G238-T4-3-13",
      "type": "ops:functional_coverage",
      "name": "统计与机器学习工具",
      "attributes": {
        "reference_id": "G238-T4-3-13",
        "reference_kind": "application_function",
        "reference_name": "统计与机器学习工具",
        "reference_definition": "面向数据科学家与数据工程师的统计与机器学习工具。",
        "reference_group": "数据工程与数据科学开发",
        "reference_level": "child-in-source-group",
        "reference_scope": "（适用于开发者工作站的能力）",
        "source_locator": "G238 表4-3 L579",
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
      "id": "BIC-A-G238-T4-3-14",
      "type": "ops:functional_coverage",
      "name": "源代码管理",
      "attributes": {
        "reference_id": "G238-T4-3-14",
        "reference_kind": "application_function",
        "reference_name": "源代码管理",
        "reference_definition": "为开发者或数据科学家提供开发代码（主干）与发布（分支）的版本管理。",
        "reference_group": "集成与部署",
        "reference_level": "child-in-source-group",
        "reference_scope": "（持续交付链，包括版本管理、部署、打包等）",
        "source_locator": "G238 表4-3 L580",
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
      "id": "BIC-A-G238-T4-3-15",
      "type": "ops:functional_coverage",
      "name": "分析模型管理",
      "attributes": {
        "reference_id": "G238-T4-3-15",
        "reference_kind": "application_function",
        "reference_name": "分析模型管理",
        "reference_definition": "管理高级分析模型（如机器学习模型）端到端生命周期的功能。",
        "reference_group": "集成与部署",
        "reference_level": "child-in-source-group",
        "reference_scope": "（持续交付链，包括版本管理、部署、打包等）",
        "source_locator": "G238 表4-3 L581",
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
      "id": "BIC-A-G238-T4-3-16",
      "type": "ops:functional_coverage",
      "name": "测试",
      "attributes": {
        "reference_id": "G238-T4-3-16",
        "reference_kind": "application_function",
        "reference_name": "测试",
        "reference_definition": "对新代码发布执行测试（非回归）。",
        "reference_group": "集成与部署",
        "reference_level": "child-in-source-group",
        "reference_scope": "（持续交付链，包括版本管理、部署、打包等）",
        "source_locator": "G238 表4-3 L582",
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
      "id": "BIC-A-G238-T4-3-17",
      "type": "ops:functional_coverage",
      "name": "构建管理",
      "attributes": {
        "reference_id": "G238-T4-3-17",
        "reference_kind": "application_function",
        "reference_name": "构建管理",
        "reference_definition": "准备待部署包：运行测试并生成二进制文件。",
        "reference_group": "集成与部署",
        "reference_level": "child-in-source-group",
        "reference_scope": "（持续交付链，包括版本管理、部署、打包等）",
        "source_locator": "G238 表4-3 L583",
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
      "id": "BIC-A-G238-T4-3-18",
      "type": "ops:functional_coverage",
      "name": "部署",
      "attributes": {
        "reference_id": "G238-T4-3-18",
        "reference_kind": "application_function",
        "reference_name": "部署",
        "reference_definition": "在给定环境（开发、集成、预生产、生产）部署包（新软件发布）。",
        "reference_group": "集成与部署",
        "reference_level": "child-in-source-group",
        "reference_scope": "（持续交付链，包括版本管理、部署、打包等）",
        "source_locator": "G238 表4-3 L584",
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
      "id": "BIC-A-G238-T4-3-19",
      "type": "ops:functional_coverage",
      "name": "元数据交换",
      "attributes": {
        "reference_id": "G238-T4-3-19",
        "reference_kind": "application_function",
        "reference_name": "元数据交换",
        "reference_definition": "并行进行元数据的摄取与分发。",
        "reference_group": "数据集成",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许在整个架构全景中实现集成与 BI 分析，包括批处理、流式、接口等；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L585",
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
      "id": "BIC-A-G238-T4-3-20",
      "type": "ops:functional_coverage",
      "name": "批交换",
      "attributes": {
        "reference_id": "G238-T4-3-20",
        "reference_kind": "application_function",
        "reference_name": "批交换",
        "reference_definition": "文件的计划性异步分发。",
        "reference_group": "数据集成",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许在整个架构全景中实现集成与 BI 分析，包括批处理、流式、接口等；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L586",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "evidenced-in-example",
        "implementation_ref": "PIPE-night",
        "evidence_detail": "虚构运行记录RUN-11说明每晚库存文件批交换",
        "gap_action": "仅库存批交换有证据，不能推断所有数据集成已覆盖",
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
      "id": "BIC-A-G238-T4-3-21",
      "type": "ops:functional_coverage",
      "name": "BI 与分析查询执行",
      "attributes": {
        "reference_id": "G238-T4-3-21",
        "reference_kind": "application_function",
        "reference_name": "BI 与分析查询执行",
        "reference_definition": "同步的 Java 数据库连接（JDBC）或开放数据库连接（ODBC）数据库连接。",
        "reference_group": "数据集成",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许在整个架构全景中实现集成与 BI 分析，包括批处理、流式、接口等；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L587",
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
      "id": "BIC-A-G238-T4-3-22",
      "type": "ops:functional_coverage",
      "name": "手工上传或下载",
      "attributes": {
        "reference_id": "G238-T4-3-22",
        "reference_kind": "application_function",
        "reference_name": "手工上传或下载",
        "reference_definition": "集成最终用户提供的文件，或下载一组数据。",
        "reference_group": "数据集成",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许在整个架构全景中实现集成与 BI 分析，包括批处理、流式、接口等；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L588",
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
      "id": "BIC-A-G238-T4-3-23",
      "type": "ops:functional_coverage",
      "name": "数据接口",
      "attributes": {
        "reference_id": "G238-T4-3-23",
        "reference_kind": "application_function",
        "reference_name": "数据接口",
        "reference_definition": "Web 服务集成、API 等。",
        "reference_group": "数据集成",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许在整个架构全景中实现集成与 BI 分析，包括批处理、流式、接口等；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L589",
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
      "id": "BIC-A-G238-T4-3-24",
      "type": "ops:functional_coverage",
      "name": "流式",
      "attributes": {
        "reference_id": "G238-T4-3-24",
        "reference_kind": "application_function",
        "reference_name": "流式",
        "reference_definition": "通过消息系统传输并保障数据流背压的流处理。",
        "reference_group": "数据集成",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许在整个架构全景中实现集成与 BI 分析，包括批处理、流式、接口等；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L590",
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
      "id": "BIC-A-G238-T4-3-25",
      "type": "ops:functional_coverage",
      "name": "外部设备连接",
      "attributes": {
        "reference_id": "G238-T4-3-25",
        "reference_kind": "application_function",
        "reference_name": "外部设备连接",
        "reference_definition": "与外部设备连接集成。",
        "reference_group": "数据集成",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许在整个架构全景中实现集成与 BI 分析，包括批处理、流式、接口等；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L591",
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
      "id": "BIC-A-G238-T4-3-26",
      "type": "ops:functional_coverage",
      "name": "传输加密",
      "attributes": {
        "reference_id": "G238-T4-3-26",
        "reference_kind": "application_function",
        "reference_name": "传输加密",
        "reference_definition": "通过加密网络中传输中的数据（in motion）来保护数据传输。",
        "reference_group": "数据集成",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许在整个架构全景中实现集成与 BI 分析，包括批处理、流式、接口等；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L592",
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
      "id": "BIC-A-G238-T4-3-27",
      "type": "ops:functional_coverage",
      "name": "接口管理",
      "attributes": {
        "reference_id": "G238-T4-3-27",
        "reference_kind": "application_function",
        "reference_name": "接口管理",
        "reference_definition": "提供集中点，以自助方式为各实体监控与配置接口。",
        "reference_group": "数据集成",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许在整个架构全景中实现集成与 BI 分析，包括批处理、流式、接口等；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L593",
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
      "id": "BIC-A-G238-T4-3-28",
      "type": "ops:functional_coverage",
      "name": "批处理",
      "attributes": {
        "reference_id": "G238-T4-3-28",
        "reference_kind": "application_function",
        "reference_name": "批处理",
        "reference_definition": "按日、周、月、年执行的批量数据传输。",
        "reference_group": "数据处理",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许数据转换，包括基础准备或借助统计、数据科学的更高级特征计算；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L594",
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
      "id": "BIC-A-G238-T4-3-29",
      "type": "ops:functional_coverage",
      "name": "业务转换",
      "attributes": {
        "reference_id": "G238-T4-3-29",
        "reference_kind": "application_function",
        "reference_name": "业务转换",
        "reference_definition": "业务处理（过滤、聚合、连接、去重）。",
        "reference_group": "数据处理",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许数据转换，包括基础准备或借助统计、数据科学的更高级特征计算；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L595",
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
      "id": "BIC-A-G238-T4-3-30",
      "type": "ops:functional_coverage",
      "name": "质量剖析",
      "attributes": {
        "reference_id": "G238-T4-3-30",
        "reference_kind": "application_function",
        "reference_name": "质量剖析",
        "reference_definition": "通过统计技术剖析数据质量。",
        "reference_group": "数据处理",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许数据转换，包括基础准备或借助统计、数据科学的更高级特征计算；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L596",
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
      "id": "BIC-A-G238-T4-3-31",
      "type": "ops:functional_coverage",
      "name": "统计计算",
      "attributes": {
        "reference_id": "G238-T4-3-31",
        "reference_kind": "application_function",
        "reference_name": "统计计算",
        "reference_definition": "数据科学与统计处理（使用统计对数据分类、聚类，数据科学建模，含机器学习）。",
        "reference_group": "数据处理",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许数据转换，包括基础准备或借助统计、数据科学的更高级特征计算；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L597",
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
      "id": "BIC-A-G238-T4-3-32",
      "type": "ops:functional_coverage",
      "name": "删除",
      "attributes": {
        "reference_id": "G238-T4-3-32",
        "reference_kind": "application_function",
        "reference_name": "删除",
        "reference_definition": "从 BI 与分析中删除数据（如为 GDPR）。",
        "reference_group": "数据处理",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许数据转换，包括基础准备或借助统计、数据科学的更高级特征计算；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L598",
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
      "id": "BIC-A-G238-T4-3-33",
      "type": "ops:functional_coverage",
      "name": "近实时处理",
      "attributes": {
        "reference_id": "G238-T4-3-33",
        "reference_kind": "application_function",
        "reference_name": "近实时处理",
        "reference_definition": "低时延数据处理——小于 24 小时（含微批与分钟或秒级时延的近实时）。",
        "reference_group": "数据处理",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许数据转换，包括基础准备或借助统计、数据科学的更高级特征计算；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L599",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "unknown",
        "implementation_ref": "unknown",
        "evidence_detail": "没有端到端延时测量",
        "gap_action": "近实时<24小时的参考定义不能证明秒级要求",
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
      "id": "BIC-A-G238-T4-3-34",
      "type": "ops:functional_coverage",
      "name": "技术准备",
      "attributes": {
        "reference_id": "G238-T4-3-34",
        "reference_kind": "application_function",
        "reference_name": "技术准备",
        "reference_definition": "与业务无关、对所有用例通用的技术处理（即类型格式、清洗、集成）。",
        "reference_group": "数据处理",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许数据转换，包括基础准备或借助统计、数据科学的更高级特征计算；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L600",
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
      "id": "BIC-A-G238-T4-3-35",
      "type": "ops:functional_coverage",
      "name": "掩码",
      "attributes": {
        "reference_id": "G238-T4-3-35",
        "reference_kind": "application_function",
        "reference_name": "掩码",
        "reference_definition": "对 BI 与分析数据匿名化或假名化。",
        "reference_group": "数据处理",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许数据转换，包括基础准备或借助统计、数据科学的更高级特征计算；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L601",
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
      "id": "BIC-A-G238-T4-3-36",
      "type": "ops:functional_coverage",
      "name": "元数据推断",
      "attributes": {
        "reference_id": "G238-T4-3-36",
        "reference_kind": "application_function",
        "reference_name": "元数据推断",
        "reference_definition": "通过分析数据本身推断数据属性（如类型、分类、元数据等）的过程。",
        "reference_group": "数据处理",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许数据转换，包括基础准备或借助统计、数据科学的更高级特征计算；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L602",
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
      "id": "BIC-A-G238-T4-3-37",
      "type": "ops:functional_coverage",
      "name": "变更数据捕获",
      "attributes": {
        "reference_id": "G238-T4-3-37",
        "reference_kind": "application_function",
        "reference_name": "变更数据捕获",
        "reference_definition": "变更数据捕获流的摄取或分发。",
        "reference_group": "数据处理",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许数据转换，包括基础准备或借助统计、数据科学的更高级特征计算；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L603",
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
      "id": "BIC-A-G238-T4-3-38",
      "type": "ops:functional_coverage",
      "name": "原始数据存储",
      "attributes": {
        "reference_id": "G238-T4-3-38",
        "reference_kind": "application_function",
        "reference_name": "原始数据存储",
        "reference_definition": "不对源数据做任何更改的存储。",
        "reference_group": "数据存储",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许结构化或非结构化数据的持久存储；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L604",
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
      "id": "BIC-A-G238-T4-3-39",
      "type": "ops:functional_coverage",
      "name": "存储数据加密",
      "attributes": {
        "reference_id": "G238-T4-3-39",
        "reference_kind": "application_function",
        "reference_name": "存储数据加密",
        "reference_definition": "通过静态数据加密保护节点内数据。",
        "reference_group": "数据存储",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许结构化或非结构化数据的持久存储；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L605",
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
      "id": "BIC-A-G238-T4-3-40",
      "type": "ops:functional_coverage",
      "name": "元数据存储",
      "attributes": {
        "reference_id": "G238-T4-3-40",
        "reference_kind": "application_function",
        "reference_name": "元数据存储",
        "reference_definition": "存储 BI 与分析所需的元数据（模式）。",
        "reference_group": "数据存储",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许结构化或非结构化数据的持久存储；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L606",
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
      "id": "BIC-A-G238-T4-3-41",
      "type": "ops:functional_coverage",
      "name": "已准备数据存储",
      "attributes": {
        "reference_id": "G238-T4-3-41",
        "reference_kind": "application_function",
        "reference_name": "已准备数据存储",
        "reference_definition": "存储已按与业务无关的标准技术规则处理过的数据：类型格式、空值管理、唯一键生成等。",
        "reference_group": "数据存储",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许结构化或非结构化数据的持久存储；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L607",
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
      "id": "BIC-A-G238-T4-3-42",
      "type": "ops:functional_coverage",
      "name": "数据复制",
      "attributes": {
        "reference_id": "G238-T4-3-42",
        "reference_kind": "application_function",
        "reference_name": "数据复制",
        "reference_definition": "允许在不同环境之间复制数据集的功能。",
        "reference_group": "数据存储",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许结构化或非结构化数据的持久存储；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L608",
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
      "id": "BIC-A-G238-T4-3-43",
      "type": "ops:functional_coverage",
      "name": "数据版本管理",
      "attributes": {
        "reference_id": "G238-T4-3-43",
        "reference_kind": "application_function",
        "reference_name": "数据版本管理",
        "reference_definition": "便于对数据集合进行版本管理的功能。",
        "reference_group": "数据存储",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许结构化或非结构化数据的持久存储；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L609",
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
      "id": "BIC-A-G238-T4-3-44",
      "type": "ops:functional_coverage",
      "name": "信息数据存储",
      "attributes": {
        "reference_id": "G238-T4-3-44",
        "reference_kind": "application_function",
        "reference_name": "信息数据存储",
        "reference_definition": "存储为特定业务用例准备的数据：洞察、数据科学计算的特征、聚合结果；包括为流式作业执行低时延查询的能力。",
        "reference_group": "数据存储",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许结构化或非结构化数据的持久存储；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L610",
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
      "id": "BIC-A-G238-T4-3-45",
      "type": "ops:functional_coverage",
      "name": "敏感数据存储",
      "attributes": {
        "reference_id": "G238-T4-3-45",
        "reference_kind": "application_function",
        "reference_name": "敏感数据存储",
        "reference_definition": "存储敏感数据，如个人、财务、战略、业务数据等。",
        "reference_group": "数据存储",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许结构化或非结构化数据的持久存储；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L611",
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
      "id": "BIC-A-G238-T4-3-46",
      "type": "ops:functional_coverage",
      "name": "归档与压缩",
      "attributes": {
        "reference_id": "G238-T4-3-46",
        "reference_kind": "application_function",
        "reference_name": "归档与压缩",
        "reference_definition": "管理数据生命周期并优化存储资源的归档与压缩功能。",
        "reference_group": "数据存储",
        "reference_level": "child-in-source-group",
        "reference_scope": "（允许结构化或非结构化数据的持久存储；下列要求适用于完整范围）",
        "source_locator": "G238 表4-3 L612",
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
      "id": "BIC-A-G238-T4-3-47",
      "type": "ops:functional_coverage",
      "name": "可视化数据发现",
      "attributes": {
        "reference_id": "G238-T4-3-47",
        "reference_kind": "application_function",
        "reference_name": "可视化数据发现",
        "reference_definition": "动态下钻以浏览数据并找到合适的图表、图形等。",
        "reference_group": "决策支持分析与可视化",
        "reference_level": "child-in-source-group",
        "reference_scope": "（支持使用 BI 与分析中存储的数据进行数据发现与可视化）",
        "source_locator": "G238 表4-3 L613",
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
      "id": "BIC-A-G238-T4-3-48",
      "type": "ops:functional_coverage",
      "name": "统计分析",
      "attributes": {
        "reference_id": "G238-T4-3-48",
        "reference_kind": "application_function",
        "reference_name": "统计分析",
        "reference_definition": "对在线可用信息应用动态的统计“现成”模型。",
        "reference_group": "决策支持分析与可视化",
        "reference_level": "child-in-source-group",
        "reference_scope": "（支持使用 BI 与分析中存储的数据进行数据发现与可视化）",
        "source_locator": "G238 表4-3 L614",
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
      "id": "BIC-A-G238-T4-3-49",
      "type": "ops:functional_coverage",
      "name": "动态数据准备",
      "attributes": {
        "reference_id": "G238-T4-3-49",
        "reference_kind": "application_function",
        "reference_name": "动态数据准备",
        "reference_definition": "不持久化的数据动态准备，以支持统计处理。",
        "reference_group": "决策支持分析与可视化",
        "reference_level": "child-in-source-group",
        "reference_scope": "（支持使用 BI 与分析中存储的数据进行数据发现与可视化）",
        "source_locator": "G238 表4-3 L615",
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
      "id": "BIC-A-G238-T4-3-50",
      "type": "ops:functional_coverage",
      "name": "信息服务",
      "attributes": {
        "reference_id": "G238-T4-3-50",
        "reference_kind": "application_function",
        "reference_name": "信息服务",
        "reference_definition": "以适合查询的格式（立方体、内存、视图等）存储信息数据。",
        "reference_group": "信息报表与仪表盘",
        "reference_level": "child-in-source-group",
        "reference_scope": "（支持使用 BI 与分析中存储的数据开展报表与仪表盘活动）",
        "source_locator": "G238 表4-3 L616",
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
      "id": "BIC-A-G238-T4-3-51",
      "type": "ops:functional_coverage",
      "name": "格式化在线报表",
      "attributes": {
        "reference_id": "G238-T4-3-51",
        "reference_kind": "application_function",
        "reference_name": "格式化在线报表",
        "reference_definition": "可交互刷新的即用型报表与图表，使不具备专门数据管理技能的用户也能使用数据。",
        "reference_group": "信息报表与仪表盘",
        "reference_level": "child-in-source-group",
        "reference_scope": "（支持使用 BI 与分析中存储的数据开展报表与仪表盘活动）",
        "source_locator": "G238 表4-3 L617",
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
      "id": "BIC-A-G238-T4-3-52",
      "type": "ops:functional_coverage",
      "name": "报表创作",
      "attributes": {
        "reference_id": "G238-T4-3-52",
        "reference_kind": "application_function",
        "reference_name": "报表创作",
        "reference_definition": "构建报表并用数据刷新；业务用户无需 SQL 技能，通过拖拽式用户界面（UI）即可基于可用信息创建报表并与其他用户共享。",
        "reference_group": "信息报表与仪表盘",
        "reference_level": "child-in-source-group",
        "reference_scope": "（支持使用 BI 与分析中存储的数据开展报表与仪表盘活动）",
        "source_locator": "G238 表4-3 L618",
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
      "id": "BIC-A-G238-T4-3-53",
      "type": "ops:functional_coverage",
      "name": "报表分发调度",
      "attributes": {
        "reference_id": "G238-T4-3-53",
        "reference_kind": "application_function",
        "reference_name": "报表分发调度",
        "reference_definition": "定期生成的即用型静态报表、图表，通常分页并以可打印格式提供。",
        "reference_group": "信息报表与仪表盘",
        "reference_level": "child-in-source-group",
        "reference_scope": "（支持使用 BI 与分析中存储的数据开展报表与仪表盘活动）",
        "source_locator": "G238 表4-3 L619",
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
      "id": "BIC-A-G238-T4-3-54",
      "type": "ops:functional_coverage",
      "name": "基本数据表操作与分析",
      "attributes": {
        "reference_id": "G238-T4-3-54",
        "reference_kind": "application_function",
        "reference_name": "基本数据表操作与分析",
        "reference_definition": "便于对数据表进行最基础、最频繁的操作、处理与分析的功能。",
        "reference_group": "信息报表与仪表盘",
        "reference_level": "child-in-source-group",
        "reference_scope": "（支持使用 BI 与分析中存储的数据开展报表与仪表盘活动）",
        "source_locator": "G238 表4-3 L620",
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
      "id": "BIC-A-G238-T4-3-55",
      "type": "ops:functional_coverage",
      "name": "技术监控",
      "attributes": {
        "reference_id": "G238-T4-3-55",
        "reference_kind": "application_function",
        "reference_name": "技术监控",
        "reference_definition": "对网络层与基础设施层的监控。",
        "reference_group": "监控",
        "reference_level": "child-in-source-group",
        "reference_scope": "（对基础设施、网络与应用进行监控，以保障约定的服务水平）",
        "source_locator": "G238 表4-3 L621",
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
      "id": "BIC-A-G238-T4-3-56",
      "type": "ops:functional_coverage",
      "name": "业务使用监控",
      "attributes": {
        "reference_id": "G238-T4-3-56",
        "reference_kind": "application_function",
        "reference_name": "业务使用监控",
        "reference_definition": "对平台业务服务的监控（监督数据科学模型漂移等）。",
        "reference_group": "监控",
        "reference_level": "child-in-source-group",
        "reference_scope": "（对基础设施、网络与应用进行监控，以保障约定的服务水平）",
        "source_locator": "G238 表4-3 L622",
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
      "id": "BIC-A-G238-T4-3-57",
      "type": "ops:functional_coverage",
      "name": "安全监控",
      "attributes": {
        "reference_id": "G238-T4-3-57",
        "reference_kind": "application_function",
        "reference_name": "安全监控",
        "reference_definition": "对安全层的监控。",
        "reference_group": "监控",
        "reference_level": "child-in-source-group",
        "reference_scope": "（对基础设施、网络与应用进行监控，以保障约定的服务水平）",
        "source_locator": "G238 表4-3 L623",
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
      "id": "BIC-A-G238-T4-3-58",
      "type": "ops:functional_coverage",
      "name": "数据与应用监控",
      "attributes": {
        "reference_id": "G238-T4-3-58",
        "reference_kind": "application_function",
        "reference_name": "数据与应用监控",
        "reference_definition": "对数据（如质量）与应用层（如服务可用性）的监控。",
        "reference_group": "监控",
        "reference_level": "child-in-source-group",
        "reference_scope": "（对基础设施、网络与应用进行监控，以保障约定的服务水平）",
        "source_locator": "G238 表4-3 L624",
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
      "id": "BIC-A-G238-T4-3-59",
      "type": "ops:functional_coverage",
      "name": "血缘与审计",
      "attributes": {
        "reference_id": "G238-T4-3-59",
        "reference_kind": "application_function",
        "reference_name": "血缘与审计",
        "reference_definition": "捕获数据生命周期，包括数据来源及其随时间迁移的位置。",
        "reference_group": "监控",
        "reference_level": "child-in-source-group",
        "reference_scope": "（对基础设施、网络与应用进行监控，以保障约定的服务水平）",
        "source_locator": "G238 表4-3 L625",
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
    }
  ],
  "relationships": [],
  "extensions": {
    "relationship_types": {}
  },
  "states": [],
  "view": {
    "id": "v-bi-application-function-coverage",
    "artifact_id": "bi-requirements-profile",
    "profile_id": "bi-application-function-coverage",
    "title": "BI应用功能参考覆盖",
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
      "BIC-A-G238-T4-3-01",
      "BIC-A-G238-T4-3-02",
      "BIC-A-G238-T4-3-03",
      "BIC-A-G238-T4-3-04",
      "BIC-A-G238-T4-3-05",
      "BIC-A-G238-T4-3-06",
      "BIC-A-G238-T4-3-07",
      "BIC-A-G238-T4-3-08",
      "BIC-A-G238-T4-3-09",
      "BIC-A-G238-T4-3-10",
      "BIC-A-G238-T4-3-11",
      "BIC-A-G238-T4-3-12",
      "BIC-A-G238-T4-3-13",
      "BIC-A-G238-T4-3-14",
      "BIC-A-G238-T4-3-15",
      "BIC-A-G238-T4-3-16",
      "BIC-A-G238-T4-3-17",
      "BIC-A-G238-T4-3-18",
      "BIC-A-G238-T4-3-19",
      "BIC-A-G238-T4-3-20",
      "BIC-A-G238-T4-3-21",
      "BIC-A-G238-T4-3-22",
      "BIC-A-G238-T4-3-23",
      "BIC-A-G238-T4-3-24",
      "BIC-A-G238-T4-3-25",
      "BIC-A-G238-T4-3-26",
      "BIC-A-G238-T4-3-27",
      "BIC-A-G238-T4-3-28",
      "BIC-A-G238-T4-3-29",
      "BIC-A-G238-T4-3-30",
      "BIC-A-G238-T4-3-31",
      "BIC-A-G238-T4-3-32",
      "BIC-A-G238-T4-3-33",
      "BIC-A-G238-T4-3-34",
      "BIC-A-G238-T4-3-35",
      "BIC-A-G238-T4-3-36",
      "BIC-A-G238-T4-3-37",
      "BIC-A-G238-T4-3-38",
      "BIC-A-G238-T4-3-39",
      "BIC-A-G238-T4-3-40",
      "BIC-A-G238-T4-3-41",
      "BIC-A-G238-T4-3-42",
      "BIC-A-G238-T4-3-43",
      "BIC-A-G238-T4-3-44",
      "BIC-A-G238-T4-3-45",
      "BIC-A-G238-T4-3-46",
      "BIC-A-G238-T4-3-47",
      "BIC-A-G238-T4-3-48",
      "BIC-A-G238-T4-3-49",
      "BIC-A-G238-T4-3-50",
      "BIC-A-G238-T4-3-51",
      "BIC-A-G238-T4-3-52",
      "BIC-A-G238-T4-3-53",
      "BIC-A-G238-T4-3-54",
      "BIC-A-G238-T4-3-55",
      "BIC-A-G238-T4-3-56",
      "BIC-A-G238-T4-3-57",
      "BIC-A-G238-T4-3-58",
      "BIC-A-G238-T4-3-59"
    ],
    "relationship_ids": [],
    "analysis": "依据raw-brief.md的虚构材料，按analysis.md人工分析；生成器转换已审查模型。",
    "legend": "参考功能行不是实际部署；计划和未知不计已实现。本表不声明来源图视觉通过。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile bi-application-function-coverage --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile bi-application-function-coverage --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
