# 安全与ADM概念整合

`profile_id`: security-adm-concept-map；`artifact_id`: security-blueprint；主责：[togaf-security-risk](../../../togaf-security-risk/SKILL.md)。

来源：G152/fig1-1。

## 构图与定义状态

表示族：`deployment`；输出：`diagram`。规范版本：2.3。

{
  "id": "security-adm-concept-map",
  "version": "2.3",
  "source_verified": false,
  "source_figure": "G152/fig1-1",
  "source_topology": "security-adm-map",
  "separate_detail_ledger": true,
  "review_status": "source-topology-registered-awaiting-independent-review",
  "layout_notes": "阶段—概念组无方向关联；H 无概念组"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：adm_phase, erm_process, ism_process, security_risk_concept, security_service。关系类型：project:associates, project:catalog_expands, project:continues。

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

- 阶段—概念组无方向关联；H 无概念组
- 下划线概念为 ISM/ERM 新增

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "来源结构指导的解释性示例；项目事实为假设；不代表原图逐像素复刻、标准认证或架构批准。",
  "sources": [
    {
      "id": "example-source",
      "kind": "example",
      "description": "专用拓扑验收示例：G152/fig1-1；来源图解释与候选企业场景分开。"
    }
  ],
  "entities": [
    {
      "id": "phase-P",
      "type": "adm_phase",
      "name": "Preliminary",
      "attributes": {
        "definition": "ADM 阶段，不是自动批准点",
        "phase_code": "P"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "phase-A",
      "type": "adm_phase",
      "name": "A. Architecture Vision",
      "attributes": {
        "definition": "ADM 阶段，不是自动批准点",
        "phase_code": "A"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "phase-B",
      "type": "adm_phase",
      "name": "B. Business Architecture",
      "attributes": {
        "definition": "ADM 阶段，不是自动批准点",
        "phase_code": "B"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "phase-C",
      "type": "adm_phase",
      "name": "C. Information Systems Architectures",
      "attributes": {
        "definition": "ADM 阶段，不是自动批准点",
        "phase_code": "C"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "phase-D",
      "type": "adm_phase",
      "name": "D. Technology Architecture",
      "attributes": {
        "definition": "ADM 阶段，不是自动批准点",
        "phase_code": "D"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "phase-E",
      "type": "adm_phase",
      "name": "E. Opportunities and Solutions",
      "attributes": {
        "definition": "ADM 阶段，不是自动批准点",
        "phase_code": "E"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "phase-F",
      "type": "adm_phase",
      "name": "F. Migration Planning",
      "attributes": {
        "definition": "ADM 阶段，不是自动批准点",
        "phase_code": "F"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "phase-G",
      "type": "adm_phase",
      "name": "G. Implementation Governance",
      "attributes": {
        "definition": "ADM 阶段，不是自动批准点",
        "phase_code": "G"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "phase-H",
      "type": "adm_phase",
      "name": "H. Architecture Change Management",
      "attributes": {
        "definition": "ADM 阶段，不是自动批准点",
        "phase_code": "H"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "phase-RM",
      "type": "adm_phase",
      "name": "Requirements Management",
      "attributes": {
        "definition": "ADM 阶段，不是自动批准点",
        "phase_code": "RM"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-business_drivers",
      "type": "security_risk_concept",
      "name": "业务驱动 / 目标",
      "attributes": {
        "definition": "来源概念：业务驱动 / 目标",
        "concept_key": "business_drivers",
        "phase_code": "P",
        "ism_erm_addition": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-security_principles",
      "type": "security_risk_concept",
      "name": "安全原则",
      "attributes": {
        "definition": "来源概念：安全原则",
        "concept_key": "security_principles",
        "phase_code": "P",
        "ism_erm_addition": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-risk_appetite",
      "type": "security_risk_concept",
      "name": "风险偏好",
      "attributes": {
        "definition": "来源概念：风险偏好",
        "concept_key": "risk_appetite",
        "phase_code": "P",
        "ism_erm_addition": true
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-key_risk_areas",
      "type": "security_risk_concept",
      "name": "关键风险领域 / 业务影响",
      "attributes": {
        "definition": "来源概念：关键风险领域 / 业务影响",
        "concept_key": "key_risk_areas",
        "phase_code": "P",
        "ism_erm_addition": true
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-security_resource_plan",
      "type": "security_risk_concept",
      "name": "安全资源计划",
      "attributes": {
        "definition": "来源概念：安全资源计划",
        "concept_key": "security_resource_plan",
        "phase_code": "A",
        "ism_erm_addition": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-security_policy_architecture",
      "type": "security_risk_concept",
      "name": "安全政策架构",
      "attributes": {
        "definition": "来源概念：安全政策架构",
        "concept_key": "security_policy_architecture",
        "phase_code": "B",
        "ism_erm_addition": true
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-security_domain_model",
      "type": "security_risk_concept",
      "name": "安全域模型",
      "attributes": {
        "definition": "来源概念：安全域模型",
        "concept_key": "security_domain_model",
        "phase_code": "B",
        "ism_erm_addition": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-trust_framework",
      "type": "security_risk_concept",
      "name": "信任框架",
      "attributes": {
        "definition": "来源概念：信任框架",
        "concept_key": "trust_framework",
        "phase_code": "B",
        "ism_erm_addition": true
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-risk_assessment",
      "type": "security_risk_concept",
      "name": "风险评估",
      "attributes": {
        "definition": "来源概念：风险评估",
        "concept_key": "risk_assessment",
        "phase_code": "B",
        "ism_erm_addition": true
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-business_risk_model",
      "type": "security_risk_concept",
      "name": "业务风险模型 / 风险登记",
      "attributes": {
        "definition": "来源概念：业务风险模型 / 风险登记",
        "concept_key": "business_risk_model",
        "phase_code": "B",
        "ism_erm_addition": true
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-law_register",
      "type": "security_risk_concept",
      "name": "适用法律法规登记",
      "attributes": {
        "definition": "来源概念：适用法律法规登记",
        "concept_key": "law_register",
        "phase_code": "B",
        "ism_erm_addition": true
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-control_framework_register",
      "type": "security_risk_concept",
      "name": "适用控制框架登记",
      "attributes": {
        "definition": "来源概念：适用控制框架登记",
        "concept_key": "control_framework_register",
        "phase_code": "B",
        "ism_erm_addition": true
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-security_services_catalog",
      "type": "security_risk_concept",
      "name": "安全服务目录",
      "attributes": {
        "definition": "来源概念：安全服务目录",
        "concept_key": "security_services_catalog",
        "phase_code": "C",
        "ism_erm_addition": true
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-security_classification",
      "type": "security_risk_concept",
      "name": "安全分类",
      "attributes": {
        "definition": "来源概念：安全分类",
        "concept_key": "security_classification",
        "phase_code": "C",
        "ism_erm_addition": true
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-data_quality",
      "type": "security_risk_concept",
      "name": "数据质量",
      "attributes": {
        "definition": "来源概念：数据质量",
        "concept_key": "data_quality",
        "phase_code": "C",
        "ism_erm_addition": true
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-security_standards",
      "type": "security_risk_concept",
      "name": "安全标准",
      "attributes": {
        "definition": "来源概念：安全标准",
        "concept_key": "security_standards",
        "phase_code": "D",
        "ism_erm_addition": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-business_attribute_profile",
      "type": "security_risk_concept",
      "name": "业务属性概况",
      "attributes": {
        "definition": "来源概念：业务属性概况",
        "concept_key": "business_attribute_profile",
        "phase_code": "E",
        "ism_erm_addition": true
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-control_objectives",
      "type": "security_risk_concept",
      "name": "控制目标 / 安全目标",
      "attributes": {
        "definition": "来源概念：控制目标 / 安全目标",
        "concept_key": "control_objectives",
        "phase_code": "E",
        "ism_erm_addition": true
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-risk_mitigation_plan",
      "type": "security_risk_concept",
      "name": "风险缓解计划",
      "attributes": {
        "definition": "来源概念：风险缓解计划",
        "concept_key": "risk_mitigation_plan",
        "phase_code": "F",
        "ism_erm_addition": false
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-security_audit",
      "type": "security_risk_concept",
      "name": "安全审计",
      "attributes": {
        "definition": "来源概念：安全审计",
        "concept_key": "security_audit",
        "phase_code": "G",
        "ism_erm_addition": true
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "c-security_training",
      "type": "security_risk_concept",
      "name": "安全培训与意识",
      "attributes": {
        "definition": "来源概念：安全培训与意识",
        "concept_key": "security_training",
        "phase_code": "G",
        "ism_erm_addition": true
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "ism",
      "type": "ism_process",
      "name": "信息安全管理",
      "attributes": {
        "definition": "持续循环，不是一次活动"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "erm",
      "type": "erm_process",
      "name": "企业风险管理",
      "attributes": {
        "definition": "持续循环，不是一次活动"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "svc-iam",
      "type": "security_service",
      "name": "身份与访问管理",
      "attributes": {
        "definition": "服务目录展开项"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "svc-mon",
      "type": "security_service",
      "name": "安全监控",
      "attributes": {
        "definition": "服务目录展开项"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "assoc-business_drivers",
      "source": "phase-P",
      "target": "c-business_drivers",
      "type": "project:associates",
      "label": "阶段关联概念组",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "阶段关联概念组"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assoc-security_principles",
      "source": "phase-P",
      "target": "c-security_principles",
      "type": "project:associates",
      "label": "阶段关联概念组",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "阶段关联概念组"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assoc-risk_appetite",
      "source": "phase-P",
      "target": "c-risk_appetite",
      "type": "project:associates",
      "label": "阶段关联概念组",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "阶段关联概念组"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assoc-key_risk_areas",
      "source": "phase-P",
      "target": "c-key_risk_areas",
      "type": "project:associates",
      "label": "阶段关联概念组",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "阶段关联概念组"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assoc-security_resource_plan",
      "source": "phase-A",
      "target": "c-security_resource_plan",
      "type": "project:associates",
      "label": "阶段关联概念组",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "阶段关联概念组"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assoc-security_policy_architecture",
      "source": "phase-B",
      "target": "c-security_policy_architecture",
      "type": "project:associates",
      "label": "阶段关联概念组",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "阶段关联概念组"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assoc-security_domain_model",
      "source": "phase-B",
      "target": "c-security_domain_model",
      "type": "project:associates",
      "label": "阶段关联概念组",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "阶段关联概念组"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assoc-trust_framework",
      "source": "phase-B",
      "target": "c-trust_framework",
      "type": "project:associates",
      "label": "阶段关联概念组",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "阶段关联概念组"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assoc-risk_assessment",
      "source": "phase-B",
      "target": "c-risk_assessment",
      "type": "project:associates",
      "label": "阶段关联概念组",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "阶段关联概念组"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assoc-business_risk_model",
      "source": "phase-B",
      "target": "c-business_risk_model",
      "type": "project:associates",
      "label": "阶段关联概念组",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "阶段关联概念组"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assoc-law_register",
      "source": "phase-B",
      "target": "c-law_register",
      "type": "project:associates",
      "label": "阶段关联概念组",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "阶段关联概念组"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assoc-control_framework_register",
      "source": "phase-B",
      "target": "c-control_framework_register",
      "type": "project:associates",
      "label": "阶段关联概念组",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "阶段关联概念组"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assoc-security_services_catalog",
      "source": "phase-C",
      "target": "c-security_services_catalog",
      "type": "project:associates",
      "label": "阶段关联概念组",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "阶段关联概念组"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assoc-security_classification",
      "source": "phase-C",
      "target": "c-security_classification",
      "type": "project:associates",
      "label": "阶段关联概念组",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "阶段关联概念组"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assoc-data_quality",
      "source": "phase-C",
      "target": "c-data_quality",
      "type": "project:associates",
      "label": "阶段关联概念组",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "阶段关联概念组"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assoc-security_standards",
      "source": "phase-D",
      "target": "c-security_standards",
      "type": "project:associates",
      "label": "阶段关联概念组",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "阶段关联概念组"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assoc-business_attribute_profile",
      "source": "phase-E",
      "target": "c-business_attribute_profile",
      "type": "project:associates",
      "label": "阶段关联概念组",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "阶段关联概念组"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assoc-control_objectives",
      "source": "phase-E",
      "target": "c-control_objectives",
      "type": "project:associates",
      "label": "阶段关联概念组",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "阶段关联概念组"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assoc-risk_mitigation_plan",
      "source": "phase-F",
      "target": "c-risk_mitigation_plan",
      "type": "project:associates",
      "label": "阶段关联概念组",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "阶段关联概念组"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assoc-security_audit",
      "source": "phase-G",
      "target": "c-security_audit",
      "type": "project:associates",
      "label": "阶段关联概念组",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "阶段关联概念组"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assoc-security_training",
      "source": "phase-G",
      "target": "c-security_training",
      "type": "project:associates",
      "label": "阶段关联概念组",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "阶段关联概念组"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "ism-loop",
      "source": "ism",
      "target": "ism",
      "type": "project:continues",
      "label": "ISM 持续循环",
      "attributes": {
        "meaning": "ISM 持续循环"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "erm-loop",
      "source": "erm",
      "target": "erm",
      "type": "project:continues",
      "label": "ERM 持续循环",
      "attributes": {
        "meaning": "ERM 持续循环"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cat-iam",
      "source": "c-security_services_catalog",
      "target": "svc-iam",
      "type": "project:catalog_expands",
      "label": "目录展开",
      "attributes": {
        "meaning": "目录展开"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cat-mon",
      "source": "c-security_services_catalog",
      "target": "svc-mon",
      "type": "project:catalog_expands",
      "label": "目录展开",
      "attributes": {
        "meaning": "目录展开"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assoc-shared-business_drivers",
      "source": "phase-A",
      "target": "c-business_drivers",
      "type": "project:associates",
      "label": "P/A 共享概念组",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "P/A 共享概念组"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assoc-shared-security_principles",
      "source": "phase-A",
      "target": "c-security_principles",
      "type": "project:associates",
      "label": "P/A 共享概念组",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "P/A 共享概念组"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assoc-shared-risk_appetite",
      "source": "phase-A",
      "target": "c-risk_appetite",
      "type": "project:associates",
      "label": "P/A 共享概念组",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "P/A 共享概念组"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assoc-shared-key_risk_areas",
      "source": "phase-A",
      "target": "c-key_risk_areas",
      "type": "project:associates",
      "label": "P/A 共享概念组",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "P/A 共享概念组"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assoc-shared-security_resource_plan",
      "source": "phase-P",
      "target": "c-security_resource_plan",
      "type": "project:associates",
      "label": "P/A 共享概念组",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "P/A 共享概念组"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assoc-rm-business_attribute_profile",
      "source": "phase-RM",
      "target": "c-business_attribute_profile",
      "type": "project:associates",
      "label": "持续需求管理关联",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "持续需求管理关联"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "assoc-rm-control_objectives",
      "source": "phase-RM",
      "target": "c-control_objectives",
      "type": "project:associates",
      "label": "持续需求管理关联",
      "attributes": {
        "notation": "unarrowed",
        "meaning": "持续需求管理关联"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "extensions": {
    "relationship_types": {
      "project:associates": {
        "meaning": "无方向关联",
        "source_types": [
          "adm_phase"
        ],
        "target_types": [
          "security_risk_concept"
        ]
      },
      "project:catalog_expands": {
        "meaning": "目录展开",
        "source_types": [
          "security_risk_concept"
        ],
        "target_types": [
          "security_service"
        ]
      },
      "project:continues": {
        "meaning": "持续循环",
        "source_types": [
          "ism_process",
          "erm_process"
        ],
        "target_types": [
          "ism_process",
          "erm_process"
        ]
      }
    }
  },
  "view": {
    "id": "v-security-adm-concept-map",
    "artifact_id": "security-blueprint",
    "profile_id": "security-adm-concept-map",
    "title": "安全与ADM概念整合／来源结构专用示例",
    "entity_ids": [
      "phase-P",
      "phase-A",
      "phase-B",
      "phase-C",
      "phase-D",
      "phase-E",
      "phase-F",
      "phase-G",
      "phase-H",
      "phase-RM",
      "c-business_drivers",
      "c-security_principles",
      "c-risk_appetite",
      "c-key_risk_areas",
      "c-security_resource_plan",
      "c-security_policy_architecture",
      "c-security_domain_model",
      "c-trust_framework",
      "c-risk_assessment",
      "c-business_risk_model",
      "c-law_register",
      "c-control_framework_register",
      "c-security_services_catalog",
      "c-security_classification",
      "c-data_quality",
      "c-security_standards",
      "c-business_attribute_profile",
      "c-control_objectives",
      "c-risk_mitigation_plan",
      "c-security_audit",
      "c-security_training",
      "ism",
      "erm",
      "svc-iam",
      "svc-mon"
    ],
    "relationship_ids": [
      "assoc-business_drivers",
      "assoc-security_principles",
      "assoc-risk_appetite",
      "assoc-key_risk_areas",
      "assoc-security_resource_plan",
      "assoc-security_policy_architecture",
      "assoc-security_domain_model",
      "assoc-trust_framework",
      "assoc-risk_assessment",
      "assoc-business_risk_model",
      "assoc-law_register",
      "assoc-control_framework_register",
      "assoc-security_services_catalog",
      "assoc-security_classification",
      "assoc-data_quality",
      "assoc-security_standards",
      "assoc-business_attribute_profile",
      "assoc-control_objectives",
      "assoc-risk_mitigation_plan",
      "assoc-security_audit",
      "assoc-security_training",
      "ism-loop",
      "erm-loop",
      "cat-iam",
      "cat-mon",
      "assoc-shared-business_drivers",
      "assoc-shared-security_principles",
      "assoc-shared-risk_appetite",
      "assoc-shared-key_risk_areas",
      "assoc-shared-security_resource_plan",
      "assoc-rm-business_attribute_profile",
      "assoc-rm-control_objectives"
    ],
    "analysis": "明确来源结构、节点角色、流向与边界；未将相邻、颜色或布局当作企业事实。",
    "legend": "虚构候选或来源解释；相同ID表示同一对象。工程生成不授予来源等价或业务验收。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile security-adm-concept-map --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile security-adm-concept-map --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
