# 信息聚合组合泛化

`profile_id`: information-aggregation-generalization；`artifact_id`: information-map；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G190/figA-1。

## 构图与定义状态

表示族：`er`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "source_figure": "G190/figA-1",
  "layout_notes": "关联、聚合、组合和泛化不可仅以相同箭头代替",
  "review_status": "source-located-awaiting-template-validation"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：information。关系类型：aggregation, composition, generalization。

```json
{
  "entities": {
    "information": [
      "definition"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 关联、聚合、组合和泛化不可仅以相同箭头代替

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
      "id": "information-aggregation-generalization-customer",
      "type": "information",
      "name": "客户",
      "attributes": {
        "definition": "与企业形成业务关系的主体"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "information-aggregation-generalization-person",
      "type": "information",
      "name": "自然人客户",
      "attributes": {
        "definition": "作为自然人参与的客户"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "information-aggregation-generalization-order",
      "type": "information",
      "name": "订单",
      "attributes": {
        "definition": "包含商品和履约承诺的业务对象"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "information-aggregation-generalization-line",
      "type": "information",
      "name": "订单明细",
      "attributes": {
        "definition": "只在所属订单中存在的商品条目"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "information-aggregation-generalization-general",
      "type": "generalization",
      "source": "information-aggregation-generalization-person",
      "target": "information-aggregation-generalization-customer",
      "label": "自然人客户是客户的特化",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "information-aggregation-generalization-composition",
      "type": "composition",
      "source": "information-aggregation-generalization-order",
      "target": "information-aggregation-generalization-line",
      "label": "订单独占组成订单明细",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "information-aggregation-generalization-aggregation",
      "type": "aggregation",
      "source": "information-aggregation-generalization-customer",
      "target": "information-aggregation-generalization-order",
      "label": "客户聚合与其关联的订单；订单有独立生命周期",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-information-aggregation-generalization",
    "artifact_id": "information-map",
    "profile_id": "information-aggregation-generalization",
    "title": "信息聚合组合泛化／虚构案例",
    "entity_ids": [
      "information-aggregation-generalization-customer",
      "information-aggregation-generalization-person",
      "information-aggregation-generalization-order",
      "information-aggregation-generalization-line"
    ],
    "relationship_ids": [
      "information-aggregation-generalization-general",
      "information-aggregation-generalization-composition",
      "information-aggregation-generalization-aggregation"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile information-aggregation-generalization --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile information-aggregation-generalization --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
