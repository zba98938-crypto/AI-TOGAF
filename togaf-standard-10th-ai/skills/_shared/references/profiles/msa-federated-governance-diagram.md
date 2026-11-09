# MSA双轨治理与豁免过程／图形

`profile_id`: msa-federated-governance-diagram；`artifact_id`: microservice-technical-guidance；主责：[togaf-technology-architecture](../../../togaf-technology-architecture/SKILL.md)。

来源：G21I §5.3、表5-1、§12.2；G21I/fig5-2。

## 构图与定义状态

表示族：`deployment`；输出：`diagram`。规范版本：2.4。

{
  "id": "msa-federated-governance-diagram",
  "version": "2.4",
  "source_verified": false,
  "source_topology": "msa-governance",
  "separate_detail_ledger": true,
  "review_status": "awaiting-source-and-business-review",
  "companion_table_profile_id": "msa-federated-governance-process"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：ops:msa_governance。关系类型：ops:governance_supports, ops:governance_aligns, ops:governance_extends, ops:governance_constrains。

```json
{
  "entities": {
    "ops:msa_governance": [
      "authority",
      "roles",
      "decision",
      "decision_status",
      "waiver",
      "controls",
      "feedback",
      "scope",
      "mapping_origin",
      "evidence_detail"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 待决豁免不能被采用为已批准
- 四种关系不得统一为泛化依赖
- 治理有执行/反馈过程
- 项目图关系不冒称源图核实

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构完整案例；手工分析、表格操作语义，不冒称源图复刻。",
  "raw_input": "examples/addenda/operations/msa-federated-governance-process/raw-brief.md",
  "analysis_path": "examples/addenda/operations/msa-federated-governance-process/analysis.md",
  "sources": [
    {
      "id": "case-source",
      "kind": "example",
      "description": "海岚维修由业务赞助人审视投资价值，IT负责人要求生产访问和变更受控，EA委员会决定标准豁免。预约团队临时共享数据库的申请EX-1未获决定。项目架构师与团队拟在每次发布前四眼复核、最小权限保护管道、自动测试和持续监控。项目会议明确MSA控制支持IT治理；决策对齐EA；MSA过程扩展EA细节；EA规则约束MSA。此四关系是本项目映射，不是原图逐边转录。",
      "locator": "raw-brief.md"
    }
  ],
  "entities": [
    {
      "id": "GOV-CORP",
      "type": "ops:msa_governance",
      "name": "企业治理",
      "attributes": {
        "authority": "业务赞助人",
        "roles": {
          "企业架构师": "公司标准/主持评审委员会",
          "架构评审委员会": "符合性协调及豁免批准",
          "项目架构师": "MSA设计与跨方协调",
          "领域架构师": "领域限界上下文",
          "开发/运维/IT": "开发及日常运营，自治受企业/领域约束"
        },
        "decision": "两城扩展须有可运营性和业务价值证据",
        "decision_status": "proposed",
        "waiver": {
          "request": "none",
          "status": "not-applicable",
          "decision_evidence": "none",
          "approver": "none"
        },
        "controls": "关注投资与责任",
        "feedback": "每次发布核查控制证据；故障或偏离触发持续改进",
        "scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "mapping_origin": "project-proposal；不是G21I图5-1逐边复刻",
        "evidence_detail": "虚构治理访谈和待决EX-1"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "GOV-IT",
      "type": "ops:msa_governance",
      "name": "IT治理",
      "attributes": {
        "authority": "IT治理负责人",
        "roles": {
          "企业架构师": "公司标准/主持评审委员会",
          "架构评审委员会": "符合性协调及豁免批准",
          "项目架构师": "MSA设计与跨方协调",
          "领域架构师": "领域限界上下文",
          "开发/运维/IT": "开发及日常运营，自治受企业/领域约束"
        },
        "decision": "生产访问与变更必须受控",
        "decision_status": "project-policy-stated",
        "waiver": {
          "request": "none",
          "status": "not-applicable",
          "decision_evidence": "none",
          "approver": "none"
        },
        "controls": "生产管道最小权限、变更监控",
        "feedback": "每次发布核查控制证据；故障或偏离触发持续改进",
        "scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "mapping_origin": "project-proposal；不是G21I图5-1逐边复刻",
        "evidence_detail": "虚构治理访谈和待决EX-1"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "GOV-EA",
      "type": "ops:msa_governance",
      "name": "EA治理",
      "attributes": {
        "authority": "架构评审委员会",
        "roles": {
          "企业架构师": "公司标准/主持评审委员会",
          "架构评审委员会": "符合性协调及豁免批准",
          "项目架构师": "MSA设计与跨方协调",
          "领域架构师": "领域限界上下文",
          "开发/运维/IT": "开发及日常运营，自治受企业/领域约束"
        },
        "decision": "预约团队提出临时继续共享数据库的偏离；委员会尚未决定",
        "decision_status": "waiver-pending",
        "waiver": {
          "request": "EX-1",
          "status": "pending",
          "decision_evidence": "unknown",
          "approver": "架构评审委员会"
        },
        "controls": "申请EX-1明确范围/到期/风险，收到委员会决定前不能视为允许",
        "feedback": "每次发布核查控制证据；故障或偏离触发持续改进",
        "scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "mapping_origin": "project-proposal；不是G21I图5-1逐边复刻",
        "evidence_detail": "虚构治理访谈和待决EX-1"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "GOV-MSA",
      "type": "ops:msa_governance",
      "name": "MSA治理",
      "attributes": {
        "authority": "项目架构师与预约团队",
        "roles": {
          "企业架构师": "公司标准/主持评审委员会",
          "架构评审委员会": "符合性协调及豁免批准",
          "项目架构师": "MSA设计与跨方协调",
          "领域架构师": "领域限界上下文",
          "开发/运维/IT": "开发及日常运营，自治受企业/领域约束"
        },
        "decision": "计划发布前四眼复核，并持续复盘例外与监控",
        "decision_status": "planned",
        "waiver": {
          "request": "none",
          "status": "not-applicable",
          "decision_evidence": "none",
          "approver": "none"
        },
        "controls": "预发布评审、最小权限、自动测试、运行监控与反馈",
        "feedback": "每次发布核查控制证据；故障或偏离触发持续改进",
        "scope": "海岚家电维修（虚构），两城服务试点，2026年11月",
        "mapping_origin": "project-proposal；不是G21I图5-1逐边复刻",
        "evidence_detail": "虚构治理访谈和待决EX-1",
        "process_aspects": {
          "principles": "保持自治边界，豁免须由EA委员会决定；EX-1待决",
          "governing": "每次发布前四眼复核，监测偏离并纠偏",
          "governed": "预约服务的设计、构建、测试、发布和运行流程",
          "artifacts": "候选契约、EX-1申请、测试及监控回执；真实签署缺失",
          "roles": "项目/领域架构师、开发运维执行；架构委员会审定豁免",
          "technology": "受控管道、最小权限、自动测试、运行监控"
        }
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    }
  ],
  "relationships": [
    {
      "id": "GOV-R1",
      "type": "ops:governance_supports",
      "source": "GOV-MSA",
      "target": "GOV-IT",
      "label": "MSA控制支持IT服务治理",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "GOV-R2",
      "type": "ops:governance_aligns",
      "source": "GOV-MSA",
      "target": "GOV-EA",
      "label": "MSA决策对齐EA政策",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "GOV-R3",
      "type": "ops:governance_extends",
      "source": "GOV-MSA",
      "target": "GOV-EA",
      "label": "MSA增加频繁发布的过程细节",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "GOV-R4",
      "type": "ops:governance_constrains",
      "source": "GOV-EA",
      "target": "GOV-MSA",
      "label": "企业架构约束团队自治",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    }
  ],
  "extensions": {
    "relationship_types": {
      "ops:governance_supports": {
        "source_types": [
          "ops:msa_governance"
        ],
        "target_types": [
          "ops:msa_governance"
        ],
        "meaning": "MSA控制支持IT服务治理；项目明确方向；不声明原图箭头已核实"
      },
      "ops:governance_aligns": {
        "source_types": [
          "ops:msa_governance"
        ],
        "target_types": [
          "ops:msa_governance"
        ],
        "meaning": "MSA决策对齐EA政策；项目明确方向；不声明原图箭头已核实"
      },
      "ops:governance_extends": {
        "source_types": [
          "ops:msa_governance"
        ],
        "target_types": [
          "ops:msa_governance"
        ],
        "meaning": "MSA增加频繁发布的过程细节；项目明确方向；不声明原图箭头已核实"
      },
      "ops:governance_constrains": {
        "source_types": [
          "ops:msa_governance"
        ],
        "target_types": [
          "ops:msa_governance"
        ],
        "meaning": "企业架构约束团队自治；项目明确方向；不声明原图箭头已核实"
      }
    }
  },
  "states": [],
  "view": {
    "id": "v-msa-federated-governance-diagram",
    "artifact_id": "microservice-technical-guidance",
    "profile_id": "msa-federated-governance-diagram",
    "title": "MSA双轨治理与豁免过程／图形",
    "context": {
      "domains": [
        "business",
        "data",
        "application",
        "technology"
      ],
      "landscape": "capability",
      "purpose": "project",
      "abstraction": "logical",
      "evolution": "target"
    },
    "entity_ids": [
      "GOV-CORP",
      "GOV-IT",
      "GOV-EA",
      "GOV-MSA"
    ],
    "relationship_ids": [
      "GOV-R1",
      "GOV-R2",
      "GOV-R3",
      "GOV-R4"
    ],
    "analysis": "依据raw-brief.md的虚构材料，按analysis.md人工分析；生成器转换已审查模型。",
    "legend": "图形与表格复用同一ID；未知不等于无关系或不适用；项目映射不是原图逐格验收。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile msa-federated-governance-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile msa-federated-governance-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
