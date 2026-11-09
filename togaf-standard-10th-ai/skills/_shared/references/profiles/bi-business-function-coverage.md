# BI业务功能参考覆盖

`profile_id`: bi-business-function-coverage；`artifact_id`: bi-requirements-profile；主责：[togaf-requirements](../../../togaf-requirements/SKILL.md)。

来源：G238 §2.2、表4-2。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-operations-1。

{
  "id": "bi-business-function-coverage",
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
  "raw_input": "examples/addenda/operations/bi-business-function-coverage/raw-brief.md",
  "analysis_path": "examples/addenda/operations/bi-business-function-coverage/analysis.md",
  "sources": [
    {
      "id": "case-source",
      "kind": "example",
      "description": "海岚只出示U1/U2用途待办及拟每周复核模型的计划。其余业务功能没有访谈/运行证据；不能因软件已采购就声称覆盖。54源表行包括宏观参考行与子功能，全部逐行登记未知/已见/计划。",
      "locator": "raw-brief.md"
    }
  ],
  "entities": [
    {
      "id": "BIC-B-G238-T4-2-01",
      "type": "ops:functional_coverage",
      "name": "定义战略与路线图",
      "attributes": {
        "reference_id": "G238-T4-2-01",
        "reference_kind": "business_function",
        "reference_name": "定义战略与路线图",
        "reference_definition": "见 2.2 节。",
        "reference_group": "定义战略与路线图",
        "reference_level": "macro",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L465",
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
      "id": "BIC-B-G238-T4-2-02",
      "type": "ops:functional_coverage",
      "name": "构建 BI 与分析战略",
      "attributes": {
        "reference_id": "G238-T4-2-02",
        "reference_kind": "business_function",
        "reference_name": "构建 BI 与分析战略",
        "reference_definition": "围绕 BI 与分析构建业务与 IT 战略，明确目标与整体旅程。",
        "reference_group": "定义战略与路线图",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L466",
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
      "id": "BIC-B-G238-T4-2-03",
      "type": "ops:functional_coverage",
      "name": "构建路线图",
      "attributes": {
        "reference_id": "G238-T4-2-03",
        "reference_kind": "business_function",
        "reference_name": "构建路线图",
        "reference_definition": "构建实施 BI 与分析战略的路线图。",
        "reference_group": "定义战略与路线图",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L467",
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
      "id": "BIC-B-G238-T4-2-04",
      "type": "ops:functional_coverage",
      "name": "维护 BI 与分析用途待办列表",
      "attributes": {
        "reference_id": "G238-T4-2-04",
        "reference_kind": "business_function",
        "reference_name": "维护 BI 与分析用途待办列表",
        "reference_definition": "维护一份由 BI 与分析能力支持（或应支持）的合格业务用途清单。",
        "reference_group": "定义战略与路线图",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L468",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "evidenced-in-example",
        "implementation_ref": "BACKLOG-11",
        "evidence_detail": "虚构访谈和U1/U2用途清单证明两用例待办已编制",
        "gap_action": "需继续验合格标准与版本治理",
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
      "id": "BIC-B-G238-T4-2-05",
      "type": "ops:functional_coverage",
      "name": "定义 KPI",
      "attributes": {
        "reference_id": "G238-T4-2-05",
        "reference_kind": "business_function",
        "reference_name": "定义 KPI",
        "reference_definition": "定义用于展示 BI 与分析如何实现战略目标（定性/定量）的 KPI。",
        "reference_group": "定义战略与路线图",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L469",
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
      "id": "BIC-B-G238-T4-2-06",
      "type": "ops:functional_coverage",
      "name": "识别并发展赞助",
      "attributes": {
        "reference_id": "G238-T4-2-06",
        "reference_kind": "business_function",
        "reference_name": "识别并发展赞助",
        "reference_definition": "让业务与 IT 赞助人参与 BI 与分析治理。",
        "reference_group": "定义战略与路线图",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L470",
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
      "id": "BIC-B-G238-T4-2-07",
      "type": "ops:functional_coverage",
      "name": "确保与相关战略一致（安全、可持续性等）",
      "attributes": {
        "reference_id": "G238-T4-2-07",
        "reference_kind": "business_function",
        "reference_name": "确保与相关战略一致（安全、可持续性等）",
        "reference_definition": "确保 BI 与分析的抱负与实现同组织各项政策一致（尤其是安全、合规与数字可持续性政策）。",
        "reference_group": "定义战略与路线图",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L471",
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
      "id": "BIC-B-G238-T4-2-08",
      "type": "ops:functional_coverage",
      "name": "设计与开发 BI 与分析价值链条",
      "attributes": {
        "reference_id": "G238-T4-2-08",
        "reference_kind": "business_function",
        "reference_name": "设计与开发 BI 与分析价值链条",
        "reference_definition": "见 2.2 节。",
        "reference_group": "设计与开发 BI 与分析价值链条",
        "reference_level": "macro",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L472",
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
      "id": "BIC-B-G238-T4-2-09",
      "type": "ops:functional_coverage",
      "name": "定义 BI 与分析架构原则并确保方案一致性",
      "attributes": {
        "reference_id": "G238-T4-2-09",
        "reference_kind": "business_function",
        "reference_name": "定义 BI 与分析架构原则并确保方案一致性",
        "reference_definition": "定义 BI 与分析架构原则，确保解决方案的一致性。",
        "reference_group": "设计与开发 BI 与分析价值链条",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L473",
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
      "id": "BIC-B-G238-T4-2-10",
      "type": "ops:functional_coverage",
      "name": "设计基础设施与适配的存储空间",
      "attributes": {
        "reference_id": "G238-T4-2-10",
        "reference_kind": "business_function",
        "reference_name": "设计基础设施与适配的存储空间",
        "reference_definition": "设计面向 BI 与分析的技术架构，包括按不同需求与用途（冷数据、热数据、敏感数据等）结构化相关存储空间。",
        "reference_group": "设计与开发 BI 与分析价值链条",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L474",
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
      "id": "BIC-B-G238-T4-2-11",
      "type": "ops:functional_coverage",
      "name": "依据用途建模并构建数据结构化（原始、仓库、业务视图）",
      "attributes": {
        "reference_id": "G238-T4-2-11",
        "reference_kind": "business_function",
        "reference_name": "依据用途建模并构建数据结构化（原始、仓库、业务视图）",
        "reference_definition": "对数据建模并实施结构化，以支撑从原始数据到业务视图的整个价值链条。",
        "reference_group": "设计与开发 BI 与分析价值链条",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L475",
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
      "id": "BIC-B-G238-T4-2-12",
      "type": "ops:functional_coverage",
      "name": "定义并实施业务规则",
      "attributes": {
        "reference_id": "G238-T4-2-12",
        "reference_kind": "business_function",
        "reference_name": "定义并实施业务规则",
        "reference_definition": "定义并实施与业务需求相关的规则（业务计算规则、业务数据有效性检查等）。",
        "reference_group": "设计与开发 BI 与分析价值链条",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L476",
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
      "id": "BIC-B-G238-T4-2-13",
      "type": "ops:functional_coverage",
      "name": "定义并实施技术规则",
      "attributes": {
        "reference_id": "G238-T4-2-13",
        "reference_kind": "business_function",
        "reference_name": "定义并实施技术规则",
        "reference_definition": "定义并实施技术规则，通常为基础技术格式规则（如数据同质性、浮点格式等）。",
        "reference_group": "设计与开发 BI 与分析价值链条",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L477",
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
      "id": "BIC-B-G238-T4-2-14",
      "type": "ops:functional_coverage",
      "name": "定义并实施特定数据保护规则",
      "attributes": {
        "reference_id": "G238-T4-2-14",
        "reference_kind": "business_function",
        "reference_name": "定义并实施特定数据保护规则",
        "reference_definition": "定义并实施特定数据保护规则，包括保留规则、合规自动化等。",
        "reference_group": "设计与开发 BI 与分析价值链条",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L478",
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
      "id": "BIC-B-G238-T4-2-15",
      "type": "ops:functional_coverage",
      "name": "设计与开发数据管道",
      "attributes": {
        "reference_id": "G238-T4-2-15",
        "reference_kind": "business_function",
        "reference_name": "设计与开发数据管道",
        "reference_definition": "设计并开发从原始数据到业务视图的流程。",
        "reference_group": "设计与开发 BI 与分析价值链条",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L479",
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
      "id": "BIC-B-G238-T4-2-16",
      "type": "ops:functional_coverage",
      "name": "设计语义层",
      "attributes": {
        "reference_id": "G238-T4-2-16",
        "reference_kind": "business_function",
        "reference_name": "设计语义层",
        "reference_definition": "设计语义层，使业务用户能方便地操作数据，例如用于即席/自助报表。",
        "reference_group": "设计与开发 BI 与分析价值链条",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L480",
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
      "id": "BIC-B-G238-T4-2-17",
      "type": "ops:functional_coverage",
      "name": "数据整理（Data Wrangling）",
      "attributes": {
        "reference_id": "G238-T4-2-17",
        "reference_kind": "business_function",
        "reference_name": "数据整理（Data Wrangling）",
        "reference_definition": "探索数据、为分析目的可视化可用数据、构建首批样本机器学习模型（用于探索）。",
        "reference_group": "设计与开发 BI 与分析价值链条",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L481",
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
      "id": "BIC-B-G238-T4-2-18",
      "type": "ops:functional_coverage",
      "name": "设计与构建高级分析模型",
      "attributes": {
        "reference_id": "G238-T4-2-18",
        "reference_kind": "business_function",
        "reference_name": "设计与构建高级分析模型",
        "reference_definition": "与业务共同确定需建模的事件或问题、目的及运营要求；设计并构建满足要求的高级分析模型，并依据要求评估模型。",
        "reference_group": "设计与开发 BI 与分析价值链条",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L482",
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
      "id": "BIC-B-G238-T4-2-19",
      "type": "ops:functional_coverage",
      "name": "设计与构建工业化稳定报表",
      "attributes": {
        "reference_id": "G238-T4-2-19",
        "reference_kind": "business_function",
        "reference_name": "设计与构建工业化稳定报表",
        "reference_definition": "设计并构建稳定的周期性报表。",
        "reference_group": "设计与开发 BI 与分析价值链条",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L483",
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
      "id": "BIC-B-G238-T4-2-20",
      "type": "ops:functional_coverage",
      "name": "设计与构建即席报表",
      "attributes": {
        "reference_id": "G238-T4-2-20",
        "reference_kind": "business_function",
        "reference_name": "设计与构建即席报表",
        "reference_definition": "设计并构建即席报表，例如以“自助”模式——通常由业务参与者（最终用户）直接完成。",
        "reference_group": "设计与开发 BI 与分析价值链条",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L484",
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
      "id": "BIC-B-G238-T4-2-21",
      "type": "ops:functional_coverage",
      "name": "工业化并部署高级分析模型",
      "attributes": {
        "reference_id": "G238-T4-2-21",
        "reference_kind": "business_function",
        "reference_name": "工业化并部署高级分析模型",
        "reference_definition": "把已验证的高级分析模型（如分类模型）投入运营，集成到相关业务流程（如用于优化），并建立监控与控制真实环境准确性的方式。",
        "reference_group": "设计与开发 BI 与分析价值链条",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L485",
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
      "id": "BIC-B-G238-T4-2-22",
      "type": "ops:functional_coverage",
      "name": "为 BI 与分析提供必要数据源",
      "attributes": {
        "reference_id": "G238-T4-2-22",
        "reference_kind": "business_function",
        "reference_name": "为 BI 与分析提供必要数据源",
        "reference_definition": "见 2.2 节。",
        "reference_group": "为 BI 与分析提供必要数据源",
        "reference_level": "macro",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L486",
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
      "id": "BIC-B-G238-T4-2-23",
      "type": "ops:functional_coverage",
      "name": "识别相关数据源",
      "attributes": {
        "reference_id": "G238-T4-2-23",
        "reference_kind": "business_function",
        "reference_name": "识别相关数据源",
        "reference_definition": "制定实践与流程，快速、精确地识别给定用例的相关数据源并对其加以认证。",
        "reference_group": "为 BI 与分析提供必要数据源",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L487",
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
      "id": "BIC-B-G238-T4-2-24",
      "type": "ops:functional_coverage",
      "name": "识别并管理数据提供方",
      "attributes": {
        "reference_id": "G238-T4-2-24",
        "reference_kind": "business_function",
        "reference_name": "识别并管理数据提供方",
        "reference_definition": "管理与外部数据提供方的技术与业务关系。",
        "reference_group": "为 BI 与分析提供必要数据源",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L488",
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
      "id": "BIC-B-G238-T4-2-25",
      "type": "ops:functional_coverage",
      "name": "设计并构建必要数据接口",
      "attributes": {
        "reference_id": "G238-T4-2-25",
        "reference_kind": "business_function",
        "reference_name": "设计并构建必要数据接口",
        "reference_definition": "设计并构建支撑 BI 与分析价值链的数据接口，例如从数据源向原始数据空间供数、使运营系统与 BI 分析能力计算的指标对齐等。",
        "reference_group": "为 BI 与分析提供必要数据源",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L489",
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
      "id": "BIC-B-G238-T4-2-26",
      "type": "ops:functional_coverage",
      "name": "治理与度量",
      "attributes": {
        "reference_id": "G238-T4-2-26",
        "reference_kind": "business_function",
        "reference_name": "治理与度量",
        "reference_definition": "见 2.2 节。",
        "reference_group": "治理与度量",
        "reference_level": "macro",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L490",
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
      "id": "BIC-B-G238-T4-2-27",
      "type": "ops:functional_coverage",
      "name": "定义治理组织与 RACI",
      "attributes": {
        "reference_id": "G238-T4-2-27",
        "reference_kind": "business_function",
        "reference_name": "定义治理组织与 RACI",
        "reference_definition": "定义治理组织，尤其包括业务参与者、CDO 与 IT 团队在能力建设与运行中的角色。",
        "reference_group": "治理与度量",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L491",
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
      "id": "BIC-B-G238-T4-2-28",
      "type": "ops:functional_coverage",
      "name": "定义并执行新数据源接入流程",
      "attributes": {
        "reference_id": "G238-T4-2-28",
        "reference_kind": "business_function",
        "reference_name": "定义并执行新数据源接入流程",
        "reference_definition": "定义数据接入流程：新数据源进入 BI 与分析范围时应做什么（新源认证、相关数据认证、加入元数据管理存储库、BI 与分析用途规格等）。",
        "reference_group": "治理与度量",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L492",
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
      "id": "BIC-B-G238-T4-2-29",
      "type": "ops:functional_coverage",
      "name": "定义并执行成本优化原则",
      "attributes": {
        "reference_id": "G238-T4-2-29",
        "reference_kind": "business_function",
        "reference_name": "定义并执行成本优化原则",
        "reference_definition": "定义如何优化 BI 与分析能力成本（围绕组织、流程、技术平台实施与监控的优化原则等）。",
        "reference_group": "治理与度量",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L493",
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
      "id": "BIC-B-G238-T4-2-30",
      "type": "ops:functional_coverage",
      "name": "定义并执行合规要求",
      "attributes": {
        "reference_id": "G238-T4-2-30",
        "reference_kind": "business_function",
        "reference_name": "定义并执行合规要求",
        "reference_definition": "定义并执行合规要求。",
        "reference_group": "治理与度量",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L494",
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
      "id": "BIC-B-G238-T4-2-31",
      "type": "ops:functional_coverage",
      "name": "度量数据量",
      "attributes": {
        "reference_id": "G238-T4-2-31",
        "reference_kind": "business_function",
        "reference_name": "度量数据量",
        "reference_definition": "了解 BI 与分析所需数据量（有助于监控与控制成本、促进数字可持续性等）。",
        "reference_group": "治理与度量",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L495",
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
      "id": "BIC-B-G238-T4-2-32",
      "type": "ops:functional_coverage",
      "name": "度量数据使用频率",
      "attributes": {
        "reference_id": "G238-T4-2-32",
        "reference_kind": "business_function",
        "reference_name": "度量数据使用频率",
        "reference_definition": "了解哪些数据被使用、哪些使用不足；这是理解平台现有数据价值的关键信息。",
        "reference_group": "治理与度量",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L496",
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
      "id": "BIC-B-G238-T4-2-33",
      "type": "ops:functional_coverage",
      "name": "跟踪用途 ROI",
      "attributes": {
        "reference_id": "G238-T4-2-33",
        "reference_kind": "business_function",
        "reference_name": "跟踪用途 ROI",
        "reference_definition": "通过投资回报（ROI）的定义与计算，衡量 BI 与分析用途的价值。",
        "reference_group": "治理与度量",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L497",
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
      "id": "BIC-B-G238-T4-2-34",
      "type": "ops:functional_coverage",
      "name": "保护数据并确保合规",
      "attributes": {
        "reference_id": "G238-T4-2-34",
        "reference_kind": "business_function",
        "reference_name": "保护数据并确保合规",
        "reference_definition": "见 2.2 节。",
        "reference_group": "保护数据并确保合规",
        "reference_level": "macro",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L498",
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
      "id": "BIC-B-G238-T4-2-35",
      "type": "ops:functional_coverage",
      "name": "定义并管理数据访问",
      "attributes": {
        "reference_id": "G238-T4-2-35",
        "reference_kind": "business_function",
        "reference_name": "定义并管理数据访问",
        "reference_definition": "定义、管理并控制数据的访问方式、途径与主体。",
        "reference_group": "保护数据并确保合规",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L499",
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
      "id": "BIC-B-G238-T4-2-36",
      "type": "ops:functional_coverage",
      "name": "审计平台安全与合规",
      "attributes": {
        "reference_id": "G238-T4-2-36",
        "reference_kind": "business_function",
        "reference_name": "审计平台安全与合规",
        "reference_definition": "对 BI 与分析平台、流程、安全与合规建立定期审计。",
        "reference_group": "保护数据并确保合规",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L500",
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
      "id": "BIC-B-G238-T4-2-37",
      "type": "ops:functional_coverage",
      "name": "定义匿名化需求与流程",
      "attributes": {
        "reference_id": "G238-T4-2-37",
        "reference_kind": "business_function",
        "reference_name": "定义匿名化需求与流程",
        "reference_definition": "定义数据匿名化/假名化的原因与方式。",
        "reference_group": "保护数据并确保合规",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L501",
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
      "id": "BIC-B-G238-T4-2-38",
      "type": "ops:functional_coverage",
      "name": "检测并通知数据泄露",
      "attributes": {
        "reference_id": "G238-T4-2-38",
        "reference_kind": "business_function",
        "reference_name": "检测并通知数据泄露",
        "reference_definition": "建立检测并通知潜在数据泄露的流程。",
        "reference_group": "保护数据并确保合规",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L502",
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
      "id": "BIC-B-G238-T4-2-39",
      "type": "ops:functional_coverage",
      "name": "支持处理数据可携带请求",
      "attributes": {
        "reference_id": "G238-T4-2-39",
        "reference_kind": "business_function",
        "reference_name": "支持处理数据可携带请求",
        "reference_definition": "建立组织以支持数据可携带请求的处理。",
        "reference_group": "保护数据并确保合规",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L503",
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
      "id": "BIC-B-G238-T4-2-40",
      "type": "ops:functional_coverage",
      "name": "定义并应用数据质量框架",
      "attributes": {
        "reference_id": "G238-T4-2-40",
        "reference_kind": "business_function",
        "reference_name": "定义并应用数据质量框架",
        "reference_definition": "为 BI 与分析应用数据质量框架。",
        "reference_group": "定义并应用数据质量框架",
        "reference_level": "standalone-high-function",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L504",
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
      "id": "BIC-B-G238-T4-2-41",
      "type": "ops:functional_coverage",
      "name": "为 BI 与分析利用元数据管理",
      "attributes": {
        "reference_id": "G238-T4-2-41",
        "reference_kind": "business_function",
        "reference_name": "为 BI 与分析利用元数据管理",
        "reference_definition": "在 BI 与分析数据价值链上应用元数据管理能力。",
        "reference_group": "为 BI 与分析利用元数据管理",
        "reference_level": "standalone-high-function",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L505",
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
      "id": "BIC-B-G238-T4-2-42",
      "type": "ops:functional_coverage",
      "name": "运营平台",
      "attributes": {
        "reference_id": "G238-T4-2-42",
        "reference_kind": "business_function",
        "reference_name": "运营平台",
        "reference_definition": "见 2.2 节。",
        "reference_group": "运营平台",
        "reference_level": "macro",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L506",
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
      "id": "BIC-B-G238-T4-2-43",
      "type": "ops:functional_coverage",
      "name": "检测并管理事件",
      "attributes": {
        "reference_id": "G238-T4-2-43",
        "reference_kind": "business_function",
        "reference_name": "检测并管理事件",
        "reference_definition": "检测并管理 BI 与分析平台/工具上的事件。",
        "reference_group": "运营平台",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L507",
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
      "id": "BIC-B-G238-T4-2-44",
      "type": "ops:functional_coverage",
      "name": "检测并管理数据问题",
      "attributes": {
        "reference_id": "G238-T4-2-44",
        "reference_kind": "business_function",
        "reference_name": "检测并管理数据问题",
        "reference_definition": "检测并管理数据问题（数据质量、数据管道问题等）。",
        "reference_group": "运营平台",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L508",
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
      "id": "BIC-B-G238-T4-2-45",
      "type": "ops:functional_coverage",
      "name": "监控与控制成本",
      "attributes": {
        "reference_id": "G238-T4-2-45",
        "reference_kind": "business_function",
        "reference_name": "监控与控制成本",
        "reference_definition": "监控成本，尤其是云解决方案。",
        "reference_group": "运营平台",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L509",
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
      "id": "BIC-B-G238-T4-2-46",
      "type": "ops:functional_coverage",
      "name": "监控与控制数据质量",
      "attributes": {
        "reference_id": "G238-T4-2-46",
        "reference_kind": "business_function",
        "reference_name": "监控与控制数据质量",
        "reference_definition": "监控 BI 与分析用例所用数据的质量。",
        "reference_group": "运营平台",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L510",
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
      "id": "BIC-B-G238-T4-2-47",
      "type": "ops:functional_coverage",
      "name": "监控与控制模型准确性",
      "attributes": {
        "reference_id": "G238-T4-2-47",
        "reference_kind": "business_function",
        "reference_name": "监控与控制模型准确性",
        "reference_definition": "监控已部署高级分析模型的准确性。",
        "reference_group": "运营平台",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L511",
        "reference_identity": "reference-only; coverage-assessment-is-project-record",
        "project_scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "coverage_status": "planned",
        "implementation_ref": "OPS-model-review",
        "evidence_detail": "模型运营负责人拟定每周复核",
        "gap_action": "尚无准确性实际监控记录",
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
      "id": "BIC-B-G238-T4-2-48",
      "type": "ops:functional_coverage",
      "name": "调度数据集成与管道",
      "attributes": {
        "reference_id": "G238-T4-2-48",
        "reference_kind": "business_function",
        "reference_name": "调度数据集成与管道",
        "reference_definition": "管理 BI 与分析的所有调度任务（数据管道运行、集成等）。",
        "reference_group": "运营平台",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L512",
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
      "id": "BIC-B-G238-T4-2-49",
      "type": "ops:functional_coverage",
      "name": "授予访问",
      "attributes": {
        "reference_id": "G238-T4-2-49",
        "reference_kind": "business_function",
        "reference_name": "授予访问",
        "reference_definition": "按合规与安全政策处理访问请求/授予访问。",
        "reference_group": "运营平台",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L513",
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
      "id": "BIC-B-G238-T4-2-50",
      "type": "ops:functional_coverage",
      "name": "沟通与培训",
      "attributes": {
        "reference_id": "G238-T4-2-50",
        "reference_kind": "business_function",
        "reference_name": "沟通与培训",
        "reference_definition": "见 2.2 节。",
        "reference_group": "沟通与培训",
        "reference_level": "macro",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L514",
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
      "id": "BIC-B-G238-T4-2-51",
      "type": "ops:functional_coverage",
      "name": "培训最终用户使用 BI 与分析工具",
      "attributes": {
        "reference_id": "G238-T4-2-51",
        "reference_kind": "business_function",
        "reference_name": "培训最终用户使用 BI 与分析工具",
        "reference_definition": "组织培训，使每位业务与数据专家都能熟练开展 BI 与分析实践。",
        "reference_group": "沟通与培训",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L515",
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
      "id": "BIC-B-G238-T4-2-52",
      "type": "ops:functional_coverage",
      "name": "利用技术布道",
      "attributes": {
        "reference_id": "G238-T4-2-52",
        "reference_kind": "business_function",
        "reference_name": "利用技术布道",
        "reference_definition": "鼓励数据专家（数据科学家、数据工程师、数据管理者等）之间的知识资本化与经验回流，利用可复用材料。",
        "reference_group": "沟通与培训",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L516",
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
      "id": "BIC-B-G238-T4-2-53",
      "type": "ops:functional_coverage",
      "name": "活跃 BI 与分析用户与专家社区",
      "attributes": {
        "reference_id": "G238-T4-2-53",
        "reference_kind": "business_function",
        "reference_name": "活跃 BI 与分析用户与专家社区",
        "reference_definition": "活跃用户社区（如 BI 与分析平台工具）与数据专家社区。",
        "reference_group": "沟通与培训",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L517",
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
      "id": "BIC-B-G238-T4-2-54",
      "type": "ops:functional_coverage",
      "name": "就战略、业务与技术路线图开展沟通",
      "attributes": {
        "reference_id": "G238-T4-2-54",
        "reference_kind": "business_function",
        "reference_name": "就战略、业务与技术路线图开展沟通",
        "reference_definition": "沟通 BI 与分析战略、价值、进行中/已完成的关键项目，以及业务与技术路线图；沟通能力对组织的影响。",
        "reference_group": "沟通与培训",
        "reference_level": "child",
        "reference_scope": "源表分组；无额外应用范围规则",
        "source_locator": "G238 表4-2 L518",
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
    "id": "v-bi-business-function-coverage",
    "artifact_id": "bi-requirements-profile",
    "profile_id": "bi-business-function-coverage",
    "title": "BI业务功能参考覆盖",
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
      "BIC-B-G238-T4-2-01",
      "BIC-B-G238-T4-2-02",
      "BIC-B-G238-T4-2-03",
      "BIC-B-G238-T4-2-04",
      "BIC-B-G238-T4-2-05",
      "BIC-B-G238-T4-2-06",
      "BIC-B-G238-T4-2-07",
      "BIC-B-G238-T4-2-08",
      "BIC-B-G238-T4-2-09",
      "BIC-B-G238-T4-2-10",
      "BIC-B-G238-T4-2-11",
      "BIC-B-G238-T4-2-12",
      "BIC-B-G238-T4-2-13",
      "BIC-B-G238-T4-2-14",
      "BIC-B-G238-T4-2-15",
      "BIC-B-G238-T4-2-16",
      "BIC-B-G238-T4-2-17",
      "BIC-B-G238-T4-2-18",
      "BIC-B-G238-T4-2-19",
      "BIC-B-G238-T4-2-20",
      "BIC-B-G238-T4-2-21",
      "BIC-B-G238-T4-2-22",
      "BIC-B-G238-T4-2-23",
      "BIC-B-G238-T4-2-24",
      "BIC-B-G238-T4-2-25",
      "BIC-B-G238-T4-2-26",
      "BIC-B-G238-T4-2-27",
      "BIC-B-G238-T4-2-28",
      "BIC-B-G238-T4-2-29",
      "BIC-B-G238-T4-2-30",
      "BIC-B-G238-T4-2-31",
      "BIC-B-G238-T4-2-32",
      "BIC-B-G238-T4-2-33",
      "BIC-B-G238-T4-2-34",
      "BIC-B-G238-T4-2-35",
      "BIC-B-G238-T4-2-36",
      "BIC-B-G238-T4-2-37",
      "BIC-B-G238-T4-2-38",
      "BIC-B-G238-T4-2-39",
      "BIC-B-G238-T4-2-40",
      "BIC-B-G238-T4-2-41",
      "BIC-B-G238-T4-2-42",
      "BIC-B-G238-T4-2-43",
      "BIC-B-G238-T4-2-44",
      "BIC-B-G238-T4-2-45",
      "BIC-B-G238-T4-2-46",
      "BIC-B-G238-T4-2-47",
      "BIC-B-G238-T4-2-48",
      "BIC-B-G238-T4-2-49",
      "BIC-B-G238-T4-2-50",
      "BIC-B-G238-T4-2-51",
      "BIC-B-G238-T4-2-52",
      "BIC-B-G238-T4-2-53",
      "BIC-B-G238-T4-2-54"
    ],
    "relationship_ids": [],
    "analysis": "依据raw-brief.md的虚构材料，按analysis.md人工分析；生成器转换已审查模型。",
    "legend": "参考功能行不是实际部署；计划和未知不计已实现。本表不声明来源图视觉通过。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile bi-business-function-coverage --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile bi-business-function-coverage --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
