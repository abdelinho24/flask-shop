from flask.ext.login import UserMixin
from flask_shop import bcrypt, app
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


products = db.Table('products',
    db.Column('product_id', db.Integer, db.ForeignKey('product.id')),
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'))
)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String)
    image = db.Column(db.String)
    price = db.Column(db.Float, default=0.0)
    discontinued = db.Column(db.Boolean, default=False)

    def __unicode__(self):
        return self.name


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String)
    stripe_id = db.Column(db.String)
    client_email = db.Column(db.String)
    total_price = db.Column(db.String)
    description = db.Column(db.String)
    products = db.relationship('Product', secondary=products,
        backref=db.backref('orders', lazy='dynamic'))
    completed = db.Column(db.Boolean, default=False)
    completed_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    comment = db.Column(db.String)
    created = db.Column(db.DateTime)

    def __unicode__(self):
        return '%s - %s' %  (uuid, client_email)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
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
        return self.email

    def is_admin(self):
        return False

    def __str__(self):
        return self.email
