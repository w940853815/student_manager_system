#coding:utf-8
from flask import Flask,render_template,url_for,Response,request
from app.model.model import *
import socket
app=Flask(__name__)


@app.route('/login',methods=['POST','GET'])
def login():
	#return request.form[]
	return render_template('index.html')
@app.route('/json',methods=['GET'])
def get_json():
	data={}
	data['meta']=StuInfo_ToJson(132055114)
	data['informs']=query_Inform()
	jsonp_callback = request.args.get('callback', '')  # 关键代码
	jsonStr = json.dumps(data)
	return Response("%s(%s)" % (jsonp_callback, jsonStr), mimetype='text/javascript')
@app.route('/main.html',methods=['POST','GET'])
def main():
	return  render_template('main.html')

if __name__ == '__main__':
	while 1:
		try:

			#app.run(host='0.0.0.0',port='80')
			app.run(host='0.0.0.0',port=80,debug=True)

		except socket.error,e:
			print e