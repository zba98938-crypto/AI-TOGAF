# G186/fig4-2 · 半座桥

类型：`illustrative-photo`。作者在讲“支持项目的架构”时用这张照片把“完整性”变成可感知的形象：项目把桥墩、引桥、拱都建好了，却差最后一段跨过障碍，组织并没有真正前进，只是浪费资源。照片不是模型，是修辞。

英文 PDF 物理页：[44]。本页为架构语义分析，原文与原图分别保留。

## 原图与可编辑图

![PDF 第 44 页原图](../../../figures/assets/G186/fig4-2-p0044.png)

[完整 JSON](fig4-2.json) · [可编辑 Mermaid](fig4-2.mmd) · [仅关系图](fig4-2.relations.mmd) · [层级分解图](fig4-2.hierarchy.mmd)

图形重建表达语义，不复制源图布局。虚线表示解释、矩阵映射或分组关系，不自动表示不确定性的概率。

```mermaid
flowchart TB
  %% Semantic reconstruction; see original source image for exact layout.
```

## 架构分析

观察石桥在河中终止、未连接另一岸的可见景象；结合44页正文理解项目完整性比喻。照片不是架构模型，也不能单凭画面推断桥梁历史。

- 本图有 0 个具名或隐含元素、0 条关系和 0 条包含/分组记录。
- 源图为河中中断石桥的照片，可见石砌拱桥、河水、岸边植被及远处人物；没有文字标签、架构节点、箭头或数据表。
- 44页明确用半座桥比喻缺少完整交付的实施项目，照片本身不能证实桥是未施工完成、毁损或其他历史原因。

### 如何用于项目

- 围绕作者目的读取本图实体、分组与连线，并用对应原文限定其含义。
- 把参考模型与项目事实分开，实际范围、约束、值和责任须有项目证据。

### 结构所表达的逻辑

- 照片显示石桥在河中终止，桥上无信息标签。
- 正文的半座桥是项目比喻：投入资源却不能完成跨越障碍的最后一部分，不是值得采用的阶段性交付建议。
- 画面中的桥、河、树和人物是摄影内容，不赋予架构节点或业务关系。

## 上下级与包含

无层级：单张照片，画面中只有桥、河、树木与少量人物，没有框、泳道或分组。

|父项|子项|层级类型|依据与解释|
|---|---|---|---|
|—|—|无视觉包含|关系中明确的组成/特化见 JSON semantic_hierarchy。|

## 全部元素与角色

|元素ID|原文名称|类型|含义|直接父项|深度|
|---|---|---|---|---|---|

## 全部关系

没有任何连线或箭头。画面中的桥面本身形成一条从左下到右中的视觉引导线，断口就是视觉终点；这是摄影构图，不是图表的语义连线。

|主体|语义关系|客体|显式线/隐式|原文标签|依据|
|---|---|---|---|---|---|

## 误读检查

- 不能从照片判断该桥是建设中、未完工还是历史残存；本文仅借其外观比喻。
- 不能把照片视作实际项目架构图、工程规格或建议方案。

## 原文证据

### [PDF 第 44 页](../../../documents/G186.md#page-44)

> Architecture to Support Project is the first time you can see that work to effect change is about to be done. Before the release of funding to an Implementation Project, no change is going to happen. The classic alignment of this purpose in Phase F is the development of an Implementation Project business case or Implementation Project charter.
> Architecture work facilitates the organization’s final decision-making about the use of funding and other scarce change resources. The tendency of implementation teams to focus exclusively on the creation of tactical business value needs to be balanced with the roadmap purpose and value against the target. It is common for implementation teams to sacrifice substantive organization value to provide what might be considered “decorative” features to the operational team the implementers work with.

## 来源与分析状态

所有元素/关系均有来源定位；未把历史解释重命名为本轮逐线视觉确认。源图与语义图是两种视图，布局不证明汇报或因果。

源 PDF SHA-256：`ed1c26faba5023a8d1b32b0ec893d75a3bb1d7a6508e99fa56ded079585d922a`。

源图记录：[原始解释与转录](../../../figures/G186/fig4-2.json)。

```json
{
  "quality": {
    "graph_integrity": "checked",
    "semantic_analysis": "typed-graph-and-context-analysis",
    "visual_review": "source-content-audited",
    "notice_zh": "所有元素/关系均有来源定位；未把历史解释重命名为本轮逐线视觉确认。源图与语义图是两种视图，布局不证明汇报或因果。"
  },
  "source_uncertainty": {
    "confidence": "high",
    "uncertainties_zh": [
      "照片的拍摄地点与版权信息未在图内标注；据画面可辨认为法国阿维尼翁的圣贝内泽桥，但正文只称“半座桥”。",
      "图题后的脚注 [2] 在 PDF 中未见展开，无法确认照片来源。",
      "中文图为重新裁剪，边缘构图与英文原图略有差异，不影响比喻。"
    ],
    "analyzed_from": [
      "英文 PDF 第 44 页图 4-2 截图（220 dpi）",
      "英文 PDF 第 44 页正文",
      "中文稿 G186e_实践者方法_按TOGAF_ADM开发企业架构.md 第 444–452 行",
      "figs/g186e_fig4-2_en.png 与 figs/zh/g186e_fig4-2_zh.png"
    ],
    "date": "2026-10-31"
  },
  "source_conflicts": []
}
```
