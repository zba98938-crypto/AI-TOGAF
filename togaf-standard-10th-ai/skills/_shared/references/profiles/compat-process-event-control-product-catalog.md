# 流程/事件/控制/产品目录（兼容默认）

`profile_id`: compat-process-event-control-product-catalog；`artifact_id`: process-event-control-product-catalog；主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G248；G248；G152；G233。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1。

{
  "id": "compat-process-event-control-product-catalog",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：process, event, control, product。关系类型：triggers, produces, controls。

```json
{
  "entities": {
    "process": [
      "definition",
      "owner",
      "lifecycle"
    ],
    "event": [
      "definition",
      "owner",
      "lifecycle"
    ],
    "control": [
      "definition",
      "owner",
      "lifecycle"
    ],
    "product": [
      "definition",
      "owner",
      "lifecycle"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 事件不是活动
- 控制目标与控制措施要可区分

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
      "id": "control",
      "type": "control",
      "name": "最小权限与审计控制",
      "attributes": {
        "definition": "按角色和目的限制数据并记录访问",
        "owner": "安全负责人",
        "lifecycle": "目标设计",
        "classification": "客户联系信息",
        "purpose": "订单履约"
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
    },
    {
      "id": "control-process",
      "type": "controls",
      "source": "control",
      "target": "process",
      "label": "限制客户信息访问",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-process-event-control-product-catalog",
    "artifact_id": "process-event-control-product-catalog",
    "title": "流程/事件/控制/产品目录 · 星河零售虚构案例",
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
      "process",
      "event-submit",
      "control",
      "product"
    ],
    "relationship_ids": [
      "event-process",
      "process-product",
      "control-process"
    ],
    "analysis": "哪些事件启动流程，流程受何控制并产出什么？ 本视图限定订单履约改造范围，展示案例设定的流程/事件/控制/产品目录。分别识别流程、事件、控制和产品；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-process-event-control-product-catalog"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-process-event-control-product-catalog --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-process-event-control-product-catalog --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
