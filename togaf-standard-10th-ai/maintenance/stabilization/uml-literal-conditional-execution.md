# UML/OCL 字面量条件的受限执行适配

本组只补充已固定本地 Eclipse UML/OCL 后端的纯字面量条件表达式，并修正可选 `--operation-cases` 输入分类。公开标准绑定、规范原文、依赖、其他 UML operation 组与主工程不在本组修改范围。完整 UML/BPMN 设计时能力、507 项模型评测、专业验收与真实组织签署仍未完成。

## 来源与实际基线

本地 `skills/_shared/standards/sources/ocl-2.4/OCL-2.4.pdf` SHA-256 为 `b97e46a946418ba3c8db6f33def013e4d8a56ac500cb1bed055fed660977a7ef`。原字节、pdftotext 命令、对应页文字及页图保留在 `output/uml-conditional-baseline-next-01/`。

| 物理页／印刷页 | 原文依据 | 本组用途 |
| --- | --- | --- |
| 57／41 | InvalidType: “OclInvalid conforms to all other types.” | 保留 InvalidLiteralExp 本身类型 |
| 58／42 | VoidType: “OclVoid conforms to all other types except OclInvalid.” | null 可作为 Boolean 声明的初始化值 |
| 73／57 | IfExp: “The type of the condition of an if expression must be Boolean.” | 条件 AST 必须具有 Boolean 静态类型 |
| 73／57、80／64 | IfExp 整体类型是 then／else 的最具体共同父类型 | 在三类字面量域内显式对称 join；原 parser／witness 类型单独记录 |
| 77／61、80／64 | LetExp 类型来自 in 表达式；初始化类型须符合声明类型；VariableExp 类型来自变量 | 明确的局部 Boolean let 执行适配 |
| 148／132 | IfExpEval: true 选择 then；false 选择 else；否则结果 invalid | null／invalid 不等于 false，也不访问 else |
| 248／232 | “A null or invalid condition makes the whole expression invalid.”；未选分支 undefined 可不污染结果 | 同值分支、嵌套及未选分支的独立反例 |

原版本对 45 个诊断输入进行原 parser 与原 query 分别实测：各 22 次解析与求值，23 次原始失败。14 个直接使用 null／invalid 条件的原文均被原 parser 拒绝。诊断专用 Boolean let AST 骨架对这 14 个输入实际求值全部为 invalid，访问事件只包含 condition／初始化／变量，then 与 else 均未访问。原 parser 已能处理显式 `let condition : Boolean = null/invalid`，其实际结果同样为 invalid。65 层合法括号、1025 项 true-and 平链、64 项 not 均保留原 parser 成功路径。原失败日志与源码、旧测试原字节均保留，不能作为当前通过结果。

## 实施边界

`UmlValidate.query` 先执行原 parser；只有其失败后才进入扩展的封闭字面量语法。既有 18 个精确 whole-expression Boolean 适配保持原行为。新增语法只接受 true／false／null／invalid、not、and／or／xor／implies、括号与完整 if／then／else／endif，允许闭合嵌套，每层最多一个二元运算，限制为 64 层及 2048 tokens。被原 parser 接受的合法长表达式不受 fallback 限制。

若条件 AST 是 OclVoid 或 OclInvalid，适配新增仅限该条件的 `let __literal_condition : Boolean = true in __literal_condition` 骨架，并把初始化表达式替换为原字面量树。字面量仍保持 OclVoid／OclInvalid 类型，变量及 in 表达式为 Boolean。该方法不改规范文字，也不声称 AST 与来源完全同一；它是单独披露的 execution-only typing adaptation。then／else 原树与顺序保留。原生 IfExp 求值器没有修改。

共同类型另用 `conditional_type_adapter` 披露，不能把原 parser 成功的类型调整记成 fallback。规范在本闭域形成 OclInvalid → OclVoid → Boolean：Invalid 符合 Void，Void 不符合 Invalid，所以 null／invalid 两种分支次序都取 OclVoid；Boolean 与任一 undefined 类型都取 Boolean。同类分别保留其类型。原 parser 先尝试来源文字；成功后，受限源码树与原 AST 的每个字面量、If 与标准 Boolean operation 必须逐节点匹配。先后序计算完整调整计划，再统一只写 IfExp.type；任何 gate 失败或超限均返回原 AST 并标 uncovered，不新增解析拒绝。fallback 同样先处理子树，再对 witness 解析结果显式设置规范 join。逐节点记录逻辑来源路径、original-parser／fallback-witness-parser、原类型、调整类型与分支类型，原文字面量与求值器保持原样。通用 OCL、显式用户 let、Integer、模型属性及已接受长式的类型修复不在这个闭域。

新增可选结果字段 `conditional_ast_adapter` 与 `original_parser_error` 保留原解析失败原因；既有 `literal_ast_adapter`、true／false／null／invalid／non-boolean 计数及旧命令格式继续保留。缺实例仅说明 applicable=0，不能算约束通过；非 Boolean、模型内容、字符串、标识符、非白名单字符、残缺与超限条件继续 uncovered。

## 独立验收与复现

`tests/uml_conditional_fixtures.py` 从独立 XML 树产生 115 个条件矩阵、同值分支、嵌套与 grouped Boolean 条件，并保留独立复核首次失败的五组固定来源／XML 配对。独立值表、AST 形状、所选分支及固定 3×3 递归类型 oracle 不导入生产 parser、类型函数或 visitor；类型检查访问全部子树，包括未求值分支。`tests/java/UmlConditionalProbe.java` 只作测试观察，记录原 parser、当前 query、实际求值与访问事件；两条故意错误 AST（把 null 条件换成 false、交换 then／else）实际得到错误结果，被独立 XML oracle 拒绝。另四条实际错 IfExp.type 的反例保持值、形状与分支轨迹，却必须被类型 oracle 拒绝；故意制造后续源码／AST 不匹配验证全部已规划修改均未应用。原测试 ID 保留。

在仓库根目录复制脚本到新的空轮次目录后，使用现有 Java；保留本轮证据原字节：

```sh
mkdir output/uml-conditional-replay-01
cp output/uml-conditional-next-final-04/run_formal.py output/uml-conditional-replay-01/run_formal.py
JAVA_HOME=/Users/Shared/ai-togaf-java-20261106-01 PYTHONDONTWRITEBYTECODE=1 python3 -B output/uml-conditional-replay-01/run_formal.py
```

02 的 67 项通过与 132 输入、03 的条号目标测试、根先前的 512 嵌套输入仅绑定当时源码。随后 14 项独立复核中五组出现 IfExp 共同类型错误（另有一处类型传播）；其值、形状与分支一致不能认证静态类型。03、14 失败记录及旧字节原样保留。当前新增共同类型版本的实际相关回归、137 输入及逐节点类型结果以 `output/uml-conditional-next-final-04/` 的命令、源冻结和交接为准；不得用旧 Java 的结果认证新版本。规范补充候选均保持 partial，公开 UML 标准台账不增加条目。全工程、全部规范义务与 507 项模型评测仍交由统一冻结轮次。

## 可选 operation-cases 的分类

`uml_backend.read_operation_cases` 对新参数先做 UTF-8、JSON、列表与记录字段检查，并使用现有固定来源目录展开 exact obligation。未知义务仍为 `Incomplete` 的子类；旧 API 的 `Invalid`／`Incomplete` 捕获与成功 incomplete exit 3 兼容。新参数的错误输出在 stdout 返回小型 JSON，并且不写成果报告：

| failure_category | conformance_status | 触发 |
| --- | --- | --- |
| validation-error | invalid | 非 UTF-8、无效 JSON、错误容器／字段、已存在输出 |
| material-missing | incomplete | 新 case 文件或模型文件缺失、case 依赖来源缺失 |
| capability-uncovered | incomplete | exact obligation 不在受限能力目录 |
| backend-incomplete | incomplete | 后端其他未完成或超时 |

新 case 预检和现有输出检查发生在启动 Java 前。旧无 `--operation-cases` 错误文字与摘要保持兼容；新成功调用仍实际运行 Java并以 incomplete exit 3 返回。CLI 独立 8 项测试与 10 个持久诊断、无 Java 调用计数、输出旧字节、实际成功日志，以及只包含 CLI 改动的审查 patch，保留在 `output/uml-operation-cases-cli-next-final-02/`。诊断中的来源缺失使用显式受控模拟，未删除真实资料。

本组不新增外部软件、远程执行或模型请求；model_requests=0。候选能力关联均为 partial，来源语义复核、专业签署和组织批准分别保持待办。

CLI 01 的成功测试曾包含一个 conditional 字段断言；审查后把该断言移到已有 conditional 测试，避免 CLI-only 产品 patch 依赖条件组。01 交接和运行原字节保留，当前绑定采用追加的 CLI 02 与 conditional 02 轮次。
