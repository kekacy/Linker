# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length


class HelloForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 10)])
    body = TextAreaField('Message', validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField()


class UsersForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(1, 10)])
    password = PasswordField('密码', validators=[DataRequired(), Length(1, 10)])
    remember = BooleanField('记住我')
    logon = SubmitField('登录')
    register = SubmitField('注册')
