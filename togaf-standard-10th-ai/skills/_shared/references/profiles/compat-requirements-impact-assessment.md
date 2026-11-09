# 需求影响评估（兼容默认）

`profile_id`: compat-requirements-impact-assessment；`artifact_id`: requirements-impact-assessment；主责：[togaf-requirements](../../../togaf-requirements/SKILL.md)。

来源：G248；G186；G152；G188。

## 构图与定义状态

表示族：`assessment`；输出：`table`。规范版本：2.1。

{
  "id": "compat-requirements-impact-assessment",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：requirement, change_request, risk, work_package。关系类型：changes, traces_to, affects。

```json
{
  "entities": {
    "requirement": [
      "owner"
    ],
    "change_request": [
      "reason",
      "impact",
      "severity",
      "owner",
      "decision"
    ],
    "risk": [
      "impact",
      "owner"
    ],
    "work_package": [
      "owner"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 可达性不自动等于实际影响
- 影响分析不自动批准变更

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
      "id": "req-accuracy",
      "type": "requirement",
      "name": "订单库存一致性",
      "attributes": {
        "statement": "确认订单前校验可售库存并记录处理结果",
        "priority": "must",
        "owner": "履约负责人",
        "acceptance": "用并发场景验证无超量确认且失败可恢复"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "req-privacy",
      "type": "requirement",
      "name": "客户信息最小访问",
      "attributes": {
        "statement": "仅授权角色可按业务目的读取客户联系信息",
        "priority": "must",
        "owner": "客户数据负责人",
        "acceptance": "验证允许与拒绝路径，检查审计记录"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "wp-data",
      "type": "work_package",
      "name": "统一数据与接口",
      "attributes": {
        "duration_days": 15,
        "owner": "数据负责人",
        "output": "数据映射及接口契约",
        "cost": "示例估算待确认"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "wp-app",
      "type": "work_package",
      "name": "迁移订单应用",
      "attributes": {
        "duration_days": 20,
        "owner": "实施负责人",
        "output": "可试运行订单服务",
        "cost": "示例估算待确认"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "risk",
      "type": "risk",
      "name": "客户信息被越权读取",
      "attributes": {
        "owner": "客户数据负责人",
        "likelihood": "待评估",
        "impact": "客户权益受损"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "change",
      "type": "change_request",
      "name": "调整客户访问范围",
      "attributes": {
        "reason": "履约角色仅需必要字段",
        "impact": "数据接口、控制与测试",
        "severity": "待业务评定",
        "owner": "安全负责人",
        "decision": "candidate"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "req-risk",
      "type": "traces_to",
      "source": "req-privacy",
      "target": "risk",
      "label": "最小访问需求来自越权风险",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "change-req",
      "type": "changes",
      "source": "change",
      "target": "req-privacy",
      "label": "拟调整访问范围需求",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "req-affect",
      "type": "affects",
      "source": "req-privacy",
      "target": "wp-app",
      "label": "需求变化影响迁移验收",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-requirements-impact-assessment",
    "artifact_id": "requirements-impact-assessment",
    "title": "需求影响评估 · 星河零售虚构案例",
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
      "req-accuracy",
      "req-privacy",
      "wp-data",
      "wp-app",
      "risk",
      "change"
    ],
    "relationship_ids": [
      "req-risk",
      "change-req",
      "req-affect"
    ],
    "analysis": "访问范围变更首先影响隐私需求及订单迁移验收；沿控制和应用追溯进一步确认，不能仅凭图可达给出确定成本。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-requirements-impact-assessment"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-requirements-impact-assessment --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-requirements-impact-assessment --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
