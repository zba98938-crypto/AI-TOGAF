# 阶段边界与项目收尾记录

ID：`project-stage-closure-record`。主责：[togaf-artifact-review](../../../togaf-artifact-review/SKILL.md)。

来源：G188 §3.5.1–3.6.3。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

是否继续、修改或终止阶段/项目，责任与成果是否可交接？

- 架构工作发起人
- 项目经理/架构师
- 业务利益相关者与SME
- 是否继续、修改或终止阶段/项目，责任与成果是否可交接？
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

对象类型：guide:closure_record。

```json
{
  "guide:closure_record": [
    "closure_kind",
    "closure_reason",
    "products",
    "performance",
    "risks_issues",
    "handover",
    "next_stage",
    "authority",
    "decision",
    "evidence_refs",
    "follow_up"
  ]
}
```

{
  "name": {
    "meaning": "收尾/边界记录",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "closure_kind": {
    "meaning": "stage-boundary或project-closure",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "closure_reason": {
    "meaning": "完成或提前终止及依据",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "products": {
    "meaning": "产品验收状态与未完成处置",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "performance": {
    "meaning": "计划/实际时间成本质量范围风险收益；不合并成单分",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "risks_issues": {
    "meaning": "风险问题剩余责任和处置",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "handover": {
    "meaning": "接收方与足以开展后续工作的条件",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "next_stage": {
    "meaning": "下一阶段计划或不适用",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "authority": {
    "meaning": "决定继续/变更/终止的监督机构",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "decision": {
    "meaning": "建议与批准分开",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "evidence_refs": {
    "meaning": "材料ID",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "follow_up": {
    "meaning": "所需补证、变更或资源释放条件",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 区分阶段边界、成功完成和提前终止
2. 核对所有产品状态及验收/撤销/移交去向
3. 比较计划/实际并保留容差未知
4. 提交剩余风险、项目影响与下一阶段或关闭建议
5. 监督机构决定并记录正式接受，之后才能释放/重新授权资源

## 输出、检查与误读

- 实际分析记录和结论
- 未决项、责任及动作
- 稳定对象ID、来源与实际view_id

- 阶段产品验收、边界决策、下一阶段授权是不同事实
- 商业论证失效可以提前终止，不能假装全部产品成功交付
- 计划/实际偏差不自动证明超过未给出的容差

- 阶段产品验收、边界决策、下一阶段授权是不同事实
- 商业论证失效可以提前终止，不能假装全部产品成功交付
- 计划/实际偏差不自动证明超过未给出的容差


## 视图和交付物

- [阶段边界报告](../profiles/project-stage-closure-record-stage.md)
- [项目收尾建议](../profiles/project-stage-closure-record-project.md)

- [statement-of-work](../deliverables/statement-of-work.md)
- [compliance-assessment](../deliverables/compliance-assessment.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "未接受产品且无终止理由就宣布completed",
    "expected": "closure-products-not-accepted"
  },
  "modification_example": {
    "change": "说明表修订获接受并批准下一阶段；项目终止获发起人接受",
    "expected": "阶段可关闭并另行授权下一阶段；项目按终止结案，保持未交付目标事实"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/project-stage-closure-record.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

```json
{
  "notice": "虚构海岚配送架构项目；所有访谈、估算、任务与批准资料仅用于方法演示。",
  "sources": [
    {
      "id": "src-project-stage-closure-record-stage",
      "kind": "example",
      "description": "虚构海岚配送架构项目；所有访谈、估算、任务与批准资料仅用于方法演示。 材料组 stage-close",
      "locator": "examples/addenda/project-management/raw-business-materials.json#stage-close"
    }
  ],
  "entities": [
    {
      "id": "project-stage-closure-record-stage-1",
      "type": "guide:closure_record",
      "name": "流程分析阶段",
      "attributes": {
        "closure_kind": "stage-boundary",
        "closure_reason": "completed-proposed",
        "products": [
          {
            "id": "DEL-FLOW",
            "accepted": true
          },
          {
            "id": "DEL-DESC",
            "accepted": false
          }
        ],
        "performance": {
          "planned_days": 10,
          "actual_days": 11,
          "planned_hours": 60,
          "actual_hours": 68,
          "tolerances": "unknown"
        },
        "risks_issues": "新增门店增加后续工作；DEL-DESC未接受",
        "handover": "流程图可供内部建模；说明表缺口未关闭",
        "next_stage": "建模计划草拟，尚未批准",
        "authority": "项目监督机构/发起人",
        "decision": "pending",
        "evidence_refs": [
          "SC-01",
          "SC-02"
        ],
        "follow_up": "修正说明表并取得接受；确认容差与下一阶段计划，不能自行宣布完成"
      },
      "evidence": [
        "src-project-stage-closure-record-stage"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-project-stage-closure-record-stage",
    "artifact_id": "project-stage-closure-record",
    "profile_id": "project-stage-closure-record-stage",
    "title": "阶段边界报告",
    "entity_ids": [
      "project-stage-closure-record-stage-1"
    ],
    "relationship_ids": [],
    "analysis": "阶段实际比计划多1天8小时，但容差未知不能断言越权；未接受说明表阻断完成型收尾。",
    "legend": "虚构记录；计划、实绩、建议、授权和批准分别表述。空缺不等于零或已接受。"
  },
  "raw_input_group": "stage-close"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact project-stage-closure-record --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
