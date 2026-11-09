# 数字业务参考模型裁剪

`profile_id`: digital-business-reference-tailoring-default；`artifact_id`: digital-business-reference-tailoring；主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G21H §1.1–1.2。

## 构图与定义状态

表示族：`nested-map`；输出：`diagram`。规范版本：2.0。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：dbrm_domain, dbrm_element。关系类型：contains。

```json
{
  "entities": {
    "dbrm_domain": [
      "definition"
    ],
    "dbrm_element": [
      "definition",
      "local_mapping",
      "applicability"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 参考模型裁剪不表示全量采用，也不等于最终技术架构
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
      "id": "digital-business-reference-tailoring-default-domain0",
      "type": "dbrm_domain",
      "name": "数字域",
      "attributes": {
        "definition": "DBRM参考域；不是TOGAF业务数据应用技术域",
        "category": "数字"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-element00",
      "type": "dbrm_element",
      "name": "客户聚焦",
      "attributes": {
        "definition": "DBRM十核心要素之一：客户聚焦",
        "local_mapping": "本例在线履约需补充客户聚焦的业务证据",
        "applicability": "候选适用，需裁剪责任人验证",
        "category": "数字",
        "parent_id": "digital-business-reference-tailoring-default-domain0"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-element01",
      "type": "dbrm_element",
      "name": "数字企业",
      "attributes": {
        "definition": "DBRM十核心要素之一：数字企业",
        "local_mapping": "本例在线履约需补充数字企业的业务证据",
        "applicability": "候选适用，需裁剪责任人验证",
        "category": "数字",
        "parent_id": "digital-business-reference-tailoring-default-domain0"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-domain1",
      "type": "dbrm_domain",
      "name": "战略域",
      "attributes": {
        "definition": "DBRM参考域；不是TOGAF业务数据应用技术域",
        "category": "战略"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-element10",
      "type": "dbrm_element",
      "name": "战略语境",
      "attributes": {
        "definition": "DBRM十核心要素之一：战略语境",
        "local_mapping": "本例在线履约需补充战略语境的业务证据",
        "applicability": "候选适用，需裁剪责任人验证",
        "category": "战略",
        "parent_id": "digital-business-reference-tailoring-default-domain1"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-element11",
      "type": "dbrm_element",
      "name": "业务动机",
      "attributes": {
        "definition": "DBRM十核心要素之一：业务动机",
        "local_mapping": "本例在线履约需补充业务动机的业务证据",
        "applicability": "候选适用，需裁剪责任人验证",
        "category": "战略",
        "parent_id": "digital-business-reference-tailoring-default-domain1"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-element12",
      "type": "dbrm_element",
      "name": "业务服务与产品",
      "attributes": {
        "definition": "DBRM十核心要素之一：业务服务与产品",
        "local_mapping": "本例在线履约需补充业务服务与产品的业务证据",
        "applicability": "候选适用，需裁剪责任人验证",
        "category": "战略",
        "parent_id": "digital-business-reference-tailoring-default-domain1"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-domain2",
      "type": "dbrm_domain",
      "name": "结构域",
      "attributes": {
        "definition": "DBRM参考域；不是TOGAF业务数据应用技术域",
        "category": "结构"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-element20",
      "type": "dbrm_element",
      "name": "生态与业务模型",
      "attributes": {
        "definition": "DBRM十核心要素之一：生态与业务模型",
        "local_mapping": "本例在线履约需补充生态与业务模型的业务证据",
        "applicability": "候选适用，需裁剪责任人验证",
        "category": "结构",
        "parent_id": "digital-business-reference-tailoring-default-domain2"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-element21",
      "type": "dbrm_element",
      "name": "运营模式",
      "attributes": {
        "definition": "DBRM十核心要素之一：运营模式",
        "local_mapping": "本例在线履约需补充运营模式的业务证据",
        "applicability": "候选适用，需裁剪责任人验证",
        "category": "结构",
        "parent_id": "digital-business-reference-tailoring-default-domain2"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-element22",
      "type": "dbrm_element",
      "name": "业务能力模型",
      "attributes": {
        "definition": "DBRM十核心要素之一：业务能力模型",
        "local_mapping": "本例在线履约需补充业务能力模型的业务证据",
        "applicability": "候选适用，需裁剪责任人验证",
        "category": "结构",
        "parent_id": "digital-business-reference-tailoring-default-domain2"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-domain3",
      "type": "dbrm_domain",
      "name": "运营域",
      "attributes": {
        "definition": "DBRM参考域；不是TOGAF业务数据应用技术域",
        "category": "运营"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-element30",
      "type": "dbrm_element",
      "name": "业务运营环境",
      "attributes": {
        "definition": "DBRM十核心要素之一：业务运营环境",
        "local_mapping": "本例在线履约需补充业务运营环境的业务证据",
        "applicability": "候选适用，需裁剪责任人验证",
        "category": "运营",
        "parent_id": "digital-business-reference-tailoring-default-domain3"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-element31",
      "type": "dbrm_element",
      "name": "数字使能",
      "attributes": {
        "definition": "DBRM十核心要素之一：数字使能",
        "local_mapping": "本例在线履约需补充数字使能的业务证据",
        "applicability": "候选适用，需裁剪责任人验证",
        "category": "运营",
        "parent_id": "digital-business-reference-tailoring-default-domain3"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "digital-business-reference-tailoring-default-contains00",
      "type": "contains",
      "source": "digital-business-reference-tailoring-default-domain0",
      "target": "digital-business-reference-tailoring-default-element00",
      "label": "DBRM域含核心要素；是参考结构，不是本地业务事实",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-contains01",
      "type": "contains",
      "source": "digital-business-reference-tailoring-default-domain0",
      "target": "digital-business-reference-tailoring-default-element01",
      "label": "DBRM域含核心要素；是参考结构，不是本地业务事实",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-contains10",
      "type": "contains",
      "source": "digital-business-reference-tailoring-default-domain1",
      "target": "digital-business-reference-tailoring-default-element10",
      "label": "DBRM域含核心要素；是参考结构，不是本地业务事实",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-contains11",
      "type": "contains",
      "source": "digital-business-reference-tailoring-default-domain1",
      "target": "digital-business-reference-tailoring-default-element11",
      "label": "DBRM域含核心要素；是参考结构，不是本地业务事实",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-contains12",
      "type": "contains",
      "source": "digital-business-reference-tailoring-default-domain1",
      "target": "digital-business-reference-tailoring-default-element12",
      "label": "DBRM域含核心要素；是参考结构，不是本地业务事实",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-contains20",
      "type": "contains",
      "source": "digital-business-reference-tailoring-default-domain2",
      "target": "digital-business-reference-tailoring-default-element20",
      "label": "DBRM域含核心要素；是参考结构，不是本地业务事实",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-contains21",
      "type": "contains",
      "source": "digital-business-reference-tailoring-default-domain2",
      "target": "digital-business-reference-tailoring-default-element21",
      "label": "DBRM域含核心要素；是参考结构，不是本地业务事实",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-contains22",
      "type": "contains",
      "source": "digital-business-reference-tailoring-default-domain2",
      "target": "digital-business-reference-tailoring-default-element22",
      "label": "DBRM域含核心要素；是参考结构，不是本地业务事实",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-contains30",
      "type": "contains",
      "source": "digital-business-reference-tailoring-default-domain3",
      "target": "digital-business-reference-tailoring-default-element30",
      "label": "DBRM域含核心要素；是参考结构，不是本地业务事实",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "digital-business-reference-tailoring-default-contains31",
      "type": "contains",
      "source": "digital-business-reference-tailoring-default-domain3",
      "target": "digital-business-reference-tailoring-default-element31",
      "label": "DBRM域含核心要素；是参考结构，不是本地业务事实",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-digital-business-reference-tailoring-default",
    "artifact_id": "digital-business-reference-tailoring",
    "profile_id": "digital-business-reference-tailoring-default",
    "title": "数字业务参考模型裁剪／虚构案例",
    "entity_ids": [
      "digital-business-reference-tailoring-default-domain0",
      "digital-business-reference-tailoring-default-element00",
      "digital-business-reference-tailoring-default-element01",
      "digital-business-reference-tailoring-default-domain1",
      "digital-business-reference-tailoring-default-element10",
      "digital-business-reference-tailoring-default-element11",
      "digital-business-reference-tailoring-default-element12",
      "digital-business-reference-tailoring-default-domain2",
      "digital-business-reference-tailoring-default-element20",
      "digital-business-reference-tailoring-default-element21",
      "digital-business-reference-tailoring-default-element22",
      "digital-business-reference-tailoring-default-domain3",
      "digital-business-reference-tailoring-default-element30",
      "digital-business-reference-tailoring-default-element31"
    ],
    "relationship_ids": [
      "digital-business-reference-tailoring-default-contains00",
      "digital-business-reference-tailoring-default-contains01",
      "digital-business-reference-tailoring-default-contains10",
      "digital-business-reference-tailoring-default-contains11",
      "digital-business-reference-tailoring-default-contains12",
      "digital-business-reference-tailoring-default-contains20",
      "digital-business-reference-tailoring-default-contains21",
      "digital-business-reference-tailoring-default-contains22",
      "digital-business-reference-tailoring-default-contains30",
      "digital-business-reference-tailoring-default-contains31"
    ],
    "analysis": "依据本例目的选择对象与显式关系，结论仅用于演示方法和生成；实际责任人、度量及证据仍需核实。",
    "legend": "虚构示例／候选；相同ID表示复用。箭头按关系类型读，不从颜色或相邻推断事实。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile digital-business-reference-tailoring-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile digital-business-reference-tailoring-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
