# 运营模式四子模型及资源取舍

`profile_id`: operating-model-four-submodels；`artifact_id`: operating-model；主责：[togaf-business-models-processes](../../../togaf-business-models-processes/SKILL.md)。

来源：G21H §4.4.2、§5.3。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-reference-1。

{
  "id": "operating-model-four-submodels",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "图形保留显式部门—功能—服务分类结构；表格保持完整源字段/本地判断，均不声称原图已通过。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:operating_submodel。关系类型：。

```json
{
  "entities": {
    "guide:operating_submodel": [
      "submodel",
      "customer_segment",
      "decision",
      "implication",
      "linked_submodels",
      "measures",
      "capacity",
      "action",
      "evidence_detail",
      "reference_identity"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 四子模型不漏
- 资源缺口必须计算依据/单位/期间和行动
- 未知成本或时长不捏造
- 四子模型不是四象限

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "明确虚构项目裁剪与真实参考来源分离；源图视觉核验另记。",
  "raw_input": "examples/addenda/reference-models/raw-business-materials.json",
  "analysis_path": "examples/addenda/reference-models/analysis.md",
  "sources": [
    {
      "id": "raw",
      "kind": "example",
      "description": "虚构松川市养老服务数字化试点；实际原料见本包raw-business-materials.json；补充场景参数均明示，不代表真实审批。",
      "locator": "raw-business-materials.json"
    },
    {
      "id": "grm",
      "kind": "local-translation",
      "description": "G21D本地正文目录摘录，官方定义/图形复核另记；保留参考身份。",
      "locator": "references/source-tables/government-reference-catalog.json"
    },
    {
      "id": "dbrm",
      "kind": "local-translation",
      "description": "G21H本地正文五表摘录；原始空格/破折号保留，项目裁剪与源映射分离。",
      "locator": "references/source-tables/dbrm-reference-mappings.json"
    }
  ],
  "entities": [
    {
      "id": "OM-posture",
      "type": "guide:operating_submodel",
      "name": "战略姿态与价值准则",
      "attributes": {
        "submodel": "posture",
        "customer_segment": "线上申领人及需要人工/无障碍协助的申领人",
        "decision": "客户可访问性优先，同时观察成本",
        "implication": "不以唯一最低成本决定渠道；线上与人工并行",
        "linked_submodels": [
          "OM-service"
        ],
        "measures": {
          "cost": "unknown；未提供金额",
          "lead_time": "unknown；未采样等待时长",
          "quality": "需记录申请/回执一致性证据",
          "flexibility": "保留线上/人工两入口",
          "agility": "变更申请经跨组三方复核，不给虚构分数"
        },
        "capacity": {
          "status": "see OM-resource"
        },
        "action": "与关联子模型责任人核对取舍",
        "evidence_detail": "R08",
        "reference_identity": "G21H §4.4.2四子模型；不等同G184运营模式二维象限"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "OM-service",
      "type": "guide:operating_submodel",
      "name": "服务模型",
      "attributes": {
        "submodel": "service",
        "customer_segment": "线上申领人及需要人工/无障碍协助的申领人",
        "decision": "线上状态查询＋人工协助",
        "implication": "受理失败转服务台；保留申请/回执和更新时间",
        "linked_submodels": [
          "OM-organization",
          "OM-resource"
        ],
        "measures": {
          "cost": "unknown；未提供金额",
          "lead_time": "unknown；未采样等待时长",
          "quality": "需记录申请/回执一致性证据",
          "flexibility": "保留线上/人工两入口",
          "agility": "变更申请经跨组三方复核，不给虚构分数"
        },
        "capacity": {
          "status": "see OM-resource"
        },
        "action": "与关联子模型责任人核对取舍",
        "evidence_detail": "R03/R08/R09",
        "reference_identity": "G21H §4.4.2四子模型；不等同G184运营模式二维象限"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "OM-organization",
      "type": "guide:operating_submodel",
      "name": "组织模型",
      "attributes": {
        "submodel": "organization",
        "customer_segment": "线上申领人及需要人工/无障碍协助的申领人",
        "decision": "待遇服务台确认；数据管家处理争议；平台组支持",
        "implication": "明确交接角色和升级，不把政府分类树当组织架构",
        "linked_submodels": [
          "OM-service",
          "OM-resource"
        ],
        "measures": {
          "cost": "unknown；未提供金额",
          "lead_time": "unknown；未采样等待时长",
          "quality": "需记录申请/回执一致性证据",
          "flexibility": "保留线上/人工两入口",
          "agility": "变更申请经跨组三方复核，不给虚构分数"
        },
        "capacity": {
          "status": "see OM-resource"
        },
        "action": "与关联子模型责任人核对取舍",
        "evidence_detail": "R01/R06/R07",
        "reference_identity": "G21H §4.4.2四子模型；不等同G184运营模式二维象限"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "OM-resource",
      "type": "guide:operating_submodel",
      "name": "资源模型",
      "attributes": {
        "submodel": "resource",
        "customer_segment": "线上申领人及需要人工/无障碍协助的申领人",
        "decision": "人工协助可用20h/周，需求24h/周",
        "implication": "差额4h/周未解决前不承诺无等待人工服务",
        "linked_submodels": [
          "OM-posture",
          "OM-service"
        ],
        "measures": {
          "cost": "unknown；未提供金额",
          "lead_time": "unknown；未采样等待时长",
          "quality": "需记录申请/回执一致性证据",
          "flexibility": "保留线上/人工两入口",
          "agility": "变更申请经跨组三方复核，不给虚构分数"
        },
        "capacity": {
          "required": 24,
          "available": 20,
          "gap": 4,
          "unit": "person-hour/week",
          "period": "试点第1周",
          "basis": "R08项目输入；gap=max(required-available,0)，非TOGAF公式"
        },
        "action": "补4h/周容量或调整服务范围，当前为候选",
        "evidence_detail": "R08",
        "reference_identity": "G21H §4.4.2四子模型；不等同G184运营模式二维象限"
      },
      "evidence": [
        "raw",
        "dbrm"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    }
  ],
  "relationships": [],
  "extensions": {
    "relationship_types": {}
  },
  "view": {
    "id": "v-operating-model-four-submodels",
    "artifact_id": "operating-model",
    "profile_id": "operating-model-four-submodels",
    "title": "运营模式四子模型及资源取舍",
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
      "OM-posture",
      "OM-service",
      "OM-organization",
      "OM-resource"
    ],
    "relationship_ids": [],
    "analysis": "依本包raw-business-materials.json观察形成候选分析；源表身份与本地判断分开。详细步骤见相应规范。",
    "legend": "参考分类/映射不是本地事实；未知与不适用分开。表格邻接不表达关系；图形嵌套仅由显式reference_classifies关系建立。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile operating-model-four-submodels --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile operating-model-four-submodels --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
