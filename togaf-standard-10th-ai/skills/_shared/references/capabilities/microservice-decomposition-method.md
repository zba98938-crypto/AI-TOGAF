# 微服务应用分解方法

ID：`microservice-decomposition-method`。主责：[togaf-application-architecture](../../../togaf-application-architecture/SKILL.md)。

来源：G21I §10.5 / Table 10-1。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

应用应按什么边界拆分？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 应用应按什么边界拆分？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- business_function
- ownership
- cohesion

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：service_boundary。

```json
{
  "service_boundary": [
    "business_function",
    "ownership",
    "cohesion",
    "coupling",
    "interface",
    "data_responsibility"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "business_function": {
    "meaning": "业务功能引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "ownership": {
    "meaning": "数据所有权及责任",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "cohesion": {
    "meaning": "候选边界内聚性及判断依据",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "coupling": {
    "meaning": "边界之间的耦合与代价",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "interface": {
    "meaning": "公开接口与契约",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "data_responsibility": {
    "meaning": "数据读写与所有权责任",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `project:service_partition` | service_boundary → service_boundary | 父业务边界分割为具有生命周期与数据责任的服务边界；非技术进程或部署包含 |

## 分析步骤

1. 从业务功能和质量目标确定候选边界
2. 检查职责与数据所有权
3. 比较耦合和独立部署代价
4. 记录分解原则和过渡

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 小服务数量不是微服务架构成功指标
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 小服务数量不是微服务架构成功指标


## 视图和交付物

- [微服务应用分解方法](../profiles/microservice-decomposition-method-default.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「微服务应用分解方法」给出：小服务数量不是微服务架构成功指标",
    "expected": "missing-evidence",
    "why": "小服务数量不是微服务架构成功指标"
  },
  "modification_example": {
    "change": "在「微服务应用分解方法」的范围内新增或修改一项，检查下游是否随之变化",
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
      "description": "虚构业务原料：在线订单履约业务边界：{\"business_function\": \"确认订单、预留库存并协调发运\", \"ownership\": \"跨服务架构组协调边界，不共享单一数据库所有权\", \"cohesion\": \"统一客户履约目标，内部可由契约分离\", \"coupling\": \"订单与库存通过预留契约协作\", \"interface\": \"客户提交订单；内部预留和取消契约\", \"data_responsibility\": \"订单状态归订单服务，库存可用量归库存服务\", \"definition\": \"按业务职责拆分，不能按数据表一表一服务\"}；订单确认服务：{\"business_function\": \"接受订单、确认付款状态与维持订单生命周期\", \"ownership\": \"订单产品团队\", \"cohesion\": \"订单状态机及客户确认规则一起变化\", \"coupling\": \"通过预留token调用库存服务；不直接写库存表\", \"interface\": \"POST /orders、GET /orders/{id}；输出订单事件\", \"data_responsibility\": \"订单及确认状态；引用预留token不拥有库存可用量\", \"definition\": \"对内聚交易职责建服务，跨服务一致性需补补偿策略\"}；库存预留服务：{\"business_function\": \"为指定订单预留、释放及确认库存\", \"ownership\": \"库存产品团队\", \"cohesion\": \"可用量与预留一致性规则由同团队维护\", \"coupling\": \"消费订单取消，向订单返回预留token和到期时间\", \"interface\": \"POST /reservations、DELETE /reservations/{token}\", \"data_responsibility\": \"库存与预留记录；不复制客户付款信息\", \"definition\": \"为超时和取消提供幂等释放；跨服务补偿仍需演练\"}"
    }
  ],
  "entities": [
    {
      "id": "microservice-decomposition-method-default-root",
      "type": "service_boundary",
      "name": "在线订单履约业务边界",
      "attributes": {
        "business_function": "确认订单、预留库存并协调发运",
        "ownership": "跨服务架构组协调边界，不共享单一数据库所有权",
        "cohesion": "统一客户履约目标，内部可由契约分离",
        "coupling": "订单与库存通过预留契约协作",
        "interface": "客户提交订单；内部预留和取消契约",
        "data_responsibility": "订单状态归订单服务，库存可用量归库存服务",
        "definition": "按业务职责拆分，不能按数据表一表一服务"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "microservice-decomposition-method-default-child0",
      "type": "service_boundary",
      "name": "订单确认服务",
      "attributes": {
        "business_function": "接受订单、确认付款状态与维持订单生命周期",
        "ownership": "订单产品团队",
        "cohesion": "订单状态机及客户确认规则一起变化",
        "coupling": "通过预留token调用库存服务；不直接写库存表",
        "interface": "POST /orders、GET /orders/{id}；输出订单事件",
        "data_responsibility": "订单及确认状态；引用预留token不拥有库存可用量",
        "definition": "对内聚交易职责建服务，跨服务一致性需补补偿策略"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "microservice-decomposition-method-default-child1",
      "type": "service_boundary",
      "name": "库存预留服务",
      "attributes": {
        "business_function": "为指定订单预留、释放及确认库存",
        "ownership": "库存产品团队",
        "cohesion": "可用量与预留一致性规则由同团队维护",
        "coupling": "消费订单取消，向订单返回预留token和到期时间",
        "interface": "POST /reservations、DELETE /reservations/{token}",
        "data_responsibility": "库存与预留记录；不复制客户付款信息",
        "definition": "为超时和取消提供幂等释放；跨服务补偿仍需演练"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "microservice-decomposition-method-default-part0",
      "type": "project:service_partition",
      "source": "microservice-decomposition-method-default-root",
      "target": "microservice-decomposition-method-default-child0",
      "label": "父业务边界分割为具有生命周期与数据责任的服务边界；非技术进程或部署包含",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "microservice-decomposition-method-default-part1",
      "type": "project:service_partition",
      "source": "microservice-decomposition-method-default-root",
      "target": "microservice-decomposition-method-default-child1",
      "label": "父业务边界分割为具有生命周期与数据责任的服务边界；非技术进程或部署包含",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-microservice-decomposition-method-default",
    "artifact_id": "microservice-decomposition-method",
    "profile_id": "microservice-decomposition-method-default",
    "title": "微服务应用分解方法／虚构案例",
    "entity_ids": [
      "microservice-decomposition-method-default-root",
      "microservice-decomposition-method-default-child0",
      "microservice-decomposition-method-default-child1"
    ],
    "relationship_ids": [
      "microservice-decomposition-method-default-part0",
      "microservice-decomposition-method-default-part1"
    ],
    "analysis": "从本例原始职责、权限、契约与验收材料形成明确分解。关系类型为命名空间项目语义，来源仅指导方法。父子结构不赋予批准或执行先后。",
    "legend": "嵌套只表示已声明的project:service_partition关系；候选事实、实际批准与实现状态分开。"
  },
  "extensions": {
    "relationship_types": {
      "project:service_partition": {
        "source_types": [
          "service_boundary"
        ],
        "target_types": [
          "service_boundary"
        ],
        "meaning": "父业务边界分割为具有生命周期与数据责任的服务边界；非技术进程或部署包含"
      }
    }
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact microservice-decomposition-method --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
