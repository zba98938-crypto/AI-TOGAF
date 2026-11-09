# 数字可持续性能力评估

ID：`sustainability-capability-assessment`。主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G242 §3.2、§5.2表5-1。定义状态：`guide-work-product-with-project-operational-contract`。字段与工具接口为项目操作约定，不自动成为官方强制规则。

## 决策与受众

企业可持续ICT能力有哪些具体强项、缺口和改进？

- 业务负责人
- 企业架构师
- 环境核算负责人
- 采购及供应商负责人
- HR与治理负责人
- 企业可持续ICT能力有哪些具体强项、缺口和改进？
- 依据、权限、完整性和可追溯性


## 输入及缺口处理

必需：

- 组织、服务、业务用途及所评估期间/生命周期边界
- 原始访谈、使用数据、供应商记录及稳定证据ID
- 适用目标、职责和组织自定决策规则；未知项显式登记

可选：

- 历史评估、环境数据目录、采购契约及角色技能资料

关键依据未知时给候选表、受影响ID与责任；不编造权重、阈值、估算、批准或实际完成。

## 元素、属性与关系

对象类型：guide:sustainability_capability。

```json
{
  "guide:sustainability_capability": [
    "dimension",
    "reference_functions",
    "current_evidence",
    "target_need",
    "gap",
    "action",
    "owner",
    "assessment_rule",
    "rating",
    "evidence_refs"
  ]
}
```

{
  "name": {
    "meaning": "评估项",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "dimension": {
    "meaning": "G242六维之一",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "reference_functions": {
    "meaning": "关联的七功能组/详细功能；多对多",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "current_evidence": {
    "meaning": "已做/未证/部分开展的事实",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "target_need": {
    "meaning": "组织实际需要",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "gap": {
    "meaning": "当前与需要之间的具体缺口",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "action": {
    "meaning": "改进动作",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "owner": {
    "meaning": "责任人",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "assessment_rule": {
    "meaning": "定性或已选成熟度规则及出处",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "rating": {
    "meaning": "未选规则时not-scored",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  },
  "evidence_refs": {
    "meaning": "原始材料ID",
    "value_rule": "原料ID与数据版本明确；组织规则显式注明；未知保留缺口。",
    "definition_origin": "guide-derived-project-operational-convention"
  }
}

| 关系 | 起点 → 终点 | 语义 |
| --- | --- | --- |

## 分析步骤

1. 按六维访谈并核查已开展活动
2. 以七高层功能/35详细功能作非穷尽检查参照，按范围裁剪
3. 区分缺证、未开展和有效执行
4. 只有项目选择成熟度模型后才评分，公开规则来源
5. 把缺口转为有责任和验收依据的改进

## 输出、检查与误读

- 实际分析记录和结论
- 未决项、责任及动作
- 稳定对象ID、来源与实际view_id

- 六维评估不等于七高层功能的一一映射
- 源文未给等级/权重/合格线，不能默认ACMM或自造评分
- 参加宣导或发布政策不能自动证明能力成熟

- 六维评估不等于七高层功能的一一映射
- 源文未给等级/权重/合格线，不能默认ACMM或自造评分
- 参加宣导或发布政策不能自动证明能力成熟


## 视图和交付物

- [数字可持续能力六维评估](../profiles/sustainability-capability-assessment-default.md)

- [capability-assessment](../deliverables/capability-assessment.md)
- [tailored-architecture-framework](../deliverables/tailored-architecture-framework.md)


## 反例与修改示例

```json
{
  "counterexample": {
    "input": "无评分模型却给成熟度3/5",
    "expected": "unsourced-maturity-rating"
  },
  "modification_example": {
    "change": "环境职责经确认并有首次评审记录",
    "expected": "治理当前证据更新、缺口缩小，但六维仍无数字评分"
  }
}
```

## 可编辑示例与调用

[原料、分析、修改与反例能力包](../capability-addenda/sustainability-capability-assessment.md)

以下片段包含全部选择对象与关系；宿主模型提供五维语境。参考内容和虚构项目内容均不等于真实批准。

```json
{
  "notice": "虚构澄源服务企业可持续ICT案例；全部数据、角色与供应商证据为演示，不是排放因子建议。",
  "sources": [
    {
      "id": "src-sustainability-capability-assessment-default",
      "kind": "example",
      "description": "虚构澄源服务企业可持续ICT案例；全部数据、角色与供应商证据为演示，不是排放因子建议。 材料组 capability",
      "locator": "examples/addenda/sustainability/raw-business-materials.json#capability"
    }
  ],
  "entities": [
    {
      "id": "sustainability-capability-assessment-default-1",
      "type": "guide:sustainability_capability",
      "name": "战略",
      "attributes": {
        "dimension": "战略",
        "reference_functions": [
          "制定并推展可持续信息系统战略"
        ],
        "current_evidence": "董事会愿景已发布",
        "target_need": "职能级目标与责任",
        "gap": "职能目标未分配",
        "action": "由业务/CSR/ICT细化目标",
        "owner": "发起人",
        "assessment_rule": "G242 §5.2六维；企业未选评分模型，使用证据缺口评估",
        "rating": "not-scored",
        "evidence_refs": [
          "CA-01"
        ]
      },
      "evidence": [
        "src-sustainability-capability-assessment-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "sustainability-capability-assessment-default-2",
      "type": "guide:sustainability_capability",
      "name": "治理",
      "attributes": {
        "dimension": "治理",
        "reference_functions": [
          "治理转型"
        ],
        "current_evidence": "现有架构委员会不含环境职责",
        "target_need": "环境评审、债务与例外流程",
        "gap": "职权与准则未更新",
        "action": "修订现有委员会职责",
        "owner": "架构委员会流程负责人",
        "assessment_rule": "G242 §5.2六维；企业未选评分模型，使用证据缺口评估",
        "rating": "not-scored",
        "evidence_refs": [
          "CA-01"
        ]
      },
      "evidence": [
        "src-sustainability-capability-assessment-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "sustainability-capability-assessment-default-3",
      "type": "guide:sustainability_capability",
      "name": "业务/数据/应用/技术架构",
      "attributes": {
        "dimension": "业务/数据/应用/技术架构",
        "reference_functions": [
          "架构并构建可持续信息系统",
          "运营可持续信息系统"
        ],
        "current_evidence": "数据删除期限已提出",
        "target_need": "全栈及全生命周期考虑",
        "gap": "终端/外包生命周期未检验",
        "action": "把设备、软件与外包纳入设计检查",
        "owner": "架构负责人",
        "assessment_rule": "G242 §5.2六维；企业未选评分模型，使用证据缺口评估",
        "rating": "not-scored",
        "evidence_refs": [
          "CA-02"
        ]
      },
      "evidence": [
        "src-sustainability-capability-assessment-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "sustainability-capability-assessment-default-4",
      "type": "guide:sustainability_capability",
      "name": "文化",
      "attributes": {
        "dimension": "文化",
        "reference_functions": [
          "发展可持续数字文化"
        ],
        "current_evidence": "两场全员宣导",
        "target_need": "全员理解与角色技能",
        "gap": "采购/核算岗位缺专项技能",
        "action": "按角色训练并验证应用",
        "owner": "HR/培训负责人",
        "assessment_rule": "G242 §5.2六维；企业未选评分模型，使用证据缺口评估",
        "rating": "not-scored",
        "evidence_refs": [
          "CA-02"
        ]
      },
      "evidence": [
        "src-sustainability-capability-assessment-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "sustainability-capability-assessment-default-5",
      "type": "guide:sustainability_capability",
      "name": "数字环境足迹度量",
      "attributes": {
        "dimension": "数字环境足迹度量",
        "reference_functions": [
          "从摇篮到坟墓度量",
          "运营可持续信息系统"
        ],
        "current_evidence": "只有自营机房电力台账",
        "target_need": "制造/运行/退出/云边界完整",
        "gap": "制造回收云资料不全",
        "action": "完善清单和供应方数据契约",
        "owner": "环境核算负责人",
        "assessment_rule": "G242 §5.2六维；企业未选评分模型，使用证据缺口评估",
        "rating": "not-scored",
        "evidence_refs": [
          "CA-03"
        ]
      },
      "evidence": [
        "src-sustainability-capability-assessment-default"
      ],
      "certainty": "assumed"
    },
    {
      "id": "sustainability-capability-assessment-default-6",
      "type": "guide:sustainability_capability",
      "name": "生态系统",
      "attributes": {
        "dimension": "生态系统",
        "reference_functions": [
          "与客户/提供方/伙伴/主管部门互动"
        ],
        "current_evidence": "供应商愿给用电",
        "target_need": "端到端服务足迹透明度",
        "gap": "无设备Scope3承诺",
        "action": "采购纳入数据和复评条款",
        "owner": "采购负责人",
        "assessment_rule": "G242 §5.2六维；企业未选评分模型，使用证据缺口评估",
        "rating": "not-scored",
        "evidence_refs": [
          "CA-03"
        ]
      },
      "evidence": [
        "src-sustainability-capability-assessment-default"
      ],
      "certainty": "assumed"
    }
  ],
  "relationships": [],
  "view": {
    "id": "v-sustainability-capability-assessment-default",
    "artifact_id": "sustainability-capability-assessment",
    "profile_id": "sustainability-capability-assessment-default",
    "title": "数字可持续能力六维评估",
    "entity_ids": [
      "sustainability-capability-assessment-default-1",
      "sustainability-capability-assessment-default-2",
      "sustainability-capability-assessment-default-3",
      "sustainability-capability-assessment-default-4",
      "sustainability-capability-assessment-default-5",
      "sustainability-capability-assessment-default-6"
    ],
    "relationship_ids": [],
    "analysis": "把CA-01至03按六维记录事实和改进；七高层功能组多对多关联，不把七组当七级，也不移植ACMM评分。",
    "legend": "虚构记录；计划、实绩、建议、授权和批准分别表述。空缺不等于零或已接受。"
  },
  "raw_input_group": "capability"
}
```

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --artifact sustainability-capability-assessment --layout adaptive --out output --render
```

单项请求只生成该选择；同族多视图用独立view_id。
