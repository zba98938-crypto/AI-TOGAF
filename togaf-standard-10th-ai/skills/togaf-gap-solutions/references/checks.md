# togaf-gap-solutions 检查清单

由注册表显式 `check_specs` 与 `misreadings` 生成；不再按关键词推断断言码。
机器检查由 `field_contracts.run_check(spec, model, work_product)` 执行；适用类型不存在返回not-applicable，不冒充通过。
字段类型检查不证明专业正确性；review/manual保留人工责任，任何结果均不授予批准。

## 机器可判（5 条）

| 对象 | 检查 | 断言码 | 执行器 | 适用条件 |
| --- | --- | --- | --- | --- |
| `options-decision-matrix` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:delivery_feature_review, guide:delivery_style_decision, guide:sbce_iteration, guide:sbce_constraint, option |
| `options-decision-matrix` | 按轮次保留方案身份、淘汰/重开证据及显式所选集合兼容约束；未建模耦合仍需人工评审 | `sbce-contract-violation` | `sbce-contract` | 模型含类型：guide:sbce_iteration, guide:sbce_constraint |
| `capability-increment-analysis` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：capability, capability_instance |
| `building-block-description` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：abb, guide:product_function, guide:product_component, guide:product_interface |
| `transition-architecture-model` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：transition |

## 需人工判（19 条）

| 对象 | 检查 | 判定方式 |
| --- | --- | --- |
| `options-decision-matrix` | 成本原值不能直接当越高越好的评分，权重必须显式 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `options-decision-matrix` | G20F交付风格与SBCE子规范不使用一次性加权评分，按其独立方法执行。 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `options-decision-matrix` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `options-decision-matrix` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `options-decision-matrix` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `capability-increment-analysis` | 绿色不等于已实现或高成熟度，新建改进退役标签与颜色分开记录 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `capability-increment-analysis` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `capability-increment-analysis` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `capability-increment-analysis` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `building-block-description` | ABB不是一个指定技术产品，SBB不能仅按图中的相邻位置推断实现 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `building-block-description` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `building-block-description` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `building-block-description` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `transition-architecture-model` | 过渡架构不是仅有交付日期的里程碑 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `transition-architecture-model` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `transition-architecture-model` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `transition-architecture-model` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `option-weighted-decision` | 成本量不能直接当越高越好的分值 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `capability-instance-gap-method` | 名称相同不等于同一实例 | `review`：责任方依据证据判断，不得由生成结果替代 |

## 常见误读（4 条）

这些是注册表登记过的读图或读模型错误，读产出前先核对。

- `options-decision-matrix`：成本原值不能直接当越高越好的评分，权重必须显式
- `capability-increment-analysis`：绿色不等于已实现或高成熟度，新建改进退役标签与颜色分开记录
- `building-block-description`：ABB不是一个指定技术产品，SBB不能仅按图中的相邻位置推断实现
- `transition-architecture-model`：过渡架构不是仅有交付日期的里程碑
