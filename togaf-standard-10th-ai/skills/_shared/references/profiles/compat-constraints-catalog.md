# 约束目录（兼容默认）

`profile_id`: compat-constraints-catalog；`artifact_id`: constraints-catalog；主责：[togaf-requirements](../../../togaf-requirements/SKILL.md)。

来源：G248；G186；G152。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1。

{
  "id": "compat-constraints-catalog",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：constraint。关系类型：constrains。

```json
{
  "entities": {
    "constraint": [
      "category",
      "rationale",
      "owner",
      "source",
      "expiry"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 不能把偏好写成强制约束
- 过期限制需复核

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
      "id": "constraint-budget",
      "type": "constraint",
      "name": "季度交付窗口",
      "attributes": {
        "category": "时间",
        "rationale": "示例业务要求下一季度前试运行",
        "owner": "业务发起方",
        "source": "虚构案例",
        "expiry": "试运行结束后复核"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-constraints-catalog",
    "artifact_id": "constraints-catalog",
    "title": "约束目录 · 星河零售虚构案例",
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
      "constraint-budget"
    ],
    "relationship_ids": [],
    "analysis": "哪些边界限制架构选项，谁可以解除限制？ 本视图限定订单履约改造范围，展示案例设定的约束目录。区分法规、资源、时间和技术限制；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-constraints-catalog"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-constraints-catalog --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-constraints-catalog --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
