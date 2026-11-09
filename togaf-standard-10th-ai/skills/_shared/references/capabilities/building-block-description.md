# 构建块描述

ID：`building-block-description`。主责：[togaf-gap-solutions](../../../togaf-gap-solutions/SKILL.md)。

来源：G248 §2–3；G21H §2产品架构定义、§5.3。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

构建块定义和选择怎样追溯到需求与实现？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 构建块定义和选择怎样追溯到需求与实现？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- definition
- abstraction
- service

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：abb, goal, guide:product_function, guide:product_component, guide:product_interface, sbb, requirement。

```json
{
  "abb": [
    "definition",
    "abstraction",
    "service",
    "requirements",
    "realization",
    "owner"
  ],
  "guide:product_function": [
    "product",
    "requirement",
    "operating_capability",
    "version",
    "evidence_detail"
  ],
  "guide:product_component": [
    "product",
    "component_role",
    "technical_component",
    "version",
    "evidence_detail"
  ],
  "guide:product_interface": [
    "product",
    "sender_ref",
    "receiver_ref",
    "operation",
    "request",
    "response",
    "security",
    "version",
    "evidence_detail"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "definition": {
    "meaning": "业务含义和排除边界",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "abstraction": {
    "meaning": "语境、概念、逻辑或物理层次",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "service": {
    "meaning": "服务对象引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "requirements": {
    "meaning": "架构要求引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "realization": {
    "meaning": "构建块的实现关系与候选",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "owner": {
    "meaning": "对对象负责的责任方",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |
| `guide:allocates_function` | guide:product_function → guide:product_component | 产品功能分配到组件实现；非流程先后 |
| `guide:interface_sender` | guide:product_interface → guide:product_component | 接口记录指定发送方组件；非该有向边本身作为数据流 |
| `guide:interface_receiver` | guide:product_interface → guide:product_component | 接口记录指定接收方组件；真实请求方向由sender/receiver二者共同定义 |
| `realizes` | function,outcome,sbb,technology → abb,business_service,goal,technology_service | 实现规定的服务、构建块或目标；成果到目标表示达成，不表示目标导致成果。 |

## 分析步骤

1. 描述所需架构服务与边界
2. 区分ABB和SBB
3. 比较候选实现
4. 记录要求、接口与选择依据

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- ABB不是一个指定技术产品，SBB不能仅按图中的相邻位置推断实现
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- ABB不是一个指定技术产品，SBB不能仅按图中的相邻位置推断实现


## 视图和交付物

- [构建块描述](../profiles/building-block-description-default.md)
- [构建块内容元模型](../profiles/building-block-content-model.md)
- [产品功能、组件与接口追溯](../profiles/product-function-component-interface.md)

- [architecture-roadmaps](../deliverables/architecture-roadmaps.md)
- [solution-building-blocks](../deliverables/solution-building-blocks.md)
- [architecture-building-blocks](../deliverables/architecture-building-blocks.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「构建块描述」给出：ABB不是一个指定技术产品，SBB不能仅按图中的相邻位置推断实现",
    "expected": "missing-evidence",
    "why": "ABB不是一个指定技术产品，SBB不能仅按图中的相邻位置推断实现"
  },
  "modification_example": {
    "change": "在「构建块描述」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "building-block-description-default-record",
      "type": "abb",
      "name": "构建块描述：订单范围记录",
      "attributes": {
        "definition": "构建块描述的虚构零售企业示例",
        "abstraction": "逻辑",
        "service": "虚构订单案例中需验证的服务对象引用",
        "requirements": "虚构订单案例中需验证的架构要求引用",
        "realization": "候选SBB方案，尚未选定",
        "owner": "虚构业务负责人"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "building-block-description-default-target",
      "type": "goal",
      "name": "可靠履约",
      "attributes": {
        "definition": "在承诺时间内交付且状态可追溯"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "building-block-description-default-supports",
      "type": "traces_to",
      "source": "building-block-description-default-record",
      "target": "building-block-description-default-target",
      "label": "本工作产品的结论为该业务目标提供候选支撑",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-building-block-description-default",
    "artifact_id": "building-block-description",
    "profile_id": "building-block-description-default",
    "title": "构建块描述／虚构案例",
    "entity_ids": [
      "building-block-description-default-record",
      "building-block-description-default-target"
    ],
    "relationship_ids": [
      "building-block-description-default-supports"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact building-block-description --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
