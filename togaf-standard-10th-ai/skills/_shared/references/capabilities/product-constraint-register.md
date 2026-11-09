# 产品边界与企业约束登记

ID：`product-constraint-register`。主责：[togaf-implementation-governance](../../../togaf-implementation-governance/SKILL.md)。

来源：G186 §12.1。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

架构定义了哪些产品、边界与产品负责人约束，哪些待办项与约束冲突，是否有阶段G豁免？

- 该范围业务负责人
- 架构师
- 评审及治理负责人
- 架构定义了哪些产品、边界与产品负责人约束，哪些待办项与约束冲突，是否有阶段G豁免？
- 来源、范围与适用性


## 输入及缺口处理

必需：

- {'id': 'products', 'meaning': '产品、边界、产品负责人及架构依据', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'constraints', 'meaning': '对产品的企业约束及架构依据', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'backlog_items', 'meaning': '产品待办项及冲突约束', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'dispensations', 'meaning': '阶段G豁免：约束、权限、理由、到期日与证据', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'purpose', 'meaning': '本登记的用途与范围说明', 'origin': 'source-purpose-plus-project-contract'}

可选：

- 既有模型及历史结论

关键输入缺失时生成带ID的草稿与缺口，不计算无依据数值，不伪造批准或事实；结构错误直接拒绝。

## 元素、属性与关系

对象类型：guide:product-constraint-register。

```json
{
  "guide:product-constraint-register": [
    "products",
    "constraints",
    "backlog_items",
    "dispensations"
  ]
}
```

{
  "products": {
    "meaning": "产品、边界、产品负责人及架构依据",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "constraints": {
    "meaning": "对产品的企业约束及架构依据",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "backlog_items": {
    "meaning": "产品待办项及冲突约束",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "dispensations": {
    "meaning": "阶段G豁免：约束、权限、理由、到期日与证据",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "purpose": {
    "meaning": "本登记的用途与范围说明",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 从组合或项目架构列出产品、边界与产品负责人
2. 登记对产品的企业约束及架构依据
3. 标记与约束冲突的待办项
4. 冲突项只有在阶段G有证据豁免时放行，否则阻止
5. 豁免到期前复核

## 输出、检查与误读

- 范围及依据
- 逐条结果与理由
- 缺口、下一步与责任
- 版本和来源引用

- 敏捷对齐落在阶段G；不把ADM各阶段改写成冲刺
- 产品负责人的局部偏好不能越过企业约束
- 豁免须有权限方、理由、到期日与证据

- 名称、来源表格和成功输出不等于业务结论已核实
- 敏捷对齐落在阶段G；不把ADM各阶段改写成冲刺
- 产品负责人的局部偏好不能越过企业约束
- 豁免须有权限方、理由、到期日与证据


## 视图和交付物

- [产品边界与企业约束登记](../profiles/product-constraint-register-default.md)

- [architecture-contract](../deliverables/architecture-contract.md)
- [compliance-assessment](../deliverables/compliance-assessment.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "待办B-3引用另一产品的约束",
    "expected": "PCC-004",
    "why": "PCC-004 [B-3]: Constraint belongs to another product"
  },
  "modification_example": {
    "change": "为B-3补记有证据的豁免D-1",
    "expected": "分析结果变化：blocked_item_ids：[\"B-3\"]→[]"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/product-constraint-register.md)
[完整操作案例](../../references/capability-addenda/product-constraint-register.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

```json
{
  "notice": "虚构星河零售教学案例；规则不是TOGAF规定，不代表批准。",
  "sources": [
    {
      "id": "PCC-R1",
      "kind": "example",
      "description": "虚构架构定义：订单服务边界含下单与支付确认，产品负责人李某；库存预占只能经库存服务（约束K-1）。",
      "locator": "raw-materials.json#PCC-R1"
    },
    {
      "id": "PCC-R2",
      "kind": "example",
      "description": "促销团队待办B-3要求直接写库存表以加快秒杀；B-4同样冲突，但架构委员会已于10月批准临时豁免D-1至2027-01-31。",
      "locator": "raw-materials.json#PCC-R2"
    }
  ],
  "entities": [
    {
      "id": "PCC-REG",
      "type": "guide:product-constraint-register",
      "name": "产品边界与约束登记：订单与促销",
      "attributes": {
        "purpose": "登记订单与促销产品的企业约束、冲突待办与阶段G豁免",
        "products": [
          {
            "id": "P-ORDER",
            "name": "订单服务",
            "boundary": "下单与支付确认",
            "product_owner": "李某",
            "architecture_ref": "v-app-portfolio",
            "evidence": [
              "PCC-R1"
            ]
          },
          {
            "id": "P-PROMO",
            "name": "促销引擎",
            "boundary": "价格与券规则",
            "product_owner": "王某",
            "architecture_ref": "v-app-portfolio",
            "evidence": [
              "PCC-R1"
            ]
          }
        ],
        "constraints": [
          {
            "id": "K-1",
            "product_id": "P-PROMO",
            "statement": "库存预占只能经库存服务",
            "architecture_ref": "S-1",
            "evidence": [
              "PCC-R1"
            ]
          }
        ],
        "backlog_items": [
          {
            "id": "B-3",
            "product_id": "P-PROMO",
            "title": "秒杀直接写库存表",
            "conflicts_with": [
              "K-1"
            ]
          },
          {
            "id": "B-4",
            "product_id": "P-PROMO",
            "title": "大促预热直接写库存表",
            "conflicts_with": [
              "K-1"
            ],
            "dispensation_id": "D-1"
          }
        ],
        "dispensations": [
          {
            "id": "D-1",
            "constraint_ids": [
              "K-1"
            ],
            "authority": "架构委员会",
            "rationale": "库存服务扩容前的临时安排",
            "expiry": "2027-01-31",
            "evidence": [
              "PCC-R2"
            ]
          }
        ]
      },
      "evidence": [
        "PCC-R1",
        "PCC-R2"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "product-constraint-register-baseline",
    "artifact_id": "product-constraint-register",
    "profile_id": "product-constraint-register-default",
    "title": "产品边界与企业约束登记／虚构星河零售",
    "context": {
      "domains": [
        "business",
        "data",
        "application",
        "technology"
      ],
      "landscape": "segment",
      "purpose": "project",
      "abstraction": "logical",
      "evolution": "target"
    },
    "entity_ids": [
      "PCC-REG"
    ],
    "relationship_ids": [],
    "analysis": "从随包虚构原料提取字段，执行product-constraint-conformance-review；规则为项目操作约定。",
    "legend": "虚构示例；同一ID在修改前后代表同一对象；嵌套记录按表可见。",
    "attributes": {
      "analysis_ids": [
        "product-constraint-register-analysis"
      ]
    }
  },
  "analyses": [
    {
      "id": "product-constraint-register-analysis",
      "method_id": "product-constraint-conformance-review",
      "inputs": {
        "name": "产品边界与约束登记：订单与促销",
        "purpose": "登记订单与促销产品的企业约束、冲突待办与阶段G豁免",
        "products": [
          {
            "id": "P-ORDER",
            "name": "订单服务",
            "boundary": "下单与支付确认",
            "product_owner": "李某",
            "architecture_ref": "v-app-portfolio",
            "evidence": [
              "PCC-R1"
            ]
          },
          {
            "id": "P-PROMO",
            "name": "促销引擎",
            "boundary": "价格与券规则",
            "product_owner": "王某",
            "architecture_ref": "v-app-portfolio",
            "evidence": [
              "PCC-R1"
            ]
          }
        ],
        "constraints": [
          {
            "id": "K-1",
            "product_id": "P-PROMO",
            "statement": "库存预占只能经库存服务",
            "architecture_ref": "S-1",
            "evidence": [
              "PCC-R1"
            ]
          }
        ],
        "backlog_items": [
          {
            "id": "B-3",
            "product_id": "P-PROMO",
            "title": "秒杀直接写库存表",
            "conflicts_with": [
              "K-1"
            ]
          },
          {
            "id": "B-4",
            "product_id": "P-PROMO",
            "title": "大促预热直接写库存表",
            "conflicts_with": [
              "K-1"
            ],
            "dispensation_id": "D-1"
          }
        ],
        "dispensations": [
          {
            "id": "D-1",
            "constraint_ids": [
              "K-1"
            ],
            "authority": "架构委员会",
            "rationale": "库存服务扩容前的临时安排",
            "expiry": "2027-01-31",
            "evidence": [
              "PCC-R2"
            ]
          }
        ],
        "source_ids": [
          "PCC-R1",
          "PCC-R2"
        ]
      }
    }
  ]
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact product-constraint-register --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
