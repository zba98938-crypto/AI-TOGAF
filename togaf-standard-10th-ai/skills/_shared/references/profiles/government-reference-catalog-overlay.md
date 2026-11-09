# 政府参考目录与本地职责覆盖

`profile_id`: government-reference-catalog-overlay；`artifact_id`: government-reference-tailoring；主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G21D §1.3、§2.1–12.1、§8.1、§11.1。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-reference-1。

{
  "id": "government-reference-catalog-overlay",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "图形保留显式部门—功能—服务分类结构；表格保持完整源字段/本地判断，均不声称原图已通过。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:government_overlay。关系类型：。

```json
{
  "entities": {
    "guide:government_overlay": [
      "reference_id",
      "reference_kind",
      "reference_path",
      "reference_description",
      "reference_version",
      "local_object_ids",
      "mapping_type",
      "applicability",
      "reason",
      "dependencies",
      "impact_scope",
      "source_locator",
      "review_action"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 同名养老基金管理保留两个路径和两个职责
- 源目录11部门，不虚构第12项
- 排除必须有范围理由
- 不得将参考分类当能力分解/组织汇报

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "明确虚构项目裁剪与真实参考来源分离；源图视觉核验另记。",
  "raw_input": "examples/addenda/reference-models/raw-business-materials.json",
  "analysis_path": "examples/addenda/reference-models/analysis.md",
  "sources": [
    {
      "id": "raw",
      "kind": "example",
      "description": "虚构松川市养老服务数字化试点；实际原料见本包raw-business-materials.json；补充场景参数均明示，不代表真实审批。",
      "locator": "raw-business-materials.json"
    },
    {
      "id": "grm",
      "kind": "local-translation",
      "description": "G21D本地正文目录摘录，官方定义/图形复核另记；保留参考身份。",
      "locator": "references/source-tables/government-reference-catalog.json"
    },
    {
      "id": "dbrm",
      "kind": "local-translation",
      "description": "G21H本地正文五表摘录；原始空格/破折号保留，项目裁剪与源映射分离。",
      "locator": "references/source-tables/dbrm-reference-mappings.json"
    }
  ],
  "entities": [
    {
      "id": "GM-G21D-S02",
      "type": "guide:government_overlay",
      "name": "国际事务与贸易",
      "attributes": {
        "reference_id": "G21D-S02",
        "reference_kind": "sector",
        "reference_path": [
          "国际事务与贸易"
        ],
        "reference_description": "政府为促进与国际经济体的财政支持与贸易而开展的活动，并涉及政策、援助计划、条约与外交关系的实施。",
        "reference_version": "2ab155c82bbca9ab1f78534fd977dca6e48608dc1ce82da1a720af400f3148bf",
        "local_object_ids": [],
        "mapping_type": "excluded-from-project-scope",
        "applicability": "out-of-scope",
        "reason": "本轮只覆盖养老资产与待遇服务，其他部门未纳入；不推断其不存在",
        "dependencies": [],
        "impact_scope": "未评估",
        "source_locator": "G21D §2 / 表1-1:209",
        "review_action": "未来扩范围时重新评估"
      },
      "evidence": [
        "raw",
        "grm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started",
      "scope_id": "ref-sector-G21D-S02"
    },
    {
      "id": "GM-G21D-S03",
      "type": "guide:government_overlay",
      "name": "国防与安全",
      "attributes": {
        "reference_id": "G21D-S03",
        "reference_kind": "sector",
        "reference_path": [
          "国防与安全"
        ],
        "reference_description": "对应部队、武器及相关实体的研究、维护、装备、采购与开发；也包括向所有现役与非现役文职人员与军人支付的薪酬与福利。",
        "reference_version": "2ab155c82bbca9ab1f78534fd977dca6e48608dc1ce82da1a720af400f3148bf",
        "local_object_ids": [],
        "mapping_type": "excluded-from-project-scope",
        "applicability": "out-of-scope",
        "reason": "本轮只覆盖养老资产与待遇服务，其他部门未纳入；不推断其不存在",
        "dependencies": [],
        "impact_scope": "未评估",
        "source_locator": "G21D §3 / 表1-1:280",
        "review_action": "未来扩范围时重新评估"
      },
      "evidence": [
        "raw",
        "grm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started",
      "scope_id": "ref-sector-G21D-S03"
    },
    {
      "id": "GM-G21D-S04",
      "type": "guide:government_overlay",
      "name": "一般政府与地方服务",
      "attributes": {
        "reference_id": "G21D-S04",
        "reference_kind": "sector",
        "reference_path": [
          "一般政府与地方服务"
        ],
        "reference_description": "提供一般客户服务与运营，包括登记、许可、申请、劳动力规划、社会服务、劳动权利管理与地方服务。",
        "reference_version": "2ab155c82bbca9ab1f78534fd977dca6e48608dc1ce82da1a720af400f3148bf",
        "local_object_ids": [],
        "mapping_type": "excluded-from-project-scope",
        "applicability": "out-of-scope",
        "reason": "本轮只覆盖养老资产与待遇服务，其他部门未纳入；不推断其不存在",
        "dependencies": [],
        "impact_scope": "未评估",
        "source_locator": "G21D §4 / 表1-1:355",
        "review_action": "未来扩范围时重新评估"
      },
      "evidence": [
        "raw",
        "grm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started",
      "scope_id": "ref-sector-G21D-S04"
    },
    {
      "id": "GM-G21D-S05",
      "type": "guide:government_overlay",
      "name": "青少年与教育",
      "attributes": {
        "reference_id": "G21D-S05",
        "reference_kind": "sector",
        "reference_path": [
          "青少年与教育"
        ],
        "reference_description": "对应早期教育、小学、中学、高等教育与特殊教育的教育项目；儿童社会服务、保护及相关儿童与青少年服务；以及政府为促进教育开展的技能或培训活动。",
        "reference_version": "2ab155c82bbca9ab1f78534fd977dca6e48608dc1ce82da1a720af400f3148bf",
        "local_object_ids": [],
        "mapping_type": "excluded-from-project-scope",
        "applicability": "out-of-scope",
        "reason": "本轮只覆盖养老资产与待遇服务，其他部门未纳入；不推断其不存在",
        "dependencies": [],
        "impact_scope": "未评估",
        "source_locator": "G21D §5 / 表1-1:461",
        "review_action": "未来扩范围时重新评估"
      },
      "evidence": [
        "raw",
        "grm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started",
      "scope_id": "ref-sector-G21D-S05"
    },
    {
      "id": "GM-G21D-S06",
      "type": "guide:government_overlay",
      "name": "健康与社区福祉",
      "attributes": {
        "reference_id": "G21D-S06",
        "reference_kind": "sector",
        "reference_path": [
          "健康与社区福祉"
        ],
        "reference_description": "涵盖向个人与家庭提供的医疗与护理治理、战略与照护服务，研究，以及为保障心理与身体健康而提供的医院与社区服务。",
        "reference_version": "2ab155c82bbca9ab1f78534fd977dca6e48608dc1ce82da1a720af400f3148bf",
        "local_object_ids": [],
        "mapping_type": "excluded-from-project-scope",
        "applicability": "out-of-scope",
        "reason": "本轮只覆盖养老资产与待遇服务，其他部门未纳入；不推断其不存在",
        "dependencies": [],
        "impact_scope": "未评估",
        "source_locator": "G21D §6 / 表1-1:543",
        "review_action": "未来扩范围时重新评估"
      },
      "evidence": [
        "raw",
        "grm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started",
      "scope_id": "ref-sector-G21D-S06"
    },
    {
      "id": "GM-G21D-S07",
      "type": "guide:government_overlay",
      "name": "司法、治安与内政",
      "attributes": {
        "reference_id": "G21D-S07",
        "reference_kind": "sector",
        "reference_path": [
          "司法、治安与内政"
        ],
        "reference_description": "涵盖司法、检察、与保护资金相关的支出、执法服务，以及刑事司法成本——包括监禁、监督、假释与罪犯康复——的总成本。",
        "reference_version": "2ab155c82bbca9ab1f78534fd977dca6e48608dc1ce82da1a720af400f3148bf",
        "local_object_ids": [],
        "mapping_type": "excluded-from-project-scope",
        "applicability": "out-of-scope",
        "reason": "本轮只覆盖养老资产与待遇服务，其他部门未纳入；不推断其不存在",
        "dependencies": [],
        "impact_scope": "未评估",
        "source_locator": "G21D §7 / 表1-1:648",
        "review_action": "未来扩范围时重新评估"
      },
      "evidence": [
        "raw",
        "grm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started",
      "scope_id": "ref-sector-G21D-S07"
    },
    {
      "id": "GM-G21D-S08",
      "type": "guide:government_overlay",
      "name": "财政",
      "attributes": {
        "reference_id": "G21D-S08",
        "reference_kind": "sector",
        "reference_path": [
          "财政"
        ],
        "reference_description": "对公共支出、收入、财务报告与审计保持控制，并为未来投资决策与财务规划提供方向。",
        "reference_version": "2ab155c82bbca9ab1f78534fd977dca6e48608dc1ce82da1a720af400f3148bf",
        "local_object_ids": [
          "LOCAL-PENSION",
          "LOCAL-ASSET"
        ],
        "mapping_type": "project-partial-coverage",
        "applicability": "applicable",
        "reason": "项目R01/R02职责映射；不意味着复制参考机构",
        "dependencies": [
          "LOCAL-ASSET→LOCAL-BENEFIT：投资/支付对账，项目关系待契约确认"
        ],
        "impact_scope": "试点养老办公室、资产组、待遇台",
        "source_locator": "G21D §8 / 表1-1:735",
        "review_action": "核对本地职责与参考细项的差异；不将同名记录合并"
      },
      "evidence": [
        "raw",
        "grm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started",
      "scope_id": "ref-sector-G21D-S08"
    },
    {
      "id": "GM-G21D-S09",
      "type": "guide:government_overlay",
      "name": "增长、住房与环境",
      "attributes": {
        "reference_id": "G21D-S09",
        "reference_kind": "sector",
        "reference_path": [
          "增长、住房与环境"
        ],
        "reference_description": "通过监管的许可与执法，确保对自然与城市环境的责任、提供核心基础设施，并保护公民的生活水平与安全的活动。",
        "reference_version": "2ab155c82bbca9ab1f78534fd977dca6e48608dc1ce82da1a720af400f3148bf",
        "local_object_ids": [],
        "mapping_type": "excluded-from-project-scope",
        "applicability": "out-of-scope",
        "reason": "本轮只覆盖养老资产与待遇服务，其他部门未纳入；不推断其不存在",
        "dependencies": [],
        "impact_scope": "未评估",
        "source_locator": "G21D §9 / 表1-1:828",
        "review_action": "未来扩范围时重新评估"
      },
      "evidence": [
        "raw",
        "grm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started",
      "scope_id": "ref-sector-G21D-S09"
    },
    {
      "id": "GM-G21D-S10",
      "type": "guide:government_overlay",
      "name": "政策、绩效、人口与创新",
      "attributes": {
        "reference_id": "G21D-S10",
        "reference_kind": "sector",
        "reference_path": [
          "政策、绩效、人口与创新"
        ],
        "reference_description": "涉及政府范围内的政策制定，提供人口统计数据以及对照基准的绩效数据以确保持续改进，并包含战略与长期规划，以识别未来风险、机遇与解决方案。",
        "reference_version": "2ab155c82bbca9ab1f78534fd977dca6e48608dc1ce82da1a720af400f3148bf",
        "local_object_ids": [],
        "mapping_type": "excluded-from-project-scope",
        "applicability": "out-of-scope",
        "reason": "本轮只覆盖养老资产与待遇服务，其他部门未纳入；不推断其不存在",
        "dependencies": [],
        "impact_scope": "未评估",
        "source_locator": "G21D §10 / 表1-1:929",
        "review_action": "未来扩范围时重新评估"
      },
      "evidence": [
        "raw",
        "grm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started",
      "scope_id": "ref-sector-G21D-S10"
    },
    {
      "id": "GM-G21D-S11",
      "type": "guide:government_overlay",
      "name": "共享服务",
      "attributes": {
        "reference_id": "G21D-S11",
        "reference_kind": "sector",
        "reference_path": [
          "共享服务"
        ],
        "reference_description": "代表公众协调并管理人员、沟通、财务与转型服务，以促进信息流转，并对人员、流程与技术实施监督，从而支持采购并与企业战略对齐。",
        "reference_version": "2ab155c82bbca9ab1f78534fd977dca6e48608dc1ce82da1a720af400f3148bf",
        "local_object_ids": [
          "LOCAL-PENSION",
          "LOCAL-BENEFIT"
        ],
        "mapping_type": "project-partial-coverage",
        "applicability": "applicable",
        "reason": "项目R01/R02职责映射；不意味着复制参考机构",
        "dependencies": [
          "LOCAL-ASSET→LOCAL-BENEFIT：投资/支付对账，项目关系待契约确认"
        ],
        "impact_scope": "试点养老办公室、资产组、待遇台",
        "source_locator": "G21D §11 / 表1-1:1010",
        "review_action": "核对本地职责与参考细项的差异；不将同名记录合并"
      },
      "evidence": [
        "raw",
        "grm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started",
      "scope_id": "ref-sector-G21D-S11"
    },
    {
      "id": "GM-G21D-S12",
      "type": "guide:government_overlay",
      "name": "交通与运营",
      "attributes": {
        "reference_id": "G21D-S12",
        "reference_kind": "sector",
        "reference_path": [
          "交通与运营"
        ],
        "reference_description": "使一般运营得以实现，并保障人员与货物在陆地、空中、海上与太空的安全转移与可用性的活动。",
        "reference_version": "2ab155c82bbca9ab1f78534fd977dca6e48608dc1ce82da1a720af400f3148bf",
        "local_object_ids": [],
        "mapping_type": "excluded-from-project-scope",
        "applicability": "out-of-scope",
        "reason": "本轮只覆盖养老资产与待遇服务，其他部门未纳入；不推断其不存在",
        "dependencies": [],
        "impact_scope": "未评估",
        "source_locator": "G21D §12 / 表1-1:1133",
        "review_action": "未来扩范围时重新评估"
      },
      "evidence": [
        "raw",
        "grm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started",
      "scope_id": "ref-sector-G21D-S12"
    },
    {
      "id": "GM-G21D-S08-F04",
      "type": "guide:government_overlay",
      "name": "投资管理",
      "attributes": {
        "reference_id": "G21D-S08-F04",
        "reference_kind": "function",
        "reference_path": [
          "财政",
          "投资管理"
        ],
        "reference_description": "**功能概述**：指金融资产与其他投资的处理。",
        "reference_version": "2ab155c82bbca9ab1f78534fd977dca6e48608dc1ce82da1a720af400f3148bf",
        "local_object_ids": [
          "LOCAL-PENSION",
          "LOCAL-ASSET"
        ],
        "mapping_type": "project-partial-coverage",
        "applicability": "applicable",
        "reason": "项目R01/R02职责映射；不意味着复制参考机构",
        "dependencies": [
          "LOCAL-ASSET→LOCAL-BENEFIT：投资/支付对账，项目关系待契约确认"
        ],
        "impact_scope": "试点养老办公室、资产组、待遇台",
        "source_locator": "G21D §8.1:792",
        "review_action": "核对本地职责与参考细项的差异；不将同名记录合并"
      },
      "evidence": [
        "raw",
        "grm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started",
      "scope_id": "ref-sector-G21D-S08"
    },
    {
      "id": "GM-G21D-S08-F04-S04",
      "type": "guide:government_overlay",
      "name": "养老基金管理",
      "attributes": {
        "reference_id": "G21D-S08-F04-S04",
        "reference_kind": "service",
        "reference_path": [
          "财政",
          "投资管理",
          "养老基金管理"
        ],
        "reference_description": "涉及投资并管理养老基金资产，以优化对该养老基金的缴款。",
        "reference_version": "2ab155c82bbca9ab1f78534fd977dca6e48608dc1ce82da1a720af400f3148bf",
        "local_object_ids": [
          "LOCAL-PENSION",
          "LOCAL-ASSET"
        ],
        "mapping_type": "project-partial-coverage",
        "applicability": "applicable",
        "reason": "项目R01/R02职责映射；不意味着复制参考机构",
        "dependencies": [
          "LOCAL-ASSET→LOCAL-BENEFIT：投资/支付对账，项目关系待契约确认"
        ],
        "impact_scope": "试点养老办公室、资产组、待遇台",
        "source_locator": "G21D §8.1:796",
        "review_action": "核对本地职责与参考细项的差异；不将同名记录合并"
      },
      "evidence": [
        "raw",
        "grm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started",
      "scope_id": "ref-sector-G21D-S08"
    },
    {
      "id": "GM-G21D-S11-F05",
      "type": "guide:government_overlay",
      "name": "财务共享中心",
      "attributes": {
        "reference_id": "G21D-S11-F05",
        "reference_kind": "function",
        "reference_path": [
          "共享服务",
          "财务共享中心"
        ],
        "reference_description": "**功能概述**：大量且多样的金融服务机构总部所在的金融中心。",
        "reference_version": "2ab155c82bbca9ab1f78534fd977dca6e48608dc1ce82da1a720af400f3148bf",
        "local_object_ids": [
          "LOCAL-PENSION",
          "LOCAL-BENEFIT"
        ],
        "mapping_type": "project-partial-coverage",
        "applicability": "applicable",
        "reason": "项目R01/R02职责映射；不意味着复制参考机构",
        "dependencies": [
          "LOCAL-ASSET→LOCAL-BENEFIT：投资/支付对账，项目关系待契约确认"
        ],
        "impact_scope": "试点养老办公室、资产组、待遇台",
        "source_locator": "G21D §11.1:1098",
        "review_action": "核对本地职责与参考细项的差异；不将同名记录合并"
      },
      "evidence": [
        "raw",
        "grm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started",
      "scope_id": "ref-sector-G21D-S11"
    },
    {
      "id": "GM-G21D-S11-F05-S06",
      "type": "guide:government_overlay",
      "name": "养老基金管理",
      "attributes": {
        "reference_id": "G21D-S11-F05-S06",
        "reference_kind": "service",
        "reference_path": [
          "共享服务",
          "财务共享中心",
          "养老基金管理"
        ],
        "reference_description": "负责开立退休储蓄账户（RSA）、支付退休福利，并对与养老基金相关的所有交易进行会计核算。",
        "reference_version": "2ab155c82bbca9ab1f78534fd977dca6e48608dc1ce82da1a720af400f3148bf",
        "local_object_ids": [
          "LOCAL-PENSION",
          "LOCAL-BENEFIT"
        ],
        "mapping_type": "project-partial-coverage",
        "applicability": "applicable",
        "reason": "项目R01/R02职责映射；不意味着复制参考机构",
        "dependencies": [
          "LOCAL-ASSET→LOCAL-BENEFIT：投资/支付对账，项目关系待契约确认"
        ],
        "impact_scope": "试点养老办公室、资产组、待遇台",
        "source_locator": "G21D §11.1:1104",
        "review_action": "核对本地职责与参考细项的差异；不将同名记录合并"
      },
      "evidence": [
        "raw",
        "grm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started",
      "scope_id": "ref-sector-G21D-S11"
    }
  ],
  "relationships": [],
  "extensions": {
    "relationship_types": {}
  },
  "view": {
    "id": "v-government-reference-catalog-overlay",
    "artifact_id": "government-reference-tailoring",
    "profile_id": "government-reference-catalog-overlay",
    "title": "政府参考目录与本地职责覆盖",
    "context": {
      "domains": [
        "business",
        "data",
        "application",
        "technology"
      ],
      "landscape": "segment",
      "purpose": "project",
      "abstraction": "logical",
      "evolution": "target"
    },
    "entity_ids": [
      "GM-G21D-S02",
      "GM-G21D-S03",
      "GM-G21D-S04",
      "GM-G21D-S05",
      "GM-G21D-S06",
      "GM-G21D-S07",
      "GM-G21D-S08",
      "GM-G21D-S09",
      "GM-G21D-S10",
      "GM-G21D-S11",
      "GM-G21D-S12",
      "GM-G21D-S08-F04",
      "GM-G21D-S08-F04-S04",
      "GM-G21D-S11-F05",
      "GM-G21D-S11-F05-S06"
    ],
    "relationship_ids": [],
    "analysis": "依本包raw-business-materials.json观察形成候选分析；源表身份与本地判断分开。详细步骤见相应规范。",
    "legend": "参考分类/映射不是本地事实；未知与不适用分开。表格邻接不表达关系；图形嵌套仅由显式reference_classifies关系建立。"
  },
  "scopes": [
    {
      "id": "ref-sector-G21D-S02",
      "description": "G21D参考分类范围：国际事务与贸易；仅区别来源同名项，不代表本地组织边界。"
    },
    {
      "id": "ref-sector-G21D-S03",
      "description": "G21D参考分类范围：国防与安全；仅区别来源同名项，不代表本地组织边界。"
    },
    {
      "id": "ref-sector-G21D-S04",
      "description": "G21D参考分类范围：一般政府与地方服务；仅区别来源同名项，不代表本地组织边界。"
    },
    {
      "id": "ref-sector-G21D-S05",
      "description": "G21D参考分类范围：青少年与教育；仅区别来源同名项，不代表本地组织边界。"
    },
    {
      "id": "ref-sector-G21D-S06",
      "description": "G21D参考分类范围：健康与社区福祉；仅区别来源同名项，不代表本地组织边界。"
    },
    {
      "id": "ref-sector-G21D-S07",
      "description": "G21D参考分类范围：司法、治安与内政；仅区别来源同名项，不代表本地组织边界。"
    },
    {
      "id": "ref-sector-G21D-S08",
      "description": "G21D参考分类范围：财政；仅区别来源同名项，不代表本地组织边界。"
    },
    {
      "id": "ref-sector-G21D-S09",
      "description": "G21D参考分类范围：增长、住房与环境；仅区别来源同名项，不代表本地组织边界。"
    },
    {
      "id": "ref-sector-G21D-S10",
      "description": "G21D参考分类范围：政策、绩效、人口与创新；仅区别来源同名项，不代表本地组织边界。"
    },
    {
      "id": "ref-sector-G21D-S11",
      "description": "G21D参考分类范围：共享服务；仅区别来源同名项，不代表本地组织边界。"
    },
    {
      "id": "ref-sector-G21D-S12",
      "description": "G21D参考分类范围：交通与运营；仅区别来源同名项，不代表本地组织边界。"
    }
  ]
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile government-reference-catalog-overlay --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile government-reference-catalog-overlay --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
