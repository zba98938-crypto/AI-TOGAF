# 参与者/角色矩阵（Actor/Role Matrix）

ID：`actor-role-matrix` · 主责：[togaf-organization-roles](../../../togaf-organization-roles/SKILL.md) · 原文域：业务。

**定义边界**：名称与域来自 G248 附录 A。下列输入、字段、分析和验收是项目操作约定；尚未取得 C220 正文进行逐项正式定义核验，不宣称官方强制最小字段。

## 决策与受众

哪些参与者承担哪些角色？

主要受众：组织及人力负责人、业务责任方、合作伙伴。输出需回应已确认关注点，不因清单存在就强制生成。

## 输入与属性

必需：五维语境、决策问题、领域对象及证据或明确候选假设。按对象类型收集适用字段：

- `actor`：名称、边界、来源及对象类型。
- `role`：名称、边界、来源及对象类型。

可选：既有模型、版本差异、度量、质量要求和法规约束。关键缺口影响结论时先询问，局部不足写入 gaps 并保持 assumed/uncertain。确实不适用的字段说明理由；不以默认数值冒充事实。

## 关系与表示语义

- `plays`：参与者承担角色。actor → role。

行：actor；列：role。模型关系从行到列。单元含义：参与者被分配到角色；允许代码：assigned；空白：未记录，不能直接解释为不存在。同一单元可有多个有依据的代码。

## 分析与构造

1. 列出参与者与角色。
2. 逐项确认角色分配。
3. 检查关键角色空缺与职责冲突。

按 [共享规则](../modeling-rules.md) 复用稳定 ID 和证据，区分对象、关系、版本及演进状态。修改需要比较属性和关系，不只比较框数量。

## 输出

Markdown 回答决策并展示目录、矩阵或视图；JSON 保存对象、关系、来源和模型版本。表示法：`table`。

## 质量与常见误读

- 分配关系不是 RACI 责任类型。
- 矩阵方向必须声明。
- 五维独立；源图解释不能直接成为项目事实，候选不等于批准。
- 对照相关目录、矩阵和图的共享对象与关系方向；检查证据、假设和缺口。
- 图形需检查中文标签、箭头、边界和可读性；脚本检查不能替代业务验证。

## 复用与追溯

支撑交付物：[企业架构组织模型](../deliverables/organization-model.md)。

相关制品：[组织/参与者目录](organization-actor-catalog.md)、[角色目录](role-catalog.md)、[角色/应用矩阵](role-application-matrix.md)、[应用与用户位置图](application-and-user-location-diagram.md)、[业务用例图](business-use-case-diagram.md)、[流程图](process-flow-diagram.md)。跨制品复用实体 ID、需求及构建块追溯，不复制独立冲突对象。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际生成结果（历史材料已清理） 包含模型对象、关系、分析、图例和证据。以下为可运行输入的视图定义；对象和关系可在 完整案例模型（历史材料已清理） 按 ID 定位。

```json
{
  "id": "v-actor-role-matrix",
  "artifact_id": "actor-role-matrix",
  "title": "参与者/角色矩阵 · 星河零售虚构案例",
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
    "actor-picker",
    "role-picker"
  ],
  "relationship_ids": [
    "actor-role"
  ],
  "analysis": "哪些参与者承担哪些角色？ 本视图限定订单履约改造范围，展示案例设定的参与者/角色矩阵。列出参与者与角色；实际项目需由相关责任方核实。",
  "legend": "参与者被分配到角色；单元代码：assigned；未记录不等于不存在。",
  "allow_mixed_evolution": false
}
```

生成单项：

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --artifact actor-role-matrix --out ./architecture-output
```

TOGAF_SKILLS 由使用者设为技能集合根目录，非机器固定路径。

## 来源

G248 附录 A，源行 504, 507；方法指南：G248, G249, G198。见 [来源分析](../source-analysis.md)、[来源指纹](../../sources.json) 与 [图表解释索引](../figure-index.json)。行号以原项目版本为准；图表不确定性必须保留，操作规则是项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-purpose-title`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 3.6.4.13. Actor/Role Matrix](../../corpus/fundamental/analysis/05-architecture-content.md#tag_03_06_03_13)
  - 概念：演员/角色矩阵显示演员执行哪些角色。
  - 逻辑：Actor performs Role关系连接两轴。
  - 决策：核对承担关系再识别相应要求。
  - 边界：承担角色不证明技能达标或正式授权已获证实。
