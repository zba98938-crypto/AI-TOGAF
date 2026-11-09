# 能力变更叠加图

`profile_id`: capability-change-overlay；`artifact_id`: capability-increment-analysis；主责：[togaf-gap-solutions](../../../togaf-gap-solutions/SKILL.md)。

来源：G233/fig7-1。

## 构图与定义状态

表示族：`stage-map`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "source_figure": "G233/fig7-1",
  "layout_notes": "新建改进退役与配色是不同属性；必须回链详细模型",
  "review_status": "source-located-awaiting-template-validation",
  "verification_evidence": "reviews/source-verification/capability-change-overlay.json",
  "source_asset_status": "available-separate-from-template-review"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：application, capability, capability_instance, information, process, role, value_stage。关系类型：instance_comprises, instance_of, precedes, stage_uses_instance。

```json
{
  "entities": {
    "capability": [
      "definition"
    ],
    "capability_instance": [
      "definition",
      "stage_id"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 新建改进退役与配色是不同属性；必须回链详细模型

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
      "id": "capability-change-overlay-type",
      "type": "capability",
      "name": "客户身份管理",
      "attributes": {
        "definition": "建立并校验履约所需客户身份，不限定某应用"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-change-overlay-select",
      "type": "value_stage",
      "name": "选择商品",
      "attributes": {
        "order": 1,
        "entry_condition": "客户进入商店",
        "exit_condition": "形成待结算商品",
        "value_item": "可购买的商品选择"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-change-overlay-buy",
      "type": "value_stage",
      "name": "购买商品",
      "attributes": {
        "order": 2,
        "entry_condition": "客户确认购物篮",
        "exit_condition": "付款和客户身份得到确认",
        "value_item": "有效订单"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-change-overlay-browse",
      "type": "capability_instance",
      "name": "客户身份管理：选择阶段",
      "attributes": {
        "definition": "在该阶段按对应安全和体验要求实现客户身份管理",
        "stage_id": "capability-change-overlay-select",
        "change_kind": "保留",
        "baseline": "人工确认或访客身份",
        "target": "按风险分级校验身份",
        "rationale": "避免不必要的登录摩擦并满足付款安全",
        "gap": "付款阶段需补充强校验"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-change-overlay-browse-role",
      "type": "role",
      "name": "选择阶段：客户服务角色",
      "attributes": {
        "definition": "该阶段实例使用的客户服务角色"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-change-overlay-browse-process",
      "type": "process",
      "name": "选择阶段：校验客户身份",
      "attributes": {
        "definition": "该阶段实例使用的校验客户身份"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-change-overlay-browse-app",
      "type": "application",
      "name": "选择阶段：客户身份服务",
      "attributes": {
        "definition": "该阶段实例使用的客户身份服务"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-change-overlay-browse-info",
      "type": "information",
      "name": "选择阶段：客户身份信息",
      "attributes": {
        "definition": "该阶段实例使用的客户身份信息"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-change-overlay-payment",
      "type": "capability_instance",
      "name": "客户身份管理：购买阶段",
      "attributes": {
        "definition": "在该阶段按对应安全和体验要求实现客户身份管理",
        "stage_id": "capability-change-overlay-buy",
        "change_kind": "改进",
        "baseline": "人工确认或访客身份",
        "target": "按风险分级校验身份",
        "rationale": "避免不必要的登录摩擦并满足付款安全",
        "gap": "付款阶段需补充强校验"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-change-overlay-payment-role",
      "type": "role",
      "name": "购买阶段：客户服务角色",
      "attributes": {
        "definition": "该阶段实例使用的客户服务角色"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-change-overlay-payment-process",
      "type": "process",
      "name": "购买阶段：校验客户身份",
      "attributes": {
        "definition": "该阶段实例使用的校验客户身份"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-change-overlay-payment-app",
      "type": "application",
      "name": "购买阶段：客户身份服务",
      "attributes": {
        "definition": "该阶段实例使用的客户身份服务"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-change-overlay-payment-info",
      "type": "information",
      "name": "购买阶段：客户身份信息",
      "attributes": {
        "definition": "该阶段实例使用的客户身份信息"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "capability-change-overlay-next",
      "type": "precedes",
      "source": "capability-change-overlay-select",
      "target": "capability-change-overlay-buy",
      "label": "选择后进入购买",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-change-overlay-browse-type",
      "type": "instance_of",
      "source": "capability-change-overlay-browse",
      "target": "capability-change-overlay-type",
      "label": "实例属于客户身份管理能力类型",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-change-overlay-browse-stage",
      "type": "stage_uses_instance",
      "source": "capability-change-overlay-select",
      "target": "capability-change-overlay-browse",
      "label": "阶段由该身份实例使能",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-change-overlay-browse-role-composition",
      "type": "instance_comprises",
      "source": "capability-change-overlay-browse",
      "target": "capability-change-overlay-browse-role",
      "label": "实例组成：客户服务角色",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-change-overlay-browse-process-composition",
      "type": "instance_comprises",
      "source": "capability-change-overlay-browse",
      "target": "capability-change-overlay-browse-process",
      "label": "实例组成：校验客户身份",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-change-overlay-browse-app-composition",
      "type": "instance_comprises",
      "source": "capability-change-overlay-browse",
      "target": "capability-change-overlay-browse-app",
      "label": "实例组成：客户身份服务",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-change-overlay-browse-info-composition",
      "type": "instance_comprises",
      "source": "capability-change-overlay-browse",
      "target": "capability-change-overlay-browse-info",
      "label": "实例组成：客户身份信息",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-change-overlay-payment-type",
      "type": "instance_of",
      "source": "capability-change-overlay-payment",
      "target": "capability-change-overlay-type",
      "label": "实例属于客户身份管理能力类型",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-change-overlay-payment-stage",
      "type": "stage_uses_instance",
      "source": "capability-change-overlay-buy",
      "target": "capability-change-overlay-payment",
      "label": "阶段由该身份实例使能",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-change-overlay-payment-role-composition",
      "type": "instance_comprises",
      "source": "capability-change-overlay-payment",
      "target": "capability-change-overlay-payment-role",
      "label": "实例组成：客户服务角色",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-change-overlay-payment-process-composition",
      "type": "instance_comprises",
      "source": "capability-change-overlay-payment",
      "target": "capability-change-overlay-payment-process",
      "label": "实例组成：校验客户身份",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-change-overlay-payment-app-composition",
      "type": "instance_comprises",
      "source": "capability-change-overlay-payment",
      "target": "capability-change-overlay-payment-app",
      "label": "实例组成：客户身份服务",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-change-overlay-payment-info-composition",
      "type": "instance_comprises",
      "source": "capability-change-overlay-payment",
      "target": "capability-change-overlay-payment-info",
      "label": "实例组成：客户身份信息",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-capability-change-overlay",
    "artifact_id": "capability-increment-analysis",
    "profile_id": "capability-change-overlay",
    "title": "能力变更叠加图／虚构案例",
    "entity_ids": [
      "capability-change-overlay-type",
      "capability-change-overlay-select",
      "capability-change-overlay-buy",
      "capability-change-overlay-browse",
      "capability-change-overlay-browse-role",
      "capability-change-overlay-browse-process",
      "capability-change-overlay-browse-app",
      "capability-change-overlay-browse-info",
      "capability-change-overlay-payment",
      "capability-change-overlay-payment-role",
      "capability-change-overlay-payment-process",
      "capability-change-overlay-payment-app",
      "capability-change-overlay-payment-info"
    ],
    "relationship_ids": [
      "capability-change-overlay-next",
      "capability-change-overlay-browse-type",
      "capability-change-overlay-browse-stage",
      "capability-change-overlay-browse-role-composition",
      "capability-change-overlay-browse-process-composition",
      "capability-change-overlay-browse-app-composition",
      "capability-change-overlay-browse-info-composition",
      "capability-change-overlay-payment-type",
      "capability-change-overlay-payment-stage",
      "capability-change-overlay-payment-role-composition",
      "capability-change-overlay-payment-process-composition",
      "capability-change-overlay-payment-app-composition",
      "capability-change-overlay-payment-info-composition"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile capability-change-overlay --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile capability-change-overlay --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
