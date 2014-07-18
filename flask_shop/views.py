from flask.ext.login import LoginManager, login_required, login_user, logout_user, current_user
from flask import flash, redirect, url_for, session, render_template, request, Blueprint
from flask_shop import app
from .forms import LoginForm
from .models import User
login_manager = LoginManager(app)
flask_shop = Blueprint('shop', __name__, url_prefix='/shop')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@flask_shop.route('/')
def index():
    return redirect(url_for('shop.login'))


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
        user = User.objects.get_or_404(
            email=request.form['alternative_mail'])
        if user is not None and user.check_password(request.form['password']):
            flash(u'Successfully logged in as %s' % user.email)
        session['user_id'] = user.id
        login_user(user)
        return redirect(url_for("shop.reports"))
    return render_template('login.html', form=form)


@flask_shop.route("shop")
def shop():
    pass


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
