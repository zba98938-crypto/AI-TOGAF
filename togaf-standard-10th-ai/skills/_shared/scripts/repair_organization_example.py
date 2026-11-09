"""Repair the registered organization exchange example without inferring facts.

Only the named profile is patched. All evidence remains explicitly fictional.
"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def repair(profile):
    p=profile; ex=p['example']; prefix='organization-work-network-'
    def entity(suffix,typ,name,definition):
        return {'id':prefix+suffix,'type':typ,'name':name,'attributes':{'definition':definition},'evidence':['case-source'],'certainty':'assumed'}
    def relationship(suffix,typ,source,target,label):
        return {'id':prefix+suffix,'type':typ,'source':prefix+source,'target':prefix+target,'label':label,'evidence':['case-source'],'certainty':'assumed'}
    new_entities=[entity('order-capability','capability','订单处理能力','运营负责确认订单与交接'),entity('delivery-capability','capability','履约协调能力','合作方负责协调委托履约'),entity('order-information','information','订单信息','用于订单确认与委托履约的信息概念；不是物理表')]
    new_relationships=[relationship('order-owned','owned_by','order-capability','ops','订单处理能力由在线运营负责'),relationship('order-used','uses_information','order-capability','order-information','订单处理使用订单信息'),relationship('delivery-owned','owned_by','delivery-capability','carrier','履约协调能力由承运合作方负责'),relationship('delivery-used','uses_information','delivery-capability','order-information','履约协调使用订单信息')]
    ids={e['id'] for e in new_entities};rids={r['id'] for r in new_relationships}
    ex['entities']=[e for e in ex['entities'] if e['id'] not in ids]+new_entities
    ex['relationships']=[r for r in ex['relationships'] if r['id'] not in rids]+new_relationships
    exchange=next(r for r in ex['relationships'] if r['id']==prefix+'info')
    exchange['label']='确认订单后运营向承运合作方交接订单信息（虚构访谈声明）'
    exchange['attributes'].update({'information_ref_id':prefix+'order-information','derivation_relationship_ids':[r['id'] for r in new_relationships],'derivation_path':'在线运营←订单处理能力→订单信息←履约协调能力→承运合作方；路径只证明关联，交换方向另由访谈声明'})
    ex['sources'][0]['description']='虚构访谈：运营负责订单处理、承运方负责履约协调，二者使用订单信息；运营在确认后将订单信息交接承运方。结构链不证明实际发生或批准。'
    ex['view']['analysis']='先区分组织、能力和独立信息概念，按owned_by及uses_information追溯两端关联；定向信息交换仅依据另行声明的虚构访谈，不能由共用信息自动推断。'
    ex['view']['entity_ids']=list(dict.fromkeys(ex['view']['entity_ids']+[e['id'] for e in new_entities]))
    ex['view']['relationship_ids']=list(dict.fromkeys(ex['view']['relationship_ids']+[r['id'] for r in new_relationships]))
    p['entity_types']=list(dict.fromkeys(p['entity_types']+['capability','information']))
    p['relationship_types']=list(dict.fromkeys(p['relationship_types']+['owned_by','uses_information']))
    p['required_attributes'].update({'capability':['definition'],'information':['definition']})
    p['source_refs']=list(dict.fromkeys(p['source_refs']+['G206 §5 表5-1','G190 §4']))
    check='information_ref_id与derivation_relationship_ids为项目结构化追溯约定；旧自由文本仅人工声明并提示unverified-derivation。两端组织通过能力关联同一信息不证明定向交换已发生。'
    p['checks']=list(dict.fromkeys(p['checks']+[check]));p['version']='2.3'
    return p

def main():
    path=ROOT/'capabilities.json';cap=json.loads(path.read_text())
    profile=next(p for p in cap['profiles'] if p['id']=='organization-work-network')
    repair(profile)
    path.write_text(json.dumps(cap,ensure_ascii=False,indent=2)+'\n')
    print('Patched organization-work-network 2.3; source/visual acceptance unchanged')
if __name__=='__main__':main()
