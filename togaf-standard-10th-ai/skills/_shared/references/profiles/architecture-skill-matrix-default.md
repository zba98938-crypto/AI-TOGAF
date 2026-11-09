# 架构技能／角色矩阵

`profile_id`: architecture-skill-matrix-default；`artifact_id`: architecture-skill-matrix。

来源：G249 §5 Tables 5-1 and 5-2。字段与运行时检查为项目约定。

表示族：`matrix`。同一技能角色单元可保留多个有语义和证据的评级记录。

## 必需模型内容

```json
{
  "skill": [
    "skill_id",
    "category",
    "subskill"
  ],
  "architecture_role": [
    "definition"
  ],
  "guide:architecture-role": [
    "tier",
    "scope",
    "primary_responsibility"
  ]
}
```

关系 `supports_role` 的属性须分别声明 `assessment_kind`、`assessment_state`、`scale_id`、`proficiency`；原文目标另需 `reference_role_id`、`source_locator`；项目目标另需 `task_refs`、`tailoring_reason`、`behavioral_criteria`；已评价个人另需 `person_ref`、`task_refs`、`assessor`、`observed_on`、`behavioral_evidence`。证据引用保留在关系 `evidence`。

原文目标状态为 `reference`；项目目标为 `proposed/adopted`；个人观察为 `unassessed/evidence_insufficient/assessed/superseded`。未评估及证据不足使用null；缺新字段的旧草稿产生gap，非法值及语义矛盾报error。G249四级锚点不能作为agent权限或Open CA三级认证。

## 检查

- 原文参考目标绑定原始技能与六个角色列；Chief和通用Segment不得伪造列
- 评级必须绑定量表和语义；未评价保留null，非法等级报错
- 项目目标保留任务和裁剪理由；个人观察保留正向行为证据与时点

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
      "id": "architecture-skill-matrix-default-skill",
      "type": "skill",
      "name": "业务场景分析",
      "attributes": {
        "skill_id": "G249:skill:business:business-scenario",
        "category": "Business",
        "subskill": "Business Scenario"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-skill-matrix-default-role",
      "type": "architecture_role",
      "name": "企业架构角色",
      "attributes": {
        "definition": "本项目将业务场景结果用于跨域架构决策",
        "reference_role_id": "G249:role:enterprise-architect"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "architecture-skill-matrix-default-source",
      "type": "supports_role",
      "source": "architecture-skill-matrix-default-skill",
      "target": "architecture-skill-matrix-default-role",
      "label": "原文参考目标",
      "attributes": {
        "proficiency": 3,
        "assessment_kind": "source_reference_target",
        "assessment_state": "reference",
        "scale_id": "G249-table5-1",
        "reference_role_id": "G249:role:enterprise-architect",
        "source_locator": "G249 Table 5-2 Business Scenario / Enterprise Architect"
      },
      "evidence": [
        "g249-table-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-skill-matrix-default-target",
      "type": "supports_role",
      "source": "architecture-skill-matrix-default-skill",
      "target": "architecture-skill-matrix-default-role",
      "label": "项目目标",
      "attributes": {
        "proficiency": 3,
        "assessment_kind": "tailored_target",
        "assessment_state": "proposed",
        "scale_id": "G249-table5-1",
        "tailoring_reason": "本次需形成可用于决策的业务场景；采用原文参考等级，限本任务范围",
        "task_refs": [
          "TASK-SCENARIO"
        ],
        "behavioral_criteria": [
          "能依据业务证据形成场景、识别冲突并说明决策依据；困难情形寻求专家"
        ]
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-skill-matrix-default-observed",
      "type": "supports_role",
      "source": "architecture-skill-matrix-default-skill",
      "target": "architecture-skill-matrix-default-role",
      "label": "人员观察",
      "attributes": {
        "proficiency": 2,
        "assessment_kind": "observed_assessment",
        "assessment_state": "assessed",
        "scale_id": "G249-table5-1",
        "person_ref": "PERSON-A",
        "task_refs": [
          "TASK-SCENARIO"
        ],
        "assessor": "REVIEWER-A",
        "observed_on": "2026-11-05",
        "behavioral_evidence": [
          {
            "criterion": "在专家支持下处理场景中的冲突",
            "demonstrated": true,
            "evidence": [
              "example-source"
            ]
          }
        ]
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-architecture-skill-matrix-default",
    "artifact_id": "architecture-skill-matrix",
    "profile_id": "architecture-skill-matrix-default",
    "title": "架构技能／角色矩阵／虚构案例",
    "entity_ids": [
      "architecture-skill-matrix-default-skill",
      "architecture-skill-matrix-default-role"
    ],
    "relationship_ids": [
      "architecture-skill-matrix-default-source",
      "architecture-skill-matrix-default-target",
      "architecture-skill-matrix-default-observed"
    ],
    "analysis": "目标与人员证据逐项比较；未知不赋低分；目标不由个人现状倒推。",
    "legend": "原文参考≠项目目标≠人员观察；四级技能熟练度≠组织成熟度≠Open CA三级认证。"
  }
}
```
