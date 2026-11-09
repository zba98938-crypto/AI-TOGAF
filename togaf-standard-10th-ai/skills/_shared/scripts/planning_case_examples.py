"""Six explicit synthetic business cases, with missing-input and changed variants.

These authored case decisions are not a general natural-language planner.
The raw material is packaged separately; test oracles do not call this builder.
"""
import copy
import json
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATERIAL = ROOT / 'examples/planning-six-cases/business-materials.json'
ASSIGNMENT = 'architecture-work-assignment-map'
ARTIFACTS = ('implementation-factor-catalog', 'consolidated-gaps-solutions-dependencies-matrix',
             'architecture-definition-increments-table', 'transition-architecture-state-evolution-table',
             'business-value-risk-matrix')
PROFILE_IDS = (ASSIGNMENT,) + tuple('c220-' + x for x in ARTIFACTS)
KINDS = dict(zip(PROFILE_IDS, ('assignment', 'factor', 'gap', 'increment', 'transition', 'value_risk')))
CONTEXT = dict(domains=['business', 'data', 'application', 'technology'], landscape='segment',
               purpose='project', abstraction='logical', evolution='target')


def raw_case(profile_id, variant='sufficient'):
    if profile_id not in PROFILE_IDS or variant not in ('sufficient', 'missing', 'change'):
        raise ValueError('Unknown case or variant')
    raw = json.loads(MATERIAL.read_text())
    raw['scenario'] = variant
    raw['request_change'] = raw.pop('variants').get(variant, {}).get(KINDS[profile_id], 'Use the supplied records.')
    if profile_id == ASSIGNMENT:
        raw.pop('planning')
        if variant == 'missing':
            raw['role_inputs']['assignments'][0]['available_hours'] = None
        elif variant == 'change':
            raw['role_inputs']['tasks'][0]['workload_hours'] = 48
    else:
        raw.pop('role_inputs')
        raw.pop('role_reuse_provenance')
        p = raw['planning']
        if variant == 'missing':
            if KINDS[profile_id] == 'factor': p['factor']['drain_events_per_hour'] = None
            if KINDS[profile_id] == 'gap': p['gap']['dependency_work_packages'] = None
            if KINDS[profile_id] == 'increment': p['increment']['description'] = None
            if KINDS[profile_id] == 'transition': p['transition']['service_taxonomy'] = None
            if KINDS[profile_id] == 'value_risk': p['value_risk']['criteria'][1]['weight'] = None
        elif variant == 'change':
            if KINDS[profile_id] == 'factor':
                p['factor']['backlog_events'] = 3000
                p['factor']['description'] = 'Recovery backlog increased to 3000 events; rate stays 500 events/hour; window stays 4 hours.'
            if KINDS[profile_id] == 'gap':
                p['gap']['dependency_work_packages'].append('WP-AUDIT')
                p['work_packages'].append(dict(id='WP-AUDIT', name='Security audit gate', owner='Simulated security owner',
                                               scope='Review event trace and access logs before pilot', start='2026-11-09', end='2026-11-16'))
            if KINDS[profile_id] == 'increment':
                p['additional_increment'] = dict(work_package='WP-OFFLINE', transition='TRANS-OFFLINE',
                    description='Persist offline requests; replay idempotently; central confirmation precedes fulfilment.',
                    acceptance='Replay duplicates, expired requests and stock conflicts; actual results still pending.')
            if KINDS[profile_id] == 'transition':
                p['transition'].update(name='Four-store online pilot', proposed_state='expanded-pilot',
                                       scope='Four stores, online orders only; independent capacity verification remains pending.')
            if KINDS[profile_id] == 'value_risk':
                p['value_risk']['options'][0]['scores']['V-COVERAGE'] = 3
    return raw


def entity(identity, kind, name, attrs):
    return dict(id=identity, type=kind, name=name, attributes=copy.deepcopy(attrs), evidence=['SIX-RAW'], certainty='assumed')


def view(pid, artifact, ids, edges=()):
    return dict(id='six-case-view', artifact_id=artifact, profile_id=pid, title='Synthetic candidate: ' + KINDS[pid],
                context=copy.deepcopy(CONTEXT), entity_ids=list(ids), relationship_ids=list(edges),
                analysis='Read the supplied synthetic records and explicit changes; missing inputs remain gaps.',
                legend='Candidate design; no actual implementation, competence certification or approval.')


def base_model(raw):
    return dict(schema_version='2.0', project=dict(id='six-business-case', name='Synthetic omnichannel planning',
                version=raw['scenario'], context=copy.deepcopy(CONTEXT), is_example=True,
                approval_status='candidate', implementation_status='not-started'),
                sources=[dict(id='SIX-RAW', kind='example', description='Explicit synthetic business records; no real approval',
                              locator='examples/planning-six-cases/business-materials.json')],
                entities=[], relationships=[], views=[], deliverables=[], gaps=[])


def assignment_model(raw):
    from assignment_projection import prepare
    from proficiency_contract import scale, sources
    m = base_model(raw)
    data = copy.deepcopy(raw['role_inputs'])
    m['sources'] += [s for s in sources() if s['id'] != 'SIX-RAW']
    data['source_ids'] = [s['id'] for s in m['sources']]
    m['scales'] = [scale()]
    role = data['roles'][0]
    m['entities'] = [entity(role['id'], 'guide:architecture-role', role['name'], {k:v for k,v in role.items() if k not in ('id','name','evidence')}),
        entity('APP-ORDER', 'application', 'Order pilot client', dict(version='candidate-v1', owner='Order team', lifecycle='pilot', criticality='synthetic', cost='unknown')),
        entity('APP-STOCK', 'application', 'Central stock service', dict(version='candidate-v1', owner='Inventory team', lifecycle='pilot', criticality='synthetic', cost='unknown')),
        entity('IF-RESERVE', 'interface', 'Central reservation contract', dict(protocol='HTTPS', payload='event_id, order_id, quantity; confirm only after atomic reservation', version='candidate-v1'))]
    m['relationships'] = [dict(id=i, type=t, source=a, target=b, label=label, attributes={}, evidence=['SIX-RAW'], certainty='assumed')
        for i,t,a,b,label in [('EXPOSE','exposes','APP-STOCK','IF-RESERVE','Provides atomic reservation'), ('CONSUME','consumes','APP-ORDER','IF-RESERVE','Requests reservation')]]
    v = view(ASSIGNMENT, 'application-communication-diagram', ['APP-ORDER','APP-STOCK','IF-RESERVE'], ['EXPOSE','CONSUME'])
    v.update(id='reservation-contract', profile_id='compat-application-communication-diagram', title='Pilot reservation contract')
    m['views'] = [v]
    data['tasks'][0].update(model_object_refs=[e['id'] for e in m['entities']], artifact_ids=['application-communication-diagram'])
    data['model_objects'] = copy.deepcopy(m['entities'])
    data['model_relationships'] = copy.deepcopy(m['relationships'])
    data['model_views'] = copy.deepcopy(m['views'])
    data['model_binding'] = dict(version='g249-assessment-binding/1', context_ref='G249-SIX-CONTEXT')
    m['entities'].append(entity('G249-SIX-CONTEXT','guide:g249-assessment-context','Bound role inputs',dict(assessment_inputs=copy.deepcopy(data))))
    m['extensions'] = {'entity_types': {'guide:g249-assessment-context':'Bound task and personnel evidence'}}
    m['analyses'] = [dict(id='six-role-review', method_id='architecture-role-skill-assessment', inputs=data, evidence=data['source_ids'])]
    return prepare(m, view_id='six-case-view')


def planning_model(pid, raw):
    m = base_model(raw); p = raw['planning']; aid = pid.removeprefix('c220-')
    es = []; rs = []
    def add(i,t,n,a): es.append(entity(i,t,n,a))
    if aid == 'implementation-factor-catalog':
        f = p['factor']; rate = f['drain_events_per_hour']; hours = f['backlog_events']/rate if rate else None
        action = (None if hours is None else 'Candidate pilot fits the given recovery window; actual approval pending.' if hours <= f['recovery_window_hours'] else 'Capacity increase or narrower pilot required before cutover.')
        add(f['id'],'implementation_factor','Recovery processing capacity', dict(f, calculated_recovery_hours=hours,
            deduction=None if hours is None else str(hours)+' hours recovery versus '+str(f['recovery_window_hours'])+' hours window', action_or_constraint=action))
    elif aid == 'consolidated-gaps-solutions-dependencies-matrix':
        g=p['gap'];add(g['id'],'gap','Cross-channel event identity',dict(description=g['description'],solution_refs=g['solution_work_packages'],dependency_refs=g['dependency_work_packages'],dependency_basis=g['dependency_basis']))
        for w in p['work_packages']: add(w['id'],'work_package',w['name'],w)
    elif aid == 'architecture-definition-increments-table':
        for n, inc in enumerate([p['increment']] + ([p['additional_increment']] if 'additional_increment' in p else [])):
            add(inc['work_package'],'work_package','Online event key pilot' if n==0 else 'Offline reception pilot',dict(scope=inc['description'],approval='not-granted'))
            add(inc['transition'],'transition','Online pilot' if n==0 else 'Offline reception with central confirmation',dict(description=inc['acceptance']))
            rs.append(dict(id='INCREMENT-'+str(n+1),type='implements_transition',source=inc['work_package'],target=inc['transition'],label='Candidate increment',attributes=dict(increment_description=inc['description'],acceptance=inc['acceptance']),evidence=['SIX-RAW'],certainty='assumed'))
    elif aid == 'transition-architecture-state-evolution-table':
        t=p['transition'];add(t['service_id'],'business_service',t['service_name'],dict(scope=t['scope']))
        add(t['id'],'transition',t['name'],dict(description=t['scope']))
        add(t['sbb_id'],'sbb',t['sbb_name'],dict(service_taxonomy=t['service_taxonomy'],proposed_state=t['proposed_state'],transition_ref=t['id'],service_refs=[t['service_id']],scope=t['scope']))
    elif aid == 'business-value-risk-matrix':
        v=p['value_risk']
        for option in v['options']:
            indexes={}
            for dimension in ('value','risk'):
                criteria=[c for c in v['criteria'] if c['dimension']==dimension]
                indexes[dimension+'_index'] = float(sum(Decimal(str(option['scores'][c['id']]))*Decimal(str(c['weight'])) for c in criteria)) if all(c['weight'] is not None for c in criteria) else None
            w=next(w for w in p['work_packages'] if w['id']==option['id'])
            add(w['id'],'work_package',w['name'],dict(**indexes,criterion_scores=option['scores'],evaluation_state='simulation-only',approval='not-granted',criteria_basis=dict(method='Explicit weighted sum within each dimension; synthetic rules only',source_refs=['SIX-RAW'],defined_on=v['criteria_defined_on'],options_disclosed_on=v['options_disclosed_on'],criteria=v['criteria'],authority=v['authority'])))
    m['entities']=es;m['relationships']=rs;m['views']=[view(pid,aid,[e['id'] for e in es],[r['id'] for r in rs])]
    return m


def model(pid, variant='sufficient', raw=None):
    raw=copy.deepcopy(raw if raw is not None else raw_case(pid,variant))
    return assignment_model(raw) if pid==ASSIGNMENT else planning_model(pid,raw)


def example(pid):
    m=model(pid);main=next(v for v in m['views'] if v['profile_id']==pid)
    fragment={k:copy.deepcopy(v) for k,v in m.items() if k not in ('schema_version','project','views','deliverables','gaps')}
    fragment.update(view=main, supporting_views=[v for v in m['views'] if v['id']!=main['id']],
                    raw_input='examples/planning-six-cases/business-materials.json', notice='Synthetic sufficient input; actual approval remains not-granted.')
    return fragment


def install(caps):
    for profile in caps['profiles']:
        if profile['id'] in PROFILE_IDS:
            profile['example']=example(profile['id'])
        if profile['id'] == ASSIGNMENT:
            # Optional legacy input spellings remain model-local extensions.
            # Their meanings are explicit here rather than promoted to core.
            profile.setdefault('extensions', {}).setdefault('entity_types', {}).update({
                'case:architecture-task': '本案例需完成的架构工作，区别于职位和人员分配',
                'case:person-assignment': '本案例有期间与容量条件的候选人员分配',
                'case:competence-evidence': '本案例人员观察及其证据状态，不表示认证',
            })
    return caps
