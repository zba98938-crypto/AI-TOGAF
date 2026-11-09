# 元数据规则与政策文档

ID：`metadata-policy-documentation`。主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G234 §3、§5.1。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

怎样保证元数据被一致维护？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 怎样保证元数据被一致维护？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- scope
- rule
- authority

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：metadata_policy。

```json
{
  "metadata_policy": [
    "scope",
    "rule",
    "authority",
    "validation",
    "exception",
    "version"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "scope": {
    "meaning": "适用组织、业务及架构边界",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "rule": {
    "meaning": "可验证规则陈述",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "authority": {
    "meaning": "决策或数据权威及授权范围",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "validation": {
    "meaning": "校验条件与方法",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "exception": {
    "meaning": "例外及其治理方式",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "version": {
    "meaning": "来源或规范版本",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 收集监管和业务规则
2. 形式化验证条件
3. 明确维护责任和例外流程
4. 与质量需求对齐

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 政策描述与可执行验证规则需分别标识
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 政策描述与可执行验证规则需分别标识


## 视图和交付物

- [元数据规则与政策文档](../profiles/metadata-policy-documentation-default.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)
- [architecture-requirements-specification](../deliverables/architecture-requirements-specification.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「元数据规则与政策文档」给出：政策描述与可执行验证规则需分别标识",
    "expected": "missing-evidence",
    "why": "政策描述与可执行验证规则需分别标识"
  },
  "modification_example": {
    "change": "在「元数据规则与政策文档」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "metadata-policy-documentation-default-record",
      "type": "metadata_policy",
      "name": "元数据规则与政策文档：订单范围记录",
      "attributes": {
        "scope": "虚构星河零售：在线下单至仓库发运",
        "rule": "已发运订单必须有关联发运记录",
        "authority": "虚构订单案例中需验证的决策或数据权威及授权范围",
        "validation": "校验订单与发运标识对应关系",
        "exception": "虚构订单案例中需验证的例外及其治理方式",
        "version": "示例2026.1"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-metadata-policy-documentation-default",
    "artifact_id": "metadata-policy-documentation",
    "profile_id": "metadata-policy-documentation-default",
    "title": "元数据规则与政策文档／虚构案例",
    "entity_ids": [
      "metadata-policy-documentation-default-record"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact metadata-policy-documentation --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
