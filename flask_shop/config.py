"""Settings for Flask-Shop installation."""


DEBUG = True
SECRET_KEY = 'it^g$mn2aap1(01*p=kbl165x-6)8*lj^md!96yprdp17wcu9s'

# sqllite3
SQLALCHEMY_DATABASE_URI='sqlite:///shop.db'

# Debug Toolbar Configuration
DEBUG_TB_INTERCEPT_REDIRECTS = False

# Stripe secret key to be used to process purchases
STRIPE_SECRET_KEY = 'foo'

# Stripe public key to be used to process purchases
STRIPE_PUBLIC_KEY = 'bar'
