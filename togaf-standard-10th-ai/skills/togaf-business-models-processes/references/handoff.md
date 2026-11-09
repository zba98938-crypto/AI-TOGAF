# togaf-business-models-processes 交接说明

由注册表计算：本技能使用的对象类型由谁生产，本技能涉及的类型又被谁使用。
交接只是依赖关系，不代表对方已接受或已完成。

## 入向（本技能需要、由他方生产，10 项）

| 对象类型 | 生产方技能 |
| --- | --- |
| `activity` | togaf-application-architecture |
| `actor` | togaf-application-architecture, togaf-organization-roles, togaf-security-risk, togaf-value-streams, togaf-vision-scenarios |
| `business_service` | togaf-information-data, togaf-strategy-capabilities |
| `control` | togaf-security-risk |
| `event` | togaf-gap-solutions |
| `function` | togaf-application-architecture, togaf-information-data, togaf-strategy-capabilities |
| `organization` | togaf-application-architecture, togaf-organization-roles, togaf-strategy-capabilities, togaf-vision-scenarios |
| `process` | togaf-application-architecture, togaf-gap-solutions, togaf-strategy-capabilities, togaf-vision-scenarios |
| `role` | togaf-application-architecture, togaf-gap-solutions, togaf-information-data, togaf-organization-roles, togaf-strategy-capabilities |
| `value_stream` | togaf-value-streams |

## 出向（本技能涉及、被他方使用，10 项）

| 对象类型 | 使用方技能 |
| --- | --- |
| `activity` | togaf-application-architecture |
| `actor` | togaf-application-architecture, togaf-organization-roles, togaf-security-risk, togaf-value-streams, togaf-vision-scenarios |
| `business_service` | togaf-information-data, togaf-strategy-capabilities |
| `control` | togaf-security-risk |
| `event` | togaf-gap-solutions |
| `function` | togaf-application-architecture, togaf-information-data, togaf-strategy-capabilities |
| `organization` | togaf-application-architecture, togaf-organization-roles, togaf-strategy-capabilities, togaf-vision-scenarios |
| `process` | togaf-application-architecture, togaf-gap-solutions, togaf-strategy-capabilities, togaf-vision-scenarios |
| `role` | togaf-application-architecture, togaf-gap-solutions, togaf-information-data, togaf-organization-roles, togaf-strategy-capabilities |
| `value_stream` | togaf-value-streams |

## 交接条件

接收方在读入前须确认：来源定位、五维语境、以及本包 `checks.md` 中标记为「需人工判」的项目已由责任方判定。缺少任一项时按缺口处理，不默认接受。

## 本技能产出的工作产品

| 工作产品 | 关联交付物 | 对象类型 |
| --- | --- | --- |
| `customer-journey` | `architecture-definition-document` | `customer_journey_stage`, `journey_stage`, `value_stream` |
| `customer-persona` | `architecture-definition-document` | `persona` |
| `government-reference-tailoring` | `architecture-definition-document` | `government_service`, `guide:government_overlay`, `guide:government_reference_node` |
| `digital-business-reference-tailoring` | `architecture-definition-document` | `dbrm_domain`, `dbrm_element`, `digital_business_function`, `guide:dbrm_applicability`, `guide:dbrm_mapping_row`, `guide:competency_overlay` |
| `four-box-business-model` | `architecture-definition-document` | `business_model_component` |
| `business-model-cube` | `architecture-definition-document` | `business_model_dimension` |
| `operating-model` | `architecture-definition-document` | `operating_model`, `guide:operating_submodel` |

## 本技能负责的分析方法

| 方法 | 输出工作产品 | 实现状态 |
| --- | --- | --- |
| `government-reference-catalog-overlay-method` | `government-reference-tailoring` | `未声明` |
| `dbrm-mapping-suite-method` | `digital-business-reference-tailoring` | `未声明` |
| `digital-enablement-competency-mapping-method` | `digital-business-reference-tailoring` | `未声明` |
| `operating-model-submodel-analysis-method` | `operating-model` | `未声明` |
