#!/usr/bin/env python
# --*--coding: utf-8 --*--

from app01 import db
from app01 import app
from app01 import models

with app.app_context():
    '''
    可以在这里进行一系列操作，创建或删除表，增删改查表数据等。。
    '''
    # db.drop_all()
    db.create_all()
    # data = db.session.query(models.Users).all()
    # print(data)

