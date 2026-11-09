# 架构项目状态要点报告

`profile_id`: project-status-highlight-report-default；`artifact_id`: project-status-highlight-report；主责：[togaf-architecture-workbench](../../../togaf-architecture-workbench/SKILL.md)。

来源：G188 §3.4.2–3.4.8 L1112–1205。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：1.0。

{
  "id": "project-status-highlight-report-default",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "按已核查的来源结构参数化；参考图与业务实例的验收分别进行。",
  "structure_basis": "正文定义的工作产品；记录表是项目操作表示法，不冒充来源原图"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:project-highlight-report。关系类型：。

```json
{
  "entities": {
    "guide:project-highlight-report": [
      "period",
      "next_period",
      "audience",
      "communication_plan_ref",
      "approved_plan_ref",
      "previous_planned_task_ids",
      "tasks",
      "next_period_activities",
      "risks_issues",
      "corrective_actions",
      "remaining_stage_forecast",
      "remaining_project_forecast",
      "decisions_required",
      "changes",
      "schedule_tolerance",
      "analysis_result",
      "raw_material_refs"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 对象、关系、必要属性均可追溯并得到表达
- 参考内容不自动成为项目事实；未知项保持显式
- 要点报告是按时间驱动的沟通，不替代例外报告
- 预测/已提交不等于完成验收
- 上期计划任务不能在下期无解释消失
- 未批准变更与已批准变更分开
- 示例一页、三条和每周频率不是通用规则
- 只有显式项目容差才能判断越界

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构案例；规则不是TOGAF规定",
  "sources": [
    {
      "id": "H-R1",
      "kind": "example",
      "description": "批准进度PLAN-1安排TASK-A需求核对10月12日完成、TASK-B接口分析10月16日完成；上期要点的计划清单含TASK-A和TASK-B。沟通计划CP-1要求10月12–18日一页周报，下一期10月19–25日。项目规则：预测相对批准日期延误大于2个日历日须上报，等于2日不越权。",
      "locator": "raw-materials.json#H-R1"
    },
    {
      "id": "H-R2",
      "kind": "example",
      "description": "10月18日检查点：TASK-A已于10月12日完成并有验收记录ACC-A；TASK-B仍分析中，预测10月18日完成，未验收。关键问题ISS-1是合作方接口样本不齐，责任人为接口负责人；纠正措施是10月19日补齐样本并验证。下一期继续TASK-B并准备TASK-C集成模型评审。阶段余项预计10月25日结束，项目仍预计11月15日结束。",
      "locator": "raw-materials.json#H-R2"
    },
    {
      "id": "H-R3",
      "kind": "example",
      "description": "CH-1增加一个试点接口仍待指导组批准，未写入批准基线。指导组需决定是否批准试点范围；当前周报需要保留该待决项，而非默认已批准。",
      "locator": "raw-materials.json#H-R3"
    },
    {
      "id": "H-R4",
      "kind": "example",
      "description": "修改：供应商通知样本再晚两天，TASK-B预测完成改为10月20日，实际仍未验收；项目经理更新上报需求，保持PLAN-1的10月16日批准基线不变。",
      "locator": "raw-materials.json#H-R4"
    }
  ],
  "entities": [
    {
      "id": "HL-1",
      "type": "guide:project-highlight-report",
      "name": "架构项目状态要点报告：虚构图书馆联盟",
      "attributes": {
        "period": {
          "start": "2026-10-12",
          "end": "2026-10-18"
        },
        "next_period": {
          "start": "2026-10-19",
          "end": "2026-10-25"
        },
        "audience": "项目指导组；一页摘要",
        "communication_plan_ref": "CP-1",
        "approved_plan_ref": "PLAN-1",
        "previous_planned_task_ids": [
          "TASK-A",
          "TASK-B"
        ],
        "tasks": [
          {
            "id": "TASK-A",
            "name": "需求核对",
            "state": "accepted",
            "planned_finish": "2026-10-12",
            "forecast_finish": "2026-10-12",
            "owner": "业务架构师",
            "evidence": [
              "H-R1",
              "H-R2"
            ],
            "acceptance_evidence": [
              "H-R2"
            ]
          },
          {
            "id": "TASK-B",
            "name": "接口分析",
            "state": "in-progress",
            "planned_finish": "2026-10-16",
            "forecast_finish": "2026-10-18",
            "owner": "应用架构师",
            "evidence": [
              "H-R1",
              "H-R2"
            ]
          }
        ],
        "next_period_activities": [
          {
            "id": "TASK-B",
            "action": "补齐接口分析并送验收",
            "owner": "应用架构师"
          },
          {
            "id": "TASK-C",
            "action": "准备集成模型评审，开始工作仍须授权",
            "owner": "集成架构师"
          }
        ],
        "risks_issues": [
          {
            "id": "ISS-1",
            "kind": "issue",
            "description": "合作方接口样本不齐",
            "owner": "接口负责人",
            "evidence": [
              "H-R2"
            ]
          }
        ],
        "corrective_actions": [
          {
            "id": "ACT-1",
            "issue_id": "ISS-1",
            "action": "10月19日补齐样本并验证",
            "owner": "接口负责人"
          }
        ],
        "remaining_stage_forecast": "余项预计2026-10-25结束，待接口样本验证",
        "remaining_project_forecast": "仍预计2026-11-15结束；预测不是批准",
        "decisions_required": [
          {
            "id": "DEC-1",
            "question": "是否批准增加试点接口CH-1",
            "authority": "项目指导组"
          }
        ],
        "changes": [
          {
            "id": "CH-1",
            "status": "pending",
            "incorporated_into_approved_baseline": false,
            "evidence": [
              "H-R3"
            ]
          }
        ],
        "schedule_tolerance": {
          "unit": "calendar-day",
          "operator": ">",
          "value": 2,
          "authority": "项目指导组",
          "evidence": [
            "H-R1"
          ]
        },
        "analysis_result": {
          "report_id": "HL-1",
          "period": {
            "start": "2026-10-12",
            "end": "2026-10-18"
          },
          "task_reviews": [
            {
              "id": "TASK-A",
              "state": "accepted",
              "completion_supported": true,
              "forecast_variance_calendar_days": 0,
              "schedule_exception": false,
              "gaps": []
            },
            {
              "id": "TASK-B",
              "state": "in-progress",
              "completion_supported": false,
              "forecast_variance_calendar_days": 2,
              "schedule_exception": false,
              "gaps": []
            }
          ],
          "schedule_exception_task_ids": [],
          "approved_change_ids": [],
          "pending_change_ids": [
            "CH-1"
          ],
          "gaps": [],
          "state": "reviewable-report",
          "notice": "状态要点按报告期汇总实际、下一期计划、风险问题、纠偏和预测；预期完成不等于已验收。例外报告是另一个治理动作，本审查只标识显式项目容差越界。"
        },
        "raw_material_refs": [
          "H-R1",
          "H-R2",
          "H-R3"
        ]
      },
      "evidence": [
        "H-R1",
        "H-R2",
        "H-R3"
      ],
      "certainty": "assumed",
      "version": "1.0"
    }
  ],
  "relationships": [],
  "view": {
    "id": "project-status-highlight-report-baseline",
    "artifact_id": "project-status-highlight-report",
    "profile_id": "project-status-highlight-report-default",
    "title": "架构项目状态要点报告／baseline",
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
      "HL-1"
    ],
    "relationship_ids": [],
    "analysis": "从随包原始业务陈述提取字段、明确来源及项目规则，再执行project-highlight-review；逐字段保持假设与实际观察的区分。",
    "legend": "同一ID在修改前后代表同一工作产品；完整字段、嵌套记录及分析缺口按记录表可见。",
    "attributes": {
      "analysis_ids": [
        "project-status-highlight-report-analysis"
      ]
    }
  },
  "analyses": [
    {
      "id": "project-status-highlight-report-analysis",
      "method_id": "project-highlight-review",
      "inputs": {
        "id": "HL-1",
        "source_ids": [
          "H-R1",
          "H-R2",
          "H-R3"
        ],
        "period": {
          "start": "2026-10-12",
          "end": "2026-10-18"
        },
        "next_period": {
          "start": "2026-10-19",
          "end": "2026-10-25"
        },
        "audience": "项目指导组；一页摘要",
        "communication_plan_ref": "CP-1",
        "approved_plan_ref": "PLAN-1",
        "previous_planned_task_ids": [
          "TASK-A",
          "TASK-B"
        ],
        "tasks": [
          {
            "id": "TASK-A",
            "name": "需求核对",
            "state": "accepted",
            "planned_finish": "2026-10-12",
            "forecast_finish": "2026-10-12",
            "owner": "业务架构师",
            "evidence": [
              "H-R1",
              "H-R2"
            ],
            "acceptance_evidence": [
              "H-R2"
            ]
          },
          {
            "id": "TASK-B",
            "name": "接口分析",
            "state": "in-progress",
            "planned_finish": "2026-10-16",
            "forecast_finish": "2026-10-18",
            "owner": "应用架构师",
            "evidence": [
              "H-R1",
              "H-R2"
            ]
          }
        ],
        "next_period_activities": [
          {
            "id": "TASK-B",
            "action": "补齐接口分析并送验收",
            "owner": "应用架构师"
          },
          {
            "id": "TASK-C",
            "action": "准备集成模型评审，开始工作仍须授权",
            "owner": "集成架构师"
          }
        ],
        "risks_issues": [
          {
            "id": "ISS-1",
            "kind": "issue",
            "description": "合作方接口样本不齐",
            "owner": "接口负责人",
            "evidence": [
              "H-R2"
            ]
          }
        ],
        "corrective_actions": [
          {
            "id": "ACT-1",
            "issue_id": "ISS-1",
            "action": "10月19日补齐样本并验证",
            "owner": "接口负责人"
          }
        ],
        "remaining_stage_forecast": "余项预计2026-10-25结束，待接口样本验证",
        "remaining_project_forecast": "仍预计2026-11-15结束；预测不是批准",
        "decisions_required": [
          {
            "id": "DEC-1",
            "question": "是否批准增加试点接口CH-1",
            "authority": "项目指导组"
          }
        ],
        "changes": [
          {
            "id": "CH-1",
            "status": "pending",
            "incorporated_into_approved_baseline": false,
            "evidence": [
              "H-R3"
            ]
          }
        ],
        "schedule_tolerance": {
          "unit": "calendar-day",
          "operator": ">",
          "value": 2,
          "authority": "项目指导组",
          "evidence": [
            "H-R1"
          ]
        },
        "evidence": [
          "H-R1",
          "H-R2",
          "H-R3"
        ]
      },
      "evidence": [
        "H-R1",
        "H-R2",
        "H-R3"
      ]
    }
  ]
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile project-status-highlight-report-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile project-status-highlight-report-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
