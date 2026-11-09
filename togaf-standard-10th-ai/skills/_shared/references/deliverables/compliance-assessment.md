# 合规评估（Compliance Assessment）

ID：`compliance-assessment` · 主责：[togaf-implementation-governance](../../../togaf-implementation-governance/SKILL.md) · 常用 ADM：G。

名称与用途现已逐项绑定本地C220；下列组装结构仍为项目约定。

## 输入与内容

输入工作范围、五维语境、关注点、模型和制品版本、来源及真实评审状态。每章回答问题，不能只复制标题。

- **评估范围**：界定适用架构版本、要求和实施范围。
- **证据与结果**：逐项列出满足、偏离或证据不足。
- **风险与处置**：关联例外、补救、责任与期限。
- **评审结论**：记录评审者及实际批准状态。

## 组装与引用

- [需求目录](../artifacts/requirements-catalog.md)。
- [数据安全图](../artifacts/data-security-diagram.md)。

以上为项目推荐支撑制品，按决策需要裁剪并说明理由。引用原制品及模型版本，保留相对链接和对象 ID；JSON 保存章节、视图与实体引用。生成器组装已完成分析的 sections，不会自行创造业务结论。

## 评审与不足

- 无证据不能判定合规。
- 自动检查不替代业务审批。
- 缺输入记录 gap、假设及待决项；不虚构签署、预算承诺或实施证据。
- 所有引用可达，结论可回溯到模型、需求及来源。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际组装结果（历史材料已清理）。以下为完整案例中的组装输入，实体和视图见 案例模型（历史材料已清理）。

```json
{
  "id": "d-compliance-assessment",
  "deliverable_id": "compliance-assessment",
  "title": "合规评估 · 星河零售虚构案例",
  "view_ids": [
    "v-requirements-catalog",
    "v-data-security-diagram"
  ],
  "entity_ids": [
    "req-accuracy",
    "req-privacy",
    "decision-stock",
    "control",
    "decision",
    "evidence"
  ],
  "sections": {
    "评估范围": "评估候选订单应用对 req-accuracy 与 req-privacy 的满足情况。",
    "证据与结果": "仅有设计和测试计划，所有实施有效性结论均为证据不足。",
    "风险与处置": "越权风险需最小权限与审计验证，补救负责人建议为安全及实施负责人。",
    "评审结论": "未完成正式评审，不出具已合规结论。"
  },
  "decision_status": "candidate"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --deliverable compliance-assessment --out ./architecture-output --render
```

## 来源

G248, G186, G152，详见 [来源分析](../source-analysis.md)。基础标准定义及限定条件见下方来源绑定；生成结构为项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-source-description`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 4.2.13. Compliance Assessment](../../corpus/fundamental/analysis/05-architecture-content.md#tag_04_02_13)
  - 概念：符合性评估的条目标题。
  - 边界：目的和内容在子节。
