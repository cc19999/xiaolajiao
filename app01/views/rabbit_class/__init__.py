#!/usr/bin/env python
# --*--coding: utf-8 --*--
from flask import(
	Blueprint,flash,g,redirect,render_template,request,url_for
)


rabbit = Blueprint('rabbit',__name__,url_prefix='/rabbit')




@rabbit.route('/index')
def index():
	return '长长的耳朵一定是兔子嘛？？？？？'