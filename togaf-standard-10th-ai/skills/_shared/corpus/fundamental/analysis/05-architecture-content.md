# 架构内容：当前语义解析

本页为逐节语义解释，不能把解释当全文译文。本卷另有[逐块中文正文](../chinese-text/05-architecture-content.md)，已写正文的最终独立语义校核仍待完成。

[英文及离线原文](../web-2025/volumes/05-architecture-content/index.html)

<a id="chap01"></a>
## 1. Introduction

概念：本章是内容框架导读。

适用条件：阅读本卷时。

逻辑关系：后续依次展开制品、交付物、构建块、连续体与资料库。

制品及证据：本卷目录。

适用边界：引言不新增完整性验收规则。

来源块：C220-web-2025:05-architecture-content:b00041, C220-web-2025:05-architecture-content:b00042

<details><summary>展开本节完整英文来源</summary>

1. Introduction

This chapter provides an introduction to the guidance provided in the
TOGAF Standard — Architecture Content (this document).

</details>

<a id="tag_01_01"></a>
## 1.1. Overview

概念：交付物有契约与正式审签语境；制品表达架构某方面；构建块是可复用组成。

适用条件：执行ADM和整理工作成果时。

逻辑关系：交付物可含多个制品；制品可表达多个构建块；ABB描述逻辑需要，SBB实现部分或全部ABB。

决策方法：按用途分类成果，并映射采用的外部内容框架。

制品及证据：交付物—制品—构建块关系及审签记录。

适用边界：文件或图片存在不证明契约审签；业务构建块不限IT产品。

来源块：C220-web-2025:05-architecture-content:b00043, C220-web-2025:05-architecture-content:b00044, C220-web-2025:05-architecture-content:b00045, C220-web-2025:05-architecture-content:b00046, C220-web-2025:05-architecture-content:b00047, C220-web-2025:05-architecture-content:b00048, C220-web-2025:05-architecture-content:b00049, C220-web-2025:05-architecture-content:b00050, C220-web-2025:05-architecture-content:b00051, C220-web-2025:05-architecture-content:b00052, C220-web-2025:05-architecture-content:b00053

<details><summary>展开本节完整英文来源</summary>

1.1. Overview

Architects executing the Architecture Development Method (ADM) will
produce a number of outputs as a result of their efforts, such as
process flows, architectural requirements, project plans, or project
compliance assessments. The Content Framework provides a structural
model for architectural content that allows the major work products that
an architect creates to be consistently defined, structured, and
presented.

The Content Framework provided here is intended to allow the TOGAF
framework to be used as a stand-alone framework for architecture within
an enterprise. However, other Content Frameworks exist (such as the
Zachman ® Framework) and it is anticipated that some enterprises may opt to use an external framework in conjunction with the TOGAF framework. In these cases, the TOGAF Content Framework provides a useful reference and
starting point for TOGAF content to be mapped to other Content
Frameworks.

The Architecture Content Framework uses the following three categories to describe the type of architectural work product within the context of use:

A deliverable is a work product that is contractually specified and in turn formally reviewed, approved, and signed off by the stakeholders Deliverables represent the output of projects and those deliverables
that are in documentation form will typically be archived at completion
of a project, or transitioned into an Architecture Repository as a
reference model, standard, or snapshot of the Architecture Landscape at a point in time. An artifact is an architectural work product that describes an aspect of the architecture Artifacts are generally classified as catalogs (lists of things),
matrices (showing relationships between things), and diagrams (pictures of things). Examples include a requirements catalog, application interaction matrix, and a value chain diagram. An architectural deliverable may contain many artifacts and artifacts will form the
content of the Architecture Repository. A building block represents a potentially re-usable component
that can be combined with other building blocks to deliver architectures and solutions Building blocks can be defined at various levels of detail, depending on what stage of architecture development has been reached. For instance, at an early stage, a building block can simply consist of a name or an outline description. Later on, a building block may be decomposed into
multiple supporting building blocks and may be accompanied by a full
specification. Building blocks can relate to “architectures” or
“solutions”. Architecture Building Blocks (ABBs) typically describe what is
required of SBBs at a more logical or supplier-independent level; those
requirements may include services to be performed, data resources, and
capabilities needed. ABBs include logical business, application, and
technology components Solution Building Blocks (SBBs) represent physical or supplier-specific components that have the capability to realize part or all of a more logical ABB. There are business, application, and
technology SBBs.

The relationships between deliverables, artifacts, and building blocks are shown in Figure 1-1 .



Figure 1-1: Relationships between Deliverables, Artifacts, and Building Blocks

For example, an Architecture Definition Document is a deliverable that
documents an Architecture Description. This document will contain a number of complementary artifacts that are architecture views of the building blocks relevant to the architecture. For example, a process flow diagram (an artifact) may be created to describe the target call
handling process (a building block). This artifact may also describe other building blocks, such as the actors involved in the process (e.g., a Customer Services Representative). An example of the relationships between deliverables, artifacts, and building blocks is illustrated in Figure 1-2 .



Figure 1-2: Example — Architecture Definition Document

</details>

<a id="tag_01_02"></a>
## 1.2. TOGAF Content Framework and Enterprise Metamodel

概念：内容框架与企业元模型的分组标题。

适用边界：本节仅标题，定义和要求在子节。

来源块：C220-web-2025:05-architecture-content:b00054

<details><summary>展开本节完整英文来源</summary>

1.2. TOGAF Content Framework and Enterprise Metamodel

</details>

<a id="tag_01_02_01"></a>
## 1.2.1. Overview

概念：预备阶段需定义成果分类、企业实体关系与具体制品。

适用条件：建立组织特定EA能力。

逻辑关系：内容框架及元模型支持ADM生命周期；选择受框架与工具影响。

决策方法：先明确分类和模型范围，再确认需开发的制品。

制品及证据：组织内容框架、元模型及制品选择记录。

适用边界：原文“specific artifacts”指向交付物章，术语引用张力保留。

来源块：C220-web-2025:05-architecture-content:b00055, C220-web-2025:05-architecture-content:b00056, C220-web-2025:05-architecture-content:b00057, C220-web-2025:05-architecture-content:b00058, C220-web-2025:05-architecture-content:b00059, C220-web-2025:05-architecture-content:b00060

<details><summary>展开本节完整英文来源</summary>

1.2.1. Overview

The TOGAF ADM provides lifecycle management to create and manage architectures within an enterprise. At each phase within the ADM, a discussion of inputs, outputs, and steps describes a number of architecture work products.

An essential task when establishing the enterprise-specific Enterprise
Architecture Capability in the Preliminary Phase of the ADM is to
define:

A categorization framework to be used to structure the Architecture
Descriptions, the work products used to express an architecture, and the collection of models that describe the architecture; this is referred to as the Content Framework An understanding of the types of entities within the enterprise and
the relationships between them that need to be captured, stored, and
analyzed in order to create the Architecture Description; this Enterprise Metamodel depicts this information in the form of a formal
model The specific artifacts to be developed (see Chapter 4, Architecture Deliverables )

The Content Framework chosen is likely to be influenced by:

The Architecture Framework selected as the basis for the Enterprise
Architecture Capability The chosen software tool used to support the Enterprise Architecture
Capability

</details>

<a id="tag_01_02_02"></a>
## 1.2.2. Content Framework

概念：内容框架规定架构描述、表达成果与模型的分类。

适用条件：建立企业特定架构框架及资料库。

逻辑关系：资料库按此分类保存成果；内容框架是企业框架的一部分。

决策方法：确认保存分类与成果类型一致。

制品及证据：成果分类及资料库组织方式。

适用边界：内容框架不是企业实体关系元模型。

来源块：C220-web-2025:05-architecture-content:b00061, C220-web-2025:05-architecture-content:b00062, C220-web-2025:05-architecture-content:b00063

<details><summary>展开本节完整英文来源</summary>

1.2.2. Content Framework

The Content Framework defines a categorization framework to be used to structure the Architecture Description, the work product used to express an architecture, and the collection of models that describe the architecture.

The Architecture Repository, which is explained in Section 4.2.5, “Architecture Repository” ,
is structured to store the artifacts and work products identified in the
Content Framework. The Content Framework is one element of the
Enterprise-Specific Architecture Framework.

</details>

<a id="tag_01_02_03"></a>
## 1.2.3. Enterprise Metamodel

概念：元模型定义企业模型中实体类型及关系，支持一致、完整与追溯检查。

适用条件：建立模型语言、架构工具和EA能力时。

逻辑关系：类型、属性、关系覆盖需结合具体企业；可用不同能表达相关概念的记法。

决策方法：检验所选语言能否保存所需实体及事实，按企业裁剪。

制品及证据：组织元模型及记法覆盖说明。

适用边界：不限制选择制品或记法；结构完整不证明所有业务事实正确。

来源块：C220-web-2025:05-architecture-content:b00064, C220-web-2025:05-architecture-content:b00065, C220-web-2025:05-architecture-content:b00066, C220-web-2025:05-architecture-content:b00067, C220-web-2025:05-architecture-content:b00068, C220-web-2025:05-architecture-content:b00069, C220-web-2025:05-architecture-content:b00070

<details><summary>展开本节完整英文来源</summary>

1.2.3. Enterprise Metamodel

The TOGAF Standard encourages development of an Enterprise Metamodel, which defines the types of entity to appear in the models that describe the enterprise, together with the relationships between these entities.

An Enterprise Metamodel provides value in several ways:

It gives architects a starter set of the types of thing to investigate
and to cover in their models It provides a form of completeness-check for any architecture modeling
language, or architecture metamodel, that is proposed for use in an
enterprise Namely, how completely does it handle the types of entity in the
Enterprise Metamodel, and manage required facts about them such as their
attributes and relationships? It can help ensure: Consistency Completeness Traceability

Note that the TOGAF Standard does not aim to constrain an enterprise’s:

Selection of artifacts Modeling notation The TOGAF Standard can be used with the ArchiMate ® modeling language, Business
Process Model and Notation™ (BPMN™), Unified Modeling
Language™ (UML ® ), entity relationship diagramming, flowcharting, or
any other notation that can express some TOGAF ideas.

The types of entity within an enterprise and the relationships between
them are specific to the individual enterprise. Developing a
high-quality metamodel is an important aspect of establishing the
Enterprise Architecture Capability.

</details>

<a id="tag_01_02_04"></a>
## 1.2.4. The TOGAF Content Framework

概念：内容框架按ADM阶段组织架构成果及其上下文。

适用条件：企业可选TOGAF或其他框架并适配。

逻辑关系：原则愿景需求、B业务、C信息系统、D技术、实现转型及变更价值分别组织内容。

决策方法：选择并裁剪分类，以成果检查表降低遗漏。

制品及证据：分类结构及各域/过渡/变更成果。

适用边界：可创建的全面清单不是每次必须制作的全部制品。

来源块：C220-web-2025:05-architecture-content:b00071, C220-web-2025:05-architecture-content:b00072, C220-web-2025:05-architecture-content:b00073, C220-web-2025:05-architecture-content:b00074, C220-web-2025:05-architecture-content:b00075, C220-web-2025:05-architecture-content:b00076, C220-web-2025:05-architecture-content:b00077, C220-web-2025:05-architecture-content:b00078, C220-web-2025:05-architecture-content:b00079, C220-web-2025:05-architecture-content:b00080, C220-web-2025:05-architecture-content:b00081

<details><summary>展开本节完整英文来源</summary>

1.2.4. The TOGAF Content Framework

The TOGAF Content Framework defines a categorization framework to be
used to structure the Architecture Description, the work products used
to express an architecture, and the collection of models that describe
the architecture.

There are many alternative Content Frameworks (e.g., the TOGAF Content
Framework, the Zachman Framework, DoDAF, NAF, etc.). Selecting a Content
Framework is essential even though the choice of Content Framework is
less important. The final Content Framework is usually adapted to fit
specific organization needs.

The TOGAF Content Framework is intended to:

Provide a detailed model of architectural work products Drive consistency in the outputs created when following the ADM Provide a comprehensive checklist of architecture output that could be
created Reduce the risk of gaps within the final architecture deliverable set Help an enterprise mandate standard architecture concepts, terms, and
deliverables

At the highest level, the TOGAF Content Framework (see Figure 1-3 ) is structured in line with the phases of the ADM.



Figure 1-3: Content Framework by ADM Phase

Architecture Principles, Vision, Motivation, and Requirements models
are intended to capture the surrounding context of formal architecture models, including general Architecture Principles, strategic context that forms input for architecture modeling, and requirements generated
from the architecture The relevant aspects of the business context that have given rise to the
Request for Architecture work are typically investigated, refined,
validated, and recorded in the Preliminary and Architecture Vision
phases. Business Architecture captures architecture models of the business,
looking specifically at factors that motivate the enterprise, its
structure, and its capabilities Information Systems Architecture models capture architecture models
of IT systems, looking at applications and data in line with the TOGAF
ADM phases Technology Architecture models capture technology assets that are
used to implement and realize information system solutions Architecture Realization/Transformation models capture change
roadmaps showing transition between architecture states and binding
statements that are used to steer and govern an implementation of the
architecture Architecture Change Management models capture value realization
management events, internal and external, that impact the Enterprise
Architecture and the generation of requirements for action



Figure 1-4: Content Framework Overview

</details>

<a id="tag_01_03"></a>
## 1.3. Content Framework and the TOGAF ADM

概念：ADM描述工作过程，内容框架细化其输入输出及整体架构语境。

适用条件：基线到目标的愿景、定义、转型及治理全过程。

逻辑关系：过程回答如何开发，内容框架说明开发成果如何组织。

决策方法：将阶段步骤与成果定义共同使用。

制品及证据：阶段输入输出映射。

适用边界：有内容结构不能代替实际ADM工作及业务判断。

来源块：C220-web-2025:05-architecture-content:b00082, C220-web-2025:05-architecture-content:b00083, C220-web-2025:05-architecture-content:b00084

<details><summary>展开本节完整英文来源</summary>

1.3. Content Framework and the TOGAF ADM

The TOGAF ADM describes the process of moving from a baseline state of
the enterprise to a target state of the enterprise. The ADM will address
a business need through a process of visioning, architecture definition,
transformation planning, and Architecture Governance. At each stage in this process, the ADM requires information as inputs and will create outputs as a result of executing a number of steps. The Content Framework provides an underlying structure for the ADM that defines inputs and outputs in more detail and puts each deliverable into the context of the holistic architecture view of the enterprise.

The Content Framework should therefore be used as a companion to the ADM. The ADM describes what needs to be done to create an architecture and the Content Framework describes what the architecture should look like once it is done.

</details>

<a id="tag_01_04"></a>
## 1.4. The Enterprise Continuum

概念：连续体显示多份相关架构从通用到专用、抽象到具体、逻辑到物理的演进。

适用条件：无法用一个架构永久满足所有关切。

逻辑关系：明确架构边界可把复杂问题分解成可管理部分。

决策方法：先限定目的与范围，再分析架构间关系。

制品及证据：架构范围及连续体分类。

适用边界：不是强行把多份相关架构合成一个永久架构。

来源块：C220-web-2025:05-architecture-content:b00085, C220-web-2025:05-architecture-content:b00086, C220-web-2025:05-architecture-content:b00087, C220-web-2025:05-architecture-content:b00088, C220-web-2025:05-architecture-content:b00089

<details><summary>展开本节完整英文来源</summary>

1.4. The Enterprise Continuum

It is usually impossible to create a single unified architecture that
meets all the requirements of all stakeholders for all time. Therefore,
the Enterprise Architect will need to deal not just with a single
Enterprise Architecture, but with many related Enterprise Architectures.

Each architecture may have a different purpose and architectures may relate to one another. Effectively bounding the scope of an architecture is therefore a Critical Success Factor (CSF) in allowing architects to break down a complex problem space into manageable components that can be individually addressed.

The Enterprise Continuum provides a view of the Architecture Repository that shows the evolution of these related architectures from generic to specific, from abstract to concrete, and from logical to physical.

Chapter 6, Enterprise Continuum discusses the Enterprise Continuum; including the Architecture Continuum and the Solutions Continuum.

</details>

<a id="tag_01_05"></a>
## 1.5. The Architecture Repository

概念：成熟EA能力需资产分类以及存储流程和工具。

适用条件：企业架构产物规模较大。

逻辑关系：资料库区分不同抽象层的资产，结构详见第7章。

决策方法：确定资产分类与管理流程。

制品及证据：资料库结构与管理约定。

适用边界：储存数量不能证明内容质量或成熟度。

来源块：C220-web-2025:05-architecture-content:b00090, C220-web-2025:05-architecture-content:b00091, C220-web-2025:05-architecture-content:b00092

<details><summary>展开本节完整英文来源</summary>

1.5. The Architecture Repository

Operating a mature Architecture Capability within a large enterprise
creates a huge volume of architectural output. Effective management and
leverage of these architectural work products require a formal taxonomy
for different types of architectural asset alongside dedicated processes
and tools for architectural content storage.

Chapter 7, Architecture Repository provides a structural framework for an Architecture Repository that allows an enterprise to distinguish between different types of architectural assets that exist at different levels of abstraction in the organization.

</details>

<a id="chap02"></a>
## 2. TOGAF Content Framework and Enterprise Metamodel

概念：内容框架与元模型的章节标题。

适用边界：仅分组，无独立新增约束。

来源块：C220-web-2025:05-architecture-content:b00093

<details><summary>展开本节完整英文来源</summary>

2. TOGAF Content Framework and Enterprise Metamodel

</details>

<a id="tag_02_01"></a>
## 2.1. Overview

概念：内容框架组织架构描述；元模型定义实体类型及关系。

适用条件：ADM术语一致化与架构工具实现。

逻辑关系：正式结构支持成果与模型术语一致。

决策方法：分开配置成果分类和实体关系模型。

制品及证据：内容框架及企业元模型。

适用边界：工具字段完整不表示企业事实已核实。

来源块：C220-web-2025:05-architecture-content:b00094, C220-web-2025:05-architecture-content:b00095, C220-web-2025:05-architecture-content:b00096, C220-web-2025:05-architecture-content:b00097, C220-web-2025:05-architecture-content:b00098

<details><summary>展开本节完整英文来源</summary>

2.1. Overview

The TOGAF ADM provides a process lifecycle to create and manage
architectures within an enterprise. At each phase within the ADM, a
discussion of inputs, outputs, and steps describes a number of
architectural work products or artifacts, such as process and
application.

The Content Framework and Enterprise Metamodel provided here define a formal structure for these terms to ensure consistency within the ADM and also to provide guidance for organizations that wish to implement their architecture within an architecture tool.

The Content Framework defines a categorization framework to be used to structure the Architecture Description, the work product used to express an architecture, and the collection of models that describe the architecture.

The Enterprise Metamodel defines the types of entities to appear in
the models that describe the enterprise, together with the relationships between these entities.

</details>

<a id="tag_02_02"></a>
## 2.2. TOGAF Enterprise Metamodel Vision

概念：TOGAF元模型覆盖多数企业可能遇到的实体关系，供预备阶段组织特定模型起点。

适用条件：建立EA能力及选择阶段制品。

逻辑关系：组织可移除不适用类型，也可增加所需类型与关系。

决策方法：逐项判断相关性并记录增删依据。

制品及证据：组织元模型及裁剪记录。

适用边界：参考模型不是当前企业实体清单。

来源块：C220-web-2025:05-architecture-content:b00099, C220-web-2025:05-architecture-content:b00100, C220-web-2025:05-architecture-content:b00101, C220-web-2025:05-architecture-content:b00102

<details><summary>展开本节完整英文来源</summary>

2.2. TOGAF Enterprise Metamodel Vision

The TOGAF Standard includes the TOGAF Enterprise Metamodel which
captures the entities and relationships that are likely to be
encountered in the majority of enterprises. This may be used as the
basis for developing an Organization-Specific Metamodel when
establishing the Enterprise Architecture Capability in the Preliminary Phase and also provides the context for the specific artifacts referenced in the descriptions of the ADM phases and described in detail in Chapter 3, Architectural Artifacts .

When developing an Organization-Specific Metamodel, architects may
choose not to include entities and relationships from the TOGAF
Enterprise Metamodel which are not relevant and/or add additional
entities and relationships.

This section provides an overview of the TOGAF Enterprise Metamodel.
Subsequent sections discuss each area of the metamodel in more detail.

</details>

<a id="tag_02_02_01"></a>
## 2.2.1. Overview of the TOGAF Enterprise Metamodel

概念：元模型允许概念被捕获、保存、过滤、查询及表达。

适用条件：追求模型一致性、完整性和可追溯性。

逻辑关系：内容框架可用于组织元模型的表示。

决策方法：按所需查询检查类型和关系。

制品及证据：结构化元模型及查询/表示约定。

适用边界：模型分类图不定义实体实例或实际关系。

来源块：C220-web-2025:05-architecture-content:b00103, C220-web-2025:05-architecture-content:b00104, C220-web-2025:05-architecture-content:b00105, C220-web-2025:05-architecture-content:b00106, C220-web-2025:05-architecture-content:b00107

<details><summary>展开本节完整英文来源</summary>

2.2.1. Overview of the TOGAF Enterprise Metamodel

The TOGAF Enterprise Metamodel includes a set of entities, defined in Section 2.4, “TOGAF Enterprise Metamodel Entities” , that allow
architectural concepts to be captured, stored, filtered, queried, and
represented in a way that supports consistency, completeness, and
traceability.

The categorization mechanism of the Content Framework may be used to
structure a representation of the TOGAF Enterprise Metamodel, as shown
in Figure 2-1 .



Figure 2-1: Using the Content Framework to Structure the TOGAF Enterprise Metamodel

</details>

<a id="tag_02_03"></a>
## 2.3. TOGAF Enterprise Metamodel in Detail

概念：图2-2展示元模型实体间关系。

适用条件：查看完整关系结构。

逻辑关系：关系必须与类型定义及表2-3共同解释。

决策方法：保留源图端点、方向及关系含义，并核查表格。

制品及证据：图2-2及关系定义表。

适用边界：密集关系不得从布局推断未标基数；独立图审另存。

来源块：C220-web-2025:05-architecture-content:b00108, C220-web-2025:05-architecture-content:b00109, C220-web-2025:05-architecture-content:b00110, C220-web-2025:05-architecture-content:b00111

<details><summary>展开本节完整英文来源</summary>

2.3. TOGAF Enterprise Metamodel in Detail

The relationships between entities in the TOGAF Enterprise Metamodel are
shown in Figure 2-2 .



Figure 2-2: Relationships between Entities in the TOGAF Enterprise Metamodel

</details>

<a id="tag_02_04"></a>
## 2.4. TOGAF Enterprise Metamodel Entities

概念：表2-1给出企业元模型实体的定义。

适用条件：构建组织模型和检查术语。

逻辑关系：类型定义约束实体身份，避免角色、演员、能力或服务混用。

决策方法：按定义判断类型，再决定是否适用于企业。

制品及证据：实体类型、源定义及采用范围。

适用边界：定义不证明该实体在本项目存在；单元格复核由独立表审补入。

来源块：C220-web-2025:05-architecture-content:b00112, C220-web-2025:05-architecture-content:b00113, C220-web-2025:05-architecture-content:b00114

<details><summary>展开本节完整英文来源</summary>

2.4. TOGAF Enterprise Metamodel Entities

Table 2-1 lists and describes the entities within the Enterprise Metamodel.

Table 2-1:  TOGAF Enterprise Metamodel Entities Metamodel Entity Description Actor A person, organization, or system that has a role that initiates
or interacts with activities; for example, a sales representative who
travels to visit customers. Actors may be internal or external to an
organization. In the automotive industry, an original equipment
manufacturer would be considered an actor by an automotive dealership
that interacts with its supply chain activities. Application Service The automated elements of a business service. An
application service may deliver or support part or all of one or more
business services. Assumption A statement of probable fact that has not been fully
validated at this stage, due to external constraints. For example, it
may be assumed that an existing application will support a certain set
of functional requirements, although those requirements may not yet have
been individually validated. Business Capability A particular ability that a business may possess
or exchange to achieve a particular purpose. Business Information Represents a concept and its semantics used
within the business. Business Service Supports the business by encapsulating a unique
element of business behavior; a service offered external to the
enterprise may be supported by business services. Capability An ability that an organization, person, or system possesses. Note: This a general-purpose definition. See Business Capability for how
this concept is refined for usage in Business Architecture. Constraint An external factor that prevents an organization from
pursuing particular approaches to meet its goals. For example, customer
data is not harmonized within the organization, regionally or
nationally, constraining the organization’s ability to offer effective
customer service. Contract An agreement between a consumer and a provider that
establishes functional and non-functional parameters for interaction.
This applies to all types of service interactions within the metamodel. Control A decision-making step with accompanying decision logic used
to determine execution approach for a process or to ensure that a
process complies with governance criteria. For example, a sign-off
control on the purchase request processing process that checks whether
the total value of the request is within the sign-off limits of the
requester, or whether it needs escalating to higher authority. Course of Action Direction and focus provided by strategic goals and
objectives, often to deliver the value proposition characterized in the
business model. Data Entity Represents data that is recognized by the business as a
distinct concept. Driver An external or internal condition that motivates the
organization to define its goals. An example of an external driver is a
change in regulation or compliance rules which, for example, require
changes to the way an organization operates; i.e., Sarbanes-Oxley in the
US. Event An organizational state change that triggers processing events;
may originate from inside or outside the organization and may be
resolved inside or outside the organization. Function A set of business behaviors based on a chosen set of
criteria. Functions are usually close-coupled to/with organizational
units. Gap A statement of difference between two states. Used in the context of gap
analysis, where the difference between the Baseline and Target
Architecture is identified. Note: Gap analysis is described in the TOGAF Standard — ADM Techniques . Goal A high-level statement of intent or direction for an
organization. Typically used to measure success of an organization. Location A place where activities occur. Locations can be composed and
decomposed. Logical Application Component An encapsulation of application functionality that is
definable by services offered and data maintained, independently of
implementation and technology. Logical Data Component A data structure composed of logically-related data entities. Logical Technology Component An implementation-independent encapsulation of technology
services. Measure An indicator or factor that can be tracked, usually on an
ongoing basis, to determine success or alignment with objectives and
goals. Objective An organizational aim that is declared in a Simple,
Measurable, Actionable, Realistic, and Timebound (SMART) way. For
example, “Increase capacity utilization by 30% by the end of the year,
to support the planned increase in market share”. Organization Unit A self-contained unit of resources with goals,
objectives, and measures. Organization units may include external
parties and business partner organizations. Physical Application Component A realization of logical application functionality using
components of functionality in applications that may be hired, procured,
or built. Physical Data Component A data structure that realizes related logical data
components represented in the format or schema required by a particular
technology. Physical Technology Component A realization of logical technology functionality using a
particular technology product that may be deployed. Principle A qualitative statement of intent that should be met by the
architecture. It has at least a supporting rationale and a measure of
importance. Note: A sample set of Architecture Principles is defined in the TOGAF Standard — ADM Techniques . Process A process represents a sequence of activities that together achieve a
specified outcome, can be decomposed into sub-processes, and can show
operation of a business capability or service (at next level of detail). Processes may also be used to link organizations, business capabilities,
services, and processes. A process may realize one service and/or
orchestrate subordinate services. Product An outcome generated by the business to be offered to
customers. Products include materials and/or services. Requirement A quantitative statement of business need that must be met
by a particular architecture or work package. Role The usual or expected behavior of an actor, or the part somebody or
something plays in a particular process or event. An actor may have a
number of roles. See also Actor . Service Quality A configuration of non-functional requirements or
attributes that may be assigned to a business, application, or
technology service. Technology Service A technical capability required to provide enabling
infrastructure that supports the delivery of applications. Value Stream A representation of an end-to-end collection of
activities that create an overall result for a customer, stakeholder, or
end-user. Work Package A set of actions identified to achieve one or more
objectives for the business. A work package can be a part of a project,
a complete project, or a program.

</details>

<a id="tag_02_05"></a>
## 2.5. TOGAF Enterprise Metamodel Attributes

概念：表2-2列出元模型实体的典型属性。

适用条件：设计记录字段与查询分析。

逻辑关系：属性附属于实体类型，需结合具体企业事实。

决策方法：按用途选择字段并保留未知与来源。

制品及证据：属性定义及取值证据。

适用边界：typical不等于全部强制字段；补空值不能伪造真实事实。

来源块：C220-web-2025:05-architecture-content:b00115, C220-web-2025:05-architecture-content:b00116, C220-web-2025:05-architecture-content:b00117

<details><summary>展开本节完整英文来源</summary>

2.5. TOGAF Enterprise Metamodel Attributes

Table 2-2 shows typical attributes for each of the metamodel entities described previously.

Table 2-2:  TOGAF Enterprise Metamodel Attributes Metamodel Entity Attribute Description All Metamodel Entities ID Unique identifier for the architecture entity. Description Textual description of the architecture entity. Category User-definable categorization taxonomy for each metamodel
entity. Source Location from where the information was collected. Owner Owner of the architecture entity. Capability Business value Describes how this capability provides value to the enterprise. Increments Lists possible maturity/quality levels for the capability. Constraint No additional attributes This metamodel entity has only basic attributes. Gap No additional attributes This metamodel entity has only basic attributes. Location Category The following categories of Location apply: Region
(applies to a grouping of countries or territory; e.g., South East Asia,
UK, and Ireland), Country (applies to a single country; e.g., US),
Building (applies to a site of operation; where several offices are
collected in a single city, this category may represent a city), and
Specific Location (applies to any specific location within a building,
such as a server room). The nature of the business may introduce other
Locations: Ship or Port for a ferry company, Mine for a gold company,
Car for a police force, Hotel for any firm’s traveling workers, and so
on. Principle Category The following categories of principle apply:
Guiding Principle, Business Principle, Data Principle, Application
Principle, Integration Principle, Technology Principle. Priority Priority of this principle relative to other principles. Statement of principle Statement of what the principle is. Rationale Statement of why the principle is required and the
desired outcome to be reached. Implication Statement of what the principle means in practical
terms. Metric Identifies mechanisms that will be used to measure whether
the principle has been met or not. Requirement Statement of requirement Statement of what the
requirement is, including a definition of whether the requirement shall
be met, should be met, or may be met. Rationale Statement of why the requirement exists. Acceptance criteria The parameters that will be fulfilled if the requirement is being met, together with the tests that will be carried out to assess the state of the parameters. Actor # FTEs Estimated number of FTEs that operate as this actor. Actor goal Objectives that this actor has, in general terms. Actor tasks Tasks that this actor performs, in general terms. Business Service Standards class Non-Standard, Proposed Standard, Provisional Standard, Standard, Phasing-Out Standard, Retired Standard. Standard creation date If the business service is a standard, when
the standard was created. Last standard review date Last date that the standard was reviewed. Next standard review date Next date for the standard to be
reviewed. Retire date Date when the standard was/will be retired. Contract Behavior characteristics Functional behavior to be supported
within the scope of the contract. Service name “caller” Consuming service. Service name “called” Providing service. Service quality characteristics Non-functional behavior to be
supported within the scope of the contract. Availability characteristics Degree to which something is available
for use. Service times Hours during which the service must be available. Manageability characteristics Ability to gather information about
the state of something and control it. Serviceability characteristics Ability to identify problems and
take corrective action, such as to repair or upgrade a component in a
running system. Performance characteristics Ability of a component to perform its tasks in an appropriate time. Response requirements Response times that the service provider must
meet for particular operations. Reliability characteristics Resistance to failure. Quality of information required Contracted requirements on accuracy
and completeness of information. Contract control requirements Level of governance and enforcement
applied to the contractual parameters for overall service. Result control requirements Measures in place to ensure that each service request meets contracted criteria. Recoverability characteristics Ability to restore a system to a
working state after an interruption. Locatability characteristics Ability of a system to be found when needed. Security characteristics Ability of a system to prevent
unauthorized access to functions and data.
(continued) Privacy characteristics Protection of data from unauthorized access. Integrity characteristics Ability of a system to ensure that data
has not been corrupted. Credibility characteristics Ability of a system to ensure that the service request originates from an authorized source. Localization characteristics Ability of a service to support
localized variants for different consumer groups. Internationalization characteristics Ability of a service to support international variations in business logic and data representation (such as character set). Interoperability characteristics Ability of the service to
interoperate with different technical environments, inside and outside of the organization. Scalability characteristics Ability of the service to grow or
shrink its performance or capacity appropriately to the demands of the
environment in which it operates. Portability characteristics Of data, people, applications, and
components. Extensibility characteristics Ability to accept new functionality. Capacity characteristics Contracted capacity of the service
provider to meet requests. Throughput Required throughput capacity. Throughput period Time period needed to deliver throughput
capacity. Growth Expected future growth rate of service request. Growth period Time period needed to reach the expected growth rate. Peak profile short term Short-term profile of peak service traffic. Peak profile long term Long-term profile of peak service traffic. Control No additional attributes This metamodel entity has only basic
attributes. Driver No additional attributes This metamodel entity has only basic attributes. Event No additional attributes This metamodel entity has only basic attributes. Function Standards class Non-Standard, Proposed Standard, Provisional Standard, Standard, Phasing-Out Standard, Retired Standard. Standard creation date If the product is a standard, when the
standard was created. Last standard review date Last date that the standard was reviewed. Next standard review date Next date for the standard to be
reviewed. Retire date Date when the standard was/will be retired. Goal No additional attributes This metamodel entity has only basic attributes. Measure No additional attributes This metamodel entity has only basic attributes. Objective No additional attributes This metamodel entity has only basic attributes. Organization Unit Headcount Number of FTEs working within the
organization. Process Standards class Non-Standard, Proposed Standard, Provisional Standard, Standard, Phasing-Out Standard, Retired Standard. Standard creation date If the product is a standard, when the
standard was created. Last standard review date Last date that the standard was reviewed. Next standard review date Next date for the standard to be
reviewed. Retire date Date when the standard was/will be retired. Process criticality Criticality of this process to business
operations. Manual or automated Whether this process is supported by IT or is a
manual process. Process volumetrics Data on frequency of process execution. Product No additional attributes This metamodel entity has only basic
attributes. Role Estimated number of FTEs that operate in this Role This
metamodel entity has only basic attributes. Service Quality No additional attributes This metamodel entity fulfills some or all of
the attributes of its associated Contract(s). Service Standards class Non-Standard, Proposed Standard, Provisional Standard, Standard, Phasing-Out Standard, Retired Standard. Standard creation date If the product is a standard, when the
standard was created. Last standard review date Last date that the standard was reviewed. Next standard review date Next date for the standard to be
reviewed. Retire date Date when the standard was/will be retired. Application Component Standards class Non-Standard, Proposed
Standard, Provisional Standard, Standard, Phasing-Out Standard, Retired Standard. Standard creation date If the product is a standard, when the
standard was created. Last standard review date Last date that the standard was reviewed. Next standard review date Next date for the standard to be
reviewed. Retire date Date when the standard was/will be retired. Application Service Standards class Non-Standard, Proposed Standard, Provisional Standard, Standard, Phasing-Out Standard, Retired Standard. Standard creation date If the product is a standard, when the
standard was created. Last standard review date Last date that the standard was reviewed. Next standard review date Next date for the standard to be
reviewed. Retire date Date when the standard was/will be retired. Logical Application Component Standards class Non-Standard, Proposed Standard, Provisional
Standard, Standard, Phasing-Out Standard, Retired Standard. Standard creation date If the product is a standard, when the
standard was created. Last standard review date Last date that the standard was reviewed. Next standard review date Next date for the standard to be
reviewed. Retire date Date when the standard was/will be retired. Physical Application Component Lifecycle status Proposed, In Development, Live, Phasing Out, Retired. Standards class Non-Standard, Proposed Standard, Provisional
Standard, Standard, Phasing-Out Standard, Retired Standard. Standard creation date If the product is a standard, when the
standard was created. Last standard review date Last date that the standard was reviewed. Next standard review date Next date for the standard to be
reviewed. Retire date Date when the standard was/will be retired. Initial live date Date when the first release of the application
was/will be released into production. Date of last release Date when the last release of the application
was released into production. Date of next release Date when the next release of the application
will be released into production. Retirement date Date when the application was/will be retired. Availability characteristics Degree to which something is available for use. Service times Hours during which the application must be available. Manageability characteristics Ability to gather information about
the state of something and control it. Serviceability characteristics Ability to identify problems and
take corrective action, such as to repair or upgrade a component in a
running system. Performance characteristics Ability of a component to perform its tasks in an appropriate time. Reliability characteristics Resistance to failure. Recoverability characteristics Ability to restore a system to a
working state after an interruption. Locatability characteristics Ability of a system to be found when
needed.
(continued) Security characteristics Ability of a system to prevent unauthorized access to functions and data. Privacy characteristics Protection of data from unauthorized
access. Integrity characteristics Ability of a system to ensure that data
has not been corrupted. Credibility characteristics Ability of a system to ensure that the service request originates from an authorized source. Localization characteristics Ability of a service to support
localized variants for different consumer groups. Internationalization characteristics Ability of a service to
support international variations in business logic and data
representation (such as character set). Interoperability characteristics Ability of the service to
interoperate with different technical environments, inside and outside
of the organization. Scalability characteristics Ability of the service to grow or
shrink its performance or capacity appropriately to the demands of the
environment in which it operates. Portability characteristics Of data, people, applications, and
components. Extensibility characteristics Ability to accept new functionality. Capacity characteristics Contracted capacity of the service
provider to meet requests. Throughput Required throughput capacity. Throughput period Time period needed to deliver throughput
capacity. Growth Expected future growth rate of service request. Growth period Time period needed to reach the expected growth rate. Peak profile short term Short-term profile of peak service traffic. Peak profile long term Long-term profile of peak service traffic. Data Entity Category The following categories of data entity apply: Message, Internally Stored Entity. Privacy classification Level of restriction placed on access to the
data. Retention classification Level of retention to be placed on the
data. Logical Data Component Standards class Non-Standard, Proposed Standard, Provisional
Standard, Standard, Phasing-Out Standard, Retired Standard. Standard creation date If the product is a standard, when the
standard was created. Last standard review date Last date that the standard was reviewed. Next standard review date Next date for the standard to be
reviewed. Retire date Date when the standard was/will be retired. Physical Data Component Standards class Non-Standard, Proposed Standard, Provisional
Standard, Standard, Phasing-Out Standard, Retired Standard. Standard creation date If the product is a standard, when the
standard was created. Last standard review date Last date that the standard was reviewed. Next standard review date Next date for the standard to be
reviewed. Retire date Date when the standard was/will be retired. Logical Technology Component Standards class Non-Standard, Proposed Standard, Provisional
Standard, Standard, Phasing-Out Standard, Retired Standard. Standard creation date If the product is a standard, when the
standard was created. Last standard review date Last date that the standard was reviewed. Next standard review date Next date for the standard to be
reviewed. Retire date Date when the standard was/will be retired. Category Logical Technology Components are categorized according to the defined taxonomy (such as the TOGAF Technical Reference Model
(TRM)), adapted to meet the needs of an individual organization. Physical Technology Component Standards class Non-Standard, Proposed Standard, Provisional Standard, Standard, Phasing-Out Standard, Retired Standard. Standard creation date If the product is a standard, when the
standard was created. Last standard review date Last date that the standard was reviewed. Next standard review date Next date for the standard to be
reviewed. Retire date Date when the standard was/will be retired. Category Physical Technology Components are categorized according
to the defined taxonomy (such as the TOGAF TRM), adapted to meet the
needs of an individual organization. Product name Name of the product making up the technology
component. Module name Module, or other sub-product, name making up the
technology component. Vendor Vendor providing the technology component. Version Version of the product making up the technology component. Technology Service Standards class Non-Standard, Proposed Standard, Provisional Standard, Standard, Phasing-Out Standard, Retired Standard. Category Technology Services are categorized according to the
defined taxonomy (such as the TOGAF TRM), adapted to meet the needs of
an individual organization. Business Capability No additional attributes This metamodel entity
has only basic attributes. Technology Component Standards class Non-Standard, Proposed Standard,
Provisional Standard, Standard, Phasing-Out Standard, Retired Standard. Course of Action No additional attributes This metamodel entity has
only basic attributes. Value Stream No additional attributes This metamodel entity has only basic attributes. Work Package Category The following categories of work package apply: Work Package, Work Stream, Project, Program, Portfolio. Capability delivered Describes the contribution this work package
makes to capability delivery.

</details>

<a id="tag_02_06"></a>
## 2.6. TOGAF Enterprise Metamodel Relationships

概念：表2-3给出元模型关系。

适用条件：连接实体并追溯架构内容。

逻辑关系：类型、端点和关系谓词应保持表中语义。

决策方法：逐关系核对定义及适用端点。

制品及证据：关系清单与表2-3来源。

适用边界：不得把无说明连线变为顺序、权限或任意基数。

来源块：C220-web-2025:05-architecture-content:b00118, C220-web-2025:05-architecture-content:b00119, C220-web-2025:05-architecture-content:b00120

<details><summary>展开本节完整英文来源</summary>

2.6. TOGAF Enterprise Metamodel Relationships

Table 2-3 presents the TOGAF Enterprise Metamodel Relationships.

Table 2-3:  TOGAF Enterprise Metamodel Relationships Source Entity Target Entity Name Actor Actor Decomposes Actor Business Service Consumes Actor Data Entity Supplies or consumes Actor Event Generates Actor Event Resolves Actor Function Interacts with Actor Function Performs Actor Organization Unit Belongs to Actor Process Participates in Actor Process Triggers Actor Role Performs task in Actor Value Stream Performs a task in Application Service Business Service Automates some or all of Application Service Data Entity Used by Application Service Logical Application Component Is realized through Application Service Technology Service Is served by Business Capability Business Information Uses Business Capability Course of Action Is influenced by Business Capability Function Is delivered by Business Capability Organization Unit Is used by Business Capability Process Is operationalized by Business Capability Value Stream Enables Business Information Business Capability Is used by Business Information Business Service Used to derive Business Information Course of Action Is influenced by Business Information Data Entity Is realized by Business Information Process Uses Business Service Actor Is provided to Business Service Application Service Uses Business Service Business Information Is derived from Business Service Business Service Quality Meets Business Service Business Service Consumes Business Service Business Service Decomposes Business Service Contract Is governed and measured by Business Service Data Entity Is accessed and updated through Business Service Event Resolves Business Service Function Provides governed interface to access Business Service Logical Technology Component Is implemented on Business Service Organization Unit Is owned and governed by Business Service Process Is realized by Business Service Process Supports Capability Work Package Is delivered by Contract Business Service Governs, measures Contract Service Quality Meets Control Process Ensures correct operation of Course of Action Business Capability Influences Course of Action Business Information Influences Course of Action Function Influences Course of Action Goal Realizes Course of Action Organization Unit Influences Course of Action Product Influences Course of Action Value Stream Influences Data Entity Actor Is supplied or consumed by Data Entity Application Service Used by Data Entity Business Information Realizes Data Entity Business Service Is accessed and updated through Data Entity Data Entity Decomposes Data Entity Data Entity Relates to Data Entity Logical Data Component Resides within Driver Driver Decomposes Driver Goal Creates Driver Organization Unit Motivates Event Actor Is generated by Event Actor Is resolved by Event Business Service Is resolved by Event Process Is generated by Event Process Is resolved by Function Actor Supports Function Business Capability Delivers Function Business Service Is bounded by Function Course of Action Is influenced by Function Function Communicates with Function Function Decomposes Function Organization Unit Is owned by Function Process Orchestrates Function Process Decomposes Goal Course of Action Is realized by Goal Driver Addresses Goal Goal Decomposes Goal Objective Is made specific Logical Application Component Application Service Implements Logical Application Component Logical Application Component Decomposes Logical Application Component Logical Application Component Communicates with Logical Application Component Logical Data Component Used by Logical Application Component Logical Technology Component Is served
by Logical Application Component Physical Application Component Is
realized by Logical Data Component Data Entity Encapsulates Logical Data Component Logical Application Component Uses Logical Data Component Physical Data Component Is realized by Logical Technology Component Business Service Provides platform for Logical Technology Component Logical Application Component Serves Logical Technology Component Logical Technology Component Decomposes Logical Technology Component Logical Technology Component Is
dependent on Logical Technology Component Physical Technology Component Is
realized by Logical Technology Component Technology Service Supplies Measure Measure Decomposes Measure Objective Sets performance criteria for Objective Goal Realizes Objective Measure Is tracked against Objective Objective Decomposes Organization Unit Actor Contains Organization Unit Business Capability Delivers Organization Unit Business Service Owns and governs Organization Unit Course of Action Participates in Organization Unit Driver Is motivated by Organization Unit Function Enables Organization Unit Organization Unit Decomposes Organization Unit Product Delivers Physical Application Component Logical Application Component Realizes Physical Application Component Physical Application Component Decomposes Physical Application Component Physical Application Component Communicates with Physical Application Component Physical Data Component Used by Physical Application Component Physical Technology Component Is
served by Physical Data Component Logical Data Component Realizes Physical Data Component Physical Application Component Used by Physical Data Component Physical Data Component Decomposes Physical Technology Component Logical Technology Component Realizes Physical Technology Component Physical Application Component Serves Physical Technology Component Physical Technology Component Decomposes Physical Technology Component Physical Technology Component Is
dependent on Process Actor Is produced by Process Actor Supports Process Business Capability Operationalizes Process Business Information Is used by Process Business Service Orchestrates Process Business Service Decomposes Process Control Is guided by Process Event Generates Process Event Resolves Process Function Supports Process Function Is realized by Process Process Decomposes Process Process Precedes, follows Process Product Delivers Process Role Involves Process Role Is performed by Process Value Stream Operationalizes Product Course of Action Is produced by Product Organization Unit Is produced by Product Process Is produced by Role Actor Is performed by Role Process Participates in Role Process Performs Role Role Decomposes Service Quality Contract Applies to Service Quality Service Applies to Technology Service Application Service Serves Technology Service Logical Technology Component Is supplied by Value Stream Actor Involves Value Stream Actor Is triggered by Value Stream Business Capability Is enabled by Value Stream Course of Action Is influenced by Value Stream Process Is operationalized by Work Package Capability Delivers

</details>

<a id="chap03"></a>
## 3. Architectural Artifacts

概念：本章先定义制品概念，再按ADM阶段描述推荐成果。

适用条件：准备制品选择与表达。

逻辑关系：概念基础支持后续目录、矩阵和图。

决策方法：先确定关切和表达需要，再选择推荐制品。

制品及证据：制品选择记录。

适用边界：推荐集合不自动变成项目必交清单。

来源块：C220-web-2025:05-architecture-content:b00121, C220-web-2025:05-architecture-content:b00122

<details><summary>展开本节完整英文来源</summary>

3. Architectural Artifacts

This chapter discusses the concepts surrounding architecture artifacts and then describes the artifacts that are recommended to be created for each phase within the ADM.

</details>

<a id="tag_03_01"></a>
## 3.1. Basic Concepts

概念：架构描述表达架构；视图含模型选定部分并回应关切；视点定义构造解释与使用约定。

适用条件：面向系统、方案或企业状态表达架构。

逻辑关系：利益相关者→关切→视点/模型种类→视图/模型；通用视点可复用，视图始终针对具体架构。

决策方法：明确相关者和关切，区分具体内容与表达约定。

制品及证据：视点定义、模型及具体视图、关切到需求映射。

适用边界：视图不等于架构全貌；关切可能导出多个需求；ISO定义为本卷适配表达。

来源块：C220-web-2025:05-architecture-content:b00123, C220-web-2025:05-architecture-content:b00124, C220-web-2025:05-architecture-content:b00125, C220-web-2025:05-architecture-content:b00126, C220-web-2025:05-architecture-content:b00127, C220-web-2025:05-architecture-content:b00128, C220-web-2025:05-architecture-content:b00129, C220-web-2025:05-architecture-content:b00130, C220-web-2025:05-architecture-content:b00131, C220-web-2025:05-architecture-content:b00132, C220-web-2025:05-architecture-content:b00133, C220-web-2025:05-architecture-content:b00134, C220-web-2025:05-architecture-content:b00135, C220-web-2025:05-architecture-content:b00136, C220-web-2025:05-architecture-content:b00137, C220-web-2025:05-architecture-content:b00138, C220-web-2025:05-architecture-content:b00139, C220-web-2025:05-architecture-content:b00140, C220-web-2025:05-architecture-content:b00141, C220-web-2025:05-architecture-content:b00142

<details><summary>展开本节完整英文来源</summary>

3.1. Basic Concepts

Architectural artifacts are created in order to describe a system, solution, or state of the enterprise. The concepts discussed in this section have been adapted from more formal definitions contained in
ISO/IEC/IEEE 42010:2022 and ISO/IEC/IEEE 15288:2015. They are
illustrated in Figure 3-1 .

The “environment” of a system is the context determining the setting and circumstances of all influences upon a system. The environment of a system includes developmental, technological, business, operational,
organizational, political, economic, legal, regulatory, ecological, and social influences.

A “system” is a combination of interacting elements organized to achieve
one or more stated purposes.

The “architecture” of a system is the fundamental concepts or properties of a system in its environment embodied in its elements, relationships,
and in the principles of its design and evolution.

An “Architecture Description” is a work product used to express an architecture; a collection of architecture views and models that
together document the architecture.

“Stakeholders” are individuals, teams, organizations, or classes thereof, having an interest in a system.

“Concerns” are interests in a system relevant to one or more of its stakeholders. Concerns may pertain to any aspect of the system’s functioning, development, or operation, including considerations such as
performance, reliability, security, distribution, and evolvability and may determine the acceptability of the system.

An “architecture view” is a representation of a system from the
perspective of a related set of concerns. It consists of one or more architecture models of the system.

An “Architecture Model” is a representation of a subject of interest. A
model provides a smaller scale, simplified, and/or abstract
representation of the subject matter.

In capturing or representing the design of a system architecture, the architect will typically create one or more architecture models, possibly using different tools. An architecture view will comprise selected parts of one or more models, chosen so as to demonstrate to a particular stakeholder or group of stakeholders that their concerns are being adequately addressed in the design of the system architecture.



Figure 3-1: Basic Architectural Concepts

An “architecture viewpoint” is a specification of the conventions for a particular kind of architecture view. It can also be called the definition or schema for that kind of architecture view. It establishes the conventions for constructing, interpreting, and using an
architecture view to address a specific concern (or set of concerns) about a system-of-interest.

A “Model Kind” establishes conventions for a type of modeling.

An architecture viewpoint references one or more model kinds; an architecture view incorporates one or more models.

A “viewpoint library” is a collection of the specifications of
architecture viewpoints contained in the Reference Library portion of
the Architecture Repository.

An architecture view is what you see; an architecture viewpoint is
where you are looking from — the vantage point or perspective that
determines what you see Architecture viewpoints are generic, and can be stored in libraries for re-use; an architecture view is always specific to the architecture
for which it is created Every architecture view has an associated architecture viewpoint that describes it, at least implicitly ISO/IEC/IEEE 42010:2022 encourages architects to define architecture
viewpoints explicitly. Making this distinction between the content and
schema of a view may seem at first to be an unnecessary overhead, but it provides a mechanism for re-using architecture viewpoints across different architectures.

In summary, then, architecture views are representations of the overall architecture in terms meaningful to stakeholders. They enable the architecture to be communicated to and understood by the stakeholders, so they can verify that the system will address their concerns.

Concerns are often related to requirements. A concern can be a general requirement type, such as availability. It may lead to the definition of several particular requirements. It may be an interest related to some
goal of a stakeholder. Identifying concerns helps ensure stakeholders'
interests are addressed and requirements are identified. Associating concerns with general artifact types helps architects to select and develop particular artifacts for presentation to stakeholders.

</details>

<a id="tag_03_01_01"></a>
## 3.1.1. Simple Example of an Architecture Viewpoint and Architecture View

概念：表3-1定义业务域视点，图3-2给出对应2017年视图。

适用条件：理解同一视点怎样产生具体视图。

逻辑关系：外框地点、内框业务职能，嵌套表示职能在地点执行。

决策方法：先读取利益相关者、关切与嵌套语义，再读示例。

制品及证据：视点模板与2017年具体视图。

适用边界：示例年份和组织不代表当前状态，嵌套不表示组织汇报。

来源块：C220-web-2025:05-architecture-content:b00143, C220-web-2025:05-architecture-content:b00144, C220-web-2025:05-architecture-content:b00145, C220-web-2025:05-architecture-content:b00146, C220-web-2025:05-architecture-content:b00147, C220-web-2025:05-architecture-content:b00148, C220-web-2025:05-architecture-content:b00149

<details><summary>展开本节完整英文来源</summary>

3.1.1. Simple Example of an Architecture Viewpoint and Architecture View

For many architectures, a useful architecture viewpoint is that of
business domains, which can be illustrated by an example from The Open Group itself.

The architecture viewpoint is specified as shown in Table 3-1 .

Table 3-1:  Architecture Viewpoint Example Architecture Viewpoint Element Description Stakeholders Management Board, Chief Executive Officer Concerns Show the top-level relationships between US/UK geographical
sites and business functions. Modeling technique Nested boxes diagram. Outer boxes = locations; inner boxes = business functions. Semantics of nesting = functions performed in the locations.

The corresponding architecture view of The Open Group (in 2017) is shown
in Figure 3-2 .



Figure 3-2: Example Architecture View — The Open Group Business Domains

</details>

<a id="tag_03_02"></a>
## 3.2. Developing Architecture Views in the ADM

概念：ADM中视图开发的分组标题。

适用边界：具体指导在子节，无独立过程。

来源块：C220-web-2025:05-architecture-content:b00150

<details><summary>展开本节完整英文来源</summary>

3.2. Developing Architecture Views in the ADM

</details>

<a id="tag_03_02_01"></a>
## 3.2.1. General Guidelines

概念：视图需同时适合目的并完整回应相关关切，且视图间完整一致。

适用条件：选择和迭代基线/目标视图。

逻辑关系：业务到技术、高层到细节的进展持续回到关切；B/C/D两状态视图支持差距分析。

决策方法：在实用边界内检验关切覆盖、冲突协调和权衡。

制品及证据：基线/目标视图、关切覆盖与权衡记录。

适用边界：适合目的后应止于所需细节，不无限学术迭代。

来源块：C220-web-2025:05-architecture-content:b00151, C220-web-2025:05-architecture-content:b00152, C220-web-2025:05-architecture-content:b00153, C220-web-2025:05-architecture-content:b00154, C220-web-2025:05-architecture-content:b00155, C220-web-2025:05-architecture-content:b00156, C220-web-2025:05-architecture-content:b00157

<details><summary>展开本节完整英文来源</summary>

3.2.1. General Guidelines

The choice of which particular architecture views to develop is one of the key decisions that the architect has to make.

The architect has a responsibility for ensuring the completeness
(fitness-for-purpose) of the architecture, in terms of adequately addressing all the pertinent concerns of its stakeholders; and the integrity of the architecture, in terms of connecting all the various
views to each other, satisfactorily reconciling the conflicting concerns
of different stakeholders, and showing the trade-offs made in so doing (as between security and performance, for example).

The choice has to be constrained by considerations of practicality, and by the principle of fitness-for-purpose (i.e., the architecture should be developed only to the point at which it is fit-for-purpose, and not
reiterated ad infinitum as an academic exercise).

As explained in the TOGAF Standard — Architecture Development Method , the development of architecture views is an iterative process. The typical progression is from business to technology, using a technique such as business scenarios (see the TOGAF ® Series Guide: Business Scenarios ) to properly identify all pertinent concerns; and from high-level overview to lower-level detail, continually referring back to the concerns and requirements of the stakeholders throughout the process.

Moreover, each of these progressions has to be made for two distinct environments: the existing environment (referred to as the baseline in the ADM) and the target environment. The architect must develop pertinent architecture views of both the Baseline Architecture and the Target Architecture. This provides the context for the gap analysis at the end of Phases B, C, and D of the ADM, which establishes the elements of the Baseline Architecture to be carried forward and the elements to be added, removed, or replaced.

This whole process is explained in the TOGAF Standard — ADM Techniques .

</details>

<a id="tag_03_02_02"></a>
## 3.2.2. Architecture View Creation Process

概念：有视点库可选模板生成视图；缺合适视点时可新建或先做临时视图再抽象。

适用条件：采用或尚未采用ISO42010的组织。

逻辑关系：每个视图至少隐含视点；系统化显式定义便于检验关切覆盖。

决策方法：查库、按关切选择；没有适用模板时记录新视点或临时约定。

制品及证据：视点选择依据、生成视图及可复用定义。

适用边界：TOGAF鼓励而不强制ISO42010；所列过程不是该标准强制程序。

来源块：C220-web-2025:05-architecture-content:b00158, C220-web-2025:05-architecture-content:b00159, C220-web-2025:05-architecture-content:b00160, C220-web-2025:05-architecture-content:b00161, C220-web-2025:05-architecture-content:b00162, C220-web-2025:05-architecture-content:b00163, C220-web-2025:05-architecture-content:b00164, C220-web-2025:05-architecture-content:b00165, C220-web-2025:05-architecture-content:b00166

<details><summary>展开本节完整英文来源</summary>

3.2.2. Architecture View Creation Process

As mentioned above, the TOGAF framework encourages but does not mandate the use of ISO/IEC/IEEE 42010:2022. The following description therefore covers both the situation where ISO/IEC/IEEE 42010:2022 has been adopted
and where it has not.

ISO/IEC/IEEE 42010:2022 itself does not require any specific process for developing architecture viewpoints or creating views from them. Where
ISO/IEC/IEEE 42010:2022 has been adopted and become well-established
practice within an organization, it will often be possible to create the required views for a particular architecture by following these steps:

Refer to an existing library of architecture viewpoints Select the appropriate architecture viewpoints (based on the
stakeholders and concerns that need to be covered by views) Generate views of the system by using the selected architecture
viewpoints as templates

This approach can be expected to bring the following benefits:

Less work for the architects (the architecture viewpoints have
already been defined and therefore the views can be created faster) Better comprehensibility for stakeholders (the architecture
viewpoints are already familiar) Greater confidence in the validity of the views (their
architecture viewpoints have a known track record)

However, situations can always arise in which an architecture view is needed for which no appropriate architecture viewpoint has been predefined. This is also the situation, of course, when an organization has not yet incorporated ISO/IEC/IEEE 42010:2022 into its architecture
practice and established a library of architecture viewpoints.

In each case, the architect may choose to develop a new architecture viewpoint that will cover the outstanding need, and then generate an architecture view from it. (This is ISO/IEC/IEEE 42010:2022 recommended practice.) Alternatively, a more pragmatic approach can be equally successful: the architect can create an ad hoc architecture view for a specific system and later consider whether a generalized form of the
implicit architecture viewpoint should be defined explicitly and saved in a library, so that it can be re-used. (This is one way of
establishing a library of architecture viewpoints initially.)

Whatever the context, the architect should be aware that every architecture view has an architecture viewpoint, at least implicitly, and that defining the architecture viewpoint in a systematic way (as recommended by ISO/IEC/IEEE 42010:2022) will help in assessing its effectiveness; i.e., does the architecture viewpoint cover the relevant
stakeholder concerns?

</details>

<a id="tag_03_03"></a>
## 3.3. Views, Tools, and Languages

概念：本节讨论视图、工具及支持互操作的共同语言。

适用条件：需要多工具开发与分析。

逻辑关系：表达语义、工具和视图不能相互替代。

决策方法：检查共同语言及工具交换需求。

制品及证据：工具与语言约定。

适用边界：本分组未指定具体工具。

来源块：C220-web-2025:05-architecture-content:b00167, C220-web-2025:05-architecture-content:b00168

<details><summary>展开本节完整英文来源</summary>

3.3. Views, Tools, and Languages

The need for architecture views, and the process of developing them
following the ADM, is explained above. This section describes the
relationships between architecture views, the tools used to develop and analyze them, and a standard language enabling interoperability between the tools.

</details>

<a id="tag_03_03_01"></a>
## 3.3.1. Overview

概念：不同视图常用不同工具，标准语言和标准视点有利语义复用和工具互操作。

适用条件：开发、沟通及管理架构描述。

逻辑关系：视点模板/模式与内容语言均需支持交换。

决策方法：按所需语义评估工具，并保持模型可共享。

制品及证据：语言编码、视点及工具评估。

适用边界：市场状态是源文描述，不能当作当前工具能力调查。

来源块：C220-web-2025:05-architecture-content:b00169, C220-web-2025:05-architecture-content:b00170, C220-web-2025:05-architecture-content:b00171, C220-web-2025:05-architecture-content:b00172, C220-web-2025:05-architecture-content:b00173

<details><summary>展开本节完整英文来源</summary>

3.3.1. Overview

In order to achieve the goals of completeness and integrity in an
architecture, architecture views are usually developed, visualized,
communicated, and managed using a tool.

In the current state of the market, different tools normally have to be used to develop and analyze different views of the architecture. It is highly desirable that an Architecture Description be encoded in a
standard language, to enable a standard approach to the description of architecture semantics and their re-use among different tools.

An architecture viewpoint is also normally developed, visualized,
communicated, and managed using a tool, and it is also highly desirable that standard architecture viewpoints (i.e., templates or schemas) be
developed, so that different tools that deal in the same views can
interoperate, the fundamental elements of an architecture can be
re-used, and the Architecture Description can be shared among tools.

Issues relating to the evaluation of tools for architecture work are
discussed in detail in the TOGAF Standard — Architecture Development Method .

</details>

<a id="tag_03_04"></a>
## 3.4. Architecture Views and Architecture Viewpoints

概念：视图与视点示例的分组标题。

适用边界：例子展开在子节。

来源块：C220-web-2025:05-architecture-content:b00174

<details><summary>展开本节完整英文来源</summary>

3.4. Architecture Views and Architecture Viewpoints

</details>

<a id="tag_03_04_01"></a>
## 3.4.1. Example of Architecture Views and Architecture Viewpoints

概念：飞行员与空管各有不同关切、抽象模型和专用工具，共享部分信息与无线通信语言。

适用条件：理解视点限制与视图协同。

逻辑关系：两视图各是系统子集；交集信息和共同语言支撑协作。

决策方法：识别共同及独有信息、所用工具和交换语义。

制品及证据：视点模型、关切集合及共享通信约定。

适用边界：航空示例不是企业角色权限或具体航空操作规范。

来源块：C220-web-2025:05-architecture-content:b00175, C220-web-2025:05-architecture-content:b00176, C220-web-2025:05-architecture-content:b00177, C220-web-2025:05-architecture-content:b00178, C220-web-2025:05-architecture-content:b00179, C220-web-2025:05-architecture-content:b00180, C220-web-2025:05-architecture-content:b00181, C220-web-2025:05-architecture-content:b00182, C220-web-2025:05-architecture-content:b00183, C220-web-2025:05-architecture-content:b00184, C220-web-2025:05-architecture-content:b00185, C220-web-2025:05-architecture-content:b00186, C220-web-2025:05-architecture-content:b00187

<details><summary>展开本节完整英文来源</summary>

3.4.1. Example of Architecture Views and Architecture Viewpoints

To illustrate the concepts of architecture views and architecture
viewpoints, consider the example of a very simple airport system with two different stakeholders: the pilot and the air traffic controller.

One architecture view can be developed from the architecture viewpoint of the pilot, which addresses the pilot’s concerns. Equally, another architecture view can be developed from the architecture viewpoint of
the air traffic controller. Neither architecture view completely describes the system in its entirety, because the architecture viewpoint of each stakeholder constrains (and reduces) how each sees the overall
system.

The architecture viewpoint of the pilot comprises some concerns that are not relevant to the controller, such as passengers and fuel, while the architecture viewpoint of the controller comprises some concerns not
relevant to the pilot, such as other planes. There are also elements shared between the two architecture viewpoints, such as the communication model between the pilot and the controller, and the vital information about the plane itself.

An architecture viewpoint is a model (or description) of the information contained in a view. In our example, one architecture viewpoint is the description of how the pilot sees the system, and the other architecture viewpoint is how the controller sees the system.

Pilots describe the system from their perspective, using a model of
their position and vector toward or away from the runway. All pilots use this model, and the model has a specific language that is used to capture information and populate the model.

Controllers describe the system differently, using a model of the
airspace and the locations and vectors of aircraft within the airspace. Again, all controllers use a common language derived from the common model in order to capture and communicate information pertinent to their
architecture viewpoint.

Fortunately, when controllers talk with pilots, they use a common
communication language. (In other words, the models representing their individual architecture viewpoints partially intersect.) Part of this common language is about location and vectors of aircraft, and is essential to safety.

So, in essence, each architecture viewpoint is an abstract model of how all the stakeholders of a particular type — all pilots, or all controllers — view the airport system.

Tools exist to assist stakeholders, especially when they are interacting with complex models such as the model of an airspace, or the model of
air flight.

The interface to the human user of a tool is typically close to the
model and language associated with the architecture viewpoint. The
unique tools of the pilot are fuel, altitude, speed, and location
indicators. The main tool of the controller is radar. The common tool is a radio.

To summarize from the above example, we can see that an architecture view can subset the system through the perspective of the stakeholder, such as the pilot versus the controller. This subset can be described by an abstract model called an architecture viewpoint, such as an air flight versus an air space model. This description of the architecture view is documented in a partially specialized language, such as “pilot-speak” versus “controller-speak”. Tools are used to assist the stakeholders, and they interface with each other in terms of the
language derived from the architecture viewpoint (“pilot-speak” versus “controller-speak”).

When stakeholders use common tools, such as the radio contact between
pilot and controller, a common language is essential.

</details>

<a id="tag_03_04_02"></a>
## 3.4.2. Architecture Views and Architecture Viewpoints in Enterprise Architecture

概念：用户与开发者的EA视点关注不同内容，单一视图难以穷尽系统。

适用条件：描述用户可用性与开发结构。

逻辑关系：用户关注可用性响应及访问；开发者关注工具、软件硬件等；共同过程/问题沟通连接二者。

决策方法：辨别共享信息并处理不同开发专业的语言差异。

制品及证据：用户/开发视图及共享模型部分。

适用边界：例子不意味着真实开发者永远不关心运行数据或用户。

来源块：C220-web-2025:05-architecture-content:b00188, C220-web-2025:05-architecture-content:b00189, C220-web-2025:05-architecture-content:b00190, C220-web-2025:05-architecture-content:b00191, C220-web-2025:05-architecture-content:b00192, C220-web-2025:05-architecture-content:b00193, C220-web-2025:05-architecture-content:b00194, C220-web-2025:05-architecture-content:b00195

<details><summary>展开本节完整英文来源</summary>

3.4.2. Architecture Views and Architecture Viewpoints in Enterprise Architecture

Now let us map this example to the Enterprise Architecture. Consider two
stakeholders in a new small computing system: the users and the
developers.

The users of the system have an architecture viewpoint that reflects
their concerns when interacting with the system, and the developers of
the system have a different architecture viewpoint. Architecture views
that are developed to address either of the two architecture viewpoints
are unlikely to exhaustively describe the whole system, because each
perspective reduces how each sees the system.

The architecture viewpoint of the user is comprised of all the ways in
which the user interacts with the system, not seeing any details such as applications or Database Management Systems (DBMS).

The architecture viewpoint of the developer is one of productivity and
tools, and doesn’t include things such as actual live data and
connections with consumers.

However, there are things that are shared, such as descriptions of the
processes that are enabled by the system and/or communications protocols set up for users to communicate problems directly to development.

In this example, one architecture viewpoint is the description of how
the user sees the system, and the other architecture viewpoint is how
the developer sees the system. Users describe the system from their
perspective, using a model of availability, response time, and access to information. All users of the system use this model, and the model has a specific language.

Developers describe the system differently than users, using a model of software connected to hardware distributed over a network, etc. However, there are many types of developers (database, security, etc.) of the system, and they do not have a common language derived from the model.

</details>

<a id="tag_03_04_03"></a>
## 3.4.3. Need for a Common Language and Interoperable Tools for Architecture Description

概念：共同架构语言有助多工具把系统信息连为整体。

适用条件：用户与不同开发专业需协作。

逻辑关系：用户工具用用户语言，开发工具之间缺共同语言会阻碍交换。

决策方法：依语义与互操作需要评估工具。

制品及证据：共同语言及工具交换验证。

适用边界：原文市场困难判断并非本轮最新产品评测。

来源块：C220-web-2025:05-architecture-content:b00196, C220-web-2025:05-architecture-content:b00197, C220-web-2025:05-architecture-content:b00198

<details><summary>展开本节完整英文来源</summary>

3.4.3. Need for a Common Language and Interoperable Tools for Architecture Description

Tools exist for both users and developers. Tools such as online help are there specifically for users, and attempt to use the language of the user. Many different tools exist for different types of developers, but they suffer from the lack of a common language that is required to bring
the system together. It is difficult, if not impossible, in the current state of the tools market to have one tool interoperate with another
tool.

Issues relating to the evaluation of tools for architecture work are
discussed in detail in the TOGAF Standard — Architecture Development Method .

</details>

<a id="tag_03_05"></a>
## 3.5. Conclusions

概念：可行动视图需要确定关键相关者、理解并归纳关切、选择建模与处理方式。

适用条件：结构化地开发视图。

逻辑关系：关切与表达方法共同决定视图有效性。

决策方法：逐视图检验所选关切是否被模型回应。

制品及证据：相关者—关切—建模方式关联。

适用边界：本章不是视图理论的完整论述。

来源块：C220-web-2025:05-architecture-content:b00199, C220-web-2025:05-architecture-content:b00200, C220-web-2025:05-architecture-content:b00201, C220-web-2025:05-architecture-content:b00202

<details><summary>展开本节完整英文来源</summary>

3.5. Conclusions

This section attempts to deal with views in a structured manner, but
this is by no means a complete treatise on views.

In general, the TOGAF framework embraces the concepts and definitions presented in ISO/IEC/IEEE 42010:2022, specifically the concepts that help guide the development of an architecture view and make the architecture view actionable. These concepts can be summarized as:

Selecting a key stakeholder Understanding their concerns and generalizing/documenting those
concerns Understanding how to model and deal with those concerns

</details>

<a id="tag_03_06"></a>
## 3.6. Architectural Artifacts by ADM Phase

概念：按ADM阶段推荐制品的分组标题。

适用边界：阶段列表不新增固定输出义务。

来源块：C220-web-2025:05-architecture-content:b00203

<details><summary>展开本节完整英文来源</summary>

3.6. Architectural Artifacts by ADM Phase

</details>

<a id="tag_03_06_00_01"></a>
## 3.6.1. Catalog, Matrix, and Diagram Concept

概念：构建块是带元模型元数据的实体；目录列类型实例；矩阵表示关系；图表达内容。

适用条件：回答相关者的具体查询问题。

逻辑关系：模型支持目录/矩阵/图等投影，图还可帮助采集和完整性检查。

决策方法：按关切选实体和表示法，按需搜索过滤查询资料库。

制品及证据：共享构建块、元数据及查询产生的制品。

适用边界：按需查询不限于固定元模型制品清单；不同视图不应复制成分叉实体。

来源块：C220-web-2025:05-architecture-content:b00204, C220-web-2025:05-architecture-content:b00205, C220-web-2025:05-architecture-content:b00206, C220-web-2025:05-architecture-content:b00207, C220-web-2025:05-architecture-content:b00208, C220-web-2025:05-architecture-content:b00209, C220-web-2025:05-architecture-content:b00210, C220-web-2025:05-architecture-content:b00211, C220-web-2025:05-architecture-content:b00212, C220-web-2025:05-architecture-content:b00213, C220-web-2025:05-architecture-content:b00214, C220-web-2025:05-architecture-content:b00215, C220-web-2025:05-architecture-content:b00216, C220-web-2025:05-architecture-content:b00217

<details><summary>展开本节完整英文来源</summary>

3.6.1. Catalog, Matrix, and Diagram Concept

The Enterprise Metamodel is used as a technique to structure
architectural information in an ordered way so that it can be processed to meet the stakeholder needs. The majority of architecture stakeholders do not actually need to know what the architecture metamodel is and are
only concerned with specific issues, such as “what functionality does this application support?”, “which processes will be impacted by this project?”, etc. In order to meet the needs of these stakeholders, the TOGAF concepts of building blocks, catalogs, matrices, and diagrams are used.

Building blocks are entities of a particular type within the metamodel
(for example, a business service called “Purchase Order”). Building
blocks carry metadata according to the metamodel, which supports query
and analysis. For example, business services have a metadata attribute
for owner, which allows a stakeholder to query all business services owned by a particular organization. Building blocks may also include
dependent or contained entities as appropriate to the context of the
architecture (for example, a business service called “Purchase Order” may implicitly include a number of processes, data entities, application components, etc.).

Catalogs are lists of building blocks of a specific type, or of related types, that are used for governance or reference purposes (for example, an organization chart, showing locations and actors). As with building
blocks, catalogs carry metadata according to the metamodel, which
supports query and analysis.

Matrices are grids that show relationships between two or more model entities. Matrices are used to represent relationships that are
list-based rather than graphical in their usage (for example, a CRUD matrix showing which applications Create, Read, Update, and Delete a particular type of data is difficult to represent visually).

Diagrams are renderings of architectural content in a graphical format to allow stakeholders to retrieve the required information. Diagrams can
also be used as a technique for graphically populating architecture
content or for checking the completeness of information that has been collected. The TOGAF Content Framework defines a set of architecture diagrams to be created (e.g., organization chart). Each of these diagrams may be created several times for an architecture with different
style or content coverage to suit stakeholder concerns.

Building blocks, catalogs, matrices, and diagrams are all concepts that are well supported by leading Enterprise Architecture tools. In environments where tools are used to model the architecture, such tools
typically support mechanisms to search, filter, and query the
Architecture Repository.

On-demand querying of the Architecture Repository (such as the business service ownership example mentioned above) can be used to generate ad hoc catalogs, matrices, and diagrams of the architecture. As this type
of query is by nature required to be flexible, it is therefore not
restricted or defined within the Enterprise Metamodel.

The interactions between metamodel, building blocks, diagrams, and stakeholders are shown in Figure 3-3 . Figure 3-4 shows the artifacts that are associated
with the TOGAF Enterprise Metamodel.



Figure 3-3: Interactions between Metamodel, Building Blocks, Diagrams, and Stakeholders



Figure 3-4: Artifacts Associated with the Enterprise Metamodel

The recommended artifacts for production in each ADM phase are as
follows.

</details>

<a id="tag_03_06_01"></a>
## 3.6.2. Preliminary Phase

概念：预备阶段可创建的制品。

适用条件：执行预备阶段时。

逻辑关系：下一节给原则目录。

决策方法：按本组织需要确定采用范围。

制品及证据：所选预备制品。

适用边界：may be created不等于无条件必交。

来源块：C220-web-2025:05-architecture-content:b00218, C220-web-2025:05-architecture-content:b00219

<details><summary>展开本节完整英文来源</summary>

3.6.2. Preliminary Phase

The following describes catalogs, matrices, and diagrams that may be
created within the Preliminary Phase, as described in the TOGAF Standard — Architecture Development Method .

</details>

<a id="tag_03_06_01_01"></a>
## 3.6.2.1. Principles Catalog

概念：原则目录记录描述好方案/架构的业务及架构原则。

适用条件：架构决定点和变革治理。

逻辑关系：原则支持评估及对结果达成一致。

决策方法：按原则评价方案并记录同意或权衡。

制品及证据：Principle目录及决定记录。

适用边界：目录记录不能代替真实组织共识或批准。

来源块：C220-web-2025:05-architecture-content:b00220, C220-web-2025:05-architecture-content:b00221, C220-web-2025:05-architecture-content:b00222, C220-web-2025:05-architecture-content:b00223

<details><summary>展开本节完整英文来源</summary>

3.6.2.1. Principles Catalog

The Principles catalog captures principles of the Business and
Architecture Principles that describe what a “good” solution or
architecture should look like. Principles are used to evaluate and agree an outcome for architecture decision points. Principles are also used as a tool to assist in architectural governance of change initiatives.

The Principles catalog contains the following metamodel entities:

Principle

</details>

<a id="tag_03_06_02"></a>
## 3.6.3. Phase A: Architecture Vision

概念：A阶段可创建的愿景制品。

适用条件：架构愿景工作。

逻辑关系：高层定向与后续正式模型相衔接。

决策方法：按关切选制品。

制品及证据：A阶段选定制品。

适用边界：本节为推荐入口，不新增固定必交清单。

来源块：C220-web-2025:05-architecture-content:b00224, C220-web-2025:05-architecture-content:b00225

<details><summary>展开本节完整英文来源</summary>

3.6.3. Phase A: Architecture Vision

The following describes catalogs, matrices, and diagrams that may be
created within Phase A (Architecture Vision) as described in the TOGAF Standard — Architecture Development Method .

</details>

<a id="tag_03_06_02_01"></a>
## 3.6.3.1. Stakeholder Catalog

概念：利益相关者目录记录影响、问题和关切。

适用条件：架构参与及利益相关者映射。

逻辑关系：了解需求可聚焦工作；参与信息可能敏感且A阶段使用非正式建模。

决策方法：识别真实参与者和关切，控制敏感信息的表达。

制品及证据：利益相关者目录与参与地图。

适用边界：源文不指定生成目录的元模型实体；影响力不是自动批准权限。

来源块：C220-web-2025:05-architecture-content:b00226, C220-web-2025:05-architecture-content:b00227, C220-web-2025:05-architecture-content:b00228, C220-web-2025:05-architecture-content:b00229

<details><summary>展开本节完整英文来源</summary>

3.6.3.1. Stakeholder Catalog

The purpose of the Stakeholder catalog is to identify the stakeholders for the architecture engagement, their influence over the engagement, and their key questions, issues, or concerns that must be addressed by
the architecture framework.
The Stakeholder catalog is referenced in creating a stakeholder map, showing which stakeholders are involved with a specific aspect of the Enterprise Architecture, their level of involvement, and their key concerns.

Understanding stakeholders and their requirements allows an architect to focus effort in areas that meet the needs of stakeholders (see the TOGAF Standard — ADM Techniques ).

Due to the potentially sensitive nature of stakeholder mapping
information and the fact that the Architecture Vision phase is intended to be conducted using informal modeling techniques, no specific metamodel entities will be used to generate a Stakeholder catalog.

</details>

<a id="tag_03_06_02_02"></a>
## 3.6.3.2. Value Chain Diagram

概念：价值链图表达企业及外部交互的高层定向。

适用条件：快速使参与者理解变革上下文。

逻辑关系：着重沟通呈现，区别于B阶段较正式组织图。

决策方法：用适合高层沟通的职能/组织背景对齐理解。

制品及证据：高层价值链图。

适用边界：不能将价值链、价值流或组织结构视为同一对象。

来源块：C220-web-2025:05-architecture-content:b00230, C220-web-2025:05-architecture-content:b00231, C220-web-2025:05-architecture-content:b00232

<details><summary>展开本节完整英文来源</summary>

3.6.3.2. Value Chain Diagram

A Value Chain diagram provides a high-level orientation view of an
enterprise and how it interacts with the outside world. In contrast to the more formal organization map developed within Phase B (Business Architecture), the Value Chain diagram focuses on presentational impact.

The purpose of this diagram is to quickly on-board and align
stakeholders for a particular change initiative, so that all
participants understand the high-level functional and organizational
context of the architecture engagement.

</details>

<a id="tag_03_06_02_03"></a>
## 3.6.3.3. Solution Concept Diagram

概念：方案概念图是拟议方案的高层铅笔草图。

适用条件：参与工作初期对齐目标和预期方法。

逻辑关系：可包含目标需求约束并标需正式建模的后续工作。

决策方法：表达拟议方向并安排详细调查。

制品及证据：方案概念图及待调查区域。

适用边界：草图不证明方案已详细设计、择优或批准。

来源块：C220-web-2025:05-architecture-content:b00233, C220-web-2025:05-architecture-content:b00234, C220-web-2025:05-architecture-content:b00235, C220-web-2025:05-architecture-content:b00236

<details><summary>展开本节完整英文来源</summary>

3.6.3.3. Solution Concept Diagram

A Solution Concept diagram provides a high-level orientation of the solution that is envisaged in order to meet the objectives of the architecture engagement. In contrast to the more formal and detailed architecture diagrams developed in the following phases, the solution concept represents a “pencil sketch” of the expected solution at the outset of the engagement.

This diagram may embody key objectives, requirements, and constraints for the engagement and also highlight work areas to be investigated in more detail with formal architecture modeling.

Its purpose is to quickly on-board and align stakeholders for a
particular change initiative, so that all participants understand what the architecture engagement is seeking to achieve and how it is expected that a particular solution approach will meet the needs of the enterprise.

</details>

<a id="tag_03_06_02_04"></a>
## 3.6.3.4. Business Model Diagram

概念：业务模型说明企业怎样创造、交付及获取价值。

适用条件：表达业务价值逻辑。

逻辑关系：三方面共同形成模型理由。

决策方法：核对模型是否解释价值逻辑。

制品及证据：业务模型图。

适用边界：本节只给定义，不指定Canvas模板或指标。

来源块：C220-web-2025:05-architecture-content:b00237, C220-web-2025:05-architecture-content:b00238

<details><summary>展开本节完整英文来源</summary>

3.6.3.4. Business Model Diagram

A model describing the rationale for how an enterprise creates,
delivers, and captures value.

</details>

<a id="tag_03_06_02_05"></a>
## 3.6.3.5. Business Capability Map

概念：能力地图展示企业为达目的所需能力。

适用条件：愿景层确定能力需要。

逻辑关系：能力与企业目的关联。

决策方法：核查需要的能力范围。

制品及证据：业务能力地图。

适用边界：所需能力不表示已有实现或成熟等级。

来源块：C220-web-2025:05-architecture-content:b00239, C220-web-2025:05-architecture-content:b00240

<details><summary>展开本节完整英文来源</summary>

3.6.3.5. Business Capability Map

A diagram that shows the business capabilities that an enterprise needs to meet its purposes.

</details>

<a id="tag_03_06_02_06"></a>
## 3.6.3.6. Value Stream Map

概念：价值流图表示为客户/相关者/终端用户产生整体结果的端到端增值活动。

适用条件：愿景层表达价值产生。

逻辑关系：活动以整体结果连接。

决策方法：明确结果及受益者。

制品及证据：价值流图。

适用边界：不是技术任务序列或能力列表。

来源块：C220-web-2025:05-architecture-content:b00241, C220-web-2025:05-architecture-content:b00242

<details><summary>展开本节完整英文来源</summary>

3.6.3.6. Value Stream Map

A diagram representing an end-to-end collection of value-adding
activities that create an overall result for a customer, stakeholder, or end user.

</details>

<a id="tag_03_06_03"></a>
## 3.6.4. Phase B: Business Architecture

概念：B阶段可创建的业务架构制品。

适用条件：开发业务架构。

逻辑关系：目录、矩阵和图支持不同关切。

决策方法：按目的选择适用制品。

制品及证据：B阶段选择清单。

适用边界：may be created不等于全部强制生成。

来源块：C220-web-2025:05-architecture-content:b00243, C220-web-2025:05-architecture-content:b00244

<details><summary>展开本节完整英文来源</summary>

3.6.4. Phase B: Business Architecture

The following describes catalogs, matrices, and diagrams that may be
created within Phase B (Business Architecture) as described in the TOGAF Standard — Architecture Development Method .

</details>

<a id="tag_03_06_03_01"></a>
## 3.6.4.1. Organization/Actor Catalog

概念：组织/演员目录列与IT交互的参与者，包括用户和系统所有者。

适用条件：检查需求覆盖及用户类型限制。

逻辑关系：Organization Unit、Actor，可选Location补充参与范围。

决策方法：按参与类型核查需求完整性和限制。

制品及证据：组织/演员目录。

适用边界：有独立地点目录时不需在此重复；演员不等于角色或人员评级。

来源块：C220-web-2025:05-architecture-content:b00245, C220-web-2025:05-architecture-content:b00246, C220-web-2025:05-architecture-content:b00247, C220-web-2025:05-architecture-content:b00248, C220-web-2025:05-architecture-content:b00249, C220-web-2025:05-architecture-content:b00250

<details><summary>展开本节完整英文来源</summary>

3.6.4.1. Organization/Actor Catalog

The purpose of the Organization/Actor catalog is to capture a definitive listing of all participants that interact with IT, including users and owners of IT systems.

The Organization/Actor catalog can be referenced when developing
requirements in order to test for completeness.

For example, requirements for an application that services customers can be tested for completeness by verifying exactly which customer types
need to be supported and whether there are any particular requirements or restrictions for user types.

The Organization/Actor catalog contains the following metamodel
entities:

Organization Unit Actor Location (may be included in this catalog if an independent Location
catalog is not maintained)

</details>

<a id="tag_03_06_03_02"></a>
## 3.6.4.2. Driver/Goal/Objective Catalog

概念：驱动/目标/具体目标目录给跨组织行动与目标的参照。

适用条件：识别协同、相关者和重复举措。

逻辑关系：组织单位—驱动—目标—具体目标，可选度量。

决策方法：比较相似目标，决定对齐或合并举措。

制品及证据：目录及可选Measure。

适用边界：目录说明目标关系，不证明举措收益已实现。

来源块：C220-web-2025:05-architecture-content:b00251, C220-web-2025:05-architecture-content:b00252, C220-web-2025:05-architecture-content:b00253, C220-web-2025:05-architecture-content:b00254, C220-web-2025:05-architecture-content:b00255

<details><summary>展开本节完整英文来源</summary>

3.6.4.2. Driver/Goal/Objective Catalog

The purpose of the Driver/Goal Objective catalog is to provide a
cross-organizational reference of how an organization meets its drivers in practical terms through goals, objectives, and (optionally) measures.

Publishing a definitive breakdown of drivers, goals, and objectives
allows change initiatives within the enterprise to identify synergies across the organization (e.g., multiple organizations attempting to achieve similar objectives), which in turn allow stakeholders to be identified and related change initiatives to be aligned or consolidated.

The Driver/Goal/Objective catalog contains the following metamodel
entities:

Organization Unit Driver Goal Objective Measure (may optionally be included)

</details>

<a id="tag_03_06_03_03"></a>
## 3.6.4.3. Role Catalog

概念：角色目录列企业授权等级或区域。

适用条件：应用安全、岗位职能及变更培训。

逻辑关系：跨应用角色一致可减少权限变通；业务职能变化可能影响责任和培训。

决策方法：核查真实角色授权及跨应用一致性，评估变更影响。

制品及证据：Role目录、安全及培训需求。

适用边界：此处是企业访问/职能角色，不自动等同G249架构师角色、熟练度或批准人。

来源块：C220-web-2025:05-architecture-content:b00256, C220-web-2025:05-architecture-content:b00257, C220-web-2025:05-architecture-content:b00258, C220-web-2025:05-architecture-content:b00259, C220-web-2025:05-architecture-content:b00260, C220-web-2025:05-architecture-content:b00261, C220-web-2025:05-architecture-content:b00262

<details><summary>展开本节完整英文来源</summary>

3.6.4.3. Role Catalog

The purpose of the Role catalog is to provide a listing of all authorization levels or zones within an enterprise. Frequently, application security or behavior is defined against locally understood concepts of authorization that create complex and unexpected consequences when combined on the user desktop.

If roles are defined, understood, and aligned across organizations and applications, this allows for a more seamless user experience and
generally more secure applications, as administrators do not need to resort to workarounds in order to enable users to carry out their jobs.

In addition to supporting security definition for the enterprise, the
Role catalog also forms a key input to identifying organizational change management impacts, defining job functions, and executing end-user training.

As each role implies access to a number of business functions, if any of these business functions are impacted then change management will be required, organizational responsibilities may need to be redefined, and
retraining may be needed.

The Role catalog contains the following metamodel entities:

Role

</details>

<a id="tag_03_06_03_04"></a>
## 3.6.4.4. Business Service/Function Catalog

概念：服务/职能目录是可查询的职能分解，补充图形分解。

适用条件：识别所需能力、治理层级及变革范围。

逻辑关系：组织单位、业务职能、业务服务，可选应用服务。

决策方法：据分解查询新增需要和组件影响。

制品及证据：服务/职能目录。

适用边界：表达组织能力不使Function与Capability成为相同实体类型。

来源块：C220-web-2025:05-architecture-content:b00263, C220-web-2025:05-architecture-content:b00264, C220-web-2025:05-architecture-content:b00265, C220-web-2025:05-architecture-content:b00266, C220-web-2025:05-architecture-content:b00267

<details><summary>展开本节完整英文来源</summary>

3.6.4.4. Business Service/Function Catalog

The purpose of the Business Service/Function catalog is to provide a functional decomposition in a form that can be filtered, reported on, and queried, as a supplement to graphical Functional Decomposition diagrams.

The Business Service/Function catalog can be used to identify
capabilities of an organization and to understand the level that
governance is applied to the functions of an organization. This
functional decomposition can be used to identify new capabilities
required to support business change or may be used to determine the scope of change initiatives, applications, or technology components.

The Business Service/Function catalog contains the following metamodel entities:

Organization Unit Business Function Business Service Application Service (may optionally be included here)

</details>

<a id="tag_03_06_03_05"></a>
## 3.6.4.5. Location Catalog

概念：地点目录列业务运营及重要资产所在地。

适用条件：界定变革地理范围及部署策略。

逻辑关系：用户/应用位置影响时区可用性、延迟、带宽、访问和本地化。

决策方法：对地点范围检查完整性及环境影响。

制品及证据：Location目录及部署范围。

适用边界：地点名称不证明已有容量或可用性接受标准。

来源块：C220-web-2025:05-architecture-content:b00268, C220-web-2025:05-architecture-content:b00269, C220-web-2025:05-architecture-content:b00270, C220-web-2025:05-architecture-content:b00271, C220-web-2025:05-architecture-content:b00272, C220-web-2025:05-architecture-content:b00273

<details><summary>展开本节完整英文来源</summary>

3.6.4.5. Location Catalog

The Location catalog provides a listing of all locations where an
enterprise carries out business operations or houses architecturally
relevant assets, such as data centers or end-user computing equipment.

Maintaining a definitive list of locations allows change initiatives to quickly define a location scope and to test for completeness when assessing current landscapes or proposed target solutions. For example,
a project to upgrade desktop operating systems will need to identify all locations where desktop operating systems are deployed.

Similarly, when new systems are being implemented a diagram of locations is essential in order to develop appropriate deployment strategies that comprehend both user and application location and identify location-related issues, such as internationalization, localization, timezone impacts on availability, distance impacts on latency, network impacts on bandwidth, and access.

The Location catalog contains the following metamodel entities:

Location

</details>

<a id="tag_03_06_03_06"></a>
## 3.6.4.6. Process/Event/Control/Product Catalog

概念：流程/事件/控制/产品目录记录流程层次、触发、输出和执行控制。

适用条件：查询跨组织范围、共同性和影响。

逻辑关系：高层流程变化可沿子流程影响链追踪。

决策方法：核查触发、控制及产出，并追踪层次变更。

制品及证据：Process/Event/Control/Product目录。

适用边界：目录层次不自动提供控制的真实执行证据。

来源块：C220-web-2025:05-architecture-content:b00274, C220-web-2025:05-architecture-content:b00275, C220-web-2025:05-architecture-content:b00276, C220-web-2025:05-architecture-content:b00277, C220-web-2025:05-architecture-content:b00278

<details><summary>展开本节完整英文来源</summary>

3.6.4.6. Process/Event/Control/Product Catalog

The Process/Event/Control/Product catalog provides a hierarchy of processes, events that trigger processes, outputs from processes, and controls applied to the execution of processes. This catalog provides a
supplement to any Process Flow diagrams that are created and allows an enterprise to filter, report, and query across organizations and processes to identify scope, commonality, or impact.

For example, the Process/Event/Control/Product catalog allows an
enterprise to see relationships of processes to sub-processes in order
to identify the full chain of impacts resulting from changing a
high-level process.

The Process/Event/Control/Product catalog contains the following
metamodel entities:

Process Event Control Product

</details>

<a id="tag_03_06_03_07"></a>
## 3.6.4.7. Contract/Measure Catalog

概念：契约/度量目录记录已约定服务契约及附属度量。

适用条件：管理企业已同意服务水平。

逻辑关系：业务服务、可选应用服务、契约和度量关联。

决策方法：核对指标对应的真实服务协议。

制品及证据：Contract/Measure主清单。

适用边界：拟议指标不能列成已约定服务水平。

来源块：C220-web-2025:05-architecture-content:b00279, C220-web-2025:05-architecture-content:b00280, C220-web-2025:05-architecture-content:b00281, C220-web-2025:05-architecture-content:b00282

<details><summary>展开本节完整英文来源</summary>

3.6.4.7. Contract/Measure Catalog

The Contract/Measure catalog provides a listing of all agreed service contracts and the measures attached to those contracts. It forms the master list of service levels agreed to across the enterprise.

The Contract/Measure catalog contains the following metamodel entities:

Business Service Application Service (optionally) Contract Measure

</details>

<a id="tag_03_06_03_08"></a>
## 3.6.4.8. Business Capabilities Catalog

概念：业务能力目录列为特定目的可能拥有的能力。

适用条件：记录业务能力。

逻辑关系：能力与目的关联。

决策方法：据定义辨别能力身份。

制品及证据：业务能力目录。

适用边界：may possess不证明组织现有能力已实现。

来源块：C220-web-2025:05-architecture-content:b00283, C220-web-2025:05-architecture-content:b00284

<details><summary>展开本节完整英文来源</summary>

3.6.4.8. Business Capabilities Catalog

A listing of abilities that a business may possess to achieve specific purposes.

</details>

<a id="tag_03_06_03_09"></a>
## 3.6.4.9. Value Stream Catalog

概念：价值流目录列面向受益者整体结果的端到端增值活动集合。

适用条件：组织多个价值流。

逻辑关系：每个价值流有结果与客户/相关者。

决策方法：区分流的范围和结果。

制品及证据：价值流目录。

适用边界：不把目录条目当技术流程或实现实例。

来源块：C220-web-2025:05-architecture-content:b00285, C220-web-2025:05-architecture-content:b00286

<details><summary>展开本节完整英文来源</summary>

3.6.4.9. Value Stream Catalog

A listing of end-to-end collections of value-adding activities that create an overall result for a customer, stakeholder, or end user.

</details>

<a id="tag_03_06_03_10"></a>
## 3.6.4.10. Value Stream Stages Catalog

概念：价值流阶段目录组织增值活动的不同阶段。

适用条件：分解端到端价值产生。

逻辑关系：源列Business Capability与Value Stream。

决策方法：核对阶段结果及能力支持关系。

制品及证据：阶段目录和源实体列表。

适用边界：列表未单列阶段实体，不能以此抹除G178/G233的阶段身份。

来源块：C220-web-2025:05-architecture-content:b00287, C220-web-2025:05-architecture-content:b00288, C220-web-2025:05-architecture-content:b00289, C220-web-2025:05-architecture-content:b00290

<details><summary>展开本节完整英文来源</summary>

3.6.4.10. Value Stream Stages Catalog

A listing of end-to-end collections of the different stages for the value-adding activities that create an overall result for customer, stakeholder, or end user.

The Value Stream Stages catalog includes the following metamodel
entities:

Business Capability Value Stream

</details>

<a id="tag_03_06_03_11"></a>
## 3.6.4.11. Business Glossary Catalog

概念：业务术语目录给企业架构元素无歧义名称与描述。

适用条件：业务、信息和系统分析共享语义。

逻辑关系：可补同义词、缩略语及关系，并在ADM中演进。

决策方法：协调术语定义、更新和跨模型使用。

制品及证据：业务词汇表及可选语义关系。

适用边界：同名或同义词不等于合并不同实体身份。

来源块：C220-web-2025:05-architecture-content:b00291, C220-web-2025:05-architecture-content:b00292, C220-web-2025:05-architecture-content:b00293

<details><summary>展开本节完整英文来源</summary>

3.6.4.11. Business Glossary Catalog

This catalog contains the name and unambiguous description of all
elements contained in or interacting with the Enterprise Architecture.

Optional information could include element enterprise synonyms,
abbreviations/acronyms, and relationships with other elements. This catalog provides the semantics to be used by all analysts (e.g., business, information, and system) for their architecture products,
including information/data models, and evolves throughout the ADM.

</details>

<a id="tag_03_06_03_12"></a>
## 3.6.4.12. Business Interaction Matrix

概念：业务交互矩阵表达组织与职能的交互和依赖。

适用条件：识别跨组织价值链。

逻辑关系：源列Organization、Function、Service及服务通信/依赖关系。

决策方法：区分通信与依赖并核查交互事实。

制品及证据：业务交互矩阵。

适用边界：源列表Organization用词与Organization Unit保持可追溯，不从空格推断无交互。

来源块：C220-web-2025:05-architecture-content:b00294, C220-web-2025:05-architecture-content:b00295, C220-web-2025:05-architecture-content:b00296, C220-web-2025:05-architecture-content:b00297, C220-web-2025:05-architecture-content:b00298

<details><summary>展开本节完整英文来源</summary>

3.6.4.12. Business Interaction Matrix

The purpose of this matrix is to depict the relationship interactions
between organizations and business functions across the enterprise.

Understanding business interaction of an enterprise is important as it
helps to highlight value chain and dependencies across organizations.

The Business Interaction matrix shows the following metamodel entities
and relationships:

Organization Business Function Business Service Business Service communicates with Business Service relationships Business Service is dependent on Business Service relationships

</details>

<a id="tag_03_06_03_13"></a>
## 3.6.4.13. Actor/Role Matrix

概念：演员/角色矩阵显示演员执行哪些角色。

适用条件：安全、技能要求、培训及组织变更。

逻辑关系：Actor performs Role关系连接两轴。

决策方法：核对承担关系再识别相应要求。

制品及证据：演员—角色矩阵。

适用边界：承担角色不证明技能达标或正式授权已获证实。

来源块：C220-web-2025:05-architecture-content:b00299, C220-web-2025:05-architecture-content:b00300, C220-web-2025:05-architecture-content:b00301, C220-web-2025:05-architecture-content:b00302, C220-web-2025:05-architecture-content:b00303

<details><summary>展开本节完整英文来源</summary>

3.6.4.13. Actor/Role Matrix

The purpose of this matrix is to show which actors perform which roles, supporting definition of security and skills requirements.

Understanding Actor-to-Role relationships is a key supporting tool in
definition of training needs, user security settings, and organizational
change management.

The Actor/Role matrix shows the following metamodel entities and
relationships:

Actor Role Actor performs Role relationships

</details>

<a id="tag_03_06_03_14"></a>
## 3.6.4.14. Value Stream/Capability Matrix

概念：价值流/能力矩阵显示每一阶段所需能力。

适用条件：分析阶段能力支持。

逻辑关系：阶段到能力的需要关系。

决策方法：检查阶段是否缺能力支持。

制品及证据：价值流/能力矩阵。

适用边界：需要关系不证明能力实例已经实现阶段结果。

来源块：C220-web-2025:05-architecture-content:b00304, C220-web-2025:05-architecture-content:b00305

<details><summary>展开本节完整英文来源</summary>

3.6.4.14. Value Stream/Capability Matrix

The purpose of this matrix is to show the capabilities required to
support each stage of a value stream.

</details>

<a id="tag_03_06_03_15"></a>
## 3.6.4.15. Strategy/Capability Matrix

概念：战略/能力矩阵显示支持特定战略陈述所需能力。

适用条件：把战略要求映射能力。

逻辑关系：陈述和所需能力保持关联。

决策方法：核查战略覆盖及能力缺口。

制品及证据：战略/能力矩阵。

适用边界：所需支持不自动量化价值或确定投资优先级。

来源块：C220-web-2025:05-architecture-content:b00306, C220-web-2025:05-architecture-content:b00307

<details><summary>展开本节完整英文来源</summary>

3.6.4.15. Strategy/Capability Matrix

The purpose of this matrix is to show the capabilities required to
support specific strategy statements.

</details>

<a id="tag_03_06_03_16"></a>
## 3.6.4.16. Capability/Organization Matrix

概念：能力/组织矩阵显示实现能力的组织元素。

适用条件：确定能力实现组织范围。

逻辑关系：源列能力、价值流及组织单位。

决策方法：核查组织对能力的实现关联。

制品及证据：能力/组织矩阵。

适用边界：出现Value Stream实体不改变其主要能力—组织用途，不能推定单一所有者。

来源块：C220-web-2025:05-architecture-content:b00308, C220-web-2025:05-architecture-content:b00309, C220-web-2025:05-architecture-content:b00310

<details><summary>展开本节完整英文来源</summary>

3.6.4.16. Capability/Organization Matrix

The purpose of this matrix is to show the organization elements that
implement each capability. The Capability/Organization matrix includes
the following metamodel entities:

Business Capability Value Stream Organization Unit

</details>

<a id="tag_03_06_03_17"></a>
## 3.6.4.17. Business Footprint Diagram

概念：业务足迹图把目标、组织、职能、服务和实现技术组件相连。

适用条件：向CxO沟通关键追溯和服务所有权。

逻辑关系：技术组件沿服务/职能到满足的业务目标。

决策方法：只选高层关键事实并核查归属。

制品及证据：业务足迹图及目标追溯。

适用边界：关键事实图不替代完整需求或业务价值证据。

来源块：C220-web-2025:05-architecture-content:b00311, C220-web-2025:05-architecture-content:b00312, C220-web-2025:05-architecture-content:b00313, C220-web-2025:05-architecture-content:b00314

<details><summary>展开本节完整英文来源</summary>

3.6.4.17. Business Footprint Diagram

A Business Footprint diagram describes the links between business goals,
organizational units, business functions, and services, and maps these
functions to the technical components delivering the required
capability.

A Business Footprint diagram provides a clear traceability between a
technical component and the business goal that it satisfies, while also
demonstrating ownership of the services identified.

A Business Footprint diagram demonstrates only the key facts linking
organization unit functions to delivery services and is utilized as a
communication platform for senior-level (CxO) stakeholders.

</details>

<a id="tag_03_06_03_18"></a>
## 3.6.4.18. Business Service/Information Diagram

概念：服务/信息图显示服务需要、消费或产生的数据，可示信息来源。

适用条件：B阶段初步信息表达。

逻辑关系：初始信息模型在C数据架构继续细化。

决策方法：核查服务输入输出及来源。

制品及证据：业务服务/信息图。

适用边界：初始信息模型不等于已完成逻辑/物理数据架构。

来源块：C220-web-2025:05-architecture-content:b00315, C220-web-2025:05-architecture-content:b00316, C220-web-2025:05-architecture-content:b00317

<details><summary>展开本节完整英文来源</summary>

3.6.4.18. Business Service/Information Diagram

The Business Service/Information diagram shows the information needed to support one or more business services. The Business Service/Information diagram shows what data is consumed by or produced by a business service
and may also show the source of information.

The Business Service/Information diagram shows an initial representation of the information present within the architecture and therefore forms a basis for elaboration and refinement within Phase C (Data Architecture).

</details>

<a id="tag_03_06_03_19"></a>
## 3.6.4.19. Functional Decomposition Diagram

概念：职能分解图在一页表达相关组织能力的职能视角。

适用条件：先理解组织做什么，避免陷入如何做。

逻辑关系：可叠热图表示变革范围与分期决定。

决策方法：先分解职能，再按证据叠加范围/决定。

制品及证据：职能分解与可选热图。

适用边界：文本使用capabilities不证明职能与能力实体同一，热图不自动生成无依据评级。

来源块：C220-web-2025:05-architecture-content:b00318, C220-web-2025:05-architecture-content:b00319, C220-web-2025:05-architecture-content:b00320

<details><summary>展开本节完整英文来源</summary>

3.6.4.19. Functional Decomposition Diagram

The purpose of the Functional Decomposition diagram is to show on a
single page the capabilities of an organization that are relevant to the
consideration of an architecture. By examining the capabilities of an
organization from a functional perspective, it is possible to quickly
develop models of what the organization does without being dragged into
extended debate on how the organization does it.

Once a basic Functional Decomposition diagram has been developed, it
becomes possible to layer heat maps on top of this diagram to show scope
and decisions. For example, the capabilities to be implemented in
different phases of a change program.

</details>

<a id="tag_03_06_03_20"></a>
## 3.6.4.20. Product Lifecycle Diagram

概念：产品生命周期图表示产品从创建/接收到销售、处置或销毁的可能状态变化。

适用条件：物理、软件及服务产品。

逻辑关系：状态及迁移表示产品生命周期。

决策方法：核对可能状态与迁移。

制品及证据：产品状态图。

适用边界：产品不限实物，不能套未经业务确认的统一状态序列。

来源块：C220-web-2025:05-architecture-content:b00321, C220-web-2025:05-architecture-content:b00322, C220-web-2025:05-architecture-content:b00323

<details><summary>展开本节完整英文来源</summary>

3.6.4.20. Product Lifecycle Diagram

This diagram shows the possible state transitions of a business product,
from its creation or receipt to its sale, disposal, or destruction.

The product may be a product of any kind (physical, software, or
service).

</details>

<a id="tag_03_06_03_21"></a>
## 3.6.4.21. Goal/Objective/Business Service Diagram

概念：目标/具体目标/服务图说明服务如何支持愿景或战略。

适用条件：分析服务对业务绩效的贡献。

逻辑关系：服务关联驱动、目标、具体目标和度量。

决策方法：核对共同绩效目标与高绩效的定性条件。

制品及证据：服务—目标—指标关联图。

适用边界：定性输入不能冒充测得绩效或量化价值。

来源块：C220-web-2025:05-architecture-content:b00324, C220-web-2025:05-architecture-content:b00325, C220-web-2025:05-architecture-content:b00326

<details><summary>展开本节完整英文来源</summary>

3.6.4.21. Goal/Objective/Business Service Diagram

The purpose of a Goal/Objective/Business Service diagram is to define
the ways in which a business service contributes to the achievement of a
business vision or strategy.

Business services are associated with the drivers, goals, objectives,
and measures that they support, allowing the enterprise to understand
which business services contribute to similar aspects of business
performance. The Goal/Objective/Business Service diagram also provides
qualitative input on what constitutes high performance for a particular
business service.

</details>

<a id="tag_03_06_03_22"></a>
## 3.6.4.22. Business Use-Case Diagram

概念：业务用例图显示服务提供者与消费者，说明能力怎样及何时使用。

适用条件：验证演员、角色与流程职能交互。

逻辑关系：演员或其他服务消费业务服务；后续可扩为数据应用技术细节。

决策方法：验证业务交互，再决定设计复用和细化。

制品及证据：业务用例及交互验证。

适用边界：用例不是全部业务流程或已实现系统行为。

来源块：C220-web-2025:05-architecture-content:b00327, C220-web-2025:05-architecture-content:b00328, C220-web-2025:05-architecture-content:b00329

<details><summary>展开本节完整英文来源</summary>

3.6.4.22. Business Use-Case Diagram

A Business Use-Case diagram displays the relationships between consumers
and providers of business services. Business services are consumed by
actors or other business services and the Business Use-Case diagram
provides added richness in describing business capability by
illustrating how and when that capability is used.

The purpose of the Business Use-Case diagram is to help to describe and
validate the interaction between actors and their roles to processes and
functions. As the architecture progresses, the use-case can evolve from
the business level to include data, application, and technology details.
Architectural business use-cases can also be re-used in systems design
work.

</details>

<a id="tag_03_06_03_23"></a>
## 3.6.4.23. Organization Decomposition Diagram

概念：组织分解图连接组织树内演员、角色和地点。

适用条件：呈现所有者与决策者指挥链。

逻辑关系：组织地图应能追溯决策链，目标关联非其直接意图。

决策方法：核查真实所有者、决策者及组织关系。

制品及证据：组织分解图。

适用边界：可直觉关联目标不证明具体目标归属或实际授权。

来源块：C220-web-2025:05-architecture-content:b00330, C220-web-2025:05-architecture-content:b00331, C220-web-2025:05-architecture-content:b00332

<details><summary>展开本节完整英文来源</summary>

3.6.4.23. Organization Decomposition Diagram

An Organization Decomposition diagram describes the links between actor,
roles, and location within an organization tree.

An organization map should provide a chain of command of owners and
decision-makers in the organization. Although it is not the intent of
the Organization Decomposition diagram to link goal to organization, it
should be possible to intuitively link the goals to the stakeholders
from the Organization Decomposition diagram.

</details>

<a id="tag_03_06_03_24"></a>
## 3.6.4.24. Process Flow Diagram

概念：流程图表示活动控制顺序以及控制、触发事件和产出。

适用条件：与专业人员阐明如何完成工作。

逻辑关系：泳道可表示归属或实现应用；步骤可细分为职能再展开流程。

决策方法：按实际活动核对顺序、控制、触发及产出。

制品及证据：流程图、泳道及步骤细化。

适用边界：泳道不是任意RACI，不能由流程图推断未定义并发或异常规则。

来源块：C220-web-2025:05-architecture-content:b00333, C220-web-2025:05-architecture-content:b00334, C220-web-2025:05-architecture-content:b00335, C220-web-2025:05-architecture-content:b00336, C220-web-2025:05-architecture-content:b00337

<details><summary>展开本节完整英文来源</summary>

3.6.4.24. Process Flow Diagram

The purpose of the Process Flow diagram is to depict all models and
mappings related to the process metamodel entity.

Process Flow diagrams show sequential flow of control between activities
and may utilize swim-lane techniques to represent ownership and
realization of process steps. For example, the application that supports
a process step may be shown as a swim-lane.

In addition to showing a sequence of activity, process flows can also be
used to detail the controls that apply to a process, the events that
trigger or result from completion of a process, and also the products
that are generated from process execution.

Process Flow diagrams are useful in elaborating the architecture with
subject specialists, as they allow the specialist to describe “how the
job is done” for a particular function. Through this process, each
process step can become a more fine-grained function and can then in
turn be elaborated as a process.

</details>

<a id="tag_03_06_03_25"></a>
## 3.6.4.25. Business Event Diagram

概念：业务事件图连接触发事件及响应流程。

适用条件：信息到达或时间点引发业务工作。

逻辑关系：事件应触发流程并生成业务响应/结果。

决策方法：核对触发和业务结果。

制品及证据：事件—流程图。

适用边界：业务事件不等于必须使用事件消息技术。

来源块：C220-web-2025:05-architecture-content:b00338, C220-web-2025:05-architecture-content:b00339, C220-web-2025:05-architecture-content:b00340

<details><summary>展开本节完整英文来源</summary>

3.6.4.25. Business Event Diagram

The purpose of the Business Event diagram is to depict the relationship between events and process.

Certain events — such as arrival of certain information (e.g., customer
submits sales order) or a certain point in time (e.g., end of fiscal
quarter) — cause work and certain actions need to be undertaken within
the business. These are often referred to as “business events” or simply
“events” and are considered as triggers for a process. It is important
to note that the event has to trigger a process and generate a business
response or result.

</details>

<a id="tag_03_06_03_26"></a>
## 3.6.4.26. Business Capability Map

概念：能力地图显示目的所需能力，可分解子能力。

适用条件：B阶段表达业务能力结构。

逻辑关系：父子能力分解保持能力身份。

决策方法：核对能力范围及分解。

制品及证据：能力地图。

适用边界：分解不表示活动先后、人员等级或实现状态。

来源块：C220-web-2025:05-architecture-content:b00341, C220-web-2025:05-architecture-content:b00342, C220-web-2025:05-architecture-content:b00343

<details><summary>展开本节完整英文来源</summary>

3.6.4.26. Business Capability Map

A diagram that shows the business capabilities that an enterprise needs
to meet its purposes.

Business capabilities may be decomposed into sub-capabilities.

</details>

<a id="tag_03_06_03_27"></a>
## 3.6.4.27. Value Stream Map

概念：价值流图表示产生整体结果的端到端增值集合。

适用条件：B阶段建模客户/相关者价值。

逻辑关系：源列Business Capability和Value Stream。

决策方法：核对受益者、结果及能力支持。

制品及证据：价值流地图。

适用边界：能力支持关系不能把价值流与能力合并。

来源块：C220-web-2025:05-architecture-content:b00344, C220-web-2025:05-architecture-content:b00345, C220-web-2025:05-architecture-content:b00346, C220-web-2025:05-architecture-content:b00347

<details><summary>展开本节完整英文来源</summary>

3.6.4.27. Value Stream Map

A diagram representing an end-to-end collection of value-adding
activities that create an overall result for a customer, stakeholder, or
end user.

The value stream map includes the following metamodel entities:

Business Capability Value Stream

</details>

<a id="tag_03_06_03_28"></a>
## 3.6.4.28. Organization Map

概念：组织地图显示企业、伙伴及相关者主要实体的关系。

适用条件：分析企业内外组织关联。

逻辑关系：关系范围可跨企业边界。

决策方法：按实际组织关系建图。

制品及证据：组织地图。

适用边界：本节未规定组织树、审批链或网络方向。

来源块：C220-web-2025:05-architecture-content:b00348, C220-web-2025:05-architecture-content:b00349

<details><summary>展开本节完整英文来源</summary>

3.6.4.28. Organization Map

A diagram showing the relationships between the primary entities that
make up the enterprise, its partners, and stakeholders.

</details>

<a id="tag_03_06_03_29"></a>
## 3.6.4.29. Information Map

概念：信息地图是一组业务词汇反映的信息概念及关系。

适用条件：B阶段从关键业务信息开始。

逻辑关系：如客户、账户、产品等概念以业务术语描述。

决策方法：先列最重要概念并定义语义关系。

制品及证据：信息概念地图。

适用边界：概念不能直接视为物理数据库表或数据对象实例。

来源块：C220-web-2025:05-architecture-content:b00350, C220-web-2025:05-architecture-content:b00351

<details><summary>展开本节完整英文来源</summary>

3.6.4.29. Information Map

A collection of information concepts and their relationships to one
another. Information concepts, in effect, reflect the business
vocabulary; e.g., client, account, or product. Mapping information in
the Business Architecture starts with listing those elements that matter
most to the business as well as how they are described in business
terms.

</details>

<a id="tag_03_06_04"></a>
## 3.6.5. Phase C: Data Architecture

概念：C数据架构阶段可选制品。

适用条件：开发数据架构。

逻辑关系：后续目录矩阵和图处理数据不同关切。

决策方法：按用途选择适用制品。

制品及证据：数据制品选择记录。

适用边界：阶段清单不表示每图无条件必交。

来源块：C220-web-2025:05-architecture-content:b00352, C220-web-2025:05-architecture-content:b00353

<details><summary>展开本节完整英文来源</summary>

3.6.5. Phase C: Data Architecture

The following describes catalogs, matrices, and diagrams that may be
created within Phase C (Data Architecture) as described in the TOGAF Standard — Architecture Development Method .

</details>

<a id="tag_03_06_04_01"></a>
## 3.6.5.1. Data Entity/Data Component Catalog

概念：数据实体/组件目录记录全企业数据及其结构实现。

适用条件：维护数据清单并鼓励有效使用。

逻辑关系：实体关联逻辑和物理数据组件。

决策方法：核查覆盖范围及实体—组件结构映射。

制品及证据：Data Entity、Logical/Physical Data Component目录。

适用边界：逻辑实体和物理组件不同身份，不因名称相同合并。

来源块：C220-web-2025:05-architecture-content:b00354, C220-web-2025:05-architecture-content:b00355, C220-web-2025:05-architecture-content:b00356, C220-web-2025:05-architecture-content:b00357, C220-web-2025:05-architecture-content:b00358, C220-web-2025:05-architecture-content:b00359

<details><summary>展开本节完整英文来源</summary>

3.6.5.1. Data Entity/Data Component Catalog

This catalog identifies and maintains a list of the data used across the
enterprise, relating data entities to data components showing how data
entities are structured.

Its purpose is to:

Identify all data used in the enterprise Encourage effective data use

The Data Entity/Data Component catalog contains the following metamodel entities:

Data Entity Logical Data Component Physical Data Component

</details>

<a id="tag_03_06_04_02"></a>
## 3.6.5.2. Data Entity/Business Function Matrix

概念：数据实体/业务职能矩阵支持数据归属、交换、差距及来源/记录/参考应用分析。

适用条件：建立企业数据治理。

逻辑关系：职能由有边界服务支持并通过流程实现；数据与所有组织关联。

决策方法：按映射识别缺数据及明确数据责任和应用角色。

制品及证据：数据—职能矩阵及治理分配。

适用边界：图中归属建议仍需真实组织接受；origin/record/reference不可混用。

来源块：C220-web-2025:05-architecture-content:b00360, C220-web-2025:05-architecture-content:b00361, C220-web-2025:05-architecture-content:b00362, C220-web-2025:05-architecture-content:b00363, C220-web-2025:05-architecture-content:b00364

<details><summary>展开本节完整英文来源</summary>

3.6.5.2. Data Entity/Business Function Matrix

The purpose of the Data Entity/Business Function matrix is to depict the relationship between data entities and business functions within the
enterprise. Business functions are supported by business services with
explicitly defined boundaries and will be supported and realized by business processes. The mapping of the Data Entity-Business Function relationship enables the following to take place:

Assign ownership of data entities to organizations Understand the data and information exchange requirements business
services Support the gap analysis and determine whether any data entities are
missing and need to be created Define application of origin, application of record, and application
of reference for data entities Enable development of data governance programs across the enterprise
(establish data steward, develop data standards pertinent to the
business function, etc.)

The Data Entity/Business Function matrix shows the following entities
and relationships:

Data Entity Business Function Data Entity relationship to owning Organization Unit

</details>

<a id="tag_03_06_04_03"></a>
## 3.6.5.3. Application/Data Matrix

概念：应用/数据矩阵显示逻辑应用组件对数据实体的创建、读取、更新、删除关系。

适用条件：分析访问、复制、重复更新及应用缺口。

逻辑关系：两轴为Logical Application Component和Data Entity。

决策方法：逐应用逐数据核查实际CRUD及重复更新。

制品及证据：应用/数据矩阵。

适用边界：不能给每个单元格默认完整CRUD；master/reference等数据分类不是自动一致性政策。

来源块：C220-web-2025:05-architecture-content:b00365, C220-web-2025:05-architecture-content:b00366, C220-web-2025:05-architecture-content:b00367, C220-web-2025:05-architecture-content:b00368, C220-web-2025:05-architecture-content:b00369, C220-web-2025:05-architecture-content:b00370, C220-web-2025:05-architecture-content:b00371

<details><summary>展开本节完整英文来源</summary>

3.6.5.3. Application/Data Matrix

The purpose of the Application/Data matrix is to depict the relationship
between applications (i.e., application components) and the data
entities that are accessed and updated by them.

Applications will create, read, update, and delete specific data
entities that are associated with them. For example, a Customer
Relationship Management (CRM) application will create, read, update, and
delete customer entity information.

The data entities in a package/packaged services environment can be
classified as master data, reference data, transactional data, content
data, and historical data. Applications that operate on the data
entities include transactional applications, information management
applications, and business warehouse applications.

The mapping of the Application Component-Data Entity relationship is an
important step as it enables the following to take place:

Assign access of data to specific applications in the organization Understand the degree of data duplication within different
applications, and the scale of the data lifecycle Understand where the same data is updated by different applications Support the gap analysis and determine whether any of the applications
are missing and as a result need to be created

The Application/Data matrix is a two-dimensional table with Logical
Application Component on one axis and Data Entity on the other axis.

</details>

<a id="tag_03_06_04_04"></a>
## 3.6.5.4. Conceptual Data Diagram

概念：概念数据图描述关键数据实体关系，面向业务相关者。

适用条件：回应业务数据关切。

逻辑关系：可用ER或简化UML类图。

决策方法：选择业务可理解的概念关系表示。

制品及证据：概念数据图。

适用边界：不规定物理实现或特定数据库。

来源块：C220-web-2025:05-architecture-content:b00372, C220-web-2025:05-architecture-content:b00373, C220-web-2025:05-architecture-content:b00374, C220-web-2025:05-architecture-content:b00375

<details><summary>展开本节完整英文来源</summary>

3.6.5.4. Conceptual Data Diagram

The key purpose of the Conceptual Data diagram is to depict the relationships between critical data entities within the enterprise. This diagram is developed to address the concerns of business stakeholders.

Techniques used include:

Entity relationship models Simplified UML class diagrams

</details>

<a id="tag_03_06_04_05"></a>
## 3.6.5.5. Logical Data Diagram

概念：逻辑数据图展示关键实体关系的逻辑视图。

适用条件：面向应用开发者及数据库设计者。

逻辑关系：细节与受众区别于业务概念图。

决策方法：核查逻辑关系能支持设计关切。

制品及证据：逻辑数据图。

适用边界：本节未定义完整字段、基数或物理表规范。

来源块：C220-web-2025:05-architecture-content:b00376, C220-web-2025:05-architecture-content:b00377, C220-web-2025:05-architecture-content:b00378

<details><summary>展开本节完整英文来源</summary>

3.6.5.5. Logical Data Diagram

The key purpose of the Logical Data diagram is to show logical views of the relationships between critical data entities within the enterprise. This diagram is developed to address the concerns of:

Application developers Database designers

</details>

<a id="tag_03_06_04_06"></a>
## 3.6.5.6. Data Dissemination Diagram

概念：数据传播图连接实体、服务与应用组件，展示逻辑数据的物理实现。

适用条件：细化IT规模及业务关键性。

逻辑关系：可示复制、主副本归属及封装/访问数据的服务。

决策方法：核对实现、复制和主参考关系，结合业务价值判断关键性。

制品及证据：数据传播图与复制/主副本映射。

适用边界：图支持容量估算，不提供无测量依据的容量或一致性结论。

来源块：C220-web-2025:05-architecture-content:b00379, C220-web-2025:05-architecture-content:b00380, C220-web-2025:05-architecture-content:b00381

<details><summary>展开本节完整英文来源</summary>

3.6.5.6. Data Dissemination Diagram

The purpose of the Data Dissemination diagram is to show the
relationship between data entity, business service, and application
components. The diagram shows how the logical entities are to be
physically realized by application components. This allows effective
sizing to be carried out and the IT footprint to be refined. Moreover,
by assigning business value to data, an indication of the business
criticality of application components can be gained.

Additionally, the diagram may show data replication and application
ownership of the master reference for data. In this instance, it can
show two copies and the master-copy relationship between them. This
diagram can include services; that is, services encapsulate data and
they reside in an application, or services that reside on an application
and access data encapsulated within the application.

</details>

<a id="tag_03_06_04_07"></a>
## 3.6.5.7. Data Security Diagram

概念：数据安全图/矩阵表示角色、组织、应用访问数据及保护措施。

适用条件：分析隐私、外部访问和威胁。

逻辑关系：访问与安全措施对应数据边界。

决策方法：核查访问方、外部范围及措施证据。

制品及证据：数据安全图或矩阵。

适用边界：表达访问不自动证明实际法律合规或授权执行成功。

来源块：C220-web-2025:05-architecture-content:b00382, C220-web-2025:05-architecture-content:b00383, C220-web-2025:05-architecture-content:b00384, C220-web-2025:05-architecture-content:b00385

<details><summary>展开本节完整英文来源</summary>

3.6.5.7. Data Security Diagram

This diagram shows which data is accessed by which roles, organization units, and applications. It may be shown as a diagram or presented as a matrix.

Its purpose is to:

Demonstrate compliance with data privacy laws and regulations Show security threats arising as a result of data access Show which parties outside of the organization have access to data Show security measures applied to data access

</details>

<a id="tag_03_06_04_08"></a>
## 3.6.5.8. Data Migration Diagram

概念：数据迁移图显示源提取、目标加载及可选转换清洗。

适用条件：从基线数据迁到目标。

逻辑关系：C阶段可概览，后续细化源字段到目标字段。

决策方法：核查源目标及转换关系并按需细化。

制品及证据：迁移图及字段映射。

适用边界：迁移设计不表示已执行、清洗成功或数据丢失可接受。

来源块：C220-web-2025:05-architecture-content:b00386, C220-web-2025:05-architecture-content:b00387

<details><summary>展开本节完整英文来源</summary>

3.6.5.8. Data Migration Diagram

This diagram shows how data is extracted from baseline or source location(s) and loaded into target location(s). It may show where data is transformed and/or cleansed on the way. In Phase C of the ADM, the diagram is likely to be at an overview level. Later, it may be
elaborated to show which source data items map to which target data
items.

</details>

<a id="tag_03_06_04_09"></a>
## 3.6.5.9. Data Lifecycle Diagram

概念：数据生命周期图把数据作为独立实体表达从构想到处置的状态变化。

适用条件：在业务流程约束内管理数据。

逻辑关系：可标触发事件/规则；与流程分离可发现共同数据需求。

决策方法：核查状态、触发及共享需求。

制品及证据：数据状态图。

适用边界：数据状态不等于流程活动；未定义状态或保留期限不能自动补齐。

来源块：C220-web-2025:05-architecture-content:b00388, C220-web-2025:05-architecture-content:b00389, C220-web-2025:05-architecture-content:b00390, C220-web-2025:05-architecture-content:b00391

<details><summary>展开本节完整英文来源</summary>

3.6.5.9. Data Lifecycle Diagram

The Data Lifecycle diagram is an essential part of managing business
data throughout its lifecycle from conception until disposal within the
constraints of the business process.

The data is considered as an entity in its own right, decoupled from
business process and activity. Each change in state is represented on
the diagram which may include the event or rules that trigger that
change in state.

The separation of data from process allows common data requirements to
be identified which enables resource sharing to be achieved more
effectively.

</details>

<a id="tag_03_06_05"></a>
## 3.6.6. Phase C: Application Architecture

概念：C应用架构阶段可选的目录、矩阵与图。

适用条件：开发应用架构。

逻辑关系：推荐制品回应应用范围、交互、使用和部署关切。

决策方法：按架构目的选取制品。

制品及证据：应用制品选择记录。

适用边界：may be created不等于每次全部必交。

来源块：C220-web-2025:05-architecture-content:b00392, C220-web-2025:05-architecture-content:b00393

<details><summary>展开本节完整英文来源</summary>

3.6.6. Phase C: Application Architecture

The following describes catalogs, matrices, and diagrams that may be
created within Phase C (Application Architecture) as described in the TOGAF Standard — Architecture Development Method .

</details>

<a id="tag_03_06_05_01"></a>
## 3.6.6.1. Application Portfolio Catalog

概念：应用组合目录维护企业应用清单。

适用条件：界定跨应用变革范围及应用治理。

逻辑关系：经约定的组合是其余应用矩阵和图的基础，通常为C应用阶段起点。

决策方法：核查应用服务及逻辑/物理应用组件的覆盖与约定。

制品及证据：Application Service、Logical/Physical Application Component目录。

适用边界：清单存在不等于组合已经组织批准；服务与组件不合并。

来源块：C220-web-2025:05-architecture-content:b00394, C220-web-2025:05-architecture-content:b00395, C220-web-2025:05-architecture-content:b00396, C220-web-2025:05-architecture-content:b00397, C220-web-2025:05-architecture-content:b00398

<details><summary>展开本节完整英文来源</summary>

3.6.6.1. Application Portfolio Catalog

The purpose of this catalog is to identify and maintain a list of all
the applications in the enterprise. This list helps to define the
horizontal scope of change initiatives that may impact particular kinds
of applications. An agreed Application Portfolio allows a standard set
of applications to be defined and governed.

The Application Portfolio catalog provides a foundation on which to base
the remaining matrices and diagrams. It is typically the start point of
the Application Architecture phase.

The Application Portfolio catalog contains the following metamodel
entities:

Application Service Logical Application Component Physical Application Component

</details>

<a id="tag_03_06_05_02"></a>
## 3.6.6.2. Interface Catalog

概念：接口目录记录应用间接口及依赖范围。

适用条件：尽早界定应用交互及差距。

逻辑关系：接口可为批文件、数据库直连、API或Web服务；组件通信映射支持识别中心依赖、数量类型、重复和简化机会。

决策方法：逐接口核对端点、方式及依赖，评估目标组合简化和缺失应用。

制品及证据：逻辑/物理应用组件及application communicates with application关系目录。

适用边界：接口不必是API；目录不能证明真实交互成功或默认全部CRUD。

来源块：C220-web-2025:05-architecture-content:b00399, C220-web-2025:05-architecture-content:b00400, C220-web-2025:05-architecture-content:b00401, C220-web-2025:05-architecture-content:b00402, C220-web-2025:05-architecture-content:b00403, C220-web-2025:05-architecture-content:b00404, C220-web-2025:05-architecture-content:b00405

<details><summary>展开本节完整英文来源</summary>

3.6.6.2. Interface Catalog

The purpose of the Interface catalog is to scope and document the
interfaces between applications to enable the overall dependencies
between applications to be scoped as early as possible.

Applications will create, read, update, and delete data within other
applications; this will be achieved by some kind of interface, whether
via a batch file that is loaded periodically, a direct connection to
another application’s database, or via some form of API or web service.

The mapping of the Application Component-Application Component entity
relationship is an important step as it enables the following to take
place:

Understand the degree of interaction between applications, identifying
those that are central in terms of their dependencies on other
applications Understand the number and types of interfaces between applications Understand the degree of duplication of interfaces between
applications Identify the potential for simplification of interfaces when
considering the target Application Portfolio Support the gap analysis and determine whether any of the applications
are missing and as a result need to be created

The Interface catalog contains the following metamodel entities:

Logical Application Component Physical Application Component Application communicates with application relationship

</details>

<a id="tag_03_06_05_03"></a>
## 3.6.6.3. Application/Organization Matrix

概念：应用/组织矩阵表达组织单位使用的应用及其支持需求。

适用条件：界定业务运营应用集合和应用缺口。

逻辑关系：两轴为逻辑/物理应用组件与组织单位；复合路径为组织拥有服务、所属演员使用服务、应用实现服务。

决策方法：分别验证复合路径再建立使用映射。

制品及证据：应用/组织矩阵及组织—演员—服务—应用证据。

适用边界：使用不等于所有权，不能仅因同一组织名称而推断全路径。

来源块：C220-web-2025:05-architecture-content:b00406, C220-web-2025:05-architecture-content:b00407, C220-web-2025:05-architecture-content:b00408, C220-web-2025:05-architecture-content:b00409, C220-web-2025:05-architecture-content:b00410, C220-web-2025:05-architecture-content:b00411, C220-web-2025:05-architecture-content:b00412

<details><summary>展开本节完整英文来源</summary>

3.6.6.3. Application/Organization Matrix

The purpose of this matrix is to depict the relationship between
applications and organizational units within the enterprise.

Business operations are performed by organizational units. Some of the
operations and services performed by those organizational units will be
supported by applications. The mapping of the Application
Component-Organization Unit relationship is an important step as it
enables the following to take place:

Assign usage of applications to the organization units that perform
business operations Understand the application support requirements of the business
services and processes carried out by an organization unit Support the gap analysis and determine whether any of the applications
are missing and as a result need to be created Define the application set used by a particular organization unit

The Application/Organization matrix is a two-dimensional table with
Logical/Physical Application Component on one axis and Organization Unit
on the other axis.

The relationship between these two entities is a composite of a number
of metamodel relationships that need validating:

Organization Units own Services Actors that belong to Organization Units use Services Services are realized by Logical/Physical Application Components

</details>

<a id="tag_03_06_05_04"></a>
## 3.6.6.4. Role/Application Matrix

概念：角色/应用矩阵表达业务角色所用应用。

适用条件：角色化使用、安全政策和支持缺口分析。

逻辑关系：人员在任务中承担角色；逻辑应用组件与Role构成两轴。

决策方法：核查实际角色使用，比较安全需求与现有政策。

制品及证据：角色/应用矩阵及政策核对。

适用边界：使用角色不证明人员能力、真实授权或架构治理批准权限。

来源块：C220-web-2025:05-architecture-content:b00413, C220-web-2025:05-architecture-content:b00414, C220-web-2025:05-architecture-content:b00415, C220-web-2025:05-architecture-content:b00416, C220-web-2025:05-architecture-content:b00417, C220-web-2025:05-architecture-content:b00418

<details><summary>展开本节完整英文来源</summary>

3.6.6.4. Role/Application Matrix

The purpose of the Role/Application matrix is to depict the relationship
between applications and the business roles that use them within the
enterprise.

People in an organization interact with applications. During this
interaction, these people assume a specific role to perform a task; for
example, product buyer.

The mapping of the Application Component-Role relationship is an
important step as it enables the following to take place:

Assign usage of applications to the specific roles in the organization Understand the application security requirements of the business
services and processes supporting the function, and check these are in
line with current policy Support the gap analysis and determine whether any of the applications
are missing and as a result need to be created Define the application set used by a particular business role;
essential in any move to role-based computing

The Role/Application matrix is a two-dimensional table with Logical
Application Component on one axis and Role on the other axis.

</details>

<a id="tag_03_06_05_05"></a>
## 3.6.6.5. Application/Function Matrix

概念：应用/职能矩阵表达应用支持的业务职能。

适用条件：分析服务/流程支持与缺失应用。

逻辑关系：两轴为逻辑应用组件与Function；Function bounded by Service，服务由逻辑/物理应用组件实现。

决策方法：验证职能—服务—应用复合关系后判断覆盖。

制品及证据：应用/职能矩阵及复合路径证据。

适用边界：关系路径需验证，不能无依据生成直接实现映射。

来源块：C220-web-2025:05-architecture-content:b00419, C220-web-2025:05-architecture-content:b00420, C220-web-2025:05-architecture-content:b00421, C220-web-2025:05-architecture-content:b00422, C220-web-2025:05-architecture-content:b00423, C220-web-2025:05-architecture-content:b00424, C220-web-2025:05-architecture-content:b00425

<details><summary>展开本节完整英文来源</summary>

3.6.6.5. Application/Function Matrix

The purpose of the Application/Function matrix is to depict the
relationship between applications and business functions within the
enterprise.

Business functions are performed by organizational units. Some of the
business functions and services will be supported by applications. The
mapping of the Application Component-Function relationship is an
important step as it enables the following to take place:

Assign usage of applications to the business functions that are
supported by them Understand the application support requirements of the business
services and processes carried out Support the gap analysis and determine whether any of the applications
are missing and as a result need to be created Define the application set used by a particular business function

The Application/Function matrix is a two-dimensional table with Logical
Application Component on one axis and Function on the other axis.

The relationship between these two entities is a composite of a number
of metamodel relationships that need validating:

Function is bounded by Service Services are realized by Logical/Physical Application Components

</details>

<a id="tag_03_06_05_06"></a>
## 3.6.6.6. Application Interaction Matrix

概念：应用交互矩阵表示应用通信，相当于接口目录/通信图的矩阵投影。

适用条件：核查服务及组件间交互。

逻辑关系：双轴均可含应用服务、逻辑组件和物理组件；分别为服务消费服务、逻辑通信逻辑、物理通信物理。

决策方法：保留实体层次、端点及关系方向。

制品及证据：应用交互矩阵。

适用边界：不同层次关系不可互换；空单元格不自动证明无交互。

来源块：C220-web-2025:05-architecture-content:b00426, C220-web-2025:05-architecture-content:b00427, C220-web-2025:05-architecture-content:b00428, C220-web-2025:05-architecture-content:b00429, C220-web-2025:05-architecture-content:b00430, C220-web-2025:05-architecture-content:b00431

<details><summary>展开本节完整英文来源</summary>

3.6.6.6. Application Interaction Matrix

The purpose of the Application Interaction matrix is to depict
communications relationships between applications.

The mapping of the application interactions shows in matrix form the
equivalent of the Interface Catalog or an Application Communication
diagram.

The Application Interaction matrix is a two-dimensional table with
Application Service, Logical Application Component, and Physical
Application Component on both the rows and the columns of the table.

The relationships depicted by this matrix include:

Application Service consumes Application Service Logical Application Component communicates with Logical Application
Component Physical Application Component communicates with Physical
Application Component

</details>

<a id="tag_03_06_05_07"></a>
## 3.6.6.7. Application Communication Diagram

概念：应用通信图展示组件、接口及相关通信映射。

适用条件：表达逻辑应用交互。

逻辑关系：适用时接口关联数据实体、应用关联业务服务；只有架构相关时才展示中间技术。

决策方法：先表达逻辑通信，再判断附加数据/服务/技术是否回应关切。

制品及证据：应用通信图。

适用边界：不可把每个技术网络节点强制加入逻辑图。

来源块：C220-web-2025:05-architecture-content:b00432, C220-web-2025:05-architecture-content:b00433, C220-web-2025:05-architecture-content:b00434

<details><summary>展开本节完整英文来源</summary>

3.6.6.7. Application Communication Diagram

The purpose of the Application Communication diagram is to depict all
models and mappings related to communication between applications in the
metamodel entity.

It shows application components and interfaces between components.
Interfaces may be associated with data entities where appropriate.
Applications may be associated with business services where appropriate.
Communication should be logical and should only show intermediary
technology where it is architecturally relevant.

</details>

<a id="tag_03_06_05_08"></a>
## 3.6.6.8. Application and User Location Diagram

概念：应用和用户地点图展示使用、托管、开发、测试及发布的地理分布。

适用条件：识别应用重复/缺口、许可、支持与性能规划。

逻辑关系：地理用户、应用执行及薄客户端分布影响实例、许可、支持中心、管理工具、服务器及带宽估算。

决策方法：核查位置及用户活动，结合真实使用数据作估算。

制品及证据：应用/用户地点图及实例许可容量估算依据。

适用边界：图支持估算，不提供未经测量的工作量、容量或性能保证。

来源块：C220-web-2025:05-architecture-content:b00435, C220-web-2025:05-architecture-content:b00436, C220-web-2025:05-architecture-content:b00437, C220-web-2025:05-architecture-content:b00438, C220-web-2025:05-architecture-content:b00439, C220-web-2025:05-architecture-content:b00440, C220-web-2025:05-architecture-content:b00441, C220-web-2025:05-architecture-content:b00442

<details><summary>展开本节完整英文来源</summary>

3.6.6.8. Application and User Location Diagram

The Application and User Location diagram shows the geographical
distribution of applications. It can be used to show where applications
are used by the end user; the distribution of where the host application
is executed and/or delivered in thin client scenarios; the distribution
of where applications are developed, tested, and released; etc.

Analysis can reveal opportunities for rationalization, as well as
duplication and/or gaps.

The purpose of this diagram is to clearly depict the business locations
from which business users typically interact with the applications, but
also the hosting location of the application infrastructure.

The diagram enables:

Identification of the number of package instances needed to
sufficiently support the user population that may be spread out
geographically Estimation of the number and type of user licenses for the package or
other software Estimation of the level of support needed for the users and the
location of the support center Selection of system management tools, structure, and management system
required to support the enterprise users/customers/partners both locally
and remotely Appropriate planning for the technological components of the business,
namely server sizing and network bandwidth, etc. Performance considerations while implementing application and
technology architecture solutions

Users typically interact with applications in a variety of ways; for
example:

To support the operations of the business day-to-day To participate in the execution of a business process To access information (look-up, read) To develop the application To administer and maintain the application

</details>

<a id="tag_03_06_05_09"></a>
## 3.6.6.9. Application Use-Case Diagram

概念：应用用例连接应用服务消费者与提供者。

适用条件：描述和验证演员/角色与应用怎样及何时交互。

逻辑关系：消费者可为演员或其他应用服务；用例可随架构进展细化技术实现并用于设计。

决策方法：先验证功能交互，再按需要细化实现。

制品及证据：应用用例及交互验证。

适用边界：用例不是已部署或运行成功证据。

来源块：C220-web-2025:05-architecture-content:b00443, C220-web-2025:05-architecture-content:b00444, C220-web-2025:05-architecture-content:b00445, C220-web-2025:05-architecture-content:b00446

<details><summary>展开本节完整英文来源</summary>

3.6.6.9. Application Use-Case Diagram

An Application Use-Case diagram displays the relationships between
consumers and providers of application services. Application services
are consumed by actors or other application services and the Application
Use-Case diagram provides added richness in describing application
functionality by illustrating how and when that functionality is used.

The purpose of the Application Use-Case diagram is to help to describe
and validate the interaction between actors and their roles with
applications. As the architecture progresses, the use-case can evolve
from functional information to include technical realization detail.

Application use-cases can also be re-used in more detailed systems
design work.

</details>

<a id="tag_03_06_05_10"></a>
## 3.6.6.10. Enterprise Manageability Diagram

概念：企业可管理性图突出支持方案运行管理的应用及技术组件。

适用条件：发现IT服务管理重复、缺口及机会。

逻辑关系：它是应用通信图针对企业管理软件的过滤视图。

决策方法：保留共享通信实体，以运行管理关切过滤分析。

制品及证据：企业可管理性图及管理改进候选。

适用边界：过滤视图不是全部企业通信或真实管理能力认证。

来源块：C220-web-2025:05-architecture-content:b00447, C220-web-2025:05-architecture-content:b00448, C220-web-2025:05-architecture-content:b00449, C220-web-2025:05-architecture-content:b00450

<details><summary>展开本节完整英文来源</summary>

3.6.6.10. Enterprise Manageability Diagram

The Enterprise Manageability diagram shows how one or more applications
interact with application and technology components that support the
operational management of a solution.

This diagram is really a filter on the Application Communication
diagram, specifically for enterprise management class software.

Analysis can reveal duplication and gaps, and opportunities in the IT
service management operation of an organization.

</details>

<a id="tag_03_06_05_11"></a>
## 3.6.6.11. Process/Application Realization Diagram

概念：流程/应用实现图表达多应用执行流程的事件序列。

适用条件：分析批处理与实时交接以及时效和效率。

逻辑关系：在通信图上增加顺序约束与交接点，可揭示复杂序列及冗余流量。

决策方法：核查实际顺序、约束和交接，再评价简化机会。

制品及证据：流程/应用实现图。

适用边界：通信连线自身不等于执行顺序；机会不等于已证明改进收益。

来源块：C220-web-2025:05-architecture-content:b00451, C220-web-2025:05-architecture-content:b00452, C220-web-2025:05-architecture-content:b00453, C220-web-2025:05-architecture-content:b00454

<details><summary>展开本节完整英文来源</summary>

3.6.6.11. Process/Application Realization Diagram

The purpose of the Process/Application Realization diagram is to clearly
depict the sequence of events when multiple applications are involved in
executing a business process.

It enhances the Application Communication diagram by augmenting it with
any sequencing constraints, and hand-off points between batch and
real-time processing.

It would identify complex sequences that could be simplified, and
identify possible rationalization points in the architecture in order to
provide more timely information to business users. It may also identify
process efficiency improvements that may reduce interaction traffic
between applications.

</details>

<a id="tag_03_06_05_12"></a>
## 3.6.6.12. Software Engineering Diagram

概念：软件工程图从开发视角将应用分为包、模块、服务与操作。

适用条件：复杂开发/管理环境及迁移影响分析。

逻辑关系：内部结构支持阶段迁移和机会方案分析。

决策方法：按开发关切检查分解及受影响单元。

制品及证据：软件工程图。

适用边界：开发分解不替代业务功能、部署结构或详细程序设计。

来源块：C220-web-2025:05-architecture-content:b00455, C220-web-2025:05-architecture-content:b00456, C220-web-2025:05-architecture-content:b00457, C220-web-2025:05-architecture-content:b00458

<details><summary>展开本节完整英文来源</summary>

3.6.6.12. Software Engineering Diagram

The Software Engineering diagram breaks applications into packages,
modules, services, and operations from a development perspective.

It enables more detailed impact analysis when planning migration stages,
and analyzing opportunities and solutions.

It is ideal for application development teams and application management
teams when managing complex development environments.

</details>

<a id="tag_03_06_05_13"></a>
## 3.6.6.13. Application Migration Diagram

概念：应用迁移图显示基线到目标应用组件和接口的阶段映射。

适用条件：迁移成本估算与过渡安排。

逻辑关系：需识别临时应用、暂存区和并行运行等迁移基础设施。

决策方法：核对每阶段映射及临时支持需求。

制品及证据：应用迁移图、阶段映射及估算依据。

适用边界：细化映射提高估算基础，不自动提供真实成本或迁移验收。

来源块：C220-web-2025:05-architecture-content:b00459, C220-web-2025:05-architecture-content:b00460, C220-web-2025:05-architecture-content:b00461

<details><summary>展开本节完整英文来源</summary>

3.6.6.13. Application Migration Diagram

The Application Migration diagram identifies application migration from
baseline to target application components. It enables a more accurate
estimation of migration costs by showing precisely which applications
and interfaces need to be mapped between migration stages.

It would identify temporary applications, staging areas, and the
infrastructure required to support migrations (for example, parallel run
environments, etc).

</details>

<a id="tag_03_06_05_14"></a>
## 3.6.6.14. Software Distribution Diagram

概念：软件分布图表达物理应用在物理技术及地点上的分布。

适用条件：系统升级、应用整合和安装后运行维护。

逻辑关系：应用—托管技术—地点关联同时支持结构和维护理解。

决策方法：核查托管及维护边界。

制品及证据：软件分布图。

适用边界：不能从托管位置自动推断服务所有权或运维能力。

来源块：C220-web-2025:05-architecture-content:b00462, C220-web-2025:05-architecture-content:b00463, C220-web-2025:05-architecture-content:b00464, C220-web-2025:05-architecture-content:b00465

<details><summary>展开本节完整英文来源</summary>

3.6.6.14. Software Distribution Diagram

The Software Distribution diagram shows how application software is
structured and distributed across the estate. It is useful in systems
upgrade or application consolidation projects.

This diagram shows how physical applications are distributed across
physical technology and the location of that technology.

This enables a clear view of how the software is hosted, but also
enables managed operations staff to understand how that application
software is maintained once installed.

</details>

<a id="tag_03_06_06"></a>
## 3.6.7. Phase D: Technology Architecture

概念：D阶段可选技术架构制品。

适用条件：开发技术架构。

逻辑关系：目录、矩阵与图回应标准、平台和通信部署关切。

决策方法：按范围及目的选择。

制品及证据：技术制品选择记录。

适用边界：推荐清单不等于每次全部必交。

来源块：C220-web-2025:05-architecture-content:b00466, C220-web-2025:05-architecture-content:b00467

<details><summary>展开本节完整英文来源</summary>

3.6.7. Phase D: Technology Architecture

The following section describes catalogs, matrices, and diagrams that
may be created within Phase D (Technology Architecture) as described in
the TOGAF Standard — Architecture Development Method .

</details>

<a id="tag_03_06_06_01"></a>
## 3.6.7.1. Technology Standards Catalog

概念：技术标准目录记录已约定技术、版本、生命周期及刷新周期。

适用条件：企业标准治理及基线符合性分析。

逻辑关系：可含地点/业务域特定标准；现有标准应应用于技术组合以识别差异。

决策方法：核查标准实际约定范围及组合符合性。

制品及证据：Technology Service、Logical/Physical Technology Component标准目录和差异记录。

适用边界：标准快照不证明部署合规或获得豁免；候选技术不能冒充已约定标准。

来源块：C220-web-2025:05-architecture-content:b00468, C220-web-2025:05-architecture-content:b00469, C220-web-2025:05-architecture-content:b00470, C220-web-2025:05-architecture-content:b00471, C220-web-2025:05-architecture-content:b00472, C220-web-2025:05-architecture-content:b00473, C220-web-2025:05-architecture-content:b00474

<details><summary>展开本节完整英文来源</summary>

3.6.7.1. Technology Standards Catalog

The Technology Standards catalog documents the agreed standards for
technology across the enterprise covering technologies, and versions,
the technology lifecycles, and the refresh cycles for the technology.

Depending upon the organization, this may also include location or
business domain-specific standards information.

This catalog provides a snapshot of the enterprise standard technologies
that are or can be deployed, and also helps identify the discrepancies
across the enterprise.

The Technology Standards catalog contains the following metamodel
entities:

Technology Service Logical Technology Component Physical Technology Component

If technology standards are currently in place, apply these to the
Technology Portfolio catalog to gain a baseline view of compliance with
technology standards.

</details>

<a id="tag_03_06_06_02"></a>
## 3.6.7.2. Technology Portfolio Catalog

概念：技术组合目录维护在用硬件、基础设施软件及应用软件。

适用条件：技术产品版本生命周期和标准制定。

逻辑关系：通常为D起点；登记库提供基线/目标输入；按企业采用分类法如裁剪TRM归类。

决策方法：核查在用技术与分类适配，关联版本生命周期。

制品及证据：技术服务及逻辑/物理技术组件目录。

适用边界：参考TRM不等于企业实际产品清单或未经核实的最新版本。

来源块：C220-web-2025:05-architecture-content:b00475, C220-web-2025:05-architecture-content:b00476, C220-web-2025:05-architecture-content:b00477, C220-web-2025:05-architecture-content:b00478, C220-web-2025:05-architecture-content:b00479, C220-web-2025:05-architecture-content:b00480, C220-web-2025:05-architecture-content:b00481

<details><summary>展开本节完整英文来源</summary>

3.6.7.2. Technology Portfolio Catalog

The purpose of this catalog is to identify and maintain a list of all
the technology in use across the enterprise, including hardware,
infrastructure software, and application software. An agreed technology
portfolio supports the lifecycle management of technology products and
versions and also forms the basis for the definition of technology
standards.

The Technology Portfolio catalog provides a foundation on which to base
the remaining matrices and diagrams. It is typically the start point of
the Technology Architecture phase.

Technology registries and repositories also provide input into this
catalog from a baseline and target perspective.

Technologies in the catalog should be classified against the defined
taxonomy in use in the enterprise, such as the TOGAF TRM — see the TOGAF ® Series Guide: The TOGAF ® Technical Reference Model (TRM) — adapted as necessary to fit the
classification of technology products in use.

The Technology Portfolio catalog contains the following metamodel
entities:

Technology Service Logical Technology Component Physical Technology Component

</details>

<a id="tag_03_06_06_03"></a>
## 3.6.7.3. Application/Technology Matrix

概念：应用/技术矩阵记录应用到技术平台映射。

适用条件：与平台分解图共同分析平台支持。

逻辑关系：源列逻辑/物理应用组件、服务、逻辑/物理技术组件及物理技术组件实现物理应用组件关系。

决策方法：核对矩阵与平台图实体和映射一致。

制品及证据：应用/技术矩阵。

适用边界：保留源realizes措辞及方向，不能自动扩成逻辑技术实现所有应用关系。

来源块：C220-web-2025:05-architecture-content:b00482, C220-web-2025:05-architecture-content:b00483, C220-web-2025:05-architecture-content:b00484, C220-web-2025:05-architecture-content:b00485

<details><summary>展开本节完整英文来源</summary>

3.6.7.3. Application/Technology Matrix

The Application/Technology matrix documents the mapping of applications to technology platform. This matrix should be aligned with and complement one or more platform decomposition diagrams.

The Application/Technology matrix shows:

Logical/Physical Application Components Services, Logical Technology Components, and Physical Technology
Components Physical Technology Component realizes Physical Application
Component relationships

</details>

<a id="tag_03_06_06_04"></a>
## 3.6.7.4. Environments and Locations Diagram

概念：环境和地点图表达应用托管、技术/应用使用及用户交互地点。

适用条件：部署环境范围分析。

逻辑关系：应包括开发、预生产等非生产环境的存在及位置。

决策方法：分别核对生产和非生产环境。

制品及证据：环境与地点图。

适用边界：环境名字不能证明隔离、权限或可用性符合性。

来源块：C220-web-2025:05-architecture-content:b00486, C220-web-2025:05-architecture-content:b00487, C220-web-2025:05-architecture-content:b00488

<details><summary>展开本节完整英文来源</summary>

3.6.7.4. Environments and Locations Diagram

The Environments and Locations diagram depicts which locations host which applications, identifies what technologies and/or applications are used at which locations, and finally identifies the locations from which business users typically interact with the applications.

This diagram should also show the existence and location of different deployment environments, including non-production environments, such as
development and pre-production.

</details>

<a id="tag_03_06_06_05"></a>
## 3.6.7.5. Platform Decomposition Diagram

概念：平台分解图概览支持信息系统的基础设施平台。

适用条件：企业或特定职能/流程范围的技术分析。

逻辑关系：显示企业应用，可细分硬件软件的逻辑/物理技术组件；按范围加入跨平台通信并可选产品版本/CPU细节。

决策方法：选择概览或详细程度，核对平台到应用支持。

制品及证据：平台分解图及可选规格属性。

适用边界：非正式概览允许但不是已验证容量；所需细节由关切决定。

来源块：C220-web-2025:05-architecture-content:b00489, C220-web-2025:05-architecture-content:b00490, C220-web-2025:05-architecture-content:b00491, C220-web-2025:05-architecture-content:b00492, C220-web-2025:05-architecture-content:b00493

<details><summary>展开本节完整英文来源</summary>

3.6.7.5. Platform Decomposition Diagram

The Platform Decomposition diagram depicts the technology platform that supports the operations of the Information Systems Architecture. The diagram covers all aspects of the infrastructure platform and provides an overview of the enterprise’s technology platform. The diagram can be expanded to map the technology platform to appropriate application components within a specific functional or process area. This diagram may show specification details, such as product versions, number of
CPUs, etc. or simply could be an informal “eye-chart” providing an overview of the technical environment.

The diagram should clearly show the enterprise applications. The technology platform for each application area can further be decomposed
as follows:

Hardware: Logical Technology Components (with attributes) Physical Technology Components (with attributes) Software: Logical Technology Components (with attributes) Physical Technology Components (with attributes)

Depending upon the scope of the Enterprise Architecture work, additional
technology cross-platform information (e.g., communications, telco, and
video information) may be addressed.

</details>

<a id="tag_03_06_06_06"></a>
## 3.6.7.6. Processing Diagram

概念：处理图关注代码/配置部署单元及其技术部署。

适用条件：分析分组、交互和负载/容量需求。

逻辑关系：层分离、服务水平、地点与角色影响分组；单元含安装、运行状态执行、持久数据子单元，并部署于专用或共享技术。

决策方法：以实际配置与使用模式选择分组，核查协议连接及服务粒度影响。

制品及证据：处理图、安装/执行/持久化分解及负载依据。

适用边界：业务能力/服务/应用分组不同于它们身份合并；容量和工作量未知不能自动填充。

来源块：C220-web-2025:05-architecture-content:b00494, C220-web-2025:05-architecture-content:b00495, C220-web-2025:05-architecture-content:b00496, C220-web-2025:05-architecture-content:b00497, C220-web-2025:05-architecture-content:b00498, C220-web-2025:05-architecture-content:b00499, C220-web-2025:05-architecture-content:b00500, C220-web-2025:05-architecture-content:b00501

<details><summary>展开本节完整英文来源</summary>

3.6.7.6. Processing Diagram

The Processing diagram focuses on deployable units of code/configuration
and how these are deployed onto the technology platform. A deployment
unit represents the grouping of business capability, service, or
application components. The Processing diagram addresses the following:

Which set of application components need to be grouped to form a
deployment unit How one deployment unit connects/interacts with another (LAN, WAN, and
the applicable protocols) How application configuration and usage patterns generate load or
capacity requirements for different technology components

The organization and grouping of deployment units depends on separation
concerns of the presentation, business logic, and data store layers and
service-level requirements of the components. For example, the
presentation layer deployment unit is grouped based on the following:

Application components that provide user interface or user access
functions Application components that are differentiated by location and user
roles

There are several considerations to determine how application components
are grouped together. Each deployment unit is made up of sub-units, such
as:

Installation : part that holds the executable code or package
configuration (in case of packages) Execution : application component with its associated state at run
time Persistence : data that represents the persistent state of the
application component

Finally, these deployment units are deployed on either dedicated or
shared technology components (workstation, web server, application
server, or database server, etc.). It is important to note that
technology processing can influence and have implications on the
services definition and granularity.

</details>

<a id="tag_03_06_06_07"></a>
## 3.6.7.7. Networked Computing/Hardware Diagram

概念：网络计算/硬件图表达分布环境中逻辑应用的实际部署视图。

适用条件：开发/生产位置、安全、排障、性能、审计与变更分析。

逻辑关系：逻辑应用映射技术组件；范围可为应用、职能或企业，企业层也可不指定应用。

决策方法：核查实际部署与端点变化，按证据诊断和验证标准符合性。

制品及证据：部署图及实际位置/安全/审计证据。

适用边界：原文web/J2EE/三层当前叙述有时代性，不应视为2026所有应用强制结构；图不独自证明合规。

来源块：C220-web-2025:05-architecture-content:b00502, C220-web-2025:05-architecture-content:b00503, C220-web-2025:05-architecture-content:b00504, C220-web-2025:05-architecture-content:b00505, C220-web-2025:05-architecture-content:b00506

<details><summary>展开本节完整英文来源</summary>

3.6.7.7. Networked Computing/Hardware Diagram

Starting with the transformation to client-server systems from
mainframes and later with the advent of e-Business and J2EE, large
enterprises moved predominantly into a highly network-based distributed
network computing environment with firewalls and demilitarized zones.
Currently, most of the applications have a web front-end and, looking at
the deployment architecture of these applications, it is very common to
find three distinct layers in the network landscape; namely a web
presentation layer, a business logic or application layer, and a
back-end data store layer. It is common practice for applications to be
deployed and hosted in a shared and common infrastructure environment.

So it becomes highly critical to document the mapping between logical
applications and the technology components (e.g., server) that supports
the application both in the development and production environments. The
purpose of this diagram is to show the “as deployed” logical view of
logical application components in a distributed network computing
environment. The diagram is useful for the following reasons:

Enable understanding of which application is deployed where in the
distributed network computing environment Establishing authorization, security, and access to these technology
components Understand the Technology Architecture that supports the applications
during problem resolution and troubleshooting Isolate performance problems encountered by applications, determine
whether it is application code-related or technology platform-related,
and perform necessary upgrade to specific physical technology components Identify areas of optimization as and when newer technologies are
available which will eventually reduce cost Enable application/technology auditing and prove compliance with
enterprise technology standards Serve as an important tool to introduce changes to the Technology
Architecture, thereby supporting effective change management Establish traceability and changing application end-point address
while moving application either from a shared environment to a dedicated
environment or vice versa

The scope of the diagram can be appropriately defined to cover a
specific application, business function, or the entire enterprise. If
chosen to be developed at the enterprise level, then the network
computing landscape can be depicted in an application-agnostic way as
well.

</details>

<a id="tag_03_06_06_08"></a>
## 3.6.7.8. Network and Communications Diagram

概念：网络和通信图表达技术资产间物理发送/接收方式。

适用条件：实现由应用方案要求的逻辑客户/服务器连接。

逻辑关系：逻辑连接映射网络边界及基础设施，关注协议与容量。

决策方法：核查物理实现能支持所需逻辑通信。

制品及证据：网络边界、设施、协议与容量图。

适用边界：明确不描述信息格式或内容，不能由网络图补出数据契约。

来源块：C220-web-2025:05-architecture-content:b00507, C220-web-2025:05-architecture-content:b00508, C220-web-2025:05-architecture-content:b00509

<details><summary>展开本节完整英文来源</summary>

3.6.7.8. Network and Communications Diagram

The Network and Communications diagram describes the means of
communication — the method of sending and receiving information —
between these assets in the Technology Architecture; insofar as the
selection of package solutions in the preceding architectures put
specific requirements on the communications between the applications.

The Network and Communications diagram will take logical connections
between client and server components and identify network boundaries and
network infrastructure required to physically implement those
connections. It does not describe the information format or content, but
will address protocol and capacity issues.

</details>

<a id="tag_03_06_07"></a>
## 3.6.8. Phase E: Opportunities and Solutions

概念：E阶段可选机会与方案制品。

适用条件：识别实施机会与方案。

逻辑关系：项目上下文、收益、因素、差距和增量支持迁移规划。

决策方法：按规划关切选择。

制品及证据：E阶段制品选择记录。

适用边界：本节不规定自动排序或每次全部必交。

来源块：C220-web-2025:05-architecture-content:b00510, C220-web-2025:05-architecture-content:b00511

<details><summary>展开本节完整英文来源</summary>

3.6.8. Phase E: Opportunities and Solutions

The following section describes catalogs, matrices, and diagrams that
may be created within Phase E (Opportunities & Solutions) as described
in the TOGAF Standard — Architecture Development Method .

</details>

<a id="tag_03_06_07_01"></a>
## 3.6.8.1. Project Context Diagram

概念：项目上下文图界定工作包在更大转型路线图中的范围。

适用条件：项目组合管理和动员。

逻辑关系：工作包连接将新增、删除或影响的组织、职能、服务、流程、应用、数据和技术。

决策方法：核对影响对象及所属路线图。

制品及证据：工作包上下文与对象变更映射。

适用边界：范围图不证明项目授权、资源落实或业务收益。

来源块：C220-web-2025:05-architecture-content:b00512, C220-web-2025:05-architecture-content:b00513, C220-web-2025:05-architecture-content:b00514

<details><summary>展开本节完整英文来源</summary>

3.6.8.1. Project Context Diagram

A Project Context diagram shows the scope of a work package to be
implemented as a part of a broader transformation roadmap. The Project
Context diagram links a work package to the organizations, functions,
services, processes, applications, data, and technology that will be
added, removed, or impacted by the project.

The Project Context diagram is also a valuable tool for project
portfolio management and project mobilization.

</details>

<a id="tag_03_06_07_02"></a>
## 3.6.8.2. Benefits Diagram

概念：收益图按相对规模、收益和复杂度分类架构机会。

适用条件：相关者选择、优先级与顺序决定。

逻辑关系：机会分类提供决策输入。

决策方法：依据实际评价比较机会并记录选择。

制品及证据：收益图及评价证据。

适用边界：本节没有固定评分算法或阈值，不得自动制造收益评级。

来源块：C220-web-2025:05-architecture-content:b00515, C220-web-2025:05-architecture-content:b00516

<details><summary>展开本节完整英文来源</summary>

3.6.8.2. Benefits Diagram

The Benefits diagram shows opportunities identified in an architecture
definition, classified according to their relative size, benefit, and
complexity. This diagram can be used by stakeholders to make selection,
prioritization, and sequencing decisions on identified opportunities.

</details>

<a id="_implementation_factor_catalog"></a>
## 3.6.8.3. Implementation Factor Catalog

概念：实施因素目录记录影响实施和迁移计划的因素及推导。

适用条件：制定计划行动和约束。

逻辑关系：因素通常为风险、问题、假设、依赖、行动与影响；描述需连接推导出的行动/约束。

决策方法：逐因素核查来源、描述及计划含义。

制品及证据：实施因素目录、推导与行动/约束。

适用边界：假设不是已证实事实；样例图不强制规定真实风险值。

来源块：C220-web-2025:05-architecture-content:b00517, C220-web-2025:05-architecture-content:b00518, C220-web-2025:05-architecture-content:b00519, C220-web-2025:05-architecture-content:b00520, C220-web-2025:05-architecture-content:b00521, C220-web-2025:05-architecture-content:b00522, C220-web-2025:05-architecture-content:b00523, C220-web-2025:05-architecture-content:b00524

<details><summary>展开本节完整英文来源</summary>

3.6.8.3. Implementation Factor Catalog

The Implementation Factor catalog can be used
to document factors impacting the architecture Implementation and
Migration Plan.

The catalog should include a list of the factors to be considered, their
descriptions, and the deductions that indicate the actions or
constraints that have to be taken into consideration when formulating
the plans.

Factors typically include:

Risks Issues Assumptions Dependencies Actions Impacts

An example catalog is shown in Figure 3-5 .



Figure 3-5: Implementation Factor Catalog

</details>

<a id="_consolidated_gaps_solutions_and_dependencies_matrix"></a>
## 3.6.8.4. Consolidated Gaps, Solutions, and Dependencies Matrix

概念：合并差距、方案和依赖矩阵汇总各域差距并评价候选解决方式。

适用条件：形成工作包及E/F项目和迁移规划。

逻辑关系：一个方案/依赖可对应一个或多个差距；依赖驱动项目安排。

决策方法：整合差距后评估方案覆盖及依赖。

制品及证据：合并矩阵与工作包/项目追溯。

适用边界：潜在方案不等于选定或批准方案，差距合并不能丢失来源。

来源块：C220-web-2025:05-architecture-content:b00525, C220-web-2025:05-architecture-content:b00526, C220-web-2025:05-architecture-content:b00527, C220-web-2025:05-architecture-content:b00528, C220-web-2025:05-architecture-content:b00529, C220-web-2025:05-architecture-content:b00530

<details><summary>展开本节完整英文来源</summary>

3.6.8.4. Consolidated Gaps, Solutions, and Dependencies Matrix

The Consolidated Gaps, Solutions, and Dependencies matrix allows the architect to group the gaps identified in
the domain architecture gap analysis results and assess potential
solutions and dependencies to one or more gaps.

This matrix can be used as a planning tool when creating work packages.
The identified dependencies will drive the creation of projects and
migration planning in Phases E and F.

An example matrix is shown in Figure 3-6 .



Figure 3-6: Consolidated Gaps, Solutions, and Dependencies Matrix

</details>

<a id="_architecture_definition_increments_table"></a>
## 3.6.8.5. Architecture Definition Increments Table

概念：架构定义增量表把项目增量交付分配到各过渡架构。

适用条件：规划指定时间的企业架构状态。

逻辑关系：项目—增量—过渡架构—时间共同表达演进。

决策方法：核对阶段交付与状态之间的关系。

制品及证据：增量表及过渡状态计划。

适用边界：计划时间和交付分配不等于已交付、已验收状态。

来源块：C220-web-2025:05-architecture-content:b00531, C220-web-2025:05-architecture-content:b00532, C220-web-2025:05-architecture-content:b00533, C220-web-2025:05-architecture-content:b00534, C220-web-2025:05-architecture-content:b00535

<details><summary>展开本节完整英文来源</summary>

3.6.8.5. Architecture Definition Increments Table

The Architecture Definition Increments table
allows the architect to plan a series of Transition Architectures
outlining the status of the Enterprise Architecture at specified times.

A table should be drawn up, as shown in Figure 3-7 , listing the projects and then assigning their incremental deliverables across the Transition Architectures.



Figure 3-7: Architecture Definition Increments Table

</details>

<a id="_phase_f_migration_planning"></a>
## 3.6.9. Phase F: Migration Planning

概念：F阶段可选迁移规划制品。

适用条件：制定迁移计划。

逻辑关系：状态演进及价值风险评价支持选择。

决策方法：按决策需要选择制品。

制品及证据：F阶段选择记录。

适用边界：本节未定义强制评分或批准权限。

来源块：C220-web-2025:05-architecture-content:b00536, C220-web-2025:05-architecture-content:b00537

<details><summary>展开本节完整英文来源</summary>

3.6.9. Phase F: Migration Planning

The following section describes catalogs, matrices, and diagrams that may be created within Phase F (Migration Planning) as described in the TOGAF Standard — Architecture Development Method.

</details>

<a id="_transition_architecture_state_evolution_table"></a>
## 3.6.9.1. Transition Architecture State Evolution Table

概念：过渡架构状态演进表按企业分类法表达不同层次的拟议变换。

适用条件：展示SBB交付及对服务的影响。

逻辑关系：服务×过渡架构记录转换；示例new/retain、transition、replace，也可用绿/黄/红表示到位、转型、替换。

决策方法：核查所有SBB的服务交付/影响及进展标记。

制品及证据：服务状态表及SBB交付/影响映射。

适用边界：样例文字或颜色不能证明能力已验收，须区分计划状态与实际证据。

来源块：C220-web-2025:05-architecture-content:b00538, C220-web-2025:05-architecture-content:b00539, C220-web-2025:05-architecture-content:b00540, C220-web-2025:05-architecture-content:b00541, C220-web-2025:05-architecture-content:b00542, C220-web-2025:05-architecture-content:b00543, C220-web-2025:05-architecture-content:b00544, C220-web-2025:05-architecture-content:b00545

<details><summary>展开本节完整英文来源</summary>

3.6.9.1. Transition Architecture State Evolution Table

The Transition Architecture State Evolution table allows the architect to show the proposed state of the architectures at various levels using the defined taxonomy (e.g., the TOGAF TRM).

A table should be drawn, listing the services from the taxonomy used in the enterprise, the Transition Architectures, and proposed transformations, as shown in Figure 3-8 .

All SBBs should be described with respect to their delivery and impact on these services. They should also be marked to show the progression of the Enterprise Architecture. In the example, where target capability has been reached, this is shown as “new” or “retain”; where capability is transitioned to a new solution, this is marked as “transition”; and
where a capability is to be replaced, this is marked as “replace”.



Figure 3-8: Transition Architecture State Evolution Table

Another technique (not shown here) is to use color coding in the matrix;
for example:

Green: service SBB in place (either new or retained) Yellow: service being transitioned into a new solution Red: service to be replaced

</details>

<a id="_business_value_and_risk_matrix"></a>
## 3.6.9.2. Business Value and Risk Matrix

概念：业务价值/风险矩阵以分别加权的价值和风险指数评价项目。

适用条件：比较机会的选择及排序。

逻辑关系：价值可考虑原则、财务、战略和竞争；风险可考虑规模复杂性、技术、组织容量及失败影响。

决策方法：高级管理层在知道选项前制定并批准指数、准则及权重，再应用真实证据。

制品及证据：已批准准则/权重、评价矩阵与决定。

适用边界：不得从样例自动产生分数、组织容量或管理批准；先知选项后调权重违背本节决策顺序。

来源块：C220-web-2025:05-architecture-content:b00546, C220-web-2025:05-architecture-content:b00547, C220-web-2025:05-architecture-content:b00548, C220-web-2025:05-architecture-content:b00549, C220-web-2025:05-architecture-content:b00550

<details><summary>展开本节完整英文来源</summary>

3.6.9.2. Business Value and Risk Matrix

A Business Value and Risk Matrix shows a value index dimension and a risk index dimension.
An example is shown in Figure 3-9 . The value index should include criteria such as compliance to principles, financial contribution, strategic alignment, and competitive position. The risk index should include
criteria such as size and complexity, technology, organizational capacity, and impact of a failure. Each criterion should be assigned an individual weight.

The index and its criteria and weighting should be developed and approved by senior management. It is important to establish the decision-making criteria before the options are known.



Figure 3-9: Sample Project Assessment with Respect to Business Value and Risk

</details>

<a id="tag_03_06_08"></a>
## 3.6.10. Requirements Management

概念：需求管理可创建的制品入口。

适用条件：贯穿架构开发的需求管理。

逻辑关系：下一节需求目录支持目标和适用性检查。

决策方法：按持续管理需要选择。

制品及证据：需求管理制品选择记录。

适用边界：源称Requirements Management phase，不应解为A—H以外的单次Phase I。

来源块：C220-web-2025:05-architecture-content:b00551, C220-web-2025:05-architecture-content:b00552

<details><summary>展开本节完整英文来源</summary>

3.6.10. Requirements Management

The following section describes catalogs, matrices, and diagrams that
may be created within the Requirements Management phase as described in
the TOGAF Standard — Architecture Development Method .

</details>

<a id="tag_03_06_08_01"></a>
## 3.6.10.1. Requirements Catalog

概念：需求目录记录企业为达目标需要做的事。

适用条件：架构需求追溯及适合目的质量保证。

逻辑关系：架构参与需求通常经E范围化变革实施；目录含Requirement、Assumption、Constraint与Gap。

决策方法：核对架构是否满足已识别需求，并分别标记需求、假设、约束、差距。

制品及证据：需求目录、目标追溯及质量核查。

适用边界：假设不等于验证过的需求，目录记录不证明全部需求已满足或变革已实施。

来源块：C220-web-2025:05-architecture-content:b00553, C220-web-2025:05-architecture-content:b00554, C220-web-2025:05-architecture-content:b00555, C220-web-2025:05-architecture-content:b00556

<details><summary>展开本节完整英文来源</summary>

3.6.10.1. Requirements Catalog

The Requirements catalog captures things that the enterprise needs to do
to meet its objectives. Requirements generated from architecture
engagements are typically implemented through change initiatives
identified and scoped during Phase E (Opportunities & Solutions).
Requirements can also be used as a quality assurance tool to ensure that
a particular architecture is fit-for-purpose (i.e., the architecture can
meet all identified requirements).

The Requirements catalog contains the following metamodel entities:

Requirement Assumption Constraint Gap

</details>

<a id="chap04"></a>
## 4. Architecture Deliverables

概念：本章描述ADM引用的交付物。

适用条件：查阅架构工作的正式成果。

逻辑关系：后续导言与条目给出典型起点。

决策方法：结合ADM和组织过程选择。

制品及证据：交付物定义。

适用边界：本导言未规定全部交付物无条件必交。

来源块：C220-web-2025:05-architecture-content:b00557, C220-web-2025:05-architecture-content:b00558

<details><summary>展开本节完整英文来源</summary>

4. Architecture Deliverables

This chapter provides descriptions of deliverables referenced in the
ADM.

</details>

<a id="tag_04_01"></a>
## 4.1. Introduction

概念：交付物通常是契约性或正式架构工作产物。

适用条件：组织项目/过程管理约束下的ADM执行。

逻辑关系：ADM产出可成为别处输入，也可消费外部产出；典型清单是组织裁剪起点。

决策方法：考虑企业管理框架后裁剪交付物及活动。

制品及证据：交付物输入/输出清单与裁剪依据。

适用边界：表4-1是典型基线，不能忽略契约和组织管理约束；源存在编辑残留字符串。

来源块：C220-web-2025:05-architecture-content:b00559, C220-web-2025:05-architecture-content:b00560, C220-web-2025:05-architecture-content:b00561, C220-web-2025:05-architecture-content:b00562, C220-web-2025:05-architecture-content:b00563, C220-web-2025:05-architecture-content:b00564

<details><summary>展开本节完整英文来源</summary>

4.1. Introduction

This chapter defines the deliverables that will typically be consumed and produced across the TOGAF ADM cycle. As (architecture deliverablesdeliverables are typically the contractual or formal work products of an architecture project, it is likely that these deliverables will be constrained or altered by any overarching project or process management for the enterprise (such as CMMI ® , PRINCE2 ® , PMBOK ® , or MSP ® ).

This chapter therefore is intended to provide a typical baseline of
architecture deliverables in order to better define the activities
required in the ADM and act as a starting point for tailoring within a
specific organization.

The TOGAF Content Framework (see Chapter 1, Introduction )
identifies deliverables that are produced as outputs
from executing the ADM cycle and potentially consumed as inputs at other
points in the ADM. Other deliverables may be produced elsewhere and
consumed by the ADM.

Deliverables produced by executing the ADM are shown in Table 4-1 .

Table 4-1:  Architecture Deliverables Produced by Executing the ADM Deliverable Output from…​ Input to…​ Architecture Building Blocks (see Section 4.2.1, “Architecture Building Blocks” ) B, C, D, F, H A, B, C, D, E, F, G, H Architecture Contract (see Section 4.2.2, “Architecture Contract” ) G G, H Architecture Definition Document (see Section 4.2.3, “Architecture Definition Document” ) A, B, C, D, E, F B, C, D, E, F, G, H Architecture Principles (see Section 4.2.4, “Architecture Principles” ) Preliminary, A, B, C, D Preliminary, A, B, C, D, E, F, G, H Architecture Repository (see Section 4.2.5, “Architecture Repository” ) Preliminary, A, B, C, D, Preliminary, A, B, C, D, E, F, G, H Requirements Management Architecture Requirements Specification (see Section 4.2.6, “Architecture Requirements Specification” ) B, C, D, E, F, Requirements Management C, D, Requirements Management Architecture Roadmap (see Section 4.2.7, “Architecture Roadmap” ) B, C, D, E, F B, C, D, E, F Architecture Vision (see Section 4.2.8, “Architecture Vision” ) A, E B, C, D, E, F, G, H, Requirements Management Business Principles, Business Goals, and Business Drivers (see Section 4.2.9, “Business Principles, Business Goals, and Business Drivers” ) Preliminary, A, B A, B Capability Assessment (see Section 4.2.10, “Capability Assessment” ) A, E B, C, D, E, F Change Request (see Section 4.2.11, “Change Request” ) F, G, H H Communications Plan (see Section 4.2.12, “Communications Plan” ) A B, C, D, E, F Compliance Assessment (see Section 4.2.13, “Compliance Assessment” ) G H Implementation and Migration Plan (see Section 4.2.14, “Implementation and Migration Plan” ) E, F F Implementation Governance Model (see Section 4.2.15, “Implementation Governance Model” ) F G, H Organizational Model for Enterprise Architecture (see Section 4.2.16, “Organizational Model for Enterprise Architecture” ) Preliminary Preliminary, A, B, C, D, E, F, G, H, Requirements Management Request for Architecture Work (see Section 4.2.17, “Request for Architecture Work” ) Preliminary, F, H A, G Requirements Impact Assessment (see Section 4.2.18, “Requirements Impact Assessment” ) Requirements Management Requirements Management Solution Building Blocks (see Section 4.2.19, “Solution Building Blocks” ) G A, B, C, D, E, F, G Statement of Architecture Work (see Section 4.2.20, “Statement of Architecture Work” ) A, B, C, D, E, F, G, H B, C, D, E, F,
G, H, Requirements Management Tailored Architecture Framework (see Section 4.2.21, “Tailored Architecture Framework” ) Preliminary, A Preliminary, A, B, C, D, E, F, G, H, Requirements Management

</details>

<a id="tag_04_02"></a>
## 4.2. Deliverable Descriptions

概念：交付物描述是示例，应仔细考虑每个元素。

适用条件：确定具体交付内容。

逻辑关系：可用外部引用避免复制，如请求引用战略计划标题。

决策方法：逐元素判断包含、引用或有理由省略，评估下游影响。

制品及证据：交付内容范围、外部引用及省略依据。

适用边界：不要求逐字照做或全放同一文件，但省略输入/输出可能影响下游。

来源块：C220-web-2025:05-architecture-content:b00565, C220-web-2025:05-architecture-content:b00566, C220-web-2025:05-architecture-content:b00567, C220-web-2025:05-architecture-content:b00568

<details><summary>展开本节完整英文来源</summary>

4.2. Deliverable Descriptions

The following sections provide example descriptions of deliverables
referenced in the ADM.

Note that not all the content described here need be contained in a
particular deliverable. Rather, it is recommended that external
references be used where possible; for example, the strategic plans of a
business should not be copied into a Request for Architecture Work, but
rather the title of the strategic plans should be referenced.

Also, it is not suggested that these descriptions should be followed to
the letter. However, each element should be considered carefully;
ignoring any input or output item may cause problems downstream.

</details>

<a id="tag_04_02_01"></a>
## 4.2.1. Architecture Building Blocks

概念：ABB交付内容是企业资料库中的架构文档和模型。

适用条件：复用或消费架构构建块。

逻辑关系：详细特征见第5章。

决策方法：按逻辑架构需要选择并追溯资料库资产。

制品及证据：资料库架构文档、模型及ABB引用。

适用边界：ABB不同于实现特定的SBB，不以文件存在证明可复用。

来源块：C220-web-2025:05-architecture-content:b00569, C220-web-2025:05-architecture-content:b00570

<details><summary>展开本节完整英文来源</summary>

4.2.1. Architecture Building Blocks

Architecture documentation and models from the enterprise’s Architecture
Repository; see Chapter 5, Building Blocks .

</details>

<a id="tag_04_02_02"></a>
## 4.2.2. Architecture Contract

概念：架构契约的条目标题。

适用边界：目的及内容分别在子节，无独立额外要求。

来源块：C220-web-2025:05-architecture-content:b00571

<details><summary>展开本节完整英文来源</summary>

4.2.2. Architecture Contract

</details>

<a id="tag_04_02_02_01"></a>
## 4.2.2.1. Purpose

概念：架构契约是开发伙伴与赞助方就交付物、质量和适合目的达成的共同协议。

适用条件：通过架构治理管理开发与实施。

逻辑关系：持续监测、原则标准需求遵循、风险、责任纪律和治理机构权限/范围共同支撑执行。

决策方法：核对协议双方、治理机构权限及范围，再建立监测审计机制。

制品及证据：共同协议、监测审计及责任/权限证据。

适用边界：契约文本不能独自保证韧性或遵从；实际决策权限必须由真实组织输入证实。

来源块：C220-web-2025:05-architecture-content:b00572, C220-web-2025:05-architecture-content:b00573, C220-web-2025:05-architecture-content:b00574, C220-web-2025:05-architecture-content:b00575

<details><summary>展开本节完整英文来源</summary>

4.2.2.1. Purpose

Architecture Contracts are the joint agreements between development
partners and sponsors on the deliverables, quality, and
fitness-for-purpose of an architecture. Successful implementation of
these agreements will be delivered through effective Architecture
Governance (see the TOGAF Standard — EA Capability and Governance ).

By implementing a governed approach to the management of contracts, the following will be ensured:

A system of continuous monitoring to check integrity, changes,
decision-making, and audit of all architecture-related activities within the organization Adherence to the principles, standards, and requirements of the
existing or developing architectures Identification of risks in all aspects of the development and
implementation of the architecture(s) covering the internal development
against accepted standards, policies, technologies, and products as well as the operational aspects of the architectures such that the
organization can continue its business within a resilient environment A set of processes and practices that ensure accountability,
responsibility, and discipline with regard to the development and usage
of all architectural artifacts A formal understanding of the governance organization responsible for the contract, their level of authority, and scope of the architecture under the governance of this body

</details>

<a id="tag_04_02_02_02"></a>
## 4.2.2.2. Content

概念：源分别给架构设计开发契约与业务用户契约的典型内容。

适用条件：按契约对象确定条款。

逻辑关系：前者含原则需求、过程角色、目标度量、阶段交付、共同计划；后者含采用方、业务度量和服务架构/SLA；均含背景、性质、范围、符合性和时间。

决策方法：选择适用契约类型，逐条确认范围、责任、交付和指标。

制品及证据：已约定契约、工作计划、时间窗、业务/交付指标及适用SLA。

适用边界：典型条款并非填入即被双方接受，业务用户契约不得自动套用开发流程职责。

来源块：C220-web-2025:05-architecture-content:b00576, C220-web-2025:05-architecture-content:b00577, C220-web-2025:05-architecture-content:b00578, C220-web-2025:05-architecture-content:b00579, C220-web-2025:05-architecture-content:b00580, C220-web-2025:05-architecture-content:b00581

<details><summary>展开本节完整英文来源</summary>

4.2.2.2. Content

Typical contents of an Architecture Design and Development Contract are:

Introduction and background The nature of the agreement Scope of the architecture Architecture and strategic principles and requirements Conformance requirements Architecture development and management process and roles Target Architecture measures Defined phases of deliverables Prioritized joint workplan Time window(s) Architecture delivery and business metrics

Typical contents of a Business Users' Architecture Contract are:

Introduction and background The nature of the agreement Scope Strategic requirements Conformance requirements Architecture adopters Time window Architecture business metrics Service architecture (includes Service-Level Agreement (SLA))

For more detail on the use of Architecture Contracts, see the TOGAF Standard — EA Capability and Governance .

</details>

<a id="tag_04_02_03"></a>
## 4.2.3. Architecture Definition Document

概念：架构定义文档的条目标题。

适用边界：定义及内容在子节。

来源块：C220-web-2025:05-architecture-content:b00582

<details><summary>展开本节完整英文来源</summary>

4.2.3. Architecture Definition Document

</details>

<a id="tag_04_02_03_01"></a>
## 4.2.3.1. Purpose

概念：架构定义文档容纳核心制品和关联信息，表达方案的定性意图。

适用条件：全域业务/数据/应用/技术及基线/过渡/目标状态。

逻辑关系：过渡架构是基线与目标之间有架构意义的状态；定义文档与量化需求规格互补。

决策方法：明确相关状态与定性意图，并把可测标准交给需求规格。

制品及证据：架构定义文档、各域各状态制品及互补需求规格。

适用边界：文档不是只含目标架构；意图表达不能替代可测验实现要求。

来源块：C220-web-2025:05-architecture-content:b00583, C220-web-2025:05-architecture-content:b00584, C220-web-2025:05-architecture-content:b00585, C220-web-2025:05-architecture-content:b00586, C220-web-2025:05-architecture-content:b00587

<details><summary>展开本节完整英文来源</summary>

4.2.3.1. Purpose

The Architecture Definition Document is the deliverable container for
the core architectural artifacts created during a project and for
important related information. The Architecture Definition Document
spans all architecture domains (Business, Data, Application, and
Technology) and also examines all relevant states of the architecture
(Baseline, Transition, and Target).

A Transition Architecture shows the enterprise at an architecturally
significant state between the Baseline and Target Architectures.
Transition Architectures are used to describe transitional Target
Architectures necessary for effective realization of the Target
Architecture.

The Architecture Definition Document is a companion to the Architecture
Requirements Specification, with a complementary objective:

The Architecture Definition Document provides a qualitative view of
the solution and aims to communicate the intent of the architects The Architecture Requirements Specification provides a quantitative
view of the solution, stating measurable criteria that must be met
during the implementation of the architecture

</details>

<a id="tag_04_02_03_02"></a>
## 4.2.3.2. Content

概念：典型定义文档包含范围、目标约束、原则、基线、各状态模型、理由与资料库映射。

适用条件：沟通和维护完整架构定义。

逻辑关系：复用评估、差距/影响分析及过渡定义把各域状态连入景观、参考模型和标准。

决策方法：核对模型状态及方法理由，追溯资料库并分析差距影响。

制品及证据：定义文档及基线/过渡/目标模型、理由、复用/差距/影响评估。

适用边界：不要求无关状态或重复外部全文；引用须能定位实际模型。

来源块：C220-web-2025:05-architecture-content:b00588, C220-web-2025:05-architecture-content:b00589, C220-web-2025:05-architecture-content:b00590

<details><summary>展开本节完整英文来源</summary>

4.2.3.2. Content

Typical contents of an Architecture Definition Document are:

Scope Goals, objectives, and constraints Architecture Principles Baseline Architecture Architecture models (for each state to be modeled): Business Architecture models Data Architecture models Application Architecture models Technology Architecture models Rationale and justification for architectural approach Mapping to Architecture Repository: Mapping to Architecture Landscape Mapping to reference models Mapping to standards Re-use assessment Gap analysis Impact assessment Transition Architecture: Definition of transition states Business Architecture for each transition state Data Architecture for each transition state Application Architecture for each transition state Technology Architecture for each transition state

</details>

<a id="tag_04_02_04"></a>
## 4.2.4. Architecture Principles

概念：架构原则的条目标题。

适用边界：原则性质与参考域在子节。

来源块：C220-web-2025:05-architecture-content:b00591

<details><summary>展开本节完整英文来源</summary>

4.2.4. Architecture Principles

</details>

<a id="tag_04_02_04_01"></a>
## 4.2.4.1. Purpose

概念：原则是持久且较少修改的通用规则和指导。

适用条件：支持组织履行使命。

逻辑关系：原则属于从价值到行动/结果的结构化思想集合。

决策方法：用组织使命检验原则并审慎管理改变。

制品及证据：组织原则及使命关联。

适用边界：原则不是孤立临时指标或自动实现结果。

来源块：C220-web-2025:05-architecture-content:b00592, C220-web-2025:05-architecture-content:b00593, C220-web-2025:05-architecture-content:b00594

<details><summary>展开本节完整英文来源</summary>

4.2.4.1. Purpose

Principles are general rules and guidelines, intended to be enduring and seldom amended, that inform and support the way in which an organization sets about fulfilling its mission.

In their turn, principles may be just one element in a structured set of ideas that collectively define and guide the organization, from values through to actions and results.

</details>

<a id="tag_04_02_04_02"></a>
## 4.2.4.2. Content

概念：源引用ADM Techniques的业务、数据、应用、技术原则指导和通用实例。

适用条件：选择/发展组织架构原则。

逻辑关系：各域原则参照技巧卷后裁剪。

决策方法：核查组织适用性，不直接把通用原则当已批准政策。

制品及证据：跨域原则及来源引用。

适用边界：本节不重复完整原则内容，也不证明原则被组织接受。

来源块：C220-web-2025:05-architecture-content:b00595, C220-web-2025:05-architecture-content:b00596, C220-web-2025:05-architecture-content:b00597

<details><summary>展开本节完整英文来源</summary>

4.2.4.2. Content

See the TOGAF Standard — ADM Techniques for guidelines and a detailed set of generic Architecture
Principles, including:

Business principles (see the TOGAF Standard — ADM Techniques ) Data principles (see the TOGAF Standard — ADM Techniques ) Application principles (see the TOGAF Standard — ADM Techniques ) Technology principles (see the TOGAF Standard — ADM Techniques )

</details>

<a id="tag_04_02_05"></a>
## 4.2.5. Architecture Repository

概念：架构资料库的条目标题。

适用边界：目的和详细内容引用在子节。

来源块：C220-web-2025:05-architecture-content:b00598

<details><summary>展开本节完整英文来源</summary>

4.2.5. Architecture Repository

</details>

<a id="tag_04_02_05_01"></a>
## 4.2.5.1. Purpose

概念：资料库保存企业架构相关项目，支持管理交付物、寻找复用资产和发布成果。

适用条件：企业多架构项目协作。

逻辑关系：项目成果与共享资产和相关者发布相连。

决策方法：明确保存、检索、复用及发布流程。

制品及证据：资料库及项目交付/复用/发布记录。

适用边界：存储存在不保证质量、权限或有效复用。

来源块：C220-web-2025:05-architecture-content:b00599, C220-web-2025:05-architecture-content:b00600

<details><summary>展开本节完整英文来源</summary>

4.2.5.1. Purpose

The Architecture Repository acts as a holding area for all
architecture-related projects within the enterprise. The repository
allows projects to manage their deliverables, locate re-usable assets, and publish outputs to stakeholders and other interested parties.

</details>

<a id="tag_04_02_05_02"></a>
## 4.2.5.2. Content

概念：资料库具体内容见第7章。

适用条件：配置资料库。

逻辑关系：交付物描述引用资料库详细结构。

决策方法：按第7章区分资产类型和管理机制。

制品及证据：资料库结构引用。

适用边界：本节仅交叉引用，不新增字段或固定存储工具。

来源块：C220-web-2025:05-architecture-content:b00601, C220-web-2025:05-architecture-content:b00602

<details><summary>展开本节完整英文来源</summary>

4.2.5.2. Content

See Chapter 7, Architecture Repository for a detailed
description of the content of an Architecture Repository.

</details>

<a id="tag_04_02_06"></a>
## 4.2.6. Architecture Requirements Specification

概念：架构需求规格的条目标题。

适用边界：定量目的与内容在子节。

来源块：C220-web-2025:05-architecture-content:b00603

<details><summary>展开本节完整英文来源</summary>

4.2.6. Architecture Requirements Specification

</details>

<a id="tag_04_02_06_01"></a>
## 4.2.6.1. Purpose

概念：架构需求规格以量化陈述界定实施为遵守架构必须做的事。

适用条件：实施契约或更详细架构定义契约。

逻辑关系：与表达定性意图的架构定义文档互补，陈述可测的实现标准。

决策方法：把实现符合性转为可测验要求并追溯定义意图。

制品及证据：量化需求规格及契约引用。

适用边界：不能用架构图替代测验标准，未知恢复/一致性目标不得凭空量化。

来源块：C220-web-2025:05-architecture-content:b00604, C220-web-2025:05-architecture-content:b00605, C220-web-2025:05-architecture-content:b00606, C220-web-2025:05-architecture-content:b00607

<details><summary>展开本节完整英文来源</summary>

4.2.6.1. Purpose

The Architecture Requirements Specification provides a set of
quantitative statements that outline what an implementation project must
do in order to comply with the architecture. An Architecture
Requirements Specification will typically form a major component of an
implementation contract or contract for more detailed Architecture
Definition.

As mentioned above, the Architecture Requirements Specification is a
companion to the Architecture Definition Document, with a complementary
objective:

The Architecture Definition Document provides a qualitative view of
the solution and aims to communicate the intent of the architect The Architecture Requirements Specification provides a quantitative
view of the solution, stating measurable criteria that must be met
during the implementation of the architecture

</details>

<a id="tag_04_02_06_02"></a>
## 4.2.6.2. Content

概念：典型需求规格含成功度量、架构要求、业务/应用服务契约及实施指南规格标准。

适用条件：约定实施符合性。

逻辑关系：互操作与IT服务管理需求、约束和假设共同限定实现。

决策方法：区分已约定契约、强制要求、实施指导及待验证假设。

制品及证据：需求规格、成功度量、服务契约、实施/互操作/ITSM要求。

适用边界：假设不可充作成功证据；典型项按范围考虑，不机械补值。

来源块：C220-web-2025:05-architecture-content:b00608, C220-web-2025:05-architecture-content:b00609, C220-web-2025:05-architecture-content:b00610

<details><summary>展开本节完整英文来源</summary>

4.2.6.2. Content

Typical contents of an Architecture Requirements Specification are:

Success measures Architecture requirements Business service contracts Application service contracts Implementation guidelines Implementation specifications Implementation standards Interoperability requirements IT Service Management requirements Constraints Assumptions

</details>

<a id="tag_04_02_07"></a>
## 4.2.7. Architecture Roadmap

概念：架构路线图的条目标题。

适用边界：目的和内容分别在子节。

来源块：C220-web-2025:05-architecture-content:b00611

<details><summary>展开本节完整英文来源</summary>

4.2.7. Architecture Roadmap

</details>

<a id="tag_04_02_07_01"></a>
## 4.2.7.1. Purpose

概念：路线图按时间排列实现目标的工作包，并显明各阶段业务价值。

适用条件：从基线经必要过渡到目标的变革规划。

逻辑关系：B/C/D可识别部件，E/F逐步发展路线图。

决策方法：核对工作包、价值、过渡状态及时间进展。

制品及证据：工作包路线图与过渡架构。

适用边界：路线图计划不等于可执行项目已立项或收益已实现。

来源块：C220-web-2025:05-architecture-content:b00612, C220-web-2025:05-architecture-content:b00613

<details><summary>展开本节完整英文来源</summary>

4.2.7.1. Purpose

The Architecture Roadmap lists individual work packages that will
realize the Target Architecture and lays them out on a timeline to show
progression from the Baseline Architecture to the Target Architecture.
The Architecture Roadmap highlights individual work packages' business
value at each stage. Transition Architectures necessary to effectively
realize the Target Architecture are identified as intermediate steps.
The Architecture Roadmap is incrementally developed throughout Phases E
and F, and informed by readily identifiable roadmap components from
Phase B, C, and D within the ADM.

</details>

<a id="tag_04_02_07_02"></a>
## 4.2.7.2. Content

概念：路线图内容包括工作包组合、因素目录、合并差距方案依赖、过渡架构和实施建议。

适用条件：追溯机会、架构定义/需求规格、业务价值及迁移选择。

逻辑关系：工作包功能要求和依赖连到机会；实施建议含有效性准则、风险问题与SBB。

决策方法：核对各包依赖/来源和方案覆盖，保持风险/假设与输入可追溯。

制品及证据：路线图、工作包说明、因素/差距矩阵和建议。

适用边界：此处因素列Inputs，3.6.8.3列Impacts，保留源差别而非默默强制同义。

来源块：C220-web-2025:05-architecture-content:b00614, C220-web-2025:05-architecture-content:b00615, C220-web-2025:05-architecture-content:b00616

<details><summary>展开本节完整英文来源</summary>

4.2.7.2. Content

Typical contents of an Architecture Roadmap are:

Work package portfolio: Work package description (name, description, objectives,
deliverables) Functional requirements Dependencies Relationship to opportunity Relationship to Architecture Definition Document and Architecture
Requirements Specification Business value Implementation Factor catalog, including: Risks Issues Assumptions Dependencies Actions Inputs Consolidated Gaps, Solutions, and Dependencies matrix, including: Architecture domain Gap Potential solutions Dependencies Any Transition Architectures Implementation recommendations: Criteria measures of effectiveness of projects Risks and issues Solution Building Blocks

</details>

<a id="tag_04_02_08"></a>
## 4.2.8. Architecture Vision

概念：架构愿景的条目标题。

适用边界：目的及典型内容在子节。

来源块：C220-web-2025:05-architecture-content:b00617

<details><summary>展开本节完整英文来源</summary>

4.2.8. Architecture Vision

</details>

<a id="tag_04_02_08_01"></a>
## 4.2.8.1. Purpose

概念：愿景早期概述成功部署目标架构带来的企业变化。

适用条件：关键相关者正式同意预期结果。

逻辑关系：早期结果共识使架构师聚焦可行性验证，也支持完整定义的摘要沟通。

决策方法：取得对结果的正式共识，再细化所需可行性证据。

制品及证据：架构愿景与共识记录。

适用边界：愿景同意不等于目标实现已证明或细节全部批准。

来源块：C220-web-2025:05-architecture-content:b00618, C220-web-2025:05-architecture-content:b00619

<details><summary>展开本节完整英文来源</summary>

4.2.8.1. Purpose

The Architecture Vision is created early on in the ADM cycle. It
provides a summary of the changes to the enterprise that will accrue
from successful deployment of the Target Architecture. The purpose of
the Architecture Vision is to provide key stakeholders with a formally
agreed outcome. Early agreement on the outcome enables the architects to
focus on the detail necessary to validate feasibility. Providing an
Architecture Vision also supports stakeholder communication by providing
a summary version of the full Architecture Definition.

</details>

<a id="tag_04_02_08_02"></a>
## 4.2.8.2. Content

概念：愿景典型内容为问题、相关者关切、业务情景/问题和工作说明目标。

适用条件：形成高层愿景与初步全域表达。

逻辑关系：请求所需摘要及初步业务/数据/应用/技术可含价值链、方案概念、映射需求和定义草案引用。

决策方法：核对关切问题与摘要及需求映射一致。

制品及证据：愿景、相关情景、摘要图及定义草案引用。

适用边界：初步图和映射不能当最终设计或量化验收标准。

来源块：C220-web-2025:05-architecture-content:b00620, C220-web-2025:05-architecture-content:b00621, C220-web-2025:05-architecture-content:b00622

<details><summary>展开本节完整英文来源</summary>

4.2.8.2. Content

Typical contents of an Architecture Vision are:

Problem description: Stakeholders and their concerns List of Business Scenarios to be addressed List of issues/scenarios to be addressed Objective of the Statement of Architecture Work Summary views necessary for the Request for Architecture Work and the
Draft Business, Data, Application, and Technology Architectures created;
typically including: Value Chain diagram Solution Concept diagram Mapped requirements Reference to Draft Architecture Definition Document

</details>

<a id="tag_04_02_09"></a>
## 4.2.9. Business Principles, Business Goals, and Business Drivers

概念：业务原则、目标和驱动的条目标题。

适用边界：上下文目的及内容差异在子节。

来源块：C220-web-2025:05-architecture-content:b00623

<details><summary>展开本节完整英文来源</summary>

4.2.9. Business Principles, Business Goals, and Business Drivers

</details>

<a id="tag_04_02_09_01"></a>
## 4.2.9.1. Purpose

概念：业务原则/目标/驱动描述企业需要与工作方式，提供架构上下文。

适用条件：确定架构外因素的实际影响。

逻辑关系：架构学科范围外因素仍可能显著影响开发方式。

决策方法：识别业务上下文与外部影响并保留来源。

制品及证据：业务原则、目标、驱动及上下文引用。

适用边界：不能因不属架构专业范围而忽略真实约束。

来源块：C220-web-2025:05-architecture-content:b00624, C220-web-2025:05-architecture-content:b00625

<details><summary>展开本节完整英文来源</summary>

4.2.9.1. Purpose

Business principles, business goals, and business drivers provide
context for architecture work, by describing the needs and ways of
working employed by the enterprise. Many factors that lie outside the
consideration of architecture discipline may nevertheless have
significant implications for the way that architecture is developed.

</details>

<a id="tag_04_02_09_02"></a>
## 4.2.9.2. Content

概念：业务上下文内容和结构随组织变化。

适用条件：组织特定架构工作。

逻辑关系：没有统一固定内容结构。

决策方法：按组织实际信息选择表达。

制品及证据：组织业务上下文。

适用边界：不得制造统一必填模板或未知业务目标。

来源块：C220-web-2025:05-architecture-content:b00626, C220-web-2025:05-architecture-content:b00627

<details><summary>展开本节完整英文来源</summary>

4.2.9.2. Content

The content and structure of business context for architecture is likely
to vary considerably from one organization to the next.

</details>

<a id="tag_04_02_10"></a>
## 4.2.10. Capability Assessment

概念：能力评估的条目标题。

适用边界：评估层次、目的和内容在子节。

来源块：C220-web-2025:05-architecture-content:b00628

<details><summary>展开本节完整英文来源</summary>

4.2.10. Capability Assessment

</details>

<a id="tag_04_02_10_01"></a>
## 4.2.10.1. Purpose

概念：详细架构定义前需理解企业、IT、架构职能及转型准备度的基线和目标能力。

适用条件：确定关注领域、治理/技能/组织影响及适合的正式程度和细节。

逻辑关系：现有资产维护准确性、标准参考模型、复用潜力及文化风险共同影响工作安排。

决策方法：分别评估业务、IT、架构及准备度，再决定重点与工作风格。

制品及证据：多层能力/成熟度与准备度评估。

适用边界：不同能力和成熟度不能合并单分数，人员技能与文化准备度须有真实证据。

来源块：C220-web-2025:05-architecture-content:b00629, C220-web-2025:05-architecture-content:b00630, C220-web-2025:05-architecture-content:b00631

<details><summary>展开本节完整英文来源</summary>

4.2.10.1. Purpose

Before embarking upon a detailed Architecture Definition, it is valuable to understand the baseline and target capability level of the
enterprise. This Capability Assessment can be examined on several levels:

What is the capability level of the enterprise as a whole? Where does the enterprise wish to increase or optimize capability? What are the architectural focus areas that will support the desired development of the enterprise? What is the capability or maturity level of the IT function within the enterprise? What are the likely implications of conducting the architecture project in terms of design governance, operational
governance, skills, and organization structure? What is an appropriate style, level of formality, and amount of detail for the architecture project to fit with the culture and capability of the IT organization? What is the capability and maturity of the architecture function within the enterprise? What architectural assets are currently in existence? Are they maintained and accurate? What standards and reference models need to be considered? Are there likely to be opportunities to create re-usable assets during the architecture project? Where capability gaps exist, to what extent is the business ready to
transform in order to reach the target capability? What are the risks to transformation, cultural barriers, and other considerations to be addressed beyond the basic capability gap?

</details>

<a id="tag_04_02_10_02"></a>
## 4.2.10.2. Content

概念：典型评估覆盖业务能力表现/实现、IT变更与运维成熟度/容量、架构成熟度和业务转型准备度。

适用条件：形成基线、目标愿望及组织影响证据。

逻辑关系：架构评估含治理、技能、景观/标准/参考模型广度深度质量与复用潜力；准备度含因素愿景、当前目标评级和风险。

决策方法：区分实测基线、目标愿望和评估依据，分别追踪差距。

制品及证据：四类评估、来源和风险。

适用边界：能力表现、人员技能、IT容量和准备度未知时保留未知，填字段不等于评估完成。

来源块：C220-web-2025:05-architecture-content:b00632, C220-web-2025:05-architecture-content:b00633, C220-web-2025:05-architecture-content:b00634

<details><summary>展开本节完整英文来源</summary>

4.2.10.2. Content

Typical contents of a Capability Assessment are:

Business Capability Assessment, including: Capabilities of the business Baseline state assessment of the performance level of each capability Future state aspiration for the performance level of each capability Baseline state assessment of how each capability is realized Future state aspiration for how each capability should be realized Assessment of likely impacts to the business organization resulting
from the successful deployment of the Target Architecture IT Capability Assessment, including: Baseline and target maturity level of change process Baseline and target maturity level of operational processes Baseline capability and capacity assessment Assessment of the likely impacts to the IT organization resulting
from the successful deployment of the Target Architecture Architecture maturity assessment, including: Architecture Governance processes, organization, roles, and
responsibilities Architecture skills assessment Breadth, depth, and quality of landscape definition with the
Architecture Repository Breadth, depth, and quality of standards definition with the
Architecture Repository Breadth, depth, and quality of reference model definition with the
Architecture Repository Assessment of re-use potential Business Transformation Readiness Assessment, including: Readiness factors Vision for each readiness factor Current and target readiness ratings Readiness risks

</details>

<a id="tag_04_02_11"></a>
## 4.2.11. Change Request

概念：变更请求的条目标题。

适用边界：触发和内容在子节。

来源块：C220-web-2025:05-architecture-content:b00635

<details><summary>展开本节完整英文来源</summary>

4.2.11. Change Request

</details>

<a id="tag_04_02_11_01"></a>
## 4.2.11.1. Purpose

概念：新事实、原定义/要求不足或外部战略市场技术因素可引发偏离、扩展和改进请求。

适用条件：实施中或发现架构变化机会。

逻辑关系：变更请求可启动进一步架构周期。

决策方法：评估是否需偏离/扩展及新周期，再提交正式请求。

制品及证据：变更请求及事实/机会来源。

适用边界：提出请求不等于偏离获批或自动启动完整周期。

来源块：C220-web-2025:05-architecture-content:b00636, C220-web-2025:05-architecture-content:b00637, C220-web-2025:05-architecture-content:b00638

<details><summary>展开本节完整英文来源</summary>

4.2.11.1. Purpose

During implementation of an architecture, as more facts become known, it
is possible that the original Architecture Definition and requirements
are not suitable or are not sufficient to complete the implementation of
a solution. In these circumstances, it is necessary for implementation
projects to either deviate from the suggested architectural approach or
to request scope extensions. Additionally, external factors — such as
market factors, changes in business strategy, and new technology
opportunities — may open up opportunities to extend and refine the
architecture.

In these circumstances, a Change Request may be submitted in order to
kick-start a further cycle of architecture work.

</details>

<a id="tag_04_02_11_02"></a>
## 4.2.11.2. Content

概念：变更请求记录拟变更、理由及其需求影响。

适用条件：支持范围和需求决策。

逻辑关系：影响评估包括特定需求、现优先级、重访阶段、主导优先级阶段、调查结果/修订优先级和管理建议。

决策方法：核查影响及阶段责任，保存资料库编号。

制品及证据：变更说明、理由、影响评估和资料库引用。

适用边界：评估建议不等于真实权限批准或优先级已达共识。

来源块：C220-web-2025:05-architecture-content:b00639, C220-web-2025:05-architecture-content:b00640, C220-web-2025:05-architecture-content:b00641

<details><summary>展开本节完整英文来源</summary>

4.2.11.2. Content

Typical contents of a Change Request are:

Description of the proposed change Rationale for the proposed change Impact assessment of the proposed change, including: Reference to specific requirements Stakeholder priority of the requirements to date Phases to be revisited Phase to lead on requirements prioritization Results of phase investigations and revised priorities Recommendations on management of requirements Repository reference number

</details>

<a id="tag_04_02_12"></a>
## 4.2.12. Communications Plan

概念：沟通计划的条目标题。

适用边界：目的和内容在子节。

来源块：C220-web-2025:05-architecture-content:b00642

<details><summary>展开本节完整英文来源</summary>

4.2.12. Communications Plan

</details>

<a id="tag_04_02_12_01"></a>
## 4.2.12.1. Purpose

概念：在合适时间向正确相关者传递定向信息是EA成功关键。

适用条件：处理大量复杂、相互依赖的架构信息。

逻辑关系：沟通计划使沟通进入有计划管理过程。

决策方法：根据相关者需要安排信息与时间。

制品及证据：沟通计划。

适用边界：信息发送数量不证明理解或正式同意。

来源块：C220-web-2025:05-architecture-content:b00643, C220-web-2025:05-architecture-content:b00644

<details><summary>展开本节完整英文来源</summary>

4.2.12.1. Purpose

Enterprise Architectures contain large volumes of complex and
inter-dependent information. Effective communication of targeted
information to the right stakeholders at the right time is a CSF for Enterprise Architecture. Development of a Communications Plan for architecture allows for this communication to be carried out within a planned and managed process.

</details>

<a id="tag_04_02_12_02"></a>
## 4.2.12.2. Content

概念：沟通计划识别相关者群组、信息需要、愿景信息、风险、关键成功因素、机制及时间地点。

适用条件：执行和管理架构沟通。

逻辑关系：会议、通讯及资料库等机制连接各群组的具体沟通安排。

决策方法：核对每类需要有渠道与时地安排。

制品及证据：沟通计划、机制及时间表。

适用边界：本节未授予自动联系他人的权限，也未要求所有相关者接收全部信息。

来源块：C220-web-2025:05-architecture-content:b00645, C220-web-2025:05-architecture-content:b00646, C220-web-2025:05-architecture-content:b00647

<details><summary>展开本节完整英文来源</summary>

4.2.12.2. Content

Typical contents of a Communications Plan are:

Identification of stakeholders and grouping by communication
requirements Identification of communication needs, key messages in relation to the
Architecture Vision, communication risks, and CSFs Identification of mechanisms that will be used to communicate with
stakeholders and allow access to architecture information, such as
meetings, newsletters, repositories, etc. Identification of a communications timetable, showing which
communications will occur with which stakeholder groups at what time and
in what location

</details>

<a id="tag_04_02_13"></a>
## 4.2.13. Compliance Assessment

概念：符合性评估的条目标题。

适用边界：目的和内容在子节。

来源块：C220-web-2025:05-architecture-content:b00648

<details><summary>展开本节完整英文来源</summary>

4.2.13. Compliance Assessment

</details>

<a id="tag_04_02_13_01"></a>
## 4.2.13.1. Purpose

概念：定期实施符合性审查检查战略/架构目标的实现进展。

适用条件：架构定义后治理实施。

逻辑关系：保持愿景实现方向并将实施经验反馈架构过程。

决策方法：结合项目进展核对设计/实施目标，反馈偏差与经验。

制品及证据：周期符合性审查及反馈。

适用边界：定期审查不等于全部合规证明或组织批准替代。

来源块：C220-web-2025:05-architecture-content:b00649, C220-web-2025:05-architecture-content:b00650

<details><summary>展开本节完整英文来源</summary>

4.2.13.1. Purpose

Once an architecture has been defined, it is necessary to govern that
architecture through implementation to ensure that the original
Architecture Vision is appropriately realized and that any
implementation learnings are fed back into the architecture process.
Periodic compliance reviews of implementation projects provide a
mechanism to review project progress and ensure that the design and
implementation is proceeding in line with the strategic and
architectural objectives.

</details>

<a id="tag_04_02_13_02"></a>
## 4.2.13.2. Content

概念：符合性评估含项目状态、架构/设计概况及已完成架构检查表。

适用条件：审查实施进展与符合性。

逻辑关系：检查领域含硬件OS、软件服务中间件、应用、信息、安全、管理、工程、方法工具。

决策方法：按适用领域填写有证据的检查结论。

制品及证据：状态概况、设计概况和已完成检查表。

适用边界：勾选表不能独自证明真实运行合规，未查项目须明确保留。

来源块：C220-web-2025:05-architecture-content:b00651, C220-web-2025:05-architecture-content:b00652, C220-web-2025:05-architecture-content:b00653

<details><summary>展开本节完整英文来源</summary>

4.2.13.2. Content

Typical contents of a Compliance Assessment are:

Overview of project progress and status Overview of project architecture/design Completed architecture checklists: Hardware and operating system checklist Software services and middleware checklist Applications checklists Information management checklists Security checklists System management checklists System engineering checklists Methods and tools checklists

</details>

<a id="tag_04_02_14"></a>
## 4.2.14. Implementation and Migration Plan

概念：实施和迁移计划的条目标题。

适用边界：可执行项目安排和内容在子节。

来源块：C220-web-2025:05-architecture-content:b00654

<details><summary>展开本节完整英文来源</summary>

4.2.14. Implementation and Migration Plan

</details>

<a id="tag_04_02_14_01"></a>
## 4.2.14.1. Purpose

概念：实施和迁移计划安排实现目标架构的项目进度。

适用条件：组合/项目群管理下的可执行实施。

逻辑关系：实施迁移策略规定变革方法，是计划关键元素。

决策方法：把工作转为受管理项目/组合并明确变革策略。

制品及证据：计划、项目安排及迁移策略。

适用边界：路线图和计划相关但不相同；列时间不证明项目资源已落实。

来源块：C220-web-2025:05-architecture-content:b00655, C220-web-2025:05-architecture-content:b00656

<details><summary>展开本节完整英文来源</summary>

4.2.14.1. Purpose

The Implementation and Migration Plan provides a schedule of the
projects that will realize the Target Architecture. The Implementation
and Migration Plan includes executable projects grouped into managed
portfolios and programs. The Implementation and Migration Strategy
identifying the approach to change is a key element of the
Implementation and Migration Plan.

</details>

<a id="tag_04_02_14_02"></a>
## 4.2.14.2. Content

概念：计划典型含战略方向、顺序方法、项目/组合分解、包分配、能力、里程碑和WBS。

适用条件：形成执行和资源计划。

逻辑关系：可包含现有组合影响、项目章程、包价值风险、资源成本、收益到需求映射和迁移选项估算。

决策方法：核对项目能力、依赖、时间及资源依据，标记可选内容。

制品及证据：实施计划、策略、WBS及适用章程/资源成本收益估算。

适用边界：may include不能解释为所有项目强制章程字段；实际工作量容量成本未知须保留。

来源块：C220-web-2025:05-architecture-content:b00657, C220-web-2025:05-architecture-content:b00658, C220-web-2025:05-architecture-content:b00659, C220-web-2025:05-architecture-content:b00660, C220-web-2025:05-architecture-content:b00661

<details><summary>展开本节完整英文来源</summary>

4.2.14.2. Content

Typical contents of an Implementation and Migration Plan are:

Implementation and Migration Strategy: Strategic implementation direction Implementation sequencing approach Project and portfolio breakdown of implementation: Allocation of work packages to project and portfolio Capabilities delivered by projects Milestones and timing Work breakdown structure May include impact on existing portfolio, program, and projects

It may contain:

Project charters: Included work packages Business value Risk, issues, assumptions, dependencies Resource requirements and costs Benefits of migration, determined (including mapping to business
requirements) Estimated costs of migration options

</details>

<a id="tag_04_02_15"></a>
## 4.2.15. Implementation Governance Model

概念：实施治理模型的条目标题。

适用边界：治理过渡目的及内容在子节。

来源块：C220-web-2025:05-architecture-content:b00662

<details><summary>展开本节完整英文来源</summary>

4.2.15. Implementation Governance Model

</details>

<a id="tag_04_02_15_01"></a>
## 4.2.15.1. Purpose

概念：实施治理模型使进入实施的项目平滑进入适当架构治理。

适用条件：目标经由过渡架构实施。

逻辑关系：既有治理框架可复用，但项目特定过程组织角色责任度量可能需定义。

决策方法：核查既有治理适用性并补项目特定安排。

制品及证据：实施治理模型与过渡治理安排。

适用边界：模型模板不证明实际治理机构拥有该项目决策权限。

来源块：C220-web-2025:05-architecture-content:b00663, C220-web-2025:05-architecture-content:b00664, C220-web-2025:05-architecture-content:b00665

<details><summary>展开本节完整英文来源</summary>

4.2.15.1. Purpose

Once an architecture has been defined, it is necessary to plan how the
Transition Architecture that implements the architecture will be
governed through implementation. Within organizations that have
established architecture functions, there is likely to be a governance
framework already in place, but specific processes, organizations,
roles, responsibilities, and measures may need to be defined on a
project-by-project basis.

The Implementation Governance Model ensures that a project transitioning
into implementation also smoothly transitions into appropriate
Architecture Governance.

</details>

<a id="tag_04_02_15_02"></a>
## 4.2.15.2. Content

概念：典型模型含治理过程、组织结构、角色责任、检查点和成功/失败准则。

适用条件：实施阶段的治理与验收。

逻辑关系：治理角色与检查点及准则相连。

决策方法：核对真实职责、检查程序和可判定准则。

制品及证据：治理模型、检查点及成败标准。

适用边界：角色名和准则填写不等于授权或验收证据。

来源块：C220-web-2025:05-architecture-content:b00666, C220-web-2025:05-architecture-content:b00667, C220-web-2025:05-architecture-content:b00668

<details><summary>展开本节完整英文来源</summary>

4.2.15.2. Content

Typical contents of an Implementation Governance Model are:

Governance processes Governance organization structure Governance roles and responsibilities Governance checkpoints and success/failure criteria

</details>

<a id="tag_04_02_16"></a>
## 4.2.16. Organizational Model for Enterprise Architecture

概念：EA组织模型的条目标题。

适用边界：组织边界与内容在子节。

来源块：C220-web-2025:05-architecture-content:b00669

<details><summary>展开本节完整英文来源</summary>

4.2.16. Organizational Model for Enterprise Architecture

</details>

<a id="tag_04_02_16_01"></a>
## 4.2.16.1. Purpose

概念：成功应用架构框架需正确组织、角色和责任。

适用条件：界定不同EA实践者边界及跨边界治理关系。

逻辑关系：实践者范围与治理接口共同支持框架。

决策方法：明确职责边界和跨边界治理关系。

制品及证据：EA组织模型及治理接口。

适用边界：组织图不自动生成真实授权或个人能力。

来源块：C220-web-2025:05-architecture-content:b00670, C220-web-2025:05-architecture-content:b00671

<details><summary>展开本节完整英文来源</summary>

4.2.16.1. Purpose

In order for an architecture framework to be used successfully, it must
be supported by the correct organization, roles, and responsibilities
within the enterprise. Of particular importance is the definition of
boundaries between different Enterprise Architecture practitioners and
the governance relationships that span across these boundaries.

</details>

<a id="tag_04_02_16_02"></a>
## 4.2.16.2. Content

概念：组织模型典型含受影响组织范围、成熟度差距/解决方法、团队角色责任、约束、预算和治理支持策略。

适用条件：建立组织特定EA能力。

逻辑关系：范围和能力约束影响团队安排及支持需求。

决策方法：依据真实范围、成熟度及资源输入形成模型。

制品及证据：组织模型、成熟度/差距、角色责任和预算/治理策略。

适用边界：预算要求不同于已批准预算；角色需求不同于已证明人员技能。

来源块：C220-web-2025:05-architecture-content:b00672, C220-web-2025:05-architecture-content:b00673, C220-web-2025:05-architecture-content:b00674

<details><summary>展开本节完整英文来源</summary>

4.2.16.2. Content

Typical contents of an Organizational Model for Enterprise Architecture
are:

Scope of organizations impacted Maturity assessment, gaps, and resolution approach Roles and responsibilities for architecture team(s) Constraints on architecture work Budget requirements Governance and support strategy

</details>

<a id="tag_04_02_17"></a>
## 4.2.17. Request for Architecture Work

概念：架构工作请求的条目标题。

适用边界：发起来源及高层内容在子节。

来源块：C220-web-2025:05-architecture-content:b00675

<details><summary>展开本节完整英文来源</summary>

4.2.17. Request for Architecture Work

</details>

<a id="tag_04_02_17_01"></a>
## 4.2.17.1. Purpose

概念：赞助组织向架构组织发送请求，触发架构开发周期。

适用条件：预备产出、已批准变更或迁移规划职权范围发起。

逻辑关系：请求来源与正式赞助关系决定启动背景。

决策方法：核实赞助、来源及触发依据，保持内容高层。

制品及证据：架构工作请求及批准变更/规划引用。

适用边界：不能把未批准变更或自行创建请求当真实组织授权。

来源块：C220-web-2025:05-architecture-content:b00676, C220-web-2025:05-architecture-content:b00677, C220-web-2025:05-architecture-content:b00678

<details><summary>展开本节完整英文来源</summary>

4.2.17.1. Purpose

This is a document that is sent from the sponsoring organization to the
architecture organization to trigger the start of an architecture
development cycle. Requests for Architecture Work can be created as an
output of the Preliminary Phase, a result of approved architecture
Change Requests, or terms of reference for architecture work originating
from migration planning.

In general, all the information in this document should be at a high
level.

</details>

<a id="tag_04_02_17_02"></a>
## 4.2.17.2. Content

概念：请求典型含赞助、使命目标、战略、时间、环境变化、组织/财务/外部业务约束。

适用条件：确定架构工作上下文与可用资源。

逻辑关系：当前业务系统/架构、开发组织和资源描述补足基线。

决策方法：引用实际计划及基线资料，区分预算信息和限制。

制品及证据：工作请求及战略/系统/资源引用。

适用边界：高层请求不是详细设计或可行性证明；未知资源不得补造。

来源块：C220-web-2025:05-architecture-content:b00679, C220-web-2025:05-architecture-content:b00680, C220-web-2025:05-architecture-content:b00681

<details><summary>展开本节完整英文来源</summary>

4.2.17.2. Content

Requests for Architecture Work typically include:

Organization sponsors Organization’s mission statement Business goals (and changes) Strategic plans of the business Time limits Changes in the business environment Organizational constraints Budget information, financial constraints External constraints, business constraints Current business system description Current architecture/IT system description Description of developing organization Description of resources available to developing organization

</details>

<a id="tag_04_02_18"></a>
## 4.2.18. Requirements Impact Assessment

概念：需求影响评估的条目标题。

适用边界：持续评估目的和内容在子节。

来源块：C220-web-2025:05-architecture-content:b00682

<details><summary>展开本节完整英文来源</summary>

4.2.18. Requirements Impact Assessment

</details>

<a id="tag_04_02_18_01"></a>
## 4.2.18.1. Purpose

概念：ADM中新信息可能使既有架构无效，影响评估检查当前需求/规格及改变含义。

适用条件：整个ADM的新事实识别。

逻辑关系：需求变化影响架构和重访工作。

决策方法：依据新事实判断需改变要求及后续影响。

制品及证据：需求影响评估与新事实证据。

适用边界：仅更新文本不能自动认定所有依赖已处理。

来源块：C220-web-2025:05-architecture-content:b00683, C220-web-2025:05-architecture-content:b00684

<details><summary>展开本节完整英文来源</summary>

4.2.18.1. Purpose

Throughout the ADM, new information is collected relating to an
architecture. As this information is gathered, new facts may come to
light that invalidate existing aspects of the architecture. A
Requirements Impact Assessment assesses the current architecture
requirements and specification to identify changes that should be made
and the implications of those changes.

</details>

<a id="tag_04_02_18_02"></a>
## 4.2.18.2. Content

概念：影响评估含特定需求、当前相关者优先级、需重访阶段及优先级主导阶段。

适用条件：追溯调查、修订和管理决定。

逻辑关系：阶段调查结果/新优先级连接需求管理建议及资料库编号。

决策方法：核对需求影响、阶段责任及修订依据。

制品及证据：需求影响评估及资料库追溯。

适用边界：与变更请求内容重叠但用途不同；建议不能当已批准变更。

来源块：C220-web-2025:05-architecture-content:b00685, C220-web-2025:05-architecture-content:b00686, C220-web-2025:05-architecture-content:b00687

<details><summary>展开本节完整英文来源</summary>

4.2.18.2. Content

Typical contents of a Requirements Impact Assessment are:

Reference to specific requirements Stakeholder priority of the requirements to date Phases to be revisited Phase to lead on requirements prioritization Results of phase investigations and revised priorities Recommendations on management of requirements Repository reference number

</details>

<a id="tag_04_02_19"></a>
## 4.2.19. Solution Building Blocks

概念：SBB是资料库中实现特定的构建块。

适用条件：实施具体方案或复用实现资产。

逻辑关系：具体特征见第5章。

决策方法：按实现需要与ABB匹配并追溯资料库。

制品及证据：实现特定SBB引用。

适用边界：SBB与逻辑ABB身份不同，不因同名而合并。

来源块：C220-web-2025:05-architecture-content:b00688, C220-web-2025:05-architecture-content:b00689

<details><summary>展开本节完整英文来源</summary>

4.2.19. Solution Building Blocks

Implementation-specific building blocks from the enterprise’s
Architecture Repository; see Chapter 5, Building Blocks .

</details>

<a id="tag_04_02_20"></a>
## 4.2.20. Statement of Architecture Work

概念：架构工作说明的条目标题。

适用边界：工作范围、验收及典型内容在子节。

来源块：C220-web-2025:05-architecture-content:b00690

<details><summary>展开本节完整英文来源</summary>

4.2.20. Statement of Architecture Work

</details>

<a id="tag_04_02_20_01"></a>
## 4.2.20.1. Purpose

概念：工作说明定义完成架构周期的范围和方法。

适用条件：衡量架构项目执行成功及可能形成服务供需契约。

逻辑关系：范围/方法连接项目成功评价和契约基础。

决策方法：明确可评价范围与方法并与双方约定相衔接。

制品及证据：工作说明及执行衡量依据。

适用边界：工作说明不同于触发请求，也不证明契约已签署。

来源块：C220-web-2025:05-architecture-content:b00691, C220-web-2025:05-architecture-content:b00692

<details><summary>展开本节完整英文来源</summary>

4.2.20.1. Purpose

The Statement of Architecture Work defines the scope and approach that
will be used to complete an architecture development cycle. The
Statement of Architecture Work is typically the document against which
successful execution of the architecture project will be measured and
may form the basis for a contractual agreement between the supplier and
consumer of architecture services.

</details>

<a id="tag_04_02_20_02"></a>
## 4.2.20.2. Content

概念：典型说明含标题背景、项目范围、愿景摘要、范围变更程序、角色责任交付、验收准则程序、计划及批准。

适用条件：约定架构工作执行和验收。

逻辑关系：范围、责任与交付对应验收和批准流程。

决策方法：核查准则可判定、变更程序明确且批准真实。

制品及证据：工作说明、验收程序、计划及批准记录。

适用边界：字段齐全不代表实际权限/签批，架构服务验收不同于业务恢复目标验证。

来源块：C220-web-2025:05-architecture-content:b00693, C220-web-2025:05-architecture-content:b00694, C220-web-2025:05-architecture-content:b00695

<details><summary>展开本节完整英文来源</summary>

4.2.20.2. Content

Typical contents of a Statement of Architecture Work are:

Title Architecture project request and background Architecture project description and scope Overview of Architecture Vision Specific change of scope procedures Roles, responsibilities, and deliverables Acceptance criteria and procedures Architecture project plan and schedule Approvals

</details>

<a id="tag_04_02_21"></a>
## 4.2.21. Tailored Architecture Framework

概念：裁剪架构框架的条目标题。

适用边界：两级裁剪及内容在子节。

来源块：C220-web-2025:05-architecture-content:b00696

<details><summary>展开本节完整英文来源</summary>

4.2.21. Tailored Architecture Framework

</details>

<a id="tag_04_02_21_01"></a>
## 4.2.21.1. Purpose

概念：框架须先集成并裁剪到企业，再按具体架构项目裁剪。

适用条件：企业和项目有效使用TOGAF。

逻辑关系：企业层处理管理框架、术语、表达、工具并适配文化/相关者/商业模式/能力；项目层选满足需要的交付物和制品。

决策方法：先确认企业适配，再按项目相关者需要选择内容。

制品及证据：企业及项目两级裁剪依据。

适用边界：不能直接把通用清单当每项目全部必交，也不能无说明以裁剪删掉真实约束。

来源块：C220-web-2025:05-architecture-content:b00697, C220-web-2025:05-architecture-content:b00698, C220-web-2025:05-architecture-content:b00699, C220-web-2025:05-architecture-content:b00700, C220-web-2025:05-architecture-content:b00701

<details><summary>展开本节完整英文来源</summary>

4.2.21.1. Purpose

The TOGAF framework provides an industry standard for architecture that
may be used in a wide variety of organizations. However, before the
TOGAF framework can be effectively used within an architecture project,
tailoring at two levels is necessary.

Firstly, it is necessary to tailor the TOGAF model for integration into
the enterprise. This tailoring will include integration with management
frameworks, customization of terminology, development of presentational
styles, selection, configuration, and deployment of architecture tools,
etc. The formality and detail of any frameworks adopted should also
align with other contextual factors for the enterprise, such as culture,
stakeholders, commercial models for Enterprise Architecture, and the
existing level of Architecture Capability.

Once the framework has been tailored to the enterprise, further
tailoring is necessary in order to tailor the framework for the specific
architecture project. Tailoring at this level will select appropriate
deliverables and artifacts to meet project and stakeholder needs.

See the TOGAF Standard — Architecture Development Method for further considerations when selecting and tailoring the
architecture framework.

</details>

<a id="tag_04_02_21_02"></a>
## 4.2.21.2. Content

概念：典型裁剪框架含方法、交付物/制品内容、配置部署工具及治理/其他框架接口。

适用条件：建立可执行的企业/项目方法。

逻辑关系：接口覆盖企业业务规划、EA、组合项目群项目、系统开发工程及运行。

决策方法：核查方法内容工具和各管理接口一致。

制品及证据：裁剪框架、工具及接口约定。

适用边界：工具安装不证明方法能力或治理批准，接口需实际组织证据。

来源块：C220-web-2025:05-architecture-content:b00702, C220-web-2025:05-architecture-content:b00703, C220-web-2025:05-architecture-content:b00704

<details><summary>展开本节完整英文来源</summary>

4.2.21.2. Content

Typical contents of a Tailored Architecture Framework are:

Tailored architecture method Tailored architecture content (deliverables and artifacts) Configured and deployed tools Interfaces with governance models and other frameworks: Corporate Business Planning Enterprise Architecture Portfolio, Program, Project Management System Development/Engineering Operations (Services)

</details>

<a id="chap05"></a>
## 5. Building Blocks

概念：本章解释构建块概念。

适用条件：理解架构组成及复用。

逻辑关系：子节分通用特征和ADM中的定义过程。

决策方法：按概念再查过程。

制品及证据：构建块解释。

适用边界：章节标题不新增规格义务。

来源块：C220-web-2025:05-architecture-content:b00705, C220-web-2025:05-architecture-content:b00706

<details><summary>展开本节完整英文来源</summary>

5. Building Blocks

This chapter explains the concept of building blocks.

</details>

<a id="tag_05_01"></a>
## 5.1. Overview

概念：本章分构建块概念及ABB/SBB区别、ADM中的设计规格阶段。

适用条件：阅读构建块理论与过程。

逻辑关系：5.2解释概念，5.3说明ADM采用。

决策方法：分别核查构建块身份与演化过程。

制品及证据：章节导读。

适用边界：本节不规定所有块统一粒度。

来源块：C220-web-2025:05-architecture-content:b00707, C220-web-2025:05-architecture-content:b00708, C220-web-2025:05-architecture-content:b00709, C220-web-2025:05-architecture-content:b00710

<details><summary>展开本节完整英文来源</summary>

5.1. Overview

This section is intended to explain and illustrate the concept of
building blocks in architecture.

Following this overview, there are two main parts:

Introduction to Building Blocks (see Section 5.2, “Introduction to Building Blocks” ), discusses the general concepts of building blocks,
and explains the differences between ABBs and SBBs Building Blocks and the ADM (see Section 5.3, “Building Blocks and the ADM” ), summarizes the stages at which building block design and
specification occurs within the TOGAF ADM

</details>

<a id="tag_05_02"></a>
## 5.2. Introduction to Building Blocks

概念：构建块概念的导读。

适用条件：理解构建块。

逻辑关系：特征在后续节，ADM另在5.3。

决策方法：先读通用和具体类别特征。

制品及证据：构建块概念引用。

适用边界：不新增独立必填清单。

来源块：C220-web-2025:05-architecture-content:b00711, C220-web-2025:05-architecture-content:b00712

<details><summary>展开本节完整英文来源</summary>

5.2. Introduction to Building Blocks

This section is an introduction to the concept of building blocks.

</details>

<a id="tag_05_02_01"></a>
## 5.2.1. Overview

概念：本节概览构建块特征，ADM用法另述。

适用条件：区分特征与过程。

逻辑关系：5.2.2通用、5.2.3 ABB、5.2.4 SBB。

决策方法：按类别核查规格。

制品及证据：特征章节引用。

适用边界：概览不证明块已实现。

来源块：C220-web-2025:05-architecture-content:b00713, C220-web-2025:05-architecture-content:b00714

<details><summary>展开本节完整英文来源</summary>

5.2.1. Overview

This section describes the characteristics of building blocks. The use
of building blocks in the ADM is described separately in Section 5.3, “Building Blocks and the ADM” .

</details>

<a id="tag_05_02_02"></a>
## 5.2.2. Generic Characteristics

概念：构建块是为跨组织业务需要定义的功能包，通常有元模型类型和领域专家可识别的边界。

适用条件：选择架构组成、接口及复用粒度。

逻辑关系：可互操作/相互依赖、由其他块组装或作为子装配；边界规格应与实现松耦合。

决策方法：按企业目标选择组合和细节，在互操作时公布合理稳定接口，考虑实现使用/标准及复用替换。

制品及证据：块类型边界、功能规格、接口、依赖和组合关系。

适用边界：早期名字/概要可足够；详细程度按目的而定，理想复用性不等于已验证复用；RAS是参考实例非本项目强制格式。

来源块：C220-web-2025:05-architecture-content:b00715, C220-web-2025:05-architecture-content:b00716, C220-web-2025:05-architecture-content:b00717, C220-web-2025:05-architecture-content:b00718, C220-web-2025:05-architecture-content:b00719, C220-web-2025:05-architecture-content:b00720, C220-web-2025:05-architecture-content:b00721, C220-web-2025:05-architecture-content:b00722, C220-web-2025:05-architecture-content:b00723

<details><summary>展开本节完整英文来源</summary>

5.2.2. Generic Characteristics

Building blocks have generic characteristics as follows:

A building block is a package of functionality defined to meet the
business needs across an organization A building block normally has a type that corresponds to the metamodel
(such as actor, business service, application, or data entity) A building block has a defined boundary and is generally recognizable
as “a thing” by domain experts A building block may interoperate with other, inter-dependent building
blocks. A good building block has the following characteristics: It considers implementation and usage, and evolves to exploit
technology and standards It may be assembled from other building blocks It may be a subassembly of other building blocks Ideally a building block is re-usable and replaceable, and well
specified

A building block’s boundary and specification should be loosely coupled
to its implementation; i.e., it should be possible to realize a building
block in several different ways without impacting the boundary or
specification of the building block. The way in which assets and
capabilities are assembled into building blocks will vary widely between
individual architectures. Every organization must decide for itself what
arrangement of building blocks works best for it. A good choice of
building blocks can lead to improvements in legacy system integration,
interoperability, and flexibility in the creation of new systems and
applications.

Systems are built up from collections of building blocks, so most
building blocks have to interoperate with other building blocks.
Wherever that is true, it is important that the interfaces to a building
block are published and reasonably stable.

Building blocks can be defined at various levels of detail, depending on
what stage of architecture development has been reached.

For instance, at an early stage, a building block can simply consist of
a name or an outline description. Later on, a building block may be
decomposed into multiple supporting building blocks and may be
accompanied by a full specification.

The level of detail to which a building block should be specified is
dependent on the objectives of the architecture and, in some cases, less
detail may be of greater value (for example, when presenting the
capabilities of an enterprise, a single clear and concise picture has
more value than a dense 100-page specification).

The Object Management Group ® (OMG ® ) has developed a standard for Re-usable Asset Specification (RAS), [ 1 ] which provides a good example of how building blocks can be formally described and managed.

</details>

<a id="tag_05_02_03"></a>
## 5.2.3. Architecture Building Blocks

概念：ABB属于架构连续体，由ADM定义或选择。

适用条件：形成逻辑架构组成。

逻辑关系：后续特征与规格指引SBB。

决策方法：按架构需要选择。

制品及证据：ABB及ADM来源。

适用边界：ABB不等于选定厂商产品。

来源块：C220-web-2025:05-architecture-content:b00724, C220-web-2025:05-architecture-content:b00725

<details><summary>展开本节完整英文来源</summary>

5.2.3. Architecture Building Blocks

Architecture Building Blocks (ABBs) relate to the Architecture Continuum
(see Section 6.4.1, “Architecture Continuum” ),
and are defined or selected as a result of the application of the ADM.

</details>

<a id="tag_05_02_03_01"></a>
## 5.2.3.1. Characteristics

概念：ABB捕获业务、数据、应用和技术架构需求。

适用条件：指导SBB发展。

逻辑关系：需求—ABB—SBB保持方向性。

决策方法：核对ABB所捕获需求及对实现的指导。

制品及证据：ABB需求及SBB指导映射。

适用边界：捕获需求不证明实现已经满足需求。

来源块：C220-web-2025:05-architecture-content:b00726, C220-web-2025:05-architecture-content:b00727, C220-web-2025:05-architecture-content:b00728

<details><summary>展开本节完整英文来源</summary>

5.2.3.1. Characteristics

ABBs:

Capture architecture requirements; e.g., Business, Data, Application,
and Technology requirements Direct and guide the development of SBBs

</details>

<a id="tag_05_02_03_02"></a>
## 5.2.3.2. Specification Content

概念：ABB规格最少包含无歧义功能属性、选定供应接口、互操作/块关系、依赖功能及命名接口、业务组织实体/政策映射。

适用条件：建立可用的ABB规格。

逻辑关系：安全能力和可管理性属于功能属性的明确语义范围。

决策方法：逐项核查最少规格及来源，明确接口和依赖。

制品及证据：ABB最少规格及政策/业务映射。

适用边界：minimum不同于可任意忽略的典型项；未知要求需显式记录和补证，不伪造符合性。

来源块：C220-web-2025:05-architecture-content:b00729, C220-web-2025:05-architecture-content:b00730, C220-web-2025:05-architecture-content:b00731

<details><summary>展开本节完整英文来源</summary>

5.2.3.2. Specification Content

ABB specifications include the following as a minimum:

Fundamental functionality and attributes: semantic, unambiguous,
including security capability and manageability Interfaces: chosen set, supplied Interoperability and relationship with other building blocks Dependent building blocks with required functionality and named user
interfaces Map to business/organizational entities and policies

</details>

<a id="tag_05_02_04"></a>
## 5.2.4. Solution Building Blocks

概念：SBB属于方案连续体，可采购或开发。

适用条件：具体实现选择。

逻辑关系：后续特征和规格描述产品感知实现。

决策方法：按所需实现选择采购/开发路径。

制品及证据：SBB来源及采购/开发选择。

适用边界：构建块存在不等于采购完成或开发验收。

来源块：C220-web-2025:05-architecture-content:b00732, C220-web-2025:05-architecture-content:b00733

<details><summary>展开本节完整英文来源</summary>

5.2.4. Solution Building Blocks

Solution Building Blocks (SBBs) relate to the Solutions Continuum (see Section 6.4.2, “Solutions Continuum” ),
and may be either procured or developed.

</details>

<a id="tag_05_02_04_01"></a>
## 5.2.4.1. Characteristics

概念：SBB定义实现功能的产品组件及具体实现，并满足业务需求。

适用条件：表达产品或厂商感知方案。

逻辑关系：实现—产品—业务要求关联。

决策方法：核查具体方案及业务要求满足证据。

制品及证据：SBB产品/组件实现定义。

适用边界：vendor-aware不意味着必须外购；写有满足需求不能替代验证。

来源块：C220-web-2025:05-architecture-content:b00734, C220-web-2025:05-architecture-content:b00735, C220-web-2025:05-architecture-content:b00736

<details><summary>展开本节完整英文来源</summary>

5.2.4.1. Characteristics

SBBs:

Define what products and components will implement the functionality Define the implementation Fulfill business requirements Are product or vendor-aware

</details>

<a id="tag_05_02_04_02"></a>
## 5.2.4.2. Specification Content

概念：SBB最少规格含具体功能属性、已实现接口、依赖SBB功能/接口、IT拓扑/运维政策及与ABB关系。

适用条件：规定物理实现和环境质量要求。

逻辑关系：安全、可管理、本地化、扩展等共享属性区别于功能；性能配置、设计驱动约束含物理架构。

决策方法：逐项核查已实现接口和环境属性，追溯ABB、拓扑及政策。

制品及证据：SBB最少规格、依赖、质量属性、物理约束和ABB映射。

适用边界：不能把ABB选定接口冒充SBB已实现接口，未知性能和恢复目标不得编造。

来源块：C220-web-2025:05-architecture-content:b00737, C220-web-2025:05-architecture-content:b00738, C220-web-2025:05-architecture-content:b00739

<details><summary>展开本节完整英文来源</summary>

5.2.4.2. Specification Content

SBB specifications include the following as a minimum:

Specific functionality and attributes Interfaces; the implemented set Required SBBs used with required functionality and names of the
interfaces used Mapping from the SBBs to the IT topology and operational policies Specifications of attributes shared across the environment (not to be
confused with functionality) such as security, manageability,
localizability, scalability Performance, configurability Design drivers and constraints, including the physical architecture Relationships between SBBs and ABBs

</details>

<a id="tag_05_03"></a>
## 5.3. Building Blocks and the ADM

概念：构建块与ADM的分组标题。

适用边界：基本原则与规格过程在子节。

来源块：C220-web-2025:05-architecture-content:b00740

<details><summary>展开本节完整英文来源</summary>

5.3. Building Blocks and the ADM

</details>

<a id="tag_05_03_01"></a>
## 5.3.1. Basic Principles

概念：本节聚焦ADM中构建块用法，通用特征在5.2。

适用条件：架构开发过程。

逻辑关系：过程与块特征互补。

决策方法：共同使用概念与过程指导。

制品及证据：ADM构建块指导引用。

适用边界：不新增独立流程阶段。

来源块：C220-web-2025:05-architecture-content:b00741, C220-web-2025:05-architecture-content:b00742

<details><summary>展开本节完整英文来源</summary>

5.3.1. Basic Principles

This section focuses on the use of building blocks in the ADM. General
considerations and characteristics of building blocks are described in Section 5.2, “Introduction to Building Blocks” .

</details>

<a id="tag_05_03_01_01"></a>
## 5.3.1.1. Building Blocks in Architecture Design

概念：架构由模型中的构建块及其满足总体业务需求的连接规格组成。

适用条件：针对具体业务问题进行架构设计。

逻辑关系：只需相关块；关系可复杂、多对多或部分支持；应遵守适用类型标准、企业原则和标准。

决策方法：据问题限定范围，核查支持关系及符合性。

制品及证据：相关构建块集合、连接规格和标准追溯。

适用边界：支持多个或部分块不能默认一一实现；架构无需包含企业所有资产。

来源块：C220-web-2025:05-architecture-content:b00743, C220-web-2025:05-architecture-content:b00744, C220-web-2025:05-architecture-content:b00745, C220-web-2025:05-architecture-content:b00746, C220-web-2025:05-architecture-content:b00747

<details><summary>展开本节完整英文来源</summary>

5.3.1.1. Building Blocks in Architecture Design

An architecture is a set of building blocks depicted in an architectural
model, and a specification of how those building blocks are connected to
meet the overall requirements of the business.

The various building blocks in an architecture specify the scope and
approach that will be used to address a specific business problem.

There are some general principles underlying the use of building blocks
in the design of specific architectures:

An architecture need only contain building blocks that are relevant to
the business problem that the architecture is attempting to address Building blocks may have complex relationships to one another One building block may support multiple building blocks or may partially
support a single building block (for example, the business service of
“complaint handling” would be supported by many data entities and
possibly multiple application components) Building blocks should conform to standards relevant to their type,
the principles of the enterprise, and the standards of the enterprise

</details>

<a id="tag_05_03_01_02"></a>
## 5.3.1.2. Building Block Design

概念：构建块设计识别交互能力/资产并按期望集成程度聚合或分离。

适用条件：选择复用遗留、开发新块或采购COTS。

逻辑关系：早期广义集成有利服务定义；详细视图支持实现、战略权衡及共同性/复用价值判断。

决策方法：考虑三类来源和目标集成，按决策需要细化。

制品及证据：块来源选择、组合边界及细化视图。

适用边界：遗留块可保留大粒度，不能强制拆解；候选COTS不等于已采购。

来源块：C220-web-2025:05-architecture-content:b00748, C220-web-2025:05-architecture-content:b00749, C220-web-2025:05-architecture-content:b00750, C220-web-2025:05-architecture-content:b00751

<details><summary>展开本节完整英文来源</summary>

5.3.1.2. Building Block Design

The process of identifying building blocks includes looking for
collections of capabilities or assets that interact with one another and
then drawing them together or making them different:

Consider three classes of building blocks: Re-usable building blocks, such as legacy items Building blocks to be the subject of development, such as new
applications Building blocks to be the subject of purchase; i.e., Commercial
Off-The-Shelf (COTS)  applications Use the desired level of integration to bind or combine functions into
building blocks; for instance, legacy elements could be treated as large
building blocks to avoid breaking them apart

In the early stages and during views of the highest-level enterprise,
the building blocks are often kept at a broad integration definition. It
is during these exercises that the services definitions can often be
best viewed. As implementation considerations are addressed, more
detailed views of building blocks can often be used to address
implementation decisions, focus on the critical strategic decisions, or
aid in assessing the value and future impact of commonality and
re-usability.

</details>

<a id="tag_05_03_02"></a>
## 5.3.2. Building Block Specification Process in the ADM

概念：块定义在ADM主要A/B/C/D中渐进、演化并迭代。

适用条件：功能约束和产品可用性逐步澄清。

逻辑关系：识别满足业务目标的ABB，再迭代形成可采购或开发的SBB；信息可改变选择/内容。

决策方法：按新功能约束和产品事实重访规格及映射。

制品及证据：ABB到SBB演进记录及图5-1阶段引用。

适用边界：不是ABB名称自动改成SBB，也不是只允许A—D发现新的块。

来源块：C220-web-2025:05-architecture-content:b00752, C220-web-2025:05-architecture-content:b00753, C220-web-2025:05-architecture-content:b00754, C220-web-2025:05-architecture-content:b00755, C220-web-2025:05-architecture-content:b00756

<details><summary>展开本节完整英文来源</summary>

5.3.2. Building Block Specification Process in the ADM

The process of building block definition takes place gradually as the
ADM is followed, mainly in Phases A, B, C, and D. It is an evolutionary
and iterative process because as definition proceeds, detailed
information about the functionality required, the constraints imposed on
the architecture, and the availability of products may affect the choice
and the content of building blocks.

The key phases and steps of the ADM at which building blocks are evolved
and specified are summarized in Figure 5-1 . The major
work in these steps consists of identifying the ABBs required to meet
the business goals and objectives. The selected set of ABBs is then
refined in an iterative process to arrive at a set of SBBs which can
either be bought off-the-shelf or custom developed.



Figure 5-1: Key ADM Phases/Steps at which Building Blocks are Evolved/Specified

</details>

<a id="chap06"></a>
## 6. Enterprise Continuum

概念：企业连续体的章节标题。

适用边界：分类、复用与组织用法在子节。

来源块：C220-web-2025:05-architecture-content:b00757

<details><summary>展开本节完整英文来源</summary>

6. Enterprise Continuum

</details>

<a id="tag_06_01"></a>
## 6.1. Overview

概念：企业连续体分类资料库内外架构/方案制品，从通用基础到组织特定。

适用条件：表达架构设计的内容、原因、方法及驱动，协调企业与客户/供应方沟通。

逻辑关系：所有架构具上下文，连续体提供一致语言来区别抽象/具体范围并组织复用资产。

决策方法：明确当前分类位置及上下文，再比较与复用。

制品及证据：资产分类、架构上下文和沟通映射。

适用边界：不同位置不可无说明混称同一架构；分类不证明投资收益已实现。

来源块：C220-web-2025:05-architecture-content:b00758, C220-web-2025:05-architecture-content:b00759, C220-web-2025:05-architecture-content:b00760, C220-web-2025:05-architecture-content:b00761, C220-web-2025:05-architecture-content:b00762

<details><summary>展开本节完整英文来源</summary>

6.1. Overview

The Enterprise Continuum provides methods for classifying architecture
and solution artifacts, both internal and external to the Architecture Repository, as they evolve from generic Foundation Architectures to Organization-Specific Architectures.

The Enterprise Continuum enables the architect to articulate the broad
perspective of what, why, and how the Enterprise Architecture has been
designed with the factors and drivers considered. The Enterprise
Continuum is an important aid to communication and understanding, both
within individual enterprises, and between customer enterprises and
vendor organizations. Without an understanding of “where in the
continuum you are”, people discussing architecture can often talk at cross-purposes because they are referencing different points in the continuum at the same time, without realizing it.

Any architecture is context-specific; for example, there are
architectures that are specific to individual customers, industries,
subsystems, products, and services. Architects, on both the buy side and
supply side, must have at their disposal a consistent language to
effectively communicate the differences between architectures. Such a language will enable engineering efficiency and the effective leveraging of COTS product functionality. The Enterprise Continuum provides that consistent language.

The Enterprise Continuum enables the organization of re-usable
architecture artifacts and solution assets to maximize the Enterprise
Architecture investment opportunities.

</details>

<a id="tag_06_02"></a>
## 6.2. Enterprise Continuum and Architecture Re-Use

概念：连续体可视为企业认为可用于开发的架构资产库视图。

适用条件：选择内外描述、模型、块、模式、视点及其他制品用于复用。

逻辑关系：既有交付物、行业模型/模式及基础/领域/行业参考都可考虑；EA决定纳入资料库的资产。

决策方法：按架构需要及复用价值筛选并记录来源。

制品及证据：内外资产选择和资料库纳入记录。

适用边界：宽泛资产视图不是单一数据库或默认所有外部模型都适用。

来源块：C220-web-2025:05-architecture-content:b00763, C220-web-2025:05-architecture-content:b00764, C220-web-2025:05-architecture-content:b00765, C220-web-2025:05-architecture-content:b00766

<details><summary>展开本节完整英文来源</summary>

6.2. Enterprise Continuum and Architecture Re-Use

The simplest way of thinking of the Enterprise Continuum is as a view of
the repository of all the architecture assets. It can contain
Architecture Descriptions, models, building blocks, patterns,
architecture viewpoints, and other artifacts — that exist both within
the enterprise and in the IT industry at large, which the enterprise considers to have available for the development of architectures for the
enterprise.

Examples of internal architecture and solution artifacts are the
deliverables of previous architecture work, which are available for re-use. Examples of external architecture and solution artifacts are the wide variety of industry reference models and architecture patterns that
exist, and are continually emerging, including those that are highly
generic (such as the TOGAF TRM); those specific to certain aspects of IT (such as a web services architecture, or a generic manageability architecture); those specific to certain types of information processing, such as e-Commerce, supply chain management, etc.; and those specific to certain vertical industries, such as the models generated by vertical consortia like the TM Forum (in the Telecommunications sector),
ARTS (Retail), Energistics ® (Petrotechnical), etc.

The Enterprise Architecture determines which architecture and solution artifacts an organization includes in its Architecture Repository. Re-use is a major consideration in this decision.

</details>

<a id="tag_06_03"></a>
## 6.3. Constituents of the Enterprise Continuum

概念：企业连续体含总体上下文分类及架构、方案两个专化连续体。

适用条件：区分背景约束、ABB和可复用SBB。

逻辑关系：上下文资产影响架构；架构连续体组织可复用ABB并指导方案选择；方案连续体解释实现及产品系统服务共同性/差异。

决策方法：先判别资产用途和类别，再追溯指导/实现。

制品及证据：上下文资产、ABB/SBB分类及图6-1关系。

适用边界：源称上下文不直接用于ADM，但不能理解为忽略它们对ADM的约束；三者并非互斥的物理仓库。

来源块：C220-web-2025:05-architecture-content:b00767, C220-web-2025:05-architecture-content:b00768, C220-web-2025:05-architecture-content:b00769, C220-web-2025:05-architecture-content:b00770, C220-web-2025:05-architecture-content:b00771, C220-web-2025:05-architecture-content:b00772, C220-web-2025:05-architecture-content:b00773, C220-web-2025:05-architecture-content:b00774

<details><summary>展开本节完整英文来源</summary>

6.3. Constituents of the Enterprise Continuum

An overview of the context and constituents of the Enterprise Continuum is shown in Figure 6-1 .



Figure 6-1: Enterprise Continuum

The Enterprise Continuum is partitioned into three distinct continua as
follows:

The Enterprise Continuum (see Section 6.4, “Enterprise Continuum in Detail” ) is the outermost continuum and classifies assets
related to the context of the overall Enterprise Architecture The Enterprise Continuum classes of assets may influence architectures,
but are not directly used during the ADM architecture development. The
Enterprise Continuum classifies contextual assets used to develop
architectures, such as policies, standards, strategic initiatives,
organizational structures, and enterprise-level capabilities. The
Enterprise Continuum can also classify solutions (as opposed to
descriptions or specifications of solutions). Finally, the Enterprise
Continuum contains two specializations, namely the Architecture and Solutions Continua. The Architecture Continuum (see Section 6.4.1, “Architecture Continuum” ) offers a consistent way to define and
understand the generic rules, representations, and relationships in an architecture, including traceability and derivation relationships (e.g., to show that an Organization-Specific Architecture is based on an industry or generic standard) The Architecture Continuum represents a structuring of Architecture Building Blocks (ABBs) which are re-usable architecture assets. ABBs evolve through their development lifecycle from abstract and generic entities to fully expressed Organization-Specific Architecture assets. The Architecture Continuum assets will be used to guide and select the
elements in the Solutions Continuum (see below). The Architecture
Continuum shows the relationships among foundational frameworks (such as the TOGAF framework), common system architectures (such as the III-RM), industry architectures, and Enterprise Architectures. The Architecture Continuum is a useful tool to discover commonality and eliminate unnecessary redundancy. The Solutions Continuum (see Section 6.4.2, “Solutions Continuum” ) provides a consistent way to describe and understand the
implementation of the assets defined in the Architecture Continuum The Solutions Continuum defines what is available in the organizational
environment as re-usable SBBs. The solutions are the results of
agreements between customers and business partners that implement the
rules and relationships defined in the architecture space. The Solutions
Continuum addresses the commonalities and differences among the products, systems, and services of implemented systems.

The Enterprise Continuum classifies architecture assets that are
applicable across the entire scope of the Enterprise Architecture. These
assets, which may be referred to as building blocks, can represent a
variety of elements that collectively define and constrain the
Enterprise Architecture. They can take the form of business goals and
objectives, strategic initiatives, capabilities, policies, standards,
and principles.

The Enterprise Continuum also contains the Architecture Continuum and the Solutions Continuum. Each of these continua is described in greater detail in the following sections.

</details>

<a id="tag_06_04"></a>
## 6.4. Enterprise Continuum in Detail

概念：连续体分类企业内外所有相关资产，并必须准确反映外部上下文。

适用条件：法律/市场技术、业务战略转型及当前运营影响架构。

逻辑关系：上下文定义ABB→SBB→真实方案→基线运营；实际表现形成未来变革需求并反馈目标架构。

决策方法：核查上下文适用范围和真实运营证据，形成反馈。

制品及证据：上下文因素、实现/运营映射及新需求证据。

适用边界：TOGAF范围外因素仍重要；不可把设计预测当实际运营表现。

来源块：C220-web-2025:05-architecture-content:b00775, C220-web-2025:05-architecture-content:b00776, C220-web-2025:05-architecture-content:b00777, C220-web-2025:05-architecture-content:b00778, C220-web-2025:05-architecture-content:b00779, C220-web-2025:05-architecture-content:b00780, C220-web-2025:05-architecture-content:b00781, C220-web-2025:05-architecture-content:b00782

<details><summary>展开本节完整英文来源</summary>

6.4. Enterprise Continuum in Detail

The Enterprise Continuum is intended to represent the classification of
all assets that are available to an enterprise. It classifies assets
that exist within the enterprise along with other assets in the wider
environment that are relevant to the enterprise, such as products,
research, market factors, commercial factors, business strategies, and
legislation.

The TOGAF Standard is intended to be a framework for conducting
Enterprise Architecture and as a result many of the assets that reside within the Enterprise Continuum are beyond the specific consideration of
the TOGAF framework.

However, architectures are fundamentally shaped by concerns outside the practice of architecture and it is therefore of paramount importance that any architecture must accurately reflect external context.

The specific contextual factors to be identified and incorporated in an
architecture will vary from architecture to architecture. However, typical contextual factors for architecture development are likely to include:

External influencing factors, such as regulatory change, technological advances, and competitor activity Business strategy and context, including mergers, acquisitions, and
other business transformation requirements Current business operations, reflecting deployed architectures and solutions

By observing the context for architecture, it can be seen that
architecture development activity exists within a wider enterprise
lifecycle of continuous change.

ABBs are defined in relation to a set of contextual factors and then
realized through SBBs. SBBs are deployed as live solutions and become a
part of the baseline operating model of the enterprise. The operating
model of the enterprise and empiric information on the performance of
the enterprise shapes the context and requirements for future change.
Finally, these new requirements for change create a feedback loop to
influence the creation of new Target Architectures.

</details>

<a id="tag_06_04_01"></a>
## 6.4.1. Architecture Continuum

概念：架构连续体由基础、通用系统、行业到组织特定表达逐渐详细的要求。

适用条件：发现可复用架构及分类相关架构。

逻辑关系：可描述逻辑到物理、横向到纵向、通用到特化、分类到完整规格的进展；中间可有其他类型。

决策方法：按可用相关设计概念定位并朝通用端寻找复用。

制品及证据：架构分类及派生/复用关系。

适用边界：四种类型不是固定流程阶段，图上位置不必等同时间顺序。

来源块：C220-web-2025:05-architecture-content:b00783, C220-web-2025:05-architecture-content:b00784, C220-web-2025:05-architecture-content:b00785, C220-web-2025:05-architecture-content:b00786, C220-web-2025:05-architecture-content:b00787, C220-web-2025:05-architecture-content:b00788, C220-web-2025:05-architecture-content:b00789, C220-web-2025:05-architecture-content:b00790, C220-web-2025:05-architecture-content:b00791, C220-web-2025:05-architecture-content:b00792

<details><summary>展开本节完整英文来源</summary>

6.4.1. Architecture Continuum

The Architecture Continuum illustrates how architectures are developed
and evolved across a continuum ranging from Foundation Architectures,
such as the TOGAF ® Series Guide: The TOGAF ® Technical Reference Model (TRM) through Common Systems
Architectures, and Industry Architectures, and to an enterprise’s own
Organization-Specific Architectures.



Figure 6-2: Architecture Continuum

The requirements are addressed in
increasing detail from left to right. The architect will typically look to find re-usable architectural elements toward the left of the
continuum.

The four particular architecture types illustrated in Figure 6-2 are intended to indicate the range of
different types of architecture that may be developed at different
points in the continuum; they are not fixed stages in a process.

Many different types of architecture may occur at points in between
those illustrated in Figure 6-2 . Although the evolutionary transformation continuum illustrated does not represent a formal process, it does represent a progression, which occurs at several
levels:

Logical to physical Horizontal (IT-focused) to vertical (business-focused) Generalization to specialization Taxonomy to complete and specific architecture specification

At each point in the continuum, an architecture is designed in terms of
the design concepts and building blocks available and relevant to that
point.

The four architectures illustrated in Figure 6-2 represent main classifications of potential architectures, and will be
relevant and familiar to many architects. They are analyzed in detail below.

</details>

<a id="tag_06_04_01_01"></a>
## 6.4.1.1. Foundation Architecture

概念：基础架构提供通用组件、关系、原则和指南供更具体架构构建。

适用条件：特化组织架构。

逻辑关系：ADM支持特化；TRM是基础架构例子。

决策方法：核查所选通用基础与组织需要。

制品及证据：基础架构及TRM引用。

适用边界：采用例子不表示组织技术组合已合规或无需裁剪。

来源块：C220-web-2025:05-architecture-content:b00793, C220-web-2025:05-architecture-content:b00794, C220-web-2025:05-architecture-content:b00795

<details><summary>展开本节完整英文来源</summary>

6.4.1.1. Foundation Architecture

A Foundation Architecture consists of generic components,
inter-relationships, principles, and guidelines that provide a
foundation on which more specific architectures can be built. The TOGAF
ADM is a process that would support specialization of such Foundation
Architectures in order to create organization-specific models.

The TOGAF TRM is an example of a Foundation Architecture. It is a
fundamental architecture upon which other, more specific architectures
can be based. See the TOGAF ® Series Guide: The TOGAF ® Technical Reference Model (TRM) for more details.

</details>

<a id="tag_06_04_01_02"></a>
## 6.4.1.2. Common Systems Architectures

概念：通用系统架构为多领域可复用的问题域方案选择/集成基础服务。

适用条件：安全、管理、网络、运营等领域。

逻辑关系：总体功能不完整但相应问题域完整；要求、块和跨域标准支持复用；III-RM为应用域无边界信息流参考。

决策方法：界定问题域完整性，选择标准与可复用块。

制品及证据：通用系统架构、领域块/标准及III-RM引用。

适用边界：问题域完整不能当全企业功能完整；复用低成本是潜力不是实测结果。

来源块：C220-web-2025:05-architecture-content:b00796, C220-web-2025:05-architecture-content:b00797, C220-web-2025:05-architecture-content:b00798, C220-web-2025:05-architecture-content:b00799, C220-web-2025:05-architecture-content:b00800, C220-web-2025:05-architecture-content:b00801

<details><summary>展开本节完整英文来源</summary>

6.4.1.2. Common Systems Architectures

Common Systems Architectures guide the selection and integration of specific services from the Foundation Architecture to create an
architecture useful for building common (i.e., highly re-usable)
solutions across a wide number of relevant domains.

Examples of Common Systems Architectures include: a security
architecture, a management architecture, a network architecture, an
operations architecture, etc. Each is incomplete in terms of overall
system functionality, but is complete in terms of a particular problem
domain (security, manageability, networking, operations, etc.), so that
solutions implementing the architecture constitute re-usable building
blocks for the creation of functionally complete operating states of the
enterprise.

Other characteristics of Common Systems Architectures include:

Reflects requirements specific to a generic problem domain Defines building blocks specific to a generic problem domain Defines business, data, application, or technology standards for
implementing these building blocks Provides building blocks for easy re-use and lower costs

The TOGAF Integrated Information Infrastructure Reference Model (III-RM)
— see the TOGAF ® Series Guide: The TOGAF Integrated Information Infrastructure Reference Model (III-RM) — is a reference model that supports describing Common Systems
Architecture in the Application Domain that focuses on the requirements,
building blocks, and standards relating to the vision of Boundaryless
Information Flow.

</details>

<a id="tag_06_04_01_03"></a>
## 6.4.1.3. Industry Architectures

概念：行业架构结合通用与行业组件解决特定行业客户问题。

适用条件：行业要求、标准、逻辑数据流程、应用业务规则与互操作。

逻辑关系：行业模型提供构建块及系统集合测试指导。

决策方法：核查本行业范围及引用模型适用性。

制品及证据：行业架构、行业模型/标准和测试指导。

适用边界：原文还使用generic problem domain措辞，不能由此删去行业特定性；源例不等于当前模型版本验证。

来源块：C220-web-2025:05-architecture-content:b00802, C220-web-2025:05-architecture-content:b00803, C220-web-2025:05-architecture-content:b00804, C220-web-2025:05-architecture-content:b00805, C220-web-2025:05-architecture-content:b00806

<details><summary>展开本节完整英文来源</summary>

6.4.1.3. Industry Architectures

Industry Architectures guide the integration of common systems
components with industry-specific components, and guide the creation of
industry solutions for targeted customer problems within a particular
industry.

A typical example of an industry-specific component is a data model
representing the business capabilities and processes specific to a
particular vertical industry, such as the Retail industry’s “Active Store” architecture, or an Industry Architecture that incorporates the
Energistics Data Model (refer to www.energistics.org ).

Other characteristics of Industry Architectures include:

Reflects requirements and standards specific to a vertical industry Defines building blocks specific to a generic problem domain Contains industry-specific logical data and process models Contains industry-specific applications and process models, as well as industry-specific business rules Provides guidelines for testing collections of systems Encourages levels of interoperability throughout the industry

</details>

<a id="tag_06_04_01_04"></a>
## 6.4.1.4. Organization-Specific Architectures

概念：组织特定架构指导企业或关联企业网络的最终方案部署与定制。

适用条件：全域运营及企业特定需求。

逻辑关系：可需多个粒度/分区架构；具体模型和块支持产品方案服务选择、度量及演进。

决策方法：按组织范围粒度分解，制定选择标准和成长路径。

制品及证据：组织特定架构、块、业务/数据/应用/技术模型及选择准则。

适用边界：特定不等于单一永久架构；最终定制指导不证明部署已完成。

来源块：C220-web-2025:05-architecture-content:b00807, C220-web-2025:05-architecture-content:b00808, C220-web-2025:05-architecture-content:b00809, C220-web-2025:05-architecture-content:b00810, C220-web-2025:05-architecture-content:b00811

<details><summary>展开本节完整英文来源</summary>

6.4.1.4. Organization-Specific Architectures

Organization-Specific Architectures describe and guide the final deployment of solution components for a particular enterprise or extended network of connected enterprises.

There may be a variety of Organization-Specific Architectures that are needed to effectively cover the organization’s requirements by defining the architectures in increasing levels of detail. Alternatively, this might result in several more detailed Organization-Specific Architectures for specific entities within the global enterprise. Breaking down Organization-Specific Architectures into constituent pieces is addressed in the TOGAF Standard — Applying the ADM .

The Organization-Specific Architecture guides the final customization of
the solution, and has the following characteristics:

Provides a means to communicate and manage business operations across
all four architecture domains Reflects requirements specific to a particular enterprise Defines building blocks specific to a particular enterprise Contains organization-specific business models, data, applications,
and technologies Provides a means to encourage implementation of appropriate solutions
to meet business needs Provides the criteria to measure and select appropriate products,
solutions, and services Provides an evolutionary path to support growth and new business needs

</details>

<a id="tag_06_04_02"></a>
## 6.4.2. Solutions Continuum

概念：方案连续体在相应架构层次填入采购产品或开发组件的实现规格/构造。

适用条件：方案库存和复用库管理。

逻辑关系：向具体端提供方案价值，向通用端从企业需要寻找可用资源。

决策方法：在满足需求同时检查通用方案复用及层级关联。

制品及证据：方案资产库及架构实现映射。

适用边界：连续体位置不是质量排名或必经采购阶段。

来源块：C220-web-2025:05-architecture-content:b00812, C220-web-2025:05-architecture-content:b00813, C220-web-2025:05-architecture-content:b00814, C220-web-2025:05-architecture-content:b00815, C220-web-2025:05-architecture-content:b00816, C220-web-2025:05-architecture-content:b00817, C220-web-2025:05-architecture-content:b00818

<details><summary>展开本节完整英文来源</summary>

6.4.2. Solutions Continuum

The Solutions Continuum represents the detailed specification and construction of the architectures at the corresponding levels of the
Architecture Continuum. At each level, the Solutions Continuum is a
population of the architecture with reference building blocks — either
purchased products or built components — that represent a solution to the enterprise’s business need expressed at that level. A populated repository based on the Solutions Continuum can be regarded as a solutions inventory or re-use library, which can add significant value to the task of managing and implementing improvements to the enterprise.

The Solutions Continuum is illustrated in Figure 6-3 .



Figure 6-3: Solutions Continuum

“Moving to the right” on the Solutions Continuum is focused on providing
solutions value (i.e., foundation solutions provide value in creating
common systems solutions; common systems solutions are used to create
industry solutions; and industry solutions are used to create
organization-specific solutions). “Moving to the left” on the Solutions
Continuum is focused on addressing enterprise needs. These two
viewpoints are significant for a company attempting to focus on its
needs while maximizing the use of available resources through leverage.

The following subsections describe each of the solution types within the
Solutions Continuum.

</details>

<a id="tag_06_04_02_01"></a>
## 6.4.2.1. Foundation Solutions

概念：基础方案是通用概念、工具、产品、服务及能力组件。

适用条件：支撑更具体实现。

逻辑关系：专业培训咨询和支持服务也属方案，可含语言、OS、数据结构及组织/IT运营方式。

决策方法：按具体需要选择可用基础。

制品及证据：基础方案及服务来源。

适用边界：基础方案不限硬件软件，样例不保证投资价值或升级服务已落实。

来源块：C220-web-2025:05-architecture-content:b00819, C220-web-2025:05-architecture-content:b00820, C220-web-2025:05-architecture-content:b00821

<details><summary>展开本节完整英文来源</summary>

6.4.2.1. Foundation Solutions

Foundation Solutions are highly generic concepts, tools, products,
services, and solution components that are the fundamental providers of
capabilities. Services include professional services — such as training
and consulting services — that ensure the maximum investment value from
solutions in the shortest possible time; and support services — such as
Help Desk — that ensure the maximum possible value from solutions
(services that ensure timely updates and upgrades to the products and
systems).

Example Foundation Solutions would include programming languages,
operating systems, foundational data structures (such as EDIFACT),
generic approaches to organization structuring, foundational structures
for organizing IT operations (such as ITIL ® or the IT4IT Reference Architecture), etc.

</details>

<a id="tag_06_04_02_02"></a>
## 6.4.2.2. Common Systems Solutions

概念：通用系统方案实现通用问题域架构，组合产品与服务且可能认证/品牌化。

适用条件：共性运营/信息需要如事务高可用、可扩展仓库、管理和安全。

逻辑关系：体现共性要求/能力而非客户或行业特定；技术供应商、SaaS和业务外包可提供不同类型。

决策方法：核查共同能力及需要的适配范围。

制品及证据：通用系统方案组成及共性能力。

适用边界：may be certified不证明已认证；供应方类别是典型例而非唯一许可来源。

来源块：C220-web-2025:05-architecture-content:b00822, C220-web-2025:05-architecture-content:b00823, C220-web-2025:05-architecture-content:b00824, C220-web-2025:05-architecture-content:b00825

<details><summary>展开本节完整英文来源</summary>

6.4.2.2. Common Systems Solutions

A Common Systems Solution is an implementation of a Common Systems
Architecture comprised of a set of products and services, which may be
certified or branded. It represents the highest common denominator for
one or more solutions in the industry segments that the Common Systems
Solution supports.

Common Systems Solutions represent collections of common requirements and capabilities, rather than those specific to a particular customer or industry. Common Systems Solutions provide organizations with operating
environments specific to operational and informational needs, such as high availability transaction processing and scalable data warehousing systems. Examples of Common Systems Solutions include an enterprise management system product or a security system product.

Computer systems vendors are the typical providers of technology-centric Common Systems Solutions. “Software as a service” vendors are typical providers of common application solutions. Business process outsourcing vendors are typical providers of business capability-centric Common Systems Solutions.

</details>

<a id="tag_06_04_02_03"></a>
## 6.4.2.3. Industry Solutions

概念：行业方案实现行业架构，提供行业可复用组件/服务包。

适用条件：采购并裁剪到组织要求。

逻辑关系：通用/基础组件加行业组件，可含物理数据模式、专用终端及其他行业产品服务。

决策方法：核查行业组成和组织适配需要。

制品及证据：行业方案包及基础/通用/行业映射。

适用边界：ready to be tailored不是已满足组织全部要求或已经交付。

来源块：C220-web-2025:05-architecture-content:b00826, C220-web-2025:05-architecture-content:b00827, C220-web-2025:05-architecture-content:b00828, C220-web-2025:05-architecture-content:b00829, C220-web-2025:05-architecture-content:b00830

<details><summary>展开本节完整英文来源</summary>

6.4.2.3. Industry Solutions

An Industry Solution is an implementation of an Industry Architecture,
which provides re-usable packages of common components and services
specific to an industry.

Fundamental components are provided by Common Systems Solutions and/or
Foundation Solutions, and are augmented with industry-specific
components. Examples include: a physical database schema or an
industry-specific point-of-service device.

Industry Solutions are industry-specific, aggregate procurements that
are ready to be tailored to an individual organization’s requirements.

In some cases an industry solution may include not only an
implementation of the Industry Architecture, but also other solution
elements, such as specific products, services, and systems solutions
that are appropriate to that industry.

</details>

<a id="tag_06_04_02_04"></a>
## 6.4.2.4. Organization-Specific Solutions

概念：组织特定方案实现组织架构所需业务能力，含最多人员流程特定内容。

适用条件：真实运营支持及服务水平管理。

逻辑关系：从行业/通用/基础方案构建，定义SLA、关键运营参数和质量指标；连续体连通架构开发运营沟通。

决策方法：核对运营支持协议与可监测参数，并让运行人员获取所需概念/服务信息。

制品及证据：组织方案、SLA、运营参数、质量指标及交接协议。

适用边界：示例服务等级不是业务已同意目标；实际恢复/一致性/容量指标未知须保留。

来源块：C220-web-2025:05-architecture-content:b00831, C220-web-2025:05-architecture-content:b00832, C220-web-2025:05-architecture-content:b00833, C220-web-2025:05-architecture-content:b00834, C220-web-2025:05-architecture-content:b00835, C220-web-2025:05-architecture-content:b00836

<details><summary>展开本节完整英文来源</summary>

6.4.2.4. Organization-Specific Solutions

An Organization-Specific Solution is an implementation of the
Organization-Specific Architecture that provides the required business
capabilities. Because solutions are designed for specific business
operations, they contain the highest amount of unique content in order to accommodate the varying people and processes of specific
organizations.

Building Organization-Specific Solutions on Industry Solutions, Common Systems Solutions, and Foundation Solutions is the primary purpose of connecting the Architecture Continuum to the Solutions Continuum, as guided by the architects within an enterprise.

An Organization-Specific Solution will be structured in order to support specific SLAs to ensure support of the operational systems at desired service levels. For example, a third-party application hosting provider may offer different levels of support for operational systems. These
agreements would define the terms and conditions of that support.

Other key factors to be defined within an Organization-Specific Solution are the key operating parameters and quality metrics that can be used to monitor and manage the environment.

The Enterprise Continuum can provide a key link between architecture, development, and operations personnel by allowing them to communicate and reach agreement on anticipated operational support requirements.
Operations personnel can in turn access the Enterprise Continuum to
obtain information regarding the operation concepts and service support requirements of the deployed system.

</details>

<a id="tag_06_05"></a>
## 6.5. The Enterprise Continuum and the ADM

概念：ADM通过采用/适配通用架构方案形成组织特定成果，也可把可信有效的特定成果泛化复用。

适用条件：贯穿各域的架构资产选择。

逻辑关系：向具体端特化、向通用端泛化；TOGAF Library及行业参考供考虑。

决策方法：选择相关抽象级资产，验证特定成果可信有效后再泛化。

制品及证据：采用/适配及泛化复用记录。

适用边界：案例结构通过不能独自证明成果可信有效或允许推广全部业务语义。

来源块：C220-web-2025:05-architecture-content:b00837, C220-web-2025:05-architecture-content:b00838, C220-web-2025:05-architecture-content:b00839, C220-web-2025:05-architecture-content:b00840, C220-web-2025:05-architecture-content:b00841

<details><summary>展开本节完整英文来源</summary>

6.5. The Enterprise Continuum and the ADM

The TOGAF ADM describes the process of developing an enterprise-specific
architecture and an enterprise-specific solution(s) which conform to that architecture by adopting and adapting (where appropriate) generic architectures and solutions (left to right in the continuum
classification). In a similar fashion, specific architectures and
solutions that prove to be credible and effective will be generalized
for re-use (right to left in the continuum classification).

At relevant places throughout the TOGAF ADM, there are pointers to
useful architecture assets at the relevant level of generality in the
continuum classification. These assets can include reference models from The Open Group and industries at large.

The TOGAF Library provides reference models for consideration for use in developing an organization’s architecture.

However, in developing architectures in the various domains within an overall Enterprise Architecture, the architect will need to consider the
use and re-use of a wide variety of different architecture assets, and
the Enterprise Continuum provides an approach for categorizing and
communicating these different assets.

</details>

<a id="tag_06_06"></a>
## 6.6. The Enterprise Continuum and Your Organization

概念：本节导入三个连续体之间关系及组织应用。

适用条件：组织内使用连续体。

逻辑关系：关系与实际组织架构安排在子节。

决策方法：据上下文使用后续关系指导。

制品及证据：组织应用引用。

适用边界：导读不新增必经链条。

来源块：C220-web-2025:05-architecture-content:b00842, C220-web-2025:05-architecture-content:b00843

<details><summary>展开本节完整英文来源</summary>

6.6. The Enterprise Continuum and Your Organization

The preceding sections have described the Enterprise Continuum, the
Architecture Continuum, and the Solutions Continuum. The following
sections describe the relationships between each of the three continua
and how these relationships should be applied within your organization.

</details>

<a id="tag_06_06_01"></a>
## 6.6.1. Relationships

概念：三个连续体分别提供上下文、架构及可实现方案分类。

适用条件：理解指导、方向与支持关系并提高复用。

逻辑关系：基础架构指导方案，方案实现并支持架构，其他层同理；组织特定可直接含通用/基础组件。

决策方法：核查实际指导/实现关系及跨层复用。

制品及证据：连续体关系与图6-4映射。

适用边界：明确不是严格串联链；不能强制基础→通用→行业→组织逐层经过。

来源块：C220-web-2025:05-architecture-content:b00844, C220-web-2025:05-architecture-content:b00845, C220-web-2025:05-architecture-content:b00846, C220-web-2025:05-architecture-content:b00847, C220-web-2025:05-architecture-content:b00848, C220-web-2025:05-architecture-content:b00849, C220-web-2025:05-architecture-content:b00850, C220-web-2025:05-architecture-content:b00851, C220-web-2025:05-architecture-content:b00852

<details><summary>展开本节完整英文来源</summary>

6.6.1. Relationships

Each of the three continua contains information about the evolution of
the architectures during their lifecycle:

The Enterprise Continuum provides an overall context for architectures
and solutions, and classifies assets that apply across the entire scope
of the enterprise The Architecture Continuum provides a classification mechanism for
assets that collectively define the architecture at different levels of
evolution from generic to specific The Solutions Continuum provides the classification for assets to
describe specific solutions for the organization that can be implemented
to achieve the intent of the architecture

The relationships between the Architecture Continuum and Solutions
Continuum are shown in Figure 6-4 .



Figure 6-4: Relationships between Architecture and Solutions Continua

The relationship between the Architecture Continuum and the Solutions Continuum is one of guidance, direction, and support. For example, Foundation Architectures guide the creation or selection of Foundation
Solutions. Foundation Solutions support the Foundation Architecture by helping to realize the architecture defined in the Architecture Continuum. The Foundation Architecture also guides development of Foundation Solutions, by providing architectural direction,
requirements, and principles that guide selection, and realization of
appropriate solutions. A similar relationship exists between the other
elements of the Enterprise Continuum.

The Enterprise Continuum presents mechanisms to help improve
productivity through leverage. The Architecture Continuum offers a
consistent way to understand the different architectures and their
components. The Solutions Continuum offers a consistent way to
understand the different products, systems, services, and solutions
required.

The Enterprise Continuum should not be interpreted as representing
strictly chained relationships. Organization-Specific Architectures
could have components from a Common Systems Architecture, and
Organization-Specific Solutions could contain Foundation Solutions. The relationships depicted in Figure 6-1 are an illustration showing opportunities for leveraging architecture and solution components.

</details>

<a id="tag_06_06_02"></a>
## 6.6.2. Your Enterprise

概念：组织可采用、适配既有架构或从头开发，ADM帮助各类架构生成维护与复用。

适用条件：治理企业系统和共享/行业/部门范围。

逻辑关系：推荐本组织基础和通用系统架构，行业或部门架构按需要；内外已有资产可复用。

决策方法：按系统范围确定所需架构类型和采用/适配/开发策略。

制品及证据：组织架构集合及复用策略。

适用边界：推荐不意味着每种架构都必须单独制作；复用效率需实际验证。

来源块：C220-web-2025:05-architecture-content:b00853, C220-web-2025:05-architecture-content:b00854, C220-web-2025:05-architecture-content:b00855

<details><summary>展开本节完整英文来源</summary>

6.6.2. Your Enterprise

The TOGAF Standard provides a method for you to “architect” the systems
in your enterprise. Your architecture organization will have to deal with each type of architecture described above. For example, it is recommended that you have your own Foundation Architecture that governs
all of your systems. You should also have your own Common Systems
Architectures that govern major shared systems — such as the networking system or management system. You may have your own industry-specific
architectures that govern the way your systems must behave within your
industry. Finally, any given department or organization within your business may need its own individual Organization-Specific Architecture to govern the systems within that department.

Your architecture organization will either adopt or adapt existing
architectures, or will develop its own architectures from the ground up.
In either case, the TOGAF Standard is a tool to help. It provides a
method to assist you in generating/maintaining any type of architecture
within the Architecture Continuum while leveraging architecture assets
already defined, internal or external to your organization. The TOGAF ADM helps you to re-use architecture assets, making your architecture organization more efficient and effective.

</details>

<a id="chap07"></a>
## 7. Architecture Repository

概念：架构资料库的章节标题。

适用边界：分类结构、各库及外部记录在子节。

来源块：C220-web-2025:05-architecture-content:b00856

<details><summary>展开本节完整英文来源</summary>

7. Architecture Repository

</details>

<a id="tag_07_01"></a>
## 7.1. Overview

概念：成熟架构能力需资产正式分类、保存过程和工具；资料库是更大企业资料库的一部分。

适用条件：管理大量不同抽象层架构产出。

逻辑关系：高层含元模型、能力、架构景观、标准库、参考库、治理库、授权需求库及方案景观，并可连详细设计/部署/服务管理库。

决策方法：分别配置资产含义、管理流程和跨库链接。

制品及证据：资料库八类结构及企业库连接。

适用边界：元模型类源含裁剪方法，不能只当字段表；授权需求必须与架构委员会同意，候选需求不能自动算授权。

来源块：C220-web-2025:05-architecture-content:b00857, C220-web-2025:05-architecture-content:b00858, C220-web-2025:05-architecture-content:b00859, C220-web-2025:05-architecture-content:b00860, C220-web-2025:05-architecture-content:b00861, C220-web-2025:05-architecture-content:b00862, C220-web-2025:05-architecture-content:b00863, C220-web-2025:05-architecture-content:b00864, C220-web-2025:05-architecture-content:b00865

<details><summary>展开本节完整英文来源</summary>

7.1. Overview

Operating a mature Architecture Capability within a large enterprise
creates a huge volume of architectural output. Effective management and
leverage of these architectural work products require a formal taxonomy
for different types of architectural asset alongside dedicated processes
and tools for architectural content storage.

This section provides a structural framework for an Architecture
Repository that allows an enterprise to distinguish between different
types of architectural assets that exist at different levels of
abstraction in the organization. This Architecture Repository is one
part of the wider Enterprise Repository, which provides the capability
to link architectural assets to components of the Detailed Design,
Deployment, and Service Management Repositories.

At a high level, the following classes of architectural information are
expected to be held within an Architecture Repository:

The Architecture Metamodel describes the organizationally tailored
application of an architecture framework, including a method for
architecture development and a metamodel for architecture content The Architecture Capability defines the parameters, structures, and
processes that support governance of the Architecture Repository The Architecture Landscape presents an architectural representation
of assets in use, or planned, by the enterprise at particular points in
time The Standards Library captures the standards with which new
architectures must comply, which may include industry standards,
selected products and services from suppliers, or shared services
already deployed within the organization The Reference Library provides guidelines, templates, patterns, and
other forms of reference material that can be leveraged in order to
accelerate the creation of new architectures for the enterprise The Governance Repository provides a record of governance activity
across the enterprise The Architecture Requirements Repository provides a view of all
authorized architecture requirements which have been agreed with the
Architecture Board The Solutions Landscape presents an architectural representation of
the SBBs supporting the Architecture Landscape which have been planned
or deployed by the enterprise

The relationships between these areas of the Architecture Repository are
shown in Figure 7-1 .



Figure 7-1: Overview of Architecture Repository

The following sections describe the structure and content of the
repository areas.

</details>

<a id="tag_07_02"></a>
## 7.2. Architecture Landscape

概念：架构景观保存企业在特定时间的状态视图。

适用条件：按全企业多相关者需要组织架构粒度。

逻辑关系：战略长期全局定向、分段更详运营/项目群组合、能力具体单位及增量/工作包项目。

决策方法：区分粒度与时间状态，按管理需要定位。

制品及证据：战略、分段、能力架构景观。

适用边界：粒度不同于连续体通用性或基线/目标状态；Capability Architecture不等于人员能力等级。

来源块：C220-web-2025:05-architecture-content:b00866, C220-web-2025:05-architecture-content:b00867, C220-web-2025:05-architecture-content:b00868

<details><summary>展开本节完整英文来源</summary>

7.2. Architecture Landscape

The Architecture Landscape holds architectural views of the state of the enterprise at particular points in time. Due to the sheer volume and the diverse stakeholder needs throughout an entire enterprise, the Architecture Landscape is divided into three levels of granularity:

Strategic Architectures (see the TOGAF Standard — Architecture Development Method ) show a long-term summary view of the entire enterprise. Strategic Architectures provide an organizing framework for operational and change activity and allow for
direction setting at an executive level Segment Architectures (see the TOGAF Standard — Architecture Development Method ) provide more detailed operating
models for areas within an enterprise. Segment Architectures can be used at the program or portfolio level to organize and operationally align more detailed change activity Capability Architectures (see the TOGAF Standard — Architecture Development Method ) show in a more detailed
fashion how the enterprise can support a particular unit of capability. Capability Architectures are used to provide an overview of current
capability, target capability, and capability increments and allow for
individual work packages and projects to be grouped within managed portfolios and programs

</details>

<a id="tag_07_03"></a>
## 7.3. Reference Library

概念：参考库的分组标题。

适用边界：来源、类型与分类在子节。

来源块：C220-web-2025:05-architecture-content:b00869

<details><summary>展开本节完整英文来源</summary>

7.3. Reference Library

</details>

<a id="tag_07_03_01"></a>
## 7.3.1. Overview

概念：参考库存参考架构、参考模型、视点库、模板及可复用指导。

适用条件：从标准机构、供应商、行业、模板和企业实践发展架构。

逻辑关系：架构与模型关系也适用于参考架构/模型，两者均可通用或组织特定；连续体可分类，粒度/分区选择不同参考。

决策方法：核查来源、抽象/具体程度及范围；无所需元素时反馈需求以纳入通用参考。

制品及证据：参考库、来源、分类与缺失元素需求。

适用边界：文献常混用参考架构/模型，不能据名称合并；IT4IT/eTOM/SID例子需按源范围理解，不假设最新版本。

来源块：C220-web-2025:05-architecture-content:b00870, C220-web-2025:05-architecture-content:b00871, C220-web-2025:05-architecture-content:b00872, C220-web-2025:05-architecture-content:b00873, C220-web-2025:05-architecture-content:b00874, C220-web-2025:05-architecture-content:b00875, C220-web-2025:05-architecture-content:b00876, C220-web-2025:05-architecture-content:b00877, C220-web-2025:05-architecture-content:b00878, C220-web-2025:05-architecture-content:b00879, C220-web-2025:05-architecture-content:b00880

<details><summary>展开本节完整英文来源</summary>

7.3.1. Overview

The Reference Library provides a repository to hold reference materials that should be used to develop architectures. Reference materials held may be obtained from a variety of sources, including:

Standards bodies Product and service vendors Industry communities or forums Standard templates Enterprise best practice

The Reference Library should contain:

Reference Architectures Reference Models Viewpoint Library Templates Note: The terms reference architecture and reference model are not used carefully in most literature. Reference architecture and reference model have the same relationship as architecture and model. Either can
exist as either generic or an organization-specific state. Typically, a generic reference architecture provides the architecture team with an outline of their organization-specific reference architecture that
will be customized for a specific organization. For example, a generic reference architecture may identify that there is a need for data models. An example of a reference architecture is the IT4IT Reference Architecture which also defines a common information model for IT
management. Another example is the TM Forum eTOM and SID as an
organization-specific reference architecture.

In order to segregate different classes of architecture reference
materials, the Reference Library can use the Architecture Continuum as a method for classification.



Figure 7-2: Architecture Continuum

The Architecture Continuum, as shown in Figure 7-2 ,
can be viewed as a Reference Library classification scheme. As such it illustrates how reference architectures can be organized across a range — from Foundation Architectures, and Industry-Specific Architectures, to an Organization-Specific Architecture.

The enterprise needs and business requirements are addressed in
decreasing abstraction from left to right. The architect will typically
find more re-usable architectural elements toward the left of the range. When elements are not found, the requirements for the missing elements are passed to the left of the range for incorporation.

Through this exercise it is important to keep in mind the concepts of levels and partitions. At different levels of granularity there may exist reference materials appropriate to the level, and partitions within the Architecture Landscape can be expected to use different reference material (see the TOGAF Standard — Applying the ADM ).

</details>

<a id="tag_07_04"></a>
## 7.4. Standards Library

概念：标准库的分组标题。

适用边界：标准义务、类别、生命周期及分类在子节。

来源块：C220-web-2025:05-architecture-content:b00881

<details><summary>展开本节完整英文来源</summary>

7.4. Standards Library

</details>

<a id="tag_07_04_01"></a>
## 7.4.1. Overview

概念：标准库存架构必须遵循的规格，供明确治理和客观符合性评价。

适用条件：项目理解和规划标准义务。

逻辑关系：易访问且无歧义的标准支持客观检查。

决策方法：核查适用规范能被访问并可判定符合性。

制品及证据：标准库及明确规格。

适用边界：可访问文本不等于实际符合，含糊标准需补明而非自动通过。

来源块：C220-web-2025:05-architecture-content:b00882, C220-web-2025:05-architecture-content:b00883, C220-web-2025:05-architecture-content:b00884

<details><summary>展开本节完整英文来源</summary>

7.4.1. Overview

The Standards Library provides a repository area to hold a set of
specifications, to which architectures must conform. Establishment of a Standards Library provides an unambiguous basis for Architecture
Governance because:

The standards are easily accessible to projects and therefore the obligations of the project can be understood and planned for Standards are stated in a clear and unambiguous manner, so that
compliance can be objectively assessed

</details>

<a id="tag_07_04_02"></a>
## 7.4.2. Types of Standard

概念：标准分法律监管义务、企业选择采用的行业标准和组织标准。

适用条件：确定不同标准治理来源。

逻辑关系：法律义务外部强制；行业标准需主动监测；组织标准需豁免和演进过程。

决策方法：核实来源与采用范围，建立监测及适用豁免程序。

制品及证据：分类标准、采用记录、监测和豁免流程。

适用边界：本节不是具体法律意见或现行法规调查；不能把组织豁免延伸为法律义务豁免。

来源块：C220-web-2025:05-architecture-content:b00885, C220-web-2025:05-architecture-content:b00886, C220-web-2025:05-architecture-content:b00887

<details><summary>展开本节完整英文来源</summary>

7.4.2. Types of Standard

Standards typically fall into three classes:

Legal and Regulatory Obligations : these standards are mandated by law and therefore an enterprise must comply or face serious consequences Industry Standards : these standards are established by industry bodies, such as The Open Group, and are then selected by the enterprise for adoption Industry Standards offer potential for interoperation and sharing across enterprises, but also fall outside of the control of the enterprise and therefore must be actively monitored. Organizational Standards : these standards are set within the
organization and are based on business aspiration (e.g., selection of standard applications to support portfolio consolidation) Organizational Standards require processes to allow for exemptions and standards evolution.

</details>

<a id="tag_07_04_03"></a>
## 7.4.3. Standards Lifecycle

概念：标准典型生命周期为拟议、试行、有效、逐步退出和退役。

适用条件：管理新标准试验与存量退出。

逻辑关系：试行受特定试点条件；有效通常首选；退出可继续复用但不鼓励新增；退役通常应移除且变更仅在退役计划内。

决策方法：定期复核阶段和状态变更对景观影响，安排行动。

制品及证据：标准状态、试点条件、影响分析及退出计划。

适用边界：typical通常指导需结合组织过程；仅改状态字段不证明景观已迁移或豁免获批。

来源块：C220-web-2025:05-architecture-content:b00888, C220-web-2025:05-architecture-content:b00889, C220-web-2025:05-architecture-content:b00890, C220-web-2025:05-architecture-content:b00891

<details><summary>展开本节完整英文来源</summary>

7.4.3. Standards Lifecycle

Standards do not generally exist for all time. New standards are
identified and managed through a lifecycle process. Typically, standards pass through the following stages:

Proposed Standard : a potential standard has been identified for the
organization, but has not yet been evaluated for adoption Provisional Standard (also known as a Trial Standard ): a
Provisional Standard has been identified as a potential standard for the
organization, but has not been tried and tested to a level where its
value is fully understood Projects wishing to adopt Provisional Standards may do so, but under
specific pilot conditions, so that the viability of the standard can be
examined in more detail. Standard (also known as an Active Standard ): a Standard defines a
mainstream solution that should generally be used as the approach of
choice Phasing-Out Standard (also known as a Deprecated Standard ): a
Phasing-Out Standard is approaching the end of its useful lifecycle Projects that are re-using existing components can generally continue to
make use of Phasing-Out Standards. Deployment of new instances of the
Phasing-Out Standard is generally discouraged. Retired Standard (also known as an Obsolete Standard ): a Retired
Standard is no longer accepted as valid within the landscape In most cases, remedial action should be taken to remove the Retired
Standard from the landscape. Change activity on a Retired Standard
should only be accepted as a part of an overall decommissioning plan.

All standards should be periodically reviewed to ensure that they sit
within the right stage of the standards lifecycle. As a part of
standards lifecycle management, the impact of changing the lifecycle
status should be addressed to understand the landscape impact of a
standards change and plan for appropriate action to address it.

</details>

<a id="tag_07_04_04"></a>
## 7.4.4. Standards Classification within the Standards Library

概念：标准按企业元模型构建块及业务/数据/应用/技术域分类。

适用条件：定义批准块清单或使用情景约束。

逻辑关系：各类型可关联标准；域标准覆盖能力/角色/安全治理、编码结构归属复制访问、应用通信使用、硬软件开发。

决策方法：核对标准所约束类型、批准清单或具体用法。

制品及证据：域标准分类及构建块/使用条件映射。

适用边界：批准产品与允许任何用法不同，应用标准不可代替数据归属和访问规则。

来源块：C220-web-2025:05-architecture-content:b00892, C220-web-2025:05-architecture-content:b00893, C220-web-2025:05-architecture-content:b00894, C220-web-2025:05-architecture-content:b00895, C220-web-2025:05-architecture-content:b00896

<details><summary>展开本节完整英文来源</summary>

7.4.4. Standards Classification within the Standards Library

Standards within the Standards Library are categorized according to the
building blocks within the TOGAF Enterprise Metamodel. Each metamodel
entity can potentially have standards associated with it (e.g., Business
Service, Technology Component).

Standards may relate to “approved” building blocks (e.g., a list of
standard technology components) or may specify appropriate use of a
building block (e.g., scenarios where messaging infrastructure is
appropriate, application communication standards are defined).

At the top level, standards are classified in line with the TOGAF
architecture domains, including the following areas:

Business Standards : Standard shared business capabilities Standard role and actor definitions Security and governance standards for business activity Data Standards : Standard coding and values for data Standard structures and formats for data Standards for origin and ownership of data Restrictions on replication and access Applications Standards : Standard/shared applications supporting specific business functions Standards for application communication and interoperation Standards for access, presentation, and style Technology Standards ; Standard hardware products Standard software products Standards for software development

</details>

<a id="tag_07_05"></a>
## 7.5. Governance Repository

概念：治理库的分组标题。

适用边界：目的及内容在子节。

来源块：C220-web-2025:05-architecture-content:b00897

<details><summary>展开本节完整英文来源</summary>

7.5. Governance Repository

</details>

<a id="tag_07_05_01"></a>
## 7.5.1. Overview

概念：治理库存持续项目治理的共享信息。

适用条件：保留重大决定、标准偏离和架构理由供未来替换/其他相关者参考。

逻辑关系：历史理由揭示可能隐蔽的约束；多相关者关心治理结果。

决策方法：持续记录并提供可检索决定依据。

制品及证据：治理记录及决定理由。

适用边界：记录结果不自动授予其他项目采用同一偏离的权限。

来源块：C220-web-2025:05-architecture-content:b00898, C220-web-2025:05-architecture-content:b00899, C220-web-2025:05-architecture-content:b00900

<details><summary>展开本节完整英文来源</summary>

7.5.1. Overview

The Governance Repository provides a repository area to hold shared
information relating to the ongoing governance of projects. Maintaining
a shared repository of governance information is important, because:

Decisions made during projects (such as standards deviations or the
rationale for a particular architectural approach) are important to
retain and access on an ongoing basis For example, if a system is to be replaced, having sight of the key
architectural decisions that shaped the initial implementation is highly
valuable as it will highlight constraints that may otherwise be
obscured. Many stakeholders are interested in the outcome of project governance
(e.g., other projects, customers of the project, the Architecture Board,
etc.)

</details>

<a id="tag_07_05_02"></a>
## 7.5.2. Contents of the Governance Repository

概念：治理库应含决定日志、符合性/能力评估、日历、受治理项目组合及绩效记录。

适用条件：持续检查、审计和架构职能评价。

逻辑关系：决定含产品、重大特征、标准偏离/生命周期、变更评价批准、复用；检查记录项目状态/检查表/建议；能力评估周期跟踪；绩效依职能章程。

决策方法：核对每类记录有范围、证据和时间，追踪评估与检查行动。

制品及证据：治理日志、正式检查、能力评估、审查日历、组合及绩效度量。

适用边界：批准记录与建议不同；绩效字段不是实测绩效，部分项目评估能力不代表全部项目均已评估。

来源块：C220-web-2025:05-architecture-content:b00901, C220-web-2025:05-architecture-content:b00902, C220-web-2025:05-architecture-content:b00903

<details><summary>展开本节完整英文来源</summary>

7.5.2. Contents of the Governance Repository

The Governance Repository should contain the following items:

Decision Log : a log of all architecturally significant decisions
that have been made in the organization This would typically include: Product selections Justification for major architectural features of projects Standards deviations Standards lifecycle changes Change Request evaluations and approvals Re-use assessments Compliance Assessments : at key checkpoint milestones in the progress
of a project, a formal architecture review will be carried out This review will measure the compliance of the project to the defined
architecture standards. For each project, this log should include: Project overview Progress overview (timeline, status, issues, risks, dependencies,
etc.) Completed architecture checklists Standards compliance assessment Recommended actions Capability Assessments : depending on their objectives, some projects
will carry out assessments of business, IT, or Architecture Capability These assessments should be periodically carried out and tracked to
ensure that appropriate progress is being made. This log should include: Templates and reference models for executing Capability Assessments Business Capability Assessments IT capability, maturity, and impact assessments Architecture maturity assessments Calendar : the Calendar should show a schedule of in-flight projects
and formal review sessions to be held against these projects Project Portfolio : the Project Portfolio should hold summary
information about all in-flight projects that fall under Architecture
Governance, including: The name and description of the project Architectural scope of the project Architectural roles and responsibilities associated with the project Performance Measurement : based on a charter for the architecture
function, a number of performance criteria will typically be defined The Performance Measurement log should capture metrics relating to
project governance and any other performance metrics relating to the
architecture charter so that performance can be measured and evaluated
on an ongoing basis.

</details>

<a id="tag_07_06"></a>
## 7.6. The Architecture Requirements Repository

概念：架构需求库的分组标题。

适用边界：持续管理及内容在子节。

来源块：C220-web-2025:05-architecture-content:b00904

<details><summary>展开本节完整英文来源</summary>

7.6. The Architecture Requirements Repository

</details>

<a id="tag_07_06_01"></a>
## 7.6.1. Overview

概念：各ADM阶段都用需求库记录管理架构需求，收集可贯穿周期且需经过阶段/治理批准。

适用条件：战略、分段和能力需求全过程。

逻辑关系：需求管理负责库内容、完整性及各阶段可访问性。

决策方法：持续维护需求来源、批准状态和可访问完整性。

制品及证据：需求库、阶段/治理批准及完整性记录。

适用边界：源称phase不能解释为Phase I；采集不等于批准。

来源块：C220-web-2025:05-architecture-content:b00905, C220-web-2025:05-architecture-content:b00906, C220-web-2025:05-architecture-content:b00907, C220-web-2025:05-architecture-content:b00908

<details><summary>展开本节完整英文来源</summary>

7.6.1. Overview

The Architecture Requirements Repository is used by all phases of the ADM to record and manage all information relevant to the architecture requirements. The requirements address the many types of architecture requirements; i.e., strategic, segment, and capability requirements which are the major drivers for the Enterprise Architecture.

Requirements can be gathered at every stage of the architecture
development cycle and need to be approved through the various phases and governance processes.

The Requirements Management phase is responsible for the management of
the contents of the Architecture Requirements Repository and ensuring
the integrity of all requirements and their availability for access by
all phases.

</details>

<a id="tag_07_06_02"></a>
## 7.6.2. Contents of the Architecture Requirements Repository

概念：需求库存特定时间企业所需状态，按战略、分段和能力粒度组织。

适用条件：区分全局运营变更、区域运营模型及具体工作包项目需求。

逻辑关系：业务结果逐渐反映于方案景观；要求满足后为审计归档。

决策方法：按粒度时间追溯方案实际结果，核查满足再归档。

制品及证据：三级需求、方案结果/满足证据及归档记录。

适用边界：方案被计划或选中不等于业务结果实现；归档须有满足依据。

来源块：C220-web-2025:05-architecture-content:b00909, C220-web-2025:05-architecture-content:b00910, C220-web-2025:05-architecture-content:b00911, C220-web-2025:05-architecture-content:b00912, C220-web-2025:05-architecture-content:b00913

<details><summary>展开本节完整英文来源</summary>

7.6.2. Contents of the Architecture Requirements Repository

The Architecture Requirements Repository holds architectural
requirements of the required state of the enterprise at particular
points in time.

Due to the sheer volume and the diverse stakeholder
needs throughout the architecture development cycle, the Architecture
Requirements are divided into three levels of granularity:

Strategic Architecture Requirements show a long-term summary view of
the requirements for the entire enterprise Strategic Architecture Requirements identify operational and change
requirements for direction setting at an executive level. Segment Architecture Requirements provide more detailed operating
model requirements for areas within an enterprise Segment Architecture Requirements may identify requirements at the
program or portfolio level to identify and align more detailed change
activity. Capability Architecture Requirements identify the detailed requirements for a particular unit of capability Capability Architecture Requirements identify requirements for individual work packages and projects to be grouped within managed portfolios and programs.

The business outcomes for architecture requirements will be reflected in the Solutions Landscape over time. When this occurs, the architecture
requirements are met and archived for audit purposes.

</details>

<a id="tag_07_07"></a>
## 7.7. Solutions Landscape

概念：方案景观保存支持ABB的拟定/已部署SBB，可按连续体及战略/分段/能力分类。

适用条件：管理产品服务、工具系统信息及供应商特定实现/运营说明。

逻辑关系：SBB与ABB要求相连；方案自身产生的业务数据内容由方案负责。

决策方法：区分候选与部署状态，核查实现映射及运营描述。

制品及证据：SBB方案景观、ABB映射、状态和运营资料。

适用边界：景观不包含方案产生的数据内容；同处景观不证明全部SBB已部署或需求满足。

来源块：C220-web-2025:05-architecture-content:b00914, C220-web-2025:05-architecture-content:b00915, C220-web-2025:05-architecture-content:b00916, C220-web-2025:05-architecture-content:b00917

<details><summary>展开本节完整英文来源</summary>

7.7. Solutions Landscape

The Solutions Landscape holds the SBBs which support the ABBS specified, developed, and deployed. The building blocks may be products or services which may be categorized according to the Enterprise Continuum categorization and/or the ABB specifications as Strategic, Segment, or Capability SBBs.

SBBs may also include tools, systems, services, and information which
describe the actual solutions that may be selected and their operation.
For example, vendor-specific reference models or vendor-specific Levels
4 and 5 of the IT4IT Reference Architecture would be defined here.

However, the Solutions Landscape will not include the information and
data content produced by the solutions selected; that is the
responsibility of the solutions themselves.

</details>

<a id="tag_07_08"></a>
## 7.8. The Enterprise Repository

概念：企业还有内外开发、运行环境、说明和配置管理等资料库支持架构。

适用条件：连接架构规格与企业实际实现/运维。

逻辑关系：架构资料库是企业资料库的一部分。

决策方法：建立可定位跨库引用和责任边界。

制品及证据：企业资料库及架构关联。

适用边界：不要求把所有实现和运行数据复制进架构资料库。

来源块：C220-web-2025:05-architecture-content:b00918, C220-web-2025:05-architecture-content:b00919, C220-web-2025:05-architecture-content:b00920

<details><summary>展开本节完整英文来源</summary>

7.8. The Enterprise Repository

While the Architecture Repository holds information concerning the
Enterprise Architecture and associated specifications and artifacts,
there are a considerable number of enterprise repositories that support
the architecture both inside and outside of the enterprise.

These can include development repositories, specific operating
environments, instructions, and configuration management repositories.

</details>

<a id="tag_07_09"></a>
## 7.9. External Repositories

概念：外部资料库的分组标题。

适用边界：模型、标准与委员会批准记录在子节。

来源块：C220-web-2025:05-architecture-content:b00921

<details><summary>展开本节完整英文来源</summary>

7.9. External Repositories

</details>

<a id="tag_07_09_01"></a>
## 7.9.1. External Reference Models

概念：行业参考模型可帮助理解及开发参考架构。

适用条件：选择外部参考。

逻辑关系：模型提供参考输入而非现成组织架构。

决策方法：核查模型来源与本组织需要。

制品及证据：外部模型引用。

适用边界：本节未指定唯一模型或证明当下版本适用。

来源块：C220-web-2025:05-architecture-content:b00922, C220-web-2025:05-architecture-content:b00923

<details><summary>展开本节完整英文来源</summary>

7.9.1. External Reference Models

There are many industry reference models available which may assist in
understanding the role of and developing the reference architectures.

</details>

<a id="tag_07_09_02"></a>
## 7.9.2. External Standards

概念：外部标准可为行业、最佳实践或正式标准，如ISO/IEEE/政府。

适用条件：查找外部规范来源。

逻辑关系：应与企业选择采用/强制义务相区分。

决策方法：记录具体规范及采用适用范围。

制品及证据：外部标准引用。

适用边界：例子不代表所有规范自动强制适用或已核实最新版本。

来源块：C220-web-2025:05-architecture-content:b00924, C220-web-2025:05-architecture-content:b00925

<details><summary>展开本节完整英文来源</summary>

7.9.2. External Standards

These relate to industry, best practice, or formal defined standards
used by leading organizations. Examples include ISO, IEEE, and
Government standards.

</details>

<a id="tag_07_09_03"></a>
## 7.9.3. Architecture Board Approvals

概念：架构委员会影响EA的决定常在会议纪要中，法律/监管原因可能存于资料库之外的文档档案。

适用条件：定位正式批准证据。

逻辑关系：外部存放不妨碍需要跨库追溯。

决策方法：引用真实纪要及其权限/范围，遵守记录位置约束。

制品及证据：委员会决定纪要及档案引用。

适用边界：不能仅因库内缺少纪要推断未批准，也不能以占位纪要冒充真实决策权限。

来源块：C220-web-2025:05-architecture-content:b00926, C220-web-2025:05-architecture-content:b00927

<details><summary>展开本节完整英文来源</summary>

7.9.3. Architecture Board Approvals

Decisions made by the Architecture Board which affect the Enterprise
Architecture are often recorded in the minutes of meetings. These
minutes are often held in documentation archives which are excluded from
the Architecture Repository for legal or regulatory reasons.

</details>

