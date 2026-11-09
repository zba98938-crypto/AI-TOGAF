# togaf-security-risk 检查清单

由注册表显式 `check_specs` 与 `misreadings` 生成；不再按关键词推断断言码。
机器检查由 `field_contracts.run_check(spec, model, work_product)` 执行；适用类型不存在返回not-applicable，不冒充通过。
字段类型检查不证明专业正确性；review/manual保留人工责任，任何结果均不授予批准。

## 机器可判（17 条）

| 对象 | 检查 | 断言码 | 执行器 | 适用条件 |
| --- | --- | --- | --- | --- |
| `risk-appetite` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：risk_appetite |
| `business-impact-analysis` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：impact_scenario, risk_asset |
| `security-resource-plan` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：security_resource |
| `security-blueprint` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：security_component |
| `business-attribute-profile` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：business_attribute |
| `security-policy-architecture` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：security_policy |
| `security-domain-model` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：security_domain |
| `trust-framework` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：trust_party |
| `business-risk-register` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：risk, threat_event |
| `applicable-legislation-register` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：legal_obligation |
| `applicable-control-framework-register` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：control_framework |
| `security-services-catalog` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：security_service, control_objective |
| `security-classification-scheme` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：security_classification |
| `risk-mitigation-plan` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：risk_treatment |
| `transition-risk-assessment` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：transition_risk |
| `security-impact-analysis` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：security_impact |
| `security-training-plan` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：training_need |

## 需人工判（82 条）

| 对象 | 检查 | 判定方式 |
| --- | --- | --- |
| `risk-appetite` | 风险偏好不是一条任意高低分线，批准状态需要证据 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `risk-appetite` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `risk-appetite` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `risk-appetite` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-impact-analysis` | 业务影响分析不定义事件发生的可能性 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-impact-analysis` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-impact-analysis` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-impact-analysis` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-resource-plan` | 资源计划不等于把所有安全职责交给一位架构师 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-resource-plan` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-resource-plan` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-resource-plan` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-blueprint` | 愿景蓝图不等于已完成的技术方案或已运行控制 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-blueprint` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-blueprint` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-blueprint` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-attribute-profile` | 采用 SABSA 画像作为起点不表示所有参考属性都适用 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-attribute-profile` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-attribute-profile` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-attribute-profile` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-attribute-profile` | 所有指标拥有单位、尺度、时期、数据和计算依据 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-attribute-profile` | 缺目标或容差不可自动判定通过 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-attribute-profile` | 不得将百分比与百分点混用 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-attribute-profile` | 频率和成本字段可以不适用，但必须写理由 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-attribute-profile` | 目标与触发边界显式说明包含/不包含等号 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-attribute-profile` | 保持需求与控制目标的独立身份 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-policy-architecture` | 政策架构不是防火墙规则列表 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-policy-architecture` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-policy-architecture` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-policy-architecture` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-domain-model` | 视觉容器只有经定义后才能表示安全域，组织部门不自动等于安全域 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-domain-model` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-domain-model` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-domain-model` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `trust-framework` | 数字证书可以传递既有信任，不能创造业务信任 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `trust-framework` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `trust-framework` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `trust-framework` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-risk-register` | 业务风险模型和风险登记册是同一工作产品的表达，不重复计数 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-risk-register` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-risk-register` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-risk-register` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `applicable-legislation-register` | 法规适用不能仅由系统部署地推断 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `applicable-legislation-register` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `applicable-legislation-register` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `applicable-legislation-register` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `applicable-control-framework-register` | 历史引用的框架版本不是当前项目自动适用的版本 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `applicable-control-framework-register` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `applicable-control-framework-register` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `applicable-control-framework-register` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-services-catalog` | 控制框架包含要求，安全服务描述实现安全目标的构建块 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-services-catalog` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-services-catalog` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-services-catalog` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-classification-scheme` | 分类适用于业务能力服务信息和技术等多种资产 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-classification-scheme` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-classification-scheme` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-classification-scheme` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `risk-mitigation-plan` | 计划中的控制不能被写成已经有效运行 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `risk-mitigation-plan` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `risk-mitigation-plan` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `risk-mitigation-plan` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `transition-risk-assessment` | 目标架构安全不等于迁移过程安全 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `transition-risk-assessment` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `transition-risk-assessment` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `transition-risk-assessment` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-impact-analysis` | 图可达只是候选影响，不能自动认定所有对象受损 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-impact-analysis` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-impact-analysis` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-impact-analysis` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-training-plan` | 计划中的培训不等于完成或达到熟练度 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-training-plan` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-training-plan` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-training-plan` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-risk-assessment` | 概率未知不能自行代入统一乘法 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-impact-method` | 影响不含事件发生可能性 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-attribute-evaluation` | 所有指标拥有单位、尺度、时期、数据和计算依据 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-attribute-evaluation` | 缺目标或容差不可自动判定通过 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-attribute-evaluation` | 不得将百分比与百分点混用 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-attribute-evaluation` | 频率和成本字段可以不适用，但必须写理由 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-attribute-evaluation` | 目标与触发边界显式说明包含/不包含等号 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-attribute-evaluation` | 保持需求与控制目标的独立身份 | `review`：责任方依据证据判断，不得由生成结果替代 |

## 常见误读（20 条）

这些是注册表登记过的读图或读模型错误，读产出前先核对。

- `risk-appetite`：风险偏好不是一条任意高低分线，批准状态需要证据
- `business-impact-analysis`：业务影响分析不定义事件发生的可能性
- `security-resource-plan`：资源计划不等于把所有安全职责交给一位架构师
- `security-blueprint`：愿景蓝图不等于已完成的技术方案或已运行控制
- `business-attribute-profile`：SABSA属性参考集不是所有项目强制清单
- `business-attribute-profile`：99.5%、0.2个百分点等案例值不是TOGAF阈值
- `business-attribute-profile`：画像的target不是任意措施文字
- `business-attribute-profile`：没有运营数据时不能声称实时仪表板已运行
- `security-policy-architecture`：政策架构不是防火墙规则列表
- `security-domain-model`：视觉容器只有经定义后才能表示安全域，组织部门不自动等于安全域
- `trust-framework`：数字证书可以传递既有信任，不能创造业务信任
- `business-risk-register`：业务风险模型和风险登记册是同一工作产品的表达，不重复计数
- `applicable-legislation-register`：法规适用不能仅由系统部署地推断
- `applicable-control-framework-register`：历史引用的框架版本不是当前项目自动适用的版本
- `security-services-catalog`：控制框架包含要求，安全服务描述实现安全目标的构建块
- `security-classification-scheme`：分类适用于业务能力服务信息和技术等多种资产
- `risk-mitigation-plan`：计划中的控制不能被写成已经有效运行
- `transition-risk-assessment`：目标架构安全不等于迁移过程安全
- `security-impact-analysis`：图可达只是候选影响，不能自动认定所有对象受损
- `security-training-plan`：计划中的培训不等于完成或达到熟练度
