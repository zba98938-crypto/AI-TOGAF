# 能力实例组成图

`profile_id`: capability-instance-composition；`artifact_id`: capability-instance-model；主责：[togaf-strategy-capabilities](../../../togaf-strategy-capabilities/SKILL.md)。

来源：G233/fig6-3。

## 构图与定义状态

表示族：`stage-map`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "source_figure": "G233/fig6-3",
  "layout_notes": "实例组成、能力类型、阶段顺序与跨实例信息流分开",
  "review_status": "source-located-awaiting-template-validation",
  "verification_evidence": "reviews/source-verification/capability-instance-composition.json",
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

- 实例组成、能力类型、阶段顺序与跨实例信息流分开

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
      "id": "capability-instance-composition-type",
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
      "id": "capability-instance-composition-select",
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
      "id": "capability-instance-composition-buy",
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
      "id": "capability-instance-composition-browse",
      "type": "capability_instance",
      "name": "客户身份管理：选择阶段",
      "attributes": {
        "definition": "在该阶段按对应安全和体验要求实现客户身份管理",
        "stage_id": "capability-instance-composition-select",
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
      "id": "capability-instance-composition-browse-role",
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
      "id": "capability-instance-composition-browse-process",
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
      "id": "capability-instance-composition-browse-app",
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
      "id": "capability-instance-composition-browse-info",
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
      "id": "capability-instance-composition-payment",
      "type": "capability_instance",
      "name": "客户身份管理：购买阶段",
      "attributes": {
        "definition": "在该阶段按对应安全和体验要求实现客户身份管理",
        "stage_id": "capability-instance-composition-buy",
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
      "id": "capability-instance-composition-payment-role",
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
      "id": "capability-instance-composition-payment-process",
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
      "id": "capability-instance-composition-payment-app",
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
      "id": "capability-instance-composition-payment-info",
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
      "id": "capability-instance-composition-next",
      "type": "precedes",
      "source": "capability-instance-composition-select",
      "target": "capability-instance-composition-buy",
      "label": "选择后进入购买",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-instance-composition-browse-type",
      "type": "instance_of",
      "source": "capability-instance-composition-browse",
      "target": "capability-instance-composition-type",
      "label": "实例属于客户身份管理能力类型",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-instance-composition-browse-stage",
      "type": "stage_uses_instance",
      "source": "capability-instance-composition-select",
      "target": "capability-instance-composition-browse",
      "label": "阶段由该身份实例使能",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-instance-composition-browse-role-composition",
      "type": "instance_comprises",
      "source": "capability-instance-composition-browse",
      "target": "capability-instance-composition-browse-role",
      "label": "实例组成：客户服务角色",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-instance-composition-browse-process-composition",
      "type": "instance_comprises",
      "source": "capability-instance-composition-browse",
      "target": "capability-instance-composition-browse-process",
      "label": "实例组成：校验客户身份",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-instance-composition-browse-app-composition",
      "type": "instance_comprises",
      "source": "capability-instance-composition-browse",
      "target": "capability-instance-composition-browse-app",
      "label": "实例组成：客户身份服务",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-instance-composition-browse-info-composition",
      "type": "instance_comprises",
      "source": "capability-instance-composition-browse",
      "target": "capability-instance-composition-browse-info",
      "label": "实例组成：客户身份信息",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-instance-composition-payment-type",
      "type": "instance_of",
      "source": "capability-instance-composition-payment",
      "target": "capability-instance-composition-type",
      "label": "实例属于客户身份管理能力类型",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-instance-composition-payment-stage",
      "type": "stage_uses_instance",
      "source": "capability-instance-composition-buy",
      "target": "capability-instance-composition-payment",
      "label": "阶段由该身份实例使能",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-instance-composition-payment-role-composition",
      "type": "instance_comprises",
      "source": "capability-instance-composition-payment",
      "target": "capability-instance-composition-payment-role",
      "label": "实例组成：客户服务角色",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-instance-composition-payment-process-composition",
      "type": "instance_comprises",
      "source": "capability-instance-composition-payment",
      "target": "capability-instance-composition-payment-process",
      "label": "实例组成：校验客户身份",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-instance-composition-payment-app-composition",
      "type": "instance_comprises",
      "source": "capability-instance-composition-payment",
      "target": "capability-instance-composition-payment-app",
      "label": "实例组成：客户身份服务",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-instance-composition-payment-info-composition",
      "type": "instance_comprises",
      "source": "capability-instance-composition-payment",
      "target": "capability-instance-composition-payment-info",
      "label": "实例组成：客户身份信息",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-capability-instance-composition",
    "artifact_id": "capability-instance-model",
    "profile_id": "capability-instance-composition",
    "title": "能力实例组成图／虚构案例",
    "entity_ids": [
      "capability-instance-composition-type",
      "capability-instance-composition-select",
      "capability-instance-composition-buy",
      "capability-instance-composition-browse",
      "capability-instance-composition-browse-role",
      "capability-instance-composition-browse-process",
      "capability-instance-composition-browse-app",
      "capability-instance-composition-browse-info",
      "capability-instance-composition-payment",
      "capability-instance-composition-payment-role",
      "capability-instance-composition-payment-process",
      "capability-instance-composition-payment-app",
      "capability-instance-composition-payment-info"
    ],
    "relationship_ids": [
      "capability-instance-composition-next",
      "capability-instance-composition-browse-type",
      "capability-instance-composition-browse-stage",
      "capability-instance-composition-browse-role-composition",
      "capability-instance-composition-browse-process-composition",
      "capability-instance-composition-browse-app-composition",
      "capability-instance-composition-browse-info-composition",
      "capability-instance-composition-payment-type",
      "capability-instance-composition-payment-stage",
      "capability-instance-composition-payment-role-composition",
      "capability-instance-composition-payment-process-composition",
      "capability-instance-composition-payment-app-composition",
      "capability-instance-composition-payment-info-composition"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile capability-instance-composition --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile capability-instance-composition --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
