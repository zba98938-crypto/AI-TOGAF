# T1价值实现评估

`profile_id`: value-realization-assessment-default；`artifact_id`: value-realization-assessment；主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G184 §10.1.7、§10.1.9、§11.4；G186 §8.7、§10.4、§14、§15.2.3。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-addenda。

{
  "id": "value-realization-assessment-default",
  "version": "2.1-addenda",
  "source_verified": false,
  "layout_notes": "正文工作产品的字段表；不冒称原图复刻。reference/adaptive均保留全部列语义。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:value_observation。关系类型：。

```json
{
  "entities": {
    "guide:value_observation": [
      "target_ref",
      "beneficiary",
      "baseline",
      "expected",
      "observed",
      "unit",
      "periods",
      "scope",
      "method",
      "calculation_basis",
      "finding",
      "confounders",
      "attribution",
      "owner",
      "next_review",
      "compliance_link"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- G检验实施合规，H检验价值持续性及新变化，不能互相替代
- 不同范围、业务量、期间口径须归一化有依据或保持不可比
- 没有来源或明确项目规则不得计算ROI、权重或宣称收益归因
- 实际未测不能用0代替；计划收益不等于已实现价值

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构云帆物流案例；访谈、会议、测量与批准记录均为演示资料，不是实际业务证据。",
  "sources": [
    {
      "id": "src-value-realization-assessment-default",
      "kind": "example",
      "description": "虚构云帆物流案例；访谈、会议、测量与批准记录均为演示资料，不是实际业务证据。 原始材料组：value",
      "locator": "examples/addenda/governance/raw-business-materials.json#value"
    }
  ],
  "entities": [
    {
      "id": "value-realization-assessment-default-1",
      "type": "guide:value_observation",
      "name": "人工签收工时",
      "attributes": {
        "target_ref": "TARGET-T1-v2",
        "beneficiary": "城西站运营与客户",
        "baseline": 800,
        "expected": {
          "target": 500,
          "improvement": 300
        },
        "observed": {
          "actual": 620,
          "improvement": 180,
          "evidence": "VL-01"
        },
        "unit": {
          "observation": "小时/月",
          "difference": "小时/月"
        },
        "periods": {
          "baseline": "2026-10",
          "actual": "2027-01"
        },
        "scope": "城西站10000单/月，订单集合口径相同",
        "method": "从工时日志/送达记录汇总；率指标为该月晚送单数/该月总单数；此计算是项目规则",
        "calculation_basis": {
          "rule": "越低越好；改善=基线-实际，目标差距=实际-目标；百分点不作百分比增长",
          "remaining_gap": 120
        },
        "finding": "target-not-met",
        "confounders": [
          "同期运营排班优化"
        ],
        "attribution": "not-established；不能归功为EA独占收益",
        "owner": "组合负责人会同运营负责人",
        "next_review": "2027-03-10",
        "compliance_link": "VL-03/G实施检查通过只证明规定实现项符合；H继续验证价值"
      },
      "evidence": [
        "src-value-realization-assessment-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "value-realization-assessment-default-2",
      "type": "guide:value_observation",
      "name": "晚送率",
      "attributes": {
        "target_ref": "TARGET-T1-v2",
        "beneficiary": "城西站运营与客户",
        "baseline": 4,
        "expected": {
          "target": 2,
          "improvement": 2
        },
        "observed": {
          "actual": 2.8,
          "improvement": 1.2,
          "evidence": "VL-02"
        },
        "unit": {
          "observation": "%",
          "difference": "百分点"
        },
        "periods": {
          "baseline": "2026-10",
          "actual": "2027-01"
        },
        "scope": "城西站10000单/月，订单集合口径相同",
        "method": "从工时日志/送达记录汇总；率指标为该月晚送单数/该月总单数；此计算是项目规则",
        "calculation_basis": {
          "rule": "越低越好；改善=基线-实际，目标差距=实际-目标；百分点不作百分比增长",
          "remaining_gap": 0.8
        },
        "finding": "target-not-met",
        "confounders": [
          "同期运营排班优化"
        ],
        "attribution": "not-established；不能归功为EA独占收益",
        "owner": "组合负责人会同运营负责人",
        "next_review": "2027-03-10",
        "compliance_link": "VL-03/G实施检查通过只证明规定实现项符合；H继续验证价值"
      },
      "evidence": [
        "src-value-realization-assessment-default"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-value-realization-assessment-default",
    "artifact_id": "value-realization-assessment",
    "profile_id": "value-realization-assessment-default",
    "title": "T1价值实现评估",
    "entity_ids": [
      "value-realization-assessment-default-1",
      "value-realization-assessment-default-2"
    ],
    "relationship_ids": [],
    "analysis": "工时改善180小时但离目标仍差120小时；晚送率改善1.2百分点但仍差0.8百分点。G合规通过不能改变两个未达成结论；排班变化阻止单独归因EA。",
    "legend": "表格逐行记录；所有业务内容虚构。未知、未达到、未批准分别显示；ID用于稳定引用。"
  },
  "raw_input_group": "value"
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile value-realization-assessment-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile value-realization-assessment-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
