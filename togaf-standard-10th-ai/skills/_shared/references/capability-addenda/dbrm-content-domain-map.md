# DBRM与元模型及架构域

制品族 `digital-business-reference-tailoring`；规范 `dbrm-content-domain-map`。来源是参考分类/映射，不是本项目已实现事实。

## 必要输入与缺口

本地职责/客户/决策问题、范围、时点、资料证据和所选参考路径。源空格/破折号保留；本地缺数据写unknown及下一步，不伪造成熟度/金额/批准。

## 元素、属性、关系

- `source_table`：来源表ID，各轴独立
- `source_row_id`：源表稳定行ID，项目补充行单列
- `raw_cells`：源空格/破折号原样保留
- `resolved_cells`：组内延续解释；不能变造源标签
- `source_mapping_status`：local-body-mapping/not-specified/project-only
- `local_object_ids`：本地资料稳定ID
- `local_mapping_status`：项目候选映射/未评估，不是源结论
- `local_evidence`：本地观察依据或unknown
- `tailoring_reason`：本地选择理由
- `review_action`：下一步核实
- `reference_identity`：参考/项目身份边界

关系：{}

## 分析步骤

1. 读取对应自包含源表，保留raw_cells
2. 按表独立维度解释组内延续，保留来源—/空缺
3. 建立本地映射及依据；未知不变不适用
4. 项目补充映射另标project-only，不反写来源

## 输出与评审

table规范完整输出逐行/逐对象字段；图形仅使用显式分类关系，输出可编辑SVG/PNG并核对coverage。保持artifact_id/profile_id/view_id独立。
- 源行/原值不能被项目变更覆写
- DBRM域、架构域、ADM、全景层级互不替代
- 表6-2运营管理与正文服务交付管理差异保留
- 表未列G/H不意味着无适用关系

## 完整实例

原业务材料（历史材料已清理） → 分析（历史材料已清理） → 初始模型（历史材料已清理）。修改（历史材料已清理）依据R11，反例（历史材料已清理）逐规范带ID错误。

显式调用：`generate.py model.json --profile dbrm-content-domain-map --layout reference|adaptive --out output`。只请求本规范时不要求全量产出。

## 可携带来源

- `references/source-tables/dbrm-reference-mappings.json`
- G21H 表6-2

生成和本地检查不替代源图视觉或独立业务评审。G21D12/11冲突、G21H未来安全成熟度、破折号及术语差异均在可携带表中，不靠外部源文件运行。
