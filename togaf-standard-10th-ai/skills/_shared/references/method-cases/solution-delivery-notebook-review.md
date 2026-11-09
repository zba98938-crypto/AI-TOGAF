# 预约工作包的需求规格与风险控制配对

所有业务材料、人员、目标和授权均为明示虚构；执行结果只覆盖下述情景。

方法：`solution-delivery-notebook-review`。来源：G186 附录D 表D-1。
可复用材料：[四类场景JSON](../method-case-materials/solution-delivery-notebook-review.json)。

## 决策与原始业务资料

仅有目标架构概念图，能否据此判断重试控制和退货能力已交付？

|证据 ID|原始业务材料|
|---|---|
|SCOPE|工作包只补预约中央预占，不处理自提退货；双店试点后才讨论推广。|
|SPEC|需求是确认前取得预占凭证；事件接口规格必须携带该凭证ID。|
|RISK|重试可能重复预占，候选控制为请求键幂等；尚无控制运行结果。|

充分输入的精确结构如下；数值与ID来自本案例材料，不从执行结果反推。

```json
{
  "id": "NB-PILOT",
  "source_ids": [
    "SCOPE",
    "SPEC",
    "RISK"
  ],
  "evidence": [
    "SCOPE",
    "SPEC",
    "RISK"
  ],
  "work_package_id": "WP-PILOT",
  "solution_concept_ref": "VIEW-RESERVATION",
  "implementation_strategy": "先双店试点；中央预占成功才确认预约",
  "stakeholders": [
    {
      "id": "OPS",
      "name": "门店运营",
      "requirement_ids": [
        "REQ-RESERVE"
      ]
    }
  ],
  "requirements": [
    {
      "id": "REQ-RESERVE",
      "statement": "确认前取得中央库存预占凭证",
      "stakeholder_ids": [
        "OPS"
      ]
    }
  ],
  "specifications": [
    {
      "id": "SPEC-RESERVE",
      "requirement_id": "REQ-RESERVE",
      "statement": "确认事件引用预占凭证ID",
      "spec_type": "事件接口",
      "applies_to": "预约服务"
    }
  ],
  "risks": [
    {
      "id": "RISK-DUP",
      "description": "重试重复预占"
    }
  ],
  "controls": [
    {
      "id": "CTRL-IDEM",
      "risk_id": "RISK-DUP",
      "statement": "重复请求键只返回同一预占结果",
      "applies_to": "预约接口"
    }
  ],
  "gaps": [
    {
      "id": "GAP-RESERVE",
      "description": "当前确认无中央预占",
      "in_scope": true
    },
    {
      "id": "GAP-RETURN",
      "description": "自提退货流程未覆盖",
      "in_scope": false
    }
  ],
  "architecture_summary": {
    "business": {
      "view_ids": [
        "VIEW-business"
      ]
    },
    "information": {
      "view_ids": [
        "VIEW-information"
      ]
    },
    "application": {
      "view_ids": [
        "VIEW-application"
      ]
    },
    "security": {
      "view_ids": [
        "VIEW-security"
      ]
    },
    "infrastructure": {
      "not_applicable_reason": "沿用已声明的试点平台，本工作包不改变基础设施"
    }
  }
}
```

## 来源规则与项目规则

1. **来源规则**：G186表D-1区分需求/规格与风险/控制两种配对，并明确范围内外差距；领域架构摘要只供参考。
2. **项目规则**：本案例采用明确的来源ID、结构字段和有界状态；执行器检查可观察契约，业务充分性另由推理审阅说明。
3. **项目规则**：变化场景只改变材料中列出的事实；未变字段不被重新编造，所有批准与实际运行效果均保持未授予。

## 转换与推理

1. 概念图只解释方案，不能代替可检查的事件规格。
2. 需求与规格、风险与控制分别配对，不能把同一条连线当两种证明。
3. 退货是明确范围外差距，保留后续工作责任。
4. 有控制条目只证明设计已记录；没有运行证据就不能判断重复预占已被消除。

## 输出与追溯

下列预期在执行前由业务材料独立编写；实际执行只对这些明确字段作比较。

```json
{
  "gap_reasons": [],
  "in_scope_gap_ids": [
    "GAP-RESERVE"
  ],
  "out_of_scope_gap_ids": [
    "GAP-RETURN"
  ]
}
```

一项规格与一项控制分别回链需求和风险。

机械可复核字段、缺口和引用；业务结论不由计算器输出自动批准。完整输入、预期与实际结果见本轮方法证据目录。

## 修改演练

本次替换的业务字段如下；需按新事实重评。

- `gaps[1].in_scope`：false → true

将退货纳入工作包后，原范围外说明失效，需重新确认未处理差距。

变化后需重新执行原方法；原结论只保留到未改变的事实范围。

```json
{
  "in_scope_gap_ids": [
    "GAP-RESERVE",
    "GAP-RETURN"
  ],
  "out_of_scope_gap_ids": [],
  "gap_reasons": [
    "out-of-scope-gaps-not-identified"
  ]
}
```

## 反例与输入不足

- 缺输入：删除控制且无风险处理决定，保留未受控风险。 预期 `uncontrolled-risk`，这是结果中的缺口原因，不是伪装为抛异常。
- 结构反例：规格指向不存在的需求必须拒绝。 预期 `SDN-004`，此项由执行器实际拒绝。

缺输入的预期结果：

```json
{
  "gap_reasons": [
    "uncontrolled-risk"
  ]
}
```

## 评审记录

- 已将本案来源规则与明确的项目约定分开。
- 已核对充分、缺输入、变化及结构反例四类材料的实际结果。
- 已核对缺输入没有被补为通过、零值或真实授权。
- 概念图只解释方案，不能代替可检查的事件规格。
- 需求与规格、风险与控制分别配对，不能把同一条连线当两种证明。
- 退货是明确范围外差距，保留后续工作责任。
- 有控制条目只证明设计已记录；没有运行证据就不能判断重复预占已被消除。

本例已完成编写者一致性复核；业务事实、授权与执行成效均为虚构，独立代理/业务责任人评审仍为待验证。
