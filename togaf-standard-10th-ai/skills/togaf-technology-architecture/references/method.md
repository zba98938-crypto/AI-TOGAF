# 技术架构：分析方法

适用 ADM：D。以下为跨指南综合及项目生成约定。

## 分析路径

1. 从质量需求提取技术服务。
2. 区分逻辑组件和产品实例。
3. 确定环境、地点、网络与信任边界。
4. 分析容量、可用性、可观测性和恢复。
5. 核对标准与生命周期。

## 关键判断

技术服务、平台、组件、部署实例各有身份。网络通信描述被允许的协议与端口，硬件图描述物理拓扑与故障域。环境可持续性采用生命周期和明确测量范围，迁云只改变边界不自动降低总影响。

## 评审重点

标准状态不等于部署状态；网络连通不自动证明应用可用；容量与恢复结论有测量或假设；历史统计不作为现行阈值。

## 来源定位

- [G248 方法摘要](../../_shared/references/source-analysis.md#g248)；原文位置见 sources.json。
- [G152 方法摘要](../../_shared/references/source-analysis.md#g152)；原文位置见 sources.json。
- [G242 方法摘要](../../_shared/references/source-analysis.md#g242)；原文位置见 sources.json。

## 共用约定

输入处理、图表检索与验收边界见 [_shared/references/method-common.md](../../_shared/references/method-common.md)。
