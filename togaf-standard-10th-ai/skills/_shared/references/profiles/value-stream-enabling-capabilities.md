# 价值流阶段与使能能力

`profile_id`: value-stream-enabling-capabilities；`artifact_id`: value-stream-map；主责：[togaf-value-streams](../../../togaf-value-streams/SKILL.md)。

来源：G178/fig4-3。

## 构图与定义状态

表示族：`stage-map`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "source_figure": "G178/fig4-3",
  "layout_notes": "阶段横向有序；同一能力可支持多个阶段",
  "review_status": "source-located-awaiting-template-validation"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：capability, value_stage, value_stream。关系类型：enabled_by, precedes, traces_to。

```json
{
  "entities": {
    "value_stage": [
      "order",
      "entry_condition",
      "exit_condition",
      "value_item"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 阶段横向有序；同一能力可支持多个阶段

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
      "id": "value-stream-enabling-capabilities-stream",
      "type": "value_stream",
      "name": "获取零售商品",
      "attributes": {
        "beneficiary": "线上客户",
        "trigger": "客户需要商品",
        "outcome": "客户按承诺获得商品"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "value-stream-enabling-capabilities-stage1",
      "type": "value_stage",
      "name": "选择商品",
      "attributes": {
        "order": 1,
        "entry_condition": "客户确认需求",
        "exit_condition": "形成购物篮",
        "value_item": "适合需要的商品组合"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "value-stream-enabling-capabilities-stage2",
      "type": "value_stage",
      "name": "确认订单",
      "attributes": {
        "order": 2,
        "entry_condition": "已选择商品",
        "exit_condition": "有效订单已确认",
        "value_item": "可履行的购买承诺"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "value-stream-enabling-capabilities-stage3",
      "type": "value_stage",
      "name": "接收商品",
      "attributes": {
        "order": 3,
        "entry_condition": "已确认并发运",
        "exit_condition": "客户确认收货",
        "value_item": "可使用的商品"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "value-stream-enabling-capabilities-cap",
      "type": "capability",
      "name": "订单履约",
      "attributes": {
        "definition": "实现有效订单并按承诺交付",
        "level": 1,
        "dimension": "阶段支持充分性",
        "score": 2,
        "scale": "虚构1缺失2临时3受控4优化",
        "target": 4,
        "category": "核心"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "value-stream-enabling-capabilities-stream-stage1",
      "type": "traces_to",
      "source": "value-stream-enabling-capabilities-stream",
      "target": "value-stream-enabling-capabilities-stage1",
      "label": "价值流包含该阶段；非流程控制线",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "value-stream-enabling-capabilities-stream-stage2",
      "type": "traces_to",
      "source": "value-stream-enabling-capabilities-stream",
      "target": "value-stream-enabling-capabilities-stage2",
      "label": "价值流包含该阶段；非流程控制线",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "value-stream-enabling-capabilities-precedence2",
      "type": "precedes",
      "source": "value-stream-enabling-capabilities-stage1",
      "target": "value-stream-enabling-capabilities-stage2",
      "label": "客户价值阶段依次推进",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "value-stream-enabling-capabilities-stream-stage3",
      "type": "traces_to",
      "source": "value-stream-enabling-capabilities-stream",
      "target": "value-stream-enabling-capabilities-stage3",
      "label": "价值流包含该阶段；非流程控制线",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "value-stream-enabling-capabilities-precedence3",
      "type": "precedes",
      "source": "value-stream-enabling-capabilities-stage2",
      "target": "value-stream-enabling-capabilities-stage3",
      "label": "客户价值阶段依次推进",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "value-stream-enabling-capabilities-enable0",
      "type": "enabled_by",
      "source": "value-stream-enabling-capabilities-stage1",
      "target": "value-stream-enabling-capabilities-cap",
      "label": "阶段由订单履约能力使能",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "value-stream-enabling-capabilities-enable1",
      "type": "enabled_by",
      "source": "value-stream-enabling-capabilities-stage2",
      "target": "value-stream-enabling-capabilities-cap",
      "label": "阶段由订单履约能力使能",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "value-stream-enabling-capabilities-enable2",
      "type": "enabled_by",
      "source": "value-stream-enabling-capabilities-stage3",
      "target": "value-stream-enabling-capabilities-cap",
      "label": "阶段由订单履约能力使能",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-value-stream-enabling-capabilities",
    "artifact_id": "value-stream-map",
    "profile_id": "value-stream-enabling-capabilities",
    "title": "价值流阶段与使能能力／虚构案例",
    "entity_ids": [
      "value-stream-enabling-capabilities-stream",
      "value-stream-enabling-capabilities-stage1",
      "value-stream-enabling-capabilities-stage2",
      "value-stream-enabling-capabilities-stage3",
      "value-stream-enabling-capabilities-cap"
    ],
    "relationship_ids": [
      "value-stream-enabling-capabilities-stream-stage1",
      "value-stream-enabling-capabilities-stream-stage2",
      "value-stream-enabling-capabilities-precedence2",
      "value-stream-enabling-capabilities-stream-stage3",
      "value-stream-enabling-capabilities-precedence3",
      "value-stream-enabling-capabilities-enable0",
      "value-stream-enabling-capabilities-enable1",
      "value-stream-enabling-capabilities-enable2"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile value-stream-enabling-capabilities --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile value-stream-enabling-capabilities --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
