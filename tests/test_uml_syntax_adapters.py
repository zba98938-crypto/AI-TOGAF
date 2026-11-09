"""Pinned syntax adapters checked against direction and XML ownership oracles."""
import copy
import base64
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from lxml import etree

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'togaf-standard-10th-ai/skills/_shared/scripts'))
from uml_backend import official_rules,execution_rules,validate_mapped,official_query_adapters,JARS,ROOT as BACKEND_ROOT,ECLIPSE_UML,OMG_UML
from standards import Incomplete,sha

XMI='{http://www.omg.org/spec/XMI/20131001}'
UML='http://www.omg.org/spec/UML/20131001'
OPAQUE='OpaqueExpression-only_in_or_return_parameters'
TRANSITION='Transition-transition_vertices'
LIFELINE='Lifeline-interaction_uses_share_lifeline'
SAME_CLASSIFIER='Lifeline-same_classifier'


def syntax_fixture():
    root=etree.Element(XMI+'XMI',nsmap={'xmi':XMI[1:-1],'uml':UML})
    model=etree.SubElement(root,'{'+UML+'}Model');model.set(XMI+'id','M');model.set('name','Fictional syntax adapter cases')
    def add(parent,tag,kind,identity,**attrs):
        e=etree.SubElement(parent,tag);e.set(XMI+'type','uml:'+kind);e.set(XMI+'id',identity)
        for key,value in attrs.items():e.set(key,str(value))
        return e
    add(model,'packagedElement','PrimitiveType','STR',name='String')
    owner=add(model,'packagedElement','Class','VALUE_OWNER',name='ValueOwner')
    parameter_cases=[('E_'+direction.upper()+'_'+str(int(stream)),[(direction,stream)])
                     for direction in ('in','out','inout','return') for stream in (False,True)]
    parameter_cases += [('E_ABSENT',None),('E_EMPTY',[]),('E_ALLOWED_MIX',[('in',False),('return',False)]),
                        ('E_FORBIDDEN_MIX',[('in',False),('out',False)])]
    for identity,parameters in parameter_cases:
        prop=add(owner,'ownedAttribute','Property','PROP_'+identity,name=identity.lower(),type='STR')
        attrs={}
        if parameters is not None:
            behavior=add(model,'packagedElement','OpaqueBehavior','BEHAVIOR_'+identity,name=identity.lower()+'_behavior')
            for number,(direction,stream) in enumerate(parameters):
                add(behavior,'ownedParameter','Parameter','PARAM_'+identity+'_'+str(number),name='p'+str(number),
                    type='STR',direction=direction,isStream='true' if stream else 'false')
            attrs['behavior']='BEHAVIOR_'+identity
        add(prop,'defaultValue','OpaqueExpression',identity,**attrs)
    pa=add(model,'packagedElement','Package','PA',name='NamespaceA');pb=add(model,'packagedElement','Package','PB',name='NamespaceB')
    sa=add(pa,'packagedElement','StateMachine','SM_A',name='SameName');sb=add(pb,'packagedElement','StateMachine','SM_B',name='SameName')
    ra=add(sa,'region','Region','RA',name='direct');rb=add(sb,'region','Region','RB',name='foreign')
    for region,ids in [(ra,['A1','A2']),(rb,['B1','B2'])]:
        for identity in ids:add(region,'subvertex','State',identity,name=identity.lower())
    sibling=add(sa,'region','Region','RS',name='sibling');add(sibling,'subvertex','State','S1',name='siblingState')
    composite=add(ra,'subvertex','State','COMPOSITE',name='composite');nested=add(composite,'region','Region','RN',name='nested')
    for identity in ['N1','N2']:add(nested,'subvertex','State',identity,name=identity.lower())
    cases=[(ra,'T_DIRECT','A1','A2'),(nested,'T_NESTED','N1','N2'),(ra,'T_SIBLING','A1','S1'),
           (ra,'T_FOREIGN_SOURCE','B1','A1'),(ra,'T_FOREIGN_TARGET','A1','B1'),(ra,'T_BOTH_FOREIGN','B1','B2'),
           (ra,'T_NO_SOURCE',None,'A1'),(ra,'T_NO_TARGET','A1',None),(ra,'T_FALSE_AND_MISSING','B1',None)]
    for parent,identity,source,target in cases:
        attrs={'name':identity.lower()}
        if source:attrs['source']=source
        if target:attrs['target']=target
        add(parent,'transition','Transition',identity,**attrs)
    orphan=etree.SubElement(root,'{'+UML+'}Transition');orphan.set(XMI+'id','T_NO_CONTAINER');orphan.set('source','A1');orphan.set('target','A2')
    state=etree.SubElement(root,'{'+UML+'}State');state.set(XMI+'id','ORPHAN_STATE')
    add(ra,'transition','Transition','T_ORPHAN_ENDPOINT',name='orphanEndpoint',source='A1',target='ORPHAN_STATE')
    return etree.tostring(root,xml_declaration=True,encoding='UTF-8',pretty_print=True)


def fixture_oracles(data):
    """Read declared parameter values and climb XML owners, without UML queries."""
    root=etree.fromstring(data);objects={e.get(XMI+'id'):e for e in root.iter() if e.get(XMI+'id')}
    def kind(e):return e.get(XMI+'type','').split(':')[-1] or etree.QName(e).localname
    def machine(e):
        while e is not None:
            if kind(e)=='StateMachine':return e.get(XMI+'id')
            e=e.getparent()
        return None
    opaque={};transitions={}
    for identity,e in objects.items():
        if kind(e)=='OpaqueExpression':
            behavior=objects.get(e.get('behavior'))
            opaque[identity]=behavior is None or all(p.get('isStream','false')!='true' and p.get('direction','in') in {'in','return'}
                                                   for p in behavior.findall('ownedParameter'))
        elif kind(e)=='Transition':
            owner=machine(e);source=objects.get(e.get('source'));target=objects.get(e.get('target'))
            comparisons=[None if endpoint is None else machine(endpoint)==owner for endpoint in [source,target]]
            transitions[identity]='invalid' if owner is None else 'false' if False in comparisons else 'invalid' if None in comparisons else 'true'
    return {'opaque':opaque,'transition':transitions}


def query_boundary_probe(data):
    """Execute the native query and normative RHS separately, without adapters."""
    source=etree.parse(str(BACKEND_ROOT/'standards/sources/uml-2.5.1/UML.xmi'))
    operations={e.get(XMI+'id'):e for e in source.iter('ownedOperation')}
    transition_rhs=operations['Transition-containingStateMachine'].findtext('ownedRule/specification/body')[len('result = '):]
    vertex_rhs=operations['Vertex-containingStateMachine'].findtext('ownedRule/specification/body')[len('result = '):]
    executable,_=execution_rules(official_rules()[0]);body=next(r['body'] for r in executable if r['id']==TRANSITION)
    probes=[{'context':'Transition','id':'native-owner-null','body':'self.containingStateMachine() = null'},
            {'context':'Transition','id':'normative-owner-null','body':'('+transition_rhs+') = null'},
            {'context':'Transition','id':'normative-owner-vertices','body':body.replace('self.containingStateMachine()',transition_rhs,1)},
            {'context':'Vertex','id':'native-vertex-null','body':'self.containingStateMachine() = null'},
            {'context':'Vertex','id':'normative-vertex-null','body':'('+vertex_rhs+') = null'}]
    original=etree.fromstring(data);mapping={OMG_UML:ECLIPSE_UML,XMI[1:-1]:'http://www.omg.org/XMI'}
    def mapped(e):
        tag=e.tag
        for old,new in mapping.items():tag=tag.replace('{'+old+'}','{'+new+'}')
        n=etree.Element(tag,nsmap={k:mapping.get(v,v) for k,v in e.nsmap.items()} if e is original else None)
        for key,value in e.attrib.items():
            for old,new in mapping.items():key=key.replace('{'+old+'}','{'+new+'}')
            n.set(key,value)
        n.text=e.text;n.tail=e.tail
        for child in e:n.append(mapped(child))
        return n
    def tsv(rows,fields):return '\n'.join('\t'.join(base64.b64encode(row[k].encode()).decode() for k in fields) for row in rows)+'\n'
    with tempfile.TemporaryDirectory(prefix='uml-query-boundary-') as folder:
        folder=Path(folder);model=folder/'probe.uml';model.write_bytes(etree.tostring(mapped(original),xml_declaration=True,encoding='UTF-8'))
        rules=folder/'probes.tsv';rules.write_text(tsv(probes,('context','id','body')))
        queries=folder/'queries.tsv';queries.write_text(tsv(official_query_adapters(),('context','id','definition')))
        result=subprocess.run([str(Path(os.environ['JAVA_HOME'])/'bin/java'),'-Xmx512m','--class-path',str(JARS/'*'),
                               str(BACKEND_ROOT/'scripts/UmlValidate.java'),str(model),str(rules),str(JARS),str(queries)],
                              capture_output=True,text=True,timeout=120,check=True)
        return json.loads(result.stdout)


class SyntaxAdapterSourceGuards(unittest.TestCase):
    def test_only_execution_copies_of_four_pinned_bodies_change(self):
        rows,digest=official_rules();original=copy.deepcopy(rows);executable,adapters=execution_rules(rows)
        self.assertEqual(original,rows);self.assertEqual(425,len(rows));self.assertEqual(digest,official_rules()[1])
        self.assertEqual({OPAQUE,TRANSITION,LIFELINE,SAME_CLASSIFIER},{a['id'] for a in adapters})
        self.assertEqual({OPAQUE,TRANSITION,LIFELINE,SAME_CLASSIFIER},{r['id'] for r,e in zip(rows,executable) if r['body']!=e['body']})
        for adapter in adapters:
            self.assertEqual(sha(adapter['original_body'].encode()),adapter['original_body_sha256'])
            self.assertEqual(sha(adapter['execution_body'].encode()),adapter['execution_body_sha256'])
    def test_body_whitespace_context_and_wrong_id_do_not_bypass_fingerprint_guard(self):
        for identity in [OPAQUE,TRANSITION,LIFELINE,SAME_CLASSIFIER]:
            for field,value in [('body',None),('context','State'),('id',identity+'-different')]:
                rows,_=official_rules();row=next(r for r in rows if r['id']==identity)
                row[field]=row[field]+' ' if value is None else value
                with self.subTest(identity=identity,field=field),self.assertRaises(Incomplete):execution_rules(rows)
            rows,_=official_rules();row=next(r for r in rows if r['id']==identity)
            with self.subTest(identity=identity,field='missing'),self.assertRaises(Incomplete):execution_rules([r for r in rows if r is not row])
            with self.subTest(identity=identity,field='duplicate'),self.assertRaises(Incomplete):execution_rules(rows+[dict(row)])


@unittest.skipUnless(os.getenv('JAVA_HOME') and (Path(os.getenv('JAVA_HOME',''))/'bin/java').is_file(),'set isolated JAVA_HOME to execute Java OCL')
class ActualSyntaxAdapterOracleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=syntax_fixture();cls.expected=fixture_oracles(cls.data);cls.report=validate_mapped(cls.data)
    def test_complete_direction_stream_matrix_and_absence_mixed_cases(self):
        row=next(r for r in self.report['ocl_rules'] if r['id']==OPAQUE)
        self.assertEqual('parsed',row['parse_status']);self.assertEqual(12,row['applicable']);self.assertEqual(0,row['invalid_evaluations'])
        self.assertEqual({identity for identity,value in self.expected['opaque'].items() if not value},set(row['violation_ids']))
        matrix={identity for identity in self.expected['opaque'] if identity.endswith(('_0','_1'))}
        self.assertEqual(8,len(matrix));self.assertEqual(6,len(matrix&set(row['violation_ids'])))
    def test_transition_against_independent_xml_ownership_and_three_valued_oracle(self):
        row=next(r for r in self.report['ocl_rules'] if r['id']==TRANSITION)
        self.assertEqual('parsed',row['parse_status']);self.assertEqual(len(self.expected['transition']),row['applicable'])
        # Eclipse's native query returns null for a missing required container;
        # the normative query RHS navigates null and is invalid. Keep that
        # oracle expectation and assert the one observed difference explicitly.
        boundary={'T_NO_CONTAINER'}
        self.assertEqual({identity for identity,value in self.expected['transition'].items() if value=='false'},set(row['violation_ids'])-boundary)
        self.assertEqual({identity for identity,value in self.expected['transition'].items() if value=='invalid'}-boundary,set(row['invalid_ids']))
        self.assertEqual('invalid',self.expected['transition']['T_NO_CONTAINER']);self.assertIn('T_NO_CONTAINER',row['violation_ids'])
        self.assertEqual('false',self.expected['transition']['T_FALSE_AND_MISSING'])
    def test_missing_required_owner_keeps_normative_invalid_and_native_query_divergence_explicit(self):
        probes=query_boundary_probe(self.data);rows={r['id']:r for r in probes['ocl_rules']}
        self.assertTrue(all(row['parse_status']=='parsed' for row in rows.values()))
        native=rows['native-owner-null'];normative=rows['normative-owner-null'];vertices=rows['normative-owner-vertices']
        self.assertEqual(len(self.expected['transition']),native['applicable'])
        self.assertEqual(0,native['invalid_evaluations']);self.assertNotIn('T_NO_CONTAINER',native['violation_ids'])
        self.assertEqual({'T_NO_CONTAINER'},set(normative['invalid_ids']));self.assertNotIn('T_NO_CONTAINER',normative['violation_ids'])
        self.assertEqual({identity for identity,value in self.expected['transition'].items() if value=='false'},set(vertices['violation_ids']))
        self.assertEqual({identity for identity,value in self.expected['transition'].items() if value=='invalid'},set(vertices['invalid_ids']))
        self.assertEqual(rows['native-vertex-null']['violation_ids'],rows['normative-vertex-null']['violation_ids'])
        self.assertEqual([],rows['normative-vertex-null']['invalid_ids']);self.assertNotIn('ORPHAN_STATE',rows['native-vertex-null']['violation_ids'])
        required=[d for d in self.report['diagnostics'] if '#T_NO_CONTAINER' in d['message'] and "required feature 'container'" in d['message']]
        self.assertEqual(1,len(required));self.assertEqual(4,required[0]['severity'])
    def test_report_preserves_source_authority_and_lifeline_prose_basis(self):
        self.assertEqual(425,self.report['normative_ocl_rule_count']);self.assertEqual(425,self.report['ocl_parsed']);self.assertEqual(0,self.report['ocl_unmapped'])
        self.assertFalse(self.report['official_full_conformance']);self.assertEqual('incomplete',self.report['conformance_status'])
        pending=next(r for r in self.report['ocl_rules'] if r['id']==LIFELINE)
        self.assertEqual('parsed',pending['parse_status'])
        self.assertEqual([LIFELINE,SAME_CLASSIFIER],[a['id'] for a in self.report['semantic_adapters']])
        self.assertEqual([664,665],self.report['semantic_adapters'][0]['basis']['pdf_pages'])
        self.assertEqual({OPAQUE,TRANSITION},{a['id'] for a in self.report['syntax_adapters']})


if __name__=='__main__':unittest.main()
