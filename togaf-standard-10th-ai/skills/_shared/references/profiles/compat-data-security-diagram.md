# 数据安全图（兼容默认）

`profile_id`: compat-data-security-diagram；`artifact_id`: data-security-diagram；主责：[togaf-security-risk](../../../togaf-security-risk/SKILL.md)。

来源：G248；G152；G234。

## 构图与定义状态

表示族：`deployment`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-data-security-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：data_entity, data_component, actor, control, trust_zone。关系类型：stored_in, protected_by, authorized_for, crosses_boundary。

```json
{
  "entities": {
    "data_entity": [
      "classification",
      "owner",
      "purpose"
    ],
    "data_component": [
      "classification",
      "owner",
      "purpose"
    ],
    "actor": [
      "owner"
    ],
    "control": [
      "classification",
      "owner",
      "purpose"
    ],
    "trust_zone": [
      "classification",
      "owner",
      "purpose"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 画锁图标不构成控制设计
- 角色使用关系不自动表示授权

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
      "id": "actor-picker",
      "type": "actor",
      "name": "仓储操作员",
      "attributes": {
        "category": "内部参与者",
        "owner": "仓储负责人",
        "boundary": "内部",
        "jurisdiction": "示例境内"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "control",
      "type": "control",
      "name": "最小权限与审计控制",
      "attributes": {
        "definition": "按角色和目的限制数据并记录访问",
        "owner": "安全负责人",
        "lifecycle": "目标设计",
        "classification": "客户联系信息",
        "purpose": "订单履约"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "data-customer",
      "type": "data_entity",
      "name": "客户",
      "attributes": {
        "definition": "可识别的购买主体数据",
        "owner": "客户数据负责人",
        "classification": "受限联系信息",
        "retention": "示例：合同完成后按已确认政策处置",
        "authority": "客户主数据服务",
        "latency": "待确认",
        "delivery_mode": "受控查询",
        "purpose": "受控订单履约或已声明分析"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "component-order",
      "type": "data_component",
      "name": "订单主存储",
      "attributes": {
        "definition": "订单逻辑存储组件",
        "owner": "应用负责人",
        "classification": "内部交易数据",
        "retention": "继承订单政策",
        "authority": "订单应用",
        "latency": "事务提交",
        "delivery_mode": "受控查询",
        "purpose": "受控订单履约或已声明分析"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "trust",
      "type": "trust_zone",
      "name": "受控数据域",
      "attributes": {
        "classification": "受限",
        "owner": "安全负责人",
        "purpose": "受控处理客户数据"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "data-protect",
      "type": "protected_by",
      "source": "data-customer",
      "target": "control",
      "label": "限制和审计客户信息访问",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "data-authorize",
      "type": "authorized_for",
      "source": "actor-picker",
      "target": "data-customer",
      "label": "仅示例：按履约目的读取必要字段",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "data-boundary",
      "type": "crosses_boundary",
      "source": "component-order",
      "target": "trust",
      "label": "数据跨受控边界需验证",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-data-security-diagram",
    "artifact_id": "data-security-diagram",
    "title": "数据安全图 · 星河零售虚构案例",
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
      "data-customer",
      "control",
      "actor-picker",
      "component-order",
      "trust"
    ],
    "relationship_ids": [
      "data-protect",
      "data-authorize",
      "data-boundary"
    ],
    "analysis": "拣货角色仅为履约目的读取必要联系信息；控制需要覆盖允许和拒绝路径及审计，示例并未证明控制有效。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-data-security-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-data-security-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-data-security-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
