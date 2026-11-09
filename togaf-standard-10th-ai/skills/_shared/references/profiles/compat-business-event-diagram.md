# 业务事件图（兼容默认）

`profile_id`: compat-business-event-diagram；`artifact_id`: business-event-diagram；主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G248；G176；G248。

## 构图与定义状态

表示族：`network`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-business-event-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：event, process, business_service。关系类型：triggers, produces。

```json
{
  "entities": {
    "event": [
      "trigger",
      "outcome"
    ],
    "process": [],
    "business_service": []
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 消息是事件载体而非必然等于业务事件
- 不要与完整流程控制流混同

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
      "id": "process",
      "type": "process",
      "name": "订单履行流程",
      "attributes": {
        "definition": "从订单提交到送达的处理",
        "owner": "履约负责人",
        "lifecycle": "持续运营",
        "entry": "订单已提交",
        "exit": "交付确认",
        "automation": "部分自动"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "event-submit",
      "type": "event",
      "name": "订单已提交",
      "attributes": {
        "definition": "客户完成订单提交",
        "owner": "销售负责人",
        "lifecycle": "业务事件",
        "trigger": "客户提交",
        "outcome": "启动确认"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "product",
      "type": "product",
      "name": "零售商品",
      "attributes": {
        "definition": "面向客户销售的产品",
        "owner": "商品负责人",
        "lifecycle": "在售"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "event-process",
      "type": "triggers",
      "source": "event-submit",
      "target": "process",
      "label": "提交事件触发履行",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "process-product",
      "type": "produces",
      "source": "process",
      "target": "product",
      "label": "流程交付商品",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-business-event-diagram",
    "artifact_id": "business-event-diagram",
    "title": "业务事件图 · 星河零售虚构案例",
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
      "event-submit",
      "process",
      "product"
    ],
    "relationship_ids": [
      "event-process",
      "process-product"
    ],
    "analysis": "哪些业务事件触发、终止或改变业务行为？ 本视图限定订单履约改造范围，展示案例设定的业务事件图。识别有业务意义的发生事实；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-business-event-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-business-event-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-business-event-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
