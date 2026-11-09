# 解决方案协作冲刺协作图

`profile_id`: agile-solution-collaboration；`artifact_id`: architecture-project-schedule；主责：[togaf-architecture-workbench](../../../togaf-architecture-workbench/SKILL.md)。

来源：G210 §3.3、§3.3.6；G210 图3-3。

## 构图与定义状态

表示族：`agile-sprints`；输出：`diagram`。规范版本：2.1-agile-1。

{
  "id": "agile-solution-collaboration",
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
      "id": "scope-solution",
      "description": "解决方案协作备选范围"
    }
  ],
  "entities": [
    {
      "id": "solution-vision",
      "type": "guide:agile_context",
      "name": "业务愿景：座位预约与无障碍协助",
      "scope_id": "scope-solution",
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
      "id": "solution-s0",
      "type": "guide:agile_sprint",
      "name": "冲刺0",
      "scope_id": "scope-solution",
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
      "id": "solution-dorp0",
      "type": "guide:dorp_gate",
      "name": "DORP0",
      "scope_id": "scope-solution",
      "attributes": {
        "sprint_ref": "solution-s0",
        "outputs": [
          {
            "id": "solution-BACKLOG0",
            "kind": "待办",
            "lane": "ea",
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
      "id": "solution-s1",
      "type": "guide:agile_sprint",
      "name": "冲刺1",
      "scope_id": "scope-solution",
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
      "id": "solution-dorp1",
      "type": "guide:dorp_gate",
      "name": "DORP1",
      "scope_id": "scope-solution",
      "attributes": {
        "sprint_ref": "solution-s1",
        "outputs": [
          {
            "id": "solution-MVA1",
            "kind": "MVA",
            "lane": "ea",
            "necessity": "optional",
            "meaning": "候选可演示增量；不等于每轮必需/已上线"
          },
          {
            "id": "solution-MVP1",
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
      "id": "solution-ea1",
      "type": "guide:agile_activity",
      "name": "企业架构团队·冲刺1",
      "scope_id": "scope-solution",
      "attributes": {
        "sprint_ref": "solution-s1",
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
      "id": "solution-solution1",
      "type": "guide:agile_activity",
      "name": "解决方案团队·冲刺1",
      "scope_id": "scope-solution",
      "attributes": {
        "sprint_ref": "solution-s1",
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
      "id": "solution-s2",
      "type": "guide:agile_sprint",
      "name": "冲刺2",
      "scope_id": "scope-solution",
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
      "id": "solution-dorp2",
      "type": "guide:dorp_gate",
      "name": "DORP2",
      "scope_id": "scope-solution",
      "attributes": {
        "sprint_ref": "solution-s2",
        "outputs": [
          {
            "id": "solution-MVA2",
            "kind": "MVA",
            "lane": "ea",
            "necessity": "optional",
            "meaning": "候选可演示增量；不等于每轮必需/已上线"
          },
          {
            "id": "solution-MVP2",
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
      "id": "solution-ea2",
      "type": "guide:agile_activity",
      "name": "企业架构团队·冲刺2",
      "scope_id": "scope-solution",
      "attributes": {
        "sprint_ref": "solution-s2",
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
      "id": "solution-solution2",
      "type": "guide:agile_activity",
      "name": "解决方案团队·冲刺2",
      "scope_id": "scope-solution",
      "attributes": {
        "sprint_ref": "solution-s2",
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
      "id": "solution-s3",
      "type": "guide:agile_sprint",
      "name": "冲刺…（本例3）",
      "scope_id": "scope-solution",
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
      "id": "solution-dorp3",
      "type": "guide:dorp_gate",
      "name": "DORP3",
      "scope_id": "scope-solution",
      "attributes": {
        "sprint_ref": "solution-s3",
        "outputs": [
          {
            "id": "solution-MVP3",
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
      "id": "solution-ea3",
      "type": "guide:agile_activity",
      "name": "企业架构团队·冲刺…（本例3）",
      "scope_id": "scope-solution",
      "attributes": {
        "sprint_ref": "solution-s3",
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
      "id": "solution-solution3",
      "type": "guide:agile_activity",
      "name": "解决方案团队·冲刺…（本例3）",
      "scope_id": "scope-solution",
      "attributes": {
        "sprint_ref": "solution-s3",
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
      "id": "solution-start-ea",
      "type": "guide:agile_handoff",
      "source": "solution-vision",
      "target": "solution-ea1",
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
      "id": "solution-continue-ea1",
      "type": "guide:agile_continues",
      "source": "solution-ea1",
      "target": "solution-ea2",
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
      "id": "solution-continue-ea2",
      "type": "guide:agile_continues",
      "source": "solution-ea2",
      "target": "solution-ea3",
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
      "id": "solution-start-solution",
      "type": "guide:agile_handoff",
      "source": "solution-vision",
      "target": "solution-solution1",
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
      "id": "solution-continue-solution1",
      "type": "guide:agile_continues",
      "source": "solution-solution1",
      "target": "solution-solution2",
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
      "id": "solution-continue-solution2",
      "type": "guide:agile_continues",
      "source": "solution-solution2",
      "target": "solution-solution3",
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
      "id": "solution-MVA-handoff1",
      "type": "guide:agile_handoff",
      "source": "solution-ea1",
      "target": "solution-solution2",
      "label": "MVA由后续方案冲刺消费",
      "attributes": {
        "output_kind": "MVA",
        "output_id": "solution-MVA1",
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
      "id": "solution-MVA-handoff2",
      "type": "guide:agile_handoff",
      "source": "solution-ea2",
      "target": "solution-solution3",
      "label": "MVA由后续方案冲刺消费",
      "attributes": {
        "output_kind": "MVA",
        "output_id": "solution-MVA2",
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
      "id": "solution-collab-ea-solution1",
      "type": "guide:agile_collaborates",
      "source": "solution-ea1",
      "target": "solution-solution1",
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
      "id": "solution-collab-ea-solution2",
      "type": "guide:agile_collaborates",
      "source": "solution-ea2",
      "target": "solution-solution2",
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
      "id": "solution-collab-ea-solution3",
      "type": "guide:agile_collaborates",
      "source": "solution-ea3",
      "target": "solution-solution3",
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
    "id": "v-agile-solution-collaboration",
    "artifact_id": "architecture-project-schedule",
    "profile_id": "agile-solution-collaboration",
    "title": "解决方案协作：预约服务备选推演",
    "scope_id": "scope-solution",
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
      "solution-vision",
      "solution-s0",
      "solution-dorp0",
      "solution-s1",
      "solution-dorp1",
      "solution-ea1",
      "solution-solution1",
      "solution-s2",
      "solution-dorp2",
      "solution-ea2",
      "solution-solution2",
      "solution-s3",
      "solution-dorp3",
      "solution-ea3",
      "solution-solution3"
    ],
    "relationship_ids": [
      "solution-start-ea",
      "solution-continue-ea1",
      "solution-continue-ea2",
      "solution-start-solution",
      "solution-continue-solution1",
      "solution-continue-solution2",
      "solution-MVA-handoff1",
      "solution-MVA-handoff2",
      "solution-collab-ea-solution1",
      "solution-collab-ea-solution2",
      "solution-collab-ea-solution3"
    ],
    "analysis": "R01–R06及选择表；开放序列只是参数化片段，非成熟度等级。",
    "legend": "MVA最小可行架构；MVBD最小可行业务开发；MVP最小可行产品。DORP为演示/成果/回顾/规划，不是实施阶段。",
    "attributes": {
      "sprint_pattern": {
        "pattern": "solution",
        "pattern_label": "解决方案协作",
        "lanes": [
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
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile agile-solution-collaboration --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile agile-solution-collaboration --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
