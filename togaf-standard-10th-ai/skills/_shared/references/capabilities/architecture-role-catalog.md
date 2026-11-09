# 架构角色定义目录

ID：`architecture-role-catalog`。主责：[togaf-organization-roles](../../../togaf-organization-roles/SKILL.md)。

来源：G249 §4、§4.1–4.4。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

架构实践需要哪些职责，各角色如何提供上下文、治理、协作和交接，任务由谁在什么范围内承担？

- 该范围业务负责人
- 架构师
- 评审及治理负责人
- 架构实践需要哪些职责，各角色如何提供上下文、治理、协作和交接，任务由谁在什么范围内承担？
- 来源、范围与适用性


## 输入及缺口处理

必需：

- {'id': 'tier', 'meaning': '角色类别：chief/enterprise/segment/solution/specialist；不是通用人事职级总序', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'scope', 'meaning': '该对象负责或适用的范围', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'primary_responsibility', 'meaning': '首要职责', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'segment_scope', 'meaning': '分段或域范围；企业级角色写不适用及原因', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'activities', 'meaning': '主要活动清单', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'key_stakeholders', 'meaning': '关键利益相关者类别', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'kpis', 'meaning': 'KPI记录：度量、目标、目标来源（project-adopted/source-illustrative）及证据', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'leads', 'meaning': '旧版未分类领导关系；需补类型、范围和证据，保留为草稿缺口', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'relationships', 'meaning': '有类型关系：architecture_guidance/architecture_constraint/specialization/collaborates_with/reports_to/handoff，含target、scope和evidence', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'assignments', 'meaning': '人员、岗位、角色任务分配：person_ref、job_ref、task_refs、authority、valid_from、valid_until和evidence', 'origin': 'source-purpose-plus-project-contract'}

可选：

- 既有模型及历史结论

关键输入缺失时生成带ID的草稿与缺口，不计算无依据数值，不伪造批准或事实；结构错误直接拒绝。

## 元素、属性与关系

对象类型：guide:architecture-role。

```json
{
  "guide:architecture-role": [
    "tier",
    "scope",
    "primary_responsibility",
    "segment_scope",
    "activities",
    "key_stakeholders",
    "kpis"
  ]
}
```

{
  "tier": {
    "meaning": "角色类别：chief/enterprise/segment/solution/specialist；不是通用人事职级总序",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "scope": {
    "meaning": "该对象负责或适用的范围",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "primary_responsibility": {
    "meaning": "首要职责",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "segment_scope": {
    "meaning": "分段或域范围；企业级角色写不适用及原因",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "activities": {
    "meaning": "主要活动清单",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "key_stakeholders": {
    "meaning": "关键利益相关者类别",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "kpis": {
    "meaning": "KPI记录：度量、目标、目标来源（project-adopted/source-illustrative）及证据",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "leads": {
    "meaning": "旧版未分类领导关系；需补类型、范围和证据，保留为草稿缺口",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "relationships": {
    "meaning": "有类型关系：architecture_guidance/architecture_constraint/specialization/collaborates_with/reports_to/handoff，含target、scope和evidence",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "assignments": {
    "meaning": "人员、岗位、角色任务分配：person_ref、job_ref、task_refs、authority、valid_from、valid_until和evidence",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 按G249 §4区分首席、企业、分段、解决方案架构师及专家
2. 为每个角色记录范围、首要职责、活动和关键利益相关者
3. 分别记录专业指导、架构约束、特化、协作、汇报与交接；旧leads产生待分类缺口
4. 记录KPI口径、期间、来源和责任，区分企业采用目标与来源示例
5. 按第3、6章记录角色裁剪；只有显式采用的项目策略才施加严格层级规则
6. 记录有权限和有效期的人员任务分配，再用architecture-role-skill-assessment连接任务、技能证据及发展

## 输出、检查与误读

- 范围及依据
- 逐条结果与理由
- 缺口、下一步与责任
- 版本和来源引用

- 首席架构师是企业架构师的特例，不是另一个并列层级
- KPI中的3/5与（xxx）四分位是来源示例，不是企业目标
- 岗位、角色、任务不同；一人可担任多角色
- 角色定义不评价任何人员的能力或绩效

- 名称、来源表格和成功输出不等于业务结论已核实
- 首席架构师是企业架构师的特例，不是另一个并列层级
- KPI中的3/5与（xxx）四分位是来源示例，不是企业目标
- 岗位、角色、任务不同；一人可担任多角色
- 角色定义不评价任何人员的能力或绩效


## 视图和交付物

- [架构角色定义目录](../profiles/architecture-role-catalog-default.md)
- [架构角色协作与指导关系](../profiles/architecture-role-collaboration.md)
- [架构工作与人员配置证据审查](../profiles/architecture-work-assignment-review.md)

- [organization-model](../deliverables/organization-model.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "角色关系引用不存在的角色",
    "expected": "ROLE-REL",
    "why": "ROLE-REL [REL-BROKEN]: Relationship target must be another declared role"
  },
  "modification_example": {
    "change": "把首席架构师满意度KPI改为企业批准目标4/5并附证据",
    "expected": "分析结果变化：新增缺口KPI-CH-1:adopted_by；关闭缺口KPI-CH-1:target"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/architecture-role-catalog.md)
[完整操作案例](../../references/capability-addenda/architecture-role-catalog.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

```json
{
  "notice": "虚构星河零售教学案例；规则不是TOGAF规定，不代表批准。",
  "sources": [
    {
      "id": "ROLE-R1",
      "kind": "example",
      "description": "虚构星河零售EA章程：首席架构师统筹，下设企业架构师1名、订单分段架构师1名、门店解决方案架构师1名。",
      "locator": "raw-materials.json#ROLE-R1"
    },
    {
      "id": "ROLE-R2",
      "kind": "example",
      "description": "人力资源与EA负责人约定：利益相关者满意度目标暂按来源示例3/5记录，尚未批准；交付准时率目标90%已由架构委员会批准。",
      "locator": "raw-materials.json#ROLE-R2"
    }
  ],
  "entities": [
    {
      "id": "ROLE-CHIEF",
      "type": "guide:architecture-role",
      "name": "首席架构师",
      "attributes": {
        "tier": "chief",
        "scope": "企业整体战略与运营语境",
        "primary_responsibility": "为企业期望的战略变革创造有效响应条件",
        "segment_scope": "不适用（企业级）",
        "activities": [
          "支持业务战略制定",
          "把战略转为运营模式变更",
          "对最大、最复杂、风险最高的变更负责"
        ],
        "key_stakeholders": [
          "董事会",
          "高管",
          "分段架构师"
        ],
        "leads": [
          "ROLE-EA",
          "ROLE-SEG",
          "ROLE-SOL"
        ],
        "kpis": [
          {
            "id": "KPI-CH-1",
            "measure": "利益相关者满意度",
            "target": "3/5（来源示例）",
            "target_origin": "source-illustrative"
          }
        ]
      },
      "evidence": [
        "ROLE-R1"
      ],
      "certainty": "assumed"
    },
    {
      "id": "ROLE-EA",
      "type": "guide:architecture-role",
      "name": "企业架构师",
      "attributes": {
        "tier": "enterprise",
        "scope": "跨多个分段的变革",
        "primary_responsibility": "为解决方案组件的集成、互操作与治理创造条件",
        "segment_scope": "不适用（跨分段）",
        "activities": [
          "创建跨分段路线图",
          "定义塑造全景的原则与政策",
          "参与架构变更治理"
        ],
        "key_stakeholders": [
          "首席架构师",
          "组合经理",
          "分段架构师"
        ],
        "leads": [
          "ROLE-SEG",
          "ROLE-SOL"
        ],
        "kpis": [
          {
            "id": "KPI-EA-1",
            "measure": "解决方案按约定时间、资源与成本交付并签核的比例",
            "target": "90%",
            "target_origin": "project-adopted",
            "evidence": [
              "ROLE-R2"
            ]
          }
        ]
      },
      "evidence": [
        "ROLE-R1"
      ],
      "certainty": "assumed"
    },
    {
      "id": "ROLE-SEG",
      "type": "guide:architecture-role",
      "name": "订单分段架构师",
      "attributes": {
        "tier": "segment",
        "scope": "订单与履约业务分段",
        "primary_responsibility": "塑造并治理订单分段的系统、子系统与组件",
        "segment_scope": "业务域：订单与履约",
        "activities": [
          "制定分段演进路线图",
          "识别分段政策与标准",
          "支持解决方案架构师"
        ],
        "key_stakeholders": [
          "订单业务负责人",
          "产品负责人",
          "解决方案架构师"
        ],
        "leads": [
          "ROLE-SOL"
        ],
        "kpis": [
          {
            "id": "KPI-SEG-1",
            "measure": "分段服务达到计划服务水平的比例",
            "target": "90%",
            "target_origin": "project-adopted",
            "evidence": [
              "ROLE-R2"
            ]
          }
        ]
      },
      "evidence": [
        "ROLE-R1"
      ],
      "certainty": "assumed"
    },
    {
      "id": "ROLE-SOL",
      "type": "guide:architecture-role",
      "name": "门店解决方案架构师",
      "attributes": {
        "tier": "solution",
        "scope": "门店自提解决方案",
        "primary_responsibility": "基于特定需求塑造并治理所需解决方案",
        "segment_scope": "订单分段内的门店自提",
        "activities": [
          "规定服务、流程与技术变更",
          "为过渡架构建立路线图",
          "管理变更请求与规格偏差"
        ],
        "key_stakeholders": [
          "门店运营",
          "交付团队",
          "分段架构师"
        ],
        "leads": [],
        "kpis": [
          {
            "id": "KPI-SOL-1",
            "measure": "解决方案在约定边界内交付并签核",
            "target": "按项目边界",
            "target_origin": "project-adopted",
            "evidence": [
              "ROLE-R2"
            ]
          }
        ]
      },
      "evidence": [
        "ROLE-R1"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "architecture-role-catalog-baseline",
    "artifact_id": "architecture-role-catalog",
    "profile_id": "architecture-role-catalog-default",
    "title": "架构角色定义目录／虚构星河零售",
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
      "ROLE-CHIEF",
      "ROLE-EA",
      "ROLE-SEG",
      "ROLE-SOL"
    ],
    "relationship_ids": [],
    "analysis": "从随包虚构原料提取字段，执行architecture-role-catalog-review；规则为项目操作约定。",
    "legend": "虚构示例；同一ID在修改前后代表同一对象；嵌套记录按表可见。",
    "attributes": {
      "analysis_ids": [
        "architecture-role-catalog-analysis"
      ]
    }
  },
  "analyses": [
    {
      "id": "architecture-role-catalog-analysis",
      "method_id": "architecture-role-catalog-review",
      "inputs": {
        "source_ids": [
          "ROLE-R1",
          "ROLE-R2"
        ],
        "roles": [
          {
            "id": "ROLE-CHIEF",
            "name": "首席架构师",
            "tier": "chief",
            "scope": "企业整体战略与运营语境",
            "primary_responsibility": "为企业期望的战略变革创造有效响应条件",
            "segment_scope": "不适用（企业级）",
            "activities": [
              "支持业务战略制定",
              "把战略转为运营模式变更",
              "对最大、最复杂、风险最高的变更负责"
            ],
            "key_stakeholders": [
              "董事会",
              "高管",
              "分段架构师"
            ],
            "leads": [
              "ROLE-EA",
              "ROLE-SEG",
              "ROLE-SOL"
            ],
            "kpis": [
              {
                "id": "KPI-CH-1",
                "measure": "利益相关者满意度",
                "target": "3/5（来源示例）",
                "target_origin": "source-illustrative"
              }
            ],
            "evidence": [
              "ROLE-R1"
            ]
          },
          {
            "id": "ROLE-EA",
            "name": "企业架构师",
            "tier": "enterprise",
            "scope": "跨多个分段的变革",
            "primary_responsibility": "为解决方案组件的集成、互操作与治理创造条件",
            "segment_scope": "不适用（跨分段）",
            "activities": [
              "创建跨分段路线图",
              "定义塑造全景的原则与政策",
              "参与架构变更治理"
            ],
            "key_stakeholders": [
              "首席架构师",
              "组合经理",
              "分段架构师"
            ],
            "leads": [
              "ROLE-SEG",
              "ROLE-SOL"
            ],
            "kpis": [
              {
                "id": "KPI-EA-1",
                "measure": "解决方案按约定时间、资源与成本交付并签核的比例",
                "target": "90%",
                "target_origin": "project-adopted",
                "evidence": [
                  "ROLE-R2"
                ]
              }
            ],
            "evidence": [
              "ROLE-R1"
            ]
          },
          {
            "id": "ROLE-SEG",
            "name": "订单分段架构师",
            "tier": "segment",
            "scope": "订单与履约业务分段",
            "primary_responsibility": "塑造并治理订单分段的系统、子系统与组件",
            "segment_scope": "业务域：订单与履约",
            "activities": [
              "制定分段演进路线图",
              "识别分段政策与标准",
              "支持解决方案架构师"
            ],
            "key_stakeholders": [
              "订单业务负责人",
              "产品负责人",
              "解决方案架构师"
            ],
            "leads": [
              "ROLE-SOL"
            ],
            "kpis": [
              {
                "id": "KPI-SEG-1",
                "measure": "分段服务达到计划服务水平的比例",
                "target": "90%",
                "target_origin": "project-adopted",
                "evidence": [
                  "ROLE-R2"
                ]
              }
            ],
            "evidence": [
              "ROLE-R1"
            ]
          },
          {
            "id": "ROLE-SOL",
            "name": "门店解决方案架构师",
            "tier": "solution",
            "scope": "门店自提解决方案",
            "primary_responsibility": "基于特定需求塑造并治理所需解决方案",
            "segment_scope": "订单分段内的门店自提",
            "activities": [
              "规定服务、流程与技术变更",
              "为过渡架构建立路线图",
              "管理变更请求与规格偏差"
            ],
            "key_stakeholders": [
              "门店运营",
              "交付团队",
              "分段架构师"
            ],
            "leads": [],
            "kpis": [
              {
                "id": "KPI-SOL-1",
                "measure": "解决方案在约定边界内交付并签核",
                "target": "按项目边界",
                "target_origin": "project-adopted",
                "evidence": [
                  "ROLE-R2"
                ]
              }
            ],
            "evidence": [
              "ROLE-R1"
            ]
          }
        ]
      }
    }
  ]
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact architecture-role-catalog --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
