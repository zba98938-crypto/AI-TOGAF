# SMART目的评估

ID：`smart-objective-assessment`。主责：[togaf-strategy-capabilities](../../../togaf-strategy-capabilities/SKILL.md)。

来源：G176 §9.1–9.3。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

每个目的是否具体、可度量、可行动、现实、有时限，并追溯到已分类的目标？

- 该范围业务负责人
- 架构师
- 评审及治理负责人
- 每个目的是否具体、可度量、可行动、现实、有时限，并追溯到已分类的目标？
- 来源、范围与适用性


## 输入及缺口处理

必需：

- {'id': 'statement', 'meaning': '陈述', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'category', 'meaning': 'G176 §9.3目标类别ID', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'business_goal_ref', 'meaning': '对应的组织业务目标', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'goal_id', 'meaning': '所属目标ID', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'scope', 'meaning': '该对象负责或适用的范围', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'measure', 'meaning': '度量', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'unit', 'meaning': '单位', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'target', 'meaning': '目标值', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'organization_category', 'meaning': '组织自定类别', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'baseline', 'meaning': '基线值', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'owner', 'meaning': '负责人', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'action', 'meaning': '实现行动', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'realism_rationale', 'meaning': '现实性理由', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'realism_evidence', 'meaning': '支持现实性的证据ID', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'due', 'meaning': '截止日期（ISO）', 'origin': 'source-purpose-plus-project-contract'}

可选：

- 既有模型及历史结论

关键输入缺失时生成带ID的草稿与缺口，不计算无依据数值，不伪造批准或事实；结构错误直接拒绝。

## 元素、属性与关系

对象类型：guide:goal, guide:smart-objective。

```json
{
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
}
```

{
  "statement": {
    "meaning": "陈述",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "category": {
    "meaning": "G176 §9.3目标类别ID",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "business_goal_ref": {
    "meaning": "对应的组织业务目标",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "goal_id": {
    "meaning": "所属目标ID",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "scope": {
    "meaning": "该对象负责或适用的范围",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "measure": {
    "meaning": "度量",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "unit": {
    "meaning": "单位",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "target": {
    "meaning": "目标值",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "organization_category": {
    "meaning": "组织自定类别",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "baseline": {
    "meaning": "基线值",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "owner": {
    "meaning": "负责人",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "action": {
    "meaning": "实现行动",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "realism_rationale": {
    "meaning": "现实性理由",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "realism_evidence": {
    "meaning": "支持现实性的证据ID",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  },
  "due": {
    "meaning": "截止日期（ISO）",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-statement-plus-explicit-project-operational-field"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 把目标归入G176 §9.3的13类之一或组织自定类别
2. 把每个目的追溯到目标
3. 逐项核对具体、可度量、可行动、现实、有时限
4. 可度量项记录基线、目标与单位
5. 现实性给出理由与证据
6. 缺项列为待补，不由模板补数值

## 输出、检查与误读

- 范围及依据
- 逐条结果与理由
- 缺口、下一步与责任
- 版本和来源引用

- 13类目标是示例类别，不是封闭清单
- SMART只检查结构，现实性与数值合理性由责任人判断
- 目的须追溯到组织业务目标

- 名称、来源表格和成功输出不等于业务结论已核实
- 13类目标是示例类别，不是封闭清单
- SMART只检查结构，现实性与数值合理性由责任人判断
- 目的须追溯到组织业务目标


## 视图和交付物

- [SMART目的评估](../profiles/smart-objective-assessment-default.md)

- [business-goals-objectives](../deliverables/business-goals-objectives.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "目的O-1追溯到不存在的目标",
    "expected": "SMART-002",
    "why": "SMART-002 [O-1]: Objective must trace to a registered goal"
  },
  "modification_example": {
    "change": "为O-2补负责人、行动、现实性证据与截止日期",
    "expected": "分析结果变化：关闭缺口O-2:actionable,O-2:baseline,O-2:realistic,O-2:time-bound"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/smart-objective-assessment.md)
[完整操作案例](../../references/capability-addenda/smart-objective-assessment.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

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

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact smart-objective-assessment --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
