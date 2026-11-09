# 业务场景关联矩阵

ID：`scenario-traceability-matrix`。主责：[togaf-vision-scenarios](../../../togaf-vision-scenarios/SKILL.md)。

来源：G176 §3.2.3; English PDF22–23；G176 §11.4; English PDF45–46。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

流程与各关键场景要素是否一致？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 流程与各关键场景要素是否一致？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- {'id': 'raw_records', 'origin': 'source', 'meaning': '只读原始业务材料与定位'}
- {'id': 'normalized_records', 'origin': 'source', 'meaning': '拆分复合陈述、统一术语和分类后的原子记录'}
- {'id': 'transformation_log', 'origin': 'source', 'meaning': '每一步输入、输出、操作、理由、证据'}
- {'id': 'processes', 'origin': 'source', 'meaning': '作为关联焦点的流程'}
- {'id': 'constituencies', 'origin': 'source', 'meaning': '受影响利益相关方群体'}
- {'id': 'human_actors', 'origin': 'source', 'meaning': '人的参与者'}
- {'id': 'computer_actors', 'origin': 'source', 'meaning': '计算机参与者'}
- {'id': 'problems', 'origin': 'source', 'meaning': '待改善问题/痛点'}
- {'id': 'objectives', 'origin': 'source', 'meaning': '期望达成的结果'}

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

未知关系用缺口ID，不把空格当确定无关联。缺任一类别可生成范围受限草稿；未关联结果的痛点必须列为阻断检查项。

## 元素、属性与关系

对象类型：actor, application, goal, problem, process, repository_asset, stakeholder。

```json
{}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "process": {
    "meaning": "业务流程或行为引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "stakeholder": {
    "meaning": "利益相关者引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "human_actor": {
    "meaning": "人的参与者引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "computer_actor": {
    "meaning": "计算机参与者引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "problem": {
    "meaning": "待解决问题及其业务证据",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "goal": {
    "meaning": "业务目标引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 锁定原始资料
2. 按单点拆分复合陈述
3. 统一术语并分类，记录每次转换
4. 以流程链接五类要素，逐个关联给证据
5. 验证每个痛点至少有一个成果
6. 从已支持关系形成业务/技术需求
7. 评审是否回应原始问题，批准后才进入需求存储库

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 矩阵关联不等于流程控制顺序或 CRUD
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯
- 每个规范条目可追溯只读原始记录与转换步骤
- 复合陈述不得丢失子句
- 每个痛点至少一个成果
- 矩阵关系没有未经原文授权的CRUD/顺序/责任编码
- 同ID复用、重名不同ID不合并
- 单一制品请求仍可输出本矩阵和最小必要追溯，不强制全套成果

- 6项总体任务、5个迭代步骤与3个阶段是不同分解
- 矩阵有一条关联不代表实际控制流
- 把全部流程和全部参与者自动连满会制造事实


## 视图和交付物

- [流程与五类场景要素关联](../profiles/scenario-traceability-matrix-default.md)
- [问题与预期结果关联](../profiles/scenario-painpoint-outcome-matrix.md)
- [原始材料、规范化、转换与派生要求](../profiles/scenario-transformation-audit.md)

- [architecture-vision](../deliverables/architecture-vision.md)
- [statement-of-work](../deliverables/statement-of-work.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「业务场景关联矩阵」给出：6项总体任务、5个迭代步骤与3个阶段是不同分解",
    "expected": "missing-evidence",
    "why": "6项总体任务、5个迭代步骤与3个阶段是不同分解"
  },
  "modification_example": {
    "change": "在「业务场景关联矩阵」的范围内新增或修改一项，检查下游是否随之变化",
    "expected": "受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/scenario-traceability-matrix.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

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

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact scenario-traceability-matrix --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
