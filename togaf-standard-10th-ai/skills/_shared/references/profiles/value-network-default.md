# 价值网络

`profile_id`: value-network-default；`artifact_id`: value-network；主责：[togaf-value-streams](../../../togaf-value-streams/SKILL.md)。

来源：G178/figA-2。

## 构图与定义状态

表示族：`network`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：value_network_actor。关系类型：exchanges_value。

```json
{
  "entities": {
    "value_network_actor": [
      "role",
      "beneficiary"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 价值网络不是顺序价值流，连接不默认双向，不把信息发送自动视为价值
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
      "id": "value-network-default-customer",
      "type": "value_network_actor",
      "name": "线上客户",
      "attributes": {
        "role": "价值需求与付款方",
        "beneficiary": "获得可用商品和可靠交付"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "value-network-default-retailer",
      "type": "value_network_actor",
      "name": "零售商",
      "attributes": {
        "role": "商品组合与履约承诺方",
        "beneficiary": "获得商品销售收入"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "value-network-default-carrier",
      "type": "value_network_actor",
      "name": "承运商",
      "attributes": {
        "role": "配送服务方",
        "beneficiary": "获得明确配送服务费"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "value-network-default-goods",
      "type": "exchanges_value",
      "source": "value-network-default-retailer",
      "target": "value-network-default-customer",
      "label": "商品和可跟踪交付",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "value_item": "商品和可跟踪交付",
        "conditions": "订单有效且承诺已确认",
        "tangible": true
      }
    },
    {
      "id": "value-network-default-payment",
      "type": "exchanges_value",
      "source": "value-network-default-customer",
      "target": "value-network-default-retailer",
      "label": "商品对价",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "value_item": "商品对价",
        "conditions": "依已确认销售条款",
        "tangible": true
      }
    },
    {
      "id": "value-network-default-delivery",
      "type": "exchanges_value",
      "source": "value-network-default-carrier",
      "target": "value-network-default-retailer",
      "label": "履行配送服务",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "value_item": "履行配送服务",
        "conditions": "受托订单范围内",
        "tangible": true
      }
    },
    {
      "id": "value-network-default-fee",
      "type": "exchanges_value",
      "source": "value-network-default-retailer",
      "target": "value-network-default-carrier",
      "label": "配送服务费",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "value_item": "配送服务费",
        "conditions": "依可验证服务成果结算",
        "tangible": true
      }
    }
  ],
  "view": {
    "id": "v-value-network-default",
    "artifact_id": "value-network",
    "profile_id": "value-network-default",
    "title": "价值网络／虚构案例",
    "entity_ids": [
      "value-network-default-customer",
      "value-network-default-retailer",
      "value-network-default-carrier"
    ],
    "relationship_ids": [
      "value-network-default-goods",
      "value-network-default-payment",
      "value-network-default-delivery",
      "value-network-default-fee"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile value-network-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile value-network-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
