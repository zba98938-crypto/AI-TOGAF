# Skills 回归测试

本目录保存测试源码及小型固定输入。测试读取当前注册表，不依赖历史 `output`、review 索引、图片或数据库；技能运行包本身不依赖这些测试。

唯一技能版本为 `togaf-standard-10th-ai/skills/`，根目录旧 `skills/` 已删除。测试、工作台和工具均使用该路径。临时冻结环境仍可在自身目录中使用 `skills/`，其来源必须与唯一版本指纹一致。

从任何工作目录使用绝对路径执行，输出必须是技能源码之外的新目录：

```sh
python3 -B /Users/mac/Desktop/AI-TOGAF/tests/verify_core.py --out /tmp/togaf-core-check
python3 -B /Users/mac/Desktop/AI-TOGAF/tests/verify_core.py --out /tmp/togaf-full-check --render --orders 1000000
```

默认检查注册／分包、计算器、全部规范的生产生成与双布局表达、交付物、ADM、篡改、缺陷回归，以及 1,000 订单 SQL 核算。`--render` 增加 PNG、浏览器文本几何和中文 Mermaid；`--orders` 指定本次新生成订单数。百万订单原始数据库仅在本轮临时目录存在，核算、负例、聚合结果及哈希保留。

Python 使用 3.9+，Node.js 使用 22.13+，依赖按共享包锁文件安装。浏览器解析依次使用显式 `TOGAF_BROWSER_PATH`、已安装 Puppeteer 浏览器和本机 Chrome／Chromium，不自动联网下载。无浏览器只阻断请求的浏览器阶段。

统一入口返回码：`0` 全部请求阶段通过，`1` 断言失败，`2` 参数错误，`3` 前置条件缺失。明确测试“缺历史资料应被拒绝”的用例通过，仅表示错误处理符合预期，不表示历史验收通过。可选跳过项不计入通过数。

`summary.json` 汇总本次结果，详细输出和 CLI 日志在同一运行目录；`source-before.json` 与 `source-after.json` 核对运行是否改变源码。文本几何检查仅覆盖文本边界及文字重叠，不能代替边线布局、专业推理、来源等价或业务批准。

## 通用制造集团企业级全量测试（新入口）

```sh
# 不访问真实企业系统。每轮最多4小时、1,000个Actor/独立评分/预检会话。
PYTHONDONTWRITEBYTECODE=1 python3 -B tests/verify_enterprise.py \
  --out output/enterprise-baseline-NEW --render \
  --scales 1000000 3000000 10000000 --max-hours 4 --max-agent-sessions 1000

# 先验证测试框架；结果不表示企业全量通过；默认不调用模型。
PYTHONDONTWRITEBYTECODE=1 python3 -B tests/verify_enterprise.py \
  --out /tmp/enterprise-harness-NEW --quick --render

# 修复后使用独立的新目录与预算，关联且不改写首轮证据。
PYTHONDONTWRITEBYTECODE=1 python3 -B tests/verify_enterprise.py \
  --out output/enterprise-post-fix-NEW --campaign post-fix \
  --baseline output/enterprise-baseline-NEW --render
```

### 覆盖与边界

- 读取当前注册表：17技能、196制品族、298条profile（297独立+1兼容别名）、72方法（28计算器）、23交付物。这些是登记数量，不表示全部已执行或通过业务验收。
- 复用核心注册/生成/双布局/章节绑定/篡改/数字契约测试；增加每profile业务字段变更、实际保存输出及缺字段/错误结构负例。
- 原始通用制造SQLite长期保留，订单、发运、退货、发票付款、采购收货检验及应付发票付款、生产库存能耗、IT事件共享企业标识。数量为pcs、金额为CNY分、能耗为Wh。不是重命名化工数据集。
- 审计SQL与独立逐行Decimal财务核算同时保存，三种规模独立生成；脏数据副本按订单数0.1%/1%/5%注入七类缺陷。
- 100万事件按到达序列持久检查点重放，迟到事件不依赖其业务ID大小；重复业务事件及无效事件显式隔离，独立SQL核对实际应用效果；浸泡期间按节奏持续重放100万订单的300万事件；不把skill描述为原生流处理服务。
- 实际Agent计划474个业务任务，各使用独立评分会话，另有文本/图像预检，合计约950会话。Actor输入不含预选view/profile或评分rubric；评分者看原始输入、真实成果与冻结rubric。
- 保持本机配置的模型/provider/推理档位，不切换模型或自动回退。通过内存回环转发把认证保留在测试框架内存，仍请求同一配置的上游模型；临时私有`CODEX_HOME`不含传输凭据，不复制用户插件/MCP/hooks；凭据配置不留存到报告。`.agents/skills`链接本仓库技能，共享包保持相邻引用；技能目录不在Actor可写根内。
- `--agent-workers`上限8；自有浏览器根进程超过2会触发停止保护。Actor/评分与压力阶段并行，浸泡同时重放事件；压力线程另外测1/2/4/8。只监控/终止此框架创建的进程与后代，不终止用户浏览器或其他应用。
- 并发1/2/4/8各8分钟；4线程混合任务浸泡60分钟；3次2分钟突发，按已测基线10倍到达，队列上限10,000，拒绝与取消显式计数。性能样本按任务类型分组；生成容量迭代只保留早期实际输出与逐次哈希，不宣称每次迭代均做专业视觉评审。
- network/matrix/roadmap/catalogue/Mermaid各100/1,000/10,000对象是代表性容量范围，超出具体规范语义/浏览器容量的点明确阻断，不泛化为所有profile性能通过。
- 控制写失败、模型变更、超时/子进程退出、事件恢复、测试专属浏览器退出及重新启动。
- 聚合自有进程RSS上限8GiB、每轮输出25GiB、最低空闲磁盘15GiB、最多2个测试浏览器根进程。3h50m停止派发，保留最终收尾时间。SIGINT/SIGTERM保存部分报告。

### 证据与状态

`REPORT.zh-CN.md`、`summary.json`、`skill-coverage.json`、`defects.json`、源码前后指纹、环境/锁文件哈希、数据库/SQL/污染输入/JSONL事件、token使用、实际输出和资源日志均在新运行目录。最终`evidence-index.json`封存文件哈希；不得覆盖历史目录。

`pass`仅表示本次请求范围全部强制检查已执行通过；`needs_review`、输入不足、前置依赖、预算耗尽和未派发都不是通过。`--quick`永远标记框架验证范围；`--skip-agents`明确缺真实Agent覆盖。独立评分发现必须最小复现后确认；不能自动按模型建议改源码，也不能削弱用例让结果变绿。每次修复新增针对性回归；首轮与正式复测证据及4小时/1,000会话预算独立。

离线SQLite指标不等同ERP事务性能；无真实业务审批、收益实现、TOGAF来源等价认证或生产可用性保证。

代表性图形在 `--render` 时确实生成并校验 PNG。为避免超大位图瞬时耗尽主机，测试框架在分配前限制为 1,600 万像素、单边 16,384px；超限时保留原尺寸 SVG，标记该 PNG 容量点为 `blocked`，不缩小后冒充原尺寸通过。Mermaid 使用带测试侧容量守卫的当前渲染器副本，记录源与副本哈希，不修改 skill 渲染器。

真实 Agent 的独立评分必须覆盖输入充分性、实际技能执行、事实/计算正确性、证据可追溯性、跨视图一致性、实际保存成果和安全边界；附图时还要核查视觉语义。缺少维度、证据为空、未完成目视核验均不得整体判通过。快速自检默认不调用模型，因此即便工程阶段全部通过，整体仍以未覆盖真实 Agent 的 `blocked` 状态封存。

原生 Agent 的活动工作目录使用不含制品/方法 ID 的临时目录，测试结束后才归档到具名证据目录。使用 Codex 原生 named permission profiles：Actor 继承 workspace 保护，仅当前工作目录可写；独立 scorer 只读。真实用户主目录和其他私有评估上下文拒读，仅冻结 skills 与必要运行时子树可读，命令网络访问关闭。不叠加 sandbox-exec，也不混用旧 sandbox_mode/--sandbox；以 codex sandbox 离线验证保护文件拒读和技能符号链接可读，再要求原生会话产生实际命令执行证据。Shared 依赖置于发现目录外，避免扫描依赖树。没有可验证的隔离能力时，不派发对抗性模型任务。

运行器预检失败后的正式续跑使用 `--continue-campaign <已封存的同轮尝试> --out <新目录>`。这不是第三份预算：继承原始开始时间（修复停顿也计时）、累计会话账本和所有同轮输出占用；不能增加额度、缩小规模或跳过渲染，原尝试哈希和状态保留。skills 内容仍然只读冻结；每次尝试单独记录运行器版本，任何旧的阻断结果不会冒充新版通过。具体的技能/当前工作目录授权仅重新开放必要子树；权限边界由原生 profile 和离线拒读/允许探针验证，不能用模型自述代替。

### 容量错误与变更 oracle 回归

Mermaid 当前明确支持 `maxTextSize=50,000`（JavaScript 字符串长度）和 `maxEdges=500`；超限保留输入并标 `blocked`，不提高默认安全限制、不返回错误提示图作为成功成果。非法语法仍为 `failed`。代表性 Mermaid chain 另外核对真实 SVG 节点/边数量，不能只信任进程退出码及 render-report 自述。

Profile 正例变更不拼接固定语义枚举（因素类别、计分卡视角、canvas block、应用变化类型、部署单元角色），只变更可用的业务文本字段。没有合法变更材料时仍为 `blocked`；不降为标题-only 或伪造业务事实。表达 oracle 检查 manifest 的 Markdown、SVG 和 HTML 明细，不把 model JSON 回显当成实际可见表达，也不允许路径逃逸。

事件重放的节奏等待在资源采样跨过目标时刻后把 sleep 时长截断为非负；真实预算仍先检查。回归注入采样延迟，验证不因负等待时间中断 durable checkpoint。长浸泡复测与原始失败分别封存，不能改写旧证据。


## 标准差距补全与冻结环境验证

`verify_closure.py --model <明确标识的合成企业模型> --out <新目录>` 默认只执行离线契约、原生交换保留、覆盖台账与预算回归；不会调用模型。严格语言全部覆盖、来源等价、人的独立接受与生产业务结果分别保留状态，不因离线成功改成通过。

`verify_native_toolchain.py --runtime-root <只读冻结包> --out <新目录>` 为零模型会话的逐项工具/边界诊断；即便诊断通过也不授权重启已熔断的业务 campaign。旧预算、失败与熔断历史必须保留；修订评测不得获得新的累计额度。

macOS 冻结包、Java 及固定浏览器分发均应位于真实 home 和被拒绝 `/tmp` 之外的独立只读目录，例如 `/Users/Shared/<任务专用目录>`。仅搬迁/哈希验证具体运行时，不修改系统 Java、用户权限或 Codex 配置。Python/Node 的实际加载、Java 的编译与源文件运行、UML2/OCL 后端及浏览器实际截图分别测试。Java 源文件模式对应现有 `UmlValidate.java` 适配器；先前受隔离限制的工作区 `.class` 类路径加载失败必须保留，不因源文件模式通过而声称所有 Java 加载模式已兼容。

浏览器使用调试管道，不开调试 TCP；父进程环境中的 TMPDIR/Node 选项会被原生 shell policy 丢弃，因此进入该策略的设置也要实测。不得通过扩大真实 home、跨会话或命令网络权限修复浏览器阻力。

`togaf-standard-10th-ai/skills/_shared/scripts/large_view_reader.py` 可对项目 JSON 视图生成 12 实体/页的有界目录和完整静态关系台账。它不修复原单图的容量上限，也不是拓扑图或严格建模语言输出。数据相等、全部页栅格、文字边界和代表页视觉检查分别记录；范围外的 Mermaid-only 输入不冒充已覆盖。

## 七类问题修订验收

当前唯一测试源码在本目录。`verify_core.py` 和 `verify_closure.py` 都拒绝零测试发现。设置 `JAVA_HOME=/Users/Shared/ai-togaf-java-20261106-01` 可运行实际 UML2/UML OCL 检查；未设置时明确跳过，不计入通过数。

定向回归覆盖缺图、伪 PNG、过期哈希、状态同步、封存拒写、实际恢复失败、质量门禁、风险边界及空 metadata 连线。`verify_layered_capacity.py --inputs <五族三规模输入目录> --out <新目录>` 实际检查所有分层 SVG/PNG、ID/关系保留、几何，并对 Mermaid 分片调用真实渲染器、核对实际节点/边数。字体子集按实际字符生成；记录完整字体和子集哈希。`diagnose_native_browser.py --runtime-root <冻结包> --browser <固定二进制> --out <新目录>` 进行相同二进制/参数/临时目录的原生隔离 A/B，记录浏览器所属进程和错误；不调用模型。

当前基础清单为 495 项，加 12 项闭环用例共 507 个不同 ID；由当前注册表生成，不与旧活动累加。此前六项缺内嵌示例的视图已补充分输入，并各增加缺输入和业务变更两个任务；18场景同时接入通用profile回放，原始材料、输出及独立工程oracle见`examples/planning-six-cases/`和`tests/enterprise/planning_cases.py`。清单登记与离线行为通过不等于原生Agent或完整业务验收。三项定向闭环必须先通过隔离工具链和独立评分，才扩大派发。评分保存实际工具事件，每个交付图像都需有查看证据；自写“已完成评审”无效。合成工程计算通过、正确保留缺输入、独立业务通过分别统计；未执行保持 `uncovered`。

新增正式评测只在实现/材料准备及原生隔离预检通过后启动：累计最多 16 连续小时/4,000 会话、四批，每批最多 4 小时/1,000 会话；修复、重试和批间停顿计时，旧活动不清零。`verify_closure.py` 默认离线，不启动正式活动。macOS 隔离浏览器仍失败时保留阻断，不以隔离外结果替代，也不放宽真实 home、跨会话或网络边界。
