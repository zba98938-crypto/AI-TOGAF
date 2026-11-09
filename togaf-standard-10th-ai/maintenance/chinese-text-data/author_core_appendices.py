# -*- coding: utf-8 -*-
from pathlib import Path
import json,re
from bs4 import BeautifulSoup
C=Path(__file__).resolve().parents[2];d=json.loads((C/'fundamental/web-2025/volumes/01-introduction-and-core-concepts/document.json').read_text());p=Path(__file__).parent/'partial/01-introduction-and-core-concepts.txt';s=p.read_text()
titles='''应用软件
可用性
业务系统
目录
客户端
COBIT
配置管理
CxO
数据字典
数据元素
数据库
数据库管理系统
最终用户
企业资源规划ERP系统
硬件
信息域
信息系统IS
交互
交互模型
接口
关键绩效指标KPI
生命周期
成功项目群管理MSP
矩阵
元视图
开放系统
运营治理
套装服务
可迁移性
组合
PRINCE2
项目群
项目
风险管理
可伸缩性
安全
服务器
服务质量
SMART
供应商管理
系统
时间段
用例
用户'''.splitlines()
for b in d['blocks']:
 if b['kind']=='h3' and b['text_en'].startswith('B.'):
  n=int(b['text_en'].split('.')[1]);s+='@@ '+b['id'].split(':')[-1]+'\nB.'+str(n)+'. '+titles[n-1]+'\n'
zh='''架构构建块
架构能力成熟度模型
架构开发方法
美国国家标准学会
应用平台接口
零售技术标准协会
业务动机模型
业务流程管理
业务流程模型与记法
加拿大政府业务转型使能项目
能力成熟度模型
能力成熟度模型集成
信息及相关技术控制目标
商用现成应用
客户关系管理
创建/读取/更新/删除
关键成功因素
数据库管理员
数据库管理系统
美国商务部
美国国防部
国防部架构框架
企业应用集成
联合国行政、商业和运输电子数据交换
企业资源规划
抽取、转换、加载
Fair Isaac公司
全职当量
政府现成应用
健康保险可携带性与责任法案
集成计算机辅助制造
输入、控制、输出及机制/资源
集成计算机辅助制造定义
国际电工委员会
电气电子工程师学会
集成信息基础设施参考模型
物联网
信息系统审计与控制协会
信息系统审计与控制基金会
国际标准组织
信息技术
IT治理研究所
信息技术基础设施库
IT组合管理设施
Java 2企业版平台
关键绩效指标
局域网
模型驱动架构
微服务架构
成功项目群管理
最小可行架构
北约架构框架
美国各州首席信息官协会
经济合作与发展组织
英国政府商务办公室
运营水平协议
管理与预算办公室
对象管理组织
对象请求代理
开放系统互连
开放面向服务架构
便携文档格式
项目管理知识体系
受控环境中的项目
服务质量
远程访问服务
变更请求
信息请求
建议书请求
参考模型
解决方案构建块
服务组件架构
服务数据对象
软件工程研究所
标准通用标记语言
服务水平协议
具体、可度量、可行动、现实、有时限
面向服务架构
软件过程工程元模型
系统建模语言
信息管理技术架构框架
技术参考模型
统一建模语言
广域网
可扩展标记语言'''.splitlines()
b=next(b for b in d['blocks'] if b['id'].endswith('b00704'));soup=BeautifulSoup(b['html'],'html.parser');dts=soup.find_all('dt');dds=soup.find_all('dd');assert len(dts)==len(dds)==len(zh),(len(dts),len(dds),len(zh))
s+='@@ b00704\n|缩略语|中文释义|英文原释义（保留来源用词）|\n|---|---|---|\n'+'\n'.join('|'+t.get_text(' ',strip=True)+'|'+z+'|'+' '.join(v.stripped_strings).replace('\r','').replace('\n',' ')+'|' for t,v,z in zip(dts,dds,zh))+'\n'
# Sort and enforce one translation per source block.
a=re.split(r'^@@ (b\d+)\n',s,flags=re.M);rows={}
for i in range(1,len(a),2):assert a[i] not in rows;rows[a[i]]=a[i+1].strip()
p.write_text(''.join('@@ '+k+'\n'+v+'\n' for k,v in sorted(rows.items())));p.rename(p.parent.parent/p.name)
p.with_suffix('.scope.json').rename(p.parent.parent/'scope-history/01-first-three-selected-chapters.scope.json')
