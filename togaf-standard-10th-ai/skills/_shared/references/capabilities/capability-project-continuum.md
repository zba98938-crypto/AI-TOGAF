# 能力与项目连续谱

ID：`capability-project-continuum`。主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G186/fig8-1。定义状态：`source-derived-view-with-project-construction-rules`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。



## 输入及缺口处理

必需：

- 视点问题与范围
- 带来源的对象、关系及定义

可选：

- 企业裁剪及例外说明

关键输入缺失时生成明确标记的草稿与缺口，不伪造批准或事实。

## 元素、属性与关系

对象类型：g186:continuum, g186:continuum_label。

```json
{
  "*": [
    "definition"
  ]
}
```

{
  "definition": {
    "meaning": "对象在本视点中的可检查定义",
    "value_rule": "使用可追溯描述；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 确认视点问题、范围和来源，区分参考结构与企业事实。
2. 用显式对象和类型化关系建模，核查边界、方向及完整性。
3. 生成视图与明细，记录取舍、缺口并复核来源及业务适用性。

## 输出、检查与误读

- 可编辑SVG/PNG概览
- 同ID的可读伴随明细与coverage表示位置

- 关系端点及类型有效
- 专用拓扑检查通过
- 必要字段可追溯到实际输出

- 登记来源或成功生成不表示来源等价
- 参考示例的固定结构不直接强制所有企业采用


## 视图和交付物

- [能力与项目连续谱](../profiles/capability-project-continuum.md)

- [architecture-vision](../deliverables/architecture-vision.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "从所选对象删除必需的definition属性，保留其稳定ID及视图选择。",
    "expected": "missing-profile-attribute",
    "why": "缺少对象含义，无法支持依据模型关系判断本视点的结构与范围；缺失输入保留为缺口。"
  },
  "modification_example": {
    "change": "修改同ID对象的definition，保持结构角色、类别和边界属性不变。",
    "expected": "reference与adaptive保存输出均表达新定义；覆盖位置指向该对象；不沿用旧版定义。"
  }
}
```

## 可编辑示例与调用



以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

```json
{
  "notice": "来源结构指导的解释性示例；项目事实为假设；不代表原图逐像素复刻、标准认证或架构批准。",
  "sources": [
    {
      "id": "example-source",
      "kind": "example",
      "description": "专用拓扑验收示例：G186/fig8-1；来源图解释与候选企业场景分开。"
    }
  ],
  "entities": [
    {
      "id": "continuum",
      "type": "g186:continuum",
      "name": "能力与项目连续谱",
      "attributes": {
        "definition": "0–10无单位；标签仅有阅读顺序，无精确分段值、时间或成熟度含义",
        "scale_min": 0,
        "scale_max": 10,
        "unit": "unitless"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "position-0",
      "type": "g186:continuum_label",
      "name": "维持：与他人持平",
      "attributes": {
        "definition": "维持：与他人持平",
        "order": 1
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "position-1",
      "type": "g186:continuum_label",
      "name": "维持：保持相同优势",
      "attributes": {
        "definition": "维持：保持相同优势",
        "order": 2
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "position-2",
      "type": "g186:continuum_label",
      "name": "改进：创造竞争优势",
      "attributes": {
        "definition": "改进：创造竞争优势",
        "order": 3
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "position-3",
      "type": "g186:continuum_label",
      "name": "改进：创造新收入流",
      "attributes": {
        "definition": "改进：创造新收入流",
        "order": 4
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "extensions": {
    "entity_types": {},
    "relationship_types": {}
  },
  "view": {
    "id": "v-capability-project-continuum",
    "artifact_id": "capability-project-continuum",
    "profile_id": "capability-project-continuum",
    "title": "能力与项目连续谱／来源结构专用示例",
    "entity_ids": [
      "continuum",
      "position-0",
      "position-1",
      "position-2",
      "position-3"
    ],
    "relationship_ids": [],
    "analysis": "明确来源结构、节点角色、流向与边界；未将相邻、颜色或布局当作企业事实。",
    "legend": "虚构候选或来源解释；相同ID表示同一对象。工程生成不授予来源等价或业务验收。"
  }
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact capability-project-continuum --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
