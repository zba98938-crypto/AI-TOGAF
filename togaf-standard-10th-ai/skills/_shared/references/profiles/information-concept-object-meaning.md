# 信息概念、业务对象与解释语境

`profile_id`: information-concept-object-meaning；`artifact_id`: information-map；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G190 §2、附录A.1。

## 构图与定义状态

表示族：`network`；输出：`diagram`。规范版本：2.2。

{
  "id": "information-concept-object-meaning",
  "version": "2.2",
  "source_verified": false,
  "layout_notes": "按已核查的来源结构参数化；参考图与业务实例的验收分别进行。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：information, business_object, information_meaning。关系类型：makes_explicit, is_about, interprets_information, interprets_information。

```json
{
  "entities": {
    "information": [
      "definition"
    ],
    "business_object": [
      "definition"
    ],
    "information_meaning": [
      "stakeholder",
      "context",
      "interpretation"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 对象、关系、必要属性均可追溯并得到表达
- 参考内容不自动成为项目事实；未知项保持显式

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构业务案例；采用来源结构及术语，不代表真实实施或批准。",
  "sources": [
    {
      "id": "case-source",
      "kind": "example",
      "description": "虚构社区服务机构的访谈、记录和项目约定"
    }
  ],
  "entities": [
    {
      "id": "customer-info",
      "type": "information",
      "name": "服务对象信息",
      "attributes": {
        "definition": "用于理解居民服务需求的信息概念"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "customer-record",
      "type": "business_object",
      "name": "服务对象记录",
      "attributes": {
        "definition": "把服务对象信息显性记录的业务对象类型"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "customer-person",
      "type": "business_object",
      "name": "服务对象",
      "attributes": {
        "definition": "接受社区服务的居民主体类型"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "meaning-ops",
      "type": "information_meaning",
      "name": "运营解释",
      "attributes": {
        "stakeholder": "服务运营",
        "context": "排班预约",
        "interpretation": "按实际到场的人识别服务对象"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "meaning-finance",
      "type": "information_meaning",
      "name": "财务解释",
      "attributes": {
        "stakeholder": "结算管理",
        "context": "补贴结算",
        "interpretation": "按资格申请主体识别，可能与实际到场者不同"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "record-explicit",
      "type": "makes_explicit",
      "source": "customer-record",
      "target": "customer-info",
      "label": "记录使服务对象信息显性化",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "info-about",
      "type": "is_about",
      "source": "customer-info",
      "target": "customer-person",
      "label": "信息关于服务对象",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "ops-meaning",
      "type": "interprets_information",
      "source": "meaning-ops",
      "target": "customer-info",
      "label": "运营解释：到场主体",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "finance-meaning",
      "type": "interprets_information",
      "source": "meaning-finance",
      "target": "customer-info",
      "label": "财务解释：申请主体",
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-information-concept-object-meaning",
    "artifact_id": "information-map",
    "profile_id": "information-concept-object-meaning",
    "title": "信息概念、业务对象与解释语境",
    "entity_ids": [
      "customer-info",
      "customer-record",
      "customer-person",
      "meaning-ops",
      "meaning-finance"
    ],
    "relationship_ids": [
      "record-explicit",
      "info-about",
      "ops-meaning",
      "finance-meaning"
    ],
    "analysis": "原料：预约以到场人为单位，补贴以申请主体为单位。归一为同一信息主题并保留两个利益相关者解释；记录、主体、信息不能合并成一个同名节点。",
    "legend": "同一ID表示同一对象；箭头依关系标签；未知不等于不存在；示例未获业务批准。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile information-concept-object-meaning --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile information-concept-object-meaning --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
