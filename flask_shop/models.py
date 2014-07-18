from flask.ext.login import UserMixin
from flask_shop import bcrypt, app
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)

    def __str__(self):
        return self.name


class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String)
    currency = db.Column(db.String)

    def __str__(self):
        return self.currency + " " + self.caption


class ProductPrice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)

    def __str__(self):
        return self.price + " " + self.currency


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    image = db.Column(db.String)
    discontinued = db.Column(db.Boolean, default=False)
    colors = db.Column(db.String)
    size = db.Column(db.Integer)

    def __str__(self):
        return self.name if self.name is not None else 'No name'


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String)
    stripe_id = db.Column(db.String)
    description = db.Column(db.String)
    completed = db.Column(db.Boolean, default=False)
    comment = db.Column(db.String)
    created = db.Column(db.DateTime)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    password = db.Column(db.String)
    active = db.Column(db.Boolean, default=True)
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.passwords, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)

    def is_admin(self):
        return False

    def __str__(self):
        return self.email
