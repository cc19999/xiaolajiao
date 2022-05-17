#!/usr/bin/env python
# --*--coding: utf-8 --*--
from celery_manage import celery_app


@celery_app.task
def add2(x,y):
    print('加减计算')
    res = x+y
    print(res)
    return res


