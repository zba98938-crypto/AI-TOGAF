# BPMN MI、SequenceFlow 数据简写与混合数据 DI

本组是有限能力补齐，工作树为 `codex/standards-next`。源码、原生输入和新证据
均保存在本机；历史记录不覆盖，完整标准能力、507 项、人工验收和组织签署
未提升完成状态。

官方依据为本地 BPMN 2.0.2 PDF（物理 220–224、240、253–254、398、405、
423、441–442 页）、CMOF 和 Semantic/BPMNDI XSD。Table 10.29 规定 Task 的
MI 集合引用属于同一 Activity IOSpecification；SubProcess 使用其上下文可见
的集合 DataObject。实现核对初始化输入、引用类型、所有权/生命周期、集合
标志、每实例数据项标量标志及事件定义引用类型。`inputDataItem/outputDataItem`
在原生图形中通过已核对的 XSD 局部角色映射为 DataInput/DataOutput，而非
根据 XML 标签大小写猜测。它们属于可见 MI Activity 的可选外部数据描绘；
即使 SubProcess 折叠也保留其图示，省略时记录未图示库存。

外部 ItemDefinition 的 scalar-of 类型关系没有官方可直接执行的本地映射，
相同 structureRef 文本不能证明语义等价。因此具体 `mi_unverified_obligations`
仍记录这一子义务。loopCardinality 的整数值、completionCondition/Complex
条件的布尔求值和默认事件选择不执行；未知 Activity 子类的 MI 引用规则
同样保留未覆盖。可选事件引用未提供时不会制造缺失错误。

Figure 10.68 与 Table 12.35 的数据简写不含 `bpmnElement`，其 `sourceElement`
指向 DataObjectReference 图形，`targetElement` 指向当前同一 BPMNPlane 中
的 SequenceFlow 图形。源/目标活动中的两条真实数据关联必须存在且解析唯一；
缺项、反向/错误端点、零来源转换冒充源活动输出和歧义会被拒绝。输出保存 `normalized_semantic_ids`，
简写本身的 `semantic_id` 为 null，`view_identity` 仅供绘制。浏览器以临时
Association 符号绘制无箭头点线，不把临时符号写入原生模型或导出包。

Section 9.7（物理 166–167 页）允许 Collaboration 显式引用 Choreography。
设计图后端按 `choreographyRef` 和源 DI 选择展开被图示的编排范围；
完全未图示引用保留为可选原生库存，保留 Pool/Process 的
可选数据图示和 participant associations。DataAssociation 的活动/数据项
端点覆盖不能冒充同级活动或 Participant Band。普通元素重复图示在原生 validate 与 render 中均被拒绝；
参与者 band 的合法多次图示保持原行为。

Bounds、BPMNLabel 和 waypoints 的原始字符串在 plan 和原生包中保存。设计图
保留已有报告 `source_geometry` 数值 Bounds 兼容字段，并新增
`source_coordinate_geometry` 原始坐标字段。SVG 属性保持源字符串；全部
图形组按 BPMNPlane 的原有顺序排列。仅在显示过程中转换为数值以及派生文字
布局，节点与连线均不自动布局。

受控进程继续使用已有固定 renderer。合法 `oneBehaviorEventRef` 原生属性被
旧通用 on* 检查误拒绝的真实记录保存在新的 controlled-first-diagnostic-01。
共享入站门禁修复由 root 负责，并且只允许官方 MI 元素上精确无命名空间的
该属性；大小写变体、其他元素、命名空间及主动属性仍拒绝。本组保持合法
属性的真实正例，不通过删除它绕过验证。

必要旧测试修订保留语义约束：原 MI role 正例的 Task/外部 DataObject 组合
改为规范 SubProcess 场景；原“双 scalar item 改为 collection=true 应 valid”
断言保留集合属性匹配检查并补充两条 MI scalar 拒绝断言。其原生反例与
Table 10.29 原文作为本组证据保留，旧失败轮次原字节不变。

独立 binding delta 不修改公共 coverage-bindings。所有绑定继续 partial，
既有 MI item、DI bpmnElement/sourceElement/targetElement 绑定的新执行扩展
需 root 独立审查，不在此 delta 中覆盖。

复现入口：

```sh
TOGAF_BROWSER_PATH=/Users/Shared/ai-togaf-browser-20261106-01/chrome-headless-shell-mac-arm64/chrome-headless-shell \
python3 -B tests/run_native_standard_evidence.py --out output/<new-empty-test-round> \
  test_bpmn_mi_shortcut test_bpmn_role_types test_controlled_bpmn_mi_shortcut
python3 -B tests/diagnose_bpmn_mi_shortcut.py --out output/<new-empty-graphic-round>
```

具体实际执行结果、源码指纹、正反例输入、SVG/PNG/浏览器截图、清理记录和
限制由本组输出 handoff 绑定。工程全量冻结、独立模型评测和业务签署仍由
后续正式轮次分别验收。
