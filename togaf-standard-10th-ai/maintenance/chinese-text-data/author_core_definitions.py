# -*- coding: utf-8 -*-
from pathlib import Path
import json,re
from bs4 import BeautifulSoup
C=Path(__file__).resolve().parents[2];d=json.loads((C/'fundamental/web-2025/volumes/01-introduction-and-core-concepts/document.json').read_text());p=Path(__file__).parent/'partial/01-introduction-and-core-concepts.txt'
s=p.read_text();existing=set(re.findall(r'^@@ (b\d+)',s,re.M))
titles='''抽象
参与者
应用架构
应用组件
应用平台
应用服务
架构风格
架构
架构构建块ABB
架构连续系列
架构开发方法ADM
架构域
架构框架
架构治理
架构全景
架构层级
架构模型
架构分区
架构原则
架构视图
架构视点
架构愿景
制品
基线
无边界信息流
构建块
业务架构
业务能力
业务职能
业务治理
业务模型
业务服务
能力
能力架构
能力增量
沟通与利益相关者管理
关注点
行动方案
数据架构
交付物
数字架构
EA全景
企业
企业架构服务
企业连续系列
基础架构
框架
差距
治理
信息
信息技术IT
互操作性
逻辑
元数据
元模型
方法
建模
模型种类
具体目标
模式
物理
原则
产品
参考模型RM
需求
路线图
角色
分段架构
服务
服务导向
面向服务架构SOA
服务组合
解决方案架构
解决方案构建块SBB
解决方案连续系列
利益相关者
标准库
战略架构
目标架构
架构视图分类体系
技术架构
技术组件
技术服务
过渡架构
价值流
视图
视点
视点库
工作包'''.splitlines()
for b in d['blocks']:
 if b['kind']=='h3' and b['text_en'].startswith('4.'):
  num=int(b['text_en'].split('.')[1]);k=b['id'].split(':')[-1]
  if k not in existing:s+='@@ '+k+'\n4.'+str(num)+'. '+titles[num-1]+'\n'
refs={601:'''使用敏捷Sprint应用ADM
遵循ADM开发EA的实践者方法
构建块选择方法
架构成熟度模型
架构项目管理
架构角色与技能
架构技能框架
业务能力（第2版）
业务能力规划
业务模型
业务场景
数字技术采用：准备度评估与路线图
使能企业敏捷性
环境可持续信息系统
信息架构：商业智能与分析
信息架构：客户主数据管理
信息架构：元数据管理
信息映射
在TOGAF EA中集成风险与安全
组织映射
集成信息基础设施参考模型III-RM
建立演进EA能力的领导者指南
技术参考模型TRM
定义和治理面向服务架构
价值流'''.splitlines(),603:'''以TOGAF整合应用组合的实践方法
Archi Banking：结合BIAN、ArchiMate与TOGAF
ArchiMate 3.2规范
数字实践者知识体系DPBoK
TOGAF与Frameworx协同
BI与分析及元数据管理参考模型
开放风险分析O-RA 2.0.1
开放风险分类法O-RT 3.0.1
开放敏捷架构
IT4IT 3.0.1
TOGAF 9与DoDAF 2.0
TOGAF与SABSA集成
架构合规评审检查清单'''.splitlines(),605:'''项目管理知识体系PMBOK指南
识别流程复用机会以增强运营模型的方法
分析模式：可复用对象模型
软件密集系统架构描述推荐实践
模式语言：城镇、建筑、建造
业务动机模型BMM
业务流程模型与记法BPMN
业务转型使能项目BTEP
信息及相关技术控制目标COBIT 4.0
公司治理
设计模式：可复用面向对象软件的要素
作为战略的企业架构
企业架构能力成熟度模型ACMM 1.2
企业架构成熟度模型1.3
企业架构规划：数据、应用和技术蓝图
美国空军总部信息管理原则
信息技术：服务管理
系统生命周期流程
架构描述
IT组合管理设施ITPMF
敏捷软件开发宣言
韦氏大学词典第11版
模型驱动架构MDA
OECD公司治理原则
组织图：描绘公司的实际运作
面向模式的软件架构：模式系统
模式与软件：基本概念及术语
可复用资产规格RAS 2.2
服务组件架构SCA
服务数据对象SDO
软件过程工程元模型SPEM 2.0
系统建模语言SysML
系统架构的艺术
俄勒冈实验
永恒的建造之道
Zachman框架
服务UML Profile及元模型征求建议书
统一建模语言UML'''.splitlines()}
for n,zh in refs.items():
 b=next(b for b in d['blocks'] if b['id'].endswith('b%05d'%n));lis=BeautifulSoup(b['html'],'html.parser').find_all('li',recursive=True);assert len(lis)==len(zh),(n,len(lis),len(zh));s+='@@ b%05d\n'%n+'\n'.join('- '+z+'。书目信息与版本原样保留：'+' '.join(li.stripped_strings).replace('\r','').replace('\n',' ') for z,li in zip(zh,lis))+'\n'
p.write_text(s)
