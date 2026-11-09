# togaf-gap-solutions 判断规则

本文件是唯一需要人工撰写的部分：机器无法从注册表推出「什么情况选 A 不选 B」。

每条含判据、反例、影响。

## 判断 1：ABB 不等于产品选型

- 判据：`abb` 规定「需要具备什么能力、接口与质量要求」，与厂商无关；`sbb` 是「用哪个具体产品与配置去实现」。ABB 写成型号即失去复用与比选价值。
- 反例：ABB 直接写「采用某厂商 MES 3.2 版」，后续比选空间消失，也无法判断是否满足要求。
- 影响：`building-block-description` 的 `definition`、`abstraction`、`service`、`owner`；`g20f:allocated-to-sbb` 边；`solution-building-blocks` 交付物。

## 判断 2：工作包必须闭合至少一个缺口

- 判据：每个 `work_package` 必须连到至少一个 `gap`，且该 `gap` 能追到 `requirement` 或 `risk`。追不到的工作包是「想做的事」，不是架构工作。
- 反例：工作包写「升级中间件版本」，但无对应缺口与需求，实施后无人能说明价值。
- 影响：`work_package` 的 `owner`；`implementation-migration-plan` 的章节绑定；缺口清单的完整性。

## 判断 3：三种变革画像按不确定性与成本决定分析深度

- 判据：**快速画像**适用于低不确定、低影响，重速度；**功能画像**重完整功能与集成；**稳健画像**适用于高不确定、高影响，重分析与保证。画像决定需要多少分析与验证，不决定技术方案。
- 反例：对一个替换内部报表的小改动使用稳健画像，投入远超收益；对一个核心结算系统使用快速画像，风险失控。
- 影响：`change-profile-governance-checklist`；`guide:change_profile` 类记录；分析与验证工作量。

## 判断 4：过渡架构必须功能完整才成立

- 判据：过渡状态必须是「可运营的完整状态」，不是主线的部分快照。判断标准见 `transition-operability-check` 的五项条件。
- 反例：把「三个模块已上线、两个还在开发」当作过渡架构，此时业务无法完整运转。
- 影响：`transition_architecture` 的 `definition` 与 `operating_conditions`；`transition-architecture-model`；路线图的阶段划分。

## 判断 5：能力增量的四种动作不可混用

- 判据：**优化**（同能力改法）、**整合**（多合一）、**新建**（从无到有）、**退役**（停用）。退役前必须检查其他价值流对该能力实例的依赖。
- 反例：直接退役一个被三个价值流共用的应用，未查依赖，导致另外两条链断裂。
- 影响：`capability_change` 的 `kind`；`capability-increment-analysis`；`capability-instance-gap-method` 的结论范围。
