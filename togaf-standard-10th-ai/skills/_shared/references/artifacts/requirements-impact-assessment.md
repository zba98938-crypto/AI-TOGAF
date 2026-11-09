# 需求影响评估（Requirements Impact Assessment）

ID：`requirements-impact-assessment` · 主责：[togaf-requirements](../../../togaf-requirements/SKILL.md) · 原文域：通用。

**定义边界**：名称与域来自 G248 附录 A。下列输入、字段、分析和验收是项目操作约定；尚未取得 C220 正文进行逐项正式定义核验，不宣称官方强制最小字段。

## 决策与受众

需求变化影响哪些架构资产、成本、风险与决策？

主要受众：需求责任方、业务验收方、架构与实施团队。输出需回应已确认关注点，不因清单存在就强制生成。

## 输入与属性

必需：五维语境、决策问题、领域对象及证据或明确候选假设。按对象类型收集适用字段：

- `requirement`：`owner`。
- `change_request`：`reason`、`impact`、`severity`、`owner`、`decision`。
- `risk`：`impact`、`owner`。
- `work_package`：`owner`。

可选：既有模型、版本差异、度量、质量要求和法规约束。关键缺口影响结论时先询问，局部不足写入 gaps 并保持 assumed/uncertain。确实不适用的字段说明理由；不以默认数值冒充事实。

## 关系与表示语义

- `changes`：变更修改需求。change_request → requirement。
- `traces_to`：显式追溯，具体理由记录在 label。* → *。
- `affects`：有证据或待验证的影响。requirement, change_request → *。

## 分析与构造

1. 记录变更前后需求和理由。
2. 沿显式追溯关系分析影响并标记推测。
3. 给出处置选项、责任和待决问题。

按 [共享规则](../modeling-rules.md) 复用稳定 ID 和证据，区分对象、关系、版本及演进状态。修改需要比较属性和关系，不只比较框数量。

## 输出

Markdown 回答决策并展示目录、矩阵或视图；JSON 保存对象、关系、来源和模型版本。表示法：`impact-register`。

## 质量与常见误读

- 可达性不自动等于实际影响。
- 影响分析不自动批准变更。
- 五维独立；源图解释不能直接成为项目事实，候选不等于批准。
- 对照相关目录、矩阵和图的共享对象与关系方向；检查证据、假设和缺口。
- 图形需检查中文标签、箭头、边界和可读性；脚本检查不能替代业务验证。

## 复用与追溯

支撑交付物：[变更请求](../deliverables/change-request.md)、[需求影响评估](../deliverables/requirements-impact-assessment.md)。

相关制品：[需求目录](requirements-catalog.md)、[收益图](benefits-diagram.md)、[应用迁移图](application-migration-diagram.md)。跨制品复用实体 ID、需求及构建块追溯，不复制独立冲突对象。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际生成结果（历史材料已清理） 包含模型对象、关系、分析、图例和证据。以下为可运行输入的视图定义；对象和关系可在 完整案例模型（历史材料已清理） 按 ID 定位。

```json
{
  "id": "v-requirements-impact-assessment",
  "artifact_id": "requirements-impact-assessment",
  "title": "需求影响评估 · 星河零售虚构案例",
  "context": {
    "domains": [
      "business",
      "data",
      "application",
      "technology"
    ],
    "landscape": "segment",
    "purpose": "project",
    "abstraction": "logical",
    "evolution": "target"
  },
  "entity_ids": [
    "req-accuracy",
    "req-privacy",
    "wp-data",
    "wp-app",
    "risk",
    "change"
  ],
  "relationship_ids": [
    "req-risk",
    "change-req",
    "req-affect"
  ],
  "analysis": "访问范围变更首先影响隐私需求及订单迁移验收；沿控制和应用追溯进一步确认，不能仅凭图可达给出确定成本。",
  "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
  "allow_mixed_evolution": false
}
```

生成单项：

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --artifact requirements-impact-assessment --out ./architecture-output
```

TOGAF_SKILLS 由使用者设为技能集合根目录，非机器固定路径。

## 来源

G248 附录 A，源行 503；方法指南：G248, G186, G152, G188。见 [来源分析](../source-analysis.md)、[来源指纹](../../sources.json) 与 [图表解释索引](../figure-index.json)。行号以原项目版本为准；图表不确定性必须保留，操作规则是项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`supporting-concept-not-same-named-artifact`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 4.2.18. Requirements Impact Assessment](../../corpus/fundamental/analysis/05-architecture-content.md#tag_04_02_18)
  - 概念：需求影响评估的条目标题。
  - 边界：持续评估目的和内容在子节。
