# BI业务功能参考覆盖

主责 `togaf-requirements`；既有制品 `bi-requirements-profile`；视图规范 `bi-business-function-coverage`。

必要输入：原始业务访谈/观察、组织与时间范围、参考功能或目标、责任和实际证据。关键内容缺失时记录unknown与补证行动，不补造参数或通过结论。

## 决策与关注点

海岚只出示U1/U2用途待办及拟每周复核模型的计划。其余业务功能没有访谈/运行证据；不能因软件已采购就声称覆盖。54源表行包括宏观参考行与子功能，全部逐行登记未知/已见/计划。

适用ADM：预备/A–D形成范围、角色和需求，E/F据价值和缺口选择演进，G/H持续验证运营与变更。不是唯一阶段归属。

## 元素与输出语义

| 字段 | 含义 |
|---|---|
| reference_id | 稳定参考行ID |
| reference_kind | 业务/应用参考功能 |
| reference_name | 源行功能名 |
| reference_definition | 源行完整含义 |
| reference_group | 源参考分组，不是部署边界 |
| reference_level | 宏观/独立高层/组内子功能，保留源表粒度 |
| reference_scope | 源表分组适用范围，不从标签隐含推断 |
| source_locator | 源表行 |
| reference_identity | reference-only，不能当实现对象 |
| project_scope | 评估范围与时间 |
| coverage_status | evidenced-in-example/planned/unknown/out-of-scope-with-reason |
| implementation_ref | 真实/计划项目实现或unknown |
| evidence_detail | 范围内观察，不由名称推断 |
| gap_action | 不足/不适用理由及下一步 |
| source_uncertainty | 本地翻译/缺失来源边界 |

## 分析与质量检查

1. 加载随技能携带的完整源表，保留参考分组/ID/出处
2. 限定项目范围和时点，逐项寻找组织活动或实际应用功能证据
3. 区分已见、计划、未知和有理由不适用
4. 不得以宏观组或产品名称推断子项覆盖
5. 对缺口形成具体补证/实现/复评行动，不合成成熟度分数

- 源表ID全集覆盖且不重复
- 已见必须有具体实现/证据，计划不算已实现
- 不适用必须有范围理由
- 参考表行不是软件组件或独立制品
- 保留本地翻译不确定

输出可编辑模型JSON与完整Markdown表及覆盖台账；命令支持reference/adaptive，但表格不冒充图形SVG/PNG视觉验收。关系逐行表示源→目标、类型及证据，不能只留在JSON。

## 完整案例

原始材料（历史材料已清理） → 分析（历史材料已清理） → 模型（历史材料已清理）。
追加业务材料（历史材料已清理）与反例（历史材料已清理）。

## 来源、误读与追溯

- G238 §2.2、表4-2
- 表格覆盖评估不是源图嵌套地图视觉验收。
- 完整参考表不代表项目全部功能实现；未知不计通过。

随技能携带[17项目标](../../examples/addenda/operations/references/bi-goals.json)、[BI业务功能](../../examples/addenda/operations/references/bi-business-functions.json)、[BI应用功能](../../examples/addenda/operations/references/bi-application-functions.json)、[C-MDM业务功能](../../examples/addenda/operations/references/mdm-business-functions.json)、[C-MDM应用功能](../../examples/addenda/operations/references/mdm-application-functions.json)。这些是本地正文参考表，不是已部署组件。

调用：`generate.py MODEL --profile bi-business-function-coverage --layout reference --out OUTPUT`；可用`--view`选择实例。两种布局同一表格语义，不降级成通用流程图。

运行示例不依赖原工作区原始文档；只有一次性审计提取脚本需要原文。
