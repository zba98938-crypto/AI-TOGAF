# BPMN Data/IO 与补偿设计时规则子集

此组在 `codex/standards-next` 隔离工作树实现。正式入口为现有
`standards.py` 的 `import / validate / export`，由
`bpmn_design_semantics.check` 合并 `bpmn_data_compensation.check` 的发现、
来源定位、执行适配说明和能力缺项。原生 XML 字节仍为权威内容。

本组提供 21 个源绑定规则族：数据端点的 ItemAwareElement 类型、输入/输出
方向与所属 Activity/Event、无转换时单一来源、生命周期访问范围、
ItemDefinition 类型与 collection 默认值一致性、类型转换要求、
DataObject/DataStore 引用类型、DataObjectReference 派生定义、DataObject/
Property 所属容器、嵌入 SubProcess 直接 IO 禁止、IO set 类型/所属/子集/
成员关系，以及补偿事件放置、边界 SequenceFlow 禁止、Activity 引用类型和
throw/end 可见性。类型继承来自指纹一致的官方 BPMN20.cmof 内部 Package；
缺少必要类或继承目标时拒绝使用该来源，不将缺资料报为模型错误。

来源为本地官方 `BPMN-2.0.2.pdf` 与 `BPMN20.cmof`。每个发现保留模型 XPath、
PDF 物理页码、CMOF 原生 ID 与 SHA-256。
`bpmn-data-compensation-binding-additions.json` 包含 30 个已校核存在的条目、
实现及独立正反例位置，尚未合并共享覆盖台账。条目保持局部实现与有限夹具
验证状态，不据测试数量提升全语言完整性。

规范差异单独保留：

| 项目 | 原文与适配依据 |
| --- | --- |
| DataObjectReference.itemSubjectRef | PDF 物理 234 页禁止声明；继承的 CMOF/XSD 字段仍可表达。拒绝显式声明，从 dataObjectRef 推导有效定义，原 XML 不改写。 |
| DataOutputAssociation 方向 | PDF 244 页措辞与 253 页明确的关联定义冲突。采用 253 页所属 Activity/Event 输出作为来源的规则，不倒置模型。 |
| SubProcess.compensable | PDF 333 页提及，但已获官方 CMOF/XSD 无该属性。保留争议，不创造属性，不一律拒绝所有缺显式 handler 的模型。 |
| DataObject.dataState | PDF 234 页禁止、235 页允许。保留两处原文，暂不添加一律禁止状态的规则。 |
| Semantic.cmof 导入 | 官方机器来源中存在未获导入。它仍是来源与溯源缺项；本组需要的类在已获 BPMN20.cmof 中可定位，不等于整个元模型来源闭包已完成。 |

验证目录为隔离工作树 `output/bpmn-data-compensation-20261109/`：
`audit-replay` 原字节重放此前 2 个正例及 11 个 schema-valid 反例，全部按预期
处理；`native-exchange` 保存 3 个模型的 import/validate/export 命令与无损
往返结果，并验证错误 Activity 引用无法生成原生包。

35 项新增测试通过。`regression-02` 使用未修改的正式证据 runner 实际运行
109 项，失败、错误、跳过均为零。运行时其他并行任务修改了无关 UML/
workbench/资料测试源码，因此该轮 `passed=false` 并保留
`source_changed_during_execution`；它证明本组夹具和 BPMN 回归结果，不能充当
全工程冻结证据。root 集成冻结后须执行正式全量验证。历史失败目录原样保留。

复现当前规则及回归：

```sh
TOGAF_BROWSER_PATH=/Users/Shared/ai-togaf-browser-20261106-01/chrome-headless-shell-mac-arm64/chrome-headless-shell \
python3 -B tests/run_native_standard_evidence.py --out output/<new-empty-round> \
  test_bpmn_data_compensation test_bpmn_reference_semantics \
  test_bpmn_design_time test_bpmn_render test_native_standard_cli
```

尚未声称完整设计时能力、全部资料专业验收、507 项模型评测或组织批准。
本组不执行表达式、流程运行或回滚调度。数据图形义务另行补齐：既有 process
渲染计划尚未遍历 Activity 内 Data/IO 和 DataAssociation，不能把语义正例
解释为这些图形表达也已获验证。模型会话用量为零，人工验收与组织签署待办。
