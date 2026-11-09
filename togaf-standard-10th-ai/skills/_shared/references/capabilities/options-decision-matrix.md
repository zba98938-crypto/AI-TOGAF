# 备选方案决策矩阵

ID：`options-decision-matrix`。主责：[togaf-gap-solutions](../../../togaf-gap-solutions/SKILL.md)。

来源：G176 §12.8；G20F §4.6；G20F §4.7.1 表4-1；G210 §3.3–3.3.8。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

哪项候选方案更适合业务问题？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 哪项候选方案更适合业务问题？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- option
- criterion
- score

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：criterion, option, option_score, guide:delivery_feature_review, guide:delivery_style_decision, guide:sbce_iteration, guide:sbce_constraint, guide:agile_pattern_choice。

```json
{
  "guide:delivery_feature_review": [
    "feature_id",
    "source_guidance",
    "applies",
    "observation",
    "evidence_refs"
  ],
  "guide:delivery_style_decision": [
    "scope_id",
    "styles",
    "owner",
    "rationale",
    "evidence_refs",
    "conflicting_features",
    "tailoring"
  ],
  "guide:sbce_iteration": [
    "option_id",
    "subsystem",
    "goal",
    "iteration",
    "hypothesis",
    "assessment",
    "evidence_refs",
    "decision_owner",
    "status",
    "decision_reason",
    "new_evidence_refs"
  ],
  "guide:sbce_constraint": [
    "source_option_id",
    "target_option_id",
    "rule",
    "status",
    "evidence_refs"
  ],
  "option": [
    "option_id",
    "criteria_scores",
    "rationale",
    "tradeoff"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "option": {
    "meaning": "候选方案",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "criterion": {
    "meaning": "单项判断准则",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "score": {
    "meaning": "所声明量表下的评分",
    "value_rule": "保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "weight": {
    "meaning": "明确声明的聚合权重",
    "value_rule": "保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "evidence": {
    "meaning": "本条观察的证据描述或引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "feasibility": {
    "meaning": "可行性判断及依据",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `evaluated_by` | * → assessment_factor,criterion,measure,environment_measure | 对象由判据或度量评价 |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 归一化候选方案
2. 比较成本资源贡献和可行性
3. 声明一至五分的优劣方向
4. 必要时加权并检查敏感性

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 成本原值不能直接当越高越好的评分，权重必须显式
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 成本原值不能直接当越高越好的评分，权重必须显式


## 视图和交付物

- [备选方案决策矩阵](../profiles/options-decision-matrix-default.md)
- [交付风格逐范围比较](../profiles/delivery-style-assessment.md)
- [集合式并行方案逐轮评估](../profiles/set-based-options-iteration.md)
- [敏捷协作模式选择与切换](../profiles/agile-pattern-selection.md)

- [architecture-roadmaps](../deliverables/architecture-roadmaps.md)
- [solution-building-blocks](../deliverables/solution-building-blocks.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「备选方案决策矩阵」给出：成本原值不能直接当越高越好的评分，权重必须显式",
    "expected": "missing-evidence",
    "why": "成本原值不能直接当越高越好的评分，权重必须显式"
  },
  "modification_example": {
    "change": "在「备选方案决策矩阵」的范围内新增或修改一项，检查下游是否随之变化",
    "expected": "受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用"
  }
}
```

## 可编辑示例与调用



以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

```json
{
  "notice": "虚构星河零售验收示例；全部对象为假设，未声称事实、批准或来源图复刻。",
  "sources": [
    {
      "id": "example-source",
      "kind": "example",
      "description": "虚构业务案例：在线订单、仓库发运及客户通知"
    }
  ],
  "entities": [
    {
      "id": "options-decision-matrix-default-option0",
      "type": "option",
      "name": "改善现有平台",
      "attributes": {
        "definition": "待选择，未批准"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "options-decision-matrix-default-option1",
      "type": "option",
      "name": "整体替换平台",
      "attributes": {
        "definition": "待选择，未批准"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "options-decision-matrix-default-criterion0",
      "type": "criterion",
      "name": "成本偏好",
      "attributes": {
        "weight": 1,
        "scale": "1最差至5最佳的偏好评分"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "options-decision-matrix-default-criterion1",
      "type": "criterion",
      "name": "资源偏好",
      "attributes": {
        "weight": 1,
        "scale": "1最差至5最佳的偏好评分"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "options-decision-matrix-default-criterion2",
      "type": "criterion",
      "name": "问题贡献",
      "attributes": {
        "weight": 2,
        "scale": "1最差至5最佳的偏好评分"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "options-decision-matrix-default-criterion3",
      "type": "criterion",
      "name": "可行性",
      "attributes": {
        "weight": 1,
        "scale": "1最差至5最佳的偏好评分"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "options-decision-matrix-default-score00",
      "type": "evaluated_by",
      "source": "options-decision-matrix-default-option0",
      "target": "options-decision-matrix-default-criterion0",
      "label": "偏好值 4；虚构评议证据",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "score": 4
      }
    },
    {
      "id": "options-decision-matrix-default-score01",
      "type": "evaluated_by",
      "source": "options-decision-matrix-default-option0",
      "target": "options-decision-matrix-default-criterion1",
      "label": "偏好值 4；虚构评议证据",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "score": 4
      }
    },
    {
      "id": "options-decision-matrix-default-score02",
      "type": "evaluated_by",
      "source": "options-decision-matrix-default-option0",
      "target": "options-decision-matrix-default-criterion2",
      "label": "偏好值 3；虚构评议证据",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "score": 3
      }
    },
    {
      "id": "options-decision-matrix-default-score03",
      "type": "evaluated_by",
      "source": "options-decision-matrix-default-option0",
      "target": "options-decision-matrix-default-criterion3",
      "label": "偏好值 5；虚构评议证据",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "score": 5
      }
    },
    {
      "id": "options-decision-matrix-default-score10",
      "type": "evaluated_by",
      "source": "options-decision-matrix-default-option1",
      "target": "options-decision-matrix-default-criterion0",
      "label": "偏好值 2；虚构评议证据",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "score": 2
      }
    },
    {
      "id": "options-decision-matrix-default-score11",
      "type": "evaluated_by",
      "source": "options-decision-matrix-default-option1",
      "target": "options-decision-matrix-default-criterion1",
      "label": "偏好值 2；虚构评议证据",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "score": 2
      }
    },
    {
      "id": "options-decision-matrix-default-score12",
      "type": "evaluated_by",
      "source": "options-decision-matrix-default-option1",
      "target": "options-decision-matrix-default-criterion2",
      "label": "偏好值 5；虚构评议证据",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "score": 5
      }
    },
    {
      "id": "options-decision-matrix-default-score13",
      "type": "evaluated_by",
      "source": "options-decision-matrix-default-option1",
      "target": "options-decision-matrix-default-criterion3",
      "label": "偏好值 2；虚构评议证据",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "score": 2
      }
    }
  ],
  "view": {
    "id": "v-options-decision-matrix-default",
    "artifact_id": "options-decision-matrix",
    "profile_id": "options-decision-matrix-default",
    "title": "备选方案决策矩阵／虚构案例",
    "entity_ids": [
      "options-decision-matrix-default-option0",
      "options-decision-matrix-default-option1",
      "options-decision-matrix-default-criterion0",
      "options-decision-matrix-default-criterion1",
      "options-decision-matrix-default-criterion2",
      "options-decision-matrix-default-criterion3"
    ],
    "relationship_ids": [
      "options-decision-matrix-default-score00",
      "options-decision-matrix-default-score01",
      "options-decision-matrix-default-score02",
      "options-decision-matrix-default-score03",
      "options-decision-matrix-default-score10",
      "options-decision-matrix-default-score11",
      "options-decision-matrix-default-score12",
      "options-decision-matrix-default-score13"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact options-decision-matrix --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
