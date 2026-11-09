# 数字技术采用定位

`profile_id`: digital-adoption-position-default；`artifact_id`: digital-adoption-position；主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G212 §5.1；图5-2。

## 构图与定义状态

表示族：`quadrant`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。",
  "x_axis": "普及度 Ubiquity（采用覆盖程度）",
  "y_axis": "速度 Velocity（采用速度）",
  "quadrant_labels": {
    "top-left": "先锋式 Avant-Garde",
    "top-right": "大爆炸式 Big-Bang",
    "bottom-left": "谨慎式 Discreet",
    "bottom-right": "凝聚式 Cohesive"
  }
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：adoption_option。关系类型：。

```json
{
  "entities": {
    "adoption_option": [
      "ubiquity",
      "velocity",
      "rationale",
      "scope",
      "tradeoffs"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- ABCD 不是由低到高的优劣或成熟度等级
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
      "id": "digital-adoption-position-default-A",
      "type": "adoption_option",
      "name": "先锋式",
      "attributes": {
        "ubiquity": "低",
        "velocity": "高",
        "rationale": "按本企业范围速度与资源权衡；字母无优劣",
        "scope": "在线订单业务范围",
        "tradeoffs": "广度速度与风险资源之间的取舍",
        "quadrant": "top-left"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-adoption-position-default-B",
      "type": "adoption_option",
      "name": "大爆炸式",
      "attributes": {
        "ubiquity": "高",
        "velocity": "高",
        "rationale": "按本企业范围速度与资源权衡；字母无优劣",
        "scope": "在线订单业务范围",
        "tradeoffs": "广度速度与风险资源之间的取舍",
        "quadrant": "top-right"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-adoption-position-default-C",
      "type": "adoption_option",
      "name": "凝聚式",
      "attributes": {
        "ubiquity": "高",
        "velocity": "低",
        "rationale": "按本企业范围速度与资源权衡；字母无优劣",
        "scope": "在线订单业务范围",
        "tradeoffs": "广度速度与风险资源之间的取舍",
        "quadrant": "bottom-right"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-adoption-position-default-D",
      "type": "adoption_option",
      "name": "谨慎式",
      "attributes": {
        "ubiquity": "低",
        "velocity": "低",
        "rationale": "按本企业范围速度与资源权衡；字母无优劣",
        "scope": "在线订单业务范围",
        "tradeoffs": "广度速度与风险资源之间的取舍",
        "quadrant": "bottom-left"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-digital-adoption-position-default",
    "artifact_id": "digital-adoption-position",
    "profile_id": "digital-adoption-position-default",
    "title": "数字技术采用定位／虚构案例",
    "entity_ids": [
      "digital-adoption-position-default-A",
      "digital-adoption-position-default-B",
      "digital-adoption-position-default-C",
      "digital-adoption-position-default-D"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile digital-adoption-position-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile digital-adoption-position-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
