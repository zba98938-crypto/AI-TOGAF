# togaf-vision-scenarios 交接说明

由注册表计算：本技能使用的对象类型由谁生产，本技能涉及的类型又被谁使用。
交接只是依赖关系，不代表对方已接受或已完成。

## 入向（本技能需要、由他方生产，8 项）

| 对象类型 | 生产方技能 |
| --- | --- |
| `actor` | togaf-application-architecture, togaf-business-models-processes, togaf-organization-roles, togaf-security-risk, togaf-value-streams |
| `application` | togaf-application-architecture, togaf-gap-solutions, togaf-information-data, togaf-migration-roadmap, togaf-security-risk, togaf-strategy-capabilities, togaf-technology-architecture, togaf-value-streams |
| `capability` | togaf-ea-capability, togaf-gap-solutions, togaf-information-data, togaf-organization-roles, togaf-strategy-capabilities, togaf-value-streams |
| `goal` | togaf-ea-capability, togaf-gap-solutions, togaf-information-data, togaf-requirements, togaf-security-risk, togaf-strategy-capabilities |
| `organization` | togaf-application-architecture, togaf-business-models-processes, togaf-organization-roles, togaf-strategy-capabilities |
| `process` | togaf-application-architecture, togaf-business-models-processes, togaf-gap-solutions, togaf-strategy-capabilities |
| `repository_asset` | togaf-change-value, togaf-ea-capability |
| `technology` | togaf-application-architecture, togaf-technology-architecture |

## 出向（本技能涉及、被他方使用，8 项）

| 对象类型 | 使用方技能 |
| --- | --- |
| `actor` | togaf-application-architecture, togaf-business-models-processes, togaf-organization-roles, togaf-security-risk, togaf-value-streams |
| `application` | togaf-application-architecture, togaf-gap-solutions, togaf-information-data, togaf-migration-roadmap, togaf-security-risk, togaf-strategy-capabilities, togaf-technology-architecture, togaf-value-streams |
| `capability` | togaf-ea-capability, togaf-gap-solutions, togaf-information-data, togaf-organization-roles, togaf-strategy-capabilities, togaf-value-streams |
| `goal` | togaf-ea-capability, togaf-gap-solutions, togaf-information-data, togaf-requirements, togaf-security-risk, togaf-strategy-capabilities |
| `organization` | togaf-application-architecture, togaf-business-models-processes, togaf-organization-roles, togaf-strategy-capabilities |
| `process` | togaf-application-architecture, togaf-business-models-processes, togaf-gap-solutions, togaf-strategy-capabilities |
| `repository_asset` | togaf-change-value, togaf-ea-capability |
| `technology` | togaf-application-architecture, togaf-technology-architecture |

## 交接条件

接收方在读入前须确认：来源定位、五维语境、以及本包 `checks.md` 中标记为「需人工判」的项目已由责任方判定。缺少任一项时按缺口处理，不默认接受。

## 本技能产出的工作产品

| 工作产品 | 关联交付物 | 对象类型 |
| --- | --- | --- |
| `business-scenario-document` | `architecture-vision`, `statement-of-work`, `business-drivers`, `request-for-architecture-work` | `scenario` |
| `scenario-traceability-matrix` | `architecture-vision`, `statement-of-work` | `actor`, `application`, `goal`, `problem`, `process`, `repository_asset`, `stakeholder` |
| `stakeholder-influence-matrix` | `architecture-vision`, `statement-of-work` | `stakeholder` |
| `business-scenario-checklist-record` | `architecture-vision`, `statement-of-work` | `guide:scenario-checklist-stage` |

## 本技能负责的分析方法

| 方法 | 输出工作产品 | 实现状态 |
| --- | --- | --- |
| `scenario-elicitation` | `business-scenario-document` | `specified-awaiting-behavioral-validation` |
| `scenario-traceability-review` | `scenario-traceability-matrix` | `production-calculator-pending-tests` |
| `business-scenario-checklist-review` | `business-scenario-checklist-record` | `calculator-executed-validation-pending` |
