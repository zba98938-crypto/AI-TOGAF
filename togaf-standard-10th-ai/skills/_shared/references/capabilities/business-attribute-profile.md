# 业务属性画像

ID：`business-attribute-profile`。主责：[togaf-security-risk](../../../togaf-security-risk/SKILL.md)。

来源：G152 §5.10.1; English PDF40–41。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

安全架构以什么业务价值衡量？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 安全架构以什么业务价值衡量？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- {'id': 'business_case_ref', 'origin': 'source', 'meaning': '当前业务论证及业务驱动'}
- {'id': 'attribute_definition', 'origin': 'source', 'meaning': '按业务语境定义的属性，含边界'}
- {'id': 'measurement_approach', 'origin': 'source', 'meaning': '获取和解释指标的方法'}
- {'id': 'metrics', 'origin': 'source-plus-project-contract', 'meaning': '带单位、尺度、时期、样本、证据及计算依据的指标'}
- {'id': 'target', 'origin': 'source', 'meaning': '与业务论证关联的绩效目标'}
- {'id': 'tolerable_deviation', 'origin': 'source', 'meaning': '管理层在介入前允许的最大结果偏差'}
- {'id': 'frequency_or_cost_threshold', 'origin': 'source-conditional', 'meaning': '业务采用时记录事件频率/成本阈值；不适用须说明，非强制统一指标'}
- {'id': 'corrective_action_trigger', 'origin': 'source', 'meaning': '超过业务容忍范围时的显式管理动作'}

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

缺业务论证、量表、目标或容差时生成带ID草稿和阻断项；可以给出观测值，不能判定达标或违规。未知值不填零。

## 元素、属性与关系

对象类型：business_attribute, control_objective, goal, requirement。

```json
{
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
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "definition": {
    "meaning": "业务含义和排除边界",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "metric": {
    "meaning": "度量方法和计算定义",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "unit": {
    "meaning": "度量单位",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "target": {
    "meaning": "期望结果或目标值",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "owner": {
    "meaning": "对对象负责的责任方",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 锁定原始材料及出处
2. 提炼业务关注，按业务语境重定义属性
3. 明确测量样本、分子分母和口径
4. 引用项目已声明目标及容差，不自行补值
5. 从原始数据计算观测并解释目标差值与纠偏触发
6. 建立业务论证—属性—要求—控制目标追溯
7. 提交缺口和纠偏建议供实际责任人评审

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 采用 SABSA 画像作为起点不表示所有参考属性都适用
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯
- 所有指标拥有单位、尺度、时期、数据和计算依据
- 缺目标或容差不可自动判定通过
- 不得将百分比与百分点混用
- 频率和成本字段可以不适用，但必须写理由
- 目标与触发边界显式说明包含/不包含等号
- 保持需求与控制目标的独立身份

- SABSA属性参考集不是所有项目强制清单
- 99.5%、0.2个百分点等案例值不是TOGAF阈值
- 画像的target不是任意措施文字
- 没有运营数据时不能声称实时仪表板已运行


## 视图和交付物

- [业务属性画像：定义、规则与观测](../profiles/business-attribute-profile-default.md)
- [业务属性—业务目标—要求—控制追溯](../profiles/business-attribute-profile-trace.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)
- [architecture-requirements-specification](../deliverables/architecture-requirements-specification.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「业务属性画像」给出：SABSA属性参考集不是所有项目强制清单",
    "expected": "missing-attribute",
    "why": "SABSA属性参考集不是所有项目强制清单"
  },
  "modification_example": {
    "change": "在「业务属性画像」的范围内新增或修改一项，检查下游是否随之变化",
    "expected": "受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/business-attribute-profile.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

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

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact business-attribute-profile --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
