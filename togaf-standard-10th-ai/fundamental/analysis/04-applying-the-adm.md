# ADM应用：当前语义解析

本页为逐节语义解释，不能把解释当全文译文。本卷另有[逐块中文正文](../chinese-text/04-applying-the-adm.md)，已写正文的最终独立语义校核仍待完成。

[英文及离线原文](../web-2025/volumes/04-applying-the-adm/index.html)

<a id="chap01"></a>
## 1. Introduction

概念：本卷说明不同风格、迭代、全景层级与分区应用。

适用条件：将通用ADM用于具体组织和问题。

逻辑关系：应用规则调整范围、描述和治理连接。

决策方法：结合后续四章选择方法配置。

制品及证据：ADM应用约定及裁剪理由。

适用边界：章节标题不另立固定流程。

来源块：C220-web-2025:04-applying-the-adm:b00035, C220-web-2025:04-applying-the-adm:b00036, C220-web-2025:04-applying-the-adm:b00037, C220-web-2025:04-applying-the-adm:b00038

<details><summary>展开本节完整英文来源</summary>

1. Introduction

This chapter provides an introduction to the guidance provided in the TOGAF Standard — Applying the ADM (this document).

The Architecture Development Method (ADM) process can be adapted to deal
with many different usage scenarios, including different process styles
(e.g., the use of iteration) and also specific specialist architectures
(such as security). Guidelines included within this document are as
follows:

Using the TOGAF Framework with Different Architecture Styles (see Section 1.1, “Using the TOGAF Framework with Different Architecture Styles” ) discusses how the framework can be adapted to
different architectural styles Applying Iteration to the ADM (see Chapter 2, Applying Iteration to the ADM )
discusses the concept of iteration and shows potential strategies for applying iterative concepts to the ADM Applying the ADM across the Architecture Landscape (see Chapter 3, Applying the ADM Across the Architecture Landscape )
discusses the different types of architecture engagement
that may occur at different levels of the enterprise — this section then also discusses how the ADM process can be focused to support different types of engagement Architecture Partitioning (see Chapter 4, Architecture Partitioning )
discusses how partitions are used to
simplify the development and management of the Enterprise Architecture

</details>

<a id="tag_01_01"></a>
## 1.1. Using the TOGAF Framework with Different Architecture Styles

概念：风格在焦点、形式、技术、材料、主题和时间方面有独特特征。

适用条件：全景中可同时存在不同风格。

逻辑关系：先识别特征，再调整模型、视点、工具及必要元模型扩展；主导风格可触发预备阶段能力调整。

决策方法：B/C/D选择能回应关切的资源，检验对其他利益相关者及基线的影响。

制品及证据：风格特征清单、视点、元模型扩展与能力变更。

适用边界：通常不需大改TOGAF；外部风格资料是引用而非本六卷已收齐来源。

来源块：C220-web-2025:04-applying-the-adm:b00039, C220-web-2025:04-applying-the-adm:b00040, C220-web-2025:04-applying-the-adm:b00041, C220-web-2025:04-applying-the-adm:b00042, C220-web-2025:04-applying-the-adm:b00043, C220-web-2025:04-applying-the-adm:b00044, C220-web-2025:04-applying-the-adm:b00045, C220-web-2025:04-applying-the-adm:b00046, C220-web-2025:04-applying-the-adm:b00047, C220-web-2025:04-applying-the-adm:b00048, C220-web-2025:04-applying-the-adm:b00049, C220-web-2025:04-applying-the-adm:b00050, C220-web-2025:04-applying-the-adm:b00051, C220-web-2025:04-applying-the-adm:b00052, C220-web-2025:04-applying-the-adm:b00053

<details><summary>展开本节完整英文来源</summary>

1.1. Using the TOGAF Framework with Different Architecture Styles

The TOGAF framework is designed to be flexible and is used with various architectural styles.

Architectural styles differ in terms of focus, form, techniques,
materials, subject, and time period. The TOGAF Standard is a generic
framework intended to be used in a wide variety of environments. It is a
flexible and extensible framework that can be readily adapted to a
number of architectural styles.

An organization’s Architecture Landscape can be expected to contain
architecture work that is developed in many architectural styles. The
TOGAF Standard ensures that the needs of each stakeholder are
appropriately addressed in the context of other stakeholders and the
Baseline Architecture.

When using the TOGAF Standard to support a specific architectural style
the practitioner must take into account the combination of distinctive
features in which architecture is performed or expressed. As a first
step, the distinctive features of a style must be identified.

The second step is determining how these distinctive features will be
addressed. Addressing a distinctive style should not call for
significant changes to the TOGAF framework; instead it should adjust the
models, viewpoints, and tools used by the practitioner.

In Phase B, Phase C, and Phase D the practitioner is expected to select
the relevant architecture resources, including models, viewpoints, and
tools, to properly describe the architecture domain and demonstrate that
stakeholder concerns are addressed (see the TOGAF Standard — ADM Techniques ).
Depending upon the distinctive features, different architectural styles
will add new elements that must be described, highlight existing
elements, adjust the notation used to describe the architecture, and
focus the architect on some stakeholders or stakeholder concerns.

Addressing the distinctive features will usually include extensions to
the Architecture Content Metamodel and the use of specific notation or
modeling techniques and the identification of viewpoints. Dominance of a
particular architectural style can direct the practitioner to revisit
the Preliminary Phase to make changes to the Architecture Capability or
to address a distinctive feature in the expected scope of a single ADM
cycle.

Style-specific reference models and maturity models are commonly used
tools that support a practitioner.

During the lifetime of the TOGAF framework many architectural styles
have been developed to address key problems facing practitioners and to
demonstrate how the TOGAF framework can be made more relevant within
defined contexts.

Some of these have been developed by The Open Group Forums and Work
Groups working in specific areas and have been published in Guides,
White Papers, and Standards. Examples include:

TOGAF ® Series Guide: Using the TOGAF ® Framework to Define and Govern Service-Oriented Architectures TOGAF ® Series Guide: Integrating Risk and Security within a TOGAF ® Enterprise Architecture

Some of these have been developed collaboratively between The Open Group
and other bodies. Examples include:

TOGAF ® and SABSA ® Integration Archi Banking Group: Combining the BIAN Reference Model, ArchiMate ® Modeling Notation, and the TOGAF ® Framework Exploring Synergies between TOGAF ® and Frameworx TOGAF ® 9 and DoDAF 2.0

The TOGAF Library (see www.opengroup.org/togaf-library )
is a structured library of resources that support the TOGAF Standard.

</details>

<a id="chap02"></a>
## 2. Applying Iteration to the ADM

概念：迭代是管理架构复杂性及生命周期的实际应用方式。

适用条件：描述顺序可能被误读为瀑布时。

逻辑关系：多轮完整ADM、同一轮跨阶段和能力自身演进是不同迭代维度。

决策方法：按架构目标设计回返和检查点。

制品及证据：迭代计划与输入输出依赖。

适用边界：不把示意圆环解释成唯一执行日程。

来源块：C220-web-2025:04-applying-the-adm:b00054

<details><summary>展开本节完整英文来源</summary>

2. Applying Iteration to the ADM

</details>

<a id="tag_02_01"></a>
## 2.1. Overview

概念：多项目构建全景、同周期跨阶段综合、架构能力更新是三种迭代概念。

适用条件：每轮工作受架构工作请求范围约束，项目可并行且相互触发。

逻辑关系：基线目标和B/C/D/E/F活动互相反馈；A或H的能力需求可回到预备阶段。

决策方法：区分工作范围改变与能力更新，必要时启动独立项目。

制品及证据：请求范围、全景更新、阶段回返及能力变化记录。

适用边界：迭代不取消项目启动或全景治理。

来源块：C220-web-2025:04-applying-the-adm:b00055, C220-web-2025:04-applying-the-adm:b00056, C220-web-2025:04-applying-the-adm:b00057, C220-web-2025:04-applying-the-adm:b00058, C220-web-2025:04-applying-the-adm:b00059, C220-web-2025:04-applying-the-adm:b00060, C220-web-2025:04-applying-the-adm:b00061, C220-web-2025:04-applying-the-adm:b00062, C220-web-2025:04-applying-the-adm:b00063

<details><summary>展开本节完整英文来源</summary>

2.1. Overview

The graphical representation of the TOGAF ADM and the description of the
ADM phases discretely in order, as shown in the TOGAF Standard — Architecture Development Method , can be read to imply a deterministic waterfall methodology.
This method of presentation is provides a means of quickly communicating the basics of architecture development and the
architecture development cycle. In practice, two key concepts are used to manage the complexity of developing an Enterprise Architecture and managing its lifecycle — iteration and levels; see Chapter 3, Applying the ADM Across the Architecture Landscape .
The two concepts are tightly linked.

The ADM supports a number of concepts that are characterized as iteration. First, iteration describes the process of describing a comprehensive Architecture Landscape through multiple ADM cycles based
upon individual initiatives bound to the scope of the Request for Architecture Work. Second, iteration describes the integrated process of
developing an architecture where the activities described in different ADM phases interact to produce an integrated architecture. In order to concisely describe the activity and outputs, this latter iteration is
described in sequential terms. Third, iteration describes the process of managing change to the organization’s Architecture Capability.

Iteration to develop a comprehensive Architecture Landscape:

Projects will exercise through the entire ADM cycle, commencing with
Phase A Each cycle of the ADM will be bound by a Request for Architecture Work.
The architecture output will populate the Architecture Landscape, either extending the landscape described, or changing the landscape where
required. Separate projects may operate their own ADM cycles concurrently, with
relationships between the different projects One project may trigger the initiation of another project Typically, this is used when higher-level architecture initiatives identify opportunities or solutions that require more detailed
architecture, or when a project identifies landscape impacts outside the scope of its Request for Architecture Work.

Iteration within an ADM cycle (Architecture Development iteration):

Projects may operate multiple ADM phases concurrently Typically, this is used to manage the inter-relationship between Business Architecture, Information Systems Architecture, and Technology
Architecture. Projects may cycle between ADM phases, in planned cycles covering multiple phases Typically, this is used to converge on a detailed Target Architecture when higher-level architecture does not exist to provide context and
constraint. Projects may return to previous phases to update work products with new information Typically, this is used to converge on an executable Architecture Roadmap or Implementation and Migration Plan, when the implementation
details and scope of change trigger a change or re-prioritization of
stakeholder requirements.

Iteration to manage the Architecture Capability (Architecture Capability
iteration):

Projects may require a new iteration of the Preliminary Phase to (re-)establish aspects of the Architecture Capability identified in Phase A to address a Request for Architecture Work Projects may require a new iteration of the Preliminary Phase to adjust the organization’s Architecture Capability as a result of
identifying new or changed requirements for Architecture Capability as a result of a Change Request in Phase H

</details>

<a id="tag_02_02"></a>
## 2.2. Iteration Cycles

概念：能力、开发、过渡规划、治理四类迭代聚合相关活动。

适用条件：依架构工作目的组织活动。

逻辑关系：开发迭代综合B/C/D并扩展E/F检查可实施性；规划形成路线图；治理管理目标方向的变更。

决策方法：选择聚焦活动并决定必要扩展。

制品及证据：能力配置、架构内容、路线图和治理记录。

适用边界：图外侧圈表示活动焦点，不是每圈强制单独项目。

来源块：C220-web-2025:04-applying-the-adm:b00064, C220-web-2025:04-applying-the-adm:b00065, C220-web-2025:04-applying-the-adm:b00066, C220-web-2025:04-applying-the-adm:b00067, C220-web-2025:04-applying-the-adm:b00068

<details><summary>展开本节完整英文来源</summary>

2.2. Iteration Cycles

The suggested iteration cycles for the TOGAF ADM are shown in Figure 2-1 , and can be used to effectively group related architectural activities to achieve a specific purpose. These
iteration cycles are referenced in Section 2.3, “Classes of Architecture Engagement” and Section 2.5, “Iteration Considerations” .



Figure 2-1: Iteration Cycles

Architecture Capability iterations support the
creation [ 1 ] and evolution of the required Architecture Capability This includes the initial mobilization of the architecture activity for
a given purpose or architecture engagement type by establishing or adjusting the architecture approach, principles, scope, vision, and governance. Architecture Development iterations allow the creation of
architecture content by cycling through, or integrating, Business, Information Systems, and Technology Architecture phases These iterations ensure that the architecture is considered as a whole. In this type of iteration stakeholder reviews are typically broader. As
the iterations converge on a target, extensions into the Opportunities & Solutions and Migration Planning phases ensure that the architecture’s
implementability is considered as the architecture is finalized. Transition Planning iterations support the creation of formal change roadmaps for a defined architecture Architecture Governance iterations support governance of change activity progressing towards a defined Target Architecture

</details>

<a id="tag_02_03"></a>
## 2.3. Classes of Architecture Engagement

概念：架构参与可识别所需变革、定义变革、治理实施。

适用条件：支持战略、全景/项目组合、基础性/有界变化和实施治理。

逻辑关系：6类参与各有不同焦点、迭代与范围；基础性变革需澄清问题，有界变革已有愿景范围。

决策方法：按问题是否已理解及组织层级选参与类型。

制品及证据：参与声明、范围、对应产物及迭代配置。

适用边界：组合治理的架构维度补充服务/项目管理，不替代其权限。

来源块：C220-web-2025:04-applying-the-adm:b00069, C220-web-2025:04-applying-the-adm:b00070, C220-web-2025:04-applying-the-adm:b00071, C220-web-2025:04-applying-the-adm:b00072, C220-web-2025:04-applying-the-adm:b00073, C220-web-2025:04-applying-the-adm:b00074, C220-web-2025:04-applying-the-adm:b00075, C220-web-2025:04-applying-the-adm:b00076, C220-web-2025:04-applying-the-adm:b00077, C220-web-2025:04-applying-the-adm:b00078, C220-web-2025:04-applying-the-adm:b00079

<details><summary>展开本节完整英文来源</summary>

2.3. Classes of Architecture Engagement

An architecture function or services organization may be called upon to assist an enterprise in a number of different contexts, as the
architectures developed can range from summary to detail, broad to narrow coverage, and current state to future state. In these contexts the concept of iteration should be used in developing the architecture.

Typically, there are three areas of engagement for architects:

Identification of Required Change : outside the context of any change initiative, architecture can be used as a technique to provide
visibility of the IT capability in order to support strategic
decision-making and alignment of execution Definition of Change : where a need to change has been identified, architecture can be used as a technique to define the nature and extent
of change in a structured fashion Within large-scale change initiatives, architectures can be developed to provide detailed Architecture Definition for change initiatives that are
bounded by the scope of a program or portfolio. Implementation of Change : architecture at all levels of the enterprise can be used as a technique to provide design governance to change initiatives by providing big-picture visibility, supplying
structural constraints, and defining criteria on which to evaluate technical decisions

Figure 2-2 and the following table show the classes of Enterprise Architecture engagement.



Figure 2-2: Classes of Enterprise Architecture Engagement

Each of these architecture engagement types is described in Table 2-1 .

Table 2-1:  Architecture Engagement Types Area of Engagement Architecture Engagement Description Identification of Required Change Supporting Business Strategy As the business strategies, objectives, goals, and drivers change, it is
necessary for the enterprise to change in order to maintain alignment. The creation of new business strategies can be supported by Enterprise
Architecture by: Providing visibility of change opportunities Providing elaboration on the practical impacts of a particular
strategic choice Providing tests on the feasibility or viability of a particular
strategic direction Architectural Portfolio Management of the Landscape It is common practice across large organizations for a service
management organization to provide operational reporting and management
of the IT portfolio. Enterprise Architecture can add a further dimension to service
management reporting, by supporting a linkage between operational
performance and the strategic need for IT. Using the traceability between IT and business inherent in Enterprise
Architecture, it is possible to evaluate the IT portfolio against
operational performance data and business needs (e.g., cost,
functionality, availability, responsiveness) to determine areas where
misalignment is occurring and change needs to take place. Architectural Portfolio Management of Projects It is common practice across large organizations for a program
management organization to provide operational reporting and management
of the change portfolio. Enterprise Architecture can add a further dimension to project portfolio
management reporting, by supporting a linkage between project scope,
architectural impact, and business value. Architectural factors can be added to other quantitative project factors
to support strategic decision-making on project priority and funding
levels. Definition of Change Architectural Definition of Foundational Change
Initiatives Foundational change initiatives are change efforts that have a known
objective, but are not strictly scoped or bounded by a shared vision or
requirements. In foundational change initiatives, the initial priority is to
understand the nature of the problem and to bring structure to the
definition of the problem. Once the problem is more effectively understood, it is possible to
define appropriate solutions and to align stakeholders around a common
vision and purpose. Architectural Definition of Bounded Change Initiatives Bounded change initiatives are change efforts that typically arise as
the outcome of a prior architectural strategy, evaluation, or vision. In bounded change initiatives, the desired outcome is already understood
and agreed upon. The focus of architectural effort in this class of
engagement is to effectively elaborate a baseline solution that
addresses the identified requirements, issues, drivers, and constraints. Implementation of Change Architectural Governance of Change
Implementation Once an architectural solution model has been defined, it provides a
basis for design and implementation. In order to ensure that the objectives and value of the defined
architecture are appropriately realized, it is necessary for continuing
Architecture Governance of the implementation process to support design
review, architecture refinement, and issue escalation.

Different classes of architecture engagement at different levels of the
enterprise will require focus in specific areas, as shown in Table 2-2 .

Table 2-2:  Classes of Architecture Engagement at Levels of the Enterprise Engagement Type Focus Iteration Cycles Scope Focus Supporting Business Strategy Architecture Capability Architecture Development (Baseline First) Broad, shallow consideration given to the Architecture Landscape in
order to address a specific strategic question and define terms for more
detailed architecture efforts to address strategy realization. Architectural Portfolio Management of the Landscape Architecture Capability Architecture Development (Baseline First) Focus on physical assessment of baseline applications and technology
infrastructure to identify improvement opportunities, typically within
the constraints of maintaining business as usual. Architectural Portfolio Management of Projects Transition Planning Architecture Governance Focus on projects, project dependencies, and landscape impacts to align
project sequencing in a way that is architecturally optimized. Architectural Definition of Foundational Change Initiatives Architecture Capability Architecture Development (Baseline First) Transition Planning Focus on elaborating a vision through definition of baseline and
identifying what needs to change to transition the baseline to the
target. Architectural Definition of Bounded Change Initiatives Architecture Development (Target First) Transition Planning Focus on elaborating the target to meet a previously defined and agreed
vision, scope, or set of constraints. Use the target as a basis for
analysis to avoid perpetuation of baseline, sub-optimal architectures. Architectural Governance of Change Implementation Architecture
Governance Use the Architecture Vision, constraints, principles,
requirements, Target Architecture definition, and transition roadmap to
ensure that projects realize their intended benefit, are aligned with
each other, and are aligned with wider business need.

</details>

<a id="tag_02_04"></a>
## 2.4. Approaches to Architecture Development

概念：可选择基线优先或目标优先。

适用条件：复杂不明/不一致基线适合前者，已有高层目标适合后者。

逻辑关系：两状态仍互相考虑；焦点选择维持执行一致性。

决策方法：基线已广泛理解时通常优先目标，再按差距需要补基线。

制品及证据：选择理由、基线/目标说明及差距。

适用边界：目标优先不允许完全忽略现有依赖。

来源块：C220-web-2025:04-applying-the-adm:b00080, C220-web-2025:04-applying-the-adm:b00081, C220-web-2025:04-applying-the-adm:b00082, C220-web-2025:04-applying-the-adm:b00083, C220-web-2025:04-applying-the-adm:b00084

<details><summary>展开本节完整英文来源</summary>

2.4. Approaches to Architecture Development

Two approaches can be adopted within the ADM for the development of
architectures:

Baseline First : in this style, an assessment of the baseline
landscape is used to identify problem areas and improvement
opportunities This process is most suitable when the baseline is complex, not clearly
understood, or agreed upon. This approach is common where organizational
units have had a high degree of autonomy. Target First : in this style, the target solution is elaborated in
detail and then mapped back to the baseline, in order to identify change
activity This process is suitable when a target state is agreed at a high level
and where the enterprise wishes to effectively transition to the target
model.

Typically, if the baseline is broadly understood a higher value will be
obtained focusing on the target first then baseline to the extent
necessary to identify changes.

In practical terms, an architecture team will always give informal
consideration to the baseline when analyzing the target (and vice
versa ). In situations where baseline and target are expected to be
considered in parallel by stakeholders, it is recommended that the
architecture team focuses priority on one state in order to maintain
focus and consistency of execution.

</details>

<a id="tag_02_05"></a>
## 2.5. Iteration Considerations

概念：迭代次数、过程及检查点依目的和参与程度设计。

适用条件：部分迭代可一次，部分自然需多次。

逻辑关系：高度参与可频繁非正式检查，低参与可能稀疏正式检查。

决策方法：明确每次迭代目标、退出证据和检查频率。

制品及证据：迭代检查点、参与及审阅证据。

适用边界：原文不给每迭代统一时间盒。

来源块：C220-web-2025:04-applying-the-adm:b00085, C220-web-2025:04-applying-the-adm:b00086, C220-web-2025:04-applying-the-adm:b00087

<details><summary>展开本节完整英文来源</summary>

2.5. Iteration Considerations

Some iteration cycles can be executed once, whereas others have a
natural minimum number of cycles. For some iteration cycles, each
iteration follows the same process; where there is more than one
iteration within a cycle, the process differs slightly for each of the
iterations.

When considering the usage of iteration cycles, it is also necessary to
consider where to place appropriate checkpoints within the process. If
the expected level of stakeholder involvement is high, it may be
sensible to carry out very frequent but informal checkpoints to ensure
that the process is moving in the intended direction. If stakeholders
are less closely involved, then checkpoints may be less frequent but
more formal. Checkpoints at the completion of each iteration cycle, or
at the end of several iteration cycles, are common.

</details>

<a id="tag_02_05_01"></a>
## 2.5.1. Iteration between ADM Cycles

概念：单一描述层级的完整ADM周期可由F启动更细架构项目。

适用条件：需要高层约束指导低层并形成全景。

逻辑关系：Strategic→Segment→Capability是架构层级关系，各层有独立或并行周期。

决策方法：界定细化工作的独立请求及高层约束。

制品及证据：多周期工作请求、治理和约束追溯。

适用边界：图中叠层只说明多个架构，不能推断确切项目数量。

来源块：C220-web-2025:04-applying-the-adm:b00088, C220-web-2025:04-applying-the-adm:b00089, C220-web-2025:04-applying-the-adm:b00090, C220-web-2025:04-applying-the-adm:b00091

<details><summary>展开本节完整英文来源</summary>

2.5.1. Iteration between ADM Cycles

Each iteration completes an ADM cycle at a single level of Architecture
Description. This approach to the ADM uses Phase F (Migration Planning) to initiate new more detailed architecture development projects. This approach is illustrated in Figure 2-3 . This type of iteration highlights the need for higher-level architecture to guide and constrain more detailed architecture. It also highlights that the complete Architecture Landscape is developed by multiple ADM iterations.



Figure 2-3: A Hierarchy of ADM Processes Example

</details>

<a id="tag_02_05_02"></a>
## 2.5.2. Iteration within an ADM Cycle

概念：同一周期中的迭代跨多个阶段，Core/Light/Informal表示活动焦点。

适用条件：基线优先或目标优先、多次规划和治理。

逻辑关系：前两轮先一状态再另一状态，后续共同细化；E/F在开发中轻量，在过渡规划中核心。

决策方法：按迭代目的确定活动深度，向前阶段反馈实施问题。

制品及证据：迭代活动矩阵、可行性/存续性检验和计划修订。

适用边界：Light、Informal、空白不是完成度、免责或允许忽略适用要求。

来源块：C220-web-2025:04-applying-the-adm:b00092, C220-web-2025:04-applying-the-adm:b00093, C220-web-2025:04-applying-the-adm:b00094, C220-web-2025:04-applying-the-adm:b00095, C220-web-2025:04-applying-the-adm:b00096, C220-web-2025:04-applying-the-adm:b00097, C220-web-2025:04-applying-the-adm:b00098, C220-web-2025:04-applying-the-adm:b00099

<details><summary>展开本节完整英文来源</summary>

2.5.2. Iteration within an ADM Cycle

Each iteration cycle crosses multiple TOGAF ADM phases. The following
figures show at a high level which phases should be completed for which
iteration cycle, showing activity that is core (i.e., the primary focus of the iteration), activity that is light (i.e., the secondary focus of
the iteration), and activity that may be informally conducted (i.e.,
some activity may be carried out, but it is not explicitly mentioned in the ADM).



Figure 2-4: Activity by Iteration for Baseline First Architecture Definition



Figure 2-5: Activity by Iteration for Target First Architecture Definition

The suggested iteration cycles mapped to the TOGAF phases are described in Table 2-3 .

Table 2-3:  Iteration cycles mapped to the TOGAF ADM Phases Iteration Cycle Iteration Purpose Description Architecture Development (Baseline First) Iteration 1 Define the Baseline Architecture. This iteration comprises a pass through the Business Architecture,
Information Systems Architecture, and Technology Architecture phases of
the ADM, focusing on definition of the baseline. Opportunities, solutions, and migration plans are also considered to
drive out the focus for change and test feasibility. Iteration 2 Define the Target Architecture and gaps. This iteration comprises a pass through the Business Architecture,
Information Systems Architecture, and Technology Architecture phases of
the ADM, focusing on definition of the target and analyzing gaps against
the baseline. Opportunities, solutions, and migration plans are also considered to
test viability. Iteration n Refine baseline, target, and gaps. Subsequent
Architecture Development iterations attempt to correct and refine the
target to achieve an outcome that is beneficial, feasible, and viable. Architecture Development (Target First) Iteration 1 Define the Target Architecture. This iteration comprises a pass through the Business Architecture,
Information Systems Architecture, and Technology Architecture phases of
the ADM, focusing on definition of the target. Opportunities, solutions, and migration plans are also considered to
drive out the focus for change and test feasibility. Iteration 2 Define the Baseline Architecture and gaps. This iteration comprises a pass through the Business Architecture,
Information Systems Architecture, and Technology Architecture phases of
the ADM, focusing on definition of the baseline and analyzing gaps
against the target. Opportunities, solutions, and migration plans are also considered to
test viability. Iteration n Refine baseline, target, and gaps. Subsequent
Architecture Development iterations attempt to correct and refine the
target to achieve an outcome that is beneficial, feasible, and viable. Transition Planning Iteration 1 Define and agree a set of improvement
opportunities, aligned against a provisional Transition Architecture. The initial iteration of Transition Planning seeks to gain buy-in to a
portfolio of solution opportunities in the Opportunities & Solutions
phase of ADM. This iteration also delivers a provisional Migration Plan. Iteration n Agree the Transition Architecture, refining the
identified improvement opportunities to fit. Subsequent iterations of
Transition Planning seek to refine the Migration Plan, feeding back
issues into the Opportunities & Solutions phase for refinement. Architecture Governance Iteration 1 Mobilize Architecture Governance
and change management processes. The initial Architecture Governance
iteration establishes a process for governance of change and also puts
in place the appropriate people, processes, and technology to support
managed access to and change of the defined architecture. Iteration n Carry out Architecture Governance and change control. Subsequent iterations of the Architecture Governance cycle focus on
periodic reviews of change initiatives to resolve issues and ensure
compliance. Results of a Change Request may trigger another phase to be
revisited; for example, feeding back a new requirement to the
Preliminary Phase to improve the Architecture Capability, or a new
requirement for the architecture into the Architecture Development
phases.

</details>

<a id="tag_02_06"></a>
## 2.6. Conclusions

概念：ADM实际迭代方式取决于组织检查点、参与、团队、成熟度、风险文化及参与类型。

适用条件：制定本组织工作计划。

逻辑关系：六因素决定回返、正式性、试验及团队关系。

决策方法：在组织约束内组合本章方法。

制品及证据：组织因素和选用迭代方式的依据。

适用边界：不宣称单次完成总是可行。

来源块：C220-web-2025:04-applying-the-adm:b00100, C220-web-2025:04-applying-the-adm:b00101, C220-web-2025:04-applying-the-adm:b00102

<details><summary>展开本节完整英文来源</summary>

2.6. Conclusions

All of these techniques are valid applications of the ADM. Combined
together, they represent how the ADM can be used in practice. The ADM
should always be used in an iterative process. How this process is
exercised is dependent upon organizational factors. Particular factors
for consideration include:

The formality and nature of established process checkpoints within
the organization Does the organization mandate that certain groups of activities are
carried out between checkpoints? Does the organization mandate that
certain activities must be finalized before other activities can be
carried out? The level of stakeholder involvement expected within the process Are stakeholders expecting to be closely involved within the development
of a solution, or are they expecting to see a complete set of
deliverables for review and approval? The number of teams involved and the relationships between different
teams Is the entire architecture being developed by a specific team, or is
there a hierarchy of teams with governance relationships between them? The maturity of the solution area and the expected amount of rework
and refinement required to arrive at an acceptable solution Can the solution be achieved in a single pass, or does it require
extensive proof-of-concept and prototyping work to evolve a suitable
outcome? Attitude to risk Does the organizational culture react negatively to partially complete
work products being circulated? Does the organizational culture require
solutions to be proved in a trial environment before they can be
implemented for mainstream application? The class of engagement What is the context for development of the Enterprise Architecture?

</details>

<a id="chap03"></a>
## 3. Applying the ADM Across the Architecture Landscape

概念：架构全景同时包含具体与概括、详细与宏观的描述。

适用条件：组织并管理多个相关架构。

逻辑关系：层级和架构连续体与存储库及分区关联，但分类维度不同。

决策方法：按利益相关者需求组织可导航全景。

制品及证据：全景结构与存储库引用。

适用边界：本章不提供唯一企业组织模型。

来源块：C220-web-2025:04-applying-the-adm:b00103

<details><summary>展开本节完整英文来源</summary>

3. Applying the ADM Across the Architecture Landscape

</details>

<a id="tag_03_01"></a>
## 3.1. Overview

概念：层级和连续体帮助管理不同范围和细节的复杂架构。

适用条件：全景内容繁多且用途不同。

逻辑关系：分类框架需映射实际存储内容与架构分区。

决策方法：检验层级分类是否帮助检索、治理与复用。

制品及证据：全景分类与存储库映射。

适用边界：分类架构不等于制定团队权限。

来源块：C220-web-2025:04-applying-the-adm:b00104, C220-web-2025:04-applying-the-adm:b00105

<details><summary>展开本节完整英文来源</summary>

3.1. Overview

In a typical enterprise, many architectures will be described in the
Architecture Landscape at any point in time. Some architectures will
address very specific needs; others will be more general. Some will
address detail; some will provide a big picture. To address this
complexity, the TOGAF Standard uses the concepts of levels and the
Enterprise Continuum to provide a conceptual framework for organizing
the Architecture Landscape. These concepts are tightly linked with
organizing actual content in the Architecture Repository and any
architecture partitions discussed in the TOGAF Standard — Architecture Content .

</details>

<a id="tag_03_02"></a>
## 3.2. Architecture Landscape

概念：战略、分段、能力三层分别支持执行方向、项目组合/计划和能力增量。

适用条件：以粒度划分全景，以抽象度用连续体进一步分类。

逻辑关系：层级与连续体可组合，通用到特定支持派生追溯及消除冗余。

决策方法：按运行模型定义分组、层级、导航、过程和责任。

制品及证据：三层全景、连续体位置、派生与治理关系。

适用边界：Capability Architecture不是能力目录里单个能力对象，也不规定唯一分组。

来源块：C220-web-2025:04-applying-the-adm:b00106, C220-web-2025:04-applying-the-adm:b00107, C220-web-2025:04-applying-the-adm:b00108, C220-web-2025:04-applying-the-adm:b00109, C220-web-2025:04-applying-the-adm:b00110, C220-web-2025:04-applying-the-adm:b00111, C220-web-2025:04-applying-the-adm:b00112, C220-web-2025:04-applying-the-adm:b00113, C220-web-2025:04-applying-the-adm:b00114, C220-web-2025:04-applying-the-adm:b00115, C220-web-2025:04-applying-the-adm:b00116, C220-web-2025:04-applying-the-adm:b00117, C220-web-2025:04-applying-the-adm:b00118, C220-web-2025:04-applying-the-adm:b00119

<details><summary>展开本节完整英文来源</summary>

3.2. Architecture Landscape

Levels provide a framework for dividing the Architecture Landscape into
three levels of granularity:

Strategic Architecture provides an organizing framework for
operational and change activity and allows for direction setting at an
executive level Segment Architecture provides an organizing framework for
operational and change activity and allows for direction setting and the
development of effective architecture roadmaps at a program or portfolio
level Capability Architecture provides an organizing framework for change
activity and the development of effective architecture roadmaps
realizing capability increments

Figure 3-1 shows a summary of the classification model
for Architecture Landscapes.



Figure 3-1: Summary Classification Model for Architecture Landscapes

The Architecture Continuum provides a method of dividing each level of
the Architecture Landscape (see the TOGAF Standard — Architecture Content ) by abstraction. It offers a consistent way to define and
understand the generic rules, representations, and relationships in an
architecture, including traceability and derivation relationships. The
Architecture Continuum shows the relationships from foundation elements
to organization-specific architecture, as shown in Figure 3-2 .

The Architecture Continuum is a useful tool to discover commonality and
eliminate unnecessary redundancy.



Figure 3-2: Summary of Architecture Continuum

Levels and the Architecture Continuum provide a comprehensive mechanism
to describe and classify the Architecture Landscape.

These concepts can
be used to organize the Architecture Landscape into a set of related
architectures with:

Manageable complexity for each individual architecture or solution Defined groupings Defined hierarchies and navigation structures Appropriate processes, roles, and responsibilities attached to each
grouping

There is no definitive organizing model for architecture, as each
enterprise should adopt a model that reflects its own operating model.

</details>

<a id="tag_03_03"></a>
## 3.3. Developing Architectures at Different Levels

概念：宽而概括架构为窄而详细架构设置方向和约束。

适用条件：不同层利益相关者有不同描述需求。

逻辑关系：可在单周期内迭代不同层，或采用并行ADM层级，也可混合。

决策方法：根据工作请求选择混合策略并保持治理层级。

制品及证据：层间约束及周期关系。

适用边界：层级不同不意味独立于上位治理。

来源块：C220-web-2025:04-applying-the-adm:b00120, C220-web-2025:04-applying-the-adm:b00121, C220-web-2025:04-applying-the-adm:b00122, C220-web-2025:04-applying-the-adm:b00123, C220-web-2025:04-applying-the-adm:b00124

<details><summary>展开本节完整英文来源</summary>

3.3. Developing Architectures at Different Levels

The previous sections have identified that different types of
architecture are required to address different stakeholder needs at
different levels of the organization. Each architecture typically does
not exist in isolation and must therefore sit within a governance
hierarchy. Broad, summary architectures set the direction for narrow and
detailed architectures.

A number of techniques can be employed to use the ADM as a process that
supports such hierarchies of architectures. Essentially there are two
strategies that can be applied:

Architectures at different levels can be developed through iterations
within a single cycle of the ADM process Architectures at different levels can be developed through a hierarchy
of ADM processes, executed concurrently

At the extreme ends of the scale, either of these two options can be
fully adopted. In practice, an architect is likely to need to blend
elements of each to fit the exact requirements of their Request for
Architecture Work. Each of these approaches is described in Chapter 2, Applying Iteration to the ADM .

</details>

<a id="tag_03_04"></a>
## 3.4. Organizing the Architecture Landscape

概念：全景以广度、深度、时间和新近程度组织。

适用条件：理解企业在过去、现状和未来的状态。

逻辑关系：宽范围通常较浅且有效期较长；批准后不维护会随时间失真。

决策方法：区分描述时间、计划有效期和最后维护日期。

制品及证据：基线/多个目标、范围/粒度、版本与维护记录。

适用边界：批准不是永久准确，recency不能等同目标时间。

来源块：C220-web-2025:04-applying-the-adm:b00125, C220-web-2025:04-applying-the-adm:b00126, C220-web-2025:04-applying-the-adm:b00127, C220-web-2025:04-applying-the-adm:b00128

<details><summary>展开本节完整英文来源</summary>

3.4. Organizing the Architecture Landscape

The following characteristics are typically used to organize the
Architecture Landscape to understand the state of the enterprise:

Breadth : the breadth (subject matter) area is generally the primary
organizing characteristic for describing an Architecture Landscape Architectures are functionally decomposed into a hierarchy of specific
subject areas or segments. Depth : with broader subject areas, less detail is needed to ensure
that the architecture has a manageable size and complexity More specific subject matter areas will generally permit (and require)
more detailed architectures. Time : for a specific breadth and depth an enterprise can create a
Baseline Architecture and a set of Target Architectures that stretch
into the future Broader and less detailed architectures will generally be valid for
longer periods of time and can provide a vision for the enterprise that
stretches further into the future. Recency : finally, each architecture view will progress through a
development cycle where it increases in accuracy until finally approved After approval, an architecture will begin to decrease in accuracy if
not actively maintained. In some cases recency may be used as an
organizing factor for historic architectures.

Using the criteria above, architectures can be grouped into Strategic,
Segment, and Capability Architecture levels, as described in Figure 3-1 .

</details>

<a id="chap04"></a>
## 4. Architecture Partitioning

概念：架构分区使复杂性、同时工作及复用可管理。

适用条件：不同组织架构冲突或多团队并行。

逻辑关系：分区奠定治理基础，区别于层级和连续体分类。

决策方法：按运行模型选择分区并定义责任。

制品及证据：分区目录、范围与治理归属。

适用边界：不存在本章规定的唯一分区模型。

来源块：C220-web-2025:04-applying-the-adm:b00129

<details><summary>展开本节完整英文来源</summary>

4. Architecture Partitioning

</details>

<a id="tag_04_01"></a>
## 4.1. Overview

概念：冲突、团队所有权及模块复用是分区理由。

适用条件：需要不同团队同时处理不同架构部分。

逻辑关系：分类准则帮助界定可管理架构和有效治理。

决策方法：明确要解决的冲突与复用边界。

制品及证据：分区问题、拥有者和治理原则。

适用边界：分区不是只把图切小或按域分文件。

来源块：C220-web-2025:04-applying-the-adm:b00130, C220-web-2025:04-applying-the-adm:b00131, C220-web-2025:04-applying-the-adm:b00132, C220-web-2025:04-applying-the-adm:b00133, C220-web-2025:04-applying-the-adm:b00134, C220-web-2025:04-applying-the-adm:b00135, C220-web-2025:04-applying-the-adm:b00136

<details><summary>展开本节完整英文来源</summary>

4.1. Overview

Partitions are used to simplify the development and management of the
Enterprise Architecture.

Partitions lie at the foundation of Architecture Governance and are
distinct from levels and the organizing concepts of the Architecture
Continuum (see the TOGAF Standard — Architecture Content ).

Architectures are partitioned because:

Organizational unit architectures conflict with one another Different teams need to work on different elements of architecture at
the same time and partitions allow for specific groups of architects to
own and develop specific elements of the architecture Effective architecture re-use requires modular architecture segments
that can be taken and incorporated into broader architectures and
solutions

It is impractical to present a definitive partitioning model for
architecture. Each enterprise needs to adopt a partitioning model that
reflects its own operating model.

This chapter discusses the classification criteria that are generally
applied to architectures and how these can be leveraged to partition the
enterprise into a set of architectures with manageable complexity and
effective governance.

</details>

<a id="tag_04_02"></a>
## 4.2. Applying Classification to Create Partitioned Architectures

概念：解决方案按主题/时间/成熟波动分类；架构还按深度匹配受众。

适用条件：建立相关解决方案与架构的分组导航。

逻辑关系：真实全景通常不按抽象度分区，波动性限制未来描述与历史准确性。

决策方法：结合主题、生命周期、成熟度和受众选边界。

制品及证据：分类准则及分区映射。

适用边界：本节对全景描述的抽象限制与连续体通用性分类需区分用途。

来源块：C220-web-2025:04-applying-the-adm:b00137, C220-web-2025:04-applying-the-adm:b00138, C220-web-2025:04-applying-the-adm:b00139, C220-web-2025:04-applying-the-adm:b00140, C220-web-2025:04-applying-the-adm:b00141, C220-web-2025:04-applying-the-adm:b00142, C220-web-2025:04-applying-the-adm:b00143, C220-web-2025:04-applying-the-adm:b00144, C220-web-2025:04-applying-the-adm:b00145, C220-web-2025:04-applying-the-adm:b00146, C220-web-2025:04-applying-the-adm:b00147

<details><summary>展开本节完整英文来源</summary>

4.2. Applying Classification to Create Partitioned Architectures

For the reasons outlined in the previous section, it is valuable to
partition and organize the Enterprise Continuum into a set of related
solutions and architectures with:

Manageable complexity for each individual architecture or solution Defined groupings Defined hierarchies and navigation structures Appropriate processes, roles, and responsibilities attached to each
grouping

Table 4-1 shows how suitable classification criteria can be
used to support partitioning of solutions:

Table 4-1:  Classification Criteria to support Partitioning of Solutions Characteristic Usage to Support Solution Partitioning Subject Matter (Breadth) Solutions are naturally organized into groups to support operational
management and control. Examples of solution partitions according to
subject matter would include applications, departments, divisions,
products, services, service centers, sites, etc. Solution decomposition by subject matter is typically the fundamental
technique for structuring both solutions and the architectures that
represent them. Time Solution lifecycles are typically organized around a timeline,
which allows the impact of solution development, introduction,
operation, and retirement to be managed against other business activity
occurring in similar time periods. Maturity/Volatility The maturity and volatility of a solution will typically impact the
speed of execution required for the solution lifecycle. Additionally, volatility and maturity will shape investment priorities.
Solutions existing in highly volatile environments may be better suited
to rapid, agile development techniques.

Table 4-2 shows how each classification criteria can be used
to support partitioning of architectures:

Table 4-2:  Classification Criteria to support Partitioning of Architectures Characteristic Usage to Support Architecture Partitioning Depth The level of detail within an architecture has a strong correlation to
the stakeholder groups that will be interested in the architecture. Typically, less detailed architectures will be of interest to executive
stakeholders. As architectures increase in detail, their relevance to
implementation and operational personnel will also increase.

In practical terms, architecture discipline is used to support a number
of different types of architecture that are used for different
objectives. The classification criteria described above can be used in
different ways to support the achievement of each objective.

The following characteristics are generally not used to partition an
Architecture Landscape:

Architectures used to describe the Architecture Landscape are
generally not abstract Solution volatility generally prevents architectures from being
defined that are far in the future; volatility also reduces the accuracy
of historic architectures over time, as the organization changes and
adapts to new circumstances

Using the criteria above, architectures can be grouped into partitions.

</details>

<a id="tag_04_02_01"></a>
## 4.2.1. Activities within the Preliminary Phase

概念：预备阶段建立边界、治理和拥有者，优先每架构一个拥有团队。

适用条件：常设团队与临时变革团队共同工作。

逻辑关系：临时团队置于常设团队治理下；明确团队组织、职责范围与架构间符合/复用关系。

决策方法：先确认治理主体、成员汇报线，再分主题深度时间利益相关者及重叠细化。

制品及证据：团队责任分区定义、治理汇报和架构关系。

适用边界：一个拥有者不禁止跨团队协作；实际组织授权需独立确认。

来源块：C220-web-2025:04-applying-the-adm:b00148, C220-web-2025:04-applying-the-adm:b00149, C220-web-2025:04-applying-the-adm:b00150, C220-web-2025:04-applying-the-adm:b00151, C220-web-2025:04-applying-the-adm:b00152, C220-web-2025:04-applying-the-adm:b00153, C220-web-2025:04-applying-the-adm:b00154, C220-web-2025:04-applying-the-adm:b00155, C220-web-2025:04-applying-the-adm:b00156, C220-web-2025:04-applying-the-adm:b00157, C220-web-2025:04-applying-the-adm:b00158, C220-web-2025:04-applying-the-adm:b00159

<details><summary>展开本节完整英文来源</summary>

4.2.1. Activities within the Preliminary Phase

The key objective of the Preliminary Phase is to establish the
Architecture Capability for the enterprise. In practical terms this
activity will require the establishment of a number of architecture
partitions, providing defined boundaries, governance, and ownership.

Generally speaking, each team carrying out architecture activity within
the enterprise will own one or more architecture partitions and will
execute the ADM to define, govern, and realize their architectures.

If more than one team is expected to work on a single architecture, this
can become problematic, as the precise responsibilities of each team are
difficult to establish. For this reason, it is preferable to apply
partitioning to the architecture until each architecture has one owning
team.

Finally, it is worth considering the distinction between standing
capabilities of the enterprise and temporary teams mobilized to support
a particular change initiative. Although the remit of standing teams
within the enterprise can be precisely defined, it is more difficult to
anticipate and specify the responsibilities of (possibly unknown)
temporary architecture teams. In the cases of these temporary teams,
each team should come under the governance of a standing architecture
team and there should be a process within the ADM cycle of these teams
to establish appropriate architecture partitioning.

Steps within the Preliminary Phase to support architecture partitioning
are as follows:

Determine the organization structure for architecture within the
enterprise : the various standing teams that will create the
architecture should be identified For each of these teams, appropriate boundaries should be established,
including: Governance bodies that are applicable to the team Team membership Team reporting lines Determine the responsibilities for each standing architecture team :
for each architecture team, the responsibilities should be identified This step applies partitioning logic to the Enterprise Architecture in
order to firstly identify the scope of each team and secondly to
partition the architecture under the remit of a single team. Once
complete, this step should have partitioned the entire scope of the
enterprise and should have assigned responsibility for each partitioned
architecture to a single team. Partitioning should create a definition
of each architecture that includes: Subject matter areas being covered Level of detail at which the team will work Time periods to be covered Stakeholders Determine the relationships between architectures : once a set of
partitioned architectures has been created, the relationships between
architectures should be developed This step allows governance relationships to be formalized and also
shows where artifacts from one architecture are expected to be re-used
within other architectures. Areas of consideration include: Where do different architectures overlap/dovetail/drill-down? What are the compliance requirements between architectures?

Once the Preliminary Phase is complete, the teams conducting the
architecture should be understood. Each team should have a defined scope
and the relationships between teams and architecture should be
understood. Allocation of teams to architecture scope is illustrated in Figure 4-1 .



Figure 4-1: Allocation of Teams to Architecture Scope

Figure 4-1 shows that:

The Enterprise Layer is defined through collaboration between the Corporate Enterprise Capability and Segment EA Capability The Segment Layer is defined through collaboration between the Corporate Enterprise Capability, the Segment EA Capability, and the Portfolio Team The Capability Layer is defined through collaboration between the Portfolio Team and the Project Team

</details>

<a id="tag_04_03"></a>
## 4.3. Integration

概念：联邦架构需集成框架避免碎片化。

适用条件：大型政府、集团或独立组织单元。

逻辑关系：互操作/迁移/符合原则和标准构建块制品是内容集成约束；跨域、跨组织、愿景到定义/过渡均需整合。

决策方法：将内容集成列为符合条件并复用共同目录与交叉引用。

制品及证据：集成标准、共用业务过程目录、跨域/分段/过渡追溯。

适用边界：共用标识或视图一致性本身不证明业务语义正确。

来源块：C220-web-2025:04-applying-the-adm:b00160, C220-web-2025:04-applying-the-adm:b00161, C220-web-2025:04-applying-the-adm:b00162, C220-web-2025:04-applying-the-adm:b00163, C220-web-2025:04-applying-the-adm:b00164, C220-web-2025:04-applying-the-adm:b00165, C220-web-2025:04-applying-the-adm:b00166, C220-web-2025:04-applying-the-adm:b00167, C220-web-2025:04-applying-the-adm:b00168, C220-web-2025:04-applying-the-adm:b00169

<details><summary>展开本节完整英文来源</summary>

4.3. Integration

The creation of partitioned architectures runs the risk of producing a
fragmented and disjointed collection of architectures that cannot be
integrated to form an overall big picture (see the TOGAF Standard — Architecture Development Method ).

For large complex enterprises, federated architectures — independently
developed, maintained, and managed architectures that are subsequently
integrated within an integration framework — are typical. Federated
architectures typically are used in governments and conglomerates, where
the separate organizational units need separate architectures. Such a
framework specifies the principles for interoperability, migration, and
conformance. This allows specific business units to have architectures
developed and governed as stand-alone architecture projects. More
details and guidance on specifying the interoperability requirements for
different solutions can be found in the TOGAF Standard — ADM Techniques .

In order to mitigate against this risk, standards for content
integration should be defined and Architecture Governance should address
content integration as a condition of architectural compliance. Content
frameworks, such as the TOGAF content framework (refer to the TOGAF Standard — Architecture Content ) can be used to specify standard building blocks and artifacts
that are the subject of content integration standards.

For example, a standard catalog of business processes can be agreed for
an enterprise. Subsequent architectures can then ease integration by
using the same process list and cross-referencing other aspects of the
architecture to those standard processes.

Integration can be addressed from a number of dimensions:

Integration across the architecture domains provides a cross-domain
view of the state of a segment of the enterprise for a point in time Integration across the organizational scope of the business provides a
cross-segment view of the enterprise The Architecture Vision provides an integrated summary of Architecture
Definitions, which provide an integrated summary of Transition
Architectures

Figure 4-2 shows how architectural content can be aggregated using a variety of techniques.



Figure 4-2: Architecture Content Aggregation

</details>

