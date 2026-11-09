# togaf-artifact-review 检查清单

由注册表显式 `check_specs` 与 `misreadings` 生成；不再按关键词推断断言码。
机器检查由 `field_contracts.run_check(spec, model, work_product)` 执行；适用类型不存在返回not-applicable，不冒充通过。
字段类型检查不证明专业正确性；review/manual保留人工责任，任何结果均不授予批准。

## 机器可判（8 条）

| 对象 | 检查 | 断言码 | 执行器 | 适用条件 |
| --- | --- | --- | --- | --- |
| `architecture-acceptance-criteria` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：acceptance_criterion |
| `sustainability-review-canvas` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：sustainability_action |
| `viewpoint-library` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:viewpoint |
| `architecture-governance-checklist` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:governance_check |
| `non-compliance-disposition` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:noncompliance_disposition |
| `architecture-description-formality-review` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:description_review |
| `project-stage-closure-record` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:closure_record |
| `project-deliverable-charter` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:deliverable_charter |

## 需人工判（35 条）

| 对象 | 检查 | 判定方式 |
| --- | --- | --- |
| `architecture-acceptance-criteria` | 工件不要求各自成为独立文档，数量不是验收目标 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-acceptance-criteria` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-acceptance-criteria` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-acceptance-criteria` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `sustainability-review-canvas` | 图3-14存在数值疑点，应保留来源值与差异，不能强行消解 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `sustainability-review-canvas` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `sustainability-review-canvas` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `sustainability-review-canvas` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `viewpoint-library` | 视角定义构造规范，view_id标识具体实例，两者不混同 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `viewpoint-library` | 每项授权关注点都有所需信息及构造规则 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `viewpoint-library` | 附录C是空白参考库，填入内容是项目分析而非原指南答案 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-governance-checklist` | 目标九问与实施七问独立；实施第一问为是会直接接受合规 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-governance-checklist` | SME确认事实、审计记录符合性、利益相关者批准目标和处置，不混淆角色 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-governance-checklist` | 只有真实授权证据才能改变批准状态，示例所有状态保持候选 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-governance-checklist` | G184简版与G186详细分支有差异，引用具体版本 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `non-compliance-disposition` | 永久豁免实质改变目标，必须转目标变更 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `non-compliance-disposition` | 更换指标/范围来获得通过会使评估失效 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `non-compliance-disposition` | 建议、批准和落实是三个独立事实 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-description-formality-review` | 充分性与正式度各有独立依据 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-description-formality-review` | 没有来源的等级、数值轴、总分一律不用 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-description-formality-review` | 相对于指定决策而非抽象完整性给结论 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-description-formality-review` | 批准/实现/演进与正式度不同字段 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-description-formality-review` | 修订后复核受影响关注点并保留原判断 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-stage-closure-record` | 阶段产品验收、边界决策、下一阶段授权是不同事实 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-stage-closure-record` | 商业论证失效可以提前终止，不能假装全部产品成功交付 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-stage-closure-record` | 计划/实际偏差不自动证明超过未给出的容差 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-deliverable-charter` | 文档与软件可有不同验收流程，不复制时长为TOGAF要求 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-deliverable-charter` | 生成、移交、评审与接受是不同状态 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-deliverable-charter` | 一项未满足准则不能被其他已满足项的数量抵消 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `sustainability-option-review` | 原图印刷矛盾保留证据，不静默改数 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-description-formality-review-method` | 充分性与正式度各有独立依据 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-description-formality-review-method` | 没有来源的等级、数值轴、总分一律不用 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-description-formality-review-method` | 相对于指定决策而非抽象完整性给结论 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-description-formality-review-method` | 批准/实现/演进与正式度不同字段 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-description-formality-review-method` | 修订后复核受影响关注点并保留原判断 | `review`：责任方依据证据判断，不得由生成结果替代 |

## 常见误读（22 条）

这些是注册表登记过的读图或读模型错误，读产出前先核对。

- `architecture-acceptance-criteria`：工件不要求各自成为独立文档，数量不是验收目标
- `sustainability-review-canvas`：图3-14存在数值疑点，应保留来源值与差异，不能强行消解
- `viewpoint-library`：视角定义构造规范，view_id标识具体实例，两者不混同
- `viewpoint-library`：每项授权关注点都有所需信息及构造规则
- `viewpoint-library`：附录C是空白参考库，填入内容是项目分析而非原指南答案
- `architecture-governance-checklist`：目标九问与实施七问独立；实施第一问为是会直接接受合规
- `architecture-governance-checklist`：SME确认事实、审计记录符合性、利益相关者批准目标和处置，不混淆角色
- `architecture-governance-checklist`：只有真实授权证据才能改变批准状态，示例所有状态保持候选
- `architecture-governance-checklist`：G184简版与G186详细分支有差异，引用具体版本
- `non-compliance-disposition`：永久豁免实质改变目标，必须转目标变更
- `non-compliance-disposition`：更换指标/范围来获得通过会使评估失效
- `non-compliance-disposition`：建议、批准和落实是三个独立事实
- `architecture-description-formality-review`：形式规范不证明内容充分
- `architecture-description-formality-review`：非正式探索不意味着没有架构
- `architecture-description-formality-review`：本表是正文操作化模板，不是已核验图2-1复刻
- `architecture-description-formality-review`：不同用途结论不能直接互换
- `project-stage-closure-record`：阶段产品验收、边界决策、下一阶段授权是不同事实
- `project-stage-closure-record`：商业论证失效可以提前终止，不能假装全部产品成功交付
- `project-stage-closure-record`：计划/实际偏差不自动证明超过未给出的容差
- `project-deliverable-charter`：文档与软件可有不同验收流程，不复制时长为TOGAF要求
- `project-deliverable-charter`：生成、移交、评审与接受是不同状态
- `project-deliverable-charter`：一项未满足准则不能被其他已满足项的数量抵消
