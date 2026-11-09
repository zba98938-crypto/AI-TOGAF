# togaf-information-data 检查清单

由注册表显式 `check_specs` 与 `misreadings` 生成；不再按关键词推断断言码。
机器检查由 `field_contracts.run_check(spec, model, work_product)` 执行；适用类型不存在返回not-applicable，不冒充通过。
字段类型检查不证明专业正确性；review/manual保留人工责任，任何结果均不授予批准。

## 机器可判（17 条）

| 对象 | 检查 | 断言码 | 执行器 | 适用条件 |
| --- | --- | --- | --- | --- |
| `data-quality-assessment` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：data_quality_measure, data_quality_rule |
| `metadata-dictionary` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：metadata_asset |
| `data-usage-documentation` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：data_usage |
| `metadata-policy-documentation` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：metadata_policy |
| `data-issue-register` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：data_issue |
| `business-technical-asset-mapping` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：metadata_asset |
| `metadata-repository-design` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：metadata_repository |
| `metadata-model` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：metadata_asset |
| `metadata-validation-workflow` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：metadata_activity |
| `metadata-integration-model` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：metadata_repository |
| `metadata-ingestion-options` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：metadata_component |
| `metadata-inference-design` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：inference_source |
| `customer-mdm-model` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：master_data, guide:mdm_diagnostic_answer, guide:mdm_plateau, guide:mdm_match_case, ops:functional_coverage |
| `mdm-integration-style` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：master_repository |
| `mdm-exchange-pattern` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：master_exchange |
| `bi-transition-architecture` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：analytics_component, guide:bi_operating_state, ops:bi_value_chain, ops:bi_model_operations |
| `bi-transition-architecture` | 申请退役时，旧用途逐项已验证且退出验收有权威与证据 | `bi-retirement-not-ready` | `bi-retirement` | 模型含类型：guide:bi_operating_state |

## 需人工判（114 条）

| 对象 | 检查 | 判定方式 |
| --- | --- | --- |
| `data-quality-assessment` | 不同质量维度不能无依据地加总成一个精确分数 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `data-quality-assessment` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `data-quality-assessment` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `data-quality-assessment` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-dictionary` | 资产名称相同不保证含义相同，字典不是所有数据值的副本 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-dictionary` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-dictionary` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-dictionary` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `data-usage-documentation` | 存在使用关系不等于已获访问授权 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `data-usage-documentation` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `data-usage-documentation` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `data-usage-documentation` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-policy-documentation` | 政策描述与可执行验证规则需分别标识 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-policy-documentation` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-policy-documentation` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-policy-documentation` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `data-issue-register` | 未经验证的根因只能标为假设 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `data-issue-register` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `data-issue-register` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `data-issue-register` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-technical-asset-mapping` | 概念相近不等于同一资产，关联不是自动实现关系 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-technical-asset-mapping` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-technical-asset-mapping` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-technical-asset-mapping` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-repository-design` | 部署一个存储库不自动建立数据治理 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-repository-design` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-repository-design` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-repository-design` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-model` | 图4-5的参考资产不是每个项目必须全选的模型 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-model` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-model` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-model` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-asset-coverage` | 参考图空格不表示禁止、不存在或无需管理 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-asset-coverage` | 源表每行有一个处置结果；遗漏为未知 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-asset-coverage` | 641八类创建对象需逐类资产或明确裁剪，原定义保留子项 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-asset-coverage` | 659必须区分事件、修改历史、来源、作者；历史存在不证明其余 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-asset-coverage` | 已实现须有逐资产/方面的通过观察，计划不提升为实现 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-asset-coverage` | 重复工具复用稳定ID，不重复计算源功能 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-asset-coverage` | 参考图/产品介绍不构成实施证据，不创建TOGAF分数或合格线 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-asset-coverage` | 不适用须有范围、理由与授权证据；批准状态另记 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-asset-coverage` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-asset-coverage` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-asset-coverage` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-validation-workflow` | 协作式的最终一致性不等于没有治理 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-validation-workflow` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-validation-workflow` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-validation-workflow` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-integration-model` | 集成组织方式与手工推送拉取采集方式是两个独立维度 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-integration-model` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-integration-model` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-integration-model` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-ingestion-options` | 三种机制是备选方案，不是三个固定先后阶段 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-ingestion-options` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-ingestion-options` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-ingestion-options` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-inference-design` | 采集模式不必然需要读取实际业务数据 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-inference-design` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-inference-design` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-inference-design` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `customer-mdm-model` | 统一客户标识不等于无条件合并不同业务语境 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `customer-mdm-model` | 十问各一条且编号不重复 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `customer-mdm-model` | 未知必须有需补证据行动 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `customer-mdm-model` | 不适用必须有范围理由 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `customer-mdm-model` | 无总分/权重/合格线 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `customer-mdm-model` | 两个命名transition保留 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `customer-mdm-model` | 分析黄金态不声称自动双向同步 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `customer-mdm-model` | 每态有主控/CRUD/可运营门槛/恢复 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `customer-mdm-model` | 不覆写历史交易事实 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `customer-mdm-model` | 姓名相同不作为唯一合并依据 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `customer-mdm-model` | merge状态需人工证据及实际谱系 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `customer-mdm-model` | 概率/阈值必须有项目来源 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `customer-mdm-model` | 历史原值与源ID保留 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `customer-mdm-model` | 源表ID全集覆盖且不重复 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `customer-mdm-model` | 已见必须有具体实现/证据，计划不算已实现 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `customer-mdm-model` | 参考表行不是软件组件或独立制品 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `customer-mdm-model` | 保留本地翻译不确定 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `customer-mdm-model` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `customer-mdm-model` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `customer-mdm-model` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `mdm-integration-style` | 参考集成风格不是指定厂商产品 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `mdm-integration-style` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `mdm-integration-style` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `mdm-integration-style` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `mdm-exchange-pattern` | 缩写必须随来源定义，不凭名称猜测语义 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `mdm-exchange-pattern` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `mdm-exchange-pattern` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `mdm-exchange-pattern` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-transition-architecture` | 不同状态是同一架构的演进视图，不机械当成独立制品种类 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-transition-architecture` | step1基线/step2–3过渡/step4目标不混同 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-transition-architecture` | 目标未覆盖旧需求不得退旧仓 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-transition-architecture` | 数据流方向随状态变化要表达 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-transition-architecture` | 无成本/时间依据不估算或强定期限 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-transition-architecture` | 原始层不得修改源内容 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-transition-architecture` | 有向关系和input_refs一致 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-transition-architecture` | 技术规则与业务规则分开 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-transition-architecture` | 每层有质量/保护/血缘责任 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-transition-architecture` | 未知阈值不能判模型通过 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-transition-architecture` | 监测漂移不等于可自动重训投产 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-transition-architecture` | 模型版本与数据/用途可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-transition-architecture` | 监控包含处置责任和回退 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-transition-architecture` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-transition-architecture` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-transition-architecture` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-requirement-method` | 参考资产清单不是强制全选 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-integration-tradeoff` | 组织模型和采集机制不能混为一维 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `mdm-identity-analysis` | 统一客户视图不是无条件合并所有记录 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `bi-transition-method` | 参考目标平台不直接指定厂商 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-application-coverage-review` | 源表每行有一个处置结果；遗漏为未知 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-application-coverage-review` | 641八类创建对象需逐类资产或明确裁剪，原定义保留子项 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-application-coverage-review` | 659必须区分事件、修改历史、来源、作者；历史存在不证明其余 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-application-coverage-review` | 已实现须有逐资产/方面的通过观察，计划不提升为实现 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-application-coverage-review` | 重复工具复用稳定ID，不重复计算源功能 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-application-coverage-review` | 参考图/产品介绍不构成实施证据，不创建TOGAF分数或合格线 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `metadata-application-coverage-review` | 不适用须有范围、理由与授权证据；批准状态另记 | `review`：责任方依据证据判断，不得由生成结果替代 |

## 常见误读（17 条）

这些是注册表登记过的读图或读模型错误，读产出前先核对。

- `data-quality-assessment`：不同质量维度不能无依据地加总成一个精确分数
- `metadata-dictionary`：资产名称相同不保证含义相同，字典不是所有数据值的副本
- `data-usage-documentation`：存在使用关系不等于已获访问授权
- `metadata-policy-documentation`：政策描述与可执行验证规则需分别标识
- `data-issue-register`：未经验证的根因只能标为假设
- `business-technical-asset-mapping`：概念相近不等于同一资产，关联不是自动实现关系
- `metadata-repository-design`：部署一个存储库不自动建立数据治理
- `metadata-model`：图4-5的参考资产不是每个项目必须全选的模型
- `metadata-asset-coverage`：参考图空格不表示禁止、不存在或无需管理
- `metadata-validation-workflow`：协作式的最终一致性不等于没有治理
- `metadata-integration-model`：集成组织方式与手工推送拉取采集方式是两个独立维度
- `metadata-ingestion-options`：三种机制是备选方案，不是三个固定先后阶段
- `metadata-inference-design`：采集模式不必然需要读取实际业务数据
- `customer-mdm-model`：统一客户标识不等于无条件合并不同业务语境
- `mdm-integration-style`：参考集成风格不是指定厂商产品
- `mdm-exchange-pattern`：缩写必须随来源定义，不凭名称猜测语义
- `bi-transition-architecture`：不同状态是同一架构的演进视图，不机械当成独立制品种类
