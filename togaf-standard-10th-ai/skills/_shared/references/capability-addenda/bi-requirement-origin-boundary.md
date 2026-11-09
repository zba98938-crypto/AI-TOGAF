# BI架构需求及来源边界

主责 `togaf-requirements`；既有制品 `bi-requirements-profile` 的专用规范 `bi-requirement-origin-boundary`。

必要输入：本页字段对应的原始业务观察、来源、范围和时点。缺关键证据时保留unknown及缺口，不作通过判断。

## 字段与语义

| 字段 | 含义 |
|---|---|
| statement | 系统应+动词+对象+利益相关者，避免指定产品 |
| function | “系统”指的功能子系统 |
| requirement_origin | project-user-input/local-translation-added-example/verified-companion区别 |
| origin_locator | 具体出处 |
| official_requirement_id | 未取得配套源则unknown |
| verification | 当前核实范围 |
| completeness_claim | 项目局部/示例/全集的严格边界 |
| validation_criteria | 清晰原子唯一可验证，不混成测试细节 |
| companion_sheet | 配套电子表格是否实际找到并读完 |

## 分析

1. 记录来源身份再提炼需求
2. 按功能解释系统，检查原子/唯一/可验证
3. 区分项目需求和本地示例与官方配套记录
4. 未找到电子表格时只交付局部候选与缺口

## 表示与检查

输出对象/完整属性表、所有有类型关系与证据。table输出不进入通用流程图，不等于对应来源图已通过两布局视觉验收。
- 本地16例不得标原文逐条需求
- 缺配套源时official_requirement_id保持unknown
- 不宣称完整需求数量或全集覆盖
- 来源冲突明确登记

## 完整例与反例

原料（历史材料已清理） → 分析（历史材料已清理） → 结果（历史材料已清理）。
修改（历史材料已清理）与失败反例（历史材料已清理）。

## 来源边界

- G238 §4.4（特别是本地补写示例说明）
- 有需求示例不等于需求全集
- 没有电子表格不妨碍生成项目自己的需求

本页字段与检查是正文指导下的项目操作规范，非TOGAF新增固定量表。路径相对skills/_shared，原始指南不随技能复制也可运行本例。
