#!/usr/bin/env python
# --*--coding: utf-8 --*--
from flask import(
	Blueprint,flash,g,redirect,render_template,request,url_for
)
from app01 import cache,db,models


dog = Blueprint('dog',__name__,url_prefix='/dog')




@dog.route('/index')
def index():
	return '你是柯基么？？？'


@dog.route('/getuser')
def get_user():
	cache.set('user_info',123)
	res = cache.get('user_info')
	if not res:
		return render_template('dog/userinfo.html',user_info=res)
	user = models.Users.all()
	print('user',user)
	if user:
		return render_template('dog/userinfo.html',user_info=res)