# 元数据集成组织备选

`profile_id`: metadata-central-hybrid-unified；`artifact_id`: metadata-integration-model；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G234/fig4-6；G234/fig4-7；G234/fig4-8。

## 构图与定义状态

表示族：`deployment`；输出：`diagram`。规范版本：2.3。

{
  "source_verified": false,
  "source_figure": "G234/fig4-7",
  "layout_notes": "集成风格与采集方式两个独立维度",
  "review_status": "source-topology-repaired-awaiting-independent-review",
  "source_topology": "metadata-integration",
  "version": "2.3"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：metadata_component, metadata_repository。关系类型：project:metadata_exchange。

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

- 集成风格与采集方式两个独立维度

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "来源结构指导的解释性示例；项目事实为假设；不代表原图逐像素复刻、标准认证或架构批准。",
  "sources": [
    {
      "id": "example-source",
      "kind": "example",
      "description": "专用拓扑验收示例：G234/fig4-6, G234/fig4-7, G234/fig4-8；来源图解释与候选企业场景分开。"
    }
  ],
  "entities": [
    {
      "id": "con-central",
      "type": "metadata_repository",
      "name": "集中式中央库",
      "attributes": {
        "definition": "统一访问副本；不迁移源方维护流程",
        "integration_style": "consolidation",
        "topology_role": "central",
        "authority": "copy-only",
        "workflow_owner": "external",
        "scope": "九个元数据域社区"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "con-glossary",
      "type": "metadata_component",
      "name": "词汇表、政策与质量社区",
      "attributes": {
        "definition": "外部保留本域主记录与维护流程",
        "integration_style": "consolidation",
        "topology_role": "community",
        "domain_key": "glossary",
        "repository_location": "external",
        "authority": "external-master"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "con-processes",
      "type": "metadata_component",
      "name": "业务流程社区",
      "attributes": {
        "definition": "外部保留本域主记录与维护流程",
        "integration_style": "consolidation",
        "topology_role": "community",
        "domain_key": "processes",
        "repository_location": "external",
        "authority": "external-master"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "con-application",
      "type": "metadata_component",
      "name": "应用存储库社区",
      "attributes": {
        "definition": "外部保留本域主记录与维护流程",
        "integration_style": "consolidation",
        "topology_role": "community",
        "domain_key": "application",
        "repository_location": "external",
        "authority": "external-master"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "con-technical",
      "type": "metadata_component",
      "name": "技术与运营元数据社区",
      "attributes": {
        "definition": "外部保留本域主记录与维护流程",
        "integration_style": "consolidation",
        "topology_role": "community",
        "domain_key": "technical",
        "repository_location": "external",
        "authority": "external-master"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "con-privacy",
      "type": "metadata_component",
      "name": "数据隐私社区",
      "attributes": {
        "definition": "外部保留本域主记录与维护流程",
        "integration_style": "consolidation",
        "topology_role": "community",
        "domain_key": "privacy",
        "repository_location": "external",
        "authority": "external-master"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "con-risk",
      "type": "metadata_component",
      "name": "风险管理社区",
      "attributes": {
        "definition": "外部保留本域主记录与维护流程",
        "integration_style": "consolidation",
        "topology_role": "community",
        "domain_key": "risk",
        "repository_location": "external",
        "authority": "external-master"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "con-security",
      "type": "metadata_component",
      "name": "安全管理社区",
      "attributes": {
        "definition": "外部保留本域主记录与维护流程",
        "integration_style": "consolidation",
        "topology_role": "community",
        "domain_key": "security",
        "repository_location": "external",
        "authority": "external-master"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "con-reference",
      "type": "metadata_component",
      "name": "参考数据社区",
      "attributes": {
        "definition": "外部保留本域主记录与维护流程",
        "integration_style": "consolidation",
        "topology_role": "community",
        "domain_key": "reference",
        "repository_location": "external",
        "authority": "external-master"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "con-governance",
      "type": "metadata_component",
      "name": "数据治理社区",
      "attributes": {
        "definition": "治理监督，不是独立存储库",
        "integration_style": "consolidation",
        "topology_role": "community",
        "domain_key": "governance",
        "repository_location": "none",
        "authority": "governance"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "hyb-central",
      "type": "metadata_repository",
      "name": "混合式中央库",
      "attributes": {
        "definition": "选定域主记录及工作流迁入中央",
        "integration_style": "hybrid",
        "topology_role": "central",
        "authority": "selected-scopes",
        "workflow_owner": "mixed",
        "scope": "九个元数据域社区"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "hyb-glossary",
      "type": "metadata_component",
      "name": "词汇表、政策与质量社区",
      "attributes": {
        "definition": "直接在中央维护本域元数据",
        "integration_style": "hybrid",
        "topology_role": "community",
        "domain_key": "glossary",
        "repository_location": "central",
        "authority": "central-master"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "hyb-processes",
      "type": "metadata_component",
      "name": "业务流程社区",
      "attributes": {
        "definition": "直接在中央维护本域元数据",
        "integration_style": "hybrid",
        "topology_role": "community",
        "domain_key": "processes",
        "repository_location": "central",
        "authority": "central-master"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "hyb-application",
      "type": "metadata_component",
      "name": "应用存储库社区",
      "attributes": {
        "definition": "外部保留本域主记录与维护流程",
        "integration_style": "hybrid",
        "topology_role": "community",
        "domain_key": "application",
        "repository_location": "external",
        "authority": "external-master"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "hyb-technical",
      "type": "metadata_component",
      "name": "技术与运营元数据社区",
      "attributes": {
        "definition": "外部保留本域主记录与维护流程",
        "integration_style": "hybrid",
        "topology_role": "community",
        "domain_key": "technical",
        "repository_location": "external",
        "authority": "external-master"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "hyb-privacy",
      "type": "metadata_component",
      "name": "数据隐私社区",
      "attributes": {
        "definition": "外部保留本域主记录与维护流程",
        "integration_style": "hybrid",
        "topology_role": "community",
        "domain_key": "privacy",
        "repository_location": "external",
        "authority": "external-master"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "hyb-risk",
      "type": "metadata_component",
      "name": "风险管理社区",
      "attributes": {
        "definition": "外部保留本域主记录与维护流程",
        "integration_style": "hybrid",
        "topology_role": "community",
        "domain_key": "risk",
        "repository_location": "external",
        "authority": "external-master"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "hyb-security",
      "type": "metadata_component",
      "name": "安全管理社区",
      "attributes": {
        "definition": "外部保留本域主记录与维护流程",
        "integration_style": "hybrid",
        "topology_role": "community",
        "domain_key": "security",
        "repository_location": "external",
        "authority": "external-master"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "hyb-reference",
      "type": "metadata_component",
      "name": "参考数据社区",
      "attributes": {
        "definition": "直接在中央维护本域元数据",
        "integration_style": "hybrid",
        "topology_role": "community",
        "domain_key": "reference",
        "repository_location": "central",
        "authority": "central-master"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "hyb-governance",
      "type": "metadata_component",
      "name": "数据治理社区",
      "attributes": {
        "definition": "治理监督，不是独立存储库",
        "integration_style": "hybrid",
        "topology_role": "community",
        "domain_key": "governance",
        "repository_location": "none",
        "authority": "governance"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "uni-central",
      "type": "metadata_repository",
      "name": "统一式中央库",
      "attributes": {
        "definition": "全范围主记录与维护工作流统一",
        "integration_style": "unified",
        "topology_role": "central",
        "authority": "all-scopes",
        "workflow_owner": "central",
        "scope": "九个元数据域社区"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "uni-glossary",
      "type": "metadata_component",
      "name": "词汇表、政策与质量社区",
      "attributes": {
        "definition": "直接在中央维护本域元数据",
        "integration_style": "unified",
        "topology_role": "community",
        "domain_key": "glossary",
        "repository_location": "central",
        "authority": "central-master"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "uni-processes",
      "type": "metadata_component",
      "name": "业务流程社区",
      "attributes": {
        "definition": "直接在中央维护本域元数据",
        "integration_style": "unified",
        "topology_role": "community",
        "domain_key": "processes",
        "repository_location": "central",
        "authority": "central-master"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "uni-application",
      "type": "metadata_component",
      "name": "应用存储库社区",
      "attributes": {
        "definition": "直接在中央维护本域元数据",
        "integration_style": "unified",
        "topology_role": "community",
        "domain_key": "application",
        "repository_location": "central",
        "authority": "central-master"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "uni-technical",
      "type": "metadata_component",
      "name": "技术与运营元数据社区",
      "attributes": {
        "definition": "直接在中央维护本域元数据",
        "integration_style": "unified",
        "topology_role": "community",
        "domain_key": "technical",
        "repository_location": "central",
        "authority": "central-master"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "uni-privacy",
      "type": "metadata_component",
      "name": "数据隐私社区",
      "attributes": {
        "definition": "直接在中央维护本域元数据",
        "integration_style": "unified",
        "topology_role": "community",
        "domain_key": "privacy",
        "repository_location": "central",
        "authority": "central-master"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "uni-risk",
      "type": "metadata_component",
      "name": "风险管理社区",
      "attributes": {
        "definition": "直接在中央维护本域元数据",
        "integration_style": "unified",
        "topology_role": "community",
        "domain_key": "risk",
        "repository_location": "central",
        "authority": "central-master"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "uni-security",
      "type": "metadata_component",
      "name": "安全管理社区",
      "attributes": {
        "definition": "直接在中央维护本域元数据",
        "integration_style": "unified",
        "topology_role": "community",
        "domain_key": "security",
        "repository_location": "central",
        "authority": "central-master"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "uni-reference",
      "type": "metadata_component",
      "name": "参考数据社区",
      "attributes": {
        "definition": "直接在中央维护本域元数据",
        "integration_style": "unified",
        "topology_role": "community",
        "domain_key": "reference",
        "repository_location": "central",
        "authority": "central-master"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "uni-governance",
      "type": "metadata_component",
      "name": "数据治理社区",
      "attributes": {
        "definition": "治理监督，不是独立存储库",
        "integration_style": "unified",
        "topology_role": "community",
        "domain_key": "governance",
        "repository_location": "none",
        "authority": "governance"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "con-glossary-in",
      "source": "con-glossary",
      "target": "con-central",
      "type": "project:metadata_exchange",
      "label": "来源向中央供副本",
      "attributes": {
        "flow_role": "copy",
        "data_scope": "glossary",
        "meaning": "来源向中央供副本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "con-processes-in",
      "source": "con-processes",
      "target": "con-central",
      "type": "project:metadata_exchange",
      "label": "来源向中央供副本",
      "attributes": {
        "flow_role": "copy",
        "data_scope": "processes",
        "meaning": "来源向中央供副本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "con-application-in",
      "source": "con-application",
      "target": "con-central",
      "type": "project:metadata_exchange",
      "label": "来源向中央供副本",
      "attributes": {
        "flow_role": "copy",
        "data_scope": "application",
        "meaning": "来源向中央供副本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "con-technical-in",
      "source": "con-technical",
      "target": "con-central",
      "type": "project:metadata_exchange",
      "label": "来源向中央供副本",
      "attributes": {
        "flow_role": "copy",
        "data_scope": "technical",
        "meaning": "来源向中央供副本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "con-privacy-in",
      "source": "con-privacy",
      "target": "con-central",
      "type": "project:metadata_exchange",
      "label": "来源向中央供副本",
      "attributes": {
        "flow_role": "copy",
        "data_scope": "privacy",
        "meaning": "来源向中央供副本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "con-risk-in",
      "source": "con-risk",
      "target": "con-central",
      "type": "project:metadata_exchange",
      "label": "来源向中央供副本",
      "attributes": {
        "flow_role": "copy",
        "data_scope": "risk",
        "meaning": "来源向中央供副本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "con-security-in",
      "source": "con-security",
      "target": "con-central",
      "type": "project:metadata_exchange",
      "label": "来源向中央供副本",
      "attributes": {
        "flow_role": "copy",
        "data_scope": "security",
        "meaning": "来源向中央供副本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "con-reference-in",
      "source": "con-reference",
      "target": "con-central",
      "type": "project:metadata_exchange",
      "label": "来源向中央供副本",
      "attributes": {
        "flow_role": "copy",
        "data_scope": "reference",
        "meaning": "来源向中央供副本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "con-governance-in",
      "source": "con-governance",
      "target": "con-central",
      "type": "project:metadata_exchange",
      "label": "治理输入",
      "attributes": {
        "flow_role": "governance",
        "data_scope": "governance",
        "meaning": "治理输入"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "con-governance-out",
      "source": "con-central",
      "target": "con-governance",
      "type": "project:metadata_exchange",
      "label": "治理反馈",
      "attributes": {
        "flow_role": "governance",
        "data_scope": "governance",
        "meaning": "治理反馈"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "hyb-glossary-in",
      "source": "hyb-glossary",
      "target": "hyb-central",
      "type": "project:metadata_exchange",
      "label": "中央直接维护",
      "attributes": {
        "flow_role": "write",
        "data_scope": "glossary",
        "meaning": "中央直接维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "hyb-glossary-out",
      "source": "hyb-central",
      "target": "hyb-glossary",
      "type": "project:metadata_exchange",
      "label": "社区读取中央元数据",
      "attributes": {
        "flow_role": "read",
        "data_scope": "glossary",
        "meaning": "社区读取中央元数据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "hyb-processes-in",
      "source": "hyb-processes",
      "target": "hyb-central",
      "type": "project:metadata_exchange",
      "label": "中央直接维护",
      "attributes": {
        "flow_role": "write",
        "data_scope": "processes",
        "meaning": "中央直接维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "hyb-processes-out",
      "source": "hyb-central",
      "target": "hyb-processes",
      "type": "project:metadata_exchange",
      "label": "社区读取中央元数据",
      "attributes": {
        "flow_role": "read",
        "data_scope": "processes",
        "meaning": "社区读取中央元数据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "hyb-application-in",
      "source": "hyb-application",
      "target": "hyb-central",
      "type": "project:metadata_exchange",
      "label": "来源向中央供副本",
      "attributes": {
        "flow_role": "copy",
        "data_scope": "application",
        "meaning": "来源向中央供副本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "hyb-technical-in",
      "source": "hyb-technical",
      "target": "hyb-central",
      "type": "project:metadata_exchange",
      "label": "来源向中央供副本",
      "attributes": {
        "flow_role": "copy",
        "data_scope": "technical",
        "meaning": "来源向中央供副本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "hyb-privacy-in",
      "source": "hyb-privacy",
      "target": "hyb-central",
      "type": "project:metadata_exchange",
      "label": "来源向中央供副本",
      "attributes": {
        "flow_role": "copy",
        "data_scope": "privacy",
        "meaning": "来源向中央供副本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "hyb-risk-in",
      "source": "hyb-risk",
      "target": "hyb-central",
      "type": "project:metadata_exchange",
      "label": "来源向中央供副本",
      "attributes": {
        "flow_role": "copy",
        "data_scope": "risk",
        "meaning": "来源向中央供副本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "hyb-security-in",
      "source": "hyb-security",
      "target": "hyb-central",
      "type": "project:metadata_exchange",
      "label": "来源向中央供副本",
      "attributes": {
        "flow_role": "copy",
        "data_scope": "security",
        "meaning": "来源向中央供副本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "hyb-reference-in",
      "source": "hyb-reference",
      "target": "hyb-central",
      "type": "project:metadata_exchange",
      "label": "中央直接维护",
      "attributes": {
        "flow_role": "write",
        "data_scope": "reference",
        "meaning": "中央直接维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "hyb-reference-out",
      "source": "hyb-central",
      "target": "hyb-reference",
      "type": "project:metadata_exchange",
      "label": "社区读取中央元数据",
      "attributes": {
        "flow_role": "read",
        "data_scope": "reference",
        "meaning": "社区读取中央元数据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "hyb-governance-in",
      "source": "hyb-governance",
      "target": "hyb-central",
      "type": "project:metadata_exchange",
      "label": "治理输入",
      "attributes": {
        "flow_role": "governance",
        "data_scope": "governance",
        "meaning": "治理输入"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "hyb-governance-out",
      "source": "hyb-central",
      "target": "hyb-governance",
      "type": "project:metadata_exchange",
      "label": "治理反馈",
      "attributes": {
        "flow_role": "governance",
        "data_scope": "governance",
        "meaning": "治理反馈"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "uni-glossary-in",
      "source": "uni-glossary",
      "target": "uni-central",
      "type": "project:metadata_exchange",
      "label": "中央直接维护",
      "attributes": {
        "flow_role": "write",
        "data_scope": "glossary",
        "meaning": "中央直接维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "uni-glossary-out",
      "source": "uni-central",
      "target": "uni-glossary",
      "type": "project:metadata_exchange",
      "label": "社区读取中央元数据",
      "attributes": {
        "flow_role": "read",
        "data_scope": "glossary",
        "meaning": "社区读取中央元数据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "uni-processes-in",
      "source": "uni-processes",
      "target": "uni-central",
      "type": "project:metadata_exchange",
      "label": "中央直接维护",
      "attributes": {
        "flow_role": "write",
        "data_scope": "processes",
        "meaning": "中央直接维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "uni-processes-out",
      "source": "uni-central",
      "target": "uni-processes",
      "type": "project:metadata_exchange",
      "label": "社区读取中央元数据",
      "attributes": {
        "flow_role": "read",
        "data_scope": "processes",
        "meaning": "社区读取中央元数据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "uni-application-in",
      "source": "uni-application",
      "target": "uni-central",
      "type": "project:metadata_exchange",
      "label": "中央直接维护",
      "attributes": {
        "flow_role": "write",
        "data_scope": "application",
        "meaning": "中央直接维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "uni-application-out",
      "source": "uni-central",
      "target": "uni-application",
      "type": "project:metadata_exchange",
      "label": "社区读取中央元数据",
      "attributes": {
        "flow_role": "read",
        "data_scope": "application",
        "meaning": "社区读取中央元数据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "uni-technical-in",
      "source": "uni-technical",
      "target": "uni-central",
      "type": "project:metadata_exchange",
      "label": "中央直接维护",
      "attributes": {
        "flow_role": "write",
        "data_scope": "technical",
        "meaning": "中央直接维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "uni-technical-out",
      "source": "uni-central",
      "target": "uni-technical",
      "type": "project:metadata_exchange",
      "label": "社区读取中央元数据",
      "attributes": {
        "flow_role": "read",
        "data_scope": "technical",
        "meaning": "社区读取中央元数据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "uni-privacy-in",
      "source": "uni-privacy",
      "target": "uni-central",
      "type": "project:metadata_exchange",
      "label": "中央直接维护",
      "attributes": {
        "flow_role": "write",
        "data_scope": "privacy",
        "meaning": "中央直接维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "uni-privacy-out",
      "source": "uni-central",
      "target": "uni-privacy",
      "type": "project:metadata_exchange",
      "label": "社区读取中央元数据",
      "attributes": {
        "flow_role": "read",
        "data_scope": "privacy",
        "meaning": "社区读取中央元数据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "uni-risk-in",
      "source": "uni-risk",
      "target": "uni-central",
      "type": "project:metadata_exchange",
      "label": "中央直接维护",
      "attributes": {
        "flow_role": "write",
        "data_scope": "risk",
        "meaning": "中央直接维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "uni-risk-out",
      "source": "uni-central",
      "target": "uni-risk",
      "type": "project:metadata_exchange",
      "label": "社区读取中央元数据",
      "attributes": {
        "flow_role": "read",
        "data_scope": "risk",
        "meaning": "社区读取中央元数据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "uni-security-in",
      "source": "uni-security",
      "target": "uni-central",
      "type": "project:metadata_exchange",
      "label": "中央直接维护",
      "attributes": {
        "flow_role": "write",
        "data_scope": "security",
        "meaning": "中央直接维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "uni-reference-in",
      "source": "uni-reference",
      "target": "uni-central",
      "type": "project:metadata_exchange",
      "label": "中央直接维护",
      "attributes": {
        "flow_role": "write",
        "data_scope": "reference",
        "meaning": "中央直接维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "uni-reference-out",
      "source": "uni-central",
      "target": "uni-reference",
      "type": "project:metadata_exchange",
      "label": "社区读取中央元数据",
      "attributes": {
        "flow_role": "read",
        "data_scope": "reference",
        "meaning": "社区读取中央元数据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "uni-governance-in",
      "source": "uni-governance",
      "target": "uni-central",
      "type": "project:metadata_exchange",
      "label": "治理输入",
      "attributes": {
        "flow_role": "governance",
        "data_scope": "governance",
        "meaning": "治理输入"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "uni-governance-out",
      "source": "uni-central",
      "target": "uni-governance",
      "type": "project:metadata_exchange",
      "label": "治理反馈",
      "attributes": {
        "flow_role": "governance",
        "data_scope": "governance",
        "meaning": "治理反馈"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "extensions": {
    "relationship_types": {
      "project:metadata_exchange": {
        "source_types": [
          "metadata_repository",
          "metadata_component"
        ],
        "target_types": [
          "metadata_repository",
          "metadata_component"
        ],
        "meaning": "指定元数据范围的供副本、读写或治理交换；关系角色在flow_role中明示。"
      }
    }
  },
  "view": {
    "id": "v-metadata-central-hybrid-unified",
    "artifact_id": "metadata-integration-model",
    "profile_id": "metadata-central-hybrid-unified",
    "title": "元数据集成组织备选／来源结构专用示例",
    "entity_ids": [
      "con-central",
      "con-glossary",
      "con-processes",
      "con-application",
      "con-technical",
      "con-privacy",
      "con-risk",
      "con-security",
      "con-reference",
      "con-governance",
      "hyb-central",
      "hyb-glossary",
      "hyb-processes",
      "hyb-application",
      "hyb-technical",
      "hyb-privacy",
      "hyb-risk",
      "hyb-security",
      "hyb-reference",
      "hyb-governance",
      "uni-central",
      "uni-glossary",
      "uni-processes",
      "uni-application",
      "uni-technical",
      "uni-privacy",
      "uni-risk",
      "uni-security",
      "uni-reference",
      "uni-governance"
    ],
    "relationship_ids": [
      "con-glossary-in",
      "con-processes-in",
      "con-application-in",
      "con-technical-in",
      "con-privacy-in",
      "con-risk-in",
      "con-security-in",
      "con-reference-in",
      "con-governance-in",
      "con-governance-out",
      "hyb-glossary-in",
      "hyb-glossary-out",
      "hyb-processes-in",
      "hyb-processes-out",
      "hyb-application-in",
      "hyb-technical-in",
      "hyb-privacy-in",
      "hyb-risk-in",
      "hyb-security-in",
      "hyb-reference-in",
      "hyb-reference-out",
      "hyb-governance-in",
      "hyb-governance-out",
      "uni-glossary-in",
      "uni-glossary-out",
      "uni-processes-in",
      "uni-processes-out",
      "uni-application-in",
      "uni-application-out",
      "uni-technical-in",
      "uni-technical-out",
      "uni-privacy-in",
      "uni-privacy-out",
      "uni-risk-in",
      "uni-risk-out",
      "uni-security-in",
      "uni-reference-in",
      "uni-reference-out",
      "uni-governance-in",
      "uni-governance-out"
    ],
    "analysis": "明确来源结构、节点角色、流向与边界；未将相邻、颜色或布局当作企业事实。",
    "legend": "虚构候选或来源解释；相同ID表示同一对象。按专用线型、区域与编号语义读取；工程生成不授予来源等价或业务验收。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile metadata-central-hybrid-unified --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile metadata-central-hybrid-unified --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
