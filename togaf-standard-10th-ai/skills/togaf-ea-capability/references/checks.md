# togaf-ea-capability 检查清单

由注册表显式 `check_specs` 与 `misreadings` 生成；不再按关键词推断断言码。
机器检查由 `field_contracts.run_check(spec, model, work_product)` 执行；适用类型不存在返回not-applicable，不冒充通过。
字段类型检查不证明专业正确性；review/manual保留人工责任，任何结果均不授予批准。

## 机器可判（15 条）

| 对象 | 检查 | 断言码 | 执行器 | 适用条件 |
| --- | --- | --- | --- | --- |
| `architecture-maturity-scorecard` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：maturity_observation, assessment_result |
| `digital-adoption-position` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：adoption_option |
| `digital-readiness-questionnaire` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：readiness_question |
| `digital-readiness-assessment` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：readiness_factor |
| `adoption-factor-progression` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：readiness_factor, assessment_result |
| `ea-service-catalog` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：ea_service, guide:ea_service_context, guide:ea_adm_mapping |
| `ea-value-map` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：ea_value |
| `ea-team-capacity-plan` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：ea_capacity |
| `enterprise-framework-alignment-catalog` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:framework_touchpoint |
| `business-cycle-product-alignment` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:cycle_product |
| `value-realization-assessment` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:value_observation |
| `project-learning-record` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:project_learning |
| `sustainability-capability-assessment` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:sustainability_capability |
| `ea-point-of-view-register` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:ea-point-of-view |
| `dtra-adm-phase-alignment` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:dtra-alignment-summary, guide:dtra-phase-record |

## 需人工判（101 条）

| 对象 | 检查 | 判定方式 |
| --- | --- | --- |
| `architecture-maturity-model` | ACMM 六级九要素是指南示例，不是所有 TOGAF 项目的统一评级 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-maturity-model` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-maturity-model` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-maturity-model` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-maturity-scorecard` | 加权等级与各级达成百分比是互补结果，不能互相替代 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-maturity-scorecard` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-maturity-scorecard` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-maturity-scorecard` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `digital-adoption-position` | ABCD 不是由低到高的优劣或成熟度等级 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `digital-adoption-position` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `digital-adoption-position` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `digital-adoption-position` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `digital-readiness-questionnaire` | 问卷答案不是客观测量值，需说明参与者与共识过程 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `digital-readiness-questionnaire` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `digital-readiness-questionnaire` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `digital-readiness-questionnaire` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `digital-readiness-assessment` | 没有来源或用户规则时不创建统一总分合格线 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `digital-readiness-assessment` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `digital-readiness-assessment` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `digital-readiness-assessment` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `readiness-consequence-analysis` | 背景重复因素列表不表示全连接依赖，后果未自带概率和严重度 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `readiness-consequence-analysis` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `readiness-consequence-analysis` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `readiness-consequence-analysis` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `adoption-factor-progression` | 射线长度和角度不是定量评分，因素层次不等于 ADM 阶段 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `adoption-factor-progression` | 基础、影响、持续三层完整；类型1/2/3不是实施步骤 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `adoption-factor-progression` | 类型2满足基础与影响；类型3还须满足持续因素 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `adoption-factor-progression` | 日期不进入因素递进图；项目分类须以明确评估证据支持 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-service-catalog` | 候选服务不是每个 EA 团队必须提供的服务清单 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-service-catalog` | D有深化说明 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-service-catalog` | P/D前应有已引入历史 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-service-catalog` | 未引入不能误用D | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-service-catalog` | 项目映射不得标为原图逐格复刻 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-service-catalog` | 每条映射有来源与目的 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-service-catalog` | 制定准则和执行评估分开 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-service-catalog` | 未知保持unknown | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-service-catalog` | 不得把项目安排伪称原图精确对应 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-service-catalog` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-service-catalog` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-service-catalog` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-value-map` | 相关性或贡献假设不能直接断言为确定收益因果 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-value-map` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-value-map` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-value-map` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-team-capacity-plan` | 人数不等于可用容量，技能熟练度不等于工时 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-team-capacity-plan` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-team-capacity-plan` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-team-capacity-plan` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `enterprise-framework-alignment-catalog` | 不把框架目录当企业已采用清单 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `enterprise-framework-alignment-catalog` | 承诺深度由证据叙述，不凭空创建评分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `enterprise-framework-alignment-catalog` | 框架重叠不表示包含或优先级，优先级须组织规则 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-cycle-product-alignment` | ADM阶段顺序不决定业务消费时点 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-cycle-product-alignment` | 30天/季度是G186的实践建议，项目日期必须由实际日历确认 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `business-cycle-product-alignment` | 计划早于期限不证明实际已按时交付 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `value-realization-assessment` | G检验实施合规，H检验价值持续性及新变化，不能互相替代 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `value-realization-assessment` | 不同范围、业务量、期间口径须归一化有依据或保持不可比 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `value-realization-assessment` | 没有来源或明确项目规则不得计算ROI、权重或宣称收益归因 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `value-realization-assessment` | 实际未测不能用0代替；计划收益不等于已实现价值 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-learning-record` | 持续Lessons Log与最终Lessons Learned/Report不是同一个状态 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-learning-record` | 参加复盘或提出建议不等于改进已验证 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-learning-record` | 无原计划/实绩不能编造差异；未经验证原因不能写成确定事实 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `sustainability-capability-assessment` | 六维评估不等于七高层功能的一一映射 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `sustainability-capability-assessment` | 源文未给等级/权重/合格线，不能默认ACMM或自造评分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `sustainability-capability-assessment` | 参加宣导或发布政策不能自动证明能力成熟 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-point-of-view-register` | point of view经营不等同于viewpoint library | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-point-of-view-register` | 分发不等于已阅读；重复阅读不重复计人数 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-point-of-view-register` | 读者与后续变更关联不证明因果或价值实现 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-point-of-view-register` | 修订文件版本不覆盖原阅读记录 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-repository-structure` | 关系端点及类型有效 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-repository-structure` | 专用拓扑检查通过 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-repository-structure` | 必要字段可追溯到实际输出 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-landscape-projection` | 关系端点及类型有效 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-landscape-projection` | 专用拓扑检查通过 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-landscape-projection` | 必要字段可追溯到实际输出 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `repository-state-view-tree` | 关系端点及类型有效 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `repository-state-view-tree` | 专用拓扑检查通过 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `repository-state-view-tree` | 必要字段可追溯到实际输出 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `repository-parallel-candidates` | 关系端点及类型有效 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `repository-parallel-candidates` | 专用拓扑检查通过 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `repository-parallel-candidates` | 必要字段可追溯到实际输出 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `capability-project-continuum` | 关系端点及类型有效 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `capability-project-continuum` | 专用拓扑检查通过 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `capability-project-continuum` | 必要字段可追溯到实际输出 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `portfolio-stakeholder-concern-matrix` | 关系端点及类型有效 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `portfolio-stakeholder-concern-matrix` | 专用拓扑检查通过 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `portfolio-stakeholder-concern-matrix` | 必要字段可追溯到实际输出 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `repository-target-baseline-comparison` | 关系端点及类型有效 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `repository-target-baseline-comparison` | 专用拓扑检查通过 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `repository-target-baseline-comparison` | 必要字段可追溯到实际输出 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `dtra-adm-phase-alignment` | 阶段-因素映射来自图6-1同区位置推断，不是原文逐条规定 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `dtra-adm-phase-alignment` | 阶段G治理指实施方法恰当性，不是“治理与合规”因素 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `dtra-adm-phase-alignment` | 评分低于“同意”只触发复核，不是不合格判定 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `acmm-maturity-assessment` | 无显式权重与规则不计算统一总分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `dtra-readiness-method` | 不自造统一总分通过线，采用类型不是成熟度 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-point-of-view-review` | point of view经营不等同于viewpoint library | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-point-of-view-review` | 分发不等于已阅读；重复阅读不重复计人数 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-point-of-view-review` | 读者与后续变更关联不证明因果或价值实现 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `ea-point-of-view-review` | 修订文件版本不覆盖原阅读记录 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `dtra-adm-phase-alignment-review` | 阶段-因素映射来自图6-1同区位置推断，不是原文逐条规定 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `dtra-adm-phase-alignment-review` | 阶段G治理指实施方法恰当性，不是“治理与合规”因素 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `dtra-adm-phase-alignment-review` | 评分低于“同意”只触发复核，不是不合格判定 | `review`：责任方依据证据判断，不得由生成结果替代 |

## 常见误读（52 条）

这些是注册表登记过的读图或读模型错误，读产出前先核对。

- `architecture-maturity-model`：ACMM 六级九要素是指南示例，不是所有 TOGAF 项目的统一评级
- `architecture-maturity-scorecard`：加权等级与各级达成百分比是互补结果，不能互相替代
- `digital-adoption-position`：ABCD 不是由低到高的优劣或成熟度等级
- `digital-readiness-questionnaire`：问卷答案不是客观测量值，需说明参与者与共识过程
- `digital-readiness-assessment`：没有来源或用户规则时不创建统一总分合格线
- `readiness-consequence-analysis`：背景重复因素列表不表示全连接依赖，后果未自带概率和严重度
- `adoption-factor-progression`：把类型1/2/3当成三个实施步骤
- `adoption-factor-progression`：把射线角度长度解释为评分
- `adoption-factor-progression`：尚未满足基础层就声称满足外层
- `adoption-factor-progression`：把示意类型当作企业实际评估结果
- `ea-service-catalog`：候选服务不是每个 EA 团队必须提供的服务清单
- `ea-value-map`：相关性或贡献假设不能直接断言为确定收益因果
- `ea-team-capacity-plan`：人数不等于可用容量，技能熟练度不等于工时
- `enterprise-framework-alignment-catalog`：不把框架目录当企业已采用清单
- `enterprise-framework-alignment-catalog`：承诺深度由证据叙述，不凭空创建评分
- `enterprise-framework-alignment-catalog`：框架重叠不表示包含或优先级，优先级须组织规则
- `business-cycle-product-alignment`：ADM阶段顺序不决定业务消费时点
- `business-cycle-product-alignment`：30天/季度是G186的实践建议，项目日期必须由实际日历确认
- `business-cycle-product-alignment`：计划早于期限不证明实际已按时交付
- `value-realization-assessment`：G检验实施合规，H检验价值持续性及新变化，不能互相替代
- `value-realization-assessment`：不同范围、业务量、期间口径须归一化有依据或保持不可比
- `value-realization-assessment`：没有来源或明确项目规则不得计算ROI、权重或宣称收益归因
- `value-realization-assessment`：实际未测不能用0代替；计划收益不等于已实现价值
- `project-learning-record`：持续Lessons Log与最终Lessons Learned/Report不是同一个状态
- `project-learning-record`：参加复盘或提出建议不等于改进已验证
- `project-learning-record`：无原计划/实绩不能编造差异；未经验证原因不能写成确定事实
- `sustainability-capability-assessment`：六维评估不等于七高层功能的一一映射
- `sustainability-capability-assessment`：源文未给等级/权重/合格线，不能默认ACMM或自造评分
- `sustainability-capability-assessment`：参加宣导或发布政策不能自动证明能力成熟
- `ea-point-of-view-register`：名称、来源表格和成功输出不等于业务结论已核实
- `ea-point-of-view-register`：point of view经营不等同于viewpoint library
- `ea-point-of-view-register`：分发不等于已阅读；重复阅读不重复计人数
- `ea-point-of-view-register`：读者与后续变更关联不证明因果或价值实现
- `ea-point-of-view-register`：修订文件版本不覆盖原阅读记录
- `architecture-repository-structure`：登记来源或成功生成不表示来源等价
- `architecture-repository-structure`：参考示例的固定结构不直接强制所有企业采用
- `architecture-landscape-projection`：登记来源或成功生成不表示来源等价
- `architecture-landscape-projection`：参考示例的固定结构不直接强制所有企业采用
- `repository-state-view-tree`：登记来源或成功生成不表示来源等价
- `repository-state-view-tree`：参考示例的固定结构不直接强制所有企业采用
- `repository-parallel-candidates`：登记来源或成功生成不表示来源等价
- `repository-parallel-candidates`：参考示例的固定结构不直接强制所有企业采用
- `capability-project-continuum`：登记来源或成功生成不表示来源等价
- `capability-project-continuum`：参考示例的固定结构不直接强制所有企业采用
- `portfolio-stakeholder-concern-matrix`：登记来源或成功生成不表示来源等价
- `portfolio-stakeholder-concern-matrix`：参考示例的固定结构不直接强制所有企业采用
- `repository-target-baseline-comparison`：登记来源或成功生成不表示来源等价
- `repository-target-baseline-comparison`：参考示例的固定结构不直接强制所有企业采用
- `dtra-adm-phase-alignment`：名称、来源表格和成功输出不等于业务结论已核实
- `dtra-adm-phase-alignment`：阶段-因素映射来自图6-1同区位置推断，不是原文逐条规定
- `dtra-adm-phase-alignment`：阶段G治理指实施方法恰当性，不是“治理与合规”因素
- `dtra-adm-phase-alignment`：评分低于“同意”只触发复核，不是不合格判定
