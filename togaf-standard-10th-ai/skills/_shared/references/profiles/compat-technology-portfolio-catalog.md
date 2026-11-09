# 技术组合目录（兼容默认）

`profile_id`: compat-technology-portfolio-catalog；`artifact_id`: technology-portfolio-catalog；主责：[togaf-technology-architecture](../../../togaf-technology-architecture/SKILL.md)。

来源：G248；G248；G242。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1。

{
  "id": "compat-technology-portfolio-catalog",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：technology。关系类型：implements_standard。

```json
{
  "entities": {
    "technology": [
      "product",
      "version",
      "owner",
      "lifecycle",
      "support_end"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 厂商产品不能代替技术能力需求
- 停止支持日期应有证据

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
      "id": "tech-db",
      "type": "technology",
      "name": "数据服务节点",
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
        "responsibility": "提供受控数据存储",
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
  "relationships": [],
  "view": {
    "id": "v-technology-portfolio-catalog",
    "artifact_id": "technology-portfolio-catalog",
    "title": "技术组合目录 · 星河零售虚构案例",
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
      "tech-platform",
      "tech-db",
      "tech-old"
    ],
    "relationship_ids": [],
    "analysis": "哪些技术组件在用或候选，处于何种支持周期？ 本视图限定订单履约改造范围，展示案例设定的技术组合目录。区分技术服务、逻辑类别与产品实例；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": true,
    "profile_id": "compat-technology-portfolio-catalog"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-technology-portfolio-catalog --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-technology-portfolio-catalog --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
