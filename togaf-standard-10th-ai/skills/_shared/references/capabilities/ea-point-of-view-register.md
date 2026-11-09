# EA观点文件与影响经营登记

ID：`ea-point-of-view-register`。主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G184 §12.2–12.4；本地L1351–1373。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

外部生态变化要求什么转型，EA建议如何被阅读、讨论并关联到后续变更？

- 该范围业务负责人
- 架构师
- 评审及运营负责人
- 外部生态变化要求什么转型，EA建议如何被阅读、讨论并关联到后续变更？
- 来源、范围与适用性


## 输入及缺口处理

必需：

- {'id': 'charter_alignment', 'meaning': 'EA章程目的与本主张的关联', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'ecosystem_change', 'meaning': '外部生态信号及来源', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'decision_question', 'meaning': '决策者要回答的问题', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'position', 'meaning': '有理由的主张，不是建模视角规范', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'rationale', 'meaning': '回应未来需求、文化与权衡的论据', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'alternatives', 'meaning': '候选方案及各自影响和取舍', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'recommendation', 'meaning': '待决策的转型建议', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'adoption_timing', 'meaning': '从热潮到需要的时间判断及证据', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'cost_risk_tradeoff', 'meaning': '采用成本与失败风险的条件性比较', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'audience_ids', 'meaning': '目标利益相关者稳定标识', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'document_version', 'meaning': '被阅读或修订的观点版本', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'reading_events', 'meaning': '有时间、版本、读者和来源的实际阅读观察', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'initiated_changes', 'meaning': '后续变更、发起人、证据及关联，不推断因果', 'origin': 'source-purpose-plus-project-contract'}
- {'id': 'follow_up', 'meaning': '负责人、复评期限与下一步', 'origin': 'source-purpose-plus-project-contract'}

可选：

- 既有模型及历史结论

不足时保留带ID草案与needs-input；未知容差不设默认值，缺实际阅读/验收证据不声称已阅读/完成。冲突、重复ID和未经批准覆盖基线属于错误。

## 元素、属性与关系

对象类型：guide:ea-point-of-view。

```json
{
  "guide:ea-point-of-view": [
    "charter_alignment",
    "ecosystem_change",
    "decision_question",
    "position",
    "rationale",
    "alternatives",
    "recommendation",
    "adoption_timing",
    "cost_risk_tradeoff",
    "audience_ids",
    "document_version",
    "reading_events",
    "initiated_changes",
    "follow_up",
    "analysis_result",
    "raw_material_refs"
  ]
}
```

{
  "charter_alignment": {
    "meaning": "EA章程目的与本主张的关联",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "ecosystem_change": {
    "meaning": "外部生态信号及来源",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "decision_question": {
    "meaning": "决策者要回答的问题",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "position": {
    "meaning": "有理由的主张，不是建模视角规范",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "rationale": {
    "meaning": "回应未来需求、文化与权衡的论据",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "alternatives": {
    "meaning": "候选方案及各自影响和取舍",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "recommendation": {
    "meaning": "待决策的转型建议",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "adoption_timing": {
    "meaning": "从热潮到需要的时间判断及证据",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "cost_risk_tradeoff": {
    "meaning": "采用成本与失败风险的条件性比较",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "audience_ids": {
    "meaning": "目标利益相关者稳定标识",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "document_version": {
    "meaning": "被阅读或修订的观点版本",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "reading_events": {
    "meaning": "有时间、版本、读者和来源的实际阅读观察",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "initiated_changes": {
    "meaning": "后续变更、发起人、证据及关联，不推断因果",
    "value_rule": "来源事实、项目规则、参考内容与未知分别记录；不填造数据",
    "definition_origin": "guide-purpose-plus-explicit-project-operational-field"
  },
  "follow_up": {
    "meaning": "负责人、复评期限与下一步",
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

1. 从章程与外部生态原料提炼决策问题和时间窗口
2. 提出有理由的主张、备选方案及影响和成本/失败风险权衡
3. 形成面向明确受众的观点文件与建议清单
4. 分别登记分发、实际阅读及文档版本
5. 跟踪阅读者发起的变更并核实归属，保留因果限制
6. 修订观点后分别报告旧版阅读与新版反馈缺口

## 输出、检查与误读

- 范围及依据
- 逐条结果与理由
- 缺口、下一步与责任
- 版本和来源引用

- point of view经营不等同于viewpoint library
- 分发不等于已阅读；重复阅读不重复计人数
- 读者与后续变更关联不证明因果或价值实现
- 修订文件版本不覆盖原阅读记录

- 名称、来源表格和成功输出不等于业务结论已核实
- point of view经营不等同于viewpoint library
- 分发不等于已阅读；重复阅读不重复计人数
- 读者与后续变更关联不证明因果或价值实现
- 修订文件版本不覆盖原阅读记录


## 视图和交付物

- [EA观点文件与影响经营登记](../profiles/ea-point-of-view-register-default.md)

- [organization-model](../deliverables/organization-model.md)
- [architecture-vision](../deliverables/architecture-vision.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「EA观点文件与影响经营登记」给出：名称、来源表格和成功输出不等于业务结论已核实",
    "expected": "missing-evidence",
    "why": "名称、来源表格和成功输出不等于业务结论已核实"
  },
  "modification_example": {
    "change": "在「EA观点文件与影响经营登记」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "P-R1",
      "kind": "example",
      "description": "图书馆联盟EA章程要求降低服务中断风险，并为理事会提供投资建议。伙伴平台宣布2027年底停用旧认证接口。运营经理要求避免寒假期间集中改造。",
      "locator": "raw-materials.json#P-R1"
    },
    {
      "id": "P-R2",
      "kind": "example",
      "description": "EA团队建议先在一个分馆试点新接口，再分批替换；备选是维持旧接口直至期限，短期成本低但临近期限集中失败风险高。试点会增加双接口维护成本，应在2027年4月前评审结果。",
      "locator": "raw-materials.json#P-R2"
    },
    {
      "id": "P-R3",
      "kind": "example",
      "description": "观点文档POV-1版本1于10月5日分发。10月6日、10月8日均记录运营经理阅读版本1；只收到两次记录，未观察其他收件人阅读。10月9日运营经理提交变更CH-1：为分馆试点留出窗口，未声称观点文件是唯一原因。",
      "locator": "raw-materials.json#P-R3"
    },
    {
      "id": "P-R4",
      "kind": "example",
      "description": "修改：财务负责人10月12日也阅读版本1并提交CH-2成本验证请求；10月15日观点版本升为2，新增双运行成本核实要求，尚无版本2阅读记录。",
      "locator": "raw-materials.json#P-R4"
    }
  ],
  "entities": [
    {
      "id": "POV-1",
      "type": "guide:ea-point-of-view",
      "name": "EA观点文件与影响经营登记：虚构图书馆联盟",
      "attributes": {
        "charter_alignment": "降低服务中断风险并支持理事会投资决策",
        "ecosystem_change": "伙伴平台2027年底停用旧认证接口",
        "decision_question": "是否在2027年4月前启动分馆试点并分批迁移？",
        "position": "先试点再分批替换",
        "rationale": "分离技术不确定性与寒假服务窗口，避免临期集中切换",
        "alternatives": [
          {
            "id": "POV-1-ALT-A",
            "description": "试点后分批替换",
            "impact": "提前验证兼容性并保留回退窗口",
            "tradeoff": "增加双运行维护成本"
          },
          {
            "id": "POV-1-ALT-B",
            "description": "维持旧接口至期限",
            "impact": "短期投入较低，临期替换风险集中",
            "tradeoff": "延期保留现金但减少试错窗口"
          }
        ],
        "recommendation": "将分馆试点与成本核实提交理事会讨论，尚未申请生产切换批准",
        "adoption_timing": "2027年4月前评审试点，避开寒假切换；不是指南固定周期",
        "cost_risk_tradeoff": "双接口维护成本尚待核实，与临期集中失败风险并列评估；不填写臆造金额",
        "audience_ids": [
          "operations-manager",
          "finance-director",
          "board"
        ],
        "document_version": "1",
        "distribution_record": {
          "date": "2026-10-05",
          "audience_ids": [
            "operations-manager",
            "finance-director",
            "board"
          ],
          "evidence": [
            "P-R3"
          ]
        },
        "reading_events": [
          {
            "id": "READ-1",
            "reader_id": "operations-manager",
            "document_version": "1",
            "observed_at": "2026-10-06",
            "evidence": [
              "P-R3"
            ]
          },
          {
            "id": "READ-2",
            "reader_id": "operations-manager",
            "document_version": "1",
            "observed_at": "2026-10-08",
            "evidence": [
              "P-R3"
            ]
          }
        ],
        "initiated_changes": [
          {
            "id": "CH-1",
            "initiator_id": "operations-manager",
            "description": "为分馆试点留出窗口",
            "reading_event_id": "READ-1",
            "claims_causation": false,
            "evidence": [
              "P-R3"
            ]
          }
        ],
        "follow_up": {
          "owner": "EA负责人",
          "due": "2027-04-01",
          "action": "核实试点与成本证据，再更新建议及归属说明"
        },
        "analysis_result": {
          "rows": [
            {
              "id": "POV-1",
              "review_state": "document-and-observations-reviewable",
              "unique_observed_readers": 1,
              "reader_ids": [
                "operations-manager"
              ],
              "current_version_reader_ids": [
                "operations-manager"
              ],
              "stale_version_reading_event_ids": [],
              "change_associations": [
                {
                  "change_id": "CH-1",
                  "reader_id": "operations-manager",
                  "reading_event_id": "READ-1",
                  "meaning": "observed-sequence-and-stakeholder-association; no causal inference"
                }
              ],
              "recommended_action": "将分馆试点与成本核实提交理事会讨论，尚未申请生产切换批准",
              "gaps": []
            }
          ],
          "gaps": [],
          "notice": "观点是面向变革决策的有理由主张及经营反馈，不是viewpoint规范库；阅读记录说明兴趣，不证明采纳、变革成效或因果贡献。"
        },
        "raw_material_refs": [
          "P-R1",
          "P-R2",
          "P-R3"
        ]
      },
      "evidence": [
        "P-R1",
        "P-R2",
        "P-R3"
      ],
      "certainty": "assumed",
      "version": "1.0"
    }
  ],
  "relationships": [],
  "view": {
    "id": "ea-point-of-view-register-baseline",
    "artifact_id": "ea-point-of-view-register",
    "profile_id": "ea-point-of-view-register-default",
    "title": "EA观点文件与影响经营登记／baseline",
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
      "POV-1"
    ],
    "relationship_ids": [],
    "analysis": "从随包原始业务陈述提取字段、明确来源及项目规则，再执行ea-point-of-view-review；逐字段保持假设与实际观察的区分。",
    "legend": "同一ID在修改前后代表同一工作产品；完整字段、嵌套记录及分析缺口按记录表可见。",
    "attributes": {
      "analysis_ids": [
        "ea-point-of-view-register-analysis"
      ]
    }
  },
  "analyses": [
    {
      "id": "ea-point-of-view-register-analysis",
      "method_id": "ea-point-of-view-review",
      "inputs": {
        "source_ids": [
          "P-R1",
          "P-R2",
          "P-R3"
        ],
        "points": [
          {
            "id": "POV-1",
            "charter_alignment": "降低服务中断风险并支持理事会投资决策",
            "ecosystem_change": "伙伴平台2027年底停用旧认证接口",
            "decision_question": "是否在2027年4月前启动分馆试点并分批迁移？",
            "position": "先试点再分批替换",
            "rationale": "分离技术不确定性与寒假服务窗口，避免临期集中切换",
            "alternatives": [
              {
                "id": "POV-1-ALT-A",
                "description": "试点后分批替换",
                "impact": "提前验证兼容性并保留回退窗口",
                "tradeoff": "增加双运行维护成本"
              },
              {
                "id": "POV-1-ALT-B",
                "description": "维持旧接口至期限",
                "impact": "短期投入较低，临期替换风险集中",
                "tradeoff": "延期保留现金但减少试错窗口"
              }
            ],
            "recommendation": "将分馆试点与成本核实提交理事会讨论，尚未申请生产切换批准",
            "adoption_timing": "2027年4月前评审试点，避开寒假切换；不是指南固定周期",
            "cost_risk_tradeoff": "双接口维护成本尚待核实，与临期集中失败风险并列评估；不填写臆造金额",
            "audience_ids": [
              "operations-manager",
              "finance-director",
              "board"
            ],
            "document_version": "1",
            "distribution_record": {
              "date": "2026-10-05",
              "audience_ids": [
                "operations-manager",
                "finance-director",
                "board"
              ],
              "evidence": [
                "P-R3"
              ]
            },
            "reading_events": [
              {
                "id": "READ-1",
                "reader_id": "operations-manager",
                "document_version": "1",
                "observed_at": "2026-10-06",
                "evidence": [
                  "P-R3"
                ]
              },
              {
                "id": "READ-2",
                "reader_id": "operations-manager",
                "document_version": "1",
                "observed_at": "2026-10-08",
                "evidence": [
                  "P-R3"
                ]
              }
            ],
            "initiated_changes": [
              {
                "id": "CH-1",
                "initiator_id": "operations-manager",
                "description": "为分馆试点留出窗口",
                "reading_event_id": "READ-1",
                "claims_causation": false,
                "evidence": [
                  "P-R3"
                ]
              }
            ],
            "follow_up": {
              "owner": "EA负责人",
              "due": "2027-04-01",
              "action": "核实试点与成本证据，再更新建议及归属说明"
            },
            "evidence": [
              "P-R1",
              "P-R2",
              "P-R3"
            ]
          }
        ]
      },
      "evidence": [
        "P-R1",
        "P-R2",
        "P-R3"
      ]
    }
  ]
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact ea-point-of-view-register --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
