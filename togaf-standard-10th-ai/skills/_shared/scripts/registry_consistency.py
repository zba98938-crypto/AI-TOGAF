"""Maintain cross-registry contracts and detect drift without granting acceptance."""
import argparse, copy, hashlib, json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
GUIDE = re.compile(r'\bG[0-9]{2}[0-9A-Z]\b')
BASE_BINDINGS = {
 'information-map': ('G190', 'information-concept-network', ['G190/fig2-1', 'G190 §3–5']),
 'organization-map': ('G206', 'organization-work-network', ['G206/fig3-2', 'G206 §5 表5-1']),
 'business-capability-map': ('G211', 'capability-decomposition', ['G211/fig3-3', 'G211 §3–5']),
}
DELIVERY_LINKS = {
 'security-policy-architecture': ['architecture-principles'],
 'environmental-decision-log': ['business-principles'],
 'balanced-scorecard': ['business-goals-objectives'],
 'business-scenario-document': ['business-drivers', 'request-for-architecture-work'],
 'building-block-description': ['architecture-building-blocks'],
 'security-impact-analysis': ['requirements-impact-assessment'],
 'architecture-repository-structure': ['architecture-repository'],
 'architecture-landscape-projection': ['architecture-definition-document'],
 'soa-layered-reference': ['architecture-definition-document', 'architecture-building-blocks'],
 'repository-state-view-tree': ['architecture-repository'],
 'repository-parallel-candidates': ['architecture-repository'],
 'capability-project-continuum': ['architecture-vision'],
 'portfolio-stakeholder-concern-matrix': ['communications-plan'],
 'repository-target-baseline-comparison': ['requirements-impact-assessment', 'architecture-repository'],
 'architecture-governance-checklist': ['implementation-governance-model'],
 'decision-delegation-register': ['implementation-governance-model'],
}
GOVERNANCE_LINK_CONTEXT = '项目路由：F阶段在适用时（if any）准备实施治理模型；G阶段使用其检查点、决策权和升级规则进行实施治理。关联工作产品不自动创建必需交付物、不代替适用性裁剪或真实授权。'


def apply_delivery_links(cap):
 """Add explicit project routes without changing ADM output obligations."""
 for w in cap['work_products']:
  for did in DELIVERY_LINKS.get(w['id'],[]):
   if did not in w.setdefault('related_deliverables',[]):w['related_deliverables'].append(did)
  if w['id'] in {'architecture-governance-checklist','decision-delegation-register'}:
   w.setdefault('related_deliverable_context',{})['implementation-governance-model']=GOVERNANCE_LINK_CONTEXT
 return cap

def read(path): return json.loads(path.read_text())
def write(path, value): path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def package_sources(directory):
 return sorted({g for p in directory.rglob('*.md') for g in GUIDE.findall(p.read_text())})
def canonical_candidate(identity, known):
 candidate = identity.removeprefix('new:')
 return candidate if candidate in known else identity

def canonicalize_resolutions(records, known):
 result = {}
 for raw in records:
  row = copy.deepcopy(raw); old = row.get('candidate_id', row.get('id'))
  if not old: raise ValueError('candidate resolution has no ID')
  identity = canonical_candidate(old, known)
  row['candidate_id'] = identity
  aliases = set(row.get('legacy_candidate_ids', []))
  if identity != old: aliases.add(old)
  previous = result.get(identity)
  if previous:
   if {k:v for k,v in previous.items() if k!='legacy_candidate_ids'} != {k:v for k,v in row.items() if k!='legacy_candidate_ids'}:
    raise ValueError('Conflicting candidate resolutions: '+identity)
   aliases.update(previous.get('legacy_candidate_ids', []))
  if aliases: row['legacy_candidate_ids'] = sorted(aliases)
  result[identity] = row
 return list(result.values())

def work_product_bindings(cap, arts):
 """First-class contracts for existing base IDs; no duplicate artifact/profile IDs."""
 ps = {p['id']:p for p in cap['profiles']}; byid={a['id']:a for a in arts}; rows=[]
 for aid,(guide,pid,refs) in BASE_BINDINGS.items():
  a=byid[aid];p=ps[pid]
  if p['artifact_id']!=aid: raise ValueError('Base work-product profile mismatch: '+aid)
  fields=copy.deepcopy(p['required_attributes'])
  rows.append({'id':aid,'registration_class':'base-artifact-work-product-binding',
   'guide':guide,'source_refs':refs,'owner':a['owner'],'profile_id':pid,
   'decision':a['question'],'required_inputs':['带来源的业务范围、对象定义及类型化关系'],
   'analysis_steps':a['analysis'],'required_attributes':fields,
   'example':copy.deepcopy(p['example']),
   'counterexample':{'input':'删除已选对象的必需业务属性','expected':'missing-profile-attribute',
                    'why':'缺定义、范围或责任时不得声称完整工作产品。'},
   'modification_example':{'change':'修改同ID对象的definition，并核对两种布局中的正文与覆盖位置',
                           'expected':'新定义出现在保存输出；旧定义不作为当前事实。'},
   'evidence_policy':'执行verify_artifact_profiles.py逐profile的原始、修改及反例；来源等价和业务批准分别评审。'})
 return rows

def sync():
 cap=read(ROOT/'capabilities.json');arts=read(ROOT/'artifacts.json')['artifacts']
 apply_delivery_links(cap)
 for w in cap['work_products']:
  if not w.get('counterexample'):
   w['counterexample']={'input':'从所选对象删除必需的definition属性，保留其稳定ID及视图选择。',
    'expected':'missing-profile-attribute','why':'缺少对象含义，无法支持'+w['decision']}
  if not w.get('modification_example'):
   w['modification_example']={'change':'修改同ID对象的definition，保持结构角色、类别和边界属性不变。',
    'expected':'reference与adaptive保存输出均表达新定义；覆盖位置指向该对象；不沿用旧版定义。'}
 # Persist the specialized vocabulary already carried by profile examples.
 for p in cap['profiles']:
  for name,definition in p.get('example',{}).get('extensions',{}).get('relationship_types',{}).items():
   cap.setdefault('extension_relationship_definitions',{}).setdefault(name,copy.deepcopy(definition))
 meanings={'g186:comparison_item':'两个存储库快照之间的同ID比较项；变化从属性与子项推导。',
 'g186:concern':'组合目的的利益相关者关注点，不是流程或RACI码。',
 'g186:continuum':'来源无单位0至10能力与项目连续谱，不表示日期或成熟度。',
 'g186:continuum_label':'连续谱上的阅读顺序标签，不表示精确数值分段。',
 'g186:repository_node':'存储库中具有明确父项和展开状态的节点。',
 'g186:repository_snapshot':'用于有方向版本比较的源或目标架构快照。',
 'g186:stakeholder':'在指定组合范围承担关注职责的利益相关者。',
 'guide:architecture_domain':'来源说明的业务、数据、应用或技术架构域，非企业实例。',
 'guide:metamodel_entity':'来源元模型实体类型的解释对象，非企业实例。'}
 for name,meaning in meanings.items():cap.setdefault('extension_entity_definitions',{}).setdefault(name,meaning)
 cap['base_work_product_bindings']=work_product_bindings(cap,arts)
 known={x['id'] for k in ['work_products','profiles','analysis_methods'] for x in cap[k]}|{a['id'] for a in arts}
 cap['candidate_resolutions']=canonicalize_resolutions(cap.get('candidate_resolutions',[]),known)
 write(ROOT/'capabilities.json',cap)
 index=read(ROOT/'skill-index.json')
 for skill in index: skill['sources']=package_sources(ROOT.parent/skill['name'])
 write(ROOT/'skill-index.json',index)
 return cap

def check(cap=None, include_review_evidence=False):
 cap=cap or read(ROOT/'capabilities.json');errors=[];ps={p['id']:p for p in cap['profiles']}
 for name in (['source-verification','profile-visual-review'] if include_review_evidence else []):
  if not (ROOT/('reviews/'+name+'-index.json')).is_file():
   errors.append(name+': review evidence is not included in this core package');continue
  idx=read(ROOT/('reviews/'+name+'-index.json'))
  if idx.get('total')!=len(ps) or {r['profile_id'] for r in idx['records']}!=set(ps):errors.append(name+': profile inventory drift')
  if idx.get('registry_sha256')!=sha(ROOT/'capabilities.json'):errors.append(name+': registry fingerprint drift')
  if name=='profile-visual-review' and idx.get('output_current')!={'reference':True,'adaptive':True}:errors.append(name+': generated outputs stale or absent')
 for skill in read(ROOT/'skill-index.json'):
  if skill['sources']!=package_sources(ROOT.parent/skill['name']):errors.append(skill['name']+': sources drift')
 for w in cap['work_products']:
  for field in ['counterexample','modification_example']:
   if not w.get(field):errors.append(w['id']+': missing '+field)
  for did in DELIVERY_LINKS.get(w['id'],[]):
   if did not in w.get('related_deliverables',[]):errors.append(w['id']+': missing delivery route '+did)
 ds={d['id'] for d in read(ROOT/'deliverables.json')['deliverables']}
 linked={d for w in cap['work_products'] for d in w.get('related_deliverables',[])}
 if ds-linked:errors.append('Unlinked deliverables: '+','.join(sorted(ds-linked)))
 for b in cap.get('base_work_product_bindings',[]):
  if b['profile_id'] not in ps or ps[b['profile_id']]['artifact_id']!=b['id']:errors.append('Invalid base WP binding: '+b['id'])
 if {b['guide'] for b in cap.get('base_work_product_bindings',[])}!={'G190','G206','G211'}:errors.append('Missing base WP guide contract')
 return errors

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--sync',action='store_true');ap.add_argument('--with-review-evidence',action='store_true',help='Also require separately supplied historical review indices and generated outputs');args=ap.parse_args()
 if args.sync:sync()
 else:
  errors=check(include_review_evidence=args.with_review_evidence);print(json.dumps({'errors':errors,'review_evidence_required':args.with_review_evidence},ensure_ascii=False));raise SystemExit(bool(errors))
