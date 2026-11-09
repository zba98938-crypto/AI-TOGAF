# 安全策略架构

`profile_id`: security-policy-architecture-default；`artifact_id`: security-policy-architecture；主责：[togaf-security-risk](../../../togaf-security-risk/SKILL.md)。

来源：G152 §5.3.1。

## 构图与定义状态

表示族：`nested-map`；输出：`diagram`。规范版本：2.2。

{
  "source_verified": false,
  "layout_notes": "按工作产品属性组织；来源无直接对应图时为项目补充模板。",
  "version": "2.2"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：security_policy。关系类型：project:policy_specializes。

```json
{
  "entities": {
    "security_policy": [
      "scope",
      "authority",
      "accountability",
      "policy_level",
      "review_cycle"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 政策架构不是防火墙规则列表
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构星河零售验收示例；全部对象为假设，未声称事实、批准或来源图复刻。",
  "sources": [
    {
      "id": "example-source",
      "kind": "example",
      "description": "虚构业务原料：订单安全总方针：{\"scope\": \"订单、付款与仓库履约\", \"authority\": \"虚构治理委员会提出，批准状态另行记录\", \"accountability\": \"企业风险负责人\", \"policy_level\": \"企业政策\", \"review_cycle\": \"项目规则：每季度及重大变更后\", \"definition\": \"订单与履约信息按已授权职责访问；政策尚属候选\"}；客户订单数据处理政策：{\"scope\": \"客户资料及退款交易\", \"authority\": \"数据负责人建议，须治理委员会接受\", \"accountability\": \"客户数据所有者\", \"policy_level\": \"领域政策\", \"review_cycle\": \"项目规则：每季度及处理目的改变后\", \"definition\": \"仅客户服务和退款处理角色可访问对应目的字段；新用途先审查\"}；仓库终端访问政策：{\"scope\": \"共享扫描终端与发运状态\", \"authority\": \"运营安全负责人建议，须运营负责人接受\", \"accountability\": \"仓储服务负责人\", \"policy_level\": \"领域政策\", \"review_cycle\": \"项目规则：每月复核账号，重大变更后复评\", \"definition\": \"个人账号登录；离岗撤权；只允许改写所属仓发运状态\"}"
    }
  ],
  "entities": [
    {
      "id": "security-policy-architecture-default-root",
      "type": "security_policy",
      "name": "订单安全总方针",
      "attributes": {
        "scope": "订单、付款与仓库履约",
        "authority": "虚构治理委员会提出，批准状态另行记录",
        "accountability": "企业风险负责人",
        "policy_level": "企业政策",
        "review_cycle": "项目规则：每季度及重大变更后",
        "definition": "订单与履约信息按已授权职责访问；政策尚属候选"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "security-policy-architecture-default-child0",
      "type": "security_policy",
      "name": "客户订单数据处理政策",
      "attributes": {
        "scope": "客户资料及退款交易",
        "authority": "数据负责人建议，须治理委员会接受",
        "accountability": "客户数据所有者",
        "policy_level": "领域政策",
        "review_cycle": "项目规则：每季度及处理目的改变后",
        "definition": "仅客户服务和退款处理角色可访问对应目的字段；新用途先审查"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "security-policy-architecture-default-child1",
      "type": "security_policy",
      "name": "仓库终端访问政策",
      "attributes": {
        "scope": "共享扫描终端与发运状态",
        "authority": "运营安全负责人建议，须运营负责人接受",
        "accountability": "仓储服务负责人",
        "policy_level": "领域政策",
        "review_cycle": "项目规则：每月复核账号，重大变更后复评",
        "definition": "个人账号登录；离岗撤权；只允许改写所属仓发运状态"
      },
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [
    {
      "id": "security-policy-architecture-default-part0",
      "type": "project:policy_specializes",
      "source": "security-policy-architecture-default-root",
      "target": "security-policy-architecture-default-child0",
      "label": "父政策在领域的专门化；方向从一般政策到更具体政策，不代表执行流程或组织汇报",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    },
    {
      "id": "security-policy-architecture-default-part1",
      "type": "project:policy_specializes",
      "source": "security-policy-architecture-default-root",
      "target": "security-policy-architecture-default-child1",
      "label": "父政策在领域的专门化；方向从一般政策到更具体政策，不代表执行流程或组织汇报",
      "evidence": [
        "example-source"
      ],
      "certainty": "assumed"
    }
  ],
  "view": {
    "id": "v-security-policy-architecture-default",
    "artifact_id": "security-policy-architecture",
    "profile_id": "security-policy-architecture-default",
    "title": "安全策略架构／虚构案例",
    "entity_ids": [
      "security-policy-architecture-default-root",
      "security-policy-architecture-default-child0",
      "security-policy-architecture-default-child1"
    ],
    "relationship_ids": [
      "security-policy-architecture-default-part0",
      "security-policy-architecture-default-part1"
    ],
    "analysis": "从本例原始职责、权限、契约与验收材料形成明确分解。关系类型为命名空间项目语义，来源仅指导方法。父子结构不赋予批准或执行先后。",
    "legend": "嵌套只表示已声明的project:policy_specializes关系；候选事实、实际批准与实现状态分开。"
  },
  "extensions": {
    "relationship_types": {
      "project:policy_specializes": {
        "source_types": [
          "security_policy"
        ],
        "target_types": [
          "security_policy"
        ],
        "meaning": "父政策在领域的专门化；方向从一般政策到更具体政策，不代表执行流程或组织汇报"
      }
    }
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile security-policy-architecture-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile security-policy-architecture-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
