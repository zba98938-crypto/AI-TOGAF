"""Independent native UMLDI fixtures with deliberately noncanonical decimals."""
HEAD = '''<xmi:XMI xmlns:xmi="http://www.omg.org/spec/XMI/20131001"
 xmlns:u="http://www.omg.org/spec/UML/20131001"
 xmlns:ud="http://www.omg.org/spec/UML/20161101/UMLDI"
 xmlns:dc="http://www.omg.org/spec/DD/20131001/DC">'''
MODEL = '''<u:Model xmi:id="M" name="Native class view">
 <packagedElement xmi:type="u:PrimitiveType" xmi:id="STRING" name="String"/>
 <packagedElement xmi:type="u:Class" xmi:id="ORDER" name="Order">
  <ownedAttribute xmi:id="STATUS" name="status" type="STRING"/>
  <ownedOperation xmi:id="SUBMIT" name="submit"/>
  <generalization xmi:id="GENERAL" general="ENTITY"/>
 </packagedElement>
 <packagedElement xmi:type="u:Class" xmi:id="ENTITY" name="Entity" isAbstract="true"/>
 <packagedElement xmi:type="u:Class" xmi:id="LINE" name="OrderLine"/>
 <packagedElement xmi:type="u:Association" xmi:id="REL" memberEnd="END_ORDER END_LINE">
  <ownedEnd xmi:id="END_ORDER" type="ORDER" association="REL"/>
  <ownedEnd xmi:id="END_LINE" type="LINE" association="REL">
   <lowerValue xmi:type="u:LiteralInteger" value="0"/>
   <upperValue xmi:type="u:LiteralUnlimitedNatural" value="*"/>
  </ownedEnd>
 </packagedElement>
</u:Model>
<ud:UMLStyle xmi:id="STYLE" fontSize="12"/>'''
DI = '''<ud:UMLClassDiagram xmi:id="D" name="Native view" resolution="96" isFrame="false">
 <ownedElement xmi:type="ud:UMLClassifierShape" xmi:id="S_ORDER" modelElement="ORDER" sharedStyle="STYLE">
  <bounds xmi:type="dc:Bounds" x="20.5000" y="30.25" width="240" height="240"/>
  <ownedElement xmi:type="ud:UMLLabel" xmi:id="L_ORDER" modelElement="ORDER" text="Order">
   <bounds xmi:type="dc:Bounds" x="40.5000" y="50.25" width="200" height="24"/>
  </ownedElement>
  <compartment xmi:type="ud:UMLCompartment" xmi:id="C_ATTR">
   <elementInCompartment xmi:type="ud:UMLLabel" xmi:id="L_ATTR" modelElement="STATUS" text="status : String">
    <bounds xmi:type="dc:Bounds" x="40.5000" y="102.50" width="200" height="24"/>
   </elementInCompartment>
  </compartment>
  <compartment xmi:type="ud:UMLCompartment" xmi:id="C_OP">
   <elementInCompartment xmi:type="ud:UMLLabel" xmi:id="L_OP" modelElement="SUBMIT" text="submit()">
    <bounds xmi:type="dc:Bounds" x="40.5000" y="164.500" width="200" height="24"/>
   </elementInCompartment>
  </compartment>
 </ownedElement>
 <ownedElement xmi:type="ud:UMLClassifierShape" xmi:id="S_ENTITY" modelElement="ENTITY" sharedStyle="STYLE">
  <bounds xmi:type="dc:Bounds" x="450.25" y="30.25" width="200" height="100"/>
  <ownedElement xmi:type="ud:UMLLabel" xmi:id="L_ENTITY" modelElement="ENTITY" text="Entity">
   <bounds xmi:type="dc:Bounds" x="470.25" y="50.25" width="160" height="24"/>
  </ownedElement>
 </ownedElement>
 <ownedElement xmi:type="ud:UMLClassifierShape" xmi:id="S_LINE" modelElement="LINE" sharedStyle="STYLE">
  <bounds xmi:type="dc:Bounds" x="450.25" y="200.25" width="200" height="140"/>
  <ownedElement xmi:type="ud:UMLLabel" xmi:id="L_LINE" modelElement="LINE" text="OrderLine">
   <bounds xmi:type="dc:Bounds" x="470.25" y="220.25" width="160" height="24"/>
  </ownedElement>
 </ownedElement>
 <ownedElement xmi:type="ud:UMLEdge" xmi:id="E_GENERAL" source="S_ORDER" target="S_ENTITY" modelElement="GENERAL">
  <waypoint xmi:type="dc:Point" x="260.5000" y="60.25"/>
  <waypoint xmi:type="dc:Point" x="355.7500" y="60.25"/>
  <waypoint xmi:type="dc:Point" x="450.25" y="60.25"/>
 </ownedElement>
 <ownedElement xmi:type="ud:UMLEdge" xmi:id="E_ASSOC" source="S_ORDER" target="S_LINE" modelElement="REL">
  <waypoint xmi:type="dc:Point" x="260.5000" y="250.25"/>
  <waypoint xmi:type="dc:Point" x="360.7500" y="250.25"/>
  <waypoint xmi:type="dc:Point" x="450.25" y="260.25"/>
  <ownedElement xmi:type="ud:UMLMultiplicityLabel" xmi:id="L_MULT" modelElement="END_LINE" text="0..*">
   <bounds xmi:type="dc:Bounds" x="380.7500" y="270.25" width="60" height="24"/>
  </ownedElement>
 </ownedElement>
</ud:UMLClassDiagram>'''


def document(model=MODEL, diagram=DI):
    return (HEAD + model + diagram + '</xmi:XMI>').encode('utf-8')


def framed_document():
    diagram=DI.replace('isFrame="false"','isFrame="true" heading="H"')
    diagram=diagram.replace('isFrame="true" heading="H">', '''isFrame="true" heading="H">
 <bounds xmi:type="dc:Bounds" x="0" y="0" width="680" height="370"/>
 <ownedElement xmi:type="ud:UMLLabel" xmi:id="H" text="class Native view">
  <bounds xmi:type="dc:Bounds" x="20" y="5" width="300" height="24"/>
 </ownedElement>''')
    return document(diagram=diagram)
