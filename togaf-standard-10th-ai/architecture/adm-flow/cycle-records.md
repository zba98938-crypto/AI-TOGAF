# 实际周期对象、状态与依赖

依赖箭头只来自实际depends_on；已填写completed与当前有效完成分别显示。

当前检查仍有缺口时保留其原状态；图不覆盖、签署或推进周期。

## Preliminary-1

记录状态：completed；决定：accepted

当前阶段检查：`recorded-complete`

依赖：

输入：entities/ROLE-CHIEF · 首席架构师
输入：entities/ROLE-EA · 企业架构师
输入：entities/ROLE-SEG · 库存分段架构师
输入：entities/ROLE-SOL · 履约解决方案架构师
输出：entities/ADM-WORK-Preliminary · 虚构 Preliminary 架构工作记录
输出：deliverables/ADM-DLV-architecture-principles · 全渠道／架构原则
输出：deliverables/ADM-DLV-architecture-repository · 全渠道／架构存储库
输出：deliverables/ADM-DLV-business-principles · 全渠道／业务原则
输出：deliverables/ADM-DLV-organization-model · 全渠道／企业架构组织模型
输出：deliverables/ADM-DLV-request-for-architecture-work · 全渠道／架构工作请求
输出：deliverables/ADM-DLV-tailored-architecture-framework · 全渠道／裁剪后的架构框架

## A-1

记录状态：completed；决定：accepted

当前阶段检查：`recorded-complete`

依赖：Preliminary-1

输入：entities/CAP-FULFIL · 全渠道履约
输入：entities/REQ-CONSISTENCY · 库存一致性与承诺标准待明确
输入：entities/REQ-OFFLINE · 门店断连仍可受理销售
输出：entities/ADM-WORK-A · 虚构 A 架构工作记录
输出：deliverables/ADM-DLV-architecture-requirements-specification · 全渠道／架构需求规格
输出：deliverables/ADM-DLV-architecture-vision · 全渠道／架构愿景
输出：deliverables/ADM-DLV-business-goals-objectives · 全渠道／业务目标与目的
输出：deliverables/ADM-DLV-business-principles · 全渠道／业务原则
输出：deliverables/ADM-DLV-business-drivers · 全渠道／业务驱动因素
输出：deliverables/ADM-DLV-capability-assessment · 全渠道／能力评估
输出：deliverables/ADM-DLV-communications-plan · 全渠道／沟通计划
输出：deliverables/ADM-DLV-request-for-architecture-work · 全渠道／架构工作请求
输出：deliverables/ADM-DLV-statement-of-work · 全渠道／架构工作说明书

## B-1

记录状态：completed；决定：accepted

当前阶段检查：`recorded-complete`

依赖：A-1

输入：entities/CAP-ORDER · 订单承诺
输入：entities/CAP-RESERVE · 库存预占
输入：entities/CAP-LOGISTICS · 物流履约
输入：entities/ORDER-PENDING · 订单已受理／待确认
输入：entities/ORDER-CONFIRMED · 订单已确认
输出：entities/ADM-WORK-B · 虚构 B 架构工作记录
输出：deliverables/ADM-DLV-architecture-building-blocks · 全渠道／架构构建块
输出：deliverables/ADM-DLV-architecture-definition-document · 全渠道／架构定义文档
输出：deliverables/ADM-DLV-architecture-requirements-specification · 全渠道／架构需求规格
输出：deliverables/ADM-DLV-business-goals-objectives · 全渠道／业务目标与目的
输出：deliverables/ADM-DLV-capability-assessment · 全渠道／能力评估

## C-1

记录状态：completed；决定：accepted

当前阶段检查：`recorded-complete`

依赖：A-1

输入：entities/APP-ORDER · 线上订单应用
输入：entities/APP-STOCK · 库存服务
输入：entities/APP-STORE · 门店销售应用
输入：entities/IF-RESERVE · 中央库存预占接口
输入：entities/IF-RECOVERY · 门店恢复同步接口
输出：entities/ADM-WORK-C · 虚构 C 架构工作记录
输出：deliverables/ADM-DLV-architecture-building-blocks · 全渠道／架构构建块
输出：deliverables/ADM-DLV-architecture-definition-document · 全渠道／架构定义文档
输出：deliverables/ADM-DLV-architecture-requirements-specification · 全渠道／架构需求规格

## D-1

记录状态：completed；决定：accepted

当前阶段检查：`recorded-complete`

依赖：A-1

输入：entities/LOCAL-ORDER-RECORD · 门店本地待同步订单记录
输入：entities/CENTRAL-ORDER-RECORD · 中央接收与承诺记录
输出：entities/ADM-WORK-D · 虚构 D 架构工作记录
输出：deliverables/ADM-DLV-architecture-building-blocks · 全渠道／架构构建块
输出：deliverables/ADM-DLV-architecture-definition-document · 全渠道／架构定义文档
输出：deliverables/ADM-DLV-architecture-requirements-specification · 全渠道／架构需求规格

## E-1

记录状态：completed；决定：accepted

当前阶段检查：`recorded-complete`

依赖：B-1, C-1, D-1

输入：entities/WP-ONLINE · 在线试点准备
输入：entities/WP-OFFLINE · 断连与恢复演练
输入：entities/TRANS-ONLINE · 受控在线试点
输入：entities/TRANS-OFFLINE · 断连受理与恢复对账试点
输出：entities/ADM-WORK-E · 虚构 E 架构工作记录
输出：deliverables/ADM-DLV-architecture-building-blocks · 全渠道／架构构建块
输出：deliverables/ADM-DLV-architecture-definition-document · 全渠道／架构定义文档
输出：deliverables/ADM-DLV-architecture-roadmaps · 全渠道／架构路线图
输出：deliverables/ADM-DLV-capability-assessment · 全渠道／能力评估
输出：deliverables/ADM-DLV-solution-building-blocks · 全渠道／解决方案构建块

## F-1

记录状态：completed；决定：accepted

当前阶段检查：`recorded-complete`

依赖：E-1

输入：entities/WP-ONLINE · 在线试点准备
输入：entities/WP-OFFLINE · 断连与恢复演练
输入：entities/TRANS-ONLINE · 受控在线试点
输入：entities/TRANS-OFFLINE · 断连受理与恢复对账试点
输出：entities/ADM-WORK-F · 虚构 F 架构工作记录
输出：deliverables/ADM-DLV-architecture-roadmaps · 全渠道／架构路线图
输出：deliverables/ADM-DLV-implementation-migration-plan · 全渠道／实施与迁移计划
输出：deliverables/ADM-DLV-implementation-governance-model · 全渠道／实施治理模型

## G-1

记录状态：completed；决定：accepted

当前阶段检查：`recorded-complete`

依赖：F-1

输入：entities/ORDER-CONFIRMED · 订单已确认
输入：entities/ORDER-FULFIL · 允许物流履约的订单记录
输入：entities/IF-RECOVERY · 门店恢复同步接口
输出：entities/ADM-WORK-G · 虚构 G 架构工作记录
输出：deliverables/ADM-DLV-architecture-contract · 全渠道／架构合同
输出：deliverables/ADM-DLV-change-request · 全渠道／变更请求
输出：deliverables/ADM-DLV-communications-plan · 全渠道／沟通计划
输出：deliverables/ADM-DLV-compliance-assessment · 全渠道／合规评估
输出：deliverables/ADM-DLV-solution-building-blocks · 全渠道／解决方案构建块
输出：deliverables/ADM-DLV-implementation-governance-model · 全渠道／实施治理模型

## H-1

记录状态：completed；决定：accepted

当前阶段检查：`recorded-complete`

依赖：G-1

输入：entities/CAP-RESERVE · 库存预占
输入：entities/RISK-STOCK · 库存冲突风险处理
输出：entities/ADM-WORK-H · 虚构 H 架构工作记录
输出：deliverables/ADM-DLV-architecture-repository · 全渠道／架构存储库
输出：deliverables/ADM-DLV-architecture-roadmaps · 全渠道／架构路线图
输出：deliverables/ADM-DLV-change-request · 全渠道／变更请求
输出：deliverables/ADM-DLV-communications-plan · 全渠道／沟通计划
输出：deliverables/ADM-DLV-request-for-architecture-work · 全渠道／架构工作请求
输出：deliverables/ADM-DLV-requirements-impact-assessment · 全渠道／需求影响评估
