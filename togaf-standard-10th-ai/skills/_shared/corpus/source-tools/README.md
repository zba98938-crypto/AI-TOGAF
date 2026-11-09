# TOGAF 文档转换与检索

从项目根目录运行，转换输入是 `togaf-standard-10th/` 中全部 26 份英文 PDF；既有中文稿与图表解释来自 `togaf-standard-10th-zh/`。统一输出目录为 `togaf-standard-10th-ai/`，文档目录在 `index.json`，检索片段在 `retrieval/chunks.jsonl`。

构建与验证需要 Python 3.9+、PyMuPDF 和 Pillow（版本见 `requirements.txt`）；图像 OCR 使用系统 `tesseract` 及 `eng` 语言数据。当前成果已包含 OCR 转录，缓存由原图 SHA-256 校验。缺少 Tesseract 时图像管道保留数字文本并明确记录 OCR 不可用，不把空结果当作图中没有文字。

```sh
python3 -m pip install -r tools/togaf_corpus/requirements.txt
```

```sh
python3 tools/togaf_corpus/build.py
python3 tools/togaf_corpus/validate.py
python3 tools/togaf_corpus/test_corpus.py
```

构建时同步生成图表数据。完整性、来源指纹和链接检查的结果用于发现转换缺口；机械检查通过不表示译文已经逐句校对，也不表示每个图内箭头都得到独立确认。每条记录保留自己的质量状态。

## 架构语义构建

`build.py` 全量构建会继续调用架构分析、角色能力、图关系解析和统一集成。已有正文时可单独运行：

```sh
python3 tools/togaf_corpus/build_architecture.py
python3 tools/togaf_corpus/validate_architecture.py
python3 -m unittest discover -s tools/togaf_corpus -p 'test_*.py'
node tools/togaf_corpus/verify_architecture_mermaid.mjs
node tools/togaf_corpus/verify_architecture_explorer.mjs
```

成果入口为 [architecture/README.md](../architecture/README.md)，可视浏览为 [explorer.html](../architecture/explorer.html)。`catalog.json` 汇总覆盖；`knowledge-graph.json` 保留概念、角色、技能、图内实体及关系，节点引用不把不同指南中的同名对象自动合并。类型与实例、业务组成、治理范围、视觉包含及组织汇报分开记录。

角色矩阵分别保留 G249 的 71 技能 × 6 角色与 G198 的 79 技能 × 10 角色。没有独立矩阵列的首席、分段等角色使用文字要求，数值未规定。等级是来源参考要求，不构成个人评分或通用招聘门槛。每图的 `current_visual_review` / `quality` 明确本轮视觉核验与继承语义范围。

`retrieval/architecture-chunks.jsonl` 是独立架构分析检索层。记录的 `source_path` / `source_sha256` 指向派生分析 JSON；`source_locators` 列出所有支撑原 PDF、指纹和物理页码。原文检索层 `chunks.jsonl` 保持原始来源身份。

```sh
python3 tools/togaf_corpus/query.py "企业架构师 技能要求" --role role --doc G249 --limit 3
python3 tools/togaf_corpus/query.py "能力实例 实例化" --role relationship --limit 5
python3 tools/togaf_corpus/query.py "上下级 组织" --role diagram --limit 5
```

默认同时检索原文、当前架构语义及章节校订；`--layer source` 只查全文与旧图转录，`--layer architecture` 查架构语义与章节校订。新增内容角色为 `architecture`、`role`、`diagram`、`concept`、`relationship`、`chapter-review`。返回结果明确标识 authored analysis，引用原文时继续读取 `source_locators`。

中文对照校订维护在 `chapter-review-data/`，构建时发布为 `chapters/*.{md,json}` 与 `retrieval/chapter-chunks.jsonl`。每节保留修订中文、全部英文源内容单元、页码/文本块、语义规则、条件/例外、误译修正及源文冲突。`chapters/index.json` 逐文档列明剩余单元与书签；前置资料未译和正文未审分别如实保留，不能把正文覆盖外推为完整全译。精确来源核对不等于语义认证。

```sh
python3 tools/togaf_corpus/chapter_reviews.py
python3 tools/togaf_corpus/query.py "lead Architect" --role chapter-review --doc G249 --limit 3
```

默认查询只替换已通过章节编号对齐、且已完成对照校订的旧译章节。其他旧译保持 `translation-unverified`；显式 `--role translation` 可审查历史。修正记录中的旧错误保存在完整JSON，默认校订检索只包含当前中文及证据。

默认综合查询中，已有当前图示分析的历史 `figure` 片段由当前 `diagram` 记录替代，避免已纠正的方向或撤销的连线重新进入答案。显式 `--role figure` 或 `--layer source` 仍可审查历史记录，结果同时给出 `current_diagram_analysis` 入口。撤销关系保留在 `rejected_edges` / 知识图谱的 `rejected_claims` 中，不能作为有效边。

全文 Markdown 的图片入口与 JSON 的 `pages[].current_image_analysis` 都指向当前解析；`figures/current-analysis.{md,json}` 保存完整路由。图示中的 `flows`、`tables`、`legend` 是当前内容，`source_flows`、`source_tables`、`source_legend` 保留历史归档及明确身份，默认架构检索排除这些旧载荷。原图中的连续连线可以穿过DORP等区域；途经区域与真实连接端点分别记录。

`quality.visual_review` 有四种状态：`source-content-audited` 已核对完整可见内容；`selected-facts-reviewed` 只核对登记的部分事实；`source-symbol-or-table-transcribed` 已转录原图中的独立图元或表格；`inherited-source-interpretation-with-new-normalization` 保留历史图意并作类型规范化。各状态不相互代替。全部图像的MD/JSON位置及剩余整图独立审校清单见 [conversion-coverage.md](../quality/conversion-coverage.md) 与 [conversion-coverage.json](../quality/conversion-coverage.json)。

正文使用 PDF 原始书签构建章节层级，同时保存未删减的逐页文本和带坐标文本块。整理后的 Markdown 去掉页眉页脚，并重组上标与断行。表格仅从实际边框提取；跨页表保持片段，合并单元格保留 `null`。图片文件同时保留源 PDF、原图坐标、数字文字、OCR、历史语义与本轮修正。

JSON 数据契约见 [文档 schema](schemas/document.schema.json) 与 [检索块 schema](schemas/chunk.schema.json)。检索图块按长度拆分，`parent_record_id`、`part`、`part_count` 用于还原完整记录；完整图形结构始终保存在独立 JSON 中。

`validate.py` 重新打开全部源 PDF，逐页核对原始文字、书签层级、表格单元格坐标及字符、正文检索覆盖、图像指纹和本地链接，并验证实际文档JSON契约。每个图像区域以相同坐标重新从原PDF渲染，逐像素比较RGB图像；结果写入 `quality/validation.json`。`test_corpus.py` 用构造 PDF 验证丢页、错列、检索丢块、图像被改及中英文查询的回归行为。架构验证进一步检查全图路由、历史载荷保留、当前修正、知识图与检索同步。数据契约见 [document.schema.json](schemas/document.schema.json) 和 [chunk.schema.json](schemas/chunk.schema.json)；实际来源一致性由验证器检查。

查看 [可读验证报告](../quality/validation.md) 与 [完整检查数据](../quality/validation.json)。

## 检索

查询工具只需要 Python 标准库，直接扫描 JSONL，无需数据库、外部服务或 API 密钥。以下命令返回 JSON，包含命中文本、文档编号、PDF 页码、章节、来源路径与 SHA-256、Markdown 路径、关联图及质量标记。

```sh
# 中文术语可检索英文原文，适合追溯定义。
python3 tools/togaf_corpus/query.py "业务能力" --lang en --role source --limit 5

# 在指定指南中查找英文片段。
python3 tools/togaf_corpus/query.py "value stream" --doc G178 --limit 5

# 查图内元素、关系和解释。
python3 tools/togaf_corpus/query.py "元数据" --doc G234 --role figure --limit 5

# 需要核对全文时返回完整片段。
python3 tools/togaf_corpus/query.py "架构治理" --doc G186 --full-text --limit 3
```

`--doc`、`--lang` 和 `--role` 可以重复；同一选项内为“或”，选项之间为“且”。语言取 `en` 或 `zh`，内容角色取 `source`、`translation`、`figure`、`architecture`、`role`、`diagram`、`concept` 或 `relationship`。`--limit` 取 1–100，默认 10。默认文本摘要最长约 700 个字符；`text_truncated=true` 时可使用 `--full-text`。用 `--corpus /绝对路径/togaf-standard-10th-ai` 指定其他构建目录。

默认排除目录、术语索引及含大量点线的导航片段，避免将目录标题误用为定义证据。需要查找目录时添加 `--include-navigation`；完整 JSONL 仍保留这些记录。`skipped_navigation_chunks` 返回此次排除数量。

中文检索使用来自既有中文 README 的术语表，将“业务能力”等术语扩展为 `Business Capability`、`Business Capabilities`，并结合原始词与中文双字词匹配。`expanded_terms` 明示扩展原因，`matched_terms` 明示命中词。这是词项检索，分数只用于排序；没有命中不代表标准没有讨论该主题，也不会生成问答事实。

## 使用来源

- `source`：英文 PDF 的抽取文本，可通过页码和指纹回到原件核对；排版抽取可能保留换行或表格阅读顺序问题。
- `translation`：既有中文稿，查询结果始终标记 `translation-unverified`；译者补充、摘要和原文不可互换。
- `chapter-review`：有来源单元覆盖的中文章节校订与分析；保留 `source-compared-revised` 或标题容器状态，不等同逐句对齐、原文或独立双人认证。
- `figure`：图片的文字、节点、关系和解释。阅读 `quality` 与记录中的依据，保留显式连线和推测关系的区别；中文自绘图不能当成原文图。

项目技能的使用约定见 [AI 语料接入说明](../../references/ai-corpus.md)。读取正文时保持章节上下文；使用表格和图示时读取其完整记录，引用时保存 `document_id`、`pdf_pages`、`source_sha256`。这些指南中的示例实体和方法建议不自动成为用户项目的架构事实。
