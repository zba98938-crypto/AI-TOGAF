#!/usr/bin/env python3
"""Forward checks of the authored dossier and saved formal outputs; no builder import.

These are bounded source/output assertions and adversarial cases. They are not
independent professional acceptance of all 90 authored chapters.
"""
from pathlib import Path
import argparse
import copy
import hashlib
import json
import re
import sys
from urllib.parse import unquote, urlsplit

H=Path(__file__).resolve().parent
C=H.parents[2];S=C/'skills/_shared'
sys.path[:0]=[str(S/'scripts'),str(S/'vendor')]
sys.dont_write_bytecode=True
from adm import check_cycle
from architecture_delivery import output_check
from deliverable_assembly import assemble
from registry import load as registry

def load(path):return json.loads(Path(path).read_text())
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def digest(value):return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def save(path,value):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def generated_markdown_links(directory):
    """Check the generator's inline local links, including images, in actual files."""
    checked=[];missing=[]
    for path in sorted(directory.rglob('*.md')):
        text=re.sub(r'```[^\n]*\n.*?```','',path.read_text(),flags=re.S)
        text=re.sub(r'`[^`\n]*`','',text)
        for match in re.finditer(r'!?\[[^\]]*\]\(([^)]+)\)',text):
            url=match[1].strip('<>');parsed=urlsplit(url)
            if parsed.scheme or parsed.netloc or not parsed.path:continue
            target=(path.parent/unquote(parsed.path)).resolve()
            row={'file':str(path.relative_to(directory)),'target':url,'exists':target.is_file()}
            checked.append(row)
            if not row['exists']:missing.append(row)
    return checked,missing

def binding_findings(material,model,cycle,mapping):
    """Compare source-authored decisions, exact supporting objects and phase outputs."""
    issues=[]
    _,contracts,_,_=registry()
    specs={r['deliverable_id']:r for r in material['deliverables']}
    actual={r['deliverable_id']:r for r in model['deliverables']}
    if set(specs)!=set(contracts) or set(actual)!=set(contracts) or len(actual)!=len(model['deliverables']):
        issues.append('formal-deliverable-coverage')
    entities={r['id']:r for r in model['entities']}
    window=material['planning']['experiment_window']
    for identity in ('WP-ONLINE','WP-OFFLINE','TRANS-ONLINE','TRANS-OFFLINE','RISK-STOCK'):
        attrs=entities.get(identity,{}).get('attributes',{})
        if any(attrs.get(key)!=window[key] for key in ('start','end')):
            issues.append('experiment-window-mismatch:'+identity)
        if not attrs.get('schedule_semantics'):
            issues.append('experiment-schedule-semantics-missing:'+identity)
        if not {'ADM-INPUT-F','ADM-DELIVERY-BRIEF'}<=set(entities.get(identity,{}).get('evidence',[])):
            issues.append('experiment-schedule-source-missing:'+identity)
    if entities.get('RISK-STOCK',{}).get('attributes',{}).get('due_date')!=window['end']:
        issues.append('experiment-risk-deadline-mismatch')
    links={r['deliverable_id']:r for r in mapping}
    for did,spec in specs.items():
        if did not in actual:continue
        item=actual[did]
        if item.get('approval_status')!='candidate' or item.get('implementation_status')!='not-started':issues.append('fabricated-delivery-acceptance:'+did)
        if links.get(did,{}).get('phases')!=spec['phases'] or links.get(did,{}).get('source_material_sha256')!=digest(spec):issues.append('stale-phase-material-map:'+did)
        if not spec.get('scope_rationale') or spec.get('applicability')!='applicable-scenario-draft':issues.append('missing-applicability:'+did)
        source_titles=[r['title'] for r in spec['sections']]
        if source_titles!=[r['title'] for r in contracts[did]['sections']] or set(item['sections'])!=set(source_titles):issues.append('chapter-coverage:'+did)
        for chapter in spec['sections']:
            title=chapter['title'];key=did+':'+title
            if item['sections'].get(title)!=chapter['conclusion']:issues.append('stale-chapter-prose:'+key)
            binding=item.get('assembly',{}).get('section_bindings',{}).get(title,{})
            records=[entities[i] for i in binding.get('entity_ids',[]) if i in entities and entities[i]['type']=='project:section_evidence']
            if len(records)!=1:issues.append('missing-or-duplicate-chapter-evidence:'+key);continue
            record=records[0];a=record['attributes']
            if a.get('deliverable_id')!=did or a.get('section_title')!=title or a.get('conclusion')!=chapter['conclusion'] or a.get('source_material_sha256')!=digest(chapter):issues.append('stale-chapter-record:'+key)
            if a.get('status')!='scenario-proposal' or a.get('authority')!='scenario-authority':issues.append('fabricated-chapter-acceptance:'+key)
            if a.get('unknowns')!=spec['unknowns'] or not a.get('unknowns'):issues.append('lost-real-world-gaps:'+key)
            if not set(spec['support_ids'])<=set(binding.get('entity_ids',[])):issues.append('unbound-domain-support:'+key)
            if not {'ADM-DELIVERY-BRIEF',*('ADM-INPUT-'+p for p in chapter['source_anchors'])}<=set(record.get('evidence',[])):issues.append('missing-raw-source:'+key)
        for phase in spec['phases']:
            if phase=='Requirements':continue
            step=next((p for p in cycle['phases'] if p['phase']==phase),None)
            if not step or {'collection':'deliverables','id':item['id']} not in step['iterations'][-1]['output_refs']:issues.append('formal-output-not-in-phase:'+did+':'+phase)
    if model['project'].get('approval_status')!='candidate' or not model['project'].get('is_example'):issues.append('fictional-project-boundary-lost')
    return issues


def run(folder):
    folder=folder.resolve()
    material=load(folder/'materials/adm-delivery-materials.json');model=load(folder/'model.json');cycle=load(folder/'cycles/cycle.json');mapping=load(folder/'stage-deliverable-map.json')
    rows=[]
    def check(identity,fn):
        try:detail=fn();rows.append({'id':identity,'passed':True,'detail':detail})
        except Exception as e:rows.append({'id':identity,'passed':False,'detail':str(e)})
    def require(value,message):
        if not value:raise AssertionError(message)
    def raw_sources():
        for name,expected in material['raw_source_files'].items():require(sha(folder/'materials'/name)==expected,'raw material drift '+name)
        require(sha(folder/'materials/adm-delivery-materials.json')==sha(H/'adm-delivery-materials.json'),'current authored material changed')
        return 'Two original raw sources retained byte-for-byte; new delivery dossier explicitly declared as added authored material.'
    check('raw-inputs-and-added-material-version',raw_sources)
    def bindings():
        errors=binding_findings(material,model,cycle,mapping);require(not errors,str(errors))
        return {'deliverables':len(model['deliverables']),'chapters':sum(len(d['sections']) for d in model['deliverables']),'stage_output_refs':sum(len(p['iterations'][-1]['output_refs'])-1 for p in cycle['phases'])}
    check('same-model-23-deliverables-90-chapters-and-phase-bindings',bindings)
    def adm():
        r=check_cycle(cycle,model,folder/'cycles');require(not r['errors'] and r['recorded_cycle_complete'] and r['foundation_source_coverage_complete'],str(r['errors']))
        require(sum(p['source_step_coverage']['expected_count'] for p in r['phases'])+r['requirements_source_step_coverage']['expected_count']==94,'lost ADM source steps')
        for phase in cycle['phases']:
            ev=phase['iterations'][-1]['decision']['evidence']
            require(any(e['path'].endswith('adm-delivery-materials.json') for e in ev),'new output material missing from phase evidence')
        return '9 phases and continuous requirements retain 94 steps; added candidate outputs are bound to new material, not retroactively approved.'
    check('current-94-step-cycle-and-new-material-evidence',adm)
    manifest=load(folder/'generated/manifest.json')
    def outputs():
        require(manifest['model_sha256']==digest(model),'saved output belongs to another model')
        require(len(manifest['deliverables'])==23,'23 actual output files required')
        for row in manifest['deliverables']:
            text=(folder/'generated'/row['path']).read_text();payload=load(folder/'generated'/row['json']);did=row['id']
            authored=next(d for d in material['deliverables'] if d['deliverable_id']==did)
            require(payload['assembly']['status']=='assembled-awaiting-review' and not payload['assembly']['unbound_section_titles'],'strict assembly incomplete '+did)
            require(payload['deliverable']==next(d for d in model['deliverables'] if d['deliverable_id']==did),'saved JSON differs '+did)
            for chapter in authored['sections']:require(chapter['conclusion'] in text,'actual Markdown lost content '+did+':'+chapter['title'])
            require(payload['assembly']['content_status']=='all-sections-bound-business-review-pending','assembly upgraded business acceptance '+did)
        _,errors=output_check(folder/'generated',model);require(not errors,str(errors))
        return {'actual_markdown_files':23,'actual_json_files':23,'generated_views':len(manifest['artifacts']),'output_check':'passed','raster_visual_review':'not-requested-not-claimed'}
    check('actual-saved-assemblies-and-visible-markdown',outputs)
    def links():
        checked,missing=generated_markdown_links(folder/'generated')
        save(folder/'generated-local-links.json',{'passed':not missing,'checked':len(checked),'missing':missing})
        require(checked and not missing,'missing actual local Markdown/image links: '+str(missing))
        assignment=(folder/'generated/artifacts/role-assignment.md').read_text()
        require('PNG 尚未渲染' in assignment and '(role-assignment.png)' not in assignment,'non-rendered PNG remains linked')
        return {'local_links_checked':len(checked),'missing':len(missing),'assignment_png':'not-linked-before-rendering'}
    check('all-actual-non-rendered-markdown-links-resolve',links)
    def numbers():
        raw=(folder/'materials/adm-business-materials.md').read_text()
        o=material['given_observations'];planning=material['planning']
        require('160ms' in raw and '420ms' in raw and '300ms' in raw,'comparison absent from original source')
        require(o['online_A_p95_ms']<=o['online_target_ms']<o['online_B_p95_ms'],'online option inequality')
        require(o['recovery_completed']/o['recovery_population']>=o['recovery_target_ratio'],'recovery threshold')
        require(o['offline_confirmed']+o['offline_manual_exceptions']==o['offline_population'],'observation denominator')
        values=[round(sum(a*b for a,b in zip(w['value_scores'],planning['value_weights'])),1) for w in planning['work_packages']]
        risks=[round(sum(a*b for a,b in zip(w['risk_scores'],planning['risk_weights'])),1) for w in planning['work_packages']]
        require(values==[4.1,3.6] and risks==[2.8,4.0],'value/risk independent arithmetic')
        require(planning['budget_CNY'] is None and planning['ROI'] is None,'financial unknown converted into value')
        require(all(w['estimated_hours']<=w['available_hours'] for w in planning['work_packages']),'experiment resource insufficiency')
        for f in ['architecture-roadmaps','implementation-migration-plan','compliance-assessment']:
            text=(folder/'generated/deliverables'/f'{f}.md').read_text()
            require('真实' in text and ('未知' in text or '未提供' in text),'real-world gaps not visible '+f)
        return {'value':values,'risk':risks,'recovery_ratio':o['recovery_completed']/o['recovery_population'],'offline_confirmation_ratio':o['offline_confirmed']/o['offline_population'],'ROI':None}
    check('raw-source-numeric-and-business-boundaries',numbers)
    def domain_semantics():
        e={x['id']:x for x in model['entities']};contract=e['DELIVERY-NOTE']['attributes']['recovery_contract']
        require([r['source'] for r in model['relationships'] if r['type']=='exposes' and r['target']==contract['interface_ref']]==[contract['central_receiver_ref']],'central recovery provider changed')
        require(not any(r['type']=='transitions_to' and r['target']=='ORDER-FULFIL' and r['source']!='ORDER-CONFIRMED' for r in model['relationships']),'unconfirmed logistics allowed')
        definition=next(d for d in model['deliverables'] if d['deliverable_id']=='architecture-definition-document')['sections']
        require(all(x in definition['基线架构'] for x in ['纸面','缺','人工','单中心']),'four-domain baseline missing')
        require(all(x in definition['目标架构'] for x in ['受理','order/event/reservation/policy','中央预占','认证']),'four-domain target missing')
        require('只排' in material['view_selections']['application-migration-diagram']['rationale'],'schedule selection needs explicit tailoring')
        return 'Central recovery ownership and confirmed-only logistics retained; four-domain baseline/target and schedule selection remain specific.'
    check('cross-domain-semantic-chain',domain_semantics)
    def experiment_schedule():
        raw=(folder/'materials/adm-business-materials.md').read_text()
        require('同一11-17至11-30实验窗口' in raw and '可并行开发日志' in raw,'raw experiment window/dependency basis absent')
        window=material['planning']['experiment_window']
        require(window['start']=='2026-11-17' and window['end']=='2026-11-30','authored schedule drifts from raw')
        e={x['id']:x for x in model['entities']}
        for identity in ['WP-ONLINE','WP-OFFLINE','TRANS-ONLINE','TRANS-OFFLINE','RISK-STOCK']:
            require(all(e[identity]['attributes'][key]==window[key] for key in ['start','end']),'scheduled object drifts: '+identity)
        artifacts={r['view_id']:r for r in manifest['artifacts']}
        for view in ['adm-delivery-application-migration-diagram','transition-roadmap','risk-treatment']:
            row=artifacts[view]
            md=(folder/'generated'/row['path']).read_text()
            svg=(folder/'generated'/row['svg']).read_text()
            require('2026-11-17' in md and '2026-11-30' in md,'actual Markdown lacks correct dates: '+view)
            require('2026-11-09' not in svg and '2026-11-21' not in svg and '2026-12-04' not in svg,'actual SVG retains inherited schedule: '+view)
        changed=copy.deepcopy(model)
        next(e for e in changed['entities'] if e['id']=='WP-OFFLINE')['attributes'].update(start='2026-11-21',end='2026-12-04')
        findings=binding_findings(material,changed,cycle,mapping)
        require('experiment-window-mismatch:WP-OFFLINE' in findings,'old serial schedule accepted')
        save(folder/'counterexamples/old-serial-schedule-findings.json',findings)
        return {'start':window['start'],'end':window['end'],'schedule':'common experiment window; detailed staffing unknown','old_serial_schedule':'rejected','actual_views_checked':3}
    check('raw-experiment-window-in-actual-migration-transition-and-risk-outputs',experiment_schedule)
    _,contracts,_,_=registry()
    def missing_chapter():
        mutated=copy.deepcopy(model);delivery=next(d for d in mutated['deliverables'] if d['deliverable_id']=='architecture-contract')
        title='验收与证据';ids=delivery['assembly']['section_bindings'][title]['entity_ids'];record=next(e for e in mutated['entities'] if e['id'] in ids and e['type']=='project:section_evidence')
        record['attributes']['decision']='';record['evidence']=[]
        result=assemble(mutated,delivery,contracts[delivery['deliverable_id']]);save(folder/'counterexamples/missing-chapter-assembly.json',result)
        require(result['status']=='blocked','missing evidence allowed strict assembly')
        return [r['code'] for r in result['gaps']]
    check('missing-chapter-evidence-blocks-strict-assembly',missing_chapter)
    def false_approval():
        mutated=copy.deepcopy(model);mutated['deliverables'][0]['approval_status']='approved'
        errors=binding_findings(material,mutated,cycle,mapping);require(any(e.startswith('fabricated-delivery-acceptance') for e in errors),'false approval accepted')
        save(folder/'counterexamples/false-approval-findings.json',errors);return errors
    check('fictional-acceptance-cannot-become-real-approval',false_approval)
    def unbound():
        mutated=copy.deepcopy(cycle);p=next(p for p in mutated['phases'] if p['phase']=='G');p['iterations'][-1]['output_refs']=[r for r in p['iterations'][-1]['output_refs'] if r['collection']!='deliverables']
        errors=binding_findings(material,model,mutated,mapping);require(any(e.startswith('formal-output-not-in-phase') for e in errors),'phase without formal outputs accepted')
        return errors
    check('removing-formal-stage-output-is-rejected',unbound)
    def changed_material():
        changed=copy.deepcopy(material);row=next(d for d in changed['deliverables'] if d['deliverable_id']=='architecture-requirements-specification')
        row['sections'][1]['conclusion']=row['sections'][1]['conclusion'].replace('2件','1件').replace('24小时','8小时')
        errors=binding_findings(changed,model,cycle,mapping)
        require(any(e.startswith('stale-chapter-prose') for e in errors),'old document accepted changed business requirement')
        save(folder/'counterexamples/policy-material-stale-output.json',{'changed_material':changed,'findings':errors});return errors
    check('changed-business-material-invalidates-old-formal-output',changed_material)
    def policy_change():
        changed=copy.deepcopy(model);p=next(e for e in changed['entities'] if e['id']=='ADM-DELIVERY-POLICY')
        p['attributes']['active_policy']={'version':'V2-candidate','offline_max_items':1,'pending_hours':8}
        report=check_cycle(cycle,changed,folder/'cycles')
        save(folder/'counterexamples/policy-v2-model.json',changed);save(folder/'counterexamples/policy-v2-old-cycle-check.json',report)
        require(not report['recorded_cycle_complete'] and not report['foundation_source_coverage_complete'],'old phase decisions support V2')
        require(not any(x['code']=='model-invalid' for x in report['errors']),'change only failed structural validation')
        require(digest(changed)!=manifest['model_sha256'],'old saved delivery digest supports new policy')
        affected=[p['phase'] for p in report['phases'] if p['gaps']]
        require({'B','C','D','E','F','G'}<=set(affected),'missing affected phase review')
        return {'changed_business_fields':['offline_max_items:2→1','pending_hours:24→8'],'phases_requiring_review':affected,'old_saved_outputs_current':False}
    check('policy-change-invalidates-old-phase-decisions-and-deliveries',policy_change)
    summary={'schema_version':'omnichannel-adm-delivery-forward/1','passed':all(r['passed'] for r in rows),'checks':rows,'counts':{'checks':len(rows),'passed':sum(r['passed'] for r in rows),'failed':sum(not r['passed'] for r in rows)},
        'input_sha256':{str(p.relative_to(C.parent)):sha(p) for p in [H/'adm-delivery-materials.json',folder/'model.json',folder/'cycles/cycle.json',folder/'generated/manifest.json',Path(__file__)]},
        'independence':'separate forward implementation, not different-reviewer professional acceptance',
        'independent_business_accepted':False,'real_approval':'not-granted'}
    save(folder/'forward-acceptance.json',summary);print(json.dumps(summary['counts']));print([r for r in rows if not r['passed']]);return int(not summary['passed'])

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--case',type=Path,required=True);args=p.parse_args();raise SystemExit(run(args.case))
