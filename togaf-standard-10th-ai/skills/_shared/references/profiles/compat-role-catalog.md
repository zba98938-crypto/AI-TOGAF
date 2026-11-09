# 角色目录（兼容默认）

`profile_id`: compat-role-catalog；`artifact_id`: role-catalog；主责：[togaf-organization-roles](../../../togaf-organization-roles/SKILL.md)。

来源：G248；G198；G249；G152。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1。

{
  "id": "compat-role-catalog",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：role。关系类型：assigned_to。

```json
{
  "entities": {
    "role": [
      "responsibility",
      "authority",
      "skill"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 岗位名称不必等于角色
- RACI 是可选补充不能冒充默认矩阵语义

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
      "id": "role-buyer",
      "type": "role",
      "name": "购买方角色",
      "attributes": {
        "responsibility": "提交并确认订单",
        "authority": "管理本人订单",
        "skill": "订单操作"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "role-picker",
      "type": "role",
      "name": "拣货角色",
      "attributes": {
        "responsibility": "按已确认订单备货",
        "authority": "查看必要的备货信息",
        "skill": "仓储拣配"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-role-catalog",
    "artifact_id": "role-catalog",
    "title": "角色目录 · 星河零售虚构案例",
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
      "role-buyer",
      "role-picker"
    ],
    "relationship_ids": [],
    "analysis": "哪些职责与权限可分配给参与者？ 本视图限定订单履约改造范围，展示案例设定的角色目录。从职责识别角色；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-role-catalog"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-role-catalog --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-role-catalog --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
