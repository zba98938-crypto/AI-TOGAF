# 目标九问检查

`profile_id`: architecture-governance-checklist-target；`artifact_id`: architecture-governance-checklist；主责：[togaf-artifact-review](../../../togaf-artifact-review/SKILL.md)。

来源：G184 §6.2；G186 §15.2.1表15-1、§15.2.2表15-2。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-addenda。

{
  "id": "architecture-governance-checklist-target",
  "version": "2.1-addenda",
  "source_verified": false,
  "layout_notes": "正文工作产品的字段表；不冒称原图复刻。reference/adaptive均保留全部列语义。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:governance_check。关系类型：。

```json
{
  "entities": {
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
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 目标九问与实施七问独立；实施第一问为是会直接接受合规
- SME确认事实、审计记录符合性、利益相关者批准目标和处置，不混淆角色
- 只有真实授权证据才能改变批准状态，示例所有状态保持候选
- G184简版与G186详细分支有差异，引用具体版本

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

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

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile architecture-governance-checklist-target --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile architecture-governance-checklist-target --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
