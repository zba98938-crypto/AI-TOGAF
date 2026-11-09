# 网络与通信图（兼容默认）

`profile_id`: compat-network-and-communications-diagram；`artifact_id`: network-and-communications-diagram；主责：[togaf-technology-architecture](../../../togaf-technology-architecture/SKILL.md)。

来源：G248；G152；G248。

## 构图与定义状态

表示族：`deployment`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-network-and-communications-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：network_zone, technology。关系类型：network_connects, member_of_zone。

```json
{
  "entities": {
    "network_zone": [
      "protocol",
      "ports",
      "trust"
    ],
    "technology": [
      "protocol",
      "ports",
      "trust"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 物理相邻不代表可通信
- 网络边与应用调用分别建模

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
      "id": "tech-platform",
      "type": "technology",
      "name": "应用运行节点",
      "attributes": {
        "product": "示例通用平台产品",
        "version": "候选版本",
        "owner": "平台负责人",
        "lifecycle": "候选",
        "support_end": "待厂商确认",
        "capacity": "待压测",
        "redundancy": "跨两个示例故障域",
        "protocol": "TLS",
        "ports": "443",
        "trust": "业务服务区",
        "responsibility": "承载运行服务",
        "standard": "受支持运行时"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "network-app",
      "type": "network_zone",
      "name": "应用网络区",
      "attributes": {
        "protocol": "HTTPS",
        "ports": "443",
        "trust": "内部业务区"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "network-data",
      "type": "network_zone",
      "name": "数据网络区",
      "attributes": {
        "protocol": "受控数据库连接",
        "ports": "示例专用端口",
        "trust": "受限区"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "network",
      "type": "network_connects",
      "source": "network-app",
      "target": "network-data",
      "label": "仅允许服务访问数据端口",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "network-member",
      "type": "member_of_zone",
      "source": "tech-platform",
      "target": "network-app",
      "label": "节点位于应用区",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-network-and-communications-diagram",
    "artifact_id": "network-and-communications-diagram",
    "title": "网络与通信图 · 星河零售虚构案例",
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
      "network-app",
      "network-data",
      "tech-platform"
    ],
    "relationship_ids": [
      "network",
      "network-member"
    ],
    "analysis": "哪些网络区域通过什么通信规则连接？ 本视图限定订单履约改造范围，展示案例设定的网络与通信图。定义信任与网络边界；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-network-and-communications-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-network-and-communications-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-network-and-communications-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
