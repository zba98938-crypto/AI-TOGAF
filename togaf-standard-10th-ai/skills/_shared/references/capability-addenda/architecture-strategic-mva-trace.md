# 战略—MVA—产品待办追溯

主责 `togaf-requirements`；制品族 `architecture-backlog`，视图规范 `architecture-strategic-mva-trace`，分析方法 `architecture-backlog-trace-review`。本实现扩展既有族，不把同一故事在不同待办中的出现计为新制品。

## 决策与输入

产品负责人、架构负责人和开发团队判断：本次MVA为何纳入这些故事、有哪些护栏及依赖、证据是否足以交付。必要输入为原始战略/需求、负责人明确排序、项目层次规则、MVA边界、ABB/SBB设计和验收证据。缺来源/断链拒绝通过；缺运行观察保持pending-evidence。

## 方法

1. 逐句提取战略意图、业务分段、故事和原始来源；项目声明epic/feature/story层次，不能假称标准要求
2. 依据产品负责人排序形成MVA必须项边界；保留未纳入项及排除理由
3. 把ABB护栏及计划SBB实现显式关联到故事；核对实现方向和前置依赖
4. 修改战略或边界时保留ID与历史，重算纳入集合与依赖；分别检查验收证据和可运营条件

## 语义与输出

五维语境分别保留；本例全为target状态，同时包含strategic/segment/capability全景层级以及conceptual/logical/physical抽象。批准candidate和实现not-started单独记录。core ABB/SBB与realizes不被扩展覆盖。项目采用的epic/feature/story细化不是所有TOGAF项目的强制结构。MVA不是MVP。

|关系|方向及含义|
|---|---|
|`g20f:refines`|本项目声明的战略意图到epic/feature/story逐层细化，不是流程先后|
|`g20f:constrains-story`|ABB对故事给出功能/非功能护栏|
|`g20f:allocated-to-sbb`|故事分配到候选SBB实现，不表示已实现|
|`g20f:included-in-mva`|显式必须项纳入命名MVA边界，非已验收或完整MVP|
|`g20f:story-depends-on`|依赖方故事指向前置故事，非优先级或完成顺序断言|
|`realizes`|SBB → ABB；本例为候选设计，不能视为已部署|

每个对象和关系都有稳定ID、属性及证据；两种布局均输出逐记录表和关系表。表示只依据已审查模型，不从行序推断依赖。分析结果输出战略路径、ABB/SBB关联、传递前置和MVA缺口；保存在JSON的事实同时可见于Markdown表。

## 完整案例与修改

原料（历史材料已清理）按BR-1至BR-4提取初始范围；初始模型（历史材料已清理）只纳入S-BOOK；BR-5把退款登记改为必须项并扩大同一MVA，保留历史。修改模型（历史材料已清理）纳入S-REFUND，BR-6仅使预约验收证据齐备，退款仍待验证，不应得出整体可运营。

执行及反例（历史材料已清理）检查改动、重复ID、断链、反向实现、MVA漏项、缺证据和依赖环。评审按每个story稳定ID追溯原料、护栏、实现、排序和验收；仅请求本制品时不用生成整个成果包。

## 调用与来源

`generate.py model.json --profile architecture-strategic-mva-trace --layout reference|adaptive --out output`；`analyze.py model.json --evaluate A-TRACE`。模型内analysis使用来源ID，不能给不存在的来源。

来源：G20F §4.5 L304–327；G20F §5.2.3 L529–547；G20F §5.3.2 L601–632。方法摘要与虚构原料随技能相对路径携带；原文用于审计，生成不依赖原工作区。该表是正文的项目操作化，未声称对应图的结构复刻；也未规定默认权重、合格线或MVA必定可运营。
