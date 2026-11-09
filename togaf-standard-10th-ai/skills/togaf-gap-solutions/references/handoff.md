# togaf-gap-solutions 交接说明

由注册表计算：本技能使用的对象类型由谁生产，本技能涉及的类型又被谁使用。
交接只是依赖关系，不代表对方已接受或已完成。

## 入向（本技能需要、由他方生产，16 项）

| 对象类型 | 生产方技能 |
| --- | --- |
| `abb` | togaf-requirements |
| `application` | togaf-application-architecture, togaf-information-data, togaf-migration-roadmap, togaf-security-risk, togaf-strategy-capabilities, togaf-technology-architecture, togaf-value-streams, togaf-vision-scenarios |
| `capability` | togaf-ea-capability, togaf-information-data, togaf-organization-roles, togaf-strategy-capabilities, togaf-value-streams, togaf-vision-scenarios |
| `capability_instance` | togaf-strategy-capabilities |
| `criterion` | togaf-ea-capability, togaf-information-data |
| `data_entity` | togaf-application-architecture, togaf-information-data, togaf-security-risk |
| `event` | togaf-business-models-processes |
| `goal` | togaf-ea-capability, togaf-information-data, togaf-requirements, togaf-security-risk, togaf-strategy-capabilities, togaf-vision-scenarios |
| `guide:agile_pattern_choice` | togaf-architecture-workbench |
| `information` | togaf-information-data, togaf-organization-roles, togaf-strategy-capabilities |
| `process` | togaf-application-architecture, togaf-business-models-processes, togaf-strategy-capabilities, togaf-vision-scenarios |
| `requirement` | togaf-information-data, togaf-requirements, togaf-security-risk |
| `role` | togaf-application-architecture, togaf-business-models-processes, togaf-information-data, togaf-organization-roles, togaf-strategy-capabilities |
| `sbb` | togaf-requirements |
| `value_stage` | togaf-strategy-capabilities, togaf-value-streams |
| `work_package` | togaf-migration-roadmap, togaf-requirements, togaf-strategy-capabilities |

## 出向（本技能涉及、被他方使用，16 项）

| 对象类型 | 使用方技能 |
| --- | --- |
| `abb` | togaf-requirements |
| `application` | togaf-application-architecture, togaf-information-data, togaf-migration-roadmap, togaf-security-risk, togaf-strategy-capabilities, togaf-technology-architecture, togaf-value-streams, togaf-vision-scenarios |
| `capability` | togaf-ea-capability, togaf-information-data, togaf-organization-roles, togaf-strategy-capabilities, togaf-value-streams, togaf-vision-scenarios |
| `capability_instance` | togaf-strategy-capabilities |
| `criterion` | togaf-ea-capability, togaf-information-data |
| `data_entity` | togaf-application-architecture, togaf-information-data, togaf-security-risk |
| `event` | togaf-business-models-processes |
| `goal` | togaf-ea-capability, togaf-information-data, togaf-requirements, togaf-security-risk, togaf-strategy-capabilities, togaf-vision-scenarios |
| `guide:agile_pattern_choice` | togaf-architecture-workbench |
| `information` | togaf-information-data, togaf-organization-roles, togaf-strategy-capabilities |
| `process` | togaf-application-architecture, togaf-business-models-processes, togaf-strategy-capabilities, togaf-vision-scenarios |
| `requirement` | togaf-information-data, togaf-requirements, togaf-security-risk |
| `role` | togaf-application-architecture, togaf-business-models-processes, togaf-information-data, togaf-organization-roles, togaf-strategy-capabilities |
| `sbb` | togaf-requirements |
| `value_stage` | togaf-strategy-capabilities, togaf-value-streams |
| `work_package` | togaf-migration-roadmap, togaf-requirements, togaf-strategy-capabilities |

## 交接条件

接收方在读入前须确认：来源定位、五维语境、以及本包 `checks.md` 中标记为「需人工判」的项目已由责任方判定。缺少任一项时按缺口处理，不默认接受。

## 本技能产出的工作产品

| 工作产品 | 关联交付物 | 对象类型 |
| --- | --- | --- |
| `options-decision-matrix` | `architecture-roadmaps`, `solution-building-blocks` | `criterion`, `option`, `option_score`, `guide:delivery_feature_review`, `guide:delivery_style_decision`, `guide:sbce_iteration`, `guide:sbce_constraint`, `guide:agile_pattern_choice` |
| `capability-increment-analysis` | `architecture-roadmaps`, `solution-building-blocks` | `application`, `capability`, `capability_change`, `capability_instance`, `information`, `process`, `role`, `value_stage` |
| `building-block-description` | `architecture-roadmaps`, `solution-building-blocks`, `architecture-building-blocks` | `abb`, `goal`, `guide:product_function`, `guide:product_component`, `guide:product_interface`, `sbb`, `requirement` |
| `transition-architecture-model` | `architecture-roadmaps`, `solution-building-blocks` | `transition`, `transition_architecture`, `work_package` |

## 本技能负责的分析方法

| 方法 | 输出工作产品 | 实现状态 |
| --- | --- | --- |
| `option-weighted-decision` | `options-decision-matrix` | `operational-steps-with-explicit-input-calculator` |
| `capability-instance-gap-method` | `capability-increment-analysis` | `specified-awaiting-behavioral-validation` |
| `delivery-style-review` | `options-decision-matrix` | `未声明` |
| `set-based-options-review` | `options-decision-matrix` | `未声明` |
| `product-architecture-allocation-method` | `building-block-description` | `未声明` |
