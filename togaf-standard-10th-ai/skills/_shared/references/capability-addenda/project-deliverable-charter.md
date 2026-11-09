# 交付物章程与验收流程

交付物要交什么、如何核验、由谁接受？

依据：G188 §3.1.8示例3-14、§3.2.2–3.2.3、§3.5.1。字段结构与状态编码是项目操作规范，原始指南不随运行读取。

## 输入与缺口

范围、五维语境、所用目标与交付物版本；原始计划/访谈/验收/估算及来源ID；组织授权和容差规则；缺失时不代推。关键依据未知时给候选表、受影响ID与责任；不编造权重、阈值、估算、批准或实际完成。

## 字段语义

| 字段 | 含义 |
|---|---|
| name | 交付物章程名称 |
| deliverable_id | 交付物稳定ID与版本 |
| scope | 内容与范围 |
| exclusions | 明确排除 |
| required_inputs | 输入及其版本/就绪情况 |
| acceptance_criteria | 可检验条件与既有单项验收准则ID |
| acceptance_process | 按组织规则的移交/评审/修订/终审流程 |
| decision_roles | 评审/修订/最终接受角色分开 |
| review_observations | 实际评审发现与证据 |
| status | 候选/评审/接受/拒绝；生成不等于接受 |
| evidence_refs | 材料ID |
| next_action | 补缺或下一验收动作 |

## 分析步骤

1. 从决策和利益相关者定义产品范围与排除
2. 确认输入与版本并找缺口
3. 写可观察验收准则，引用已有architecture-acceptance-criteria记录
4. 规定评审与修订流程及有权接受者
5. 逐条实际评审，保留拒绝/重作路径；接受后再进入阶段/项目关闭

### 交付物章程与验收流程

原始材料（历史材料已清理）组 `charter`。从DC-01/02区分范围、排除、输入和四条验收准则；DC-03是项目5/3/2日流程，不照搬G188示例的2周等时长。11/12覆盖不满足准则。

`artifact_id=project-deliverable-charter`；`profile_id=project-deliverable-charter-default`；`view_id=v-project-deliverable-charter-default`。完整表见生成索引（历史材料已清理）。

## 修改与反例

修改：补齐APP-12且四项准则都得到验证，仍未取得业务负责人接受。结果：准则已满足但状态仍awaiting-acceptance，不能自动accepted。

反例：覆盖11/12却标全部准则通过。结果：criterion-result-contradiction。

## 质量与追溯

- 文档与软件可有不同验收流程，不复制时长为TOGAF要求
- 生成、移交、评审与接受是不同状态
- 一项未满足准则不能被其他已满足项的数量抵消

执行证据（历史材料已清理）分别记录模型、生成、修改、反例及表内表达。表格不进行图形视觉验收。工程执行不能替代业务审批和独立业务审查。
