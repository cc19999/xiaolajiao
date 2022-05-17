from flask import Flask, render_template, request, redirect, session, g,views,current_app,make_response,flash
from app01.config import Config
# from .tool.url_convertere import MyConverter
# from .tool.my_wraps import login_required
# from .cbv import IndexView,IndexView2
# from .tool.middle import InterceptMiddle
from werkzeug.utils import import_string
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from exts.auth import Auth
# from app01.tasks.celery_worker import make_celery
# redis 缓存相关
from flask_cache import Cache
import os



db = SQLAlchemy()
cache = Cache()

def auto_register_blueprint(app):
    base_path = r'app01/views/'
    bp_list = os.listdir(base_path)
    for bp in bp_list:
        bp_path = os.path.join(base_path,bp)
        if os.path.exists(os.path.join(bp_path,'__init__.py')):
            zoo = bp.split("_")[0]
            bp_path = bp_path.replace('/','.')
            # print(bp_path+'.'+zoo)
            auto_bp = import_string(bp_path+'.'+zoo)
            app.register_blueprint(auto_bp)



def create_app(config_name='development',*args,**kwargs):


    app = Flask(__name__,static_folder=Config[config_name].STATIC_ROOT,static_url_path='/static')
    # static_folder:静态资源路径,static_url_path:静态资源展示的url前缀
    app.config.from_object(Config[config_name])
    # 自定义路由转换类型
    #app.url_map.converters['myconver'] = MyConverter
    #app.add_url_rule('/what',view_func=IndexView.as_view(name='what')) # 这里的name就等于 endpoint
    #app.add_url_rule('/what2',view_func=IndexView2.as_view(name='what2')) # 这里的name就等于 endpoint
    # app.wsgi_app = InterceptMiddle(app.wsgi_app)
    auto_register_blueprint(app)


    db.init_app(app)
    #cache.init_app(app)

    register_celery(celery=kwargs.get('celery'), app=app)


    # 将 session 替换成 redis-session
    Session(app)

    Auth(app)

    return app






def register_celery(celery, app):
    class ContextTask(celery.Task):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask







# @app.before_request
# def xxx2():
#     print('xxx2 执行了')
#
# @app.after_request
# def ddd(response):
#     print('ddd 最后执行')
#     return response
# @app.after_request
# def ddd2(response):
#     print('ddd2 执行了')
#     return response





# @app.route('/',redirect_to='/account/login')
# def hello_world():  # put application's code here
#     print('当前请求是 /')
#     return 'xxxx'


# @app.route('/login', methods=['get', 'post'])
# def login():
#     if request.method == 'GET':
#         print('请求来了')
#         return render_template('/login.html')
#     user = request.form.get('user')
#     password = request.form.get('password')
#     if user == 'chen' and password == '123':
#         session['user_info'] = user
#         session['info'] = {'k1':123,'k2':456}
#         flash('登录成功！')
#         return redirect('/index')
#     else:
#         return render_template('/login.html', msg='用户名密码错误')
# #        return render_template('login.html',**{'msg' : '用户名密码错误'})








# @app.route('/index/<myconver:nid>')
# @login_required
# def book(nid):
#     print('nid:', nid)
#     return render_template('index.html')

# @app.route('/index2/<int:nid>')
# @login_required
# def boo2(nid):
#     print('book2:',nid)
#     return render_template('index.html')








