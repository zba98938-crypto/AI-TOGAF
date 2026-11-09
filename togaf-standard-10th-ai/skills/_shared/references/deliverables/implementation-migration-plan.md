# 实施与迁移计划（Implementation and Migration Plan）

ID：`implementation-migration-plan` · 主责：[togaf-migration-roadmap](../../../togaf-migration-roadmap/SKILL.md) · 常用 ADM：F。

名称与用途现已逐项绑定本地C220；下列组装结构仍为项目约定。

## 输入与内容

输入工作范围、五维语境、关注点、模型和制品版本、来源及真实评审状态。每章回答问题，不能只复制标题。

- **实施安排**：明确工作包交付、责任、资源和成本依据。
- **依赖与排期**：协调前置、并行和外部承诺。
- **迁移与运营**：规定数据、应用、平台切换和可运营过渡。
- **验收与回退**：定义准入、核对、退出和恢复条件。

## 组装与引用

- [应用迁移图](../artifacts/application-migration-diagram.md)。
- [数据迁移图](../artifacts/data-migration-diagram.md)。

以上为项目推荐支撑制品，按决策需要裁剪并说明理由。引用原制品及模型版本，保留相对链接和对象 ID；JSON 保存章节、视图与实体引用。生成器组装已完成分析的 sections，不会自行创造业务结论。

## 评审与不足

- 估算保留假设与区间。
- 不可只给时间轴而缺少切换条件。
- 缺输入记录 gap、假设及待决项；不虚构签署、预算承诺或实施证据。
- 所有引用可达，结论可回溯到模型、需求及来源。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际组装结果（历史材料已清理）。以下为完整案例中的组装输入，实体和视图见 案例模型（历史材料已清理）。

```json
{
  "id": "d-implementation-migration-plan",
  "deliverable_id": "implementation-migration-plan",
  "title": "实施与迁移计划 · 星河零售虚构案例",
  "view_ids": [
    "v-application-migration-diagram",
    "v-data-migration-diagram"
  ],
  "entity_ids": [
    "wp-data",
    "wp-app",
    "risk",
    "milestone",
    "transition"
  ],
  "sections": {
    "实施安排": "wp-data 由数据负责人牵头，wp-app 由实施负责人牵头；资源成本待确认。",
    "依赖与排期": "示例依赖为数据映射和契约先于应用切换，15/20 日仅演示安排。",
    "迁移与运营": "双运行保留旧入口，冻结窗口内核对金额和订单，运营由履约负责人负责。",
    "验收与回退": "准入需场景和控制验证；核对失败保持旧系统接单，撤销本次切换。"
  },
  "decision_status": "candidate"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --deliverable implementation-migration-plan --out ./architecture-output --render
```

## 来源

G248, G186, G188, G233，详见 [来源分析](../source-analysis.md)。基础标准定义及限定条件见下方来源绑定；生成结构为项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-source-description`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 4.2.14. Implementation and Migration Plan](../../corpus/fundamental/analysis/05-architecture-content.md#tag_04_02_14)
  - 概念：实施和迁移计划的条目标题。
  - 边界：可执行项目安排和内容在子节。
