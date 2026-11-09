# 跨开发协作冲刺协作图

`profile_id`: agile-cross-development；`artifact_id`: architecture-project-schedule；主责：[togaf-architecture-workbench](../../../togaf-architecture-workbench/SKILL.md)。

来源：G210 §3.3、§3.3.7；G210 图3-4。

## 构图与定义状态

表示族：`agile-sprints`；输出：`diagram`。规范版本：2.1-agile-1。

{
  "id": "agile-cross-development",
  "version": "1.0",
  "source_verified": false,
  "structure": "sprint-columns; DORP boundaries; parallel lanes; output markers; handoff distinct from symmetric collaboration"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:agile_sprint, guide:agile_activity, guide:dorp_gate, guide:agile_context。关系类型：guide:agile_handoff, guide:agile_continues, guide:agile_collaborates, guide:agile_finalizes。

```json
{
  "entities": {
    "guide:agile_sprint": [
      "order",
      "timebox",
      "goal",
      "display_label"
    ],
    "guide:agile_activity": [
      "sprint_ref",
      "lane",
      "team",
      "capabilities",
      "work",
      "parallel_teams",
      "selection_basis"
    ],
    "guide:dorp_gate": [
      "sprint_ref",
      "outputs",
      "dorp_actions",
      "unfinished_return",
      "coordination"
    ],
    "guide:agile_context": [
      "role",
      "business_change",
      "backlog",
      "boundary",
      "source_boundary"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- DORP边界及四活动
- 冲刺0不虚构增量
- 交接后续冲刺
- 协作双向且同冲刺
- 混合每队三能力
- 非成熟度评分

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "四个备选推演；非同时发生/成熟度等级",
  "raw_input": "examples/addenda/agile-collaboration/raw-business-materials.json",
  "analysis_path": "examples/addenda/agile-collaboration/analysis.md",
  "sources": [
    {
      "id": "raw-agile",
      "kind": "example",
      "description": "虚构云港城市图书馆预约服务，原业务材料在本包内，未声称真实批准。",
      "locator": "examples/addenda/agile-collaboration/raw-business-materials.json"
    },
    {
      "id": "guide-agile",
      "kind": "local-translation",
      "description": "G210本地正文§3.3–3.3.8；历史图JSON不证明本轮原图已核验。",
      "locator": "references/source-tables/agile-collaboration-patterns.json"
    }
  ],
  "scopes": [
    {
      "id": "scope-cross",
      "description": "跨开发协作备选范围"
    }
  ],
  "entities": [
    {
      "id": "cross-vision",
      "type": "guide:agile_context",
      "name": "业务愿景：座位预约与无障碍协助",
      "scope_id": "scope-cross",
      "attributes": {
        "role": "input",
        "business_change": "可靠确认、可访问服务；独立备选推演",
        "backlog": [
          "B-BOOK预约",
          "B-CANCEL取消",
          "G-PRIV隐私待确认"
        ],
        "boundary": "候选组织方案；没有上线许可",
        "source_boundary": "正文＋历史JSON解释；当前原图缺失"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "cross-s0",
      "type": "guide:agile_sprint",
      "name": "冲刺0",
      "scope_id": "scope-cross",
      "attributes": {
        "order": 0,
        "timebox": "2周（R06项目约定）",
        "goal": "愿景与待办",
        "display_label": "冲刺0"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "cross-dorp0",
      "type": "guide:dorp_gate",
      "name": "DORP0",
      "scope_id": "scope-cross",
      "attributes": {
        "sprint_ref": "cross-s0",
        "outputs": [
          {
            "id": "cross-BACKLOG0",
            "kind": "待办",
            "lane": "business",
            "necessity": "required",
            "meaning": "业务变革待办，不是MVA/MVP"
          }
        ],
        "dorp_actions": [
          "演示",
          "成果管理",
          "回顾",
          "下一冲刺规划"
        ],
        "unfinished_return": "保留ID回到业务待办",
        "coordination": "与利益相关者核对目标价值；混合团队在冲刺末协调"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "cross-s1",
      "type": "guide:agile_sprint",
      "name": "冲刺1",
      "scope_id": "scope-cross",
      "attributes": {
        "order": 1,
        "timebox": "2周（R06项目约定）",
        "goal": "预约确认",
        "display_label": "冲刺1"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "cross-dorp1",
      "type": "guide:dorp_gate",
      "name": "DORP1",
      "scope_id": "scope-cross",
      "attributes": {
        "sprint_ref": "cross-s1",
        "outputs": [
          {
            "id": "cross-MVBD1",
            "kind": "MVBD",
            "lane": "business",
            "necessity": "optional",
            "meaning": "候选可演示增量；不等于每轮必需/已上线"
          },
          {
            "id": "cross-MVA1",
            "kind": "MVA",
            "lane": "ea",
            "necessity": "optional",
            "meaning": "候选可演示增量；不等于每轮必需/已上线"
          },
          {
            "id": "cross-MVP1",
            "kind": "MVP",
            "lane": "solution",
            "necessity": "optional",
            "meaning": "候选可演示增量；不等于每轮必需/已上线"
          }
        ],
        "dorp_actions": [
          "演示",
          "成果管理",
          "回顾",
          "下一冲刺规划"
        ],
        "unfinished_return": "保留ID回到业务待办",
        "coordination": "与利益相关者核对目标价值；混合团队在冲刺末协调"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "cross-business1",
      "type": "guide:agile_activity",
      "name": "业务开发团队·冲刺1",
      "scope_id": "scope-cross",
      "attributes": {
        "sprint_ref": "cross-s1",
        "lane": "business",
        "team": "BUS-T候选",
        "capabilities": [
          "业务开发"
        ],
        "work": "形成该轮目标的可演示切片",
        "parallel_teams": 1,
        "selection_basis": "R02/R05备选推演；是否采用见选择表"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "cross-ea1",
      "type": "guide:agile_activity",
      "name": "企业架构团队·冲刺1",
      "scope_id": "scope-cross",
      "attributes": {
        "sprint_ref": "cross-s1",
        "lane": "ea",
        "team": "EA-T",
        "capabilities": [
          "企业架构"
        ],
        "work": "形成该轮目标的可演示切片",
        "parallel_teams": 1,
        "selection_basis": "R02/R05备选推演；是否采用见选择表"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "cross-solution1",
      "type": "guide:agile_activity",
      "name": "解决方案团队·冲刺1",
      "scope_id": "scope-cross",
      "attributes": {
        "sprint_ref": "cross-s1",
        "lane": "solution",
        "team": "DEV-A / DEV-B",
        "capabilities": [
          "解决方案开发"
        ],
        "work": "业务待办样机，不消费MVA0",
        "parallel_teams": 2,
        "selection_basis": "R02/R05备选推演；是否采用见选择表"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "cross-s2",
      "type": "guide:agile_sprint",
      "name": "冲刺2",
      "scope_id": "scope-cross",
      "attributes": {
        "order": 2,
        "timebox": "2周（R06项目约定）",
        "goal": "取消与容量",
        "display_label": "冲刺2"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "cross-dorp2",
      "type": "guide:dorp_gate",
      "name": "DORP2",
      "scope_id": "scope-cross",
      "attributes": {
        "sprint_ref": "cross-s2",
        "outputs": [
          {
            "id": "cross-MVBD2",
            "kind": "MVBD",
            "lane": "business",
            "necessity": "optional",
            "meaning": "候选可演示增量；不等于每轮必需/已上线"
          },
          {
            "id": "cross-MVA2",
            "kind": "MVA",
            "lane": "ea",
            "necessity": "optional",
            "meaning": "候选可演示增量；不等于每轮必需/已上线"
          },
          {
            "id": "cross-MVP2",
            "kind": "MVP",
            "lane": "solution",
            "necessity": "optional",
            "meaning": "候选可演示增量；不等于每轮必需/已上线"
          }
        ],
        "dorp_actions": [
          "演示",
          "成果管理",
          "回顾",
          "下一冲刺规划"
        ],
        "unfinished_return": "保留ID回到业务待办",
        "coordination": "与利益相关者核对目标价值；混合团队在冲刺末协调"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "cross-business2",
      "type": "guide:agile_activity",
      "name": "业务开发团队·冲刺2",
      "scope_id": "scope-cross",
      "attributes": {
        "sprint_ref": "cross-s2",
        "lane": "business",
        "team": "BUS-T候选",
        "capabilities": [
          "业务开发"
        ],
        "work": "形成该轮目标的可演示切片",
        "parallel_teams": 1,
        "selection_basis": "R02/R05备选推演；是否采用见选择表"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "cross-ea2",
      "type": "guide:agile_activity",
      "name": "企业架构团队·冲刺2",
      "scope_id": "scope-cross",
      "attributes": {
        "sprint_ref": "cross-s2",
        "lane": "ea",
        "team": "EA-T",
        "capabilities": [
          "企业架构"
        ],
        "work": "形成该轮目标的可演示切片",
        "parallel_teams": 1,
        "selection_basis": "R02/R05备选推演；是否采用见选择表"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "cross-solution2",
      "type": "guide:agile_activity",
      "name": "解决方案团队·冲刺2",
      "scope_id": "scope-cross",
      "attributes": {
        "sprint_ref": "cross-s2",
        "lane": "solution",
        "team": "DEV-A / DEV-B",
        "capabilities": [
          "解决方案开发"
        ],
        "work": "形成该轮目标的可演示切片",
        "parallel_teams": 2,
        "selection_basis": "R02/R05备选推演；是否采用见选择表"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "cross-s3",
      "type": "guide:agile_sprint",
      "name": "冲刺…（本例3）",
      "scope_id": "scope-cross",
      "attributes": {
        "order": 3,
        "timebox": "2周（R06项目约定）",
        "goal": "无障碍协助",
        "display_label": "冲刺…（本例3）"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "cross-dorp3",
      "type": "guide:dorp_gate",
      "name": "DORP3",
      "scope_id": "scope-cross",
      "attributes": {
        "sprint_ref": "cross-s3",
        "outputs": [
          {
            "id": "cross-MVP3",
            "kind": "MVP",
            "lane": "solution",
            "necessity": "optional",
            "meaning": "候选可演示增量；不等于每轮必需/已上线"
          }
        ],
        "dorp_actions": [
          "演示",
          "成果管理",
          "回顾",
          "下一冲刺规划"
        ],
        "unfinished_return": "保留ID回到业务待办",
        "coordination": "与利益相关者核对目标价值；混合团队在冲刺末协调"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "cross-business3",
      "type": "guide:agile_activity",
      "name": "业务开发团队·冲刺…（本例3）",
      "scope_id": "scope-cross",
      "attributes": {
        "sprint_ref": "cross-s3",
        "lane": "business",
        "team": "BUS-T候选",
        "capabilities": [
          "业务开发"
        ],
        "work": "形成该轮目标的可演示切片",
        "parallel_teams": 1,
        "selection_basis": "R02/R05备选推演；是否采用见选择表"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "cross-ea3",
      "type": "guide:agile_activity",
      "name": "企业架构团队·冲刺…（本例3）",
      "scope_id": "scope-cross",
      "attributes": {
        "sprint_ref": "cross-s3",
        "lane": "ea",
        "team": "EA-T",
        "capabilities": [
          "企业架构"
        ],
        "work": "形成该轮目标的可演示切片",
        "parallel_teams": 1,
        "selection_basis": "R02/R05备选推演；是否采用见选择表"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "cross-solution3",
      "type": "guide:agile_activity",
      "name": "解决方案团队·冲刺…（本例3）",
      "scope_id": "scope-cross",
      "attributes": {
        "sprint_ref": "cross-s3",
        "lane": "solution",
        "team": "DEV-A / DEV-B",
        "capabilities": [
          "解决方案开发"
        ],
        "work": "形成该轮目标的可演示切片",
        "parallel_teams": 2,
        "selection_basis": "R02/R05备选推演；是否采用见选择表"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    }
  ],
  "relationships": [
    {
      "id": "cross-start-business",
      "type": "guide:agile_handoff",
      "source": "cross-vision",
      "target": "cross-business1",
      "label": "冲刺0愿景/待办进入首轮",
      "attributes": {
        "output_kind": "BACKLOG",
        "timing": "冲刺0之后；不是MVA0",
        "review": "DORP0计划"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cross-continue-business1",
      "type": "guide:agile_continues",
      "source": "cross-business1",
      "target": "cross-business2",
      "label": "同泳道滚动延续",
      "attributes": {
        "timing": "k→k+1",
        "review": "DORP回顾/规划；未完成回流"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cross-continue-business2",
      "type": "guide:agile_continues",
      "source": "cross-business2",
      "target": "cross-business3",
      "label": "同泳道滚动延续",
      "attributes": {
        "timing": "k→k+1",
        "review": "DORP回顾/规划；未完成回流"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cross-start-ea",
      "type": "guide:agile_handoff",
      "source": "cross-vision",
      "target": "cross-ea1",
      "label": "冲刺0愿景/待办进入首轮",
      "attributes": {
        "output_kind": "BACKLOG",
        "timing": "冲刺0之后；不是MVA0",
        "review": "DORP0计划"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cross-continue-ea1",
      "type": "guide:agile_continues",
      "source": "cross-ea1",
      "target": "cross-ea2",
      "label": "同泳道滚动延续",
      "attributes": {
        "timing": "k→k+1",
        "review": "DORP回顾/规划；未完成回流"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cross-continue-ea2",
      "type": "guide:agile_continues",
      "source": "cross-ea2",
      "target": "cross-ea3",
      "label": "同泳道滚动延续",
      "attributes": {
        "timing": "k→k+1",
        "review": "DORP回顾/规划；未完成回流"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cross-start-solution",
      "type": "guide:agile_handoff",
      "source": "cross-vision",
      "target": "cross-solution1",
      "label": "冲刺0愿景/待办进入首轮",
      "attributes": {
        "output_kind": "BACKLOG",
        "timing": "冲刺0之后；不是MVA0",
        "review": "DORP0计划"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cross-continue-solution1",
      "type": "guide:agile_continues",
      "source": "cross-solution1",
      "target": "cross-solution2",
      "label": "同泳道滚动延续",
      "attributes": {
        "timing": "k→k+1",
        "review": "DORP回顾/规划；未完成回流"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cross-continue-solution2",
      "type": "guide:agile_continues",
      "source": "cross-solution2",
      "target": "cross-solution3",
      "label": "同泳道滚动延续",
      "attributes": {
        "timing": "k→k+1",
        "review": "DORP回顾/规划；未完成回流"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cross-MVA-handoff1",
      "type": "guide:agile_handoff",
      "source": "cross-ea1",
      "target": "cross-solution2",
      "label": "MVA由后续方案冲刺消费",
      "attributes": {
        "output_kind": "MVA",
        "output_id": "cross-MVA1",
        "timing": "k→k+1",
        "review": "DORP架构演示后交接"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cross-MVA-handoff2",
      "type": "guide:agile_handoff",
      "source": "cross-ea2",
      "target": "cross-solution3",
      "label": "MVA由后续方案冲刺消费",
      "attributes": {
        "output_kind": "MVA",
        "output_id": "cross-MVA2",
        "timing": "k→k+1",
        "review": "DORP架构演示后交接"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cross-MVBD-handoff1",
      "type": "guide:agile_handoff",
      "source": "cross-business1",
      "target": "cross-ea2",
      "label": "MVBD由后续架构冲刺消费",
      "attributes": {
        "output_kind": "MVBD",
        "output_id": "cross-MVBD1",
        "timing": "k→k+1",
        "review": "DORP业务演示后交接"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cross-MVBD-handoff2",
      "type": "guide:agile_handoff",
      "source": "cross-business2",
      "target": "cross-ea3",
      "label": "MVBD由后续架构冲刺消费",
      "attributes": {
        "output_kind": "MVBD",
        "output_id": "cross-MVBD2",
        "timing": "k→k+1",
        "review": "DORP业务演示后交接"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cross-collab-business-ea1",
      "type": "guide:agile_collaborates",
      "source": "cross-business1",
      "target": "cross-ea1",
      "label": "协作、敏捷治理与支持",
      "attributes": {
        "timing": "same-sprint",
        "directionality": "symmetric",
        "review": "支持当前成果、反馈下一增量；非数据流"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cross-collab-business-solution1",
      "type": "guide:agile_collaborates",
      "source": "cross-business1",
      "target": "cross-solution1",
      "label": "协作、敏捷治理与支持",
      "attributes": {
        "timing": "same-sprint",
        "directionality": "symmetric",
        "review": "支持当前成果、反馈下一增量；非数据流"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cross-collab-ea-solution1",
      "type": "guide:agile_collaborates",
      "source": "cross-ea1",
      "target": "cross-solution1",
      "label": "协作、敏捷治理与支持",
      "attributes": {
        "timing": "same-sprint",
        "directionality": "symmetric",
        "review": "支持当前成果、反馈下一增量；非数据流"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cross-collab-business-ea2",
      "type": "guide:agile_collaborates",
      "source": "cross-business2",
      "target": "cross-ea2",
      "label": "协作、敏捷治理与支持",
      "attributes": {
        "timing": "same-sprint",
        "directionality": "symmetric",
        "review": "支持当前成果、反馈下一增量；非数据流"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cross-collab-business-solution2",
      "type": "guide:agile_collaborates",
      "source": "cross-business2",
      "target": "cross-solution2",
      "label": "协作、敏捷治理与支持",
      "attributes": {
        "timing": "same-sprint",
        "directionality": "symmetric",
        "review": "支持当前成果、反馈下一增量；非数据流"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cross-collab-ea-solution2",
      "type": "guide:agile_collaborates",
      "source": "cross-ea2",
      "target": "cross-solution2",
      "label": "协作、敏捷治理与支持",
      "attributes": {
        "timing": "same-sprint",
        "directionality": "symmetric",
        "review": "支持当前成果、反馈下一增量；非数据流"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cross-collab-business-ea3",
      "type": "guide:agile_collaborates",
      "source": "cross-business3",
      "target": "cross-ea3",
      "label": "协作、敏捷治理与支持",
      "attributes": {
        "timing": "same-sprint",
        "directionality": "symmetric",
        "review": "支持当前成果、反馈下一增量；非数据流"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cross-collab-business-solution3",
      "type": "guide:agile_collaborates",
      "source": "cross-business3",
      "target": "cross-solution3",
      "label": "协作、敏捷治理与支持",
      "attributes": {
        "timing": "same-sprint",
        "directionality": "symmetric",
        "review": "支持当前成果、反馈下一增量；非数据流"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cross-collab-ea-solution3",
      "type": "guide:agile_collaborates",
      "source": "cross-ea3",
      "target": "cross-solution3",
      "label": "协作、敏捷治理与支持",
      "attributes": {
        "timing": "same-sprint",
        "directionality": "symmetric",
        "review": "支持当前成果、反馈下一增量；非数据流"
      },
      "evidence": [
        "raw-agile",
        "guide-agile"
      ],
      "certainty": "assumed"
    }
  ],
  "extensions": {
    "relationship_types": {
      "guide:agile_handoff": {
        "source_types": [
          "guide:agile_activity",
          "guide:agile_context"
        ],
        "target_types": [
          "guide:agile_activity",
          "guide:agile_context"
        ],
        "meaning": "前冲刺成果经DORP评审移交后续冲刺，有方向"
      },
      "guide:agile_continues": {
        "source_types": [
          "guide:agile_activity",
          "guide:agile_context"
        ],
        "target_types": [
          "guide:agile_activity",
          "guide:agile_context"
        ],
        "meaning": "同泳道下一冲刺的滚动延续，不等于一个ADM阶段"
      },
      "guide:agile_collaborates": {
        "source_types": [
          "guide:agile_activity",
          "guide:agile_context"
        ],
        "target_types": [
          "guide:agile_activity",
          "guide:agile_context"
        ],
        "meaning": "同冲刺不同团队的对称协作、敏捷治理与支持；不是有向数据流"
      },
      "guide:agile_finalizes": {
        "source_types": [
          "guide:agile_activity",
          "guide:agile_context"
        ],
        "target_types": [
          "guide:agile_activity",
          "guide:agile_context"
        ],
        "meaning": "仅EA模式形成最终产品架构后安排实施，本图不伪造实施任务"
      }
    }
  },
  "view": {
    "id": "v-agile-cross-development",
    "artifact_id": "architecture-project-schedule",
    "profile_id": "agile-cross-development",
    "title": "跨开发协作：预约服务备选推演",
    "scope_id": "scope-cross",
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
      "cross-vision",
      "cross-s0",
      "cross-dorp0",
      "cross-s1",
      "cross-dorp1",
      "cross-business1",
      "cross-ea1",
      "cross-solution1",
      "cross-s2",
      "cross-dorp2",
      "cross-business2",
      "cross-ea2",
      "cross-solution2",
      "cross-s3",
      "cross-dorp3",
      "cross-business3",
      "cross-ea3",
      "cross-solution3"
    ],
    "relationship_ids": [
      "cross-start-business",
      "cross-continue-business1",
      "cross-continue-business2",
      "cross-start-ea",
      "cross-continue-ea1",
      "cross-continue-ea2",
      "cross-start-solution",
      "cross-continue-solution1",
      "cross-continue-solution2",
      "cross-MVA-handoff1",
      "cross-MVA-handoff2",
      "cross-MVBD-handoff1",
      "cross-MVBD-handoff2",
      "cross-collab-business-ea1",
      "cross-collab-business-solution1",
      "cross-collab-ea-solution1",
      "cross-collab-business-ea2",
      "cross-collab-business-solution2",
      "cross-collab-ea-solution2",
      "cross-collab-business-ea3",
      "cross-collab-business-solution3",
      "cross-collab-ea-solution3"
    ],
    "analysis": "R01–R06及选择表；开放序列只是参数化片段，非成熟度等级。",
    "legend": "MVA最小可行架构；MVBD最小可行业务开发；MVP最小可行产品。DORP为演示/成果/回顾/规划，不是实施阶段。",
    "attributes": {
      "sprint_pattern": {
        "pattern": "cross",
        "pattern_label": "跨开发协作",
        "lanes": [
          {
            "id": "business",
            "label": "业务开发团队"
          },
          {
            "id": "ea",
            "label": "企业架构团队"
          },
          {
            "id": "solution",
            "label": "解决方案团队"
          }
        ],
        "adaptive_columns": 2,
        "decision": "四图分别推演备选方式；采用与依据见选择表。"
      }
    }
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile agile-cross-development --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile agile-cross-development --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
