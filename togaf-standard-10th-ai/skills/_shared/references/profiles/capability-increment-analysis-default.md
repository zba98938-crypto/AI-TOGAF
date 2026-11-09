# 能力增量分析

`profile_id`: capability-increment-analysis-default；`artifact_id`: capability-increment-analysis；主责：[togaf-gap-solutions](../../../togaf-gap-solutions/SKILL.md)。

来源：G233 §7.1–7.2；图7-1、7-2。

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

- 绿色不等于已实现或高成熟度，新建改进退役标签与颜色分开记录
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
      "id": "capability-increment-analysis-default-type",
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
      "id": "capability-increment-analysis-default-select",
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
      "id": "capability-increment-analysis-default-buy",
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
      "id": "capability-increment-analysis-default-browse",
      "type": "capability_instance",
      "name": "客户身份管理：选择阶段",
      "attributes": {
        "definition": "在该阶段按对应安全和体验要求实现客户身份管理",
        "stage_id": "capability-increment-analysis-default-select",
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
      "id": "capability-increment-analysis-default-browse-role",
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
      "id": "capability-increment-analysis-default-browse-process",
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
      "id": "capability-increment-analysis-default-browse-app",
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
      "id": "capability-increment-analysis-default-browse-info",
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
      "id": "capability-increment-analysis-default-payment",
      "type": "capability_instance",
      "name": "客户身份管理：购买阶段",
      "attributes": {
        "definition": "在该阶段按对应安全和体验要求实现客户身份管理",
        "stage_id": "capability-increment-analysis-default-buy",
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
      "id": "capability-increment-analysis-default-payment-role",
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
      "id": "capability-increment-analysis-default-payment-process",
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
      "id": "capability-increment-analysis-default-payment-app",
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
      "id": "capability-increment-analysis-default-payment-info",
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
      "id": "capability-increment-analysis-default-next",
      "type": "precedes",
      "source": "capability-increment-analysis-default-select",
      "target": "capability-increment-analysis-default-buy",
      "label": "选择后进入购买",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-increment-analysis-default-browse-type",
      "type": "instance_of",
      "source": "capability-increment-analysis-default-browse",
      "target": "capability-increment-analysis-default-type",
      "label": "实例属于客户身份管理能力类型",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-increment-analysis-default-browse-stage",
      "type": "stage_uses_instance",
      "source": "capability-increment-analysis-default-select",
      "target": "capability-increment-analysis-default-browse",
      "label": "阶段由该身份实例使能",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-increment-analysis-default-browse-role-composition",
      "type": "instance_comprises",
      "source": "capability-increment-analysis-default-browse",
      "target": "capability-increment-analysis-default-browse-role",
      "label": "实例组成：客户服务角色",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-increment-analysis-default-browse-process-composition",
      "type": "instance_comprises",
      "source": "capability-increment-analysis-default-browse",
      "target": "capability-increment-analysis-default-browse-process",
      "label": "实例组成：校验客户身份",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-increment-analysis-default-browse-app-composition",
      "type": "instance_comprises",
      "source": "capability-increment-analysis-default-browse",
      "target": "capability-increment-analysis-default-browse-app",
      "label": "实例组成：客户身份服务",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-increment-analysis-default-browse-info-composition",
      "type": "instance_comprises",
      "source": "capability-increment-analysis-default-browse",
      "target": "capability-increment-analysis-default-browse-info",
      "label": "实例组成：客户身份信息",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-increment-analysis-default-payment-type",
      "type": "instance_of",
      "source": "capability-increment-analysis-default-payment",
      "target": "capability-increment-analysis-default-type",
      "label": "实例属于客户身份管理能力类型",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-increment-analysis-default-payment-stage",
      "type": "stage_uses_instance",
      "source": "capability-increment-analysis-default-buy",
      "target": "capability-increment-analysis-default-payment",
      "label": "阶段由该身份实例使能",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-increment-analysis-default-payment-role-composition",
      "type": "instance_comprises",
      "source": "capability-increment-analysis-default-payment",
      "target": "capability-increment-analysis-default-payment-role",
      "label": "实例组成：客户服务角色",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-increment-analysis-default-payment-process-composition",
      "type": "instance_comprises",
      "source": "capability-increment-analysis-default-payment",
      "target": "capability-increment-analysis-default-payment-process",
      "label": "实例组成：校验客户身份",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-increment-analysis-default-payment-app-composition",
      "type": "instance_comprises",
      "source": "capability-increment-analysis-default-payment",
      "target": "capability-increment-analysis-default-payment-app",
      "label": "实例组成：客户身份服务",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "capability-increment-analysis-default-payment-info-composition",
      "type": "instance_comprises",
      "source": "capability-increment-analysis-default-payment",
      "target": "capability-increment-analysis-default-payment-info",
      "label": "实例组成：客户身份信息",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-capability-increment-analysis-default",
    "artifact_id": "capability-increment-analysis",
    "profile_id": "capability-increment-analysis-default",
    "title": "能力增量分析／虚构案例",
    "entity_ids": [
      "capability-increment-analysis-default-type",
      "capability-increment-analysis-default-select",
      "capability-increment-analysis-default-buy",
      "capability-increment-analysis-default-browse",
      "capability-increment-analysis-default-browse-role",
      "capability-increment-analysis-default-browse-process",
      "capability-increment-analysis-default-browse-app",
      "capability-increment-analysis-default-browse-info",
      "capability-increment-analysis-default-payment",
      "capability-increment-analysis-default-payment-role",
      "capability-increment-analysis-default-payment-process",
      "capability-increment-analysis-default-payment-app",
      "capability-increment-analysis-default-payment-info"
    ],
    "relationship_ids": [
      "capability-increment-analysis-default-next",
      "capability-increment-analysis-default-browse-type",
      "capability-increment-analysis-default-browse-stage",
      "capability-increment-analysis-default-browse-role-composition",
      "capability-increment-analysis-default-browse-process-composition",
      "capability-increment-analysis-default-browse-app-composition",
      "capability-increment-analysis-default-browse-info-composition",
      "capability-increment-analysis-default-payment-type",
      "capability-increment-analysis-default-payment-stage",
      "capability-increment-analysis-default-payment-role-composition",
      "capability-increment-analysis-default-payment-process-composition",
      "capability-increment-analysis-default-payment-app-composition",
      "capability-increment-analysis-default-payment-info-composition"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile capability-increment-analysis-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile capability-increment-analysis-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
