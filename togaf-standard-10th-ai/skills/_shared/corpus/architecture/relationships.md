# 架构关系与层级语义

严格区分组成、类型特化、分类、实现、架构约束、信息流和组织汇报；图形嵌套、位置、颜色及线条样式本身不足以新增人员汇报关系。

仅在来源明确说明时记录基数。null表示未在所引证据中规定，不表示不存在、零或无限。

关系是依据正文证据建立的语义标准化分析；箭头按各关系的说明解释，并非把所有关系视作同一种流程。

## 关系类型

| 类型 | 含义 |
|---|---|
| `specialization` · 类型特化 | 源概念是目标概念的一种具体类型；不表示人事层级。 |
| `part_of` · 组成 | 源对象构成目标模型或复合对象的一部分；不推断排他拥有。 |
| `enables` · 使能 | 源对象为目标活动或能力提供必要作用；不同于组成或因果充分条件。 |
| `realization` · 实现或具体化 | 源对象在明确上下文中实现或具体化目标的抽象意义。 |
| `instantiates` · 实例化 | 源对象是目标类型在特定上下文中的具体实例；不是类型特化、子能力或人员汇报。 |
| `governance` · 治理 | 源对象对目标承担所注明的决策、过程或符合性责任；权力不能扩大。 |
| `flow` · 信息输入或反馈 | 所引用证据中的信息向目标传递；不默认是运行时数据流或固定执行顺序。 |
| `mapping` · 关联映射 | 两个视角中的对象有关联；不表示等价、包含或未声明的基数。 |
| `depends_on` · 依赖 | 源对象按所注明语义需要目标；不推断完整因果网络。 |
| `classification` · 分类 | 按指定维度分类或分组；不等同父子分解或人事汇报。 |
| `constraint` · 约束 | 源架构、目标或政策对目标工作施加已注明约束；不表示人员直属关系。 |

## 关系明细

<a id="r001"></a>

### R001 · 构成价值流

[价值流阶段](concepts.md#value_stream_stage) → `part_of` → [价值流](concepts.md#value_stream)

阶段是价值流的分解组成，可有顺序或并行安排。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：不能把阶段当作业务能力或子能力。

- [G178 PDF 16](../documents/G178.md#page-16)；书页 6，证据 `G178:A04`：sequential and/or parallel actions
  章节：2.2. Decomposing a Value Stream；正文块：`G178:p0016:b002`、`G178:p0016:b003`、`G178:p0016:b004`。

<a id="r002"></a>

### R002 · 使能阶段

[业务能力](concepts.md#business_capability) → `enables` → [价值流阶段](concepts.md#value_stream_stage)

能力提供阶段创造价值所需的业务作用。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：能力框放在阶段下方不表示阶段包含能力；未声明固定基数。

- [G178 PDF 16](../documents/G178.md#page-16)；书页 6，证据 `G178:A06`：required to enable each value stream stage
  章节：2.3. Mapping Capabilities to Value Stream Stages；正文块：`G178:p0016:b024`、`G178:p0016:b025`、`G178:p0016:b026`、`G178:p0016:b027`。
- [G233 PDF 35](../documents/G233.md#page-35)；书页 21，证据 `G233:A03`：required to enable each value stream stage
  章节：6.3. Mapping Business Capabilities to Value Stream Stages；正文块：`G233:p0035:b003`、`G233:p0035:b004`、`G233:p0035:b005`、`G233:p0035:b006`。

<a id="r003"></a>

### R003 · 映射实现过程

[价值流阶段](concepts.md#value_stream_stage) → `mapping` → [业务过程](concepts.md#business_process)

阶段可映射一个或多个业务过程。

关系方向语义：`association`；基数：{"source_to_target": "one-or-more", "target_to_source": null, "evidence_text": "one or more business processes"}。

不可推断：不能强制每个阶段仅有一个过程，也没有证据确定反向最小基数。

- [G178 PDF 13](../documents/G178.md#page-13)；书页 3，证据 `G178:A01`：one or more business processes
  章节：1.4. Relationship of Value Streams to Other Business Architecture Concepts；正文块：`G178:p0013:b002`、`G178:p0013:b003`、`G178:p0013:b004`、`G178:p0013:b005`、`G178:p0013:b006`、`G178:p0013:b007`、`G178:p0013:b008`、`G178:p0013:b009`。

<a id="r004"></a>

### R004 · 说明阶段价值

[价值流阶段](concepts.md#value_stream_stage) → `mapping` → [价值项](concepts.md#value_item)

阶段说明包含价值项及进入、退出条件。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：不由字段清单推断价值项唯一或必为金额。

- [G178 PDF 16](../documents/G178.md#page-16)；书页 6，证据 `G178:A05`：Entrance Criteria
  章节：2.2. Decomposing a Value Stream；正文块：`G178:p0016:b011`、`G178:p0016:b012`。

<a id="r005"></a>

### R005 · 共同创造或交付能力

[组织单元](concepts.md#organization_unit) → `mapping` → [业务能力](concepts.md#business_capability)

组织单元与能力之间是多对多映射。

关系方向语义：`association`；基数：{"source_to_target": "many", "target_to_source": "many", "minimums_specified": false, "evidence_text": "many-to-many"}。

不可推断：不能用组织树复制能力分解，也未声明零或一的下界。

- [G206 PDF 19](../documents/G206.md#page-19)；书页 9，证据 `G206:A05`：with a many-to-many mapping
  章节：5. The Relationship to Business Capabilities, Value Streams, and Information Maps；正文块：`G206:p0019:b002`、`G206:p0019:b003`、`G206:p0019:b004`、`G206:p0019:b005`、`G206:p0019:b006`、`G206:p0019:b007`、`G206:p0019:b008`。
- [G211 PDF 16](../documents/G211.md#page-16)；书页 6，证据 `G211:A04`：multiple business units
  章节：3.1.1. Organizational Structure；正文块：`G211:p0016:b011`、`G211:p0016:b012`、`G211:p0016:b013`、`G211:p0016:b014`、`G211:p0016:b015`。

<a id="r006"></a>

### R006 · 实例化能力类型

[业务能力实例](concepts.md#capability_instance) → `instantiates` → [业务能力](concepts.md#business_capability)

实例表达能力类型在特定组织或价值流位置的实际使用。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：不因实例不同而重复创建能力类型；这不是软件继承关系。

- [G233 PDF 32](../documents/G233.md#page-32)；书页 18，证据 `G233:A02`：business capability instance
  章节：6. Business Capabilities；正文块：`G233:p0032:b006`、`G233:p0032:b007`、`G233:p0032:b008`、`G233:p0032:b009`、`G233:p0032:b010`、`G233:p0032:b011`。
- [G233 PDF 36](../documents/G233.md#page-36)；书页 22，证据 `G233:A04`：otherwise conflict or create duplicates
  章节：6.4. Business Capability Instances；正文块：`G233:p0036:b002`、`G233:p0036:b003`、`G233:p0036:b004`。

<a id="r007"></a>

### R007 · 使能实际阶段

[业务能力实例](concepts.md#capability_instance) → `enables` → [价值流阶段](concepts.md#value_stream_stage)

具体使用位置把能力与阶段价值及绩效评价连接。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：不能用能力类型的抽象存在证明实例已满足阶段绩效。

- [G233 PDF 35](../documents/G233.md#page-35)；书页 21，证据 `G233:A03`：required to enable each value stream stage
  章节：6.3. Mapping Business Capabilities to Value Stream Stages；正文块：`G233:p0035:b003`、`G233:p0035:b004`、`G233:p0035:b005`、`G233:p0035:b006`。
- [G233 PDF 36](../documents/G233.md#page-36)；书页 22，证据 `G233:A04`：otherwise conflict or create duplicates
  章节：6.4. Business Capability Instances；正文块：`G233:p0036:b002`、`G233:p0036:b003`、`G233:p0036:b004`。

<a id="r008"></a>

### R008 · 定位能力使用

[业务能力实例](concepts.md#capability_instance) → `mapping` → [组织单元](concepts.md#organization_unit)

能力实例连接组织位置及实现资源差距。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：不得从该关系自动推导人员汇报、固定基数、时间顺序或项目事实。

- [G233 PDF 36](../documents/G233.md#page-36)；书页 22，证据 `G233:A04`：otherwise conflict or create duplicates
  章节：6.4. Business Capability Instances；正文块：`G233:p0036:b002`、`G233:p0036:b003`、`G233:p0036:b004`。
- [G233 PDF 36](../documents/G233.md#page-36)；书页 22，证据 `G233:A05`：actors, stakeholders, resources, applications, or processes
  章节：6.4. Business Capability Instances；正文块：`G233:p0036:b005`、`G233:p0036:b006`、`G233:p0036:b007`、`G233:p0036:b008`。

<a id="r009"></a>

### R009 · 将能力分类或分组

[能力组或层](concepts.md#capability_group) → `classification` → [业务能力](concepts.md#business_capability)

能力层、类别或组为理解和管理提供分类。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：分类分层不表示父子能力分解或人员汇报。

- [G211 PDF 20](../documents/G211.md#page-20)；书页 10，证据 `G211:A05`：classifying, grouping, and aligning
  章节：3.2.1. Business Capability Stratification；正文块：`G211:p0020:b007`、`G211:p0020:b008`、`G211:p0020:b009`、`G211:p0020:b010`。
- [G249 PDF 21](../documents/G249.md#page-21)；书页 11，证据 `G249:A05`：coherent grouping of capabilities
  章节：4.3. Segment Architect (Business and Technical)；正文块：`G249:p0021:b010`、`G249:p0021:b011`、`G249:p0021:b012`、`G249:p0021:b013`、`G249:p0021:b014`、`G249:p0021:b015`、`G249:p0021:b016`。

<a id="r010"></a>

### R010 · 展开更细能力

[能力分解](concepts.md#capability_decomposition) → `mapping` → [业务能力](concepts.md#business_capability)

分解方法逐级展开能力；实际父子边要从具体模型提取。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：这里是方法与对象关联，不生成所有能力之间的自包含边。

- [G211 PDF 21](../documents/G211.md#page-21)；书页 11，证据 `G211:A06`：decomposing each top-level
  章节：3.2.2. Leveling；正文块：`G211:p0021:b002`、`G211:p0021:b003`、`G211:p0021:b004`、`G211:p0021:b005`。

<a id="r011"></a>

### R011 · 参与能力实现

[业务过程](concepts.md#business_process) → `enables` → [业务能力](concepts.md#business_capability)

过程与角色、信息和工具一起使能能力。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：一个过程不是能力本身，也不足以单独证明全部能力就绪。

- [G211 PDF 13](../documents/G211.md#page-13)；书页 3，证据 `G211:A02`：roles, processes, information, and tools
  章节：2.2. Elements to Implement Business Capabilities；正文块：`G211:p0013:b014`、`G211:p0013:b015`、`G211:p0013:b016`、`G211:p0013:b017`、`G211:p0013:b018`。

<a id="r012"></a>

### R012 · 提供实现职责

[角色](concepts.md#role) → `enables` → [业务能力](concepts.md#business_capability)

角色是能力实现所需的使能要素之一。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：不将能力分配自动转成人员任命。

- [G211 PDF 13](../documents/G211.md#page-13)；书页 3，证据 `G211:A02`：roles, processes, information, and tools
  章节：2.2. Elements to Implement Business Capabilities；正文块：`G211:p0013:b014`、`G211:p0013:b015`、`G211:p0013:b016`、`G211:p0013:b017`、`G211:p0013:b018`。

<a id="r013"></a>

### R013 · 提供业务信息

[信息概念](concepts.md#information_concept) → `enables` → [业务能力](concepts.md#business_capability)

信息语义与能力使用关联。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：不能因关联就推导系统读写权限。

- [G211 PDF 13](../documents/G211.md#page-13)；书页 3，证据 `G211:A02`：roles, processes, information, and tools
  章节：2.2. Elements to Implement Business Capabilities；正文块：`G211:p0013:b014`、`G211:p0013:b015`、`G211:p0013:b016`、`G211:p0013:b017`、`G211:p0013:b018`。
- [G190 PDF 21](../documents/G190.md#page-21)；书页 11，证据 `G190:A06`：joined with business capabilities, value streams, and organization maps
  章节：8. Conclusion；正文块：`G190:p0021:b002`、`G190:p0021:b003`、`G190:p0021:b004`、`G190:p0021:b005`、`G190:p0021:b006`、`G190:p0021:b007`、`G190:p0021:b008`。

<a id="r014"></a>

### R014 · 提供价值逻辑输入

[业务模型](concepts.md#business_model) → `flow` → [业务架构](concepts.md#business_architecture)

业务模型作为业务架构输入，被展开为能力、价值流、组织和信息。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：这表示架构信息输入，不是系统运行数据流。

- [G18A PDF 17](../documents/G18A.md#page-17)；书页 7，证据 `G18A:A03`：business capabilities, value streams, organizational structure and information objects
  章节：4. The Relationship between Business Models and Business Architecture；正文块：`G18A:p0017:b017`、`G18A:p0017:b018`、`G18A:p0017:b019`、`G18A:p0017:b020`、`G18A:p0017:b021`、`G18A:p0017:b022`、`G18A:p0017:b023`。
- [G18A PDF 19](../documents/G18A.md#page-19)；书页 9，证据 `G18A:A05`：key input into Phase B
  章节：5. Using Business Models in the TOGAF Standard；正文块：`G18A:p0019:b009`、`G18A:p0019:b010`、`G18A:p0019:b011`、`G18A:p0019:b012`、`G18A:p0019:b013`、`G18A:p0019:b014`。

<a id="r015"></a>

### R015 · 反馈缺口与假设

[业务架构](concepts.md#business_architecture) → `flow` → [业务模型](concepts.md#business_model)

业务架构发现的问题反馈修订业务模型。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：反馈关系不表示必须每次重做全部模型。

- [G18A PDF 17](../documents/G18A.md#page-17)；书页 7，证据 `G18A:A04`：loop the discussion back
  章节：4. The Relationship between Business Models and Business Architecture；正文块：`G18A:p0017:b017`、`G18A:p0017:b018`、`G18A:p0017:b019`、`G18A:p0017:b020`、`G18A:p0017:b021`、`G18A:p0017:b022`、`G18A:p0017:b023`。

<a id="r016"></a>

### R016 · 采用能力视角

[业务架构](concepts.md#business_architecture) → `mapping` → [业务能力](concepts.md#business_capability)

业务能力是业务架构的互补视角。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：不要把视角关联解释为所有能力均为一个文档容器的物理组成。

- [G18A PDF 17](../documents/G18A.md#page-17)；书页 7，证据 `G18A:A03`：business capabilities, value streams, organizational structure and information objects
  章节：4. The Relationship between Business Models and Business Architecture；正文块：`G18A:p0017:b017`、`G18A:p0017:b018`、`G18A:p0017:b019`、`G18A:p0017:b020`、`G18A:p0017:b021`、`G18A:p0017:b022`、`G18A:p0017:b023`。
- [G21H PDF 18](../documents/G21H.md#page-18)；书页 4，证据 `G21H:A01`：holistic, multi-dimensional business views
  章节：2.3. Business Architecture；正文块：`G21H:p0018:b014`、`G21H:p0018:b015`、`G21H:p0018:b016`。

<a id="r017"></a>

### R017 · 采用价值视角

[业务架构](concepts.md#business_architecture) → `mapping` → [价值流](concepts.md#value_stream)

价值流是业务架构的互补视角。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：不得从该关系自动推导人员汇报、固定基数、时间顺序或项目事实。

- [G18A PDF 17](../documents/G18A.md#page-17)；书页 7，证据 `G18A:A03`：business capabilities, value streams, organizational structure and information objects
  章节：4. The Relationship between Business Models and Business Architecture；正文块：`G18A:p0017:b017`、`G18A:p0017:b018`、`G18A:p0017:b019`、`G18A:p0017:b020`、`G18A:p0017:b021`、`G18A:p0017:b022`、`G18A:p0017:b023`。
- [G21H PDF 18](../documents/G21H.md#page-18)；书页 4，证据 `G21H:A01`：holistic, multi-dimensional business views
  章节：2.3. Business Architecture；正文块：`G21H:p0018:b014`、`G21H:p0018:b015`、`G21H:p0018:b016`。

<a id="r018"></a>

### R018 · 采用组织视角

[业务架构](concepts.md#business_architecture) → `mapping` → [组织单元](concepts.md#organization_unit)

组织关系是业务架构的互补视角。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：不得从该关系自动推导人员汇报、固定基数、时间顺序或项目事实。

- [G18A PDF 17](../documents/G18A.md#page-17)；书页 7，证据 `G18A:A03`：business capabilities, value streams, organizational structure and information objects
  章节：4. The Relationship between Business Models and Business Architecture；正文块：`G18A:p0017:b017`、`G18A:p0017:b018`、`G18A:p0017:b019`、`G18A:p0017:b020`、`G18A:p0017:b021`、`G18A:p0017:b022`、`G18A:p0017:b023`。
- [G21H PDF 18](../documents/G21H.md#page-18)；书页 4，证据 `G21H:A01`：holistic, multi-dimensional business views
  章节：2.3. Business Architecture；正文块：`G21H:p0018:b014`、`G21H:p0018:b015`、`G21H:p0018:b016`。

<a id="r019"></a>

### R019 · 采用信息视角

[业务架构](concepts.md#business_architecture) → `mapping` → [信息概念](concepts.md#information_concept)

业务信息是业务架构的互补视角。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：不得从该关系自动推导人员汇报、固定基数、时间顺序或项目事实。

- [G18A PDF 17](../documents/G18A.md#page-17)；书页 7，证据 `G18A:A03`：business capabilities, value streams, organizational structure and information objects
  章节：4. The Relationship between Business Models and Business Architecture；正文块：`G18A:p0017:b017`、`G18A:p0017:b018`、`G18A:p0017:b019`、`G18A:p0017:b020`、`G18A:p0017:b021`、`G18A:p0017:b022`、`G18A:p0017:b023`。
- [G21H PDF 18](../documents/G21H.md#page-18)；书页 4，证据 `G21H:A01`：holistic, multi-dimensional business views
  章节：2.3. Business Architecture；正文块：`G21H:p0018:b014`、`G21H:p0018:b015`、`G21H:p0018:b016`。

<a id="r020"></a>

### R020 · 转为运行安排

[运营模型](concepts.md#operating_model) → `realization` → [业务模型](concepts.md#business_model)

运营模型把价值逻辑转成能力、过程、环境和资源安排。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：这里是模型间具体化，不表示一个运营模型只对应一个业务模型。

- [G21H PDF 34](../documents/G21H.md#page-34)；书页 20，证据 `G21H:A05`：translates the business model
  章节：4.4.2. Operating Model；正文块：`G21H:p0034:b002`、`G21H:p0034:b003`、`G21H:p0034:b004`、`G21H:p0034:b005`、`G21H:p0034:b006`、`G21H:p0034:b007`。

<a id="r021"></a>

### R021 · 组合资源实现能力

[业务系统](concepts.md#business_system) → `realization` → [业务能力](concepts.md#business_capability)

业务系统包括人员、政策、标准、过程及软硬资源。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：不能把业务系统缩减为一个软件应用。

- [G21H PDF 19](../documents/G21H.md#page-19)；书页 5，证据 `G21H:A02`：together implement a business capability
  章节：2.10. Business System；正文块：`G21H:p0019:b005`、`G21H:p0019:b006`。

<a id="r022"></a>

### R022 · 构成信息地图

[信息概念](concepts.md#information_concept) → `part_of` → [信息地图](concepts.md#information_map)

信息概念及其关系构成信息地图。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：这表示模型组成，不代表信息实体独占一个地图。

- [G190 PDF 12](../documents/G190.md#page-12)；书页 2，证据 `G190:A01`：collection of information concepts and their relationships
  章节：2. What is an Information Map?；正文块：`G190:p0012:b002`、`G190:p0012:b003`、`G190:p0012:b004`、`G190:p0012:b005`。

<a id="r023"></a>

### R023 · 提供业务语义输入

[信息地图](concepts.md#information_map) → `flow` → [数据模型](concepts.md#data_model)

可表示的信息在后续阶段转为数据模型。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：不宣称主观信息都能无损转成数据字段，也不宣称两模型等价。

- [G190 PDF 16](../documents/G190.md#page-16)；书页 6，证据 `G190:A03`：not the same
  章节：5. Distinguishing between Information Maps and Data Models；正文块：`G190:p0016:b002`、`G190:p0016:b003`、`G190:p0016:b004`、`G190:p0016:b005`、`G190:p0016:b006`、`G190:p0016:b007`、`G190:p0016:b008`。
- [G190 PDF 17](../documents/G190.md#page-17)；书页 7，证据 `G190:A05`：Phases C and D translate information
  章节：6. Using Information Maps with the TOGAF ADM；正文块：`G190:p0017:b011`、`G190:p0017:b012`、`G190:p0017:b013`。

<a id="r024"></a>

### R024 · 关联信息与能力

[信息地图](concepts.md#information_map) → `mapping` → [业务能力](concepts.md#business_capability)

信息地图与能力视角共同支持业务价值分析。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：不得从该关系自动推导人员汇报、固定基数、时间顺序或项目事实。

- [G190 PDF 21](../documents/G190.md#page-21)；书页 11，证据 `G190:A06`：joined with business capabilities, value streams, and organization maps
  章节：8. Conclusion；正文块：`G190:p0021:b002`、`G190:p0021:b003`、`G190:p0021:b004`、`G190:p0021:b005`、`G190:p0021:b006`、`G190:p0021:b007`、`G190:p0021:b008`。

<a id="r025"></a>

### R025 · 关联信息与价值流

[信息地图](concepts.md#information_map) → `mapping` → [价值流](concepts.md#value_stream)

信息地图与价值流视角共同支持业务价值分析。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：不得从该关系自动推导人员汇报、固定基数、时间顺序或项目事实。

- [G190 PDF 21](../documents/G190.md#page-21)；书页 11，证据 `G190:A06`：joined with business capabilities, value streams, and organization maps
  章节：8. Conclusion；正文块：`G190:p0021:b002`、`G190:p0021:b003`、`G190:p0021:b004`、`G190:p0021:b005`、`G190:p0021:b006`、`G190:p0021:b007`、`G190:p0021:b008`。

<a id="r026"></a>

### R026 · 关联组织与信息

[信息地图](concepts.md#information_map) → `mapping` → [组织地图](concepts.md#organization_map)

组织地图可表达信息交换，信息视角与组织视角共同使用。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：不得仅从两个框相邻推导某种信息交换。

- [G190 PDF 21](../documents/G190.md#page-21)；书页 11，证据 `G190:A06`：joined with business capabilities, value streams, and organization maps
  章节：8. Conclusion；正文块：`G190:p0021:b002`、`G190:p0021:b003`、`G190:p0021:b004`、`G190:p0021:b005`、`G190:p0021:b006`、`G190:p0021:b007`、`G190:p0021:b008`。
- [G206 PDF 19](../documents/G206.md#page-19)；书页 9，证据 `G206:A06`：information types can be shown flowing
  章节：5. The Relationship to Business Capabilities, Value Streams, and Information Maps；正文块：`G206:p0019:b009`、`G206:p0019:b010`、`G206:p0019:b011`、`G206:p0019:b012`、`G206:p0019:b013`、`G206:p0019:b014`、`G206:p0019:b015`、`G206:p0019:b016`、`G206:p0019:b017`。

<a id="r027"></a>

### R027 · 描述工作关系

[组织地图](concepts.md#organization_map) → `mapping` → [组织单元](concepts.md#organization_unit)

组织地图展示单元、伙伴和相关方的正式或非正式工作关系。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：地图不等同汇报树；正式汇报需独立证据。

- [G206 PDF 12](../documents/G206.md#page-12)；书页 2，证据 `G206:A01`：informal as well as formal
  章节：2. What is an Organization Map?；正文块：`G206:p0012:b005`。
- [G206 PDF 14](../documents/G206.md#page-14)；书页 4，证据 `G206:A03`：horizontal, peer-to-peer, or many-to-many relationships
  章节：3. Differentiating between Organization Maps and Organization Charts；正文块：`G206:p0014:b006`、`G206:p0014:b007`、`G206:p0014:b008`、`G206:p0014:b009`、`G206:p0014:b010`。

<a id="r028"></a>

### R028 · 交付EA能力

[企业架构服务](concepts.md#ea_service) → `realization` → [企业架构能力](concepts.md#ea_capability)

EA服务是交付EA能力的机制。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：不将服务和能力强制一对一。

- [G217 PDF 49](../documents/G217.md#page-49)；书页 33，证据 `G217:A05`：delivery mechanism
  章节：4.4. Enterprise Architecture Capabilities and Services；正文块：`G217:p0049:b012`、`G217:p0049:b013`、`G217:p0049:b014`、`G217:p0049:b015`、`G217:p0049:b016`、`G217:p0049:b017`、`G217:p0049:b018`、`G217:p0049:b019`。

<a id="r029"></a>

### R029 · 按上下文选择服务

[企业架构服务](concepts.md#ea_service) → `mapping` → [数字企业上下文](concepts.md#digital_enterprise_context)

服务涌现模型描述成长上下文中服务的适用关联。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：不是固定人员等级，也不代表所有服务必须同时提供。

- [G217 PDF 31](../documents/G217.md#page-31)；书页 15，证据 `G217:A04`：minimal set of Enterprise Architecture services
  章节：4.1. Introduction；正文块：`G217:p0031:b014`、`G217:p0031:b015`、`G217:p0031:b016`、`G217:p0031:b017`、`G217:p0031:b018`。
- [G217 PDF 59](../documents/G217.md#page-59)；书页 43，证据 `G217:A06`：services per context
  章节：4.4.5. Enterprise Architecture Services Emergence Model；正文块：`G217:p0059:b018`、`G217:p0059:b019`。

<a id="r030"></a>

### R030 · 提供架构实践能力

[企业架构能力](concepts.md#ea_capability) → `enables` → [架构开发方法](concepts.md#adm)

建立架构能力为架构开发、维护和治理提供条件。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：不把某个EA部门的成立当作全部能力已经就绪。

- [G184 PDF 20](../documents/G184.md#page-20)；书页 6，证据 `G184:A02`：ability to use the architecture to govern change activity
  章节：2.3. Enterprise Architecture (EA) Capability；正文块：`G184:p0020:b020`、`G184:p0020:b021`。
- [G188 PDF 19](../documents/G188.md#page-19)；书页 5，证据 `G188:A02`：does not include the Preliminary Phase, Phase G, or Phase H
  章节：2.1. Architecture Project Definition；正文块：`G188:p0019:b011`。

<a id="r031"></a>

### R031 · 维护治理过程

[架构治理委员会](concepts.md#architecture_board) → `governance` → [企业架构能力](concepts.md#ea_capability)

委员会负责过程及对完整性、可信度的建议。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：该过程责任不自动赋予全部目标批准权。

- [G184 PDF 61](../documents/G184.md#page-61)；书页 47，证据 `G184:A04`：An EA governance board owns process
  章节：6.2. Essential Governance；正文块：`G184:p0061:b003`、`G184:p0061:b004`、`G184:p0061:b005`、`G184:p0061:b006`、`G184:p0061:b007`、`G184:p0061:b008`、`G184:p0061:b009`。

<a id="r032"></a>

### R032 · 拥有相应目标决策权

[利益相关者](concepts.md#stakeholder) → `governance` → [目标架构](concepts.md#target_architecture)

G184/G186治理语境中的利益相关者批准目标架构，并决定是否豁免或要求遵守目标。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：需明确有批准权的具体相关方集合；enforcement指强制遵守目标，不是自动取得所有变更执行或投资决定权。

- [G184 PDF 68](../documents/G184.md#page-68)；书页 54，证据 `G184:A05`：Only the set of stakeholders can approve an architecture and roadmap
  章节：6.5.1. Definition of Roles；正文块：`G184:p0068:b018`、`G184:p0068:b019`、`G184:p0068:b020`、`G184:p0068:b021`、`G184:p0068:b022`、`G184:p0068:b023`、`G184:p0068:b024`、`G184:p0068:b025`。
- [G186 PDF 139](../documents/G186.md#page-139)；书页 125，证据 `G186:A08`：Decision rights about the Target Architecture
  章节：15.2. Roles, Duties, and Decision Rights；正文块：`G186:p0139:b020`、`G186:p0139:b021`、`G186:p0139:b025`、`G186:p0139:b026`。

<a id="r033"></a>

### R033 · 批准路线图

[利益相关者](concepts.md#stakeholder) → `governance` → [架构路线图](concepts.md#roadmap)

路线图批准权与能力治理政策批准不同。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：不因架构师编制路线图就推定其独立批准权。

- [G184 PDF 68](../documents/G184.md#page-68)；书页 54，证据 `G184:A05`：Only the set of stakeholders can approve an architecture and roadmap
  章节：6.5.1. Definition of Roles；正文块：`G184:p0068:b018`、`G184:p0068:b019`、`G184:p0068:b020`、`G184:p0068:b021`、`G184:p0068:b022`、`G184:p0068:b023`、`G184:p0068:b024`、`G184:p0068:b025`。

<a id="r034"></a>

### R034 · 负责适用性及完整性

[架构师](concepts.md#architect) → `governance` → [架构模型](concepts.md#architecture_model)

架构师协调关注点及视图，负责架构的适用与完整。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：专业责任不等同全部业务投资决策权。

- [G198 PDF 20](../documents/G198.md#page-20)；书页 12，证据 `G198:A03`：completeness (fitness-for-purpose)
  章节：6.1. Role Description；正文块：`G198:p0020:b014`、`G198:p0020:b015`、`G198:p0020:b016`、`G198:p0020:b017`、`G198:p0020:b018`。
- [G198 PDF 20](../documents/G198.md#page-20)；书页 12，证据 `G198:A04`：connecting all the various views
  章节：6.1. Role Description；正文块：`G198:p0020:b014`、`G198:p0020:b015`、`G198:p0020:b016`、`G198:p0020:b017`、`G198:p0020:b018`。

<a id="r035"></a>

### R035 · 关联关注点归属

[利益相关者关注点](concepts.md#concern) → `mapping` → [利益相关者](concepts.md#stakeholder)

视图要回答具体利益相关者关注点。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：不得从该关系自动推导人员汇报、固定基数、时间顺序或项目事实。

- [G186 PDF 35](../documents/G186.md#page-35)；书页 21，证据 `G186:A02`：a representation of the EA Landscape that addresses
  章节：3.3.1. Communicating with Stakeholders (Concern and View)；正文块：`G186:p0035:b026`、`G186:p0035:b027`、`G186:p0035:b028`。
- [G184 PDF 73](../documents/G184.md#page-73)；书页 59，证据 `G184:A06`：viewpoint library
  正文块：`G184:p0073:b011`、`G184:p0073:b012`、`G184:p0073:b013`、`G184:p0073:b014`、`G184:p0073:b015`、`G184:p0073:b016`、`G184:p0073:b017`、`G184:p0073:b018`、`G184:p0073:b019`、`G184:p0073:b021`、`G184:p0073:b022`、`G184:p0073:b023`、`G184:p0073:b024`；短引在多个章节出现，未自动归属：G184:s0068、G184:s0069。

<a id="r036"></a>

### R036 · 回应关注点

[架构视图](concepts.md#view) → `mapping` → [利益相关者关注点](concepts.md#concern)

视图面向选定关注点描述架构。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：图存在不证明所有关注点已被解决。

- [G186 PDF 35](../documents/G186.md#page-35)；书页 21，证据 `G186:A02`：a representation of the EA Landscape that addresses
  章节：3.3.1. Communicating with Stakeholders (Concern and View)；正文块：`G186:p0035:b026`、`G186:p0035:b027`、`G186:p0035:b028`。
- [G198 PDF 20](../documents/G198.md#page-20)；书页 12，证据 `G198:A03`：completeness (fitness-for-purpose)
  章节：6.1. Role Description；正文块：`G198:p0020:b014`、`G198:p0020:b015`、`G198:p0020:b016`、`G198:p0020:b017`、`G198:p0020:b018`。

<a id="r037"></a>

### R037 · 表示全景的一面

[架构视图](concepts.md#view) → `mapping` → [架构全景](concepts.md#architecture_landscape)

视图是架构全景的一种有目的表示。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：视图与被表示的架构对象不是同一实体。

- [G186 PDF 35](../documents/G186.md#page-35)；书页 21，证据 `G186:A02`：a representation of the EA Landscape that addresses
  章节：3.3.1. Communicating with Stakeholders (Concern and View)；正文块：`G186:p0035:b026`、`G186:p0035:b027`、`G186:p0035:b028`。

<a id="r038"></a>

### R038 · 依据选定视点构造

[架构视图](concepts.md#view) → `depends_on` → [架构视点](concepts.md#viewpoint)

选定视点决定视图需要哪些实体、构建块和关系。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：不能由相似画法推定两个视图采用同一视点。

- [G248 PDF 19](../documents/G248.md#page-19)；书页 7，证据 `G248:A03`：selected viewpoints
  章节：3. Choosing the Building Blocks for the Relevant Entities for Each Change Profile；正文块：`G248:p0019:b002`、`G248:p0019:b003`、`G248:p0019:b004`、`G248:p0019:b005`、`G248:p0019:b006`、`G248:p0019:b007`、`G248:p0019:b008`、`G248:p0019:b009`。

<a id="r039"></a>

### R039 · 由关注点驱动

[架构视点](concepts.md#viewpoint) → `depends_on` → [利益相关者关注点](concepts.md#concern)

视点库从稳定关注点及所需信息出发。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：不由模板可用性替代真实决策问题。

- [G184 PDF 73](../documents/G184.md#page-73)；书页 59，证据 `G184:A06`：viewpoint library
  正文块：`G184:p0073:b011`、`G184:p0073:b012`、`G184:p0073:b013`、`G184:p0073:b014`、`G184:p0073:b015`、`G184:p0073:b016`、`G184:p0073:b017`、`G184:p0073:b018`、`G184:p0073:b019`、`G184:p0073:b021`、`G184:p0073:b022`、`G184:p0073:b023`、`G184:p0073:b024`；短引在多个章节出现，未自动归属：G184:s0068、G184:s0069。

<a id="r040"></a>

### R040 · 追溯所服务需求

[架构规范](concepts.md#architecture_specification) → `depends_on` → [架构需求](concepts.md#requirement)

每项规范应联系其服务的要求。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：追溯不是需求已实现或已验收的证明。

- [G186 PDF 37](../documents/G186.md#page-37)；书页 23，证据 `G186:A04`：always to link a specification to a requirement
  章节：3.3.2. Communicating with Implementers (Gap, Specification, and Control)；正文块：`G186:p0037:b031`、`G186:p0037:b032`、`G186:p0037:b033`、`G186:p0037:b034`、`G186:p0037:b035`、`G186:p0037:b036`、`G186:p0037:b037`、`G186:p0037:b038`。

<a id="r041"></a>

### R041 · 传递实现期望

[架构规范](concepts.md#architecture_specification) → `flow` → [实施者](concepts.md#implementer)

规范与上下文、差距、控制一并交给实施者。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：信息交接不等同批准权转移。

- [G186 PDF 37](../documents/G186.md#page-37)；书页 23，证据 `G186:A03`：context, gap, architecture specification, and control
  章节：3.3.2. Communicating with Implementers (Gap, Specification, and Control)；正文块：`G186:p0037:b002`、`G186:p0037:b003`、`G186:p0037:b004`、`G186:p0037:b005`、`G186:p0037:b006`。

<a id="r042"></a>

### R042 · 约束与验证实施

[架构实施控制](concepts.md#implementation_control) → `governance` → [实施者](concepts.md#implementer)

治理提供控制并检查目标符合性及变更请求。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：合规检查不免除利益相关者目标决策。

- [G186 PDF 37](../documents/G186.md#page-37)；书页 23，证据 `G186:A03`：context, gap, architecture specification, and control
  章节：3.3.2. Communicating with Implementers (Gap, Specification, and Control)；正文块：`G186:p0037:b002`、`G186:p0037:b003`、`G186:p0037:b004`、`G186:p0037:b005`、`G186:p0037:b006`。
- [G21I PDF 48](../documents/G21I.md#page-48)；书页 34，证据 `G21I:A08`：conformance with the Target Architecture
  章节：12. Phase G: Implementation Governance；正文块：`G21I:p0048:b005`。

<a id="r043"></a>

### R043 · 指引并约束细化

[上位架构](concepts.md#superior_architecture) → `constraint` → [更详细的架构](concepts.md#detailed_architecture)

交叠范围内较少细节的已批准目标约束详细架构。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：绝不据此生成chief/enterprise/solution角色之间的人事汇报线。

- [G186 PDF 72](../documents/G186.md#page-72)；书页 58，证据 `G186:A06`：less detailed approved target that overlaps in terms of breadth
  章节：5.3. Operating in the Context of Superior Architecture；正文块：`G186:p0072:b013`、`G186:p0072:b014`、`G186:p0072:b015`、`G186:p0072:b016`。
- [G248 PDF 30](../documents/G248.md#page-30)；书页 18，证据 `G248:A06`：superior architecture
  章节：7. Outlining the Concept；正文块：`G248:p0030:b011`、`G248:p0030:b012`、`G248:p0030:b013`。

<a id="r044"></a>

### R044 · 属于战略粒度

[战略架构](concepts.md#strategic_architecture) → `classification` → [架构详细程度](concepts.md#detail_level)

战略是详细程度维度上的类别。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：粒度分类不是法人或职级层级。

- [G20F PDF 20](../documents/G20F.md#page-20)；书页 8，证据 `G20F:A01`：three levels of detail
  章节：4.1. Different Levels of Detail Enable Agility；正文块：`G20F:p0020:b003`、`G20F:p0020:b004`。

<a id="r045"></a>

### R045 · 属于分段粒度

[分段架构](concepts.md#segment_architecture) → `classification` → [架构详细程度](concepts.md#detail_level)

分段是详细程度维度上的类别。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：与业务/数据/应用/技术域正交，不强制等同部门。

- [G20F PDF 20](../documents/G20F.md#page-20)；书页 8，证据 `G20F:A01`：three levels of detail
  章节：4.1. Different Levels of Detail Enable Agility；正文块：`G20F:p0020:b003`、`G20F:p0020:b004`。

<a id="r046"></a>

### R046 · 属于能力粒度

[能力架构](concepts.md#capability_architecture) → `classification` → [架构详细程度](concepts.md#detail_level)

能力是详细程度维度上的类别。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：不能据此宣称能力架构只有业务域。

- [G20F PDF 20](../documents/G20F.md#page-20)；书页 8，证据 `G20F:A01`：three levels of detail
  章节：4.1. Different Levels of Detail Enable Agility；正文块：`G20F:p0020:b003`、`G20F:p0020:b004`。

<a id="r047"></a>

### R047 · 属于TOGAF架构域

[业务架构](concepts.md#business_architecture) → `specialization` → [架构域](concepts.md#architecture_domain)

该概念是四个架构域中的一个类别。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：specialization表示概念类型，不是组织上下级。

- [G20F PDF 20](../documents/G20F.md#page-20)；书页 8，证据 `G20F:A02`：may exist at all levels of detail
  章节：4.1. Different Levels of Detail Enable Agility；正文块：`G20F:p0020:b010`、`G20F:p0020:b011`。
- [G21H PDF 46](../documents/G21H.md#page-46)；书页 32，证据 `G21H:A07`：Business Architecture defines
  章节：6.3. Architecture Domains；正文块：`G21H:p0046:b002`、`G21H:p0046:b003`。

<a id="r048"></a>

### R048 · 属于TOGAF架构域

[数据架构](concepts.md#data_architecture) → `specialization` → [架构域](concepts.md#architecture_domain)

该概念是四个架构域中的一个类别。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：specialization表示概念类型，不是组织上下级。

- [G20F PDF 20](../documents/G20F.md#page-20)；书页 8，证据 `G20F:A02`：may exist at all levels of detail
  章节：4.1. Different Levels of Detail Enable Agility；正文块：`G20F:p0020:b010`、`G20F:p0020:b011`。
- [G21H PDF 46](../documents/G21H.md#page-46)；书页 32，证据 `G21H:A07`：Business Architecture defines
  章节：6.3. Architecture Domains；正文块：`G21H:p0046:b002`、`G21H:p0046:b003`。

<a id="r049"></a>

### R049 · 属于TOGAF架构域

[应用架构](concepts.md#application_architecture) → `specialization` → [架构域](concepts.md#architecture_domain)

该概念是四个架构域中的一个类别。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：specialization表示概念类型，不是组织上下级。

- [G20F PDF 20](../documents/G20F.md#page-20)；书页 8，证据 `G20F:A02`：may exist at all levels of detail
  章节：4.1. Different Levels of Detail Enable Agility；正文块：`G20F:p0020:b010`、`G20F:p0020:b011`。
- [G21H PDF 46](../documents/G21H.md#page-46)；书页 32，证据 `G21H:A07`：Business Architecture defines
  章节：6.3. Architecture Domains；正文块：`G21H:p0046:b002`、`G21H:p0046:b003`。

<a id="r050"></a>

### R050 · 属于TOGAF架构域

[技术架构](concepts.md#technology_architecture) → `specialization` → [架构域](concepts.md#architecture_domain)

该概念是四个架构域中的一个类别。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：specialization表示概念类型，不是组织上下级。

- [G20F PDF 20](../documents/G20F.md#page-20)；书页 8，证据 `G20F:A02`：may exist at all levels of detail
  章节：4.1. Different Levels of Detail Enable Agility；正文块：`G20F:p0020:b010`、`G20F:p0020:b011`。
- [G21H PDF 46](../documents/G21H.md#page-46)；书页 32，证据 `G21H:A07`：Business Architecture defines
  章节：6.3. Architecture Domains；正文块：`G21H:p0046:b002`、`G21H:p0046:b003`。

<a id="r051"></a>

### R051 · 可出现在各粒度

[架构域](concepts.md#architecture_domain) → `mapping` → [架构详细程度](concepts.md#detail_level)

四个架构域可在每个详细程度层级出现。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：不要将四域竖排位置直接等同战略到实现的单向层级。

- [G20F PDF 20](../documents/G20F.md#page-20)；书页 8，证据 `G20F:A02`：may exist at all levels of detail
  章节：4.1. Different Levels of Detail Enable Agility；正文块：`G20F:p0020:b010`、`G20F:p0020:b011`。

<a id="r052"></a>

### R052 · 区分抽象与详细程度

[架构抽象层次](concepts.md#abstraction_level) → `mapping` → [架构详细程度](concepts.md#detail_level)

两者用于不同建模问题：抽象维度与粒度维度。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：这是跨指南辨析，不定义其数值换算或固定笛卡尔组合。

- [G248 PDF 25](../documents/G248.md#page-25)；书页 13，证据 `G248:A05`：four levels of abstraction
  章节：4. The Guide Approach；正文块：`G248:p0025:b006`、`G248:p0025:b007`、`G248:p0025:b008`。
- [G20F PDF 20](../documents/G20F.md#page-20)；书页 8，证据 `G20F:A01`：three levels of detail
  章节：4.1. Different Levels of Detail Enable Agility；正文块：`G20F:p0020:b003`、`G20F:p0020:b004`。

<a id="r053"></a>

### R053 · 构成模型的一部分

[架构构建块](concepts.md#abb) → `part_of` → [架构模型](concepts.md#architecture_model)

ABB是架构模型的组成构件。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：模型构件不等于描述它的文件或制品。

- [G186 PDF 73](../documents/G186.md#page-73)；书页 59，证据 `G186:A07`：a constituent of the architecture model
  章节：5.5. Where are ABBs?；正文块：`G186:p0073:b005`、`G186:p0073:b006`、`G186:p0073:b007`、`G186:p0073:b008`。

<a id="r054"></a>

### R054 · 表达物理或运营实现

[解决方案构建块](concepts.md#sbb) → `realization` → [架构构建块](concepts.md#abb)

SBB与逻辑ABB关联，表达实现安排。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：源文未给定一对一、唯一产品或特定供应商。

- [G248 PDF 19](../documents/G248.md#page-19)；书页 7，证据 `G248:A02`：physical/operational implementations
  章节：3. Choosing the Building Blocks for the Relevant Entities for Each Change Profile；正文块：`G248:p0019:b002`、`G248:p0019:b003`、`G248:p0019:b004`、`G248:p0019:b005`、`G248:p0019:b006`、`G248:p0019:b007`、`G248:p0019:b008`、`G248:p0019:b009`。

<a id="r055"></a>

### R055 · 记录架构构建块

[架构制品](concepts.md#artifact) → `mapping` → [架构构建块](concepts.md#abb)

制品描述实体、构建块及关系。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：制品不是构建块本身。

- [G248 PDF 24](../documents/G248.md#page-24)；书页 12，证据 `G248:A04`：documented by various artifacts and organized into specific deliverables
  章节：3.6. What About Artifacts and Deliverables?；正文块：`G248:p0024:b010`、`G248:p0024:b011`、`G248:p0024:b012`、`G248:p0024:b013`、`G248:p0024:b014`、`G248:p0024:b015`、`G248:p0024:b016`。

<a id="r056"></a>

### R056 · 组织到交付物

[架构制品](concepts.md#artifact) → `part_of` → [架构交付物](concepts.md#deliverable)

相关制品组织进用于沟通和管理的交付物。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：不推断每个制品只能在一个交付物中使用。

- [G248 PDF 24](../documents/G248.md#page-24)；书页 12，证据 `G248:A04`：documented by various artifacts and organized into specific deliverables
  章节：3.6. What About Artifacts and Deliverables?；正文块：`G248:p0024:b010`、`G248:p0024:b011`、`G248:p0024:b012`、`G248:p0024:b013`、`G248:p0024:b014`、`G248:p0024:b015`、`G248:p0024:b016`。

<a id="r057"></a>

### R057 · 表达增量后的状态

[过渡架构](concepts.md#transition_architecture) → `mapping` → [能力增量](concepts.md#capability_increment)

有意义的过渡状态可包含多个能力增量。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：状态与工作活动不能混为一谈，也不以每个增量必成独立过渡架构。

- [G20F PDF 22](../documents/G20F.md#page-22)；书页 10，证据 `G20F:A03`：architecturally significant point in time
  章节：4.2. Transition Architectures；正文块：`G20F:p0022:b003`、`G20F:p0022:b004`、`G20F:p0022:b005`、`G20F:p0022:b006`、`G20F:p0022:b007`、`G20F:p0022:b008`。
- [G233 PDF 43](../documents/G233.md#page-43)；书页 29，证据 `G233:A07`：preserve a functional value stream
  章节：7.2. Planning Business Capability Instance Increments；正文块：`G233:p0043:b003`、`G233:p0043:b004`、`G233:p0043:b005`、`G233:p0043:b006`、`G233:p0043:b007`、`G233:p0043:b008`。

<a id="r058"></a>

### R058 · 组织过渡演进

[架构路线图](concepts.md#roadmap) → `mapping` → [过渡架构](concepts.md#transition_architecture)

路线图和迁移协调工作包、过渡架构及业务价值。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：图中横向位置本身不提供真实日期或依赖。

- [G21I PDF 46](../documents/G21I.md#page-46)；书页 32，证据 `G21I:A07`：business value and cost of work packages
  章节：11. Phase F: Migration Planning；正文块：`G21I:p0046:b006`、`G21I:p0046:b007`。
- [G242 PDF 85](../documents/G242.md#page-85)；书页 67，证据 `G242:A06`：incremental approach supported by Transition Architecture
  章节：4. Process and Methodology: Using the TOGAF ADM to Build a Digital Sustainability Capability；正文块：`G242:p0085:b004`、`G242:p0085:b005`、`G242:p0085:b006`、`G242:p0085:b007`、`G242:p0085:b008`、`G242:p0085:b009`、`G242:p0085:b010`。

<a id="r059"></a>

### R059 · 纳入迁移规划

[迁移工作包](concepts.md#work_package) → `mapping` → [架构路线图](concepts.md#roadmap)

迁移工作包需要纳入价值、成本及企业组合协调。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：这里是迁移工作包，不自动等同架构项目WBS包。

- [G21I PDF 46](../documents/G21I.md#page-46)；书页 32，证据 `G21I:A07`：business value and cost of work packages
  章节：11. Phase F: Migration Planning；正文块：`G21I:p0046:b006`、`G21I:p0046:b007`。

<a id="r060"></a>

### R060 · 限定A至F和需求管理

[架构项目](concepts.md#architecture_project) → `mapping` → [架构开发方法](concepts.md#adm)

G188架构项目定义只覆盖指定ADM范围。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：不要将该指南的范围限定误作全部ADM范围。

- [G188 PDF 19](../documents/G188.md#page-19)；书页 5，证据 `G188:A01`：Phases A to F and Requirements Management
  章节：2.1. Architecture Project Definition；正文块：`G188:p0019:b007`、`G188:p0019:b008`、`G188:p0019:b009`、`G188:p0019:b010`。
- [G188 PDF 19](../documents/G188.md#page-19)；书页 5，证据 `G188:A02`：does not include the Preliminary Phase, Phase G, or Phase H
  章节：2.1. Architecture Project Definition；正文块：`G188:p0019:b011`。

<a id="r061"></a>

### R061 · 按需使用阶段

[最小可行架构](concepts.md#minimum_viable_architecture) → `mapping` → [架构开发方法](concepts.md#adm)

MVA可涉及部分或全部ADM阶段，并跨域形成切片。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：不代表每个冲刺必须跑完完整ADM。

- [G210 PDF 30](../documents/G210.md#page-30)；书页 18，证据 `G210:A04`：some or all TOGAF ADM phases
  章节：4. TOGAF Phases and Sprints；正文块：`G210:p0030:b002`、`G210:p0030:b003`。
- [G210 PDF 30](../documents/G210.md#page-30)；书页 18，证据 `G210:A05`：slices (partitions) across Phases B to E
  章节：4.2. Phases B, C, D, and E；正文块：`G210:p0030:b016`、`G210:p0030:b017`、`G210:p0030:b018`、`G210:p0030:b019`、`G210:p0030:b020`、`G210:p0030:b021`、`G210:p0030:b022`、`G210:p0030:b023`。

<a id="r062"></a>

### R062 · 导出架构需求

[业务场景](concepts.md#business_scenario) → `enables` → [架构需求](concepts.md#requirement)

业务问题、参与者及交互分析帮助明确需求。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：场景未经适用性和相关方检验不自动成为批准需求。

- [G176 PDF 18](../documents/G176.md#page-18)；书页 6，证据 `G176:A01`：six steps
  章节：3.1. The Overall Process；正文块：`G176:p0018:b003`、`G176:p0018:b004`。
- [G176 PDF 30](../documents/G176.md#page-30)；书页 18，证据 `G176:A03`：any ADM phase
  章节：6. Business Scenarios and the TOGAF ADM；正文块：`G176:p0030:b009`、`G176:p0030:b010`、`G176:p0030:b011`。

<a id="r063"></a>

### R063 · 以可检验结果评估

[业务场景](concepts.md#business_scenario) → `depends_on` → [SMART目标](concepts.md#smart_goal)

场景预期结果需要SMART目标来衡量成功。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：权重和评分规则仍须按项目确定。

- [G176 PDF 36](../documents/G176.md#page-36)；书页 24，证据 `G176:A04`：specific, measurable
  章节：9.2.1. Example of Making Objectives SMART；正文块：`G176:p0036:b031`、`G176:p0036:b032`。

<a id="r064"></a>

### R064 · 横贯四个架构域

[安全架构](concepts.md#security_architecture) → `mapping` → [架构域](concepts.md#architecture_domain)

安全架构与业务、数据、应用和技术域交互。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：不能按横切关注点推导孤立第五域或第五团队。

- [G152 PDF 28](../documents/G152.md#page-28)；书页 16，证据 `G152:A03`：Business, Data, Application, and Technology
  章节：4. Security as a Cross-Cutting Concern；正文块：`G152:p0028:b007`、`G152:p0028:b008`、`G152:p0028:b009`、`G152:p0028:b011`、`G152:p0028:b012`、`G152:p0028:b013`、`G152:p0028:b014`。

<a id="r065"></a>

### R065 · 维持受管理风险

[安全架构](concepts.md#security_architecture) → `mapping` → [风险](concepts.md#risk)

安全架构服务目标和风险管理。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：风险包括正向和负向影响，不只是漏洞清单。

- [G152 PDF 20](../documents/G152.md#page-20)；书页 8，证据 `G152:A01`：organizational, conceptual, logical, and physical components
  章节：3. Enterprise Security Architecture；正文块：`G152:p0020:b002`、`G152:p0020:b003`、`G152:p0020:b004`、`G152:p0020:b005`。
- [G152 PDF 21](../documents/G152.md#page-21)；书页 9，证据 `G152:A02`：effect of uncertainty on objectives
  章节：3.1.1. Definition of Risk；正文块：`G152:p0021:b009`。

<a id="r066"></a>

### R066 · 显式说明域间信任

[安全域](concepts.md#security_domain) → `mapping` → [信任关系](concepts.md#trust_relationship)

安全域政策边界与信任依据和方向需要明确。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：没有信任不等于缺失数据；双向也不能从一条无方向线默认。

- [G152 PDF 33](../documents/G152.md#page-33)；书页 21，证据 `G152:A04`：one security policy
  章节：5.3.2. Security Domain Model；正文块：`G152:p0033:b001`、`G152:p0033:b002`、`G152:p0033:b003`、`G152:p0033:b004`、`G152:p0033:b005`、`G152:p0033:b006`。
- [G152 PDF 33](../documents/G152.md#page-33)；书页 21，证据 `G152:A05`：unidirectional, bidirectional, or non-existent
  章节：5.3.3. Trust Framework；正文块：`G152:p0033:b015`、`G152:p0033:b016`、`G152:p0033:b017`、`G152:p0033:b018`、`G152:p0033:b019`、`G152:p0033:b020`。

<a id="r067"></a>

### R067 · 属于安全相关需求

[安全需求](concepts.md#security_requirement) → `specialization` → [架构需求](concepts.md#requirement)

安全需求保持到业务驱动的追溯。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：不把控制目标或任何政策原句都当成需求。

- [G152 PDF 40](../documents/G152.md#page-40)；书页 28，证据 `G152:A06`：Traceability mapping between business drivers and requirements
  章节：5.10.1. Business Attribute Profile；正文块：`G152:p0040:b007`。
- [G152 PDF 41](../documents/G152.md#page-41)；书页 29，证据 `G152:A07`：It differs from a security requirement
  章节：5.10.2. Control Objectives/Security Objectives；正文块：`G152:p0041:b031`、`G152:p0041:b032`、`G152:p0041:b033`、`G152:p0041:b034`。

<a id="r068"></a>

### R068 · 区分目标与需求

[安全控制目标](concepts.md#control_objective) → `mapping` → [安全需求](concepts.md#security_requirement)

两者相关但语义不同，应保留单独对象。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：mapping不表示等价或继承。

- [G152 PDF 41](../documents/G152.md#page-41)；书页 29，证据 `G152:A07`：It differs from a security requirement
  章节：5.10.2. Control Objectives/Security Objectives；正文块：`G152:p0041:b031`、`G152:p0041:b032`、`G152:p0041:b033`、`G152:p0041:b034`。

<a id="r069"></a>

### R069 · 把核心客户数据作为资产管理

[客户主数据管理](concepts.md#customer_mdm) → `mapping` → [核心客户数据](concepts.md#kernel_customer_data)

C-MDM能力围绕跨部门共享的核心客户信息。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：指南清单不自动成为所有项目强制字段。

- [G21B PDF 21](../documents/G21B.md#page-21)；书页 11，证据 `G21B:A01`：people, processes, organizations, and systems
  章节：3. C-MDM Capability；正文块：`G21B:p0021:b002`、`G21B:p0021:b003`、`G21B:p0021:b004`。
- [G21B PDF 21](../documents/G21B.md#page-21)；书页 11，证据 `G21B:A02`：shared across the organization’s departments
  章节：3. C-MDM Capability；正文块：`G21B:p0021:b005`。

<a id="r070"></a>

### R070 · 提供公共部门参考

[政府参考模型](concepts.md#government_reference_model) → `enables` → [业务架构](concepts.md#business_architecture)

GRM用于ADM业务架构阶段的公共部门业务建模。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：Sector/Function/Service分类不自动表示真实政府部门汇报。

- [G21D PDF 21](../documents/G21D.md#page-21)；书页 1，证据 `G21D:A02`：reference model template
  章节：1.1. Objective；正文块：`G21D:p0021:b011`、`G21D:p0021:b012`、`G21D:p0021:b013`、`G21D:p0021:b014`。
- [G21D PDF 24](../documents/G21D.md#page-24)；书页 4，证据 `G21D:A04`：Phase B: Business Architecture
  章节：1.4. The TOGAF Standard and the Government Reference Model；正文块：`G21D:p0024:b002`、`G21D:p0024:b003`、`G21D:p0024:b004`、`G21D:p0024:b005`。

<a id="r071"></a>

### R071 · 提供数字业务参考视角

[数字业务参考模型](concepts.md#dbrm) → `mapping` → [业务架构](concepts.md#business_architecture)

DBRM要素可与TOGAF架构内容建立映射。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：高层图明确不规定详细关系，禁止据布局补全概念依赖图。

- [G21H PDF 18](../documents/G21H.md#page-18)；书页 4，证据 `G21H:A01`：holistic, multi-dimensional business views
  章节：2.3. Business Architecture；正文块：`G21H:p0018:b014`、`G21H:p0018:b015`、`G21H:p0018:b016`。
- [G21H PDF 24](../documents/G21H.md#page-24)；书页 10，证据 `G21H:A03`：ten (10) core elements
  章节：3.1. Introduction；正文块：`G21H:p0024:b005`、`G21H:p0024:b006`、`G21H:p0024:b007`。
- [G21H PDF 46](../documents/G21H.md#page-46)；书页 32，证据 `G21H:A07`：Business Architecture defines
  章节：6.3. Architecture Domains；正文块：`G21H:p0046:b002`、`G21H:p0046:b003`。

<a id="r072"></a>

### R072 · 实现原子业务功能

[微服务](concepts.md#microservice) → `realization` → [原子业务功能](concepts.md#atomic_business_function)

微服务实现独立且自包含的原子业务功能。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：原文没有在此建立数据库、容器或进程的一对一基数。

- [G21I PDF 16](../documents/G21I.md#page-16)；书页 2，证据 `G21I:A02`：implements an Atomic Business Function
  章节：2. Microservices Architecture Defined；正文块：`G21I:p0016:b006`、`G21I:p0016:b007`、`G21I:p0016:b008`、`G21I:p0016:b009`、`G21I:p0016:b010`。

<a id="r073"></a>

### R073 · 提供支持能力的服务

[原子业务功能](concepts.md#atomic_business_function) → `enables` → [业务能力](concepts.md#business_capability)

ABF通常提供支持企业能力的服务。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：通常不等于所有情形的强制唯一关系。

- [G21I PDF 35](../documents/G21I.md#page-35)；书页 21，证据 `G21I:A03`：smallest unit of business function
  章节：7. Phase B: Business Architecture；正文块：`G21I:p0035:b015`、`G21I:p0035:b016`、`G21I:p0035:b017`、`G21I:p0035:b018`、`G21I:p0035:b019`、`G21I:p0035:b020`。

<a id="r074"></a>

### R074 · 定义服务契约与API

[微服务](concepts.md#microservice) → `depends_on` → [微服务契约与API](concepts.md#service_contract)

每个微服务提供契约和接口以支持使用。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：这里不规定API数量、协议或消费者数量。

- [G21I PDF 41](../documents/G21I.md#page-41)；书页 27，证据 `G21I:A06`：defined service contract
  章节：9.1. Microservices；正文块：`G21I:p0041:b018`、`G21I:p0041:b019`、`G21I:p0041:b020`。

<a id="r075"></a>

### R075 · 作为架构风格的服务单元

[微服务](concepts.md#microservice) → `mapping` → [微服务架构](concepts.md#msa)

独立、自包含和单一责任的服务是MSA的关键。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：采用一个微服务不证明整个企业架构就是MSA。

- [G21I PDF 16](../documents/G21I.md#page-16)；书页 2，证据 `G21I:A01`：not a product, framework, or platform
  章节：2. Microservices Architecture Defined；正文块：`G21I:p0016:b002`、`G21I:p0016:b003`、`G21I:p0016:b004`、`G21I:p0016:b005`。
- [G21I PDF 16](../documents/G21I.md#page-16)；书页 2，证据 `G21I:A02`：implements an Atomic Business Function
  章节：2. Microservices Architecture Defined；正文块：`G21I:p0016:b006`、`G21I:p0016:b007`、`G21I:p0016:b008`、`G21I:p0016:b009`、`G21I:p0016:b010`。

<a id="r076"></a>

### R076 · 约束企业上下文中的业务功能

[目标架构](concepts.md#target_architecture) → `constraint` → [原子业务功能](concepts.md#atomic_business_function)

业务功能价值流需与整体目标架构一致。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：不把业务功能拆分当成可以脱离整体架构的局部决定。

- [G21I PDF 36](../documents/G21I.md#page-36)；书页 22，证据 `G21I:A04`：align with the overall Target Architecture
  章节：7.1. Business Function Decomposition；正文块：`G21I:p0036:b017`、`G21I:p0036:b018`、`G21I:p0036:b019`、`G21I:p0036:b020`。

<a id="r077"></a>

### R077 · 按所服务业务功能界定数据

[数据架构](concepts.md#data_architecture) → `depends_on` → [原子业务功能](concepts.md#atomic_business_function)

MSA数据架构考虑业务功能管理的数据及必要外部源。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：该关系限定MSA上下文，不规定所有企业数据都只能局部私有。

- [G21I PDF 38](../documents/G21I.md#page-38)；书页 24，证据 `G21I:A05`：data managed by the business function
  章节：8. Phase C: Information Systems Architectures (Data and Application)；正文块：`G21I:p0038:b002`、`G21I:p0038:b003`、`G21I:p0038:b004`、`G21I:p0038:b005`、`G21I:p0038:b006`、`G21I:p0038:b007`。

<a id="r078"></a>

### R078 · 规划实施并控制质量

[元数据管理](concepts.md#metadata_management) → `governance` → [元数据](concepts.md#metadata)

通过过程和验证工作流保障集成元数据质量。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：存储成功不等于质量验证通过。

- [G234 PDF 14](../documents/G234.md#page-14)；书页 4，证据 `G234:A01`：planning, implementation, and control activity
  章节：3. Metadata Management Capability；正文块：`G234:p0014:b012`、`G234:p0014:b013`、`G234:p0014:b014`。
- [G234 PDF 24](../documents/G234.md#page-24)；书页 14，证据 `G234:A03`：processes and validation workflows
  章节：4.2.2. Formalize Metadata Management Processes；正文块：`G234:p0024:b009`、`G234:p0024:b010`。

<a id="r079"></a>

### R079 · 属于元数据类别

[业务元数据](concepts.md#business_metadata) → `specialization` → [元数据](concepts.md#metadata)

元数据三分类之一。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：不由类别名称推断存储位置、所有权或更新频率。

- [G234 PDF 26](../documents/G234.md#page-26)；书页 16，证据 `G234:A05`：Business metadata
  章节：4.3. Metadata Management Guidelines for Information Systems Architectures (ADM Phase C)；正文块：`G234:p0026:b007`、`G234:p0026:b008`、`G234:p0026:b012`、`G234:p0026:b013`、`G234:p0026:b014`、`G234:p0026:b015`。

<a id="r080"></a>

### R080 · 属于元数据类别

[技术元数据](concepts.md#technical_metadata) → `specialization` → [元数据](concepts.md#metadata)

元数据三分类之一。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：不由类别名称推断存储位置、所有权或更新频率。

- [G234 PDF 26](../documents/G234.md#page-26)；书页 16，证据 `G234:A05`：Business metadata
  章节：4.3. Metadata Management Guidelines for Information Systems Architectures (ADM Phase C)；正文块：`G234:p0026:b007`、`G234:p0026:b008`、`G234:p0026:b012`、`G234:p0026:b013`、`G234:p0026:b014`、`G234:p0026:b015`。

<a id="r081"></a>

### R081 · 属于元数据类别

[运营元数据](concepts.md#operational_metadata) → `specialization` → [元数据](concepts.md#metadata)

元数据三分类之一。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：不由类别名称推断存储位置、所有权或更新频率。

- [G234 PDF 26](../documents/G234.md#page-26)；书页 16，证据 `G234:A05`：Business metadata
  章节：4.3. Metadata Management Guidelines for Information Systems Architectures (ADM Phase C)；正文块：`G234:p0026:b007`、`G234:p0026:b008`、`G234:p0026:b012`、`G234:p0026:b013`、`G234:p0026:b014`、`G234:p0026:b015`。

<a id="r082"></a>

### R082 · 存储与交换元数据

[元数据存储库](concepts.md#metadata_repository) → `mapping` → [元数据](concepts.md#metadata)

元数据可通过手工导入、推送或拉取交换。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：交换方式与集成风格不同；拉取需另行审查访问与侵入性。

- [G234 PDF 28](../documents/G234.md#page-28)；书页 18，证据 `G234:A06`：Manual ingestion
  章节：4.3. Metadata Management Guidelines for Information Systems Architectures (ADM Phase C)；正文块：`G234:p0028:b017`、`G234:p0028:b018`、`G234:p0028:b027`。

<a id="r083"></a>

### R083 · 配置存储及交换机制

[元数据管理](concepts.md#metadata_management) → `depends_on` → [元数据存储库](concepts.md#metadata_repository)

IT方案还需要数据模型及更新/验证流程。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：存储库不是元数据管理能力的全部。

- [G234 PDF 25](../documents/G234.md#page-25)；书页 15，证据 `G234:A04`：combination of technologies
  章节：4.3. Metadata Management Guidelines for Information Systems Architectures (ADM Phase C)；正文块：`G234:p0025:b003`、`G234:p0025:b004`、`G234:p0025:b005`。
- [G234 PDF 28](../documents/G234.md#page-28)；书页 18，证据 `G234:A06`：Manual ingestion
  章节：4.3. Metadata Management Guidelines for Information Systems Architectures (ADM Phase C)；正文块：`G234:p0028:b017`、`G234:p0028:b018`、`G234:p0028:b027`。

<a id="r084"></a>

### R084 · 追溯完整数据价值链

[商业智能能力](concepts.md#bi_capability) → `depends_on` → [数据血缘](concepts.md#data_lineage)

BI质量和元数据需要从运营源到消费端的血缘支持。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：不以局部ETL流程图代替完整源到消费追溯。

- [G238 PDF 14](../documents/G238.md#page-14)；书页 4，证据 `G238:A02`：from operational data sources to data consumption
  章节：2.2. BI & Analytics High-Level Business Functions Description；表格：`G238:p0014:t01`。

<a id="r085"></a>

### R085 · 用环境政策和影响评价约束变更

[信息系统环境可持续性](concepts.md#digital_sustainability) → `governance` → [目标架构](concepts.md#target_architecture)

业务环境政策及治理阈值影响基线到目标的增量变更。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：指南没有给所有组织通用的环境阈值或统一交换标准。

- [G242 PDF 30](../documents/G242.md#page-30)；书页 12，证据 `G242:A02`：Business Policies for Sustainability
  章节：3.2. How to Deploy a Sustainable Information System Policy；正文块：`G242:p0030:b012`、`G242:p0030:b013`、`G242:p0030:b014`、`G242:p0030:b015`、`G242:p0030:b016`。
- [G242 PDF 78](../documents/G242.md#page-78)；书页 60，证据 `G242:A05`：criteria determining whether a decision
  章节：3.9.2. Setting Up Decision Validation Bodies Aligned with the Environmental Issue；正文块：`G242:p0078:b002`、`G242:p0078:b003`、`G242:p0078:b004`、`G242:p0078:b005`。
- [G242 PDF 85](../documents/G242.md#page-85)；书页 67，证据 `G242:A06`：incremental approach supported by Transition Architecture
  章节：4. Process and Methodology: Using the TOGAF ADM to Build a Digital Sustainability Capability；正文块：`G242:p0085:b004`、`G242:p0085:b005`、`G242:p0085:b006`、`G242:p0085:b007`、`G242:p0085:b008`、`G242:p0085:b009`、`G242:p0085:b010`。

<a id="r086"></a>

### R086 · 通过增量过渡改进

[信息系统环境可持续性](concepts.md#digital_sustainability) → `mapping` → [过渡架构](concepts.md#transition_architecture)

过渡架构承担向更可持续目标演进的中间状态。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：运行耗电改善不能单独证明整个生命周期足迹改善。

- [G242 PDF 85](../documents/G242.md#page-85)；书页 67，证据 `G242:A06`：incremental approach supported by Transition Architecture
  章节：4. Process and Methodology: Using the TOGAF ADM to Build a Digital Sustainability Capability；正文块：`G242:p0085:b004`、`G242:p0085:b005`、`G242:p0085:b006`、`G242:p0085:b007`、`G242:p0085:b008`、`G242:p0085:b009`、`G242:p0085:b010`。

<a id="r087"></a>

### R087 · 评价并改进实践

[架构成熟度模型](concepts.md#maturity_model) → `mapping` → [企业架构能力](concepts.md#ea_capability)

定期评估用于业务目标导向的架构能力改进。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：参考成熟度分数不是个人技能等级或认证数量。

- [G203 PDF 11](../documents/G203.md#page-11)；书页 1，证据 `G203:A01`：organization-specific maturity model
  章节：1.1. Objective；正文块：`G203:p0011:b003`、`G203:p0011:b004`、`G203:p0011:b005`、`G203:p0011:b006`。
- [G203 PDF 11](../documents/G203.md#page-11)；书页 1，证据 `G203:A02`：periodically measure improvement
  章节：1.2. Background；正文块：`G203:p0011:b017`。
- [G203 PDF 18](../documents/G203.md#page-18)；书页 8，证据 `G203:A06`：align operations to business goals
  章节：3.1.1. Introduction；正文块：`G203:p0018:b019`、`G203:p0018:b020`、`G203:p0018:b021`、`G203:p0018:b022`。

<a id="r088"></a>

### R088 · 为采用取舍提供依据

[数字技术采用就绪度评估](concepts.md#readiness_assessment) → `enables` → [ABCD采用方式](concepts.md#adoption_approach)

就绪因素、广度和速度共同帮助选择采用方式。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：四类型不是优劣排序，依赖图也不是完整因果网络。

- [G212 PDF 39](../documents/G212.md#page-39)；书页 23，证据 `G212:A03`：breadth/extensiveness
  章节：5.1. Step 1: Select the Adoption Approach；正文块：`G212:p0039:b010`、`G212:p0039:b011`、`G212:p0039:b012`、`G212:p0039:b013`、`G212:p0039:b014`。
- [G212 PDF 44](../documents/G212.md#page-44)；书页 28，证据 `G212:A05`：not mutually-exclusive
  章节：5.4. Step 4: Address Shortcomings and Initiate Digital Technology Adoption；正文块：`G212:p0044:b001`、`G212:p0044:b002`、`G212:p0044:b003`。
- [G212 PDF 46](../documents/G212.md#page-46)；书页 30，证据 `G212:A06`：identification of stakeholders
  章节：6. Architectural Implication and Alignment to the TOGAF ADM；表格：`G212:p0046:t01`。

<a id="r089"></a>

### R089 · 可承担多个角色

[人员](concepts.md#person) → `mapping` → [角色](concepts.md#role)

一人可能承担多个角色；源文也提到多人各自只承担一个角色，实际配置需按企业需要明确。

关系方向语义：`association`；基数：{"source_to_target": "may-be-many", "target_to_source": null, "minimums_specified": false, "evidence_text": "people who perform multiple roles"}。

不可推断：不把角色数等同人数；此处证据不明确规定每个角色可同时由多少人承担。

- [G249 PDF 16](../documents/G249.md#page-16)；书页 6，证据 `G249:A02`：multiple roles
  章节：4. Architecture Roles；正文块：`G249:p0016:b012`、`G249:p0016:b013`、`G249:p0016:b014`、`G249:p0016:b015`。
- [G176 PDF 42](../documents/G176.md#page-42)；书页 30，证据 `G176:A05`：roles that can be filled by the same person
  章节：10. Roles；正文块：`G176:p0042:b002`、`G176:p0042:b003`、`G176:p0042:b004`、`G176:p0042:b005`。

<a id="r090"></a>

### R090 · 区分岗位与活动职责

[岗位](concepts.md#job) → `mapping` → [角色](concepts.md#role)

岗位是正式位置，角色是活动和技能组合。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：不同对象间的关联不是等价，也不提供固定基数。

- [G249 PDF 16](../documents/G249.md#page-16)；书页 6，证据 `G249:A01`：Job means
  章节：4. Architecture Roles；正文块：`G249:p0016:b008`。

<a id="r091"></a>

### R091 · 关联具体任务

[任务分配](concepts.md#assignment) → `mapping` → [角色](concepts.md#role)

具体任务在角色上下文中分配。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：任务分配不自动改变岗位或治理授权。

- [G249 PDF 16](../documents/G249.md#page-16)；书页 6，证据 `G249:A01`：Job means
  章节：4. Architecture Roles；正文块：`G249:p0016:b008`。

<a id="r092"></a>

### R092 · 需要相关技能

[角色](concepts.md#role) → `depends_on` → [技能](concepts.md#skill)

成功履行角色需要相应技能及深度。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：要求不是个人已经具备的事实；来源量表不能混用。

- [G198 PDF 13](../documents/G198.md#page-13)；书页 5，证据 `G198:A01`：depth of knowledge required
  章节：4.1. Overview；正文块：`G198:p0013:b012`。
- [G249 PDF 26](../documents/G249.md#page-26)；书页 16，证据 `G249:A06`：categories of skills
  章节：5. Skills and Proficiency Levels；正文块：`G249:p0026:b002`。

<a id="r093"></a>

### R093 · 逐技能表达深度

[技能](concepts.md#skill) → `mapping` → [技能熟练等级](concepts.md#proficiency_level)

技能矩阵按相应指南量表表达要求。

关系方向语义：`association`；基数：未在所引证据中规定。

不可推断：不得跨G198/G249直接平均或换算等级。

- [G198 PDF 13](../documents/G198.md#page-13)；书页 5，证据 `G198:A01`：depth of knowledge required
  章节：4.1. Overview；正文块：`G198:p0013:b012`。
- [G198 PDF 15](../documents/G198.md#page-15)；书页 7，证据 `G198:A02`：four levels of knowledge or proficiency
  章节：4.4. Proficiency Levels；正文块：`G198:p0015:b020`、`G198:p0015:b021`。

<a id="r094"></a>

### R094 · 是企业架构师的特例

[首席架构师](concepts.md#chief_architect) → `specialization` → [企业架构师](concepts.md#enterprise_architect)

首席角色特别关注企业战略和运营上下文。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：类型特化绝不证明首席架构师向企业架构师汇报。

- [G249 PDF 17](../documents/G249.md#page-17)；书页 7，证据 `G249:A03`：special case of an Enterprise Architect
  章节：4. Architecture Roles；正文块：`G249:p0017:b001`、`G249:p0017:b002`、`G249:p0017:b003`、`G249:p0017:b004`、`G249:p0017:b005`。

<a id="r095"></a>

### R095 · 企业范围的架构角色

[企业架构师](concepts.md#enterprise_architect) → `specialization` → [架构师](concepts.md#architect)

企业架构师是架构角色的具体类别。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：类别关系不是实际职位或人事层级。

- [G249 PDF 17](../documents/G249.md#page-17)；书页 7，证据 `G249:A03`：special case of an Enterprise Architect
  章节：4. Architecture Roles；正文块：`G249:p0017:b001`、`G249:p0017:b002`、`G249:p0017:b003`、`G249:p0017:b004`、`G249:p0017:b005`。
- [G198 PDF 20](../documents/G198.md#page-20)；书页 12，证据 `G198:A03`：completeness (fitness-for-purpose)
  章节：6.1. Role Description；正文块：`G198:p0020:b014`、`G198:p0020:b015`、`G198:p0020:b016`、`G198:p0020:b017`、`G198:p0020:b018`。

<a id="r096"></a>

### R096 · 方案范围的架构角色

[解决方案架构师](concepts.md#solution_architect) → `specialization` → [架构师](concepts.md#architect)

解决方案架构师是架构角色的具体类别。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：不由类型关系推断其具体职级。

- [G249 PDF 17](../documents/G249.md#page-17)；书页 7，证据 `G249:A04`：superior architectures
  章节：4. Architecture Roles；正文块：`G249:p0017:b006`、`G249:p0017:b007`、`G249:p0017:b008`、`G249:p0017:b009`、`G249:p0017:b010`、`G249:p0017:b011`。
- [G198 PDF 20](../documents/G198.md#page-20)；书页 12，证据 `G198:A03`：completeness (fitness-for-purpose)
  章节：6.1. Role Description；正文块：`G198:p0020:b014`、`G198:p0020:b015`、`G198:p0020:b016`、`G198:p0020:b017`、`G198:p0020:b018`。

<a id="r097"></a>

### R097 · 指引方案工作

[上位架构](concepts.md#superior_architecture) → `constraint` → [解决方案架构工作](concepts.md#solution_architecture_work)

企业及分段上位架构约束方案工作的架构选择。

关系方向语义：`directed`；基数：未在所引证据中规定。

不可推断：这是适用于方案工作的架构约束，不是对个人的人事汇报或任命；不能把架构范围替换成该范围架构师的全部个人授权。

- [G249 PDF 17](../documents/G249.md#page-17)；书页 7，证据 `G249:A04`：superior architectures
  章节：4. Architecture Roles；正文块：`G249:p0017:b006`、`G249:p0017:b007`、`G249:p0017:b008`、`G249:p0017:b009`、`G249:p0017:b010`、`G249:p0017:b011`。
