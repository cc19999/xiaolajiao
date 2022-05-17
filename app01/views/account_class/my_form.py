#!/usr/bin/env python
# --*--coding: utf-8 --*--

from wtforms import Form
from wtforms.fields import core
from wtforms.fields import simple
from wtforms import validators
from wtforms import widgets,SelectField,SelectMultipleField,EmailField,RadioField
from flask_wtf.file import FileAllowed,FileRequired  # 发现不生效,可能是因为用的 wtforms.Form
from app01 import db,models



class LoginForm(Form):
    name = simple.StringField(
        validators=[
            validators.DataRequired(message='用户名不能为空.'),
            #validators.Length(min=6,max=18,message=f'用户名长度必须大于{min}且小于{max}')
        ],
        widget=widgets.TextInput(),
        render_kw={'class':'form-control','color':'red'}
    )
    password = simple.PasswordField(
        validators=[
            validators.DataRequired(message='密码不能为空'),
            #validators.Length(min=8,message=f'用户名长度必须大于{min}'),
            #validators.Regexp(regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}",
                              #message='密码至少8个字符，包含1个大写字母，1个小写字母，1数字和1个特殊符号！')
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class':'form-control'}
    )


class RegisterForm(Form):

    user_code = simple.StringField(
        label='用户名',
        validators=[
            validators.DataRequired('用户名不能为空。')
        ],
        widget=widgets.TextInput(),
        render_kw={'class':'form-control'},
        default=''
    )
    name = simple.StringField(
        label='名称',
        validators=[
            validators.DataRequired('名称不能为空')
        ],
        widget=widgets.TextInput(),
        render_kw={'class':'form-control'}
    )
    password = simple.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired('密码不能为空'),
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class':'form-control'}
    )
    pwd_confirm = simple.PasswordField(
        label='重复密码',
        validators=[
            validators.DataRequired('密码不能为空'),
            validators.EqualTo('password',message='两次密码不一致')
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class':'form-control'}
    )
    email = EmailField(
        label='邮箱',
        validators=[
            validators.DataRequired('邮箱不能为空'),
            validators.Email('邮箱格式错误')  # 校验email需要安装 email_validator pip install email_validator
        ],
        widget=widgets.TextInput(input_type='email'),
        render_kw={'class':'form-control'}
    )
    avatar = simple.Field(
        label='头像',
        widget=widgets.FileInput()
    )
    # gender = RadioField(
    #     label = '性别',
    #     choices=(
    #         (1,'男'),
    #         (2,'女')
    #     ),
    #     coerce=int
    # )
    # city = SelectField(
    #     label='城市',
    #     choices=(
    #         ('bj','北京'),
    #         ('hn','河南'),
    #         ('gz','广州')
    #     )
    # )
    #
    # phone = simple.StringField(
    #     label='手机号',
    #     validators=[
    #         validators.DataRequired('手机号不能为空'),
    #         validators.Regexp(regex=r'1[35789]\d{9}',message='手机号码不正确')
    #     ],
    #     widget=widgets.TextInput(),
    #     render_kw={'class': 'form-control'}
    # )
    #
    # favor = SelectMultipleField(
    #     label='喜好',
    #     choices=(
    #         (1, '篮球'), (2, '足球'), (3, '乒乓球'), (4, '羽毛球')
    #     ),
    #     widget=widgets.ListWidget(prefix_label=False)
    # )
    #
    # def __init__(self,*args,**kwargs):
    #     super(RegisterForm, self).__init__(*args,**kwargs)
    #     # 这里可以写构造方法，如地区加载: self.city.choices=db.query("select * from city")
    #     self.favor.choices = ((1,'篮球'),(2,'足球'),(3,'乒乓球'),(4,'羽毛球'))

    def validate_pwd_confirm(self,field):
        '''
        自定义 pwd_confirm 字段规则
        格式：validate_ + 校验的字段
        接收 filed 为当前校验字段输入的值
        self.data 有所有字段的值
        :param field:
        :return:
        '''
        # 最开始初始话的时候，self.data 中已经有所有的值
        if field.data != self.data['password']:
            # raise validators.ValidationError("密码不一致") # 继续后续验证
            raise validators.StopValidation("密码不一致")  # 不再继续后续验证

    def validate_user_code(self,field):
        '''
        自定义 user_code 是否存在
        :param field:
        :return:
        '''
        user_code = field.data
        user = models.Users.query.filter(models.Users.user_code==user_code).first()
        if user:
            raise validators.ValidationError("用户名已经存在。")

    def validate_avatar(self,field):
        '''
        自定义 头像 校验
        :param field:
        :return:
        '''
        file = field.data
        print('xxxxxfile',file)
        print('232131312',field)
