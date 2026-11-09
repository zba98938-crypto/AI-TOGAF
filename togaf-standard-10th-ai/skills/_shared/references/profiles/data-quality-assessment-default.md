# 数据质量评估

`profile_id`: data-quality-assessment-default；`artifact_id`: data-quality-assessment；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G152 §5.4；G234 §4.2。

## 构图与定义状态

表示族：`assessment`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：data_quality_measure。关系类型：。

```json
{
  "entities": {
    "data_quality_measure": [
      "dataset",
      "dimension",
      "metric",
      "unit",
      "threshold",
      "owner",
      "evidence_period"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 不同质量维度不能无依据地加总成一个精确分数
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

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
      "id": "data-quality-assessment-default-record",
      "type": "data_quality_measure",
      "name": "数据质量评估：订单范围记录",
      "attributes": {
        "dataset": "虚构在线订单集",
        "dimension": "完整性",
        "metric": "已确认订单中包含履约必填项的比例",
        "unit": "百分比",
        "threshold": "示例期望100%，需业务方确认",
        "owner": "虚构业务负责人",
        "evidence_period": "2026年10月虚构抽样"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-data-quality-assessment-default",
    "artifact_id": "data-quality-assessment",
    "profile_id": "data-quality-assessment-default",
    "title": "数据质量评估／虚构案例",
    "entity_ids": [
      "data-quality-assessment-default-record"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile data-quality-assessment-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile data-quality-assessment-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
