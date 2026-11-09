---
name: togaf-business-models-processes
description: 分析业务模式、客户旅程与画像、功能、服务、事件和流程，生成九块画布、用例、分解与实现视图及产品生命周期。
---

# 业务模式与流程

先读取 [专属方法](references/method.md) 和 [共用规则](../_shared/references/modeling-rules.md)，再按请求只读取相关制品或交付物定义。默认中文，保留标准英文名称。

## 工作流程

1. 解释客户价值及收入成本逻辑。
2. 区分服务承诺与内部功能。
3. 从事件到成果走查流程、角色和控制。
4. 细化场景、分支和例外。
5. 与能力及应用实现关系交叉核对。

按五维语境建立或修改共享 JSON 模型；使用同一模型派生文字、目录、矩阵和图。关键输入缺失先列缺口，不用虚构事实补齐。

## ADM 与架构成果联动

参与跨阶段任务或阶段评审时，按[阶段到制品工作映射](../_shared/references/architecture-delivery.md)承接B 阶段的领域工作：从实际利益相关者关注点选择本技能相关视图和方法，关联当前迭代判据及模型输出，生成后核对当前成果。用 `architecture_delivery.py catalog` 查询候选；选择理由、实际分析、生成完整性与真实决定分别保留。单项制品继续按用户指定范围执行。

## 主责制品

- [业务服务/功能目录 / Business Service/Function Catalog](../_shared/references/artifacts/business-service-function-catalog.md)
- [流程/事件/控制/产品目录 / Process/Event/Control/Product Catalog](../_shared/references/artifacts/process-event-control-product-catalog.md)
- [业务交互矩阵 / Business Interaction Matrix](../_shared/references/artifacts/business-interaction-matrix.md)
- [业务事件图 / Business Event Diagram](../_shared/references/artifacts/business-event-diagram.md)
- [业务模式图 / Business Model Diagram](../_shared/references/artifacts/business-model-diagram.md)
- [业务用例图 / Business Use-Case Diagram](../_shared/references/artifacts/business-use-case-diagram.md)
- [功能分解图 / Functional Decomposition Diagram](../_shared/references/artifacts/functional-decomposition-diagram.md)
- [流程图 / Process Flow Diagram](../_shared/references/artifacts/process-flow-diagram.md)
- [产品生命周期图 / Product Lifecycle Diagram](../_shared/references/artifacts/product-lifecycle-diagram.md)

## 主责交付物

按请求维护分析结果或交给工作台组装交付物。

## 生成与验收

按 [覆盖索引](../_shared/references/coverage.md) 获取 ID，运行集合说明中的 validate/generate/render 工具。仅处理用户请求的输出；跨域关系复用对象并咨询相应能力的方法。流程分支有条件且可终止；服务有消费者和承诺；事件不是活动；状态转换和价值阶段分别表述。

输出包括 Markdown 和模型 JSON；图形另附可编辑源、SVG、PNG。报告来源、假设、未决项和验证结果。自动生成或检查不能改变真实批准状态。

## 全量指南能力与多视图

先读取 [全量能力工作流](../_shared/references/workflow-v2.md)。通过 [能力注册](../_shared/capabilities.json) 中的 owner 定位本技能的新增工作产品、视图规范和分析方法，按任务读取对应定义；原清单是兼容入口，不是能力上限。

分析、生成、修改和评审均须依据具体规范执行。一个制品族可以有多个 profile 和实际 view；保留五维语境、来源、假设及多个过渡状态。来源结构布局与业务适配布局共享模型。图形与表格均检查保存输出中的对象、关系、必要属性及 coverage.json 表示位置；存在遗漏或依据不足时交付明确标记的草稿及缺口，不声明已通过对标。核对 manifest.json 的模型、规范、模板与执行依赖指纹，旧输出不自动成为当前版本证据。组装交付物时按[动态组装规则](../_shared/references/deliverable-assembly.md)显式选择视图/分析；章节复制或 legacy-unassembled 不计为组装通过。

## 任务路由表

本技能注册 26 个视图规范、7 个工作产品。先按决策问题选一行，再读对应规范；不要一次生成全部。

| 决策问题 | 建议规范 | 制品族 |
| --- | --- | --- |
| 业务事件图（兼容默认） | `compat-business-event-diagram` | `business-event-diagram` |
| 业务交互矩阵（兼容默认） | `compat-business-interaction-matrix` | `business-interaction-matrix` |
| 检查价值主张、客户、伙伴、活动、胜任力和价值公式及其关系是否一致 | `business-model-cube-default` | `business-model-cube` |
| 九块业务模式画布 | `business-model-canvas`, `business-model-baseline-target` | `business-model-diagram` |
| 业务服务/功能目录（兼容默认） | `compat-business-service-function-catalog` | `business-service-function-catalog` |
| 业务用例图（兼容默认） | `compat-business-use-case-diagram` | `business-use-case-diagram` |
| 客户如何经历服务并取得价值？ | `customer-journey-default` | `customer-journey` |
| 为谁设计业务和产品体验？ | `customer-persona-default` | `customer-persona` |
| 哪些数字业务功能适用于目标企业？ | `digital-business-reference-tailoring-default`, `dbrm-element-applicability`, `dbrm-digital-perspective-map` | `digital-business-reference-tailoring` |
| 评价客户价值主张能否由利润公式、资源和流程支持 | `four-box-business-model-default` | `four-box-business-model` |
| 功能分解图（兼容默认） | `compat-functional-decomposition-diagram` | `functional-decomposition-diagram` |
| 怎样把政府参考分类映射到实际职责？ | `government-reference-tailoring-default`, `government-reference-catalog-overlay` | `government-reference-tailoring` |
| 决定业务流程跨单元集成与标准化的合理程度 | `operating-model-default`, `operating-model-four-submodels` | `operating-model` |
| 流程/事件/控制/产品目录（兼容默认） | `compat-process-event-control-product-catalog` | `process-event-control-product-catalog` |
| 流程图（兼容默认） | `compat-process-flow-diagram` | `process-flow-diagram` |
| 产品生命周期图（兼容默认） | `compat-product-lifecycle-diagram` | `product-lifecycle-diagram` |

**何时不用本技能**：问题只涉及单一交付物的排版、或只需读取既有模型而不改结构时，直接查 `_shared/references/coverage.md` 而不启动本技能的分析流程。



## 原生标准与企业仿真接口

只有任务要求严格 UML 2.5.1、BPMN 2.0.2、ArchiMate 4、TRM/III-RM 或完整企业仿真闭环时，读取[共享标准与闭环接口](../_shared/references/standards-and-enterprise-closure.md)。保留原生包、项目模型和模拟/真实授权边界；接口报告未覆盖时不得宣称正式标准等价。普通单项制品沿用本技能的范围。

按需入口：[togaf-business-models-processes 能力包索引](../_shared/references/togaf-business-models-processes-package.md)；只读取与本次任务相关的条目。


## 本地解析与证据入口

先按当前任务运行 `python3 -B ../_shared/scripts/corpus_query.py "查询词"`，从结果定位本包 `corpus/` 中的当前章节解析和来源块。涉及基础标准时读取对应卷，不以指南摘要代替基础正文。当前逐节分析与完整中文译文的完成状态分别记录。使用相对路径运行共享工具；完整命令和依赖见[包运行约定](../_shared/references/local-package.md)。

## 本轮已审阅方法路由

用业务模型、组织和流程共同解释责任与价值。适用ADM入口：B。按[已审阅来源路由](../_shared/references/reviewed-method-routing.md)读取本技能的基础卷和指南；由当前业务材料实例化任务、待决问题、方法、制品与证据。单项架构图只收集相关业务输入；只有角色评价、人员配置或发展任务才启用人员证据。
