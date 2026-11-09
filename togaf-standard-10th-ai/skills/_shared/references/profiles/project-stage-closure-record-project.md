# 项目收尾建议

`profile_id`: project-stage-closure-record-project；`artifact_id`: project-stage-closure-record；主责：[togaf-artifact-review](../../../togaf-artifact-review/SKILL.md)。

来源：G188 §3.5.1–3.6.3。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-addenda。

{
  "id": "project-stage-closure-record-project",
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
      "id": "src-project-stage-closure-record-project",
      "kind": "example",
      "description": "虚构海岚配送架构项目；所有访谈、估算、任务与批准资料仅用于方法演示。 材料组 project-close",
      "locator": "examples/addenda/project-management/raw-business-materials.json#project-close"
    }
  ],
  "entities": [
    {
      "id": "project-stage-closure-record-project-1",
      "type": "guide:closure_record",
      "name": "门店合并架构终止",
      "attributes": {
        "closure_kind": "project-closure",
        "closure_reason": "terminated-business-case-invalid",
        "products": [
          {
            "id": "DEL-INTERFACE-PART",
            "accepted": false,
            "disposition": "交PMO保存为部分成果"
          },
          {
            "id": "TARGET-CANDIDATE",
            "accepted": false,
            "disposition": "撤销候选，不计成功交付"
          }
        ],
        "performance": {
          "planned_outcome": "合并目标架构",
          "actual_outcome": "部分接口分析",
          "benefits": "未实现，不以完成统计代替"
        },
        "risks_issues": "R-DATA转运营负责人跟踪",
        "handover": "PMO保存部分分析；运营承接数据风险",
        "next_stage": "not-applicable",
        "authority": "执行发起人",
        "decision": "termination-recommended; approval-pending",
        "evidence_refs": [
          "PC-01",
          "PC-02"
        ],
        "follow_up": "取得正式收尾接受后释放资源；记录未完内容与风险去向"
      },
      "evidence": [
        "src-project-stage-closure-record-project"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-project-stage-closure-record-project",
    "artifact_id": "project-stage-closure-record",
    "profile_id": "project-stage-closure-record-project",
    "title": "项目收尾建议",
    "entity_ids": [
      "project-stage-closure-record-project-1"
    ],
    "relationship_ids": [],
    "analysis": "商业论证失效允许提出提前终止；不要求把所有未完成产品虚假标已接受，但必须明确去向、风险移交与授权。",
    "legend": "虚构记录；计划、实绩、建议、授权和批准分别表述。空缺不等于零或已接受。"
  },
  "raw_input_group": "project-close"
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile project-stage-closure-record-project --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile project-stage-closure-record-project --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
