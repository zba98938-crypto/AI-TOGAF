---
name: togaf-application-architecture
description: 分析应用组合、接口、应用支撑与交互，生成应用用例、处理、软件工程和分布等制品。
---

# 应用架构

先读取 [专属方法](references/method.md) 和 [共用规则](../_shared/references/modeling-rules.md)，再按请求只读取相关制品或交付物定义。默认中文，保留标准英文名称。

## 工作流程

1. 定义逻辑应用和实例边界。
2. 从业务功能和流程识别应用职责。
3. 采集接口契约和通信模式。
4. 分析数据访问与依赖。
5. 形成组件设计及部署分配并识别冗余。

按五维语境建立或修改共享 JSON 模型；使用同一模型派生文字、目录、矩阵和图。关键输入缺失先列缺口，不用虚构事实补齐。

## ADM 与架构成果联动

参与跨阶段任务或阶段评审时，按[阶段到制品工作映射](../_shared/references/architecture-delivery.md)承接C 阶段的领域工作：从实际利益相关者关注点选择本技能相关视图和方法，关联当前迭代判据及模型输出，生成后核对当前成果。用 `architecture_delivery.py catalog` 查询候选；选择理由、实际分析、生成完整性与真实决定分别保留。单项制品继续按用户指定范围执行。

## 主责制品

- [应用组合目录 / Application Portfolio Catalog](../_shared/references/artifacts/application-portfolio-catalog.md)
- [接口目录 / Interface Catalog](../_shared/references/artifacts/interface-catalog.md)
- [应用/功能矩阵 / Application/Function Matrix](../_shared/references/artifacts/application-function-matrix.md)
- [应用/组织矩阵 / Application/Organization Matrix](../_shared/references/artifacts/application-organization-matrix.md)
- [角色/应用矩阵 / Role/Application Matrix](../_shared/references/artifacts/role-application-matrix.md)
- [应用交互矩阵 / Application Interaction Matrix](../_shared/references/artifacts/application-interaction-matrix.md)
- [应用与用户位置图 / Application and User Location Diagram](../_shared/references/artifacts/application-and-user-location-diagram.md)
- [流程/应用实现图 / Process/Application Realization Diagram](../_shared/references/artifacts/process-application-realization-diagram.md)
- [应用通信图 / Application Communication Diagram](../_shared/references/artifacts/application-communication-diagram.md)
- [应用用例图 / Application Use-Case Diagram](../_shared/references/artifacts/application-use-case-diagram.md)
- [处理图 / Processing Diagram](../_shared/references/artifacts/processing-diagram.md)
- [软件分布图 / Software Distribution Diagram](../_shared/references/artifacts/software-distribution-diagram.md)
- [软件工程图 / Software Engineering Diagram](../_shared/references/artifacts/software-engineering-diagram.md)

## 主责交付物

按请求维护分析结果或交给工作台组装交付物。

## 生成与验收

按 [覆盖索引](../_shared/references/coverage.md) 获取 ID，运行集合说明中的 validate/generate/render 工具。仅处理用户请求的输出；跨域关系复用对象并咨询相应能力的方法。调用方向、消息与数据所有权分开；接口有版本及失败行为；角色使用不是授权；部署与逻辑支撑不混用。

输出包括 Markdown 和模型 JSON；图形另附可编辑源、SVG、PNG。报告来源、假设、未决项和验证结果。自动生成或检查不能改变真实批准状态。

## 全量指南能力与多视图

先读取 [全量能力工作流](../_shared/references/workflow-v2.md)。通过 [能力注册](../_shared/capabilities.json) 中的 owner 定位本技能的新增工作产品、视图规范和分析方法，按任务读取对应定义；原清单是兼容入口，不是能力上限。

分析、生成、修改和评审均须依据具体规范执行。一个制品族可以有多个 profile 和实际 view；保留五维语境、来源、假设及多个过渡状态。来源结构布局与业务适配布局共享模型。图形与表格均检查保存输出中的对象、关系、必要属性及 coverage.json 表示位置；存在遗漏或依据不足时交付明确标记的草稿及缺口，不声明已通过对标。核对 manifest.json 的模型、规范、模板与执行依赖指纹，旧输出不自动成为当前版本证据。组装交付物时按[动态组装规则](../_shared/references/deliverable-assembly.md)显式选择视图/分析；章节复制或 legacy-unassembled 不计为组装通过。

涉及元数据、客户主数据或 BI 演进时，读取 [信息架构专题手册](../_shared/references/information-architecture-handbook.md)，分别分析权威、交换、质量、职责及可运营状态。

## 任务路由表

本技能注册 17 个视图规范、2 个工作产品。先按决策问题选一行，再读对应规范；不要一次生成全部。

| 决策问题 | 建议规范 | 制品族 |
| --- | --- | --- |
| 应用与用户位置图（兼容默认） | `compat-application-and-user-location-diagram` | `application-and-user-location-diagram` |
| 应用通信图（兼容默认） | `compat-application-communication-diagram` | `application-communication-diagram` |
| 应用/功能矩阵（兼容默认） | `compat-application-function-matrix` | `application-function-matrix` |
| 应用交互矩阵（兼容默认） | `compat-application-interaction-matrix` | `application-interaction-matrix` |
| 应用/组织矩阵（兼容默认） | `compat-application-organization-matrix` | `application-organization-matrix` |
| 应用组合目录（兼容默认） | `compat-application-portfolio-catalog` | `application-portfolio-catalog` |
| 应用用例图（兼容默认） | `compat-application-use-case-diagram` | `application-use-case-diagram` |
| 接口目录（兼容默认） | `msa-contract-consumer-evidence` | `interface-catalog` |
| 应用应按什么边界拆分？ | `microservice-decomposition-method-default` | `microservice-decomposition-method` |
| 已实现和计划服务贡献什么价值？ | `microservice-value-catalog-default`, `msa-value-resource-evidence` | `microservice-value-catalog` |
| 流程/应用实现图（兼容默认） | `compat-process-application-realization-diagram` | `process-application-realization-diagram` |
| 处理图（兼容默认） | `compat-processing-diagram` | `processing-diagram` |
| 角色/应用矩阵（兼容默认） | `compat-role-application-matrix` | `role-application-matrix` |
| 软件分布图（兼容默认） | `compat-software-distribution-diagram` | `software-distribution-diagram` |
| 软件工程图（兼容默认） | `compat-software-engineering-diagram` | `software-engineering-diagram` |

**何时不用本技能**：问题只涉及单一交付物的排版、或只需读取既有模型而不改结构时，直接查 `_shared/references/coverage.md` 而不启动本技能的分析流程。



## 原生标准与企业仿真接口

只有任务要求严格 UML 2.5.1、BPMN 2.0.2、ArchiMate 4、TRM/III-RM 或完整企业仿真闭环时，读取[共享标准与闭环接口](../_shared/references/standards-and-enterprise-closure.md)。保留原生包、项目模型和模拟/真实授权边界；接口报告未覆盖时不得宣称正式标准等价。普通单项制品沿用本技能的范围。

按需入口：[togaf-application-architecture 能力包索引](../_shared/references/togaf-application-architecture-package.md)；只读取与本次任务相关的条目。


## 本地解析与证据入口

先按当前任务运行 `python3 -B ../_shared/scripts/corpus_query.py "查询词"`，从结果定位本包 `corpus/` 中的当前章节解析和来源块。涉及基础标准时读取对应卷，不以指南摘要代替基础正文。当前逐节分析与完整中文译文的完成状态分别记录。使用相对路径运行共享工具；完整命令和依赖见[包运行约定](../_shared/references/local-package.md)。

## 本轮已审阅方法路由

由需求和上位边界比较服务及应用方案，保留契约与失败场景。适用ADM入口：C。按[已审阅来源路由](../_shared/references/reviewed-method-routing.md)读取本技能的基础卷和指南；由当前业务材料实例化任务、待决问题、方法、制品与证据。单项架构图只收集相关业务输入；只有角色评价、人员配置或发展任务才启用人员证据。
