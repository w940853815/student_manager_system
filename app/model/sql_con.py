#coding:utf-8
'''配置数据库'''
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:940wangrui@123.207.139.130:3306/bootstrap_student_system'
db=SQLAlchemy(app)
