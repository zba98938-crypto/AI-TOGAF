# 引言与核心概念：当前语义解析

本页为逐节语义解释，不能把解释当全文译文。本卷另有[逐块中文正文](../chinese-text/01-introduction-and-core-concepts.md)，已写正文的最终独立语义校核仍待完成。

[英文及离线原文](../web-2025/volumes/01-introduction-and-core-concepts/index.html)

<a id="chap01"></a>
## 1. Introduction

概念：TOGAF以可裁剪框架支持可持续企业架构；六卷与指南整体协作但允许选取、改造、排除和新增元素。

适用条件：组织采用或更新架构方法，尤其已有方法或大量使用云服务时。

逻辑关系：标准提供通用框架，Library补充特定行业、风格和用途的方法；采用范围不等于全部出版物。

决策方法：先界定组织需要和采用范围，再记录采纳/修改/排除理由。

制品及证据：组织特定框架、采用范围和引用清单；本节未给当前组织的实施授权。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00064, C220-web-2025:01-introduction-and-core-concepts:b00065, C220-web-2025:01-introduction-and-core-concepts:b00066, C220-web-2025:01-introduction-and-core-concepts:b00067, C220-web-2025:01-introduction-and-core-concepts:b00068, C220-web-2025:01-introduction-and-core-concepts:b00069, C220-web-2025:01-introduction-and-core-concepts:b00070, C220-web-2025:01-introduction-and-core-concepts:b00071

<details><summary>展开本节完整英文来源</summary>

1. Introduction

The TOGAF ® Standard is a framework for Enterprise Architecture. It may be
used freely by any organization wishing to develop an Enterprise
Architecture for use within that organization; see Section 1.3.1, “Conditions of Use” .

The TOGAF Standard is developed and maintained by members of The Open
Group, working within the Architecture Forum (refer to www.opengroup.org/architecture-forum ).
The original development of TOGAF Version 1 in 1995 was based on the
Technical Architecture Framework for Information Management (TAFIM),

developed by the US Department of Defense (DoD). The DoD gave The Open
Group explicit permission and encouragement to create Version 1 of the
TOGAF Standard by building on the TAFIM, which itself was the result of
many years of development effort and many millions of dollars of US
Government investment.

Starting from this sound foundation, the members of The Open Group
Architecture Forum have developed successive versions of the TOGAF
Standard and published each one on The Open Group public website.

This version builds on previous versions of the TOGAF Standard and
updates the material available to architecture practitioners to assist
them in building a sustainable Enterprise Architecture. Work on White
Papers and Guides describing how to integrate and use this standard with
other frameworks and architectural styles has highlighted the universal
framework parts of the standard, as well as industry, architecture
style, and purpose-specific tools, techniques, and guidance. This work
is embodied in the TOGAF Library. [ 1 ]

Although all of the TOGAF documentation works together as a whole, it is
expected that organizations will customize it during adoption, and
deliberately choose some elements, customize some, exclude some, and
create others. For example, an organization may wish to adopt the TOGAF metamodel, but elect not to use any of the guidance on how to develop an in-house Technology Architecture because they are heavy consumers of cloud services.

You are recommended to first read the Executive Overview (see Section 1.1, “Executive Overview” ),
which includes an outline of
The Open Group understanding of Enterprise Architecture and answers to
fundamental questions, such as:

Why is an Enterprise Architecture needed? Why use the TOGAF Standard as a framework for Enterprise Architecture?

</details>

<a id="sec-01_01"></a>
## 1.1. Executive Overview

概念：企业可由共享目标的多个组织构成；EA跨系统和职能优化碎片化流程，服务战略与持续运营。

适用条件：多系统依赖、业务转型、并购、技术整合或敏捷技术债等变化。

逻辑关系：利益相关者关切→需求→可理解视图→冲突权衡；应在决策前及变化全过程参与，事后制图仅能记录或执行既决事项。

决策方法：以运营模型界定企业边界；比较转型与运营效率、共享与局部创新的取舍；列示潜在收益而不自动认定实际收益。

制品及证据：目标/驱动/范围、利益相关者需求、权衡视图和收益证据；隐私立法描述为源文概述而非当前法律结论。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00072, C220-web-2025:01-introduction-and-core-concepts:b00073, C220-web-2025:01-introduction-and-core-concepts:b00074, C220-web-2025:01-introduction-and-core-concepts:b00075, C220-web-2025:01-introduction-and-core-concepts:b00076, C220-web-2025:01-introduction-and-core-concepts:b00077, C220-web-2025:01-introduction-and-core-concepts:b00078, C220-web-2025:01-introduction-and-core-concepts:b00079, C220-web-2025:01-introduction-and-core-concepts:b00080, C220-web-2025:01-introduction-and-core-concepts:b00081, C220-web-2025:01-introduction-and-core-concepts:b00082, C220-web-2025:01-introduction-and-core-concepts:b00083, C220-web-2025:01-introduction-and-core-concepts:b00084, C220-web-2025:01-introduction-and-core-concepts:b00085, C220-web-2025:01-introduction-and-core-concepts:b00086, C220-web-2025:01-introduction-and-core-concepts:b00087, C220-web-2025:01-introduction-and-core-concepts:b00088, C220-web-2025:01-introduction-and-core-concepts:b00089, C220-web-2025:01-introduction-and-core-concepts:b00090, C220-web-2025:01-introduction-and-core-concepts:b00091, C220-web-2025:01-introduction-and-core-concepts:b00092, C220-web-2025:01-introduction-and-core-concepts:b00093, C220-web-2025:01-introduction-and-core-concepts:b00094, C220-web-2025:01-introduction-and-core-concepts:b00095, C220-web-2025:01-introduction-and-core-concepts:b00096, C220-web-2025:01-introduction-and-core-concepts:b00097, C220-web-2025:01-introduction-and-core-concepts:b00098, C220-web-2025:01-introduction-and-core-concepts:b00099, C220-web-2025:01-introduction-and-core-concepts:b00100, C220-web-2025:01-introduction-and-core-concepts:b00101, C220-web-2025:01-introduction-and-core-concepts:b00102, C220-web-2025:01-introduction-and-core-concepts:b00103, C220-web-2025:01-introduction-and-core-concepts:b00104, C220-web-2025:01-introduction-and-core-concepts:b00105, C220-web-2025:01-introduction-and-core-concepts:b00106, C220-web-2025:01-introduction-and-core-concepts:b00107

<details><summary>展开本节完整英文来源</summary>

1.1. Executive Overview

This section provides an executive overview of Enterprise Architecture,
the basic concepts of what it is (not just another name for IT
Architecture), and why it is needed. It provides a summary of the
benefits of establishing an Enterprise Architecture and adopting the TOGAF approach to achieve that.

What is an Enterprise?

The TOGAF Standard considers an “enterprise” to be any collection of organizations that have common goals. For example, an enterprise could be:

A whole corporation or a division of a corporation A government agency or a single government department A chain of geographically distant organizations linked together by
common ownership Groups of countries, governments, or governmental organizations (such
as militaries) working together to create common or shareable
deliverables or infrastructures Partnerships and alliances of businesses working together, such as a
consortium or supply chain

The term “Enterprise” in the context of “Enterprise Architecture” can be
applied to either an entire enterprise, encompassing all of its business
activities and capabilities, information, and technology that make up
the entire infrastructure and governance of the enterprise, or to one or
more specific areas of interest within the enterprise. An enterprise may
include partners, suppliers, and customers as well as internal business
units. In all cases, the architecture crosses multiple systems, and
multiple functional groups within the enterprise.

The enterprise operating model concept is useful to determine the nature
and scope of the Enterprise Architecture within an organization. Many
organizations may comprise multiple enterprises, and may develop and
maintain a number of independent Enterprise Architectures to address
each one. These enterprises often have much in common with each other
including processes, functions, and their information systems, and there
is often great potential for wider gain in the use of a common
architecture framework. For example, a common framework can provide a
basis for the development of common building blocks and solutions, and a
shareable Architecture Repository for the integration and re-use of
business models, designs, information, and data.

Why is an Enterprise Architecture Needed?

The purpose of Enterprise Architecture is to optimize across the
enterprise the often fragmented legacy of processes (both manual and
automated) into an integrated environment that is responsive to change
and supportive of the delivery of the business strategy.

The effective management and exploitation of information and Digital
Transformation are key factors to business success, and indispensable
means to achieving competitive advantage. An Enterprise Architecture
addresses this need, by providing a strategic context for the evolution
and reach of digital capability in response to the constantly changing
needs of the business environment.

Furthermore, a good Enterprise Architecture enables you to achieve the
right balance between business transformation and continuous operational
efficiency. It allows individual business units to innovate safely in
their pursuit of evolving business goals and competitive advantage. At
the same time, the Enterprise Architecture enables the needs of the
organization to be met with an integrated strategy which permits the
closest possible synergies across the enterprise and beyond.

And lastly, much of the global privacy legislation demands that
processes around personal data are fully documented in a way that can be
easily understood by untrained readers — such as the data subjects and
judges and lawyers. The penalties for failing to have this can be very
significant.
Clearly the requirement to create documentation
responding to this type of legislation is now crucial.

What are the Benefits of an Enterprise Architecture?

An effective Enterprise Architecture can bring important benefits to the
organization. Potential benefits of an Enterprise Architecture include:

More effective strategic decision-making by C-Level executives and
business leaders: Quick response to change and support for enterprise agility aligned
with the organization strategy Organizational transformation, adopting new trends in business and
technology Organizational change to support Digital Transformation Organizational and operating model changes to improve efficiency and
effectiveness More effective and efficient business operations: Lower business operation costs More Agile organization Business capabilities shared across the organization Lower change management costs More flexible workforce Improved business productivity Improved organization integration in support of mergers and
acquisitions More effective and efficient Digital Transformation and operations: Extending effective reach of the enterprise (e.g., through digital
capability) Bringing all components of the enterprise into a harmonized
environment Lower development, deployment, operations, support, and maintenance
costs Improved interoperability Improved system management Improved ability to address critical enterprise-wide issues (e.g.,
security) Easier upgrade and exchange of system components Better return on existing investment, reduced risk for future
investment: Reduced complexity in the business and IT Maximized return on investment in existing business and IT The flexibility to make, buy, or outsource business and IT solutions Understanding how return on investment changes over time Faster, simpler, and cheaper procurement: Buying decisions are simpler, because the information governing
procurement is readily available in a coherent plan The procurement process is faster — maximizing procurement speed and
flexibility without sacrificing architectural coherence The ability to procure heterogeneous, multi-vendor open systems The ability to secure more economic capabilities

What Specifically Would Prompt the Development of an Enterprise Architecture?

The reasons for embarking on an Enterprise Architecture review or
development are varied, including:

Business-driven initiatives to enable business transformation; for example, to leverage digital services and products as revenue generating assets Technology-driven initiatives for efficiency and cost reduction; for example, technology consolidation initiatives, where the consolidation destination can be physical, virtual, or a combination Merger or acquisition, where the return on investment is only realized after technology efficiencies are realized Management of technical debt accrued by Agile development initiatives

In all of these situations, Enterprise Architecture review or
development is needed to manage complexity when change involves multiple systems with multiple inter-dependencies. Often, key people identify areas of change required in order for new business goals to be met. Such people are commonly referred to as the “stakeholders” in the change. The role of the architect is to address their concerns by:

Identifying and refining the requirements of the stakeholders Developing views of the architecture that show how the concerns and requirements are going to be addressed Showing the trade-offs that are going to be made in reconciling the potentially conflicting concerns of different stakeholders

Without the Enterprise Architecture, it is highly unlikely that all the concerns and requirements will be considered and met.

What is an Architecture Framework

An architecture framework is a foundational structure, or set of
structures, which can be used for developing a broad range of different architectures. It should include a method for describing both a baseline and target state of the enterprise, in terms of a set of building blocks for showing how the building blocks fit together and planning the evolution from baseline to target states.

A framework is typically tailored to meet the specific needs of the
organization. Tailoring of the framework should establish a set of tools and a common vocabulary.

Why Use the TOGAF Standard as a Framework for Enterprise Architecture?

The TOGAF Standard has been developed through the collaborative efforts of the whole community. Using the TOGAF Standard results in Enterprise Architecture that is consistent, reflects the needs of stakeholders, employs best practice, and gives due consideration both to current requirements and the perceived future needs of the business.

Developing and sustaining an Enterprise Architecture is a technically complex process which involves many stakeholders and decision processes in the organization. The TOGAF Standard plays an important role in standardizing and de-risks the architecture development process. The TOGAF Standard provides a best practice framework for adding value, and enables the organization to build workable and economic solutions which address their business issues and needs.

The TOGAF Standard value proposition is to enable organizations to
operate in an efficient and effective way using a proven and recognized set of best practices, across the enterprise and in different sectors to address specific business and technology trends.

A key consideration is that guidance provided by the standard is
intended to be adapted to address different needs and particular
use cases. That means it can be used to create a sustainable Enterprise Architecture for a broad range of use cases, including Agile enterprises and Digital Transformation.

Who Would Benefit From Using the TOGAF Standard?

Any organization undertaking, or planning to undertake, the development and implementation of an Enterprise Architecture for the support of business transformation will benefit from use of the TOGAF Standard.

Organizations seeking Boundaryless Information Flow™ can use the
TOGAF Standard to define and implement the structures and processes to enable access to integrated information within and between enterprises.

Organizations that design and implement Enterprise Architectures using the TOGAF Standard are assured of a design and a procurement
specification that can facilitate an open systems implementation, thus enabling the benefits of open systems with reduced risk.

Organizations that need to adapt to face new business and market
challenges, to improve value propositions to their customers as part of Digital Transformation.

When Should Enterprise Architecture be Done?

To get the greatest benefit from Enterprise Architecture it should be done early and throughout the change process to help decision-makers understand the implications of their decisions. Without this
understanding, costly mistakes can be made and Enterprise Architecture is not serving its fullest potential. Enterprise Architecture done after decisions are made is merely documentation of those decisions or at best enforcement of those decisions. No insight is gained as to the effect of those decisions which could be far-reaching and perhaps detrimental.

</details>

<a id="sec-01_02"></a>
## 1.2. Structure of this Document

概念：本卷区分总览、文档集、核心概念、定义、参考文献、补充词汇与缩略语。

适用条件：阅读、检索或确定引用层次时。

逻辑关系：正文概念与定义层不同；附录A是引用索引，不能把被引出版物计为本卷正文。

决策方法：按问题选择章节，术语先查第四章再查补充词汇；引用回到实际原文。

制品及证据：阅读范围及引用定位；本节没有架构决策或新制品要求。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00108, C220-web-2025:01-introduction-and-core-concepts:b00109, C220-web-2025:01-introduction-and-core-concepts:b00110

<details><summary>展开本节完整英文来源</summary>

1.2. Structure of this Document

This document introduces the TOGAF Standard and the TOGAF Library, and includes definitions and referenced materials relevant to the individual elements of the Standard.

This chapter provides a general introduction to Enterprise Architecture and the TOGAF Standard Chapter 2, The TOGAF Documentation Set describes: The scope and structure of the materials that make up the TOGAF Standard The scope and structure of the TOGAF Library Chapter 3, Core Concepts describes the core concepts that are used across the components of the TOGAF Standard Chapter 4, Definitions contains definitions of terms that are used consistently across the components of the TOGAF
Standard Appendix A, Referenced Documents contains a list of documents referenced in the TOGAF Standard Appendix B, Glossary of Supplementary Definitions contains a supplementary list of definitions of terms that may be
encountered when reading the materials that make up the TOGAF Standard Appendix C, Acronyms and Abbreviations contains a list of commonly used abbreviations

</details>

<a id="sec-01_03"></a>
## 1.3. Information on Using the TOGAF Standard

概念：使用信息按在线查看、授权下载和费用说明展开。

适用条件：保存、内部使用或分发标准前。

逻辑关系：本父节仅组织1.3.1—1.3.3；具体许可条件须读子节与版权通知。

决策方法：分别识别查看、保存、内部使用和其他用途。

制品及证据：获取方式与许可记录；本节不构成对任何外部用途的授权。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00111

<details><summary>展开本节完整英文来源</summary>

1.3. Information on Using the TOGAF Standard

</details>

<a id="sec-01_03_01"></a>
## 1.3.1. Conditions of Use

概念：在线查看无需许可；下载保存按许可办理，内部架构使用与其他用途分开。

适用条件：使用和保管源标准时。

逻辑关系：免费内部使用不推出任意复制、检索保存、传播或商业使用；首部版权通知还列有生成式AI用途限制。

决策方法：保留实际获取与许可条件；对用途范围不能从可访问性推出授权。

制品及证据：源版权与许可条款原样保留；本次解析不判定用户法律权限。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00112, C220-web-2025:01-introduction-and-core-concepts:b00113, C220-web-2025:01-introduction-and-core-concepts:b00114

<details><summary>展开本节完整英文来源</summary>

1.3.1. Conditions of Use

The TOGAF Standard is freely available for viewing online without a license. Alternatively, it can be downloaded and stored under license, as explained on the TOGAF information website.

In either case, the TOGAF Standard can be used freely by any
organization wishing to do so to develop an architecture for use within that organization. No part of it may be reproduced, stored in a retrieval system, or transmitted, in any form or by any means,
electronic, mechanical, photocopying, recording, or otherwise, for any other purpose including, but not by way of limitation, any use for commercial gain, without the prior permission of the copyright owners.

</details>

<a id="sec-01_03_02"></a>
## 1.3.2. How Much Does the TOGAF Standard Cost?

概念：免费内部采用支持实践反馈和降低整合障碍；商业使用仍受限制。

适用条件：估算标准采用成本或说明价格时。

逻辑关系：免费材料与架构工作/采购实际费用不同；本段目的陈述不是节省费用的项目证明。

决策方法：区分标准许可费用和实施总成本；价格按本地2025版源陈述引用。

制品及证据：费用假设与出处；未给当前会员费或市场价格。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00115, C220-web-2025:01-introduction-and-core-concepts:b00116, C220-web-2025:01-introduction-and-core-concepts:b00117, C220-web-2025:01-introduction-and-core-concepts:b00118

<details><summary>展开本节完整英文来源</summary>

1.3.2. How Much Does the TOGAF Standard Cost?

The Open Group is committed to delivering greater business efficiency by bringing together buyers and suppliers of information systems to lower the barriers of integrating new technology across the enterprise. Its goal is to realize the vision of Boundaryless Information Flow.

The TOGAF Standard is a key part of its strategy for achieving this
goal, and The Open Group wants it to be taken up and used in practical architecture projects, and the experience from its use fed back to help improve it.

The Open Group therefore publishes it on its public web server, and
allows and encourages its reproduction and use free-of-charge by any organization wishing to use it internally to develop an Enterprise Architecture. (There are, however, restrictions on its commercial use; see Section 1.3.1, “Conditions of Use” .)

</details>

<a id="sec-01_03_03"></a>
## 1.3.3. Downloads

概念：可打印PDF等下载按许可提供，全部内部使用可获得免费许可。

适用条件：选择正式下载与归档格式时。

逻辑关系：下载入口指正式授权材料；当前网页MHTML副本不能改称正式PDF。

决策方法：记录实际下载格式、版本、时间与许可来源。

制品及证据：下载记录、文件指纹及源链接；本节没有下载状态自动验收规则。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00119, C220-web-2025:01-introduction-and-core-concepts:b00120

<details><summary>展开本节完整英文来源</summary>

1.3.3. Downloads

Downloads of the TOGAF Standard, including printable PDF files, are available under license from the TOGAF information website (refer to www.opengroup.org/togaf/downloads ).
The license is free to any organization wishing to use the standard
entirely for internal purposes (for example, to develop an Enterprise Architecture for use within that organization).

</details>

<a id="sec-01_04"></a>
## 1.4. Why Join The Open Group?

概念：加入组织可获得论坛参与、交流、未出版成果访问及案例同行评阅。

适用条件：选择协作或标准演进参与方式时。

逻辑关系：会员价值陈述与使用公开标准分别成立；会员不是所有内部采用的前提。

决策方法：把协作需求与成本单独评估，不从源营销陈述推导当前ROI。

制品及证据：成员参与/同行评阅计划；实际组织预算未知。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00121, C220-web-2025:01-introduction-and-core-concepts:b00122, C220-web-2025:01-introduction-and-core-concepts:b00123, C220-web-2025:01-introduction-and-core-concepts:b00124, C220-web-2025:01-introduction-and-core-concepts:b00125, C220-web-2025:01-introduction-and-core-concepts:b00126

<details><summary>展开本节完整英文来源</summary>

1.4. Why Join The Open Group?

Organizations wishing to reduce the time, cost, and risk of implementing multi-vendor solutions that integrate within and between enterprises need The Open Group as their key partner.

The Open Group brings together the buyers and suppliers of information systems worldwide, and enables them to work together, both to ensure that IT solutions meet the needs of customers, and to make it easier to integrate IT across the enterprise. The TOGAF Standard is a key enabler in this task.

Yes, the TOGAF Standard itself is freely available. But how much will you spend on developing or updating your Enterprise Architecture? And how much will you spend on procurements based on that architecture? The price of membership of The Open Group is insignificant in comparison with these amounts.

In addition to the general benefits of membership, as a member of The Open Group you will be eligible to participate in The Open Group Architecture Forum, which is the development program within which the TOGAF Standard is evolved, and in which TOGAF users come together to exchange information and feedback. Members of the Architecture Forum gain:

Immediate access to the fruits of the current TOGAF work program (not publicly available until publication of the next edition of the TOGAF Standard); i.e., the latest information on the standard Exchange of experience with other customer and vendor organizations involved in Enterprise Architecture in general, and networking with architects using the TOGAF Standard in significant architecture development projects around the world Peer review of specific architecture case study material

</details>

<a id="chap02"></a>
## 2. The TOGAF Documentation Set

概念：文档集由基础标准、系列指南和更广的Library组成。

适用条件：核对已收齐范围与知识入口时。

逻辑关系：基础六卷相互关联；指南是标准的实用指导部分；Library还含其他参考材料。

决策方法：用出版物类别而非文件数量判断覆盖。

制品及证据：分类目录与版本记录；不能把26份指南等同所有TOGAF资料。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00127

<details><summary>展开本节完整英文来源</summary>

2. The TOGAF Documentation Set

</details>

<a id="sec-02_01"></a>
## 2.1. Structure of the TOGAF Documentation Set

概念：图2-1展示Open Group Library、TOGAF Library、标准与其他参考材料的嵌套范围。

适用条件：组装企业参考资料库时。

逻辑关系：图示包含层级表明资料所属，不表明每项必须采用或全部已取得。

决策方法：将标准基础内容、指南、白皮书等分别登记。

制品及证据：资料分类与来源映射；图中图标不证明某具体出版物已解析。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00128, C220-web-2025:01-introduction-and-core-concepts:b00129, C220-web-2025:01-introduction-and-core-concepts:b00130, C220-web-2025:01-introduction-and-core-concepts:b00131

<details><summary>展开本节完整英文来源</summary>

2.1. Structure of the TOGAF Documentation Set

The TOGAF documentation set consists of a portfolio of documents
illustrated in Figure 2-1 .



Figure 2-1: The TOGAF Documentation Set

</details>

<a id="sec-02_01_00_01"></a>
## 2.1.1. The TOGAF Standard

概念：基础标准以独立但紧密关联的文档陈述通用EA/IT架构方法。

适用条件：确定通用框架的规范来源时。

逻辑关系：行业共识与开放标准支持互操作；文档独立性允许专业化阅读，不能忽略依赖。

决策方法：选择适用卷同时登记关联输入输出。

制品及证据：基础标准卷清单与适用性理由；不是固定项目执行序列。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00132, C220-web-2025:01-introduction-and-core-concepts:b00133, C220-web-2025:01-introduction-and-core-concepts:b00134

<details><summary>展开本节完整英文来源</summary>

2.1.1. The TOGAF Standard

The TOGAF Standard describes the generally applicable approach to Enterprise and IT Architecture. It is presented as a series of
free-standing, but closely linked documents, as shown in Figure 2-1 .

The TOGAF Standard is a standard of The Open Group. The Open Group works with customers and suppliers of technology products and services, and with consortia and other standards organizations to capture, clarify, and integrate current and emerging requirements, establish standards and policies, and share best practices. Standards ensure openness,
interoperability, and consensus.

</details>

<a id="sec-02_01_00_02"></a>
## 2.1.2. The TOGAF Library

概念：Library补充实际应用的指导材料。

适用条件：需要具体情境方法、模板和模式时。

逻辑关系：指导性材料支持框架；不自动替代基础定义或当前业务事实。

决策方法：按情境筛选参考材料并核对版本。

制品及证据：参考材料选取清单；未规定全部Library一律使用。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00135, C220-web-2025:01-introduction-and-core-concepts:b00136

<details><summary>展开本节完整英文来源</summary>

2.1.2. The TOGAF Library

The TOGAF Library is a portfolio of additional guidance material, which supports the practical application of the TOGAF approach.

</details>

<a id="sec-02_02"></a>
## 2.2. The TOGAF Standard

概念：六卷基础内容与持续演进系列指南共同构成标准；组织可增量采用或与现有框架融合。

适用条件：部署TOGAF、决定采用范围和特定风格支持时。

逻辑关系：方法、内容、技术、应用和能力治理共同支持架构；不是每份指南在每情境都相关。

决策方法：先识别实践需求再选择卷/指南；允许排除但应识别其留下的职责和证据缺口。

制品及证据：组织特定框架与定制理由；指南更新速度较快但本地范围仍以实际版本为准。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00137, C220-web-2025:01-introduction-and-core-concepts:b00138, C220-web-2025:01-introduction-and-core-concepts:b00139, C220-web-2025:01-introduction-and-core-concepts:b00140, C220-web-2025:01-introduction-and-core-concepts:b00141, C220-web-2025:01-introduction-and-core-concepts:b00142, C220-web-2025:01-introduction-and-core-concepts:b00143, C220-web-2025:01-introduction-and-core-concepts:b00144, C220-web-2025:01-introduction-and-core-concepts:b00145, C220-web-2025:01-introduction-and-core-concepts:b00146, C220-web-2025:01-introduction-and-core-concepts:b00147, C220-web-2025:01-introduction-and-core-concepts:b00148, C220-web-2025:01-introduction-and-core-concepts:b00149, C220-web-2025:01-introduction-and-core-concepts:b00150, C220-web-2025:01-introduction-and-core-concepts:b00151, C220-web-2025:01-introduction-and-core-concepts:b00152, C220-web-2025:01-introduction-and-core-concepts:b00153, C220-web-2025:01-introduction-and-core-concepts:b00154, C220-web-2025:01-introduction-and-core-concepts:b00155, C220-web-2025:01-introduction-and-core-concepts:b00156, C220-web-2025:01-introduction-and-core-concepts:b00157

<details><summary>展开本节完整英文来源</summary>

2.2. The TOGAF Standard

The TOGAF Standard is an open, industry consensus framework for Enterprise Architecture.

It is a foundational framework, which means that it is applicable to the development of any kind of architecture in any context. This foundational framework is supplemented by The Open Group TOGAF Library, an extensive and growing portfolio of guidance material, providing practical guidance in the application of the TOGAF framework in specific contexts.

The structure of the TOGAF Standard reflects the structure and content of an Architecture Capability within an enterprise, as shown in Figure 2-2 .



Figure 2-2: Structure of the TOGAF Standard

The TOGAF Standard Fundamental Content is presented as six free-standing
documents:

The TOGAF Standard — Introduction and Core Concepts (this document) The TOGAF Standard — Architecture Development Method This document describes the TOGAF Architecture Development Method (ADM)
— an iterative approach to developing an Enterprise Architecture. The TOGAF Standard — ADM Techniques This document contains a collection of techniques available for use in
applying the TOGAF approach and the TOGAF ADM. The TOGAF Standard — Applying the ADM This document contains guidelines for adapting the TOGAF ADM to address
the specific style of architecture required in a practical context. The TOGAF Standard — Architecture Content This document describes the TOGAF Content Framework and a structured metamodel for architectural artifacts, the use of re-usable Architecture Building Blocks (ABBs), and an overview of typical architecture
deliverables. The TOGAF Standard — EA Capability and Governance This document discusses the organization, processes, skills, roles, and
responsibilities required to establish and operate an architecture
function within an enterprise and describes an Enterprise Architecture
governance framework.

The intention of dividing the TOGAF Standard into these independent
documents is to allow for different areas of specialization to be
considered in detail and potentially addressed in isolation. Although
all the constituent documents work together as a whole, it is also
feasible to select particular documents for adoption while excluding
others. For example, an organization may wish to adopt the ADM process,
but elect not to use any of the materials relating to Architecture
Capability. As an open framework, such use is encouraged, particularly
in the following situations:

Organizations that are new to the TOGAF approach and wish to
incrementally adopt TOGAF concepts are expected to focus on particular
constituent documents of the standard for initial adoption, with other
areas tabled for later consideration Organizations that have already deployed architecture frameworks may
choose to merge these frameworks with aspects of the TOGAF Standard

The TOGAF Standard comprises the TOGAF Fundamental Content and a
collection of TOGAF Series Guides, which provide the practical guidance
in the application of the TOGAF Standard.

Figure 2-3 depicts the structure and scope of the TOGAF Standard.



Figure 2-3: The TOGAF Standard

Besides the core framework content covered by the six documents
explained above, the standard provides guidance to address specific
concerns and use cases through the TOGAF Series Guides.

The TOGAF Series Guides are designed to support more specific needs from
practitioners who need further explanation or more detail than that
provided in the core content.

Not all the TOGAF Series Guides will be relevant in every situation.
However, Enterprise Architects who are planning the deployment of the TOGAF Standard should be aware of the guidance available.

This content will evolve more rapidly than the core content to cover new
needs as they emerge from market trends and the needs of the industry. There is a set of activities running continuously in The Open Group Architecture Forum to deliver this content following a continuous and incremental delivery pipeline.

Examples of the areas covered by this guidance material are:

Strategy decision-making and business value-oriented decisions Business Architecture and operating model description Information and data management Information system guidance Information reference models and data integration models Technology Architecture: how Enterprise Architecture as a practice can
be applied to adopt new technology trends to assess if the organization
owns the right capabilities to support the new technology adoption Security Architecture: how the TOGAF Standard can be applied to
deliver and support Security Architecture and risk management How Enterprise Architecture as a practice and the TOGAF Standard can
be applied to support the Agile enterprise, to be delivered following an
Agile style, and how the standard can support organizations using Agile
methodologies How Enterprise Architecture as a practice and the TOGAF Standard
support the digital enterprise so that organizations can deliver digital
products, and improve their digital offering and digital value
proposition How the standard can be applied with other standards and methodologies
of The Open Group such as the O-AA™ Standard, the DPBoK™
Standard, the IT4IT™ Reference Architecture, the ArchiMate ® Specification, Microservices Architecture (MSA), security standards, and
also with other standards bodies’ standards and best practices

The complete set of TOGAF Series Guides can be found at www.opengroup.org/library/guides/togaf/togaf-series-guides .

</details>

<a id="sec-02_03"></a>
## 2.3. The TOGAF Library

概念：Library是可用指南、模板、模式等参考资源集合，由Architecture Forum治理。

适用条件：利用外部资产加速组织特定架构时。

逻辑关系：Library支持企业Architecture Repository的Reference Library部分；参考资产不是已采用标准。

决策方法：按适用性、可靠性、可复用性分类和选用。

制品及证据：参考库条目、采用状态与来源；分类模型不是成熟等级或强制顺序。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00158, C220-web-2025:01-introduction-and-core-concepts:b00159, C220-web-2025:01-introduction-and-core-concepts:b00160, C220-web-2025:01-introduction-and-core-concepts:b00161, C220-web-2025:01-introduction-and-core-concepts:b00162, C220-web-2025:01-introduction-and-core-concepts:b00163, C220-web-2025:01-introduction-and-core-concepts:b00164, C220-web-2025:01-introduction-and-core-concepts:b00165

<details><summary>展开本节完整英文来源</summary>

2.3. The TOGAF Library

Accompanying the TOGAF Standard is a broad portfolio of guidance
material, known as the TOGAF Library, to
support the practical application of the TOGAF approach. The TOGAF
Library is a reference library containing guidelines, templates,
patterns, and other forms of reference material to accelerate the creation of new architectures for the enterprise.

The TOGAF Library is maintained under the governance of The Open Group Architecture Forum.

The TOGAF Library supports one of the classes of information in the TOGAF Enterprise Architecture Repository, the Reference Library.

The Reference Library provides guidelines, templates, patterns, and
other forms of reference material that can be leveraged in order to
accelerate the creation of new architectures for the enterprise.

The TOGAF Library is a Reference Library of potentially useful
resources. The TOGAF Library follows a categorization model based on capabilities and features that can be delivered into the market through
different sets of documents and resources, as depicted in Figure 2-4 .



Figure 2-4: The TOGAF Library Continuum

</details>

<a id="chap03"></a>
## 3. Core Concepts

概念：核心概念提供跨六卷解释ADM、服务、抽象、制品、治理、敏捷和风险的共同语义。

适用条件：跨卷跨指南统一术语时。

逻辑关系：这些概念相互关联但身份不同；不能以一个图或一个PASS概括全部。

决策方法：用本章概念约束跨文档解释，再回到具体卷方法。

制品及证据：术语/关系映射与源问题记录；不是现成项目方案。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00166, C220-web-2025:01-introduction-and-core-concepts:b00167

<details><summary>展开本节完整英文来源</summary>

3. Core Concepts

For the purposes of the TOGAF Standard, the core concepts provided in
this chapter apply.

</details>

<a id="sec-03_01"></a>
## 3.1. What is the TOGAF Standard?

概念：TOGAF提供接受、产出、使用和维护EA的方法与工具，基于迭代、最佳实践及复用资产。

适用条件：建设或运行架构实践。

逻辑关系：方法过程与已有架构资产共同支持持续生命周期。

决策方法：明确需要的架构服务和可复用资产，再裁剪方法。

制品及证据：组织方法和资产引用；框架本身不是某架构已被接受的证据。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00168, C220-web-2025:01-introduction-and-core-concepts:b00169

<details><summary>展开本节完整英文来源</summary>

3.1. What is the TOGAF Standard?

The TOGAF Standard is an architecture framework. It provides the methods and tools for assisting in the acceptance, production, use, and maintenance of an Enterprise Architecture. It is based on an iterative process model supported by best practices and a re-usable set of existing architecture assets; see Section 2.2, “The TOGAF Standard” .

</details>

<a id="sec-03_02"></a>
## 3.2. What is Architecture in the Context of the TOGAF Standard?

概念：架构有ISO实体环境与治理原则含义，以及TOGAF组件结构、相互关系和演进原则含义。

适用条件：统一跨标准术语和架构描述时。

逻辑关系：TOGAF采纳但不严格等同42010:2022全部术语；企业作为系统。

决策方法：明确当前“架构”是实体属性、结构还是描述，保留定义上下文。

制品及证据：术语映射及架构描述；不能把42010或TOGAF定义强制解释为完全同义。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00170, C220-web-2025:01-introduction-and-core-concepts:b00171, C220-web-2025:01-introduction-and-core-concepts:b00172, C220-web-2025:01-introduction-and-core-concepts:b00173, C220-web-2025:01-introduction-and-core-concepts:b00174, C220-web-2025:01-introduction-and-core-concepts:b00175

<details><summary>展开本节完整英文来源</summary>

3.2. What is Architecture in the Context of the TOGAF Standard?

ISO/IEC/IEEE 42010:2022 defines “architecture” as:

“[The] fundamental concepts or properties of an entity in its environment and governing principles for the realization and evolution of this entity and its related life cycle processes.”

The TOGAF Standard embraces but does not strictly adhere to ISO/IEC/IEEE
42010:2022 terminology. In addition to the ISO/IEC/IEEE 42010:2022
definition of “architecture”, the TOGAF Standard defines a second
meaning depending upon the context:

“The structure of components, their inter-relationships, and the
principles and guidelines governing their design and evolution over
time.”

The TOGAF Standard considers the enterprise as a system and endeavors to
strike a balance between promoting the concepts and terminology drawn
from relevant standards, and commonly accepted terminology that is
familiar to the majority of the TOGAF readership. For more on
terminology, refer to Chapter 4, Definitions and the TOGAF Standard — Architecture Content .

</details>

<a id="sec-03_03"></a>
## 3.3. What Kind of Architecture Does the TOGAF Standard Deal With?

概念：业务、数据、应用、技术是常用四域；信息、风险安全、数字架构可组合多个域的视图。

适用条件：划分责任与建模范围。

逻辑关系：多维领域由相关视图组合，不应将安全/信息限在单一技术域。

决策方法：按关切选择跨域视图与责任，检查业务到数据/应用/技术的连接。

制品及证据：域范围与交叉视图；四域不是封闭穷举。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00176, C220-web-2025:01-introduction-and-core-concepts:b00177, C220-web-2025:01-introduction-and-core-concepts:b00178, C220-web-2025:01-introduction-and-core-concepts:b00179, C220-web-2025:01-introduction-and-core-concepts:b00180, C220-web-2025:01-introduction-and-core-concepts:b00181

<details><summary>展开本节完整英文来源</summary>

3.3. What Kind of Architecture Does the TOGAF Standard Deal With?

There are four architecture domains that are commonly accepted as
subsets of an overall Enterprise Architecture, all of which the TOGAF
Standard is designed to support:

The Business Architecture defines the business strategy, governance,
organization, and key business processes The Data Architecture describes the structure of an organization’s
logical and physical data assets and data management resources The Application Architecture provides a blueprint for the individual
applications to be deployed, their interactions, and their relationships
to the core business processes of the organization The Technology Architecture describes the digital architecture and
the logical software and hardware infrastructure capabilities and
standards that are required to support the deployment of business, data,
and applications services. This includes digital services, Internet of
Things (IoT), social media infrastructure, cloud services, IT
infrastructure, middleware, networks, communications, processing,
standards, etc.

There are many other domains that could be defined by combining
appropriate views of the Business, Data, Application, and Technology
domains. For example:

Information Architecture Risk and Security Architectures Digital Architecture

The TOGAF framework enables the creation of these multi-dimensional
views and categorizes them to create specific domains that enable an
enterprise to consider the wider scope of their enterprise and
capabilities.

</details>

<a id="sec-03_04"></a>
## 3.4. Architecture Development Method

概念：ADM是定义与实现架构的可重复、迭代参考模型，含预备、A—H和贯穿需求管理。

适用条件：规划架构活动、迭代或敏捷裁剪。

逻辑关系：圆图不能当强制流程顺序；源明确不规定固定阶段序列或瀑布；指南补“如何做”。

决策方法：选择适用活动、迭代与回访条件，保留需求贯穿关系；不得创建Phase I。

制品及证据：裁剪ADM、批准范围、阶段输出与需求变更链；实际顺序依情境决定。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00182, C220-web-2025:01-introduction-and-core-concepts:b00183, C220-web-2025:01-introduction-and-core-concepts:b00184, C220-web-2025:01-introduction-and-core-concepts:b00185, C220-web-2025:01-introduction-and-core-concepts:b00186, C220-web-2025:01-introduction-and-core-concepts:b00187, C220-web-2025:01-introduction-and-core-concepts:b00188, C220-web-2025:01-introduction-and-core-concepts:b00189, C220-web-2025:01-introduction-and-core-concepts:b00190, C220-web-2025:01-introduction-and-core-concepts:b00191, C220-web-2025:01-introduction-and-core-concepts:b00192, C220-web-2025:01-introduction-and-core-concepts:b00193, C220-web-2025:01-introduction-and-core-concepts:b00194

<details><summary>展开本节完整英文来源</summary>

3.4. Architecture Development Method

The TOGAF Architecture Development Method (ADM) provides a tested and
repeatable process for developing architectures. The ADM includes
establishing an architecture framework, developing architecture content,
transitioning, and governing the realization of architectures.

All of these activities are carried out within an iterative cycle of
continuous architecture definition and realization that allows
organizations to transform their enterprises in a controlled manner in
response to business goals and opportunities. This is illustrated in Figure 3-1 .



Figure 3-1: Architecture Development Cycle

Phases within the ADM are as follows:

The Preliminary Phase describes the preparation and initiation
activities required to create an Architecture Capability including
customization of the TOGAF framework and definition of Architecture
Principles Phase A: Architecture Vision describes the initial phase of an
architecture development cycle It includes information about defining the scope of the architecture
development initiative, identifying the stakeholders, creating the
Architecture Vision, and obtaining approval to proceed with the
architecture development. Phase B: Business Architecture describes the development of a
Business Architecture to support the agreed Architecture Vision Phase C: Information Systems Architectures describes the development
of Information Systems Architectures to support the agreed Architecture
Vision Phase D: Technology Architecture describes the development of the
Technology Architecture to support the agreed Architecture Vision Phase E: Opportunities & Solutions conducts initial implementation
planning and the identification of delivery vehicles for the
architecture defined in the previous phases Phase F: Migration Planning addresses how to move from the Baseline
to the Target Architectures by finalizing a detailed Implementation and
Migration Plan Phase G: Implementation Governance provides an architectural
oversight of the implementation Phase H: Architecture Change Management establishes procedures for
managing change to the new architecture Requirements Management operates the process of managing
architecture requirements throughout the ADM

The description of the phases of the ADM in the TOGAF Standard — Architecture Development Method focuses on recommendations on what may be done to define and deploy an
Enterprise Architecture.

Guidance on how to do what is specified can be found in the TOGAF
Series Guides (see Section 2.2, “The TOGAF Standard” ).
A full list of referenced TOGAF Series Guides is included
in Appendix A, Referenced Documents .

The TOGAF framework recommends that the ADM be adapted to meet the needs
of the enterprise and to support different architecture styles; see Section 3.15, “Using the TOGAF Framework with Different Architecture Styles” .

In particular, the ADM does not:

Mandate that the phases must be performed in any specific sequence Mandate a “waterfall” method

The TOGAF Standard describes how the ADM can be used iteratively to develop a comprehensive Enterprise Architecture landscape. Rather than
viewing the ADM graphic as a process model, it is helpful to view it as a reference model defining what has to be done in order to deliver solutions in an architected way and identifying interacting components across the enterprise and the relationships between them.

</details>

<a id="sec-03_05"></a>
## 3.5. Enterprise Architecture Services

概念：EA活动可组织成六类服务，前四类客户导向，后两类支持架构团队及实践。

适用条件：设计架构服务产品和客户接口。

逻辑关系：各服务按需要使用适当ADM活动，独立于具体运营模型；候选服务非强制组织层级。

决策方法：按客户决策与期望结果选服务，避免把分类带当独立服务或自动变阶段。

制品及证据：客户/提供者/交付物/结果服务目录；实际服务能力及容量须取证。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00195, C220-web-2025:01-introduction-and-core-concepts:b00196, C220-web-2025:01-introduction-and-core-concepts:b00197, C220-web-2025:01-introduction-and-core-concepts:b00198

<details><summary>展开本节完整英文来源</summary>

3.5. Enterprise Architecture Services

Activities described in the ADM are often provided through a service delivery model. The services are organized and presented in service
categories. These services address specific needs independent of an
organization’s specific operation model. Any given service described
utilizes the appropriate activities in the ADM to address a given need.

Table 3-1 summarizes the proposed service categories
and provides some context. The first four categories are
customer-centric and the others are more internally centered on
architects. Each service category is briefly described in the following
subsections.

Table 3-1:  Service Categories and Descriptors Categories Typical Customer Descriptor Typical Provider Descriptor Deliverable(s) Desired
Result Customer-Centric Enterprise Support Services C-level management Enterprise analysts
using Enterprise Architecture as a tool Answers to questions Assessment reports Recommendations Better enterprise decisions Lower risk Design Support Services Program-level decision-makers Enterprise
Architect builder/modeler MVAs (including standards and compliance criteria, roadmaps) for
programs Compliance guidance Compliance reports Better design decisions Successful programs and projects Development Support Services Project-level decision-makers Enterprise
Architect builder/modeler MVAs (including standards and compliance criteria) for projects/products Compliance guidance Compliance reports Better product decisions Successful products Requirements Elicitation and Understanding Services Product managers Enterprise Architect with requirements understanding specialty Stakeholder concerns Requirements Assessments (value, ability, etc.) Solid outside-in view of requirements and value for solutions balanced
among stakeholders Internal-Centric Architecture Planning Services Architecture team leaders Experienced
Enterprise Architect Architecture project plans Resourced architecture
team Enterprise Architecture Practice Development Support Services Architecture organization decision-makers Enterprise Architecture
practice experts Enterprise Architecture Capability assessments Enterprise Architecture Capability improvement recommendations Highly skilled and organized Enterprise Architecture practice
organization (internal or external)

</details>

<a id="sec-03_05_01"></a>
## 3.5.1. Enterprise Support Services

概念：企业支持服务以分析、报告和建议支持战略决策，可独立于个别项目。

适用条件：C级管理层组织变革决策。

逻辑关系：企业问题→企业分析→建议与风险信息；不必等待某项目立项。

决策方法：界定需要回答的企业问题与决策受众。

制品及证据：答案、评估报告、建议及预期企业结果；不能保证风险已降低。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00199, C220-web-2025:01-introduction-and-core-concepts:b00200

<details><summary>展开本节完整英文来源</summary>

3.5.1. Enterprise Support Services

This service category contains candidate services that enable informed
enterprise decisions in support of organization change. These services
could be provided independent of any individual project. These services
focus on answering questions and providing enterprise analysis in
support of strategic decisions.

</details>

<a id="sec-03_05_02"></a>
## 3.5.2. Design Support Services

概念：设计支持服务通常在项目获资金后提供MVA和分析以支持设计决策。

适用条件：大型/小型、瀑布/敏捷项目的设计选择。

逻辑关系：项目/项目群决策、MVA与合规标准关联；“通常”不是唯一允许时点。

决策方法：确定支持决策的最小充分架构、标准和路线图。

制品及证据：MVA、合规指导与报告、设计权衡；MVA不等于免治理。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00201, C220-web-2025:01-introduction-and-core-concepts:b00202

<details><summary>展开本节完整英文来源</summary>

3.5.2. Design Support Services

This service category contains candidate services that enable informed design decisions in support of organization change. These services would typically be provided after a project has been funded, whether large or small, waterfall or Agile. These services include the development of Minimum Viable Architectures (MVAs) and associated analysis to support the design decisions.

</details>

<a id="sec-03_05_03"></a>
## 3.5.3. Development Support Services

概念：开发支持服务在开发期回答问题并提供企业分析，支持产品/项目开发决策。

适用条件：各类方法的开发阶段。

逻辑关系：开发决策仍与企业架构和合规要求连接。

决策方法：识别开发实际问题并评估其跨企业影响。

制品及证据：项目/产品MVA、合规指导与报告；不能以编码完成判业务成功。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00203, C220-web-2025:01-introduction-and-core-concepts:b00204

<details><summary>展开本节完整英文来源</summary>

3.5.3. Development Support Services

This service category contains candidate services that enable informed development decisions in support of organization change. These services
would typically be provided during the development phase of a project, whether large or small, waterfall or Agile. These services focus on answering questions and providing enterprise analysis in support of development decisions.

</details>

<a id="sec-03_05_04"></a>
## 3.5.4. Requirements Elicitation and Understanding Services

概念：需求引出与理解服务超出管理已有需求，探究可带来业务价值的真实需要。

适用条件：产品经理和多个利益相关者需求冲突时。

逻辑关系：外向内需求与价值、可实现性评估需平衡利益相关者。

决策方法：验证真实需要与价值，不把需求字段完备等同需求已理解。

制品及证据：关切、需求、价值/能力评估；实际价值证据未知仍保留。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00205, C220-web-2025:01-introduction-and-core-concepts:b00206

<details><summary>展开本节完整英文来源</summary>

3.5.4. Requirements Elicitation and Understanding Services

This service category contains candidate services that enable
requirements understanding. Taking a step beyond requirements
management, these services help get closer to real need that will
deliver greater business value.

</details>

<a id="sec-03_05_05"></a>
## 3.5.5. Architecture Planning Services

概念：架构规划服务支持有计划地执行架构项目，通常项目开始时提供。

适用条件：为团队领导安排架构工作。

逻辑关系：项目计划服务面向架构工作和资源，不等于业务迁移计划。

决策方法：依据范围和工作量安排团队、依赖与时点。

制品及证据：架构项目计划；人员数量出现不能证明资源充分。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00207, C220-web-2025:01-introduction-and-core-concepts:b00208

<details><summary>展开本节完整英文来源</summary>

3.5.5. Architecture Planning Services

This service category contains candidate services that enable
well-planned and executed architecture projects in support of
organization change. These services would typically be provided at the beginning of a “project” whether large or small, waterfall or Agile.

</details>

<a id="sec-03_05_06"></a>
## 3.5.6. Enterprise Architecture Practice Development Support Services

概念：实践开发支持服务面向EA组织决策者，支持管理和改进架构实践。

适用条件：提高组织架构实践能力。

逻辑关系：能力评估→改进建议；关注熟练与组织化实践，而非某产品设计。

决策方法：评估现有实践及所需改进，不从培训完成推能力等级。

制品及证据：EA能力评估与改进建议；技能行为证据和运营表现须另取证。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00209, C220-web-2025:01-introduction-and-core-concepts:b00210

<details><summary>展开本节完整英文来源</summary>

3.5.6. Enterprise Architecture Practice Development Support Services

This service category contains candidate services that enable the
development and management of an Enterprise Architecture practice. These
services are focused on improving Enterprise Architecture Capability.

</details>

<a id="sec-03_06"></a>
## 3.6. Deliverables, Artifacts, and Building Blocks

概念：交付物按契约定义并正式评审签署；制品描述架构方面；构建块是可复用组件。

适用条件：制定交付合同、模型库或复用方案。

逻辑关系：交付物可含多个目录/矩阵/图；制品描述构建块，制品也可因契约成为交付物；ABB定义能力并塑造SBB选择。

决策方法：先定契约验收再选视图；区分逻辑能力需求、实现选择与表示它们的图。

制品及证据：交付约定、批准记录、制品到构建块追踪；名称/文件格式不能决定身份。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00211, C220-web-2025:01-introduction-and-core-concepts:b00212, C220-web-2025:01-introduction-and-core-concepts:b00213, C220-web-2025:01-introduction-and-core-concepts:b00214, C220-web-2025:01-introduction-and-core-concepts:b00215, C220-web-2025:01-introduction-and-core-concepts:b00216, C220-web-2025:01-introduction-and-core-concepts:b00217, C220-web-2025:01-introduction-and-core-concepts:b00218, C220-web-2025:01-introduction-and-core-concepts:b00219, C220-web-2025:01-introduction-and-core-concepts:b00220, C220-web-2025:01-introduction-and-core-concepts:b00221, C220-web-2025:01-introduction-and-core-concepts:b00222

<details><summary>展开本节完整英文来源</summary>

3.6. Deliverables, Artifacts, and Building Blocks

Architects executing the ADM will produce a number of outputs as a
result of their efforts, such as process flows, architectural
requirements, project plans, project compliance assessments, etc. The
TOGAF Architecture Content Framework (see the TOGAF Standard — Architecture Content ) provides a structural model for architectural content that
allows major work products to be consistently defined, structured, and
presented.

The Architecture Content Framework uses the following three categories
to describe the type of architectural work product within the context of
use:

A deliverable is a work product that is contractually specified and
in turn formally reviewed, approved, and signed off by the stakeholders Deliverables represent the output of projects and those deliverables
that are in documentation form will typically be archived at completion
of a project, or transitioned into an Architecture Repository as a
reference model, standard, or snapshot of the Architecture Landscape at
a point in time. An artifact is an architectural work product that describes an
aspect of the architecture Artifacts are generally classified as catalogs (lists of things),
matrices (showing relationships between things), and diagrams (pictures
of things). Examples include a requirements catalog, application
interaction matrix, and a value chain diagram. An architectural
deliverable may contain one or more artifacts and artifacts will form
the content of the Architecture Repository. An artifact may or may not
be considered a deliverable based on the contractual specification. A building block represents a potentially re-usable component that
can be combined with other building blocks to deliver architectures and
solutions Building blocks can be defined at various levels of detail, depending on
what stage of architecture development has been reached. For instance,
at an early stage, a building block can simply consist of a name or an
outline description. Later on, a building block may be decomposed into
multiple supporting building blocks and may be accompanied by a full
specification. Building blocks can relate to “architectures” or
“solutions”. Architecture Building Blocks (ABBs) typically describe required
capability and shape the specification of Solution Building Blocks
(SBBs); for example, a customer services capability may be required
within an enterprise, supported by many SBBs, such as processes, data,
and application software Solution Building Blocks (SBBs) represent actual implementation choices to realize a required capability; for example, a network is an ABB that can be realized by different implementation choices (SBBs), such as a satellite network in two major configurations: a hive of myriad microsatellites or a small set of large satellites

The relationships between deliverables, artifacts, and building blocks
are shown in Figure 3-2 .



Figure 3-2: Relationships between Deliverables, Artifacts, and Building Blocks

For example, an Architecture Definition Document is a deliverable that
documents an Architecture Description. This document will contain a
number of complementary artifacts that are views of the building blocks
relevant to the architecture. For example, a process flow diagram (an
artifact) may be created to describe the target call handling process (a
building block). This artifact may also describe other building blocks,
such as the actors involved in the process (e.g., a Customer Services
Representative). An example of the relationships between deliverables,
artifacts, and building blocks is illustrated in Figure 3-3 .



Figure 3-3: Example — Architecture Definition Document

The concepts of Deliverables, Artifacts, and Building Blocks are
described in more detail in the TOGAF Standard — Architecture Content .

The TOGAF Standard — ADM Techniques describes the Architecture Development Method and includes summary lists
of Deliverables and Artifacts that may be created in each phase. The TOGAF Standard — Architecture Content contains detailed descriptions of these.

</details>

<a id="sec-03_07"></a>
## 3.7. Architecture Abstraction

概念：上下文、概念、逻辑、物理抽象跨四域逐步回答为什么、什么、如何、用什么。

适用条件：控制复杂架构的沟通与决策细节。

逻辑关系：抽象层不是ADM阶段或战略/分段/能力粒度；why/what/how不对应Zachman用法。

决策方法：固定分析问题与细节一致性，避免把实现细节提前当需求。

制品及证据：分层模型及跨层追踪；源未规定每层一套固定图。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00223, C220-web-2025:01-introduction-and-core-concepts:b00224, C220-web-2025:01-introduction-and-core-concepts:b00225, C220-web-2025:01-introduction-and-core-concepts:b00226, C220-web-2025:01-introduction-and-core-concepts:b00227, C220-web-2025:01-introduction-and-core-concepts:b00228

<details><summary>展开本节完整英文来源</summary>

3.7. Architecture Abstraction

A process or technique for creating simplified views of a system-of-interest, for the purpose of discussion, communication, and decision-making about some aspect of the system, pertinent to its stakeholders.

Abstraction levels are layered in nature, moving from high-level models
to more detailed models.

Architecture effort can be divided into four distinct abstraction levels
that cross the Business, Data, Application, and Technology domains to
answer fundamental questions about an architecture:

Why — why is the architecture needed? What — what functionality and other requirements need to be met by the
architecture? How — how do we structure the functionality? With what — with what assets shall we implement this structure?

Note that why, what, and how have no connection to their use in the
Zachman ® Enterprise Architecture Framework.

</details>

<a id="sec-03_07_01"></a>
## 3.7.1. Contextual Abstraction Level

概念：上下文层描述企业环境、架构动机、目标驱动及工作范围。

适用条件：解释为何开展架构及边界。

逻辑关系：环境/目标驱动→范围与动机；不是组件选择层。

决策方法：明确目标、外部条件与组织边界。

制品及证据：情境、目标、驱动、范围模型；实际驱动应有业务来源。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00229, C220-web-2025:01-introduction-and-core-concepts:b00230

<details><summary>展开本节完整英文来源</summary>

3.7.1. Contextual Abstraction Level

This abstraction level is focused on understanding the environment in
which an enterprise operates and the context in which architecture work
is planned and executed. It answers why an enterprise undertakes
architecture work, what is the scope of work, and the motivation in
terms of goals, drivers, and objectives.

</details>

<a id="sec-03_07_02"></a>
## 3.7.2. Conceptual Abstraction Level

概念：概念层分解需求，描述必要行为/服务，避免过早关注实现。

适用条件：明确问题与所需服务。

逻辑关系：业务/应用/技术服务表达期望行为；可称服务或行为抽象。

决策方法：验证服务是否实现需要，暂不绑定供应商和物理产品。

制品及证据：需求到服务模型；服务名称不能替代可测试需求。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00231, C220-web-2025:01-introduction-and-core-concepts:b00232, C220-web-2025:01-introduction-and-core-concepts:b00233

<details><summary>展开本节完整英文来源</summary>

3.7.2. Conceptual Abstraction Level

This abstraction level is centered on decomposing the requirements to
understand the problem, and what is needed to address the problem,
without unduly focusing on how the architecture will be realized. It
answers what is necessary to realize the requirements and is usually
modeled using service models (business service, application service,
technology service) that represent desired behavior.

Note this abstraction level can also be referred to as either service
abstraction or behavior abstraction.

</details>

<a id="sec-03_07_03"></a>
## 3.7.3. Logical Abstraction Level

概念：逻辑层识别实现服务所需组件类型，保持实现独立。

适用条件：比较功能结构与组织方式。

逻辑关系：服务可按原则和分组准则组织成多个逻辑备选。

决策方法：比较逻辑分组备选并记录原则与取舍。

制品及证据：逻辑组件、关系、备选理由；逻辑组件不是已采购产品。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00234, C220-web-2025:01-introduction-and-core-concepts:b00235

<details><summary>展开本节完整英文来源</summary>

3.7.3. Logical Abstraction Level

This abstraction level is focused on identifying the kinds of business,
data, application, and technology components needed to achieve the
services identified in the conceptual level. It is about identifying how an architecture can be organized and structured, in an
implementation-independent fashion. There will potentially be several ways to group services into logical components, based on principles and
other grouping criteria, providing different logical solution alternatives.

</details>

<a id="sec-03_07_04"></a>
## 3.7.4. Physical Abstraction Level

概念：物理层将逻辑组件分配到具体实现资产。

适用条件：选择实际组件与部署实现。

逻辑关系：同一逻辑结构可由多个物理实现组合实现。

决策方法：按原则、约束和分组标准比较实现备选。

制品及证据：逻辑到物理分配、产品/部署选择证据；源不指定供应商优劣。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00236, C220-web-2025:01-introduction-and-core-concepts:b00237

<details><summary>展开本节完整英文来源</summary>

3.7.4. Physical Abstraction Level

This abstraction level manages the allocation and implementation of
physical components to meet the identified logical components. It is about determining with what physical components the logical-level components can be realized. There will potentially be many ways to use
physical components to realize logical components, based on principles and other grouping criteria, providing different physical solution
alternatives.

</details>

<a id="sec-03_08"></a>
## 3.8. Architecture Principles

概念：原则是持久、少变的通用指导；架构原则应体现企业原则及共识。

适用条件：制定和裁剪架构治理指导。

逻辑关系：企业→下级领域/分段原则形成继承边界，下级不能越过上级；架构实现目标须可回溯原则。

决策方法：检查原则与组织情境一致，冲突提交授权治理决策。

制品及证据：原则层次、理由及目标/驱动追踪；原则不是凭空设置的评级分。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00238, C220-web-2025:01-introduction-and-core-concepts:b00239, C220-web-2025:01-introduction-and-core-concepts:b00240, C220-web-2025:01-introduction-and-core-concepts:b00241, C220-web-2025:01-introduction-and-core-concepts:b00242, C220-web-2025:01-introduction-and-core-concepts:b00243, C220-web-2025:01-introduction-and-core-concepts:b00244, C220-web-2025:01-introduction-and-core-concepts:b00245

<details><summary>展开本节完整英文来源</summary>

3.8. Architecture Principles

Principles are general rules and guidelines, intended to be enduring and
seldom amended, that inform and support the way in which an organization
sets about fulfilling its mission.

Depending on the organization, principles may be established within
different domains and at different levels. Two key domains inform the
development and utilization of architecture:

Enterprise Principles provide a basis for decision-making throughout
an enterprise, and inform how the organization sets about fulfilling its
mission Enterprise Principles define the underlying general rules and
guidelines for the use and deployment of all resources and assets across the enterprise. They reflect a level of consensus among the various elements of the enterprise . Such principles are commonly found as a means of harmonizing
decision-making across an organization. In particular, they are a key
element in a successful Architecture Governance strategy (see TOGAF Standard — EA Capability and Governance ). Within the broad domain of Enterprise Principles, it is common to have
subsidiary principles within a business or organizational unit; for
example, principles specific to IT, HR, domestic operations, or overseas
operations. These principles provide a basis for decision-making within
the subsidiary domain and will inform architecture development within
the domain. Care must be taken to ensure that the principles used to
inform architecture development align to the organizational context of
the Architecture Capability. Architecture Principles are a set of principles that relate to
architecture work They reflect a level of consensus across the enterprise and embody the
spirit and thinking of existing Enterprise Principles. Architecture
Principles govern the architecture process, affecting the development,
maintenance, and use of the Enterprise Architecture.

Within an enterprise the hierarchy of principles starts with the
Enterprise Principles. The subsidiary segment principles must exist
within the bounds of these Enterprise Principles which are overarching.
Consequently, at each hierarchical level the set of principles will be
informed by and elaborate on the principles inherited from the level
above and cannot overstep their boundaries.

Architecture Principles may restate other enterprise guidance in terms and form that effectively guide architecture development.

The architecture should be clearly relatable to Principles for the manner in which it realizes objectives responding to drivers.

Architecture Principles are further explained in the TOGAF Standard — ADM Techniques .

</details>

<a id="sec-03_09"></a>
## 3.9. Interoperability

概念：互操作是共享信息与服务的能力，需明确共享程度及安全要求。

适用条件：跨单位、伙伴或系统的信息/服务交换。

逻辑关系：A揭示交换，B业务定义，C数据内容/应用共享，D机制，E选择，F逻辑实现规划；业务/信息/技术和EAI分类应一致。

决策方法：统一企业与扩展企业定义；分别验证共享语义、使用和技术连接。

制品及证据：交换需求、信息模型、接口及机制、合规证据；连接成功不等于信息可正确使用。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00246, C220-web-2025:01-introduction-and-core-concepts:b00247, C220-web-2025:01-introduction-and-core-concepts:b00248, C220-web-2025:01-introduction-and-core-concepts:b00249, C220-web-2025:01-introduction-and-core-concepts:b00250, C220-web-2025:01-introduction-and-core-concepts:b00251, C220-web-2025:01-introduction-and-core-concepts:b00252, C220-web-2025:01-introduction-and-core-concepts:b00253, C220-web-2025:01-introduction-and-core-concepts:b00254, C220-web-2025:01-introduction-and-core-concepts:b00255

<details><summary>展开本节完整英文来源</summary>

3.9. Interoperability

A definition of interoperability is “the ability to share information and services”. Defining the degree to which the information and services
are or are not to be shared is a very useful architectural requirement,
especially in a complex organization and/or extended enterprise.

The determination of interoperability is present throughout the
Architecture Development Method (ADM) as follows:

In the Architecture Vision (Phase A), the nature and security
considerations of the information and service exchanges are first
revealed within the business scenarios In the Business Architecture (Phase B), the information and service exchanges are further defined in business terms In the Data Architecture (Phase C), the content of the information exchanges is detailed using the corporate data and/or information
exchange model In the Application Architecture (Phase C), the way that the various
applications are to share the information and services is specified In the Technology Architecture (Phase D), the appropriate technical
mechanisms to permit the information and service exchanges are specified In Opportunities & Solutions (Phase E), the actual solutions (e.g.,
Commercial Off-The-Shelf (COTS) packages) are selected In Migration Planning (Phase F), the interoperability is logically
implemented

There are many ways to define interoperability and the aim is to define
one that is consistently applied within the enterprise and extended
enterprise. It is best that both the enterprise and the extended
enterprise use the same definitions.

Many organizations find it useful to categorize interoperability as
follows:

Operational or Business Interoperability defines how different parts
of the enterprise work together at the business level Information Interoperability defines how information is to be shared Technical Interoperability defines how technical resources are to be
shared or at least connect to one another

From an IT perspective, it is also useful to consider interoperability
in a similar vein to Enterprise Application Integration (EAI);
specifically:

Presentation Integration/Interoperability is where a common
look-and-feel approach through a common portal-like solution guides the
user to the underlying functionality of the set of systems Information Integration/Interoperability is where the corporate
information is seamlessly shared between the various corporate
applications to achieve, for example, a common set of client information Normally this is based upon a commonly accepted corporate ontology and
shared services for the structure, quality, access, and security/privacy
for the information. Application Integration/Interoperability is where the corporate
functionality is integrated and shareable so that the applications are
not duplicated (e.g., one change of address service/component; not one
for every application) and are seamlessly linked together through
functionality such as workflow This impacts the business and infrastructure applications and is very
closely linked to corporate business process unification/interoperability. Technical Integration/Interoperability includes common methods and shared services for the communication, storage, processing, and access to data primarily in the application platform and communications
infrastructure domains

Interoperability and Interoperability Requirements are addressed in detail in the TOGAF Standard — ADM Techniques .

</details>

<a id="sec-03_10"></a>
## 3.10. Enterprise Continuum

概念：企业连续统为资产从通用到组织特定或反向泛化的分类机制。

适用条件：选择与复用架构和解决方案资产。

逻辑关系：Architecture Continuum与Solutions Continuum互补；部署方案反过来成为架构情境。

决策方法：评估可采用、需适配、可泛化资产，记录约束和上下文。

制品及证据：资产分类、来源及适配理由；连续统不是实际工作流水线。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00256, C220-web-2025:01-introduction-and-core-concepts:b00257, C220-web-2025:01-introduction-and-core-concepts:b00258, C220-web-2025:01-introduction-and-core-concepts:b00259, C220-web-2025:01-introduction-and-core-concepts:b00260, C220-web-2025:01-introduction-and-core-concepts:b00261, C220-web-2025:01-introduction-and-core-concepts:b00262

<details><summary>展开本节完整英文来源</summary>

3.10. Enterprise Continuum

The TOGAF Standard includes the concept of the Enterprise Continuum, which sets the broader context for an architect and explains how generic
solutions can be leveraged and specialized in order to support the requirements of an individual organization.

The Enterprise Continuum is a categorization for assets held in the
Enterprise Repositories that provides methods for classifying assets,
including architecture and solution artifacts as they evolve from
generic Foundation Architectures to Organization-Specific Architectures.
The Enterprise Continuum comprises two complementary concepts: the Architecture Continuum and the Solutions Continuum.

The Enterprise Continuum is described in detail in the TOGAF Standard — Architecture Content .

An overview of the structure and context for the Enterprise Continuum is
shown in Figure 3-4 .



Figure 3-4: Enterprise Continuum

</details>

<a id="sec-03_10_1"></a>
## 3.10.1. Architecture Repository

概念：Repository存储ADM不同抽象层的输出，支持全局治理下多层协作。

适用条件：维护架构资产与授权需求。

逻辑关系：元模型、能力、景观、标准、参考、治理、需求、解决方案景观有不同身份；标准与参考、已部署与计划不能混同。

决策方法：按资产身份、时点、批准状态和适用范围存储；已授权需求与Board约定连接。

制品及证据：版本化仓库、授权需求及治理记录；存进仓库不是批准。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00263, C220-web-2025:01-introduction-and-core-concepts:b00264, C220-web-2025:01-introduction-and-core-concepts:b00265, C220-web-2025:01-introduction-and-core-concepts:b00266, C220-web-2025:01-introduction-and-core-concepts:b00267, C220-web-2025:01-introduction-and-core-concepts:b00268, C220-web-2025:01-introduction-and-core-concepts:b00269, C220-web-2025:01-introduction-and-core-concepts:b00270, C220-web-2025:01-introduction-and-core-concepts:b00271

<details><summary>展开本节完整英文来源</summary>

3.10.1. Architecture Repository

Supporting the Enterprise Continuum is the concept of an Architecture Repository which can be used to store different classes of architectural
output at different levels of abstraction, created by the ADM. In this way, the TOGAF Standard facilitates understanding and co-operation
between stakeholders and practitioners at different levels.

By means of the Enterprise Continuum and Architecture Repository,
architects are encouraged to leverage all other relevant architectural
resources and assets in developing an Organization-Specific
Architecture. In this context, the TOGAF ADM can be regarded as
describing a process lifecycle that operates at multiple levels within the organization, operating within a holistic governance framework and
producing aligned outputs that reside in an Architecture Repository. The
Enterprise Continuum provides a valuable context for understanding
architectural models: it shows building blocks and their relationships
to each other, and the constraints and requirements on a cycle of architecture development.

The structure of the TOGAF Architecture Repository is shown in Figure 3-5 .



Figure 3-5: TOGAF Architecture Repository Structure

The major components within an Architecture Repository are as follows:

The Architecture Metamodel describes the organizationally tailored
application of an architecture framework, including a metamodel for architecture content The Architecture Capability defines the parameters, structures, and
processes that support governance of the Architecture Repository The Architecture Landscape is the architectural representation of
assets deployed within the operating enterprise at a particular point in
time — the landscape is likely to exist at multiple levels of
abstraction to suit different architecture objectives The Standards Library captures the standards with which new
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

The TOGAF Architecture Repository is described in the TOGAF Standard — Architecture Content .

</details>

<a id="sec-03_12"></a>
## 3.11. TOGAF Content Framework and Enterprise Metamodel

概念：内容框架、企业元模型及选定制品共同定义组织的架构表达。

适用条件：预备阶段建立组织特定架构能力。

逻辑关系：内容分类回答输出如何组织；元模型回答实体类型、属性关系；具体制品回答如何表达。

决策方法：分别决策分类、语义结构和表示工具，再检查一致性。

制品及证据：内容框架、企业元模型、制品清单；源锚点sec-03_12仍对应显示3.11，引用不改号。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00272

<details><summary>展开本节完整英文来源</summary>

3.11. TOGAF Content Framework and Enterprise Metamodel

</details>

<a id="sec-03_12_01"></a>
## 3.11.1. Overview

概念：ADM输入输出为工作产品建立生命周期，预备阶段需定义分类框架、元模型和具体制品。

适用条件：架构能力搭建。

逻辑关系：选定架构框架与软件工具会影响内容框架，不能由工具自动决定业务语义。

决策方法：明确需要存储/分析的实体关系，再选择适当工具。

制品及证据：分类框架、实体关系模型和制品目录；不可只列文件名。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00273, C220-web-2025:01-introduction-and-core-concepts:b00274, C220-web-2025:01-introduction-and-core-concepts:b00275, C220-web-2025:01-introduction-and-core-concepts:b00276, C220-web-2025:01-introduction-and-core-concepts:b00277, C220-web-2025:01-introduction-and-core-concepts:b00278

<details><summary>展开本节完整英文来源</summary>

3.11.1. Overview

The TOGAF ADM provides lifecycle management to create and manage
architectures within an enterprise. At each phase within the ADM, a
discussion of inputs, outputs, and steps describes a number of
architectural work products.

An essential task when establishing the enterprise-specific Enterprise
Architecture Capability in the Preliminary Phase of the ADM is to
define:

A categorization framework to be used to structure the Architecture
Descriptions, the work products used to express an architecture, and the
collection of models that describe the architecture; this is referred to
as the Content Framework An understanding of the types of entities within the enterprise and
the relationships between them that need to be captured, stored, and
analyzed in order to create the Architecture Description; this Enterprise Metamodel depicts this information in the form of a formal
model The specific artifacts to be developed; see Section 3.6, “Deliverables, Artifacts, and Building Blocks”

The Content Framework chosen is likely to be influenced by:

The Architecture Framework selected as the basis for the Enterprise
Architecture Capability The chosen software tool used to support the Enterprise Architecture
Capability

</details>

<a id="sec-03_12_02"></a>
## 3.11.2. Content Framework

概念：内容框架结构化表达决策的构建块和制品，降低遗漏并提高一致性。

适用条件：组织项目输出和仓库。

逻辑关系：框架可替换和适配；按ADM阶段分类是内容组织，不是执行顺序。

决策方法：选择并定制一个一致框架，用作可能输出清单；不把全部候选制品变为强制。

制品及证据：内容分类及仓库结构映射、输出缺口记录。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00279, C220-web-2025:01-introduction-and-core-concepts:b00280, C220-web-2025:01-introduction-and-core-concepts:b00281, C220-web-2025:01-introduction-and-core-concepts:b00282, C220-web-2025:01-introduction-and-core-concepts:b00283, C220-web-2025:01-introduction-and-core-concepts:b00284, C220-web-2025:01-introduction-and-core-concepts:b00285, C220-web-2025:01-introduction-and-core-concepts:b00286, C220-web-2025:01-introduction-and-core-concepts:b00287, C220-web-2025:01-introduction-and-core-concepts:b00288, C220-web-2025:01-introduction-and-core-concepts:b00289

<details><summary>展开本节完整英文来源</summary>

3.11.2. Content Framework

The Content Framework defines a categorization framework to be used to
describe the building blocks and artifacts reflecting decisions taken in
creating the overall architecture deliverables.

The Architecture Repository, which is explained in Section 3.10.1, “Architecture Repository” ,
is structured to store the artifacts and work products identified in the Content Framework. The Content Framework is one element of the Enterprise-Specific Architecture Framework.

There are many alternative Content Frameworks (e.g., the TOGAF Content Framework, the Zachman Framework, DoDAF, NAF, etc.). Selecting a Content
Framework is essential even though the choice of Content Framework is less important. The final Content Framework is usually adapted to fit specific organization needs.

The TOGAF Content Framework is intended to:

Provide a detailed model of architectural work products Drive consistency in the outputs created when following the ADM Provide a comprehensive checklist of architecture output that could be created Reduce the risk of gaps within the final architecture deliverable set Help an enterprise mandate standard architecture concepts, terms, and deliverables

At the highest level, the TOGAF Content Framework (see Figure 3-6 ) is structured in line with the phases of
the ADM.



Figure 3-6: Content Framework by ADM Phase

Architecture Principles, Vision, Motivation, and Requirements models
are intended to capture the surrounding context of formal architecture
models, including general Architecture Principles, strategic context
that forms input for architecture modeling, and requirements generated
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

The TOGAF Content Framework is described in detail in the TOGAF Standard — Architecture Content .

</details>

<a id="sec-03_12_03"></a>
## 3.11.3. Enterprise Metamodel

概念：企业元模型定义企业模型出现的类型与关系，支持一致、完备和追踪。

适用条件：评估建模语言或架构工具覆盖。

逻辑关系：类型Role与实例Teller等不同；符号语言可选ArchiMate/BPMN/UML等，需能表达组织需要。

决策方法：验证实体/属性/关系是否可表达，不凭图形相似认语义等价。

制品及证据：组织元模型、类型/实例规则及表示映射；标准不强制单一记法。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00290, C220-web-2025:01-introduction-and-core-concepts:b00291, C220-web-2025:01-introduction-and-core-concepts:b00292, C220-web-2025:01-introduction-and-core-concepts:b00293, C220-web-2025:01-introduction-and-core-concepts:b00294, C220-web-2025:01-introduction-and-core-concepts:b00295, C220-web-2025:01-introduction-and-core-concepts:b00296, C220-web-2025:01-introduction-and-core-concepts:b00297

<details><summary>展开本节完整英文来源</summary>

3.11.3. Enterprise Metamodel

The TOGAF Standard encourages development of an Enterprise Metamodel,
which defines the types of entity to appear in the models that describe
the enterprise, together with the relationships between these entities.

For example, one type in an Enterprise Metamodel might be Role. Then the
enterprise’s Business Architecture models might include such instances
of Role as Teller, Pilot, Manager, Volunteer, Customer, or Firefighter.
Of course it would be an unusual enterprise that had all of these roles.

An Enterprise Metamodel provides value in several ways:

It gives architects a starter set of the types of thing to investigate
and to cover in their models It provides a form of completeness-check for any architecture modeling language, or architecture metamodel, that is proposed for use in an enterprise Namely, how completely does it handle the types of entity in the
Enterprise Metamodel, and manage required facts about them such as their attributes and relationships? It can help ensure: Consistency Completeness Traceability

Note that the TOGAF Standard does not aim to constrain an enterprise’s:

Selection of artifacts Modeling notation The TOGAF Standard may use a variety of modeling languages, such as the ArchiMate ® modeling language, Business Process Model and Notation™
(BPMN™), Unified Modeling Language™ (UML ® ), entity relationship diagramming, flowcharting, or any other notation that can
express some TOGAF ideas.

The types of entity within an enterprise and the relationships between them are specific to the individual enterprise. Developing a high-quality metamodel is an important aspect of establishing the
Enterprise Architecture Capability.

</details>

<a id="sec-03_12_04"></a>
## 3.11.4. Developing the Enterprise Metamodel

概念：Library的基础核心元模型是组织元模型的可用起点。

适用条件：从通用到行业/组织特定模型适配。

逻辑关系：连续统支持基础、通用、行业、组织特定适配；核心类型是多数企业可能需要的语义。

决策方法：保留适用类型和关系，按组织需要增改并记录来源。

制品及证据：企业特定元模型、适配规则和关系检查；图不含基数，不能杜撰。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00298, C220-web-2025:01-introduction-and-core-concepts:b00299, C220-web-2025:01-introduction-and-core-concepts:b00300, C220-web-2025:01-introduction-and-core-concepts:b00301, C220-web-2025:01-introduction-and-core-concepts:b00302, C220-web-2025:01-introduction-and-core-concepts:b00303, C220-web-2025:01-introduction-and-core-concepts:b00304, C220-web-2025:01-introduction-and-core-concepts:b00305

<details><summary>展开本节完整英文来源</summary>

3.11.4. Developing the Enterprise Metamodel

The Enterprise Metamodel is an important part of the
Organization-Specific Architecture Framework, as highlighted here. Figure 3-7 shows how the Enterprise Continuum (see Section 3.10, “Enterprise Continuum” )
provides a way to consider resources on a scale ranging from the most general (“Foundation”) to
most specific (“Organization-Specific”):



Figure 3-7: Applying the Enterprise Continuum

To support development of the enterprise’s metamodel, the TOGAF Library
includes a Foundation-level Core Enterprise Metamodel, detailed in the TOGAF Standard — Architecture Content . It shows types of entity, and relationships between them, that are likely to be required in modeling most enterprises and provides a context for the artifacts suggested in the ADM.

The Foundation Enterprise Metamodel is illustrated in Figure 3-8 .



Figure 3-8: The TOGAF Core Enterprise Metamodel

</details>

<a id="sec-03_13"></a>
## 3.12. Establishing and Maintaining an Enterprise Architecture Capability

概念：有效架构活动需要结构、角色、责任、技能和过程构成的业务能力。

适用条件：建立或评估架构实践。

逻辑关系：治理、资源池、角色责任、项目/组合治理、仓库与业务运营相互支持。

决策方法：按实际架构任务匹配授权和能力证据，识别资源缺口。

制品及证据：能力模型、任务责任和技能证据；成熟度标签不能证明实际人员能力。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00306, C220-web-2025:01-introduction-and-core-concepts:b00307, C220-web-2025:01-introduction-and-core-concepts:b00308, C220-web-2025:01-introduction-and-core-concepts:b00309

<details><summary>展开本节完整英文来源</summary>

3.12. Establishing and Maintaining an Enterprise Architecture Capability

In order to carry out architectural activity effectively within an
enterprise, it is necessary to put in place an appropriate business
capability for architecture, through organization structures, roles,
responsibilities, skills, and processes. An overview of the TOGAF
Architecture Capability is shown in Figure 3-9 .



Figure 3-9: TOGAF Architecture Capability Overview

</details>

<a id="sec-03_14"></a>
## 3.13. Establishing the Architecture Capability as an Operational Entity

概念：持续EA实践应作为运营单元经营，除ADM还需财务、绩效、服务、风险、资源等管理能力。

适用条件：长期运行EA能力，纯项目支持能力须按例外判断。

逻辑关系：持续治理把有架构影响活动统一控制并连接战略；治理益处需监测评价而非自动承诺。

决策方法：明确服务运营、预算、绩效、供应商、配置及环境管理机制。

制品及证据：运营模型、服务指标、配置基线和授权控制；原文“treated like a business”不表示另成立法律实体。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00310, C220-web-2025:01-introduction-and-core-concepts:b00311, C220-web-2025:01-introduction-and-core-concepts:b00312, C220-web-2025:01-introduction-and-core-concepts:b00313, C220-web-2025:01-introduction-and-core-concepts:b00314, C220-web-2025:01-introduction-and-core-concepts:b00315, C220-web-2025:01-introduction-and-core-concepts:b00316, C220-web-2025:01-introduction-and-core-concepts:b00317

<details><summary>展开本节完整英文来源</summary>

3.13. Establishing the Architecture Capability as an Operational Entity

Barring Architecture Capabilities set up to purely support change
delivery programs, it is increasingly recognized that a successful
Enterprise Architecture practice must sit on a firm operational footing.
In effect, an Enterprise Architecture practice must be run like any
other operational unit within a business; i.e., it should be treated
like a business. To this end, and over and above the core processes
defined within the ADM, an Enterprise Architecture practice should
establish capabilities in the following areas:

Financial Management Performance Management Service Management Risk and Opportunity Management; see Section B.34, “Risk Management” Resource Management Communications and Stakeholder Management; see Section 4.36, “Communications and Stakeholder Management” Quality Management Supplier Management; see Section B.40, “Supplier Management” Configuration Management; see Section B.7, “Configuration Management” Environment Management

Central to the notion of operating an ongoing architecture is the
execution of well-defined and effective governance, whereby all
architecturally significant activity is controlled and aligned within a
single framework.

As governance has become an increasingly visible requirement for
organizational management, the inclusion of governance within the TOGAF
Standard aligns the framework with current business best practice and
also ensures a level of visibility, guidance, and control that will
support all architecture stakeholder requirements and obligations.

The benefits of Architecture Governance include:

Increased transparency of accountability, and informed delegation of
authority Proactive risk and opportunity management Protection of the existing asset base through maximizing re-use of
existing architectural components Proactive control, monitoring, and management mechanisms Process, concept, and component re-use across all organizational
business units Value creation through monitoring, measuring, evaluation, and feedback Increased visibility supporting internal processes and external
parties’ requirements; in particular, increased visibility of
decision-making at lower levels ensures oversight at an appropriate
level within the enterprise of decisions that may have far-reaching
strategic consequences for the organization Greater shareholder value; in particular, Enterprise Architecture
increasingly represents the core intellectual property of the enterprise
— studies have demonstrated a correlation between increased shareholder
value and well-governed enterprises Integrates with existing processes and methodologies and complements
functionality by adding control capabilities

Further detail on establishing an Enterprise Architecture Capability is
given in the TOGAF Standard — EA Capability and Governance .

</details>

<a id="sec-03_15"></a>
## 3.14. Using the TOGAF Standard with Other Frameworks

概念：TOGAF可单独使用或用其他框架替换/扩展交付物，并融入企业流程与结构。

适用条件：已有架构/管理框架或专业领域方法时。

逻辑关系：方法与交付物是不同框架维度；ITIL/COBIT/项目方法整合不等于互相代替。

决策方法：映射职责、输入输出、术语和治理，再确定裁剪。

制品及证据：组织特定方法、框架映射、职责与制品协议；不宣称跨标准全部等价。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00318, C220-web-2025:01-introduction-and-core-concepts:b00319, C220-web-2025:01-introduction-and-core-concepts:b00320, C220-web-2025:01-introduction-and-core-concepts:b00321, C220-web-2025:01-introduction-and-core-concepts:b00322, C220-web-2025:01-introduction-and-core-concepts:b00323, C220-web-2025:01-introduction-and-core-concepts:b00324, C220-web-2025:01-introduction-and-core-concepts:b00325

<details><summary>展开本节完整英文来源</summary>

3.14. Using the TOGAF Standard with Other Frameworks

Two of the key elements of any Enterprise Architecture framework are:

A definition of the deliverables that the architecting activity should
produce A description of the method by which this should be done

With some exceptions, the majority of Enterprise Architecture frameworks
focus on the first of these — the specific set of deliverables — and are
relatively silent about the methods to be used to generate them
(intentionally so, in some cases).

Because the TOGAF Standard is a generic framework and intended to be
used in a wide variety of environments, it provides a flexible and
extensible content framework that underpins a set of generic
architecture deliverables.

As a result, the TOGAF framework may be used either in its own right,
with the generic deliverables that it describes; or else these
deliverables may be replaced or extended by a more specific set, defined
in any other framework that the architect considers relevant.

In all cases, it is expected that the architect will adapt and build on
the TOGAF framework in order to define a tailored method that is
integrated into the processes and organization structures of the
enterprise. This architecture tailoring may include adopting elements
from other architecture frameworks, or integrating TOGAF methods with
other standard frameworks or best practices, such as ITIL ® , CMMI ® ,
COBIT ® , PRINCE2, PMBOK, and MSP ® . It may also include adopting reference
materials from the TOGAF Library, such as the IT4IT™ Reference
Architecture. Guidelines for adapting the TOGAF ADM in such a way are
given in the TOGAF Standard — ADM Techniques .

As a generic framework and method for Enterprise Architecture, the TOGAF
Standard provides the capability and the collaborative environment to
integrate with other frameworks. Organizations are able to fully utilize
vertical business domains, horizontal technology areas (such as security
or manageability), or application areas (such as e-Commerce) to produce
a competitive Enterprise Architecture framework which maximizes their
business opportunities.

</details>

<a id="sec-03_16"></a>
## 3.15. Using the TOGAF Framework with Different Architecture Styles

概念：架构风格按情境、关注、形式、技术等特征区别，框架可适配多风格。

适用条件：安全、SOA、微服务等特定风格。

逻辑关系：先识别特征再调整模型/视点/工具；主导风格或重大能力变更可触发预备阶段回访。

决策方法：判断需新增实体、记法与关切，避免把风格变强制ADM顺序。

制品及证据：风格特征、元模型扩展、视点和工具选择；示例出版物不是全部已取得。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00326, C220-web-2025:01-introduction-and-core-concepts:b00327, C220-web-2025:01-introduction-and-core-concepts:b00328, C220-web-2025:01-introduction-and-core-concepts:b00329, C220-web-2025:01-introduction-and-core-concepts:b00330, C220-web-2025:01-introduction-and-core-concepts:b00331, C220-web-2025:01-introduction-and-core-concepts:b00332, C220-web-2025:01-introduction-and-core-concepts:b00333, C220-web-2025:01-introduction-and-core-concepts:b00334, C220-web-2025:01-introduction-and-core-concepts:b00335, C220-web-2025:01-introduction-and-core-concepts:b00336, C220-web-2025:01-introduction-and-core-concepts:b00337, C220-web-2025:01-introduction-and-core-concepts:b00338, C220-web-2025:01-introduction-and-core-concepts:b00339, C220-web-2025:01-introduction-and-core-concepts:b00340

<details><summary>展开本节完整英文来源</summary>

3.15. Using the TOGAF Framework with Different Architecture Styles

The TOGAF framework is designed to be flexible and is used with various
architectural styles.

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
Depending upon the distinctive features, different architectural styles will add new elements that must be described, highlight existing elements, adjust the notation used to describe the architecture, and
focus the architect on some stakeholders or stakeholder concerns.

Addressing the distinctive features will usually include extensions to
the Architecture Content Metamodel and the use of specific notation or
modeling techniques and the identification of viewpoints. Dominance of a particular architectural style can direct the practitioner to revisit the Preliminary Phase to make changes to the Architecture Capability or to address a distinctive feature in the expected scope of a single ADM
cycle.

Style-specific reference models and maturity models are commonly used
tools that support a practitioner.

During the lifetime of the TOGAF framework many architectural styles
have been developed to address key problems facing practitioners and to
demonstrate how the TOGAF framework can be made more relevant within
defined contexts.

Some of these have been developed by The Open Group Forums and Work Groups working in specific areas and have been published in Guides, White Papers, and Standards. Examples include:

TOGAF ® Series Guide: Using the TOGAF ® Framework to Define and Govern Service-Oriented Architectures TOGAF ® Series Guide: Integrating Risk and Security within a TOGAF ® Enterprise Architecture

Some of these have been developed collaboratively between The Open Group and other bodies. Examples include:

TOGAF ® and SABSA ® Integration Archi Banking Group: Combining the BIAN Reference Model, ArchiMate ® Modeling Notation, and the TOGAF ® Framework Exploring Synergies between TOGAF ® and Frameworx TOGAF ® 9 and DoDAF 2.0

The TOGAF Library (see www.opengroup.org/togaf-library )
is a structured library of resources that support the TOGAF Standard.

</details>

<a id="sec-03_17"></a>
## 3.16. Architecture Views and Viewpoints

概念：视图让特定利益相关者以可理解形式看到系统的相关关切；视点是构造解释的规则。

适用条件：沟通复杂架构和核对多视图一致性。

逻辑关系：系统/架构/描述、利益相关者/关切、视点/视图/模型/模型种类身份分离。

决策方法：先定关切与视点，再产生模型和视图；共享对象改变须评估语义影响。

制品及证据：关切到视图追踪、模型及构造规则；同ID一致不能证明业务理解正确。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00341, C220-web-2025:01-introduction-and-core-concepts:b00342, C220-web-2025:01-introduction-and-core-concepts:b00343, C220-web-2025:01-introduction-and-core-concepts:b00344, C220-web-2025:01-introduction-and-core-concepts:b00345

<details><summary>展开本节完整英文来源</summary>

3.16. Architecture Views and Viewpoints

The ability to create specific “views” of parts of a complex architecture is fundamental in being able to communicate with and allay concerns of stakeholders or groups of stakeholders. To gain full understanding and support from stakeholders it is necessary to present
information in a form that each stakeholder will relate to and understand.

The role of architecture views is shown in Figure 3-10 , adapted from more formal definitions contained in ISO/IEC/IEEE 42010:2022 and ISO/IEC/IEEE 15288:2015.



Figure 3-10: Basic Architectural Concepts

</details>

<a id="sec-03_18"></a>
## 3.17. Enterprise Agility

概念：企业敏捷比敏捷软件开发宽，连接战略、业务价值、连续变化和风险。

适用条件：客户/产品导向组织快速反应。

逻辑关系：分区分解架构倡议，层级区分粒度；与迭代共同支持及时决策。

决策方法：按变化需要选择粒度、分区和迭代，保留跨域依赖与合规。

制品及证据：架构分区/层级与迭代计划；未提供统一企业敏捷分数。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00346, C220-web-2025:01-introduction-and-core-concepts:b00347, C220-web-2025:01-introduction-and-core-concepts:b00348, C220-web-2025:01-introduction-and-core-concepts:b00349, C220-web-2025:01-introduction-and-core-concepts:b00350, C220-web-2025:01-introduction-and-core-concepts:b00351, C220-web-2025:01-introduction-and-core-concepts:b00352, C220-web-2025:01-introduction-and-core-concepts:b00353, C220-web-2025:01-introduction-and-core-concepts:b00354

<details><summary>展开本节完整英文来源</summary>

3.17. Enterprise Agility

Enterprise agility is a commonly used term, but the exact definition
differs among practitioners. Regardless of how the term is defined, it
is important because it enables an enterprise to better react to change by being more customer and product-centric, more efficient, and better
able to ensure regulatory compliance.

The term “Agile” is frequently associated with Agile software
development processes associated with the Manifesto for Agile Software
Development.

While these “Agile” principles and techniques can be applied to adapt
the TOGAF framework, enterprise agility is a broader context than Agile software development. Therefore, additional techniques are employed in
adapting the TOGAF framework to an Agile enterprise.

Enterprise Architecture provides a framework for change, linked to both strategic direction and business value. It provides a sufficient view of
the organization to manage complexity, support continuous change, and manage the risk of unanticipated consequences.

The TOGAF framework has embraced the call to respond to the needs of the enterprise in a timely manner, through the concepts of “partitions” and “levels”. Partitions define how the work is broken down into multiple architecture initiatives. Levels define how the overall architecture can be developed at different levels of granularity and detail.

In addition, the TOGAF ADM supports a number of concepts that are
characterized as iteration.

More detailed descriptions of how to adapt the TOGAF ADM to support
enterprise agility can be found in:

TOGAF ® Series Guide: Applying the TOGAF ® ADM using Agile Sprints TOGAF ® Series Guide: Enabling Enterprise Agility The Open Agile Architecture™ Standard

</details>

<a id="sec-03_19"></a>
## 3.18. Risk Management

概念：风险需开始前识别分类并在转型全程持续监控；初始与剩余风险按缓解前后区分。

适用条件：任何架构或业务转型。

逻辑关系：架构师可识别/缓解部分风险，风险必须由治理框架接受管理；外部触发不受规划者完全控制。

决策方法：分类→识别→初评→缓解/剩余评估→监控；记录谁有接受权和何证据证明措施有效。

制品及证据：风险登记、评估、缓解和监控/接受记录；定性/定量方法不同，不填假概率。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00355, C220-web-2025:01-introduction-and-core-concepts:b00356, C220-web-2025:01-introduction-and-core-concepts:b00357, C220-web-2025:01-introduction-and-core-concepts:b00358, C220-web-2025:01-introduction-and-core-concepts:b00359, C220-web-2025:01-introduction-and-core-concepts:b00360, C220-web-2025:01-introduction-and-core-concepts:b00361, C220-web-2025:01-introduction-and-core-concepts:b00362, C220-web-2025:01-introduction-and-core-concepts:b00363, C220-web-2025:01-introduction-and-core-concepts:b00364, C220-web-2025:01-introduction-and-core-concepts:b00365, C220-web-2025:01-introduction-and-core-concepts:b00366

<details><summary>展开本节完整英文来源</summary>

3.18. Risk Management

There will always be risk with any architecture/business transformation effort. It is important to identify, classify, and mitigate these risks before starting so that they can be tracked throughout the transformation effort.

Mitigation is an ongoing effort and often the risk triggers may be
outside the scope of the transformation planners (e.g., merger,
acquisition) so planners must monitor the transformation context
constantly.

It is also important to note that the Enterprise Architect may identify
the risks and mitigate certain ones, but it is within the governance
framework that risks have to be first accepted and then managed.

There are two levels of risk that should be considered, namely:

Initial level of risk: risk categorization prior to determining and
implementing mitigating actions Residual level of risk: risk categorization after implementation of
mitigating actions (if any)

The process for risk management consists of the following activities:

Risk classification Risk identification Initial risk assessment Risk mitigation and residual risk assessment Risk monitoring

A qualitative approach to risk management is described in the TOGAF Standard — ADM Techniques .

Risk concepts are included in the Enterprise Security Architecture
described in the

TOGAF ® Series Guide: Integrating Risk and Security within a TOGAF ® Enterprise Architecture

A more rigorous quantitative approach is described in the Open
FAIR™ Body of Knowledge which comprises two standards from The Open
Group: Open Risk Taxonomy (O-RT) and Open Risk Analysis (O-RA).

</details>

<a id="chap04"></a>
## 4. Definitions

概念：第四章提供标准通用定义；补充术语查附录B，仍未定义的词按源指定词典理解。

适用条件：跨卷术语和模型语义核对。

逻辑关系：定义层次有优先关系；同词可能按上下文有多个义项。

决策方法：先统一词义再做关系/制品映射，保留源内异义。

制品及证据：术语表与歧义记录；定义不是现成执行算法。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00367, C220-web-2025:01-introduction-and-core-concepts:b00368

<details><summary>展开本节完整英文来源</summary>

4. Definitions

For the purposes of the TOGAF Standard, the following terms and
definitions apply. Appendix B, Glossary of Supplementary Definitions should be referenced for supplementary definitions not
defined in this chapter. The Merriam-Webster ® Collegiate Dictionary
should be referenced for terms not defined in this section or Appendix B, Glossary of Supplementary Definitions .

</details>

<a id="sec-04_01"></a>
## 4.1. Abstraction

概念：抽象是对复杂细节作概括，亦可表示保持共同分析细节层次。

适用条件：术语用于抽象的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：统一层次使跨域沟通与决策可比较。

决策方法：派生检查：先说明分析问题及保留/省略的细节。

制品及证据：本节未要求新增独立交付物；派生检查可使用：抽象层声明、模型范围与细化链。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00369, C220-web-2025:01-introduction-and-core-concepts:b00370, C220-web-2025:01-introduction-and-core-concepts:b00371

<details><summary>展开本节完整英文来源</summary>

4.1. Abstraction

The technique of providing summarized or generalized descriptions of
detailed and complex content.

Note: Abstraction, as in “level of abstraction”, can also mean providing a
focus for analysis that is concerned with a consistent and common
level of detail or abstraction. Abstraction in this sense is typically
used in architecture to allow a consistent level of definition and
understanding to be achieved in each area of the architecture in order
to support effective communication and decision-making. It is
especially useful when dealing with large and complex architectures as
it allows relevant issues to be identified before further detail is
attempted.

</details>

<a id="sec-04_02"></a>
## 4.2. Actor

概念：Actor是发起或参与活动、拥有一个或多个角色的人、组织或系统，可内外部。

适用条件：术语用于Actor的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：Actor与Role身份不同，一Actor可多Role。

决策方法：派生检查：把实际参与者和其扮演角色分开登记。

制品及证据：本节未要求新增独立交付物；派生检查可使用：参与者、角色及活动关系。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00372, C220-web-2025:01-introduction-and-core-concepts:b00373, C220-web-2025:01-introduction-and-core-concepts:b00374

<details><summary>展开本节完整英文来源</summary>

4.2. Actor

A person, organization, or system that has one or more roles that
initiates or interacts with activities; for example, a sales
representative who travels to visit customers. Actors may be internal or
external to an organization.

Note: In the automotive industry, an original equipment manufacturer would
be considered an actor by an automotive dealership that interacts with
its supply chain activities.

</details>

<a id="sec-04_03"></a>
## 4.3. Application Architecture

概念：应用架构描述提供业务能力和管理数据资产的应用结构与交互。

适用条件：术语用于应用架构描述提供业务能力和管理数据资产的应用结构与交互。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：应用需连接业务能力和数据资产。

决策方法：派生检查：检验应用交互是否支持相应能力及数据责任。

制品及证据：本节未要求新增独立交付物；派生检查可使用：应用结构、交互、能力与数据映射。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00375, C220-web-2025:01-introduction-and-core-concepts:b00376, C220-web-2025:01-introduction-and-core-concepts:b00377

<details><summary>展开本节完整英文来源</summary>

4.3. Application Architecture

A description of the structure and interaction of the applications that
provide key business capabilities and manage the data assets.

Note: Application Architecture is described in the TOGAF Standard — Architecture Development Method .

</details>

<a id="sec-04_04"></a>
## 4.4. Application Component

概念：应用组件是与实现结构对齐、可替换的模块封装，封装行为/数据并经接口提供服务。

适用条件：术语用于应用组件的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：组件通常维护数据组件，受技术组件的技术服务支持。

决策方法：派生检查：区分组件、接口、服务和数据，不以部署名称替代行为。

制品及证据：本节未要求新增独立交付物；派生检查可使用：组件/服务/接口和数据技术依赖。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00378, C220-web-2025:01-introduction-and-core-concepts:b00379, C220-web-2025:01-introduction-and-core-concepts:b00380

<details><summary>展开本节完整英文来源</summary>

4.4. Application Component

An encapsulation of application functionality aligned to implementation
structure, which is modular and replaceable. It encapsulates its
behavior and data, provides services, and makes them available through
interfaces.

Note: For example, a business application such as an accounting, payroll, or
CRM system. An application component usually maintains a data component. It is
enabled by technology services provided by technology components.

</details>

<a id="sec-04_05"></a>
## 4.5. Application Platform

概念：应用平台是支持应用所用服务的软硬件技术组件集合。

适用条件：术语用于应用平台的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：平台是组件集合，不是某一个应用服务。

决策方法：派生检查：列清支持应用的组件和所供服务。

制品及证据：本节未要求新增独立交付物；派生检查可使用：平台组件与服务依赖。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00381, C220-web-2025:01-introduction-and-core-concepts:b00382

<details><summary>展开本节完整英文来源</summary>

4.5. Application Platform

The collection of technology components of hardware and software that
provide the services used to support applications.

</details>

<a id="sec-04_06"></a>
## 4.6. Application Service

概念：应用服务是可向应用请求的离散行为，自动支持或交付业务服务的一部或全部。

适用条件：术语用于应用服务的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：应用服务与业务服务可部分实现，非必然一对一。

决策方法：派生检查：验证请求行为和业务服务实现范围。

制品及证据：本节未要求新增独立交付物；派生检查可使用：应用服务接口、行为与业务服务映射。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00383, C220-web-2025:01-introduction-and-core-concepts:b00384

<details><summary>展开本节完整英文来源</summary>

4.6. Application Service

A discrete behavior requestable from an application; an automated
element supporting or delivering part or all of one or more business
services.

</details>

<a id="sec-04_07"></a>
## 4.7. Architectural Style

概念：架构风格是特定情境的独特原则与特征集合，引导或限制形成方式。

适用条件：术语用于架构风格的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：风格影响表达与方法，非阶段或产品类型。

决策方法：派生检查：说清所采用风格特征及适用边界。

制品及证据：本节未要求新增独立交付物；派生检查可使用：风格原则、模型/视点适配理由。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00385, C220-web-2025:01-introduction-and-core-concepts:b00386

<details><summary>展开本节完整英文来源</summary>

4.7. Architectural Style

The combination of distinctive features related to the specific context
within which architecture is performed or expressed; a collection of
principles and characteristics that steer or constrain how an
architecture is formed.

</details>

<a id="sec-04_08"></a>
## 4.8. Architecture

概念：架构可指实体环境中的基本概念属性与生命周期原则，也可指组件结构关系及演进准则。

适用条件：术语用于架构可指实体环境中的基本概念属性与生命周期原则，也可指组件结构关系及演进准则。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：同词两义需依上下文，不能等同图或文件。

决策方法：派生检查：明确所谈架构的实体、结构与描述分别是什么。

制品及证据：本节未要求新增独立交付物；派生检查可使用：实体边界、结构关系和原则。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00387, C220-web-2025:01-introduction-and-core-concepts:b00388

<details><summary>展开本节完整英文来源</summary>

4.8. Architecture

The fundamental concepts or properties of an entity in its environment
and governing principles for the realization and evolution of this entity and its related lifecycle processes
(Source: ISO/IEC/IEEE 42010:2022) The structure of components, their inter-relationships, and the
principles and guidelines governing their design and evolution over
time

</details>

<a id="sec-04_09"></a>
## 4.9. Architecture Building Block (ABB)

概念：ABB在逻辑或供应商独立层规定所需SBB。

适用条件：术语用于ABB在逻辑或供应商独立层规定所需SBB。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：ABB与实现它的SBB层次不同。

决策方法：派生检查：先明确能力需求，再比较实现选择。

制品及证据：本节未要求新增独立交付物；派生检查可使用：ABB规格、SBB候选和实现追踪。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00389, C220-web-2025:01-introduction-and-core-concepts:b00390, C220-web-2025:01-introduction-and-core-concepts:b00391

<details><summary>展开本节完整英文来源</summary>

4.9. Architecture Building Block (ABB)

An architectural component that specifies the required Solution Building
Blocks (SBBs) at a more logical (or supplier-independent) level.

See also Section 4.26, “Building Block” .

</details>

<a id="sec-04_10"></a>
## 4.10. Architecture Continuum

概念：架构连续统把景观/参考库中的组件和制品按详细度、专门化分类。

适用条件：术语用于架构连续统把景观/参考库中的组件和制品按详细度、专门化分类。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：基础→行业→组织特定是分类/适配，非项目时间序列。

决策方法：派生检查：标资产通用度和适配依据。

制品及证据：本节未要求新增独立交付物；派生检查可使用：架构资产分类及来源。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00392, C220-web-2025:01-introduction-and-core-concepts:b00393, C220-web-2025:01-introduction-and-core-concepts:b00394, C220-web-2025:01-introduction-and-core-concepts:b00395

<details><summary>展开本节完整英文来源</summary>

4.10. Architecture Continuum

A categorization mechanism, with increasing detail and specialization,
for the components and artifacts stored in the Architecture Landscape or
Reference Library (part of the Architecture Repository).

Note: This Continuum begins with foundational definitions like reference
models, core strategies, and basic building blocks. From there it
spans to Industry Architectures and all the way to an
Organization-Specific Architecture.

See also Section 4.45, “Enterprise Continuum” .

</details>

<a id="sec-04_11"></a>
## 4.11. Architecture Development Method (ADM)

概念：ADM是用EA塑造和治理业务转型的多阶段迭代方法。

适用条件：术语用于ADM的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：核心方法与技法不同，源注错指ADM Techniques卷。

决策方法：派生检查：用实际方法卷核对阶段定义，并保留错引记录。

制品及证据：本节未要求新增独立交付物；派生检查可使用：裁剪/迭代方法及源问题。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00396, C220-web-2025:01-introduction-and-core-concepts:b00397, C220-web-2025:01-introduction-and-core-concepts:b00398

<details><summary>展开本节完整英文来源</summary>

4.11. Architecture Development Method (ADM)

The core of the TOGAF framework. A multi-phase, iterative approach to
develop and use an Enterprise Architecture to shape and govern business
transformation.

Note: The ADM is described in the TOGAF Standard — ADM Techniques .

</details>

<a id="sec-04_12"></a>
## 4.12. Architecture Domain

概念：架构域是分析区域，四主域可被安全、动机、治理等跨越。

适用条件：术语用于架构域的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：横切域与四主域不是互斥分类。

决策方法：派生检查：交叉域责任和依赖是否覆盖。

制品及证据：本节未要求新增独立交付物；派生检查可使用：域范围及横切关切映射。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00399, C220-web-2025:01-introduction-and-core-concepts:b00400

<details><summary>展开本节完整英文来源</summary>

4.12. Architecture Domain

The architectural area being considered. The TOGAF framework follows the
tradition of dividing Enterprise Architecture into four primary
architecture domains: business, data, application, and technology. Other
domains (motivation, security, governance, etc.) may span those four
primary domains.

</details>

<a id="sec-04_13"></a>
## 4.13. Architecture Framework

概念：架构框架是计划、开发、实现、治理和维持架构的概念结构。

适用条件：术语用于架构框架的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：框架不是某具体架构，也不限制品模板。

决策方法：派生检查：检查方法、内容及治理覆盖。

制品及证据：本节未要求新增独立交付物；派生检查可使用：组织特定框架及适用约定。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00401, C220-web-2025:01-introduction-and-core-concepts:b00402

<details><summary>展开本节完整英文来源</summary>

4.13. Architecture Framework

A conceptual structure used to plan, develop, implement, govern, and
sustain an architecture.

</details>

<a id="sec-04_14"></a>
## 4.14. Architecture Governance

概念：架构治理监控并引导架构相关工作以达结果并遵循原则、标准和路线图。

适用条件：术语用于架构治理监控并引导架构相关工作以达结果并遵循原则、标准和路线图。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：治理不仅Phase G，且须有授权和结果依据。

决策方法：派生检查：区分建议、监督、批准与实际决策权。

制品及证据：本节未要求新增独立交付物；派生检查可使用：职责权限、合规和结果记录。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00403, C220-web-2025:01-introduction-and-core-concepts:b00404, C220-web-2025:01-introduction-and-core-concepts:b00405

<details><summary>展开本节完整英文来源</summary>

4.14. Architecture Governance

The practice of monitoring and directing architecture-related work. The
goal is to deliver desired outcomes and adhere to relevant principles,
standards, and roadmaps.

See also Section 4.49, “Governance” .

</details>

<a id="sec-04_15"></a>
## 4.15. Architecture Landscape

概念：架构景观按特定时点表述企业使用中或计划的资产。

适用条件：术语用于架构景观按特定时点表述企业使用中或计划的资产。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：使用中与计划状态须显式分开。

决策方法：派生检查：不把目标资产当现状，不把历史快照当当前。

制品及证据：本节未要求新增独立交付物；派生检查可使用：时点/状态明确的资产模型。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00406, C220-web-2025:01-introduction-and-core-concepts:b00407

<details><summary>展开本节完整英文来源</summary>

4.15. Architecture Landscape

The architectural representation of assets in use, or planned, by the enterprise at particular points in time.

</details>

<a id="sec-04_16"></a>
## 4.16. Architecture Level

概念：架构层级按粒度划分景观。

适用条件：术语用于架构层级按粒度划分景观。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：层级不同于分区，也不同于抽象层。

决策方法：派生检查：说明粒度和分析对象。

制品及证据：本节未要求新增独立交付物；派生检查可使用：粒度层次、范围及细化关系。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00408, C220-web-2025:01-introduction-and-core-concepts:b00409, C220-web-2025:01-introduction-and-core-concepts:b00410

<details><summary>展开本节完整英文来源</summary>

4.16. Architecture Level

Levels provide a framework for dividing the Architecture Landscape into
levels of granularity.

Note: Architecture levels are distinct from architecture partitions.

</details>

<a id="sec-04_17"></a>
## 4.17. Architecture Model

概念：架构模型是兴趣主题的缩小、简化或抽象表示。

适用条件：术语用于架构模型的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：模型与主题本身不同，可支持视图表达。

决策方法：派生检查：记录模型所表示对象及省略范围。

制品及证据：本节未要求新增独立交付物；派生检查可使用：模型范围、实体与源事实追踪。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00411, C220-web-2025:01-introduction-and-core-concepts:b00412, C220-web-2025:01-introduction-and-core-concepts:b00413, C220-web-2025:01-introduction-and-core-concepts:b00414

<details><summary>展开本节完整英文来源</summary>

4.17. Architecture Model

A representation of a subject of interest.

Note: An architecture model provides a smaller scale, simplified, and/or
abstract representation of the subject matter.

See also Section 4.76, “Stakeholder” , Section 4.20, “Architecture View” , and Section 4.21, “Architecture Viewpoint” .

</details>

<a id="sec-04_18"></a>
## 4.18. Architecture Partition

概念：架构分区是为开发管理而划分的架构子集。

适用条件：术语用于架构分区的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：分区是工作范围划分，非粒度层级。

决策方法：派生检查：说明分区边界及跨区依赖。

制品及证据：本节未要求新增独立交付物；派生检查可使用：分区范围、接口、责任。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00415, C220-web-2025:01-introduction-and-core-concepts:b00416

<details><summary>展开本节完整英文来源</summary>

4.18. Architecture Partition

A subset of architecture resulting from dividing that architecture to
facilitate its development and management.

</details>

<a id="sec-04_19"></a>
## 4.19. Architecture Principle

概念：架构原则是架构应满足的定性意图。

适用条件：术语用于架构原则的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：原则指导架构，与量化需求/验收标准不同。

决策方法：派生检查：将原则连至具体取舍和符合证据。

制品及证据：本节未要求新增独立交付物；派生检查可使用：原则、理由、影响和例外。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00417, C220-web-2025:01-introduction-and-core-concepts:b00418, C220-web-2025:01-introduction-and-core-concepts:b00419

<details><summary>展开本节完整英文来源</summary>

4.19. Architecture Principle

A qualitative statement of intent that should be met by the
architecture.

Note: A sample set of Architecture Principles is defined in the TOGAF Standard — ADM Techniques .

</details>

<a id="sec-04_20"></a>
## 4.20. Architecture View

概念：架构视图从一组相关关切的角度表示系统。

适用条件：术语用于架构视图从一组相关关切的角度表示系统。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：视图是具体表示，不是构造规则。

决策方法：派生检查：识别关切受众并确认视图覆盖。

制品及证据：本节未要求新增独立交付物；派生检查可使用：关切到视图追踪。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00420, C220-web-2025:01-introduction-and-core-concepts:b00421, C220-web-2025:01-introduction-and-core-concepts:b00422, C220-web-2025:01-introduction-and-core-concepts:b00423

<details><summary>展开本节完整英文来源</summary>

4.20. Architecture View

A representation of a system from the perspective of a related set of concerns.

Note: In some sections of this standard, the term “view” is used as a
synonym for “architecture view”.

See also Section 4.76, “Stakeholder” and Section 4.21, “Architecture Viewpoint” .

</details>

<a id="sec-04_21"></a>
## 4.21. Architecture Viewpoint

概念：架构视点规定一类视图的构造、解释、使用惯例与模式。

适用条件：术语用于架构视点规定一类视图的构造、解释、使用惯例与模式。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：视点定义规则，视图是具体实例。

决策方法：派生检查：核对视图是否按其视点规则构造。

制品及证据：本节未要求新增独立交付物；派生检查可使用：视点规范、模型种类和视图实例。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00424, C220-web-2025:01-introduction-and-core-concepts:b00425, C220-web-2025:01-introduction-and-core-concepts:b00426, C220-web-2025:01-introduction-and-core-concepts:b00427

<details><summary>展开本节完整英文来源</summary>

4.21. Architecture Viewpoint

A specification of the conventions for a particular kind of architecture
view.

Note: An architecture viewpoint can also be seen as the definition or schema
for that kind of architecture view. It establishes the conventions for constructing, interpreting, and using an architecture view to address
a specific concern (or set of concerns) about a system-of-interest. In some sections of this standard, the term “viewpoint” is used as a
synonym for “architecture viewpoint”.

See also Section B.25, “Metaview” .

</details>

<a id="sec-04_22"></a>
## 4.22. Architecture Vision

概念：架构愿景简述目标架构的业务价值与成功部署后的变化，作为详细工作的边界。

适用条件：术语用于架构愿景简述目标架构的业务价值与成功部署后的变化，作为详细工作的边界。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：愿景有激励与定界作用，非实现全部规格。

决策方法：派生检查：业务价值和范围能否指导后续设计。

制品及证据：本节未要求新增独立交付物；派生检查可使用：愿景、价值和批准范围。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00428, C220-web-2025:01-introduction-and-core-concepts:b00429, C220-web-2025:01-introduction-and-core-concepts:b00430

<details><summary>展开本节完整英文来源</summary>

4.22. Architecture Vision

A succinct description of the Target Architecture that describes its business value and the changes to the enterprise that will result from its successful deployment. It serves as an aspirational vision and a boundary for detailed architecture development.

Note: Phase A (Architecture Vision) is described in the TOGAF Standard — Architecture Development Method .

</details>

<a id="sec-04_23"></a>
## 4.23. Artifact

概念：制品描述架构的某方面。

适用条件：术语用于制品描述架构的某方面。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：制品表示构建块，不等于构建块或自动签署交付物。

决策方法：派生检查：指明所描述内容及契约身份。

制品及证据：本节未要求新增独立交付物；派生检查可使用：制品到模型对象与合同映射。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00431, C220-web-2025:01-introduction-and-core-concepts:b00432, C220-web-2025:01-introduction-and-core-concepts:b00433

<details><summary>展开本节完整英文来源</summary>

4.23. Artifact

An architectural work product that describes an aspect of the
architecture.

See also Section 4.26, “Building Block” .

</details>

<a id="sec-04_24"></a>
## 4.24. Baseline

概念：基线是正式评审同意后作为后续发展/变更依据的规格。

适用条件：术语用于基线的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：变更只能经正式变更控制或配置程序。

决策方法：派生检查：验证同意和版本，不从文件存在推基线。

制品及证据：本节未要求新增独立交付物；派生检查可使用：批准记录、版本和变更日志。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00434, C220-web-2025:01-introduction-and-core-concepts:b00435

<details><summary>展开本节完整英文来源</summary>

4.24. Baseline

A specification that has been formally reviewed and agreed upon, that
thereafter serves as the basis for further development or change and
that can be changed only through formal change control procedures or a
type of procedure such as configuration management.

</details>

<a id="sec-04_25"></a>
## 4.25. Boundaryless Information Flow™

概念：Boundaryless Information Flow指为业务流程改善访问集成信息的期望状态。

适用条件：术语用于Boundaryless Information Flow指为业务流程改善访问集成信息的期望状态。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：“无边界”不表示取消安全/隐私控制。

决策方法：派生检查：界定业务需要与授权共享程度。

制品及证据：本节未要求新增独立交付物；派生检查可使用：交换需求、权限和业务改进依据。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00436, C220-web-2025:01-introduction-and-core-concepts:b00437, C220-web-2025:01-introduction-and-core-concepts:b00438

<details><summary>展开本节完整英文来源</summary>

4.25. Boundaryless Information Flow™

A shorthand representation of “access to integrated information to
support business process improvements” representing a desired state of
an enterprise’s infrastructure specific to the business needs of the
organization.

Note: The need for Boundaryless Information Flow, a trademark of The Open Group, is described in the TOGAF ® Series Guide: The TOGAF Integrated Information Infrastructure Reference Model (III-RM) .

</details>

<a id="sec-04_26"></a>
## 4.26. Building Block

概念：构建块是可组合交付架构/解决方案的潜在可复用组件，细节随发展变化。

适用条件：术语用于构建块的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：早期名称可后续细分规格，ABB与SBB分别逻辑/实现。

决策方法：派生检查：保持身份与细化链，别把早期名称当完整规格。

制品及证据：本节未要求新增独立交付物；派生检查可使用：构建块定义、组合及细化追踪。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00439, C220-web-2025:01-introduction-and-core-concepts:b00440, C220-web-2025:01-introduction-and-core-concepts:b00441

<details><summary>展开本节完整英文来源</summary>

4.26. Building Block

A potentially re-usable component that can be combined with other
building blocks to deliver architectures and solutions.

Note: Building blocks can be defined at various levels of detail, depending
  on what stage of architecture development has been reached. E.g., at an early stage, a building block can simply consist of a name or an outline description. Later on, a building block may be
  decomposed into multiple supporting building blocks and may be accompanied by a full specification. Building blocks can relate to “architectures” or “solutions”. They are described in the TOGAF Standard — Architecture Content . See also Section 4.23, “Artifact” .

</details>

<a id="sec-04_27"></a>
## 4.27. Business Architecture

概念：业务架构多维表达能力、价值交付、信息、组织与战略产品政策流程等关系。

适用条件：术语用于业务架构多维表达能力、价值交付、信息、组织与战略产品政策流程等关系。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：业务架构连接业务目标及其他域，非单流程或组织图。

决策方法：派生检查：跨业务视角的关系是否有一致来源。

制品及证据：本节未要求新增独立交付物；派生检查可使用：能力/价值流/信息/组织与目标映射。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00442, C220-web-2025:01-introduction-and-core-concepts:b00443, C220-web-2025:01-introduction-and-core-concepts:b00444

<details><summary>展开本节完整英文来源</summary>

4.27. Business Architecture

A representation of holistic, multi-dimensional business views of:
capabilities, end-to-end value delivery, information, and organizational
structure; and the relationships among these business views and
strategies, products, policies, processes, initiatives, and
stakeholders.

Note: Business Architecture relates business elements to business goals and
elements of other domains. Business Architecture is described in the TOGAF Standard — Architecture Development Method .

</details>

<a id="sec-04_28"></a>
## 4.28. Business Capability

概念：业务能力是业务为特定目的拥有或可交换的特定能力。

适用条件：术语用于业务能力的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：能力what与实现方式how、组织和实例不同。

决策方法：派生检查：检验定义是否避免实现耦合。

制品及证据：本节未要求新增独立交付物；派生检查可使用：能力定义、目的及实现实例映射。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00445, C220-web-2025:01-introduction-and-core-concepts:b00446

<details><summary>展开本节完整英文来源</summary>

4.28. Business Capability

A particular ability that a business may possess or exchange to achieve
a specific purpose.

</details>

<a id="sec-04_29"></a>
## 4.29. Business Function

概念：业务功能按选定准则聚合业务行为，通常紧密对齐组织。

适用条件：术语用于业务功能按选定准则聚合业务行为，通常紧密对齐组织。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：功能聚合与稳定业务能力不同。

决策方法：派生检查：记录聚合准则和组织联系。

制品及证据：本节未要求新增独立交付物；派生检查可使用：功能行为、组织与能力映射。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00447, C220-web-2025:01-introduction-and-core-concepts:b00448

<details><summary>展开本节完整英文来源</summary>

4.29. Business Function

A collection of business behavior based on a chosen set of criteria, closely aligned to an organization.

</details>

<a id="sec-04_30"></a>
## 4.30. Business Governance

概念：业务治理确保流程政策及运营交付业务结果并遵守法规。

适用条件：术语用于业务治理确保流程政策及运营交付业务结果并遵守法规。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：结果、政策和运营对应，不能由技术合规代替。

决策方法：派生检查：识别业务结果责任与遵从证据。

制品及证据：本节未要求新增独立交付物；派生检查可使用：政策、业务指标、运营及接受记录。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00449, C220-web-2025:01-introduction-and-core-concepts:b00450

<details><summary>展开本节完整英文来源</summary>

4.30. Business Governance

Concerned with ensuring that the business processes and policies (and
their operation) deliver the business outcomes and adhere to relevant
business regulation.

</details>

<a id="sec-04_31"></a>
## 4.31. Business Model

概念：业务模型解释企业如何创造、交付、捕获价值。

适用条件：术语用于业务模型解释企业如何创造、交付、捕获价值。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：业务模型与流程/能力表示有不同关注点。

决策方法：派生检查：三个价值环节能否对应业务事实。

制品及证据：本节未要求新增独立交付物；派生检查可使用：价值主张、交付机制及收益模式。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00451, C220-web-2025:01-introduction-and-core-concepts:b00452

<details><summary>展开本节完整英文来源</summary>

4.31. Business Model

A model describing the rationale for how an enterprise creates, delivers, and captures value.

</details>

<a id="sec-04_32"></a>
## 4.32. Business Service

概念：业务服务封装独特业务行为以支持业务。

适用条件：术语用于业务服务封装独特业务行为以支持业务。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：对外服务可由多个内部业务服务支持。

决策方法：派生检查：明确服务行为、消费者和边界。

制品及证据：本节未要求新增独立交付物；派生检查可使用：业务服务与行为/消费者关系。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00453, C220-web-2025:01-introduction-and-core-concepts:b00454, C220-web-2025:01-introduction-and-core-concepts:b00455

<details><summary>展开本节完整英文来源</summary>

4.32. Business Service

Supports the business by encapsulating a unique “element of business
behavior”.

Note: A service offered external to the enterprise may be supported by
business services.

</details>

<a id="sec-04_33"></a>
## 4.33. Capability

概念：Capability是组织、人或系统拥有的能力。

适用条件：术语用于Capability的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：通用能力要按领域细化，不与业务能力及人员熟练度自动等同。

决策方法：派生检查：先声明能力拥有者与用途。

制品及证据：本节未要求新增独立交付物；派生检查可使用：能力主体、任务及证据。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00456, C220-web-2025:01-introduction-and-core-concepts:b00457, C220-web-2025:01-introduction-and-core-concepts:b00458

<details><summary>展开本节完整英文来源</summary>

4.33. Capability

An ability that an organization, person, or system possesses.

Note: This a general-purpose definition. See Section 4.28, “Business Capability” for how this concept is refined for usage in Business Architecture.

</details>

<a id="sec-04_34"></a>
## 4.34. Capability Architecture

概念：能力架构描述企业拥有的能力。

适用条件：术语用于能力架构描述企业拥有的能力。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：能力架构与能力增量、实现实例不同。

决策方法：派生检查：区分能力目标与已实现能力。

制品及证据：本节未要求新增独立交付物；派生检查可使用：能力范围、依赖与状态。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00459, C220-web-2025:01-introduction-and-core-concepts:b00460, C220-web-2025:01-introduction-and-core-concepts:b00461

<details><summary>展开本节完整英文来源</summary>

4.34. Capability Architecture

An architecture that describes the abilities that an enterprise possesses.

See also the TOGAF ® Series Guide: A Practitioners’ Approach to Developing Enterprise Architecture Following the TOGAF ADM .

</details>

<a id="sec-04_35"></a>
## 4.35. Capability Increment

概念：能力增量是能力架构中交付特定价值的离散部分，全部完成后实现能力。

适用条件：术语用于能力增量的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：增量不是单纯时间片或任务列表。

决策方法：派生检查：检验每增量价值及整体完备。

制品及证据：本节未要求新增独立交付物；派生检查可使用：增量、价值、能力实现关系。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00462, C220-web-2025:01-introduction-and-core-concepts:b00463

<details><summary>展开本节完整英文来源</summary>

4.35. Capability Increment

A discrete portion of a capability architecture that delivers specific
value. When all increments have been completed, the capability has been
realized.

</details>

<a id="sec-04_36"></a>
## 4.36. Communications and Stakeholder Management

概念：沟通/利益相关者管理管理EA实践关切及与服务消费者的沟通执行。

适用条件：术语用于沟通/利益相关者管理管理EA实践关切及与服务消费者的沟通执行。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：管理需求与执行沟通均需，不是通讯录。

决策方法：派生检查：关切、受众、内容及反馈是否连接。

制品及证据：本节未要求新增独立交付物；派生检查可使用：沟通计划、关切与反馈记录。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00464, C220-web-2025:01-introduction-and-core-concepts:b00465, C220-web-2025:01-introduction-and-core-concepts:b00466

<details><summary>展开本节完整英文来源</summary>

4.36. Communications and Stakeholder Management

The management of needs of stakeholders of the Enterprise Architecture
practice. It also manages the execution of communication between the
practice and the stakeholders and the practice and the consumers of its
services.

Note: Architecture stakeholder management is described in the TOGAF Standard — ADM Techniques .

</details>

<a id="sec-04_37"></a>
## 4.37. Concern

概念：Concern是一个或多个利益相关者对系统的兴趣，可决定可接受性。

适用条件：术语用于Concern的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：关切涵盖功能、开发、运营等，非必然已批准需求。

决策方法：派生检查：把关切转成明确可验证需求并保留来源。

制品及证据：本节未要求新增独立交付物；派生检查可使用：关切、利益相关者、需求追踪。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00467, C220-web-2025:01-introduction-and-core-concepts:b00468, C220-web-2025:01-introduction-and-core-concepts:b00469, C220-web-2025:01-introduction-and-core-concepts:b00470

<details><summary>展开本节完整英文来源</summary>

4.37. Concern

An interest in a system relevant to one or more of its stakeholders.

Note: Concerns may pertain to any aspect of the system’s functioning,
development, or operation, including considerations such as
performance, reliability, security, distribution, and evolvability and
may determine the acceptability of the system.

See also Section 4.76, “Stakeholder” .

</details>

<a id="sec-04_38"></a>
## 4.38. Course of Action

概念：Course of Action由战略目标提供方向和焦点，常交付业务模型价值主张。

适用条件：术语用于Course of Action由战略目标提供方向和焦点，常交付业务模型价值主张。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：行动方针连接战略与行动，非具体产品。

决策方法：派生检查：战略目标与行动方向是否一致。

制品及证据：本节未要求新增独立交付物；派生检查可使用：目标、行动方针及价值主张映射。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00471, C220-web-2025:01-introduction-and-core-concepts:b00472

<details><summary>展开本节完整英文来源</summary>

4.38. Course of Action

Direction and focus provided by strategic goals and objectives, often to deliver the value proposition characterized in the business model.

</details>

<a id="sec-04_39"></a>
## 4.39. Data Architecture

概念：数据架构描述主要数据类型/来源、逻辑/物理资产和管理资源。

适用条件：术语用于数据架构描述主要数据类型/来源、逻辑/物理资产和管理资源。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：逻辑、物理、管理责任与数据源分别记录。

决策方法：派生检查：检验数据结构、来源、所有权与使用需要。

制品及证据：本节未要求新增独立交付物；派生检查可使用：数据资产/来源和管理模型。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00473, C220-web-2025:01-introduction-and-core-concepts:b00474, C220-web-2025:01-introduction-and-core-concepts:b00475

<details><summary>展开本节完整英文来源</summary>

4.39. Data Architecture

A description of the structure of the enterprise’s major types and
sources of data, logical data assets, physical data assets, and data
management resources.

Note: Data Architecture is described in the TOGAF Standard — Architecture Method .

</details>

<a id="sec-04_40"></a>
## 4.40. Deliverable

概念：交付物由契约规定并经利益相关者正式评审同意签署。

适用条件：术语用于交付物由契约规定并经利益相关者正式评审同意签署。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：项目输出可转成仓库参考、标准或时点快照，身份有生命周期。

决策方法：派生检查：验收证据是否实际签署。

制品及证据：本节未要求新增独立交付物；派生检查可使用：合同、评审签署及归档状态。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00476, C220-web-2025:01-introduction-and-core-concepts:b00477, C220-web-2025:01-introduction-and-core-concepts:b00478

<details><summary>展开本节完整英文来源</summary>

4.40. Deliverable

An architectural work product that is contractually specified and in
turn formally reviewed, agreed, and signed off by the stakeholders.

Note: Deliverables represent the output of projects and those deliverables
that are in documentation form will typically be archived at
completion of a project, or transitioned into an Architecture
Repository as a reference model, standard, or snapshot of the
Architecture Landscape at a point in time.

</details>

<a id="sec-04_41"></a>
## 4.41. Digital Architecture

概念：数字架构综合EA、数据科学、通信IoT、安全AI等以交付运营服务。

适用条件：术语用于数字架构综合EA、数据科学、通信IoT、安全AI等以交付运营服务。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：跨学科范围不能自动推出每技术都适用。

决策方法：派生检查：按运营服务需求确定学科/技术范围。

制品及证据：本节未要求新增独立交付物；派生检查可使用：运营服务及跨域依赖。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00479, C220-web-2025:01-introduction-and-core-concepts:b00480

<details><summary>展开本节完整英文来源</summary>

4.41. Digital Architecture

The inclusive architecture focused on a combination of Enterprise
Architecture, data science, telecommunications and IoT, security,
artificial intelligence, cognitive science, neuroscience, robotics, and
social medias to deliver operational services.

</details>

<a id="sec-04_42"></a>
## 4.42. EA Landscape

概念：EA Landscape在本源直接指Architecture Landscape。

适用条件：术语用于EA Landscape在本源直接指Architecture Landscape。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：同义引用合并语义但保留来源别名。

决策方法：派生检查：统一对象ID并保留使用中/计划与时点。

制品及证据：本节未要求新增独立交付物；派生检查可使用：别名映射与景观状态。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00481, C220-web-2025:01-introduction-and-core-concepts:b00482

<details><summary>展开本节完整英文来源</summary>

4.42. EA Landscape

See Section 4.15, “Architecture Landscape” .

</details>

<a id="sec-04_43"></a>
## 4.43. Enterprise

概念：Enterprise通常最高层组织描述，覆盖使命功能且常跨多个组织。

适用条件：术语用于Enterprise通常最高层组织描述，覆盖使命功能且常跨多个组织。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：与1.1共同目标集合的表述范围有差异，需用情境边界协调。

决策方法：派生检查：明确本次企业包含哪些组织和使命。

制品及证据：本节未要求新增独立交付物；派生检查可使用：企业边界、共同目标和参与方。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00483, C220-web-2025:01-introduction-and-core-concepts:b00484

<details><summary>展开本节完整英文来源</summary>

4.43. Enterprise

The highest level (typically) of description of an organization and
typically covers all missions and functions. An enterprise will often
span multiple organizations.

</details>

<a id="sec-04_44"></a>
## 4.44. Enterprise Architecture Service

概念：EA服务是封装EA能力并提供特定EA功能的元素。

适用条件：术语用于EA服务的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：服务与人员角色、组织部门不同。

决策方法：派生检查：说明消费者、功能与服务责任。

制品及证据：本节未要求新增独立交付物；派生检查可使用：EA服务目录及能力/角色映射。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00485, C220-web-2025:01-introduction-and-core-concepts:b00486

<details><summary>展开本节完整英文来源</summary>

4.44. Enterprise Architecture Service

An encapsulated element of Enterprise Architecture capability that
delivers specific Enterprise Architecture functionality.

</details>

<a id="sec-04_45"></a>
## 4.45. Enterprise Continuum

概念：企业连续统将架构/SBB从通用到特定或逆向分类。

适用条件：术语用于企业连续统将架构/SBB从通用到特定或逆向分类。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：架构与解决方案连续统互补，不是仓库本身。

决策方法：派生检查：标分类方向与资产出处。

制品及证据：本节未要求新增独立交付物；派生检查可使用：连续统分类与仓库关联。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00487, C220-web-2025:01-introduction-and-core-concepts:b00488, C220-web-2025:01-introduction-and-core-concepts:b00489

<details><summary>展开本节完整英文来源</summary>

4.45. Enterprise Continuum

A categorization mechanism for classifying architecture and Solution
Building Blocks (SBBs) as they evolve from generic to specific
applicability (or vice versa ).

See also Section 4.10, “Architecture Continuum” and Section 4.75, “Solutions Continuum” .

</details>

<a id="sec-04_46"></a>
## 4.46. Foundation Architecture

概念：基础架构由通用构建块、关系及原则指南组成，为特定架构提供基础。

适用条件：术语用于基础架构由通用构建块、关系及原则指南组成，为特定架构提供基础。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：通用基础不能直接认定组织适用。

决策方法：派生检查：检验适配条件和需补内容。

制品及证据：本节未要求新增独立交付物；派生检查可使用：基础资产、适配理由及约束。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00490, C220-web-2025:01-introduction-and-core-concepts:b00491

<details><summary>展开本节完整英文来源</summary>

4.46. Foundation Architecture

Generic building blocks, their inter-relationships with other building
blocks, combined with the principles and guidelines that provide a
foundation on which more specific architectures can be built.

</details>

<a id="sec-04_47"></a>
## 4.47. Framework

概念：Framework为内容/过程提供结构以组织思考并保一致完备。

适用条件：术语用于Framework为内容/过程提供结构以组织思考并保一致完备。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：框架不等于实际模型或证据。

决策方法：派生检查：按框架检查遗漏，而非按模板存在判质量。

制品及证据：本节未要求新增独立交付物；派生检查可使用：框架、范围和缺口记录。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00492, C220-web-2025:01-introduction-and-core-concepts:b00493

<details><summary>展开本节完整英文来源</summary>

4.47. Framework

A structure for content or process that can be used as a tool to structure thinking, ensuring consistency and completeness.

</details>

<a id="sec-04_48"></a>
## 4.48. Gap

概念：Gap是两个状态差异的陈述，架构常比较基线与目标。

适用条件：术语用于Gap的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：差距不是已选解决方案或工作包。

决策方法：派生检查：同范围同粒度比较并保差异依据。

制品及证据：本节未要求新增独立交付物；派生检查可使用：基线/目标、差异及处理追踪。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00494, C220-web-2025:01-introduction-and-core-concepts:b00495, C220-web-2025:01-introduction-and-core-concepts:b00496

<details><summary>展开本节完整英文来源</summary>

4.48. Gap

A statement of difference between two states. Used in the context of gap
analysis, where the difference between the Baseline and Target
Architecture is identified.

Note: Gap analysis is described in the TOGAF Standard — ADM Techniques .

</details>

<a id="sec-04_49"></a>
## 4.49. Governance

概念：Governance监控指导业务或IS/IT管理以交付所需业务结果。

适用条件：术语用于Governance监控指导业务或IS/IT管理以交付所需业务结果。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：架构、业务、运营治理各有具体对象。

决策方法：派生检查：识别治理层级和决策权限。

制品及证据：本节未要求新增独立交付物；派生检查可使用：治理职责、结果标准和审计。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00497, C220-web-2025:01-introduction-and-core-concepts:b00498, C220-web-2025:01-introduction-and-core-concepts:b00499

<details><summary>展开本节完整英文来源</summary>

4.49. Governance

The discipline of monitoring and guiding the management of a business
(or IS/IT landscape) to deliver the business outcomes required.

See also Section 4.14, “Architecture Governance” , Section 4.30, “Business Governance” , Section B.27, “Operational Governance” ,
and Appendix B, Glossary of Supplementary Definitions .

</details>

<a id="sec-04_50"></a>
## 4.50. Information

概念：Information可用任何介质表示或沟通事实、数据或意见。

适用条件：术语用于Information可用任何介质表示或沟通事实、数据或意见。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：信息不局限数据库记录，也不必然是已验证事实。

决策方法：派生检查：保持来源、介质和可信状态。

制品及证据：本节未要求新增独立交付物；派生检查可使用：信息地图、出处及使用语境。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00500, C220-web-2025:01-introduction-and-core-concepts:b00501

<details><summary>展开本节完整英文来源</summary>

4.50. Information

Any communication or representation of facts, data, or opinions, in any
medium or form, including textual, numerical, graphic, cartographic, narrative, or audio-visual forms.

</details>

<a id="sec-04_51"></a>
## 4.51. Information Technology (IT)

概念：IT在本源是组织所用信息及相关技术的生命周期管理。

适用条件：术语用于IT在本源的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：定义侧重管理而非仅硬件软件总称。

决策方法：派生检查：跨定义映射时标出管理含义。

制品及证据：本节未要求新增独立交付物；派生检查可使用：信息技术生命周期与职责。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00502, C220-web-2025:01-introduction-and-core-concepts:b00503

<details><summary>展开本节完整英文来源</summary>

4.51. Information Technology (IT)

The lifecycle management of information and related technology used by
an organization.

</details>

<a id="sec-04_52"></a>
## 4.52. Interoperability

概念：互操作包含共享、交换并使用信息、互供互用服务以有效共同运作。

适用条件：术语用于互操作包含共享、交换并使用信息、互供互用服务以有效共同运作。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：可连通不等于语义可用或协作有效。

决策方法：派生检查：分别验证交换、理解、使用和服务行为。

制品及证据：本节未要求新增独立交付物；派生检查可使用：交换/使用测试、语义契约和服务结果。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00504, C220-web-2025:01-introduction-and-core-concepts:b00505

<details><summary>展开本节完整英文来源</summary>

4.52. Interoperability

The ability to share information and services The ability of two or more systems or components to exchange and use
information The ability of systems to provide and receive services from other
systems and to use the services so interchanged to enable them to
operate effectively together

</details>

<a id="sec-04_53"></a>
## 4.53. Logical

概念：Logical表示实现独立。

适用条件：术语用于Logical表示实现独立。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：逻辑架构不绑定物理供应商产品。

决策方法：派生检查：规格是否意外锁定实现。

制品及证据：本节未要求新增独立交付物；派生检查可使用：逻辑规格及物理分配分离。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00506, C220-web-2025:01-introduction-and-core-concepts:b00507, C220-web-2025:01-introduction-and-core-concepts:b00508

<details><summary>展开本节完整英文来源</summary>

4.53. Logical

Implementation-independent.

Note: A logical architecture is an implementation-independent definition of
the architecture.

</details>

<a id="sec-04_54"></a>
## 4.54. Metadata

概念：元数据是描述实体特征的关于数据的数据，介质不限。

适用条件：术语用于元数据的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：元数据与业务数据或元模型身份不同。

决策方法：派生检查：标描述对象、含义和治理责任。

制品及证据：本节未要求新增独立交付物；派生检查可使用：元数据定义、来源和对象映射。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00509, C220-web-2025:01-introduction-and-core-concepts:b00510

<details><summary>展开本节完整英文来源</summary>

4.54. Metadata

Data about data, of any sort in any media, that describes the characteristics of an entity.

</details>

<a id="sec-04_55"></a>
## 4.55. Metamodel

概念：元模型描述架构描述所用实体、特征和关键关系。

适用条件：术语用于元模型描述架构描述所用实体、特征和关键关系。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：元模型是模型规则，非具体企业实例集合。

决策方法：派生检查：类型/实例、属性/关系是否分离。

制品及证据：本节未要求新增独立交付物；派生检查可使用：元模型、实例校验和关系约束。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00511, C220-web-2025:01-introduction-and-core-concepts:b00512

<details><summary>展开本节完整英文来源</summary>

4.55. Metamodel

A model that describes the entities used in building an Architecture
Description, their characteristics, and the key relationships between
those entities.

</details>

<a id="sec-04_56"></a>
## 4.56. Method

概念：Method是处理一类问题的已定义可重复方法。

适用条件：术语用于Method的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：方法与实例执行、工具不同。

决策方法：派生检查：输入/步骤/输出能否重复说明。

制品及证据：本节未要求新增独立交付物；派生检查可使用：方法规则与执行证据。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00513, C220-web-2025:01-introduction-and-core-concepts:b00514

<details><summary>展开本节完整英文来源</summary>

4.56. Method

A defined, repeatable approach to address a particular type of problem.

</details>

<a id="sec-04_57"></a>
## 4.57. Modeling

概念：建模以模型构造帮助推理、洞见和澄清主题本质。

适用条件：术语用于建模以模型构造帮助推理、洞见和澄清主题本质。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：制图完成不等于推理有效。

决策方法：派生检查：模型如何支持所需决策。

制品及证据：本节未要求新增独立交付物；派生检查可使用：模型假设、推理与事实依据。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00515, C220-web-2025:01-introduction-and-core-concepts:b00516

<details><summary>展开本节完整英文来源</summary>

4.57. Modeling

A technique through construction of models which enables a subject to be
represented in a form that enables reasoning, insight, and clarity
concerning the essence of the subject matter.

</details>

<a id="sec-04_58"></a>
## 4.58. Model Kind

概念：Model Kind是一类建模的惯例。

适用条件：术语用于Model Kind的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：视点引用模型种类；视图包含模型。

决策方法：派生检查：记法/规则是否适配视点。

制品及证据：本节未要求新增独立交付物；派生检查可使用：模型种类、视点规范、模型实例。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00517, C220-web-2025:01-introduction-and-core-concepts:b00518, C220-web-2025:01-introduction-and-core-concepts:b00519

<details><summary>展开本节完整英文来源</summary>

4.58. Model Kind

Conventions for a type of modeling.

Note: An architecture viewpoint references one or more model kinds; an
architecture view incorporates one or more models.

</details>

<a id="sec-04_59"></a>
## 4.59. Objective

概念：Objective以Specific/Measurable/Actionable/Realistic/Timebound陈述组织目标。

适用条件：术语用于Objective以Specific/Measurable/Actionable/Realistic/Timebound陈述组织目标。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：目标值需时间与可测条件，源A是Actionable。

决策方法：派生检查：目标基值、量纲、时限及可行依据是否完整。

制品及证据：本节未要求新增独立交付物；派生检查可使用：目标、度量、期限与业务依据。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00520, C220-web-2025:01-introduction-and-core-concepts:b00521

<details><summary>展开本节完整英文来源</summary>

4.59. Objective

An organizational aim that is declared in a Specific, Measurable,
Actionable, Realistic, and Timebound (SMART) way. For example, “Increase
capacity utilization by 30% by the end of the year, to support the
planned increase in market share”.

</details>

<a id="sec-04_60"></a>
## 4.60. Pattern

概念：Pattern在情境中说明构建块的可复用问题解法。

适用条件：术语用于Pattern在情境中说明构建块的可复用问题解法。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：构建块是使用对象，模式说明何时为何如何与取舍。

决策方法：派生检查：当前情境是否满足模式适用条件。

制品及证据：本节未要求新增独立交付物；派生检查可使用：模式问题、条件、组合和取舍。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00522, C220-web-2025:01-introduction-and-core-concepts:b00523, C220-web-2025:01-introduction-and-core-concepts:b00524, C220-web-2025:01-introduction-and-core-concepts:b00525

<details><summary>展开本节完整英文来源</summary>

4.60. Pattern

A technique for putting building blocks into context; for example, to
describe a re-usable solution to a problem.

Note: Building blocks are what you use: (architecture) patterns can tell you
how you use them, when, why, and what trade-offs you have to make in
doing so.

See also Section 4.26, “Building Block” .

</details>

<a id="sec-04_61"></a>
## 4.61. Physical

概念：Physical指现实、有形的实现。

适用条件：术语用于Physical指现实、有形的实现。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：逻辑架构由物理架构实现，不要求一对一。

决策方法：派生检查：是否有实际实现资产与配置证据。

制品及证据：本节未要求新增独立交付物；派生检查可使用：物理组件/部署及逻辑追踪。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00526, C220-web-2025:01-introduction-and-core-concepts:b00527, C220-web-2025:01-introduction-and-core-concepts:b00528

<details><summary>展开本节完整英文来源</summary>

4.61. Physical

Real-world, tangible.

Note: A logical architecture is realized through a physical architecture.

</details>

<a id="sec-04_62"></a>
## 4.62. Principle

概念：Principle在本源指Architecture Principle。

适用条件：术语用于Principle在本源指Architecture Principle。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：引用别名不创建新原则类型。

决策方法：派生检查：按4.19定性意图核对。

制品及证据：本节未要求新增独立交付物；派生检查可使用：原则别名与治理记录。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00529, C220-web-2025:01-introduction-and-core-concepts:b00530

<details><summary>展开本节完整英文来源</summary>

4.62. Principle

See Section 4.19, “Architecture Principle” .

</details>

<a id="sec-04_63"></a>
## 4.63. Product

概念：Product是企业向客户提供的业务成果，含材料或服务。

适用条件：术语用于Product的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：产品不局限软件，也不同于单服务。

决策方法：派生检查：标客户成果及价值而非仅技术模块。

制品及证据：本节未要求新增独立交付物；派生检查可使用：产品、客户、材料/服务映射。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00531, C220-web-2025:01-introduction-and-core-concepts:b00532

<details><summary>展开本节完整英文来源</summary>

4.63. Product

An outcome generated by the business to be offered to customers. Products include materials and/or services.

</details>

<a id="sec-04_64"></a>
## 4.64. Reference Model (RM)

概念：参考模型以少量统一概念解释环境重要关系，支持一致语义和规范。

适用条件：术语用于参考模型以少量统一概念解释环境重要关系，支持一致语义和规范。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：参考模型不直接绑定具体技术实现。

决策方法：派生检查：复用其语义而非照抄部署。

制品及证据：本节未要求新增独立交付物；派生检查可使用：参考模型概念、组织适配和实现映射。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00533, C220-web-2025:01-introduction-and-core-concepts:b00534, C220-web-2025:01-introduction-and-core-concepts:b00535

<details><summary>展开本节完整英文来源</summary>

4.64. Reference Model (RM)

An abstract framework for understanding significant relationships among
the entities of [an] environment, and for the development of consistent
standards or specifications supporting that environment.

Note: A reference model is based on a small number of unifying concepts and
may be used as a basis for education and explaining standards to a
non-specialist. A reference model is not directly tied to any
standards, technologies, or other concrete implementation details, but
it does seek to provide common semantics that can be used
unambiguously across and between different implementations. Source: OASIS ® ; refer to www.oasis-open.org/committees/soa-rm/faq.php .

</details>

<a id="sec-04_65"></a>
## 4.65. Requirement

概念：Requirement是不歧义、可测试/度量且为可接受性所必需的需求陈述。

适用条件：术语用于Requirement的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：愿望、问题和需求不同，必要性须关联接受。

决策方法：派生检查：给明确测试或度量办法并核对必要性。

制品及证据：本节未要求新增独立交付物；派生检查可使用：需求来源、验收方法与接受证据。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00536, C220-web-2025:01-introduction-and-core-concepts:b00537

<details><summary>展开本节完整英文来源</summary>

4.65. Requirement

A statement of need, which is unambiguous, testable or measurable, and
necessary for acceptability.

</details>

<a id="sec-04_66"></a>
## 4.66. Roadmap

概念：Roadmap是跨学科通常跨年的业务或技术变化抽象计划。

适用条件：术语用于Roadmap的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：路线图不同于详细迁移计划或单项目进度。

决策方法：派生检查：状态、依赖和时间范围是否可理解。

制品及证据：本节未要求新增独立交付物；派生检查可使用：路线图、过渡状态和依赖。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00538, C220-web-2025:01-introduction-and-core-concepts:b00539

<details><summary>展开本节完整英文来源</summary>

4.66. Roadmap

An abstracted plan for business or technology change, typically
operating across multiple disciplines over multiple years. Normally used
in the phrases Technology Roadmap, Architecture Roadmap, etc.

</details>

<a id="sec-04_67"></a>
## 4.67. Role

概念：Role是参与者在活动中的行为/所扮角色，也指个人在组织中以技能经验贡献的职责。

适用条件：术语用于Role的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：Actor可多Role，角色不是人员或能力等级。

决策方法：派生检查：角色任务、授权和人员证据分别记录。

制品及证据：本节未要求新增独立交付物；派生检查可使用：角色、Actor、任务和能力证据。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00540, C220-web-2025:01-introduction-and-core-concepts:b00541, C220-web-2025:01-introduction-and-core-concepts:b00542

<details><summary>展开本节完整英文来源</summary>

4.67. Role

The usual or expected behavior of an actor, or the part somebody or something plays in a particular process or event. An actor may have a number of roles The part an individual plays in an organization and the contribution they make through the application of their skills, knowledge,
experience, and abilities

See also Section 4.2, “Actor” .

</details>

<a id="sec-04_68"></a>
## 4.68. Segment Architecture

概念：Segment Architecture是企业区域的详细正式描述，用于项目群/组合对齐变化。

适用条件：术语用于Segment Architecture的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：分段粒度与战略总体及离散解决方案有别。

决策方法：派生检查：范围与战略约束及跨段依赖是否明确。

制品及证据：本节未要求新增独立交付物；派生检查可使用：分段模型、战略对齐和项目组合关系。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00543, C220-web-2025:01-introduction-and-core-concepts:b00544, C220-web-2025:01-introduction-and-core-concepts:b00545

<details><summary>展开本节完整英文来源</summary>

4.68. Segment Architecture

A detailed, formal description of areas within an enterprise, used at the program or portfolio level to organize and align change activity.

See also Section 4.78, “Strategic Architecture” .

</details>

<a id="sec-04_69"></a>
## 4.69. Service

概念：Service封装行为，响应Actor或其他服务请求，有接口和描述。

适用条件：术语用于Service封装行为，响应Actor或其他服务请求，有接口和描述。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：服务是行为及契约边界，非组织单元。

决策方法：派生检查：请求、响应、接口与质量是否明确。

制品及证据：本节未要求新增独立交付物；派生检查可使用：服务接口、描述和消费者关系。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00546, C220-web-2025:01-introduction-and-core-concepts:b00547, C220-web-2025:01-introduction-and-core-concepts:b00548

<details><summary>展开本节完整英文来源</summary>

4.69. Service

An encapsulated element of behavior that provides specific functionality
in response to requests from actors or other services.

Note: A service has an interface and description.

</details>

<a id="sec-04_70"></a>
## 4.70. Service Orientation

概念：服务导向从提供和消费服务理解企业/系统/构建块。

适用条件：术语用于服务导向从提供和消费服务理解企业/系统/构建块。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：导向是分析视角，非具体SOA实现。

决策方法：派生检查：供需服务与责任是否连接。

制品及证据：本节未要求新增独立交付物；派生检查可使用：服务提供/消费模型。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00549, C220-web-2025:01-introduction-and-core-concepts:b00550, C220-web-2025:01-introduction-and-core-concepts:b00551

<details><summary>展开本节完整英文来源</summary>

4.70. Service Orientation

Viewing an enterprise, system, or building block in terms of services
provided and consumed.

See also Section 4.71, “Service-Oriented Architecture (SOA)” .

</details>

<a id="sec-04_71"></a>
## 4.71. Service-Oriented Architecture (SOA)

概念：SOA是支持服务导向的架构风格。

适用条件：术语用于SOA的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：风格不等于单一通信协议或产品。

决策方法：派生检查：风格原则是否体现在服务边界和交互。

制品及证据：本节未要求新增独立交付物；派生检查可使用：SOA原则、服务契约与模型。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00552, C220-web-2025:01-introduction-and-core-concepts:b00553, C220-web-2025:01-introduction-and-core-concepts:b00554

<details><summary>展开本节完整英文来源</summary>

4.71. Service-Oriented Architecture (SOA)

An architectural style that supports service orientation.

See also Section 4.7, “Architectural Style” and Section 4.70, “Service Orientation” .

</details>

<a id="sec-04_72"></a>
## 4.72. Service Portfolio

概念：服务组合是服务集合，可能含接口定义，用于规定构建块/系统需求。

适用条件：术语用于服务组合的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：集合的需求用途不同于实际部署目录。

决策方法：派生检查：标所需/已提供状态及组合范围。

制品及证据：本节未要求新增独立交付物；派生检查可使用：服务组合与需求/接口映射。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00555, C220-web-2025:01-introduction-and-core-concepts:b00556, C220-web-2025:01-introduction-and-core-concepts:b00557

<details><summary>展开本节完整英文来源</summary>

4.72. Service Portfolio

A collection of services, potentially an interface definition.

Note: It is used in the TOGAF framework to define the requirement for a building block or system.

</details>

<a id="sec-04_73"></a>
## 4.73. Solution Architecture

概念：解决方案架构描述离散聚焦的业务运营活动及IS/IT支持。

适用条件：术语用于解决方案架构描述离散聚焦的业务运营活动及IS/IT支持。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：解决方案视角仍有业务对象，不只技术设计。

决策方法：派生检查：方案如何支持该业务活动及企业约束。

制品及证据：本节未要求新增独立交付物；派生检查可使用：解决方案范围、活动和IS/IT支撑。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00558, C220-web-2025:01-introduction-and-core-concepts:b00559

<details><summary>展开本节完整英文来源</summary>

4.73. Solution Architecture

A description of a discrete and focused business operation or activity and how IS/IT supports that operation.

</details>

<a id="sec-04_74"></a>
## 4.74. Solution Building Block (SBB)

概念：SBB为物理/实现特定组件，实现一个或多个逻辑ABB的一部或全部。

适用条件：术语用于SBB为物理/实现特定组件，实现一个或多个逻辑ABB的一部或全部。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：业务、应用、技术皆可有SBB，不限定软件。

决策方法：派生检查：明确实现覆盖与不足，不推一ABB一SBB。

制品及证据：本节未要求新增独立交付物；派生检查可使用：SBB配置、ABB覆盖和证据。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00560, C220-web-2025:01-introduction-and-core-concepts:b00561, C220-web-2025:01-introduction-and-core-concepts:b00562

<details><summary>展开本节完整英文来源</summary>

4.74. Solution Building Block (SBB)

A physical or implementation-specific component that realizes part or all of one or more logical Architecture Building Blocks (ABBs).

Note: There are business, application, and technology SBBs.

</details>

<a id="sec-04_75"></a>
## 4.75. Solutions Continuum

概念：解决方案连续统将Solutions Landscape/Reference Library组件制品按专门化分类。

适用条件：术语用于解决方案连续统将Solutions Landscape/Reference Library组件制品按专门化分类。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：解决方案分类不同于架构分类但共同属于企业连续统。

决策方法：派生检查：标实现资产来源和通用度。

制品及证据：本节未要求新增独立交付物；派生检查可使用：解决方案分类及复用适配。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00563, C220-web-2025:01-introduction-and-core-concepts:b00564, C220-web-2025:01-introduction-and-core-concepts:b00565

<details><summary>展开本节完整英文来源</summary>

4.75. Solutions Continuum

A categorization mechanism, with increasing detail and specialization, for the components and artifacts stored in the Solutions Landscape or Reference Library (part of the Architecture Repository).

See also Section 4.45, “Enterprise Continuum” and Section 4.10, “Architecture Continuum” .

</details>

<a id="sec-04_76"></a>
## 4.76. Stakeholder

概念：Stakeholder是对系统有兴趣的个人、团队、组织或其类别。

适用条件：术语用于Stakeholder的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：Stakeholder未必Actor，也未必有批准权。

决策方法：派生检查：分别记录关切、参与和权限。

制品及证据：本节未要求新增独立交付物；派生检查可使用：利益相关者、关切及授权记录。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00566, C220-web-2025:01-introduction-and-core-concepts:b00567

<details><summary>展开本节完整英文来源</summary>

4.76. Stakeholder

An individual, team, organization, or class thereof, having an interest
in a system.

</details>

<a id="sec-04_77"></a>
## 4.77. Standards Library

概念：标准库收集可定义组织特定服务与组件的标准。

适用条件：术语用于标准库收集可定义组织特定服务与组件的标准。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：已采用标准与参考建议不同。

决策方法：派生检查：注明批准状态、适用范围和版本。

制品及证据：本节未要求新增独立交付物；派生检查可使用：标准库、采用记录和合规规则。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00568, C220-web-2025:01-introduction-and-core-concepts:b00569, C220-web-2025:01-introduction-and-core-concepts:b00570

<details><summary>展开本节完整英文来源</summary>

4.77. Standards Library

A library of standards that can be used to define the particular
services and other components of an Organization-Specific Architecture.

Note: The Standards Library is described in the TOGAF Standard — Architecture Content .

</details>

<a id="sec-04_78"></a>
## 4.78. Strategic Architecture

概念：战略架构给企业长期高层正式概览以组织运营变化并设置方向。

适用条件：术语用于战略架构给企业长期高层正式概览以组织运营变化并设置方向。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：战略概要与分段详细度不同。

决策方法：派生检查：方向、约束及到分段/能力架构追踪是否明确。

制品及证据：本节未要求新增独立交付物；派生检查可使用：战略架构、目标与下层追踪。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00571, C220-web-2025:01-introduction-and-core-concepts:b00572

<details><summary>展开本节完整英文来源</summary>

4.78. Strategic Architecture

A summary formal description of the enterprise, providing an organizing framework for operational and change activity, and an executive-level, long-term view for direction setting.

</details>

<a id="sec-04_79"></a>
## 4.79. Target Architecture

概念：目标架构描述组织正在开发的未来状态，可有多未来状态组成演进路线。

适用条件：术语用于目标架构描述组织正在开发的未来状态，可有多未来状态组成演进路线。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：目标与过渡及现状不是同状态。

决策方法：派生检查：标时点和目标/过渡身份。

制品及证据：本节未要求新增独立交付物；派生检查可使用：未来状态、路线图和目标验收。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00573, C220-web-2025:01-introduction-and-core-concepts:b00574, C220-web-2025:01-introduction-and-core-concepts:b00575

<details><summary>展开本节完整英文来源</summary>

4.79. Target Architecture

The description of a future state of the architecture being developed
for an organization.

Note: There may be several future states developed as a roadmap to show the evolution of the architecture to a target state.

</details>

<a id="sec-04_80"></a>
## 4.80. Taxonomy of Architecture Views

概念：视图分类体系是架构相关全部视图的有组织集合。

适用条件：术语用于视图分类体系的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：集合组织不保证每关切已覆盖。

决策方法：派生检查：体系是否覆盖所需受众且视图一致。

制品及证据：本节未要求新增独立交付物；派生检查可使用：视图分类、关切覆盖和模型追踪。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00576, C220-web-2025:01-introduction-and-core-concepts:b00577

<details><summary>展开本节完整英文来源</summary>

4.80. Taxonomy of Architecture Views

The organized collection of all architecture views pertinent to an
architecture.

</details>

<a id="sec-04_81"></a>
## 4.81. Technology Architecture

概念：技术架构描述技术服务与技术组件的结构和交互。

适用条件：术语用于技术架构描述技术服务与技术组件的结构和交互。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：技术服务行为与组件实现分开。

决策方法：派生检查：技术支撑如何满足应用和数据需要。

制品及证据：本节未要求新增独立交付物；派生检查可使用：技术组件/服务/交互和依赖。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00578, C220-web-2025:01-introduction-and-core-concepts:b00579, C220-web-2025:01-introduction-and-core-concepts:b00580

<details><summary>展开本节完整英文来源</summary>

4.81. Technology Architecture

A description of the structure and interaction of the technology
services and technology components.

Note: Technology Architecture is described in the TOGAF Standard — Architecture Development Method .

</details>

<a id="sec-04_82"></a>
## 4.82. Technology Component

概念：技术组件可为支持应用数据的通用基础设施构建块，也可封装产品类或具体产品。

适用条件：术语用于技术组件可为支持应用数据的通用基础设施构建块，也可封装产品类或具体产品。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：术语兼有通用/具体义，需声明抽象身份。

决策方法：派生检查：区分产品类、实际产品和服务。

制品及证据：本节未要求新增独立交付物；派生检查可使用：技术组件类型、配置和技术服务。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00581, C220-web-2025:01-introduction-and-core-concepts:b00582

<details><summary>展开本节完整英文来源</summary>

4.82. Technology Component

A technology building block. A generic infrastructure technology that
supports and enables application or data components (directly or indirectly) by providing technology services An encapsulation of technology infrastructure that represents a class of technology product or specific technology product

</details>

<a id="sec-04_83"></a>
## 4.83. Technology Service

概念：技术服务是提供应用交付支撑基础设施所需的技术能力。

适用条件：术语用于技术服务的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：技术能力和实际组件实现不同。

决策方法：派生检查：服务功能质量与应用需求匹配。

制品及证据：本节未要求新增独立交付物；派生检查可使用：技术服务、应用依赖和实现。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00583, C220-web-2025:01-introduction-and-core-concepts:b00584

<details><summary>展开本节完整英文来源</summary>

4.83. Technology Service

A technical capability required to provide enabling infrastructure that supports the delivery of applications.

</details>

<a id="sec-04_84"></a>
## 4.84. Transition Architecture

概念：过渡架构正式描述架构有意义时点的一个状态。

适用条件：术语用于过渡架构正式描述架构有意义时点的一个状态。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：一或多过渡状态连接基线至目标，非阶段名。

决策方法：派生检查：证明状态可运营和满足里程碑条件。

制品及证据：本节未要求新增独立交付物；派生检查可使用：过渡状态、依赖与接受条件。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00585, C220-web-2025:01-introduction-and-core-concepts:b00586, C220-web-2025:01-introduction-and-core-concepts:b00587

<details><summary>展开本节完整英文来源</summary>

4.84. Transition Architecture

A formal description of one state of the architecture at an
architecturally significant point in time.

Note: One or more Transition Architectures may be used to describe the progression in time from the Baseline to the Target Architecture. Transition Architecture is described in the TOGAF Standard — Architecture Content .

</details>

<a id="sec-04_85"></a>
## 4.85. Value Stream

概念：价值流表示为客户、利益相关者或最终用户形成整体结果的端到端活动。

适用条件：术语用于价值流表示为客户、利益相关者或最终用户形成整体结果的端到端活动。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：价值流与业务能力/实现流程不同。

决策方法：派生检查：每阶段增值与总体客户结果明确。

制品及证据：本节未要求新增独立交付物；派生检查可使用：价值流阶段、价值项与能力映射。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00588, C220-web-2025:01-introduction-and-core-concepts:b00589

<details><summary>展开本节完整英文来源</summary>

4.85. Value Stream

A representation of an end-to-end collection of activities that create
an overall result for a customer, stakeholder, or end user.

</details>

<a id="sec-04_86"></a>
## 4.86. View

概念：View在本源指Architecture View。

适用条件：术语用于View在本源指Architecture View。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：同义别名不等于视点。

决策方法：派生检查：按4.20追踪关切和实际表示。

制品及证据：本节未要求新增独立交付物；派生检查可使用：视图别名和关切覆盖。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00590, C220-web-2025:01-introduction-and-core-concepts:b00591

<details><summary>展开本节完整英文来源</summary>

4.86. View

See Section 4.20, “Architecture View” .

</details>

<a id="sec-04_87"></a>
## 4.87. Viewpoint

概念：Viewpoint在本源指Architecture Viewpoint。

适用条件：术语用于Viewpoint在本源指Architecture Viewpoint。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：同义别名是规则而非具体图。

决策方法：派生检查：按4.21核对构造惯例。

制品及证据：本节未要求新增独立交付物；派生检查可使用：视点别名与规则。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00592, C220-web-2025:01-introduction-and-core-concepts:b00593

<details><summary>展开本节完整英文来源</summary>

4.87. Viewpoint

See Section 4.21, “Architecture Viewpoint” .

</details>

<a id="sec-04_88"></a>
## 4.88. Viewpoint Library

概念：视点库把视点规格存于Reference Library。

适用条件：术语用于视点库把视点规格存于Reference Library。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：视点规格可复用，视图实例仍属具体架构。

决策方法：派生检查：标视点版本及实例应用。

制品及证据：本节未要求新增独立交付物；派生检查可使用：视点库、版本和视图追踪。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00594, C220-web-2025:01-introduction-and-core-concepts:b00595

<details><summary>展开本节完整英文来源</summary>

4.88. Viewpoint Library

A collection of the specifications of architecture viewpoints contained
in the Reference Library portion of the Architecture Repository.

</details>

<a id="sec-04_89"></a>
## 4.89. Work Package

概念：工作包为实现一个或多业务目标的一组行动，可是项目部分、整项目或项目群。

适用条件：术语用于工作包为实现一个或多业务目标的一组行动，可的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：工作包不是必然一项目，也不是能力增量同义。

决策方法：派生检查：说明目标、范围及与项目/能力关系。

制品及证据：本节未要求新增独立交付物；派生检查可使用：工作包、业务目标和交付依赖。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00596, C220-web-2025:01-introduction-and-core-concepts:b00597

<details><summary>展开本节完整英文来源</summary>

4.89. Work Package

A set of actions identified to achieve one or more objectives for the
business. A work package can be a part of a project, a complete project,
or a program.

</details>

<a id="apdxa"></a>
## A: Referenced Documents

概念：附录A登记标准引用来源，含指南、其他Open Group出版物和其他机构资料。

适用条件：核对引用依据与语料覆盖。

逻辑关系：引用存在不表示本地已取得或逐章审阅；参考版本属于源版快照。

决策方法：按A.1/A.2/A.3类别登记取得与解析状态。

制品及证据：来源版本和解析状态；本轮26指南以外引用保持独立范围。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00598, C220-web-2025:01-introduction-and-core-concepts:b00599

<details><summary>展开本节完整英文来源</summary>

A: Referenced Documents

This informative appendix contains a list of the TOGAF Series Guides that form part of the overall TOGAF Library built around the TOGAF Fundamentals.

</details>

<a id="sec-05_00_00_01"></a>
## A.1. The Open Group TOGAF Series Guides

概念：引用指南清单覆盖方法、业务、安全、数据、敏捷、可持续等特定场景。

适用条件：选用详细实践方法。

逻辑关系：G175/G174/G179等被引指南与当前26份本地系列指南集合不同。

决策方法：逐项匹配本地出版物与版本，缺项不能以他书转述冒充。

制品及证据：引文到本地资料映射及缺失清单。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00600, C220-web-2025:01-introduction-and-core-concepts:b00601

<details><summary>展开本节完整英文来源</summary>

A.1. The Open Group TOGAF Series Guides

TOGAF ® Series Guide: Applying the ADM Using Agile Sprints, April 2022 (G210), published by The Open Group; refer to www.opengroup.org/library/g210 TOGAF ® Series Guide: A Practitioners’ Approach to Developing Enterprise Architecture Following the TOGAF ADM, April 2022 (G186), published by The Open Group; refer to: www.opengroup.org/library/g186 TOGAF ® Series Guide: An Approach to Selecting Building Blocks, September 2024 (G248), published by The Open Group; refer to: www.opengroup.org/library/g248 TOGAF ® Series Guide: Architecture Maturity Models, April 2022 (G203), published by The Open Group; refer to: www.opengroup.org/library/g203 TOGAF ® Series Guide: Architecture Project Management, April 2022 (G188), published by The Open Group; refer to: www.opengroup.org/library/g188 TOGAF ® Series Guide: Architecture Roles and Skills, September 2024 (G249), published by The Open Group; refer to: www.opengroup.org/library/g249 TOGAF ® Series Guide: Architecture Skills Framework, April 2022 (G198), published by The Open Group; refer to: www.opengroup.org/library/g198 TOGAF ® Series Guide: Business Capabilities, Version 2, April 2022 (G211), published by The Open Group; refer to: www.opengroup.org/library/g211 TOGAF ® Series Guide: Business Capability Planning, April 2023 (G233), published by The Open Group; refer to: www.opengroup.org/library/g233 TOGAF ® Series Guide: Business Models, April 2022 (G18A), published by The Open Group; refer to: www.opengroup.org/library/g18a TOGAF ® Series Guide: Business Scenarios, April 2022 (G176), published by The Open Group; refer to: www.opengroup.org/library/g176 TOGAF ® Series Guide: Digital Technology Adoption — A Guide to Readiness Assessment and Roadmap Development, April 2022 (G212), published by The Open Group; refer to: www.opengroup.org/library/g212 TOGAF ® Series Guide: Enabling Enterprise Agility, April 2022 (G20F), published by The Open Group; refer to: www.opengroup.org/library/g20f TOGAF ® Series Guide: Environmentally Sustainable Information Systems, February 2024 (G242), published by The Open Group; refer to: www.opengroup.org/library/g242 TOGAF ® Series Guide: Information Architecture: Business Intelligence & Analytics, September 2023 (G238), published by The Open Group; refer to: www.opengroup.org/library/g238 TOGAF ® Series Guide: Information Architecture — Customer Master Data Management, April 2022 (G21B), published by The Open Group; refer to: www.opengroup.org/library/g21b TOGAF ® Series Guide: Information Architecture: Metadata Management, April 2023 (G234), published by The Open Group; refer to: www.opengroup.org/library/g234 TOGAF ® Series Guide: Information Mapping, April 2022 (G190), published by The Open Group; refer to: www.opengroup.org/library/g190 TOGAF ® Series Guide: Integrating Risk and Security within a TOGAF ® Enterprise Architecture, April 2022 (G152), published by The Open Group; refer to: www.opengroup.org/library/g152 TOGAF ® Series Guide: Organization Mapping, April 2022 (G206), published by The Open Group; refer to: www.opengroup.org/library/g206 TOGAF ® Series Guide: The TOGAF Integrated Information Infrastructure Reference Model (III-RM): An Architected Approach to Boundaryless Information Flow™, November 2017 (G179), published by The Open Group; refer to: www.opengroup.org/library/g179 TOGAF ® Series Guide: The TOGAF Leader’s Guide to Establishing and Evolving an EA Capability, April 2022 (G184), published by The Open Group; refer to: www.opengroup.org/library/g184 TOGAF ® Series Guide: The TOGAF Technical Reference Model (TRM), September 2017 (G175), published by The Open Group; refer to: www.opengroup.org/library/g175 TOGAF ® Series Guide: Using the TOGAF ® Framework to Define and Govern Service-Oriented Architectures, September 2017 (G174), published by The Open Group; refer to: www.opengroup.org/library/g174 TOGAF ® Series Guide: Value Streams, April 2022 (G178), published by The Open Group; refer to: www.opengroup.org/library/g178

</details>

<a id="sec-05_00_00_02"></a>
## A.2. Other Publications from The Open Group

概念：其他Open Group资料含ArchiMate、DPBoK、Open FAIR、O-AA、IT4IT及合规检查清单等。

适用条件：需要相关模型、量化风险或合规问题库。

逻辑关系：这些各有独立标准/指南范围；不计入六卷正文。

决策方法：区分本地已保存与被引用，按用途另核对适用版本。

制品及证据：跨标准来源清单；G253被引用不表示已在本轮主语料深析。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00602, C220-web-2025:01-introduction-and-core-concepts:b00603

<details><summary>展开本节完整英文来源</summary>

A.2. Other Publications from The Open Group

A Practical Approach to Application Portfolio Consolidation using the TOGAF ® Standard, The Open Group Guide, July 2018 (G18B), published by The Open Group; refer to: www.opengroup.org/library/g18b Archi Banking Group: Combining the BIAN Reference Model, ArchiMate ® Modeling Notation, and the TOGAF ® Framework, Case Study, March 2020 (Y201), published by The Open Group; refer to: www.opengroup.org/library/y201 ArchiMate ® 3.2 Specification, The Open Group Standard, October 2022 (C226), published by The Open Group; refer to: www.opengroup.org/library/c226 Digital Practitioner Body of Knowledge™ Standard (also known as the DPBoK™ Standard), The Open Group Standard, January 2020 (C196), published by The Open Group; refer to: www.opengroup.org/library/c196 Exploring Synergies between TOGAF ® and Frameworx, White Paper, May 2011 (W114), published by The Open Group; refer to: www.opengroup.org/library/w114 Information Architecture: Business Intelligence & Analytics and Metadata Management Reference Models, The Open Group Guide, January 2020 (G201), published by The Open Group; refer to: www.opengroup.org/library/g201 Open Risk Analysis (O-RA), Version 2.0.1, The Open Group Standard, November 2021 (C20A), published by The Open Group; refer to: www.opengroup.org/library/c20a Open Risk Taxonomy (O-RT), Version 3.0.1, The Open Group Standard, November 2021 (C20B), published by The Open Group; refer to: www.opengroup.org/library/c20b The Open Agile Architecture™ Standard, The Open Group Standard, September 2020 (C208), published by The Open Group; refer to: www.opengroup.org/library/c208 The Open Group IT4IT™ Standard, Version 3.0.1, The Open Group Standard, October 2024 (C24A), published by The Open Group; refer to: www.opengroup.org/library/c24a TOGAF ® 9 and DoDAF 2.0, White Paper, July 2010 (W105), published by The Open Group; refer to: www.opengroup.org/library/w105 TOGAF ® and SABSA ® Integration, White Paper, October 2011 (W117), published by The Open Group; refer to: www.opengroup.org/library/w117 Architecture Compliance Review Checklists, The Open Group Guide, June 2025 (G253), published by The Open Group; refer to: https://www.opengroup.org/library/g253 [www.opengroup.org/library/g253]

</details>

<a id="sec-05_00_00_03"></a>
## A.3. Other Referenced Documents

概念：其他引用含项目管理、治理、建模、生命周期、模式和架构方法文献。

适用条件：解释来源或组合方法。

逻辑关系：版本与年份是本地2025标准的引用快照；不可当“最新”版本。

决策方法：保持精确书目和实际引用单元，跨框架冲突显式登记。

制品及证据：参考书目与依赖映射；未读取外文献不得推其完整方法。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00604, C220-web-2025:01-introduction-and-core-concepts:b00605

<details><summary>展开本节完整英文来源</summary>

A.3. Other Referenced Documents

A Guide to the Project Management Body of Knowledge (PMBOK ® ) Guide), Project Management Institute; refer to: www.pmi.org/pmbok-guide-standards A Method for Identifying Process Re-Use Opportunities to Enhance the Operating Model, M. de Vries, A. van der Merwe, P. Kotze, A. Gerber, in proceedings of the 2011 IEEE International Conference on Industrial Engineering and Engineering Management (IEEM) Analysis Patterns — Reusable Object Models, M. Fowler, ISBN: 0-201-89542-0, Addison-Wesley ANSI/IEEE Std 1471-2000: Systems and Software Engineering — Recommended Practice for Architectural Description of Software-intensive Systems A Pattern Language: Towns, Buildings, Construction, Christopher Alexander, ISBN: 0-19-501919-9, Oxford University Press, 1979 Business Motivation Model™ (BMM™), Object Management Group (OMG); refer to: www.omg.org/spec/BMM/About-BMM Business Process Model and Notation™ (BPMN™) Specification, Object Management Group (OMG); refer to: www.bpmn.org Business Transformation Enablement Program (BTEP), Canadian Government; refer to: purl.org/theopengroup/btep Control Objectives for Information and related Technology (COBIT ® ), Version 4.0, IT Governance Institute, 2005 Corporate Governance, Ranami Naidoo, ISBN: 1-919-903-0086, Double Storey, 2002 Design Patterns: Elements of Reusable Object-Oriented Software, Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, ISBN: 0-201-63361-2, Addison-Wesley, October 1994 Enterprise Architecture as Strategy, Jeanne Ross, Peter Weill, David C. Robertson, ISBN: 1-59139-839-8, Harvard Business School Press, 2006 Enterprise Architecture Capability Maturity Model (ACMM), Version 1.2, United States Department of Commerce, December 2007 Enterprise Architecture Maturity Model, Version 1.3, National Association of State CIOs (NASCIO), December 2003 Enterprise Architecture Planning (EAP): Developing a Blueprint for Data, Applications, and Technology, Steven H. Spewak, Steven C. Hill, ISBN: 0-47-159985-9, John Wiley & Sons, 1993 Headquarters Air Force Principles for Information Management, US Air Force, June 29, 1998 ISO/IEC 20000:2011, Information Technology — Service Management ISO/IEC/IEEE 15288:2015, Systems and Software Engineering — System Life Cycle Processes ISO/IEC/IEEE 42010:2022, Systems and Software Engineering — Architecture Description IT Portfolio Management Facility™ (ITPMF™) Specification, Object Management Group (OMG); refer to: www.omg.org/spec/ITPMF Manifesto for Agile Software Development, 2001; refer to: www.agilemanifesto.org Merriam-Webster Collegiate Dictionary, Merriam-Webster, English
Language, 11th Edition, April 2008, ISBN-10: 0877798095, ISBN-13: 978-0877798095; refer to: www.merriam-webster.com Model-Driven Architecture ® (MDA ® ) Specification, Object Management (OMG); refer to: www.omg.org/mda OECD Principles of Corporate Governance, Organization for Economic Co-operation and Development, December 2001; refer to: www.oecd.org Organigraphs: Drawing How Companies Really Work, H. Mintzberg and L. Van der Heyden, Harvard Business Review, October 1999; refer to: hbr.org/1999/09/organigraphs-drawing-how-companies-really-work Pattern-Oriented Software Architecture: A System of Patterns, F. Buschmann, R. Meunier, H. Rohnert, P. Sommerlad, M. Stal, ISBN: 0-471-95869-7, John Wiley & Sons, 1996 Patterns and Software: Essential Concepts and Terminology, Brad Appleton, 2000; refer to: www.bradapp.com/docs/patterns-intro.html Re-usable Asset Specification (RAS), Version 2.2, Object Management Group (OMG), November 2005; refer to: www.omg.org/spec/RAS Service Component Architecture (SCA) Specification, developed by the Open Service Oriented Architecture (OSOA) collaboration; refer to: www.oasis-opencsa.org/sca Service Data Objects (SDO) Specification, developed by the Open Service Oriented Architecture (OSOA) collaboration; refer to: www.oasis-opencsa.org/sdo Software Processing Engineering Metamodel (SPEM™) Specification, Version 2.0, Object Management Group (OMG), April 2008; refer to: www.omg.org/spec/SPEM Systems Modeling Language™ (SysML ® ), Object Management Group (OMG); refer to: www.sysml.org The Art of Systems Architecting, Eberhardt Rechtin, Mark W. Maier, 2000 The Oregon Experiment, Christopher Alexander, ISBN: 0-19-501824-9, Oxford University Press, 1975 The Timeless Way of Building, Christopher Alexander, ISBN: 0-19-502402-8, Oxford University Press, 1979 The Zachman ® Framework, Zachman International; refer to: www.zachman.com UML Profile and Metamodel for Services (UPMS) RFP (OMG soa/2006-09-09), Object Management Group (OMG), June 2007 Unified Modeling Language™ (UML ® ) Specification, Object Management Group (OMG); refer to: www.uml.org

</details>

<a id="apdxb"></a>
## B: Glossary of Supplementary Definitions

概念：附录B补充第四章以外词义，覆盖系统、治理、配置、质量和项目组合等。

适用条件：术语不在核心定义时。

逻辑关系：补充定义不替代核心定义，引用回核心节时遵循其身份。

决策方法：按实际语境选择义项，记录与通常用词不同处。

制品及证据：补充词汇映射；未规定新的强制交付物。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00606, C220-web-2025:01-introduction-and-core-concepts:b00607

<details><summary>展开本节完整英文来源</summary>

B: Glossary of Supplementary Definitions

This appendix contains additional definitions to supplement the
definitions contained in Chapter 4, Definitions .

</details>

<a id="sec-06_01"></a>
## B.1. Application Software

概念：应用软件是具有特定业务目的的软件实体。

适用条件：术语用于应用软件的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：业务目的区别于通用基础软件。

决策方法：派生检查：软件条目连接其业务用途。

制品及证据：本节未要求新增独立交付物；派生检查可使用：软件与业务目的映射。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00608, C220-web-2025:01-introduction-and-core-concepts:b00609

<details><summary>展开本节完整英文来源</summary>

B.1. Application Software

Software entities which have a specific business purpose.

</details>

<a id="sec-06_02"></a>
## B.2. Availability

概念：可用性是系统功能任意时刻可用的概率，全部时间含操作、维修、管理及后勤。

适用条件：术语用于可用性的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：按系统类别及常规/优先操作细化，分母范围不可偷换。

决策方法：派生检查：明确时间分母、系统类别和测量窗口。

制品及证据：本节未要求新增独立交付物；派生检查可使用：可用性目标、观测时间和中断记录。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00610, C220-web-2025:01-introduction-and-core-concepts:b00611

<details><summary>展开本节完整英文来源</summary>

B.2. Availability

In the context of IT systems, the probability that system functional
capabilities are ready for use by a user at any time, where all time is
considered, including operations, repair, administration, and logistic
time. Availability is further defined by system category for both
routine and priority operations.

</details>

<a id="sec-06_03"></a>
## B.3. Business System

概念：业务系统由硬件软件政策流程活动标准人员共同实现业务能力。

适用条件：术语用于业务系统由硬件软件政策流程活动标准人员共同实现业务能力。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：信息系统只是其计算机部分。

决策方法：派生检查：变更影响覆盖人/政策/流程而非仅软件。

制品及证据：本节未要求新增独立交付物；派生检查可使用：业务系统组成与能力关系。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00612, C220-web-2025:01-introduction-and-core-concepts:b00613

<details><summary>展开本节完整英文来源</summary>

B.3. Business System

Hardware, software, policy statements, processes, activities, standards,
and people which together implement a business capability.

</details>

<a id="sec-06_04"></a>
## B.4. Catalog

概念：Catalog是同类架构输出的结构化参考列表。

适用条件：术语用于Catalog的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：目录是制品种类，不是元模型或自动批准标准。

决策方法：派生检查：类别、字段及来源一致。

制品及证据：本节未要求新增独立交付物；派生检查可使用：技术标准或应用目录及状态。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00614, C220-web-2025:01-introduction-and-core-concepts:b00615

<details><summary>展开本节完整英文来源</summary>

B.4. Catalog

A structured list of architectural outputs of a similar kind, used for
reference. For example, a technology standards catalog or an application
portfolio.

</details>

<a id="sec-06_05"></a>
## B.5. Client

概念：Client是向Server请求服务的应用组件。

适用条件：术语用于Client的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：客户端/服务端是交互角色，非必然终端硬件或人。

决策方法：派生检查：记录请求服务与对端。

制品及证据：本节未要求新增独立交付物；派生检查可使用：客户端组件、服务和交互。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00616, C220-web-2025:01-introduction-and-core-concepts:b00617

<details><summary>展开本节完整英文来源</summary>

B.5. Client

An application component which requests services from a server.

</details>

<a id="sec-06_06"></a>
## B.6. COBIT

概念：COBIT是IS/IT治理管理最佳实践集合，源列ISACA/ITGI。

适用条件：术语用于COBIT的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：与TOGAF架构治理互补，非完整同范围。

决策方法：派生检查：引用所用版本和控制来源。

制品及证据：本节未要求新增独立交付物；派生检查可使用：控制框架映射；本文未读取COBIT全文。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00618, C220-web-2025:01-introduction-and-core-concepts:b00619

<details><summary>展开本节完整英文来源</summary>

B.6. COBIT

An acronym for Control OBjectives for Information and related
Technology, created by the Information Systems Audit and Control
Association (ISACA) and the IT Governance Institute (ITGI), which
provides a set of recommended best practices for the
governance/management of information systems and technology.

</details>

<a id="sec-06_07"></a>
## B.7. Configuration Management

概念：配置管理识别记录配置项特征、控制变化并报告状态，也管理EA知识资产与基线。

适用条件：术语用于配置管理识别记录配置项特征、控制变化并报告状态，也管理EA知识资产与基线。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：配置控制涉及功能/物理与知识资产，不仅文件备份。

决策方法：派生检查：基线、变更权、版本和实施状态可追踪。

制品及证据：本节未要求新增独立交付物；派生检查可使用：配置项、基线、变更和状态日志。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00620, C220-web-2025:01-introduction-and-core-concepts:b00621, C220-web-2025:01-introduction-and-core-concepts:b00622, C220-web-2025:01-introduction-and-core-concepts:b00623

<details><summary>展开本节完整英文来源</summary>

B.7. Configuration Management

A discipline applying technical and administrative direction and
surveillance to:

Identify and document the functional and physical characteristics of a
configuration item Control changes to those characteristics Record and report changes to processing and implementation status

Also, the management of the configuration of Enterprise Architecture
practice (intellectual property) assets and baselines and the control of
change over of those assets.

</details>

<a id="sec-06_08"></a>
## B.8. CxO

概念：CxO指特定业务职能最高负责人，如CEO/CFO/CIO/CTO。

适用条件：术语用于CxO指特定业务职能最高负责人，如CEO/CFO/CIO/CTO。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：职务称谓不自动给所有架构决定权。

决策方法：派生检查：按组织授权界定负责人权限。

制品及证据：本节未要求新增独立交付物；派生检查可使用：职务及授权范围。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00624, C220-web-2025:01-introduction-and-core-concepts:b00625

<details><summary>展开本节完整英文来源</summary>

B.8. CxO

The chief officer within a particular function of the business; e.g.,
Chief Executive Officer, Chief Financial Officer, Chief Information
Officer, Chief Technology Officer.

</details>

<a id="sec-06_09"></a>
## B.9. Data Dictionary

概念：数据字典存储描述数据特征的元数据并支持定义管理。

适用条件：术语用于数据字典存储描述数据特征的元数据并支持定义管理。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：数据字典/应用系统与业务数据库不同。

决策方法：派生检查：字段含义与保护控制可追踪。

制品及证据：本节未要求新增独立交付物；派生检查可使用：元数据字典、所有者和变更。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00626, C220-web-2025:01-introduction-and-core-concepts:b00627

<details><summary>展开本节完整英文来源</summary>

B.9. Data Dictionary

A specialized type of database containing metadata; a repository of
information describing the characteristics of data used to design,
monitor, document, protect, and control data in information systems and
databases; an application system supporting the definition and
management of database metadata.

</details>

<a id="sec-06_10"></a>
## B.10. Data Element

概念：数据元素是有含义的基本信息单位，可有不同单位值的子类别。

适用条件：术语用于数据元素的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：元素语义与具体值和物理字段区分。

决策方法：派生检查：定义含义、单位和取值结构。

制品及证据：本节未要求新增独立交付物；派生检查可使用：数据元素定义与字段映射。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00628, C220-web-2025:01-introduction-and-core-concepts:b00629

<details><summary>展开本节完整英文来源</summary>

B.10. Data Element

A basic unit of information having a meaning and that may have
subcategories (data items) of distinct units and values.

</details>

<a id="sec-06_11"></a>
## B.11. Database

概念：数据库是供计算机访问的结构化数据实体集合。

适用条件：术语用于数据库的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：数据库与管理它的DBMS不同。

决策方法：派生检查：资产身份与数据实体关系明确。

制品及证据：本节未要求新增独立交付物；派生检查可使用：数据库资产、实体和访问。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00630, C220-web-2025:01-introduction-and-core-concepts:b00631

<details><summary>展开本节完整英文来源</summary>

B.11. Database

A structured or organized collection of data entities, which is to be
accessed by a computer.

</details>

<a id="sec-06_12"></a>
## B.12. Database Management System

概念：DBMS是访问或操作数据库的程序。

适用条件：术语用于DBMS的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：管理程序与数据库数据不同。

决策方法：派生检查：分开登记引擎产品和数据资产。

制品及证据：本节未要求新增独立交付物；派生检查可使用：DBMS配置及数据库依赖。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00632, C220-web-2025:01-introduction-and-core-concepts:b00633

<details><summary>展开本节完整英文来源</summary>

B.12. Database Management System

A computer application program that accesses or manipulates the
database.

</details>

<a id="sec-06_13"></a>
## B.13. End User

概念：End User最终使用应用或输出的人。

适用条件：术语用于End User最终使用应用或输出的人。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：终端使用者未必采购客户或批准者。

决策方法：派生检查：最终使用情境和关切有来源。

制品及证据：本节未要求新增独立交付物；派生检查可使用：用户、使用场景及需求。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00634, C220-web-2025:01-introduction-and-core-concepts:b00635

<details><summary>展开本节完整英文来源</summary>

B.13. End User

Person who ultimately uses the computer application or output.

</details>

<a id="sec-06_14"></a>
## B.14. Enterprise Resource Planning (ERP) System

概念：ERP是一套集成应用，支持财务、人事、库存、订单、采购等主要支持职能。

适用条件：术语用于ERP的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：ERP是应用组合，不等于全部业务系统。

决策方法：派生检查：按实际模块和接口确定能力覆盖。

制品及证据：本节未要求新增独立交付物；派生检查可使用：ERP模块、能力及数据关系。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00636, C220-web-2025:01-introduction-and-core-concepts:b00637

<details><summary>展开本节完整英文来源</summary>

B.14. Enterprise Resource Planning (ERP) System

A complete suite of integrated applications that support the major
business support functions of an organization; e.g., Financial
(AP/AR/GL), HR, Payroll, Stock, Order Processing and Invoicing,
Purchasing, Logistics, Manufacturing, etc.

</details>

<a id="sec-06_15"></a>
## B.15. Hardware

概念：硬件是运行软件的物理基础设施。

适用条件：术语用于硬件的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：物理基础设施与逻辑服务/云消费关系不同。

决策方法：派生检查：实际资产与责任边界明确。

制品及证据：本节未要求新增独立交付物；派生检查可使用：硬件资产、部署及运维责任。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00638, C220-web-2025:01-introduction-and-core-concepts:b00639

<details><summary>展开本节完整英文来源</summary>

B.15. Hardware

The physical infrastructure needed to run software; e.g., servers,
workstations, network equipment, etc.

</details>

<a id="sec-06_16"></a>
## B.16. Information Domain

概念：信息域按安全、所有权、位置等准则分组信息；安全域含用户、对象和政策。

适用条件：术语用于信息域按安全、所有权、位置等准则分组信息；安全域含用户、对象和政策。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：领域分组必须声明准则，不自动等于架构域。

决策方法：派生检查：域成员和政策/所有权边界清楚。

制品及证据：本节未要求新增独立交付物；派生检查可使用：信息域、对象、用户和政策。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00640, C220-web-2025:01-introduction-and-core-concepts:b00641

<details><summary>展开本节完整英文来源</summary>

B.16. Information Domain

Grouping of information (or data entities) by a set of criteria such as
security classification, ownership, location, etc. In the context of
security, information domains are defined as a set of users, their
information objects, and a security policy.

</details>

<a id="sec-06_17"></a>
## B.17. Information System (IS)

概念：IS是业务系统中计算机或IT部分。

适用条件：术语用于IS的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：IS不包含业务系统全部人、流程政策。

决策方法：派生检查：技术变化仍评估外部业务组成影响。

制品及证据：本节未要求新增独立交付物；派生检查可使用：IS范围及业务系统依赖。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00642, C220-web-2025:01-introduction-and-core-concepts:b00643

<details><summary>展开本节完整英文来源</summary>

B.17. Information System (IS)

The computer (or IT)-based portion of a business system.

</details>

<a id="sec-06_18"></a>
## B.18. Interaction

概念：Interaction是构建块间体现通信或使用的关系。

适用条件：术语用于Interaction的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：关系不是自动有方向/协议/多重性。

决策方法：派生检查：以实际行为界定通信/使用。

制品及证据：本节未要求新增独立交付物；派生检查可使用：交互端点、行为和契约。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00644, C220-web-2025:01-introduction-and-core-concepts:b00645

<details><summary>展开本节完整英文来源</summary>

B.18. Interaction

A relationship between architectural building blocks (i.e., services or
components) that embodies communication or usage.

</details>

<a id="sec-06_19"></a>
## B.19. Interaction Model

概念：交互模型用视图、目录或矩阵表示特定类型交互。

适用条件：术语用于交互模型用视图、目录或矩阵表示特定类型交互。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：表示种类可不同，底层语义须一致。

决策方法：派生检查：多视图同交互对象及属性一致。

制品及证据：本节未要求新增独立交付物；派生检查可使用：交互模型和关系追踪。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00646, C220-web-2025:01-introduction-and-core-concepts:b00647

<details><summary>展开本节完整英文来源</summary>

B.19. Interaction Model

An architectural view, catalog, or matrix that shows a particular type
of interaction. For example, a diagram showing application integration.

</details>

<a id="sec-06_20"></a>
## B.20. Interface

概念：Interface是人、系统、设备、应用或用户间连接与相互关系。

适用条件：术语用于Interface的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：接口不仅API，还需语义与交互行为。

决策方法：派生检查：参与方、数据/行为及契约明确。

制品及证据：本节未要求新增独立交付物；派生检查可使用：接口描述、对象及责任。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00648, C220-web-2025:01-introduction-and-core-concepts:b00649

<details><summary>展开本节完整英文来源</summary>

B.20. Interface

Interconnection and inter-relationships between, for example, people,
systems, devices, applications, or the user and an application or
device.

</details>

<a id="sec-06_21"></a>
## B.21. Key Performance Indicator (KPI)

概念：KPI量化业务或项目绩效。

适用条件：术语用于KPI量化业务或项目绩效。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：指标与目标值、实际观测不同。

决策方法：派生检查：量纲、时间窗、基值与来源明确。

制品及证据：本节未要求新增独立交付物；派生检查可使用：指标定义、目标和观测。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00650, C220-web-2025:01-introduction-and-core-concepts:b00651

<details><summary>展开本节完整英文来源</summary>

B.21. Key Performance Indicator (KPI)

A way of quantifying the performance of the business or project.

</details>

<a id="sec-06_22"></a>
## B.22. Lifecycle

概念：生命周期从系统构想到不再可用。

适用条件：术语用于生命周期从系统构想到不再可用。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：包含构思/退役而不只是开发。

决策方法：派生检查：覆盖运行和终止的风险/责任。

制品及证据：本节未要求新增独立交付物；派生检查可使用：生命周期状态和退役条件。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00652, C220-web-2025:01-introduction-and-core-concepts:b00653

<details><summary>展开本节完整英文来源</summary>

B.22. Lifecycle

The period of time that begins when a system is conceived and ends when
the system is no longer available for use.

</details>

<a id="sec-06_23"></a>
## B.23. Managing Successful Programs (MSP)

概念：MSP是源所述英国OGC项目群管理最佳实践。

适用条件：术语用于MSP的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：项目群方法与架构方法不同。

决策方法：派生检查：引用源版本并映射交付治理。

制品及证据：本节未要求新增独立交付物；派生检查可使用：方法与架构治理接口；无最新版本断言。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00654, C220-web-2025:01-introduction-and-core-concepts:b00655

<details><summary>展开本节完整英文来源</summary>

B.23. Managing Successful Programs (MSP)

A best practice methodology for program management, developed by the UK
Office of Government Commerce (OGC).

</details>

<a id="sec-06_24"></a>
## B.24. Matrix

概念：Matrix用网格表示两个或多个架构元素关系。

适用条件：术语用于Matrix用网格表示两个或多个架构元素关系。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：标记必须有语义，空白不能任意认不存在。

决策方法：派生检查：行列、图例及每单元格含义可追踪。

制品及证据：本节未要求新增独立交付物；派生检查可使用：矩阵对象、关系、图例及源坐标。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00656, C220-web-2025:01-introduction-and-core-concepts:b00657

<details><summary>展开本节完整英文来源</summary>

B.24. Matrix

A format for showing the relationship between two (or more)
architectural elements in a grid format.

</details>

<a id="sec-06_25"></a>
## B.25. Metaview

概念：Metaview是视图模式模板，确定目的受众、表达与分析用途。

适用条件：术语用于Metaview的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：本源连至Architecture Viewpoint，非具体视图。

决策方法：派生检查：模板规则和实例分开。

制品及证据：本节未要求新增独立交付物；派生检查可使用：视点目的、受众及模型规则。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00658, C220-web-2025:01-introduction-and-core-concepts:b00659, C220-web-2025:01-introduction-and-core-concepts:b00660

<details><summary>展开本节完整英文来源</summary>

B.25. Metaview

A pattern or template of the view, from which to develop individual
views. Establishes the purposes and audience for a view, the ways in
which the view is documented (e.g., for visual modeling), and the ways
in which it is used (e.g., for analysis).

See also Section 4.21, “Architecture Viewpoint” in Chapter 4, Definitions .

</details>

<a id="sec-06_26"></a>
## B.26. Open System

概念：开放系统采用足够开放的接口服务格式规格以支持移植、互操作与用户可迁移。

适用条件：术语用于开放系统采用足够开放的接口服务格式规格以支持移植、互操作与用户可迁移。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：开放是规范实现条件，不等于开源或无安全控制。

决策方法：派生检查：以接口规范和实际移植互操作证明。

制品及证据：本节未要求新增独立交付物；派生检查可使用：规范、移植/互操作/用户测试。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00661, C220-web-2025:01-introduction-and-core-concepts:b00662, C220-web-2025:01-introduction-and-core-concepts:b00663

<details><summary>展开本节完整英文来源</summary>

B.26. Open System

A system that implements sufficient open specifications for interfaces,
services, and supporting formats to enable properly engineered
application software:

To be ported with minimal changes across a wide range of systems To interoperate with other applications on local and remote systems To interact with users in a style that facilitates user portability

</details>

<a id="sec-06_27"></a>
## B.27. Operational Governance

概念：运营治理把系统绩效对照契约级别并保证有效运行。

适用条件：术语用于运营治理把系统绩效对照契约级别并保证有效运行。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：运营结果与设计合规分开验收。

决策方法：派生检查：目标级别及观测依据实际存在。

制品及证据：本节未要求新增独立交付物；派生检查可使用：SLA/OLA、运行观测和运营责任。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00664, C220-web-2025:01-introduction-and-core-concepts:b00665, C220-web-2025:01-introduction-and-core-concepts:b00666

<details><summary>展开本节完整英文来源</summary>

B.27. Operational Governance

The operational performance of systems against contracted performance
levels, the definition of operational performance levels, and the
implementation of systems that ensure effective operation of systems.

See also Section 4.49, “Governance” in Chapter 4, Definitions .

</details>

<a id="sec-06_28"></a>
## B.28. Packaged Services

概念：Packaged Services从COTS市场购买而非自行编程构建。

适用条件：术语用于Packaged Services从COTS市场购买而非自行编程构建。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：采购服务仍需契约与架构适配。

决策方法：派生检查：规格、约束和采用理由明确。

制品及证据：本节未要求新增独立交付物；派生检查可使用：采购服务、契约和需求覆盖。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00667, C220-web-2025:01-introduction-and-core-concepts:b00668

<details><summary>展开本节完整英文来源</summary>

B.28. Packaged Services

Services that are acquired from the market from a Commercial
Off-The-Shelf (COTS) vendor, rather than being constructed via code
build.

</details>

<a id="sec-06_29"></a>
## B.29. Portability

概念：可移植性表示跨软硬件环境迁移容易度，也可量化迁移/转换相对努力。

适用条件：术语用于可移植性表示跨软硬件环境迁移容易度，也可量化迁移/转换相对努力。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：可移植与扩容能力不同。

决策方法：派生检查：指定源/目标环境和迁移工作量。

制品及证据：本节未要求新增独立交付物；派生检查可使用：移植测试、改动与努力证据。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00669, C220-web-2025:01-introduction-and-core-concepts:b00670

<details><summary>展开本节完整英文来源</summary>

B.29. Portability

The ease with which a system, component, data, or user can be
transferred from one hardware or software environment to another A quality metric that can be used to measure the relative effort to
transport the software for use in another environment or to convert
software for use in another operating environment, hardware
configuration, or software system environment

</details>

<a id="sec-06_30"></a>
## B.30. Portfolio

概念：Portfolio为战略目标成组管理项目群、项目或运营。

适用条件：术语用于Portfolio为战略目标成组管理项目群、项目或运营。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：项目组合不等于单项目群，也含应用/技术/服务组合。

决策方法：派生检查：共享战略目标及组合决策依据明确。

制品及证据：本节未要求新增独立交付物；派生检查可使用：组合、战略和治理记录。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00671, C220-web-2025:01-introduction-and-core-concepts:b00672, C220-web-2025:01-introduction-and-core-concepts:b00673

<details><summary>展开本节完整英文来源</summary>

B.30. Portfolio

A collection of programs, projects, and/or operations managed as a group to achieve strategic objectives. For example, project portfolio,
application portfolio, technology portfolio, or service portfolio.

Note: Portfolio management is the act of managing portfolios.

</details>

<a id="sec-06_31"></a>
## B.31. PRINCE2

概念：PRINCE2是PRojects IN Controlled Environments的项目管理方法。

适用条件：术语用于PRINCE2的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：项目方法不是ADM的替代定义。

决策方法：派生检查：映射计划、授权和架构决策接口。

制品及证据：本节未要求新增独立交付物；派生检查可使用：方法集成与职责映射。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00674, C220-web-2025:01-introduction-and-core-concepts:b00675

<details><summary>展开本节完整英文来源</summary>

B.31. PRINCE2

An acronym for PRojects IN Controlled Environments, which is a standard
project management method.

</details>

<a id="sec-06_32"></a>
## B.32. Program

概念：Program是协调交付组织业务收益的变更项目集合。

适用条件：术语用于Program的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：协调收益区别于单项目或纯项目清单。

决策方法：派生检查：项目间依赖与共同收益清楚。

制品及证据：本节未要求新增独立交付物；派生检查可使用：项目群、依赖和收益。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00676, C220-web-2025:01-introduction-and-core-concepts:b00677

<details><summary>展开本节完整英文来源</summary>

B.32. Program

A co-ordinated set of change projects that deliver business benefit to
the organization.

</details>

<a id="sec-06_33"></a>
## B.33. Project

概念：Project是向组织交付业务收益的单个变更项目。

适用条件：术语用于Project的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：完成任务不自动证明收益实现。

决策方法：派生检查：明确项目边界和收益接受条件。

制品及证据：本节未要求新增独立交付物；派生检查可使用：项目范围、交付与收益证据。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00678, C220-web-2025:01-introduction-and-core-concepts:b00679

<details><summary>展开本节完整英文来源</summary>

B.33. Project

A single change project which delivers business benefit to the
organization.

</details>

<a id="sec-06_34"></a>
## B.34. Risk Management

概念：风险管理处理威胁EA实践成功、愿景目标与服务提供的风险/问题。

适用条件：术语用于风险管理处理威胁EA实践成功、愿景目标与服务提供的风险/问题。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：实践风险与单一方案风险有不同对象；源注卷名错引待保留。

决策方法：派生检查：识别实践服务风险与接受权限。

制品及证据：本节未要求新增独立交付物；派生检查可使用：实践风险登记、监控和治理。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00680, C220-web-2025:01-introduction-and-core-concepts:b00681, C220-web-2025:01-introduction-and-core-concepts:b00682

<details><summary>展开本节完整英文来源</summary>

B.34. Risk Management

The management of risks and issues that may threaten the success of the
Enterprise Architecture practice and its ability to meet its vision,
goals, and objectives, and, importantly, its service provision.

Note: Risk management is described in the TOGAF Standard — Architecture Content .

</details>

<a id="sec-06_35"></a>
## B.35. Scalability

概念：可扩展性既涉及不同平台范围，也指增长以适应工作量。

适用条件：术语用于可扩展性既涉及不同平台范围，也指增长以适应工作量。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：平台兼容与容量增长是不同义项。

决策方法：派生检查：注明使用义项及工作量/容量依据。

制品及证据：本节未要求新增独立交付物；派生检查可使用：平台覆盖、容量测试和负载。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00683, C220-web-2025:01-introduction-and-core-concepts:b00684

<details><summary>展开本节完整英文来源</summary>

B.35. Scalability

The ability to use the same application software on many different
classes of hardware/software platforms from PCs to super-computers
(extends the portability concept). The capability to grow to accommodate
increased work loads.

</details>

<a id="sec-06_36"></a>
## B.36. Security

概念：安全服务保护数据机密性、可用性和完整性。

适用条件：术语用于安全服务保护数据机密性、可用性和完整性。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：安全不能仅由加密或单个测试代表。

决策方法：派生检查：按三属性与威胁取证。

制品及证据：本节未要求新增独立交付物；派生检查可使用：安全需求、控制及有效性证据。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00685, C220-web-2025:01-introduction-and-core-concepts:b00686

<details><summary>展开本节完整英文来源</summary>

B.36. Security

Services which protect data, ensuring its confidentiality, availability,
and integrity.

</details>

<a id="sec-06_37"></a>
## B.37. Server

概念：Server是回应Client请求的应用组件。

适用条件：术语用于Server的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：服务器交互角色不必是物理设备。

决策方法：派生检查：记录服务行为与客户端关系。

制品及证据：本节未要求新增独立交付物；派生检查可使用：服务端组件、接口和请求响应。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00687, C220-web-2025:01-introduction-and-core-concepts:b00688

<details><summary>展开本节完整英文来源</summary>

B.37. Server

An application component which responds to requests from a client.

</details>

<a id="sec-06_38"></a>
## B.38. Service Quality

概念：服务质量是可赋予服务/契约的预设非功能属性配置。

适用条件：术语用于服务质量的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：质量目标配置与实际结果分开。

决策方法：派生检查：属性单位、阈值与验证办法明确。

制品及证据：本节未要求新增独立交付物；派生检查可使用：服务质量规格、契约和观测。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00689, C220-web-2025:01-introduction-and-core-concepts:b00690

<details><summary>展开本节完整英文来源</summary>

B.38. Service Quality

A preset configuration of non-functional attributes that may be assigned
to a service or service contract.

</details>

<a id="sec-06_39"></a>
## B.39. SMART

概念：SMART在本源展开为Specific/Measurable/Actionable/Realistic/Timebound。

适用条件：术语用于SMART在本源展开为Specific/Measurable/Actionable/Realistic/Timebound。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：Actionable不默改其他资料常见Achievable，目标需可达可测。

决策方法：派生检查：每个目标有时限、量纲和行动依据。

制品及证据：本节未要求新增独立交付物；派生检查可使用：目标质量与业务依据。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00691, C220-web-2025:01-introduction-and-core-concepts:b00692

<details><summary>展开本节完整英文来源</summary>

B.39. SMART

An acronym for Specific, Measurable, Actionable, Realistic, and
Timebound, which is an approach to ensure that targets and objectives
are set in a way that can be achieved and measured.

</details>

<a id="sec-06_40"></a>
## B.40. Supplier Management

概念：供应商管理协调EA实践产品服务供应者与企业采购活动。

适用条件：术语用于供应商管理协调EA实践产品服务供应者与企业采购活动。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：采购合同、架构责任与供应商能力不同。

决策方法：派生检查：供应商承诺与监督责任明确。

制品及证据：本节未要求新增独立交付物；派生检查可使用：供应商契约、能力和绩效。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00693, C220-web-2025:01-introduction-and-core-concepts:b00694

<details><summary>展开本节完整英文来源</summary>

B.40. Supplier Management

The management of suppliers of products and services to the Enterprise
Architecture practice in concert with larger corporate procurement
activities.

</details>

<a id="sec-06_41"></a>
## B.41. System

概念：System是为一个或多目的组织的相互作用元素组合。

适用条件：术语用于System的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：系统边界可包含非技术元素。

决策方法：派生检查：目的、元素和交互边界明确。

制品及证据：本节未要求新增独立交付物；派生检查可使用：系统边界、目标和依赖。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00695, C220-web-2025:01-introduction-and-core-concepts:b00696

<details><summary>展开本节完整英文来源</summary>

B.41. System

A combination of interacting elements organized to achieve one or more
stated purposes. (Source: ISO/IEC/IEEE 15288:2015)

</details>

<a id="sec-06_42"></a>
## B.42. Time Period

概念：Time Period是潜在影响的测量时间框。

适用条件：术语用于Time Period的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：时间窗不等于生命周期或任意历年。

决策方法：派生检查：不同指标比较使用一致范围。

制品及证据：本节未要求新增独立交付物；派生检查可使用：测量时间窗及影响数据。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00697, C220-web-2025:01-introduction-and-core-concepts:b00698

<details><summary>展开本节完整英文来源</summary>

B.42. Time Period

The timeframe over which the potential impact is to be measured.

</details>

<a id="sec-06_43"></a>
## B.43. Use Case

概念：Use Case从用户情境表述组织、应用或产品功能能力。

适用条件：术语用于Use Case从用户情境表述组织、应用或产品功能能力。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：用例与实际业务流程/需求定义不同。

决策方法：派生检查：用户、触发和结果与能力有关联。

制品及证据：本节未要求新增独立交付物；派生检查可使用：用例、用户和能力关系。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00699, C220-web-2025:01-introduction-and-core-concepts:b00700

<details><summary>展开本节完整英文来源</summary>

B.43. Use Case

A view of organization, application, or product functionality that
illustrates capabilities in context with the user of that capability.

</details>

<a id="sec-06_44"></a>
## B.44. User

概念：User可为使用处理系统服务的人组织功能单位，也可为发收命令消息的任何主体。

适用条件：术语用于User可为使用处理系统服务的人组织功能单位，也可为发收命令消息的任何主体。的身份、范围和跨文档解释；该节本身是定义，非操作流程。

逻辑关系：两义项不限定为自然人或客户。

决策方法：派生检查：按系统语境声明用户种类与权限。

制品及证据：本节未要求新增独立交付物；派生检查可使用：用户类别、服务交互和授权。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00701, C220-web-2025:01-introduction-and-core-concepts:b00702

<details><summary>展开本节完整英文来源</summary>

B.44. User

Any person, organization, or functional unit that uses the services of
an information processing system In a conceptual schema language, any person or any thing that may
issue or receive commands and messages to or from the information
system

</details>

<a id="apdxc"></a>
## C: Acronyms and Abbreviations

概念：缩略语是本卷快照索引，含ADM、MVA、SBB、SLA等，也有特定展开。

适用条件：消除简称歧义与旧译差异。

逻辑关系：本源API展开为Application Platform Interface，RAS为Remote Access Services；不能默改常见其他展开。

决策方法：引用保持源展开并标上下文歧义，不凭简称认资料或概念完全同一。

制品及证据：缩略语/上下文表和歧义记录；原文部分旧名称不证明当前机构名称。

适用边界：本文区分源文概念/条件与标“派生检查”的项目应用方法；不据此生成当前组织事实、授权、能力或业务批准。

来源块：C220-web-2025:01-introduction-and-core-concepts:b00703, C220-web-2025:01-introduction-and-core-concepts:b00704

<details><summary>展开本节完整英文来源</summary>

C: Acronyms and Abbreviations

ABB Architecture Building Block ACMM Architecture Capability Maturity Model ADM Architecture Development Method ANSI American National Standards Institute API Application Platform Interface ARTS Association for Retail Technology Standards BMM Business Motivation Model BPM Business Process Management BPMN Business Process Model and Notation BTEP The Canadian Government Business Transformation Enablement Program CMM Capability Maturity Models CMMI Capability Maturity Model Integration COBIT Control OBjectives for Information and related Technology COTS Commercial Off-The-Shelf applications CRM Customer Relationship Management CRUD Create/Read/Update/Delete CSF Critical Success Factor DBA Database Administrator DBMS Database Management System DoC US Department of Commerce DoD US Department of Defense DoDAF Department of Defense Architecture Framework EAI Enterprise Application Integration EDIFACT (United Nations) Electronic Data Interchange For Administration,
Commerce, and Transport ERP Enterprise Resource Planning ETL Extract, Transform, Load FICO Fair Isaac Corporation FTE Full-Time Equivalent GOTS Government Off-The-Shelf applications HIPAA Health Insurance Portability and Accountability Act ICAM Integrated Computer Aided Manufacturing ICOM Inputs, Controls, Outputs, and Mechanisms/Resources IDEF Integrated Computer Aided Manufacturing (ICAM) DEFinition IEC International Electrotechnical Commission IEEE Institute of Electrical and Electronic Engineers III-RM Integrated Information Infrastructure Reference Model IoT Internet of Things ISACA Information Systems Audit and Control Association ISACF Information Systems Audit and Control Foundation ISO International Standards Organization IT Information Technology ITGI IT Governance Institute ITIL Information Technology Infrastructure Library ITPMF IT Portfolio Management Facility J2EE Java 2 Platform, Enterprise Edition KPI Key Performance Indicator LAN Local Area Network MDA Model-Driven Architecture MSA Microservices Architecture MSP Managing Successful Programs MVA Minimum Viable Architecture NAF NATO Architecture Framework NASCIO National Association of State Chief Information Officers OECD Organization for Economic Co-operation and Development OGC UK Office of Government Commerce OLA Operational-Level Agreement OMB Office of Management and Budget OMG Object Management Group ORB Object Request Broker OSI Open Systems Interconnection OSOA Open Service-Oriented Architecture PDF Portable Document Format PMBOK Project Management Body of Knowledge PRINCE PRojects in Controlled Environments QoS Quality of Service RAS Remote Access Services RFC Request For Change RFI Request for Information RFP Request for Proposal RM Reference Model SBB Solution Building Block SCA Service Component Architecture SDO Service Data Objects SEI Software Engineering Institute SGML Standard Generalized Markup Language SLA Service-Level Agreement SMART Specific, Measurable, Actionable, Realistic, and Timebound SOA Service-Oriented Architecture SPEM Software Processing Engineering Metamodel SysML Systems Modeling Language TAFIM Technical Architecture Framework for Information Management TRM Technical Reference Model UML Unified Modeling Language WAN Wide Area Network XML Extensible Markup Language

</details>

