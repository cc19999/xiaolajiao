#!/usr/bin/env python
# --*--coding: utf-8 --*--
from flask import(
	Blueprint,flash,g,redirect,render_template,request,url_for,session
)

from app01.db_old import SQLHelper,getConnectDb
from threading import Thread
import time


# 猪
pig = Blueprint('pig',__name__,url_prefix='/pig')



@pig.route('/index')
def index():
	print('pig-index-session',session.get('user_info'))
	return "pig's index"

def task(arg):
	db = getConnectDb()
	# ss = db.query("select * from user where name = %s and password = %s", ['admin', '123'])
	print('task 进入1 秒休眠 --- %s'%arg)
	time.sleep(1)


	sql = "insert into user (name,password) values (%s,%s)"
	info = db.updata_db(sql,[f'admin{arg}','123123'])
	print(f'pig-eat-{arg}', info)
	pass


def test(arg):
	print(f'{arg} 进来了')
	time.sleep(1)
	print(f'{arg} 出去了')

@pig.route('/eat')
def eat():
	session['info']['k1'] = 'old pig baby'
	print('pig-eat-session',session['info'])
	#for i in range(10):
	#	t = Thread(target=task,args=(i,))
	#	t.start()

	return 'pig 就知道吃饭，而且饭量巨大'

@pig.route('/ppp')
def ppp():
	print('pig-ppp-transaction')
	db = getConnectDb()
	t = db.transaction()
	try:
		sql = 'insert into test.user (name,usercode,password) values (%s,%s,%s)'
		db.query(sql,args=('郜梦瑶','mengyao','mengyao123'))
	except Exception as  e:
		print('出错了---',e)
		t.rollback()
	else:
		print('成功了')
		t.commit()
	return 'pig--ppp'



