# 运营模式

ID：`operating-model`。主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G184/fig4-1；G21H §4.4.2、§5.3。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

决定业务流程跨单元集成与标准化的合理程度

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 决定业务流程跨单元集成与标准化的合理程度
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- integration
- standardization
- scope

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：operating_model, guide:operating_submodel。

```json
{
  "operating_model": [
    "integration",
    "standardization",
    "scope",
    "rationale",
    "quadrant"
  ],
  "guide:operating_submodel": [
    "submodel",
    "customer_segment",
    "decision",
    "implication",
    "linked_submodels",
    "measures",
    "capacity",
    "action",
    "evidence_detail",
    "reference_identity"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "integration": {
    "meaning": "与其他系统的集成约定",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "standardization": {
    "meaning": "在本工作产品范围中明确定义的 standardization 属性",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "scope": {
    "meaning": "适用组织、业务及架构边界",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "rationale": {
    "meaning": "分析或选择的理由",
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

1. 界定业务单元和流程范围
2. 分别评估业务流程集成和标准化
3. 按高低组合定位
4. 检验数据共享和治理要求
5. 允许企业内不同范围并存不同模式

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 两轴是业务流程而非IT集成与技术标准；四模式无优劣或必经演进顺序
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 两轴是业务流程而非IT集成与技术标准；四模式无优劣或必经演进顺序


## 视图和交付物

- [运营模式](../profiles/operating-model-default.md)
- [运营模式四子模型及资源取舍](../profiles/operating-model-four-submodels.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「运营模式」给出：两轴是业务流程而非IT集成与技术标准；四模式无优劣或必经演进顺序",
    "expected": "missing-evidence",
    "why": "两轴是业务流程而非IT集成与技术标准；四模式无优劣或必经演进顺序"
  },
  "modification_example": {
    "change": "在「运营模式」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "operating-model-default-coord",
      "type": "operating_model",
      "name": "协调",
      "attributes": {
        "integration": "高",
        "standardization": "低",
        "scope": "参考候选模式，尚未选定本地适用范围",
        "rationale": "本例只展示两轴定义；实际范围与权衡需访谈取证",
        "quadrant": "top-left"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "operating-model-default-unify",
      "type": "operating_model",
      "name": "统一",
      "attributes": {
        "integration": "高",
        "standardization": "高",
        "scope": "参考候选模式，尚未选定本地适用范围",
        "rationale": "本例只展示两轴定义；实际范围与权衡需访谈取证",
        "quadrant": "top-right"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "operating-model-default-diverse",
      "type": "operating_model",
      "name": "多元化",
      "attributes": {
        "integration": "低",
        "standardization": "低",
        "scope": "参考候选模式，尚未选定本地适用范围",
        "rationale": "本例只展示两轴定义；实际范围与权衡需访谈取证",
        "quadrant": "bottom-left"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "operating-model-default-replicate",
      "type": "operating_model",
      "name": "复制",
      "attributes": {
        "integration": "低",
        "standardization": "高",
        "scope": "参考候选模式，尚未选定本地适用范围",
        "rationale": "本例只展示两轴定义；实际范围与权衡需访谈取证",
        "quadrant": "bottom-right"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-operating-model-default",
    "artifact_id": "operating-model",
    "profile_id": "operating-model-default",
    "title": "运营模式／虚构案例",
    "entity_ids": [
      "operating-model-default-coord",
      "operating-model-default-unify",
      "operating-model-default-diverse",
      "operating-model-default-replicate"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact operating-model --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
