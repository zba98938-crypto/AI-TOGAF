---
name: togaf-value-streams
description: 定义价值流、阶段、价值链、价值流地图及价值流能力矩阵，分析端到端价值交付。
---

# 价值流分析

先读取 [专属方法](references/method.md) 和 [共用规则](../_shared/references/modeling-rules.md)，再按请求只读取相关制品或交付物定义。默认中文，保留标准英文名称。

## 工作流程

请求精益价值流、等待/加工时间或完整准确率时，读取 [精益流分析](../_shared/references/lean-flow-analysis.md)。先区分流程绩效与业务架构价值阶段；显式换算规则下可调用 lean-serial-flow，不能默认每天8小时或把流程映射当能力分解。

1. 确定触发方及其期望价值。
2. 定义开始结束边界。
3. 用进入退出条件和价值项界定阶段。
4. 逐阶段映射使能能力。
5. 识别价值断点、瓶颈及改进候选。

按五维语境建立或修改共享 JSON 模型；使用同一模型派生文字、目录、矩阵和图。关键输入缺失先列缺口，不用虚构事实补齐。

## ADM 与架构成果联动

参与跨阶段任务或阶段评审时，按[阶段到制品工作映射](../_shared/references/architecture-delivery.md)承接B 阶段的领域工作：从实际利益相关者关注点选择本技能相关视图和方法，关联当前迭代判据及模型输出，生成后核对当前成果。用 `architecture_delivery.py catalog` 查询候选；选择理由、实际分析、生成完整性与真实决定分别保留。单项制品继续按用户指定范围执行。

## 主责制品

- [价值流目录 / Value Stream Catalog](../_shared/references/artifacts/value-stream-catalog.md)
- [价值流阶段目录 / Value Stream Stages Catalog](../_shared/references/artifacts/value-stream-stages-catalog.md)
- [价值流/能力矩阵 / Value Stream/Capability Matrix](../_shared/references/artifacts/value-stream-capability-matrix.md)
- [价值链图 / Value Chain Diagram](../_shared/references/artifacts/value-chain-diagram.md)
- [价值流地图 / Value Stream Map](../_shared/references/artifacts/value-stream-map.md)

## 主责交付物

按请求维护分析结果或交给工作台组装交付物。

## 生成与验收

按 [覆盖索引](../_shared/references/coverage.md) 获取 ID，运行集合说明中的 validate/generate/render 工具。仅处理用户请求的输出；跨域关系复用对象并咨询相应能力的方法。阶段有可验证退出条件；能力映射不暗示时间顺序；颜色不凭空产生绩效结论；子价值流与能力实例分别建模。

输出包括 Markdown 和模型 JSON；图形另附可编辑源、SVG、PNG。报告来源、假设、未决项和验证结果。自动生成或检查不能改变真实批准状态。

## 全量指南能力与多视图

先读取 [全量能力工作流](../_shared/references/workflow-v2.md)。通过 [能力注册](../_shared/capabilities.json) 中的 owner 定位本技能的新增工作产品、视图规范和分析方法，按任务读取对应定义；原清单是兼容入口，不是能力上限。

分析、生成、修改和评审均须依据具体规范执行。一个制品族可以有多个 profile 和实际 view；保留五维语境、来源、假设及多个过渡状态。来源结构布局与业务适配布局共享模型。图形与表格均检查保存输出中的对象、关系、必要属性及 coverage.json 表示位置；存在遗漏或依据不足时交付明确标记的草稿及缺口，不声明已通过对标。核对 manifest.json 的模型、规范、模板与执行依赖指纹，旧输出不自动成为当前版本证据。组装交付物时按[动态组装规则](../_shared/references/deliverable-assembly.md)显式选择视图/分析；章节复制或 legacy-unassembled 不计为组装通过。

## 任务路由表

本技能注册 11 个视图规范、2 个工作产品。先按决策问题选一行，再读对应规范；不要一次生成全部。

| 决策问题 | 建议规范 | 制品族 |
| --- | --- | --- |
| 识别信息物料流中的等待、返工和浪费 | `lean-value-stream-default` | `lean-value-stream` |
| 主要与支持活动价值链 | `porter-value-chain` | `value-chain-diagram` |
| 判断多个参与者如何交换有形或无形价值以及网络依赖 | `value-network-default` | `value-network` |
| 价值流/能力矩阵（兼容默认） | `compat-value-stream-capability-matrix` | `value-stream-capability-matrix` |
| 价值流目录（兼容默认） | `compat-value-stream-catalog` | `value-stream-catalog` |
| 价值流阶段定义图 | `value-stream-definition`, `value-stream-enabling-capabilities`, `value-stream-capability-heatmap` | `value-stream-map` |
| 价值流阶段目录（兼容默认） | `compat-value-stream-stages-catalog` | `value-stream-stages-catalog` |

**何时不用本技能**：问题只涉及单一交付物的排版、或只需读取既有模型而不改结构时，直接查 `_shared/references/coverage.md` 而不启动本技能的分析流程。



## 原生标准与企业仿真接口

只有任务要求严格 UML 2.5.1、BPMN 2.0.2、ArchiMate 4、TRM/III-RM 或完整企业仿真闭环时，读取[共享标准与闭环接口](../_shared/references/standards-and-enterprise-closure.md)。保留原生包、项目模型和模拟/真实授权边界；接口报告未覆盖时不得宣称正式标准等价。普通单项制品沿用本技能的范围。

按需入口：[togaf-value-streams 能力包索引](../_shared/references/togaf-value-streams-package.md)；只读取与本次任务相关的条目。


## 本地解析与证据入口

先按当前任务运行 `python3 -B ../_shared/scripts/corpus_query.py "查询词"`，从结果定位本包 `corpus/` 中的当前章节解析和来源块。涉及基础标准时读取对应卷，不以指南摘要代替基础正文。当前逐节分析与完整中文译文的完成状态分别记录。使用相对路径运行共享工具；完整命令和依赖见[包运行约定](../_shared/references/local-package.md)。

## 本轮已审阅方法路由

区分价值阶段、能力使能及流程执行。适用ADM入口：B。按[已审阅来源路由](../_shared/references/reviewed-method-routing.md)读取本技能的基础卷和指南；由当前业务材料实例化任务、待决问题、方法、制品与证据。单项架构图只收集相关业务输入；只有角色评价、人员配置或发展任务才启用人员证据。
