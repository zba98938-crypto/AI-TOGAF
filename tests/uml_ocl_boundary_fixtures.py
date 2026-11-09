"""Explicit XML graph/values for independent UML OCL boundary oracles."""
from lxml import etree
XMI='{http://www.omg.org/spec/XMI/20131001}'
UML='http://www.omg.org/spec/UML/20131001'
def lifeline_classifier_fixture():
    root=etree.Element('{'+UML+'}Model',nsmap={'uml':UML,'xmi':XMI[1:-1]});root.set(XMI+'id','M');root.set('name','OCL boundary fixtures')
    def add(parent,tag,kind,identity,**attrs):
        e=etree.SubElement(parent,tag);e.set(XMI+'type','uml:'+kind);e.set(XMI+'id',identity)
        for key,value in attrs.items():e.set(key,str(value))
        return e
    classes={}
    for identity in ['GRAND','PARENT','CHILD','UNRELATED']:
        classes[identity]=add(root,'packagedElement','Class',identity,name=identity.lower())
    add(classes['PARENT'],'generalization','Generalization','G_PARENT',general='GRAND')
    add(classes['CHILD'],'generalization','Generalization','G_CHILD',general='PARENT')
    nested=add(classes['CHILD'],'nestedClassifier','Class','NESTED',name='nested')
    classes['NESTED']=nested
    for identity,owner in classes.items():add(owner,'ownedAttribute','Property','P_'+identity,name='part_'+identity.lower())
    multi=add(classes['CHILD'],'ownedAttribute','Property','P_MULTI',name='multi')
    add(multi,'upperValue','LiteralUnlimitedNatural','P_MULTI_UPPER',value='*')
    interaction=add(classes['CHILD'],'ownedBehavior','Interaction','I',name='interaction')
    for identity,represented in [('L_SELF','P_CHILD'),('L_PARENT','P_PARENT'),('L_GRAND','P_GRAND'),
                                  ('L_UNRELATED','P_UNRELATED'),('L_NESTED','P_NESTED'),('L_ABSENT',None),
                                  ('L_MULTI_ABSENT','P_MULTI'),('L_MULTI_INT','P_MULTI'),
                                  ('L_MULTI_STRING','P_MULTI'),('L_MULTI_BOOLEAN','P_MULTI'),('L_SINGLE_INT','P_CHILD')]:
        attrs={'name':identity.lower()}
        if represented:attrs['represents']=represented
        ll=add(interaction,'lifeline','Lifeline',identity,**attrs)
        if identity.endswith('_INT'):add(ll,'selector','LiteralInteger',identity+'_SELECTOR',value='2')
        if identity.endswith('_STRING'):add(ll,'selector','LiteralString',identity+'_SELECTOR',value='east')
        if identity.endswith('_BOOLEAN'):add(ll,'selector','LiteralBoolean',identity+'_SELECTOR',value='true')
    return etree.tostring(root,xml_declaration=True,encoding='UTF-8')

def classifier_oracle(data):
    """Closest containing XML classifier plus explicit generalization graph."""
    root=etree.fromstring(data);objects={e.get(XMI+'id'):e for e in root.iter() if e.get(XMI+'id')}
    def kind(e):return e.get(XMI+'type','').split(':')[-1]
    def owner_class(e):
        e=e.getparent()
        while e is not None:
            if kind(e)=='Class':return e.get(XMI+'id')
            e=e.getparent()
        return None
    parents={identity:{g.get('general') for g in e.findall('generalization')} for identity,e in objects.items() if kind(e)=='Class'}
    def ancestors(identity):
        reached=set();todo=list(parents.get(identity,()))
        while todo:
            candidate=todo.pop()
            if candidate in reached:continue
            reached.add(candidate);todo.extend(parents.get(candidate,()))
        return reached
    result={}
    for identity,ll in objects.items():
        if kind(ll)!='Lifeline':continue
        represented=objects.get(ll.get('represents'))
        if represented is None:result[identity]='invalid';continue
        context=owner_class(ll);part=owner_class(represented)
        result[identity]='true' if part==context or part in ancestors(context) else 'false'
    return result

def boolean_boundary_expressions():
    # All compound literal cases are explicitly grouped. Expectations follow
    # the published truth tables, independently of the Java parser/visitor.
    return {'(not null)':'null','((null)) and ((invalid))':'invalid',
        'false and (null or invalid)':'false','(null or invalid) or true':'true',
        '(not invalid) and false':'false','(null and invalid) implies true':'true',
        'let n : Boolean = null in (n or false) and true':'null',
        'let i : Boolean = invalid in i implies true':'true',
        'if null then true else false endif':'invalid','if invalid then true else false endif':'invalid',
        'false and (1.div(0) = 0)':'false','(1.div(0) = 0) and false':'false',
        "'not null' = 'not null'":'true',"'null and invalid'":'non-boolean'}

def parser_compatible_large_boolean_expressions():
    """Known installed-parser inputs; fallback bounds must never apply."""
    return {'('*65+'true'+')'*65:'true',
        ' and '.join(['true']*1025):'true',
        '('*64+'false'+')'*64:'false',
        'not '*64+'false':'false'}

def balanced_over_token_boolean_expression():
    """Valid bounded-depth literal tree exceeds the fallback token ceiling."""
    expression='(null and invalid)'
    for _ in range(9):expression='('+expression+' and '+expression+')'
    return expression

def multiplicity_boundary_fixture():
    root=etree.Element('{'+UML+'}Model',nsmap={'uml':UML,'xmi':XMI[1:-1]});root.set(XMI+'id','M');root.set('name','Multiplicity boundaries')
    owner=etree.SubElement(root,'packagedElement');owner.set(XMI+'type','uml:Class');owner.set(XMI+'id','C');owner.set('name','Owner')
    cases={'P_DEFAULT':(1,1),'P_ZERO':(0,0),'P_FINITE':(2,5),'P_UNLIMITED':(1,'*')}
    for identity,(lower,upper) in cases.items():
        prop=etree.SubElement(owner,'ownedAttribute');prop.set(XMI+'type','uml:Property');prop.set(XMI+'id',identity);prop.set('name',identity)
        if identity=='P_DEFAULT':continue
        for field,kind,value in [('lowerValue','LiteralInteger',lower),('upperValue','LiteralUnlimitedNatural',upper)]:
            scalar=etree.SubElement(prop,field);scalar.set(XMI+'type','uml:'+kind);scalar.set(XMI+'id',identity+'_'+field);scalar.set('value',str(value))
    return etree.tostring(root,xml_declaration=True,encoding='UTF-8'),cases
