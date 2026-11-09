# 架构项目管理策略

`profile_id`: project-management-strategy-default；`artifact_id`: project-management-strategy；主责：[togaf-architecture-workbench](../../../togaf-architecture-workbench/SKILL.md)。

来源：G188 §3.1.8 L541–631；G188 §4.2.1 L1524–1531。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：1.0。

{
  "id": "project-management-strategy-default",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "按已核查的来源结构参数化；参考图与业务实例的验收分别进行。",
  "structure_basis": "正文定义的工作产品；记录表是项目操作表示法，不冒充来源原图"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:project-management-strategy。关系类型：。

```json
{
  "entities": {
    "guide:project-management-strategy": [
      "project_scope",
      "selected_method",
      "method_tailoring",
      "project_governance",
      "architecture_governance",
      "confirmation_state",
      "topics",
      "analysis_result",
      "raw_material_refs"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 对象、关系、必要属性均可追溯并得到表达
- 参考内容不自动成为项目事实；未知项保持显式
- 四核心方面来自§3.1.8，配置管理来自§4.2.1
- 项目风险与架构愿景/实现风险不混淆
- 质量完备不等于已验收
- 管理阶段与ADM阶段无需一一对应
- 未经批准的变更不得纳入批准基线
- 容差和频率是项目约定，不是TOGAF标准阈值

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构案例；规则不是TOGAF规定",
  "sources": [
    {
      "id": "M-R1",
      "kind": "example",
      "description": "馆群架构项目采用机构既有项目管理框架补充ADM A–F。项目治理由项目指导组负责时间预算质量；架构委员会负责跨分馆架构一致性。PMO维护CONFIG-REG项目配置记录，逐个保存批准的范围、产品、进度版本和审批记录；未批准内容只能存在候选区。",
      "locator": "raw-materials.json#M-R1"
    },
    {
      "id": "M-R2",
      "kind": "example",
      "description": "风险按交付风险与架构实现风险分开登记，每周识别、定性复评并指定应对责任人；没有获批的概率/损失数据时不出定量等级。交付物必须可追溯到需求，由编制者先自查、业务代表评审、架构委员会检查一致性，再由交付物章程指定的业务验收人确认；每份章程说明范围、输入和验收条件，检查采用机构已有质量审批记录格式。风险日志标识为RISK-LOG，每周重审征兆、未决和变化。",
      "locator": "raw-materials.json#M-R2"
    },
    {
      "id": "M-R3",
      "kind": "example",
      "description": "沟通计划CP-1：项目指导组每周收一页要点，领域负责人每周参加工作包审查。SM-1利益相关者图记录指导组关注进展风险，领域负责人关注工作包输入和交付；沟通用要点报告、工作包审查记录和需求视图。项目有两个管理阶段，阶段末各评审，不强制与ADM阶段对应；团队向项目经理、再向指导组报告，架构一致性另向架构委员会报告。问题和变更分别进入ISS-LOG/CHG-LOG；未经批准变更不得写入基线。项目规则TOL-1：预测里程碑延误大于2个日历日时由项目经理上报指导组，等于2日仍在其委托范围；该规则仅为本案例。",
      "locator": "raw-materials.json#M-R3"
    },
    {
      "id": "M-R4",
      "kind": "example",
      "description": "修改：指导组换届后，例外上报接收人尚未确定；项目经理明确暂停将上报路径标为已确定。其他管理主题维持原约定。",
      "locator": "raw-materials.json#M-R4"
    }
  ],
  "entities": [
    {
      "id": "PMS-1",
      "type": "guide:project-management-strategy",
      "name": "架构项目管理策略：虚构图书馆联盟",
      "attributes": {
        "project_scope": "馆群预约服务的架构开发ADM A–F，实施治理另行安排",
        "selected_method": "机构既有项目管理框架，参考G188的管理方面",
        "method_tailoring": "两管理阶段覆盖架构开发，按项目治理与架构治理分别处理事项",
        "project_governance": "项目指导组负责项目时间预算质量",
        "architecture_governance": "架构委员会负责架构一致性",
        "confirmation_state": "awaiting-confirmation",
        "topics": [
          {
            "id": "M-RISK",
            "topic": "risk",
            "identification_classification": "分交付风险与架构实现风险登记来源和责任人",
            "analysis_method": "依据证据定性复评；缺概率/损失不计算定量等级",
            "response_design": "逐风险指定缓解与应对责任人和触发条件",
            "monitoring": "每周重审征兆、未决和变化",
            "risk_log_ref": "RISK-LOG",
            "project_vs_architecture_risk": "交付目标风险与架构愿景/实现风险分开追溯",
            "owner": "项目经理",
            "evidence": [
              "M-R2"
            ]
          },
          {
            "id": "M-QUALITY",
            "topic": "quality",
            "quality_characteristics": "需求可追溯、模型一致、业务代表确认范围",
            "documentation": "每份交付物章程记录范围、输入和验收条件",
            "assurance_process": "编制者自查→业务评审→架构一致性检查→指定验收人确认",
            "organization_qms_alignment": "采用机构已有质量审批记录格式",
            "acceptance_authority": "章程指定的业务验收人；架构委员会不代替全部业务验收",
            "owner": "质量负责人",
            "evidence": [
              "M-R2"
            ]
          },
          {
            "id": "M-COMMS",
            "topic": "stakeholder-communication",
            "stakeholder_map_ref": "SM-1",
            "concerns": "指导组关注进展风险；领域负责人关注工作包输入和交付",
            "engagement_deliverables": "要点报告、工作包审查记录、需求视图",
            "audience": [
              "项目指导组",
              "领域负责人"
            ],
            "frequency": "每周（项目约定）",
            "format": "一页要点及审查会议",
            "communication_plan_ref": "CP-1",
            "owner": "项目经理",
            "evidence": [
              "M-R3"
            ]
          },
          {
            "id": "M-CONTROLS",
            "topic": "project-controls",
            "reporting_levels": "团队→项目经理→指导组；架构一致性另向架构委员会报告",
            "stage_boundaries": "两个管理阶段，阶段末各评审；与ADM阶段不强行一一对应",
            "issue_change_capture": "ISS-LOG/CHG-LOG记录、分析及指定责任人",
            "exception_path": "项目经理向项目指导组上报并等待决定",
            "delegated_tolerances": [
              {
                "id": "TOL-1",
                "metric": "预测里程碑相对批准日期延误",
                "unit": "calendar-day",
                "operator": ">",
                "value": 2,
                "authority": "项目指导组",
                "evidence": [
                  "M-R3"
                ]
              }
            ],
            "delegation_monitoring": "每周审查实际和预测偏差；超容差形成例外报告",
            "owner": "项目经理",
            "evidence": [
              "M-R3"
            ]
          },
          {
            "id": "M-CONFIG",
            "topic": "configuration",
            "baseline_identification": "为批准的范围、产品与进度保存版本和审批记录",
            "change_approval": "变更先进入CHG-LOG，由授权治理者决定",
            "unapproved_change_rule": "exclude-from-approved-baseline",
            "configuration_records_ref": "CONFIG-REG",
            "owner": "PMO",
            "evidence": [
              "M-R1",
              "M-R3"
            ]
          }
        ],
        "analysis_result": {
          "strategy_id": "PMS-1",
          "topic_reviews": [
            {
              "topic": "risk",
              "id": "M-RISK",
              "state": "documented-awaiting-governance-confirmation",
              "gaps": []
            },
            {
              "topic": "quality",
              "id": "M-QUALITY",
              "state": "documented-awaiting-governance-confirmation",
              "gaps": []
            },
            {
              "topic": "stakeholder-communication",
              "id": "M-COMMS",
              "state": "documented-awaiting-governance-confirmation",
              "gaps": []
            },
            {
              "topic": "project-controls",
              "id": "M-CONTROLS",
              "state": "documented-awaiting-governance-confirmation",
              "gaps": []
            },
            {
              "topic": "configuration",
              "id": "M-CONFIG",
              "state": "documented-awaiting-governance-confirmation",
              "gaps": []
            }
          ],
          "gaps": [],
          "state": "ready-for-governance-review",
          "notice": "四个核心管理方面见G188§3.1.8；配置管理见§4.2.1。字段完备不代表批准；容差、频率与工具均来自项目规则，不是TOGAF默认值。"
        },
        "raw_material_refs": [
          "M-R1",
          "M-R2",
          "M-R3"
        ]
      },
      "evidence": [
        "M-R1",
        "M-R2",
        "M-R3"
      ],
      "certainty": "assumed",
      "version": "1.0"
    }
  ],
  "relationships": [],
  "view": {
    "id": "project-management-strategy-baseline",
    "artifact_id": "project-management-strategy",
    "profile_id": "project-management-strategy-default",
    "title": "架构项目管理策略／baseline",
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
      "PMS-1"
    ],
    "relationship_ids": [],
    "analysis": "从随包原始业务陈述提取字段、明确来源及项目规则，再执行project-management-strategy-review；逐字段保持假设与实际观察的区分。",
    "legend": "同一ID在修改前后代表同一工作产品；完整字段、嵌套记录及分析缺口按记录表可见。",
    "attributes": {
      "analysis_ids": [
        "project-management-strategy-analysis"
      ]
    }
  },
  "analyses": [
    {
      "id": "project-management-strategy-analysis",
      "method_id": "project-management-strategy-review",
      "inputs": {
        "id": "PMS-1",
        "source_ids": [
          "M-R1",
          "M-R2",
          "M-R3"
        ],
        "project_scope": "馆群预约服务的架构开发ADM A–F，实施治理另行安排",
        "selected_method": "机构既有项目管理框架，参考G188的管理方面",
        "method_tailoring": "两管理阶段覆盖架构开发，按项目治理与架构治理分别处理事项",
        "project_governance": "项目指导组负责项目时间预算质量",
        "architecture_governance": "架构委员会负责架构一致性",
        "confirmation_state": "awaiting-confirmation",
        "topics": [
          {
            "id": "M-RISK",
            "topic": "risk",
            "identification_classification": "分交付风险与架构实现风险登记来源和责任人",
            "analysis_method": "依据证据定性复评；缺概率/损失不计算定量等级",
            "response_design": "逐风险指定缓解与应对责任人和触发条件",
            "monitoring": "每周重审征兆、未决和变化",
            "risk_log_ref": "RISK-LOG",
            "project_vs_architecture_risk": "交付目标风险与架构愿景/实现风险分开追溯",
            "owner": "项目经理",
            "evidence": [
              "M-R2"
            ]
          },
          {
            "id": "M-QUALITY",
            "topic": "quality",
            "quality_characteristics": "需求可追溯、模型一致、业务代表确认范围",
            "documentation": "每份交付物章程记录范围、输入和验收条件",
            "assurance_process": "编制者自查→业务评审→架构一致性检查→指定验收人确认",
            "organization_qms_alignment": "采用机构已有质量审批记录格式",
            "acceptance_authority": "章程指定的业务验收人；架构委员会不代替全部业务验收",
            "owner": "质量负责人",
            "evidence": [
              "M-R2"
            ]
          },
          {
            "id": "M-COMMS",
            "topic": "stakeholder-communication",
            "stakeholder_map_ref": "SM-1",
            "concerns": "指导组关注进展风险；领域负责人关注工作包输入和交付",
            "engagement_deliverables": "要点报告、工作包审查记录、需求视图",
            "audience": [
              "项目指导组",
              "领域负责人"
            ],
            "frequency": "每周（项目约定）",
            "format": "一页要点及审查会议",
            "communication_plan_ref": "CP-1",
            "owner": "项目经理",
            "evidence": [
              "M-R3"
            ]
          },
          {
            "id": "M-CONTROLS",
            "topic": "project-controls",
            "reporting_levels": "团队→项目经理→指导组；架构一致性另向架构委员会报告",
            "stage_boundaries": "两个管理阶段，阶段末各评审；与ADM阶段不强行一一对应",
            "issue_change_capture": "ISS-LOG/CHG-LOG记录、分析及指定责任人",
            "exception_path": "项目经理向项目指导组上报并等待决定",
            "delegated_tolerances": [
              {
                "id": "TOL-1",
                "metric": "预测里程碑相对批准日期延误",
                "unit": "calendar-day",
                "operator": ">",
                "value": 2,
                "authority": "项目指导组",
                "evidence": [
                  "M-R3"
                ]
              }
            ],
            "delegation_monitoring": "每周审查实际和预测偏差；超容差形成例外报告",
            "owner": "项目经理",
            "evidence": [
              "M-R3"
            ]
          },
          {
            "id": "M-CONFIG",
            "topic": "configuration",
            "baseline_identification": "为批准的范围、产品与进度保存版本和审批记录",
            "change_approval": "变更先进入CHG-LOG，由授权治理者决定",
            "unapproved_change_rule": "exclude-from-approved-baseline",
            "configuration_records_ref": "CONFIG-REG",
            "owner": "PMO",
            "evidence": [
              "M-R1",
              "M-R3"
            ]
          }
        ],
        "evidence": [
          "M-R1",
          "M-R2",
          "M-R3"
        ]
      },
      "evidence": [
        "M-R1",
        "M-R2",
        "M-R3"
      ]
    }
  ]
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile project-management-strategy-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile project-management-strategy-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
