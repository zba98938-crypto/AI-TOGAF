# 业务场景步骤清单与角色记录

`profile_id`: business-scenario-checklist-record-default；`artifact_id`: business-scenario-checklist-record；主责：[togaf-vision-scenarios](../../../togaf-vision-scenarios/SKILL.md)。

来源：G176 §10、§11.1–11.6。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：1.0。

{
  "id": "business-scenario-checklist-record-default",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "按工作产品字段组织的记录表；来源无对应原图。",
  "structure_basis": "正文定义的工作产品；记录表是项目操作表示法，不冒充来源原图"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:scenario-checklist-stage。关系类型：。

```json
{
  "entities": {
    "guide:scenario-checklist-stage": [
      "stage",
      "responses",
      "uses_workshop"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 对象、关系、必要属性均可追溯并得到表达
- 参考内容不自动成为项目事实；未知项保持显式
- 勾选项须有证据；不适用须有理由
- 工作坊条件项只在采用工作坊时适用
- 一人可担任多个G176角色；角色数不等于人数
- 清单完成不表示业务场景被接受

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

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

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile business-scenario-checklist-record-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile business-scenario-checklist-record-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
