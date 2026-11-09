---
name: togaf-change-value
description: 分析架构变更、价值与绩效，生成影响评估、变更请求、监控与环境可持续性评估、债务日志及下一轮工作输入。
---

# 变更与价值管理

先读取 [专属方法](references/method.md) 和 [共用规则](../_shared/references/modeling-rules.md)，再按请求只读取相关制品或交付物定义。默认中文，保留标准英文名称。

## 工作流程

1. 比较承诺成果与实际观测。
2. 区分业务、技术、外部和治理变化。
3. 分析影响范围和紧迫度。
4. 提出维护、局部迭代或新周期选项。
5. 更新全景、请求与复评安排。

按五维语境建立或修改共享 JSON 模型；使用同一模型派生文字、目录、矩阵和图。关键输入缺失先列缺口，不用虚构事实补齐。

## ADM 与架构成果联动

参与跨阶段任务或阶段评审时，按[阶段到制品工作映射](../_shared/references/architecture-delivery.md)承接H 阶段的领域工作：从实际利益相关者关注点选择本技能相关视图和方法，关联当前迭代判据及模型输出，生成后核对当前成果。用 `architecture_delivery.py catalog` 查询候选；选择理由、实际分析、生成完整性与真实决定分别保留。单项制品继续按用户指定范围执行。

## 主责制品

本技能通过共享模型处理跨制品分析；按覆盖索引选择需要的表达，不额外创造清单外强制制品。

## 主责交付物

- [变更请求](../_shared/references/deliverables/change-request.md)
- [架构工作请求](../_shared/references/deliverables/request-for-architecture-work.md)

## 生成与验收

按 [覆盖索引](../_shared/references/coverage.md) 获取 ID，运行集合说明中的 validate/generate/render 工具。仅处理用户请求的输出；跨域关系复用对象并咨询相应能力的方法。实际值与目标值独立；触发下一轮有理由；未决变更不覆盖已知基线；新工作保留审批状态。

输出包括 Markdown 和模型 JSON；图形另附可编辑源、SVG、PNG。报告来源、假设、未决项和验证结果。自动生成或检查不能改变真实批准状态。

## 全量指南能力与多视图

先读取 [全量能力工作流](../_shared/references/workflow-v2.md)。通过 [能力注册](../_shared/capabilities.json) 中的 owner 定位本技能的新增工作产品、视图规范和分析方法，按任务读取对应定义；原清单是兼容入口，不是能力上限。

分析、生成、修改和评审均须依据具体规范执行。一个制品族可以有多个 profile 和实际 view；保留五维语境、来源、假设及多个过渡状态。来源结构布局与业务适配布局共享模型。图形与表格均检查保存输出中的对象、关系、必要属性及 coverage.json 表示位置；存在遗漏或依据不足时交付明确标记的草稿及缺口，不声明已通过对标。核对 manifest.json 的模型、规范、模板与执行依赖指纹，旧输出不自动成为当前版本证据。组装交付物时按[动态组装规则](../_shared/references/deliverable-assembly.md)显式选择视图/分析；章节复制或 legacy-unassembled 不计为组装通过。

## 任务路由表

本技能注册 11 个视图规范、7 个工作产品。先按决策问题选一行，再读对应规范；不要一次生成全部。

| 决策问题 | 建议规范 | 制品族 |
| --- | --- | --- |
| 本冲刺是否达成目标、学到什么、哪些工作需要回流或进入下一次规划？ | `dorp-record-default` | `dorp-record` |
| 哪些环境代价被推迟处理？ | `environmental-debt-register-default` | `environmental-debt-register` |
| 数字节制文化四维图 | `sustainability-culture-quadrant` | `environmental-decision-log` |
| 信息系统的环境影响从何而来？ | `environmental-is-assessment-default`, `annual-environmental-accounting`, `sustainability-causal-loop` | `environmental-is-assessment` |
| 事件如何改变了利益相关者的风险偏好与需求，有哪些目标变更、取消目标或取消变更的选项？ | `incident-architecture-adjustment-default` | `incident-architecture-adjustment` |
| 哪些单位数据可在什么边界、版本和单位下复用于环境评估？ | `shared-carbon-factor-catalog-default` | `shared-carbon-factor-catalog` |
| 从哪里识别可放弃/优化用途与设备，如何形成可接受约束？ | `sustainability-dual-entry-analysis-default` | `sustainability-dual-entry-analysis` |
| 哪些债务应由本产品或EA协调处理，如何追溯偿还并验证关闭？ | `technical-debt-register-default` | `technical-debt-register` |

**何时不用本技能**：问题只涉及单一交付物的排版、或只需读取既有模型而不改结构时，直接查 `_shared/references/coverage.md` 而不启动本技能的分析流程。



## 原生标准与企业仿真接口

只有任务要求严格 UML 2.5.1、BPMN 2.0.2、ArchiMate 4、TRM/III-RM 或完整企业仿真闭环时，读取[共享标准与闭环接口](../_shared/references/standards-and-enterprise-closure.md)。保留原生包、项目模型和模拟/真实授权边界；接口报告未覆盖时不得宣称正式标准等价。普通单项制品沿用本技能的范围。

按需入口：[togaf-change-value 能力包索引](../_shared/references/togaf-change-value-package.md)；只读取与本次任务相关的条目。


## 本地解析与证据入口

先按当前任务运行 `python3 -B ../_shared/scripts/corpus_query.py "查询词"`，从结果定位本包 `corpus/` 中的当前章节解析和来源块。涉及基础标准时读取对应卷，不以指南摘要代替基础正文。当前逐节分析与完整中文译文的完成状态分别记录。使用相对路径运行共享工具；完整命令和依赖见[包运行约定](../_shared/references/local-package.md)。

## 本轮已审阅方法路由

变更影响、收益归属和实际决策依据驱动迭代，不由渲染推断价值。适用ADM入口：H,E,F。按[已审阅来源路由](../_shared/references/reviewed-method-routing.md)读取本技能的基础卷和指南；由当前业务材料实例化任务、待决问题、方法、制品与证据。单项架构图只收集相关业务输入；只有角色评价、人员配置或发展任务才启用人员证据。
