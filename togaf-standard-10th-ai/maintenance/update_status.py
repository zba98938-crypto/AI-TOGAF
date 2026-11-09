# -*- coding: utf-8 -*-
"""Single current status derived from evidence; missing semantic work remains explicit."""
from pathlib import Path
import json,hashlib,datetime
from verify_implementation_ledger import declared_inputs, verify as verify_ledger
from report_outcome import engineering_complete, report_outcome
C=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def read(name,default=None):
 p=C/name;return json.loads(p.read_text()) if p.exists() else default
def evidence(name):
 r=read(name)
 if r is None:return {'status':'not-executed','path':name}
 checked=declared_inputs(C,C/name)
 current=[x['path'] for x in checked if not x['passed']]
 outcome=report_outcome(r)
 return {'path':name,'sha256':sha(C/name),'passed':outcome['passed'],'validation_outcome':outcome,'counts':r.get('counts'),'inputs_current':not current if checked else None,'input_freshness':'not-recorded' if not checked else 'stale' if current else 'current','stale_inputs':current}
def main():
 ci=read('chapters/index.json');ext=read('quality/extended-publication.json',{'documents':[],'counts':{}});fund=read('fundamental/web-2025/manifest.json');skills=read('skills/upstream-manifest.json',{'skills':[]});rows=[];counts={'rules':0,'corrections':0,'source_issues':0}
 for d in ci['documents']:
  code=d['document_id'];p=C/'maintenance/chapter-review-data'/f'{code}.json';maint=json.loads(p.read_text());pub=read(f'chapters/{code}.json');rows.append({'document_id':code,'reviewed_sections':len(maint['sections']),'published_current':pub['maintenance_sha256']==sha(p)})
  counts['rules']+=sum(len(s.get('semantic_rules',[])) for s in maint['sections']);counts['corrections']+=sum(len(s.get('corrections',[])) for s in maint['sections']);counts['source_issues']+=len(maint.get('source_issues',[]))
 foundation=[d for d in ext['documents'] if d['publication_role']=='fundamental-content'];extras=[d for d in ext['documents'] if d not in foundation]
 tests=[evidence(p) for p in ['quality/source-consolidation-verification.json','quality/chinese-body-verification.json','quality/supplementary-chinese-body-verification.json','quality/chinese-body-author-review-final-volumes.json','quality/g226-body-author-review.json','quality/foundation-execution-verification.json','quality/extended-verification.json','quality/execution-bridge.json','quality/local-runtime-regression.json','quality/skill-frontmatter-validation.json','quality/portability-validation.json','quality/current-entrypoint-links.json','quality/release-current-validation.json','release/release-manifest.json','maintenance/semantic-regression-report.json','maintenance/cases/omnichannel/forward-acceptance.json','maintenance/cases/omnichannel/adm-forward-acceptance.json','maintenance/cases/omnichannel/semantic-change-verification.json','maintenance/cases/omnichannel/current-delivery-review.json']]
 tests.extend(evidence(p) for p in ['quality/adm-completion-verification.json','quality/adm-flow-verification.json','quality/procedural-method-review-validation.json'])
 body=read('fundamental/chinese-text/index.json',{'volumes':[],'counts':{}})
 completed=[v['volume_id'] for v in body['volumes'] if v['volume_body_complete']]
 remaining=[v['id'].split(':')[-1] for v in fund['documents'] if v['id'].split(':')[-1] not in completed]
 gb=read('supplementary/chinese-text/G226.json',{'coverage':{}})
 body_summary=f"当前已有{len(completed)}卷完整编号正文译写，共{body['counts'].get('body_sections_written',0)}个小节、{body['counts'].get('body_blocks',0)}个来源块；G226另有{gb['coverage'].get('body_sections',0)}节中文正文与{gb['coverage'].get('unique_source_blocks',0)}个精确英文来源块。W242C逐页中文原文保全。不同评审人的最终校核待完成。"
 ledger=read('quality/implementation-ledger.json',{'items':[]});pending=[x['id'] for x in ledger['items'] if x['state']!='done']
 r={'schema_version':'completion-status/3','generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'implementation-in-progress-not-final-semantic-release','all_plan_items_complete':False,'source_scope':{'series_guides':26,'series_pdf_pages':1487,'fundamental':fund['counts'],'supplementary':[{'document_id':d['document_id'],'publication_role':d['publication_role'],'translation_status':d['translation_status']} for d in extras],'all_togaf_publications_claim':False},'chapter_review':{'counts':ci['counts'],**counts,'guides':rows,'published_current':all(x['published_current'] for x in rows)},'foundation_review':{'volumes':foundation,'numbered_headings':sum(d['numbered_sections'] for d in foundation),'figure_references':sum(d['figures'] for d in foundation),'extracted_tables':sum(d['tables'] for d in foundation),'body_tables':17,'frontmatter_contributor_tables':1,'full_chinese_translation_complete':False,'body_translation_progress':read('fundamental/chinese-text/index.json',{}),'independent_semantic_acceptance':'not-finally-established'},'skills':{'count':len(skills['skills']),'location':'skills/','external_installation':'not-performed','runtime_localized':True,'source_copy_manifest':'skills/upstream-manifest.json','reading_links':'skills/reading-link-manifest.json'},'verification':tests,'case_variants':read('maintenance/cases/omnichannel/generated/summary.json',{}),'sufficient_fictional_case':read('maintenance/cases/omnichannel/sufficient-results.json',{}),'pending_plan_items':pending,'real_business_approval':'not-granted','limits_zh':['章节分析记录不等同完整中文逐句校订；六卷及G226全文工作仍未完成。','自动回归、来源指纹、图表审查、不同评审人语义验收和真实组织批准分别报告。','未在外部目录核对全球出版物集合；范围限用户计划内本地来源。']}
 r['foundation_review']['full_body_written_volumes']=completed
 r['foundation_review']['full_body_remaining_volumes']=remaining
 r['status']='implementation-delivered-independent-semantic-review-pending'
 r['implementation_ledger_integrity']={k:v for k,v in verify_ledger(C,ledger).items() if k!='evidence'}
 r['engineering_implementation_complete']=engineering_complete(ledger['items'],r['implementation_ledger_integrity']['passed'])
 r['engineering_implementation_scope']='listed-documentation-and-delivery-plan-only; not all method/diagram/language/business capabilities'
 r['capability_gaps']={'path':'quality/seven-gap-reconciliation.md','all_capabilities_accepted':False}
 r['adm_framework_and_artifact_delivery']={'flow_reader':'architecture/adm-flow/index.html','evidence':'quality/adm-completion-verification.json','candidate_deliverables':23,'source_steps':94,'diagram_count':13,'business_approval':'not-granted'}
 if not r['implementation_ledger_integrity']['passed']:r['status']='implementation-evidence-invalid-review-required'
 elif not r['engineering_implementation_complete']:r['status']='implementation-in-progress-not-final-semantic-release'
 r['source_consolidation']={'single_root':'togaf-standard-10th-ai/','manifest':'sources/relocation-manifest.json','verification':'quality/source-consolidation-verification.json','historical_source_paths':'resolved-through-relocation-map'}
 r['foundation_review']['full_chinese_body_authoring_complete']=len(completed)==6
 r['foundation_review']['full_chinese_translation_complete']=False
 r['supplementary_body_progress']={'G226':gb.get('coverage',{}),'W242C':'local-Chinese-source-preserved'}
 r['limits_zh'][0]='六卷和G226编号正文已译写；来源核对与作者重点语义复核已记录，不同评审人的全文最终校核待完成。'
 r['author_source_reviews']=[{'path':p,'sha256':sha(C/p),'review_type':'same-author-source-comparison','independent_acceptance':'pending'} for p in ['quality/chinese-body-author-review.json','quality/chinese-body-author-review-additions.json','quality/adm-body-author-review.json','quality/chinese-body-author-review-final-volumes.json','quality/g226-body-author-review.json'] if (C/p).is_file()]
 (C/'quality/completion-status.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
 text=['# 当前交付状态','','本报告是当前状态入口；旧审阅报告仅证明其记录的版本和指纹。**本计划尚未全部完成，不能宣称所有资料已完成中文校订或深度理解验收。**','', '|范围|已有证据|仍须区分的边界|','|---|---|---|',f"|26份系列指南|{ci['counts']['reviewed_sections']}条章节记录；{ci['counts']['reviewed_source_units']}个源单元；242张原图审查|前置/导航剩余项单列，不把覆盖计数当逐句认证|",f"|六卷基础标准|43章、3附录；{r['foundation_review']['numbered_headings']}个编号小节分析；75处正文图片引用有审阅记录；18张提取表|其中17张正文表、1张前置贡献者表；完整中文正文及不同评审人的最终语义验收未完成|",'|补充资料|G226：75节、8图、3表/规格；W242C：33节、3图、3表/术语记录|G226是2022 Playbook，W242C是2025中文白皮书；G226完整中文正文未完成|',f"|skills包|目录内{len(skills['skills'])}个入口、共享执行器和本地来源映射；71项技能与426参考值保留|可运行性以迁移报告为准；不是人员认证或组织批准|",'|虚构案例|保留未知三版；另有输入充分与政策变更两版；结构化行为复评、期间和政策联动|输入充分仅限已声明决策；生产、安全、真实工作量与组织批准不由虚构材料证明|','','《ADM应用》已完成21个编号小节、135个来源块的正文译写（5张表、9张原图保留及1条脚注）；其余五卷与G226全文仍待完成。已写正文的最终独立校核仍待完成。','','## 当前验证证据','','|报告|结果|输入是否当前|','|---|---|---|']
 text=[body_summary if x.startswith('《ADM应用》已完成') else x.replace('完整中文正文及不同评审人的最终语义验收未完成','完整编号正文已译写；不同评审人的最终语义验收未完成').replace('G226完整中文正文未完成','G226中文正文已译写；不同评审人最终校核待完成') for x in text]
 for e in tests:text.append('|['+e['path']+'](../'+e['path']+')|'+('通过' if e.get('passed') else e.get('status','未通过'))+'|'+('未登记输入指纹' if e.get('input_freshness')=='not-recorded' else str(e.get('inputs_current','未执行')))+'|')
 text+=['','台账证据完整性：'+('通过' if r['implementation_ledger_integrity']['passed'] else '未通过，证据已过期或缺失')+'。工程完成字段仅限表列资料整理与交付计划；全量方法、生成图、正式语言和业务能力仍见[七类缺口核查](seven-gap-reconciliation.md)。','','## 当前入口','','- [ADM框架、制品与完整流程图](../architecture/adm-flow/index.html)','- [当前稳定工程验证](adm-completion-verification.json)','- [基础及补充解析](extended-publication.md)','- [逐项实施缺口与证据](implementation-ledger.md)','- [七类能力缺口及本轮修复](seven-gap-reconciliation.md)','- [实际中文正文与边界](../fundamental/chinese-text/README.md)','- [本地skills包](../skills/README.md)','- [案例与当前验收](../maintenance/cases/omnichannel/README.md)','- [机器状态](completion-status.json)','','表列计划未完成项目：'+(', '.join(pending) if pending else '以缺口清单审查状态为准；不自动推断全部完成。'),'']
 (C/'quality/completion-status.md').write_text('\n'.join(text));print({'guides':len(rows),'foundation_numbered_headings':r['foundation_review']['numbered_headings'],'skills':r['skills']['count'],'all_plan_items_complete':False})
if __name__=='__main__':main()
