from flask.ext.wtf import Form
from wtforms import PasswordField
from flask.ext.wtf.html5 import EmailField
from wtforms.validators import Required


class LoginForm(Form):
    email = EmailField('email', [Required()])
    password = PasswordField('Password', [Required()])
