# togaf-architecture-workbench 交接说明

由注册表计算：本技能使用的对象类型由谁生产，本技能涉及的类型又被谁使用。
交接只是依赖关系，不代表对方已接受或已完成。

## 入向（本技能需要、由他方生产，1 项）

| 对象类型 | 生产方技能 |
| --- | --- |
| `guide:agile_pattern_choice` | togaf-gap-solutions |

## 出向（本技能涉及、被他方使用，1 项）

| 对象类型 | 使用方技能 |
| --- | --- |
| `guide:agile_pattern_choice` | togaf-gap-solutions |

## 交接条件

接收方在读入前须确认：来源定位、五维语境、以及本包 `checks.md` 中标记为「需人工判」的项目已由责任方判定。缺少任一项时按缺口处理，不默认接受。

## 本技能产出的工作产品

| 工作产品 | 关联交付物 | 对象类型 |
| --- | --- | --- |
| `architecture-project-wbs` | `statement-of-work` | `architecture_task` |
| `architecture-project-schedule` | `statement-of-work` | `architecture_activity`, `guide:agile_sprint`, `guide:agile_activity`, `guide:dorp_gate`, `guide:agile_context` |
| `project-management-strategy` | `statement-of-work`, `tailored-architecture-framework` | `guide:project-management-strategy` |
| `project-status-highlight-report` | `statement-of-work`, `communications-plan` | `guide:project-highlight-report` |
| `domain-architecture-alignment` | `architecture-definition-document` | `guide:domain-architecture`, `guide:ea-project-scope` |

## 本技能负责的分析方法

| 方法 | 输出工作产品 | 实现状态 |
| --- | --- | --- |
| `architecture-project-scheduling` | `architecture-project-schedule` | `specified-awaiting-behavioral-validation` |
| `reference-model-tailoring` | `government-reference-tailoring` | `specified-awaiting-behavioral-validation` |
| `project-management-strategy-review` | `project-management-strategy` | `calculator-executed-validation-pending` |
| `project-highlight-review` | `project-status-highlight-report` | `calculator-executed-validation-pending` |
| `agile-collaboration-selection-switch` | `architecture-project-schedule`, `options-decision-matrix` | `未声明` |
| `domain-architecture-alignment-review` | `domain-architecture-alignment` | `calculator-executed-validation-pending` |
