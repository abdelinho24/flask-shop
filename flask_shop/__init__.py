"""
Flask-Shop description here.

"""

import os

from flask import Flask
from jinja2 import Environment, FileSystemLoader, ChoiceLoader, PackageLoader
import stripe

app = Flask(__name__)
app.config['SECRET_KEY'] = '=k%!&f)tw+2f&mypfm+i!ynh&(ev^tm&t(1j&b@py%s_!jgrlm'
app.config['WTF_CSRF_KEY'] = '!r2pw0i%)8b2=kx^o-%#0+f*d2oudycd9bxho=9cd1%7#snqa-'
app.config.from_object('config')
app.jinja_loader = ChoiceLoader([
    FileSystemLoader(os.path.join(os.getcwd(), 'templates')),
    PackageLoader('flask_shop'),
    ])
stripe.api_key = app.config['STRIPE_SECRET_KEY']
db.init_app(app)
mail.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)
app.register_blueprint(flask_shop)

__version__ = '0.0.1'