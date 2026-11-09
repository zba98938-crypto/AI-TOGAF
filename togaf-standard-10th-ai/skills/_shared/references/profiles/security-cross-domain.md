# 跨域安全关注点

`profile_id`: security-cross-domain；`artifact_id`: security-blueprint；主责：[togaf-security-risk](../../../togaf-security-risk/SKILL.md)。

来源：G152/fig4-1。

## 构图与定义状态

表示族：`deployment`；输出：`diagram`。规范版本：2.3。

{
  "source_verified": false,
  "source_figure": "G152/fig4-1",
  "layout_notes": "风险与安全横贯业务数据应用技术，不作为第五个互斥架构域",
  "review_status": "source-topology-repaired-awaiting-independent-review",
  "source_topology": "security-crosscut",
  "version": "2.3"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:architecture_domain, security_component。关系类型：project:cross_cuts。

```json
{
  "entities": {
    "*": [
      "definition"
    ]
  },
  "relationships": {
    "*": [
      "meaning"
    ]
  }
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 风险与安全横贯业务数据应用技术，不作为第五个互斥架构域

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "来源结构指导的解释性示例；项目事实为假设；不代表原图逐像素复刻、标准认证或架构批准。",
  "sources": [
    {
      "id": "example-source",
      "kind": "example",
      "description": "专用拓扑验收示例：G152/fig4-1；来源图解释与候选企业场景分开。"
    }
  ],
  "entities": [
    {
      "id": "security-concern",
      "type": "security_component",
      "name": "安全、隐私与运营风险",
      "attributes": {
        "definition": "同一组跨域安全关注点",
        "concern": "授权、机密性、完整性、可用性",
        "principle": "最小权限与可追溯职责",
        "risk": "未授权操作与履约中断",
        "scope": "业务、数据、应用和技术"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "domain-business",
      "type": "guide:architecture_domain",
      "name": "业务域",
      "attributes": {
        "definition": "交易职责与履约规则",
        "architecture_domain": "business"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "domain-data",
      "type": "guide:architecture_domain",
      "name": "数据域",
      "attributes": {
        "definition": "客户、订单及生产数据",
        "architecture_domain": "data"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "domain-application",
      "type": "guide:architecture_domain",
      "name": "应用域",
      "attributes": {
        "definition": "应用与接口实现",
        "architecture_domain": "application"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "domain-technology",
      "type": "guide:architecture_domain",
      "name": "技术域",
      "attributes": {
        "definition": "运行平台与基础设施",
        "architecture_domain": "technology"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "cross-business",
      "source": "security-concern",
      "target": "domain-business",
      "type": "project:cross_cuts",
      "label": "职责分离与授权审批",
      "attributes": {
        "domain": "business",
        "meaning": "职责分离与授权审批"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cross-data",
      "source": "security-concern",
      "target": "domain-data",
      "type": "project:cross_cuts",
      "label": "分类、保留与用途限制",
      "attributes": {
        "domain": "data",
        "meaning": "分类、保留与用途限制"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cross-application",
      "source": "security-concern",
      "target": "domain-application",
      "type": "project:cross_cuts",
      "label": "身份、访问控制与审计",
      "attributes": {
        "domain": "application",
        "meaning": "身份、访问控制与审计"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cross-technology",
      "source": "security-concern",
      "target": "domain-technology",
      "type": "project:cross_cuts",
      "label": "网络隔离、恢复与监控",
      "attributes": {
        "domain": "technology",
        "meaning": "网络隔离、恢复与监控"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "extensions": {
    "entity_types": {
      "guide:architecture_domain": "指南中的架构域类别，不是企业组织或部署容器"
    },
    "relationship_types": {
      "project:cross_cuts": {
        "source_types": [
          "security_component"
        ],
        "target_types": [
          "guide:architecture_domain"
        ],
        "meaning": "关注点横切指定架构域；覆盖关系，不表示流程、包含或数据流。"
      }
    }
  },
  "view": {
    "id": "v-security-cross-domain",
    "artifact_id": "security-blueprint",
    "profile_id": "security-cross-domain",
    "title": "跨域安全关注点／来源结构专用示例",
    "entity_ids": [
      "security-concern",
      "domain-business",
      "domain-data",
      "domain-application",
      "domain-technology"
    ],
    "relationship_ids": [
      "cross-business",
      "cross-data",
      "cross-application",
      "cross-technology"
    ],
    "analysis": "明确来源结构、节点角色、流向与边界；未将相邻、颜色或布局当作企业事实。",
    "legend": "虚构候选或来源解释；相同ID表示同一对象。按专用线型、区域与编号语义读取；工程生成不授予来源等价或业务验收。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile security-cross-domain --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile security-cross-domain --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
