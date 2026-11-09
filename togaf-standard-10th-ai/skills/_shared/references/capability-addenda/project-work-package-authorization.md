# 项目工作包授权记录

项目WBS工作能否开始，产品、前提和授权是否齐备？

依据：G188 §2.3、§3.4.1–3.4.3。字段结构与状态编码是项目操作规范，原始指南不随运行读取。

## 输入与缺口

范围、五维语境、所用目标与交付物版本；原始计划/访谈/验收/估算及来源ID；组织授权和容差规则；缺失时不代推。关键依据未知时给候选表、受影响ID与责任；不编造权重、阈值、估算、批准或实际完成。

## 字段语义

| 字段 | 含义 |
|---|---|
| name | 授权事项 |
| project_task_id | 项目任务稳定ID |
| wbs_parent | WBS父项 |
| work_package_kind | 必须明确project-wbs-leaf，非TOGAF变革包 |
| deliverable | 应交付产品及范围 |
| preconditions | 前置产品验收与其他进入条件 |
| cost_time_tolerance | 成本/工期/容差及项目规则出处 |
| quality_configuration | 质量准则、版本/配置要求 |
| reporting | 检查点频率和信息分发 |
| authority | 谁有权授权以及授权范围 |
| authorization | 未授权/授权证据，不能从空闲推断 |
| evidence_refs | 材料ID |
| next_action | 允许开始或缺口处理 |

## 分析步骤

1. 识别PM项目工作包及其WBS/产品范围
2. 核实前置产品验收及所有进入条件
3. 确认成本/工期/容差、质量配置及报告要求
4. 取得权限范围内PM明确授权并留记录
5. 完成并接受产品后才允许后续工作包重新走授权

### 项目工作包授权记录

原始材料（历史材料已清理）组 `authorization`。AU-02前置交付物未获接受，也没有PM明确授权；团队空闲不能替代任一条件。成本/时间容差仍是提案。

`artifact_id=project-work-package-authorization`；`profile_id=project-work-package-authorization-default`；`view_id=v-project-work-package-authorization-default`。完整表见生成索引（历史材料已清理）。

## 修改与反例

修改：DEL-APPS-v2已接受且PM确认规则并发授权。结果：状态改为authorized-in-fixture，可在虚构案例开始；不授予真实人工作权限。

反例：无授权却请求开始。结果：authorization-not-ready。

## 质量与追溯

- 依赖完成不等于已授权，团队空闲不等于允许开始
- PM工作包与变革工作包分开建模
- 无授权记录不得转为已开始或已完成

执行证据（历史材料已清理）分别记录模型、生成、修改、反例及表内表达。表格不进行图形视觉验收。工程执行不能替代业务审批和独立业务审查。
