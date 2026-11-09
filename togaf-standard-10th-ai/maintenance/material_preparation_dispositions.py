"""Pinned source dispositions and historical candidate bindings, never review.

The adapter changes preparation metadata only. Source identities, text, raw
fragments, locations and image references are immutable across its application.
"""
import copy
from html.parser import HTMLParser
import hashlib
import json
from pathlib import Path
import re

DEFAULT_MANIFEST = 'togaf-standard-10th-ai/maintenance/material-source-adapters/r7-preparation-dispositions.json'
MODULE_PATH = 'togaf-standard-10th-ai/maintenance/material_preparation_dispositions.py'
GROUPS = {'web-image', 'web-caption-context', 'footnote-context', 'empty-navigation',
          'empty-pdf-content', 'embedded-source-image', 'empty-raw-table-cell',
          'guide-figure-no-title', 'g226-whitespace', 'w242c-source-figures', 'w242c-publication-pages'}
PENDING = 'historical-project-candidate-pending-independent-review'


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False)


def textsha(value):return hashlib.sha256(value.encode('utf-8')).hexdigest()


def raw_binding(unit):
    """Raw acquisition identity; derived page raster selection is independent."""
    keys=('id','document_id','family','kind','text_en','text_zh','source','source_document','source_locator','source_fragments')
    return {key:copy.deepcopy(unit[key]) for key in keys if key in unit}


def immutable_binding(unit):
    return {key:copy.deepcopy(value) for key,value in unit.items()
            if key in ('id','document_id','family','kind','text_en','text_zh') or key.startswith('source_') or key=='source'}


def pointer(value, path):
    if not isinstance(path,str) or not path.startswith('/'):
        raise ValueError('noncanonical preparation JSON pointer')
    for raw in path[1:].split('/'):
        if any(raw[i]=='~' and (i+1==len(raw) or raw[i+1] not in '01') for i in range(len(raw))):
            raise ValueError('invalid preparation JSON pointer escape')
        token=raw.replace('~1','/').replace('~0','~')
        if isinstance(value,list):
            if not token.isdigit() or (token!='0' and token.startswith('0')):
                raise ValueError('noncanonical preparation array pointer')
            value=value[int(token)]
        else:value=value[token]
    return value


def group_for(unit):
    kind=unit['kind']
    if kind=='web-block':return 'web-image' if unit.get('source_material_form')=='image' else 'web-caption-context'
    try:
        return {'navigation-entry':'empty-navigation','pdf-content':'empty-pdf-content',
            'pdf-unmapped-raw-block':'empty-raw-table-cell','pdf-source-block':'g226-whitespace',
            'embedded_images':'embedded-source-image','figures':'guide-figure-no-title',
            'footnote':'footnote-context','pdf-page':'w242c-publication-pages','source-figure':'w242c-source-figures'}[kind]
    except KeyError as exc:raise ValueError('unsupported preparation disposition kind') from exc


def historical_fields(value,path='',keep=False):
    if isinstance(value,dict):
        for key,item in value.items():
            escaped=key.replace('~','~0').replace('/','~1')
            yield from historical_fields(item,path+'/'+escaped,keep or key.endswith('_zh'))
    elif isinstance(value,list):
        for i,item in enumerate(value):yield from historical_fields(item,path+'/'+str(i),keep)
    elif isinstance(value,str) and keep and value.strip():yield path,value


class SourceReader:
    def __init__(self,builder):self.builder=builder;self.cache={}
    def get(self,reference):
        if not isinstance(reference,dict) or set(reference)!={'path','sha256'}:
            raise ValueError('preparation source reference schema differs')
        ref=self.builder.reference(self.builder.root/reference['path'],reference['sha256'])
        if ref['path'] not in self.cache:self.cache[ref['path']]=self.builder.read(self.builder.root/ref['path'])
        return self.cache[ref['path']]
    def local(self,name):
        ref=self.builder.reference(self.builder.root/name)
        return self.get(ref),ref
    def item(self,unit):
        doc=self.get(unit['source_document']);locator=unit['source_locator']
        raw=pointer(doc,locator['json_pointer']);kind=unit['kind'];code=unit['document_id']
        if not isinstance(raw,dict):raise ValueError('preparation source locator is not an acquired record')
        if kind in ('pdf-content','pdf-unmapped-raw-block','pdf-page'):original=raw.get('text',raw.get('raw_text',''))
        elif kind in ('figures','embedded_images'):original=raw.get('title_en','')
        elif kind=='source-figure':original=raw.get('caption_en','')
        else:original=raw.get('text_en','')
        if original is None:original=''
        if unit.get('text_en',unit.get('text_zh',''))!=original:
            raise ValueError('preparation actual source text/locator differs')
        parts=locator['json_pointer'].split('/');identity=None
        if kind in ('web-block','pdf-unmapped-raw-block','pdf-source-block'):identity=raw.get('id')
        elif kind in ('figures','embedded_images'):identity='source-image:'+raw['id']
        elif kind=='source-figure':identity=raw.get('figure_id') or raw['id']
        elif kind=='footnote':identity=code+':footnote:'+raw['id']
        elif kind=='navigation-entry':identity=code+':navigation:'+f'{int(parts[-1]):05}'
        elif kind=='pdf-content':identity=f'{code}:p{doc["pages"][int(parts[2])]["pdf_page"]:04}:c{int(parts[-1]):03}'
        elif kind=='pdf-page':identity=f'{code}:p{raw["pdf_page"]:04}'+(':empty-source-page' if unit['family']=='series-guide' else '')
        if identity is None or identity!=unit['id']:raise ValueError('preparation actual source unit ID/locator differs')
        for field in ('bbox','source_dom_order','source_block_ids'):
            if field in locator and locator[field]!=raw.get(field):raise ValueError('preparation original source locator lineage differs')
        return raw


def candidate_sources(unit,reader):
    """Only existing fields related by exact original image/figure records."""
    raw=reader.item(unit);located=[]
    if unit['kind']=='figures' and raw.get('json_path'):
        located.append(('togaf-standard-10th-ai/'+raw['json_path'],None))
    elif unit['kind']=='embedded_images':
        if raw.get('json_path'):located.append(('togaf-standard-10th-ai/'+raw['json_path'],None))
        index,_=reader.local('togaf-standard-10th-ai/figures/index.json')
        figures={row['id']:row for row in index['figures']}
        for identity in raw.get('figure_ids',[]):
            if identity not in figures:raise ValueError('preparation image links an absent original figure')
            located.append(('togaf-standard-10th-ai/'+figures[identity]['json_path'],None))
    elif unit['kind']=='source-figure':located.append((unit['source_document']['path'],unit['source_locator']['json_pointer']))
    result={}
    def add(reference,path,text):
        context_id=reference['path']+'#'+path
        value={'reference':reference,'json_pointer':path,'text_sha256':textsha(text)}
        if context_id in result and result[context_id]!=value:raise ValueError('historical candidate context collision')
        result[context_id]=value
    for name,prefix in located:
        value,reference=reader.local(name)
        if prefix:
            rows=historical_fields(pointer(value,prefix),prefix)
        else:
            rows=[]
            for field in ('figure','elements','semantics','description_zh','semantic_review_zh','labels_connections_zh','limits_zh'):
                if field in value:rows.extend(historical_fields(value[field],'/'+field,field.endswith('_zh')))
        for path,text in rows:add(reference,path,text)
    if unit['kind']=='embedded_images' and isinstance(raw.get('description_zh'),str) and raw['description_zh'].strip():
        add(unit['source_document'],unit['source_locator']['json_pointer']+'/description_zh',raw['description_zh'])
    return result


class LinkReader(HTMLParser):
    def __init__(self):super().__init__(convert_charrefs=True);self.hrefs=[]
    def handle_starttag(self,tag,attrs):
        if tag=='a':self.hrefs.append(dict(attrs).get('href'))


def disposition(unit,reader):
    group=group_for(unit);raw=reader.item(unit);basis=copy.deepcopy(unit['classification_basis'])
    titles=list(basis['section_titles']);category=unit['classification'];supported=True;role=group
    if group=='web-image':
        supported=bool(raw.get('section_path')) and bool(unit.get('source_images'))
        titles=[p['title_en'] for p in raw.get('section_path',[])]
    elif group=='web-caption-context':
        doc=reader.get(unit['source_document']);index=int(unit['source_locator']['json_pointer'].rsplit('/',1)[1])
        previous=doc['blocks'][index-1] if index else {}
        supported=(raw.get('parent_tag')=='div' and 'title' in (raw.get('parent_class') or [])
            and raw.get('text_en','').startswith('Figure ') and previous.get('kind')=='img'
            and bool(previous.get('section_path')) and previous.get('source_dom_order',-1)<raw.get('source_dom_order',-1))
        titles=[p['title_en'] for p in previous.get('section_path',[])] if supported else []
        role='body-figure-caption'
    elif group=='footnote-context':
        doc=reader.get(unit['source_document']);anchor=unit['source_locator']['anchor'].replace('_footnotedef_','_footnoteref_')
        calls=[b for b in doc['blocks'] if anchor in b.get('html','')]
        paths={canonical(b.get('section_path',[])) for b in calls}
        supported=len(calls)>0 and len(paths)==1 and bool(calls[0].get('section_path'))
        titles=[p['title_en'] for p in calls[0].get('section_path',[])] if supported else []
        role='body-footnote-with-retained-reference';category='body'
    elif group=='empty-navigation':
        source=unit['source'];reader.builder.reference(reader.builder.root/source['path'],source['sha256'])
        html=(reader.builder.root/source['path']).read_text();links=LinkReader();links.feed(html)
        supported=not raw.get('text_en','').strip() and raw.get('href') in links.hrefs
        category='navigation';role='publication-site-navigation-component'
    elif group=='empty-pdf-content':
        doc=reader.get(unit['source_document']);page=doc['pages'][unit['source_locator']['pdf_page']-1]
        ids=set(unit['source_locator']['source_block_ids']);blocks=[b for b in page['blocks'] if b['id'] in ids]
        supported=len(blocks)==len(ids) and not unit.get('text_en','').strip() and all(not b.get('text','').strip() for b in blocks)
        role='source-extraction-whitespace-fragment'
    elif group in ('empty-raw-table-cell','g226-whitespace'):
        supported=not unit.get('text_en','').strip()
        if group=='empty-raw-table-cell':supported=supported and unit['source_material_form']=='table-cell'
        role='blank-table-cell' if group=='empty-raw-table-cell' else 'source-extraction-layout-fragment'
    elif group=='embedded-source-image':
        supported=bool(unit.get('source_images')) and (bool(titles) or basis['rule']=='before-first-substantive-heading')
        role='historical-image-role:'+raw.get('image_kind','linked-source-figure-occurrence')
    elif group=='guide-figure-no-title':
        supported=raw.get('title_en') is None and bool(titles) and bool(unit.get('source_images'))
        role='source-figure-with-no-provided-English-title'
    elif group=='w242c-source-figures':
        supported=unit['document_id']=='W242C' and bool(unit.get('source_images')) and bool(unit['source_locator'].get('pdf_pages'))
        role='original-Chinese-body-figure';category='body'
    elif group=='w242c-publication-pages':
        page=unit['source_locator']['pdf_page'];text=unit.get('text_zh','')
        if page==1:supported=not text.strip() and bool(unit.get('source_images'));titles=['封面'];role='publication-cover'
        elif page==37:supported='关于作者' in text;titles=['关于作者'];role='publication-authors'
        elif page==38:
            doc=reader.get(unit['source_document']);supported='关于作者' in doc['pages'][36]['text'] and 'Chris Searle' in text and 'Graham Neal' in text
            titles=['关于作者（续页）'];role='publication-authors-continuation'
        elif page==39:supported='致谢' in text;titles=['致谢'];role='publication-acknowledgements'
        elif page==40:supported='关于The Open Group' in text;titles=['关于The Open Group'];role='publication-publisher-information'
        else:supported=False
        category='front-matter'
    return {'group':group,'supported':supported,'classification':category if supported else unit['classification'],
        'section_titles':titles if supported else basis['section_titles'],'material_role':role,
        'confidence':'source-located-preparation' if supported else 'uncertain'}


def apply(builder,path):
    """Validate the complete profile against actual acquisition before mutation."""
    source_ref=builder.reference(path)
    def pairs(items):
        result={}
        for key,value in items:
            if key in result:raise ValueError('duplicate preparation decision JSON key')
            result[key]=value
        return result
    data=json.loads(Path(path).read_text(),object_pairs_hook=pairs,
        parse_constant=lambda value: (_ for _ in ()).throw(ValueError('nonfinite preparation decision JSON')))
    reader=SourceReader(builder)
    required={'schema_version','baseline_inventory_sha256','source_units','dispositions','visual_bindings','candidate_contexts'}
    if not isinstance(data,dict) or set(data)!=required or data['schema_version']!='material-preparation-dispositions/1':
        raise ValueError('material preparation decision schema differs')
    if not isinstance(data['baseline_inventory_sha256'],str) or not re.fullmatch('[0-9a-f]{64}',data['baseline_inventory_sha256']):
        raise ValueError('preparation baseline inventory fingerprint differs')
    if type(data['source_units']) is not int or data['source_units']!=len(builder.units):raise ValueError('preparation source unit scope differs')
    if not isinstance(data['dispositions'],list) or not isinstance(data['visual_bindings'],list) or not isinstance(data['candidate_contexts'],dict):
        raise ValueError('material preparation decision collections differ')
    # Standalone adapter calls must also refuse bytes changed since acquisition.
    # Each input is hashed once, rather than re-reading a PDF for every unit.
    for name,fingerprint in list(builder.inputs.items()):builder.reference(builder.root/name,fingerprint)
    units={u['id']:u for u in builder.units}
    if len(units)!=len(builder.units):raise ValueError('preparation source IDs duplicate')
    for unit in builder.units:
        for reference in [unit['source'],unit['source_document']]+unit.get('source_images',[]):
            if not isinstance(reference,dict) or builder.inputs.get(reference.get('path'))!=reference.get('sha256'):
                raise ValueError('preparation source reference is outside acquired input closure')
    expected={u['id'] for u in builder.units if u['classification_basis']['confidence']=='uncertain'}
    rows={}
    outcomes={}
    for row in data['dispositions']:
        if not isinstance(row,dict) or set(row)!={'id','group','raw_binding_sha256','original_classification_basis','original_classification'}:
            raise ValueError('material preparation disposition row schema differs')
        identity=row['id']
        if identity in rows or identity not in units:raise ValueError('preparation disposition has duplicate/unknown ID')
        unit=units[identity]
        if (row['group'] not in GROUPS or row['group']!=group_for(unit)
            or row['raw_binding_sha256']!=textsha(canonical(raw_binding(unit)))
            or row['original_classification']!=unit['classification']
            or row['original_classification_basis']!=unit['classification_basis']):
            raise ValueError('preparation disposition changed raw source/ID/context binding')
        rows[identity]=row;outcomes[identity]=disposition(unit,reader)
    if set(rows)!=expected:raise ValueError('preparation disposition omits or replaces an uncertain source unit')
    expected_visual={u['id'] for u in builder.units if u['classification']=='body' and u['source_material_form']=='image'
        and not u['translation_candidates'] and u['document_id']!='W242C'}
    bindings={};catalog={}
    for row in data['visual_bindings']:
        if not isinstance(row,dict) or set(row)!={'id','raw_binding_sha256','context_ids'} or not isinstance(row['context_ids'],list):
            raise ValueError('preparation visual binding schema differs')
        identity=row['id']
        if identity in bindings or identity not in expected_visual:raise ValueError('preparation visual binding has duplicate/unknown ID')
        unit=units[identity]
        if row['raw_binding_sha256']!=textsha(canonical(raw_binding(unit))):raise ValueError('preparation visual binding changed raw source')
        actual=candidate_sources(unit,reader)
        if len(row['context_ids'])!=len(set(row['context_ids'])) or set(row['context_ids'])!=set(actual):
            raise ValueError('preparation visual candidate field scope differs from actual related source records')
        if not actual:raise ValueError('preparation visual source lacks a located historical candidate')
        for identity2,reference in actual.items():
            if identity2 in catalog and catalog[identity2]!=reference:raise ValueError('preparation candidate catalog collision')
            catalog[identity2]=reference
        bindings[identity]=row
    if set(bindings)!=expected_visual or data['candidate_contexts']!=catalog:
        raise ValueError('preparation visual candidate catalog omits or invents related source fields')
    immutable={u['id']:immutable_binding(u) for u in builder.units}
    if any(u['review_status']!='not-executed' or u['independent_model_review'] is not False
        or u['human_professional_acceptance']!='pending' or u['organizational_approval']!='pending-signature' for u in builder.units):
        raise ValueError('preparation may not inherit or claim semantic acceptance')
    for identity,outcome in outcomes.items():
        unit=units[identity]
        unit['classification_preparation']={'decision_manifest':source_ref,'group':outcome['group'],
            'original_classification_basis':copy.deepcopy(unit['classification_basis']),
            'status':'source-located-disposition-prepared' if outcome['supported'] else 'source-disposition-pending-insufficient-evidence',
            'material_role':outcome['material_role'],'independent_semantic_review':'not-executed'}
        unit['classification']=outcome['classification']
        unit['classification_basis']={**unit['classification_basis'],'section_titles':outcome['section_titles'],
            'confidence':outcome['confidence'],'preparation_rule':outcome['group']}
        unit['classification_status']='source-disposition-prepared-independent-adjudication-pending' if outcome['supported'] else 'pending-independent-adjudication'
        unit['disposition']='保留原文、来源定位及原图；按'+outcome['material_role']+'记录来源处理；候选及语义可靠性须逐项独立复核，当前未验收。'
    for identity,row in bindings.items():
        unit=units[identity]
        for context_id in sorted(row['context_ids']):
            entry=catalog[context_id];value=pointer(reader.get(entry['reference']),entry['json_pointer'])
            if not isinstance(value,str) or textsha(value)!=entry['text_sha256']:raise ValueError('preparation candidate text/locator drift')
            candidate=builder.candidate(builder.root/entry['reference']['path'],entry['json_pointer'],value,'source-image-historical-field',status=PENDING)
            unit['translation_candidates'].append(candidate)
        unit['historical_candidate_binding']={'decision_manifest':source_ref,'status':PENDING,'candidate_fields':len(row['context_ids']),
            'semantic_reliability':'not-certified','independent_semantic_review':'not-executed'}
    if immutable!={u['id']:immutable_binding(u) for u in builder.units}:raise ValueError('preparation changed authoritative acquisition fields')
    builder.reference(builder.root/MODULE_PATH)
    return {'manifest':source_ref,'dispositions':len(rows),'supported_dispositions':sum(v['supported'] for v in outcomes.values()),
        'pending_ids':sorted(k for k,v in outcomes.items() if not v['supported']),
        'bound_English_body_visual_units':len(bindings),'unique_historical_candidate_fields':len(catalog),
        'independent_semantic_reviews_executed':0,'source_fields_unchanged':True}
