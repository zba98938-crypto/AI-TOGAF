# TOGAF 标准与系列指南 AI 可读语料

本轮当前状态见[本地工程稳定化维护](maintenance/stabilization/README.md)。本轮源码正在修复与补齐，尚未执行完整507项独立评测或切换真实入口。下列历史质量报告、图册和中文作者复核记录保留原有范围；模型复核、人工专业验收与真实组织批准分别记录。

以已归并到本目录的26份英文指南PDF为源，保存完整正文、表格、图片语义和可追溯检索块。另保存用户指定的2025数字版六卷基础正文（43章、3附录）。26份系列指南、六卷基础正文及G226/W242C现有逐节语义分析；六卷874个编号小节、3522个来源块已完成中文正文译写；G226另有75节中文正文和764个精确英文来源块，W242C中文原文逐页保全。作者重点来源复核已记录，不同评审人的最终语义验收仍待完成。当前状态以[实施证据与缺口](quality/implementation-ledger.md)为准。

## 从这里读取

- [ADM框架与完整流程图](architecture/adm-flow/index.html)：Preliminary、A–H、持续需求管理、94来源步骤及13幅流程图。
- [当前制品与图形图册](../output/adm-language-continuation-20261108/artifacts.html)，[完整案例的23份候选交付物与33视图](../output/adm-language-continuation-20261108/adm-delivery-after-four-box/index.md)。
- [当前工程证据及七类验收边界](quality/seven-gap-reconciliation.md)：工程检查、专业语义接受和真实组织批准分别记录。

- [唯一来源保存位置与旧路径迁移清单](sources/README.md)：旧资料目录已去重归并，历史路径不再代表当前磁盘位置。

- [ADM、制品、流程及层次关系的系统解释](skills/_shared/references/togaf-explained.md)。
- [基础标准执行验证](quality/foundation-execution-verification.json)：75项基础制品、23项交付物及94个来源步骤的绑定与反例。
- [全周期ADM虚构案例](maintenance/cases/omnichannel/generated-adm/adm-check.md)及[独立原始材料](maintenance/cases/omnichannel/adm-business-materials.md)。

- [目录内可运行skills包](skills/README.md)：17个入口、本地来源与共享执行器；[安装归档](release/README.md)。
- [六卷及补充资料解析](quality/extended-publication.md)：982个小节分析、86处图像引用及24张表/规格记录。

- [六卷实际中文正文](fundamental/chinese-text/README.md)：874个编号小节、3522个来源块；[G226与W242C中文正文](supplementary/chinese-text/README.md)。正文译写、作者复核和最终独立验收分别记录。
- [六卷基础标准本地副本](fundamental/web-2025/README.md)：完整MHTML、离线HTML、英文MD/JSON与获取审计。
- [本地来源与基础标准范围](fundamental/README.md)：保留初次本地清点与后续用户授权保存记录，区分基础正文与补充资料。
- [全渠道履约贯通案例](maintenance/cases/omnichannel/README.md)：任务、角色、技能证据、接口、风险与过渡状态的联合验证。
- [实际完成状态](quality/completion-status.md)：区分维护记录、已发布解析、验证与业务验收。

- [架构解析、图示关系与角色能力](architecture/README.md)：架构实体、方向、分类层级、角色职责及全部参考技能等级。
- [转换覆盖与视觉审校清单](quality/conversion-coverage.md)：全部文档和图像的输出位置、实际覆盖及剩余独立审校范围。
- [当前图片解析](figures/current-analysis.md)：已集成的当前解释与质量状态，关联原图及历史转录。
- [中文阅读导航](reading-guide.md)：各指南用途、核心概念、项目适用场景与原文页码；标记为派生阅读指南。
- `index.json`：文档目录、源文件 SHA-256、页数与路径。
- `documents/*.md`：英文全文；章节和物理页码；正文、列表、表格与图片解释入口。
- `documents/*.json`：全文、PDF 书签层级、原始逐页文本、字体/坐标、链接、表格和来源；`pages[].current_image_analysis` 直接指向当前图示解析。
- `tables/*.json`：真实边框提取的表格片段，保留合并单元格及坐标，跨页不臆测合并。
- `figures/index.json` 和 `figures/<文档>/*.{md,json}`：图片标签、元素、包含关系、箭头、流程、矩阵及解释；原图证据与历史解读分别记录。
- `translations/*.{md,json}`：既有中文全文与章节定位；标记 `translation-unverified`，不宣称已重新完整翻译。
- `retrieval/chunks.jsonl`：可直接供检索使用的内容块；每条带语言、来源角色、物理页码和证据指纹。
- [quality/validation.md](quality/validation.md)：转换覆盖、单元格和来源验证结果；同目录保存中英章节定位报告。

## 项目使用规则

1. 先按主题检索，再读取完整章节及相邻页；不要把目录条目当作正文证据。
2. 以英文 `source` 为引用依据；优先使用 `chapters/` 的当前中文校订与方法分析。`translations/`和`figures/`保存历史转录，不能替代当前解释。
3. 指南页码以PDF物理页为准，从封面计第1页；基础网页正文按卷、标题锚点和内容块ID定位。当前章节分析附精确来源证据；历史中文定位仅按编号，不证明语义等价。
4. 指南中的样例实体、关系和方案不自动构成当前项目事实。
5. 原始文本完整保存在 JSON 的 `pages[].raw_text`；页眉、页脚和水印从整理后正文移除但仍可追溯。
6. 图示的 `flows`、`tables`、`legend` 为当前内容；`source_flows`、`source_tables`、`source_legend` 是归档的历史记录，已从默认架构检索文本排除。按 `quality.visual_review` 读取独立审校范围。

## 构建和查询

在项目根目录执行：

```bash
python3 -B togaf-standard-10th-ai/maintenance/publish.py
node togaf-standard-10th-ai/maintenance/pipeline/verify_architecture_mermaid.mjs
node togaf-standard-10th-ai/maintenance/pipeline/verify_architecture_explorer.mjs
python3 -B togaf-standard-10th-ai/maintenance/verify.py
python3 -B togaf-standard-10th-ai/skills/_shared/scripts/local_tool.py query '业务能力 价值流' --limit 5
```

本轮维护入口见 [维护说明](maintenance/README.md)，发布器限制所有写入在本目录内。旧原始转换工具用于历史来源追溯，不会读取本轮新增的维护记录。

依赖和数据模型见 [转换工具说明](../tools/togaf_corpus/README.md)。

## 文档

|编号|中文名称|英文全文|结构化 JSON|页数|
|---|---|---|---|---|
|G152|将风险与安全融入TOGAF企业架构|[Markdown](documents/G152.md)|[JSON](documents/G152.json)|45|
|G176|业务场景|[Markdown](documents/G176.md)|[JSON](documents/G176.json)|53|
|G178|价值流|[Markdown](documents/G178.md)|[JSON](documents/G178.json)|28|
|G184|领导者指南_建立并演进EA能力|[Markdown](documents/G184.md)|[JSON](documents/G184.json)|138|
|G186|实践者方法_按TOGAF_ADM开发企业架构|[Markdown](documents/G186.md)|[JSON](documents/G186.json)|161|
|G188|架构项目管理|[Markdown](documents/G188.md)|[JSON](documents/G188.json)|94|
|G18A|业务模型|[Markdown](documents/G18A.md)|[JSON](documents/G18A.json)|30|
|G190|信息映射|[Markdown](documents/G190.md)|[JSON](documents/G190.json)|27|
|G198|架构技能框架|[Markdown](documents/G198.md)|[JSON](documents/G198.json)|27|
|G203|架构成熟度模型|[Markdown](documents/G203.md)|[JSON](documents/G203.json)|22|
|G206|组织映射|[Markdown](documents/G206.md)|[JSON](documents/G206.json)|25|
|G20F|赋能企业敏捷性|[Markdown](documents/G20F.md)|[JSON](documents/G20F.json)|48|
|G210|以敏捷冲刺应用TOGAF_ADM|[Markdown](documents/G210.md)|[JSON](documents/G210.json)|41|
|G211|业务能力|[Markdown](documents/G211.md)|[JSON](documents/G211.json)|29|
|G212|数字技术采用就绪度评估|[Markdown](documents/G212.md)|[JSON](documents/G212.json)|57|
|G217|在数字企业中使用TOGAF标准|[Markdown](documents/G217.md)|[JSON](documents/G217.json)|90|
|G21B|信息架构_客户主数据管理|[Markdown](documents/G21B.md)|[JSON](documents/G21B.json)|58|
|G21D|政府参考模型|[Markdown](documents/G21D.md)|[JSON](documents/G21D.json)|76|
|G21H|TOGAF数字业务参考模型|[Markdown](documents/G21H.md)|[JSON](documents/G21H.json)|52|
|G21I|微服务架构|[Markdown](documents/G21I.md)|[JSON](documents/G21I.json)|53|
|G233|业务能力规划|[Markdown](documents/G233.md)|[JSON](documents/G233.json)|59|
|G234|信息架构_元数据管理|[Markdown](documents/G234.md)|[JSON](documents/G234.json)|45|
|G238|信息架构_商业智能与分析|[Markdown](documents/G238.md)|[JSON](documents/G238.json)|44|
|G242|环境可持续的信息系统|[Markdown](documents/G242.md)|[JSON](documents/G242.json)|105|
|G248|构建块的选择方法|[Markdown](documents/G248.md)|[JSON](documents/G248.json)|47|
|G249|架构角色与技能|[Markdown](documents/G249.md)|[JSON](documents/G249.json)|33|









中文章节校订入口：[26 份指南的当前校订与剩余覆盖](chapters/index.md)；机读记录见 [JSON](chapters/index.json)。
