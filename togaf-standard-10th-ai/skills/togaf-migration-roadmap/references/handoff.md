# togaf-migration-roadmap 交接说明

由注册表计算：本技能使用的对象类型由谁生产，本技能涉及的类型又被谁使用。
交接只是依赖关系，不代表对方已接受或已完成。

## 入向（本技能需要、由他方生产，2 项）

| 对象类型 | 生产方技能 |
| --- | --- |
| `application` | togaf-application-architecture, togaf-gap-solutions, togaf-information-data, togaf-security-risk, togaf-strategy-capabilities, togaf-technology-architecture, togaf-value-streams, togaf-vision-scenarios |
| `work_package` | togaf-gap-solutions, togaf-requirements, togaf-strategy-capabilities |

## 出向（本技能涉及、被他方使用，2 项）

| 对象类型 | 使用方技能 |
| --- | --- |
| `application` | togaf-application-architecture, togaf-gap-solutions, togaf-information-data, togaf-security-risk, togaf-strategy-capabilities, togaf-technology-architecture, togaf-value-streams, togaf-vision-scenarios |
| `work_package` | togaf-gap-solutions, togaf-requirements, togaf-strategy-capabilities |

## 交接条件

接收方在读入前须确认：来源定位、五维语境、以及本包 `checks.md` 中标记为「需人工判」的项目已由责任方判定。缺少任一项时按缺口处理，不默认接受。

## 本技能产出的工作产品

| 工作产品 | 关联交付物 | 对象类型 |
| --- | --- | --- |
| `rollback-plan` | `implementation-migration-plan` | `rollback_step` |
| `implementation-factor-catalog` | `implementation-migration-plan`, `capability-assessment` | `guide:implementation_factor` |
| `portfolio-theme-work-package-register` | `architecture-roadmaps`, `implementation-migration-plan` | `guide:portfolio_assignment` |
| `portfolio-estimate-sufficiency-check` | `implementation-migration-plan` | `guide:estimate_check` |
| `project-work-package-authorization` | `statement-of-work`, `implementation-migration-plan` | `guide:project_authorization` |

## 本技能负责的分析方法

| 方法 | 输出工作产品 | 实现状态 |
| --- | --- | --- |
| `dependency-topological-order` | `portfolio-theme-work-package-register` | `executable-with-bounded-tests` |
| `transition-operability-check` | `transition-architecture-model` | `executable-with-bounded-tests` |
| `work-package-prioritization` | `portfolio-estimate-sufficiency-check` | `executable-with-bounded-tests` |
| `benefit-realization-trigger` | `value-realization-assessment` | `executable-with-bounded-tests` |
