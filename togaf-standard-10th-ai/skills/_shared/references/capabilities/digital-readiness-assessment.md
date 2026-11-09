# 数字技术就绪度评估

ID：`digital-readiness-assessment`。主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G212 §5.2–5.4。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

哪些采用因素需要管理关注？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 哪些采用因素需要管理关注？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- category
- question_ids
- rating

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：readiness_factor。

```json
{
  "readiness_factor": [
    "category",
    "question_ids",
    "rating",
    "anchor",
    "evidence",
    "attention"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "category": {
    "meaning": "所声明分类体系下的分类",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "question_ids": {
    "meaning": "参与评价的问题标识",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "rating": {
    "meaning": "声明量表下的评价值",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "anchor": {
    "meaning": "评价值对应的量表锚点",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "evidence": {
    "meaning": "本条观察的证据描述或引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "attention": {
    "meaning": "需要管理关注的原因",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 逐因素汇总有依据的问卷结果
2. 按来源规则识别关注因素
3. 分析其主要后果
4. 形成改进建议

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 没有来源或用户规则时不创建统一总分合格线
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 没有来源或用户规则时不创建统一总分合格线


## 视图和交付物

- [数字技术就绪度评估](../profiles/digital-readiness-assessment-default.md)

- [organization-model](../deliverables/organization-model.md)
- [tailored-architecture-framework](../deliverables/tailored-architecture-framework.md)
- [capability-assessment](../deliverables/capability-assessment.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「数字技术就绪度评估」给出：没有来源或用户规则时不创建统一总分合格线",
    "expected": "missing-evidence",
    "why": "没有来源或用户规则时不创建统一总分合格线"
  },
  "modification_example": {
    "change": "在「数字技术就绪度评估」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "digital-readiness-assessment-default-record",
      "type": "readiness_factor",
      "name": "数字技术就绪度评估：订单范围记录",
      "attributes": {
        "category": "基础因素",
        "question_ids": "虚构订单案例中需验证的参与评价的问题标识",
        "rating": "同意（虚构回答）",
        "anchor": "虚构订单案例中需验证的评价值对应的量表锚点",
        "evidence": "虚构场景说明，非实测证据",
        "attention": "需补充承运商一侧的责任证据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-digital-readiness-assessment-default",
    "artifact_id": "digital-readiness-assessment",
    "profile_id": "digital-readiness-assessment-default",
    "title": "数字技术就绪度评估／虚构案例",
    "entity_ids": [
      "digital-readiness-assessment-default-record"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact digital-readiness-assessment --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
