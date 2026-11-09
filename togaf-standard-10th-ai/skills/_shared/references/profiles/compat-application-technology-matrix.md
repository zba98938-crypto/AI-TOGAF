# 应用/技术矩阵（兼容默认）

`profile_id`: compat-application-technology-matrix；`artifact_id`: application-technology-matrix；主责：[togaf-technology-architecture](../../../togaf-technology-architecture/SKILL.md)。

来源：G248；G248；G242。

## 构图与定义状态

表示族：`matrix`；输出：`table`。规范版本：2.1。

{
  "id": "compat-application-technology-matrix",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：application, technology。关系类型：runs_on。

```json
{
  "entities": {
    "application": [],
    "technology": []
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 应用依赖技术不一定直接部署其上
- 逻辑和物理层不可无标记混用

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
      "id": "app-oms",
      "type": "application",
      "name": "目标订单应用",
      "attributes": {
        "owner": "应用负责人",
        "lifecycle": "候选目标",
        "criticality": "业务关键",
        "cost": "待估算",
        "jurisdiction": "示例境内",
        "automation": "辅助业务确认",
        "capacity": 250,
        "responsibility": "支持客户购买与订单履约",
        "boundary": "订单履约系统边界",
        "version": "候选或现状示例版本"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed",
      "concept_id": "order-management-system",
      "evolution": "target"
    },
    {
      "id": "app-old",
      "type": "application",
      "name": "现有订单应用",
      "attributes": {
        "owner": "应用负责人",
        "lifecycle": "现状在用",
        "criticality": "业务关键",
        "cost": "待估算",
        "jurisdiction": "示例境内",
        "automation": "辅助业务确认",
        "capacity": 100,
        "responsibility": "支持客户购买与订单履约",
        "boundary": "订单履约系统边界",
        "version": "候选或现状示例版本"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed",
      "concept_id": "order-management-system",
      "evolution": "baseline"
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
      "id": "tech-old",
      "type": "technology",
      "name": "现有单节点平台",
      "attributes": {
        "product": "示例通用平台产品",
        "version": "候选版本",
        "owner": "平台负责人",
        "lifecycle": "现状在用",
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
      "certainty": "assumed",
      "evolution": "baseline"
    }
  ],
  "relationships": [
    {
      "id": "app-tech",
      "type": "runs_on",
      "source": "app-oms",
      "target": "tech-platform",
      "label": "部署于目标运行节点",
      "evidence": [
        "case"
      ],
      "certainty": "assumed",
      "codes": [
        "runs_on"
      ]
    },
    {
      "id": "old-tech",
      "type": "runs_on",
      "source": "app-old",
      "target": "tech-old",
      "label": "现有应用在单节点上运行",
      "evidence": [
        "case"
      ],
      "certainty": "assumed",
      "codes": [
        "runs_on"
      ]
    }
  ],
  "view": {
    "id": "v-application-technology-matrix",
    "artifact_id": "application-technology-matrix",
    "title": "应用/技术矩阵 · 星河零售虚构案例",
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
      "app-oms",
      "tech-platform",
      "app-old",
      "tech-old"
    ],
    "relationship_ids": [
      "app-tech",
      "old-tech"
    ],
    "analysis": "哪些技术组件承载哪些应用？ 本视图限定订单履约改造范围，展示案例设定的应用/技术矩阵。确认应用运行边界；实际项目需由相关责任方核实。",
    "legend": "区分应用部署依赖与一般技术依赖；单元代码：runs_on,depends_on；未记录不等于不存在。",
    "allow_mixed_evolution": true,
    "profile_id": "compat-application-technology-matrix"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-application-technology-matrix --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-application-technology-matrix --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
