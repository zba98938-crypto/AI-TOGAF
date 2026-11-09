# MSA源、部署与执行单元追溯表

主责 `togaf-technology-architecture`；既有制品 `software-distribution-diagram` 的专用规范 `msa-source-deployment-execution`。

必要输入：本页字段对应的原始业务观察、来源、范围和时点。缺关键证据时保留unknown及缺口，不作通过判断。

## 字段与语义

| 字段 | 含义 |
|---|---|
| unit_kind | source/library/deployment/execution角色 |
| service_id | 所属逻辑服务，无业务库明确business-neutral |
| function | 各单元职责及ABF实现关系 |
| included_business_services | 包/源含的业务服务，禁止默默混包 |
| libraries | 依赖库ID；需验证无业务 |
| environment | 源码/制品仓库/执行环境身份 |
| instances | 实际或候选运行数量，非源与包复制数 |
| operating_condition | 健康、数据和故障/伸缩条件 |

## 分析

1. 分开源、公共库、部署包、运行实例
2. 验证单ABF与每源/包业务代码独立
3. 构建与部署用不同有向关系
4. 按需求/故障条件扩实例并保留同包追溯

## 表示与检查

输出对象/完整属性表、所有有类型关系与证据。table输出不进入通用流程图，不等于对应来源图已通过两布局视觉验收。
- 部署单元不得包含多个微服务代码
- 公共库必须无业务逻辑
- 多实例复用同部署包ID
- 部署端点角色与关系方向一致

## 完整例与反例

原料（历史材料已清理） → 分析（历史材料已清理） → 结果（历史材料已清理）。
修改（历史材料已清理）与失败反例（历史材料已清理）。

## 来源边界

- G21I §9.1–9.2
- 运行两实例不是两个微服务
- 本表完整表达关系；来源图形布局仍另验

本页字段与检查是正文指导下的项目操作规范，非TOGAF新增固定量表。路径相对skills/_shared，原始指南不随技能复制也可运行本例。
