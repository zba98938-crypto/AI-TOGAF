# ADM 周期：从阶段目标到可追踪工作

在用户要求完整 ADM、跨阶段推进、阶段评审或需求变更时读取本文件。单一制品任务按其主责技能执行，不为画一张图自动创建完整周期。

## 方法依据与边界

依据本地 G186 §5.2、§6、§15，G184 §4–12，G210 的敏捷实践和 G248 附录 A/B。详细阶段输入、活动、评审问题与现有交付物 ID 在 [adm-phases.json](adm-phases.json)。已纳入本地C220基础标准ADM卷的84个编号步骤及需求管理表的10行步骤。`source_step_records`保留原文定位与责任列，`steps`为操作摘要。这里的状态、JSON结构和机器检查是项目实现约定，不能替代对C220正式步骤的实际分析，也不能把候选交付物清单解释为每项目必须生成。

ADM 是有信息依赖的迭代方法。先落实阶段 A 的项目启动、范围、利益相关者及目标设置；可复用既有且适用的 A 输出，不必重做同一套材料。B/C/D/E 可以并行探索并反复收敛。Preliminary 管理 EA 能力，不意味着每个项目都重建组织。Requirements Management 贯穿所有阶段，H 的变化也可触发早期阶段或新周期。

## 执行一项架构任务

1. 确定目的（战略、组合、项目或解决方案交付）、范围、规划期、业务周期和利益相关者决策。先查架构存储库，复用有效上层约束、基线与既有工作产品。
2. 选择阶段工作：对每阶段注明 `execute`、`reuse` 或 `not-applicable`。说明复用的范围/时效或裁剪理由；A 可复用，不能整体省略。未取得正式裁剪决定的工作可保留为计划，不能声称已通过阶段退出。
3. 按阶段合同的 `inputs` 识别信息缺口，按 `steps` 开展领域分析，路由到 `owners` 中的技能。B/C/D 均执行视点选择、同口径目标/基线与差距、工作/价值/风险评估、跨域影响解决及利益相关者评审。C 同时处理数据与应用；没有变化的域仍说明保留现状的影响。
4. 把候选输出绑定到共享模型的实际实体、关系、视图、分析或交付物 ID。用现有 `validate.py`、`analyze.py`、`generate.py` 完成模型验证、分析与制品生成。目录/矩阵/图仍从同一模型派生。
5. 复核需求的来源、责任人、可验证验收及目标/架构/工作包/验证证据的追踪；记录已知未覆盖项。变化先运行影响分析获取候选范围，再逐项作业务判断，登记受影响阶段和输出。
6. 评审退出判据时记录观察、理由、实际证据和决策。只有利益相关者或有授权证据的代理人能作目标接受、豁免或变更决定。脚本不创造批准或实施有效性。
7. 复用、变更或新迭代后重新核对当前输入。保留原阶段迭代，追加下一轮，完成后向后续工作提供明确版本的信息。H 说明维护、局部重开或新 ADM 周期的选择；新周期填 `previous_cycle_id`。

## 可执行周期记录

周期 JSON 是与已有架构模型配套的独立记录，使用 [adm-cycle.schema.json](../schemas/adm-cycle.schema.json)，不向现有模型 Schema 偷加字段。所有命令均不覆盖既有文件；输出应在原周期目录以保留相对证据路径。

```bash
python skills/_shared/scripts/adm.py init \
  --model project/model.json --id cycle-2026-01 \
  --scope '订单履约改造：项目级；范围和日期来自项目工作请求' \
  --out project/adm-cycle.json
python skills/_shared/scripts/adm.py report \
  --model project/model.json --cycle project/adm-cycle.json \
  --out project/adm-check.md
```

`init` 只创建未完成、未批准的工作计划。`report` 给出阶段、责任技能、候选交付物和缺少的信息。`check` 返回 JSON；普通检查允许如实保留草稿，但无效引用和虚假完成声明返回非零。需要自动验收周期记录闭合时加 `--require-complete`，草稿返回非零。

具体绑定采用 `{"collection":"views","id":"business-target"}`；`collection` 可取 `entities`、`relationships`、`views`、`deliverables`、`analyses`。`depends_on` 引用具体迭代 ID，表示退出所需信息版本；不是预设 A→B→C 的流水线。不要把“下一轮需要回访前轮”写成相互依赖的退出环，应追加迭代并提供所需的信息版本。

在开始本轮证据评审前记录输入指纹：

```bash
python skills/_shared/scripts/adm.py bind --phase A \
  --cycle project/adm-cycle.json --model project/model.json \
  --out project/adm-cycle-bound.json
```

随后在该副本记录实际判断。`bind` 不改变判据、批准或完成状态；已有判据结论/决定的迭代禁止重新盖指纹。迭代的 `model_sha256` 绑定所选输入/输出、其显式引用闭包、直接关联关系及端点、来源、语境和信息依赖；未关联的模型增补、全局版本号或实施进度不会使阶段 A 自动失效。项目范围、被引用数据、关系或来源发生变化时，先判断影响，再用 `iterate` 保留历史并重开受影响工作。模型引用中的精确 ID 会纳入闭包，依赖关系不能仅写在自由叙述中。

`check` 每阶段返回 `current_input_sha256` 与 `current_requirements_sha256`，供评审时核对。前者写入迭代的 `model_sha256`（由 bind 完成），后者由需求复核者在实际复核后写入 `requirements.reviews[].model_sha256`。需求复核指纹覆盖需求基线、直接追踪关系及其端点、相关来源与该阶段的变更处置，不受无关能力对象的新增影响；指纹相同不替代实际追踪检查。用 [requirements_trace.py](requirements-trace.md) 形成规划或交付追溯报告，再由复核者判断缺口及阶段影响。

```bash
python skills/_shared/scripts/adm.py iterate --phase C \
  --cycle project/adm-cycle-bound.json --reason '需求 CR-07 改变客户数据保留期' \
  --out project/adm-cycle-next.json
```

新迭代保留全部历史，输出仅复制为本次候选输入，退出判据和决定全部回到待处理；工具不自动重新批准。若要改变裁剪决定，应保留原周期文件，在新副本把该阶段的 `tailoring_decision` 设为待决，再重新评审。

## 阶段退出与证据

每个执行/复用阶段有完整判据：`pending`、`satisfied` 或带理由的 `not-applicable`。每项非待决结论都引用实际文件证据，例如：

```json
{"path":"reviews/architecture-review.md","sha256":"文件当前的64位SHA256","locator":"2026-11-04 评审记录，决定 D-03"}
```

哈希可用 `shasum -a 256 文件路径` 获取。文件必须真实存在，定位必须指向相应观察或决定。禁止为“让检查通过”创建虚构签字、批准或业务测量。测试夹具只能保留 `is_example: true`。

`decision` 分开记录 `status`、`authority`、`authority_role`、`rationale`、`evidence`；代理人另提供 `delegation_evidence`。有资料、有模型、有格式校验不等于已接受。`completed` 只由执行者在实际完成后填写；机器结果 `recorded-complete` 仅表示所录判断、引用、指纹与信息依赖一致，仍不证明文档签名真实性或语义结论正确。

## 持续需求与重开

`requirements.baseline_ids` 必须对应本模型的全部 `requirement`、`security_requirement` 和 `analytics_requirement`；宽模型中本次无关的内容先明确裁剪到任务模型。`owner` 是需求管理责任人。没有需求时填 `no_requirements_reason` 并由每次退出评审证明适用性，不能以空数组隐去尚未收集的需求。

每条 `changes` 记录需求 ID、原因、受影响阶段、候选受影响输出和实际决定。未决或延期的变化阻止受影响阶段退出；被接受/拒绝的变化仍须由对应迭代的需求复核明确处理。`requirements.reviews` 以迭代 ID 绑定当前模型指纹、变更 ID、复核人、理由和证据。完成状态并不免除后续需求变化的复核义务。

阶段 G 逐项判断实施范围及实际实现是否符合要求；不符合时形成强制执行、限时豁免或变更架构建议，并追踪真正决定。阶段 H 依据实际价值和变化反馈，不用部署完成代替收益实现。

## 将退出判据落实到当前制品

跨域交付按[阶段到制品工作映射](architecture-delivery.md)明确利益相关者关注点、判据、实际视图和交付物实例。`architecture_delivery.py catalog/init/check/report`复用当前注册表和周期；`adm.py check/report --delivery-plan 计划文件 --products 生成目录`同时核对成果的模型、依赖、保存文件及表达证据。映射、生成和阶段记录分别报告，不能相互替代。单一制品请求无需创建周期。

## 版本化需求的选择性影响

新增需求版本可以用 attributes.supersedes_id 引用仍保留在基线中的旧ID；concept_id相同且version为更大整数，并有明确接受且限定受影响阶段的变更记录时，无关阶段仍按旧版本投影核验。原基线编辑、未知前版、不同概念、非递增版本和未接受变更均不享受此规则；仍需专业判断未建模的跨域耦合。受影响阶段追加新迭代、实际重做证据和需求复核，旧文件及其哈希保持不变。

## 基础标准步骤覆盖

`adm init`为94个来源步骤创建`pending`草稿。旧周期仍可读取；缺失步骤记录作为覆盖缺口，不默认已执行或不适用。`adm check --require-source-coverage`在步骤记录未闭合时返回非零，和`--require-complete`的项目退出检查分别使用。

每条`source_step_coverage`记录含`source_step_id`、`disposition`（pending/execute/reuse/not-applicable）、具体理由、定位及SHA256证据、`source_step_sha256`和`context_sha256`。来源指纹取当前步骤记录的`adm.digest(step)`；语境指纹使用检查报告返回的`current_context_sha256`。指纹只绑定版本，实际工作证据需先取得，不能用盖指纹代替工作或批准。更改模型相关对象、需求或步骤定义后须重审。复用和不适用须有范围、适用性及裁剪理由。

持续需求管理的10步保留Requirements Management Steps与ADM Phase Steps两类责任。Step 10中的gap requirement指被意外消除的基线内容；不能把全部新目标差距都套用此名称。

## 完整ADM架构流程图

`adm.py flow --out <不存在的新目录> --render`从当前阶段合同和制品注册派生预备阶段、A–H、持续需求管理、输入—工作—制品—交付物—治理门及ABB/SBB内容关系。输出含中文SVG/PNG、可编辑Mermaid、完整阶段候选清单、来源定位及指纹；F的条件治理模型保留`if any`。候选产品可跨阶段复用，不是必须生成清单。

总览实线用于阅读常见信息流；B/C/D可以并行和迭代。加`--cycle 周期.json --model 模型.json`可另绘实际迭代和`depends_on`依赖，保留模型对象引用、已记录状态与当前证据检查。未完成或过期记录不会因绘图变成批准。可移植运行示例见[examples/adm-flow](../examples/adm-flow/README.md)。
