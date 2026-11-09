# ABCD 采用定位象限

`profile_id`: dtra-adoption-quadrant；`artifact_id`: digital-adoption-position；主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G212/fig5-2。

## 构图与定义状态

表示族：`quadrant`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "source_figure": "G212/fig5-2",
  "layout_notes": "横轴普及度纵轴速度；四种方式不表示优劣等级",
  "review_status": "source-located-awaiting-template-validation",
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
      "rationale"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 横轴普及度纵轴速度；四种方式不表示优劣等级

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
      "id": "dtra-adoption-quadrant-A",
      "type": "adoption_option",
      "name": "先锋式",
      "attributes": {
        "ubiquity": "低",
        "velocity": "高",
        "rationale": "按本企业范围速度与资源权衡；字母无优劣",
        "quadrant": "top-left",
        "scope": "在线订单业务范围",
        "tradeoffs": "广度速度与风险资源之间的取舍"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "dtra-adoption-quadrant-B",
      "type": "adoption_option",
      "name": "大爆炸式",
      "attributes": {
        "ubiquity": "高",
        "velocity": "高",
        "rationale": "按本企业范围速度与资源权衡；字母无优劣",
        "quadrant": "top-right",
        "scope": "在线订单业务范围",
        "tradeoffs": "广度速度与风险资源之间的取舍"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "dtra-adoption-quadrant-C",
      "type": "adoption_option",
      "name": "凝聚式",
      "attributes": {
        "ubiquity": "高",
        "velocity": "低",
        "rationale": "按本企业范围速度与资源权衡；字母无优劣",
        "quadrant": "bottom-right",
        "scope": "在线订单业务范围",
        "tradeoffs": "广度速度与风险资源之间的取舍"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "dtra-adoption-quadrant-D",
      "type": "adoption_option",
      "name": "谨慎式",
      "attributes": {
        "ubiquity": "低",
        "velocity": "低",
        "rationale": "按本企业范围速度与资源权衡；字母无优劣",
        "quadrant": "bottom-left",
        "scope": "在线订单业务范围",
        "tradeoffs": "广度速度与风险资源之间的取舍"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-dtra-adoption-quadrant",
    "artifact_id": "digital-adoption-position",
    "profile_id": "dtra-adoption-quadrant",
    "title": "ABCD 采用定位象限／虚构案例",
    "entity_ids": [
      "dtra-adoption-quadrant-A",
      "dtra-adoption-quadrant-B",
      "dtra-adoption-quadrant-C",
      "dtra-adoption-quadrant-D"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile dtra-adoption-quadrant --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile dtra-adoption-quadrant --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
