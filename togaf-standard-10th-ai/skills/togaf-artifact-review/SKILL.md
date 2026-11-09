---
name: togaf-artifact-review
description: 评审 TOGAF 制品的语义、追溯、跨视图一致性、基线目标可比性和图形可读性。
---

# 架构制品评审

先读取 [专属方法](references/method.md) 和 [共用规则](../_shared/references/modeling-rules.md)，再按请求只读取相关制品或交付物定义。默认中文，保留标准英文名称。

## 工作流程

1. 确定制品用途和所用表示法。
2. 校验对象类型、关系方向及数量。
3. 跨目录矩阵图对照共享对象。
4. 检查证据假设、状态与差距。
5. 渲染后目视检查并按严重度报告。

按五维语境建立或修改共享 JSON 模型；使用同一模型派生文字、目录、矩阵和图。关键输入缺失先列缺口，不用虚构事实补齐。

## ADM 与架构成果联动

参与跨阶段任务或阶段评审时，按[阶段到制品工作映射](../_shared/references/architecture-delivery.md)承接贯穿 Preliminary 与 A–H 的关注点评审与成果验收：从实际利益相关者关注点选择本技能相关视图和方法，关联当前迭代判据及模型输出，生成后核对当前成果。用 `architecture_delivery.py catalog` 查询候选；选择理由、实际分析、生成完整性与真实决定分别保留。单项制品继续按用户指定范围执行。

## 主责制品

本技能通过共享模型处理跨制品分析；按覆盖索引选择需要的表达，不额外创造清单外强制制品。

## 主责交付物

按请求维护分析结果或交给工作台组装交付物。

## 生成与验收

按 [覆盖索引](../_shared/references/coverage.md) 获取 ID，运行集合说明中的 validate/generate/render 工具。仅处理用户请求的输出；跨域关系复用对象并咨询相应能力的方法。报告包含对象或关系 ID、依据、影响和修正建议；不能只给总体通过；渲染成功不等于业务正确。

输出包括 Markdown 和模型 JSON；图形另附可编辑源、SVG、PNG。报告来源、假设、未决项和验证结果。自动生成或检查不能改变真实批准状态。

## 全量指南能力与多视图

先读取 [全量能力工作流](../_shared/references/workflow-v2.md)。通过 [能力注册](../_shared/capabilities.json) 中的 owner 定位本技能的新增工作产品、视图规范和分析方法，按任务读取对应定义；原清单是兼容入口，不是能力上限。

分析、生成、修改和评审均须依据具体规范执行。一个制品族可以有多个 profile 和实际 view；保留五维语境、来源、假设及多个过渡状态。来源结构布局与业务适配布局共享模型。图形与表格均检查保存输出中的对象、关系、必要属性及 coverage.json 表示位置；存在遗漏或依据不足时交付明确标记的草稿及缺口，不声明已通过对标。核对 manifest.json 的模型、规范、模板与执行依赖指纹，旧输出不自动成为当前版本证据。组装交付物时按[动态组装规则](../_shared/references/deliverable-assembly.md)显式选择视图/分析；章节复制或 legacy-unassembled 不计为组装通过。

## 任务路由表

本技能注册 11 个视图规范、8 个工作产品。先按决策问题选一行，再读对应规范；不要一次生成全部。

| 决策问题 | 建议规范 | 制品族 |
| --- | --- | --- |
| 怎样判断架构成果足以支持决策？ | `architecture-acceptance-criteria-default` | `architecture-acceptance-criteria` |
| 当前描述是否足以支持指定决策，表达与治理控制是否适合当前目的？ | `architecture-description-formality-table` | `architecture-description-formality-review` |
| 目标能否批准，实施是否合理遵循目标且如何处理偏差？ | `architecture-governance-checklist-target`, `architecture-governance-checklist-implementation` | `architecture-governance-checklist` |
| 对已证实偏差应强制执行、临时豁免还是重审目标？ | `non-compliance-disposition-default` | `non-compliance-disposition` |
| 交付物要交什么、如何核验、由谁接受？ | `project-deliverable-charter-default` | `project-deliverable-charter` |
| 是否继续、修改或终止阶段/项目，责任与成果是否可交接？ | `project-stage-closure-record-stage`, `project-stage-closure-record-project` | `project-stage-closure-record` |
| 方案的环境贡献与措施是否一致？ | `sustainability-review-canvas-default`, `sustainability-architecture-canvas` | `sustainability-review-canvas` |
| 为完整利益相关者关注点选择哪些可复用构图规范？ | `viewpoint-library-default` | `viewpoint-library` |

**何时不用本技能**：问题只涉及单一交付物的排版、或只需读取既有模型而不改结构时，直接查 `_shared/references/coverage.md` 而不启动本技能的分析流程。



## 原生标准与企业仿真接口

只有任务要求严格 UML 2.5.1、BPMN 2.0.2、ArchiMate 4、TRM/III-RM 或完整企业仿真闭环时，读取[共享标准与闭环接口](../_shared/references/standards-and-enterprise-closure.md)。保留原生包、项目模型和模拟/真实授权边界；接口报告未覆盖时不得宣称正式标准等价。普通单项制品沿用本技能的范围。

按需入口：[togaf-artifact-review 能力包索引](../_shared/references/togaf-artifact-review-package.md)；只读取与本次任务相关的条目。


## 本地解析与证据入口

先按当前任务运行 `python3 -B ../_shared/scripts/corpus_query.py "查询词"`，从结果定位本包 `corpus/` 中的当前章节解析和来源块。涉及基础标准时读取对应卷，不以指南摘要代替基础正文。当前逐节分析与完整中文译文的完成状态分别记录。使用相对路径运行共享工具；完整命令和依赖见[包运行约定](../_shared/references/local-package.md)。

## 本轮已审阅方法路由

从原始业务材料核对决定与制品，结构、语义、视觉和批准各自取证。适用ADM入口：Preliminary,A,B,C,D,E,F,G,H,Requirements。按[已审阅来源路由](../_shared/references/reviewed-method-routing.md)读取本技能的基础卷和指南；由当前业务材料实例化任务、待决问题、方法、制品与证据。单项架构图只收集相关业务输入；只有角色评价、人员配置或发展任务才启用人员证据。
