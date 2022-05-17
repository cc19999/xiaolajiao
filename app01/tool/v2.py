#!/usr/bin/env python
# --*--coding: utf-8 --*--

from functools import reduce
import itertools


# def add(x,y):
#     return x+y
#
# sum1 = reduce(add,[1,2,3,4,5,6,7])
# print(sum1)
#
# sum2 = reduce(lambda x,y:x+y,(1,2,3,4,5,6,7,8))
# print(sum2)

class Base(object):
    name = 'base'
    def get(self):
        xx = getattr(self.__class__,'name',None)
        print('父类找获取的name是：',xx)
        print(self.__class__)


class Foo(Base):
    # name = 'foo'
    pass


foo = Foo()
foo.get()


v = itertools.chain((12,3,4,5),(6,7,8))
print(v)
for i in v:
    print(i)