from flask.ext.script import Manager
from flask_shop.flask_shop import app, clear_db, create_db
manager = Manager(app)


@manager.command
def cleardb():
    """Initialize database."""
    with app.app_context():
        clear_db()


@manager.command
def createdb():
    """Initialize database."""
    with app.app_context():
        create_db()

if __name__ == '__main__':
    manager.run()
