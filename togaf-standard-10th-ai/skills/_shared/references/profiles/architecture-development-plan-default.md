# 架构人员发展计划

`profile_id`: architecture-development-plan-default；`artifact_id`: architecture-development-plan。

来源：G249 §5–6（发展计划字段与判据为项目约定）。字段与运行时检查为项目约定。

表示族：`roadmap`。按工作产品属性组织；来源无直接对应图时为项目补充模板。。

## 必需模型内容

```json
{
  "skill_development": [
    "person",
    "role",
    "skill_id",
    "scale_id",
    "task_refs",
    "requirement_refs",
    "current_proficiency",
    "target_proficiency",
    "behavioral_gap",
    "action",
    "success_criteria",
    "reassessment",
    "history",
    "evidence"
  ]
}
```

## 检查

- 每项发展行动绑定技能、任务要求和量表，目标与当前证据分开
- 完成培训不自动提升评级；复评完成须引用实测评价和行为证据
- 历史证据不覆盖；目标不随观察值变化；未证明高级不自动降为低级

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
      "id": "architecture-development-plan-default-practice",
      "type": "skill_development",
      "name": "共同主持并形成决策记录",
      "attributes": {
        "person": "PERSON-A",
        "role": "G249:role:enterprise-architect",
        "skill_id": "G249:skill:business:business-scenario",
        "scale_id": "G249-table5-1",
        "task_refs": [
          "TASK-SCENARIO"
        ],
        "requirement_refs": [
          "REQ-SCENARIO"
        ],
        "current_proficiency": 2,
        "target_proficiency": 3,
        "behavioral_gap": "缺少能据详细业务证据作决策并解释困难情况专家介入的观察",
        "evidence": [
          "example-source"
        ],
        "history": [
          {
            "observed_on": "2026-11-05",
            "proficiency": 2,
            "evidence": [
              "example-source"
            ],
            "status": "assessed",
            "rationale": "在专家主持下实际完成场景冲突分析；不是由未达到3级反推"
          }
        ],
        "action": "与导师共同处理两个业务场景冲突，形成证据与决策理由",
        "success_criteria": [
          "记录冲突、依据、备选及专家支持点"
        ],
        "order": 1,
        "start": "2026-11-09",
        "end": "2026-11-13",
        "reassessment": {
          "assessor": "REVIEWER-A",
          "due_on": "2026-11-13",
          "criteria": [
            "检查共同实践产出"
          ],
          "status": "planned"
        }
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-development-plan-default-reassess",
      "type": "skill_development",
      "name": "完成任务并按行为证据复评",
      "attributes": {
        "person": "PERSON-A",
        "role": "G249:role:enterprise-architect",
        "skill_id": "G249:skill:business:business-scenario",
        "scale_id": "G249-table5-1",
        "task_refs": [
          "TASK-SCENARIO"
        ],
        "requirement_refs": [
          "REQ-SCENARIO"
        ],
        "current_proficiency": 2,
        "target_proficiency": 3,
        "behavioral_gap": "缺少能据详细业务证据作决策并解释困难情况专家介入的观察",
        "evidence": [
          "example-source"
        ],
        "history": [
          {
            "observed_on": "2026-11-05",
            "proficiency": 2,
            "evidence": [
              "example-source"
            ],
            "status": "assessed",
            "rationale": "在专家主持下实际完成场景冲突分析；不是由未达到3级反推"
          }
        ],
        "action": "主导后续场景分析；评审实际决策理由、异议处理及必要的专家介入",
        "success_criteria": [
          "足够细节支持有效决策",
          "困难情形及时寻求专家，保留依据"
        ],
        "order": 2,
        "start": "2026-11-16",
        "end": "2026-11-20",
        "reassessment": {
          "assessor": "REVIEWER-B",
          "due_on": "2026-11-20",
          "criteria": [
            "按任务行为证据核对G249三级含义"
          ],
          "status": "planned"
        }
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "architecture-development-plan-default-dependency",
      "type": "traces_to",
      "source": "architecture-development-plan-default-reassess",
      "target": "architecture-development-plan-default-practice",
      "label": "复评使用共同实践记录；培训出席不代替行为证据",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-architecture-development-plan-default",
    "artifact_id": "architecture-development-plan",
    "profile_id": "architecture-development-plan-default",
    "title": "架构人员发展计划／虚构案例",
    "entity_ids": [
      "architecture-development-plan-default-practice",
      "architecture-development-plan-default-reassess"
    ],
    "relationship_ids": [
      "architecture-development-plan-default-dependency"
    ],
    "analysis": "目标与人员证据逐项比较；未知不赋低分；目标不由个人现状倒推。",
    "legend": "原文参考≠项目目标≠人员观察；四级技能熟练度≠组织成熟度≠Open CA三级认证。"
  }
}
```
