# 采用因素递进路线

ID：`adoption-factor-progression`。主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G212 §5.4；图5-4。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

怎样逐步补齐采用短板？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 怎样逐步补齐采用短板？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- factor_category
- prerequisite
- action

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：readiness_factor, assessment_result。

```json
{
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
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "factor_category": {
    "meaning": "基础、影响或持续因素分类",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "prerequisite": {
    "meaning": "可执行该项的前置条件",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "action": {
    "meaning": "拟采取的具体行动",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "state_id": {
    "meaning": "具体架构状态的稳定标识",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "readiness_evidence": {
    "meaning": "就绪条件的证据",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 依据问卷及特征证据识别基础、影响、持续因素短板
2. 保留三层前置语义及类型1/2/3的定性定义
3. 将项目分类与原始证据绑定；证据不足保留待评估
4. 将补齐短板的具体行动追溯至因素；日期与依赖另建工作包路线图

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 基础、影响、持续三层完整；类型1/2/3不是实施步骤
- 类型2满足基础与影响；类型3还须满足持续因素
- 日期不进入因素递进图；项目分类须以明确评估证据支持

- 把类型1/2/3当成三个实施步骤
- 把射线角度长度解释为评分
- 尚未满足基础层就声称满足外层
- 把示意类型当作企业实际评估结果


## 视图和交付物

- [采用因素分层与就绪类型](../profiles/adoption-factor-progression-default.md)
- [采用因素分层与就绪类型](../profiles/dtra-factor-progression.md)

- [organization-model](../deliverables/organization-model.md)
- [tailored-architecture-framework](../deliverables/tailored-architecture-framework.md)
- [capability-assessment](../deliverables/capability-assessment.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「采用因素递进路线」给出：射线长度和角度不是定量评分，因素层次不等于 ADM 阶段",
    "expected": "missing-evidence",
    "why": "射线长度和角度不是定量评分，因素层次不等于 ADM 阶段"
  },
  "modification_example": {
    "change": "在「采用因素递进路线」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "adoption-factor-progression-default-foundational",
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
      "id": "adoption-factor-progression-default-impact",
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
      "id": "adoption-factor-progression-default-sustaining",
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
      "id": "adoption-factor-progression-default-type1",
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
      "id": "adoption-factor-progression-default-type2",
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
      "id": "adoption-factor-progression-default-type3",
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
      "id": "adoption-factor-progression-default-type1-foundational",
      "source": "adoption-factor-progression-default-type1",
      "target": "adoption-factor-progression-default-foundational",
      "type": "traces_to",
      "label": "该就绪情形满足此因素层（定性定义）",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "adoption-factor-progression-default-type2-foundational",
      "source": "adoption-factor-progression-default-type2",
      "target": "adoption-factor-progression-default-foundational",
      "type": "traces_to",
      "label": "该就绪情形满足此因素层（定性定义）",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "adoption-factor-progression-default-type2-impact",
      "source": "adoption-factor-progression-default-type2",
      "target": "adoption-factor-progression-default-impact",
      "type": "traces_to",
      "label": "该就绪情形满足此因素层（定性定义）",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "adoption-factor-progression-default-type3-foundational",
      "source": "adoption-factor-progression-default-type3",
      "target": "adoption-factor-progression-default-foundational",
      "type": "traces_to",
      "label": "该就绪情形满足此因素层（定性定义）",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "adoption-factor-progression-default-type3-impact",
      "source": "adoption-factor-progression-default-type3",
      "target": "adoption-factor-progression-default-impact",
      "type": "traces_to",
      "label": "该就绪情形满足此因素层（定性定义）",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "adoption-factor-progression-default-type3-sustaining",
      "source": "adoption-factor-progression-default-type3",
      "target": "adoption-factor-progression-default-sustaining",
      "type": "traces_to",
      "label": "该就绪情形满足此因素层（定性定义）",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-adoption-factor-progression-default",
    "artifact_id": "adoption-factor-progression",
    "profile_id": "adoption-factor-progression-default",
    "title": "采用因素分层与三种就绪情形／虚构示例",
    "entity_ids": [
      "adoption-factor-progression-default-foundational",
      "adoption-factor-progression-default-impact",
      "adoption-factor-progression-default-sustaining",
      "adoption-factor-progression-default-type1",
      "adoption-factor-progression-default-type2",
      "adoption-factor-progression-default-type3"
    ],
    "relationship_ids": [
      "adoption-factor-progression-default-type1-foundational",
      "adoption-factor-progression-default-type2-foundational",
      "adoption-factor-progression-default-type2-impact",
      "adoption-factor-progression-default-type3-foundational",
      "adoption-factor-progression-default-type3-impact",
      "adoption-factor-progression-default-type3-sustaining"
    ],
    "analysis": "依据 G212 §5.4 与图5-4保留三层因素及内层前置条件。三种类型是解释性情形，不能据此认定本企业达到任何类型。",
    "legend": "三层颜色区分因素；射线只区分就绪类型，角度与长度无量化含义。日期须使用独立工作包路线图。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact adoption-factor-progression --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
