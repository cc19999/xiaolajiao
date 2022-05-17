#!/usr/bin/env python
# --*--coding: utf-8 --*--
from flask import Flask
from werkzeug.wsgi import WSGIApplication
from werkzeug.serving import run_simple


app1 = Flask('app1')
app2 = Flask('app2')


@app1.route('/login')
def login():
    return 'app1.login'


@app2.route('/index')
def index():
    return 'app2.index'


dm = WSGIApplication(app1,{
    '/app2':app2
})

if __name__ == '__main__':
    run_simple('localhost',5000,dm)