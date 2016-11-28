#coding:utf-8
from  sql_con import db
from flask_sqlalchemy import SQLAlchemy
class stu_info(db.Model):
	'''对数据库'''
	__tablename__='stu_info'
	stu_id = db.Column(db.Integer, primary_key=True)
	stu_name=db.Column(db.VARCHAR(8),nullable=False)
	stu_cardID=db.Column(db.CHAR(10),nullable=True)
	stu_sex=db.Column(db.VARCHAR(2),nullable=False)
	stu_birthday=db.Column(db.DATE,nullable=False)
	stu_nation=db.Column(db.VARCHAR(5),nullable=False)
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
	def __init__(self,stu_id,stu_name,stu_cardID,stu_sex,stu_birthday,stu_nation,
	             stu_zzmm,stu_qq,stu_email,stu_yzbm,stu_ksh,stu_rxsj,stu_rxfs,
	             stu_xxxs,stu_pylx,stu_pydx,stu_pycc,stu_bxlx,stu_bxxx,stu_img,
	             stu_tel,stu_dept,stu_profession,stu_class,stu_start_date,stu_native,
	             stu_record):
		self.stu_id=stu_id
		self.stu_name=stu_name
		self.stu_cardID=stu_cardID
		self.stu_sex=stu_sex
		self.stu_birthday=stu_birthday
		self.stu_nation=stu_nation
		self.stu_zzmm=stu_zzmm
		self.stu_qq=stu_qq
		self.stu_email=stu_email
		self.stu_yzbm=stu_yzbm
		self.stu_ksh=stu_ksh
		self.stu_rxsj=stu_rxsj
		self.stu_rxfs=stu_rxfs
		self.stu_xxxs=stu_xxxs
		self.stu_pylx=stu_pylx
		self.stu_pydx=stu_pydx
		self.stu_pycc=stu_pycc
		self.stu_bxlx=stu_bxlx
		self.stu_bxlx=stu_bxlx
		self.stu_bxxx=stu_bxxx
		self.stu_img=stu_img
		self.stu_tel=stu_tel
		self.stu_dept=stu_dept
		self.stu_profession=stu_class
		self.stu_class = stu_class
		self.stu_start_date = stu_start_date
		self.stu_native = stu_native
		self.stu_record = stu_record


	def creat_table(self):
		db.create_all()
		print u'stu_info表创建成功'
	def delete_table(self):
		db.drop_all()
		print u'stu_info表已删除'





# stu.delete_table()
# stu.creat_table()
s=stu_info.query.filter_by(stu_id='1').first()

s1=stu_info.query.all()
print s.stu_id,s.stu_name,s.stu_cardID,s.stu_sex,s.stu_birthday,s.stu_nation,s.stu_zzmm,s.stu_qq,s.stu_email,s.stu_yzbm,s.stu_ksh,s.stu_rxsj,s.stu_rxfs,s.stu_xxxs,s.stu_pylx,s.stu_pydx,s.stu_pycc,s.stu_bxlx,s.stu_bxxx,s.stu_img,s.stu_tel,s.stu_dept,s.stu_profession,s.stu_class,s.stu_start_date,s.stu_native,s.stu_record



















