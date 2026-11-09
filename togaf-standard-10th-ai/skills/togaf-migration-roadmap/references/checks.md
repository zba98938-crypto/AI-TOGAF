# togaf-migration-roadmap 检查清单

由注册表显式 `check_specs` 与 `misreadings` 生成；不再按关键词推断断言码。
机器检查由 `field_contracts.run_check(spec, model, work_product)` 执行；适用类型不存在返回not-applicable，不冒充通过。
字段类型检查不证明专业正确性；review/manual保留人工责任，任何结果均不授予批准。

## 机器可判（5 条）

| 对象 | 检查 | 断言码 | 执行器 | 适用条件 |
| --- | --- | --- | --- | --- |
| `rollback-plan` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：rollback_step |
| `implementation-factor-catalog` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:implementation_factor |
| `portfolio-theme-work-package-register` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:portfolio_assignment |
| `portfolio-estimate-sufficiency-check` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:estimate_check |
| `project-work-package-authorization` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:project_authorization, project |

## 需人工判（20 条）

| 对象 | 检查 | 判定方式 |
| --- | --- | --- |
| `rollback-plan` | 回退不是仅写恢复备份，应说明业务与数据恢复条件 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `rollback-plan` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `rollback-plan` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `rollback-plan` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `implementation-factor-catalog` | 只记录具体因素及影响，不默认文化可用分数衡量 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `implementation-factor-catalog` | 访谈说有能力不等于已演练、可用容量或正式承诺 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `portfolio-theme-work-package-register` | 表8-2空格表示架构信息未完整，不用0替代 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `portfolio-theme-work-package-register` | TOGAF变革工作包与PM的WBS叶任务不是同一概念 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `portfolio-theme-work-package-register` | 一个工作包不同时承担保持和改进分类；共享ID不重复预算 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `portfolio-estimate-sufficiency-check` | 第6问“有无担忧”与其他问不是同方向，禁止全是即通过 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `portfolio-estimate-sufficiency-check` | 第10问是数量，不能硬转是/否 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `portfolio-estimate-sufficiency-check` | 8/9为该指南收益递减信号，项目缓冲和公式须明确来源 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `portfolio-estimate-sufficiency-check` | 缺范围可比性或深度分母为零时保留未知 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-work-package-authorization` | 依赖完成不等于已授权，团队空闲不等于允许开始 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-work-package-authorization` | PM工作包与变革工作包分开建模 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `project-work-package-authorization` | 无授权记录不得转为已开始或已完成 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `dependency-topological-order` | 存在环却直接给出顺序，未报告环 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `transition-operability-check` | 只给进度百分比就判定过渡可运营 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `work-package-prioritization` | 权重无来源却直接加权算出总分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `benefit-realization-trigger` | 把计划值当实测值计算偏差 | `review`：责任方依据证据判断，不得由生成结果替代 |

## 常见误读（13 条）

这些是注册表登记过的读图或读模型错误，读产出前先核对。

- `rollback-plan`：回退不是仅写恢复备份，应说明业务与数据恢复条件
- `implementation-factor-catalog`：只记录具体因素及影响，不默认文化可用分数衡量
- `implementation-factor-catalog`：访谈说有能力不等于已演练、可用容量或正式承诺
- `portfolio-theme-work-package-register`：表8-2空格表示架构信息未完整，不用0替代
- `portfolio-theme-work-package-register`：TOGAF变革工作包与PM的WBS叶任务不是同一概念
- `portfolio-theme-work-package-register`：一个工作包不同时承担保持和改进分类；共享ID不重复预算
- `portfolio-estimate-sufficiency-check`：第6问“有无担忧”与其他问不是同方向，禁止全是即通过
- `portfolio-estimate-sufficiency-check`：第10问是数量，不能硬转是/否
- `portfolio-estimate-sufficiency-check`：8/9为该指南收益递减信号，项目缓冲和公式须明确来源
- `portfolio-estimate-sufficiency-check`：缺范围可比性或深度分母为零时保留未知
- `project-work-package-authorization`：依赖完成不等于已授权，团队空闲不等于允许开始
- `project-work-package-authorization`：PM工作包与变革工作包分开建模
- `project-work-package-authorization`：无授权记录不得转为已开始或已完成
