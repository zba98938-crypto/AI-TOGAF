# BPMN 本地资源包的受限能力

本轮实现 BPMN 2.0.2 的本地文档导入、限定名身份解析和原字节资源保存。它是标准能力的一部分，不能提升完整 UML/BPMN、507 项评测、人工验收或组织批准状态。

规范依据是 BPMN 2.0.2 §8.2.2（物理页 81–83）、§15.3.1/15.3.2（物理页 505–507），以及原始 BPMN20.xsd、Semantic.xsd、BPMN20.cmof。§8.2.2 的 XSD 1.0、WSDL 2.0 导入支持义务仍未完成；§15.1 的不完整模型交换仍未完成。Table 8.2 将 location 记为可选，而 Table 8.4 和取得的 BPMN20.xsd 要求 location；这里继续执行原始 XSD，没有修改来源。

`standards.py` 的 `import/validate/export` 保持旧用法，原生 JSON 包版本仍为 `1.0`。新增可选的 `document_path` 和 `resources`，资源条目为 `{path,payload_encoding,content,sha256}`；编码固定为 base64。旧单文件包仍不要求新增字段。

```sh
python3 -B togaf-standard-10th-ai/skills/_shared/scripts/standards.py import \
  --language bpmn --version 2.0.2 --input PACKAGE/nested/main.bpmn \
  --package-root PACKAGE --out NEW/native-package.json
python3 -B togaf-standard-10th-ai/skills/_shared/scripts/standards.py validate \
  --language bpmn --version 2.0.2 --input NEW/native-package.json
python3 -B togaf-standard-10th-ai/skills/_shared/scripts/standards.py export \
  --language bpmn --version 2.0.2 --input NEW/native-package.json \
  --materialize --out NEW/materialized-bundle
```

只有显式 `package_root` 才允许库接口读取本地导入文件；命令行从包根内的实际输入路径推导主文档路径。旧 API 未提供路径时使用虚拟 `main.bpmn`。嵌入包始终只消费包内资源，即使传入 `--package-root` 也不会用磁盘填补缺项。

仅支持 `importType=http://www.omg.org/spec/BPMN/20100524/MODEL`。location 相对当前文档，而不是相对包根；例如 `nested/main.bpmn` 可以导入 `../shared/model.bpmn`。越界、协议、查询、片段、百分号编码、控制字符和符号链接逃逸被拒绝；符号链接循环归类为错误。有效循环导入有限遍历，每份文档只读取、索引和输出一次。含有效 `xml:base` 的导入保留未覆盖状态且不读文件；XSD 不允许的属性仍按原始 XSD 拒绝。非 import 的 BPMN href，包括扩展元素中的 href，仅保留为未覆盖内容，绝不读取文件。UML 原有 href 分支不变。

磁盘路径先作严格解析，在 Python 3.9 与 3.13 下文件自身及祖先目录的符号链接循环均归类为输入错误；只有真实路径不存在时才允许非严格解析。普通缺文件、缺父目录及指向包内缺文件的链接仍报告原始导入逻辑路径的材料缺失，后续包内边界检查继续执行。

限定名使用命名空间和本地 ID，并逐文档、所有者 XPath、属性/文本角色和字段生成解析记录。同 ID 不同命名空间不会别名；同命名空间的重复 ID 会报告歧义。所有导入文档仍执行原有 XSD 和单文件语义校验；IDREF 只在本文件内解析。新目标类型依据原始 CMOF 类型、继承关系以及取得的 XSD 角色映射，不使用统一的已验证 QName 白名单。单文件已有语义规则仍是其权威检查。

交换名与元模型名的适配单独记录：`calledElement → CallActivity.calledElementRef`、`eventDefinitionRef → CatchEvent/ThrowEvent.eventDefinitionRefs`、`participantRef → ConversationNode/ChoreographyActivity.participantRefs`。PartnerEntity/PartnerRole 本来就使用 participantRef，不改变。规范原文不变。

资源限制为主文档加资源最多 64 份、资源最多 63 份、解码总字节最多 64 MiB、图深度最多 16、引用最多 20,000、路径/引用最多 4,096 字符。资源数量、编码长度和估计解码总量在 base64 分配之前检查；文件大小、图深度和数量在磁盘读取之前检查。串行化 CLI 输入最多 192 MiB。不可达的附带资源、重复路径、主文档冲突、文件与祖先目录冲突和指纹不一致被拒绝；目录形 location 不会被折叠为文件。

默认 export 继续输出主 XML 原字节。`--materialize` 先核验包、完整导入图和每份文档，再创建全新的目录；失败不覆盖旧目录。该能力保留 BOM、换行、QName 拼写、原始 XML 和 DI 坐标。它不补坐标、不执行跨文档语义、不合并模型、不渲染跨文档图形；这些能力明确未覆盖。

工作台保持 8 MiB HTTP 请求容量和 7 MiB 主 XML 编辑容量。大于编辑容量的 CLI 包会明确拒绝进入编辑器，文件不会截断。BPMN 原生包通过新增固定 `/api/native/unpack` 调用同一 `package_bytes` 完整性核验，再保存 `native.xml`、`native.resources` 和 `native.document_path`；非空合法 bindings 因编辑能力未覆盖而拒绝，非法 bindings 归类为输入错误。主文档编辑保留导入资源原字节，并纳入不可变版本、诊断和生成任务。导出原生源码包 JSON 可以再次导入；完整标准包的库存和绑定不被编辑器静默绕过。

`resource_closure.status=complete` 仅表示受限文档和身份闭包完成。`diagnostic_groups` 分别呈现输入错误、材料缺失和能力未覆盖；跨文档身份成功仍保留逐角色语义未覆盖记录，渲染在浏览器启动之前拒绝。确定性反例见 `tests/test_bpmn_import_resources.py`；实际本地 UI 复现入口为 `node workbench/verify_bpmn_resources_ui.mjs --out output/NEW_DIRECTORY`。
