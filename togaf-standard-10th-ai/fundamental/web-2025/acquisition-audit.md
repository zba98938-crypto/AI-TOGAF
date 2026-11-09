# TOGAF 基础标准网页快照采集审计

审计对象为本地六份 Single Page View MHTML，均标注 2022 年 4 月出版、2025 年 5 月纳入 Technical Corrigendum 1。仅检查采集完整性，尚未完成正文深度解析。

六卷共 **43 章、3 个附录**。全部章节与附录均在目录和正文中存在，编号连续且正文非空；81 处图片引用对应 79 个封装图片资源，全部成功解码。

| 文件 | 官方卷名 | 章 | 附录 | 目录锚点已找到/总数 | 图片引用/资源 |
|---|---|---:|---:|---:|---:|
| [01-introduction-and-core-concepts.mhtml](01-introduction-and-core-concepts.mhtml) | TOGAF® Standard — Introduction and Core Concepts | 4 | 3 | 197/198 | 15/15 |
| [02-architecture-development-method.mhtml](02-architecture-development-method.mhtml) | TOGAF® Standard — Architecture Development Method | 13 | 0 | 267/268 | 17/17 |
| [03-adm-techniques.mhtml](03-adm-techniques.mhtml) | TOGAF® Standard — ADM Techniques | 9 | 0 | 100/101 | 11/11 |
| [04-applying-the-adm.mhtml](04-applying-the-adm.mhtml) | TOGAF® Standard — Applying the ADM | 4 | 0 | 31/31 | 10/10 |
| [05-architecture-content.mhtml](05-architecture-content.mhtml) | TOGAF® Standard — Architecture Content | 7 | 0 | 246/246 | 23/21 |
| [06-ea-capability-and-governance.mhtml](06-ea-capability-and-governance.mhtml) | TOGAF® Standard — Enterprise Architecture Capability and Governance | 6 | 0 | 89/90 | 5/5 |

**已确认的限制**

- 4 个卷标题目录锚点缺失（01、02、03、06），可见标题仍在；未发现章节或附录断链。总计 1308 个同页 fragment 引用中仅这 4 个缺失。
- 六卷范围内可确定映射的 332 个跨页或跨卷链接未发现目标缺失；其他外部网址未联网验证。
- 每卷 3 份 CSS 均已封装，但字体依赖未封装，共 40 个不同的字体 URL。离线可能出现字体回退和界面图标缺失，正文图片均存在。
- 每卷侧栏均重复使用 `toctitle` 14 次；未见正文 id 重复。
- 原始链接保留官方绝对网址；本审计不重写链接、不生成正文衍生文件，未进行离线浏览器视觉验收。

**缺失的卷标题锚点**

- `01-introduction-and-core-concepts.mhtml`：`_togaf_standard_introduction_and_core_concepts`。
- `02-architecture-development-method.mhtml`：`_togaf_standard_architecture_development_method`。
- `03-adm-techniques.mhtml`：`_togaf_standard_adm_techniques`。
- `06-ea-capability-and-governance.mhtml`：`_togaf_standard_enterprise_architecture_capability_and_governance`。

**章节与附录清单**

**TOGAF® Standard — Introduction and Core Concepts**

- `chap01` — 1. Introduction；正文 17,982 字符，目录对应已核查。
- `chap02` — 2. The TOGAF Documentation Set；正文 7,553 字符，目录对应已核查。
- `chap03` — 3. Core Concepts；正文 46,878 字符，目录对应已核查。
- `chap04` — 4. Definitions；正文 21,957 字符，目录对应已核查。
- `apdxa` — A: Referenced Documents；正文 11,182 字符，目录对应已核查。
- `apdxb` — B: Glossary of Supplementary Definitions；正文 8,414 字符，目录对应已核查。
- `apdxc` — C: Acronyms and Abbreviations；正文 3,276 字符，目录对应已核查。

**TOGAF® Standard — Architecture Development Method**

- `chap01` — 1. Introduction；正文 34,210 字符，目录对应已核查。
- `chap02` — 2. Preliminary Phase；正文 27,361 字符，目录对应已核查。
- `chap03` — 3. Phase A: Architecture Vision；正文 27,439 字符，目录对应已核查。
- `chap04` — 4. Phase B: Business Architecture；正文 35,158 字符，目录对应已核查。
- `chap05` — 5. Phase C: Information Systems Architectures；正文 1,900 字符，目录对应已核查。
- `chap06` — 6. Phase C: Information Systems Architectures — Data Architecture；正文 24,301 字符，目录对应已核查。
- `chap07` — 7. Phase C: Information Systems Architectures — Application Architecture；正文 20,884 字符，目录对应已核查。
- `chap08` — 8. Phase D: Technology Architecture；正文 24,961 字符，目录对应已核查。
- `chap09` — 9. Phase E: Opportunities & Solutions；正文 20,754 字符，目录对应已核查。
- `chap10` — 10. Phase F: Migration Planning；正文 16,138 字符，目录对应已核查。
- `chap11` — 11. Phase G: Implementation Governance；正文 10,532 字符，目录对应已核查。
- `chap12` — 12. Phase H: Architecture Change Management；正文 17,824 字符，目录对应已核查。
- `chap13` — 13. ADM Architecture Requirements Management；正文 10,541 字符，目录对应已核查。

**TOGAF® Standard — ADM Techniques**

- `chap01` — 1. Introduction；正文 1,605 字符，目录对应已核查。
- `chap02` — 2. Architecture Principles；正文 41,465 字符，目录对应已核查。
- `chap03` — 3. Stakeholder Management；正文 19,128 字符，目录对应已核查。
- `chap04` — 4. Architecture Patterns；正文 10,383 字符，目录对应已核查。
- `chap05` — 5. Gap Analysis；正文 2,938 字符，目录对应已核查。
- `chap06` — 6. Interoperability Requirements；正文 12,971 字符，目录对应已核查。
- `chap07` — 7. Business Transformation Readiness Assessment；正文 18,335 字符，目录对应已核查。
- `chap08` — 8. Risk Management；正文 8,457 字符，目录对应已核查。
- `chap09` — 9. Architecture Alternatives and Trade-Offs；正文 5,903 字符，目录对应已核查。

**TOGAF® Standard — Applying the ADM**

- `chap01` — 1. Introduction；正文 4,804 字符，目录对应已核查。
- `chap02` — 2. Applying Iteration to the ADM；正文 20,404 字符，目录对应已核查。
- `chap03` — 3. Applying the ADM Across the Architecture Landscape；正文 5,194 字符，目录对应已核查。
- `chap04` — 4. Architecture Partitioning；正文 10,169 字符，目录对应已核查。

**TOGAF® Standard — Architecture Content**

- `chap01` — 1. Introduction；正文 12,251 字符，目录对应已核查。
- `chap02` — 2. TOGAF Content Framework and Enterprise Metamodel；正文 32,702 字符，目录对应已核查。
- `chap03` — 3. Architectural Artifacts；正文 73,373 字符，目录对应已核查。
- `chap04` — 4. Architecture Deliverables；正文 27,491 字符，目录对应已核查。
- `chap05` — 5. Building Blocks；正文 8,677 字符，目录对应已核查。
- `chap06` — 6. Enterprise Continuum；正文 25,139 字符，目录对应已核查。
- `chap07` — 7. Architecture Repository；正文 17,649 字符，目录对应已核查。

**TOGAF® Standard — Enterprise Architecture Capability and Governance**

- `chap01` — 1. Introduction；正文 1,109 字符，目录对应已核查。
- `chap02` — 2. Establishing an Architecture Capability；正文 10,692 字符，目录对应已核查。
- `chap03` — 3. Architecture Governance；正文 21,927 字符，目录对应已核查。
- `chap04` — 4. Architecture Board；正文 12,532 字符，目录对应已核查。
- `chap05` — 5. Architecture Contracts；正文 8,485 字符，目录对应已核查。
- `chap06` — 6. Architecture Compliance；正文 16,157 字符，目录对应已核查。

**证据与边界**

机器可读审计见 [acquisition-audit.json](acquisition-audit.json)，包含快照 SHA-256、源 URL、MIME 保存时间、完整目录核查、图片尺寸/哈希/解码状态及字体缺失明细。

本结论只证明本地快照目录、正文结构和图片附件的内部一致性；不证明与在线原文逐句一致，也不表示已完成翻译、语义规则提炼、图表建模或 skills 能力开发。

**衍生离线 HTML 复核**

另行只读核查6份 `volumes/*/index.html`：检查 1827 处本地资源或锚点引用，发现 0 处缺失。本地图片均存在；`source.html` 与MHTML中的原HTML字节一致，离线版正文容器文字保持一致。4个卷标题锚点已在衍生离线版修复，原始快照未修改。

该附加核查仍是文件及锚点检查，未进行浏览器视觉验收，也不改变原始MHTML的字体及外部链接限制。
