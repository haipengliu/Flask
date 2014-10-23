from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(Form):
    user_id  = TextField('username', validators = [DataRequired()])
    password = PasswordField('password', validators = [DataRequired()])
