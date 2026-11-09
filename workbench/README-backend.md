# 本地工作台后端

在仓库根目录运行：

```sh
python3 -B workbench/server.py --port 8765 --data-dir output/workbench-data
```

浏览器访问 `http://127.0.0.1:8765`。静态文件仅从 `workbench/web/` 提供。
服务本身只用 Python 标准库；模型校验/生成复用现有
`togaf-standard-10th-ai/skills/_shared/scripts/{registry,profile_examples,validate,generate}.py` 及当前 Python 环境中已准备的依赖。
不会安装依赖、调用模型 API、读取远程来源或修改共享 skills/历史成果。

## 数据与语义

- `--data-dir` 下建立 `workbench.sqlite3`、SQLite WAL、锁文件及 `jobs/<job-id>/`。
  默认路径是新的 `output/workbench-data`，不要将历史成果目录指定为工作目录。
  同一工作目录只允许一个服务实例，单实例可服务多个浏览器标签。
- 版本是不可变快照；`id`/`version_hash` 是 model、layout、parent、created_at、message
  及可选 native 原文的规范 JSON 的 SHA-256。`model_hash` 仍只对项目 JSON 计算，保持旧语义。
  `native_sha256` 对原生源码 UTF-8 字节计算。重复保存或回滚仍产生新版本。
- 创建项目时，省略 model 则使用所选 registry 模板经 `normalize_example` 包装；默认
  `trust-framework-default`。不将项目显示名称写回模型，不推断批准、不自动修复业务内容。
  示例仍保留虚构示例/候选状态。
- 结构与已编码业务约束错误阻止创建、保存和生成（422）；警告保留。
  不存在“自动满足全部业务要求”的默认规则；`valid` 仅表示没有校验 error。
- 原生 XML 是可选版本字段，必须明确指定 BPMN 2.0.2 或 UML 2.5.1。
  UTF-8 原文（包括 BOM、空白及换行）保存在 `native.xml`；交换清单不是权威编辑数据。
  无效原生源码允许建立带诊断的草稿版本，生成和 accept 会重新校验并拒绝输入错误。
  材料缺失和能力未覆盖分别报告；`conformance_complete` 只有实际完整验证通过才为 true。
  当前 UML/BPMN 均保持 incomplete，未宣称完整标准或业务验收通过。
- layout 是前端编辑布局元数据，完整保存、版本化和对比；不会被解释为业务关系。
  生成器仍使用其自身 reference/adaptive 布局，原编辑布局另导出 `workbench-layout.json`。
- 评审状态按版本独立：`draft → in_review → accepted | changes_requested`。
  只有 `submit` 可以使 draft 进入评审；接受/退回只能从 in_review 发生。
  comment 不改变状态，可随时追加；终态如需修改应新建版本。
  accept 会重新校验该版本；旧版本接受不会接受新 head。
  作者只是本地声明身份，不是登录认证、电子签名、专业批准或正式合规结论。
  评审事件永不改变 model 内的 approval/implementation 状态。

## HTTP API

所有写入使用 `Content-Type: application/json`。成功返回 JSON 对象；错误为
`{"error":"code","message":"说明","issues":[]}`（issues 按需出现）。

| 方法与路径 | 请求 / 响应 |
| --- | --- |
| GET `/api/health` | `{status:"ok",local_only:true,notice}` |
| GET `/api/catalog` | `{templates:[{id,name}],artifacts,deliverables,profiles,analysis_methods,notice}` |
| GET `/api/projects` | `{projects:[{id,name,head_version,created_at,updated_at}]}` |
| POST `/api/projects` | `{name,model?,template?,native?}` → 201 项目详情 |
| GET `/api/projects/:id` | 项目详情 |
| POST `/api/projects/:id/versions` | `{base_version,model,layout?,message?,native?}` → 201 更新的项目详情 |
| GET `/api/projects/:id/versions/:version` | `{id,version_hash,project_id,parent,model,layout,native,native_sha256,model_hash,validation,created_at,message,review_state}` |
| POST `/api/validate` | `{model}` → `{issues,valid}`；无效模型仍为 200/valid=false |
| POST `/api/native/validate` | `{native}` → `{valid,validation_errors,missing_material,capability_uncovered,conformance_complete,source_sha256,standard_report}` |
| GET `/api/projects/:id/diff?from=…&to=…` | `{from,to,changes:[{group,id,kind,before,after}]}` |
| POST `/api/projects/:id/reviews` | `{version,action,author,comment?}` → 201 事件，含 state/version_hash |
| POST `/api/projects/:id/generate` | `{version,render?:false,kind?:"project",auto_layout?:false}` → 202 持久化 queued 任务 |
| GET `/api/jobs/:id` | 任务详情 |
| GET `/api/jobs/:id/files/*` | succeeded 或 blocked 任务已核验输出附件；其他状态 409 |

项目详情包含 `{id,name,head_version,created_at,updated_at,model,layout,native,validation,
versions,reviews,review_states,review_state,jobs,notice}`。versions 是不含 model/layout
的元数据列表；reviews 和 jobs 包含所有历史事件/任务。
validation 为 `{issues,valid,native?}`，issue 保持原校验器的 `{level,code,id,message}`；原生诊断项另有 category。
jobs 含 `{id,project_id,version,version_hash,status,render,kind,auto_layout,created_at,started_at,finished_at,
outputs:[{name,url}],error,notice,native_preview?,native_source_sha256?,full_language_acceptance?}`。
客户端可轮询直到 succeeded/blocked/failed。

原生字段示例：

```json
{"language":"bpmn","version":"2.0.2","xml":"<definitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" targetNamespace=\"urn:example\"/>"}
```

源码限制 7 MiB；可选 `source_sha256` 是请求方断言，服务重新计算并核对。
拒绝 `package_root`、任意输入路径等额外原生字段。XML 禁止 DTD/实体扩展和危险 href。
保存时省略 native 沿用旧版本原文，保持旧客户端兼容；明确 `native:null` 在新版本移除原生模型。
只含 native 的新项目会建立无实体、无关系且批准/实施状态为 unknown 的兼容 JSON。

保存时 base_version 必须等于当前 head，否则 409，不覆盖或自动合并。
模型校验失败为 422；非法评审转换为 409；未知资源为 404；非法输入为 400。
Diff 对全部顶级字段比较，含 project/sources/extensions 等；原生变化单列 native/xml 等字段。
ID 对象数组按 ID 比较，
顺序变化另列 `$order`；layout 单独列出。kind 为 added/removed/modified。
字段缺失的一端用 null，未改动字段不列出。

## 后台生成与恢复

固定入口的本地 Python 子进程调用 `generate(..., all_items=True, strict=True)`，
不拼接 shell、不传递 API 密钥环境变量。默认不生成 PNG；render=true 使用既有离线
Node/resvg 渲染链，缺失本地依赖或表达检查错误都会使任务 failed，不会伪报通过。
任务成功还须检查生成 manifest、运行依赖稳定性及输出 SHA-256。

`kind:"native"` 使用固定原生 worker；输出 exact `native.bpmn`/`native.uml`、无损 native-package、
三类诊断、预览报告和带指纹清单。服务核对原文、清单与不可变版本的来源 SHA。
`render:false` 仅交换，成功不表示完整能力通过。`render:true` 请求本地预览：
BPMN 使用显式 DI，缺少 DI 且未选择自动布局时 blocked；显式 `auto_layout:true` 为当前支持的
过程/协作/会话/编排子集生成独立 `.layout.bpmn`，保留原始 XML 和已有坐标，布局能力未覆盖时 blocked。
UML 有受支持的原生 UMLDI 类图时按原有 bounds、waypoints 和标签顺序预览，不生成布局。
其他 UMLDI 图形或未支持的符号明确返回能力未覆盖；自动布局选项不替换已有 DI。
UML 无 DI 时只有 `auto_layout:true` 才渲染现有类图子集，派生布局单独标记。
现有 UMLDI 保留原文，预览标记 capability_uncovered，避免覆盖已有坐标。
blocked 表示原文/交换输出有效而预览不可满足，已核验文件仍可下载；失败不会提供部分文件。

最多一个生成子进程同时执行；跨进程文件信号量由子进程继承，即使服务异常退出也不会
与重启后的生成重叠。默认超时 180 秒，可用 `--job-timeout` 调整；超时杀死整个生成进程组。
子进程自己也设置截止时间，防止服务消失后永久残留。
重启将上次 running 标记 failed（结果不计成功），queued 自动继续。
失败任务仍保留记录、input.json、layout.json、generation.log 和不完整输出用于本机诊断，
但 HTTP 不提供失败任务的文件下载。不会自动重试失败任务，需用户重新生成。

## 安全边界

- 默认只绑定 127.0.0.1，拒绝非 loopback；可显式使用 localhost/::1。
  对 Host 端口/loopback、Origin 同源、Sec-Fetch-Site 检查，不启用 CORS；
  JSON Content-Type 和拒绝预检防跨域写入。无 Origin 的本机 CLI 请求可以使用。
- 写入请求最多 8 MiB；不接受重复 JSON 键、非有限数、Transfer-Encoding、非对象请求。
- 静态与下载逐级 `O_NOFOLLOW` 打开，不接受路径穿越、反斜线、符号链接或非普通文件。
  共享 skills、SQLite、原始日志等不会被映射为 HTTP 静态目录。
  输出以附件响应，设置 nosniff 和 sandbox CSP；前端脚本必须外链至同源文件。
- Python 生成进程审计钩子拒绝网络连接及任务目录外写入，仅允许固定的离线 renderer 子进程。
  不读取来源 URI、不执行模型内提供的命令，也不开放外网代理/下载接口。
  这是受信任本机用户的离线工具，不是 OS 级沙箱或多租户服务；同机恶意程序/文件系统
  管理员仍可改写数据，勿暴露端口、勿以高权限运行、勿将身份声明视作认证。
- 当前适用于 macOS/Linux（使用 POSIX 文件锁、进程组、O_NOFOLLOW）。
  没有用户管理、删除、迁移、云同步、审计签名或自动数据清理；备份请停服后复制整个 data-dir。

## 验证

```sh
python3 -B -m unittest discover -s tests -p 'test_workbench*.py' -v
```

测试使用临时目录、真实随机端口 HTTP 服务和真实生成子进程，不依赖历史 output。
覆盖项目、校验、并发保存/冲突、不可变快照、字段差异、版本绑定评审、任务成功/失败/超时/
重启恢复，以及 Host/Origin/请求体/路径/符号链接保护。失败场景会产生预期 WARNING 日志。
原生测试另覆盖 BOM/CRLF 保真、无效草稿、版本来源绑定、旧客户端兼容、诊断分类、交换包、
无 DI 阻断、实际 UML 自动布局、已有 UMLDI 保留和原生队列重启恢复。

实际界面检查使用已有 Puppeteer 与已安装的浏览器，创建独立临时端口、数据目录和 profile。
输出目录必须尚不存在；浏览器和服务在完成后退出，profile 清理，截图与 JSON/SQLite 证据保留：

```sh
node workbench/verify_native_ui.mjs --out output/workbench-native-ui-round
```

若浏览器没有默认安装路径，先设置 `TOGAF_BROWSER_PATH` 为已存在的可执行文件。
检查包含原生导入、源码编辑、键盘保存、三类诊断、版本对比、重载恢复、UML 派生预览、
BPMN 显式 DI 预览、移动端几何和进程清理。运行方式标为本地测试控制器，不属于 Actor 原生沙箱。
