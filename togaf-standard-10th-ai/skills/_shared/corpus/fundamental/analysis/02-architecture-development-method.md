# 架构开发方法：当前语义解析

本页为逐节语义解释，不能把解释当全文译文。本卷另有[逐块中文正文](../chinese-text/02-architecture-development-method.md)，已写正文的最终独立语义校核仍待完成。

[英文及离线原文](../web-2025/volumes/02-architecture-development-method/index.html)

<a id="chap01"></a>
## 1. Introduction

概念：ADM把开发、生命周期管理、范围与集成连接成一个架构方法。

适用条件：开展企业架构或裁剪企业专用方法前。

逻辑关系：本章由总览、迭代、裁剪、治理、范围、备选与集成展开。

决策方法：先决定架构工作的问题和边界，再选用本章机制。

制品及证据：后续1.1—1.8的工作范围与方法决策。

适用边界：本章导入不单独给出企业范围或批准。

来源块：C220-web-2025:02-architecture-development-method:b00038, C220-web-2025:02-architecture-development-method:b00039

<details><summary>展开本节完整英文来源</summary>

1. Introduction

This chapter introduces the Architecture Development Method (ADM) cycle, adapting the ADM,
architecture scope, and architecture integration.

</details>

<a id="tag_01_01"></a>
## 1.1. ADM Overview

概念：ADM是企业架构开发与生命周期管理的核心方法。

适用条件：组织需要将标准和既有架构资产用于业务需求时。

逻辑关系：业务需求决定如何组合TOGAF元素与其他可用资产。

决策方法：判断资产对本组织需求是否相关。

制品及证据：组织所采用的方法及相关资产。

适用边界：核心方法不是现成组织架构。

来源块：C220-web-2025:02-architecture-development-method:b00040, C220-web-2025:02-architecture-development-method:b00041, C220-web-2025:02-architecture-development-method:b00042

<details><summary>展开本节完整英文来源</summary>

1.1. ADM Overview

The TOGAF ® ADM describes a method for developing and managing the lifecycle of an Enterprise Architecture, and forms the core of the TOGAF
Standard.

It integrates elements of the TOGAF Standard, as well as other available architectural assets, to meet the business needs of an organization.

</details>

<a id="tag_01_01_01"></a>
## 1.1.1. The ADM, Enterprise Continuum, and Architecture Repository

概念：企业连续体分类来源材料，架构库是通常的实践实现；两者身份不同。

适用条件：ADM各轮使用内部或外部参考架构、模型、模式与既往工作。

逻辑关系：治理决定哪些一般资源适配企业、哪些专用解法推广复用；各轮将决策快照与可复用块充实到组织架构景观。

决策方法：逐项判断复用相关性和入库标准；首轮资产少不能跳过外部资产调查。

制品及证据：架构库中的已接受资产、在制工作、组织特定架构和时点决策。

适用边界：资产数量增加不自动证明复用质量或集成一致。

来源块：C220-web-2025:02-architecture-development-method:b00043, C220-web-2025:02-architecture-development-method:b00044, C220-web-2025:02-architecture-development-method:b00045, C220-web-2025:02-architecture-development-method:b00046, C220-web-2025:02-architecture-development-method:b00047, C220-web-2025:02-architecture-development-method:b00048, C220-web-2025:02-architecture-development-method:b00049, C220-web-2025:02-architecture-development-method:b00050, C220-web-2025:02-architecture-development-method:b00051, C220-web-2025:02-architecture-development-method:b00052

<details><summary>展开本节完整英文来源</summary>

1.1.1. The ADM, Enterprise Continuum, and Architecture Repository

The Enterprise Continuum provides a framework and context to support the
leverage of relevant architecture assets in executing the ADM. These
assets may include Architecture Descriptions, models, and patterns taken
from a variety of sources, as explained in the TOGAF Standard — Architecture Content .

The Enterprise Continuum categorizes architectural source material —
both the contents of the organization’s own enterprise repositories and
the set of relevant, available reference models and standards in the
industry.

The practical implementation of the Enterprise Continuum will typically
take the form of an Architecture Repository (see the TOGAF Standard — Architecture Content ) that includes reference architectures, models, and patterns
that have been accepted for use within the enterprise, and actual
architectural work done previously within the enterprise. The architect
would seek to re-use as much as possible from the Architecture
Repository that was relevant to the project in hand. (In addition to the
collection of architecture source material, the repository would also
contain architecture development work-in-progress.)

At relevant places throughout the ADM there are reminders to consider
which, if any, architecture assets from the Architecture Repository the
architect should use. In some cases — for example, in the development of
a Technology Architecture — this may be the TOGAF Foundation
Architecture. In other cases — for example, in the development of a
Business Architecture — it may be a reference model for e-Commerce taken
from the industry at large.

The criteria for including source materials in an organization’s
Architecture Repository will typically form part of the Enterprise
Architecture Governance process. These governance processes should
consider available resources both within and outside the enterprise in
order to determine when general resources can be adapted for specific
enterprise needs and also to determine where specific solutions can be
generalized to support wider re-use.

While using the ADM, the architect is developing a snapshot of the
enterprise’s decisions and their implications at particular points in
time. Each iteration of the ADM will populate an organization-specific
landscape with all the architecture assets identified and leveraged
through the process, including the final organization-specific
architecture delivered.

Architecture development is a continuous, cyclical process, and in
executing the ADM repeatedly over time, the architect gradually adds
more and more content to the organization’s Architecture Repository.
Although the primary focus of the ADM is on the development of the
enterprise-specific architecture, in this wider context the ADM can also
be viewed as the process of populating the enterprise’s own Architecture
Repository with relevant re-usable building blocks taken from the
“left”, more generic side of the Enterprise Continuum.

In fact, the first execution of the ADM will often be the hardest, since
the architecture assets available for re-use will be relatively scarce.
Even at this stage of development, however, there will be architecture
assets available from external sources such as the TOGAF Standard, as
well as the IT industry at large, that could be leveraged in support of
the effort.

Subsequent executions will be easier as more and more architecture
assets become identified, are used to populate the organization’s
Architecture Repository, and are thus available for future re-use.

</details>

<a id="tag_01_01_02"></a>
## 1.1.2. The ADM and the Foundation Architecture

概念：ADM亦可填充企业基础架构，包括公共模型、政策治理定义和必要技术选择。

适用条件：需要建立整个企业通用基础或法律规定技术时。

逻辑关系：基础架构关切比特定企业问题更总体、不完整；来自不同来源的模型组合仍需集成。

决策方法：辨别通用要求与特定范围要求，并检查可集成性。

制品及证据：公共模型、政策、治理和基础技术选择。

适用边界：不能因模型都存在而认定形成连贯企业架构。

来源块：C220-web-2025:02-architecture-development-method:b00053, C220-web-2025:02-architecture-development-method:b00054, C220-web-2025:02-architecture-development-method:b00055

<details><summary>展开本节完整英文来源</summary>

1.1.2. The ADM and the Foundation Architecture

The ADM is also useful to populate the Foundation Architecture of an
enterprise. Business requirements of an enterprise may be used to
identify the necessary definitions and selections in the Foundation
Architecture. This could be a set of re-usable common models, policy and
governance definitions, or even as specific as overriding technology
selections (e.g., if mandated by law). Population of the Foundation
Architecture follows similar principles as for an Enterprise
Architecture, with the difference that requirements for a whole
enterprise are restricted to the overall concerns and thus less complete
than for a specific enterprise.

It is important to recognize that existing models from these various
sources, when integrated, may not necessarily result in a coherent
Enterprise Architecture. “Integratability” of Architecture Descriptions
is considered in Section 1.7, “Architecture Integration” .

</details>

<a id="tag_01_01_03"></a>
## 1.1.3. ADM and Supporting Guidelines and Techniques

概念：ADM主体与技术、指南、模板和检查表分开组织。

适用条件：在ADM相关工作点需要细节或特定情境裁剪时。

逻辑关系：ADM引用技术卷、系列指南以及TOGAF Library资料作为适用资源。

决策方法：按当前工作需要选择具体指南而非一次堆砌全部材料。

制品及证据：被选指南、模板、检查表的来源关系。

适用边界：辅助指南的存在不证明当前任务已经执行。

来源块：C220-web-2025:02-architecture-development-method:b00056, C220-web-2025:02-architecture-development-method:b00057, C220-web-2025:02-architecture-development-method:b00058, C220-web-2025:02-architecture-development-method:b00059

<details><summary>展开本节完整英文来源</summary>

1.1.3. ADM and Supporting Guidelines and Techniques

The application of the TOGAF ADM is supported by an extended set of
resources — guidelines, templates, checklists, and other detailed
materials. These are included in:

The TOGAF Standard — ADM Techniques TOGAF Series Guides — the Guidance part of the Standard (guidance
material on how to use and adapt the TOGAF Standard for specific needs) White Papers and Guides published by The Open Group, classified and
referenced in the TOGAF Library (see www.opengroup.org/togaf-library )

The individual guidelines and techniques are described separately so
that they can be referenced from the relevant points in the ADM as
necessary, rather than having the detailed text clutter the description
of the ADM itself.

</details>

<a id="tag_01_02"></a>
## 1.2. Architecture Development Cycle

概念：本标题为结构容器，无独立说明段落。

适用条件：阅读该主题时应继续读取下列子节。

逻辑关系：子节分工：tag_01_02_01: 1.2.1. Key Points；tag_01_02_02: 1.2.2. Basic Structure

决策方法：不从空容器推出附加规则或完成状态。

制品及证据：实际概念、决策和制品证据见上述子节。

适用边界：空容器覆盖仅证明目录和子节连接，不计额外深度结论。

来源块：C220-web-2025:02-architecture-development-method:b00060

<details><summary>展开本节完整英文来源</summary>

1.2. Architecture Development Cycle

</details>

<a id="tag_01_02_01"></a>
## 1.2.1. Key Points

概念：ADM在整轮、阶段间、阶段内三个层面迭代。

适用条件：每轮架构工作均须重新界定范围与资源。

逻辑关系：广度、细节、时间及复用资产选择应服从资源能力现实与可实现价值；通用方法可裁剪，也不一定必须裁剪。

决策方法：每轮新决策覆盖范围、深度、时间、资产和是否采用其他框架制品。

制品及证据：每轮范围与裁剪决定及资源/能力/价值依据。

适用边界：既往轮次选择不能替代本轮重新评估。

来源块：C220-web-2025:02-architecture-development-method:b00061, C220-web-2025:02-architecture-development-method:b00062, C220-web-2025:02-architecture-development-method:b00063, C220-web-2025:02-architecture-development-method:b00064

<details><summary>展开本节完整英文来源</summary>

1.2.1. Key Points

The following are the key points about the ADM:

The ADM is iterative, over the whole process, between phases, and
within phases (see the TOGAF Standard — ADM Techniques ) For each iteration of the ADM, a fresh decision must be taken as to: The breadth of coverage of the enterprise to be defined The level of detail to be defined The extent of the time period aimed at, including the number and
extent of any intermediate time periods The architectural assets to be leveraged, including: Assets created in previous iterations of the ADM cycle within the
enterprise Assets available elsewhere in the industry (other frameworks,
systems models, vertical industry models, etc.) These decisions should be based on a practical assessment of resource
and competence availability, and the value that can realistically be
expected to accrue to the enterprise from the chosen scope of the
architecture work As a generic method, the ADM is intended to be used by enterprises in
a wide variety of different geographies and applied in different
vertical sectors/industry types As such, it may be, but does not necessarily have to be, tailored to
specific needs. For example, it may be used in conjunction with the set
of deliverables of another framework, where these have been deemed to be
more appropriate for a specific organization. (For example, many US
Federal agencies have developed individual frameworks that define the
deliverables specific to their particular departmental needs.)

These issues are considered in detail in Section 1.3, “Adapting the ADM” .

</details>

<a id="tag_01_02_02"></a>
## 1.2.2. Basic Structure

概念：需求管理贯穿各阶段；draft与approved表达治理状态，approved不等于最终冻结。

适用条件：开发周期中持续验证整轮与本阶段原始期望，维护版本对象。

逻辑关系：早期输出可在后期修改；已批准文档必须通过变更控制和治理修改，需求变化须在其他阶段反映。

决策方法：设置组织适用版本政策和需求登记入口；按证据判断草稿或批准。

制品及证据：阶段输出版本、正式复核批准记录、单一需求库（组织可选）。

适用边界：图的推荐周期不能消除迭代；批准状态不能靠生成文档取得。

来源块：C220-web-2025:02-architecture-development-method:b00065, C220-web-2025:02-architecture-development-method:b00066, C220-web-2025:02-architecture-development-method:b00067, C220-web-2025:02-architecture-development-method:b00068, C220-web-2025:02-architecture-development-method:b00069, C220-web-2025:02-architecture-development-method:b00070, C220-web-2025:02-architecture-development-method:b00071, C220-web-2025:02-architecture-development-method:b00072, C220-web-2025:02-architecture-development-method:b00073, C220-web-2025:02-architecture-development-method:b00074

<details><summary>展开本节完整英文来源</summary>

1.2.2. Basic Structure

The basic structure of the ADM is shown in Figure 1-1, “Architecture Development Cycle” .

Throughout the ADM cycle, there needs to be frequent validation of
results against the original expectations, both those for the whole ADM
cycle, and those for the particular phase of the process.



Figure 1-1. Architecture Development Cycle

The phases of the ADM cycle are further divided into steps, which are
defined in the detailed description of each phase.

The Requirements Management phase is a continuous phase which ensures
that any changes to requirements are handled through appropriate
governance processes and reflected in all other phases. An enterprise
may choose to record all new requirements, including those which are in
scope of the current Statement of Architecture Work through a single
Requirements Repository.

The phases of the cycle are described in detail in the following
chapters.

Note that output is generated throughout the process, and that the
output from an early phase may be modified in a later phase. In the ADM,
the status of outputs at each stage is defined. The lifecycle of outputs
must be managed through a version numbering policy, adapted by the
architect to meet the requirements of the organization and to work with
the architecture tools and repositories employed by the organization.

In the ADM, documents which are under development and have not undergone
any formal review and approval process are designated “draft”. Documents
which have been reviewed and approved are designated “approved” in
accordance with the organization’s governance practices. Approved does
not necessarily mean finalized. Documents may evolve during subsequent
phases but may only be changed through an appropriate change control and
governance process. This is used in particular within the ADM to
illustrate the evolution of Baseline and Target Architecture
Definitions.

</details>

<a id="tag_01_03"></a>
## 1.3. Adapting the ADM

概念：ADM适配涉及顺序、组织治理、外包、规模、联邦、产品线以及内容框架。

适用条件：通用组件适用性不足、其他框架制品更合适、敏捷交付或企业规模要求不同。

逻辑关系：成熟度和业务原则可调整顺序：愿景/业务论证通常先行，但基线盘点或套装方案约束可使业务架构后置。

决策方法：先审适用性，再修改或扩展；大型组织在总体规划、参考架构实例化、复制验证等策略间选择。

制品及证据：企业专用ADM、内容框架和元模型、组织专用交付物/制品。

适用边界：裁剪不是无条件删除业务理解或治理；产品线例子不是所有用户企业必选方法。

来源块：C220-web-2025:02-architecture-development-method:b00075, C220-web-2025:02-architecture-development-method:b00076, C220-web-2025:02-architecture-development-method:b00077, C220-web-2025:02-architecture-development-method:b00078, C220-web-2025:02-architecture-development-method:b00079, C220-web-2025:02-architecture-development-method:b00080, C220-web-2025:02-architecture-development-method:b00081, C220-web-2025:02-architecture-development-method:b00082, C220-web-2025:02-architecture-development-method:b00083, C220-web-2025:02-architecture-development-method:b00084, C220-web-2025:02-architecture-development-method:b00085, C220-web-2025:02-architecture-development-method:b00086

<details><summary>展开本节完整英文来源</summary>

1.3. Adapting the ADM

The ADM is a generic method for architecture development, which is
designed to deal with most system and organizational requirements.
However, it will often be necessary to modify or extend the ADM to suit
specific needs. One of the tasks before applying the ADM is to review
its components for applicability, and then tailor them as appropriate to
the circumstances of the individual enterprise. This activity may well
produce an “enterprise-specific” ADM.

One reason for wanting to adapt the ADM, which it is important to
stress, is that the order of the phases in the ADM is to some extent
dependent on the maturity of the architecture discipline within the
enterprise. For example, if the business case for doing architecture at
all is not well recognized, then creating an Architecture Vision is
almost always essential; and a detailed Business Architecture often
needs to come next, in order to underpin the Architecture Vision, detail
the business case for remaining architecture work, and secure the active
participation of key stakeholders in that work. In other cases a
slightly different order may be preferred; for example, a detailed
inventory of the baseline environment may be done before undertaking the
Business Architecture.

The order of phases may also be defined by the Architecture Principles
and business principles of an enterprise. For example, the business
principles may dictate that the enterprise be prepared to adjust its
business processes to meet the needs of a packaged solution, so that it
can be implemented quickly to enable a fast response to market changes.
In such a case, the Business Architecture (or at least the completion of
it) may well follow completion of the Information Systems Architecture
or the Technology Architecture.

Another reason for wanting to adapt the ADM is if the TOGAF framework is
to be integrated with another enterprise framework (as explained in the TOGAF Standard — Introduction and Core Concepts ). For example, an enterprise may wish to use the TOGAF
framework and its generic ADM in conjunction with the Zachman ® Framework,

or another Enterprise Architecture framework that has a
defined set of deliverables specific to a particular vertical sector:
Government, Defense, e-Business, Telecommunications, etc. The ADM has
been specifically designed with this potential integration in mind.

Other possible reasons for wanting to adapt the ADM include:

The ADM is one of the many corporate processes that make up the
corporate governance model It is complementary to, and supportive of, other standard program
management processes, such as those for authorization, risk management,
business planning and budgeting, development planning, systems
development, and procurement. The ADM is being mandated for use by a prime or lead contractor in an
outsourcing situation, and needs to be tailored to achieve a suitable
compromise between the contractor’s existing practices and the
contracting enterprise’s requirements The enterprise is a small-to-medium enterprise, and wishes to use a
“cut-down” method more attuned to the reduced level of resources and
system complexity typical of such an environment The enterprise is very large and complex, comprising many separate but
interlinked “enterprises” within an overall collaborative business
framework, and the architecture method needs to be adapted to recognize
this Different approaches to planning and integration may be used in such
cases, including the following (possibly in combination): Top-down planning and development — designing the whole
interconnected meta-enterprise as a single entity (an exercise that
typically stretches the limits of practicality) Development of a “generic” or “reference” architecture, typical of
the enterprises within the organization, but not representing any
specific enterprise, which individual enterprises are then expected to
adapt in order to produce an architecture “instance” suited to the
particular enterprise concerned Replication — developing a specific architecture for one enterprise,
implementing it as a proof-of-concept, and then taking that as a
“reference architecture” to be cloned in other enterprises In a vendor or production environment, a generic architecture for a
family of related products is often referred to as a “Product Line
Architecture”, and the analogous process to that outlined above is
termed “(Architecture-based) Product Line Engineering”. The ADM is
targeted primarily at architects in IT user enterprises, but a vendor
organization whose products are IT-based might well wish to adapt it as
a generic method for a Product Line Architecture development.

The descriptions of the phases of the ADM contain lists of deliverables
and artifacts that could be applicable to any enterprise. It is
important to adapt deliverables and artifacts to reflect the specific
needs of the enterprise for the required architecture.

Adapting the Content Framework and Enterprise Metamodel, which defines
the organization-specific deliverables and artifacts, together with
detailed descriptions of the specific deliverables and artifacts
referenced in the ADM phase descriptions may be found in the TOGAF Standard — Architecture Content .

The ADM can also be adapted to support an Agile Enterprise Architecture
delivery style as well as to enable enterprise agility. Detailed
guidance on how to adapt the ADM may be found in the following
documents:

TOGAF ® Series Guide: Enabling Enterprise Agility TOGAF ® Series Guide: Applying the TOGAF ® ADM using Agile Sprints

Additional guidance on adapting the ADM process may be found in the TOGAF Standard — Applying the ADM ,
and also in the TOGAF ® Series Guide: A Practitioners’ Approach to Developing Enterprise Architecture Following the TOGAF ® ADM .

</details>

<a id="tag_01_04"></a>
## 1.4. Architecture Governance

概念：ADM本身是受治理和版本控制的架构资产。

适用条件：采用原方法或组织裁剪方法的所有阶段。

逻辑关系：架构委员会核对方法正确应用与必需交付物；受控库分参考资料、流程状态、完成后的审计信息。

决策方法：保留待处理符合性/豁免请求及已完成决策责任人。

制品及证据：版本对象、过程控制、状态、治理程序与决策审计。

适用边界：治理库记录不自动赋予个人决策权限。

来源块：C220-web-2025:02-architecture-development-method:b00087, C220-web-2025:02-architecture-development-method:b00088, C220-web-2025:02-architecture-development-method:b00089, C220-web-2025:02-architecture-development-method:b00090, C220-web-2025:02-architecture-development-method:b00091, C220-web-2025:02-architecture-development-method:b00092, C220-web-2025:02-architecture-development-method:b00093

<details><summary>展开本节完整英文来源</summary>

1.4. Architecture Governance

The ADM, whether adapted by the organization or used as documented here,
is a key process to be managed in the same manner as other architecture
artifacts classified through the Enterprise Continuum and held in the
Architecture Repository. The Architecture Board should be satisfied that
the method is being applied correctly across all phases of an
architecture development iteration. Compliance with the ADM is
fundamental to the governance of the architecture, to ensure that all
considerations are made and all required deliverables are produced.

The management of all architectural artifacts, governance, and related
processes should be supported by a controlled environment. Typically,
this would be based on one or more repositories supporting versioned
objects, process control, and status.

The major information areas managed by a governance repository should
contain the following types of information:

Reference Data (collateral from the organization’s own
repositories/Enterprise Continuum, including external data; e.g.,
COBIT ® , the IT4IT Reference Architecture): used for guidance and
instruction during project implementation This includes the details of information outlined above. The reference
data includes a description of the governance procedures themselves. Process Status : all information regarding the state of any
governance processes will be managed Examples of this include outstanding compliance requests, dispensation
requests, and compliance assessments investigations. Audit Information : this will record all completed governance process
actions and will be used to support: Key decisions and responsible personnel for any architecture project
that has been sanctioned by the governance process A reference for future architectural and supporting process
developments, guidance, and precedence

The governance artifacts and process are themselves part of the contents
of the Architecture Repository.

Architecture Governance is addressed in detail in the TOGAF Standard — EA Capability and Governance .

</details>

<a id="tag_01_05"></a>
## 1.5. Scoping the Architecture

概念：范围受团队权力、目标关切、人员资金资源约束；四维为广度、深度、时间、域。

适用条件：定义单个或联邦架构工作时。

逻辑关系：先理解广度/深度/时间再选择适合问题的域；分区需对齐复用和符合性，局部可能需要让步以优化企业整体。

决策方法：决定四维与跨分区关系，防止重复和冲突。

制品及证据：范围说明、架构分区、复用/符合性关联。

适用边界：完整企业架构与有意限定域的工作需明确区分。

来源块：C220-web-2025:02-architecture-development-method:b00094, C220-web-2025:02-architecture-development-method:b00095, C220-web-2025:02-architecture-development-method:b00096, C220-web-2025:02-architecture-development-method:b00097, C220-web-2025:02-architecture-development-method:b00098, C220-web-2025:02-architecture-development-method:b00099, C220-web-2025:02-architecture-development-method:b00100, C220-web-2025:02-architecture-development-method:b00101, C220-web-2025:02-architecture-development-method:b00102

<details><summary>展开本节完整英文来源</summary>

1.5. Scoping the Architecture

There are many reasons to constrain (or restrict) the scope of the
architectural activity to be undertaken, most of which relate to limits
in:

The organizational authority of the team producing the architecture The objectives and stakeholder concerns to be addressed within the
architecture The availability of people, finance, and other resources

The scope chosen for the architecture activity should ideally allow the
work of all architects within the enterprise to be effectively governed
and integrated. This requires a set of aligned “architecture partitions”
that ensure architects are not working on duplicate or conflicting
activities. It also requires the definition of re-use and compliance
relationships between architecture partitions.

The division of the enterprise and its architecture-related activity is
discussed in more detail in the TOGAF Standard — Applying the ADM .

Four dimensions are typically used in order to define and limit the
scope of an architecture:

Breadth : what is the full extent of the enterprise, and what part of
that extent will this architecting effort deal with? Many enterprises are very large, effectively comprising a federation
of organizational units that could validly be considered enterprises in
their own right The modern enterprise increasingly extends beyond its traditional
boundaries, to embrace a fuzzy combination of traditional business
enterprise combined with suppliers, customers, and partners Depth : to what level of detail should the architecting effort go? How much architecture is “enough”? What is the appropriate demarcation
between the architecture effort and other, related activities (system
design, system engineering, system development)? Time Period : what is the time period that needs to be articulated
for the Architecture Vision, and does it make sense (in terms of
practicality and resources) for the same period to be covered in the
detailed Architecture Description? If not, how many Transition Architectures are to be defined, and what
are their time periods? Architecture Domains :  a complete Enterprise Architecture Description
should contain all four architecture domains (Business, Data,
Application, Technology), but the realities of resource and time
constraints often mean there is not enough time, funding, or resources
to build a top-down, all-inclusive Architecture Description encompassing
all four architecture domains, even if the enterprise scope is chosen to
be less than the full extent of the overall enterprise

Typically, the scope of an architecture is first expressed in terms of
breadth, depth, and time. Once these dimensions are understood, a
suitable combination of architecture domains can be selected that are
appropriate to the problem being addressed. Techniques for using the ADM
to develop a number of related architectures are discussed in the TOGAF Standard — Applying the ADM .

The four dimensions of architecture scope are explored in detail below.
In each case, particularly in large-scale environments where
architectures are necessarily developed in a federated manner, there is
a danger of architects optimizing within their own scope of activity,
instead of at the level of the overall enterprise. It is often necessary
to sub-optimize in a particular area, in order to optimize at the
enterprise level. The aim should always be to seek the highest level of
commonality and focus on scalable and re-usable modules in order to
maximize re-use at the enterprise level.

</details>

<a id="tag_01_05_01"></a>
## 1.5.1. Breadth

概念：广度定义业务部门、功能、组织与地域覆盖；联邦架构需要集成与治理框架。

适用条件：单一企业范围过于复杂或不同业务单位独立开展工作。

逻辑关系：发布订阅使供需方共享质量、时效、用途、已审同意发布状态；使用方接受符合性评估与有业务理由的豁免流程。

决策方法：判断单一总体架构可行性，选择联邦边界、互操作迁移符合性原则及订阅承诺。

制品及证据：已发布架构材料、符合性评估、受治理豁免。

适用边界：业务迫切性支持请求但不自动批准豁免。

来源块：C220-web-2025:02-architecture-development-method:b00103, C220-web-2025:02-architecture-development-method:b00104, C220-web-2025:02-architecture-development-method:b00105, C220-web-2025:02-architecture-development-method:b00106, C220-web-2025:02-architecture-development-method:b00107, C220-web-2025:02-architecture-development-method:b00108, C220-web-2025:02-architecture-development-method:b00109

<details><summary>展开本节完整英文来源</summary>

1.5.1. Breadth

One of the key decisions is the focus of the architecture effort, in
terms of the breadth of overall enterprise activity to be covered (which
specific business sectors, functions, organizations, geographical areas,
etc.).

It is often necessary to have a number of different architectures
existing across an enterprise, focused on particular timeframes,
business functions, or business requirements.

For large complex enterprises, federated architectures — independently
developed, maintained, and managed architectures that are subsequently
integrated within an integration framework — are typical. Such a
framework specifies the principles for interoperability, migration, and
conformance. This allows specific business units to have architectures
developed and governed as stand-alone architecture projects. More
details and guidance on specifying the interoperability requirements for
different solutions can be found in the TOGAF Standard — ADM Techniques .

The feasibility of a single enterprise-wide architecture for every
business function or purpose may be rejected as too complex and
unwieldy. In these circumstances it is suggested that a number of
different Enterprise Architectures exist across an enterprise. These
Enterprise Architectures focus on particular timeframes, business
segments or functions, and specific organizational requirements. In such
a case we need to create the overarching Enterprise Architecture as a
“federation” of these Enterprise Architectures. An effective way of
managing and exploiting these Enterprise Architectures is to adopt a
publish-and-subscribe model that allows architecture to be brought under
a governance framework. In such a model, architecture developers and
architecture consumers in projects (the supply and demand sides of
architecture work) sign up to a mutually beneficial framework of
governance that ensures that:

Architectural material is of good quality, up-to-date,
fit-for-purpose, and published (reviewed and agreed to be made public) Usage of architecture material can be monitored, and compliance with
standards, models, and principles can be exhibited, via: A Compliance Assessment process that describes what the user is
subscribing to, and assesses their level of compliance A dispensation process that may grant dispensations from adherence to
architecture standards and guidelines in specific cases (usually with a
strong business imperative)

Publish and subscribe techniques are being developed as part of general
IT governance and specifically for the Defense sphere.

</details>

<a id="tag_01_05_02"></a>
## 1.5.2. Depth

概念：深度以用途和决策所需信息为准，所选域应完成一致、相当的细节。

适用条件：时间资源有限且需要未来复用扩展时。

逻辑关系：漏掉相关细节损害用途，加入无关细节耗费资源；各轮在既往资产与能力上积累。

决策方法：根据当前能力和可交付利益判断足够细节，预留合理扩展结构。

制品及证据：各域模型及粒度、用途、资源可行性说明。

适用边界：不是细节越多越好，也不能用领域间不一致掩盖遗漏。

来源块：C220-web-2025:02-architecture-development-method:b00110, C220-web-2025:02-architecture-development-method:b00111, C220-web-2025:02-architecture-development-method:b00112, C220-web-2025:02-architecture-development-method:b00113, C220-web-2025:02-architecture-development-method:b00114

<details><summary>展开本节完整英文来源</summary>

1.5.2. Depth

Care should be taken to judge the appropriate level of detail to be
captured, based on the intended use of the Enterprise Architecture and
the decisions to be made based on it. It is important that a consistent
and equal level of depth be completed in each architecture domain
(Business, Data, Application, Technology) included in the architecture
effort. If pertinent detail is omitted, the architecture may not be
useful. If unnecessary detail is included, the architecture effort may
exceed the time and resources available, and/or the resultant
architecture may be confusing or cluttered. Developing architectures at
different levels of detail within an enterprise is discussed in more
detail in the TOGAF Standard — Applying the ADM .

It is also important to predict the future uses of the architecture so
that, within resource limitations, the architecture can be structured to
accommodate future tailoring, extension, or re-use. The depth and detail
of the Enterprise Architecture needs to be sufficient for its purpose,
and no more.

Iterations of the ADM will build on the artifacts and the capabilities
created during previous iterations.

There is a need to document all the models in an enterprise, to the
level of detail appropriate to the need of the current ADM cycle. The
key is to understand the status of the enterprise’s architecture work,
and what can realistically be achieved with the resources and
competencies available, and then focus on identifying and delivering the
value that is achievable. Stakeholder value is a key focus: too broad a
scope may deter some stakeholders (no return on investment).

</details>

<a id="tag_01_05_03"></a>
## 1.5.3. Time Period

概念：基线、远期目标与中间过渡是不同时间实例；过渡应成为一致可运营平台。

适用条件：长期愿景不能在单一阶段实现时。

逻辑关系：先形成长期目标再形成收敛的增量过渡；目标可周期演进，过渡原则上在实施增量内保持稳定以免移动靶。

决策方法：选择时间范围、平台和更新节奏；详细技术选择尽量接近实施时点。

制品及证据：各过渡完整的目标描述、关系与迁移顺序。

适用边界：源文六年和通常少于两年是说明性例子/经验，不是强制企业期限；愿景可能随环境更新。

来源块：C220-web-2025:02-architecture-development-method:b00115, C220-web-2025:02-architecture-development-method:b00116, C220-web-2025:02-architecture-development-method:b00117, C220-web-2025:02-architecture-development-method:b00118, C220-web-2025:02-architecture-development-method:b00119, C220-web-2025:02-architecture-development-method:b00120, C220-web-2025:02-architecture-development-method:b00121, C220-web-2025:02-architecture-development-method:b00122, C220-web-2025:02-architecture-development-method:b00123

<details><summary>展开本节完整英文来源</summary>

1.5.3. Time Period

The ADM is described in terms of a single cycle of Architecture Vision,
and a set of Target Architectures (Business, Data, Application,
Technology) that enable the implementation of the vision.

In such cases, a wider view may be taken, whereby an enterprise is
represented by several different architecture instances (for example,
strategic, segment, capability), each representing the enterprise at a
particular point in time. One architecture instance will represent the
current enterprise state (the “as-is”, or baseline). Another
architecture instance, perhaps defined only partially, will represent
the ultimate target end-state (the “vision”). In-between, intermediate
or “Transition Architecture” instances may be defined, each comprising
its own set of Target Architecture Descriptions. An example of how this
might be achieved is given in the TOGAF Standard — ADM Techniques .

By this approach, the Target Architecture work is split into two or more
discrete stages:

First, develop Target Architecture Descriptions for the overall
(large-scale) system, demonstrating a response to stakeholder objectives
and concerns for a relatively distant timeframe (for example, a six-year
period) Then develop one or more “Transition Architecture” descriptions, as
increments or plateaus, each in line with and converging on the Target
Architecture Descriptions, and describing the specifics of the increment
concerned

In such an approach, the Target Architectures are evolutionary in
nature, and require periodic review and update according to evolving
business requirements and developments in technology, whereas the
Transition Architectures are (by design) incremental in nature, and in
principle should not evolve during the implementation phase of the
increment, in order to avoid the “moving target” syndrome. This, of
course, is only possible if the implementation schedule is under tight
control and relatively short (typically less than two years).

The Target Architectures remain relatively generic, and are therefore
less vulnerable to obsolescence than the Transition Architectures. They
embody only the key strategic architectural decisions, which should be
blessed by the stakeholders from the outset, whereas the detailed
architectural decisions in the Transition Architectures are deliberately
postponed as far as possible (i.e., just before implementation) in order
to improve responsiveness vis a vis new technologies and products.

The enterprise evolves by migrating to each of these Transition
Architectures in turn. As each Transition Architecture is implemented,
the enterprise achieves a consistent, operational state on the way to
the ultimate vision. However, this vision itself is periodically updated
to reflect changes in the business and technology environment, and in
effect may never actually be achieved, as originally described. The
whole process continues for as long as the enterprise exists and
continues to change.

Such a breakdown of the Architecture Description into a family of
related architecture products of course requires effective management of
the set and their relationships.

</details>

<a id="tag_01_05_04"></a>
## 1.5.4. Architecture Domains

概念：完整企业架构覆盖业务、数据、应用、技术四域；特定问题可合理缩小实际开发范围。

适用条件：业务流程不允许更改且工作只探索某能力的技术选项等情境。

逻辑关系：数据/应用/技术仍以业务理解为基础；未开发所有域须说明集成一致性成本风险。

决策方法：明确需要回答的问题、选择域并让管理层理解遗漏域的取舍。

制品及证据：业务关切、域选择及风险/取舍说明。

适用边界：缺域的描述按定义不能称完整企业架构；不做完整业务模型不等于不理解业务。

来源块：C220-web-2025:02-architecture-development-method:b00124, C220-web-2025:02-architecture-development-method:b00125, C220-web-2025:02-architecture-development-method:b00126, C220-web-2025:02-architecture-development-method:b00127, C220-web-2025:02-architecture-development-method:b00128

<details><summary>展开本节完整英文来源</summary>

1.5.4. Architecture Domains

A complete Enterprise Architecture should address all four architecture
domains (Business, Data, Application, Technology), but the realities of
resource and time constraints often mean there is not enough time,
funding, or resources to build a top-down, all-inclusive Architecture
Description encompassing all four architecture domains.

Architecture Descriptions will normally be built with a specific purpose
in mind — a specific set of business drivers that drive the architecture
development — and clarifying the specific issue(s) that the Architecture
Description is intended to help explore, and the questions it is
expected to help answer, is an important part of the initial phase of
the ADM.

For example, if the purpose of a particular architecture effort is to
define and examine technology options for achieving a particular
capability, and the fundamental business processes are not open to
modification, then a full Business Architecture may well not be
warranted. However, because the Data, Application, and Technology
Architectures build on the Business Architecture, the Business
Architecture still needs to be thought through and understood.

While circumstances may sometimes dictate building an Architecture
Description not containing all four architecture domains, it should be
understood that such an architecture cannot, by definition, be a
complete Enterprise Architecture. One of the risks is a lack of
consistency and therefore an ability to integrate. Integration either
needs to come later — with its own costs and risks — or the risks and
trade-offs involved in not developing a complete and integrated
architecture need to be articulated by the architect, and communicated
to and understood by the enterprise management.

</details>

<a id="tag_01_06"></a>
## 1.6. Architecture Alternatives

概念：多个目标方案可同样满足愿景原则需求；比较揭露隐藏关切和要求。

适用条件：存在竞争性力量、利益相关者偏好或替代技术路径时。

逻辑关系：方案与取舍展示促进需求澄清，支持最终目标选择。

决策方法：识别多个候选并明确取舍。

制品及证据：候选目标架构及关切/原则/要求映射。

适用边界：不存在一案自然满足全部利益相关者的保证。

来源块：C220-web-2025:02-architecture-development-method:b00129, C220-web-2025:02-architecture-development-method:b00130

<details><summary>展开本节完整英文来源</summary>

1.6. Architecture Alternatives

There is often more than one possible Target Architecture that would
conform to the Architecture Vision, Architecture Principles, and
Requirements. It is important to identify alternative Target
Architectures and build understanding of different possibilities and
identify trade-offs between the alternatives. Creating an architecture
normally requires trade-offs among competing forces. Presenting
different alternatives and trade-offs to stakeholders helps architects
to extract hidden agendas, principles, and requirements that could
impact the final Target Architecture.

</details>

<a id="tag_01_06_01"></a>
## 1.6.1. Method

概念：备选方法分为选择评价准则、定义理解备选、选择或组合特征。

适用条件：任何阶段、任何架构层级需要比较决策时。

逻辑关系：可先按域简化比较再合并整体分析；分析深度以支持决定为限。

决策方法：采用一案或综合多个方案特征，并验证综合后的整体关系。

制品及证据：准则集、备选理解、拟议方案和决定依据。

适用边界：拼合各域最佳特征不自动形成整体最优或一致方案。

来源块：C220-web-2025:02-architecture-development-method:b00131, C220-web-2025:02-architecture-development-method:b00132, C220-web-2025:02-architecture-development-method:b00133, C220-web-2025:02-architecture-development-method:b00134, C220-web-2025:02-architecture-development-method:b00135, C220-web-2025:02-architecture-development-method:b00136, C220-web-2025:02-architecture-development-method:b00137, C220-web-2025:02-architecture-development-method:b00138

<details><summary>展开本节完整英文来源</summary>

1.6.1. Method

It is most common that a single alternative does not exist that will
meet all stakeholders’ concerns. The TOGAF Standard (see the TOGAF Standard — ADM Techniques :
Architecture Alternatives and Trade-offs) provides a technique to
investigate different alternatives and to discuss these with the
stakeholders.

Commonly, alternatives are defined per domain. This is done to simplify
the analysis of the different alternatives. Of course, the alternatives
per domain can be merged into on overall analysis of the alternatives
for the whole architecture. This approach is illustrated in Figure 1-2, “Architecture Alternatives Method” .

The first part of the method uses the vision, principles, requirements,
and other information to select sets of criteria fitting for different
alternatives.

The second part of the method defines alternatives based on the criteria
and builds an understanding of each.

The third part of the method will either select one of the alternatives,
or else combine features from more than one, to create the proposed
alternative. Perform the following activities in just enough detail to
support that decision. The method can be used for any phase at any level
of an architecture.



Figure 1-2. Architecture Alternatives Method

</details>

<a id="tag_01_07"></a>
## 1.7. Architecture Integration

概念：多个子架构需要一致参照系，范围维度亦是集成维度。

适用条件：将不同粒度、域、时间或问题的架构一起使用。

逻辑关系：制品粒度和描述交换标准成熟度限制可集成性；标准治理仍需支持手工协调与冲突解决。

决策方法：对齐粒度、细节和标准，评估当前可实现集成程度。

制品及证据：各架构参照维度、交换标准、冲突处理。

适用边界：源文对技术现状的断言属于源版本陈述，不据此断言当前所有工具能力；标准化不消除协调需求。

来源块：C220-web-2025:02-architecture-development-method:b00139, C220-web-2025:02-architecture-development-method:b00140, C220-web-2025:02-architecture-development-method:b00141, C220-web-2025:02-architecture-development-method:b00142, C220-web-2025:02-architecture-development-method:b00143, C220-web-2025:02-architecture-development-method:b00144

<details><summary>展开本节完整英文来源</summary>

1.7. Architecture Integration

Architectures that are created to address a subset of issues within an
enterprise require a consistent frame of reference so that they can be
considered as a group as well as point deliverables. The dimensions that
are used to define the scope boundary of a single architecture (e.g.,
level of detail, architecture domain, etc.) are typically the same
dimensions that must be addressed when considering the integration of
many architectures. Figure 1-3, “Integration of Architecture Artifacts” illustrates how
different types of architecture need to co-exist.

At the present time, the state of the art is such that architecture
integration can be accomplished only at the lower end of the
integratability spectrum. Key factors to consider are the granularity
and level of detail in each artifact, and the maturity of standards for
the interchange of architectural descriptions.



Figure 1-3. Integration of Architecture Artifacts

As organizations address common themes (such as Service-Oriented
Architecture (SOA), and integrated information infrastructure) and
universal data models and standard data structures emerge, integration
toward the high end of the spectrum will be facilitated. However, there
will always be the need for effective standards governance to reduce the
need for manual co-ordination and conflict resolution.

</details>

<a id="tag_01_08"></a>
## 1.8. Summary

概念：ADM推荐阶段步骤的迭代顺序，组织自行决定具体范围。

适用条件：首轮与后续轮均需建立清楚期望。

逻辑关系：本轮可创造价值决定横向纵向范围与时间，后轮在当前资产上扩展。

决策方法：将可交付价值与目标边界一致并明确范围依据。

制品及证据：范围依据、工作目标、可复用库增量。

适用边界：完整框架作为长期目标不能推导本轮必须全部开发。

来源块：C220-web-2025:02-architecture-development-method:b00145, C220-web-2025:02-architecture-development-method:b00146, C220-web-2025:02-architecture-development-method:b00147, C220-web-2025:02-architecture-development-method:b00148

<details><summary>展开本节完整英文来源</summary>

1.8. Summary

The TOGAF ADM defines a recommended sequence for the various phases and
steps involved in developing an architecture, but it cannot recommend a
scope — this has to be determined by the organization itself, bearing in
mind that the recommended sequence of development in the ADM process is
an iterative one, with the depth and breadth of scope and deliverables
increasing with each iteration. Each iteration will add resources to the
organization’s Architecture Repository.

While a complete framework is useful (indeed, essential) to have in mind
as the ultimate long-term goal, in practice there is a key decision to
be made as to the scope of a specific Enterprise Architecture effort.
This being the case, it is vital to understand the basis on which
scoping decisions are being made, and to set clear expectations for the
goal of the effort.

The main guideline is to focus on what creates value to the enterprise,
and to select horizontal and vertical scope, and time periods,
accordingly. Whether or not this is the first time around, understand
that this exercise will be repeated, and that future iterations will
build on what is being created in the current effort, adding greater
width and depth.

</details>

<a id="chap02"></a>
## 2. Preliminary Phase

概念：预备阶段准备企业专用架构框架、原则及EA能力。

适用条件：业务指令要求建立新的企业架构或调整能力时。

逻辑关系：建立开展架构的组织与方法条件，区别于阶段A的特定架构任务。

决策方法：明确新能力需要覆盖哪些组织与原则。

制品及证据：组织专用框架及原则，相关阶段图。

适用边界：已有能力可复用，不意味着每轮从零建团队。

来源块：C220-web-2025:02-architecture-development-method:b00149, C220-web-2025:02-architecture-development-method:b00150, C220-web-2025:02-architecture-development-method:b00151, C220-web-2025:02-architecture-development-method:b00152

<details><summary>展开本节完整英文来源</summary>

2. Preliminary Phase

This chapter describes the preparation and initiation activities
required to meet the business directive for a new Enterprise
Architecture, including the definition of an Organization-Specific
Architecture framework and the definition of principles.



Figure 2-1: Preliminary Phase

</details>

<a id="tag_02_01"></a>
## 2.1. Objectives

概念：目标分为确定期望能力和建立该能力。

适用条件：组织需要确定架构开展条件及成熟度目标。

逻辑关系：先审组织与交叉框架、范围及成熟度，再建组织模型、治理过程资源、工具和原则。

决策方法：确定能力成熟度目标并选择组织/治理/工具。

制品及证据：EA组织模型、治理资源、能力目标及原则。

适用边界：目标成熟度不能取代现状能力证据。

来源块：C220-web-2025:02-architecture-development-method:b00153, C220-web-2025:02-architecture-development-method:b00154, C220-web-2025:02-architecture-development-method:b00155

<details><summary>展开本节完整英文来源</summary>

2.1. Objectives

The objectives of the Preliminary Phase are to:

Determine the Architecture Capability desired by the organization: Review the organizational context for conducting Enterprise
Architecture Identify and scope the elements of the enterprise organizations
affected by the Architecture Capability Identify the established frameworks, methods, and processes that
intersect with the Architecture Capability Establish Capability Maturity target Establish the Architecture Capability: Define and establish the Organizational Model for Enterprise
Architecture Define and establish the detailed process and resources for
Architecture Governance Select and implement tools that support the Architecture Capability Define the Architecture Principles

</details>

<a id="tag_02_02"></a>
## 2.2. Inputs

概念：预备输入区分企业外参考、非架构和既有架构资料。

适用条件：启动预备阶段盘点可用信息时。

逻辑关系：2.2.1—2.2.3分别处理参考、业务治理情境和已有能力基线。

决策方法：逐类确认存在与适用性。

制品及证据：三类输入清单及出处。

适用边界：输入导航不是材料已经齐备的结论。

来源块：C220-web-2025:02-architecture-development-method:b00156, C220-web-2025:02-architecture-development-method:b00157

<details><summary>展开本节完整英文来源</summary>

2.2. Inputs

This section defines the inputs to the Preliminary Phase.

</details>

<a id="tag_02_02_01"></a>
## 2.2.1. Reference Materials External to the Enterprise

概念：外部输入为TOGAF Library及按需要采用的其他框架。

适用条件：需要参考外部方法内容时。

逻辑关系：其他框架是条件性输入，不强制并用。

决策方法：判断是否需要另一架构框架。

制品及证据：外部参考及适用性记录。

适用边界：引用资源不代表已授权使用或已验证具体项目适配。

来源块：C220-web-2025:02-architecture-development-method:b00158, C220-web-2025:02-architecture-development-method:b00159

<details><summary>展开本节完整英文来源</summary>

2.2.1. Reference Materials External to the Enterprise

The TOGAF Library Other architecture framework(s), if required

</details>

<a id="tag_02_02_02"></a>
## 2.2.2. Non-Architectural Inputs

概念：业务策略目标原则、既有治理法律、能力和合作合同构成非架构情境。

适用条件：评估组织能力建立条件时。

逻辑关系：材料有些仅在预先存在时输入；项目/组合等运行框架给出接点约束。

决策方法：确认既有策略治理与合同边界。

制品及证据：业务计划、法律治理、合作合同和能力材料。

适用边界：不存在的策略不得自动补写成组织事实。

来源块：C220-web-2025:02-architecture-development-method:b00160, C220-web-2025:02-architecture-development-method:b00161

<details><summary>展开本节完整英文来源</summary>

2.2.2. Non-Architectural Inputs

Board strategies and board business plans, business strategy, IT
strategy, business principles, business goals, and business drivers,
when pre-existing Major frameworks operating in the business; e.g., project/portfolio
management Governance and legal frameworks, including Architecture Governance
strategy, when pre-existing Architecture capability Partnership and contract agreements

</details>

<a id="tag_02_02_03"></a>
## 2.2.3. Architectural Inputs

概念：已有EA运作模型可作预备基线。

适用条件：企业已有EA组织框架和架构库时。

逻辑关系：组织模型含范围成熟度差距角色预算治理；已有框架含方法内容工具与原则。

决策方法：检查哪些已有能力适用，哪些需调整。

制品及证据：组织模型、框架配置、原则和架构库。

适用边界：已有模型与真实运作有效性不同，仍需评估。

来源块：C220-web-2025:02-architecture-development-method:b00162, C220-web-2025:02-architecture-development-method:b00163, C220-web-2025:02-architecture-development-method:b00164

<details><summary>展开本节完整英文来源</summary>

2.2.3. Architectural Inputs

Pre-existing models for operating an Enterprise Architecture Capability
can be used as a baseline for the Preliminary Phase. Inputs would
include:

Organizational Model for Enterprise Architecture (see the TOGAF Standard — Architecture Content ), including: Scope of organizations impacted Maturity assessment, gaps, and resolution approach Roles and responsibilities for architecture team(s) Budget requirements Governance and support strategy Existing Architecture Framework, if any, including: Architecture method Architecture content Configured and deployed tools Architecture Principles Architecture Repository

</details>

<a id="tag_02_03"></a>
## 2.3. Steps

概念：预备步骤实施组织适配，详细度取决于整体范围与目标。

适用条件：启动或调整企业专用框架时。

逻辑关系：组织治理允许根据情况调整各步骤顺序与正式起止。

决策方法：在六步中确定实际顺序、细节与时机。

制品及证据：受治理的预备工作安排，2.3.1—2.3.6结果。

适用边界：步骤列表不是固定瀑布时间线。

来源块：C220-web-2025:02-architecture-development-method:b00165, C220-web-2025:02-architecture-development-method:b00166, C220-web-2025:02-architecture-development-method:b00167, C220-web-2025:02-architecture-development-method:b00168, C220-web-2025:02-architecture-development-method:b00169, C220-web-2025:02-architecture-development-method:b00170

<details><summary>展开本节完整英文来源</summary>

2.3. Steps

The TOGAF ADM is a generic method, intended to be used by a wide variety
of different enterprises, and in conjunction with a wide variety of
other architecture frameworks, if required. The Preliminary Phase
therefore involves doing any necessary work to initiate and adapt the
ADM to define an organization-specific framework. The issues involved
with adapting the ADM to a specific organizational context are discussed
in detail in Section 1.3, “Adapting the ADM” .

The level of detail addressed in the Preliminary Phase will depend on the scope and goals of the overall architecture effort.

The order of the steps in the Preliminary Phase as well as the time at which they are formally started and completed should be adapted to the situation at hand in accordance with the established Architecture Governance.

The steps within the Preliminary Phase are as follows:

Scope the enterprise organizations impacted; see Section 2.3.1, “Scope the Enterprise Organizations Impacted” Confirm governance and support frameworks; see Section 2.3.2, “Confirm Governance and Support Frameworks” Define and establish Enterprise Architecture team and organization; see Section 2.3.3, “Define and Establish Enterprise Architecture Team and Organization” Identify and establish Architecture Principles; see Section 2.3.4, “Identify and Establish Architecture Principles” Tailor the TOGAF framework and, if any, other selected architecture frameworks; see Section 2.3.5, “Tailor the TOGAF Framework and, if any, Other Selected Architecture Framework(s)” Develop a strategy and implementation plan for tools and techniques; see Section 2.3.6, “Develop a Strategy and Implementation Plan for Tools and Techniques”

</details>

<a id="tag_02_03_01"></a>
## 2.3.1. Scope the Enterprise Organizations Impacted

概念：受影响组织分核心、软、扩展企业、社区与相关治理范围。

适用条件：确定EA能力影响广度。

逻辑关系：按影响和价值区分核心；软单位能力会变、扩展单位在范围外但自身架构受影响。

决策方法：识别各组、法律框架和地域。

制品及证据：组织范围和受影响利益相关者清单。

适用边界：这些是影响类别，不是自动授予的组织汇报层级。

来源块：C220-web-2025:02-architecture-development-method:b00171, C220-web-2025:02-architecture-development-method:b00172

<details><summary>展开本节完整英文来源</summary>

2.3.1. Scope the Enterprise Organizations Impacted

Identify core enterprise (units) — those who are most affected and
achieve most value from the work Identify soft enterprise (units) — those who will see change to their
capability and work with core units but are otherwise not directly
affected Identify extended enterprise (units) — those units outside the scoped
enterprise who will be affected in their own Enterprise Architecture Identify communities involved (enterprises) — those stakeholders who
will be affected and who are in groups of communities Identify governance involved, including legal frameworks and
geographies (enterprises)

</details>

<a id="tag_02_03_02"></a>
## 2.3.2. Confirm Governance and Support Frameworks

概念：架构框架决定集中/联邦、轻/重等治理形式及库要求。

适用条件：新框架可能改变已有治理支持时。

逻辑关系：评估现有模型并咨询发起人与相关方，确认制品由豁免、符合性、纳入、退役等哪一流程拥有。

决策方法：对架构接点与影响达成一致。

制品及证据：治理模型、库关系状态、相关方影响同意。

适用边界：咨询与登记不能代替正式治理授权。

来源块：C220-web-2025:02-architecture-development-method:b00173, C220-web-2025:02-architecture-development-method:b00174, C220-web-2025:02-architecture-development-method:b00175, C220-web-2025:02-architecture-development-method:b00176, C220-web-2025:02-architecture-development-method:b00177

<details><summary>展开本节完整英文来源</summary>

2.3.2. Confirm Governance and Support Frameworks

The architecture framework will form the keystone to the flavor
(centralized or federated, light or heavy, etc.) of Architecture
Governance organization and guidelines that need to be developed. Part
of the major output of this phase is a framework for Architecture
Governance. We need to understand how architectural material (standards,
guidelines, models, compliance reports, etc.) is brought under
governance; i.e., what type of governance repository characteristics are
going to be required, what relationships and status recording are
necessary to ascertain which governance process (dispensation,
compliance, take-on, retirement, etc.) has ownership of an architectural
artifact.

It is likely that the existing governance and support models of an
organization will need to change to support the newly adopted
architecture framework.

To manage the organizational change required to adopt the new
architectural framework, the current enterprise governance and support
models will need to be assessed to understand their overall shape and
content. Additionally, the sponsors and stakeholders for architecture
will need to be consulted on potential impacts that could occur.

Upon completion of this step, the architecture touch-points and likely
impacts should be understood and agreed by relevant stakeholders.

</details>

<a id="tag_02_03_03"></a>
## 2.3.3. Define and Establish Enterprise Architecture Team and Organization

概念：EA团队建立要连接现有能力、工作差距、职责、预算与其他工作计划。

适用条件：组织分配EA能力管理及治理职责时。

逻辑关系：需要时做成熟度评估；就既有项目计划影响、共同利益和冲突提出变更，并与发起人/委员会审定。

决策方法：分配关键职责、评估约束预算与需变更的工作。

制品及证据：成熟度/差距、角色责任、请求变更、预算与审定依据。

适用边界：岗位配置不能证明人员已具能力或容量。

来源块：C220-web-2025:02-architecture-development-method:b00178, C220-web-2025:02-architecture-development-method:b00179

<details><summary>展开本节完整英文来源</summary>

2.3.3. Define and Establish Enterprise Architecture Team and Organization

Determine existing enterprise and business capability Conduct an Enterprise Architecture/business change maturity
assessment, if required Identify gaps in existing work areas Allocate key roles and responsibilities for Enterprise Architecture
Capability management and governance Define requests for change to existing business programs and projects: Inform existing Enterprise Architecture and IT architecture work of
stakeholder requirements Request assessment of impact on their plans and work Identify common areas of interest Identify any critical differences and conflicts of interest Produce requests for change to stakeholder activities Determine constraints on Enterprise Architecture work Review and agree with sponsors and board Assess budget requirements

</details>

<a id="tag_02_03_04"></a>
## 2.3.4. Identify and Establish Architecture Principles

概念：架构原则依据业务原则并奠定架构治理基础。

适用条件：组织情境已理解后制定原则。

逻辑关系：从本企业业务基础导出适合企业的原则。

决策方法：确定哪些原则适用并进入治理。

制品及证据：架构原则与业务原则关联。

适用边界：不能用标准样例代替本企业原则批准。

来源块：C220-web-2025:02-architecture-development-method:b00180, C220-web-2025:02-architecture-development-method:b00181

<details><summary>展开本节完整英文来源</summary>

2.3.4. Identify and Establish Architecture Principles

Architecture Principles (see the TOGAF Standard — ADM Techniques ) are based on business principles and are
critical in setting the foundation for Architecture Governance. Once the
organizational context is understood, define a set of Architecture
Principles that is appropriate to the enterprise.

</details>

<a id="tag_02_03_05"></a>
## 2.3.5. Tailor the TOGAF Framework and, if any, Other Selected Architecture Framework(s)

概念：框架裁剪有术语、流程和内容三条线。

适用条件：跨企业理解不同、已有任务在别处执行或需要特定制品时。

逻辑关系：术语形成共享词表；流程删除重复、加入特定关卡，并对齐组合、项目、运营交接、配置变更服务管理和采购；内容调整分类与第三方框架。

决策方法：选择删除/增加任务及流程接点，确定内容结构。

制品及证据：企业词汇表、裁剪ADM、接点及内容框架。

适用边界：删任务的理由是已有执行安排，不能默默删掉仍需完成的职责。

来源块：C220-web-2025:02-architecture-development-method:b00182, C220-web-2025:02-architecture-development-method:b00183, C220-web-2025:02-architecture-development-method:b00184

<details><summary>展开本节完整英文来源</summary>

2.3.5. Tailor the TOGAF Framework and, if any, Other Selected Architecture Framework(s)

In this step, determine what tailoring of the TOGAF framework is
required. Consider the need for:

Terminology Tailoring : architecture practitioners should use
terminology that is generally understood across the enterprise Tailoring should produce an agreed terminology set for description of
architectural content. Consideration should be given to the creation of
an Enterprise Glossary, to be updated throughout the architecture
process. Process Tailoring : the TOGAF ADM provides a generic process for
carrying out architecture Process tailoring provides the opportunity to remove tasks that are
already carried out elsewhere in the organization, add
organization-specific tasks (such as specific checkpoints), and to align
the ADM processes to external process frameworks and touch-points. Key
touch-points to be addressed would include: Links to (project and service) portfolio management processes Links to project lifecycle Links to operations handover processes Links to operational management processes (including configuration
management, change management, and service management) Links to procurement processes Content Tailoring : using the TOGAF Architecture Content Framework
and Enterprise Continuum as a basis, tailoring of content structure and
classification approach allows adoption of third-party content
frameworks and also allows for customization of the framework to support
organization-specific requirements

</details>

<a id="tag_02_03_06"></a>
## 2.3.6. Develop a Strategy and Implementation Plan for Tools and Techniques

概念：工具策略涵盖管理、决策、工作坊、模型、办公产品、语言和库，不限于建模软件。

适用条件：利益相关者表达与正式程度、能力文化规模不同。

逻辑关系：工具应让相关方理解和拥有制品；部署须治理制品变更、敏感决策访问和内容安全。

决策方法：按表达需要与敏感度选择普通办公或专业工具实现。

制品及证据：工具策略、实施计划、访问安全和制品变更控制。

适用边界：平衡计分卡是可用例子，不强制所有组织使用。

来源块：C220-web-2025:02-architecture-development-method:b00185, C220-web-2025:02-architecture-development-method:b00186, C220-web-2025:02-architecture-development-method:b00187, C220-web-2025:02-architecture-development-method:b00188

<details><summary>展开本节完整英文来源</summary>

2.3.6. Develop a Strategy and Implementation Plan for Tools and Techniques

There are many tools and techniques which may be used to develop
Enterprise Architecture across many domains. The development of a tools
strategy is recommended that reflects the understanding and level of
formality required by the enterprise’s stakeholders. Architecture
content will be highly dependent on the scale, sophistication, and
culture of both the stakeholders and the Architecture Capability within
the organization. A tools strategy which recognizes the stakeholders’
articulation requirements will enable more effective and rapid
decision-making by stakeholders and their ownership of artifacts.

The strategy should encompass management techniques, decision
management, workshop techniques, business modeling, detailed
infrastructure modeling, office products, languages, and repository
management as well as more formal architecture tools. For example, the
Balanced Scorecard technique is a best practice performance measurement
tool used by business schools and many organizations that can be used
successfully in architecture projects.

The implementation of the tools strategy may be based on common desktop
and office tools or may be based on a customized deployment of
specialist management and architecture tools. Change management of the
artifact deliverables is a major consideration and a degree of
management control and governance of artifacts needs to be considered.
Access to decisions needs to be managed carefully as many of the
artifacts may contain sensitive information. Therefore the tools
implementation, access, and security of the content needs to reflect the
sensitivity requirements.

</details>

<a id="tag_02_03_06_01"></a>
## 2.3.6.1. Issues in Tools Standardization

概念：单一工具与多工具方案存在培训许可交换便利和成熟度适配的取舍。

适用条件：多个组织能力、成熟度、架构关注不同。

逻辑关系：单一工具可能降低维护成本，却可能无法覆盖所有组织需求；工具需匹配团队成熟度目标。

决策方法：评估统一工具或工具套件是否适合各单位。

制品及证据：标准化取舍与能力/目标匹配依据。

适用边界：源文市场描述不可当成当前产品性能评测；不预定单一工具必优。

来源块：C220-web-2025:02-architecture-development-method:b00189, C220-web-2025:02-architecture-development-method:b00190, C220-web-2025:02-architecture-development-method:b00191, C220-web-2025:02-architecture-development-method:b00192

<details><summary>展开本节完整英文来源</summary>

2.3.6.1. Issues in Tools Standardization

In the current state of the tools market, many enterprises developing
Enterprise Architectures struggle with the issue of standardizing on
tools, whether they seek a single “one size fits all” tool or a
multi-tool suite for modeling architectures and generating the different
architecture views required.

There are ostensible advantages associated with selecting a single tool.
Organizations following such a policy can hope to realize benefits such
as reduced training, shared licenses, quantity discounts, maintenance,
and easier data interchange. However, there are also reasons for
refusing to identify a single mandated tool, including reasons of
principle (endorsing a single architecture tool would not encourage
competitive commercial innovation or the development of advanced tool
capability); and the fact that a single tool would not accommodate a
variety of architecture development “maturity levels” and specific needs
across an enterprise.

Successful Enterprise Architecture teams are often those that harmonize
their architecture tools with their architecture maturity level,
team/organizational capabilities, and objectives or focus. If different
organizations within an enterprise are at different architecture
maturity levels and have different objectives or focus (e.g., Enterprise versus Business versus Technology Architecture), it becomes very
difficult for one tool to satisfy all organizations’ needs.

</details>

<a id="tag_02_04"></a>
## 2.4. Outputs

概念：预备输出建立EA组织、裁剪框架、工具、原则、初始库和治理。

适用条件：预备阶段结果交付与治理时。

逻辑关系：组织模型还含工作约束；可重述或引用业务驱动；架构工作请求可选。

决策方法：按企业需要选择可能的输出，明确哪些是现有引用。

制品及证据：EA组织模型、裁剪方法内容、原则目录、配置工具、初始库、治理框架和EA能力架构。

适用边界：源文may include和optional不能改成全部强制交付物。

来源块：C220-web-2025:02-architecture-development-method:b00193, C220-web-2025:02-architecture-development-method:b00194, C220-web-2025:02-architecture-development-method:b00195, C220-web-2025:02-architecture-development-method:b00196, C220-web-2025:02-architecture-development-method:b00197

<details><summary>展开本节完整英文来源</summary>

2.4. Outputs

The outputs of the Preliminary Phase may include, but are not restricted
to:

Organizational Model for Enterprise Architecture (see the TOGAF Standard — Architecture Content ), including: Scope of organizations impacted Maturity assessment, gaps, and resolution approach Roles and responsibilities for architecture team(s) Constraints on architecture work Budget requirements Governance and support strategy Tailored Architecture Framework (see the TOGAF Standard — Architecture Content ), including: Tailored architecture method Tailored architecture content (deliverables and artifacts) Architecture Principles (see the TOGAF Standard — Architecture Content ) Configured and deployed tools Initial Architecture Repository (see the TOGAF Standard — Architecture Content ), populated with framework content Restatement of, or reference to, business principles, business goals,
and business drivers (see the TOGAF Standard — Architecture Content ) Request for Architecture Work (optional) (see the TOGAF Standard — Architecture Content ) Architecture Governance Framework (see the TOGAF Standard — EA Capability and Governance ) The Architecture of the Enterprise Architecture Capability (see the TOGAF Standard — EA Capability and Governance )

The outputs may include some or all of the following:

Catalogs: Principles catalog

</details>

<a id="tag_02_05"></a>
## 2.5. Approach

概念：预备阶段回答哪里、做什么、为什么、谁、如何开展架构。

适用条件：形成战略、中间和战术各层架构能力时。

逻辑关系：能力本身应使用架构最佳实践；可从A回访预备，以确保当前能力适合特定问题。

决策方法：选择团队流程交付物分区并协调业务管理框架。

制品及证据：企业与情境、工作需求原则、框架接点、成熟度及分区基础。

适用边界：EA开发是协作活动，预备完成不保证后续任何问题都能处理。

来源块：C220-web-2025:02-architecture-development-method:b00198, C220-web-2025:02-architecture-development-method:b00199, C220-web-2025:02-architecture-development-method:b00200, C220-web-2025:02-architecture-development-method:b00201, C220-web-2025:02-architecture-development-method:b00202, C220-web-2025:02-architecture-development-method:b00203, C220-web-2025:02-architecture-development-method:b00204, C220-web-2025:02-architecture-development-method:b00205, C220-web-2025:02-architecture-development-method:b00206

<details><summary>展开本节完整英文来源</summary>

2.5. Approach

This Preliminary Phase is about defining “where, what, why, who, and how
we do architecture” in the enterprise concerned. The main aspects are as
follows:

Defining the enterprise Identifying key drivers and elements in the organizational context Defining the requirements for architecture work Defining the Architecture Principles that will inform any architecture
work Defining the framework to be used Defining the relationships between management frameworks Evaluating the Enterprise Architecture maturity

The Enterprise Architecture provides a strategic, top-down view of an organization to enable executives, planners, architects, and engineers to coherently co-ordinate, integrate, and conduct their activities. The Enterprise Architecture framework provides the strategic context within which this team can operate.

Therefore, developing the Enterprise Architecture is not a solitary activity and Enterprise Architects need to recognize the
interoperability between their frameworks and the rest of the business.

Strategic, interim, and tactical business objectives and aspirations
need to be met. Similarly, the Enterprise Architecture needs to reflect
this requirement and allow for operation of architecture discipline at
different levels within the organization.

Depending on the scale of the enterprise and the level of budgetary
commitment to Enterprise Architecture discipline, a number of approaches
may be adopted to sub-divide or partition architecture teams, processes,
and deliverables. Approaches for architecture partitioning are discussed
in the TOGAF Standard — Architecture Content . The Preliminary Phase should be used to determine
the desired approach to partitioning and to establish the groundwork for
the selected approach to be put into practice.

The Preliminary Phase may be revisited, from the Architecture Vision
phase (see the TOGAF Standard — Applying the ADM ), in order to ensure that the organization’s
Architecture Capability is suitable to address a specific architecture
problem.

The Preliminary Phase is about creating an architecture for the
Enterprise Architecture Capability in an organization. As such, the same
best practices employed in developing any architecture should be used
here. Refer to the TOGAF Standard — EA Capability and Governance for an explanation about the
application of the TOGAF ADM to establish the Enterprise Architecture
Capability. Further guidance on how to construct an Enterprise Architecture
Capability may be found in the following document: TOGAF ® Series Guide: The TOGAF Leader’s Guide to Establishing and Evolving an EA Capability .

</details>

<a id="tag_02_05_01"></a>
## 2.5.1. Enterprise

概念：企业范围和联邦性决定主要受益方；必须任命发起人。

适用条件：建立EA能力且范围可能涵盖多个组织。

逻辑关系：发起人保障资源和业务支持，确保所有相关方参与定义、建立和使用。

决策方法：确定企业边界并任命覆盖该边界的发起人。

制品及证据：发起人职责、业务支持和资源安排。

适用边界：范围大于现有权限时不能自行扩大授权。

来源块：C220-web-2025:02-architecture-development-method:b00207, C220-web-2025:02-architecture-development-method:b00208, C220-web-2025:02-architecture-development-method:b00209

<details><summary>展开本节完整英文来源</summary>

2.5.1. Enterprise

One of the main challenges of Enterprise Architecture is that of
enterprise scope.

The scope of the enterprise, and whether it is federated, will determine
those stakeholders who will derive most benefit from the Enterprise
Architecture Capability. It is imperative that a sponsor is appointed at
this stage to ensure that the resultant activity has resources to
proceed and the clear support of the business management. The enterprise
may encompass many organizations and the duties of the sponsor are to
ensure that all stakeholders are included in defining, establishing, and
using the Architecture Capability.

</details>

<a id="tag_02_05_02"></a>
## 2.5.2. Organizational Context

概念：组织情境包括商业/预算、相关方文化策略、现有变化与运营流程、基线及技能。

适用条件：裁剪架构框架前。

逻辑关系：现有框架严谨程度、组合/设计开发方法和景观文档影响形式、投入、接点和内容重点。

决策方法：无预算计划时在预备制定；确定合适严谨程度与内容。

制品及证据：预算、相关方关切、流程和基线/能力情境。

适用边界：文化意图与已存在能力需分别取证。

来源块：C220-web-2025:02-architecture-development-method:b00210, C220-web-2025:02-architecture-development-method:b00211, C220-web-2025:02-architecture-development-method:b00212, C220-web-2025:02-architecture-development-method:b00213, C220-web-2025:02-architecture-development-method:b00214

<details><summary>展开本节完整英文来源</summary>

2.5.2. Organizational Context

In order to make effective and informed decisions about the framework
for architecture to be used within a particular enterprise, it is
necessary to understand the context surrounding the architecture
framework. Specific areas to consider would include:

The commercial models for Enterprise Architecture and budgetary plans
for Enterprise Architecture activity; where no such plans exist, the
Preliminary Phase should be used to develop a budget plan The stakeholders for architecture in the enterprise; their key issues
and concerns The intentions and culture of the organization, as captured within
board business directives, business imperatives, business strategies,
business principles, business goals, and business drivers Current processes that support execution of change and operation of
the enterprise, including the structure of the process and also the
level of rigor and formality applied within the organization Areas for focus should include: Current methods for architecture description Current project management frameworks and methods Current systems management frameworks and methods Current project portfolio management processes and methods Current application portfolio management processes and methods Current technology portfolio management processes and methods Current information portfolio management processes and methods Current systems design and development frameworks and methods The Baseline Architecture landscape, including the state of the
enterprise and also how the landscape is currently represented in
documentation form The skills and capabilities of the enterprise and specific
organizations that will be adopting the framework

Review of the organizational context should provide valuable
requirements on how to tailor the architecture framework in terms of:

Level of formality and rigor to be applied Level of sophistication and expenditure required Touch-points with other organizations, processes, roles, and
responsibilities Focus of content coverage

</details>

<a id="tag_02_05_03"></a>
## 2.5.3. Requirements for Architecture Work

概念：业务迫切需求驱动架构工作需求和性能指标。

适用条件：需要发起人识别决策者、相关方、结果与资源。

逻辑关系：清楚表达业务文化组织战略意图和资金预测，才能圈定工作。

决策方法：明确业务结果、资源及信息要求策略。

制品及证据：工作要求、性能指标、信息要求和主要决策者。

适用边界：预测财务要求不是资金批准。

来源块：C220-web-2025:02-architecture-development-method:b00215, C220-web-2025:02-architecture-development-method:b00216, C220-web-2025:02-architecture-development-method:b00217, C220-web-2025:02-architecture-development-method:b00218

<details><summary>展开本节完整英文来源</summary>

2.5.3. Requirements for Architecture Work

The business imperatives behind the Enterprise Architecture work drive
the requirements and performance metrics for the architecture work. They
should be sufficiently clear so that this phase may scope the business
outcomes and resource requirements, and define the outline enterprise
business information requirements and associated strategies of the
Enterprise Architecture work to be done. For example, these may include:

Business requirements Cultural aspirations Organization intents Strategic intent Forecast financial requirements

Significant elements of these need to be articulated so that the sponsor
can identify all the key decision-makers and stakeholders involved in
defining and establishing an Architecture Capability.

</details>

<a id="tag_02_05_04"></a>
## 2.5.4. Principles

概念：业务原则通常由架构职能外定义；架构原则受治理机构批准。

适用条件：架构项目引用业务原则目标驱动时。

逻辑关系：架构师保证定义当前且澄清歧义，可重述或引用；通常治理机构同时解决架构问题。

决策方法：核实业务依据和原则批准的责任机构。

制品及证据：当前业务原则引用、架构原则及批准记录。

适用边界：不能将架构师澄清权当成业务原则制定权或最终批准权。

来源块：C220-web-2025:02-architecture-development-method:b00219, C220-web-2025:02-architecture-development-method:b00220, C220-web-2025:02-architecture-development-method:b00221, C220-web-2025:02-architecture-development-method:b00222

<details><summary>展开本节完整英文来源</summary>

2.5.4. Principles

The Preliminary Phase defines the Architecture Principles that will form
part of the constraints on any architecture work undertaken in the
enterprise. The issues involved in this are explained in the TOGAF Standard — ADM Techniques .

The definition of Architecture Principles is fundamental to the
development of an Enterprise Architecture. Architecture work is informed
by business principles as well as Architecture Principles. The
Architecture Principles themselves are also normally based in part on
business principles. Defining business principles normally lies outside
the scope of the architecture function. However, depending on how such
principles are defined and promulgated within the enterprise, it may be
possible for the set of Architecture Principles to also restate, or
cross-refer to a set of business principles, business goals, and
strategic business drivers defined elsewhere within the enterprise.
Within an architecture project, the architect will normally need to
ensure that the definitions of these business principles, goals, and
strategic drivers are current, and to clarify any areas of ambiguity.

The issue of Architecture Governance is closely linked to that of
Architecture Principles. The body responsible for governance will also
normally be responsible for approving the Architecture Principles, and
for resolving architecture issues. The issues involved in governance are
explained in the TOGAF Standard — EA Capability and Governance .

</details>

<a id="tag_02_05_05"></a>
## 2.5.5. Management Frameworks

概念：ADM需与业务能力、项目组合、运营、解决方案开发框架协同。

适用条件：EA与企业正式或非正式管理框架并存时。

逻辑关系：框架有交叠，业务能力管理以价值、ROI与控制性能衡量为焦点；系统结合人流程材料技术。

决策方法：确认四类框架交叠和协调方式。

制品及证据：框架关系与业务价值/控制指标。

适用边界：不能把EA狭义化为IT实施；不一定需要改造原ADM。

来源块：C220-web-2025:02-architecture-development-method:b00223, C220-web-2025:02-architecture-development-method:b00224, C220-web-2025:02-architecture-development-method:b00225, C220-web-2025:02-architecture-development-method:b00226, C220-web-2025:02-architecture-development-method:b00227, C220-web-2025:02-architecture-development-method:b00228, C220-web-2025:02-architecture-development-method:b00229, C220-web-2025:02-architecture-development-method:b00230, C220-web-2025:02-architecture-development-method:b00231, C220-web-2025:02-architecture-development-method:b00232

<details><summary>展开本节完整英文来源</summary>

2.5.5. Management Frameworks

The TOGAF ADM is a generic method, intended to be used by enterprises in
a wide variety of industry types and geographies. It is also designed
for use with a wide variety of other Enterprise Architecture frameworks,
if required (although it can be used perfectly well in its own right,
without adaptation).

The TOGAF framework has to co-exist with and enhance the operational
capabilities of other management frameworks that are present within any
organization either formally or informally. In addition to these
frameworks, most organizations have a method for the development of
solutions, most of which have an IT component. The significance of
systems is that they bring together the various domains (also known as
People, Processes, and Material/Technology) to deliver a business
capability.

The main frameworks suggested to be co-ordinated with the TOGAF
framework are:

Business Capability Management that determines what business
capabilities are required to deliver business value including the
definition of return on investment and the requisite control/performance
measures Project/Portfolio Management Methods that determine how a company
manages its change initiatives Operations Management Methods that describe how a company runs its
day-to-day operations, including IT Solution Development Methods that formalize the way that business
systems are delivered in accordance with the structures developed in the
IT architecture

As illustrated in Figure 2-2 , these frameworks are not
discrete and there are significant overlaps between them and the
Business Capability Management. The latter includes the delivery of
performance measured business value.

The overall significance is that the Enterprise Architect applying the
TOGAF framework cannot narrowly focus on the IT implementation, but must
be aware of the impact that the architecture has on the entire
enterprise.



Figure 2-2: Management Frameworks to Co-ordinate with the TOGAF Framework

The Preliminary Phase therefore involves doing any necessary work to
adapt the ADM to define an organization-specific framework, using either
the TOGAF deliverables or the deliverables of another framework. The
issues involved in this are discussed in Section 1.3, “Adapting the ADM” .

</details>

<a id="tag_02_05_06"></a>
## 2.5.6. Relating the Management Frameworks

概念：战略/年度业务规划指导EA，EA组织整合计划并反馈，组合交付组件，运营接收持续运行。

适用条件：跨管理框架协调企业变更时。

逻辑关系：业务规划者贯穿过程保留资源批准；解决方案交付可含建筑技能招聘设备市场等非IT结果。

决策方法：将规划、资源关卡、组合章程和运营接收连接。

制品及证据：业务规划反馈、项目/组合章程、交付物和运营纳入。

适用边界：图中框架关系不定义本企业职位权力；提及IT服务标准版本属于源文。

来源块：C220-web-2025:02-architecture-development-method:b00233, C220-web-2025:02-architecture-development-method:b00234, C220-web-2025:02-architecture-development-method:b00235, C220-web-2025:02-architecture-development-method:b00236, C220-web-2025:02-architecture-development-method:b00237, C220-web-2025:02-architecture-development-method:b00238, C220-web-2025:02-architecture-development-method:b00239, C220-web-2025:02-architecture-development-method:b00240, C220-web-2025:02-architecture-development-method:b00241, C220-web-2025:02-architecture-development-method:b00242, C220-web-2025:02-architecture-development-method:b00243, C220-web-2025:02-architecture-development-method:b00244

<details><summary>展开本节完整英文来源</summary>

2.5.6. Relating the Management Frameworks

Figure 2-3 illustrates a more detailed set of
dependencies between the various frameworks and business planning
activity that incorporates the enterprise’s strategic plan and
direction. The Enterprise Architecture can be used to provide a
structure for all of the corporate initiatives, the Portfolio Management
Framework can be used to deliver the components of the architecture, and
the Operations Management Framework supports incorporation of these new
components within the corporate infrastructure.

The business planners are present throughout the process and are in a
position to support and enforce the architecture by retaining approval
for resources at the various stages of planning and development.

The solution development methodology is used within the Portfolio
Management Framework to plan, create, and deliver the architectural
components specified in the project and portfolio charters. These
deliverables include, but are not exclusively, IT; for example, a new
building, a new set of skills, production equipment, hiring, marketing,
and so on. Enterprise Architecture potentially provides the context for
all enterprise activities.

The management frameworks are required to complement each other and work
in close harmony for the good of the enterprise.



Figure 2-3: Interoperability and Relationships between Management Frameworks

Business planning at the strategy level provides the initial direction
to Enterprise Architecture. Updates at the annual planning level provide
a finer level of ongoing guidance. Capability-based planning is one of
many popular techniques for business planning.

Enterprise Architecture structures the business planning into an
integrated framework that regards the enterprise as a system or system
of systems. This integrated approach will validate the business plan and
can provide valuable feedback to the corporate planners. In some
organizations, the Enterprise Architects have been moved to or work very
closely with the strategic direction groups. The TOGAF approach delivers
a framework for Enterprise Architecture.

Project/portfolio management is the delivery framework that receives the structured, detailed direction that enables them to plan and build what is required, knowing that each assigned deliverable will be in context (i.e., the piece of the puzzle that they deliver will fit into the corporate puzzle that is the Enterprise Architecture). Often this framework is based upon the Project Management Institute or UK Office of Government Commerce (PRINCE2 ® ) project management methodologies. Project architectures and detailed out-of-context design are often based upon systems design methodologies.

Guidance on how to use the TOGAF ADM along with a Project Management framework may be found in the TOGAF ® Series Guide: Architecture Project Management .

Operations management receives the deliverables and then integrates and sustains them within the corporate infrastructure. Often the IT service management services are based upon the IT4IT Reference Architecture, ITIL ® , and ISO/IEC 20000:2011.

</details>

<a id="tag_02_05_07"></a>
## 2.5.7. Planning for Enterprise Architecture/Business Change Maturity Evaluation

概念：成熟度模型通过执行能力所需因素评估与改进步骤支持管理判断。

适用条件：准备EA/业务变更成熟度评估。

逻辑关系：应同时评估架构开发与消费；可自定因素，但推荐裁剪已有模型，政府模型亦可工业使用。

决策方法：选择/裁剪模型和可观察因素。

制品及证据：成熟度因素、执行证据、改进序列。

适用边界：评估洞见不是自动评级；不将模型名称当成当前组织分数。

来源块：C220-web-2025:02-architecture-development-method:b00245, C220-web-2025:02-architecture-development-method:b00246, C220-web-2025:02-architecture-development-method:b00247, C220-web-2025:02-architecture-development-method:b00248, C220-web-2025:02-architecture-development-method:b00249

<details><summary>展开本节完整英文来源</summary>

2.5.7. Planning for Enterprise Architecture/Business Change Maturity Evaluation

Capability Maturity Models are useful ways of assessing the ability of
an enterprise to exercise different capabilities.

Capability Maturity Models typically identify selected factors that are
required to exercise a capability. An organization’s ability to execute
specific factors provides a measure of maturity and can be used to
recommend a series of sequential steps to improve a capability. It is an
assessment that gives executives an insight into pragmatically improving
a capability.

A good Enterprise Architecture maturity model covers the characteristics
necessary to develop and consume Enterprise Architecture. Organizations
can determine their own factors and derive the appropriate maturity
models, but it is recommended to take an existing model and customize it
as required.

Several good models exist, including National Association of State CIOs
(NASCIO), and the US Department of Commerce Architecture Capability
Maturity Model. Other examples include the US Federal Enterprise
Architecture Maturity Model. Even though the models are originally from
government, they are equally applicable to industry.

</details>

<a id="chap03"></a>
## 3. Phase A: Architecture Vision

概念：A阶段形成特定任务范围、相关方、愿景与批准。

适用条件：收到架构工作请求并启动当前ADM轮时。

逻辑关系：愿景连接业务价值、工作范围和开展授权。

决策方法：确定本轮参与方和批准路径。

制品及证据：架构愿景、范围与批准材料。

适用边界：愿景不是详细解决方案或批准事实。

来源块：C220-web-2025:02-architecture-development-method:b00250, C220-web-2025:02-architecture-development-method:b00251, C220-web-2025:02-architecture-development-method:b00252, C220-web-2025:02-architecture-development-method:b00253

<details><summary>展开本节完整英文来源</summary>

3. Phase A: Architecture Vision

This chapter describes the initial phase of the ADM. It includes
information about defining the scope, identifying the stakeholders,
creating the Architecture Vision, and obtaining approvals.



Figure 3-1: Phase A: Architecture Vision

</details>

<a id="tag_03_01"></a>
## 3.1. Objectives

概念：A的双目标为高层能力/业务价值愿景和工作说明书批准。

适用条件：需要给架构开发部署定义工作计划。

逻辑关系：愿景描述愿望，批准工作说明书授权围绕愿景开展工作。

决策方法：明确期望价值与取得工作授权。

制品及证据：高层愿景及获批工作说明书。

适用边界：工作授权不等于具体目标架构或实施方案已获批。

来源块：C220-web-2025:02-architecture-development-method:b00254, C220-web-2025:02-architecture-development-method:b00255, C220-web-2025:02-architecture-development-method:b00256

<details><summary>展开本节完整英文来源</summary>

3.1. Objectives

The objectives of Phase A are to:

Develop a high-level aspirational vision of the capabilities and
business value to be delivered as a result of the proposed Enterprise
Architecture Obtain approval for a Statement of Architecture Work that defines a
program of works to develop and deploy the architecture outlined in the
Architecture Vision

</details>

<a id="tag_03_02"></a>
## 3.2. Inputs

概念：A输入按外部参考、业务请求与已建立EA能力分类。

适用条件：本轮愿景启动。

逻辑关系：3.2.1—3.2.3分别给出资料类别。

决策方法：确认参考、业务请求与能力基线是否齐备。

制品及证据：输入清单及出处。

适用边界：导航不构成材料完整验收。

来源块：C220-web-2025:02-architecture-development-method:b00257, C220-web-2025:02-architecture-development-method:b00258

<details><summary>展开本节完整英文来源</summary>

3.2. Inputs

This section defines the inputs to Phase A.

</details>

<a id="tag_03_02_01"></a>
## 3.2.1. Reference Materials External to the Enterprise

概念：外部输入为架构参考材料。

适用条件：需要愿景参考和既有架构模式时。

逻辑关系：参考适用性须与当前业务需求匹配。

决策方法：选择可用外部参考。

制品及证据：架构参考材料及来源。

适用边界：不能将参考场景当成当前企业事实。

来源块：C220-web-2025:02-architecture-development-method:b00259, C220-web-2025:02-architecture-development-method:b00260

<details><summary>展开本节完整英文来源</summary>

3.2.1. Reference Materials External to the Enterprise

Architecture reference materials (see the TOGAF Standard — Architecture Content )

</details>

<a id="tag_03_02_02"></a>
## 3.2.2. Non-Architectural Inputs

概念：架构工作请求及业务原则目标驱动是非架构输入。

适用条件：业务发起特定架构任务。

逻辑关系：工作请求圈定诉求，业务基础决定愿景方向。

决策方法：确认请求与业务依据当前一致。

制品及证据：工作请求、业务原则目标驱动。

适用边界：请求存在不等于工作计划已批准。

来源块：C220-web-2025:02-architecture-development-method:b00261, C220-web-2025:02-architecture-development-method:b00262

<details><summary>展开本节完整英文来源</summary>

3.2.2. Non-Architectural Inputs

Request for Architecture Work (see the TOGAF Standard — Architecture Content ) Business principles, business goals, and business drivers (see the TOGAF Standard — Architecture Content )

</details>

<a id="tag_03_02_03"></a>
## 3.2.3. Architectural Inputs

概念：A利用EA组织模型、裁剪框架和已有库。

适用条件：预备能力可支持当前任务时。

逻辑关系：组织模型增加复用要求和变更请求；库提供框架、基线描述、ABBs等。

决策方法：确认人员资源、约束和复用要求适合本轮。

制品及证据：组织模型、裁剪方法内容工具、原则、库中既有描述/ABBs。

适用边界：已有框架不适合愿景时需回访预备。

来源块：C220-web-2025:02-architecture-development-method:b00263, C220-web-2025:02-architecture-development-method:b00264

<details><summary>展开本节完整英文来源</summary>

3.2.3. Architectural Inputs

Organizational Model for Enterprise Architecture (see the TOGAF Standard — Architecture Content ),
including: Scope of organizations impacted Maturity assessment, gaps, and resolution approach Roles and responsibilities for architecture team(s) Constraints on architecture work Re-use requirements Budget requirements Requests for change Governance and support strategy Tailored Architecture Framework (see the TOGAF Standard — Architecture Content ), including: Tailored architecture method Tailored architecture content (deliverables and artifacts) Architecture Principles (see the TOGAF Standard — Architecture Content ), including business principles, when pre-existing Configured and deployed tools Populated Architecture Repository (see the TOGAF Standard — Architecture Content ) — existing architectural documentation (framework description,
architectural descriptions, baseline descriptions, Architecture Building
Blocks (ABBs), etc.)

</details>

<a id="tag_03_03"></a>
## 3.3. Steps

概念：A的细节服从本轮请求范围目标，步骤时序由情境与治理裁剪。

适用条件：执行愿景十一项工作。

逻辑关系：相关方、能力就绪、范围、原则、愿景价值风险与工作批准相互支撑。

决策方法：安排步骤顺序与细节，不把列表当严格流水线。

制品及证据：十一项工作结果及治理安排。

适用边界：不能从列表相邻推导额外因果箭头。

来源块：C220-web-2025:02-architecture-development-method:b00265, C220-web-2025:02-architecture-development-method:b00266, C220-web-2025:02-architecture-development-method:b00267, C220-web-2025:02-architecture-development-method:b00268, C220-web-2025:02-architecture-development-method:b00269

<details><summary>展开本节完整英文来源</summary>

3.3. Steps

The level of detail addressed in Phase A will depend on the scope and
goals of the Request for Architecture Work, or the subset of scope and
goals associated with this iteration of architecture development.

The order of the steps in Phase A as well as the time at which they are
formally started and completed should be adapted to the situation at
hand in accordance with the established Architecture Governance.

The steps in Phase A are as follows:

Establish the architecture project; see Section 3.3.1, “Establish the Architecture Project” Identify stakeholders, concerns, and business requirements; see Section 3.3.2, “Identify Stakeholders, Concerns, and Business Requirements” Confirm and elaborate business goals, business drivers, and constraints; see Section 3.3.3, “Confirm and Elaborate Business Goals, Business Drivers, and Constraints” Evaluate capabilities; see Section 3.3.4, “Evaluate Capabilities” Assess readiness for business transformation; see Section 3.3.5, “Assess Readiness for Business Transformation” Define scope; see Section 3.3.6, “Define Scope” Confirm and elaborate Architecture Principles, including business principles; see Section 3.3.7, “Confirm and Elaborate Architecture Principles, including Business Principles” Develop Architecture Vision; see Section 3.3.8, “Develop Architecture Vision” Define the Target Architecture value propositions and KPIs; see Section 3.3.9, “Define the Target Architecture Value Propositions and KPIs” Identify the business transformation risks and mitigation activities; see Section 3.3.10, “Identify the Business Transformation Risks and Mitigation Activities” Develop Statement of Architecture Work; secure approval; see Section 3.3.11, “Develop Statement of Architecture Work; Secure Approval”

</details>

<a id="tag_03_03_01"></a>
## 3.3.1. Establish the Architecture Project

概念：架构循环通常按企业项目管理处理，可独立或嵌入较大项目。

适用条件：建立当前架构工作项目。

逻辑关系：需要组织承认、公司管理背书与直线管理支持，说明其他管理框架关系。

决策方法：采用企业认可规划管理实践并取得支持。

制品及证据：项目认可、管理承诺与框架接点。

适用边界：嵌入项目不免除架构工作管理；管理支持不自动代替正式批准。

来源块：C220-web-2025:02-architecture-development-method:b00270, C220-web-2025:02-architecture-development-method:b00271, C220-web-2025:02-architecture-development-method:b00272

<details><summary>展开本节完整英文来源</summary>

3.3.1. Establish the Architecture Project

Enterprise Architecture is a business capability; each cycle of the ADM
should normally be handled as a project using the project management
framework of the enterprise. In some cases, architecture projects will
be stand-alone. In other cases, architectural activities will be a
subset of the activities within a larger project. In either case,
architecture activity should be planned and managed using accepted
practices for the enterprise.

Conduct the necessary procedures to secure recognition of the project,
the endorsement of corporate management, and the support and commitment
of the necessary line management. Include references to other management
frameworks in use within the enterprise, explaining how this project
relates to those frameworks.

</details>

<a id="tag_03_03_02"></a>
## 3.3.2. Identify Stakeholders, Concerns, and Business Requirements

概念：相关方识别同时产生候选愿景要求、候选范围和沟通表达因素。

适用条件：设置当前任务调查范围与视点。

逻辑关系：相关方图给参与程度关切，支撑愿景、沟通计划和说明书职责；范围内需求入规格、范围外入需求库。

决策方法：选择需开发视图视点及相关方参与安排。

制品及证据：相关方图、关切/视点、需求规格与库、沟通计划起点。

适用边界：相关方图不是组织层级；范围外需求不得丢弃。

来源块：C220-web-2025:02-architecture-development-method:b00273, C220-web-2025:02-architecture-development-method:b00274, C220-web-2025:02-architecture-development-method:b00275, C220-web-2025:02-architecture-development-method:b00276, C220-web-2025:02-architecture-development-method:b00277, C220-web-2025:02-architecture-development-method:b00278, C220-web-2025:02-architecture-development-method:b00279

<details><summary>展开本节完整英文来源</summary>

3.3.2. Identify Stakeholders, Concerns, and Business Requirements

Identify the key stakeholders and their concerns/objectives, and define
the key business requirements to be addressed in the architecture
engagement. Stakeholder engagement at this stage is intended to
accomplish three objectives:

To identify candidate vision components and requirements to be tested
as the Architecture Vision is developed To identify candidate scope boundaries for the engagement to limit the
extent of architectural investigation required To identify stakeholder concerns, issues, and cultural factors that
will shape how the architecture is presented and communicated

The major product resulting from this step is a stakeholder map for the
engagement, showing which stakeholders are involved with the engagement,
their level of involvement, and their key concerns (see the TOGAF Standard — ADM Techniques ). The
stakeholder map is used to support various outputs of the Architecture
Vision phase, and to identify:

The concerns and viewpoints that are relevant to this project; this is
captured in the Architecture Vision (see the TOGAF Standard — Architecture Content ) The stakeholders that are involved with the project and as a result
form the starting point for a Communications Plan (see the TOGAF Standard — Architecture Content ) The key roles and responsibilities within the project, which should be
included within the Statement of Architecture Work (see the TOGAF Standard — Architecture Content )

Another key task will be to consider which architecture views and
viewpoints need to be developed to satisfy the various stakeholder
requirements. As described in the TOGAF Standard — ADM Techniques ,
understanding at this stage which stakeholders and which views need to
be developed is important in setting the scope of the engagement.

During the Architecture Vision phase, new requirements generated for
future architecture work within the scope of the selected requirements
need to be documented within the Architecture Requirements
Specification, and new requirements which are beyond the scope of the
selected requirements must be input to the Requirements Repository for
management through the Requirements Management process.

</details>

<a id="tag_03_03_03"></a>
## 3.3.3. Confirm and Elaborate Business Goals, Business Drivers, and Constraints

概念：业务目标驱动和企业/项目约束须当前且清楚。

适用条件：业务基础已有或首次定义时。

逻辑关系：已有定义需查新和澄清；无定义时回到说明书发起人协同并取得公司管理背书。

决策方法：确认目标、时间资源等约束及其责任来源。

制品及证据：当前目标驱动约束和背书。

适用边界：架构师不能凭空定义战略并自我批准。

来源块：C220-web-2025:02-architecture-development-method:b00280, C220-web-2025:02-architecture-development-method:b00281, C220-web-2025:02-architecture-development-method:b00282, C220-web-2025:02-architecture-development-method:b00283

<details><summary>展开本节完整英文来源</summary>

3.3.3. Confirm and Elaborate Business Goals, Business Drivers, and Constraints

Identify the business goals and strategic drivers of the organization.

If these have already been defined elsewhere within the enterprise,
ensure that the existing definitions are current, and clarify any areas
of ambiguity. Otherwise, go back to the originators of the Statement of
Architecture Work and work with them to define these essential items and
secure their endorsement by corporate management.

Define the constraints that must be dealt with, including
enterprise-wide constraints and project-specific constraints (time,
schedule, resources, etc.). The enterprise-wide constraints may be
informed by the business and Architecture Principles developed in the
Preliminary Phase or clarified as part of Phase A.

</details>

<a id="tag_03_03_04"></a>
## 3.3.4. Evaluate Capabilities

概念：能力评估区分开发/消费架构的EA能力与企业基线/目标业务能力。

适用条件：判断本轮架构能否继续及变更能否执行。

逻辑关系：EA技能信息流程工具短缺可触发A与预备迭代；详细业务差距在B，变更能力限制影响目标及E/F迁移。

决策方法：确定EA能力是否足以推进，识别所需业务能力及粗粒度差距。

制品及证据：能力评估、基线目标能力和价值链关联。

适用边界：信息/能力未知不能评成充分；A粗评不冒充B详细差距。

来源块：C220-web-2025:02-architecture-development-method:b00284, C220-web-2025:02-architecture-development-method:b00285, C220-web-2025:02-architecture-development-method:b00286, C220-web-2025:02-architecture-development-method:b00287, C220-web-2025:02-architecture-development-method:b00288, C220-web-2025:02-architecture-development-method:b00289

<details><summary>展开本节完整英文来源</summary>

3.3.4. Evaluate Capabilities

It is valuable to understand a collection of capabilities within the
enterprise. One part refers to the capability of the enterprise to
develop and consume the architecture. The second part refers to the
baseline and target capability level of the enterprise. Gaps identified
in the Architecture Capability require iteration between Architecture
Vision and Preliminary Phase to ensure that the Architecture Capability
is suitable to address the scope of the architecture project (see the TOGAF Standard — Applying the ADM ).

A key step following from evaluation of business models, or artifacts
that clarify priorities of a business strategy, is to identify the
required business capabilities the enterprise must possess to act on the
strategic priorities.

The detailed assessment of business capability gaps belongs in Phase B
as a core aspect of the Business Architecture, where the architect can
help the enterprise understand gaps throughout the business, of many
types, that need to be addressed in later phases of the architecture.

In the Architecture Vision phase, however, the architect should consider
the capability of the enterprise to develop the Enterprise Architecture
itself, as required in the specific initiative or project underway. Gaps
in the ability to progress through the ADM, whether deriving from skill
shortages, information required, process weakness, or systems and tools,
are a serious consideration in the vision of whether the architecture
effort should continue. The architect can find guidance in Section 3.5, “Approach” to gather existing business capability
frameworks for the enterprise in this early assessment.

Gaps, or limitations, identified in the enterprise’s capability to
execute on change will inform the architect on the description of the
Target Architecture and on the Implementation and Migration Plan (see
the TOGAF Standard — Architecture Content ) created in Phase E and Phase F. This step seeks
to understand the capabilities and desires of the enterprise at an
appropriate level of abstraction (see the TOGAF Standard — Applying the ADM ).
Consideration of the gap between the baseline and target capability of
the enterprise is critical. Showing the baseline and target capabilities
within the context of the overall enterprise can be supported by
creating Value Chain diagrams that show the linkage of related
capabilities. The results of the assessment are documented in a
Capability Assessment (see the TOGAF Standard — Architecture Content ).

</details>

<a id="tag_03_03_05"></a>
## 3.3.5. Assess Readiness for Business Transformation

概念：变更就绪评估按因素分析/评级，可定量组织变更准备程度。

适用条件：愿景可能要求业务转型。

逻辑关系：结果写入能力评估，塑造范围、项目活动与风险重点。

决策方法：选择有依据的就绪因素和后续行动。

制品及证据：就绪证据、因素评估及更新的能力评估。

适用边界：未给数据时不能自动量化评分；通用就绪与G212特定数字采用模型需区别。

来源块：C220-web-2025:02-architecture-development-method:b00290, C220-web-2025:02-architecture-development-method:b00291, C220-web-2025:02-architecture-development-method:b00292

<details><summary>展开本节完整英文来源</summary>

3.3.5. Assess Readiness for Business Transformation

A Business Transformation Readiness Assessment can be used to evaluate
and quantify the organization’s readiness to undergo a change. This
assessment is based upon the determination and analysis/rating of a
series of readiness factors, as described in the TOGAF Standard — ADM Techniques .

The results of the readiness assessment should be added to the
Capability Assessment (see the TOGAF Standard — Architecture Content ). These results are then used to shape the scope of the
architecture, to identify activities required within the architecture
project, and to identify risk areas to be addressed.

</details>

<a id="tag_03_03_06"></a>
## 3.3.6. Define Scope

概念：范围区分基线与目标内外，二者细节不必相同。

适用条件：限定本轮愿景和开发。

逻辑关系：基线可更抽象，以留资源深入目标；范围含广度细节分区域时间过渡与复用资产。

决策方法：明确范围内外、两状态粒度及复用来源。

制品及证据：范围、分区、域、时间和资产选择记录。

适用边界：允许两状态不同粒度不是允许所选域间无理由失衡；仍受1.5约束。

来源块：C220-web-2025:02-architecture-development-method:b00293, C220-web-2025:02-architecture-development-method:b00294, C220-web-2025:02-architecture-development-method:b00295

<details><summary>展开本节完整英文来源</summary>

3.3.6. Define Scope

Define what is inside and what is outside the scope of the Baseline
Architecture and Target Architecture efforts, understanding that the
baseline and target need not be described at the same level of detail.
In many cases, the baseline is described at a higher level of
abstraction, so more time is available to specify the target in
sufficient detail. The issues involved in this are discussed in Section 1.5, “Scoping the Architecture” .
In particular, define:

The breadth of coverage of the enterprise The level of detail required The partitioning characteristics of the architecture (see the TOGAF Standard — Applying the ADM for more details) The specific architecture domains to be covered (Business, Data,
Application, Technology) The extent of the time period aimed at, plus the number and extent of
any intermediate time period The architectural assets to be leveraged, or considered for use, from
the organization’s Architecture Repository: Assets created in previous iterations of the ADM cycle within the
enterprise Assets available elsewhere in the industry (other frameworks, systems
models, vertical industry models, etc.)

</details>

<a id="tag_03_03_07"></a>
## 3.3.7. Confirm and Elaborate Architecture Principles, including Business Principles

概念：A重新确认架构及业务原则的时效和含义。

适用条件：预备原则已有或尚未定义时。

逻辑关系：缺失时与架构治理机构共同定义并取得管理背书。

决策方法：核查原则当前性、歧义及批准责任。

制品及证据：原则定义、引用和治理背书。

适用边界：样例原则不构成组织原则。

来源块：C220-web-2025:02-architecture-development-method:b00296, C220-web-2025:02-architecture-development-method:b00297

<details><summary>展开本节完整英文来源</summary>

3.3.7. Confirm and Elaborate Architecture Principles, including Business Principles

Review the principles under which the architecture is to be developed.
Architecture Principles are normally based on the principles developed
as part of the Preliminary Phase. They are explained, and an example set
given, in the TOGAF Standard — ADM Techniques . Ensure that the existing definitions are current, and
clarify any areas of ambiguity. Otherwise, go back to the body
responsible for Architecture Governance and work with them to define
these essential items for the first time and secure their endorsement by
corporate management.

</details>

<a id="tag_03_03_08"></a>
## 3.3.8. Develop Architecture Vision

概念：愿景先决定整体域交付物如何组合，再以相关方关切形成高层基线/目标。

适用条件：需要战略方向、政策决策和后续量化依据时。

逻辑关系：政策合理化收入目标等需捕获；简洁解决方案概念图或业务场景可表达收益，初始版本入库。

决策方法：选定行动路径与高层总体架构并在相关方图反映其决定。

制品及证据：愿景、概念图/场景、初始基线目标和策略决定。

适用边界：概念图是高层表达，不能替代详细域分析或业务批准。

来源块：C220-web-2025:02-architecture-development-method:b00298, C220-web-2025:02-architecture-development-method:b00299, C220-web-2025:02-architecture-development-method:b00300, C220-web-2025:02-architecture-development-method:b00301, C220-web-2025:02-architecture-development-method:b00302, C220-web-2025:02-architecture-development-method:b00303, C220-web-2025:02-architecture-development-method:b00304, C220-web-2025:02-architecture-development-method:b00305

<details><summary>展开本节完整英文来源</summary>

3.3.8. Develop Architecture Vision

An understanding of the required artifacts will enable the stakeholders
to start to scope out their decision-making which will guide subsequent
phases. These decisions need to be reflected in the stakeholder map.

Policy development and strategic decisions need to be captured in this
phase to enable the subsequent work to be quantified; for example,
rationalization decisions and metrics, revenue generation, and targets
which meet the business strategy. There are also other areas which need
to be addressed; for example, Digital Transformation and IT strategy
where decisions on the Architecture Vision will provide leadership and
direction for the organization in subsequent phases.

For the Architecture Vision it is recommended that first an overall
architecture be decided upon showing how all of the various architecture
domain deliverables will fit together (based upon the selected course of
action).

Based on the stakeholder concerns, business capability requirements,
scope, constraints, and principles, create a high-level view of the
Baseline and Target Architectures. The Architecture Vision typically
covers the breadth of scope identified for the project, at a high level.
Informal techniques are often employed. A common practice is to draw a
simple solution concept diagram that illustrates concisely the major
components of the solution and how the solution will result in benefit
for the enterprise.

Business scenarios are an appropriate and useful technique to discover
and document business requirements, and to articulate an Architecture
Vision that responds to those requirements. Business scenarios may also
be used at more detailed levels of the architecture work (e.g., in Phase
B) and are described in the TOGAF ® Series Guide: Business Scenarios .

This step generates the first, very high-level definitions of the
baseline and target environments, from a business, information systems,
and technology perspective, as described in Section 3.4, “Outputs” .

These initial versions of the architecture should be stored in the
Architecture Repository, organized according to the standards and
guidelines established in the architecture framework.

</details>

<a id="tag_03_03_09"></a>
## 3.3.9. Define the Target Architecture Value Propositions and KPIs

概念：价值主张应逐相关方组形成，并纳入工作说明书跟踪。

适用条件：要求业务论证、采购要求与性能衡量时。

逻辑关系：业务案例、采购、指标、业务风险一起支持与发起人相关方同意的价值主张。

决策方法：确认各组价值和指标/测量方法。

制品及证据：价值主张、采购要求、性能指标、风险及说明书内容。

适用边界：指标存在不证明收益已实现。

来源块：C220-web-2025:02-architecture-development-method:b00306, C220-web-2025:02-architecture-development-method:b00307, C220-web-2025:02-architecture-development-method:b00308

<details><summary>展开本节完整英文来源</summary>

3.3.9. Define the Target Architecture Value Propositions and KPIs

Develop the business case for the architectures and changes required Produce the value proposition for each of the stakeholder groupings Assess and define the procurement requirements Review and agree the value propositions with the sponsors and stakeholders concerned Define the performance metrics and measures to be built into the
Enterprise Architecture to meet the business needs Assess the business risk (see the TOGAF Standard — ADM Techniques )

The outputs from this activity should be incorporated within the
Statement of Architecture Work to allow performance to be tracked
accordingly.

</details>

<a id="tag_03_03_10"></a>
## 3.3.10. Identify the Business Transformation Risks and Mitigation Activities

概念：风险区分缓解前初始等级与实施缓解后的剩余等级。

适用条件：愿景带来业务转型风险。

逻辑关系：评估严重度及可能频率，逐风险分配缓解策略，并考虑纳入说明书。

决策方法：确定初始风险、缓解动作和何时可评剩余风险。

制品及证据：风险评估、缓解活动及说明书关联。

适用边界：计划缓解未执行时不能把预计剩余风险当实际剩余。

来源块：C220-web-2025:02-architecture-development-method:b00309, C220-web-2025:02-architecture-development-method:b00310, C220-web-2025:02-architecture-development-method:b00311, C220-web-2025:02-architecture-development-method:b00312, C220-web-2025:02-architecture-development-method:b00313

<details><summary>展开本节完整英文来源</summary>

3.3.10. Identify the Business Transformation Risks and Mitigation Activities

Identify the risks associated with the Architecture Vision and assess
the initial level of risk (e.g., catastrophic, critical, marginal, or
negligible) and the potential frequency associated with it. Assign a
mitigation strategy for each risk. A risk management framework is
described in the TOGAF Standard — ADM Techniques .

There are two levels of risk that should be considered, namely:

Initial Level of Risk : risk categorization prior to determining and
implementing mitigating actions Residual Level of Risk : risk categorization after implementation of
mitigating actions (if any)

Risk mitigation activities should be considered for inclusion within the
Statement of Architecture Work.

</details>

<a id="tag_03_03_11"></a>
## 3.3.11. Develop Statement of Architecture Work; Secure Approval

概念：工作说明书将工作产品、性能、变更影响、资源依赖、时间与沟通连接到授权。

适用条件：请求正式开展当前ADM周期。

逻辑关系：评估工作产品所需时间与业务性能，协调已有块/产品变更；形成资源路线图日程及沟通计划，按治理获正式批准和发起人签字。

决策方法：判断可用资源与时限，选域细节视图，确认计划可行并取批准。

制品及证据：说明书、性能产品、计划资源日程、依赖影响与沟通计划。

适用边界：资源估计不等于可用容量；文档生成或签字段不等于签字批准。

来源块：C220-web-2025:02-architecture-development-method:b00314, C220-web-2025:02-architecture-development-method:b00315, C220-web-2025:02-architecture-development-method:b00316, C220-web-2025:02-architecture-development-method:b00317, C220-web-2025:02-architecture-development-method:b00318

<details><summary>展开本节完整英文来源</summary>

3.3.11. Develop Statement of Architecture Work; Secure Approval

Assess the work products that are required to be produced (and by when)
against the set of business performance requirements. This will involve
ensuring that:

Performance metrics are built into the work products Specific performance-related work products are available

Then, activities will include:

Identify new work products that will need to be changed Provide direction on which existing work products, including building
blocks, will need to be changed and ensure that all activities and
dependencies on these are co-ordinated Identify the impact of change on other work products and dependence on
their activities Based on the purpose, focus, scope, and constraints, determine which
architecture domains should be developed, to what level of detail, and
which architecture views should be built Assess the resource requirements and availability to perform the work
in the timescale required; this will include adhering to the
organization’s planning methods and work products to produce the plans
for performing a cycle of the ADM Estimate the resources needed, develop a roadmap and schedule for the
proposed development, and document all these in the Statement of
Architecture Work Define the performance metrics to be met during this cycle of the ADM
by the Enterprise Architecture team Develop the specific Enterprise Architecture Communications Plan and
show where, how, and when the Enterprise Architects will communicate
with the stakeholders, including affinity groupings and communities,
about the progress of the Enterprise Architecture developments Review and agree the plans with the sponsors, and secure formal
approval of the Statement of Architecture Work under the appropriate
governance procedures Gain sponsor’s sign-off to proceed

</details>

<a id="tag_03_04"></a>
## 3.4. Outputs

概念：A输出强调已批准工作说明书、愿景、能力评估、参与任务裁剪和草稿定义文档。

适用条件：当前轮愿景交付。

逻辑关系：愿景可含可选场景、摘要视图和高层需求；多场景可支持同一愿景，库持续补充。

决策方法：依情境选择输出并准确标示批准和草稿。

制品及证据：说明书计划、原则、能力评估、裁剪框架、愿景、草稿定义文档、沟通计划。

适用边界：输出may include并非每项必选，草稿定义文档不是已批准架构。

来源块：C220-web-2025:02-architecture-development-method:b00319, C220-web-2025:02-architecture-development-method:b00320, C220-web-2025:02-architecture-development-method:b00321, C220-web-2025:02-architecture-development-method:b00322

<details><summary>展开本节完整英文来源</summary>

3.4. Outputs

The outputs of Phase A may include, but are not restricted to:

Approved Statement of Architecture Work (see the TOGAF Standard — Architecture Content ), including in particular: Architecture project description and scope Overview of Architecture Vision Architecture project plan and schedule Refined statements of business principles, business goals, and
business drivers (see the TOGAF Standard — Architecture Content ) Architecture Principles (see the TOGAF Standard — ADM Techniques ) Capability Assessment (see the TOGAF Standard — Architecture Content ) Tailored Architecture Framework (see the TOGAF Standard — Architecture Content ) (for the engagement), including: Tailored architecture method Tailored architecture content (deliverables and artifacts) Configured and deployed tools Architecture Vision (see the TOGAF Standard — Architecture Content ), including: Problem description Objective of the Statement of Architecture Work Summary views Business scenario (optional) Refined key high-level stakeholder requirements Draft Architecture Definition Document, which may include Baseline
and/or Target Architectures of any architecture domain Communications Plan (see the TOGAF Standard — Architecture Content ) Additional content populating the Architecture Repository (see the TOGAF Standard — Architecture Content ) Note: Multiple business scenarios may be used to generate a single
Architecture Vision.

The TOGAF Standard — Architecture Content contains a detailed description of architectural
artifacts which might be produced in this phase, describing them in
detail and relating them to entities, attributes, and relationships in
the TOGAF Enterprise Metamodel.

</details>

<a id="tag_03_05"></a>
## 3.5. Approach

概念：本标题为结构容器，无独立说明段落。

适用条件：阅读该主题时应继续读取下列子节。

逻辑关系：子节分工：tag_03_05_01: 3.5.1. General；tag_03_05_02: 3.5.2. Creating the Architecture Vision

决策方法：不从空容器推出附加规则或完成状态。

制品及证据：实际概念、决策和制品证据见上述子节。

适用边界：空容器覆盖仅证明目录和子节连接，不计额外深度结论。

来源块：C220-web-2025:02-architecture-development-method:b00323

<details><summary>展开本节完整英文来源</summary>

3.5. Approach

</details>

<a id="tag_03_05_01"></a>
## 3.5.1. General

概念：A由发起组织的架构工作请求开始，受预备总范围限制。

适用条件：当前框架可能不能支撑期望愿景。

逻辑关系：按资源能力价值圈定本轮；不适合时回访预备并扩展框架，已有业务原则目标优先核实。

决策方法：判断本轮是否在现有框架能力与范围内。

制品及证据：请求、范围依据、原则核实或框架扩展。

适用边界：不能以本轮目标自行突破原总体授权。

来源块：C220-web-2025:02-architecture-development-method:b00324, C220-web-2025:02-architecture-development-method:b00325, C220-web-2025:02-architecture-development-method:b00326, C220-web-2025:02-architecture-development-method:b00327, C220-web-2025:02-architecture-development-method:b00328, C220-web-2025:02-architecture-development-method:b00329, C220-web-2025:02-architecture-development-method:b00330, C220-web-2025:02-architecture-development-method:b00331

<details><summary>展开本节完整英文来源</summary>

3.5.1. General

Phase A starts with receipt of a Request for Architecture Work from the
sponsoring organization to the architecture organization.

The issues involved in ensuring proper recognition and endorsement from
corporate management, and the support and commitment of line management,
are discussed in the TOGAF Standard — EA Capability and Governance .

Phase A also defines what is in and what is outside the scope of the
architecture effort and the constraints that must be dealt with. Scoping
decisions need to be made on the basis of a practical assessment of
resource and competence availability, and the value that can
realistically be expected to accrue to the enterprise from the chosen
scope of architecture work. The issues involved in this are discussed in Section 1.5, “Scoping the Architecture” .
Scoping issues addressed in the Architecture Vision phase will be restricted to
the specific objectives for this ADM cycle and will be constrained
within the overall scope definition for architecture activity as
established within the Preliminary Phase and embodied within the
architecture framework.

In situations where the architecture framework in place is not
appropriate to achieve the desired Architecture Vision, revisit the
Preliminary Phase and extend the overall architecture framework for the
enterprise.

The constraints will normally be informed by the business principles and
Architecture Principles, developed as part of the Preliminary Phase; see Chapter 2, Preliminary Phase .

Normally, the business principles, business goals, and strategic drivers
of the organization are already defined elsewhere in the enterprise. If
so, the activity in Phase A is involved with ensuring that existing
definitions are current, and clarifying any areas of ambiguity.
Otherwise, it involves defining these essential items for the first
time.

Similarly, the Architecture Principles that form part of the constraints
on architecture work will normally have been defined in the Preliminary
Phase; see Chapter 2, Preliminary Phase .
The activity in Phase A is concerned with ensuring that the existing principle definitions are current, and clarifying any areas of ambiguity. Otherwise, it entails defining the Architecture Principles for the first time, as explained in the TOGAF Standard — ADM Techniques .

</details>

<a id="tag_03_05_02"></a>
## 3.5.2. Creating the Architecture Vision

概念：愿景让发起人向相关方说明能力收益并形成共识。

适用条件：既有战略需连接当前现实，或业务架构研究尚少。

逻辑关系：研究验证业务目标流程；寻找能力/价值流/组织图，其他专业域可独立或关联；评估行动路径，形成四域高层基线目标。

决策方法：澄清目的，选择路径，决定是否在范围内新建能力框架，并取得说明书签署共识。

制品及证据：高层愿景、能力价值流组织资料、业务评估和签署说明书。

适用边界：理解新兴技术不等于选择产品；共识应有发起组织签署证据。

来源块：C220-web-2025:02-architecture-development-method:b00332, C220-web-2025:02-architecture-development-method:b00333, C220-web-2025:02-architecture-development-method:b00334, C220-web-2025:02-architecture-development-method:b00335, C220-web-2025:02-architecture-development-method:b00336, C220-web-2025:02-architecture-development-method:b00337, C220-web-2025:02-architecture-development-method:b00338, C220-web-2025:02-architecture-development-method:b00339, C220-web-2025:02-architecture-development-method:b00340, C220-web-2025:02-architecture-development-method:b00341, C220-web-2025:02-architecture-development-method:b00342, C220-web-2025:02-architecture-development-method:b00343, C220-web-2025:02-architecture-development-method:b00344, C220-web-2025:02-architecture-development-method:b00345, C220-web-2025:02-architecture-development-method:b00346

<details><summary>展开本节完整英文来源</summary>

3.5.2. Creating the Architecture Vision

The Architecture Vision provides the sponsor with a key tool to sell the
benefits of the proposed capability to stakeholders and decision-makers
within the enterprise. Architecture Vision describes how the new
capability will meet the business goals and strategic objectives and
address the stakeholder concerns when implemented.

Integral to the Architecture Vision is an understanding of emerging
technologies and their potential impact on industries and enterprises,
without which many business opportunities may be missed.

Clarifying and agreeing the purpose of the architecture effort is one of
the key parts of this activity, and the purpose needs to be clearly
reflected in the vision that is created. Architecture projects are often
undertaken with a specific purpose in mind — a specific set of business
drivers that represent the return on investment for the stakeholders in
the architecture development. Clarifying that purpose, and demonstrating
how it will be achieved by the proposed architecture development, is the
whole point of the Architecture Vision.

Normally, key elements of the Architecture Vision — such as the
enterprise mission, vision, strategy, and goals — have been documented
as part of some wider business strategy or enterprise planning activity
that has its own lifecycle within the enterprise. In such cases, the
activity in Phase A is concerned with verifying and understanding the
documented business strategy and goals, and possibly bridging between
the enterprise strategy and goals on the one hand, and the strategy and
goals implicit within the current architecture reality.

Business models are key strategy artifacts that can provide such a perspective, by showing how the organization intends to deliver value to
its customers and stakeholders. Section 3.3.4, “Evaluate Capabilities” introduces the application of business models as a step in developing the Architecture Vision.

In other cases, little or no Business Architecture work may have been
done to date. In such cases, there will be a need for the architecture
team to research, verify, and gain buy-in to the key business objectives
and processes that the architecture is to support. This may be done as a
free-standing exercise, either preceding architecture development, or as
part of the ADM initiation phase (Preliminary Phase).

This exercise should examine and search for existing materials on
fundamental Business Architecture concepts such as:

Business Capabilities , which represent a particular ability or
capacity that a business may possess or exchange to achieve a specific
purpose or outcome In this phase, the architect should determine whether a framework exists
in the organization to represent business capabilities. If one does not
exist, the architect should consider whether developing a framework is
within the scope of the project. For an introduction to business
capabilities, see TOGAF ® Series Guide: Business Capabilities . Value Streams , which represent an end-to-end collection of
value-adding activities that create an overall result for a customer,
stakeholder, or end user; for an introduction to value streams, see the TOGAF ® Series Guide: Value Streams . Organization Maps , which depict the relationships between the
primary entities that make up the enterprise, its partners, and
stakeholders As traditional organizational charts often lack the necessary detail to
reflect the full scope of the enterprise’s activities, the architect can
help to identify and understand the complex web of relationships between
business entities as well as where business capabilities are used and
connection to value stream stages. These are refined and extended in
subsequent phases. For an introduction to organization maps, see the TOGAF ® Series Guide: Organization Mapping .

In addition, the Architecture Vision explores other domains which are
appropriate for the Enterprise Architecture in hand. These domains may
include elements of the basic domains, yet serve an additional purpose
for the stakeholders. Example domains may include:

Information Security Digital Network Management Knowledge Industry-specific Services Partnership Cybersecurity

These domains may be free-standing or linked with other domains to
provide enterprise-wide views of the organization vision and structure.

The Architecture Vision phase includes the conduct of a business
assessment (using, for example, business scenarios) where critical
factors are documented and various courses of action are assessed.
High-level advantages and disadvantages, including risks and
opportunities, are documented and the best course of action selected to
serve as the basis for the Architecture Vision.

The Architecture Vision provides a first-cut, high-level description of
the Baseline and Target Architectures, covering the Business, Data,
Application, and Technology domains. These outline descriptions are
developed in subsequent phases.

Once an Architecture Vision is defined and documented in the Statement
of Architecture Work, it is critical to use it to build a consensus, as
described in the TOGAF Standard — EA Capability and Governance . Without this consensus it is
very unlikely that the final architecture will be accepted by the
organization as a whole. The consensus is represented by the sponsoring
organization signing the Statement of Architecture Work.

</details>

<a id="chap04"></a>
## 4. Phase B: Business Architecture

概念：B开发支持约定愿景的业务架构。

适用条件：愿景范围要求业务如何运作的具体描述时。

逻辑关系：业务架构为后续数据应用技术提供业务基础。

决策方法：确定业务建模范围。

制品及证据：业务基线/目标和对应阶段图。

适用边界：可复用既有业务理解，不能跳过业务依据。

来源块：C220-web-2025:02-architecture-development-method:b00347, C220-web-2025:02-architecture-development-method:b00348, C220-web-2025:02-architecture-development-method:b00349, C220-web-2025:02-architecture-development-method:b00350

<details><summary>展开本节完整英文来源</summary>

4. Phase B: Business Architecture

This chapter describes the development of a Business Architecture to
support an agreed Architecture Vision.



Figure 4-1: Phase B: Business Architecture

</details>

<a id="tag_04_01"></a>
## 4.1. Objectives

概念：B目标是描述达成业务目标与战略驱动所需目标运作方式并找路线图候选。

适用条件：工作说明书与相关方关切已界定。

逻辑关系：基线目标差距产生候选变更组件。

决策方法：判断目标是否响应愿景及关切。

制品及证据：目标业务架构、差距及候选路线图组件。

适用边界：候选路线图不等于跨域实施计划。

来源块：C220-web-2025:02-architecture-development-method:b00351, C220-web-2025:02-architecture-development-method:b00352, C220-web-2025:02-architecture-development-method:b00353

<details><summary>展开本节完整英文来源</summary>

4.1. Objectives

The objectives of Phase B are to:

Develop the Target Business Architecture that describes how the
enterprise needs to operate to achieve the business goals, and respond
to the strategic drivers set out in the Architecture Vision, in a way
that addresses the Statement of Architecture Work and stakeholder
concerns Identify candidate Architecture Roadmap components based upon gaps
between the Baseline and Target Business Architectures

</details>

<a id="tag_04_02"></a>
## 4.2. Inputs

概念：B输入继承A授权和愿景并补充参考与业务能力情境。

适用条件：开始B开发时。

逻辑关系：4.2.1—4.2.3分别列外部、非架构、架构输入。

决策方法：确认各类输入状态。

制品及证据：输入登记与出处。

适用边界：必须区分A已批准说明书和仍草稿的定义文档。

来源块：C220-web-2025:02-architecture-development-method:b00354, C220-web-2025:02-architecture-development-method:b00355

<details><summary>展开本节完整英文来源</summary>

4.2. Inputs

This section defines the inputs to Phase B.

</details>

<a id="tag_04_02_01"></a>
## 4.2.1. Reference Materials External to the Enterprise

概念：B外部输入为架构参考材料。

适用条件：选择业务参考模式时。

逻辑关系：资源应与本业务驱动关切匹配。

决策方法：确定参考适用性。

制品及证据：架构参考及来源。

适用边界：参考模式不是组织业务事实。

来源块：C220-web-2025:02-architecture-development-method:b00356, C220-web-2025:02-architecture-development-method:b00357

<details><summary>展开本节完整英文来源</summary>

4.2.1. Reference Materials External to the Enterprise

Architecture reference materials (see the TOGAF Standard — Architecture Content )

</details>

<a id="tag_04_02_02"></a>
## 4.2.2. Non-Architectural Inputs

概念：B非架构输入含工作请求、业务驱动、能力评估和沟通计划。

适用条件：业务目标及参与安排传入B。

逻辑关系：能力与沟通情况影响业务模型和审阅。

决策方法：确认能力/参与条件。

制品及证据：请求、业务原则目标驱动、能力评估和沟通计划。

适用边界：能力评估中的缺口不能因进入B而消除。

来源块：C220-web-2025:02-architecture-development-method:b00358, C220-web-2025:02-architecture-development-method:b00359

<details><summary>展开本节完整英文来源</summary>

4.2.2. Non-Architectural Inputs

Request for Architecture Work (see the TOGAF Standard — Architecture Content ) Business principles, business goals, and business drivers (see the TOGAF Standard — Architecture Content ) Capability Assessment (see the TOGAF Standard — Architecture Content ) Communications Plan (see the TOGAF Standard — Architecture Content )

</details>

<a id="tag_04_02_03"></a>
## 4.2.3. Architectural Inputs

概念：B继承EA组织框架、已批准说明书、原则、连续体、库、愿景和草稿定义。

适用条件：需要开展详细业务开发。

逻辑关系：库提供可复用块和内外参考；愿景高层需求界定细化。

决策方法：确认授权范围与可复用资产。

制品及证据：已批准工作说明书、愿景/高层需求、库资产和草稿定义文档。

适用边界：可选业务场景和任何域的基线/目标草稿不能默改成强制已批准输入。

来源块：C220-web-2025:02-architecture-development-method:b00360, C220-web-2025:02-architecture-development-method:b00361

<details><summary>展开本节完整英文来源</summary>

4.2.3. Architectural Inputs

Organizational Model for Enterprise Architecture (see the TOGAF Standard — Architecture Content ), including: Scope of organizations impacted Maturity assessment, gaps, and resolution approach Roles and responsibilities for architecture team(s) Constraints on architecture work Budget requirements Governance and support strategy Tailored Architecture Framework (see the TOGAF Standard — Architecture Content ), including: Tailored architecture method Tailored architecture content (deliverables and artifacts) Configured and deployed tools Approved Statement of Architecture Work (see the TOGAF Standard — Architecture Content ) Architecture Principles (see the TOGAF Standard — Architecture Content ), including business principles, when pre-existing Enterprise Continuum (see the TOGAF Standard — Architecture Content ) Architecture Repository (see the TOGAF Standard — Architecture Content ), including: Re-usable building blocks Publicly available reference models Organization-specific reference models Organization standards Architecture Vision (see the TOGAF Standard — Architecture Content ), including: Problem description Objective of the Statement of Architecture Work Summary views Business Scenario (optional) Refined key high-level stakeholder requirements Draft Architecture Definition Document, which may include Baseline
and/or Target Architectures of any architecture domain

</details>

<a id="tag_04_03"></a>
## 4.3. Steps

概念：B新业务模型应详细定义，既有保留元素不足时补定义。

适用条件：按本轮范围开展九步业务开发。

逻辑关系：可依情境选择基线或目标先行；启动的活动在Finalize关闭，文档在Create/Update正式发布。

决策方法：选择先后顺序并确保收尾/发布。

制品及证据：九步工作结果、收尾与正式发布记录。

适用边界：顺序可调整不免除关闭活动和发布责任。

来源块：C220-web-2025:02-architecture-development-method:b00362, C220-web-2025:02-architecture-development-method:b00363, C220-web-2025:02-architecture-development-method:b00364, C220-web-2025:02-architecture-development-method:b00365, C220-web-2025:02-architecture-development-method:b00366, C220-web-2025:02-architecture-development-method:b00367, C220-web-2025:02-architecture-development-method:b00368

<details><summary>展开本节完整英文来源</summary>

4.3. Steps

The level of detail addressed in Phase B will depend on the scope and
goals of the overall architecture effort.

New models characterizing the needs of the business will need to be
defined in detail during Phase B. Existing business artifacts to be
carried over and supported in the target environment may already have
been adequately defined in previous architectural work; but, if not,
they too will need to be defined in Phase B.

The order of the steps in Phase B as well as the time at which they are
formally started and completed should be adapted to the situation at
hand, in accordance with the established Architecture Governance. In
particular, determine whether in this situation it is appropriate to
conduct Baseline or Target Architecture development first, as described
in the TOGAF Standard — Applying the ADM .

All activities that have been initiated in these steps should be closed
during the Finalize the Business Architecture step; see Section 4.3.8, “Finalize the Business Architecture” .
The documentation generated from these steps must be formally published in
the Create/Update the Architecture Definition Document step; see Section 4.3.9, “Create/Update the Architecture Definition Document” .

The steps in Phase B are as follows:

Select reference models, viewpoints, and tools; see Section 4.3.1, “Select Reference Models, Viewpoints, and Tools” Develop Baseline Business Architecture Description; see Section 4.3.2, “Develop Baseline Business Architecture Description” Develop Target Business Architecture Description; see Section 4.3.3, “Develop Target Business Architecture Description” Perform gap analysis; see Section 4.3.4, “Perform Gap Analysis” Define candidate roadmap components; see Section 4.3.5, “Define Candidate Roadmap Components” Resolve impacts across the Architecture Landscape; see Section 4.3.6, “Resolve Impacts Across the Architecture Landscape” Conduct formal stakeholder review; see Section 4.3.7, “Conduct Formal Stakeholder Review” Finalize the Business Architecture; see Section 4.3.8, “Finalize the Business Architecture” Create/Update the Architecture Definition Document; see Section 4.3.9, “Create/Update the Architecture Definition Document”

</details>

<a id="tag_04_03_01"></a>
## 4.3.1. Select Reference Models, Viewpoints, and Tools

概念：按业务驱动和相关方关切选业务参考、视点和工具。

适用条件：运营、管理、财务等关注不同。

逻辑关系：视点决定所需捕获模型分析；复杂程度可由普通文档到专业建模。

决策方法：选择能证明关切得到回答的视点/工具。

制品及证据：业务参考、视点、工具方法选择。

适用边界：视点名称不证明对应视图已形成。

来源块：C220-web-2025:02-architecture-development-method:b00369, C220-web-2025:02-architecture-development-method:b00370, C220-web-2025:02-architecture-development-method:b00371, C220-web-2025:02-architecture-development-method:b00372

<details><summary>展开本节完整英文来源</summary>

4.3.1. Select Reference Models, Viewpoints, and Tools

Select relevant Business Architecture resources (reference models,
patterns, etc.) from the Architecture Repository, on the basis of the
business drivers and stakeholder concerns.

Select relevant Business Architecture viewpoints (e.g., operations,
management, financial); i.e., those that will enable the architect to
demonstrate how the stakeholder concerns are being addressed in the
Business Architecture.

Identify appropriate tools and techniques to be used for capture,
modeling, and analysis, in association with the selected viewpoints.
Depending on the degree of sophistication warranted, these may comprise
simple documents or spreadsheets, or more sophisticated modeling tools
and techniques, such as activity models, business process models,
use-case models, etc.

</details>

<a id="tag_04_03_01_01"></a>
## 4.3.1.1. Determine Overall Modeling Process

概念：整体建模把战略评估转为能力、组织、价值流及信息/过程/用例模型。

适用条件：按视点形成具体业务视图。

逻辑关系：利用已有框架揭示差距并映射价值；未覆盖关切要增加或扩展模型，场景可迭代分解。

决策方法：按目标范围用途决定分解严谨程度。

制品及证据：所选模型、关切覆盖、能力/信息/组织/流程/用例/价值流映射。

适用边界：分解细节依企业与工作而异，不能强制一套全模型。

来源块：C220-web-2025:02-architecture-development-method:b00373, C220-web-2025:02-architecture-development-method:b00374, C220-web-2025:02-architecture-development-method:b00375, C220-web-2025:02-architecture-development-method:b00376, C220-web-2025:02-architecture-development-method:b00377, C220-web-2025:02-architecture-development-method:b00378

<details><summary>展开本节完整英文来源</summary>

4.3.1.1. Determine Overall Modeling Process

Business modeling and strategy assessments are effective techniques for
framing the target state of an organization’s Business Architecture; see Section 3.3.4, “Evaluate Capabilities” .
The output from that activity is then used to articulate the business
capabilities, organizational structure, and value streams required to
close gaps between the current and target state. As addressed in Section 3.5, “Approach” ,
the frameworks for these
maps may already exist and should be leveraged, now using them to
characterize gaps and better map business value to achieve the Target
Business Architecture.

For each viewpoint, select the models needed to support the specific
view required, using the selected tool or method.

Ensure that all stakeholder concerns are covered. If they are not,
create new models to address concerns not covered, or augment existing
models; see Section 4.5.7, “Applying Modeling Techniques” .
Business scenarios are a useful technique to discover and document
business requirements, and may be used iteratively, at different levels
of detail in the hierarchical decomposition of the Business
Architecture. Business scenarios are described in the TOGAF ® Series Guide: Business Scenarios .
The techniques described in Section 4.5, “Approach” can be utilized to progressively decompose a business:

Business Capability Mapping : identifies, categorizes, and decomposes
the business capabilities required for the business to have the ability
to deliver value to one or more stakeholders Information Mapping : collecting the information concepts and their
relationships that matter most to the business Organization Mapping : a representation of the organizational
structure of the business (including third-party domains), depicting
business units, the decomposition of those units into lower-level
functions, and organizational relationships (unit-to-unit and mapping to
business capabilities, locations, and other attributes) Process Modeling : the activity of articulating business processes of
an enterprise, to enable analysis and improvement Structured Analysis : identifies the key business capabilities within
the scope of the architecture, and maps those capabilities onto business
functions and organizational units within the business Use-case Analysis : a technique used to identify the requirements of
a system or task to be completed, from a user’s perspective Value Stream Mapping : the end-to-end breakdown of activities that an
organization performs to create the value being exchanged with
stakeholders Value stream maps illustrate how an organization delivers value and are
in the context of a specific set of stakeholders, and leverage business
capabilities in order to create stakeholder value and align to other
aspects of the Target Business Architecture.

The level and rigor of decomposition needed varies from enterprise to
enterprise, as well as within an enterprise, and the architect should
consider the enterprise’s goals, objectives, scope, and purpose of the
Enterprise Architecture effort to determine the level of decomposition.

</details>

<a id="tag_04_03_01_02"></a>
## 4.3.1.2. Identify Required Catalogs of Business Building Blocks

概念：业务目录是核心资产层次盘点，含构建块及跨块分解。

适用条件：需要矩阵视图和业务/IT能力管理基础。

逻辑关系：目录为矩阵与视图提供原材料，内容卷关联元模型。

决策方法：确定需要的业务块目录和分解关系。

制品及证据：业务目录与元模型实体属性关系。

适用边界：目录盘点不是关系矩阵，也不自动生成全部关系。

来源块：C220-web-2025:02-architecture-development-method:b00379, C220-web-2025:02-architecture-development-method:b00380, C220-web-2025:02-architecture-development-method:b00381, C220-web-2025:02-architecture-development-method:b00382

<details><summary>展开本节完整英文来源</summary>

4.3.1.2. Identify Required Catalogs of Business Building Blocks

Catalogs capture inventories of the core assets of the business.
Catalogs are hierarchical in nature and capture the decomposition of a
building block and also decompositions across related building blocks
(e.g., organization/actor).

Catalogs form the raw material for development of matrices and views and
also act as a key resource for managing the business and IT capability.

The TOGAF Standard — Architecture Content contains a detailed description of catalogs which
should be considered for development within a Business Architecture,
describing them in detail and relating them to entities, attributes, and
relationships in the TOGAF Enterprise Metamodel.

</details>

<a id="tag_04_03_01_03"></a>
## 4.3.1.3. Identify Required Matrices

概念：业务矩阵表达模型实体的核心关系。

适用条件：差距影响评估与视图开发。

逻辑关系：矩阵从目录关系支持影响评估，再构成视图原材料。

决策方法：选择为当前关切所需矩阵。

制品及证据：业务关系矩阵及实体依据。

适用边界：空格不能无依据视作不存在关系。

来源块：C220-web-2025:02-architecture-development-method:b00383, C220-web-2025:02-architecture-development-method:b00384, C220-web-2025:02-architecture-development-method:b00385, C220-web-2025:02-architecture-development-method:b00386

<details><summary>展开本节完整英文来源</summary>

4.3.1.3. Identify Required Matrices

Matrices show the core relationships between related model entities.

Matrices form the raw material for development of views and also act as
a key resource for impact assessment, carried out as a part of gap
analysis.

The TOGAF Standard — Architecture Content contains a detailed description of matrices which
should be considered for development within a Business Architecture,
describing them in detail and relating them to entities, attributes, and
relationships in the TOGAF Enterprise Metamodel.

</details>

<a id="tag_04_03_01_04"></a>
## 4.3.1.4. Identify Required Diagrams

概念：业务图按相关方要求提供不同视点的架构信息。

适用条件：需要沟通具体业务关切。

逻辑关系：图应对应视点和元模型实体属性关系。

决策方法：选择需形成的图与表达。

制品及证据：业务图及关切/视点关联。

适用边界：画图不自动证明模型完整或业务正确。

来源块：C220-web-2025:02-architecture-development-method:b00387, C220-web-2025:02-architecture-development-method:b00388, C220-web-2025:02-architecture-development-method:b00389

<details><summary>展开本节完整英文来源</summary>

4.3.1.4. Identify Required Diagrams

Diagrams present the Business Architecture information from a set of
different perspectives (viewpoints) according to the requirements of the
stakeholders.

The TOGAF Standard — Architecture Content contains a detailed description of diagrams which
should be considered for development within a Business Architecture,
describing them in detail and relating them to entities, attributes, and
relationships in the TOGAF Enterprise Metamodel.

</details>

<a id="tag_04_03_01_05"></a>
## 4.3.1.5. Identify Types of Requirement to be Collected

概念：业务模型完成后正式化目标实施所需业务聚焦要求。

适用条件：要求需传到数据应用技术或设计实施。

逻辑关系：要求可跨域传递，但说明书决定要求内容范围；超范围的新/变要求送受治理需求库。

决策方法：识别由架构满足的要求和应转交一般需求管理的细节。

制品及证据：业务要求、域传递、设计指导与需求库记录。

适用边界：定义文档通常不提供完整详细解决方案需求。

来源块：C220-web-2025:02-architecture-development-method:b00390, C220-web-2025:02-architecture-development-method:b00391, C220-web-2025:02-architecture-development-method:b00392, C220-web-2025:02-architecture-development-method:b00393, C220-web-2025:02-architecture-development-method:b00394, C220-web-2025:02-architecture-development-method:b00395, C220-web-2025:02-architecture-development-method:b00396

<details><summary>展开本节完整英文来源</summary>

4.3.1.5. Identify Types of Requirement to be Collected

Once the Business Architecture catalogs, matrices, and diagrams have
been developed, architecture modeling is completed by formalizing the
business-focused requirements for implementing the Target Architecture.

These requirements may:

Relate to the business domain Provide requirements input into the Data, Application, and Technology
Architectures Provide detailed guidance to be reflected during design and
implementation to ensure that the solution addresses the original
architecture requirements

Within this step, the architect should identify requirements that should
be met by the architecture; see Section 13.5.2, “Requirements Development” .

In many cases, the Architecture Definition will not be intended to give
detailed or comprehensive requirements for a solution (as these can be
better addressed through general requirements management discipline).
The expected scope of requirements content should be established during
the Architecture Vision phase and documented in the approved Statement
of Architecture Work.

Any requirement, or change in requirement, that is outside of the scope
defined in the Statement of Architecture Work must be submitted to the
Requirements Repository for management through the governed Requirements
Management process.

</details>

<a id="tag_04_03_02"></a>
## 4.3.2. Develop Baseline Business Architecture Description

概念：业务基线只深入到支持目标所需程度。

适用条件：现有业务元素将保留或已有描述可复用。

逻辑关系：细节按保留程度与已有描述决定；缺模型按所选视点新建。

决策方法：确定基线必须调查哪些业务块。

制品及证据：基线业务描述、块和新增模型。

适用边界：不能以目标假设替代现状事实。

来源块：C220-web-2025:02-architecture-development-method:b00397, C220-web-2025:02-architecture-development-method:b00398, C220-web-2025:02-architecture-development-method:b00399

<details><summary>展开本节完整英文来源</summary>

4.3.2. Develop Baseline Business Architecture Description

Develop a Baseline Description of the existing Business Architecture, to
the extent necessary to support the Target Business Architecture. The
scope and level of detail to be defined will depend on the extent to
which existing business elements are likely to be carried over into the
Target Business Architecture, and on whether Architecture Descriptions
exist, as described in Section 4.5, “Approach” .
To the extent possible, identify the relevant Business Architecture building blocks,
drawing on the Architecture Repository (see the TOGAF Standard — Architecture Content ).

Where new architecture models need to be developed to satisfy
stakeholder concerns, use the models identified within
the first step in this phase (see Section 4.3.1, “Select Reference Models, Viewpoints, and Tools” )
as a guideline for creating new architecture content to describe the Baseline
Architecture.

</details>

<a id="tag_04_03_03"></a>
## 4.3.3. Develop Target Business Architecture Description

概念：目标业务描述细节以支持愿景为准。

适用条件：业务元素影响实现目标愿景。

逻辑关系：优先库资产，缺模型则新建；适合时探索备选并与相关方讨论。

决策方法：选择目标业务块及候选取舍。

制品及证据：目标业务描述、块和备选。

适用边界：复用资产仍需证明对目标适用。

来源块：C220-web-2025:02-architecture-development-method:b00400, C220-web-2025:02-architecture-development-method:b00401, C220-web-2025:02-architecture-development-method:b00402, C220-web-2025:02-architecture-development-method:b00403

<details><summary>展开本节完整英文来源</summary>

4.3.3. Develop Target Business Architecture Description

Develop a Target Description for the Business Architecture, to the
extent necessary to support the Architecture Vision. The scope and level
of detail to be defined will depend on the relevance of the business
elements to attaining the Target Architecture Vision, and on whether
architectural descriptions exist. To the extent possible, identify the
relevant Business Architecture building blocks, drawing on the
Architecture Repository (see the TOGAF Standard — Architecture Content ).

Where new architecture models need to be developed to satisfy
stakeholder concerns, use the models identified within
the first step in this phase (see Section 4.3.1, “Select Reference Models, Viewpoints, and Tools” )
as a guideline for creating new architecture content to describe the Target
Architecture.

If appropriate, investigate different Target Architecture alternatives
and discuss these with stakeholders using the Architecture Alternatives
and Trade-offs technique (see the TOGAF Standard — ADM Techniques ).

</details>

<a id="tag_04_03_04"></a>
## 4.3.4. Perform Gap Analysis

概念：业务差距分析先核查模型一致性准确性与需求完整。

适用条件：基线和目标业务模型已形成。

逻辑关系：解决视图冲突、检验原则目标约束、记录参考视点修改，再识别基线目标差距。

决策方法：确认模型有效及应消除的差距。

制品及证据：取舍、模型检查、视点修改与业务差距。

适用边界：不应仅靠名称集合差集替代语义检验。

来源块：C220-web-2025:02-architecture-development-method:b00404, C220-web-2025:02-architecture-development-method:b00405, C220-web-2025:02-architecture-development-method:b00406, C220-web-2025:02-architecture-development-method:b00407

<details><summary>展开本节完整英文来源</summary>

4.3.4. Perform Gap Analysis

Verify the architecture models for internal consistency and accuracy:

Perform trade-off analysis to resolve conflicts (if any) among the
different views Validate that the models support the principles, objectives, and
constraints Note changes to the viewpoint represented in the selected models from
the Architecture Repository, and document Test architecture models for completeness against requirements

Identify gaps between the baseline and target, using the gap analysis
technique, as described in the TOGAF Standard — ADM Techniques .

</details>

<a id="tag_04_03_05"></a>
## 4.3.5. Define Candidate Roadmap Components

概念：初始业务路线图为后续活动排序并支撑E的跨域整合。

适用条件：业务基线目标差距已形成。

逻辑关系：业务候选组件是综合路线图原材料。

决策方法：确定初步优先活动。

制品及证据：业务路线图候选。

适用边界：局部业务排序不是最终跨域优先级。

来源块：C220-web-2025:02-architecture-development-method:b00408, C220-web-2025:02-architecture-development-method:b00409, C220-web-2025:02-architecture-development-method:b00410

<details><summary>展开本节完整英文来源</summary>

4.3.5. Define Candidate Roadmap Components

Following the creation of a Baseline Architecture, Target Architecture,
and gap analysis results, a business roadmap is required to prioritize
activities over the coming phases.

This initial Business Architecture Roadmap will be used as raw material
to support more detailed definition of a consolidated, cross-discipline
roadmap within the Opportunities & Solutions phase.

</details>

<a id="tag_04_03_06"></a>
## 4.3.6. Resolve Impacts Across the Architecture Landscape

概念：业务架构需检查整个景观的双向影响及复用机会。

适用条件：业务方案与既有/近期架构和项目并存。

逻辑关系：同时检查本架构影响其他资产/计划及其受其他架构/项目影响。

决策方法：识别并处理跨景观依赖。

制品及证据：影响分析、复用机会和项目关联。

适用边界：仅共享ID一致不足以证明业务影响被理解。

来源块：C220-web-2025:02-architecture-development-method:b00411, C220-web-2025:02-architecture-development-method:b00412, C220-web-2025:02-architecture-development-method:b00413

<details><summary>展开本节完整英文来源</summary>

4.3.6. Resolve Impacts Across the Architecture Landscape

Once the Business Architecture is finalized, it is necessary to
understand any wider impacts or implications. At this stage, other architecture artifacts in the Architecture
Landscape should be examined to identify:

Does this Business Architecture create an impact on any pre-existing
architectures? Have recent changes been made that impact on the Business
Architecture? Are there any opportunities to leverage work from this Business
Architecture in other areas of the organization? Does this Business Architecture impact other projects (those
planned as well as those in progress)? Will this Business Architecture be impacted by other projects
(those planned as well as those in progress)?

</details>

<a id="tag_04_03_07"></a>
## 4.3.7. Conduct Formal Stakeholder Review

概念：正式相关方复核以原动机和工作说明书检验业务方案用途。

适用条件：业务模型将支撑后续其他域。

逻辑关系：仅在需要时细化方案以适合后续工作。

决策方法：判断业务架构是否fit-for-purpose。

制品及证据：相关方复核、动机/范围核验和必要修订。

适用边界：技术校验不能代替相关方正式复核。

来源块：C220-web-2025:02-architecture-development-method:b00414, C220-web-2025:02-architecture-development-method:b00415

<details><summary>展开本节完整英文来源</summary>

4.3.7. Conduct Formal Stakeholder Review

Check the original motivation for the architecture project and the
Statement of Architecture Work against the proposed Business
Architecture, asking if it is fit for the purpose of supporting
subsequent work in the other architecture domains. Refine the proposed
Business Architecture only if necessary.

</details>

<a id="tag_04_03_08"></a>
## 4.3.8. Finalize the Business Architecture

概念：Finalize完成每个业务块标准描述、决策理由与最终追溯及工作产品。

适用条件：业务开发收尾。

逻辑关系：对业务目标总核验；找工作实践角色关系岗位等可复用块并经库发布。

决策方法：选择标准和可复用业务内容并关闭工作。

制品及证据：块说明/标准、最终需求追溯、库映射、决策理由和差距结果。

适用边界：发布复用仍受库和治理过程约束。

来源块：C220-web-2025:02-architecture-development-method:b00416, C220-web-2025:02-architecture-development-method:b00417

<details><summary>展开本节完整英文来源</summary>

4.3.8. Finalize the Business Architecture

Select standards for each of the building blocks, re-using as much as
possible from the reference models selected from the Architecture
Repository Fully document each building block Conduct a final cross-check of overall architecture against business
goals; document the rationale for building block decisions in the
architecture document Document the final requirements traceability report Document the final mapping of the architecture within the Architecture
Repository; from the selected building blocks, identify those that might
be re-used (working practices, roles, business relationships, job
descriptions, etc.), and publish via the Architecture Repository Finalize all the work products, such as gap analysis results

</details>

<a id="tag_04_03_09"></a>
## 4.3.9. Create/Update the Architecture Definition Document

概念：定义文档的业务部分按预定范围用途正式化。

适用条件：业务结果需发布并供相关方复核。

逻辑关系：记录块决策理由，可用工具图表展示关键视图，经复核纳入反馈。

决策方法：准备适当业务内容并决定反馈修订。

制品及证据：架构定义文档业务章节与复核反馈。

适用边界：自动生成报告不等于正式发布批准。

来源块：C220-web-2025:02-architecture-development-method:b00418, C220-web-2025:02-architecture-development-method:b00419, C220-web-2025:02-architecture-development-method:b00420

<details><summary>展开本节完整英文来源</summary>

4.3.9. Create/Update the Architecture Definition Document

Document the rationale for building block decisions in the
Architecture Definition Document Prepare the appropriate business sections of the Architecture
Definition Document related to the intended scope and use of the
architecture

If appropriate, use reports and/or graphics generated by modeling tools
to demonstrate key views of the architecture. Route the document for
review by relevant stakeholders, and incorporate feedback.

</details>

<a id="tag_04_04"></a>
## 4.4. Outputs

概念：B输出使目标业务内容获批而整份定义文档仍可为草稿。

适用条件：交付业务阶段结果。

逻辑关系：目标包括组织地点目标功能能力服务产品流程角色技能数据及关系视图；要求规格草稿含差距、跨域技术要求和更新业务需求。

决策方法：准确标示基线按适合情况批准、目标批准和整体文档草稿。

制品及证据：业务定义/要求、业务路线图及必要A输出更新。

适用边界：已批准目标不等于整个跨域定义文档最终完成。

来源块：C220-web-2025:02-architecture-development-method:b00421, C220-web-2025:02-architecture-development-method:b00422, C220-web-2025:02-architecture-development-method:b00423, C220-web-2025:02-architecture-development-method:b00424

<details><summary>展开本节完整英文来源</summary>

4.4. Outputs

The outputs of Phase B may include, but are not restricted to:

Refined and updated versions of the Architecture Vision phase
deliverables, where applicable, including: Statement of Architecture Work (see the TOGAF Standard — Architecture Content ), updated if necessary Validated business principles, business goals, and business drivers
(see the TOGAF Standard — Architecture Content ), updated if necessary Architecture Principles (see the TOGAF Standard — Architecture Content ) Draft Architecture Definition Document (see the TOGAF Standard — Architecture Content ), including: Baseline Business Architecture, Approved, if appropriate Target Business Architecture, Approved, including: Organization structure — identifying business locations and relating
them to organizational units Business goals and objectives — for the enterprise and each
organizational unit Business functions — a detailed, recursive step involving successive
decomposition of major functional areas into sub-functions Business capabilities — the abilities that a business needs to
possess or exchange to achieve its goals and objectives Business services — the services that support the business by
encapsulating a unique “elements of business behavior”; a service
offered external to the enterprise may be supported by business services Products — output generated by the business to be offered to
customers; products include materials and/or services Business processes, including measures and deliverables Business roles, including development and modification of skills
requirements Business data model Correlation of organization/business functions and business
capabilities — relate business capabilities to organizational units in
the form of a matrix report Views corresponding to the selected viewpoints addressing key
stakeholder concerns Draft Architecture Requirements Specification (see the TOGAF Standard — Architecture Content ), including such Business Architecture requirements as: Gap analysis results Technical requirements — identifying, categorizing, and prioritizing
the implications for work in the remaining architecture domains; for
example, by a dependency/priority matrix (e.g., guiding trade-off
between speed of transaction processing and security); list the specific
models that are expected to be produced (for example, expressed as
primitives of the Zachman Framework) Updated business requirements Business Architecture components of an Architecture Roadmap (see the TOGAF Standard — Architecture Content )

The TOGAF Standard — Architecture Content contains a detailed description of architectural
artifacts which might be produced in this phase.

</details>

<a id="tag_04_05"></a>
## 4.5. Approach

概念：业务架构以能力、端到端价值、信息、组织及其策略产品政策等关系形成多维整体。

适用条件：业务视图需与目标及其他域相联。

逻辑关系：单一视图只能覆盖部分业务，应关联各维。

决策方法：确定业务元素与目标/他域关系。

制品及证据：多维业务视图与关系。

适用边界：业务架构不是仅组织结构或流程图。

来源块：C220-web-2025:02-architecture-development-method:b00425, C220-web-2025:02-architecture-development-method:b00426, C220-web-2025:02-architecture-development-method:b00427

<details><summary>展开本节完整英文来源</summary>

4.5. Approach

Business Architecture is a representation of holistic, multi-dimensional
business views of capabilities, end-to-end value delivery, information,
and organizational structure; and the relationships among these business
views and strategies, products, policies, initiatives, and stakeholders.

Business Architecture relates business elements to business goals and
elements of other domains.

</details>

<a id="tag_04_05_01"></a>
## 4.5.1. General

概念：业务理解是他域前提，可由已有组织流程满足。

适用条件：B范围由A愿景确定且资料成熟度不同。

逻辑关系：策略讲目标指标，B讲如何实现；优先核实复用已有战略描述，缺失时研究验证并获认同。

决策方法：按当前决策范围收集信息，新业务流程则更深入。

制品及证据：业务理解、战略桥接、场景/要求与更新描述。

适用边界：不做冗余业务模型不等于可跳过业务理解。

来源块：C220-web-2025:02-architecture-development-method:b00428, C220-web-2025:02-architecture-development-method:b00429, C220-web-2025:02-architecture-development-method:b00430, C220-web-2025:02-architecture-development-method:b00431, C220-web-2025:02-architecture-development-method:b00432, C220-web-2025:02-architecture-development-method:b00433, C220-web-2025:02-architecture-development-method:b00434, C220-web-2025:02-architecture-development-method:b00435, C220-web-2025:02-architecture-development-method:b00436, C220-web-2025:02-architecture-development-method:b00437

<details><summary>展开本节完整英文来源</summary>

4.5.1. General

A knowledge of the Business Architecture is a prerequisite for
architecture work in any other domain (Data, Application, Technology),
and is therefore the first architecture activity that needs to be
undertaken, if not catered for already in other organizational processes
(enterprise planning, strategic business planning, business process
re-engineering, etc.).

In practical terms, the Business Architecture is also often necessary as
a means of demonstrating the business value of subsequent architecture
work to key stakeholders, and the return on investment to those
stakeholders from supporting and participating in the subsequent work.

The scope of work in Phase B is primarily determined by the Architecture
Vision as set out in Phase A. The business strategy defines the goals
and drivers and the metrics for success, but not necessarily how to get
there. That is the role of the Business Architecture, defined in detail
in Phase B.

This will depend to a large extent on the enterprise environment. In
some cases, key elements of the Business Architecture may be done in
other activities; for example, the enterprise mission, vision, strategy,
and goals may be documented as part of some wider business strategy or
enterprise planning activity that has its own lifecycle within the
enterprise.

In such cases, there may be a need to verify and update the currently
documented business strategy and plans, and/or to bridge between
high-level business drivers, business strategy, and goals on the one
hand, and the specific business requirements that are relevant to this
architecture development effort.

In other cases, little or no Business Architecture work may have been
done to date. In such cases, there will be a need for the architecture
team to research, verify, and gain buy-in to the key business objectives
and processes that the architecture is to support. This may be done as a
free-standing exercise, either preceding architecture development, or as
part of Phase A.

In both of these cases, the business scenarios technique (see the TOGAF ® Series Guide: Business Scenarios ), or any other method that illuminates the
key business requirements and indicates the implied technical
requirements for IT architecture, may be used.

A key objective is to re-use existing material as much as possible. In
architecturally more mature environments, there will be existing
Architecture Definitions, which (hopefully) will have been maintained
since the last architecture development cycle. Where Architecture
Descriptions exist, these can be used as a starting point, and verified
and updated if necessary; see the TOGAF Standard — Architecture Content .

Gather and analyze only that information that allows informed decisions
to be made relevant to the scope of this architecture effort. If this
effort is focused on the definition of (possibly new) business
processes, then Phase B will necessarily involve a lot of detailed work.
If the focus is more on the Target Architectures in other domains
(data/information, application systems, infrastructure) to support an
essentially existing Business Architecture, then it is important to
build a complete picture in Phase B without going into unnecessary
detail.

</details>

<a id="tag_04_05_02"></a>
## 4.5.2. Developing the Baseline Description

概念：已有能力图价值流等可足够作基线，未必需修改公共框架。

适用条件：当前任务只是对企业视图使用方式或重点改变。

逻辑关系：区分业务基本视图变化与因项目范围优先关系变化而运用已有视图。

决策方法：识别新增能力/价值流/组织变化是否需更新基线。

制品及证据：核实或新增的基线模型及变化分类。

适用边界：应用共同能力图不应无依据改变能力身份。

来源块：C220-web-2025:02-architecture-development-method:b00438, C220-web-2025:02-architecture-development-method:b00439, C220-web-2025:02-architecture-development-method:b00440, C220-web-2025:02-architecture-development-method:b00441, C220-web-2025:02-architecture-development-method:b00442

<details><summary>展开本节完整英文来源</summary>

4.5.2. Developing the Baseline Description

If an enterprise has existing Architecture Descriptions, they should be
used as the basis for the Baseline Description. This input may have been
used already in Phase A in developing the Architecture Vision, such as
the business capability map or a core set of value streams as introduced
in Section 3.5.2, “Creating the Architecture Vision” ,
and may be sufficient in itself for this baseline.

The reasons to update these materials include having a missing business
capability, a new value stream, or changed organizational unit that has
not previously been assessed within the scope of the Enterprise
Architecture project. Section 4.5.3, “Applying Business Capabilities” ,
through Section 4.5.6, “Applying Information Maps” ,
address the use of core Business Architecture methods to model the Business Architecture driven by the strategy scope from Phase A. Note
that putting these methods into action to drive a focus and target state
for later architecture work does not mean that the fundamental
frameworks from Phase A, such as a common enterprise business capability
map, will necessarily change but rather that they are applied in a
manner driven by the scope and needs of the specific Enterprise
Architecture project.

If no Architecture Descriptions exist, information should be gathered
and Business Architecture models developed.

Whatever the scope of the specific project, it is important to determine
whether it is the fundamental view of the business that is changing or
the usage of those views to determine scope, priorities, and
relationships for the specific project in relation to the rest of the
enterprise.

</details>

<a id="tag_04_05_03"></a>
## 4.5.3. Applying Business Capabilities

概念：能力图独立于当前组织流程应用产品组合，需映回组织价值流系统战略。

适用条件：评估当前项目能力差距与价值。

逻辑关系：关系映射分析对齐；热图可按成熟度有效性性能价值成本显示同一能力集。

决策方法：选择热图指标和业务情境下目标差距。

制品及证据：能力关系映射、指标/图例与热图。

适用边界：绿黄红紫是源例，紫含缺能力或过度投入等不同解释，必须定义图例，不能自动评级。

来源块：C220-web-2025:02-architecture-development-method:b00443, C220-web-2025:02-architecture-development-method:b00444, C220-web-2025:02-architecture-development-method:b00445, C220-web-2025:02-architecture-development-method:b00446

<details><summary>展开本节完整英文来源</summary>

4.5.3. Applying Business Capabilities

The business capability map found or developed in the Architecture
Vision phase provides a self-contained view of the business that is
independent of the current organizational structure, business processes,
information systems and applications, and the rest of the product or
service portfolio. Those business capabilities should be mapped back to
the organizational units, value streams, information systems, and
strategic plans within the scope of the Enterprise Architecture project.
This relationship mapping provides greater insight into the alignment
and optimization of each of those domains (see Relationship Mapping in TOGAF ® Series Guide: Business Capabilities ).

Another common analysis technique involves heat mapping, which can be
used to show a range of different perspectives on the same set of core
business capabilities. These include maturity, effectiveness,
performance, and the value or cost of each capability to the business.
Different attributes determine the colors of each capability on the
business capability map (see Heat Mapping in TOGAF ® Series Guide: Business Capabilities ).

For example, a business capability maturity heat map shows the desired
maturity as green for a specific capability, one level down as yellow,
and two or more levels down as red. Other colors may indicate status,
such as purple denoting a capability that does not exist yet in the
company but is desired, or perhaps as a capability that is over-funded
and has more resources than necessary. This gap analysis is directly
tied to the Enterprise Architecture project underway; a gap is only
relevant in the context of the business need and provides focus for more
mapping in this phase or priorities for later architecture phases.

</details>

<a id="tag_04_05_04"></a>
## 4.5.4. Applying Value Streams

概念：价值流说明为何需能力，能力说明价值阶段需具备什么。

适用条件：按具体相关方价值分析当前项目。

逻辑关系：复用A价值流，范围扩大会需新增；阶段能力映射加差距分析产生主要利益。

决策方法：选择聚焦相关方、价值元素或阶段及适用新流。

制品及证据：价值流/阶段、用例或热图、阶段能力映射。

适用边界：价值阶段能力关系不等于流程步骤或组织顺序。

来源块：C220-web-2025:02-architecture-development-method:b00447, C220-web-2025:02-architecture-development-method:b00448, C220-web-2025:02-architecture-development-method:b00449, C220-web-2025:02-architecture-development-method:b00450, C220-web-2025:02-architecture-development-method:b00451

<details><summary>展开本节完整英文来源</summary>

4.5.4. Applying Value Streams

Value streams provide valuable stakeholder context into why the
organization needs business capabilities, while business capabilities
provide what the organization needs for a particular value stage to be
successful.

Start with the initial set of value stream models for the business
documented in the Architecture Vision phase. Within the scope of the
specific Enterprise Architecture project, if sufficiently larger in
breadth, there may be a need for new value streams not already in the
repository.

A new or existing value stream can be analyzed within the scope of the
project through heat mapping (by value stream stage) or by developing
use-cases around a complete definition of the value stream (see Baseline
Example in the TOGAF ® Series Guide: Value Streams ). A project might focus on specific
stakeholders, one element of business value, or stress some stages over
others to develop better requirements for solutions in later phases.

The most substantive benefits come from mapping relationships between
the stages in a value stream to business capabilities, then performing a
gap analysis for capabilities (such as heat mapping) in the context of
the business value achieved by the value stream for a specific
stakeholder (see Mapping Value Streams to Business Capabilities in the TOGAF ® Series Guide: Value Streams ).

</details>

<a id="tag_04_05_05"></a>
## 4.5.5. Applying the Organization Map

概念：组织图表达单位、伙伴、相关方工作网络，区别于汇报图。

适用条件：识别谁拥有/使用能力、谁参与价值流。

逻辑关系：组织范围依本轮边界，可含第三方；结合能力价值流决定谁何时讨论要求和影响测量。

决策方法：确认受影响单位及工作关系。

制品及证据：组织映射、能力归属/使用与价值流参与。

适用边界：网络线条不能默认有方向或汇报权。

来源块：C220-web-2025:02-architecture-development-method:b00452, C220-web-2025:02-architecture-development-method:b00453, C220-web-2025:02-architecture-development-method:b00454, C220-web-2025:02-architecture-development-method:b00455, C220-web-2025:02-architecture-development-method:b00456, C220-web-2025:02-architecture-development-method:b00457

<details><summary>展开本节完整英文来源</summary>

4.5.5. Applying the Organization Map

An organization map shows the key organizational units, partners, and
stakeholder groups that make up the enterprise ecosystem. The map should
also depict the working relationship between those entities, as distinct
from an organizational chart that only shows hierarchical reporting
relationships. The map is typically depicted as a network or web of
relationships and interactions between the various business entities
(see Organigraphs: Drawing How Companies Really Work , by Mintzberg and
Van der Heyden, 1999).

The business unit is the main concept used to establish organization
maps. In keeping with the relatively unconstrained view of what
constitutes as enterprise, the enterprise may be one business unit for
the project underway, may include all business units, or also include
third parties or other stakeholder groups. The interpretation depends on
the scope of the architecture effort.

This map is a key element of Business Architecture because it provides
the organizational context for the whole Enterprise Architecture effort.
While capability mapping exposes what a business does and value stream
mapping exposes how it delivers value to specific stakeholders, the
organization map identities the business units or third parties that
possess or use those capabilities and which participate in the value
streams.

Taken together with the methods in Section 4.5.3, “Applying Business Capabilities” , Section 4.5.4, “Applying Value Streams” ,
and the associated Guides, the organization map provides an
understanding of which business units to involve in the architecture
effort, who and when to talk about a given requirement, and how to
measure the impact of various decisions.

For further guidance on organization maps, see the TOGAF ® Series Guide: Organization Mapping .

</details>

<a id="tag_04_05_06"></a>
## 4.5.6. Applying Information Maps

概念：信息映射从业务最重要的概念和术语开始。

适用条件：在详细数据类型前理解信息价值。

逻辑关系：跨专业团队按逻辑类别形成信息域及域关系，再以信息/能力矩阵支撑后续数据应用基础设施。

决策方法：选择核心业务信息域和能力关联。

制品及证据：信息图、域关系与信息能力矩阵。

适用边界：业务信息概念不等同物理数据表字段。

来源块：C220-web-2025:02-architecture-development-method:b00458, C220-web-2025:02-architecture-development-method:b00459, C220-web-2025:02-architecture-development-method:b00460, C220-web-2025:02-architecture-development-method:b00461

<details><summary>展开本节完整英文来源</summary>

4.5.6. Applying Information Maps

Characterizing information in the Business Architecture phase starts
with the elements that matter most to the business, such as product,
customer, factory, etc. With a list of these key elements, a
cross-discipline team can list and map the information that matters most
and how it is described using business terms. Domains of information can
be derived from groupings or categories that the business terms fall
into logically. These domains are a good place to start the information
map for completeness and highest value before proceeding later to the
details of data types.

Relationships among the information domains can then be added to the map
as the next level of understanding for a good baseline information map.
The most significant benefit then comes with building matrices between
information and business capabilities. The linkage between the
information that matters most to the business and the business
capabilities that describe the ability to apply that information to
create value is a key aspect of Business Architecture. These information
maps and relationships to business capabilities will then apply in later
architecture phases on data characterization, applications, and
infrastructure.

For further guidance on information maps, see the TOGAF ® Series Guide: Information Mapping .

</details>

<a id="tag_04_05_07"></a>
## 4.5.7. Applying Modeling Techniques

概念：活动、用例、逻辑数据/类模型把业务映射扩展为运作实践。

适用条件：需更具体分析业务流程或规则。

逻辑关系：活动含ICOM和规则；用例含参与者与规格；逻辑数据含实体属性值关系，类模型再加方法。

决策方法：依问题选择适当模型/行业技术和继承关系。

制品及证据：活动ICOM/规则、用例、逻辑数据或UML类图。

适用边界：is-a继承区别于包含/关联；图4-2为示例不构成领域事实。

来源块：C220-web-2025:02-architecture-development-method:b00462, C220-web-2025:02-architecture-development-method:b00463, C220-web-2025:02-architecture-development-method:b00464, C220-web-2025:02-architecture-development-method:b00465, C220-web-2025:02-architecture-development-method:b00466, C220-web-2025:02-architecture-development-method:b00467, C220-web-2025:02-architecture-development-method:b00468, C220-web-2025:02-architecture-development-method:b00469

<details><summary>展开本节完整英文来源</summary>

4.5.7. Applying Modeling Techniques

The modeling and mapping techniques provided here are extensions that
implement the business capabilities, value streams, and organization
maps described above in Phase B into the practices of the business. They
expand the operating model, which is a representation for how an
organization operates across a range of domains in order to accomplish
its purpose (see A Method for Identifying Process Re-Use Opportunities
to Enhance the Operating Model, M. de Vries et al. ).

In addition to the techniques described above (capability maps, value
streams, and organization maps), a variety of other modeling techniques
may be employed, if deemed appropriate. For example:

Activity Models (also called Business Process Models ) describe the
enterprise’s business activities, the data and/or information exchanged
between activities (internal exchanges), and the data and/or information
exchanged with other activities that are outside the scope of the model
(external exchanges) Activity models are hierarchical in nature. They capture the activities
performed in a business process, and the Inputs, Controls, Outputs, and
Mechanisms/Resources (ICOMs) of those activities. Activity models can be
annotated with explicit statements of business rules, which represent
relationships among the ICOMs. For example, a business rule can specify
who can do what under specified conditions, the combination of inputs
and controls needed, and the resulting outputs. One technique for
creating activity models is the Integrated Computer Aided Manufacturing
(ICAM) DEFinition (IDEF) modeling technique. The Object Management Group (OMG) has developed the Business Process
Model and Notation TM (BPMN TM ), a standard for business process
modeling that includes a language with which to specify business
processes, their tasks/steps, and the documents produced. Use-Case Models describe the business process of an enterprise in
terms of use-cases and actors corresponding to business processes and
organizational participants (people, organizations, etc.) The use-case model is described in use-case diagrams and use-case
specifications. Logical Data Model (or Class Model ) Logical data models describe the entities, their attributes, and the
acceptable values for these attributes as well as the relationships
between the various entities. Particularly useful is the “is-a”
relationship for analyses. For example, if a sedan is a type of car
which is a type of vehicle, then a general business rule for all
vehicles can be written once and automatically picked up for all types
of cars and trucks. A class model expands the logical data model to include behaviors by
including services (methods) unique to the entity (now called a class).
Normally applications and information architects will use the class
diagram, and Business Architects will use the logical data model.



Figure 4-2: UML Business Class Diagram

All three types of model above can be represented in the Unified
Modeling Language™ (UML ® ), and a variety of tools exist for
generating such models.

Certain industry sectors have modeling techniques specific to the sector
concerned.

</details>

<a id="tag_04_05_08"></a>
## 4.5.8. Architecture Repository

概念：B库资源包括行业参考、企业业务视图、业务块和适用标准。

适用条件：业务建模准备复用。

逻辑关系：过程规则岗位描述等块与能力价值流组织图不同但均可相关。

决策方法：筛选适用且当前的参考与块。

制品及证据：所选业务参考/视图/块/标准。

适用边界：库中存在不等于当前业务适配和批准。

来源块：C220-web-2025:02-architecture-development-method:b00470, C220-web-2025:02-architecture-development-method:b00471, C220-web-2025:02-architecture-development-method:b00472

<details><summary>展开本节完整英文来源</summary>

4.5.8. Architecture Repository

As part of Phase B, the architecture team will need to consider what
relevant Business Architecture resources are available from the
Architecture Repository (see the TOGAF Standard — Architecture Content ), in particular:

Industry reference models relevant to the organization’s industry
sector Enterprise-specific Business Architecture views (capability maps,
value stream maps, organization maps, etc.) Enterprise-specific building blocks (process components, business
rules, job descriptions, etc.) Applicable standards

</details>

<a id="chap05"></a>
## 5. Phase C: Information Systems Architectures

概念：C包含数据和应用架构的开发。

适用条件：业务架构需要信息系统支持。

逻辑关系：本章导入双域，再分别在6、7章展开。

决策方法：确定C需哪些数据/应用工作。

制品及证据：信息系统阶段图和双域工作范围。

适用边界：两章分开不代表可忽略彼此依赖。

来源块：C220-web-2025:02-architecture-development-method:b00473, C220-web-2025:02-architecture-development-method:b00474, C220-web-2025:02-architecture-development-method:b00475, C220-web-2025:02-architecture-development-method:b00476

<details><summary>展开本节完整英文来源</summary>

5. Phase C: Information Systems Architectures

This chapter describes the Information Systems Architectures for an
architecture project, including the development of Data and Application
Architectures.



Figure 5-1: Phase C: Information Systems

</details>

<a id="tag_05_01"></a>
## 5.1. Objectives

概念：C目标信息系统使业务架构和愿景得到支撑。

适用条件：满足工作说明书与相关方关切。

逻辑关系：基线目标数据/应用差距产生路线图候选。

决策方法：验证双域对业务支持及差距。

制品及证据：目标信息系统架构和候选组件。

适用边界：不是仅IT软件清单。

来源块：C220-web-2025:02-architecture-development-method:b00477, C220-web-2025:02-architecture-development-method:b00478, C220-web-2025:02-architecture-development-method:b00479

<details><summary>展开本节完整英文来源</summary>

5.1. Objectives

The objectives of Phase C are to:

Develop the Target Information Systems Architectures, describing how
the enterprise’s Information Systems Architecture will enable the
Business Architecture and the Architecture Vision, in a way that
addresses the Statement of Architecture Work and stakeholder concerns Identify candidate Architecture Roadmap components based upon gaps
between the Baseline and Target Information Systems (Data and
Application) Architectures

</details>

<a id="tag_05_02"></a>
## 5.2. Approach

概念：C可按数据优先或应用优先任一顺序开展。

适用条件：数据驱动规划或ERP/CRM核心应用驱动等情况。

逻辑关系：大型应用含基础设施和业务逻辑，应用实现集成可成主要焦点。

决策方法：依任务确定双域顺序与集成重点。

制品及证据：数据/应用开发顺序和接口依赖。

适用边界：数据优先是某方法例子，不是TOGAF唯一顺序。

来源块：C220-web-2025:02-architecture-development-method:b00480, C220-web-2025:02-architecture-development-method:b00481, C220-web-2025:02-architecture-development-method:b00482, C220-web-2025:02-architecture-development-method:b00483, C220-web-2025:02-architecture-development-method:b00484

<details><summary>展开本节完整英文来源</summary>

5.2. Approach

Phase C involves some combination of Data and Application Architecture,
in either order. Advocates exist for both sequences. For example, Steven
Spewak’s Enterprise Architecture Planning (EAP) recommends a
data-driven approach.

On the other hand, major applications systems — such as those for
Enterprise Resource Planning (ERP), Customer Relationship Management
(CRM), etc. — often provide a combination of technology infrastructure
and business application logic. Some organizations take an
application-driven approach, whereby they recognize certain key
applications as forming the core underpinning of the mission-critical
business processes, and take the implementation and integration of those
core applications as the primary focus of their architecture effort (the
integration issues often constituting a major challenge).

Detailed descriptions for Phase C are given separately for each
architecture domain:

Phase C: Information Systems Architectures — Data Architecture; see Chapter 6, Phase C: Information Systems Architectures — Data Architecture Phase C: Information Systems Architectures — Application Architecture; see Chapter 7, Phase C: Information Systems Architectures — Application Architecture

</details>

<a id="chap06"></a>
## 6. Phase C: Information Systems Architectures — Data Architecture

概念：本章开发数据架构。

适用条件：需要数据域支撑愿景及业务时。

逻辑关系：数据描述与其他域共同形成信息系统或技术架构。

决策方法：确定本轮数据工作边界。

制品及证据：数据基线/目标与工作结果。

适用边界：域开发不能脱离已批准工作范围。

来源块：C220-web-2025:02-architecture-development-method:b00485, C220-web-2025:02-architecture-development-method:b00486

<details><summary>展开本节完整英文来源</summary>

6. Phase C: Information Systems Architectures — Data Architecture

This chapter describes the Data Architecture part of Phase C.

</details>

<a id="tag_06_01"></a>
## 6.1. Objectives

概念：目标数据架构支撑业务架构和愿景，基线目标差距产生路线图候选。

适用条件：工作说明书和相关方关切确定后。

逻辑关系：数据变更须连接业务支持和价值。

决策方法：核验目标数据满足愿景/工作关切。

制品及证据：目标数据架构与候选组件。

适用边界：候选组件不等于已批准跨域实施计划。

来源块：C220-web-2025:02-architecture-development-method:b00487, C220-web-2025:02-architecture-development-method:b00488, C220-web-2025:02-architecture-development-method:b00489

<details><summary>展开本节完整英文来源</summary>

6.1. Objectives

The objectives of the Data Architecture part of Phase C are to:

Develop the Target Data Architecture that enables the Business Architecture and the Architecture Vision, in a way that addresses the Statement of Architecture Work and stakeholder concerns Identify candidate Architecture Roadmap components based upon gaps between the Baseline and Target Data Architectures

</details>

<a id="tag_06_02"></a>
## 6.2. Inputs

概念：数据输入按外部、非架构和架构资料分类。

适用条件：启动数据开发时。

逻辑关系：6.2.1—6.2.3给出三类具体输入。

决策方法：确认各类资料及状态。

制品及证据：数据输入来源与状态清单。

适用边界：导航不证明输入完整。

来源块：C220-web-2025:02-architecture-development-method:b00490, C220-web-2025:02-architecture-development-method:b00491

<details><summary>展开本节完整英文来源</summary>

6.2. Inputs

This section defines the inputs to Phase C (Data Architecture).

</details>

<a id="tag_06_02_01"></a>
## 6.2.1. Reference Materials External to the Enterprise

概念：数据外部参考包括架构参考及客户主数据、商业智能分析、元数据管理系列指南。

适用条件：选择数据参考时。

逻辑关系：参考为模式与约束信息来源，仍需按业务需求评估。

决策方法：判断外部资源适用性。

制品及证据：架构参考及客户主数据、商业智能分析、元数据管理系列指南及出处。

适用边界：外部内容不自动成为当前目标架构。

来源块：C220-web-2025:02-architecture-development-method:b00492, C220-web-2025:02-architecture-development-method:b00493

<details><summary>展开本节完整英文来源</summary>

6.2.1. Reference Materials External to the Enterprise

Architecture reference materials (see the TOGAF Standard — Architecture Content ) TOGAF ® Series Guide: Information Architecture — Customer Master Data Management TOGAF ® Series Guide: Information Architecture: Business Intelligence & Analytics and Metadata Management Reference Models

</details>

<a id="tag_06_02_02"></a>
## 6.2.2. Non-Architectural Inputs

概念：数据非架构输入为工作请求、能力评估和沟通计划。

适用条件：安排数据工作与参与条件。

逻辑关系：业务任务、能力和沟通影响域分析。

决策方法：确认任务与人员参与及能力条件。

制品及证据：工作请求、能力评估、沟通计划。

适用边界：已识别能力缺口持续保留，不能默认消除。

来源块：C220-web-2025:02-architecture-development-method:b00494, C220-web-2025:02-architecture-development-method:b00495

<details><summary>展开本节完整英文来源</summary>

6.2.2. Non-Architectural Inputs

Request for Architecture Work (see the TOGAF Standard — Architecture Content ) Capability Assessment (see the TOGAF Standard — Architecture Content ) Communications Plan (see the TOGAF Standard — Architecture Content )

</details>

<a id="tag_06_02_03"></a>
## 6.2.3. Architectural Inputs

概念：数据架构输入继承组织模型、裁剪框架、说明书愿景、库、现有数据原则（如有）。

适用条件：开展数据域细化。

逻辑关系：B差距与本阶段技术要求、业务路线图，尤其当前数据定义

决策方法：检查上游要求、已有块与路线图是否适用且当前。

制品及证据：B差距与本阶段技术要求、业务路线图，尤其当前数据定义及草稿定义/要求文档。

适用边界：if existing/if available保留条件性，不能伪造缺失输入。

来源块：C220-web-2025:02-architecture-development-method:b00496, C220-web-2025:02-architecture-development-method:b00497

<details><summary>展开本节完整英文来源</summary>

6.2.3. Architectural Inputs

Organizational Model for Enterprise Architecture (see the TOGAF Standard — Architecture Content ), including: Scope of organizations impacted Maturity assessment, gaps, and resolution approach Roles and responsibilities for architecture team(s) Constraints on architecture work Budget requirements Governance and support strategy Tailored Architecture Framework (see the TOGAF Standard — Architecture Content ), including: Tailored architecture method Tailored architecture content (deliverables and artifacts) Configured and deployed tools Data principles (see the TOGAF Standard — ADM Techniques ), if existing Statement of Architecture Work (see the TOGAF Standard — Architecture Content ) Architecture Vision (see the TOGAF Standard — Architecture Content ) Architecture Repository (see the TOGAF Standard — Architecture Content ), including: Re-usable building blocks (in particular, definitions of current data) Publicly available reference models Organization-specific reference models Organization standards Draft Architecture Definition Document, which may include Baseline
and/or Target Architectures of any architecture domain Draft Architecture Requirements Specification (see the TOGAF Standard — Architecture Content ), including: Gap analysis results (from Business Architecture) Relevant technical requirements that will apply to this phase Business Architecture components of an Architecture Roadmap (see the TOGAF Standard — Architecture Content )

</details>

<a id="tag_06_03"></a>
## 6.3. Steps

概念：数据开发九步以总体范围目标确定细节。

适用条件：新数据块或已有块需支持目标时。

逻辑关系：新数据块详细定义；已有保留数据块若定义不足也需补定义；基线/目标可先行任一，启动活动在6.3.8关闭，文档在6.3.9正式发布。

决策方法：按治理调整顺序、起止和所需深度。

制品及证据：数据开发步骤、收尾和发布记录。

适用边界：可迭代不免除收尾和正式发布要求。

来源块：C220-web-2025:02-architecture-development-method:b00498, C220-web-2025:02-architecture-development-method:b00499, C220-web-2025:02-architecture-development-method:b00500, C220-web-2025:02-architecture-development-method:b00501, C220-web-2025:02-architecture-development-method:b00502, C220-web-2025:02-architecture-development-method:b00503, C220-web-2025:02-architecture-development-method:b00504

<details><summary>展开本节完整英文来源</summary>

6.3. Steps

The level of detail addressed in Phase C will depend on the scope and
goals of the overall architecture effort.

New data building blocks being introduced as part of this effort will
need to be defined in detail during Phase C. Existing data building
blocks to be carried over and supported in the target environment may
already have been adequately defined in previous architectural work;
but, if not, they too will need to be defined in Phase C.

The order of the steps in this phase as well as the time at which they
are formally started and completed should be adapted to the situation at
hand in accordance with the established Architecture Governance. In
particular, determine whether in this situation it is appropriate to
conduct Baseline Description or Target Architecture development first,
as described in the TOGAF Standard — Applying the ADM .

All activities that have been initiated in these steps should be closed during the Finalize the Data Architecture step; see Section 6.3.8, “Finalize the Data Architecture” .
The documentation generated from these steps must be formally published in the Create/Update the Architecture Definition Document step; see Section 6.3.9, “Create/Update the Architecture Definition Document” .

The steps in Phase C (Data Architecture) are as follows:

Select reference models, viewpoints, and tools; see Section 6.3.1, “Select Reference Models, Viewpoints, and Tools” Develop Baseline Data Architecture Description; see Section 6.3.2, “Develop Baseline Data Architecture Description” Develop Target Data Architecture Description; see Section 6.3.3, “Develop Target Data Architecture Description” Perform gap analysis; see Section 6.3.4, “Perform Gap Analysis” Define candidate roadmap components; see Section 6.3.5, “Define Candidate Roadmap Components” Resolve impacts across the Architecture Landscape; see Section 6.3.6, “Resolve Impacts Across the Architecture Landscape” Conduct formal stakeholder review; see Section 6.3.7, “Conduct Formal Stakeholder Review” Finalize the Data Architecture; see Section 6.3.8, “Finalize the Data Architecture” Create/update the Architecture Definition Document; see Section 6.3.9, “Create/Update the Architecture Definition Document”

</details>

<a id="tag_06_03_01"></a>
## 6.3.1. Select Reference Models, Viewpoints, and Tools

概念：数据原则应复核验证，必要时生成，并选择参考/视点/捕获建模工具。

适用条件：需回答监管者、用户、生成者、主体、审计者及时间地点业务过程关切。

逻辑关系：数据视点覆盖实时、报告期、事件等维度；实体关系或类图可用，客户主数据/BI/元数据指南辅助。

决策方法：选择能回答具体数据关切的原则和模型。

制品及证据：数据原则、参考、视点、表单/模型工具。

适用边界：样例原则不自动成为企业已批准原则。

来源块：C220-web-2025:02-architecture-development-method:b00505, C220-web-2025:02-architecture-development-method:b00506, C220-web-2025:02-architecture-development-method:b00507, C220-web-2025:02-architecture-development-method:b00508, C220-web-2025:02-architecture-development-method:b00509, C220-web-2025:02-architecture-development-method:b00510, C220-web-2025:02-architecture-development-method:b00511, C220-web-2025:02-architecture-development-method:b00512, C220-web-2025:02-architecture-development-method:b00513

<details><summary>展开本节完整英文来源</summary>

6.3.1. Select Reference Models, Viewpoints, and Tools

Review and validate (or generate, if necessary) the set of data
principles. These will normally form part of an overarching set of
Architecture Principles. Guidelines for developing and applying
principles, and a sample set of data principles, are given in the TOGAF Standard — ADM Techniques .

Select relevant Data Architecture resources (reference models, patterns,
etc.) on the basis of the business drivers, stakeholders, concerns, and
Business Architecture.

Select relevant Data Architecture viewpoints (for example, stakeholders
of the data — regulatory bodies, users, generators, subjects, auditors,
etc.; various time dimensions — real-time, reporting period,
event-driven, etc.; locations; business processes); i.e., those that
will enable the architect to demonstrate how the stakeholder concerns
are being addressed in the Data Architecture.

Identify appropriate tools and techniques (including forms) to be used
for data capture, modeling, and analysis, in association with the
selected viewpoints. Depending on the degree of sophistication
warranted, these may comprise simple documents or spreadsheets, or more
sophisticated modeling tools and techniques such as data management
models, data models, etc.

Examples of data modeling techniques are:

Entity relationship diagram Class diagram

Further guidance on Information Architecture reference models can be
found in the following documents:

TOGAF ® Series Guide: Information Architecture — Customer Master Data Management TOGAF ® Series Guide: Information Architecture: Business Intelligence & Analytics TOGAF ® Series Guide: Information Architecture: Metadata Management

</details>

<a id="tag_06_03_01_01"></a>
## 6.3.1.1. Determine Overall Modeling Process

概念：数据整体建模从业务/应用资料收集模型，再统一要求和数据清单。

适用条件：各数据视点需具体模型。

逻辑关系：数据关联业务服务能力功能访问权限应用；视图说明创建、分布、迁移、安全与归档，缺关切需扩展模型。

决策方法：选择模型并协调已有数据目录语义。

制品及证据：数据清单、实体关系、跨域矩阵和生命周期视图。

适用边界：数据集中记录不自动保证语义一致。

来源块：C220-web-2025:02-architecture-development-method:b00514, C220-web-2025:02-architecture-development-method:b00515, C220-web-2025:02-architecture-development-method:b00516, C220-web-2025:02-architecture-development-method:b00517, C220-web-2025:02-architecture-development-method:b00518

<details><summary>展开本节完整英文来源</summary>

6.3.1.1. Determine Overall Modeling Process

For each viewpoint, select the models needed to support the specific
view required, using the selected tool or method.

Ensure that all stakeholder concerns are covered. If they are not,
create new models to address concerns not covered, or augment existing
models (see above).

The recommended process for developing a Data Architecture is as
follows:

Collect data-related models from existing Business Architecture and
Application Architecture materials Rationalize data requirements and align with any existing enterprise
data catalogs and models; this allows the development of a data
inventory and entity relationship Update and develop matrices across the architecture by relating data
to business service, business capability, business function, access
rights, and application Elaborate Data Architecture views by examining how data is created,
distributed, migrated, secured, and archived

</details>

<a id="tag_06_03_01_02"></a>
## 6.3.1.2. Identify Required Catalogs of Data Building Blocks

概念：数据目录表达数据实体→逻辑数据组件→物理数据组件等分解。

适用条件：盘点实现愿景所需数据。

逻辑关系：业务服务/信息图为前提；利用功能能力到应用/数据追溯统一要求，再清理语义差距重叠。

决策方法：确定完整数据清单及其分解/追溯。

制品及证据：数据目录、业务服务信息图和功能能力/应用/实体追溯。

适用边界：不同层级身份不能合并成同一物理表。

来源块：C220-web-2025:02-architecture-development-method:b00519, C220-web-2025:02-architecture-development-method:b00520, C220-web-2025:02-architecture-development-method:b00521, C220-web-2025:02-architecture-development-method:b00522, C220-web-2025:02-architecture-development-method:b00523, C220-web-2025:02-architecture-development-method:b00524

<details><summary>展开本节完整英文来源</summary>

6.3.1.2. Identify Required Catalogs of Data Building Blocks

Descriptions of data may be captured as a catalog showing decomposition
across related model entities (e.g., data entity → logical data
component → physical data component).

During the Business Architecture phase, a Business Service/Information
diagram was created showing the key data entities required by the main
business services. This is a prerequisite to successful Data
Architecture activities.

Using the traceability from business function/business capability to
application and data entity, it is possible to create an inventory of
the data needed to support the Architecture Vision.

Once the data requirements are consolidated in a single location, it is
possible to refine the data inventory to achieve semantic consistency
and to remove gaps and overlaps.

The TOGAF Standard — Architecture Content contains a detailed description of catalogs which
should be considered for development within a Data Architecture,
describing them in detail and relating them to entities, attributes, and
relationships in the TOGAF Enterprise Metamodel.

</details>

<a id="tag_06_03_01_03"></a>
## 6.3.1.3. Identify Required Matrices

概念：实体应用矩阵验证创建维护变换传递和使用映射。

适用条件：数据清单整理后发现实体无创建者或有创建无使用。

逻辑关系：标记明显问题供差距分析，更新关联图；必要时短迭代应用架构处理变化。

决策方法：核查数据应用映射与应回访应用的问题。

制品及证据：实体应用矩阵、未创建/未使用疑点和图更新。

适用边界：矩阵空白是调查线索，不自动证明实体无业务价值。

来源块：C220-web-2025:02-architecture-development-method:b00525, C220-web-2025:02-architecture-development-method:b00526, C220-web-2025:02-architecture-development-method:b00527, C220-web-2025:02-architecture-development-method:b00528, C220-web-2025:02-architecture-development-method:b00529

<details><summary>展开本节完整英文来源</summary>

6.3.1.3. Identify Required Matrices

At this stage, an entity to applications matrix could be produced to
validate this mapping. How data is created, maintained, transformed, and
passed to other applications, or used by other applications, will now
start to be understood. Obvious gaps such as entities that never seem to
be created by an application or data created but never used, need to be
noted for later gap analysis.

The rationalized data inventory can be used to update and refine the
architectural diagrams of how data relates to other aspects of the
architecture.

Once these updates have been made, it may be appropriate to drop into a
short iteration of the Application Architecture to resolve the changes
identified.

The TOGAF Standard — Architecture Content contains a detailed description of matrices which
should be considered for development within a Data Architecture,
describing them in detail and relating them to entities, attributes, and
relationships in the TOGAF Enterprise Metamodel.

</details>

<a id="tag_06_03_01_04"></a>
## 6.3.1.4. Identify Required Diagrams

概念：数据图需包括实体属性关系，并考虑企业与个人库/电子表格数据。

适用条件：数据模型粒度及维护现状不一。

逻辑关系：核查过时模型，在极细物理模式与高层过程要求之间取得适当细节平衡。

决策方法：选择满足关切且经过现状核实的建模粒度。

制品及证据：实体属性关系、企业/本地数据范围和模型核实。

适用边界：已有详细schema可能过时；层次差异不得视为齐备。

来源块：C220-web-2025:02-architecture-development-method:b00530, C220-web-2025:02-architecture-development-method:b00531, C220-web-2025:02-architecture-development-method:b00532, C220-web-2025:02-architecture-development-method:b00533, C220-web-2025:02-architecture-development-method:b00534, C220-web-2025:02-architecture-development-method:b00535

<details><summary>展开本节完整英文来源</summary>

6.3.1.4. Identify Required Diagrams

Diagrams present the Data Architecture information from a set of
different perspectives (viewpoints) according to the requirements of the
stakeholders.

Once the data entities have been refined, a diagram of the relationships
between entities and their attributes can be produced.

It is important to note at this stage that information may be a mixture
of enterprise-level data (from system service providers and package
vendor information) and local-level data held in personal databases and
spreadsheets.

The level of detail modeled needs to be carefully assessed. Some
physical system data models will exist down to a very detailed level;
others will only have core entities modeled. Not all data models will
have been kept up-to-date as applications were modified and extended
over time. It is important to achieve a balance in the level of detail
provided (e.g., the reproduction of existing detailed system physical
data schemas or the presentation of high-level process maps and data
requirements highlight the two extreme views).

The TOGAF Standard — Architecture Content contains a detailed description of diagrams which
should be considered for development within a Data Architecture,
describing them in detail and relating them to entities, attributes, and
relationships in the TOGAF Enterprise Metamodel.

</details>

<a id="tag_06_03_01_05"></a>
## 6.3.1.5. Identify Types of Requirement to be Collected

概念：数据聚焦要求由目录矩阵图正式化。

适用条件：目标数据实施并向应用技术传递约束。

逻辑关系：要求可属本域、传到应用/技术或指导设计实施以回应原架构要求。

决策方法：识别应由架构满足的数据要求。

制品及证据：数据要求、跨域输入和设计指导。

适用边界：架构要求不自动等于完整解决方案需求。

来源块：C220-web-2025:02-architecture-development-method:b00536, C220-web-2025:02-architecture-development-method:b00537, C220-web-2025:02-architecture-development-method:b00538, C220-web-2025:02-architecture-development-method:b00539, C220-web-2025:02-architecture-development-method:b00540

<details><summary>展开本节完整英文来源</summary>

6.3.1.5. Identify Types of Requirement to be Collected

Once the Data Architecture catalogs, matrices, and diagrams have been
developed, architecture modeling is completed by formalizing the
data-focused requirements for implementing the Target Architecture.

These requirements may:

Relate to the data domain Provide requirements input into the Application and Technology
Architectures Provide detailed guidance to be reflected during design and
implementation to ensure that the solution addresses the original
architecture requirements

Within this step, the architect should identify requirements that should
be met by the architecture (see Section 13.5.2, “Requirements Development” ).

</details>

<a id="tag_06_03_02"></a>
## 6.3.2. Develop Baseline Data Architecture Description

概念：数据基线细节以支持目标及保留数据元素为准。

适用条件：已有数据描述或需要新基线模型。

逻辑关系：优先库资产；按第一步模型补充相关方关切。

决策方法：决定现状数据块调查范围。

制品及证据：基线数据描述及数据块。

适用边界：现状不由目标推断。

来源块：C220-web-2025:02-architecture-development-method:b00541, C220-web-2025:02-architecture-development-method:b00542, C220-web-2025:02-architecture-development-method:b00543

<details><summary>展开本节完整英文来源</summary>

6.3.2. Develop Baseline Data Architecture Description

Develop a Baseline Description of the existing Data Architecture, to the
extent necessary to support the Target Data Architecture. The scope and
level of detail to be defined will depend on the extent to which
existing data elements are likely to be carried over into the Target
Data Architecture, and on whether architectural descriptions exist, as
described in Section 6.5, “Approach” . To the extent possible,
identify the relevant Data Architecture building blocks, drawing on the
Architecture Repository (see the TOGAF Standard — Architecture Content ).

Where new architecture models need to be developed to satisfy
stakeholder concerns, use the models identified within
the first step in this phase (see Section 6.3.1, “Select Reference Models, Viewpoints, and Tools” )
as a guideline for creating new architecture content to describe the Baseline
Architecture.

</details>

<a id="tag_06_03_03"></a>
## 6.3.3. Develop Target Data Architecture Description

概念：目标数据描述支撑愿景及目标业务架构。

适用条件：数据元素与目标有明确关系。

逻辑关系：按相关性和已有描述选细节、复用库、补模型，适当比较备选。

决策方法：选择目标数据块与方案。

制品及证据：目标数据模型、数据块和备选。

适用边界：参考模型不直接替代本企业数据规则。

来源块：C220-web-2025:02-architecture-development-method:b00544, C220-web-2025:02-architecture-development-method:b00545, C220-web-2025:02-architecture-development-method:b00546, C220-web-2025:02-architecture-development-method:b00547

<details><summary>展开本节完整英文来源</summary>

6.3.3. Develop Target Data Architecture Description

Develop a Target Description for the Data Architecture, to the extent
necessary to support the Architecture Vision and Target Business
Architecture. The scope and level of detail to be defined will depend on
the relevance of the data elements to attaining the Target Architecture,
and on whether architectural descriptions exist. To the extent possible,
identify the relevant Data Architecture building blocks, drawing on the
Architecture Repository (see TOGAF Standard — Architecture Content ).

Where new architecture models need to be developed to satisfy
stakeholder concerns, use the models identified within
the first step in this phase (see Section 6.3.1, “Select Reference Models, Viewpoints, and Tools” )
as a guideline for creating new architecture content to describe the Target
Architecture.

If appropriate, investigate different Target Architecture alternatives
and discuss these with stakeholders using the Architecture Alternatives
and Trade-offs technique (see the TOGAF Standard — ADM Techniques ).

</details>

<a id="tag_06_03_04"></a>
## 6.3.4. Perform Gap Analysis

概念：数据差距分析必须先核对内部一致性和准确性。

适用条件：基线目标数据模型已形成。

逻辑关系：取舍解决视图冲突、检查原则目标约束、记录参考视点变化并测需求完整，再分析差距。

决策方法：判断数据差距及视图冲突如何处理。

制品及证据：数据模型验证、视点修改、需求完整性与差距。

适用边界：名称集合相等不证明业务语义一致。

来源块：C220-web-2025:02-architecture-development-method:b00548, C220-web-2025:02-architecture-development-method:b00549, C220-web-2025:02-architecture-development-method:b00550, C220-web-2025:02-architecture-development-method:b00551

<details><summary>展开本节完整英文来源</summary>

6.3.4. Perform Gap Analysis

Verify the architecture models for internal consistency and accuracy:

Perform trade-off analysis to resolve conflicts (if any) among the
different views Validate that the models support the principles, objectives, and
constraints Note changes to the viewpoint represented in the selected models from
the Architecture Repository, and document Test architecture models for completeness against requirements

Identify gaps between the Baseline and Target, using the gap analysis
technique as described in the TOGAF Standard — ADM Techniques .

</details>

<a id="tag_06_03_05"></a>
## 6.3.5. Define Candidate Roadmap Components

概念：初始数据路线图基于基线目标差距并为后续活动排序。

适用条件：域差距已有结果。

逻辑关系：数据路线图是E跨专业综合路线图的原材料。

决策方法：确定候选活动优先顺序。

制品及证据：数据路线图候选组件。

适用边界：局部排序不是最终迁移优先级或资源承诺。

来源块：C220-web-2025:02-architecture-development-method:b00552, C220-web-2025:02-architecture-development-method:b00553, C220-web-2025:02-architecture-development-method:b00554

<details><summary>展开本节完整英文来源</summary>

6.3.5. Define Candidate Roadmap Components

Following the creation of a Baseline Architecture, Target Architecture,
and gap analysis, a data roadmap is required to prioritize activities
over the coming phases.

This initial Data Architecture roadmap will be used as raw material to
support more detailed definition of a consolidated, cross-discipline
roadmap within the Opportunities & Solutions phase.

</details>

<a id="tag_06_03_06"></a>
## 6.3.6. Resolve Impacts Across the Architecture Landscape

概念：数据架构需识别景观范围的双向影响与复用。

适用条件：本域与既有架构和计划/在建项目并存。

逻辑关系：同时检查本域影响他域、近期变化影响本域、他处复用与项目双向影响。

决策方法：逐项识别跨景观依赖与需协调变化。

制品及证据：数据影响分析、复用机会和项目关联。

适用边界：仅检测共享标识一致不足以证明变更影响已覆盖。

来源块：C220-web-2025:02-architecture-development-method:b00555, C220-web-2025:02-architecture-development-method:b00556, C220-web-2025:02-architecture-development-method:b00557, C220-web-2025:02-architecture-development-method:b00558

<details><summary>展开本节完整英文来源</summary>

6.3.6. Resolve Impacts Across the Architecture Landscape

Once the Data Architecture is finalized, it is necessary to understand
any wider impacts or implications.

At this stage, other architecture artifacts in the Architecture
Landscape should be examined to identify:

Does this Data Architecture create an impact on any pre-existing
architectures? Have recent changes been made that impact the Data Architecture? Are there any opportunities to leverage work from this Data
Architecture in other areas of the organization? Does this Data Architecture impact other projects (including those
planned as well as those currently in progress)? Will this Data Architecture be impacted by other projects (including
those planned as well as those currently in progress)?

</details>

<a id="tag_06_03_07"></a>
## 6.3.7. Conduct Formal Stakeholder Review

概念：正式数据复核检查动机和说明书，同时评估对业务/应用影响与技术约束。

适用条件：数据变化可能改变表单流程应用或数据库。

逻辑关系：重大影响可回访B/应用或短迭代应用；约束即将设计的技术，仅必要时细化数据方案。

决策方法：决定影响是否重大及是否重访上游/同域工作。

制品及证据：复核、业务/应用影响和技术约束。

适用边界：影响分析必须具体到变化含义，不仅对象引用。

来源块：C220-web-2025:02-architecture-development-method:b00559, C220-web-2025:02-architecture-development-method:b00560, C220-web-2025:02-architecture-development-method:b00561, C220-web-2025:02-architecture-development-method:b00562, C220-web-2025:02-architecture-development-method:b00563, C220-web-2025:02-architecture-development-method:b00564

<details><summary>展开本节完整英文来源</summary>

6.3.7. Conduct Formal Stakeholder Review

Check the original motivation for the architecture project and the
Statement of Architecture Work against the proposed Data Architecture.
Conduct an impact analysis to identify any areas where the Business and
Application Architectures (e.g., business practices) may need to change
to cater for changes in the Data Architecture (for example, changes to
forms or procedures, applications, or database systems).

If the impact is significant, this may warrant the Business and
Application Architectures being revisited.

Identify any areas where the Application Architecture (if generated at
this point) may need to change to cater for changes in the Data
Architecture (or to identify constraints on the Application Architecture
about to be designed).

If the impact is significant, it may be appropriate to drop into a short
iteration of the Application Architecture at this point.

Identify any constraints on the Technology Architecture about to be
designed, refining the proposed Data Architecture only if necessary.

</details>

<a id="tag_06_03_08"></a>
## 6.3.8. Finalize the Data Architecture

概念：完成数据块标准、完整描述、最终追溯和库映射。

适用条件：数据架构收尾。

逻辑关系：复用选定参考标准，总核验业务要求/目标，记录块决定理由，发布可复用块并关闭差距等工作。

决策方法：确认块标准、业务适配和可复用发布。

制品及证据：数据块描述、标准/理由、追溯报告、库映射和最终产品。

适用边界：发布经过治理，不以文件存在自动认定正式完成。

来源块：C220-web-2025:02-architecture-development-method:b00565, C220-web-2025:02-architecture-development-method:b00566

<details><summary>展开本节完整英文来源</summary>

6.3.8. Finalize the Data Architecture

Select standards for each of the building blocks, re-using as much as
possible from the reference models selected from the Architecture
Repository Fully document each building block Conduct a final cross-check of overall architecture against business
requirements; document the rationale for building block decisions in the
architecture document Document the final requirements traceability report Document the final mapping of the architecture within the Architecture
Repository; from the selected building blocks, identify those that might
be re-used, and publish via the Architecture Repository Finalize all the work products, such as gap analysis

</details>

<a id="tag_06_03_09"></a>
## 6.3.9. Create/Update the Architecture Definition Document

概念：定义文档数据部分记录块决策理由并可含业务/逻辑数据和管理过程模型。

适用条件：发布数据架构结果。

逻辑关系：可含实体业务功能矩阵、互操作要求如XML模式安全政策；按相关方反馈修改。

决策方法：选择满足范围的模型与互操作内容。

制品及证据：数据章节、模型/矩阵、互操作要求及复核。

适用边界：some or all保留可裁剪性；XML是例子。

来源块：C220-web-2025:02-architecture-development-method:b00567, C220-web-2025:02-architecture-development-method:b00568, C220-web-2025:02-architecture-development-method:b00569, C220-web-2025:02-architecture-development-method:b00570

<details><summary>展开本节完整英文来源</summary>

6.3.9. Create/Update the Architecture Definition Document

Document the rationale for building block decisions in the Architecture
Definition Document.

Prepare the Data Architecture sections of the Architecture Definition
Document, comprising some or all of:

Business data model Logical data model Data management process model Data Entity/Business Function matrix Data interoperability requirements (e.g., XML schema, security
policies) If appropriate, use reports and/or graphics generated by modeling
tools to demonstrate key views of the architecture; route the document
for review by relevant stakeholders, and incorporate feedback

</details>

<a id="tag_06_04"></a>
## 6.4. Outputs

概念：数据输出包含获批目标及可适用的获批基线，定义/要求文档整体可仍是草稿。

适用条件：交付数据部分C结果。

逻辑关系：目标含数据模型管理过程矩阵视图；要求含差距互操作技术约束，必要时更新业务/应用要求及A产物。

决策方法：标定批准状态及向他域传递要求。

制品及证据：数据定义/要求、数据原则和路线图组件。

适用边界：模板字段不能替代正式批准与真实数据质量。

来源块：C220-web-2025:02-architecture-development-method:b00571, C220-web-2025:02-architecture-development-method:b00572, C220-web-2025:02-architecture-development-method:b00573, C220-web-2025:02-architecture-development-method:b00574

<details><summary>展开本节完整英文来源</summary>

6.4. Outputs

The outputs of Phase C (Data Architecture) may include, but are not
restricted to:

Refined and updated versions of the Architecture Vision phase
deliverables, where applicable: Statement of Architecture Work (see the TOGAF Standard — Architecture Content ), updated if necessary Validated data principles (see the TOGAF Standard — ADM Techniques ), or
new data principles (if generated here) Draft Architecture Definition Document (see the TOGAF Standard — Architecture Content ), including: Baseline Data Architecture, Approved, if appropriate Target Data Architecture, Approved, including: Business data model Logical data model Data management process models Data Entity/Business Function matrix Views corresponding to the selected viewpoints addressing key
stakeholder concerns Draft Architecture Requirements Specification (see the TOGAF Standard — Architecture Content ), including such Data Architecture requirements as: Gap analysis results Data interoperability requirements Relevant technical requirements that will apply to this evolution of
the architecture development cycle Constraints on the Technology Architecture about to be designed Updated business requirements, if appropriate Updated application requirements, if appropriate Data Architecture components of an Architecture Roadmap (see the TOGAF Standard — Architecture Content )

The TOGAF Standard — Architecture Content contains a detailed description of architectural
artifacts which might be produced in this phase.

</details>

<a id="tag_06_05"></a>
## 6.5. Approach

概念：本标题为结构容器，无独立说明段落。

适用条件：阅读该主题时应继续读取下列子节。

逻辑关系：子节分工：tag_06_05_01: 6.5.1. Data Structure；tag_06_05_02: 6.5.2. Key Considerations for Data Architecture；tag_06_05_03: 6.5.3. Architecture Repository

决策方法：不从空容器推出附加规则或完成状态。

制品及证据：实际概念、决策和制品证据见上述子节。

适用边界：空容器覆盖仅证明目录和子节连接，不计额外深度结论。

来源块：C220-web-2025:02-architecture-development-method:b00575

<details><summary>展开本节完整英文来源</summary>

6.5. Approach

</details>

<a id="tag_06_05_01"></a>
## 6.5.1. Data Structure

概念：数据范围包括静止、运动、使用中、开放数据；三层实体为数据实体/逻辑组件/物理组件。

适用条件：描述概念到实施及交换质量时。

逻辑关系：概念模型帮助开发理解，逻辑模型定义存储交换界面要求；物理组件是已实施集群或实施要求，各层均可用于交换和情境质量属性。

决策方法：选正确数据身份和生命周期/交换要求。

制品及证据：概念/逻辑/物理模型及静止运动使用开放数据要求。

适用边界：客户只有一地址是示例规则，不能推广到所有企业；实体层级不能混同。

来源块：C220-web-2025:02-architecture-development-method:b00576, C220-web-2025:02-architecture-development-method:b00577, C220-web-2025:02-architecture-development-method:b00578, C220-web-2025:02-architecture-development-method:b00579, C220-web-2025:02-architecture-development-method:b00580, C220-web-2025:02-architecture-development-method:b00581, C220-web-2025:02-architecture-development-method:b00582, C220-web-2025:02-architecture-development-method:b00583, C220-web-2025:02-architecture-development-method:b00584, C220-web-2025:02-architecture-development-method:b00585

<details><summary>展开本节完整英文来源</summary>

6.5.1. Data Structure

A Data Architecture should be able to handle:

Data at rest — data in stores Data in motion — data in transactions or services/APIs Data in use — data at the border of the application (e.g., GUI) Open data — data that the organization provides for public usage and
which it is voluntarily or legally required to provide

Different alternate ways of working with these types of Data
Architecture will be added.

Data Architecture is created by using three metamodel entities: data
entity, logical data component, and physical data component.

Data entities can be used to create conceptual data models to help the
IT developers understand the concepts they will be dealing with. Often
the entity relationship models also contain some requirements on the
relations (e.g., a customer can only have one address).

Logical data components can be used to create logical data models. Often
it is important for the IT area to have a clear view of all data that is
used in the IT environment. The logical data model is often used as a
requirement on the data stored in applications (at rest), data moved
between applications (in motion), or data at the user interface of
applications (data in use).

Physical data components are clusters of logical data components that
have been implemented by some earlier project (links to, for example,
XML message, database schemas) or requirements for new implementation
projects.

All three data entities can be used in data exchange models for data
passed between/into/out of IS services, logical application components,
or physical application components.

All data entities can have quality attributes for specific situations.

</details>

<a id="tag_06_05_02"></a>
## 6.5.2. Key Considerations for Data Architecture

概念：本标题为结构容器，无独立说明段落。

适用条件：阅读该主题时应继续读取下列子节。

逻辑关系：子节分工：tag_06_05_02_01: 6.5.2.1. Data Management；tag_06_05_02_02: 6.5.2.2. Data Migration；tag_06_05_02_03: 6.5.2.3. Data Governance

决策方法：不从空容器推出附加规则或完成状态。

制品及证据：实际概念、决策和制品证据见上述子节。

适用边界：空容器覆盖仅证明目录和子节连接，不计额外深度结论。

来源块：C220-web-2025:02-architecture-development-method:b00586

<details><summary>展开本节完整英文来源</summary>

6.5.2. Key Considerations for Data Architecture

</details>

<a id="tag_06_05_02_01"></a>
## 6.5.2.1. Data Management

概念：大型转型要明确主数据记录/参考系统、数据标准和交换变换。

适用条件：数据管理可能形成竞争价值或集成约束。

逻辑关系：需理解业务/服务使用及创建存储运输报告位置、变换复杂度、客户供应商集成软件需求。

决策方法：决定主数据权威、企业标准与套装约束、ETL/质量分析需求。

制品及证据：数据管理规则、系统权威及流向/变换需求。

适用边界：记录系统不等于所有场景唯一一致性方案；需业务依据。

来源块：C220-web-2025:02-architecture-development-method:b00587, C220-web-2025:02-architecture-development-method:b00588, C220-web-2025:02-architecture-development-method:b00589, C220-web-2025:02-architecture-development-method:b00590, C220-web-2025:02-architecture-development-method:b00591

<details><summary>展开本节完整英文来源</summary>

6.5.2.1. Data Management

When an enterprise has chosen to undertake large-scale architectural
transformation, it is important to understand and address data
management issues. A structured and comprehensive approach to data
management enables the effective use of data to capitalize on its
competitive advantages.

Considerations include:

A clear definition of which application components in the landscape
will serve as the system of record or reference for enterprise master
data Will there be an enterprise-wide standard that all application
components, including software packages, need to adopt? (In the main, packages can be prescriptive about the data models and may
not be flexible.) Clearly understand how data entities are utilized by business
capabilities, business functions, processes, and business and
application services Clearly understand how and where enterprise data entities are created,
stored, transported, and reported What is the level and complexity of data transformations required to
support the information exchange needs between applications? What will be the requirement for software in supporting data integration with the enterprise’s customers and suppliers (e.g., use of Extract, Transform, Load (ETL) tools during data migration, data profiling tools to evaluate data quality, etc.)?

More guidance on data management can be found in the TOGAF ® Series Guide: Information Architecture — Customer Master Data Management .

</details>

<a id="tag_06_05_02_02"></a>
## 6.5.2.2. Data Migration

概念：替换应用必须迁移主、交易和参考数据并保证目标填充质量。

适用条件：现有应用被新应用替代。

逻辑关系：架构识别迁移和转换筛选清理程度，企业公共数据定义支撑转换。

决策方法：确认迁移范围与质量/目标约束。

制品及证据：迁移要求、变换清理指示和公共定义。

适用边界：迁移脚本存在不能证明质量和恢复目标达成。

来源块：C220-web-2025:02-architecture-development-method:b00592, C220-web-2025:02-architecture-development-method:b00593

<details><summary>展开本节完整英文来源</summary>

6.5.2.2. Data Migration

When an existing application is replaced, there will be a critical need to migrate data (master, transactional, and reference) to the new application. The Data Architecture should identify data migration requirements and also provide indicators as to the level of transformation, weeding, and cleansing that will be required to present data in a format that meets the requirements and constraints of the
target application. The objective being that the target application has quality data when it is populated. Another key consideration is to ensure that an enterprise-wide common data definition is established to support the transformation.

</details>

<a id="tag_06_05_02_03"></a>
## 6.5.2.3. Data Governance

概念：数据治理考虑结构、管理系统、人员三维。

适用条件：组织需支撑数据实体全生命周期转型。

逻辑关系：标准组织与管理项目建立治理；缺技能角色时可获取技能或制定学习计划。

决策方法：确认治理结构与角色技能缺口及取得路径。

制品及证据：组织/标准机构、生命周期管理、技能角色和学习计划。

适用边界：培训安排不证明人员行为胜任已提升。

来源块：C220-web-2025:02-architecture-development-method:b00594, C220-web-2025:02-architecture-development-method:b00595, C220-web-2025:02-architecture-development-method:b00596

<details><summary>展开本节完整英文来源</summary>

6.5.2.3. Data Governance

Data governance considerations ensure that the enterprise has the necessary dimensions in place to enable the transformation, as follows:

Structure : this dimension pertains to whether the enterprise has the necessary organizational structure and the standards bodies to manage data entity aspects of the transformation Management System : here enterprises should have the necessary management system and data-related programs to manage the governance aspects of data entities throughout its lifecycle People : this dimension addresses what data-related skills and roles the enterprise requires for the transformation If the enterprise lacks such resources and skills, the enterprise should consider either acquiring those critical skills or training existing internal resources to meet the requirements through a well-defined learning program.

</details>

<a id="tag_06_05_03"></a>
## 6.5.3. Architecture Repository

概念：数据库资源尤其包括行业通用数据模型。

适用条件：本阶段选择可复用数据参考。

逻辑关系：通用模型需与企业数据情境匹配。

决策方法：判断行业模型适合哪些实体。

制品及证据：数据参考选择与库映射。

适用边界：行业模型不自动成为企业主数据定义。

来源块：C220-web-2025:02-architecture-development-method:b00597, C220-web-2025:02-architecture-development-method:b00598

<details><summary>展开本节完整英文来源</summary>

6.5.3. Architecture Repository

As part of this phase, the architecture team will need to consider what relevant Data Architecture resources are available in the organization’s Architecture Repository (see the TOGAF Standard — Architecture Content ); in particular, generic data models relevant to the
organization’s industry “vertical” sector.

</details>

<a id="chap07"></a>
## 7. Phase C: Information Systems Architectures — Application Architecture

概念：本章开发应用架构。

适用条件：需要应用域支撑愿景及业务时。

逻辑关系：应用描述与其他域共同形成信息系统或技术架构。

决策方法：确定本轮应用工作边界。

制品及证据：应用基线/目标与工作结果。

适用边界：域开发不能脱离已批准工作范围。

来源块：C220-web-2025:02-architecture-development-method:b00599, C220-web-2025:02-architecture-development-method:b00600

<details><summary>展开本节完整英文来源</summary>

7. Phase C: Information Systems Architectures — Application Architecture

This chapter describes the Application Architecture part of Phase C.

</details>

<a id="tag_07_01"></a>
## 7.1. Objectives

概念：目标应用架构支撑业务架构和愿景，基线目标差距产生路线图候选。

适用条件：工作说明书和相关方关切确定后。

逻辑关系：应用变更须连接业务支持和价值。

决策方法：核验目标应用满足愿景/工作关切。

制品及证据：目标应用架构与候选组件。

适用边界：候选组件不等于已批准跨域实施计划。

来源块：C220-web-2025:02-architecture-development-method:b00601, C220-web-2025:02-architecture-development-method:b00602, C220-web-2025:02-architecture-development-method:b00603

<details><summary>展开本节完整英文来源</summary>

7.1. Objectives

The objectives of the Application Architecture part of Phase C are to:

Develop the Target Application Architecture that enables the Business
Architecture and the Architecture Vision, in a way that addresses the
Statement of Architecture Work and stakeholder concerns Identify candidate Architecture Roadmap components based upon gaps
between the Baseline and Target Application Architectures

</details>

<a id="tag_07_02"></a>
## 7.2. Inputs

概念：应用输入按外部、非架构和架构资料分类。

适用条件：启动应用开发时。

逻辑关系：7.2.1—7.2.3给出三类具体输入。

决策方法：确认各类资料及状态。

制品及证据：应用输入来源与状态清单。

适用边界：导航不证明输入完整。

来源块：C220-web-2025:02-architecture-development-method:b00604, C220-web-2025:02-architecture-development-method:b00605

<details><summary>展开本节完整英文来源</summary>

7.2. Inputs

This section defines the inputs to Phase C (Application Architecture).

</details>

<a id="tag_07_02_01"></a>
## 7.2.1. Reference Materials External to the Enterprise

概念：应用外部参考包括架构参考材料。

适用条件：选择应用参考时。

逻辑关系：参考为模式与约束信息来源，仍需按业务需求评估。

决策方法：判断外部资源适用性。

制品及证据：架构参考材料及出处。

适用边界：外部内容不自动成为当前目标架构。

来源块：C220-web-2025:02-architecture-development-method:b00606, C220-web-2025:02-architecture-development-method:b00607

<details><summary>展开本节完整英文来源</summary>

7.2.1. Reference Materials External to the Enterprise

Architecture reference materials (see the TOGAF Standard — Architecture Content )

</details>

<a id="tag_07_02_02"></a>
## 7.2.2. Non-Architectural Inputs

概念：应用非架构输入为工作请求、能力评估和沟通计划。

适用条件：安排应用工作与参与条件。

逻辑关系：业务任务、能力和沟通影响域分析。

决策方法：确认任务与人员参与及能力条件。

制品及证据：工作请求、能力评估、沟通计划。

适用边界：已识别能力缺口持续保留，不能默认消除。

来源块：C220-web-2025:02-architecture-development-method:b00608, C220-web-2025:02-architecture-development-method:b00609

<details><summary>展开本节完整英文来源</summary>

7.2.2. Non-Architectural Inputs

Request for Architecture Work (see the TOGAF Standard — Architecture Content ) Capability Assessment (see the TOGAF Standard — Architecture Content ) Communications Plan (see the TOGAF Standard — Architecture Content )

</details>

<a id="tag_07_02_03"></a>
## 7.2.3. Architectural Inputs

概念：应用架构输入继承组织模型、裁剪框架、说明书愿景、库、现有应用原则（如有）。

适用条件：开展应用域细化。

逻辑关系：B及可用时的数据差距、技术要求，以及可用的业务/数据路线图

决策方法：检查上游要求、已有块与路线图是否适用且当前。

制品及证据：B及可用时的数据差距、技术要求，以及可用的业务/数据路线图及草稿定义/要求文档。

适用边界：if existing/if available保留条件性，不能伪造缺失输入。

来源块：C220-web-2025:02-architecture-development-method:b00610, C220-web-2025:02-architecture-development-method:b00611

<details><summary>展开本节完整英文来源</summary>

7.2.3. Architectural Inputs

Organizational Model for Enterprise Architecture (see the TOGAF Standard — Architecture Content ), including: Scope of organizations impacted Maturity assessment, gaps, and resolution approach Roles and responsibilities for architecture team(s) Constraints on architecture work Budget requirements Governance and support strategy Tailored Architecture Framework (see the TOGAF Standard — Architecture Content ), including: Tailored architecture method Tailored architecture content (deliverables and artifacts) Configured and deployed tools Application principles (see the TOGAF Standard — ADM Techniques ), if
existing Statement of Architecture Work (see the TOGAF Standard — Architecture Content ) Architecture Vision (see the TOGAF Standard — Architecture Content ) Architecture Repository (see the TOGAF Standard — Architecture Content ), including: Re-usable building blocks Publicly available reference models Organization-specific reference models Organization standards Draft Architecture Definition Document, which may include Baseline
and/or Target Architectures of any architecture domain Draft Architecture Requirements Specification (see the TOGAF Standard — Architecture Content ), including: Gap analysis results (from Business Architecture and Data
Architecture, if available) Relevant technical requirements that will apply to this phase Business and Data Architecture components of an Architecture Roadmap,
if available (see the TOGAF Standard — Architecture Content )

</details>

<a id="tag_07_03"></a>
## 7.3. Steps

概念：应用开发九步以总体范围目标确定细节。

适用条件：新应用块或已有块需支持目标时。

逻辑关系：新应用块详细定义；已有保留应用块若定义不足也需补定义；基线/目标可先行任一，启动活动在7.3.8关闭，文档在7.3.9正式发布。

决策方法：按治理调整顺序、起止和所需深度。

制品及证据：应用开发步骤、收尾和发布记录。

适用边界：可迭代不免除收尾和正式发布要求。

来源块：C220-web-2025:02-architecture-development-method:b00612, C220-web-2025:02-architecture-development-method:b00613, C220-web-2025:02-architecture-development-method:b00614, C220-web-2025:02-architecture-development-method:b00615, C220-web-2025:02-architecture-development-method:b00616, C220-web-2025:02-architecture-development-method:b00617, C220-web-2025:02-architecture-development-method:b00618

<details><summary>展开本节完整英文来源</summary>

7.3. Steps

The level of detail addressed in Phase C will depend on the scope and
goals of the overall architecture effort.

New application building blocks being introduced as part of this effort
will need to be defined in detail during Phase C. Existing application
building blocks to be carried over and supported in the target
environment may already have been adequately defined in previous
architectural work; but, if not, they too will need to be defined in
Phase C.

The order of the steps in this phase as well as the time at which they
are formally started and completed should be adapted to the situation at
hand in accordance with the established Architecture Governance. In
particular, determine whether in this situation it is appropriate to
conduct Baseline Description or Target Architecture development first,
as described in the TOGAF Standard — Applying the ADM .

All activities that have been initiated in these steps should be closed
during the Finalize the Application Architecture step; see Section 7.3.8, “Finalize the Application Architecture” .
The documentation generated from these steps must be formally published in
the Create/Update the Architecture Definition Document step; see Section 7.3.9, “Create/Update the Architecture Definition Document” .

The steps in Phase C (Application Architecture) are as follows:

Select reference models, viewpoints, and tools; see Section 7.3.1, “Select Reference Models, Viewpoints, and Tools” Develop Baseline Application Architecture Description; see Section 7.3.2, “Develop Baseline Application Architecture Description” Develop Target Application Architecture Description; see Section 7.3.3, “Develop Target Application Architecture Description” Perform gap analysis; see Section 7.3.4, “Perform Gap Analysis” Define candidate roadmap components; see Section 7.3.5, “Define Candidate Roadmap Components” Resolve impacts across the Architecture Landscape; see Section 7.3.6, “Resolve Impacts Across the Architecture Landscape” Conduct formal stakeholder review; see Section 7.3.7, “Conduct Formal Stakeholder Review” Finalize the Application Architecture; see Section 7.3.8, “Finalize the Application Architecture” Create/Update the Architecture Definition Document; see Section 7.3.9, “Create/Update the Architecture Definition Document”

</details>

<a id="tag_07_03_01"></a>
## 7.3.1. Select Reference Models, Viewpoints, and Tools

概念：应用原则需验证或必要时生成，并选择应用参考、用户视点与工具。

适用条件：应用用户与功能关切需要表达。

逻辑关系：可考虑平台独立业务逻辑描述，MDA是保留逻辑不受实现技术变化的一种方法。

决策方法：选择相关原则、视点及是否使用平台无关模型。

制品及证据：应用原则/参考、视点、模型工具与逻辑描述。

适用边界：MDA是可考虑方式，不是强制技术标准。

来源块：C220-web-2025:02-architecture-development-method:b00619, C220-web-2025:02-architecture-development-method:b00620, C220-web-2025:02-architecture-development-method:b00621, C220-web-2025:02-architecture-development-method:b00622, C220-web-2025:02-architecture-development-method:b00623, C220-web-2025:02-architecture-development-method:b00624

<details><summary>展开本节完整英文来源</summary>

7.3.1. Select Reference Models, Viewpoints, and Tools

Review and validate (or generate, if necessary) the set of application
principles. These will normally form part of an overarching set of
Architecture Principles. Guidelines for developing and applying
principles, and a sample set of application principles, are given in the TOGAF Standard — ADM Techniques .

Select relevant Application Architecture resources (reference models,
patterns, etc.) from the Architecture Repository, on the basis of the
business drivers, the stakeholders, and their concerns.

Select relevant Application Architecture viewpoints (for example,
stakeholders of the applications — viewpoints relevant to functional and
individual users of applications, etc.); i.e., those that will enable
the architect to demonstrate how the stakeholder concerns are being
addressed in the Application Architecture.

Identify appropriate tools and techniques to be used for capture,
modeling, and analysis, in association with the selected viewpoints.
Depending on the degree of sophistication warranted, these may comprise
simple documents or spreadsheets, or more sophisticated modeling tools
and techniques.

Consider using platform-independent descriptions of business logic. For
example, the OMG Model-Driven Architecture ® (MDA ® ) offers an approach to
modeling Application Architectures that preserves the business logic
from changes to the underlying platform and implementation technology.

</details>

<a id="tag_07_03_01_01"></a>
## 7.3.1.1. Determine Overall Modeling Process

概念：应用整体建模从基线组合、要求和业务范围开始。

适用条件：需要形成足够粒度以识别差距和工作包。

逻辑关系：分解复杂应用、去重复功能、合并相似应用，识别逻辑及适当物理应用，映射业务服务能力数据流程并分析集成迁移开发运营。

决策方法：按范围目的确定分解程度和候选工作包。

制品及证据：应用定义、逻辑/物理应用、矩阵与应用视图。

适用边界：去重合并需语义判断，名称类似不是充分依据。

来源块：C220-web-2025:02-architecture-development-method:b00625, C220-web-2025:02-architecture-development-method:b00626, C220-web-2025:02-architecture-development-method:b00627, C220-web-2025:02-architecture-development-method:b00628, C220-web-2025:02-architecture-development-method:b00629, C220-web-2025:02-architecture-development-method:b00630, C220-web-2025:02-architecture-development-method:b00631

<details><summary>展开本节完整英文来源</summary>

7.3.1.1. Determine Overall Modeling Process

For each viewpoint, select the models needed to support the specific
view required, using the selected tool or method.

Ensure that all stakeholder concerns are covered. If they are not,
create new models to address concerns not covered, or augment existing
models (see above).

The recommended process for developing an Application Architecture is as
follows:

Understand the list of applications or application components that are
required, based on the baseline Application Portfolio, what the
requirements are, and the Business Architecture scope Simplify complicated applications by decomposing them into two or more
applications Ensure that the set of application definitions is internally
consistent, by removing duplicate functionality as far as possible, and
combining similar applications into one Identify logical applications and the most appropriate physical
applications Develop matrices across the architecture by relating applications to
business services, business capabilities, data, processes, etc. Elaborate a set of Application Architecture views by examining how the
application will function, capturing integration, migration,
development, and operational concerns

The level and rigor of decomposition needed varies from enterprise to
enterprise, as well as within an enterprise, and the architect should
consider the enterprise’s goals, objectives, scope, and purpose of the
Enterprise Architecture effort to determine the level of decomposition.

The level of granularity should be sufficient to enable identification
of gaps and the scope of candidate work packages.

</details>

<a id="tag_07_03_01_02"></a>
## 7.3.1.2. Identify Required Catalogs of Application Building Blocks

概念：应用组合目录表达逻辑应用→物理应用→应用服务等层次与跨实体分解。

适用条件：建立矩阵图和能力管理原材料。

逻辑关系：目录结构依元模型实体属性，存架构库。

决策方法：确定组合目录与相关实体层级。

制品及证据：应用组合目录、属性和分解关系。

适用边界：逻辑/物理组件及服务不能混成同一对象。

来源块：C220-web-2025:02-architecture-development-method:b00632, C220-web-2025:02-architecture-development-method:b00633, C220-web-2025:02-architecture-development-method:b00634, C220-web-2025:02-architecture-development-method:b00635, C220-web-2025:02-architecture-development-method:b00636

<details><summary>展开本节完整英文来源</summary>

7.3.1.2. Identify Required Catalogs of Application Building Blocks

The organization’s Application Portfolio is captured as a catalog within
the Architecture Repository. Catalogs are hierarchical in nature and
capture a decomposition of a metamodel entity and also decompositions
across related model entities (e.g., logical application component →
physical application component → application service).

Catalogs form the raw material for the development of matrices and
diagrams and also act as a key resource for managing the business and IT
capability.

The structure of catalogs is based on the attributes of metamodel entities, as defined in the TOGAF Standard — Architecture Content .

The TOGAF Standard — Architecture Content contains a detailed description of catalogs which
should be considered for development within an Application Architecture, describing them in detail and relating them to entities, attributes, and relationships in the TOGAF Enterprise Metamodel.

</details>

<a id="tag_07_03_01_03"></a>
## 7.3.1.3. Identify Required Matrices

概念：应用矩阵先映射业务服务目的，再关联数据与用户/组织依赖。

适用条件：已有基线组合且需影响/未来规划。

逻辑关系：业务信息图可联系数据；可用数据模型核实本地/远程数据，适合时短迭代数据；必须特别考虑运营支持和共享运营依赖。

决策方法：确定受影响用户组、运营能力与需新增治理/应用要求。

制品及证据：应用业务服务/数据/用户组织矩阵、运营管理依赖图。

适用边界：运营支持方不能被仅功能用户视点遗漏。

来源块：C220-web-2025:02-architecture-development-method:b00637, C220-web-2025:02-architecture-development-method:b00638, C220-web-2025:02-architecture-development-method:b00639, C220-web-2025:02-architecture-development-method:b00640, C220-web-2025:02-architecture-development-method:b00641, C220-web-2025:02-architecture-development-method:b00642, C220-web-2025:02-architecture-development-method:b00643, C220-web-2025:02-architecture-development-method:b00644, C220-web-2025:02-architecture-development-method:b00645, C220-web-2025:02-architecture-development-method:b00646, C220-web-2025:02-architecture-development-method:b00647

<details><summary>展开本节完整英文来源</summary>

7.3.1.3. Identify Required Matrices

Matrices show the core relationships between related model entities.

Matrices form the raw material for development of diagrams and also act as a key resource for impact assessment.

Once the baseline Application Portfolio has been assembled, it is
necessary to map the applications to their purpose in supporting the
business. The initial mapping should focus on business services within
the Business Architecture, as this is the level of granularity where
architecturally significant decisions are most likely to be needed.

Once applications are mapped to business services, it will also be
possible to make associations from applications to data, through the
business-information diagrams developed during Business Architecture.

If readily available, baseline application data models may be used to
validate the Business Architecture and also to identify which data is
held locally and which is accessed remotely.

The Data Architecture phase will focus on these issues, so at this point
it may be appropriate to drop into a short iteration of the Data
Architecture if it is deemed to be valuable to the scope of the
architecture engagement.

Using existing information in the baseline application catalog, the
Application Architecture should identify user and organizational
dependencies on applications. This activity will support future state
planning by determining impacted user communities and also facilitating
the grouping of applications by user type or user location.

A key user community to be specifically considered is the operational
support organization. This activity should examine application
dependencies on shared operations capabilities and produce a diagram on
how each application is effectively operated and managed.

Specifically considering the needs of the operational community may
identify requirements for new or extended governance capabilities and
applications.

The TOGAF Standard — Architecture Content contains a detailed description of matrices which
should be considered for development within an Application Architecture,
describing them in detail and relating them to entities, attributes, and
relationships in the TOGAF Enterprise Metamodel.

</details>

<a id="tag_07_03_01_04"></a>
## 7.3.1.4. Identify Required Diagrams

概念：应用图除表达视点还应评估内部结构。

适用条件：功能已知，需要组织后续设计。

逻辑关系：套装应用有配置附加模块服务选项；定制应用需高层模块/子系统。

决策方法：选择套装配置或定制高层结构。

制品及证据：应用结构和相关方视图。

适用边界：架构高层结构不等于详细实现设计。

来源块：C220-web-2025:02-architecture-development-method:b00648, C220-web-2025:02-architecture-development-method:b00649, C220-web-2025:02-architecture-development-method:b00650, C220-web-2025:02-architecture-development-method:b00651

<details><summary>展开本节完整英文来源</summary>

7.3.1.4. Identify Required Diagrams

Diagrams present the Application Architecture information from a set of
different perspectives (viewpoints) according to the requirements of the
stakeholders. Once the desired functionality of an application is known,
it is necessary to perform an internal assessment of how the application
should be best structured to meet its requirements.

In the case of packaged applications, it is likely to be the case that
the application supports a number of configuration options, add-on
modules, or application services that may be applied to the solution.
For custom developed applications, it is necessary to identify the
high-level structure of the application in terms of modules or
subsystems as a foundation to organize design activity.

The TOGAF Standard — Architecture Content contains a detailed description of diagrams which
should be considered for development within an Application Architecture,
describing them in detail and relating them to entities, attributes, and
relationships in the TOGAF Enterprise Metamodel.

</details>

<a id="tag_07_03_01_05"></a>
## 7.3.1.5. Identify Types of Requirement to be Collected

概念：应用聚焦要求由目录矩阵图正式化。

适用条件：目标应用实施并向数据技术传递输入。

逻辑关系：要求属本域、约束数据/技术或指导设计实施以满足原架构。

决策方法：识别需由架构满足的应用要求。

制品及证据：应用要求、数据技术输入及设计指导。

适用边界：要求传递须保留源业务依据。

来源块：C220-web-2025:02-architecture-development-method:b00652, C220-web-2025:02-architecture-development-method:b00653, C220-web-2025:02-architecture-development-method:b00654, C220-web-2025:02-architecture-development-method:b00655, C220-web-2025:02-architecture-development-method:b00656

<details><summary>展开本节完整英文来源</summary>

7.3.1.5. Identify Types of Requirement to be Collected

Once the Application Architecture catalogs, matrices, and diagrams have
been developed, architecture modeling is completed by formalizing the
application-focused requirements for implementing the Target
Architecture.

These requirements may:

Relate to the application domain Provide requirements input into the Data and Technology Architectures Provide detailed guidance to be reflected during design and
implementation to ensure that the solution addresses the original
architecture requirements

Within this step, the architect should identify requirements that should
be met by the architecture; see Section 13.5.2, “Requirements Development” .

</details>

<a id="tag_07_03_02"></a>
## 7.3.2. Develop Baseline Application Architecture Description

概念：应用基线深度依保留应用和已有描述决定。

适用条件：现状需支撑目标应用。

逻辑关系：复用库应用块；未入库应用需按应用组合目录定义，新增模型按首步所选视点。

决策方法：确认现有应用定义与目录一致。

制品及证据：基线应用描述、组合目录和模型。

适用边界：实际应用存在不代表目录信息当前准确。

来源块：C220-web-2025:02-architecture-development-method:b00657, C220-web-2025:02-architecture-development-method:b00658, C220-web-2025:02-architecture-development-method:b00659

<details><summary>展开本节完整英文来源</summary>

7.3.2. Develop Baseline Application Architecture Description

Develop a Baseline Description of the existing Application Architecture, to the extent necessary to support the Target Application Architecture.
The scope and level of detail to be defined will depend on the extent to which existing applications are likely to be carried over into the Target Application Architecture, and on whether Architecture Descriptions exist, as described in Section 7.5, “Approach” .
To the extent possible, identify the relevant Application Architecture building blocks, drawing on the Architecture Repository (see the TOGAF Standard — Architecture Content ). If not already existing within the Architecture Repository,
define each application in line with the Application Portfolio catalog (see the TOGAF Standard — Architecture Content ).

Where new architecture models need to be developed to satisfy
stakeholder concerns, use the models identified within
the first step in this phase (see Section 7.3.1, “Select Reference Models, Viewpoints, and Tools” )
as a guideline for creating new architecture content to describe the Baseline
Architecture.

</details>

<a id="tag_07_03_03"></a>
## 7.3.3. Develop Target Application Architecture Description

概念：目标应用支撑愿景、目标业务及目标数据。

适用条件：应用元素有目标关联。

逻辑关系：按相关性取细节，复用库，缺关切则补模型；适当讨论备选。

决策方法：选择目标应用块与取舍。

制品及证据：目标应用描述、模型和备选。

适用边界：数据优先不是强制顺序，但目标数据依赖必须协调。

来源块：C220-web-2025:02-architecture-development-method:b00660, C220-web-2025:02-architecture-development-method:b00661, C220-web-2025:02-architecture-development-method:b00662, C220-web-2025:02-architecture-development-method:b00663

<details><summary>展开本节完整英文来源</summary>

7.3.3. Develop Target Application Architecture Description

Develop a Target Description for the Application Architecture, to the
extent necessary to support the Architecture Vision, Target Business
Architecture, and Target Data Architecture. The scope and level of
detail to be defined will depend on the relevance of the application
elements to attaining the Target Architecture Vision, and on whether
architectural descriptions exist. To the extent possible, identify the
relevant Application Architecture building blocks, drawing on the
Architecture Repository (see the TOGAF Standard — Architecture Content ).

Where new architecture models need to be developed to satisfy
stakeholder concerns, use the models identified within
the first step in this phase (see Section 7.3.1, “Select Reference Models, Viewpoints, and Tools” )
as a guideline for creating new architecture content to describe the Target
Architecture.

If appropriate, investigate different Target Architecture alternatives
and discuss these with stakeholders using the Architecture Alternatives
and Trade-offs technique (see the TOGAF Standard — ADM Techniques ).

</details>

<a id="tag_07_03_04"></a>
## 7.3.4. Perform Gap Analysis

概念：应用差距分析必须先核对内部一致性和准确性。

适用条件：基线目标应用模型已形成。

逻辑关系：取舍解决视图冲突、检查原则目标约束、记录参考视点变化并测需求完整，再分析差距。

决策方法：判断应用差距及视图冲突如何处理。

制品及证据：应用模型验证、视点修改、需求完整性与差距。

适用边界：名称集合相等不证明业务语义一致。

来源块：C220-web-2025:02-architecture-development-method:b00664, C220-web-2025:02-architecture-development-method:b00665, C220-web-2025:02-architecture-development-method:b00666, C220-web-2025:02-architecture-development-method:b00667

<details><summary>展开本节完整英文来源</summary>

7.3.4. Perform Gap Analysis

Verify the architecture models for internal consistency and accuracy:

Perform trade-off analysis to resolve conflicts (if any) among the
different views Validate that the models support the principles, objectives, and
constraints Note changes to the viewpoint represented in the selected models from
the Architecture Repository, and document Test architecture models for completeness against requirements

Identify gaps between the baseline and target, using the gap analysis
technique as described in the TOGAF Standard — ADM Techniques .

</details>

<a id="tag_07_03_05"></a>
## 7.3.5. Define Candidate Roadmap Components

概念：初始应用路线图基于基线目标差距并为后续活动排序。

适用条件：域差距已有结果。

逻辑关系：应用路线图是E跨专业综合路线图的原材料。

决策方法：确定候选活动优先顺序。

制品及证据：应用路线图候选组件。

适用边界：局部排序不是最终迁移优先级或资源承诺。

来源块：C220-web-2025:02-architecture-development-method:b00668, C220-web-2025:02-architecture-development-method:b00669, C220-web-2025:02-architecture-development-method:b00670

<details><summary>展开本节完整英文来源</summary>

7.3.5. Define Candidate Roadmap Components

Following the creation of a Baseline Architecture, Target Architecture,
and gap analysis, an application roadmap is required to prioritize
activities over the coming phases.

This initial Application Architecture roadmap will be used as raw
material to support more detailed definition of a consolidated,
cross-discipline roadmap within the Opportunities & Solutions phase.

</details>

<a id="tag_07_03_06"></a>
## 7.3.6. Resolve Impacts Across the Architecture Landscape

概念：应用架构需识别景观范围的双向影响与复用。

适用条件：本域与既有架构和计划/在建项目并存。

逻辑关系：同时检查本域影响他域、近期变化影响本域、他处复用与项目双向影响。

决策方法：逐项识别跨景观依赖与需协调变化。

制品及证据：应用影响分析、复用机会和项目关联。

适用边界：仅检测共享标识一致不足以证明变更影响已覆盖。

来源块：C220-web-2025:02-architecture-development-method:b00671, C220-web-2025:02-architecture-development-method:b00672, C220-web-2025:02-architecture-development-method:b00673, C220-web-2025:02-architecture-development-method:b00674

<details><summary>展开本节完整英文来源</summary>

7.3.6. Resolve Impacts Across the Architecture Landscape

Once the Application Architecture is finalized, it is necessary to
understand any wider impacts or implications.

At this stage, other architecture artifacts in the Architecture
Landscape should be examined to identify:

Does this Application Architecture create an impact on any
pre-existing architectures? Have recent changes been made that impact the Application
Architecture? Are there any opportunities to leverage work from this Application
Architecture in other areas of the organization? Does this Application Architecture impact other projects (including those planned as well as those currently in progress)? Will this Application Architecture be impacted by other projects
(including those planned as well as those currently in progress)?

</details>

<a id="tag_07_03_07"></a>
## 7.3.7. Conduct Formal Stakeholder Review

概念：应用正式复核检验动机说明书并识别业务/数据改动和技术基础设施约束。

适用条件：应用改变表单流程数据系统等。

逻辑关系：影响重大可回访B与数据；技术约束传到即将设计阶段。

决策方法：判断影响显著程度及重访需求。

制品及证据：应用复核、业务数据影响、技术约束。

适用边界：对象同步一致不等于业务实践已适配。

来源块：C220-web-2025:02-architecture-development-method:b00675, C220-web-2025:02-architecture-development-method:b00676, C220-web-2025:02-architecture-development-method:b00677

<details><summary>展开本节完整英文来源</summary>

7.3.7. Conduct Formal Stakeholder Review

Check the original motivation for the architecture project and the
Statement of Architecture Work against the proposed Application
Architecture. Conduct an impact analysis, to identify any areas where
the Business and Data Architectures (e.g., business practices) may need
to change to cater for changes in the Application Architecture (for
example, changes to forms or procedures, applications, or database
systems). If the impact is significant, this may warrant the Business
and Data Architectures being revisited.

Identify any constraints on the Technology Architecture (especially the
infrastructure) about to be designed.

</details>

<a id="tag_07_03_08"></a>
## 7.3.8. Finalize the Application Architecture

概念：完成应用块标准、完整描述、最终追溯和库映射。

适用条件：应用架构收尾。

逻辑关系：复用选定参考标准，总核验业务要求/目标，记录块决定理由，发布可复用块并关闭差距等工作。

决策方法：确认块标准、业务适配和可复用发布。

制品及证据：应用块描述、标准/理由、追溯报告、库映射和最终产品。

适用边界：发布经过治理，不以文件存在自动认定正式完成。

来源块：C220-web-2025:02-architecture-development-method:b00678, C220-web-2025:02-architecture-development-method:b00679

<details><summary>展开本节完整英文来源</summary>

7.3.8. Finalize the Application Architecture

Select standards for each of the building blocks, re-using as much as
possible from the reference models selected from the Architecture
Repository Fully document each building block Conduct a final cross-check of overall architecture against business
requirements; document the rationale for building block decisions in the
architecture document Document the final requirements traceability report Document the final mapping of the architecture within the Architecture
Repository; from the selected building blocks, identify those that might
be re-used, and publish via the Architecture Repository Finalize all the work products, such as gap analysis

</details>

<a id="tag_07_03_09"></a>
## 7.3.9. Create/Update the Architecture Definition Document

概念：定义文档应用部分应记录块决定理由和关键视图。

适用条件：发布应用架构。

逻辑关系：工具报表图可辅助相关方复核并纳入反馈。

决策方法：准备适用应用章节并处理反馈。

制品及证据：应用定义章节、决策理由和复核。

适用边界：自动报告不自动取得正式发布/批准状态。

来源块：C220-web-2025:02-architecture-development-method:b00680, C220-web-2025:02-architecture-development-method:b00681

<details><summary>展开本节完整英文来源</summary>

7.3.9. Create/Update the Architecture Definition Document

Document the rationale for building block decisions in the
Architecture Definition Document Prepare the Application Architecture sections of the Architecture Definition Document; if appropriate, use reports and/or graphics generated by modeling tools to demonstrate key views of the architecture; route the document for review by relevant stakeholders, incorporate feedback

</details>

<a id="tag_07_04"></a>
## 7.4. Outputs

概念：应用输出包括获批目标/条件性获批基线、原则、互操作要求和路线图。

适用条件：交付C应用结果。

逻辑关系：定义和要求整体仍草稿；需要时更新A材料、业务/数据要求，给技术约束。

决策方法：维护状态并传递跨域要求。

制品及证据：应用定义/要求、原则、互操作和路线图组件。

适用边界：may include不是所有项目均必须产出全部项。

来源块：C220-web-2025:02-architecture-development-method:b00682, C220-web-2025:02-architecture-development-method:b00683, C220-web-2025:02-architecture-development-method:b00684, C220-web-2025:02-architecture-development-method:b00685

<details><summary>展开本节完整英文来源</summary>

7.4. Outputs

The outputs of Phase C (Application Architecture) may include, but are
not restricted to:

Refined and updated versions of the Architecture Vision phase
deliverables, where applicable: Statement of Architecture Work (see the TOGAF Standard — Architecture Content ), updated if necessary Validated application principles, or new application principles (if
generated here) Draft Architecture Definition Document (see the TOGAF Standard — Architecture Content ), including: Baseline Application Architecture, Approved, if appropriate Target Application Architecture, Approved Views corresponding to the selected viewpoints, addressing key
stakeholder concerns Draft Architecture Requirements Specification (see the TOGAF Standard — Architecture Content ), including such Application Architecture requirements as: Gap analysis results Applications interoperability requirements Relevant technical requirements that will apply to this evolution of
the architecture development cycle Constraints on the Technology Architecture about to be designed Updated business requirements, if appropriate Updated data requirements, if appropriate Application Architecture components of an Architecture Roadmap (see
the TOGAF Standard — Architecture Content )

The TOGAF Standard — Architecture Content contains a detailed description of architectural
artifacts which might be produced in this phase.

</details>

<a id="tag_07_05"></a>
## 7.5. Approach

概念：本标题为结构容器，无独立说明段落。

适用条件：阅读该主题时应继续读取下列子节。

逻辑关系：子节分工：tag_07_05_01: 7.5.1. Architecture Repository

决策方法：不从空容器推出附加规则或完成状态。

制品及证据：实际概念、决策和制品证据见上述子节。

适用边界：空容器覆盖仅证明目录和子节连接，不计额外深度结论。

来源块：C220-web-2025:02-architecture-development-method:b00686

<details><summary>展开本节完整英文来源</summary>

7.5. Approach

</details>

<a id="tag_07_05_01"></a>
## 7.5.1. Architecture Repository

概念：应用库参考包括行业业务/应用模型、电子商务和供应链等常用功能模型。

适用条件：寻找应用层整合信息基础设施参考。

逻辑关系：III-RM聚焦应用组件与服务，可作为参考资源。

决策方法：判断通用功能和行业模型相关性。

制品及证据：应用参考模型与选择依据。

适用边界：本目录未因此完成III-RM外部资料解析，不把引用当成已审全文。

来源块：C220-web-2025:02-architecture-development-method:b00687, C220-web-2025:02-architecture-development-method:b00688, C220-web-2025:02-architecture-development-method:b00689, C220-web-2025:02-architecture-development-method:b00690

<details><summary>展开本节完整英文来源</summary>

7.5.1. Architecture Repository

As part of this phase, the architecture team will need to consider what
relevant Application Architecture resources are available in the
Architecture Repository (see the TOGAF Standard — Architecture Content ).
In particular:

Generic business models and related application models relevant to the
organization’s industry sector Application models relevant to common high-level business functions,
such as electronic commerce, supply chain management, etc.

The Open Group has a Reference Model for Integrated Information
Infrastructure (III-RM) — see the TOGAF ® Series Guide: The TOGAF Integrated Information Infrastructure Reference Model (III-RM) — that focuses on the application-level components and services necessary to
provide an integrated information infrastructure.

</details>

<a id="chap08"></a>
## 8. Phase D: Technology Architecture

概念：本章开发技术架构。

适用条件：需要技术域支撑愿景及业务时。

逻辑关系：技术描述与其他域共同形成信息系统或技术架构。

决策方法：确定本轮技术工作边界。

制品及证据：技术基线/目标与工作结果。

适用边界：域开发不能脱离已批准工作范围。

来源块：C220-web-2025:02-architecture-development-method:b00691, C220-web-2025:02-architecture-development-method:b00692, C220-web-2025:02-architecture-development-method:b00693, C220-web-2025:02-architecture-development-method:b00694

<details><summary>展开本节完整英文来源</summary>

8. Phase D: Technology Architecture

This chapter describes the development of a Technology Architecture for
an architecture project.



Figure 8-1: Phase D: Technology Architecture

</details>

<a id="tag_08_01"></a>
## 8.1. Objectives

概念：目标技术架构支撑愿景及目标业务/数据/应用构建块，通过技术组件与服务交付，基线目标差距产生路线图候选。

适用条件：工作说明书和相关方关切确定后。

逻辑关系：技术变更须连接业务支持和价值。

决策方法：核验目标技术满足愿景/工作关切。

制品及证据：目标技术架构与候选组件。

适用边界：候选组件不等于已批准跨域实施计划。

来源块：C220-web-2025:02-architecture-development-method:b00695, C220-web-2025:02-architecture-development-method:b00696, C220-web-2025:02-architecture-development-method:b00697

<details><summary>展开本节完整英文来源</summary>

8.1. Objectives

The objectives of Phase D are to:

Develop the Target Technology Architecture that enables the
Architecture Vision, target business, data, and application building
blocks to be delivered through technology components and technology
services, in a way that addresses the Statement of Architecture Work and
stakeholder concerns Identify candidate Architecture Roadmap components based upon gaps
between the Baseline and Target Technology Architectures

</details>

<a id="tag_08_02"></a>
## 8.2. Inputs

概念：技术输入按外部、非架构和架构资料分类。

适用条件：启动技术开发时。

逻辑关系：8.2.1—8.2.3给出三类具体输入。

决策方法：确认各类资料及状态。

制品及证据：技术输入来源与状态清单。

适用边界：导航不证明输入完整。

来源块：C220-web-2025:02-architecture-development-method:b00698, C220-web-2025:02-architecture-development-method:b00699

<details><summary>展开本节完整英文来源</summary>

8.2. Inputs

This section defines the inputs to Phase D.

</details>

<a id="tag_08_02_01"></a>
## 8.2.1. Reference Materials External to the Enterprise

概念：技术外部参考包括架构参考及候选产品信息。

适用条件：选择技术参考时。

逻辑关系：参考为模式与约束信息来源，仍需按业务需求评估。

决策方法：判断外部资源适用性。

制品及证据：架构参考及候选产品信息及出处。

适用边界：外部内容不自动成为当前目标架构。

来源块：C220-web-2025:02-architecture-development-method:b00700, C220-web-2025:02-architecture-development-method:b00701

<details><summary>展开本节完整英文来源</summary>

8.2.1. Reference Materials External to the Enterprise

Architecture reference materials (see the TOGAF Standard — Architecture Content ) Product information on candidate products

</details>

<a id="tag_08_02_02"></a>
## 8.2.2. Non-Architectural Inputs

概念：技术非架构输入为工作请求、能力评估和沟通计划。

适用条件：安排技术工作与参与条件。

逻辑关系：业务任务、能力和沟通影响域分析。

决策方法：确认任务与人员参与及能力条件。

制品及证据：工作请求、能力评估、沟通计划。

适用边界：已识别能力缺口持续保留，不能默认消除。

来源块：C220-web-2025:02-architecture-development-method:b00702, C220-web-2025:02-architecture-development-method:b00703

<details><summary>展开本节完整英文来源</summary>

8.2.2. Non-Architectural Inputs

Request for Architecture Work (see the TOGAF Standard — Architecture Content ) Capability Assessment (see the TOGAF Standard — Architecture Content ) Communications Plan (see the TOGAF Standard — Architecture Content )

</details>

<a id="tag_08_02_03"></a>
## 8.2.3. Architectural Inputs

概念：技术架构输入继承组织模型、裁剪框架、说明书愿景、库、现有技术原则（如有）。

适用条件：开展技术域细化。

逻辑关系：B、数据、应用差距与先前技术要求，以及三域路线图组件

决策方法：检查上游要求、已有块与路线图是否适用且当前。

制品及证据：B、数据、应用差距与先前技术要求，以及三域路线图组件及草稿定义/要求文档。

适用边界：if existing/if available保留条件性，不能伪造缺失输入。

来源块：C220-web-2025:02-architecture-development-method:b00704, C220-web-2025:02-architecture-development-method:b00705

<details><summary>展开本节完整英文来源</summary>

8.2.3. Architectural Inputs

Organizational Model for Enterprise Architecture (see the TOGAF Standard — Architecture Content ), including: Scope of organizations impacted Maturity assessment, gaps, and resolution approach Roles and responsibilities for architecture team(s) Constraints on architecture work Budget requirements Governance and support strategy Tailored Architecture Framework (see the TOGAF Standard — Architecture Content ), including: Tailored architecture method Tailored architecture content (deliverables and artifacts) Configured and deployed tools Technology principles (see the TOGAF Standard — ADM Techniques ), if existing Statement of Architecture Work (see the TOGAF Standard — Architecture Content ) Architecture Vision (see the TOGAF Standard — Architecture Content ) Architecture Repository (see the TOGAF Standard — Architecture Content ), including: Re-usable building blocks Publicly available reference models Organization-specific reference models Organization standards Draft Architecture Definition Document, which may include Baseline
and/or Target Architectures of any architecture domain Draft Architecture Requirements Specification (see the TOGAF Standard — Architecture Content ), including: Gap analysis results (from Business, Data, and Application
Architectures) Relevant technical requirements from previous phases Business, Data, and Application Architecture components of an
Architecture Roadmap (see the TOGAF Standard — Architecture Content )

</details>

<a id="tag_08_03"></a>
## 8.3. Steps

概念：技术开发九步以总体范围目标确定细节。

适用条件：新技术块或已有块需支持目标时。

逻辑关系：新技术块详细定义；保留技术块可能需重新定义以确保本次互操作和用途适合；基线/目标可先行任一，启动活动在8.3.8关闭，文档在8.3.9正式发布。

决策方法：按治理调整顺序、起止和所需深度。

制品及证据：技术开发步骤、收尾和发布记录。

适用边界：可迭代不免除收尾和正式发布要求。

来源块：C220-web-2025:02-architecture-development-method:b00706, C220-web-2025:02-architecture-development-method:b00707, C220-web-2025:02-architecture-development-method:b00708, C220-web-2025:02-architecture-development-method:b00709, C220-web-2025:02-architecture-development-method:b00710, C220-web-2025:02-architecture-development-method:b00711

<details><summary>展开本节完整英文来源</summary>

8.3. Steps

The level of detail addressed in Phase D will depend on the scope and
goals of the overall architecture effort.

New technology building blocks being introduced as part of this effort
will need to be defined in detail during Phase D. Existing technology
building blocks to be supported in the target environment may need to be
redefined in Phase D to ensure interoperability and fit-for-purpose
within this specific Technology Architecture.

The order of the steps in Phase D as well as the time at which they are
formally started and completed should be adapted to the situation at
hand in accordance with the established Architecture Governance. In
particular, determine whether it is appropriate to
conduct Baseline Description or Target Architecture development first,
as described in the TOGAF Standard — Applying the ADM .

All activities that have been initiated in these steps should be closed
during the Finalize the Technology Architecture step; see Section 8.3.8, “Finalize the Technology Architecture” .
The documentation generated from these steps must be formally published in
the Create/Update the Architecture Definition Document step; see Section 8.3.9, “Create/Update the Architecture Definition Document” . The steps in Phase D are as follows:

Select reference models, viewpoints, and tools; see Section 8.3.1, “Select Reference Models, Viewpoints, and Tools” Develop Baseline Technology Architecture Description; see Section 8.3.2, “Develop Baseline Technology Architecture Description” Develop Target Technology Architecture Description; see Section 8.3.3, “Develop Target Technology Architecture Description” Perform gap analysis; see Section 8.3.4, “Perform Gap Analysis” Define candidate roadmap components; see Section 8.3.5, “Define Candidate Roadmap Components” Resolve impacts across the Architecture Landscape; see Section 8.3.6, “Resolve Impacts Across the Architecture Landscape” Conduct formal stakeholder review; see Section 8.3.7, “Conduct Formal Stakeholder Review” Finalize the Technology Architecture; see Section 8.3.8, “Finalize the Technology Architecture” Create/Update the Architecture Definition Document; see Section 8.3.9, “Create/Update the Architecture Definition Document”

</details>

<a id="tag_08_03_01"></a>
## 8.3.1. Select Reference Models, Viewpoints, and Tools

概念：技术原则、参考、视点和工具根据业务驱动及相关方关切选择。

适用条件：开始技术模型捕获分析。

逻辑关系：工具复杂程度随需要，原则属于整体原则集。

决策方法：验证原则并选择关切对应视点。

制品及证据：技术原则、参考、视点及工具。

适用边界：技术选择仍要回应业务需求。

来源块：C220-web-2025:02-architecture-development-method:b00712, C220-web-2025:02-architecture-development-method:b00713, C220-web-2025:02-architecture-development-method:b00714, C220-web-2025:02-architecture-development-method:b00715, C220-web-2025:02-architecture-development-method:b00716

<details><summary>展开本节完整英文来源</summary>

8.3.1. Select Reference Models, Viewpoints, and Tools

Review and validate the set of technology principles. These will
normally form part of an overarching set of Architecture Principles.
Guidelines for developing and applying principles, and a sample set of
technology principles, are given in the TOGAF Standard — ADM Techniques .

Select relevant Technology Architecture resources (reference models,
patterns, etc.) from the Architecture Repository (see the TOGAF Standard — Architecture Content ), on the basis of the business drivers, stakeholders, and their
concerns.

Select relevant Technology Architecture viewpoints that will enable the
architect to demonstrate how the stakeholder concerns are being
addressed in the Technology Architecture.

Identify appropriate tools and techniques to be used for capture,
modeling, and analysis, in association with the selected viewpoints.
Depending on the degree of sophistication required, these may comprise
simple documents and spreadsheets, or more sophisticated modeling tools
and techniques.

</details>

<a id="tag_08_03_01_01"></a>
## 8.3.1.1. Determine Overall Modeling Process

概念：技术建模从服务/逻辑组件分类、部署地点和物理清单开始。

适用条件：评估现有技术是否满足功能与非功能要求。

逻辑关系：分类→需求核验→调整分类→产品/依赖选择与配置→规模成本容量安装治理迁移影响；服务粒度影响性能维护时延可用性。

决策方法：现有复用、增量容量或初始产品约束可在D选择；偏标准、费力或广泛影响的产品选择转E为机会。

制品及证据：技术分类/清单、需求适配、产品配置、容量成本及影响分析。

适用边界：不能把所有采购强制归D或禁止D选产品；容量无数据保持未知。

来源块：C220-web-2025:02-architecture-development-method:b00717, C220-web-2025:02-architecture-development-method:b00718, C220-web-2025:02-architecture-development-method:b00719, C220-web-2025:02-architecture-development-method:b00720, C220-web-2025:02-architecture-development-method:b00721, C220-web-2025:02-architecture-development-method:b00722, C220-web-2025:02-architecture-development-method:b00723, C220-web-2025:02-architecture-development-method:b00724

<details><summary>展开本节完整英文来源</summary>

8.3.1.1. Determine Overall Modeling Process

For each viewpoint, select the models needed to support the specific
view required, using the selected tool or method. Ensure that all
stakeholder concerns are covered. If they are not, create new models to
address them, or augment existing models (see above).

The process to develop a Technology Architecture incorporates the
following steps:

Define a taxonomy of technology services and logical technology
components (including standards) Identify relevant locations where technology is deployed Carry out a physical inventory of deployed technology and abstract up
to fit into the taxonomy Look at application and business requirements for technology Is the technology in place fit-for-purpose to meet new requirements
(i.e., does it meet functional and non-functional requirements)? Refine the taxonomy Product selection (including dependent products) Determine configuration of the selected technology Determine impact: Sizing and costing Capacity planning Installation/governance/migration impacts

In the earlier phases of the ADM, certain decisions made around service
granularity and service boundaries will have implications on the
technology component and the technology service. The areas where the
Technology Architecture may be impacted will include the following:

Performance : the granularity of the service will impact on
technology service requirements Coarse-grained services contain several units of functionality with
potentially varying non-functional requirements, so platform performance
should be considered. In addition, coarse-grained services can sometimes
contain more information than actually required by the requesting
system. Maintainability : if service granularity is too coarse, then
introducing changes to that service becomes difficult and impacts the
maintenance of the service and the platform on which it is delivered Location and Latency : services might interact with each other over
remote links and inter-service communication will have in-built latency Drawing service boundaries and setting the service granularity should
consider platform/location impact of these inter-service communications. Availability : service invocation is subject to network and/or
service failure High communication availability is an important consideration during
service decomposition and defining service granularity.

Product selection processes may occur within the Technology Architecture
phase where existing products are re-used, incremental capacity is being
added, or product selection decisions are a constraint during project
initiation.

Where product selection deviates from existing standards, involves
significant effort, or has wide-ranging impact, this activity should be
flagged as an opportunity and addressed through the Opportunities &
Solutions phase.

</details>

<a id="tag_08_03_01_02"></a>
## 8.3.1.2. Identify Required Catalogs of Technology Building Blocks

概念：技术目录表达服务→逻辑技术组件→物理技术组件等层次。

适用条件：根据应用需求盘点产品及标准符合性。

逻辑关系：已有产品不满足要求时调查满足功能标准的市场产品，分类必要时扩展，既有标准应用于目录基线。

决策方法：选择需扩展产品清单和分类。

制品及证据：技术组件/产品目录、分类和标准符合性基线。

适用边界：产品列表不是采购批准或真实性能证明。

来源块：C220-web-2025:02-architecture-development-method:b00725, C220-web-2025:02-architecture-development-method:b00726, C220-web-2025:02-architecture-development-method:b00727, C220-web-2025:02-architecture-development-method:b00728, C220-web-2025:02-architecture-development-method:b00729, C220-web-2025:02-architecture-development-method:b00730

<details><summary>展开本节完整英文来源</summary>

8.3.1.2. Identify Required Catalogs of Technology Building Blocks

Catalogs are inventories of the core assets of the business. Catalogs
are hierarchical in nature and capture a decomposition of a metamodel
entity and also decompositions across related model entities (e.g.,
technology service → logical technology component → physical
technology component).

Catalogs form the raw material for development of matrices and diagrams
and also act as a key resource for managing the business and IT
capability.

The Technology Architecture should create technology catalogs as
follows:

Based on existing technology catalogs and analysis of applications
carried out in the Application Architecture phase, collect a list of
products in use If the requirements identified in the Application Architecture are not
met by existing products, extend the product list by examining products
available on the market that provide the functionality and meet the
required standards Classify products against the selected taxonomy if appropriate,
extending the model as necessary to fit the classification of technology
products in use If technology standards are currently in place, apply these to the
technology component catalog to gain a baseline view of compliance with
technology standards

The TOGAF Standard — Architecture Content contains a detailed description of catalogs which
should be considered for development within a Technology Architecture,
describing them in detail and relating them to entities, attributes, and
relationships in the TOGAF Enterprise Metamodel.

</details>

<a id="tag_08_03_01_03"></a>
## 8.3.1.3. Identify Required Matrices

概念：技术矩阵表示核心模型实体关系并支撑图和影响评估。

适用条件：技术对象需跨实体关系分析。

逻辑关系：矩阵关系可驱动视图与变更影响。

决策方法：选择满足当前关切的矩阵。

制品及证据：技术关系矩阵与元模型映射。

适用边界：矩阵格不能默认无语义或自动数值评级。

来源块：C220-web-2025:02-architecture-development-method:b00731, C220-web-2025:02-architecture-development-method:b00732, C220-web-2025:02-architecture-development-method:b00733, C220-web-2025:02-architecture-development-method:b00734

<details><summary>展开本节完整英文来源</summary>

8.3.1.3. Identify Required Matrices

Matrices show the core relationships between related model entities.

Matrices form the raw material for development of diagrams and also act
as a key resource for impact assessment.

The TOGAF Standard — Architecture Content contains a detailed description of matrices which
should be considered for development within a Technology Architecture,
describing them in detail and relating them to entities, attributes, and
relationships in the TOGAF Enterprise Metamodel.

</details>

<a id="tag_08_03_01_04"></a>
## 8.3.1.4. Identify Required Diagrams

概念：技术图连接平台与托管环境，应用可位于多环境。

适用条件：部署、开发生命周期或本地访问要求不同。

逻辑关系：主要平台栈图含硬件OS基础软件应用；各环境需逻辑基础设施通信和物理网络图，可用时收集容量。

决策方法：决定环境分布、应用平台映射及需容量证据。

制品及证据：栈图、分布图、环境逻辑/物理网络图、可得容量。

适用边界：容量信息where available是条件，不得用自动值补缺；通信线需依据。

来源块：C220-web-2025:02-architecture-development-method:b00735, C220-web-2025:02-architecture-development-method:b00736, C220-web-2025:02-architecture-development-method:b00737, C220-web-2025:02-architecture-development-method:b00738, C220-web-2025:02-architecture-development-method:b00739, C220-web-2025:02-architecture-development-method:b00740, C220-web-2025:02-architecture-development-method:b00741, C220-web-2025:02-architecture-development-method:b00742

<details><summary>展开本节完整英文来源</summary>

8.3.1.4. Identify Required Diagrams

Diagrams present the Technology Architecture information from a set of
different perspectives (viewpoints) according to the requirements of the
stakeholders.

This activity provides a link between platform requirements and hosting
requirements, as a single application may need to be physically located
in several environments to support local access, development lifecycles,
and hosting requirements.

For major baseline applications or application platforms (where multiple
applications are hosted on the same infrastructure stack), produce a
stack diagram showing how hardware, operating system, software
infrastructure, and packaged applications combine.

If appropriate, extend the Application Architecture diagrams of software
distribution to show how applications map onto the technology platform.

For each environment, produce a logical diagram of hardware and software
infrastructure showing the contents of the environment and logical
communications between components. Where available, collect capacity
information on the deployed infrastructure.

For each environment, produce a physical diagram of communications
infrastructure, such as routers, switches, firewalls, and network links.
Where available, collect capacity information on the communications
infrastructure.

The TOGAF Standard — Architecture Content contains a detailed description of diagrams which
should be considered for development within a Technology Architecture,
describing them in detail and relating them to entities, attributes, and
relationships in the TOGAF Enterprise Metamodel.

</details>

<a id="tag_08_03_01_05"></a>
## 8.3.1.5. Identify Types of Requirement to be Collected

概念：技术聚焦要求在目录矩阵图后正式化。

适用条件：目标技术实施需设计指导。

逻辑关系：技术域要求约束后续设计实施以满足原架构要求。

决策方法：识别需由技术架构满足的要求。

制品及证据：技术要求和设计实施指导。

适用边界：平台配置本身不等于要求满足证据。

来源块：C220-web-2025:02-architecture-development-method:b00743, C220-web-2025:02-architecture-development-method:b00744, C220-web-2025:02-architecture-development-method:b00745, C220-web-2025:02-architecture-development-method:b00746, C220-web-2025:02-architecture-development-method:b00747

<details><summary>展开本节完整英文来源</summary>

8.3.1.5. Identify Types of Requirement to be Collected

Once the Technology Architecture catalogs, matrices, and diagrams have
been developed, architecture modeling is completed by formalizing the
technology-focused requirements for implementing the Target Architecture.

These requirements may:

Relate to the technology domain Provide detailed guidance to be reflected during design and
implementation to ensure that the solution addresses the original
architecture requirements

Within this step, the architect should identify requirements that should
be met by the architecture; see Section 13.5.2, “Requirements Development” .

</details>

<a id="tag_08_03_01_06"></a>
## 8.3.1.6. Select Services

概念：每块技术服务组合必须互不冲突且满足应用要求。

适用条件：完整架构定义之前选择服务。

逻辑关系：要求纳入组织既有不变元素/决策和外部约束；专门服务可考虑未来标准服务替换。

决策方法：构造每块服务描述组合并测试应用功能支持。

制品及证据：服务组合、测试、专用服务替换考虑。

适用边界：分类相同不自动证明组合无冲突。

来源块：C220-web-2025:02-architecture-development-method:b00748, C220-web-2025:02-architecture-development-method:b00749, C220-web-2025:02-architecture-development-method:b00750, C220-web-2025:02-architecture-development-method:b00751, C220-web-2025:02-architecture-development-method:b00752, C220-web-2025:02-architecture-development-method:b00753

<details><summary>展开本节完整英文来源</summary>

8.3.1.6. Select Services

The services portfolios are combinations of basic services from the
service categories in the defined taxonomy that do not conflict. The
combination of services are again tested to ensure support for the
applications. This is a prerequisite to the later step of defining the
architecture fully.

The previously identified requirements can provide more detailed
information about:

Requirements for organization-specific elements or pre-existing
decisions (as applicable) Pre-existing and unchanging organizational elements (as applicable) Inherited external environment constraints

Where requirements demand definition of specialized services that are
not identified in the TOGAF Standard, consideration should be given to
how these might be replaced if standardized services become available in
the future.

For each building block, build up a service description portfolio as a
set of non-conflicting services. The set of services must be tested to
ensure that the functionality provided meets application requirements.

</details>

<a id="tag_08_03_02"></a>
## 8.3.2. Develop Baseline Technology Architecture Description

概念：技术基线将已有环境转译为组织技术服务/组件分类。

适用条件：支持目标且已有技术需保留。

逻辑关系：复用库，适配旧描述，设关键问题以衡量新架构有效性，缺模型则按首步新建。

决策方法：选基线细节并核实分类与测量问题。

制品及证据：技术基线、分类、关键问题及目录。

适用边界：源文b00756写define each application in line with Technology Portfolio catalog，疑似沿用应用措辞；保留原文，不能推断应用=技术组件。

来源块：C220-web-2025:02-architecture-development-method:b00754, C220-web-2025:02-architecture-development-method:b00755, C220-web-2025:02-architecture-development-method:b00756, C220-web-2025:02-architecture-development-method:b00757, C220-web-2025:02-architecture-development-method:b00758

<details><summary>展开本节完整英文来源</summary>

8.3.2. Develop Baseline Technology Architecture Description

Develop a Baseline Description of the existing Technology Architecture,
to support the Target Technology Architecture. The scope and level of
detail to be defined will depend on the extent to which existing
technology components are likely to be carried over into the Target
Technology Architecture, and on whether architectural descriptions
exist, as described in Section 8.5, “Approach” .

Identify the relevant Technology Architecture building blocks, drawing on any artifacts held in the Architecture Repository. If nothing exists
within the Architecture Repository, define each application in line with the Technology Portfolio catalog (see the TOGAF Standard — Architecture Content ).

Begin by converting the description of the existing environment into the
terms of the organization’s taxonomy of technology services and
technology components (e.g., the TOGAF Technical Reference Model (TRM)).
This will allow the team developing the architecture to gain experience
and understanding of the taxonomy. The team may be able to take
advantage of a previous architectural definition, but it is assumed that
some adaptation may be required to match the architectural definition
techniques described as part of this process. Another important task is
to set down a list of key questions which can be used later in the
development process to measure the effectiveness of the new
architecture.

Where new architecture models need to be developed to satisfy
stakeholder concerns, use the models identified within
the first step in this phase (see Section 8.3.1, “Select Reference Models, Viewpoints, and Tools” )
as a
guideline for creating new architecture content to describe the Baseline
Architecture.

</details>

<a id="tag_08_03_03"></a>
## 8.3.3. Develop Target Technology Architecture Description

概念：目标技术支撑愿景、业务和信息系统架构；ABBs描述功能及可能实现。

适用条件：形成目标总体架构模型。

逻辑关系：块概念化不带配置或详细设计；按关切补模型并适当讨论备选。

决策方法：选择技术ABBs与目标取舍。

制品及证据：目标技术描述、ABBs、模型与备选。

适用边界：ABBs不能直接当作配置完毕SBB或具体采购产品。

来源块：C220-web-2025:02-architecture-development-method:b00759, C220-web-2025:02-architecture-development-method:b00760, C220-web-2025:02-architecture-development-method:b00761, C220-web-2025:02-architecture-development-method:b00762

<details><summary>展开本节完整英文来源</summary>

8.3.3. Develop Target Technology Architecture Description

Develop a Target Description for the Technology Architecture, to the
extent necessary to support the Architecture Vision, Target Business
Architecture, and Target Information Systems Architecture. The scope and
level of detail to be defined will depend on the relevance of the
technology elements to attaining the Target Architecture, and on whether
architectural descriptions exist. To the extent possible, identify the
relevant Technology Architecture building blocks, drawing on the
Architecture Repository (see the TOGAF Standard — Architecture Content ).

A key process in the creation of a broad architectural model of the
target system is the conceptualization of building blocks. ABBs describe
the functionality and how they may be implemented without the detail
introduced by configuration or detailed design. The method of defining
building blocks, along with some general guidelines for their use in
creating an architectural model, is described in the TOGAF Standard — Architecture Content .

Where new architecture models need to be developed to satisfy
stakeholder concerns, use the models identified within
the first step in this phase (see Section 8.3.1, “Select Reference Models, Viewpoints, and Tools” )
as a guideline for creating new architecture content to describe the Target
Architecture. If appropriate, investigate different Target Architecture alternatives
and discuss these with stakeholders using the Architecture Alternatives
and Trade-offs technique (see the TOGAF Standard — ADM Techniques ).

</details>

<a id="tag_08_03_04"></a>
## 8.3.4. Perform Gap Analysis

概念：技术差距分析必须先核对内部一致性和准确性。

适用条件：基线目标技术模型已形成。

逻辑关系：取舍解决视图冲突、检查原则目标约束、记录参考视点变化并测需求完整，再分析差距。

决策方法：判断技术差距及视图冲突如何处理。

制品及证据：技术模型验证、视点修改、需求完整性与差距。

适用边界：名称集合相等不证明业务语义一致。

来源块：C220-web-2025:02-architecture-development-method:b00763, C220-web-2025:02-architecture-development-method:b00764, C220-web-2025:02-architecture-development-method:b00765, C220-web-2025:02-architecture-development-method:b00766

<details><summary>展开本节完整英文来源</summary>

8.3.4. Perform Gap Analysis

Verify the architecture models for internal consistency and accuracy:

Perform trade-off analysis to resolve conflicts (if any) among the
different views Validate that the models support the principles, objectives, and
constraints Note changes to the viewpoint represented in the selected models from
the Architecture Repository, and document Test architecture models for completeness against requirements

Identify gaps between the baseline and target, using the gap analysis
technique as described in the TOGAF Standard — ADM Techniques .

</details>

<a id="tag_08_03_05"></a>
## 8.3.5. Define Candidate Roadmap Components

概念：初始技术路线图基于基线目标差距并为后续活动排序。

适用条件：域差距已有结果。

逻辑关系：技术路线图是E跨专业综合路线图的原材料。

决策方法：确定候选活动优先顺序。

制品及证据：技术路线图候选组件。

适用边界：局部排序不是最终迁移优先级或资源承诺。

来源块：C220-web-2025:02-architecture-development-method:b00767, C220-web-2025:02-architecture-development-method:b00768, C220-web-2025:02-architecture-development-method:b00769

<details><summary>展开本节完整英文来源</summary>

8.3.5. Define Candidate Roadmap Components

Following the creation of a Baseline Architecture, Target Architecture,
and gap analysis, a Technology Roadmap is required to prioritize
activities over the coming phases.

This initial Technology Architecture roadmap will be used as raw
material to support more detailed definition of a consolidated,
cross-discipline roadmap within the Opportunities & Solutions phase.

</details>

<a id="tag_08_03_06"></a>
## 8.3.6. Resolve Impacts Across the Architecture Landscape

概念：技术架构需识别景观范围的双向影响与复用。

适用条件：本域与既有架构和计划/在建项目并存。

逻辑关系：同时检查本域影响他域、近期变化影响本域、他处复用与项目双向影响。

决策方法：逐项识别跨景观依赖与需协调变化。

制品及证据：技术影响分析、复用机会和项目关联。

适用边界：仅检测共享标识一致不足以证明变更影响已覆盖。

来源块：C220-web-2025:02-architecture-development-method:b00770, C220-web-2025:02-architecture-development-method:b00771, C220-web-2025:02-architecture-development-method:b00772, C220-web-2025:02-architecture-development-method:b00773

<details><summary>展开本节完整英文来源</summary>

8.3.6. Resolve Impacts Across the Architecture Landscape

Once the Technology Architecture is finalized, it is necessary to
understand any wider impacts or implications.

At this stage, other architecture artifacts in the Architecture
Landscape should be examined to identify:

Does this Technology Architecture create an impact on any pre-existing
architectures? Have recent changes been made that impact the Technology Architecture? Are there any opportunities to leverage work from this Technology
Architecture in other areas of the organization? Does this Technology Architecture impact other projects (including those planned as well as those currently in progress)? Will this Technology Architecture be impacted by other projects
(including those planned as well as those currently in progress)?

</details>

<a id="tag_08_03_07"></a>
## 8.3.7. Conduct Formal Stakeholder Review

概念：技术正式复核以原动机和说明书检验适合后续域工作。

适用条件：拟定技术架构需要相关方验核。

逻辑关系：只在必要时细化拟议技术描述。

决策方法：判断技术方案fit-for-purpose。

制品及证据：正式复核及必要修订。

适用边界：语法正确的图不能代替关切和用途验核。

来源块：C220-web-2025:02-architecture-development-method:b00774, C220-web-2025:02-architecture-development-method:b00775

<details><summary>展开本节完整英文来源</summary>

8.3.7. Conduct Formal Stakeholder Review

Check the original motivation for the architecture project and the
Statement of Architecture Work against the proposed Technology
Architecture, asking if it is fit for the purpose of supporting
subsequent work in the other architecture domains. Refine the proposed
Technology Architecture only if necessary.

</details>

<a id="tag_08_03_08"></a>
## 8.3.8. Finalize the Technology Architecture

概念：完成技术块标准、完整描述、最终追溯和库映射。

适用条件：技术架构收尾。

逻辑关系：复用选定参考标准，总核验业务要求/目标，记录块决定理由，发布可复用块并关闭差距等工作。

决策方法：确认块标准、业务适配和可复用发布。

制品及证据：技术块描述、标准/理由、追溯报告、库映射和最终产品。

适用边界：发布经过治理，不以文件存在自动认定正式完成。

来源块：C220-web-2025:02-architecture-development-method:b00776, C220-web-2025:02-architecture-development-method:b00777

<details><summary>展开本节完整英文来源</summary>

8.3.8. Finalize the Technology Architecture

Select standards for each of the building blocks, re-using as much as
possible from the reference models selected from the Architecture
Repository Fully document each building block Conduct a final cross-check of overall architecture against business
goals; document the rationale for building block decisions in the
architecture document Document the final requirements traceability report Document the final mapping of the architecture within the Architecture
Repository; from the selected building blocks, identify those that might
be re-used (working practices, roles, business relationships, job
descriptions, etc.), and publish via the Architecture Repository Finalize all the work products, such as gap analysis

</details>

<a id="tag_08_03_09"></a>
## 8.3.9. Create/Update the Architecture Definition Document

概念：技术定义需无歧义地表达功能属性、安全和可管理性。

适用条件：技术内容正式发布。

逻辑关系：可含依赖块功能/命名接口、API格式协议硬件标准，以及业务组织政策映射，并纳入复核反馈。

决策方法：选适用内容并确认接口/依赖要求明确。

制品及证据：技术定义、接口依赖、政策映射、理由与复核。

适用边界：some or all允许裁剪，但所需接口不能靠图线猜测。

来源块：C220-web-2025:02-architecture-development-method:b00778, C220-web-2025:02-architecture-development-method:b00779, C220-web-2025:02-architecture-development-method:b00780, C220-web-2025:02-architecture-development-method:b00781, C220-web-2025:02-architecture-development-method:b00782

<details><summary>展开本节完整英文来源</summary>

8.3.9. Create/Update the Architecture Definition Document

Document the rationale for building block decisions in the Architecture
Definition Document.

Prepare the technology sections of the Architecture Definition Document,
comprising some or all of:

Fundamental functionality and attributes — semantic, unambiguous
including security capability and manageability Dependent building blocks with required functionality and named
interfaces Interfaces — chosen set, supplied (APIs, data formats, protocols,
hardware interfaces, standards) Map to business/organizational entities and policies

If appropriate, use reports and/or graphics generated by modeling tools
to demonstrate key views of the architecture. Route the document for
review by relevant stakeholders, and incorporate feedback.

</details>

<a id="tag_08_04"></a>
## 8.4. Outputs

概念：D输出目标技术组件平台环境负载网络规格视图，目标可获批而整体定义仍草稿。

适用条件：交付技术阶段。

逻辑关系：要求汇集B/C输出、差距与更新技术要求；必要时更新A材料原则，形成技术路线图组件。

决策方法：标示状态并确认负载和需求证据。

制品及证据：技术定义/要求、原则、路线图和必要A更新。

适用边界：预期负载是需要证据的输入，不是自动容量充分结论。

来源块：C220-web-2025:02-architecture-development-method:b00783, C220-web-2025:02-architecture-development-method:b00784, C220-web-2025:02-architecture-development-method:b00785, C220-web-2025:02-architecture-development-method:b00786

<details><summary>展开本节完整英文来源</summary>

8.4. Outputs

The outputs of Phase D may include, but are not restricted to:

Refined and updated versions of the Architecture Vision phase
deliverables, where applicable: Statement of Architecture Work (see the TOGAF Standard — Architecture Content ), updated if necessary Validated technology principles, or new technology principles (if
generated here) Draft Architecture Definition Document (see the TOGAF Standard — Architecture Content ), including: Baseline Technology Architecture, Approved, if appropriate Target Technology Architecture, Approved, including: Technology Components and their relationships to information systems Technology platforms and their decomposition, showing the
combinations of technology required to realize a particular technology
“stack” Environments and locations — a grouping of the required technology
into computing environments (e.g., development, production) Expected processing load and distribution of load across technology
components Physical (network) communications Hardware and network specifications Views corresponding to the selected viewpoints addressing key
stakeholder concerns Draft Architecture Requirements Specification (see the TOGAF Standard — Architecture Content ), including such Technology Architecture requirements as: Gap analysis results Requirements output from Phases B and C Updated technology requirements Technology Architecture components of an Architecture Roadmap (see the TOGAF Standard — Architecture Content )

The TOGAF Standard — Architecture Content contains a detailed description of architectural
artifacts which might be produced in this phase.

</details>

<a id="tag_08_05"></a>
## 8.5. Approach

概念：本标题为结构容器，无独立说明段落。

适用条件：阅读该主题时应继续读取下列子节。

逻辑关系：子节分工：tag_08_05_01: 8.5.1. Emerging Technologies；tag_08_05_02: 8.5.2. Architecture Repository

决策方法：不从空容器推出附加规则或完成状态。

制品及证据：实际概念、决策和制品证据见上述子节。

适用边界：空容器覆盖仅证明目录和子节连接，不计额外深度结论。

来源块：C220-web-2025:02-architecture-development-method:b00787

<details><summary>展开本节完整英文来源</summary>

8.5. Approach

</details>

<a id="tag_08_05_01"></a>
## 8.5.1. Emerging Technologies

概念：新技术可驱动业务变化，技术架构既响应信息系统又推动业务能力。

适用条件：数字创新和新开发方法改变共享服务与基础设施时。

逻辑关系：业务关切仍领导EA，架构协调整合以防快速技术采用造成企业断裂。

决策方法：识别技术转型机会并与企业方向协调。

制品及证据：技术机会、业务能力关联与变更要求。

适用边界：新技术出现不自动证明组织应采购或转型。

来源块：C220-web-2025:02-architecture-development-method:b00788, C220-web-2025:02-architecture-development-method:b00789, C220-web-2025:02-architecture-development-method:b00790, C220-web-2025:02-architecture-development-method:b00791, C220-web-2025:02-architecture-development-method:b00792

<details><summary>展开本节完整英文来源</summary>

8.5.1. Emerging Technologies

The evolution of new technologies is a major driver for change in
enterprises looking for new innovative ways of operating and improving
their business. The Technology Architecture needs to capture the
transformation opportunities available to the enterprise through the
adoption of new technology.

While the Enterprise Architecture is led by business concerns, drivers
for change are often found within evolving technology capabilities. As
more digital innovations reach the market, stakeholders need to both
anticipate and be open to technology-driven change. Part of Digital
Transformation has arisen due to the convergence of telecommunications
and computer capabilities which have opened up new ways of implementing
infrastructures.

Solution development methods are also evolving to challenge traditional
development methods and are putting pressure on the shared services and
common use benefits of the traditional Enterprise Architecture approach.
Without a strong Enterprise Architecture approach, the rapid adoption of
changing technologies will cause discontinuities across the
enterprise.

The flexibility of the TOGAF ADM enables technology change to become a
driver and strategic resource rather than a recipient of Change
Requests. As a result, the Technology Architecture may both drive
business capabilities and respond to information system requirements at
the same time.

</details>

<a id="tag_08_05_02"></a>
## 8.5.2. Architecture Repository

概念：技术库资源含已有IT服务目录、适用TRM、行业/通用技术模型及III-RM。

适用条件：寻找基础技术资产与集成信息基础设施参考。

逻辑关系：参考的应用层组件与底层服务需区分。

决策方法：选择相关且当前技术参考。

制品及证据：技术服务、模型与库选择。

适用边界：提到参考出版物不代表本轮已独立解析它。

来源块：C220-web-2025:02-architecture-development-method:b00793, C220-web-2025:02-architecture-development-method:b00794, C220-web-2025:02-architecture-development-method:b00795, C220-web-2025:02-architecture-development-method:b00796

<details><summary>展开本节完整英文来源</summary>

8.5.2. Architecture Repository

As part of Phase D, the architecture team will need to consider what
relevant Technology Architecture resources are available in the
Architecture Repository (see the TOGAF Standard — Architecture Content ).

In particular:

Existing IT services as documented in the IT repository or IT service
catalog The adopted technical reference model, if applicable Generic technology models relevant to the organization’s industry
sector Technology models relevant to Common Systems Architectures The Open Group has a Reference Model for Integrated Information
Infrastructure (III-RM) — see the TOGAF ® Series Guide: The TOGAF Integrated Information Infrastructure Reference Model (III-RM) — that focuses on the application-level components and underlying services
necessary to provide an integrated information infrastructure

</details>

<a id="chap09"></a>
## 9. Phase E: Opportunities & Solutions

概念：E识别能交付既定目标架构的项目、计划或组合载体。

适用条件：域目标与候选组件已形成。

逻辑关系：由架构开发转向实现方案安排。

决策方法：选择有效交付载体。

制品及证据：工作包、载体与路线图。

适用边界：交付载体不是架构域或组织岗位。

来源块：C220-web-2025:02-architecture-development-method:b00797, C220-web-2025:02-architecture-development-method:b00798, C220-web-2025:02-architecture-development-method:b00799, C220-web-2025:02-architecture-development-method:b00800

<details><summary>展开本节完整英文来源</summary>

9. Phase E: Opportunities & Solutions

This chapter describes the process of identifying delivery vehicles
(projects, programs, or portfolios) that effectively deliver the Target
Architecture identified in previous phases.



Figure 9-1: Phase E: Opportunities & Solutions

</details>

<a id="tag_09_01"></a>
## 9.1. Objectives

概念：E形成初始完整路线图、按需过渡架构和基于ABBs的总体SBBs。

适用条件：B/C/D差距和候选组件输入。

逻辑关系：是否增量决定是否需要持续价值的过渡状态。

决策方法：确定增量路径与总体方案构建块。

制品及证据：初始完整路线图、过渡架构、SBBs。

适用边界：初始完整仍可草稿，不等于F最终获批迁移计划。

来源块：C220-web-2025:02-architecture-development-method:b00801, C220-web-2025:02-architecture-development-method:b00802, C220-web-2025:02-architecture-development-method:b00803

<details><summary>展开本节完整英文来源</summary>

9.1. Objectives

The objectives of Phase E are to:

Generate the initial complete version of the Architecture Roadmap,
based upon the gap analysis and candidate Architecture Roadmap
components from Phases B, C, and D Determine whether an incremental approach is required, and if so
identify Transition Architectures that will deliver continuous business
value Define the overall Solution Building Blocks (SBBs) to finalize the
Target Architecture based on the ABBs

</details>

<a id="tag_09_02"></a>
## 9.2. Inputs

概念：E输入整合各域候选、差距和组织交付能力。

适用条件：启动机会解决方案分析。

逻辑关系：9.2.1—9.2.3按参考、业务、架构分类。

决策方法：确认跨域输入。

制品及证据：输入来源及状态。

适用边界：输入导航不证明跨域语义已统一。

来源块：C220-web-2025:02-architecture-development-method:b00804, C220-web-2025:02-architecture-development-method:b00805

<details><summary>展开本节完整英文来源</summary>

9.2. Inputs

This section defines the inputs to Phase E.

</details>

<a id="tag_09_02_01"></a>
## 9.2.1. Reference Materials External to the Enterprise

概念：E外部参考含架构参考和产品信息。

适用条件：评估实现方案。

逻辑关系：产品事实应支持候选机制评估。

决策方法：选择相关产品参考。

制品及证据：参考材料和产品信息。

适用边界：产品资料不代表采购或能力证实。

来源块：C220-web-2025:02-architecture-development-method:b00806, C220-web-2025:02-architecture-development-method:b00807

<details><summary>展开本节完整英文来源</summary>

9.2.1. Reference Materials External to the Enterprise

Architecture reference materials (see the TOGAF Standard — Architecture Content ) Product information

</details>

<a id="tag_09_02_02"></a>
## 9.2.2. Non-Architectural Inputs

概念：E非架构输入含请求、能力评估、沟通计划和规划方法。

适用条件：交付路径需适应组织实践。

逻辑关系：规划方法及能力影响载体与顺序。

决策方法：确认可用规划和参与安排。

制品及证据：请求、评估、沟通和规划方法。

适用边界：规划方法存在不消除能力缺口。

来源块：C220-web-2025:02-architecture-development-method:b00808, C220-web-2025:02-architecture-development-method:b00809

<details><summary>展开本节完整英文来源</summary>

9.2.2. Non-Architectural Inputs

Request for Architecture Work (see the TOGAF Standard — Architecture Content ) Capability Assessment (see the TOGAF Standard — Architecture Content ) Communications Plan (see the TOGAF Standard — Architecture Content ) Planning methodologies

</details>

<a id="tag_09_02_03"></a>
## 9.2.3. Architectural Inputs

概念：E输入含五类治理框架、四域差距/要求与B/C/D候选路线图。

适用条件：汇总交付方案。

逻辑关系：EA组织与框架、说明书愿景库、草稿定义要求、服务管理要求、既有项目变更共同约束实现。

决策方法：确认跨业务规划、EA、组合项目、系统开发和运营框架接点。

制品及证据：四域草稿、候选组件、变更请求、IT服务管理要求。

适用边界：草稿状态保留；未有项目变更不自动补造。

来源块：C220-web-2025:02-architecture-development-method:b00810, C220-web-2025:02-architecture-development-method:b00811

<details><summary>展开本节完整英文来源</summary>

9.2.3. Architectural Inputs

Organizational Model for Enterprise Architecture (see the TOGAF Standard — Architecture Content ), including: Scope of organizations impacted Maturity assessment, gaps, and resolution approach Roles and responsibilities for architecture team(s) Constraints on architecture work Budget requirements Governance and support strategy Governance models and frameworks for: Corporate Business Planning Enterprise Architecture Portfolio, Program, Project Management System Development/Engineering Operations (Service) Tailored Architecture Framework (see the TOGAF Standard — Architecture Content ), including: Tailored architecture method Tailored architecture content (deliverables and artifacts) Configured and deployed tools Statement of Architecture Work (see the TOGAF Standard — Architecture Content ) Architecture Vision (see the TOGAF Standard — Architecture Content ) Architecture Repository (see the TOGAF Standard — Architecture Content ), including: Re-usable building blocks Publicly available reference models Organization-specific reference models Organization standards Draft Architecture Definition Document, which may include Baseline
and/or Target Architectures of any architecture domain Draft Architecture Requirements Specification (see the TOGAF Standard — Architecture Content ), including: Architectural requirements Gap analysis results (from Business, Data, Application, and
Technology Architecture) IT Service Management requirements Change Requests for existing business programs and projects (see the TOGAF Standard — Architecture Content ) Candidate Architecture Roadmap components from Phases B, C, and D

</details>

<a id="tag_09_03"></a>
## 9.3. Steps

概念：E步骤按范围目标与治理调整，但活动必须在路线图/迁移计划生成时关闭。

适用条件：执行十一项机会方案工作。

逻辑关系：因素约束、差距要求互操作依赖、就绪风险、策略工作包过渡与计划逐步整合。

决策方法：确定顺序和收尾条件。

制品及证据：十一项结果及关闭记录。

适用边界：顺序裁剪不免除已启动工作关闭。

来源块：C220-web-2025:02-architecture-development-method:b00812, C220-web-2025:02-architecture-development-method:b00813, C220-web-2025:02-architecture-development-method:b00814, C220-web-2025:02-architecture-development-method:b00815, C220-web-2025:02-architecture-development-method:b00816, C220-web-2025:02-architecture-development-method:b00817

<details><summary>展开本节完整英文来源</summary>

9.3. Steps

The level of detail addressed in Phase E will depend on the scope and
goals of the overall architecture effort.

The order of the steps in Phase E as well as the time at which they are
formally started and completed should be adapted to the situation at
hand in accordance with the established Architecture Governance.

All activities that have been initiated in these steps must be closed
during the Create the Architecture Roadmap & Implementation and
Migration Plan step; see Section 9.3.11, “Create the Architecture Roadmap & Implementation and Migration Plan” .

The steps in Phase E are as follows:

Determine/confirm key corporate change attributes; see Section 9.3.1, “Determine/Confirm Key Corporate Change Attributes” Determine business constraints for implementation; see Section 9.3.2, “Determine Business Constraints for Implementation” Review and consolidate gap analysis results from Phases B to D; see Section 9.3.3, “Review and Consolidate Gap Analysis Results from Phases B to D” Review consolidated requirements across related business functions; see Section 9.3.4, “Review Consolidated Requirements Across Related Business Functions” Consolidate and reconcile interoperability requirements; see Section 9.3.5, “Consolidate and Reconcile Interoperability Requirements” Refine and validate dependencies; see Section 9.3.6, “Refine and Validate Dependencies” Confirm readiness and risk for business transformation; see Section 9.3.7, “Confirm Readiness and Risk for Business Transformation” Formulate Implementation and Migration Strategy; see Section 9.3.8, “Formulate Implementation and Migration Strategy” Identify and group major work packages; see Section 9.3.9, “Identify and Group Major Work Packages” Identify Transition Architectures; see Section 9.3.10, “Identify Transition Architectures” Create the Architecture Roadmap & Implementation and Migration Plan; see Section 9.3.11, “Create the Architecture Roadmap & Implementation and Migration Plan”

</details>

<a id="tag_09_03_01"></a>
## 9.3.1. Determine/Confirm Key Corporate Change Attributes

概念：企业文化和单位/企业转型能力形成实施因素。

适用条件：实施需要适应组织文化技能。

逻辑关系：因素目录是实施迁移决定的资料库与档案，即使EA成熟此步骤简单也要建立。

决策方法：评估组织文化能力并记录因素。

制品及证据：实施因素目录和决定记录。

适用边界：有成熟EA不意味着因素可略去。

来源块：C220-web-2025:02-architecture-development-method:b00818, C220-web-2025:02-architecture-development-method:b00819, C220-web-2025:02-architecture-development-method:b00820

<details><summary>展开本节完整英文来源</summary>

9.3.1. Determine/Confirm Key Corporate Change Attributes

This step determines how the Enterprise Architecture can be best
implemented to take advantage of the organization’s business culture.
This should include the creation of an Implementation Factor catalog
(see the TOGAF Standard — Architecture Content ) to serve as a repository for architecture implementation
and migration decisions. The step also includes assessments of the
transition capabilities of the organization units involved (including
culture and abilities), and assessments of the enterprise (including
culture and skill sets).

The resulting factors from the assessments should be documented in the
Implementation Factor catalog. For organizations where Enterprise
Architecture is well established, this step can be simple, but the
catalog has to be established so that it can be used as an archive and
record of decisions taken.

</details>

<a id="tag_09_03_02"></a>
## 9.3.2. Determine Business Constraints for Implementation

概念：业务驱动可约束实施顺序。

适用条件：企业及业务线计划和成熟度影响实施。

逻辑关系：复核两层战略/业务计划及EA成熟度。

决策方法：确定不可违背的业务时序约束。

制品及证据：实施业务约束与计划/评估依据。

适用边界：偏好不应伪装成硬约束。

来源块：C220-web-2025:02-architecture-development-method:b00821, C220-web-2025:02-architecture-development-method:b00822

<details><summary>展开本节完整英文来源</summary>

9.3.2. Determine Business Constraints for Implementation

Identify any business drivers that would constrain the sequence of
implementation. This should include a review of the business and
strategic plans, at both a corporate and line-of-business level, and a
review of the Enterprise Architecture Maturity Assessment.

</details>

<a id="tag_09_03_03"></a>
## 9.3.3. Review and Consolidate Gap Analysis Results from Phases B to D

概念：综合差距、方案与依赖矩阵连接四域差距、候选SBBs和相关ABBs。

适用条件：B—D局部结果已形成。

逻辑关系：使用业务交互、实体功能、应用功能等关系找跨域依赖；相似差距整理并核对因素，新增因素回目录。

决策方法：选择潜在解法、去重复或分组且适当讨论备选。

制品及证据：综合矩阵、单一差距表、SBB/ABB映射和因素更新。

适用边界：一个SBB可解决多个差距，不能把差距条数当采购件数。

来源块：C220-web-2025:02-architecture-development-method:b00823, C220-web-2025:02-architecture-development-method:b00824, C220-web-2025:02-architecture-development-method:b00825, C220-web-2025:02-architecture-development-method:b00826, C220-web-2025:02-architecture-development-method:b00827, C220-web-2025:02-architecture-development-method:b00828

<details><summary>展开本节完整英文来源</summary>

9.3.3. Review and Consolidate Gap Analysis Results from Phases B to D

Consolidate and integrate the gap analysis results from the Business,
Information Systems, and Technology Architectures (created in Phases B
to D) and assess their implications with respect to potential solutions
and inter-dependencies. This should be done by creating a Consolidated
Gaps, Solutions, and Dependencies matrix, as shown in the TOGAF Standard — Architecture Content ,
which will enable the identification of SBBs that could potentially
address one or more gaps and their associated ABBs.

The SBBs are created based on the candidate roadmap components from
Phases B, C, and D.

If appropriate, investigate different Target Architecture alternatives
and discuss these with stakeholders using the Architecture Alternatives
and Trade-offs technique (see the TOGAF Standard — ADM Techniques ).

Review the Phase B, C, and D gap analysis results and consolidate them
in a single list. The gaps should be consolidated along with potential
solutions to the gaps and dependencies. A recommended technique for
determining the dependencies is to use sets of views such as the
Business Interaction matrix, the Data Entity/Business Function matrix,
and the Application/Function matrix to completely relate elements from
different architecture domains.

Rationalize the Consolidated Gaps, Solutions, and Dependencies matrix.
Once all of the gaps have been documented, re-organize the gap list and
place similar items together. When grouping the gaps, refer to the
Implementation Factor catalog and review the implementation factors. Any
additional factors should be added to the Implementation Factor catalog.

</details>

<a id="tag_09_03_04"></a>
## 9.3.4. Review Consolidated Requirements Across Related Business Functions

概念：跨业务功能要求整合寻找更有效的最小要求集及共享解法。

适用条件：多业务线可共享业务/应用服务。

逻辑关系：把要求差距方案因素整合进工作包可能改变资源需求。

决策方法：识别共享方案与合并后资源影响。

制品及证据：整合要求、共享服务/方案和工作包。

适用边界：最小集是实现效率讨论，不允许删掉未满足必要要求。

来源块：C220-web-2025:02-architecture-development-method:b00829, C220-web-2025:02-architecture-development-method:b00830

<details><summary>展开本节完整英文来源</summary>

9.3.4. Review Consolidated Requirements Across Related Business Functions

Assess the requirements, gaps, solutions, and factors to identify a
minimal set of requirements whose integration into work packages would
lead to a more efficient and effective implementation of the Target
Architecture across the business functions that are participating in the
architecture. This functional perspective leads to the satisfaction of
multiple requirements through the provision of shared solutions and
services. The implications of this consolidation of requirements with
respect to architectural components can be significant with respect to
the provision of resources. For example, several requirements raised by
several lines of business can be resolved through the provision of a
shared set of Business Services and Application Services within a work
package or project.

</details>

<a id="tag_09_03_05"></a>
## 9.3.5. Consolidate and Reconcile Interoperability Requirements

概念：互操作冲突应跨业务数据应用技术四域解决。

适用条件：复用SBB、COTS和第三方要求可能冲突。

逻辑关系：复核愿景目标因素矩阵；可加转换翻译块或修改冲突块规格。

决策方法：选择转换机制或规格调整并检验冲突。

制品及证据：综合互操作要求、冲突及处理。

适用边界：不能将互操作仅理解为数据格式转换。

来源块：C220-web-2025:02-architecture-development-method:b00831, C220-web-2025:02-architecture-development-method:b00832, C220-web-2025:02-architecture-development-method:b00833, C220-web-2025:02-architecture-development-method:b00834

<details><summary>展开本节完整英文来源</summary>

9.3.5. Consolidate and Reconcile Interoperability Requirements

Consolidate the interoperability requirements identified in previous
phases. The Architecture Vision and Target Architectures, as well as the
Implementation Factor catalog and Consolidated Gaps, Solutions, and
Dependencies matrix, should be consolidated and reviewed to identify any
constraints on interoperability required by the potential set of
solutions.

A key outcome is to minimize interoperability conflicts, or to ensure
such conflicts are addressed in the architecture. Re-used SBBs,
Commercial Off-The-Shelf (COTS) products, and third-party service
providers typically impose interoperability requirements that conflict.
Any such conflicts must be addressed in the architecture, and conflicts
must be considered across all architecture domains (Business, Data,
Application, Technology).

There are two basic approaches to interoperability conflicts; either
create a building block that transforms or translates between
conflicting building blocks, or make a change to the specification of
the conflicting building blocks.

</details>

<a id="tag_09_03_06"></a>
## 9.3.6. Refine and Validate Dependencies

概念：依赖支撑实施排序、协调、项目分组和增量时间。

适用条件：已有业务/应用服务实现或变更限制迁移。

逻辑关系：细化约束并识别逻辑交付增量，结果记入路线图和必要过渡架构。

决策方法：确认依赖与可交付顺序。

制品及证据：依赖评估、项目/增量、路线图/过渡记录。

适用边界：无循环的依赖图不证明实施容量可行。

来源块：C220-web-2025:02-architecture-development-method:b00835, C220-web-2025:02-architecture-development-method:b00836, C220-web-2025:02-architecture-development-method:b00837

<details><summary>展开本节完整英文来源</summary>

9.3.6. Refine and Validate Dependencies

Refine the initial dependencies, ensuring that any constraints on the
Implementation and Migration Plans are identified. There are several key
dependencies that should be taken into account, such as dependencies on
existing implementations of Business Services and Application Services
or changes to them. Dependencies should be used for determining the
sequence of implementation and identifying the co-ordination required. A
study of the dependencies should group activities together, creating a
basis for projects to be established. Examine the relevant projects and
see whether logical increments of deliverables can be identified. The
dependencies will also help to identify when the identified increments
can be delivered. Once finished, an assessment of these dependencies
should be documented as part of the Architecture Roadmap and any
necessary Transition Architectures.

Addressing dependencies serves as the basis for most migration planning.

</details>

<a id="tag_09_03_07"></a>
## 9.3.7. Confirm Readiness and Risk for Business Transformation

概念：E复核A就绪评估对路线图与策略的影响。

适用条件：转型风险需识别分类缓解。

逻辑关系：风险记入综合差距方案依赖矩阵并影响交付路径。

决策方法：判断就绪变化和缓解措施。

制品及证据：更新就绪、风险和综合矩阵。

适用边界：A结论不能无限沿用；缓解计划不是已缓解事实。

来源块：C220-web-2025:02-architecture-development-method:b00838, C220-web-2025:02-architecture-development-method:b00839

<details><summary>展开本节完整英文来源</summary>

9.3.7. Confirm Readiness and Risk for Business Transformation

Review the findings of the Business Transformation Readiness Assessment
previously conducted in Phase A and determine their impact on the
Architecture Roadmap and the Implementation and Migration Strategy. It
is important to identify, classify, and mitigate risks associated with
the transformation effort. Risks should be documented in the
Consolidated Gaps, Solutions, and Dependencies matrix.

</details>

<a id="tag_09_03_08"></a>
## 9.3.8. Formulate Implementation and Migration Strategy

概念：实施迁移策略可全新、革命切换或演化收敛。

适用条件：确定总体实现目标及过渡安排。

逻辑关系：快赢、可达目标、价值链等方法结合风险依赖形成工作包基础，最后取得策略同意。

决策方法：选择策略及风险控制路径。

制品及证据：总体实施迁移策略、方法、依赖和同意。

适用边界：三策略是基本分类不自动排名；并行/分阶段需业务条件。

来源块：C220-web-2025:02-architecture-development-method:b00840, C220-web-2025:02-architecture-development-method:b00841, C220-web-2025:02-architecture-development-method:b00842, C220-web-2025:02-architecture-development-method:b00843, C220-web-2025:02-architecture-development-method:b00844, C220-web-2025:02-architecture-development-method:b00845

<details><summary>展开本节完整英文来源</summary>

9.3.8. Formulate Implementation and Migration Strategy

Create an overall Implementation and Migration Strategy that will guide
the implementation of the Target Architecture, and structure any
Transition Architectures. The first activity is to determine an overall
strategic approach to implementing the solutions and/or exploiting
opportunities. There are three basic approaches as follows:

Greenfield: a completely new implementation Revolutionary: a radical change (i.e., switch on, switch off) Evolutionary: a strategy of convergence, such as parallel running or a
phased approach to introduce new capabilities

Next, determine an approach for the overall strategic direction that
will address and mitigate the risks identified in the Consolidated Gaps,
Solutions, and Dependencies matrix. The most common implementation
methodologies are:

Quick win (snapshots) Achievable targets Value chain method

These approaches and the identified dependencies should become the basis
for the creation of the work packages. This activity terminates with
agreement on the Implementation and Migration Strategy for the
enterprise.

</details>

<a id="tag_09_03_09"></a>
## 9.3.9. Identify and Group Major Work Packages

概念：主要工作包按综合差距因素逻辑分组，再分增量/项目组合。

适用条件：相关方规划者EA评估缺业务能力。

逻辑关系：每差距指定新开发、已有增强或采购及自建/合同方式；现系统分mainstream/contain/replace。

决策方法：按依赖和策略选机制、分组和系统处理。

制品及证据：解法列、系统分类、工作包/能力增量及组合项目。

适用边界：next three years是源文规划视野例，不强制本企业三年；contain不是立即替换。

来源块：C220-web-2025:02-architecture-development-method:b00846, C220-web-2025:02-architecture-development-method:b00847, C220-web-2025:02-architecture-development-method:b00848, C220-web-2025:02-architecture-development-method:b00849, C220-web-2025:02-architecture-development-method:b00850, C220-web-2025:02-architecture-development-method:b00851, C220-web-2025:02-architecture-development-method:b00852

<details><summary>展开本节完整英文来源</summary>

9.3.9. Identify and Group Major Work Packages

Key stakeholders, planners, and the Enterprise Architects should assess
the missing business capabilities identified in the Architecture Vision
and Target Architecture.

Using the Consolidated Gaps, Solutions, and Dependencies matrix together
with the Implementation Factor catalog, logically group the various
activities into work packages.

Fill in the “Solution” column in the Consolidated Gaps, Solutions, and
Dependencies matrix to recommend the proposed solution mechanisms.
Indicate for every gap/activity whether the solution should be oriented
towards a new development, or be based on an existing product, and/or
use a solution that can be purchased. An existing system may resolve the
requirement with minor enhancements. For new development this is a good
time to determine whether the work should be conducted in-house or
through a contract.

Classify every current system that is under consideration as:

Mainstream: part of the future information system Contain: expected to be replaced or modified in the planning horizon
(next three years) Replace: to be replaced in the planning horizon

Supporting top-level work packages should then in turn be decomposed
into increments to deliver the capability increments. Analyze and refine
these work packages or increments with respect to their business
transformation issues and the strategic implementation approach.
Finally, group the work packages into portfolios and projects within a
portfolio, taking into consideration the dependencies and the strategic
implementation approach.

</details>

<a id="tag_09_03_10"></a>
## 9.3.10. Identify Transition Architectures

概念：过渡架构是增量路径的明确目标并须具可测业务价值。

适用条件：变更规模需要增量实现。

逻辑关系：依据策略、综合矩阵、项目组合和组织产生/吸收变更容量；困难活动通常后置但有充分理由可例外。

决策方法：选择过渡状态、非均等时间间隔与困难活动顺序。

制品及证据：过渡架构、可测价值和容量/依赖依据。

适用边界：时间间隔不必均等；容量未知不能判过渡可行。

来源块：C220-web-2025:02-architecture-development-method:b00853, C220-web-2025:02-architecture-development-method:b00854, C220-web-2025:02-architecture-development-method:b00855, C220-web-2025:02-architecture-development-method:b00856

<details><summary>展开本节完整英文来源</summary>

9.3.10. Identify Transition Architectures

Where the scope of change to implement the Target Architecture requires
an incremental approach, then one or more Transition Architectures may
be necessary. These provide an ability to identify clear targets along
the roadmap to realizing the Target Architecture. The Transition
Architectures should provide measurable business value. The time-span
between successive Transition Architectures does not have to be of
uniform duration.

Development of Transition Architectures must be based upon the preferred
implementation approach, the Consolidated Gaps, Solutions, and
Dependencies matrix, the listing of projects and portfolios, as well as
the enterprise’s capacity for creating and absorbing change.

Determine where the difficult activities are, and unless there are
compelling reasons, implement them after other activities that most
easily deliver missing capability.

</details>

<a id="tag_09_03_11"></a>
## 9.3.11. Create the Architecture Roadmap & Implementation and Migration Plan

概念：E草稿路线图展示基线到目标工作包/过渡时序，迁移计划展示实现所需活动。

适用条件：准备F详细迁移规划。

逻辑关系：两者细节应与B—D定义相当且彼此对齐；工作包过渡成果要明确，依赖和既有SBB生命周期决定排序。

决策方法：判断是否需要另层迭代，确认项目资源识别足够。

制品及证据：草稿路线图/迁移计划及愿景定义要求更新。

适用边界：数据创建应用先行是可考虑方式非强制；草稿不能当最终实施授权。

来源块：C220-web-2025:02-architecture-development-method:b00857, C220-web-2025:02-architecture-development-method:b00858, C220-web-2025:02-architecture-development-method:b00859, C220-web-2025:02-architecture-development-method:b00860, C220-web-2025:02-architecture-development-method:b00861, C220-web-2025:02-architecture-development-method:b00862

<details><summary>展开本节完整英文来源</summary>

9.3.11. Create the Architecture Roadmap & Implementation and Migration Plan

Consolidate the work packages and Transition Architectures into the
Architecture Roadmap, Draft, which describes a timeline of the
progression from the Baseline Architecture to the Target Architecture.
The timeline informs the Implementation and Migration Plan. The
Architecture Roadmap frames the migration planning in Phase F.
Identified Transition Architectures and work packages should have a
clear set of outcomes. The Architecture Roadmap must demonstrate how the
selection and timeline of Transition Architectures and work packages
realizes the Target Architecture.

The detail of the Architecture Roadmap, Draft, should be expressed at a
similar level of detail to the Architecture Definition Document
developed in Phases B, C, and D. Where significant additional detail is
required before implementation the architecture is likely transitioning
to a different level. See the TOGAF Standard — Applying the ADM for techniques to manage iteration and
different levels of detail.

The Implementation and Migration Plan must demonstrate the activity
necessary to realize the Architecture Roadmap. The Implementation and
Migration Plan forms the basis of the migration planning in Phase F. The
detail of the Implementation and Migration Plan, Draft, must be aligned
to the detail of the Architecture Roadmap and be sufficient to identify
the necessary projects and resource requirements to realize the roadmap.

When creating the Implementation and Migration Plan there are many
approaches to consider, such as a data-driven sequence, where
application systems that create data are implemented first, then
applications that process the data. A clear understanding of the
dependencies and lifecycle of in-place SBBs is required for an effective
Implementation and Migration Plan.

Finally, update the Architecture Vision, Architecture Definition
Document, and Architecture Requirements Specification with any
additional relevant outcomes from this phase.

</details>

<a id="tag_09_04"></a>
## 9.4. Outputs

概念：E输出将四域获批描述、按需过渡、综合矩阵、能力评估、SBBs与初始路线图汇总。

适用条件：交付E结果。

逻辑关系：工作包含功能依赖机会/定义/要求/能力增量关系、价值因素影响；建议含效能标准风险问题；迁移计划仍草稿。

决策方法：保留状态并确保工作包可追溯。

制品及证据：草稿定义/要求、路线图工作包、SBBs、实施因素与草稿迁移策略计划。

适用边界：段落列出Approved更新不意味着生成器可授予批准。

来源块：C220-web-2025:02-architecture-development-method:b00863, C220-web-2025:02-architecture-development-method:b00864, C220-web-2025:02-architecture-development-method:b00865, C220-web-2025:02-architecture-development-method:b00866

<details><summary>展开本节完整英文来源</summary>

9.4. Outputs

The outputs of Phase E may include, but are not restricted to:

Refined and updated version of the Architecture Vision phase
deliverables, where applicable, including: Architecture Vision, including definition of types and degrees of
interoperability Statement of Architecture Work (see the TOGAF Standard — Architecture Content ), updated if necessary Draft Architecture Definition Document (see the TOGAF Standard — Architecture Content ), including: Baseline Business Architecture, Approved, updated if necessary Target Business Architecture, Approved, updated if necessary Baseline Data Architecture, Approved, updated if necessary Target Data Architecture, Approved, updated if necessary Baseline Application Architecture, Approved, updated if necessary Target Application Architecture, Approved, updated if necessary Baseline Technology Architecture, Approved, updated if necessary Target Technology Architecture, Approved, updated if necessary Transition Architecture, number and scope as necessary Views corresponding to the selected viewpoints addressing key
stakeholder concerns Draft Architecture Requirements Specification (see the TOGAF Standard — Architecture Content ), including: Consolidated Gaps, Solutions, and Dependencies Assessment Capability Assessments, including: Business Capability Assessment IT Capability Assessment Architecture Roadmap (see the TOGAF Standard — Architecture Content ), including: Work package portfolio: Work package description (name, description, objectives) Functional requirements Dependencies Relationship to opportunity Relationship to Architecture Definition Document and Architecture
Requirements Specification Relationship to any capability increments Business value Implementation Factor catalog Impact Identification of Transition Architectures, if any, including: Relationship to Architecture Definition Document Implementation recommendations: Criteria measures of effectiveness Risks and issues Solution Building Blocks (SBBs) Implementation and Migration Plan, Draft, including: Implementation and Migration Strategy

The TOGAF Standard — Architecture Content contains a detailed description of architectural
artifacts which might be produced in this phase, describing them in
detail and relating them to entities, attributes, and relationships in
the TOGAF Enterprise Metamodel.

</details>

<a id="tag_09_05"></a>
## 9.5. Approach

概念：路线图、工作包、过渡架构、迁移计划是四个不同交付概念。

适用条件：由开发转交付。

逻辑关系：路线图列时间线工作包，工作包是一组逻辑变更，过渡是显著中间架构状态，迁移计划为项目日程。

决策方法：在组织就绪、机会和约束下选择最佳适配路径兼顾目标及增量价值。

制品及证据：四类关联对象及初始迁移计划。

适用边界：不能把工作包、项目、过渡状态和路线图节点合并成同一身份。

来源块：C220-web-2025:02-architecture-development-method:b00867, C220-web-2025:02-architecture-development-method:b00868, C220-web-2025:02-architecture-development-method:b00869, C220-web-2025:02-architecture-development-method:b00870, C220-web-2025:02-architecture-development-method:b00871, C220-web-2025:02-architecture-development-method:b00872, C220-web-2025:02-architecture-development-method:b00873, C220-web-2025:02-architecture-development-method:b00874, C220-web-2025:02-architecture-development-method:b00875

<details><summary>展开本节完整英文来源</summary>

9.5. Approach

Phase E concentrates on how to deliver the architecture. It takes into
account the complete set of gaps between the Target and Baseline
Architectures in all architecture domains, and logically groups changes
into work packages within the enterprise’s portfolios. This is an effort
to build a best-fit roadmap that is based upon the stakeholder
requirements, the enterprise’s business transformation readiness,
identified opportunities and solutions, and identified implementation
constraints. The key is to focus on the final target while realizing
incremental business value.

Phase E is the initial step in the creation of the Implementation and
Migration Plan which is completed in Phase F. It provides the basis of a
well considered Implementation and Migration Plan that is integrated
into the enterprise’s portfolio in Phase F.

The following four concepts are key to transitioning from developing to
delivering a Target Architecture:

Architecture Roadmap Work Packages Transition Architectures Implementation and Migration Plan

The Architecture Roadmap lists individual work packages in a timeline
that will realize the Target Architecture.

Each work package identifies a logical group of changes necessary to
realize the Target Architecture.

A Transition Architecture describes the enterprise at an architecturally
significant state between the Baseline and Target Architectures.
Transition Architectures provide interim Target Architectures upon which
the organization can converge.

The Implementation and Migration Plan provides a schedule of the
projects that will realize the Target Architecture.

</details>

<a id="chap10"></a>
## 10. Phase F: Migration Planning

概念：F将基线到目标的迁移细化为最终实施迁移计划。

适用条件：E草稿可供组合/项目整合时。

逻辑关系：迁移规划连接架构与组织整体变更。

决策方法：确定详细实施路径。

制品及证据：最终迁移计划和路线图。

适用边界：最终计划不等于实际部署已完成。

来源块：C220-web-2025:02-architecture-development-method:b00876, C220-web-2025:02-architecture-development-method:b00877, C220-web-2025:02-architecture-development-method:b00878, C220-web-2025:02-architecture-development-method:b00879

<details><summary>展开本节完整英文来源</summary>

10. Phase F: Migration Planning

This chapter addresses migration planning; that is, how to move from the
Baseline to the Target Architectures by finalizing a detailed
Implementation and Migration Plan.



Figure 10-1: Phase F: Migration Planning

</details>

<a id="tag_10_01"></a>
## 10.1. Objectives

概念：F定稿路线图与支持计划、协调整体变更组合并确保相关方理解价值成本。

适用条件：组织需决策资源和迁移项目。

逻辑关系：业务价值/成本理解支撑计划同意。

决策方法：确认跨组合协调与工作包/过渡价值。

制品及证据：最终路线图/计划及价值成本材料。

适用边界：不能只出时间表便称达到F目标。

来源块：C220-web-2025:02-architecture-development-method:b00880, C220-web-2025:02-architecture-development-method:b00881, C220-web-2025:02-architecture-development-method:b00882

<details><summary>展开本节完整英文来源</summary>

10.1. Objectives

The objectives of Phase F are to:

Finalize the Architecture Roadmap and the supporting Implementation and Migration Plan Ensure that the Implementation and Migration Plan is co-ordinated with the enterprise’s approach to managing and implementing change in the enterprise’s overall change portfolio Ensure that the business value and cost of work packages and
Transition Architectures is understood by key stakeholders

</details>

<a id="tag_10_02"></a>
## 10.2. Inputs

概念：F输入继承E草稿路线图迁移策略及跨域成果。

适用条件：详细规划开始。

逻辑关系：10.2.1—10.2.3列三类输入。

决策方法：确认草稿和能力评估是否可用于规划。

制品及证据：F输入来源状态。

适用边界：导航不证明资源数据完整。

来源块：C220-web-2025:02-architecture-development-method:b00883, C220-web-2025:02-architecture-development-method:b00884

<details><summary>展开本节完整英文来源</summary>

10.2. Inputs

This section defines the inputs to Phase F.

</details>

<a id="tag_10_02_01"></a>
## 10.2.1. Reference Materials External to the Enterprise

概念：F外部输入为架构参考材料。

适用条件：补充规划参考。

逻辑关系：资源需适合迁移与本范围。

决策方法：选择参考。

制品及证据：参考材料及来源。

适用边界：不能把外部计划直接当本企业日程。

来源块：C220-web-2025:02-architecture-development-method:b00885, C220-web-2025:02-architecture-development-method:b00886

<details><summary>展开本节完整英文来源</summary>

10.2.1. Reference Materials External to the Enterprise

Architecture reference materials (see the TOGAF Standard — Architecture Content )

</details>

<a id="tag_10_02_02"></a>
## 10.2.2. Non-Architectural Inputs

概念：F非架构输入为请求、能力评估和沟通计划。

适用条件：协调任务能力及相关方。

逻辑关系：评估和沟通安排支持迁移规划。

决策方法：确认能力缺口及参与要求。

制品及证据：工作请求、能力评估、沟通。

适用边界：未知工作量不因输入计划而自动变已知。

来源块：C220-web-2025:02-architecture-development-method:b00887, C220-web-2025:02-architecture-development-method:b00888

<details><summary>展开本节完整英文来源</summary>

10.2.2. Non-Architectural Inputs

Request for Architecture Work (see the TOGAF Standard — Architecture Content ) Capability Assessment (see the TOGAF Standard — Architecture Content ) Communications Plan (see TOGAF Standard — Architecture Content )

</details>

<a id="tag_10_02_03"></a>
## 10.2.3. Architectural Inputs

概念：F包含五类治理框架、各域定义要求、项目变更、草稿路线图因素能力及迁移策略。

适用条件：从E进入最终规划。

逻辑关系：路线图标出工作包过渡，能力包括业务与IT，草稿迁移计划含高层策略。

决策方法：确认跨框架规划依据、草稿状态和能力现实。

制品及证据：E草稿、因素目录、能力评估、变更请求和上游架构。

适用边界：过渡架构if any和部分域描述保留范围限制。

来源块：C220-web-2025:02-architecture-development-method:b00889, C220-web-2025:02-architecture-development-method:b00890

<details><summary>展开本节完整英文来源</summary>

10.2.3. Architectural Inputs

Organizational Model for Enterprise Architecture (see the TOGAF Standard — Architecture Content ), including: Scope of organizations impacted Maturity assessment, gaps, and resolution approach Roles and responsibilities for architecture team(s) Constraints on architecture work Budget requirements Governance and support strategy Governance models and frameworks for: Corporate Business Planning Enterprise Architecture Portfolio, Program, Project Management System Development/Engineering Operations (Service) Tailored Architecture Framework (see the TOGAF Standard — Architecture Content ), including: Tailored architecture method Tailored architecture content (deliverables and artifacts) Configured and deployed tools Statement of Architecture Work (see the TOGAF Standard — Architecture Content ) Architecture Vision (see the TOGAF Standard — Architecture Content ) Architecture Repository (see the TOGAF Standard — Architecture Content ), including: Re-usable building blocks Publicly available reference models Organization-specific reference models Organization standards Draft Architecture Definition Document, which may include Baseline
and/or Target Architectures of any architecture domain, and/or
Transition Architectures Draft Architecture Requirements Specification (see the TOGAF Standard — Architecture Content ), including: Architectural requirements Gap analysis results (from Business, Data, Application, and
Technology Architecture) IT Service Management requirements Change Requests for existing business programs and projects (see the TOGAF Standard — Architecture Content ) Architecture Roadmap, Draft (see the TOGAF Standard — Architecture Content ), including: Identification of work packages Identification of Transition Architectures Implementation Factor catalog Capability Assessment (see the TOGAF Standard — Architecture Content ), including: Business Capability Assessment IT Capability Assessment Implementation and Migration Plan, Draft (see the TOGAF Standard — Architecture Content ), including the high-level Implementation and Migration
Strategy

</details>

<a id="tag_10_03"></a>
## 10.3. Steps

概念：F七步按范围与治理调整，活动须在开发周期完成/教训步骤关闭。

适用条件：执行最终迁移规划。

逻辑关系：框架接点、价值、资源、优先级、路线图、计划与开发收尾形成治理过渡。

决策方法：安排步骤与关闭条件。

制品及证据：七项结果及开发收尾。

适用边界：F收尾不是实施项目实际关闭。

来源块：C220-web-2025:02-architecture-development-method:b00891, C220-web-2025:02-architecture-development-method:b00892, C220-web-2025:02-architecture-development-method:b00893, C220-web-2025:02-architecture-development-method:b00894, C220-web-2025:02-architecture-development-method:b00895, C220-web-2025:02-architecture-development-method:b00896

<details><summary>展开本节完整英文来源</summary>

10.3. Steps

The level of detail addressed in Phase F will depend on the scope and
goals of the overall architecture effort.

The order of the steps in Phase F as well as the time at which they are
formally started and completed should be adapted to the situation at
hand in accordance with the established Architecture Governance.

All activities that have been initiated in these steps must be closed
during the “Complete the Architecture Development Cycle and Document
Lessons Learned” step; see Section 10.3.7, “Complete the Architecture Development Cycle and Document Lessons Learned” .

The steps in Phase F are as follows:

Confirm management framework interactions for Implementation and
Migration Plan; see Section 10.3.1, “Confirm Management Framework Interactions for the Implementation and Migration Plan” Assign a business value to each work package; see Section 10.3.2, “Assign a Business Value to Each Work Package” Estimate resource requirements, project timings, and availability/delivery vehicle; see Section 10.3.3, “Estimate Resource Requirements, Project Timings, and Availability/Delivery Vehicle” Prioritize the migration projects by conducting a cost/benefit assessment and risk assessment; see Section 10.3.4, “Prioritize the Migration Projects by Conducting a Cost/Benefit Assessment and Risk Assessment” Confirm Architecture Roadmap and update Architecture Definition Document; see Section 10.3.5, “Confirm Architecture Roadmap and Update Architecture Definition Document” Complete the Implementation and Migration Plan; see Section 10.3.6, “Complete the Implementation and Migration Plan” Complete the architecture development cycle and document lessons learned; see Section 10.3.7, “Complete the Architecture Development Cycle and Document Lessons Learned”

</details>

<a id="tag_10_03_01"></a>
## 10.3.1. Confirm Management Framework Interactions for the Implementation and Migration Plan

概念：迁移计划需在业务规划、EA、项目组合、运营管理四框架的计划中反映。

适用条件：组织框架共同交付业务结果。

逻辑关系：规划供资源，EA结构上下文，组合建系统，运营整合维护；迁移计划可嵌入其他框架计划。

决策方法：确认计划归属及各框架摘要对齐。

制品及证据：迁移计划与四框架计划接点。

适用边界：不强制单独一份EA控制全部资源的计划。

来源块：C220-web-2025:02-architecture-development-method:b00897, C220-web-2025:02-architecture-development-method:b00898, C220-web-2025:02-architecture-development-method:b00899, C220-web-2025:02-architecture-development-method:b00900, C220-web-2025:02-architecture-development-method:b00901

<details><summary>展开本节完整英文来源</summary>

10.3.1. Confirm Management Framework Interactions for the Implementation and Migration Plan

This step is about co-ordinating the Implementation and Migration Plan
with the management frameworks within the organization. There are
typically four management frameworks that have to work closely together
for the Implementation and Migration Plan to succeed:

Business Planning that conceives, directs, and provides the
resources for all of the activities required to achieve concrete
business objectives/outcomes Enterprise Architecture that structures and gives context to all
enterprise activities delivering concrete business outcomes primarily
but not exclusively in the IT domain Project/Portfolio Management that co-ordinates, designs, and builds
the business systems that deliver the concrete business outcomes Operations Management that integrates, operates, and maintains the
deliverables that deliver the concrete business outcomes

The Implementation and Migration Plan will impact the outputs of each of
these frameworks and consequently has to be reflected in them. In the
course of this step, understand the frameworks within the organization
and ensure that these plans are co-ordinated and inserted (in a summary
format) within the plans of each one of these frameworks.

The outcome of this step may well be that the Implementation and
Migration Plan could be part of a different plan produced by another one
of the frameworks with Enterprise Architecture participation.

</details>

<a id="tag_10_03_02"></a>
## 10.3.2. Assign a Business Value to Each Work Package

概念：工作包价值必须先定义组织价值及测量方法，再应用到项目增量。

适用条件：组合能力管理需审批监控和资源取舍。

逻辑关系：性能标准、签字ROI、CSF/MOE及战略适配支撑决策；聚合E风险，项目可能反改路线图定义。

决策方法：按一致业务价值和风险评价项目。

制品及证据：价值/风险矩阵、ROI签署、CSF/MOE、工作包项目映射。

适用边界：风险高低或价值数值无真实输入不能自动评分。

来源块：C220-web-2025:02-architecture-development-method:b00902, C220-web-2025:02-architecture-development-method:b00903, C220-web-2025:02-architecture-development-method:b00904, C220-web-2025:02-architecture-development-method:b00905, C220-web-2025:02-architecture-development-method:b00906, C220-web-2025:02-architecture-development-method:b00907, C220-web-2025:02-architecture-development-method:b00908

<details><summary>展开本节完整英文来源</summary>

10.3.2. Assign a Business Value to Each Work Package

Establish and assign a business value to each of the work packages. The
intent is to first establish what constitutes business value within the
organization, how value can be measured, and then apply this to each one
of the projects and project increments.

There are several issues to address in this activity:

Performance Evaluation Criteria are used by portfolio and capability
managers to approve and monitor the progress of the architecture
transformation Return-on-Investment Criteria have to be detailed and signed off by
the various executive stakeholders Business Value has to be defined as well as techniques, such as the
value chain, which are to be used to illustrate the role in achieving
tangible business outcomes Business value will be used by portfolio and capability managers to
allocate resources and, in cases where there are cutbacks, business
value in conjunction with return on investment can be used to determine
whether an endeavor proceeds, is delayed, or is canceled. Critical Success Factors (CSFs) should be established to define
success for a project and/or project increment These will provide managers and implementers with a gauge as to what
constitutes a successful implementation. Measures of Effectiveness (MOE) are often performance criteria and
many corporations include them in the CSFs Where they are treated discretely, it should be clear as to how these
criteria are to be grouped. Strategic Fit based upon the overall Enterprise Architecture (all
tiers) will be the critical factor for allowing the approval of any new
project or initiative and for determining the value of any deliverable

Use the work packages as a basis of identifying projects that will be in
the Implementation and Migration Plan. The identified projects will be
fully developed in other steps in Phase F. The projects, and project
increments, may require adjustment of the Architecture Roadmap and
Architecture Definition Document.

Risks should then be assigned to the projects and project increments by
aggregating risks identified in the Consolidated Gaps, Solutions, and
Dependencies Matrix (from Phase E).

Estimate the business value for each project using the Business Value
and Risk Matrix
(see the TOGAF Standard — Architecture Content ).

</details>

<a id="tag_10_03_03"></a>
## 10.3.3. Estimate Resource Requirements, Project Timings, and Availability/Delivery Vehicle

概念：资源时间与成本按项目及增量估计，资本投入和运营维护须分开。

适用条件：形成初始成本和资源日程。

逻辑关系：逐活动分配再汇总，可用退役旧系统抵消新能力成本。

决策方法：确认资源需求、时间和净成本。

制品及证据：活动/增量/项目资源、资本运营维护估计及退役抵扣。

适用边界：成本估计不等于真实容量与资金可用。

来源块：C220-web-2025:02-architecture-development-method:b00909, C220-web-2025:02-architecture-development-method:b00910

<details><summary>展开本节完整英文来源</summary>

10.3.3. Estimate Resource Requirements, Project Timings, and Availability/Delivery Vehicle

This step determines the required resources and times for each project
and their increments and provides the initial cost estimates. The costs
should be broken down into capital (to create the capability) and
operations and maintenance (to run and sustain the capability).
Opportunities should be identified where the costs associated with
delivering new and/or better capability can be offset by decommissioning
existing systems. Assign required resources to each activity and
aggregate them at the project increment and project level.

</details>

<a id="tag_10_03_04"></a>
## 10.3.4. Prioritize the Migration Projects by Conducting a Cost/Benefit Assessment and Risk Assessment

概念：迁移排序比较全部SBB净收益、交付成本和已计入风险并取得相关方共识。

适用条件：资源需在项目之间分配。

逻辑关系：理解随时间净收益；即使直接收益小，通向大收益的关键交付也可高优先，正式复核剩余风险及预计资金线。

决策方法：确定有共识的优先级与风险资金取舍。

制品及证据：优先项目表、成本收益、风险备注和正式复核。

适用边界：短期ROI不是唯一排序准则；缓解计划不能当成已有效执行。

来源块：C220-web-2025:02-architecture-development-method:b00911, C220-web-2025:02-architecture-development-method:b00912, C220-web-2025:02-architecture-development-method:b00913, C220-web-2025:02-architecture-development-method:b00914, C220-web-2025:02-architecture-development-method:b00915, C220-web-2025:02-architecture-development-method:b00916

<details><summary>展开本节完整英文来源</summary>

10.3.4. Prioritize the Migration Projects by Conducting a Cost/Benefit Assessment and Risk Assessment

Prioritize the projects by ascertaining their business value against the
cost of delivering them. The approach is to first determine, as clearly
as possible, the net benefit of all of the SBBs delivered by the
projects, and then verify that the risks have been effectively mitigated
and factored in. Afterwards, the intent is to gain the requisite
consensus to create a prioritized list of projects that will provide the
basis for resource allocation.

It is important to discover all costs, and to ensure that
decision-makers understand the net benefit over time.

Review the risks to ensure that the risks for the project deliverables
have been mitigated as much as possible. The project list is then
updated with risk-related comments.

Have the stakeholders agree upon a prioritization of the projects.
Prioritization criteria will use elements identified in the creation of
the draft Architecture Roadmap in Phase E as well as those relating to
individual stakeholder agendas. Notice that it is possible for a project
to earn a high priority if it provides a critical deliverable on the
path to some large benefit, even if the immediate benefit of the project
itself is small.

Formally review the risk assessment and revise it as necessary ensuring
that there is a full understanding of the residual risk associated with
the prioritization and the projected funding line.

</details>

<a id="tag_10_03_05"></a>
## 10.3.5. Confirm Architecture Roadmap and Update Architecture Definition Document

概念：F更新路线图/过渡间隔并按项目整合能力增量交付物。

适用条件：确认增量后策略可能改变。

逻辑关系：状态演进表协调并行架构实例；定义增量表把项目目标交付物与过渡对齐。

决策方法：按价值能力风险选择间隔并更新定义。

制品及证据：修订路线图、状态演进表和定义增量表。

适用边界：状态演进表不是项目任务日程。

来源块：C220-web-2025:02-architecture-development-method:b00917, C220-web-2025:02-architecture-development-method:b00918, C220-web-2025:02-architecture-development-method:b00919, C220-web-2025:02-architecture-development-method:b00920

<details><summary>展开本节完整英文来源</summary>

10.3.5. Confirm Architecture Roadmap and Update Architecture Definition Document

Update the Architecture Roadmap including any Transition Architectures.
Review the work to date to assess what the time-spans between Transition
Architecture should be, taking into consideration the increments in
business value and capability and other factors, such as risk. Once the
capability increments have been finalized, consolidate the deliverables
by project. This will result in a revised Architecture Roadmap.

This is needed in order to co-ordinate the development of several
concurrent instances of the various architectures. A Transition
Architecture State Evolution Table (see the TOGAF Standard — Architecture Content ) can
be used to show the proposed state of the domain architectures at
various levels of detail.

If the implementation approach has shifted as a result of confirming the
implementation increments, update the Architecture Definition Document.
This may include assigning project objectives and aligning projects and
their deliverables with the Transition Architectures to create an
Architecture Definition Increments Table (see the TOGAF Standard — Architecture Content ).

</details>

<a id="tag_10_03_06"></a>
## 10.3.6. Complete the Implementation and Migration Plan

概念：完整迁移计划整合项目活动、依赖和变更影响，过渡架构作组合里程碑。

适用条件：已有规划细节需汇总。

逻辑关系：所有外部依赖纳入，并评估总体资源可用性；项目计划可附入。

决策方法：核验跨项目可用资源与完整依赖。

制品及证据：最终迁移计划、外部依赖、总体资源评估及项目计划。

适用边界：资源/容量未知不能以字段齐全判规划可执行。

来源块：C220-web-2025:02-architecture-development-method:b00921, C220-web-2025:02-architecture-development-method:b00922, C220-web-2025:02-architecture-development-method:b00923

<details><summary>展开本节完整英文来源</summary>

10.3.6. Complete the Implementation and Migration Plan

Generate the completed Implementation and Migration Plan. Much of the
detail for the plan has already been gathered and this step brings it
all together using accepted planning and management techniques. This
should include integrating all of the projects and activities as well as
dependencies and impact of change into a project plan. Any Transition
Architectures will act as portfolio milestones.

All external dependencies should be captured and included, and the
overall availability of resources assessed. Project plans may be
included within the Implementation and Migration Plan.

</details>

<a id="tag_10_03_07"></a>
## 10.3.7. Complete the Architecture Development Cycle and Document Lessons Learned

概念：F结束架构开发并将治理移交架构实现。

适用条件：开发结果与迁移安排完成。

逻辑关系：能力成熟度适合时形成实施治理模型，教训输入H能力管理；若下阶段要更多细节可需较低层再迭代。

决策方法：判断治理模型需求与是否另轮开发。

制品及证据：教训、治理移交/模型、后续ADM请求。

适用边界：开发周期完成不等于实现完成或无需后续迭代。

来源块：C220-web-2025:02-architecture-development-method:b00924, C220-web-2025:02-architecture-development-method:b00925, C220-web-2025:02-architecture-development-method:b00926, C220-web-2025:02-architecture-development-method:b00927

<details><summary>展开本节完整英文来源</summary>

10.3.7. Complete the Architecture Development Cycle and Document Lessons Learned

This step transitions governance from the development of the
architecture to the realization of the architecture. If the maturity of
the Architecture Capability warrants, an Implementation Governance Model
may be produced (see the TOGAF Standard — Architecture Content ).

Lessons learned during the development of the architecture should be
documented and captured by the appropriate governance process in Phase H
as inputs to managing the Architecture Capability.

The detail of the Architecture Roadmap and the Implementation and
Migration Plan should be expressed at a similar level of detail to the
Architecture Definition Document developed in Phases B, C, and D. Where
significant additional detail is required by the next phase the
architecture is likely transitioning to a different level. Depending
upon the level of the Target Architecture and Implementation and
Migration Plan it may be necessary to iterate another ADM cycle at a
lower level of detail. See the TOGAF Standard — Applying the ADM for techniques to manage iteration and
different levels of detail.

</details>

<a id="tag_10_04"></a>
## 10.4. Outputs

概念：F输出包含已批准实施迁移计划及定稿架构定义要求路线图。

适用条件：交付规划收尾。

逻辑关系：计划含项目组合分配、能力和目标/过渡关系、里程碑WBS；项目章程可选，后续请求/治理模型有条件。

决策方法：准确标示批准、定稿和可选项。

制品及证据：获批计划、定稿过渡/定义/要求/路线图、复用ABBs及教训能力变更请求。

适用边界：Approved、Finalized与实际实施状态不同，章程optional不得强制。

来源块：C220-web-2025:02-architecture-development-method:b00928, C220-web-2025:02-architecture-development-method:b00929, C220-web-2025:02-architecture-development-method:b00930

<details><summary>展开本节完整英文来源</summary>

10.4. Outputs

The outputs of Phase F may include, but are not restricted to:

Implementation and Migration Plan, Approved (see the TOGAF Standard — Architecture Content ), including: Implementation and Migration Strategy Project and portfolio breakdown of the implementation: Allocation of work packages to project and portfolio Capabilities delivered by projects Relationship to Target Architecture and any Transition Architectures Milestones and timing Work breakdown structure Project charters (optional): Related work packages Business value Risk, issues, assumptions, dependencies Resource requirements and costs Benefits of migration Estimated costs of migration options Finalized Architecture Definition Document (see the TOGAF Standard — Architecture Content ), including: Finalized Transition Architectures, if any Finalized Architecture Requirements Specification (see the TOGAF Standard — Architecture Content ) Finalized Architecture Roadmap (see the TOGAF Standard — Architecture Content ) Re-Usable ABBs (see the TOGAF Standard — Architecture Content ) Requests for Architecture Work (see the TOGAF Standard — Architecture Content ) for a new iteration of the ADM cycle (if any) Implementation Governance Model (if any) (see the TOGAF Standard — Architecture Content ) Change Requests for the Architecture Capability arising from lessons
learned

</details>

<a id="tag_10_05"></a>
## 10.5. Approach

概念：F与项目组合经理合作，把E草稿整合进企业其他变更。

适用条件：企业同时有其他活动和迁移项目。

逻辑关系：按总体活动评依赖成本收益，最终计划含组合项目细节并记录教训持续改进。

决策方法：确认与整体变更组合协调。

制品及证据：最终计划及教训。

适用边界：只针对当前模型排期不证明全企业资源冲突已消除。

来源块：C220-web-2025:02-architecture-development-method:b00931, C220-web-2025:02-architecture-development-method:b00932, C220-web-2025:02-architecture-development-method:b00933, C220-web-2025:02-architecture-development-method:b00934, C220-web-2025:02-architecture-development-method:b00935

<details><summary>展开本节完整英文来源</summary>

10.5. Approach

The focus of Phase F is the creation of an Implementation and Migration
Plan in co-operation with the project and portfolio managers.

Phase E provides an incomplete Architecture Roadmap and Implementation and Migration Plan that address the Statement of Architecture Work. In
Phase F this Roadmap and the Implementation and Migration Plan are integrated with the enterprise’s other change activity.

Activities include assessing the dependencies, costs, and benefits of the various migration projects within the context of the enterprise’s
other activity. The Draft Architecture Roadmap, and Draft Implementation and Migration Plan, from Phase E will form the basis of the final
Implementation and Migration Plan that will include portfolio and project-level detail.

The architecture development cycle should then be completed and lessons learned documented to enable continuous process improvement.

</details>

<a id="chap11"></a>
## 11. Phase G: Implementation Governance

概念：G提供实施的架构监督。

适用条件：项目进行实际开发部署时。

逻辑关系：监督与组织实际开发过程并行。

决策方法：确定架构治理接点。

制品及证据：实施监督与治理记录。

适用边界：G不取代组织开发过程。

来源块：C220-web-2025:02-architecture-development-method:b00936, C220-web-2025:02-architecture-development-method:b00937, C220-web-2025:02-architecture-development-method:b00938, C220-web-2025:02-architecture-development-method:b00939

<details><summary>展开本节完整英文来源</summary>

11. Phase G: Implementation Governance

This chapter provides an architectural oversight of the implementation.



Figure 11-1: Phase G: Implementation

</details>

<a id="tag_11_01"></a>
## 11.1. Objectives

概念：G确保实施项目符合目标架构并治理解决方案及实施驱动变更请求。

适用条件：方案开发部署期间。

逻辑关系：符合性与变更处理共同保持目标和实现对齐。

决策方法：判断符合性与需治理变化。

制品及证据：符合性评估和变更治理。

适用边界：符合性不等于业务收益、容量或运营恢复自动达到。

来源块：C220-web-2025:02-architecture-development-method:b00940, C220-web-2025:02-architecture-development-method:b00941, C220-web-2025:02-architecture-development-method:b00942

<details><summary>展开本节完整英文来源</summary>

11.1. Objectives

The objectives of Phase G are to:

Ensure conformance with the Target Architecture by implementation
projects Perform appropriate Architecture Governance functions for the solution
and any implementation-driven architecture Change Requests

</details>

<a id="tag_11_02"></a>
## 11.2. Inputs

概念：G输入含架构目标、要求、路线图、迁移计划和治理/合同。

适用条件：建立实施监督。

逻辑关系：11.2.1—11.2.3区分参考、业务与架构输入。

决策方法：确认监督所需依据。

制品及证据：输入来源状态。

适用边界：输入列表不证明合同已签。

来源块：C220-web-2025:02-architecture-development-method:b00943, C220-web-2025:02-architecture-development-method:b00944

<details><summary>展开本节完整英文来源</summary>

11.2. Inputs

This section defines the inputs to Phase G.

</details>

<a id="tag_11_02_01"></a>
## 11.2.1. Reference Materials External to the Enterprise

概念：G外部输入为架构参考材料。

适用条件：监督需外部参考。

逻辑关系：参考应适合当前实现。

决策方法：选择必要参考。

制品及证据：参考材料及来源。

适用边界：不能用外部样例代替合同符合性规则。

来源块：C220-web-2025:02-architecture-development-method:b00945, C220-web-2025:02-architecture-development-method:b00946

<details><summary>展开本节完整英文来源</summary>

11.2.1. Reference Materials External to the Enterprise

Architecture reference materials (see the TOGAF Standard — Architecture Content )

</details>

<a id="tag_11_02_02"></a>
## 11.2.2. Non-Architectural Inputs

概念：G非架构输入为工作请求与能力评估。

适用条件：实施任务及资源能力需了解。

逻辑关系：能力状态影响部署监督可行性。

决策方法：核实能力评估当前。

制品及证据：工作请求和能力评估。

适用边界：原文此处未列沟通计划，不自动虚构其强制输入。

来源块：C220-web-2025:02-architecture-development-method:b00947, C220-web-2025:02-architecture-development-method:b00948

<details><summary>展开本节完整英文来源</summary>

11.2.2. Non-Architectural Inputs

Request for Architecture Work (see the TOGAF Standard — Architecture Content ) Capability Assessment (see the TOGAF Standard — Architecture Content )

</details>

<a id="tag_11_02_03"></a>
## 11.2.3. Architectural Inputs

概念：G架构输入包括已开发定义要求、路线图、治理框架/模型、标准合同与迁移计划。

适用条件：正式实施监督开始。

逻辑关系：组织框架库说明书愿景及E/F新请求提供边界，合同需在部署步骤正式签署。

决策方法：确认目标要求和治理合同依据。

制品及证据：定义/要求、治理模型、标准合同、E/F请求、迁移计划。

适用边界：标准合同模板不同于已签合同。

来源块：C220-web-2025:02-architecture-development-method:b00949, C220-web-2025:02-architecture-development-method:b00950

<details><summary>展开本节完整英文来源</summary>

11.2.3. Architectural Inputs

Organizational Model for Enterprise Architecture (see the TOGAF Standard — Architecture Content ), including: Scope of organizations impacted Maturity assessment, gaps, and resolution approach Roles and responsibilities for architecture team(s) Constraints on architecture work Budget requirements Governance and support strategy Tailored Architecture Framework (see TOGAF Standard — Architecture Content ), including: Tailored architecture method Tailored architecture content (deliverables and artifacts) Configured and deployed tools Statement of Architecture Work (see the TOGAF Standard — Architecture Content ) Architecture Vision (see the TOGAF Standard — Architecture Content ) Architecture Repository (see the TOGAF Standard — Architecture Content ), including: Re-usable building blocks Publicly available reference models Organization-specific reference models Organization standards Architecture Definition Document (see the TOGAF Standard — Architecture Content ) Architecture Requirements Specification (see the TOGAF Standard — Architecture Content ), including: Architectural requirements Gap analysis results (from Business, Data, Application, and
Technology Architectures) Architecture Roadmap (see the TOGAF Standard — Architecture Content ) Architecture Governance Framework (see the TOGAF Standard — EA Capability and Governance ) Implementation Governance Model (see the TOGAF Standard — Architecture Content ) Architecture Contract (standard) (see the TOGAF Standard — EA Capability and Governance ) Request for Architecture Work (see the TOGAF Standard — Architecture Content ) identified during Phases E and F Implementation and Migration Plan (see the TOGAF Standard — Architecture Content )

</details>

<a id="tag_11_03"></a>
## 11.3. Steps

概念：G六步按范围目标与组织治理调整时序。

适用条件：部署监督、运营与收尾。

逻辑关系：范围资源技能、部署指导、符合性、运营和实施后复核相联。

决策方法：决定部署与治理活动顺序。

制品及证据：六步安排和结果。

适用边界：调整步骤不替代实际开发部署。

来源块：C220-web-2025:02-architecture-development-method:b00951, C220-web-2025:02-architecture-development-method:b00952, C220-web-2025:02-architecture-development-method:b00953, C220-web-2025:02-architecture-development-method:b00954, C220-web-2025:02-architecture-development-method:b00955

<details><summary>展开本节完整英文来源</summary>

11.3. Steps

The level of detail addressed in Phase G will depend on the scope and
goals of the overall architecture effort.

The order of the steps in Phase G as well as the time at which they are
formally started and completed should be adapted to the situation at
hand in accordance with the established Architecture Governance.

The steps in Phase G are as follows:

Confirm scope and priorities for deployment with development management; see Section 11.3.1, “Confirm Scope and Priorities for Deployment with Development Management” Identify deployment resources and skills; see Section 11.3.2, “Identify Deployment Resources and Skills” Guide development of solutions deployment; see Section 11.3.3, “Guide Development of Solutions Deployment” Perform Enterprise Architecture Compliance reviews; see Section 11.3.4, “Perform Enterprise Architecture Compliance Reviews” Implement business and IT operations; see Section 11.3.5, “Implement Business and IT Operations” Perform post-implementation review and close the implementation; see Section 11.3.6, “Perform Post-Implementation Review and Close the Implementation”

</details>

<a id="tag_11_03_01"></a>
## 11.3.1. Confirm Scope and Priorities for Deployment with Development Management

概念：与开发管理确认部署范围优先、问题与块替换更新。

适用条件：迁移规划需落到具体项目。

逻辑关系：解决方案架构师识别SBB填补企业解法差距，其与项目可一对一或多对一，并协调同能力其他项目投资。

决策方法：明确SBB如何实现与跨项目复用。

制品及证据：部署建议、SBB/项目映射及差距报告。

适用边界：工作包、SBB和项目不是一一对应的强制关系。

来源块：C220-web-2025:02-architecture-development-method:b00956, C220-web-2025:02-architecture-development-method:b00957

<details><summary>展开本节完整英文来源</summary>

11.3.1. Confirm Scope and Priorities for Deployment with Development Management

Review migration planning outputs and produce recommendations on
deployment Identify Enterprise Architecture priorities for development teams Identify deployment issues and make recommendations Identify building blocks for replacement, update, etc. Perform gap analysis on Enterprise Architecture and solutions
framework The gaps in the existing enterprise solutions framework need to be
identified and the specific SBBs required to fill these gaps will be
identified by the Solution Architects. These SBBs may have a one-to-one
or many-to-one relationship with the projects. The Solution Architects
need to define exactly how this will be done. There may be other
projects working on these same capabilities and the Solution Architects
need to ensure that they can leverage best value from these investments. Produce a gap analysis report

</details>

<a id="tag_11_03_02"></a>
## 11.3.2. Identify Deployment Resources and Skills

概念：部署资源需理解总体EA结果及项目期望，方法应支持架构与设计互操作反馈。

适用条件：开发团队接收架构工作。

逻辑关系：适当模型可输入开发工具减少成本，方法必须允许设计向架构团队反馈。

决策方法：选择开发方法及资源教育安排。

制品及证据：方法、架构期望传达、设计反馈接点。

适用边界：教育和可生成代码不证明人员胜任或容量足够。

来源块：C220-web-2025:02-architecture-development-method:b00958, C220-web-2025:02-architecture-development-method:b00959, C220-web-2025:02-architecture-development-method:b00960, C220-web-2025:02-architecture-development-method:b00961

<details><summary>展开本节完整英文来源</summary>

11.3.2. Identify Deployment Resources and Skills

The project resources will include the development resources which will
need to be educated in the overall Enterprise Architecture deliverables
and expectations from the specific development and implementation
projects.

The following considerations should be addressed in this step:

Identify system development methods required for solutions development Note: There are a range of systems development methods and tools available
to the project teams. The method should ideally be able to
interoperate with the architecture outputs; for example, generate code
from architecture artifacts delivered to date. This could be achieved
through the use of modeling languages used for the Enterprise
Architecture development that may be captured as inputs to the systems
development tools and thereby reduce the cost of solutions
development. Ensure that the systems development method enables feedback to the
architecture team on designs

</details>

<a id="tag_11_03_03"></a>
## 11.3.3. Guide Development of Solutions Deployment

概念：每实施部署项目需影响分析、符合性规则、路线图时限和已签架构合同。

适用条件：指导解法部署与运营衔接。

逻辑关系：开发各组织及发起人签署合同；更新连续体/解法库，指导业务IT运营模型要求并分析解法运营差距。

决策方法：确认每项目范围策略变更规则时限与运营要求。

制品及证据：影响分析、合同签署、运营模型/要求、实施计划。

适用边界：签字段或模板不等于各方实际签署。

来源块：C220-web-2025:02-architecture-development-method:b00962, C220-web-2025:02-architecture-development-method:b00963

<details><summary>展开本节完整英文来源</summary>

11.3.3. Guide Development of Solutions Deployment

Formulate project recommendation For each separate implementation and deployment project, do the
following: Document scope of individual project in impact analysis Document strategic requirements (from the architectural perspective)
in impact analysis Document Change Requests (such as support for a standard interface)
in impact analysis Document rules for conformance in impact analysis Document timeline requirements from roadmap in impact analysis Document Architecture Contract Obtain signature from all developing organizations and sponsoring
organization Update Enterprise Continuum directory and repository for solutions Guide development of business & IT operating models for services Provide service requirements derived from Enterprise Architecture Guide definition of business & IT operational requirements Carry out gap analysis between the Solution Architecture and
operations Produce Implementation Plan

</details>

<a id="tag_11_03_04"></a>
## 11.3.4. Perform Enterprise Architecture Compliance Reviews

概念：按每个构建块审查持续实施治理与符合性。

适用条件：开发完成但部署项目尚未全部收尾。

逻辑关系：开展开发后审阅并关闭部署项目中的开发部分。

决策方法：确认块符合性和开发关闭。

制品及证据：符合性/开发后复核、开发部分关闭。

适用边界：关闭开发部分不是整个实施部署已关闭。

来源块：C220-web-2025:02-architecture-development-method:b00964, C220-web-2025:02-architecture-development-method:b00965

<details><summary>展开本节完整英文来源</summary>

11.3.4. Perform Enterprise Architecture Compliance Reviews

Review ongoing implementation governance and Architecture Compliance
for each building block Conduct post-development reviews Close development part of deployment projects

</details>

<a id="tag_11_03_05"></a>
## 11.3.5. Implement Business and IT Operations

概念：运营实施含IT/业务服务、技能培训和沟通文档发布。

适用条件：部署项目实际执行。

逻辑关系：新基线应发布到架构库，同时更新受影响运营配置等库。

决策方法：确认服务、技能与信息交接及基线更新。

制品及证据：已部署服务、培训/沟通证据、新基线及配置库更新。

适用边界：培训完成不等于已证明技能提升；新基线要代表实际状态。

来源块：C220-web-2025:02-architecture-development-method:b00966, C220-web-2025:02-architecture-development-method:b00967

<details><summary>展开本节完整英文来源</summary>

11.3.5. Implement Business and IT Operations

Carry out the deployment projects including: IT services delivery
implementation; business services delivery implementation; skills
development & training implementation; communications documentation
publication Publish new Baseline Architectures to the Architecture Repository and
update other impacted repositories, such as operational configuration
management stores

</details>

<a id="tag_11_03_06"></a>
## 11.3.6. Perform Post-Implementation Review and Close the Implementation

概念：实施后复核需发布并关闭项目，G在解法完整部署一次后关闭。

适用条件：实际部署完成。

逻辑关系：部署完成事实支撑后复核和关闭。

决策方法：确认是否完全部署并可关闭。

制品及证据：实施后审阅、发布与关闭记录。

适用边界：生成制品或通过离线校验不是完全部署一次。

来源块：C220-web-2025:02-architecture-development-method:b00968, C220-web-2025:02-architecture-development-method:b00969, C220-web-2025:02-architecture-development-method:b00970

<details><summary>展开本节完整英文来源</summary>

11.3.6. Perform Post-Implementation Review and Close the Implementation

Conduct post-implementation reviews Publish reviews and close projects

Closure on Phase G will be when the solutions are fully deployed once.

</details>

<a id="tag_11_04"></a>
## 11.4. Outputs

概念：G输出含签合同、符合性、变更、已部署符合架构解法和运营模型。

适用条件：部署治理交付。

逻辑关系：实施系统实际来自开发过程，架构人员直接参与程度依组织政策；库更新、豁免建议、SLA、指标和实现后文档亦可输出。

决策方法：区分开发产物、架构监督产物和运营要求。

制品及证据：合同/评估/请求、系统部署、库、SLA、指标及更新文档。

适用边界：ADM列系统为重要输出不意味着架构团队替代开发团队。

来源块：C220-web-2025:02-architecture-development-method:b00971, C220-web-2025:02-architecture-development-method:b00972, C220-web-2025:02-architecture-development-method:b00973

<details><summary>展开本节完整英文来源</summary>

11.4. Outputs

The outputs of Phase G may include, but are not restricted to:

Architecture Contract (signed) (see the TOGAF Standard — EA Capability and Governance ), as recommended in the
architecture-compliant implemented architectures Compliance Assessments (see the TOGAF Standard — Architecture Content ) Change Requests (see the TOGAF Standard — Architecture Content ) Architecture-compliant solutions deployed including: The architecture-compliant implemented system Note: The implemented system is actually an output of the development
process. However, given the importance of this output, it is stated
here as an output of the ADM. The direct involvement of architecture
staff in implementation will vary according to organizational policy,
as described in the TOGAF Standard — EA Capability and Governance . Populated Architecture Repository Architecture compliance recommendations and dispensations Recommendations on service delivery requirements Recommendations on performance metrics Service-Level Agreements (SLAs) Architecture Vision, updated post-implementation Architecture Definition Document, updated post-implementation Business and IT operating models for the implemented solution Architecture Building Blocks (ABBs)

</details>

<a id="tag_11_05"></a>
## 11.5. Approach

概念：G通过架构合同连接架构与实施组织，实际开发并行。

适用条件：按业务优先进行分阶段过渡部署。

逻辑关系：依标准治理/组合管理安排，运营框架保证长寿；项目详情需效能接受标准风险，符合性也覆盖企业其他在行项目。

决策方法：明确接受准则和跨项目治理覆盖。

制品及证据：项目范围交付约束、效能/验收标准、风险、合同和运营框架。

适用边界：分阶段是favored策略，不自动合适所有迁移；接受需实际业务依据。

来源块：C220-web-2025:02-architecture-development-method:b00974, C220-web-2025:02-architecture-development-method:b00975, C220-web-2025:02-architecture-development-method:b00976, C220-web-2025:02-architecture-development-method:b00977, C220-web-2025:02-architecture-development-method:b00978, C220-web-2025:02-architecture-development-method:b00979, C220-web-2025:02-architecture-development-method:b00980, C220-web-2025:02-architecture-development-method:b00981, C220-web-2025:02-architecture-development-method:b00982

<details><summary>展开本节完整英文来源</summary>

11.5. Approach

It is here that all the information for successful management of the
various implementation projects is brought together. Note that, in
parallel with Phase G, there is the execution of an
organizational-specific development process, where the actual
development happens.

To enable early realization of business value and benefits, and to
minimize the risk in the transformation and migration program, the
favored approach is to deploy the Target Architecture as a series of
transitions. Each transition represents an incremental step towards the
target, and each delivers business benefit in its own right. Therefore,
the overall approach in Phase G is to:

Establish an implementation program that will enable the delivery of
the Transition Architectures agreed for implementation during the
Migration Planning phase Adopt a phased deployment schedule that reflects the business
priorities embodied in the Architecture Roadmap Follow the organization’s standard for corporate, IT, and Architecture
Governance Use the organization’s established portfolio/program management
approach, where this exists Define an operations framework to ensure the effective long life of
the deployed solution

Phase G establishes the connection between architecture and
implementation organization, through the Architecture Contract.

Project details are developed, including:

Name, description, and objectives Scope, deliverables, and constraints Measures of effectiveness Acceptance criteria Risks and issues

Implementation governance is closely allied to overall Architecture
Governance, which is discussed in the TOGAF Standard — EA Capability and Governance .

A key aspect of Phase G is ensuring compliance with the defined
architecture(s), not only by the implementation projects, but also by
other ongoing projects within the enterprise. The considerations
involved with this are explained in detail in the TOGAF Standard — EA Capability and Governance .

</details>

<a id="chap12"></a>
## 12. Phase H: Architecture Change Management

概念：H建立新架构变更管理程序。

适用条件：架构部署后需持续演进。

逻辑关系：架构使用与业务技术变更形成新的管理循环。

决策方法：定义持续监测与变更入口。

制品及证据：变更管理程序。

适用边界：H不是单纯替换版本号。

来源块：C220-web-2025:02-architecture-development-method:b00983, C220-web-2025:02-architecture-development-method:b00984, C220-web-2025:02-architecture-development-method:b00985, C220-web-2025:02-architecture-development-method:b00986

<details><summary>展开本节完整英文来源</summary>

12. Phase H: Architecture Change Management

This chapter looks at establishing procedures for managing change to the
new architecture.



Figure 12-1: Phase H: Architecture Change Management

</details>

<a id="tag_12_01"></a>
## 12.1. Objectives

概念：H保持开发周期、执行治理框架并确保EA能力满足当前要求。

适用条件：组织与环境持续变化。

逻辑关系：架构与EA能力同时需要维护。

决策方法：核验当前需求与能力适配。

制品及证据：循环、治理执行和能力管理记录。

适用边界：历史批准不保证当前适配。

来源块：C220-web-2025:02-architecture-development-method:b00987, C220-web-2025:02-architecture-development-method:b00988, C220-web-2025:02-architecture-development-method:b00989

<details><summary>展开本节完整英文来源</summary>

12.1. Objectives

The objectives of Phase H are to:

Ensure that the architecture development cycle is maintained Ensure that the Architecture Governance Framework is executed Ensure that the Enterprise Architecture Capability meets current
requirements

</details>

<a id="tag_12_02"></a>
## 12.2. Inputs

概念：H输入包含架构成果和业务/技术/教训变更。

适用条件：变更管理开始。

逻辑关系：12.2.1—12.2.3区分参考、请求与架构输入。

决策方法：确认变更证据来源。

制品及证据：H输入清单。

适用边界：输入导航不证明变化影响已评估。

来源块：C220-web-2025:02-architecture-development-method:b00990, C220-web-2025:02-architecture-development-method:b00991

<details><summary>展开本节完整英文来源</summary>

12.2. Inputs

This section defines the inputs to Phase H.

</details>

<a id="tag_12_02_01"></a>
## 12.2.1. Reference Materials External to the Enterprise

概念：H外部输入为架构参考材料。

适用条件：评估演进变化需要参考。

逻辑关系：参考需适用于当前架构与环境。

决策方法：筛选相关参考。

制品及证据：参考及出处。

适用边界：最新性须按资料实际版本核实。

来源块：C220-web-2025:02-architecture-development-method:b00992, C220-web-2025:02-architecture-development-method:b00993

<details><summary>展开本节完整英文来源</summary>

12.2.1. Reference Materials External to the Enterprise

Architecture reference materials (see the TOGAF Standard — Architecture Content )

</details>

<a id="tag_12_02_02"></a>
## 12.2.2. Non-Architectural Inputs

概念：H非架构输入为架构工作请求。

适用条件：发起当前变更任务。

逻辑关系：请求进入架构演进流程。

决策方法：确认请求范围与来源。

制品及证据：架构工作请求。

适用边界：请求不是投资批准。

来源块：C220-web-2025:02-architecture-development-method:b00994, C220-web-2025:02-architecture-development-method:b00995

<details><summary>展开本节完整英文来源</summary>

12.2.2. Non-Architectural Inputs

Request for Architecture Work (see the TOGAF Standard — Architecture Content )

</details>

<a id="tag_12_02_03"></a>
## 12.2.3. Architectural Inputs

概念：H输入继承定义要求路线图计划、已签合同符合性与技术/业务/教训请求。

适用条件：分析新技术退役标准、业务发展异常创新或战略变化。

逻辑关系：原EA组织框架和治理模型约束演进，三类请求来源保持区分。

决策方法：确认变更与既有合同目标约束。

制品及证据：业务/技术/教训请求、签合同、评估、架构定义要求计划。

适用边界：存在变更请求不自动批准修改当前架构。

来源块：C220-web-2025:02-architecture-development-method:b00996, C220-web-2025:02-architecture-development-method:b00997

<details><summary>展开本节完整英文来源</summary>

12.2.3. Architectural Inputs

Organizational Model for Enterprise Architecture (see the TOGAF Standard — Architecture Content ), including: Scope of organizations impacted Maturity assessment, gaps, and resolution approach Roles and responsibilities for architecture team(s) Constraints on architecture work Budget requirements Governance and support strategy Tailored Architecture Framework (see the TOGAF Standard — Architecture Content ), including: Tailored architecture method Tailored architecture content (deliverables and artifacts) Configured and deployed tools Statement of Architecture Work (see the TOGAF Standard — Architecture Content ) Architecture Vision (see the TOGAF Standard — Architecture Content ) Architecture Repository (see the TOGAF Standard — Architecture Content ), including: Re-usable building blocks Publicly available reference models Organization-specific reference models Organization standards Architecture Definition Document (see the TOGAF Standard — Architecture Content ) Architecture Requirements Specification (see the TOGAF Standard — Architecture Content ), including: Gap analysis results (from Business, Data, Application, and
Technology Architectures) Architectural requirements Architecture Roadmap (see the TOGAF Standard — Architecture Content ) Change Request (see the TOGAF Standard — Architecture Content ) — technology changes: New technology reports Asset management cost reduction initiatives Technology withdrawal reports Standards initiatives Change Request (see the TOGAF Standard — Architecture Content ) — business changes: Business developments Business exceptions Business innovations Business technology innovations Strategic change developments Change Request (see the TOGAF Standard — Architecture Content ) — from lessons learned Implementation Governance Model (see the TOGAF Standard — Architecture Content ) Architecture Contract (signed) (see the TOGAF Standard — EA Capability and Governance ) Compliance Assessments (see the TOGAF Standard — Architecture Content ) Implementation and Migration Plan (see the TOGAF Standard — Architecture Content )

</details>

<a id="tag_12_03"></a>
## 12.3. Steps

概念：H七步包含价值实现、监测、风险、性能分析、要求、治理与激活变更。

适用条件：持续管理业务价值和架构适配。

逻辑关系：按范围目标与治理调整时序。

决策方法：确定各类监测与决策安排。

制品及证据：七步过程和结果。

适用边界：步骤列表不是自行执行自动批准流程。

来源块：C220-web-2025:02-architecture-development-method:b00998, C220-web-2025:02-architecture-development-method:b00999, C220-web-2025:02-architecture-development-method:b01000, C220-web-2025:02-architecture-development-method:b01001, C220-web-2025:02-architecture-development-method:b01002

<details><summary>展开本节完整英文来源</summary>

12.3. Steps

The level of detail addressed in Phase H will depend on the scope and
goals of the overall architecture effort.

The order of the steps in Phase H as well as the time at which they are
formally started and completed should be adapted to the situation at
hand in accordance with the established Architecture Governance.

The steps in Phase H are as follows:

Establish value realization process; see Section 12.3.1, “Establish Value Realization Process” Deploy monitoring tools; see Section 12.3.2, “Deploy Monitoring Tools” Manage risks; see Section 12.3.3, “Manage Risks” Provide analysis for architecture change management; see Section 12.3.4, “Provide Analysis for Architecture Change Management” Develop change requirements to meet performance targets; see Section 12.3.5, “Develop Change Requirements to Meet Performance Targets” Manage governance process; see Section 12.3.6, “Manage Governance Process” Activate the process to implement change; see Section 12.3.7, “Activate the Process to Implement Change”

</details>

<a id="tag_12_03_01"></a>
## 12.3.1. Establish Value Realization Process

概念：价值实现过程影响业务项目利用EA达成结果。

适用条件：架构产物需要转为实际业务收益。

逻辑关系：项目运用架构是价值实现载体。

决策方法：建立促进项目使用与收益实现安排。

制品及证据：价值实现过程及业务结果依据。

适用边界：使用次数或视图数量不能代替业务价值。

来源块：C220-web-2025:02-architecture-development-method:b01003, C220-web-2025:02-architecture-development-method:b01004

<details><summary>展开本节完整英文来源</summary>

12.3.1. Establish Value Realization Process

Influence business projects to exploit the Enterprise Architecture for
value realization (outcomes).

</details>

<a id="tag_12_03_02"></a>
## 12.3.2. Deploy Monitoring Tools

概念：监测覆盖业务技术变化、价值、EA成熟度、资产、QoS使用与连续性。

适用条件：已部署架构需要持续评估。

逻辑关系：工具必须部署且实际应用；指标连接业务目标与容量/连续性要求。

决策方法：选监测指标和证据渠道。

制品及证据：监测结果、价值指标、成熟度/资产/QoS和连续性要求。

适用边界：监测工具存在不代表监测有效或恢复目标满足。

来源块：C220-web-2025:02-architecture-development-method:b01005, C220-web-2025:02-architecture-development-method:b01006, C220-web-2025:02-architecture-development-method:b01007

<details><summary>展开本节完整英文来源</summary>

12.3.2. Deploy Monitoring Tools

Ensure monitoring tools are deployed and applied to enable the
following:

Monitor technology changes which could impact the Baseline
Architecture Monitor business changes which could impact the Baseline Architecture Business value tracking; e.g., investment appraisal method to
determine value metrics for the business objectives Monitor Enterprise Architecture Capability maturity Track and assess asset management programs Track the Quality of Service (QoS) performances and usage Determine and track business continuity requirements

</details>

<a id="tag_12_03_03"></a>
## 12.3.3. Manage Risks

概念：H管理EA风险并提供IT策略建议。

适用条件：运行中风险变化。

逻辑关系：风险处理为策略决策提供依据。

决策方法：提出风险及策略建议。

制品及证据：EA风险与IT策略建议。

适用边界：建议不等于治理批准或已降低风险。

来源块：C220-web-2025:02-architecture-development-method:b01008, C220-web-2025:02-architecture-development-method:b01009

<details><summary>展开本节完整英文来源</summary>

12.3.3. Manage Risks

Manage Enterprise Architecture risks and provide recommendations for IT
strategy.

</details>

<a id="tag_12_03_04"></a>
## 12.3.4. Provide Analysis for Architecture Change Management

概念：变更分析结合性能、服务管理复核、价值与客户SLA。

适用条件：结果与性能目标出现差距。

逻辑关系：评估请求/报告以确保价值和SLA期望；性能差距和治理遵循共同约束变更。

决策方法：决定应处理哪些性能差距及请求。

制品及证据：性能复核、SLA/价值评估、差距和治理检查。

适用边界：未知服务目标不能补字段消除。

来源块：C220-web-2025:02-architecture-development-method:b01010, C220-web-2025:02-architecture-development-method:b01011, C220-web-2025:02-architecture-development-method:b01012

<details><summary>展开本节完整英文来源</summary>

12.3.4. Provide Analysis for Architecture Change Management

Provide analysis for architecture change management:

Analyze performance Conduct Enterprise Architecture performance reviews with service
management Assess Change Requests and reporting to ensure that the expected value
realization and Service-Level Agreement (SLA) expectations of the
customers are met Undertake a gap analysis of the performance of the Enterprise
Architecture Ensure change management requests adhere to the Enterprise
Architecture Governance and framework

</details>

<a id="tag_12_03_05"></a>
## 12.3.5. Develop Change Requirements to Meet Performance Targets

概念：H针对性能目标提出变更要求并准备行动。

适用条件：监测分析显示需要变化。

逻辑关系：要求推荐连接未达性能与可执行变更。

决策方法：提出支持性能目标的要求。

制品及证据：变更要求建议及行动准备。

适用边界：推荐不等于变更批准或目标已达。

来源块：C220-web-2025:02-architecture-development-method:b01013, C220-web-2025:02-architecture-development-method:b01014

<details><summary>展开本节完整英文来源</summary>

12.3.5. Develop Change Requirements to Meet Performance Targets

Make recommendations on change requirements to meet performance targets
and development of position to act.

</details>

<a id="tag_12_03_06"></a>
## 12.3.6. Manage Governance Process

概念：架构委员会或治理理事会决定技术、业务与豁免变更处理。

适用条件：请求需要治理决策。

逻辑关系：安排并召开有明确决策目的的会议。

决策方法：由适当治理机构决定处理。

制品及证据：委员会会议与变更/豁免决定。

适用边界：架构师不能以分析结果代替实际治理权限。

来源块：C220-web-2025:02-architecture-development-method:b01015, C220-web-2025:02-architecture-development-method:b01016, C220-web-2025:02-architecture-development-method:b01017

<details><summary>展开本节完整英文来源</summary>

12.3.6. Manage Governance Process

Manage governance process and framework for architecture:

Arrange meeting of Architecture Board (or other Governing Council) Hold meeting of the Architecture Board with the aim of the meeting to
decide on handling changes (technology and business and dispensations)

</details>

<a id="tag_12_03_07"></a>
## 12.3.7. Activate the Process to Implement Change

概念：激活变更需新的架构工作请求及投资请求，实施变化应入库。

适用条件：治理决定需推进改变时。

逻辑关系：请求启动工作，已实施变化记录到架构库。

决策方法：提出工作/投资请求并维护实际变更记录。

制品及证据：新请求、投资请求和库中变化。

适用边界：投资请求不是资金批准。

来源块：C220-web-2025:02-architecture-development-method:b01018, C220-web-2025:02-architecture-development-method:b01019, C220-web-2025:02-architecture-development-method:b01020

<details><summary>展开本节完整英文来源</summary>

12.3.7. Activate the Process to Implement Change

Activate the architecture process to implement change:

Produce a new Request for Architecture Work and request for investment Ensure any changes implemented in this phase are captured and
documented in the Architecture Repository

</details>

<a id="tag_12_04"></a>
## 12.4. Outputs

概念：H维护性变化更新架构/框架原则，重大变化产生新ADM请求。

适用条件：变更管理结果交付。

逻辑关系：必要时更新说明书、合同和符合性评估。

决策方法：区分维护与重大变更交付。

制品及证据：架构更新、框架原则、新请求及必要合同/评估更新。

适用边界：不应把全部变更统一归成新周期。

来源块：C220-web-2025:02-architecture-development-method:b01021, C220-web-2025:02-architecture-development-method:b01022, C220-web-2025:02-architecture-development-method:b01023

<details><summary>展开本节完整英文来源</summary>

12.4. Outputs

The outputs of Phase H may include, but are not restricted to:

Architecture updates (for maintenance changes) Changes to architecture framework and principles (for maintenance
changes) New Request for Architecture Work (see the TOGAF Standard — Architecture Content ), to move to another cycle (for major changes) Statement of Architecture Work (see the TOGAF Standard — Architecture Content ), updated if necessary Architecture Contract (see the TOGAF Standard — EA Capability and Governance ), updated if necessary Compliance Assessments (see the TOGAF Standard — Architecture Content ), updated if necessary

</details>

<a id="tag_12_05"></a>
## 12.5. Approach

概念：H持续使架构实现原目标价值并由治理判断更新或新周期。

适用条件：业务增长衰退、技术与解法运营变化。

逻辑关系：架构规格可仍合适但解法/运营需变；容量持续测量，避免只追求优雅，与业务价值直接关联。

决策方法：制定判据、处理符合性及有理由的豁免、高影响管理策略。

制品及证据：容量/使用、价值/性能、变更判据、符合性报告和豁免。

适用边界：源文10倍扩展是例；判断标准依企业风险接受，不能自动固定阈值。

来源块：C220-web-2025:02-architecture-development-method:b01024, C220-web-2025:02-architecture-development-method:b01025, C220-web-2025:02-architecture-development-method:b01026, C220-web-2025:02-architecture-development-method:b01027, C220-web-2025:02-architecture-development-method:b01028, C220-web-2025:02-architecture-development-method:b01029, C220-web-2025:02-architecture-development-method:b01030, C220-web-2025:02-architecture-development-method:b01031, C220-web-2025:02-architecture-development-method:b01032, C220-web-2025:02-architecture-development-method:b01033, C220-web-2025:02-architecture-development-method:b01034, C220-web-2025:02-architecture-development-method:b01035, C220-web-2025:02-architecture-development-method:b01036, C220-web-2025:02-architecture-development-method:b01037, C220-web-2025:02-architecture-development-method:b01038

<details><summary>展开本节完整英文来源</summary>

12.5. Approach

The goal of an architecture change management process is to ensure that
the architecture achieves its original target business value. This
includes managing changes to the architecture in a cohesive and
architected way.

This process will typically provide for the continual monitoring of such
things as governance requests, new developments in technology, and
changes in the business environment. When changes are identified, change
management will determine whether to formally initiate a new
architecture evolution cycle.

Additionally, the architecture change management process aims to
establish and support the implemented Enterprise Architecture as a
dynamic architecture; that is, one having the flexibility to evolve
rapidly in response to changes in the technology and business
environment.

Monitoring business growth and decline is a critical aspect of this
phase. Usage of the Enterprise Architecture is the most important part
of the architecture development cycle. All too often the business has
been left with an Enterprise Architecture that works for the
organization of yesterday but may not give back sufficient capability to
meet the needs of the enterprise of today and tomorrow.

In many cases the architecture continues to fit, but the solutions
underlying them may not, and some changes are required. The Enterprise
Architect needs to be aware of these change requirements and considers
this an essential part of constant renewal of the architecture.

Capacity measurement and recommendations for planning are a key aspect
of this phase. While the architecture has been built to deliver a steady
state Business Architecture with agreed capacity during the lifecycle of
this Enterprise Architecture, the growth or decline in usage needs to be
continually assessed to ensure that maximum business value is achieved.

For example, some Solution Architectures may not lend themselves to be
scalable by a large factor — say 10 — or alternative solutions may be
more economic when scaled up. While the architecture specifications may
not change, the solutions or their operational context may change.

If the performance management and reporting has been built into the work
products through previous phases, then this phase is about ensuring the
effectiveness of these. If there needs to be additional monitoring or
reporting, then this phase will handle the changes.

The value and change management process, once established, will
determine:

The circumstances under which the Enterprise Architecture, or parts of
it, will be permitted to change after deployment, and the process by
which that will happen The circumstances under which the architecture development cycle will
be initiated again to develop a new architecture

The architecture change management process is very closely related to
the Architecture Governance processes of the enterprise, and to the
management of the Architecture Contract (see the TOGAF Standard — EA Capability and Governance )
between the architecture function and the
business users of the enterprise.

In Phase H it is critical that the governance body establish criteria to
judge whether a Change Request warrants just an architecture update or
whether it warrants starting a new cycle of the ADM. It is especially
important to avoid “creeping elegance”, and the governance body must
continue to look for changes that relate directly to business value.

An Architecture Compliance report should state whether the change is
compliant to the current architecture. If it is non-compliant, an
exemption may be granted with valid rationale. If the change has high
impact on the architecture, then a strategy to manage its impact should
be defined.

Guidelines for establishing these criteria are difficult to prescribe,
as many companies accept risk differently, but as the ADM is exercised,
the maturity level of the governance body will improve, and criteria
will become clear for specific needs.

</details>

<a id="tag_12_05_01"></a>
## 12.5.1. Drivers for Change

概念：H协调战略自上而下、运营自下而上及持续交付增量经验。

适用条件：既有基础设施仍有价值且创新/问题驱动变更。

逻辑关系：教训可来自任何层和人，委员会需判请求批准还是已规划过渡项目会解决；业务/技术驱动影响不同。

决策方法：决定是否新变更及与既有过渡计划协调。

制品及证据：变更来源、教训、RFC决定和计划关联。

适用边界：技术请求通常可管理不表示永远无需重构；业务驱动often不是硬规则。

来源块：C220-web-2025:02-architecture-development-method:b01039, C220-web-2025:02-architecture-development-method:b01040, C220-web-2025:02-architecture-development-method:b01041, C220-web-2025:02-architecture-development-method:b01042, C220-web-2025:02-architecture-development-method:b01043, C220-web-2025:02-architecture-development-method:b01044, C220-web-2025:02-architecture-development-method:b01045, C220-web-2025:02-architecture-development-method:b01046, C220-web-2025:02-architecture-development-method:b01047, C220-web-2025:02-architecture-development-method:b01048, C220-web-2025:02-architecture-development-method:b01049, C220-web-2025:02-architecture-development-method:b01050, C220-web-2025:02-architecture-development-method:b01051, C220-web-2025:02-architecture-development-method:b01052, C220-web-2025:02-architecture-development-method:b01053

<details><summary>展开本节完整英文来源</summary>

12.5.1. Drivers for Change

The main purpose for the development of the Enterprise Architecture so
far has been strategic direction and top-down architecture and project
generation to achieve corporate capabilities. However, Enterprise
Architecture does not operate in a vacuum. There is usually an existing
infrastructure and business which is already providing value.

There are also probably drivers for change which are often bottom-up,
based upon modifying the existing infrastructure to enhance
functionality. Enterprise Architecture changes this paradigm by a
strategic top-down approach to a degree, although the delivery of
increments makes the equation more complex.

There are three ways to change the existing infrastructure that have to
be integrated:

Strategic, top-down directed change to enhance or create new
capability (capital) Bottom-up changes to correct or enhance capability (operations and
maintenance) for infrastructure under operations management Experiences with the previously delivered project increments in the
care of operations management, but still being delivered by ongoing
projects

Governance will have to handle the co-ordination of these Requests for
Change, plus there needs to be a lessons learned process to allow for
problems with the recently delivered increments to be resolved and
changes made to the Target Architectures being designed and planned.

A lessons learned process ensures that mistakes are made once and not
repeated. They can come from anywhere and anyone and cover any aspect of
the Enterprise Architecture at any level (strategic, Enterprise
Architecture definition, transition, or project). Often an Enterprise
Architecture-related lesson may be an indirect outcome of a lesson
learned elsewhere in the organization.

The Architecture Board (see the TOGAF Standard — EA Capability and Governance ) assesses and approves Requests for Change
(RFC). An RFC is typically in response to known problems but can also
include improvements. A challenge for the Architecture Board when
handling an RFC is to determine whether it should be approved or whether
a project in a Transition Architecture will resolve the issue.

When assessing project or solution fit into the architecture, there may
also be the case when an innovative solution or RFC drives a change in
the architecture.

In addition, there are many technology-related drivers for architecture
Change Requests. For example:

New technology reports Asset management cost reductions Technology withdrawal Standards initiatives

This type of Change Request is normally manageable primarily through an
enterprise’s change management and Architecture Governance processes.

In addition, there are business drivers for architecture change,
including:

Business-as-usual developments Business exceptions Business innovations Business technology innovations Strategic change

This type of Change Request often results in a complete re-development
of the architecture, or at least in an iteration of a part of the
architecture development cycle, as explained below.

</details>

<a id="tag_12_05_02"></a>
## 12.5.2. Enterprise Architecture Change Management Process

概念：变更可分简化、增量、重构，也可适配组织已有变更方法。

适用条件：尚无类似过程或需支持动态EA。

逻辑关系：过滤受影响阶段；简化通常变更管理、增量可能局部重构、重构需整轮；事件登记资源评估影响支撑分类。

决策方法：按变化性质选择管理路径和受影响阶段。

制品及证据：事件/资源/影响、变化分类、过程方法。

适用边界：三类是可考虑方法，投资降低/增值/增加是解释性关联不能机械分类。

来源块：C220-web-2025:02-architecture-development-method:b01054, C220-web-2025:02-architecture-development-method:b01055, C220-web-2025:02-architecture-development-method:b01056, C220-web-2025:02-architecture-development-method:b01057, C220-web-2025:02-architecture-development-method:b01058, C220-web-2025:02-architecture-development-method:b01059, C220-web-2025:02-architecture-development-method:b01060, C220-web-2025:02-architecture-development-method:b01061, C220-web-2025:02-architecture-development-method:b01062

<details><summary>展开本节完整英文来源</summary>

12.5.2. Enterprise Architecture Change Management Process

The Enterprise Architecture change management process needs to determine
how changes are to be managed, what techniques are to be applied, and
what methodologies used. The process also needs a filtering function
that determines which phases of the architecture development process are
impacted by requirements. For example, changes that affect only
migration may be of no interest in the architecture development phases.

There are many valid approaches to change management, and various
management techniques and methodologies that can be used to manage
change; for example, project management methods such as PRINCE2, service
management methods such as ITIL, management consultancy methods such as
Catalyst, and many others.

An enterprise that already has a change management process in place in a
field other than architecture (for example, in systems development or
project management) may well be able to adapt it for use in relation to
architecture.

The following describes an approach to change management, aimed
particularly at the support of a dynamic Enterprise Architecture, which
may be considered for use if no similar process currently exists. The approach is based on classifying required architectural changes into
one of three categories:

Simplification change : a simplification change can normally be
handled via change management techniques Incremental change : an incremental change may be capable of being
handled via change management techniques, or it may require partial
re-architecting, depending on the nature of the change (see Section 12.5.3, “Guidelines for Maintenance versus Architecture Redesign” for guidelines) Re-architecting change : a re-architecting change requires putting
the whole architecture through the architecture development cycle again

Another way of looking at these three choices is to say that a
simplification change to an architecture is often driven by a
requirement to reduce investment; an incremental change is driven by a
requirement to derive additional value from existing investment; and a
re-architecting change is driven by a requirement to increase investment
in order to create new value for exploitation.

To determine whether a change is simplification, incremental, or
re-architecting, the following activities are undertaken:

Registration of all events that may impact the architecture Resource allocation and management for architecture tasks The process or role responsible for architecture resources has to make
an assessment of what should be done Evaluation of impacts

</details>

<a id="tag_12_05_03"></a>
## 12.5.3. Guidelines for Maintenance versus Architecture Redesign

概念：维护与重构判据须体现业务战略、标准/用户影响和架构层次。

适用条件：选择更新或重新进入ADM。

逻辑关系：两个以上相关方likely重构、一个more likely管理，豁免亦可能管理；重大战略或基础/部署标准变化可能需刷新。

决策方法：由治理按影响判断刷新需要；需要刷新必须发新工作请求。

制品及证据：影响依据、分类决定和新请求（如需）。

适用边界：likely/may不能变为人数硬阈值；十系统缩一是示例，不能凭数量判简化。

来源块：C220-web-2025:02-architecture-development-method:b01063, C220-web-2025:02-architecture-development-method:b01064, C220-web-2025:02-architecture-development-method:b01065, C220-web-2025:02-architecture-development-method:b01066, C220-web-2025:02-architecture-development-method:b01067, C220-web-2025:02-architecture-development-method:b01068, C220-web-2025:02-architecture-development-method:b01069, C220-web-2025:02-architecture-development-method:b01070

<details><summary>展开本节完整英文来源</summary>

12.5.3. Guidelines for Maintenance versus Architecture Redesign

A good guideline is:

If the change impacts two stakeholders or more, then it is likely to
require an architecture redesign and re-entry to the ADM If the change impacts only one stakeholder, then it is more likely to
be a candidate for change management If the change can be allowed under a dispensation, then it is more
likely to be a candidate for change management

For example:

If the impact is significant for the business strategy, then there may
be a need to redo the whole Enterprise Architecture — thus a
re-architecting approach If a new technology or standards emerge, then there may be a need to
refresh the Technology Architecture, but not the whole Enterprise
Architecture — thus an incremental change If the change is at an infrastructure level — for example, ten systems
reduced or changed to one system — this may not change the architecture
above the physical layer, but it will change the Baseline Description of
the Technology Architecture; this would be a simplification change
handled via change management techniques

In particular, a refreshment cycle (partial or complete re-architecting)
may be required if:

The Foundation Architecture needs to be re-aligned with the business
strategy Substantial change is required to components and guidelines for use in
deployment of the architecture Significant standards used in the product architecture are changed
which have significant end-user impact; e.g., regulatory changes

If there is a need for a refreshment cycle, then a new Request for
Architecture Work must be issued (to move to another cycle).

</details>

<a id="chap13"></a>
## 13. ADM Architecture Requirements Management

概念：需求管理贯穿所有ADM相关阶段与周期。

适用条件：需求持续识别及变化。

逻辑关系：管理过程与实际阶段对需求处置保持分工。

决策方法：建立动态需求入口和阶段供应。

制品及证据：需求库、规格、影响评估。

适用边界：不是追加一个Phase I。

来源块：C220-web-2025:02-architecture-development-method:b01071, C220-web-2025:02-architecture-development-method:b01072, C220-web-2025:02-architecture-development-method:b01073, C220-web-2025:02-architecture-development-method:b01074

<details><summary>展开本节完整英文来源</summary>

13. ADM Architecture Requirements Management

This chapter looks at the process of managing architecture requirements
throughout the ADM.



Figure 13-1: ADM Architecture Requirements

</details>

<a id="tag_13_01"></a>
## 13.1. Objectives

概念：需求管理应持续运行、管理任何ADM执行中需求并为每阶段提供相关需求。

适用条件：全部相关阶段执行。

逻辑关系：持续性与可用性支持正确阶段决策。

决策方法：确认需求过程覆盖。

制品及证据：阶段可用需求及管理记录。

适用边界：需求过程不代替相关阶段的优先决策。

来源块：C220-web-2025:02-architecture-development-method:b01075, C220-web-2025:02-architecture-development-method:b01076, C220-web-2025:02-architecture-development-method:b01077

<details><summary>展开本节完整英文来源</summary>

13.1. Objectives

The objectives of the Requirements Management phase are to:

Ensure that the Requirements Management process is sustained and
operates for all relevant ADM phases Manage architecture requirements identified during any execution of
the ADM cycle or a phase Ensure that relevant architecture requirements are available for use
by each phase as the phase is executed

</details>

<a id="tag_13_02"></a>
## 13.2. Inputs

概念：需求输入含已有库、组织框架、说明书愿景、规格和影响评估。

适用条件：需求变化需在架构情境下理解。

逻辑关系：规格记录本轮需求，影响评估体现变更后果。

决策方法：确认需求、范围与已有影响资料。

制品及证据：组织/框架、愿景说明书、库、规格和影响评估。

适用边界：库可多周期，规格/影响评估对象范围不可混同。

来源块：C220-web-2025:02-architecture-development-method:b01078, C220-web-2025:02-architecture-development-method:b01079, C220-web-2025:02-architecture-development-method:b01080

<details><summary>展开本节完整英文来源</summary>

13.2. Inputs

Inputs to the Requirements Management phase are:

A populated Architecture Repository (see the TOGAF Standard — Architecture Content ) Organizational Model for Enterprise Architecture (see the TOGAF Standard — Architecture Content ), including: Scope of organizations impacted Maturity assessment, gaps, and resolution approach Roles and responsibilities for architecture team(s) Constraints on architecture work Budget requirements Governance and support strategy Tailored Architecture Framework (see the TOGAF Standard — Architecture Content ), including: Tailored architecture method Tailored architecture content (deliverables and artifacts) Configured and deployed tools Statement of Architecture Work (see the TOGAF Standard — Architecture Content ) Architecture Vision (see the TOGAF Standard — Architecture Content ) Architecture requirements, populating an Architecture Requirements
Specification (see the TOGAF Standard — Architecture Content ) Requirements Impact Assessment (see the TOGAF Standard — Architecture Content )

</details>

<a id="tag_13_03"></a>
## 13.3. Steps

概念：双列表区分需求管理步骤与ADM阶段步骤，不能读成十项同角色流水线。

适用条件：需求识别/变更/影响/落实全过程。

逻辑关系：1阶段识别；2管理列建立基线并写决定优先级；3管理监测；4阶段识别变化；5管理记录优先/冲突/影响且明确由阶段架构师与相关方排序；6阶段评当前/过去影响与实施或延后；7阶段落实H要求；8管理更新库；9阶段实施；10阶段修订历史差距。

决策方法：确认优先、影响、延期及误删差距的责任方。

制品及证据：需求规格/库、优先共识、影响评估n+1、阶段变更与差距修订。

适用边界：gap requirement特指意外消除需修正目标；不是所有基线删除或新目标差距都自动成缺陷要求。

来源块：C220-web-2025:02-architecture-development-method:b01081, C220-web-2025:02-architecture-development-method:b01082, C220-web-2025:02-architecture-development-method:b01083

<details><summary>展开本节完整英文来源</summary>

13.3. Steps

The steps in the Requirements Management phase are described in the
table below:

Requirements Management Steps ADM Phase Steps Step 1 Identify requirements (typically by analyzing how business
goals/objectives can be met through the design of value streams,
business scenarios, user experiences, or the provision of management
information) and document them in the Architecture Requirements
Specification and Requirements Repository. Step 2 Establish baseline requirements: determine priorities, confirm
stakeholder agreement to priorities, and document them in the
Architecture Requirements Specification and Requirements Repository. Step 3 Monitor baseline requirements. Step 4 Identify new and changed requirements: Remove or re-assess priorities Add requirements and re-assess priorities Modify existing requirements Step 5 Identify changed requirements and record priorities: Identify changed requirements and ensure the requirements are
prioritized by the architect(s) responsible for the current phase, and
by the relevant stakeholders Record new priorities Ensure that any conflicts are identified and managed through the
phases to a successful conclusion and prioritization Generate Requirements Impact Assessment (see the TOGAF Standard — Architecture Content ) for steering the architecture team Notes Changed requirements can come in through any route To ensure that the requirements are properly assessed and prioritized,
this process needs to direct the ADM phases and record the decisions
related to the requirements. The Requirements Management phase needs to determine stakeholder
satisfaction with the decisions Where there is dissatisfaction, the phase remains accountable to ensure
the resolution of the issues and determine next steps. Step 6 Assess impact of changed requirements on current (active) phase Assess impact of changed requirements on previous phases Determine whether to implement change, or defer to later ADM cycle; if
decision is to implement, assess timescale for change management
implementation Issue Requirements Impact Assessment, Version n +1 Step 7 Implement requirements arising from Phase H. The architecture can be changed through its lifecycle by the
Architecture Change Management phase (Phase H). The Requirements
Management process ensures that new or changing requirements that are
derived from Phase H are managed accordingly. Step 8 Update the Architecture Requirements Repository with
information relating to the changes requested, including stakeholder
views affected. Step 9 Implement change in the current phase. Step 10 Assess and revise gap analysis for past phases. The gap analysis in the ADM Phases B through D identifies the gaps
between Baseline and Target Architectures. Certain types of gap can give
rise to gap requirements. The ADM describes two kinds of gap: Something that is present in the baseline, but not in the target
(i.e., eliminated — by accident or design) Something not in the baseline, but present in the target (i.e., new) A “gap requirement” is anything that has been eliminated by accident,
and therefore requires a change to the Target Architecture. If the gap analysis generates gap requirements, then this step will
ensure that they are addressed, documented, and recorded in the
Architecture Requirements Repository, and that the Target Architecture
is revised accordingly.

</details>

<a id="tag_13_04"></a>
## 13.4. Outputs

概念：新/变需求产生影响评估，说明需回访的阶段并逐版完善完整影响。

适用条件：需求变化或当前周期定稿。

逻辑关系：影响包含成本时间业务指标；本轮定稿后更新规格，需求库持续含全部需求信息。

决策方法：决定需回访阶段并完善影响。

制品及证据：需求影响评估、更新规格、更新库。

适用边界：多次迭代不是随意改已批准需求，仍受治理。

来源块：C220-web-2025:02-architecture-development-method:b01084, C220-web-2025:02-architecture-development-method:b01085, C220-web-2025:02-architecture-development-method:b01086, C220-web-2025:02-architecture-development-method:b01087, C220-web-2025:02-architecture-development-method:b01088, C220-web-2025:02-architecture-development-method:b01089

<details><summary>展开本节完整英文来源</summary>

13.4. Outputs

The outputs of the Requirements Management process may include, but are
not restricted to:

Requirements Impact Assessment (see the TOGAF Standard — Architecture Content ) Updated Architecture Requirements Specification (see the TOGAF Standard — Architecture Content : Architecture Requirements Specification), if necessary

The TOGAF Standard — Architecture Content contains a detailed description of architectural
artifacts which may be produced in this phase, describing them in detail
and relating them to entities, attributes, and relationships in the
TOGAF Enterprise Metamodel.

The Architecture Requirements Repository will be updated as part of the
Requirements Management phase and should contain all requirements
information.

When new requirements arise, or existing ones are changed, a
Requirements Impact Assessment is generated, which identifies the phases
of the ADM that need to be revisited to address the changes. The
statement goes through various iterations until the final version, which
includes the full implications of the requirements (e.g., costs,
timescales, and business metrics) on the architecture development. Once
requirements for the current ADM cycle have been finalized then the
Architecture Requirements Specification should be updated.

</details>

<a id="tag_13_05"></a>
## 13.5. Approach

概念：本标题为结构容器，无独立说明段落。

适用条件：阅读该主题时应继续读取下列子节。

逻辑关系：子节分工：tag_13_05_01: 13.5.1. General；tag_13_05_02: 13.5.2. Requirements Development；tag_13_05_03: 13.5.3. Resources

决策方法：不从空容器推出附加规则或完成状态。

制品及证据：实际概念、决策和制品证据见上述子节。

适用边界：空容器覆盖仅证明目录和子节连接，不计额外深度结论。

来源块：C220-web-2025:02-architecture-development-method:b01090

<details><summary>展开本节完整英文来源</summary>

13.5. Approach

</details>

<a id="tag_13_05_01"></a>
## 13.5.1. General

概念：中央需求圈是动态过程，不是静态要求集合。

适用条件：不确定环境下管理阶段间与周期间变化。

逻辑关系：过程自身不处置、解决或排序要求，相关阶段负责；需求库可含多轮信息，区别规格/影响评估。

决策方法：建立全周期记录并让相关阶段承担实际需求决策。

制品及证据：动态库及需求输入/输出、阶段决定。

适用边界：管理步骤5明确阶段架构师/相关方排序，但源表步骤2管理列写determine priorities，与本节过程不排序有张力；保留双方原文，不移动源表列位。

来源块：C220-web-2025:02-architecture-development-method:b01091, C220-web-2025:02-architecture-development-method:b01092, C220-web-2025:02-architecture-development-method:b01093, C220-web-2025:02-architecture-development-method:b01094, C220-web-2025:02-architecture-development-method:b01095, C220-web-2025:02-architecture-development-method:b01096

<details><summary>展开本节完整英文来源</summary>

13.5.1. General

As indicated by the “Requirements Management” circle at the center of
the ADM graphic, the ADM is continuously driven by the Requirements
Management process.

It is important to note that the Requirements Management circle denotes
not a static set of requirements, but a dynamic process whereby
requirements for Enterprise Architecture and subsequent changes to those
requirements are identified, stored, and fed into and out of the
relevant ADM phases, and also between cycles of the ADM.

The ability to deal with changes in requirements is crucial.
Architecture is an activity that by its very nature deals with
uncertainty and change — the “grey area” between what stakeholders
aspire to and what can be specified and engineered as a solution.
Architecture requirements are therefore invariably subject to change in
practice. Moreover, architecture often deals with drivers and
constraints, many of which by their very nature are beyond the control
of the enterprise (changing market conditions, new legislation, etc.),
and which can produce changes in requirements in an unforeseen manner.

Note also that the Requirements Management process itself does not
dispose of, address, or prioritize any requirements; this is done within
the relevant phase of the ADM. It is merely the process for managing
requirements throughout the overall ADM.

It is recommended that an Architecture Requirements Repository (see the TOGAF Standard — Architecture Content ) is used to record and manage all architecture requirements.
Unlike the Architecture Requirements Specification, and the Requirements
Impact Assessment, the Architecture Requirements Repository can hold
information from multiple ADM cycles.

</details>

<a id="tag_13_05_02"></a>
## 13.5.2. Requirements Development

概念：每阶段从预备到H选择已批准本阶段需求，结束更新其状态。

适用条件：阶段执行及范围内外新要求出现。

逻辑关系：范围内未来工作入规格，超说明书范围入库；要求包括功能/非功能及假设约束原则政策标准指南规格，后期可生符合性或实施时窗要求。

决策方法：确认批准需求和状态并判新需求范围。

制品及证据：阶段需求状态、规格/库及功能非功能依据。

适用边界：需求批准要有证据，不能通过状态字段自称获批。

来源块：C220-web-2025:02-architecture-development-method:b01097, C220-web-2025:02-architecture-development-method:b01098, C220-web-2025:02-architecture-development-method:b01099, C220-web-2025:02-architecture-development-method:b01100, C220-web-2025:02-architecture-development-method:b01101, C220-web-2025:02-architecture-development-method:b01102, C220-web-2025:02-architecture-development-method:b01103, C220-web-2025:02-architecture-development-method:b01104

<details><summary>展开本节完整英文来源</summary>

13.5.2. Requirements Development

The first high-level requirements are articulated as part of the
Architecture Vision, generated by means of the business scenario or
analogous technique.

Each phase of the ADM, from Preliminary to Phase H, must select the
approved requirements for that phase as held in the Architecture
Requirements Repository and Architecture Requirements Specification. At
the completion of the phase the status of all such requirements needs to
be updated. During the phase execution, new requirements generated for
future architecture work within the scope of the current Statement of
Architecture Work need to be documented within the Architecture
Requirements Specification, and new requirements which are outside of
the scope of the current Statement of Architecture Work must be input to
the Architecture Requirements Repository for management through the
Requirements Management process.

In each relevant phase of the ADM the architect should identify types of
requirement that must be met by the architecture, including applicable:

Functional requirements Non-functional requirements

When defining requirements the architect should take into account:

Assumptions for requirements Constraints for requirements Domain-specific principles that drive requirements Policies affecting requirements Standards that requirements must meet Organization guidelines for requirements Specifications for requirements

Deliverables in later ADM phases also contain mappings to the design
requirements, and may also generate new types of requirements (for
example, conformance requirements, time windows for implementation).

</details>

<a id="tag_13_05_03"></a>
## 13.5.3. Resources

概念：TOGAF规定有效需求管理要达成什么，不指定或推荐特定过程/工具。

适用条件：选择需求工程资源。

逻辑关系：需求工程方法可丰富，需满足管理结果。

决策方法：依据组织需求选择过程工具。

制品及证据：被选方法工具及满足过程目标的理由。

适用边界：不能把某工具或固定方法写成TOGAF强制。

来源块：C220-web-2025:02-architecture-development-method:b01105, C220-web-2025:02-architecture-development-method:b01106

<details><summary>展开本节完整英文来源</summary>

13.5.3. Resources

The world of requirements engineering is rich with emerging
recommendations and processes for Requirements Management. The TOGAF
Standard does not mandate or recommend any specific process or tool; it
simply states what an effective Requirements Management process should
achieve (i.e., the “requirements for requirements”, if you like).

</details>

<a id="tag_13_05_03_01"></a>
## 13.5.3.1. Business Scenarios

概念：业务场景通过目标如何由流程/价值流及人/机参与者达成识别架构需求。

适用条件：需澄清高层或细化需求。

逻辑关系：分析活动和参与者使目标转为具体要求。

决策方法：选择适用业务场景分析。

制品及证据：目标、流程/价值流、人机参与者和需求。

适用边界：场景是有效技术，不是TOGAF唯一需求发现法。

来源块：C220-web-2025:02-architecture-development-method:b01107, C220-web-2025:02-architecture-development-method:b01108

<details><summary>展开本节完整英文来源</summary>

13.5.3.1. Business Scenarios

A technique used to analyze how a business goal or objective can be met
by a process or value stream. Analyzing where the activities in that
process are performed by human and computer actors is a highly effective
way to identify and clarify architecture requirements. The technique is
detailed in the TOGAF ® Series Guide: Business Scenarios .

</details>

<a id="tag_13_05_03_02"></a>
## 13.5.3.2. Requirements Tools

概念：商业需求管理工具可支持管理，但未必专为架构要求设计。

适用条件：挑选需求工具。

逻辑关系：工具能力应匹配架构需求而非仅名称。

决策方法：评估工具对全周期架构管理适配。

制品及证据：工具适用性依据。

适用边界：原文市场增长描述是源版本陈述，不当成当前产品排名。

来源块：C220-web-2025:02-architecture-development-method:b01109, C220-web-2025:02-architecture-development-method:b01110

<details><summary>展开本节完整英文来源</summary>

13.5.3.2. Requirements Tools

There is a large, and increasing, number of Commercial Off-The-Shelf
(COTS) tools available for the support of Requirements Management,
albeit not necessarily designed for architecture requirements.

</details>

