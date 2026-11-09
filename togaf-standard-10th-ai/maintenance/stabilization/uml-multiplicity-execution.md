本轮增加 MultiplicityElement 的显式原生查询执行帧，范围为 8 个查询、10 条操作约束与 2 个派生属性。候选覆盖绑定位于同目录 uml-multiplicity-execution-binding-candidates.json，20 条候选分别对应 8 个操作构造、10 条约束和 2 个属性；全部保持 partial。公共绑定由正式维护流程另行审查，本轮不改公共绑定。

规范身份固定为 UML.xmi SHA256 e8166c91f51b8a0c015a90101b83d2249d03252e9f9a500a6511654347804f21。每条候选保存文件指纹、原生 ID、XML 路径、发生次序、完整原文及原文 SHA、owner、参数方向、类型、界限、ordered/unique。bodyCondition 与 precondition 保留规范角色；result = 的完整原文进入独立类型帧，不使用 postcondition API，不提取 RHS 提升状态。

| 查询 | 精确输入 | 规范返回 |
|---|---|---|
| compatibleWith | other: MultiplicityElement [1..1] | Boolean [1..1] |
| includesMultiplicity | M: MultiplicityElement [1..1] | Boolean [1..1] |
| is | lowerbound: Integer [1..1], upperbound: UnlimitedNatural [1..1] | Boolean [1..1] |
| isMultivalued | 无 | Boolean [1..1] |
| lower | 无 | Integer [0..1] |
| lowerBound | 无 | Integer [1..1] |
| upper | 无 | UnlimitedNatural [0..1] |
| upperBound | 无 | UnlimitedNatural [1..1] |

所有输入为 in 参数、无序、唯一；所有查询 isQuery=true。return 参数独立于调用参数排序。lower/upper 的派生属性为 [1..1]，与对应查询的可选返回界限分别记录。getter 桥只对规范 constrainedElement 明确关联的两个派生定义使用；ExtensionEnd 的重定义缺省下界不在此组。

validate_mapped 的第三个可选参数 operation_cases 接受逐项调用清单，原有调用和四参数 Java 命令继续兼容。CLI 增加 --operation-cases JSON 路径。每项提供 id、self、obligation（完整来源 key）和带类型的 arguments；派生属性使用其来源 key。调用者不能提供 OCL、方法名、脚本或 URL。Java 核对唯一规范语义签名，并按精确原生方法及 carrier 调用；参数和实际 result 显式绑定到独立变量。result_probe 仅为固定 false/null/invalid/true 诊断，原生结果另存，诊断结果不计验收。

回归输出为 output/uml-multiplicity-execution-next-final-02。49 项测试（新增 9、既有 40）实际执行，失败、错误、跳过为零，执行前后 UML 3 文件及新测试/夹具指纹一致。首组 119 个调用请求产生 149 条约束/派生记录：140 次完整规范表达式求值，另有 1 次取得 invalid sentinel 的辅助字面量求值；110 次实际原生调用。同一夹具的既有类不变量另有 407 次求值。125 条正例均为 true 并与独立原 XML 判定一致；3 条结果诊断区分 false、null 与 invalid；9 条未执行的缺实例、类型、参数、错误 UnlimitedNatural 负数或 int 溢出记录均为 uncovered。

nullable 限制保持真实：ValueSpecification.integerValue()/unlimitedValue() 的规范结果可为 null，Java carrier 为 int。12 条错误值种类、LiteralNull 或 OpaqueExpression 边界中，实际原生界限返回 1 并与原 XML 默认值一致，但 6 条相关完整规范 bodyCondition 的 OCL 求值为 invalid，均保持 uncovered。此组不认证可空查询载体、所有值表达式、所有模型子类、int 范围之外的 Integer 或完整规范义务。

根代理另以八组新 XML 界限独立回放，记录 output/uml-multiplicity-root-independent-01/summary.json：208 个请求、280 次完整原文求值、208 次真实原生调用均与独立原 XML 数学判定一致，源码稳定、模型请求 0。该复查与本组测试分别记录，不是独立模型评测、专业人工签署或真实组织批准。

失败历史保留在 output/uml-multiplicity-execution-next-01：第一版 Java 泛型编译失败及其源码原字节、argv/退出值/日志；修复后的 first-probe-v2 实际执行 12 条规范/派生表达式。CLI 返回 3 沿用 incomplete 契约，不代表测试失败。分析目录 output/uml-operation-derived-mapping-next-01 继续只读保留；225 条操作约束与 73 个派生属性的全量映射不会因这 12 条限定证据而整体提升。

完整 UML 2.5.1/BPMN 2.0.2、507 项独立模型评测、专业人工验收和组织批准继续未完成。if null/invalid 条件的解析缺口另列方案，不由此组混入全部 OCL 能力声明。
