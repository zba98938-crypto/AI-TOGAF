"""Derive stable, evidence-scoped work items without upgrading acceptance."""
import hashlib
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];REV=ROOT/'reviews'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def build():
    status=load(REV/'capability-status.json');unified=load(REV/'source-coverage-unified.json');cap=load(ROOT/'capabilities.json');items=[]
    def add(identity,kind,scope,action,dependencies=None,**extra):
        items.append({'id':identity,'kind':kind,'scope':scope,'status':'pending','accepted':False,
          'action':action,'depends_on':dependencies or [],**extra})
    for entry in status['capabilities']:
        category=entry['category'];identity=entry['id'];key=category+':'+identity
        if not entry['accepted']:
            dims=entry.get('acceptance_evaluation',{}).get('dimensions',{})
            add('accept:'+key,'acceptance-evidence-missing',{'category':category,'id':identity},
              '核对适用七维实际证据；代码已存在不等于待重写，证据缺失不等于功能缺失。',
              dimensions={k:v.get('status','pending') for k,v in dims.items()},evidence_path='reviews/capability-status.json')
        if category=='deliverable':
            titles=sorted({title for g in entry['generation'].get('unbound_sections',[]) for title in g.get('titles',[])})
            for title in titles:
                suffix=hashlib.sha256(title.encode()).hexdigest()[:12]
                add('chapter:'+identity+':'+suffix,'chapter-content-binding',{'deliverable_id':identity,'section_title':title},
                  '建立同一主场景原料、实际章节绑定、修改及缺输入反例；不得拿独立项目补充附录抵主场景。',
                  ['source:'+category+':'+identity],closure_requires=['baseline','modified','negative','independent-content-review'])
        if category=='analysis-method':
            add('method:'+identity,'method-current-semantic-replay',{'method_id':identity},
              '按实际方法路线运行并独立核推理、修改与反例；保留历史过期记录，不只换哈希。',
              ['source:'+category+':'+identity],historical_status=entry['analysis'].get('status'))
        add('source:'+key,'source-definition-review',{'category':category,'id':identity},
          '逐能力核实际来源资产、定位、定义和适用条件；缺正式资料记外部依赖。',
          evidence_status=entry.get('definition',{}).get('status'))
    for w in cap['work_products']:
        source_id='source:guide-work-product:'+w['id']
        if not any(i['id']==source_id for i in items):
            add(source_id,'source-definition-review',{'category':'guide-work-product','id':w['id']},'核对新增工作产品的定义、输入输出、分析、验收及来源', evidence_status='awaiting-review')
            add('work-product:'+w['id'],'work-product-implementation-review',{'id':w['id']},'按明确输入和方法生成实际成果，缺输入及修改反例重放',[source_id])
    for p in cap['profiles']:
        if p.get('alias_of'):continue
        source_id='source:view-template:'+p['id']
        if not any(item['id']==source_id for item in items):
            add(source_id,'source-definition-review',{'category':'view-template','id':p['id']},
                '核对新模板的来源定位、定义与适用范围；注册不授予来源验收。', evidence_status='awaiting-review')
        add('template:'+p['id'],'template-modification-review',{'profile_id':p['id'],'artifact_id':p['artifact_id']},
          '核字段表达、语义关系、双布局、实质修改与负例；视觉适用时须实际打开来源及输出。',
          ['source:view-template:'+p['id']],source_refs=p.get('source_refs',[]),
          visual_required=p.get('output_kind','diagram')!='table',source_verified=p.get('template',{}).get('source_verified',False))
    # Route-equal observations are associated, not semantically declared equal.
    groups={}
    for candidate in unified['candidates']:
        resolution=candidate.get('resolution') or {};route={k:sorted(resolution.get(k,[])) for k in ['work_product_ids','profile_ids','method_ids','analysis_method_ids']}
        route['method_contract']=resolution.get('method')
        canonical=json.dumps(route,sort_keys=True)
        key='route:'+hashlib.sha256(canonical.encode()).hexdigest()[:16] if any(route.values()) else 'candidate:'+candidate['id']
        group=groups.setdefault(key,{'candidate_observations':[],'route':route})
        group['candidate_observations'].append({'id':candidate['id'],'status':candidate.get('status'),'observations':candidate.get('observations',[]),'resolution':resolution})
    for identity,group in groups.items():
        add('observation:'+identity,'candidate-routing-review',group['route'],
          '相同登记路由仅共享实施线索，逐条核remaining scope；保留所有候选ID与来源，不凭前缀或相同名称自动语义合并。',**group)
    add('external:official-sources','external-dependency',{'sources':['C220 full body','G238 workbook','G210 figures','corrupt or conflicting source assets']},'取得可合法访问来源；未取得时明确受影响scope，不自编官方内容。')
    add('external:visual-review','external-dependency',{'purpose':'actual original/output image opening'},'先验证审核者图像能力；真实打开与具体观察才可授视觉通过，XML/几何不替代。')
    add('final:freeze-and-regression','integration-release',{'purpose':'current-version engineering and scoped acceptance'},'开发完成后冻结，实际重跑受影响证据与离线复制，审核七维门；外部依赖未满足不宣称整体完成。')
    assert len({x['id'] for x in items})==len(items)
    counts={kind:sum(x['kind']==kind for x in items) for kind in sorted({x['kind'] for x in items})}
    return {'schema_version':'development-backlog/1','status':'planned-not-completed','accepted':False,
      'input_sha256':{str(p.relative_to(ROOT)):sha(p) for p in [REV/'capability-status.json',REV/'source-coverage-unified.json',ROOT/'capabilities.json',Path(__file__)]},
      'counts':counts,'candidate_record_count':len(unified['candidates']),'candidate_route_groups':len(groups),'items':items,
      'limits':['Route association is not semantic equivalence or proof implementation is absent.',
        'All records pending until actual scope-specific execution/review; no automatic acceptance.',
        'Historical evidence is retained; this plan does not refresh execution hashes.']}
def main():
    report=build();(REV/'development-backlog.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps({**report['counts'],'candidate_route_groups':report['candidate_route_groups']},ensure_ascii=False))
if __name__=='__main__':main()
