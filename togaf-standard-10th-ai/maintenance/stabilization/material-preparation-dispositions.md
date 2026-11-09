# 来源处置与历史图形候选准备契约

`build_material_review_inventory.py` 以已获取的六卷、26 份指南及 G226、W242C 为输入。`material_preparation_dispositions.py` 在原始单元清点完成后，依据固定的源码清单 `maintenance/material-source-adapters/r7-preparation-dispositions.json` 核对 734 个尚未分配确定来源处理方式的单元，并为 641 个英文正文图单元绑定已存在的中文历史候选。输入仍有 34,571 个来源单元；来源 ID、文档、类型、英文或中文原文、片段、定位、原图引用及全部 `source_*` 字段均保持不变。

来源可定位、候选可定位和语义可靠性分别记录。处置的 `source-located-preparation` 只表示原始上下文足以准备材料角色；每项分类仍为 `source-disposition-prepared-independent-adjudication-pending`。历史候选使用 `historical-project-candidate-pending-independent-review`，其语义可靠性为 `not-certified`。所有单元的独立复核为 `not-executed`，人工专业验收为 `pending`，真实组织批准为 `pending-signature`。历史 JSON 中的 `done`、`reviewed` 或类似声明不会成为当前复核证据。正文图具有候选也不证明图中文字、连线或语义已验收。

默认模式 `default-static-source-manifest` 仅选择上述固定源码路径。`--preparation-manifest <仓库内文件>` 选择 `explicit-manifest`；`--no-preparation-dispositions` 选择 `explicit-disabled`，恢复准备处理前的整个清点值。默认静态文件缺失会明确记录 `static-source-manifest-unavailable`，显式指定的文件缺失则拒绝构建。输出清单总是记录应用模式、确切决策引用、处置数量、未决 ID、英文正文图候选绑定数量和零执行复核数量。实际应用时，决策清单和适配器源码进入 `input_sha256`。任意 `output/` 历史目录或同名候选文件不会被自动发现或作为权威输入。

静态清单保存源单元原始绑定的 SHA-256、原分类与依据，以及完整去重的候选字段目录。其 `baseline_inventory_sha256` 是历史 r6 的指纹定位说明；实际验证依靠每项来源绑定和从原始记录重新生成的关系与候选字段集合，不把这个字符串当作已经执行历史重建的证据。适配器拒绝遗漏、重复或未知源单元、错误原文或定位、输入指纹漂移、缺少或虚构的候选字段、无关记录中的同文候选、非规范 JSON、路径越界和符号链接。适配器也拒绝继承已宣称完成的模型、人工或组织验收状态。

正文图候选只从原始图记录明确关联的文件及内嵌图记录、原始 `figure_ids` 关系中选择既有中文字段。每个候选保存原始 JSON 指针、原始字符串指纹和实际文件引用，分片只包含其单元需要的上下文。未提供的 G188 `ex3-22` 英文图题继续为原始 `null`；不会补造英文图题。三幅原始中文 W242C 正文图不创建虚构翻译。W242C 第 37–40 页根据原始作者、致谢和出版者材料准备为出版前置类；第 38 页必须同时有第 37 页作者标题及实际续页人名。页号、文字和页图不变。

此准备组包含 11 类：75 个网页图、75 个图题、4 个脚注、42 个空导航项、32 个空 PDF 内容项、417 个内嵌图来源项、17 个空表格单元、1 个无英文题图、63 个 G226 空白抽取块、3 个原始中文正文图及 5 个 W242C 出版材料页。缺少实际上下文时保留 `uncertain` 与确切未决 ID，不用静态决定替代来源。

本次最终准备目录为 `output/material-r7-preparation-implementation-20261109-r1/material-review-inputs-r7-final/`，共 899 个分片；旧 r6、旧 r5、首次 r7 和初次反例失败日志保留原字节。首次反例发现的单独适配调用边界已收紧，最终版本重新构建。关闭准备处理的实际 r6 重建使用以下命令，其证据记录整个清点及 891 个分片全值相等，并核对 2,101 个 r6 引用和 1,749 个 r5 引用的前后指纹：

```sh
python3 -B output/material-r7-preparation-implementation-20261109-r1/reproduce_actual_r6_final.py
```

常规重建使用新且尚不存在的目录，避免覆盖准备输入或旧复核：

```sh
python3 -B togaf-standard-10th-ai/maintenance/build_material_review_inventory.py \
  --out output/<新的准备目录> \
  --visual-source-manifest output/material-source-binding-implementation-20261109-r1/w242c-visual/manifest.json
```

历史 r6 的 API 重建为 `Inventory(root, visual_source_manifest=原清单, preparation_manifest=False).build()`；`prepare_shards(..., max_units=40, max_characters=24000)` 仍产生同样的 891 个分片。关闭模式不会向清点值加入新来源处理字段，CLI 输入清单则仍明确记录关闭模式。

单独可重复的反例测试命令如下，不建立模型会话、原生运行许可或真实/模拟评测预算：

```sh
python3 -B -m unittest discover -s tests -p test_material_preparation_dispositions.py -v
python3 -B -m unittest discover -s tests -p test_material_review_inventory.py -v
python3 -B -m unittest discover -s tests -p test_material_source_adapters.py -v
```

最终只读验证仍使用未修改的 `enterprise.material_review.ReviewInputs`，独立核对候选关系、原始指针及分片预算，并在当前 authority 审计前冻结 owned 源码。准备完成不提升资料复核、标准能力或 507 项模型评测的完成状态。
