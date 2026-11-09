# togaf-organization-roles 交接说明

由注册表计算：本技能使用的对象类型由谁生产，本技能涉及的类型又被谁使用。
交接只是依赖关系，不代表对方已接受或已完成。

## 入向（本技能需要、由他方生产，5 项）

| 对象类型 | 生产方技能 |
| --- | --- |
| `actor` | togaf-application-architecture, togaf-business-models-processes, togaf-security-risk, togaf-value-streams, togaf-vision-scenarios |
| `capability` | togaf-ea-capability, togaf-gap-solutions, togaf-information-data, togaf-strategy-capabilities, togaf-value-streams, togaf-vision-scenarios |
| `information` | togaf-gap-solutions, togaf-information-data, togaf-strategy-capabilities |
| `organization` | togaf-application-architecture, togaf-business-models-processes, togaf-strategy-capabilities, togaf-vision-scenarios |
| `role` | togaf-application-architecture, togaf-business-models-processes, togaf-gap-solutions, togaf-information-data, togaf-strategy-capabilities |

## 出向（本技能涉及、被他方使用，5 项）

| 对象类型 | 使用方技能 |
| --- | --- |
| `actor` | togaf-application-architecture, togaf-business-models-processes, togaf-security-risk, togaf-value-streams, togaf-vision-scenarios |
| `capability` | togaf-ea-capability, togaf-gap-solutions, togaf-information-data, togaf-strategy-capabilities, togaf-value-streams, togaf-vision-scenarios |
| `information` | togaf-gap-solutions, togaf-information-data, togaf-strategy-capabilities |
| `organization` | togaf-application-architecture, togaf-business-models-processes, togaf-strategy-capabilities, togaf-vision-scenarios |
| `role` | togaf-application-architecture, togaf-business-models-processes, togaf-gap-solutions, togaf-information-data, togaf-strategy-capabilities |

## 交接条件

接收方在读入前须确认：来源定位、五维语境、以及本包 `checks.md` 中标记为「需人工判」的项目已由责任方判定。缺少任一项时按缺口处理，不默认接受。

## 本技能产出的工作产品

| 工作产品 | 关联交付物 | 对象类型 |
| --- | --- | --- |
| `architecture-skill-matrix` | `organization-model` | `skill`, `architecture_role`, `guide:architecture-role` |
| `architecture-development-plan` | `organization-model` | `skill_development` |
| `sustainability-education-plan` | `organization-model`, `capability-assessment` | `guide:sustainability_learning` |
| `architecture-role-catalog` | `organization-model` | `guide:architecture-role` |

## 本技能负责的分析方法

| 方法 | 输出工作产品 | 实现状态 |
| --- | --- | --- |
| `architecture-role-skill-assessment` | `architecture-role-catalog`, `architecture-skill-matrix`, `architecture-development-plan`, `ea-team-capacity-plan` | `deterministic-evidence-review-with-human-judgement-boundaries` |
| `architecture-role-catalog-review` | `architecture-role-catalog` | `calculator-executed-validation-pending` |
