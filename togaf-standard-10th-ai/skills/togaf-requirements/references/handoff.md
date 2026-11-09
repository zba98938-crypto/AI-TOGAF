# togaf-requirements 交接说明

由注册表计算：本技能使用的对象类型由谁生产，本技能涉及的类型又被谁使用。
交接只是依赖关系，不代表对方已接受或已完成。

## 入向（本技能需要、由他方生产，7 项）

| 对象类型 | 生产方技能 |
| --- | --- |
| `abb` | togaf-gap-solutions |
| `goal` | togaf-ea-capability, togaf-gap-solutions, togaf-information-data, togaf-security-risk, togaf-strategy-capabilities, togaf-vision-scenarios |
| `ops:functional_coverage` | togaf-information-data |
| `requirement` | togaf-gap-solutions, togaf-information-data, togaf-security-risk |
| `risk` | togaf-security-risk |
| `sbb` | togaf-gap-solutions |
| `work_package` | togaf-gap-solutions, togaf-migration-roadmap, togaf-strategy-capabilities |

## 出向（本技能涉及、被他方使用，7 项）

| 对象类型 | 使用方技能 |
| --- | --- |
| `abb` | togaf-gap-solutions |
| `goal` | togaf-ea-capability, togaf-gap-solutions, togaf-information-data, togaf-security-risk, togaf-strategy-capabilities, togaf-vision-scenarios |
| `ops:functional_coverage` | togaf-information-data |
| `requirement` | togaf-gap-solutions, togaf-information-data, togaf-security-risk |
| `risk` | togaf-security-risk |
| `sbb` | togaf-gap-solutions |
| `work_package` | togaf-gap-solutions, togaf-migration-roadmap, togaf-strategy-capabilities |

## 交接条件

接收方在读入前须确认：来源定位、五维语境、以及本包 `checks.md` 中标记为「需人工判」的项目已由责任方判定。缺少任一项时按缺口处理，不默认接受。

## 本技能产出的工作产品

| 工作产品 | 关联交付物 | 对象类型 |
| --- | --- | --- |
| `bi-requirements-profile` | `architecture-requirements-specification` | `analytics_requirement`, `guide:bi_requirement_provenance`, `ops:bi_usage`, `ops:functional_coverage` |
| `architecture-backlog` | `architecture-requirements-specification`, `implementation-migration-plan`, `architecture-definition-document` | `guide:backlog_item`, `guide:sprint`, `goal`, `requirement`, `abb`, `sbb`, `guide:mva_scope` |

## 本技能负责的分析方法

| 方法 | 输出工作产品 | 实现状态 |
| --- | --- | --- |
| `architecture-backlog-method` | `architecture-backlog` | `procedural-analysis-with-scoped-checks` |
| `bi-requirement-origin-boundary-method` | `bi-requirements-profile` | `未声明` |
| `architecture-backlog-trace-review` | `architecture-backlog` | `未声明` |
| `bi-usage-goal-measures-method` | `bi-requirements-profile` | `未声明` |
| `bi-business-function-coverage-method` | `bi-requirements-profile` | `未声明` |
| `bi-application-function-coverage-method` | `bi-requirements-profile` | `未声明` |
