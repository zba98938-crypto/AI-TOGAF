# togaf-value-streams 交接说明

由注册表计算：本技能使用的对象类型由谁生产，本技能涉及的类型又被谁使用。
交接只是依赖关系，不代表对方已接受或已完成。

## 入向（本技能需要、由他方生产，5 项）

| 对象类型 | 生产方技能 |
| --- | --- |
| `actor` | togaf-application-architecture, togaf-business-models-processes, togaf-organization-roles, togaf-security-risk, togaf-vision-scenarios |
| `application` | togaf-application-architecture, togaf-gap-solutions, togaf-information-data, togaf-migration-roadmap, togaf-security-risk, togaf-strategy-capabilities, togaf-technology-architecture, togaf-vision-scenarios |
| `capability` | togaf-ea-capability, togaf-gap-solutions, togaf-information-data, togaf-organization-roles, togaf-strategy-capabilities, togaf-vision-scenarios |
| `value_stage` | togaf-gap-solutions, togaf-strategy-capabilities |
| `value_stream` | togaf-business-models-processes |

## 出向（本技能涉及、被他方使用，5 项）

| 对象类型 | 使用方技能 |
| --- | --- |
| `actor` | togaf-application-architecture, togaf-business-models-processes, togaf-organization-roles, togaf-security-risk, togaf-vision-scenarios |
| `application` | togaf-application-architecture, togaf-gap-solutions, togaf-information-data, togaf-migration-roadmap, togaf-security-risk, togaf-strategy-capabilities, togaf-technology-architecture, togaf-vision-scenarios |
| `capability` | togaf-ea-capability, togaf-gap-solutions, togaf-information-data, togaf-organization-roles, togaf-strategy-capabilities, togaf-vision-scenarios |
| `value_stage` | togaf-gap-solutions, togaf-strategy-capabilities |
| `value_stream` | togaf-business-models-processes |

## 交接条件

接收方在读入前须确认：来源定位、五维语境、以及本包 `checks.md` 中标记为「需人工判」的项目已由责任方判定。缺少任一项时按缺口处理，不默认接受。

## 本技能产出的工作产品

| 工作产品 | 关联交付物 | 对象类型 |
| --- | --- | --- |
| `value-network` | `architecture-definition-document`, `capability-assessment` | `value_network_actor` |
| `lean-value-stream` | `architecture-definition-document`, `capability-assessment` | `actor`, `application`, `lean_process` |

## 本技能负责的分析方法

| 方法 | 输出工作产品 | 实现状态 |
| --- | --- | --- |
| `value-stream-definition-method` | `value-stream-map` | `specified-awaiting-behavioral-validation` |
