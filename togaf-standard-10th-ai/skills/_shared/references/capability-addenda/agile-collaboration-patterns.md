# G210四种敏捷架构协作模式

四种模式按组织需要选用。来源仅说常与成熟度相关，没有定义四级量尺、分数、权重或必经路线。

## 输入、分析与缺口

需要每个团队业务开发/EA/方案能力与容量证据、业务目标、时间盒、反馈需求、授权治理边界、冲刺目标和待办ID。缺资料保留缺口，不能按团队名称推断能力。逐项比较四模式并说明采用/不采用依据。时间盒为项目约定。

## 对象与关系

guide:agile_sprint定义目标/片段；guide:agile_activity表示团队当轮工作，lane不是组织等级；guide:dorp_gate表示演示/成果/回顾/规划。outputs标记不是活动节点。guide:agile_handoff是后续冲刺交接；guide:agile_collaborates是同冲刺对称协作治理；guide:agile_continues为同泳道延续。跨职能必须每队三能力，不能整体相加。

## 输出、修改与评审

专用图保留冲刺列、橙色DORP边界、并行泳道、成果标记、单向交接和双向协作。reference为来源结构解释，adaptive按两列分图，以同关系ID端口追溯。长字段在SVG内明细带表达。提供SVG/PNG、关系源、图例、模型和coverage，缺口报ID，不静默降为通用图。

切换仅未来周期，保留历史，继承待办/未决项，更新交接计划。核对零冲刺增量、交接时序/方向、协作双向、逐队能力、DORP四活动与未完成回流。演示不等于批准上线，开放尾列不等于固定冲刺数。

## 完整案例与来源

输入（历史材料已清理） → 分析（历史材料已清理） → 基线（历史材料已清理） → 修改（历史材料已清理）；反例（历史材料已清理）。调用generate.py model.json --profile agile-solution-collaboration --layout reference --render --out out。

便携来源：references/source-tables/agile-collaboration-patterns.json；G210§3.3–3.3.8、图3-2至3-5。原图缺失，历史解释/重绘偏差分列；source_verified=false，生成与目视检查不升级为原图等价。
