---
name: togaf-information-data
description: 分析信息与数据架构，生成信息关系与使用修改视图、概念及逻辑数据模型、生命周期和迁移，以及主数据、元数据、血缘与 BI 架构工作产品。
---

# 信息与数据架构

先读取 [专属方法](references/method.md) 和 [共用规则](../_shared/references/modeling-rules.md)，再按请求只读取相关制品或交付物定义。默认中文，保留标准英文名称。

## 工作流程

1. 统一业务术语和信息概念。
2. 区分业务数据实体及逻辑物理组件。
3. 确认属性、标识、关系及基数。
4. 映射应用操作、权威源和分发。
5. 设计质量、保留、迁移及核对。

按五维语境建立或修改共享 JSON 模型；使用同一模型派生文字、目录、矩阵和图。关键输入缺失先列缺口，不用虚构事实补齐。

## ADM 与架构成果联动

参与跨阶段任务或阶段评审时，按[阶段到制品工作映射](../_shared/references/architecture-delivery.md)承接C 阶段的领域工作：从实际利益相关者关注点选择本技能相关视图和方法，关联当前迭代判据及模型输出，生成后核对当前成果。用 `architecture_delivery.py catalog` 查询候选；选择理由、实际分析、生成完整性与真实决定分别保留。单项制品继续按用户指定范围执行。

## 主责制品

- [业务术语表目录 / Business Glossary Catalog](../_shared/references/artifacts/business-glossary-catalog.md)
- [数据实体/数据组件目录 / Data Entity/Data Component Catalog](../_shared/references/artifacts/data-entity-data-component-catalog.md)
- [数据实体/业务功能矩阵 / Data Entity/Business Function Matrix](../_shared/references/artifacts/data-entity-business-function-matrix.md)
- [应用/数据矩阵 / Application/Data Matrix](../_shared/references/artifacts/application-data-matrix.md)
- [业务服务/信息图 / Business Service/Information Diagram](../_shared/references/artifacts/business-service-information-diagram.md)
- [概念数据图 / Conceptual Data Diagram](../_shared/references/artifacts/conceptual-data-diagram.md)
- [信息地图 / Information Map](../_shared/references/artifacts/information-map.md)
- [数据分发图 / Data Dissemination Diagram](../_shared/references/artifacts/data-dissemination-diagram.md)
- [数据生命周期图 / Data Lifecycle Diagram](../_shared/references/artifacts/data-lifecycle-diagram.md)
- [数据迁移图 / Data Migration Diagram](../_shared/references/artifacts/data-migration-diagram.md)
- [逻辑数据图 / Logical Data Diagram](../_shared/references/artifacts/logical-data-diagram.md)

## 主责交付物

按请求维护分析结果或交给工作台组装交付物。

## 生成与验收

按 [覆盖索引](../_shared/references/coverage.md) 获取 ID，运行集合说明中的 validate/generate/render 工具。仅处理用户请求的输出；跨域关系复用对象并咨询相应能力的方法。未知基数不自动变成一对多；CRUD 主体按矩阵方向读取；副本不等于权威源；迁移有映射、核对、切换与回退。

输出包括 Markdown 和模型 JSON；图形另附可编辑源、SVG、PNG。报告来源、假设、未决项和验证结果。自动生成或检查不能改变真实批准状态。

## 全量指南能力与多视图

先读取 [全量能力工作流](../_shared/references/workflow-v2.md)。通过 [能力注册](../_shared/capabilities.json) 中的 owner 定位本技能的新增工作产品、视图规范和分析方法，按任务读取对应定义；原清单是兼容入口，不是能力上限。

分析、生成、修改和评审均须依据具体规范执行。一个制品族可以有多个 profile 和实际 view；保留五维语境、来源、假设及多个过渡状态。来源结构布局与业务适配布局共享模型。图形与表格均检查保存输出中的对象、关系、必要属性及 coverage.json 表示位置；存在遗漏或依据不足时交付明确标记的草稿及缺口，不声明已通过对标。核对 manifest.json 的模型、规范、模板与执行依赖指纹，旧输出不自动成为当前版本证据。组装交付物时按[动态组装规则](../_shared/references/deliverable-assembly.md)显式选择视图/分析；章节复制或 legacy-unassembled 不计为组装通过。

涉及元数据、客户主数据或 BI 演进时，读取 [信息架构专题手册](../_shared/references/information-architecture-handbook.md)，分别分析权威、交换、质量、职责及可运营状态。

评估项目元数据工具是否覆盖应用功能时，读取[元数据功能覆盖方法](../_shared/references/capability-addenda/metadata-function-coverage.md)，使用 `metadata-asset-coverage` 的 `metadata-application-function-coverage` 表格规范；参考功能地图与项目实现证据分别审查。

## 任务路由表

本技能注册 53 个视图规范、17 个工作产品。先按决策问题选一行，再读对应规范；不要一次生成全部。

| 决策问题 | 建议规范 | 制品族 |
| --- | --- | --- |
| 应用/数据矩阵（兼容默认） | `compat-application-data-matrix` | `application-data-matrix` |
| 如何从现有数仓演进到目标分析平台？ | `bi-transition-architecture-default`, `bi-baseline-transition-target`, `bi-stage-operability-and-exit` | `bi-transition-architecture` |
| 业务术语表目录（兼容默认） | `compat-business-glossary-catalog` | `business-glossary-catalog` |
| 业务服务/信息图（兼容默认） | `compat-business-service-information-diagram` | `business-service-information-diagram` |
| 业务概念落在哪些技术资产上？ | `business-technical-asset-mapping-default` | `business-technical-asset-mapping` |
| 有界基数概念关系 | `information-bounded-cardinality` | `conceptual-data-diagram` |
| 怎样形成可复用的客户主数据？ | `customer-mdm-model-default`, `mdm-operational-ten-questions`, `mdm-four-plateau-operations` | `customer-mdm-model` |
| 数据分发图（兼容默认） | `msa-data-distribution-conditions` | `data-dissemination-diagram` |
| 数据实体/业务功能矩阵（兼容默认） | `compat-data-entity-business-function-matrix` | `data-entity-business-function-matrix` |
| 数据实体/数据组件目录（兼容默认） | `compat-data-entity-data-component-catalog` | `data-entity-data-component-catalog` |
| 哪些数据问题应优先解决？ | `data-issue-register-default` | `data-issue-register` |
| 数据生命周期图（兼容默认） | `compat-data-lifecycle-diagram` | `data-lifecycle-diagram` |
| 数据迁移图（兼容默认） | `compat-data-migration-diagram` | `data-migration-diagram` |
| 数据质量能否支持业务与风险目标？ | `data-quality-assessment-default` | `data-quality-assessment` |
| 谁为何在什么条件下使用数据？ | `data-usage-documentation-default` | `data-usage-documentation` |
| 元数据业务功能参考地图 | `metadata-business-function-map`, `metadata-application-function-map` | `functional-decomposition-diagram` |
| 信息概念关系网络 | `information-concept-network`, `information-capability-use-modify`, `information-aggregation-generalization` | `information-map` |
| 逻辑实体属性与标识 | `logical-data-identifiers` | `logical-data-diagram` |
| 主数据交换由哪些应用与责任控制？ | `mdm-exchange-pattern-default` | `mdm-exchange-pattern` |
| 整合、协作还是集中管理主数据？ | `mdm-integration-style-default`, `mdm-consolidation-collaboration-central` | `mdm-integration-style` |
| 所需元数据范围是否覆盖管理关注点？ | `metadata-asset-coverage-default`, `metadata-category-coverage`, `metadata-application-function-coverage` | `metadata-asset-coverage` |
| 元数据资产究竟表示什么？ | `metadata-dictionary-default` | `metadata-dictionary` |
| 抽取技术元数据需要访问什么？ | `metadata-inference-design-default`, `metadata-inference-structure` | `metadata-inference-design` |
| 选择手工、推送还是拉取元数据？ | `metadata-ingestion-options-default`, `metadata-manual-push-pull` | `metadata-ingestion-options` |
| 多个元数据源如何协作并避免孤岛？ | `metadata-integration-model-default`, `metadata-central-hybrid-unified` | `metadata-integration-model` |
| 哪些元数据对象和关系足以支撑需求？ | `metadata-model-default` | `metadata-model` |
| 怎样保证元数据被一致维护？ | `metadata-policy-documentation-default` | `metadata-policy-documentation` |
| 元数据如何存储治理和供不同社区使用？ | `metadata-repository-design-default`, `metadata-three-part-solution` | `metadata-repository-design` |
| 谁在何时保证元数据质量？ | `metadata-validation-workflow-default` | `metadata-validation-workflow` |

**何时不用本技能**：问题只涉及单一交付物的排版、或只需读取既有模型而不改结构时，直接查 `_shared/references/coverage.md` 而不启动本技能的分析流程。



来源工作产品契约：[G190 information-map](../_shared/references/capabilities/information-map-source-contract.md)。按此契约核对输入、修改及反例，复用稳定基础制品ID。

## 原生标准与企业仿真接口

只有任务要求严格 UML 2.5.1、BPMN 2.0.2、ArchiMate 4、TRM/III-RM 或完整企业仿真闭环时，读取[共享标准与闭环接口](../_shared/references/standards-and-enterprise-closure.md)。保留原生包、项目模型和模拟/真实授权边界；接口报告未覆盖时不得宣称正式标准等价。普通单项制品沿用本技能的范围。

按需入口：[togaf-information-data 能力包索引](../_shared/references/togaf-information-data-package.md)；只读取与本次任务相关的条目。


## 本地解析与证据入口

先按当前任务运行 `python3 -B ../_shared/scripts/corpus_query.py "查询词"`，从结果定位本包 `corpus/` 中的当前章节解析和来源块。涉及基础标准时读取对应卷，不以指南摘要代替基础正文。当前逐节分析与完整中文译文的完成状态分别记录。使用相对路径运行共享工具；完整命令和依赖见[包运行约定](../_shared/references/local-package.md)。

## 本轮已审阅方法路由

区分业务信息、逻辑数据和物理实现；核对权威来源、生命周期、迁移及保护。适用ADM入口：C,Requirements。按[已审阅来源路由](../_shared/references/reviewed-method-routing.md)读取本技能的基础卷和指南；由当前业务材料实例化任务、待决问题、方法、制品与证据。单项架构图只收集相关业务输入；只有角色评价、人员配置或发展任务才启用人员证据。
