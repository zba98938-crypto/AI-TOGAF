# togaf-ea-capability 判断规则

本文件是唯一需要人工撰写的部分：机器无法从注册表推出「什么情况选 A 不选 B」。

每条含判据、反例、影响。

## 判断 1：成熟度与就绪度是两个问题

- 判据：**架构成熟度**（G203，ACMM 九要素、0–5 级）评价「架构实践本身有多成熟」；**就绪度**（G212，15 因素分基础 7／影响 5／持续 3）评价「某项数字技术在本组织能否被采纳」。前者看能力，后者看条件。
- 反例：因为成熟度评级高就判定新技术可立即采用；成熟度高只说明架构管理有章法，不说明该技术的组织条件具备。
- 影响：`architecture-maturity-scorecard` 与 `digital-readiness-assessment` 的数据来源与结论适用范围；`maturity_criterion` 与 `readiness_question` 两类对象。

## 判断 2：G212 没有官方总分合格线，不得自造阈值

- 判据：G212 建议复核未达到「同意／非常同意」的因素，未规定按总分判断项目能否启动的统一阈值。本项目若要设阈值，必须显式标为项目规则并写明来源。
- 反例：把 15 项打分求和得 62 分，宣称「超过 60 分可以通过」；该 60 分没有任何来源，属于自造标准。
- 影响：`digital-readiness-assessment` 的输出结构；`dtra-readiness-method` 的 `dtra-factor-review` 计算器要求逐因素而非总分；`missing-evidence` 检查。

## 判断 3：视角缺少关注点就不是视角

- 判据：`guide:viewpoint` 必须同时说明「面向哪些利益相关者、回答哪些关注点、需要什么信息、用什么记法」。只有图名与图例不构成视角。
- 反例：目录里写着「数据流图」但没有关注点与所需信息，评审时无法判断该图是否回答了任何人的问题。
- 影响：`viewpoint-library`；`viewpoint-information-gap` 类反例；`stakeholder` / `concern` 的必填性。

## 判断 4：EA 服务清单随组织规模变化，不是固定编制

- 判据：G217 按个人／团队／团队之团队／持久企业四种语境给出由浅到深的架构服务。小团队可用「按需咨询」覆盖，不要求设专职架构部门。
- 反例：把面向持久企业的全套 EA 服务清单直接套到十人团队，结果是流程重于人，服务无人使用。
- 影响：`ea-service-catalog` 的 `consumer`、`service_level`、`adm_phase`；`guide:ea_service_context`；`ea-capability` 相关交付物。

## 判断 5：成熟度评级必须有逐条证据

- 判据：每个 `maturity_criterion` 需要一条 `maturity_observation` 支撑，观察须带证据引用。没有观察的判据不能计分。
- 反例：直接给「内容管理 4 级」，但拿不出任何内容清单、责任人、更新记录的证据。
- 影响：`architecture-maturity-scorecard` 的 `assessment_result`；`acmm-maturity-assessment` 的 `maturity-weighted` 计算器；`missing-evidence` 检查。
