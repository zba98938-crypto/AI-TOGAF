# SMART目的评估（SMART Objective Assessment）

工作产品 `smart-objective-assessment` · 视图 `smart-objective-assessment-default` · 方法 `smart-objective-review` · 主责 [togaf-strategy-capabilities](../../../togaf-strategy-capabilities/SKILL.md) · 常用ADM：A B。

来源：G176 §9.1–9.3。本地中文正文已逐节阅读，英文PDF已抽查对应段落。字段、规则与计算是项目操作约定，不冒充TOGAF强制规则；官方来源等价、专业充分性与业务批准另行评审。

## 决策问题

每个目的是否具体、可度量、可行动、现实、有时限，并追溯到已分类的目标？

## 字段

- `guide:goal` 必填：`statement`（陈述）、`category`（G176 §9.3目标类别ID）、`business_goal_ref`（对应的组织业务目标）
- `guide:smart-objective` 必填：`goal_id`（所属目标ID）、`statement`（陈述）、`scope`（该对象负责或适用的范围）、`measure`（度量）、`unit`（单位）、`target`（目标值）
- 可选：`organization_category`（组织自定类别）、`baseline`（基线值）、`owner`（负责人）、`action`（实现行动）、`realism_rationale`（现实性理由）、`realism_evidence`（支持现实性的证据ID）、`due`（截止日期（ISO））

## 步骤

1. 把目标归入G176 §9.3的13类之一或组织自定类别
2. 把每个目的追溯到目标
3. 逐项核对具体、可度量、可行动、现实、有时限
4. 可度量项记录基线、目标与单位
5. 现实性给出理由与证据
6. 缺项列为待补，不由模板补数值

## 判定

结构错误（未知ID、追溯断裂、非法取值等）直接拒绝并返回错误码；缺输入或证据记为带ID的缺口，草稿仍可输出。角色关系依实际类型与明确采用的项目策略检查，位置或层级本身不证明人事汇报。检查要点：

- 13类目标是示例类别，不是封闭清单
- SMART只检查结构，现实性与数值合理性由责任人判断
- 目的须追溯到组织业务目标

## 调用

```sh
"$TOGAF_SHARED/.venv/bin/python" "$TOGAF_SHARED/scripts/analyze.py" model.json --evaluate smart-objective-assessment-analysis
"$TOGAF_SHARED/.venv/bin/python" "$TOGAF_SHARED/scripts/generate.py" model.json --profile smart-objective-assessment-default --out output
```

分析写在 `model.analyses`，由视图 `attributes.analysis_ids` 引用；`inputs.source_ids` 须列出所用来源。

## 虚构案例（星河零售）

原料：

- `SMART-R1`：虚构目标G-UP（类别：提高用户生产率）：门店前台界面一致；业务目标引用BG-3。
- `SMART-R2`：目的O-1：2027-06-30前三类前台设备界面一致，订单录入错误由5%降到4%，负责人UX组；可用性测试支持可行性。

基线结果（实际执行计算器所得）：

```json
{
  "rows": [
    {
      "id": "O-1",
      "goal_id": "G-UP",
      "criteria": {
        "specific": true,
        "measurable": true,
        "actionable": true,
        "realistic": true,
        "time-bound": true
      },
      "state": "structurally-smart-awaiting-review",
      "gaps": []
    },
    {
      "id": "O-2",
      "goal_id": "G-UP",
      "criteria": {
        "specific": true,
        "measurable": true,
        "actionable": false,
        "realistic": false,
        "time-bound": false
      },
      "state": "needs-input",
      "gaps": [
        {
          "id": "O-2:baseline",
          "reason": "no-baseline",
          "action": "有目标但无基线，无法判断改进幅度"
        },
        {
          "id": "O-2:actionable",
          "reason": "smart-actionable-missing",
          "action": "按G176 §9.2补充该维度的具体内容"
        },
        {
          "id": "O-2:realistic",
          "reason": "smart-realistic-missing",
          "action": "按G176 §9.2补充该维度的具体内容"
        },
        {
          "id": "O-2:time-bound",
          "reason": "smart-time-bound-missing",
          "action": "按G176 §9.2补充该维度的具体内容"
        }
      ]
    }
  ],
  "gaps": [
    {
      "id": "O-2:baseline",
      "reason": "no-baseline",
      "action": "有目标但无基线，无法判断改进幅度"
    },
    {
      "id": "O-2:actionable",
      "reason": "smart-actionable-missing",
      "action": "按G176 §9.2补充该维度的具体内容"
    },
    {
      "id": "O-2:realistic",
      "reason": "smart-realistic-missing",
      "action": "按G176 §9.2补充该维度的具体内容"
    },
    {
      "id": "O-2:time-bound",
      "reason": "smart-time-bound-missing",
      "action": "按G176 §9.2补充该维度的具体内容"
    }
  ],
  "notice": "SMART只检查五个维度是否有可核对内容；现实性与数值是否合理由责任人判断。"
}
```

修改：为O-2补负责人、行动、现实性证据与截止日期。分析结果变化：关闭缺口O-2:actionable,O-2:baseline,O-2:realistic,O-2:time-bound。修改后结果：

```json
{
  "rows": [
    {
      "id": "O-1",
      "goal_id": "G-UP",
      "criteria": {
        "specific": true,
        "measurable": true,
        "actionable": true,
        "realistic": true,
        "time-bound": true
      },
      "state": "structurally-smart-awaiting-review",
      "gaps": []
    },
    {
      "id": "O-2",
      "goal_id": "G-UP",
      "criteria": {
        "specific": true,
        "measurable": true,
        "actionable": true,
        "realistic": true,
        "time-bound": true
      },
      "state": "structurally-smart-awaiting-review",
      "gaps": []
    }
  ],
  "gaps": [],
  "notice": "SMART只检查五个维度是否有可核对内容；现实性与数值是否合理由责任人判断。"
}
```

反例：目的O-1追溯到不存在的目标。实际拒绝：`SMART-002 [O-1]: Objective must trace to a registered goal`

完整模型片段见 [能力注册](../capabilities/smart-objective-assessment.md)。以上全部为虚构教学材料，不代表真实企业事实或批准。
