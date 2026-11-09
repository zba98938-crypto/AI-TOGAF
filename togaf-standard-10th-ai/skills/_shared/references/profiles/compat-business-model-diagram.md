# 业务模式图（兼容默认）

`profile_id`: compat-business-model-diagram；`artifact_id`: business-model-diagram；主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G248；G18A。

## 构图与定义状态

表示族：`canvas`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-business-model-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：business_model_element。关系类型：business_dependency。

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

- 九宫格是所选方法不是 TOGAF 唯一强制表示
- 不能用组织图代替业务模式

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
      "id": "bmc-partner",
      "type": "business_model_element",
      "name": "物流伙伴",
      "attributes": {
        "block": "伙伴",
        "detail": "受控物流协作"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "bmc-activities",
      "type": "business_model_element",
      "name": "订单与交付",
      "attributes": {
        "block": "活动",
        "detail": "可靠履约"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "bmc-resources",
      "type": "business_model_element",
      "name": "库存与人员",
      "attributes": {
        "block": "资源",
        "detail": "可售商品和作业能力"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "bmc-value",
      "type": "business_model_element",
      "name": "可靠购物体验",
      "attributes": {
        "block": "价值",
        "detail": "可靠承诺并及时送达"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "bmc-relations",
      "type": "business_model_element",
      "name": "客户支持",
      "attributes": {
        "block": "关系",
        "detail": "自助加人工支持"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "bmc-channels",
      "type": "business_model_element",
      "name": "线上商城",
      "attributes": {
        "block": "渠道",
        "detail": "线上购买入口"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "bmc-customers",
      "type": "business_model_element",
      "name": "零售客户",
      "attributes": {
        "block": "客户",
        "detail": "购买商品的客户群"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "bmc-cost",
      "type": "business_model_element",
      "name": "履约成本",
      "attributes": {
        "block": "成本",
        "detail": "仓储、配送与系统成本"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "bmc-revenue",
      "type": "business_model_element",
      "name": "商品销售收入",
      "attributes": {
        "block": "收入",
        "detail": "销售商品获得收入"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "bmc-dependency",
      "type": "business_dependency",
      "source": "bmc-activities",
      "target": "bmc-value",
      "label": "履约活动创造可靠体验",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-business-model-diagram",
    "artifact_id": "business-model-diagram",
    "title": "业务模式图 · 星河零售虚构案例",
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
      "bmc-partner",
      "bmc-activities",
      "bmc-resources",
      "bmc-value",
      "bmc-relations",
      "bmc-channels",
      "bmc-customers",
      "bmc-cost",
      "bmc-revenue"
    ],
    "relationship_ids": [
      "bmc-dependency"
    ],
    "analysis": "线上渠道服务零售客户，以可靠履约形成价值，依赖库存、人员和物流伙伴。示例尚无真实收入成本，不能得出盈利结论。",
    "legend": "卡片按布局排列；下方有向关系清单给出语义；未使用绩效热力颜色。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-business-model-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-business-model-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-business-model-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
