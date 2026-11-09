"""Check a declared strategic/MVA/backlog trace; no default prioritization scores."""
from evidence_analysis import unique,require,evidence,sources

REFINES='g20f:refines'
CONSTRAINS='g20f:constrains-story'
ALLOCATES='g20f:allocated-to-sbb'
MEMBER='g20f:included-in-mva'
DEPENDS='g20f:story-depends-on'

def review_backlog_trace(data):
    code='BACKLOG-TRACE';known=sources(data,code,'input')
    nodes=unique(data.get('nodes',[]),code,'nodes');edges=unique(data.get('relationships',[]),code,'relationships')
    policy=data.get('hierarchy_policy',{})
    levels=policy.get('levels',[])
    require(levels==['strategic_intent','epic','feature','story'],code,'hierarchy-policy','Declare this project hierarchy explicitly; it is not a TOGAF mandatory chain')
    evidence(policy.get('evidence'),known,code,'hierarchy-policy')
    for n in nodes.values():
        evidence(n.get('evidence'),known,code,n['id'])
        require(n.get('name') and n.get('owner'),code,n['id'],'Meaning and responsible owner required')
        require(n.get('kind') in levels+['abb','sbb','mva'],code,n['id'],'Unknown semantic kind')
        if n['kind'] in levels:
            require(n.get('landscape') in ['strategic','segment','capability'] and n.get('evolution') in ['baseline','transition','target'],code,n['id'],'Landscape level and evolution are independent fields')
        if n['kind']=='story':
            require(n.get('priority') in ['must-have','should-have','could-have','deferred'] and n.get('acceptance_criteria'),code,n['id'],'Explicit project priority and acceptance criteria required')
            evidence(n.get('priority_evidence'),known,code,n['id'])
            obs=n.get('acceptance',{})
            require(obs.get('status') in ['not-observed','failed','verified'],code,n['id'],'Acceptance state is not inferred from selection')
            if obs['status']!='not-observed':evidence(obs.get('evidence'),known,code,n['id'])
    parents={};dependencies={};constraints={};allocations={};realizations={};members={}
    allowed={REFINES,CONSTRAINS,ALLOCATES,MEMBER,DEPENDS,'realizes'}
    for edge in edges.values():
        i=edge['id'];s=edge.get('source');t=edge.get('target');typ=edge.get('type')
        require(s in nodes and t in nodes and s!=t,code,i,'Unknown or identical endpoints')
        evidence(edge.get('evidence'),known,code,i)
        require(typ in allowed,code,i,'Unsupported relationship meaning')
        a,b=nodes[s],nodes[t]
        if typ==REFINES:
            require(a['kind'] in levels and b['kind'] in levels and levels.index(b['kind'])==levels.index(a['kind'])+1,code,i,'Refinement direction must follow the declared semantic hierarchy')
            parents.setdefault(t,[]).append(s)
        elif typ==CONSTRAINS:
            require((a['kind'],b['kind'])==('abb','story'),code,i,'ABB constrains story');constraints.setdefault(t,[]).append(s)
        elif typ==ALLOCATES:
            require((a['kind'],b['kind'])==('story','sbb'),code,i,'Story allocation points to SBB');allocations.setdefault(s,[]).append(t)
        elif typ=='realizes':
            require((a['kind'],b['kind'])==('sbb','abb'),code,i,'Realization points from SBB to ABB');realizations.setdefault(s,[]).append(t)
        elif typ==MEMBER:
            require((a['kind'],b['kind'])==('story','mva'),code,i,'MVA membership points from story to named scope');members.setdefault(t,[]).append(s)
        elif typ==DEPENDS:
            require(a['kind']==b['kind']=='story',code,i,'Dependency points from dependent story to prerequisite story');dependencies.setdefault(s,[]).append(t)
    def paths_to_goal(i,trail=()):
        require(i not in trail,code,i,'Refinement cycle')
        if nodes[i]['kind']=='strategic_intent':return [[i]]
        require(bool(parents.get(i)),code,i,'Backlog item has no trace to strategic intent')
        return [path+[i] for parent in parents[i] for path in paths_to_goal(parent,trail+(i,))]
    def dependency_closure(i,trail=()):
        require(i not in trail,code,i,'Story dependency cycle')
        found=set()
        for parent in dependencies.get(i,[]):found.add(parent);found.update(dependency_closure(parent,trail+(i,)))
        return found
    stories=[n for n in nodes.values() if n['kind']=='story'];traces=[]
    require(bool(stories),code,'stories','No stories in the selected scope')
    for n in stories:
        i=n['id'];paths=paths_to_goal(i);deps=dependency_closure(i)
        require(constraints.get(i) and allocations.get(i),code,i,'Story lacks ABB guardrails or planned SBB allocation')
        for abb in constraints[i]:
            require(any(abb in realizations.get(sbb,[]) for sbb in allocations[i]),code,i,'Allocated SBB does not realize the constraining ABB')
        traces.append({'story_id':i,'strategic_paths':paths,'abb_ids':constraints[i],'sbb_ids':allocations[i],'prerequisite_ids':sorted(deps)})
    mva_results=[]
    for mva in [n for n in nodes.values() if n['kind']=='mva']:
        i=mva['id'];candidates=mva.get('candidate_story_ids',[]);chosen=members.get(i,[])
        require(candidates and len(candidates)==len(set(candidates)) and all(x in nodes and nodes[x]['kind']=='story' for x in candidates),code,i,'Declare a non-empty comparison scope of story IDs')
        require(len(chosen)==len(set(chosen)) and set(chosen)<=set(candidates),code,i,'Duplicate or out-of-scope MVA membership')
        required={x for x in candidates if nodes[x]['priority']=='must-have'}
        require(set(chosen)==required,code,i,'Selected MVA stories must match explicit must-have prioritization for this declared scope')
        require(mva.get('boundary') and mva.get('exclusions') and mva.get('decision_owner'),code,i,'MVA scope, exclusions and decision owner required')
        evidence(mva.get('decision_evidence'),known,code,i)
        gaps=[]
        for story in chosen:
            for dep in dependency_closure(story):
                if dep not in chosen and nodes[dep].get('acceptance',{}).get('status')!='verified':gaps.append({'story_id':story,'prerequisite_id':dep,'code':'prerequisite-outside-mva-unverified'})
            if nodes[story]['acceptance']['status']!='verified':gaps.append({'story_id':story,'code':'acceptance-not-verified'})
        mva_results.append({'mva_id':i,'selected_story_ids':chosen,'readiness':'evidence-complete-awaiting-business-review' if not gaps else 'pending-evidence','gaps':gaps})
    require(bool(mva_results),code,'mva','Named MVA boundary required')
    return {'traces':traces,'mva_assessments':mva_results,'notice':'Only the declared project hierarchy and evidence are checked. MVA selection, realization links, approval and operational deployment are separate.'}
