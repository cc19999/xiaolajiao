#!/usr/bin/env python
# --*--coding: utf-8 --*--
from datetime import timedelta
from redis import Redis
from dbutils.pooled_db import PooledDB,SharedDBConnection
import time
import pymysql
import os,base64
import sys

POOL = PooledDB(
    creator=pymysql,  # 使用连接数据库的模块
    maxconnections=6,  # 连接池允许的最大连接数，0 和 None 表示不限制连接数
    mincached=2,  # 初始话时，连接池中至少创建的空闲连接，0 表示不创建
    maxcached=5,  # 连接池中最多闲置的链接，0 和 None 表示不限制
    maxshared=3,
    # 连接池中最多共享的链接数量，0 和 None 表示全部共享。但是，因为pymysql和mysqldb等模块的 threadsafety 都为1，所有值无论设置多少，_maxcached永远为0，所以永远是所有链接都共享
    blocking=True,  # 连接池中如果没有可用链接后，是否阻塞等待。True 等待，False 不等待然后报错
    maxusage=None,  # 一个链接最大多被重复使用的次数，None 表示无限制
    setsession=[],  # 开始会话前执行的命令列表。如:["set datestyle to ...","set time zone..."]
    ping=0,
    # ping MySQL服务端，检查是否服务可用。如 0=None=never，1=default=whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
    host='127.0.0.1',
    port=3306,
    user='root',
    password='root',
    database='nan',
    charset='utf8'
)

class BaseConfig(object):
    SECRET_KEY = 'fsfhjsh23hsdai34'
    DATABASE_URL='mysql:\\root@localhost\pro'
    PERMANENT_SESSION_LIFETIME = timedelta(hours=6)  # 设置 cookie 的有效时间 为 6 小时
    SESSION_TYPE = 'redis'
    BASE_DIR = os.path.dirname(__file__)
    sys.path.append(BASE_DIR)
    # 静态配置文件 static
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    # 自定义的 图片上传路径
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    #MYSQL_POOL=POOL

    # 白名单
    WHITE_LIST = ['chen']
    # 黑名单
    BLACK_LIST = ['liu']
    # 受限名单
    RESTRICTED_LIST = ['gao']


class MasterConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_ECHO = False


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SESSION_REDIS = Redis(host='127.0.0.1',port=6379)



Config = {'master':MasterConfig,'development':DevConfig}




if __name__ == '__main__':
    print(BaseConfig.BASE_DIR)
    print(BaseConfig.STATIC_ROOT)
    # print('123')