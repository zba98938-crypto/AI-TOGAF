# 利益相关者影响力与影响程度矩阵

ID：`stakeholder-influence-matrix`。主责：[togaf-vision-scenarios](../../../togaf-vision-scenarios/SKILL.md)。

来源：G184/fig4-3。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

依据影响力与所受影响程度选择介入策略

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 依据影响力与所受影响程度选择介入策略
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- influence
- impact
- engagement

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：stakeholder。

```json
{
  "stakeholder": [
    "influence",
    "impact",
    "engagement",
    "concern",
    "quadrant"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "influence": {
    "meaning": "在本工作产品范围中明确定义的 influence 属性",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "impact": {
    "meaning": "业务影响及其依据",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "engagement": {
    "meaning": "参与方式与节奏",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "concern": {
    "meaning": "利益相关者的具体关注点",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "quadrant": {
    "meaning": "在本工作产品范围中明确定义的 quadrant 属性",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 明确决策和关注点
2. 分别取得Influence与Impact证据
3. 按高低定位
4. 选择重点管理令其满意随时告知或监督
5. 核实问责与沟通边界

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 来源横轴是Impact不是Interest；介入策略不能取代RACI或决策授权
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 来源横轴是Impact不是Interest；介入策略不能取代RACI或决策授权


## 视图和交付物

- [利益相关者影响力与影响程度矩阵](../profiles/stakeholder-influence-matrix-default.md)

- [architecture-vision](../deliverables/architecture-vision.md)
- [statement-of-work](../deliverables/statement-of-work.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「利益相关者影响力与影响程度矩阵」给出：来源横轴是Impact不是Interest；介入策略不能取代RACI或决策授权",
    "expected": "missing-evidence",
    "why": "来源横轴是Impact不是Interest；介入策略不能取代RACI或决策授权"
  },
  "modification_example": {
    "change": "在「利益相关者影响力与影响程度矩阵」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "stakeholder-influence-matrix-default-sponsor",
      "type": "stakeholder",
      "name": "业务赞助人",
      "attributes": {
        "influence": "高",
        "impact": "高",
        "engagement": "重点管理",
        "concern": "本例在线履约变更对职责或成果的影响",
        "quadrant": "top-right",
        "evidence": "虚构分级，待当事方核实；不代表决策授权"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "stakeholder-influence-matrix-default-legal",
      "type": "stakeholder",
      "name": "法律顾问",
      "attributes": {
        "influence": "高",
        "impact": "低",
        "engagement": "令其满意",
        "concern": "本例在线履约变更对职责或成果的影响",
        "quadrant": "top-left",
        "evidence": "虚构分级，待当事方核实；不代表决策授权"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "stakeholder-influence-matrix-default-operator",
      "type": "stakeholder",
      "name": "仓库操作员",
      "attributes": {
        "influence": "低",
        "impact": "高",
        "engagement": "随时告知",
        "concern": "本例在线履约变更对职责或成果的影响",
        "quadrant": "bottom-right",
        "evidence": "虚构分级，待当事方核实；不代表决策授权"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "stakeholder-influence-matrix-default-observer",
      "type": "stakeholder",
      "name": "非试点地区观察者",
      "attributes": {
        "influence": "低",
        "impact": "低",
        "engagement": "监督",
        "concern": "本例在线履约变更对职责或成果的影响",
        "quadrant": "bottom-left",
        "evidence": "虚构分级，待当事方核实；不代表决策授权"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-stakeholder-influence-matrix-default",
    "artifact_id": "stakeholder-influence-matrix",
    "profile_id": "stakeholder-influence-matrix-default",
    "title": "利益相关者影响力与影响程度矩阵／虚构案例",
    "entity_ids": [
      "stakeholder-influence-matrix-default-sponsor",
      "stakeholder-influence-matrix-default-legal",
      "stakeholder-influence-matrix-default-operator",
      "stakeholder-influence-matrix-default-observer"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact stakeholder-influence-matrix --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
