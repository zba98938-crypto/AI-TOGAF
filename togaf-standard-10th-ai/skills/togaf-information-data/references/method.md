# 信息与数据架构：分析方法

适用 ADM：B C-data。以下为跨指南综合及项目生成约定。

## 分析路径

1. 统一业务术语和信息概念。
2. 区分业务数据实体及逻辑物理组件。
3. 确认属性、标识、关系及基数。
4. 映射应用操作、权威源和分发。
5. 设计质量、保留、迁移及核对。

## 关键判断

信息地图建立业务语义，概念数据模型强调实体与业务关系，逻辑模型细化属性和标识而不绑定产品。客户主数据需处理身份、匹配合并、质量和治理。元数据类型与组织/交换机制独立选择；BI 从决策问题反推信息，不默认替换现有仓库。

## 评审重点

未知基数不自动变成一对多；CRUD 主体按矩阵方向读取；副本不等于权威源；迁移有映射、核对、切换与回退。

## 来源定位

- [G190 方法摘要](../../_shared/references/source-analysis.md#g190)；原文位置见 sources.json。
- [G234 方法摘要](../../_shared/references/source-analysis.md#g234)；原文位置见 sources.json。
- [G238 方法摘要](../../_shared/references/source-analysis.md#g238)；原文位置见 sources.json。
- [G152 方法摘要](../../_shared/references/source-analysis.md#g152)；原文位置见 sources.json。

## 共用约定

输入处理、图表检索与验收边界见 [_shared/references/method-common.md](../../_shared/references/method-common.md)。
