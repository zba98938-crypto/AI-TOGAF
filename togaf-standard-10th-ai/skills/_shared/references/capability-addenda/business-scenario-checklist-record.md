# 业务场景步骤清单与角色记录（Business Scenario Checklists and Roles Record）

工作产品 `business-scenario-checklist-record` · 视图 `business-scenario-checklist-record-default` · 方法 `business-scenario-checklist-review` · 主责 [togaf-vision-scenarios](../../../togaf-vision-scenarios/SKILL.md) · 常用ADM：A。

来源：G176 §10、§11.1–11.6。本地中文正文已逐节阅读，英文PDF已抽查对应段落。字段、规则与计算是项目操作约定，不冒充TOGAF强制规则；官方来源等价、专业充分性与业务批准另行评审。

## 决策问题

业务场景每个步骤的清单完成到哪里，缺什么证据，G176的角色是否在规划步骤指定？

## 字段

- `guide:scenario-checklist-stage` 必填：`stage`（G176 §11清单阶段）、`responses`（清单项结果：done需证据，not-applicable需理由，open需负责人和行动）、`uses_workshop`（是否采用工作坊（决定工作坊条件项是否适用））
- 可选：`role_assignments`（G176 §10角色分配：人员、指定阶段与证据）

## 步骤

1. 选择本次涉及的清单阶段
2. 逐项记录done/not-applicable/open及证据、理由或负责人
3. 仅在采用工作坊时纳入工作坊条件项
4. 分组项按任一或全部子项规则核对
5. 在规划步骤指定项目经理、顾问、作者与编辑等角色
6. 报告未完成项，不计算完成率

## 判定

结构错误（未知ID、追溯断裂、非法取值等）直接拒绝并返回错误码；缺输入或证据记为带ID的缺口，草稿仍可输出。角色关系依实际类型与明确采用的项目策略检查，位置或层级本身不证明人事汇报。检查要点：

- 勾选项须有证据；不适用须有理由
- 工作坊条件项只在采用工作坊时适用
- 一人可担任多个G176角色；角色数不等于人数
- 清单完成不表示业务场景被接受

## 调用

```sh
"$TOGAF_SHARED/.venv/bin/python" "$TOGAF_SHARED/scripts/analyze.py" model.json --evaluate business-scenario-checklist-record-analysis
"$TOGAF_SHARED/.venv/bin/python" "$TOGAF_SHARED/scripts/generate.py" model.json --profile business-scenario-checklist-record-default --out output
```

分析写在 `model.analyses`，由视图 `attributes.analysis_ids` 引用；`inputs.source_ids` 须列出所用来源。

## 虚构案例（星河零售）

原料：

- `BSC-R1`：虚构星河零售“门店自提”业务场景：前提为“顾客希望当日自提”；发起人为零售副总裁；触发因素为业务需求不清。
- `BSC-R2`：规划会议纪要：指定项目经理赵某、顾问钱某、作者孙某、编辑周某；时间6周、人员4人、预算待定。

基线结果（实际执行计算器所得）：

```json
{
  "rows": [
    {
      "id": "premise-01",
      "state": "done",
      "children": {}
    },
    {
      "id": "premise-02",
      "state": "done",
      "children": {}
    },
    {
      "id": "premise-03",
      "state": "done",
      "children": {}
    },
    {
      "id": "premise-04",
      "state": "done",
      "children": {
        "premise-04a": "done",
        "premise-04b": "unreviewed",
        "premise-04c": "unreviewed",
        "premise-04d": "unreviewed",
        "premise-04e": "unreviewed",
        "premise-04f": "unreviewed"
      }
    },
    {
      "id": "premise-05",
      "state": "done",
      "children": {}
    },
    {
      "id": "premise-06",
      "state": "done",
      "children": {}
    },
    {
      "id": "premise-07",
      "state": "open",
      "children": {}
    },
    {
      "id": "premise-08",
      "state": "done",
      "children": {}
    },
    {
      "id": "plan-01",
      "state": "done",
      "children": {}
    },
    {
      "id": "plan-02",
      "state": "done",
      "children": {}
    },
    {
      "id": "plan-03",
      "state": "done",
      "children": {}
    },
    {
      "id": "plan-04",
      "state": "done",
      "children": {
        "plan-04a": "done",
        "plan-04b": "done",
        "plan-04c": "open"
      }
    },
    {
      "id": "plan-05",
      "state": "unreviewed"
    },
    {
      "id": "plan-06",
      "state": "unreviewed"
    },
    {
      "id": "plan-07",
      "state": "unreviewed"
    },
    {
      "id": "plan-08",
      "state": "unreviewed"
    },
    {
      "id": "plan-09",
      "state": "unreviewed"
    },
    {
      "id": "plan-10",
      "state": "unreviewed"
    },
    {
      "id": "plan-11",
      "state": "unreviewed"
    }
  ],
  "open_item_ids": [
    "plan-05",
    "plan-06",
    "plan-07",
    "plan-08",
    "plan-09",
    "plan-10",
    "plan-11",
    "premise-07"
  ],
  "staffed_role_ids": [
    "business-scenario-author",
    "business-scenario-consultant",
    "business-scenario-editor",
    "project-manager"
  ],
  "unstaffed_role_ids": [
    "business-scenario-analyst",
    "business-scenario-facilitator",
    "host",
    "sme-contributor",
    "sme-reviewer",
    "sponsor",
    "workshop-questioner",
    "workshop-recorder"
  ],
  "gaps": [
    {
      "id": "plan-04",
      "reason": "all-of-incomplete",
      "action": "每个子项须完成或说明不适用"
    }
  ],
  "notice": "逐项记录清单完成情况；不计算完成率，不表示业务场景已被接受。一人可担任多个角色。"
}
```

修改：删除规划阶段的角色分配。分析结果变化：新增缺口plan-01:role,plan-02:role,role:business-scenario-author,role:business-scenario-consultant,role:business-scenario-editor,role:project-manager。修改后结果：

```json
{
  "rows": [
    {
      "id": "premise-01",
      "state": "done",
      "children": {}
    },
    {
      "id": "premise-02",
      "state": "done",
      "children": {}
    },
    {
      "id": "premise-03",
      "state": "done",
      "children": {}
    },
    {
      "id": "premise-04",
      "state": "done",
      "children": {
        "premise-04a": "done",
        "premise-04b": "unreviewed",
        "premise-04c": "unreviewed",
        "premise-04d": "unreviewed",
        "premise-04e": "unreviewed",
        "premise-04f": "unreviewed"
      }
    },
    {
      "id": "premise-05",
      "state": "done",
      "children": {}
    },
    {
      "id": "premise-06",
      "state": "done",
      "children": {}
    },
    {
      "id": "premise-07",
      "state": "open",
      "children": {}
    },
    {
      "id": "premise-08",
      "state": "done",
      "children": {}
    },
    {
      "id": "plan-01",
      "state": "done",
      "children": {}
    },
    {
      "id": "plan-02",
      "state": "done",
      "children": {}
    },
    {
      "id": "plan-03",
      "state": "done",
      "children": {}
    },
    {
      "id": "plan-04",
      "state": "done",
      "children": {
        "plan-04a": "done",
        "plan-04b": "done",
        "plan-04c": "open"
      }
    },
    {
      "id": "plan-05",
      "state": "unreviewed"
    },
    {
      "id": "plan-06",
      "state": "unreviewed"
    },
    {
      "id": "plan-07",
      "state": "unreviewed"
    },
    {
      "id": "plan-08",
      "state": "unreviewed"
    },
    {
      "id": "plan-09",
      "state": "unreviewed"
    },
    {
      "id": "plan-10",
      "state": "unreviewed"
    },
    {
      "id": "plan-11",
      "state": "unreviewed"
    }
  ],
  "open_item_ids": [
    "plan-05",
    "plan-06",
    "plan-07",
    "plan-08",
    "plan-09",
    "plan-10",
    "plan-11",
    "premise-07"
  ],
  "staffed_role_ids": [],
  "unstaffed_role_ids": [
    "business-scenario-analyst",
    "business-scenario-author",
    "business-scenario-consultant",
    "business-scenario-editor",
    "business-scenario-facilitator",
    "host",
    "project-manager",
    "sme-contributor",
    "sme-reviewer",
    "sponsor",
    "workshop-questioner",
    "workshop-recorder"
  ],
  "gaps": [
    {
      "id": "plan-04",
      "reason": "all-of-incomplete",
      "action": "每个子项须完成或说明不适用"
    },
    {
      "id": "role:project-manager",
      "reason": "role-not-staffed-in-plan",
      "action": "G176 §10/§11：project-manager应在规划步骤指定"
    },
    {
      "id": "plan-01:role",
      "reason": "checklist-role-mismatch",
      "action": "清单标记已指定，但没有对应角色分配记录"
    },
    {
      "id": "role:business-scenario-consultant",
      "reason": "role-not-staffed-in-plan",
      "action": "G176 §10/§11：business-scenario-consultant应在规划步骤指定"
    },
    {
      "id": "plan-02:role",
      "reason": "checklist-role-mismatch",
      "action": "清单标记已指定，但没有对应角色分配记录"
    },
    {
      "id": "role:business-scenario-author",
      "reason": "role-not-staffed-in-plan",
      "action": "G176 §10/§11：business-scenario-author应在规划步骤指定"
    },
    {
      "id": "role:business-scenario-editor",
      "reason": "role-not-staffed-in-plan",
      "action": "G176 §10/§11：business-scenario-editor应在规划步骤指定"
    }
  ],
  "notice": "逐项记录清单完成情况；不计算完成率，不表示业务场景已被接受。一人可担任多个角色。"
}
```

反例：清单项状态写为passed。实际拒绝：`BSC-002 [plan-01]: status must be done, not-applicable or open`

完整模型片段见 [能力注册](../capabilities/business-scenario-checklist-record.md)。以上全部为虚构教学材料，不代表真实企业事实或批准。
