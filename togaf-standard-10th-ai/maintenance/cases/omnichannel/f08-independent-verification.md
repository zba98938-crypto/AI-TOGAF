# F08 独立复核：角色分配制品

**结论：原来的空主目录问题已实质修复。4个角色、4项任务、1项配置、2项能力证据均在主目录和实际PNG中可见。7条关系是整个制品包的覆盖；主图直接显示5条，另外2条只在明细页。**

本次为独立AI复核，仅审查保存的 `offline-change` 制品；不是业务批准、人员评级、技能认证或上线授权。未重跑 `run.py`，未修改输入、生成文件或覆盖状态。

| 检查对象 | 主目录/主图 | JSON与明细 | 结论 |
| --- | --- | --- | --- |
| 角色 | 4个，均有职责与任务 | 4个 | 可直接回答谁负责什么 |
| 任务 | 4项，有预期成果、要求及未决条件 | 4项 | 不再隐藏于分析上下文 |
| 人员配置 | ASSIGN-A，可见PERSON-A、期限、40小时、未知工作量、未批准 | 1项 | 候选状态保留 |
| 能力证据 | EVIDENCE-A与EVIDENCE-EXPERT均有独立记录 | 2项 | 当前等级均未知 |
| 角色到任务关系 | 4条主图箭头 | 4条 | 直接可见 |
| 配置到任务关系 | 1条主图箭头 | 1条 | 直接可见 |
| 配置到证据关系 | 主图没有这2条箭头 | 明细页有源、目标与语义 | 不应称主图7条关系全部可见 |

## 已核对的未知与约束

- 甲缺少异常接口设计评审证据；专家只有一项行为记录。两人的当前等级均为未知，未自动记2级、3级或4级。
- 4项任务工作量均未知。40小时候选投入与8小时专家支持不证明容量足够，`capacity_state`仍为`unresolved`。
- 首席、企业和库存分段三个角色尚未配置具体人员，期限和容量待明确。
- ASSIGN-A有效期为2026-11-07至2026-11-30；离线工作包候选结束日为2026-12-04。12月1日至4日续任、替代或交接及容量缺口直接列为`GAP-ASSIGNMENT-PERIOD`，未自动延长。
- 四项3级要求为虚构项目裁剪目标。`optimistic-pessimistic-patterns`定义与项目目标仍未解决。
- 断连恢复要求进入TASK-SOL及发展行动，未覆盖或升级已有人员评价。复评仍是计划，等级变化为`not-inferred`。
- 经营负责人仅委托分析，最终决定人、风险接受者和审批机制待确认；配置`approval=not-granted`。

## 图片与覆盖记录

实际查看了1590×1179的PNG，全部11个主体清楚可辨，未发现主体框被截断。SVG的实体标识与主表一致。5条主图箭头包括4条角色到任务，以及ASSIGN-A到TASK-SOL。两个证据主体有可读状态，但对应的配置关系只在明细页。覆盖记录准确区分`main`与`companion`，没有把这2条关系登记为主图表达。

`errors=[]`与`unrepresented=[]`说明当前表达契约的制品包覆盖成立；不能据此推定单图包含所有字段、业务条件已经满足或业务批准已取得。覆盖状态仍为`generated-awaiting-review`，布局仍为项目表达且`source_verified=false`。

若交付要求是单张图片独立表达全部7条关系，还应加入两条配置到证据的连线。PNG中`None`等字段形式可进一步改成“未知”，但现有中文说明已保留其含义。

## 来源与范围

回查了同目录的原始业务材料和角色技能输入，核对CASE-MANDATE、CASE-BASELINE、CASE-CHANGE及人员行为记录，并从保存模型核实工作包期限。制品里部分人员来源locator仍为旧相对路径，本次按任务指定的本地材料核对内容，没有把旧路径宣称为已归一化的可点击来源。

本次不自动覆盖其他案例变体或其他缺陷；未重跑生成器或检查删除主体后的负向覆盖行为。完整证据、关系可见性及文件SHA-256见[f08-independent-verification.json](f08-independent-verification.json)。

受检主制品：[角色分配说明](generated/offline-change/artifacts/role-assignment.md) · [PNG](generated/offline-change/artifacts/role-assignment.png) · [关系明细](generated/offline-change/artifacts/role-assignment.details.html) · [覆盖记录](generated/offline-change/artifacts/role-assignment.coverage.json)
