# 架构合同（Architecture Contract）

ID：`architecture-contract` · 主责：[togaf-implementation-governance](../../../togaf-implementation-governance/SKILL.md) · 常用 ADM：G。

名称与用途现已逐项绑定本地C220；下列组装结构仍为项目约定。

## 输入与内容

输入工作范围、五维语境、关注点、模型和制品版本、来源及真实评审状态。每章回答问题，不能只复制标题。

- **缔约方与范围**：明确业务、架构、实施各方及交付边界。
- **架构义务**：引用适用架构、需求及实现责任。
- **验收与证据**：定义合规检查、证据及时间。
- **偏离与变更**：规定例外、变更、升级和争议处理。
- **状态与签署**：记录草案、决策方和真实签署状态。

## 组装与引用

- [合同/度量目录](../artifacts/contract-measure-catalog.md)。
- [需求目录](../artifacts/requirements-catalog.md)。

以上为项目推荐支撑制品，按决策需要裁剪并说明理由。引用原制品及模型版本，保留相对链接和对象 ID；JSON 保存章节、视图与实体引用。生成器组装已完成分析的 sections，不会自行创造业务结论。

G186 附录 D 给出面向解决方案交付团队的架构契约模板（解决方案交付笔记本）：解决方案摘要、规格摘要（需求/规格配对、风险/控制配对）和仅供参考的架构描述摘要。需要按此模板沟通时，选用 [解决方案交付笔记本](../capability-addenda/solution-delivery-notebook.md)（`solution-delivery-notebook-default`），它可选绑定到本交付物的“架构义务”“缔约方与范围”两章；冲突待办与豁免可选用 [产品边界与企业约束登记](../capability-addenda/product-constraint-register.md) 绑定到“偏离与变更”。上面五章结构仍是项目约定，两者都不替代 C220 正式定义。

## 评审与不足

- 不伪造签署或法律效力。
- 验收责任和证据可定位。
- 缺输入记录 gap、假设及待决项；不虚构签署、预算承诺或实施证据。
- 所有引用可达，结论可回溯到模型、需求及来源。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际组装结果（历史材料已清理）。以下为完整案例中的组装输入，实体和视图见 案例模型（历史材料已清理）。

```json
{
  "id": "d-architecture-contract",
  "deliverable_id": "architecture-contract",
  "title": "架构合同 · 星河零售虚构案例",
  "view_ids": [
    "v-contract-measure-catalog",
    "v-requirements-catalog"
  ],
  "entity_ids": [
    "req-accuracy",
    "req-privacy",
    "contract",
    "decision-stock",
    "control",
    "decision"
  ],
  "sections": {
    "缔约方与范围": "业务发起方、架构负责人和实施负责人拟就订单确认范围建立约定。",
    "架构义务": "实施应满足库存一致性及最小访问需求，并维护接口兼容。",
    "验收与证据": "试运行前完成业务场景、并发校验、访问拒绝与回退演练；证据待提供。",
    "偏离与变更": "偏离由架构负责人分析风险，业务发起方决定处置；期限待协商。",
    "状态与签署": "全部为候选草案，无真实签署。"
  },
  "decision_status": "candidate"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --deliverable architecture-contract --out ./architecture-output --render
```

## 来源

G248, G186，详见 [来源分析](../source-analysis.md)。基础标准定义及限定条件见下方来源绑定；生成结构为项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-source-description`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 4.2.2. Architecture Contract](../../corpus/fundamental/analysis/05-architecture-content.md#tag_04_02_02)
  - 概念：架构契约的条目标题。
  - 边界：目的及内容分别在子节，无独立额外要求。
