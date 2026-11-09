# 架构成熟度评分卡

ID：`architecture-maturity-scorecard`。主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G203 §2.2–2.3。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

当前 EA 实践达到哪些成熟度特征？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 当前 EA 实践达到哪些成熟度特征？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- element
- level
- evidence

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：maturity_observation。

```json
{
  "maturity_observation": [
    "element",
    "level",
    "evidence",
    "assessment_date",
    "assessor",
    "confidence"
  ],
  "assessment_result": [
    "subject_ref",
    "method_ref",
    "result_value",
    "unit",
    "period",
    "evidence"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "element": {
    "meaning": "成熟度要素",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "level": {
    "meaning": "所用模型下的层级",
    "value_rule": "保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "evidence": {
    "meaning": "本条观察的证据描述或引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "assessment_date": {
    "meaning": "评估日期",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "assessor": {
    "meaning": "评价人或评价角色",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "confidence": {
    "meaning": "判断可信度及理由",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 按要素获取证据
2. 逐特征评价达成
3. 记录争议和未知
4. 分别报告加权级别与逐级达成比例

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 加权等级与各级达成百分比是互补结果，不能互相替代
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 加权等级与各级达成百分比是互补结果，不能互相替代


## 视图和交付物

- [架构成熟度评分卡](../profiles/architecture-maturity-scorecard-default.md)
- [ACMM 证据评分卡](../profiles/acmm-scorecard.md)

- [organization-model](../deliverables/organization-model.md)
- [tailored-architecture-framework](../deliverables/tailored-architecture-framework.md)
- [capability-assessment](../deliverables/capability-assessment.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「架构成熟度评分卡」给出：加权等级与各级达成百分比是互补结果，不能互相替代",
    "expected": "missing-evidence",
    "why": "加权等级与各级达成百分比是互补结果，不能互相替代"
  },
  "modification_example": {
    "change": "在「架构成熟度评分卡」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "architecture-maturity-scorecard-default-record",
      "type": "maturity_observation",
      "name": "架构成熟度评分卡：订单范围记录",
      "attributes": {
        "element": "架构治理",
        "level": 2,
        "evidence": "虚构场景说明，非实测证据",
        "assessment_date": "2026-11-01",
        "assessor": "虚构评审小组",
        "confidence": "示例推演，不代表实测结论"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-architecture-maturity-scorecard-default",
    "artifact_id": "architecture-maturity-scorecard",
    "profile_id": "architecture-maturity-scorecard-default",
    "title": "架构成熟度评分卡／虚构案例",
    "entity_ids": [
      "architecture-maturity-scorecard-default-record"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact architecture-maturity-scorecard --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
