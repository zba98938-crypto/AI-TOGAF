# 价值实现评估

ID：`value-realization-assessment`。主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G184 §10.1.7、§10.1.9、§11.4；G186 §8.7、§10.4、§14、§15.2.3。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

目标价值是否实际实现，差距是否需要H阶段发起新工作？

- 授权业务利益相关者
- 架构师
- 相关SME与实施负责人
- 目标价值是否实际实现，差距是否需要H阶段发起新工作？
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

对象类型：guide:value_observation。

```json
{
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
}
```

{
  "name": {
    "meaning": "价值指标",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "target_ref": {
    "meaning": "目标/价值主张及版本",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "beneficiary": {
    "meaning": "价值接收方",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "baseline": {
    "meaning": "基线值",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "expected": {
    "meaning": "目标值及期望改善",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "observed": {
    "meaning": "实际值及证据",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "unit": {
    "meaning": "带方向的单位/量表",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "periods": {
    "meaning": "基线与实际期间",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "scope": {
    "meaning": "比较范围及业务量",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "method": {
    "meaning": "同口径测量方法",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "calculation_basis": {
    "meaning": "明确声明的比较规则及计算",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "finding": {
    "meaning": "已达/未达/待测；不得把合规当收益",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "confounders": {
    "meaning": "同时变化的非架构因素",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "attribution": {
    "meaning": "归因是否证实",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "owner": {
    "meaning": "组合/运营价值责任人",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "next_review": {
    "meaning": "下次价值复评",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "compliance_link": {
    "meaning": "G实施合规引用与其证明边界",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 明确价值主张、接收方、责任人与观察期间
2. 锁定同范围同单位的基线/目标和计算依据
3. 收集运营实际及证据，识别同时发生变化
4. 逐指标比较目标差距并解释不确定性与归因限制
5. 由组合/运营持续复评，必要时创建H变更/新工作请求

## 输出、检查与误读

- 结论与证据表
- 未决项与责任/下一动作
- 模型和实际view_id引用

- G检验实施合规，H检验价值持续性及新变化，不能互相替代
- 不同范围、业务量、期间口径须归一化有依据或保持不可比
- 没有来源或明确项目规则不得计算ROI、权重或宣称收益归因
- 实际未测不能用0代替；计划收益不等于已实现价值

- G检验实施合规，H检验价值持续性及新变化，不能互相替代
- 不同范围、业务量、期间口径须归一化有依据或保持不可比
- 没有来源或明确项目规则不得计算ROI、权重或宣称收益归因
- 实际未测不能用0代替；计划收益不等于已实现价值


## 视图和交付物

- [T1价值实现评估](../profiles/value-realization-assessment-default.md)

- [compliance-assessment](../deliverables/compliance-assessment.md)
- [change-request](../deliverables/change-request.md)
- [implementation-migration-plan](../deliverables/implementation-migration-plan.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "实际为全部站点而基线只有城西站",
    "expected": "missing-evidence",
    "why": "incomparable-measurement-scope；停止差额计算",
    "original_expected_text": "incomparable-measurement-scope；停止差额计算"
  },
  "modification_example": {
    "change": "人工签收实际工时620改为480且保持口径",
    "expected": "观察改善320小时，目标超额20小时；归因仍未证实，晚送率仍未达成"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/value-realization-assessment.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

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

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact value-realization-assessment --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
