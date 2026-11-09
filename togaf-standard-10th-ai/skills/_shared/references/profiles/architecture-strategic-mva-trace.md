# 战略—MVA—产品待办追溯

`profile_id`: architecture-strategic-mva-trace；`artifact_id`: architecture-backlog；主责：[togaf-requirements](../../../togaf-requirements/SKILL.md)。

来源：G20F §4.5 L304–327；G20F §5.2.3 L529–547；G20F §5.3.2 L601–632。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.2。

{
  "id": "architecture-strategic-mva-trace",
  "version": "2.2",
  "source_verified": false,
  "layout_notes": "正文方法的关系表；不声称复刻G20F图4-4或5-4"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：goal, requirement, abb, sbb, guide:mva_scope。关系类型：g20f:refines, g20f:constrains-story, g20f:allocated-to-sbb, g20f:included-in-mva, g20f:story-depends-on, realizes。

```json
{
  "entities": {
    "goal": [
      "kind",
      "owner",
      "statement"
    ],
    "requirement": [
      "kind",
      "owner",
      "statement"
    ],
    "abb": [
      "kind",
      "owner",
      "responsibility",
      "interface",
      "quality"
    ],
    "sbb": [
      "kind",
      "owner",
      "responsibility",
      "product",
      "version"
    ],
    "guide:mva_scope": [
      "kind",
      "owner",
      "boundary",
      "exclusions",
      "candidate_story_ids",
      "decision_owner",
      "decision_evidence",
      "history"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 每个故事追溯到战略意图
- MVA选择与明确的must-have一致
- SBB到ABB方向和故事分配一致
- 未验收和未验证的范围外依赖必须显式报告

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "sources": [
    {
      "id": "BR-1",
      "kind": "example",
      "description": "虚构图书馆战略：让读者自助办理预约与取消，减少人工重复录入。本项目采用战略意图—epic—feature—story层次；只是本项目追溯规则。"
    },
    {
      "id": "BR-2",
      "kind": "example",
      "description": "产品负责人把预约受理列为首次开放的必须项，退款登记暂为应有项。首个MVA仅覆盖预约受理，排除退款自动结算和历史借阅迁移；后续功能仍保留在产品待办。"
    },
    {
      "id": "BR-3",
      "kind": "example",
      "description": "预约受理故事要求每位读者每场次最多一项有效预约。退款登记故事要求取消后下一营业日生成退款队列记录；依赖预约标识。两故事均由读者服务负责人确认，尚无运行验收结果。"
    },
    {
      "id": "BR-4",
      "kind": "example",
      "description": "架构负责人规定预约幂等ABB及退款可追溯ABB；实施候选分别为预约API与退款队列适配器SBB。SBB到ABB是设计实现关系，尚未部署。"
    },
    {
      "id": "BR-5",
      "kind": "example",
      "description": "修改：预约与取消必须在同一开放窗口提供。产品负责人把退款登记提升为must-have，扩展同一MVA范围，仍排除自动结算及历史迁移；保留原MVA范围历史。"
    },
    {
      "id": "BR-6",
      "kind": "example",
      "description": "修改后的测试记录：预约幂等契约测试通过；退款队列与外部财务接口尚未演练。测试通过仅证明预约验收条件，不证明整套MVA可运营。"
    }
  ],
  "entities": [
    {
      "id": "G-SELF",
      "type": "goal",
      "name": "读者自助服务",
      "attributes": {
        "kind": "strategic_intent",
        "owner": "读者服务负责人",
        "statement": "让读者自助办理预约与取消，减少人工重复录入"
      },
      "evidence": [
        "BR-1"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started",
      "context": {
        "domains": [
          "business",
          "application"
        ],
        "landscape": "strategic",
        "purpose": "project",
        "abstraction": "conceptual",
        "evolution": "target"
      }
    },
    {
      "id": "E-RESERVE",
      "type": "requirement",
      "name": "自助预约与取消产品",
      "attributes": {
        "kind": "epic",
        "owner": "读者服务负责人",
        "statement": "读者可自助完成预约及取消申请"
      },
      "evidence": [
        "BR-1"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started",
      "context": {
        "domains": [
          "business",
          "application"
        ],
        "landscape": "segment",
        "purpose": "project",
        "abstraction": "logical",
        "evolution": "target"
      }
    },
    {
      "id": "F-BOOK",
      "type": "requirement",
      "name": "预约受理功能",
      "attributes": {
        "kind": "feature",
        "owner": "读者服务负责人",
        "statement": "受理并核验预约唯一性"
      },
      "evidence": [
        "BR-3"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started",
      "context": {
        "domains": [
          "business",
          "application"
        ],
        "landscape": "segment",
        "purpose": "project",
        "abstraction": "logical",
        "evolution": "target"
      }
    },
    {
      "id": "F-REFUND",
      "type": "requirement",
      "name": "取消退款登记功能",
      "attributes": {
        "kind": "feature",
        "owner": "读者服务负责人",
        "statement": "保留取消依据并登记退款队列"
      },
      "evidence": [
        "BR-3"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started",
      "context": {
        "domains": [
          "business",
          "application"
        ],
        "landscape": "segment",
        "purpose": "project",
        "abstraction": "logical",
        "evolution": "target"
      }
    },
    {
      "id": "S-BOOK",
      "type": "requirement",
      "name": "预约唯一性故事",
      "attributes": {
        "kind": "story",
        "owner": "读者服务负责人",
        "statement": "作为读者，我希望不会因重复提交产生重复预约",
        "priority": "must-have",
        "priority_evidence": [
          "BR-2"
        ],
        "acceptance_criteria": "每位读者每场次最多一项有效预约",
        "acceptance": {
          "status": "not-observed",
          "evidence": []
        }
      },
      "evidence": [
        "BR-2",
        "BR-3"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started",
      "context": {
        "domains": [
          "business",
          "application"
        ],
        "landscape": "capability",
        "purpose": "project",
        "abstraction": "logical",
        "evolution": "target"
      }
    },
    {
      "id": "S-REFUND",
      "type": "requirement",
      "name": "取消后退款登记故事",
      "attributes": {
        "kind": "story",
        "owner": "读者服务负责人",
        "statement": "作为读者，我希望取消后可查询退款登记",
        "priority": "should-have",
        "priority_evidence": [
          "BR-2"
        ],
        "acceptance_criteria": "取消后下一营业日生成带预约标识的退款队列记录",
        "acceptance": {
          "status": "not-observed",
          "evidence": []
        }
      },
      "evidence": [
        "BR-2",
        "BR-3"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started",
      "context": {
        "domains": [
          "business",
          "application"
        ],
        "landscape": "capability",
        "purpose": "project",
        "abstraction": "logical",
        "evolution": "target"
      }
    },
    {
      "id": "ABB-IDEMPOTENT",
      "type": "abb",
      "name": "预约幂等规定",
      "attributes": {
        "kind": "abb",
        "owner": "架构负责人",
        "responsibility": "保证预约标识与幂等处理",
        "interface": "提交/查询预约",
        "quality": "并发重复提交不重复受理"
      },
      "evidence": [
        "BR-4"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started",
      "context": {
        "domains": [
          "business",
          "application"
        ],
        "landscape": "capability",
        "purpose": "project",
        "abstraction": "logical",
        "evolution": "target"
      }
    },
    {
      "id": "ABB-REFUND",
      "type": "abb",
      "name": "退款可追溯规定",
      "attributes": {
        "kind": "abb",
        "owner": "架构负责人",
        "responsibility": "关联取消、退款登记及原预约",
        "interface": "登记/查询退款",
        "quality": "取消记录可追溯"
      },
      "evidence": [
        "BR-4"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started",
      "context": {
        "domains": [
          "business",
          "application"
        ],
        "landscape": "capability",
        "purpose": "project",
        "abstraction": "logical",
        "evolution": "target"
      }
    },
    {
      "id": "SBB-API",
      "type": "sbb",
      "name": "预约API候选实现",
      "attributes": {
        "kind": "sbb",
        "owner": "架构负责人",
        "responsibility": "实现预约幂等契约",
        "product": "项目自研预约API",
        "version": "candidate-v1"
      },
      "evidence": [
        "BR-4"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started",
      "context": {
        "domains": [
          "business",
          "application"
        ],
        "landscape": "capability",
        "purpose": "project",
        "abstraction": "physical",
        "evolution": "target"
      }
    },
    {
      "id": "SBB-QUEUE",
      "type": "sbb",
      "name": "退款队列适配器候选实现",
      "attributes": {
        "kind": "sbb",
        "owner": "架构负责人",
        "responsibility": "实现取消后队列登记",
        "product": "项目队列适配器",
        "version": "candidate-v1"
      },
      "evidence": [
        "BR-4"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started",
      "context": {
        "domains": [
          "business",
          "application"
        ],
        "landscape": "capability",
        "purpose": "project",
        "abstraction": "physical",
        "evolution": "target"
      }
    },
    {
      "id": "MVA-OPEN",
      "type": "guide:mva_scope",
      "name": "首次开放MVA",
      "attributes": {
        "kind": "mva",
        "owner": "读者服务负责人",
        "boundary": "预约受理及幂等护栏",
        "exclusions": [
          "退款自动结算",
          "历史借阅迁移",
          "本期退款队列登记"
        ],
        "candidate_story_ids": [
          "S-BOOK",
          "S-REFUND"
        ],
        "decision_owner": "产品负责人",
        "decision_evidence": [
          "BR-2"
        ],
        "history": [
          {
            "version": "v1",
            "boundary": "仅预约受理",
            "selected_story_ids": [
              "S-BOOK"
            ],
            "evidence": [
              "BR-2"
            ]
          }
        ]
      },
      "evidence": [
        "BR-2"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started",
      "context": {
        "domains": [
          "business",
          "application"
        ],
        "landscape": "capability",
        "purpose": "project",
        "abstraction": "logical",
        "evolution": "target"
      }
    }
  ],
  "relationships": [
    {
      "id": "R-GE",
      "type": "g20f:refines",
      "source": "G-SELF",
      "target": "E-RESERVE",
      "evidence": [
        "BR-1"
      ],
      "label": "细化",
      "certainty": "assumed"
    },
    {
      "id": "R-EFB",
      "type": "g20f:refines",
      "source": "E-RESERVE",
      "target": "F-BOOK",
      "evidence": [
        "BR-1",
        "BR-3"
      ],
      "label": "细化",
      "certainty": "assumed"
    },
    {
      "id": "R-EFR",
      "type": "g20f:refines",
      "source": "E-RESERVE",
      "target": "F-REFUND",
      "evidence": [
        "BR-1",
        "BR-3"
      ],
      "label": "细化",
      "certainty": "assumed"
    },
    {
      "id": "R-FSB",
      "type": "g20f:refines",
      "source": "F-BOOK",
      "target": "S-BOOK",
      "evidence": [
        "BR-3"
      ],
      "label": "细化",
      "certainty": "assumed"
    },
    {
      "id": "R-FSR",
      "type": "g20f:refines",
      "source": "F-REFUND",
      "target": "S-REFUND",
      "evidence": [
        "BR-3"
      ],
      "label": "细化",
      "certainty": "assumed"
    },
    {
      "id": "R-CB",
      "type": "g20f:constrains-story",
      "source": "ABB-IDEMPOTENT",
      "target": "S-BOOK",
      "evidence": [
        "BR-4"
      ],
      "label": "护栏约束",
      "certainty": "assumed"
    },
    {
      "id": "R-CR",
      "type": "g20f:constrains-story",
      "source": "ABB-REFUND",
      "target": "S-REFUND",
      "evidence": [
        "BR-4"
      ],
      "label": "护栏约束",
      "certainty": "assumed"
    },
    {
      "id": "R-AB",
      "type": "g20f:allocated-to-sbb",
      "source": "S-BOOK",
      "target": "SBB-API",
      "evidence": [
        "BR-4"
      ],
      "label": "计划分配",
      "certainty": "assumed"
    },
    {
      "id": "R-AR",
      "type": "g20f:allocated-to-sbb",
      "source": "S-REFUND",
      "target": "SBB-QUEUE",
      "evidence": [
        "BR-4"
      ],
      "label": "计划分配",
      "certainty": "assumed"
    },
    {
      "id": "R-IB",
      "type": "realizes",
      "source": "SBB-API",
      "target": "ABB-IDEMPOTENT",
      "evidence": [
        "BR-4"
      ],
      "label": "候选设计实现",
      "certainty": "assumed"
    },
    {
      "id": "R-IR",
      "type": "realizes",
      "source": "SBB-QUEUE",
      "target": "ABB-REFUND",
      "evidence": [
        "BR-4"
      ],
      "label": "候选设计实现",
      "certainty": "assumed"
    },
    {
      "id": "R-MB",
      "type": "g20f:included-in-mva",
      "source": "S-BOOK",
      "target": "MVA-OPEN",
      "evidence": [
        "BR-2"
      ],
      "label": "纳入MVA",
      "certainty": "assumed"
    },
    {
      "id": "R-DEP",
      "type": "g20f:story-depends-on",
      "source": "S-REFUND",
      "target": "S-BOOK",
      "evidence": [
        "BR-3"
      ],
      "label": "依赖前置",
      "certainty": "assumed"
    }
  ],
  "extensions": {
    "relationship_types": {
      "g20f:refines": {
        "source_types": [
          "goal",
          "requirement"
        ],
        "target_types": [
          "requirement"
        ],
        "meaning": "本项目声明的战略意图到epic/feature/story逐层细化，不是流程先后"
      },
      "g20f:constrains-story": {
        "source_types": [
          "abb"
        ],
        "target_types": [
          "requirement"
        ],
        "meaning": "ABB对故事给出功能/非功能护栏"
      },
      "g20f:allocated-to-sbb": {
        "source_types": [
          "requirement"
        ],
        "target_types": [
          "sbb"
        ],
        "meaning": "故事分配到候选SBB实现，不表示已实现"
      },
      "g20f:included-in-mva": {
        "source_types": [
          "requirement"
        ],
        "target_types": [
          "guide:mva_scope"
        ],
        "meaning": "显式必须项纳入命名MVA边界，非已验收或完整MVP"
      },
      "g20f:story-depends-on": {
        "source_types": [
          "requirement"
        ],
        "target_types": [
          "requirement"
        ],
        "meaning": "依赖方故事指向前置故事，非优先级或完成顺序断言"
      }
    }
  },
  "analyses": [
    {
      "id": "A-TRACE",
      "method_id": "architecture-backlog-trace-review",
      "inputs": {
        "source_ids": [
          "BR-1",
          "BR-2",
          "BR-3",
          "BR-4",
          "BR-5",
          "BR-6"
        ],
        "hierarchy_policy": {
          "levels": [
            "strategic_intent",
            "epic",
            "feature",
            "story"
          ],
          "evidence": [
            "BR-1"
          ]
        },
        "nodes": [
          {
            "id": "G-SELF",
            "kind": "strategic_intent",
            "name": "读者自助服务",
            "owner": "读者服务负责人",
            "evidence": [
              "BR-1"
            ],
            "landscape": "strategic",
            "evolution": "target",
            "statement": "让读者自助办理预约与取消，减少人工重复录入"
          },
          {
            "id": "E-RESERVE",
            "kind": "epic",
            "name": "自助预约与取消产品",
            "owner": "读者服务负责人",
            "evidence": [
              "BR-1"
            ],
            "landscape": "segment",
            "evolution": "target",
            "statement": "读者可自助完成预约及取消申请"
          },
          {
            "id": "F-BOOK",
            "kind": "feature",
            "name": "预约受理功能",
            "owner": "读者服务负责人",
            "evidence": [
              "BR-3"
            ],
            "landscape": "segment",
            "evolution": "target",
            "statement": "受理并核验预约唯一性"
          },
          {
            "id": "F-REFUND",
            "kind": "feature",
            "name": "取消退款登记功能",
            "owner": "读者服务负责人",
            "evidence": [
              "BR-3"
            ],
            "landscape": "segment",
            "evolution": "target",
            "statement": "保留取消依据并登记退款队列"
          },
          {
            "id": "S-BOOK",
            "kind": "story",
            "name": "预约唯一性故事",
            "owner": "读者服务负责人",
            "evidence": [
              "BR-2",
              "BR-3"
            ],
            "landscape": "capability",
            "evolution": "target",
            "statement": "作为读者，我希望不会因重复提交产生重复预约",
            "priority": "must-have",
            "priority_evidence": [
              "BR-2"
            ],
            "acceptance_criteria": "每位读者每场次最多一项有效预约",
            "acceptance": {
              "status": "not-observed",
              "evidence": []
            }
          },
          {
            "id": "S-REFUND",
            "kind": "story",
            "name": "取消后退款登记故事",
            "owner": "读者服务负责人",
            "evidence": [
              "BR-2",
              "BR-3"
            ],
            "landscape": "capability",
            "evolution": "target",
            "statement": "作为读者，我希望取消后可查询退款登记",
            "priority": "should-have",
            "priority_evidence": [
              "BR-2"
            ],
            "acceptance_criteria": "取消后下一营业日生成带预约标识的退款队列记录",
            "acceptance": {
              "status": "not-observed",
              "evidence": []
            }
          },
          {
            "id": "ABB-IDEMPOTENT",
            "kind": "abb",
            "name": "预约幂等规定",
            "owner": "架构负责人",
            "evidence": [
              "BR-4"
            ],
            "responsibility": "保证预约标识与幂等处理",
            "interface": "提交/查询预约",
            "quality": "并发重复提交不重复受理"
          },
          {
            "id": "ABB-REFUND",
            "kind": "abb",
            "name": "退款可追溯规定",
            "owner": "架构负责人",
            "evidence": [
              "BR-4"
            ],
            "responsibility": "关联取消、退款登记及原预约",
            "interface": "登记/查询退款",
            "quality": "取消记录可追溯"
          },
          {
            "id": "SBB-API",
            "kind": "sbb",
            "name": "预约API候选实现",
            "owner": "架构负责人",
            "evidence": [
              "BR-4"
            ],
            "responsibility": "实现预约幂等契约",
            "product": "项目自研预约API",
            "version": "candidate-v1"
          },
          {
            "id": "SBB-QUEUE",
            "kind": "sbb",
            "name": "退款队列适配器候选实现",
            "owner": "架构负责人",
            "evidence": [
              "BR-4"
            ],
            "responsibility": "实现取消后队列登记",
            "product": "项目队列适配器",
            "version": "candidate-v1"
          },
          {
            "id": "MVA-OPEN",
            "kind": "mva",
            "name": "首次开放MVA",
            "owner": "读者服务负责人",
            "evidence": [
              "BR-2"
            ],
            "boundary": "预约受理及幂等护栏",
            "exclusions": [
              "退款自动结算",
              "历史借阅迁移",
              "本期退款队列登记"
            ],
            "candidate_story_ids": [
              "S-BOOK",
              "S-REFUND"
            ],
            "decision_owner": "产品负责人",
            "decision_evidence": [
              "BR-2"
            ],
            "history": [
              {
                "version": "v1",
                "boundary": "仅预约受理",
                "selected_story_ids": [
                  "S-BOOK"
                ],
                "evidence": [
                  "BR-2"
                ]
              }
            ]
          }
        ],
        "relationships": [
          {
            "id": "R-GE",
            "type": "g20f:refines",
            "source": "G-SELF",
            "target": "E-RESERVE",
            "evidence": [
              "BR-1"
            ]
          },
          {
            "id": "R-EFB",
            "type": "g20f:refines",
            "source": "E-RESERVE",
            "target": "F-BOOK",
            "evidence": [
              "BR-1",
              "BR-3"
            ]
          },
          {
            "id": "R-EFR",
            "type": "g20f:refines",
            "source": "E-RESERVE",
            "target": "F-REFUND",
            "evidence": [
              "BR-1",
              "BR-3"
            ]
          },
          {
            "id": "R-FSB",
            "type": "g20f:refines",
            "source": "F-BOOK",
            "target": "S-BOOK",
            "evidence": [
              "BR-3"
            ]
          },
          {
            "id": "R-FSR",
            "type": "g20f:refines",
            "source": "F-REFUND",
            "target": "S-REFUND",
            "evidence": [
              "BR-3"
            ]
          },
          {
            "id": "R-CB",
            "type": "g20f:constrains-story",
            "source": "ABB-IDEMPOTENT",
            "target": "S-BOOK",
            "evidence": [
              "BR-4"
            ]
          },
          {
            "id": "R-CR",
            "type": "g20f:constrains-story",
            "source": "ABB-REFUND",
            "target": "S-REFUND",
            "evidence": [
              "BR-4"
            ]
          },
          {
            "id": "R-AB",
            "type": "g20f:allocated-to-sbb",
            "source": "S-BOOK",
            "target": "SBB-API",
            "evidence": [
              "BR-4"
            ]
          },
          {
            "id": "R-AR",
            "type": "g20f:allocated-to-sbb",
            "source": "S-REFUND",
            "target": "SBB-QUEUE",
            "evidence": [
              "BR-4"
            ]
          },
          {
            "id": "R-IB",
            "type": "realizes",
            "source": "SBB-API",
            "target": "ABB-IDEMPOTENT",
            "evidence": [
              "BR-4"
            ]
          },
          {
            "id": "R-IR",
            "type": "realizes",
            "source": "SBB-QUEUE",
            "target": "ABB-REFUND",
            "evidence": [
              "BR-4"
            ]
          },
          {
            "id": "R-MB",
            "type": "g20f:included-in-mva",
            "source": "S-BOOK",
            "target": "MVA-OPEN",
            "evidence": [
              "BR-2"
            ]
          },
          {
            "id": "R-DEP",
            "type": "g20f:story-depends-on",
            "source": "S-REFUND",
            "target": "S-BOOK",
            "evidence": [
              "BR-3"
            ]
          }
        ]
      },
      "evidence": [
        "BR-1",
        "BR-2",
        "BR-3",
        "BR-4",
        "BR-5",
        "BR-6"
      ]
    }
  ],
  "view": {
    "id": "v-architecture-strategic-mva-trace",
    "artifact_id": "architecture-backlog",
    "profile_id": "architecture-strategic-mva-trace",
    "title": "战略意图—MVA—产品待办—ABB/SBB追溯",
    "context": {
      "domains": [
        "business",
        "application"
      ],
      "landscape": "capability",
      "purpose": "project",
      "abstraction": "logical",
      "evolution": "target"
    },
    "entity_ids": [
      "G-SELF",
      "E-RESERVE",
      "F-BOOK",
      "F-REFUND",
      "S-BOOK",
      "S-REFUND",
      "ABB-IDEMPOTENT",
      "ABB-REFUND",
      "SBB-API",
      "SBB-QUEUE",
      "MVA-OPEN"
    ],
    "relationship_ids": [
      "R-GE",
      "R-EFB",
      "R-EFR",
      "R-FSB",
      "R-FSR",
      "R-CB",
      "R-CR",
      "R-AB",
      "R-AR",
      "R-IB",
      "R-IR",
      "R-MB",
      "R-DEP"
    ],
    "analysis": "从原始材料逐层形成稳定对象、MVA范围和设计实现链接。优先级来自产品负责人；候选SBB关系不证明已部署。",
    "legend": "战略/分段/能力是全景层级，全部目标状态另记；关系方向和项目层次显式定义；入选不等于验收。",
    "attributes": {
      "analysis_ids": [
        "A-TRACE"
      ]
    }
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile architecture-strategic-mva-trace --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile architecture-strategic-mva-trace --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
