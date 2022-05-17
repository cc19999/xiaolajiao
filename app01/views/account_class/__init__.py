#!/usr/bin/env python
# --*--coding: utf-8 --*--
import os.path

from flask import Blueprint,g,url_for,request,render_template,redirect,session,current_app,flash,signals
from .my_form import LoginForm,RegisterForm
from app01 import models
# from app01.db_old import getConnectDb
from app01 import db


account = Blueprint('account',__name__,url_prefix='/account')

def func(*args,**kwargs):
    print('============信号出发 func=============')

@account.route('/login',methods=['GET','POST'])
def login():
    print('account/login')
    if request.method == 'GET':
        form = LoginForm()
        return render_template('login.html',form=form)
    else:
        form = LoginForm(formdata=request.form)
        if form.validate():
            signals.appcontext_pushed.connect(func)
            name = request.form.get('name')
            password = request.form.get('password')
            print('登录信息：',name,password)
            info = models.Users.query.filter(models.Users.user_code==name,models.Users.password==password).first()
            db.session.remove()
            if info:
                user_code = info.user_code
                name = info.name
                session['user_code']=user_code
                session['user_name']=name
                return redirect('/index')
            else:
                form.msg='用户名或密码错误！'
                # flash('账号信息不存在！')
                print('账户信息不存在')
                return render_template('login.html',form=form)

        else:
            print('校验出错--',form.errors)

            return render_template('login.html',form=form)


@account.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        form = RegisterForm()
        return render_template('register.html',form=form)
    else:
        form = RegisterForm(request.form)
        if form.validate():
            filename = request.files.get('avatar')
            name = request.form.get('name')
            user_code = request.form.get('user_code')
            password = request.form.get('password')
            email = request.form.get('email')
            extra = {}
            if filename:
                extra['avatar'] = filename.filename
                avartar_path = os.path.join(current_app.config['UPLOAD_FOLDER'],filename.filename)
                filename.save(avartar_path)
            use = models.Users(name=name,user_code=user_code,password=password,email=email,**extra)
            db.session.add(use)
            db.session.commit()
            return redirect(url_for('account.login'))
        else:
            print('注册失败')
            return render_template('register.html',form=form)


@account.route('/logout')
def logout():
    current_app.auth_manage.logout()
    return redirect('/account/login')

@account.route('/index')
def index():
    return 'account-index'