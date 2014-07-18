import logging
import sys
import uuid

from flask import Flask
from flask.ext.mail import Mail
from flask.ext.babel import Babel
from flask.ext.bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension
import config

app = Flask(__name__)
app.config.from_object(config)
mail = Mail(app)
babel = Babel(app)
bcrypt = Bcrypt(app)

toolbar = DebugToolbarExtension(app)

# logger = logging.getLogger(__name__)
# flask_shop = Blueprint('flask_shop', __name__)
# mail = Mail()
# login_manager = LoginManager()
# bcrypt = Bcrypt()

from views import *
from forms import *
from models import *

app.register_blueprint(flask_shop)


def create_db():
    db.create_all()


def clear_db():
    db.drop_all()


def main():
    app.run()

if __name__ == '__main__':
    sys.exit(main())
