# 产品边界与企业约束登记

`profile_id`: product-constraint-register-default；`artifact_id`: product-constraint-register；主责：[togaf-implementation-governance](../../../togaf-implementation-governance/SKILL.md)。

来源：G186 §12.1。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：1.0。

{
  "id": "product-constraint-register-default",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "按工作产品字段组织的记录表；来源无对应原图。",
  "structure_basis": "正文定义的工作产品；记录表是项目操作表示法，不冒充来源原图"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:product-constraint-register。关系类型：。

```json
{
  "entities": {
    "guide:product-constraint-register": [
      "products",
      "constraints",
      "backlog_items",
      "dispensations"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 对象、关系、必要属性均可追溯并得到表达
- 参考内容不自动成为项目事实；未知项保持显式
- 敏捷对齐落在阶段G；不把ADM各阶段改写成冲刺
- 产品负责人的局部偏好不能越过企业约束
- 豁免须有权限方、理由、到期日与证据

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

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

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile product-constraint-register-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile product-constraint-register-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
