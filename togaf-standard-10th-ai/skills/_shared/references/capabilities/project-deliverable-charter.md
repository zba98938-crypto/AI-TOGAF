# 交付物章程与验收流程

ID：`project-deliverable-charter`。主责：[togaf-artifact-review](../../../togaf-artifact-review/SKILL.md)。

来源：G188 §3.1.8示例3-14、§3.2.2–3.2.3、§3.5.1。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

交付物要交什么、如何核验、由谁接受？

- 架构工作发起人
- 项目经理/架构师
- 业务利益相关者与SME
- 交付物要交什么、如何核验、由谁接受？
- 依据、权限、完整性和可追溯性


## 输入及缺口处理

必需：

- 范围、五维语境、所用目标与交付物版本
- 原始计划/访谈/验收/估算及来源ID
- 组织授权和容差规则；缺失时不代推

可选：

- 历史项目及组织模板

关键依据未知时给候选表、受影响ID与责任；不编造权重、阈值、估算、批准或实际完成。

## 元素、属性与关系

对象类型：guide:deliverable_charter。

```json
{
  "guide:deliverable_charter": [
    "deliverable_id",
    "scope",
    "exclusions",
    "required_inputs",
    "acceptance_criteria",
    "acceptance_process",
    "decision_roles",
    "review_observations",
    "status",
    "evidence_refs",
    "next_action"
  ]
}
```

{
  "name": {
    "meaning": "交付物章程名称",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "deliverable_id": {
    "meaning": "交付物稳定ID与版本",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "scope": {
    "meaning": "内容与范围",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "exclusions": {
    "meaning": "明确排除",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "required_inputs": {
    "meaning": "输入及其版本/就绪情况",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "acceptance_criteria": {
    "meaning": "可检验条件与既有单项验收准则ID",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "acceptance_process": {
    "meaning": "按组织规则的移交/评审/修订/终审流程",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "decision_roles": {
    "meaning": "评审/修订/最终接受角色分开",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "review_observations": {
    "meaning": "实际评审发现与证据",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "status": {
    "meaning": "候选/评审/接受/拒绝；生成不等于接受",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "evidence_refs": {
    "meaning": "材料ID",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "next_action": {
    "meaning": "补缺或下一验收动作",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 从决策和利益相关者定义产品范围与排除
2. 确认输入与版本并找缺口
3. 写可观察验收准则，引用已有architecture-acceptance-criteria记录
4. 规定评审与修订流程及有权接受者
5. 逐条实际评审，保留拒绝/重作路径；接受后再进入阶段/项目关闭

## 输出、检查与误读

- 实际分析记录和结论
- 未决项、责任及动作
- 稳定对象ID、来源与实际view_id

- 文档与软件可有不同验收流程，不复制时长为TOGAF要求
- 生成、移交、评审与接受是不同状态
- 一项未满足准则不能被其他已满足项的数量抵消

- 文档与软件可有不同验收流程，不复制时长为TOGAF要求
- 生成、移交、评审与接受是不同状态
- 一项未满足准则不能被其他已满足项的数量抵消


## 视图和交付物

- [交付物章程与验收流程](../profiles/project-deliverable-charter-default.md)

- [statement-of-work](../deliverables/statement-of-work.md)
- [compliance-assessment](../deliverables/compliance-assessment.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "覆盖11/12却标全部准则通过",
    "expected": "criterion-result-contradiction"
  },
  "modification_example": {
    "change": "补齐APP-12且四项准则都得到验证，仍未取得业务负责人接受",
    "expected": "准则已满足但状态仍awaiting-acceptance，不能自动accepted"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/project-deliverable-charter.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

```json
{
  "notice": "虚构海岚配送架构项目；所有访谈、估算、任务与批准资料仅用于方法演示。",
  "sources": [
    {
      "id": "src-project-deliverable-charter-default",
      "kind": "example",
      "description": "虚构海岚配送架构项目；所有访谈、估算、任务与批准资料仅用于方法演示。 材料组 charter",
      "locator": "examples/addenda/project-management/raw-business-materials.json#charter"
    }
  ],
  "entities": [
    {
      "id": "project-deliverable-charter-default-1",
      "type": "guide:deliverable_charter",
      "name": "应用关系与信息使用说明章程",
      "attributes": {
        "deliverable_id": "DEL-REL-v1",
        "scope": "城东/城西两仓订单与库存接口，12应用",
        "exclusions": [
          "薪酬系统"
        ],
        "required_inputs": [
          {
            "id": "DEL-APPS-v2",
            "status": "provided"
          },
          {
            "id": "DATA-INTERVIEWS",
            "status": "APP-12资料缺失"
          }
        ],
        "acceptance_criteria": [
          {
            "id": "AC-COVERAGE",
            "rule": "12应用全部覆盖",
            "required_total": 12,
            "observed": 11,
            "result": "not-met"
          },
          {
            "id": "AC-DIRECTION",
            "rule": "方向来自接口记录",
            "result": "needs-review"
          },
          {
            "id": "AC-USEMOD",
            "rule": "信息使用/修改分别表达",
            "result": "needs-review"
          },
          {
            "id": "AC-UNKNOWN",
            "rule": "未知带ID与责任人",
            "result": "needs-review"
          }
        ],
        "acceptance_process": [
          {
            "step": "初审",
            "duration": 5,
            "unit": "workday",
            "role": "业务代表"
          },
          {
            "step": "处理意见",
            "duration": 3,
            "unit": "workday",
            "role": "架构师"
          },
          {
            "step": "终审",
            "duration": 2,
            "unit": "workday",
            "role": "业务负责人",
            "outcomes": [
              "accept",
              "reject",
              "rework"
            ]
          }
        ],
        "decision_roles": "业务代表评审、架构师修订、业务负责人接受；项目经理记录",
        "review_observations": "APP-12接口缺失，当前只覆盖11应用",
        "status": "in-review; not-accepted",
        "evidence_refs": [
          "DC-01",
          "DC-02",
          "DC-03",
          "DC-04"
        ],
        "next_action": "补APP-12数据并复核其余条件；终审不预设通过"
      },
      "evidence": [
        "src-project-deliverable-charter-default"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-project-deliverable-charter-default",
    "artifact_id": "project-deliverable-charter",
    "profile_id": "project-deliverable-charter-default",
    "title": "交付物章程与验收流程",
    "entity_ids": [
      "project-deliverable-charter-default-1"
    ],
    "relationship_ids": [],
    "analysis": "从DC-01/02区分范围、排除、输入和四条验收准则；DC-03是项目5/3/2日流程，不照搬G188示例的2周等时长。11/12覆盖不满足准则。",
    "legend": "虚构记录；计划、实绩、建议、授权和批准分别表述。空缺不等于零或已接受。"
  },
  "raw_input_group": "charter"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact project-deliverable-charter --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
