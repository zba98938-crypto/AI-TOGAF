# 架构项目管理策略

ID：`project-management-strategy`。主责：[togaf-architecture-workbench](../../../togaf-architecture-workbench/SKILL.md)。

来源：G188 §3.1.8 L541–631；G188 §4.2.1 L1524–1531。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

架构项目如何管理风险、质量、沟通、配置与控制，谁确认方法和授权边界？

- 该范围业务负责人
- 架构师
- 评审及运营负责人
- 架构项目如何管理风险、质量、沟通、配置与控制，谁确认方法和授权边界？
- 来源、范围与适用性


## 输入及缺口处理

必需：

- {'id': 'project_scope', 'meaning': '作为项目管理的工作范围与排除项', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'selected_method', 'meaning': '组织采用的项目管理方法', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'method_tailoring', 'meaning': '阶段和方法裁剪理由', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'project_governance', 'meaning': '时间预算质量监督职能与责任方', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'architecture_governance', 'meaning': '架构一致性治理职能与责任方', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'confirmation_state', 'meaning': '管理方法确认状态及所缺依据', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'topics', 'meaning': '风险、质量、利益相关者沟通、控制、配置五主题的实际操作规范和责任', 'origin': 'source-purpose-plus-project-contract'}

可选：

- 既有模型及历史结论

不足时保留带ID草案与needs-input；未知容差不设默认值，缺实际阅读/验收证据不声称已阅读/完成。冲突、重复ID和未经批准覆盖基线属于错误。

## 元素、属性与关系

对象类型：guide:project-management-strategy。

```json
{
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
}
```

{
  "project_scope": {
    "meaning": "作为项目管理的工作范围与排除项",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "selected_method": {
    "meaning": "组织采用的项目管理方法",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "method_tailoring": {
    "meaning": "阶段和方法裁剪理由",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "project_governance": {
    "meaning": "时间预算质量监督职能与责任方",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "architecture_governance": {
    "meaning": "架构一致性治理职能与责任方",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "confirmation_state": {
    "meaning": "管理方法确认状态及所缺依据",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "topics": {
    "meaning": "风险、质量、利益相关者沟通、控制、配置五主题的实际操作规范和责任",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "analysis_result": {
    "meaning": "确定性审查结果与带ID缺口",
    "value_rule": "由所列method输入重新计算，不作为治理批准"
  },
  "raw_material_refs": {
    "meaning": "完整原始业务材料ID列表",
    "value_rule": "随包原料可检索"
  },
  "name": {
    "meaning": "工作产品对象的业务名称",
    "value_rule": "使用范围内可识别的业务名称；身份由稳定ID确定，不以同名合并对象",
    "definition_origin": "project-operational-convention",
    "value_schema": {
      "type": "string",
      "minLength": 1,
      "pattern": "\\S"
    }
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 识别项目范围和组织既有项目管理框架
2. 分开项目治理与架构治理角色，即使由同一机构承担也分别说明
3. 提炼风险、质量、沟通和控制方法并链接对应登记册
4. 按组织方法明确配置基线与批准后变更规则
5. 记录有来源的频率、容差、上报和授权监控，不套用示例数值
6. 交治理责任方确认，变更后复核受影响控制

## 输出、检查与误读

- 范围及依据
- 逐条结果与理由
- 缺口、下一步与责任
- 版本和来源引用

- 四核心方面来自§3.1.8，配置管理来自§4.2.1
- 项目风险与架构愿景/实现风险不混淆
- 质量完备不等于已验收
- 管理阶段与ADM阶段无需一一对应
- 未经批准的变更不得纳入批准基线
- 容差和频率是项目约定，不是TOGAF标准阈值

- 名称、来源表格和成功输出不等于业务结论已核实
- 四核心方面来自§3.1.8，配置管理来自§4.2.1
- 项目风险与架构愿景/实现风险不混淆
- 质量完备不等于已验收
- 管理阶段与ADM阶段无需一一对应
- 未经批准的变更不得纳入批准基线
- 容差和频率是项目约定，不是TOGAF标准阈值


## 视图和交付物

- [架构项目管理策略](../profiles/project-management-strategy-default.md)

- [statement-of-work](../deliverables/statement-of-work.md)
- [tailored-architecture-framework](../deliverables/tailored-architecture-framework.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「架构项目管理策略」给出：名称、来源表格和成功输出不等于业务结论已核实",
    "expected": "missing-evidence",
    "why": "名称、来源表格和成功输出不等于业务结论已核实"
  },
  "modification_example": {
    "change": "在「架构项目管理策略」的范围内新增或修改一项，检查下游是否随之变化",
    "expected": "受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用"
  }
}
```

## 可编辑示例与调用



以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

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

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact project-management-strategy --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
