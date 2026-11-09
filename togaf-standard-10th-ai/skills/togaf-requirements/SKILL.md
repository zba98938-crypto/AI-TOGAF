---
name: togaf-requirements
description: 维护架构需求、约束、需求规格及需求影响评估，支持跨阶段追溯和版本变化。
---

# 需求与影响

先读取 [专属方法](references/method.md) 和 [共用规则](../_shared/references/modeling-rules.md)，再按请求只读取相关制品或交付物定义。默认中文，保留标准英文名称。

## 工作流程

1. 从场景和目标识别需求。
2. 区分功能、质量、约束与设计决定。
3. 补齐来源优先级责任和验收。
4. 关联模型、控制及工作包。
5. 分析变更影响并记录处置。

跨阶段追溯或需求变更时，读取[持续需求追溯](../_shared/references/requirements-trace.md)，运行 `requirements_trace.py` 检查来源目标、设计分配、工作包、验收计划及结果证据，并定位受影响视图/交付物。按当前决策使用 planning 或 delivery，早期缺口保留为待办，不将计划或图可达性当作已满足。

按五维语境建立或修改共享 JSON 模型；使用同一模型派生文字、目录、矩阵和图。关键输入缺失先列缺口，不用虚构事实补齐。

## ADM 与架构成果联动

参与跨阶段任务或阶段评审时，按[阶段到制品工作映射](../_shared/references/architecture-delivery.md)承接贯穿 Preliminary 与 A–H 的持续需求管理：从实际利益相关者关注点选择本技能相关视图和方法，关联当前迭代判据及模型输出，生成后核对当前成果。用 `architecture_delivery.py catalog` 查询候选；选择理由、实际分析、生成完整性与真实决定分别保留。单项制品继续按用户指定范围执行。

## 主责制品

- [约束目录 / Constraints Catalog](../_shared/references/artifacts/constraints-catalog.md)
- [需求目录 / Requirements Catalog](../_shared/references/artifacts/requirements-catalog.md)
- [需求影响评估 / Requirements Impact Assessment](../_shared/references/artifacts/requirements-impact-assessment.md)

## 主责交付物

- [架构需求规格](../_shared/references/deliverables/architecture-requirements-specification.md)
- [需求影响评估](../_shared/references/deliverables/requirements-impact-assessment.md)

## 生成与验收

按 [覆盖索引](../_shared/references/coverage.md) 获取 ID，运行集合说明中的 validate/generate/render 工具。仅处理用户请求的输出；跨域关系复用对象并咨询相应能力的方法。禁止用未知关系证明无影响；保留需求和规格区别；验收可验证；同名影响评估制品及交付物共享数据。

输出包括 Markdown 和模型 JSON；图形另附可编辑源、SVG、PNG。报告来源、假设、未决项和验证结果。自动生成或检查不能改变真实批准状态。

## 全量指南能力与多视图

先读取 [全量能力工作流](../_shared/references/workflow-v2.md)。通过 [能力注册](../_shared/capabilities.json) 中的 owner 定位本技能的新增工作产品、视图规范和分析方法，按任务读取对应定义；原清单是兼容入口，不是能力上限。

分析、生成、修改和评审均须依据具体规范执行。一个制品族可以有多个 profile 和实际 view；保留五维语境、来源、假设及多个过渡状态。来源结构布局与业务适配布局共享模型。图形与表格均检查保存输出中的对象、关系、必要属性及 coverage.json 表示位置；存在遗漏或依据不足时交付明确标记的草稿及缺口，不声明已通过对标。核对 manifest.json 的模型、规范、模板与执行依赖指纹，旧输出不自动成为当前版本证据。组装交付物时按[动态组装规则](../_shared/references/deliverable-assembly.md)显式选择视图/分析；章节复制或 legacy-unassembled 不计为组装通过。

## 任务路由表

本技能注册 11 个视图规范、2 个工作产品。先按决策问题选一行，再读对应规范；不要一次生成全部。

| 决策问题 | 建议规范 | 制品族 |
| --- | --- | --- |
| 先处理哪些业务变革，当前团队冲刺承诺哪些架构结果？ | `architecture-business-backlog`, `architecture-sprint-backlog`, `architecture-strategic-mva-trace` | `architecture-backlog` |
| 分析平台需要满足什么可验证业务要求？ | `bi-requirements-profile-default`, `bi-requirement-origin-boundary`, `bi-usage-goal-measures` | `bi-requirements-profile` |
| 约束目录（兼容默认） | `compat-constraints-catalog` | `constraints-catalog` |
| 需求目录（兼容默认） | `compat-requirements-catalog` | `requirements-catalog` |
| 需求影响评估（兼容默认） | `compat-requirements-impact-assessment` | `requirements-impact-assessment` |

**何时不用本技能**：问题只涉及单一交付物的排版、或只需读取既有模型而不改结构时，直接查 `_shared/references/coverage.md` 而不启动本技能的分析流程。



## 原生标准与企业仿真接口

只有任务要求严格 UML 2.5.1、BPMN 2.0.2、ArchiMate 4、TRM/III-RM 或完整企业仿真闭环时，读取[共享标准与闭环接口](../_shared/references/standards-and-enterprise-closure.md)。保留原生包、项目模型和模拟/真实授权边界；接口报告未覆盖时不得宣称正式标准等价。普通单项制品沿用本技能的范围。

按需入口：[togaf-requirements 能力包索引](../_shared/references/togaf-requirements-package.md)；只读取与本次任务相关的条目。


## 本地解析与证据入口

先按当前任务运行 `python3 -B ../_shared/scripts/corpus_query.py "查询词"`，从结果定位本包 `corpus/` 中的当前章节解析和来源块。涉及基础标准时读取对应卷，不以指南摘要代替基础正文。当前逐节分析与完整中文译文的完成状态分别记录。使用相对路径运行共享工具；完整命令和依赖见[包运行约定](../_shared/references/local-package.md)。

## 本轮已审阅方法路由

持续维护需求依据、冲突、变化及各域制品追溯。适用ADM入口：Requirements,A,B,C,D,E,F,G,H。按[已审阅来源路由](../_shared/references/reviewed-method-routing.md)读取本技能的基础卷和指南；由当前业务材料实例化任务、待决问题、方法、制品与证据。单项架构图只收集相关业务输入；只有角色评价、人员配置或发展任务才启用人员证据。
