#coding:utf-8
from  sql_con import db
import json
from flask import Response,request
from flask_sqlalchemy import SQLAlchemy
class stu_info(db.Model):
	'''Flask-SQLAlchemy这个框架SQLAlchemy 的操作，而SQLAlchemy 是一个很强大的关系型数据库框架

	'''
	__tablename__='stu_info'
	stu_id = db.Column(db.Integer, primary_key=True)
	stu_name=db.Column(db.VARCHAR(8),nullable=False)
	stu_cardID=db.Column(db.CHAR(10),nullable=True)
	stu_sex=db.Column(db.VARCHAR(2),nullable=False)
	stu_birthday=db.Column(db.DATE,nullable=False)
	stu_nation=db.Column(db.VARCHAR(5),nullable=False)
	stu_adress=db.Column(db.VARCHAR(50),nullable=False)
	stu_zzmm=db.Column(db.CHAR(18),nullable=True)
	stu_qq=db.Column(db.CHAR(11),nullable=True)
	stu_email=db.Column(db.CHAR(25),nullable=True)
	stu_yzbm=db.Column(db.CHAR(6),nullable=True)
	stu_ksh=db.Column(db.CHAR(10),nullable=True)
	stu_rxsj=db.Column(db.DATE,nullable=True)
	stu_rxfs=db.Column(db.CHAR(10),nullable=True)
	stu_xxxs=db.Column(db.CHAR(10),nullable=True)
	stu_pylx=db.Column(db.CHAR(12),nullable=True)
	stu_pydx=db.Column(db.CHAR(4),nullable=True)
	stu_pycc=db.Column(db.CHAR(4),nullable=True)
	stu_bxlx=db.Column(db.CHAR(12),nullable=True)
	stu_bxxx=db.Column(db.CHAR(8),nullable=True)
	stu_img=db.Column(db.VARCHAR(200),nullable=True)
	stu_tel=db.Column(db.CHAR(11),nullable=False)
	stu_dept=db.Column(db.VARCHAR(30),nullable=False)
	stu_profession=db.Column(db.VARCHAR(30),nullable=False)
	stu_class=db.Column(db.Integer,nullable=False)
	stu_start_date=db.Column(db.DATE,nullable=False)
	stu_native=db.Column(db.VARCHAR(20),nullable=False)
	stu_record=db.Column(db.VARCHAR(3),nullable=False)
	# def __init__(self,stu_id=None,stu_name=None,stu_cardID=None,stu_sex=None,stu_birthday=None,stu_nation=None,
	#              stu_zzmm=None,stu_qq=None,stu_email=None,stu_yzbm=None,stu_ksh=None,stu_rxsj=None,stu_rxfs=None,
	#              stu_xxxs=None,stu_adress=None,stu_pylx=None,stu_pydx=None,stu_pycc=None,stu_bxlx=None,stu_bxxx=None,stu_img=None,
	#              stu_tel=None,stu_dept=None,stu_profession=None,stu_class=None,stu_start_date=None,stu_native=None,
	#              stu_record=None):
	# 	self.stu_id=stu_id
	# 	self.stu_name=stu_name
	# 	self.stu_adress=stu_adress
	# 	self.stu_cardID=stu_cardID
	# 	self.stu_sex=stu_sex
	# 	self.stu_birthday=stu_birthday
	# 	self.stu_nation=stu_nation
	# 	self.stu_zzmm=stu_zzmm
	# 	self.stu_qq=stu_qq
	# 	self.stu_email=stu_email
	# 	self.stu_yzbm=stu_yzbm
	# 	self.stu_ksh=stu_ksh
	# 	self.stu_rxsj=stu_rxsj
	# 	self.stu_rxfs=stu_rxfs
	# 	self.stu_xxxs=stu_xxxs
	# 	self.stu_pylx=stu_pylx
	# 	self.stu_pydx=stu_pydx
	# 	self.stu_pycc=stu_pycc
	# 	self.stu_bxlx=stu_bxlx
	# 	self.stu_bxlx=stu_bxlx
	# 	self.stu_bxxx=stu_bxxx
	# 	self.stu_img=stu_img
	# 	self.stu_tel=stu_tel
	# 	self.stu_dept=stu_dept
	# 	self.stu_profession=stu_profession
	# 	self.stu_class = stu_class
	# 	self.stu_start_date = stu_start_date
	# 	self.stu_native = stu_native
	# 	self.stu_record = stu_record


	def creat_table(self):
		db.create_all()
		print u'stu_info表创建成功'
	def delete_table(self):
		'''慎用！！！！会将表和数据一块删除'''
		db.drop_all()
		print u'stu_info表已删除'

def query_by_stu_id(stu_id):
	query = stu_info.query.filter_by(stu_id=stu_id).first()
	dict={}
	dict['stu_id']=stu_id
	dict['stu_name'] = query.stu_name
	dict['stu_cardID'] = query.stu_cardID
	dict['stu_sex'] = query.stu_sex
	dict['stu_adress']=query.stu_adress
	dict['stu_birthday'] = str(query.stu_birthday)#datetime.date类型不能转json
	dict['stu_nation'] = query.stu_nation
	dict['stu_zzmm'] = query.stu_zzmm
	dict['stu_qq'] = query.stu_qq
	dict['stu_email'] = query.stu_email
	dict['stu_yzbm'] = query.stu_yzbm
	dict['stu_ksh'] = query.stu_ksh
	dict['stu_rxsj'] = str(query.stu_rxsj)
	dict['stu_rxfs'] = query.stu_rxfs
	dict['stu_xxxs'] = query.stu_xxxs
	dict['stu_pylx'] = query.stu_pylx
	dict['stu_pydx'] = query.stu_pydx
	dict['stu_pycc'] = query.stu_pycc
	dict['stu_bxlx'] = query.stu_bxlx
	dict['stu_bxxx'] = query.stu_bxxx
	dict['stu_class']=query.stu_class
	dict['stu_img'] = query.stu_img
	dict['stu_tel'] = query.stu_tel
	dict['stu_dept'] = query.stu_dept
	dict['stu_profession'] = query.stu_profession
	dict['stu_start_date'] = str(query.stu_start_date)
	dict['stu_native'] = query.stu_native
	dict['stu_record'] = query.stu_record
	return dict
def StuInfo_ToJson(stu_id):
	'''http://www.jb51.net/article/46462.htm json原理
	http://www.jb51.net/article/74935.htm 参考资料
	'''
	return query_by_stu_id(stu_id)
	# for x,y in query_by_stu_id(stu_id):
	# 	meta[x]=y

	# angular={}
	# meta={}
	# data={}
	# inform_content={}
	# messages={}
	# jsonp_callback = request.args.get('callback', '')#关键代码
	# angular["meta"]=meta
	# angular["messages"] = messages
	# angular["data"] = data
	# angular["inform_content"] = inform_content
	# meta["stu_name"]="高慧鹏"
	# meta["stu_cardID"] = "142401199501284219"
	# meta["stu_sex"] = "男"
	# meta["stu_NO"] = "132055110"
	# meta["stu_start_date"] = "2013"
	# meta["stu_record"] = "本科"
	# meta["stu_birthday"] = "1995-01-28"
	# meta["stu_nation"] = "汉族"
	# meta["stu_zzmm"] = "团员"
	# meta["stu_adress"] = "山西省晋中市榆次区乌金山镇"
	# meta["stu_qq"]="573941623"
	# meta["stu_email"] = "573941623@qq.com"
	# meta["stu_yzbm"] = "030600"
	# meta["stu_ksh"] = "0310612654"
	# meta["stu_rxsj"] = "2013-9"
	# meta["stu_rxfs"] = "普通入学"
	# meta["stu_xxxs"] = "普通全日制"
	# meta["stu_pylx"] = "普通本科生"
	# meta["stu_pydx"] = "统招"
	# meta["stu_pycc"] = "本科"
	# meta["stu_bxlx"] = "普通高等教育"
	# meta["stu_bxxx"] = "国家任务"
	# meta["stu_img"] = "img/default_user_logo.png"
	# meta["stu_tel"] = "18835179550"
	# meta["stu_dept"] = "计算机工程系"
	# meta["stu_profession"] = "网络工程"
	# meta["stu_class"] = "132055110"
	# meta["stu_start_date"] = "2013"
	# meta["stu_native"] = "中国"
	# meta["class_name"] = "132055110网络工程"
	# meta["class_qq"] = "123456789"
	# meta["class_word"] = "奋斗奋斗奋斗！"
	# meta["school_name"] = "太原工业学院"
	# meta["leadr_tec"] = "张某某"
	# meta["leadr_tec_tel"] = "18812341234"
	# inform_content["inform_id"] = "001"
	# inform_content["inform_type"] = "学校通知"
	# inform_content["inform_tit"] = "关于开展太原工业学院第六届“安全月”活动的通知"
	# inform_content["inform_type"] = "学校通知"
	# inform_content["inform_content"] = "学校通知"
	# inform_content["inform_type"] = "为坚持落实“安全第一、预防为主、重在宣传”的方针，大力宣传校园安全知识，进一步增强学生的安全防范意识，提高学生的自护自救能力，进一步推进学校安全文化建设，营造“时时讲安全，处处抓安全，人人保安全”的良好氛围，确保学生人身和财产安全。经研究，特举办第六届“安全月”活动，具体安排如下:一、活动主题谱安全乐章创和谐太工二、活动时间2016年11月10日--12月8日三、活动内容:(一)安全知识讲座针对大一新生进行各项安全教育。包括网络安全、防盗安全、食品安全，重点进行消防安全及防诈骗安全教育。（二）“ 谨防诈骗 拒绝网贷”主题班会以班级为单位，就“谨防诈骗，拒绝网贷”为内容举办主题班会，借此唤醒大学生尤其是大一新生的警觉意识，提高自我防范能力（三）“ 谱安全乐章  创和谐太工”承诺签名活动紧扣“ 谱安全乐章  创和谐太工”的主题，倡导学生们树立校园安全意识。面向全校师生倡导安全文明大型签名活动，并发放“大学生安全知识手册”，宣传安全知识。（四）漫画征集大赛将安全常识以漫画的形式创作展示出来，全面普及我校学生的安全知识，提高安全意识。(五)安全知识竞赛（团体赛）以系为单位进行安全知识竞赛。让安全知识更深刻、牢固的在学生中普及，让学生在掌握知识的同时增强团队合作的意识。（六）2016级新生消防演练组织大一全体新生模拟火灾现场进行应急疏散演练，让同学们在参与的过程中增强安全防火意识，提高火灾安全防范及自救能力，普及逃生知识和方法，学习在特殊情况下的医疗救护知识"
	# inform_content["inform_date"] = "2016-11-1"
	# messages[0]["message_id"]="001"
	# messages[0]["message_type"] = "问候"
	# messages[0]["message_tit"] = "你好，高慧鹏"
	# messages[0]["message_content"] = "你好，我是你的新班主任张某某，平时要好好学习天天向上哦！"
	# messages[0]["message_date"] = "2016-11-10"
	# messages[1]["message_id"] = "002"
	# messages[1]["message_type"] = "问候"
	# messages[1]["message_tit"] = "你好，高慧鹏"
	# messages[1]["message_content"] = "你好，我是你的新班主任张某某，平时要好好学习天天向上哦！"
	# messages[1]["message_date"] = "2016-11-10"
	# data["message"]="Not Found"
	# data["message"]="https://developer.github.com/v3"
	# jsonStr = json.dumps(angular)
	# return Response("%s(%s)"%(jsonp_callback,jsonStr),mimetype='text/javascript')#关键代码

# stu_info().delete_table()
# stu_info().creat_table()
# s=stu_info.query.filter_by(stu_id='1').first() #返回值是类类型  s.stu_id
# s1=stu_info.query.all() #返回值是list类型 s1[0].stu_id
# print s.stu_id,s.stu_name,s.stu_cardID,s.stu_sex,s.stu_birthday,s.stu_nation,s.stu_zzmm,s.stu_qq,s.stu_email,s.stu_yzbm,s.stu_ksh,s.stu_rxsj,s.stu_rxfs,s.stu_xxxs,s.stu_pylx,s.stu_pydx,s.stu_pycc,s.stu_bxlx,s.stu_bxxx,s.stu_img,s.stu_tel,s.stu_dept,s.stu_profession,s.stu_class,s.stu_start_date,s.stu_native,s.stu_record



















