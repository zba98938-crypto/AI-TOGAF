# UML OCL 执行边界下一组

本组只修改 `codex/standards-next` 的 UML 模块、Java 执行适配和 UML 测试。规范文件、现有 5,779 个 UML 义务 ID、8 组重复 native ID、依赖、公共覆盖清单、当前发布与 HEAD 保持原样。没有模型请求、预算变化、专业签署或组织批准；完整 UML 2.5.1 设计时能力仍未完成。

## Lifeline 的正文与可执行 OCL

`Lifeline` 有四条 OCL 约束。本组保留既有 `interaction_uses_share_lifeline` 的正文适配，并对 `selector_specified`、`selector_int_or_string` 添加独立多重性和选择器反例。

真实 Java 基线发现 `same_classifier` 的发布 OCL 在同类及继承祖先模型上返回 `false`，在嵌套但不是继承祖先的类上返回 `true`。规范 PDF 的物理第 665 页、印刷第 623 页、§17.12.17.5 正文明确要求引用端所属 classifier 为 Interaction 所属 classifier 本身或其祖先。

`uml_backend.lifeline_classifier_adapter` 仅对固定 ID、Lifeline context、原 body SHA `596379a2f9be5fbce04025106cc1ea79e1ecce7c017588f792c256c7be594567` 和固定规范 PDF 指纹执行适配。适配先找到最近的包含 classifier，再比较相同 classifier 和 generalization 祖先。它分别处理 namespace 包含与继承，不全局修改 `closure`，也不修改元模型。缺少 `represents`、namespace、Interaction 或 context 时回到原 OCL；本组缺 `represents` 反例继续返回 `invalid`。

原 body、适配 body、各自指纹、原文定位和差异一起返回。独立 XML oracle 只读取 containment、显式 generalization、represents 与 selector；发布原 body 也在原生 Java 中另行执行。正文适配和发布 OCL 的语义等价性**未认证**，人工专业裁决仍待签署。

## Boolean 四值与有括号的表达式

原有十八个完整表达式的 typed AST 适配保留。真实基线中的六个显式嵌套表达式，例如 `(not null)`、`false and (null or invalid)`，无法被已安装 OCL parser 定型。

`UmlValidate.GroupedLiteralParser` 增加受限备用路径：只接受 `true/false/null/invalid`、`not/and/or/xor/implies` 和配对括号，每个分组最多一个二元操作，递归深度在 64 触发上限，最多 2,048 tokens。首先调用原 parser；仅原 parser 不能定型且受限语法完整匹配时，构造指向同一个标准 Boolean operation 的 AST。表达式源码不替换；字符串、标识符、自定义 operation、条件表达式和一般 OCL 都交给原 parser。

根代理独立执行的反例发现首版实现先检查备用 grammar 的限额，误拒绝原 parser 能处理的长纯 Boolean 表达式。本轮将备用 grammar 的解析和限额检查移至原 parser 失败之后；原十八条必要 AST 规则继续保留。65 层括号 `true`、1,025 项 `true and`、64 层括号 `false` 和 64 次 `not false` 都用实际原生执行确认兼容，且不采用 AST 适配。仅需要备用路径的超限 `null/invalid` 表达式仍拒绝。首版源码指纹、原生回归结果和审计前交接清单按原字节保留，修复后使用新的验证轮次。

将原 parser 恢复为第一入口后，1,025 项 `null and` 链在实际合批中达到 120 秒超时，逐项诊断又达到 15 秒超时；这条原解析器资源边界保留为 **uncovered／未完成执行**，不把超时写成拒绝通过，也不提高限额。正式 token 上限反例使用语法完整、深度低于 64、tokens 超过 2,048 的平衡 `null/invalid` 树；该原生端到端输入在单独诊断中快速得到明确 token-limit 拒绝。适配器的 token 和递归限制没有放宽，四个原 parser 可解析的长输入继续端到端执行。

实际反例分别记录 `true`、`false`、`null`、`invalid` 与非 Boolean。畸形括号、嵌套和 token 上限反例仍拒绝。`if null then ...` 与 `if invalid then ...` 条件尚不能定型，本组明确保留 `unmapped-or-parse-failed`、零执行次数，不把参考真值记为执行通过。完整 OCL 语言等价性仍未认证。

## Operation 与派生属性台账

`uml_ocl_obligations.execution_inventory` 从未改动的 UML.xmi 生成独立台账，保留每个原 body、source identity、owner identity、context identity、来源指纹和引用候选。

| 本地规范声明 | 数量 | 当前独立执行状态 |
|---|---:|---|
| Class-owned OCL invariant | 425 | 沿用现有逐项解析和执行结果；不代表完整标准 |
| Operation-owned OCL constraint | 225 | 完整范围未认证 |
| Operation declaration | 205 | 完整 operation 等价性未认证 |
| bodyCondition 引用 | 202 | 保持 bodyCondition 身份，不改称 postcondition 声明 |
| precondition 引用 | 23 | 完整范围未认证 |
| 显式 postcondition 引用 | 0 | 仅陈述当前已获取 UML.xmi 的声明情况 |
| derived attribute | 73 | 完整派生与派生联合等价性未认证 |

本组实际执行了 `isMultivalued` 的固定 precondition/bodyCondition，以及 `lower/upper` 的固定派生 bodyCondition；默认、零、有限值和 unlimited 模型使用独立 XML 数值 oracle。该有限验收集不提升其他 operation、用户模型 pre/postcondition 或全部派生属性的状态。台账生成本身执行次数始终为零。

`State-isConsistentWith` 的 State 与 Vertex 声明继续使用不同完整 source identity。其 bare body/precondition 引用保留两个候选，不选定隐式目标。`Vertex.redefinedElement` 由已获取的 generalization 链定位到 `RedefinableElement` 的继承派生联合特征；不改成 `redefiningElement` 参数，不改 native ID，也不凭测试修订规范。

## 本地复现与证据

使用现有 Java 和项目依赖：

```sh
JAVA_HOME=/Users/Shared/ai-togaf-java-20261106-01 \
python3 -B -m unittest discover -s tests -p 'test_uml_ocl_boundaries.py' -v
```

旧实现的真实失败与原始输入在 `output/uml-ocl-boundary-baseline-next-01/`。修订后的原生输入、结果、XML oracle、operation/derived 台账、逐项实际测试日志和源码指纹在本组新的 `output/uml-ocl-next-verification-*` 轮次中。后续复测写入新目录；原记录不覆盖。公共 binding 只提供独立增量文件供根代理审核，不在本组修改公共清单。
