#!/usr/bin/env python3
"""Offline semantic regressions of reviewed publications and the local case runtime.

Only the two reports beside this file are written. Counterexamples are in memory.
This is a project regression contract, not a new review of every source page and
not an authorization/competence/production-readiness decision.
"""
from pathlib import Path
import copy
import datetime
import hashlib
import json
import os
import runpy
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
CORPUS = HERE.parent
ROOT = CORPUS.parent
CASE = HERE / 'cases/omnichannel'
JSON_REPORT = HERE / 'semantic-regression-report.json'
MD_REPORT = HERE / 'semantic-regression-report.md'
ALLOWED_WRITES = {JSON_REPORT, MD_REPORT}
checks = []
inputs = {}


def guard(event, args):
    if event.startswith('socket.'):
        raise PermissionError('Semantic regression is offline: ' + event)
    if event == 'open':
        path, mode, flags = args
        if ((mode and any(c in mode for c in 'wax+')) or
                flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND)):
            if isinstance(path, int) or Path(os.fsdecode(path)).resolve() not in ALLOWED_WRITES:
                raise PermissionError('Only semantic regression reports may be written: ' + str(path))
    elif event in {'os.remove', 'os.rmdir', 'os.rename', 'os.link', 'os.symlink', 'os.chmod', 'os.utime'}:
        raise PermissionError('Mutation prohibited: ' + event)
    elif event == 'os.mkdir':
        # Existing local runner calls mkdir(exist_ok=True) on this existing path.
        target = Path(os.fsdecode(args[0])).resolve()
        if target != CASE / 'tmp' or not target.is_dir():
            raise PermissionError('Directory creation prohibited: ' + str(target))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tracked(path):
    path = Path(path).resolve()
    inputs[str(path.relative_to(ROOT))] = sha(path)
    return path


def read(path):
    return json.loads(tracked(path).read_text())


def ensure(condition, message, actual=None):
    if not condition:
        raise AssertionError(message + (': ' + json.dumps(actual, ensure_ascii=False) if actual is not None else ''))


def run(identity, assertion, action, basis='project-regression-over-reviewed-source', mutation=None):
    row = {'id': identity, 'assertion_zh': assertion, 'basis': basis}
    if mutation:
        row['in_memory_counterexample'] = mutation
    try:
        row['actual'] = action()
        row['status'] = 'passed'
    except Exception as exc:
        row.update(status='failed', actual={'exception': type(exc).__name__, 'message': str(exc)})
    checks.append(row)


def one(items, field, value):
    rows = [r for r in items if r.get(field) == value]
    ensure(len(rows) == 1, 'Expected exactly one ' + value, len(rows))
    return rows[0]


def node(d, local):
    return one(d['nodes'], 'local_id', local)


def edge(d, local):
    return one(d['edges'], 'id', d['id'] + '#' + local)


def g188(d):
    rejected = {e['id']: e for e in d['rejected_edges']}
    current = {e['id'] for e in d['edges']}
    ids = [d['id'] + '#r%04d' % i for i in range(1, 10)]
    ensure(all(i in rejected and i not in current for i in ids), 'Nine invented ADM sequences must remain rejected')
    ensure(all(rejected[i]['predicate'] == 'sequence' and rejected[i]['semantic_state'] == 'rejected-unobserved' for i in ids), 'Rejected ADM edge semantics changed')
    adm_chain = ['adm_stakeholders','adm_goals','adm_capabilities','adm_readiness','adm_scope','adm_principles','adm_vision','adm_value','adm_risks','adm_soaw']
    forbidden = {(d['id']+'#'+a, d['id']+'#'+b) for a,b in zip(adm_chain, adm_chain[1:])}
    ensure(not any((e['from'], e['to']) in forbidden and e['predicate'] == 'sequence' for e in d['edges']), 'Renamed invented sequence reappeared')
    plans = [e for e in d['edges'] if e['to'] == d['id']+'#d_communication_plan']
    ensure(len(plans) == 1 and plans[0]['from'] == d['id']+'#adm_soaw' and plans[0]['predicate'] == 'produces', 'Communication Plan must originate at SoAW in this figure', plans)
    return {'rejected_ADM_sequences': len(ids), 'communication_plan_producer': plans[0]['from'], 'scope': '图中关系；不消除邻近正文的源文冲突'}


def g206(d):
    old = {kind+'_'+color for kind in ('comm','hub') for color in ('red','purple','blue','teal','green')}
    ensure(not ({n['local_id'] for n in d['nodes']} & old), 'Invented five communities/hubs returned')
    ensure(old <= {n['local_id'] for n in d['rejected_nodes']}, 'Historical community correction lost')
    points = [n for n in d['nodes'] if n['type'] == 'organization_unit']
    ensure(len(points) == 84 and len(d['nodes']) == 92, 'Visible point/annotation coverage changed')
    ensure(all(n['label_en'] is None and n.get('source_label_basis') == 'unlabeled-visible-point' for n in points), 'Anonymous source points acquired fabricated names')
    ensure(all(e['predicate'] == 'association' and e['direction'] == 'undirected' and e['visual']['arrow'] == 'none' and e['cardinality'] is None for e in d['edges']), 'Unlabeled lines acquired direction or cardinality')
    return {'anonymous_points': len(points), 'annotations': len(d['nodes'])-len(points), 'fabricated_communities': 0}


def g212(d):
    response_ids = ['sa','a','swa','n','swd','d','sd']
    for name in response_ids:
        n = node(d, name)
        attrs = n.get('attributes', {})
        ensure('score' not in n and 'score' not in attrs and attrs.get('official_numeric_score') is None, 'No official numeric score may be inferred', name)
    table = one(d['tables'], 'id', 't_likert')
    ensure(len(table['columns']) == 8 and len(table['rows']) == 6 and all(len(r) == 8 for r in table['rows']), 'Expected six conditions by seven answers (42 cells)')
    ensure([c.split()[0] for c in table['columns'][1:]] == ['Strongly','Agree','Somewhat','Neutral','Somewhat','Disagree','Strongly'], 'Response order changed')
    for i, condition in enumerate(['Evolve','Disseminate','Commit','Understand','Validate','Define']):
        row = table['rows'][i]
        ensure(row[0].startswith(condition), 'Condition order changed')
        expected = ['已存在/已满足']*(i+1)+['不存在/未满足']*(6-i)
        ensure(row[1:] == expected, 'Cumulative filled/empty pattern changed', {'condition': condition, 'actual': row[1:]})
    return {'cells': 42, 'fulfilled': 21, 'unfulfilled': 21, 'official_numeric_scores': 0, 'neutral': 'Define/Validate/Understand fulfilled; Commit/Disseminate/Evolve unfulfilled'}


# Independently fixed reviewed matrix coordinates. Counts alone miss swapped Xs.
G217_MARKS = [[],[1,2,6,9,10],[1,2,6,7,8,10],[],[1,2,3,4,5,7,9],[1,2,9],[],[2,3,4,5,9],[3,4,5,9],[3,4,5,6,7],[8,9],[8],[3,4,5,6,7,8,9],[],[8],[8],[],[6,7,8],[2,9],[3,4,5,6],[3,4,5,7,8,9],[3],[],[9]]


def g217(d):
    table = one(d['tables'], 'id', 't_adm')
    ensure(len(table['columns']) == 11 and len(table['rows']) == 24 and all(len(r) == 11 for r in table['rows']), 'Expected transposed 24 x 10 matrix')
    # Figure C-1 has ten phase rows: Preliminary, A–H, and Requirements
    # Management. Phase I is not present in the reviewed source matrix.
    ensure(table['columns'][1:] == ['Preliminary Phase']+['Phase '+c for c in 'ABCDEFGH']+['ADM Architecture Requirements Management'], 'ADM column order changed')
    ensure(all(cell in ('', '×') for row in table['rows'] for cell in row[1:]), 'Unknown matrix symbol')
    marks = [[i for i,cell in enumerate(row) if i and cell == '×'] for row in table['rows']]
    ensure(marks == G217_MARKS, 'Reviewed X coordinates changed', marks)
    count = sum(map(len, marks))
    ensure(count == 64, 'Expected 64 source Xs', count)
    row = table['rows'][11]
    ensure(row[0] == 'Development Support Services（分类带）' and row[8] == '×', 'Classification-band source X in Phase G must be preserved')
    return {'rows':24,'data_cells':240,'phase_columns':table['columns'][1:],'source_Xs':count,'classification_band_G_X':'preserved; not a new service'}


def g249_roles(d, retrieval=False):
    for name, side in [('business_domain','左'),('tech_domain','右')]:
        n = node(d, name)
        ensure(n['position'] == '连续灰色域范围的'+side+'侧标签', 'Separate domain box interpretation returned', n['position'])
        ensure(n['visual_parent'] == d['id']+'#domain_scope' and n['group_parent'] == d['id']+'#domain_scope', 'Domains lost shared visual scope')
    ensure('连续灰色' in node(d,'domain_scope')['description_zh'], 'Single shared gray scope missing')
    ensure(all(e.get('cardinality') is None for e in d['edges']), 'Unsupported role relationship cardinality')
    if retrieval:
        ensure(all('source_element' not in n and 'source_position' not in n for n in d['nodes']), 'Historical node payload leaked into current retrieval')
        ensure('左侧灰色大框' not in json.dumps(d,ensure_ascii=False) and '右侧灰色大框' not in json.dumps(d,ensure_ascii=False), 'Old domain boxes leaked into retrieval')
    return {'domain_labels':2,'shared_gray_scope':1,'unsupported_role_cardinalities':0}


def g249_blocks(d, retrieval=False):
    e = edge(d,'r0005')
    ensure(e['predicate'] == 'contains' and e['cardinality'] == 'unspecified:1..*', 'Unprinted containing-end cardinality invented', e.get('cardinality'))
    ensure(e['endpoint_cardinalities'] == {'from':None,'to':'1..*','basis':'nested-building-block-count-only'}, 'Nested count incorrectly became two-end association')
    ensure(e['visual']['explicit_connection'] is False, 'Containment became a printed connector')
    if retrieval:
        ensure('source_relation' not in e, 'Historical false cardinality leaked into retrieval')
    return {'r0005_cardinality':e['cardinality'],'from_cardinality':None,'to_cardinality':'1..*','explicit_connector':False}


def counterexample(checker, original, mutate):
    damaged = copy.deepcopy(original)
    mutate(damaged)
    try:
        checker(damaged)
    except AssertionError as exc:
        return {'rejected':True,'reason':str(exc)}
    raise AssertionError('Counterexample was accepted')


def protected_hashes():
    # Current case products and the shared runtime are evidence, never test output.
    return {str(p.relative_to(ROOT)):sha(p) for base in (CASE,CORPUS/'skills') for p in base.rglob('*')
            if p.is_file() and '__pycache__' not in p.parts and p.name != '.DS_Store'}


def synchronize(m):
    """Keep model, reasoning inputs, and bound snapshots consistent after mutation."""
    d = m['analyses'][0]['inputs']
    entities = {e['id']:e for e in m['entities']}
    relations = {r['id']:r for r in m['relationships']}
    for key in ('requirements','assessments'):
        for row in d[key]:
            relation = relations[row['id']]
            relation['attributes'] = {k:copy.deepcopy(v) for k,v in row.items() if k not in {'id','skill_id','role_ref','evidence'}}
            if key == 'requirements':
                relation['attributes']['task_refs'] = [row['task_ref']]
                relation['target'] = row['role_ref']
            relation['evidence'] = copy.deepcopy(row['evidence'])
    for row in d['development']:
        entities[row['id']]['attributes'].update(copy.deepcopy(row))
    for row in d['assessments']:
        ident = 'EVIDENCE-EXPERT' if row['person_ref'] == 'PERSON-EXPERT' else 'EVIDENCE-A'
        entities[ident]['attributes'].update(state=row['assessment_state'],current_proficiency=row.get('proficiency'),behavioral_evidence=copy.deepcopy(row['behavioral_evidence']))
    for row in d['tasks']:
        entities[row['id']]['attributes']['workload_hours'] = row.get('workload_hours')
    selected = {i for t in d['tasks'] for i in t['model_object_refs']}
    d['model_objects'] = copy.deepcopy([e for e in m['entities'] if e['id'] in selected])
    d['model_relationships'] = copy.deepcopy([r for r in m['relationships'] if r['source'] in selected and r['target'] in selected])
    intended = {a for t in d['tasks'] for a in t['artifact_ids']}
    d['model_views'] = copy.deepcopy([v for v in m['views'] if v['artifact_id'] in intended])
    entities[d['model_binding']['context_ref']]['attributes']['assessment_inputs'] = copy.deepcopy(d)


def runtime_checks():
    ns = runpy.run_path(str(tracked(CASE/'run.py')), run_name='semantic_regression_runtime')
    base = ns['base']
    from analysis_binding import binding_issues
    m = ns['build'](True)

    def evaluate(model):
        a = model['analyses'][0]
        issues = binding_issues(model, a)
        ensure(not issues, 'Mutation is invalid because binding is stale; not a semantic rejection', issues)
        return base.evaluate(a,model)['result']

    def baseline():
        errors = [x for x in base.validate(m) if x['level']=='error']
        ensure(not errors,'Current case has structural errors',errors)
        r = evaluate(m)
        a = one(r['assignment_reviews'],'id','ASSIGN-A')
        ensure(a['capacity_state']=='unresolved' and a['approval']=='not-granted' and a['state']=='needs-evidence','Unknown capacity or approval silently granted',a)
        ensure(any(g['reason']=='capacity-unresolved' for g in r['gaps']),'Missing capacity gap')
        return {'structural_errors':errors,'gap_count':len(r['gaps']),'assignment':a,'business_approval':'not-granted'}
    run('CASE-BASELINE','实际调用 case build(True)、validate、evaluate；结构有效仍保留未知容量与未批准',baseline,'project-runtime-behavior')

    def invalid_level(collection):
        mutated = copy.deepcopy(m)
        row = mutated['analyses'][0]['inputs'][collection][0]
        row['proficiency'] = 99
        synchronize(mutated)
        try:
            evaluate(mutated)
        except ValueError as exc:
            ensure(str(exc).startswith('G249-LEVEL '),'Expected semantic G249-LEVEL rejection, not incidental failure',str(exc))
            return {'rejected':True,'code':'G249-LEVEL','binding_errors':0,'message':str(exc)}
        raise AssertionError('99 was accepted')
    for collection in ('requirements','assessments'):
        run('CASE-99-'+collection,'99 超出四级量表，必须由实际评价器拒绝',lambda c=collection:invalid_level(c),'project-runtime-behavior',collection+'[0].proficiency = 99; synchronize bound model')

    def missing_level(delete):
        mutated = copy.deepcopy(m)
        row = mutated['analyses'][0]['inputs']['requirements'][0]
        if delete: row.pop('proficiency')
        else: row['proficiency']=None
        synchronize(mutated)
        r = evaluate(mutated)
        result = one(r['requirement_reviews'],'id',row['id'])
        ensure(result['state']=='needs-input' and result['proficiency'] is None,'Missing level became a completed requirement',result)
        gap = one(r['gaps'],'id',row['id']+':proficiency')
        ensure(gap['reason']=='missing-input','Expected explicit missing-input gap',gap)
        ensure(all(a['approval']=='not-granted' for a in r['assignment_reviews']),'Approval granted with missing input')
        return {'hard_exception':False,'rejected_as_complete':True,'binding_errors':0,'requirement':result,'gap':gap,'semantic_boundary':'待补草稿有效；不得宣称等级齐备或人员达标。不是缺字段必抛异常。'}
    for delete in (False,True):
        run('CASE-MISSING-'+('absent' if delete else 'null'),'缺等级拒绝判为完备，保留未知而不默认为 1',lambda d=delete:missing_level(d),'project-runtime-behavior','Remove proficiency' if delete else 'proficiency = null')

    def training():
        mutated=copy.deepcopy(m)
        d=mutated['analyses'][0]['inputs']
        before=copy.deepcopy(d['assessments'])
        dev=d['development'][0]
        dev['action']='培训活动已完成（虚构反例）；没有新增能力行为评价'
        dev['reassessment'].update(status='completed',evidence=['CASE-REVIEW'])
        dev['reassessment'].pop('assessment_ref',None)
        synchronize(mutated)
        r=evaluate(mutated)
        result=one(r['development_reviews'],'id',dev['id'])
        ensure(result['rating_change']=='not-inferred' and result['state']=='needs-input','Training became competency upgrade',result)
        ensure(any(g['id']==dev['id']+':reassessment.assessment_ref' and g['reason']=='missing-reassessment' for g in r['gaps']),'Completion without reassessment not flagged')
        ensure(d['assessments']==before and dev['current_proficiency'] is None,'Evaluator modified observed rating')
        return {'development':result,'missing_reassessment':True,'current_proficiency':None,'assessments_unchanged':True,'binding_errors':0}
    run('CASE-TRAINING','完成培训／宣称复评完成，没有新行为评审不能自动升级',training,'project-runtime-behavior','Mark reassessment completed without assessment_ref')

    def forged_official(tier):
        mutated=copy.deepcopy(m)
        ref=one(mutated['relationships'],'id','REF-REQ-SKILL-EA')
        ref['target']='ROLE-CHIEF' if tier=='chief' else 'ROLE-SEG'
        synchronize(mutated)
        ensure(not binding_issues(mutated,mutated['analyses'][0]),'Forged official test has stale binding')
        findings=base.validate(mutated)
        matches=[x for x in findings if x['level']=='error' and x['code']=='source-role-column' and x['id']==ref['id']]
        ensure(matches,'Chief/Segment acquired an official column',findings)
        return {'rejected_by':'model.validate/proficiency_semantics','errors':matches,'binding_errors':0,'note':'此项调用模型校验；不将 evaluate 单独冒称完整的模型校验。'}
    for tier in ('chief','segment'):
        run('CASE-OFFICIAL-'+tier,'Chief／通用 Segment 无官方独立等级列，模型校验必须拒绝伪装',lambda t=tier:forged_official(t),'project-runtime-behavior','Retarget official EA reference to '+tier+' role')

    def role_review(reporting=False):
        mutated=copy.deepcopy(m)
        data=mutated['analyses'][0]['inputs']
        roles=[]
        for source in data['roles']:
            e=one(mutated['entities'],'id',source['id'])
            row={'id':e['id'],'name':e['name'],'evidence':copy.deepcopy(e['evidence']),**copy.deepcopy(e['attributes'])}
            roles.append(row)
        sol=one(roles,'id','ROLE-SOL'); peer=copy.deepcopy(sol)
        peer.update(id='ROLE-SOL-PEER',name='同级协作解决方案架构师（内存反例）')
        roles.append(peer)
        kind='reports_to' if reporting else 'architecture_guidance'
        sol['relationships']=[{'id':'LATERAL-A','type':kind,'target':peer['id'],'scope':'候选接口相互评审','evidence':['CASE-REVIEW']}]
        peer['relationships']=[{'id':'LATERAL-B','type':kind if reporting else 'collaborates_with','target':sol['id'],'scope':'候选接口相互评审','evidence':['CASE-REVIEW']}]
        for role in (sol,peer):
            if reporting: role['relationships'][0].update(authority='虚构项目授权',valid_from='2026-11-07',valid_until='2026-11-30')
        for row in roles:
            e=next((e for e in mutated['entities'] if e['id']==row['id']),None)
            if e is None:
                e={'id':row['id'],'type':'guide:architecture-role','certainty':'assumed'};mutated['entities'].append(e)
            e.update(name=row['name'],evidence=copy.deepcopy(row['evidence']),attributes={k:copy.deepcopy(v) for k,v in row.items() if k not in {'id','name','evidence'}})
        analysis={'id':'semantic-role-review','method_id':'architecture-role-catalog-review','inputs':{'source_ids':data['source_ids'],'roles':roles},'evidence':['CASE-REVIEW']}
        ensure(not binding_issues(mutated,analysis),'Role counterexample has stale model binding',binding_issues(mutated,analysis))
        try:r=base.evaluate(analysis,mutated)['result']
        except ValueError as exc:
            ensure(reporting and str(exc).startswith('ROLE-REPORT-CYCLE '),'Unexpected role failure',str(exc))
            return {'rejected':True,'code':'ROLE-REPORT-CYCLE','binding_errors':0}
        ensure(not reporting,'Reporting cycle accepted')
        ensure(r['hierarchy_policy'] is None and {x['id'] for x in r['relationships']}=={'LATERAL-A','LATERAL-B'},'Lateral relationships lost')
        return {'accepted_relationships':r['relationships'],'hierarchy_policy':None,'gaps':len(r['gaps']),'binding_errors':0,'boundary':'允许有证据的同级专业指导与协调；缺少职责细节仍待补，不代表组织批准。'}
    run('CASE-LATERAL','没有项目强制职级政策时，同级专业指导与协作循环允许',role_review,'project-runtime-behavior','Same-tier guidance plus reverse collaboration in a bound case model')
    run('CASE-REPORT-CYCLE','组织汇报循环仍应拒绝，避免同级协调规则过度放宽',lambda:role_review(True),'project-runtime-behavior','Replace the pair with a reports_to cycle')


def main():
    protected_before=protected_hashes()
    sys.addaudithook(guard)
    tracked(Path(__file__))
    chunks_path=tracked(CORPUS/'retrieval/architecture-chunks.jsonl')
    chunks=[json.loads(line) for line in chunks_path.read_text().splitlines() if line.strip()]
    fixtures={}
    validators={'G188/fig4-2':g188,'G188/fig5-1':g188,'G206/fig2-1':g206,'G212/figA-1':g212,'G217/figC-1':g217,'G249/fig4-1':g249_roles,'G249/fig4-2':g249_blocks}
    for figure,checker in validators.items():
        d=read(CORPUS/'architecture/diagrams'/ (figure+'.json'))
        fixtures[figure]=d
        run('PUB-'+figure,'当前发布图语义保持已审阅事实',lambda d=d,c=checker:c(d))
        def retrieval(f=figure,c=checker):
            parts=sorted([x for x in chunks if x['parent_record_id']=='diagram:'+f],key=lambda x:x['part'])
            ensure(parts and [x['part'] for x in parts]==list(range(1,len(parts)+1)),'Retrieval parts missing/duplicated')
            ensure(all(x['part_count']==len(parts) for x in parts),'Retrieval part count differs')
            ensure(all(x['source_sha256']==sha(CORPUS/'architecture/diagrams'/(f+'.json')) for x in parts),'Retrieval source hash stale')
            text=''.join(x['text'] for x in parts)
            value=json.loads(text.split('\n',1)[1])
            result=c(value,True) if f.startswith('G249') else c(value)
            result['retrieval_parts']=len(parts)
            return result
        run('RAG-'+figure,'当前检索重组后保持语义及来源指纹；不能只测磁盘 JSON',retrieval)
    negatives=[
        ('ADM-SEQUENCE','G188/fig5-1',g188,lambda d:d['edges'].append(copy.deepcopy(d['rejected_edges'][0])),'Restore one rejected ADM sequence'),
        ('COMM-PLAN','G188/fig5-1',g188,lambda d:edge(d,'r0015').update({'from':d['id']+'#adm_risks'}),'Move Communication Plan origin back to risks'),
        ('COMMUNITY','G206/fig2-1',g206,lambda d:next(n for n in d['nodes'] if n['type']=='organization_unit').update(label_en='Red Community'),'Invent community label on anonymous point'),
        ('SCORE','G212/figA-1',g212,lambda d:node(d,'sa')['attributes'].update(score=7),'Restore invented score=7'),
        ('42-CELLS','G212/figA-1',g212,lambda d:d['tables'][0]['rows'][0].pop(),'Remove one of 42 cells'),
        ('SAME-COUNT-SWAP','G212/figA-1',g212,lambda d:d['tables'][0]['rows'][0].__setitem__(slice(1,3),['不存在/未满足','已存在/已满足']),'Swap filled/empty cells without changing count'),
        ('64-X','G217/figC-1',g217,lambda d:d['tables'][0]['rows'][11].__setitem__(8,''),'Remove classification-band G X'),
        ('X-COORDINATE','G217/figC-1',g217,lambda d:d['tables'][0]['rows'][11].__setitem__(slice(7,9),['×','']),'Move X to another phase while retaining 64 Xs'),
        ('TWO-DOMAIN-BOXES','G249/fig4-1',g249_roles,lambda d:node(d,'business_domain').update(position='左侧灰色大框'),'Restore independent left domain box'),
        ('INVENTED-CARDINALITY','G249/fig4-2',g249_blocks,lambda d:edge(d,'r0005').update(cardinality='1..* → 1..*'),'Invent source-end cardinality on nested containment')]
    for ident,fig,checker,mutate,description in negatives:
        run('NEG-'+ident,'注入曾见误读，检查器必须拒绝',lambda c=checker,d=fixtures[fig],m=mutate:counterexample(c,d,m),mutation=description)
    run('RUNTIME-SUITE','加载本地案例与共享只读运行时，执行业务语义反例',runtime_checks,'project-runtime-loading')
    # Record precisely which loaded runtime modules participated in this run.
    for module in list(sys.modules.values()):
        filename=getattr(module,'__file__',None)
        if filename:
            path=Path(filename).resolve()
            if path.is_file() and (CORPUS/'skills' in path.parents or CASE in path.parents):tracked(path)
    for path in [CASE/'role-skill-inputs.json',CASE/'raw-business-materials.md',CORPUS/'skills/_shared/references/source-tables/g249-skill-proficiency.json',CORPUS/'skills/_shared/references/g249/skill-task-map.json']:
        tracked(path)
    def unchanged():
        after=protected_hashes()
        delta=sorted(k for k in set(protected_before)|set(after) if protected_before.get(k)!=after.get(k))
        ensure(not delta,'Protected case/skills files changed',delta)
        return {'files_hashed':len(after),'changed':delta,'network':'blocked by audit hook','write_allowlist':[str(x.relative_to(ROOT)) for x in sorted(ALLOWED_WRITES)]}
    run('BOUNDARY-READONLY','skills 与 case 文件前后逐字节指纹一致，反例只在内存中',unchanged,'execution-boundary')
    failed=[x['id'] for x in checks if x['status']=='failed']
    report={'schema_version':'semantic-regression/1','executed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':'python3 togaf-standard-10th-ai/maintenance/semantic-regression.py','result':'failed' if failed else 'passed','counts':{'checks':len(checks),'passed':len(checks)-len(failed),'failed':len(failed)},'failed_checks':failed,'scope_zh':'7 张已发布图及其当前检索；本地全渠道案例 build/validate/evaluate；已识别误读的正例与内存反例。','limits_zh':['这些是项目回归断言；本轮未重新逐页视觉审阅全部官方出版物。','通过只确认已列语义边界与反例行为，不确认真实人员胜任、培训有效、业务方案充分或组织批准。','缺等级实际行为为 missing-input/needs-input，拒绝判为完备而非必抛异常；99 为 G249-LEVEL 硬拒绝。','历史 source_element/source_relation 保留在审计文件，当前检索不得复用旧错误语义；不能要求全文删除历史字符串。','脚本不联网，只写两个 maintenance 报告，未调用 case 主程序或生成器。'],'input_sha256':dict(sorted(inputs.items())),'checks':checks}
    JSON_REPORT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    lines=['# 已发布语料与本地案例的语义回归','',f"执行结果：**{report['result']}**；{len(checks)} 项，{len(checks)-len(failed)} 通过，{len(failed)} 失败。",'',f"执行时间：{report['executed_at']}",'','重跑：`'+report['command']+'`','',report['scope_zh'],'','| 检查 | 结果 | 实际观察 |','|---|---|---|']
    for row in checks:
        actual=json.dumps(row['actual'],ensure_ascii=False)
        if len(actual)>950:actual=actual[:950]+'…（完整实际结果见 JSON）'
        lines.append('| '+row['id']+' | '+row['status']+' | '+actual.replace('|','\\|').replace('\n',' ')+' |')
    lines+=['','边界与解释：','']+['- '+x for x in report['limits_zh']]+['','所有输入 SHA-256、反例变更与完整实际结果见 [JSON 报告](semantic-regression-report.json)。','']
    MD_REPORT.write_text('\n'.join(lines))
    print(json.dumps({'result':report['result'],'counts':report['counts'],'failed_checks':failed,'report':str(JSON_REPORT)},ensure_ascii=False))
    return 1 if failed else 0


if __name__=='__main__':
    raise SystemExit(main())
