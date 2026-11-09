# togaf-application-architecture 字段契约

本文件由 `_shared/scripts/build_skill_packages.py` 从 `capabilities.json` 生成，字段名与注册表逐字一致。

本文件说明字段如何填，不授予任何验收。标有「项目补充」的字段不是原文强制字段。

## 微服务应用分解方法

- `id`：`microservice-decomposition-method`
- 英文名：Microservice Decomposition Method
- 决策问题：应用应按什么边界拆分？
- 主责技能：`togaf-application-architecture`
- 来源：G21I §10.5 / Table 10-1
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, business_function, ownership, cohesion
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：7；对象类型：service_boundary
- 关系类型：project:service_partition
- 关联交付物：`architecture-definition-document`

### 分析步骤

1. 从业务功能和质量目标确定候选边界
2. 检查职责与数据所有权
3. 比较耦合和独立部署代价
4. 记录分解原则和过渡

### `service_boundary` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `business_function` | 业务功能引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `ownership` | 数据所有权及责任 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `cohesion` | 候选边界内聚性及判断依据 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `coupling` | 边界之间的耦合与代价 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `interface` | 公开接口与契约 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `data_responsibility` | 数据读写与所有权责任 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

其余字段（1）：`name`

### 输出

- 范围及决策问题
- 对象／属性／关系
- 分析结果与理由
- 来源、假设、未决项
- 相关制品与交付物引用

### 关系语义

使用下列有类型的关系；每条关系均需明确方向、条件、范围和证据。traces_to仅表示已说明的追溯，不能替代组成、实现、信息使用或价值交换。

## 微服务价值与资源目录

- `id`：`microservice-value-catalog`
- 英文名：Microservice Value and Resource Catalog
- 决策问题：已实现和计划服务贡献什么价值？
- 主责技能：`togaf-application-architecture`
- 来源：G21I §7；G21I §11.3、§12.1
- 定义状态：`guide-work-product-with-project-operational-contract`
- 必需输入：范围与五维语境, 相关原始业务材料及其定位, business_function, value, planned_state
- 可选输入：现有架构模型, 历史评估或决策, 组织特定量表和裁剪规则
- 缺输入策略：关键输入缺失时生成明确标记的草稿与缺口，不计算无依据数值，不伪造批准或事实。
- 字段总数：14；对象类型：microservice, ops:msa_value_resource
- 关系类型：traces_to
- 关联交付物：`architecture-definition-document`

### 分析步骤

1. 盘点服务及状态
2. 关联业务功能与价值
3. 记录开发运营资源
4. 评估重复与持续收益
5. 区分已实现和计划服务
6. 逐服务确认一个ABF与业务价值
7. 开发/运营及已分配/计划四格分开记录单位时段
8. 关联工作包及命名过渡，检查运营计划缺口
9. 成本或ROI规则未提供则不计算

### `microservice` 必填字段（6）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `business_function` | 业务功能引用 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `value` | 度量值或业务价值陈述，依语境声明 | 保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。（来源：`project-operational-convention-guided-by-cited-source`） |
| `planned_state` | 已实现或计划等实现状态 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `development_resources` | 开发资源投入 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `operations_resources` | 运营资源投入 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `owner` | 对对象负责的责任方 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |

### `ops:msa_value_resource` 必填字段（11）

| 字段 | 含义 | 取值规则 |
| --- | --- | --- |
| `service_status` | 目录中的实际/计划状态 | 微服务目录项的计划或实际状态；存在于目录不表示已部署、运行或产生价值；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `ABF` | 单原子业务功能 | 单一原子业务功能；写清业务结果和边界，不能以服务名代替功能；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `value` | 度量值或业务价值陈述，依语境声明 | 保留实际值、单位、量表和证据；未知显式登记缺口，不能用零代替。（来源：`project-operational-convention-guided-by-cited-source`） |
| `development_resources` | 开发资源投入 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `operations_resources` | 运营资源投入 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `owner` | 对对象负责的责任方 | 使用可追溯的业务描述或稳定标识；未确定内容标为假设或缺口。（来源：`project-operational-convention-guided-by-cited-source`） |
| `work_package_ref` | 工作包外部引用 | 资源目录关联工作包的外部引用；工作包存在不表示已授权或实际实施；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `architecture_state_ref` | 相关过渡范围外部引用，不冒充v2 state_id | 相关架构状态的外部引用；不能自动视作当前实体state_id或已实现状态；类型约束：`{"type":"string","minLength":1,"pattern":"\\S"}`（来源：`project-operational-convention`） |
| `evidence_detail` | 资源记录定位 | 实际观察的证据定位与时点；缺证据明确未知，摘要不能冒充真实批准；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `cost_and_return` | 未知成本与未算ROI边界 | 微服务成本与收益依据；缺成本、收益或时间窗时保留未知，不计算ROI；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |
| `gap` | 资源或价值证据不足 | 未覆盖或未验证事项；记录影响与后续补证，不把未知写成已通过；类型约束：`{"anyOf":[{"type":"string","minLength":1,"pattern":"\\S"},{"type":"object","minProperties":1}]}`（来源：`project-operational-convention`） |

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

合计 2 个工作产品，21 个字段。
