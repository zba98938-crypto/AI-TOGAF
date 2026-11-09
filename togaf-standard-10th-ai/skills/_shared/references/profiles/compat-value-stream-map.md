# 价值流地图（兼容默认）

`profile_id`: compat-value-stream-map；`artifact_id`: value-stream-map；主责：[togaf-value-streams](../../../togaf-value-streams/SKILL.md)。

来源：G248；G178；G233。

## 构图与定义状态

表示族：`stage-map`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-value-stream-map",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：value_stream, value_stage, capability。关系类型：has_stage, precedes, enabled_by。

```json
{
  "entities": {
    "value_stream": [
      "description",
      "value"
    ],
    "value_stage": [
      "entry",
      "exit",
      "value_item",
      "ordinal",
      "description"
    ],
    "capability": []
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 重复能力是跨阶段复用
- 能力列中上下位置不代表优先级

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
      "id": "cap-order",
      "type": "capability",
      "name": "订单管理",
      "attributes": {
        "definition": "维护订单承诺及履行状态",
        "owner": "销售负责人",
        "level": 2,
        "category": "核心能力",
        "score": "待真实评估"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cap-stock",
      "type": "capability",
      "name": "库存管理",
      "attributes": {
        "definition": "掌握库存并分配可售数量",
        "owner": "仓储负责人",
        "level": 2,
        "category": "核心能力",
        "score": "待真实评估"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cap-delivery",
      "type": "capability",
      "name": "交付管理",
      "attributes": {
        "definition": "完成发运及送达确认",
        "owner": "配送负责人",
        "level": 2,
        "category": "核心能力",
        "score": "待真实评估"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "vs",
      "type": "value_stream",
      "name": "获得零售商品",
      "attributes": {
        "stakeholder": "客户",
        "trigger": "客户形成购买需要",
        "outcome": "客户获得所需商品",
        "owner": "履约负责人",
        "description": "从可靠购买承诺到获得可用商品的端到端价值",
        "value": "客户可靠并及时获得所需商品"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "stage-order",
      "type": "value_stage",
      "name": "确认购买",
      "attributes": {
        "entry": "客户已选择商品",
        "exit": "订单和可售库存已确认",
        "value_item": "可靠购买承诺",
        "stakeholder": "客户",
        "ordinal": 1,
        "description": "按进入退出条件交付该阶段增量价值"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "stage-deliver",
      "type": "value_stage",
      "name": "收到商品",
      "attributes": {
        "entry": "订单已确认",
        "exit": "客户确认送达",
        "value_item": "商品可使用",
        "stakeholder": "客户",
        "ordinal": 2,
        "description": "按进入退出条件交付该阶段增量价值"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "vs-stage1",
      "type": "has_stage",
      "source": "vs",
      "target": "stage-order",
      "label": "包含确认购买阶段",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "vs-stage2",
      "type": "has_stage",
      "source": "vs",
      "target": "stage-deliver",
      "label": "包含收到商品阶段",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "stage-ordering",
      "type": "precedes",
      "source": "stage-order",
      "target": "stage-deliver",
      "label": "确认后交付",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "stage-cap-order",
      "type": "enabled_by",
      "source": "stage-order",
      "target": "cap-order",
      "label": "订单能力使能确认",
      "evidence": [
        "case"
      ],
      "certainty": "assumed",
      "codes": [
        "enables"
      ]
    },
    {
      "id": "stage-cap-stock",
      "type": "enabled_by",
      "source": "stage-order",
      "target": "cap-stock",
      "label": "库存能力使能确认",
      "evidence": [
        "case"
      ],
      "certainty": "assumed",
      "codes": [
        "enables"
      ]
    },
    {
      "id": "stage-cap-delivery",
      "type": "enabled_by",
      "source": "stage-deliver",
      "target": "cap-delivery",
      "label": "交付能力使能收货",
      "evidence": [
        "case"
      ],
      "certainty": "assumed",
      "codes": [
        "enables"
      ]
    }
  ],
  "view": {
    "id": "v-value-stream-map",
    "artifact_id": "value-stream-map",
    "title": "价值流地图 · 星河零售虚构案例",
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
      "vs",
      "stage-order",
      "stage-deliver",
      "cap-order",
      "cap-stock",
      "cap-delivery"
    ],
    "relationship_ids": [
      "vs-stage1",
      "vs-stage2",
      "stage-ordering",
      "stage-cap-order",
      "stage-cap-stock",
      "stage-cap-delivery"
    ],
    "analysis": "客户先获得可靠购买承诺，再获得商品。库存能力使能确认阶段；交付能力使能收货，能力不是流程步骤。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-value-stream-map"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-value-stream-map --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-value-stream-map --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
