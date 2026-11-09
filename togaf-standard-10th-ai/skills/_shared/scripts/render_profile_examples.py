"""Generate fictional renderer exercises in both layouts; no source-parity claim."""
import argparse
import base64
import json
import subprocess
from pathlib import Path
from profile_render import render_profile

ROOT=Path(__file__).resolve().parents[1]

def examples():
    def e(i,t="capability",**a):return {"id":i,"name":"示例"+i,"type":t,"attributes":a,"evidence":["example"],"certainty":"assumed"}
    def r(i,s,t,k="decomposes",**a):return {"id":i,"source":s,"target":t,"type":k,"label":i,"attributes":a,"evidence":["example"],"certainty":"assumed"}
    yield "nested-map",[e("战略管理",category="战略能力",level=1),e("规划管理",level=2),e("客户运营",category="核心能力",level=1)],[r("战略分解","战略管理","规划管理")],{}
    yield "heatmap",[e("客户管理",category="核心能力",score=1),e("履约管理",category="核心能力",score=3),e("新服务",category="核心能力",existence="future-absent")],[],{"colors":{"1":"#f2b9b2","2":"#ffe5a8","3":"#b8dbbe"},"score_field":"score"}
    es=[e("确认购买","value_stage",ordinal=1,entry="客户选择商品",exit="购买承诺确认",value_item="可靠承诺"),e("获得商品","value_stage",ordinal=2,value_item="可使用商品"),e("订单能力实例","capability_instance",stage_id="确认购买",capability_id="订单能力"),e("订单应用","application",instance_id="订单能力实例"),e("客户信息","information",instance_id="订单能力实例"),e("订单能力")]
    rs=[r("阶段顺序","确认购买","获得商品","precedes"),r("阶段使能","确认购买","订单能力实例","enabled_by"),r("实例应用组成","订单能力实例","订单应用","contains"),r("实例信息组成","订单能力实例","客户信息","contains"),r("实例属于类型","订单能力实例","订单能力","instance_of")]
    yield "stage-map",es,rs,{}
    yield "network",[e("销售团队","organization",boundary="内部"),e("物流伙伴","organization",boundary="外部"),e("客户信息","information")],[r("协作履约","销售团队","物流伙伴","collaborates_with"),r("使用客户信息","销售团队","客户信息","uses_information")],{}
    blocks=["伙伴","活动","资源","价值","关系","渠道","客户","成本","收入"]
    yield "canvas",[e(b,"business_model_element",block=b,detail="此区块的虚构业务内容，实际项目需验证") for b in blocks],[],{}
    yield "value-chain",[e("采购","value_chain_activity",category="主要活动"),e("生产运营","value_chain_activity",category="主要活动"),e("配送服务","value_chain_activity",category="主要活动"),e("人员管理","value_chain_activity",category="支持活动"),e("技术开发","value_chain_activity",category="支持活动")],[r("技术支撑","技术开发","生产运营","supports_activity")],{}
    er=r("共同持有","客户","账户","data_association");er["cardinality"]={"source":{"min":1,"max":2},"target":{"min":1,"max":"*"}}
    yield "er",[e("客户","logical_entity",attributes=[{"name":"客户标识","required":True}],key="客户标识"),e("账户","logical_entity",attributes=[{"name":"账户标识","required":True}],key="账户标识")],[er],{}
    yield "sequence",[e("业务流程","process"),e("订单应用","application"),e("订单数据","data_entity")],[r("提交订单","业务流程","订单应用","processing_step",order=1),r("创建订单","订单应用","订单数据","accesses",order=2)],{}
    yield "state",[e("活动","data_state",retention="业务处理中",initial=True),e("归档","data_state",retention="依政策保留"),e("销毁","data_state",retention="到期无保留义务",final=True)],[r("交易结束归档","活动","归档","transitions_to",trigger="交易结束",guard="无未决争议"),r("保留期限届满销毁","归档","销毁","transitions_to",trigger="保留期届满")],{}
    yield "deployment",[e("业务安全域","trust_zone",classification="受限"),e("目标应用","application",version="候选1.0"),e("应用节点","technology",responsibility="应用运行")],[r("安全域归属","目标应用","业务安全域","within_boundary"),r("部署运行","目标应用","应用节点","runs_on")],{}
    yield "roadmap",[e("数据准备","work_package",start="2027-01-01",end="2027-01-08"),e("双运行试点","work_package",start="2027-01-09",end="2027-01-20",rollback="切回旧入口"),e("正式迁移","work_package",start="2027-01-21",end="2027-01-25")],[r("准备前置","双运行试点","数据准备","depends_on"),r("试点前置","正式迁移","双运行试点","depends_on")],{}
    yield "matrix",[e("应用A","application"),e("应用B","application"),e("客户","data_entity"),e("订单","data_entity")],[r("A读客户","应用A","客户","accesses"),r("B维护订单","应用B","订单","accesses")],{"row_types":["application"],"column_types":["data_entity"]}
    yield "causal",[e("数字使用","variable"),e("基础设施","variable"),e("数字成本","variable")],[r("使用增加资源","数字使用","基础设施","causes",polarity="+"),r("资源支撑使用","基础设施","数字使用","causes",polarity="+"),r("资源增加成本","基础设施","数字成本","causes",polarity="+"),r("成本限制资源","数字成本","基础设施","causes",polarity="-")],{"loops":[{"id":"R1","type":"reinforcing","relationship_ids":["使用增加资源","资源支撑使用"]},{"id":"B1","type":"balancing","relationship_ids":["资源增加成本","成本限制资源"]}]}
    yield "quadrant",[e("组织文化","culture_axis",quadrant="top-left"),e("技能教育","culture_axis",quadrant="top-right"),e("沟通","culture_axis",quadrant="bottom-left"),e("节俭创新","culture_axis",quadrant="bottom-right")],[],{}
    yield "assessment",[e("架构流程","assessment_factor",score=3,scale="0—5",evidence="虚构访谈"),e("架构治理","assessment_factor",score=2,scale="0—5",evidence="虚构治理记录")],[],{}
    yield "catalog",[e("需求A","requirement",statement="示例需求",owner="业务负责人",acceptance="给定输入下验证结果")],[],{}
    yield "four-box",[e(n,"business_model_component",component=n,detail="虚构区块内容") for n in ["客户价值主张","利润公式","关键资源","关键流程"]],[r("资源支撑主张","关键资源","客户价值主张","traces_to")],{}
    yield "cube",[e(n,"business_model_dimension",dimension=n,detail="虚构维度内容") for n in ["价值主张","客户","网络伙伴","活动","胜任力","价值公式"]],[r("伙伴参与活动","网络伙伴","活动","traces_to")],{}
    yield "perspectives",[e("提升留存","goal",perspective="客户"),e("复购率提高","outcome",perspective="客户",metric="复购客户占比",unit="%"),e("提高效率","goal",perspective="内部流程"),e("确认时长下降","outcome",perspective="内部流程",metric="平均确认时长",unit="分钟")],[r("复购实现留存","复购率提高","提升留存","realizes"),r("时长实现效率","确认时长下降","提高效率","realizes")],{}
    lean=[e(n,"lean_process",function="虚构职能",lead_time=lt,processing_time=pt,complete_accurate=ca,unit="分钟",queue=q) for n,lt,pt,ca,q in [("核对",480,10,0.9,2),("拣配",960,30,0.95,12),("发运",480,15,0.99,4)]]
    yield "lean-flow",[e("客户","actor"),e("订单应用","application")]+lean,[r("下单","客户","订单应用","information_flow"),r("派单","订单应用","核对","information_flow"),r("推送1","核对","拣配","work_flow"),r("推送2","拣配","发运","work_flow"),r("通知","发运","客户","information_flow")],{}
    yield "swimlane",[e("客服","role"),e("仓库","role"),e("收到订单","event"),e("核对订单","activity"),e("库存充足","decision"),e("拣配","activity")],[r("客服执行核对","客服","核对订单","assigned_to"),r("仓库执行拣配","仓库","拣配","assigned_to"),r("仓库判断库存","仓库","库存充足","assigned_to"),r("订单触发","收到订单","核对订单","triggers"),r("核对后判断","核对订单","库存充足","flows_to"),r("充足则拣配","库存充足","拣配","branches"),r("不足则重核","库存充足","核对订单","branches")],{}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--out",required=True);p.add_argument("--render",action="store_true");args=p.parse_args()
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True);results=[];jobs=[];svgs=[]
    for renderer,es,rs,template in examples():
        for layout in ["reference","adaptive"]:
            identity=renderer+"-"+layout
            v={"id":identity,"title":"虚构渲染验收："+renderer,"entity_ids":[e["id"] for e in es],"relationship_ids":[r["id"] for r in rs],"legend":"候选示例；关系方向与文字明确；来源等价另验收","_is_example":True}
            model={"entities":es,"relationships":rs};profile={"id":renderer+"-exercise","renderer":renderer,"template":template,"definition_status":"project-renderer-exercise"}
            svg,report=render_profile(model,v,profile,layout);svgs.append((identity,svg));(out/(identity+".coverage.json")).write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
            jobs.append({"id":identity,"kind":"svg","source":identity+".svg","svg":identity+".svg","png":identity+".png"});results.append({"id":identity,"renderer":renderer,"layout":layout,"errors":report["errors"],"missing_entities":report["unrepresented_entity_ids"],"missing_relationships":report["unrepresented_relationship_ids"]})
    from generate import subset_font
    font=subset_font("".join(svg for _,svg in svgs),out/"font-subset.ttf")
    for identity,svg in svgs:
        svg=svg.replace(">",'><defs><style>@font-face{font-family:TogafCJK;src:url(data:font/ttf;base64,'+font+")}</style></defs>",1);(out/(identity+".svg")).write_text(svg)
    (out/"render-jobs.json").write_text(json.dumps({"font":"font-subset.ttf","jobs":jobs},ensure_ascii=False,indent=2)+"\n")
    if args.render:subprocess.run(["node",str(ROOT/"scripts/render.mjs"),str((out/"render-jobs.json").resolve())],check=True)
    (out/"exercise-report.json").write_text(json.dumps({"notice":"虚构渲染器练习，不代表完整 TOGAF 对标通过。","results":results},ensure_ascii=False,indent=2)+"\n")
    text="# 专用渲染器双布局示例\n\n这些图是虚构的渲染行为练习，验证构图和输出机制；不能作为来源图等价证明。\n\n| 模板族 | 来源结构布局 | 业务适配布局 |\n| --- | --- | --- |\n"
    for renderer,_,_,_ in examples():
        text+="| "+renderer+" | [SVG]("+renderer+"-reference.svg) / [PNG]("+renderer+"-reference.png) | [SVG]("+renderer+"-adaptive.svg) / [PNG]("+renderer+"-adaptive.png) |\n"
    text+="\n每图的 .coverage.json 记录对象、关系、属性的表达和缺口。reference 的来源核实状态保持未验证，不由生成操作改变。\n"
    (out/"index.md").write_text(text)
    print(json.dumps({"views":len(results),"errors":sum(len(r["errors"]) for r in results),"rendered":args.render},ensure_ascii=False))
if __name__=="__main__":main()
