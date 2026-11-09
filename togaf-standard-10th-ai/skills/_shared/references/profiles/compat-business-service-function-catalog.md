# 业务服务/功能目录（兼容默认）

`profile_id`: compat-business-service-function-catalog；`artifact_id`: business-service-function-catalog；主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G248；G248；G233。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1。

{
  "id": "compat-business-service-function-catalog",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：business_service, function。关系类型：realizes。

```json
{
  "entities": {
    "business_service": [
      "definition",
      "owner",
      "service_level"
    ],
    "function": [
      "definition",
      "owner",
      "service_level"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 服务不等于部门
- 业务服务不直接等同于 API

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
      "id": "fn-order",
      "type": "function",
      "name": "订单处理",
      "attributes": {
        "definition": "记录、校验并确认订单",
        "owner": "销售负责人",
        "service_level": "由订单确认服务承诺约束",
        "level": 1
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "fn-validate",
      "type": "function",
      "name": "订单校验",
      "attributes": {
        "definition": "校验库存与客户输入",
        "owner": "销售负责人",
        "service_level": "继承确认服务承诺",
        "level": 2
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "fn-service",
      "type": "realizes",
      "source": "fn-order",
      "target": "service-order",
      "label": "订单处理实现订单确认服务",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-business-service-function-catalog",
    "artifact_id": "business-service-function-catalog",
    "title": "业务服务/功能目录 · 星河零售虚构案例",
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
      "fn-order",
      "fn-validate"
    ],
    "relationship_ids": [
      "fn-service"
    ],
    "analysis": "哪些业务功能提供哪些面向消费者的服务？ 本视图限定订单履约改造范围，展示案例设定的业务服务/功能目录。区分服务承诺与内部功能；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-business-service-function-catalog"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-business-service-function-catalog --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-business-service-function-catalog --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
