# 阶段边界报告

`profile_id`: project-stage-closure-record-stage；`artifact_id`: project-stage-closure-record；主责：[togaf-artifact-review](../../../togaf-artifact-review/SKILL.md)。

来源：G188 §3.5.1–3.6.3。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-addenda。

{
  "id": "project-stage-closure-record-stage",
  "version": "2.1-addenda",
  "source_verified": false,
  "layout_notes": "源正文方法的项目字段表；没有原图复刻声明。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:closure_record。关系类型：。

```json
{
  "entities": {
    "guide:closure_record": [
      "closure_kind",
      "closure_reason",
      "products",
      "performance",
      "risks_issues",
      "handover",
      "next_stage",
      "authority",
      "decision",
      "evidence_refs",
      "follow_up"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 阶段产品验收、边界决策、下一阶段授权是不同事实
- 商业论证失效可以提前终止，不能假装全部产品成功交付
- 计划/实际偏差不自动证明超过未给出的容差

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构海岚配送架构项目；所有访谈、估算、任务与批准资料仅用于方法演示。",
  "sources": [
    {
      "id": "src-project-stage-closure-record-stage",
      "kind": "example",
      "description": "虚构海岚配送架构项目；所有访谈、估算、任务与批准资料仅用于方法演示。 材料组 stage-close",
      "locator": "examples/addenda/project-management/raw-business-materials.json#stage-close"
    }
  ],
  "entities": [
    {
      "id": "project-stage-closure-record-stage-1",
      "type": "guide:closure_record",
      "name": "流程分析阶段",
      "attributes": {
        "closure_kind": "stage-boundary",
        "closure_reason": "completed-proposed",
        "products": [
          {
            "id": "DEL-FLOW",
            "accepted": true
          },
          {
            "id": "DEL-DESC",
            "accepted": false
          }
        ],
        "performance": {
          "planned_days": 10,
          "actual_days": 11,
          "planned_hours": 60,
          "actual_hours": 68,
          "tolerances": "unknown"
        },
        "risks_issues": "新增门店增加后续工作；DEL-DESC未接受",
        "handover": "流程图可供内部建模；说明表缺口未关闭",
        "next_stage": "建模计划草拟，尚未批准",
        "authority": "项目监督机构/发起人",
        "decision": "pending",
        "evidence_refs": [
          "SC-01",
          "SC-02"
        ],
        "follow_up": "修正说明表并取得接受；确认容差与下一阶段计划，不能自行宣布完成"
      },
      "evidence": [
        "src-project-stage-closure-record-stage"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-project-stage-closure-record-stage",
    "artifact_id": "project-stage-closure-record",
    "profile_id": "project-stage-closure-record-stage",
    "title": "阶段边界报告",
    "entity_ids": [
      "project-stage-closure-record-stage-1"
    ],
    "relationship_ids": [],
    "analysis": "阶段实际比计划多1天8小时，但容差未知不能断言越权；未接受说明表阻断完成型收尾。",
    "legend": "虚构记录；计划、实绩、建议、授权和批准分别表述。空缺不等于零或已接受。"
  },
  "raw_input_group": "stage-close"
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile project-stage-closure-record-stage --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile project-stage-closure-record-stage --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
