#!/usr/bin/env python
# --*--coding: utf-8 --*--
import json

from flask import(
	Blueprint, render_template, request, current_app
)
import datetime
from flask_mail import Mail,Message




cattle = Blueprint('cattle',__name__,url_prefix='/cattle')



@cattle.route('/index')
def index():
	return '牛脾气老道！！！'

def mail_init():
	mail = Mail(current_app)
	return mail,Message



@cattle.route('/ctime_email',methods=['GET','POST'])
def ctime_email():
	if request.method=='GET':
		return render_template('cattle/index.html')
	else:
		from app01.sms.task01 import send_email
		data = request.json
		print(data)
		if data:
			cdatelist = data.get('cdate').split('-')
			ctimelist = data.get('ctime').split(':')
			v1 = datetime.datetime(int(cdatelist[0]),int(cdatelist[1]),int(cdatelist[2]),int(ctimelist[0]),int(ctimelist[1]))
			new_date = datetime.datetime.utcfromtimestamp(v1.timestamp()) # 将v1转成时间戳
			print('newdata',new_date)
			result = send_email.apply_async(args=[data],eta=new_date)
			print(
				result.id,
				result
			)
		return 'ok'


		# from celery_app.test_celery.task1 import send_email
		# result = send_email.delay(1,3)
		# print('xxxxxxxx-id',result)
		# return json.dumps(1)


@cattle.route('/ctime_email2',methods=['GET','POST'])
def ctime_email2():
	if request.method=='GET':
		return render_template('cattle/index.html')
	else:
		data = request.json
