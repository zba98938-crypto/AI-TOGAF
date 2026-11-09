---
name: togaf-strategy-capabilities
description: 分析战略和业务能力，生成分类、分解、热力、足迹及收益视图，开展能力评估、能力实例与增量规划及投资方案比较。
---

# 战略与业务能力

先读取 [专属方法](references/method.md) 和 [共用规则](../_shared/references/modeling-rules.md)，再按请求只读取相关制品或交付物定义。默认中文，保留标准英文名称。

## 工作流程

1. 分离业务驱动、目标与可衡量目的。
2. 以业务对象和结果定义稳定能力。
3. 检查分解覆盖、同层粒度和复用。
4. 连接目标、组织和实现要素。
5. 用明确量尺分析差距、收益及投资候选。

按五维语境建立或修改共享 JSON 模型；使用同一模型派生文字、目录、矩阵和图。关键输入缺失先列缺口，不用虚构事实补齐。

## ADM 与架构成果联动

参与跨阶段任务或阶段评审时，按[阶段到制品工作映射](../_shared/references/architecture-delivery.md)承接B 阶段的领域工作：从实际利益相关者关注点选择本技能相关视图和方法，关联当前迭代判据及模型输出，生成后核对当前成果。用 `architecture_delivery.py catalog` 查询候选；选择理由、实际分析、生成完整性与真实决定分别保留。单项制品继续按用户指定范围执行。

## 主责制品

- [业务能力目录 / Business Capabilities Catalog](../_shared/references/artifacts/business-capabilities-catalog.md)
- [驱动因素/目标/目的目录 / Driver/Goal/Objective Catalog](../_shared/references/artifacts/driver-goal-objective-catalog.md)
- [战略/能力矩阵 / Strategy/Capability Matrix](../_shared/references/artifacts/strategy-capability-matrix.md)
- [收益图 / Benefits Diagram](../_shared/references/artifacts/benefits-diagram.md)
- [业务能力地图 / Business Capability Map](../_shared/references/artifacts/business-capability-map.md)
- [业务足迹图 / Business Footprint Diagram](../_shared/references/artifacts/business-footprint-diagram.md)
- [目标/目的/服务图 / Goal/Objective/Service Diagram](../_shared/references/artifacts/goal-objective-service-diagram.md)

## 主责交付物

- [业务目标与目的](../_shared/references/deliverables/business-goals-objectives.md)
- [业务驱动因素](../_shared/references/deliverables/business-drivers.md)
- [能力评估](../_shared/references/deliverables/capability-assessment.md)

## 生成与验收

按 [覆盖索引](../_shared/references/coverage.md) 获取 ID，运行集合说明中的 validate/generate/render 工具。仅处理用户请求的输出；跨域关系复用对象并咨询相应能力的方法。能力不以应用或部门命名；战略关系方向清楚；同一能力多处使用不重复建对象；评分不跨量尺求总分。

输出包括 Markdown 和模型 JSON；图形另附可编辑源、SVG、PNG。报告来源、假设、未决项和验证结果。自动生成或检查不能改变真实批准状态。

## 全量指南能力与多视图

先读取 [全量能力工作流](../_shared/references/workflow-v2.md)。通过 [能力注册](../_shared/capabilities.json) 中的 owner 定位本技能的新增工作产品、视图规范和分析方法，按任务读取对应定义；原清单是兼容入口，不是能力上限。

分析、生成、修改和评审均须依据具体规范执行。一个制品族可以有多个 profile 和实际 view；保留五维语境、来源、假设及多个过渡状态。来源结构布局与业务适配布局共享模型。图形与表格均检查保存输出中的对象、关系、必要属性及 coverage.json 表示位置；存在遗漏或依据不足时交付明确标记的草稿及缺口，不声明已通过对标。核对 manifest.json 的模型、规范、模板与执行依赖指纹，旧输出不自动成为当前版本证据。组装交付物时按[动态组装规则](../_shared/references/deliverable-assembly.md)显式选择视图/分析；章节复制或 legacy-unassembled 不计为组装通过。

涉及 ACMM、DTRA、场景关联或方案评分时，读取 [评价与场景分析手册](../_shared/references/assessment-handbook.md)，按特征证据开展评价；不得用统一总分代替来源方法。

## 任务路由表

本技能注册 15 个视图规范、3 个工作产品。先按决策问题选一行，再读对应规范；不要一次生成全部。

| 决策问题 | 建议规范 | 制品族 |
| --- | --- | --- |
| 从四个视角识别可追溯目标与可度量成果以驱动能力改进 | `balanced-scorecard-default` | `balanced-scorecard` |
| 收益图（兼容默认） | `compat-benefits-diagram` | `benefits-diagram` |
| 业务能力目录（兼容默认） | `compat-business-capabilities-catalog` | `business-capabilities-catalog` |
| 能力分类地图 | `capability-classification`, `capability-decomposition`, `capability-gap-heatmap` | `business-capability-map` |
| 能力与战略足迹 | `capability-strategy-overlay` | `business-footprint-diagram` |
| 某阶段由什么具体组成实现能力？ | `capability-instance-model-default`, `capability-instance-composition` | `capability-instance-model` |
| 驱动因素/目标/目的目录（兼容默认） | `compat-driver-goal-objective-catalog` | `driver-goal-objective-catalog` |
| 目标/目的/服务图（兼容默认） | `compat-goal-objective-service-diagram` | `goal-objective-service-diagram` |
| 每个目的是否具体、可度量、可行动、现实、有时限，并追溯到已分类的目标？ | `smart-objective-assessment-default` | `smart-objective-assessment` |
| 战略/能力矩阵（兼容默认） | `compat-strategy-capability-matrix` | `strategy-capability-matrix` |

**何时不用本技能**：问题只涉及单一交付物的排版、或只需读取既有模型而不改结构时，直接查 `_shared/references/coverage.md` 而不启动本技能的分析流程。



来源工作产品契约：[G211 business-capability-map](../_shared/references/capabilities/business-capability-map-source-contract.md)。按此契约核对输入、修改及反例，复用稳定基础制品ID。

## 原生标准与企业仿真接口

只有任务要求严格 UML 2.5.1、BPMN 2.0.2、ArchiMate 4、TRM/III-RM 或完整企业仿真闭环时，读取[共享标准与闭环接口](../_shared/references/standards-and-enterprise-closure.md)。保留原生包、项目模型和模拟/真实授权边界；接口报告未覆盖时不得宣称正式标准等价。普通单项制品沿用本技能的范围。

按需入口：[togaf-strategy-capabilities 能力包索引](../_shared/references/togaf-strategy-capabilities-package.md)；只读取与本次任务相关的条目。


## 本地解析与证据入口

先按当前任务运行 `python3 -B ../_shared/scripts/corpus_query.py "查询词"`，从结果定位本包 `corpus/` 中的当前章节解析和来源块。涉及基础标准时读取对应卷，不以指南摘要代替基础正文。当前逐节分析与完整中文译文的完成状态分别记录。使用相对路径运行共享工具；完整命令和依赖见[包运行约定](../_shared/references/local-package.md)。

## 本轮已审阅方法路由

核对战略—能力—实例—增量的身份与范围。适用ADM入口：A,B,E。按[已审阅来源路由](../_shared/references/reviewed-method-routing.md)读取本技能的基础卷和指南；由当前业务材料实例化任务、待决问题、方法、制品与证据。单项架构图只收集相关业务输入；只有角色评价、人员配置或发展任务才启用人员证据。
