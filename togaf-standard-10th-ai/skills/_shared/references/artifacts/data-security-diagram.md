# 数据安全图（Data Security Diagram）

ID：`data-security-diagram` · 主责：[togaf-security-risk](../../../togaf-security-risk/SKILL.md) · 原文域：数据。

**定义边界**：名称与域来自 G248 附录 A。下列输入、字段、分析和验收是项目操作约定；尚未取得 C220 正文进行逐项正式定义核验，不宣称官方强制最小字段。

## 决策与受众

敏感数据跨越哪些信任边界，由哪些控制保护？

主要受众：业务风险责任方、数据责任方、控制验证方。输出需回应已确认关注点，不因清单存在就强制生成。

## 输入与属性

必需：五维语境、决策问题、领域对象及证据或明确候选假设。按对象类型收集适用字段：

- `data_entity`：`classification`、`owner`、`purpose`。
- `data_component`：`classification`、`owner`、`purpose`。
- `actor`：`owner`。
- `control`：`classification`、`owner`、`purpose`。
- `trust_zone`：`classification`、`owner`、`purpose`。

可选：既有模型、版本差异、度量、质量要求和法规约束。关键缺口影响结论时先询问，局部不足写入 gaps 并保持 assumed/uncertain。确实不适用的字段说明理由；不以默认数值冒充事实。

## 关系与表示语义

- `stored_in`：数据由组件存储。data_entity → data_component。
- `protected_by`：数据由控制保护。data_entity, data_component → control。
- `authorized_for`：经证据支持的访问授权。actor → data_entity。
- `crosses_boundary`：数据处理跨信任边界。data_component → trust_zone。

## 分析与构造

1. 分类数据与处理目的。
2. 识别身份、边界、存储和传输路径。
3. 将控制关联到风险及验证证据。

按 [共享规则](../modeling-rules.md) 复用稳定 ID 和证据，区分对象、关系、版本及演进状态。修改需要比较属性和关系，不只比较框数量。

## 输出

Markdown 回答决策并展示目录、矩阵或视图；JSON 保存对象、关系、来源和模型版本。表示法：`flowchart`。提供可编辑 Mermaid 或 SVG 源、布局说明、独立 SVG 和 PNG。图例解释箭头、区域和颜色；简化关系图不宣称完整 ArchiMate/UML/BPMN。

## 质量与常见误读

- 画锁图标不构成控制设计。
- 角色使用关系不自动表示授权。
- 五维独立；源图解释不能直接成为项目事实，候选不等于批准。
- 对照相关目录、矩阵和图的共享对象与关系方向；检查证据、假设和缺口。
- 图形需检查中文标签、箭头、边界和可读性；脚本检查不能替代业务验证。

## 复用与追溯

支撑交付物：[合规评估](../deliverables/compliance-assessment.md)。

相关制品：[组织/参与者目录](organization-actor-catalog.md)、[流程/事件/控制/产品目录](process-event-control-product-catalog.md)、[数据实体/数据组件目录](data-entity-data-component-catalog.md)、[参与者/角色矩阵](actor-role-matrix.md)、[数据实体/业务功能矩阵](data-entity-business-function-matrix.md)、[应用/数据矩阵](application-data-matrix.md)。跨制品复用实体 ID、需求及构建块追溯，不复制独立冲突对象。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际生成结果（历史材料已清理） 包含模型对象、关系、分析、图例和证据。以下为可运行输入的视图定义；对象和关系可在 完整案例模型（历史材料已清理） 按 ID 定位。

```json
{
  "id": "v-data-security-diagram",
  "artifact_id": "data-security-diagram",
  "title": "数据安全图 · 星河零售虚构案例",
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
    "data-customer",
    "control",
    "actor-picker",
    "component-order",
    "trust"
  ],
  "relationship_ids": [
    "data-protect",
    "data-authorize",
    "data-boundary"
  ],
  "analysis": "拣货角色仅为履约目的读取必要联系信息；控制需要覆盖允许和拒绝路径及审计，示例并未证明控制有效。",
  "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
  "allow_mixed_evolution": false
}
```

生成单项：

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --artifact data-security-diagram --out ./architecture-output --render
```

TOGAF_SKILLS 由使用者设为技能集合根目录，非机器固定路径。

## 来源

G248 附录 A，源行 571；方法指南：G248, G152, G234。见 [来源分析](../source-analysis.md)、[来源指纹](../../sources.json) 与 [图表解释索引](../figure-index.json)。行号以原项目版本为准；图表不确定性必须保留，操作规则是项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-purpose-title`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 3.6.5.7. Data Security Diagram](../../corpus/fundamental/analysis/05-architecture-content.md#tag_03_06_04_07)
  - 概念：数据安全图/矩阵表示角色、组织、应用访问数据及保护措施。
  - 逻辑：访问与安全措施对应数据边界。
  - 决策：核查访问方、外部范围及措施证据。
  - 边界：表达访问不自动证明实际法律合规或授权执行成功。
