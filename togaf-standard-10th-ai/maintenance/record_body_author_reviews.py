# -*- coding: utf-8 -*-
"""Record the author's actual focused source comparisons in this revision.

These observations were made while reading source and authored body. They are
not generated semantic verdicts and do not constitute a second reviewer.
"""
from pathlib import Path
import json,hashlib,datetime
C=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
NOTES={
'01-introduction-and-core-concepts':{
'b00094':'框架含基线、目标、构建块组合与演进方法，不只是一张分类图。',
'b00183':'ADM含框架建立、架构开发、过渡和实现治理。',
'b00193':'必须连同b00192的ADM does not读取：不强制特定阶段顺序，也不强制瀑布；分离否定上下文会反转语义。',
'b00222':'保留本地错引ADM Techniques的事实，不把源错误当作已校正的官方定位。',
'b00241':'企业原则及子域原则需保持组织语境一致；架构原则不脱离企业原则。',
'b00258':'连续系列为资产分类与复用，包括架构和方案两个互补系列，不是时间线。',
'b00265':'ADM多层运行、整体治理、资产入库与构建块约束保留。',
'b00324':'可与其他方法集成，按企业流程与组织裁剪，不自动新增强制模板。',
'b00400':'四主域与跨域的动机、安全、治理区分；域不等于固定组织岗位。',
'b00407':'全景含某时点在用及计划资产，计划不等于已经实施。',
'b00421':'视图是从一组关注点看系统的表示，不等于规定表示约定的视点。',
'b00426':'视点规定构建、解释、使用视图的约定；术语别名保留。',
'b00561':'SBB可实现一个或多个逻辑ABB的部分或全部，不强制一对一。'},
'03-adm-techniques':{
'b00058':'原则有名称、陈述、理由、影响；优先级冲突需解释，潜在影响不冒充已验证。',
'b00070':'原则一致性允许平衡解释，稳定也需要批准后的修订过程。',
'b00109':'连续性需求覆盖外部事件及替代信息机制；这仍处于示例原则语境。',
'b00209':'易用性不应狭隘假定人员位置、语言、培训或身体能力。',
'b00303':'模式包括适用前提、冲突力量、结果语境、未解决问题和已知使用，不只存可复制方案。',
'b00323':'差距须考虑遗漏关注点，而非只做两个组件清单差集。',
'b00325':'差距覆盖人员、过程、工具、信息、度量、财务、设施及数据及时性等，不只技术缺件。',
'b00328':'差距矩阵轴向及New行、Eliminated列保留；意外遗漏须恢复，正确删除要解释。',
'b00355':'补全SMART五个英文展开及中文，不以熟悉术语代替原文。',
'b00470':'风险测量没有固定规则；示例分级不得当普遍数值阈值。',
'b00472':'四效果等级按财务和交付影响保留。',
'b00474':'五发生频率等级保留转型周期语境，不换成无来源百分率。',
'b00476':'四风险等级描述保留，低风险也不是无风险。',
'b00485':'纠正把little or no residual risk译成改善很小的跳跃；重大支出与低/零剩余风险是取舍，不能自动接受。',
'b00486':'风险缓解须真正降低企业影响，不只从一个极高格移到另一个极高格。',
'b00491':'剩余风险须IT治理批准，需业务接受时可能进入企业治理，不由生成器接受。',
'b00492':'批准接受与实际缓解执行监控分开，G维护工作表。',
'b00507':'可选择一个备选或组合特征，只做足以决策的细节，任意阶段层次可用。',
'b00516':'影响评估覆盖现有和过渡架构、项目双向约束、跨阶段影响及价值；基线未定义时只能非正式差距。',
'b00519':'正式评审决定方案与资金；有评分或画图不代表已经批准。'},
'05-architecture-content':{
'b00047':'交付物有契约及正式评审批准签署语境；制品是某方面表示；ABB/SBB适用于业务、应用、技术，且实现可部分。',
'b00070':'实体关系依企业而异，标准元模型需裁剪，不作为所有企业既定事实。',
'b00073':'选定内容框架重要，具体哪一个可按组织适配。',
'b00104':'实体可捕获、存储、过滤、查询及表示，支持一致、完整、追溯；不能只维护互不关联图片。',
'b00114':'36实体逐行保留；能力、业务能力、服务、流程、组织、角色及工作包分开；本表SMART为Simple，与核心定义Specific不默合并。',
'b00117':'175属性行源表合并实体归属展开；ID、生命周期、服务容量和FTE等属性定义不自动填数值。',
'b00120':'154关系逐行保留源目标及英文标签；双向Used by和双向Is accessed and updated through存在疑点，新增明确源问题，不自动改写或发明基数。',
'b00146':'例子嵌套表示职能在地点执行，是该视点指定语义，不推广成一切嵌套的包含关系。',
'b00197':'工具互操作困难为源文时期判断，不假装当前市场调查。',
'b00332':'组织分解/组织地图有指挥链语境；不能据此把其他角色协作图统统当汇报树。',
'b00509':'网络通信图处理协议容量和物理边界，不描述信息格式内容。',
'b00564':'交付物输出和输入可跨阶段，源表按行保留，不把交付物登记等同实际接受。',
'b00568':'不要求逐字照搬，但必须仔细考虑要素及省略的下游影响。',
'b00605':'需求规格是实施必须满足的定量陈述，和定义文档互补，生成文件不证明符合。',
'b00739':'SBB含实现接口、拓扑、运营政策、共享质量属性及ABB映射，不只是产品名。',
'b00794':'基础架构向组织特定模型的特化，不是实施时间顺序。',
'b00917':'方案全景不存放方案产生的全部业务数据，和实际运营数据责任分开。'}
}
def main():
 reviews=[]
 for vol,notes in NOTES.items():
  path=C/'fundamental/chinese-text'/(vol+'.json');d=json.loads(path.read_text());bm={b['source_block_id'].split(':')[-1]:b for b in d['blocks']};observations=[]
  for suffix,note in notes.items():
   b=bm[suffix];observations.append({'source_block_id':b['source_block_id'],'source_quote_en':b['text_en'],'translation_zh':b['text_zh'],'source_block_sha256':b['source_locator']['block_sha256'],'review_observation_zh':note})
  reviews.append({'volume_id':vol,'source_document_path':d['source_document_path'],'source_document_sha256':d['source_document_sha256'],'translation_path':str(path.relative_to(C)),'translation_sha256':sha(path),'authoring_path':d['authoring_path'],'authoring_sha256':d['authoring_sha256'],'observations':observations})
 report={'schema_version':'Chinese-body-author-semantic-review/2','recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'passed':True,'review_type':'same-author-focused-source-comparison-after-authoring','reviews':reviews,'counts':{'volumes':len(reviews),'focused_observations':sum(len(r['observations']) for r in reviews)},'input_sha256':{p:h for r in reviews for p,h in [(r['source_document_path'],r['source_document_sha256']),(r['translation_path'],r['translation_sha256']),(r['authoring_path'],r['authoring_sha256'])]},'independent_acceptance':'pending','limits_zh':['来源块全量译写与覆盖检查另见正文索引；本报告只列实际重点二次对照观察，不能扩大为每句由另一评审人校核。','passed指本报告列出的作者复核及修正已落实；不同评审人最终语义验收未授予。']}
 dump(C/'quality/chinese-body-author-review-final-volumes.json',report)
 # Retain the historical review exactly; annotate its scope without replacing
 # historical hashes with today's bytes.
 old=C/'quality/chinese-body-author-review-additions.json';history=json.loads(old.read_text())
 for r in history['reviews']:
  if r['volume_id']=='02-architecture-development-method':r['current_scope_status']='superseded-selected-chapters-review';r['superseded_by']='quality/adm-body-author-review.json'
 dump(old,history)
 gpath=C/'supplementary/chinese-text/G226.json';g=json.loads(gpath.read_text());gm={s['section_number']:s for s in g['sections']}
 gn={'2.4.5':'先框定问题再邀提案，法律监管例外保留；领导与多方参与并存，不预设答案。','2.4.6':'企业架构师对整体战略和运营有效性负责，视角跨团队；不是每个局部实现的替代岗位。','3.1.2':'创新可在所有阶段，D新技术与H变更驱动的重点区别保留；重大转型可先评估准备度。','3.2.1':'MVA基于有意架构；短内部版本和外部发布区分，部署但不发布及停用均保留。','3.2.2':'SaaS和频繁UI重写是来源作者经验，未转成当前项目事实。','3.3.1':'协作不止演示评审，还包括决策；非财务价值与客户外向内保留。','3.4.1.1':'完整性按关注点和适用性判断，一致性连接视图并展示冲突取舍。','3.4.2':'组合、项目群、产品、项目、PO及Scrum Master按源定义分开，不造汇报树。','3.4.3':'B—E产品架构、E工作产品、F管理交互与迁移计划分别保留；源Scrum Manager不擅改。','3.5.2':'采购双方互相理解、共同治理；采购方最终决定仍需充分分析。','3.6.2':'滚动预测使用不断改善的成本价值理解，过渡架构输入预算，不代表预算已经批准。','4.1.7':'图6无额外正文，不由图推导每冲刺必须完整A—H及固定时长。','4.1.9':'MVA输入解决方案积压，方案团队反馈架构，不推断图中固定冲刺比例。','4.2.1':'标准规定输入输出类型，但不规定固定文档格式；Library模板不属于标准本体。','4.2.2':'最低文档按下一步而定；末期运营所需内容不会为零，保留长期可访问性。','4.3.1':'结对在预备阶段定义职责；A—F和需求管理按价值使用；G支持及合规消息一致。','4.3.2':'ISO/IEC 27001/27002按脚注展开；结对安全架构是作者案例。'}
 gr={'schema_version':'G226-body-author-review/1','passed':True,'review_type':'same-author-source-comparison-during-and-after-authoring','input_sha256':{str(gpath.relative_to(C)):sha(gpath),g['source_extraction_path']:g['source_extraction_sha256'],g['authoring_path']:g['authoring_sha256']},'observations':[{'section_id':gm[n]['id'],'source_block_ids':gm[n]['source_block_ids'],'source_quotes_en':[b['text_en'] for b in gm[n]['source_blocks']],'translation_zh':gm[n]['text_zh'],'review_observation_zh':note} for n,note in gn.items()],'independent_acceptance':'pending','limits_zh':['75节均按原文阅读译写，本报告列17个重点来源对照；中文按节对齐，部分采用连续压缩表达，不宣称逐句等价已获独立认证。']}
 dump(C/'quality/g226-body-author-review.json',gr)
 print(report['counts'],{'G226_observations':len(gr['observations'])})
if __name__=='__main__':main()
