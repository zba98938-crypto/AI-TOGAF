# 元数据资产覆盖矩阵

`profile_id`: metadata-asset-coverage-default；`artifact_id`: metadata-asset-coverage；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G234 §4.3；图4-5。

## 构图与定义状态

表示族：`matrix`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。",
  "row_types": [
    "metadata_asset"
  ],
  "column_types": [
    "criterion"
  ]
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：criterion, metadata_asset。关系类型：traces_to。

```json
{
  "entities": {},
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 参考图空格不表示禁止、不存在或无需管理
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

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

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile metadata-asset-coverage-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile metadata-asset-coverage-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
