#!/usr/bin/env python
# --*--coding: utf-8 --*--
from flask import(
	Blueprint,flash,g,redirect,render_template,request,url_for
)


phone = Blueprint('phone',__name__,url_prefix='/phone')




@phone.route('/index')
def index():
	return '电话当然是每个动物的必备产品的啦 ！！！'