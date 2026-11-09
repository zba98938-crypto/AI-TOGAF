# 促销待办对库存约束的临时豁免

所有业务材料、人员、目标和授权均为明示虚构；执行结果只覆盖下述情景。

方法：`product-constraint-conformance-review`。来源：G186 §12.1。
可复用材料：[四类场景JSON](../method-case-materials/product-constraint-conformance-review.json)。

## 决策与原始业务资料

产品负责人能否以大促紧急为由绕过库存服务，缺少豁免权限时能否解除冲突阻断？

|证据 ID|原始业务材料|
|---|---|
|ARCH|促销产品只管理资格和价格；企业架构约束库存写入经库存服务，产品偏好不能自行解除约束。|
|DISP|虚构委员会仅对11月预热批次登记临时安排，理由、权限和到期日分别记录。|

充分输入的精确结构如下；数值与ID来自本案例材料，不从执行结果反推。

```json
{
  "source_ids": [
    "ARCH",
    "DISP"
  ],
  "as_of": "2026-11-08",
  "products": [
    {
      "id": "PROMO",
      "name": "促销产品",
      "boundary": "促销资格与价格",
      "product_owner": "虚构产品负责人",
      "architecture_ref": "ARCH-1",
      "evidence": [
        "ARCH"
      ]
    }
  ],
  "constraints": [
    {
      "id": "K-RESERVE",
      "product_id": "PROMO",
      "statement": "库存操作必须经过库存服务",
      "architecture_ref": "ARCH-1",
      "evidence": [
        "ARCH"
      ]
    }
  ],
  "backlog_items": [
    {
      "id": "B-DIRECT",
      "product_id": "PROMO",
      "title": "预热批次绕过库存服务",
      "conflicts_with": [
        "K-RESERVE"
      ],
      "dispensation_id": "D-TEMP"
    }
  ],
  "dispensations": [
    {
      "id": "D-TEMP",
      "constraint_ids": [
        "K-RESERVE"
      ],
      "authority": "虚构架构委员会",
      "rationale": "限11月预热批次，隔离执行并核对库存差额",
      "expiry": "2026-11-30",
      "evidence": [
        "DISP"
      ]
    }
  ]
}
```

## 来源规则与项目规则

1. **来源规则**：G186 §12.1由架构限定产品边界和负责人约束；敏捷实施与ADM在阶段G相接，局部偏好不能越过企业问题。
2. **项目规则**：本案例采用明确的来源ID、结构字段和有界状态；执行器检查可观察契约，业务充分性另由推理审阅说明。
3. **项目规则**：变化场景只改变材料中列出的事实；未变字段不被重新编造，所有批准与实际运行效果均保持未授予。

## 转换与推理

1. 待办与约束归属于同一产品；跨产品豁免不能复用。
2. 豁免是阶段G治理材料，记录完整仍不等于真实组织已授权。
3. 权限方、理由、期限及证据构成同一条记录的必要条件，缺字段不能只靠证据ID解除阻断。
4. 业务变更去掉豁免时，原冲突仍然存在；不能把紧急程度当作授权。

## 输出与追溯

下列预期在执行前由业务材料独立编写；实际执行只对这些明确字段作比较。

```json
{
  "blocked_item_ids": [],
  "finding_states": [
    "dispensation-recorded"
  ],
  "gap_reasons": []
}
```

本情景完整记录临时豁免；效果与真实授权另行审阅。

机械可复核字段、缺口和引用；业务结论不由计算器输出自动批准。完整输入、预期与实际结果见本轮方法证据目录。

## 修改演练

本次替换的业务字段如下；需按新事实重评。

- `dispensations`：[{"id": "D-TEMP", "constraint_ids": ["K-RESERVE"], "authority": "虚构架构委员会", "rationale": "限11月预热批次，隔离执行并核对库存差额", "expiry": "2026-11-30", "evidence": ["DISP"]}] → []

撤销临时豁免后，库存约束继续阻断直接写库待办。

变化后需重新执行原方法；原结论只保留到未改变的事实范围。

```json
{
  "blocked_item_ids": [
    "B-DIRECT"
  ],
  "finding_states": [
    "blocked-local-preference"
  ]
}
```

## 反例与输入不足

- 缺输入：没有权限方的豁免草稿不能解除约束冲突。 预期 `missing-input`，这是结果中的缺口原因，不是伪装为抛异常。
- 结构反例：待办引用不存在的约束应拒绝，不制造空约束。 预期 `PCC-004`，此项由执行器实际拒绝。

缺输入的预期结果：

```json
{
  "blocked_item_ids": [
    "B-DIRECT"
  ],
  "gap_ids": [
    "D-TEMP:authority"
  ]
}
```

## 评审记录

- 已将本案来源规则与明确的项目约定分开。
- 已核对充分、缺输入、变化及结构反例四类材料的实际结果。
- 已核对缺输入没有被补为通过、零值或真实授权。
- 待办与约束归属于同一产品；跨产品豁免不能复用。
- 豁免是阶段G治理材料，记录完整仍不等于真实组织已授权。
- 权限方、理由、期限及证据构成同一条记录的必要条件，缺字段不能只靠证据ID解除阻断。
- 业务变更去掉豁免时，原冲突仍然存在；不能把紧急程度当作授权。

本例已完成编写者一致性复核；业务事实、授权与执行成效均为虚构，独立代理/业务责任人评审仍为待验证。
