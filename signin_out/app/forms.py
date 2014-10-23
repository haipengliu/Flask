#coding:utf-8
from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField
from wtforms.validators import DataRequired, InputRequired, EqualTo
from models import db, User
from werkzeug import generate_password_hash, check_password_hash

def check_password(pwd1, pwd2):     
  return check_password_hash(pwd1, pwd2)

class SignupForm(Form):
    username = TextField(u'用户名',  validators = [DataRequired()])
    password = PasswordField(u'密码', validators = [DataRequired()])
    submit = SubmitField(u'确认')
 
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
     
            user = User.query.filter_by(username = self.username.data).first()
            if user and user.check_password(self.password.data):
                return True
            else:
                self.username.errors.append(u'无效用户名或密码')
                return False
           
class ChangePwd(Form):
    username = TextField(u'用户名',  validators = [DataRequired(u'请输入用户名')])
    oldpwd  = PasswordField(u'旧密码', validators = [DataRequired(u'请输入旧密码')])
    newpwd1 = PasswordField(u'新密码',  [InputRequired(u'请输入您的新密码'), EqualTo(u'newpwd2', message=u'您两次输入的新密码不一致')])
    newpwd2 = PasswordField(u'重复新密码', validators = [DataRequired(u'请重复输入您的新密码')])
    submit  = SubmitField(u'确认')
 
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
          return False
     
          user = User.query.filter_by(username = self.username.data).first()
          if user and user.check_password(self.oldpwd.data):
            return true
          else:
            self.username.errors.append(u'无效用户名或旧密码')
            return False
 
