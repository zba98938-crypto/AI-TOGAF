# 解决方案交付笔记本

ID：`solution-delivery-notebook`。主责：[togaf-implementation-governance](../../../togaf-implementation-governance/SKILL.md)。

来源：G186 附录D 表D-1。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

交付团队据以设计和测试的需求/规格、风险/控制配对、差距范围与目标架构摘要是什么？

- 该范围业务负责人
- 架构师
- 评审及治理负责人
- 交付团队据以设计和测试的需求/规格、风险/控制配对、差距范围与目标架构摘要是什么？
- 来源、范围与适用性


## 输入及缺口处理

必需：

- {'id': 'work_package_id', 'meaning': '笔记本所对应的工作包', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'solution_concept_ref', 'meaning': '解决方案概念图视图ID', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'implementation_strategy', 'meaning': '处理差距或工作包的首选方法', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'stakeholders', 'meaning': '利益相关者及其需求ID', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'requirements', 'meaning': '入向需求及利益相关者ID', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'specifications', 'meaning': '架构规格；每条追溯到一项需求', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'risks', 'meaning': '适用风险；无控制时记录有证据的处理决定', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'controls', 'meaning': '控制；每条追溯到一项风险', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'gaps', 'meaning': '差距及in_scope真假', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'architecture_summary', 'meaning': '各域目标架构视图引用或不适用理由（仅供参考）', 'origin': 'source-purpose-plus-project-contract'}

可选：

- 既有模型及历史结论

关键输入缺失时生成带ID的草稿与缺口，不计算无依据数值，不伪造批准或事实；结构错误直接拒绝。

## 元素、属性与关系

对象类型：guide:solution-delivery-notebook。

```json
{
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
}
```

{
  "work_package_id": {
    "meaning": "笔记本所对应的工作包",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "solution_concept_ref": {
    "meaning": "解决方案概念图视图ID",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "implementation_strategy": {
    "meaning": "处理差距或工作包的首选方法",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "stakeholders": {
    "meaning": "利益相关者及其需求ID",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "requirements": {
    "meaning": "入向需求及利益相关者ID",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "specifications": {
    "meaning": "架构规格；每条追溯到一项需求",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "risks": {
    "meaning": "适用风险；无控制时记录有证据的处理决定",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "controls": {
    "meaning": "控制；每条追溯到一项风险",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "gaps": {
    "meaning": "差距及in_scope真假",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "architecture_summary": {
    "meaning": "各域目标架构视图引用或不适用理由（仅供参考）",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 写解决方案摘要：概念图、利益相关者目录、风险目录、差距目录
2. 写规格摘要：实施策略、架构规格、控制
3. 每条规格追溯到需求，每个控制追溯到风险
4. 标出本工作包处理与不处理的差距
5. 用视图引用概述各域目标架构（仅供参考）
6. 用需求/规格与风险/控制两类配对作为合规评估依据

## 输出、检查与误读

- 范围及依据
- 逐条结果与理由
- 缺口、下一步与责任
- 版本和来源引用

- 规格总追溯到某项需求
- 控制总追溯到某项风险
- 架构描述摘要仅供参考，不替代规格
- 笔记本是交付沟通模板，不代表合同已签署

- 名称、来源表格和成功输出不等于业务结论已核实
- 规格总追溯到某项需求
- 控制总追溯到某项风险
- 架构描述摘要仅供参考，不替代规格
- 笔记本是交付沟通模板，不代表合同已签署


## 视图和交付物

- [解决方案交付笔记本](../profiles/solution-delivery-notebook-default.md)

- [architecture-contract](../deliverables/architecture-contract.md)
- [compliance-assessment](../deliverables/compliance-assessment.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "规格S-1追溯到不存在的需求R-NONE",
    "expected": "SDN-004",
    "why": "SDN-004 [S-1]: Every specification must trace to a requirement"
  },
  "modification_example": {
    "change": "删除控制C-1",
    "expected": "分析结果变化：新增缺口RK-1:control"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/solution-delivery-notebook.md)
[完整操作案例](../../references/capability-addenda/solution-delivery-notebook.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

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

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact solution-delivery-notebook --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
