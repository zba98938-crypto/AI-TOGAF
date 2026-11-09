# 能力差距热力图

`profile_id`: capability-gap-heatmap；`artifact_id`: business-capability-map；主责：[togaf-strategy-capabilities](../../../togaf-strategy-capabilities/SKILL.md)。

来源：G211/fig5-1。

## 构图与定义状态

表示族：`heatmap`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "source_figure": "G211/fig5-1",
  "layout_notes": "颜色有评价维度和量表；未来不存在能力单独表示",
  "review_status": "source-located-awaiting-template-validation",
  "score_field": "score",
  "colors": {
    "1": "#f3c6c2",
    "2": "#ffe5b1",
    "3": "#bfe0c6",
    "4": "#98cba8"
  }
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：capability。关系类型：。

```json
{
  "entities": {
    "capability": [
      "definition",
      "dimension",
      "score",
      "scale",
      "target"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 颜色有评价维度和量表；未来不存在能力单独表示

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
      "id": "capability-gap-heatmap-0",
      "type": "capability",
      "name": "订单管理",
      "attributes": {
        "definition": "管理订单相关结果",
        "category": "核心",
        "dimension": "履约支持充分性",
        "score": 2,
        "scale": "虚构1至4级：缺失、临时、受控、优化",
        "target": 4
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-gap-heatmap-1",
      "type": "capability",
      "name": "库存管理",
      "attributes": {
        "definition": "管理库存相关结果",
        "category": "核心",
        "dimension": "履约支持充分性",
        "score": 3,
        "scale": "虚构1至4级：缺失、临时、受控、优化",
        "target": 4
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-gap-heatmap-2",
      "type": "capability",
      "name": "交付管理",
      "attributes": {
        "definition": "管理交付相关结果",
        "category": "核心",
        "dimension": "履约支持充分性",
        "score": 1,
        "scale": "虚构1至4级：缺失、临时、受控、优化",
        "target": 4
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-capability-gap-heatmap",
    "artifact_id": "business-capability-map",
    "profile_id": "capability-gap-heatmap",
    "title": "能力差距热力图／虚构案例",
    "entity_ids": [
      "capability-gap-heatmap-0",
      "capability-gap-heatmap-1",
      "capability-gap-heatmap-2"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile capability-gap-heatmap --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile capability-gap-heatmap --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
