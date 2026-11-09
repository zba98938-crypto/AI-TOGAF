# 业务模式基线目标比较

`profile_id`: business-model-baseline-target；`artifact_id`: business-model-diagram；主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G18A §5–7；G18A/fig7-1；G18A/fig7-2。

## 构图与定义状态

表示族：`canvas-compare`；输出：`diagram`。规范版本：2.1。

{
  "source_verified": false,
  "source_figure": "G18A/fig7-1",
  "layout_notes": "逐块比较变化，状态与批准状态分开",
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
  "verification_evidence": "reviews/source-verification/business-model-baseline-target.json",
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

- 逐块比较变化，状态与批准状态分开

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
      "id": "business-model-baseline-target-0-current",
      "type": "business_model_element",
      "name": "商品供应商与承运商",
      "attributes": {
        "block": "关键伙伴",
        "detail": "商品供应商与承运商"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "concept_id": "business-model-baseline-target-0",
      "state_id": "current",
      "evolution": "baseline"
    },
    {
      "id": "business-model-baseline-target-1-current",
      "type": "business_model_element",
      "name": "订单确认与履约",
      "attributes": {
        "block": "关键活动",
        "detail": "订单确认与履约"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "concept_id": "business-model-baseline-target-1",
      "state_id": "current",
      "evolution": "baseline"
    },
    {
      "id": "business-model-baseline-target-2-current",
      "type": "business_model_element",
      "name": "门店库存和店员",
      "attributes": {
        "block": "关键资源",
        "detail": "门店库存和店员"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "concept_id": "business-model-baseline-target-2",
      "state_id": "current",
      "evolution": "baseline"
    },
    {
      "id": "business-model-baseline-target-3-current",
      "type": "business_model_element",
      "name": "现场获得合适商品",
      "attributes": {
        "block": "价值主张",
        "detail": "现场获得合适商品"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "concept_id": "business-model-baseline-target-3",
      "state_id": "current",
      "evolution": "baseline"
    },
    {
      "id": "business-model-baseline-target-4-current",
      "type": "business_model_element",
      "name": "门店人工咨询",
      "attributes": {
        "block": "客户关系",
        "detail": "门店人工咨询"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "concept_id": "business-model-baseline-target-4",
      "state_id": "current",
      "evolution": "baseline"
    },
    {
      "id": "business-model-baseline-target-5-current",
      "type": "business_model_element",
      "name": "门店柜台",
      "attributes": {
        "block": "渠道",
        "detail": "门店柜台"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "concept_id": "business-model-baseline-target-5",
      "state_id": "current",
      "evolution": "baseline"
    },
    {
      "id": "business-model-baseline-target-6-current",
      "type": "business_model_element",
      "name": "门店周边客户",
      "attributes": {
        "block": "客户细分",
        "detail": "门店周边客户"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "concept_id": "business-model-baseline-target-6",
      "state_id": "current",
      "evolution": "baseline"
    },
    {
      "id": "business-model-baseline-target-7-current",
      "type": "business_model_element",
      "name": "库存、仓储、人员与配送成本",
      "attributes": {
        "block": "成本结构",
        "detail": "库存、仓储、人员与配送成本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "concept_id": "business-model-baseline-target-7",
      "state_id": "current",
      "evolution": "baseline"
    },
    {
      "id": "business-model-baseline-target-8-current",
      "type": "business_model_element",
      "name": "商品销售收入及明确服务收费",
      "attributes": {
        "block": "收入来源",
        "detail": "商品销售收入及明确服务收费"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "concept_id": "business-model-baseline-target-8",
      "state_id": "current",
      "evolution": "baseline"
    },
    {
      "id": "business-model-baseline-target-0-target",
      "type": "business_model_element",
      "name": "商品供应商与承运商",
      "attributes": {
        "block": "关键伙伴",
        "detail": "商品供应商与承运商"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "concept_id": "business-model-baseline-target-0",
      "state_id": "target",
      "evolution": "target"
    },
    {
      "id": "business-model-baseline-target-1-target",
      "type": "business_model_element",
      "name": "订单确认与履约",
      "attributes": {
        "block": "关键活动",
        "detail": "订单确认与履约"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "concept_id": "business-model-baseline-target-1",
      "state_id": "target",
      "evolution": "target"
    },
    {
      "id": "business-model-baseline-target-2-target",
      "type": "business_model_element",
      "name": "共享库存与履约服务团队",
      "attributes": {
        "block": "关键资源",
        "detail": "共享库存与履约服务团队"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "concept_id": "business-model-baseline-target-2",
      "state_id": "target",
      "evolution": "target"
    },
    {
      "id": "business-model-baseline-target-3-target",
      "type": "business_model_element",
      "name": "跨渠道选择并跟踪交付",
      "attributes": {
        "block": "价值主张",
        "detail": "跨渠道选择并跟踪交付"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "concept_id": "business-model-baseline-target-3",
      "state_id": "target",
      "evolution": "target"
    },
    {
      "id": "business-model-baseline-target-4-target",
      "type": "business_model_element",
      "name": "人工支持与线上履约通知",
      "attributes": {
        "block": "客户关系",
        "detail": "人工支持与线上履约通知"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "concept_id": "business-model-baseline-target-4",
      "state_id": "target",
      "evolution": "target"
    },
    {
      "id": "business-model-baseline-target-5-target",
      "type": "business_model_element",
      "name": "门店与线上预约渠道",
      "attributes": {
        "block": "渠道",
        "detail": "门店与线上预约渠道"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "concept_id": "business-model-baseline-target-5",
      "state_id": "target",
      "evolution": "target"
    },
    {
      "id": "business-model-baseline-target-6-target",
      "type": "business_model_element",
      "name": "本地门店及异地线上客户",
      "attributes": {
        "block": "客户细分",
        "detail": "本地门店及异地线上客户"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "concept_id": "business-model-baseline-target-6",
      "state_id": "target",
      "evolution": "target"
    },
    {
      "id": "business-model-baseline-target-7-target",
      "type": "business_model_element",
      "name": "库存、仓储、人员与配送成本",
      "attributes": {
        "block": "成本结构",
        "detail": "库存、仓储、人员与配送成本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "concept_id": "business-model-baseline-target-7",
      "state_id": "target",
      "evolution": "target"
    },
    {
      "id": "business-model-baseline-target-8-target",
      "type": "business_model_element",
      "name": "商品销售收入及明确服务收费",
      "attributes": {
        "block": "收入来源",
        "detail": "商品销售收入及明确服务收费"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "concept_id": "business-model-baseline-target-8",
      "state_id": "target",
      "evolution": "target"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-business-model-baseline-target",
    "artifact_id": "business-model-diagram",
    "profile_id": "business-model-baseline-target",
    "title": "业务模式基线目标比较／虚构案例",
    "entity_ids": [
      "business-model-baseline-target-0-current",
      "business-model-baseline-target-1-current",
      "business-model-baseline-target-2-current",
      "business-model-baseline-target-3-current",
      "business-model-baseline-target-4-current",
      "business-model-baseline-target-5-current",
      "business-model-baseline-target-6-current",
      "business-model-baseline-target-7-current",
      "business-model-baseline-target-8-current",
      "business-model-baseline-target-0-target",
      "business-model-baseline-target-1-target",
      "business-model-baseline-target-2-target",
      "business-model-baseline-target-3-target",
      "business-model-baseline-target-4-target",
      "business-model-baseline-target-5-target",
      "business-model-baseline-target-6-target",
      "business-model-baseline-target-7-target",
      "business-model-baseline-target-8-target"
    ],
    "relationship_ids": [],
    "analysis": "逐一核对相同区块在当前门店模式和目标全渠道模式的内容。渠道、客户关系、关键资源、细分及价值主张变化；关键活动、伙伴、成本与收入本例未变，不能据此推断没有未来成本影响。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。",
    "state_ids": [
      "current",
      "target"
    ],
    "allow_mixed_evolution": true
  },
  "states": [
    {
      "id": "current",
      "name": "当前门店模式",
      "evolution": "baseline"
    },
    {
      "id": "target",
      "name": "目标全渠道模式",
      "evolution": "target"
    }
  ]
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile business-model-baseline-target --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile business-model-baseline-target --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
