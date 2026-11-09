# 能力使用与修改信息

`profile_id`: information-capability-use-modify；`artifact_id`: information-map；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G190/fig4-1。

## 构图与定义状态

表示族：`network`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "source_figure": "G190/fig4-1",
  "layout_notes": "能力到信息为修改；信息到能力为使用，图例需保留",
  "review_status": "source-located-awaiting-template-validation"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：capability, information。关系类型：modifies_information, uses_information。

```json
{
  "entities": {
    "capability": [
      "definition"
    ],
    "information": [
      "definition"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 能力到信息为修改；信息到能力为使用，图例需保留

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
      "id": "information-capability-use-modify-cap",
      "type": "capability",
      "name": "订单管理",
      "attributes": {
        "definition": "建立并维护有效订单状态"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "information-capability-use-modify-order",
      "type": "information",
      "name": "订单",
      "attributes": {
        "definition": "客户与企业间的商品和履约承诺"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "information-capability-use-modify-read",
      "type": "uses_information",
      "source": "information-capability-use-modify-cap",
      "target": "information-capability-use-modify-order",
      "label": "使用订单信息进行确认",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "information-capability-use-modify-write",
      "type": "modifies_information",
      "source": "information-capability-use-modify-cap",
      "target": "information-capability-use-modify-order",
      "label": "修改订单状态；不等同于只读使用",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-information-capability-use-modify",
    "artifact_id": "information-map",
    "profile_id": "information-capability-use-modify",
    "title": "能力使用与修改信息／虚构案例",
    "entity_ids": [
      "information-capability-use-modify-cap",
      "information-capability-use-modify-order"
    ],
    "relationship_ids": [
      "information-capability-use-modify-read",
      "information-capability-use-modify-write"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile information-capability-use-modify --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile information-capability-use-modify --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
