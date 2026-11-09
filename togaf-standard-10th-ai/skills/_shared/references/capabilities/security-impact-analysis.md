# 安全影响分析

ID：`security-impact-analysis`。主责：[togaf-security-risk](../../../togaf-security-risk/SKILL.md)。

来源：G152 §5.7、5.9。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

架构变更怎样改变安全与风险？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 架构变更怎样改变安全与风险？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- change
- affected_asset
- requirement

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：security_impact。

```json
{
  "security_impact": [
    "change",
    "affected_asset",
    "requirement",
    "control",
    "risk",
    "decision"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "change": {
    "meaning": "待评估变更引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "affected_asset": {
    "meaning": "经分析受影响的资产",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "requirement": {
    "meaning": "需求对象引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "control": {
    "meaning": "控制措施引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "risk": {
    "meaning": "风险对象引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "decision": {
    "meaning": "决策结果、理由和状态",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 定位变化对象
2. 沿已知关系查找安全需求控制和风险
3. 区分候选与确认影响
4. 提出复评或新 ADM 迭代建议

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 图可达只是候选影响，不能自动认定所有对象受损
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 图可达只是候选影响，不能自动认定所有对象受损


## 视图和交付物

- [安全影响分析](../profiles/security-impact-analysis-default.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)
- [architecture-requirements-specification](../deliverables/architecture-requirements-specification.md)
- [requirements-impact-assessment](../deliverables/requirements-impact-assessment.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「安全影响分析」给出：图可达只是候选影响，不能自动认定所有对象受损",
    "expected": "missing-evidence",
    "why": "图可达只是候选影响，不能自动认定所有对象受损"
  },
  "modification_example": {
    "change": "在「安全影响分析」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "security-impact-analysis-default-record",
      "type": "security_impact",
      "name": "安全影响分析：订单范围记录",
      "attributes": {
        "change": "虚构订单案例中需验证的待评估变更引用",
        "affected_asset": "虚构订单案例中需验证的经分析受影响的资产",
        "requirement": "订单不得丢失且一天内发运",
        "control": "访问认证和操作审计",
        "risk": "虚构订单案例中需验证的风险对象引用",
        "decision": "虚构订单案例中需验证的决策结果、理由和状态"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-security-impact-analysis-default",
    "artifact_id": "security-impact-analysis",
    "profile_id": "security-impact-analysis-default",
    "title": "安全影响分析／虚构案例",
    "entity_ids": [
      "security-impact-analysis-default-record"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact security-impact-analysis --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
