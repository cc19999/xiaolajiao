#!/usr/bin/env python
# --*--coding: utf-8 --*--
from functools import wraps
from flask import g,request,redirect,url_for

def login_required(func):
    @wraps(func)
    def inner(*args,**kwargs):
        if g.user is None:
            print('login_required-重定向了')
            return redirect(url_for('account.login',next=request.url))
        print('come in login_required')
        return func(*args,**kwargs)
    return inner