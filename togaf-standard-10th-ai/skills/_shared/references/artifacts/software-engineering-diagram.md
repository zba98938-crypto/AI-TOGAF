# 软件工程图（Software Engineering Diagram）

ID：`software-engineering-diagram` · 主责：[togaf-application-architecture](../../../togaf-application-architecture/SKILL.md) · 原文域：应用。

**定义边界**：名称与域来自 G248 附录 A。下列输入、字段、分析和验收是项目操作约定；尚未取得 C220 正文进行逐项正式定义核验，不宣称官方强制最小字段。

## 决策与受众

软件组件如何组织并依赖接口或模块？

主要受众：应用和业务功能负责人、集成及数据团队。输出需回应已确认关注点，不因清单存在就强制生成。

## 输入与属性

必需：五维语境、决策问题、领域对象及证据或明确候选假设。按对象类型收集适用字段：

- `software_module`：`responsibility`、`version`。
- `interface`：`version`。

可选：既有模型、版本差异、度量、质量要求和法规约束。关键缺口影响结论时先询问，局部不足写入 gaps 并保持 assumed/uncertain。确实不适用的字段说明理由；不以默认数值冒充事实。

## 关系与表示语义

- `depends_on`：对象依赖目标作为前置。software_module, work_package → software_module, work_package。
- `implements_interface`：模块实现接口。software_module → interface。

## 分析与构造

1. 确定设计层级和组件职责。
2. 显式提供或依赖接口。
3. 检查循环依赖及责任过载。

按 [共享规则](../modeling-rules.md) 复用稳定 ID 和证据，区分对象、关系、版本及演进状态。修改需要比较属性和关系，不只比较框数量。

## 输出

Markdown 回答决策并展示目录、矩阵或视图；JSON 保存对象、关系、来源和模型版本。表示法：`flowchart`。提供可编辑 Mermaid 或 SVG 源、布局说明、独立 SVG 和 PNG。图例解释箭头、区域和颜色；简化关系图不宣称完整 ArchiMate/UML/BPMN。

## 质量与常见误读

- 不把开发工具流水线误作软件结构。
- 结构图不自动描述部署。
- 五维独立；源图解释不能直接成为项目事实，候选不等于批准。
- 对照相关目录、矩阵和图的共享对象与关系方向；检查证据、假设和缺口。
- 图形需检查中文标签、箭头、边界和可读性；脚本检查不能替代业务验证。

## 复用与追溯

按视点需要被架构定义文档等交付物引用，不强制绑定。

相关制品：[接口目录](interface-catalog.md)、[应用通信图](application-communication-diagram.md)、[软件分布图](software-distribution-diagram.md)。跨制品复用实体 ID、需求及构建块追溯，不复制独立冲突对象。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际生成结果（历史材料已清理） 包含模型对象、关系、分析、图例和证据。以下为可运行输入的视图定义；对象和关系可在 完整案例模型（历史材料已清理） 按 ID 定位。

```json
{
  "id": "v-software-engineering-diagram",
  "artifact_id": "software-engineering-diagram",
  "title": "软件工程图 · 星河零售虚构案例",
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
    "module-order",
    "module-stock",
    "interface"
  ],
  "relationship_ids": [
    "module-dependency",
    "module-interface"
  ],
  "analysis": "软件组件如何组织并依赖接口或模块？ 本视图限定订单履约改造范围，展示案例设定的软件工程图。确定设计层级和组件职责；实际项目需由相关责任方核实。",
  "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
  "allow_mixed_evolution": false
}
```

生成单项：

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --artifact software-engineering-diagram --out ./architecture-output --render
```

TOGAF_SKILLS 由使用者设为技能集合根目录，非机器固定路径。

## 来源

G248 附录 A，源行 562；方法指南：G248, G248, G21I。见 [来源分析](../source-analysis.md)、[来源指纹](../../sources.json) 与 [图表解释索引](../figure-index.json)。行号以原项目版本为准；图表不确定性必须保留，操作规则是项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-purpose-title`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 3.6.6.12. Software Engineering Diagram](../../corpus/fundamental/analysis/05-architecture-content.md#tag_03_06_05_12)
  - 概念：软件工程图从开发视角将应用分为包、模块、服务与操作。
  - 逻辑：内部结构支持阶段迁移和机会方案分析。
  - 决策：按开发关切检查分解及受影响单元。
  - 边界：开发分解不替代业务功能、部署结构或详细程序设计。
