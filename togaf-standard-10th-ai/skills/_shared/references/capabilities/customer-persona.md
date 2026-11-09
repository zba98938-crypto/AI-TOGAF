# 客户画像

ID：`customer-persona`。主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G20F §5.5。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

为谁设计业务和产品体验？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 为谁设计业务和产品体验？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- segment
- goals
- behaviors

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：persona。

```json
{
  "persona": [
    "segment",
    "goals",
    "behaviors",
    "needs",
    "evidence",
    "assumptions"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "segment": {
    "meaning": "客户或业务分群",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "goals": {
    "meaning": "用户群体或业务目标",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "behaviors": {
    "meaning": "观察到的行为",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "needs": {
    "meaning": "用户需求",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "evidence": {
    "meaning": "本条观察的证据描述或引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "assumptions": {
    "meaning": "待验证假设",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 从研究划分相关群体
2. 归纳目标行为需求
3. 区分观察和假设
4. 检验代表性并链接旅程

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 虚构人物叙述不能冒充真实用户研究结果
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 虚构人物叙述不能冒充真实用户研究结果


## 视图和交付物

- [客户画像](../profiles/customer-persona-default.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「客户画像」给出：虚构人物叙述不能冒充真实用户研究结果",
    "expected": "missing-evidence",
    "why": "虚构人物叙述不能冒充真实用户研究结果"
  },
  "modification_example": {
    "change": "在「客户画像」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "customer-persona-default-persona",
      "type": "persona",
      "name": "线上常购客户画像",
      "attributes": {
        "segment": "虚构线上常购客户",
        "goals": "按承诺收货并可追踪",
        "behaviors": "本例假设会在发货前查询状态",
        "needs": "准确状态及例外说明",
        "evidence": "虚构案例输入，不是真实用户研究",
        "assumptions": "行为频次和群体代表性尚待验证",
        "block": "客户群体"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-customer-persona-default",
    "artifact_id": "customer-persona",
    "profile_id": "customer-persona-default",
    "title": "客户画像／虚构案例",
    "entity_ids": [
      "customer-persona-default-persona"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact customer-persona --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
