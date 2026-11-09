# 架构路线图（Architecture Roadmaps）

ID：`architecture-roadmaps` · 主责：[togaf-migration-roadmap](../../../togaf-migration-roadmap/SKILL.md) · 常用 ADM：E F H。

名称与用途现已逐项绑定本地C220；下列组装结构仍为项目约定。

## 输入与内容

输入工作范围、五维语境、关注点、模型和制品版本、来源及真实评审状态。每章回答问题，不能只复制标题。

- **变革目标**：说明业务成果和衡量方式。
- **工作包与依赖**：引用跨域差距及有向依赖。
- **过渡与里程碑**：定义可运营状态和进入退出条件。
- **排序与决策**：说明价值、风险、资源及批准情况。

## 组装与引用

- [应用迁移图](../artifacts/application-migration-diagram.md)。
- [数据迁移图](../artifacts/data-migration-diagram.md)。
- [收益图](../artifacts/benefits-diagram.md)。

以上为项目推荐支撑制品，按决策需要裁剪并说明理由。引用原制品及模型版本，保留相对链接和对象 ID；JSON 保存章节、视图与实体引用。生成器组装已完成分析的 sections，不会自行创造业务结论。

## 评审与不足

- 依赖无未解释环。
- 过渡状态有运营和回退考虑。
- 缺输入记录 gap、假设及待决项；不虚构签署、预算承诺或实施证据。
- 所有引用可达，结论可回溯到模型、需求及来源。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际组装结果（历史材料已清理）。以下为完整案例中的组装输入，实体和视图见 案例模型（历史材料已清理）。

```json
{
  "id": "d-architecture-roadmaps",
  "deliverable_id": "architecture-roadmaps",
  "title": "架构路线图 · 星河零售虚构案例",
  "view_ids": [
    "v-application-migration-diagram",
    "v-data-migration-diagram",
    "v-benefits-diagram"
  ],
  "entity_ids": [
    "wp-data",
    "wp-app",
    "benefit",
    "milestone",
    "transition"
  ],
  "sections": {
    "变革目标": "目标为缩短确认时间且维持库存准确性，收益因果仍是假设。",
    "工作包与依赖": "wp-data 完成数据与契约，wp-app 依赖其完成后迁移应用。",
    "过渡与里程碑": "过渡为双运行与核对；试运行准入要求可运营、访问控制和回退演练通过。",
    "排序与决策": "优先处理数据契约，示例 15/20 日为未承诺估算，实际资源预算待确认。"
  },
  "decision_status": "candidate"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --deliverable architecture-roadmaps --out ./architecture-output --render
```

## 来源

G248, G186, G233，详见 [来源分析](../source-analysis.md)。基础标准定义及限定条件见下方来源绑定；生成结构为项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-source-description`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 4.2.7. Architecture Roadmap](../../corpus/fundamental/analysis/05-architecture-content.md#tag_04_02_07)
  - 概念：架构路线图的条目标题。
  - 边界：目的和内容分别在子节。
