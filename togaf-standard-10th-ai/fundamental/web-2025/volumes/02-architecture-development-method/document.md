# TOGAF® Standard — Architecture Development Method

原文保存及结构转换；未完成逐章深度语义审阅。

[离线原貌](index.html) · [原始HTML](source.html) · [结构化正文](document.json)

The Open Group Standard

Copyright © 2005 - 2025, The Open Group All rights reserved.

No part of this publication may be reproduced, stored in a retrieval system, or transmitted, in any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior permission of the copyright owners. Specifically, without such written permission, the use or incorporation of this publication, in whole or in part, is NOT PERMITTED for the purposes of training or developing large language models (LLMs) or any other generative artificial intelligence systems, or otherwise for the purposes of using, or in connection with the use of, such technologies, tools, or models to generate any data or content and/or to synthesize or combine with any other data or content.

Any use of this publication for commercial purposes is subject to the terms of the Annual Commercial License relating to it. For further information, see www.opengroup.org/legal/licensing .

The Open Group Standard TOGAF® Standard — Architecture Development Method ISBN: 1-947754-90-4 Document Number: C220

Published by The Open Group, April 2022. Updated May 2025 to include Technical Corrigendum 1

Comments relating to the material contained in this document may be submitted to: The Open Group, Apex Plaza, Forbury Road, Reading, Berkshire, RG1 1AX, United Kingdom or by electronic mail to: ogspecs@opengroup.org

Built with asciidoctor , version 2.0.18.
Backend: html5
Build date: 2025-06-02 17:38:09 +0100

## Preface

### The Open Group

The Open Group is a global consortium that enables the achievement of business objectives through technology standards and open source initiatives by fostering a culture of collaboration, inclusivity, and mutual respect among our diverse group of 900+ memberships. Our membership includes customers, systems and solutions suppliers, tool vendors, integrators, academics, and consultants across multiple industries.

The mission of The Open Group is to drive the creation of Boundaryless Information Flow™ achieved by:

<ul>
<li>
<p>Working with customers to capture, understand, and address current and emerging requirements, establish policies, and share best practices</p>
</li>
<li>
<p>Working with suppliers, consortia, and standards bodies to develop consensus and facilitate interoperability, to evolve and integrate specifications and open source technologies</p>
</li>
<li>
<p>Offering a comprehensive set of services to enhance the operational efficiency of consortia</p>
</li>
<li>
<p>Developing and operating the industry’s premier certification service and encouraging procurement of certified products</p>
</li>
</ul>

Further information on The Open Group is available at www.opengroup.org .

The Open Group publishes a wide range of technical documentation, most of which is focused on development of standards and guides, but which also includes white papers, technical studies, certification and testing documentation, and business titles. Full details are available at www.opengroup.org/library .

### The TOGAF® Standard

The TOGAF ® Standard is an open, industry consensus framework for Enterprise Architecture.

It is a foundational framework, which means that it is applicable to the development of any kind of architecture in any context. This foundational framework is supplemented by The Open Group TOGAF Library, a publicly-accessible resource with an extensive and growing portfolio of guidance material, providing practical guidance in the application of the TOGAF framework in specific contexts; refer to: www.opengroup.org/togaf-library .

### The TOGAF Documentation

The TOGAF documentation consists of a set of documents:

<ul>
<li>
<p>The TOGAF Standard, which describes the generally applicable approach to Enterprise and IT Architecture</p>
</li>
<li>
<p>The TOGAF Library, a portfolio of additional guidance material, which supports the practical application of the TOGAF approach</p>
</li>
</ul>

### This Document

This document is the TOGAF® Standard — Architecture Development Method.

It has been developed and approved by The Open Group.

### Intended Audience

The TOGAF Standard is intended for Enterprise Architects, Business Architects, IT Architects, Data Architects, Systems Architects, Solution Architects, and anyone responsible for the architecture function within an organization.

## Trademarks

ArchiMate, FACE, FACE logo, Future Airborne Capability Environment, Making Standards Work, Open Footprint, Open O logo, Open O and Check certification logo, Open Subsurface Data Universe, OSDU, SOSA, SOSA logo, The Open Group, TOGAF, UNIX, UNIXWARE, and X logo are registered trademarks and Boundaryless Information Flow, Build with Integrity Buy with Confidence, Commercial Aviation Reference Architecture, Dependability Through Assuredness, Digital Practitioner Body of Knowledge, DPBoK, EMMM, FHIM Profile Builder, FHIM logo, FPB, IT4IT, IT4IT logo, O-AA, O-DA, O-DEF, O-HERA, O-PAS, O-TTPS, O-VBA, Open Agile Architecture, Open FAIR, Open Process Automation, Open Trusted Technology Provider, Sensor Integration Simplified, and Sensor Open Systems Architecture are trademarks of The Open Group.

COBIT is a registered trademark of the Information Systems Audit and Control Association (ISACA) and the IT Governance Institute.

ITIL and PRINCE2 are registered trademarks of AXELOS Limited.

MDA, Model-Driven Architecture, Object Management Group, OMG, and UML are registered trademarks and BPMN, Business Process Model and Notation, and Unified Modeling Language are trademarks of the Object Management Group.

Zachman is a registered trademark of Zachman International, Inc.

The Open Group acknowledges that there may be other company names and products that might be covered by trademark protection and advises the reader to verify them independently.

## Acknowledgements

The Open Group is grateful for the contribution of many individuals and organizations in the development of the TOGAF Standard. See the TOGAF Standard — Introduction and Core Concepts for details.

## Referenced Documents

Please refer to the TOGAF Standard — Introduction and Core Concepts, Appendix A for documents referenced in the TOGAF Standard.

## 1. Introduction

This chapter introduces the Architecture Development Method (ADM) cycle, adapting the ADM,
architecture scope, and architecture integration.

### 1.1. ADM Overview

The TOGAF ® ADM describes a method for developing and managing the lifecycle of an Enterprise Architecture, and forms the core of the TOGAF
Standard.

It integrates elements of the TOGAF Standard, as well as other available architectural assets, to meet the business needs of an organization.

#### 1.1.1. The ADM, Enterprise Continuum, and Architecture Repository

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

#### 1.1.2. The ADM and the Foundation Architecture

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

#### 1.1.3. ADM and Supporting Guidelines and Techniques

The application of the TOGAF ADM is supported by an extended set of
resources — guidelines, templates, checklists, and other detailed
materials. These are included in:

<ul>
<li>
<p>The <a href="https://pubs.opengroup.org/togaf-standard/adm-techniques/chap01.html">TOGAF Standard — ADM Techniques</a></p>
</li>
<li>
<p>TOGAF Series Guides — the Guidance part of the Standard (guidance
material on how to use and adapt the TOGAF Standard for specific needs)</p>
</li>
<li>
<p>White Papers and Guides published by The Open Group, classified and
referenced in the TOGAF Library (see
<a href="https://www.opengroup.org/togaf-library">www.opengroup.org/togaf-library</a>)</p>
</li>
</ul>

The individual guidelines and techniques are described separately so
that they can be referenced from the relevant points in the ADM as
necessary, rather than having the detailed text clutter the description
of the ADM itself.

### 1.2. Architecture Development Cycle

#### 1.2.1. Key Points

The following are the key points about the ADM:

<ul>
<li>
<p>The ADM is iterative, over the whole process, between phases, and
within phases (see the <a href="https://pubs.opengroup.org/togaf-standard/adm-techniques/chap01.html">TOGAF Standard — ADM Techniques</a>)</p>
</li>
<li>
<p>For each iteration of the ADM, a fresh decision must be taken as to:</p>
<div class="ulist">
<ul>
<li>
<p>The breadth of coverage of the enterprise to be defined</p>
</li>
<li>
<p>The level of detail to be defined</p>
</li>
<li>
<p>The extent of the time period aimed at, including the number and
extent of any intermediate time periods</p>
</li>
<li>
<p>The architectural assets to be leveraged, including:</p>
<div class="ulist">
<ul>
<li>
<p>Assets created in previous iterations of the ADM cycle within the
enterprise</p>
</li>
<li>
<p>Assets available elsewhere in the industry (other frameworks,
systems models, vertical industry models, etc.)</p>
</li>
</ul>
</div>
</li>
</ul>
</div>
</li>
<li>
<p>These decisions should be based on a practical assessment of resource
and competence availability, and the value that can realistically be
expected to accrue to the enterprise from the chosen scope of the
architecture work</p>
</li>
<li>
<p>As a generic method, the ADM is intended to be used by enterprises in
a wide variety of different geographies and applied in different
vertical sectors/industry types</p>
<div class="paragraph">
<p>As such, it may be, but does not necessarily have to be, tailored to
specific needs. For example, it may be used in conjunction with the set
of deliverables of another framework, where these have been deemed to be
more appropriate for a specific organization. (For example, many US
Federal agencies have developed individual frameworks that define the
deliverables specific to their particular departmental needs.)</p>
</div>
</li>
</ul>

These issues are considered in detail in Section 1.3, “Adapting the ADM” .

#### 1.2.2. Basic Structure

The basic structure of the ADM is shown in Figure 1-1, “Architecture Development Cycle” .

Throughout the ADM cycle, there needs to be frequent validation of
results against the original expectations, both those for the whole ADM
cycle, and those for the particular phase of the process.

![Architecture Development Cycle](assets/016-adm.png)

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

### 1.3. Adapting the ADM

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

<ul>
<li>
<p>The ADM is one of the many corporate processes that make up the
corporate governance model</p>
<div class="paragraph">
<p>It is complementary to, and supportive of, other standard program
management processes, such as those for authorization, risk management,
business planning and budgeting, development planning, systems
development, and procurement.</p>
</div>
</li>
<li>
<p>The ADM is being mandated for use by a prime or lead contractor in an
outsourcing situation, and needs to be tailored to achieve a suitable
compromise between the contractor’s existing practices and the
contracting enterprise’s requirements</p>
</li>
<li>
<p>The enterprise is a small-to-medium enterprise, and wishes to use a
“cut-down” method more attuned to the reduced level of resources and
system complexity typical of such an environment</p>
</li>
<li>
<p>The enterprise is very large and complex, comprising many separate but
interlinked “enterprises” within an overall collaborative business
framework, and the architecture method needs to be adapted to recognize
this</p>
</li>
<li>
<p>Different approaches to planning and integration may be used in such
cases, including the following (possibly in combination):</p>
<div class="ulist">
<ul>
<li>
<p>Top-down planning and development — designing the whole
interconnected meta-enterprise as a single entity (an exercise that
typically stretches the limits of practicality)</p>
</li>
<li>
<p>Development of a “generic” or “reference” architecture, typical of
the enterprises within the organization, but not representing any
specific enterprise, which individual enterprises are then expected to
adapt in order to produce an architecture “instance” suited to the
particular enterprise concerned</p>
</li>
<li>
<p>Replication — developing a specific architecture for one enterprise,
implementing it as a proof-of-concept, and then taking that as a
“reference architecture” to be cloned in other enterprises</p>
</li>
</ul>
</div>
</li>
<li>
<p>In a vendor or production environment, a generic architecture for a
family of related products is often referred to as a “Product Line
Architecture”, and the analogous process to that outlined above is
termed “(Architecture-based) Product Line Engineering”. The ADM is
targeted primarily at architects in IT user enterprises, but a vendor
organization whose products are IT-based might well wish to adapt it as
a generic method for a Product Line Architecture development.
</p>
</li>
</ul>

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

<ul>
<li>
<p><a href="https://pubs.opengroup.org/togaf-standard/enabling-enterprise-agility/index.html">TOGAF<sup>®</sup> Series Guide: Enabling Enterprise Agility</a></p>
</li>
<li>
<p><a href="https://pubs.opengroup.org/togaf-standard/agile-sprints/index.html">TOGAF<sup>®</sup> Series Guide: Applying the TOGAF<sup>®</sup> ADM using Agile Sprints</a></p>
</li>
</ul>

Additional guidance on adapting the ADM process may be found in the TOGAF Standard — Applying the ADM ,
and also in the TOGAF ® Series Guide: A Practitioners’ Approach to Developing Enterprise Architecture Following the TOGAF ® ADM .

### 1.4. Architecture Governance

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

<ul>
<li>
<p><strong>Reference Data</strong> (collateral from the organization’s own
repositories/Enterprise Continuum, including external data; e.g.,
COBIT<sup>®</sup>, the IT4IT Reference Architecture): used for guidance and
instruction during project implementation</p>
<div class="paragraph">
<p>This includes the details of information outlined above. The reference
data includes a description of the governance procedures themselves.</p>
</div>
</li>
<li>
<p><strong>Process Status</strong>: all information regarding the state of any
governance processes will be managed</p>
<div class="paragraph">
<p>Examples of this include outstanding compliance requests, dispensation
requests, and compliance assessments investigations.</p>
</div>
</li>
<li>
<p><strong>Audit Information</strong>: this will record all completed governance process
actions and will be used to support:</p>
<div class="ulist">
<ul>
<li>
<p>Key decisions and responsible personnel for any architecture project
that has been sanctioned by the governance process</p>
</li>
<li>
<p>A reference for future architectural and supporting process
developments, guidance, and precedence</p>
</li>
</ul>
</div>
</li>
</ul>

The governance artifacts and process are themselves part of the contents
of the Architecture Repository.

Architecture Governance is addressed in detail in the TOGAF Standard — EA Capability and Governance .

### 1.5. Scoping the Architecture

There are many reasons to constrain (or restrict) the scope of the
architectural activity to be undertaken, most of which relate to limits
in:

<ul>
<li>
<p>The organizational authority of the team producing the architecture</p>
</li>
<li>
<p>The objectives and stakeholder concerns to be addressed within the
architecture</p>
</li>
<li>
<p>The availability of people, finance, and other resources</p>
</li>
</ul>

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

<ul>
<li>
<p><strong>Breadth</strong>: what is the full extent of the enterprise, and what part of
that extent will this architecting effort deal with?</p>
<div class="ulist">
<ul>
<li>
<p>Many enterprises are very large, effectively comprising a federation
of organizational units that could validly be considered enterprises in
their own right</p>
</li>
<li>
<p>The modern enterprise increasingly extends beyond its traditional
boundaries, to embrace a fuzzy combination of traditional business
enterprise combined with suppliers, customers, and partners</p>
</li>
</ul>
</div>
</li>
<li>
<p><strong>Depth</strong>: to what level of detail should the architecting effort go?</p>
<div class="paragraph">
<p>How much architecture is “enough”? What is the appropriate demarcation
between the architecture effort and other, related activities (system
design, system engineering, system development)?</p>
</div>
</li>
<li>
<p><strong>Time Period</strong>: what is the time period that needs to be articulated
for the Architecture Vision, and does it make sense (in terms of
practicality and resources) for the same period to be covered in the
detailed Architecture Description?</p>
<div class="paragraph">
<p>If not, how many Transition Architectures are to be defined, and what
are their time periods?</p>
</div>
</li>
<li>
<p><strong>Architecture Domains</strong>:  a complete Enterprise Architecture Description
should contain all four architecture domains (Business, Data,
Application, Technology), but the realities of resource and time
constraints often mean there is not enough time, funding, or resources
to build a top-down, all-inclusive Architecture Description encompassing
all four architecture domains, even if the enterprise scope is chosen to
be less than the full extent of the overall enterprise</p>
</li>
</ul>

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

#### 1.5.1. Breadth

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

<ul>
<li>
<p>Architectural material is of good quality, up-to-date,
fit-for-purpose, and published (reviewed and agreed to be made public)</p>
</li>
<li>
<p>Usage of architecture material can be monitored, and compliance with
standards, models, and principles can be exhibited, via:</p>
<div class="ulist">
<ul>
<li>
<p>A Compliance Assessment process that describes what the user is
subscribing to, and assesses their level of compliance</p>
</li>
<li>
<p>A dispensation process that may grant dispensations from adherence to
architecture standards and guidelines in specific cases (usually with a
strong business imperative)</p>
</li>
</ul>
</div>
</li>
</ul>

Publish and subscribe techniques are being developed as part of general
IT governance and specifically for the Defense sphere.

#### 1.5.2. Depth

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

#### 1.5.3. Time Period

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

<ol class="arabic">
<li>
<p>First, develop Target Architecture Descriptions for the overall
(large-scale) system, demonstrating a response to stakeholder objectives
and concerns for a relatively distant timeframe (for example, a six-year
period)</p>
</li>
<li>
<p>Then develop one or more “Transition Architecture” descriptions, as
increments or plateaus, each in line with and converging on the Target
Architecture Descriptions, and describing the specifics of the increment
concerned</p>
</li>
</ol>

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

#### 1.5.4. Architecture Domains

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

### 1.6. Architecture Alternatives

There is often more than one possible Target Architecture that would
conform to the Architecture Vision, Architecture Principles, and
Requirements. It is important to identify alternative Target
Architectures and build understanding of different possibilities and
identify trade-offs between the alternatives. Creating an architecture
normally requires trade-offs among competing forces. Presenting
different alternatives and trade-offs to stakeholders helps architects
to extract hidden agendas, principles, and requirements that could
impact the final Target Architecture.

#### 1.6.1. Method

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

![Architecture Alternatives Method](assets/015-04_alternatives.png)

Figure 1-2. Architecture Alternatives Method

### 1.7. Architecture Integration

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

![Integration of Architecture Artifacts](assets/014-05_admintro2.png)

Figure 1-3. Integration of Architecture Artifacts

As organizations address common themes (such as Service-Oriented
Architecture (SOA), and integrated information infrastructure) and
universal data models and standard data structures emerge, integration
toward the high end of the spectrum will be facilitated. However, there
will always be the need for effective standards governance to reduce the
need for manual co-ordination and conflict resolution.

### 1.8. Summary

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

## 2. Preliminary Phase

This chapter describes the preparation and initiation activities
required to meet the business directive for a new Enterprise
Architecture, including the definition of an Organization-Specific
Architecture framework and the definition of principles.

![Preliminary Phase](assets/013-prelim.png)

Figure 2-1: Preliminary Phase

### 2.1. Objectives

The objectives of the Preliminary Phase are to:

<ol class="arabic">
<li>
<p>Determine the Architecture Capability desired by the organization:</p>
<div class="ulist">
<ul>
<li>
<p>Review the organizational context for conducting Enterprise
Architecture</p>
</li>
<li>
<p>Identify and scope the elements of the enterprise organizations
affected by the Architecture Capability</p>
</li>
<li>
<p>Identify the established frameworks, methods, and processes that
intersect with the Architecture Capability</p>
</li>
<li>
<p>Establish Capability Maturity target</p>
</li>
</ul>
</div>
</li>
<li>
<p>Establish the Architecture Capability:</p>
<div class="ulist">
<ul>
<li>
<p>Define and establish the Organizational Model for Enterprise
Architecture</p>
</li>
<li>
<p>Define and establish the detailed process and resources for
Architecture Governance</p>
</li>
<li>
<p>Select and implement tools that support the Architecture Capability</p>
</li>
<li>
<p>Define the Architecture Principles</p>
</li>
</ul>
</div>
</li>
</ol>

### 2.2. Inputs

This section defines the inputs to the Preliminary Phase.

#### 2.2.1. Reference Materials External to the Enterprise

<ul>
<li>
<p>The TOGAF Library</p>
</li>
<li>
<p>Other architecture framework(s), if required</p>
</li>
</ul>

#### 2.2.2. Non-Architectural Inputs

<ul>
<li>
<p>Board strategies and board business plans, business strategy, IT
strategy, business principles, business goals, and business drivers,
when pre-existing</p>
</li>
<li>
<p>Major frameworks operating in the business; e.g., project/portfolio
management</p>
</li>
<li>
<p>Governance and legal frameworks, including Architecture Governance
strategy, when pre-existing</p>
</li>
<li>
<p>Architecture capability</p>
</li>
<li>
<p>Partnership and contract agreements</p>
</li>
</ul>

#### 2.2.3. Architectural Inputs

Pre-existing models for operating an Enterprise Architecture Capability
can be used as a baseline for the Preliminary Phase. Inputs would
include:

<ul>
<li>
<p>Organizational Model for Enterprise Architecture (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Scope of organizations impacted</p>
</li>
<li>
<p>Maturity assessment, gaps, and resolution approach</p>
</li>
<li>
<p>Roles and responsibilities for architecture team(s)</p>
</li>
<li>
<p>Budget requirements</p>
</li>
<li>
<p>Governance and support strategy</p>
</li>
</ul>
</div>
</li>
<li>
<p>Existing Architecture Framework, if any, including:</p>
<div class="ulist">
<ul>
<li>
<p>Architecture method</p>
</li>
<li>
<p>Architecture content</p>
</li>
<li>
<p>Configured and deployed tools</p>
</li>
<li>
<p>Architecture Principles</p>
</li>
<li>
<p>Architecture Repository</p>
</li>
</ul>
</div>
</li>
</ul>

### 2.3. Steps

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

<ul>
<li>
<p>Scope the enterprise organizations impacted; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_02_03_01">Section 2.3.1, “Scope the Enterprise Organizations Impacted”</a></p>
</li>
<li>
<p>Confirm governance and support frameworks; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_02_03_02">Section 2.3.2, “Confirm Governance and Support Frameworks”</a></p>
</li>
<li>
<p>Define and establish Enterprise Architecture team and organization; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_02_03_03">Section 2.3.3, “Define and Establish Enterprise Architecture Team and Organization”</a></p>
</li>
<li>
<p>Identify and establish Architecture Principles; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_02_03_04">Section 2.3.4, “Identify and Establish Architecture Principles”</a></p>
</li>
<li>
<p>Tailor the TOGAF framework and, if any, other selected architecture frameworks; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_02_03_05">Section 2.3.5, “Tailor the TOGAF Framework and, if any, Other Selected Architecture Framework(s)”</a></p>
</li>
<li>
<p>Develop a strategy and implementation plan for tools and techniques; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_02_03_06">Section 2.3.6, “Develop a Strategy and Implementation Plan for Tools and Techniques”</a></p>
</li>
</ul>

#### 2.3.1. Scope the Enterprise Organizations Impacted

<ul>
<li>
<p>Identify core enterprise (units) — those who are most affected and
achieve most value from the work</p>
</li>
<li>
<p>Identify soft enterprise (units) — those who will see change to their
capability and work with core units but are otherwise not directly
affected</p>
</li>
<li>
<p>Identify extended enterprise (units) — those units outside the scoped
enterprise who will be affected in their own Enterprise Architecture</p>
</li>
<li>
<p>Identify communities involved (enterprises) — those stakeholders who
will be affected and who are in groups of communities</p>
</li>
<li>
<p>Identify governance involved, including legal frameworks and
geographies (enterprises)</p>
</li>
</ul>

#### 2.3.2. Confirm Governance and Support Frameworks

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

#### 2.3.3. Define and Establish Enterprise Architecture Team and Organization

<ul>
<li>
<p>Determine existing enterprise and business capability</p>
</li>
<li>
<p>Conduct an Enterprise Architecture/business change maturity
assessment, if required</p>
</li>
<li>
<p>Identify gaps in existing work areas</p>
</li>
<li>
<p>Allocate key roles and responsibilities for Enterprise Architecture
Capability management and governance<br/></p>
</li>
<li>
<p>Define requests for change to existing business programs and projects:</p>
<div class="ulist">
<ul>
<li>
<p>Inform existing Enterprise Architecture and IT architecture work of
stakeholder requirements</p>
</li>
<li>
<p>Request assessment of impact on their plans and work</p>
</li>
<li>
<p>Identify common areas of interest</p>
</li>
<li>
<p>Identify any critical differences and conflicts of interest</p>
</li>
<li>
<p>Produce requests for change to stakeholder activities</p>
</li>
</ul>
</div>
</li>
<li>
<p>Determine constraints on Enterprise Architecture work</p>
</li>
<li>
<p>Review and agree with sponsors and board</p>
</li>
<li>
<p>Assess budget requirements</p>
</li>
</ul>

#### 2.3.4. Identify and Establish Architecture Principles

Architecture Principles (see the TOGAF Standard — ADM Techniques ) are based on business principles and are
critical in setting the foundation for Architecture Governance. Once the
organizational context is understood, define a set of Architecture
Principles that is appropriate to the enterprise.

#### 2.3.5. Tailor the TOGAF Framework and, if any, Other Selected Architecture Framework(s)

In this step, determine what tailoring of the TOGAF framework is
required. Consider the need for:

<ul>
<li>
<p><strong>Terminology Tailoring</strong>: architecture practitioners should use
terminology that is generally understood across the enterprise</p>
<div class="paragraph">
<p>Tailoring should produce an agreed terminology set for description of
architectural content. Consideration should be given to the creation of
an Enterprise Glossary, to be updated throughout the architecture
process.</p>
</div>
</li>
<li>
<p><strong>Process Tailoring</strong>: the TOGAF ADM provides a generic process for
carrying out architecture</p>
<div class="paragraph">
<p>Process tailoring provides the opportunity to remove tasks that are
already carried out elsewhere in the organization, add
organization-specific tasks (such as specific checkpoints), and to align
the ADM processes to external process frameworks and touch-points. Key
touch-points to be addressed would include:</p>
</div>
<div class="ulist">
<ul>
<li>
<p>Links to (project and service) portfolio management processes</p>
</li>
<li>
<p>Links to project lifecycle</p>
</li>
<li>
<p>Links to operations handover processes</p>
</li>
<li>
<p>Links to operational management processes (including configuration
management, change management, and service management)</p>
</li>
<li>
<p>Links to procurement processes</p>
</li>
</ul>
</div>
</li>
<li>
<p><strong>Content Tailoring</strong>: using the TOGAF Architecture Content Framework
and Enterprise Continuum as a basis, tailoring of content structure and
classification approach allows adoption of third-party content
frameworks and also allows for customization of the framework to support
organization-specific requirements</p>
</li>
</ul>

#### 2.3.6. Develop a Strategy and Implementation Plan for Tools and Techniques

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

##### 2.3.6.1. Issues in Tools Standardization

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

### 2.4. Outputs

The outputs of the Preliminary Phase may include, but are not restricted
to:

<ul>
<li>
<p>Organizational Model for Enterprise Architecture (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Scope of organizations impacted</p>
</li>
<li>
<p>Maturity assessment, gaps, and resolution approach</p>
</li>
<li>
<p>Roles and responsibilities for architecture team(s)</p>
</li>
<li>
<p>Constraints on architecture work</p>
</li>
<li>
<p>Budget requirements</p>
</li>
<li>
<p>Governance and support strategy</p>
</li>
</ul>
</div>
</li>
<li>
<p>Tailored Architecture Framework (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Tailored architecture method</p>
</li>
<li>
<p>Tailored architecture content (deliverables and artifacts)</p>
</li>
<li>
<p>Architecture Principles (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Configured and deployed tools</p>
</li>
</ul>
</div>
</li>
<li>
<p>Initial Architecture Repository (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), populated with framework content</p>
</li>
<li>
<p>Restatement of, or reference to, business principles, business goals,
and business drivers (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Request for Architecture Work (optional) (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Architecture Governance Framework (see the
<a href="https://pubs.opengroup.org/togaf-standard/ea-capability-and-governance/chap01.html">TOGAF Standard — EA Capability and Governance</a>)</p>
</li>
<li>
<p>The Architecture of the Enterprise Architecture Capability (see the
<a href="https://pubs.opengroup.org/togaf-standard/ea-capability-and-governance/chap01.html">TOGAF Standard — EA Capability and Governance</a>)</p>
</li>
</ul>

The outputs may include some or all of the following:

<ul>
<li>
<p>Catalogs:</p>
<div class="ulist">
<ul>
<li>
<p>Principles catalog</p>
</li>
</ul>
</div>
</li>
</ul>

### 2.5. Approach

This Preliminary Phase is about defining “where, what, why, who, and how
we do architecture” in the enterprise concerned. The main aspects are as
follows:

<ul>
<li>
<p>Defining the enterprise</p>
</li>
<li>
<p>Identifying key drivers and elements in the organizational context</p>
</li>
<li>
<p>Defining the requirements for architecture work</p>
</li>
<li>
<p>Defining the Architecture Principles that will inform any architecture
work</p>
</li>
<li>
<p>Defining the framework to be used</p>
</li>
<li>
<p>Defining the relationships between management frameworks</p>
</li>
<li>
<p>Evaluating the Enterprise Architecture maturity</p>
</li>
</ul>

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

#### 2.5.1. Enterprise

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

#### 2.5.2. Organizational Context

In order to make effective and informed decisions about the framework
for architecture to be used within a particular enterprise, it is
necessary to understand the context surrounding the architecture
framework. Specific areas to consider would include:

<ul>
<li>
<p>The commercial models for Enterprise Architecture and budgetary plans
for Enterprise Architecture activity; where no such plans exist, the
Preliminary Phase should be used to develop a budget plan</p>
</li>
<li>
<p>The stakeholders for architecture in the enterprise; their key issues
and concerns</p>
</li>
<li>
<p>The intentions and culture of the organization, as captured within
board business directives, business imperatives, business strategies,
business principles, business goals, and business drivers</p>
</li>
<li>
<p>Current processes that support execution of change and operation of
the enterprise, including the structure of the process and also the
level of rigor and formality applied within the organization</p>
<div class="paragraph">
<p>Areas for focus should include:</p>
</div>
<div class="ulist">
<ul>
<li>
<p>Current methods for architecture description</p>
</li>
<li>
<p>Current project management frameworks and methods</p>
</li>
<li>
<p>Current systems management frameworks and methods</p>
</li>
<li>
<p>Current project portfolio management processes and methods</p>
</li>
<li>
<p>Current application portfolio management processes and methods</p>
</li>
<li>
<p>Current technology portfolio management processes and methods</p>
</li>
<li>
<p>Current information portfolio management processes and methods</p>
</li>
<li>
<p>Current systems design and development frameworks and methods</p>
</li>
</ul>
</div>
</li>
<li>
<p>The Baseline Architecture landscape, including the state of the
enterprise and also how the landscape is currently represented in
documentation form</p>
</li>
<li>
<p>The skills and capabilities of the enterprise and specific
organizations that will be adopting the framework</p>
</li>
</ul>

Review of the organizational context should provide valuable
requirements on how to tailor the architecture framework in terms of:

<ul>
<li>
<p>Level of formality and rigor to be applied</p>
</li>
<li>
<p>Level of sophistication and expenditure required</p>
</li>
<li>
<p>Touch-points with other organizations, processes, roles, and
responsibilities</p>
</li>
<li>
<p>Focus of content coverage</p>
</li>
</ul>

#### 2.5.3. Requirements for Architecture Work

The business imperatives behind the Enterprise Architecture work drive
the requirements and performance metrics for the architecture work. They
should be sufficiently clear so that this phase may scope the business
outcomes and resource requirements, and define the outline enterprise
business information requirements and associated strategies of the
Enterprise Architecture work to be done. For example, these may include:

<ul>
<li>
<p>Business requirements</p>
</li>
<li>
<p>Cultural aspirations</p>
</li>
<li>
<p>Organization intents</p>
</li>
<li>
<p>Strategic intent</p>
</li>
<li>
<p>Forecast financial requirements</p>
</li>
</ul>

Significant elements of these need to be articulated so that the sponsor
can identify all the key decision-makers and stakeholders involved in
defining and establishing an Architecture Capability.

#### 2.5.4. Principles

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

#### 2.5.5. Management Frameworks

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

<ul>
<li>
<p><strong>Business Capability Management</strong> that determines what business
capabilities are required to deliver business value including the
definition of return on investment and the requisite control/performance
measures</p>
</li>
<li>
<p><strong>Project/Portfolio Management Methods</strong> that determine how a company
manages its change initiatives</p>
</li>
<li>
<p><strong>Operations Management Methods</strong> that describe how a company runs its
day-to-day operations, including IT</p>
</li>
<li>
<p><strong>Solution Development Methods</strong> that formalize the way that business
systems are delivered in accordance with the structures developed in the
IT architecture</p>
</li>
</ul>

As illustrated in Figure 2-2 , these frameworks are not
discrete and there are significant overlaps between them and the
Business Capability Management. The latter includes the delivery of
performance measured business value.

The overall significance is that the Enterprise Architect applying the
TOGAF framework cannot narrowly focus on the IT implementation, but must
be aware of the impact that the architecture has on the entire
enterprise.

![Management Frameworks to Co-ordinate with the TOGAF Framework](assets/012-06_mgmtfwks.png)

Figure 2-2: Management Frameworks to Co-ordinate with the TOGAF Framework

The Preliminary Phase therefore involves doing any necessary work to
adapt the ADM to define an organization-specific framework, using either
the TOGAF deliverables or the deliverables of another framework. The
issues involved in this are discussed in Section 1.3, “Adapting the ADM” .

#### 2.5.6. Relating the Management Frameworks

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

![Interoperability and Relationships between Management Frameworks](assets/011-06_mgmtfwks_interop.png)

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

#### 2.5.7. Planning for Enterprise Architecture/Business Change Maturity Evaluation

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

## 3. Phase A: Architecture Vision

This chapter describes the initial phase of the ADM. It includes
information about defining the scope, identifying the stakeholders,
creating the Architecture Vision, and obtaining approvals.

![Phase A: Architecture Vision](assets/010-a_vis.png)

Figure 3-1: Phase A: Architecture Vision

### 3.1. Objectives

The objectives of Phase A are to:

<ul>
<li>
<p>Develop a high-level aspirational vision of the capabilities and
business value to be delivered as a result of the proposed Enterprise
Architecture</p>
</li>
<li>
<p>Obtain approval for a Statement of Architecture Work that defines a
program of works to develop and deploy the architecture outlined in the
Architecture Vision</p>
</li>
</ul>

### 3.2. Inputs

This section defines the inputs to Phase A.

#### 3.2.1. Reference Materials External to the Enterprise

<ul>
<li>
<p>Architecture reference materials (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
</ul>

#### 3.2.2. Non-Architectural Inputs

<ul>
<li>
<p>Request for Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Business principles, business goals, and business drivers (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
</ul>

#### 3.2.3. Architectural Inputs

<ul>
<li>
<p>Organizational Model for Enterprise Architecture (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>),
including:</p>
<div class="ulist">
<ul>
<li>
<p>Scope of organizations impacted</p>
</li>
<li>
<p>Maturity assessment, gaps, and resolution approach</p>
</li>
<li>
<p>Roles and responsibilities for architecture team(s)</p>
</li>
<li>
<p>Constraints on architecture work</p>
</li>
<li>
<p>Re-use requirements</p>
</li>
<li>
<p>Budget requirements</p>
</li>
<li>
<p>Requests for change</p>
</li>
<li>
<p>Governance and support strategy</p>
</li>
</ul>
</div>
</li>
<li>
<p>Tailored Architecture Framework (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Tailored architecture method</p>
</li>
<li>
<p>Tailored architecture content (deliverables and artifacts)</p>
</li>
<li>
<p>Architecture Principles (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including business principles, when pre-existing</p>
</li>
<li>
<p>Configured and deployed tools</p>
</li>
</ul>
</div>
</li>
<li>
<p>Populated Architecture Repository (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>) — existing architectural documentation (framework description,
architectural descriptions, baseline descriptions, Architecture Building
Blocks (ABBs), etc.)</p>
</li>
</ul>

### 3.3. Steps

The level of detail addressed in Phase A will depend on the scope and
goals of the Request for Architecture Work, or the subset of scope and
goals associated with this iteration of architecture development.

The order of the steps in Phase A as well as the time at which they are
formally started and completed should be adapted to the situation at
hand in accordance with the established Architecture Governance.

The steps in Phase A are as follows:

<ul>
<li>
<p>Establish the architecture project; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_03_03_01">Section 3.3.1, “Establish the Architecture Project”</a></p>
</li>
<li>
<p>Identify stakeholders, concerns, and business requirements; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_03_03_02">Section 3.3.2, “Identify Stakeholders, Concerns, and Business Requirements”</a></p>
</li>
<li>
<p>Confirm and elaborate business goals, business drivers, and constraints; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_03_03_03">Section 3.3.3, “Confirm and Elaborate Business Goals, Business Drivers, and Constraints”</a></p>
</li>
<li>
<p>Evaluate capabilities; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_03_03_04">Section 3.3.4, “Evaluate Capabilities”</a></p>
</li>
<li>
<p>Assess readiness for business transformation; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_03_03_05">Section 3.3.5, “Assess Readiness for Business Transformation”</a></p>
</li>
<li>
<p>Define scope; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_03_03_06">Section 3.3.6, “Define Scope”</a></p>
</li>
<li>
<p>Confirm and elaborate Architecture Principles, including business principles; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_03_03_07">Section 3.3.7, “Confirm and Elaborate Architecture Principles, including Business Principles”</a></p>
</li>
<li>
<p>Develop Architecture Vision; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_03_03_08">Section 3.3.8, “Develop Architecture Vision”</a></p>
</li>
<li>
<p>Define the Target Architecture value propositions and KPIs; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_03_03_09">Section 3.3.9, “Define the Target Architecture Value Propositions and KPIs”</a></p>
</li>
<li>
<p>Identify the business transformation risks and mitigation activities; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_03_03_10">Section 3.3.10, “Identify the Business Transformation Risks and Mitigation Activities”</a></p>
</li>
<li>
<p>Develop Statement of Architecture Work; secure approval; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_03_03_11">Section 3.3.11, “Develop Statement of Architecture Work; Secure Approval”</a></p>
</li>
</ul>

#### 3.3.1. Establish the Architecture Project

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

#### 3.3.2. Identify Stakeholders, Concerns, and Business Requirements

Identify the key stakeholders and their concerns/objectives, and define
the key business requirements to be addressed in the architecture
engagement. Stakeholder engagement at this stage is intended to
accomplish three objectives:

<ul>
<li>
<p>To identify candidate vision components and requirements to be tested
as the Architecture Vision is developed</p>
</li>
<li>
<p>To identify candidate scope boundaries for the engagement to limit the
extent of architectural investigation required</p>
</li>
<li>
<p>To identify stakeholder concerns, issues, and cultural factors that
will shape how the architecture is presented and communicated</p>
</li>
</ul>

The major product resulting from this step is a stakeholder map for the
engagement, showing which stakeholders are involved with the engagement,
their level of involvement, and their key concerns (see the TOGAF Standard — ADM Techniques ). The
stakeholder map is used to support various outputs of the Architecture
Vision phase, and to identify:

<ul>
<li>
<p>The concerns and viewpoints that are relevant to this project; this is
captured in the Architecture Vision (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>The stakeholders that are involved with the project and as a result
form the starting point for a Communications Plan (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>The key roles and responsibilities within the project, which should be
included within the Statement of Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
</ul>

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

#### 3.3.3. Confirm and Elaborate Business Goals, Business Drivers, and Constraints

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

#### 3.3.4. Evaluate Capabilities

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

#### 3.3.5. Assess Readiness for Business Transformation

A Business Transformation Readiness Assessment can be used to evaluate
and quantify the organization’s readiness to undergo a change. This
assessment is based upon the determination and analysis/rating of a
series of readiness factors, as described in the TOGAF Standard — ADM Techniques .

The results of the readiness assessment should be added to the
Capability Assessment (see the TOGAF Standard — Architecture Content ). These results are then used to shape the scope of the
architecture, to identify activities required within the architecture
project, and to identify risk areas to be addressed.

#### 3.3.6. Define Scope

Define what is inside and what is outside the scope of the Baseline
Architecture and Target Architecture efforts, understanding that the
baseline and target need not be described at the same level of detail.
In many cases, the baseline is described at a higher level of
abstraction, so more time is available to specify the target in
sufficient detail. The issues involved in this are discussed in Section 1.5, “Scoping the Architecture” .
In particular, define:

<ul>
<li>
<p>The breadth of coverage of the enterprise</p>
</li>
<li>
<p>The level of detail required</p>
</li>
<li>
<p>The partitioning characteristics of the architecture (see the
<a href="https://pubs.opengroup.org/togaf-standard/applying-the-adm/chap01.html">TOGAF Standard — Applying the ADM</a>
for more details)</p>
</li>
<li>
<p>The specific architecture domains to be covered (Business, Data,
Application, Technology)</p>
</li>
<li>
<p>The extent of the time period aimed at, plus the number and extent of
any intermediate time period</p>
</li>
<li>
<p>The architectural assets to be leveraged, or considered for use, from
the organization’s Architecture Repository:</p>
<div class="ulist">
<ul>
<li>
<p>Assets created in previous iterations of the ADM cycle within the
enterprise</p>
</li>
<li>
<p>Assets available elsewhere in the industry (other frameworks, systems
models, vertical industry models, etc.)</p>
</li>
</ul>
</div>
</li>
</ul>

#### 3.3.7. Confirm and Elaborate Architecture Principles, including Business Principles

Review the principles under which the architecture is to be developed.
Architecture Principles are normally based on the principles developed
as part of the Preliminary Phase. They are explained, and an example set
given, in the TOGAF Standard — ADM Techniques . Ensure that the existing definitions are current, and
clarify any areas of ambiguity. Otherwise, go back to the body
responsible for Architecture Governance and work with them to define
these essential items for the first time and secure their endorsement by
corporate management.

#### 3.3.8. Develop Architecture Vision

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

#### 3.3.9. Define the Target Architecture Value Propositions and KPIs

<ul>
<li>
<p>Develop the business case for the architectures and changes required</p>
</li>
<li>
<p>Produce the value proposition for each of the stakeholder groupings</p>
</li>
<li>
<p>Assess and define the procurement requirements</p>
</li>
<li>
<p>Review and agree the value propositions with the sponsors and stakeholders concerned</p>
</li>
<li>
<p>Define the performance metrics and measures to be built into the
Enterprise Architecture to meet the business needs</p>
</li>
<li>
<p>Assess the business risk (see the
<a href="https://pubs.opengroup.org/togaf-standard/adm-techniques/chap01.html">TOGAF Standard — ADM Techniques</a>)</p>
</li>
</ul>

The outputs from this activity should be incorporated within the
Statement of Architecture Work to allow performance to be tracked
accordingly.

#### 3.3.10. Identify the Business Transformation Risks and Mitigation Activities

Identify the risks associated with the Architecture Vision and assess
the initial level of risk (e.g., catastrophic, critical, marginal, or
negligible) and the potential frequency associated with it. Assign a
mitigation strategy for each risk. A risk management framework is
described in the TOGAF Standard — ADM Techniques .

There are two levels of risk that should be considered, namely:

<ul>
<li>
<p><strong>Initial Level of Risk</strong>: risk categorization prior to determining and
implementing mitigating actions</p>
</li>
<li>
<p><strong>Residual Level of Risk</strong>: risk categorization after implementation of
mitigating actions (if any)</p>
</li>
</ul>

Risk mitigation activities should be considered for inclusion within the
Statement of Architecture Work.

#### 3.3.11. Develop Statement of Architecture Work; Secure Approval

Assess the work products that are required to be produced (and by when)
against the set of business performance requirements. This will involve
ensuring that:

<ul>
<li>
<p>Performance metrics are built into the work products</p>
</li>
<li>
<p>Specific performance-related work products are available</p>
</li>
</ul>

Then, activities will include:

<ul>
<li>
<p>Identify new work products that will need to be changed</p>
</li>
<li>
<p>Provide direction on which existing work products, including building
blocks, will need to be changed and ensure that all activities and
dependencies on these are co-ordinated</p>
</li>
<li>
<p>Identify the impact of change on other work products and dependence on
their activities</p>
</li>
<li>
<p>Based on the purpose, focus, scope, and constraints, determine which
architecture domains should be developed, to what level of detail, and
which architecture views should be built</p>
</li>
<li>
<p>Assess the resource requirements and availability to perform the work
in the timescale required; this will include adhering to the
organization’s planning methods and work products to produce the plans
for performing a cycle of the ADM</p>
</li>
<li>
<p>Estimate the resources needed, develop a roadmap and schedule for the
proposed development, and document all these in the Statement of
Architecture Work</p>
</li>
<li>
<p>Define the performance metrics to be met during this cycle of the ADM
by the Enterprise Architecture team</p>
</li>
<li>
<p>Develop the specific Enterprise Architecture Communications Plan and
show where, how, and when the Enterprise Architects will communicate
with the stakeholders, including affinity groupings and communities,
about the progress of the Enterprise Architecture developments</p>
</li>
<li>
<p>Review and agree the plans with the sponsors, and secure formal
approval of the Statement of Architecture Work under the appropriate
governance procedures</p>
</li>
<li>
<p>Gain sponsor’s sign-off to proceed</p>
</li>
</ul>

### 3.4. Outputs

The outputs of Phase A may include, but are not restricted to:

<ul>
<li>
<p>Approved Statement of Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including in particular:</p>
<div class="ulist">
<ul>
<li>
<p>Architecture project description and scope</p>
</li>
<li>
<p>Overview of Architecture Vision</p>
</li>
<li>
<p>Architecture project plan and schedule</p>
</li>
</ul>
</div>
</li>
<li>
<p>Refined statements of business principles, business goals, and
business drivers (see the <a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Architecture Principles (see the
<a href="https://pubs.opengroup.org/togaf-standard/adm-techniques/chap01.html">TOGAF Standard — ADM Techniques</a>)</p>
</li>
<li>
<p>Capability Assessment (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Tailored Architecture Framework (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>) (for the engagement), including:</p>
<div class="ulist">
<ul>
<li>
<p>Tailored architecture method</p>
</li>
<li>
<p>Tailored architecture content (deliverables and artifacts)</p>
</li>
<li>
<p>Configured and deployed tools</p>
</li>
</ul>
</div>
</li>
<li>
<p>Architecture Vision (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Problem description</p>
</li>
<li>
<p>Objective of the Statement of Architecture Work</p>
</li>
<li>
<p>Summary views</p>
</li>
<li>
<p>Business scenario (optional)</p>
</li>
<li>
<p>Refined key high-level stakeholder requirements</p>
</li>
</ul>
</div>
</li>
<li>
<p>Draft Architecture Definition Document, which may include Baseline
and/or Target Architectures of any architecture domain</p>
</li>
<li>
<p>Communications Plan (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Additional content populating the Architecture Repository (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
<div class="dlist">
<dl>
<dt class="hdlist1"><strong>Note:</strong></dt>
<dd>
<p>Multiple business scenarios may be used to generate a single
Architecture Vision.</p>
</dd>
</dl>
</div>
</li>
</ul>

The TOGAF Standard — Architecture Content contains a detailed description of architectural
artifacts which might be produced in this phase, describing them in
detail and relating them to entities, attributes, and relationships in
the TOGAF Enterprise Metamodel.

### 3.5. Approach

#### 3.5.1. General

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

#### 3.5.2. Creating the Architecture Vision

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

<ul>
<li>
<p><strong>Business Capabilities</strong>, which represent a particular ability or
capacity that a business may possess or exchange to achieve a specific
purpose or outcome</p>
<div class="paragraph">
<p>In this phase, the architect should determine whether a framework exists
in the organization to represent business capabilities. If one does not
exist, the architect should consider whether developing a framework is
within the scope of the project. For an introduction to business
capabilities, see
<a href="https://pubs.opengroup.org/togaf-standard/business-capabilities/index.html">TOGAF<sup>®</sup> Series Guide: Business Capabilities</a>.</p>
</div>
</li>
<li>
<p><strong>Value Streams</strong>, which represent an end-to-end collection of
value-adding activities that create an overall result for a customer,
stakeholder, or end user; for an introduction to value streams, see the
<a href="https://pubs.opengroup.org/togaf-standard/value-streams/index.html">TOGAF<sup>®</sup> Series Guide: Value Streams</a>.</p>
</li>
<li>
<p><strong>Organization Maps</strong>, which depict the relationships between the
primary entities that make up the enterprise, its partners, and
stakeholders</p>
<div class="paragraph">
<p>As traditional organizational charts often lack the necessary detail to
reflect the full scope of the enterprise’s activities, the architect can
help to identify and understand the complex web of relationships between
business entities as well as where business capabilities are used and
connection to value stream stages. These are refined and extended in
subsequent phases. For an introduction to organization maps, see the
<a href="https://pubs.opengroup.org/togaf-standard/organization-mapping/index.html">TOGAF<sup>®</sup> Series Guide: Organization Mapping</a>.</p>
</div>
</li>
</ul>

In addition, the Architecture Vision explores other domains which are
appropriate for the Enterprise Architecture in hand. These domains may
include elements of the basic domains, yet serve an additional purpose
for the stakeholders. Example domains may include:

<ul>
<li>
<p>Information</p>
</li>
<li>
<p>Security</p>
</li>
<li>
<p>Digital</p>
</li>
<li>
<p>Network Management</p>
</li>
<li>
<p>Knowledge</p>
</li>
<li>
<p>Industry-specific</p>
</li>
<li>
<p>Services</p>
</li>
<li>
<p>Partnership</p>
</li>
<li>
<p>Cybersecurity</p>
</li>
</ul>

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

## 4. Phase B: Business Architecture

This chapter describes the development of a Business Architecture to
support an agreed Architecture Vision.

![Phase B: Business Architecture](assets/009-b_bus.png)

Figure 4-1: Phase B: Business Architecture

### 4.1. Objectives

The objectives of Phase B are to:

<ul>
<li>
<p>Develop the Target Business Architecture that describes how the
enterprise needs to operate to achieve the business goals, and respond
to the strategic drivers set out in the Architecture Vision, in a way
that addresses the Statement of Architecture Work and stakeholder
concerns</p>
</li>
<li>
<p>Identify candidate Architecture Roadmap components based upon gaps
between the Baseline and Target Business Architectures</p>
</li>
</ul>

### 4.2. Inputs

This section defines the inputs to Phase B.

#### 4.2.1. Reference Materials External to the Enterprise

<ul>
<li>
<p>Architecture reference materials (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
</ul>

#### 4.2.2. Non-Architectural Inputs

<ul>
<li>
<p>Request for Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Business principles, business goals, and business drivers (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Capability Assessment (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Communications Plan (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
</ul>

#### 4.2.3. Architectural Inputs

<ul>
<li>
<p>Organizational Model for Enterprise Architecture (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Scope of organizations impacted</p>
</li>
<li>
<p>Maturity assessment, gaps, and resolution approach</p>
</li>
<li>
<p>Roles and responsibilities for architecture team(s)</p>
</li>
<li>
<p>Constraints on architecture work</p>
</li>
<li>
<p>Budget requirements</p>
</li>
<li>
<p>Governance and support strategy</p>
</li>
</ul>
</div>
</li>
<li>
<p>Tailored Architecture Framework (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Tailored architecture method</p>
</li>
<li>
<p>Tailored architecture content (deliverables and artifacts)</p>
</li>
<li>
<p>Configured and deployed tools</p>
</li>
</ul>
</div>
</li>
<li>
<p>Approved Statement of Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Architecture Principles (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including business principles, when pre-existing</p>
</li>
<li>
<p>Enterprise Continuum (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Architecture Repository (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Re-usable building blocks</p>
</li>
<li>
<p>Publicly available reference models</p>
</li>
<li>
<p>Organization-specific reference models</p>
</li>
<li>
<p>Organization standards</p>
</li>
</ul>
</div>
</li>
<li>
<p>Architecture Vision (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Problem description</p>
</li>
<li>
<p>Objective of the Statement of Architecture Work</p>
</li>
<li>
<p>Summary views</p>
</li>
<li>
<p>Business Scenario (optional)</p>
</li>
<li>
<p>Refined key high-level stakeholder requirements</p>
</li>
</ul>
</div>
</li>
<li>
<p>Draft Architecture Definition Document, which may include Baseline
and/or Target Architectures of any architecture domain</p>
</li>
</ul>

### 4.3. Steps

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

<ul>
<li>
<p>Select reference models, viewpoints, and tools; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_04_03_01">Section 4.3.1, “Select Reference Models, Viewpoints, and Tools”</a></p>
</li>
<li>
<p>Develop Baseline Business Architecture Description; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_04_03_02">Section 4.3.2, “Develop Baseline Business Architecture Description”</a></p>
</li>
<li>
<p>Develop Target Business Architecture Description; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_04_03_03">Section 4.3.3, “Develop Target Business Architecture Description”</a></p>
</li>
<li>
<p>Perform gap analysis; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_04_03_04">Section 4.3.4, “Perform Gap Analysis”</a></p>
</li>
<li>
<p>Define candidate roadmap components; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_04_03_05">Section 4.3.5, “Define Candidate Roadmap Components”</a></p>
</li>
<li>
<p>Resolve impacts across the Architecture Landscape; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_04_03_06">Section 4.3.6, “Resolve Impacts Across the Architecture Landscape”</a></p>
</li>
<li>
<p>Conduct formal stakeholder review; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_04_03_07">Section 4.3.7, “Conduct Formal Stakeholder Review”</a></p>
</li>
<li>
<p>Finalize the Business Architecture; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_04_03_08">Section 4.3.8, “Finalize the Business Architecture”</a></p>
</li>
<li>
<p>Create/Update the Architecture Definition Document; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_04_03_09">Section 4.3.9, “Create/Update the Architecture Definition Document”</a></p>
</li>
</ul>

#### 4.3.1. Select Reference Models, Viewpoints, and Tools

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

##### 4.3.1.1. Determine Overall Modeling Process

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

<ul>
<li>
<p><strong>Business Capability Mapping</strong>: identifies, categorizes, and decomposes
the business capabilities required for the business to have the ability
to deliver value to one or more stakeholders</p>
</li>
<li>
<p><strong>Information Mapping</strong>: collecting the information concepts and their
relationships that matter most to the business</p>
</li>
<li>
<p><strong>Organization Mapping</strong>: a representation of the organizational
structure of the business (including third-party domains), depicting
business units, the decomposition of those units into lower-level
functions, and organizational relationships (unit-to-unit and mapping to
business capabilities, locations, and other attributes)</p>
</li>
<li>
<p><strong>Process Modeling</strong>: the activity of articulating business processes of
an enterprise, to enable analysis and improvement</p>
</li>
<li>
<p><strong>Structured Analysis</strong>: identifies the key business capabilities within
the scope of the architecture, and maps those capabilities onto business
functions and organizational units within the business</p>
</li>
<li>
<p><strong>Use-case Analysis</strong>: a technique used to identify the requirements of
a system or task to be completed, from a user’s perspective</p>
</li>
<li>
<p><strong>Value Stream Mapping</strong>: the end-to-end breakdown of activities that an
organization performs to create the value being exchanged with
stakeholders</p>
<div class="paragraph">
<p>Value stream maps illustrate how an organization delivers value and are
in the context of a specific set of stakeholders, and leverage business
capabilities in order to create stakeholder value and align to other
aspects of the Target Business Architecture.</p>
</div>
</li>
</ul>

The level and rigor of decomposition needed varies from enterprise to
enterprise, as well as within an enterprise, and the architect should
consider the enterprise’s goals, objectives, scope, and purpose of the
Enterprise Architecture effort to determine the level of decomposition.

##### 4.3.1.2. Identify Required Catalogs of Business Building Blocks

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

##### 4.3.1.3. Identify Required Matrices

Matrices show the core relationships between related model entities.

Matrices form the raw material for development of views and also act as
a key resource for impact assessment, carried out as a part of gap
analysis.

The TOGAF Standard — Architecture Content contains a detailed description of matrices which
should be considered for development within a Business Architecture,
describing them in detail and relating them to entities, attributes, and
relationships in the TOGAF Enterprise Metamodel.

##### 4.3.1.4. Identify Required Diagrams

Diagrams present the Business Architecture information from a set of
different perspectives (viewpoints) according to the requirements of the
stakeholders.

The TOGAF Standard — Architecture Content contains a detailed description of diagrams which
should be considered for development within a Business Architecture,
describing them in detail and relating them to entities, attributes, and
relationships in the TOGAF Enterprise Metamodel.

##### 4.3.1.5. Identify Types of Requirement to be Collected

Once the Business Architecture catalogs, matrices, and diagrams have
been developed, architecture modeling is completed by formalizing the
business-focused requirements for implementing the Target Architecture.

These requirements may:

<ul>
<li>
<p>Relate to the business domain</p>
</li>
<li>
<p>Provide requirements input into the Data, Application, and Technology
Architectures</p>
</li>
<li>
<p>Provide detailed guidance to be reflected during design and
implementation to ensure that the solution addresses the original
architecture requirements</p>
</li>
</ul>

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

#### 4.3.2. Develop Baseline Business Architecture Description

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

#### 4.3.3. Develop Target Business Architecture Description

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

#### 4.3.4. Perform Gap Analysis

Verify the architecture models for internal consistency and accuracy:

<ul>
<li>
<p>Perform trade-off analysis to resolve conflicts (if any) among the
different views</p>
</li>
<li>
<p>Validate that the models support the principles, objectives, and
constraints</p>
</li>
<li>
<p>Note changes to the viewpoint represented in the selected models from
the Architecture Repository, and document</p>
</li>
<li>
<p>Test architecture models for completeness against requirements</p>
</li>
</ul>

Identify gaps between the baseline and target, using the gap analysis
technique, as described in the TOGAF Standard — ADM Techniques .

#### 4.3.5. Define Candidate Roadmap Components

Following the creation of a Baseline Architecture, Target Architecture,
and gap analysis results, a business roadmap is required to prioritize
activities over the coming phases.

This initial Business Architecture Roadmap will be used as raw material
to support more detailed definition of a consolidated, cross-discipline
roadmap within the Opportunities & Solutions phase.

#### 4.3.6. Resolve Impacts Across the Architecture Landscape

Once the Business Architecture is finalized, it is necessary to
understand any wider impacts or implications. At this stage, other architecture artifacts in the Architecture
Landscape should be examined to identify:

<ul>
<li>
<p>Does this Business Architecture create an impact on any pre-existing
architectures?</p>
</li>
<li>
<p>Have recent changes been made that impact on the Business
Architecture?</p>
</li>
<li>
<p>Are there any opportunities to leverage work from this Business
Architecture in other areas of the organization?</p>
</li>
<li>
<p>Does this Business Architecture impact other projects (those
planned as well as those in progress)?</p>
</li>
<li>
<p>Will this Business Architecture be impacted by other projects
(those planned as well as those in progress)?</p>
</li>
</ul>

#### 4.3.7. Conduct Formal Stakeholder Review

Check the original motivation for the architecture project and the
Statement of Architecture Work against the proposed Business
Architecture, asking if it is fit for the purpose of supporting
subsequent work in the other architecture domains. Refine the proposed
Business Architecture only if necessary.

#### 4.3.8. Finalize the Business Architecture

<ul>
<li>
<p>Select standards for each of the building blocks, re-using as much as
possible from the reference models selected from the Architecture
Repository</p>
</li>
<li>
<p>Fully document each building block</p>
</li>
<li>
<p>Conduct a final cross-check of overall architecture against business
goals; document the rationale for building block decisions in the
architecture document</p>
</li>
<li>
<p>Document the final requirements traceability report</p>
</li>
<li>
<p>Document the final mapping of the architecture within the Architecture
Repository; from the selected building blocks, identify those that might
be re-used (working practices, roles, business relationships, job
descriptions, etc.), and publish via the Architecture Repository</p>
</li>
<li>
<p>Finalize all the work products, such as gap analysis results</p>
</li>
</ul>

#### 4.3.9. Create/Update the Architecture Definition Document

<ul>
<li>
<p>Document the rationale for building block decisions in the
Architecture Definition Document</p>
</li>
<li>
<p>Prepare the appropriate business sections of the Architecture
Definition Document related to the intended scope and use of the
architecture</p>
</li>
</ul>

If appropriate, use reports and/or graphics generated by modeling tools
to demonstrate key views of the architecture. Route the document for
review by relevant stakeholders, and incorporate feedback.

### 4.4. Outputs

The outputs of Phase B may include, but are not restricted to:

<ul>
<li>
<p>Refined and updated versions of the Architecture Vision phase
deliverables, where applicable, including:</p>
<div class="ulist">
<ul>
<li>
<p>Statement of Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), updated if necessary</p>
</li>
<li>
<p>Validated business principles, business goals, and business drivers
(see the <a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), updated if necessary</p>
</li>
<li>
<p>Architecture Principles (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
</ul>
</div>
</li>
<li>
<p>Draft Architecture Definition Document (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Baseline Business Architecture, Approved, if appropriate</p>
</li>
<li>
<p>Target Business Architecture, Approved, including:</p>
<div class="ulist">
<ul>
<li>
<p>Organization structure — identifying business locations and relating
them to organizational units</p>
</li>
<li>
<p>Business goals and objectives — for the enterprise and each
organizational unit</p>
</li>
<li>
<p>Business functions — a detailed, recursive step involving successive
decomposition of major functional areas into sub-functions</p>
</li>
<li>
<p>Business capabilities — the abilities that a business needs to
possess or exchange to achieve its goals and objectives</p>
</li>
<li>
<p>Business services — the services that support the business by
encapsulating a unique “elements of business behavior”; a service
offered external to the enterprise may be supported by business services</p>
</li>
<li>
<p>Products — output generated by the business to be offered to
customers; products include materials and/or services</p>
</li>
<li>
<p>Business processes, including measures and deliverables</p>
</li>
<li>
<p>Business roles, including development and modification of skills
requirements</p>
</li>
<li>
<p>Business data model</p>
</li>
<li>
<p>Correlation of organization/business functions and business
capabilities — relate business capabilities to organizational units in
the form of a matrix report</p>
</li>
</ul>
</div>
</li>
<li>
<p>Views corresponding to the selected viewpoints addressing key
stakeholder concerns</p>
</li>
</ul>
</div>
</li>
<li>
<p>Draft Architecture Requirements Specification (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including such Business Architecture requirements as:</p>
<div class="ulist">
<ul>
<li>
<p>Gap analysis results</p>
</li>
<li>
<p>Technical requirements — identifying, categorizing, and prioritizing
the implications for work in the remaining architecture domains; for
example, by a dependency/priority matrix (e.g., guiding trade-off
between speed of transaction processing and security); list the specific
models that are expected to be produced (for example, expressed as
primitives of the Zachman Framework)</p>
</li>
<li>
<p>Updated business requirements</p>
</li>
</ul>
</div>
</li>
<li>
<p>Business Architecture components of an Architecture Roadmap (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
</ul>

The TOGAF Standard — Architecture Content contains a detailed description of architectural
artifacts which might be produced in this phase.

### 4.5. Approach

Business Architecture is a representation of holistic, multi-dimensional
business views of capabilities, end-to-end value delivery, information,
and organizational structure; and the relationships among these business
views and strategies, products, policies, initiatives, and stakeholders.

Business Architecture relates business elements to business goals and
elements of other domains.

#### 4.5.1. General

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

#### 4.5.2. Developing the Baseline Description

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

#### 4.5.3. Applying Business Capabilities

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

#### 4.5.4. Applying Value Streams

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

#### 4.5.5. Applying the Organization Map

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

#### 4.5.6. Applying Information Maps

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

#### 4.5.7. Applying Modeling Techniques

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

<ul>
<li>
<p><strong>Activity Models</strong> (also called <strong>Business Process Models</strong>) describe the
enterprise’s business activities, the data and/or information exchanged
between activities (internal exchanges), and the data and/or information
exchanged with other activities that are outside the scope of the model
(external exchanges)</p>
<div class="paragraph">
<p>Activity models are hierarchical in nature. They capture the activities
performed in a business process, and the Inputs, Controls, Outputs, and
Mechanisms/Resources (ICOMs) of those activities. Activity models can be
annotated with explicit statements of business rules, which represent
relationships among the ICOMs. For example, a business rule can specify
who can do what under specified conditions, the combination of inputs
and controls needed, and the resulting outputs. One technique for
creating activity models is the Integrated Computer Aided Manufacturing
(ICAM) DEFinition (IDEF) modeling technique.</p>
</div>
<div class="paragraph">
<p>The Object Management Group (OMG) has developed the Business Process
Model and Notation<sup><strong>TM</strong></sup> (BPMN<sup><strong>TM</strong></sup>), a standard for business process
modeling that includes a language with which to specify business
processes, their tasks/steps, and the documents produced.</p>
</div>
</li>
<li>
<p><strong>Use-Case Models</strong> describe the business process of an enterprise in
terms of use-cases and actors corresponding to business processes and
organizational participants (people, organizations, etc.)</p>
<div class="paragraph">
<p>The use-case model is described in use-case diagrams and use-case
specifications.</p>
</div>
</li>
<li>
<p><strong>Logical Data Model</strong> (or <strong>Class Model</strong>)</p>
<div class="paragraph">
<p>Logical data models describe the entities, their attributes, and the
acceptable values for these attributes as well as the relationships
between the various entities. Particularly useful is the “is-a”
relationship for analyses. For example, if a sedan is a type of car
which is a type of vehicle, then a general business rule for all
vehicles can be written once and automatically picked up for all types
of cars and trucks.</p>
</div>
<div class="paragraph">
<p>A class model expands the logical data model to include behaviors by
including services (methods) unique to the entity (now called a class).
Normally applications and information architects will use the class
diagram, and Business Architects will use the logical data model.</p>
</div>
</li>
</ul>

![UML Business Class Diagram](assets/008-08_umlbusclass.png)

Figure 4-2: UML Business Class Diagram

All three types of model above can be represented in the Unified
Modeling Language™ (UML ® ), and a variety of tools exist for
generating such models.

Certain industry sectors have modeling techniques specific to the sector
concerned.

#### 4.5.8. Architecture Repository

As part of Phase B, the architecture team will need to consider what
relevant Business Architecture resources are available from the
Architecture Repository (see the TOGAF Standard — Architecture Content ), in particular:

<ul>
<li>
<p>Industry reference models relevant to the organization’s industry
sector</p>
</li>
<li>
<p>Enterprise-specific Business Architecture views (capability maps,
value stream maps, organization maps, etc.)</p>
</li>
<li>
<p>Enterprise-specific building blocks (process components, business
rules, job descriptions, etc.)</p>
</li>
<li>
<p>Applicable standards</p>
</li>
</ul>

## 5. Phase C: Information Systems Architectures

This chapter describes the Information Systems Architectures for an
architecture project, including the development of Data and Application
Architectures.

![Phase C: Information Systems](assets/007-c_inf.png)

Figure 5-1: Phase C: Information Systems

### 5.1. Objectives

The objectives of Phase C are to:

<ul>
<li>
<p>Develop the Target Information Systems Architectures, describing how
the enterprise’s Information Systems Architecture will enable the
Business Architecture and the Architecture Vision, in a way that
addresses the Statement of Architecture Work and stakeholder concerns</p>
</li>
<li>
<p>Identify candidate Architecture Roadmap components based upon gaps
between the Baseline and Target Information Systems (Data and
Application) Architectures</p>
</li>
</ul>

### 5.2. Approach

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

<ul>
<li>
<p>Phase C: Information Systems Architectures — Data Architecture; see
<a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#chap06">Chapter 6, <em>Phase C: Information Systems Architectures — Data Architecture</em></a></p>
</li>
<li>
<p>Phase C: Information Systems Architectures — Application Architecture; see
<a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#chap07">Chapter 7, <em>Phase C: Information Systems Architectures — Application Architecture</em></a></p>
</li>
</ul>

## 6. Phase C: Information Systems Architectures — Data Architecture

This chapter describes the Data Architecture part of Phase C.

### 6.1. Objectives

The objectives of the Data Architecture part of Phase C are to:

<ul>
<li>
<p>Develop the Target Data Architecture that enables the Business Architecture and the Architecture Vision, in a way that addresses the Statement of Architecture Work and stakeholder concerns</p>
</li>
<li>
<p>Identify candidate Architecture Roadmap components based upon gaps between the Baseline and Target Data Architectures</p>
</li>
</ul>

### 6.2. Inputs

This section defines the inputs to Phase C (Data Architecture).

#### 6.2.1. Reference Materials External to the Enterprise

<ul>
<li>
<p>Architecture reference materials (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p><a href="https://pubs.opengroup.org/togaf-standard/master-data-management/index.html">TOGAF<sup>®</sup> Series Guide: Information Architecture — Customer Master Data Management</a></p>
</li>
<li>
<p><a href="https://pubs.opengroup.org/togaf-standard/bi-analytics/index.html">TOGAF<sup>®</sup> Series Guide: Information Architecture: Business Intelligence &amp; Analytics and Metadata Management Reference Models</a></p>
</li>
</ul>

#### 6.2.2. Non-Architectural Inputs

<ul>
<li>
<p>Request for Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Capability Assessment (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Communications Plan (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
</ul>

#### 6.2.3. Architectural Inputs

<ul>
<li>
<p>Organizational Model for Enterprise Architecture (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Scope of organizations impacted</p>
</li>
<li>
<p>Maturity assessment, gaps, and resolution approach</p>
</li>
<li>
<p>Roles and responsibilities for architecture team(s)</p>
</li>
<li>
<p>Constraints on architecture work</p>
</li>
<li>
<p>Budget requirements</p>
</li>
<li>
<p>Governance and support strategy</p>
</li>
</ul>
</div>
</li>
<li>
<p>Tailored Architecture Framework (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Tailored architecture method</p>
</li>
<li>
<p>Tailored architecture content (deliverables and artifacts)</p>
</li>
<li>
<p>Configured and deployed tools</p>
</li>
</ul>
</div>
</li>
<li>
<p>Data principles (see the <a href="https://pubs.opengroup.org/togaf-standard/adm-techniques/chap01.html">TOGAF Standard — ADM Techniques</a>), if existing</p>
</li>
<li>
<p>Statement of Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Architecture Vision (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Architecture Repository (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Re-usable building blocks (in particular, definitions of current data)</p>
</li>
<li>
<p>Publicly available reference models</p>
</li>
<li>
<p>Organization-specific reference models</p>
</li>
<li>
<p>Organization standards</p>
</li>
</ul>
</div>
</li>
<li>
<p>Draft Architecture Definition Document, which may include Baseline
and/or Target Architectures of any architecture domain</p>
</li>
<li>
<p>Draft Architecture Requirements Specification (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Gap analysis results (from Business Architecture)</p>
</li>
<li>
<p>Relevant technical requirements that will apply to this phase</p>
</li>
</ul>
</div>
</li>
<li>
<p>Business Architecture components of an Architecture Roadmap (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
</ul>

### 6.3. Steps

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

<ul>
<li>
<p>Select reference models, viewpoints, and tools; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_06_03_01">Section 6.3.1, “Select Reference Models, Viewpoints, and Tools”</a></p>
</li>
<li>
<p>Develop Baseline Data Architecture Description; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_06_03_02">Section 6.3.2, “Develop Baseline Data Architecture Description”</a></p>
</li>
<li>
<p>Develop Target Data Architecture Description; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_06_03_03">Section 6.3.3, “Develop Target Data Architecture Description”</a></p>
</li>
<li>
<p>Perform gap analysis; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_06_03_04">Section 6.3.4, “Perform Gap Analysis”</a></p>
</li>
<li>
<p>Define candidate roadmap components; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_06_03_05">Section 6.3.5, “Define Candidate Roadmap Components”</a></p>
</li>
<li>
<p>Resolve impacts across the Architecture Landscape; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_06_03_06">Section 6.3.6, “Resolve Impacts Across the Architecture Landscape”</a></p>
</li>
<li>
<p>Conduct formal stakeholder review; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_06_03_07">Section 6.3.7, “Conduct Formal Stakeholder Review”</a></p>
</li>
<li>
<p>Finalize the Data Architecture; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_06_03_08">Section 6.3.8, “Finalize the Data Architecture”</a></p>
</li>
<li>
<p>Create/update the Architecture Definition Document; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_06_03_09">Section 6.3.9, “Create/Update the Architecture Definition Document”</a></p>
</li>
</ul>

#### 6.3.1. Select Reference Models, Viewpoints, and Tools

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

<ul>
<li>
<p>Entity relationship diagram</p>
</li>
<li>
<p>Class diagram</p>
</li>
</ul>

Further guidance on Information Architecture reference models can be
found in the following documents:

<ul>
<li>
<p><a href="https://pubs.opengroup.org/togaf-standard/master-data-management/index.html">TOGAF<sup>®</sup> Series Guide: Information Architecture — Customer Master Data Management</a></p>
</li>
<li>
<p><a href="https://pubs.opengroup.org/togaf-standard/bi-analytics/index.html">TOGAF<sup>®</sup> Series Guide: Information Architecture: Business Intelligence &amp; Analytics</a></p>
</li>
<li>
<p><a href="https://pubs.opengroup.org/togaf-standard/metadata-management/index.html">TOGAF<sup>®</sup> Series Guide: Information Architecture: Metadata Management</a></p>
</li>
</ul>

##### 6.3.1.1. Determine Overall Modeling Process

For each viewpoint, select the models needed to support the specific
view required, using the selected tool or method.

Ensure that all stakeholder concerns are covered. If they are not,
create new models to address concerns not covered, or augment existing
models (see above).

The recommended process for developing a Data Architecture is as
follows:

<ul>
<li>
<p>Collect data-related models from existing Business Architecture and
Application Architecture materials</p>
</li>
<li>
<p>Rationalize data requirements and align with any existing enterprise
data catalogs and models; this allows the development of a data
inventory and entity relationship</p>
</li>
<li>
<p>Update and develop matrices across the architecture by relating data
to business service, business capability, business function, access
rights, and application</p>
</li>
<li>
<p>Elaborate Data Architecture views by examining how data is created,
distributed, migrated, secured, and archived</p>
</li>
</ul>

##### 6.3.1.2. Identify Required Catalogs of Data Building Blocks

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

##### 6.3.1.3. Identify Required Matrices

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

##### 6.3.1.4. Identify Required Diagrams

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

##### 6.3.1.5. Identify Types of Requirement to be Collected

Once the Data Architecture catalogs, matrices, and diagrams have been
developed, architecture modeling is completed by formalizing the
data-focused requirements for implementing the Target Architecture.

These requirements may:

<ul>
<li>
<p>Relate to the data domain</p>
</li>
<li>
<p>Provide requirements input into the Application and Technology
Architectures</p>
</li>
<li>
<p>Provide detailed guidance to be reflected during design and
implementation to ensure that the solution addresses the original
architecture requirements</p>
</li>
</ul>

Within this step, the architect should identify requirements that should
be met by the architecture (see Section 13.5.2, “Requirements Development” ).

#### 6.3.2. Develop Baseline Data Architecture Description

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

#### 6.3.3. Develop Target Data Architecture Description

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

#### 6.3.4. Perform Gap Analysis

Verify the architecture models for internal consistency and accuracy:

<ul>
<li>
<p>Perform trade-off analysis to resolve conflicts (if any) among the
different views</p>
</li>
<li>
<p>Validate that the models support the principles, objectives, and
constraints</p>
</li>
<li>
<p>Note changes to the viewpoint represented in the selected models from
the Architecture Repository, and document</p>
</li>
<li>
<p>Test architecture models for completeness against requirements</p>
</li>
</ul>

Identify gaps between the Baseline and Target, using the gap analysis
technique as described in the TOGAF Standard — ADM Techniques .

#### 6.3.5. Define Candidate Roadmap Components

Following the creation of a Baseline Architecture, Target Architecture,
and gap analysis, a data roadmap is required to prioritize activities
over the coming phases.

This initial Data Architecture roadmap will be used as raw material to
support more detailed definition of a consolidated, cross-discipline
roadmap within the Opportunities & Solutions phase.

#### 6.3.6. Resolve Impacts Across the Architecture Landscape

Once the Data Architecture is finalized, it is necessary to understand
any wider impacts or implications.

At this stage, other architecture artifacts in the Architecture
Landscape should be examined to identify:

<ul>
<li>
<p>Does this Data Architecture create an impact on any pre-existing
architectures?</p>
</li>
<li>
<p>Have recent changes been made that impact the Data Architecture?</p>
</li>
<li>
<p>Are there any opportunities to leverage work from this Data
Architecture in other areas of the organization?</p>
</li>
<li>
<p>Does this Data Architecture impact other projects (including those
planned as well as those currently in progress)?</p>
</li>
<li>
<p>Will this Data Architecture be impacted by other projects (including
those planned as well as those currently in progress)?</p>
</li>
</ul>

#### 6.3.7. Conduct Formal Stakeholder Review

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

#### 6.3.8. Finalize the Data Architecture

<ul>
<li>
<p>Select standards for each of the building blocks, re-using as much as
possible from the reference models selected from the Architecture
Repository</p>
</li>
<li>
<p>Fully document each building block</p>
</li>
<li>
<p>Conduct a final cross-check of overall architecture against business
requirements; document the rationale for building block decisions in the
architecture document</p>
</li>
<li>
<p>Document the final requirements traceability report</p>
</li>
<li>
<p>Document the final mapping of the architecture within the Architecture
Repository; from the selected building blocks, identify those that might
be re-used, and publish via the Architecture Repository</p>
</li>
<li>
<p>Finalize all the work products, such as gap analysis</p>
</li>
</ul>

#### 6.3.9. Create/Update the Architecture Definition Document

Document the rationale for building block decisions in the Architecture
Definition Document.

Prepare the Data Architecture sections of the Architecture Definition
Document, comprising some or all of:

<ul>
<li>
<p>Business data model</p>
</li>
<li>
<p>Logical data model</p>
</li>
<li>
<p>Data management process model</p>
</li>
<li>
<p>Data Entity/Business Function matrix</p>
</li>
<li>
<p>Data interoperability requirements (e.g., XML schema, security
policies)</p>
</li>
<li>
<p>If appropriate, use reports and/or graphics generated by modeling
tools to demonstrate key views of the architecture; route the document
for review by relevant stakeholders, and incorporate feedback</p>
</li>
</ul>

### 6.4. Outputs

The outputs of Phase C (Data Architecture) may include, but are not
restricted to:

<ul>
<li>
<p>Refined and updated versions of the Architecture Vision phase
deliverables, where applicable:</p>
<div class="ulist">
<ul>
<li>
<p>Statement of Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), updated if necessary</p>
</li>
<li>
<p>Validated data principles (see the
<a href="https://pubs.opengroup.org/togaf-standard/adm-techniques/chap01.html">TOGAF Standard — ADM Techniques</a>), or
new data principles (if generated here)</p>
</li>
</ul>
</div>
</li>
<li>
<p>Draft Architecture Definition Document (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Baseline Data Architecture, Approved, if appropriate</p>
</li>
<li>
<p>Target Data Architecture, Approved, including:</p>
<div class="ulist">
<ul>
<li>
<p>Business data model</p>
</li>
<li>
<p>Logical data model</p>
</li>
<li>
<p>Data management process models</p>
</li>
<li>
<p>Data Entity/Business Function matrix</p>
</li>
</ul>
</div>
</li>
<li>
<p>Views corresponding to the selected viewpoints addressing key
stakeholder concerns</p>
</li>
</ul>
</div>
</li>
<li>
<p>Draft Architecture Requirements Specification (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including such Data Architecture requirements as:</p>
<div class="ulist">
<ul>
<li>
<p>Gap analysis results</p>
</li>
<li>
<p>Data interoperability requirements</p>
</li>
<li>
<p>Relevant technical requirements that will apply to this evolution of
the architecture development cycle</p>
</li>
<li>
<p>Constraints on the Technology Architecture about to be designed</p>
</li>
<li>
<p>Updated business requirements, if appropriate</p>
</li>
<li>
<p>Updated application requirements, if appropriate</p>
</li>
</ul>
</div>
</li>
<li>
<p>Data Architecture components of an Architecture Roadmap (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
</ul>

The TOGAF Standard — Architecture Content contains a detailed description of architectural
artifacts which might be produced in this phase.

### 6.5. Approach

#### 6.5.1. Data Structure

A Data Architecture should be able to handle:

<ul>
<li>
<p>Data at rest — data in stores</p>
</li>
<li>
<p>Data in motion — data in transactions or services/APIs</p>
</li>
<li>
<p>Data in use — data at the border of the application (e.g., GUI)</p>
</li>
<li>
<p>Open data — data that the organization provides for public usage and
which it is voluntarily or legally required to provide</p>
</li>
</ul>

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

#### 6.5.2. Key Considerations for Data Architecture

##### 6.5.2.1. Data Management

When an enterprise has chosen to undertake large-scale architectural
transformation, it is important to understand and address data
management issues. A structured and comprehensive approach to data
management enables the effective use of data to capitalize on its
competitive advantages.

Considerations include:

<ul>
<li>
<p>A clear definition of which application components in the landscape
will serve as the system of record or reference for enterprise master
data</p>
</li>
<li>
<p>Will there be an enterprise-wide standard that all application
components, including software packages, need to adopt?</p>
<div class="paragraph">
<p>(In the main, packages can be prescriptive about the data models and may
not be flexible.)</p>
</div>
</li>
<li>
<p>Clearly understand how data entities are utilized by business
capabilities, business functions, processes, and business and
application services</p>
</li>
<li>
<p>Clearly understand how and where enterprise data entities are created,
stored, transported, and reported</p>
</li>
<li>
<p>What is the level and complexity of data transformations required to
support the information exchange needs between applications?</p>
</li>
<li>
<p>What will be the requirement for software in supporting data integration with the enterprise’s customers and suppliers (e.g., use of Extract, Transform, Load (ETL) tools during data migration, data profiling tools to evaluate data quality, etc.)?</p>
</li>
</ul>

More guidance on data management can be found in the TOGAF ® Series Guide: Information Architecture — Customer Master Data Management .

##### 6.5.2.2. Data Migration

When an existing application is replaced, there will be a critical need to migrate data (master, transactional, and reference) to the new application. The Data Architecture should identify data migration requirements and also provide indicators as to the level of transformation, weeding, and cleansing that will be required to present data in a format that meets the requirements and constraints of the
target application. The objective being that the target application has quality data when it is populated. Another key consideration is to ensure that an enterprise-wide common data definition is established to support the transformation.

##### 6.5.2.3. Data Governance

Data governance considerations ensure that the enterprise has the necessary dimensions in place to enable the transformation, as follows:

<ul>
<li>
<p><strong>Structure</strong>: this dimension pertains to whether the enterprise has the necessary organizational structure and the standards bodies to manage data entity aspects of the transformation</p>
</li>
<li>
<p><strong>Management System</strong>: here enterprises should have the necessary management system and data-related programs to manage the governance aspects of data entities throughout its lifecycle</p>
</li>
<li>
<p><strong>People</strong>: this dimension addresses what data-related skills and roles the enterprise requires for the transformation</p>
<div class="paragraph">
<p>If the enterprise lacks such resources and skills, the enterprise should consider either acquiring those critical skills or training existing internal resources to meet the requirements through a well-defined learning program.</p>
</div>
</li>
</ul>

#### 6.5.3. Architecture Repository

As part of this phase, the architecture team will need to consider what relevant Data Architecture resources are available in the organization’s Architecture Repository (see the TOGAF Standard — Architecture Content ); in particular, generic data models relevant to the
organization’s industry “vertical” sector.

## 7. Phase C: Information Systems Architectures — Application Architecture

This chapter describes the Application Architecture part of Phase C.

### 7.1. Objectives

The objectives of the Application Architecture part of Phase C are to:

<ul>
<li>
<p>Develop the Target Application Architecture that enables the Business
Architecture and the Architecture Vision, in a way that addresses the
Statement of Architecture Work and stakeholder concerns</p>
</li>
<li>
<p>Identify candidate Architecture Roadmap components based upon gaps
between the Baseline and Target Application Architectures</p>
</li>
</ul>

### 7.2. Inputs

This section defines the inputs to Phase C (Application Architecture).

#### 7.2.1. Reference Materials External to the Enterprise

<ul>
<li>
<p>Architecture reference materials (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
</ul>

#### 7.2.2. Non-Architectural Inputs

<ul>
<li>
<p>Request for Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Capability Assessment (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Communications Plan (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
</ul>

#### 7.2.3. Architectural Inputs

<ul>
<li>
<p>Organizational Model for Enterprise Architecture (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Scope of organizations impacted</p>
</li>
<li>
<p>Maturity assessment, gaps, and resolution approach</p>
</li>
<li>
<p>Roles and responsibilities for architecture team(s)</p>
</li>
<li>
<p>Constraints on architecture work</p>
</li>
<li>
<p>Budget requirements</p>
</li>
<li>
<p>Governance and support strategy</p>
</li>
</ul>
</div>
</li>
<li>
<p>Tailored Architecture Framework (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Tailored architecture method</p>
</li>
<li>
<p>Tailored architecture content (deliverables and artifacts)</p>
</li>
<li>
<p>Configured and deployed tools</p>
</li>
</ul>
</div>
</li>
<li>
<p>Application principles (see the
<a href="https://pubs.opengroup.org/togaf-standard/adm-techniques/chap01.html">TOGAF Standard — ADM Techniques</a>), if
existing</p>
</li>
<li>
<p>Statement of Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Architecture Vision (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Architecture Repository (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Re-usable building blocks</p>
</li>
<li>
<p>Publicly available reference models</p>
</li>
<li>
<p>Organization-specific reference models</p>
</li>
<li>
<p>Organization standards</p>
</li>
</ul>
</div>
</li>
<li>
<p>Draft Architecture Definition Document, which may include Baseline
and/or Target Architectures of any architecture domain</p>
</li>
<li>
<p>Draft Architecture Requirements Specification (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Gap analysis results (from Business Architecture and Data
Architecture, if available)</p>
</li>
<li>
<p>Relevant technical requirements that will apply to this phase</p>
</li>
</ul>
</div>
</li>
<li>
<p>Business and Data Architecture components of an Architecture Roadmap,
if available (see the <a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
</ul>

### 7.3. Steps

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

<ul>
<li>
<p>Select reference models, viewpoints, and tools; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_07_03_01">Section 7.3.1, “Select Reference Models, Viewpoints, and Tools”</a></p>
</li>
<li>
<p>Develop Baseline Application Architecture Description; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_07_03_02">Section 7.3.2, “Develop Baseline Application Architecture Description”</a></p>
</li>
<li>
<p>Develop Target Application Architecture Description; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_07_03_03">Section 7.3.3, “Develop Target Application Architecture Description”</a></p>
</li>
<li>
<p>Perform gap analysis; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_07_03_04">Section 7.3.4, “Perform Gap Analysis”</a></p>
</li>
<li>
<p>Define candidate roadmap components; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_07_03_05">Section 7.3.5, “Define Candidate Roadmap Components”</a></p>
</li>
<li>
<p>Resolve impacts across the Architecture Landscape; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_07_03_06">Section 7.3.6, “Resolve Impacts Across the Architecture Landscape”</a></p>
</li>
<li>
<p>Conduct formal stakeholder review; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_07_03_07">Section 7.3.7, “Conduct Formal Stakeholder Review”</a></p>
</li>
<li>
<p>Finalize the Application Architecture; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_07_03_08">Section 7.3.8, “Finalize the Application Architecture”</a></p>
</li>
<li>
<p>Create/Update the Architecture Definition Document; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_07_03_09">Section 7.3.9, “Create/Update the Architecture Definition Document”</a></p>
</li>
</ul>

#### 7.3.1. Select Reference Models, Viewpoints, and Tools

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

##### 7.3.1.1. Determine Overall Modeling Process

For each viewpoint, select the models needed to support the specific
view required, using the selected tool or method.

Ensure that all stakeholder concerns are covered. If they are not,
create new models to address concerns not covered, or augment existing
models (see above).

The recommended process for developing an Application Architecture is as
follows:

<ul>
<li>
<p>Understand the list of applications or application components that are
required, based on the baseline Application Portfolio, what the
requirements are, and the Business Architecture scope</p>
</li>
<li>
<p>Simplify complicated applications by decomposing them into two or more
applications</p>
</li>
<li>
<p>Ensure that the set of application definitions is internally
consistent, by removing duplicate functionality as far as possible, and
combining similar applications into one</p>
</li>
<li>
<p>Identify logical applications and the most appropriate physical
applications</p>
</li>
<li>
<p>Develop matrices across the architecture by relating applications to
business services, business capabilities, data, processes, etc.</p>
</li>
<li>
<p>Elaborate a set of Application Architecture views by examining how the
application will function, capturing integration, migration,
development, and operational concerns</p>
</li>
</ul>

The level and rigor of decomposition needed varies from enterprise to
enterprise, as well as within an enterprise, and the architect should
consider the enterprise’s goals, objectives, scope, and purpose of the
Enterprise Architecture effort to determine the level of decomposition.

The level of granularity should be sufficient to enable identification
of gaps and the scope of candidate work packages.

##### 7.3.1.2. Identify Required Catalogs of Application Building Blocks

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

##### 7.3.1.3. Identify Required Matrices

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

##### 7.3.1.4. Identify Required Diagrams

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

##### 7.3.1.5. Identify Types of Requirement to be Collected

Once the Application Architecture catalogs, matrices, and diagrams have
been developed, architecture modeling is completed by formalizing the
application-focused requirements for implementing the Target
Architecture.

These requirements may:

<ul>
<li>
<p>Relate to the application domain</p>
</li>
<li>
<p>Provide requirements input into the Data and Technology Architectures</p>
</li>
<li>
<p>Provide detailed guidance to be reflected during design and
implementation to ensure that the solution addresses the original
architecture requirements</p>
</li>
</ul>

Within this step, the architect should identify requirements that should
be met by the architecture; see Section 13.5.2, “Requirements Development” .

#### 7.3.2. Develop Baseline Application Architecture Description

Develop a Baseline Description of the existing Application Architecture, to the extent necessary to support the Target Application Architecture.
The scope and level of detail to be defined will depend on the extent to which existing applications are likely to be carried over into the Target Application Architecture, and on whether Architecture Descriptions exist, as described in Section 7.5, “Approach” .
To the extent possible, identify the relevant Application Architecture building blocks, drawing on the Architecture Repository (see the TOGAF Standard — Architecture Content ). If not already existing within the Architecture Repository,
define each application in line with the Application Portfolio catalog (see the TOGAF Standard — Architecture Content ).

Where new architecture models need to be developed to satisfy
stakeholder concerns, use the models identified within
the first step in this phase (see Section 7.3.1, “Select Reference Models, Viewpoints, and Tools” )
as a guideline for creating new architecture content to describe the Baseline
Architecture.

#### 7.3.3. Develop Target Application Architecture Description

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

#### 7.3.4. Perform Gap Analysis

Verify the architecture models for internal consistency and accuracy:

<ul>
<li>
<p>Perform trade-off analysis to resolve conflicts (if any) among the
different views</p>
</li>
<li>
<p>Validate that the models support the principles, objectives, and
constraints</p>
</li>
<li>
<p>Note changes to the viewpoint represented in the selected models from
the Architecture Repository, and document</p>
</li>
<li>
<p>Test architecture models for completeness against requirements</p>
</li>
</ul>

Identify gaps between the baseline and target, using the gap analysis
technique as described in the TOGAF Standard — ADM Techniques .

#### 7.3.5. Define Candidate Roadmap Components

Following the creation of a Baseline Architecture, Target Architecture,
and gap analysis, an application roadmap is required to prioritize
activities over the coming phases.

This initial Application Architecture roadmap will be used as raw
material to support more detailed definition of a consolidated,
cross-discipline roadmap within the Opportunities & Solutions phase.

#### 7.3.6. Resolve Impacts Across the Architecture Landscape

Once the Application Architecture is finalized, it is necessary to
understand any wider impacts or implications.

At this stage, other architecture artifacts in the Architecture
Landscape should be examined to identify:

<ul>
<li>
<p>Does this Application Architecture create an impact on any
pre-existing architectures?</p>
</li>
<li>
<p>Have recent changes been made that impact the Application
Architecture?</p>
</li>
<li>
<p>Are there any opportunities to leverage work from this Application
Architecture in other areas of the organization?</p>
</li>
<li>
<p>Does this Application Architecture impact other projects (including those planned as well as those currently in progress)?</p>
</li>
<li>
<p>Will this Application Architecture be impacted by other projects
(including those planned as well as those currently in progress)?</p>
</li>
</ul>

#### 7.3.7. Conduct Formal Stakeholder Review

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

#### 7.3.8. Finalize the Application Architecture

<ul>
<li>
<p>Select standards for each of the building blocks, re-using as much as
possible from the reference models selected from the Architecture
Repository</p>
</li>
<li>
<p>Fully document each building block</p>
</li>
<li>
<p>Conduct a final cross-check of overall architecture against business
requirements; document the rationale for building block decisions in the
architecture document</p>
</li>
<li>
<p>Document the final requirements traceability report</p>
</li>
<li>
<p>Document the final mapping of the architecture within the Architecture
Repository; from the selected building blocks, identify those that might
be re-used, and publish via the Architecture Repository</p>
</li>
<li>
<p>Finalize all the work products, such as gap analysis</p>
</li>
</ul>

#### 7.3.9. Create/Update the Architecture Definition Document

<ul>
<li>
<p>Document the rationale for building block decisions in the
Architecture Definition Document</p>
</li>
<li>
<p>Prepare the Application Architecture sections of the Architecture Definition Document; if appropriate, use reports and/or graphics generated by modeling tools to demonstrate key views of the architecture; route the document for review by relevant stakeholders, incorporate feedback</p>
</li>
</ul>

### 7.4. Outputs

The outputs of Phase C (Application Architecture) may include, but are
not restricted to:

<ul>
<li>
<p>Refined and updated versions of the Architecture Vision phase
deliverables, where applicable:</p>
<div class="ulist">
<ul>
<li>
<p>Statement of Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), updated if necessary</p>
</li>
<li>
<p>Validated application principles, or new application principles (if
generated here)</p>
</li>
</ul>
</div>
</li>
<li>
<p>Draft Architecture Definition Document (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Baseline Application Architecture, Approved, if appropriate</p>
</li>
<li>
<p>Target Application Architecture, Approved</p>
</li>
<li>
<p>Views corresponding to the selected viewpoints, addressing key
stakeholder concerns</p>
</li>
</ul>
</div>
</li>
<li>
<p>Draft Architecture Requirements Specification (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including such Application Architecture requirements as:</p>
<div class="ulist">
<ul>
<li>
<p>Gap analysis results</p>
</li>
<li>
<p>Applications interoperability requirements</p>
</li>
<li>
<p>Relevant technical requirements that will apply to this evolution of
the architecture development cycle</p>
</li>
<li>
<p>Constraints on the Technology Architecture about to be designed</p>
</li>
<li>
<p>Updated business requirements, if appropriate</p>
</li>
<li>
<p>Updated data requirements, if appropriate</p>
</li>
</ul>
</div>
</li>
<li>
<p>Application Architecture components of an Architecture Roadmap (see
the <a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
</ul>

The TOGAF Standard — Architecture Content contains a detailed description of architectural
artifacts which might be produced in this phase.

### 7.5. Approach

#### 7.5.1. Architecture Repository

As part of this phase, the architecture team will need to consider what
relevant Application Architecture resources are available in the
Architecture Repository (see the TOGAF Standard — Architecture Content ).
In particular:

<ul>
<li>
<p>Generic business models and related application models relevant to the
organization’s industry sector</p>
</li>
<li>
<p>Application models relevant to common high-level business functions,
such as electronic commerce, supply chain management, etc.</p>
</li>
</ul>

The Open Group has a Reference Model for Integrated Information
Infrastructure (III-RM) — see the TOGAF ® Series Guide: The TOGAF Integrated Information Infrastructure Reference Model (III-RM) — that focuses on the application-level components and services necessary to
provide an integrated information infrastructure.

## 8. Phase D: Technology Architecture

This chapter describes the development of a Technology Architecture for
an architecture project.

![Phase D: Technology Architecture](assets/006-d_tech.png)

Figure 8-1: Phase D: Technology Architecture

### 8.1. Objectives

The objectives of Phase D are to:

<ul>
<li>
<p>Develop the Target Technology Architecture that enables the
Architecture Vision, target business, data, and application building
blocks to be delivered through technology components and technology
services, in a way that addresses the Statement of Architecture Work and
stakeholder concerns</p>
</li>
<li>
<p>Identify candidate Architecture Roadmap components based upon gaps
between the Baseline and Target Technology Architectures</p>
</li>
</ul>

### 8.2. Inputs

This section defines the inputs to Phase D.

#### 8.2.1. Reference Materials External to the Enterprise

<ul>
<li>
<p>Architecture reference materials (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Product information on candidate products</p>
</li>
</ul>

#### 8.2.2. Non-Architectural Inputs

<ul>
<li>
<p>Request for Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Capability Assessment (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Communications Plan (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
</ul>

#### 8.2.3. Architectural Inputs

<ul>
<li>
<p>Organizational Model for Enterprise Architecture (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Scope of organizations impacted</p>
</li>
<li>
<p>Maturity assessment, gaps, and resolution approach</p>
</li>
<li>
<p>Roles and responsibilities for architecture team(s)</p>
</li>
<li>
<p>Constraints on architecture work</p>
</li>
<li>
<p>Budget requirements</p>
</li>
<li>
<p>Governance and support strategy</p>
</li>
</ul>
</div>
</li>
<li>
<p>Tailored Architecture Framework (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Tailored architecture method</p>
</li>
<li>
<p>Tailored architecture content (deliverables and artifacts)</p>
</li>
<li>
<p>Configured and deployed tools</p>
</li>
</ul>
</div>
</li>
<li>
<p>Technology principles (see the <a href="https://pubs.opengroup.org/togaf-standard/adm-techniques/chap01.html">TOGAF Standard — ADM Techniques</a>), if existing</p>
</li>
<li>
<p>Statement of Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Architecture Vision (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Architecture Repository (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Re-usable building blocks</p>
</li>
<li>
<p>Publicly available reference models</p>
</li>
<li>
<p>Organization-specific reference models</p>
</li>
<li>
<p>Organization standards</p>
</li>
</ul>
</div>
</li>
<li>
<p>Draft Architecture Definition Document, which may include Baseline
and/or Target Architectures of any architecture domain</p>
</li>
<li>
<p>Draft Architecture Requirements Specification (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Gap analysis results (from Business, Data, and Application
Architectures)</p>
</li>
<li>
<p>Relevant technical requirements from previous phases</p>
</li>
</ul>
</div>
</li>
<li>
<p>Business, Data, and Application Architecture components of an
Architecture Roadmap (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
</ul>

### 8.3. Steps

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

<ul>
<li>
<p>Select reference models, viewpoints, and tools; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_08_03_01">Section 8.3.1, “Select Reference Models, Viewpoints, and Tools”</a></p>
</li>
<li>
<p>Develop Baseline Technology Architecture Description; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_08_03_02">Section 8.3.2, “Develop Baseline Technology Architecture Description”</a></p>
</li>
<li>
<p>Develop Target Technology Architecture Description; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_08_03_03">Section 8.3.3, “Develop Target Technology Architecture Description”</a></p>
</li>
<li>
<p>Perform gap analysis; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_08_03_04">Section 8.3.4, “Perform Gap Analysis”</a></p>
</li>
<li>
<p>Define candidate roadmap components; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_08_03_05">Section 8.3.5, “Define Candidate Roadmap Components”</a></p>
</li>
<li>
<p>Resolve impacts across the Architecture Landscape; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_08_03_06">Section 8.3.6, “Resolve Impacts Across the Architecture Landscape”</a></p>
</li>
<li>
<p>Conduct formal stakeholder review; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_08_03_07">Section 8.3.7, “Conduct Formal Stakeholder Review”</a></p>
</li>
<li>
<p>Finalize the Technology Architecture; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_08_03_08">Section 8.3.8, “Finalize the Technology Architecture”</a></p>
</li>
<li>
<p>Create/Update the Architecture Definition Document; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_08_03_09">Section 8.3.9, “Create/Update the Architecture Definition Document”</a></p>
</li>
</ul>

#### 8.3.1. Select Reference Models, Viewpoints, and Tools

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

##### 8.3.1.1. Determine Overall Modeling Process

For each viewpoint, select the models needed to support the specific
view required, using the selected tool or method. Ensure that all
stakeholder concerns are covered. If they are not, create new models to
address them, or augment existing models (see above).

The process to develop a Technology Architecture incorporates the
following steps:

<ul>
<li>
<p>Define a taxonomy of technology services and logical technology
components (including standards)</p>
</li>
<li>
<p>Identify relevant locations where technology is deployed</p>
</li>
<li>
<p>Carry out a physical inventory of deployed technology and abstract up
to fit into the taxonomy</p>
</li>
<li>
<p>Look at application and business requirements for technology</p>
</li>
<li>
<p>Is the technology in place fit-for-purpose to meet new requirements
(i.e., does it meet functional and non-functional requirements)?</p>
<div class="ulist">
<ul>
<li>
<p>Refine the taxonomy</p>
</li>
<li>
<p>Product selection (including dependent products)</p>
</li>
</ul>
</div>
</li>
<li>
<p>Determine configuration of the selected technology</p>
</li>
<li>
<p>Determine impact:</p>
<div class="ulist">
<ul>
<li>
<p>Sizing and costing</p>
</li>
<li>
<p>Capacity planning</p>
</li>
<li>
<p>Installation/governance/migration impacts</p>
</li>
</ul>
</div>
</li>
</ul>

In the earlier phases of the ADM, certain decisions made around service
granularity and service boundaries will have implications on the
technology component and the technology service. The areas where the
Technology Architecture may be impacted will include the following:

<ul>
<li>
<p><strong>Performance</strong>: the granularity of the service will impact on
technology service requirements</p>
<div class="paragraph">
<p>Coarse-grained services contain several units of functionality with
potentially varying non-functional requirements, so platform performance
should be considered. In addition, coarse-grained services can sometimes
contain more information than actually required by the requesting
system.</p>
</div>
</li>
<li>
<p><strong>Maintainability</strong>: if service granularity is too coarse, then
introducing changes to that service becomes difficult and impacts the
maintenance of the service and the platform on which it is delivered</p>
</li>
<li>
<p><strong>Location and Latency</strong>: services might interact with each other over
remote links and inter-service communication will have in-built latency</p>
<div class="paragraph">
<p>Drawing service boundaries and setting the service granularity should
consider platform/location impact of these inter-service communications.</p>
</div>
</li>
<li>
<p><strong>Availability</strong>: service invocation is subject to network and/or
service failure</p>
<div class="paragraph">
<p>High communication availability is an important consideration during
service decomposition and defining service granularity.</p>
</div>
</li>
</ul>

Product selection processes may occur within the Technology Architecture
phase where existing products are re-used, incremental capacity is being
added, or product selection decisions are a constraint during project
initiation.

Where product selection deviates from existing standards, involves
significant effort, or has wide-ranging impact, this activity should be
flagged as an opportunity and addressed through the Opportunities &
Solutions phase.

##### 8.3.1.2. Identify Required Catalogs of Technology Building Blocks

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

<ul>
<li>
<p>Based on existing technology catalogs and analysis of applications
carried out in the Application Architecture phase, collect a list of
products in use</p>
</li>
<li>
<p>If the requirements identified in the Application Architecture are not
met by existing products, extend the product list by examining products
available on the market that provide the functionality and meet the
required standards</p>
</li>
<li>
<p>Classify products against the selected taxonomy if appropriate,
extending the model as necessary to fit the classification of technology
products in use</p>
</li>
<li>
<p>If technology standards are currently in place, apply these to the
technology component catalog to gain a baseline view of compliance with
technology standards</p>
</li>
</ul>

The TOGAF Standard — Architecture Content contains a detailed description of catalogs which
should be considered for development within a Technology Architecture,
describing them in detail and relating them to entities, attributes, and
relationships in the TOGAF Enterprise Metamodel.

##### 8.3.1.3. Identify Required Matrices

Matrices show the core relationships between related model entities.

Matrices form the raw material for development of diagrams and also act
as a key resource for impact assessment.

The TOGAF Standard — Architecture Content contains a detailed description of matrices which
should be considered for development within a Technology Architecture,
describing them in detail and relating them to entities, attributes, and
relationships in the TOGAF Enterprise Metamodel.

##### 8.3.1.4. Identify Required Diagrams

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

##### 8.3.1.5. Identify Types of Requirement to be Collected

Once the Technology Architecture catalogs, matrices, and diagrams have
been developed, architecture modeling is completed by formalizing the
technology-focused requirements for implementing the Target Architecture.

These requirements may:

<ul>
<li>
<p>Relate to the technology domain</p>
</li>
<li>
<p>Provide detailed guidance to be reflected during design and
implementation to ensure that the solution addresses the original
architecture requirements</p>
</li>
</ul>

Within this step, the architect should identify requirements that should
be met by the architecture; see Section 13.5.2, “Requirements Development” .

##### 8.3.1.6. Select Services

The services portfolios are combinations of basic services from the
service categories in the defined taxonomy that do not conflict. The
combination of services are again tested to ensure support for the
applications. This is a prerequisite to the later step of defining the
architecture fully.

The previously identified requirements can provide more detailed
information about:

<ul>
<li>
<p>Requirements for organization-specific elements or pre-existing
decisions (as applicable)</p>
</li>
<li>
<p>Pre-existing and unchanging organizational elements (as applicable)</p>
</li>
<li>
<p>Inherited external environment constraints</p>
</li>
</ul>

Where requirements demand definition of specialized services that are
not identified in the TOGAF Standard, consideration should be given to
how these might be replaced if standardized services become available in
the future.

For each building block, build up a service description portfolio as a
set of non-conflicting services. The set of services must be tested to
ensure that the functionality provided meets application requirements.

#### 8.3.2. Develop Baseline Technology Architecture Description

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

#### 8.3.3. Develop Target Technology Architecture Description

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

#### 8.3.4. Perform Gap Analysis

Verify the architecture models for internal consistency and accuracy:

<ul>
<li>
<p>Perform trade-off analysis to resolve conflicts (if any) among the
different views</p>
</li>
<li>
<p>Validate that the models support the principles, objectives, and
constraints</p>
</li>
<li>
<p>Note changes to the viewpoint represented in the selected models from
the Architecture Repository, and document</p>
</li>
<li>
<p>Test architecture models for completeness against requirements</p>
</li>
</ul>

Identify gaps between the baseline and target, using the gap analysis
technique as described in the TOGAF Standard — ADM Techniques .

#### 8.3.5. Define Candidate Roadmap Components

Following the creation of a Baseline Architecture, Target Architecture,
and gap analysis, a Technology Roadmap is required to prioritize
activities over the coming phases.

This initial Technology Architecture roadmap will be used as raw
material to support more detailed definition of a consolidated,
cross-discipline roadmap within the Opportunities & Solutions phase.

#### 8.3.6. Resolve Impacts Across the Architecture Landscape

Once the Technology Architecture is finalized, it is necessary to
understand any wider impacts or implications.

At this stage, other architecture artifacts in the Architecture
Landscape should be examined to identify:

<ul>
<li>
<p>Does this Technology Architecture create an impact on any pre-existing
architectures?</p>
</li>
<li>
<p>Have recent changes been made that impact the Technology Architecture?</p>
</li>
<li>
<p>Are there any opportunities to leverage work from this Technology
Architecture in other areas of the organization?</p>
</li>
<li>
<p>Does this Technology Architecture impact other projects (including those planned as well as those currently in progress)?</p>
</li>
<li>
<p>Will this Technology Architecture be impacted by other projects
(including those planned as well as those currently in progress)?</p>
</li>
</ul>

#### 8.3.7. Conduct Formal Stakeholder Review

Check the original motivation for the architecture project and the
Statement of Architecture Work against the proposed Technology
Architecture, asking if it is fit for the purpose of supporting
subsequent work in the other architecture domains. Refine the proposed
Technology Architecture only if necessary.

#### 8.3.8. Finalize the Technology Architecture

<ul>
<li>
<p>Select standards for each of the building blocks, re-using as much as
possible from the reference models selected from the Architecture
Repository</p>
</li>
<li>
<p>Fully document each building block</p>
</li>
<li>
<p>Conduct a final cross-check of overall architecture against business
goals; document the rationale for building block decisions in the
architecture document</p>
</li>
<li>
<p>Document the final requirements traceability report</p>
</li>
<li>
<p>Document the final mapping of the architecture within the Architecture
Repository; from the selected building blocks, identify those that might
be re-used (working practices, roles, business relationships, job
descriptions, etc.), and publish via the Architecture Repository</p>
</li>
<li>
<p>Finalize all the work products, such as gap analysis</p>
</li>
</ul>

#### 8.3.9. Create/Update the Architecture Definition Document

Document the rationale for building block decisions in the Architecture
Definition Document.

Prepare the technology sections of the Architecture Definition Document,
comprising some or all of:

<ul>
<li>
<p>Fundamental functionality and attributes — semantic, unambiguous
including security capability and manageability</p>
</li>
<li>
<p>Dependent building blocks with required functionality and named
interfaces</p>
</li>
<li>
<p>Interfaces — chosen set, supplied (APIs, data formats, protocols,
hardware interfaces, standards)</p>
</li>
<li>
<p>Map to business/organizational entities and policies</p>
</li>
</ul>

If appropriate, use reports and/or graphics generated by modeling tools
to demonstrate key views of the architecture. Route the document for
review by relevant stakeholders, and incorporate feedback.

### 8.4. Outputs

The outputs of Phase D may include, but are not restricted to:

<ul>
<li>
<p>Refined and updated versions of the Architecture Vision phase
deliverables, where applicable:</p>
<div class="ulist">
<ul>
<li>
<p>Statement of Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), updated if necessary</p>
</li>
<li>
<p>Validated technology principles, or new technology principles (if
generated here)</p>
</li>
</ul>
</div>
</li>
<li>
<p>Draft Architecture Definition Document (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Baseline Technology Architecture, Approved, if appropriate</p>
</li>
<li>
<p>Target Technology Architecture, Approved, including:</p>
<div class="ulist">
<ul>
<li>
<p>Technology Components and their relationships to information systems</p>
</li>
<li>
<p>Technology platforms and their decomposition, showing the
combinations of technology required to realize a particular technology
“stack”</p>
</li>
<li>
<p>Environments and locations — a grouping of the required technology
into computing environments (e.g., development, production)</p>
</li>
<li>
<p>Expected processing load and distribution of load across technology
components</p>
</li>
<li>
<p>Physical (network) communications</p>
</li>
<li>
<p>Hardware and network specifications</p>
</li>
</ul>
</div>
</li>
<li>
<p>Views corresponding to the selected viewpoints addressing key
stakeholder concerns</p>
</li>
</ul>
</div>
</li>
<li>
<p>Draft Architecture Requirements Specification (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including such Technology Architecture requirements as:</p>
<div class="ulist">
<ul>
<li>
<p>Gap analysis results</p>
</li>
<li>
<p>Requirements output from Phases B and C</p>
</li>
<li>
<p>Updated technology requirements</p>
</li>
</ul>
</div>
</li>
<li>
<p>Technology Architecture components of an Architecture Roadmap (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
</ul>

The TOGAF Standard — Architecture Content contains a detailed description of architectural
artifacts which might be produced in this phase.

### 8.5. Approach

#### 8.5.1. Emerging Technologies

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

#### 8.5.2. Architecture Repository

As part of Phase D, the architecture team will need to consider what
relevant Technology Architecture resources are available in the
Architecture Repository (see the TOGAF Standard — Architecture Content ).

In particular:

<ul>
<li>
<p>Existing IT services as documented in the IT repository or IT service
catalog</p>
</li>
<li>
<p>The adopted technical reference model, if applicable</p>
</li>
<li>
<p>Generic technology models relevant to the organization’s industry
sector</p>
</li>
<li>
<p>Technology models relevant to Common Systems Architectures</p>
<div class="ulist">
<ul>
<li>
<p>The Open Group has a Reference Model for Integrated Information
Infrastructure (III-RM) — see the
<a href="https://pubs.opengroup.org/togaf-standard/reference-models/iiirm.html">TOGAF<sup>®</sup> Series Guide: The TOGAF Integrated Information Infrastructure Reference Model (III-RM)</a> — that focuses on the application-level components and underlying services
necessary to provide an integrated information infrastructure</p>
</li>
</ul>
</div>
</li>
</ul>

## 9. Phase E: Opportunities & Solutions

This chapter describes the process of identifying delivery vehicles
(projects, programs, or portfolios) that effectively deliver the Target
Architecture identified in previous phases.

![Phase E: Opportunities & Solutions](assets/005-e_opp.png)

Figure 9-1: Phase E: Opportunities & Solutions

### 9.1. Objectives

The objectives of Phase E are to:

<ul>
<li>
<p>Generate the initial complete version of the Architecture Roadmap,
based upon the gap analysis and candidate Architecture Roadmap
components from Phases B, C, and D</p>
</li>
<li>
<p>Determine whether an incremental approach is required, and if so
identify Transition Architectures that will deliver continuous business
value</p>
</li>
<li>
<p>Define the overall Solution Building Blocks (SBBs) to finalize the
Target Architecture based on the ABBs</p>
</li>
</ul>

### 9.2. Inputs

This section defines the inputs to Phase E.

#### 9.2.1. Reference Materials External to the Enterprise

<ul>
<li>
<p>Architecture reference materials (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Product information</p>
</li>
</ul>

#### 9.2.2. Non-Architectural Inputs

<ul>
<li>
<p>Request for Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Capability Assessment (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Communications Plan (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Planning methodologies</p>
</li>
</ul>

#### 9.2.3. Architectural Inputs

<ul>
<li>
<p>Organizational Model for Enterprise Architecture (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Scope of organizations impacted</p>
</li>
<li>
<p>Maturity assessment, gaps, and resolution approach</p>
</li>
<li>
<p>Roles and responsibilities for architecture team(s)</p>
</li>
<li>
<p>Constraints on architecture work</p>
</li>
<li>
<p>Budget requirements</p>
</li>
<li>
<p>Governance and support strategy</p>
</li>
</ul>
</div>
</li>
<li>
<p>Governance models and frameworks for:</p>
<div class="ulist">
<ul>
<li>
<p>Corporate Business Planning</p>
</li>
<li>
<p>Enterprise Architecture</p>
</li>
<li>
<p>Portfolio, Program, Project Management</p>
</li>
<li>
<p>System Development/Engineering</p>
</li>
<li>
<p>Operations (Service)</p>
</li>
</ul>
</div>
</li>
<li>
<p>Tailored Architecture Framework (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Tailored architecture method</p>
</li>
<li>
<p>Tailored architecture content (deliverables and artifacts)</p>
</li>
<li>
<p>Configured and deployed tools</p>
</li>
</ul>
</div>
</li>
<li>
<p>Statement of Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Architecture Vision (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Architecture Repository (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Re-usable building blocks</p>
</li>
<li>
<p>Publicly available reference models</p>
</li>
<li>
<p>Organization-specific reference models</p>
</li>
<li>
<p>Organization standards</p>
</li>
</ul>
</div>
</li>
<li>
<p>Draft Architecture Definition Document, which may include Baseline
and/or Target Architectures of any architecture domain</p>
</li>
<li>
<p>Draft Architecture Requirements Specification (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Architectural requirements</p>
</li>
<li>
<p>Gap analysis results (from Business, Data, Application, and
Technology Architecture)</p>
</li>
<li>
<p>IT Service Management requirements</p>
</li>
</ul>
</div>
</li>
<li>
<p>Change Requests for existing business programs and projects (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Candidate Architecture Roadmap components from Phases B, C, and D</p>
</li>
</ul>

### 9.3. Steps

The level of detail addressed in Phase E will depend on the scope and
goals of the overall architecture effort.

The order of the steps in Phase E as well as the time at which they are
formally started and completed should be adapted to the situation at
hand in accordance with the established Architecture Governance.

All activities that have been initiated in these steps must be closed
during the Create the Architecture Roadmap & Implementation and
Migration Plan step; see Section 9.3.11, “Create the Architecture Roadmap & Implementation and Migration Plan” .

The steps in Phase E are as follows:

<ul>
<li>
<p>Determine/confirm key corporate change attributes; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_09_03_01">Section 9.3.1, “Determine/Confirm Key Corporate Change Attributes”</a></p>
</li>
<li>
<p>Determine business constraints for implementation; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_09_03_02">Section 9.3.2, “Determine Business Constraints for Implementation”</a></p>
</li>
<li>
<p>Review and consolidate gap analysis results from Phases B to D; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_09_03_03">Section 9.3.3, “Review and Consolidate Gap Analysis Results from Phases B to D”</a></p>
</li>
<li>
<p>Review consolidated requirements across related business functions; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_09_03_04">Section 9.3.4, “Review Consolidated Requirements Across Related Business Functions”</a></p>
</li>
<li>
<p>Consolidate and reconcile interoperability requirements; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_09_03_05">Section 9.3.5, “Consolidate and Reconcile Interoperability Requirements”</a></p>
</li>
<li>
<p>Refine and validate dependencies; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_09_03_06">Section 9.3.6, “Refine and Validate Dependencies”</a></p>
</li>
<li>
<p>Confirm readiness and risk for business transformation; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_09_03_07">Section 9.3.7, “Confirm Readiness and Risk for Business Transformation”</a></p>
</li>
<li>
<p>Formulate Implementation and Migration Strategy; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_09_03_08">Section 9.3.8, “Formulate Implementation and Migration Strategy”</a></p>
</li>
<li>
<p>Identify and group major work packages; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_09_03_09">Section 9.3.9, “Identify and Group Major Work Packages”</a></p>
</li>
<li>
<p>Identify Transition Architectures; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_09_03_10">Section 9.3.10, “Identify Transition Architectures”</a></p>
</li>
<li>
<p>Create the Architecture Roadmap &amp; Implementation and Migration Plan; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_09_03_11">Section 9.3.11, “Create the Architecture Roadmap &amp; Implementation and Migration Plan”</a></p>
</li>
</ul>

#### 9.3.1. Determine/Confirm Key Corporate Change Attributes

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

#### 9.3.2. Determine Business Constraints for Implementation

Identify any business drivers that would constrain the sequence of
implementation. This should include a review of the business and
strategic plans, at both a corporate and line-of-business level, and a
review of the Enterprise Architecture Maturity Assessment.

#### 9.3.3. Review and Consolidate Gap Analysis Results from Phases B to D

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

#### 9.3.4. Review Consolidated Requirements Across Related Business Functions

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

#### 9.3.5. Consolidate and Reconcile Interoperability Requirements

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

#### 9.3.6. Refine and Validate Dependencies

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

#### 9.3.7. Confirm Readiness and Risk for Business Transformation

Review the findings of the Business Transformation Readiness Assessment
previously conducted in Phase A and determine their impact on the
Architecture Roadmap and the Implementation and Migration Strategy. It
is important to identify, classify, and mitigate risks associated with
the transformation effort. Risks should be documented in the
Consolidated Gaps, Solutions, and Dependencies matrix.

#### 9.3.8. Formulate Implementation and Migration Strategy

Create an overall Implementation and Migration Strategy that will guide
the implementation of the Target Architecture, and structure any
Transition Architectures. The first activity is to determine an overall
strategic approach to implementing the solutions and/or exploiting
opportunities. There are three basic approaches as follows:

<ul>
<li>
<p>Greenfield: a completely new implementation</p>
</li>
<li>
<p>Revolutionary: a radical change (i.e., switch on, switch off)</p>
</li>
<li>
<p>Evolutionary: a strategy of convergence, such as parallel running or a
phased approach to introduce new capabilities</p>
</li>
</ul>

Next, determine an approach for the overall strategic direction that
will address and mitigate the risks identified in the Consolidated Gaps,
Solutions, and Dependencies matrix. The most common implementation
methodologies are:

<ul>
<li>
<p>Quick win (snapshots)</p>
</li>
<li>
<p>Achievable targets</p>
</li>
<li>
<p>Value chain method</p>
</li>
</ul>

These approaches and the identified dependencies should become the basis
for the creation of the work packages. This activity terminates with
agreement on the Implementation and Migration Strategy for the
enterprise.

#### 9.3.9. Identify and Group Major Work Packages

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

<ul>
<li>
<p>Mainstream: part of the future information system</p>
</li>
<li>
<p>Contain: expected to be replaced or modified in the planning horizon
(next three years)</p>
</li>
<li>
<p>Replace: to be replaced in the planning horizon</p>
</li>
</ul>

Supporting top-level work packages should then in turn be decomposed
into increments to deliver the capability increments. Analyze and refine
these work packages or increments with respect to their business
transformation issues and the strategic implementation approach.
Finally, group the work packages into portfolios and projects within a
portfolio, taking into consideration the dependencies and the strategic
implementation approach.

#### 9.3.10. Identify Transition Architectures

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

#### 9.3.11. Create the Architecture Roadmap & Implementation and Migration Plan

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

### 9.4. Outputs

The outputs of Phase E may include, but are not restricted to:

<ul>
<li>
<p>Refined and updated version of the Architecture Vision phase
deliverables, where applicable, including:</p>
<div class="ulist">
<ul>
<li>
<p>Architecture Vision, including definition of types and degrees of
interoperability</p>
</li>
<li>
<p>Statement of Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), updated if necessary</p>
</li>
</ul>
</div>
</li>
<li>
<p>Draft Architecture Definition Document (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Baseline Business Architecture, Approved, updated if necessary</p>
</li>
<li>
<p>Target Business Architecture, Approved, updated if necessary</p>
</li>
<li>
<p>Baseline Data Architecture, Approved, updated if necessary</p>
</li>
<li>
<p>Target Data Architecture, Approved, updated if necessary</p>
</li>
<li>
<p>Baseline Application Architecture, Approved, updated if necessary</p>
</li>
<li>
<p>Target Application Architecture, Approved, updated if necessary</p>
</li>
<li>
<p>Baseline Technology Architecture, Approved, updated if necessary</p>
</li>
<li>
<p>Target Technology Architecture, Approved, updated if necessary</p>
</li>
<li>
<p>Transition Architecture, number and scope as necessary</p>
</li>
<li>
<p>Views corresponding to the selected viewpoints addressing key
stakeholder concerns</p>
</li>
</ul>
</div>
</li>
<li>
<p>Draft Architecture Requirements Specification (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Consolidated Gaps, Solutions, and Dependencies Assessment</p>
</li>
</ul>
</div>
</li>
<li>
<p>Capability Assessments, including:</p>
<div class="ulist">
<ul>
<li>
<p>Business Capability Assessment</p>
</li>
<li>
<p>IT Capability Assessment</p>
</li>
</ul>
</div>
</li>
<li>
<p>Architecture Roadmap (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Work package portfolio:</p>
<div class="ulist">
<ul>
<li>
<p>Work package description (name, description, objectives)</p>
</li>
<li>
<p>Functional requirements</p>
</li>
<li>
<p>Dependencies</p>
</li>
<li>
<p>Relationship to opportunity</p>
</li>
<li>
<p>Relationship to Architecture Definition Document and Architecture
Requirements Specification</p>
</li>
<li>
<p>Relationship to any capability increments</p>
</li>
<li>
<p>Business value</p>
</li>
<li>
<p>Implementation Factor catalog</p>
</li>
<li>
<p>Impact</p>
</li>
</ul>
</div>
</li>
<li>
<p>Identification of Transition Architectures, if any, including:</p>
<div class="ulist">
<ul>
<li>
<p>Relationship to Architecture Definition Document</p>
</li>
</ul>
</div>
</li>
<li>
<p>Implementation recommendations:</p>
<div class="ulist">
<ul>
<li>
<p>Criteria measures of effectiveness</p>
</li>
<li>
<p>Risks and issues</p>
</li>
<li>
<p>Solution Building Blocks (SBBs)</p>
</li>
</ul>
</div>
</li>
</ul>
</div>
</li>
<li>
<p>Implementation and Migration Plan, Draft, including:</p>
<div class="ulist">
<ul>
<li>
<p>Implementation and Migration Strategy</p>
</li>
</ul>
</div>
</li>
</ul>

The TOGAF Standard — Architecture Content contains a detailed description of architectural
artifacts which might be produced in this phase, describing them in
detail and relating them to entities, attributes, and relationships in
the TOGAF Enterprise Metamodel.

### 9.5. Approach

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

<ul>
<li>
<p>Architecture Roadmap</p>
</li>
<li>
<p>Work Packages</p>
</li>
<li>
<p>Transition Architectures</p>
</li>
<li>
<p>Implementation and Migration Plan</p>
</li>
</ul>

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

## 10. Phase F: Migration Planning

This chapter addresses migration planning; that is, how to move from the
Baseline to the Target Architectures by finalizing a detailed
Implementation and Migration Plan.

![Phase F: Migration Planning](assets/004-f_mig.png)

Figure 10-1: Phase F: Migration Planning

### 10.1. Objectives

The objectives of Phase F are to:

<ul>
<li>
<p>Finalize the Architecture Roadmap and the supporting Implementation and Migration Plan</p>
</li>
<li>
<p>Ensure that the Implementation and Migration Plan is co-ordinated with the enterprise’s approach to managing and implementing change in the enterprise’s overall change portfolio</p>
</li>
<li>
<p>Ensure that the business value and cost of work packages and
Transition Architectures is understood by key stakeholders</p>
</li>
</ul>

### 10.2. Inputs

This section defines the inputs to Phase F.

#### 10.2.1. Reference Materials External to the Enterprise

<ul>
<li>
<p>Architecture reference materials (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
</ul>

#### 10.2.2. Non-Architectural Inputs

<ul>
<li>
<p>Request for Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Capability Assessment (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Communications Plan (see <a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
</ul>

#### 10.2.3. Architectural Inputs

<ul>
<li>
<p>Organizational Model for Enterprise Architecture (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Scope of organizations impacted</p>
</li>
<li>
<p>Maturity assessment, gaps, and resolution approach</p>
</li>
<li>
<p>Roles and responsibilities for architecture team(s)</p>
</li>
<li>
<p>Constraints on architecture work</p>
</li>
<li>
<p>Budget requirements</p>
</li>
<li>
<p>Governance and support strategy</p>
</li>
</ul>
</div>
</li>
<li>
<p>Governance models and frameworks for:</p>
<div class="ulist">
<ul>
<li>
<p>Corporate Business Planning</p>
</li>
<li>
<p>Enterprise Architecture</p>
</li>
<li>
<p>Portfolio, Program, Project Management<br/></p>
</li>
<li>
<p>System Development/Engineering</p>
</li>
<li>
<p>Operations (Service)</p>
</li>
</ul>
</div>
</li>
<li>
<p>Tailored Architecture Framework (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Tailored architecture method</p>
</li>
<li>
<p>Tailored architecture content (deliverables and artifacts)</p>
</li>
<li>
<p>Configured and deployed tools</p>
</li>
</ul>
</div>
</li>
<li>
<p>Statement of Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Architecture Vision (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Architecture Repository (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Re-usable building blocks</p>
</li>
<li>
<p>Publicly available reference models</p>
</li>
<li>
<p>Organization-specific reference models</p>
</li>
<li>
<p>Organization standards</p>
</li>
</ul>
</div>
</li>
<li>
<p>Draft Architecture Definition Document, which may include Baseline
and/or Target Architectures of any architecture domain, and/or
Transition Architectures</p>
</li>
<li>
<p>Draft Architecture Requirements Specification (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Architectural requirements</p>
</li>
<li>
<p>Gap analysis results (from Business, Data, Application, and
Technology Architecture)</p>
</li>
<li>
<p>IT Service Management requirements</p>
</li>
</ul>
</div>
</li>
<li>
<p>Change Requests for existing business programs and projects (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Architecture Roadmap, Draft (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Identification of work packages</p>
</li>
<li>
<p>Identification of Transition Architectures</p>
</li>
<li>
<p>Implementation Factor catalog</p>
</li>
</ul>
</div>
</li>
<li>
<p>Capability Assessment (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Business Capability Assessment</p>
</li>
<li>
<p>IT Capability Assessment</p>
</li>
</ul>
</div>
</li>
<li>
<p>Implementation and Migration Plan, Draft (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including the high-level Implementation and Migration
Strategy</p>
</li>
</ul>

### 10.3. Steps

The level of detail addressed in Phase F will depend on the scope and
goals of the overall architecture effort.

The order of the steps in Phase F as well as the time at which they are
formally started and completed should be adapted to the situation at
hand in accordance with the established Architecture Governance.

All activities that have been initiated in these steps must be closed
during the “Complete the Architecture Development Cycle and Document
Lessons Learned” step; see Section 10.3.7, “Complete the Architecture Development Cycle and Document Lessons Learned” .

The steps in Phase F are as follows:

<ul>
<li>
<p>Confirm management framework interactions for Implementation and
Migration Plan; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_10_03_01">Section 10.3.1, “Confirm Management Framework Interactions for the Implementation and Migration Plan”</a></p>
</li>
<li>
<p>Assign a business value to each work package; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_10_03_02">Section 10.3.2, “Assign a Business Value to Each Work Package”</a></p>
</li>
<li>
<p>Estimate resource requirements, project timings, and availability/delivery vehicle; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_10_03_03">Section 10.3.3, “Estimate Resource Requirements, Project Timings, and Availability/Delivery Vehicle”</a></p>
</li>
<li>
<p>Prioritize the migration projects by conducting a cost/benefit assessment and risk assessment; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_10_03_04">Section 10.3.4, “Prioritize the Migration Projects by Conducting a Cost/Benefit Assessment and Risk Assessment”</a></p>
</li>
<li>
<p>Confirm Architecture Roadmap and update Architecture Definition Document; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_10_03_05">Section 10.3.5, “Confirm Architecture Roadmap and Update Architecture Definition Document”</a></p>
</li>
<li>
<p>Complete the Implementation and Migration Plan; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_10_03_06">Section 10.3.6, “Complete the Implementation and Migration Plan”</a></p>
</li>
<li>
<p>Complete the architecture development cycle and document lessons learned; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_10_03_07">Section 10.3.7, “Complete the Architecture Development Cycle and Document Lessons Learned”</a></p>
</li>
</ul>

#### 10.3.1. Confirm Management Framework Interactions for the Implementation and Migration Plan

This step is about co-ordinating the Implementation and Migration Plan
with the management frameworks within the organization. There are
typically four management frameworks that have to work closely together
for the Implementation and Migration Plan to succeed:

<ul>
<li>
<p><strong>Business Planning</strong> that conceives, directs, and provides the
resources for all of the activities required to achieve concrete
business objectives/outcomes</p>
</li>
<li>
<p><strong>Enterprise Architecture</strong> that structures and gives context to all
enterprise activities delivering concrete business outcomes primarily
but not exclusively in the IT domain</p>
</li>
<li>
<p><strong>Project/Portfolio Management</strong> that co-ordinates, designs, and builds
the business systems that deliver the concrete business outcomes</p>
</li>
<li>
<p><strong>Operations Management</strong> that integrates, operates, and maintains the
deliverables that deliver the concrete business outcomes</p>
</li>
</ul>

The Implementation and Migration Plan will impact the outputs of each of
these frameworks and consequently has to be reflected in them. In the
course of this step, understand the frameworks within the organization
and ensure that these plans are co-ordinated and inserted (in a summary
format) within the plans of each one of these frameworks.

The outcome of this step may well be that the Implementation and
Migration Plan could be part of a different plan produced by another one
of the frameworks with Enterprise Architecture participation.

#### 10.3.2. Assign a Business Value to Each Work Package

Establish and assign a business value to each of the work packages. The
intent is to first establish what constitutes business value within the
organization, how value can be measured, and then apply this to each one
of the projects and project increments.

There are several issues to address in this activity:

<ul>
<li>
<p><strong>Performance Evaluation Criteria</strong> are used by portfolio and capability
managers to approve and monitor the progress of the architecture
transformation</p>
</li>
<li>
<p><strong>Return-on-Investment Criteria</strong> have to be detailed and signed off by
the various executive stakeholders</p>
</li>
<li>
<p><strong>Business Value</strong> has to be defined as well as techniques, such as the
value chain, which are to be used to illustrate the role in achieving
tangible business outcomes</p>
<div class="paragraph">
<p>Business value will be used by portfolio and capability managers to
allocate resources and, in cases where there are cutbacks, business
value in conjunction with return on investment can be used to determine
whether an endeavor proceeds, is delayed, or is canceled.</p>
</div>
</li>
<li>
<p><strong>Critical Success Factors (CSFs)</strong> should be established to define
success for a project and/or project increment</p>
<div class="paragraph">
<p>These will provide managers and implementers with a gauge as to what
constitutes a successful implementation.</p>
</div>
</li>
<li>
<p><strong>Measures of Effectiveness (MOE)</strong> are often performance criteria and
many corporations include them in the CSFs</p>
<div class="paragraph">
<p>Where they are treated discretely, it should be clear as to how these
criteria are to be grouped.</p>
</div>
</li>
<li>
<p><strong>Strategic Fit</strong> based upon the overall Enterprise Architecture (all
tiers) will be the critical factor for allowing the approval of any new
project or initiative and for determining the value of any deliverable</p>
</li>
</ul>

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

#### 10.3.3. Estimate Resource Requirements, Project Timings, and Availability/Delivery Vehicle

This step determines the required resources and times for each project
and their increments and provides the initial cost estimates. The costs
should be broken down into capital (to create the capability) and
operations and maintenance (to run and sustain the capability).
Opportunities should be identified where the costs associated with
delivering new and/or better capability can be offset by decommissioning
existing systems. Assign required resources to each activity and
aggregate them at the project increment and project level.

#### 10.3.4. Prioritize the Migration Projects by Conducting a Cost/Benefit Assessment and Risk Assessment

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

#### 10.3.5. Confirm Architecture Roadmap and Update Architecture Definition Document

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

#### 10.3.6. Complete the Implementation and Migration Plan

Generate the completed Implementation and Migration Plan. Much of the
detail for the plan has already been gathered and this step brings it
all together using accepted planning and management techniques. This
should include integrating all of the projects and activities as well as
dependencies and impact of change into a project plan. Any Transition
Architectures will act as portfolio milestones.

All external dependencies should be captured and included, and the
overall availability of resources assessed. Project plans may be
included within the Implementation and Migration Plan.

#### 10.3.7. Complete the Architecture Development Cycle and Document Lessons Learned

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

### 10.4. Outputs

The outputs of Phase F may include, but are not restricted to:

<ul>
<li>
<p>Implementation and Migration Plan, Approved (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Implementation and Migration Strategy</p>
</li>
<li>
<p>Project and portfolio breakdown of the implementation:</p>
<div class="ulist">
<ul>
<li>
<p>Allocation of work packages to project and portfolio</p>
</li>
<li>
<p>Capabilities delivered by projects</p>
</li>
<li>
<p>Relationship to Target Architecture and any Transition Architectures</p>
</li>
<li>
<p>Milestones and timing</p>
</li>
<li>
<p>Work breakdown structure</p>
</li>
</ul>
</div>
</li>
<li>
<p>Project charters (optional):</p>
<div class="ulist">
<ul>
<li>
<p>Related work packages</p>
</li>
<li>
<p>Business value</p>
</li>
<li>
<p>Risk, issues, assumptions, dependencies</p>
</li>
<li>
<p>Resource requirements and costs</p>
</li>
<li>
<p>Benefits of migration</p>
</li>
<li>
<p>Estimated costs of migration options</p>
</li>
</ul>
</div>
</li>
</ul>
</div>
</li>
<li>
<p>Finalized Architecture Definition Document (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Finalized Transition Architectures, if any</p>
</li>
</ul>
</div>
</li>
<li>
<p>Finalized Architecture Requirements Specification (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Finalized Architecture Roadmap (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Re-Usable ABBs (see the <a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Requests for Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>) for a new iteration of the ADM cycle (if any)</p>
</li>
<li>
<p>Implementation Governance Model (if any) (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Change Requests for the Architecture Capability arising from lessons
learned</p>
</li>
</ul>

### 10.5. Approach

The focus of Phase F is the creation of an Implementation and Migration
Plan in co-operation with the project and portfolio managers.

Phase E provides an incomplete Architecture Roadmap and Implementation and Migration Plan that address the Statement of Architecture Work. In
Phase F this Roadmap and the Implementation and Migration Plan are integrated with the enterprise’s other change activity.

Activities include assessing the dependencies, costs, and benefits of the various migration projects within the context of the enterprise’s
other activity. The Draft Architecture Roadmap, and Draft Implementation and Migration Plan, from Phase E will form the basis of the final
Implementation and Migration Plan that will include portfolio and project-level detail.

The architecture development cycle should then be completed and lessons learned documented to enable continuous process improvement.

## 11. Phase G: Implementation Governance

This chapter provides an architectural oversight of the implementation.

![Phase G: Implementation Governance](assets/003-g_gov.png)

Figure 11-1: Phase G: Implementation

### 11.1. Objectives

The objectives of Phase G are to:

<ul>
<li>
<p>Ensure conformance with the Target Architecture by implementation
projects</p>
</li>
<li>
<p>Perform appropriate Architecture Governance functions for the solution
and any implementation-driven architecture Change Requests</p>
</li>
</ul>

### 11.2. Inputs

This section defines the inputs to Phase G.

#### 11.2.1. Reference Materials External to the Enterprise

<ul>
<li>
<p>Architecture reference materials (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
</ul>

#### 11.2.2. Non-Architectural Inputs

<ul>
<li>
<p>Request for Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Capability Assessment (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
</ul>

#### 11.2.3. Architectural Inputs

<ul>
<li>
<p>Organizational Model for Enterprise Architecture (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Scope of organizations impacted</p>
</li>
<li>
<p>Maturity assessment, gaps, and resolution approach</p>
</li>
<li>
<p>Roles and responsibilities for architecture team(s)</p>
</li>
<li>
<p>Constraints on architecture work</p>
</li>
<li>
<p>Budget requirements</p>
</li>
<li>
<p>Governance and support strategy</p>
</li>
</ul>
</div>
</li>
<li>
<p>Tailored Architecture Framework (see
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Tailored architecture method</p>
</li>
<li>
<p>Tailored architecture content (deliverables and artifacts)</p>
</li>
<li>
<p>Configured and deployed tools</p>
</li>
</ul>
</div>
</li>
<li>
<p>Statement of Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Architecture Vision (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Architecture Repository (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Re-usable building blocks</p>
</li>
<li>
<p>Publicly available reference models</p>
</li>
<li>
<p>Organization-specific reference models</p>
</li>
<li>
<p>Organization standards</p>
</li>
</ul>
</div>
</li>
<li>
<p>Architecture Definition Document (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Architecture Requirements Specification (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Architectural requirements</p>
</li>
<li>
<p>Gap analysis results (from Business, Data, Application, and
Technology Architectures)</p>
</li>
</ul>
</div>
</li>
<li>
<p>Architecture Roadmap (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Architecture Governance Framework (see the
<a href="https://pubs.opengroup.org/togaf-standard/ea-capability-and-governance/chap01.html">TOGAF Standard — EA Capability and Governance</a>)</p>
</li>
<li>
<p>Implementation Governance Model (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Architecture Contract (standard) (see the
<a href="https://pubs.opengroup.org/togaf-standard/ea-capability-and-governance/chap01.html">TOGAF Standard — EA Capability and Governance</a>)</p>
</li>
<li>
<p>Request for Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>) identified during Phases E and F</p>
</li>
<li>
<p>Implementation and Migration Plan (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
</ul>

### 11.3. Steps

The level of detail addressed in Phase G will depend on the scope and
goals of the overall architecture effort.

The order of the steps in Phase G as well as the time at which they are
formally started and completed should be adapted to the situation at
hand in accordance with the established Architecture Governance.

The steps in Phase G are as follows:

<ul>
<li>
<p>Confirm scope and priorities for deployment with development management; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_11_03_01">Section 11.3.1, “Confirm Scope and Priorities for Deployment with Development Management”</a></p>
</li>
<li>
<p>Identify deployment resources and skills; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_11_03_02">Section 11.3.2, “Identify Deployment Resources and Skills”</a></p>
</li>
<li>
<p>Guide development of solutions deployment; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_11_03_03">Section 11.3.3, “Guide Development of Solutions Deployment”</a></p>
</li>
<li>
<p>Perform Enterprise Architecture Compliance reviews; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_11_03_04">Section 11.3.4, “Perform Enterprise Architecture Compliance Reviews”</a></p>
</li>
<li>
<p>Implement business and IT operations; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_11_03_05">Section 11.3.5, “Implement Business and IT Operations”</a></p>
</li>
<li>
<p>Perform post-implementation review and close the implementation; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_11_03_06">Section 11.3.6, “Perform Post-Implementation Review and Close the Implementation”</a></p>
</li>
</ul>

#### 11.3.1. Confirm Scope and Priorities for Deployment with Development Management

<ul>
<li>
<p>Review migration planning outputs and produce recommendations on
deployment</p>
</li>
<li>
<p>Identify Enterprise Architecture priorities for development teams</p>
</li>
<li>
<p>Identify deployment issues and make recommendations</p>
</li>
<li>
<p>Identify building blocks for replacement, update, etc.</p>
</li>
<li>
<p>Perform gap analysis on Enterprise Architecture and solutions
framework</p>
<div class="paragraph">
<p>The gaps in the existing enterprise solutions framework need to be
identified and the specific SBBs required to fill these gaps will be
identified by the Solution Architects. These SBBs may have a one-to-one
or many-to-one relationship with the projects. The Solution Architects
need to define exactly how this will be done. There may be other
projects working on these same capabilities and the Solution Architects
need to ensure that they can leverage best value from these investments.</p>
</div>
</li>
<li>
<p>Produce a gap analysis report</p>
</li>
</ul>

#### 11.3.2. Identify Deployment Resources and Skills

The project resources will include the development resources which will
need to be educated in the overall Enterprise Architecture deliverables
and expectations from the specific development and implementation
projects.

The following considerations should be addressed in this step:

<ul>
<li>
<p>Identify system development methods required for solutions development</p>
<div class="dlist">
<dl>
<dt class="hdlist1"><strong>Note:</strong></dt>
<dd>
<p>There are a range of systems development methods and tools available
to the project teams. The method should ideally be able to
interoperate with the architecture outputs; for example, generate code
from architecture artifacts delivered to date. This could be achieved
through the use of modeling languages used for the Enterprise
Architecture development that may be captured as inputs to the systems
development tools and thereby reduce the cost of solutions
development.</p>
</dd>
</dl>
</div>
</li>
<li>
<p>Ensure that the systems development method enables feedback to the
architecture team on designs</p>
</li>
</ul>

#### 11.3.3. Guide Development of Solutions Deployment

<ul>
<li>
<p>Formulate project recommendation</p>
<div class="paragraph">
<p>For each separate implementation and deployment project, do the
following:</p>
</div>
<div class="ulist">
<ul>
<li>
<p>Document scope of individual project in impact analysis</p>
</li>
<li>
<p>Document strategic requirements (from the architectural perspective)
in impact analysis</p>
</li>
<li>
<p>Document Change Requests (such as support for a standard interface)
in impact analysis</p>
</li>
<li>
<p>Document rules for conformance in impact analysis</p>
</li>
<li>
<p>Document timeline requirements from roadmap in impact analysis</p>
</li>
</ul>
</div>
</li>
<li>
<p>Document Architecture Contract</p>
<div class="ulist">
<ul>
<li>
<p>Obtain signature from all developing organizations and sponsoring
organization</p>
</li>
</ul>
</div>
</li>
<li>
<p>Update Enterprise Continuum directory and repository for solutions</p>
</li>
<li>
<p>Guide development of business &amp; IT operating models for services</p>
</li>
<li>
<p>Provide service requirements derived from Enterprise Architecture</p>
</li>
<li>
<p>Guide definition of business &amp; IT operational requirements</p>
</li>
<li>
<p>Carry out gap analysis between the Solution Architecture and
operations</p>
</li>
<li>
<p>Produce Implementation Plan</p>
</li>
</ul>

#### 11.3.4. Perform Enterprise Architecture Compliance Reviews

<ul>
<li>
<p>Review ongoing implementation governance and Architecture Compliance
for each building block</p>
</li>
<li>
<p>Conduct post-development reviews</p>
</li>
<li>
<p>Close development part of deployment projects</p>
</li>
</ul>

#### 11.3.5. Implement Business and IT Operations

<ul>
<li>
<p>Carry out the deployment projects including: IT services delivery
implementation; business services delivery implementation; skills
development &amp; training implementation; communications documentation
publication</p>
</li>
<li>
<p>Publish new Baseline Architectures to the Architecture Repository and
update other impacted repositories, such as operational configuration
management stores</p>
</li>
</ul>

#### 11.3.6. Perform Post-Implementation Review and Close the Implementation

<ul>
<li>
<p>Conduct post-implementation reviews</p>
</li>
<li>
<p>Publish reviews and close projects</p>
</li>
</ul>

Closure on Phase G will be when the solutions are fully deployed once.

### 11.4. Outputs

The outputs of Phase G may include, but are not restricted to:

<ul>
<li>
<p>Architecture Contract (signed) (see the
<a href="https://pubs.opengroup.org/togaf-standard/ea-capability-and-governance/chap01.html">TOGAF Standard — EA Capability and Governance</a>), as recommended in the
architecture-compliant implemented architectures</p>
</li>
<li>
<p>Compliance Assessments (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Change Requests (see the <a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Architecture-compliant solutions deployed including:</p>
<div class="ulist">
<ul>
<li>
<p>The architecture-compliant implemented system</p>
<div class="dlist">
<dl>
<dt class="hdlist1"><strong>Note:</strong></dt>
<dd>
<p>The implemented system is actually an output of the development
process. However, given the importance of this output, it is stated
here as an output of the ADM. The direct involvement of architecture
staff in implementation will vary according to organizational policy,
as described in the
<a href="https://pubs.opengroup.org/togaf-standard/ea-capability-and-governance/chap01.html">TOGAF Standard — EA Capability and Governance</a>.</p>
</dd>
</dl>
</div>
</li>
<li>
<p>Populated Architecture Repository</p>
</li>
<li>
<p>Architecture compliance recommendations and dispensations</p>
</li>
<li>
<p>Recommendations on service delivery requirements</p>
</li>
<li>
<p>Recommendations on performance metrics</p>
</li>
<li>
<p>Service-Level Agreements (SLAs)</p>
</li>
<li>
<p>Architecture Vision, updated post-implementation</p>
</li>
<li>
<p>Architecture Definition Document, updated post-implementation</p>
</li>
<li>
<p>Business and IT operating models for the implemented solution</p>
</li>
<li>
<p>Architecture Building Blocks (ABBs)</p>
</li>
</ul>
</div>
</li>
</ul>

### 11.5. Approach

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

<ul>
<li>
<p>Establish an implementation program that will enable the delivery of
the Transition Architectures agreed for implementation during the
Migration Planning phase</p>
</li>
<li>
<p>Adopt a phased deployment schedule that reflects the business
priorities embodied in the Architecture Roadmap</p>
</li>
<li>
<p>Follow the organization’s standard for corporate, IT, and Architecture
Governance</p>
</li>
<li>
<p>Use the organization’s established portfolio/program management
approach, where this exists</p>
</li>
<li>
<p>Define an operations framework to ensure the effective long life of
the deployed solution</p>
</li>
</ul>

Phase G establishes the connection between architecture and
implementation organization, through the Architecture Contract.

Project details are developed, including:

<ul>
<li>
<p>Name, description, and objectives</p>
</li>
<li>
<p>Scope, deliverables, and constraints</p>
</li>
<li>
<p>Measures of effectiveness</p>
</li>
<li>
<p>Acceptance criteria</p>
</li>
<li>
<p>Risks and issues</p>
</li>
</ul>

Implementation governance is closely allied to overall Architecture
Governance, which is discussed in the TOGAF Standard — EA Capability and Governance .

A key aspect of Phase G is ensuring compliance with the defined
architecture(s), not only by the implementation projects, but also by
other ongoing projects within the enterprise. The considerations
involved with this are explained in detail in the TOGAF Standard — EA Capability and Governance .

## 12. Phase H: Architecture Change Management

This chapter looks at establishing procedures for managing change to the
new architecture.

![Phase H: Architecture Change Management](assets/002-h_cha.png)

Figure 12-1: Phase H: Architecture Change Management

### 12.1. Objectives

The objectives of Phase H are to:

<ul>
<li>
<p>Ensure that the architecture development cycle is maintained</p>
</li>
<li>
<p>Ensure that the Architecture Governance Framework is executed</p>
</li>
<li>
<p>Ensure that the Enterprise Architecture Capability meets current
requirements</p>
</li>
</ul>

### 12.2. Inputs

This section defines the inputs to Phase H.

#### 12.2.1. Reference Materials External to the Enterprise

<ul>
<li>
<p>Architecture reference materials (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
</ul>

#### 12.2.2. Non-Architectural Inputs

<ul>
<li>
<p>Request for Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
</ul>

#### 12.2.3. Architectural Inputs

<ul>
<li>
<p>Organizational Model for Enterprise Architecture (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Scope of organizations impacted</p>
</li>
<li>
<p>Maturity assessment, gaps, and resolution approach</p>
</li>
<li>
<p>Roles and responsibilities for architecture team(s)</p>
</li>
<li>
<p>Constraints on architecture work</p>
</li>
<li>
<p>Budget requirements</p>
</li>
<li>
<p>Governance and support strategy</p>
</li>
</ul>
</div>
</li>
<li>
<p>Tailored Architecture Framework (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Tailored architecture method</p>
</li>
<li>
<p>Tailored architecture content (deliverables and artifacts)</p>
</li>
<li>
<p>Configured and deployed tools</p>
</li>
</ul>
</div>
</li>
<li>
<p>Statement of Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Architecture Vision (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)<br/></p>
</li>
<li>
<p>Architecture Repository (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Re-usable building blocks</p>
</li>
<li>
<p>Publicly available reference models<br/></p>
</li>
<li>
<p>Organization-specific reference models</p>
</li>
<li>
<p>Organization standards</p>
</li>
</ul>
</div>
</li>
<li>
<p>Architecture Definition Document (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Architecture Requirements Specification (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Gap analysis results (from Business, Data, Application, and
Technology Architectures)</p>
</li>
<li>
<p>Architectural requirements</p>
</li>
</ul>
</div>
</li>
<li>
<p>Architecture Roadmap (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Change Request (see the <a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>) — technology changes:</p>
<div class="ulist">
<ul>
<li>
<p>New technology reports</p>
</li>
<li>
<p>Asset management cost reduction initiatives</p>
</li>
<li>
<p>Technology withdrawal reports</p>
</li>
<li>
<p>Standards initiatives</p>
</li>
</ul>
</div>
</li>
<li>
<p>Change Request (see the <a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>) — business changes:</p>
<div class="ulist">
<ul>
<li>
<p>Business developments</p>
</li>
<li>
<p>Business exceptions</p>
</li>
<li>
<p>Business innovations</p>
</li>
<li>
<p>Business technology innovations</p>
</li>
<li>
<p>Strategic change developments</p>
</li>
</ul>
</div>
</li>
<li>
<p>Change Request (see the <a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>) — from lessons learned</p>
</li>
<li>
<p>Implementation Governance Model (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Architecture Contract (signed) (see the
<a href="https://pubs.opengroup.org/togaf-standard/ea-capability-and-governance/chap01.html">TOGAF Standard — EA Capability and Governance</a>)</p>
</li>
<li>
<p>Compliance Assessments (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Implementation and Migration Plan (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
</ul>

### 12.3. Steps

The level of detail addressed in Phase H will depend on the scope and
goals of the overall architecture effort.

The order of the steps in Phase H as well as the time at which they are
formally started and completed should be adapted to the situation at
hand in accordance with the established Architecture Governance.

The steps in Phase H are as follows:

<ul>
<li>
<p>Establish value realization process; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_12_03_01">Section 12.3.1, “Establish Value Realization Process”</a></p>
</li>
<li>
<p>Deploy monitoring tools; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_12_03_02">Section 12.3.2, “Deploy Monitoring Tools”</a></p>
</li>
<li>
<p>Manage risks; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_12_03_03">Section 12.3.3, “Manage Risks”</a></p>
</li>
<li>
<p>Provide analysis for architecture change management; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_12_03_04">Section 12.3.4, “Provide Analysis for Architecture Change Management”</a></p>
</li>
<li>
<p>Develop change requirements to meet performance targets; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_12_03_05">Section 12.3.5, “Develop Change Requirements to Meet Performance Targets”</a></p>
</li>
<li>
<p>Manage governance process; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_12_03_06">Section 12.3.6, “Manage Governance Process”</a></p>
</li>
<li>
<p>Activate the process to implement change; see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_12_03_07">Section 12.3.7, “Activate the Process to Implement Change”</a></p>
</li>
</ul>

#### 12.3.1. Establish Value Realization Process

Influence business projects to exploit the Enterprise Architecture for
value realization (outcomes).

#### 12.3.2. Deploy Monitoring Tools

Ensure monitoring tools are deployed and applied to enable the
following:

<ul>
<li>
<p>Monitor technology changes which could impact the Baseline
Architecture</p>
</li>
<li>
<p>Monitor business changes which could impact the Baseline Architecture</p>
</li>
<li>
<p>Business value tracking; e.g., investment appraisal method to
determine value metrics for the business objectives</p>
</li>
<li>
<p>Monitor Enterprise Architecture Capability maturity</p>
</li>
<li>
<p>Track and assess asset management programs</p>
</li>
<li>
<p>Track the Quality of Service (QoS) performances and usage</p>
</li>
<li>
<p>Determine and track business continuity requirements</p>
</li>
</ul>

#### 12.3.3. Manage Risks

Manage Enterprise Architecture risks and provide recommendations for IT
strategy.

#### 12.3.4. Provide Analysis for Architecture Change Management

Provide analysis for architecture change management:

<ul>
<li>
<p>Analyze performance</p>
</li>
<li>
<p>Conduct Enterprise Architecture performance reviews with service
management</p>
</li>
<li>
<p>Assess Change Requests and reporting to ensure that the expected value
realization and Service-Level Agreement (SLA) expectations of the
customers are met</p>
</li>
<li>
<p>Undertake a gap analysis of the performance of the Enterprise
Architecture</p>
</li>
<li>
<p>Ensure change management requests adhere to the Enterprise
Architecture Governance and framework</p>
</li>
</ul>

#### 12.3.5. Develop Change Requirements to Meet Performance Targets

Make recommendations on change requirements to meet performance targets
and development of position to act.

#### 12.3.6. Manage Governance Process

Manage governance process and framework for architecture:

<ul>
<li>
<p>Arrange meeting of Architecture Board (or other Governing Council)</p>
</li>
<li>
<p>Hold meeting of the Architecture Board with the aim of the meeting to
decide on handling changes (technology and business and dispensations)</p>
</li>
</ul>

#### 12.3.7. Activate the Process to Implement Change

Activate the architecture process to implement change:

<ul>
<li>
<p>Produce a new Request for Architecture Work and request for investment</p>
</li>
<li>
<p>Ensure any changes implemented in this phase are captured and
documented in the Architecture Repository</p>
</li>
</ul>

### 12.4. Outputs

The outputs of Phase H may include, but are not restricted to:

<ul>
<li>
<p>Architecture updates (for maintenance changes)</p>
</li>
<li>
<p>Changes to architecture framework and principles (for maintenance
changes)</p>
</li>
<li>
<p>New Request for Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), to move to another cycle (for major changes)</p>
</li>
<li>
<p>Statement of Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), updated if necessary</p>
</li>
<li>
<p>Architecture Contract (see the
<a href="https://pubs.opengroup.org/togaf-standard/ea-capability-and-governance/chap01.html">TOGAF Standard — EA Capability and Governance</a>), updated if necessary</p>
</li>
<li>
<p>Compliance Assessments (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), updated if necessary</p>
</li>
</ul>

### 12.5. Approach

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

<ul>
<li>
<p>The circumstances under which the Enterprise Architecture, or parts of
it, will be permitted to change after deployment, and the process by
which that will happen</p>
</li>
<li>
<p>The circumstances under which the architecture development cycle will
be initiated again to develop a new architecture</p>
</li>
</ul>

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

#### 12.5.1. Drivers for Change

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

<ul>
<li>
<p>Strategic, top-down directed change to enhance or create new
capability (capital)</p>
</li>
<li>
<p>Bottom-up changes to correct or enhance capability (operations and
maintenance) for infrastructure under operations management</p>
</li>
<li>
<p>Experiences with the previously delivered project increments in the
care of operations management, but still being delivered by ongoing
projects</p>
</li>
</ul>

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

<ul>
<li>
<p>New technology reports</p>
</li>
<li>
<p>Asset management cost reductions</p>
</li>
<li>
<p>Technology withdrawal</p>
</li>
<li>
<p>Standards initiatives</p>
</li>
</ul>

This type of Change Request is normally manageable primarily through an
enterprise’s change management and Architecture Governance processes.

In addition, there are business drivers for architecture change,
including:

<ul>
<li>
<p>Business-as-usual developments</p>
</li>
<li>
<p>Business exceptions</p>
</li>
<li>
<p>Business innovations</p>
</li>
<li>
<p>Business technology innovations</p>
</li>
<li>
<p>Strategic change</p>
</li>
</ul>

This type of Change Request often results in a complete re-development
of the architecture, or at least in an iteration of a part of the
architecture development cycle, as explained below.

#### 12.5.2. Enterprise Architecture Change Management Process

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

<ul>
<li>
<p><strong>Simplification change</strong>: a simplification change can normally be
handled via change management techniques</p>
</li>
<li>
<p><strong>Incremental change</strong>: an incremental change may be capable of being
handled via change management techniques, or it may require partial
re-architecting, depending on the nature of the change (see <a href="https://pubs.opengroup.org/togaf-standard/architecture-development-method.single/togaf-standard-architecture-development-method.html#tag_12_05_03">Section 12.5.3, “Guidelines for Maintenance <em>versus</em> Architecture Redesign”</a>
for guidelines)</p>
</li>
<li>
<p><strong>Re-architecting change</strong>: a re-architecting change requires putting
the whole architecture through the architecture development cycle again</p>
</li>
</ul>

Another way of looking at these three choices is to say that a
simplification change to an architecture is often driven by a
requirement to reduce investment; an incremental change is driven by a
requirement to derive additional value from existing investment; and a
re-architecting change is driven by a requirement to increase investment
in order to create new value for exploitation.

To determine whether a change is simplification, incremental, or
re-architecting, the following activities are undertaken:

<ol class="arabic">
<li>
<p>Registration of all events that may impact the architecture</p>
</li>
<li>
<p>Resource allocation and management for architecture tasks</p>
</li>
<li>
<p>The process or role responsible for architecture resources has to make
an assessment of what should be done</p>
</li>
<li>
<p>Evaluation of impacts</p>
</li>
</ol>

#### 12.5.3. Guidelines for Maintenance versus Architecture Redesign

A good guideline is:

<ul>
<li>
<p>If the change impacts two stakeholders or more, then it is likely to
require an architecture redesign and re-entry to the ADM</p>
</li>
<li>
<p>If the change impacts only one stakeholder, then it is more likely to
be a candidate for change management</p>
</li>
<li>
<p>If the change can be allowed under a dispensation, then it is more
likely to be a candidate for change management</p>
</li>
</ul>

For example:

<ul>
<li>
<p>If the impact is significant for the business strategy, then there may
be a need to redo the whole Enterprise Architecture — thus a
re-architecting approach</p>
</li>
<li>
<p>If a new technology or standards emerge, then there may be a need to
refresh the Technology Architecture, but not the whole Enterprise
Architecture — thus an incremental change</p>
</li>
<li>
<p>If the change is at an infrastructure level — for example, ten systems
reduced or changed to one system — this may not change the architecture
above the physical layer, but it will change the Baseline Description of
the Technology Architecture; this would be a simplification change
handled via change management techniques</p>
</li>
</ul>

In particular, a refreshment cycle (partial or complete re-architecting)
may be required if:

<ul>
<li>
<p>The Foundation Architecture needs to be re-aligned with the business
strategy</p>
</li>
<li>
<p>Substantial change is required to components and guidelines for use in
deployment of the architecture</p>
</li>
<li>
<p>Significant standards used in the product architecture are changed
which have significant end-user impact; e.g., regulatory changes</p>
</li>
</ul>

If there is a need for a refreshment cycle, then a new Request for
Architecture Work must be issued (to move to another cycle).

## 13. ADM Architecture Requirements Management

This chapter looks at the process of managing architecture requirements
throughout the ADM.

![ADM Architecture Requirements](assets/001-req_mgt.png)

Figure 13-1: ADM Architecture Requirements

### 13.1. Objectives

The objectives of the Requirements Management phase are to:

<ul>
<li>
<p>Ensure that the Requirements Management process is sustained and
operates for all relevant ADM phases</p>
</li>
<li>
<p>Manage architecture requirements identified during any execution of
the ADM cycle or a phase</p>
</li>
<li>
<p>Ensure that relevant architecture requirements are available for use
by each phase as the phase is executed</p>
</li>
</ul>

### 13.2. Inputs

Inputs to the Requirements Management phase are:

<ul>
<li>
<p>A populated Architecture Repository (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Organizational Model for Enterprise Architecture (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Scope of organizations impacted</p>
</li>
<li>
<p>Maturity assessment, gaps, and resolution approach</p>
</li>
<li>
<p>Roles and responsibilities for architecture team(s)</p>
</li>
<li>
<p>Constraints on architecture work</p>
</li>
<li>
<p>Budget requirements</p>
</li>
<li>
<p>Governance and support strategy</p>
</li>
</ul>
</div>
</li>
<li>
<p>Tailored Architecture Framework (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>), including:</p>
<div class="ulist">
<ul>
<li>
<p>Tailored architecture method</p>
</li>
<li>
<p>Tailored architecture content (deliverables and artifacts)</p>
</li>
<li>
<p>Configured and deployed tools</p>
</li>
</ul>
</div>
</li>
<li>
<p>Statement of Architecture Work (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Architecture Vision (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Architecture requirements, populating an Architecture Requirements
Specification (see the <a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Requirements Impact Assessment (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
</ul>

### 13.3. Steps

The steps in the Requirements Management phase are described in the
table below:

<table class="tableblock frame-all grid-all stretch">
<colgroup>
<col style="width: 10%;"/>
<col style="width: 45%;"/>
<col style="width: 45%;"/>
</colgroup>
<thead>
<tr>
<th class="tableblock halign-left valign-top"><strong> </strong></th>
<th class="tableblock halign-left valign-top"><strong>Requirements Management Steps</strong></th>
<th class="tableblock halign-left valign-top"><strong>ADM Phase Steps</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">Step 1</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock"> </p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">Identify requirements (typically by analyzing how business
goals/objectives can be met through the design of value streams,
business scenarios, user experiences, or the provision of management
information) and document them in the Architecture Requirements
Specification and Requirements Repository.</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">Step 2</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">Establish baseline requirements: determine priorities, confirm
stakeholder agreement to priorities, and document them in the
Architecture Requirements Specification and Requirements Repository.</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock"> </p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">Step 3</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">Monitor baseline requirements.</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock"> </p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">Step 4</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock"> </p></td>
<td class="tableblock halign-left valign-top"><div class="content"><div class="paragraph">
<p>Identify new and changed requirements:</p>
</div>
<div class="olist loweralpha">
<ol class="loweralpha" type="a">
<li>
<p>Remove or re-assess priorities</p>
</li>
<li>
<p>Add requirements and re-assess priorities</p>
</li>
<li>
<p>Modify existing requirements</p>
</li>
</ol>
</div></div></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">Step 5</p></td>
<td class="tableblock halign-left valign-top"><div class="content"><div class="paragraph">
<p>Identify changed requirements and record priorities:</p>
</div>
<div class="olist loweralpha">
<ol class="loweralpha" type="a">
<li>
<p>Identify changed requirements and ensure the requirements are
prioritized by the architect(s) responsible for the current phase, and
by the relevant stakeholders</p>
</li>
<li>
<p>Record new priorities</p>
</li>
<li>
<p>Ensure that any conflicts are identified and managed through the
phases to a successful conclusion and prioritization</p>
</li>
<li>
<p>Generate Requirements Impact Assessment (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>) for steering the architecture team</p>
</li>
</ol>
</div>
<div class="paragraph">
<p><strong>Notes</strong></p>
</div>
<div class="ulist">
<ul>
<li>
<p>Changed requirements can come in through any route</p>
<div class="paragraph">
<p>To ensure that the requirements are properly assessed and prioritized,
this process needs to direct the ADM phases and record the decisions
related to the requirements.</p>
</div>
</li>
<li>
<p>The Requirements Management phase needs to determine stakeholder
satisfaction with the decisions</p>
<div class="paragraph">
<p>Where there is dissatisfaction, the phase remains accountable to ensure
the resolution of the issues and determine next steps.</p>
</div>
</li>
</ul>
</div></div></td>
<td class="tableblock halign-left valign-top"><p class="tableblock"> </p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">Step 6</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock"> </p></td>
<td class="tableblock halign-left valign-top"><div class="content"><div class="olist loweralpha">
<ol class="loweralpha" type="a">
<li>
<p>Assess impact of changed requirements on current (active) phase</p>
</li>
<li>
<p>Assess impact of changed requirements on previous phases</p>
</li>
<li>
<p>Determine whether to implement change, or defer to later ADM cycle; if
decision is to implement, assess timescale for change management
implementation</p>
</li>
<li>
<p>Issue Requirements Impact Assessment, Version <em>n</em>+1</p>
</li>
</ol>
</div></div></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">Step 7</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock"> </p></td>
<td class="tableblock halign-left valign-top"><div class="content"><div class="paragraph">
<p>Implement requirements arising from Phase H.</p>
</div>
<div class="paragraph">
<p>The architecture can be changed through its lifecycle by the
Architecture Change Management phase (Phase H). The Requirements
Management process ensures that new or changing requirements that are
derived from Phase H are managed accordingly.</p>
</div></div></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">Step 8</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">Update the Architecture Requirements Repository with
information relating to the changes requested, including stakeholder
views affected.</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock"> </p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">Step 9</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock"> </p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock">Implement change in the current phase.</p></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><p class="tableblock">Step 10</p></td>
<td class="tableblock halign-left valign-top"><p class="tableblock"> </p></td>
<td class="tableblock halign-left valign-top"><div class="content"><div class="paragraph">
<p>Assess and revise gap analysis for past phases.</p>
</div>
<div class="paragraph">
<p>The gap analysis in the ADM Phases B through D identifies the gaps
between Baseline and Target Architectures. Certain types of gap can give
rise to gap requirements.</p>
</div>
<div class="paragraph">
<p>The ADM describes two kinds of gap:</p>
</div>
<div class="ulist">
<ul>
<li>
<p>Something that is present in the baseline, but not in the target
(i.e., eliminated — by accident or design)</p>
</li>
<li>
<p>Something not in the baseline, but present in the target (i.e., new)</p>
</li>
</ul>
</div>
<div class="paragraph">
<p>A “gap requirement” is anything that has been eliminated by accident,
and therefore requires a change to the Target Architecture.</p>
</div>
<div class="paragraph">
<p>If the gap analysis generates gap requirements, then this step will
ensure that they are addressed, documented, and recorded in the
Architecture Requirements Repository, and that the Target Architecture
is revised accordingly.</p>
</div></div></td>
</tr>
</tbody>
</table>

### 13.4. Outputs

The outputs of the Requirements Management process may include, but are
not restricted to:

<ul>
<li>
<p>Requirements Impact Assessment (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>)</p>
</li>
<li>
<p>Updated Architecture Requirements Specification (see the
<a href="https://pubs.opengroup.org/togaf-standard/architecture-content/chap01.html">TOGAF Standard — Architecture Content</a>: Architecture Requirements Specification), if necessary</p>
</li>
</ul>

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

### 13.5. Approach

#### 13.5.1. General

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

#### 13.5.2. Requirements Development

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

<ul>
<li>
<p>Functional requirements</p>
</li>
<li>
<p>Non-functional requirements</p>
</li>
</ul>

When defining requirements the architect should take into account:

<ul>
<li>
<p>Assumptions for requirements</p>
</li>
<li>
<p>Constraints for requirements</p>
</li>
<li>
<p>Domain-specific principles that drive requirements</p>
</li>
<li>
<p>Policies affecting requirements</p>
</li>
<li>
<p>Standards that requirements must meet</p>
</li>
<li>
<p>Organization guidelines for requirements</p>
</li>
<li>
<p>Specifications for requirements</p>
</li>
</ul>

Deliverables in later ADM phases also contain mappings to the design
requirements, and may also generate new types of requirements (for
example, conformance requirements, time windows for implementation).

#### 13.5.3. Resources

The world of requirements engineering is rich with emerging
recommendations and processes for Requirements Management. The TOGAF
Standard does not mandate or recommend any specific process or tool; it
simply states what an effective Requirements Management process should
achieve (i.e., the “requirements for requirements”, if you like).

##### 13.5.3.1. Business Scenarios

A technique used to analyze how a business goal or objective can be met
by a process or value stream. Analyzing where the activities in that
process are performed by human and computer actors is a highly effective
way to identify and clarify architecture requirements. The technique is
detailed in the TOGAF ® Series Guide: Business Scenarios .

##### 13.5.3.2. Requirements Tools

There is a large, and increasing, number of Commercial Off-The-Shelf
(COTS) tools available for the support of Requirements Management,
albeit not necessarily designed for architecture requirements.

