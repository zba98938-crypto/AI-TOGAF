# 养老业务的政府参考分类裁剪

`profile_id`: government-reference-tailoring-default；`artifact_id`: government-reference-tailoring；主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G21D §1.3、§8.1、§11.1。

## 构图与定义状态

表示族：`nested-map`；输出：`diagram`。规范版本：2.1-reference-1。

{
  "id": "government-reference-tailoring-default",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "图形保留显式部门—功能—服务分类结构；表格保持完整源字段/本地判断，均不声称原图已通过。",
  "columns": 2,
  "default_group_label": "政府参考目录：两条选定路径",
  "hierarchy_caption": "嵌套表达参考分类上下位；不表示组织汇报或能力分解：",
  "verification_evidence": "reviews/source-verification/government-reference-tailoring-default.json",
  "source_asset_status": "available-separate-from-template-review"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:government_reference_node。关系类型：guide:reference_classifies。

```json
{
  "entities": {
    "guide:government_reference_node": [
      "reference_level",
      "reference_path",
      "definition",
      "local_mapping",
      "applicability"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 四条分类关系显式存在
- 不用parent_id猜层级
- 两个同名服务ID和路径不同

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
      "id": "GN-G21D-S08",
      "type": "guide:government_reference_node",
      "name": "财政",
      "attributes": {
        "reference_level": "sector",
        "reference_path": "财政",
        "definition": "对公共支出、收入、财务报告与审计保持控制，并为未来投资决策与财务规划提供方向。",
        "local_mapping": "养老业务办公室＋资产投资组",
        "applicability": "本试点部分适用，详见目录覆盖表"
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
      "id": "GN-G21D-S08-F04",
      "type": "guide:government_reference_node",
      "name": "投资管理",
      "attributes": {
        "reference_level": "function",
        "reference_path": "财政 / 投资管理",
        "definition": "指金融资产与其他投资的处理。",
        "local_mapping": "养老业务办公室＋资产投资组",
        "applicability": "本试点部分适用，详见目录覆盖表"
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
      "id": "GN-G21D-S08-F04-S04",
      "type": "guide:government_reference_node",
      "name": "养老基金管理",
      "attributes": {
        "reference_level": "service",
        "reference_path": "财政 / 投资管理 / 养老基金管理",
        "definition": "涉及投资并管理养老基金资产，以优化对该养老基金的缴款。",
        "local_mapping": "养老业务办公室＋资产投资组",
        "applicability": "本试点部分适用，详见目录覆盖表"
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
      "id": "GN-G21D-S11",
      "type": "guide:government_reference_node",
      "name": "共享服务",
      "attributes": {
        "reference_level": "sector",
        "reference_path": "共享服务",
        "definition": "代表公众协调并管理人员、沟通、财务与转型服务，以促进信息流转，并对人员、流程与技术实施监督，从而支持采购并与企业战略对齐。",
        "local_mapping": "养老业务办公室＋待遇服务台",
        "applicability": "本试点部分适用，详见目录覆盖表"
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
      "id": "GN-G21D-S11-F05",
      "type": "guide:government_reference_node",
      "name": "财务共享中心",
      "attributes": {
        "reference_level": "function",
        "reference_path": "共享服务 / 财务共享中心",
        "definition": "大量且多样的金融服务机构总部所在的金融中心。",
        "local_mapping": "养老业务办公室＋待遇服务台",
        "applicability": "候选采用；Finance Hub原定义与下属服务有歧义，待核查"
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
      "id": "GN-G21D-S11-F05-S06",
      "type": "guide:government_reference_node",
      "name": "养老基金管理",
      "attributes": {
        "reference_level": "service",
        "reference_path": "共享服务 / 财务共享中心 / 养老基金管理",
        "definition": "负责开立退休储蓄账户（RSA）、支付退休福利，并对与养老基金相关的所有交易进行会计核算。",
        "local_mapping": "养老业务办公室＋待遇服务台",
        "applicability": "本试点部分适用，详见目录覆盖表"
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
  "relationships": [
    {
      "id": "GH-G21D-S08-F04",
      "type": "guide:reference_classifies",
      "source": "GN-G21D-S08",
      "target": "GN-G21D-S08-F04",
      "label": "参考分类上位→下位；非组织汇报、非能力组成",
      "attributes": {},
      "evidence": [
        "raw"
      ],
      "certainty": "assumed"
    },
    {
      "id": "GH-G21D-S08-F04-S04",
      "type": "guide:reference_classifies",
      "source": "GN-G21D-S08-F04",
      "target": "GN-G21D-S08-F04-S04",
      "label": "参考分类上位→下位；非组织汇报、非能力组成",
      "attributes": {},
      "evidence": [
        "raw"
      ],
      "certainty": "assumed"
    },
    {
      "id": "GH-G21D-S11-F05",
      "type": "guide:reference_classifies",
      "source": "GN-G21D-S11",
      "target": "GN-G21D-S11-F05",
      "label": "参考分类上位→下位；非组织汇报、非能力组成",
      "attributes": {},
      "evidence": [
        "raw"
      ],
      "certainty": "assumed"
    },
    {
      "id": "GH-G21D-S11-F05-S06",
      "type": "guide:reference_classifies",
      "source": "GN-G21D-S11-F05",
      "target": "GN-G21D-S11-F05-S06",
      "label": "参考分类上位→下位；非组织汇报、非能力组成",
      "attributes": {},
      "evidence": [
        "raw"
      ],
      "certainty": "assumed"
    }
  ],
  "extensions": {
    "relationship_types": {
      "guide:reference_classifies": {
        "source_types": [
          "guide:government_reference_node"
        ],
        "target_types": [
          "guide:government_reference_node"
        ],
        "meaning": "目录规定的部门→功能→服务分类方向；不表示本地组织汇报、运行依赖或能力组成"
      }
    }
  },
  "view": {
    "id": "v-government-reference-tailoring-default",
    "artifact_id": "government-reference-tailoring",
    "profile_id": "government-reference-tailoring-default",
    "title": "养老业务的政府参考分类裁剪",
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
      "GN-G21D-S08",
      "GN-G21D-S08-F04",
      "GN-G21D-S08-F04-S04",
      "GN-G21D-S11",
      "GN-G21D-S11-F05",
      "GN-G21D-S11-F05-S06"
    ],
    "relationship_ids": [
      "GH-G21D-S08-F04",
      "GH-G21D-S08-F04-S04",
      "GH-G21D-S11-F05",
      "GH-G21D-S11-F05-S06"
    ],
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
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile government-reference-tailoring-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile government-reference-tailoring-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
