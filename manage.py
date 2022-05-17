#!/usr/bin/env python
# --*--coding: utf-8 --*--


from app01 import create_app,render_template
from flask_script import Manager
from celery_manage import celery_app

# from flask_migrate import Migrate,MigrateCommand
# from app01 import db
# import os,base64
# import sys


# manager = Manager(app)
# Migrate(app,db)
'''
数据库迁移命令：
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
表字段变更后，再执行后两条即可。
'''
# manager.add_command('db',MigrateCommand)

#
# print(__file__)  # 当前文件的绝对路径
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# sys.path.append(BASE_DIR)
# STATIC_ROOT= os.path.join(BASE_DIR,'static')
#
# def create_key(length):
#     random_str = os.urandom(length)
#     byte_ret = base64.b64encode(random_str) # 生成byte类型字符串: b'Easpoammc+/'
#     result = byte_ret.decode('unicode_escape')
#     return result


app = create_app(celery=celery_app)


@app.route('/index')
def index():

    return render_template('/index.html')

manager = Manager(app)

if __name__ == '__main__':
    # app.run()
    # app.run()
    manager.run()
    # app.run()



