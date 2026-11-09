"""Independent raw XML scalar oracle; it never calls native/production helpers."""
from lxml import etree
UML='http://www.omg.org/spec/UML/20131001'
XMI='{http://www.omg.org/spec/XMI/20131001}'

def multiplicity_operation_fixture():
    root=etree.Element('{'+UML+'}Model',nsmap={'uml':UML,'xmi':XMI[1:-1]});root.set(XMI+'id','M');root.set('name','Operation frames')
    owner=etree.SubElement(root,'packagedElement');owner.set(XMI+'type','uml:Class');owner.set(XMI+'id','C');owner.set('name','Owner')
    definitions=[('DEFAULT',None,None),('ZERO',('LiteralInteger','0'),('LiteralUnlimitedNatural','0')),
        ('FINITE',('LiteralInteger','2'),('LiteralUnlimitedNatural','5')),
        ('UNLIMITED',('LiteralInteger','1'),('LiteralUnlimitedNatural','*')),
        ('OPTIONAL',('LiteralInteger','0'),('LiteralUnlimitedNatural','1')),
        ('WRONG_LOWER',('LiteralString','text'),('LiteralUnlimitedNatural','1')),
        ('WRONG_UPPER',('LiteralInteger','1'),('LiteralString','text')),
        ('NULL_LOWER',('LiteralNull',None),('LiteralUnlimitedNatural','1')),
        ('NULL_UPPER',('LiteralInteger','1'),('LiteralNull',None)),
        ('OPAQUE_LOWER',('OpaqueExpression',None),('LiteralUnlimitedNatural','1')),
        ('OPAQUE_UPPER',('LiteralInteger','1'),('OpaqueExpression',None))]
    for identity,lower,upper in definitions:
        prop=etree.SubElement(owner,'ownedAttribute');prop.set(XMI+'type','uml:Property');prop.set(XMI+'id',identity);prop.set('name',identity)
        for field,definition in [('lowerValue',lower),('upperValue',upper)]:
            if definition is None:continue
            kind,value=definition;child=etree.SubElement(prop,field);child.set(XMI+'type','uml:'+kind);child.set(XMI+'id',identity+'_'+field)
            if value is not None:child.set('value',value)
    return etree.tostring(root,xml_declaration=True,encoding='UTF-8')

def scalar_xml_oracle(data):
    root=etree.fromstring(data);results={}
    for prop in root.iter('ownedAttribute'):
        values={};boundaries=[]
        for role,expected_kind in [('lowerValue','LiteralInteger'),('upperValue','LiteralUnlimitedNatural')]:
            child=prop.find(role)
            if child is None:
                value=1
            elif child.get(XMI+'type')!='uml:'+expected_kind:
                # The inherited ValueSpecification scalar query is null,
                # so the normative MultiplicityElement bound defaults to 1.
                value=1;boundaries.append({'role':role,'kind':child.get(XMI+'type'),'optional_scalar_query':'null'})
            else:
                text=child.get('value','0');value='*' if text=='*' else int(text)
            values['lower' if role=='lowerValue' else 'upper']=value
        results[prop.get(XMI+'id')]={**values,'nullable_carrier_boundaries':boundaries}
    return results

def expected_native_value(operation,self_id,arguments,oracle):
    own=oracle[self_id];low,high=own['lower'],own['upper']
    if operation in {'lower','lowerBound'}:return ('integer',low)
    if operation in {'upper','upperBound'}:return ('unlimited',high)
    if operation=='isMultivalued':answer=high=='*' or high>1
    elif operation=='is':answer=arguments[0]['value']==low and arguments[1]['value']==high
    else:
        other=oracle[arguments[0]['value']]
        if operation=='includesMultiplicity':
            answer=low<=other['lower'] and (high=='*' or (other['upper']!='*' and high>=other['upper']))
        elif operation=='compatibleWith':
            answer=other['lower']<=low and (other['upper']=='*' or (high!='*' and high<=other['upper']))
        else:raise AssertionError('unsupported independent oracle operation')
    return ('true' if answer else 'false',answer)

def positive_cases(catalog,oracle):
    cases=[];valid=[identity for identity,values in oracle.items() if not values['nullable_carrier_boundaries']]
    for operation in catalog['operations']:
        for identity in valid:
            if operation['name'] in {'compatibleWith','includesMultiplicity'}:
                inputs=[([{'kind':'object','value':other}],other) for other in valid]
            elif operation['name']=='is':
                values=oracle[identity];inputs=[([{'kind':'integer','value':values['lower']},{'kind':'unlimited','value':values['upper']}],'match'),
                    ([{'kind':'integer','value':values['lower']+1},{'kind':'unlimited','value':values['upper']}],'mismatch')]
            else:inputs=[([], 'scalar')]
            for arguments,label in inputs:
                cases.append({'id':operation['name']+'-'+identity+'-'+label,'self':identity,'obligation':operation['source_identity']['key'],'arguments':arguments})
            if operation['derived']:
                cases.append({'id':'derived-'+operation['name']+'-'+identity,'self':identity,'obligation':operation['derived']['source_identity']['key']})
    return cases
