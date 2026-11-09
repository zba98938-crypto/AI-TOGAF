# togaf-value-streams 字段契约

本文件由 `_shared/scripts/build_skill_packages.py` 从 `capabilities.json` 生成，字段名与注册表逐字一致。

本文件说明字段如何填，不授予任何验收。标有「项目补充」的字段不是原文强制字段。

## 价值网络

- `id`：`value-network`
- 英文名：Value Network
- 决策问题：判断多个参与者如何交换有形或无形价值以及网络依赖
- 主责技能：`togaf-value-streams`
- 来源：G178/figA-2
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, role, value_exchange, beneficiary
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：5；对象类型：value_network_actor
- 关系类型：exchanges_value, traces_to
- 关联交付物：`architecture-definition-document`, `capability-assessment`

### 分析步骤

1. 确定网络边界和受益者
2. 识别参与者角色
3. 逐方向定义价值交换及对价
4. 识别依赖与失衡
5. 核实每条交换的依据

### `value_network_actor` 必填字段（2）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `role` | 承担职责的角色 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `beneficiary` | 在本工作产品范围中明确定义的 beneficiary 属性 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（3）：`name`、`value_exchange`、`conditions`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 精益价值流

- `id`：`lean-value-stream`
- 英文名：Lean Value Stream
- 决策问题：识别信息物料流中的等待、返工和浪费
- 主责技能：`togaf-value-streams`
- 来源：G178/figA-3
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, function, lead_time, processing_time
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：actor, application, lean_process
- 关系类型：information_flow, traces_to, work_flow
- 关联交付物：`architecture-definition-document`, `capability-assessment`

### 分析步骤

1. 确定产品范围和时间边界
2. 记录信息流与工作流
3. 逐流程采集LT/PT与完整准确率
4. 统一时间单位和工作日口径
5. 分析瓶颈和改进机会

### `lean_process` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `function` | 参考功能或实际功能映射 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `lead_time` | 在本工作产品范围中明确定义的 lead_time 属性 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `processing_time` | 在本工作产品范围中明确定义的 processing_time 属性 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `complete_accurate` | 在本工作产品范围中明确定义的 complete_accurate 属性 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `unit` | 度量单位 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `queue` | 在本工作产品范围中明确定义的 queue 属性 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

---

合计 2 个工作产品，12 个字段。
