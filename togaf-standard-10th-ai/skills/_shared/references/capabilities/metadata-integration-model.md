# 元数据集成模型

ID：`metadata-integration-model`。主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G234 §4.3；图4-7、4-8。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

多个元数据源如何协作并避免孤岛？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 多个元数据源如何协作并避免孤岛？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- integration_style
- authority
- scope

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：metadata_repository。

```json
{
  "metadata_repository": [
    "integration_style",
    "authority",
    "scope",
    "contract",
    "synchronization",
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
  "integration_style": {
    "meaning": "集中、混合或统一等组织方式",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "authority": {
    "meaning": "决策或数据权威及授权范围",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "scope": {
    "meaning": "适用组织、业务及架构边界",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "contract": {
    "meaning": "数据或元数据交换契约",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "synchronization": {
    "meaning": "同步方向、时效和一致性条件",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "owner": {
    "meaning": "对对象负责的责任方",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 比较集中混合统一模型
2. 明确各库主次权威
3. 定义交换契约
4. 检查一致性和社区协作

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 集成组织方式与手工推送拉取采集方式是两个独立维度
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 集成组织方式与手工推送拉取采集方式是两个独立维度


## 视图和交付物

- [元数据集成模型](../profiles/metadata-integration-model-default.md)
- [元数据集成组织备选](../profiles/metadata-central-hybrid-unified.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)
- [architecture-requirements-specification](../deliverables/architecture-requirements-specification.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「元数据集成模型」给出：集成组织方式与手工推送拉取采集方式是两个独立维度",
    "expected": "missing-evidence",
    "why": "集成组织方式与手工推送拉取采集方式是两个独立维度"
  },
  "modification_example": {
    "change": "在「元数据集成模型」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "metadata-integration-model-default-0",
      "type": "metadata_repository",
      "name": "集中候选方案",
      "attributes": {
        "integration_style": "集中",
        "authority": "明确中央与源方的主记录责任；需逐项裁剪",
        "scope": "虚构星河零售：在线下单至仓库发运",
        "contract": "虚构订单案例中需验证的数据或元数据交换契约",
        "synchronization": "按权威和时效要求交换，非默认双向写",
        "owner": "虚构业务负责人",
        "style": "集中",
        "collaboration": "源方与中央团队按契约协作",
        "consumers": "订单与客户服务应用"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-integration-model-default-1",
      "type": "metadata_repository",
      "name": "混合候选方案",
      "attributes": {
        "integration_style": "混合",
        "authority": "明确中央与源方的主记录责任；需逐项裁剪",
        "scope": "虚构星河零售：在线下单至仓库发运",
        "contract": "虚构订单案例中需验证的数据或元数据交换契约",
        "synchronization": "按权威和时效要求交换，非默认双向写",
        "owner": "虚构业务负责人",
        "style": "混合",
        "collaboration": "源方与中央团队按契约协作",
        "consumers": "订单与客户服务应用"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-integration-model-default-2",
      "type": "metadata_repository",
      "name": "统一候选方案",
      "attributes": {
        "integration_style": "统一",
        "authority": "明确中央与源方的主记录责任；需逐项裁剪",
        "scope": "虚构星河零售：在线下单至仓库发运",
        "contract": "虚构订单案例中需验证的数据或元数据交换契约",
        "synchronization": "按权威和时效要求交换，非默认双向写",
        "owner": "虚构业务负责人",
        "style": "统一",
        "collaboration": "源方与中央团队按契约协作",
        "consumers": "订单与客户服务应用"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-metadata-integration-model-default",
    "artifact_id": "metadata-integration-model",
    "profile_id": "metadata-integration-model-default",
    "title": "元数据集成模型／虚构案例",
    "entity_ids": [
      "metadata-integration-model-default-0",
      "metadata-integration-model-default-1",
      "metadata-integration-model-default-2"
    ],
    "relationship_ids": [],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact metadata-integration-model --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
