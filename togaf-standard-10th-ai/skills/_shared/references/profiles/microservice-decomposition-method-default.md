# 微服务应用分解方法

`profile_id`: microservice-decomposition-method-default；`artifact_id`: microservice-decomposition-method；主责：[togaf-application-architecture](../../../togaf-application-architecture/SKILL.md)。

来源：G21I §10.5 / Table 10-1。

## 构图与定义状态

表示族：`nested-map`；输出：`diagram`。规范版本：2.2。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。",
  "version": "2.2"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：service_boundary。关系类型：project:service_partition。

```json
{
  "entities": {
    "service_boundary": [
      "business_function",
      "ownership",
      "cohesion",
      "coupling",
      "interface",
      "data_responsibility"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 小服务数量不是微服务架构成功指标
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

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile microservice-decomposition-method-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile microservice-decomposition-method-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
