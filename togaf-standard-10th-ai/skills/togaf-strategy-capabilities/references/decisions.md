# togaf-strategy-capabilities 判断规则

本文件是唯一需要人工撰写的部分：机器无法从注册表推出「什么情况选 A 不选 B」。

每条含判据（什么条件下适用）、反例（什么时候不该用）、影响（波及哪些制品或字段）。

## 判断 1：能力实例不是能力的子能力

- 判据：问「这个能力在某价值流阶段、某范围、某状态下具体怎么实现」时建**能力实例**（`capability_instance`），连 `instance_of` 到稳定能力；问「这个能力由哪些更小的能力组成」时才用 `decomposes`。
- 反例：把「订单履约能力」下的「某仓订单履约」挂成 `decomposes`，会让能力地图出现「每个基地一套能力」的假分解，层级爆炸且无法比较。
- 影响：`capability_instance_model` 的 `instance_of` 边；`capability-decomposition` 的层级数；G233 能力增量分析的基线范围。

## 判断 2：能力分类（战略／核心／支撑）按「改变谁」判定

- 判据：该能力失效会直接改变客户获得的价值 → 核心；改变企业长期定位与选择 → 战略；只支撑前者且可替换而不被客户察觉 → 支撑。
- 反例：把「财务核算」判为核心，理由是「很重要」；重要性不是分类标准，客户价值路径才是。
- 影响：`capability` 的 `category` 字段；`capability-classification` 的分区；`capability-organization-matrix` 的读法。

## 判断 3：能力层级止于「可指派责任人」

- 判据：L1–L3 每层，L3 必须能指派明确责任人（岗位或角色），且该责任人能对该能力产出负责。再往下不是能力层级，而是流程或组织。
- 反例：把能力拆到「每天核对台账」这一层，那是流程活动；继续拆会出现几十个只有一句话的「能力」。
- 影响：`capability` 的 `level` 与 `owner`；`capability-decomposition` 的深度；能力目录的可维护性。

## 判断 4：能力评分必须有量表与目标

- 判据：要出热力图，必须同时给出 `dimension`（评什么）、`scale`（几级、每级含义）、`score`（当前值）、`target`（目标值）。缺任一项只能出目录，不能出热力。
- 反例：只给「成熟度 3 分」而不说 3 分对应什么，读者无法判断 3 分是好是差，也无法比较两个能力。
- 影响：`capability-gap-heatmap` 的四字段；`unknown-scale-not-invented` 与 `attribute-not-expressed` 检查。

## 判断 5：平衡计分卡的四种视角不可增删

- 判据：使用 `balanced-scorecard` 时，四个视角固定为财务、客户、内部流程、学习与成长；每个视角的目标连到成果时用 `realizes`，成果与目标的类型必须分别正确。
- 反例：为贴合本项目自行增加「生态」第五视角，会让该图不再可与其他企业比较，也失去 BSC 的因果链假设。
- 影响：`balanced-scorecard-default` 示例的 `perspective` 取值；`realizes` 边的端点类型；该视图的可比性。
