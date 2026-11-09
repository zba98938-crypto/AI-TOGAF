# 本地可迁移包运行约定

从本包根目录运行；包内所有工具、资料引用均相对自身定位。`corpus/`保存当前章节解析、图示解释和来源块；原始资料指纹保留。历史解释不进入默认检索。

```bash
python3 -B _shared/scripts/local_tool.py doctor
python3 -B _shared/scripts/local_tool.py query '库存 一致性 过渡架构'
python3 -B _shared/scripts/local_tool.py validate work/model.json --report work/validation.json
python3 -B _shared/scripts/local_tool.py generate work/model.json --out work/output --all --render --strict
```

输入已有模型时复用对象ID和来源。自然语言任务由技能按照实际来源开展分析并维护模型；脚本进行确定性的校验和生成，不宣称从任意文本自动推出正确架构。

需要任务与人员配置时，先运行 `local_tool.py assignments work/model.json --out work/assignment-model.json`，将已有任务、配置、观察投影为模型中的显式主体及关系，再校验生成。单项架构图无需收集人员评价。

缺失等级保留null/needs-input，培训完成不自动提升等级。官方参考目标、组织裁剪目标与人员观察分别保存。能力、容量、期间和授权分别核验；有支持计划不等于支持者具备能力或投入足够。

依赖：Python按 `_shared/requirements.txt`；Node按 `_shared/package-lock.json`，Node>=22.13。需已安装Chrome/Chromium或设置 `TOGAF_BROWSER_PATH`；不会自动下载浏览器。开发副本复用已在本地安装的Node依赖。可安装归档不包含node_modules或机器特定虚拟环境，首次部署按锁文件安装依赖；离线环境使用相同平台已准备依赖。所有输出与临时文件放包内 `work/`。

CLI `generate --out work/<交付目录>` 会先在同级临时目录生成、校验，再替换已有的生成目录；旧目录中不属于本次交付的文件会移除。若已有目录没有版本 2 的生成清单，命令会拒绝覆盖。工作台任务和正式评测仍使用各自的新目录及不可变证据规则。日常检查使用项目根目录的 `tools/daily_check.py`，无需运行全量渲染或封包。

独立复制该`skills/`目录后仍可执行。安装时17个技能目录与`_shared/`保持为同级；本次交付不写入用户的全局技能目录。

## 部署到另一个目录

解包后从`skills/`运行，保留17个入口与`_shared/`同级。Python>=3.9，Node>=22.13。若使用当前macOS平台离线Node依赖包，将其解到同一位置；不同平台按锁文件准备本机依赖。Python依赖及Chrome/Chromium需要预先具备或自行安装。

首次准备依赖的示例（以下仅说明，本轮未联网安装）：

```bash
mkdir -p work/tmp work/pip-cache work/npm-cache
python3 -m venv work/venv
TMPDIR="$PWD/work/tmp" PIP_CACHE_DIR="$PWD/work/pip-cache" work/venv/bin/python -m pip install -r _shared/requirements.txt
TMPDIR="$PWD/work/tmp" PUPPETEER_SKIP_DOWNLOAD=true npm ci --prefix _shared --cache "$PWD/work/npm-cache"
work/venv/bin/python -B _shared/scripts/local_tool.py doctor
```

浏览器不会随包下载；通过`TOGAF_BROWSER_PATH`指定已有Chrome/Chromium。`doctor`检查依赖、字体和语料存在性；渲染成功以实际生成及报告为准。来源中英文引用与译文校订状态保留，各出版物原版权和许可不被技能包重新授权。
