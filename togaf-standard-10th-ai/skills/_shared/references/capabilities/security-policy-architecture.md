# 安全策略架构

ID：`security-policy-architecture`。主责：[togaf-security-risk](../../../togaf-security-risk/SKILL.md)。

来源：G152 §5.3.1。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

安全政策如何分层及分配责任？

- 业务或领域责任人
- 架构工作利益相关者
- 相关实施与治理人员
- 安全政策如何分层及分配责任？
- 结论的来源、范围与可验证性


## 输入及缺口处理

必需：

- 范围与五维语境
- 相关原始业务材料及其定位
- scope
- authority
- accountability

可选：

- 现有架构模型
- 历史评估或决策
- 组织特定量表和裁剪规则

关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。

## 元素、属性与关系

对象类型：security_policy。

```json
{
  "security_policy": [
    "scope",
    "authority",
    "accountability",
    "policy_level",
    "review_cycle"
  ]
}
```

{
  "name": {
    "meaning": "对象在本业务范围内的明确名称",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "scope": {
    "meaning": "适用组织、业务及架构边界",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "authority": {
    "meaning": "决策或数据权威及授权范围",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "accountability": {
    "meaning": "最终问责关系",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "policy_level": {
    "meaning": "政策在治理结构中的层级",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  },
  "review_cycle": {
    "meaning": "复核周期",
    "value_rule": "使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。",
    "definition_origin": "project-operational-convention-guided-by-cited-source"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |
| `project:policy_specializes` | security_policy → security_policy | 父政策在领域的专门化；方向从一般政策到更具体政策，不代表执行流程或组织汇报 |

## 分析步骤

1. 识别业务安全政策
2. 区分治理层级和领域
3. 明确政策权威与问责
4. 检查政策冲突和连续性联系

## 输出、检查与误读

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

- 政策架构不是防火墙规则列表
- 必需属性具有明确值或被登记为阻断缺口
- 来源与项目事实、参考内容、假设保持可区分
- 结论回应本规范的决策问题并可追溯

- 政策架构不是防火墙规则列表


## 视图和交付物

- [安全策略架构](../profiles/security-policy-architecture-default.md)

- [architecture-definition-document](../deliverables/architecture-definition-document.md)
- [architecture-requirements-specification](../deliverables/architecture-requirements-specification.md)
- [architecture-principles](../deliverables/architecture-principles.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "对「安全策略架构」给出：政策架构不是防火墙规则列表",
    "expected": "missing-evidence",
    "why": "政策架构不是防火墙规则列表"
  },
  "modification_example": {
    "change": "在「安全策略架构」的范围内新增或修改一项，检查下游是否随之变化",
    "expected": "受影响对象、关系、视图与缺口须同步更新；旧结论不自动沿用"
  }
}
```

## 可编辑示例与调用



以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

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

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact security-policy-architecture --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
