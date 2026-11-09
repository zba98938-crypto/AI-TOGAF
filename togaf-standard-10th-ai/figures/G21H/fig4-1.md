# G21H/fig4-1 · DBRM 要素——详细视图

> 当前图示解析：[Markdown](../../architecture/diagrams/G21H/fig4-1.md) · [JSON](../../architecture/diagrams/G21H/fig4-1.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G21He.pdf`；SHA-256：`40881f73b66ae8cfabc279aba8fe3767182ac3e865823054d0aca58f6292a470`。

## 原图 · PDF 第 27 页

![英文原图](../assets/G21H/fig4-1-p0027.png)

PDF 坐标：`[48.2, 137.8, 563.8, 377.9]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
(Customer Focus
Strategic Context
1
‘Market Trends and Consumer
‘Business Influencers and
Investment and Stakeholder
Legislative and Regulatory
ramowork
Drivers
Industry Landscape and
Customers
Value Creation Framework
Digital ContexwNoeds
‘Business Motivation
Business Strategy and
‘Sralogie Goals and Objectives
Business Measures, Outcome
Corporate Governanee
f=
Customer Experience
>}
‘Business Vision and Mission
Principles
‘& Drivers
and impact
Framework and Enterprise
{_—Accitectute Strategy —_]
‘Business Services and Products
Primary Business Services
Core Business Products
Value Add Services
Digital Value
t
es ae
~
i
Ecosystem and Business Model
Operating Model
Business Capability Mode!
5
—
‘Stratogic Principles and
Business Ecosystem
‘Strategie Posture and
(customer-Facng & Marketing| Operations Management
Digital Products &
‘Business Model
Mode!
Valve Disciplines
‘Service Model
Focused
Capabilities
i
i
Service Potioiottode!
Policy and Risk
‘Organization Culture
Resource Model
‘Service Delvory Enabling
‘Shared & Suppor
Management Framework
‘and Behavior
Organizational Mode!
Capabiltes
Capabilities
Business Operating Environment
L|
Digital Operations
‘Service Experience and
‘Value Chain Model and
Busines Information
Business Process Map
‘Adors, Roles, and
Business Systoms and
Customer Joumey Maps
‘Valve Steams
Map
Organization Structure
Data Models
Digital Enablement
Digital Compotencios
L|
Digtal Principles and
‘Strategy
Digtal Governance
Digital Products and Services
‘Agi Digital Delivery Mode
Digital Phatorms
—,
```

## 概要（历史解释；局部修正见上）

把图 3-1 的十个核心要素逐一展开为 42 个子要素，并补出组内支撑箭头与组间汇流关系。

## 目的（历史解释；局部修正见上）

第 4 章逐节讨论 DBRM 各要素的构成；本图先把每个核心要素“拆开”，让读者看到每个要素由哪些子要素组成（如客户聚焦由数字语境/需求、客户体验、数字价值构成），从而把第 3 章的高层范围与第 4 章的细部说明对应起来。它也是第 6 章把 DBRM 要素映射到 TOGAF 内容框架/元模型时的子要素索引。

## 阅读顺序（历史解释；局部修正见上）

整体布局与图 3-1 相同：左侧橙色数字实践列，右侧自上而下为战略、结构、运营三条横带。区别是每个核心要素现在是一个带粗体标题的圆角容器，容器内并列 3–6 个白色子要素框。先读容器标题确认是哪个核心要素，再读容器内的白框；左侧两个容器内的白框自下而上用箭头串联，其余容器内的白框只是并列。最后沿容器外的绿色箭头读组间关系：数字实践列向右的分支、结构三组之间的双向箭头、顶部/底部两条汇流线。

## 关键含义（历史解释；局部修正见上）

- 全图共 10 个核心要素容器、42 个子要素：客户聚焦 3、数字企业 3、战略语境 5、业务动机 5、业务服务与产品 3、生态与业务模型 4、运营模式 4、业务能力模型 4、业务运营环境 6、数字使能 5。
- 客户聚焦容器内自下而上为 Digital Value→Customer Experience→Digital Context/Needs；数字企业容器内自下而上为 Digital Competencies→Digital Operations→Digital Products & Service Portfolio/Model。箭头表示下层子要素支撑/输入上层子要素，不是章节叙述顺序。
- 战略语境展开为立法与监管框架、市场趋势与消费者驱动、行业格局与竞争者、业务影响者与客户、投资与利益相关者价值创造框架五项；业务动机展开为业务愿景与使命、业务战略与原则、战略目标/目的与驱动因素、业务度量/成果与影响、公司治理框架与企业架构战略五项。
- 业务服务与产品只展开为三类：主要业务服务、核心业务产品、增值服务；这三类是业务组合的分类，不是流程步骤。
- 结构域三组：生态与业务模型（战略原则与业务模型、业务生态模型、政策与风险管理框架、组织文化与行为）、运营模式（战略姿态与价值准则、服务模型、组织模型、资源模型）、业务能力模型（面向客户与市场的营销能力、运营管理能力、服务交付使能能力、共享与支撑能力）；三组之间仍是双向箭头。
- 运营域两组：业务运营环境（服务体验与客户旅程地图、价值链模型与价值流、业务信息地图、业务流程地图、参与者/角色与组织结构、业务系统与数据模型）与数字使能（数字原则与战略、数字治理、数字产品与服务、敏捷数字交付模型、数字平台）。
- 组间大关系与图 3-1 相同：Customer Focus→战略三组；Digital Enterprise→生态与业务模型、业务运营环境、数字使能；Digital Enterprise→Customer Focus；结构三组共同支撑业务服务与产品；业务运营环境与结构三组通过底部汇流线相连。
- 与图 3-1 的差别：多出 42 个子要素和组内箭头；底部汇流线在业务运营环境顶端多了一个向下的箭头（图 3-1 没有），因此这条线在图 4-1 中读作双向连接，而不是单纯的“运营环境→结构要素”。

## 层级（历史解释；局部修正见上）

三层。第 1 层是四个域（三条横带 + 一条纵列）；第 2 层是十个核心要素容器；第 3 层是 42 个白色子要素。数字实践列内 Customer Focus 与 Digital Enterprise 并列；每个核心要素容器内的子要素并列（只有左侧两个容器用向上箭头表示支撑顺序）。核心要素与子要素是组成关系（容器包含白框），图 3-1 的组间关系在本图继续保留。

## 线条含义（历史解释；局部修正见上）

绿色实线箭头，无文字标签。四类：①数字实践列→其他要素（影响/使能）；②左侧两个容器内的自下而上箭头（下层子要素支撑上层子要素）；③结构三组之间的双向箭头（相互依赖）；④两条汇流线：顶部把三个结构组汇成一个箭头送入业务服务与产品，底部把业务运营环境与三个结构组相连，图 4-1 中底部线的四个端点都带箭头（三个向上进入结构组、一个向下进入业务运营环境），故读作双向。域带与容器边框不是关系线；容器内的白框位置表达的是并列组成，不是流程。

## 易误读点（历史解释；局部修正见上）

- 组内向上箭头容易被读成时间顺序或成熟度顺序；这里只表示下层子要素支撑上层子要素（如数字胜任力支撑数字运营），不是实施步骤。
- 客户聚焦容器内的箭头是 Digital Value→Customer Experience→Digital Context/Needs，而正文 4.2.1 的叙述顺序是数字语境/需求→客户体验→数字价值；不要据箭头重排章节，也不要把箭头读成“价值产生需求”。
- 不要把 42 个白框都当成独立的核心要素：它们只是 10 个核心要素的内部组成，核心要素只有 10 个。
- 结构三组之间的双向箭头不是流程；顶部汇流线虽然只有一个箭头进入业务服务与产品，但三个结构组都接入。
- 图 4-1 的底部汇流线在业务运营环境顶端有一个向下箭头，而图 3-1 没有；不要把两图的这条线当成完全相同的单向关系。
- 中文稿引用的 figs/g21h_fig4-1.svg 只画了 10 个框和 8 条无箭头短线，完全没有 42 个子要素与组内箭头，不能代表本图；它下面的“客户旅程/体验”等副标签也不是原图子要素。

## 元素

```json
[
  {
    "id": "digital_practices",
    "label_en": "Digital Practices",
    "label_zh": "数字实践（数字域）",
    "type": "group",
    "parent": null,
    "level": 0,
    "position": "左侧橙色竖带，纵贯三域"
  },
  {
    "id": "customer_focus",
    "label_en": "Customer Focus",
    "label_zh": "客户聚焦",
    "type": "group",
    "parent": "digital_practices",
    "level": 1,
    "position": "橙色列上方容器"
  },
  {
    "id": "cf_context",
    "label_en": "Digital Context/Needs",
    "label_zh": "数字语境/需求",
    "type": "concept",
    "parent": "customer_focus",
    "level": 2,
    "order": 1,
    "position": "客户聚焦容器内最上方白框"
  },
  {
    "id": "cf_experience",
    "label_en": "Customer Experience",
    "label_zh": "客户体验",
    "type": "concept",
    "parent": "customer_focus",
    "level": 2,
    "order": 2,
    "position": "客户聚焦容器内中间白框"
  },
  {
    "id": "cf_value",
    "label_en": "Digital Value",
    "label_zh": "数字价值",
    "type": "concept",
    "parent": "customer_focus",
    "level": 2,
    "order": 3,
    "position": "客户聚焦容器内最下方白框"
  },
  {
    "id": "digital_enterprise",
    "label_en": "Digital Enterprise",
    "label_zh": "数字企业",
    "type": "group",
    "parent": "digital_practices",
    "level": 1,
    "position": "橙色列下方容器"
  },
  {
    "id": "dent_portfolio",
    "label_en": "Digital Products & Service Portfolio/Model",
    "label_zh": "数字产品与服务组合/模型",
    "type": "concept",
    "parent": "digital_enterprise",
    "level": 2,
    "order": 1,
    "position": "数字企业容器内最上方白框"
  },
  {
    "id": "dent_operations",
    "label_en": "Digital Operations",
    "label_zh": "数字运营",
    "type": "concept",
    "parent": "digital_enterprise",
    "level": 2,
    "order": 2,
    "position": "数字企业容器内中间白框"
  },
  {
    "id": "dent_competencies",
    "label_en": "Digital Competencies",
    "label_zh": "数字胜任力",
    "type": "concept",
    "parent": "digital_enterprise",
    "level": 2,
    "order": 3,
    "position": "数字企业容器内最下方白框"
  },
  {
    "id": "strategy_domain",
    "label_en": "Strategy Domain (Why)",
    "label_zh": "战略域（为什么）",
    "type": "group",
    "parent": null,
    "level": 0,
    "position": "右侧最上方浅绿横带"
  },
  {
    "id": "strategic_context",
    "label_en": "Strategic Context",
    "label_zh": "战略语境",
    "type": "group",
    "parent": "strategy_domain",
    "level": 1,
    "order": 1,
    "position": "战略域第一组"
  },
  {
    "id": "sc_legislative",
    "label_en": "Legislative and Regulatory Framework",
    "label_zh": "立法与监管框架",
    "type": "concept",
    "parent": "strategic_context",
    "level": 2,
    "order": 1
  },
  {
    "id": "sc_market",
    "label_en": "Market Trends and Consumer Drivers",
    "label_zh": "市场趋势与消费者驱动",
    "type": "concept",
    "parent": "strategic_context",
    "level": 2,
    "order": 2
  },
  {
    "id": "sc_industry",
    "label_en": "Industry Landscape and Competitors",
    "label_zh": "行业格局与竞争者",
    "type": "concept",
    "parent": "strategic_context",
    "level": 2,
    "order": 3
  },
  {
    "id": "sc_influencers",
    "label_en": "Business Influencers and Customers",
    "label_zh": "业务影响者与客户",
    "type": "concept",
    "parent": "strategic_context",
    "level": 2,
    "order": 4
  },
  {
    "id": "sc_investment",
    "label_en": "Investment and Stakeholder Value Creation Framework",
    "label_zh": "投资与利益相关者价值创造框架",
    "type": "concept",
    "parent": "strategic_context",
    "level": 2,
    "order": 5
  },
  {
    "id": "business_motivation",
    "label_en": "Business Motivation",
    "label_zh": "业务动机",
    "type": "group",
    "parent": "strategy_domain",
    "level": 1,
    "order": 2,
    "position": "战略域第二组"
  },
  {
    "id": "bm_vision",
    "label_en": "Business Vision and Mission",
    "label_zh": "业务愿景与使命",
    "type": "concept",
    "parent": "business_motivation",
    "level": 2,
    "order": 1
  },
  {
    "id": "bm_strategy",
    "label_en": "Business Strategy and Principles",
    "label_zh": "业务战略与原则",
    "type": "concept",
    "parent": "business_motivation",
    "level": 2,
    "order": 2
  },
  {
    "id": "bm_goals",
    "label_en": "Strategic Goals and Objectives & Drivers",
    "label_zh": "战略目标、目的与驱动因素",
    "type": "concept",
    "parent": "business_motivation",
    "level": 2,
    "order": 3
  },
  {
    "id": "bm_measures",
    "label_en": "Business Measures, Outcome and Impact",
    "label_zh": "业务度量、成果与影响",
    "type": "concept",
    "parent": "business_motivation",
    "level": 2,
    "order": 4
  },
  {
    "id": "bm_governance",
    "label_en": "Corporate Governance Framework and Enterprise Architecture Strategy",
    "label_zh": "公司治理框架与企业架构战略",
    "type": "concept",
    "parent": "business_motivation",
    "level": 2,
    "order": 5
  },
  {
    "id": "business_services",
    "label_en": "Business Services and Products",
    "label_zh": "业务服务与产品",
    "type": "group",
    "parent": "strategy_domain",
    "level": 1,
    "order": 3,
    "position": "战略域第三组"
  },
  {
    "id": "bsp_primary",
    "label_en": "Primary Business Services",
    "label_zh": "主要业务服务",
    "type": "concept",
    "parent": "business_services",
    "level": 2,
    "order": 1
  },
  {
    "id": "bsp_products",
    "label_en": "Core Business Products",
    "label_zh": "核心业务产品",
    "type": "concept",
    "parent": "business_services",
    "level": 2,
    "order": 2
  },
  {
    "id": "bsp_valueadd",
    "label_en": "Value Add Services",
    "label_zh": "增值服务",
    "type": "concept",
    "parent": "business_services",
    "level": 2,
    "order": 3
  },
  {
    "id": "structural_domain",
    "label_en": "Structural Domain (What)",
    "label_zh": "结构域（是什么）",
    "type": "group",
    "parent": null,
    "level": 0,
    "position": "右侧中部蓝灰横带"
  },
  {
    "id": "ecosystem_model",
    "label_en": "Ecosystem and Business Model",
    "label_zh": "生态与业务模型",
    "type": "group",
    "parent": "structural_domain",
    "level": 1,
    "order": 1,
    "position": "结构域左侧容器"
  },
  {
    "id": "eb_principles",
    "label_en": "Strategic Principles and Business Model",
    "label_zh": "战略原则与业务模型",
    "type": "concept",
    "parent": "ecosystem_model",
    "level": 2,
    "order": 1
  },
  {
    "id": "eb_ecosystem",
    "label_en": "Business Ecosystem Model",
    "label_zh": "业务生态模型",
    "type": "concept",
    "parent": "ecosystem_model",
    "level": 2,
    "order": 2
  },
  {
    "id": "eb_policy",
    "label_en": "Policy and Risk Management Framework",
    "label_zh": "政策与风险管理框架",
    "type": "concept",
    "parent": "ecosystem_model",
    "level": 2,
    "order": 3
  },
  {
    "id": "eb_culture",
    "label_en": "Organization Culture and Behavior",
    "label_zh": "组织文化与行为",
    "type": "concept",
    "parent": "ecosystem_model",
    "level": 2,
    "order": 4
  },
  {
    "id": "operating_model",
    "label_en": "Operating Model",
    "label_zh": "运营模式",
    "type": "group",
    "parent": "structural_domain",
    "level": 1,
    "order": 2,
    "position": "结构域中间容器"
  },
  {
    "id": "om_posture",
    "label_en": "Strategic Posture and Value Disciplines",
    "label_zh": "战略姿态与价值准则",
    "type": "concept",
    "parent": "operating_model",
    "level": 2,
    "order": 1
  },
  {
    "id": "om_service",
    "label_en": "Service Model",
    "label_zh": "服务模型",
    "type": "concept",
    "parent": "operating_model",
    "level": 2,
    "order": 2
  },
  {
    "id": "om_org",
    "label_en": "Organizational Model",
    "label_zh": "组织模型",
    "type": "concept",
    "parent": "operating_model",
    "level": 2,
    "order": 3
  },
  {
    "id": "om_resource",
    "label_en": "Resource Model",
    "label_zh": "资源模型",
    "type": "concept",
    "parent": "operating_model",
    "level": 2,
    "order": 4
  },
  {
    "id": "capability_model",
    "label_en": "Business Capability Model",
    "label_zh": "业务能力模型",
    "type": "group",
    "parent": "structural_domain",
    "level": 1,
    "order": 3,
    "position": "结构域右侧容器"
  },
  {
    "id": "bcm_customer",
    "label_en": "Customer-Facing & Marketing-Focused Capabilities",
    "label_zh": "面向客户与市场的营销能力",
    "type": "concept",
    "parent": "capability_model",
    "level": 2,
    "order": 1
  },
  {
    "id": "bcm_operations",
    "label_en": "Operations Management Capabilities",
    "label_zh": "运营管理能力",
    "type": "concept",
    "parent": "capability_model",
    "level": 2,
    "order": 2,
    "description_zh": "原图作 Operations Management Capabilities；中文稿表 6-2 也作“运营管理能力”，但 4.4.3 节对应条目写作“服务交付管理能力（Service Delivery Management Capabilities）”，稿件内部术语不一致。"
  },
  {
    "id": "bcm_delivery",
    "label_en": "Service Delivery Enabling Capabilities",
    "label_zh": "服务交付使能能力",
    "type": "concept",
    "parent": "capability_model",
    "level": 2,
    "order": 3
  },
  {
    "id": "bcm_shared",
    "label_en": "Shared & Support Capabilities",
    "label_zh": "共享与支撑能力",
    "type": "concept",
    "parent": "capability_model",
    "level": 2,
    "order": 4
  },
  {
    "id": "operational_domain",
    "label_en": "Operational Domain (How)",
    "label_zh": "运营域（怎么做）",
    "type": "group",
    "parent": null,
    "level": 0,
    "position": "右侧最下方淡黄横带"
  },
  {
    "id": "business_operating_env",
    "label_en": "Business Operating Environment",
    "label_zh": "业务运营环境",
    "type": "group",
    "parent": "operational_domain",
    "level": 1,
    "order": 1,
    "position": "运营域上方容器"
  },
  {
    "id": "boe_experience",
    "label_en": "Service Experience and Customer Journey Maps",
    "label_zh": "服务体验与客户旅程地图",
    "type": "concept",
    "parent": "business_operating_env",
    "level": 2,
    "order": 1
  },
  {
    "id": "boe_valuechain",
    "label_en": "Value Chain Model and Value Streams",
    "label_zh": "价值链模型与价值流",
    "type": "concept",
    "parent": "business_operating_env",
    "level": 2,
    "order": 2
  },
  {
    "id": "boe_information",
    "label_en": "Business Information Map",
    "label_zh": "业务信息地图",
    "type": "concept",
    "parent": "business_operating_env",
    "level": 2,
    "order": 3
  },
  {
    "id": "boe_process",
    "label_en": "Business Process Map",
    "label_zh": "业务流程地图",
    "type": "concept",
    "parent": "business_operating_env",
    "level": 2,
    "order": 4
  },
  {
    "id": "boe_actors",
    "label_en": "Actors, Roles, and Organization Structure",
    "label_zh": "参与者、角色与组织结构",
    "type": "concept",
    "parent": "business_operating_env",
    "level": 2,
    "order": 5
  },
  {
    "id": "boe_systems",
    "label_en": "Business Systems and Data Models",
    "label_zh": "业务系统与数据模型",
    "type": "concept",
    "parent": "business_operating_env",
    "level": 2,
    "order": 6
  },
  {
    "id": "digital_enablement",
    "label_en": "Digital Enablement",
    "label_zh": "数字使能",
    "type": "group",
    "parent": "operational_domain",
    "level": 1,
    "order": 2,
    "position": "运营域下方容器"
  },
  {
    "id": "den_principles",
    "label_en": "Digital Principles and Strategy",
    "label_zh": "数字原则与战略",
    "type": "concept",
    "parent": "digital_enablement",
    "level": 2,
    "order": 1
  },
  {
    "id": "den_governance",
    "label_en": "Digital Governance",
    "label_zh": "数字治理",
    "type": "concept",
    "parent": "digital_enablement",
    "level": 2,
    "order": 2
  },
  {
    "id": "den_products",
    "label_en": "Digital Products and Services",
    "label_zh": "数字产品与服务",
    "type": "concept",
    "parent": "digital_enablement",
    "level": 2,
    "order": 3
  },
  {
    "id": "den_agile",
    "label_en": "Agile Digital Delivery Model",
    "label_zh": "敏捷数字交付模型",
    "type": "concept",
    "parent": "digital_enablement",
    "level": 2,
    "order": 4
  },
  {
    "id": "den_platforms",
    "label_en": "Digital Platforms",
    "label_zh": "数字平台",
    "type": "concept",
    "parent": "digital_enablement",
    "level": 2,
    "order": 5
  }
]
```

## 关系

```json
[
  {
    "id": "r_cf_value_exp",
    "from": "cf_value",
    "to": "cf_experience",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "客户聚焦容器内自下而上的箭头，从 Digital Value 顶边指向 Customer Experience 底边。"
  },
  {
    "id": "r_cf_exp_ctx",
    "from": "cf_experience",
    "to": "cf_context",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "客户聚焦容器内自下而上的箭头，从 Customer Experience 顶边指向 Digital Context/Needs 底边。"
  },
  {
    "id": "r_de_comp_ops",
    "from": "dent_competencies",
    "to": "dent_operations",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "数字企业容器内自下而上的箭头，从 Digital Competencies 顶边指向 Digital Operations 底边。"
  },
  {
    "id": "r_de_ops_port",
    "from": "dent_operations",
    "to": "dent_portfolio",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "数字企业容器内自下而上的箭头，从 Digital Operations 顶边指向 Digital Products & Service Portfolio/Model 底边。"
  },
  {
    "id": "r_de_cf",
    "from": "digital_enterprise",
    "to": "customer_focus",
    "type": "influence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "两个容器之间的向上箭头，从 Digital Enterprise 容器顶边指向 Customer Focus 容器底边。"
  },
  {
    "id": "r_cf_sc",
    "from": "customer_focus",
    "to": "strategic_context",
    "type": "influence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "Customer Focus 容器右缘引出分支，箭头指向 Strategic Context 组左边缘。"
  },
  {
    "id": "r_cf_bm",
    "from": "customer_focus",
    "to": "business_motivation",
    "type": "influence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "同一分支向下，箭头指向 Business Motivation 组左边缘。"
  },
  {
    "id": "r_cf_bsp",
    "from": "customer_focus",
    "to": "business_services",
    "type": "influence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "同一分支再向下，箭头指向 Business Services and Products 组左边缘。"
  },
  {
    "id": "r_de_eb",
    "from": "digital_enterprise",
    "to": "ecosystem_model",
    "type": "influence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "Digital Enterprise 容器右缘（标题高度）引出的短箭头，指向 Ecosystem and Business Model 组左边缘。"
  },
  {
    "id": "r_de_boe",
    "from": "digital_enterprise",
    "to": "business_operating_env",
    "type": "influence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "Digital Enterprise 容器右缘引出分支，箭头指向 Business Operating Environment 组左边缘。"
  },
  {
    "id": "r_de_den",
    "from": "digital_enterprise",
    "to": "digital_enablement",
    "type": "influence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "同一分支向下，箭头指向 Digital Enablement 组左边缘。"
  },
  {
    "id": "r_eb_om",
    "from": "ecosystem_model",
    "to": "operating_model",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "both",
    "description_zh": "两个结构组之间的双向箭头。"
  },
  {
    "id": "r_om_bcm",
    "from": "operating_model",
    "to": "capability_model",
    "type": "association",
    "explicit": true,
    "line": "solid",
    "arrow": "both",
    "description_zh": "两个结构组之间的双向箭头。"
  },
  {
    "id": "r_eb_bsp",
    "from": "ecosystem_model",
    "to": "business_services",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "顶部汇流线左端从 Ecosystem 组顶边引出，汇入后只有一个箭头向上进入 Business Services and Products。"
  },
  {
    "id": "r_om_bsp",
    "from": "operating_model",
    "to": "business_services",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "顶部汇流线中段从 Operating Model 组顶边引出，合流后向上进入 Business Services and Products。"
  },
  {
    "id": "r_bcm_bsp",
    "from": "capability_model",
    "to": "business_services",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "顶部汇流线右端从 Business Capability Model 组顶边引出，向左汇入同一箭头。"
  },
  {
    "id": "r_boe_eb",
    "from": "business_operating_env",
    "to": "ecosystem_model",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "both",
    "description_zh": "底部汇流线：左支向上箭头进入 Ecosystem 组底边，同时干线在 Business Operating Environment 顶端有一个向下箭头，故为双向连接。"
  },
  {
    "id": "r_boe_om",
    "from": "business_operating_env",
    "to": "operating_model",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "both",
    "description_zh": "底部汇流线中支向上箭头进入 Operating Model 组底边；干线另一端向下进入 Business Operating Environment。"
  },
  {
    "id": "r_boe_bcm",
    "from": "business_operating_env",
    "to": "capability_model",
    "type": "serving",
    "explicit": true,
    "line": "solid",
    "arrow": "both",
    "description_zh": "底部汇流线右支向上箭头进入 Business Capability Model 组底边；干线另一端向下进入 Business Operating Environment。"
  }
]
```

## 转录表格

```json
[
  {
    "id": "t_sub_elements",
    "title_zh": "十个核心要素的子要素逐组转录（按图内从左到右、从上到下）",
    "columns": [
      "域",
      "核心要素",
      "子要素"
    ],
    "rows": [
      [
        "数字",
        "客户聚焦 Customer Focus",
        "数字语境/需求 Digital Context/Needs；客户体验 Customer Experience；数字价值 Digital Value"
      ],
      [
        "数字",
        "数字企业 Digital Enterprise",
        "数字产品与服务组合/模型 Digital Products & Service Portfolio/Model；数字运营 Digital Operations；数字胜任力 Digital Competencies"
      ],
      [
        "战略",
        "战略语境 Strategic Context",
        "立法与监管框架 Legislative and Regulatory Framework；市场趋势与消费者驱动 Market Trends and Consumer Drivers；行业格局与竞争者 Industry Landscape and Competitors；业务影响者与客户 Business Influencers and Customers；投资与利益相关者价值创造框架 Investment and Stakeholder Value Creation Framework"
      ],
      [
        "战略",
        "业务动机 Business Motivation",
        "业务愿景与使命 Business Vision and Mission；业务战略与原则 Business Strategy and Principles；战略目标、目的与驱动因素 Strategic Goals and Objectives & Drivers；业务度量、成果与影响 Business Measures, Outcome and Impact；公司治理框架与企业架构战略 Corporate Governance Framework and Enterprise Architecture Strategy"
      ],
      [
        "战略",
        "业务服务与产品 Business Services and Products",
        "主要业务服务 Primary Business Services；核心业务产品 Core Business Products；增值服务 Value Add Services"
      ],
      [
        "结构",
        "生态与业务模型 Ecosystem and Business Model",
        "战略原则与业务模型 Strategic Principles and Business Model；业务生态模型 Business Ecosystem Model；政策与风险管理框架 Policy and Risk Management Framework；组织文化与行为 Organization Culture and Behavior"
      ],
      [
        "结构",
        "运营模式 Operating Model",
        "战略姿态与价值准则 Strategic Posture and Value Disciplines；服务模型 Service Model；组织模型 Organizational Model；资源模型 Resource Model"
      ],
      [
        "结构",
        "业务能力模型 Business Capability Model",
        "面向客户与市场的营销能力 Customer-Facing & Marketing-Focused Capabilities；运营管理能力 Operations Management Capabilities；服务交付使能能力 Service Delivery Enabling Capabilities；共享与支撑能力 Shared & Support Capabilities"
      ],
      [
        "运营",
        "业务运营环境 Business Operating Environment",
        "服务体验与客户旅程地图 Service Experience and Customer Journey Maps；价值链模型与价值流 Value Chain Model and Value Streams；业务信息地图 Business Information Map；业务流程地图 Business Process Map；参与者、角色与组织结构 Actors, Roles, and Organization Structure；业务系统与数据模型 Business Systems and Data Models"
      ],
      [
        "运营",
        "数字使能 Digital Enablement",
        "数字原则与战略 Digital Principles and Strategy；数字治理 Digital Governance；数字产品与服务 Digital Products and Services；敏捷数字交付模型 Agile Digital Delivery Model；数字平台 Digital Platforms"
      ]
    ],
    "notes_zh": "每行一个核心要素容器；子要素顺序即图内从左到右/从上到下。业务能力模型的第二项原图为 Operations Management Capabilities，中文稿正文对应条目写作“服务交付管理能力（Service Delivery Management Capabilities）”，二者术语不一致，表中按原图直译并在元素说明中注明。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "橙色竖带 + 竖排“Digital Practices”",
    "meaning_zh": "数字实践/数字域，纵贯三个域",
    "explicit": false
  },
  {
    "symbol": "浅绿横带 + 左侧竖排“Strategy Domain (Why)”",
    "meaning_zh": "战略域（为什么）",
    "explicit": false
  },
  {
    "symbol": "蓝灰横带 + 左侧竖排“Structural Domain (What)”",
    "meaning_zh": "结构域（是什么）",
    "explicit": false
  },
  {
    "symbol": "淡黄横带 + 左侧竖排“Operational Domain (How)”",
    "meaning_zh": "运营域（怎么做）",
    "explicit": false
  },
  {
    "symbol": "带粗体标题的圆角容器",
    "meaning_zh": "一个核心要素；容器内的白框是它的子要素",
    "explicit": false
  },
  {
    "symbol": "容器内白色小框",
    "meaning_zh": "子要素；并列放置表示同属一个核心要素，没有顺序",
    "explicit": false
  },
  {
    "symbol": "绿色实线箭头",
    "meaning_zh": "要素/子要素之间的支撑或影响，箭头指向被支撑/被影响的一方",
    "explicit": false
  },
  {
    "symbol": "双向绿色箭头",
    "meaning_zh": "结构三组两两相互依赖",
    "explicit": false
  },
  {
    "symbol": "水平汇流线 + 箭头",
    "meaning_zh": "多个要素接入同一条线后合流；底部线四个端点都带箭头，表示双向连接",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "与图 3-1 相同的四域布局：左侧橙色数字实践列（上 Customer Focus、下 Digital Enterprise），右侧自上而下三条域带（战略 3 组、结构 3 组并排、运营 2 组）。每个核心要素是带标题的圆角容器，内部为 3–6 个白色子要素框；战略域 3 组纵向堆叠，结构域 3 组横向并排，运营域 2 组纵向堆叠。"
}
```

## 相关图

```json
[
  {
    "target": "G21H/fig3-1",
    "relation": "detail_of",
    "note_zh": "本图是图 3-1 高层视图的展开：十个核心要素不变，新增 42 个子要素、组内向上箭头与更完整的汇流线。"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "业务能力模型第二项原图为 Operations Management Capabilities（运营管理能力），中文稿表 6-2 同作“运营管理能力”，但 4.4.3 节对应条目为“服务交付管理能力（Service Delivery Management Capabilities）”；label_zh 按原图与表 6-2 直译，并保留这一差异说明。",
    "底部汇流线在业务运营环境顶端有一个向下箭头，同时三个结构组底边各有一个向上箭头；本分析读作双向连接，但图中没有箭头标签，也可能只是绘图时在每个端点都加了箭头。",
    "数字实践列右侧干线同时服务 Customer Focus、Digital Enterprise 与生态/业务模型分支，图中未标连接点；本分析按分支高度把生态/业务模型归到 Digital Enterprise。",
    "客户聚焦容器内箭头方向（数字价值→客户体验→数字语境/需求）与正文 4.2.1 的叙述顺序相反，图义按箭头本身记录，未据此推断因果。"
  ],
  "analyzed_from": [
    "英文 PDF 第 27 页 figure 截图（220 dpi 与 600 dpi 局部放大）",
    "英文 PDF 第 27 页正文",
    "中文稿 G21He_TOGAF数字业务参考模型.md 第 258–505 行（4.1–4.5 节）",
    "figs/g21h_fig4-1.svg 源码与文本内容"
  ],
  "date": "2026-10-31"
}
```

## 结构校验

```json
{
  "graph_integrity_issues": [],
  "location_available": true,
  "caption_page_match": true,
  "visual_review_scope": "not-reverified-this-build",
  "all_source_pages_valid": true
}
```
