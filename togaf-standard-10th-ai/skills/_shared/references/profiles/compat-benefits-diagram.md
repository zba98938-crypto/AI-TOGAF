# 收益图（兼容默认）

`profile_id`: compat-benefits-diagram；`artifact_id`: benefits-diagram；主责：[togaf-strategy-capabilities](../../../togaf-strategy-capabilities/SKILL.md)。

来源：G248；G184；G233。

## 构图与定义状态

表示族：`network`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-benefits-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：work_package, outcome, benefit, objective, measure。关系类型：delivers, enables_benefit, contributes_to, measured_by。

```json
{
  "entities": {
    "work_package": [
      "owner"
    ],
    "outcome": [
      "owner"
    ],
    "benefit": [
      "owner",
      "metric",
      "target"
    ],
    "objective": [
      "owner",
      "metric",
      "target"
    ],
    "measure": [
      "owner",
      "metric",
      "target"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 投入产出不是收益本身
- 关联箭头不代表已证实因果

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
      "id": "objective",
      "type": "objective",
      "name": "缩短订单确认时间",
      "attributes": {
        "statement": "示例目标：确认时间中位数由 20 分钟降低至 5 分钟",
        "owner": "履约负责人",
        "metric": "确认时长中位数",
        "target": 5,
        "unit": "分钟",
        "baseline": 20,
        "deadline": "试运行结束"
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
      "id": "outcome",
      "type": "outcome",
      "name": "订单状态与库存可协同",
      "attributes": {
        "owner": "履约负责人"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "benefit",
      "type": "benefit",
      "name": "减少确认等待",
      "attributes": {
        "owner": "履约负责人",
        "metric": "确认时长",
        "target": "示例 5 分钟"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "wp-outcome",
      "type": "delivers",
      "source": "wp-app",
      "target": "outcome",
      "label": "迁移交付协同能力",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "outcome-benefit",
      "type": "enables_benefit",
      "source": "outcome",
      "target": "benefit",
      "label": "假设协同减少等待",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "benefit-objective",
      "type": "contributes_to",
      "source": "benefit",
      "target": "objective",
      "label": "支持缩短确认时间",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-benefits-diagram",
    "artifact_id": "benefits-diagram",
    "title": "收益图 · 星河零售虚构案例",
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
      "wp-app",
      "outcome",
      "benefit",
      "objective"
    ],
    "relationship_ids": [
      "wp-outcome",
      "outcome-benefit",
      "benefit-objective"
    ],
    "analysis": "变革如何通过成果实现可衡量收益？ 本视图限定订单履约改造范围，展示案例设定的收益图。从目标倒推收益及可观察成果；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-benefits-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-benefits-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-benefits-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
