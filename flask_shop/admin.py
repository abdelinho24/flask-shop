from flask.ext.admin import Admin, BaseView, expose
from flask.ext.login import current_user
from flask_shop import app
from models import Product, User, Order, Currency, ProductPrice, Brand

admin = Admin(app)


class ViewWithAuth(BaseView):

    def is_accessible(self):
        return current_user.is_authenticated()
