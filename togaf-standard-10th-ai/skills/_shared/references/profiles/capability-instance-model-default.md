# 能力实例组成模型

`profile_id`: capability-instance-model-default；`artifact_id`: capability-instance-model；主责：[togaf-strategy-capabilities](../../../togaf-strategy-capabilities/SKILL.md)。

来源：G233 §6.4；图6-3。

## 构图与定义状态

表示族：`stage-map`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
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

- 同一能力的多个实例不等于多个新能力或子能力
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

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
      "id": "capability-instance-model-default-type",
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
      "id": "capability-instance-model-default-select",
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
      "id": "capability-instance-model-default-buy",
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
      "id": "capability-instance-model-default-browse",
      "type": "capability_instance",
      "name": "客户身份管理：选择阶段",
      "attributes": {
        "definition": "在该阶段按对应安全和体验要求实现客户身份管理",
        "stage_id": "capability-instance-model-default-select",
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
      "id": "capability-instance-model-default-browse-role",
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
      "id": "capability-instance-model-default-browse-process",
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
      "id": "capability-instance-model-default-browse-app",
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
      "id": "capability-instance-model-default-browse-info",
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
      "id": "capability-instance-model-default-payment",
      "type": "capability_instance",
      "name": "客户身份管理：购买阶段",
      "attributes": {
        "definition": "在该阶段按对应安全和体验要求实现客户身份管理",
        "stage_id": "capability-instance-model-default-buy",
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
      "id": "capability-instance-model-default-payment-role",
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
      "id": "capability-instance-model-default-payment-process",
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
      "id": "capability-instance-model-default-payment-app",
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
      "id": "capability-instance-model-default-payment-info",
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
      "id": "capability-instance-model-default-next",
      "type": "precedes",
      "source": "capability-instance-model-default-select",
      "target": "capability-instance-model-default-buy",
      "label": "选择后进入购买",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-instance-model-default-browse-type",
      "type": "instance_of",
      "source": "capability-instance-model-default-browse",
      "target": "capability-instance-model-default-type",
      "label": "实例属于客户身份管理能力类型",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-instance-model-default-browse-stage",
      "type": "stage_uses_instance",
      "source": "capability-instance-model-default-select",
      "target": "capability-instance-model-default-browse",
      "label": "阶段由该身份实例使能",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-instance-model-default-browse-role-composition",
      "type": "instance_comprises",
      "source": "capability-instance-model-default-browse",
      "target": "capability-instance-model-default-browse-role",
      "label": "实例组成：客户服务角色",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-instance-model-default-browse-process-composition",
      "type": "instance_comprises",
      "source": "capability-instance-model-default-browse",
      "target": "capability-instance-model-default-browse-process",
      "label": "实例组成：校验客户身份",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-instance-model-default-browse-app-composition",
      "type": "instance_comprises",
      "source": "capability-instance-model-default-browse",
      "target": "capability-instance-model-default-browse-app",
      "label": "实例组成：客户身份服务",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-instance-model-default-browse-info-composition",
      "type": "instance_comprises",
      "source": "capability-instance-model-default-browse",
      "target": "capability-instance-model-default-browse-info",
      "label": "实例组成：客户身份信息",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-instance-model-default-payment-type",
      "type": "instance_of",
      "source": "capability-instance-model-default-payment",
      "target": "capability-instance-model-default-type",
      "label": "实例属于客户身份管理能力类型",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-instance-model-default-payment-stage",
      "type": "stage_uses_instance",
      "source": "capability-instance-model-default-buy",
      "target": "capability-instance-model-default-payment",
      "label": "阶段由该身份实例使能",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-instance-model-default-payment-role-composition",
      "type": "instance_comprises",
      "source": "capability-instance-model-default-payment",
      "target": "capability-instance-model-default-payment-role",
      "label": "实例组成：客户服务角色",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-instance-model-default-payment-process-composition",
      "type": "instance_comprises",
      "source": "capability-instance-model-default-payment",
      "target": "capability-instance-model-default-payment-process",
      "label": "实例组成：校验客户身份",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-instance-model-default-payment-app-composition",
      "type": "instance_comprises",
      "source": "capability-instance-model-default-payment",
      "target": "capability-instance-model-default-payment-app",
      "label": "实例组成：客户身份服务",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-instance-model-default-payment-info-composition",
      "type": "instance_comprises",
      "source": "capability-instance-model-default-payment",
      "target": "capability-instance-model-default-payment-info",
      "label": "实例组成：客户身份信息",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-capability-instance-model-default",
    "artifact_id": "capability-instance-model",
    "profile_id": "capability-instance-model-default",
    "title": "能力实例组成模型／虚构案例",
    "entity_ids": [
      "capability-instance-model-default-type",
      "capability-instance-model-default-select",
      "capability-instance-model-default-buy",
      "capability-instance-model-default-browse",
      "capability-instance-model-default-browse-role",
      "capability-instance-model-default-browse-process",
      "capability-instance-model-default-browse-app",
      "capability-instance-model-default-browse-info",
      "capability-instance-model-default-payment",
      "capability-instance-model-default-payment-role",
      "capability-instance-model-default-payment-process",
      "capability-instance-model-default-payment-app",
      "capability-instance-model-default-payment-info"
    ],
    "relationship_ids": [
      "capability-instance-model-default-next",
      "capability-instance-model-default-browse-type",
      "capability-instance-model-default-browse-stage",
      "capability-instance-model-default-browse-role-composition",
      "capability-instance-model-default-browse-process-composition",
      "capability-instance-model-default-browse-app-composition",
      "capability-instance-model-default-browse-info-composition",
      "capability-instance-model-default-payment-type",
      "capability-instance-model-default-payment-stage",
      "capability-instance-model-default-payment-role-composition",
      "capability-instance-model-default-payment-process-composition",
      "capability-instance-model-default-payment-app-composition",
      "capability-instance-model-default-payment-info-composition"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile capability-instance-model-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile capability-instance-model-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
