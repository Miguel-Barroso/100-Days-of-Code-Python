from config import Config  # Unused in this project
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask import Flask, render_template, request
from flask_migrate import Migrate  # Unused in this project

# First declare a Base class
class Base(DeclarativeBase):
    pass

# Then instantiate a db object which inherits from this Base class
db = SQLAlchemy(model_class=Base)

# The following will create a table with the class' name in snake_case and with the schema defined as below
# The db table class object inherits from the db.Model base class
class Books(db.Model):  # Database model = a collection of classes defining the schema in Flask-SQLAlchemy
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # ids will be assigned automatically by the db if primary key
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

# Initializing the Flask app
app = Flask(__name__)

# These two lines connects SQLAlchemy to both the database file and the Flask app
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)

# Creating the table schema in the database
# Needs to have a Flask app context:
with app.app_context():
    db.create_all()  # Creates tables from all models in this file (or from imported modules)
# create_all() will not update already existing tables, for that use Flask-Migrate or similar

# Optional:
def __repr__(self):
    return f"<Book {self.title}>"
# Without it, each row will be called <Books 1>, <Books 2> and so on. Using this will say <Books Harry Potter> etc. instead

# Create a New Record

# with app.app_context():
#     new_book = Books(title="Harry Potter", author="J. K. Rowling", rating=9.3)
#     db.session.add(new_book)
#     db.session.commit()

# Read All Records
with app.app_context():
    result = db.session.execute(db.select(Books).order_by(Books.title))  # Gets the rows as a Result object
    all_books = result.scalars()  # Scalars() gets the individual elements instead of entire rows
    for book in all_books:  # You read by iterating over all objects in all_books
        print(book.title)
    # or all_books = result.scalars().all() --> this will give you a list over which you can loop, index, etc.
    # N.B.: .all() will load everything into RAM which is dangerous if your db has millions of rows!
    # Example how to retrieve millions of rows using chunking --> (thanks chatGPT)
    # stmt = db.select(Books).execution_options(yield_per=1000)
    # result = db.session.execute(stmt)
    #
    # for book in result.scalars():
    #     process(book)

# Read a Particular Record by Query
with app.app_context():
    book = db.session.execute(db.select(Books).where(Books.title == "Harry Potter")).scalar()
    # The above gets a single element using scalar() instead of scalars()

# Update a Record by Primary Key
book_id = 1
with app.app_context():
    book_to_update = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    # or book_to_update = db.get_or_404(Books, book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()

# Delete a Particular Record by Primary Key
book_id = 1
with app.app_context():
    book_to_delete = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    # or book_to_delete = db.get_or_404(Books, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()

# The "with app.app_context():" is only needed once in the code and never in Flask routes.
# Flask already provides the app context, making it redundant and can create weird behavior.
# Also, remember the type of book.id and the other columns. You should store the results as the same type!

@app.route('/')
def index():
    pass