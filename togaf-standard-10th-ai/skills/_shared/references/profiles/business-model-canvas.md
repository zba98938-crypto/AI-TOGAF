# 九块业务模式画布

`profile_id`: business-model-canvas；`artifact_id`: business-model-diagram；主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G18A/figA-1。

## 构图与定义状态

表示族：`canvas`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "source_figure": "G18A/figA-1",
  "layout_notes": "保留九块空间结构；多条目及同一对象复用不强行合并",
  "review_status": "source-located-awaiting-template-validation",
  "blocks": [
    "关键伙伴",
    "关键活动",
    "关键资源",
    "价值主张",
    "客户关系",
    "渠道",
    "客户细分",
    "成本结构",
    "收入来源"
  ],
  "canvas_kind": "business-model",
  "verification_evidence": "reviews/source-verification/business-model-canvas.json",
  "source_asset_status": "available-separate-from-template-review"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：business_model_element。关系类型：。

```json
{
  "entities": {
    "business_model_element": [
      "block",
      "detail"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 保留九块空间结构；多条目及同一对象复用不强行合并

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
      "id": "business-model-canvas-0",
      "type": "business_model_element",
      "name": "商品供应商与承运商",
      "attributes": {
        "block": "关键伙伴",
        "detail": "商品供应商与承运商"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-model-canvas-1",
      "type": "business_model_element",
      "name": "订单确认与履约",
      "attributes": {
        "block": "关键活动",
        "detail": "订单确认与履约"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-model-canvas-2",
      "type": "business_model_element",
      "name": "库存与客户服务人员",
      "attributes": {
        "block": "关键资源",
        "detail": "库存与客户服务人员"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-model-canvas-3",
      "type": "business_model_element",
      "name": "可靠且可跟踪的商品交付",
      "attributes": {
        "block": "价值主张",
        "detail": "可靠且可跟踪的商品交付"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-model-canvas-4",
      "type": "business_model_element",
      "name": "及时解释并处理例外",
      "attributes": {
        "block": "客户关系",
        "detail": "及时解释并处理例外"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-model-canvas-5",
      "type": "business_model_element",
      "name": "在线商店与通知渠道",
      "attributes": {
        "block": "渠道",
        "detail": "在线商店与通知渠道"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-model-canvas-6",
      "type": "business_model_element",
      "name": "需要透明履约的线上客户",
      "attributes": {
        "block": "客户细分",
        "detail": "需要透明履约的线上客户"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-model-canvas-7",
      "type": "business_model_element",
      "name": "库存、仓储、人员与配送成本",
      "attributes": {
        "block": "成本结构",
        "detail": "库存、仓储、人员与配送成本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-model-canvas-8",
      "type": "business_model_element",
      "name": "商品销售收入及明确服务收费",
      "attributes": {
        "block": "收入来源",
        "detail": "商品销售收入及明确服务收费"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-business-model-canvas",
    "artifact_id": "business-model-diagram",
    "profile_id": "business-model-canvas",
    "title": "九块业务模式画布／虚构案例",
    "entity_ids": [
      "business-model-canvas-0",
      "business-model-canvas-1",
      "business-model-canvas-2",
      "business-model-canvas-3",
      "business-model-canvas-4",
      "business-model-canvas-5",
      "business-model-canvas-6",
      "business-model-canvas-7",
      "business-model-canvas-8"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile business-model-canvas --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile business-model-canvas --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
