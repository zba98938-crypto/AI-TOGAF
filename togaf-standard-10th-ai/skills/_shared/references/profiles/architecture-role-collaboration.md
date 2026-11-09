# 架构角色协作与指导关系

`profile_id`: architecture-role-collaboration；`artifact_id`: architecture-role-catalog。

来源：G249 §4 Figure 4-1（角色协作语义；图示不等于本地人事汇报）。字段与运行时检查为项目约定。

表示族：`network`。角色关系按明示类型表达；专业指导、人事汇报、特化、协作与交接分开。

## 必需模型内容

```json
{
  "guide:architecture-role": [
    "tier",
    "scope",
    "primary_responsibility"
  ]
}
```

## 检查

- Chief是Enterprise角色特化，不从布局推导人事汇报
- 每条关系需范围与证据；handoff需交付物与验收条件

## 完整示例片段

示例不代表真实人员评价、业务批准或原图复刻。

```json
{
  "notice": "虚构案例；原文参考、项目目标与个人观察独立记录，生成不等于评审通过。",
  "sources": [
    {
      "id": "g249-table-source",
      "kind": "official",
      "description": "G249 §5 Tables 5-1/5-2：参考等级与量表；不证明任何人员已具备能力",
      "locator": "https://pubs.opengroup.org/togaf-standard/architecture-roles-and-skills/Architecture-Roles-and-Skills.html#chap05"
    },
    {
      "id": "example-source",
      "kind": "example",
      "description": "虚构项目要求、辅导应用记录与复评计划；非实际人员评价"
    }
  ],
  "scales": [
    {
      "id": "G249-table5-1",
      "name": "G249 Table 5-1 人的技能熟练度",
      "anchors": [
        {
          "value": 1,
          "meaning": "Background: Some understanding but reliant on specialists."
        },
        {
          "value": 2,
          "meaning": "Aware: Understands and can address issues with the support of specialists."
        },
        {
          "value": 3,
          "meaning": "Knowledgeable: Good detail enabling effective decision-making, requiring specialist input in difficult situations."
        },
        {
          "value": 4,
          "meaning": "Expert: Extensive experience, practical, and applied knowledge."
        }
      ],
      "evidence": [
        "g249-table-source"
      ]
    }
  ],
  "entities": [
    {
      "id": "architecture-role-collaboration-chief",
      "type": "guide:architecture-role",
      "name": "首席架构角色",
      "attributes": {
        "tier": "chief",
        "scope": "本次订单履约架构工作",
        "primary_responsibility": "架构实践方向和跨域协调"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-role-collaboration-enterprise",
      "type": "guide:architecture-role",
      "name": "企业架构角色",
      "attributes": {
        "tier": "enterprise",
        "scope": "本次订单履约架构工作",
        "primary_responsibility": "企业目标与架构约束对齐"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-role-collaboration-segment",
      "type": "guide:architecture-role",
      "name": "分段架构角色",
      "attributes": {
        "tier": "segment",
        "scope": "本次订单履约架构工作",
        "primary_responsibility": "领域模型与演进安排"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-role-collaboration-solution",
      "type": "guide:architecture-role",
      "name": "解决方案架构角色",
      "attributes": {
        "tier": "solution",
        "scope": "本次订单履约架构工作",
        "primary_responsibility": "在约束下设计交付方案"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "architecture-role-collaboration-relation0",
      "type": "g249:specialization",
      "source": "architecture-role-collaboration-chief",
      "target": "architecture-role-collaboration-enterprise",
      "label": "首席是企业架构角色的特化",
      "attributes": {
        "semantic_type": "specialization",
        "scope": "订单履约架构任务"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-role-collaboration-relation1",
      "type": "g249:architecture_guidance",
      "source": "architecture-role-collaboration-enterprise",
      "target": "architecture-role-collaboration-segment",
      "label": "专业指导，不表示雇佣汇报",
      "attributes": {
        "semantic_type": "architecture_guidance",
        "scope": "订单履约架构任务"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-role-collaboration-relation2",
      "type": "g249:architecture_constraint",
      "source": "architecture-role-collaboration-segment",
      "target": "architecture-role-collaboration-solution",
      "label": "架构约束及适用边界",
      "attributes": {
        "semantic_type": "architecture_constraint",
        "scope": "订单履约架构任务"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-role-collaboration-relation3",
      "type": "g249:collaborates_with",
      "source": "architecture-role-collaboration-solution",
      "target": "architecture-role-collaboration-segment",
      "label": "方案与域架构协作",
      "attributes": {
        "semantic_type": "collaborates_with",
        "scope": "订单履约架构任务"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-role-collaboration-relation4",
      "type": "g249:handoff",
      "source": "architecture-role-collaboration-segment",
      "target": "architecture-role-collaboration-solution",
      "label": "交接经说明的接口约束和未决事项",
      "attributes": {
        "semantic_type": "handoff",
        "scope": "订单履约架构任务",
        "deliverable_ref": "DEL-INTERFACE",
        "acceptance_criteria": [
          "接口范围、约束、未决项及接收方均可追溯"
        ]
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-architecture-role-collaboration",
    "artifact_id": "architecture-role-catalog",
    "profile_id": "architecture-role-collaboration",
    "title": "架构角色协作与指导关系／虚构案例",
    "entity_ids": [
      "architecture-role-collaboration-chief",
      "architecture-role-collaboration-enterprise",
      "architecture-role-collaboration-segment",
      "architecture-role-collaboration-solution"
    ],
    "relationship_ids": [
      "architecture-role-collaboration-relation0",
      "architecture-role-collaboration-relation1",
      "architecture-role-collaboration-relation2",
      "architecture-role-collaboration-relation3",
      "architecture-role-collaboration-relation4"
    ],
    "analysis": "目标与人员证据逐项比较；未知不赋低分；目标不由个人现状倒推。",
    "legend": "指导/约束/协作/特化/交接分别按边类型读取；未画reports_to表示未声明，不能由纵向布局推断。"
  },
  "extensions": {
    "relationship_types": {
      "g249:specialization": {
        "source_types": [
          "guide:architecture-role"
        ],
        "target_types": [
          "guide:architecture-role"
        ],
        "meaning": "首席是企业架构角色的特化"
      },
      "g249:architecture_guidance": {
        "source_types": [
          "guide:architecture-role"
        ],
        "target_types": [
          "guide:architecture-role"
        ],
        "meaning": "专业指导，不表示雇佣汇报"
      },
      "g249:architecture_constraint": {
        "source_types": [
          "guide:architecture-role"
        ],
        "target_types": [
          "guide:architecture-role"
        ],
        "meaning": "架构约束及适用边界"
      },
      "g249:collaborates_with": {
        "source_types": [
          "guide:architecture-role"
        ],
        "target_types": [
          "guide:architecture-role"
        ],
        "meaning": "方案与域架构协作"
      },
      "g249:handoff": {
        "source_types": [
          "guide:architecture-role"
        ],
        "target_types": [
          "guide:architecture-role"
        ],
        "meaning": "交接经说明的接口约束和未决事项"
      },
      "g249:reports_to": {
        "source_types": [
          "guide:architecture-role"
        ],
        "target_types": [
          "guide:architecture-role"
        ],
        "meaning": "仅在有明确组织授权证据时记录人事汇报"
      }
    }
  }
}
```
