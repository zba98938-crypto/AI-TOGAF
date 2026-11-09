# togaf-artifact-review 交接说明

由注册表计算：本技能使用的对象类型由谁生产，本技能涉及的类型又被谁使用。
交接只是依赖关系，不代表对方已接受或已完成。

## 入向（本技能需要、由他方生产，0 项）

本技能不依赖他方生产的对象类型。

## 出向（本技能涉及、被他方使用，0 项）

本技能的产出暂未被其他技能引用。

## 交接条件

接收方在读入前须确认：来源定位、五维语境、以及本包 `checks.md` 中标记为「需人工判」的项目已由责任方判定。缺少任一项时按缺口处理，不默认接受。

## 本技能产出的工作产品

| 工作产品 | 关联交付物 | 对象类型 |
| --- | --- | --- |
| `architecture-acceptance-criteria` | `compliance-assessment` | `acceptance_criterion` |
| `sustainability-review-canvas` | `compliance-assessment` | `sustainability_action` |
| `viewpoint-library` | `tailored-architecture-framework`, `architecture-repository` | `guide:viewpoint` |
| `architecture-governance-checklist` | `compliance-assessment`, `architecture-contract`, `implementation-governance-model` | `guide:governance_check` |
| `non-compliance-disposition` | `compliance-assessment`, `change-request`, `architecture-contract` | `guide:noncompliance_disposition` |
| `architecture-description-formality-review` | `architecture-definition-document`, `compliance-assessment`, `tailored-architecture-framework` | `guide:description_review` |
| `project-stage-closure-record` | `statement-of-work`, `compliance-assessment` | `guide:closure_record` |
| `project-deliverable-charter` | `statement-of-work`, `compliance-assessment` | `guide:deliverable_charter` |

## 本技能负责的分析方法

| 方法 | 输出工作产品 | 实现状态 |
| --- | --- | --- |
| `sustainability-option-review` | `sustainability-review-canvas` | `specified-awaiting-behavioral-validation` |
| `architecture-description-formality-review-method` | `architecture-description-formality-review` | `professional-review-with-separate-structural-checks` |
