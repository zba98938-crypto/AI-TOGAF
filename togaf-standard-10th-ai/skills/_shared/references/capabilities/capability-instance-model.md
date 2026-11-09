# 能力实例组成模型

ID：`capability-instance-model`。主责：[togaf-strategy-capabilities](../../../togaf-strategy-capabilities/SKILL.md)。

来源：G233 §6.4；图6-3。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

某阶段由什么具体组成实现能力？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 某阶段由什么具体组成实现能力？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- capability_type
- stage
- role

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：application, capability, capability_instance, information, process, role, value_stage。

```json
{
  "capability": [
    "definition"
  ],
  "capability_instance": [
    "definition",
    "stage_id"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "capability_type": {
    "meaning": "被实例化的能力类型标识",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "stage": {
    "meaning": "价值流阶段引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "role": {
    "meaning": "承担职责的角色",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "process": {
    "meaning": "业务流程或行为引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "application": {
    "meaning": "支撑应用引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "information": {
    "meaning": "被使用或修改的信息引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "definition": {
    "meaning": "业务含义和排除边界",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "stage_id": {
    "meaning": "在本工作产品范围中明确定义的 stage_id 属性",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `instance_comprises` | capability_instance → role,actor,process,business_process,application,application_component,application_process,business_object,data_object,information,data_entity,technology | 实例的实现组成 |
| `instance_of` | capability_instance → capability | 实例属于稳定能力类型 |
| `precedes` | value_stage,customer_journey_stage → value_stage,customer_journey_stage | 同一价值流或客户旅程内阶段的先后；旅程阶段的先后是体验次序，不是流程控制流，也不跨价值流与旅程连接。 |
| `stage_uses_instance` | value_stage → capability_instance | 阶段由特定能力实例使能 |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 从价值阶段识别能力使用语境
2. 引用能力类型
3. 描述实例的人员流程应用和对象
4. 校核跨实例信息流

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 同一能力的多个实例不等于多个新能力或子能力
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 同一能力的多个实例不等于多个新能力或子能力


## 视图和交付物

- [能力实例组成模型](../profiles/capability-instance-model-default.md)
- [能力实例组成图](../profiles/capability-instance-composition.md)

- [capability-assessment](../deliverables/capability-assessment.md)
- [architecture-roadmaps](../deliverables/architecture-roadmaps.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「能力实例组成模型」给出：同一能力的多个实例不等于多个新能力或子能力",
    "expected": "missing-evidence",
    "why": "同一能力的多个实例不等于多个新能力或子能力"
  },
  "modification_example": {
    "change": "在「能力实例组成模型」的范围内新增或修改一项，检查下游是否随之变化",
    "expected": "受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用"
  }
}
```

## 可编辑示例与调用



以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

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

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact capability-instance-model --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
