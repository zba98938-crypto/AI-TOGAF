# 采用因素分层与就绪类型

`profile_id`: dtra-factor-progression；`artifact_id`: adoption-factor-progression；主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G212/fig5-4。

## 构图与定义状态

表示族：`roadmap`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "source_figure": "G212/fig5-4",
  "layout_notes": "三层定性四分之一圆；三类企业射线止于对应层；不表达排期或分数。",
  "review_status": "corrected-structure-awaiting-independent-review",
  "verification_evidence": "reviews/source-verification/dtra-factor-progression.json",
  "semantic_layout": "dtra-factor-layers",
  "source_asset_status": "available-separate-from-template-review"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：readiness_factor, assessment_result。关系类型：traces_to。

```json
{
  "entities": {
    "readiness_factor": [
      "factor_category",
      "prerequisite",
      "action",
      "readiness_evidence"
    ],
    "assessment_result": [
      "organization_type",
      "fulfilled_layers",
      "interpretation"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 基础、影响、持续三层完整；类型1/2/3不是实施步骤
- 类型2满足基础与影响；类型3还须满足持续因素
- 日期不进入因素递进图；项目分类须以明确评估证据支持

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

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
      "id": "dtra-factor-progression-foundational",
      "type": "readiness_factor",
      "name": "基础因素",
      "attributes": {
        "factor_category": "foundational",
        "prerequisite": "无外层因素可替代基础就绪",
        "action": "确认领导支持、目标与数字技能短板",
        "readiness_evidence": "虚构说明；真实企业须关联问卷及特征证据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "dtra-factor-progression-impact",
      "type": "readiness_factor",
      "name": "影响因素",
      "attributes": {
        "factor_category": "impact",
        "prerequisite": "基础因素满足",
        "action": "验证治理协同和采用推动机制",
        "readiness_evidence": "虚构说明；真实企业须关联问卷及特征证据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "dtra-factor-progression-sustaining",
      "type": "readiness_factor",
      "name": "持续因素",
      "attributes": {
        "factor_category": "sustaining",
        "prerequisite": "基础与影响因素满足",
        "action": "建立持续反馈与制度化改进",
        "readiness_evidence": "虚构说明；真实企业须关联问卷及特征证据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "dtra-factor-progression-type1",
      "type": "assessment_result",
      "name": "类型 1：参考评估情形",
      "attributes": {
        "organization_type": 1,
        "fulfilled_layers": [
          "foundational"
        ],
        "interpretation": "满足列明因素层的企业类别；不是项目步骤或实际企业评定"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "dtra-factor-progression-type2",
      "type": "assessment_result",
      "name": "类型 2：参考评估情形",
      "attributes": {
        "organization_type": 2,
        "fulfilled_layers": [
          "foundational",
          "impact"
        ],
        "interpretation": "满足列明因素层的企业类别；不是项目步骤或实际企业评定"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "dtra-factor-progression-type3",
      "type": "assessment_result",
      "name": "类型 3：参考评估情形",
      "attributes": {
        "organization_type": 3,
        "fulfilled_layers": [
          "foundational",
          "impact",
          "sustaining"
        ],
        "interpretation": "满足列明因素层的企业类别；不是项目步骤或实际企业评定"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "dtra-factor-progression-type1-foundational",
      "source": "dtra-factor-progression-type1",
      "target": "dtra-factor-progression-foundational",
      "type": "traces_to",
      "label": "该就绪情形满足此因素层（定性定义）",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "dtra-factor-progression-type2-foundational",
      "source": "dtra-factor-progression-type2",
      "target": "dtra-factor-progression-foundational",
      "type": "traces_to",
      "label": "该就绪情形满足此因素层（定性定义）",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "dtra-factor-progression-type2-impact",
      "source": "dtra-factor-progression-type2",
      "target": "dtra-factor-progression-impact",
      "type": "traces_to",
      "label": "该就绪情形满足此因素层（定性定义）",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "dtra-factor-progression-type3-foundational",
      "source": "dtra-factor-progression-type3",
      "target": "dtra-factor-progression-foundational",
      "type": "traces_to",
      "label": "该就绪情形满足此因素层（定性定义）",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "dtra-factor-progression-type3-impact",
      "source": "dtra-factor-progression-type3",
      "target": "dtra-factor-progression-impact",
      "type": "traces_to",
      "label": "该就绪情形满足此因素层（定性定义）",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "dtra-factor-progression-type3-sustaining",
      "source": "dtra-factor-progression-type3",
      "target": "dtra-factor-progression-sustaining",
      "type": "traces_to",
      "label": "该就绪情形满足此因素层（定性定义）",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-dtra-factor-progression",
    "artifact_id": "adoption-factor-progression",
    "profile_id": "dtra-factor-progression",
    "title": "采用因素分层与三种就绪情形／虚构示例",
    "entity_ids": [
      "dtra-factor-progression-foundational",
      "dtra-factor-progression-impact",
      "dtra-factor-progression-sustaining",
      "dtra-factor-progression-type1",
      "dtra-factor-progression-type2",
      "dtra-factor-progression-type3"
    ],
    "relationship_ids": [
      "dtra-factor-progression-type1-foundational",
      "dtra-factor-progression-type2-foundational",
      "dtra-factor-progression-type2-impact",
      "dtra-factor-progression-type3-foundational",
      "dtra-factor-progression-type3-impact",
      "dtra-factor-progression-type3-sustaining"
    ],
    "analysis": "依据 G212 §5.4 与图5-4保留三层因素及内层前置条件。三种类型是解释性情形，不能据此认定本企业达到任何类型。",
    "legend": "三层颜色区分因素；射线只区分就绪类型，角度与长度无量化含义。日期须使用独立工作包路线图。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile dtra-factor-progression --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile dtra-factor-progression --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
