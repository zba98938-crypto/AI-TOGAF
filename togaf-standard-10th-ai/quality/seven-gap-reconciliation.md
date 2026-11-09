# 七类能力缺口：2026-11-08当前交付与验收边界

三项P1的执行逻辑已修复，本轮又修复BPMN引用/事件规则、两项OCL语法适配、状态图共享端口和四框框架箭头。当前工程入口是[ADM完成验证](adm-completion-verification.json)；其`passed`字段在真实重跑、封存及入口校验完成后派生。旧复审报告、失败尝试和发布包保留历史字节。**完整能力及独立验收仍为`accepted=false`。**

|范围|当前实现及实际证据|仍未完成的范围|
|---|---|---|
|1. 方法行为与教学|72方法的案例结构约束和24项有界推理断言通过。44项专业判断方法完成201当前步骤的候选材料审阅；19份补充材料覆盖原先47个过程缺口。180功能行、71 DBRM源行、11部门和20 MDM运营条件已保存；12份完整表及4幅敏捷SVG/PNG实际生成。旧“8项缺专用教学案例”已过期。|盲测执行0，真实应用或冲刺执行0，人的方法/业务接受未授予。候选过程材料完整不等于实际专业判断成功。|
|2. 图形与制品|297规范配置、196制品族，含178图形配置与119表格配置；两布局及业务变更表达通过。修复后实际验证712 SVG、760 PNG，4个超大任务各以13片原尺寸PNG交付；712份SVG文字几何通过。四批逐图复核及修复后重看共148次，当前对应35配置/140版本路径、136种PNG字节。140对SVG仅内嵌字体子集不同，PNG及非字体SVG字节相同，差异哈希保留。状态端口及四框箭头原缺陷图与修复图分别保留。G152五箭头及19项原PDF裁剪仍保留来源纠错。|仍有143配置/572版本未逐图查看；完整178配置的专业语义、可读性和来源等价接受未完成。实际批次观察只支持其封存图；元数据变更有仅呈现在配套明细的个别限制，不补授人类或完整验收。|
|3. ADM框架与正式候选交付|[完整离线图册](../architecture/adm-flow/index.html)有13幅流程图，覆盖Preliminary、A–H、持续需求管理、94来源步骤、23交付物及196制品族。严格候选交付物23种/90章重新生成通过；同一完整案例另实际导出23份文档、33视图及20幅SVG/PNG。桌面、手机、键盘及所有流程图文字几何已检。|项目流程投影不授组织批准；所有文档仍为candidate。同一虚构案例的记录覆盖不证明生产执行或真实业务充分性。|
|4. 通用案例及严格章节|六项通用案例的充分、缺输入、变更材料保留。官方G249量表身份不再被夹具改名；实施治理模型四章可独立绑定。严格模式空章和未绑定必需章会阻断；单章显式输入不再自动串用为其他章支撑，草稿保留缺口。|通用案例的原生Agent业务评测及不同评审人的接受仍待执行。叙述、补充证据或同一角色的隐含复用不能替代正式章节绑定。|
|5. 正式建模语言|BPMN22个有限规则族附规范PDF指纹和定位，15事件/条件及23引用/Cancel反例独立复核。当前18原生测试、12公共CLI正反例通过。真实Java21后端保留425条OCL原正文，解析424条、执行337次，1 Lifeline规则待映射。两项适配仅作用于指纹锁定的执行正文。|673 UML/442 BPMN完整构造及语义未完成。StartEvent出边条件、单出边Activity条件等义务尚未实现；无容器Transition的规范`invalid`与后端`null/false`差异明确保留。1未映射规则不冒充通过。ArchiMate 4授权规范未取得，不用3.2代替。|
|6. 独立语义与业务验收|507个唯一评测ID已核查，原零模型工具链诊断保留输入、stderr及崩溃证据。先前冻结运行时在本轮源码改变后已过期，不能称为当前快照。|507是清单，原生全范围独立业务执行仍为0。隔离浏览器探针阻断；普通环境17项迁移通过不授原生隔离预检通过。正文、来源/业务的最终独立验收及真实组织批准未授予。|
|7. 状态、发布与证据|DTRA必须有非空行动文本及合法因素引用；缺`as_of`时豁免有效性未知并保留冲突阻断。修复后428项稳定源码回归零失败/零跳过。5712源码文件、两实际归档、依赖锁及来源映射一致；实际解包17迁移检查通过。594正式生成及最终只读台账结果以当前JSON为准。生成包还核对运行前后依赖文件集合与字节，不仅核对输出。|工程通过仅限报告所列范围。旧报告保留其版本，不更新旧哈希冒充重跑，不累加重叠套件为能力覆盖率。完整能力与独立接受保持false。|

当前可直接审查的产物：

- [ADM框架与完整流程图](../architecture/adm-flow/index.html)，[逐阶段与交付物说明](../architecture/adm-flow/README.md)。
- [297配置当前制品图册](../../output/adm-language-continuation-20261108/artifacts.html)，[同一案例23文档与33视图](../../output/adm-language-continuation-20261108/adm-delivery-after-four-box/index.md)。
- [44方法候选审阅及当前指纹](procedural-method-review-validation.json)，[实际材料/输出索引](../../output/adm-goal-20261108/methods/current-input-output-sha256.json)。
- [当前工程汇总](adm-completion-verification.json)，[发布字节校验](release-current-validation.json)，[实际归档迁移](portability-validation.json)。
- [实际视觉第一批](../../output/adm-language-continuation-20261108/visual-batch-01/REVIEW.zh-CN.md)、[第二批](../../output/adm-language-continuation-20261108/visual-batch-02/REVIEW.zh-CN.md)、[第三批](../../output/adm-language-continuation-20261108/visual-batch-03/index.md)、[第四批](../../output/adm-language-continuation-20261108/visual-batch-04/REVIEW.zh-CN.md)，[当前观察字节核查](../../output/adm-language-continuation-20261108/visual-current-coverage.json)，[四框修复后记录更正](../../output/adm-language-continuation-20261108/four-box-arrow-fix/actual-after-addendum/INDEX.zh-CN.md)，[当前原生渲染与拒绝证据](../../output/adm-language-continuation-20261108/native-after-four-box/index.md)。
- [425条OCL原文、适配与后端差异](../../output/adm-language-continuation-20261108/ocl/index.md)，[BPMN规范定位与反例](../../output/adm-language-continuation-20261108/bpmn-independent-review/index.md)。
- [全范围独立验收原记录](independent-semantic-acceptance.json)，[本轮原始发布/状态快照](../../output/adm-completion-20261108-172314/before/quality/completion-status.json)。

只读核查：`python3 -B togaf-standard-10th-ai/maintenance/verify_implementation_ledger.py`。它验证记录字节、输入指纹和明确结果，不更新证据或授予接受。
