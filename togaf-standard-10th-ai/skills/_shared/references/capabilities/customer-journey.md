# 客户旅程

ID：`customer-journey`。主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G20F §5.2.1、§5.3.1、§5.5。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

客户如何经历服务并取得价值？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 客户如何经历服务并取得价值？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- actor
- goal
- touchpoint

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：customer_journey_stage, journey_stage, value_stream。

```json
{
  "customer_journey_stage": [
    "order",
    "actor",
    "touchpoint",
    "experience",
    "pain_point",
    "outcome"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "actor": {
    "meaning": "执行活动的主体",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "goal": {
    "meaning": "业务目标引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "touchpoint": {
    "meaning": "客户与服务交互触点",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "experience": {
    "meaning": "观察或期望体验",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "pain_point": {
    "meaning": "有证据的体验痛点",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "outcome": {
    "meaning": "业务或客户成果",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "order": {
    "meaning": "明确次序号",
    "value_rule": "保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `has_journey_stage` | customer_persona,value_stream → customer_journey_stage | 画像或旅程对应体验阶段 |
| `precedes` | value_stage,customer_journey_stage → value_stage,customer_journey_stage | 同一价值流或客户旅程内阶段的先后；旅程阶段的先后是体验次序，不是流程控制流，也不跨价值流与旅程连接。 |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 确定客户语境与目标
2. 识别触点和体验阶段
3. 记录证据痛点与期望
4. 连接业务运营和改进

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 客户旅程不是内部流程图，体验陈述需证据
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 客户旅程不是内部流程图，体验陈述需证据


## 视图和交付物

- [客户旅程](../profiles/customer-journey-default.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「客户旅程」给出：客户旅程不是内部流程图，体验陈述需证据",
    "expected": "missing-evidence",
    "why": "客户旅程不是内部流程图，体验陈述需证据"
  },
  "modification_example": {
    "change": "在「客户旅程」的范围内新增或修改一项，检查下游是否随之变化",
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

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact customer-journey --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
