# 技术元数据推断方案

ID：`metadata-inference-design`。主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G234 §4.3；图4-10。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

抽取技术元数据需要访问什么？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 抽取技术元数据需要访问什么？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- data_structure
- schema_access
- content_access

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：inference_source。

```json
{
  "inference_source": [
    "data_structure",
    "schema_access",
    "content_access",
    "cost",
    "risk",
    "scope"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "data_structure": {
    "meaning": "结构化、半结构化或非结构化类别",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "schema_access": {
    "meaning": "所需数据模式访问",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "content_access": {
    "meaning": "是否及如何访问实际内容",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "cost": {
    "meaning": "成本及估算边界",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "risk": {
    "meaning": "风险对象引用",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "scope": {
    "meaning": "适用组织、业务及架构边界",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 区分结构化半结构化非结构化
2. 确定可用模式与稳定性
3. 判断是否必须扫描内容
4. 评估成本隐私和风险

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 采集模式不必然需要读取实际业务数据
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 采集模式不必然需要读取实际业务数据


## 视图和交付物

- [技术元数据推断方案](../profiles/metadata-inference-design-default.md)
- [技术元数据推断架构](../profiles/metadata-inference-structure.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)
- [architecture-requirements-specification](../deliverables/architecture-requirements-specification.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「技术元数据推断方案」给出：采集模式不必然需要读取实际业务数据",
    "expected": "missing-evidence",
    "why": "采集模式不必然需要读取实际业务数据"
  },
  "modification_example": {
    "change": "在「技术元数据推断方案」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "metadata-inference-design-default-structured",
      "type": "inference_source",
      "name": "结构化来源",
      "attributes": {
        "data_structure": "结构化",
        "schema_access": "可读字段模式",
        "content_access": "无需读取客户实际值",
        "cost": "需估算连接器维护与源系统负载",
        "risk": "虚构订单案例中需验证的风险对象引用",
        "scope": "虚构星河零售：在线下单至仓库发运"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-inference-design-default-semi",
      "type": "inference_source",
      "name": "半结构化来源",
      "attributes": {
        "data_structure": "半结构化",
        "schema_access": "有结构但需验证稳定性",
        "content_access": "仅在批准范围抽样",
        "cost": "需估算连接器维护与源系统负载",
        "risk": "虚构订单案例中需验证的风险对象引用",
        "scope": "虚构星河零售：在线下单至仓库发运"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-inference-design-default-unstructured",
      "type": "inference_source",
      "name": "非结构化来源",
      "attributes": {
        "data_structure": "非结构化",
        "schema_access": "无稳定字段模式",
        "content_access": "内容扫描需独立隐私与成本评估",
        "cost": "需估算连接器维护与源系统负载",
        "risk": "虚构订单案例中需验证的风险对象引用",
        "scope": "虚构星河零售：在线下单至仓库发运"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-metadata-inference-design-default",
    "artifact_id": "metadata-inference-design",
    "profile_id": "metadata-inference-design-default",
    "title": "技术元数据推断方案／虚构案例",
    "entity_ids": [
      "metadata-inference-design-default-structured",
      "metadata-inference-design-default-semi",
      "metadata-inference-design-default-unstructured"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact metadata-inference-design --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
