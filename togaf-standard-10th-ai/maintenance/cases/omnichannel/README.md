# 全渠道订单履约贯通案例

五版虚构案例连接任务、决策、职责、技能证据、接口、风险和过渡架构。当前共49对PNG/SVG，逐图对应实际目视指纹，428项生成文件指纹及51个来源引用已核对。三版角色配置主图直接表达全部7条关系；充分虚构两版各表达12条。真实业务批准未授予。

先读[原始业务材料](raw-business-materials.md)、[角色技能输入](role-skill-inputs.json)或[充分版原始业务材料](sufficient-business-materials.md)，再读模型和制品。未知、已证明的虚构结论与真实组织事实分开保存。

|版本|判断及范围|产物|PNG/SVG|
|---|---|---|---|
|baseline|缺一致性要求时保留同步/异步两个候选，人员能力及容量未知|[模型](generated/baseline/model.json) · [索引](generated/baseline/index.md)|9对|
|offline-change|增加离线受理与恢复；受理不等于最终承诺；12月1—4日配置缺口可见|[模型](generated/offline-change/model.json) · [索引](generated/offline-change/index.md)|10对|
|shared-object-change|CAP-RESERVE稳定ID重命名，目录/矩阵/路线图投影同步|[模型](generated/shared-object-change/model.json) · [共享投影](generated/shared-object-change/shared-object-projections.md)|10对|
|sufficient|明确虚构的一致性、实验、行为及容量证据支持限定范围的建议；培训不升级|[模型](generated/sufficient/model.json) · [索引](generated/sufficient/index.md)|10对|
|sufficient-policy-change|政策v2将离线限额/期限从2件24小时变为1件8小时；联动接口、风险、运营及过渡|[模型](generated/sufficient-policy-change/model.json) · [索引](generated/sufficient-policy-change/index.md)|10对|

充分版四项任务工作量8/16/24/32小时，对应可用量10/20/28/40小时，仅证明声明期间及任务内的虚构容量。新增行为观察及虚构评审人支持本次3级评价；保留原未评价记录和课程不变级记录。人员配置为`ready-for-owner-review`，批准为`not-granted`。

实验A160ms/B420ms仅支持本案例在线p95≤300ms目标下推荐A；成本、生产负载、安全与真实规模仍未知。离线订单保持待确认，中央原子预占成功后方能最终确认并进入物流。

## 当前验收

- [五版逐图及来源复核](current-delivery-review.md)：49对图像、32种独特PNG字节；长技能矩阵建议打开原尺寸或Markdown；静态PNG不支持点击。
- [通用配置表达检查](generated/assignment-verification.json)：三版7条实际关系全部在主图；缺主体/关系及冲突反例被拒绝。
- [跨指南验证](generated/cross-guide-verification.json)：14项。
- [业务语义变更回归](semantic-change-verification.md)：8项，拒绝结构通过但提供者/职责/物流语义错误的反例。
- [原始材料前向验证](forward-acceptance.json)：12项；独立程序不调用构建器，核对实际输出与原始输入，不等于不同评审人的最终盲审。
- [共享政策契约](shared-policy-contract.json)：稳定对象上的编辑性与业务政策变更分开，4类旧投影反例被拒绝。

早期问题及审阅保存在[原始独立审阅](independent-review.md)、[F08复核](f08-independent-verification.md)和[旧19对图像报告](review-history/closeout-v1/delivery-closeout-report.md)。旧报告只证明当时字节；当前以本页和当前图像报告为准。

## 复现

从项目根目录执行，所有脚本使用`togaf-standard-10th-ai/skills/`内运行时：

```bash
python3 -B togaf-standard-10th-ai/maintenance/cases/omnichannel/run.py
python3 -B togaf-standard-10th-ai/maintenance/cases/omnichannel/build_sufficient.py
python3 -B togaf-standard-10th-ai/maintenance/cases/omnichannel/verify_assignment.py
python3 -B togaf-standard-10th-ai/maintenance/cases/omnichannel/verify_cross_guide.py
python3 -B togaf-standard-10th-ai/maintenance/cases/omnichannel/verify_semantic_change.py
python3 -B togaf-standard-10th-ai/maintenance/cases/omnichannel/forward_acceptance.py
python3 -B togaf-standard-10th-ai/maintenance/cases/omnichannel/delivery_closeout.py
```

重生成改变PNG指纹后，视觉验证会失败，须实际查看新图后单独记录指纹。不会自动授予视觉通过。包内可迁移示例见[独立包案例](../../../skills/_shared/examples/omnichannel/README.md)。

真实组织仍需提供业务政策、任务工作量、完整期间容量、可审查的行为证据、实际决定人、风险接受者及批准记录。三版未知模型和两版充分虚构模型均不能代替这些事实。

## ADM全周期补充

[独立维护的原始材料](adm-business-materials.md) → [九阶段分析与94项来源步骤](generated-adm/summary.json) → [周期检查](generated-adm/adm-check.md) → [政策变更后必须重审](generated-adm/adm-policy-v2-needs-review.json)。阶段记录以稳定对象关联原有充分输入模型，B/C/D可并行；G记录限期实验豁免及关闭，H保留观察分母和新政策反馈。所有接受、实施与测量均为给定虚构情景，不表示真实批准。

[前向回归](adm-forward-acceptance.json)不调用构建器；从原始材料核对指数计算、依赖、豁免、效果口径及变更失效。它仍是同一实现者的另一个程序，不是不同评审人的语义验收。九阶段工作记录不冒充全部正式交付物的结构化组装。

```bash
python3 -B togaf-standard-10th-ai/maintenance/cases/omnichannel/build_adm_case.py
python3 -B togaf-standard-10th-ai/maintenance/cases/omnichannel/verify_adm_forward.py
```

## 同一情景的正式交付物贯通

新增[交付物材料补充](adm-delivery-materials.json)沿用上述原始业务材料与充分案例，另明确记录本轮作者新增的章节论证和沟通计划提案。新案例在同一模型内绑定9阶段、94来源步骤和23种候选正式交付物，共90个具体章节；阶段输出引用相应交付物，新增材料指纹进入阶段证据。原`generated-adm/`和0项正式交付物历史不被改写。

[本轮实际生成及前向验收](../../../../output/review-remediation-20261108/adm-verified/README.md)保存23份Markdown/JSON及33个视图。23项严格组装、13项前向断言和9项定向回归通过；缺章、假批准、缺阶段输出和政策2→1件/24→8小时的变化均有拒绝或失效证据。候选组装不代表全范围专业语义、图形目视或真实业务接受，所有真实批准保持未授予。

```bash
python3 -B togaf-standard-10th-ai/maintenance/cases/omnichannel/build_adm_delivery_case.py --out <新的证据目录>
python3 -B togaf-standard-10th-ai/maintenance/cases/omnichannel/verify_adm_delivery_forward.py --case <该证据目录>
python3 -B togaf-standard-10th-ai/maintenance/prepare_skill_examples.py --adm-delivery-case <该证据目录>
```

便携版单独位于[包内adm-delivery](../../../skills/_shared/examples/omnichannel/adm-delivery/README.md)，保留旧五版案例及旧ADM记录。应用迁移排期只选择给定窗口的两个工作包，未给应用生产迁移日期、预算、真实容量和签署的地方保留未知。
