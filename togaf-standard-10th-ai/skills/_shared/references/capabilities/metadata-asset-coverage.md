# 元数据资产覆盖矩阵

ID：`metadata-asset-coverage`。主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G234 §4.3；图4-5；G234 §5.2 图5-2、表5-2 L641–664；G234 §4.3 图4-5（现有工作产品扩展关系）。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

所需元数据范围是否覆盖管理关注点？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 所需元数据范围是否覆盖管理关注点？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- metadata_category
- management_dimension
- definition

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则
- 按需使用 metadata-application-function-coverage，输入功能/工具/资产覆盖证据；不改变原默认分类矩阵

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：criterion, metadata_asset。

```json
{}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "metadata_category": {
    "meaning": "业务、技术或运营元数据类别",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "management_dimension": {
    "meaning": "文档化、参考数据、治理等管理维度",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "definition": {
    "meaning": "业务含义和排除边界",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "owner": {
    "meaning": "对对象负责的责任方",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "coverage": {
    "meaning": "所需范围的覆盖判断",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `traces_to` | * → * | 显式追溯，具体理由记录在 label |

## 分析步骤

1. 确定三类元数据和四个管理维度
2. 归置资产
3. 检查业务需求所需但缺失的条目
4. 记录裁剪

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 参考图空格不表示禁止、不存在或无需管理
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 参考图空格不表示禁止、不存在或无需管理


## 视图和交付物

- [元数据资产覆盖矩阵](../profiles/metadata-asset-coverage-default.md)
- [元数据资产分类覆盖](../profiles/metadata-category-coverage.md)
- [元数据应用功能—工具—资产覆盖评估表](../profiles/metadata-application-function-coverage.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)
- [architecture-requirements-specification](../deliverables/architecture-requirements-specification.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「元数据资产覆盖矩阵」给出：参考图空格不表示禁止、不存在或无需管理",
    "expected": "empty-view",
    "why": "参考图空格不表示禁止、不存在或无需管理"
  },
  "modification_example": {
    "change": "在「元数据资产覆盖矩阵」的范围内新增或修改一项，检查下游是否随之变化",
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
      "id": "metadata-asset-coverage-default-row0",
      "type": "metadata_asset",
      "name": "业务",
      "attributes": {
        "metadata_category": "业务",
        "definition": "元数据类别，不是数据保密等级"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-asset-coverage-default-row1",
      "type": "metadata_asset",
      "name": "技术",
      "attributes": {
        "metadata_category": "技术",
        "definition": "元数据类别，不是数据保密等级"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-asset-coverage-default-row2",
      "type": "metadata_asset",
      "name": "运营",
      "attributes": {
        "metadata_category": "运营",
        "definition": "元数据类别，不是数据保密等级"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-asset-coverage-default-col0",
      "type": "criterion",
      "name": "数据质量",
      "attributes": {
        "definition": "本例所检查的管理维度"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-asset-coverage-default-col1",
      "type": "criterion",
      "name": "文档化",
      "attributes": {
        "definition": "本例所检查的管理维度"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-asset-coverage-default-col2",
      "type": "criterion",
      "name": "安全与隐私",
      "attributes": {
        "definition": "本例所检查的管理维度"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "metadata-asset-coverage-default-col3",
      "type": "criterion",
      "name": "治理",
      "attributes": {
        "definition": "本例所检查的管理维度"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "metadata-asset-coverage-default-coverage00",
      "type": "traces_to",
      "source": "metadata-asset-coverage-default-row0",
      "target": "metadata-asset-coverage-default-col0",
      "label": "本例候选资产已识别；覆盖程度需核验",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "codes": "candidate"
      }
    },
    {
      "id": "metadata-asset-coverage-default-coverage01",
      "type": "traces_to",
      "source": "metadata-asset-coverage-default-row0",
      "target": "metadata-asset-coverage-default-col1",
      "label": "本例候选资产已识别；覆盖程度需核验",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "codes": "candidate"
      }
    },
    {
      "id": "metadata-asset-coverage-default-coverage02",
      "type": "traces_to",
      "source": "metadata-asset-coverage-default-row0",
      "target": "metadata-asset-coverage-default-col2",
      "label": "本例候选资产已识别；覆盖程度需核验",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "codes": "candidate"
      }
    },
    {
      "id": "metadata-asset-coverage-default-coverage03",
      "type": "traces_to",
      "source": "metadata-asset-coverage-default-row0",
      "target": "metadata-asset-coverage-default-col3",
      "label": "本例候选资产已识别；覆盖程度需核验",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "codes": "candidate"
      }
    },
    {
      "id": "metadata-asset-coverage-default-coverage10",
      "type": "traces_to",
      "source": "metadata-asset-coverage-default-row1",
      "target": "metadata-asset-coverage-default-col0",
      "label": "本例候选资产已识别；覆盖程度需核验",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "codes": "candidate"
      }
    },
    {
      "id": "metadata-asset-coverage-default-coverage11",
      "type": "traces_to",
      "source": "metadata-asset-coverage-default-row1",
      "target": "metadata-asset-coverage-default-col1",
      "label": "本例候选资产已识别；覆盖程度需核验",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "codes": "candidate"
      }
    },
    {
      "id": "metadata-asset-coverage-default-coverage12",
      "type": "traces_to",
      "source": "metadata-asset-coverage-default-row1",
      "target": "metadata-asset-coverage-default-col2",
      "label": "本例候选资产已识别；覆盖程度需核验",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "codes": "candidate"
      }
    },
    {
      "id": "metadata-asset-coverage-default-coverage13",
      "type": "traces_to",
      "source": "metadata-asset-coverage-default-row1",
      "target": "metadata-asset-coverage-default-col3",
      "label": "本例候选资产已识别；覆盖程度需核验",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "codes": "candidate"
      }
    },
    {
      "id": "metadata-asset-coverage-default-coverage20",
      "type": "traces_to",
      "source": "metadata-asset-coverage-default-row2",
      "target": "metadata-asset-coverage-default-col0",
      "label": "本例候选资产已识别；覆盖程度需核验",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "codes": "candidate"
      }
    },
    {
      "id": "metadata-asset-coverage-default-coverage22",
      "type": "traces_to",
      "source": "metadata-asset-coverage-default-row2",
      "target": "metadata-asset-coverage-default-col2",
      "label": "本例候选资产已识别；覆盖程度需核验",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "codes": "candidate"
      }
    },
    {
      "id": "metadata-asset-coverage-default-coverage23",
      "type": "traces_to",
      "source": "metadata-asset-coverage-default-row2",
      "target": "metadata-asset-coverage-default-col3",
      "label": "本例候选资产已识别；覆盖程度需核验",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed",
      "attributes": {
        "codes": "candidate"
      }
    }
  ],
  "view": {
    "id": "v-metadata-asset-coverage-default",
    "artifact_id": "metadata-asset-coverage",
    "profile_id": "metadata-asset-coverage-default",
    "title": "元数据资产覆盖矩阵／虚构案例",
    "entity_ids": [
      "metadata-asset-coverage-default-row0",
      "metadata-asset-coverage-default-row1",
      "metadata-asset-coverage-default-row2",
      "metadata-asset-coverage-default-col0",
      "metadata-asset-coverage-default-col1",
      "metadata-asset-coverage-default-col2",
      "metadata-asset-coverage-default-col3"
    ],
    "relationship_ids": [
      "metadata-asset-coverage-default-coverage00",
      "metadata-asset-coverage-default-coverage01",
      "metadata-asset-coverage-default-coverage02",
      "metadata-asset-coverage-default-coverage03",
      "metadata-asset-coverage-default-coverage10",
      "metadata-asset-coverage-default-coverage11",
      "metadata-asset-coverage-default-coverage12",
      "metadata-asset-coverage-default-coverage13",
      "metadata-asset-coverage-default-coverage20",
      "metadata-asset-coverage-default-coverage22",
      "metadata-asset-coverage-default-coverage23"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact metadata-asset-coverage --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
