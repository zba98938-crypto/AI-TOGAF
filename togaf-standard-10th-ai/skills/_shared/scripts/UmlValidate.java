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
    OCL ocl=OCL.newInstance(rs);int parseOK=0,parseFailed=0,evalCount=0;
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
        String error=null;int applicable=0,violations=0,invalid=0;List<String> violationIDs=new ArrayList<>(),invalidIDs=new ArrayList<>();
        try {
          if(!(type instanceof EClass))throw new IllegalArgumentException("context classifier not mapped");
          org.eclipse.uml2.uml.Classifier contextType=contexts.get(context);
          if(contextType==null)throw new IllegalArgumentException("UML semantic context not mapped");
          OCL.Helper helper=ocl.createOCLHelper();helper.setContext(contextType);OCLExpression expr=helper.createQuery(body);parseOK++;
          for(EObject o:objects)if(((EClass)type).isSuperTypeOf(o.eClass())) {
            applicable++;evalCount++;
            try {Object value=ocl.evaluate(o,expr);if(Boolean.FALSE.equals(value)){violations++;violationIDs.add(q(((XMLResource)r).getID(o)));}else if(!Boolean.TRUE.equals(value)){invalid++;invalidIDs.add(q(((XMLResource)r).getID(o)));}}
            catch(Exception e){invalid++;invalidIDs.add(q(((XMLResource)r).getID(o)));}
          }
        } catch(Exception e){parseFailed++;error=e.getClass().getSimpleName()+": "+e.getMessage();}
        rules.add("{\"id\":"+q(id)+",\"context\":"+q(context)+",\"parse_status\":"+q(error==null?"parsed":"unmapped-or-parse-failed")+",\"parse_error\":"+q(error)+",\"applicable\":"+applicable+",\"violations\":"+violations+",\"invalid_evaluations\":"+invalid+",\"violation_ids\":["+String.join(",",violationIDs)+"],\"invalid_ids\":["+String.join(",",invalidIDs)+"]}");
      }
    } finally {org.eclipse.ocl.Environment.Registry.INSTANCE.deregisterEnvironment(ocl.getEnvironment());ocl.dispose();}
    System.out.println("{\"backend\":\"Eclipse UML2 + EMF Diagnostician + UML OCL\",\"java_version\":"+q(System.getProperty("java.version"))+",\"loaded_objects\":"+objects.size()+",\"inventory\":["+String.join(",",inventory)+"],\"diagnostics\":["+String.join(",",diagnostics)+"],\"query_adapter_results\":["+String.join(",",queryAdapters)+"],\"ocl_rules\":["+String.join(",",rules)+"],\"ocl_parsed\":"+parseOK+",\"ocl_unmapped\":"+parseFailed+",\"ocl_evaluations\":"+evalCount+",\"official_full_conformance\":false}");
  }
}
