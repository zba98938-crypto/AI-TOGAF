# 阶段边界与项目收尾记录

是否继续、修改或终止阶段/项目，责任与成果是否可交接？

依据：G188 §3.5.1–3.6.3。字段结构与状态编码是项目操作规范，原始指南不随运行读取。

## 输入与缺口

范围、五维语境、所用目标与交付物版本；原始计划/访谈/验收/估算及来源ID；组织授权和容差规则；缺失时不代推。关键依据未知时给候选表、受影响ID与责任；不编造权重、阈值、估算、批准或实际完成。

## 字段语义

| 字段 | 含义 |
|---|---|
| name | 收尾/边界记录 |
| closure_kind | stage-boundary或project-closure |
| closure_reason | 完成或提前终止及依据 |
| products | 产品验收状态与未完成处置 |
| performance | 计划/实际时间成本质量范围风险收益；不合并成单分 |
| risks_issues | 风险问题剩余责任和处置 |
| handover | 接收方与足以开展后续工作的条件 |
| next_stage | 下一阶段计划或不适用 |
| authority | 决定继续/变更/终止的监督机构 |
| decision | 建议与批准分开 |
| evidence_refs | 材料ID |
| follow_up | 所需补证、变更或资源释放条件 |

## 分析步骤

1. 区分阶段边界、成功完成和提前终止
2. 核对所有产品状态及验收/撤销/移交去向
3. 比较计划/实际并保留容差未知
4. 提交剩余风险、项目影响与下一阶段或关闭建议
5. 监督机构决定并记录正式接受，之后才能释放/重新授权资源

### 阶段边界报告

原始材料（历史材料已清理）组 `stage-close`。阶段实际比计划多1天8小时，但容差未知不能断言越权；未接受说明表阻断完成型收尾。

`artifact_id=project-stage-closure-record`；`profile_id=project-stage-closure-record-stage`；`view_id=v-project-stage-closure-record-stage`。完整表见生成索引（历史材料已清理）。

### 项目收尾建议

原始材料（历史材料已清理）组 `project-close`。商业论证失效允许提出提前终止；不要求把所有未完成产品虚假标已接受，但必须明确去向、风险移交与授权。

`artifact_id=project-stage-closure-record`；`profile_id=project-stage-closure-record-project`；`view_id=v-project-stage-closure-record-project`。完整表见生成索引（历史材料已清理）。

## 修改与反例

修改：说明表修订获接受并批准下一阶段；项目终止获发起人接受。结果：阶段可关闭并另行授权下一阶段；项目按终止结案，保持未交付目标事实。

反例：未接受产品且无终止理由就宣布completed。结果：closure-products-not-accepted。

## 质量与追溯

- 阶段产品验收、边界决策、下一阶段授权是不同事实
- 商业论证失效可以提前终止，不能假装全部产品成功交付
- 计划/实际偏差不自动证明超过未给出的容差

执行证据（历史材料已清理）分别记录模型、生成、修改、反例及表内表达。表格不进行图形视觉验收。工程执行不能替代业务审批和独立业务审查。
