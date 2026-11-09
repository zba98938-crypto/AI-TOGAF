# 企业可管理性图（兼容默认）

`profile_id`: compat-enterprise-manageability-diagram；`artifact_id`: enterprise-manageability-diagram；主责：[togaf-technology-architecture](../../../togaf-technology-architecture/SKILL.md)。

来源：G248；G248；G184；G152。

## 构图与定义状态

表示族：`network`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-enterprise-manageability-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：technology, management_service, measure。关系类型：managed_by, measured_by。

```json
{
  "entities": {
    "technology": [
      "owner"
    ],
    "management_service": [
      "owner",
      "service_level",
      "recovery"
    ],
    "measure": [
      "owner"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 工具部署不等于形成运营能力
- 可用性指标需要观测窗口

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
      "id": "metric",
      "type": "measure",
      "name": "库存确认成功率",
      "attributes": {
        "owner": "履约负责人",
        "target": 99.5,
        "unit": "%",
        "measurement_window": "每周",
        "formula": "正确确认数 / 总确认数"
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
      "id": "management",
      "type": "management_service",
      "name": "监控和恢复服务",
      "attributes": {
        "owner": "运维负责人",
        "service_level": "试运行前约定",
        "recovery": "恢复目标由业务确认"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "tech-managed",
      "type": "managed_by",
      "source": "tech-platform",
      "target": "management",
      "label": "监控告警与恢复",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "tech-measured",
      "type": "measured_by",
      "source": "tech-platform",
      "target": "metric",
      "label": "监测业务确认成功率",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-enterprise-manageability-diagram",
    "artifact_id": "enterprise-manageability-diagram",
    "title": "企业可管理性图 · 星河零售虚构案例",
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
      "management",
      "metric"
    ],
    "relationship_ids": [
      "tech-managed",
      "tech-measured"
    ],
    "analysis": "如何监测、运维和恢复跨域运行服务？ 本视图限定订单履约改造范围，展示案例设定的企业可管理性图。识别监控、配置、告警和恢复服务；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-enterprise-manageability-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-enterprise-manageability-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-enterprise-manageability-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
