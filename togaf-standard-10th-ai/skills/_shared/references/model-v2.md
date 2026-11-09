# 共享模型 v2 与分析计算接口

这是本技能集合的项目接口约定，不是 TOGAF 官方交换格式或完整内容元模型。v1 模型仍可验证；新功能使用 schema_version `2.0`。

## 身份、视图与状态

- `artifact_id` 表示制品族；`profile_id` 选择有来源的表达规范；`view.id` 是输出视图身份。同族可有多个范围、模板及演进状态。
- `context` 保留架构域、全景层级、架构目的、抽象层次、演进状态五维，彼此独立。批准由 `approval_status`（unknown/candidate/in-review/approved/rejected/withdrawn）记录，实现由 `implementation_status`（unknown/not-started/in-progress/realized/retired）记录。`approval_evidence` 与 `implementation_evidence` 分别提供证据；批准不能推断已实现，已实现也不保证已批准。
- `decision_status` 的 candidate/approved/realized 仅为 v1 兼容字段。新项目与交付物可只提供上述两个独立状态；迁移保留旧字段但不猜测两种状态。新旧字段互相矛盾会报错。
- `states[]` 为可命名架构状态，含 `id/name/evolution`。对象、关系和视图可用 `state_id` 引用；多个 transition 状态不会覆盖。
- `scopes[]` 说明范围，`scope_id` 可用于限制版本比较。`concept_id` 对齐跨状态的业务概念，`id` 表示具体模型版本，不能用显示名称替代身份。
- `comparisons[]` 可同时指定 `baseline_state_id` 与 `target_state_id`，明确选取任意两个命名状态，包括两个不同的 transition；`state_ids` 限定参与比较的状态集合。不填这两个选择器时保留 v1 的 baseline/target 分类约定。比较实体、差距、状态、范围均检查引用；同属 transition 不意味着可混入一个命名状态视图，比较视图须显式设置 `allow_mixed_evolution:true`。
- 过渡状态的 `operating_conditions` 应说明 `operations/data_consistency/dependencies/controls/rollback`。条件缺失会报告可运营性缺口，不能把单纯日期当作可运营架构。

示例：

```json
{
  "states": [
    {"id":"t1","name":"双系统共存","evolution":"transition",
     "operating_conditions":{"operations":"两端持续服务","data_consistency":"增量同步并对账","dependencies":"先完成客户标识映射","controls":"双写审计","rollback":"切回原订单入口"}},
    {"id":"t2","name":"新系统主写","evolution":"transition"}
  ]
}
```

## 关系与数量

`metamodel.json` 补充核心对象及有向关系。`capability_instance` 通过 `instance_of` 关联唯一能力类型，或使用反向 `has_instance`；阶段可通过 `stage_uses_instance` 关联实例。实例组成、能力分解和视觉包含分别使用 `instance_comprises/decomposes/visually_contains`。

`uses_information` 和 `modifies_information` 的方向都是主体指向信息对象；具体图形可为阅读需要显示反向箭头，但应明确映射到原关系与图例。聚合、组合、泛化使用独立关系，不从摆放位置推断。

每端基数采用：

```json
{"source":{"min":1,"max":2},"target":{"min":1,"max":null}}
```

`max:null` 表示无界；`{"unknown":true}` 表示未知。未知不能填写 `min:0`，有界数值不能自动降为 `many`。

扩展对象与关系分别在 `extensions.entity_types`、`extensions.relationship_types` 声明，关系须明确端点类型与含义；键使用如 `project:approves` 的命名空间。`extensions.data` 和 `extension_data` 的顶层键也须有命名空间，其内部任意负载保持不透明。扩展不能覆盖已有核心对象或关系。显式迁移将旧的未命名类型改为无冲突的 `legacy:name`，同时更新类型引用；原名和新名保存在 `extension_data["togaf:migration"].vocabulary_renames`。第一版 v2 的 `legacy_unrecognized_fields` 仅作为兼容保留的迁移档案键。

## 度量与量表

对象的 `measurements[]` 每条包含 `dimension/value/unit/evidence`，使用 `period` 记录观察时点或统计期间、`method` 或 `calculation_basis` 记录测量／计算依据，规则来源用 `method_evidence` 引用；可补 `scale_id/uncertainty`。草稿缺少时间、依据或证据会产生明确警告，不能据结构通过认定完成评价。`scales[]` 定义离散评价锚点及证据；值不属于锚点、锚点重复、度量单位与量表单位冲突均被拒绝。不同维度、量表或单位不能直接比较。连续指标不应错误引用离散量表。

环境指标还需在属性中保留生命周期范围、Scope、年度、分摊与排放因子；单位字段本身不证明核算边界正确。

## 显式规则计算

模型的 `analyses[]` 是可选的确定性分析输入，含 `id/method_id/inputs/evidence`。运行 `analyze.py model.json --evaluate 分析ID` 得到结果；它不改变原模型，也不批准结论。领域判断和未提供确定规则的评估由技能方法完成。

### 决策矩阵

`weighted-normalized-decision` 要求 `rule_evidence`、`criteria[]` 和 `options[]`。每个判据包含 `id/weight/min/max/direction`，方向为 `maximize` 或 `minimize`；每个方案提供 `scores`。

先按明确硬约束将不合格方案标为 `eligible:false` 并记录 `reason`。计算器将合法范围内的评分线性归一化，按声明权重计算；缺评分、区间无效或权重和为零会拒绝计算。排序不自动打破同分，也不代表方案已被采用。

```json
{"id":"choice","method_id":"weighted-normalized-decision","inputs":{
 "rule_evidence":["project-criteria"],
 "criteria":[{"id":"cost","weight":1,"min":0,"max":100,"direction":"minimize"}],
 "options":[{"id":"a","scores":{"cost":20}},{"id":"b","scores":{"cost":60}}]
}}
```

### 偏好评分矩阵

`preference-weighted-decision` 用于 G176 式偏好矩阵：`rule_evidence`、`criteria:[{id,weight}]`、`options:[{id,scores}]`；单元是 1—5 最差至最佳的偏好值。权重缺省为 1，结果包含加权和及加权均值。成本已是偏好值，5 最佳，不再反向；原始金额先按有证据的锚点转换。

### DTRA 因素复核

`dtra-factor-review` 要求 `rule_evidence`、`factor_rating_rule`、`factors[]`。每因素包含 `id/category/rating/evidence`，类别是 `foundational/impact/sustaining`，等级为 1—7；十五个稳定因素 ID 及可运行输入见 计算案例（历史材料已清理）。数值管理关注阈值通过 `attention_min_rating` 与 `attention_threshold_evidence` 显式声明为项目映射，没有默认 6 分线；缺阈值、缺因素或基础未满足时不赋就绪类型。该计算器不擅自从逐题响应取平均。采用方法 ABCD 另行分析。

### 成熟度评分

`maturity-weighted` 要求 `rule_evidence`、`scale:{min,max}` 与 `factors[]`。每个因素含 `id/value/weight/evidence`。该计算规则必须由项目明确采用，不能仅因 G203 提到加权评估就擅自确定权重。

如需逐级达成比例，额外提供 `levels[]` 和每因素的 `achieved_levels[]`；计算器不从某个分值推断已经满足哪些级别的特征。ACMM 示例是六级九要素，其他模型可有不同结构。

### 风险

`risk-explicit-rule` 只计算显式采用的 `formula:"likelihood-times-impact"`，并要求 `rule_evidence`；`likelihood/impact` 分别包含 `value/scale/evidence`。这是一种可选项目规则，不是 TOGAF 统一公式。剩余风险需要控制有效性和重新评价证据，不能由控制条目存在自动推导。

### 环境变化

`environmental-delta` 要求 `boundary/method_evidence/rows`。每行含 `added/retired/unit/scope/period/evidence`，可保留 `reported_net`。计算值为新增减退役；如果与印刷或报告值不同，结果同时保留两值并报告差异。计算器不跨不同单位、Scope、生命周期范围求总量。抵消需独立记录。

## 非破坏迁移与验证

`migrate.py old.json --out new.json --report migration-report.json` 将 v1 基数映射到 v2 并迁移旧扩展名称，保留 ID、原始事实、证据、视图和交付物。输入、输出与报告必须是不同路径；输出与报告必须为新文件，拒绝覆盖已有文件。未识别字段按原路径保存在 `extension_data.legacy_unrecognized_fields` 并报告，不推断其业务含义。报告的 `pending_confirmations` 登记旧决策状态拆分和命名过渡状态等待确认项。

迁移不自动创建 profile、命名过渡状态、确认事实或批准记录。迁移前后的对象关系仍需按适用的视图规范与来源核对。`validate.py` 根据 schema_version 选择 v1 或 v2；结构通过与已编码规则通过都不能代替业务完整性及正式合规评审。
