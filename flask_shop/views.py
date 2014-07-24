from flask.ext.login import LoginManager, login_required, login_user, logout_user, current_user
from flask import flash, redirect, url_for, session, render_template, request, Blueprint
from flask_shop import app
from .forms import LoginForm
from .models import User, Product, Order
login_manager = LoginManager(app)
flask_shop = Blueprint('shop', __name__, url_prefix='/shop')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@flask_shop.route('/')
def index():
    # products = Product.query.filter_by(discontinued=False).all()
    products = Product.query.all()
    return render_template('shop.html', products=products)

@flask_shop.route('/product', methods=['GET']) # Retrive all products
@flask_shop.route('/product', methods=['POST']) # Add new product
@flask_shop.route('/product/<id>', methods=['GET']) # Retrive one product by id
@flask_shop.route('/product/<id>', methods=['PUT']) # Update product by id
@flask_shop.route('/product/<id>', methods=['DELETE']) # Delete product by id
def product(id=None):
    if request.method=='GET':
        products = Product.objects.all()
        return 'GET'
    if request.method=='POST':
        return 'POST'
    if request.method=='PUT':
        return 'PUT'
    if request.method=='DELETE':
        return 'DELETE'
    return 'Product Admin page', 200


@flask_shop.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@flask_shop.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for('shop.reports'))
        redirect()
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects.get_or_404(email=form.email.data)
        if user is not None and user.check_password(form.password.data):
            flash(u'Successfully logged in as %s' % user.email)
        session['user_id'] = user.id
        login_user(user)
        return redirect(url_for("shop.reports"))
    return render_template('login.html', form=form)


# @flask_shop.route("shop")
# def shop():
#     products = Product.query.filter(discontinued=False).all()
#     render_template('shop', products=products)


@flask_shop.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('shop.login'))


@flask_shop.route('/reports', methods=['POST'])
@login_required
def reports():
    pass


@flask_shop.route('/charge', methods=['POST'])
def charge():
    pass
