# BPMN 本轮设计时实现与证据

本轮新增 `bpmn_design_semantics.check` 的15个来源绑定规则族。规范来源为本机 BPMN 2.0.2 PDF（SHA-256 `d3d9258a70bf808c11ac52becea4ce645540a8b881117535f60a56fbf13e22f2`），每条发现记录 PDF 章节、物理页码及模型 XPath。规则检查会话参与者与消息归属、连接端点、调用目标、全局定义、编排参与者与消息方向、参与者映射/数量以及 DI 属性、参与者带和边端点。官方 XSD 引用字段由共享解析器提取；同命名空间 QName 统一解析，外部/未声明引用保持缺资料或未覆盖诊断，不当成本地别名。

`bpmn_design_render.design_plan` 将语义身份与 DI 图形身份分开，因此同一个 Participant 在多个活动上的参与者带不会互相覆盖。图形使用来源中的 Bounds、waypoints 和可选 label Bounds；未给出 label Bounds 时仅推导排字位置，不增加模型节点或连接坐标。会话六边形、双线、Sub/Call 标记，编排活动、发起/非发起参与者带、消息信封、循环/多实例标记及展开的子/调用编排由本机固定图形层绘制；普通事件、网关、任务、Pool、Lane、数据和制品使用已安装的 bpmn-js 符号服务。SVG、PNG 和报告核对完整 DI 图形集合、来源指纹和原坐标。受控渲染进程与公开原生 render 共用固定 `renderDesignScene`，不把脚本字段开放给模型会话。

安装的 bpmn-moddle 描述符与规范交换语法有明确差异：同命名空间 QName 需转换成本地 ID，ParticipantAssociation 的引用子元素需作为描述符属性，ConversationNode 的 `messageFlowRef` 描述符拼写为 `messageFlowRefs`。这些转换仅存在于排图投影；原生包导入/导出仍保留原始 XML 字节，图形报告分别保存原文、排图投影指纹和转换依据。规范正文与执行适配分别记录，不容忍导入警告作为成功。

`render(..., auto_layout=False)` 延续原接口并默认阻断缺 DI。CLI `render --language bpmn --version 2.0.2 --auto-layout` 和工作台布尔选择可调用 `bpmn_layout.derive_layout`：本机确定性代码只新增缺失图形，已存在的 Bounds/waypoints 与属性逐字保留；派生 XML 单独保存为 `.layout.bpmn`，报告分别记录 `source_sha256` 与 `rendered_model_sha256`。已有完整 DI 选择自动布局时仍返回原字节。非法坐标、歧义根/端点、容器空间不足、未给完坐标的参与者带栈、自动 Lane 分区均明确阻断；这些限制未提升为完整能力。

两项规范/交换差异在报告中单独保留：Table 11.2 的消息引用 `[1..*]` 与官方 XSD 的1–2限制；ParticipantMultiplicity 未指定 maximum 时正文要求多实例符号，而 XSD 的 default 为1。当前执行分别遵循官方 XML 交换限制和正文图形规则，并保留 omitted/explicit 区别及依据。

独立用例在 `tests/bpmn_design_fixtures.py` 手写语义、消息方向和显式坐标，`test_bpmn_design_time.py` 包含原生校验、正反例、原文无损包往返、重复图形身份、真实 Chromium/Resvg 输出以及显式自动布局验证。历史首次尝试、字体/标记容量失败和视觉复核前结果保留在 `output/project-stabilization-20261109/bpmn-design-time/`。最终针对性轮次及来源指纹在该目录另存，不覆盖旧结果。

这些证据是工程与确定性子集证据，全部标准义务、独立507项模型评测、人工专业图形验收和真实组织批准各自记录。完整 BPMN 一致性、组合 Collaboration 中嵌入 Choreography 的所有交换/图形义务、自动 Lane 分区及完整行为相关设计规则仍需台账逐项推进；专业验收与组织批准为待签署。
