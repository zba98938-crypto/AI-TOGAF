# 业务足迹图（兼容默认）

`profile_id`: compat-business-footprint-diagram；`artifact_id`: business-footprint-diagram；主责：[togaf-strategy-capabilities](../../../togaf-strategy-capabilities/SKILL.md)。

来源：G248；G186；G211；G206。

## 构图与定义状态

表示族：`network`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-business-footprint-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：goal, capability, organization, function。关系类型：requires_capability, owned_by, supports_capability。

```json
{
  "entities": {
    "goal": [],
    "capability": [
      "definition"
    ],
    "organization": [],
    "function": [
      "definition"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 业务足迹不是地理分布
- 跨层关系使用标签不能靠上下位置猜测

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
      "id": "cap-order",
      "type": "capability",
      "name": "订单管理",
      "attributes": {
        "definition": "维护订单承诺及履行状态",
        "owner": "销售负责人",
        "level": 2,
        "category": "核心能力",
        "score": "待真实评估"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cap-stock",
      "type": "capability",
      "name": "库存管理",
      "attributes": {
        "definition": "掌握库存并分配可售数量",
        "owner": "仓储负责人",
        "level": 2,
        "category": "核心能力",
        "score": "待真实评估"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "fn-order",
      "type": "function",
      "name": "订单处理",
      "attributes": {
        "definition": "记录、校验并确认订单",
        "owner": "销售负责人",
        "service_level": "由订单确认服务承诺约束",
        "level": 1
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "goal",
      "type": "goal",
      "name": "改善客户履约体验",
      "attributes": {
        "statement": "客户获得可靠及时的交付",
        "owner": "业务发起方",
        "metric": "按承诺送达比例",
        "target": "提升",
        "deadline": "下一季度"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "org-warehouse",
      "type": "organization",
      "name": "仓储团队",
      "attributes": {
        "category": "业务单元",
        "owner": "仓储负责人",
        "boundary": "内部"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "cap-org",
      "type": "owned_by",
      "source": "cap-stock",
      "target": "org-warehouse",
      "label": "负责库存能力",
      "evidence": [
        "case"
      ],
      "certainty": "assumed",
      "codes": [
        "owner"
      ]
    },
    {
      "id": "strategy-cap",
      "type": "requires_capability",
      "source": "goal",
      "target": "cap-order",
      "label": "体验目标需订单管理",
      "evidence": [
        "case"
      ],
      "certainty": "assumed",
      "codes": [
        "supports"
      ]
    },
    {
      "id": "fn-cap",
      "type": "supports_capability",
      "source": "fn-order",
      "target": "cap-order",
      "label": "订单处理支撑能力",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-business-footprint-diagram",
    "artifact_id": "business-footprint-diagram",
    "title": "业务足迹图 · 星河零售虚构案例",
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
      "goal",
      "cap-order",
      "fn-order",
      "cap-stock",
      "org-warehouse"
    ],
    "relationship_ids": [
      "strategy-cap",
      "fn-cap",
      "cap-org"
    ],
    "analysis": "目标、能力、组织和业务功能如何形成业务足迹？ 本视图限定订单履约改造范围，展示案例设定的业务足迹图。从目标识别关键能力；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-business-footprint-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-business-footprint-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-business-footprint-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
