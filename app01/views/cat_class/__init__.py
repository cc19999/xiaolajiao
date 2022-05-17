#!/usr/bin/env python
# --*--coding: utf-8 --*--
from flask import(
	Blueprint,flash,g,redirect,render_template,request,url_for,current_app
)
from flask_mail import Mail,Message

import json

cat = Blueprint('cat',__name__,url_prefix='/cat')




@cat.route('/index')
def index():
	return render_template('send_email.html')


@cat.route('/sendemail',methods=['GET','POST'])
def sendEmail():
	if request.method == 'GET':
		return render_template('send_email.html')
	else:
		print('sendemail post 请求')
		mail = Mail(current_app)
		info = request.json
		addr = info.get('addr')
		title = info.get('title')
		content = info.get('content')
		msg = Message(title,recipients=[addr],body=content)
		mail.send(msg)
		return json.dumps({'code':200,'msg':'发送成功'})



