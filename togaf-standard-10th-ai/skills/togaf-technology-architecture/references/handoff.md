# togaf-technology-architecture 交接说明

由注册表计算：本技能使用的对象类型由谁生产，本技能涉及的类型又被谁使用。
交接只是依赖关系，不代表对方已接受或已完成。

## 入向（本技能需要、由他方生产，4 项）

| 对象类型 | 生产方技能 |
| --- | --- |
| `application` | togaf-application-architecture, togaf-gap-solutions, togaf-information-data, togaf-migration-roadmap, togaf-security-risk, togaf-strategy-capabilities, togaf-value-streams, togaf-vision-scenarios |
| `location` | togaf-application-architecture |
| `measure` | togaf-change-value, togaf-implementation-governance, togaf-strategy-capabilities |
| `technology` | togaf-application-architecture, togaf-vision-scenarios |

## 出向（本技能涉及、被他方使用，4 项）

| 对象类型 | 使用方技能 |
| --- | --- |
| `application` | togaf-application-architecture, togaf-gap-solutions, togaf-information-data, togaf-migration-roadmap, togaf-security-risk, togaf-strategy-capabilities, togaf-value-streams, togaf-vision-scenarios |
| `location` | togaf-application-architecture |
| `measure` | togaf-change-value, togaf-implementation-governance, togaf-strategy-capabilities |
| `technology` | togaf-application-architecture, togaf-vision-scenarios |

## 交接条件

接收方在读入前须确认：来源定位、五维语境、以及本包 `checks.md` 中标记为「需人工判」的项目已由责任方判定。缺少任一项时按缺口处理，不默认接受。

## 本技能产出的工作产品

| 工作产品 | 关联交付物 | 对象类型 |
| --- | --- | --- |
| `microservice-technical-guidance` | `architecture-definition-document` | `microservice_guideline`, `ops:msa_readiness`, `ops:msa_governance` |
| `interoperability-assessment` | `architecture-definition-document` | `interoperability_issue` |
| `soa-layered-reference` | `architecture-definition-document`, `architecture-building-blocks` | `soa_concern`, `soa_layer` |

## 本技能负责的分析方法

| 方法 | 输出工作产品 | 实现状态 |
| --- | --- | --- |
| `msa-source-deployment-execution-method` | `software-distribution-diagram` | `未声明` |
| `msa-readiness-evidence-method` | `microservice-technical-guidance` | `未声明` |
| `msa-federated-governance-process-method` | `microservice-technical-guidance` | `未声明` |
