# 流程与五类场景要素关联

`profile_id`: scenario-traceability-matrix-default；`artifact_id`: scenario-traceability-matrix；主责：[togaf-vision-scenarios](../../../togaf-vision-scenarios/SKILL.md)。

来源：G176 §3.2.3; English PDF22–23；G176 §11.4; English PDF45–46。

## 构图与定义状态

表示族：`matrix`；输出：`diagram`。规范版本：2.1。

{
  "row_types": [
    "process"
  ],
  "column_types": [
    "stakeholder",
    "actor",
    "application",
    "problem",
    "goal"
  ],
  "source_verified": false,
  "layout_notes": "依据正文语义的项目操作表单；没有对应原图，不标记为原图复刻。",
  "review_status": "source-semantics-reviewed-project-form"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：process, stakeholder, actor, application, problem, goal。关系类型：traces_to。

```json
{
  "entities": {},
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 每个规范条目可追溯只读原始记录与转换步骤
- 复合陈述不得丢失子句
- 每个痛点至少一个成果
- 矩阵关系没有未经原文授权的CRUD/顺序/责任编码
- 同ID复用、重名不同ID不合并
- 单一制品请求仍可输出本矩阵和最小必要追溯，不强制全套成果

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构图书馆完整案例；数据与阈值不是TOGAF规定。",
  "sources": [
    {
      "id": "S-R1",
      "kind": "example",
      "description": "读者群体说：电话和网页重复报名让同一人占两个名额，希望每个读者每场课程只有一个有效预约。预约员在受理预约流程中使用课程预约系统处理两条渠道。",
      "locator": "case.json#raw_records/S-R1"
    },
    {
      "id": "S-R2",
      "kind": "example",
      "description": "读者群体说：取消后退款经常漏记，希望次一工作日内登记退款。预约员在取消退款流程里与退款队列系统交互；财务组关注这个流程的退款记录。",
      "locator": "case.json#raw_records/S-R2"
    },
    {
      "id": "S-R3",
      "kind": "example",
      "description": "修订：取消退款改由统一支付台处理，原退款队列退役。受理预约仍使用课程预约系统。",
      "locator": "case.json#raw_records/S-R3"
    }
  ],
  "entities": [
    {
      "id": "st-patrons",
      "type": "stakeholder",
      "name": "读者群体关注预约与退款结果",
      "attributes": {
        "definition": "读者群体关注预约与退款结果"
      },
      "evidence": [
        "S-R1"
      ],
      "certainty": "assumed",
      "version": "1.0"
    },
    {
      "id": "p-duplicate",
      "type": "problem",
      "name": "电话和网页重复报名占用两个名额",
      "attributes": {
        "definition": "电话和网页重复报名占用两个名额"
      },
      "evidence": [
        "S-R1"
      ],
      "certainty": "assumed",
      "version": "1.0"
    },
    {
      "id": "g-unique",
      "type": "goal",
      "name": "同一读者同场课程只保留一个有效预约",
      "attributes": {
        "definition": "同一读者同场课程只保留一个有效预约"
      },
      "evidence": [
        "S-R1"
      ],
      "certainty": "assumed",
      "version": "1.0"
    },
    {
      "id": "proc-book",
      "type": "process",
      "name": "受理预约",
      "attributes": {
        "definition": "受理预约"
      },
      "evidence": [
        "S-R1"
      ],
      "certainty": "assumed",
      "version": "1.0"
    },
    {
      "id": "actor-booking",
      "type": "actor",
      "name": "预约员",
      "attributes": {
        "definition": "预约员"
      },
      "evidence": [
        "S-R1"
      ],
      "certainty": "assumed",
      "version": "1.0"
    },
    {
      "id": "app-booking",
      "type": "application",
      "name": "课程预约系统",
      "attributes": {
        "definition": "课程预约系统"
      },
      "evidence": [
        "S-R1"
      ],
      "certainty": "assumed",
      "version": "1.0"
    },
    {
      "id": "p-refund",
      "type": "problem",
      "name": "取消后退款漏记",
      "attributes": {
        "definition": "取消后退款漏记"
      },
      "evidence": [
        "S-R2"
      ],
      "certainty": "assumed",
      "version": "1.0"
    },
    {
      "id": "g-refund",
      "type": "goal",
      "name": "次一工作日内登记退款",
      "attributes": {
        "definition": "次一工作日内登记退款"
      },
      "evidence": [
        "S-R2"
      ],
      "certainty": "assumed",
      "version": "1.0"
    },
    {
      "id": "proc-refund",
      "type": "process",
      "name": "取消退款",
      "attributes": {
        "definition": "取消退款"
      },
      "evidence": [
        "S-R2"
      ],
      "certainty": "assumed",
      "version": "1.0"
    },
    {
      "id": "app-refund-old",
      "type": "application",
      "name": "退款队列系统",
      "attributes": {
        "definition": "退款队列系统"
      },
      "evidence": [
        "S-R2"
      ],
      "certainty": "assumed",
      "version": "1.0"
    },
    {
      "id": "st-finance",
      "type": "stakeholder",
      "name": "财务组关注退款记录",
      "attributes": {
        "definition": "财务组关注退款记录"
      },
      "evidence": [
        "S-R2"
      ],
      "certainty": "assumed",
      "version": "1.0"
    }
  ],
  "relationships": [
    {
      "id": "s-book-patron",
      "type": "traces_to",
      "source": "proc-book",
      "target": "st-patrons",
      "label": "场景关联：stakeholder；不表示CRUD/顺序/责任",
      "evidence": [
        "S-R1"
      ],
      "certainty": "assumed",
      "extension_data": {
        "togaf-addenda:g176-scenario": {
          "association_kind": "stakeholder"
        }
      }
    },
    {
      "id": "s-book-human",
      "type": "traces_to",
      "source": "proc-book",
      "target": "actor-booking",
      "label": "场景关联：human_actor；不表示CRUD/顺序/责任",
      "evidence": [
        "S-R1"
      ],
      "certainty": "assumed",
      "extension_data": {
        "togaf-addenda:g176-scenario": {
          "association_kind": "human_actor"
        }
      }
    },
    {
      "id": "s-book-computer",
      "type": "traces_to",
      "source": "proc-book",
      "target": "app-booking",
      "label": "场景关联：computer_actor；不表示CRUD/顺序/责任",
      "evidence": [
        "S-R1"
      ],
      "certainty": "assumed",
      "extension_data": {
        "togaf-addenda:g176-scenario": {
          "association_kind": "computer_actor"
        }
      }
    },
    {
      "id": "s-book-problem",
      "type": "traces_to",
      "source": "proc-book",
      "target": "p-duplicate",
      "label": "场景关联：problem；不表示CRUD/顺序/责任",
      "evidence": [
        "S-R1"
      ],
      "certainty": "assumed",
      "extension_data": {
        "togaf-addenda:g176-scenario": {
          "association_kind": "problem"
        }
      }
    },
    {
      "id": "s-book-goal",
      "type": "traces_to",
      "source": "proc-book",
      "target": "g-unique",
      "label": "场景关联：objective；不表示CRUD/顺序/责任",
      "evidence": [
        "S-R1"
      ],
      "certainty": "assumed",
      "extension_data": {
        "togaf-addenda:g176-scenario": {
          "association_kind": "objective"
        }
      }
    },
    {
      "id": "s-refund-patron",
      "type": "traces_to",
      "source": "proc-refund",
      "target": "st-patrons",
      "label": "场景关联：stakeholder；不表示CRUD/顺序/责任",
      "evidence": [
        "S-R2"
      ],
      "certainty": "assumed",
      "extension_data": {
        "togaf-addenda:g176-scenario": {
          "association_kind": "stakeholder"
        }
      }
    },
    {
      "id": "s-refund-finance",
      "type": "traces_to",
      "source": "proc-refund",
      "target": "st-finance",
      "label": "场景关联：stakeholder；不表示CRUD/顺序/责任",
      "evidence": [
        "S-R2"
      ],
      "certainty": "assumed",
      "extension_data": {
        "togaf-addenda:g176-scenario": {
          "association_kind": "stakeholder"
        }
      }
    },
    {
      "id": "s-refund-human",
      "type": "traces_to",
      "source": "proc-refund",
      "target": "actor-booking",
      "label": "场景关联：human_actor；不表示CRUD/顺序/责任",
      "evidence": [
        "S-R2"
      ],
      "certainty": "assumed",
      "extension_data": {
        "togaf-addenda:g176-scenario": {
          "association_kind": "human_actor"
        }
      }
    },
    {
      "id": "s-refund-computer",
      "type": "traces_to",
      "source": "proc-refund",
      "target": "app-refund-old",
      "label": "场景关联：computer_actor；不表示CRUD/顺序/责任",
      "evidence": [
        "S-R2"
      ],
      "certainty": "assumed",
      "extension_data": {
        "togaf-addenda:g176-scenario": {
          "association_kind": "computer_actor"
        }
      }
    },
    {
      "id": "s-refund-problem",
      "type": "traces_to",
      "source": "proc-refund",
      "target": "p-refund",
      "label": "场景关联：problem；不表示CRUD/顺序/责任",
      "evidence": [
        "S-R2"
      ],
      "certainty": "assumed",
      "extension_data": {
        "togaf-addenda:g176-scenario": {
          "association_kind": "problem"
        }
      }
    },
    {
      "id": "s-refund-goal",
      "type": "traces_to",
      "source": "proc-refund",
      "target": "g-refund",
      "label": "场景关联：objective；不表示CRUD/顺序/责任",
      "evidence": [
        "S-R2"
      ],
      "certainty": "assumed",
      "extension_data": {
        "togaf-addenda:g176-scenario": {
          "association_kind": "objective"
        }
      }
    }
  ],
  "analyses": [
    {
      "id": "analysis-scenario-traceability-matrix",
      "method_id": "scenario-traceability-review",
      "inputs": {
        "processes": [
          "proc-book",
          "proc-refund"
        ],
        "categories": {
          "stakeholder": [
            "st-patrons",
            "st-finance"
          ],
          "human_actor": [
            "actor-booking"
          ],
          "computer_actor": [
            "app-booking",
            "app-refund-old"
          ],
          "problem": [
            "p-duplicate",
            "p-refund"
          ],
          "objective": [
            "g-unique",
            "g-refund"
          ]
        },
        "associations": [
          {
            "id": "s-book-patron",
            "process": "proc-book",
            "target": "st-patrons",
            "kind": "stakeholder",
            "evidence": [
              "S-R1"
            ]
          },
          {
            "id": "s-book-human",
            "process": "proc-book",
            "target": "actor-booking",
            "kind": "human_actor",
            "evidence": [
              "S-R1"
            ]
          },
          {
            "id": "s-book-computer",
            "process": "proc-book",
            "target": "app-booking",
            "kind": "computer_actor",
            "evidence": [
              "S-R1"
            ]
          },
          {
            "id": "s-book-problem",
            "process": "proc-book",
            "target": "p-duplicate",
            "kind": "problem",
            "evidence": [
              "S-R1"
            ]
          },
          {
            "id": "s-book-goal",
            "process": "proc-book",
            "target": "g-unique",
            "kind": "objective",
            "evidence": [
              "S-R1"
            ]
          },
          {
            "id": "s-refund-patron",
            "process": "proc-refund",
            "target": "st-patrons",
            "kind": "stakeholder",
            "evidence": [
              "S-R2"
            ]
          },
          {
            "id": "s-refund-finance",
            "process": "proc-refund",
            "target": "st-finance",
            "kind": "stakeholder",
            "evidence": [
              "S-R2"
            ]
          },
          {
            "id": "s-refund-human",
            "process": "proc-refund",
            "target": "actor-booking",
            "kind": "human_actor",
            "evidence": [
              "S-R2"
            ]
          },
          {
            "id": "s-refund-computer",
            "process": "proc-refund",
            "target": "app-refund-old",
            "kind": "computer_actor",
            "evidence": [
              "S-R2"
            ]
          },
          {
            "id": "s-refund-problem",
            "process": "proc-refund",
            "target": "p-refund",
            "kind": "problem",
            "evidence": [
              "S-R2"
            ]
          },
          {
            "id": "s-refund-goal",
            "process": "proc-refund",
            "target": "g-refund",
            "kind": "objective",
            "evidence": [
              "S-R2"
            ]
          }
        ],
        "painpoint_outcomes": [
          {
            "id": "pout-unique",
            "problem": "p-duplicate",
            "outcome": "g-unique",
            "evidence": [
              "S-R1"
            ]
          },
          {
            "id": "pout-refund",
            "problem": "p-refund",
            "outcome": "g-refund",
            "evidence": [
              "S-R2"
            ]
          }
        ],
        "derived_requirements": [
          {
            "id": "req-unique",
            "kind": "business",
            "statement": "同一读者和课程的有效预约唯一",
            "evidence": [
              "S-R1"
            ],
            "from_goal": "g-unique"
          },
          {
            "id": "req-refund",
            "kind": "business",
            "statement": "取消后次一工作日内登记退款",
            "evidence": [
              "S-R2"
            ],
            "from_goal": "g-refund"
          },
          {
            "id": "req-tech-proposed",
            "kind": "technical-candidate",
            "statement": "向退款系统传送取消记录并回传登记结果",
            "evidence": [
              "S-R2"
            ],
            "from_goal": "g-refund",
            "status": "assumption-requires-owner-review"
          }
        ],
        "unknowns": [
          {
            "id": "gap-zero-association",
            "description": "没有关联证据的矩阵格保持未确认；不推断确定无关联"
          }
        ],
        "normalized_records": [
          {
            "id": "S-N1",
            "from": "S-R1",
            "type": "stakeholder",
            "entity_id": "st-patrons",
            "text": "读者群体关注预约与退款结果"
          },
          {
            "id": "S-N2",
            "from": "S-R1",
            "type": "problem",
            "entity_id": "p-duplicate",
            "text": "电话和网页重复报名占用两个名额"
          },
          {
            "id": "S-N3",
            "from": "S-R1",
            "type": "goal",
            "entity_id": "g-unique",
            "text": "同一读者同场课程只保留一个有效预约"
          },
          {
            "id": "S-N4",
            "from": "S-R1",
            "type": "process",
            "entity_id": "proc-book",
            "text": "受理预约"
          },
          {
            "id": "S-N5",
            "from": "S-R1",
            "type": "actor",
            "entity_id": "actor-booking",
            "text": "预约员"
          },
          {
            "id": "S-N6",
            "from": "S-R1",
            "type": "application",
            "entity_id": "app-booking",
            "text": "课程预约系统"
          },
          {
            "id": "S-N7",
            "from": "S-R2",
            "type": "problem",
            "entity_id": "p-refund",
            "text": "取消后退款漏记"
          },
          {
            "id": "S-N8",
            "from": "S-R2",
            "type": "goal",
            "entity_id": "g-refund",
            "text": "次一工作日内登记退款"
          },
          {
            "id": "S-N9",
            "from": "S-R2",
            "type": "process",
            "entity_id": "proc-refund",
            "text": "取消退款"
          },
          {
            "id": "S-N10",
            "from": "S-R2",
            "type": "actor",
            "entity_id": "actor-booking",
            "text": "复用预约员，不生成第二个对象"
          },
          {
            "id": "S-N11",
            "from": "S-R2",
            "type": "application",
            "entity_id": "app-refund-old",
            "text": "退款队列系统"
          },
          {
            "id": "S-N12",
            "from": "S-R2",
            "type": "stakeholder",
            "entity_id": "st-finance",
            "text": "财务组关注退款记录"
          },
          {
            "id": "S-N13",
            "from": "S-R2",
            "type": "stakeholder",
            "entity_id": "st-patrons",
            "text": "复用读者群体"
          }
        ],
        "transformation_log": [
          {
            "id": "S-T1",
            "operation": "split-compound",
            "input": [
              "S-R1"
            ],
            "output": [
              "S-N1",
              "S-N2",
              "S-N3",
              "S-N4",
              "S-N5",
              "S-N6"
            ],
            "reason": "拆为利益群体、问题、目标、流程、人及计算机参与者，保留所有子句"
          },
          {
            "id": "S-T2",
            "operation": "split-and-normalize",
            "input": [
              "S-R2"
            ],
            "output": [
              "S-N7",
              "S-N8",
              "S-N9",
              "S-N10",
              "S-N11",
              "S-N12",
              "S-N13"
            ],
            "reason": "拆分第二流程；已知同一预约员/读者群体复用ID，财务组独立"
          },
          {
            "id": "S-T3",
            "operation": "classify",
            "input": [
              "S-N1",
              "S-N2",
              "S-N3",
              "S-N4",
              "S-N5",
              "S-N6",
              "S-N7",
              "S-N8",
              "S-N9",
              "S-N10",
              "S-N11",
              "S-N12",
              "S-N13"
            ],
            "output": [
              "scenario-baseline"
            ],
            "reason": "五类列与流程行；关联不是CRUD/控制流"
          }
        ],
        "raw_record_ids": [
          "S-R1",
          "S-R2",
          "S-R3"
        ],
        "source_ids": [
          "S-R1",
          "S-R2",
          "S-R3"
        ],
        "work_product_ids": [
          "scenario-baseline"
        ]
      },
      "evidence": [
        "S-R1",
        "S-R2",
        "S-R3"
      ]
    }
  ],
  "view": {
    "id": "library-scenario",
    "artifact_id": "scenario-traceability-matrix",
    "profile_id": "scenario-traceability-matrix-default",
    "title": "流程与五类场景要素关联",
    "entity_ids": [
      "proc-book",
      "proc-refund",
      "st-patrons",
      "st-finance",
      "actor-booking",
      "app-booking",
      "app-refund-old",
      "p-duplicate",
      "p-refund",
      "g-unique",
      "g-refund"
    ],
    "relationship_ids": [
      "s-book-patron",
      "s-book-human",
      "s-book-computer",
      "s-book-problem",
      "s-book-goal",
      "s-refund-patron",
      "s-refund-finance",
      "s-refund-human",
      "s-refund-computer",
      "s-refund-problem",
      "s-refund-goal"
    ],
    "analysis": "原始陈述、分析规则和修改记录均保留稳定引用；计算只采用显式项目规则。",
    "legend": "虚构图书馆案例。空白矩阵格为未确认；相邻/包含不代表额外关系；规则和数值不是TOGAF默认值。",
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
      "evolution": "baseline"
    },
    "attributes": {
      "analysis_ids": [
        "analysis-scenario-traceability-matrix"
      ]
    }
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile scenario-traceability-matrix-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile scenario-traceability-matrix-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
