"""Independent XML abstract expressions and published four-valued expectations.

No import of the backend parser or visitor. XML structure is the oracle input;
OCL source text and branch expectations are derived separately from this tree.
"""
from itertools import product
from lxml import etree

VALUES=('true','false','null','invalid')
TYPES=('OclInvalid','OclVoid','Boolean')
# Independent OCL 2.4 8.2.1, 8.3.7 and 8.3.8 common-supertype table.
COMMON_TYPES=(('OclInvalid','OclVoid','Boolean'),('OclVoid','OclVoid','Boolean'),('Boolean','Boolean','Boolean'))
def literal(value):return etree.Element(value)
def conditional(condition,then_branch,else_branch):
    result=etree.Element('if')
    for tag,node in [('condition',condition),('then',then_branch),('else',else_branch)]:
        result.append(etree.Element(tag));result[-1].append(node)
    return result

def operation(name,left,right=None):
    result=etree.Element(name);result.append(left)
    if right is not None:result.append(right)
    return result

def source(node):
    if node.tag in VALUES:return node.tag
    if node.tag=='if':return 'if '+source(node[0][0])+' then '+source(node[1][0])+' else '+source(node[2][0])+' endif'
    if node.tag=='not':return '(not '+source(node[0])+')'
    return '('+source(node[0])+' '+node.tag+' '+source(node[1])+')'

# OCL 2.4 Boolean table, independent literal matrices; order is VALUES above.
TABLES={
 'and':(('true','false','null','invalid'),('false','false','false','false'),('null','false','null','invalid'),('invalid','false','invalid','invalid')),
 'or':(('true','true','true','true'),('true','false','null','invalid'),('true','null','null','invalid'),('true','invalid','invalid','invalid')),
 'xor':(('false','true','null','invalid'),('true','false','null','invalid'),('null','null','null','invalid'),('invalid','invalid','invalid','invalid')),
 'implies':(('true','false','null','invalid'),('true','true','true','true'),('true','null','null','invalid'),('true','invalid','invalid','invalid'))}

def oracle(node,path='root',selected=None):
    if selected is None:selected=[]
    if node.tag in VALUES:return node.tag
    if node.tag=='if':
        value=oracle(node[0][0],path+'/condition',selected)
        if value not in ('true','false'):return 'invalid'
        branch=1 if value=='true' else 2
        label=path+('/thenExpression' if branch==1 else '/elseExpression');selected.append(label)
        return oracle(node[branch][0],label,selected)
    left=oracle(node[0],path+'/source',selected)
    if node.tag=='not':return dict(zip(VALUES,('false','true','null','invalid')))[left]
    # Published dominating-value controls avoid accessing irrelevant subtrees.
    if (node.tag=='and' and left=='false') or (node.tag=='or' and left=='true') or (node.tag=='implies' and left=='false'):
        return 'false' if node.tag=='and' else 'true'
    right=oracle(node[1],path+'/argument/0',selected)
    return TABLES[node.tag][VALUES.index(left)][VALUES.index(right)]

def xml_shape(node):
    if node.tag in VALUES:return node.tag
    if node.tag=='if':return ['if']+[xml_shape(node[i][0]) for i in range(3)]
    return [node.tag]+[xml_shape(child) for child in node]

def type_oracle(node):
    if node.tag in ('true','false'):return 'Boolean'
    if node.tag=='null':return 'OclVoid'
    if node.tag=='invalid':return 'OclInvalid'
    if node.tag=='if':
        condition=type_oracle(node[0][0])
        if condition not in TYPES:raise AssertionError('non Boolean-conforming condition')
        left=type_oracle(node[1][0]);right=type_oracle(node[2][0])
        return COMMON_TYPES[TYPES.index(left)][TYPES.index(right)]
    if node.tag not in TABLES and node.tag!='not':raise AssertionError('outside independent literal type oracle')
    for child in node:
        if type_oracle(child) not in TYPES:raise AssertionError('non Boolean-conforming operand')
    return 'Boolean'

def assert_native_types(node,ast,path='root'):
    """Check every subtree's static type, including branches never evaluated."""
    if ast['node']=='LetExp':
        if ast['variable']['name']!='__literal_condition':raise AssertionError(path+': unexpected let adaptation')
        for value in (ast['type'],ast['variable']['type'],ast['in']['type']):
            if value!='Boolean':raise AssertionError(path+': local Boolean let type mismatch')
        if ast['in']['node']!='VariableExp':raise AssertionError(path+': unexpected local let body')
        assert_native_types(node,ast['variable']['initExpression'],path+'/variable/initExpression');return
    expected=type_oracle(node)
    if ast['type']!=expected:raise AssertionError(path+': '+str(ast['type'])+' != '+expected)
    if native_shape(ast)!=xml_shape(node):raise AssertionError(path+': source and native AST shape mismatch')
    if node.tag in VALUES:return
    if node.tag=='if':
        for i,key in enumerate(('condition','thenExpression','elseExpression')):
            assert_native_types(node[i][0],ast[key],path+'/'+key)
    else:
        assert_native_types(node[0],ast['source'],path+'/source')
        for i,child in enumerate(node[1:]):assert_native_types(child,ast['argument'][i],path+'/argument/'+str(i))

def common_type_regressions():
    # Fixed independent source/XML pairs preserve the five first failed inputs.
    specs=[
      ('else-nested-undefined-condition','if false then invalid else if null then if true then true else invalid endif else if false then null else invalid endif endif endif','<if><false/><invalid/><if><null/><if><true/><true/><invalid/></if><if><false/><null/><invalid/></if></if></if>','failed'),
      ('both-branches-common-OclVoid','if false then if true then null else invalid endif else if false then invalid else null endif endif','<if><false/><if><true/><null/><invalid/></if><if><false/><invalid/><null/></if></if>','parsed'),
      ('nested-condition-OclVoid-to-Boolean-let','if if false then invalid else if true then null else invalid endif endif then if false then true else null endif else invalid endif','<if><if><false/><invalid/><if><true/><null/><invalid/></if></if><if><false/><true/><null/></if><invalid/></if>','failed'),
      ('grouped-implies-condition-with-null-sub-if','if (if true then null else invalid endif implies (not false)) then (if false then invalid else null endif or true) else invalid endif','<if><implies><if><true/><null/><invalid/></if><not><false/></not></implies><or><if><false/><invalid/><null/></if><true/></or><invalid/></if>','parsed'),
      ('not-nested-OclVoid-condition','if (not if true then null else invalid endif) then false else if true then invalid else null endif endif','<if><not><if><true/><null/><invalid/></if></not><false/><if><true/><invalid/><null/></if></if>','failed')]
    def convert(node):
        if node.tag=='if':return conditional(*(convert(child) for child in node))
        if node.tag in VALUES:return literal(node.tag)
        return operation(node.tag,*(convert(child) for child in node))
    result=[]
    for name,body,xml,original in specs:
        node=convert(etree.fromstring(xml.encode()))
        result.append({'id':name,'body':body,'xml':etree.tostring(node).decode(),'expected':oracle(node),
            'expected_type':type_oracle(node),'shape':xml_shape(node),'original_status':original})
    return result

def native_shape(ast):
    tag=ast['node']
    if tag=='BooleanLiteralExp':return 'true' if ast['booleanSymbol'] else 'false'
    if tag=='NullLiteralExp':return 'null'
    if tag=='InvalidLiteralExp':return 'invalid'
    if tag=='LetExp':
        # Only the explicit execution adapter's locally bound condition.
        if ast['variable']['name']!='__literal_condition':raise AssertionError('unexpected let adaptation')
        if ast['type']!='Boolean' or ast['in']['type']!='Boolean':raise AssertionError('undefined condition not Boolean typed')
        return native_shape(ast['variable']['initExpression'])
    if tag=='IfExp':return ['if']+[native_shape(ast[key]) for key in ('condition','thenExpression','elseExpression')]
    if tag=='OperationCallExp':return [ast['operation'],native_shape(ast['source'])]+[native_shape(a) for a in ast.get('argument',[])]
    raise AssertionError('unexpected AST node '+tag)

def trace_mapping(ast,actual='root',logical='root',result=None):
    if result is None:result={}
    result[actual]=logical
    if ast['node']=='LetExp' and ast['variable'].get('name')=='__literal_condition':
        trace_mapping(ast['variable']['initExpression'],actual+'/variable/initExpression',logical,result)
        result[actual+'/in']=logical
        return result
    for name,value in ast.items():
        if isinstance(value,dict) and 'node' in value:trace_mapping(value,actual+'/'+name,logical+'/'+name,result)
        if isinstance(value,list):
            for i,child in enumerate(value):
                if isinstance(child,dict) and 'node' in child:trace_mapping(child,actual+'/'+name+'/'+str(i),logical+'/'+name+'/'+str(i),result)
    return result

def branch_paths(node,path='root'):
    if node.tag in VALUES:return []
    if node.tag=='if':
        a=path+'/thenExpression';b=path+'/elseExpression'
        return [a,b]+branch_paths(node[0][0],path+'/condition')+branch_paths(node[1][0],a)+branch_paths(node[2][0],b)
    return sum((branch_paths(child,path+('/source' if i==0 else '/argument/0')) for i,child in enumerate(node)),[])

def cases():
    rows=[]
    for c,a,b in product(VALUES,repeat=3):rows.append(conditional(literal(c),literal(a),literal(b)))
    for c,a in product(VALUES,repeat=2):
        rows.append(conditional(literal(c),conditional(literal(a),literal('true'),literal('invalid')),literal('false')))
        rows.append(conditional(conditional(literal(c),literal(a),literal('false')),literal('true'),literal('false')))
    for op in ('and','or','xor','implies'):
        for a,b in product(('null','invalid'),repeat=2):rows.append(conditional(operation(op,literal(a),literal(b)),literal('true'),literal('false')))
    rows += [conditional(literal('false'),conditional(literal('null'),literal('true'),literal('true')),literal('true')),
             conditional(literal('true'),literal('false'),conditional(literal('invalid'),literal('false'),literal('false'))),
             conditional(operation('not',literal('null')),literal('true'),literal('false'))]
    return [{'id':'xml-'+str(i),'xml':etree.tostring(node).decode(),'body':source(node),'expected':oracle(node),'shape':xml_shape(node)} for i,node in enumerate(rows)]
