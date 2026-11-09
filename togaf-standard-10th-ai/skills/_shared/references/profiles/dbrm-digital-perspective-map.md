# DBRM与数字架构视角

`profile_id`: dbrm-digital-perspective-map；`artifact_id`: digital-business-reference-tailoring；主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G21H 表5-1。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-reference-1。

{
  "id": "dbrm-digital-perspective-map",
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
      "id": "RM-G21H-T5-1-R01",
      "type": "guide:dbrm_mapping_row",
      "name": "客户聚焦（Customer Focus）／G21H-T5-1-R01",
      "attributes": {
        "source_table": "G21H-T5-1",
        "source_row_id": "G21H-T5-1-R01",
        "raw_cells": {
          "dbrm_domain": "数字域",
          "dbrm_element": "客户聚焦（Customer Focus）",
          "digital_architecture_perspective": "体验设计（Experience Design）"
        },
        "resolved_cells": {
          "dbrm_domain": "数字域",
          "dbrm_element": "客户聚焦（Customer Focus）",
          "digital_architecture_perspective": "体验设计（Experience Design）"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "核对本地使用范围；来源关系和项目采用分别复核",
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
      "id": "RM-G21H-T5-1-R02",
      "type": "guide:dbrm_mapping_row",
      "name": "数字企业（Digital Enterprise）／G21H-T5-1-R02",
      "attributes": {
        "source_table": "G21H-T5-1",
        "source_row_id": "G21H-T5-1-R02",
        "raw_cells": {
          "dbrm_domain": "",
          "dbrm_element": "数字企业（Digital Enterprise）",
          "digital_architecture_perspective": "产品架构、运营架构"
        },
        "resolved_cells": {
          "dbrm_domain": "数字域",
          "dbrm_element": "数字企业（Digital Enterprise）",
          "digital_architecture_perspective": "产品架构、运营架构"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "核对本地使用范围；来源关系和项目采用分别复核",
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
      "id": "RM-G21H-T5-1-R03",
      "type": "guide:dbrm_mapping_row",
      "name": "战略语境（Strategic Context）／G21H-T5-1-R03",
      "attributes": {
        "source_table": "G21H-T5-1",
        "source_row_id": "G21H-T5-1-R03",
        "raw_cells": {
          "dbrm_domain": "战略域",
          "dbrm_element": "战略语境（Strategic Context）",
          "digital_architecture_perspective": "敏捷战略；价值创造"
        },
        "resolved_cells": {
          "dbrm_domain": "战略域",
          "dbrm_element": "战略语境（Strategic Context）",
          "digital_architecture_perspective": "敏捷战略；价值创造"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "核对本地使用范围；来源关系和项目采用分别复核",
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
      "id": "RM-G21H-T5-1-R04",
      "type": "guide:dbrm_mapping_row",
      "name": "业务动机（Business Motivation）／G21H-T5-1-R04",
      "attributes": {
        "source_table": "G21H-T5-1",
        "source_row_id": "G21H-T5-1-R04",
        "raw_cells": {
          "dbrm_domain": "",
          "dbrm_element": "业务动机（Business Motivation）",
          "digital_architecture_perspective": "敏捷战略；价值创造"
        },
        "resolved_cells": {
          "dbrm_domain": "战略域",
          "dbrm_element": "业务动机（Business Motivation）",
          "digital_architecture_perspective": "敏捷战略；价值创造"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "核对本地使用范围；来源关系和项目采用分别复核",
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
      "id": "RM-G21H-T5-1-R05",
      "type": "guide:dbrm_mapping_row",
      "name": "业务服务与产品（Business Services and Products）／G21H-T5-1-R05",
      "attributes": {
        "source_table": "G21H-T5-1",
        "source_row_id": "G21H-T5-1-R05",
        "raw_cells": {
          "dbrm_domain": "",
          "dbrm_element": "业务服务与产品（Business Services and Products）",
          "digital_architecture_perspective": "产品架构；运营架构"
        },
        "resolved_cells": {
          "dbrm_domain": "战略域",
          "dbrm_element": "业务服务与产品（Business Services and Products）",
          "digital_architecture_perspective": "产品架构；运营架构"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "核对本地使用范围；来源关系和项目采用分别复核",
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
      "id": "RM-G21H-T5-1-R06",
      "type": "guide:dbrm_mapping_row",
      "name": "生态与业务模型（Ecosystem and Business Model）／G21H-T5-1-R06",
      "attributes": {
        "source_table": "G21H-T5-1",
        "source_row_id": "G21H-T5-1-R06",
        "raw_cells": {
          "dbrm_domain": "结构域",
          "dbrm_element": "生态与业务模型（Ecosystem and Business Model）",
          "digital_architecture_perspective": "—"
        },
        "resolved_cells": {
          "dbrm_domain": "结构域",
          "dbrm_element": "生态与业务模型（Ecosystem and Business Model）",
          "digital_architecture_perspective": "—"
        },
        "source_mapping_status": "not-specified",
        "local_object_ids": [],
        "local_mapping_status": "unknown-source-mapping",
        "local_evidence": "unknown；原表—没有定义对应关系",
        "tailoring_reason": "不将—转成不适用",
        "review_action": "核对本地使用范围；来源关系和项目采用分别复核",
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
      "id": "RM-G21H-T5-1-R07",
      "type": "guide:dbrm_mapping_row",
      "name": "运营模式（Operating Model）／G21H-T5-1-R07",
      "attributes": {
        "source_table": "G21H-T5-1",
        "source_row_id": "G21H-T5-1-R07",
        "raw_cells": {
          "dbrm_domain": "",
          "dbrm_element": "运营模式（Operating Model）",
          "digital_architecture_perspective": "—"
        },
        "resolved_cells": {
          "dbrm_domain": "结构域",
          "dbrm_element": "运营模式（Operating Model）",
          "digital_architecture_perspective": "—"
        },
        "source_mapping_status": "not-specified",
        "local_object_ids": [],
        "local_mapping_status": "unknown-source-mapping",
        "local_evidence": "unknown；原表—没有定义对应关系",
        "tailoring_reason": "不将—转成不适用",
        "review_action": "核对本地使用范围；来源关系和项目采用分别复核",
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
      "id": "RM-G21H-T5-1-R08",
      "type": "guide:dbrm_mapping_row",
      "name": "业务能力模型（Business Capability Model）／G21H-T5-1-R08",
      "attributes": {
        "source_table": "G21H-T5-1",
        "source_row_id": "G21H-T5-1-R08",
        "raw_cells": {
          "dbrm_domain": "",
          "dbrm_element": "业务能力模型（Business Capability Model）",
          "digital_architecture_perspective": "—"
        },
        "resolved_cells": {
          "dbrm_domain": "结构域",
          "dbrm_element": "业务能力模型（Business Capability Model）",
          "digital_architecture_perspective": "—"
        },
        "source_mapping_status": "not-specified",
        "local_object_ids": [],
        "local_mapping_status": "unknown-source-mapping",
        "local_evidence": "unknown；原表—没有定义对应关系",
        "tailoring_reason": "不将—转成不适用",
        "review_action": "核对本地使用范围；来源关系和项目采用分别复核",
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
      "id": "RM-G21H-T5-1-R09",
      "type": "guide:dbrm_mapping_row",
      "name": "业务运营环境（Business Operating Environment）／G21H-T5-1-R09",
      "attributes": {
        "source_table": "G21H-T5-1",
        "source_row_id": "G21H-T5-1-R09",
        "raw_cells": {
          "dbrm_domain": "运营域",
          "dbrm_element": "业务运营环境（Business Operating Environment）",
          "digital_architecture_perspective": "运营架构；旅程地图与价值流"
        },
        "resolved_cells": {
          "dbrm_domain": "运营域",
          "dbrm_element": "业务运营环境（Business Operating Environment）",
          "digital_architecture_perspective": "运营架构；旅程地图与价值流"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "核对本地使用范围；来源关系和项目采用分别复核",
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
      "id": "RM-G21H-T5-1-R10",
      "type": "guide:dbrm_mapping_row",
      "name": "数字使能（Digital Enablement）／G21H-T5-1-R10",
      "attributes": {
        "source_table": "G21H-T5-1",
        "source_row_id": "G21H-T5-1-R10",
        "raw_cells": {
          "dbrm_domain": "",
          "dbrm_element": "数字使能（Digital Enablement）",
          "digital_architecture_perspective": "软件与硬件架构（技术架构）"
        },
        "resolved_cells": {
          "dbrm_domain": "运营域",
          "dbrm_element": "数字使能（Digital Enablement）",
          "digital_architecture_perspective": "软件与硬件架构（技术架构）"
        },
        "source_mapping_status": "local-body-mapping",
        "local_object_ids": [
          "PR-PENSION"
        ],
        "local_mapping_status": "candidate-project-application",
        "local_evidence": "R03–R05；本地使用仍需相应架构责任人核查",
        "tailoring_reason": "按原表参考整理试点架构问题，未断言本地活动已完成",
        "review_action": "核对本地使用范围；来源关系和项目采用分别复核",
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
    "id": "v-dbrm-digital-perspective-map",
    "artifact_id": "digital-business-reference-tailoring",
    "profile_id": "dbrm-digital-perspective-map",
    "title": "DBRM与数字架构视角",
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
      "RM-G21H-T5-1-R01",
      "RM-G21H-T5-1-R02",
      "RM-G21H-T5-1-R03",
      "RM-G21H-T5-1-R04",
      "RM-G21H-T5-1-R05",
      "RM-G21H-T5-1-R06",
      "RM-G21H-T5-1-R07",
      "RM-G21H-T5-1-R08",
      "RM-G21H-T5-1-R09",
      "RM-G21H-T5-1-R10"
    ],
    "relationship_ids": [],
    "analysis": "依本包raw-business-materials.json观察形成候选分析；源表身份与本地判断分开。详细步骤见相应规范。",
    "legend": "参考分类/映射不是本地事实；未知与不适用分开。表格邻接不表达关系；图形嵌套仅由显式reference_classifies关系建立。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile dbrm-digital-perspective-map --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile dbrm-digital-perspective-map --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
