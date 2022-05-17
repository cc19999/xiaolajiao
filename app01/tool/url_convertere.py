#!/usr/bin/env python
# --*--coding: utf-8 --*--
from werkzeug.routing import BaseConverter


class MyConverter(BaseConverter):
    '''
    自定义路由类型转换规则
    '''
    regex = r'1[3-9]\d{9}'   # 在这里可以写正则表达式，
    def __init__(self,map,regex=regex): # 这里利用正则表达式规则进行匹配
        super(MyConverter, self).__init__(map)
        self.regex=regex   # 匹配成功之后赋值，然后进入 to_python 函数

    def to_python(self, value):
        '''
        当init函数中匹配规则成功之后，就走入到这个函数中，返回值
        :param value:
        :return:
        '''
        return int(value)

    def to_url(self, value):
        '''
        使用url_for反向生成url时，传递的参数经过该方法处理，返回的值用于生成URL中的参数
        :param value:
        :return:
        '''
        val = super(MyConverter,self).to_url(value)
        return val