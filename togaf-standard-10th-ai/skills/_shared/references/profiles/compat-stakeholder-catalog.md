# 利益相关者目录（兼容默认）

`profile_id`: compat-stakeholder-catalog；`artifact_id`: stakeholder-catalog；主责：[togaf-vision-scenarios](../../../togaf-vision-scenarios/SKILL.md)。

来源：G248；G176；G186。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1。

{
  "id": "compat-stakeholder-catalog",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：stakeholder。关系类型：concerned_with。

```json
{
  "entities": {
    "stakeholder": [
      "concern",
      "influence",
      "engagement",
      "owner"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 利益相关者不只项目团队
- 影响力评分需说明尺度

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
      "id": "stakeholder",
      "type": "stakeholder",
      "name": "履约负责人",
      "attributes": {
        "concern": "确认速度与准确率",
        "influence": "高：负责业务验收",
        "engagement": "每次架构迭代评审",
        "owner": "业务发起方"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-stakeholder-catalog",
    "artifact_id": "stakeholder-catalog",
    "title": "利益相关者目录 · 星河零售虚构案例",
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
      "stakeholder"
    ],
    "relationship_ids": [],
    "analysis": "谁关心哪些结果，如何参与架构决策？ 本视图限定订单履约改造范围，展示案例设定的利益相关者目录。识别受益、受损及决策方；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-stakeholder-catalog"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-stakeholder-catalog --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-stakeholder-catalog --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
