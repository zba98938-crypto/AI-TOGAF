# 三项证据工作产品的正式调用

入口使用 `analyses[].method_id`：业务属性为 `business-attribute-evaluation`，业务场景为 `scenario-traceability-review`，年度环境核算为 `environmental-annual-accounting`。方法目录的 `environment-lifecycle-accounting` 映射到最后一个计算器；原有 `environmental-delta` 仍是独立的逐行变化比较。

三个完整虚构案例在 `examples/addenda/<能力ID>/production-baseline-model.json` 与 `production-modified-model.json`。每份包含原始陈述、稳定对象及关系、显式计算规则、证据ID和具体视图。`case.json` 记载原始材料到分析模型的步骤；修改前材料不覆盖。

从 `_shared` 运行（Python环境按项目README准备）：

```sh
python scripts/analyze.py examples/addenda/business-attribute-profile/production-baseline-model.json --evaluate analysis-business-attribute-profile
python scripts/generate.py examples/addenda/business-attribute-profile/production-baseline-model.json --out tests/tmp/bap --artifact business-attribute-profile
python scripts/generate.py examples/addenda/scenario-traceability-matrix/production-modified-model.json --out tests/tmp/scenario --artifact scenario-traceability-matrix --layout adaptive --render
python scripts/generate.py examples/addenda/environment-lifecycle-accounting/production-modified-model.json --out tests/tmp/environment --artifact environmental-is-assessment
```

仅请求单个视图时用 `--view library-scenario-outcomes` 或 `--profile scenario-painpoint-outcome-matrix`。制品入口包含其已建模的全部视图，不会用另一个视图覆盖同名制品。

业务属性画像表同时输出业务论证、测量方法、指标单位/尺度/时期、目标、容差、纠偏运算符、条件性频率/成本阈值和观测证据。追溯表保留属性、业务目标、安全要求、控制目标四类对象与三条显式关系。支持百分比/比例的样本公式与带单位直接观测值；只计算已声明的向上或向下阈值。自定义公式字符串不执行，须先扩充并评审计算契约。

场景输出分为流程—五类要素矩阵、问题—预期结果矩阵和转换审计表。五类列按利益相关者、人参与者、计算机参与者、问题、目标排列。同ID复用，未知格不等于确定无关联；分类缺口可用 `category_gaps` 的流程、类别和理由明确说明。此视图不支持用无依据CRUD编码代替关联。

环境核算表分别输出互斥核算行和计算依据：边界、因子、提供方19字段数据、历史年、抵消及规则。实现支持 `kgCO2e/tCO2e/gCO2e` 的明确换算；活动量必须与因子分母同单位，期间和地区相同或有显式适用性证据。年度计算器只接受完整年度；月报不会自动乘12。提供方Scope2只选一个口径，提供方Scope3设备是总量子集，采购服务在当前组织视角记Scope3。该版本的云服务计算要求提供方Scope1明确为零并有证据；非零或未知直接阻断，需要扩充核算契约后再计算。没有统一默认因子、分配比例、合格线或通用TOGAF公式。

修改流程：回到原始证据或已声明项目规则，更新权威 `analyses[].inputs`，同步更新用于表达的对象属性与相关视图，再运行分析、生成和对照检查。生成器不会把任意展示字段的改动推断为新的事实或自动批准。生产案例构建器 `capability-addenda/build_evidence_package.py` 演示如何从已审查输入一致地派生表和矩阵，保留历史扩展数据。

验证证据在 `reviews/evidence-work-products-integration.json`。原始材料图未提供该表单时，`reference` 是按正文定义构造的项目表单，不能声称官方图形复刻。年度核算表的图3-10原图空间等价尚未验收。表格输出为可编辑Markdown和JSON；专用矩阵另有SVG/PNG/可编辑关系源及逐对象、关系、字段表达记录。
