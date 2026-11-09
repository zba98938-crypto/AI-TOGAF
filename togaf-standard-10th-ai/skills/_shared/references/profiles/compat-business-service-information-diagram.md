# 业务服务/信息图（兼容默认）

`profile_id`: compat-business-service-information-diagram；`artifact_id`: business-service-information-diagram；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G248；G190；G248。

## 构图与定义状态

表示族：`network`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-business-service-information-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：business_service, information。关系类型：produces_information, consumes_information。

```json
{
  "entities": {
    "business_service": [
      "definition",
      "owner"
    ],
    "information": [
      "definition",
      "owner"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 信息概念不等于存储表
- 消费信息不自动赋予修改权限

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构兼容案例；不是正式定义或来源图复刻。",
  "sources": [
    {
      "id": "case",
      "kind": "example",
      "description": "全量验收使用的虚构业务情景；数字、主体和架构均非真实项目事实。"
    },
    {
      "id": "assumption",
      "kind": "assumption",
      "description": "方案和收益因果假设，需在真实项目中验证。"
    }
  ],
  "entities": [
    {
      "id": "service-order",
      "type": "business_service",
      "name": "订单确认服务",
      "attributes": {
        "definition": "向客户提供可履行的订单确认",
        "owner": "销售负责人",
        "service_level": "示例服务承诺由业务方确认"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "information-customer",
      "type": "information",
      "name": "客户信息",
      "attributes": {
        "definition": "描述交易客户的业务信息",
        "category": "客户主题",
        "owner": "客户数据负责人"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "information-order",
      "type": "information",
      "name": "订单信息",
      "attributes": {
        "definition": "描述客户购买承诺的业务信息",
        "category": "交易主题",
        "owner": "销售负责人"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "service-info",
      "type": "produces_information",
      "source": "service-order",
      "target": "information-order",
      "label": "输出订单确认信息",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "service-info-input",
      "type": "consumes_information",
      "source": "service-order",
      "target": "information-customer",
      "label": "消费必要客户信息",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-business-service-information-diagram",
    "artifact_id": "business-service-information-diagram",
    "title": "业务服务/信息图 · 星河零售虚构案例",
    "context": {
      "domains": [
        "business",
        "data",
        "application",
        "technology"
      ],
      "landscape": "segment",
      "purpose": "project",
      "abstraction": "logical",
      "evolution": "target"
    },
    "entity_ids": [
      "service-order",
      "information-order",
      "information-customer"
    ],
    "relationship_ids": [
      "service-info",
      "service-info-input"
    ],
    "analysis": "业务服务产生或消费哪些业务信息？ 本视图限定订单履约改造范围，展示案例设定的业务服务/信息图。从服务结果识别信息需要；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-business-service-information-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-business-service-information-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-business-service-information-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
