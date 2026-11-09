# 联网计算/硬件图（兼容默认）

`profile_id`: compat-networked-computing-hardware-diagram；`artifact_id`: networked-computing-hardware-diagram；主责：[togaf-technology-architecture](../../../togaf-technology-architecture/SKILL.md)。

来源：G248；G248；G242。

## 构图与定义状态

表示族：`deployment`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-networked-computing-hardware-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：hardware, network_zone, location。关系类型：hardware_connects, member_of_zone, located_at。

```json
{
  "entities": {
    "hardware": [
      "capacity",
      "redundancy",
      "owner"
    ],
    "network_zone": [],
    "location": []
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 冗余图形不能替代故障域证据
- 不要混用逻辑服务与硬件实例

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
      "id": "hardware-app",
      "type": "hardware",
      "name": "示例计算节点",
      "attributes": {
        "capacity": "待压测确认",
        "redundancy": "双节点计划",
        "owner": "平台负责人"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "hardware-storage",
      "type": "hardware",
      "name": "示例存储节点",
      "attributes": {
        "capacity": "待容量评估",
        "redundancy": "双副本计划",
        "owner": "平台负责人"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "hardware-link",
      "type": "hardware_connects",
      "source": "hardware-app",
      "target": "hardware-storage",
      "label": "存储访问连接",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "hardware-zone",
      "type": "member_of_zone",
      "source": "hardware-app",
      "target": "network-app",
      "label": "计算节点属于应用区",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "hardware-loc",
      "type": "located_at",
      "source": "hardware-app",
      "target": "loc-cloud",
      "label": "节点位于区域 A",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-networked-computing-hardware-diagram",
    "artifact_id": "networked-computing-hardware-diagram",
    "title": "联网计算/硬件图 · 星河零售虚构案例",
    "context": {
      "domains": [
        "business",
        "data",
        "application",
        "technology"
      ],
      "landscape": "segment",
      "purpose": "project",
      "abstraction": "physical",
      "evolution": "target"
    },
    "entity_ids": [
      "hardware-app",
      "hardware-storage",
      "network-app",
      "loc-cloud"
    ],
    "relationship_ids": [
      "hardware-link",
      "hardware-zone",
      "hardware-loc"
    ],
    "analysis": "哪些计算、存储和网络硬件构成运行拓扑？ 本视图限定订单履约改造范围，展示案例设定的联网计算/硬件图。识别节点角色及物理边界；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-networked-computing-hardware-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-networked-computing-hardware-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-networked-computing-hardware-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
