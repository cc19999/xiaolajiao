#!/usr/bin/env python
# --*--coding: utf-8 --*--

from sqlalchemy.orm import relationship
from app01 import db
import datetime

'''
当前模块用的是 flask-sqlalchemy
'''


class Users(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_code = db.Column(db.String(32),unique=True,nullable=False)
    name = db.Column(db.String(32))
    password = db.Column(db.String(64),nullable=False)
    email= db.Column(db.String(32))
    ctime = db.Column(db.DateTime,default=datetime.datetime.now)
    avatar = db.Column(db.String(128),default='media/avatars/default.png')
    depart_id = db.Column(db.Integer,db.ForeignKey('Department.did')) # 关联部门表

    __table_args__ = (
        # 联合唯一索引创建，前两个是 联合字段，后面的是 索引名称
        db.UniqueConstraint('name','email',name='uix_user_name_email'),
        # 普通索引，第一个是索引名称，后面是要创建的字段
        db.Index('ix_user_code','user_code','email')
    )

# 部门
class Department(db.Model):
    __tablename__='Department'
    did = db.Column(db.Integer,primary_key=True,nullable=False)
    department_name = db.Column(db.String(32),nullable=False)
    summary = db.Column(db.Text,nullable=True)


# 兴趣爱好
class Hobby(db.Model):
    __tablename__ = 'hobby'
    hid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(32),nullable=False,unique=True)
    group_name = db.Column(db.String(32),nullable=True,unique=True)
    group_id = db.Column(db.Integer,nullable=True,unique=True)

# 人员于兴趣爱好多对多关系表
class User2Hobby(db.Model):
    __tablename__ = 'user2hobby'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.uid'))
    hobby_id = db.Column(db.Integer,db.ForeignKey('hobby.hid'))

    __table_args__ = (
        # 人员于爱好联合唯一索引
        db.UniqueConstraint('user_id','hobby_id',name='uix_user_hobby'),
    )


if __name__  == '__main__':
    # drop_db()
    # init_db()
    pass