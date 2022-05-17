#!/usr/bin/env python
# --*--coding: utf-8 --*--
from datetime import timedelta
from redis import Redis
from dbutils.pooled_db import PooledDB,SharedDBConnection
import time
import pymysql
import os,base64
import sys


class BaseConfig(object):

    SECRET_KEY = 'fsfhjsh23hsdai34'
    USERNAME='root'
    PASSWORD='root'
    # DEFAULT_DB='nan'
    HOST='127.0.0.1'
    PORT=3306

    SQLALCHEMY_DATABASE_URI=f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/nan?charset=utf8"
    SQLALCHEMY_POOL_SIZE=5
    SQLALCHEMY_POOL_TIMEOUT=30
    SQLALCHEMY_POOL_RECYCLE=-1
    # 追踪对象的修改且发送信号
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    SESSION_TYPE = 'redis'

    # redis 缓存
    CACHE_TYPE='redis'
    CACHE_REDIS_HOST='127.0.0.1'
    CACHE_REDIS_PORT=6379
    CACHE_REDIS_DB=''
    CACHE_REDIS_PASSWORD=''


    BASE_DIR = os.path.dirname(__file__)
    sys.path.append(BASE_DIR)
    # 静态配置文件 static
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    # 自定义的 图片上传路径
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    # 图片上传路径
    UPLOAD_FOLDER = os.path.join(MEDIA_ROOT,'avatar')
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
    # 显示生成的SQL语句，可用于调试
    SQLALCHEMY_ECHO = True
    SESSION_REDIS = Redis(host='127.0.0.1',port=6379)

    # 邮箱配置
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = '282306889@qq.com'
    MAIL_PASSWORD = 'qtxhzbkdprcpbicc'
    MAIL_DEFAULT_SENDER = '282306889@qq.com'

    # celery 配置
    BROKER_URL='redis://127.0.0.1:6379/1'
    RESULT_BACKEND = 'redis://127.0.0.1:6379/2'

    task_serializer = 'json'
    result_serializer = 'json'
    accept_content = ['json']
    timezone = 'Europe/Oslo'  # 时区
    enable_utc = True
    imports = ('celery_task',)


Config = {'master':MasterConfig,'development':DevConfig}




if __name__ == '__main__':
    print(BaseConfig.BASE_DIR)
    print(BaseConfig.STATIC_ROOT)
    print(BaseConfig.UPLOAD_FOLDER)
    import sys
    print(sys.path)
    # print('123')