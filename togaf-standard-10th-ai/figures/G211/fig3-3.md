# G211/fig3-3 · 人力资源管理能力分解

> 当前图示解析：[Markdown](../../architecture/diagrams/G211/fig3-3.md) · [JSON](../../architecture/diagrams/G211/fig3-3.json)。包含本轮修正与证据状态；下方保留原图和历史转录。

内容角色：`source-figure-with-historical-interpretation`。历史图意解释保留其来源；OCR 不是已验证文字，布局不是业务关系。

原文：`togaf-standard-10th/G211e.pdf`；SHA-256：`93fa7ac115956d34c0ad2161c46a5fd01cbc972d5f85a0f19f2f5b9d8c0a2b34`。

## 原图 · PDF 第 21 页

![英文原图](../assets/G211/fig3-3-p0021.png)

PDF 坐标：`[151.3, 303.4, 460.7, 644.1]`；裁剪来源：`historical-bbox-checked-within-original-page`。

### 图内文字（数字提取）

原图该区域未提供可提取的数字文本。

### 图内文字（OCR，待核对）

```text
Human Resource Management
Human Resource Performance Determination
Human Resource Performance Threshold Setting
Human Resource Performance Threshold Determination
Human Resource Performance Constraints Determination
[Human Risk Management
Human Resource/Competency Matching
Human Resource/Competency Assessment
[HumanResoureProfieManagement
| Human Resource History Management
```

## 概要（历史解释；局部修正见上）

一级能力“人力资源管理”分解为 7 项二级能力，其中绩效测定再分出 3 项三级能力。

## 目的（历史解释；局部修正见上）

示范第 3.2.2 节的“分级”：把顶层（一级）能力逐层分解，以适合不同受众的细节程度沟通。高管可能只看一级视图，架构师和规划者需要更细的粒度；实践中常见 3–6 级。

## 阅读顺序（历史解释；局部修正见上）

外层蓝框的粗体标题是一级能力“人力资源管理”。框内纵向排列的 7 个蓝框是二级能力，每框首行是名称；框内缩进的小字是该二级能力下的三级能力。上下级完全由框的嵌套和缩进表达，没有连线；7 个二级框的上下次序没有含义。

## 关键含义（历史解释；局部修正见上）

- 7 项二级能力：人力资源认证与授权、人力资源绩效测定、人员风险管理、人力资源薪酬管理、人力资源/胜任力匹配、人力资源档案管理、人力资源历史管理。
- “人力资源绩效测定”分解为 3 项三级能力：绩效阈值设定、绩效阈值测定、绩效约束测定。
- “人力资源/胜任力匹配”下也缩进列出一项“人力资源/胜任力评估”；正文只提到绩效测定的 3 项三级能力，没有提这一项。
- 分解深度不均匀：只有部分二级能力继续向下分解；正文说明分解层数只取决于向目标受众传达信息、或支撑能力差距决策的需要。
- 能力名都围绕业务对象“人力资源（人员）”展开（认证授权、绩效、风险、薪酬、胜任力、档案、历史），符合第 2.1.1 节以业务对象为名词核心的命名约定；分解的是能力本身，不是 HR 部门的组织或流程。
- 本图 7 项与同文档图 5-3 中“人力资源管理”下出现的二级能力（胜任力管理、员工供需管理、职位广告、技能评估、福利/条款/薪酬管理、入职跟踪）基本不重合，只有薪酬一项近似；两图都是示例，正文没有说明二者的关系。

## 层级（历史解释；局部修正见上）

三级：一级能力“人力资源管理”（外框）→ 7 项二级能力（内框）→ 三级能力（内框中的缩进小字：绩效测定下 3 项，胜任力匹配下 1 项）。上下级只由嵌套和缩进表达。

## 线条含义（历史解释；局部修正见上）

图中没有连线。外框包含内框表示一级包含二级；内框中缩进的小字表示该二级能力下的三级能力。元素清单用 parent 记录这种包含关系。

## 易误读点（历史解释；局部修正见上）

- 二级框的上下排列不表示优先级或流程顺序。
- 缩进的小字是三级能力，不是对二级能力的说明文字。
- 原图第三项写作“Human Risk Management”（少了 Resource），按原图记录。
- 中文稿当前引用的 figs/g211_fig3-3.svg 换成了另一套通用 HR 职能，三级能力也不同，并画成连线错乱的树，不能据它理解本图。

## 元素

```json
[
  {
    "id": "c_hrm",
    "label_en": "Human Resource Management",
    "label_zh": "人力资源管理",
    "type": "capability",
    "parent": null,
    "level": 1
  },
  {
    "id": "c_hr_authn_authz",
    "label_en": "Human Resource Authentication and Authorization",
    "label_zh": "人力资源认证与授权",
    "type": "capability",
    "parent": "c_hrm",
    "level": 2,
    "order": 1
  },
  {
    "id": "c_hr_perf_determination",
    "label_en": "Human Resource Performance Determination",
    "label_zh": "人力资源绩效测定",
    "type": "capability",
    "parent": "c_hrm",
    "level": 2,
    "order": 2
  },
  {
    "id": "c_hr_perf_threshold_setting",
    "label_en": "Human Resource Performance Threshold Setting",
    "label_zh": "人力资源绩效阈值设定",
    "type": "capability",
    "parent": "c_hr_perf_determination",
    "level": 3,
    "order": 1
  },
  {
    "id": "c_hr_perf_threshold_determination",
    "label_en": "Human Resource Performance Threshold Determination",
    "label_zh": "人力资源绩效阈值测定",
    "type": "capability",
    "parent": "c_hr_perf_determination",
    "level": 3,
    "order": 2
  },
  {
    "id": "c_hr_perf_constraints_determination",
    "label_en": "Human Resource Performance Constraints Determination",
    "label_zh": "人力资源绩效约束测定",
    "type": "capability",
    "parent": "c_hr_perf_determination",
    "level": 3,
    "order": 3
  },
  {
    "id": "c_human_risk_mgmt",
    "label_en": "Human Risk Management",
    "label_zh": "人员风险管理",
    "type": "capability",
    "parent": "c_hrm",
    "level": 2,
    "order": 3
  },
  {
    "id": "c_hr_compensation_mgmt",
    "label_en": "Human Resource Compensation Management",
    "label_zh": "人力资源薪酬管理",
    "type": "capability",
    "parent": "c_hrm",
    "level": 2,
    "order": 4
  },
  {
    "id": "c_hr_competency_matching",
    "label_en": "Human Resource/Competency Matching",
    "label_zh": "人力资源/胜任力匹配",
    "type": "capability",
    "parent": "c_hrm",
    "level": 2,
    "order": 5
  },
  {
    "id": "c_hr_competency_assessment",
    "label_en": "Human Resource/Competency Assessment",
    "label_zh": "人力资源/胜任力评估",
    "type": "capability",
    "parent": "c_hr_competency_matching",
    "level": 3,
    "order": 1,
    "description_zh": "原图有，正文未提及。"
  },
  {
    "id": "c_hr_profile_mgmt",
    "label_en": "Human Resource Profile Management",
    "label_zh": "人力资源档案管理",
    "type": "capability",
    "parent": "c_hrm",
    "level": 2,
    "order": 6
  },
  {
    "id": "c_hr_history_mgmt",
    "label_en": "Human Resource History Management",
    "label_zh": "人力资源历史管理",
    "type": "capability",
    "parent": "c_hrm",
    "level": 2,
    "order": 7
  }
]
```

## 图例

```json
[
  {
    "symbol": "外层蓝框 + 左上粗体标题",
    "meaning_zh": "一级业务能力",
    "explicit": false
  },
  {
    "symbol": "内层蓝框（首行文字）",
    "meaning_zh": "二级业务能力",
    "explicit": false
  },
  {
    "symbol": "内框中缩进的小号文字",
    "meaning_zh": "三级业务能力",
    "explicit": false
  }
]
```

## 布局

```json
{
  "direction": "TB",
  "description_zh": "一个大外框，内部纵向排列 7 个等宽内框；第 2 个内框较高，内含 3 行缩进小字，第 5 个内框内含 1 行缩进小字。"
}
```

## 相关图

```json
[
  {
    "target": "G211/fig3-2",
    "relation": "detail_of",
    "note_zh": "本图是图 3-2 支撑层中一级能力“人力资源管理（HR Management）”的分解"
  },
  {
    "target": "G211/fig5-3",
    "relation": "related",
    "note_zh": "图 5-3 也在“人力资源管理”下列出二级能力，但与本图的 7 项基本不同"
  }
]
```

## 历史不确定性

```json
{
  "confidence": "high",
  "uncertainties_zh": [
    "二级、三级能力的中文译名由解析者拟定；中文稿只给出“人力资源绩效测定”一项。",
    "“人力资源/胜任力评估”按缩进记为三级能力；正文只说绩效测定下有三级能力，没有说明这一项。"
  ],
  "analyzed_from": [
    "英文 PDF 第 21 页原图截图（220 dpi）",
    "英文 PDF 第 21 页正文",
    "中文稿 G211e_业务能力.md 第 247–253 行",
    "figs/g211_fig3-3.svg 源码（文字与连线路径）"
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
