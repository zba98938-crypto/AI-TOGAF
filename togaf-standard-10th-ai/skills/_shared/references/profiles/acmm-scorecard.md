# ACMM 证据评分卡

`profile_id`: acmm-scorecard；`artifact_id`: architecture-maturity-scorecard；主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G203 §2.2–2.3。

## 构图与定义状态

表示族：`assessment`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "source_figure": null,
  "layout_notes": "分别报告加权等级与达成比例，不能自造权重",
  "review_status": "source-located-awaiting-template-validation"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：maturity_observation。关系类型：。

```json
{
  "entities": {
    "maturity_observation": [
      "element",
      "level",
      "evidence"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 分别报告加权等级与达成比例，不能自造权重

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构星河零售验收示例；全部对象为假设，未声称事实、批准或来源图复刻。",
  "sources": [
    {
      "id": "example-source",
      "kind": "example",
      "description": "虚构业务案例：在线订单、仓库发运及客户通知"
    }
  ],
  "entities": [
    {
      "id": "acmm-scorecard-record",
      "type": "maturity_observation",
      "name": "ACMM 证据评分卡：订单范围记录",
      "attributes": {
        "element": "架构治理",
        "level": 2,
        "evidence": "虚构场景说明，非实测证据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-acmm-scorecard",
    "artifact_id": "architecture-maturity-scorecard",
    "profile_id": "acmm-scorecard",
    "title": "ACMM 证据评分卡／虚构案例",
    "entity_ids": [
      "acmm-scorecard-record"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile acmm-scorecard --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile acmm-scorecard --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
