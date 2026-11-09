# UML 原生约束与 UMLDI 类图下一组

本组在 `codex/standards-next` 独立 worktree 上实现，以 `e51c4707a1b58c2b2075eac67d01b98f7245b26b` 为基础。主工程冻结版本、旧输入、历史测试日志和规范文件原字节保留。该组是有限能力增量，**完整 UML 2.5.1 设计时能力仍未完成**，也没有执行独立模型评测、人工专业签署或真实组织批准。

## 原生诊断

`uml_design_semantics.py` 从本地已核对指纹的 UML.xmi、UMLDI.xmi、DI.xmi、DC.xmi 和 PrimitiveTypes.xmi 编译继承特征、上下限、默认值、枚举域以及约束原文和来源哈希。显式标量与引用的直接、嵌套和混合编码一起计数；上限适用于显式值，序列化下限仅对已确认的 UMLClassifierShape.modelElement 和 UMLEdge.source/target 执行。隐式 UML 反向引用、派生端、subset/redefinition 的完整义务仍待补齐。

Boolean 接受 `true/false/1/0` 及其外围空白，依据是本地官方 PrimitiveTypes.xmi 的 Boolean `org.omg.xmi.schemaType` 标记 `_2` 对 XML Schema boolean 的映射。Integer、UnlimitedNatural、有限 Real 和来源枚举域分别验证，原生 XML 不被规范化或重写。该词法诊断不宣称完成 OCL `invalid/null/false` 的整体语义。

本组执行 UMLDiagram frame/heading、heading modelElement、UMLCompartment 空 modelElement、UMLLabel 的数量与 no_icon、UMLClassifierShape 双边框仅限 active Class、显式 UMLStyle.fontSize > 0 以及显式 DC Color RGB 0..255 约束。UMLDI 的 `isFrame=true` 默认值保留；缺少 heading 的默认 frame 不被放行。缺少可选 fontSize 或 RGB 分量仍返回 capability-uncovered，不把未裁定的 null/applicability 转成通过。

## 保留原生几何的类图渲染

现有 `standards render` 和 `uml_render.render_native` 对原生 UMLDI 自动分派到 `uml_di_render.py`，无需自动布局。仅支持单个 UMLClassDiagram、Class 的 UMLClassifierShape、显式文字和隔间、普通二元且非导航/非聚合/非派生 Association，以及 Generalization。模型原文保存为 `.native.uml`，bounds 和 waypoint 的数字字符串、位置和路由以及 compartment 的来源顺序不变；无坐标时不生成布局。

边的 UMLDI 端点与语义 Generalization/Association 端点对应，多重性标签与显式语义上下限一致。嵌套 Class.name、Generalization.specific、Property.aggregation 使用同一原生解析，避免静默忽略。无法表示的图形类别、字体、标记、字段、含关系之外的 DI 元素、重复或循环隔间、退化路由和不足的文字几何均明确拒绝。其他 UML 图、完整 Profile、原生编辑与全部符号仍未覆盖。

字体使用现有本机 NotoSansSC.ttf；SHA-256 为 `a3041811a78c361b1de50f953c805e0244951c21c5bd412f7232ef0d899af0da`。字体点数通过原生 Diagram.resolution 转换为用户单位，并使用 fontTools 的真实 cmap/hmtx 检查字形与文字宽度。SVG/PNG 使用已有本地 Node、resvg 和字体子集工具。viewport、隔间分隔线、框架五边形标题边界、活动类竖边、空心泛化箭头和抽象标题斜体是记录在报告中的派生装饰，不写回模型。

## 实际验证与证据

输出目录为 `output/uml-native-di-next-01/`。正式的本组收集命令：

```sh
python3 -B tests/run_native_standard_evidence.py --out output/uml-native-di-next-01/scoped-tests test_uml_native_constraints test_uml_di_render test_uml_design_semantics test_uml_render test_uml_standard_profile test_uml_standard_profile_integration
```

该次实际发现并执行 60 项：新增约束/原生 DI 29 项与已有语义、渲染、标准 Profile 和集成 31 项。失败、错误、跳过均为零，执行期间来源快照无变化。`scoped-tests/execution.log` 与 `test-evidence.json` 保留逐项结果。该集合只作为本组有限能力证据；整个后续版本须由工程冻结轮次重新绑定和验证。

四个输入与实际 SVG、PNG、原生 XML、render JSON 分别保留：无框架类图、中文框架标题、active Class 双竖边和隔间顺序反转且带负原生坐标。`final-renders/render-manifest.json` 绑定本组最终源文件/依赖指纹；初次图片也原样保留。`visual-qa.json` 记录图片检查，属于助手视觉复核，人工专业验收与真实组织签署继续待处理。

新增台账绑定在 `uml-native-di-binding-additions.json`，26 行包含 25 个新 ID 和 `uml:2.5.1:reference:UML.xmi:TypedElement-type` 的完整合并替换行，保留其原有实现和正反例。集成时按 obligation_id 添加或替换；主 coverage-bindings.json 在本组未修改。`binding-review/binding-assessment.json` 和 `uml-coverage-with-delta.json` 使用实际测试证据验证每行，全部为 passed-bounded-fixtures，implementation_status 保持 partial，verified_obligations 仍为零。

UML 台账仍有未裁定的规范正文/图注候选和五个重复 State-isConsistentWith 来源 ID；完整标准义务、507 项当前冻结版本独立模型评测、工作台集成、专业验收和组织批准尚不由本组完成。业务签署状态维持 pending-signature。
