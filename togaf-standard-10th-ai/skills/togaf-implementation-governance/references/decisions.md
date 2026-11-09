# togaf-implementation-governance 判断规则

本文件是唯一需要人工撰写的部分：机器无法从注册表推出「什么情况选 A 不选 B」。

每条含判据、反例、影响。

## 判断 1：架构合同不得由生成器自动批准

- 判据：`architecture-contract` 的 `approval_status` 只能由有权方人工置位，并须附 `approval_evidence`。生成、渲染、校验通过都不改变批准状态。
- 反例：流水线跑通后自动把合同标为 `approved`，实际无人签署，实施方据此绕过变更控制。
- 影响：`approval_status` 与 `approval_evidence` 字段；`approval-without-evidence` 检查；`compliance-assessment` 的证据链。

## 判断 2：合规偏差必须有裁决人、到期与处置方式

- 判据：`guide:noncompliance_disposition` 必须同时含偏差描述、影响、处置选项、裁决人、到期日与后续动作。缺任一项时该偏差保持未处置。
- 反例：登记「存在偏差，待整改」，无责任人无期限，两年后仍在册。
- 影响：`non-compliance-disposition` 的 13 个字段；`architecture-governance-checklist`；合规报告的完整性。

## 判断 3：治理检查清单是执行工具，不是合规证明

- 判据：清单勾选只证明「检查被执行过」，不证明「架构符合要求」。符合性结论需要证据引用与责任方判断。
- 反例：把 20 项清单全勾上，据此宣布架构合规，但没有任何一项附证据。
- 影响：`architecture-governance-checklist` 的用途边界；`guide:governance_check` 与 `guide:governance-check` 的记录内容；`compliance-assessment` 的结论依据。

## 判断 4：决策授权必须可逆性分级

- 判据：`guide:delegation_decision` 记录授权范围、层级、可逆性与护栏。可逆决策可下放；不可逆决策须上行。
- 反例：把「删除生产数据」这类不可逆决策按「日常运维」下放到班组，护栏里没有双人复核。
- 影响：`decision-delegation-register`；`decision-delegation-register-method`；`guardrails` 与 `authorization_status` 字段。

## 判断 5：云与外包的环境数据须有契约约束

- 判据：`guide:cloud_environmental_field` 与 `cloud-environmental-data-contract` 必须明确供方需提供哪些字段、频次、口径与缺失处理。没有契约时，供方排放数据按未知处理。
- 反例：默认云服务商「一定比自建环保」，但不索取其能耗与排放数据，导致 Scope 3 无法核算。
- 影响：`cloud-environmental-data-contract`；`environment_measure` 的 `scope` 与 `evidence`；`shared-carbon-factor-catalog` 的因子来源。
