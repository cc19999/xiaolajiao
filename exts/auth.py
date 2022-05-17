#!/usr/bin/env python
# --*--coding: utf-8 --*--
from flask import session,request,redirect,url_for

class Auth():

    def __init__(self,app=None):
        self.app = app
        if app:
            self.init_app(app)

    def init_app(self,app):
        app.auth_manage = self
        self.app = app


        app.before_request(self.check_login)
        app.context_processor(self.context_processor)


    def context_processor(self):
        user_name = session.get('user_name')

        return dict(current_user=user_name)

    def check_login(self):
        # print('xxxxxxxxxxxxx:',request.path)
        if request.path in ['/account/login','/account/register'] :
            return
        if request.path.startswith('/static'):
            '''在测试中发现，浏览器加载bootstrap、jquery等资源的时候的请求也传进来了，进行了多次重定向跳转，导致js加载失效。'''
            return
        user_code = session.get('user_code')
        print('check-login',user_code)
        if not user_code:
            print('请先登录！')
            return redirect(url_for('account.login'))


    def logout(self):
        del session['user_code'],session['user_name']