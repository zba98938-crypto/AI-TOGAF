# 产品功能、组件与接口追溯

`profile_id`: product-function-component-interface；`artifact_id`: building-block-description；主责：[togaf-gap-solutions](../../../togaf-gap-solutions/SKILL.md)。

来源：G21H §2产品架构定义、§5.3。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-reference-1。

{
  "id": "product-function-component-interface",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "图形保留显式部门—功能—服务分类结构；表格保持完整源字段/本地判断，均不声称原图已通过。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:product_function, guide:product_component, guide:product_interface。关系类型：guide:allocates_function, guide:interface_sender, guide:interface_receiver。

```json
{
  "entities": {
    "guide:product_function": [
      "product",
      "requirement",
      "operating_capability",
      "version",
      "evidence_detail"
    ],
    "guide:product_component": [
      "product",
      "component_role",
      "technical_component",
      "version",
      "evidence_detail"
    ],
    "guide:product_interface": [
      "product",
      "sender_ref",
      "receiver_ref",
      "operation",
      "request",
      "response",
      "security",
      "version",
      "evidence_detail"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 每功能有需求与至少一个组件分配
- 接口发送/接收与关系端点一致
- 运营/技术并行考虑，不画成串行流程
- 改变功能时更新接口/组件及运营要求

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
      "id": "F-SUBMIT",
      "type": "guide:product_function",
      "name": "提交受理",
      "attributes": {
        "product": "PR-PENSION",
        "requirement": "R-ACK：返回可追溯受理编号",
        "operating_capability": "OC-ACCEPT",
        "version": "1.0-candidate",
        "evidence_detail": "R09/R10"
      },
      "evidence": [
        "raw"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "F-STATUS",
      "type": "guide:product_function",
      "name": "查询受理状态",
      "attributes": {
        "product": "PR-PENSION",
        "requirement": "R-STATUS：返回状态与更新时间",
        "operating_capability": "OC-ANSWER",
        "version": "1.0-candidate",
        "evidence_detail": "R09/R10"
      },
      "evidence": [
        "raw"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "C-PORTAL",
      "type": "guide:product_component",
      "name": "申领前台",
      "attributes": {
        "product": "PR-PENSION",
        "component_role": "提供提交/查询交互",
        "technical_component": "TC-API受控API环境；非指定厂商",
        "version": "1.0-candidate",
        "evidence_detail": "R09/R10"
      },
      "evidence": [
        "raw"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "C-CASE",
      "type": "guide:product_component",
      "name": "受理组件",
      "attributes": {
        "product": "PR-PENSION",
        "component_role": "处理受理并保存编号",
        "technical_component": "TC-API受控API环境；非指定厂商",
        "version": "1.0-candidate",
        "evidence_detail": "R09/R10"
      },
      "evidence": [
        "raw"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "C-STATUS",
      "type": "guide:product_component",
      "name": "状态组件",
      "attributes": {
        "product": "PR-PENSION",
        "component_role": "提供状态和更新时间",
        "technical_component": "TC-API受控API环境；非指定厂商",
        "version": "1.0-candidate",
        "evidence_detail": "R09/R10"
      },
      "evidence": [
        "raw"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "I-SUBMIT",
      "type": "guide:product_interface",
      "name": "受理提交接口",
      "attributes": {
        "product": "PR-PENSION",
        "sender_ref": "C-PORTAL",
        "receiver_ref": "C-CASE",
        "operation": "submit",
        "request": "申请ID和必要字段",
        "response": "受理编号或可恢复失败",
        "security": "身份认证、按申请授权；具体规则需安全复核",
        "version": "1.0-candidate",
        "evidence_detail": "R09/R10"
      },
      "evidence": [
        "raw"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    },
    {
      "id": "I-STATUS",
      "type": "guide:product_interface",
      "name": "状态查询接口",
      "attributes": {
        "product": "PR-PENSION",
        "sender_ref": "C-PORTAL",
        "receiver_ref": "C-STATUS",
        "operation": "query",
        "request": "申请ID",
        "response": "状态/更新时间或授权拒绝",
        "security": "身份认证、按申请授权；具体规则需安全复核",
        "version": "1.0-candidate",
        "evidence_detail": "R09/R10"
      },
      "evidence": [
        "raw"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "not-started"
    }
  ],
  "relationships": [
    {
      "id": "PA-1",
      "type": "guide:allocates_function",
      "source": "F-SUBMIT",
      "target": "C-PORTAL",
      "label": "提供提交交互",
      "attributes": {},
      "evidence": [
        "raw"
      ],
      "certainty": "assumed"
    },
    {
      "id": "PA-2",
      "type": "guide:allocates_function",
      "source": "F-SUBMIT",
      "target": "C-CASE",
      "label": "处理受理",
      "attributes": {},
      "evidence": [
        "raw"
      ],
      "certainty": "assumed"
    },
    {
      "id": "PA-3",
      "type": "guide:allocates_function",
      "source": "F-STATUS",
      "target": "C-PORTAL",
      "label": "提供状态交互",
      "attributes": {},
      "evidence": [
        "raw"
      ],
      "certainty": "assumed"
    },
    {
      "id": "PA-4",
      "type": "guide:allocates_function",
      "source": "F-STATUS",
      "target": "C-STATUS",
      "label": "提供状态数据",
      "attributes": {},
      "evidence": [
        "raw"
      ],
      "certainty": "assumed"
    },
    {
      "id": "PE-I-SUBMIT-sender_ref",
      "type": "guide:interface_sender",
      "source": "I-SUBMIT",
      "target": "C-PORTAL",
      "label": "接口角色：sender_ref",
      "attributes": {},
      "evidence": [
        "raw"
      ],
      "certainty": "assumed"
    },
    {
      "id": "PE-I-SUBMIT-receiver_ref",
      "type": "guide:interface_receiver",
      "source": "I-SUBMIT",
      "target": "C-CASE",
      "label": "接口角色：receiver_ref",
      "attributes": {},
      "evidence": [
        "raw"
      ],
      "certainty": "assumed"
    },
    {
      "id": "PE-I-STATUS-sender_ref",
      "type": "guide:interface_sender",
      "source": "I-STATUS",
      "target": "C-PORTAL",
      "label": "接口角色：sender_ref",
      "attributes": {},
      "evidence": [
        "raw"
      ],
      "certainty": "assumed"
    },
    {
      "id": "PE-I-STATUS-receiver_ref",
      "type": "guide:interface_receiver",
      "source": "I-STATUS",
      "target": "C-STATUS",
      "label": "接口角色：receiver_ref",
      "attributes": {},
      "evidence": [
        "raw"
      ],
      "certainty": "assumed"
    }
  ],
  "extensions": {
    "relationship_types": {
      "guide:allocates_function": {
        "source_types": [
          "guide:product_function"
        ],
        "target_types": [
          "guide:product_component"
        ],
        "meaning": "产品功能分配到组件实现；非流程先后"
      },
      "guide:interface_sender": {
        "source_types": [
          "guide:product_interface"
        ],
        "target_types": [
          "guide:product_component"
        ],
        "meaning": "接口记录指定发送方组件；非该有向边本身作为数据流"
      },
      "guide:interface_receiver": {
        "source_types": [
          "guide:product_interface"
        ],
        "target_types": [
          "guide:product_component"
        ],
        "meaning": "接口记录指定接收方组件；真实请求方向由sender/receiver二者共同定义"
      }
    }
  },
  "view": {
    "id": "v-product-function-component-interface",
    "artifact_id": "building-block-description",
    "profile_id": "product-function-component-interface",
    "title": "产品功能、组件与接口追溯",
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
      "F-SUBMIT",
      "F-STATUS",
      "C-PORTAL",
      "C-CASE",
      "C-STATUS",
      "I-SUBMIT",
      "I-STATUS"
    ],
    "relationship_ids": [
      "PA-1",
      "PA-2",
      "PA-3",
      "PA-4",
      "PE-I-SUBMIT-sender_ref",
      "PE-I-SUBMIT-receiver_ref",
      "PE-I-STATUS-sender_ref",
      "PE-I-STATUS-receiver_ref"
    ],
    "analysis": "依本包raw-business-materials.json观察形成候选分析；源表身份与本地判断分开。详细步骤见相应规范。",
    "legend": "参考分类/映射不是本地事实；未知与不适用分开。表格邻接不表达关系；图形嵌套仅由显式reference_classifies关系建立。"
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile product-function-component-interface --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile product-function-component-interface --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
