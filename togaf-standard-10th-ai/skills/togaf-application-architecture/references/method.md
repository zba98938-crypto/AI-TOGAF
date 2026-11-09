# 应用架构：分析方法

适用 ADM：C-application。以下为跨指南综合及项目生成约定。

## 分析路径

1. 定义逻辑应用和实例边界。
2. 从业务功能和流程识别应用职责。
3. 采集接口契约和通信模式。
4. 分析数据访问与依赖。
5. 形成组件设计及部署分配并识别冗余。

## 关键判断

应用通信表达静态通信，处理图选择具体场景表达消息顺序，软件工程图表达模块职责依赖，软件分布图表达部署。微服务选择必须结合边界、数据、失败隔离和运维能力，不把拆分数量当目标。

## 评审重点

调用方向、消息与数据所有权分开；接口有版本及失败行为；角色使用不是授权；部署与逻辑支撑不混用。

## 来源定位

- [G248 方法摘要](../../_shared/references/source-analysis.md#g248)；原文位置见 sources.json。
- [G233 方法摘要](../../_shared/references/source-analysis.md#g233)；原文位置见 sources.json。
- [G234 方法摘要](../../_shared/references/source-analysis.md#g234)；原文位置见 sources.json。

## 共用约定

输入处理、图表检索与验收边界见 [_shared/references/method-common.md](../../_shared/references/method-common.md)。
