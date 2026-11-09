# 数字技术就绪度问卷

ID：`digital-readiness-questionnaire`。主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G212 §5.2、附录A。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

如何取得可比较的就绪度观察？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 如何取得可比较的就绪度观察？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- factor
- category
- statement

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：readiness_question。

```json
{
  "readiness_question": [
    "factor",
    "category",
    "statement",
    "scale_anchor",
    "respondent",
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
  "factor": {
    "meaning": "就绪度因素",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "category": {
    "meaning": "所声明分类体系下的分类",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "statement": {
    "meaning": "原子陈述或问题",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "scale_anchor": {
    "meaning": "量表级别的含义",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "respondent": {
    "meaning": "问卷回答者或角色",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "evidence": {
    "meaning": "本条观察的证据描述或引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 按因素选择问题
2. 声明七级李克特锚点
3. 邀请关键领导者作答并讨论共识
4. 保留原始答复与证据

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 问卷答案不是客观测量值，需说明参与者与共识过程
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 问卷答案不是客观测量值，需说明参与者与共识过程


## 视图和交付物

- [数字技术就绪度问卷](../profiles/digital-readiness-questionnaire-default.md)

- [organization-model](../deliverables/organization-model.md)
- [tailored-architecture-framework](../deliverables/tailored-architecture-framework.md)
- [capability-assessment](../deliverables/capability-assessment.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「数字技术就绪度问卷」给出：问卷答案不是客观测量值，需说明参与者与共识过程",
    "expected": "missing-evidence",
    "why": "问卷答案不是客观测量值，需说明参与者与共识过程"
  },
  "modification_example": {
    "change": "在「数字技术就绪度问卷」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "digital-readiness-questionnaire-default-record",
      "type": "readiness_question",
      "name": "数字技术就绪度问卷：订单范围记录",
      "attributes": {
        "factor": "变更问责",
        "category": "基础因素",
        "statement": "业务负责人明确承担数字采用的问责",
        "scale_anchor": "七级李克特：按问卷声明解释",
        "respondent": "虚构业务负责人",
        "evidence": "虚构场景说明，非实测证据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-digital-readiness-questionnaire-default",
    "artifact_id": "digital-readiness-questionnaire",
    "profile_id": "digital-readiness-questionnaire-default",
    "title": "数字技术就绪度问卷／虚构案例",
    "entity_ids": [
      "digital-readiness-questionnaire-default-record"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact digital-readiness-questionnaire --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
