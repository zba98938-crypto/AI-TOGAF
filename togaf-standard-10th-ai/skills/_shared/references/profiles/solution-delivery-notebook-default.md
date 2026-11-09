# 解决方案交付笔记本

`profile_id`: solution-delivery-notebook-default；`artifact_id`: solution-delivery-notebook；主责：[togaf-implementation-governance](../../../togaf-implementation-governance/SKILL.md)。

来源：G186 附录D 表D-1。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：1.0。

{
  "id": "solution-delivery-notebook-default",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "按工作产品字段组织的记录表；来源无对应原图。",
  "structure_basis": "正文定义的工作产品；记录表是项目操作表示法，不冒充来源原图"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:solution-delivery-notebook。关系类型：。

```json
{
  "entities": {
    "guide:solution-delivery-notebook": [
      "work_package_id",
      "solution_concept_ref",
      "implementation_strategy",
      "stakeholders",
      "requirements",
      "specifications",
      "risks",
      "controls",
      "gaps",
      "architecture_summary"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 对象、关系、必要属性均可追溯并得到表达
- 参考内容不自动成为项目事实；未知项保持显式
- 规格总追溯到某项需求
- 控制总追溯到某项风险
- 架构描述摘要仅供参考，不替代规格
- 笔记本是交付沟通模板，不代表合同已签署

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构星河零售教学案例；规则不是TOGAF规定，不代表批准。",
  "sources": [
    {
      "id": "SDN-R1",
      "kind": "example",
      "description": "虚构工作包WP-7“门店自提”：处理差距G-1（无自提预约）；G-2（退货流程）不在本工作包。",
      "locator": "raw-materials.json#SDN-R1"
    },
    {
      "id": "SDN-R2",
      "kind": "example",
      "description": "门店运营要求自提预约准确率≥99%（R-ACC），法务要求只显示脱敏手机号（R-PRIV）；风险RK-1为预约超卖。",
      "locator": "raw-materials.json#SDN-R2"
    },
    {
      "id": "SDN-R3",
      "kind": "example",
      "description": "规格S-1：预约须通过库存服务锁定；S-2：前台仅读取脱敏视图。控制C-1：锁定失败时禁止确认预约。",
      "locator": "raw-materials.json#SDN-R3"
    }
  ],
  "entities": [
    {
      "id": "SDN-WP7",
      "type": "guide:solution-delivery-notebook",
      "name": "解决方案交付笔记本：门店自提",
      "attributes": {
        "work_package_id": "WP-7",
        "solution_concept_ref": "v-solution-concept-pickup",
        "implementation_strategy": "先在两家门店试点，再分批推广",
        "stakeholders": [
          {
            "id": "SH-OPS",
            "name": "门店运营",
            "requirement_ids": [
              "R-ACC"
            ]
          },
          {
            "id": "SH-LEGAL",
            "name": "法务",
            "requirement_ids": [
              "R-PRIV"
            ]
          }
        ],
        "requirements": [
          {
            "id": "R-ACC",
            "statement": "自提预约准确率≥99%",
            "stakeholder_ids": [
              "SH-OPS"
            ]
          },
          {
            "id": "R-PRIV",
            "statement": "前台只显示脱敏手机号",
            "stakeholder_ids": [
              "SH-LEGAL"
            ]
          }
        ],
        "specifications": [
          {
            "id": "S-1",
            "requirement_id": "R-ACC",
            "statement": "预约通过库存服务锁定",
            "spec_type": "接口规格",
            "applies_to": "自提预约服务"
          },
          {
            "id": "S-2",
            "requirement_id": "R-PRIV",
            "statement": "前台只读脱敏视图",
            "spec_type": "数据访问规格",
            "applies_to": "门店前台应用"
          }
        ],
        "risks": [
          {
            "id": "RK-1",
            "description": "预约超卖导致到店无货"
          }
        ],
        "controls": [
          {
            "id": "C-1",
            "risk_id": "RK-1",
            "statement": "锁定失败时禁止确认预约",
            "applies_to": "自提预约服务"
          }
        ],
        "gaps": [
          {
            "id": "G-1",
            "description": "无自提预约能力",
            "in_scope": true
          },
          {
            "id": "G-2",
            "description": "退货流程未覆盖自提订单",
            "in_scope": false
          }
        ],
        "architecture_summary": {
          "business": {
            "view_ids": [
              "v-process-pickup"
            ]
          },
          "information": {
            "view_ids": [
              "v-data-reservation"
            ]
          },
          "application": {
            "view_ids": [
              "v-app-communication-pickup"
            ]
          },
          "infrastructure": {
            "not_applicable_reason": "沿用现有平台，无基础设施变化"
          },
          "security": {
            "view_ids": [
              "v-data-security-pickup"
            ]
          }
        }
      },
      "evidence": [
        "SDN-R1",
        "SDN-R2",
        "SDN-R3"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "solution-delivery-notebook-baseline",
    "artifact_id": "solution-delivery-notebook",
    "profile_id": "solution-delivery-notebook-default",
    "title": "解决方案交付笔记本／虚构星河零售",
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
      "SDN-WP7"
    ],
    "relationship_ids": [],
    "analysis": "从随包虚构原料提取字段，执行solution-delivery-notebook-review；规则为项目操作约定。",
    "legend": "虚构示例；同一ID在修改前后代表同一对象；嵌套记录按表可见。",
    "attributes": {
      "analysis_ids": [
        "solution-delivery-notebook-analysis"
      ]
    }
  },
  "analyses": [
    {
      "id": "solution-delivery-notebook-analysis",
      "method_id": "solution-delivery-notebook-review",
      "inputs": {
        "id": "SDN-WP7",
        "name": "解决方案交付笔记本：门店自提",
        "work_package_id": "WP-7",
        "solution_concept_ref": "v-solution-concept-pickup",
        "implementation_strategy": "先在两家门店试点，再分批推广",
        "stakeholders": [
          {
            "id": "SH-OPS",
            "name": "门店运营",
            "requirement_ids": [
              "R-ACC"
            ]
          },
          {
            "id": "SH-LEGAL",
            "name": "法务",
            "requirement_ids": [
              "R-PRIV"
            ]
          }
        ],
        "requirements": [
          {
            "id": "R-ACC",
            "statement": "自提预约准确率≥99%",
            "stakeholder_ids": [
              "SH-OPS"
            ]
          },
          {
            "id": "R-PRIV",
            "statement": "前台只显示脱敏手机号",
            "stakeholder_ids": [
              "SH-LEGAL"
            ]
          }
        ],
        "specifications": [
          {
            "id": "S-1",
            "requirement_id": "R-ACC",
            "statement": "预约通过库存服务锁定",
            "spec_type": "接口规格",
            "applies_to": "自提预约服务"
          },
          {
            "id": "S-2",
            "requirement_id": "R-PRIV",
            "statement": "前台只读脱敏视图",
            "spec_type": "数据访问规格",
            "applies_to": "门店前台应用"
          }
        ],
        "risks": [
          {
            "id": "RK-1",
            "description": "预约超卖导致到店无货"
          }
        ],
        "controls": [
          {
            "id": "C-1",
            "risk_id": "RK-1",
            "statement": "锁定失败时禁止确认预约",
            "applies_to": "自提预约服务"
          }
        ],
        "gaps": [
          {
            "id": "G-1",
            "description": "无自提预约能力",
            "in_scope": true
          },
          {
            "id": "G-2",
            "description": "退货流程未覆盖自提订单",
            "in_scope": false
          }
        ],
        "architecture_summary": {
          "business": {
            "view_ids": [
              "v-process-pickup"
            ]
          },
          "information": {
            "view_ids": [
              "v-data-reservation"
            ]
          },
          "application": {
            "view_ids": [
              "v-app-communication-pickup"
            ]
          },
          "infrastructure": {
            "not_applicable_reason": "沿用现有平台，无基础设施变化"
          },
          "security": {
            "view_ids": [
              "v-data-security-pickup"
            ]
          }
        },
        "evidence": [
          "SDN-R1",
          "SDN-R2",
          "SDN-R3"
        ],
        "source_ids": [
          "SDN-R1",
          "SDN-R2",
          "SDN-R3"
        ]
      }
    }
  ]
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile solution-delivery-notebook-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile solution-delivery-notebook-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
