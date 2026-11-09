# togaf-information-data 交接说明

由注册表计算：本技能使用的对象类型由谁生产，本技能涉及的类型又被谁使用。
交接只是依赖关系，不代表对方已接受或已完成。

## 入向（本技能需要、由他方生产，12 项）

| 对象类型 | 生产方技能 |
| --- | --- |
| `application` | togaf-application-architecture, togaf-gap-solutions, togaf-migration-roadmap, togaf-security-risk, togaf-strategy-capabilities, togaf-technology-architecture, togaf-value-streams, togaf-vision-scenarios |
| `business_service` | togaf-business-models-processes, togaf-strategy-capabilities |
| `capability` | togaf-ea-capability, togaf-gap-solutions, togaf-organization-roles, togaf-strategy-capabilities, togaf-value-streams, togaf-vision-scenarios |
| `criterion` | togaf-ea-capability, togaf-gap-solutions |
| `data_component` | togaf-security-risk |
| `data_entity` | togaf-application-architecture, togaf-gap-solutions, togaf-security-risk |
| `function` | togaf-application-architecture, togaf-business-models-processes, togaf-strategy-capabilities |
| `goal` | togaf-ea-capability, togaf-gap-solutions, togaf-requirements, togaf-security-risk, togaf-strategy-capabilities, togaf-vision-scenarios |
| `information` | togaf-gap-solutions, togaf-organization-roles, togaf-strategy-capabilities |
| `ops:functional_coverage` | togaf-requirements |
| `requirement` | togaf-gap-solutions, togaf-requirements, togaf-security-risk |
| `role` | togaf-application-architecture, togaf-business-models-processes, togaf-gap-solutions, togaf-organization-roles, togaf-strategy-capabilities |

## 出向（本技能涉及、被他方使用，12 项）

| 对象类型 | 使用方技能 |
| --- | --- |
| `application` | togaf-application-architecture, togaf-gap-solutions, togaf-migration-roadmap, togaf-security-risk, togaf-strategy-capabilities, togaf-technology-architecture, togaf-value-streams, togaf-vision-scenarios |
| `business_service` | togaf-business-models-processes, togaf-strategy-capabilities |
| `capability` | togaf-ea-capability, togaf-gap-solutions, togaf-organization-roles, togaf-strategy-capabilities, togaf-value-streams, togaf-vision-scenarios |
| `criterion` | togaf-ea-capability, togaf-gap-solutions |
| `data_component` | togaf-security-risk |
| `data_entity` | togaf-application-architecture, togaf-gap-solutions, togaf-security-risk |
| `function` | togaf-application-architecture, togaf-business-models-processes, togaf-strategy-capabilities |
| `goal` | togaf-ea-capability, togaf-gap-solutions, togaf-requirements, togaf-security-risk, togaf-strategy-capabilities, togaf-vision-scenarios |
| `information` | togaf-gap-solutions, togaf-organization-roles, togaf-strategy-capabilities |
| `ops:functional_coverage` | togaf-requirements |
| `requirement` | togaf-gap-solutions, togaf-requirements, togaf-security-risk |
| `role` | togaf-application-architecture, togaf-business-models-processes, togaf-gap-solutions, togaf-organization-roles, togaf-strategy-capabilities |

## 交接条件

接收方在读入前须确认：来源定位、五维语境、以及本包 `checks.md` 中标记为「需人工判」的项目已由责任方判定。缺少任一项时按缺口处理，不默认接受。

## 本技能产出的工作产品

| 工作产品 | 关联交付物 | 对象类型 |
| --- | --- | --- |
| `data-quality-assessment` | `architecture-definition-document`, `architecture-requirements-specification` | `data_quality_measure` |
| `metadata-dictionary` | `architecture-definition-document`, `architecture-requirements-specification` | `metadata_asset` |
| `data-usage-documentation` | `architecture-definition-document`, `architecture-requirements-specification` | `data_usage` |
| `metadata-policy-documentation` | `architecture-definition-document`, `architecture-requirements-specification` | `metadata_policy` |
| `data-issue-register` | `architecture-definition-document`, `architecture-requirements-specification` | `data_issue` |
| `business-technical-asset-mapping` | `architecture-definition-document`, `architecture-requirements-specification` | `goal`, `metadata_asset` |
| `metadata-repository-design` | `architecture-definition-document`, `architecture-requirements-specification` | `application`, `metadata_repository` |
| `metadata-model` | `architecture-definition-document`, `architecture-requirements-specification` | `metadata_asset` |
| `metadata-asset-coverage` | `architecture-definition-document`, `architecture-requirements-specification` | `criterion`, `metadata_asset` |
| `metadata-validation-workflow` | `architecture-definition-document`, `architecture-requirements-specification` | `metadata_activity` |
| `metadata-integration-model` | `architecture-definition-document`, `architecture-requirements-specification` | `metadata_repository` |
| `metadata-ingestion-options` | `architecture-definition-document`, `architecture-requirements-specification` | `metadata_component`, `metadata_repository`, `metadata_source` |
| `metadata-inference-design` | `architecture-definition-document`, `architecture-requirements-specification` | `inference_source` |
| `customer-mdm-model` | `architecture-definition-document`, `architecture-requirements-specification` | `master_data`, `guide:mdm_diagnostic_answer`, `guide:mdm_plateau`, `guide:mdm_match_case`, `ops:functional_coverage` |
| `mdm-integration-style` | `architecture-definition-document`, `architecture-requirements-specification` | `master_repository` |
| `mdm-exchange-pattern` | `architecture-definition-document`, `architecture-requirements-specification` | `master_exchange` |
| `bi-transition-architecture` | `architecture-definition-document`, `architecture-requirements-specification` | `analytics_component`, `guide:bi_operating_state`, `ops:bi_value_chain`, `ops:bi_model_operations` |

## 本技能负责的分析方法

| 方法 | 输出工作产品 | 实现状态 |
| --- | --- | --- |
| `metadata-requirement-method` | `metadata-model` | `specified-awaiting-behavioral-validation` |
| `metadata-integration-tradeoff` | `metadata-integration-model` | `specified-awaiting-behavioral-validation` |
| `mdm-identity-analysis` | `customer-mdm-model` | `specified-awaiting-behavioral-validation` |
| `bi-transition-method` | `bi-transition-architecture` | `specified-awaiting-behavioral-validation` |
| `mdm-operational-ten-questions-method` | `customer-mdm-model` | `professional-review-with-separate-structural-checks` |
| `mdm-four-plateau-operations-method` | `customer-mdm-model` | `未声明` |
| `mdm-match-merge-arbitration-method` | `customer-mdm-model` | `professional-review-with-separate-structural-checks` |
| `msa-data-distribution-conditions-method` | `data-dissemination-diagram` | `未声明` |
| `bi-stage-operability-and-exit-method` | `bi-transition-architecture` | `未声明` |
| `mdm-business-function-coverage-method` | `customer-mdm-model` | `procedural-source-row-coverage-review` |
| `mdm-application-function-coverage-method` | `customer-mdm-model` | `procedural-source-row-coverage-review` |
| `bi-value-chain-controls-method` | `bi-transition-architecture` | `未声明` |
| `bi-model-operating-monitoring-method` | `bi-transition-architecture` | `未声明` |
| `metadata-application-coverage-review` | `metadata-asset-coverage` | `calculator-executed-validation-pending` |
