# togaf-change-value 交接说明

由注册表计算：本技能使用的对象类型由谁生产，本技能涉及的类型又被谁使用。
交接只是依赖关系，不代表对方已接受或已完成。

## 入向（本技能需要、由他方生产，3 项）

| 对象类型 | 生产方技能 |
| --- | --- |
| `environmental_decision` | togaf-implementation-governance |
| `measure` | togaf-implementation-governance, togaf-strategy-capabilities, togaf-technology-architecture |
| `repository_asset` | togaf-ea-capability, togaf-vision-scenarios |

## 出向（本技能涉及、被他方使用，3 项）

| 对象类型 | 使用方技能 |
| --- | --- |
| `environmental_decision` | togaf-implementation-governance |
| `measure` | togaf-implementation-governance, togaf-strategy-capabilities, togaf-technology-architecture |
| `repository_asset` | togaf-ea-capability, togaf-vision-scenarios |

## 交接条件

接收方在读入前须确认：来源定位、五维语境、以及本包 `checks.md` 中标记为「需人工判」的项目已由责任方判定。缺少任一项时按缺口处理，不默认接受。

## 本技能产出的工作产品

| 工作产品 | 关联交付物 | 对象类型 |
| --- | --- | --- |
| `environmental-is-assessment` | `change-request`, `capability-assessment` | `environment_measure`, `repository_asset` |
| `environmental-debt-register` | `change-request`, `capability-assessment` | `environmental_debt` |
| `dorp-record` | `change-request`, `compliance-assessment`, `implementation-migration-plan` | `guide:dorp_record` |
| `technical-debt-register` | `change-request`, `architecture-repository`, `implementation-migration-plan` | `guide:technical_debt` |
| `sustainability-dual-entry-analysis` | `implementation-migration-plan`, `architecture-requirements-specification` | `guide:dual_entry_opportunity` |
| `shared-carbon-factor-catalog` | `architecture-repository`, `architecture-definition-document` | `guide:carbon_reference_data` |
| `incident-architecture-adjustment` | `change-request`, `requirements-impact-assessment` | `guide:incident-adjustment` |

## 本技能负责的分析方法

| 方法 | 输出工作产品 | 实现状态 |
| --- | --- | --- |
| `environment-lifecycle-accounting` | `environmental-is-assessment` | `production-calculator-pending-tests` |
| `dorp-record-method` | `dorp-record` | `professional-review-with-separate-structural-checks` |
| `technical-debt-register-method` | `technical-debt-register` | `professional-review-with-separate-structural-checks` |
| `incident-architecture-adjustment-review` | `incident-architecture-adjustment` | `calculator-executed-validation-pending` |
