# 项目经验记录与教训报告

哪些观察应成为后续项目和EA能力改进的输入？

依据：G188 §3.1.3、§3.6.3示例3-37及注释2。字段结构与状态编码是项目操作规范，原始指南不随运行读取。

## 输入与缺口

范围、五维语境、所用目标与交付物版本；原始计划/访谈/验收/估算及来源ID；组织授权和容差规则；缺失时不代推。关键依据未知时给候选表、受影响ID与责任；不编造权重、阈值、估算、批准或实际完成。

## 字段语义

| 字段 | 含义 |
|---|---|
| name | 经验事项 |
| record_kind | ongoing-log或final-lessons-report |
| expected | 当初计划或假设 |
| actual | 实际观察 |
| difference | 具体差异，不把因果当事实 |
| cause_hypothesis | 已证实原因或待验证假设 |
| evidence_refs | 材料ID/访谈/记录 |
| impact | 对项目的实际影响 |
| recommendation | 下一项目可执行改进 |
| owner | 负责采取改进的人 |
| verification | 如何验证建议有效 |
| status | 观察/原因待证/建议待试点等 |
| follow_up_reference | 能力变更请求或后续项目引用 |

## 分析步骤

1. 持续日志从以往经验和本项目观察开始
2. AAR分别记录预期/实际/原因/改进
3. 区别证据支持原因与待验证假设
4. 收尾筛选关键教训并指定改进责任与验证
5. 将可执行能力改进形成H变更请求并向后续项目传递

### 持续经验记录

原始材料（历史材料已清理）组 `lessons`。按AAR比较预期、实际、差异原因和改进；日志连续保留事实，最终报告筛选可行动教训。建议尚未经过试点，不宣称已消除延期。

`artifact_id=project-learning-record`；`profile_id=project-learning-record-log`；`view_id=v-project-learning-record-log`。完整表见生成索引（历史材料已清理）。

### 项目最终经验教训

原始材料（历史材料已清理）组 `lessons`。按AAR比较预期、实际、差异原因和改进；日志连续保留事实，最终报告筛选可行动教训。建议尚未经过试点，不宣称已消除延期。

`artifact_id=project-learning-record`；`profile_id=project-learning-record-report`；`view_id=v-project-learning-record-report`。完整表见生成索引（历史材料已清理）。

## 修改与反例

修改：下一项目采用模板后同范围清单确认8天、返工1次。结果：记录试点结果和可比性，改进证据增强但不能由单例证明普遍因果。

反例：仅写“沟通不好，要加强沟通”无预期实际和证据。结果：learning-evidence-gap。

## 质量与追溯

- 持续Lessons Log与最终Lessons Learned/Report不是同一个状态
- 参加复盘或提出建议不等于改进已验证
- 无原计划/实绩不能编造差异；未经验证原因不能写成确定事实

执行证据（历史材料已清理）分别记录模型、生成、修改、反例及表内表达。表格不进行图形视觉验收。工程执行不能替代业务审批和独立业务审查。
