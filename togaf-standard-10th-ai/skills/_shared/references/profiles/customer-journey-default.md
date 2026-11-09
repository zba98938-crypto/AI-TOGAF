# 客户旅程

`profile_id`: customer-journey-default；`artifact_id`: customer-journey；主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G20F §5.2.1、§5.3.1、§5.5。

## 构图与定义状态

表示族：`stage-map`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：customer_journey_stage, value_stream。关系类型：has_journey_stage, precedes。

```json
{
  "entities": {
    "customer_journey_stage": [
      "order",
      "actor",
      "touchpoint",
      "experience",
      "pain_point",
      "outcome"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 客户旅程不是内部流程图，体验陈述需证据
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
      "id": "customer-journey-default-stream",
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
      "id": "customer-journey-default-stage1",
      "type": "customer_journey_stage",
      "name": "选择商品",
      "attributes": {
        "order": 1,
        "entry_condition": "客户确认需求",
        "exit_condition": "形成购物篮",
        "value_item": "适合需要的商品组合",
        "actor": "线上客户",
        "touchpoint": "商品页面",
        "experience": "理解当前进展与下一步",
        "pain_point": "本例假设存在状态不清，需用户研究验证",
        "outcome": "适合需要的商品组合"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "customer-journey-default-stage2",
      "type": "customer_journey_stage",
      "name": "确认订单",
      "attributes": {
        "order": 2,
        "entry_condition": "已选择商品",
        "exit_condition": "有效订单已确认",
        "value_item": "可履行的购买承诺",
        "actor": "线上客户",
        "touchpoint": "结算页面",
        "experience": "理解当前进展与下一步",
        "pain_point": "本例假设存在状态不清，需用户研究验证",
        "outcome": "可履行的购买承诺"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "customer-journey-default-stage3",
      "type": "customer_journey_stage",
      "name": "接收商品",
      "attributes": {
        "order": 3,
        "entry_condition": "已确认并发运",
        "exit_condition": "客户确认收货",
        "value_item": "可使用的商品",
        "actor": "线上客户",
        "touchpoint": "配送通知",
        "experience": "理解当前进展与下一步",
        "pain_point": "本例假设存在状态不清，需用户研究验证",
        "outcome": "可使用的商品"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "customer-journey-default-stream-stage1",
      "type": "has_journey_stage",
      "source": "customer-journey-default-stream",
      "target": "customer-journey-default-stage1",
      "label": "价值流包含该阶段；非流程控制线",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "customer-journey-default-stream-stage2",
      "type": "has_journey_stage",
      "source": "customer-journey-default-stream",
      "target": "customer-journey-default-stage2",
      "label": "价值流包含该阶段；非流程控制线",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "customer-journey-default-precedence2",
      "type": "precedes",
      "source": "customer-journey-default-stage1",
      "target": "customer-journey-default-stage2",
      "label": "客户体验阶段的先后",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "customer-journey-default-stream-stage3",
      "type": "has_journey_stage",
      "source": "customer-journey-default-stream",
      "target": "customer-journey-default-stage3",
      "label": "价值流包含该阶段；非流程控制线",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "customer-journey-default-precedence3",
      "type": "precedes",
      "source": "customer-journey-default-stage2",
      "target": "customer-journey-default-stage3",
      "label": "客户体验阶段的先后",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-customer-journey-default",
    "artifact_id": "customer-journey",
    "profile_id": "customer-journey-default",
    "title": "客户旅程／虚构案例",
    "entity_ids": [
      "customer-journey-default-stream",
      "customer-journey-default-stage1",
      "customer-journey-default-stage2",
      "customer-journey-default-stage3"
    ],
    "relationship_ids": [
      "customer-journey-default-stream-stage1",
      "customer-journey-default-stream-stage2",
      "customer-journey-default-precedence2",
      "customer-journey-default-stream-stage3",
      "customer-journey-default-precedence3"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile customer-journey-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile customer-journey-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
