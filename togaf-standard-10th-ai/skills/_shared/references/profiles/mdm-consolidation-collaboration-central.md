# 客户主数据集成风格

`profile_id`: mdm-consolidation-collaboration-central；`artifact_id`: mdm-integration-style；主责：[togaf-information-data](../../../togaf-information-data/SKILL.md)。

来源：G21B/fig6-1。

## 构图与定义状态

表示族：`deployment`；输出：`diagram`。规范版本：2.3。

{
  "source_verified": false,
  "source_figure": "G21B/fig6-1",
  "layout_notes": "整合协作集中描述主记录与应用职责，不是强制技术路线",
  "review_status": "source-topology-repaired-awaiting-independent-review",
  "source_topology": "mdm-integration",
  "version": "2.3"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：application, master_repository。关系类型：project:master_data_transfer。

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

- 整合协作集中描述主记录与应用职责，不是强制技术路线

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "来源结构指导的解释性示例；项目事实为假设；不代表原图逐像素复刻、标准认证或架构批准。",
  "sources": [
    {
      "id": "example-source",
      "kind": "example",
      "description": "专用拓扑验收示例：G21B/fig6-1；来源图解释与候选企业场景分开。"
    }
  ],
  "entities": [
    {
      "id": "con-mdm",
      "type": "master_repository",
      "name": "整合式 MDM",
      "attributes": {
        "definition": "整合来源副本，供分析使用",
        "integration_style": "consolidation",
        "topology_role": "central",
        "authority": "external-master",
        "scope": "客户主数据",
        "style": "整合",
        "collaboration": "项目候选职责；需所有者确认"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "con-sys1",
      "type": "application",
      "name": "客户服务系统",
      "attributes": {
        "definition": "客户主记录的运营来源",
        "integration_style": "consolidation",
        "topology_role": "peripheral",
        "authority": "operational-master",
        "scope": "客户主数据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "con-sys2",
      "type": "application",
      "name": "销售系统",
      "attributes": {
        "definition": "客户主记录的运营来源",
        "integration_style": "consolidation",
        "topology_role": "peripheral",
        "authority": "operational-master",
        "scope": "客户主数据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "con-sys3",
      "type": "application",
      "name": "账务系统",
      "attributes": {
        "definition": "客户主记录的运营来源",
        "integration_style": "consolidation",
        "topology_role": "peripheral",
        "authority": "operational-master",
        "scope": "客户主数据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "coo-mdm",
      "type": "master_repository",
      "name": "协作式 MDM",
      "attributes": {
        "definition": "整合并形成规范客户版本",
        "integration_style": "cooperation",
        "topology_role": "central",
        "authority": "central-canonical",
        "scope": "客户主数据",
        "style": "协作",
        "collaboration": "项目候选职责；需所有者确认"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "coo-sys1",
      "type": "application",
      "name": "客户服务系统",
      "attributes": {
        "definition": "客户主记录的运营来源",
        "integration_style": "cooperation",
        "topology_role": "peripheral",
        "authority": "operational-master",
        "scope": "客户主数据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "coo-sys2",
      "type": "application",
      "name": "销售系统",
      "attributes": {
        "definition": "客户主记录的运营来源",
        "integration_style": "cooperation",
        "topology_role": "peripheral",
        "authority": "operational-master",
        "scope": "客户主数据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "coo-sys3",
      "type": "application",
      "name": "账务系统",
      "attributes": {
        "definition": "客户主记录的运营来源",
        "integration_style": "cooperation",
        "topology_role": "peripheral",
        "authority": "operational-master",
        "scope": "客户主数据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cen-mdm",
      "type": "master_repository",
      "name": "集中式 MDM",
      "attributes": {
        "definition": "唯一主数据存储与创建维护入口",
        "integration_style": "centralized",
        "topology_role": "central",
        "authority": "central-master",
        "scope": "客户主数据",
        "style": "集中",
        "collaboration": "项目候选职责；需所有者确认"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cen-sys1",
      "type": "application",
      "name": "客户服务系统",
      "attributes": {
        "definition": "消费MDM主记录，不保有独立主控权",
        "integration_style": "centralized",
        "topology_role": "peripheral",
        "authority": "consumer-only",
        "scope": "客户主数据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cen-sys2",
      "type": "application",
      "name": "销售系统",
      "attributes": {
        "definition": "消费MDM主记录，不保有独立主控权",
        "integration_style": "centralized",
        "topology_role": "peripheral",
        "authority": "consumer-only",
        "scope": "客户主数据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cen-sys3",
      "type": "application",
      "name": "账务系统",
      "attributes": {
        "definition": "消费MDM主记录，不保有独立主控权",
        "integration_style": "centralized",
        "topology_role": "peripheral",
        "authority": "consumer-only",
        "scope": "客户主数据"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "con-in1",
      "source": "con-sys1",
      "target": "con-mdm",
      "type": "project:master_data_transfer",
      "label": "源系统提交客户更新",
      "attributes": {
        "flow_role": "source-update",
        "data_scope": "客户主数据",
        "meaning": "源系统提交客户更新"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "con-in2",
      "source": "con-sys2",
      "target": "con-mdm",
      "type": "project:master_data_transfer",
      "label": "源系统提交客户更新",
      "attributes": {
        "flow_role": "source-update",
        "data_scope": "客户主数据",
        "meaning": "源系统提交客户更新"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "con-in3",
      "source": "con-sys3",
      "target": "con-mdm",
      "type": "project:master_data_transfer",
      "label": "源系统提交客户更新",
      "attributes": {
        "flow_role": "source-update",
        "data_scope": "客户主数据",
        "meaning": "源系统提交客户更新"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "coo-in1",
      "source": "coo-sys1",
      "target": "coo-mdm",
      "type": "project:master_data_transfer",
      "label": "源系统提交客户更新",
      "attributes": {
        "flow_role": "source-update",
        "data_scope": "客户主数据",
        "meaning": "源系统提交客户更新"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "coo-out1",
      "source": "coo-mdm",
      "target": "coo-sys1",
      "type": "project:master_data_transfer",
      "label": "MDM分发规范客户版本",
      "attributes": {
        "flow_role": "canonical-distribution",
        "data_scope": "客户主数据",
        "meaning": "MDM分发规范客户版本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "coo-in2",
      "source": "coo-sys2",
      "target": "coo-mdm",
      "type": "project:master_data_transfer",
      "label": "源系统提交客户更新",
      "attributes": {
        "flow_role": "source-update",
        "data_scope": "客户主数据",
        "meaning": "源系统提交客户更新"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "coo-out2",
      "source": "coo-mdm",
      "target": "coo-sys2",
      "type": "project:master_data_transfer",
      "label": "MDM分发规范客户版本",
      "attributes": {
        "flow_role": "canonical-distribution",
        "data_scope": "客户主数据",
        "meaning": "MDM分发规范客户版本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "coo-in3",
      "source": "coo-sys3",
      "target": "coo-mdm",
      "type": "project:master_data_transfer",
      "label": "源系统提交客户更新",
      "attributes": {
        "flow_role": "source-update",
        "data_scope": "客户主数据",
        "meaning": "源系统提交客户更新"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "coo-out3",
      "source": "coo-mdm",
      "target": "coo-sys3",
      "type": "project:master_data_transfer",
      "label": "MDM分发规范客户版本",
      "attributes": {
        "flow_role": "canonical-distribution",
        "data_scope": "客户主数据",
        "meaning": "MDM分发规范客户版本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cen-out1",
      "source": "cen-mdm",
      "target": "cen-sys1",
      "type": "project:master_data_transfer",
      "label": "MDM分发规范客户版本",
      "attributes": {
        "flow_role": "canonical-distribution",
        "data_scope": "客户主数据",
        "meaning": "MDM分发规范客户版本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cen-out2",
      "source": "cen-mdm",
      "target": "cen-sys2",
      "type": "project:master_data_transfer",
      "label": "MDM分发规范客户版本",
      "attributes": {
        "flow_role": "canonical-distribution",
        "data_scope": "客户主数据",
        "meaning": "MDM分发规范客户版本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "cen-out3",
      "source": "cen-mdm",
      "target": "cen-sys3",
      "type": "project:master_data_transfer",
      "label": "MDM分发规范客户版本",
      "attributes": {
        "flow_role": "canonical-distribution",
        "data_scope": "客户主数据",
        "meaning": "MDM分发规范客户版本"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "extensions": {
    "relationship_types": {
      "project:master_data_transfer": {
        "source_types": [
          "master_repository",
          "application"
        ],
        "target_types": [
          "master_repository",
          "application"
        ],
        "meaning": "项目明确的客户主数据传输；箭头指向接收方，不自动表示主控权或同步一致性。"
      }
    }
  },
  "view": {
    "id": "v-mdm-consolidation-collaboration-central",
    "artifact_id": "mdm-integration-style",
    "profile_id": "mdm-consolidation-collaboration-central",
    "title": "客户主数据集成风格／来源结构专用示例",
    "entity_ids": [
      "con-mdm",
      "con-sys1",
      "con-sys2",
      "con-sys3",
      "coo-mdm",
      "coo-sys1",
      "coo-sys2",
      "coo-sys3",
      "cen-mdm",
      "cen-sys1",
      "cen-sys2",
      "cen-sys3"
    ],
    "relationship_ids": [
      "con-in1",
      "con-in2",
      "con-in3",
      "coo-in1",
      "coo-out1",
      "coo-in2",
      "coo-out2",
      "coo-in3",
      "coo-out3",
      "cen-out1",
      "cen-out2",
      "cen-out3"
    ],
    "analysis": "明确来源结构、节点角色、流向与边界；未将相邻、颜色或布局当作企业事实。",
    "legend": "虚构候选或来源解释；相同ID表示同一对象。按专用线型、区域与编号语义读取；工程生成不授予来源等价或业务验收。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile mdm-consolidation-collaboration-central --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile mdm-consolidation-collaboration-central --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
