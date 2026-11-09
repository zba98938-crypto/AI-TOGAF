# 合同/度量目录（兼容默认）

`profile_id`: compat-contract-measure-catalog；`artifact_id`: contract-measure-catalog；主责：[togaf-implementation-governance](../../../togaf-implementation-governance/SKILL.md)。

来源：G248；G186；G184。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1。

{
  "id": "compat-contract-measure-catalog",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：contract, measure。关系类型：measured_by, commits_to。

```json
{
  "entities": {
    "contract": [
      "owner",
      "target",
      "unit",
      "measurement_window"
    ],
    "measure": [
      "owner",
      "target",
      "unit",
      "measurement_window"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 指标必须有单位与窗口
- 目标值与实际观测值分开

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
      "id": "contract",
      "type": "contract",
      "name": "订单服务架构约定",
      "attributes": {
        "owner": "业务发起方与实施负责人",
        "target": "订单准确确认",
        "unit": "比例",
        "measurement_window": "每周"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
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
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-contract-measure-catalog",
    "artifact_id": "contract-measure-catalog",
    "title": "合同/度量目录 · 星河零售虚构案例",
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
      "contract",
      "metric"
    ],
    "relationship_ids": [],
    "analysis": "哪些服务承诺以什么指标衡量和追责？ 本视图限定订单履约改造范围，展示案例设定的合同/度量目录。确定合同双方和服务范围；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-contract-measure-catalog"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-contract-measure-catalog --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-contract-measure-catalog --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
