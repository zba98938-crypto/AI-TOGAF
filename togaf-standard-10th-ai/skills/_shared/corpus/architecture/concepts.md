# 架构概念词典

每条概念与关系引用已绑定PDF指纹、实体页码和原文短引的分析发现；定义为语料上下文释义，不冒充逐字规范定义。

严格区分组成、类型特化、分类、实现、架构约束、信息流和组织汇报；图形嵌套、位置、颜色及线条样式本身不足以新增人员汇报关系。

概念边界说明是防止误读的分析提示；本词典不是TOGAF官方规范元模型。

<a id="enterprise"></a>

## 企业 · Enterprise

标识：`enterprise`；类别：`scope`。

为共同目标而考虑的架构工作范围，可跨越法人及功能边界。

边界与误读提示：企业建模范围不自动等于法人边界或组织图最高框。

- [G184 PDF 20](../documents/G184.md#page-20)；书页 6，证据 `G184:A01`：not associated with an organization’s legal or functional boundaries
  章节：2.1. Enterprise；正文块：`G184:p0020:b009`、`G184:p0020:b010`、`G184:p0020:b011`、`G184:p0020:b012`、`G184:p0020:b013`、`G184:p0020:b014`。
- [G206 PDF 12](../documents/G206.md#page-12)；书页 2，证据 `G206:A02`：beyond the legal boundaries
  章节：2. What is an Organization Map?；正文块：`G206:p0012:b006`、`G206:p0012:b007`、`G206:p0012:b008`、`G206:p0012:b009`、`G206:p0012:b010`、`G206:p0012:b011`。

<a id="ea_capability"></a>

## 企业架构能力 · Enterprise Architecture Capability

标识：`ea_capability`；类别：`capability`。

开发、维护、演进架构，并利用架构治理变更的能力。

边界与误读提示：能力与执行该能力的部门分开建模。

- [G184 PDF 20](../documents/G184.md#page-20)；书页 6，证据 `G184:A02`：ability to use the architecture to govern change activity
  章节：2.3. Enterprise Architecture (EA) Capability；正文块：`G184:p0020:b020`、`G184:p0020:b021`。
- [G184 PDF 23](../documents/G184.md#page-23)；书页 9，证据 `G184:A03`：explicitly does not discuss an EA department
  章节：3.3. What is an EA Capability and EA?；正文块：`G184:p0023:b012`、`G184:p0023:b013`、`G184:p0023:b014`、`G184:p0023:b015`、`G184:p0023:b016`、`G184:p0023:b017`。

<a id="ea_service"></a>

## 企业架构服务 · Enterprise Architecture Service

标识：`ea_service`；类别：`service`。

在特定企业上下文中交付企业架构能力的机制。

边界与误读提示：服务名称不自动代表一个人员岗位或团队。

- [G217 PDF 31](../documents/G217.md#page-31)；书页 15，证据 `G217:A04`：minimal set of Enterprise Architecture services
  章节：4.1. Introduction；正文块：`G217:p0031:b014`、`G217:p0031:b015`、`G217:p0031:b016`、`G217:p0031:b017`、`G217:p0031:b018`。
- [G217 PDF 49](../documents/G217.md#page-49)；书页 33，证据 `G217:A05`：delivery mechanism
  章节：4.4. Enterprise Architecture Capabilities and Services；正文块：`G217:p0049:b012`、`G217:p0049:b013`、`G217:p0049:b014`、`G217:p0049:b015`、`G217:p0049:b016`、`G217:p0049:b017`、`G217:p0049:b018`、`G217:p0049:b019`。

<a id="digital_enterprise_context"></a>

## 数字企业上下文 · Digital Enterprise Context

标识：`digital_enterprise_context`；类别：`classification`。

按个人/创始人、团队、团队之团队和持久企业考虑规模、文化及运营上下文。

边界与误读提示：不是固定组织晋升阶梯，也不要求按顺序采用所有架构服务。

- [G217 PDF 17](../documents/G217.md#page-17)；书页 1，证据 `G217:A01`：scale, culture, and operation
  章节：1. Introduction；正文块：`G217:p0017:b008`、`G217:p0017:b009`、`G217:p0017:b010`、`G217:p0017:b011`、`G217:p0017:b012`。
- [G217 PDF 31](../documents/G217.md#page-31)；书页 15，证据 `G217:A03`：Individual/Founder
  章节：4.2. The DPBoK Standard；正文块：`G217:p0031:b021`。

<a id="architecture_model"></a>

## 架构模型 · Architecture Model

标识：`architecture_model`；类别：`model`。

以实体、构建块及关系表达有关架构问题的模型；其内容由目的和视点决定。

边界与误读提示：模型、视图、制品和交付物不是同义词。

- [G186 PDF 73](../documents/G186.md#page-73)；书页 59，证据 `G186:A07`：a constituent of the architecture model
  章节：5.5. Where are ABBs?；正文块：`G186:p0073:b005`、`G186:p0073:b006`、`G186:p0073:b007`、`G186:p0073:b008`。
- [G248 PDF 19](../documents/G248.md#page-19)；书页 7，证据 `G248:A03`：selected viewpoints
  章节：3. Choosing the Building Blocks for the Relevant Entities for Each Change Profile；正文块：`G248:p0019:b002`、`G248:p0019:b003`、`G248:p0019:b004`、`G248:p0019:b005`、`G248:p0019:b006`、`G248:p0019:b007`、`G248:p0019:b008`、`G248:p0019:b009`。

<a id="architecture_landscape"></a>

## 架构全景 · Architecture Landscape

标识：`architecture_landscape`；类别：`model`。

被不同目的、范围、状态及视图描述的企业架构内容集合。

边界与误读提示：此处为指南上下文概括，不声明一个唯一的存储结构。

- [G186 PDF 30](../documents/G186.md#page-30)；书页 16，证据 `G186:A01`：four broad purposes
  章节：3.2.2. Introduction to Purpose；正文块：`G186:p0030:b009`。
- [G186 PDF 35](../documents/G186.md#page-35)；书页 21，证据 `G186:A02`：a representation of the EA Landscape that addresses
  章节：3.3.1. Communicating with Stakeholders (Concern and View)；正文块：`G186:p0035:b026`、`G186:p0035:b027`、`G186:p0035:b028`。
- [G186 PDF 72](../documents/G186.md#page-72)；书页 58，证据 `G186:A06`：less detailed approved target that overlaps in terms of breadth
  章节：5.3. Operating in the Context of Superior Architecture；正文块：`G186:p0072:b013`、`G186:p0072:b014`、`G186:p0072:b015`、`G186:p0072:b016`。

<a id="architecture_domain"></a>

## 架构域 · Architecture Domain

标识：`architecture_domain`；类别：`classification`。

业务、数据、应用、技术四类架构内容维度，可在不同详细程度层级出现。

边界与误读提示：G20F中架构域与详细程度是不同维度；G249中四域也被称为有用的分段视点，须保留各指南语境。

- [G20F PDF 20](../documents/G20F.md#page-20)；书页 8，证据 `G20F:A02`：may exist at all levels of detail
  章节：4.1. Different Levels of Detail Enable Agility；正文块：`G20F:p0020:b010`、`G20F:p0020:b011`。
- [G21H PDF 46](../documents/G21H.md#page-46)；书页 32，证据 `G21H:A07`：Business Architecture defines
  章节：6.3. Architecture Domains；正文块：`G21H:p0046:b002`、`G21H:p0046:b003`。

<a id="business_architecture"></a>

## 业务架构 · Business Architecture

标识：`business_architecture`；类别：`domain`。

以能力、价值流、组织、信息等相互关联视角展开业务模型并描述业务。

边界与误读提示：不能仅用组织结构或流程图代替全部业务架构。

- [G18A PDF 17](../documents/G18A.md#page-17)；书页 7，证据 `G18A:A03`：business capabilities, value streams, organizational structure and information objects
  章节：4. The Relationship between Business Models and Business Architecture；正文块：`G18A:p0017:b017`、`G18A:p0017:b018`、`G18A:p0017:b019`、`G18A:p0017:b020`、`G18A:p0017:b021`、`G18A:p0017:b022`、`G18A:p0017:b023`。
- [G21H PDF 18](../documents/G21H.md#page-18)；书页 4，证据 `G21H:A01`：holistic, multi-dimensional business views
  章节：2.3. Business Architecture；正文块：`G21H:p0018:b014`、`G21H:p0018:b015`、`G21H:p0018:b016`。

<a id="data_architecture"></a>

## 数据架构 · Data Architecture

标识：`data_architecture`；类别：`domain`。

将业务信息语义转为可表示的数据结构，并考虑数据管理、来源及使用约束的架构域。

边界与误读提示：业务信息可能包括无法直接转成数据字段的内容。

- [G190 PDF 16](../documents/G190.md#page-16)；书页 6，证据 `G190:A03`：not the same
  章节：5. Distinguishing between Information Maps and Data Models；正文块：`G190:p0016:b002`、`G190:p0016:b003`、`G190:p0016:b004`、`G190:p0016:b005`、`G190:p0016:b006`、`G190:p0016:b007`、`G190:p0016:b008`。
- [G190 PDF 17](../documents/G190.md#page-17)；书页 7，证据 `G190:A05`：Phases C and D translate information
  章节：6. Using Information Maps with the TOGAF ADM；正文块：`G190:p0017:b011`、`G190:p0017:b012`、`G190:p0017:b013`。
- [G21I PDF 38](../documents/G21I.md#page-38)；书页 24，证据 `G21I:A05`：data managed by the business function
  章节：8. Phase C: Information Systems Architectures (Data and Application)；正文块：`G21I:p0038:b002`、`G21I:p0038:b003`、`G21I:p0038:b004`、`G21I:p0038:b005`、`G21I:p0038:b006`、`G21I:p0038:b007`。

<a id="application_architecture"></a>

## 应用架构 · Application Architecture

标识：`application_architecture`；类别：`domain`。

四个TOGAF架构域之一；在本语料中与业务、数据和技术共同支持架构设计。

边界与误读提示：该局部定义只确立域身份，不能代替标准中的完整应用内容元模型。

- [G20F PDF 20](../documents/G20F.md#page-20)；书页 8，证据 `G20F:A02`：may exist at all levels of detail
  章节：4.1. Different Levels of Detail Enable Agility；正文块：`G20F:p0020:b010`、`G20F:p0020:b011`。
- [G21H PDF 46](../documents/G21H.md#page-46)；书页 32，证据 `G21H:A07`：Business Architecture defines
  章节：6.3. Architecture Domains；正文块：`G21H:p0046:b002`、`G21H:p0046:b003`。

<a id="technology_architecture"></a>

## 技术架构 · Technology Architecture

标识：`technology_architecture`；类别：`domain`。

四个TOGAF架构域之一；可按战略、分段或能力粒度描述所需技术。

边界与误读提示：技术域不等于某一粒度层级，也不自动等于基础设施团队。

- [G20F PDF 20](../documents/G20F.md#page-20)；书页 8，证据 `G20F:A02`：may exist at all levels of detail
  章节：4.1. Different Levels of Detail Enable Agility；正文块：`G20F:p0020:b010`、`G20F:p0020:b011`。
- [G21H PDF 46](../documents/G21H.md#page-46)；书页 32，证据 `G21H:A07`：Business Architecture defines
  章节：6.3. Architecture Domains；正文块：`G21H:p0046:b002`、`G21H:p0046:b003`。

<a id="detail_level"></a>

## 架构详细程度 · Architecture Level of Detail

标识：`detail_level`；类别：`classification`。

按战略、分段和能力粒度组织架构的维度。

边界与误读提示：详细程度不等于业务/数据/应用/技术域或上下文/概念/逻辑/物理抽象层次。

- [G20F PDF 20](../documents/G20F.md#page-20)；书页 8，证据 `G20F:A01`：three levels of detail
  章节：4.1. Different Levels of Detail Enable Agility；正文块：`G20F:p0020:b003`、`G20F:p0020:b004`。

<a id="strategic_architecture"></a>

## 战略架构 · Strategic Architecture

标识：`strategic_architecture`；类别：`architecture-scope`。

在战略详细程度上描述架构，以支持整体方向和相应决策。

边界与误读提示：这里的架构粒度不证明某个角色的职级。

- [G20F PDF 20](../documents/G20F.md#page-20)；书页 8，证据 `G20F:A01`：three levels of detail
  章节：4.1. Different Levels of Detail Enable Agility；正文块：`G20F:p0020:b003`、`G20F:p0020:b004`。
- [G186 PDF 30](../documents/G186.md#page-30)；书页 16，证据 `G186:A01`：four broad purposes
  章节：3.2.2. Introduction to Purpose；正文块：`G186:p0030:b009`。

<a id="segment_architecture"></a>

## 分段架构 · Segment Architecture

标识：`segment_architecture`；类别：`architecture-scope`。

按连贯能力分组或相应变更范围组织的架构，可按结果需要裁剪ADM。

边界与误读提示：分段是一致管理范围，不必等同部门。G249将四域称为有用的分段视点；不能因此把G20F的详细程度和四域合并为一条单轴。

- [G20F PDF 20](../documents/G20F.md#page-20)；书页 8，证据 `G20F:A01`：three levels of detail
  章节：4.1. Different Levels of Detail Enable Agility；正文块：`G20F:p0020:b003`、`G20F:p0020:b004`。
- [G20F PDF 25](../documents/G20F.md#page-25)；书页 13，证据 `G20F:A05`：only the minimum needed to ensure outcomes are met
  章节：4.4.2. Segment Architecture；正文块：`G20F:p0025:b014`、`G20F:p0025:b015`、`G20F:p0025:b016`、`G20F:p0025:b017`、`G20F:p0025:b018`、`G20F:p0025:b019`。
- [G249 PDF 21](../documents/G249.md#page-21)；书页 11，证据 `G249:A05`：coherent grouping of capabilities
  章节：4.3. Segment Architect (Business and Technical)；正文块：`G249:p0021:b010`、`G249:p0021:b011`、`G249:p0021:b012`、`G249:p0021:b013`、`G249:p0021:b014`、`G249:p0021:b015`、`G249:p0021:b016`。

<a id="capability_architecture"></a>

## 能力架构 · Capability Architecture

标识：`capability_architecture`；类别：`architecture-scope`。

在能力详细程度上组织的架构表达，可含多个架构域。

边界与误读提示：能力架构不是能力目录条目本身。

- [G20F PDF 20](../documents/G20F.md#page-20)；书页 8，证据 `G20F:A01`：three levels of detail
  章节：4.1. Different Levels of Detail Enable Agility；正文块：`G20F:p0020:b003`、`G20F:p0020:b004`。
- [G20F PDF 20](../documents/G20F.md#page-20)；书页 8，证据 `G20F:A02`：may exist at all levels of detail
  章节：4.1. Different Levels of Detail Enable Agility；正文块：`G20F:p0020:b010`、`G20F:p0020:b011`。

<a id="superior_architecture"></a>

## 上位架构 · Superior Architecture

标识：`superior_architecture`；类别：`architecture-scope`。

范围交叠、详细程度更低且已经批准的目标架构，为后续详细架构提供指引和约束。

边界与误读提示：上位描述架构约束关系，不自动表示人员汇报层级。

- [G186 PDF 72](../documents/G186.md#page-72)；书页 58，证据 `G186:A06`：less detailed approved target that overlaps in terms of breadth
  章节：5.3. Operating in the Context of Superior Architecture；正文块：`G186:p0072:b013`、`G186:p0072:b014`、`G186:p0072:b015`、`G186:p0072:b016`。
- [G248 PDF 30](../documents/G248.md#page-30)；书页 18，证据 `G248:A06`：superior architecture
  章节：7. Outlining the Concept；正文块：`G248:p0030:b011`、`G248:p0030:b012`、`G248:p0030:b013`。

<a id="detailed_architecture"></a>

## 更详细的架构 · More Detailed Architecture

标识：`detailed_architecture`；类别：`architecture-scope`。

在交叠范围内受适用上位架构指引与约束的更细架构内容。

边界与误读提示：不是要求所有详细架构只对应一个上位架构。

- [G186 PDF 72](../documents/G186.md#page-72)；书页 58，证据 `G186:A06`：less detailed approved target that overlaps in terms of breadth
  章节：5.3. Operating in the Context of Superior Architecture；正文块：`G186:p0072:b013`、`G186:p0072:b014`、`G186:p0072:b015`、`G186:p0072:b016`。
- [G249 PDF 17](../documents/G249.md#page-17)；书页 7，证据 `G249:A04`：superior architectures
  章节：4. Architecture Roles；正文块：`G249:p0017:b006`、`G249:p0017:b007`、`G249:p0017:b008`、`G249:p0017:b009`、`G249:p0017:b010`、`G249:p0017:b011`。

<a id="target_architecture"></a>

## 目标架构 · Target Architecture

标识：`target_architecture`；类别：`architecture-state`。

经利益相关者决策的期望架构状态，为变更和合规提供参照。

边界与误读提示：目标是否批准及适用范围应显式记录，不能由图名代替治理状态。

- [G184 PDF 68](../documents/G184.md#page-68)；书页 54，证据 `G184:A05`：Only the set of stakeholders can approve an architecture and roadmap
  章节：6.5.1. Definition of Roles；正文块：`G184:p0068:b018`、`G184:p0068:b019`、`G184:p0068:b020`、`G184:p0068:b021`、`G184:p0068:b022`、`G184:p0068:b023`、`G184:p0068:b024`、`G184:p0068:b025`。
- [G186 PDF 139](../documents/G186.md#page-139)；书页 125，证据 `G186:A08`：Decision rights about the Target Architecture
  章节：15.2. Roles, Duties, and Decision Rights；正文块：`G186:p0139:b020`、`G186:p0139:b021`、`G186:p0139:b025`、`G186:p0139:b026`。
- [G21I PDF 48](../documents/G21I.md#page-48)；书页 34，证据 `G21I:A08`：conformance with the Target Architecture
  章节：12. Phase G: Implementation Governance；正文块：`G21I:p0048:b005`。

<a id="transition_architecture"></a>

## 过渡架构 · Transition Architecture

标识：`transition_architecture`；类别：`architecture-state`。

基线到目标间具有架构意义的时间状态，与能力增量、价值释放及迁移风险有关。

边界与误读提示：过渡架构是状态描述，不是任意项目里程碑。

- [G20F PDF 22](../documents/G20F.md#page-22)；书页 10，证据 `G20F:A03`：architecturally significant point in time
  章节：4.2. Transition Architectures；正文块：`G20F:p0022:b003`、`G20F:p0022:b004`、`G20F:p0022:b005`、`G20F:p0022:b006`、`G20F:p0022:b007`、`G20F:p0022:b008`。
- [G20F PDF 22](../documents/G20F.md#page-22)；书页 10，证据 `G20F:A04`：releases of business value
  章节：4.2. Transition Architectures；正文块：`G20F:p0022:b003`、`G20F:p0022:b004`、`G20F:p0022:b005`、`G20F:p0022:b006`、`G20F:p0022:b007`、`G20F:p0022:b008`。
- [G242 PDF 85](../documents/G242.md#page-85)；书页 67，证据 `G242:A06`：incremental approach supported by Transition Architecture
  章节：4. Process and Methodology: Using the TOGAF ADM to Build a Digital Sustainability Capability；正文块：`G242:p0085:b004`、`G242:p0085:b005`、`G242:p0085:b006`、`G242:p0085:b007`、`G242:p0085:b008`、`G242:p0085:b009`、`G242:p0085:b010`。

<a id="adm"></a>

## 架构开发方法 · Architecture Development Method

标识：`adm`；类别：`method`。

组织架构活动与信息流的方法；应根据目的、上下文和结果裁剪与迭代。

边界与误读提示：ADM环图不是唯一线性活动顺序，也不是每个冲刺必须完成全部阶段的承诺。

- [G186 PDF 72](../documents/G186.md#page-72)；书页 58，证据 `G186:A05`：not an activity diagram
  章节：5.2.8. Iteration Conclusion；正文块：`G186:p0072:b002`、`G186:p0072:b003`、`G186:p0072:b004`、`G186:p0072:b005`、`G186:p0072:b006`。
- [G20F PDF 25](../documents/G20F.md#page-25)；书页 13，证据 `G20F:A05`：only the minimum needed to ensure outcomes are met
  章节：4.4.2. Segment Architecture；正文块：`G20F:p0025:b014`、`G20F:p0025:b015`、`G20F:p0025:b016`、`G20F:p0025:b017`、`G20F:p0025:b018`、`G20F:p0025:b019`。
- [G210 PDF 30](../documents/G210.md#page-30)；书页 18，证据 `G210:A04`：some or all TOGAF ADM phases
  章节：4. TOGAF Phases and Sprints；正文块：`G210:p0030:b002`、`G210:p0030:b003`。

<a id="architecture_project"></a>

## 架构项目 · Architecture Project

标识：`architecture_project`；类别：`method`。

G188将其限定为形成待实施架构的ADM A–F及需求管理工作。

边界与误读提示：不把G188的特定定义扩展为所有架构相关项目；该定义排除预备、G和H。

- [G188 PDF 19](../documents/G188.md#page-19)；书页 5，证据 `G188:A01`：Phases A to F and Requirements Management
  章节：2.1. Architecture Project Definition；正文块：`G188:p0019:b007`、`G188:p0019:b008`、`G188:p0019:b009`、`G188:p0019:b010`。
- [G188 PDF 19](../documents/G188.md#page-19)；书页 5，证据 `G188:A02`：does not include the Preliminary Phase, Phase G, or Phase H
  章节：2.1. Architecture Project Definition；正文块：`G188:p0019:b011`。

<a id="minimum_viable_architecture"></a>

## 最小可行架构 · Minimum Viable Architecture

标识：`minimum_viable_architecture`；类别：`architecture-product`。

在架构冲刺中形成、可为当前决策和利益相关者提供价值的架构结果。

边界与误读提示：最小不表示固定文档页数，也不表示完全省略治理或某个域。

- [G210 PDF 23](../documents/G210.md#page-23)；书页 11，证据 `G210:A02`：Each sprint will deliver an MVA
  章节：3.3.5. Enterprise Architecture Development Agility；正文块：`G210:p0023:b016`、`G210:p0023:b017`。
- [G210 PDF 30](../documents/G210.md#page-30)；书页 18，证据 `G210:A04`：some or all TOGAF ADM phases
  章节：4. TOGAF Phases and Sprints；正文块：`G210:p0030:b002`、`G210:p0030:b003`。
- [G210 PDF 37](../documents/G210.md#page-37)；书页 25，证据 `G210:A06`：something valuable for the stakeholders
  章节：5.3. Length of Sprints；正文块：`G210:p0037:b009`、`G210:p0037:b010`、`G210:p0037:b011`。

<a id="stakeholder"></a>

## 利益相关者 · Stakeholder

标识：`stakeholder`；类别：`governance`。

正式定义为对系统有利益的个人、团队、组织或其类别。G186的实践治理语境进一步聚焦对目标与实施适用性有批准权的参与者。

边界与误读提示：不能把G186的实务聚焦当作所有语境的通用定义；目标的enforcement指要求遵守架构，与决策者的变更execution rights不同。具体授权须另行明确。

- [G186 PDF 34](../documents/G186.md#page-34)；书页 20，证据 `G186:A09`：an individual, team, organization, or classes thereof, having an interest in a system
  章节：3.3. How to Use an Enterprise Architecture?；正文块：`G186:p0034:b023`、`G186:p0034:b024`、`G186:p0034:b025`。
- [G186 PDF 35](../documents/G186.md#page-35)；书页 21，证据 `G186:A02`：a representation of the EA Landscape that addresses
  章节：3.3.1. Communicating with Stakeholders (Concern and View)；正文块：`G186:p0035:b026`、`G186:p0035:b027`、`G186:p0035:b028`。
- [G186 PDF 139](../documents/G186.md#page-139)；书页 125，证据 `G186:A08`：Decision rights about the Target Architecture
  章节：15.2. Roles, Duties, and Decision Rights；正文块：`G186:p0139:b020`、`G186:p0139:b021`、`G186:p0139:b025`、`G186:p0139:b026`。
- [G184 PDF 68](../documents/G184.md#page-68)；书页 54，证据 `G184:A05`：Only the set of stakeholders can approve an architecture and roadmap
  章节：6.5.1. Definition of Roles；正文块：`G184:p0068:b018`、`G184:p0068:b019`、`G184:p0068:b020`、`G184:p0068:b021`、`G184:p0068:b022`、`G184:p0068:b023`、`G184:p0068:b024`、`G184:p0068:b025`。

<a id="concern"></a>

## 利益相关者关注点 · Stakeholder Concern

标识：`concern`；类别：`governance`。

架构视图需要回答的相关方问题、利益或关切，驱动视点和信息选择。

边界与误读提示：关注点与已经批准的可检验需求不是同义词。

- [G186 PDF 35](../documents/G186.md#page-35)；书页 21，证据 `G186:A02`：a representation of the EA Landscape that addresses
  章节：3.3.1. Communicating with Stakeholders (Concern and View)；正文块：`G186:p0035:b026`、`G186:p0035:b027`、`G186:p0035:b028`。
- [G184 PDF 73](../documents/G184.md#page-73)；书页 59，证据 `G184:A06`：viewpoint library
  正文块：`G184:p0073:b011`、`G184:p0073:b012`、`G184:p0073:b013`、`G184:p0073:b014`、`G184:p0073:b015`、`G184:p0073:b016`、`G184:p0073:b017`、`G184:p0073:b018`、`G184:p0073:b019`、`G184:p0073:b021`、`G184:p0073:b022`、`G184:p0073:b023`、`G184:p0073:b024`；短引在多个章节出现，未自动归属：G184:s0068、G184:s0069。
- [G198 PDF 20](../documents/G198.md#page-20)；书页 12，证据 `G198:A03`：completeness (fitness-for-purpose)
  章节：6.1. Role Description；正文块：`G198:p0020:b014`、`G198:p0020:b015`、`G198:p0020:b016`、`G198:p0020:b017`、`G198:p0020:b018`。

<a id="viewpoint"></a>

## 架构视点 · Architecture Viewpoint

标识：`viewpoint`；类别：`representation`。

为回答稳定关注点而选用的视图构造约定，决定需要的架构信息。

边界与误读提示：视点与按它形成的具体视图分开记录。

- [G184 PDF 73](../documents/G184.md#page-73)；书页 59，证据 `G184:A06`：viewpoint library
  正文块：`G184:p0073:b011`、`G184:p0073:b012`、`G184:p0073:b013`、`G184:p0073:b014`、`G184:p0073:b015`、`G184:p0073:b016`、`G184:p0073:b017`、`G184:p0073:b018`、`G184:p0073:b019`、`G184:p0073:b021`、`G184:p0073:b022`、`G184:p0073:b023`、`G184:p0073:b024`；短引在多个章节出现，未自动归属：G184:s0068、G184:s0069。
- [G248 PDF 19](../documents/G248.md#page-19)；书页 7，证据 `G248:A03`：selected viewpoints
  章节：3. Choosing the Building Blocks for the Relevant Entities for Each Change Profile；正文块：`G248:p0019:b002`、`G248:p0019:b003`、`G248:p0019:b004`、`G248:p0019:b005`、`G248:p0019:b006`、`G248:p0019:b007`、`G248:p0019:b008`、`G248:p0019:b009`。

<a id="view"></a>

## 架构视图 · Architecture View

标识：`view`；类别：`representation`。

面向特定利益相关者关注点的架构全景表示。

边界与误读提示：不同视图需相互联结并调和冲突，不能视为互不相关的图纸。

- [G186 PDF 35](../documents/G186.md#page-35)；书页 21，证据 `G186:A02`：a representation of the EA Landscape that addresses
  章节：3.3.1. Communicating with Stakeholders (Concern and View)；正文块：`G186:p0035:b026`、`G186:p0035:b027`、`G186:p0035:b028`。
- [G198 PDF 20](../documents/G198.md#page-20)；书页 12，证据 `G198:A04`：connecting all the various views
  章节：6.1. Role Description；正文块：`G198:p0020:b014`、`G198:p0020:b015`、`G198:p0020:b016`、`G198:p0020:b017`、`G198:p0020:b018`。

<a id="requirement"></a>

## 架构需求 · Architecture Requirement

标识：`requirement`；类别：`constraint`。

表达架构必须服务的需要，业务场景可用于导出需求，设计规范应追溯到需求。

边界与误读提示：不是把每条源文建议都自动变成项目强制需求。

- [G176 PDF 30](../documents/G176.md#page-30)；书页 18，证据 `G176:A03`：any ADM phase
  章节：6. Business Scenarios and the TOGAF ADM；正文块：`G176:p0030:b009`、`G176:p0030:b010`、`G176:p0030:b011`。
- [G186 PDF 37](../documents/G186.md#page-37)；书页 23，证据 `G186:A04`：always to link a specification to a requirement
  章节：3.3.2. Communicating with Implementers (Gap, Specification, and Control)；正文块：`G186:p0037:b031`、`G186:p0037:b032`、`G186:p0037:b033`、`G186:p0037:b034`、`G186:p0037:b035`、`G186:p0037:b036`、`G186:p0037:b037`、`G186:p0037:b038`。

<a id="architecture_specification"></a>

## 架构规范 · Architecture Specification

标识：`architecture_specification`；类别：`constraint`。

交给实施者、说明架构实现期望且可追溯到需求的规格。

边界与误读提示：规范与需求分别保留；同一需求的实现方案需要取舍。

- [G186 PDF 37](../documents/G186.md#page-37)；书页 23，证据 `G186:A03`：context, gap, architecture specification, and control
  章节：3.3.2. Communicating with Implementers (Gap, Specification, and Control)；正文块：`G186:p0037:b002`、`G186:p0037:b003`、`G186:p0037:b004`、`G186:p0037:b005`、`G186:p0037:b006`。
- [G186 PDF 37](../documents/G186.md#page-37)；书页 23，证据 `G186:A04`：always to link a specification to a requirement
  章节：3.3.2. Communicating with Implementers (Gap, Specification, and Control)；正文块：`G186:p0037:b031`、`G186:p0037:b032`、`G186:p0037:b033`、`G186:p0037:b034`、`G186:p0037:b035`、`G186:p0037:b036`、`G186:p0037:b037`、`G186:p0037:b038`。

<a id="implementation_control"></a>

## 架构实施控制 · Architecture Implementation Control

标识：`implementation_control`；类别：`governance`。

连同上下文、差距和规范交给实施者的治理信息，用以管理符合性及变更。

边界与误读提示：控制不等于控制目标，也不默认是技术安全控制。

- [G186 PDF 37](../documents/G186.md#page-37)；书页 23，证据 `G186:A03`：context, gap, architecture specification, and control
  章节：3.3.2. Communicating with Implementers (Gap, Specification, and Control)；正文块：`G186:p0037:b002`、`G186:p0037:b003`、`G186:p0037:b004`、`G186:p0037:b005`、`G186:p0037:b006`。
- [G21I PDF 48](../documents/G21I.md#page-48)；书页 34，证据 `G21I:A08`：conformance with the Target Architecture
  章节：12. Phase G: Implementation Governance；正文块：`G21I:p0048:b005`。

<a id="architecture_board"></a>

## 架构治理委员会 · EA Governance Board

标识：`architecture_board`；类别：`role`。

在G184治理框架中负责架构过程、完整性与可信度建议的治理角色。

边界与误读提示：不得仅因委员会名称而授予它所有目标架构批准权。

- [G184 PDF 61](../documents/G184.md#page-61)；书页 47，证据 `G184:A04`：An EA governance board owns process
  章节：6.2. Essential Governance；正文块：`G184:p0061:b003`、`G184:p0061:b004`、`G184:p0061:b005`、`G184:p0061:b006`、`G184:p0061:b007`、`G184:p0061:b008`、`G184:p0061:b009`。

<a id="architect"></a>

## 架构师 · Architect

标识：`architect`；类别：`role`。

负责架构适用性与完整性、协调视图和冲突关注点的角色。

边界与误读提示：角色不是固定职位，也不等同任何单一技术专家。

- [G198 PDF 20](../documents/G198.md#page-20)；书页 12，证据 `G198:A03`：completeness (fitness-for-purpose)
  章节：6.1. Role Description；正文块：`G198:p0020:b014`、`G198:p0020:b015`、`G198:p0020:b016`、`G198:p0020:b017`、`G198:p0020:b018`。
- [G198 PDF 20](../documents/G198.md#page-20)；书页 12，证据 `G198:A04`：connecting all the various views
  章节：6.1. Role Description；正文块：`G198:p0020:b014`、`G198:p0020:b015`、`G198:p0020:b016`、`G198:p0020:b017`、`G198:p0020:b018`。

<a id="implementer"></a>

## 实施者 · Implementer

标识：`implementer`；类别：`role`。

接收架构上下文、差距、规范和控制并实施变更的相关角色。

边界与误读提示：实施责任不自动包含目标架构或豁免的批准权。

- [G186 PDF 37](../documents/G186.md#page-37)；书页 23，证据 `G186:A03`：context, gap, architecture specification, and control
  章节：3.3.2. Communicating with Implementers (Gap, Specification, and Control)；正文块：`G186:p0037:b002`、`G186:p0037:b003`、`G186:p0037:b004`、`G186:p0037:b005`、`G186:p0037:b006`。
- [G188 PDF 72](../documents/G188.md#page-72)；书页 58，证据 `G188:A06`：body responsible for implementation
  章节：3.6.1. Products Handover；正文块：`G188:p0072:b026`、`G188:p0072:b027`、`G188:p0072:b028`。

<a id="business_model"></a>

## 业务模型 · Business Model

标识：`business_model`；类别：`business`。

说明组织如何创造、交付和获取价值的概念性模型。

边界与误读提示：摘要业务模型通常不足以单独支撑风险评估和详细实施。

- [G18A PDF 11](../documents/G18A.md#page-11)；书页 1，证据 `G18A:A01`：creates, delivers, and captures value
  章节：1. Introduction；正文块：`G18A:p0011:b002`、`G18A:p0011:b003`、`G18A:p0011:b004`、`G18A:p0011:b005`、`G18A:p0011:b006`、`G18A:p0011:b007`、`G18A:p0011:b008`。
- [G18A PDF 17](../documents/G18A.md#page-17)；书页 7，证据 `G18A:A02`：does not normally contain sufficient information
  章节：4. The Relationship between Business Models and Business Architecture；正文块：`G18A:p0017:b013`、`G18A:p0017:b014`、`G18A:p0017:b015`、`G18A:p0017:b016`。

<a id="operating_model"></a>

## 运营模型 · Operating Model

标识：`operating_model`；类别：`business`。

把业务模型转成关联能力、过程和运行环境，并据战略分配资源的模型。

边界与误读提示：运营模型与业务模型分别表达运行安排与价值逻辑。

- [G21H PDF 34](../documents/G21H.md#page-34)；书页 20，证据 `G21H:A05`：translates the business model
  章节：4.4.2. Operating Model；正文块：`G21H:p0034:b002`、`G21H:p0034:b003`、`G21H:p0034:b004`、`G21H:p0034:b005`、`G21H:p0034:b006`、`G21H:p0034:b007`。

<a id="business_capability"></a>

## 业务能力 · Business Capability

标识：`business_capability`；类别：`business`。

业务能够做什么的表达，相对独立于当前组织、过程和系统。

边界与误读提示：能力不直接规定怎样实现、由谁实现；不是价值流阶段。

- [G211 PDF 12](../documents/G211.md#page-12)；书页 2，证据 `G211:A01`：what a business does
  章节：2. What is a Business Capability?；正文块：`G211:p0012:b006`、`G211:p0012:b007`。
- [G211 PDF 15](../documents/G211.md#page-15)；书页 5，证据 `G211:A03`：independent of the current organizational structure
  章节：3. Business Capability Mapping；正文块：`G211:p0015:b007`、`G211:p0015:b008`、`G211:p0015:b009`、`G211:p0015:b010`、`G211:p0015:b011`。

<a id="capability_instance"></a>

## 业务能力实例 · Business Capability Instance

标识：`capability_instance`；类别：`business`。

同一能力在组织或价值流上下文中的具体使用，用于分析资源、绩效和投资。

边界与误读提示：实例增加不必重复建立能力类型条目。

- [G233 PDF 32](../documents/G233.md#page-32)；书页 18，证据 `G233:A02`：business capability instance
  章节：6. Business Capabilities；正文块：`G233:p0032:b006`、`G233:p0032:b007`、`G233:p0032:b008`、`G233:p0032:b009`、`G233:p0032:b010`、`G233:p0032:b011`。
- [G233 PDF 36](../documents/G233.md#page-36)；书页 22，证据 `G233:A04`：otherwise conflict or create duplicates
  章节：6.4. Business Capability Instances；正文块：`G233:p0036:b002`、`G233:p0036:b003`、`G233:p0036:b004`。
- [G233 PDF 36](../documents/G233.md#page-36)；书页 22，证据 `G233:A05`：actors, stakeholders, resources, applications, or processes
  章节：6.4. Business Capability Instances；正文块：`G233:p0036:b005`、`G233:p0036:b006`、`G233:p0036:b007`、`G233:p0036:b008`。

<a id="capability_group"></a>

## 能力组或层 · Capability Group or Stratum

标识：`capability_group`；类别：`classification`。

为理解和管理而形成的能力分类、层或连贯分组。

边界与误读提示：分类分层不是父子能力分解，分组也不自动表示直属组织。

- [G211 PDF 20](../documents/G211.md#page-20)；书页 10，证据 `G211:A05`：classifying, grouping, and aligning
  章节：3.2.1. Business Capability Stratification；正文块：`G211:p0020:b007`、`G211:p0020:b008`、`G211:p0020:b009`、`G211:p0020:b010`。
- [G249 PDF 21](../documents/G249.md#page-21)；书页 11，证据 `G249:A05`：coherent grouping of capabilities
  章节：4.3. Segment Architect (Business and Technical)；正文块：`G249:p0021:b010`、`G249:p0021:b011`、`G249:p0021:b012`、`G249:p0021:b013`、`G249:p0021:b014`、`G249:p0021:b015`、`G249:p0021:b016`。

<a id="capability_decomposition"></a>

## 能力分解 · Capability Decomposition

标识：`capability_decomposition`；类别：`method`。

把能力逐级拆为更细能力，层数由沟通和决策需要决定。

边界与误读提示：不能把分类层、热力图颜色或组织汇报线当作分解证据。

- [G211 PDF 21](../documents/G211.md#page-21)；书页 11，证据 `G211:A06`：decomposing each top-level
  章节：3.2.2. Leveling；正文块：`G211:p0021:b002`、`G211:p0021:b003`、`G211:p0021:b004`、`G211:p0021:b005`。

<a id="capability_increment"></a>

## 能力增量 · Capability Increment

标识：`capability_increment`；类别：`planning`。

以依赖顺序组合到过渡台阶中的能力变化，台阶需维持价值流可运行。

边界与误读提示：增量需结合端到端价值，不是互不相干功能清单。

- [G233 PDF 43](../documents/G233.md#page-43)；书页 29，证据 `G233:A07`：preserve a functional value stream
  章节：7.2. Planning Business Capability Instance Increments；正文块：`G233:p0043:b003`、`G233:p0043:b004`、`G233:p0043:b005`、`G233:p0043:b006`、`G233:p0043:b007`、`G233:p0043:b008`。
- [G20F PDF 22](../documents/G20F.md#page-22)；书页 10，证据 `G20F:A03`：architecturally significant point in time
  章节：4.2. Transition Architectures；正文块：`G20F:p0022:b003`、`G20F:p0022:b004`、`G20F:p0022:b005`、`G20F:p0022:b006`、`G20F:p0022:b007`、`G20F:p0022:b008`。

<a id="value_stream"></a>

## 价值流 · Value Stream

标识：`value_stream`；类别：`business`。

从触发利益相关者到预期价值的外向内价值表达，可由顺序或并行阶段构成。

边界与误读提示：不是能力分解，也不等同内部细粒度业务过程。

- [G178 PDF 13](../documents/G178.md#page-13)；书页 3，证据 `G178:A02`：outside-in perspective
  章节：1.4. Relationship of Value Streams to Other Business Architecture Concepts；正文块：`G178:p0013:b010`、`G178:p0013:b011`、`G178:p0013:b012`、`G178:p0013:b013`、`G178:p0013:b014`、`G178:p0013:b015`、`G178:p0013:b016`、`G178:p0013:b017`、`G178:p0013:b018`、`G178:p0013:b019`。
- [G178 PDF 15](../documents/G178.md#page-15)；书页 5，证据 `G178:A03`：four standard elements
  章节：2.1. Describing a Value Stream；正文块：`G178:p0015:b008`、`G178:p0015:b009`。
- [G178 PDF 16](../documents/G178.md#page-16)；书页 6，证据 `G178:A04`：sequential and/or parallel actions
  章节：2.2. Decomposing a Value Stream；正文块：`G178:p0016:b002`、`G178:p0016:b003`、`G178:p0016:b004`。

<a id="value_stream_stage"></a>

## 价值流阶段 · Value Stream Stage

标识：`value_stream_stage`；类别：`business`。

价值流中累积价值的阶段，具有进入/退出条件、参与者及价值项。

边界与误读提示：阶段属于价值流，能力通过使能关系关联阶段。

- [G178 PDF 16](../documents/G178.md#page-16)；书页 6，证据 `G178:A04`：sequential and/or parallel actions
  章节：2.2. Decomposing a Value Stream；正文块：`G178:p0016:b002`、`G178:p0016:b003`、`G178:p0016:b004`。
- [G178 PDF 16](../documents/G178.md#page-16)；书页 6，证据 `G178:A05`：Entrance Criteria
  章节：2.2. Decomposing a Value Stream；正文块：`G178:p0016:b011`、`G178:p0016:b012`。

<a id="value_item"></a>

## 价值项 · Value Item

标识：`value_item`；类别：`business`。

价值流阶段达到退出条件时为相关方贡献的价值表达。

边界与误读提示：价值不必只表示金额；数值单位及评价口径必须另行明确。

- [G178 PDF 16](../documents/G178.md#page-16)；书页 6，证据 `G178:A05`：Entrance Criteria
  章节：2.2. Decomposing a Value Stream；正文块：`G178:p0016:b011`、`G178:p0016:b012`。

<a id="business_process"></a>

## 业务过程 · Business Process

标识：`business_process`；类别：`business`。

业务操作的实现安排，可映射到价值流阶段；一个阶段可对应一个或多个过程。

边界与误读提示：过程回答实现方式，不应直接当作稳定能力目录。

- [G178 PDF 13](../documents/G178.md#page-13)；书页 3，证据 `G178:A01`：one or more business processes
  章节：1.4. Relationship of Value Streams to Other Business Architecture Concepts；正文块：`G178:p0013:b002`、`G178:p0013:b003`、`G178:p0013:b004`、`G178:p0013:b005`、`G178:p0013:b006`、`G178:p0013:b007`、`G178:p0013:b008`、`G178:p0013:b009`。
- [G178 PDF 13](../documents/G178.md#page-13)；书页 3，证据 `G178:A02`：outside-in perspective
  章节：1.4. Relationship of Value Streams to Other Business Architecture Concepts；正文块：`G178:p0013:b010`、`G178:p0013:b011`、`G178:p0013:b012`、`G178:p0013:b013`、`G178:p0013:b014`、`G178:p0013:b015`、`G178:p0013:b016`、`G178:p0013:b017`、`G178:p0013:b018`、`G178:p0013:b019`。
- [G211 PDF 13](../documents/G211.md#page-13)；书页 3，证据 `G211:A02`：roles, processes, information, and tools
  章节：2.2. Elements to Implement Business Capabilities；正文块：`G211:p0013:b014`、`G211:p0013:b015`、`G211:p0013:b016`、`G211:p0013:b017`、`G211:p0013:b018`。

<a id="organization_unit"></a>

## 组织单元 · Organization Unit

标识：`organization_unit`；类别：`organization`。

参与能力交付与正式或非正式工作关系的内部或外部组织单元。

边界与误读提示：一个单元可以关联多种能力，一种能力也可以跨单元交付。

- [G206 PDF 12](../documents/G206.md#page-12)；书页 2，证据 `G206:A01`：informal as well as formal
  章节：2. What is an Organization Map?；正文块：`G206:p0012:b005`。
- [G206 PDF 19](../documents/G206.md#page-19)；书页 9，证据 `G206:A05`：with a many-to-many mapping
  章节：5. The Relationship to Business Capabilities, Value Streams, and Information Maps；正文块：`G206:p0019:b002`、`G206:p0019:b003`、`G206:p0019:b004`、`G206:p0019:b005`、`G206:p0019:b006`、`G206:p0019:b007`、`G206:p0019:b008`。

<a id="organization_map"></a>

## 组织地图 · Organization Map

标识：`organization_map`；类别：`representation`。

展示内部单元、伙伴、相关方及其工作关系和信息/价值流的地图。

边界与误读提示：组织地图不等同法定组织树或正式汇报树。

- [G206 PDF 12](../documents/G206.md#page-12)；书页 2，证据 `G206:A01`：informal as well as formal
  章节：2. What is an Organization Map?；正文块：`G206:p0012:b005`。
- [G206 PDF 14](../documents/G206.md#page-14)；书页 4，证据 `G206:A03`：horizontal, peer-to-peer, or many-to-many relationships
  章节：3. Differentiating between Organization Maps and Organization Charts；正文块：`G206:p0014:b006`、`G206:p0014:b007`、`G206:p0014:b008`、`G206:p0014:b009`、`G206:p0014:b010`。
- [G206 PDF 19](../documents/G206.md#page-19)；书页 9，证据 `G206:A06`：information types can be shown flowing
  章节：5. The Relationship to Business Capabilities, Value Streams, and Information Maps；正文块：`G206:p0019:b009`、`G206:p0019:b010`、`G206:p0019:b011`、`G206:p0019:b012`、`G206:p0019:b013`、`G206:p0019:b014`、`G206:p0019:b015`、`G206:p0019:b016`、`G206:p0019:b017`。

<a id="information_map"></a>

## 信息地图 · Information Map

标识：`information_map`；类别：`representation`。

由业务信息概念及其关系构成，并与业务能力、价值流和组织关联的地图。

边界与误读提示：不是数据模型，包含的主观信息不一定能直接表示为数据字段。

- [G190 PDF 12](../documents/G190.md#page-12)；书页 2，证据 `G190:A01`：collection of information concepts and their relationships
  章节：2. What is an Information Map?；正文块：`G190:p0012:b002`、`G190:p0012:b003`、`G190:p0012:b004`、`G190:p0012:b005`。
- [G190 PDF 21](../documents/G190.md#page-21)；书页 11，证据 `G190:A06`：joined with business capabilities, value streams, and organization maps
  章节：8. Conclusion；正文块：`G190:p0021:b002`、`G190:p0021:b003`、`G190:p0021:b004`、`G190:p0021:b005`、`G190:p0021:b006`、`G190:p0021:b007`、`G190:p0021:b008`。

<a id="information_concept"></a>

## 信息概念 · Information Concept

标识：`information_concept`；类别：`information`。

业务需要知道、存储或操作、使用业务词汇定义的信息。

边界与误读提示：应保留主观、经验性及非结构化信息，不默认全部是数据库实体。

- [G190 PDF 12](../documents/G190.md#page-12)；书页 2，证据 `G190:A02`：business’ vocabulary
  章节：2. What is an Information Map?；正文块：`G190:p0012:b002`、`G190:p0012:b003`、`G190:p0012:b004`、`G190:p0012:b005`。
- [G190 PDF 16](../documents/G190.md#page-16)；书页 6，证据 `G190:A04`：not in a form reducible to a data field
  章节：5. Distinguishing between Information Maps and Data Models；正文块：`G190:p0016:b009`、`G190:p0016:b010`、`G190:p0016:b011`、`G190:p0016:b012`、`G190:p0016:b013`、`G190:p0016:b014`、`G190:p0016:b015`、`G190:p0016:b016`、`G190:p0016:b017`、`G190:p0016:b018`。

<a id="data_model"></a>

## 数据模型 · Data Model

标识：`data_model`；类别：`information`。

在可表示的范围内，将业务信息转化为数据架构结构的模型。

边界与误读提示：与业务信息地图保留语义追溯，不宣称完全等价。

- [G190 PDF 16](../documents/G190.md#page-16)；书页 6，证据 `G190:A03`：not the same
  章节：5. Distinguishing between Information Maps and Data Models；正文块：`G190:p0016:b002`、`G190:p0016:b003`、`G190:p0016:b004`、`G190:p0016:b005`、`G190:p0016:b006`、`G190:p0016:b007`、`G190:p0016:b008`。
- [G190 PDF 17](../documents/G190.md#page-17)；书页 7，证据 `G190:A05`：Phases C and D translate information
  章节：6. Using Information Maps with the TOGAF ADM；正文块：`G190:p0017:b011`、`G190:p0017:b012`、`G190:p0017:b013`。

<a id="abb"></a>

## 架构构建块 · Architecture Building Block

标识：`abb`；类别：`building-block`。

架构逻辑模型中的构件，描述模型的一部分。

边界与误读提示：ABB不是任意文档，也不限定为可购买产品。

- [G186 PDF 73](../documents/G186.md#page-73)；书页 59，证据 `G186:A07`：a constituent of the architecture model
  章节：5.5. Where are ABBs?；正文块：`G186:p0073:b005`、`G186:p0073:b006`、`G186:p0073:b007`、`G186:p0073:b008`。
- [G248 PDF 19](../documents/G248.md#page-19)；书页 7，证据 `G248:A02`：physical/operational implementations
  章节：3. Choosing the Building Blocks for the Relevant Entities for Each Change Profile；正文块：`G248:p0019:b002`、`G248:p0019:b003`、`G248:p0019:b004`、`G248:p0019:b005`、`G248:p0019:b006`、`G248:p0019:b007`、`G248:p0019:b008`、`G248:p0019:b009`。

<a id="sbb"></a>

## 解决方案构建块 · Solution Building Block

标识：`sbb`；类别：`building-block`。

对架构构件的物理或运营实现表达。

边界与误读提示：不从ABB/SBB关联推导唯一实现或固定一对一。

- [G248 PDF 19](../documents/G248.md#page-19)；书页 7，证据 `G248:A02`：physical/operational implementations
  章节：3. Choosing the Building Blocks for the Relevant Entities for Each Change Profile；正文块：`G248:p0019:b002`、`G248:p0019:b003`、`G248:p0019:b004`、`G248:p0019:b005`、`G248:p0019:b006`、`G248:p0019:b007`、`G248:p0019:b008`、`G248:p0019:b009`。

<a id="artifact"></a>

## 架构制品 · Architecture Artifact

标识：`artifact`；类别：`representation`。

记录架构实体、构建块及关系的表达，组织进交付物以支持沟通与变更。

边界与误读提示：记录构建块的制品不是构建块本身。

- [G248 PDF 24](../documents/G248.md#page-24)；书页 12，证据 `G248:A04`：documented by various artifacts and organized into specific deliverables
  章节：3.6. What About Artifacts and Deliverables?；正文块：`G248:p0024:b010`、`G248:p0024:b011`、`G248:p0024:b012`、`G248:p0024:b013`、`G248:p0024:b014`、`G248:p0024:b015`、`G248:p0024:b016`。

<a id="deliverable"></a>

## 架构交付物 · Architecture Deliverable

标识：`deliverable`；类别：`representation`。

承载和组织相关架构制品、用于管理和沟通变更的成果。

边界与误读提示：制品数目、文件格式和验收规则需要按项目决定。

- [G248 PDF 24](../documents/G248.md#page-24)；书页 12，证据 `G248:A04`：documented by various artifacts and organized into specific deliverables
  章节：3.6. What About Artifacts and Deliverables?；正文块：`G248:p0024:b010`、`G248:p0024:b011`、`G248:p0024:b012`、`G248:p0024:b013`、`G248:p0024:b014`、`G248:p0024:b015`、`G248:p0024:b016`。
- [G188 PDF 51](../documents/G188.md#page-51)；书页 37，证据 `G188:A03`：acceptance criteria are a set of conditions
  章节：3.2.2. Define the Final Product of the Architecture Project and its Acceptance Criteria；正文块：`G188:p0051:b010`、`G188:p0051:b011`、`G188:p0051:b012`、`G188:p0051:b013`。

<a id="abstraction_level"></a>

## 架构抽象层次 · Architecture Level of Abstraction

标识：`abstraction_level`；类别：`classification`。

按上下文、概念、逻辑和物理分别解释为何、什么、如何及用什么实现。

边界与误读提示：与战略/分段/能力详细程度不同，不用一条单轴替换所有维度。

- [G248 PDF 25](../documents/G248.md#page-25)；书页 13，证据 `G248:A05`：four levels of abstraction
  章节：4. The Guide Approach；正文块：`G248:p0025:b006`、`G248:p0025:b007`、`G248:p0025:b008`。

<a id="roadmap"></a>

## 架构路线图 · Architecture Roadmap

标识：`roadmap`；类别：`planning`。

组织能力或架构从当前到期望状态的演进、依赖与取舍，并与迁移工作协调。

边界与误读提示：路线图需与批准范围、价值、成本及迁移计划结合，不是单纯日期列表。

- [G184 PDF 107](../documents/G184.md#page-107)；书页 93，证据 `G184:A07`：Roadmap
  正文块：`G184:p0107:b001`、`G184:p0107:b002`、`G184:p0107:b003`、`G184:p0107:b004`、`G184:p0107:b005`、`G184:p0107:b006`、`G184:p0107:b010`、`G184:p0107:b026`、`G184:p0107:b027`、`G184:p0107:b028`、`G184:p0107:b029`、`G184:p0107:b030`、`G184:p0107:b031`、`G184:p0107:b032`、`G184:p0107:b033`、`G184:p0107:b034`、`G184:p0107:b035`；短引在多个章节出现，未自动归属：G184:s0099、G184:s0100。
- [G21I PDF 46](../documents/G21I.md#page-46)；书页 32，证据 `G21I:A07`：business value and cost of work packages
  章节：11. Phase F: Migration Planning；正文块：`G21I:p0046:b006`、`G21I:p0046:b007`。
- [G188 PDF 72](../documents/G188.md#page-72)；书页 58，证据 `G188:A06`：body responsible for implementation
  章节：3.6.1. Products Handover；正文块：`G188:p0072:b026`、`G188:p0072:b027`、`G188:p0072:b028`。

<a id="work_package"></a>

## 迁移工作包 · Migration Work Package

标识：`work_package`；类别：`planning`。

为架构迁移组织的变更工作，需要考虑业务价值、成本、依赖及企业组合。

边界与误读提示：与G188架构项目计划中的工作分解包需按上下文区分。

- [G21I PDF 46](../documents/G21I.md#page-46)；书页 32，证据 `G21I:A07`：business value and cost of work packages
  章节：11. Phase F: Migration Planning；正文块：`G21I:p0046:b006`、`G21I:p0046:b007`。

<a id="risk"></a>

## 风险 · Risk

标识：`risk`；类别：`risk`。

不确定性对目标的影响，包括正向和负向偏差。

边界与误读提示：不将风险等同已经发生的问题，也不只记录威胁。

- [G152 PDF 21](../documents/G152.md#page-21)；书页 9，证据 `G152:A02`：effect of uncertainty on objectives
  章节：3.1.1. Definition of Risk；正文块：`G152:p0021:b009`。

<a id="security_architecture"></a>

## 安全架构 · Security Architecture

标识：`security_architecture`；类别：`risk`。

以组织、概念、逻辑及物理构件管理风险，横贯四个架构域的架构关注点。

边界与误读提示：不是脱离四个域的独立技术实现烟囱。

- [G152 PDF 20](../documents/G152.md#page-20)；书页 8，证据 `G152:A01`：organizational, conceptual, logical, and physical components
  章节：3. Enterprise Security Architecture；正文块：`G152:p0020:b002`、`G152:p0020:b003`、`G152:p0020:b004`、`G152:p0020:b005`。
- [G152 PDF 28](../documents/G152.md#page-28)；书页 16，证据 `G152:A03`：Business, Data, Application, and Technology
  章节：4. Security as a Cross-Cutting Concern；正文块：`G152:p0028:b007`、`G152:p0028:b008`、`G152:p0028:b009`、`G152:p0028:b011`、`G152:p0028:b012`、`G152:p0028:b013`、`G152:p0028:b014`。

<a id="security_domain"></a>

## 安全域 · Security Domain

标识：`security_domain`；类别：`risk`。

按同一安全政策管辖范围分组的资产与责任边界。

边界与误读提示：网络拓扑中的方框或子网不自动构成安全域。

- [G152 PDF 33](../documents/G152.md#page-33)；书页 21，证据 `G152:A04`：one security policy
  章节：5.3.2. Security Domain Model；正文块：`G152:p0033:b001`、`G152:p0033:b002`、`G152:p0033:b003`、`G152:p0033:b004`、`G152:p0033:b005`、`G152:p0033:b006`。

<a id="trust_relationship"></a>

## 信任关系 · Trust Relationship

标识：`trust_relationship`；类别：`risk`。

具有成立依据及责任交换的域间关系，可单向、双向或不存在。

边界与误读提示：技术证书、邻近位置或连接线本身不创造业务信任。

- [G152 PDF 33](../documents/G152.md#page-33)；书页 21，证据 `G152:A05`：unidirectional, bidirectional, or non-existent
  章节：5.3.3. Trust Framework；正文块：`G152:p0033:b015`、`G152:p0033:b016`、`G152:p0033:b017`、`G152:p0033:b018`、`G152:p0033:b019`、`G152:p0033:b020`。

<a id="security_requirement"></a>

## 安全需求 · Security Requirement

标识：`security_requirement`；类别：`constraint`。

为业务目标及风险需要提出、应可追溯业务驱动的安全要求。

边界与误读提示：安全需求与安全管理所期望的控制目标分开。

- [G152 PDF 40](../documents/G152.md#page-40)；书页 28，证据 `G152:A06`：Traceability mapping between business drivers and requirements
  章节：5.10.1. Business Attribute Profile；正文块：`G152:p0040:b007`。
- [G152 PDF 41](../documents/G152.md#page-41)；书页 29，证据 `G152:A07`：It differs from a security requirement
  章节：5.10.2. Control Objectives/Security Objectives；正文块：`G152:p0041:b031`、`G152:p0041:b032`、`G152:p0041:b033`、`G152:p0041:b034`。

<a id="control_objective"></a>

## 安全控制目标 · Security Control Objective

标识：`control_objective`；类别：`risk`。

安全管理要达到的期望状态，与业务属性关联。

边界与误读提示：控制目标不等于具体安全需求或某个已部署技术控制。

- [G152 PDF 41](../documents/G152.md#page-41)；书页 29，证据 `G152:A07`：It differs from a security requirement
  章节：5.10.2. Control Objectives/Security Objectives；正文块：`G152:p0041:b031`、`G152:p0041:b032`、`G152:p0041:b033`、`G152:p0041:b034`。

<a id="business_scenario"></a>

## 业务场景 · Business Scenario

标识：`business_scenario`；类别：`method`。

结合问题、环境、预期结果、参与者及交互，经适用性检查形成需求的分析方法。

边界与误读提示：不是只写一段用户故事，也不限定只可在一个ADM阶段使用。

- [G176 PDF 18](../documents/G176.md#page-18)；书页 6，证据 `G176:A01`：six steps
  章节：3.1. The Overall Process；正文块：`G176:p0018:b003`、`G176:p0018:b004`。
- [G176 PDF 27](../documents/G176.md#page-27)；书页 15，证据 `G176:A02`：critical steps and interactions between actors
  章节：4. Contents of a Business Scenario；正文块：`G176:p0027:b002`、`G176:p0027:b003`、`G176:p0027:b004`、`G176:p0027:b005`、`G176:p0027:b006`。
- [G176 PDF 30](../documents/G176.md#page-30)；书页 18，证据 `G176:A03`：any ADM phase
  章节：6. Business Scenarios and the TOGAF ADM；正文块：`G176:p0030:b009`、`G176:p0030:b010`、`G176:p0030:b011`。

<a id="smart_goal"></a>

## SMART目标 · SMART Goal

标识：`smart_goal`；类别：`measurement`。

可用明确、可衡量等SMART条件评价的业务预期结果。

边界与误读提示：示例权重和分数不是项目默认评价参数。

- [G176 PDF 36](../documents/G176.md#page-36)；书页 24，证据 `G176:A04`：specific, measurable
  章节：9.2.1. Example of Making Objectives SMART；正文块：`G176:p0036:b031`、`G176:p0036:b032`。

<a id="maturity_model"></a>

## 架构成熟度模型 · Architecture Maturity Model

标识：`maturity_model`；类别：`measurement`。

组织裁剪并周期性使用的架构实践改进评价模型。

边界与误读提示：G203示例的六等级和九要素不应冒充所有模型的唯一结构。

- [G203 PDF 11](../documents/G203.md#page-11)；书页 1，证据 `G203:A01`：organization-specific maturity model
  章节：1.1. Objective；正文块：`G203:p0011:b003`、`G203:p0011:b004`、`G203:p0011:b005`、`G203:p0011:b006`。
- [G203 PDF 11](../documents/G203.md#page-11)；书页 1，证据 `G203:A02`：periodically measure improvement
  章节：1.2. Background；正文块：`G203:p0011:b017`。
- [G203 PDF 13](../documents/G203.md#page-13)；书页 3，证据 `G203:A03`：six maturity levels and nine architecture elements
  章节：2.2. Elements of the ACMM；正文块：`G203:p0013:b020`。

<a id="readiness_assessment"></a>

## 数字技术采用就绪度评估 · Digital Technology Adoption Readiness Assessment

标识：`readiness_assessment`；类别：`measurement`。

识别基础条件、采用影响和持续因素并据此调整采用路径的评估。

边界与误读提示：因素依赖图只覆盖强或主导关系，不是完整因果网络。

- [G212 PDF 26](../documents/G212.md#page-26)；书页 10，证据 `G212:A01`：minimum acceptable readiness
  章节：4. Factors Impacting Digital Technology Adoption；正文块：`G212:p0026:b002`、`G212:p0026:b003`。
- [G212 PDF 26](../documents/G212.md#page-26)；书页 10，证据 `G212:A02`：strong and dominant relationships
  章节：4. Factors Impacting Digital Technology Adoption；正文块：`G212:p0026:b017`、`G212:p0026:b018`、`G212:p0026:b019`、`G212:p0026:b020`、`G212:p0026:b021`。
- [G212 PDF 46](../documents/G212.md#page-46)；书页 30，证据 `G212:A06`：identification of stakeholders
  章节：6. Architectural Implication and Alignment to the TOGAF ADM；表格：`G212:p0046:t01`。

<a id="adoption_approach"></a>

## ABCD采用方式 · ABCD Adoption Approach

标识：`adoption_approach`；类别：`classification`。

按采用广度和预期速度组合的四种类型，可结合因素渐进。

边界与误读提示：四类不构成优劣等级或互斥的一次性路径。

- [G212 PDF 39](../documents/G212.md#page-39)；书页 23，证据 `G212:A03`：breadth/extensiveness
  章节：5.1. Step 1: Select the Adoption Approach；正文块：`G212:p0039:b010`、`G212:p0039:b011`、`G212:p0039:b012`、`G212:p0039:b013`、`G212:p0039:b014`。
- [G212 PDF 40](../documents/G212.md#page-40)；书页 24，证据 `G212:A04`：do not depict any type of ranking
  章节：5.1. Step 1: Select the Adoption Approach；正文块：`G212:p0040:b012`、`G212:p0040:b013`、`G212:p0040:b014`。
- [G212 PDF 44](../documents/G212.md#page-44)；书页 28，证据 `G212:A05`：not mutually-exclusive
  章节：5.4. Step 4: Address Shortcomings and Initiate Digital Technology Adoption；正文块：`G212:p0044:b001`、`G212:p0044:b002`、`G212:p0044:b003`。

<a id="customer_mdm"></a>

## 客户主数据管理 · Customer Master Data Management

标识：`customer_mdm`；类别：`information-capability`。

以人员、过程、组织和系统组合将核心客户数据作为资产管理的能力。

边界与误读提示：自动化与人工流程共同处理质量问题，不是单个数据库产品。

- [G21B PDF 21](../documents/G21B.md#page-21)；书页 11，证据 `G21B:A01`：people, processes, organizations, and systems
  章节：3. C-MDM Capability；正文块：`G21B:p0021:b002`、`G21B:p0021:b003`、`G21B:p0021:b004`。
- [G21B PDF 21](../documents/G21B.md#page-21)；书页 11，证据 `G21B:A03`：algorithms do not produce certainty
  章节：3. C-MDM Capability；正文块：`G21B:p0021:b013`、`G21B:p0021:b014`、`G21B:p0021:b015`、`G21B:p0021:b016`、`G21B:p0021:b017`、`G21B:p0021:b018`、`G21B:p0021:b019`。

<a id="kernel_customer_data"></a>

## 核心客户数据 · Kernel Customer Data

标识：`kernel_customer_data`；类别：`information`。

跨部门共享的客户标识、联系、偏好同意及关系等核心信息。

边界与误读提示：指南字段清单是比较基线，实际范围应按需要选择。

- [G21B PDF 21](../documents/G21B.md#page-21)；书页 11，证据 `G21B:A02`：shared across the organization’s departments
  章节：3. C-MDM Capability；正文块：`G21B:p0021:b005`。
- [G21B PDF 37](../documents/G21B.md#page-37)；书页 27，证据 `G21B:A05`：not be used as a mandatory guideline
  章节：5.1. C-MDM Kernel Customer Data Scope；正文块：`G21B:p0037:b015`、`G21B:p0037:b016`、`G21B:p0037:b017`、`G21B:p0037:b018`。

<a id="government_reference_model"></a>

## 政府参考模型 · Government Reference Model

标识：`government_reference_model`；类别：`reference-model`。

为公共部门业务建模及转型提供共同视角的参考模板。

边界与误读提示：模型中的领域、功能、服务是参考分类，不是现成政府组织汇报图。

- [G21D PDF 21](../documents/G21D.md#page-21)；书页 1，证据 `G21D:A01`：common way to view themselves
  章节：1. Introduction；正文块：`G21D:p0021:b008`、`G21D:p0021:b009`。
- [G21D PDF 21](../documents/G21D.md#page-21)；书页 1，证据 `G21D:A02`：reference model template
  章节：1.1. Objective；正文块：`G21D:p0021:b011`、`G21D:p0021:b012`、`G21D:p0021:b013`、`G21D:p0021:b014`。
- [G21D PDF 24](../documents/G21D.md#page-24)；书页 4，证据 `G21D:A04`：Phase B: Business Architecture
  章节：1.4. The TOGAF Standard and the Government Reference Model；正文块：`G21D:p0024:b002`、`G21D:p0024:b003`、`G21D:p0024:b004`、`G21D:p0024:b005`。

<a id="dbrm"></a>

## 数字业务参考模型 · Digital Business Reference Model

标识：`dbrm`；类别：`reference-model`。

从数字、战略、结构和运营四域及十个核心要素提供数字业务参考视角。

边界与误读提示：高层图不定义详细关系，DBRM四域不可直接与TOGAF四域划等号。

- [G21H PDF 24](../documents/G21H.md#page-24)；书页 10，证据 `G21H:A03`：ten (10) core elements
  章节：3.1. Introduction；正文块：`G21H:p0024:b005`、`G21H:p0024:b006`、`G21H:p0024:b007`。
- [G21H PDF 24](../documents/G21H.md#page-24)；书页 10，证据 `G21H:A04`：says nothing about the detailed relationships
  章节：3.1. Introduction；正文块：`G21H:p0024:b012`。

<a id="business_system"></a>

## 业务系统 · Business System

标识：`business_system`；类别：`business`。

通过软硬资源、政策、过程、标准和人员共同实现业务能力的组合。

边界与误读提示：不是仅指软件应用。

- [G21H PDF 19](../documents/G21H.md#page-19)；书页 5，证据 `G21H:A02`：together implement a business capability
  章节：2.10. Business System；正文块：`G21H:p0019:b005`、`G21H:p0019:b006`。

<a id="msa"></a>

## 微服务架构 · Microservices Architecture

标识：`msa`；类别：`architecture-style`。

以独立、自包含、单一责任服务实现业务功能的架构风格。

边界与误读提示：不是产品、平台或框架，也不意味着所有系统都应拆分。

- [G21I PDF 16](../documents/G21I.md#page-16)；书页 2，证据 `G21I:A01`：not a product, framework, or platform
  章节：2. Microservices Architecture Defined；正文块：`G21I:p0016:b002`、`G21I:p0016:b003`、`G21I:p0016:b004`、`G21I:p0016:b005`。
- [G21I PDF 16](../documents/G21I.md#page-16)；书页 2，证据 `G21I:A02`：implements an Atomic Business Function
  章节：2. Microservices Architecture Defined；正文块：`G21I:p0016:b006`、`G21I:p0016:b007`、`G21I:p0016:b008`、`G21I:p0016:b009`、`G21I:p0016:b010`。

<a id="microservice"></a>

## 微服务 · Microservice

标识：`microservice`；类别：`building-block`。

实现原子业务功能、具有服务契约及API的独立自包含服务。

边界与误读提示：服务边界需由业务功能和数据约束决定，不仅由代码体积决定。

- [G21I PDF 16](../documents/G21I.md#page-16)；书页 2，证据 `G21I:A02`：implements an Atomic Business Function
  章节：2. Microservices Architecture Defined；正文块：`G21I:p0016:b006`、`G21I:p0016:b007`、`G21I:p0016:b008`、`G21I:p0016:b009`、`G21I:p0016:b010`。
- [G21I PDF 41](../documents/G21I.md#page-41)；书页 27，证据 `G21I:A06`：defined service contract
  章节：9.1. Microservices；正文块：`G21I:p0041:b018`、`G21I:p0041:b019`、`G21I:p0041:b020`。

<a id="atomic_business_function"></a>

## 原子业务功能 · Atomic Business Function

标识：`atomic_business_function`；类别：`business`。

企业中交付价值的最小业务功能单位，通常提供支持能力的服务。

边界与误读提示：最小是相对业务价值与上下文，不是固定代码行数。

- [G21I PDF 35](../documents/G21I.md#page-35)；书页 21，证据 `G21I:A03`：smallest unit of business function
  章节：7. Phase B: Business Architecture；正文块：`G21I:p0035:b015`、`G21I:p0035:b016`、`G21I:p0035:b017`、`G21I:p0035:b018`、`G21I:p0035:b019`、`G21I:p0035:b020`。

<a id="service_contract"></a>

## 微服务契约与API · Microservice Contract and API

标识：`service_contract`；类别：`constraint`。

说明微服务对外可使用接口及服务约定的信息，可通过目录被发现。

边界与误读提示：契约/API不等于消费者内部实现，也不自动授予跨边界数据访问。

- [G21I PDF 41](../documents/G21I.md#page-41)；书页 27，证据 `G21I:A06`：defined service contract
  章节：9.1. Microservices；正文块：`G21I:p0041:b018`、`G21I:p0041:b019`、`G21I:p0041:b020`。

<a id="metadata_management"></a>

## 元数据管理 · Metadata Management

标识：`metadata_management`；类别：`information-capability`。

规划、实施及控制高质量、集成元数据的活动。

边界与误读提示：不应缩减为部署一个存储库。

- [G234 PDF 14](../documents/G234.md#page-14)；书页 4，证据 `G234:A01`：planning, implementation, and control activity
  章节：3. Metadata Management Capability；正文块：`G234:p0014:b012`、`G234:p0014:b013`、`G234:p0014:b014`。
- [G234 PDF 24](../documents/G234.md#page-24)；书页 14，证据 `G234:A03`：processes and validation workflows
  章节：4.2.2. Formalize Metadata Management Processes；正文块：`G234:p0024:b009`、`G234:p0024:b010`。

<a id="metadata"></a>

## 元数据 · Metadata

标识：`metadata`；类别：`information`。

可分为业务、技术和运营类别、需定义来源、更新及验证方式的信息。

边界与误读提示：三类信息有不同语义，不应只有一个无类型文本字段。

- [G234 PDF 25](../documents/G234.md#page-25)；书页 15，证据 `G234:A04`：combination of technologies
  章节：4.3. Metadata Management Guidelines for Information Systems Architectures (ADM Phase C)；正文块：`G234:p0025:b003`、`G234:p0025:b004`、`G234:p0025:b005`。
- [G234 PDF 26](../documents/G234.md#page-26)；书页 16，证据 `G234:A05`：Business metadata
  章节：4.3. Metadata Management Guidelines for Information Systems Architectures (ADM Phase C)；正文块：`G234:p0026:b007`、`G234:p0026:b008`、`G234:p0026:b012`、`G234:p0026:b013`、`G234:p0026:b014`、`G234:p0026:b015`。

<a id="business_metadata"></a>

## 业务元数据 · Business Metadata

标识：`business_metadata`；类别：`information`。

元数据分类中的业务类别。

边界与误读提示：具体内容须按用例和术语明确，不由技术字段名自动决定。

- [G234 PDF 26](../documents/G234.md#page-26)；书页 16，证据 `G234:A05`：Business metadata
  章节：4.3. Metadata Management Guidelines for Information Systems Architectures (ADM Phase C)；正文块：`G234:p0026:b007`、`G234:p0026:b008`、`G234:p0026:b012`、`G234:p0026:b013`、`G234:p0026:b014`、`G234:p0026:b015`。

<a id="technical_metadata"></a>

## 技术元数据 · Technical Metadata

标识：`technical_metadata`；类别：`information`。

元数据分类中的技术类别。

边界与误读提示：需要保留与业务及运营语义的关联。

- [G234 PDF 26](../documents/G234.md#page-26)；书页 16，证据 `G234:A05`：Business metadata
  章节：4.3. Metadata Management Guidelines for Information Systems Architectures (ADM Phase C)；正文块：`G234:p0026:b007`、`G234:p0026:b008`、`G234:p0026:b012`、`G234:p0026:b013`、`G234:p0026:b014`、`G234:p0026:b015`。

<a id="operational_metadata"></a>

## 运营元数据 · Operational Metadata

标识：`operational_metadata`；类别：`information`。

元数据分类中的运营类别。

边界与误读提示：运营元数据不是基础设施监控指标的简单同义词。

- [G234 PDF 26](../documents/G234.md#page-26)；书页 16，证据 `G234:A05`：Business metadata
  章节：4.3. Metadata Management Guidelines for Information Systems Architectures (ADM Phase C)；正文块：`G234:p0026:b007`、`G234:p0026:b008`、`G234:p0026:b012`、`G234:p0026:b013`、`G234:p0026:b014`、`G234:p0026:b015`。

<a id="metadata_repository"></a>

## 元数据存储库 · Metadata Repository

标识：`metadata_repository`；类别：`information-system`。

按明确交换范围和协作契约接收或拉取元数据的存储与管理设施。

边界与误读提示：推送、拉取和手工是交换机制，不可与所有权或集成风格混同。

- [G234 PDF 28](../documents/G234.md#page-28)；书页 18，证据 `G234:A06`：Manual ingestion
  章节：4.3. Metadata Management Guidelines for Information Systems Architectures (ADM Phase C)；正文块：`G234:p0028:b017`、`G234:p0028:b018`、`G234:p0028:b027`。
- [G234 PDF 29](../documents/G234.md#page-29)；书页 19，证据 `G234:A07`：Security audit is required
  章节：4.3. Metadata Management Guidelines for Information Systems Architectures (ADM Phase C)；正文块：`G234:p0029:b008`。

<a id="bi_capability"></a>

## 商业智能能力 · Business Intelligence Capability

标识：`bi_capability`；类别：`information-capability`。

组合人员、过程、组织和系统，把决策相关数据转成增值信息的能力。

边界与误读提示：BI能力不等于一个数据平台产品。

- [G238 PDF 13](../documents/G238.md#page-13)；书页 3，证据 `G238:A01`：create value-added information
  章节：2. Business Intelligence & Analytics Capability；正文块：`G238:p0013:b002`、`G238:p0013:b003`、`G238:p0013:b004`、`G238:p0013:b005`、`G238:p0013:b006`。

<a id="data_lineage"></a>

## 数据血缘 · Data Lineage

标识：`data_lineage`；类别：`information`。

从运营数据源到数据消费的完整价值链上的数据来源及处理追溯。

边界与误读提示：局部数据表依赖不足以证明端到端血缘完整。

- [G238 PDF 14](../documents/G238.md#page-14)；书页 4，证据 `G238:A02`：from operational data sources to data consumption
  章节：2.2. BI & Analytics High-Level Business Functions Description；表格：`G238:p0014:t01`。

<a id="digital_sustainability"></a>

## 信息系统环境可持续性 · Environmental Sustainability of Information Systems

标识：`digital_sustainability`；类别：`cross-cutting`。

在业务生态范围内，以生命周期环境影响支持架构政策、目标、治理和增量改进。

边界与误读提示：运行能效不是完整环境足迹；指南提出的数据交换模型不是既有统一标准。

- [G242 PDF 29](../documents/G242.md#page-29)；书页 11，证据 `G242:A01`：environmental footprint required to build
  章节：3. Capabilities；正文块：`G242:p0029:b005`、`G242:p0029:b006`、`G242:p0029:b007`、`G242:p0029:b008`、`G242:p0029:b009`、`G242:p0029:b010`、`G242:p0029:b011`、`G242:p0029:b012`。
- [G242 PDF 30](../documents/G242.md#page-30)；书页 12，证据 `G242:A02`：Business Policies for Sustainability
  章节：3.2. How to Deploy a Sustainable Information System Policy；正文块：`G242:p0030:b012`、`G242:p0030:b013`、`G242:p0030:b014`、`G242:p0030:b015`、`G242:p0030:b016`。
- [G242 PDF 61](../documents/G242.md#page-61)；书页 43，证据 `G242:A03`：yearly environmental assessment
  章节：3.6.1. Build and Share Information System Carbon Footprint Measure from Cradle to Grave；正文块：`G242:p0061:b002`、`G242:p0061:b003`、`G242:p0061:b018`。
- [G242 PDF 75](../documents/G242.md#page-75)；书页 57，证据 `G242:A04`：entire business ecosystem
  章节：3.9. Governing the Transition Towards a Sustainable Information System；正文块：`G242:p0075:b004`、`G242:p0075:b005`、`G242:p0075:b006`。

<a id="role"></a>

## 角色 · Role

标识：`role`；类别：`people`。

活动与技能的组合；具体人员可承担多个角色。

边界与误读提示：岗位、角色和具体任务必须分别建模。

- [G249 PDF 16](../documents/G249.md#page-16)；书页 6，证据 `G249:A01`：Job means
  章节：4. Architecture Roles；正文块：`G249:p0016:b008`。
- [G249 PDF 16](../documents/G249.md#page-16)；书页 6，证据 `G249:A02`：multiple roles
  章节：4. Architecture Roles；正文块：`G249:p0016:b012`、`G249:p0016:b013`、`G249:p0016:b014`、`G249:p0016:b015`。

<a id="person"></a>

## 人员 · Person

标识：`person`；类别：`people`。

可在实际配置中承担一个或多个角色的个人。

边界与误读提示：语料角色模型不证明任何真实个人具有对应技能或任命。

- [G249 PDF 16](../documents/G249.md#page-16)；书页 6，证据 `G249:A02`：multiple roles
  章节：4. Architecture Roles；正文块：`G249:p0016:b012`、`G249:p0016:b013`、`G249:p0016:b014`、`G249:p0016:b015`。
- [G176 PDF 42](../documents/G176.md#page-42)；书页 30，证据 `G176:A05`：roles that can be filled by the same person
  章节：10. Roles；正文块：`G176:p0042:b002`、`G176:p0042:b003`、`G176:p0042:b004`、`G176:p0042:b005`。

<a id="job"></a>

## 岗位 · Job

标识：`job`；类别：`people`。

通常与雇佣契约对应的正式位置。

边界与误读提示：岗位名称不能直接确定架构角色范围、资格或决策权。

- [G249 PDF 16](../documents/G249.md#page-16)；书页 6，证据 `G249:A01`：Job means
  章节：4. Architecture Roles；正文块：`G249:p0016:b008`。

<a id="assignment"></a>

## 任务分配 · Assignment

标识：`assignment`；类别：`people`。

在角色和岗位上下文中分配的具体工作。

边界与误读提示：任务、角色和岗位不是一对一关系的预设。

- [G249 PDF 16](../documents/G249.md#page-16)；书页 6，证据 `G249:A01`：Job means
  章节：4. Architecture Roles；正文块：`G249:p0016:b008`。

<a id="skill"></a>

## 技能 · Skill

标识：`skill`；类别：`people`。

为履行架构角色需要、可按类别及熟练/知识深度分别描述的能力项。

边界与误读提示：技能类别不是岗位层级，矩阵要求也不是个人实测分数。

- [G198 PDF 13](../documents/G198.md#page-13)；书页 5，证据 `G198:A01`：depth of knowledge required
  章节：4.1. Overview；正文块：`G198:p0013:b012`。
- [G249 PDF 26](../documents/G249.md#page-26)；书页 16，证据 `G249:A06`：categories of skills
  章节：5. Skills and Proficiency Levels；正文块：`G249:p0026:b002`。

<a id="proficiency_level"></a>

## 技能熟练等级 · Skill Proficiency Level

标识：`proficiency_level`；类别：`measurement`。

在明确的指南量表中对单项技能知识深度或熟练程度的等级表达。

边界与误读提示：G198与G249的量表须保持各自定义，不自动换算或求平均。

- [G198 PDF 15](../documents/G198.md#page-15)；书页 7，证据 `G198:A02`：four levels of knowledge or proficiency
  章节：4.4. Proficiency Levels；正文块：`G198:p0015:b020`、`G198:p0015:b021`。
- [G198 PDF 13](../documents/G198.md#page-13)；书页 5，证据 `G198:A01`：depth of knowledge required
  章节：4.1. Overview；正文块：`G198:p0013:b012`。

<a id="enterprise_architect"></a>

## 企业架构师 · Enterprise Architect

标识：`enterprise_architect`；类别：`role`。

处理企业架构范围与整体上下文的角色；首席架构师是其中的特殊情况。

边界与误读提示：架构角色范围不自动等于职级或人员汇报结构。

- [G249 PDF 17](../documents/G249.md#page-17)；书页 7，证据 `G249:A03`：special case of an Enterprise Architect
  章节：4. Architecture Roles；正文块：`G249:p0017:b001`、`G249:p0017:b002`、`G249:p0017:b003`、`G249:p0017:b004`、`G249:p0017:b005`。
- [G249 PDF 17](../documents/G249.md#page-17)；书页 7，证据 `G249:A04`：superior architectures
  章节：4. Architecture Roles；正文块：`G249:p0017:b006`、`G249:p0017:b007`、`G249:p0017:b008`、`G249:p0017:b009`、`G249:p0017:b010`、`G249:p0017:b011`。

<a id="chief_architect"></a>

## 首席架构师 · Chief Architect

标识：`chief_architect`；类别：`role`。

企业架构师的特例，重点把架构融入战略和运营上下文。

边界与误读提示：specialization不是chief向enterprise任职者汇报的证据。

- [G249 PDF 17](../documents/G249.md#page-17)；书页 7，证据 `G249:A03`：special case of an Enterprise Architect
  章节：4. Architecture Roles；正文块：`G249:p0017:b001`、`G249:p0017:b002`、`G249:p0017:b003`、`G249:p0017:b004`、`G249:p0017:b005`。

<a id="solution_architect"></a>

## 解决方案架构师 · Solution Architect

标识：`solution_architect`；类别：`role`。

在企业及分段上位架构约束下处理具体方案工作的角色。

边界与误读提示：本概念只建模架构范围；详细职责及技能要求参见角色档案。

- [G249 PDF 17](../documents/G249.md#page-17)；书页 7，证据 `G249:A04`：superior architectures
  章节：4. Architecture Roles；正文块：`G249:p0017:b006`、`G249:p0017:b007`、`G249:p0017:b008`、`G249:p0017:b009`、`G249:p0017:b010`、`G249:p0017:b011`。

<a id="solution_architecture_work"></a>

## 解决方案架构工作 · Solution Architecture Work

标识：`solution_architecture_work`；类别：`work-scope`。

围绕明确需求形成并实施新增或变更解决方案的架构工作，受相关企业与分段架构指引。

边界与误读提示：这是工作范围，不能替换为架构师个人的全部权限、岗位或人事上下级。

- [G249 PDF 17](../documents/G249.md#page-17)；书页 7，证据 `G249:A04`：superior architectures
  章节：4. Architecture Roles；正文块：`G249:p0017:b006`、`G249:p0017:b007`、`G249:p0017:b008`、`G249:p0017:b009`、`G249:p0017:b010`、`G249:p0017:b011`。
