# 业务属性画像：定义、规则与观测

`profile_id`: business-attribute-profile-default；`artifact_id`: business-attribute-profile；主责：[togaf-security-risk](../../../togaf-security-risk/SKILL.md)。

来源：G152 §5.10.1; English PDF40–41。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1。

{
  "source_verified": false,
  "layout_notes": "依据正文语义的项目操作表单；没有对应原图，不标记为原图复刻。",
  "review_status": "source-semantics-reviewed-project-form"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：business_attribute。关系类型：。

```json
{
  "entities": {
    "business_attribute": [
      "business_case_ref",
      "definition",
      "measurement_approach",
      "metric",
      "target",
      "tolerable_deviation",
      "corrective_action_trigger",
      "frequency_or_cost_threshold",
      "owner",
      "source_refs",
      "unit",
      "observation"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 所有指标拥有单位、尺度、时期、数据和计算依据
- 缺目标或容差不可自动判定通过
- 不得将百分比与百分点混用
- 频率和成本字段可以不适用，但必须写理由
- 目标与触发边界显式说明包含/不包含等号
- 保持需求与控制目标的独立身份

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构图书馆完整案例；数据与阈值不是TOGAF规定。",
  "sources": [
    {
      "id": "B-R1",
      "kind": "example",
      "description": "馆长：座位被取消后必须能找到操作者。保留原记录，后续修正不能覆盖最初记录。",
      "locator": "case.json#raw_records/B-R1"
    },
    {
      "id": "B-R2",
      "kind": "example",
      "description": "案例治理小组规则：每月抽样预约变更记录，操作者与时间均可追溯的比例目标至少99.5%；最多容忍比目标低0.2个百分点，低于99.3%时由服务台负责人发起纠偏。该属性不使用损失金额阈值。",
      "locator": "case.json#raw_records/B-R2"
    },
    {
      "id": "B-R3",
      "kind": "example",
      "description": "2026年9月抽样1000条，有996条同时具备不可改写的操作者标识和时间戳。抽样只覆盖预约变更，不包括浏览日志。",
      "locator": "case.json#raw_records/B-R3"
    },
    {
      "id": "B-R4",
      "kind": "example",
      "description": "复核发现4条标识来自共享账号，不能归属个人。有效记录从996改为992；总样本仍1000。",
      "locator": "case.json#raw_records/B-R4"
    }
  ],
  "entities": [
    {
      "id": "bap-accountability",
      "type": "business_attribute",
      "name": "预约变更可追责",
      "attributes": {
        "business_case_ref": "B-R1",
        "definition": "在月度抽样的预约变更范围内，每条操作均可追溯到唯一个人和不可改写的时间戳。",
        "measurement_approach": {
          "source_refs": [
            "B-R3"
          ],
          "population": "2026-09预约变更记录",
          "sampling": "本例给定样本1000条，不外推全体",
          "numerator_rule": "个人操作者和时间戳同时有效",
          "denominator_rule": "样本中所有预约变更记录"
        },
        "metric": {
          "id": "m-attribution",
          "unit": "percent",
          "scale": "ratio",
          "period": "2026-09",
          "numerator": 996,
          "denominator": 1000,
          "formula": "100 * numerator / denominator",
          "rule_origin": "fictional-project-rule",
          "evidence": [
            "B-R2",
            "B-R3"
          ]
        },
        "target": {
          "operator": ">=",
          "value": 99.5,
          "unit": "percent",
          "evidence": [
            "B-R2"
          ]
        },
        "tolerable_deviation": {
          "value": 0.2,
          "unit": "percentage-point",
          "direction": "below-target",
          "evidence": [
            "B-R2"
          ]
        },
        "corrective_action_trigger": {
          "operator": "<",
          "threshold": 99.3,
          "unit": "percent",
          "action": "服务台负责人发起可追责性缺陷纠偏并复核共享账号",
          "evidence": [
            "B-R2"
          ]
        },
        "frequency_or_cost_threshold": {
          "status": "not-applicable",
          "reason": "此属性按样本可追溯比例评判；案例未采用事件发生频率或损失金额阈值。",
          "review_cadence": "monthly",
          "evidence": [
            "B-R2"
          ]
        },
        "owner": "服务台负责人",
        "source_refs": [
          "B-R1",
          "B-R2",
          "B-R3"
        ],
        "unit": "percent",
        "observation": {
          "numerator": 996,
          "denominator": 1000,
          "period": "2026-09"
        }
      },
      "evidence": [
        "B-R1",
        "B-R2",
        "B-R3"
      ],
      "certainty": "assumed",
      "version": "1.0",
      "extension_data": {
        "togaf-addenda:g152-bap": {
          "attribute_id": "bap-accountability",
          "business_case_ref": "B-R1",
          "definition": "在月度抽样的预约变更范围内，每条操作均可追溯到唯一个人和不可改写的时间戳。",
          "measurement_approach": {
            "source_refs": [
              "B-R3"
            ],
            "population": "2026-09预约变更记录",
            "sampling": "本例给定样本1000条，不外推全体",
            "numerator_rule": "个人操作者和时间戳同时有效",
            "denominator_rule": "样本中所有预约变更记录"
          },
          "metric": {
            "id": "m-attribution",
            "unit": "percent",
            "scale": "ratio",
            "period": "2026-09",
            "numerator": 996,
            "denominator": 1000,
            "formula": "100 * numerator / denominator",
            "rule_origin": "fictional-project-rule",
            "evidence": [
              "B-R2",
              "B-R3"
            ]
          },
          "target": {
            "operator": ">=",
            "value": 99.5,
            "unit": "percent",
            "evidence": [
              "B-R2"
            ]
          },
          "tolerable_deviation": {
            "value": 0.2,
            "unit": "percentage-point",
            "direction": "below-target",
            "evidence": [
              "B-R2"
            ]
          },
          "corrective_action_trigger": {
            "operator": "<",
            "threshold": 99.3,
            "unit": "percent",
            "action": "服务台负责人发起可追责性缺陷纠偏并复核共享账号",
            "evidence": [
              "B-R2"
            ]
          },
          "frequency_or_cost_threshold": {
            "status": "not-applicable",
            "reason": "此属性按样本可追溯比例评判；案例未采用事件发生频率或损失金额阈值。",
            "review_cadence": "monthly",
            "evidence": [
              "B-R2"
            ]
          },
          "owner": "服务台负责人",
          "source_refs": [
            "B-R1",
            "B-R2",
            "B-R3"
          ]
        }
      }
    }
  ],
  "relationships": [],
  "analyses": [
    {
      "id": "analysis-business-attribute-profile",
      "method_id": "business-attribute-evaluation",
      "inputs": {
        "attribute_id": "bap-accountability",
        "business_case_ref": "B-R1",
        "definition": "在月度抽样的预约变更范围内，每条操作均可追溯到唯一个人和不可改写的时间戳。",
        "measurement_approach": {
          "source_refs": [
            "B-R3"
          ],
          "population": "2026-09预约变更记录",
          "sampling": "本例给定样本1000条，不外推全体",
          "numerator_rule": "个人操作者和时间戳同时有效",
          "denominator_rule": "样本中所有预约变更记录"
        },
        "metric": {
          "id": "m-attribution",
          "unit": "percent",
          "scale": "ratio",
          "period": "2026-09",
          "numerator": 996,
          "denominator": 1000,
          "formula": "100 * numerator / denominator",
          "rule_origin": "fictional-project-rule",
          "evidence": [
            "B-R2",
            "B-R3"
          ]
        },
        "target": {
          "operator": ">=",
          "value": 99.5,
          "unit": "percent",
          "evidence": [
            "B-R2"
          ]
        },
        "tolerable_deviation": {
          "value": 0.2,
          "unit": "percentage-point",
          "direction": "below-target",
          "evidence": [
            "B-R2"
          ]
        },
        "corrective_action_trigger": {
          "operator": "<",
          "threshold": 99.3,
          "unit": "percent",
          "action": "服务台负责人发起可追责性缺陷纠偏并复核共享账号",
          "evidence": [
            "B-R2"
          ]
        },
        "frequency_or_cost_threshold": {
          "status": "not-applicable",
          "reason": "此属性按样本可追溯比例评判；案例未采用事件发生频率或损失金额阈值。",
          "review_cadence": "monthly",
          "evidence": [
            "B-R2"
          ]
        },
        "owner": "服务台负责人",
        "source_refs": [
          "B-R1",
          "B-R2",
          "B-R3"
        ],
        "source_ids": [
          "B-R1",
          "B-R2",
          "B-R3",
          "B-R4"
        ]
      },
      "evidence": [
        "B-R1",
        "B-R2",
        "B-R3",
        "B-R4"
      ]
    }
  ],
  "view": {
    "id": "library-bap",
    "artifact_id": "business-attribute-profile",
    "profile_id": "business-attribute-profile-default",
    "title": "业务属性画像：定义、规则与观测",
    "entity_ids": [
      "bap-accountability"
    ],
    "relationship_ids": [],
    "analysis": "原始陈述、分析规则和修改记录均保留稳定引用；计算只采用显式项目规则。",
    "legend": "虚构图书馆案例。空白矩阵格为未确认；相邻/包含不代表额外关系；规则和数值不是TOGAF默认值。",
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
      "evolution": "baseline"
    },
    "attributes": {
      "analysis_ids": [
        "analysis-business-attribute-profile"
      ]
    }
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile business-attribute-profile-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile business-attribute-profile-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
