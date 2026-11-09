"""Executable design simulations, explicitly distinct from product/field tests."""
import copy

def cold_chain(events, tolerance=60):
    seen=set();current={};receipts=[]
    for raw in events:
        e=copy.deepcopy(raw);key=(e['appointment'],e['version'],e['event'])
        status='accepted'
        if key in seen:status='duplicate'
        elif not e['authorized']:status='unauthorized'
        elif not 2<=e['temperature']<=8:status='temperature-rejected'
        elif abs(e['received']-e['sampled'])>tolerance:status='clock-rejected'
        elif e['version']<current.get(e['appointment'],0):status='stale-version'
        if status=='accepted':
            seen.add(key);current[e['appointment']]=e['version']
        receipts.append({'input':e,'status':status,'current_version':current.get(e['appointment'])})
    return {'current':current,'receipts':receipts,'notice':'Software design simulation; no sensor, network or production acceptance.'}

def batch_quality(events):
    seen=set();batches={};receipts=[]
    for e in events:
        key=(e['batch'],e['sample'],e['method_version'],e['event_version'])
        state=batches.setdefault(e['batch'],{'version':0,'state':'pending','release_count':0})
        if key in seen:status='duplicate'
        elif e['event_version']<state['version']:status='stale-version'
        else:
            seen.add(key);state['version']=e['event_version'];status='recorded'
            if e['kind']=='revoke':state['state']='frozen'
            elif state['state']=='frozen':status='manual-review-required'
            elif e['kind']=='result':state['state']='awaiting-human-signature'
            elif e['kind']=='human-release' and e.get('authorized') and state['state']=='awaiting-human-signature':
                state['state']='released';state['release_count']+=1
            else:status='rejected'
        receipts.append({'input':copy.deepcopy(e),'status':status,'state':copy.deepcopy(state)})
    return {'batches':batches,'receipts':receipts,'notice':'Software design simulation; no LIMS/MES, isolation or real business signature.'}

def run():
    cold=[];quality=[]
    for i in range(20):
        e={'appointment':'A'+str(i),'version':1,'event':'first','temperature':2 if i%2 else 8,'sampled':100,'received':100,'authorized':True}
        cold += [e,copy.deepcopy(e),dict(e,version=2,event='update',sampled=200,received=200),dict(e,event='late')]
        cold += [dict(e,event='too-cold',temperature=1.9),dict(e,event='too-warm',temperature=8.1),dict(e,event='clock',received=161),dict(e,event='access',authorized=False)]
        q={'batch':'B'+str(i),'sample':'S'+str(i),'method_version':1,'event_version':1,'kind':'result'}
        quality += [q,copy.deepcopy(q),dict(q,event_version=2,kind='human-release',authorized=True),dict(q,event_version=3,kind='revoke'),dict(q,event_version=4,kind='result'),dict(q,kind='result')]
    return {'lingang':cold_chain(cold),'qianlin':batch_quality(quality),
            'lingang_modified_tolerance':cold_chain([dict(cold[0],event='clock-change',sampled=100,received=131)],30)}
