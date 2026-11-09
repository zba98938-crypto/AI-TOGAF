# 就绪度因素后果分析

ID：`readiness-consequence-analysis`。主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G212 §5.3；图5-3。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

缺失因素会如何影响采用结果？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 缺失因素会如何影响采用结果？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- factor
- primary_consequence
- business_effect

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：consequence, readiness_consequence, readiness_factor。

```json
{}
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
  "primary_consequence": {
    "meaning": "因素缺失的主要后果",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "business_effect": {
    "meaning": "对本地业务的影响解释",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "owner": {
    "meaning": "对对象负责的责任方",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "action": {
    "meaning": "拟采取的具体行动",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `has_consequence` | readiness_factor,assessment_factor,problem → consequence | 缺失或不足条件对应定性后果 |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 识别不足因素
2. 对照其主要后果
3. 分析多个后果相互作用
4. 指定管理行动及责任

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 背景重复因素列表不表示全连接依赖，后果未自带概率和严重度
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 背景重复因素列表不表示全连接依赖，后果未自带概率和严重度


## 视图和交付物

- [就绪度因素后果分析](../profiles/readiness-consequence-analysis-default.md)
- [因素与主要后果矩阵](../profiles/dtra-factor-consequence.md)

- [organization-model](../deliverables/organization-model.md)
- [tailored-architecture-framework](../deliverables/tailored-architecture-framework.md)
- [capability-assessment](../deliverables/capability-assessment.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「就绪度因素后果分析」给出：背景重复因素列表不表示全连接依赖，后果未自带概率和严重度",
    "expected": "duplicate-id",
    "why": "背景重复因素列表不表示全连接依赖，后果未自带概率和严重度"
  },
  "modification_example": {
    "change": "在「就绪度因素后果分析」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "readiness-consequence-analysis-default-factor",
      "type": "readiness_factor",
      "name": "赞助与方向",
      "attributes": {
        "category": "基础",
        "rating": 4,
        "evidence": "虚构访谈：发起人尚未承诺"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "readiness-consequence-analysis-default-consequence",
      "type": "consequence",
      "name": "决策和资源缺乏持续支持",
      "attributes": {
        "definition": "条件性主要后果；发生概率待分析"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "readiness-consequence-analysis-default-factor-consequence",
      "type": "has_consequence",
      "source": "readiness-consequence-analysis-default-factor",
      "target": "readiness-consequence-analysis-default-consequence",
      "label": "因素不足可能导致该后果",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-readiness-consequence-analysis-default",
    "artifact_id": "readiness-consequence-analysis",
    "profile_id": "readiness-consequence-analysis-default",
    "title": "就绪度因素后果分析／虚构案例",
    "entity_ids": [
      "readiness-consequence-analysis-default-factor",
      "readiness-consequence-analysis-default-consequence"
    ],
    "relationship_ids": [
      "readiness-consequence-analysis-default-factor-consequence"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact readiness-consequence-analysis --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
