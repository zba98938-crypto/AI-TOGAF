# togaf-implementation-governance 交接说明

由注册表计算：本技能使用的对象类型由谁生产，本技能涉及的类型又被谁使用。
交接只是依赖关系，不代表对方已接受或已完成。

## 入向（本技能需要、由他方生产，2 项）

| 对象类型 | 生产方技能 |
| --- | --- |
| `environmental_decision` | togaf-change-value |
| `measure` | togaf-change-value, togaf-strategy-capabilities, togaf-technology-architecture |

## 出向（本技能涉及、被他方使用，2 项）

| 对象类型 | 使用方技能 |
| --- | --- |
| `environmental_decision` | togaf-change-value |
| `measure` | togaf-change-value, togaf-strategy-capabilities, togaf-technology-architecture |

## 交接条件

接收方在读入前须确认：来源定位、五维语境、以及本包 `checks.md` 中标记为「需人工判」的项目已由责任方判定。缺少任一项时按缺口处理，不默认接受。

## 本技能产出的工作产品

| 工作产品 | 关联交付物 | 对象类型 |
| --- | --- | --- |
| `security-audit-record` | `compliance-assessment` | `audit_finding` |
| `environmental-decision-log` | `compliance-assessment`, `business-principles` | `environmental_decision` |
| `change-profile-governance-checklist` | `compliance-assessment`, `architecture-contract`, `implementation-migration-plan` | `guide:governance-check` |
| `decision-delegation-register` | `organization-model`, `tailored-architecture-framework`, `compliance-assessment`, `implementation-governance-model` | `guide:delegation_decision` |
| `sustainable-procurement-strategy` | `implementation-migration-plan`, `architecture-contract` | `guide:sustainable_procurement` |
| `cloud-environmental-data-contract` | `architecture-contract`, `architecture-repository` | `guide:cloud_environmental_field` |
| `solution-delivery-notebook` | `architecture-contract`, `compliance-assessment` | `guide:solution-delivery-notebook` |
| `product-constraint-register` | `architecture-contract`, `compliance-assessment` | `guide:product-constraint-register` |

## 本技能负责的分析方法

| 方法 | 输出工作产品 | 实现状态 |
| --- | --- | --- |
| `change-profile-governance-review` | `change-profile-governance-checklist` | `case-executed-awaiting-independent-business-review` |
| `decision-delegation-register-method` | `decision-delegation-register` | `professional-review-with-separate-structural-checks` |
| `solution-delivery-notebook-review` | `solution-delivery-notebook` | `calculator-executed-validation-pending` |
| `product-constraint-conformance-review` | `product-constraint-register` | `calculator-executed-validation-pending` |
