# 原生标准接口与合成企业闭环

这是一组共享工具，不把单项制品任务扩大成全量 ADM。

## 企业输入

`enterprise_closure.py --base <已审计投影.json> --out <新目录>` 在原交易投影上增加独立编写的企业仿真材料：组织/角色、能力与价值流、四域基线/过渡/目标、接口、风险/质量政策、恢复点、实施合规及价值复核。来源明确标为合成，不把统计事实反推为企业授权。`validate.py` 在模型含 `extension_data.enterprise:closure` 时校验这些额外契约；不含该扩展的单项模型保持原范围。

`closure_simulator.py --model ... --flow closure-rollback --observations ... --out ...` 只做符号路径重放，绝不执行恢复、结算等操作。守卫观察缺失、出口不唯一或越过步数上限立即失败；模拟完成不等于生产恢复成功。

`closure_render.py --model ... --out <新目录>` 输出概览、三状态细图、带守卫与异常路径的回退图，以及无需点击即可阅读的关系/质量明细。工程元数据位于附录。图名必须注明**项目简化关系图**，不能冒充严格 UML/BPMN/ArchiMate 符号。

## 语言接口

`standards.py catalog|import|validate|export|render --language bpmn|uml|archimate --version 2.0.2|2.5.1|4 ...`

- 版本显式指定；不自动降级或替换。项目 JSON v1/v2 继续使用原工具。
- UML/BPMN 使用独立原生包，保留 native XML、ID、属性、关系、DI、扩展与外部引用。`bindings` 通过命名空间联结项目 ID，不把原生格式强塞进项目元模型。
- 原生保留式导出只允许完整性一致的包；修改 inventory 不能冒充可编辑的原生写入。BPMN 可请求 `--normalize` 运行固定 `bpmn-moddle` 后端；任何未审查变化/警告都阻断严格导出。
- 导入/无损保留成功不是全语言语义一致性。`validate` 当前实施官方 BPMN XSD、独立基础语义、ID/引用及安全检查；UML 全 OCL/Profiles/UMLDI 与 BPMN 完整语义/正式符号测试尚不完整，必须报告未覆盖构造。`render` 不以简化图替代正式图，未验证时返回 3。
- UML 可在 `validate` 时增加 `--mapped-uml-backend --java-home <Java21>`，实际运行哈希固定的 Eclipse UML2、EMF Diagnostician 与 Classic Ecore OCL。`uml_backend.py` 将 OMG 命名空间仅在派生副本中显式映射，保留原始字节；从官方 UML.xmi 提取全部类不变量并逐项报告解析、适用数量、违反和 invalid。未映射、解析失败、不适用与映射等价待审不能计作已覆盖；禁止外部资源解析。这个后端不替代完整 Profiles/UMLDI/表示法验收。
- ArchiMate **4** 的受限元模型/符号及适用官方交换原文未取得时阻断。不将 3.x 交换 XSD 宣称适用于 4。
- XML DTD/实体、远程解析、绝对外部文件路径及路径逃逸均不允许；合法 vendor 扩展保留为不透明内容，不声明已按标准验证。
- 退出码：0 为请求的保留/清单操作完成，1 为确定错误，3 为阻断或验证未完成。必须同时阅读报告中的 `conformance_status`，不能只看退出码。

## 官方来源与参考模型

`closure_source_coverage.py` 对全部现有 profile 保存来源类别、版本定位、实际表达、差异与定义哈希；绝不批量修改 `source_verified`。

`reference_models.py catalog|check|generate` 处理 TRM/III-RM 专项映射。没有经现有七维验收门槛校核的官方定义/版本/图定位时阻断。历史参考来源必须标明历史适用性，不能自动标为 TOGAF 10 基础规范。工具的验收记录完整性检查不替代独立人员的诚实、授权与签署。

## 实测与验收

`tests/verify_closure.py` 保留原回归并执行新增契约负例、原生保留往返、安全、覆盖与预算测试。原生评测运行时须冻结在真实用户 home 之外；Actor 仅本工作区可写，评分者只读，shell 网络关闭。Python/Node/Java/浏览器与跨会话边界实际预检通过后才能开始业务会话。

原生预算累计最多 16 小时/4000 会话，最多 4 批，每批最多 4 小时/1000 会话。预检、Actor、评分、重试全部计入；1→2→4 总会话并发只在较小阶段成功后提升。两次连续超时/429、隔离失效或资源超限熔断；恢复不重置预算。会话额度不是请求数、token 或费用上限。

每项分别报告实现、来源、视觉、业务执行状态。正确拒绝可以通过负例行为测试，但不能把受阻的业务决定标成完成。独立签署、正式认证与生产实施不得生成。

## 大视图与环境诊断

`large_view_reader.py --model ... --view <项目视图ID> --out <新目录>` 将实体目录限制为每页 12 个、1920×1080，并保存完整实体/关系台账、跨页端点及原模型字节。它是明确的目录切片，不将没有连线的分页目录称为完整拓扑，不声称解决单张超大图的栅格安全上限或严格标准符号。

`tests/verify_native_toolchain.py --runtime-root ... --out <新目录>` 可逐项诊断全部工具和隔离边界，**不调用模型或分发业务**。macOS 冻结路径不要位于被拒绝的 `/tmp` 或真实 home；用独立只读目录，仍保留 home/跨会话拒读。Node 的符号链接保留选项和 TMPDIR 必须进入原生 shell policy，单独传父进程环境会被丢弃。浏览器默认使用调试管道而非网络监听；仍需实际启动、截图预检通过，不因普通或 headless 浏览器的安装/版本检查成功而放行。安装的浏览器分发若纳入冻结包，完整字节必须哈希核验。

新冻结包入场检查覆盖包、Java 和固定浏览器的真实路径，拒绝 macOS 被禁止的 `/tmp` 与真实 home；只读归档的历史哈希验证不作追溯改写。Java 编译与源文件运行模式对应现有 UML2/OCL 适配器，不能代替所有工作区 `.class` 类路径加载模式。过渡模型还必须显式包含运营、数据一致性、依赖、控制与回退；当前双写场景保持订单入口，条件均为候选合成设计，不代表部署授权。

ArchiMate 4 的官方出版目录定位为 C260。目录页可公开核对，但不等于取得规范全文、元模型或交换适用性；不得自动提交许可或采购。`standards.py catalog --language archimate --version 4` 单独报告出版元数据，严格能力仍阻断。
