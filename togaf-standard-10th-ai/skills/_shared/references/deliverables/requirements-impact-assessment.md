# 需求影响评估（Requirements Impact Assessment）

ID：`requirements-impact-assessment` · 主责：[togaf-requirements](../../../togaf-requirements/SKILL.md) · 常用 ADM：Requirements。

名称与用途现已逐项绑定本地C220；下列组装结构仍为项目约定。

## 输入与内容

输入工作范围、五维语境、关注点、模型和制品版本、来源及真实评审状态。每章回答问题，不能只复制标题。

- **变更与依据**：记录需求版本差异和变更原因。
- **影响清单**：列出受影响模型、制品、交付物和实现。
- **成本风险与选项**：区分证据影响和推测影响。
- **建议与决策**：提供处置方案、责任和未决项。

## 组装与引用

- [需求影响评估](../artifacts/requirements-impact-assessment.md)。

以上为项目推荐支撑制品，按决策需要裁剪并说明理由。引用原制品及模型版本，保留相对链接和对象 ID；JSON 保存章节、视图与实体引用。生成器组装已完成分析的 sections，不会自行创造业务结论。

与同名制品共享同一次需求影响分析，交付物展开影响和处置，不重复创建需求事实。

## 评审与不足

- 与同名制品共享分析不重复建模。
- 关系可达不等于确定影响。
- 缺输入记录 gap、假设及待决项；不虚构签署、预算承诺或实施证据。
- 所有引用可达，结论可回溯到模型、需求及来源。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际组装结果（历史材料已清理）。以下为完整案例中的组装输入，实体和视图见 案例模型（历史材料已清理）。

```json
{
  "id": "d-requirements-impact-assessment",
  "deliverable_id": "requirements-impact-assessment",
  "title": "需求影响评估 · 星河零售虚构案例",
  "view_ids": [
    "v-requirements-impact-assessment"
  ],
  "entity_ids": [
    "req-accuracy",
    "req-privacy",
    "wp-data",
    "wp-app",
    "risk",
    "change"
  ],
  "sections": {
    "变更与依据": "访问范围变更拟将履约字段限制为最小必要集合，当前仍为候选。",
    "影响清单": "影响隐私需求、数据安全视图、应用接口和 wp-app 验收。",
    "成本风险与选项": "图可达提供排查对象；实际实现成本、性能和合同影响仍需逐项确认。",
    "建议与决策": "建议数据和安全负责人确认字段，再由实施负责人估算并提交业务决策。"
  },
  "decision_status": "candidate"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --deliverable requirements-impact-assessment --out ./architecture-output --render
```

## 来源

G248, G186, G152，详见 [来源分析](../source-analysis.md)。基础标准定义及限定条件见下方来源绑定；生成结构为项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-source-description`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 4.2.18. Requirements Impact Assessment](../../corpus/fundamental/analysis/05-architecture-content.md#tag_04_02_18)
  - 概念：需求影响评估的条目标题。
  - 边界：持续评估目的和内容在子节。
