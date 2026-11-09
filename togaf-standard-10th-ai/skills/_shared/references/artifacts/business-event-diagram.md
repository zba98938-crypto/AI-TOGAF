# 业务事件图（Business Event Diagram）

ID：`business-event-diagram` · 主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md) · 原文域：业务。

**定义边界**：名称与域来自 G248 附录 A。下列输入、字段、分析和验收是项目操作约定；尚未取得 C220 正文进行逐项正式定义核验，不宣称官方强制最小字段。

## 决策与受众

哪些业务事件触发、终止或改变业务行为？

主要受众：业务及流程负责人、服务消费者、执行与控制角色。输出需回应已确认关注点，不因清单存在就强制生成。

## 输入与属性

必需：五维语境、决策问题、领域对象及证据或明确候选假设。按对象类型收集适用字段：

- `event`：`trigger`、`outcome`。
- `process`：名称、边界、来源及对象类型。
- `business_service`：名称、边界、来源及对象类型。

可选：既有模型、版本差异、度量、质量要求和法规约束。关键缺口影响结论时先询问，局部不足写入 gaps 并保持 assumed/uncertain。确实不适用的字段说明理由；不以默认数值冒充事实。

## 关系与表示语义

- `triggers`：事件触发行为。event → process, activity, business_service。
- `produces`：行为产出事件或产品。process, activity → event, product。

## 分析与构造

1. 识别有业务意义的发生事实。
2. 连接触发行为与产生事件。
3. 补充异常及时间条件。

按 [共享规则](../modeling-rules.md) 复用稳定 ID 和证据，区分对象、关系、版本及演进状态。修改需要比较属性和关系，不只比较框数量。

## 输出

Markdown 回答决策并展示目录、矩阵或视图；JSON 保存对象、关系、来源和模型版本。表示法：`flowchart`。提供可编辑 Mermaid 或 SVG 源、布局说明、独立 SVG 和 PNG。图例解释箭头、区域和颜色；简化关系图不宣称完整 ArchiMate/UML/BPMN。

## 质量与常见误读

- 消息是事件载体而非必然等于业务事件。
- 不要与完整流程控制流混同。
- 五维独立；源图解释不能直接成为项目事实，候选不等于批准。
- 对照相关目录、矩阵和图的共享对象与关系方向；检查证据、假设和缺口。
- 图形需检查中文标签、箭头、边界和可读性；脚本检查不能替代业务验证。

## 复用与追溯

按视点需要被架构定义文档等交付物引用，不强制绑定。

相关制品：[业务服务/功能目录](business-service-function-catalog.md)、[流程/事件/控制/产品目录](process-event-control-product-catalog.md)、[业务服务/信息图](business-service-information-diagram.md)、[目标/目的/服务图](goal-objective-service-diagram.md)、[流程图](process-flow-diagram.md)、[流程/应用实现图](process-application-realization-diagram.md)。跨制品复用实体 ID、需求及构建块追溯，不复制独立冲突对象。

## 虚构模型片段

以下JSON仅示意被选对象，运行时需提供包含引用实体、关系和来源的完整`model.json`，见[模型约定](../model-v2.md)。

实际生成结果（历史材料已清理） 包含模型对象、关系、分析、图例和证据。以下为可运行输入的视图定义；对象和关系可在 完整案例模型（历史材料已清理） 按 ID 定位。

```json
{
  "id": "v-business-event-diagram",
  "artifact_id": "business-event-diagram",
  "title": "业务事件图 · 星河零售虚构案例",
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
    "event-submit",
    "process",
    "product"
  ],
  "relationship_ids": [
    "event-process",
    "process-product"
  ],
  "analysis": "哪些业务事件触发、终止或改变业务行为？ 本视图限定订单履约改造范围，展示案例设定的业务事件图。识别有业务意义的发生事实；实际项目需由相关责任方核实。",
  "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
  "allow_mixed_evolution": false
}
```

生成单项：

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" "model.json" --artifact business-event-diagram --out ./architecture-output --render
```

TOGAF_SKILLS 由使用者设为技能集合根目录，非机器固定路径。

## 来源

G248 附录 A，源行 512；方法指南：G248, G176, G248。见 [来源分析](../source-analysis.md)、[来源指纹](../../sources.json) 与 [图表解释索引](../figure-index.json)。行号以原项目版本为准；图表不确定性必须保留，操作规则是项目综合。

<!-- foundation-binding:start -->
## 当前基础标准依据

匹配性质：`direct-purpose-title`。字段、布局与组装结构属于项目操作化；用途绑定不等于官方图示或完整元模型等价。

- [C220 3.6.4.25. Business Event Diagram](../../corpus/fundamental/analysis/05-architecture-content.md#tag_03_06_03_25)
  - 概念：业务事件图连接触发事件及响应流程。
  - 逻辑：事件应触发流程并生成业务响应/结果。
  - 决策：核对触发和业务结果。
  - 边界：业务事件不等于必须使用事件消息技术。
