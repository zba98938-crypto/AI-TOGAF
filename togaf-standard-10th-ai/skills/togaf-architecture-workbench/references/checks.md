# togaf-architecture-workbench 检查清单

由注册表显式 `check_specs` 与 `misreadings` 生成；不再按关键词推断断言码。
机器检查由 `field_contracts.run_check(spec, model, work_product)` 执行；适用类型不存在返回not-applicable，不冒充通过。
字段类型检查不证明专业正确性；review/manual保留人工责任，任何结果均不授予批准。

## 机器可判（5 条）

| 对象 | 检查 | 断言码 | 执行器 | 适用条件 |
| --- | --- | --- | --- | --- |
| `architecture-project-wbs` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：architecture_task |
| `architecture-project-schedule` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：architecture_activity, milestone |
| `project-management-strategy` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:project-management-strategy |
| `project-status-highlight-report` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:project-highlight-report |
| `domain-architecture-alignment` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:domain-architecture, guide:ea-project-scope |

## 需人工判（40 条）

| 对象 | 检查 | 判定方式 |
| --- | --- | --- |
| `architecture-project-wbs` | 架构项目在该指南限 A–F，不代表所有架构工作都限于 A–F | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-project-wbs` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-project-wbs` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-project-wbs` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-project-schedule` | 没有依赖和工期证据不能宣称算出关键路径 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-project-schedule` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-project-schedule` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-project-schedule` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-management-strategy` | 四核心方面来自§3.1.8，配置管理来自§4.2.1 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-management-strategy` | 项目风险与架构愿景/实现风险不混淆 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-management-strategy` | 质量完备不等于已验收 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-management-strategy` | 管理阶段与ADM阶段无需一一对应 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-management-strategy` | 未经批准的变更不得纳入批准基线 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-management-strategy` | 容差和频率是项目约定，不是TOGAF标准阈值 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-status-highlight-report` | 要点报告是按时间驱动的沟通，不替代例外报告 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-status-highlight-report` | 预测/已提交不等于完成验收 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-status-highlight-report` | 上期计划任务不能在下期无解释消失 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-status-highlight-report` | 未批准变更与已批准变更分开 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-status-highlight-report` | 示例一页、三条和每周频率不是通用规则 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-status-highlight-report` | 只有显式项目容差才能判断越界 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `domain-architecture-alignment` | 领域必须融入整体EA，整体EA也须契合领域 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `domain-architecture-alignment` | 安全架构只在参照其他域时存在，按关注点处理 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `domain-architecture-alignment` | 对齐核对不评价领域方案质量 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-project-scheduling` | 不完整依赖不能支持确定关键路径 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `reference-model-tailoring` | 参考分类不是项目实际组织或部署事实 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-management-strategy-review` | 四核心方面来自§3.1.8，配置管理来自§4.2.1 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-management-strategy-review` | 项目风险与架构愿景/实现风险不混淆 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-management-strategy-review` | 质量完备不等于已验收 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-management-strategy-review` | 管理阶段与ADM阶段无需一一对应 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-management-strategy-review` | 未经批准的变更不得纳入批准基线 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-management-strategy-review` | 容差和频率是项目约定，不是TOGAF标准阈值 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-highlight-review` | 要点报告是按时间驱动的沟通，不替代例外报告 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-highlight-review` | 预测/已提交不等于完成验收 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-highlight-review` | 上期计划任务不能在下期无解释消失 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-highlight-review` | 未批准变更与已批准变更分开 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-highlight-review` | 示例一页、三条和每周频率不是通用规则 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-highlight-review` | 只有显式项目容差才能判断越界 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `domain-architecture-alignment-review` | 领域必须融入整体EA，整体EA也须契合领域 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `domain-architecture-alignment-review` | 安全架构只在参照其他域时存在，按关注点处理 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `domain-architecture-alignment-review` | 对齐核对不评价领域方案质量 | `review`：责任方依据证据判断，不得由生成结果替代 |

## 常见误读（20 条）

这些是注册表登记过的读图或读模型错误，读产出前先核对。

- `architecture-project-wbs`：架构项目在该指南限 A–F，不代表所有架构工作都限于 A–F
- `architecture-project-schedule`：没有依赖和工期证据不能宣称算出关键路径
- `project-management-strategy`：名称、来源表格和成功输出不等于业务结论已核实
- `project-management-strategy`：四核心方面来自§3.1.8，配置管理来自§4.2.1
- `project-management-strategy`：项目风险与架构愿景/实现风险不混淆
- `project-management-strategy`：质量完备不等于已验收
- `project-management-strategy`：管理阶段与ADM阶段无需一一对应
- `project-management-strategy`：未经批准的变更不得纳入批准基线
- `project-management-strategy`：容差和频率是项目约定，不是TOGAF标准阈值
- `project-status-highlight-report`：名称、来源表格和成功输出不等于业务结论已核实
- `project-status-highlight-report`：要点报告是按时间驱动的沟通，不替代例外报告
- `project-status-highlight-report`：预测/已提交不等于完成验收
- `project-status-highlight-report`：上期计划任务不能在下期无解释消失
- `project-status-highlight-report`：未批准变更与已批准变更分开
- `project-status-highlight-report`：示例一页、三条和每周频率不是通用规则
- `project-status-highlight-report`：只有显式项目容差才能判断越界
- `domain-architecture-alignment`：名称、来源表格和成功输出不等于业务结论已核实
- `domain-architecture-alignment`：领域必须融入整体EA，整体EA也须契合领域
- `domain-architecture-alignment`：安全架构只在参照其他域时存在，按关注点处理
- `domain-architecture-alignment`：对齐核对不评价领域方案质量
