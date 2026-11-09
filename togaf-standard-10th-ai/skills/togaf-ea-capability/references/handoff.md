# togaf-ea-capability 交接说明

由注册表计算：本技能使用的对象类型由谁生产，本技能涉及的类型又被谁使用。
交接只是依赖关系，不代表对方已接受或已完成。

## 入向（本技能需要、由他方生产，4 项）

| 对象类型 | 生产方技能 |
| --- | --- |
| `capability` | togaf-gap-solutions, togaf-information-data, togaf-organization-roles, togaf-strategy-capabilities, togaf-value-streams, togaf-vision-scenarios |
| `criterion` | togaf-gap-solutions, togaf-information-data |
| `goal` | togaf-gap-solutions, togaf-information-data, togaf-requirements, togaf-security-risk, togaf-strategy-capabilities, togaf-vision-scenarios |
| `repository_asset` | togaf-change-value, togaf-vision-scenarios |

## 出向（本技能涉及、被他方使用，4 项）

| 对象类型 | 使用方技能 |
| --- | --- |
| `capability` | togaf-gap-solutions, togaf-information-data, togaf-organization-roles, togaf-strategy-capabilities, togaf-value-streams, togaf-vision-scenarios |
| `criterion` | togaf-gap-solutions, togaf-information-data |
| `goal` | togaf-gap-solutions, togaf-information-data, togaf-requirements, togaf-security-risk, togaf-strategy-capabilities, togaf-vision-scenarios |
| `repository_asset` | togaf-change-value, togaf-vision-scenarios |

## 交接条件

接收方在读入前须确认：来源定位、五维语境、以及本包 `checks.md` 中标记为「需人工判」的项目已由责任方判定。缺少任一项时按缺口处理，不默认接受。

## 本技能产出的工作产品

| 工作产品 | 关联交付物 | 对象类型 |
| --- | --- | --- |
| `architecture-maturity-model` | `organization-model`, `tailored-architecture-framework`, `capability-assessment` | `criterion`, `maturity_criterion`, `maturity_element` |
| `architecture-maturity-scorecard` | `organization-model`, `tailored-architecture-framework`, `capability-assessment` | `maturity_observation` |
| `digital-adoption-position` | `organization-model`, `tailored-architecture-framework`, `capability-assessment` | `adoption_option` |
| `digital-readiness-questionnaire` | `organization-model`, `tailored-architecture-framework`, `capability-assessment` | `readiness_question` |
| `digital-readiness-assessment` | `organization-model`, `tailored-architecture-framework`, `capability-assessment` | `readiness_factor` |
| `readiness-consequence-analysis` | `organization-model`, `tailored-architecture-framework`, `capability-assessment` | `consequence`, `readiness_consequence`, `readiness_factor` |
| `adoption-factor-progression` | `organization-model`, `tailored-architecture-framework`, `capability-assessment` | `readiness_factor`, `assessment_result` |
| `ea-service-catalog` | `organization-model`, `tailored-architecture-framework`, `capability-assessment` | `ea_service`, `guide:ea_service_context`, `guide:ea_adm_mapping` |
| `ea-value-map` | `organization-model`, `tailored-architecture-framework`, `capability-assessment` | `ea_value`, `goal` |
| `ea-team-capacity-plan` | `organization-model`, `tailored-architecture-framework`, `capability-assessment` | `ea_capacity` |
| `enterprise-framework-alignment-catalog` | `tailored-architecture-framework`, `organization-model` | `guide:framework_touchpoint` |
| `business-cycle-product-alignment` | `statement-of-work`, `implementation-migration-plan` | `guide:cycle_product` |
| `value-realization-assessment` | `compliance-assessment`, `change-request`, `implementation-migration-plan` | `guide:value_observation` |
| `project-learning-record` | `change-request`, `architecture-repository` | `guide:project_learning` |
| `sustainability-capability-assessment` | `capability-assessment`, `tailored-architecture-framework` | `guide:sustainability_capability` |
| `ea-point-of-view-register` | `organization-model`, `architecture-vision` | `guide:ea-point-of-view` |
| `architecture-repository-structure` | `architecture-repository` | `repository_asset`, `repository_container`, `repository_external`, `repository_partition` |
| `architecture-landscape-projection` | `architecture-definition-document` | `capability`, `landscape_dimension`, `landscape_projection`, `landscape_slice` |
| `repository-state-view-tree` | `architecture-repository` | `g186:repository_node` |
| `repository-parallel-candidates` | `architecture-repository` | `g186:repository_node` |
| `capability-project-continuum` | `architecture-vision` | `g186:continuum`, `g186:continuum_label` |
| `portfolio-stakeholder-concern-matrix` | `communications-plan` | `g186:concern`, `g186:stakeholder` |
| `repository-target-baseline-comparison` | `requirements-impact-assessment`, `architecture-repository` | `g186:comparison_item`, `g186:repository_snapshot` |
| `dtra-adm-phase-alignment` | `capability-assessment`, `architecture-vision` | `guide:dtra-alignment-summary`, `guide:dtra-phase-record` |

## 本技能负责的分析方法

| 方法 | 输出工作产品 | 实现状态 |
| --- | --- | --- |
| `acmm-maturity-assessment` | `architecture-maturity-scorecard` | `operational-steps-with-explicit-input-calculator` |
| `dtra-readiness-method` | `digital-readiness-assessment` | `operational-steps-with-explicit-input-calculator` |
| `ea-service-emergence-npd-method` | `ea-service-catalog` | `未声明` |
| `ea-service-adm-evidence-map-method` | `ea-service-catalog` | `未声明` |
| `ea-point-of-view-review` | `ea-point-of-view-register` | `calculator-executed-validation-pending` |
| `dtra-adm-phase-alignment-review` | `dtra-adm-phase-alignment` | `calculator-executed-validation-pending` |
