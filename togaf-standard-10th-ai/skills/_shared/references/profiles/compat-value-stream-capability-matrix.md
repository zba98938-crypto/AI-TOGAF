# 价值流/能力矩阵（兼容默认）

`profile_id`: compat-value-stream-capability-matrix；`artifact_id`: value-stream-capability-matrix；主责：[togaf-value-streams](../../../togaf-value-streams/SKILL.md)。

来源：G248；G178；G233。

## 构图与定义状态

表示族：`matrix`；输出：`table`。规范版本：2.1。

{
  "id": "compat-value-stream-capability-matrix",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：value_stream, value_stage, capability。关系类型：enabled_by。

```json
{
  "entities": {
    "value_stream": [],
    "value_stage": [],
    "capability": []
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 能力多次出现是复用
- 颜色未定义时不能解释为成熟度

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
    "id": "v-value-stream-capability-matrix",
    "artifact_id": "value-stream-capability-matrix",
    "title": "价值流/能力矩阵 · 星河零售虚构案例",
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
      "stage-order",
      "cap-order",
      "cap-stock",
      "stage-deliver",
      "cap-delivery"
    ],
    "relationship_ids": [
      "stage-cap-order",
      "stage-cap-stock",
      "stage-cap-delivery"
    ],
    "analysis": "哪些能力使能哪些价值流或阶段？ 本视图限定订单履约改造范围，展示案例设定的价值流/能力矩阵。逐阶段走查价值交付；实际项目需由相关责任方核实。",
    "legend": "列能力使能行价值流或阶段；单元代码：enables；未记录不等于不存在。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-value-stream-capability-matrix"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-value-stream-capability-matrix --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-value-stream-capability-matrix --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
