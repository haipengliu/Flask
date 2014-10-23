#coding:utf-8
from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField
from wtforms.validators import DataRequired
from models import db, User

class LoginForm(Form):
    username = TextField(u'用户名', validators = [DataRequired(u'请输入用户名')])
    password = PasswordField(u'密码', validators = [DataRequired(u'请输入密码')])
    submit   = SubmitField(u'修改密码')
    
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
     
            user = User.query.filter_by(username = self.username.data).first()
            if user and user.check_password(self.password.data):
                return True
            else:
                self.username.errors.append(u"无效的用户名或密码")
                return False
