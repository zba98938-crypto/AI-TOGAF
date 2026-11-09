# SMART目的评估

`profile_id`: smart-objective-assessment-default；`artifact_id`: smart-objective-assessment；主责：[togaf-strategy-capabilities](../../../togaf-strategy-capabilities/SKILL.md)。

来源：G176 §9.1–9.3。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：1.0。

{
  "id": "smart-objective-assessment-default",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "按工作产品字段组织的记录表；来源无对应原图。",
  "structure_basis": "正文定义的工作产品；记录表是项目操作表示法，不冒充来源原图"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:goal, guide:smart-objective。关系类型：。

```json
{
  "entities": {
    "guide:goal": [
      "statement",
      "category",
      "business_goal_ref"
    ],
    "guide:smart-objective": [
      "goal_id",
      "statement",
      "scope",
      "measure",
      "unit",
      "target"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 对象、关系、必要属性均可追溯并得到表达
- 参考内容不自动成为项目事实；未知项保持显式
- 13类目标是示例类别，不是封闭清单
- SMART只检查结构，现实性与数值合理性由责任人判断
- 目的须追溯到组织业务目标

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构星河零售教学案例；规则不是TOGAF规定，不代表批准。",
  "sources": [
    {
      "id": "SMART-R1",
      "kind": "example",
      "description": "虚构目标G-UP（类别：提高用户生产率）：门店前台界面一致；业务目标引用BG-3。",
      "locator": "raw-materials.json#SMART-R1"
    },
    {
      "id": "SMART-R2",
      "kind": "example",
      "description": "目的O-1：2027-06-30前三类前台设备界面一致，订单录入错误由5%降到4%，负责人UX组；可用性测试支持可行性。",
      "locator": "raw-materials.json#SMART-R2"
    }
  ],
  "entities": [
    {
      "id": "G-UP",
      "type": "guide:goal",
      "name": "提高门店前台用户生产率",
      "attributes": {
        "statement": "门店前台用户生产率提高",
        "category": "user-productivity",
        "business_goal_ref": "BG-3"
      },
      "evidence": [
        "SMART-R1"
      ],
      "certainty": "assumed"
    },
    {
      "id": "O-1",
      "type": "guide:smart-objective",
      "name": "一致的前台界面",
      "attributes": {
        "goal_id": "G-UP",
        "statement": "三类前台设备提供一致的订单录入界面",
        "scope": "门店前台三类设备",
        "measure": "订单录入错误率",
        "unit": "%",
        "baseline": 5,
        "target": 4,
        "owner": "UX组",
        "action": "统一组件库并迁移三类设备",
        "realism_rationale": "可用性测试显示组件复用可行",
        "realism_evidence": [
          "SMART-R2"
        ],
        "due": "2027-06-30"
      },
      "evidence": [
        "SMART-R2"
      ],
      "certainty": "assumed"
    },
    {
      "id": "O-2",
      "type": "guide:smart-objective",
      "name": "缩短前台培训时间",
      "attributes": {
        "goal_id": "G-UP",
        "statement": "缩短新员工前台培训时间",
        "scope": "新入职门店员工",
        "measure": "培训时长",
        "unit": "小时",
        "baseline": "",
        "target": 6,
        "owner": "培训组",
        "action": "",
        "realism_rationale": "",
        "realism_evidence": [],
        "due": ""
      },
      "evidence": [
        "SMART-R1"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "smart-objective-assessment-baseline",
    "artifact_id": "smart-objective-assessment",
    "profile_id": "smart-objective-assessment-default",
    "title": "SMART目的评估／虚构星河零售",
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
      "G-UP",
      "O-1",
      "O-2"
    ],
    "relationship_ids": [],
    "analysis": "从随包虚构原料提取字段，执行smart-objective-review；规则为项目操作约定。",
    "legend": "虚构示例；同一ID在修改前后代表同一对象；嵌套记录按表可见。",
    "attributes": {
      "analysis_ids": [
        "smart-objective-assessment-analysis"
      ]
    }
  },
  "analyses": [
    {
      "id": "smart-objective-assessment-analysis",
      "method_id": "smart-objective-review",
      "inputs": {
        "source_ids": [
          "SMART-R1",
          "SMART-R2"
        ],
        "goals": [
          {
            "id": "G-UP",
            "name": "提高门店前台用户生产率",
            "statement": "门店前台用户生产率提高",
            "category": "user-productivity",
            "business_goal_ref": "BG-3",
            "evidence": [
              "SMART-R1"
            ]
          }
        ],
        "objectives": [
          {
            "id": "O-1",
            "name": "一致的前台界面",
            "goal_id": "G-UP",
            "statement": "三类前台设备提供一致的订单录入界面",
            "scope": "门店前台三类设备",
            "measure": "订单录入错误率",
            "unit": "%",
            "baseline": 5,
            "target": 4,
            "owner": "UX组",
            "action": "统一组件库并迁移三类设备",
            "realism_rationale": "可用性测试显示组件复用可行",
            "realism_evidence": [
              "SMART-R2"
            ],
            "due": "2027-06-30",
            "evidence": [
              "SMART-R2"
            ]
          },
          {
            "id": "O-2",
            "name": "缩短前台培训时间",
            "goal_id": "G-UP",
            "statement": "缩短新员工前台培训时间",
            "scope": "新入职门店员工",
            "measure": "培训时长",
            "unit": "小时",
            "baseline": "",
            "target": 6,
            "owner": "培训组",
            "action": "",
            "realism_rationale": "",
            "realism_evidence": [],
            "due": "",
            "evidence": [
              "SMART-R1"
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
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile smart-objective-assessment-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile smart-objective-assessment-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
