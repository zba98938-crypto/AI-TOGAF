# 把 ADM 阶段落实到架构制品

完整 ADM、跨域协同、阶段退出评审或制品变更时使用。本规范连接既有阶段合同、领域技能、制品定义、方法与生成工具。单张制品仍直接使用主责技能。

依据本地 G186 §3.3.1 的利益相关者/关注点/视图、§5.1 的视点选择与存储库、§6 的架构开发及 G248 附录 A/B 的制品/容器式交付物。JSON、映射规则和 CLI 是项目操作约定；候选清单不成为官方必交清单。

## 从决策问题开始

先明确谁要作什么决定、关注什么问题、需求与范围是什么，然后选择视点。目录用于统一对象及属性；矩阵用于检查有类型的跨对象关联；图用于解释结构、行为、边界、时序或部署。视图是模型的具体表示，交付物组织多个视图和分析，ABB 规定能力及约束，SBB 是具体实现候选。它们不能因名称接近互相代替。

运行 `architecture_delivery.py catalog --phase C` 获取该阶段主责技能、活动、判据、制品族、可选规范和分析方法。全部目录覆盖现有 192 族、290 规范入口、72 方法与 22 交付物；实际数量随注册表计算。

每个阶段的 `guide_usage` 列出指南“结合 ADM 使用”章节明确写到的用法（G190 §6、G206 §6、G211 §6、G21I §4–13、G212 §6、G186 §12 与附录 D、G249 §4、G176 §9–11），数据在 [adm-phases.json](adm-phases.json) 的 `guide_usage`。这些是候选用法和定位，不是该阶段的强制输出。`Requirements` 表示持续需求工作，`Review` 表示跨阶段评审，二者不是新增 ADM 阶段。可跨阶段复用；按目的选择必要成果。

读所选制品和规范定义，按其必需输入、实体类型、关系语义、分析步骤与检查问题开展工作。分析方法注册与执行证据分开；填入 `method_ids` 只记录选择，不代表已经执行。缺业务信息的视图可以保持草稿，不能凭模板填出业务结论。

## 建立本次工作映射

使用集合已安装依赖的 Python，从项目根运行：

```sh
skills/_shared/.venv/bin/python skills/_shared/scripts/architecture_delivery.py catalog --phase C
skills/_shared/.venv/bin/python skills/_shared/scripts/architecture_delivery.py init \
  --model project/model.json --cycle project/adm-cycle.json --phase C \
  --out project/architecture-delivery.json
```

`init` 为所选阶段的每项退出判据创建待规划工作项，保留未批准状态。省略 `--phase` 则为未裁剪阶段建立映射。根据任务合并或拆分工作项；不为每项判据强制创建独立文档。

计划遵循 [architecture-delivery.schema.json](../schemas/architecture-delivery.schema.json)，填写：

- `concerns`：稳定 ID、决策问题、共享模型中的 `stakeholder` ID，以及相关普通/安全/分析需求 ID。尚未形成需求的早期关注点可空列需求，不能以此宣称需求完整。
- `phase_work`：阶段和当前迭代 ID。阶段重开后保留旧计划，另存新计划并更新迭代及相关映射。
- `items`：判据 ID、关注点 ID、模型中实际 `view_ids`/交付物实例 `deliverable_ids`、选用的注册 `method_ids` 和选择理由。同一视图可回应多个关注点，但须解释其回答和限制。
- 阶段 `output_refs`：显式绑定本次选择的视图/交付物；方法候选、制品族 ID、文档名称不能代替模型实例 ID。

工作项示例（需替换为实际模型 ID）：

```json
{
  "id": "C-data-ownership",
  "criterion_ids": ["data-architecture", "data-application-alignment"],
  "concern_ids": ["customer-data-authority"],
  "view_ids": ["customer-information-map", "customer-application-data"],
  "deliverable_ids": [],
  "method_ids": [],
  "rationale": "信息地图定义客户信息责任边界，应用/数据矩阵检查读写及权威来源；二者复用相同数据和应用 ID。"
}
```

需求可以直接出现在所选成果中，或用有证据且同范围/状态的 `specifies`、`satisfies`、`requires_control` 等有类型关系分配给成果中的设计对象。任意图可达和泛化 `traces_to` 不能代替设计分配。结构关联不证明语义满足。

## 分析、生成与检查

先按领域技能完成模型分析，运行 `validate.py`，需要比较时运行 `analyze.py --compare`，需求变更运行 `requirements_trace.py`。选择实际视图/交付物执行 `generate.py`；图形加 `--render`。不要因为阶段候选清单而运行全量生成。

```sh
skills/_shared/.venv/bin/python skills/_shared/scripts/architecture_delivery.py report \
  --model project/model.json --cycle project/adm-cycle.json \
  --plan project/architecture-delivery.json --products project/output \
  --out project/architecture-delivery-check.md

skills/_shared/.venv/bin/python skills/_shared/scripts/adm.py check \
  --model project/model.json --cycle project/adm-cycle.json \
  --delivery-plan project/architecture-delivery.json --products project/output \
  --require-complete
```

检查分别报告：

| 结果 | 意义 |
| --- | --- |
| `structurally_linked` | 关注点、利益相关者、判据、当前迭代、成果及需求分配已形成有效结构映射 |
| `products_current` | 有选择的成果确已生成，模型、注册表、运行依赖、保存文件指纹和表达记录匹配；图形已渲染 |
| `selected_adm_records_complete` | 所选阶段的退出判断、需求复核和信息依赖记录闭合 |
| `business_acceptance` | 本工具始终 `not-assessed`；真实接受由实际评审和决策证据决定 |

普通 `check` 因无效配置/引用返回非零，允许如实记录草稿缺口；`--strict` 同时因映射缺口、成果缺口或所选阶段记录未闭合返回非零。`adm.py --require-complete` 还检查整个周期；启用成果计划时，所有适用阶段都应建立映射，否则返回 `delivery_unmapped_phase_ids` 并保持全周期未闭合。命令只读源模型和周期，不覆盖既有报告。

当前成果检查使用整个生成快照，模型任意变化后可将所需成果重生成到新目录。阶段输入是否失效仍按 `adm.py` 的相关引用闭包判断，不能把“成果快照需更新”误读为“所有阶段必须重审”。加入新 Schema 会使旧输出的运行依赖快照过期，应重新执行生成，不能改旧哈希冒充复跑。

## 实质评审

机器关联完整之后，逐关注点评审视图是否足以支持决定：边界、粒度、现状/候选/目标/过渡是否可比；目录对象、矩阵方向和代码、图形关系是否一致；负面影响、风险、硬约束、备选及取舍是否说清；未知、假设与来源解释是否显式保留。交付物须有实际章节内容，legacy 或未绑定章节不计完整组装。图形还需观察箭头、分组、中文可读性和裁切。

B/C/D 的差距要解释如何影响其他域；E/F 将选择的差距分配到工作包、可运营过渡与实施计划；G 核对实施证据与约束并处置偏离；H 比较实际价值与期望，再决定维护、局部重开或新周期。计划、模拟、生产实施和价值实现分别记录。

可运行案例见 ADM 成果联动案例（历史材料已清理），本地来源名称对照用 `compare_togaf_delivery.py --source-root 项目目录`，不能据名称全覆盖宣称正式定义或视觉等价。
