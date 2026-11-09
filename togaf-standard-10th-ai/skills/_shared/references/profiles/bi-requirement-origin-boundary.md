# BI架构需求及来源边界

`profile_id`: bi-requirement-origin-boundary；`artifact_id`: bi-requirements-profile；主责：[togaf-requirements](../../../togaf-requirements/SKILL.md)。

来源：G238 §4.4（特别是本地补写示例说明）。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-extension-1。

{
  "id": "bi-requirement-origin-boundary",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "完整字段及关系表；原图结构复刻由独立图形规范验证，本表不冒领。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:bi_requirement_provenance。关系类型：。

```json
{
  "entities": {
    "guide:bi_requirement_provenance": [
      "statement",
      "function",
      "requirement_origin",
      "origin_locator",
      "official_requirement_id",
      "verification",
      "completeness_claim",
      "validation_criteria",
      "companion_sheet"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 本地16例不得标原文逐条需求
- 缺配套源时official_requirement_id保持unknown
- 不宣称完整需求数量或全集覆盖
- 来源冲突明确登记

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构完整案例；表格伴随语义不冒称原图视觉通过。",
  "raw_input": "examples/addenda/existing-extensions/bi-requirement-origin-boundary/raw-brief.md",
  "analysis_path": "examples/addenda/existing-extensions/bi-requirement-origin-boundary/analysis.md",
  "sources": [
    {
      "id": "case-source",
      "kind": "example",
      "description": "虚构业务方提出审计血缘需求R1。分析师另看到中文G238的R-13漂移示例；该节明确16例由译者按功能补写，完整原文需求另附电子表格且本地未找到。因此R1属项目需求、R-13属本地示例，均不能用官方需求ID或声称需求全集完整。",
      "locator": "raw-brief.md"
    }
  ],
  "entities": [
    {
      "id": "BIR-01",
      "type": "guide:bi_requirement_provenance",
      "name": "借阅审计血缘需求",
      "attributes": {
        "statement": "系统应记录借阅审计数据从来源到报表的路径，向审计人员提供追溯。",
        "function": "血缘与审计",
        "requirement_origin": "project-user-input",
        "origin_locator": "本例需求访谈R1",
        "official_requirement_id": "unknown",
        "verification": "project-rule-reviewed",
        "completeness_claim": "project-scope-only；非G238需求全集",
        "validation_criteria": "清晰/无工具/原子/唯一/可验证，测试细节另行",
        "companion_sheet": "missing-locally"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "BIR-02",
      "type": "guide:bi_requirement_provenance",
      "name": "译者示例R-13的使用边界",
      "attributes": {
        "statement": "系统应监控数据科学模型漂移并触发告警，向模型负责人提供趋势视图。",
        "function": "业务使用监控",
        "requirement_origin": "local-translation-added-example",
        "origin_locator": "G238中文§4.4 R-13；正文说明示例非原文逐条照录",
        "official_requirement_id": "unknown",
        "verification": "not-original-spreadsheet-verified",
        "completeness_claim": "illustration-only；不能冒充官方全部需求",
        "validation_criteria": "作为候选需求启发；模型/阈值/数据需另取证",
        "companion_sheet": "missing-locally"
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
    "id": "v-bi-requirement-origin-boundary",
    "artifact_id": "bi-requirements-profile",
    "profile_id": "bi-requirement-origin-boundary",
    "title": "BI架构需求及来源边界",
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
      "BIR-01",
      "BIR-02"
    ],
    "relationship_ids": [],
    "analysis": "见本例analysis.md；模型为依据raw-brief.md形成的人工候选分析，不是真实批准。",
    "legend": "表格表达正文操作语义，不声称原图复刻。未知显式保留，ID稳定。",
    "allow_mixed_evolution": true
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile bi-requirement-origin-boundary --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile bi-requirement-origin-boundary --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
