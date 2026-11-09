# 软件分布图（兼容默认）

`profile_id`: compat-software-distribution-diagram；`artifact_id`: software-distribution-diagram；主责：[togaf-application-architecture](../../../togaf-application-architecture/SKILL.md)。

来源：G248；G248；G21I。

## 构图与定义状态

表示族：`deployment`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-software-distribution-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：software_module, technology, location。关系类型：deployed_on, located_at, located_at。

```json
{
  "entities": {
    "software_module": [
      "version",
      "runtime"
    ],
    "technology": [
      "version"
    ],
    "location": []
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 软件仓库位置不是运行部署位置
- 部署关系不是模块依赖

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
      "id": "module-order",
      "type": "software_module",
      "name": "订单服务模块",
      "attributes": {
        "responsibility": "实现订单确认",
        "version": "候选 v1",
        "runtime": "应用运行节点"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "loc-tech",
      "type": "located_at",
      "source": "tech-platform",
      "target": "loc-cloud",
      "label": "运行节点位于云区域",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "module-deploy",
      "type": "deployed_on",
      "source": "module-order",
      "target": "tech-platform",
      "label": "候选部署",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-software-distribution-diagram",
    "artifact_id": "software-distribution-diagram",
    "title": "软件分布图 · 星河零售虚构案例",
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
      "module-order",
      "tech-platform",
      "loc-cloud"
    ],
    "relationship_ids": [
      "module-deploy",
      "loc-tech"
    ],
    "analysis": "软件模块和版本如何分布到运行节点？ 本视图限定订单履约改造范围，展示案例设定的软件分布图。区分软件制品和运行节点；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-software-distribution-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-software-distribution-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-software-distribution-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
