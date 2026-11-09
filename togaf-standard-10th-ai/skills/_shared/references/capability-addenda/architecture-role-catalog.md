# 架构角色定义目录（Architecture Role Definition Catalog）

工作产品 `architecture-role-catalog` · 视图 `architecture-role-catalog-default` · 方法 `architecture-role-catalog-review` · 主责 [togaf-organization-roles](../../../togaf-organization-roles/SKILL.md) · 常用ADM：Preliminary。

来源：G249 §4、§4.1–4.4。本地中文正文已逐节阅读，英文PDF已抽查对应段落。字段、规则与计算是项目操作约定，不冒充TOGAF强制规则；官方来源等价、专业充分性与业务批准另行评审。

## 决策问题

架构实践需要哪些职责，各角色如何提供上下文、治理、协作和交接，任务由谁在什么范围内承担？

## 字段

- `guide:architecture-role` 必填：`tier`（角色类别：chief/enterprise/segment/solution/specialist；不是通用人事职级总序）、`scope`（该对象负责或适用的范围）、`primary_responsibility`（首要职责）、`segment_scope`（分段或域范围；企业级角色写不适用及原因）、`activities`（主要活动清单）、`key_stakeholders`（关键利益相关者类别）、`kpis`（KPI记录：度量、目标、目标来源（project-adopted/source-illustrative）及证据）
- 可选：`leads`（旧版未分类领导关系；需补类型、范围和证据，保留为草稿缺口）、`relationships`（有类型关系：architecture_guidance/architecture_constraint/specialization/collaborates_with/reports_to/handoff，含target、scope和evidence）、`assignments`（人员、岗位、角色任务分配：person_ref、job_ref、task_refs、authority、valid_from、valid_until和evidence）

## 步骤

1. 按G249 §4区分首席、企业、分段、解决方案架构师及专家
2. 为每个角色记录范围、首要职责、活动和关键利益相关者
3. 分别记录专业指导、架构约束、特化、协作、汇报与交接；旧leads产生待分类缺口
4. 记录KPI口径、期间、来源和责任，区分企业采用目标与来源示例
5. 按第3、6章记录角色裁剪；只有显式采用的项目策略才施加严格层级规则
6. 记录有权限和有效期的人员任务分配，再用architecture-role-skill-assessment连接任务、技能证据及发展

## 来源要点

- 指南示例区分企业、分段、解决方案，依第3、6章按企业需要裁剪，非所有组织的强制职级（G249 §4（书页7；PDF页17））
- 首席架构师是企业架构师的特例，不是另一个并列层级（G249 §4）
- KPI中的“3/5满意度”“（xxx）四分位”是示例或占位，需企业自行设定目标（G249 §4.1–4.4）
- 岗位、角色、任务是不同概念；一人可承担多个角色，多人可承担同一角色（G249 §4）

## 判定

结构错误（未知ID、追溯断裂、非法取值等）直接拒绝并返回错误码；缺输入或证据记为带ID的缺口，草稿仍可输出。角色关系依实际类型与明确采用的项目策略检查，位置或层级本身不证明人事汇报。检查要点：

- 首席架构师是企业架构师的特例，不是另一个并列层级
- KPI中的3/5与（xxx）四分位是来源示例，不是企业目标
- 岗位、角色、任务不同；一人可担任多角色
- 角色定义不评价任何人员的能力或绩效

## 调用

```sh
"$TOGAF_SHARED/.venv/bin/python" "$TOGAF_SHARED/scripts/analyze.py" model.json --evaluate architecture-role-catalog-analysis
"$TOGAF_SHARED/.venv/bin/python" "$TOGAF_SHARED/scripts/generate.py" model.json --profile architecture-role-catalog-default --out output
```

分析写在 `model.analyses`，由视图 `attributes.analysis_ids` 引用；`inputs.source_ids` 须列出所用来源。

## 虚构案例（星河零售）

原料：

- `ROLE-R1`：虚构星河零售EA章程：首席架构师统筹，下设企业架构师1名、订单分段架构师1名、门店解决方案架构师1名。
- `ROLE-R2`：人力资源与EA负责人约定：利益相关者满意度目标暂按来源示例3/5记录，尚未批准；交付准时率目标90%已由架构委员会批准。

基线结果（实际执行计算器所得）：

```json
{
  "rows": [
    {
      "id": "ROLE-CHIEF",
      "tier": "chief",
      "leads": [
        "ROLE-EA",
        "ROLE-SEG",
        "ROLE-SOL"
      ],
      "relationships": [],
      "assignments": [],
      "state": "needs-input",
      "gaps": [
        {
          "id": "ROLE-CHIEF:leads:ROLE-EA",
          "reason": "untyped-legacy-lead",
          "action": "旧leads无法区分专业指导、架构约束与人事汇报；保留草稿并补有范围和证据的关系类型。"
        },
        {
          "id": "ROLE-CHIEF:leads:ROLE-SEG",
          "reason": "untyped-legacy-lead",
          "action": "旧leads无法区分专业指导、架构约束与人事汇报；保留草稿并补有范围和证据的关系类型。"
        },
        {
          "id": "ROLE-CHIEF:leads:ROLE-SOL",
          "reason": "untyped-legacy-lead",
          "action": "旧leads无法区分专业指导、架构约束与人事汇报；保留草稿并补有范围和证据的关系类型。"
        },
        {
          "id": "KPI-CH-1:target",
          "reason": "kpi-target-not-adopted",
          "action": "来源的3/5或（xxx）四分位仅是示例；由企业设定并批准自己的目标值"
        },
        {
          "id": "KPI-CH-1:unit",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-CH-1:measurement_period",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-CH-1:measurement_source",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-CH-1:owner",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-CH-1:formula_or_rule",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        }
      ]
    },
    {
      "id": "ROLE-EA",
      "tier": "enterprise",
      "leads": [
        "ROLE-SEG",
        "ROLE-SOL"
      ],
      "relationships": [],
      "assignments": [],
      "state": "needs-input",
      "gaps": [
        {
          "id": "ROLE-EA:leads:ROLE-SEG",
          "reason": "untyped-legacy-lead",
          "action": "旧leads无法区分专业指导、架构约束与人事汇报；保留草稿并补有范围和证据的关系类型。"
        },
        {
          "id": "ROLE-EA:leads:ROLE-SOL",
          "reason": "untyped-legacy-lead",
          "action": "旧leads无法区分专业指导、架构约束与人事汇报；保留草稿并补有范围和证据的关系类型。"
        },
        {
          "id": "KPI-EA-1:unit",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-EA-1:measurement_period",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-EA-1:measurement_source",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-EA-1:owner",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-EA-1:formula_or_rule",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-EA-1:adopted_by",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        }
      ]
    },
    {
      "id": "ROLE-SEG",
      "tier": "segment",
      "leads": [
        "ROLE-SOL"
      ],
      "relationships": [],
      "assignments": [],
      "state": "needs-input",
      "gaps": [
        {
          "id": "ROLE-SEG:leads:ROLE-SOL",
          "reason": "untyped-legacy-lead",
          "action": "旧leads无法区分专业指导、架构约束与人事汇报；保留草稿并补有范围和证据的关系类型。"
        },
        {
          "id": "KPI-SEG-1:unit",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-SEG-1:measurement_period",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-SEG-1:measurement_source",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-SEG-1:owner",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-SEG-1:formula_or_rule",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-SEG-1:adopted_by",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        }
      ]
    },
    {
      "id": "ROLE-SOL",
      "tier": "solution",
      "leads": [],
      "relationships": [],
      "assignments": [],
      "state": "needs-input",
      "gaps": [
        {
          "id": "KPI-SOL-1:unit",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-SOL-1:measurement_period",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-SOL-1:measurement_source",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-SOL-1:owner",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-SOL-1:formula_or_rule",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-SOL-1:adopted_by",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        }
      ]
    }
  ],
  "relationships": [],
  "tiers_present": [
    "chief",
    "enterprise",
    "segment",
    "solution"
  ],
  "gaps": [
    {
      "id": "ROLE-CHIEF:leads:ROLE-EA",
      "reason": "untyped-legacy-lead",
      "action": "旧leads无法区分专业指导、架构约束与人事汇报；保留草稿并补有范围和证据的关系类型。"
    },
    {
      "id": "ROLE-CHIEF:leads:ROLE-SEG",
      "reason": "untyped-legacy-lead",
      "action": "旧leads无法区分专业指导、架构约束与人事汇报；保留草稿并补有范围和证据的关系类型。"
    },
    {
      "id": "ROLE-CHIEF:leads:ROLE-SOL",
      "reason": "untyped-legacy-lead",
      "action": "旧leads无法区分专业指导、架构约束与人事汇报；保留草稿并补有范围和证据的关系类型。"
    },
    {
      "id": "KPI-CH-1:target",
      "reason": "kpi-target-not-adopted",
      "action": "来源的3/5或（xxx）四分位仅是示例；由企业设定并批准自己的目标值"
    },
    {
      "id": "KPI-CH-1:unit",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-CH-1:measurement_period",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-CH-1:measurement_source",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-CH-1:owner",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-CH-1:formula_or_rule",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "ROLE-EA:leads:ROLE-SEG",
      "reason": "untyped-legacy-lead",
      "action": "旧leads无法区分专业指导、架构约束与人事汇报；保留草稿并补有范围和证据的关系类型。"
    },
    {
      "id": "ROLE-EA:leads:ROLE-SOL",
      "reason": "untyped-legacy-lead",
      "action": "旧leads无法区分专业指导、架构约束与人事汇报；保留草稿并补有范围和证据的关系类型。"
    },
    {
      "id": "KPI-EA-1:unit",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-EA-1:measurement_period",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-EA-1:measurement_source",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-EA-1:owner",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-EA-1:formula_or_rule",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-EA-1:adopted_by",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "ROLE-SEG:leads:ROLE-SOL",
      "reason": "untyped-legacy-lead",
      "action": "旧leads无法区分专业指导、架构约束与人事汇报；保留草稿并补有范围和证据的关系类型。"
    },
    {
      "id": "KPI-SEG-1:unit",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-SEG-1:measurement_period",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-SEG-1:measurement_source",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-SEG-1:owner",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-SEG-1:formula_or_rule",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-SEG-1:adopted_by",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-SOL-1:unit",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-SOL-1:measurement_period",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-SOL-1:measurement_source",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-SOL-1:owner",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-SOL-1:formula_or_rule",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-SOL-1:adopted_by",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    }
  ],
  "hierarchy_policy": null,
  "notice": "角色类别不是通用职级总序；专业指导、约束、特化、协作、汇报与交接分别审查。KPI需口径和采用证据，不评价人员绩效、不替代组织批准。"
}
```

修改：把首席架构师满意度KPI改为企业批准目标4/5并附证据。分析结果变化：新增缺口KPI-CH-1:adopted_by；关闭缺口KPI-CH-1:target。修改后结果：

```json
{
  "rows": [
    {
      "id": "ROLE-CHIEF",
      "tier": "chief",
      "leads": [
        "ROLE-EA",
        "ROLE-SEG",
        "ROLE-SOL"
      ],
      "relationships": [],
      "assignments": [],
      "state": "needs-input",
      "gaps": [
        {
          "id": "ROLE-CHIEF:leads:ROLE-EA",
          "reason": "untyped-legacy-lead",
          "action": "旧leads无法区分专业指导、架构约束与人事汇报；保留草稿并补有范围和证据的关系类型。"
        },
        {
          "id": "ROLE-CHIEF:leads:ROLE-SEG",
          "reason": "untyped-legacy-lead",
          "action": "旧leads无法区分专业指导、架构约束与人事汇报；保留草稿并补有范围和证据的关系类型。"
        },
        {
          "id": "ROLE-CHIEF:leads:ROLE-SOL",
          "reason": "untyped-legacy-lead",
          "action": "旧leads无法区分专业指导、架构约束与人事汇报；保留草稿并补有范围和证据的关系类型。"
        },
        {
          "id": "KPI-CH-1:unit",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-CH-1:measurement_period",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-CH-1:measurement_source",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-CH-1:owner",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-CH-1:formula_or_rule",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-CH-1:adopted_by",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        }
      ]
    },
    {
      "id": "ROLE-EA",
      "tier": "enterprise",
      "leads": [
        "ROLE-SEG",
        "ROLE-SOL"
      ],
      "relationships": [],
      "assignments": [],
      "state": "needs-input",
      "gaps": [
        {
          "id": "ROLE-EA:leads:ROLE-SEG",
          "reason": "untyped-legacy-lead",
          "action": "旧leads无法区分专业指导、架构约束与人事汇报；保留草稿并补有范围和证据的关系类型。"
        },
        {
          "id": "ROLE-EA:leads:ROLE-SOL",
          "reason": "untyped-legacy-lead",
          "action": "旧leads无法区分专业指导、架构约束与人事汇报；保留草稿并补有范围和证据的关系类型。"
        },
        {
          "id": "KPI-EA-1:unit",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-EA-1:measurement_period",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-EA-1:measurement_source",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-EA-1:owner",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-EA-1:formula_or_rule",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-EA-1:adopted_by",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        }
      ]
    },
    {
      "id": "ROLE-SEG",
      "tier": "segment",
      "leads": [
        "ROLE-SOL"
      ],
      "relationships": [],
      "assignments": [],
      "state": "needs-input",
      "gaps": [
        {
          "id": "ROLE-SEG:leads:ROLE-SOL",
          "reason": "untyped-legacy-lead",
          "action": "旧leads无法区分专业指导、架构约束与人事汇报；保留草稿并补有范围和证据的关系类型。"
        },
        {
          "id": "KPI-SEG-1:unit",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-SEG-1:measurement_period",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-SEG-1:measurement_source",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-SEG-1:owner",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-SEG-1:formula_or_rule",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-SEG-1:adopted_by",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        }
      ]
    },
    {
      "id": "ROLE-SOL",
      "tier": "solution",
      "leads": [],
      "relationships": [],
      "assignments": [],
      "state": "needs-input",
      "gaps": [
        {
          "id": "KPI-SOL-1:unit",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-SOL-1:measurement_period",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-SOL-1:measurement_source",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-SOL-1:owner",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-SOL-1:formula_or_rule",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        },
        {
          "id": "KPI-SOL-1:adopted_by",
          "reason": "missing-input",
          "action": "由责任人补充来源与值；不把未知填为通过或零"
        }
      ]
    }
  ],
  "relationships": [],
  "tiers_present": [
    "chief",
    "enterprise",
    "segment",
    "solution"
  ],
  "gaps": [
    {
      "id": "ROLE-CHIEF:leads:ROLE-EA",
      "reason": "untyped-legacy-lead",
      "action": "旧leads无法区分专业指导、架构约束与人事汇报；保留草稿并补有范围和证据的关系类型。"
    },
    {
      "id": "ROLE-CHIEF:leads:ROLE-SEG",
      "reason": "untyped-legacy-lead",
      "action": "旧leads无法区分专业指导、架构约束与人事汇报；保留草稿并补有范围和证据的关系类型。"
    },
    {
      "id": "ROLE-CHIEF:leads:ROLE-SOL",
      "reason": "untyped-legacy-lead",
      "action": "旧leads无法区分专业指导、架构约束与人事汇报；保留草稿并补有范围和证据的关系类型。"
    },
    {
      "id": "KPI-CH-1:unit",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-CH-1:measurement_period",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-CH-1:measurement_source",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-CH-1:owner",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-CH-1:formula_or_rule",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-CH-1:adopted_by",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "ROLE-EA:leads:ROLE-SEG",
      "reason": "untyped-legacy-lead",
      "action": "旧leads无法区分专业指导、架构约束与人事汇报；保留草稿并补有范围和证据的关系类型。"
    },
    {
      "id": "ROLE-EA:leads:ROLE-SOL",
      "reason": "untyped-legacy-lead",
      "action": "旧leads无法区分专业指导、架构约束与人事汇报；保留草稿并补有范围和证据的关系类型。"
    },
    {
      "id": "KPI-EA-1:unit",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-EA-1:measurement_period",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-EA-1:measurement_source",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-EA-1:owner",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-EA-1:formula_or_rule",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-EA-1:adopted_by",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "ROLE-SEG:leads:ROLE-SOL",
      "reason": "untyped-legacy-lead",
      "action": "旧leads无法区分专业指导、架构约束与人事汇报；保留草稿并补有范围和证据的关系类型。"
    },
    {
      "id": "KPI-SEG-1:unit",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-SEG-1:measurement_period",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-SEG-1:measurement_source",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-SEG-1:owner",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-SEG-1:formula_or_rule",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-SEG-1:adopted_by",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-SOL-1:unit",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-SOL-1:measurement_period",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-SOL-1:measurement_source",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-SOL-1:owner",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-SOL-1:formula_or_rule",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    },
    {
      "id": "KPI-SOL-1:adopted_by",
      "reason": "missing-input",
      "action": "由责任人补充来源与值；不把未知填为通过或零"
    }
  ],
  "hierarchy_policy": null,
  "notice": "角色类别不是通用职级总序；专业指导、约束、特化、协作、汇报与交接分别审查。KPI需口径和采用证据，不评价人员绩效、不替代组织批准。"
}
```

反例：角色关系引用不存在的角色。实际拒绝：`ROLE-REL [REL-BROKEN]: Relationship target must be another declared role`

完整模型片段见 [能力注册](../capabilities/architecture-role-catalog.md)。以上全部为虚构教学材料，不代表真实企业事实或批准。
