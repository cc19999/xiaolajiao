#!/usr/bin/env python
# --*--coding: utf-8 --*--
from .tool.my_wraps import login_required
from flask import views,request,current_app

class IndexView(views.View):
    methods = ['get','post']
    decorators = [login_required]
    def dispatch_request(self,*args,**kwargs):
        '''
        请求进来都走 dispatch_request 方法
        这里自己写反射方法
        :return:
        '''
        print(request.method)
        meth = request.method.lower()
        print(meth)
        if meth == 'get':
            print('get --- methods')
            meth=getattr(self,'get',None)
            return meth(*args,**kwargs)
        print('index')
        return 'index222111'

    def get(self):
        print('当前是 get 请求')
        return 'hahahhaa'
    def post(self):
        print('当前是 post 请求')


class IndexView2(views.MethodView):
    '''
    用 MethodView 就不用再去重写 dispatch_request 反射方法的，这个父类已经帮助我们写好了这个方法
    '''
    methods = ['get','post']
    decorators = [login_required]
    def get(self):
        print('这是get方法')
        return '这是 get 方法'
    def post(self):
        return '这是 post 方法'