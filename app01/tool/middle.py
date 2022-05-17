#!/usr/bin/env python
# --*--coding: utf-8 --*--




class InterceptMiddle(object):

    def __init__(self,wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self,environ, start_response):
        print('InterceptMiddle')
        #print(environ)
        url = environ.get('REQUEST_URI',None)
        print('url:',url)
        return self.wsgi_app(environ,start_response)
