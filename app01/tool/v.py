#!/usr/bin/env python
# --*--coding: utf-8 --*--
import time
from threading import get_ident
from threading import Thread
from threading import local



'''
做一个类似local的功能，就是 生成一个local实例对象，每个线程对这个对象进行调用之后，都会在当前线程内开辟一个独立的空间，用于当前线程，数据互补影响

需求：用面向对象方法实现增删改查
{
1:{'var':1},
2:{'var':2}
}

'''


class MyLocal(object):
    def __init__(self):
        self.dic = {}

    def set(self,k,v):
        id = get_ident()
        if id in self.dic.keys():
            ddf = self.dic[id]
            ddf[k]=v
        else:
            self.dic[id]={k:v}
        # print(self.dic)

    def get(self,k):
        id = get_ident()
        info = self.dic.get(id)
        return info.get(k,None)

    def deel(self,k):
        id = get_ident()
        info = self.dic.get(id)
        del info[k]
        return info

    def update(self,k,v):
        id = get_ident()
        info = self.dic.get(id)
        info[k]=v
        return info


test = MyLocal()


def dd(arg):
    name = 'ddd' + str(arg)
    # print(name)
    test.set(name,arg)
    time.sleep(2)
    print(test.get(name))

#
# for i in range(10):
#     t = Thread(target=dd,args=(i,))
#     t.start()
#

# salaries={'siry':3000,'tom':7000,'lili':10000,'jack':2000}
# res=sorted(salaries.items(),key=lambda kv:(kv[1],kv[0]),reverse=True)
# print(res)
# res=max(salaries,key=lambda k:salaries[k])
# print(res)


class myclass(object):

    def __call__(self, *args, **kwargs):
        print('当前是 call 方法')

    def __init__(self,name):
        print('当前是 init 方法')
        self.name = name

    def cal(self):
        print(f'我的名字是：{self.name}')

    def __enter__(self):
        print('当前是 enter 方法')
        return self.cal()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('当前是 exit 方法')



class MyType(type):
    CITY='GUANGZHOU'
    def __init__(self,*args,**kwargs):
        print('创建类前的方法')
        super(MyType,self).__init__(*args,**kwargs)
        print('创建类后的方法')

class Foo(object,metaclass=MyType):

    CITY='henan'
    def __init__(self,a,*args,**kwargs):
        super(Foo, self).__init__(*args,**kwargs)
        self.a=a
    def func(self,x):
        return x+1+self.a


# mengyao = Foo(11)
# print(mengyao.CITY)
# print(mengyao.func(1))