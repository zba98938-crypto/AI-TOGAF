# 变更请求（Change Request）

ID：`change-request` · 主责：[togaf-change-value](../../../togaf-change-value/SKILL.md) · 常用 ADM：G H。

名称与用途现已逐项绑定本地C220；下列组装结构仍为项目约定。

## 输入与内容

输入工作范围、五维语境、关注点、模型和制品版本、来源及真实评审状态。每章回答问题，不能只复制标题。

- **变更事实**：记录提出方、日期、原因和变更内容。
- **影响与选项**：引用需求影响、成本、风险和替代。
- **处置与责任**：登记决策方、候选处置和真实审批状态。
- **执行与回溯**：说明执行条件、版本与验证结果。

## 组装与引用

- [需求影响评估](../artifacts/requirements-impact-assessment.md)。

以上为项目推荐支撑制品，按决策需要裁剪并说明理由。引用原制品及模型版本，保留相对链接和对象 ID；JSON 保存章节、视图与实体引用。生成器组装已完成分析的 sections，不会自行创造业务结论。

## 评审与不足

- 请求不等于批准。
- 影响结论可追溯。
- 缺输入记录 gap、假设及待决项；不虚构签署、预算承诺或实施证据。
- 所有引用可达，结论可回溯到模型、需求及来源。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际组装结果（历史材料已清理）。以下为完整案例中的组装输入，实体和视图见 案例模型（历史材料已清理）。

```json
{
  "id": "d-change-request",
  "deliverable_id": "change-request",
  "title": "变更请求 · 星河零售虚构案例",
  "view_ids": [
    "v-requirements-impact-assessment"
  ],
  "entity_ids": [
    "req-accuracy",
    "req-privacy",
    "decision-stock",
    "change",
    "decision"
  ],
  "sections": {
    "变更事实": "安全负责人拟限制履约角色读取字段，以降低客户信息越权风险。",
    "影响与选项": "影响隐私需求、接口字段、访问控制和测试；候选成本尚未估算。",
    "处置与责任": "建议确认最小字段范围，业务与数据负责人尚未批准。",
    "执行与回溯": "批准后更新版本并运行允许/拒绝测试；当前没有实施结果。"
  },
  "decision_status": "candidate"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --deliverable change-request --out ./architecture-output --render
```

## 来源

G248, G186, G188，详见 [来源分析](../source-analysis.md)。基础标准定义及限定条件见下方来源绑定；生成结构为项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-source-description`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 4.2.11. Change Request](../../corpus/fundamental/analysis/05-architecture-content.md#tag_04_02_11)
  - 概念：变更请求的条目标题。
  - 边界：触发和内容在子节。
