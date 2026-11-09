# DBRM与元模型及架构域

`profile_id`: dbrm-content-domain-map；`artifact_id`: digital-business-reference-tailoring；主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G21H 表6-2。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-reference-1。

{
  "id": "dbrm-content-domain-map",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "图形保留显式部门—功能—服务分类结构；表格保持完整源字段/本地判断，均不声称原图已通过。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:dbrm_mapping_row。关系类型：。

```json
{
  "entities": {
    "guide:dbrm_mapping_row": [
      "source_table",
      "source_row_id",
      "raw_cells",
      "resolved_cells",
      "source_mapping_status",
      "local_object_ids",
      "local_mapping_status",
      "local_evidence",
      "tailoring_reason",
      "review_action",
      "reference_identity"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 源行/原值不能被项目变更覆写
- DBRM域、架构域、ADM、全景层级互不替代
- 表6-2运营管理与正文服务交付管理差异保留
- 表未列G/H不意味着无适用关系

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
      "id": "RM-G21H-T6-2-R01",
      "type": "guide:dbrm_mapping_row",
      "name": "生态与业务模型／G21H-T6-2-R01",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R01",
        "raw_cells": {
          "content_entities": "价值流（Value Streams）",
          "dbrm_subelements": "战略原则与业务模型；业务生态模型",
          "dbrm_element": "生态与业务模型",
          "dbrm_domain": "结构"
        },
        "resolved_cells": {
          "content_entities": "价值流（Value Streams）",
          "dbrm_subelements": "战略原则与业务模型；业务生态模型",
          "dbrm_element": "生态与业务模型",
          "dbrm_domain": "结构"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "RM-G21H-T6-2-R02",
      "type": "guide:dbrm_mapping_row",
      "name": "运营模式／G21H-T6-2-R02",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R02",
        "raw_cells": {
          "content_entities": "",
          "dbrm_subelements": "战略姿态与价值准则；服务模型",
          "dbrm_element": "运营模式",
          "dbrm_domain": "结构"
        },
        "resolved_cells": {
          "content_entities": "价值流（Value Streams）",
          "dbrm_subelements": "战略姿态与价值准则；服务模型",
          "dbrm_element": "运营模式",
          "dbrm_domain": "结构"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "RM-G21H-T6-2-R03",
      "type": "guide:dbrm_mapping_row",
      "name": "客户聚焦／G21H-T6-2-R03",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R03",
        "raw_cells": {
          "content_entities": "",
          "dbrm_subelements": "数字语境/需求；客户体验；数字价值",
          "dbrm_element": "客户聚焦",
          "dbrm_domain": "数字"
        },
        "resolved_cells": {
          "content_entities": "价值流（Value Streams）",
          "dbrm_subelements": "数字语境/需求；客户体验；数字价值",
          "dbrm_element": "客户聚焦",
          "dbrm_domain": "数字"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "RM-G21H-T6-2-R04",
      "type": "guide:dbrm_mapping_row",
      "name": "业务运营环境／G21H-T6-2-R04",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R04",
        "raw_cells": {
          "content_entities": "",
          "dbrm_subelements": "服务体验与客户旅程地图；价值链模型与价值流",
          "dbrm_element": "业务运营环境",
          "dbrm_domain": "运营"
        },
        "resolved_cells": {
          "content_entities": "价值流（Value Streams）",
          "dbrm_subelements": "服务体验与客户旅程地图；价值链模型与价值流",
          "dbrm_element": "业务运营环境",
          "dbrm_domain": "运营"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "RM-G21H-T6-2-R05",
      "type": "guide:dbrm_mapping_row",
      "name": "业务能力模型／G21H-T6-2-R05",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R05",
        "raw_cells": {
          "content_entities": "业务能力（Business Capabilities）",
          "dbrm_subelements": "面向客户与市场的营销能力；服务交付使能能力；运营管理能力；共享与支撑能力",
          "dbrm_element": "业务能力模型",
          "dbrm_domain": "结构"
        },
        "resolved_cells": {
          "content_entities": "业务能力（Business Capabilities）",
          "dbrm_subelements": "面向客户与市场的营销能力；服务交付使能能力；运营管理能力；共享与支撑能力",
          "dbrm_element": "业务能力模型",
          "dbrm_domain": "结构"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "RM-G21H-T6-2-R06",
      "type": "guide:dbrm_mapping_row",
      "name": "数字使能／G21H-T6-2-R06",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R06",
        "raw_cells": {
          "content_entities": "行动方案（Course of Action）",
          "dbrm_subelements": "数字原则与战略；敏捷数字交付模型",
          "dbrm_element": "数字使能",
          "dbrm_domain": "运营"
        },
        "resolved_cells": {
          "content_entities": "行动方案（Course of Action）",
          "dbrm_subelements": "数字原则与战略；敏捷数字交付模型",
          "dbrm_element": "数字使能",
          "dbrm_domain": "运营"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "RM-G21H-T6-2-R07",
      "type": "guide:dbrm_mapping_row",
      "name": "业务运营环境／G21H-T6-2-R07",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R07",
        "raw_cells": {
          "content_entities": "业务信息、服务质量、合同、业务服务",
          "dbrm_subelements": "业务信息地图",
          "dbrm_element": "业务运营环境",
          "dbrm_domain": "运营"
        },
        "resolved_cells": {
          "content_entities": "业务信息、服务质量、合同、业务服务",
          "dbrm_subelements": "业务信息地图",
          "dbrm_element": "业务运营环境",
          "dbrm_domain": "运营"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "RM-G21H-T6-2-R08",
      "type": "guide:dbrm_mapping_row",
      "name": "数字企业／G21H-T6-2-R08",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R08",
        "raw_cells": {
          "content_entities": "",
          "dbrm_subelements": "数字产品与服务组合/模型",
          "dbrm_element": "数字企业",
          "dbrm_domain": "数字"
        },
        "resolved_cells": {
          "content_entities": "业务信息、服务质量、合同、业务服务",
          "dbrm_subelements": "数字产品与服务组合/模型",
          "dbrm_element": "数字企业",
          "dbrm_domain": "数字"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "RM-G21H-T6-2-R09",
      "type": "guide:dbrm_mapping_row",
      "name": "业务服务与产品／G21H-T6-2-R09",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R09",
        "raw_cells": {
          "content_entities": "产品、流程、事件、控制",
          "dbrm_subelements": "主要业务服务；核心业务产品；增值服务",
          "dbrm_element": "业务服务与产品",
          "dbrm_domain": "战略"
        },
        "resolved_cells": {
          "content_entities": "产品、流程、事件、控制",
          "dbrm_subelements": "主要业务服务；核心业务产品；增值服务",
          "dbrm_element": "业务服务与产品",
          "dbrm_domain": "战略"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "RM-G21H-T6-2-R10",
      "type": "guide:dbrm_mapping_row",
      "name": "业务运营环境／G21H-T6-2-R10",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R10",
        "raw_cells": {
          "content_entities": "",
          "dbrm_subelements": "业务流程地图",
          "dbrm_element": "业务运营环境",
          "dbrm_domain": "运营"
        },
        "resolved_cells": {
          "content_entities": "产品、流程、事件、控制",
          "dbrm_subelements": "业务流程地图",
          "dbrm_element": "业务运营环境",
          "dbrm_domain": "运营"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "RM-G21H-T6-2-R11",
      "type": "guide:dbrm_mapping_row",
      "name": "生态与业务模型／G21H-T6-2-R11",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R11",
        "raw_cells": {
          "content_entities": "",
          "dbrm_subelements": "政策与风险管理框架",
          "dbrm_element": "生态与业务模型",
          "dbrm_domain": "结构"
        },
        "resolved_cells": {
          "content_entities": "产品、流程、事件、控制",
          "dbrm_subelements": "政策与风险管理框架",
          "dbrm_element": "生态与业务模型",
          "dbrm_domain": "结构"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "RM-G21H-T6-2-R12",
      "type": "guide:dbrm_mapping_row",
      "name": "数字企业／G21H-T6-2-R12",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R12",
        "raw_cells": {
          "content_entities": "",
          "dbrm_subelements": "数字运营",
          "dbrm_element": "数字企业",
          "dbrm_domain": "数字"
        },
        "resolved_cells": {
          "content_entities": "产品、流程、事件、控制",
          "dbrm_subelements": "数字运营",
          "dbrm_element": "数字企业",
          "dbrm_domain": "数字"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "RM-G21H-T6-2-R13",
      "type": "guide:dbrm_mapping_row",
      "name": "数字使能／G21H-T6-2-R13",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R13",
        "raw_cells": {
          "content_entities": "",
          "dbrm_subelements": "数字治理",
          "dbrm_element": "数字使能",
          "dbrm_domain": "运营"
        },
        "resolved_cells": {
          "content_entities": "产品、流程、事件、控制",
          "dbrm_subelements": "数字治理",
          "dbrm_element": "数字使能",
          "dbrm_domain": "运营"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "RM-G21H-T6-2-R14",
      "type": "guide:dbrm_mapping_row",
      "name": "运营模式／G21H-T6-2-R14",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R14",
        "raw_cells": {
          "content_entities": "职能、组织单元（Functions, Organization Unit）",
          "dbrm_subelements": "组织模型",
          "dbrm_element": "运营模式",
          "dbrm_domain": "结构"
        },
        "resolved_cells": {
          "content_entities": "职能、组织单元（Functions, Organization Unit）",
          "dbrm_subelements": "组织模型",
          "dbrm_element": "运营模式",
          "dbrm_domain": "结构"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "RM-G21H-T6-2-R15",
      "type": "guide:dbrm_mapping_row",
      "name": "业务运营环境／G21H-T6-2-R15",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R15",
        "raw_cells": {
          "content_entities": "",
          "dbrm_subelements": "参与者、角色与组织结构",
          "dbrm_element": "业务运营环境",
          "dbrm_domain": "运营"
        },
        "resolved_cells": {
          "content_entities": "职能、组织单元（Functions, Organization Unit）",
          "dbrm_subelements": "参与者、角色与组织结构",
          "dbrm_element": "业务运营环境",
          "dbrm_domain": "运营"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "RM-G21H-T6-2-R16",
      "type": "guide:dbrm_mapping_row",
      "name": "生态与业务模型／G21H-T6-2-R16",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R16",
        "raw_cells": {
          "content_entities": "",
          "dbrm_subelements": "组织文化与行为",
          "dbrm_element": "生态与业务模型",
          "dbrm_domain": "结构"
        },
        "resolved_cells": {
          "content_entities": "职能、组织单元（Functions, Organization Unit）",
          "dbrm_subelements": "组织文化与行为",
          "dbrm_element": "生态与业务模型",
          "dbrm_domain": "结构"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "RM-G21H-T6-2-R17",
      "type": "guide:dbrm_mapping_row",
      "name": "数字使能／G21H-T6-2-R17",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R17",
        "raw_cells": {
          "content_entities": "",
          "dbrm_subelements": "敏捷数字交付模型",
          "dbrm_element": "数字使能",
          "dbrm_domain": "运营"
        },
        "resolved_cells": {
          "content_entities": "职能、组织单元（Functions, Organization Unit）",
          "dbrm_subelements": "敏捷数字交付模型",
          "dbrm_element": "数字使能",
          "dbrm_domain": "运营"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "RM-G21H-T6-2-R18",
      "type": "guide:dbrm_mapping_row",
      "name": "数字企业／G21H-T6-2-R18",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R18",
        "raw_cells": {
          "content_entities": "参与者、角色（Actors, Roles）",
          "dbrm_subelements": "数字胜任力",
          "dbrm_element": "数字企业",
          "dbrm_domain": "数字"
        },
        "resolved_cells": {
          "content_entities": "参与者、角色（Actors, Roles）",
          "dbrm_subelements": "数字胜任力",
          "dbrm_element": "数字企业",
          "dbrm_domain": "数字"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "RM-G21H-T6-2-R19",
      "type": "guide:dbrm_mapping_row",
      "name": "运营模式／G21H-T6-2-R19",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R19",
        "raw_cells": {
          "content_entities": "",
          "dbrm_subelements": "资源模型",
          "dbrm_element": "运营模式",
          "dbrm_domain": "结构"
        },
        "resolved_cells": {
          "content_entities": "参与者、角色（Actors, Roles）",
          "dbrm_subelements": "资源模型",
          "dbrm_element": "运营模式",
          "dbrm_domain": "结构"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "RM-G21H-T6-2-R20",
      "type": "guide:dbrm_mapping_row",
      "name": "业务运营环境／G21H-T6-2-R20",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R20",
        "raw_cells": {
          "content_entities": "数据实体（Data Entities）",
          "dbrm_subelements": "业务系统与数据模型",
          "dbrm_element": "业务运营环境",
          "dbrm_domain": "运营"
        },
        "resolved_cells": {
          "content_entities": "数据实体（Data Entities）",
          "dbrm_subelements": "业务系统与数据模型",
          "dbrm_element": "业务运营环境",
          "dbrm_domain": "运营"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "RM-G21H-T6-2-R21",
      "type": "guide:dbrm_mapping_row",
      "name": "业务运营环境／G21H-T6-2-R21",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R21",
        "raw_cells": {
          "content_entities": "逻辑数据实体（Logical Data Entities）",
          "dbrm_subelements": "业务系统与数据模型",
          "dbrm_element": "业务运营环境",
          "dbrm_domain": "运营"
        },
        "resolved_cells": {
          "content_entities": "逻辑数据实体（Logical Data Entities）",
          "dbrm_subelements": "业务系统与数据模型",
          "dbrm_element": "业务运营环境",
          "dbrm_domain": "运营"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "RM-G21H-T6-2-R22",
      "type": "guide:dbrm_mapping_row",
      "name": "业务运营环境／G21H-T6-2-R22",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R22",
        "raw_cells": {
          "content_entities": "物理数据组件（Physical Data Components）",
          "dbrm_subelements": "业务系统与数据模型",
          "dbrm_element": "业务运营环境",
          "dbrm_domain": "运营"
        },
        "resolved_cells": {
          "content_entities": "物理数据组件（Physical Data Components）",
          "dbrm_subelements": "业务系统与数据模型",
          "dbrm_element": "业务运营环境",
          "dbrm_domain": "运营"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "RM-G21H-T6-2-R23",
      "type": "guide:dbrm_mapping_row",
      "name": "业务运营环境／G21H-T6-2-R23",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R23",
        "raw_cells": {
          "content_entities": "应用服务（Application Services）",
          "dbrm_subelements": "业务系统与数据模型",
          "dbrm_element": "业务运营环境",
          "dbrm_domain": "运营"
        },
        "resolved_cells": {
          "content_entities": "应用服务（Application Services）",
          "dbrm_subelements": "业务系统与数据模型",
          "dbrm_element": "业务运营环境",
          "dbrm_domain": "运营"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "RM-G21H-T6-2-R24",
      "type": "guide:dbrm_mapping_row",
      "name": "数字使能／G21H-T6-2-R24",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R24",
        "raw_cells": {
          "content_entities": "逻辑应用组件（Logical Application Components）",
          "dbrm_subelements": "数字平台",
          "dbrm_element": "数字使能",
          "dbrm_domain": "运营"
        },
        "resolved_cells": {
          "content_entities": "逻辑应用组件（Logical Application Components）",
          "dbrm_subelements": "数字平台",
          "dbrm_element": "数字使能",
          "dbrm_domain": "运营"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "RM-G21H-T6-2-R25",
      "type": "guide:dbrm_mapping_row",
      "name": "数字使能／G21H-T6-2-R25",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R25",
        "raw_cells": {
          "content_entities": "物理应用组件（Physical Application Components）",
          "dbrm_subelements": "数字平台",
          "dbrm_element": "数字使能",
          "dbrm_domain": "运营"
        },
        "resolved_cells": {
          "content_entities": "物理应用组件（Physical Application Components）",
          "dbrm_subelements": "数字平台",
          "dbrm_element": "数字使能",
          "dbrm_domain": "运营"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "RM-G21H-T6-2-R26",
      "type": "guide:dbrm_mapping_row",
      "name": "数字使能／G21H-T6-2-R26",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R26",
        "raw_cells": {
          "content_entities": "技术服务（Technology Services）",
          "dbrm_subelements": "数字平台",
          "dbrm_element": "数字使能",
          "dbrm_domain": "运营"
        },
        "resolved_cells": {
          "content_entities": "技术服务（Technology Services）",
          "dbrm_subelements": "数字平台",
          "dbrm_element": "数字使能",
          "dbrm_domain": "运营"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "RM-G21H-T6-2-R27",
      "type": "guide:dbrm_mapping_row",
      "name": "数字使能／G21H-T6-2-R27",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R27",
        "raw_cells": {
          "content_entities": "逻辑技术组件（Logical Technology Components）",
          "dbrm_subelements": "数字平台",
          "dbrm_element": "数字使能",
          "dbrm_domain": "运营"
        },
        "resolved_cells": {
          "content_entities": "逻辑技术组件（Logical Technology Components）",
          "dbrm_subelements": "数字平台",
          "dbrm_element": "数字使能",
          "dbrm_domain": "运营"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "RM-G21H-T6-2-R28",
      "type": "guide:dbrm_mapping_row",
      "name": "数字使能／G21H-T6-2-R28",
      "attributes": {
        "source_table": "G21H-T6-2",
        "source_row_id": "G21H-T6-2-R28",
        "raw_cells": {
          "content_entities": "物理技术组件（Physical Technology Components）",
          "dbrm_subelements": "数字平台",
          "dbrm_element": "数字使能",
          "dbrm_domain": "运营"
        },
        "resolved_cells": {
          "content_entities": "物理技术组件（Physical Technology Components）",
          "dbrm_subelements": "数字平台",
          "dbrm_element": "数字使能",
          "dbrm_domain": "运营"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "逐元模型项核实同名/术语差异；保留原表组合实体",
        "reference_identity": "local-source-reference; project-overlay-separate"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    }
  ],
  "relationships": [],
  "extensions": {
    "relationship_types": {}
  },
  "view": {
    "id": "v-dbrm-content-domain-map",
    "artifact_id": "digital-business-reference-tailoring",
    "profile_id": "dbrm-content-domain-map",
    "title": "DBRM与元模型及架构域",
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
      "RM-G21H-T6-2-R01",
      "RM-G21H-T6-2-R02",
      "RM-G21H-T6-2-R03",
      "RM-G21H-T6-2-R04",
      "RM-G21H-T6-2-R05",
      "RM-G21H-T6-2-R06",
      "RM-G21H-T6-2-R07",
      "RM-G21H-T6-2-R08",
      "RM-G21H-T6-2-R09",
      "RM-G21H-T6-2-R10",
      "RM-G21H-T6-2-R11",
      "RM-G21H-T6-2-R12",
      "RM-G21H-T6-2-R13",
      "RM-G21H-T6-2-R14",
      "RM-G21H-T6-2-R15",
      "RM-G21H-T6-2-R16",
      "RM-G21H-T6-2-R17",
      "RM-G21H-T6-2-R18",
      "RM-G21H-T6-2-R19",
      "RM-G21H-T6-2-R20",
      "RM-G21H-T6-2-R21",
      "RM-G21H-T6-2-R22",
      "RM-G21H-T6-2-R23",
      "RM-G21H-T6-2-R24",
      "RM-G21H-T6-2-R25",
      "RM-G21H-T6-2-R26",
      "RM-G21H-T6-2-R27",
      "RM-G21H-T6-2-R28"
    ],
    "relationship_ids": [],
    "analysis": "依本包raw-business-materials.json观察形成候选分析；源表身份与本地判断分开。详细步骤见相应规范。",
    "legend": "参考分类/映射不是本地事实；未知与不适用分开。表格邻接不表达关系；图形嵌套仅由显式reference_classifies关系建立。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile dbrm-content-domain-map --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile dbrm-content-domain-map --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
