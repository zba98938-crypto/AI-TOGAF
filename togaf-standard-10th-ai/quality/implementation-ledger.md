# 实施缺口与验证证据

本计划尚未全部完成。下表将章节分析、完整中文正文、程序验证、视觉审阅及真实批准分别记录。

|ID|任务|当前状态|实现/验证证据|剩余条件或适用边界|
|---|---|---|---|---|
|BOUNDARY|目录与来源边界|done|[quality/source-consolidation-verification.json](../quality/source-consolidation-verification.json)|按用户后续授权归并并删除旧资料目录；独有原件保留原字节，旧路径映射可追溯。根开发工程保留，不安装外部技能。|
|G217|A—H/需求管理与64标记反例|done|[maintenance/semantic-regression-report.json](../maintenance/semantic-regression-report.json)|依据本地表列和64个坐标核对；不产生Phase I。|
|GUIDES|26份指南逐节与原图审阅|done|[chapters/index.json](../chapters/index.json), [architecture/diagrams/index.json](../architecture/diagrams/index.json)|前置版权、机构、目录及导航未纳入中文修订范围的项仍单列。|
|FOUNDATION-ANALYSIS|六卷43章3附录逐节语义分析发布|done|[quality/extended-publication.json](../quality/extended-publication.json), [quality/extended-verification.json](../quality/extended-verification.json)|874个编号标题有章节特有的概念、适用、逻辑、决策、制品与边界；不冒充完整中文正文。|
|FOUNDATION-CHINESE|六卷完整编号中文正文译写与来源核对|done|[quality/chinese-body-verification.json](../quality/chinese-body-verification.json), [quality/chinese-body-author-review-final-volumes.json](../quality/chinese-body-author-review-final-volumes.json)|874小节、3522来源块；正文、表格和图注按块译写。作者重点来源复核不代替不同评审人逐句验收。|
|FOUNDATION-VISUAL|75图片引用和18提取表审查|done|[maintenance/fundamental-review-data/05-visual-review.json](../maintenance/fundamental-review-data/05-visual-review.json), [quality/extended-publication.json](../quality/extended-publication.json)|18包含17正文表及1前置贡献者表；视觉嵌套不自动转成来源未给出的连线或基数。|
|G226-ANALYSIS|G226补充解析|done|[supplementary/G226.json](../supplementary/G226.json)|2022 Version1.0 Playbook：75节、8图、3表/规格记录，保留经验性指导边界。|
|G226-CHINESE|G226完整编号中文正文译写与来源核对|done|[quality/supplementary-chinese-body-verification.json](../quality/supplementary-chinese-body-verification.json), [quality/g226-body-author-review.json](../quality/g226-body-author-review.json)|75节、764英文来源块、8原图；中文按节连续译写。不同评审人最终校核单列。|
|W242C|W242C中文原文、解析和源误释|done|[supplementary/W242C.json](../supplementary/W242C.json)|33节3图3表/术语；CNN及训练/培训等源问题保留。仅核本地中文，不宣称与英文W242逐句认证。|
|SOURCE-INTERFACE|网页/PDF来源及统一当前检索|done|[maintenance/publish_extended.py](../maintenance/publish_extended.py), [quality/extended-verification.json](../quality/extended-verification.json)|网页不伪造页码；来源指纹、正文块和解释性质分别记录。|
|CROSS-DOCUMENT|跨文档与任务链|done|[architecture/source-method-graph.json](../architecture/source-method-graph.json), [quality/execution-bridge.json](../quality/execution-bridge.json)|定义/引用/取代/冲突须有证据；一般联系保留解释性来源。任务原型需业务裁剪。|
|G249-P0-P1|G249原计划语义纠错及执行契约|done|[maintenance/semantic-regression-report.json](../maintenance/semantic-regression-report.json), [quality/local-runtime-regression.json](../quality/local-runtime-regression.json), [quality/execution-bridge.json](../quality/execution-bridge.json)|等级范围、未知、行为证据、协作关系、任务推导、发展复评、章节绑定和图/表绑定分开验证。|
|SKILL-MAP71|71项技能任务方法映射|done|[skills/_shared/references/g249/skill-task-map.json](../skills/_shared/references/g249/skill-task-map.json), [quality/execution-bridge.json](../quality/execution-bridge.json)|不拆成71个提示词；未定义专业术语记录补充来源需求；Chief/Segment无伪造官方列。|
|SKILLS-PACKAGE|17入口及共享资源依赖闭包|done|[skills/README.md](../skills/README.md), [skills/upstream-manifest.json](../skills/upstream-manifest.json), [skills/_shared/corpus/source-map.json](../skills/_shared/corpus/source-map.json)|复制字体、规范和本地来源；本地补丁及阅读链接派生记录可追溯。|
|METHOD-ROUTING|按关注点和ADM阶段更新方法|done|[skills/_shared/references/reviewed-method-routing.json](../skills/_shared/references/reviewed-method-routing.json)|Preliminary承接实践和角色配置，各领域按实际阶段路由；普通单图不要求人员评价。|
|FOUNDATION-RUNTIME|基础定义、阶段步骤与执行器贯通|done|[quality/foundation-execution-verification.json](../quality/foundation-execution-verification.json), [quality/foundation-contract-coverage.json](../quality/foundation-contract-coverage.json)|75项基础制品、23项交付物、10项阶段契约、94项来源步骤；绑定及程序反例通过不代替实际执行和语义验收。|
|ADM-TEACHING|ADM、制品、流程及各类层次的系统讲解|done|[skills/_shared/references/togaf-explained.md](../skills/_shared/references/togaf-explained.md)|区分架构全景粒度、域、抽象、演进、分解、类型实例、实现、治理协调及人事汇报；来源与项目解释分开。|
|ADM-FULL-CYCLE|基于原始业务材料的全周期虚构演练|done|[maintenance/cases/omnichannel/adm-forward-acceptance.json](../maintenance/cases/omnichannel/adm-forward-acceptance.json)|9阶段与持续需求管理94项来源步骤有具体工作记录；V2变更使旧证据失效。仅为给定虚构情景，不冒充全部正式交付物或组织批准。|
|REVIEW-REMEDIATION|当前复审修复、严格候选交付及稳定源码工程验证|done|[quality/adm-completion-verification.json](../quality/adm-completion-verification.json)|当前报告由实际重跑及当前输入/输出指纹派生；旧复审报告保留历史。工程通过不代替完整语言、全图或独立业务验收。|
|ADM-FLOW|ADM框架、制品链及完整流程图|done|[quality/adm-flow-verification.json](../quality/adm-flow-verification.json)|13幅可编辑流程图覆盖10工作域、94来源步骤、23交付物和196制品族；离线导航及文字几何已检。项目投影不授组织批准。|
|METHOD-CANDIDATES|44专业判断方法的逐步候选教学材料审阅|done|[quality/procedural-method-review-validation.json](../quality/procedural-method-review-validation.json)|201当前步骤；19份新材料补47步骤，12完整表与4敏捷图实际生成。候选材料审阅不等于盲测、真实应用或人的接受。|
|PROFILE-ENGINEERING|全量图形及表格配置的表达、栅格和稳定生成检查|done|[quality/adm-completion-verification.json](../quality/adm-completion-verification.json)|297配置、196制品族、712 SVG、760 PNG。原尺寸切片和文字几何通过；完整逐图语义、来源等价与视觉专业验收仍待完成。|
|NATIVE-NOTATION-SUBSETS|BPMN显式DI与UML类图子集的原生符号渲染|done|[quality/adm-completion-verification.json](../quality/adm-completion-verification.json)|12当前公共CLI正反例与真实PNG；只覆盖声明子集。673 UML/442 BPMN完整构造、1 Lifeline OCL映射缺口及ArchiMate 4不计为完成。|
|ASSIGNMENT-CONTRACT|通用任务角色配置及期间覆盖|done|[skills/_shared/scripts/assignment_projection.py](../skills/_shared/scripts/assignment_projection.py), [quality/local-runtime-regression.json](../quality/local-runtime-regression.json)|支持多个角色、任务、配置及观察；范围和期间独立；旧草稿缺语义返回缺口。|
|POLICY-CONTRACT|编辑性与业务政策变更及跨视图契约|done|[skills/_shared/scripts/policy_consistency.py](../skills/_shared/scripts/policy_consistency.py), [maintenance/cases/omnichannel/forward-acceptance.json](../maintenance/cases/omnichannel/forward-acceptance.json)|政策变更联动接口、风险、运营、过渡及验证；不自动授予批准。|
|UNKNOWN-CASES|三版未知案例保留与全量渲染|done|[maintenance/cases/omnichannel/generated/summary.json](../maintenance/cases/omnichannel/generated/summary.json), [maintenance/cases/omnichannel/generated/assignment-verification.json](../maintenance/cases/omnichannel/generated/assignment-verification.json)|三版9/10/10幅PNG及SVG；能力和容量未知，离线期间缺口不自动延长。|
|SUFFICIENT-CASE|输入充分与政策变更虚构案例|done|[maintenance/cases/omnichannel/sufficient-results.json](../maintenance/cases/omnichannel/sufficient-results.json), [maintenance/cases/omnichannel/sufficient-business-materials.md](../maintenance/cases/omnichannel/sufficient-business-materials.md)|两版各10幅图，四项配置及发展复评有明确虚构依据；不证明生产或真实组织事实。|
|FORWARD-REVIEW|从原始材料前向验证|done|[maintenance/cases/omnichannel/forward-acceptance.json](../maintenance/cases/omnichannel/forward-acceptance.json)|独立验证程序不调用构建器；同一实现者复核，与不同评审人的盲审区分。|
|VISUAL-CLOSEOUT|五版逐图当前指纹复核|done|[maintenance/cases/omnichannel/current-delivery-review.json](../maintenance/cases/omnichannel/current-delivery-review.json)|只有当前指纹和实际目视记录全部匹配时完成。|
|PORTABILITY|隔离位置检索校验生成渲染|done|[quality/portability-validation.json](../quality/portability-validation.json)|通过后仍明确系统Python/Node及现有浏览器依赖；不把同机迁移等同跨平台认证。|
|INSTALLABLE|交付可安装归档、依赖和指纹|done|[release/release-manifest.json](../release/release-manifest.json)|归档只在AI目录；不得安装到外部技能目录。|
|READING-LINKS|当前入口、来源和内部链接|done|[skills/reading-link-manifest.json](../skills/reading-link-manifest.json), [quality/current-entrypoint-links.json](../quality/current-entrypoint-links.json)|当前包内Markdown链接必须存在且不逃逸包；当前总入口核对文件及锚点；源文外部引文不作为联网已验证。|
|INDEPENDENT-SEMANTIC|全部正文图表的最终独立语义验收|pending|[quality/independent-semantic-acceptance.json](../quality/independent-semantic-acceptance.json)|六卷/G226须在全文校订后进行不同评审人的来源对照，不能由作者自检和程序通过代替。|
|REAL-BUSINESS|真实组织的业务/人员/容量及批准|external-condition|[maintenance/cases/omnichannel/raw-business-materials.md](../maintenance/cases/omnichannel/raw-business-materials.md)|保留真实待办，不编造。该条件不阻止教学包交付，但不得记作已批准。|

工程完成字段仅限本表资料整理与交付计划，不表示全量方法、图形配置、正式建模语言或业务能力已验收。当前能力范围见[七类缺口核查](seven-gap-reconciliation.md)。
实际中文正文已译写949个编号小节；仍有0个来源小节待全文译写，见[逐来源工作清单](chinese-text-worklist.json)。已写正文待不同评审人的最终校核；语义分析不能代替中文全文。
