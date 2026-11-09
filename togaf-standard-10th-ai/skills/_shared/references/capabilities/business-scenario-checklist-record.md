# 业务场景步骤清单与角色记录

ID：`business-scenario-checklist-record`。主责：[togaf-vision-scenarios](../../../togaf-vision-scenarios/SKILL.md)。

来源：G176 §10、§11.1–11.6。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

业务场景每个步骤的清单完成到哪里，缺什么证据，G176的角色是否在规划步骤指定？

- 该范围业务负责人
- 架构师
- 评审及治理负责人
- 业务场景每个步骤的清单完成到哪里，缺什么证据，G176的角色是否在规划步骤指定？
- 来源、范围与适用性


## 输入及缺口处理

必需：

- {'id': 'stage', 'meaning': 'G176 §11清单阶段', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'responses', 'meaning': '清单项结果：done需证据，not-applicable需理由，open需负责人和行动', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'uses_workshop', 'meaning': '是否采用工作坊（决定工作坊条件项是否适用）', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'role_assignments', 'meaning': 'G176 §10角色分配：人员、指定阶段与证据', 'origin': 'source-purpose-plus-project-contract'}

可选：

- 既有模型及历史结论

关键输入缺失时生成带ID的草稿与缺口，不计算无依据数值，不伪造批准或事实；结构错误直接拒绝。

## 元素、属性与关系

对象类型：guide:scenario-checklist-stage。

```json
{
  "guide:scenario-checklist-stage": [
    "stage",
    "responses",
    "uses_workshop"
  ]
}
```

{
  "stage": {
    "meaning": "G176 §11清单阶段",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "responses": {
    "meaning": "清单项结果：done需证据，not-applicable需理由，open需负责人和行动",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "uses_workshop": {
    "meaning": "是否采用工作坊（决定工作坊条件项是否适用）",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "role_assignments": {
    "meaning": "G176 §10角色分配：人员、指定阶段与证据",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 选择本次涉及的清单阶段
2. 逐项记录done/not-applicable/open及证据、理由或负责人
3. 仅在采用工作坊时纳入工作坊条件项
4. 分组项按任一或全部子项规则核对
5. 在规划步骤指定项目经理、顾问、作者与编辑等角色
6. 报告未完成项，不计算完成率

## 输出、检查与误读

- 范围及依据
- 逐条结果与理由
- 缺口、下一步与责任
- 版本和来源引用

- 勾选项须有证据；不适用须有理由
- 工作坊条件项只在采用工作坊时适用
- 一人可担任多个G176角色；角色数不等于人数
- 清单完成不表示业务场景被接受

- 名称、来源表格和成功输出不等于业务结论已核实
- 勾选项须有证据；不适用须有理由
- 工作坊条件项只在采用工作坊时适用
- 一人可担任多个G176角色；角色数不等于人数
- 清单完成不表示业务场景被接受


## 视图和交付物

- [业务场景步骤清单与角色记录](../profiles/business-scenario-checklist-record-default.md)

- [architecture-vision](../deliverables/architecture-vision.md)
- [statement-of-work](../deliverables/statement-of-work.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "清单项状态写为passed",
    "expected": "BSC-002",
    "why": "BSC-002 [plan-01]: status must be done, not-applicable or open"
  },
  "modification_example": {
    "change": "删除规划阶段的角色分配",
    "expected": "分析结果变化：新增缺口plan-01:role,plan-02:role,role:business-scenario-author,role:business-scenario-consultant,role:business-scenario-editor,role:project-manager"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/business-scenario-checklist-record.md)
[完整操作案例](../../references/capability-addenda/business-scenario-checklist-record.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

```json
{
  "notice": "虚构星河零售教学案例；规则不是TOGAF规定，不代表批准。",
  "sources": [
    {
      "id": "BSC-R1",
      "kind": "example",
      "description": "虚构星河零售“门店自提”业务场景：前提为“顾客希望当日自提”；发起人为零售副总裁；触发因素为业务需求不清。",
      "locator": "raw-materials.json#BSC-R1"
    },
    {
      "id": "BSC-R2",
      "kind": "example",
      "description": "规划会议纪要：指定项目经理赵某、顾问钱某、作者孙某、编辑周某；时间6周、人员4人、预算待定。",
      "locator": "raw-materials.json#BSC-R2"
    }
  ],
  "entities": [
    {
      "id": "BSC-PREMISE",
      "type": "guide:scenario-checklist-stage",
      "name": "清单：前提形成",
      "attributes": {
        "stage": "premise",
        "responses": {
          "premise-01": {
            "status": "done",
            "evidence": [
              "BSC-R1"
            ]
          },
          "premise-02": {
            "status": "done",
            "evidence": [
              "BSC-R1"
            ]
          },
          "premise-03": {
            "status": "done",
            "evidence": [
              "BSC-R1"
            ]
          },
          "premise-04": {
            "status": "done",
            "evidence": [
              "BSC-R1"
            ]
          },
          "premise-04a": {
            "status": "done",
            "evidence": [
              "BSC-R1"
            ]
          },
          "premise-05": {
            "status": "done",
            "evidence": [
              "BSC-R1"
            ]
          },
          "premise-06": {
            "status": "done",
            "evidence": [
              "BSC-R1"
            ]
          },
          "premise-07": {
            "status": "open",
            "owner": "钱某",
            "action": "联系两家物流供方"
          },
          "premise-08": {
            "status": "done",
            "evidence": [
              "BSC-R1"
            ]
          }
        },
        "uses_workshop": false,
        "role_assignments": []
      },
      "evidence": [
        "BSC-R1"
      ],
      "certainty": "assumed"
    },
    {
      "id": "BSC-PLAN",
      "type": "guide:scenario-checklist-stage",
      "name": "清单：规划",
      "attributes": {
        "stage": "plan",
        "responses": {
          "plan-01": {
            "status": "done",
            "evidence": [
              "BSC-R2"
            ]
          },
          "plan-02": {
            "status": "done",
            "evidence": [
              "BSC-R2"
            ]
          },
          "plan-03": {
            "status": "done",
            "evidence": [
              "BSC-R2"
            ]
          },
          "plan-04": {
            "status": "done",
            "evidence": [
              "BSC-R2"
            ]
          },
          "plan-04a": {
            "status": "done",
            "evidence": [
              "BSC-R2"
            ]
          },
          "plan-04b": {
            "status": "done",
            "evidence": [
              "BSC-R2"
            ]
          },
          "plan-04c": {
            "status": "open",
            "owner": "赵某",
            "action": "确认预算"
          }
        },
        "uses_workshop": false,
        "role_assignments": [
          {
            "id": "RA-1",
            "role_id": "project-manager",
            "person": "赵某",
            "assigned_in_stage": "plan",
            "evidence": [
              "BSC-R2"
            ]
          },
          {
            "id": "RA-2",
            "role_id": "business-scenario-consultant",
            "person": "钱某",
            "assigned_in_stage": "plan",
            "evidence": [
              "BSC-R2"
            ]
          },
          {
            "id": "RA-3",
            "role_id": "business-scenario-author",
            "person": "孙某",
            "assigned_in_stage": "plan",
            "evidence": [
              "BSC-R2"
            ]
          },
          {
            "id": "RA-4",
            "role_id": "business-scenario-editor",
            "person": "周某",
            "assigned_in_stage": "plan",
            "evidence": [
              "BSC-R2"
            ]
          }
        ]
      },
      "evidence": [
        "BSC-R2"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "business-scenario-checklist-record-baseline",
    "artifact_id": "business-scenario-checklist-record",
    "profile_id": "business-scenario-checklist-record-default",
    "title": "业务场景步骤清单与角色记录／虚构星河零售",
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
      "BSC-PREMISE",
      "BSC-PLAN"
    ],
    "relationship_ids": [],
    "analysis": "从随包虚构原料提取字段，执行business-scenario-checklist-review；规则为项目操作约定。",
    "legend": "虚构示例；同一ID在修改前后代表同一对象；嵌套记录按表可见。",
    "attributes": {
      "analysis_ids": [
        "business-scenario-checklist-record-analysis"
      ]
    }
  },
  "analyses": [
    {
      "id": "business-scenario-checklist-record-analysis",
      "method_id": "business-scenario-checklist-review",
      "inputs": {
        "source_ids": [
          "BSC-R1",
          "BSC-R2"
        ],
        "stages": [
          "premise",
          "plan"
        ],
        "responses": {
          "premise-01": {
            "status": "done",
            "evidence": [
              "BSC-R1"
            ]
          },
          "premise-02": {
            "status": "done",
            "evidence": [
              "BSC-R1"
            ]
          },
          "premise-03": {
            "status": "done",
            "evidence": [
              "BSC-R1"
            ]
          },
          "premise-04": {
            "status": "done",
            "evidence": [
              "BSC-R1"
            ]
          },
          "premise-04a": {
            "status": "done",
            "evidence": [
              "BSC-R1"
            ]
          },
          "premise-05": {
            "status": "done",
            "evidence": [
              "BSC-R1"
            ]
          },
          "premise-06": {
            "status": "done",
            "evidence": [
              "BSC-R1"
            ]
          },
          "premise-07": {
            "status": "open",
            "owner": "钱某",
            "action": "联系两家物流供方"
          },
          "premise-08": {
            "status": "done",
            "evidence": [
              "BSC-R1"
            ]
          },
          "plan-01": {
            "status": "done",
            "evidence": [
              "BSC-R2"
            ]
          },
          "plan-02": {
            "status": "done",
            "evidence": [
              "BSC-R2"
            ]
          },
          "plan-03": {
            "status": "done",
            "evidence": [
              "BSC-R2"
            ]
          },
          "plan-04": {
            "status": "done",
            "evidence": [
              "BSC-R2"
            ]
          },
          "plan-04a": {
            "status": "done",
            "evidence": [
              "BSC-R2"
            ]
          },
          "plan-04b": {
            "status": "done",
            "evidence": [
              "BSC-R2"
            ]
          },
          "plan-04c": {
            "status": "open",
            "owner": "赵某",
            "action": "确认预算"
          }
        },
        "uses_workshop": false,
        "role_assignments": [
          {
            "id": "RA-1",
            "role_id": "project-manager",
            "person": "赵某",
            "assigned_in_stage": "plan",
            "evidence": [
              "BSC-R2"
            ]
          },
          {
            "id": "RA-2",
            "role_id": "business-scenario-consultant",
            "person": "钱某",
            "assigned_in_stage": "plan",
            "evidence": [
              "BSC-R2"
            ]
          },
          {
            "id": "RA-3",
            "role_id": "business-scenario-author",
            "person": "孙某",
            "assigned_in_stage": "plan",
            "evidence": [
              "BSC-R2"
            ]
          },
          {
            "id": "RA-4",
            "role_id": "business-scenario-editor",
            "person": "周某",
            "assigned_in_stage": "plan",
            "evidence": [
              "BSC-R2"
            ]
          }
        ]
      }
    }
  ]
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact business-scenario-checklist-record --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
