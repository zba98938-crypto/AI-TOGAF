"""Add the missing project ABB/SBB mapping contract without broadening core edges.

G248 §3 distinguishes logical ABB specification and related operational SBB.
The stored SBB -> realizes -> ABB direction is this package's existing metamodel
convention, not a claim that prose prescribes arrow storage or figure fidelity.
Legacy views remain valid: realizes and SBB are optional, not new requirements.
"""
from copy import deepcopy

FAMILY='building-block-description'
# Content-metamodel (G248 fig3-1) is a type-level topology, not the ABB/SBB mapping family.
PROFILE_IDS={'building-block-description-default'}
NOTE=('G248 §3正文支持ABB逻辑规格与相关SBB实现的区分；SBB→realizes→ABB沿用本包既有元模型方向。'
      '允许候选或部分实现映射，须记录coverage/gap及依据；箭头不证明已部署、全覆盖或批准。'
      '本变更不证明图3-1来源结构或完整基础标准定义，source_verified保持false。')

def apply_contract(products,profiles,relations=None):
    """Idempotently add optional SBB/requirement and realizes, keeping old data."""
    touched=[]
    for item in [*products,*profiles]:
        is_family=item.get('id')==FAMILY
        if not is_family and item.get('id') not in PROFILE_IDS:continue
        if not is_family and item.get('artifact_id')!=FAMILY:raise ValueError('profile family mismatch')
        for key,add in [('entity_types',['abb','sbb','requirement']),('relationship_types',['realizes'])]:
            item[key]=list(dict.fromkeys([*item.get(key,[]),*add]))
        item['building_block_mapping_contract']={'version':'1.0','source_refs':['G248 §3正文、§3.1及§3.6'],
            'realization_direction':'sbb -> realizes -> abb','status':'optional-project-operational-convention',
            'notice':NOTE,'does_not_require_new_edges':True}
        if is_family and relations and 'realizes' in relations:
            item.setdefault('relationship_definitions',{})['realizes']=deepcopy(relations['realizes'])
        touched.append(item['id'])
    return touched
