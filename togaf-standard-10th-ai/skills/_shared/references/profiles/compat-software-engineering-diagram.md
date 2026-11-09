# 软件工程图（兼容默认）

`profile_id`: compat-software-engineering-diagram；`artifact_id`: software-engineering-diagram；主责：[togaf-application-architecture](../../../togaf-application-architecture/SKILL.md)。

来源：G248；G248；G21I。

## 构图与定义状态

表示族：`network`；输出：`diagram`。规范版本：2.1。

{
  "id": "compat-software-engineering-diagram",
  "version": "2.1",
  "source_verified": false,
  "layout_notes": "保留既有制品的生成结构；未核实官方定义，不能当作来源复刻。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：software_module, interface。关系类型：depends_on, implements_interface。

```json
{
  "entities": {
    "software_module": [
      "responsibility",
      "version"
    ],
    "interface": [
      "version"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 不把开发工具流水线误作软件结构
- 结构图不自动描述部署

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
      "id": "interface",
      "type": "interface",
      "name": "库存校验接口",
      "attributes": {
        "producer": "库存应用",
        "consumer": "订单应用",
        "protocol": "HTTPS",
        "payload": "商品和数量",
        "version": "v1",
        "owner": "库存应用负责人"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "module-order",
      "type": "software_module",
      "name": "订单服务模块",
      "attributes": {
        "responsibility": "实现订单确认",
        "version": "候选 v1",
        "runtime": "应用运行节点"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "module-stock",
      "type": "software_module",
      "name": "库存适配模块",
      "attributes": {
        "responsibility": "封装库存契约",
        "version": "候选 v1",
        "runtime": "应用运行节点"
      },
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "module-dependency",
      "type": "depends_on",
      "source": "module-order",
      "target": "module-stock",
      "label": "依赖库存适配",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    },
    {
      "id": "module-interface",
      "type": "implements_interface",
      "source": "module-stock",
      "target": "interface",
      "label": "实现库存接口",
      "evidence": [
        "case"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-software-engineering-diagram",
    "artifact_id": "software-engineering-diagram",
    "title": "软件工程图 · 星河零售虚构案例",
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
      "module-order",
      "module-stock",
      "interface"
    ],
    "relationship_ids": [
      "module-dependency",
      "module-interface"
    ],
    "analysis": "软件组件如何组织并依赖接口或模块？ 本视图限定订单履约改造范围，展示案例设定的软件工程图。确定设计层级和组件职责；实际项目需由相关责任方核实。",
    "legend": "节点类型见标签；带标签有向线按文字解释；虚线表示假设或未确认关系；位置不表示隐含语义。",
    "allow_mixed_evolution": false,
    "profile_id": "compat-software-engineering-diagram"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-software-engineering-diagram --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile compat-software-engineering-diagram --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
