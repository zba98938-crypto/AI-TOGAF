# 架构治理检查清单

ID：`architecture-governance-checklist`。主责：[togaf-artifact-review](../../../togaf-artifact-review/SKILL.md)。

来源：G184 §6.2；G186 §15.2.1表15-1、§15.2.2表15-2。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

目标能否批准，实施是否合理遵循目标且如何处理偏差？

- 授权业务利益相关者
- 架构师
- 相关SME与实施负责人
- 目标能否批准，实施是否合理遵循目标且如何处理偏差？
- 依据完整、同口径、责任和未决项清晰


## 输入及缺口处理

必需：

- 范围和五维语境
- 原始访谈/计划/测量及定位
- 授权角色和适用目标版本

可选：

- 既有模型、视图、参考规范和组织规则

逐项登记缺口；未知不等于否或零。缺授权、原口径、时点或关键证据时只能候选，不自动批准、通过或核算。

## 元素、属性与关系

对象类型：guide:governance_check。

```json
{
  "guide:governance_check": [
    "subject",
    "sequence",
    "question",
    "answer",
    "evidence_refs",
    "accountable_role",
    "next_action",
    "result",
    "source_variant"
  ]
}
```

{
  "name": {
    "meaning": "检查项名称",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "subject": {
    "meaning": "受评对象及精确版本",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "sequence": {
    "meaning": "来源规定的检查顺序",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "question": {
    "meaning": "检查问题",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "answer": {
    "meaning": "yes/no/unknown/not-reached；后两者是项目缺口约定",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "evidence_refs": {
    "meaning": "对应原料和模型/视图证据",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "accountable_role": {
    "meaning": "责任角色及决策权",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "next_action": {
    "meaning": "按本问题分支采取的动作",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "result": {
    "meaning": "本案例整体结论；不代表真实批准",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "source_variant": {
    "meaning": "使用的指南和差异说明",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 区分目标开发与实施变更两类治理对象
2. 锁定对象版本、上层约束、原价值口径和角色权利
3. 按来源顺序执行检查并引用证据
4. 目标任一否/未知先补足；实施Q1为是时接受合理解释
5. 不合规转影响评估和处置，批准不能由生成器或审计员代行

## 输出、检查与误读

- 结论与证据表
- 未决项与责任/下一动作
- 模型和实际view_id引用

- 目标九问与实施七问独立；实施第一问为是会直接接受合规
- SME确认事实、审计记录符合性、利益相关者批准目标和处置，不混淆角色
- 只有真实授权证据才能改变批准状态，示例所有状态保持候选
- G184简版与G186详细分支有差异，引用具体版本

- 目标九问与实施七问独立；实施第一问为是会直接接受合规
- SME确认事实、审计记录符合性、利益相关者批准目标和处置，不混淆角色
- 只有真实授权证据才能改变批准状态，示例所有状态保持候选
- G184简版与G186详细分支有差异，引用具体版本


## 视图和交付物

- [目标九问检查](../profiles/architecture-governance-checklist-target.md)
- [实施七问检查](../profiles/architecture-governance-checklist-implementation.md)

- [compliance-assessment](../deliverables/compliance-assessment.md)
- [architecture-contract](../deliverables/architecture-contract.md)


- [implementation-governance-model](../deliverables/implementation-governance-model.md)

项目路由：F阶段在适用时（if any）准备实施治理模型；G阶段使用其检查点、决策权和升级规则进行实施治理。关联工作产品不自动创建必需交付物、不代替适用性裁剪或真实授权。

## 反例与修改示例

```json
{
  "counterexample": {
    "input": "目标九问只给八项；或实施Q1=yes仍按个人偏好判失败",
    "expected": "missing-evidence",
    "why": "缺项被拒绝；合理解释路径保持合规",
    "original_expected_text": "缺项被拒绝；合理解释路径保持合规"
  },
  "modification_example": {
    "change": "实施样本由41秒改为93秒，Q1=no；Q2–6=yes，Q7=unknown",
    "expected": "从合规转为待利益相关者处置批准，不自动豁免"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/architecture-governance-checklist.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

```json
{
  "notice": "虚构云帆物流案例；访谈、会议、测量与批准记录均为演示资料，不是实际业务证据。",
  "sources": [
    {
      "id": "src-architecture-governance-checklist-target",
      "kind": "example",
      "description": "虚构云帆物流案例；访谈、会议、测量与批准记录均为演示资料，不是实际业务证据。 原始材料组：target",
      "locator": "examples/addenda/governance/raw-business-materials.json#target"
    }
  ],
  "entities": [
    {
      "id": "architecture-governance-checklist-target-1",
      "type": "guide:governance_check",
      "name": "target Q1",
      "attributes": {
        "subject": "TARGET-T1-v2",
        "sequence": 1,
        "question": "是否正确识别利益相关者？",
        "answer": "yes",
        "evidence_refs": [
          "TG-01"
        ],
        "accountable_role": "架构师准备／SME核实；目标/豁免/执行由授权利益相关者决定",
        "next_action": "继续下一检查",
        "result": "pending",
        "source_variant": "G186表15-1/15-2；G184 §6.2为简版。G186实施Q1=是直接接受合规，不能机械要求七个是。"
      },
      "evidence": [
        "src-architecture-governance-checklist-target"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-governance-checklist-target-2",
      "type": "guide:governance_check",
      "name": "target Q2",
      "attributes": {
        "subject": "TARGET-T1-v2",
        "sequence": 2,
        "question": "是否考虑上层约束与指导？",
        "answer": "yes",
        "evidence_refs": [
          "TG-01"
        ],
        "accountable_role": "架构师准备／SME核实；目标/豁免/执行由授权利益相关者决定",
        "next_action": "继续下一检查",
        "result": "pending",
        "source_variant": "G186表15-1/15-2；G184 §6.2为简版。G186实施Q1=是直接接受合规，不能机械要求七个是。"
      },
      "evidence": [
        "src-architecture-governance-checklist-target"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-governance-checklist-target-3",
      "type": "guide:governance_check",
      "name": "target Q3",
      "attributes": {
        "subject": "TARGET-T1-v2",
        "sequence": 3,
        "question": "适当SME是否同意事实和解释？",
        "answer": "yes",
        "evidence_refs": [
          "TG-02"
        ],
        "accountable_role": "架构师准备／SME核实；目标/豁免/执行由授权利益相关者决定",
        "next_action": "继续下一检查",
        "result": "pending",
        "source_variant": "G186表15-1/15-2；G184 §6.2为简版。G186实施Q1=是直接接受合规，不能机械要求七个是。"
      },
      "evidence": [
        "src-architecture-governance-checklist-target"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-governance-checklist-target-4",
      "type": "guide:governance_check",
      "name": "target Q4",
      "attributes": {
        "subject": "TARGET-T1-v2",
        "sequence": 4,
        "question": "约束/指导是否与视图及模型分析一致？",
        "answer": "yes",
        "evidence_refs": [
          "TG-02"
        ],
        "accountable_role": "架构师准备／SME核实；目标/豁免/执行由授权利益相关者决定",
        "next_action": "继续下一检查",
        "result": "pending",
        "source_variant": "G186表15-1/15-2；G184 §6.2为简版。G186实施Q1=是直接接受合规，不能机械要求七个是。"
      },
      "evidence": [
        "src-architecture-governance-checklist-target"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-governance-checklist-target-5",
      "type": "guide:governance_check",
      "name": "target Q5",
      "attributes": {
        "subject": "TARGET-T1-v2",
        "sequence": 5,
        "question": "视图是否回应关注点并与模型分析一致？",
        "answer": "yes",
        "evidence_refs": [
          "TG-02"
        ],
        "accountable_role": "架构师准备／SME核实；目标/豁免/执行由授权利益相关者决定",
        "next_action": "继续下一检查",
        "result": "pending",
        "source_variant": "G186表15-1/15-2；G184 §6.2为简版。G186实施Q1=是直接接受合规，不能机械要求七个是。"
      },
      "evidence": [
        "src-architecture-governance-checklist-target"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-governance-checklist-target-6",
      "type": "guide:governance_check",
      "name": "target Q6",
      "attributes": {
        "subject": "TARGET-T1-v2",
        "sequence": 6,
        "question": "利益相关者是否理解价值和实现不确定性？",
        "answer": "yes",
        "evidence_refs": [
          "TG-03"
        ],
        "accountable_role": "架构师准备／SME核实；目标/豁免/执行由授权利益相关者决定",
        "next_action": "继续下一检查",
        "result": "pending",
        "source_variant": "G186表15-1/15-2；G184 §6.2为简版。G186实施Q1=是直接接受合规，不能机械要求七个是。"
      },
      "evidence": [
        "src-architecture-governance-checklist-target"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-governance-checklist-target-7",
      "type": "guide:governance_check",
      "name": "target Q7",
      "attributes": {
        "subject": "TARGET-T1-v2",
        "sequence": 7,
        "question": "是否理解达成目标所需工作及风险？",
        "answer": "yes",
        "evidence_refs": [
          "TG-03"
        ],
        "accountable_role": "架构师准备／SME核实；目标/豁免/执行由授权利益相关者决定",
        "next_action": "继续下一检查",
        "result": "pending",
        "source_variant": "G186表15-1/15-2；G184 §6.2为简版。G186实施Q1=是直接接受合规，不能机械要求七个是。"
      },
      "evidence": [
        "src-architecture-governance-checklist-target"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-governance-checklist-target-8",
      "type": "guide:governance_check",
      "name": "target Q8",
      "attributes": {
        "subject": "TARGET-T1-v2",
        "sequence": 8,
        "question": "是否理解置信度限制？",
        "answer": "yes",
        "evidence_refs": [
          "TG-03"
        ],
        "accountable_role": "架构师准备／SME核实；目标/豁免/执行由授权利益相关者决定",
        "next_action": "继续下一检查",
        "result": "pending",
        "source_variant": "G186表15-1/15-2；G184 §6.2为简版。G186实施Q1=是直接接受合规，不能机械要求七个是。"
      },
      "evidence": [
        "src-architecture-governance-checklist-target"
      ],
      "certainty": "assumed"
    },
    {
      "id": "architecture-governance-checklist-target-9",
      "type": "guide:governance_check",
      "name": "target Q9",
      "attributes": {
        "subject": "TARGET-T1-v2",
        "sequence": 9,
        "question": "利益相关者是否批准视图？",
        "answer": "unknown",
        "evidence_refs": [
          "TG-03"
        ],
        "accountable_role": "架构师准备／SME核实；目标/豁免/执行由授权利益相关者决定",
        "next_action": "由利益相关者决定重做或取消；未批准不得发布为批准目标",
        "result": "pending",
        "source_variant": "G186表15-1/15-2；G184 §6.2为简版。G186实施Q1=是直接接受合规，不能机械要求七个是。"
      },
      "evidence": [
        "src-architecture-governance-checklist-target"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-architecture-governance-checklist-target",
    "artifact_id": "architecture-governance-checklist",
    "profile_id": "architecture-governance-checklist-target",
    "title": "目标九问检查",
    "entity_ids": [
      "architecture-governance-checklist-target-1",
      "architecture-governance-checklist-target-2",
      "architecture-governance-checklist-target-3",
      "architecture-governance-checklist-target-4",
      "architecture-governance-checklist-target-5",
      "architecture-governance-checklist-target-6",
      "architecture-governance-checklist-target-7",
      "architecture-governance-checklist-target-8",
      "architecture-governance-checklist-target-9"
    ],
    "relationship_ids": [],
    "analysis": "依来源顺序评估，目标Q9未知阻断批准；实施合理异步解法满足明确规格，不能因个人同步偏好判不合规。",
    "legend": "表格逐行记录；所有业务内容虚构。未知、未达到、未批准分别显示；ID用于稳定引用。"
  },
  "raw_input_group": "target"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact architecture-governance-checklist --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
