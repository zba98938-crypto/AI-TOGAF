# DTRA因素与ADM阶段对齐

`profile_id`: dtra-adm-phase-alignment-default；`artifact_id`: dtra-adm-phase-alignment；主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G212 §6、表6-1、图6-1。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：1.0。

{
  "id": "dtra-adm-phase-alignment-default",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "按工作产品字段组织的记录表；来源无对应原图。",
  "structure_basis": "正文定义的工作产品；记录表是项目操作表示法，不冒充来源原图"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:dtra-alignment-summary, guide:dtra-phase-record。关系类型：。

```json
{
  "entities": {
    "guide:dtra-alignment-summary": [
      "assessment_ref",
      "initiated_in_phase",
      "factor_ratings",
      "reassessment"
    ],
    "guide:dtra-phase-record": [
      "phase",
      "implication",
      "actions"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 对象、关系、必要属性均可追溯并得到表达
- 参考内容不自动成为项目事实；未知项保持显式
- 阶段-因素映射来自图6-1同区位置推断，不是原文逐条规定
- 阶段G治理指实施方法恰当性，不是“治理与合规”因素
- 评分低于“同意”只触发复核，不是不合格判定

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构星河零售教学案例；规则不是TOGAF规定，不代表批准。",
  "sources": [
    {
      "id": "DAP-R1",
      "kind": "example",
      "description": "虚构DTRA问卷汇总（DTRA-2026Q3）：文化4、IT能力5、生态系统5，其余因素6或7；评估在阶段A启动。",
      "locator": "raw-materials.json#DAP-R1"
    },
    {
      "id": "DAP-R2",
      "kind": "example",
      "description": "各阶段行动记录：B阶段安排文化变革工作坊；C/D阶段安排伙伴生态评审；D阶段安排平台能力补强；周期结束复评。",
      "locator": "raw-materials.json#DAP-R2"
    }
  ],
  "entities": [
    {
      "id": "DAP-SUM",
      "type": "guide:dtra-alignment-summary",
      "name": "DTRA与ADM对齐汇总",
      "attributes": {
        "assessment_ref": "DTRA-2026Q3",
        "initiated_in_phase": "A",
        "factor_ratings": {
          "vision": 6,
          "sponsorship-direction": 7,
          "it-capability": 5,
          "culture": 4,
          "scope-scale": 6,
          "business-rationale": 7,
          "implementation-approach": 6,
          "business-model-adaptability": 6,
          "skills-competence": 6,
          "technology-maturity": 6,
          "ecosystem": 5,
          "governance-compliance": 6,
          "value-realization": 6,
          "policy-regulations": 7,
          "funding-resources": 6
        },
        "reassessment": "end-of-cycle",
        "progression_note": "文化与IT能力补强先于生态系统扩展；生态评审只做准备性工作"
      },
      "evidence": [
        "DAP-R1"
      ],
      "certainty": "assumed"
    },
    {
      "id": "DAP-Preliminary",
      "type": "guide:dtra-phase-record",
      "name": "DTRA阶段记录：Preliminary",
      "attributes": {
        "phase": "Preliminary",
        "implication": "理解企业能力、所用架构框架与治理框架中驱动数字采用的因素；定义架构原则；确定组织期望的、聚焦数字技术的架构能力",
        "considered_factor_ids": [
          "vision",
          "sponsorship-direction"
        ],
        "actions": [
          {
            "id": "ACT-Preliminary",
            "factor_ids": [],
            "action": "按表6-1含义记录本阶段考虑"
          }
        ]
      },
      "evidence": [
        "DAP-R2"
      ],
      "certainty": "assumed"
    },
    {
      "id": "DAP-A",
      "type": "guide:dtra-phase-record",
      "name": "DTRA阶段记录：A",
      "attributes": {
        "phase": "A",
        "implication": "捕获目标状态高层愿景；识别利益相关者及业务驱动和关注点并开展就绪度评估；依评估输出选择架构路径",
        "considered_factor_ids": [
          "vision",
          "sponsorship-direction"
        ],
        "actions": [
          {
            "id": "ACT-A",
            "factor_ids": [],
            "action": "按表6-1含义记录本阶段考虑"
          }
        ]
      },
      "evidence": [
        "DAP-R2"
      ],
      "certainty": "assumed"
    },
    {
      "id": "DAP-B",
      "type": "guide:dtra-phase-record",
      "name": "DTRA阶段记录：B",
      "attributes": {
        "phase": "B",
        "implication": "开发支撑愿景的目标业务架构；开展详细能力评估及业务驱动与目标分析",
        "considered_factor_ids": [
          "business-rationale",
          "scope-scale",
          "business-model-adaptability",
          "culture",
          "funding-resources"
        ],
        "actions": [
          {
            "id": "ACT-B1",
            "factor_ids": [
              "culture"
            ],
            "action": "文化变革工作坊与试点团队"
          }
        ]
      },
      "evidence": [
        "DAP-R2"
      ],
      "certainty": "assumed"
    },
    {
      "id": "DAP-C",
      "type": "guide:dtra-phase-record",
      "name": "DTRA阶段记录：C",
      "attributes": {
        "phase": "C",
        "implication": "开发目标数据与应用架构；开展能力评估、数据与应用驱动分析、差距分析与沟通计划；因素侧重数据与应用方面的组织能力",
        "considered_factor_ids": [
          "value-realization",
          "policy-regulations",
          "governance-compliance",
          "skills-competence",
          "ecosystem"
        ],
        "actions": [
          {
            "id": "ACT-C1",
            "factor_ids": [
              "ecosystem"
            ],
            "action": "伙伴数据共享评审"
          }
        ]
      },
      "evidence": [
        "DAP-R2"
      ],
      "certainty": "assumed"
    },
    {
      "id": "DAP-D",
      "type": "guide:dtra-phase-record",
      "name": "DTRA阶段记录：D",
      "attributes": {
        "phase": "D",
        "implication": "分析技术架构差距；用技术原则使技术架构与数字采用对齐；因素侧重组织技术能力",
        "considered_factor_ids": [
          "it-capability",
          "technology-maturity",
          "governance-compliance",
          "skills-competence",
          "ecosystem"
        ],
        "actions": [
          {
            "id": "ACT-D1",
            "factor_ids": [
              "it-capability"
            ],
            "action": "平台能力补强"
          },
          {
            "id": "ACT-D2",
            "factor_ids": [
              "ecosystem"
            ],
            "action": "伙伴接口技术评审"
          }
        ]
      },
      "evidence": [
        "DAP-R2"
      ],
      "certainty": "assumed"
    },
    {
      "id": "DAP-E",
      "type": "guide:dtra-phase-record",
      "name": "DTRA阶段记录：E",
      "attributes": {
        "phase": "E",
        "implication": "在各域差距外整体判断组织数字采用现状；给出使关键因素就绪的方法；用关键因素差距推导中间与目标状态",
        "considered_factor_ids": [
          "implementation-approach"
        ],
        "actions": [
          {
            "id": "ACT-E",
            "factor_ids": [],
            "action": "按表6-1含义记录本阶段考虑"
          }
        ]
      },
      "evidence": [
        "DAP-R2"
      ],
      "certainty": "assumed"
    },
    {
      "id": "DAP-F",
      "type": "guide:dtra-phase-record",
      "name": "DTRA阶段记录：F",
      "attributes": {
        "phase": "F",
        "implication": "使实施与迁移规划同数字转型方法和愿景对齐；分解实施与迁移战略和实施计划",
        "considered_factor_ids": [
          "implementation-approach"
        ],
        "actions": [
          {
            "id": "ACT-F",
            "factor_ids": [],
            "action": "按表6-1含义记录本阶段考虑"
          }
        ]
      },
      "evidence": [
        "DAP-R2"
      ],
      "certainty": "assumed"
    },
    {
      "id": "DAP-G",
      "type": "guide:dtra-phase-record",
      "name": "DTRA阶段记录：G",
      "attributes": {
        "phase": "G",
        "implication": "通过合规与评审确保遵循实施计划、符合目标架构；此处治理指实施方法是否恰当，不是“治理与合规”因素",
        "considered_factor_ids": [
          "implementation-approach"
        ],
        "actions": [
          {
            "id": "ACT-G",
            "factor_ids": [],
            "action": "按表6-1含义记录本阶段考虑"
          }
        ]
      },
      "evidence": [
        "DAP-R2"
      ],
      "certainty": "assumed"
    },
    {
      "id": "DAP-H",
      "type": "guide:dtra-phase-record",
      "name": "DTRA阶段记录：H",
      "attributes": {
        "phase": "H",
        "implication": "随成熟度与全景演进维护架构变更周期，管理数字采用带来的架构变更",
        "considered_factor_ids": [],
        "actions": [
          {
            "id": "ACT-H",
            "factor_ids": [],
            "action": "按表6-1含义记录本阶段考虑"
          }
        ]
      },
      "evidence": [
        "DAP-R2"
      ],
      "certainty": "assumed"
    },
    {
      "id": "DAP-Requirements",
      "type": "guide:dtra-phase-record",
      "name": "DTRA阶段记录：Requirements",
      "attributes": {
        "phase": "Requirements",
        "implication": "需求管理贯穿所有阶段；需求变更经需求影响评估处理，并在下一周期的相关阶段实施",
        "considered_factor_ids": [],
        "actions": [
          {
            "id": "ACT-Requirements",
            "factor_ids": [],
            "action": "按表6-1含义记录本阶段考虑"
          }
        ],
        "requirement_changes": [
          {
            "id": "RQ-1",
            "impact_assessment_ref": "RIA-20",
            "target_cycle": "next"
          }
        ]
      },
      "evidence": [
        "DAP-R2"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "dtra-adm-phase-alignment-baseline",
    "artifact_id": "dtra-adm-phase-alignment",
    "profile_id": "dtra-adm-phase-alignment-default",
    "title": "DTRA因素与ADM阶段对齐／虚构星河零售",
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
      "DAP-SUM",
      "DAP-Preliminary",
      "DAP-A",
      "DAP-B",
      "DAP-C",
      "DAP-D",
      "DAP-E",
      "DAP-F",
      "DAP-G",
      "DAP-H",
      "DAP-Requirements"
    ],
    "relationship_ids": [],
    "analysis": "从随包虚构原料提取字段，执行dtra-adm-phase-alignment-review；规则为项目操作约定。",
    "legend": "虚构示例；同一ID在修改前后代表同一对象；嵌套记录按表可见。",
    "attributes": {
      "analysis_ids": [
        "dtra-adm-phase-alignment-analysis"
      ]
    }
  },
  "analyses": [
    {
      "id": "dtra-adm-phase-alignment-analysis",
      "method_id": "dtra-adm-phase-alignment-review",
      "inputs": {
        "source_ids": [
          "DAP-R1",
          "DAP-R2"
        ],
        "assessment_ref": "DTRA-2026Q3",
        "initiated_in_phase": "A",
        "factor_ratings": {
          "vision": 6,
          "sponsorship-direction": 7,
          "it-capability": 5,
          "culture": 4,
          "scope-scale": 6,
          "business-rationale": 7,
          "implementation-approach": 6,
          "business-model-adaptability": 6,
          "skills-competence": 6,
          "technology-maturity": 6,
          "ecosystem": 5,
          "governance-compliance": 6,
          "value-realization": 6,
          "policy-regulations": 7,
          "funding-resources": 6
        },
        "reassessment": "end-of-cycle",
        "progression_note": "文化与IT能力补强先于生态系统扩展；生态评审只做准备性工作",
        "phase_records": [
          {
            "id": "DAP-Preliminary",
            "name": "DTRA阶段记录：Preliminary",
            "phase": "Preliminary",
            "implication": "理解企业能力、所用架构框架与治理框架中驱动数字采用的因素；定义架构原则；确定组织期望的、聚焦数字技术的架构能力",
            "considered_factor_ids": [
              "vision",
              "sponsorship-direction"
            ],
            "actions": [
              {
                "id": "ACT-Preliminary",
                "factor_ids": [],
                "action": "按表6-1含义记录本阶段考虑"
              }
            ],
            "evidence": [
              "DAP-R2"
            ]
          },
          {
            "id": "DAP-A",
            "name": "DTRA阶段记录：A",
            "phase": "A",
            "implication": "捕获目标状态高层愿景；识别利益相关者及业务驱动和关注点并开展就绪度评估；依评估输出选择架构路径",
            "considered_factor_ids": [
              "vision",
              "sponsorship-direction"
            ],
            "actions": [
              {
                "id": "ACT-A",
                "factor_ids": [],
                "action": "按表6-1含义记录本阶段考虑"
              }
            ],
            "evidence": [
              "DAP-R2"
            ]
          },
          {
            "id": "DAP-B",
            "name": "DTRA阶段记录：B",
            "phase": "B",
            "implication": "开发支撑愿景的目标业务架构；开展详细能力评估及业务驱动与目标分析",
            "considered_factor_ids": [
              "business-rationale",
              "scope-scale",
              "business-model-adaptability",
              "culture",
              "funding-resources"
            ],
            "actions": [
              {
                "id": "ACT-B1",
                "factor_ids": [
                  "culture"
                ],
                "action": "文化变革工作坊与试点团队"
              }
            ],
            "evidence": [
              "DAP-R2"
            ]
          },
          {
            "id": "DAP-C",
            "name": "DTRA阶段记录：C",
            "phase": "C",
            "implication": "开发目标数据与应用架构；开展能力评估、数据与应用驱动分析、差距分析与沟通计划；因素侧重数据与应用方面的组织能力",
            "considered_factor_ids": [
              "value-realization",
              "policy-regulations",
              "governance-compliance",
              "skills-competence",
              "ecosystem"
            ],
            "actions": [
              {
                "id": "ACT-C1",
                "factor_ids": [
                  "ecosystem"
                ],
                "action": "伙伴数据共享评审"
              }
            ],
            "evidence": [
              "DAP-R2"
            ]
          },
          {
            "id": "DAP-D",
            "name": "DTRA阶段记录：D",
            "phase": "D",
            "implication": "分析技术架构差距；用技术原则使技术架构与数字采用对齐；因素侧重组织技术能力",
            "considered_factor_ids": [
              "it-capability",
              "technology-maturity",
              "governance-compliance",
              "skills-competence",
              "ecosystem"
            ],
            "actions": [
              {
                "id": "ACT-D1",
                "factor_ids": [
                  "it-capability"
                ],
                "action": "平台能力补强"
              },
              {
                "id": "ACT-D2",
                "factor_ids": [
                  "ecosystem"
                ],
                "action": "伙伴接口技术评审"
              }
            ],
            "evidence": [
              "DAP-R2"
            ]
          },
          {
            "id": "DAP-E",
            "name": "DTRA阶段记录：E",
            "phase": "E",
            "implication": "在各域差距外整体判断组织数字采用现状；给出使关键因素就绪的方法；用关键因素差距推导中间与目标状态",
            "considered_factor_ids": [
              "implementation-approach"
            ],
            "actions": [
              {
                "id": "ACT-E",
                "factor_ids": [],
                "action": "按表6-1含义记录本阶段考虑"
              }
            ],
            "evidence": [
              "DAP-R2"
            ]
          },
          {
            "id": "DAP-F",
            "name": "DTRA阶段记录：F",
            "phase": "F",
            "implication": "使实施与迁移规划同数字转型方法和愿景对齐；分解实施与迁移战略和实施计划",
            "considered_factor_ids": [
              "implementation-approach"
            ],
            "actions": [
              {
                "id": "ACT-F",
                "factor_ids": [],
                "action": "按表6-1含义记录本阶段考虑"
              }
            ],
            "evidence": [
              "DAP-R2"
            ]
          },
          {
            "id": "DAP-G",
            "name": "DTRA阶段记录：G",
            "phase": "G",
            "implication": "通过合规与评审确保遵循实施计划、符合目标架构；此处治理指实施方法是否恰当，不是“治理与合规”因素",
            "considered_factor_ids": [
              "implementation-approach"
            ],
            "actions": [
              {
                "id": "ACT-G",
                "factor_ids": [],
                "action": "按表6-1含义记录本阶段考虑"
              }
            ],
            "evidence": [
              "DAP-R2"
            ]
          },
          {
            "id": "DAP-H",
            "name": "DTRA阶段记录：H",
            "phase": "H",
            "implication": "随成熟度与全景演进维护架构变更周期，管理数字采用带来的架构变更",
            "considered_factor_ids": [],
            "actions": [
              {
                "id": "ACT-H",
                "factor_ids": [],
                "action": "按表6-1含义记录本阶段考虑"
              }
            ],
            "evidence": [
              "DAP-R2"
            ]
          },
          {
            "id": "DAP-Requirements",
            "name": "DTRA阶段记录：Requirements",
            "phase": "Requirements",
            "implication": "需求管理贯穿所有阶段；需求变更经需求影响评估处理，并在下一周期的相关阶段实施",
            "considered_factor_ids": [],
            "actions": [
              {
                "id": "ACT-Requirements",
                "factor_ids": [],
                "action": "按表6-1含义记录本阶段考虑"
              }
            ],
            "requirement_changes": [
              {
                "id": "RQ-1",
                "impact_assessment_ref": "RIA-20",
                "target_cycle": "next"
              }
            ],
            "evidence": [
              "DAP-R2"
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
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile dtra-adm-phase-alignment-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile dtra-adm-phase-alignment-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
