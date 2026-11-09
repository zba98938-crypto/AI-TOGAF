# 架构内容卷：独立图表审查

逐一查看20个独立图片资产，在22处引用中分别按上下文审查；5张HTML表逐行核对并保存真实合并单元格。

## b00049 Relationships between Deliverables, Artifacts, and Building Blocks

交付物含制品，制品分目录/矩阵/图并描述构建块；存储库保留可复用构建块及架构交付物。

左交付物与右存储库各三类制品之间双向箭头；左Artifacts到三类为无箭头分类线；交付物组与存储库交付物双向联系。

边界：制品与构建块不同身份；无打印基数，不从叠层推计数。

## b00052 Example — Architecture Definition Document

同一交付物中的多个制品可描述同一构建块，也可描述基线与目标不同状态。

Architecture Definition Document包含四制品；四条描述线指向Customer Services Representative，前两制品指Baseline Call Handling，后两指Target Call Handling。

边界：Describes是描述关系而非执行依赖；例子人物和过程不是案例事实。

## b00077 Content Framework by ADM Phase

内容框架按ADM组织上下文、定义、实现和变化管理。

顶部Preliminary/Architecture Requirements/Vision；定义中Business含Strategy/Operational，IS含Data/Application，与Technology并列；实现含Opportunities,Solutions,Migration及Implementation Governance；Change Management围外。

边界：分区不是每阶段独立模型或项目顺序，Requirements不是Phase I。

## b00080 Content Framework Overview

框架概览将业务、数据、应用、技术及变革上下文放入结构区域。

Business Capabilities与底部Capabilities分区不同；Data/Applications/Technology各有逻辑及物理组件；要求区域含Constraints/Assumptions/Gaps/Locations；下方Work Packages/Contracts。

边界：业务能力与通用能力不可仅因同译名合并；图不规定实体基数。

## b00106 Using the Content Framework to Structure the TOGAF Enterprise Metamodel

在2.3再次用内容框架分类元模型，不是新的图片内容。

与b00080共用同一资产指纹和实体分区，但本处用于元模型结构。

边界：一资产两引用分别定位；不计为两张独立源图。

## b00110 Relationships between Entities in the TOGAF Enterprise Metamodel

一般实体关联所有对象；业务层连接动机、能力、价值流、角色、流程、信息、服务，底层连接数据/应用/技术逻辑与物理组件。

Work Package与Capability以Delivers/Is delivered by关联；Driver→Goal Creates，Goal→Objective Is made specific，Objective→Measure Is tracked against；三域逻辑物理以Realizes/Is realized by配对；表2-3保留154行关系原词。

边界：密集交叉线部分无法仅凭图消除方向语义歧义，表内Used by反向成对及未定义类型另记，未杜撰基数。

## b00134 Basic Architectural Concepts

系统、架构、描述、利益相关者、关切、视点、视图、模型种类和模型保持不同身份。

System—Architecture exhibits两端1；Architecture—Description expresses两端1；Description聚合Views/VP端1..*；Viewpoint governs View两端1；ModelKind governs Model=1:1..*；Stakeholder has Concern两端1..*；View addresses Concern两端1..*。

边界：小三角表示标签阅读方向，非关联导航箭头；空心菱形与关系基数按原图保存，不把其他图泛化成此基数。

## b00148 Example Architecture View

嵌套盒示例表达2017年The Open Group地点中开展的业务职能。

五地点列Burlington/Reading/San Francisco/Dynamic-Virtual/Home Offices；Off-site有IT Infrastructure；Outsourced有PR/IT Support/Desktop Support；内部盒按table3-1表示Functions performed in Locations。

边界：不是汇报线、组织拥有权或当前2026地点事实。

## b00213 Interactions between Metamodel, Building Blocks, Diagrams, and Stakeholders

实际企业通过元模型描述进入存储库，标准制品集合组织视点，再选择具体利益相关者视图。

Reference Models与Application Platform有双向箭头；实际企业指向元模型；元模型指向Repository；Repository指向标准制品；标准制品指向Stakeholder Views；Queries/Analysis与Repository双向。

边界：缩略元模型文字不作为新增端点证据；视点方法与具体视图分开，查询不是批准。

## b00215 Artifacts Associated with the Enterprise Metamodel

各ADM区域中目录、矩阵、图示为候选制品分类。

Preliminary原则；A利益相关者及愿景图；B业务目录/矩阵/图；C数据/应用；D技术；E项目利益/因子/差距增量；F过渡和价值风险；Requirements需求目录。

边界：制品不是全都必须；同名能力/价值流图在A和B可不同深度，应用Migration/Software Distribution命名与正文3.6.6.13/14一致。

## b00523 Implementation Factor Catalog

实施因子目录用Factor/Description/Deduction关联环境因素及迁移影响。

Change in Technology例称消息中心改邮件节约700人，推论培训/重分配并提高优先；Consolidation/Introduction后两行空白。

边界：700仅源例；推论需当前业务证据，空白行不能推成无影响。

## b00529 Consolidated Gaps, Solutions, and Dependencies Matrix

整合差距、备选解决方案和依赖形成跨域规划输入。

No/Architecture/Gap/Potential Solutions/Dependencies五列；业务新订单流程drives applications(2)；应用行有COTS X或内部开发；信息行有客户库或数据集市。

边界：候选尚未选择，不能把COTS X改成最终批准方案；空依赖不等于无依赖。

## b00534 Architecture Definition Increments Table

以项目为行、过渡架构为列分配增量交付目标。

三列April2018/2019、2019/2020、2020/2021分别Preparation/Initial Operational Capability/Benefits；e-Services从培训流程到e-Licensing到e-Employment Benefits；IT信息逐步共用数据。

边界：示例旧日期不改成本项目期限；空格和省略号保未知，非容量证明。

## b00542 Transition Architecture State Evolution Table

TRM服务层面的状态演进表体现各SBB在过渡中的位置。

Information Exchange Services:System A(replace)→B-1(transition)→B-2(new)；Data Management:System D(retain)三列持续。

边界：状态标签不是自动业务验收或风险关闭；系统身份不同不可只改显示名合并。

## b00549 Sample Project Assessment with Respect to Business Value and Risk

项目气泡按价值纵轴、风险横轴和圈大小表示项目规模。

A/B左上，C/D右上，F/G左下，H右下，E跨中心；标题说明size of circle代表Project size。

边界：没有坐标数值、刻度、权重或圈面积公式，不自动算ROI或排项目优先。

## b00755 Key ADM Phases/Steps at which Building Blocks are Evolved/Specified

A高层候选构建块，B/C/D逐步选模型、定义状态、差距、路线图并评审，E把差距关联工作包。

中间Requirements Management与A—H实际双向箭头；右侧Step1—9保留；A与E外部粗箭头指相应阶段，三域框指B/C/D。

边界：中心双向箭头与其他ADM图的线样式分别取证；外环无箭头不臆造固定序列。

## b00769 Enterprise Continuum

Enterprise Continuum分类架构和方案资产，Enterprise Repositories提供实际资源。

两侧Repository↔Continuum的分类/资源方向分开；外部因素→上下文→Architecture；架构/方案之间Guides and Supports双向；Solutions→Deployed Solutions→Architecture Context回馈。

边界：连续体是分类工具不是物理存储库，部署对象不是未实现SBB规格。

## b00785 Architecture Continuum

架构连续体四类抽象由基础、共用系统、行业到组织特定。

四类相邻双向箭头，块形只示组合/扩展，无打印数量。

边界：抽象度不是ADM阶段或战略/分段/能力粒度。

## b00815 Solutions Continuum

方案连续体四类从基础、共用、行业到组织特定，支持复用和适配。

四类相邻双向箭头，Common Systems底部独立块为图形组成。

边界：不从块数推SBB多重性或真实产品清单。

## b00848 Relationships between Architecture and Solutions Continua

Architecture Continuum与Solutions Continuum对应类之间Guides & Supports双向。

上下各四类，相邻水平双向；四个垂直/斜向双箭头对应同类。

边界：四类之间不是唯一一对一实体匹配，也非四阶段采购流程。

## b00863 Overview of Architecture Repository

存储库包含元模型、全景、参考/标准库、治理、要求、方案及能力记录，并与外部来源和委员会联系。

标准与全景有遵循/生成最佳实践方向；外部参考/标准指向内库；全景与标准下指治理；Governance↔Board可见性/升级；Board→Architecture Capability治理；要求↔方案虚线Business outcomes delivered。

边界：箭头表达源关系不是自授权；要求—方案双向虚线不证明成果已实现，源表术语缺口保留。

## b00876 Architecture Continuum

Reference Library复用架构连续体进行参考材料分类。

同b00785资产和四类双向箭头，此处上下文为reference materials。

边界：复用图的分类法不表示每份参考资料已审阅或适用于当前组织。

## b00114 Table 2-1:  TOGAF Enterprise Metamodel Entities Metamodel Entity Description Actor A person, organization, or system that has a role that initiates

36个元模型实体定义形成概念边界，包括通用Capability与Business Capability、Actor与Role、逻辑与物理组件。

逐行定义Actor可以是人/组织/系统；Assumption未充分验证；Constraint阻止方法；Contract功能/非功能交互；Requirement定量需要；Process可分解且操作化能力/服务；Work Package可项目/计划。

边界：定义中的must与属性shall/should/may粒度不同；不能把未知假设当事实。

## b00117 Table 2-2:  TOGAF Enterprise Metamodel Attributes Metamodel Entity Attribute Description All Metamodel Entities ID Unique identifier for the architecture entity. Description Textual description of the architecture entity. Category User-definable categorization taxonomy for each metamodel

175属性行包含通用ID/Description/Category/Source/Owner及按实体指定的标准、生命周期、需求验收和契约质量。

合并单元格按rowspan/colspan保留；Requirement含shall/should/may与Acceptance criteria；Contract含Throughput+period、Growth+period、恢复/隐私/安全；FTE为估计，不等于任职资格。

边界：Role FTE行说明only basic attributes、Function/Process等date说明误写product，Service/Application Component/Technology Component泛型未在实体表独立定义；保留源问题，数值不补造。

## b00120 Table 2-3:  TOGAF Enterprise Metamodel Relationships Source Entity Target Entity Name Actor Actor Decomposes Actor Business Service Consumes Actor Data Entity Supplies or consumes Actor Event Generates Actor Event Resolves Actor Function Interacts with Actor Function Performs Actor Organization Unit Belongs to Actor Process Participates in Actor Process Triggers Actor Role Performs task in Actor Value Stream Performs a task in Application Service Business Service Automates some or all of Application Service Data Entity Used by Application Service Logical Application Component Is realized through Application Service Technology Service Is served by Business Capability Business Information Uses Business Capability Course of Action Is influenced by Business Capability Function Is delivered by Business Capability Organization Unit Is used by Business Capability Process Is operationalized by Business Capability Value Stream Enables Business Information Business Capability Is used by Business Information Business Service Used to derive Business Information Course of Action Is influenced by Business Information Data Entity Is realized by Business Information Process Uses Business Service Actor Is provided to Business Service Application Service Uses Business Service Business Information Is derived from Business Service Business Service Quality Meets Business Service Business Service Consumes Business Service Business Service Decomposes Business Service Contract Is governed and measured by Business Service Data Entity Is accessed and updated through Business Service Event Resolves Business Service Function Provides governed interface to access Business Service Logical Technology Component Is implemented on Business Service Organization Unit Is owned and governed by Business Service Process Is realized by Business Service Process Supports Capability Work Package Is delivered by Contract Business Service Governs, measures Contract Service Quality Meets Control Process Ensures correct operation of Course of Action Business Capability Influences Course of Action Business Information Influences Course of Action Function Influences Course of Action Goal Realizes Course of Action Organization Unit Influences Course of Action Product Influences Course of Action Value Stream Influences Data Entity Actor Is supplied or consumed by Data Entity Application Service Used by Data Entity Business Information Realizes Data Entity Business Service Is accessed and updated through Data Entity Data Entity Decomposes Data Entity Data Entity Relates to Data Entity Logical Data Component Resides within Driver Driver Decomposes Driver Goal Creates Driver Organization Unit Motivates Event Actor Is generated by Event Actor Is resolved by Event Business Service Is resolved by Event Process Is generated by Event Process Is resolved by Function Actor Supports Function Business Capability Delivers Function Business Service Is bounded by Function Course of Action Is influenced by Function Function Communicates with Function Function Decomposes Function Organization Unit Is owned by Function Process Orchestrates Function Process Decomposes Goal Course of Action Is realized by Goal Driver Addresses Goal Goal Decomposes Goal Objective Is made specific Logical Application Component Application Service Implements Logical Application Component Logical Application Component Decomposes Logical Application Component Logical Application Component Communicates with Logical Application Component Logical Data Component Used by Logical Application Component Logical Technology Component Is served

154个源/目标/关系名行逐行保留，区分语义方向及相反措辞。

Driver→Goal Creates；WorkPackage→Capability Delivers；Capability→WorkPackage Is delivered by；Physical与Logical Realizes/Is realized by；Process→Role Involves/Is performed by等可多关系。

边界：Business Service Quality和Service不在36实体表，Used by在某些两端同词不构成规范互逆关系；不臆造类型别名或基数。

## b00146 Table 3-1:  Architecture Viewpoint Example Architecture Viewpoint Element Description Stakeholders Management Board, Chief Executive Officer Concerns Show the top-level relationships between US/UK geographical

视点说明受众、关切和嵌套盒建模语义。

Management Board/CEO；关切地点与职能；外框Locations、内框Business Functions，嵌套表示职能在地点执行。

边界：无组织汇报或权限多重性，图为2017例子。

## b00564 Table 4-1:  Architecture Deliverables Produced by Executing the ADM Deliverable Output from…​ Input to…​ Architecture Building Blocks (see Section 4.2.1, “Architecture Building Blocks” ) B, C, D, F, H A, B, C, D, E, F, G, H Architecture Contract (see Section 4.2.2, “Architecture Contract” ) G G, H Architecture Definition Document (see Section 4.2.3, “Architecture Definition Document” ) A, B, C, D, E, F B, C, D, E, F, G, H Architecture Principles (see Section 4.2.4, “Architecture Principles” ) Preliminary, A, B, C, D Preliminary, A, B, C, D, E, F, G, H Architecture Repository (see Section 4.2.5, “Architecture Repository” ) Preliminary, A, B, C, D, Preliminary, A, B, C, D, E, F, G, H Requirements Management Architecture Requirements Specification (see Section 4.2.6, “Architecture Requirements Specification” ) B, C, D, E, F, Requirements Management C, D, Requirements Management Architecture Roadmap (see Section 4.2.7, “Architecture Roadmap” ) B, C, D, E, F B, C, D, E, F Architecture Vision (see Section 4.2.8, “Architecture Vision” ) A, E B, C, D, E, F, G, H, Requirements Management Business Principles, Business Goals, and Business Drivers (see Section 4.2.9, “Business Principles, Business Goals, and Business Drivers” ) Preliminary, A, B A, B Capability Assessment (see Section 4.2.10, “Capability Assessment” ) A, E B, C, D, E, F Change Request (see Section 4.2.11, “Change Request” ) F, G, H H Communications Plan (see Section 4.2.12, “Communications Plan” ) A B, C, D, E, F Compliance Assessment (see Section 4.2.13, “Compliance Assessment” ) G H Implementation and Migration Plan (see Section 4.2.14, “Implementation and Migration Plan” ) E, F F Implementation Governance Model (see Section 4.2.15, “Implementation Governance Model” ) F G, H Organizational Model for Enterprise Architecture (see Section 4.2.16, “Organizational Model for Enterprise Architecture” ) Preliminary Preliminary, A, B, C, D, E, F, G, H, Requirements Management Request for Architecture Work (see Section 4.2.17, “Request for Architecture Work” ) Preliminary, F, H A, G Requirements Impact Assessment (see Section 4.2.18, “Requirements Impact Assessment” ) Requirements Management Requirements Management Solution Building Blocks (see Section 4.2.19, “Solution Building Blocks” ) G A, B, C, D, E, F, G Statement of Architecture Work (see Section 4.2.20, “Statement of Architecture Work” ) A, B, C, D, E, F, G, H B, C, D, E, F,

21交付物按产生与消费ADM阶段形成信息依赖。

Communications Plan输出A、输入B—F；Contract输出G、输入G/H；Roadmap输出/输入B—F；Requirements Impact只在Requirements Management；SoAW可多阶段更新；原单元格全部保留。

边界：不是首次产生后才永远可用的顺序表；与阶段具体inputs/outputs细节有差异须逐项核对，末尾逗号等源排版不默补。

