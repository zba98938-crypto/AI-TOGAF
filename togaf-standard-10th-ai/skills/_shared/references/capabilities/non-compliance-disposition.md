# 不合规影响与处置登记

ID：`non-compliance-disposition`。主责：[togaf-artifact-review](../../../togaf-artifact-review/SKILL.md)。

来源：G186 §15.2.2表15-2；G184 §6.2、§6.5。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

对已证实偏差应强制执行、临时豁免还是重审目标？

- 授权业务利益相关者
- 架构师
- 相关SME与实施负责人
- 对已证实偏差应强制执行、临时豁免还是重审目标？
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

对象类型：guide:noncompliance_disposition。

```json
{
  "guide:noncompliance_disposition": [
    "subject",
    "violated_spec",
    "original_value_basis",
    "evidence_refs",
    "impact",
    "options",
    "recommendation",
    "decision_owner",
    "decision",
    "expiry",
    "review_date",
    "review_owner",
    "follow_up"
  ]
}
```

{
  "name": {
    "meaning": "处置事项",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "subject": {
    "meaning": "实施对象与目标版本",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "violated_spec": {
    "meaning": "违反的规格ID",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "original_value_basis": {
    "meaning": "与批准目标一致的范围/期间/量测方法",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "evidence_refs": {
    "meaning": "偏差证据",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "impact": {
    "meaning": "价值、风险和置信度影响",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "options": {
    "meaning": "执行、临时豁免、变更目标三个选项及影响",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "recommendation": {
    "meaning": "架构师候选建议",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "decision_owner": {
    "meaning": "授权利益相关者",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "decision": {
    "meaning": "已决定或待决定；与建议分开",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "expiry": {
    "meaning": "临时豁免有效期",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "review_date": {
    "meaning": "复评日",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "review_owner": {
    "meaning": "复评责任人",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "follow_up": {
    "meaning": "纠偏/复评/目标重批及其证据",
    "value_rule": "值可追溯到原材料；组织规则明确标项目规则；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 核对目标约束是否确被违反而非实现偏好不同
2. 按开发目标时同一价值/风险口径分析影响
3. 请SME核实事实、列出三种处置及取舍
4. 向授权利益相关者提交建议，记录其决定
5. 临时豁免设置期限、复评责任与日期；执行需纠偏证据；改目标重走目标批准

## 输出、检查与误读

- 结论与证据表
- 未决项与责任/下一动作
- 模型和实际view_id引用

- 永久豁免实质改变目标，必须转目标变更
- 更换指标/范围来获得通过会使评估失效
- 建议、批准和落实是三个独立事实

- 永久豁免实质改变目标，必须转目标变更
- 更换指标/范围来获得通过会使评估失效
- 建议、批准和落实是三个独立事实


## 视图和交付物

- [不合规影响与处置登记](../profiles/non-compliance-disposition-default.md)

- [compliance-assessment](../deliverables/compliance-assessment.md)
- [change-request](../deliverables/change-request.md)
- [architecture-contract](../deliverables/architecture-contract.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "临时豁免没有到期日或复评责任",
    "expected": "missing-evidence",
    "why": "waiver-needs-expiry-review-owner拒绝完成",
    "original_expected_text": "waiver-needs-expiry-review-owner拒绝完成"
  },
  "modification_example": {
    "change": "把建议改为强制执行，计划10工作日修复",
    "expected": "新增纠偏验证任务，豁免期限不再充当授权；目标60秒保持"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/non-compliance-disposition.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

```json
{
  "notice": "虚构云帆物流案例；访谈、会议、测量与批准记录均为演示资料，不是实际业务证据。",
  "sources": [
    {
      "id": "src-non-compliance-disposition-default",
      "kind": "example",
      "description": "虚构云帆物流案例；访谈、会议、测量与批准记录均为演示资料，不是实际业务证据。 原始材料组：disposition",
      "locator": "examples/addenda/governance/raw-business-materials.json#disposition"
    }
  ],
  "entities": [
    {
      "id": "non-compliance-disposition-default-1",
      "type": "guide:noncompliance_disposition",
      "name": "签收延迟临时处置候选",
      "attributes": {
        "subject": "DELIVERY-API-v3 / TARGET-T1-v2",
        "violated_spec": "SPEC-60S",
        "original_value_basis": "城西站、同一业务日、签收可查询时延P95（秒）",
        "evidence_refs": [
          "NC-01",
          "NC-02"
        ],
        "impact": "93秒超过60秒，晚送达风险；样本只覆盖城西站，其他站影响未评估",
        "options": [
          {
            "action": "enforce",
            "impact": "10工作日修复，延后上线，保留60秒目标"
          },
          {
            "action": "temporary-waiver",
            "impact": "30日人工查询补偿，仍有晚送达风险；目标保持60秒"
          },
          {
            "action": "change-target",
            "impact": "若改为120秒必须重新分析客户影响并重走目标批准，当前无足够证据"
          }
        ],
        "recommendation": "temporary-waiver",
        "decision_owner": "运营、数据、财务授权利益相关者",
        "decision": "pending；尚不可执行",
        "expiry": "2026-12-01",
        "review_date": "2026-11-09",
        "review_owner": "运营负责人",
        "follow_up": "批准后方可开始豁免；每周一复评；到期未关闭重新升级，不永久续期"
      },
      "evidence": [
        "src-non-compliance-disposition-default"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-non-compliance-disposition-default",
    "artifact_id": "non-compliance-disposition",
    "profile_id": "non-compliance-disposition-default",
    "title": "不合规影响与处置登记",
    "entity_ids": [
      "non-compliance-disposition-default-1"
    ],
    "relationship_ids": [],
    "analysis": "沿原P95/城西站口径分析三项选择，建议有期限豁免；尚未获得授权批准，不能把建议写作已豁免。",
    "legend": "表格逐行记录；所有业务内容虚构。未知、未达到、未批准分别显示；ID用于稳定引用。"
  },
  "raw_input_group": "disposition"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact non-compliance-disposition --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
