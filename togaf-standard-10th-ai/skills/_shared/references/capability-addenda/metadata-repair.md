# G234 元数据模板修复包

本包修复三个既有视图规范，不新增制品族或工作产品。业务图保留10组30项功能与4个角色，应用图保留6组24项功能。完整定义来自已携带的 `references/source-tables/metadata-functions.json`，生成不读取原工作区文档。

维护时运行 `python scripts/expand_metadata_views.py` 重建 `capability-addenda/metadata-repair.json`。该脚本只读取原始指南并写入本包与内部表，不改中央能力清单。由集成负责人运行 `python scripts/apply_capability_addenda.py capability-addenda/metadata-repair.json` 应用明确替换；后续运行共享索引同步。

项目使用仍调用 `generate.py model.json --profile metadata-business-function-map --layout reference --render --out output`，其余规范为 `metadata-application-function-map` 和 `metadata-three-part-solution`。同一模型可选多个视图。`--layout adaptive` 使用相同对象、关系和定义，只重排空间。

必要输入为业务范围、利益相关者、元数据需求及来源、功能适用性与裁剪理由、团队角色、现有或候选技术/数据模型/流程设计。先提炼需求，参照完整源功能表识别适用功能，再分开记录基线、目标和差距；来源参考条目不能自动标成企业现状。没有需求或裁剪理由时保持参考模型草案，缺失项按ID登记，不判定工具选型或治理成熟度通过。

层级需要显式关系：`decomposes` 表示职责/功能分解；`visually_contains` 表示视图范围分组。`g234:slot`、`reference_row`、`reference_column` 与 `g234:reference-order` 只决定布局，不能制造功能关系。修改分组时修改关系端点并保持原对象ID；功能名、完整定义、源表行、关注点和项目追溯随模型重新生成。重复名称依靠ID区分。

三要素图用 `g234:supports-requirements` 表示整个方案指向整个需求范围。模型的 `extensions.relationship_types` 必须声明该命名空间关系；定义见包。来源没有逐部门到逐组件的一一对应。示例保留的三个 `supports_metadata_requirement` 关系是虚构项目设计，单独展示，不能冒充原图事实。

检查对象及关系方向、显式包含与分解、四类关注、完整定义、审批/实现证据以及每项裁剪理由。图内主图和详细语义附表均使用同一对象ID；只在JSON存在不算已表达。来源图4-4错图继续登记；可信PDF裁图另存，原始资料未改。完整示例模型与双布局输出见 `examples/metadata-repair/`；执行和视觉证据见 `reviews/metadata-repair-validation.json`。
