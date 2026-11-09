# 预约项目的应用域与安全关注点对齐

所有业务材料、人员、目标和授权均为明示虚构；执行结果只覆盖下述情景。

方法：`domain-architecture-alignment-review`。来源：G186 §12.2。
可复用材料：[四类场景JSON](../method-case-materials/domain-architecture-alignment-review.json)。

## 决策与原始业务资料

安全方案与应用方案是否服务同一项目，独立文档能否替代共享模型和跨域引用？

|证据 ID|原始业务材料|
|---|---|
|CHARTER|EA-PILOT目标为中央预约和隐私保护，应用域引用共享对象APP-RESERVE。|
|SECURITY|手机号脱敏需求REQ-MASK适用于预约应用DOM-APP，安全作为跨域关注点记录。|

充分输入的精确结构如下；数值与ID来自本案例材料，不从执行结果反推。

```json
{
  "source_ids": [
    "CHARTER",
    "SECURITY"
  ],
  "ea_project": {
    "id": "EA-PILOT",
    "objective_ids": [
      "OBJ-RESERVE",
      "OBJ-PRIVACY"
    ]
  },
  "domains": [
    {
      "id": "DOM-APP",
      "name": "预约应用",
      "kind": "application",
      "project_id": "EA-PILOT",
      "objective_ids": [
        "OBJ-RESERVE"
      ],
      "shared_entity_ids": [
        "APP-RESERVE"
      ],
      "evidence": [
        "CHARTER"
      ]
    },
    {
      "id": "DOM-SEC",
      "name": "预约安全关注",
      "kind": "security",
      "project_id": "EA-PILOT",
      "objective_ids": [
        "OBJ-PRIVACY"
      ],
      "shared_entity_ids": [
        "REQ-MASK"
      ],
      "treated_as": "concern",
      "referenced_domain_ids": [
        "DOM-APP"
      ],
      "evidence": [
        "SECURITY"
      ]
    }
  ]
}
```

## 来源规则与项目规则

1. **来源规则**：G186 §12.2要求领域与整体EA在共同目的和项目语境中相容；安全最好视为引用其他域的关注点。
2. **项目规则**：本案例采用明确的来源ID、结构字段和有界状态；执行器检查可观察契约，业务充分性另由推理审阅说明。
3. **项目规则**：变化场景只改变材料中列出的事实；未变字段不被重新编造，所有批准与实际运行效果均保持未授予。

## 转换与推理

1. 对齐基于项目ID、目的和共享对象，不以文档标题相同为证。
2. 安全关注指向实际受影响的应用域，不能孤立成与整体EA无关的第二项目。
3. 共享引用缺失时只保留待补，不宣称架构质量不合格。
4. 项目切换是业务范围改变，应明确报出separate-project而非沿用原结论。

## 输出与追溯

下列预期在执行前由业务材料独立编写；实际执行只对这些明确字段作比较。

```json
{
  "row_states": [
    "aligned-awaiting-review",
    "aligned-awaiting-review"
  ],
  "gap_reasons": []
}
```

共同项目与目标成立；不评价脱敏方案强度。

机械可复核字段、缺口和引用；业务结论不由计算器输出自动批准。完整输入、预期与实际结果见本轮方法证据目录。

## 修改演练

本次替换的业务字段如下；需按新事实重评。

- `domains[0].project_id`："EA-PILOT" → "EA-OTHER"

应用域转入另一个项目后原整体EA对齐失效。

变化后需重新执行原方法；原结论只保留到未改变的事实范围。

```json
{
  "row_states": [
    "misaligned",
    "aligned-awaiting-review"
  ]
}
```

## 反例与输入不足

- 缺输入：应用域没有共享对象引用，不能仅靠项目名推断已融入共享模型。 预期 `no-shared-model-reference`，这是结果中的缺口原因，不是伪装为抛异常。
- 结构反例：安全引用未登记域时拒绝悬空引用。 预期 `DAA-002`，此项由执行器实际拒绝。

缺输入的预期结果：

```json
{
  "row_states": [
    "needs-input",
    "aligned-awaiting-review"
  ],
  "gap_reasons": [
    "no-shared-model-reference"
  ]
}
```

## 评审记录

- 已将本案来源规则与明确的项目约定分开。
- 已核对充分、缺输入、变化及结构反例四类材料的实际结果。
- 已核对缺输入没有被补为通过、零值或真实授权。
- 对齐基于项目ID、目的和共享对象，不以文档标题相同为证。
- 安全关注指向实际受影响的应用域，不能孤立成与整体EA无关的第二项目。
- 共享引用缺失时只保留待补，不宣称架构质量不合格。
- 项目切换是业务范围改变，应明确报出separate-project而非沿用原结论。

本例已完成编写者一致性复核；业务事实、授权与执行成效均为虚构，独立代理/业务责任人评审仍为待验证。
