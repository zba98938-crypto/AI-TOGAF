import java.util.*;
import java.nio.file.*;
import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.*;
import org.eclipse.emf.ecore.resource.*;
import org.eclipse.emf.ecore.resource.impl.*;
import org.eclipse.uml2.uml.resource.UMLResource;
import org.eclipse.uml2.uml.resources.util.UMLResourcesUtil;
import org.eclipse.ocl.uml.OCL;
import org.eclipse.ocl.uml.OCLExpression;
public class UmlConditionalProbe {
  static Map<Object,String> labels=new IdentityHashMap<>();static List<String> visits=new ArrayList<>();
  static void hit(Object o){if(labels.containsKey(o))visits.add(labels.get(o));}
  @SuppressWarnings({"rawtypes","unchecked"}) static class Visitor extends UmlValidate.BooleanEvaluationVisitor {
    Visitor(org.eclipse.ocl.Environment env,org.eclipse.ocl.EvaluationEnvironment eval,Map extent){super(env,eval,extent);}
    @Override public Object visitIfExp(org.eclipse.ocl.expressions.IfExp e){hit(e);return super.visitIfExp(e);}
    @Override public Object visitLetExp(org.eclipse.ocl.expressions.LetExp e){hit(e);return super.visitLetExp(e);}
    @Override public Object visitVariableExp(org.eclipse.ocl.expressions.VariableExp e){hit(e);return super.visitVariableExp(e);}
    @Override public Object visitBooleanLiteralExp(org.eclipse.ocl.expressions.BooleanLiteralExp e){hit(e);return super.visitBooleanLiteralExp(e);}
    @Override public Object visitNullLiteralExp(org.eclipse.ocl.expressions.NullLiteralExp e){hit(e);return super.visitNullLiteralExp(e);}
    @Override public Object visitInvalidLiteralExp(org.eclipse.ocl.expressions.InvalidLiteralExp e){hit(e);return super.visitInvalidLiteralExp(e);}
    @Override public Object visitOperationCallExp(org.eclipse.ocl.expressions.OperationCallExp e){hit(e);return super.visitOperationCallExp(e);}
  }
  @SuppressWarnings({"rawtypes","unchecked"}) static class Factory extends UmlValidate.BooleanEnvironmentFactory {
    Factory(ResourceSet rs){super(rs);}
    @Override public org.eclipse.ocl.EvaluationVisitor createEvaluationVisitor(org.eclipse.ocl.Environment env,org.eclipse.ocl.EvaluationEnvironment eval,Map extent){return new Visitor(env,eval,extent);}
  }
  static Object ast(EObject e,String path){
    labels.put(e,path);Map<String,Object> r=UmlValidate.row("node",e.eClass().getName());
    if(e instanceof OCLExpression)r.put("type",((OCLExpression)e).getType().getName());
    else if(e instanceof org.eclipse.ocl.uml.Variable)r.put("type",((org.eclipse.ocl.uml.Variable)e).getType().getName());
    if(e instanceof org.eclipse.ocl.uml.OperationCallExp)r.put("operation",((org.eclipse.ocl.uml.OperationCallExp)e).getReferredOperation().getName());
    for(EAttribute a:e.eClass().getEAllAttributes())if(Set.of("booleanSymbol","integerSymbol","name").contains(a.getName()))r.put(a.getName(),e.eGet(a));
    for(EReference ref:e.eClass().getEAllContainments()){
      Object value=e.eGet(ref);
      if(value instanceof EObject)r.put(ref.getName(),ast((EObject)value,path+"/"+ref.getName()));
      else if(value instanceof List){List<Object> children=new ArrayList<>();int i=0;for(Object child:(List)value)if(child instanceof EObject)children.add(ast((EObject)child,path+"/"+ref.getName()+"/"+i++));if(!children.isEmpty())r.put(ref.getName(),children);}
    }
    return r;
  }
  static Map<String,Object> run(OCL ocl,OCL.Helper helper,String body,String mode){
    Map<String,Object> r=UmlValidate.row("mode",mode);labels.clear();visits.clear();
    try {
      OCLExpression e;
      if(mode.equals("original-parser"))e=helper.createQuery(body);
      else if(mode.equals("current-query")){UmlValidate.ParsedQuery q=UmlValidate.query(ocl,helper,body);e=q.expression;r.put("literal_ast_adapter",q.literalAstAdapter);r.put("conditional_ast_adapter",q.conditionalAstAdapter);r.put("conditional_type_adapter",q.conditionalTypes.report());r.put("original_parser_error",q.originalParserError);}
      else if(mode.equals("counterexample-false-condition") || mode.equals("counterexample-swapped-branches")) {
        org.eclipse.ocl.uml.IfExp changed=(org.eclipse.ocl.uml.IfExp)UmlValidate.query(ocl,helper,body).expression;
        if(mode.equals("counterexample-false-condition"))changed.setCondition(helper.createQuery("false"));
        else {OCLExpression thenBranch=(OCLExpression)changed.getThenExpression(),elseBranch=(OCLExpression)changed.getElseExpression();changed.setThenExpression(elseBranch);changed.setElseExpression(thenBranch);}
        e=changed;r.put("deliberate_test_counterexample",true);
      }
      else if(mode.startsWith("counterexample-type-")) {
        org.eclipse.ocl.uml.IfExp changed=(org.eclipse.ocl.uml.IfExp)UmlValidate.query(ocl,helper,body).expression;
        var library=ocl.getEnvironment().getOCLStandardLibrary();
        if(mode.equals("counterexample-type-invalid"))changed.setType(library.getOclInvalid());
        else if(mode.equals("counterexample-type-boolean"))changed.setType(library.getBoolean());
        else if(mode.equals("counterexample-type-void"))changed.setType(library.getOclVoid());
        else if(mode.equals("counterexample-type-unvisited"))((org.eclipse.ocl.uml.IfExp)changed.getThenExpression()).setType(library.getOclInvalid());
        else throw new IllegalArgumentException("unknown type counterexample");
        e=changed;r.put("deliberate_test_counterexample",true);
      }
      else if(mode.equals("gate-mismatch-original")) {
        org.eclipse.ocl.uml.IfExp changed=(org.eclipse.ocl.uml.IfExp)helper.createQuery(body);
        org.eclipse.ocl.uml.IfExp last=(org.eclipse.ocl.uml.IfExp)changed.getElseExpression();
        last.getElseExpression().setType(ocl.getEnvironment().getOCLStandardLibrary().getBoolean());
        r.put("ast_before_gate",ast(changed,"root"));
        r.put("conditional_type_adapter",UmlValidate.originalConditionalTypes(ocl,body,changed).report());
        e=changed;r.put("deliberate_test_counterexample",true);
      }
      else throw new IllegalArgumentException("unknown probe mode");
      r.put("parse_status","parsed");if(body.length()<=2000)r.put("ast",ast(e,"root"));else r.put("ast_summary",UmlValidate.row("node",e.eClass().getName(),"type",e.getType().getName(),"full_ast_omitted",true));
      Object value=ocl.evaluate(org.eclipse.uml2.uml.UMLFactory.eINSTANCE.createModel(),e);
      r.put("value_kind",ocl.isInvalid(value)?"invalid":value==null?"null":Boolean.TRUE.equals(value)?"true":Boolean.FALSE.equals(value)?"false":"non-boolean");r.put("evaluation_count",1);r.put("visits",new ArrayList<>(visits));
    }catch(Exception e){r.put("parse_status","failed");r.put("error",e.toString());r.put("evaluation_count",0);}
    return r;
  }
  public static void main(String[] args)throws Exception {
    ResourceSet rs=new ResourceSetImpl();rs.getPackageRegistry().put(org.eclipse.uml2.uml.UMLPackage.eNS_URI,org.eclipse.uml2.uml.UMLPackage.eINSTANCE);rs.getResourceFactoryRegistry().getExtensionToFactoryMap().put("uml",UMLResource.Factory.INSTANCE);UMLResourcesUtil.init(rs);
    Path jars=Path.of(args[0]);try(var files=Files.list(jars)){Path resource=files.filter(p->p.getFileName().toString().startsWith("org.eclipse.uml2.uml.resources_")).findFirst().orElseThrow();for(String folder:new String[]{"metamodels","profiles","libraries"})rs.getURIConverter().getURIMap().put(URI.createURI("pathmap://UML_"+folder.toUpperCase()+"/"),URI.createURI("jar:"+resource.toUri()+"!/"+folder+"/"));}
    OCL.initialize(rs);Resource resource=rs.getResource(URI.createURI(UMLResource.UML_METAMODEL_URI),true);org.eclipse.uml2.uml.Classifier context=null;for(var it=resource.getAllContents();it.hasNext();){EObject o=it.next();if(o instanceof org.eclipse.uml2.uml.Classifier && "Model".equals(((org.eclipse.uml2.uml.Classifier)o).getName()))context=(org.eclipse.uml2.uml.Classifier)o;}
    OCL ocl=OCL.newInstance(new Factory(rs));OCL.Helper helper=ocl.createOCLHelper();helper.setContext(context);List<Object> rows=new ArrayList<>();
    for(String line:Files.readAllLines(Path.of(args[1]))){String body=new String(Base64.getDecoder().decode(line),java.nio.charset.StandardCharsets.UTF_8);Map<String,Object> r=UmlValidate.row("body",body);r.put("original",run(ocl,helper,body,"original-parser"));r.put("current",run(ocl,helper,body,"current-query"));
      if(body.equals("if null then true else false endif"))r.put("counterexample",run(ocl,helper,body,"counterexample-false-condition"));
      if(body.equals("if true then true else false endif"))r.put("counterexample",run(ocl,helper,body,"counterexample-swapped-branches"));
      if(body.equals("if true then null else invalid endif"))r.put("type_counterexamples",List.of(run(ocl,helper,body,"counterexample-type-invalid"),run(ocl,helper,body,"counterexample-type-boolean")));
      if(body.equals("if true then invalid else invalid endif"))r.put("type_counterexamples",List.of(run(ocl,helper,body,"counterexample-type-void")));
      if(body.equals("if false then if null then true else true endif else true endif"))r.put("type_counterexamples",List.of(run(ocl,helper,body,"counterexample-type-unvisited")));
      if(body.equals("if false then if true then null else invalid endif else if false then invalid else null endif endif"))r.put("gate_counterexample",run(ocl,helper,body,"gate-mismatch-original"));
      rows.add(r);}
    ocl.dispose();System.out.println(UmlValidate.json(rows));
  }
}
