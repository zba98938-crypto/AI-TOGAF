import java.util.*;
import java.io.*;
import java.nio.file.*;
import java.nio.charset.StandardCharsets;
import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.common.util.Diagnostic;
import org.eclipse.emf.ecore.*;
import org.eclipse.emf.ecore.resource.*;
import org.eclipse.emf.ecore.resource.impl.*;
import org.eclipse.emf.ecore.util.*;
import org.eclipse.emf.ecore.xmi.XMLResource;
import org.eclipse.uml2.uml.UMLPackage;
import org.eclipse.uml2.uml.resource.UMLResource;
import org.eclipse.uml2.uml.util.UMLValidator;
import org.eclipse.ocl.uml.OCL;
import org.eclipse.ocl.uml.OCLExpression;
import org.eclipse.uml2.uml.resources.util.UMLResourcesUtil;

/** Isolated mapped Eclipse model validation, not official full-language certification. */
public class UmlValidate {
  /** OCL 2.4 §11.5.4, applied only to standard-library Boolean operations.
   * Source expressions remain unchanged; model/custom operations are delegated.
   */
  @SuppressWarnings({"rawtypes","unchecked"})
  static class BooleanEvaluationVisitor extends org.eclipse.ocl.EvaluationVisitorImpl {
    BooleanEvaluationVisitor(org.eclipse.ocl.Environment env, org.eclipse.ocl.EvaluationEnvironment eval, Map extent) {
      super(env,eval,extent);
    }
    @Override public Object visitOperationCallExp(org.eclipse.ocl.expressions.OperationCallExp expr) {
      Object referred=expr.getReferredOperation();
      if(!(referred instanceof org.eclipse.uml2.uml.Operation))return super.visitOperationCallExp(expr);
      org.eclipse.uml2.uml.Operation operation=(org.eclipse.uml2.uml.Operation)referred;
      String name=operation.getName();
      if(operation.getOwner()!=getBoolean() || !Set.of("and","or","xor","implies","not").contains(name))
        return super.visitOperationCallExp(expr);
      int arity=name.equals("not")?0:1;
      if(expr.getArgument().size()!=arity)return getInvalid();
      Object left=safeVisitExpression(expr.getSource());
      if(name.equals("not")) {
        if(Boolean.TRUE.equals(left))return false;
        if(Boolean.FALSE.equals(left))return true;
        return left==null?null:getInvalid();
      }
      // Preserve the standard's dominating Boolean values and avoid evaluating
      // an unnecessary argument when the source already determines the result.
      if(name.equals("and") && Boolean.FALSE.equals(left))return false;
      if(name.equals("or") && Boolean.TRUE.equals(left))return true;
      if(name.equals("implies") && Boolean.FALSE.equals(left))return true;
      Object right=safeVisitExpression((org.eclipse.ocl.expressions.OCLExpression)expr.getArgument().get(0));
      if(name.equals("and") && Boolean.FALSE.equals(right))return false;
      if((name.equals("or") || name.equals("implies")) && Boolean.TRUE.equals(right))return true;
      if((left!=null && !(left instanceof Boolean)) || (right!=null && !(right instanceof Boolean)))return getInvalid();
      if(left==null || right==null)return null;
      if(name.equals("and"))return true;
      if(name.equals("or") || name.equals("implies"))return false;
      return !left.equals(right);
    }
  }
  @SuppressWarnings({"rawtypes","unchecked"})
  static class BooleanEnvironmentFactory extends org.eclipse.ocl.uml.UMLEnvironmentFactory {
    BooleanEnvironmentFactory(ResourceSet rs){super(rs);}
    @Override public org.eclipse.ocl.EvaluationVisitor createEvaluationVisitor(
        org.eclipse.ocl.Environment env, org.eclipse.ocl.EvaluationEnvironment eval, Map extent) {
      return new BooleanEvaluationVisitor(env,eval,extent);
    }
  }

  static String[] literalAstTokens(String body) {
    // A whole-expression token whitelist cannot match strings, properties,
    // identifiers, nested expressions or custom operations.
    String[] tokens=body.trim().split("\\s+");
    if(tokens.length==2 && tokens[0].equals("not") && Set.of("null","invalid").contains(tokens[1]))return tokens;
    if(tokens.length==3 && Set.of("null","invalid").contains(tokens[0]) &&
       Set.of("and","or","xor","implies").contains(tokens[1]) && Set.of("null","invalid").contains(tokens[2]))return tokens;
    return null;
  }
  static OCLExpression literal(OCL ocl,String token) {
    if(token.equals("null")) {
      org.eclipse.ocl.uml.NullLiteralExp literal=org.eclipse.ocl.uml.UMLFactory.eINSTANCE.createNullLiteralExp();
      literal.setType(ocl.getEnvironment().getOCLStandardLibrary().getOclVoid());return literal;
    }
    org.eclipse.ocl.uml.InvalidLiteralExp literal=org.eclipse.ocl.uml.UMLFactory.eINSTANCE.createInvalidLiteralExp();
    literal.setType(ocl.getEnvironment().getOCLStandardLibrary().getOclInvalid());return literal;
  }
  static class ParsedQuery {
    final OCLExpression expression; final boolean literalAstAdapter;
    ParsedQuery(OCLExpression expression,boolean adapted){this.expression=expression;this.literalAstAdapter=adapted;}
  }
  static class LiteralTree {
    final String token; final LiteralTree left,right;
    LiteralTree(String token,LiteralTree left,LiteralTree right){this.token=token;this.left=left;this.right=right;}
  }
  static class GroupedLiteralParser {
    final List<String> tokens; int at;
    GroupedLiteralParser(List<String> tokens){this.tokens=tokens;}
    static LiteralTree parse(String body) {
      List<String> tokens=new ArrayList<>();
      for(int at=0;at<body.length();) {
        char c=body.charAt(at);
        if(Character.isWhitespace(c)){at++;continue;}
        if(c=='(' || c==')'){tokens.add(String.valueOf(c));at++;}
        else {
          int start=at;while(at<body.length() && Character.isLetter(body.charAt(at)))at++;
          if(at==start)return null;
          String word=body.substring(start,at);
          if(!Set.of("true","false","null","invalid","not","and","or","xor","implies").contains(word))return null;
          tokens.add(word);
        }
        if(tokens.size()>2048)throw new IllegalArgumentException("grouped literal adapter token limit exceeded");
      }
      if(tokens.isEmpty())return null;
      GroupedLiteralParser parser=new GroupedLiteralParser(tokens);
      try {LiteralTree tree=parser.expression(0);return parser.at==tokens.size()?tree:null;}
      catch(IllegalArgumentException e) {
        if(e.getMessage().contains("limit exceeded"))throw e;
        return null;
      }
    }
    LiteralTree expression(int depth) {
      LiteralTree left=primary(depth);
      if(at<tokens.size() && Set.of("and","or","xor","implies").contains(tokens.get(at))) {
        String operation=tokens.get(at++);return new LiteralTree(operation,left,primary(depth));
      }
      return left;
    }
    LiteralTree primary(int depth) {
      if(depth>=64)throw new IllegalArgumentException("grouped literal adapter nesting limit exceeded");
      if(at>=tokens.size())throw new IllegalArgumentException("incomplete literal expression");
      String token=tokens.get(at++);
      if(token.equals("not"))return new LiteralTree(token,primary(depth+1),null);
      if(token.equals("(")) {
        LiteralTree inner=expression(depth+1);
        if(at>=tokens.size() || !tokens.get(at++).equals(")"))throw new IllegalArgumentException("unbalanced literal grouping");
        return inner;
      }
      if(!Set.of("true","false","null","invalid").contains(token))throw new IllegalArgumentException("literal expected");
      return new LiteralTree(token,null,null);
    }
  }
  static OCLExpression literalTree(OCL ocl,OCL.Helper helper,LiteralTree tree) throws Exception {
    if(tree.left==null)return Set.of("null","invalid").contains(tree.token)?literal(ocl,tree.token):helper.createQuery(tree.token);
    org.eclipse.ocl.uml.OperationCallExp expression=(org.eclipse.ocl.uml.OperationCallExp)helper.createQuery(
        tree.token.equals("not")?"not true":"true "+tree.token+" true");
    expression.setSource(literalTree(ocl,helper,tree.left));
    if(tree.right!=null)expression.getArgument().set(0,literalTree(ocl,helper,tree.right));
    return expression;
  }
  static ParsedQuery query(OCL ocl,OCL.Helper helper,String body) throws Exception {
    // The pinned backend cannot infer a Boolean overload for these eighteen
    // whole expressions. Instantiate that exact standard operation's typed
    // AST and literals. Normative/model source bytes never change.
    String[] tokens=literalAstTokens(body);
    if(tokens==null) {
      // Build a fallback only for the closed, explicitly grouped literal
      // grammar. General OCL, strings, identifiers and custom operations use
      // the installed parser unchanged. Conditionals are outside this scope.
      try {return new ParsedQuery(helper.createQuery(body),false);}
      catch(Exception original) {
        // Adapter limits constrain only the fallback. A source expression
        // accepted by the installed parser keeps its original semantics and
        // never enters this bounded auxiliary grammar.
        LiteralTree grouped=GroupedLiteralParser.parse(body);
        if(grouped==null)throw original;
        return new ParsedQuery(literalTree(ocl,helper,grouped),true);
      }
    }
    boolean unary=tokens.length==2;
    org.eclipse.ocl.uml.OperationCallExp expression=(org.eclipse.ocl.uml.OperationCallExp)helper.createQuery(unary?"not true":"true "+tokens[1]+" true");
    expression.setSource(literal(ocl,unary?tokens[1]:tokens[0]));
    if(!unary)expression.getArgument().set(0,literal(ocl,tokens[2]));
    return new ParsedQuery(expression,true);
  }
  static String q(String s) {
    if(s==null)return "null";
    StringBuilder b=new StringBuilder("\"");
    for(char c:s.toCharArray()) {switch(c) {case '"':b.append("\\\"");break;case '\\':b.append("\\\\");break;case '\n':b.append("\\n");break;case '\r':b.append("\\r");break;case '\t':b.append("\\t");break;default:if(c<32)b.append(String.format("\\u%04x",(int)c));else b.append(c);}}
    return b.append('"').toString();
  }
  static void diag(Diagnostic d,List<String> rows) {
    if(d.getSeverity()!=Diagnostic.OK && d.getChildren().isEmpty())rows.add("{\"severity\":"+d.getSeverity()+",\"code\":"+d.getCode()+",\"source\":"+q(d.getSource())+",\"message\":"+q(d.getMessage())+"}");
    for(Diagnostic c:d.getChildren())diag(c,rows);
  }
  public static void main(String[] args) throws Exception {
    if(args.length!=4)throw new IllegalArgumentException("mapped file, official rules TSV, pinned jar root and query adapters required");
    URI allowed=URI.createFileURI(Path.of(args[0]).toAbsolutePath().toString());
    Path jarRoot=Path.of(args[2]).toRealPath();
    ResourceSet rs=new ResourceSetImpl();
    rs.getPackageRegistry().put(UMLPackage.eNS_URI,UMLPackage.eINSTANCE);
    rs.getResourceFactoryRegistry().getExtensionToFactoryMap().put("uml",UMLResource.Factory.INSTANCE);
    UMLResourcesUtil.init(rs);
    try(var jars=Files.list(jarRoot)) {
      Path resources=jars.filter(p->p.getFileName().toString().startsWith("org.eclipse.uml2.uml.resources_")).findFirst().orElseThrow();
      for(String folder:new String[]{"libraries","metamodels","profiles"}) {
        String token="pathmap://UML_"+folder.toUpperCase()+"/";
        rs.getURIConverter().getURIMap().put(URI.createURI(token),URI.createURI("jar:"+resources.toUri()+"!/"+folder+"/"));
      }
    }
    EValidator.Registry.INSTANCE.put(UMLPackage.eINSTANCE,UMLValidator.INSTANCE);
    Map<URI,URI> resourceMaps=new HashMap<>(rs.getURIConverter().getURIMap());
    rs.setURIConverter(new ExtensibleURIConverterImpl() {
      @Override public InputStream createInputStream(URI uri,Map<?,?> options) throws IOException {
        URI resolved=normalize(uri).trimFragment();
        if(resolved.equals(allowed))return Files.newInputStream(Path.of(args[0]));
        String value=resolved.toString();
        if(value.startsWith("jar:") || value.startsWith("archive:")) {
          int boundary=value.indexOf("!/");
          if(boundary>0) {
            java.net.URI outer=java.net.URI.create(value.substring(value.indexOf(':')+1,boundary));
            if("file".equals(outer.getScheme())) {
              Path archive=Path.of(outer).toRealPath();
              if(archive.getParent().equals(jarRoot) && archive.getFileName().toString().endsWith(".jar"))return super.createInputStream(resolved,options);
            }
          }
        }
        throw new IOException("external resource access prohibited: "+uri+" (resolved "+resolved+")");
      }
      @Override public OutputStream createOutputStream(URI uri,Map<?,?> options) throws IOException {throw new IOException("resource writes prohibited");}
    });
    rs.getURIConverter().getURIMap().putAll(resourceMaps);
    Resource r=rs.createResource(allowed);
    r.load(Map.of(XMLResource.OPTION_DEFER_IDREF_RESOLUTION,true,XMLResource.OPTION_DISABLE_NOTIFY,true));
    List<EObject> objects=new ArrayList<>();objects.addAll(r.getContents());
    for(EObject root:r.getContents())for(var it=root.eAllContents();it.hasNext();)objects.add(it.next());
    List<String> diagnostics=new ArrayList<>(),inventory=new ArrayList<>(),rules=new ArrayList<>();
    for(Resource.Diagnostic d:r.getErrors())diagnostics.add("{\"severity\":4,\"code\":0,\"source\":\"resource\",\"message\":"+q(d.getMessage())+"}");
    for(Resource.Diagnostic d:r.getWarnings())diagnostics.add("{\"severity\":2,\"code\":0,\"source\":\"resource\",\"message\":"+q(d.getMessage())+"}");
    for(EObject root:r.getContents())diag(Diagnostician.INSTANCE.validate(root),diagnostics);
    for(EObject o:objects)inventory.add("{\"id\":"+q(((XMLResource)r).getID(o))+",\"class\":"+q(o.eClass().getName())+"}");
    OCL.initialize(rs);
    Resource metamodelResource=rs.getResource(URI.createURI(UMLResource.UML_METAMODEL_URI),true);
    Map<String,org.eclipse.uml2.uml.Classifier> contexts=new HashMap<>();
    for(var it=metamodelResource.getAllContents();it.hasNext();) {
      EObject item=it.next();
      if(item instanceof org.eclipse.uml2.uml.Classifier)contexts.put(((org.eclipse.uml2.uml.Classifier)item).getName(),(org.eclipse.uml2.uml.Classifier)item);
    }
    OCL ocl=OCL.newInstance(new BooleanEnvironmentFactory(rs));int parseOK=0,parseFailed=0,evalCount=0;
    org.eclipse.ocl.Environment.Registry.INSTANCE.registerEnvironment(ocl.getEnvironment());
    List<String> queryAdapters=new ArrayList<>();
    for(String line:Files.readAllLines(Path.of(args[3]))) {
      String[] cols=line.split("\\t",-1);if(cols.length!=3)throw new IllegalArgumentException("invalid query adapter record");
      String context=new String(Base64.getDecoder().decode(cols[0]),StandardCharsets.UTF_8);
      String id=new String(Base64.getDecoder().decode(cols[1]),StandardCharsets.UTF_8);
      String definition=new String(Base64.getDecoder().decode(cols[2]),StandardCharsets.UTF_8);
      try {OCL.Helper helper=ocl.createOCLHelper();helper.setContext(contexts.get(context));helper.defineOperation(definition);queryAdapters.add("{\"id\":"+q(id)+",\"status\":\"defined\"}");}
      catch(Exception e){queryAdapters.add("{\"id\":"+q(id)+",\"status\":\"blocked\",\"reason\":"+q(e.toString())+"}");}
    }
    try {
      for(String line:Files.readAllLines(Path.of(args[1]))) {
        String[] cols=line.split("\\t",-1);if(cols.length!=3)continue;
        String context=new String(Base64.getDecoder().decode(cols[0]),StandardCharsets.UTF_8);
        String id=new String(Base64.getDecoder().decode(cols[1]),StandardCharsets.UTF_8);
        String body=new String(Base64.getDecoder().decode(cols[2]),StandardCharsets.UTF_8);
        EClassifier type=UMLPackage.eINSTANCE.getEClassifier(context);
        String error=null;boolean literalAdapted=false;int applicable=0,violations=0,invalid=0,nulls=0,nonBoolean=0,truths=0;
        List<String> violationIDs=new ArrayList<>(),invalidIDs=new ArrayList<>(),nullIDs=new ArrayList<>(),nonBooleanIDs=new ArrayList<>(),outcomes=new ArrayList<>();
        try {
          if(!(type instanceof EClass))throw new IllegalArgumentException("context classifier not mapped");
          org.eclipse.uml2.uml.Classifier contextType=contexts.get(context);
          if(contextType==null)throw new IllegalArgumentException("UML semantic context not mapped");
          OCL.Helper helper=ocl.createOCLHelper();helper.setContext(contextType);ParsedQuery parsed=query(ocl,helper,body);
          OCLExpression expr=parsed.expression;literalAdapted=parsed.literalAstAdapter;parseOK++;
          for(EObject o:objects)if(((EClass)type).isSuperTypeOf(o.eClass())) {
            applicable++;evalCount++;
            String objectID=q(((XMLResource)r).getID(o));String valueKind;
            try {
              Object value=ocl.evaluate(o,expr);
              // OCL invalid is a backend sentinel, whereas OclVoid/null is Java
              // null. Neither is the Boolean false constraint violation.
              if(ocl.isInvalid(value)){invalid++;invalidIDs.add(objectID);valueKind="invalid";}
              else if(value==null){nulls++;nullIDs.add(objectID);valueKind="null";}
              else if(Boolean.FALSE.equals(value)){violations++;violationIDs.add(objectID);valueKind="false";}
              else if(Boolean.TRUE.equals(value)){truths++;valueKind="true";}
              else {nonBoolean++;nonBooleanIDs.add(objectID);valueKind="non-boolean";}
            }
            catch(Exception e){invalid++;invalidIDs.add(objectID);valueKind="invalid";}
            outcomes.add("{\"id\":"+objectID+",\"value_kind\":"+q(valueKind)+"}");
          }
        } catch(Exception e){parseFailed++;error=e.getClass().getSimpleName()+": "+e.getMessage();}
        rules.add("{\"id\":"+q(id)+",\"context\":"+q(context)+",\"literal_ast_adapter\":"+literalAdapted+",\"parse_status\":"+q(error==null?"parsed":"unmapped-or-parse-failed")+",\"parse_error\":"+q(error)+",\"applicable\":"+applicable+",\"true_evaluations\":"+truths+",\"violations\":"+violations+",\"invalid_evaluations\":"+invalid+",\"null_evaluations\":"+nulls+",\"non_boolean_evaluations\":"+nonBoolean+",\"violation_ids\":["+String.join(",",violationIDs)+"],\"invalid_ids\":["+String.join(",",invalidIDs)+"],\"null_ids\":["+String.join(",",nullIDs)+"],\"non_boolean_ids\":["+String.join(",",nonBooleanIDs)+"],\"evaluation_outcomes\":["+String.join(",",outcomes)+"]}");
      }
    } finally {org.eclipse.ocl.Environment.Registry.INSTANCE.deregisterEnvironment(ocl.getEnvironment());ocl.dispose();}
    System.out.println("{\"backend\":\"Eclipse UML2 + EMF Diagnostician + UML OCL\",\"java_version\":"+q(System.getProperty("java.version"))+",\"loaded_objects\":"+objects.size()+",\"inventory\":["+String.join(",",inventory)+"],\"diagnostics\":["+String.join(",",diagnostics)+"],\"query_adapter_results\":["+String.join(",",queryAdapters)+"],\"ocl_rules\":["+String.join(",",rules)+"],\"ocl_parsed\":"+parseOK+",\"ocl_unmapped\":"+parseFailed+",\"ocl_evaluations\":"+evalCount+",\"official_full_conformance\":false}");
  }
}
