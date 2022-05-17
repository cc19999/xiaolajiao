#!/usr/bin/env python
# --*--coding: utf-8 --*--

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey,UniqueConstraint,Index,Text
from sqlalchemy.orm import relationship
from app01 import db
import datetime

'''
当前示例用的是 sqlalchemy 。 但是 flask 一般使用 flask-sqlalchemy
'''

Base = declarative_base()
# flask-sqlalchemy  生成 SQLAlchemy() 对象的时候，会帮我们调用 declarative_base 方法创建base，下面将Base改成db.Model

class Users(db.Model):
    __tablename__ = 'users'
    uid = Column(Integer,primary_key=True,autoincrement=True)
    user_code = Column(String(32),unique=True,nullable=False)
    name = Column(String(32))
    password = Column(String(64),nullable=False)
    email=Column(String(32))
    ctime = Column(DateTime,default=datetime.datetime.now)
    avatar = Column(String(128),default='media/avatars/default.png')
    depart_id = Column(Integer,ForeignKey('Department.did')) # 关联部门表

    __table_args__ = (
        # 联合唯一索引创建，前两个是 联合字段，后面的是 索引名称
        UniqueConstraint('name','email',name='uix_user_name_email'),
        # 普通索引，第一个是索引名称，后面是要创建的字段
        Index('ix_user_code','user_code','email')
    )

# 部门
class Department(db.Model):
    __tablename__='Department'
    did = Column(Integer,primary_key=True,nullable=False)
    department_name = Column(String(32),nullable=False)
    summary = Column(Text,nullable=True)


# 兴趣爱好
class Hobby(db.Model):
    __tablename__ = 'hobby'
    hid = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(32),nullable=False,unique=True)
    group_name = Column(String(32),nullable=True,unique=True)
    group_id = Column(Integer,nullable=True,unique=True)

# 人员于兴趣爱好多对多关系表
class User2Hobby(db.Model):
    __tablename__ = 'user2hobby'
    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey('users.uid'))
    hobby_id = Column(Integer,ForeignKey('hobby.hid'))

    __table_args__ = (
        # 人员于爱好联合唯一索引
        UniqueConstraint('user_id','hobby_id',name='uix_user_hobby')
    )


def init_db():
    # 数据库连接相关
    engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/nan?charset=utf8",
                           max_overflow=5,  # 超过连接池大小外最多创建的连接
                           pool_size=5,  # 连接池大小
                           pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
                           pool_recycle=-1  # 多久之后对线程池进行一次连接回收（重置）
                            )
    Base.metadata.create_all(bind=engine)

def drop_db():
    engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/nan?charset=utf8",
                           max_overflow=5,  # 超过连接池大小外最多创建的连接
                           pool_size=5,  # 连接池大小
                           pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
                           pool_recycle=-1  # 多久之后对线程池进行一次连接回收（重置）
                            )
    Base.metadata.drop_all(engine)


if __name__  == '__main__':
    # drop_db()
    init_db()
    pass