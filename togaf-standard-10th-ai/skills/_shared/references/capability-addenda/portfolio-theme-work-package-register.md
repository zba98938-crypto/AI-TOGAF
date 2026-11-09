# 组合主题工作包分组

如何把工作包按主题排序并识别依赖、投资和资源？

依据：G186 §8.2表8-2、§8.3–8.5。字段结构与状态编码是项目操作规范，原始指南不随运行读取。

## 输入与缺口

范围、五维语境、所用目标与交付物版本；原始计划/访谈/验收/估算及来源ID；组织授权和容差规则；缺失时不代推。关键依据未知时给候选表、受影响ID与责任；不编造权重、阈值、估算、批准或实际完成。

## 字段语义

| 字段 | 含义 |
|---|---|
| name | 分组记录 |
| theme | 组合主题及目标来源 |
| work_package_id | TOGAF变革工作包稳定ID |
| change_kind | 保持/改进/新差异化/新市场的项目分类 |
| continuation | 新工作或本财年续作 |
| required_work_packages | 前置工作包ID，方向本项依赖所列项 |
| importance | 继承战略重要性及依据，不发明权重 |
| impact_start | 影响预计开始时间而非全部任务完成期 |
| effort | 工作量/单位/估算依据 |
| investment | 金额/币种/估算范围 |
| evidence_refs | 材料ID |
| allocation_note | 多主题复用不重复计资，分组理由 |

## 分析步骤

1. 从战略目标、当前路线和在建项目建立主题
2. 按稳定工作包ID区分新/续作与保持/改进分类
3. 记录战略重要性和前置依赖
4. 收集同口径工作量/投资/影响时点并标未齐字段
5. 检查循环、跨主题复用和资源争用后形成候选顺序

### 组合主题工作包分组

原始材料（历史材料已清理）组 `themes`。依表8-2列主题、名称、所需工作包、重要性、影响时点、工作量及投资；WP-SIGN依赖WP-ID，维护独立保持类，全部估算明确项目来源。

`artifact_id=portfolio-theme-work-package-register`；`profile_id=portfolio-theme-work-package-register-default`；`view_id=v-portfolio-theme-work-package-register-default`。完整表见生成索引（历史材料已清理）。

## 修改与反例

修改：WP-SIGN新增等待数据责任批准的前置WP-GOV。结果：新增前置记录，签收不能沿旧依赖序列启动。

反例：WP-ID依赖WP-SIGN形成循环；或一包同时keep/improve。结果：dependency-cycle或ambiguous-change-kind。

## 质量与追溯

- 表8-2空格表示架构信息未完整，不用0替代
- TOGAF变革工作包与PM的WBS叶任务不是同一概念
- 一个工作包不同时承担保持和改进分类；共享ID不重复预算

执行证据（历史材料已清理）分别记录模型、生成、修改、反例及表内表达。表格不进行图形视觉验收。工程执行不能替代业务审批和独立业务审查。
