# BI 基线多过渡与目标

`profile_id`: bi-baseline-transition-target；`artifact_id`: bi-transition-architecture；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G238/fig3-1；G238/fig3-2；G238/fig3-3；G238/fig3-4。

## 构图与定义状态

表示族：`deployment`；输出：`diagram`。规范版本：2.3。

{
  "source_verified": false,
  "source_figure": "G238/fig3-1",
  "layout_notes": "四个状态分别表达且可运营，入站出站回写区分",
  "review_status": "source-topology-repaired-awaiting-independent-review",
  "source_topology": "bi-evolution",
  "version": "2.3"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：analytics_component。关系类型：project:analytics_flow。

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

- 四个状态分别表达且可运营，入站出站回写区分

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "来源结构指导的解释性示例；项目事实为假设；不代表原图逐像素复刻、标准认证或架构批准。",
  "sources": [
    {
      "id": "example-source",
      "kind": "example",
      "description": "专用拓扑验收示例：G238/fig3-1, G238/fig3-2, G238/fig3-3, G238/fig3-4；来源图解释与候选企业场景分开。"
    }
  ],
  "entities": [
    {
      "id": "b-tx1",
      "type": "analytics_component",
      "name": "事务应用1",
      "attributes": {
        "definition": "事务数据供数",
        "stage": "baseline",
        "component_role": "transaction",
        "boundary": "outside",
        "storage": "RDBMS",
        "asset_status": "existing",
        "role": "transaction",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "唯一现有历史库"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "b-tx2",
      "type": "analytics_component",
      "name": "事务应用2",
      "attributes": {
        "definition": "事务数据供数",
        "stage": "baseline",
        "component_role": "transaction",
        "boundary": "outside",
        "storage": "RDBMS",
        "asset_status": "existing",
        "role": "transaction",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "唯一现有历史库"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "b-tx3",
      "type": "analytics_component",
      "name": "含嵌入BI的事务应用",
      "attributes": {
        "definition": "事务数据供数",
        "stage": "baseline",
        "component_role": "transaction",
        "boundary": "outside",
        "storage": "RDBMS / Other",
        "asset_status": "existing",
        "role": "transaction",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "唯一现有历史库"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "b-edw",
      "type": "analytics_component",
      "name": "企业数据仓库 EDW",
      "attributes": {
        "definition": "历史关系数据",
        "stage": "baseline",
        "component_role": "edw",
        "boundary": "inside",
        "storage": "RDBMS",
        "asset_status": "existing",
        "role": "edw",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "唯一现有历史库"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "b-dm1",
      "type": "analytics_component",
      "name": "数据集市1",
      "attributes": {
        "definition": "分析或应用消费",
        "stage": "baseline",
        "component_role": "consumer",
        "boundary": "inside",
        "storage": "RDBMS",
        "asset_status": "existing",
        "role": "consumer",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "唯一现有历史库"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "b-dm2",
      "type": "analytics_component",
      "name": "数据集市2",
      "attributes": {
        "definition": "分析或应用消费",
        "stage": "baseline",
        "component_role": "consumer",
        "boundary": "inside",
        "storage": "RDBMS",
        "asset_status": "existing",
        "role": "consumer",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "唯一现有历史库"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "b-app1",
      "type": "analytics_component",
      "name": "既有应用1",
      "attributes": {
        "definition": "分析或应用消费",
        "stage": "baseline",
        "component_role": "consumer",
        "boundary": "inside",
        "storage": "RDBMS",
        "asset_status": "existing",
        "role": "consumer",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "唯一现有历史库"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t1-tx1",
      "type": "analytics_component",
      "name": "事务应用1",
      "attributes": {
        "definition": "事务数据供数",
        "stage": "transition1",
        "component_role": "transaction",
        "boundary": "outside",
        "storage": "RDBMS",
        "asset_status": "existing",
        "role": "transaction",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "并行运营，独立维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t1-tx2",
      "type": "analytics_component",
      "name": "事务应用2",
      "attributes": {
        "definition": "事务数据供数",
        "stage": "transition1",
        "component_role": "transaction",
        "boundary": "outside",
        "storage": "RDBMS",
        "asset_status": "existing",
        "role": "transaction",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "并行运营，独立维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t1-tx3",
      "type": "analytics_component",
      "name": "含嵌入BI的事务应用",
      "attributes": {
        "definition": "事务数据供数",
        "stage": "transition1",
        "component_role": "transaction",
        "boundary": "outside",
        "storage": "RDBMS / Other",
        "asset_status": "existing",
        "role": "transaction",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "并行运营，独立维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t1-edw",
      "type": "analytics_component",
      "name": "企业数据仓库 EDW",
      "attributes": {
        "definition": "历史关系数据",
        "stage": "transition1",
        "component_role": "edw",
        "boundary": "inside",
        "storage": "RDBMS",
        "asset_status": "existing",
        "role": "edw",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "并行运营，独立维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t1-dm1",
      "type": "analytics_component",
      "name": "数据集市1",
      "attributes": {
        "definition": "分析或应用消费",
        "stage": "transition1",
        "component_role": "consumer",
        "boundary": "inside",
        "storage": "RDBMS",
        "asset_status": "existing",
        "role": "consumer",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "并行运营，独立维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t1-dm2",
      "type": "analytics_component",
      "name": "数据集市2",
      "attributes": {
        "definition": "分析或应用消费",
        "stage": "transition1",
        "component_role": "consumer",
        "boundary": "inside",
        "storage": "RDBMS",
        "asset_status": "existing",
        "role": "consumer",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "并行运营，独立维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t1-app1",
      "type": "analytics_component",
      "name": "既有应用1",
      "attributes": {
        "definition": "分析或应用消费",
        "stage": "transition1",
        "component_role": "consumer",
        "boundary": "inside",
        "storage": "RDBMS",
        "asset_status": "existing",
        "role": "consumer",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "并行运营，独立维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t1-ext",
      "type": "analytics_component",
      "name": "设备、开放数据与日志",
      "attributes": {
        "definition": "新增数据源",
        "stage": "transition1",
        "component_role": "external",
        "boundary": "outside",
        "storage": "源方存储",
        "asset_status": "new",
        "role": "external",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "并行运营，独立维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t1-ng",
      "type": "analytics_component",
      "name": "新一代分析平台",
      "attributes": {
        "definition": "新增分析能力与历史数据存储",
        "stage": "transition1",
        "component_role": "platform",
        "boundary": "inside",
        "storage": "清洗数据副本",
        "asset_status": "new",
        "role": "platform",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "并行运营，独立维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t1-dm3",
      "type": "analytics_component",
      "name": "新数据集市3",
      "attributes": {
        "definition": "分析或应用消费",
        "stage": "transition1",
        "component_role": "consumer",
        "boundary": "inside",
        "storage": "RDBMS",
        "asset_status": "new",
        "role": "consumer",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "并行运营，独立维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t1-app2",
      "type": "analytics_component",
      "name": "新分析应用2",
      "attributes": {
        "definition": "分析或应用消费",
        "stage": "transition1",
        "component_role": "consumer",
        "boundary": "inside",
        "storage": "RDBMS",
        "asset_status": "new",
        "role": "consumer",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "并行运营，独立维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t1-app3",
      "type": "analytics_component",
      "name": "新分析应用3",
      "attributes": {
        "definition": "分析或应用消费",
        "stage": "transition1",
        "component_role": "consumer",
        "boundary": "inside",
        "storage": "RDBMS / NoSQL",
        "asset_status": "new",
        "role": "consumer",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "并行运营，独立维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-tx1",
      "type": "analytics_component",
      "name": "事务应用1",
      "attributes": {
        "definition": "事务数据供数",
        "stage": "transition2",
        "component_role": "transaction",
        "boundary": "outside",
        "storage": "RDBMS",
        "asset_status": "existing",
        "role": "transaction",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "并行运营，独立维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-tx2",
      "type": "analytics_component",
      "name": "事务应用2",
      "attributes": {
        "definition": "事务数据供数",
        "stage": "transition2",
        "component_role": "transaction",
        "boundary": "outside",
        "storage": "RDBMS",
        "asset_status": "existing",
        "role": "transaction",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "并行运营，独立维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-tx3",
      "type": "analytics_component",
      "name": "含嵌入BI的事务应用",
      "attributes": {
        "definition": "事务数据供数",
        "stage": "transition2",
        "component_role": "transaction",
        "boundary": "outside",
        "storage": "RDBMS / Other",
        "asset_status": "existing",
        "role": "transaction",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "并行运营，独立维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-edw",
      "type": "analytics_component",
      "name": "企业数据仓库 EDW",
      "attributes": {
        "definition": "历史关系数据",
        "stage": "transition2",
        "component_role": "edw",
        "boundary": "inside",
        "storage": "RDBMS",
        "asset_status": "existing",
        "role": "edw",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "并行运营，独立维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-dm1",
      "type": "analytics_component",
      "name": "数据集市1",
      "attributes": {
        "definition": "分析或应用消费",
        "stage": "transition2",
        "component_role": "consumer",
        "boundary": "inside",
        "storage": "RDBMS",
        "asset_status": "existing",
        "role": "consumer",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "并行运营，独立维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-dm2",
      "type": "analytics_component",
      "name": "数据集市2",
      "attributes": {
        "definition": "分析或应用消费",
        "stage": "transition2",
        "component_role": "consumer",
        "boundary": "inside",
        "storage": "RDBMS",
        "asset_status": "existing",
        "role": "consumer",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "并行运营，独立维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-app1",
      "type": "analytics_component",
      "name": "既有应用1",
      "attributes": {
        "definition": "分析或应用消费",
        "stage": "transition2",
        "component_role": "consumer",
        "boundary": "inside",
        "storage": "RDBMS",
        "asset_status": "modified",
        "role": "consumer",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "并行运营，独立维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-ext",
      "type": "analytics_component",
      "name": "设备、开放数据与日志",
      "attributes": {
        "definition": "新增数据源",
        "stage": "transition2",
        "component_role": "external",
        "boundary": "outside",
        "storage": "源方存储",
        "asset_status": "new",
        "role": "external",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "并行运营，独立维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-ng",
      "type": "analytics_component",
      "name": "新一代分析平台",
      "attributes": {
        "definition": "新增分析能力与历史数据存储",
        "stage": "transition2",
        "component_role": "platform",
        "boundary": "inside",
        "storage": "原始、集成与加工数据",
        "asset_status": "new",
        "role": "platform",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "并行运营，独立维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-dm3",
      "type": "analytics_component",
      "name": "新数据集市3",
      "attributes": {
        "definition": "分析或应用消费",
        "stage": "transition2",
        "component_role": "consumer",
        "boundary": "inside",
        "storage": "RDBMS",
        "asset_status": "new",
        "role": "consumer",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "并行运营，独立维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-app2",
      "type": "analytics_component",
      "name": "新分析应用2",
      "attributes": {
        "definition": "分析或应用消费",
        "stage": "transition2",
        "component_role": "consumer",
        "boundary": "inside",
        "storage": "RDBMS / NoSQL",
        "asset_status": "new",
        "role": "consumer",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "并行运营，独立维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-app3",
      "type": "analytics_component",
      "name": "新分析应用3",
      "attributes": {
        "definition": "分析或应用消费",
        "stage": "transition2",
        "component_role": "consumer",
        "boundary": "inside",
        "storage": "RDBMS / NoSQL",
        "asset_status": "new",
        "role": "consumer",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "并行运营，独立维护"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t-tx1",
      "type": "analytics_component",
      "name": "事务应用1",
      "attributes": {
        "definition": "事务数据供数",
        "stage": "target",
        "component_role": "transaction",
        "boundary": "outside",
        "storage": "RDBMS",
        "asset_status": "existing",
        "role": "transaction",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "统一历史职责，退役须独立验收"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t-tx2",
      "type": "analytics_component",
      "name": "事务应用2",
      "attributes": {
        "definition": "事务数据供数",
        "stage": "target",
        "component_role": "transaction",
        "boundary": "outside",
        "storage": "RDBMS",
        "asset_status": "existing",
        "role": "transaction",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "统一历史职责，退役须独立验收"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t-tx3",
      "type": "analytics_component",
      "name": "含嵌入BI的事务应用",
      "attributes": {
        "definition": "事务数据供数",
        "stage": "target",
        "component_role": "transaction",
        "boundary": "outside",
        "storage": "RDBMS / Other",
        "asset_status": "existing",
        "role": "transaction",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "统一历史职责，退役须独立验收"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t-edw",
      "type": "analytics_component",
      "name": "企业数据仓库 EDW",
      "attributes": {
        "definition": "数仓范围与职责被覆盖",
        "stage": "target",
        "component_role": "edw",
        "boundary": "inside",
        "storage": "RDBMS",
        "asset_status": "existing",
        "role": "edw",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "统一历史职责，退役须独立验收",
        "covered_by_id": "t-ng"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t-dm1",
      "type": "analytics_component",
      "name": "数据集市1",
      "attributes": {
        "definition": "分析或应用消费",
        "stage": "target",
        "component_role": "consumer",
        "boundary": "inside",
        "storage": "RDBMS",
        "asset_status": "existing",
        "role": "consumer",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "统一历史职责，退役须独立验收"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t-dm2",
      "type": "analytics_component",
      "name": "数据集市2",
      "attributes": {
        "definition": "分析或应用消费",
        "stage": "target",
        "component_role": "consumer",
        "boundary": "inside",
        "storage": "RDBMS",
        "asset_status": "existing",
        "role": "consumer",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "统一历史职责，退役须独立验收"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t-app1",
      "type": "analytics_component",
      "name": "既有应用1",
      "attributes": {
        "definition": "分析或应用消费",
        "stage": "target",
        "component_role": "consumer",
        "boundary": "inside",
        "storage": "Other",
        "asset_status": "modified",
        "role": "consumer",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "统一历史职责，退役须独立验收"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t-ext",
      "type": "analytics_component",
      "name": "设备、开放数据与日志",
      "attributes": {
        "definition": "新增数据源",
        "stage": "target",
        "component_role": "external",
        "boundary": "outside",
        "storage": "源方存储",
        "asset_status": "new",
        "role": "external",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "统一历史职责，退役须独立验收"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t-ng",
      "type": "analytics_component",
      "name": "新一代分析平台",
      "attributes": {
        "definition": "新增分析能力与历史数据存储",
        "stage": "target",
        "component_role": "platform",
        "boundary": "inside",
        "storage": "原始、集成与加工数据",
        "asset_status": "new",
        "role": "platform",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "统一历史职责，退役须独立验收"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t-dm3",
      "type": "analytics_component",
      "name": "新数据集市3",
      "attributes": {
        "definition": "分析或应用消费",
        "stage": "target",
        "component_role": "consumer",
        "boundary": "inside",
        "storage": "RDBMS / NoSQL",
        "asset_status": "new",
        "role": "consumer",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "统一历史职责，退役须独立验收"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t-app2",
      "type": "analytics_component",
      "name": "新分析应用2",
      "attributes": {
        "definition": "分析或应用消费",
        "stage": "target",
        "component_role": "consumer",
        "boundary": "inside",
        "storage": "RDBMS / NoSQL",
        "asset_status": "new",
        "role": "consumer",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "统一历史职责，退役须独立验收"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t-app3",
      "type": "analytics_component",
      "name": "新分析应用3",
      "attributes": {
        "definition": "分析或应用消费",
        "stage": "target",
        "component_role": "consumer",
        "boundary": "inside",
        "storage": "RDBMS / NoSQL",
        "asset_status": "new",
        "role": "consumer",
        "inbound": "见显式入站关系",
        "outbound": "见显式出站关系",
        "coexistence": "统一历史职责，退役须独立验收"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "b-tx1-edw",
      "source": "b-tx1",
      "target": "b-edw",
      "type": "project:analytics_flow",
      "label": "入站摄取／应用回写",
      "attributes": {
        "flow_role": "inbound",
        "change_status": "existing",
        "meaning": "入站摄取／应用回写"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "b-tx2-edw",
      "source": "b-tx2",
      "target": "b-edw",
      "type": "project:analytics_flow",
      "label": "入站摄取／应用回写",
      "attributes": {
        "flow_role": "inbound",
        "change_status": "existing",
        "meaning": "入站摄取／应用回写"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "b-tx3-edw",
      "source": "b-tx3",
      "target": "b-edw",
      "type": "project:analytics_flow",
      "label": "入站摄取／应用回写",
      "attributes": {
        "flow_role": "inbound",
        "change_status": "existing",
        "meaning": "入站摄取／应用回写"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "b-edw-dm1",
      "source": "b-edw",
      "target": "b-dm1",
      "type": "project:analytics_flow",
      "label": "出站数据供给",
      "attributes": {
        "flow_role": "outbound",
        "change_status": "existing",
        "meaning": "出站数据供给"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "b-edw-dm2",
      "source": "b-edw",
      "target": "b-dm2",
      "type": "project:analytics_flow",
      "label": "出站数据供给",
      "attributes": {
        "flow_role": "outbound",
        "change_status": "existing",
        "meaning": "出站数据供给"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "b-edw-app1",
      "source": "b-edw",
      "target": "b-app1",
      "type": "project:analytics_flow",
      "label": "出站数据供给",
      "attributes": {
        "flow_role": "outbound",
        "change_status": "existing",
        "meaning": "出站数据供给"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t1-tx1-edw",
      "source": "t1-tx1",
      "target": "t1-edw",
      "type": "project:analytics_flow",
      "label": "入站摄取／应用回写",
      "attributes": {
        "flow_role": "inbound",
        "change_status": "existing",
        "meaning": "入站摄取／应用回写"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t1-tx2-edw",
      "source": "t1-tx2",
      "target": "t1-edw",
      "type": "project:analytics_flow",
      "label": "入站摄取／应用回写",
      "attributes": {
        "flow_role": "inbound",
        "change_status": "existing",
        "meaning": "入站摄取／应用回写"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t1-tx3-edw",
      "source": "t1-tx3",
      "target": "t1-edw",
      "type": "project:analytics_flow",
      "label": "入站摄取／应用回写",
      "attributes": {
        "flow_role": "inbound",
        "change_status": "existing",
        "meaning": "入站摄取／应用回写"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t1-edw-dm1",
      "source": "t1-edw",
      "target": "t1-dm1",
      "type": "project:analytics_flow",
      "label": "出站数据供给",
      "attributes": {
        "flow_role": "outbound",
        "change_status": "existing",
        "meaning": "出站数据供给"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t1-edw-dm2",
      "source": "t1-edw",
      "target": "t1-dm2",
      "type": "project:analytics_flow",
      "label": "出站数据供给",
      "attributes": {
        "flow_role": "outbound",
        "change_status": "existing",
        "meaning": "出站数据供给"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t1-edw-app1",
      "source": "t1-edw",
      "target": "t1-app1",
      "type": "project:analytics_flow",
      "label": "出站数据供给",
      "attributes": {
        "flow_role": "outbound",
        "change_status": "existing",
        "meaning": "出站数据供给"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t1-edw-ng",
      "source": "t1-edw",
      "target": "t1-ng",
      "type": "project:analytics_flow",
      "label": "出站数据供给",
      "attributes": {
        "flow_role": "outbound",
        "change_status": "new",
        "meaning": "出站数据供给"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t1-edw-dm3",
      "source": "t1-edw",
      "target": "t1-dm3",
      "type": "project:analytics_flow",
      "label": "出站数据供给",
      "attributes": {
        "flow_role": "outbound",
        "change_status": "new",
        "meaning": "出站数据供给"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t1-ext-ng",
      "source": "t1-ext",
      "target": "t1-ng",
      "type": "project:analytics_flow",
      "label": "入站摄取／应用回写",
      "attributes": {
        "flow_role": "inbound",
        "change_status": "new",
        "meaning": "入站摄取／应用回写"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t1-ng-dm3",
      "source": "t1-ng",
      "target": "t1-dm3",
      "type": "project:analytics_flow",
      "label": "出站数据供给",
      "attributes": {
        "flow_role": "outbound",
        "change_status": "new",
        "meaning": "出站数据供给"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t1-ng-app2",
      "source": "t1-ng",
      "target": "t1-app2",
      "type": "project:analytics_flow",
      "label": "出站数据供给",
      "attributes": {
        "flow_role": "outbound",
        "change_status": "new",
        "meaning": "出站数据供给"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t1-ng-app3",
      "source": "t1-ng",
      "target": "t1-app3",
      "type": "project:analytics_flow",
      "label": "出站数据供给",
      "attributes": {
        "flow_role": "outbound",
        "change_status": "new",
        "meaning": "出站数据供给"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t1-app3-ng",
      "source": "t1-app3",
      "target": "t1-ng",
      "type": "project:analytics_flow",
      "label": "入站摄取／应用回写",
      "attributes": {
        "flow_role": "inbound",
        "change_status": "new",
        "meaning": "入站摄取／应用回写"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-tx2-edw",
      "source": "t2-tx2",
      "target": "t2-edw",
      "type": "project:analytics_flow",
      "label": "入站摄取／应用回写",
      "attributes": {
        "flow_role": "inbound",
        "change_status": "existing",
        "source_notation_note": "G238 fig3-3将这两条保留摄取线画为实线；此解释性视图按入站虚线图例统一，差异明确保留，不宣称逐线同形。",
        "meaning": "入站摄取／应用回写"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-tx3-edw",
      "source": "t2-tx3",
      "target": "t2-edw",
      "type": "project:analytics_flow",
      "label": "入站摄取／应用回写",
      "attributes": {
        "flow_role": "inbound",
        "change_status": "existing",
        "source_notation_note": "G238 fig3-3将这两条保留摄取线画为实线；此解释性视图按入站虚线图例统一，差异明确保留，不宣称逐线同形。",
        "meaning": "入站摄取／应用回写"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-tx1-ng",
      "source": "t2-tx1",
      "target": "t2-ng",
      "type": "project:analytics_flow",
      "label": "入站摄取／应用回写",
      "attributes": {
        "flow_role": "inbound",
        "change_status": "new",
        "meaning": "入站摄取／应用回写"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-tx2-ng",
      "source": "t2-tx2",
      "target": "t2-ng",
      "type": "project:analytics_flow",
      "label": "入站摄取／应用回写",
      "attributes": {
        "flow_role": "inbound",
        "change_status": "new",
        "meaning": "入站摄取／应用回写"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-tx3-ng",
      "source": "t2-tx3",
      "target": "t2-ng",
      "type": "project:analytics_flow",
      "label": "入站摄取／应用回写",
      "attributes": {
        "flow_role": "inbound",
        "change_status": "new",
        "meaning": "入站摄取／应用回写"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-ext-ng",
      "source": "t2-ext",
      "target": "t2-ng",
      "type": "project:analytics_flow",
      "label": "入站摄取／应用回写",
      "attributes": {
        "flow_role": "inbound",
        "change_status": "new",
        "meaning": "入站摄取／应用回写"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-edw-dm1",
      "source": "t2-edw",
      "target": "t2-dm1",
      "type": "project:analytics_flow",
      "label": "出站数据供给",
      "attributes": {
        "flow_role": "outbound",
        "change_status": "existing",
        "meaning": "出站数据供给"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-edw-dm2",
      "source": "t2-edw",
      "target": "t2-dm2",
      "type": "project:analytics_flow",
      "label": "出站数据供给",
      "attributes": {
        "flow_role": "outbound",
        "change_status": "existing",
        "meaning": "出站数据供给"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-edw-app1",
      "source": "t2-edw",
      "target": "t2-app1",
      "type": "project:analytics_flow",
      "label": "出站数据供给",
      "attributes": {
        "flow_role": "outbound",
        "change_status": "new",
        "meaning": "出站数据供给"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-edw-ng",
      "source": "t2-edw",
      "target": "t2-ng",
      "type": "project:analytics_flow",
      "label": "出站数据供给",
      "attributes": {
        "flow_role": "outbound",
        "change_status": "new",
        "meaning": "出站数据供给"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-ng-edw",
      "source": "t2-ng",
      "target": "t2-edw",
      "type": "project:analytics_flow",
      "label": "出站数据供给",
      "attributes": {
        "flow_role": "outbound",
        "change_status": "new",
        "meaning": "出站数据供给"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-ng-app1",
      "source": "t2-ng",
      "target": "t2-app1",
      "type": "project:analytics_flow",
      "label": "出站数据供给",
      "attributes": {
        "flow_role": "outbound",
        "change_status": "new",
        "meaning": "出站数据供给"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-ng-dm3",
      "source": "t2-ng",
      "target": "t2-dm3",
      "type": "project:analytics_flow",
      "label": "出站数据供给",
      "attributes": {
        "flow_role": "outbound",
        "change_status": "new",
        "meaning": "出站数据供给"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-ng-app2",
      "source": "t2-ng",
      "target": "t2-app2",
      "type": "project:analytics_flow",
      "label": "出站数据供给",
      "attributes": {
        "flow_role": "outbound",
        "change_status": "new",
        "meaning": "出站数据供给"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-ng-app3",
      "source": "t2-ng",
      "target": "t2-app3",
      "type": "project:analytics_flow",
      "label": "出站数据供给",
      "attributes": {
        "flow_role": "outbound",
        "change_status": "new",
        "meaning": "出站数据供给"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-app2-ng",
      "source": "t2-app2",
      "target": "t2-ng",
      "type": "project:analytics_flow",
      "label": "入站摄取／应用回写",
      "attributes": {
        "flow_role": "inbound",
        "change_status": "new",
        "meaning": "入站摄取／应用回写"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t2-app3-ng",
      "source": "t2-app3",
      "target": "t2-ng",
      "type": "project:analytics_flow",
      "label": "入站摄取／应用回写",
      "attributes": {
        "flow_role": "inbound",
        "change_status": "new",
        "meaning": "入站摄取／应用回写"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t-tx1-ng",
      "source": "t-tx1",
      "target": "t-ng",
      "type": "project:analytics_flow",
      "label": "入站摄取／应用回写",
      "attributes": {
        "flow_role": "inbound",
        "change_status": "new",
        "meaning": "入站摄取／应用回写"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t-tx2-ng",
      "source": "t-tx2",
      "target": "t-ng",
      "type": "project:analytics_flow",
      "label": "入站摄取／应用回写",
      "attributes": {
        "flow_role": "inbound",
        "change_status": "new",
        "meaning": "入站摄取／应用回写"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t-tx3-ng",
      "source": "t-tx3",
      "target": "t-ng",
      "type": "project:analytics_flow",
      "label": "入站摄取／应用回写",
      "attributes": {
        "flow_role": "inbound",
        "change_status": "new",
        "meaning": "入站摄取／应用回写"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t-ext-ng",
      "source": "t-ext",
      "target": "t-ng",
      "type": "project:analytics_flow",
      "label": "入站摄取／应用回写",
      "attributes": {
        "flow_role": "inbound",
        "change_status": "new",
        "meaning": "入站摄取／应用回写"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t-ng-dm1",
      "source": "t-ng",
      "target": "t-dm1",
      "type": "project:analytics_flow",
      "label": "出站数据供给",
      "attributes": {
        "flow_role": "outbound",
        "change_status": "existing",
        "meaning": "出站数据供给"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t-ng-dm2",
      "source": "t-ng",
      "target": "t-dm2",
      "type": "project:analytics_flow",
      "label": "出站数据供给",
      "attributes": {
        "flow_role": "outbound",
        "change_status": "existing",
        "meaning": "出站数据供给"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t-ng-app1",
      "source": "t-ng",
      "target": "t-app1",
      "type": "project:analytics_flow",
      "label": "出站数据供给",
      "attributes": {
        "flow_role": "outbound",
        "change_status": "existing",
        "meaning": "出站数据供给"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t-ng-dm3",
      "source": "t-ng",
      "target": "t-dm3",
      "type": "project:analytics_flow",
      "label": "出站数据供给",
      "attributes": {
        "flow_role": "outbound",
        "change_status": "new",
        "meaning": "出站数据供给"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t-ng-app2",
      "source": "t-ng",
      "target": "t-app2",
      "type": "project:analytics_flow",
      "label": "出站数据供给",
      "attributes": {
        "flow_role": "outbound",
        "change_status": "new",
        "meaning": "出站数据供给"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t-ng-app3",
      "source": "t-ng",
      "target": "t-app3",
      "type": "project:analytics_flow",
      "label": "出站数据供给",
      "attributes": {
        "flow_role": "outbound",
        "change_status": "new",
        "meaning": "出站数据供给"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t-dm3-ng",
      "source": "t-dm3",
      "target": "t-ng",
      "type": "project:analytics_flow",
      "label": "入站摄取／应用回写",
      "attributes": {
        "flow_role": "inbound",
        "change_status": "new",
        "meaning": "入站摄取／应用回写"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t-app2-ng",
      "source": "t-app2",
      "target": "t-ng",
      "type": "project:analytics_flow",
      "label": "入站摄取／应用回写",
      "attributes": {
        "flow_role": "inbound",
        "change_status": "new",
        "meaning": "入站摄取／应用回写"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "t-app3-ng",
      "source": "t-app3",
      "target": "t-ng",
      "type": "project:analytics_flow",
      "label": "入站摄取／应用回写",
      "attributes": {
        "flow_role": "inbound",
        "change_status": "new",
        "meaning": "入站摄取／应用回写"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "extensions": {
    "relationship_types": {
      "project:analytics_flow": {
        "source_types": [
          "analytics_component"
        ],
        "target_types": [
          "analytics_component"
        ],
        "meaning": "指定运营状态中的分析数据传输，箭头指向接收者。入站、出站、回写和变更状态显式声明。"
      }
    }
  },
  "view": {
    "id": "v-bi-baseline-transition-target",
    "artifact_id": "bi-transition-architecture",
    "profile_id": "bi-baseline-transition-target",
    "title": "BI 基线多过渡与目标／来源结构专用示例",
    "entity_ids": [
      "b-tx1",
      "b-tx2",
      "b-tx3",
      "b-edw",
      "b-dm1",
      "b-dm2",
      "b-app1",
      "t1-tx1",
      "t1-tx2",
      "t1-tx3",
      "t1-edw",
      "t1-dm1",
      "t1-dm2",
      "t1-app1",
      "t1-ext",
      "t1-ng",
      "t1-dm3",
      "t1-app2",
      "t1-app3",
      "t2-tx1",
      "t2-tx2",
      "t2-tx3",
      "t2-edw",
      "t2-dm1",
      "t2-dm2",
      "t2-app1",
      "t2-ext",
      "t2-ng",
      "t2-dm3",
      "t2-app2",
      "t2-app3",
      "t-tx1",
      "t-tx2",
      "t-tx3",
      "t-edw",
      "t-dm1",
      "t-dm2",
      "t-app1",
      "t-ext",
      "t-ng",
      "t-dm3",
      "t-app2",
      "t-app3"
    ],
    "relationship_ids": [
      "b-tx1-edw",
      "b-tx2-edw",
      "b-tx3-edw",
      "b-edw-dm1",
      "b-edw-dm2",
      "b-edw-app1",
      "t1-tx1-edw",
      "t1-tx2-edw",
      "t1-tx3-edw",
      "t1-edw-dm1",
      "t1-edw-dm2",
      "t1-edw-app1",
      "t1-edw-ng",
      "t1-edw-dm3",
      "t1-ext-ng",
      "t1-ng-dm3",
      "t1-ng-app2",
      "t1-ng-app3",
      "t1-app3-ng",
      "t2-tx2-edw",
      "t2-tx3-edw",
      "t2-tx1-ng",
      "t2-tx2-ng",
      "t2-tx3-ng",
      "t2-ext-ng",
      "t2-edw-dm1",
      "t2-edw-dm2",
      "t2-edw-app1",
      "t2-edw-ng",
      "t2-ng-edw",
      "t2-ng-app1",
      "t2-ng-dm3",
      "t2-ng-app2",
      "t2-ng-app3",
      "t2-app2-ng",
      "t2-app3-ng",
      "t-tx1-ng",
      "t-tx2-ng",
      "t-tx3-ng",
      "t-ext-ng",
      "t-ng-dm1",
      "t-ng-dm2",
      "t-ng-app1",
      "t-ng-dm3",
      "t-ng-app2",
      "t-ng-app3",
      "t-dm3-ng",
      "t-app2-ng",
      "t-app3-ng"
    ],
    "analysis": "明确来源结构、节点角色、流向与边界；未将相邻、颜色或布局当作企业事实。",
    "legend": "虚构候选或来源解释；相同ID表示同一对象。按专用线型、区域与编号语义读取；工程生成不授予来源等价或业务验收。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile bi-baseline-transition-target --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile bi-baseline-transition-target --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
