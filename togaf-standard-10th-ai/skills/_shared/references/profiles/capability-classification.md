# 能力分类地图

`profile_id`: capability-classification；`artifact_id`: business-capability-map；主责：[togaf-strategy-capabilities](../../../togaf-strategy-capabilities/SKILL.md)。

来源：G211/fig3-2。

## 构图与定义状态

表示族：`nested-map`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "source_figure": "G211/fig3-2",
  "layout_notes": "战略、核心、支持分类带独立；带内位置不表示顺序",
  "review_status": "source-located-awaiting-template-validation",
  "bands": [
    "战略",
    "核心",
    "支持"
  ],
  "verification_evidence": "reviews/source-verification/capability-classification.json",
  "source_asset_status": "available-separate-from-template-review"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：capability。关系类型：decomposes。

```json
{
  "entities": {
    "capability": [
      "definition",
      "category",
      "level"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 战略、核心、支持分类带独立；带内位置不表示顺序

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

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
      "id": "capability-classification-fulfillment",
      "type": "capability",
      "name": "订单履约",
      "attributes": {
        "definition": "使已确认订单按承诺交付，排除市场获客",
        "category": "核心",
        "level": 1
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-classification-order",
      "type": "capability",
      "name": "订单管理",
      "attributes": {
        "definition": "建立并维持准确订单状态",
        "category": "核心",
        "level": 2
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-classification-delivery",
      "type": "capability",
      "name": "交付管理",
      "attributes": {
        "definition": "管理发运承诺和交付结果",
        "category": "核心",
        "level": 2
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-classification-strategy",
      "type": "capability",
      "name": "业务规划",
      "attributes": {
        "definition": "确定企业方向和业务结果",
        "category": "战略",
        "level": 1
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-classification-support",
      "type": "capability",
      "name": "人员发展",
      "attributes": {
        "definition": "发展履约所需人员能力",
        "category": "支持",
        "level": 1
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "capability-classification-decomp-order",
      "type": "decomposes",
      "source": "capability-classification-fulfillment",
      "target": "capability-classification-order",
      "label": "履约能力分解为订单管理",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-classification-decomp-delivery",
      "type": "decomposes",
      "source": "capability-classification-fulfillment",
      "target": "capability-classification-delivery",
      "label": "履约能力分解为交付管理",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-capability-classification",
    "artifact_id": "business-capability-map",
    "profile_id": "capability-classification",
    "title": "能力分类地图／虚构案例",
    "entity_ids": [
      "capability-classification-fulfillment",
      "capability-classification-order",
      "capability-classification-delivery",
      "capability-classification-strategy",
      "capability-classification-support"
    ],
    "relationship_ids": [
      "capability-classification-decomp-order",
      "capability-classification-decomp-delivery"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile capability-classification --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile capability-classification --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
