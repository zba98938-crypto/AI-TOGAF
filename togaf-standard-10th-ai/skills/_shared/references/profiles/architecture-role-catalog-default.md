# 架构角色定义目录

`profile_id`: architecture-role-catalog-default；`artifact_id`: architecture-role-catalog；主责：[togaf-organization-roles](../../../togaf-organization-roles/SKILL.md)。

来源：G249 §4、§4.1–4.4。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：1.0。

{
  "id": "architecture-role-catalog-default",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "按工作产品字段组织的记录表；来源无对应原图。",
  "structure_basis": "正文定义的工作产品；记录表是项目操作表示法，不冒充来源原图"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:architecture-role。关系类型：。

```json
{
  "entities": {
    "guide:architecture-role": [
      "tier",
      "scope",
      "primary_responsibility",
      "segment_scope",
      "activities",
      "key_stakeholders",
      "kpis"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 对象、关系、必要属性均可追溯并得到表达
- 参考内容不自动成为项目事实；未知项保持显式
- 首席架构师是企业架构师的特例，不是另一个并列层级
- KPI中的3/5与（xxx）四分位是来源示例，不是企业目标
- 岗位、角色、任务不同；一人可担任多角色
- 角色定义不评价任何人员的能力或绩效

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

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

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile architecture-role-catalog-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile architecture-role-catalog-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
