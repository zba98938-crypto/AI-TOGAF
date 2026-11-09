# 价值网络

ID：`value-network`。主责：[togaf-value-streams](../../../togaf-value-streams/SKILL.md)。

来源：G178/figA-2。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

判断多个参与者如何交换有形或无形价值以及网络依赖

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 判断多个参与者如何交换有形或无形价值以及网络依赖
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- role
- value_exchange
- beneficiary

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：value_network_actor。

```json
{
  "value_network_actor": [
    "role",
    "beneficiary"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "role": {
    "meaning": "承担职责的角色",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "value_exchange": {
    "meaning": "在本工作产品范围中明确定义的 value_exchange 属性",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "beneficiary": {
    "meaning": "在本工作产品范围中明确定义的 beneficiary 属性",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "conditions": {
    "meaning": "关系或规则成立的条件",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `exchanges_value` | value_network_actor → value_network_actor | 有方向且带条件的价值交换；需明确价值项与对价，不能默认双向 |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 确定网络边界和受益者
2. 识别参与者角色
3. 逐方向定义价值交换及对价
4. 识别依赖与失衡
5. 核实每条交换的依据

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 价值网络不是顺序价值流，连接不默认双向，不把信息发送自动视为价值
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 价值网络不是顺序价值流，连接不默认双向，不把信息发送自动视为价值


## 视图和交付物

- [价值网络](../profiles/value-network-default.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)
- [capability-assessment](../deliverables/capability-assessment.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「价值网络」给出：价值网络不是顺序价值流，连接不默认双向，不把信息发送自动视为价值",
    "expected": "missing-evidence",
    "why": "价值网络不是顺序价值流，连接不默认双向，不把信息发送自动视为价值"
  },
  "modification_example": {
    "change": "在「价值网络」的范围内新增或修改一项，检查下游是否随之变化",
    "expected": "受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用"
  }
}
```

## 可编辑示例与调用



以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

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

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact value-network --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
