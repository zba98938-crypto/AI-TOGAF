# 客户主数据模型

`profile_id`: customer-mdm-model-default；`artifact_id`: customer-mdm-model；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G21B §4–5。

## 构图与定义状态

表示族：`er`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：master_data。关系类型：traces_to。

```json
{
  "entities": {
    "master_data": [
      "business_identity",
      "identifier",
      "source",
      "matching",
      "ownership",
      "quality"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 统一客户标识不等于无条件合并不同业务语境
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
      "id": "customer-mdm-model-default-person",
      "type": "master_data",
      "name": "自然人客户内核",
      "attributes": {
        "business_identity": "在订单关系中承担购买主体的自然人",
        "identifier": "候选客户主标识",
        "source": "经核实的客户源记录",
        "matching": "标识冲突人工核验；不按姓名直接合并",
        "ownership": "客户数据所有者",
        "quality": "身份唯一且可追溯"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "customer-mdm-model-default-org",
      "type": "master_data",
      "name": "组织客户内核",
      "attributes": {
        "business_identity": "作为法律主体形成采购关系的组织",
        "identifier": "候选组织主标识",
        "source": "企业客户源记录",
        "matching": "按核实组织标识匹配",
        "ownership": "企业客户数据所有者",
        "quality": "组织身份及联系责任明确"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "customer-mdm-model-default-related",
      "type": "traces_to",
      "source": "customer-mdm-model-default-person",
      "target": "customer-mdm-model-default-org",
      "label": "自然人可作为组织联系人；身份不自动合并",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-customer-mdm-model-default",
    "artifact_id": "customer-mdm-model",
    "profile_id": "customer-mdm-model-default",
    "title": "客户主数据模型／虚构案例",
    "entity_ids": [
      "customer-mdm-model-default-person",
      "customer-mdm-model-default-org"
    ],
    "relationship_ids": [
      "customer-mdm-model-default-related"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile customer-mdm-model-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile customer-mdm-model-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
