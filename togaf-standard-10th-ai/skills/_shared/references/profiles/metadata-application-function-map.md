# 元数据应用功能参考地图

`profile_id`: metadata-application-function-map；`artifact_id`: functional-decomposition-diagram；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G234 §5.2；G234/fig5-2；references/source-tables/metadata-functions.json。

## 构图与定义状态

表示族：`metadata-map`；输出：`diagram`。规范版本：2.3。

{
  "id": "metadata-application-function-map",
  "version": "2.3",
  "source_verified": false,
  "layout_notes": "按已核查的来源结构参数化；参考图与业务实例的验收分别进行。",
  "structure": "application",
  "source_assets": [
    {
      "path": "reviews/source-template-bases/G234-fig5-2-local-en.png",
      "figure_id": "G234/fig5-2",
      "pdf_page": 34,
      "original_asset": "figs/g234e_fig5-2_en.png",
      "sha256": "00c5e8212648944daa5d071f77a5829dc6187d4ee3eb87ec516ea36227470c6e",
      "source_version": "G234e.pdf",
      "source_pdf_sha256": "34a1c590f938bf915182fe5bbe00d1d68f9a3e948697b5500ce7c5a9494f77e7",
      "verification_scope": "actual image opened; structural layout and readable labels compared; tiny embedded screenshots excluded"
    }
  ],
  "structure_basis": "实际打开可信来源图；主图保留容器和组带，详细属性按同一稳定ID可见呈现；空间位置不增加语义关系。",
  "reference_rows": [
    1,
    2,
    2,
    3,
    4,
    1
  ]
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
      "id": "application-functions",
      "type": "visual_container",
      "name": "元数据管理应用功能",
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
      "id": "application-group-1",
      "type": "function",
      "name": "采集",
      "attributes": {
        "level": 1,
        "definition": "采集功能组；不是流程阶段",
        "reference_row": 1,
        "reference_column": 0,
        "g234:slot": "acquisition"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-function-641",
      "type": "function",
      "name": "元数据创建、修订与删除",
      "attributes": {
        "level": 2,
        "definition": "创建并维护元数据对象，包括（但不限于）：\n• 数据术语表：业务数据对象、业务数据元素、业务术语、删除/保留日期\n• 数据字典：环境、应用（及相关技术）、数据集（数据库）、表、列\n• 数据使用：数据处理活动、数据接收方、数据传输、数据保护影响评估、数据提供方、数据访问与权限、指向外部文档参考的 URL 链接\n• 数据分类：数据保密性分类、数据隐私分类、业务价值分类、定义自定义元数据分类维度\n• 规则与政策：数据政策、业务数据质量规则\n• 问题：业务数据问题（含相关业务问题与业务影响）、按数据质量规则执行后报告的数据质量问题\n• 治理资产：元数据的逻辑分组，包括（但不限于）主题域（如保单、理赔、产品）、业务领域（如家庭、汽车、旅行、健康）、地理区域（如意大利、法国、西班牙、巴黎）；数据域，即两个或以上元数据分组的组合；数据管家、数据所有者、数据经理、数据隐私官、数据保管人、应用所有者\n• 数据质量规则执行：技术数据质量规则。",
        "source_row": "G234 表5-2 L641",
        "g234:reference-order": 641,
        "asset_categories": [
          "数据术语表",
          "数据字典",
          "数据使用",
          "数据分类",
          "规则与政策",
          "问题",
          "治理资产",
          "数据质量规则执行"
        ]
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-function-642",
      "type": "function",
      "name": "元数据分类",
      "attributes": {
        "level": 2,
        "definition": "对元数据分类的能力：数据保密性分类；数据隐私分类；定义自定义元数据分类维度。",
        "source_row": "G234 表5-2 L642",
        "g234:reference-order": 642
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-function-643",
      "type": "function",
      "name": "元数据关联",
      "attributes": {
        "level": 2,
        "definition": "链接元数据资产，以描述数据的完整价值链与数据血缘。",
        "source_row": "G234 表5-2 L643",
        "g234:reference-order": 643
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-function-644",
      "type": "function",
      "name": "元数据推断",
      "attributes": {
        "level": 2,
        "definition": "通过自动化过程（如机器学习或人工智能（AI）算法）记录元数据；例如（但不限于）：自动处理可用数据以发现元数据关系；从模式中识别元数据（电子邮件、电话号码、信用卡等）；识别数据之间的关系（相同值、分布等）；从字典中识别元数据（公司名称、城市、名字、姓氏、同义词等）。",
        "source_row": "G234 表5-2 L644",
        "g234:reference-order": 644
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-function-645",
      "type": "function",
      "name": "数据质量规则执行",
      "attributes": {
        "level": 2,
        "definition": "执行元数据存储库中定义的数据质量规则，并捕获其结果。",
        "source_row": "G234 表5-2 L645",
        "g234:reference-order": 645
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-group-2",
      "type": "function",
      "name": "治理",
      "attributes": {
        "level": 1,
        "definition": "治理功能组；不是流程阶段",
        "reference_row": 2,
        "reference_column": 0,
        "g234:slot": "governance"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-function-646",
      "type": "function",
      "name": "工作流校验",
      "attributes": {
        "level": 2,
        "definition": "创建工作流，可视化状态与任务。",
        "source_row": "G234 表5-2 L646",
        "g234:reference-order": 0
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-function-647",
      "type": "function",
      "name": "任务分配",
      "attributes": {
        "level": 2,
        "definition": "向人员分配任务。",
        "source_row": "G234 表5-2 L647",
        "g234:reference-order": 2
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-function-648",
      "type": "function",
      "name": "影响分析",
      "attributes": {
        "level": 2,
        "definition": "查看变更影响。（例如，如果我更改业务定义，有多少技术定义基于它？）",
        "source_row": "G234 表5-2 L648",
        "g234:reference-order": 1
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-function-649",
      "type": "function",
      "name": "元数据活动监控",
      "attributes": {
        "level": 2,
        "definition": "报告元数据使用情况。",
        "source_row": "G234 表5-2 L649",
        "g234:reference-order": 3
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-group-3",
      "type": "function",
      "name": "报表",
      "attributes": {
        "level": 1,
        "definition": "报表功能组；不是流程阶段",
        "reference_row": 2,
        "reference_column": 1,
        "g234:slot": "reporting"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-function-650",
      "type": "function",
      "name": "数据合规报表",
      "attributes": {
        "level": 2,
        "definition": "可视化端到端数据生命周期（数据起源、数据转换、数据传输、数据分类），以支持监管要求。",
        "source_row": "G234 表5-2 L650",
        "g234:reference-order": 650
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-function-651",
      "type": "function",
      "name": "数据文档报表",
      "attributes": {
        "level": 2,
        "definition": "可视化存储库内的元数据完成情况；可视化元数据关联；度量元数据质量并在组织内共享。",
        "source_row": "G234 表5-2 L651",
        "g234:reference-order": 651
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-function-652",
      "type": "function",
      "name": "数据问责报表",
      "attributes": {
        "level": 2,
        "definition": "以报表能力可视化组织内谁对数据负责。",
        "source_row": "G234 表5-2 L652",
        "g234:reference-order": 652
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-function-653",
      "type": "function",
      "name": "数据质量报表",
      "attributes": {
        "level": 2,
        "definition": "按时间（历史与当前）度量数据质量，并在组织内共享。",
        "source_row": "G234 表5-2 L653",
        "g234:reference-order": 653
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-function-654",
      "type": "function",
      "name": "元数据搜索",
      "attributes": {
        "level": 2,
        "definition": "对元数据进行多条件搜索；对元数据进行全文搜索（类似 Google™）；带自动补全的元数据搜索。",
        "source_row": "G234 表5-2 L654",
        "g234:reference-order": 654
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-group-4",
      "type": "function",
      "name": "参考数据管理",
      "attributes": {
        "level": 1,
        "definition": "参考数据管理功能组；不是流程阶段",
        "reference_row": 3,
        "reference_column": 0,
        "g234:slot": "reference-data"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-function-655",
      "type": "function",
      "name": "值列表管理（类别列表、代码列表等）",
      "attributes": {
        "level": 2,
        "definition": "创建并维护规范化的值列表（类别列表、代码列表等）；管理参考数据（值列表）。",
        "source_row": "G234 表5-2 L655",
        "g234:reference-order": 655
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-group-5",
      "type": "function",
      "name": "管理",
      "attributes": {
        "level": 1,
        "definition": "管理功能组；不是流程阶段",
        "reference_row": 4,
        "reference_column": 0,
        "g234:slot": "administration"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-function-656",
      "type": "function",
      "name": "环境管理",
      "attributes": {
        "level": 2,
        "definition": "管理多个环境，每个环境有自己的治理（如工作流校验）与管理（如访问管理、数据库版本管理）设置。",
        "source_row": "G234 表5-2 L656",
        "g234:reference-order": 656
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-function-657",
      "type": "function",
      "name": "访问管理",
      "attributes": {
        "level": 2,
        "definition": "管理、创建、删除、更新元数据访问权限；创建用户与组，并根据角色授予元数据授权（包括批处理或用户角色）。",
        "source_row": "G234 表5-2 L657",
        "g234:reference-order": 657
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-function-658",
      "type": "function",
      "name": "国际化与本地化",
      "attributes": {
        "level": 2,
        "definition": "提供使元数据管理工具适应不同语言和本地要求的手段。",
        "source_row": "G234 表5-2 L658",
        "g234:reference-order": 658
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-function-659",
      "type": "function",
      "name": "事件日志管理",
      "attributes": {
        "level": 2,
        "definition": "记录系统中的任何事件。保留元数据修改的历史、来源与作者。",
        "source_row": "G234 表5-2 L659",
        "g234:reference-order": 659
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-function-660",
      "type": "function",
      "name": "数据库版本管理",
      "attributes": {
        "level": 2,
        "definition": "支持元数据数据库的版本管理。",
        "source_row": "G234 表5-2 L660",
        "g234:reference-order": 660
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-group-6",
      "type": "function",
      "name": "元数据集成",
      "attributes": {
        "level": 1,
        "definition": "元数据集成功能组；不是流程阶段",
        "reference_row": 1,
        "reference_column": 1,
        "g234:slot": "integration"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-function-661",
      "type": "function",
      "name": "元数据查询",
      "attributes": {
        "level": 2,
        "definition": "使用原生 SQL 或任何其他查询语言或接口（如 API）查询存储库中的元数据资产。",
        "source_row": "G234 表5-2 L661",
        "g234:reference-order": 661
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-function-662",
      "type": "function",
      "name": "批量导入",
      "attributes": {
        "level": 2,
        "definition": "从文件（如 CSV、JSON、XML）或通过应用接口（如 API）把多条元数据导入元数据存储库。",
        "source_row": "G234 表5-2 L662",
        "g234:reference-order": 662
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-function-663",
      "type": "function",
      "name": "批量导出",
      "attributes": {
        "level": 2,
        "definition": "以非专有文件格式（如 CSV）、通过 API 或任何其他应用接口从存储库导出多条元数据。",
        "source_row": "G234 表5-2 L663",
        "g234:reference-order": 663
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "application-function-664",
      "type": "function",
      "name": "事件订阅",
      "attributes": {
        "level": 2,
        "definition": "监听来自事件代理的一个或多个事件。",
        "source_row": "G234 表5-2 L664",
        "g234:reference-order": 664
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "scope-application-group-1",
      "type": "visually_contains",
      "source": "application-functions",
      "target": "application-group-1",
      "label": "参考模型范围的视觉包含；不表示组织归属",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-application-function-641",
      "type": "decomposes",
      "source": "application-group-1",
      "target": "application-function-641",
      "label": "应用功能分解；不表示调用顺序",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-application-function-642",
      "type": "decomposes",
      "source": "application-group-1",
      "target": "application-function-642",
      "label": "应用功能分解；不表示调用顺序",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-application-function-643",
      "type": "decomposes",
      "source": "application-group-1",
      "target": "application-function-643",
      "label": "应用功能分解；不表示调用顺序",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-application-function-644",
      "type": "decomposes",
      "source": "application-group-1",
      "target": "application-function-644",
      "label": "应用功能分解；不表示调用顺序",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-application-function-645",
      "type": "decomposes",
      "source": "application-group-1",
      "target": "application-function-645",
      "label": "应用功能分解；不表示调用顺序",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "scope-application-group-2",
      "type": "visually_contains",
      "source": "application-functions",
      "target": "application-group-2",
      "label": "参考模型范围的视觉包含；不表示组织归属",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-application-function-646",
      "type": "decomposes",
      "source": "application-group-2",
      "target": "application-function-646",
      "label": "应用功能分解；不表示调用顺序",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-application-function-647",
      "type": "decomposes",
      "source": "application-group-2",
      "target": "application-function-647",
      "label": "应用功能分解；不表示调用顺序",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-application-function-648",
      "type": "decomposes",
      "source": "application-group-2",
      "target": "application-function-648",
      "label": "应用功能分解；不表示调用顺序",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-application-function-649",
      "type": "decomposes",
      "source": "application-group-2",
      "target": "application-function-649",
      "label": "应用功能分解；不表示调用顺序",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "scope-application-group-3",
      "type": "visually_contains",
      "source": "application-functions",
      "target": "application-group-3",
      "label": "参考模型范围的视觉包含；不表示组织归属",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-application-function-650",
      "type": "decomposes",
      "source": "application-group-3",
      "target": "application-function-650",
      "label": "应用功能分解；不表示调用顺序",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-application-function-651",
      "type": "decomposes",
      "source": "application-group-3",
      "target": "application-function-651",
      "label": "应用功能分解；不表示调用顺序",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-application-function-652",
      "type": "decomposes",
      "source": "application-group-3",
      "target": "application-function-652",
      "label": "应用功能分解；不表示调用顺序",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-application-function-653",
      "type": "decomposes",
      "source": "application-group-3",
      "target": "application-function-653",
      "label": "应用功能分解；不表示调用顺序",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-application-function-654",
      "type": "decomposes",
      "source": "application-group-3",
      "target": "application-function-654",
      "label": "应用功能分解；不表示调用顺序",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "scope-application-group-4",
      "type": "visually_contains",
      "source": "application-functions",
      "target": "application-group-4",
      "label": "参考模型范围的视觉包含；不表示组织归属",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-application-function-655",
      "type": "decomposes",
      "source": "application-group-4",
      "target": "application-function-655",
      "label": "应用功能分解；不表示调用顺序",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "scope-application-group-5",
      "type": "visually_contains",
      "source": "application-functions",
      "target": "application-group-5",
      "label": "参考模型范围的视觉包含；不表示组织归属",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-application-function-656",
      "type": "decomposes",
      "source": "application-group-5",
      "target": "application-function-656",
      "label": "应用功能分解；不表示调用顺序",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-application-function-657",
      "type": "decomposes",
      "source": "application-group-5",
      "target": "application-function-657",
      "label": "应用功能分解；不表示调用顺序",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-application-function-658",
      "type": "decomposes",
      "source": "application-group-5",
      "target": "application-function-658",
      "label": "应用功能分解；不表示调用顺序",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-application-function-659",
      "type": "decomposes",
      "source": "application-group-5",
      "target": "application-function-659",
      "label": "应用功能分解；不表示调用顺序",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-application-function-660",
      "type": "decomposes",
      "source": "application-group-5",
      "target": "application-function-660",
      "label": "应用功能分解；不表示调用顺序",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "scope-application-group-6",
      "type": "visually_contains",
      "source": "application-functions",
      "target": "application-group-6",
      "label": "参考模型范围的视觉包含；不表示组织归属",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-application-function-661",
      "type": "decomposes",
      "source": "application-group-6",
      "target": "application-function-661",
      "label": "应用功能分解；不表示调用顺序",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-application-function-662",
      "type": "decomposes",
      "source": "application-group-6",
      "target": "application-function-662",
      "label": "应用功能分解；不表示调用顺序",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-application-function-663",
      "type": "decomposes",
      "source": "application-group-6",
      "target": "application-function-663",
      "label": "应用功能分解；不表示调用顺序",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "part-application-function-664",
      "type": "decomposes",
      "source": "application-group-6",
      "target": "application-function-664",
      "label": "应用功能分解；不表示调用顺序",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-metadata-application-function-map",
    "artifact_id": "functional-decomposition-diagram",
    "profile_id": "metadata-application-function-map",
    "title": "元数据应用功能参考地图",
    "entity_ids": [
      "application-functions",
      "application-group-1",
      "application-function-641",
      "application-function-642",
      "application-function-643",
      "application-function-644",
      "application-function-645",
      "application-group-2",
      "application-function-646",
      "application-function-647",
      "application-function-648",
      "application-function-649",
      "application-group-3",
      "application-function-650",
      "application-function-651",
      "application-function-652",
      "application-function-653",
      "application-function-654",
      "application-group-4",
      "application-function-655",
      "application-group-5",
      "application-function-656",
      "application-function-657",
      "application-function-658",
      "application-function-659",
      "application-function-660",
      "application-group-6",
      "application-function-661",
      "application-function-662",
      "application-function-663",
      "application-function-664"
    ],
    "relationship_ids": [
      "scope-application-group-1",
      "part-application-function-641",
      "part-application-function-642",
      "part-application-function-643",
      "part-application-function-644",
      "part-application-function-645",
      "scope-application-group-2",
      "part-application-function-646",
      "part-application-function-647",
      "part-application-function-648",
      "part-application-function-649",
      "scope-application-group-3",
      "part-application-function-650",
      "part-application-function-651",
      "part-application-function-652",
      "part-application-function-653",
      "part-application-function-654",
      "scope-application-group-4",
      "part-application-function-655",
      "scope-application-group-5",
      "part-application-function-656",
      "part-application-function-657",
      "part-application-function-658",
      "part-application-function-659",
      "part-application-function-660",
      "scope-application-group-6",
      "part-application-function-661",
      "part-application-function-662",
      "part-application-function-663",
      "part-application-function-664"
    ],
    "analysis": "原料：社区服务预约与补贴数据需要共享术语、字典、隐私和质量文档。以G234完整功能表为评审清单保留参考结构，再按业务需求逐项决定适用性。本图是可裁剪参考模型，未声明全部已实施；定义来自源表译文，保留版本与翻译限制。",
    "legend": "同一ID表示同一对象；箭头依关系标签；未知不等于不存在；示例未获业务批准。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile metadata-application-function-map --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile metadata-application-function-map --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
