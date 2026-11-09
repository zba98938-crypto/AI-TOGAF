# 元数据业务功能参考地图

`profile_id`: metadata-business-function-map；`artifact_id`: functional-decomposition-diagram；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G234 §5.1；G234/fig5-1；references/source-tables/metadata-functions.json。

## 构图与定义状态

表示族：`metadata-map`；输出：`diagram`。规范版本：2.3。

{
  "id": "metadata-business-function-map",
  "version": "2.3",
  "source_verified": false,
  "layout_notes": "按已核查的来源结构参数化；参考图与业务实例的验收分别进行。",
  "structure": "business",
  "source_assets": [
    {
      "path": "reviews/source-template-bases/G234-fig5-1-p31-0.png",
      "figure_id": "G234/fig5-1",
      "pdf_page": 31,
      "sha256": "8a1c3ca521098339e8f975010c63109938f31ff5d4825d55d40634e4991796c8",
      "source_version": "G234e.pdf",
      "source_pdf_sha256": "34a1c590f938bf915182fe5bbe00d1d68f9a3e948697b5500ce7c5a9494f77e7",
      "verification_scope": "actual image opened; structural layout and readable labels compared; tiny embedded screenshots excluded"
    }
  ],
  "structure_basis": "实际打开可信来源图；主图保留容器和组带，详细属性按同一稳定ID可见呈现；空间位置不增加语义关系。",
  "reference_rows": [
    1,
    2,
    3,
    3,
    3,
    4,
    4,
    5,
    5,
    6
  ],
  "verification_evidence": "reviews/source-verification/metadata-business-function-map.json"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：function, role, visual_container。关系类型：decomposes, visually_contains。

```json
{
  "entities": {
    "function": [
      "level",
      "definition"
    ],
    "role": [
      "responsibility"
    ],
    "visual_container": [
      "definition"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 对象、关系、必要属性均可追溯并得到表达
- 参考内容不自动成为项目事实；未知项保持显式
- 团队四角色在参考模板同一行，团队不是功能节点
- 业务/应用总范围容器保持独立
- 分解是职责包含，不推导执行顺序
- 源功能定义完整，不能在句号或换行处任意截断
- 图5-2采集顶部、集成右侧纵向、管理底部，治理/报表/参考数据管理独立
- 裁剪未选项及理由在评审登记

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构业务案例；采用来源结构及术语，不代表真实实施或批准。",
  "sources": [
    {
      "id": "case-source",
      "kind": "example",
      "description": "虚构社区服务机构的访谈、记录和项目约定"
    }
  ],
  "entities": [
    {
      "id": "metadata-team",
      "type": "visual_container",
      "name": "元数据管理团队",
      "attributes": {
        "definition": "角色协作范围，具体任命与RACI另行确定",
        "g234:slot": "team"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-functions",
      "type": "visual_container",
      "name": "元数据管理业务功能",
      "attributes": {
        "definition": "G234参考功能范围；分组位置不表示执行顺序或实现状态",
        "g234:slot": "functions"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-group-1",
      "type": "function",
      "name": "战略与路线图定义",
      "attributes": {
        "level": 1,
        "definition": "战略与路线图定义功能组；不是流程阶段",
        "reference_row": 1,
        "reference_column": 0,
        "g234:slot": "1"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-560",
      "type": "function",
      "name": "定义业务驱动因素与需求",
      "attributes": {
        "level": 2,
        "definition": "描述元数据管理能力必须支持的愿景、语境与战略。捕获并记录业务用例与优先级。随时间维护该清单。",
        "source_row": "G234 表5-1 L560"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-561",
      "type": "function",
      "name": "定义角色与职责",
      "attributes": {
        "level": 2,
        "definition": "定义每个参与者（业务、IT）在元数据管理能力建设与运行中的角色与职责。",
        "source_row": "G234 表5-1 L561"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-562",
      "type": "function",
      "name": "构建路线图",
      "attributes": {
        "level": 2,
        "definition": "构建并维护路线图。形成已记录、排好优先级的业务需求清单，以实施元数据管理能力。定义目标与整体旅程。",
        "source_row": "G234 表5-1 L562"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-563",
      "type": "function",
      "name": "识别并培养赞助支持",
      "attributes": {
        "level": 2,
        "definition": "让 IT 与业务赞助人参与元数据管理平台的治理。",
        "source_row": "G234 表5-1 L563"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-564",
      "type": "function",
      "name": "定义 KPI",
      "attributes": {
        "level": 2,
        "definition": "定义关键绩效指标（KPI），以衡量并引导元数据管理平台交付业务目标的有效性。",
        "source_row": "G234 表5-1 L564"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-group-2",
      "type": "function",
      "name": "治理与度量",
      "attributes": {
        "level": 1,
        "definition": "治理与度量功能组；不是流程阶段",
        "reference_row": 2,
        "reference_column": 0,
        "g234:slot": "2"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-565",
      "type": "function",
      "name": "定义业务数据域",
      "attributes": {
        "level": 2,
        "definition": "为治理目的定义数据域。数据域是数据与元数据资产的一致分组，便于落实数据与元数据资产的管家职责与所有权。",
        "source_row": "G234 表5-1 L565"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-566",
      "type": "function",
      "name": "按数据域吸纳并任命数据管家、业务数据所有者、数据隐私官",
      "attributes": {
        "level": 2,
        "definition": "识别将维护与治理元数据存储库的关键利益相关者。",
        "source_row": "G234 表5-1 L566"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-567",
      "type": "function",
      "name": "度量元数据文档质量与使用",
      "attributes": {
        "level": 2,
        "definition": "定义 KPI 以监控存储库中元数据的质量与使用情况。",
        "source_row": "G234 表5-1 L567"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-group-3",
      "type": "function",
      "name": "业务术语表文档",
      "attributes": {
        "level": 1,
        "definition": "业务术语表文档功能组；不是流程阶段",
        "reference_row": 3,
        "reference_column": 0,
        "g234:slot": "3"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-568",
      "type": "function",
      "name": "记录业务概念",
      "attributes": {
        "level": 2,
        "definition": "定义业务概念的名称与语义，例如业务术语、业务数据对象、业务数据元素或任何其他有意义的业务概念。",
        "source_row": "G234 表5-1 L568"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-569",
      "type": "function",
      "name": "对数据对象与数据元素分类（隐私、业务关键性）",
      "attributes": {
        "level": 2,
        "definition": "为安全与合规目的对数据分类。识别对业务有价值的数据资产（关键数据、“皇冠明珠”）。",
        "source_row": "G234 表5-1 L569"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-group-4",
      "type": "function",
      "name": "数据字典文档",
      "attributes": {
        "level": 1,
        "definition": "数据字典文档功能组；不是流程阶段",
        "reference_row": 3,
        "reference_column": 1,
        "g234:slot": "4"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-570",
      "type": "function",
      "name": "记录应用",
      "attributes": {
        "level": 2,
        "definition": "描述并维护应用间的数据流；识别数据位置与数据采集点；记录并维护应用清单及相关 IT 经理信息；记录联系人信息（包括由第三方管理的应用）；为存储或处理关键数据元素的应用收集并维护 SLA。",
        "source_row": "G234 表5-1 L570"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-571",
      "type": "function",
      "name": "记录数据库",
      "attributes": {
        "level": 2,
        "definition": "记录存储数据的数据库系统。识别要纳入运营数据治理的相关数据保管人。此处数据库可理解为存储数据集合的任何手段。",
        "source_row": "G234 表5-1 L571"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-572",
      "type": "function",
      "name": "记录数据集与数据字段",
      "attributes": {
        "level": 2,
        "definition": "在每个数据库系统中捕获相关数据集与数据字段，使数据文档可供所有人使用，以促进复用并落实数据治理与合规。",
        "source_row": "G234 表5-1 L572"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-group-5",
      "type": "function",
      "name": "数据使用文档",
      "attributes": {
        "level": 1,
        "definition": "数据使用文档功能组；不是流程阶段",
        "reference_row": 3,
        "reference_column": 2,
        "g234:slot": "5"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-573",
      "type": "function",
      "name": "记录数据处理活动",
      "attributes": {
        "level": 2,
        "definition": "记录数据使用与操作，例如收集、记录、组织、结构化、存储、改编或变更、检索、咨询、使用、通过传输披露、传播或以其他方式提供、对齐或组合、限制、擦除或销毁。",
        "source_row": "G234 表5-1 L573"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-574",
      "type": "function",
      "name": "记录数据传输",
      "attributes": {
        "level": 2,
        "definition": "记录在数据使用语境下向第三方传输披露任何个人数据所适用的法律条件；记录在数据使用语境下接收个人数据的第三方。",
        "source_row": "G234 表5-1 L574"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-575",
      "type": "function",
      "name": "记录 DPIA 结果",
      "attributes": {
        "level": 2,
        "definition": "当数据使用与操作涉及个人数据处理时，记录数据保护影响评估（DPIA）结果。",
        "source_row": "G234 表5-1 L575"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-group-6",
      "type": "function",
      "name": "规则与政策文档",
      "attributes": {
        "level": 1,
        "definition": "规则与政策文档功能组；不是流程阶段",
        "reference_row": 4,
        "reference_column": 0,
        "g234:slot": "6"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-576",
      "type": "function",
      "name": "记录业务规则",
      "attributes": {
        "level": 2,
        "definition": "记录适用于数据的删除、质量及其他相关业务规则。",
        "source_row": "G234 表5-1 L576"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-577",
      "type": "function",
      "name": "记录数据政策",
      "attributes": {
        "level": 2,
        "definition": "记录应由数据治理委员会执行的数据政策。",
        "source_row": "G234 表5-1 L577"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-group-7",
      "type": "function",
      "name": "数据问题文档",
      "attributes": {
        "level": 1,
        "definition": "数据问题文档功能组；不是流程阶段",
        "reference_row": 4,
        "reference_column": 1,
        "g234:slot": "7"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-578",
      "type": "function",
      "name": "记录业务数据问题",
      "attributes": {
        "level": 2,
        "definition": "记录业务问题及相关业务影响（定量与定性）。",
        "source_row": "G234 表5-1 L578"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-579",
      "type": "function",
      "name": "记录数据质量问题",
      "attributes": {
        "level": 2,
        "definition": "记录信息生命周期分析中识别的数据质量问题。记录差质量成本与改进数据质量的成本。",
        "source_row": "G234 表5-1 L579"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-group-8",
      "type": "function",
      "name": "业务资产与技术资产关联",
      "attributes": {
        "level": 1,
        "definition": "业务资产与技术资产关联功能组；不是流程阶段",
        "reference_row": 5,
        "reference_column": 0,
        "g234:slot": "8"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-580",
      "type": "function",
      "name": "记录业务术语表概念与其在信息系统中的实现之间的链接",
      "attributes": {
        "level": 2,
        "definition": "记录业务数据对象/数据元素/业务术语与应用/数据库/数据集/数据字段之间的链接。",
        "source_row": "G234 表5-1 L580"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-581",
      "type": "function",
      "name": "记录数据使用与支撑该使用的系统之间的链接",
      "attributes": {
        "level": 2,
        "definition": "记录数据处理活动与参与该数据使用的应用/数据库之间的链接。",
        "source_row": "G234 表5-1 L581"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-582",
      "type": "function",
      "name": "把业务规则链接到数据处理活动",
      "attributes": {
        "level": 2,
        "definition": "记录数据使用和/或操作中涉及的业务规则。",
        "source_row": "G234 表5-1 L582"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-583",
      "type": "function",
      "name": "把业务规则链接到业务数据元素",
      "attributes": {
        "level": 2,
        "definition": "记录每条业务规则要评估的数据元素。",
        "source_row": "G234 表5-1 L583"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-group-9",
      "type": "function",
      "name": "元数据存储库设计",
      "attributes": {
        "level": 1,
        "definition": "元数据存储库设计功能组；不是流程阶段",
        "reference_row": 5,
        "reference_column": 1,
        "g234:slot": "9"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-584",
      "type": "function",
      "name": "设计元数据存储库模型",
      "attributes": {
        "level": 2,
        "definition": "设计元数据存储库的底层数据模型。",
        "source_row": "G234 表5-1 L584"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-585",
      "type": "function",
      "name": "设计元数据访问模型",
      "attributes": {
        "level": 2,
        "definition": "定义、管理与控制元数据的访问方式。",
        "source_row": "G234 表5-1 L585"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-586",
      "type": "function",
      "name": "设计工作流",
      "attributes": {
        "level": 2,
        "definition": "定义评审与校验元数据的工作流与流程，以保证元数据的一致性与完整性，或简化元数据采集（在元数据入口层面最少控制）。",
        "source_row": "G234 表5-1 L586"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-group-10",
      "type": "function",
      "name": "沟通与培训",
      "attributes": {
        "level": 1,
        "definition": "沟通与培训功能组；不是流程阶段",
        "reference_row": 6,
        "reference_column": 0,
        "g234:slot": "10"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-587",
      "type": "function",
      "name": "培训最终用户",
      "attributes": {
        "level": 2,
        "definition": "培训最终用户，促进元数据管理流程与工具的采用。",
        "source_row": "G234 表5-1 L587"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-588",
      "type": "function",
      "name": "沟通存储库中当前可用的元数据",
      "attributes": {
        "level": 2,
        "definition": "向广泛受众说明已记录的元数据范围，以及如何用它为组织创造价值。",
        "source_row": "G234 表5-1 L588"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-function-589",
      "type": "function",
      "name": "沟通可用元数据的使用情况",
      "attributes": {
        "level": 2,
        "definition": "向广泛受众说明已记录元数据的实际使用情况，以提升认知。",
        "source_row": "G234 表5-1 L589"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-role-1",
      "type": "role",
      "name": "数据所有者",
      "attributes": {
        "responsibility": "按数据域参与元数据治理；具体授权待项目确认"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-role-2",
      "type": "role",
      "name": "数据管家",
      "attributes": {
        "responsibility": "按数据域参与元数据治理；具体授权待项目确认"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-role-3",
      "type": "role",
      "name": "数据保管人",
      "attributes": {
        "responsibility": "按数据域参与元数据治理；具体授权待项目确认"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-role-4",
      "type": "role",
      "name": "数据保护官",
      "attributes": {
        "responsibility": "按数据域参与元数据治理；具体授权待项目确认"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "scope-business-group-1",
      "type": "visually_contains",
      "source": "business-functions",
      "target": "business-group-1",
      "label": "参考模型范围的视觉包含；不表示组织归属",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-560",
      "type": "decomposes",
      "source": "business-group-1",
      "target": "business-function-560",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-561",
      "type": "decomposes",
      "source": "business-group-1",
      "target": "business-function-561",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-562",
      "type": "decomposes",
      "source": "business-group-1",
      "target": "business-function-562",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-563",
      "type": "decomposes",
      "source": "business-group-1",
      "target": "business-function-563",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-564",
      "type": "decomposes",
      "source": "business-group-1",
      "target": "business-function-564",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "scope-business-group-2",
      "type": "visually_contains",
      "source": "business-functions",
      "target": "business-group-2",
      "label": "参考模型范围的视觉包含；不表示组织归属",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-565",
      "type": "decomposes",
      "source": "business-group-2",
      "target": "business-function-565",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-566",
      "type": "decomposes",
      "source": "business-group-2",
      "target": "business-function-566",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-567",
      "type": "decomposes",
      "source": "business-group-2",
      "target": "business-function-567",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "scope-business-group-3",
      "type": "visually_contains",
      "source": "business-functions",
      "target": "business-group-3",
      "label": "参考模型范围的视觉包含；不表示组织归属",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-568",
      "type": "decomposes",
      "source": "business-group-3",
      "target": "business-function-568",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-569",
      "type": "decomposes",
      "source": "business-group-3",
      "target": "business-function-569",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "scope-business-group-4",
      "type": "visually_contains",
      "source": "business-functions",
      "target": "business-group-4",
      "label": "参考模型范围的视觉包含；不表示组织归属",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-570",
      "type": "decomposes",
      "source": "business-group-4",
      "target": "business-function-570",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-571",
      "type": "decomposes",
      "source": "business-group-4",
      "target": "business-function-571",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-572",
      "type": "decomposes",
      "source": "business-group-4",
      "target": "business-function-572",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "scope-business-group-5",
      "type": "visually_contains",
      "source": "business-functions",
      "target": "business-group-5",
      "label": "参考模型范围的视觉包含；不表示组织归属",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-573",
      "type": "decomposes",
      "source": "business-group-5",
      "target": "business-function-573",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-574",
      "type": "decomposes",
      "source": "business-group-5",
      "target": "business-function-574",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-575",
      "type": "decomposes",
      "source": "business-group-5",
      "target": "business-function-575",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "scope-business-group-6",
      "type": "visually_contains",
      "source": "business-functions",
      "target": "business-group-6",
      "label": "参考模型范围的视觉包含；不表示组织归属",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-576",
      "type": "decomposes",
      "source": "business-group-6",
      "target": "business-function-576",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-577",
      "type": "decomposes",
      "source": "business-group-6",
      "target": "business-function-577",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "scope-business-group-7",
      "type": "visually_contains",
      "source": "business-functions",
      "target": "business-group-7",
      "label": "参考模型范围的视觉包含；不表示组织归属",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-578",
      "type": "decomposes",
      "source": "business-group-7",
      "target": "business-function-578",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-579",
      "type": "decomposes",
      "source": "business-group-7",
      "target": "business-function-579",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "scope-business-group-8",
      "type": "visually_contains",
      "source": "business-functions",
      "target": "business-group-8",
      "label": "参考模型范围的视觉包含；不表示组织归属",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-580",
      "type": "decomposes",
      "source": "business-group-8",
      "target": "business-function-580",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-581",
      "type": "decomposes",
      "source": "business-group-8",
      "target": "business-function-581",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-582",
      "type": "decomposes",
      "source": "business-group-8",
      "target": "business-function-582",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-583",
      "type": "decomposes",
      "source": "business-group-8",
      "target": "business-function-583",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "scope-business-group-9",
      "type": "visually_contains",
      "source": "business-functions",
      "target": "business-group-9",
      "label": "参考模型范围的视觉包含；不表示组织归属",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-584",
      "type": "decomposes",
      "source": "business-group-9",
      "target": "business-function-584",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-585",
      "type": "decomposes",
      "source": "business-group-9",
      "target": "business-function-585",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-586",
      "type": "decomposes",
      "source": "business-group-9",
      "target": "business-function-586",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "scope-business-group-10",
      "type": "visually_contains",
      "source": "business-functions",
      "target": "business-group-10",
      "label": "参考模型范围的视觉包含；不表示组织归属",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-587",
      "type": "decomposes",
      "source": "business-group-10",
      "target": "business-function-587",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-588",
      "type": "decomposes",
      "source": "business-group-10",
      "target": "business-function-588",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-business-function-589",
      "type": "decomposes",
      "source": "business-group-10",
      "target": "business-function-589",
      "label": "业务职责分解",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "team-metadata-role-1",
      "type": "visually_contains",
      "source": "metadata-team",
      "target": "metadata-role-1",
      "label": "角色属于图中的团队分组；不表示人事汇报",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "team-metadata-role-2",
      "type": "visually_contains",
      "source": "metadata-team",
      "target": "metadata-role-2",
      "label": "角色属于图中的团队分组；不表示人事汇报",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "team-metadata-role-3",
      "type": "visually_contains",
      "source": "metadata-team",
      "target": "metadata-role-3",
      "label": "角色属于图中的团队分组；不表示人事汇报",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "team-metadata-role-4",
      "type": "visually_contains",
      "source": "metadata-team",
      "target": "metadata-role-4",
      "label": "角色属于图中的团队分组；不表示人事汇报",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-metadata-business-function-map",
    "artifact_id": "functional-decomposition-diagram",
    "profile_id": "metadata-business-function-map",
    "title": "元数据业务功能参考地图",
    "entity_ids": [
      "metadata-team",
      "business-functions",
      "business-group-1",
      "business-function-560",
      "business-function-561",
      "business-function-562",
      "business-function-563",
      "business-function-564",
      "business-group-2",
      "business-function-565",
      "business-function-566",
      "business-function-567",
      "business-group-3",
      "business-function-568",
      "business-function-569",
      "business-group-4",
      "business-function-570",
      "business-function-571",
      "business-function-572",
      "business-group-5",
      "business-function-573",
      "business-function-574",
      "business-function-575",
      "business-group-6",
      "business-function-576",
      "business-function-577",
      "business-group-7",
      "business-function-578",
      "business-function-579",
      "business-group-8",
      "business-function-580",
      "business-function-581",
      "business-function-582",
      "business-function-583",
      "business-group-9",
      "business-function-584",
      "business-function-585",
      "business-function-586",
      "business-group-10",
      "business-function-587",
      "business-function-588",
      "business-function-589",
      "metadata-role-1",
      "metadata-role-2",
      "metadata-role-3",
      "metadata-role-4"
    ],
    "relationship_ids": [
      "scope-business-group-1",
      "part-business-function-560",
      "part-business-function-561",
      "part-business-function-562",
      "part-business-function-563",
      "part-business-function-564",
      "scope-business-group-2",
      "part-business-function-565",
      "part-business-function-566",
      "part-business-function-567",
      "scope-business-group-3",
      "part-business-function-568",
      "part-business-function-569",
      "scope-business-group-4",
      "part-business-function-570",
      "part-business-function-571",
      "part-business-function-572",
      "scope-business-group-5",
      "part-business-function-573",
      "part-business-function-574",
      "part-business-function-575",
      "scope-business-group-6",
      "part-business-function-576",
      "part-business-function-577",
      "scope-business-group-7",
      "part-business-function-578",
      "part-business-function-579",
      "scope-business-group-8",
      "part-business-function-580",
      "part-business-function-581",
      "part-business-function-582",
      "part-business-function-583",
      "scope-business-group-9",
      "part-business-function-584",
      "part-business-function-585",
      "part-business-function-586",
      "scope-business-group-10",
      "part-business-function-587",
      "part-business-function-588",
      "part-business-function-589",
      "team-metadata-role-1",
      "team-metadata-role-2",
      "team-metadata-role-3",
      "team-metadata-role-4"
    ],
    "analysis": "原料：社区服务预约与补贴数据需要共享术语、字典、隐私和质量文档。以G234完整功能表为评审清单保留参考结构，再按业务需求逐项决定适用性。本图是可裁剪参考模型，未声明全部已实施；定义来自源表译文，保留版本与翻译限制。",
    "legend": "同一ID表示同一对象；箭头依关系标签；未知不等于不存在；示例未获业务批准。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile metadata-business-function-map --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile metadata-business-function-map --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
