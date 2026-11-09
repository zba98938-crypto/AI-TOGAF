# skills唯一版本归并记录

唯一维护目录：`togaf-standard-10th-ai/skills/`。根目录 `skills/` 已删除，无兼容软链接；根目录 tests、tools、workbench保留并统一引用当前版本。

删除前核对原1488项上游复制指纹，全部与历史清单一致；功能源码均有AI版对应项，1360项同字节，129项采用AI版修订。根目录独有的.gitignore规则已合并至仓库忽略规则，机器缓存和旧虚拟环境随旧目录清理。历史upstream-manifest保留，不能再作为第二套维护源。

已迁移测试、工作台、资料工具及浏览器检查的路径；工作台生成子进程明确保留当前Python依赖位置，继续使用原有网络和写入限制。build_skill_package直接更新唯一版本语料绑定，不再从根目录复制。两幅G249图解的过期来源指纹已与当前文件同步，语义未改变。

验证结果：

- 全部295项单元回归：289项通过，6项因未配置Java后端跳过。
- 本地运行20项、解包迁移11项、G249来源语义12项及语义回归36项通过。
- 当前交付包5587项封存文件与归档一致；来源资料保留2479项检查通过。
- 离线检索成功；严格单视图生成SVG、PNG成功；未发现活动工程代码指向已删除的根skills。
- 当前基础评测为483项，另12项闭环用例，共495项；这是评测清单，非已全部执行。6项无内嵌业务示例的视图保持缺输入，不计作已验收。

[机器清单与旧指纹](skills-consolidation.json) · [最终回归日志](skills-consolidation-tests-verified.log) · [来源检查](skills-consolidation-source-tests-final.log) · [迁移运行](portability-validation.json) · [归档校验](release-current-validation.json)

本次统一不改变原有独立语义验收待完成和真实业务批准未授予的状态。历史封存证据和临时解包运行副本只用于追溯，不是第二个维护版本。
