# G178/fig4-2 · 招聘员工价值流

> 当前图示解析：[Markdown](../../architecture/diagrams/G178/fig4-2.md) · [JSON](../../architecture/diagrams/G178/fig4-2.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G178e.pdf`；SHA-256：`517130a041a8d956b2868dc39d570b84e2d80c64709e4c1368f9747388a3a026`。

## 原图 · PDF 第 20 页

![英文原图](../assets/G178/fig4-2-p0020.png)

PDF 坐标：`[48.2, 126.9, 563.8, 210.0]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
‘eT Ooen ue
Recruit Employee
Define
Communicate
Assess
Interview
Onboard
Position
Position
Candidates
>
X
»
Responses
X
y
Employee
y,
```

## 概要（历史解释；局部修正见上）

“招聘员工”价值流由 5 个依次相接的阶段组成：定义岗位→发布职位→评估应聘→面试候选人→入职。

## 目的（历史解释；局部修正见上）

第 4.2 节用它展示一轮轮迭代建模后得到的价值流图：业务利益相关者与主题专家先画草案，经业务架构师指导细化，得到只含阶段的价值流。随后的步骤都以它为基础：表 4-4 为每个阶段补充定义、参与利益相关者和价值项，图 4-3 把业务能力映射到这 5 个阶段，图 4-4 再做热力图。与图 1-1 的零售例子不同，这是一个内部触发、创造内部业务价值的价值流。

## 阅读顺序（历史解释；局部修正见上）

先读外框左上角的价值流名称“Recruit Employee（招聘员工）”，再从左到右读框内 5 个 V 形箭头，每个箭头是一个价值流阶段，箭头尖端嵌进下一个箭头的缺口表示紧接的先后顺序。图中没有连线、利益相关者、能力或流程。

## 关键含义（历史解释；局部修正见上）

- 价值流定义（表 4-3）：识别并聘用合适合格员工的活动；触发方利益相关者是想填补特定岗位的招聘经理；价值是与岗位匹配、快速聘用并高效工作的新员工。
- 5 个阶段依次为：定义岗位 → 发布职位 → 评估应聘 → 面试候选人 → 入职；阶段名采用“动词—名词”短语。
- 阶段通过退出/进入标准首尾衔接（表 4-4）：识别招聘需求 → 职位已发布 → 选出合格回应 → 作出录用决定 → 员工完成入职。
- 价值流图只描述产生预期业务影响的阶段，不规定执行阶段所需的流程、角色、信息或技术，也独立于所需的业务能力和对现状表现的评估（正文第 4.2 节）。
- 本图是迭代建模的结果：第一轮可能发现缺少能覆盖端到端的专家，需要在业务架构师指导下反复细化后才得到。
- “入职”阶段在表 4-4 中被描述为发出录用通知后触发一个内嵌的价值流，覆盖让员工融入工作环境的全部活动；第 4.3 节的热力图分析据此提出要新建一个从属价值流（图 4-4）。
- 本价值流是第 4.2、4.3 节能力映射（图 4-3）与热力图（图 4-4）的底图；正文说明它最早出自《TOGAF 系列指南：业务能力》。

## 层级（历史解释；局部修正见上）

两层。第 0 层是外框代表的“招聘员工”价值流；第 1 层是框内的 5 个价值流阶段，通过视觉包含表达“价值流由价值阶段组成”。“入职”阶段内嵌的从属价值流在本图中没有画出。

## 线条含义（历史解释；局部修正见上）

图中没有独立的连线。V 形箭头本身就是阶段，箭头尖端嵌进下一阶段的缺口，表示先后顺序（关系清单中记为 sequence）；外框只表示这些阶段属于同一条价值流（用 parent 表示）。

## 易误读点（历史解释；局部修正见上）

- V 形箭头是阶段本身，不是阶段之间的流转线。
- 阶段首尾相接不表示必须连续走完，每个阶段之后都可能停止（第 2.2 节）。
- 阶段不是部门职责或业务流程，图中没有表示由谁执行或怎样执行。
- 第 5 阶段原图为“Onboard Employee”；中文稿引用的 SVG 写成“Onboard”，并加了一行原图没有的注释。

## 元素

```json
[
  {
    "id": "vs_recruit",
    "label_en": "Recruit Employee",
    "label_zh": "招聘员工（价值流）",
    "type": "value_stream",
    "parent": null,
    "level": 0,
    "position": "外框左上角",
    "description_zh": "触发方利益相关者：想填补特定岗位的招聘经理；价值：与岗位匹配、快速聘用并高效工作的新员工（表 4-3）。"
  },
  {
    "id": "st_define",
    "label_en": "Define Position",
    "label_zh": "定义岗位",
    "type": "value_stream_stage",
    "parent": "vs_recruit",
    "level": 1,
    "order": 1,
    "description_zh": "确定用人需求、识别技能与资格并形成文档；参与者：招聘经理、HR 招聘负责人；进入：识别出人员变动；退出：识别招聘需求；价值项：节省搜寻候选人的时间与费用（表 4-4）。"
  },
  {
    "id": "st_communicate",
    "label_en": "Communicate Position",
    "label_zh": "发布职位",
    "type": "value_stream_stage",
    "parent": "vs_recruit",
    "level": 1,
    "order": 2,
    "description_zh": "向可用的招聘门户和招聘活动刊登、发布或发送职位信息；参与者：招聘专员；退出：职位已发布；价值项：找到合格候选人的可能性高。"
  },
  {
    "id": "st_assess",
    "label_en": "Assess Responses",
    "label_zh": "评估应聘",
    "type": "value_stream_stage",
    "parent": "vs_recruit",
    "level": 1,
    "order": 3,
    "description_zh": "接收、登记、分发并评分候选人回应及附加核查；参与者：招聘经理、招聘专员；退出：选出合格回应；价值项：有效利用面试时间与成本。"
  },
  {
    "id": "st_interview",
    "label_en": "Interview Candidates",
    "label_zh": "面试候选人",
    "type": "value_stream_stage",
    "parent": "vs_recruit",
    "level": 1,
    "order": 4,
    "description_zh": "与候选人沟通、安排交通、排期并开展面试；参与者：招聘经理、候选人、员工；退出：作出录用决定；价值项：选出最合适的员工。"
  },
  {
    "id": "st_onboard",
    "label_en": "Onboard Employee",
    "label_zh": "入职",
    "type": "value_stream_stage",
    "parent": "vs_recruit",
    "level": 1,
    "order": 5,
    "description_zh": "发出录用通知并触发内嵌的价值流，处理员工融入工作环境的全部活动；参与者：员工、HR、安全、设施、财务、IT；进入：已作出录用决定；退出：员工完成入职；价值项：生产力就绪、能满足业务承诺的员工队伍。"
  }
]
```

## 关系

```json
[
  {
    "from": "st_define",
    "to": "st_communicate",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward",
    "description_zh": "V 形箭头首尾相接"
  },
  {
    "from": "st_communicate",
    "to": "st_assess",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "st_assess",
    "to": "st_interview",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  },
  {
    "from": "st_interview",
    "to": "st_onboard",
    "type": "sequence",
    "explicit": true,
    "line": "solid",
    "arrow": "forward"
  }
]
```

## 有序流程

```json
[
  {
    "id": "f_recruit",
    "kind": "sequence",
    "name_zh": "招聘员工价值流",
    "steps": [
      "st_define",
      "st_communicate",
      "st_assess",
      "st_interview",
      "st_onboard"
    ],
    "description_zh": "每个阶段之后都可能停止（第 2.2 节）。"
  }
]
```

## 图例

```json
[
  {
    "symbol": "深灰色外框 + 左上角粗体名称",
    "meaning_zh": "一条价值流（整体）",
    "explicit": false
  },
  {
    "symbol": "浅灰 V 形箭头（chevron）",
    "meaning_zh": "价值流阶段",
    "explicit": false
  },
  {
    "symbol": "箭头首尾相接、从左到右",
    "meaning_zh": "阶段的先后顺序；前一阶段的退出标准是后一阶段的进入标准",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "LR",
  "description_zh": "一个横向的深灰色长框，左上角是价值流名称，框内一行 5 个首尾相接的浅灰 V 形箭头，从左到右；右上角有很小的“© The Open Group”。"
}
```

## 相关图

```json
[
  {
    "target": "G211/fig5-3",
    "relation": "based_on",
    "note_zh": "正文说明“招聘员工”价值流最早出自《业务能力》指南；G211 图 5-3 用相同的 5 个阶段名并已叠加能力映射，本图只保留阶段"
  },
  {
    "target": "G233/figC-1",
    "relation": "related",
    "note_zh": "G233 图 C-1 也是“招聘员工”价值流，但阶段划分和命名不同（定义岗位、发布空缺职位、筛选最终候选人、发出录用、候选人入职），并用 ArchiMate 展开能力实例"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "表 4-4 中“定义岗位”的参与者在 PDF 中分两行排为“HR Recruitment / Lead”，按版式理解为一个角色“HR 招聘负责人”；中文稿译成“人力资源、招聘负责人”两个角色，两种读法都有可能。"
  ],
  "analyzed_from": [
    "英文 PDF 第 20 页原图截图（220 dpi）",
    "英文 PDF 第 18–22 页正文（表 4-3、表 4-4、第 4.3 节）",
    "中文稿 G178e_价值流.md 第 226–252 行",
    "figs/g178_fig4-2.svg 源码",
    "G211/fig5-3、G233/figC-1 原图截图（仅用于核对图间关系）"
  ],
  "date": "2026-10-31"
}
```

## 结构校验

```json
{
  "graph_integrity_issues": [],
  "location_available": true,
  "caption_page_match": true,
  "visual_review_scope": "not-reverified-this-build",
  "all_source_pages_valid": true
}
```
