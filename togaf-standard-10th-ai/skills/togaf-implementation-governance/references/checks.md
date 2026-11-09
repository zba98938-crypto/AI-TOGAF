# togaf-implementation-governance 检查清单

由注册表显式 `check_specs` 与 `misreadings` 生成；不再按关键词推断断言码。
机器检查由 `field_contracts.run_check(spec, model, work_product)` 执行；适用类型不存在返回not-applicable，不冒充通过。
字段类型检查不证明专业正确性；review/manual保留人工责任，任何结果均不授予批准。

## 机器可判（8 条）

| 对象 | 检查 | 断言码 | 执行器 | 适用条件 |
| --- | --- | --- | --- | --- |
| `security-audit-record` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：audit_finding |
| `environmental-decision-log` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：environmental_decision |
| `change-profile-governance-checklist` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:governance-check |
| `decision-delegation-register` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:delegation_decision, decision_record |
| `sustainable-procurement-strategy` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:sustainable_procurement |
| `cloud-environmental-data-contract` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:cloud_environmental_field |
| `solution-delivery-notebook` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:solution-delivery-notebook |
| `product-constraint-register` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:product-constraint-register |

## 需人工判（47 条）

| 对象 | 检查 | 判定方式 |
| --- | --- | --- |
| `security-audit-record` | 生成审计表不能证明渗透测试或控制运行已经完成 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-audit-record` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-audit-record` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `security-audit-record` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `environmental-decision-log` | 低环境影响方案是否采用仍取决于明确权衡，不能伪造批准 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `environmental-decision-log` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `environmental-decision-log` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `environmental-decision-log` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `change-profile-governance-checklist` | 源表空格不代表通过 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `change-profile-governance-checklist` | 排除建议项需要明确裁剪理由 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `change-profile-governance-checklist` | 通过需要证据，已部署不证明价值已实现 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `change-profile-governance-checklist` | 安全X是源表标签，不是新增ADM阶段 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `decision-delegation-register` | 七名称来自外部方法；权责描述与组织约定一致 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `decision-delegation-register` | 可逆有回滚条件与证据；unknown不当作reversible | `review`：责任方依据证据判断，不得由生成结果替代 |
| `decision-delegation-register` | 不可逆决策有跨相关团队参与安排 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `decision-delegation-register` | 无批准证据只能proposed，不实际执行 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `decision-delegation-register` | 决策影响变化触发复评 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `sustainable-procurement-strategy` | 在岸、租赁、云或认证称号不能自动证明低足迹 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `sustainable-procurement-strategy` | 抵消后的净零不能代替端到端排放透明度 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `sustainable-procurement-strategy` | 不造权重或最低合格分；对外采购须实际授权 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `cloud-environmental-data-contract` | G242提出数据共享模型，不宣称已成为国际标准 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `cloud-environmental-data-contract` | Period允许年/月而若干描述写完整年度，必须逐值声明期间，不自动年化 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `cloud-environmental-data-contract` | 供应方scope标签与消费者组织范围归属不同 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `cloud-environmental-data-contract` | 市场法和地点法不能相加，设备子集不与Scope3总量相加，抵消不抵掉报送原始值 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `cloud-environmental-data-contract` | 复制后存储量不是逻辑原始数据；制造水未知不能记零 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `solution-delivery-notebook` | 规格总追溯到某项需求 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `solution-delivery-notebook` | 控制总追溯到某项风险 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `solution-delivery-notebook` | 架构描述摘要仅供参考，不替代规格 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `solution-delivery-notebook` | 笔记本是交付沟通模板，不代表合同已签署 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `product-constraint-register` | 敏捷对齐落在阶段G；不把ADM各阶段改写成冲刺 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `product-constraint-register` | 产品负责人的局部偏好不能越过企业约束 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `product-constraint-register` | 豁免须有权限方、理由、到期日与证据 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `change-profile-governance-review` | 无通过证据不得标通过 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `change-profile-governance-review` | 空白建议列不表示不适用 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `change-profile-governance-review` | 不计算总分或自动批准 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `decision-delegation-register-method` | 七名称来自外部方法；权责描述与组织约定一致 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `decision-delegation-register-method` | 可逆有回滚条件与证据；unknown不当作reversible | `review`：责任方依据证据判断，不得由生成结果替代 |
| `decision-delegation-register-method` | 不可逆决策有跨相关团队参与安排 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `decision-delegation-register-method` | 无批准证据只能proposed，不实际执行 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `decision-delegation-register-method` | 决策影响变化触发复评 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `solution-delivery-notebook-review` | 规格总追溯到某项需求 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `solution-delivery-notebook-review` | 控制总追溯到某项风险 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `solution-delivery-notebook-review` | 架构描述摘要仅供参考，不替代规格 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `solution-delivery-notebook-review` | 笔记本是交付沟通模板，不代表合同已签署 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `product-constraint-conformance-review` | 敏捷对齐落在阶段G；不把ADM各阶段改写成冲刺 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `product-constraint-conformance-review` | 产品负责人的局部偏好不能越过企业约束 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `product-constraint-conformance-review` | 豁免须有权限方、理由、到期日与证据 | `review`：责任方依据证据判断，不得由生成结果替代 |

## 常见误读（28 条）

这些是注册表登记过的读图或读模型错误，读产出前先核对。

- `security-audit-record`：生成审计表不能证明渗透测试或控制运行已经完成
- `environmental-decision-log`：低环境影响方案是否采用仍取决于明确权衡，不能伪造批准
- `change-profile-governance-checklist`：名称、来源表格和成功输出不等于业务结论已核实
- `change-profile-governance-checklist`：源表空格不代表通过
- `change-profile-governance-checklist`：排除建议项需要明确裁剪理由
- `change-profile-governance-checklist`：通过需要证据，已部署不证明价值已实现
- `change-profile-governance-checklist`：安全X是源表标签，不是新增ADM阶段
- `decision-delegation-register`：七级不是TOGAF成熟度评分
- `decision-delegation-register`：“高授权级”不代表更好
- `decision-delegation-register`：来源转引不等于已核实完整Management3.0规则
- `decision-delegation-register`：用户使用本技能不构成外部业务授权
- `sustainable-procurement-strategy`：在岸、租赁、云或认证称号不能自动证明低足迹
- `sustainable-procurement-strategy`：抵消后的净零不能代替端到端排放透明度
- `sustainable-procurement-strategy`：不造权重或最低合格分；对外采购须实际授权
- `cloud-environmental-data-contract`：G242提出数据共享模型，不宣称已成为国际标准
- `cloud-environmental-data-contract`：Period允许年/月而若干描述写完整年度，必须逐值声明期间，不自动年化
- `cloud-environmental-data-contract`：供应方scope标签与消费者组织范围归属不同
- `cloud-environmental-data-contract`：市场法和地点法不能相加，设备子集不与Scope3总量相加，抵消不抵掉报送原始值
- `cloud-environmental-data-contract`：复制后存储量不是逻辑原始数据；制造水未知不能记零
- `solution-delivery-notebook`：名称、来源表格和成功输出不等于业务结论已核实
- `solution-delivery-notebook`：规格总追溯到某项需求
- `solution-delivery-notebook`：控制总追溯到某项风险
- `solution-delivery-notebook`：架构描述摘要仅供参考，不替代规格
- `solution-delivery-notebook`：笔记本是交付沟通模板，不代表合同已签署
- `product-constraint-register`：名称、来源表格和成功输出不等于业务结论已核实
- `product-constraint-register`：敏捷对齐落在阶段G；不把ADM各阶段改写成冲刺
- `product-constraint-register`：产品负责人的局部偏好不能越过企业约束
- `product-constraint-register`：豁免须有权限方、理由、到期日与证据
