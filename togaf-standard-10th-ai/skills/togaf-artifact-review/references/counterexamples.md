# togaf-artifact-review 反例集

以下保留历史反例输入与原登记码，便于兼容追查；未绑定输入适配、适用条件与执行器，全部标为人工复核。
历史 `expected` 不是已执行机器断言；不能凭码名存在、关键词或文档生成声称反例已被拒绝。真实机器检查见checks.md。

## 工作产品反例

| 工作产品 | 错误输入 | 历史声明码（人工复核，非机器结论） | 为什么不通过 | 原始表述 |
| --- | --- | --- | --- | --- |
| `architecture-acceptance-criteria` | 对「架构成果验收准则」给出：工件不要求各自成为独立文档，数量不是验收目标 | `missing-evidence` | 工件不要求各自成为独立文档，数量不是验收目标 | — |
| `sustainability-review-canvas` | 对「可持续性架构评审画布」给出：图3-14存在数值疑点，应保留来源值与差异，不能强行消解 | `missing-evidence` | 图3-14存在数值疑点，应保留来源值与差异，不能强行消解 | — |
| `viewpoint-library` | 只有图名“数据流图”，无关注点/所需信息 | `missing-evidence` | 报告viewpoint-information-gap，不计完成视角 | 报告viewpoint-information-gap，不计完成视角 |
| `architecture-governance-checklist` | 目标九问只给八项；或实施Q1=yes仍按个人偏好判失败 | `missing-evidence` | 缺项被拒绝；合理解释路径保持合规 | 缺项被拒绝；合理解释路径保持合规 |
| `non-compliance-disposition` | 临时豁免没有到期日或复评责任 | `missing-evidence` | waiver-needs-expiry-review-owner拒绝完成 | waiver-needs-expiry-review-owner拒绝完成 |
| `architecture-description-formality-review` | 对「架构描述充分性与正式度评审」给出：形式规范不证明内容充分 | `missing-evidence` | 形式规范不证明内容充分 | — |
| `project-stage-closure-record` | 未接受产品且无终止理由就宣布completed | `closure-products-not-accepted` |  | — |
| `project-deliverable-charter` | 覆盖11/12却标全部准则通过 | `criterion-result-contradiction` |  | — |

## 工作产品修改示例

| 工作产品 | 变更 | 预期后果 |
| --- | --- | --- |
| `architecture-acceptance-criteria` | 在「架构成果验收准则」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `sustainability-review-canvas` | 在「可持续性架构评审画布」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `viewpoint-library` | 新增客户负责人关注签收争议处理 | 增加争议关注点、证据链信息和专门视角；旧三项不自动覆盖 |
| `architecture-governance-checklist` | 实施样本由41秒改为93秒，Q1=no；Q2–6=yes，Q7=unknown | 从合规转为待利益相关者处置批准，不自动豁免 |
| `non-compliance-disposition` | 把建议改为强制执行，计划10工作日修复 | 新增纠偏验证任务，豁免期限不再充当授权；目标60秒保持 |
| `architecture-description-formality-review` | 在「架构描述充分性与正式度评审」的范围内新增或修改一项，检查下游是否随之变化 | 受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用 |
| `project-stage-closure-record` | 说明表修订获接受并批准下一阶段；项目终止获发起人接受 | 阶段可关闭并另行授权下一阶段；项目按终止结案，保持未交付目标事实 |
| `project-deliverable-charter` | 补齐APP-12且四项准则都得到验证，仍未取得业务负责人接受 | 准则已满足但状态仍awaiting-acceptance，不能自动accepted |

## 方法反例

| 方法 | 错误输入 | 历史声明码（人工复核，非机器结论） | 为什么不通过 | 原始表述 |
| --- | --- | --- | --- | --- |
| `sustainability-option-review` | 执行「可持续性方案评审」时跳过或误做：原图印刷矛盾保留证据，不静默改数 | `missing-evidence` | 原图印刷矛盾保留证据，不静默改数 | — |
| `architecture-description-formality-review-method` | 执行「架构描述充分性与正式度评审分析方法」时跳过或误做：充分性与正式度各有独立依据 | `missing-evidence` | 充分性与正式度各有独立依据 | — |

## 判定说明

- 历史码可能只是旧注册表声明，不能证明对应叙述由校验器实际拒绝。
- 需将具体结构化输入与显式check_specs绑定执行后，才可补充机器反例证据；本表不假定已完成。
- 通过反例测试不等于业务正确，只说明错误输入没有被放行。
