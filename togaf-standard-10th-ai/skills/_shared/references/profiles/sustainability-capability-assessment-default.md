# 数字可持续能力六维评估

`profile_id`: sustainability-capability-assessment-default；`artifact_id`: sustainability-capability-assessment；主责：[togaf-ea-capability](../../../togaf-ea-capability/SKILL.md)。

来源：G242 §3.2、§5.2表5-1。

## 构图与定义状态

表示族：`catalog`；输出：`table`。规范版本：2.1-addenda。

{
  "id": "sustainability-capability-assessment-default",
  "version": "2.1-addenda",
  "source_verified": false,
  "layout_notes": "源正文方法的项目字段表；没有原图复刻声明。"
}

来源结构核实、输出可读性及业务正确性是独立验收。source_verified=false不能被成功生成或文件名覆盖。

## 必需模型内容

对象类型：guide:sustainability_capability。关系类型：。

```json
{
  "entities": {
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
  },
  "relationships": {}
}
```

缺少模型内容时输出带ID的错误或缺口，不能静默改成通用流程图。

## 检查与追溯

- 六维评估不等于七高层功能的一一映射
- 源文未给等级/权重/合格线，不能默认ACMM或自造评分
- 参加宣导或发布政策不能自动证明能力成熟

每次生成记录对象、关系、必要属性如何表达；PNG/SVG与模型及渲染器版本同时保留。

## 完整示例片段

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

## 生成

```sh
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile sustainability-capability-assessment-default --layout reference --out output/reference --render
python "$TOGAF_SKILLS/_shared/scripts/generate.py" model.json --profile sustainability-capability-assessment-default --layout adaptive --out output/adaptive --render
```

用`--view`精确选择实例；文件按view_id命名，交付物引用实际视图。
