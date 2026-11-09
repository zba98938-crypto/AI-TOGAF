# 微服务契约与实际／计划消费者

`profile_id`: msa-contract-consumer-evidence；`artifact_id`: interface-catalog；主责：[togaf-application-architecture](../../../togaf-application-architecture/SKILL.md)。

来源：G21I §8.2、§9.1、§12.2、§13.1–13.2。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-extension-1。

{
  "id": "msa-contract-consumer-evidence",
  "version": "1.0",
  "source_verified": false,
  "layout_notes": "完整字段及关系表；原图结构复刻由独立图形规范验证，本表不冒领。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:msa_contract。关系类型：。

```json
{
  "entities": {
    "guide:msa_contract": [
      "service_id",
      "ABF",
      "API",
      "version",
      "consumer",
      "consumer_status",
      "credential",
      "NFR",
      "address",
      "compatibility",
      "change_impact",
      "source"
    ]
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 每版本消费者实际/计划明确
- NFR必须有单位/期间/依据或明确待测
- 契约变更必须复核消费者影响
- 一个服务不能偷包多个独立ABF

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

```json
{
  "notice": "虚构完整案例；表格伴随语义不冒称原图视觉通过。",
  "raw_input": "examples/addenda/existing-extensions/msa-contract-consumer-evidence/raw-brief.md",
  "analysis_path": "examples/addenda/existing-extensions/msa-contract-consumer-evidence/analysis.md",
  "sources": [
    {
      "id": "case-source",
      "kind": "example",
      "description": "虚构借阅资格微服务只判断一个ABF。1.0已有预约服务和馆员台两个试点消费者；移动端拟用1.1但未获批。服务契约要求身份令牌、最小返回，项目候选p95≤200ms、月可用99.5%，尚未测试。增加原因码须检查旧消费者映射。",
      "locator": "raw-brief.md"
    }
  ],
  "entities": [
    {
      "id": "MSC-01",
      "type": "guide:msa_contract",
      "name": "读者借阅资格服务1.0",
      "attributes": {
        "service_id": "MS-eligibility",
        "ABF": "判断读者在指定时点的借阅资格",
        "API": "GET /eligibility/{readerId}",
        "version": "1.0",
        "consumer": "预约服务；馆员台",
        "consumer_status": "actual-in-fictional-pilot",
        "credential": "服务身份令牌；角色read-eligibility",
        "NFR": {
          "latency": "项目约定p95≤200ms，试点待测",
          "availability": "项目目标99.5%月度，未验证",
          "security": "不返回证件号；仅资格结论及原因码"
        },
        "address": "svc://eligibility/v1（虚构稳定逻辑名）",
        "compatibility": "既有字段不改含义，新增原因码须消费者复核",
        "change_impact": "新增原因码影响两消费者映射；不得无通知直接删除",
        "source": "项目契约草案；未真实发布"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    },
    {
      "id": "MSC-02",
      "type": "guide:msa_contract",
      "name": "读者借阅资格服务1.1候选",
      "attributes": {
        "service_id": "MS-eligibility",
        "ABF": "判断读者在指定时点的借阅资格",
        "API": "GET /eligibility/{readerId}",
        "version": "1.1-candidate",
        "consumer": "移动端自助预约",
        "consumer_status": "planned",
        "credential": "待安全负责人确认授权范围",
        "NFR": {
          "latency": "沿用1.0候选SLA，需负载重测",
          "availability": "待容量确认",
          "security": "候选同1.0最小返回"
        },
        "address": "svc://eligibility/v1（候选兼容部署）",
        "compatibility": "新消费者不得被当作已迁移；是否增加字段待需求核实",
        "change_impact": "第三消费者增加流量与跨团队变更范围",
        "source": "项目新增渠道申请，未真实批准"
      },
      "evidence": [
        "case-source"
      ],
      "certainty": "assumed",
      "approval_status": "candidate",
      "implementation_status": "unknown"
    }
  ],
  "relationships": [],
  "extensions": {
    "relationship_types": {}
  },
  "states": [],
  "view": {
    "id": "v-msa-contract-consumer-evidence",
    "artifact_id": "interface-catalog",
    "profile_id": "msa-contract-consumer-evidence",
    "title": "微服务契约与实际／计划消费者",
    "context": {
      "domains": [
        "business",
        "data",
        "application",
        "technology"
      ],
      "landscape": "capability",
      "purpose": "project",
      "abstraction": "logical",
      "evolution": "target"
    },
    "entity_ids": [
      "MSC-01",
      "MSC-02"
    ],
    "relationship_ids": [],
    "analysis": "见本例analysis.md；模型为依据raw-brief.md形成的人工候选分析，不是真实批准。",
    "legend": "表格表达正文操作语义，不声称原图复刻。未知显式保留，ID稳定。",
    "allow_mixed_evolution": true
  }
}
```

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile msa-contract-consumer-evidence --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile msa-contract-consumer-evidence --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
