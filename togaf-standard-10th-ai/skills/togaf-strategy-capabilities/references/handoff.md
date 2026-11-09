# togaf-strategy-capabilities 交接说明

由注册表计算：本技能使用的对象类型由谁生产，本技能涉及的类型又被谁使用。
交接只是依赖关系，不代表对方已接受或已完成。

## 入向（本技能需要、由他方生产，13 项）

| 对象类型 | 生产方技能 |
| --- | --- |
| `application` | togaf-application-architecture, togaf-gap-solutions, togaf-information-data, togaf-migration-roadmap, togaf-security-risk, togaf-technology-architecture, togaf-value-streams, togaf-vision-scenarios |
| `business_service` | togaf-business-models-processes, togaf-information-data |
| `capability` | togaf-ea-capability, togaf-gap-solutions, togaf-information-data, togaf-organization-roles, togaf-value-streams, togaf-vision-scenarios |
| `capability_instance` | togaf-gap-solutions |
| `function` | togaf-application-architecture, togaf-business-models-processes, togaf-information-data |
| `goal` | togaf-ea-capability, togaf-gap-solutions, togaf-information-data, togaf-requirements, togaf-security-risk, togaf-vision-scenarios |
| `information` | togaf-gap-solutions, togaf-information-data, togaf-organization-roles |
| `measure` | togaf-change-value, togaf-implementation-governance, togaf-technology-architecture |
| `organization` | togaf-application-architecture, togaf-business-models-processes, togaf-organization-roles, togaf-vision-scenarios |
| `process` | togaf-application-architecture, togaf-business-models-processes, togaf-gap-solutions, togaf-vision-scenarios |
| `role` | togaf-application-architecture, togaf-business-models-processes, togaf-gap-solutions, togaf-information-data, togaf-organization-roles |
| `value_stage` | togaf-gap-solutions, togaf-value-streams |
| `work_package` | togaf-gap-solutions, togaf-migration-roadmap, togaf-requirements |

## 出向（本技能涉及、被他方使用，13 项）

| 对象类型 | 使用方技能 |
| --- | --- |
| `application` | togaf-application-architecture, togaf-gap-solutions, togaf-information-data, togaf-migration-roadmap, togaf-security-risk, togaf-technology-architecture, togaf-value-streams, togaf-vision-scenarios |
| `business_service` | togaf-business-models-processes, togaf-information-data |
| `capability` | togaf-ea-capability, togaf-gap-solutions, togaf-information-data, togaf-organization-roles, togaf-value-streams, togaf-vision-scenarios |
| `capability_instance` | togaf-gap-solutions |
| `function` | togaf-application-architecture, togaf-business-models-processes, togaf-information-data |
| `goal` | togaf-ea-capability, togaf-gap-solutions, togaf-information-data, togaf-requirements, togaf-security-risk, togaf-vision-scenarios |
| `information` | togaf-gap-solutions, togaf-information-data, togaf-organization-roles |
| `measure` | togaf-change-value, togaf-implementation-governance, togaf-technology-architecture |
| `organization` | togaf-application-architecture, togaf-business-models-processes, togaf-organization-roles, togaf-vision-scenarios |
| `process` | togaf-application-architecture, togaf-business-models-processes, togaf-gap-solutions, togaf-vision-scenarios |
| `role` | togaf-application-architecture, togaf-business-models-processes, togaf-gap-solutions, togaf-information-data, togaf-organization-roles |
| `value_stage` | togaf-gap-solutions, togaf-value-streams |
| `work_package` | togaf-gap-solutions, togaf-migration-roadmap, togaf-requirements |

## 交接条件

接收方在读入前须确认：来源定位、五维语境、以及本包 `checks.md` 中标记为「需人工判」的项目已由责任方判定。缺少任一项时按缺口处理，不默认接受。

## 本技能产出的工作产品

| 工作产品 | 关联交付物 | 对象类型 |
| --- | --- | --- |
| `capability-instance-model` | `capability-assessment`, `architecture-roadmaps` | `application`, `capability`, `capability_instance`, `information`, `process`, `role`, `value_stage` |
| `balanced-scorecard` | `capability-assessment`, `architecture-roadmaps`, `business-goals-objectives` | `goal`, `outcome` |
| `smart-objective-assessment` | `business-goals-objectives` | `guide:goal`, `guide:smart-objective` |

## 本技能负责的分析方法

| 方法 | 输出工作产品 | 实现状态 |
| --- | --- | --- |
| `capability-decomposition-method` | `business-capabilities-catalog` | `specified-awaiting-behavioral-validation` |
| `smart-objective-review` | `smart-objective-assessment` | `calculator-executed-validation-pending` |
