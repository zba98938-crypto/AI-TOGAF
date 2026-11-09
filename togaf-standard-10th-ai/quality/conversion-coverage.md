# 转换覆盖与视觉审校清单

全文、表格和每个图像区域均有可追溯MD/JSON表示。转换覆盖与独立视觉审校分别计数；历史图意保留来源状态，未逐图完成独立审校的记录列在pending_full_visual_review。

|转换对象|数量|
|---|---:|
|英文PDF / 页面|26 / 1487|
|网格表格片段|260|
|原文逻辑图 / 中文编者自绘图|242 / 1|
|嵌入图像区域 / 已关联MD与JSON表示|417 / 417|
|独立图片记录|168|
|完整可见内容已独立审校的原文图|242|
|原文图完整视觉审校待办|0|
|缺失输出文件|0|

机器清单见[conversion-coverage.json](conversion-coverage.json)，包括417个图像区域各自的原图、MD、JSON及当前解析入口。
验证结果见[来源验证](validation.md)和[架构验证](../architecture/validation.md)。清单记录转换覆盖；验证报告分别检查来源一致性与集成完整性。

|文档|页数|表格片段|逻辑图|图像区域|完整视觉审校|全文|
|---|---:|---:|---:|---:|---:|---|
|G152|45|0|7|8|7|[MD](../documents/G152.md) · [JSON](../documents/G152.json)|
|G176|53|3|4|5|4|[MD](../documents/G176.md) · [JSON](../documents/G176.json)|
|G178|28|6|9|10|9|[MD](../documents/G178.md) · [JSON](../documents/G178.json)|
|G184|138|15|24|29|24|[MD](../documents/G184.md) · [JSON](../documents/G184.json)|
|G186|161|34|21|21|20|[MD](../documents/G186.md) · [JSON](../documents/G186.json)|
|G188|94|16|11|23|11|[MD](../documents/G188.md) · [JSON](../documents/G188.json)|
|G18A|30|0|8|9|8|[MD](../documents/G18A.md) · [JSON](../documents/G18A.json)|
|G190|27|3|8|9|8|[MD](../documents/G190.md) · [JSON](../documents/G190.json)|
|G198|27|0|2|11|2|[MD](../documents/G198.md) · [JSON](../documents/G198.json)|
|G203|22|0|0|1|0|[MD](../documents/G203.md) · [JSON](../documents/G203.json)|
|G206|25|3|5|6|5|[MD](../documents/G206.md) · [JSON](../documents/G206.json)|
|G20F|48|3|11|12|11|[MD](../documents/G20F.md) · [JSON](../documents/G20F.json)|
|G210|41|0|5|6|5|[MD](../documents/G210.md) · [JSON](../documents/G210.json)|
|G211|29|0|6|7|6|[MD](../documents/G211.md) · [JSON](../documents/G211.json)|
|G212|57|12|8|85|8|[MD](../documents/G212.md) · [JSON](../documents/G212.json)|
|G217|90|26|5|6|5|[MD](../documents/G217.md) · [JSON](../documents/G217.json)|
|G21B|58|26|16|24|16|[MD](../documents/G21B.md) · [JSON](../documents/G21B.json)|
|G21D|76|20|17|18|17|[MD](../documents/G21D.md) · [JSON](../documents/G21D.json)|
|G21H|52|7|5|6|5|[MD](../documents/G21H.md) · [JSON](../documents/G21H.json)|
|G21I|53|3|8|9|8|[MD](../documents/G21I.md) · [JSON](../documents/G21I.json)|
|G233|59|8|13|42|13|[MD](../documents/G233.md) · [JSON](../documents/G233.json)|
|G234|45|20|14|16|14|[MD](../documents/G234.md) · [JSON](../documents/G234.json)|
|G238|44|20|9|10|9|[MD](../documents/G238.md) · [JSON](../documents/G238.json)|
|G242|105|18|20|35|20|[MD](../documents/G242.md) · [JSON](../documents/G242.json)|
|G248|47|13|5|6|5|[MD](../documents/G248.md) · [JSON](../documents/G248.json)|
|G249|33|4|2|3|2|[MD](../documents/G249.md) · [JSON](../documents/G249.json)|

## 剩余独立视觉审校

下列图已转换，当前质量状态表示现有复核范围。后续独立审校应继续对照原PDF检查全部标签、实际连接端点、箭头、分组及相关正文。

|图片|PDF页|当前状态|当前解析|
|---|---|---|---|
