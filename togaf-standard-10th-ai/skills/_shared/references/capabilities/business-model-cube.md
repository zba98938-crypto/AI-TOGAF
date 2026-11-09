# 业务模型立方体

ID：`business-model-cube`。主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G18A/fig2-3。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

检查价值主张、客户、伙伴、活动、胜任力和价值公式及其关系是否一致

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 检查价值主张、客户、伙伴、活动、胜任力和价值公式及其关系是否一致
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- dimension
- detail
- local_mapping

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：business_model_dimension。

```json
{
  "business_model_dimension": [
    "dimension",
    "detail",
    "local_mapping"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "dimension": {
    "meaning": "评价维度",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "detail": {
    "meaning": "在本工作产品范围中明确定义的 detail 属性",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "local_mapping": {
    "meaning": "参考概念与本地概念的映射",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 分别界定六个并列维度
2. 采集本地内容并注明来源
3. 只声明有依据的维度间关系
4. 分析价值创造与获取约束
5. 标记关系缺口

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 中央Relations表示关系核心而非第七维度；六维没有流程先后或由位置确定的层级
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 中央Relations表示关系核心而非第七维度；六维没有流程先后或由位置确定的层级


## 视图和交付物

- [业务模型立方体](../profiles/business-model-cube-default.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「业务模型立方体」给出：中央Relations表示关系核心而非第七维度；六维没有流程先后或由位置确定的层级",
    "expected": "missing-evidence",
    "why": "中央Relations表示关系核心而非第七维度；六维没有流程先后或由位置确定的层级"
  },
  "modification_example": {
    "change": "在「业务模型立方体」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "business-model-cube-default-0",
      "type": "business_model_dimension",
      "name": "价值主张",
      "attributes": {
        "dimension": "价值主张",
        "detail": "可靠且透明的商品履约",
        "local_mapping": "从参考维度映射到本例业务候选，待验证"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-model-cube-default-1",
      "type": "business_model_dimension",
      "name": "客户",
      "attributes": {
        "dimension": "客户",
        "detail": "需要按承诺交付的线上客户",
        "local_mapping": "从参考维度映射到本例业务候选，待验证"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-model-cube-default-2",
      "type": "business_model_dimension",
      "name": "网络伙伴",
      "attributes": {
        "dimension": "网络伙伴",
        "detail": "承运商与商品供应方",
        "local_mapping": "从参考维度映射到本例业务候选，待验证"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-model-cube-default-3",
      "type": "business_model_dimension",
      "name": "活动",
      "attributes": {
        "dimension": "活动",
        "detail": "确认订单、拣配发运、处理例外",
        "local_mapping": "从参考维度映射到本例业务候选，待验证"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-model-cube-default-4",
      "type": "business_model_dimension",
      "name": "胜任力",
      "attributes": {
        "dimension": "胜任力",
        "detail": "履约协调与订单信息治理",
        "local_mapping": "从参考维度映射到本例业务候选，待验证"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-model-cube-default-5",
      "type": "business_model_dimension",
      "name": "价值公式",
      "attributes": {
        "dimension": "价值公式",
        "detail": "明确期间收入减采购履约和固定成本；尚无数值",
        "local_mapping": "从参考维度映射到本例业务候选，待验证"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "business-model-cube-default-customer-value",
      "type": "traces_to",
      "source": "business-model-cube-default-0",
      "target": "business-model-cube-default-1",
      "label": "本例价值主张面向该客户；项目补充关系",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-model-cube-default-partner-activity",
      "type": "traces_to",
      "source": "business-model-cube-default-2",
      "target": "business-model-cube-default-3",
      "label": "承运商参与发运活动；项目补充关系",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "business-model-cube-default-competence-activity",
      "type": "traces_to",
      "source": "business-model-cube-default-4",
      "target": "business-model-cube-default-3",
      "label": "胜任力支撑活动；不是来源图流程箭头",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-business-model-cube-default",
    "artifact_id": "business-model-cube",
    "profile_id": "business-model-cube-default",
    "title": "业务模型立方体／虚构案例",
    "entity_ids": [
      "business-model-cube-default-0",
      "business-model-cube-default-1",
      "business-model-cube-default-2",
      "business-model-cube-default-3",
      "business-model-cube-default-4",
      "business-model-cube-default-5"
    ],
    "relationship_ids": [
      "business-model-cube-default-customer-value",
      "business-model-cube-default-partner-activity",
      "business-model-cube-default-competence-activity"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact business-model-cube --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
