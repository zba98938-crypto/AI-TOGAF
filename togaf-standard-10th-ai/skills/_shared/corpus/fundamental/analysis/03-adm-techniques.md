# ADM技术：当前语义解析

本页为逐节语义解释，不能把解释当全文译文。本卷另有[逐块中文正文](../chinese-text/03-adm-techniques.md)，已写正文的最终独立语义校核仍待完成。

[英文及离线原文](../web-2025/volumes/03-adm-techniques/index.html)

<a id="chap01"></a>
## 1. Introduction

概念：本卷给出原则、利益相关者、模式、差距、互操作、就绪度、风险和替代方案八类技术。

适用条件：按架构任务选用，而非每次执行固定八步。

逻辑关系：技术补充ADM活动，不替代阶段输入输出。

决策方法：依据问题选择技术并回到相应阶段处理结果。

制品及证据：技术选择理由及对阶段制品的引用。

适用边界：本引言没有定义统一技术执行顺序。

来源块：C220-web-2025:03-adm-techniques:b00038, C220-web-2025:03-adm-techniques:b00039, C220-web-2025:03-adm-techniques:b00040, C220-web-2025:03-adm-techniques:b00041

<details><summary>展开本节完整英文来源</summary>

1. Introduction

This chapter provides an introduction to the guidance provided in the TOGAF Standard — ADM Techniques (this document).

Guidelines included within this document are as follows:

Architecture Principles (see Chapter 2, Architecture Principles ) describes principles for the use and deployment of IT resources across the enterprise, and how to develop the set of general rules and guidelines for the architecture being developed Stakeholder Management (see Chapter 3, Stakeholder Management ) describes stakeholder management, an important discipline that successful architecture practitioners can use to win support for their projects Architecture Patterns (see Chapter 4, Architecture Patterns ) provides guidance on using architectural patterns Gap Analysis (see Chapter 5, Gap Analysis ) describes the technique known as gap analysis; it is widely used in the TOGAF ADM to validate an architecture that is being developed Interoperability Requirements (see Chapter 6, Interoperability Requirements ) describes a technique for determining interoperability requirements Business Transformation Readiness Assessment (see Chapter 7, Business Transformation Readiness Assessment ) describes a technique for identifying business transformation issues Risk Management (see Chapter 8, Risk Management ) describes a technique for managing risk during an architecture/business transformation project Architecture Alternatives and Trade-Offs (see Chapter 9, Architecture Alternatives and Trade-Offs ) describes a technique to identify alternative Target Architectures and perform trade-offs between the alternatives

</details>

<a id="chap02"></a>
## 2. Architecture Principles

概念：架构原则是指导架构开发、维护和使用的长期规则。

适用条件：制定或更新企业架构决策依据。

逻辑关系：本章从原则来源到定义、批准、应用和示例逐层展开。

决策方法：先检查企业上位原则再定架构原则。

制品及证据：原则集、依据、批准记录。

适用边界：示例集不自动成为组织政策。

来源块：C220-web-2025:03-adm-techniques:b00042, C220-web-2025:03-adm-techniques:b00043

<details><summary>展开本节完整英文来源</summary>

2. Architecture Principles

This chapter describes principles for use in the development of an Enterprise Architecture.

</details>

<a id="tag_02_01"></a>
## 2.1. Introduction

概念：企业原则适用于企业决策；架构原则体现企业共识并约束架构过程。

适用条件：企业及分段或业务单元均可有原则。

逻辑关系：分段原则细化企业原则；架构原则受企业原则约束。

决策方法：检验原则与架构能力所在组织环境的一致性。

制品及证据：上位原则到分段原则的追溯关系。

适用边界：不能因单元原则较细就覆盖企业原则。

来源块：C220-web-2025:03-adm-techniques:b00044, C220-web-2025:03-adm-techniques:b00045, C220-web-2025:03-adm-techniques:b00046, C220-web-2025:03-adm-techniques:b00047, C220-web-2025:03-adm-techniques:b00048, C220-web-2025:03-adm-techniques:b00049, C220-web-2025:03-adm-techniques:b00050, C220-web-2025:03-adm-techniques:b00051

<details><summary>展开本节完整英文来源</summary>

2.1. Introduction

Principles are general rules and guidelines, intended to be enduring and seldom amended, that inform and support the way in which an organization sets about fulfilling its mission.

In their turn, principles may be just one element in a structured set of ideas that collectively define and guide the organization, from values through to actions and results.

Depending on the organization, principles may be established within different domains and at different levels. Two key domains inform the development and utilization of architecture:

Enterprise Principles provide a basis for decision-making throughout an enterprise, and inform how the organization sets about fulfilling its mission Such principles are commonly found as a means of harmonizing
decision-making across an organization. In particular, they are a key element in a successful Architecture Governance strategy (see the TOGAF Standard — EA Capability and Governance ). Within the broad domain of enterprise principles, it is common to have subsidiary principles within a business or organizational unit. Examples include IT, HR, domestic operations, or overseas operations. These principles provide a basis for decision-making within the subsidiary
domain and will inform architecture development within the domain. Care must be taken to ensure that the principles used to inform architecture development align to the organizational context of the Architecture Capability. Architecture Principles are a set of principles that relate to architecture work They reflect a level of consensus across the enterprise, and embody the spirit and thinking of existing enterprise principles. Architecture Principles govern the architecture process, affecting the development, maintenance, and use of the Enterprise Architecture.

It is common to have sets of principles form a hierarchy, in that segment principles will be informed by, and elaborate on, the principles at the enterprise level. Architecture Principles will be informed and constrained by enterprise principles.

Architecture Principles may restate other enterprise guidance in terms and form that effectively guide architecture development.

The remainder of this section deals exclusively with Architecture Principles.

</details>

<a id="tag_02_02"></a>
## 2.2. Characteristics of Architecture Principles

概念：架构原则是未来IT资源和资产决策的共同基础。

适用条件：跨企业使用和部署信息技术。

逻辑关系：每项原则应回溯业务目标及关键架构驱动。

决策方法：没有业务目标关联的原则需补依据或重新讨论。

制品及证据：原则—目标—驱动映射。

适用边界：有书面原则不证明已有真实共识。

来源块：C220-web-2025:03-adm-techniques:b00052, C220-web-2025:03-adm-techniques:b00053, C220-web-2025:03-adm-techniques:b00054

<details><summary>展开本节完整英文来源</summary>

2.2. Characteristics of Architecture Principles

Architecture Principles define the underlying general rules and guidelines for the use and deployment of all IT resources and assets across the enterprise. They reflect a level of consensus among the various elements of the enterprise, and form the basis for making future IT decisions.

Each Architecture Principle should be clearly related back to the business objectives and key architecture drivers.

</details>

<a id="tag_02_03"></a>
## 2.3. Components of Architecture Principles

概念：原则用名称、陈述、理由、影响四部分定义。

适用条件：希望理解、接受并解释具体决策时。

逻辑关系：理由说明业务收益和冲突平衡；影响说明资源、成本和任务。

决策方法：名称陈述避开平台名和模糊措辞，理由明确优先情形。

制品及证据：四字段原则表，潜在影响与已分析影响分别标记。

适用边界：影响可能只是推测，不能转成已验证成本。

来源块：C220-web-2025:03-adm-techniques:b00055, C220-web-2025:03-adm-techniques:b00056, C220-web-2025:03-adm-techniques:b00057, C220-web-2025:03-adm-techniques:b00058, C220-web-2025:03-adm-techniques:b00059

<details><summary>展开本节完整英文来源</summary>

2.3. Components of Architecture Principles

It is useful to have a standard way of defining principles. In addition to a definition statement, each principle should have associated rationale and implications statements, both to promote understanding and acceptance of the principles themselves, and to support the use of the principles in explaining and justifying why specific decisions are made.

A recommended template is given in Table 2-1 .

Table 2-1:  Recommended Format for Defining Principles Name Should both represent the essence of the rule as well as be easy to remember. Specific technology platforms should not be mentioned in the name or statement of a principle. Avoid ambiguous words in the Name and in the Statement such as: “support”, “open”, “consider”, and
for lack of good measure the word “avoid”, itself, be careful with “manage(ment)”, and look for unnecessary adjectives and adverbs (fluff). Statement Should succinctly and unambiguously communicate the fundamental rule. For the most part, the principles statements for managing information are similar from one organization to the next. It is vital that the principles statement is unambiguous. Rationale Should highlight the business benefits of adhering to the principle, using business terminology. Point to the similarity of information and technology principles to the principles governing business operations. Also describe the relationship to other principles, and the intentions regarding a balanced interpretation. Describe
situations where one principle would be given precedence or carry more weight than another for making a decision. Implications Should highlight the requirements, both for the business and IT, for carrying out the principle — in terms of resources, costs, and activities/tasks. Although it may often be apparent that current systems, standards, or practices would be incongruent with the principle upon adoption, context will drive the degree of scope. The
impact to the business and consequences of adopting a principle should be clearly stated. The reader should readily discern the answer to: “How does this affect me?”. It is important not to oversimplify, trivialize, or judge the merit of the impact. Some of the implications will be
identified as potential impacts only, and may be speculative rather than fully analyzed.

An example set of Architecture Principles following this template is given in Section 2.6, “Example Set of Architecture Principles” .

</details>

<a id="tag_02_04"></a>
## 2.4. Developing Architecture Principles

概念：架构师与关键利益相关者共同制定，通常由架构委员会批准。

适用条件：建立与目标架构实施及业务战略一致的原则集。

逻辑关系：使命计划、战略举措、外部约束、既有技术与行业趋势共同提供输入。

决策方法：核查可追溯性、清晰度和组织批准。

制品及证据：输入依据、原则草案、委员会审议记录。

适用边界：通常批准主体不证明本组织已有此权限配置。

来源块：C220-web-2025:03-adm-techniques:b00060, C220-web-2025:03-adm-techniques:b00061, C220-web-2025:03-adm-techniques:b00062, C220-web-2025:03-adm-techniques:b00063, C220-web-2025:03-adm-techniques:b00064, C220-web-2025:03-adm-techniques:b00065

<details><summary>展开本节完整英文来源</summary>

2.4. Developing Architecture Principles

Architecture Principles are typically developed by the Enterprise Architects, in conjunction with the key stakeholders, and are approved by the Architecture Board.

Architecture Principles will be informed by principles at the enterprise level, if they exist.

Architecture Principles must be clearly traceable and clearly
articulated to guide decision-making. They are chosen so as to ensure alignment of the architecture and implementation of the Target Architecture with business strategies and visions.

Specifically, the development of Architecture Principles is typically influenced by the following:

Enterprise mission and plans : the mission, plans, and organizational infrastructure of the enterprise Enterprise strategic initiatives : the characteristics of the enterprise — its strengths, weaknesses, opportunities, and threats — and its current enterprise-wide initiatives (such as process improvement and quality management) External constraints : market factors (time-to-market imperatives, customer expectations, etc.); existing and potential legislation Current systems and technology : the set of information resources deployed within the enterprise, including systems documentation, equipment inventories, network configuration diagrams, policies, and procedures Emerging industry trends : predictions about economic, political, technical, and market factors that influence the enterprise environment

</details>

<a id="tag_02_04_01"></a>
## 2.4.1. Qualities of Principles

概念：好原则集需易理解、稳健、完整、一致、稳定。

适用条件：检验原则质量而非仅收集同意签名。

逻辑关系：一致允许平衡解释；稳定仍需有正式修订过程。

决策方法：检查争议情形是否能得到一致且可执行的决定。

制品及证据：质量评审、冲突解释及增删改程序。

适用边界：完整性针对可预见情形，不能声称解决一切未来问题。

来源块：C220-web-2025:03-adm-techniques:b00066, C220-web-2025:03-adm-techniques:b00067, C220-web-2025:03-adm-techniques:b00068, C220-web-2025:03-adm-techniques:b00069, C220-web-2025:03-adm-techniques:b00070

<details><summary>展开本节完整英文来源</summary>

2.4.1. Qualities of Principles

Merely having a written statement that is called a principle does not mean that the principle is good, even if everyone agrees with it.

A good set of principles will be founded in the beliefs and values of the organization and expressed in language that the business understands and uses. Principles should be few in number, future-oriented, and endorsed and championed by senior management. They provide a firm foundation for making architecture and planning decisions, framing policies, procedures, and standards, and supporting resolution of
contradictory situations. A poor set of principles will quickly become disused, and the resultant architectures, policies, and standards will
appear arbitrary or self-serving, and thus lack credibility.
Essentially, principles drive behavior.

There are five criteria that distinguish a good set of principles:

Understandable : the underlying tenets can be quickly grasped and understood by individuals throughout the organization The intention of the principle is clear and unambiguous, so that violations, whether intentional or not, are minimized. Robust : enable good quality decisions about architectures and plans to be made, and enforceable policies and standards to be created Each principle should be sufficiently definitive and precise to support consistent decision-making in complex, potentially controversial situations. Complete : every potentially important principle governing the management of information and technology for the organization is defined
— the principles cover every situation perceived Consistent : strict adherence to one principle may require a loose interpretation of another principle The set of principles must be expressed in a way that allows a balance of interpretations. Principles should not be contradictory to the point where adhering to one principle would violate the spirit of another. Every word in a principle statement should be carefully chosen to allow consistent yet flexible interpretation. Stable : principles should be enduring, yet able to accommodate changes An amendment process should be established for adding, removing, or altering principles after they are ratified initially.

</details>

<a id="tag_02_05"></a>
## 2.5. Applying Architecture Principles

概念：原则作为评估标准、需求驱动、符合性依据和豁免讨论的后盾。

适用条件：方案选型、存量评估、过渡规划和架构治理。

逻辑关系：原则必须成组应用；数据可访问与安全可能竞争。

决策方法：决定个别问题的优先原则并记录理由，必要时提出豁免。

制品及证据：权衡决定、评估标准、过渡任务及豁免记录。

适用边界：违反原则没有本章统一处罚规则，不能自行添加。

来源块：C220-web-2025:03-adm-techniques:b00071, C220-web-2025:03-adm-techniques:b00072, C220-web-2025:03-adm-techniques:b00073, C220-web-2025:03-adm-techniques:b00074, C220-web-2025:03-adm-techniques:b00075, C220-web-2025:03-adm-techniques:b00076, C220-web-2025:03-adm-techniques:b00077, C220-web-2025:03-adm-techniques:b00078, C220-web-2025:03-adm-techniques:b00079

<details><summary>展开本节完整英文来源</summary>

2.5. Applying Architecture Principles

Architecture Principles are used to capture the fundamental truths about how the enterprise will use and deploy IT resources and assets.

The principles are used in a number of different ways:

To provide a framework within which the enterprise can start to make conscious decisions about Enterprise Architecture and projects that implement the target Enterprise Architecture As a guide to establishing relevant evaluation criteria, thus exerting strong influence on the selection of products, solutions, or solution architectures in the later stages of managing compliance to the Enterprise Architecture As drivers for defining the functional requirements of the
architecture As an input to assessing both existing implementations and the strategic portfolio, for compliance with the defined architectures; these assessments will provide valuable insights into the transition activities needed to implement an architecture, in support of business goals and priorities The Rationale statements within an Architecture Principle highlight the business value of implementations consistent with the principle and provide guidance for difficult decisions with conflicting drivers or objectives The Implications statements within an Architecture Principle provide an outline of the key tasks, resources, and potential costs to the enterprise of following the principle; they also provide valuable inputs to future transition initiative and planning activities Support the Architecture Governance activities in terms of: Providing a “back-stop” for the standard Architecture Compliance assessments where some interpretation is allowed or required Supporting the decision to initiate a dispensation request where the implications of a particular architecture amendment cannot be resolved within local operating procedure

Principles may be inter-related, and need to be applied as a set.

Principles will sometimes compete; for example, the principles of “accessibility” and “security” tend towards conflicting decisions. Each principle must be considered in the context of “all other things being equal”.

At times a decision will be required as to which principle will take precedence on a particular issue. The rationale for such decisions should always be documented.

A common reaction on first reading of a principle is “this is obvious and does not need to be documented”. The fact that a principle seems self-evident does not mean that the guidance in a principle is followed. Having principles that appear obvious helps ensure that decisions actually follow the desired outcome.

Although specific penalties are not prescribed in a declaration of principles, violations of principles generally cause operational problems and inhibit the ability of the organization to fulfill its mission.

</details>

<a id="tag_02_06"></a>
## 2.6. Example Set of Architecture Principles

概念：本节21个示例演示典型内容与四字段格式。

适用条件：组织可用来讨论自己的原则。

逻辑关系：原则过多会降低灵活性；10至20是偏好说明，与21例不矛盾。

决策方法：按使命和约束选取、改写或拒绝示例。

制品及证据：本组织裁剪后的原则集。

适用边界：21例与偏好数量均不是强制清单。

来源块：C220-web-2025:03-adm-techniques:b00080, C220-web-2025:03-adm-techniques:b00081, C220-web-2025:03-adm-techniques:b00082

<details><summary>展开本节完整英文来源</summary>

2.6. Example Set of Architecture Principles

Too many principles can reduce the flexibility of the architecture. Many organizations prefer to define only high-level principles, and to limit the number to between 10 and 20.

The following example illustrates both the typical content of a set of Architecture Principles, and the recommended format for defining them, as explained above.

</details>

<a id="tag_02_06_01"></a>
## 2.6.1. Business Principles

概念：九个业务示例覆盖企业整体、参与、连续性、复用、服务、法规、IT和知识产权。

适用条件：讨论业务决策与IT架构约束的关系。

逻辑关系：下列业务原则共同约束数据、应用及技术原则。

决策方法：以本企业业务目标审查每个示例。

制品及证据：业务原则组及与后续原则的关联。

适用边界：仅分组标题，没有额外独立业务要求。

来源块：C220-web-2025:03-adm-techniques:b00083

<details><summary>展开本节完整英文来源</summary>

2.6.1. Business Principles

</details>

<a id="tag_02_06_01_01"></a>
## 2.6.1.1. Principle 1: Primacy of Principles

概念：信息管理原则对企业所有组织适用。

适用条件：采用本示例原则后的企业范围。

逻辑关系：排除与偏袒会破坏信息的一致和可测质量。

决策方法：启动举措前核对原则，冲突时调整举措框架。

制品及证据：原则符合性检查与冲突处理记录。

适用边界：这是示例的普遍适用声明，不是取消合法豁免流程。

来源块：C220-web-2025:03-adm-techniques:b00084, C220-web-2025:03-adm-techniques:b00085, C220-web-2025:03-adm-techniques:b00086, C220-web-2025:03-adm-techniques:b00087, C220-web-2025:03-adm-techniques:b00088, C220-web-2025:03-adm-techniques:b00089, C220-web-2025:03-adm-techniques:b00090

<details><summary>展开本节完整英文来源</summary>

2.6.1.1. Principle 1: Primacy of Principles

Statement:

These principles of information management apply to all organizations within the enterprise.

Rationale:

The only way we can provide a consistent and measurable level of quality information to decision-makers is if all organizations abide by the principles.

Implications:

Without this principle, exclusions, favoritism, and inconsistency would rapidly undermine the management of information Information management initiatives will not begin until they are examined for compliance with the principles A conflict with a principle will be resolved by changing the framework of the initiative

</details>

<a id="tag_02_06_01_02"></a>
## 2.6.1.2. Principle 2: Maximize Benefit to the Enterprise

概念：信息管理决策最大化企业整体收益。

适用条件：局部偏好与企业长期价值竞争时。

逻辑关系：技术本身不足以改变规划管理；企业代表论坛调整优先级。

决策方法：比较跨组织收益与代价，同时保证少数组织能完成工作。

制品及证据：企业计划、共享组件和优先级决定。

适用边界：不可把整体收益解释为任意牺牲少数业务使命。

来源块：C220-web-2025:03-adm-techniques:b00091, C220-web-2025:03-adm-techniques:b00092, C220-web-2025:03-adm-techniques:b00093, C220-web-2025:03-adm-techniques:b00094, C220-web-2025:03-adm-techniques:b00095, C220-web-2025:03-adm-techniques:b00096, C220-web-2025:03-adm-techniques:b00097

<details><summary>展开本节完整英文来源</summary>

2.6.1.2. Principle 2: Maximize Benefit to the Enterprise

Statement:

Information management decisions are made to provide maximum benefit to
the enterprise as a whole.

Rationale:

This principle embodies “service above self”. Decisions made from an
enterprise-wide perspective have greater long-term value than decisions
made from any particular organizational perspective. Maximum return on
investment requires information management decisions to adhere to
enterprise-wide drivers and priorities. No minority group will detract
from the benefit of the whole. However, this principle will not preclude
any minority group from getting its job done.

Implications:

Achieving maximum enterprise-wide benefit will require changes in the way we plan and manage information — technology alone will not bring about this change Some organizations may have to concede their own preferences for the greater benefit of the entire enterprise Where feasible, application development priorities must be established by the entire enterprise for the entire enterprise Applications components should be shared across organizational boundaries Information management initiatives should be conducted in accordance with the enterprise plan Individual organizations should pursue information management
initiatives which conform to the blueprints and priorities established by the enterprise. The plan will be changed as needed. As needs arise, priorities must be adjusted; a forum with
comprehensive enterprise representation should make these decisions

</details>

<a id="tag_02_06_01_03"></a>
## 2.6.1.3. Principle 3: Information Management is Everybody’s Business

概念：各组织参与实现业务目标所需的信息管理决策。

适用条件：业务专家与技术人员共同定义IT目标。

逻辑关系：用户是关键利益相关者；参与需要真实责任和资源。

决策方法：明确各方承担的环境开发责任。

制品及证据：共同目标、资源承诺及参与记录。

适用边界：参与不是给所有参与者相同批准权。

来源块：C220-web-2025:03-adm-techniques:b00098, C220-web-2025:03-adm-techniques:b00099, C220-web-2025:03-adm-techniques:b00100, C220-web-2025:03-adm-techniques:b00101, C220-web-2025:03-adm-techniques:b00102, C220-web-2025:03-adm-techniques:b00103, C220-web-2025:03-adm-techniques:b00104

<details><summary>展开本节完整英文来源</summary>

2.6.1.3. Principle 3: Information Management is Everybody’s Business

Statement:

All organizations in the enterprise participate in information
management decisions needed to accomplish business objectives.

Rationale:

Information users are the key stakeholders, or customers, in the
application of technology to address a business need. In order to ensure
information management is aligned with the business, all organizations
in the enterprise must be involved in all aspects of the information
environment. The business experts from across the enterprise and the
technical staff responsible for developing and sustaining the
information environment need to come together as a team to jointly
define the goals and objectives of IT.

Implications:

To operate as a team, every stakeholder, or customer, will need to
accept responsibility for developing the information environment Commitment of resources will be required to implement this principle

</details>

<a id="tag_02_06_01_04"></a>
## 2.6.1.4. Principle 4: Business Continuity

概念：系统中断时仍保持企业运营。

适用条件：按应用关键性及企业使命影响确定连续性级别。

逻辑关系：共享依赖引入中断风险；设计时处理恢复、冗余、可维护性。

决策方法：先评估关键性再决定连续性和恢复计划，定期评审测试。

制品及证据：业务影响分析、恢复计划、测试证据。

适用边界：原文不提供本案例RTO/RPO或库存恢复目标。

来源块：C220-web-2025:03-adm-techniques:b00105, C220-web-2025:03-adm-techniques:b00106, C220-web-2025:03-adm-techniques:b00107, C220-web-2025:03-adm-techniques:b00108, C220-web-2025:03-adm-techniques:b00109, C220-web-2025:03-adm-techniques:b00110, C220-web-2025:03-adm-techniques:b00111

<details><summary>展开本节完整英文来源</summary>

2.6.1.4. Principle 4: Business Continuity

Statement:

Enterprise operations are maintained in spite of system interruptions.

Rationale:

As system operations become more pervasive, we become more dependent on
them; therefore, we must consider the reliability of such systems
throughout their design and use. Business premises throughout the
enterprise must be provided with the capability to continue operations
regardless of external events. Hardware failure, natural disasters, and
data corruption should not be allowed to disrupt or stop enterprise
activities. The enterprise must be capable of operating on alternative
information delivery mechanisms.

Implications:

Dependency on shared system applications mandates that the risks of
business interruption must be established in advance and managed Management includes but is not limited to periodic reviews, testing for
vulnerability and exposure, or designing mission-critical services to
ensure business continuity through redundant or alternative
capabilities. Recoverability, redundancy, and maintainability should be addressed at
the time of design Applications must be assessed for criticality and impact on the
enterprise mission, in order to determine what level of continuity is
required and what corresponding recovery plan is necessary

</details>

<a id="tag_02_06_01_05"></a>
## 2.6.1.5. Principle 5: Common Use Applications

概念：优先企业共用应用，减少仅供局部使用的重复能力。

适用条件：企业决定采用共同应用政策时。

逻辑关系：重复能力耗费资源且生成冲突数据；替换要求同步标准化数据。

决策方法：核对局部独特价值，必要时加入企业能力而不是重复建设。

制品及证据：共用政策、迁移计划及数据标准。

适用边界：共享应用偏好不是未经业务验证的集中化最优结论。

来源块：C220-web-2025:03-adm-techniques:b00112, C220-web-2025:03-adm-techniques:b00113, C220-web-2025:03-adm-techniques:b00114, C220-web-2025:03-adm-techniques:b00115, C220-web-2025:03-adm-techniques:b00116, C220-web-2025:03-adm-techniques:b00117, C220-web-2025:03-adm-techniques:b00118

<details><summary>展开本节完整英文来源</summary>

2.6.1.5. Principle 5: Common Use Applications

Statement:

Development of applications used across the enterprise is preferred over
the development of similar or duplicative applications which are only
provided to a particular organization.

Rationale:

Duplicative capability is expensive and proliferates conflicting data.

Implications:

Organizations which depend on a capability which does not serve the
entire enterprise must change over to the replacement enterprise-wide
capability; this will require establishment of and adherence to a policy
requiring this Organizations will not be allowed to develop capabilities for their
own use which are similar/duplicative of enterprise-wide capabilities;
in this way, expenditures of scarce resources to develop essentially the
same capability in marginally different ways will be reduced Data and information used to support enterprise decision-making will
be standardized to a much greater extent than previously This is because the smaller, organizational capabilities which produced
different data (which was not shared among other organizations) will be
replaced by enterprise-wide capabilities. The impetus for adding to the
set of enterprise-wide capabilities may well come from an organization
making a convincing case for the value of the data/information
previously produced by its organizational capability, but the resulting
capability will become part of the enterprise-wide system, and the data
it produces will be shared across the enterprise.

</details>

<a id="tag_02_06_01_06"></a>
## 2.6.1.6. Principle 6: Service Orientation

概念：服务表示应对应真实业务活动和企业或跨企业流程。

适用条件：采用服务导向时。

逻辑关系：服务业务描述、编排、基础设施开放标准和治理相互配合。

决策方法：建立好服务的检验准则，按环境约束评估实现。

制品及证据：业务服务描述、接口和治理规则。

适用边界：服务导向不等同自动采用微服务或某技术产品。

来源块：C220-web-2025:03-adm-techniques:b00119, C220-web-2025:03-adm-techniques:b00120, C220-web-2025:03-adm-techniques:b00121, C220-web-2025:03-adm-techniques:b00122, C220-web-2025:03-adm-techniques:b00123, C220-web-2025:03-adm-techniques:b00124, C220-web-2025:03-adm-techniques:b00125

<details><summary>展开本节完整英文来源</summary>

2.6.1.6. Principle 6: Service Orientation

Statement:

The architecture is based on a design of services which mirror
real-world business activities comprising the enterprise (or
inter-enterprise) business processes.

Rationale:

Service orientation delivers enterprise agility and Boundaryless Information Flow.

Implications:

Service representation utilizes business descriptions to provide
context (i.e., business process, goal, rule, policy, service interface,
and service component) and implements services using service
orchestration Service orientation places unique requirements on the infrastructure,
and implementations should use open standards to realize
interoperability and location transparency Implementations are environment-specific; they are constrained or
enabled by context and must be described within that context Strong governance of service representation and implementation is
required A “Litmus Test”, which determines a “good service”, is required

</details>

<a id="tag_02_06_01_07"></a>
## 2.6.1.7. Principle 7: Compliance with Law

概念：信息管理遵守相关法律、政策和法规。

适用条件：采集、留存及管理数据等活动。

逻辑关系：法规变化可驱动流程应用变化；业务改进也可推动政策改进。

决策方法：确认适用规则、提供教育和查阅入口。

制品及证据：适用规则目录及变更追溯。

适用边界：本节不是现行法条清单，不能据此判断具体法律合规。

来源块：C220-web-2025:03-adm-techniques:b00126, C220-web-2025:03-adm-techniques:b00127, C220-web-2025:03-adm-techniques:b00128, C220-web-2025:03-adm-techniques:b00129, C220-web-2025:03-adm-techniques:b00130, C220-web-2025:03-adm-techniques:b00131, C220-web-2025:03-adm-techniques:b00132

<details><summary>展开本节完整英文来源</summary>

2.6.1.7. Principle 7: Compliance with Law

Statement:

Enterprise information management processes comply with all relevant
laws, policies, and regulations.

Rationale:

Enterprise policy is to abide by laws, policies, and regulations. This
will not preclude business process improvements that lead to changes in
policies and regulations.

Implications:

The enterprise must be mindful to comply with laws, regulations, and
external policies regarding the collection, retention, and management of
data Education and access to the rules Efficiency, need, and common sense are not the only drivers. Changes in
the law and changes in regulations may drive changes in our processes or
applications.

</details>

<a id="tag_02_06_01_08"></a>
## 2.6.1.8. Principle 8: IT Responsibility

概念：IT组织负责使流程与基础设施满足用户定义的功能、服务水平、成本和交付时间要求。

适用条件：业务需求进入IT交付和运营时。

逻辑关系：业务期望需与能力和成本对齐，集成模型支撑优质方案。

决策方法：建立项目优先级与业务期望管理流程。

制品及证据：数据、应用、技术模型及服务承诺。

适用边界：职责不证明组织已拥有足够人力或容量。

来源块：C220-web-2025:03-adm-techniques:b00133, C220-web-2025:03-adm-techniques:b00134, C220-web-2025:03-adm-techniques:b00135, C220-web-2025:03-adm-techniques:b00136, C220-web-2025:03-adm-techniques:b00137, C220-web-2025:03-adm-techniques:b00138, C220-web-2025:03-adm-techniques:b00139

<details><summary>展开本节完整英文来源</summary>

2.6.1.8. Principle 8: IT Responsibility

Statement:

The IT organization is responsible for owning and implementing IT
processes and infrastructure that enable solutions to meet user-defined
requirements for functionality, service levels, cost, and delivery
timing.

Rationale:

Effectively align expectations with capabilities and costs so that all
projects are cost-effective. Efficient and effective solutions have
reasonable costs and clear benefits.

Implications:

A process must be created to prioritize projects The IT function must define processes to manage business unit
expectations Data, application, and technology models must be created to enable
integrated quality solutions and to maximize results

</details>

<a id="tag_02_06_01_09"></a>
## 2.6.1.9. Principle 9: Protection of Intellectual Property

概念：知识产权保护应贯穿架构、实施和治理。

适用条件：企业知识产权存在于IT与非IT流程时。

逻辑关系：实际控制常在IT域实施，人员和技术均需受政策约束。

决策方法：确认保护政策如何防泄漏并降低责任。

制品及证据：知识产权资产及人员/IT安全政策。

适用边界：示例外链仅是资源，不是政策强制来源。

来源块：C220-web-2025:03-adm-techniques:b00140, C220-web-2025:03-adm-techniques:b00141, C220-web-2025:03-adm-techniques:b00142, C220-web-2025:03-adm-techniques:b00143, C220-web-2025:03-adm-techniques:b00144, C220-web-2025:03-adm-techniques:b00145, C220-web-2025:03-adm-techniques:b00146

<details><summary>展开本节完整英文来源</summary>

2.6.1.9. Principle 9: Protection of Intellectual Property

Statement:

The enterprise’s Intellectual Property (IP) must be protected. This
protection must be reflected in the IT architecture, implementation, and
governance processes.

Rationale:

A major part of an enterprise’s IP is hosted in the IT domain.

Implications:

While protection of IP assets is everybody’s business, much of the
actual protection is implemented in the IT domain — even trust in non-IT
processes can be managed by IT processes (email, mandatory notes, etc.) A security policy, governing human and IT actors, will be required
that can substantially improve protection of IP; this must be capable of
both avoiding compromises and reducing liabilities Resources on such policies can be found at the SANS Institute (refer
to www.sans.org/security-resources/policies )

</details>

<a id="tag_02_06_02"></a>
## 2.6.2. Data Principles

概念：六个数据示例从价值、共享和可访问延伸到责任、语义及安全。

适用条件：建立数据管理原则集。

逻辑关系：前三项紧密相关，后续原则解决质量、定义与保护。

决策方法：同时检验可访问、安全、共享和责任。

制品及证据：数据原则组。

适用边界：分组本身没有授权用户修改或披露数据。

来源块：C220-web-2025:03-adm-techniques:b00147

<details><summary>展开本节完整英文来源</summary>

2.6.2. Data Principles

</details>

<a id="tag_02_06_02_01"></a>
## 2.6.2.1. Principle 10: Data is an Asset

概念：数据有可衡量企业价值，应作为资产管理。

适用条件：数据用于及时准确决策。

逻辑关系：质量、位置、可信度与获取能力共同支撑价值。

决策方法：赋予企业层数据管理责任者所需权限和手段，测量并改进质量。

制品及证据：责任分配、质量指标及错误防纠程序。

适用边界：数据价值不能用无依据的收益数字代替。

来源块：C220-web-2025:03-adm-techniques:b00148, C220-web-2025:03-adm-techniques:b00149, C220-web-2025:03-adm-techniques:b00150, C220-web-2025:03-adm-techniques:b00151, C220-web-2025:03-adm-techniques:b00152, C220-web-2025:03-adm-techniques:b00153, C220-web-2025:03-adm-techniques:b00154

<details><summary>展开本节完整英文来源</summary>

2.6.2.1. Principle 10: Data is an Asset

Statement:

Data is an asset that has value to the enterprise and is managed accordingly.

Rationale:

Data is a valuable corporate resource; it has real, measurable value. In simple terms, the purpose of data is to aid decision-making. Accurate,
timely data is critical to accurate, timely decisions. Most corporate assets are carefully managed, and data is no exception. Data is the
foundation of our decision-making, so we must also carefully manage data to ensure that we know where it is, can rely upon its accuracy, and can
obtain it when and where we need it.

Implications:

This is one of three closely-related principles regarding data: data
is an asset; data is shared; and data is easily accessible The implication is there is an education task to ensure that all organizations within the enterprise understand the relationship between
value of data, sharing of data, and accessibility to data. Stewards must have the authority and means to manage the data for
which they are accountable There must be a cultural transition from “data ownership” thinking to
“data stewardship” thinking The role of data steward is critical because obsolete, incorrect, or
inconsistent data could be passed to enterprise personnel and adversely
affect decisions across the enterprise Part of the role of data steward, who manages the data, is to ensure
data quality Procedures must be developed and used to prevent and correct errors in
the information and to improve those processes that produce flawed
information. Data quality will need to be measured and steps taken to
improve data quality — it is probable that policy and procedures will
need to be developed for this as well. A forum with comprehensive enterprise-wide representation should
decide on process changes suggested by the steward Since data is an asset of value to the entire enterprise, data
stewards accountable for properly managing the data must be assigned at
the enterprise level

</details>

<a id="tag_02_06_02_02"></a>
## 2.6.2.2. Principle 11: Data is Shared

概念：用户可获得完成职责所需数据，并跨职能组织共享。

适用条件：短期整合遗留系统、长期替换和持续开发。

逻辑关系：共同模型、元数据、访问政策和工具形成虚拟单一数据源。

决策方法：设计迁移、元数据存储和新系统访问规则，同时遵守保密限制。

制品及证据：共享模型、元数据、迁移和访问规范。

适用边界：共享不得破坏机密性；虚拟单源不要求一套物理数据库。

来源块：C220-web-2025:03-adm-techniques:b00155, C220-web-2025:03-adm-techniques:b00156, C220-web-2025:03-adm-techniques:b00157, C220-web-2025:03-adm-techniques:b00158, C220-web-2025:03-adm-techniques:b00159, C220-web-2025:03-adm-techniques:b00160, C220-web-2025:03-adm-techniques:b00161, C220-web-2025:03-adm-techniques:b00162

<details><summary>展开本节完整英文来源</summary>

2.6.2.2. Principle 11: Data is Shared

Statement:

Users have access to the data necessary to perform their duties;
therefore, data is shared across enterprise functions and organizations.

Rationale:

Timely access to accurate data is essential to improving the quality and
efficiency of enterprise decision-making. It is less costly to maintain
timely, accurate data in a single application, and then share it, than
it is to maintain duplicative data in multiple applications. The
enterprise holds a wealth of data, but it is stored in hundreds of
incompatible stovepipe databases. The speed of data collection,
creation, transfer, and assimilation is driven by the ability of the
organization to efficiently share these islands of data across the
organization.

Shared data will result in improved decisions since we will rely on
fewer (ultimately one virtual) sources of more accurate and timely
managed data for all of our decision-making. Electronically shared data
will result in increased efficiency when existing data entities can be
used, without re-keying, to create new entities.

Implications:

This is one of three closely-related principles regarding data: data
is an asset; data is shared; and data is easily accessible The implication is there is an education task to ensure that all
organizations within the enterprise understand the relationship between
value of data, sharing of data, and accessibility to data. To enable data sharing we must develop and abide by a common set of
policies, procedures, and standards governing data management and access
for both the short and the long term For the short term, to preserve our significant investment in legacy
systems, we must invest in software capable of migrating legacy system
data into a shared data environment We will also need to develop standard data models, data elements, and
other metadata that defines this shared environment and develop a
repository system for storing this metadata to make it accessible For the long term, as legacy systems are replaced, we must adopt and
enforce common data access policies and guidelines for new application
developers to ensure that data in new applications remains available to
the shared environment and that data in the shared environment can
continue to be used by the new applications For both the short term and the long term we must adopt common methods
and tools for creating, maintaining, and accessing the data shared
across the enterprise Data sharing will require a significant cultural change This principle of data sharing will continually “bump up against” the
principle of data security — under no circumstances will the data
sharing principle cause confidential data to be compromised Data made available for sharing will have to be relied upon by all
users to execute their respective tasks This will ensure that only the most accurate and timely data is relied
upon for decision-making. Shared data will become the enterprise-wide
“virtual single source” of data.

</details>

<a id="tag_02_06_02_03"></a>
## 2.6.2.3. Principle 12: Data is Accessible

概念：可访问性强调不同用户容易获得及呈现信息。

适用条件：支持多种任务和访问方法。

逻辑关系：得到数据不等于正确理解，也不等于修改或披露权。

决策方法：检验用户可理解性与实际权限，安排教育。

制品及证据：访问设计、解释说明及权限矩阵。

适用边界：不能以能读到文件推断深度理解或发布授权。

来源块：C220-web-2025:03-adm-techniques:b00163, C220-web-2025:03-adm-techniques:b00164, C220-web-2025:03-adm-techniques:b00165, C220-web-2025:03-adm-techniques:b00166, C220-web-2025:03-adm-techniques:b00167, C220-web-2025:03-adm-techniques:b00168, C220-web-2025:03-adm-techniques:b00169

<details><summary>展开本节完整英文来源</summary>

2.6.2.3. Principle 12: Data is Accessible

Statement:

Data is accessible for users to perform their functions.

Rationale:

Wide access to data leads to efficiency and effectiveness in
decision-making, and affords a timely response to information requests
and service delivery. Using information must be considered from an
enterprise perspective to allow access by a wide variety of users. Staff
time is saved and consistency of data is improved.

Implications:

This is one of three closely-related principles regarding data: data
is an asset; data is shared; and data is easily accessible The implication is there is an education task to ensure that all
organizations within the enterprise understand the relationship between
value of data, sharing of data, and accessibility to data. Accessibility involves the ease with which users obtain information The way information is accessed and displayed must be sufficiently
adaptable to meet a wide range of enterprise users and their
corresponding methods of access Access to data does not constitute understanding of the data —
personnel should take caution not to misinterpret information Access to data does not necessarily grant the user access rights to
modify or disclose the data This will require an education process and a change in the
organizational culture, which currently supports a belief in “ownership”
of data by functional units.

</details>

<a id="tag_02_06_02_04"></a>
## 2.6.2.4. Principle 13: Data Trustee

概念：每个数据元素有对质量负责的trustee。

适用条件：共享使多个组织依赖共同信息时。

逻辑关系：trustee负责准确性和及时性；steward可另覆盖标准化和定义。

决策方法：识别真实来源、尽早一次采集验证并落实质量责任。

制品及证据：来源依据、责任映射和质量控制。

适用边界：源资料不必公开且源头不必就是trustee；两角色不要直接译成同一职责。

来源块：C220-web-2025:03-adm-techniques:b00170, C220-web-2025:03-adm-techniques:b00171, C220-web-2025:03-adm-techniques:b00172, C220-web-2025:03-adm-techniques:b00173, C220-web-2025:03-adm-techniques:b00174, C220-web-2025:03-adm-techniques:b00175, C220-web-2025:03-adm-techniques:b00176, C220-web-2025:03-adm-techniques:b00177

<details><summary>展开本节完整英文来源</summary>

2.6.2.4. Principle 13: Data Trustee

Statement:

Each data element has a trustee accountable for data quality.

Rationale:

One of the benefits of an architected environment is the ability to share data (e.g., text, video, sound, etc.) across the enterprise. As the degree of data sharing grows and business units rely upon common
information, it becomes essential that only the data trustee makes decisions about the content of data. Since data can lose its integrity when it is entered multiple times, the data trustee will have sole
responsibility for data entry which eliminates redundant human effort and data storage resources.

Note: A trustee is different than a steward — a trustee is responsible for accuracy and currency of the data, while responsibilities of a steward may be broader and include data standardization and definition tasks.

Implications:

Real trusteeship dissolves the data “ownership” issues and allows the
data to be available to meet all users’ needs This implies that a cultural change from data “ownership” to data
“trusteeship” may be required. The data trustee will be responsible for meeting quality requirements
levied upon the data for which the trustee is accountable It is essential that the trustee has the ability to provide user
confidence in the data based upon attributes such as “data source” It is essential to identify the true source of the data in order that
the data authority can be assigned this trustee responsibility This does not mean that classified sources will be revealed nor does it
mean the source will be the trustee. Information should be captured electronically once and immediately
validated as close to the source as possible Quality control measures must be implemented to ensure the integrity of
the data. As a result of sharing data across the enterprise, the trustee is
accountable and responsible for the accuracy and currency of their
designated data element(s) and, subsequently, must then recognize the
importance of this trusteeship responsibility

</details>

<a id="tag_02_06_02_05"></a>
## 2.6.2.5. Principle 14: Common Vocabulary and Data Definitions

概念：企业一致定义数据且使词汇可理解、可用。

适用条件：跨系统交换、应用开发及业务沟通。

逻辑关系：公共词汇与数据元素定义相关但不完全同一工作。

决策方法：新定义与企业词汇表协调，消除局部歧义，指定职能数据管理职责。

制品及证据：业务词汇表、定义协调记录。

适用边界：有数据管理岗位名称不证明定义问题已解决。

来源块：C220-web-2025:03-adm-techniques:b00178, C220-web-2025:03-adm-techniques:b00179, C220-web-2025:03-adm-techniques:b00180, C220-web-2025:03-adm-techniques:b00181, C220-web-2025:03-adm-techniques:b00182, C220-web-2025:03-adm-techniques:b00183, C220-web-2025:03-adm-techniques:b00184

<details><summary>展开本节完整英文来源</summary>

2.6.2.5. Principle 14: Common Vocabulary and Data Definitions

Statement:

Data is defined consistently throughout the enterprise, and the
definitions are understandable and available to all users.

Rationale:

The data that will be used in the development of applications must have a common definition throughout the Headquarters to enable sharing of
data. A common vocabulary will facilitate communications and enable dialog to be effective. In addition, it is required to interface systems and exchange data.

Implications:

We are lulled into thinking that this issue is adequately addressed because there are people with “data administration” job titles and forums with charters implying responsibility Significant additional energy and resources must be committed to this task. It is key to the success of efforts to improve the information environment. This is separate from but related to the issue of data
element definition, which is addressed by a broad community — this is more like a common vocabulary and definition. The enterprise must establish the initial common vocabulary for the business; the definitions will be used uniformly throughout the enterprise Whenever a new data definition is required, the definition effort will be co-ordinated and reconciled with the corporate “glossary” of data
descriptions The enterprise data administrator will provide this co-ordination. Ambiguities resulting from multiple parochial definitions of data must
give way to accepted enterprise-wide definitions and understanding Multiple data standardization initiatives need to be co-ordinated Functional data administration responsibilities must be assigned

</details>

<a id="tag_02_06_02_06"></a>
## 2.6.2.6. Principle 15: Data Security

概念：保护数据免于未授权使用、泄露和操纵。

适用条件：涉及敏感、决策前、专有或分类信息。

逻辑关系：开放共享需与保护平衡；聚合可能提高敏感级别。

决策方法：在数据元素层设计分类、访问和保护期限，评估聚合影响。

制品及证据：分类策略、数据安全控制和定期复审。

适用边界：源示例国家安全情境不可无条件移植到一般企业。

来源块：C220-web-2025:03-adm-techniques:b00185, C220-web-2025:03-adm-techniques:b00186, C220-web-2025:03-adm-techniques:b00187, C220-web-2025:03-adm-techniques:b00188, C220-web-2025:03-adm-techniques:b00189, C220-web-2025:03-adm-techniques:b00190, C220-web-2025:03-adm-techniques:b00191, C220-web-2025:03-adm-techniques:b00192

<details><summary>展开本节完整英文来源</summary>

2.6.2.6. Principle 15: Data Security

Statement:

Data is protected from unauthorized use and disclosure. In addition to the traditional aspects of national security classification, this
includes, but is not limited to, protection of pre-decisional, sensitive, source selection-sensitive, and proprietary information.

Rationale:

Open sharing of information and the release of information via relevant legislation must be balanced against the need to restrict the
availability of classified, proprietary, and sensitive information.

Existing laws and regulations require the safeguarding of national security and the privacy of data, while permitting free and open access.
Pre-decisional (work-in-progress, not yet authorized for release) information must be protected to avoid unwarranted speculation, misinterpretation, and inappropriate use.

Implications:

Aggregation of data, both classified and not, will create a large target requiring review and de-classification procedures to maintain appropriate control Data owners and/or functional users must determine whether the aggregation results in an increased classification level. Appropriate policy and procedures will be needed to handle this review and
de-classification. Access to information based on a need-to-know policy will force regular reviews of the body of information. The current practice of separate systems to contain different classifications needs to be rethought Is there a software solution that enables the segregation of classified and unclassified data? The current hardware solution is unwieldy, inefficient, and costly. It is more expensive to manage unclassified data on a classified system. In order to adequately provide access to open information while maintaining secure information, security needs must be identified and developed at the data level, not the application level Data security safeguards can be put in place to restrict access to “view only” or “never see” Sensitivity labeling for access to pre-decisional, decisional, classified, sensitive, or proprietary information must be determined. Security must be designed into data elements from the beginning; it cannot be added later Systems, data, and technologies must be protected from unauthorized access and manipulation. Information at Headquarters must be safeguarded
against inadvertent or unauthorized alteration, sabotage, disaster, or disclosure. New policies are needed on managing duration of protection for pre-decisional information and other works-in-progress, in consideration of content freshness

</details>

<a id="tag_02_06_03"></a>
## 2.6.3. Application Principles

概念：应用示例讨论技术独立及易用性。

适用条件：业务功能需长期演进且面向不同用户时。

逻辑关系：技术选择应服务用户任务。

决策方法：分别检查可移植性和用户可用性。

制品及证据：应用原则及验收准则。

适用边界：只有分组，不增加额外实施步骤。

来源块：C220-web-2025:03-adm-techniques:b00193

<details><summary>展开本节完整英文来源</summary>

2.6.3. Application Principles

</details>

<a id="tag_02_06_03_01"></a>
## 2.6.3.1. Principle 16: Technology Independence

概念：应用尽量独立于特定硬件和操作系统。

适用条件：控制淘汰、供应商依赖及升级成本。

逻辑关系：接口、中间件与可移植标准减弱绑定；COTS/GOTS选择可能受限。

决策方法：评估真实平台依赖和解耦成本。

制品及证据：移植标准、子系统接口及依赖记录。

适用边界：Java只是原文例子，不是当前强制或最佳技术。

来源块：C220-web-2025:03-adm-techniques:b00194, C220-web-2025:03-adm-techniques:b00195, C220-web-2025:03-adm-techniques:b00196, C220-web-2025:03-adm-techniques:b00197, C220-web-2025:03-adm-techniques:b00198, C220-web-2025:03-adm-techniques:b00199, C220-web-2025:03-adm-techniques:b00200, C220-web-2025:03-adm-techniques:b00201

<details><summary>展开本节完整英文来源</summary>

2.6.3.1. Principle 16: Technology Independence

Statement:

Applications are independent of specific technology choices and
therefore can operate on a variety of technology platforms.

Rationale:

Independence of applications from the underlying technology allows
applications to be developed, upgraded, and operated in the most
cost-effective and timely way. Otherwise technology, which is subject to
continual obsolescence and vendor dependence, becomes the driver rather than the user requirements themselves.

Realizing that every decision made with respect to IT makes us dependent
on that technology, the intent of this principle is to ensure that
Application Software is not dependent on specific hardware and operating
systems software.

Implications:

This principle will require standards which support portability For Commercial Off-The-Shelf (COTS) and Government Off-The-Shelf (GOTS) applications, there may be limited current choices, as many of these applications are technology and platform-dependent Subsystem interfaces will need to be developed to enable legacy applications to interoperate with applications and operating environments developed under the Enterprise Architecture Middleware should be used to decouple applications from specific software solutions As an example, this principle could lead to use of Java ® , and future Java-like protocols, which give a high degree of priority to platform-independence

</details>

<a id="tag_02_06_03_02"></a>
## 2.6.3.2. Principle 17: Ease-of-Use

概念：应用应易用，使用户专注任务而非底层技术。

适用条件：不同地点、语言、训练和身体能力的用户。

逻辑关系：一致交互与人体工程学降低训练和误用风险。

决策方法：制定共同外观准则和可用性测试，不作狭窄用户假设。

制品及证据：用户界面标准、可用性测试标准及结果。

适用边界：直觉式使用比喻不是量化验收方法。

来源块：C220-web-2025:03-adm-techniques:b00202, C220-web-2025:03-adm-techniques:b00203, C220-web-2025:03-adm-techniques:b00204, C220-web-2025:03-adm-techniques:b00205, C220-web-2025:03-adm-techniques:b00206, C220-web-2025:03-adm-techniques:b00207, C220-web-2025:03-adm-techniques:b00208, C220-web-2025:03-adm-techniques:b00209

<details><summary>展开本节完整英文来源</summary>

2.6.3.2. Principle 17: Ease-of-Use

Statement:

Applications are easy to use. The underlying technology is transparent
to users, so they can concentrate on tasks at hand.

Rationale:

The more a user has to understand the underlying technology, the less
productive that user is. Ease-of-use is a positive incentive for use of
applications. It encourages users to work within the integrated
information environment instead of developing isolated systems to
accomplish the task outside of the enterprise’s integrated information
environment. Most of the knowledge required to operate one system will
be similar to others. Training is kept to a minimum, and the risk of
using a system improperly is low.

Using an application should be as intuitive as driving a different car.

Implications:

Applications will be required to have a common “look-and-feel” and
support ergonomic requirements; hence, the common look-and-feel standard
must be designed and usability test criteria must be developed Guidelines for user interfaces should not be constrained by narrow
assumptions about user location, language, systems training, or physical
capability Factors such as linguistics, customer physical infirmities (visual
acuity, ability to use keyboard/mouse), and proficiency in the use of
technology have broad ramifications in determining the ease-of-use of an
application.

</details>

<a id="tag_02_06_04"></a>
## 2.6.4. Technology Principles

概念：技术示例包括需求驱动变化、响应变化、控制多样性和互操作。

适用条件：处理技术演进与企业成本。

逻辑关系：变化速度与企业整体一致性可能冲突。

决策方法：记录权衡和标准更新例外。

制品及证据：技术原则组。

适用边界：示例不可当永久冻结技术基线。

来源块：C220-web-2025:03-adm-techniques:b00210

<details><summary>展开本节完整英文来源</summary>

2.6.4. Technology Principles

</details>

<a id="tag_02_06_04_01"></a>
## 2.6.4.1. Principle 18: Requirements-Based Change

概念：应用技术变更须响应记录的业务需要。

适用条件：预算和实施变更审批。

逻辑关系：技术机会也可改变业务需求；快速响应本身是业务需要。

决策方法：审查架构影响和业务依据，避免文档流程阻塞合理响应。

制品及证据：业务需求、架构变更评估和资金依据。

适用边界：不能将需求驱动解读为禁止技术引发业务机会。

来源块：C220-web-2025:03-adm-techniques:b00211, C220-web-2025:03-adm-techniques:b00212, C220-web-2025:03-adm-techniques:b00213, C220-web-2025:03-adm-techniques:b00214, C220-web-2025:03-adm-techniques:b00215, C220-web-2025:03-adm-techniques:b00216, C220-web-2025:03-adm-techniques:b00217, C220-web-2025:03-adm-techniques:b00218, C220-web-2025:03-adm-techniques:b00219

<details><summary>展开本节完整英文来源</summary>

2.6.4.1. Principle 18: Requirements-Based Change

Statement:

Only in response to business needs are changes to applications and
technology made.

Rationale:

This principle will foster an atmosphere where the information
environment changes in response to the needs of the business, rather
than having the business change in response to IT changes. This is to
ensure that the purpose of the information support — the transaction of
business — is the basis for any proposed change.

Unintended effects on business due to IT changes will be minimized.

A change in technology may provide an opportunity to improve the
business process and, hence, change business needs.

Implications:

Changes in implementation will follow full examination of the proposed
changes using the Enterprise Architecture There is no funding for a technical improvement or system development
unless a documented business need exists Change management processes conforming to this principle will be
developed and implemented This principle may bump up against the responsive change principle We must ensure the requirements documentation process does not hinder
responsive change to meet legitimate business needs. The purpose of this
principle is to keep the focus on business, not technology needs —
responsive change is also a business need.

</details>

<a id="tag_02_06_04_02"></a>
## 2.6.4.2. Principle 19: Responsive Change Management

概念：及时实施企业信息环境变更。

适用条件：用户对环境提出变化需求。

逻辑关系：响应变化需业务专家协作、维护架构并可能增加资源。

决策方法：检验变更流程延迟及与企业共用/整体收益原则的冲突。

制品及证据：变化流程、更新架构和资源安排。

适用边界：及时性没有原文统一天数。

来源块：C220-web-2025:03-adm-techniques:b00220, C220-web-2025:03-adm-techniques:b00221, C220-web-2025:03-adm-techniques:b00222, C220-web-2025:03-adm-techniques:b00223, C220-web-2025:03-adm-techniques:b00224, C220-web-2025:03-adm-techniques:b00225, C220-web-2025:03-adm-techniques:b00226

<details><summary>展开本节完整英文来源</summary>

2.6.4.2. Principle 19: Responsive Change Management

Statement:

Changes to the enterprise information environment are implemented in a
timely manner.

Rationale:

If people are to be expected to work within the enterprise information environment, that information environment must be responsive to their needs.

Implications:

Processes for managing and implementing change must be developed that
do not create delays A user who feels a need for change will need to connect with a
“business expert” to facilitate explanation and implementation of that
need If changes are going to be made, the architecture must be kept updated Adopting this principle might require additional resources This will conflict with other principles (e.g., maximum
enterprise-wide benefit, enterprise-wide applications, etc.)

</details>

<a id="tag_02_06_04_03"></a>
## 2.6.4.3. Principle 20: Control Technical Diversity

概念：控制技术多样性以减少维护技能和互联成本。

适用条件：选择技术和更新企业技术蓝图。

逻辑关系：有限组件产生规模经济；兼容、效率和必要能力可支持新增技术。

决策方法：设置扩充可接受技术集的过程。

制品及证据：技术蓝图、采购标准和扩充批准记录。

适用边界：控制多样性不等于冻结基线或禁止技术进步。

来源块：C220-web-2025:03-adm-techniques:b00227, C220-web-2025:03-adm-techniques:b00228, C220-web-2025:03-adm-techniques:b00229, C220-web-2025:03-adm-techniques:b00230, C220-web-2025:03-adm-techniques:b00231, C220-web-2025:03-adm-techniques:b00232, C220-web-2025:03-adm-techniques:b00233, C220-web-2025:03-adm-techniques:b00234, C220-web-2025:03-adm-techniques:b00235

<details><summary>展开本节完整英文来源</summary>

2.6.4.3. Principle 20: Control Technical Diversity

Statement:

Technological diversity is controlled to minimize the non-trivial cost
of maintaining expertise in and connectivity between multiple processing
environments.

Rationale:

There is a real, non-trivial cost of infrastructure required to support
alternative technologies for processing environments. There are further
infrastructure costs incurred to keep multiple processor constructs
interconnected and maintained.

Limiting the number of supported components will simplify
maintainability and reduce costs.

The business advantages of minimum technical diversity include: standard
packaging of components; predictable implementation impact; predictable
valuations and returns; redefined testing; utility status; and increased
flexibility to accommodate technological advancements. Common technology
across the enterprise brings the benefits of economies of scale to the
enterprise. Technical administration and support costs are better
controlled when limited resources can focus on this shared set of
technology.

Implications:

Policies, standards, and procedures that govern the acquisition of
technology must be tied directly to this principle Technology choices will be constrained by the choices available within
the technology blueprint Procedures for augmenting the acceptable technology set to meet evolving
requirements will have to be developed and put in place. The technology baseline is not being frozen Technology advances are welcomed and will change the technology
blueprint when compatibility with the current infrastructure,
improvement in operational efficiency, or a required capability has been
demonstrated.

</details>

<a id="tag_02_06_04_04"></a>
## 2.6.4.4. Principle 21: Interoperability

概念：软硬件遵守促进数据、应用、技术互操作的标准。

适用条件：保护投资及支持供应商和供应链协作。

逻辑关系：标准需制定、定期修订并有例外流程。

决策方法：非标准方案必须有有说服力的业务理由。

制品及证据：平台清单、互操作标准及例外证据。

适用边界：符合标准还需检验实际业务交换能力。

来源块：C220-web-2025:03-adm-techniques:b00236, C220-web-2025:03-adm-techniques:b00237, C220-web-2025:03-adm-techniques:b00238, C220-web-2025:03-adm-techniques:b00239, C220-web-2025:03-adm-techniques:b00240, C220-web-2025:03-adm-techniques:b00241, C220-web-2025:03-adm-techniques:b00242

<details><summary>展开本节完整英文来源</summary>

2.6.4.4. Principle 21: Interoperability

Statement:

Software and hardware should conform to defined standards that promote
interoperability for data, applications, and technology.

Rationale:

Standards help ensure consistency, thus improving the ability to manage
systems and improve user satisfaction, and protect existing IT
investments, thus maximizing return on investment and reducing costs.
Standards for interoperability additionally help ensure support from
multiple vendors for their products, and facilitate supply chain
integration.

Implications:

Interoperability standards and industry standards will be followed
unless there is a compelling business reason to implement a non-standard
solution A process for setting standards, reviewing and revising them
periodically, and granting exceptions must be established The existing IT platforms must be identified and documented

</details>

<a id="chap03"></a>
## 3. Stakeholder Management

概念：利益相关者管理旨在获得支持并处理利益冲突。

适用条件：任何架构举措均需识别受影响及影响它的人。

逻辑关系：本章按识别、分类、策略、交付物逐步组织。

决策方法：从真实人员和关切出发制定沟通策略。

制品及证据：利益相关者目录和参与计划。

适用边界：图中分类不是当前组织事实。

来源块：C220-web-2025:03-adm-techniques:b00243

<details><summary>展开本节完整英文来源</summary>

3. Stakeholder Management

</details>

<a id="tag_03_01"></a>
## 3.1. Introduction

概念：早期持续沟通可改善模型、资源支持及反应预判。

适用条件：架构会产生得益和受损群体时。

逻辑关系：识别目标竞争才能安排冲突解决。

决策方法：分析谁获益、受损、贡献和影响架构。

制品及证据：支持与阻碍判断、冲突处理策略。

适用边界：支持倾向需证据，不能从职位自动评级。

来源块：C220-web-2025:03-adm-techniques:b00244, C220-web-2025:03-adm-techniques:b00245, C220-web-2025:03-adm-techniques:b00246, C220-web-2025:03-adm-techniques:b00247, C220-web-2025:03-adm-techniques:b00248

<details><summary>展开本节完整英文来源</summary>

3.1. Introduction

Stakeholder management is an important discipline that successful
architecture practitioners can use to win support from others. It helps
them ensure that their projects succeed where others fail.

The benefits of successful stakeholder management are that:

The most powerful stakeholders can be identified early and their input
can then be used to shape the architecture; this ensures their support
and improves the quality of the models produced Support from the more powerful stakeholders will help the engagement
win more resources, thus making the architecture engagement more likely
to succeed By communicating with stakeholders early and frequently, the
architecture team can ensure that they fully understand the architecture
process, and the benefits of Enterprise Architecture; this means they
can support the architecture team more actively when necessary The architecture team can more effectively anticipate likely reactions
to the architecture models and reports, and can build into the plan the
actions that will be needed to capitalize on positive reactions while
avoiding or addressing any negative reactions The architecture team can identify conflicting or competing objectives
among stakeholders early and develop a strategy to resolve the issues
arising from them

It is essential in any initiative to identify the individuals and groups
within the organization who will contribute to the development of the
architecture, identify those that will gain and those that will lose
from its introduction, and then develop a strategy for dealing with
them.

</details>

<a id="tag_03_02"></a>
## 3.2. Approach to Stakeholder Management

概念：在Phase A开展分析，并在后续阶段持续更新。

适用条件：涉及不同域和多方利益的复杂架构。

逻辑关系：stakeholder—concern—viewpoint—view支撑不同视图。

决策方法：按关切选择视图，并更新新出现的利益相关者。

制品及证据：更新日志、关切视图关联。

适用边界：不是为每方复制互不一致模型。

来源块：C220-web-2025:03-adm-techniques:b00249, C220-web-2025:03-adm-techniques:b00250, C220-web-2025:03-adm-techniques:b00251, C220-web-2025:03-adm-techniques:b00252, C220-web-2025:03-adm-techniques:b00253, C220-web-2025:03-adm-techniques:b00254

<details><summary>展开本节完整英文来源</summary>

3.2. Approach to Stakeholder Management

Stakeholder analysis should be used during Phase A (Architecture Vision)
to identify the key players in the engagement, and also be updated
throughout each phase; different stakeholders may be uncovered as the
engagement progresses through into Opportunities & Solutions, Migration
Planning, and Architecture Change Management.

Complex architectures are extremely hard to manage, not only in terms of
the architecture development process itself, but also in terms of
obtaining agreement from the large numbers of stakeholders touched by
it.

For example, just as a building architect will create wiring diagrams,
floor plans, and elevations to describe different facets of a building
to its different stakeholders (electricians, owners, planning
officials), so an Enterprise Architect must create different
architecture views of the Business, Information Systems, and Technology
Architecture for the stakeholders who have concerns related to these
aspects.

The TOGAF Standard specifically identifies this issue throughout the ADM
through the following concepts (see the TOGAF Standard — Architecture Content ):

Architecture View Architecture Viewpoint Concern Stakeholder

</details>

<a id="tag_03_03"></a>
## 3.3. Steps in the Stakeholder Management Process

概念：推荐管理活动细化为识别、立场、参与方式和制品裁剪。

适用条件：执行本章管理方法。

逻辑关系：前面分析结果为后面策略和制品提供输入。

决策方法：结合子节安排可复审的管理活动。

制品及证据：管理活动与产物清单。

适用边界：推荐活动不是不允许回返的固定顺序。

来源块：C220-web-2025:03-adm-techniques:b00255, C220-web-2025:03-adm-techniques:b00256

<details><summary>展开本节完整英文来源</summary>

3.3. Steps in the Stakeholder Management Process

The following sections detail recommended stakeholder management
activity.

</details>

<a id="tag_03_03_01"></a>
## 3.3.1. Identify Stakeholders

概念：受影响、拥有资源/决策权或非正式影响力的人均可能是利益相关者。

适用条件：识别正式结构之外的真实贡献者。

逻辑关系：一人可属于多群体；组织最终需定位可沟通的具体个人。

决策方法：从收益损失、采购、资源、技能和会议影响证据查找。

制品及证据：具体人员及其群体、影响依据。

适用边界：不能只从组织图推断实际权力。

来源块：C220-web-2025:03-adm-techniques:b00257, C220-web-2025:03-adm-techniques:b00258, C220-web-2025:03-adm-techniques:b00259, C220-web-2025:03-adm-techniques:b00260, C220-web-2025:03-adm-techniques:b00261, C220-web-2025:03-adm-techniques:b00262, C220-web-2025:03-adm-techniques:b00263, C220-web-2025:03-adm-techniques:b00264, C220-web-2025:03-adm-techniques:b00265, C220-web-2025:03-adm-techniques:b00266

<details><summary>展开本节完整英文来源</summary>

3.3.1. Identify Stakeholders

Identify the key stakeholders of the Enterprise Architecture.

The first task is to work out who the main Enterprise Architecture
stakeholders are. As part of this, think of all the people who are
affected by it, who have influence or power over it, or have an interest
in its successful or unsuccessful conclusion.

It might include senior executives, project organization roles, client
organization roles, system developers, alliance partners, suppliers, IT
operations, customers, etc.

When identifying stakeholders there is a danger of concentrating too
heavily on the formal structure of an organization as the basis for
identification. Informal stakeholder groups may be just as powerful and
influential as the formal ones.

Most individuals will belong to more than one stakeholder group, and
these groups tend to arise as a result of specific events.

Look at who is impacted by the Enterprise Architecture project:

Who gains and who loses from this change? Who controls change management of processes? Who designs new systems? Who will make the decisions? Who procures IT systems and who decides what to buy? Who controls resources? Who has specialist skills the project needs? Who has influence?

In particular, influencers need to be identified. These will be well
respected and moving up, participate in important meetings and
committees (look at meeting minutes), know what’s going on in the
company, be valued by their peers and superiors, and not necessarily be
in any formal position of power.

Although stakeholders may be both organizations and people, ultimately
the Enterprise Architecture team will need to communicate with people.
It is the correct individual stakeholders within a stakeholder
organization that need to be formally identified.

</details>

<a id="tag_03_03_01_01"></a>
## 3.3.1.1. Sample Stakeholder Analysis

概念：图示22类、5大类，包括显性与隐性贡献团队。

适用条件：用作识别提示。

逻辑关系：支持服务等隐性贡献可能决定成功。

决策方法：按项目增删分类并找实际人。

制品及证据：本项目利益相关者分类及人员。

适用边界：22/5是示例计数，没有审批权限或指挥连线。

来源块：C220-web-2025:03-adm-techniques:b00267, C220-web-2025:03-adm-techniques:b00268, C220-web-2025:03-adm-techniques:b00269, C220-web-2025:03-adm-techniques:b00270, C220-web-2025:03-adm-techniques:b00271

<details><summary>展开本节完整英文来源</summary>

3.3.1.1. Sample Stakeholder Analysis

A sample stakeholder analysis that distinguishes 22 types of
stakeholder, in five broad categories, is shown in Figure 3-1 . Any particular architecture project may
have more, fewer, or different stakeholders; and they may be grouped
into more, fewer, or different categories.



Figure 3-1: Sample Stakeholders and Categories

Consider both the Visible team — those obviously associated with the
project/change — and the Invisible team — those who must make a real
contribution to the project/change for it to be successful but who are
not obviously associated with it (e.g., providers of support services).

</details>

<a id="tag_03_03_02"></a>
## 3.3.2. Classify Stakeholder Positions

概念：区分当前与所需理解、承诺、支持及阻碍能力。

适用条件：判断关键个人是否准备支持改变。

逻辑关系：准备程度、倡导能力、参与程度及契约承诺共同支持判断。

决策方法：对关键人物记录当前与目标承诺，持续刷新。

制品及证据：立场分析表及判断依据。

适用边界：H/M/L是示例序数，不能当人员技能等级。

来源块：C220-web-2025:03-adm-techniques:b00272, C220-web-2025:03-adm-techniques:b00273, C220-web-2025:03-adm-techniques:b00274, C220-web-2025:03-adm-techniques:b00275, C220-web-2025:03-adm-techniques:b00276, C220-web-2025:03-adm-techniques:b00277, C220-web-2025:03-adm-techniques:b00278

<details><summary>展开本节完整英文来源</summary>

3.3.2. Classify Stakeholder Positions

Develop a good understanding of the most important stakeholders and
record this analysis for reference and refresh during the project. An
example stakeholder analysis is shown in Table 3-1 .

Table 3-1:  Example Stakeholder Analysis Stakeholder Group Stakeholder Ability to Disrupt Change Current Understanding Required Understanding Current Commitment Required Commitment Required Support CIO John Smith H M H L M H CFO Jeff Brown M M M L M M

It is also important to assess the readiness of each stakeholder to behave in a supportive manner (i.e., demonstrate commitment to the Enterprise Architecture initiative).

This can be done by asking a series of questions:

Is that person ready to change direction and begin moving towards the Target Architecture? If so, how ready? Is that person capable of being a credible advocate or agent of the proposed Enterprise Architecture initiative? If so, how capable? How involved is the individual in the Enterprise Architecture initiative? Are they simply an interested observer, or do they need to be involved in the details? Has that person made a contractual commitment to the development of the Enterprise Architecture, and its role in the governance of the development of the organization?

Then, for each person whose commitment is critical to ensure success, make a judgment as to their current level of commitment and the desired future level of commitment.

</details>

<a id="tag_03_03_03"></a>
## 3.3.3. Determine Stakeholder Management Approach

概念：以权力和兴趣矩阵选择参与策略。

适用条件：面对支持者、批评者和潜在阻碍者。

逻辑关系：高低两轴产生满足、重点参与、告知和最小投入四类。

决策方法：核实影响与兴趣并安排参与频率。

制品及证据：参与策略及证据。

适用边界：策略分类不授予架构或预算批准权。

来源块：C220-web-2025:03-adm-techniques:b00279, C220-web-2025:03-adm-techniques:b00280, C220-web-2025:03-adm-techniques:b00281, C220-web-2025:03-adm-techniques:b00282, C220-web-2025:03-adm-techniques:b00283, C220-web-2025:03-adm-techniques:b00284

<details><summary>展开本节完整英文来源</summary>

3.3.3. Determine Stakeholder Management Approach

The previous steps identified a long list of people and organizations that are affected by the Enterprise Architecture project.

Some of these may have the power either to block or advance. Some may be interested in what the Enterprise Architecture initiative is doing; others may not care. This step enables the team to easily see which stakeholders are expected to be blockers or critics, and which stakeholders are likely to be advocates and supporters of the initiative.

Work out stakeholder power, influence, and interest, so as to focus the Enterprise Architecture engagement on the key individuals. These can be mapped onto a power/interest matrix, which also indicates the strategy to adopt for engaging with them. Figure 3-2 shows an example power grid matrix.



Figure 3-2: Stakeholder Power Grid

</details>

<a id="tag_03_03_04"></a>
## 3.3.4. Tailor Engagement Deliverables

概念：按利益相关者关切选择需制作并验证的目录、矩阵和图。

适用条件：沟通并验证架构是否回应关切。

逻辑关系：制品服务于特定模型和群体理解。

决策方法：共同验证制品而不只提交文件。

制品及证据：制品—关切—审阅者映射及反馈。

适用边界：制品存在不等于有效或已获接受。

来源块：C220-web-2025:03-adm-techniques:b00285, C220-web-2025:03-adm-techniques:b00286, C220-web-2025:03-adm-techniques:b00287

<details><summary>展开本节完整英文来源</summary>

3.3.4. Tailor Engagement Deliverables

Identify catalogs, matrices, and diagrams that the architecture engagement needs to produce and validate with each stakeholder group to deliver an effective architecture model.

It is important to pay particular attention to stakeholder interests by defining specific catalogs, matrices, and diagrams that are relevant for a particular Enterprise Architecture model. This enables the architecture to be communicated to, and understood by, all the stakeholders, and enables them to verify that the Enterprise
Architecture initiative will address their concerns.

</details>

<a id="tag_03_04"></a>
## 3.4. Template Stakeholder Map

概念：示例表把角色群体、关切、参与类别与制品关联。

适用条件：准备本项目stakeholder map。

逻辑关系：采购关切构建块成本约束，HR关注人员过渡，运营关注服务运行。

决策方法：按本组织调整各行类别和制品，保持关切来源。

制品及证据：裁剪后的映射表。

适用边界：表中角色和参与类别不是全企业统一职责或RACI。

来源块：C220-web-2025:03-adm-techniques:b00288, C220-web-2025:03-adm-techniques:b00289, C220-web-2025:03-adm-techniques:b00290

<details><summary>展开本节完整英文来源</summary>

3.4. Template Stakeholder Map

Table 3-2 provides an example stakeholder map for a TOGAF architecture project.

Table 3-2:  Example Stakeholder Map Stakeholder Key Concerns Class Catalogs, Matrices, and Diagrams CxO (Corporate Functions); e.g., CEO, CFO, CIO, COO The high-level drivers, goals, and objectives
of the organization, and how these are translated into an effective
process and IT architecture to advance the business. KEEP SATISFIED Business Footprint diagram Goal/Objective/Business Service diagram Organization Decomposition diagram Business Capabilities catalog Capability/Organization matrix Business Capability Map Strategy/Capability matrix Business Model diagram Value Stream catalog Value Stream Stages catalog Value Stream/Capability matrix Value Stream Map Program Management Office (Corporate Functions); e.g., Project Portfolio Managers Prioritizing, funding, and aligning
change activity. An understanding of project content and technical
dependencies between projects supports portfolio management
decision-making. KEEP SATISFIED Requirements catalog Project Context diagram Benefits diagram Business Footprint diagram Application Communication diagram Organization map Business Capabilities catalog Capability/Organization matrix Business Capability Map Strategy/Capability matrix Business Model diagram Value Stream catalog Value Stream Stages catalog Value Stream/Capability matrix Value Stream Map Procurement (Corporate Functions); e.g., Acquirers Understanding what building blocks of the architecture
can be bought, and what constraints (or rules) are relevant to the
purchase. Acquirers will shop with multiple vendors looking for the best
cost solution while adhering to the constraints (or rules) derived from
the architecture, such as standards. The key concern is to make
purchasing decisions that fit the architecture. KEY PLAYERS Technology Portfolio catalog Technology Standards catalog Human Resources (HR) (Corporate Functions); e.g., HR Managers, Training & Development Managers The roles and actors
are required to support the architecture and changes to it. The key
concern is managing people transitions. KEEP INFORMED Organization Decomposition diagram Organization/Actor catalog Location catalog Application and User Location diagram Business Capabilities catalog Capability/Organization matrix Business Capability Map Strategy/Capability matrix Business Model diagram Enterprise Security (Corporate Functions); e.g., Corporate Risk Management, Security Officers, IT Security Managers Ensuring that the information, data, and systems of the organization
are available to only those that have permission, and protecting the
information, data, and systems from unauthorized tampering. KEY PLAYERS Product Lifecycle diagram Data Dissemination diagram Data Security diagram Actor/Role matrix Networked Computing Hardware diagram Network and Communications diagram QA/Standards Group (Corporate Functions); e.g., Data Owners, Process Owners, Technical Standards Bodies Ensuring
the consistent governance of the organization’s business, data,
application, and technology assets. KEY PLAYERS Process/Event/ Control/Product catalog Contract/Measure catalog Application Portfolio catalog Interface catalog Technology Standards catalog Technology Portfolio catalog Value Stream catalog Value Stream Stages catalog Value Stream/Capability matrix Value Stream Map Executive (End-user Organization); e.g., Business Unit Directors, Business Unit CxOs, Business Unit Head of
IT/Architecture The high-level drivers, goals, and objectives of the
organization, and how these are translated into an effective process and
architecture to advance the business. KEEP SATISFIED Business Footprint diagram Goal/Objective/Business Service diagram Organization Decomposition diagram Process Flow diagram Application Communication diagram Business Capabilities catalog Capability/Organization matrix Business Capability Map Strategy/Capability matrix Business Model diagram Value Stream catalog Value Stream Stages catalog Value Stream/Capability matrix Value Stream Map Line Management (End-user Organization); e.g., Senior Business Managers, Operations Regional Managers, IT
Managers Top-level functions and processes of the organization, and how
the key applications support these processes. KEY PLAYERS Business Footprint diagram Organization Decomposition diagram Organization map Process Flow diagram Application Communication diagram Application and User Location diagram Business Capabilities catalog Capability/Organization matrix Business Capability Map Strategy/Capability matrix Business Model diagram Value Stream catalog Value Stream Stages catalog Value Stream/Capability matrix Value Stream Map Business Domain Experts (End-user Organization); e.g., Business Process Experts, Business/Process Analyst, Process
Architect, Process Designer, Functional Managers, Business Analyst Functional aspects of processes and supporting systems. This can cover
the human actors involved in the system, the user processes involved in
the system, the functions required to support the processes, and the
information required to flow in support of the processes. KEY PLAYERS Business Interaction matrix Actor/Role matrix Business Service/ Information diagram Organization map Product Lifecycle diagram Business Use-Case diagram Application Use-Case diagram Application Communication diagram Data Entity/Business Function matrix Value Stream catalog Value Stream Stages catalog Value Stream/Capability matrix Value Stream Map IT Service Management (Systems Operations); e.g., Service Delivery Manager Ensuring that IT services provided to
the organization meet the service levels required by that organization
to succeed in business. KEEP INFORMED Technology Standards catalog Technology Portfolio catalog Contract/Measure catalog Process/Application Realization diagram Enterprise Manageability diagram IT Operations — Applications (System Operations); e.g., Application Architecture, System & Software Engineers Development
approach, software modularity and re-use, portability migration, and
interoperability. KEY PLAYERS Process/Application Realization diagram Application/Data matrix Application Migration diagram Software Engineering diagram Platform Decomposition diagram Networked Computing/ Hardware diagram Software Distribution diagram IT Operations — Infrastructure (System Operations); e.g., Infrastructure Architect, Wintel support, Mid-range support,
Operational DBA, Service Desk Location, modifiability, re-usability,
and availability of all components of the system. Ensuring that the
appropriate components are developed and deployed within the system in
an optimal manner. KEY PLAYERS Platform Decomposition diagram Technology Standards catalog Technology Portfolio catalog Enterprise Manageability diagram Networked Computing/ Hardware diagram Processing diagram Environments and Locations diagram IT Operations — Data/Voice Communications (System Operations); e.g., Network Management Location, modifiability, re-usability, and
availability of communications and networking services. Ensuring that
the appropriate communications and networking services are developed and
deployed within the system in an optimal manner. KEY PLAYERS Network and Communications diagram Executive (Project Organization); e.g., Sponsor, Program Manager On-time, on-budget delivery of a change
initiative that will realize expected benefits for the organization. KEEP INFORMED Requirements catalog Principles catalog Value Chain diagram Solution Concept diagram Organization map Application and User Location diagram Business Capabilities catalog Capability/Organization matrix Business Capability Map Strategy/Capability matrix Business Model diagram Value Stream catalog Value Stream Stages catalog Value Stream/Capability matrix Value Stream Map Line Management (Project Organization); e.g., Project Manager Operationally achieving on-time, on-budget
delivery of a change initiative with an agreed scope. KEEP INFORMED Application Communication diagram Organization map Environments and Locations diagram Business Capabilities catalog Capability/Organization matrix Business Capability Map Strategy/Capability matrix Business Model diagram Value Stream catalog Value Stream Stages catalog Value Stream/Capability matrix Value Stream Map Business Process/Functional Expert (Project Organization); e.g., Financials FICO ® Functional Consultant, HR Functional Consultant Adding more detail to the functional requirements of a change
initiative based on experience and interaction with business domain
experts in the end-user organization. KEY PLAYERS Process Flow diagram Business Use-Case diagram Business Service/Information diagram Organization map Application Communication diagram Business Capabilities catalog Capability/Organization matrix Business Capability Map Strategy/Capability matrix Business Model diagram Value Stream catalog Value Stream Stages catalog Value Stream/Capability matrix Value Stream Map Product Specialist (Project Organization); e.g., Portal Product Specialist Specifying technology product designs in order to meet project
requirements and comply with the Architecture Vision of the solution. In a packages and packaged services environment, product expertise can
be used to identify product capabilities that can be readily leveraged
and can provide guidance on strategies for product customization. KEY PLAYERS Software Engineering diagram Application/Data matrix Technical Specialist (Project Organization); e.g., Application Architect Specifying technology product designs in
order to meet project requirements and comply with the Architecture
Vision of the solution. KEY PLAYERS Software Engineering diagram Platform Decomposition diagram Process/Application Realization diagram Application/Data matrix Application Migration diagram Regulatory Bodies (Outside Services); e.g., Financial Regulator, Industry Regulator Receipt of the
information they need in order to regulate the client organization, and
ensuring that their information requirements are properly satisfied.
Interested in reporting processes, and the data and applications used to
provide regulatory return information. KEEP SATISFIED Business Footprint diagram Application Communication diagram Suppliers (Outside Services); e.g., Alliance Partners, Key Suppliers Ensuring that their information
exchange requirements are met in order that agreed service contracts
with the client organizations can be fulfilled. KEEP SATISFIED Business Footprint diagram Business Service/Information diagram Application Communication diagram Business Capabilities catalog Capability/Organization matrix Business Capability Map Strategy/Capability matrix Business Model diagram Value Stream catalog Value Stream Stages catalog Value Stream/Capability matrix Value Stream Map

</details>

<a id="chap04"></a>
## 4. Architecture Patterns

概念：模式是将构建块放入可复用问题情境的技术。

适用条件：不同学科、域和细节层级的架构。

逻辑关系：模式说明如何、何时、为何组合构建块。

决策方法：核对背景、约束和已有使用证据。

制品及证据：模式目录及采用理由。

适用边界：本章没有唯一模式标准格式。

来源块：C220-web-2025:03-adm-techniques:b00291, C220-web-2025:03-adm-techniques:b00292

<details><summary>展开本节完整英文来源</summary>

4. Architecture Patterns

This chapter provides guidelines for using architecture patterns.

</details>

<a id="tag_04_01"></a>
## 4.1. Introduction

概念：模式实践跨业务与软件层级，但没有单一EA模式描述标准。

适用条件：采用模式描述架构。

逻辑关系：需保持不同领域和粒度的语义。

决策方法：选择适合受众的描述约定。

制品及证据：模式描述约定。

适用边界：不能以成熟实践推断所有模式已有标准化。

来源块：C220-web-2025:03-adm-techniques:b00293, C220-web-2025:03-adm-techniques:b00294, C220-web-2025:03-adm-techniques:b00295

<details><summary>展开本节完整英文来源</summary>

4.1. Introduction

Patterns for describing Enterprise Architectures are becoming
increasingly important to practitioners. The diverse and
multi-disciplinary nature of Enterprise Architecture requires that
patterns be developed in different disciplines, domains, and levels of
detail.

Previous versions of this standard did not fully embrace architecture
patterns due to their perceived lack of maturity. Today, many
organizations are using patterns to describe their architectures at
various levels ranging from software design patterns to business
patterns. It remains true that there is no single standard for
describing Enterprise Architecture patterns. However, it can be said
that there is a pattern for describing patterns.

</details>

<a id="tag_04_01_01"></a>
## 4.1.1. Background

概念：构建块是所用元素，模式提供组合情境和权衡。

适用条件：过去有效的组合可能解决新的重复问题。

逻辑关系：历史已验证不等于新情境保证有效。

决策方法：比较新问题与known uses的约束。

制品及证据：模式采用背景和使用证据。

适用边界：源文ABB括号存在排版残缺，保留语义与原样证据。

来源块：C220-web-2025:03-adm-techniques:b00296, C220-web-2025:03-adm-techniques:b00297, C220-web-2025:03-adm-techniques:b00298, C220-web-2025:03-adm-techniques:b00299, C220-web-2025:03-adm-techniques:b00300

<details><summary>展开本节完整英文来源</summary>

4.1.1. Background

A “pattern” has been defined as: “an idea that has been useful in one practical context and will probably be useful in others” (Source: Analysis Patterns — Re-usable Object Models, by M. Fowler).

In the TOGAF Standard, patterns are considered to be a way of putting building blocks into context; for example, to describe a re-usable solution to a problem. Building blocks are what you use: patterns can tell you how you use them, when, why, and what trade-offs you have to make in doing so. Patterns offer the promise of helping the architect to
identify combinations of Architecture(ABB and/or Solution Building Blocks (ABBs/SBBs) that have been proven to deliver effective solutions in the past, and may provide the basis for effective solutions in the future.

Pattern techniques are generally acknowledged to have been established as a valuable architectural design technique by Christopher Alexander, a buildings architect, who described this approach in his book The Timeless Way of Building , published in 1979. This book provides an introduction to the ideas behind the use of patterns, and Alexander followed it with two further books ( A Pattern Language and The Oregon
Experiment ) in which he expanded on his description of the features and benefits of a patterns approach to architecture.

Software and buildings architects have many similar issues to address, and so it was natural for software architects to take an interest in patterns as an architectural tool. Many papers and books have been published on them since Alexander’s 1979 book, perhaps the most renowned being Design Patterns: Elements of Re-usable Object-Oriented Software (Gamma et al. , 1994). This book describes simple and elegant solutions to specific problems in object-oriented software design.

</details>

<a id="tag_04_01_02"></a>
## 4.1.2. Content of a Pattern

概念：模式包含名称、问题、背景、力量、方案、结果背景、例子、理由、相关模式及已知应用。

适用条件：需要可迁移而不是仅示意图的模式描述。

逻辑关系：前置背景到结果背景解释解决及未解决力量，相关模式可前置、后续、替代或共同依赖。

决策方法：同时说明静态结构、动态协作及未解决约束。

制品及证据：完整模式记录与known uses。

适用边界：标题可不同；本列表不是全球唯一格式。

来源块：C220-web-2025:03-adm-techniques:b00301, C220-web-2025:03-adm-techniques:b00302, C220-web-2025:03-adm-techniques:b00303, C220-web-2025:03-adm-techniques:b00304

<details><summary>展开本节完整英文来源</summary>

4.1.2. Content of a Pattern

Several different formats are used in the literature for describing patterns, and no single format has achieved widespread acceptance. However, there is broad agreement on the types of things that a pattern should contain. The headings which follow are taken from Pattern-Oriented Software Architecture: A System of Patterns (Buschmann et al. , 1996). The elements described below will be found in
most patterns, even if different headings are used to describe them.

Name A meaningful and memorable way to refer to the pattern, typically a single word or short phrase. Problem A description of the problem indicating the intent in applying the pattern — the intended goals and objectives to be reached within the context and forces described below (perhaps with some indication of their priorities). Context The preconditions under which the pattern is applicable — a description of the initial state before the pattern is applied. Forces A description of the relevant forces and constraints, and how they interact/conflict with each other and with the intended goals and objectives. The description should clarify the intricacies of the problem and make explicit the kinds of trade-offs that must be considered. (The need for such trade-offs is typically what makes the problem difficult, and generates the need for the pattern in the first place.) The notion of “forces” equates in many ways to the “qualities” that architects seek to optimize, and the concerns they seek to address, in designing architectures. For example: Security, robustness, reliability, fault-tolerance Manageability Efficiency, performance, throughput, bandwidth requirements, space
utilization Scalability (incremental growth on-demand) Extensibility, evolvability, maintainability Modularity, independence, re-usability, openness, composability
(plug-and-play), portability Completeness and correctness Ease-of-construction Ease-of-use etc., …​ Solution A description, using text and/or graphics, of how to achieve the intended goals and objectives. The description should identify both the solution’s static structure and its dynamic behavior — the people and computing actors, and their collaborations. The description may include guidelines for implementing the solution. Variants or specializations of
the solution may also be described. Resulting Context The post-conditions after the pattern has been applied. Implementing the solution normally requires trade-offs among competing forces. This element describes which forces have been resolved and how, and which remain unresolved. It may also indicate other patterns that may be applicable in the new context. (A pattern may be one step in accomplishing some larger goal.) Any such other patterns will be described in detail under Related Patterns. Examples One or more sample applications of the pattern which illustrate each of the other elements: a specific problem, context, and set of forces; how the pattern is applied; and the resulting context. Rationale An explanation/justification of the pattern as a whole, or of individual components within it, indicating how the pattern actually works, and why — how it resolves the forces to achieve the desired goals and objectives, and why this is “good”. The Solution element of a pattern describes the external structure and behavior of the solution: the
Rationale provides insight into its internal workings. Related Patterns The relationships between this pattern and others. These may be predecessor patterns, whose resulting contexts correspond to the initial context of this one; or successor patterns, whose initial contexts correspond to the resulting context of this one; or alternative patterns, which describe a different solution to the same problem, but under different forces; or co-dependent patterns, which may/must be applied along with this pattern. Known Uses Known applications of the pattern within existing systems, verifying that the pattern does indeed describe a proven solution to a recurring problem. Known Uses can also serve as Examples.

Patterns may also begin with an Abstract providing an overview of the pattern and indicating the types of problems it addresses. The Abstract may also identify the target audience and what assumptions are made of the reader.

</details>

<a id="tag_04_01_03"></a>
## 4.1.3. Terminology

概念：架构模式一词在技术文献中常只指软件。

适用条件：跨企业系统解释外部模式。

逻辑关系：术语不清会把软件结构规则扩大为企业治理规则。

决策方法：先说明模式所在领域和抽象层。

制品及证据：术语及领域范围说明。

适用边界：软件架构是TOGAF关注的一部分。

来源块：C220-web-2025:03-adm-techniques:b00305, C220-web-2025:03-adm-techniques:b00306, C220-web-2025:03-adm-techniques:b00307

<details><summary>展开本节完整英文来源</summary>

4.1.3. Terminology

Although design patterns have been the focus of widespread interest in the software industry for several years, particularly in the object-oriented and component-based software fields, it is only recently that there has been increasing interest in architecture patterns — extending the principles and concepts of design patterns to the
architecture domain.

The technical literature relating to this field is complicated by the fact that many people in the software field use the term “architecture” to refer to software, and many patterns described as “architecture patterns” are high-level software design patterns. This simply makes it
all the more important to be precise in the use of terminology.

</details>

<a id="tag_04_01_03_01"></a>
## 4.1.3.1. Architecture Patterns and Design Patterns

概念：软件架构模式规定系统组织，设计模式细化组件，idiom依赖语言。

适用条件：借鉴软件模式用于企业信息系统时。

逻辑关系：企业系统还包含硬件、网络及人员。

决策方法：区分三个粒度并补足非软件因素。

制品及证据：模式分类、职责和关系规则。

适用边界：三个定义引用软件文献，不构成整个EA的完整分类。

来源块：C220-web-2025:03-adm-techniques:b00308, C220-web-2025:03-adm-techniques:b00309, C220-web-2025:03-adm-techniques:b00310, C220-web-2025:03-adm-techniques:b00311, C220-web-2025:03-adm-techniques:b00312

<details><summary>展开本节完整英文来源</summary>

4.1.3.1. Architecture Patterns and Design Patterns

The term “design pattern” is often used to refer to any pattern which addresses issues of software architecture, design, or programming implementation. In Pattern-Oriented Software Architecture: A System of Patterns , the authors define these three types of patterns as follows:

An Architecture Pattern expresses a fundamental structural organization or schema for software systems It provides a set of predefined subsystems, specifies their
responsibilities, and includes rules and guidelines for organizing the relationships between them. A Design Pattern provides a scheme for refining the subsystems or components of a software system, or the relationships between them It describes a commonly recurring structure of communicating components that solves a general design problem within a particular context. An Idiom is a low-level pattern specific to a programming language An idiom describes how to implement particular aspects of components or the relationships between them using the features of the given language.

These distinctions are useful, but it is important to note that architecture patterns in this context still refers solely to software architecture. Software architecture is certainly an important part of the focus of the TOGAF Standard, but it is not its only focus.

In this section we are concerned with patterns for enterprise system architecting. These are analogous to software architecture and design patterns, and borrow many of their concepts and terminology, but focus on providing re-usable models and methods specifically for the architecting of enterprise information systems — comprising software,
hardware, networks, and people — as opposed to purely software systems.

</details>

<a id="tag_04_01_03_02"></a>
## 4.1.3.2. Patterns and the Architecture Continuum

概念：模式是可复用架构资产，可在A—D考虑并纳入架构连续体。

适用条件：企业正式管理模式复用。

逻辑关系：本节仍称模式尚未集成进标准，而本卷已给指导。

决策方法：把此陈述记录为编排/版本张力，区分指导与正式内容模型集成。

制品及证据：模式分类、复用入口与版本说明。

适用边界：不可默改原文旧时态或宣称已完全整合。

来源块：C220-web-2025:03-adm-techniques:b00313, C220-web-2025:03-adm-techniques:b00314, C220-web-2025:03-adm-techniques:b00315

<details><summary>展开本节完整英文来源</summary>

4.1.3.2. Patterns and the Architecture Continuum

Although architecture patterns have not (as yet) been integrated into the TOGAF Standard, each of the first four main phases of the ADM (Phases A through D) gives an indication of the stage at which relevant
re-usable architecture assets from the Enterprise Architecture Continuum should be considered for use. Architecture patterns are one such asset.

An enterprise that adopts a formal approach to the use and re-use of architecture patterns will normally integrate their use into the Enterprise Architecture Continuum.

</details>

<a id="tag_04_01_03_03"></a>
## 4.1.3.3. Patterns and Views

概念：视图聚焦特定关切，模式帮助模型设计及视图组合。

适用条件：使用一个或多个系统模型时。

逻辑关系：模式与视图角色不同。

决策方法：检查模式是否支持视点要回答的问题。

制品及证据：模式—模型—视图关联。

适用边界：模式不是视点本身。

来源块：C220-web-2025:03-adm-techniques:b00316, C220-web-2025:03-adm-techniques:b00317

<details><summary>展开本节完整英文来源</summary>

4.1.3.3. Patterns and Views

Architecture views are selected parts of one or more models representing a complete system architecture, focusing on those aspects that address
the concerns of one or more stakeholders. Patterns can provide help in designing such models, and in composing views based on them.

</details>

<a id="tag_04_01_03_04"></a>
## 4.1.3.4. Patterns and Business Scenarios

概念：业务场景分析可帮助发现相关模式。

适用条件：以真实问题推导方案时。

逻辑关系：场景确定上下文，模式提供复用候选。

决策方法：从场景约束筛选而非先套模式。

制品及证据：场景及候选模式依据。

适用边界：发现候选不代表批准使用。

来源块：C220-web-2025:03-adm-techniques:b00318, C220-web-2025:03-adm-techniques:b00319

<details><summary>展开本节完整英文来源</summary>

4.1.3.4. Patterns and Business Scenarios

Relevant architecture patterns may well be identified in the work on business scenarios.

</details>

<a id="chap05"></a>
## 5. Gap Analysis

概念：差距分析验证基线到目标中有意遗漏、意外遗漏和未定义元素。

适用条件：开发或验证目标架构。

逻辑关系：缺项需解释，不能自动认为删除正确。

决策方法：用矩阵区分保留、删除和新增。

制品及证据：差距矩阵与处理决定。

适用边界：差距不只等于新增IT组件。

来源块：C220-web-2025:03-adm-techniques:b00320, C220-web-2025:03-adm-techniques:b00321

<details><summary>展开本节完整英文来源</summary>

5. Gap Analysis

The technique known as gap analysis is widely used in the TOGAF
Architecture Development Method (ADM) to validate an architecture that
is being developed. The basic premise is to highlight a shortfall
between the Baseline Architecture and the Target Architecture; that is,
items that have been deliberately omitted, accidentally left out, or not
yet defined.

</details>

<a id="tag_05_01"></a>
## 5.1. Introduction

概念：未回应的利益相关者关切是关键差距来源。

适用条件：检查业务、数据、应用和技术完整性。

逻辑关系：人员、流程、工具、指标、资金、设施及数据时效/位置/使用均可能有差距。

决策方法：逐关切核对必需信息处理需要。

制品及证据：关切覆盖和差距来源。

适用边界：组件覆盖不能证明业务关切均满足。

来源块：C220-web-2025:03-adm-techniques:b00322, C220-web-2025:03-adm-techniques:b00323, C220-web-2025:03-adm-techniques:b00324, C220-web-2025:03-adm-techniques:b00325

<details><summary>展开本节完整英文来源</summary>

5.1. Introduction

A key step in validating an architecture is to consider what may have
been forgotten. The architecture must support all of the essential
information processing needs of the organization. The most critical
source of gaps that should be considered is stakeholder concerns that
have not been addressed in prior architectural work.

Potential sources of gaps include:

Business domain gaps: People gaps (e.g., cross-training requirements) Process gaps (e.g., process inefficiencies) Tools gaps (e.g., duplicate or missing tool functionality) Information gaps Measurement gaps Financial gaps Facilities gaps (buildings, office space, etc.) Data domain gaps: Data not of sufficient currency Data not located where it is needed Not the data that is needed Data not available when needed Data not created Data not consumed Data relationship gaps Applications impacted, eliminated, or created Technologies impacted, eliminated, or created

</details>

<a id="tag_05_02"></a>
## 5.2. Suggested Steps

概念：基线ABB为纵轴，目标ABB为横轴，添加New行与Eliminated列。

适用条件：同粒度比较两个架构状态。

逻辑关系：Included保留；消失元素需判断有意删除或意外遗漏；新增需开发采购。

决策方法：逐项审查新增及删除，误删在下一迭代恢复。

制品及证据：逐格差距分类、解释与处置动作。

适用边界：空白不是默认通过；潜在匹配需要另行验证。

来源块：C220-web-2025:03-adm-techniques:b00326, C220-web-2025:03-adm-techniques:b00327, C220-web-2025:03-adm-techniques:b00328, C220-web-2025:03-adm-techniques:b00329

<details><summary>展开本节完整英文来源</summary>

5.2. Suggested Steps

The suggested steps are as follows:

Draw up a matrix with all the ABBs of the Baseline Architecture on the
vertical axis, and all the ABBs of the Target Architecture on the
horizontal axis Add to the Baseline Architecture axis a final row labeled “New”, and
to the Target Architecture axis a final column labeled “Eliminated” Where an ABB is available in both the Baseline and Target
Architectures, record this with “Included” at the intersecting cell Where an ABB from the Baseline Architecture is missing in the Target Architecture, each must be reviewed If it was correctly eliminated, mark it as such in the appropriate “Eliminated” cell. If it was not, an accidental omission in the Target Architecture has been uncovered that must be addressed by reinstating the ABB in the next iteration of the architecture design — mark it as such in the appropriate “Eliminated” cell. Where an ABB from the Target Architecture cannot be found in the Baseline Architecture, mark it at the intersection with the “New” row as a gap that needs to filled, either by developing or procuring the building block

When the exercise is complete, anything under “Eliminated” or “New” is a gap, which should either be explained as correctly eliminated, or marked as to be addressed by reinstating or developing/procuring the building block.

</details>

<a id="tag_05_03"></a>
## 5.3. Example

概念：网络服务示例显示有意删除、意外缺失、新增和潜在匹配。

适用条件：学习矩阵表示法。

逻辑关系：增强电话服务同时有潜在匹配与新增补足。

决策方法：解释每个标记而非仅计数量。

制品及证据：示例审查记录及本项目独立矩阵。

适用边界：TRM例子不证明本项目需要这些服务。

来源块：C220-web-2025:03-adm-techniques:b00330, C220-web-2025:03-adm-techniques:b00331, C220-web-2025:03-adm-techniques:b00332, C220-web-2025:03-adm-techniques:b00333

<details><summary>展开本节完整英文来源</summary>

5.3. Example

Figure 5-1 shows an example analysis for ABBs that are
services from the Network Services category of the TOGAF Technical
Reference Model (TRM), and shows a number of services from the Baseline
Architecture missing from the Target Architecture.



Figure 5-1: Gap Analysis Example

</details>

<a id="chap06"></a>
## 6. Interoperability Requirements

概念：互操作要求定义信息和服务共享能力。

适用条件：复杂或扩展企业的跨系统协作。

逻辑关系：共享程度从业务语义细化到技术和方案约束。

决策方法：先定义企业统一的交换语言与程度。

制品及证据：互操作需求模型。

适用边界：连通性不能代替业务互操作。

来源块：C220-web-2025:03-adm-techniques:b00334, C220-web-2025:03-adm-techniques:b00335

<details><summary>展开本节完整英文来源</summary>

6. Interoperability Requirements

This chapter provides guidelines for defining and establishing
interoperability requirements.

</details>

<a id="tag_07_01"></a>
## 6.1. Overview

概念：互操作贯穿A场景、B业务、C数据与应用、D机制、E选型、F规划。

适用条件：逐步细化信息及服务交换。

逻辑关系：各阶段处理不同语义和约束。

决策方法：在每阶段保持需求追溯并检查安全。

制品及证据：交换模型、应用机制、方案与迁移需求。

适用边界：F的logically implemented指规划逻辑，不等于已部署运行。

来源块：C220-web-2025:03-adm-techniques:b00336, C220-web-2025:03-adm-techniques:b00337, C220-web-2025:03-adm-techniques:b00338, C220-web-2025:03-adm-techniques:b00339

<details><summary>展开本节完整英文来源</summary>

6.1. Overview

A definition of interoperability is “the ability to share information
and services”. Defining the degree to which the information and services
are to be shared is a very useful architectural requirement, especially
in a complex organization and/or extended enterprise.

The determination of interoperability is present throughout the ADM as
follows:

In the Architecture Vision (Phase A), the nature and security
considerations of the information and service exchanges are first
revealed within the business scenarios In the Business Architecture (Phase B), the information and service
exchanges are further defined in business terms In the Data Architecture (Phase C), the content of the information
exchanges is detailed using the corporate data and/or information
exchange model In the Application Architecture (Phase C), the way that the various
applications are to share the information and services is specified In the Technology Architecture (Phase D), the appropriate technical
mechanisms to permit the information and service exchanges are specified In Opportunities & Solutions (Phase E), the actual solutions (e.g.,
COTS packages) are selected In Migration Planning (Phase F), the interoperability is logically
implemented

</details>

<a id="tag_07_02"></a>
## 6.2. Defining Interoperability

概念：业务、信息及技术互操作可再分呈现、信息、应用和基础设施集成。

适用条件：企业及扩展企业共同定义共享能力。

逻辑关系：共用外观、数据语义、功能和技术平台是不同层次。

决策方法：选择一致定义并核对运行模型。

制品及证据：企业互操作分类。

适用边界：加拿大电子政务分类是例子，不是通用强制模型。

来源块：C220-web-2025:03-adm-techniques:b00340, C220-web-2025:03-adm-techniques:b00341, C220-web-2025:03-adm-techniques:b00342, C220-web-2025:03-adm-techniques:b00343, C220-web-2025:03-adm-techniques:b00344, C220-web-2025:03-adm-techniques:b00345, C220-web-2025:03-adm-techniques:b00346, C220-web-2025:03-adm-techniques:b00347, C220-web-2025:03-adm-techniques:b00348

<details><summary>展开本节完整英文来源</summary>

6.2. Defining Interoperability

There are many ways to define interoperability and the aim is to define
one that is consistently applied within the enterprise and extended
enterprise. It is best that both the enterprise and the extended
enterprise use the same definitions.

Many organizations find it useful to categorize interoperability as
follows:

Operational or Business Interoperability defines how business
processes are to be shared Information Interoperability defines how information is to be shared Technical Interoperability defines how technical services are to be
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
closely linked to corporate business process
unification/interoperability. Technical Integration/Interoperability includes common methods and
shared services for the communication, storage, processing, and access
to data primarily in the application platform and communications
infrastructure domains This interoperability is premised upon the degree of rationalization of
the corporate IT infrastructure, based upon standards and/or common IT
platforms. For example, multiple applications sharing one infrastructure
or 10,000 corporate websites using one centralized content
management/web server (rather than thousands of servers and webmasters
spread throughout the country/globe).

Many organizations create their own interoperability models, such as
illustrated in the example below from the Canadian Government. They have
a high-level definition of the three classes of interoperability and
identify the nature of the information and services that they wish to
share. Interoperability is coined in terms of e-enablers for
e-Government. Their interoperability breakdown is as follows:

Information Interoperability: Knowledge management Business intelligence Information management Trusted identity Business Interoperability: Delivery networks e-Democracy e-Business Enterprise resource management Relationship and case management Technical Interoperability: IT infrastructure

In certain architectural approaches, such as system of systems or a
federated model, interoperability is a strongly recommended best
practice that will determine how the systems interact with each other. A
key consideration will be the enterprise’s business operating model.

</details>

<a id="tag_07_03"></a>
## 6.3. Enterprise Operating Model

概念：运行模型定义业务流程整合与标准化所需程度。

适用条件：决定文档共享、交易数据或共享服务等要求。

逻辑关系：运行模型应在A或B明确，最迟E；内外企业可有不同模型。

决策方法：比较各范围实际整合要求。

制品及证据：运行模型与互操作范围映射。

适用边界：运行模型不能从所用中间件推断。

来源块：C220-web-2025:03-adm-techniques:b00349, C220-web-2025:03-adm-techniques:b00350, C220-web-2025:03-adm-techniques:b00351, C220-web-2025:03-adm-techniques:b00352, C220-web-2025:03-adm-techniques:b00353

<details><summary>展开本节完整英文来源</summary>

6.3. Enterprise Operating Model

Key to establishing interoperability is the determination of the
corporate operating model, where the operating model is “the necessary level of business process integration and standardization for delivering
goods and services to customers. An operating model describes how a company wants to thrive and grow. By providing a more stable and actionable view of the company than strategy, the operating model drives
the design of the foundation for execution”. [ 1 ]

For example, if lines of business or business units only need to share
documents, then the ABBs and SBBs may be simpler than if there is a need
to share structured transaction data. Similarly, if the Architecture
Vision includes a shared services environment, then it is useful to
define the level the services are to be shared.

The corporate operating model will normally indicate what type of
interoperability approach will be appropriate. This model should be
determined in Phase A (Architecture Vision) if not in Phase B (Business
Architecture), and definitely by Phase E (Opportunities & Solutions).

Complex enterprises and/or extended enterprises (e.g., supply chain) may
have more than one type of operating model. For example, it is common
for the internal operating model (and supporting interoperability model)
to differ from the one used for the extended enterprise.

</details>

<a id="tag_07_04"></a>
## 6.4. Refining Interoperability

概念：互操作标准需具体、可测、可行动、现实且有时间界限。

适用条件：把高层共享要求变成可实施需求。

逻辑关系：四级交换示例从非结构化数据到共同解释信息；等级需技术细化。

决策方法：制定本企业程度、类型、目标和指标，更新目标/过渡及差距依赖。

制品及证据：标准、变革策略、度量及更新记录。

适用边界：3A—3D及四级是案例定义，其他图中代码未全定义。

来源块：C220-web-2025:03-adm-techniques:b00354, C220-web-2025:03-adm-techniques:b00355, C220-web-2025:03-adm-techniques:b00356, C220-web-2025:03-adm-techniques:b00357, C220-web-2025:03-adm-techniques:b00358, C220-web-2025:03-adm-techniques:b00359, C220-web-2025:03-adm-techniques:b00360, C220-web-2025:03-adm-techniques:b00361, C220-web-2025:03-adm-techniques:b00362, C220-web-2025:03-adm-techniques:b00363, C220-web-2025:03-adm-techniques:b00364, C220-web-2025:03-adm-techniques:b00365

<details><summary>展开本节完整英文来源</summary>

6.4. Refining Interoperability

Implementing interoperability requires the creation, management,
acceptance, and enforcement of realistic standards that are SMART
(Specific, Measurable, Actionable, Realistic, and Time-bound). Clear
measures of interoperability are key to success.

Architecture is the key for identifying standards and facilitated
sessions will examine potential pragmatic ways (that fit within the
current or emerging business culture) to achieve the requisite degree of
interoperability.

Interoperability should be refined so that it meets the needs of the
enterprise and/or extended enterprise in an unambiguous way. The refined
interoperability measures (degrees, types, and high-level targets)
should be part of or referred to the Enterprise Architecture strategic
direction.

These measures are instantiated within a transformation strategy that
should be embedded within the Target Architecture definition and
pragmatically implemented in the Transition Architectures. Upon
completion, also update the consolidated gap analysis results and
dependencies to ensure that all output from facilitated sessions is
captured.

An example of specifying interoperability is the Degrees of
Interoperability (used within the Canadian Department of National
Defense and NATO). These organizations were focused on the sharing of
information and came up with four degrees of interoperability as
follows:

Degree 1: Unstructured Data Exchange involves the exchange of
human-interpretable unstructured data, such as the free text found in
operational estimates, analysis, and papers Degree 2: Structured Data Exchange involves the exchange of
human-interpretable structured data intended for manual and/or automated
handling, but requires manual compilation, receipt, and/or message
dispatch Degree 3: Seamless Sharing of Data involves the automated sharing of
data amongst systems based on a common exchange model Degree 4: Seamless Sharing of Information is an extension of Degree
3 to the universal interpretation of information through data processing
based on co-operating applications

These degrees should be further refined and made technically meaningful
for each of the degrees. An example refinement of Degree 3 with four
subclassifications follows:

3A: Formal Message Exchange 3B: Common Data Exchange 3C: Complete Data Exchange 3D: Real-time Data Exchange

The intent is to specify the detailed degrees of interoperability to the
requisite level of detail so that they are technically meaningful.

These degrees are very useful for specifying the way that information
has to be exchanged between the various systems and provide critical
direction to the projects implementing the systems.

Similar measures should be established to determine service/business and
technical interoperability.

</details>

<a id="tag_07_05"></a>
## 6.5. Determining Interoperability Requirements

概念：基于差距与场景确定新旧系统共存及方向性交换要求。

适用条件：变革期间运营负责人和架构师参与。

逻辑关系：B利益相关者矩阵在C演进成系统矩阵，共享不必对称双向。

决策方法：逐方向定义信息、程度、依赖和边界，评估包装器及市场产品。

制品及证据：方向性互操作矩阵、目标数据应用更新。

适用边界：包装器可能长期保留，不能默认只是临时措施。

来源块：C220-web-2025:03-adm-techniques:b00366, C220-web-2025:03-adm-techniques:b00367, C220-web-2025:03-adm-techniques:b00368, C220-web-2025:03-adm-techniques:b00369, C220-web-2025:03-adm-techniques:b00370, C220-web-2025:03-adm-techniques:b00371, C220-web-2025:03-adm-techniques:b00372, C220-web-2025:03-adm-techniques:b00373, C220-web-2025:03-adm-techniques:b00374, C220-web-2025:03-adm-techniques:b00375, C220-web-2025:03-adm-techniques:b00376, C220-web-2025:03-adm-techniques:b00377, C220-web-2025:03-adm-techniques:b00378, C220-web-2025:03-adm-techniques:b00379, C220-web-2025:03-adm-techniques:b00380, C220-web-2025:03-adm-techniques:b00381

<details><summary>展开本节完整英文来源</summary>

6.5. Determining Interoperability Requirements

Co-existence between emerging and existing systems, especially during
transformation, will be a major challenge and facilitated sessions
should attempt to figure out what has to be done to reduce the pain. It
is imperative to involve the operations management staff and architects
in this step as they will be responsible for operating the portfolio
deliverables.

For example, there might be a need for a “wrapper” application (an
application that acts as the interface [a.k.a. interpreter] between the
legacy application and the emerging infrastructure). Indeed,
pragmatically, in the “if it works do not fix it” world, the “wrapper”
might become a permanent solution.

Regardless, using the gap analysis results and business scenarios as a
foundation, discuss the IT issues and work them through to ensure that
all of the gaps are clearly identified and addressed and verify that the
organization-specific requirements will be met.

It is important to note that the ensuing development process must include recognition of dependencies and boundaries for functions and should take account of what products are available in the marketplace. An example of how this might be expressed can be seen in the building blocks example; see the TOGAF Standard — Architecture Content .

If a mechanism such as the Degrees of Interoperability is used, then a
matrix showing the interoperability requirements is a useful tool, as
illustrated in Figure 6-1 and Figure 6-2 , noting that the degree of information sharing is not necessarily
symmetrical or bidirectional between systems and/or stakeholders.

The matrix below can be used within the enterprise and/or within the
extended enterprise as a way of detailing that information and/or
services can be shared. The matrix should start in the Business
Architecture (Phase B) to capture the nature of the sharing of
information between stakeholders, and evolve to determine what systems
share what information in Phase C.



Figure 6-1: Business Information Interoperability Matrix

Figure 6-1 shows that Stakeholder A requires structured
data exchange (Degree 2) with Stakeholders/Systems B and D, and seamless
sharing of data (Degree 3) with Stakeholders/Systems C, E, F, and G.

The business information interoperability matrix should be refined
within the Information Systems Architecture using refined measures and
specifying the actual systems used by the stakeholders. A sample is
shown in Figure 6-2 .



Figure 6-2: Information Systems Interoperability Matrix

In Figure 6-2 , both the nature of the exchange is
more detailed (e.g., Degree 3A versus only Degree 3) and the sharing
is between specific systems rather than stakeholders. For example,
System A shares information with the other systems in accordance with
enterprise technical standards.

In many organizations the Business Architectures describe the nature of
the information shared between stakeholders and/or organizations (e.g.,
in defense the term is “operational node”), and the Data Architecture
specifies the information shared between systems.

Update the defined target data and Application Architecture (Approved)
with the interoperability issues that were raised.

</details>

<a id="tag_07_06"></a>
## 6.6. Reconciling Interoperability Requirements with Potential Solutions

概念：COTS内嵌业务流程可能与所需业务互操作冲突。

适用条件：重用SBB或购买产品。

逻辑关系：改内嵌流程成本可能消除复用收益，并影响跨系统工作流。

决策方法：业务互操作变化由业务架构师及赞助者签署修订工作说明。

制品及证据：冲突评估和修订SoAW。

适用边界：技术接口一致不证明业务流程兼容。

来源块：C220-web-2025:03-adm-techniques:b00382, C220-web-2025:03-adm-techniques:b00383, C220-web-2025:03-adm-techniques:b00384, C220-web-2025:03-adm-techniques:b00385

<details><summary>展开本节完整英文来源</summary>

6.6. Reconciling Interoperability Requirements with Potential Solutions

The Enterprise Architect will have to ensure that there are no
interoperability conflicts, especially if there is an intention to
re-use existing SBBs and/or COTS.

The most significant issue to be addressed is in fact business
interoperability. Most SBBs or COTS will have their own business
processes embedded. Changing the embedded business processes will often
require so much work that the advantages of re-using solutions will be
lost. There are numerous examples of this in the past.

Furthermore, there is the workflow aspect between the various systems
that has to be taken into account. The Enterprise Architect will have to
ensure that any change to the business interoperability requirements is
signed off by the Business Architects and architecture sponsors in a
revised Statement of Architecture Work.

</details>

<a id="chap07"></a>
## 7. Business Transformation Readiness Assessment

概念：就绪度评估发现基线到目标变革中的人员和组织问题。

适用条件：业务转型而非只安装技术。

逻辑关系：评估输出进入E/F计划并在G监控。

决策方法：采用组织因子和标准，不从模板填充自动评级。

制品及证据：就绪度评估和改进行动。

适用边界：本章BTEP是方法来源而非组织现状。

来源块：C220-web-2025:03-adm-techniques:b00386, C220-web-2025:03-adm-techniques:b00387, C220-web-2025:03-adm-techniques:b00388

<details><summary>展开本节完整英文来源</summary>

7. Business Transformation Readiness Assessment

This chapter describes a technique known as Business Transformation Readiness Assessment, used for evaluating and quantifying an
organization’s readiness to undergo change.

This chapter builds on work by the Canadian Government and its Business
Transformation Enablement Program (BTEP).

</details>

<a id="tag_08_01"></a>
## 7.1. Introduction

概念：技术可行架构仍可能因文化、技能和变革承受力而失败。

适用条件：重大信息整合或服务导向转型。

逻辑关系：HR、业务与IT规划共同确定因子、成熟度、风险和迁移动作。

决策方法：将转型问题与架构计划联合处理。

制品及证据：跨部门工作坊、因子及迁移动作。

适用边界：不能只以技术上线证明转型成功。

来源块：C220-web-2025:03-adm-techniques:b00389, C220-web-2025:03-adm-techniques:b00390, C220-web-2025:03-adm-techniques:b00391, C220-web-2025:03-adm-techniques:b00392, C220-web-2025:03-adm-techniques:b00393

<details><summary>展开本节完整英文来源</summary>

7.1. Introduction

Enterprise Architecture is a major endeavor within an organization and
most often an innovative Architecture Vision (Phase A) and supporting
Architecture Definition (Phases B to D) will entail considerable change.
There are many dimensions to change, but by far the most important is
the human element. For example, if the enterprise envisages a
consolidation of information holdings and a move to a new paradigm such
as service orientation for integrated service delivery, then the human
resource implications are major. Potentially coupled with a
change-averse culture and a narrowly skilled workforce, the most sound
and innovative architecture could go nowhere.

Understanding the readiness of the organization to accept change,
identifying the issues, and then dealing with them in the Implementation
and Migration Plans is key to successful architecture transformation in
Phases E and F. This will be a joint effort between corporate
(especially human resources) staff, lines of business, and IT planners.

The recommended activities in an assessment of an organization’s
readiness to address business transformation are:

Determine the readiness factors that will impact the organization Present the readiness factors using maturity models Assess the readiness factors, including determination of readiness
factor ratings Assess the risks for each readiness factor and identify improvement
actions to mitigate the risk Work these actions into Phase E and F Implementation and Migration
Plan

</details>

<a id="tag_08_01_01"></a>
## 7.1.1. Business Transformation Enablement Program (BTEP)

概念：BTEP建议所有项目至少发现转型问题。

适用条件：借鉴加拿大政府方法。

逻辑关系：评估得到挑战机会，其中部分转为需治理风险。

决策方法：按本组织替换、增删因子与标准。

制品及证据：因子选择及方法裁剪。

适用边界：建议不把BTEP变成每组织强制政策。

来源块：C220-web-2025:03-adm-techniques:b00394, C220-web-2025:03-adm-techniques:b00395, C220-web-2025:03-adm-techniques:b00396, C220-web-2025:03-adm-techniques:b00397

<details><summary>展开本节完整英文来源</summary>

7.1.1. Business Transformation Enablement Program (BTEP)

The Canadian Government Business Transformation Enablement Program
(BTEP) provides guidance on how to identify the business
transformation-related issues.

The BTEP recommends that all projects conduct a transformation readiness assessment to at least uncover the business transformation issues. This
assessment is based upon the determination and analysis/rating of a
series of readiness factors. The outcome is a deeper understanding of
the challenges and opportunities that could be presented in the course
of the endeavor. Many of the challenges translate directly into risks
that have to be addressed, monitored, and, if possible, mitigated.

The following sections describe Business Transformation Readiness
Assessment using the BTEP method, including some lessons learned.
Readers should keep in mind that most organizations will have their own
unique set of factors and criteria, but most are similar.

</details>

<a id="tag_08_02"></a>
## 7.2. Determine Readiness Factors

概念：示例12因子包含愿景、意愿、需要、商业论证、资金、领导、治理、问责、方法、IT执行、企业执行和运营能力。

适用条件：从多部门获取不同观点。

逻辑关系：因子先定义后评估，既有类似交付及技能是证据线索。

决策方法：工作坊可重用、拒绝、增补或替换初始因子。

制品及证据：因子定义、组织范围、历史执行与资源证据。

适用边界：不能伪造类似项目、半规模经历或能力证明。

来源块：C220-web-2025:03-adm-techniques:b00398, C220-web-2025:03-adm-techniques:b00399, C220-web-2025:03-adm-techniques:b00400, C220-web-2025:03-adm-techniques:b00401, C220-web-2025:03-adm-techniques:b00402

<details><summary>展开本节完整英文来源</summary>

7.2. Determine Readiness Factors

The first step is to determine what factors will impact on the business
transformation associated with the migration from the Baseline to Target
Architectures.

This can be best achieved through the conduct of a facilitated workshop
with individuals from different parts of the organization. It is
important that all perspectives are sought as the issues will be varied.
In this workshop it is very useful to start off with a tentative list of
factors that participants can re-use, reject, augment, or replace. An example set of factors drawn from the BTEP follows:

Vision is the ability to clearly define and communicate what is to
be achieved This is where management is able to clearly define the objectives, in
both strategic and specific terms. Leadership in defining vision and
needs comes from the business side with IT input. Predictable and proven
processes exist for moving from vision to statement of requirements. The
primary drivers for the initiative are clear. The scope and approach of
the transformation initiative have been clearly defined throughout the
organization. Desire, Willingness, and Resolve is the presence of a desire to
achieve the results, willingness to accept the impact of doing the work,
and the resolve to follow through and complete the endeavor There is active discussion regarding the impact that executing the
project may have on the organization, with a clear indication of the
intent to accept the impacts. Key resources (e.g., financial, human,
etc.) are allocated for the endeavor and top executives project the
clear message that the organization will follow through; a message that
identifies the effort as well as the benefits. Organizationally there is
a history of finishing what is started and of coming to closure on
issues in the timeframes needed and there is agreement throughout the
organization that the transformation initiative is the “right” thing to
do. Need , in that there is a compelling need to execute the endeavor There are clear statements regarding what the organization will not be
able to do if the project does not proceed, and equally clear statements
of what the project will enable the organization to do. There are
visible and broadly understood consequences of endeavor failure and
success criteria have been clearly identified and communicated. Business Case exists that creates a strong focus for the project,
identifying benefits that must be achieved and thereby creating an
imperative to succeed The business case document identifies concrete benefits (revenues or
savings) that the organization is committed to deliver and clearly and
unquestionably points to goals that the organization is committed to
achieving. Funding , in the form of a clear source of fiscal resources, exists
that meets the endeavor’s potential expenditures Sponsorship and Leadership exists and is broadly shared, but not so
broad as to diffuse accountability Leadership keeps everyone “on board” and keeps all focused on the
strategic goals. The endeavor is sponsored by an executive who is
appropriately aligned to provide the leadership the endeavor needs and
able to articulate and defend the needs of the endeavor at the senior
management level. These executive sponsors are and will remain engaged
throughout. Governance is the ability to engage the involvement and support of
all parties with an interest in or responsibility to the endeavor with
the objective of ensuring that the corporate interests are served and
the objectives achieved There are clearly identified stakeholders and a clear sense of their
interest in and responsibility to the project; a culture that encourages
participation towards corporate rather than local objectives; a history
of being able to successfully manage activities that cross interest
areas; a culture that fosters meaningful, as opposed to symbolic,
participation in management processes; and a commitment to ongoing
project review and challenge and openness to outside advice. Accountability is the assignment of specific and appropriate
responsibility, recognition of measurable expectations by all concerned
parties, and alignment of decision-making with areas of responsibility
and with where the impact of the decisions will be felt Accountability is aligned with the area where the benefits of success or
consequences of failure of the endeavor will be felt as well as with the
responsibility areas. Workable Approach and Execution Model is an approach that makes
sense relative to the task, with a supporting environment, modeled after
a proven approach There are clear notions of the client and the client’s role relative to
the builder or prime contractor and the organization is experienced with
endeavors of this type so that the processes, disciplines, expertise,
and governance are already in place, proven, and available to apply to
the transformation endeavor. All the players know their roles because
they have played them before with success. In particular, the roles of
“client” and “systems builder” are mature and stable. There is a
communication plan covering all levels of the organization and meeting
the needs ranging from awareness to availability of technical detail.
There is a reward and recognition plan in place to recognize teams and
individuals who use good change management practices, planning and
prevention of crisis behaviors, and who reinforce behaviors appropriate
to the new way of doing business. It is clear to everyone how
implementation will occur, how it will be monitored, and how realignment
actions will be made and there are adequate resources dedicated for the
life of the transformation. IT Capacity to Execute is the ability to perform all the IT tasks
required by the project, including the skills, tools, processes, and
management capability There has been a recent successful execution of a similar endeavor of
similar size and complexity and there exist appropriate processes,
discipline, skills, and a rationale model for deciding what skills and
activities to source externally. Enterprise Capacity to Execute is the ability of the enterprise to
perform all the tasks required by the endeavor, in areas outside of IT,
including the ability to make decisions within the tight time
constraints typical to project environments based upon the recent
successful execution of a similar endeavor of at least half the size and
complexity There exist non-IT-specific processes, discipline, and skills to deal
with this type of endeavor. The enterprise has a demonstrated ability to
deal with the type of ongoing project/portfolio management issues and
requirements. There is a recognition of the need for knowledge and
skill-building for the new way of working as well as the value of a
formal gap analysis for skills and behavior. Enterprise Ability to Implement and Operate the transformation
elements and their related business processes, absorb the changes
arising from implementation, and ongoing ability to operate in the new
environment The enterprise has a recent proven ability to deal with the change
management issues arising from new processes and systems and has in
place a solid disciplined and process-driven service management program
that provides operations, maintenance, and support for existing systems.

Once the factors have been identified and defined, it is useful to call
a follow-on workshop where the factors shall be assessed in some detail
in terms of their impact/risk. The next section will deal with preparing
for an effective assessment of these factors.

</details>

<a id="tag_08_03"></a>
## 7.3. Present Readiness Factors

概念：成熟度模型帮助明确基线、目标和可较早达到的中间目标。

适用条件：使评估工作坊聚焦且一致。

逻辑关系：模型可复用为治理资产，预先征求意见和架构师建议目标。

决策方法：针对本架构范围准备模型和工作表。

制品及证据：模型、工作表、预审反馈及目标依据。

适用边界：图中推荐4级不是本企业必须达到的等级。

来源块：C220-web-2025:03-adm-techniques:b00403, C220-web-2025:03-adm-techniques:b00404, C220-web-2025:03-adm-techniques:b00405, C220-web-2025:03-adm-techniques:b00406, C220-web-2025:03-adm-techniques:b00407, C220-web-2025:03-adm-techniques:b00408, C220-web-2025:03-adm-techniques:b00409, C220-web-2025:03-adm-techniques:b00410, C220-web-2025:03-adm-techniques:b00411, C220-web-2025:03-adm-techniques:b00412, C220-web-2025:03-adm-techniques:b00413

<details><summary>展开本节完整英文来源</summary>

7.3. Present Readiness Factors

Once the factors are determined, it is necessary to present them in such
a way that the assessment is clear and the maximum value is derived from
the participants.

One such presentation is through the use of maturity models. If each
factor is converted into a maturity model (a re-usable governance asset
as well) accompanied by a standard worksheet template containing all of
the information and deductions that have to be gathered, it can be a
very useful tool.

The maturity model should enable participants to:

Assess their current (Baseline Architecture) maturity level Determine the target maturity level that would have to be achieved to
realize the Target Architecture Determine an intermediate target that would be achievable in a lesser
timeframe

The care spent preparing the models (which is not insignificant) will be
recouped by a focused workshop that will rapidly go through a
significant number of factors.

It is important that each factor be well-defined and that the scope of
the Enterprise Architecture endeavor (preliminary planning) be reflected
in the models to keep the workshop participants focused and productive.

Circulating the models before the workshop for comments would be useful,
if only to ensure that they are complete as well as allowing the
participants to prepare for the workshop. Note that the model shown
below also has a recommended target state put in by the Enterprise
Architect; this again acts as governance.

An example of a maturity model is shown in Figure 7-1 for one of the BTEP factors.



Figure 7-1: Business Transformation Readiness Assessment — Maturity Model

</details>

<a id="tag_08_04"></a>
## 7.4. Assess Readiness Factors

概念：评估同时处理因子愿景、评级及风险行动。

适用条件：多学科工作坊时间有限时。

逻辑关系：统一模板保证不同因子的可比较记录。

决策方法：逐因子取得三类结果。

制品及证据：完整评估记录。

适用边界：共同模板不保证判断证据充分。

来源块：C220-web-2025:03-adm-techniques:b00414, C220-web-2025:03-adm-techniques:b00415, C220-web-2025:03-adm-techniques:b00416, C220-web-2025:03-adm-techniques:b00417, C220-web-2025:03-adm-techniques:b00418

<details><summary>展开本节完整英文来源</summary>

7.4. Assess Readiness Factors

Ideally, the factors should be assessed in a multi-disciplinary
workshop. Using a mechanism such as maturity models, Enterprise
Architects will normally have to cover a great deal of ground in little
time.

The use of a series of templates for each factor would expedite the
assessment, and ensure consistency across the wide range of factors.

The assessment should address three things, namely:

Readiness Factor Vision Readiness Factor Rating Readiness Factor Risks & Actions

</details>

<a id="tag_08_04_01"></a>
## 7.4.1. Readiness Factor Vision

概念：就绪因子愿景定义基线、目标与可能中间状态。

适用条件：确定实现架构所需的组织能力变化。

逻辑关系：目标取决于愿景，不是总要求最高成熟度。

决策方法：核对实现目标必需的状态和可达中间状态。

制品及证据：因子基线/目标及依据。

适用边界：IT低到高是例子，未知不能当低。

来源块：C220-web-2025:03-adm-techniques:b00419, C220-web-2025:03-adm-techniques:b00420, C220-web-2025:03-adm-techniques:b00421

<details><summary>展开本节完整英文来源</summary>

7.4.1. Readiness Factor Vision

The vision for a readiness factor is the determination of where the
enterprise has to evolve to address the factor. First, the factor should
be assessed with respect to its base state and then its target state.

For example, if the “IT capacity to execute” factor is rated as low, the
factor should ideally be at “high” to realize the Target Architecture
Vision. An intermediate target might be useful to direct the
implementation. Maturity models are excellent vehicles to guide this
determination.

</details>

<a id="tag_08_04_02"></a>
## 7.4.2. Readiness Factor Rating

概念：紧迫性、就绪状态、修复难度是不同维度。

适用条件：汇总因子重要性与改变难度。

逻辑关系：紧迫是启动前要处理；就绪Low/Fair/Acceptable/Good/High；难度No Action/Easy/Moderate/Difficult。

决策方法：分别判断三维并记录证据。

制品及证据：管理汇总与逐因子评估。

适用边界：无官方数字换算，更不能与G212回答量表直接换分。

来源块：C220-web-2025:03-adm-techniques:b00422, C220-web-2025:03-adm-techniques:b00423, C220-web-2025:03-adm-techniques:b00424, C220-web-2025:03-adm-techniques:b00425, C220-web-2025:03-adm-techniques:b00426, C220-web-2025:03-adm-techniques:b00427, C220-web-2025:03-adm-techniques:b00428

<details><summary>展开本节完整英文来源</summary>

7.4.2. Readiness Factor Rating

Once the factor visions are established, then it is useful to determine
how important each factor is to the achievement of the Target
Architecture as well as how challenging it will be to migrate the factor
into an acceptable visionary state.

The BTEP uses a Readiness Rating Scheme that can be used as a start
point for any organization in any vertical. Each one of the readiness
factors are rated with respect to:

Urgency , whereby if a readiness factor is urgent, it means that
action is needed before a transformation initiative can begin Readiness Status , which is rated as either Low (needs substantial
work before proceeding), Fair (needs some work before proceeding),
Acceptable (some readiness issues exist; no showstoppers), Good
(relatively minor issues exist), or High (no readiness issues) Degree of Difficulty to Fix rates the effort required to overcome
any issues identified as either No Action Needed, Easy, Moderate, or
Difficult

Although a more extensive template can be used in the workshop, it is
useful to create a summary table of the findings to consolidate the
factors and provide a management overview. A summary is shown in Figure 7-2 .



Figure 7-2: Summary Table of Business Transformation Readiness Assessment

</details>

<a id="tag_08_04_03"></a>
## 7.4.3. Readiness Factor Risks & Actions

概念：为每个因子提出风险改进行动并纳入迁移计划。

适用条件：已完成因子评估。

逻辑关系：先检查架构既有行动避免重复，再估影响频率及剩余风险。

决策方法：复用或新增行动，正式整合E/F并持续监控。

制品及证据：行动、风险及计划追溯。

适用边界：原文错指第9章作风险过程；应并列第8章而不默改来源。

来源块：C220-web-2025:03-adm-techniques:b00429, C220-web-2025:03-adm-techniques:b00430, C220-web-2025:03-adm-techniques:b00431, C220-web-2025:03-adm-techniques:b00432, C220-web-2025:03-adm-techniques:b00433, C220-web-2025:03-adm-techniques:b00434

<details><summary>展开本节完整英文来源</summary>

7.4.3. Readiness Factor Risks & Actions

Once the factors have been rated and assessed, derive a series of actions that will enable the factors to change to a favorable state.

Each factor should be assessed with respect to risk using the process highlighted in Chapter 9, Architecture Alternatives and Trade-Offs ,
including an estimate of impact and frequency.

Each factor should be discretely assessed and a series of improvement
actions outlined. Before starting anew, existing actions outlined in the
architectures should be checked first before creating new ones.

These newly identified actions should then be formally incorporated into
the emerging Implementation and Migration Plan.

From a risk perspective, these actions are designed to mitigate the
risks and produce an acceptable residual risk. As risks, they should be
part of the risk management process and closely monitored as the
Enterprise Architecture is being implemented.

</details>

<a id="tag_08_05"></a>
## 7.5. Readiness and Migration Planning

概念：就绪评估影响关键路径和E/F迁移可行性。

适用条件：员工训练、支持运营与技术交付相互依赖。

逻辑关系：G持续监控，必要时通过IT治理迅速纠正。

决策方法：检查转型动作是否阻塞上线，保留活文档。

制品及证据：关键路径、实施迁移计划和监测记录。

适用边界：训练计划存在不等于人员已能运营。

来源块：C220-web-2025:03-adm-techniques:b00435, C220-web-2025:03-adm-techniques:b00436, C220-web-2025:03-adm-techniques:b00437, C220-web-2025:03-adm-techniques:b00438

<details><summary>展开本节完整英文来源</summary>

7.5. Readiness and Migration Planning

The assessment exercise will provide a realistic assessment of the
organization and will be a key input into the strategic migration
planning that will be initiated in Phase E and completed in Phase F. It
is important to note whether the business transformation actions will be
on the vision’s critical path and, if so, determine how they will impact
implementation. There is no point deploying new IT capability without
employees trained to use it and support staff ready to sustain it.

The readiness factors, as part of an overall Implementation and
Migration Plan, will have to be continuously monitored (Phase G) and
rapid corrective actions taken through the IT governance framework to
ensure that the defined architectures can be implemented.

The readiness factors assessment will be a living document and during
the migration planning and execution of the Transition Architectures,
the business transformation activities will play a key role.

</details>

<a id="tag_08_06"></a>
## 7.6. Marketing the Implementation Plan

概念：广泛发布架构前应识别转型影响并安排支持行动。

适用条件：如整合导致岗位减少等敏感变革。

逻辑关系：工作坊也是沟通计划，实施计划应持续告知受影响人员。

决策方法：协同HR、工会等安排再培训和支持沟通。

制品及证据：人员转型及沟通计划。

适用边界：不是允许隐瞒事实或替代适用义务的规则。

来源块：C220-web-2025:03-adm-techniques:b00439, C220-web-2025:03-adm-techniques:b00440, C220-web-2025:03-adm-techniques:b00441, C220-web-2025:03-adm-techniques:b00442, C220-web-2025:03-adm-techniques:b00443, C220-web-2025:03-adm-techniques:b00444

<details><summary>展开本节完整英文来源</summary>

7.6. Marketing the Implementation Plan

The Architecture Definition should not be widely circulated until the
business transformation issues are identified and mitigated, and the
associated actions part of an overall “marketing” plan for the vision
and the Implementation and Migration Plan.

For example, the consolidation of information holdings could result in
hundreds of lost jobs and this vision should not be announced before a
supporting business transformation/human resources plan is formulated to
retrain or support the workers’ quest for new employment.

The business transformation workshops are a critical part of the
Communications Plan whereby key individuals from within the organization
gather to assess the implications of transforming the enterprise. To do
this they will become aware of the Architecture Vision and architecture
definition (if they were not already involved through the business
scenarios and Business Architecture). This group will feel ownership of
the Enterprise Architecture, recognizing the Enterprise Architect as a
valuable steward.

Their determination of the factors will again create a culture of
understanding across the enterprise and provide useful insights for the
Implementation and Migration Plan.

The latter plan should include a Communications Plan, especially to keep
the affected personnel informed. In many cases collaborating with the
unions and shop stewards will further assist a humane (and peaceful)
transition to the target state.

</details>

<a id="tag_08_07"></a>
## 7.7. Conclusion

概念：实施计划同时包含技术与文化等转型因素。

适用条件：目标愿景需改变人员和组织。

逻辑关系：忽视文化会使技术结果不足以实现价值。

决策方法：评审计划是否覆盖关键转型因子。

制品及证据：完整转型计划。

适用边界：不能从本章结论自动判断哪个技术方案最优。

来源块：C220-web-2025:03-adm-techniques:b00445, C220-web-2025:03-adm-techniques:b00446

<details><summary>展开本节完整英文来源</summary>

7.7. Conclusion

In short, Enterprise Architecture implementation will require a deep
knowledge and awareness of all of the business transformation factors
that impact transitioning to the visionary state. With the evolution of
IT, the actual technology is not the real issue any more in Enterprise
Architecture, but the critical factors are most often the cultural ones.
Any Implementation and Migration Plan has to take both into
consideration. Neglecting these and focusing on the technical aspects
will invariably result in an implementation that falls short of
realizing the real promise of a visionary Enterprise Architecture.

</details>

<a id="chap08"></a>
## 8. Risk Management

概念：风险管理用于识别、分类、缓解、接受和监控转型风险。

适用条件：架构项目全生命周期。

逻辑关系：初始与剩余风险区分行动前后。

决策方法：使用企业风险框架，明确治理接受主体。

制品及证据：风险管理计划及登记册。

适用边界：风险数目少不等于风险可接受。

来源块：C220-web-2025:03-adm-techniques:b00447, C220-web-2025:03-adm-techniques:b00448

<details><summary>展开本节完整英文来源</summary>

8. Risk Management

This chapter describes risk management, which is a technique used to
mitigate risk when implementing an architecture project.

</details>

<a id="tag_09_01"></a>
## 8.1. Introduction

概念：风险触发可来自规划范围外，缓解需持续监测情境。

适用条件：任何业务/架构转型。

逻辑关系：架构师识别和部分缓解，接受和管理在治理框架内。

决策方法：先分类识别初始风险，再缓解评估与监测。

制品及证据：初始/剩余风险及责任。

适用边界：架构师不能由分析结果自授接受权限。

来源块：C220-web-2025:03-adm-techniques:b00449, C220-web-2025:03-adm-techniques:b00450, C220-web-2025:03-adm-techniques:b00451, C220-web-2025:03-adm-techniques:b00452, C220-web-2025:03-adm-techniques:b00453, C220-web-2025:03-adm-techniques:b00454, C220-web-2025:03-adm-techniques:b00455, C220-web-2025:03-adm-techniques:b00456

<details><summary>展开本节完整英文来源</summary>

8.1. Introduction

There will always be risk with any architecture/business transformation
effort. It is important to identify, classify, and mitigate these risks
before starting so that they can be tracked throughout the
transformation effort.

Mitigation is an ongoing effort and often the risk triggers may be
outside the scope of the transformation planners (e.g., merger,
acquisition) so planners must monitor the transformation context
constantly.

It is also important to note that the Enterprise Architect may identify
the risks and mitigate certain ones, but it is within the governance
framework that risks have to be first accepted and then managed.

There are two levels of risk that should be considered, namely:

Initial Level of Risk : risk categorization prior to determining and
implementing mitigating actions Residual Level of Risk : risk categorization after implementation of
mitigating actions (if any)

The process for risk management is described in the following sections
and consists of the following activities:

Risk classification Risk identification Initial risk assessment Risk mitigation and residual risk assessment Risk monitoring

</details>

<a id="tag_09_02"></a>
## 8.2. Risk Classification

概念：按影响、时间成本范围、架构域及企业分类组织风险。

适用条件：确定治理级别和处理职责。

逻辑关系：EA风险属于企业风险，应采用或扩展现有分类。

决策方法：与企业风险体系协调而非另造冲突体系。

制品及证据：风险类别与升级规则。

适用边界：示例分类不是完整唯一分类。

来源块：C220-web-2025:03-adm-techniques:b00457, C220-web-2025:03-adm-techniques:b00458, C220-web-2025:03-adm-techniques:b00459, C220-web-2025:03-adm-techniques:b00460, C220-web-2025:03-adm-techniques:b00461, C220-web-2025:03-adm-techniques:b00462

<details><summary>展开本节完整英文来源</summary>

8.2. Risk Classification

Risk is pervasive in any Enterprise Architecture activity and is present
in all phases within the ADM. From a management perspective, it is useful to classify the risks so that the mitigation of the risks can be executed as expeditiously as possible.

One common way for risks to be classified is with respect to impact on the organization (as discussed in Section 8.4, “Initial Risk Assessment” ), whereby risks with certain impacts have to be addressed by
certain levels of governance.

Risks are normally classified as time (schedule), cost (budget), and scope but they could also include client transformation relationship risks, contractual risks, technological risks, scope and complexity
risks, environmental (corporate) risks, personnel risks, and client acceptance risks.

Another way of delegating risk management is to further classify risks by architecture domains. Classifying risks as business, information,
applications, and technology is useful but there may be organizationally-specific ways of expressing risk that the corporate Enterprise Architecture directorate should adopt or extend rather than
modify.

Ultimately, Enterprise Architecture risks are corporate risks and should be classified and as appropriate managed in the same or extended way.

</details>

<a id="tag_09_03"></a>
## 8.3. Risk Identification

概念：成熟度与就绪度差距可暴露未达到目标的风险。

适用条件：筹划能力和组织变化。

逻辑关系：风险管理计划覆盖应急、跟踪、评估和沟通。

决策方法：从目标差距识别风险并选用适合组织的方法模板。

制品及证据：风险管理计划、触发和沟通程序。

适用边界：PMBOK/PRINCE2等只是方法引用，不代表已执行。

来源块：C220-web-2025:03-adm-techniques:b00463, C220-web-2025:03-adm-techniques:b00464, C220-web-2025:03-adm-techniques:b00465, C220-web-2025:03-adm-techniques:b00466, C220-web-2025:03-adm-techniques:b00467

<details><summary>展开本节完整英文来源</summary>

8.3. Risk Identification

The maturity and transformation readiness assessments will generate a great many risks. Identify the risks and then determine the strategy to address them throughout the transformation.

The use of Capability Maturity Models (CMMs) is suitable for specific factors associated with architecture delivery to first identify baseline
and target states and then identify the actions required to move to the target state. The implications of not achieving the target state can
result in the discovery of risks. Refer to Chapter 8, Risk Management for specific details.

Risk documentation is completed in the context of a Risk Management Plan, for which templates exist in standard project management methodologies — e.g., Project Management Body of Knowledge (PMBOK ® ) and
PRINCE2 ® — as well as with the various government methodologies.

Normally these methodologies involve procedures for contingency planning, tracking and evaluating levels of risk, reacting to changing risk level factors, as well as processes for documenting, reporting, and
communicating risks to stakeholders.

</details>

<a id="tag_09_04"></a>
## 8.4. Initial Risk Assessment

概念：按效应与频率组合评估初始风险。

适用条件：使用组织已有尺度，缺少时可参考示例。

逻辑关系：四效应×五频率的序数分类映射E/H/M/L，非算术乘积。

决策方法：逐风险估效应频率，再按一致分类映射判断。

制品及证据：尺度、估计依据和初始评估。

适用边界：原文无固定数值概率或损失阈值。

来源块：C220-web-2025:03-adm-techniques:b00468, C220-web-2025:03-adm-techniques:b00469, C220-web-2025:03-adm-techniques:b00470, C220-web-2025:03-adm-techniques:b00471, C220-web-2025:03-adm-techniques:b00472, C220-web-2025:03-adm-techniques:b00473, C220-web-2025:03-adm-techniques:b00474, C220-web-2025:03-adm-techniques:b00475, C220-web-2025:03-adm-techniques:b00476, C220-web-2025:03-adm-techniques:b00477, C220-web-2025:03-adm-techniques:b00478, C220-web-2025:03-adm-techniques:b00479

<details><summary>展开本节完整英文来源</summary>

8.4. Initial Risk Assessment

The next step is to classify risks with respect to effect and frequency in accordance with scales used within the organization. Combine effect and frequency to come up with a preliminary risk assessment.

There are no hard and fast rules with respect to measuring effect and frequency. The following guidelines are based upon existing risk
management best practices.

Effect could be assessed using the following example criteria:

Catastrophic infers critical financial loss that could result in
bankruptcy of the organization Critical infers serious financial loss in more than one line of
business leading to a loss in productivity and no return on investment
on the IT investment Marginal infers a minor financial loss in a line of business and a
reduced return on investment on the IT investment Negligible infers a minimal impact on a line of business’ ability to
deliver services and/or products

Frequency could be indicated as follows:

Frequent : likely to occur very often and/or continuously Likely : occurs several times over the course of a transformation
cycle Occasional : occurs sporadically Seldom : remotely possible and would probably occur not more than
once in the course of a transformation cycle Unlikely : will probably not occur during the course of a
transformation cycle

Combining the two factors to infer impact would be conducted using a
heuristically-based but consistent classification scheme for the risks.
A potential scheme to assess corporate impact could be as follows:

Extremely High Risk (E) : the transformation effort will most likely
fail with severe consequences High Risk (H) : significant failure of parts of the transformation
effort resulting in certain goals not being achieved Moderate Risk (M) : noticeable failure of parts of the transformation
effort threatening the success of certain goals Low Risk (L) : certain goals will not be wholly successful

These impacts can be derived using a classification scheme, as shown in Figure 8-1 .



Figure 8-1: Risk Classification Scheme

</details>

<a id="tag_09_05"></a>
## 8.5. Risk Mitigation and Residual Risk Assessment

概念：缓解包括识别、计划并实施降低风险的行动。

适用条件：优先频繁且高影响风险。

逻辑关系：措施从监测接受到冗余应急，带来范围成本时间后果。

决策方法：系统且务实地比较缓解方案和可接受水平。

制品及证据：缓解动作、资源及连续性计划。

适用边界：仅计划措施不能宣称剩余风险已实际降低。

来源块：C220-web-2025:03-adm-techniques:b00480, C220-web-2025:03-adm-techniques:b00481, C220-web-2025:03-adm-techniques:b00482, C220-web-2025:03-adm-techniques:b00483

<details><summary>展开本节完整英文来源</summary>

8.5. Risk Mitigation and Residual Risk Assessment

Risk mitigation refers to the identification, planning, and conduct of
actions that will reduce the risk to an acceptable level.

The mitigation effort could be a simple monitoring and/or acceptance of
the risk to a full-blown contingency plan calling for complete
redundancy in a Business Continuity Plan (with all of the associated
scope, cost, and time implications).

Due to the implications of this risk assessment, it has to be conducted
in a pragmatic but systematic manner. With priority going to frequent
high impact risks, each risk has to be mitigated in turn.

</details>

<a id="tag_09_06"></a>
## 8.6. Conduct Residual Risk Assessment

概念：重新评估效应和频率验证缓解是否有实质差异。

适用条件：措施确定及实施后的风险复审。

逻辑关系：从Frequent/Catastrophic到Frequent/Critical仍为E，换格不必降级。

决策方法：质疑高投入低收益或仍同高风险区的措施，重新设计。

制品及证据：初始与剩余对照工作表及实施证据。

适用边界：文本先说确定后重估，风险定义又要求实施后；预测与实现剩余值必须分开。

来源块：C220-web-2025:03-adm-techniques:b00484, C220-web-2025:03-adm-techniques:b00485, C220-web-2025:03-adm-techniques:b00486, C220-web-2025:03-adm-techniques:b00487, C220-web-2025:03-adm-techniques:b00488, C220-web-2025:03-adm-techniques:b00489

<details><summary>展开本节完整英文来源</summary>

8.6. Conduct Residual Risk Assessment

Once the mitigation effort has been identified for each one of the
risks, re-assess the effect and frequency and then recalculate the
impacts and see whether the mitigation effort has really made an
acceptable difference. The mitigation efforts will often be
resource-intensive and a major outlay for little or no residual risk
should be challenged.

Once the initial risk is mitigated, then the risk that remains is called
the “residual risk”. The key consideration is that the mitigating effort
actually reduces the corporate impact and does not just move the risk to
another similarly high quadrant. For example, changing the risk from
frequent/catastrophic to frequent/critical still delivers an extremely
high risk. If this occurs, then the mitigation effort has to be
re-considered.

The final deliverable should be a transformation risk assessment that
could be structured as a worksheet, as shown in Figure 8-2 .



Figure 8-2: Sample Risk Identification and Mitigation Assessment Worksheet

</details>

<a id="tag_09_07"></a>
## 8.7. Risk Monitoring and Governance (Phase G)

概念：剩余风险由IT治理及必要的企业治理批准后持续监测。

适用条件：Phase G实施治理。

逻辑关系：监控确保实际处理的是剩余风险，未缓解关键风险可触发完整或部分ADM循环。

决策方法：核实接受记录与动作执行证据，升级新的关键风险。

制品及证据：更新风险工作表、接受与监控记录。

适用边界：没有真实授权记录就维持未接受状态。

来源块：C220-web-2025:03-adm-techniques:b00490, C220-web-2025:03-adm-techniques:b00491, C220-web-2025:03-adm-techniques:b00492, C220-web-2025:03-adm-techniques:b00493

<details><summary>展开本节完整英文来源</summary>

8.7. Risk Monitoring and Governance (Phase G)

The residual risks have to be approved by the IT governance framework
and potentially in corporate governance where business acceptance of the
residual risks is required.

Once the residual risks have been accepted, then the execution of the
mitigating actions has to be carefully monitored to ensure that the
enterprise is dealing with residual rather than initial risk. The risk
identification and mitigation assessment worksheets are maintained as
governance artifacts and are kept up-to-date in Phase G (Implementation
Governance) where risk monitoring is conducted.

Implementation governance can identify critical risks that are not being
mitigated and might require another full or partial ADM cycle.

</details>

<a id="tag_09_08"></a>
## 8.8. Summary

概念：优先使用或扩展企业既有风险方法，缺少时可参考本章。

适用条件：组织风险方法裁剪。

逻辑关系：风险是EA活动组成部分。

决策方法：记录采用方法及与企业治理的一致性。

制品及证据：方法选择和风险治理约定。

适用边界：参考最佳实践不等于获得外部认证。

来源块：C220-web-2025:03-adm-techniques:b00494, C220-web-2025:03-adm-techniques:b00495

<details><summary>展开本节完整英文来源</summary>

8.8. Summary

Risk management is an integral part of Enterprise Architecture.
Practitioners are encouraged to use their corporate risk management
methodology or extend it using the guidance in this chapter. In the
absence of a formal corporate methodology, architects can use the
guidance in this chapter as a best practice.

</details>

<a id="chap09"></a>
## 9. Architecture Alternatives and Trade-Offs

概念：满足同一愿景原则需求的目标架构可能不止一个。

适用条件：架构域、阶段及不同抽象层均可权衡。

逻辑关系：备选分析揭示隐含关切和需求。

决策方法：先提出候选再比较，允许组合特征。

制品及证据：备选架构及权衡决定。

适用边界：不能先选最优再倒填评估标准。

来源块：C220-web-2025:03-adm-techniques:b00496, C220-web-2025:03-adm-techniques:b00497

<details><summary>展开本节完整英文来源</summary>

9. Architecture Alternatives and Trade-Offs

This chapter describes a technique to identify alternative Target
Architectures and perform trade-offs between the alternatives.

</details>

<a id="tag_10_01"></a>
## 9.1. Concept

概念：通过多个备选及其权衡理解竞争力量。

适用条件：利益相关者未显露全部目标时。

逻辑关系：讨论可暴露隐藏议程、原则和需求。

决策方法：把新发现需求返回架构分析。

制品及证据：备选与新关切记录。

适用边界：符合愿景仍需检验实施影响。

来源块：C220-web-2025:03-adm-techniques:b00498, C220-web-2025:03-adm-techniques:b00499

<details><summary>展开本节完整英文来源</summary>

9.1. Concept

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

<a id="tag_10_02"></a>
## 9.2. Method

概念：标准、候选、选择三部分可分域开展再合并。

适用条件：没有单个方案满足全部关切。

逻辑关系：影响范围仍须覆盖整体架构。

决策方法：只做到支持当前决定所需细节。

制品及证据：跨域备选分析。

适用边界：图中三个备选是示例，不限制数量。

来源块：C220-web-2025:03-adm-techniques:b00500, C220-web-2025:03-adm-techniques:b00501, C220-web-2025:03-adm-techniques:b00502, C220-web-2025:03-adm-techniques:b00503, C220-web-2025:03-adm-techniques:b00504, C220-web-2025:03-adm-techniques:b00505, C220-web-2025:03-adm-techniques:b00506, C220-web-2025:03-adm-techniques:b00507

<details><summary>展开本节完整英文来源</summary>

9.2. Method

It is most common that a single alternative does not exist that will
meet all stakeholders’ concerns. The TOGAF Standard supports a technique
to investigate different alternatives and to discuss these with the
stakeholders. Commonly, alternatives are defined per domain. This is
done to simplify the analysis of the different alternatives. Of course,
the alternatives per domain can be merged into on overall analysis of
the alternatives for the whole architecture.

Figure 9-1 illustrates the architecture trade-off method.



Figure 9-1: Architecture Trade-Off Method

The first part of the method uses the vision, principles, requirements, and other information to select sets of criteria fitting for different alternatives.

This second part of the method defines alternatives based on the criteria and builds understanding of each.

The third part of this method will either select one of the
alternatives, or else combine features from more than one, to create the proposed alternative. Perform the following activities in just enough detail to support that decision. The method can be used for any phase at any level of an architecture.

</details>

<a id="tag_10_02_01"></a>
## 9.2.1. Criteria

概念：评价准则来自愿景、原则、需求和利益相关者关切。

适用条件：比较灵活性、时间成本、收益期限、风格、复用和风险等。

逻辑关系：不同优缺点、依赖风险不确定性可能需新视图。

决策方法：共同确认准则和所需视点。

制品及证据：准则、优缺点和补充视图。

适用边界：本章不给统一权重或自动评分公式。

来源块：C220-web-2025:03-adm-techniques:b00508, C220-web-2025:03-adm-techniques:b00509, C220-web-2025:03-adm-techniques:b00510, C220-web-2025:03-adm-techniques:b00511, C220-web-2025:03-adm-techniques:b00512

<details><summary>展开本节完整英文来源</summary>

9.2.1. Criteria

The criteria are used for the different alternatives and are derived
from many different inputs to the architecture. Consider the influence
of architecture principles, requirements, vision, and stakeholder
concerns.

Each alternative will have distinct advantages or disadvantages that
will need to be discussed and agreed with stakeholders. Additional
viewpoints and views may be needed to allow stakeholders to explore the
alternatives and understand any dependencies, risks, and
uncertainties.

Typical examples of alternative types (based on criteria) include:

Flexible alternative Time and cost of realizing the alternative, including any transitions
and plateaus (“islands of stability”) Time period over which estimated benefits of the alternative will be
achieved Adherence to architecture styles or guidelines Solution delivery method (e.g., re-use, develop, buy) Minimal impact on business capabilities during implementation of the
alternative Minimized risk associated with the alternative and any mitigating
actions needed etc., …​

</details>

<a id="tag_10_02_02"></a>
## 9.2.2. Identify Alternatives

概念：每候选描述准则、必要视图、基线差距及全景影响。

适用条件：基线尚未定义时差距分析可先非正式。

逻辑关系：还需检查过渡状态、运行/计划项目、其他域及约束需求。

决策方法：逐候选识别依赖、实施后果和最终价值。

制品及证据：候选视图、影响评估、差距和需求/变更请求。

适用边界：非正式估计与完整影响评估的成熟度须分别标记。

来源块：C220-web-2025:03-adm-techniques:b00513, C220-web-2025:03-adm-techniques:b00514, C220-web-2025:03-adm-techniques:b00515, C220-web-2025:03-adm-techniques:b00516

<details><summary>展开本节完整英文来源</summary>

9.2.2. Identify Alternatives

Identify a set of possible alternatives using the Architecture Vision,
Principles, and Requirements.

For each alternative:

Define the overview criteria for the alternative Use the Architecture Vision, Principles, and Requirements to define the
criteria for the alternative. The criteria can be applied at different
abstraction levels and ADM phases to identify different architecture
alternatives. Describe the architecture for the alternative Create a set of necessary architecture views to reach a proper
understanding of the impact of the alternative. Add any other needed
information. Do not go into too much detail. It is important, however,
to carry out a good impact assessment and identify inter-dependencies
between alternatives and the existent landscape and have a complete
picture of the implications of the alternative implementation. Estimate gaps between the baseline and this alternative Based on current understanding of the baseline state, outline the gaps
that exist between the baseline and this alternative. If the baseline
has not yet been defined, this gap analysis will be informal. More
detail on how to do gap analysis appears in Chapter 5, Gap Analysis . Understand the impacts and trade-offs of the alternative across the Architecture Landscape: Identify the impact that the alternative will have on any existing architectures, and on any Transition Architecture within the Architecture Landscape Identify the impact the alternative will have on any running or planned implementation projects Identify constraints imposed on this alternative by any running or planned implementation projects Identify impacts on architecture in other ADM phases in this architecture project Identify Architecture Requirements/Change Requests from this architecture that will constrain other architectures Identify the final value delivered by the alternative, to what extent it covers the gap to reach the future state, and the purpose of the iteration

</details>

<a id="tag_10_02_03"></a>
## 9.2.3. Choose from Alternatives and Define in Detail

概念：共同选择或组合候选并细化至可决策程度。

适用条件：准则和候选影响已理解。

逻辑关系：应处理所有已识别视点及全景影响，正式审阅决定和资金。

决策方法：比较强弱、解决冲突，获取正式审阅与资金决定。

制品及证据：最终备选说明、权衡及正式决定。

适用边界：原文不授权分析器自动批准或拨款。

来源块：C220-web-2025:03-adm-techniques:b00517, C220-web-2025:03-adm-techniques:b00518, C220-web-2025:03-adm-techniques:b00519, C220-web-2025:03-adm-techniques:b00520

<details><summary>展开本节完整英文来源</summary>

9.2.3. Choose from Alternatives and Define in Detail

This step draws on the alternatives to select or define an alternate alternative. Use trade-off analysis to resolve conflicts between alternatives:

Understand the strengths and weaknesses of each alternative Compare the alternatives based on how well they align with the defined criteria Select the most suitable alternative or combine features from more than one of the alternatives, to define an alternate alternative in collaboration with stakeholders Assemble the alternative: Finalize the description of the alternative Ensure that all the architecture viewpoints identified have been
worked through for the alternative Ensure that the alternative is defined in enough detail to support
decision-making Resolve impacts across the Architecture Landscape Conduct formal stakeholder review to determine alternative decision
and funding

The impact analysis of the alternatives was done in just enough detail
to choose between them.

</details>

