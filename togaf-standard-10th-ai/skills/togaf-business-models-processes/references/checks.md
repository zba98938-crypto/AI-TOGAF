# togaf-business-models-processes 检查清单

由注册表显式 `check_specs` 与 `misreadings` 生成；不再按关键词推断断言码。
机器检查由 `field_contracts.run_check(spec, model, work_product)` 执行；适用类型不存在返回not-applicable，不冒充通过。
字段类型检查不证明专业正确性；review/manual保留人工责任，任何结果均不授予批准。

## 机器可判（7 条）

| 对象 | 检查 | 断言码 | 执行器 | 适用条件 |
| --- | --- | --- | --- | --- |
| `customer-journey` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：customer_journey_stage |
| `customer-persona` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：persona |
| `government-reference-tailoring` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：government_service, guide:government_overlay, guide:government_reference_node |
| `digital-business-reference-tailoring` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：dbrm_domain, dbrm_element, guide:dbrm_applicability, guide:dbrm_mapping_row, guide:competency_overlay |
| `four-box-business-model` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：business_model_component |
| `business-model-cube` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：business_model_dimension |
| `operating-model` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：operating_model, guide:operating_submodel |

## 需人工判（28 条）

| 对象 | 检查 | 判定方式 |
| --- | --- | --- |
| `customer-journey` | 客户旅程不是内部流程图，体验陈述需证据 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `customer-journey` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `customer-journey` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `customer-journey` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `customer-persona` | 虚构人物叙述不能冒充真实用户研究结果 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `customer-persona` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `customer-persona` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `customer-persona` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `government-reference-tailoring` | 参考部门分类不是实际组织架构，版本中的部门计数应核对 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `government-reference-tailoring` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `government-reference-tailoring` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `government-reference-tailoring` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `digital-business-reference-tailoring` | 参考模型裁剪不表示全量采用，也不等于最终技术架构 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `digital-business-reference-tailoring` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `digital-business-reference-tailoring` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `digital-business-reference-tailoring` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `four-box-business-model` | 四框不能用九块画布或六维立方体的字段替代，利润公式需要明确变量而非捏造收益 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `four-box-business-model` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `four-box-business-model` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `four-box-business-model` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-model-cube` | 中央Relations表示关系核心而非第七维度；六维没有流程先后或由位置确定的层级 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-model-cube` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-model-cube` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-model-cube` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `operating-model` | 两轴是业务流程而非IT集成与技术标准；四模式无优劣或必经演进顺序 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `operating-model` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `operating-model` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `operating-model` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |

## 常见误读（7 条）

这些是注册表登记过的读图或读模型错误，读产出前先核对。

- `customer-journey`：客户旅程不是内部流程图，体验陈述需证据
- `customer-persona`：虚构人物叙述不能冒充真实用户研究结果
- `government-reference-tailoring`：参考部门分类不是实际组织架构，版本中的部门计数应核对
- `digital-business-reference-tailoring`：参考模型裁剪不表示全量采用，也不等于最终技术架构
- `four-box-business-model`：四框不能用九块画布或六维立方体的字段替代，利润公式需要明确变量而非捏造收益
- `business-model-cube`：中央Relations表示关系核心而非第七维度；六维没有流程先后或由位置确定的层级
- `operating-model`：两轴是业务流程而非IT集成与技术标准；四模式无优劣或必经演进顺序
