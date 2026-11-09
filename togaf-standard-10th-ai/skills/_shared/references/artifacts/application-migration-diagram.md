# 应用迁移图（Application Migration Diagram）

ID：`application-migration-diagram` · 主责：[togaf-migration-roadmap](../../../togaf-migration-roadmap/SKILL.md) · 原文域：应用。

**定义边界**：名称与域来自 G248 附录 A。下列输入、字段、分析和验收是项目操作约定；尚未取得 C220 正文进行逐项正式定义核验，不宣称官方强制最小字段。

## 决策与受众

应用如何从现状经可运营过渡到目标？

主要受众：组合及项目负责人、业务运营方、实施团队。输出需回应已确认关注点，不因清单存在就强制生成。

## 输入与属性

必需：五维语境、决策问题、领域对象及证据或明确候选假设。按对象类型收集适用字段：

- `application`：`lifecycle`。
- `work_package`：名称、边界、来源及对象类型。

可选：既有模型、版本差异、度量、质量要求和法规约束。关键缺口影响结论时先询问，局部不足写入 gaps 并保持 assumed/uncertain。确实不适用的字段说明理由；不以默认数值冒充事实。

## 关系与表示语义

- `replaced_by`：现有应用被另一应用替换。application → application。
- `migrated_by`：应用由工作包迁移。application → work_package。

附加要求：`{"application": ["concept_id", "evolution"]}`。

## 分析与构造

1. 以稳定概念标识对齐现状目标应用。
2. 标记新增、替换、保留及退役。
3. 为过渡期双运行和回退设置条件。

按 [共享规则](../modeling-rules.md) 复用稳定 ID 和证据，区分对象、关系、版本及演进状态。修改需要比较属性和关系，不只比较框数量。

## 输出

Markdown 回答决策并展示目录、矩阵或视图；JSON 保存对象、关系、来源和模型版本。表示法：`flowchart`。提供可编辑 Mermaid 或 SVG 源、布局说明、独立 SVG 和 PNG。图例解释箭头、区域和颜色；简化关系图不宣称完整 ArchiMate/UML/BPMN。

## 质量与常见误读

- 目标不是已实现。
- 应用更名不必然代表新系统。
- 五维独立；源图解释不能直接成为项目事实，候选不等于批准。
- 对照相关目录、矩阵和图的共享对象与关系方向；检查证据、假设和缺口。
- 图形需检查中文标签、箭头、边界和可读性；脚本检查不能替代业务验证。

## 复用与追溯

支撑交付物：[架构路线图](../deliverables/architecture-roadmaps.md)、[实施与迁移计划](../deliverables/implementation-migration-plan.md)。

相关制品：[应用组合目录](application-portfolio-catalog.md)、[应用/功能矩阵](application-function-matrix.md)、[应用/组织矩阵](application-organization-matrix.md)、[角色/应用矩阵](role-application-matrix.md)、[应用交互矩阵](application-interaction-matrix.md)、[应用/数据矩阵](application-data-matrix.md)。跨制品复用实体 ID、需求及构建块追溯，不复制独立冲突对象。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际生成结果（历史材料已清理） 包含模型对象、关系、分析、图例和证据。以下为可运行输入的视图定义；对象和关系可在 完整案例模型（历史材料已清理） 按 ID 定位。

```json
{
  "id": "v-application-migration-diagram",
  "artifact_id": "application-migration-diagram",
  "title": "应用迁移图 · 星河零售虚构案例",
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
    "app-old",
    "app-oms",
    "wp-app"
  ],
  "relationship_ids": [
    "app-replaced",
    "app-migrated"
  ],
  "analysis": "现有单节点订单系统向目标订单应用演进。先完成数据与契约，再受控双运行、核对并切换；这是候选迁移设计。",
  "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
  "allow_mixed_evolution": true
}
```

生成单项：

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --artifact application-migration-diagram --out ./architecture-output --render
```

TOGAF_SKILLS 由使用者设为技能集合根目录，非机器固定路径。

## 来源

G248 附录 A，源行 550；方法指南：G248, G186, G248。见 [来源分析](../source-analysis.md)、[来源指纹](../../sources.json) 与 [图表解释索引](../figure-index.json)。行号以原项目版本为准；图表不确定性必须保留，操作规则是项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-purpose-title`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 3.6.6.13. Application Migration Diagram](../../corpus/fundamental/analysis/05-architecture-content.md#tag_03_06_05_13)
  - 概念：应用迁移图显示基线到目标应用组件和接口的阶段映射。
  - 逻辑：需识别临时应用、暂存区和并行运行等迁移基础设施。
  - 决策：核对每阶段映射及临时支持需求。
  - 边界：细化映射提高估算基础，不自动提供真实成本或迁移验收。
