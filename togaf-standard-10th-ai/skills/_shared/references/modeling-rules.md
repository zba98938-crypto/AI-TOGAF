# 共用建模、分析与生成规则

本文件是技能集的项目操作约定；不是 TOGAF 强制元模型或 C220 的逐项正式定义。

## 先确定问题和五维语境

接收业务材料、现有制品、访谈记录或自然语言需求。先确定谁要做什么决策、需要哪些证据，再选择制品。五维分别记录：domains（business/data/application/technology，可多选）、landscape（strategic/segment/capability）、purpose（strategy/portfolio/project/solution-delivery）、abstraction（context/conceptual/logical/physical）、evolution（baseline/transition/target）。其间没有固定对应关系。v2 另外以 `approval_status` 记录批准决定、`implementation_status` 记录实现进度，分别引用批准与实现证据；批准不能代替实现验证。`decision_status` 的 candidate/approved/realized 保留为旧模型兼容字段，迁移不会据此猜测两个独立状态，详见 [模型 v2](model-v2.md)。

当范围、目标或关键基线缺失会改变结论时，向用户询问最关键的信息。能继续的部分先建草稿，`gaps` 记录缺口、影响和所需输入。未知不是否定：不把未记录关系当不存在，不用示例值填真实项目事实。量尺、阈值、工期和预算都要来源或假设身份。

## 共同模型

以 [模型 Schema](../schemas/model.schema.json) 为交换接口；运行生成器不要求复制源资料。`entities` 存对象，`relationships` 存有向语义关系，`views` 按制品族及规范引用实体和关系；`deliverables` 显式选择实际视图、分析与组装配置，人工 `sections` 文字是待核对背景。一个对象跨多个视图复用同一 ID。同名对象如确实不同，保持不同 ID 并补充边界。跨演进状态的不同版本使用不同 ID，加同一 `concept_id`，并在 `comparisons` 声明可比范围、缺口和过渡检查。

关系语义见 [关系注册表](../relationships.json)。需要新类型时先在任务模型 `extensions` 中给出定义及端点类型，使用 `namespace:name`，不能覆盖核心语义或静默使用无定义箭头。`attributes` 装领域属性而非把所有对象强塞同一结构。每个视图指定自己的五维 context；命名状态用 `state_id` 区分，即使两个状态同为 transition 也不能静默混用。读取整个模型并不意味着输出全部制品。

`evidence` 引用来源 ID；来源 `kind` 区分 user/official/local-translation/figure-interpretation/assumption/example。`certainty` 为 confirmed/assumed/uncertain；推测和例子即使结构完整也不能变成已确认事实。`is_example: true` 表示整个项目是虚构案例，所有输出继承标记。原图 JSON 的 parent 可能只有视觉布局含义；必须依据正文和图例才能映射成领域关系。

## 制品与交付物

按 [覆盖索引](coverage.md) 与[能力注册](../capabilities.json)加载本次需要的定义，不默认读取全部规范。目录校验对象边界与属性；矩阵遵守行列方向、代码表及空白含义；图按声明表示法解释箭头、区域和数量。普通框图应写“简化关系图”，不宣称严格 ArchiMate/UML/BPMN。ER 图只有在两端基数明确时使用确定数量符号。

交付物不等于把图堆到一起；按定义中的章节回答评审问题，并引用制品及模型版本。ABB 写所需职责、接口、质量和约束；SBB 写候选或实际实现以及 ABB 映射。架构存储库应有实际资产索引。`Requirements Impact Assessment` 同时作为制品与交付物存在，后者引用同一个分析，不重复创造事实。

需要实际组装的v2交付物按[动态组装规则](deliverable-assembly.md)配置`assembly`，从所选模型记录与计算结果形成正文。严格模式有缺口阻断，草稿模式显式显示，旧兼容模型`legacy-unassembled`不计当前组装验收。表格与图形均核对保存输出与coverage表示位置；模型JSON有值不足以证明已表达。复用结果前核对manifest版本和运行依赖指纹。

## 修改与评审

保留对象 ID、来源与版本历史，先判定变化是重命名、属性变化、关系变化还是替换。基线和目标在同一范围比较；缺口不局限于新增和删除，还包括质量、责任及连接变化。过渡状态需有业务连续性、数据一致性、依赖、控制、运营责任和回退检查。治理输出保持草案状态，自动生成不产生审批或实际发送沟通。

生成后运行语义校验，查看警告，再渲染和目视检查。脚本可验证引用、类型、基本基数和依赖；业务完整性、价值因果、风险接受和是否符合真实法规仍需证据与专业判断。校验通过不能标记为正式合规或已批准。

## 工具入口

从任意目录调用 `python <skills根>/_shared/scripts/generate.py <model.json> --artifact <id> --out <目标目录> --render`。可重复指定 `--artifact` 或 `--deliverable`；仅验收案例使用 `--all`。`validate.py` 检查模型和指定视图；`analyze.py` 提供有证据边界的影响遍历和同 concept_id 的状态比较。依赖安装、字体与离线说明见 [集合说明](../../README.md)。
