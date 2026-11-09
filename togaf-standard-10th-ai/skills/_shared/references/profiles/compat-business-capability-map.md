# 业务能力地图（兼容默认）

`profile_id`: compat-business-capability-map；`artifact_id`: business-capability-map；主责：[togaf-strategy-capabilities](../../../togaf-strategy-capabilities/SKILL.md)。

来源：G248；G211；G233。

## 构图与定义状态

表示族：`nested-map`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-business-capability-map",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：capability。关系类型：decomposes。

```json
{
  "entities": {
    "capability": [
      "definition",
      "level",
      "category",
      "score"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 颜色须有量尺及证据
- 能力实例不能画成子能力

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
      "id": "cap-fulfillment",
      "type": "capability",
      "name": "订单履约管理",
      "attributes": {
        "definition": "协调从接单到交付的履约能力",
        "owner": "履约负责人",
        "level": 1,
        "category": "核心能力",
        "score": "待真实评估"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
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
    }
  ],
  "relationships": [
    {
      "id": "cap-child-order",
      "type": "decomposes",
      "source": "cap-fulfillment",
      "target": "cap-order",
      "label": "包含订单管理能力",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cap-child-stock",
      "type": "decomposes",
      "source": "cap-fulfillment",
      "target": "cap-stock",
      "label": "包含库存管理能力",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cap-child-delivery",
      "type": "decomposes",
      "source": "cap-fulfillment",
      "target": "cap-delivery",
      "label": "包含交付管理能力",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-business-capability-map",
    "artifact_id": "business-capability-map",
    "title": "业务能力地图 · 星河零售虚构案例",
    "context": {
      "domains": [
        "business",
        "data",
        "application",
        "technology"
      ],
      "landscape": "segment",
      "purpose": "project",
      "abstraction": "conceptual",
      "evolution": "target"
    },
    "entity_ids": [
      "cap-fulfillment",
      "cap-order",
      "cap-stock",
      "cap-delivery"
    ],
    "relationship_ids": [
      "cap-child-order",
      "cap-child-stock",
      "cap-child-delivery"
    ],
    "analysis": "一级履约能力分解到订单、库存和交付。同层是静态能力；没有真实评分，因此不叠加成熟度颜色。",
    "legend": "卡片按布局排列；下方有向关系清单给出语义；未使用绩效热力颜色。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-business-capability-map"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-business-capability-map --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-business-capability-map --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
