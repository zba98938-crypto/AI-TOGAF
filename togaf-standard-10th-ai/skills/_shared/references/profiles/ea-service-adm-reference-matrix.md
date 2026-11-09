# EA服务×ADM来源参考矩阵

`profile_id`: ea-service-adm-reference-matrix；`artifact_id`: ea-service-catalog；主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G217/figC-1。

## 构图与定义状态

表示族：`deployment`；输出：`diagram`。规范版本：2.3。

{
  "id": "ea-service-adm-reference-matrix",
  "version": "2.3",
  "source_verified": false,
  "source_figure": "G217/figC-1",
  "source_topology": "ea-adm-matrix",
  "separate_detail_ledger": true,
  "review_status": "source-topology-registered-awaiting-independent-review",
  "layout_notes": "24列=6分类+18服务；10阶段。空白是来源未标注，不表示禁止。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:ea_adm_mapping。关系类型：。

```json
{
  "entities": {
    "*": [
      "definition"
    ]
  },
  "relationships": {
    "*": [
      "meaning"
    ]
  }
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 24列=6分类+18服务；10阶段。空白是来源未标注，不表示禁止。
- 开发支持分类G格按来源转录但语义存疑，需原文专业复核。

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "来源结构指导的解释性示例；项目事实为假设；不代表原图逐像素复刻、标准认证或架构批准。",
  "sources": [
    {
      "id": "example-source",
      "kind": "example",
      "description": "专用拓扑验收示例：G217/figC-1；来源图解释与候选企业场景分开。"
    }
  ],
  "entities": [
    {
      "id": "cat_req",
      "type": "guide:ea_adm_mapping",
      "name": "需求获取与理解服务",
      "attributes": {
        "definition": "Requirements Elicitation and Understanding Services",
        "service": "Requirements Elicitation and Understanding Services",
        "column_kind": "category",
        "phase_map": {
          "P": "source-unmarked",
          "A": "source-unmarked",
          "B": "source-unmarked",
          "C": "source-unmarked",
          "D": "source-unmarked",
          "E": "source-unmarked",
          "F": "source-unmarked",
          "G": "source-unmarked",
          "H": "source-unmarked",
          "RM": "source-unmarked"
        },
        "mapping_origin": "local-source-transcription; not business facts"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "svc_stakeholders",
      "type": "guide:ea_adm_mapping",
      "name": "利益相关者管理服务",
      "attributes": {
        "definition": "Stakeholders Management Services",
        "service": "Stakeholders Management Services",
        "column_kind": "service",
        "phase_map": {
          "P": "source-mapped",
          "A": "source-mapped",
          "B": "source-unmarked",
          "C": "source-unmarked",
          "D": "source-unmarked",
          "E": "source-mapped",
          "F": "source-unmarked",
          "G": "source-unmarked",
          "H": "source-mapped",
          "RM": "source-mapped"
        },
        "mapping_origin": "local-source-transcription; not business facts"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "svc_business_value",
      "type": "guide:ea_adm_mapping",
      "name": "业务价值评估与分析服务",
      "attributes": {
        "definition": "Business Value Assessment and Analysis Service",
        "service": "Business Value Assessment and Analysis Service",
        "column_kind": "service",
        "phase_map": {
          "P": "source-mapped",
          "A": "source-mapped",
          "B": "source-unmarked",
          "C": "source-unmarked",
          "D": "source-unmarked",
          "E": "source-mapped",
          "F": "source-mapped",
          "G": "source-unmarked",
          "H": "source-unmarked",
          "RM": "source-mapped"
        },
        "mapping_origin": "local-source-transcription; not business facts"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cat_arch_plan",
      "type": "guide:ea_adm_mapping",
      "name": "架构规划服务",
      "attributes": {
        "definition": "Architecture Planning Services",
        "service": "Architecture Planning Services",
        "column_kind": "category",
        "phase_map": {
          "P": "source-unmarked",
          "A": "source-unmarked",
          "B": "source-unmarked",
          "C": "source-unmarked",
          "D": "source-unmarked",
          "E": "source-unmarked",
          "F": "source-unmarked",
          "G": "source-unmarked",
          "H": "source-unmarked",
          "RM": "source-unmarked"
        },
        "mapping_origin": "local-source-transcription; not business facts"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "svc_arch_project_planning",
      "type": "guide:ea_adm_mapping",
      "name": "架构项目规划服务",
      "attributes": {
        "definition": "Architecture Project Planning Services",
        "service": "Architecture Project Planning Services",
        "column_kind": "service",
        "phase_map": {
          "P": "source-mapped",
          "A": "source-mapped",
          "B": "source-mapped",
          "C": "source-mapped",
          "D": "source-mapped",
          "E": "source-unmarked",
          "F": "source-mapped",
          "G": "source-unmarked",
          "H": "source-mapped",
          "RM": "source-unmarked"
        },
        "mapping_origin": "local-source-transcription; not business facts"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "svc_arch_tailoring",
      "type": "guide:ea_adm_mapping",
      "name": "架构裁剪服务",
      "attributes": {
        "definition": "Architecting Tailoring Services",
        "service": "Architecting Tailoring Services",
        "column_kind": "service",
        "phase_map": {
          "P": "source-mapped",
          "A": "source-mapped",
          "B": "source-unmarked",
          "C": "source-unmarked",
          "D": "source-unmarked",
          "E": "source-unmarked",
          "F": "source-unmarked",
          "G": "source-unmarked",
          "H": "source-mapped",
          "RM": "source-unmarked"
        },
        "mapping_origin": "local-source-transcription; not business facts"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cat_design",
      "type": "guide:ea_adm_mapping",
      "name": "设计支持服务",
      "attributes": {
        "definition": "Design Support Services",
        "service": "Design Support Services",
        "column_kind": "category",
        "phase_map": {
          "P": "source-unmarked",
          "A": "source-unmarked",
          "B": "source-unmarked",
          "C": "source-unmarked",
          "D": "source-unmarked",
          "E": "source-unmarked",
          "F": "source-unmarked",
          "G": "source-unmarked",
          "H": "source-unmarked",
          "RM": "source-unmarked"
        },
        "mapping_origin": "local-source-transcription; not business facts"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "svc_vision",
      "type": "guide:ea_adm_mapping",
      "name": "架构愿景与战略服务",
      "attributes": {
        "definition": "Architecture Vision and Strategy Services",
        "service": "Architecture Vision and Strategy Services",
        "column_kind": "service",
        "phase_map": {
          "P": "source-unmarked",
          "A": "source-mapped",
          "B": "source-mapped",
          "C": "source-mapped",
          "D": "source-mapped",
          "E": "source-unmarked",
          "F": "source-unmarked",
          "G": "source-unmarked",
          "H": "source-mapped",
          "RM": "source-unmarked"
        },
        "mapping_origin": "local-source-transcription; not business facts"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "svc_modeling",
      "type": "guide:ea_adm_mapping",
      "name": "架构建模与文档服务（MVA）",
      "attributes": {
        "definition": "Architecture Modeling and Documentation Services (MVA)",
        "service": "Architecture Modeling and Documentation Services (MVA)",
        "column_kind": "service",
        "phase_map": {
          "P": "source-unmarked",
          "A": "source-unmarked",
          "B": "source-mapped",
          "C": "source-mapped",
          "D": "source-mapped",
          "E": "source-unmarked",
          "F": "source-unmarked",
          "G": "source-unmarked",
          "H": "source-mapped",
          "RM": "source-unmarked"
        },
        "mapping_origin": "local-source-transcription; not business facts"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "svc_integration",
      "type": "guide:ea_adm_mapping",
      "name": "架构集成服务",
      "attributes": {
        "definition": "Architecture Integration Services",
        "service": "Architecture Integration Services",
        "column_kind": "service",
        "phase_map": {
          "P": "source-unmarked",
          "A": "source-unmarked",
          "B": "source-mapped",
          "C": "source-mapped",
          "D": "source-mapped",
          "E": "source-mapped",
          "F": "source-mapped",
          "G": "source-unmarked",
          "H": "source-unmarked",
          "RM": "source-unmarked"
        },
        "mapping_origin": "local-source-transcription; not business facts"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "svc_compliance_dev",
      "type": "guide:ea_adm_mapping",
      "name": "架构合规开发服务（业务、信息、应用、基础设施、系统等）",
      "attributes": {
        "definition": "Architecture Compliance Development Services (Business, Info, Appl, Infra, Systs, ...)",
        "service": "Architecture Compliance Development Services (Business, Info, Appl, Infra, Systs, ...)",
        "column_kind": "service",
        "phase_map": {
          "P": "source-unmarked",
          "A": "source-unmarked",
          "B": "source-unmarked",
          "C": "source-unmarked",
          "D": "source-unmarked",
          "E": "source-unmarked",
          "F": "source-unmarked",
          "G": "source-mapped",
          "H": "source-mapped",
          "RM": "source-unmarked"
        },
        "mapping_origin": "local-source-transcription; not business facts"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cat_dev",
      "type": "guide:ea_adm_mapping",
      "name": "开发支持服务",
      "attributes": {
        "definition": "Development Support Services",
        "service": "Development Support Services",
        "column_kind": "category",
        "phase_map": {
          "P": "source-unmarked",
          "A": "source-unmarked",
          "B": "source-unmarked",
          "C": "source-unmarked",
          "D": "source-unmarked",
          "E": "source-unmarked",
          "F": "source-unmarked",
          "G": "source-mapped",
          "H": "source-unmarked",
          "RM": "source-unmarked"
        },
        "mapping_origin": "local-source-transcription; not business facts"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "svc_standards",
      "type": "guide:ea_adm_mapping",
      "name": "架构与标准指导服务",
      "attributes": {
        "definition": "Architecture and Standards Guidance Service",
        "service": "Architecture and Standards Guidance Service",
        "column_kind": "service",
        "phase_map": {
          "P": "source-unmarked",
          "A": "source-unmarked",
          "B": "source-mapped",
          "C": "source-mapped",
          "D": "source-mapped",
          "E": "source-mapped",
          "F": "source-mapped",
          "G": "source-mapped",
          "H": "source-mapped",
          "RM": "source-unmarked"
        },
        "mapping_origin": "local-source-transcription; not business facts"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "svc_change",
      "type": "guide:ea_adm_mapping",
      "name": "变更管理",
      "attributes": {
        "definition": "Change Management",
        "service": "Change Management",
        "column_kind": "service",
        "phase_map": {
          "P": "source-unmarked",
          "A": "source-unmarked",
          "B": "source-unmarked",
          "C": "source-unmarked",
          "D": "source-unmarked",
          "E": "source-unmarked",
          "F": "source-unmarked",
          "G": "source-mapped",
          "H": "source-unmarked",
          "RM": "source-unmarked"
        },
        "mapping_origin": "local-source-transcription; not business facts"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "svc_compliance_assessment",
      "type": "guide:ea_adm_mapping",
      "name": "合规评估与分析服务",
      "attributes": {
        "definition": "Compliance Assessment and Analysis Service",
        "service": "Compliance Assessment and Analysis Service",
        "column_kind": "service",
        "phase_map": {
          "P": "source-unmarked",
          "A": "source-unmarked",
          "B": "source-mapped",
          "C": "source-mapped",
          "D": "source-mapped",
          "E": "source-mapped",
          "F": "source-unmarked",
          "G": "source-mapped",
          "H": "source-unmarked",
          "RM": "source-unmarked"
        },
        "mapping_origin": "local-source-transcription; not business facts"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "svc_release",
      "type": "guide:ea_adm_mapping",
      "name": "发布支持服务",
      "attributes": {
        "definition": "Release Support Services",
        "service": "Release Support Services",
        "column_kind": "service",
        "phase_map": {
          "P": "source-unmarked",
          "A": "source-unmarked",
          "B": "source-unmarked",
          "C": "source-unmarked",
          "D": "source-unmarked",
          "E": "source-unmarked",
          "F": "source-unmarked",
          "G": "source-mapped",
          "H": "source-unmarked",
          "RM": "source-unmarked"
        },
        "mapping_origin": "local-source-transcription; not business facts"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cat_enterprise",
      "type": "guide:ea_adm_mapping",
      "name": "企业支持服务",
      "attributes": {
        "definition": "Enterprise Support Services",
        "service": "Enterprise Support Services",
        "column_kind": "category",
        "phase_map": {
          "P": "source-unmarked",
          "A": "source-unmarked",
          "B": "source-unmarked",
          "C": "source-unmarked",
          "D": "source-unmarked",
          "E": "source-unmarked",
          "F": "source-unmarked",
          "G": "source-unmarked",
          "H": "source-unmarked",
          "RM": "source-unmarked"
        },
        "mapping_origin": "local-source-transcription; not business facts"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "svc_portfolio",
      "type": "guide:ea_adm_mapping",
      "name": "组合管理支持服务（含资产管理、收购）",
      "attributes": {
        "definition": "Portfolio Management Support Services (including Asset Mgmt, Acquisitions)",
        "service": "Portfolio Management Support Services (including Asset Mgmt, Acquisitions)",
        "column_kind": "service",
        "phase_map": {
          "P": "source-unmarked",
          "A": "source-unmarked",
          "B": "source-unmarked",
          "C": "source-unmarked",
          "D": "source-unmarked",
          "E": "source-mapped",
          "F": "source-mapped",
          "G": "source-mapped",
          "H": "source-mapped",
          "RM": "source-unmarked"
        },
        "mapping_origin": "local-source-transcription; not business facts"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "svc_risk",
      "type": "guide:ea_adm_mapping",
      "name": "风险管理服务",
      "attributes": {
        "definition": "Risk Management Services",
        "service": "Risk Management Services",
        "column_kind": "service",
        "phase_map": {
          "P": "source-unmarked",
          "A": "source-mapped",
          "B": "source-unmarked",
          "C": "source-unmarked",
          "D": "source-unmarked",
          "E": "source-mapped",
          "F": "source-unmarked",
          "G": "source-mapped",
          "H": "source-mapped",
          "RM": "source-unmarked"
        },
        "mapping_origin": "local-source-transcription; not business facts"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "svc_sustainability",
      "type": "guide:ea_adm_mapping",
      "name": "可持续性管理支持服务",
      "attributes": {
        "definition": "Sustainability Management Support Services",
        "service": "Sustainability Management Support Services",
        "column_kind": "service",
        "phase_map": {
          "P": "source-unmarked",
          "A": "source-unmarked",
          "B": "source-mapped",
          "C": "source-mapped",
          "D": "source-mapped",
          "E": "source-mapped",
          "F": "source-unmarked",
          "G": "source-mapped",
          "H": "source-unmarked",
          "RM": "source-unmarked"
        },
        "mapping_origin": "local-source-transcription; not business facts"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "svc_enterprise_analysis",
      "type": "guide:ea_adm_mapping",
      "name": "企业分析与评估服务",
      "attributes": {
        "definition": "Enterprise Analysis and Assessment Services",
        "service": "Enterprise Analysis and Assessment Services",
        "column_kind": "service",
        "phase_map": {
          "P": "source-unmarked",
          "A": "source-unmarked",
          "B": "source-mapped",
          "C": "source-mapped",
          "D": "source-mapped",
          "E": "source-unmarked",
          "F": "source-mapped",
          "G": "source-mapped",
          "H": "source-mapped",
          "RM": "source-unmarked"
        },
        "mapping_origin": "local-source-transcription; not business facts"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "svc_capability",
      "type": "guide:ea_adm_mapping",
      "name": "能力规划支持服务",
      "attributes": {
        "definition": "Capability Planning Support Service",
        "service": "Capability Planning Support Service",
        "column_kind": "service",
        "phase_map": {
          "P": "source-unmarked",
          "A": "source-unmarked",
          "B": "source-mapped",
          "C": "source-unmarked",
          "D": "source-unmarked",
          "E": "source-unmarked",
          "F": "source-unmarked",
          "G": "source-unmarked",
          "H": "source-unmarked",
          "RM": "source-unmarked"
        },
        "mapping_origin": "local-source-transcription; not business facts"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cat_practice",
      "type": "guide:ea_adm_mapping",
      "name": "企业架构实践发展支持服务",
      "attributes": {
        "definition": "Enterprise Architecture Practice Development Support Services",
        "service": "Enterprise Architecture Practice Development Support Services",
        "column_kind": "category",
        "phase_map": {
          "P": "source-unmarked",
          "A": "source-unmarked",
          "B": "source-unmarked",
          "C": "source-unmarked",
          "D": "source-unmarked",
          "E": "source-unmarked",
          "F": "source-unmarked",
          "G": "source-unmarked",
          "H": "source-unmarked",
          "RM": "source-unmarked"
        },
        "mapping_origin": "local-source-transcription; not business facts"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "svc_process_improvement",
      "type": "guide:ea_adm_mapping",
      "name": "企业架构开发过程改进服务",
      "attributes": {
        "definition": "Enterprise Architecture Dev Process Improvement Service",
        "service": "Enterprise Architecture Dev Process Improvement Service",
        "column_kind": "service",
        "phase_map": {
          "P": "source-unmarked",
          "A": "source-unmarked",
          "B": "source-unmarked",
          "C": "source-unmarked",
          "D": "source-unmarked",
          "E": "source-unmarked",
          "F": "source-unmarked",
          "G": "source-unmarked",
          "H": "source-mapped",
          "RM": "source-unmarked"
        },
        "mapping_origin": "local-source-transcription; not business facts"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "extensions": {},
  "view": {
    "id": "v-ea-service-adm-reference-matrix",
    "artifact_id": "ea-service-catalog",
    "profile_id": "ea-service-adm-reference-matrix",
    "title": "EA服务×ADM来源参考矩阵／来源结构专用示例",
    "entity_ids": [
      "cat_req",
      "svc_stakeholders",
      "svc_business_value",
      "cat_arch_plan",
      "svc_arch_project_planning",
      "svc_arch_tailoring",
      "cat_design",
      "svc_vision",
      "svc_modeling",
      "svc_integration",
      "svc_compliance_dev",
      "cat_dev",
      "svc_standards",
      "svc_change",
      "svc_compliance_assessment",
      "svc_release",
      "cat_enterprise",
      "svc_portfolio",
      "svc_risk",
      "svc_sustainability",
      "svc_enterprise_analysis",
      "svc_capability",
      "cat_practice",
      "svc_process_improvement"
    ],
    "relationship_ids": [],
    "analysis": "明确来源结构、节点角色、流向与边界；未将相邻、颜色或布局当作企业事实。",
    "legend": "来源解释参考；24列/10行的转置表达。开发支持分类G格为不确定项，不能据此推断该分类所有服务适用。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile ea-service-adm-reference-matrix --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile ea-service-adm-reference-matrix --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
