#!/usr/bin/env python
# --*--coding: utf-8 --*--

from .config_old import POOL
import pymysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy import create_engine







class SQLHelper(object):

    @staticmethod
    def fetch_one(sql, args=()):
        conn = POOL.connection()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        result = cursor.fetchone()
        conn.close()
        return result

    @staticmethod
    def fetch_all(sql, args=()):
        conn = POOL.connection()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        result = cursor.fetchall()
        conn.close()
        return result


class getConnectDb():
    def __init__(self):
        self.conn = POOL.connection()
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)  # 设置该参数，查询回来的就是字典

    def query_db(self,sql,arg=(),one=False):
        self.cur.execute(sql,arg)
        rv = self.cur.fetchall()
        return (rv[0] if rv else None) if one else rv

    def change_db(self,sql,arg=()):
        '''更新语句'''
        try:
            self.cur.execute(sql,arg)
        except Exception as e:
            self.conn.rollback()
            print('-------处理失败',e)
        else:
            self.conn.commit()
            print('------处理成功')

    def query(self,sql,args=()):
        '''插入语句'''
        self.cur.execute(sql,args)
        return self.cur

    def transaction(self):
        '''开启事务'''
        self.conn.begin()
        return self.conn

    def __del__(self):
        self.cur.close()
        self.conn.close()
        #print('--------关闭连接')