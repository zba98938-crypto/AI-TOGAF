# togaf-change-value 检查清单

由注册表显式 `check_specs` 与 `misreadings` 生成；不再按关键词推断断言码。
机器检查由 `field_contracts.run_check(spec, model, work_product)` 执行；适用类型不存在返回not-applicable，不冒充通过。
字段类型检查不证明专业正确性；review/manual保留人工责任，任何结果均不授予批准。

## 机器可判（7 条）

| 对象 | 检查 | 断言码 | 执行器 | 适用条件 |
| --- | --- | --- | --- | --- |
| `environmental-is-assessment` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：environment_measure, phosphogypsum_record |
| `environmental-debt-register` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：environmental_debt |
| `dorp-record` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:dorp_record |
| `technical-debt-register` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:technical_debt |
| `sustainability-dual-entry-analysis` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:dual_entry_opportunity |
| `shared-carbon-factor-catalog` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:carbon_reference_data |
| `incident-architecture-adjustment` | 必填值存在；已登记类型、枚举与范围约束成立（不验证专业正确性） | `field-contract-value` | `field-values` | 模型含类型：guide:incident-adjustment |

## 需人工判（60 条）

| 对象 | 检查 | 判定方式 |
| --- | --- | --- |
| `environmental-is-assessment` | 抵消单列，不能把不同边界和单位直接相加 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `environmental-is-assessment` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `environmental-is-assessment` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `environmental-is-assessment` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `environmental-is-assessment` | 单位、期间、组织边界和来源齐全 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `environmental-is-assessment` | 市场法/地区法不可相加 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `environmental-is-assessment` | 总Scope3与设备子集不可相加 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `environmental-is-assessment` | 毛排放不扣抵消 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `environmental-is-assessment` | 选择统一组织视角并防重复归属 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `environmental-is-assessment` | 月与年口径不明即阻断自动汇总 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `environmental-is-assessment` | 印刷数与复算数分存，不能自动解释为舍入 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `environmental-is-assessment` | 数据缺失时只能称小计或估计，不能称完整实测 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `environmental-debt-register` | 环境债务不是仅有碳排总量，责任和决策也需记录 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `environmental-debt-register` | 必需属性具有明确值或被登记为阻断缺口 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `environmental-debt-register` | 来源与项目事实、参考内容、假设保持可区分 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `environmental-debt-register` | 结论回应本规范的决策问题并可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `dorp-record` | Demo/Outcome/Retrospective/Planning四项分别存在 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `dorp-record` | 有强制冲刺目标，结论对应同一目标 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `dorp-record` | 完成和未完成集不交叉，未完成集全部回流 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `dorp-record` | 未展示或缺证据的成果不标完成 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `dorp-record` | 后续完成不能倒改原冲刺历史失败 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `technical-debt-register` | 原因、后果、范围和负责人明确 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `technical-debt-register` | EA介入有跨产品或全局理由 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `technical-debt-register` | 偿还与待办可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `technical-debt-register` | 未知成本不填零、不自动算利息 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `technical-debt-register` | 关闭有验证及复核，原始观察保留 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `sustainability-dual-entry-analysis` | 基础设施看似空闲不代表没有业务用途 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `sustainability-dual-entry-analysis` | 共有设备和数据不能按单一用途全部删除 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `sustainability-dual-entry-analysis` | 排序不等于碳量核算；未测量不填虚构减排值 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `sustainability-dual-entry-analysis` | 低技术/人工替代也需同范围全生命周期比较 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `shared-carbon-factor-catalog` | 表3-4非穷尽，不把五类当数量上限 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `shared-carbon-factor-catalog` | kWh/年、kgCO2e/台、kWh/vCPU、kgCO2e/币种、kgCO2e/kWh不可混用 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `shared-carbon-factor-catalog` | 已含PUE不再次乘PUE；单位数据没有实际服务分配则不得视为已验证 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `shared-carbon-factor-catalog` | 共享目录输入核算但本工作产品不产生排放总额 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `incident-architecture-adjustment` | 事件改变风险偏好即需求变更，架构须调整 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `incident-architecture-adjustment` | 超出风险偏好的风险常用转移或规避 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `incident-architecture-adjustment` | 可接受成本的变更可能很少；取消目标或取消变更是正常选项 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `incident-architecture-adjustment` | 不推断事件原因，不代替利益相关者决定 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `environment-lifecycle-accounting` | 单位、期间、组织边界和来源齐全 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `environment-lifecycle-accounting` | 市场法/地区法不可相加 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `environment-lifecycle-accounting` | 总Scope3与设备子集不可相加 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `environment-lifecycle-accounting` | 毛排放不扣抵消 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `environment-lifecycle-accounting` | 选择统一组织视角并防重复归属 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `environment-lifecycle-accounting` | 月与年口径不明即阻断自动汇总 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `environment-lifecycle-accounting` | 印刷数与复算数分存，不能自动解释为舍入 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `environment-lifecycle-accounting` | 数据缺失时只能称小计或估计，不能称完整实测 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `dorp-record-method` | Demo/Outcome/Retrospective/Planning四项分别存在 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `dorp-record-method` | 有强制冲刺目标，结论对应同一目标 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `dorp-record-method` | 完成和未完成集不交叉，未完成集全部回流 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `dorp-record-method` | 未展示或缺证据的成果不标完成 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `dorp-record-method` | 后续完成不能倒改原冲刺历史失败 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `technical-debt-register-method` | 原因、后果、范围和负责人明确 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `technical-debt-register-method` | EA介入有跨产品或全局理由 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `technical-debt-register-method` | 偿还与待办可追溯 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `technical-debt-register-method` | 未知成本不填零、不自动算利息 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `technical-debt-register-method` | 关闭有验证及复核，原始观察保留 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `incident-architecture-adjustment-review` | 事件改变风险偏好即需求变更，架构须调整 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `incident-architecture-adjustment-review` | 超出风险偏好的风险常用转移或规避 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `incident-architecture-adjustment-review` | 可接受成本的变更可能很少；取消目标或取消变更是正常选项 | `review`：责任方依据证据判断，不得由生成结果替代 |
| `incident-architecture-adjustment-review` | 不推断事件原因，不代替利益相关者决定 | `review`：责任方依据证据判断，不得由生成结果替代 |

## 常见误读（26 条）

这些是注册表登记过的读图或读模型错误，读产出前先核对。

- `environmental-is-assessment`：Scope2转移到Scope3并不自动等于减排
- `environmental-is-assessment`：供应商金额比例只是临时近似
- `environmental-is-assessment`：公开书目页和出版时法规不是当前定义与合规证明
- `environmental-is-assessment`：净零电力宣传不能代替全生命周期毛足迹
- `environmental-is-assessment`：第6章是提议模型，非已发布独立标准
- `environmental-debt-register`：环境债务不是仅有碳排总量，责任和决策也需记录
- `dorp-record`：DORP不是只写会议纪要或四个空标题
- `dorp-record`：不能把演示次数代替价值
- `dorp-record`：下次计划是建议，非批准或实际已完成
- `technical-debt-register`：不是所有债务都必须EA处理
- `technical-debt-register`：环境债与技术债不能按名称无条件合并
- `technical-debt-register`：计划偿还不等于已偿还
- `technical-debt-register`：本例关闭门槛是项目规则，不是TOGAF强制公式
- `sustainability-dual-entry-analysis`：基础设施看似空闲不代表没有业务用途
- `sustainability-dual-entry-analysis`：共有设备和数据不能按单一用途全部删除
- `sustainability-dual-entry-analysis`：排序不等于碳量核算；未测量不填虚构减排值
- `sustainability-dual-entry-analysis`：低技术/人工替代也需同范围全生命周期比较
- `shared-carbon-factor-catalog`：表3-4非穷尽，不把五类当数量上限
- `shared-carbon-factor-catalog`：kWh/年、kgCO2e/台、kWh/vCPU、kgCO2e/币种、kgCO2e/kWh不可混用
- `shared-carbon-factor-catalog`：已含PUE不再次乘PUE；单位数据没有实际服务分配则不得视为已验证
- `shared-carbon-factor-catalog`：共享目录输入核算但本工作产品不产生排放总额
- `incident-architecture-adjustment`：名称、来源表格和成功输出不等于业务结论已核实
- `incident-architecture-adjustment`：事件改变风险偏好即需求变更，架构须调整
- `incident-architecture-adjustment`：超出风险偏好的风险常用转移或规避
- `incident-architecture-adjustment`：可接受成本的变更可能很少；取消目标或取消变更是正常选项
- `incident-architecture-adjustment`：不推断事件原因，不代替利益相关者决定
