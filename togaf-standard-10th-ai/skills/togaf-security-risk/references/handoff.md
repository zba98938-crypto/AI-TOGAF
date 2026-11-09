# togaf-security-risk 交接说明

由注册表计算：本技能使用的对象类型由谁生产，本技能涉及的类型又被谁使用。
交接只是依赖关系，不代表对方已接受或已完成。

## 入向（本技能需要、由他方生产，8 项）

| 对象类型 | 生产方技能 |
| --- | --- |
| `actor` | togaf-application-architecture, togaf-business-models-processes, togaf-organization-roles, togaf-value-streams, togaf-vision-scenarios |
| `application` | togaf-application-architecture, togaf-gap-solutions, togaf-information-data, togaf-migration-roadmap, togaf-strategy-capabilities, togaf-technology-architecture, togaf-value-streams, togaf-vision-scenarios |
| `control` | togaf-business-models-processes |
| `data_component` | togaf-information-data |
| `data_entity` | togaf-application-architecture, togaf-gap-solutions, togaf-information-data |
| `goal` | togaf-ea-capability, togaf-gap-solutions, togaf-information-data, togaf-requirements, togaf-strategy-capabilities, togaf-vision-scenarios |
| `requirement` | togaf-gap-solutions, togaf-information-data, togaf-requirements |
| `risk` | togaf-requirements |

## 出向（本技能涉及、被他方使用，8 项）

| 对象类型 | 使用方技能 |
| --- | --- |
| `actor` | togaf-application-architecture, togaf-business-models-processes, togaf-organization-roles, togaf-value-streams, togaf-vision-scenarios |
| `application` | togaf-application-architecture, togaf-gap-solutions, togaf-information-data, togaf-migration-roadmap, togaf-strategy-capabilities, togaf-technology-architecture, togaf-value-streams, togaf-vision-scenarios |
| `control` | togaf-business-models-processes |
| `data_component` | togaf-information-data |
| `data_entity` | togaf-application-architecture, togaf-gap-solutions, togaf-information-data |
| `goal` | togaf-ea-capability, togaf-gap-solutions, togaf-information-data, togaf-requirements, togaf-strategy-capabilities, togaf-vision-scenarios |
| `requirement` | togaf-gap-solutions, togaf-information-data, togaf-requirements |
| `risk` | togaf-requirements |

## 交接条件

接收方在读入前须确认：来源定位、五维语境、以及本包 `checks.md` 中标记为「需人工判」的项目已由责任方判定。缺少任一项时按缺口处理，不默认接受。

## 本技能产出的工作产品

| 工作产品 | 关联交付物 | 对象类型 |
| --- | --- | --- |
| `risk-appetite` | `architecture-definition-document`, `architecture-requirements-specification` | `risk_appetite` |
| `business-impact-analysis` | `architecture-definition-document`, `architecture-requirements-specification` | `impact_scenario` |
| `security-resource-plan` | `architecture-definition-document`, `architecture-requirements-specification` | `security_resource` |
| `security-blueprint` | `architecture-definition-document`, `architecture-requirements-specification` | `application`, `security_component` |
| `business-attribute-profile` | `architecture-definition-document`, `architecture-requirements-specification` | `business_attribute`, `control_objective`, `goal`, `requirement` |
| `security-policy-architecture` | `architecture-definition-document`, `architecture-requirements-specification`, `architecture-principles` | `security_policy` |
| `security-domain-model` | `architecture-definition-document`, `architecture-requirements-specification` | `application`, `security_domain` |
| `trust-framework` | `architecture-definition-document`, `architecture-requirements-specification` | `goal`, `trust_party` |
| `business-risk-register` | `architecture-definition-document`, `architecture-requirements-specification` | `application`, `control`, `control_objective`, `loss_event`, `risk`, `risk_asset`, `security_requirement`, `threat_event`, `vulnerability` |
| `applicable-legislation-register` | `architecture-definition-document`, `architecture-requirements-specification` | `legal_obligation` |
| `applicable-control-framework-register` | `architecture-definition-document`, `architecture-requirements-specification` | `control_framework` |
| `security-services-catalog` | `architecture-definition-document`, `architecture-requirements-specification` | `security_service` |
| `security-classification-scheme` | `architecture-definition-document`, `architecture-requirements-specification` | `security_classification` |
| `risk-mitigation-plan` | `architecture-definition-document`, `architecture-requirements-specification` | `risk_treatment` |
| `transition-risk-assessment` | `architecture-definition-document`, `architecture-requirements-specification` | `transition_risk` |
| `security-impact-analysis` | `architecture-definition-document`, `architecture-requirements-specification`, `requirements-impact-assessment` | `security_impact` |
| `security-training-plan` | `architecture-definition-document`, `architecture-requirements-specification` | `training_need` |

## 本技能负责的分析方法

| 方法 | 输出工作产品 | 实现状态 |
| --- | --- | --- |
| `business-risk-assessment` | `business-risk-register` | `operational-steps-with-explicit-input-calculator` |
| `business-impact-method` | `business-impact-analysis` | `specified-awaiting-behavioral-validation` |
| `business-attribute-evaluation` | `business-attribute-profile` | `production-calculator-pending-tests` |
