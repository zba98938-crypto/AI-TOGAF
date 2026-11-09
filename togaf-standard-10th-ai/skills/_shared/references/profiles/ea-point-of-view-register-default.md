# EA观点文件与影响经营登记

`profile_id`: ea-point-of-view-register-default；`artifact_id`: ea-point-of-view-register；主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G184 §12.2–12.4；本地L1351–1373。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：1.0。

{
  "id": "ea-point-of-view-register-default",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "按已核查的来源结构参数化；参考图与业务实例的验收分别进行。",
  "structure_basis": "正文定义的工作产品；记录表是项目操作表示法，不冒充来源原图"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:ea-point-of-view。关系类型：。

```json
{
  "entities": {
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
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 对象、关系、必要属性均可追溯并得到表达
- 参考内容不自动成为项目事实；未知项保持显式
- point of view经营不等同于viewpoint library
- 分发不等于已阅读；重复阅读不重复计人数
- 读者与后续变更关联不证明因果或价值实现
- 修订文件版本不覆盖原阅读记录

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

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

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile ea-point-of-view-register-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile ea-point-of-view-register-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
