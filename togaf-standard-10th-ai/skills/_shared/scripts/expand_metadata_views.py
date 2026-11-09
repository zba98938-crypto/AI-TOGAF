"""Build explicit G234 repair addendum without mutating central capabilities.

Maintenance reads original text; runtime needs only bundled tables and profiles.
"""
from expand_source_capabilities import ROOT, WORK, write, table, entity, edge, example, profile
import hashlib, re, shutil

def clean(value):
    return re.sub(r'<br\s*/?>', '\n', value).replace('**', '').strip()

def solution_example():
    pid='metadata-three-part-solution';aid='metadata-repository-design'
    es=[entity('metadata-needs','visual_container','业务需求',{'definition':'由业务社区及质量、文档、安全隐私合规、治理关注共同确定','g234:slot':'requirements'}),
      entity('metadata-solution','visual_container','元数据管理IT方案',{'definition':'技术功能集、数据模型、流程三部分协同构成方案','g234:slot':'solution'})]
    rs=[]
    for rid,name,meaning in [('metadata-need-ops','社区服务运营','预约术语一致，变更后下游字典可追溯'),('metadata-need-finance','补贴财务','补贴字段与业务规则匹配，报表能回溯定义'),('metadata-need-privacy','数据保护','个人数据使用目的、保留规则、访问与变更职责明确')]:
        es.append(entity(rid,'requirement',name,{'statement':meaning,'concerns':['质量','文档化','安全／隐私／合规','治理'],'concern_mapping_basis':'虚构案例的共同关注；不是源图部门与颜色的一一对应'}));rs.append(edge('group-'+rid,'visually_contains','metadata-needs',rid,'业务需求分组'))
    for cid,name,definition,target in [('metadata-tech','1. 技术','术语目录、字典连接器与权限/版本服务','metadata-need-finance'),('metadata-data-model','2. 数据模型','术语→业务元素→数据字段及处理活动关联，标识和值域明确定义','metadata-need-ops'),('metadata-process','3. 流程与工作流','管家提交→所有者评审→发布；隐私变更由数据保护角色参与','metadata-need-privacy')]:
        es.append(entity(cid,'metadata_solution_component',name,{'definition':definition}));rs.append(edge('solution-'+cid,'visually_contains','metadata-solution',cid,'方案的并列组成，不是执行步骤'))
        rs.append(edge('supports-'+cid,'supports_metadata_requirement',cid,target,'虚构项目设计支撑，待实现验证',{'definition_origin':'fictional-project-design; not a relation asserted by source figure'}))
    rs.append(edge('solution-supports-business','g234:supports-requirements','metadata-solution','metadata-needs','三个要素共同构成的IT方案支撑业务需求',{'definition_origin':'source-structure-G234-fig4-4','scope':'whole-solution-to-whole-requirements; not three one-to-one mappings'}))
    ex=example(pid,aid,'元数据业务需求与IT方案三要素',es,rs,'原料：三个业务社区要求质量、定义与隐私可追溯。先分出需求范围和技术/模型/流程；三者共同支撑业务需求。源图只规定整体支撑，案例另列三条待验证的组成到具体需求关系。')
    ex['extensions']={'relationship_types':{'g234:supports-requirements':{'source_types':['visual_container'],'target_types':['visual_container'],'meaning':'G234图4-4整体元数据IT方案支撑业务需求范围；不是特定组件到部门的一一映射'}}}
    ex['view']['legend']='四类关注：质量（绿）、文档化（浅黄）、安全／隐私／合规（粉）、治理（青）；色块不是人员数量。+ 表示三要素共同具备，不是步骤；箭头从IT方案指向业务需求；项目设计关系另列。'
    return ex

def main():
    tables=[table('G234','表5-1'),table('G234','表5-2')]
    dst=ROOT/'reviews/source-template-bases';dst.mkdir(exist_ok=True)
    shutil.copy2(WORK/'togaf-standard-10th-zh/figs/g234e_fig5-2_en.png',dst/'G234-fig5-2-local-en.png')
    bases={
      'business':{'path':'reviews/source-template-bases/G234-fig5-1-p31-0.png','figure_id':'G234/fig5-1','pdf_page':31},
      'application':{'path':'reviews/source-template-bases/G234-fig5-2-local-en.png','figure_id':'G234/fig5-2','pdf_page':34,'original_asset':'figs/g234e_fig5-2_en.png'},
      'solution':{'path':'reviews/source-template-bases/G234-fig4-4-p25-0.png','figure_id':'G234/fig4-4','pdf_page':25}}
    for base in bases.values():
        base.update({'sha256':hashlib.sha256((ROOT/base['path']).read_bytes()).hexdigest(),'source_version':'G234e.pdf','source_pdf_sha256':'34a1c590f938bf915182fe5bbe00d1d68f9a3e948697b5500ce7c5a9494f77e7','verification_scope':'actual image opened; structural layout and readable labels compared; tiny embedded screenshots excluded'})
    write('references/source-tables/metadata-functions.json',{'notice':'完整保留参考功能；项目按需求裁剪，未选项不解释为失败。表5-2 L641八类资产与L659修改历史、来源、作者不得截断。','source_assets':bases,'tables':tables})
    profiles=[]
    for kind,t in zip(['business','application'],tables):
        pid='metadata-'+kind+'-function-map';groups={};es=[];rs=[]
        rows=[1,2,3,3,3,4,4,5,5,6] if kind=='business' else [1,2,2,3,4,1]
        slots=[str(i) for i in range(1,11)] if kind=='business' else ['acquisition','governance','reporting','reference-data','administration','integration']
        outer=kind+'-functions'
        es.append(entity(outer,'visual_container','元数据管理'+('业务' if kind=='business' else '应用')+'功能',{'definition':'G234参考功能范围；分组位置不表示执行顺序或实现状态','g234:slot':'functions'}))
        counts={}
        for row in t['rows']:
            group,name,definition=row['values'];group=group.split('（')[0].strip()
            if group not in groups:
                index=len(groups);gid=f'{kind}-group-{index+1}';groups[group]=gid
                rnum=rows[index];column=counts.get(rnum,0);counts[rnum]=column+1
                es.append(entity(gid,'function',group,{'level':1,'definition':group+'功能组；不是流程阶段','reference_row':rnum,'reference_column':column,'g234:slot':slots[index]}))
                rs.append(edge('scope-'+gid,'visually_contains',outer,gid,'参考模型范围的视觉包含；不表示组织归属'))
            fid=f'{kind}-function-{row["line"]}'
            attrs={'level':2,'definition':clean(definition),'source_row':'G234 '+t['table']+' L'+str(row['line'])}
            if kind=='application':attrs['g234:reference-order']={646:0,648:1,647:2,649:3}.get(row['line'],row['line'])
            if row['line']==641:attrs['asset_categories']=['数据术语表','数据字典','数据使用','数据分类','规则与政策','问题','治理资产','数据质量规则执行']
            es.append(entity(fid,'function',name,attrs))
            rs.append(edge('part-'+fid,'decomposes',groups[group],fid,'业务职责分解' if kind=='business' else '应用功能分解；不表示调用顺序'))
        if kind=='business':
            es.insert(0,entity('metadata-team','visual_container','元数据管理团队',{'definition':'角色协作范围，具体任命与RACI另行确定','g234:slot':'team'}))
            for i,name in enumerate(['数据所有者','数据管家','数据保管人','数据保护官']):
                rid='metadata-role-'+str(i+1);es.append(entity(rid,'role',name,{'responsibility':'按数据域参与元数据治理；具体授权待项目确认'}))
                rs.append(edge('team-'+rid,'visually_contains','metadata-team',rid,'角色属于图中的团队分组；不表示人事汇报'))
        ex=example(pid,'functional-decomposition-diagram','元数据'+('业务' if kind=='business' else '应用')+'功能参考地图',es,rs,
          '原料：社区服务预约与补贴数据需要共享术语、字典、隐私和质量文档。以G234完整功能表为评审清单保留参考结构，再按业务需求逐项决定适用性。本图是可裁剪参考模型，未声明全部已实施；定义来自源表译文，保留版本与翻译限制。')
        p=profile(pid,'functional-decomposition-diagram',ex['view']['title'],'togaf-information-data',['G234 §5.'+('1' if kind=='business' else '2'),'G234/fig5-'+('1' if kind=='business' else '2'),'references/source-tables/metadata-functions.json'],
          'metadata-map',['function','role','visual_container'],['decomposes','visually_contains'],{'function':['level','definition'],'role':['responsibility'],'visual_container':['definition']},ex,
          {'structure':kind,'source_assets':[bases[kind]],'structure_basis':'实际打开可信来源图；主图保留容器和组带，详细属性按同一稳定ID可见呈现；空间位置不增加语义关系。','reference_rows':rows})
        p['version']='2.3';p['template']['version']='2.3'
        p['checks']+=['团队四角色在参考模板同一行，团队不是功能节点','业务/应用总范围容器保持独立','分解是职责包含，不推导执行顺序','源功能定义完整，不能在句号或换行处任意截断','图5-2采集顶部、集成右侧纵向、管理底部，治理/报表/参考数据管理独立','裁剪未选项及理由在评审登记']
        profiles.append(p)
    pid='metadata-three-part-solution';aid='metadata-repository-design'
    ex=solution_example();es=ex['entities'];rs=ex['relationships']
    p=profile(pid,aid,ex['view']['title'],'togaf-information-data',['G234 §4.3','G234/fig4-4'],'metadata-map',['visual_container','requirement','metadata_solution_component'],['visually_contains','supports_metadata_requirement','g234:supports-requirements'],{'visual_container':['definition'],'requirement':['statement','concerns','concern_mapping_basis'],'metadata_solution_component':['definition']},ex,
      {'structure':'solution','source_assets':[bases['solution']],'structure_basis':'实际打开英文PDF第25页：上下两层、下层三要素与两个+号、一条整体向上支撑箭头、四类关注图例。上方部门可替换，源图未规定部门/关注点数量映射。','verification_limit':'组件内产品界面截图是说明素材，不声称逐字复刻；模板结构和完整例另验收。','concern_legend':[{'label':'质量','color':'#9dc666'},{'label':'文档化','color':'#fff3b0'},{'label':'安全／隐私／合规','color':'#edb6c0'},{'label':'治理','color':'#7acbd3'}]})
    p['version']='2.3';p['template']['version']='2.3';p['checks']+=['源图支撑关系从整个IT方案指向整个业务需求','下层三要素用+表示组合，不是流程','四类关注图例齐全且不当成人员数量','虚构项目关系与来源整体支撑关系分别展示','来源错图继续保留和登记']
    profiles.append(p)
    package={'package_id':'metadata-repair','version':'2.3','profiles':profiles,'relationship_definitions':{'g234:supports-requirements':{'source_types':['visual_container'],'target_types':['visual_container'],'meaning':'G234图4-4整体元数据IT方案支撑业务需求范围；不是特定组件到部门的一一映射'}},'source_assets':bases,'acceptance_notice':'注册不是验收；六个布局执行、目视和几何证据另存。'}
    write('capability-addenda/metadata-repair.json',package)
    print({'package':'capability-addenda/metadata-repair.json','profiles':len(profiles),'business_functions':len(tables[0]['rows']),'application_functions':len(tables[1]['rows'])})

if __name__=='__main__':main()
