# 数据质量评估

ID：`data-quality-assessment`。主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G152 §5.4；G234 §4.2。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

数据质量能否支持业务与风险目标？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 数据质量能否支持业务与风险目标？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- dataset
- dimension
- metric

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：data_quality_measure。

```json
{
  "data_quality_measure": [
    "dataset",
    "dimension",
    "metric",
    "unit",
    "threshold",
    "owner",
    "evidence_period"
  ],
  "data_quality_rule": [
    "dimension",
    "rule_expression",
    "threshold",
    "measure_period",
    "owner"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "dataset": {
    "meaning": "被评价或使用的数据集",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "dimension": {
    "meaning": "评价维度",
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
  "threshold": {
    "meaning": "判定边界及依据",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "owner": {
    "meaning": "对对象负责的责任方",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "evidence_period": {
    "meaning": "证据采集期间",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 确定数据集与质量责任
2. 选定相关维度和可计算定义
3. 使用日志或样本评估
4. 关联业务影响和改进措施

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 不同质量维度不能无依据地加总成一个精确分数
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 不同质量维度不能无依据地加总成一个精确分数


## 视图和交付物

- [数据质量评估](../profiles/data-quality-assessment-default.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)
- [architecture-requirements-specification](../deliverables/architecture-requirements-specification.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「数据质量评估」给出：不同质量维度不能无依据地加总成一个精确分数",
    "expected": "missing-evidence",
    "why": "不同质量维度不能无依据地加总成一个精确分数"
  },
  "modification_example": {
    "change": "在「数据质量评估」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "data-quality-assessment-default-record",
      "type": "data_quality_measure",
      "name": "数据质量评估：订单范围记录",
      "attributes": {
        "dataset": "虚构在线订单集",
        "dimension": "完整性",
        "metric": "已确认订单中包含履约必填项的比例",
        "unit": "百分比",
        "threshold": "示例期望100%，需业务方确认",
        "owner": "虚构业务负责人",
        "evidence_period": "2026年10月虚构抽样"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-data-quality-assessment-default",
    "artifact_id": "data-quality-assessment",
    "profile_id": "data-quality-assessment-default",
    "title": "数据质量评估／虚构案例",
    "entity_ids": [
      "data-quality-assessment-default-record"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact data-quality-assessment --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
