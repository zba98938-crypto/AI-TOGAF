---
name: togaf-ea-capability
description: 建设与评估企业架构能力，生成架构组织、原则、裁剪方法、内容元模型、视点、存储库、EA 服务与成熟度及角色技能评估。
---

# EA 能力与方法

先读取 [专属方法](references/method.md) 和 [共用规则](../_shared/references/modeling-rules.md)，再按请求只读取相关制品或交付物定义。默认中文，保留标准英文名称。

## 工作流程

1. 澄清 EA 服务目的与企业语境。
2. 设计决策权、角色和架构服务。
3. 从实际关注点裁剪元模型与视点。
4. 定义原则及冲突例外机制。
5. 建立有维护责任的资产索引并规划能力提升。

按五维语境建立或修改共享 JSON 模型；使用同一模型派生文字、目录、矩阵和图。关键输入缺失先列缺口，不用虚构事实补齐。

## ADM 与架构成果联动

参与跨阶段任务或阶段评审时，按[阶段到制品工作映射](../_shared/references/architecture-delivery.md)承接Preliminary 阶段的领域工作：从实际利益相关者关注点选择本技能相关视图和方法，关联当前迭代判据及模型输出，生成后核对当前成果。用 `architecture_delivery.py catalog` 查询候选；选择理由、实际分析、生成完整性与真实决定分别保留。单项制品继续按用户指定范围执行。

## 主责制品

- [原则目录 / Principles Catalog](../_shared/references/artifacts/principles-catalog.md)

## 主责交付物

- [架构原则](../_shared/references/deliverables/architecture-principles.md)
- [架构存储库](../_shared/references/deliverables/architecture-repository.md)
- [业务原则](../_shared/references/deliverables/business-principles.md)
- [企业架构组织模型](../_shared/references/deliverables/organization-model.md)
- [裁剪后的架构框架](../_shared/references/deliverables/tailored-architecture-framework.md)

## 生成与验收

按 [覆盖索引](../_shared/references/coverage.md) 获取 ID，运行集合说明中的 validate/generate/render 工具。仅处理用户请求的输出；跨域关系复用对象并咨询相应能力的方法。原则有陈述理由和影响；视点有关注点与构造规则；存储库能找到实际资产及版本；不把组织汇报线当全部治理机制。

输出包括 Markdown 和模型 JSON；图形另附可编辑源、SVG、PNG。报告来源、假设、未决项和验证结果。自动生成或检查不能改变真实批准状态。

## 全量指南能力与多视图

先读取 [全量能力工作流](../_shared/references/workflow-v2.md)。通过 [能力注册](../_shared/capabilities.json) 中的 owner 定位本技能的新增工作产品、视图规范和分析方法，按任务读取对应定义；原清单是兼容入口，不是能力上限。

分析、生成、修改和评审均须依据具体规范执行。一个制品族可以有多个 profile 和实际 view；保留五维语境、来源、假设及多个过渡状态。来源结构布局与业务适配布局共享模型。图形与表格均检查保存输出中的对象、关系、必要属性及 coverage.json 表示位置；存在遗漏或依据不足时交付明确标记的草稿及缺口，不声明已通过对标。核对 manifest.json 的模型、规范、模板与执行依赖指纹，旧输出不自动成为当前版本证据。组装交付物时按[动态组装规则](../_shared/references/deliverable-assembly.md)显式选择视图/分析；章节复制或 legacy-unassembled 不计为组装通过。

涉及 ACMM、DTRA、场景关联或方案评分时，读取 [评价与场景分析手册](../_shared/references/assessment-handbook.md)，按特征证据开展评价；不得用统一总分代替来源方法。

DTRA 因素递进图表达基础、影响、持续三层及类型 1/2/3 就绪情形，使用专门因素分层模板。它不是日期排程；类型 2/3 必须显式满足内层因素。企业实际类型还需问卷与特征证据，示意射线不构成评估结果。

## 任务路由表

本技能注册 37 个视图规范、24 个工作产品。先按决策问题选一行，再读对应规范；不要一次生成全部。

| 决策问题 | 建议规范 | 制品族 |
| --- | --- | --- |
| 怎样逐步补齐采用短板？ | `adoption-factor-progression-default`, `dtra-factor-progression` | `adoption-factor-progression` |
| 依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。 | `architecture-landscape-projection` | `architecture-landscape-projection` |
| 用什么可解释标准评价 EA 能力？ | `architecture-maturity-model-default`, `acmm-elements-levels` | `architecture-maturity-model` |
| 当前 EA 实践达到哪些成熟度特征？ | `architecture-maturity-scorecard-default`, `acmm-scorecard` | `architecture-maturity-scorecard` |
| 依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。 | `architecture-repository-structure` | `architecture-repository-structure` |
| 架构工作产品何时必须可用以影响业务决定？ | `business-cycle-product-alignment-default` | `business-cycle-product-alignment` |
| 依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。 | `capability-project-continuum` | `capability-project-continuum` |
| 选择怎样的数字技术采用方式？ | `digital-adoption-position-default`, `dtra-adoption-quadrant` | `digital-adoption-position` |
| 哪些采用因素需要管理关注？ | `digital-readiness-assessment-default` | `digital-readiness-assessment` |
| 如何取得可比较的就绪度观察？ | `digital-readiness-questionnaire-default` | `digital-readiness-questionnaire` |
| DTRA结果在每个ADM阶段意味着什么，各阶段考虑了哪些因素，低分因素如何处理？ | `dtra-adm-phase-alignment-default` | `dtra-adm-phase-alignment` |
| 外部生态变化要求什么转型，EA建议如何被阅读、讨论并关联到后续变更？ | `ea-point-of-view-register-default` | `ea-point-of-view-register` |
| EA 团队应提供哪些决策支持服务？ | `ea-service-catalog-default`, `ea-service-emergence-npd`, `ea-service-adm-evidence-map` | `ea-service-catalog` |
| 团队容量能否支撑所选架构服务？ | `ea-team-capacity-plan-default` | `ea-team-capacity-plan` |
| EA 服务如何为企业创造价值？ | `ea-value-map-default` | `ea-value-map` |
| EA应融入哪些已在使用的框架，在哪些接触点补位？ | `enterprise-framework-alignment-catalog-default` | `enterprise-framework-alignment-catalog` |
| 依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。 | `portfolio-stakeholder-concern-matrix` | `portfolio-stakeholder-concern-matrix` |
| 原则目录（兼容默认） | `compat-principles-catalog` | `principles-catalog` |
| 哪些观察应成为后续项目和EA能力改进的输入？ | `project-learning-record-log`, `project-learning-record-report` | `project-learning-record` |
| 缺失因素会如何影响采用结果？ | `readiness-consequence-analysis-default`, `dtra-factor-consequence` | `readiness-consequence-analysis` |
| 依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。 | `repository-parallel-candidates` | `repository-parallel-candidates` |
| 依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。 | `repository-state-view-tree` | `repository-state-view-tree` |
| 依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。 | `repository-target-baseline-comparison`, `repository-baseline-target-comparison` | `repository-target-baseline-comparison` |
| 企业可持续ICT能力有哪些具体强项、缺口和改进？ | `sustainability-capability-assessment-default` | `sustainability-capability-assessment` |
| 目标价值是否实际实现，差距是否需要H阶段发起新工作？ | `value-realization-assessment-default` | `value-realization-assessment` |

**何时不用本技能**：问题只涉及单一交付物的排版、或只需读取既有模型而不改结构时，直接查 `_shared/references/coverage.md` 而不启动本技能的分析流程。



## 原生标准与企业仿真接口

只有任务要求严格 UML 2.5.1、BPMN 2.0.2、ArchiMate 4、TRM/III-RM 或完整企业仿真闭环时，读取[共享标准与闭环接口](../_shared/references/standards-and-enterprise-closure.md)。保留原生包、项目模型和模拟/真实授权边界；接口报告未覆盖时不得宣称正式标准等价。普通单项制品沿用本技能的范围。

按需入口：[togaf-ea-capability 能力包索引](../_shared/references/togaf-ea-capability-package.md)；只读取与本次任务相关的条目。


## 本地解析与证据入口

先按当前任务运行 `python3 -B ../_shared/scripts/corpus_query.py "查询词"`，从结果定位本包 `corpus/` 中的当前章节解析和来源块。涉及基础标准时读取对应卷，不以指南摘要代替基础正文。当前逐节分析与完整中文译文的完成状态分别记录。使用相对路径运行共享工具；完整命令和依赖见[包运行约定](../_shared/references/local-package.md)。

## 本轮已审阅方法路由

先明确架构实践授权、服务对象和工作需求，再配置能力与发展路径。适用ADM入口：Preliminary,H。按[已审阅来源路由](../_shared/references/reviewed-method-routing.md)读取本技能的基础卷和指南；由当前业务材料实例化任务、待决问题、方法、制品与证据。单项架构图只收集相关业务输入；只有角色评价、人员配置或发展任务才启用人员证据。
