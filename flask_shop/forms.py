from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, HiddenField
from wtforms.validators import Required


class LoginForm(Form):
    alternative_mail = TextField('alternative_mail', [Required()])
    email = HiddenField('email', [Required()])
    password = PasswordField('Password', [Required()])
