# 预约中断后的风险偏好变化与三类方案

所有业务材料、人员、目标和授权均为明示虚构；执行结果只覆盖下述情景。

方法：`incident-architecture-adjustment-review`。来源：G186 §12.3。
可复用材料：[四类场景JSON](../method-case-materials/incident-architecture-adjustment-review.json)。

## 决策与原始业务资料

40分钟中断后，是否必然选择双活系统，还是需要重审目标、变更与残余风险？

|证据 ID|原始业务材料|
|---|---|
|INCIDENT|事件记录仅确认中断40分钟，根因尚未确认。|
|RISK-DECISION|虚构风险委员会将可接受中断由60分钟调整为15分钟，并规定超出后升级复议。|
|IMPACT|自动切换估算20万元但未演练；取消目标和取消变更分别有业务后果。|

充分输入的精确结构如下；数值与ID来自本案例材料，不从执行结果反推。

```json
{
  "source_ids": [
    "INCIDENT",
    "RISK-DECISION",
    "IMPACT"
  ],
  "incident": {
    "id": "INC-4",
    "description": "预约中断40分钟",
    "occurred_on": "2026-11-01",
    "evidence": [
      "INCIDENT"
    ]
  },
  "objectives": [
    {
      "id": "OBJ-RESERVE",
      "statement": "试点预约可用"
    }
  ],
  "risk_appetite_before": {
    "statement": "接受一次60分钟中断",
    "authority": "虚构风险委员会"
  },
  "risk_appetite_after": {
    "statement": "接受一次15分钟中断",
    "authority": "虚构风险委员会"
  },
  "risk_tolerance": {
    "statement": "超过15分钟即升级复议",
    "authority": "虚构风险委员会"
  },
  "requirement_changes": [
    {
      "id": "RC-RECOVERY",
      "objective_id": "OBJ-RESERVE",
      "change": "恢复目标由60分钟改为15分钟",
      "impact_assessment_ref": "IMPACT-1"
    }
  ],
  "options": [
    {
      "id": "OPT-RECOVER",
      "kind": "change-target",
      "target_change": "自动切换",
      "work": "恢复流程及演练",
      "cost": "虚构估算20万元",
      "certainty_basis": "尚待故障演练验证的方案",
      "residual_vs_appetite": "exceeds",
      "excess_strategy": "评估转移业务损失并保留服务中断残余风险"
    },
    {
      "id": "OPT-CANCEL-GOAL",
      "kind": "cancel-objective",
      "consequence": "取消试点预约可用性目标，改人工受理"
    },
    {
      "id": "OPT-CANCEL-CHANGE",
      "kind": "cancel-change",
      "consequence": "保留原系统并上报与新偏好不符的风险"
    }
  ],
  "decision": {
    "status": "pending"
  }
}
```

## 来源规则与项目规则

1. **来源规则**：G186 §12.3将风险偏好变化作为需求变更处理，同时考虑变更目标、取消目标和取消变更；不能把风险转移当作事件不会再发生。
2. **项目规则**：本案例采用明确的来源ID、结构字段和有界状态；执行器检查可观察契约，业务充分性另由推理审阅说明。
3. **项目规则**：变化场景只改变材料中列出的事实；未变字段不被重新编造，所有批准与实际运行效果均保持未授予。

## 转换与推理

1. 观察到中断不等于知道根因，不能直接宣称双活能解决问题。
2. 偏好变化需形成有目标追溯和影响评估的需求变更。
3. 取消目标是改变业务承诺；取消变更是保留现状，两者不可合并为一个“不做”。
4. 保险转移经济后果不会减少服务中断概率；残余服务风险继续由责任方决定。

## 输出与追溯

下列预期在执行前由业务材料独立编写；实际执行只对这些明确字段作比较。

```json
{
  "appetite_changed": true,
  "decision_state": "pending",
  "gap_reasons": [],
  "option_kinds": [
    "cancel-change",
    "cancel-objective",
    "change-target"
  ]
}
```

三类方案记录完整，但没有授权选择。

机械可复核字段、缺口和引用；业务结论不由计算器输出自动批准。完整输入、预期与实际结果见本轮方法证据目录。

## 修改演练

本次替换的业务字段如下；需按新事实重评。

- `requirement_changes`：[{"id": "RC-RECOVERY", "objective_id": "OBJ-RESERVE", "change": "恢复目标由60分钟改为15分钟", "impact_assessment_ref": "IMPACT-1"}] → []
- `risk_appetite_after.statement`："接受一次15分钟中断" → "接受一次60分钟中断"

委员会撤回偏好调整并保持原口径；不因发生事件就强制认定偏好已变。

变化后需重新执行原方法；原结论只保留到未改变的事实范围。

```json
{
  "appetite_changed": false,
  "decision_state": "pending"
}
```

## 反例与输入不足

- 缺输入：偏好已变而需求变更为空，不能跳到实施方案。 预期 `appetite-change-without-requirement-change`，这是结果中的缺口原因，不是伪装为抛异常。
- 结构反例：需求变更必须指向受影响的已登记目标。 预期 `IAA-003`，此项由执行器实际拒绝。

缺输入的预期结果：

```json
{
  "gap_reasons": [
    "appetite-change-without-requirement-change"
  ]
}
```

## 评审记录

- 已将本案来源规则与明确的项目约定分开。
- 已核对充分、缺输入、变化及结构反例四类材料的实际结果。
- 已核对缺输入没有被补为通过、零值或真实授权。
- 观察到中断不等于知道根因，不能直接宣称双活能解决问题。
- 偏好变化需形成有目标追溯和影响评估的需求变更。
- 取消目标是改变业务承诺；取消变更是保留现状，两者不可合并为一个“不做”。
- 保险转移经济后果不会减少服务中断概率；残余服务风险继续由责任方决定。

本例已完成编写者一致性复核；业务事实、授权与执行成效均为虚构，独立代理/业务责任人评审仍为待验证。
