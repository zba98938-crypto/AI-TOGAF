# togaf-organization-roles 检查清单

由注册表显式 `check_specs` 与 `misreadings` 生成；不再按关键词推断断言码。
机器检查由 `field_contracts.run_check(spec, model, work_product)` 执行；适用类型不存在返回not-applicable，不冒充通过。
字段类型检查不证明专业正确性；review/manual保留人工责任，任何结果均不授予批准。

## 机器可判（4 条）

| 对象 | 检查 | 断言码 | 执行器 | 适用条件 |
| --- | --- | --- | --- | --- |
| `architecture-skill-matrix` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：skill |
| `architecture-development-plan` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：skill_development |
| `sustainability-education-plan` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:sustainability_learning |
| `architecture-role-catalog` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:architecture-role |

## 需人工判（30 条）

| 对象 | 检查 | 判定方式 |
| --- | --- | --- |
| `architecture-skill-matrix` | G249 四级熟练度不等于组织成熟度，参考等级可以裁剪 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-skill-matrix` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-skill-matrix` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-skill-matrix` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-skill-matrix` | 原文参考目标绑定原始技能与六个角色列；Chief和通用Segment不得伪造列 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-skill-matrix` | 评级必须绑定量表和语义；未评价保留null，非法等级报错 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-skill-matrix` | 项目目标保留任务和裁剪理由；个人观察保留正向行为证据与时点 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-development-plan` | 参加培训不自动提升为专家等级 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-development-plan` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-development-plan` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-development-plan` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-development-plan` | 每项发展行动绑定技能、任务要求和量表，目标与当前证据分开 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-development-plan` | 完成培训不自动提升评级；复评完成须引用实测评价和行为证据 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-development-plan` | 历史证据不覆盖；目标不随观察值变化；未证明高级不自动降为低级 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `sustainability-education-plan` | 不得仅覆盖ICT员工而漏业务及采购 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `sustainability-education-plan` | 重叠人群不重复计覆盖人数 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `sustainability-education-plan` | 课程/认证建议需核实可用性；本指南例子不代表当前认证有效 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `sustainability-education-plan` | 无评分依据不得自行给技能等级 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-role-catalog` | 首席架构师是企业架构师的特例，不是另一个并列层级 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-role-catalog` | KPI中的3/5与（xxx）四分位是来源示例，不是企业目标 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-role-catalog` | 岗位、角色、任务不同；一人可担任多角色 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-role-catalog` | 角色定义不评价任何人员的能力或绩效 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-role-skill-assessment` | 熟练度、团队容量和组织成熟度分开 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-role-skill-assessment` | 技能等级、组织成熟度、Open CA认证与人员容量分别记录 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-role-skill-assessment` | 不由缺少高级证据自动赋低级 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-role-skill-assessment` | 原文目标、项目目标和人员观察不能互相覆盖 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-role-catalog-review` | 首席架构师是企业架构师的特例，不是另一个并列层级 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-role-catalog-review` | KPI中的3/5与（xxx）四分位是来源示例，不是企业目标 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-role-catalog-review` | 岗位、角色、任务不同；一人可担任多角色 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `architecture-role-catalog-review` | 角色定义不评价任何人员的能力或绩效 | `review`：责任方依据证据判断，不得由生成结果替代 |

## 常见误读（11 条）

这些是注册表登记过的读图或读模型错误，读产出前先核对。

- `architecture-skill-matrix`：G249 四级熟练度不等于组织成熟度，参考等级可以裁剪
- `architecture-development-plan`：参加培训不自动提升为专家等级
- `sustainability-education-plan`：不得仅覆盖ICT员工而漏业务及采购
- `sustainability-education-plan`：重叠人群不重复计覆盖人数
- `sustainability-education-plan`：课程/认证建议需核实可用性；本指南例子不代表当前认证有效
- `sustainability-education-plan`：无评分依据不得自行给技能等级
- `architecture-role-catalog`：名称、来源表格和成功输出不等于业务结论已核实
- `architecture-role-catalog`：首席架构师是企业架构师的特例，不是另一个并列层级
- `architecture-role-catalog`：KPI中的3/5与（xxx）四分位是来源示例，不是企业目标
- `architecture-role-catalog`：岗位、角色、任务不同；一人可担任多角色
- `architecture-role-catalog`：角色定义不评价任何人员的能力或绩效
