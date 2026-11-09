# 位置目录（兼容默认）

`profile_id`: compat-location-catalog；`artifact_id`: location-catalog；主责：[togaf-technology-architecture](../../../togaf-technology-architecture/SKILL.md)。

来源：G248；G248。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1。

{
  "id": "compat-location-catalog",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：location, environment。关系类型：located_at。

```json
{
  "entities": {
    "location": [
      "category",
      "jurisdiction",
      "availability_zone"
    ],
    "environment": [
      "category",
      "jurisdiction",
      "availability_zone"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 环境不等于地理地点
- 云区域与可用区分别记录

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构兼容案例；不是正式定义或来源图复刻。",
  "sources": [
    {
      "id": "case",
      "kind": "example",
      "description": "全量验收使用的虚构业务情景；数字、主体和架构均非真实项目事实。"
    },
    {
      "id": "assumption",
      "kind": "assumption",
      "description": "方案和收益因果假设，需在真实项目中验证。"
    }
  ],
  "entities": [
    {
      "id": "loc-east",
      "type": "location",
      "name": "东区配送中心",
      "attributes": {
        "category": "业务站点",
        "jurisdiction": "示例东区",
        "availability_zone": "不适用：业务地点"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "loc-cloud",
      "type": "location",
      "name": "示例云区域 A",
      "attributes": {
        "category": "云区域",
        "jurisdiction": "示例境内区域",
        "availability_zone": "A1/A2"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "env-prod",
      "type": "environment",
      "name": "生产环境",
      "attributes": {
        "category": "production",
        "jurisdiction": "示例境内",
        "availability_zone": "A1/A2"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "loc-prod",
      "type": "located_at",
      "source": "env-prod",
      "target": "loc-cloud",
      "label": "生产环境位于云区域",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-location-catalog",
    "artifact_id": "location-catalog",
    "title": "位置目录 · 星河零售虚构案例",
    "context": {
      "domains": [
        "business",
        "data",
        "application",
        "technology"
      ],
      "landscape": "segment",
      "purpose": "project",
      "abstraction": "logical",
      "evolution": "target"
    },
    "entity_ids": [
      "loc-east",
      "loc-cloud",
      "env-prod"
    ],
    "relationship_ids": [
      "loc-prod"
    ],
    "analysis": "哪些地点及运行环境承载业务、用户和设施？ 本视图限定订单履约改造范围，展示案例设定的位置目录。区分地点、逻辑环境和网络区域；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-location-catalog"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-location-catalog --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-location-catalog --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
