---
name: togaf-architecture-workbench
description: 为跨域企业架构任务选择和组合 TOGAF 技能、制品及交付物，适用于完整 ADM 或多能力协同工作。
---

# 架构工作台

先读取 [专属方法](references/method.md) 和 [共用规则](../_shared/references/modeling-rules.md)，再按请求只读取相关制品或交付物定义。默认中文，保留标准英文名称。

## 工作流程

用户要求通读、讲解或核对ADM、制品、流程与上下级关系时，读取[TOGAF关系与工作解释](../_shared/references/togaf-explained.md)，再按其中来源锚点核对原文。区分全景粒度、领域、抽象、演进、组成、实现、治理协作及人事关系。

完整 ADM、跨阶段推进或需求变化时，读取 [ADM 周期执行](../_shared/references/adm-cycle.md)，按阶段信息依赖、迭代、持续需求和真实决策维护周期记录。运行 `adm.py init/check/report` 得到当前阶段缺口和下一步；不要将 ADM 当固定瀑布顺序，也不要由生成成功推断阶段完成。

1. 识别战略、组合、项目或交付目的与待作决策。
2. 把关注点映射为少量制品及主责能力。
3. 先建立共享对象、来源与五维语境。
4. 协调各域分析和差距，再组装交付物。
5. 依照风险和决策节奏安排迭代评审。

按五维语境建立或修改共享 JSON 模型；使用同一模型派生文字、目录、矩阵和图。关键输入缺失先列缺口，不用虚构事实补齐。

## ADM 与架构成果联动

参与跨阶段任务或阶段评审时，按[阶段到制品工作映射](../_shared/references/architecture-delivery.md)承接所选ADM阶段的相关工作：从实际利益相关者关注点选择本技能相关视图和方法，关联当前迭代判据及模型输出，生成后核对当前成果。用 `architecture_delivery.py catalog` 查询候选；选择理由、实际分析、生成完整性与真实决定分别保留。单项制品继续按用户指定范围执行。

## 主责制品

本技能通过共享模型处理跨制品分析；按覆盖索引选择需要的表达，不额外创造清单外强制制品。

## 主责交付物

- [架构定义文档](../_shared/references/deliverables/architecture-definition-document.md)

## 生成与验收

面对百万级交易、事件与多基地台账，读取[大规模企业投影工作流](../_shared/references/large-enterprise-projection.md)：保留快照、SQL与哈希证据，按关注点聚合，区分统计事实与架构假设，再复用同一企业模型生成制品和交付物。

按 [覆盖索引](../_shared/references/coverage.md) 获取 ID，运行集合说明中的 validate/generate/render 工具。仅处理用户请求的输出；跨域关系复用对象并咨询相应能力的方法。确认每个制品实际回答关注点；确认交付物的结论受模型支撑；单一制品请求直接路由主责技能，不启动全量工作。

输出包括 Markdown 和模型 JSON；图形另附可编辑源、SVG、PNG。报告来源、假设、未决项和验证结果。自动生成或检查不能改变真实批准状态。

## 全量指南能力与多视图

先读取 [全量能力工作流](../_shared/references/workflow-v2.md)。通过 [能力注册](../_shared/capabilities.json) 中的 owner 定位本技能的新增工作产品、视图规范和分析方法，按任务读取对应定义；原清单是兼容入口，不是能力上限。

分析、生成、修改和评审均须依据具体规范执行。一个制品族可以有多个 profile 和实际 view；保留五维语境、来源、假设及多个过渡状态。来源结构布局与业务适配布局共享模型。图形与表格均检查保存输出中的对象、关系、必要属性及 coverage.json 表示位置；存在遗漏或依据不足时交付明确标记的草稿及缺口，不声明已通过对标。核对 manifest.json 的模型、规范、模板与执行依赖指纹，旧输出不自动成为当前版本证据。组装交付物时按[动态组装规则](../_shared/references/deliverable-assembly.md)显式选择视图/分析；章节复制或 legacy-unassembled 不计为组装通过。

## 任务路由表

本技能注册 10 个视图规范、5 个工作产品。先按决策问题选一行，再读对应规范；不要一次生成全部。

| 决策问题 | 建议规范 | 制品族 |
| --- | --- | --- |
| 架构工作在资源约束下怎样安排？ | `architecture-project-schedule-default`, `agile-ea-development`, `agile-solution-collaboration` | `architecture-project-schedule` |
| 怎样把架构成果分解为可管理工作？ | `architecture-project-wbs-default` | `architecture-project-wbs` |
| 各领域架构是否服务同一EA项目与目标、引用共享模型，安全是否作为关注点贯穿其他域？ | `domain-architecture-alignment-default` | `domain-architecture-alignment` |
| 敏捷协作模式选择与切换 | `agile-pattern-selection` | `options-decision-matrix` |
| 架构项目如何管理风险、质量、沟通、配置与控制，谁确认方法和授权边界？ | `project-management-strategy-default` | `project-management-strategy` |
| 本报告期实际完成了什么、下期做什么、余项如何预测，哪些事项需要决策或上报？ | `project-status-highlight-report-default` | `project-status-highlight-report` |

**何时不用本技能**：问题只涉及单一交付物的排版、或只需读取既有模型而不改结构时，直接查 `_shared/references/coverage.md` 而不启动本技能的分析流程。



## 原生标准与企业仿真接口

只有任务要求严格 UML 2.5.1、BPMN 2.0.2、ArchiMate 4、TRM/III-RM 或完整企业仿真闭环时，读取[共享标准与闭环接口](../_shared/references/standards-and-enterprise-closure.md)。保留原生包、项目模型和模拟/真实授权边界；接口报告未覆盖时不得宣称正式标准等价。普通单项制品沿用本技能的范围。

按需入口：[togaf-architecture-workbench 能力包索引](../_shared/references/togaf-architecture-workbench-package.md)；只读取与本次任务相关的条目。


## 本地解析与证据入口

先按当前任务运行 `python3 -B ../_shared/scripts/corpus_query.py "查询词"`，从结果定位本包 `corpus/` 中的当前章节解析和来源块。涉及基础标准时读取对应卷，不以指南摘要代替基础正文。当前逐节分析与完整中文译文的完成状态分别记录。使用相对路径运行共享工具；完整命令和依赖见[包运行约定](../_shared/references/local-package.md)。

## 本轮已审阅方法路由

先定目的、范围及关注点，再选阶段和制品；迭代及需求管理持续开展。适用ADM入口：Preliminary,A,B,C,D,E,F,G,H,Requirements。按[已审阅来源路由](../_shared/references/reviewed-method-routing.md)读取本技能的基础卷和指南；由当前业务材料实例化任务、待决问题、方法、制品与证据。单项架构图只收集相关业务输入；只有角色评价、人员配置或发展任务才启用人员证据。
