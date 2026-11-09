# 架构项目状态要点报告

ID：`project-status-highlight-report`。主责：[togaf-architecture-workbench](../../../togaf-architecture-workbench/SKILL.md)。

来源：G188 §3.4.2–3.4.8 L1112–1205。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

本报告期实际完成了什么、下期做什么、余项如何预测，哪些事项需要决策或上报？

- 该范围业务负责人
- 架构师
- 评审及运营负责人
- 本报告期实际完成了什么、下期做什么、余项如何预测，哪些事项需要决策或上报？
- 来源、范围与适用性


## 输入及缺口处理

必需：

- {'id': 'period', 'meaning': '本报告期起止日期', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'next_period', 'meaning': '下一报告期起止日期', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'audience', 'meaning': '受众与所需细节', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'communication_plan_ref', 'meaning': '沟通计划引用', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'approved_plan_ref', 'meaning': '批准范围/进度基线引用', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'previous_planned_task_ids', 'meaning': '上期计划的稳定任务ID', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'tasks', 'meaning': '任务的实际/预测、责任、计划日期和验收证据', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'next_period_activities', 'meaning': '下一期关键活动与责任', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'risks_issues', 'meaning': '关键风险/问题及需关注/上报事项', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'corrective_actions', 'meaning': '纠正措施与责任、期限', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'remaining_stage_forecast', 'meaning': '阶段剩余部分预测与不确定性', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'remaining_project_forecast', 'meaning': '项目剩余部分预测与不确定性', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'decisions_required', 'meaning': '需利益相关者作出的决策及权限', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'changes', 'meaning': '批准、未批准与拒绝变更状态及基线处理', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'schedule_tolerance', 'meaning': '具有单位、比较符、依据与授权者的项目规则', 'origin': 'source-purpose-plus-project-contract'}

可选：

- 既有模型及历史结论

不足时保留带ID草案与needs-input；未知容差不设默认值，缺实际阅读/验收证据不声称已阅读/完成。冲突、重复ID和未经批准覆盖基线属于错误。

## 元素、属性与关系

对象类型：guide:project-highlight-report。

```json
{
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
}
```

{
  "period": {
    "meaning": "本报告期起止日期",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "next_period": {
    "meaning": "下一报告期起止日期",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "audience": {
    "meaning": "受众与所需细节",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "communication_plan_ref": {
    "meaning": "沟通计划引用",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "approved_plan_ref": {
    "meaning": "批准范围/进度基线引用",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "previous_planned_task_ids": {
    "meaning": "上期计划的稳定任务ID",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "tasks": {
    "meaning": "任务的实际/预测、责任、计划日期和验收证据",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "next_period_activities": {
    "meaning": "下一期关键活动与责任",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "risks_issues": {
    "meaning": "关键风险/问题及需关注/上报事项",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "corrective_actions": {
    "meaning": "纠正措施与责任、期限",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "remaining_stage_forecast": {
    "meaning": "阶段剩余部分预测与不确定性",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "remaining_project_forecast": {
    "meaning": "项目剩余部分预测与不确定性",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "decisions_required": {
    "meaning": "需利益相关者作出的决策及权限",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "changes": {
    "meaning": "批准、未批准与拒绝变更状态及基线处理",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "schedule_tolerance": {
    "meaning": "具有单位、比较符、依据与授权者的项目规则",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "analysis_result": {
    "meaning": "确定性审查结果与带ID缺口",
    "value_rule": "由所列method输入重新计算，不作为治理批准"
  },
  "raw_material_refs": {
    "meaning": "完整原始业务材料ID列表",
    "value_rule": "随包原料可检索"
  },
  "name": {
    "meaning": "工作产品对象的业务名称",
    "value_rule": "使用范围内可识别的业务名称；身份由稳定ID确定，不以同名合并对象",
    "definition_origin": "project-operational-convention",
    "value_schema": {
      "type": "string",
      "minLength": 1,
      "pattern": "\\S"
    }
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 锁定报告期、受众、沟通计划及批准基线版本
2. 读取检查点、当前阶段计划、质量/风险/问题日志和收益评审计划
3. 沿用上期计划任务的同一ID核对实际、未完、取消和验收证据
4. 列下一期关键活动、风险问题、纠正措施和阶段/项目余项预测
5. 分别登记已批准和未批准变更，保持批准基线不被草案覆盖
6. 仅按显式委托容差识别例外，形成需决策/上报事项供治理审查

## 输出、检查与误读

- 范围及依据
- 逐条结果与理由
- 缺口、下一步与责任
- 版本和来源引用

- 要点报告是按时间驱动的沟通，不替代例外报告
- 预测/已提交不等于完成验收
- 上期计划任务不能在下期无解释消失
- 未批准变更与已批准变更分开
- 示例一页、三条和每周频率不是通用规则
- 只有显式项目容差才能判断越界

- 名称、来源表格和成功输出不等于业务结论已核实
- 要点报告是按时间驱动的沟通，不替代例外报告
- 预测/已提交不等于完成验收
- 上期计划任务不能在下期无解释消失
- 未批准变更与已批准变更分开
- 示例一页、三条和每周频率不是通用规则
- 只有显式项目容差才能判断越界


## 视图和交付物

- [架构项目状态要点报告](../profiles/project-status-highlight-report-default.md)

- [statement-of-work](../deliverables/statement-of-work.md)
- [communications-plan](../deliverables/communications-plan.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「架构项目状态要点报告」给出：名称、来源表格和成功输出不等于业务结论已核实",
    "expected": "missing-evidence",
    "why": "名称、来源表格和成功输出不等于业务结论已核实"
  },
  "modification_example": {
    "change": "在「架构项目状态要点报告」的范围内新增或修改一项，检查下游是否随之变化",
    "expected": "受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用"
  }
}
```

## 可编辑示例与调用



以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

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

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact project-status-highlight-report --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
