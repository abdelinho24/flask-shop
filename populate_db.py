from flask_shop.flask_shop import app
from flask_shop.models import Product, db

product1 = Product(
    id=1,
    name="Learn Python the Hard Way: A Very Simple Introduction to the Terrifyingly Beautiful World of Computers and Code (3rd Edition)",
    description="Zed Shaw has perfected the world's best system for learning Python. Follow it and you will succeed-just like the hundreds of thousands of beginners Zed has taught to date!",
    image='book1.jpg',
    discontinued=False,
    price=9.99)

product2 = Product(
    id=2,
    name="Learning Python",
    description="Get a comprehensive, in-depth introduction to the core Python language with this hands-on book. ",
    image='book2.jpg',
    discontinued=False,
    price=9.99)

product3 = Product(
    id=3,
    name="Python Programming for the Absolute Beginner, Third Edition",
    description="If you are new to programming with Python and are looking for a solid introduction, this is the book for you. ",
    image='book3.jpg',
    discontinued=False,
    price=9.99)

product4 = Product(
    id=4,
    name="Python Programming: An Introduction to Computer Science, 2nd Ed.",
    description="This is the second edition of John Zelle's Python Programming, updated for Python 3.",
    image='book4.jpg',
    discontinued=False,
    price=9.99)

product5 = Product(
    id=5,
    name="Programming the Raspberry Pi: Getting Started with Python",
    description="Create innovative programs and fun games on your tiny yet powerful Raspberry Pi.",
    image='book5.jpg',
    discontinued=False,
    price=9.99)


db.session.add(product1)
db.session.add(product2)
db.session.add(product3)
db.session.add(product4)
db.session.add(product5)
db.session.commit()




