# togaf-application-architecture 检查清单

由注册表显式 `check_specs` 与 `misreadings` 生成；不再按关键词推断断言码。
机器检查由 `field_contracts.run_check(spec, model, work_product)` 执行；适用类型不存在返回not-applicable，不冒充通过。
字段类型检查不证明专业正确性；review/manual保留人工责任，任何结果均不授予批准。

## 机器可判（2 条）

| 对象 | 检查 | 断言码 | 执行器 | 适用条件 |
| --- | --- | --- | --- | --- |
| `microservice-decomposition-method` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：service_boundary |
| `microservice-value-catalog` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：microservice, ops:msa_value_resource |

## 需人工判（13 条）

| 对象 | 检查 | 判定方式 |
| --- | --- | --- |
| `microservice-decomposition-method` | 小服务数量不是微服务架构成功指标 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `microservice-decomposition-method` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `microservice-decomposition-method` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `microservice-decomposition-method` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `microservice-value-catalog` | 计划服务不能标为已交付，服务数量不等于业务价值 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `microservice-value-catalog` | 四格都存在；unknown不等于0 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `microservice-value-catalog` | 人日与人时不无规则相加 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `microservice-value-catalog` | 未来计划不改为已分配 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `microservice-value-catalog` | 不自创成本率或ROI公式 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `microservice-value-catalog` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `microservice-value-catalog` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `microservice-value-catalog` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `microservice-boundary-method` | 更多更小服务不自动提供价值 | `review`：责任方依据证据判断，不得由生成结果替代 |

## 常见误读（2 条）

这些是注册表登记过的读图或读模型错误，读产出前先核对。

- `microservice-decomposition-method`：小服务数量不是微服务架构成功指标
- `microservice-value-catalog`：计划服务不能标为已交付，服务数量不等于业务价值
