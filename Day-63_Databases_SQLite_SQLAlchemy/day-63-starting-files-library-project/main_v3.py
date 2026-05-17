from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import os
from dotenv import load_dotenv
load_dotenv()

# Version 3 of main.py puts delete in its own route which is easier to follow than v2. Both works though!

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

# First declaring the base class
class Base(DeclarativeBase):
    pass  # In simple terms, this is where a model of the database gets created in memory
          # The model is stored in a registry together with metadata and mapping engine by SQLAlchemy
          # Every class that inherits from this base model becomes a mapped table (ORM)
          # metadata is literally a collection of all tables in the database
          # DeclarativeBase basically means you declare the database schema using Python classes instead of SQL

db = SQLAlchemy(model_class=Base)  # Tells SQLAlchemy what registry to use for all database models

# Initializing the flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
db.init_app(app)

class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # The first "int" is the Python type and the second Integer is the column type
    # Both needs to be defined and are usually the same
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    rating: Mapped[float] = mapped_column(Float, unique=False, nullable=False)

    # Optional:
    def __repr__(self):
        return f"<Book {self.title}>"
    # Without it, each row will be called <Books 1>, <Books 2> and so on. Using this will say <Books Harry Potter> etc.
    # Needs to be inside this class

with app.app_context():  # With handles opening and closing of databases, files, etc.
    db.create_all()  # Creates all tables based on the model as defined above

# all_books = []

@app.route('/')
def home():
    # Display all books, if any from the database, descending alphabetic order
    result = db.session.execute(db.select(Books).order_by(Books.title))
    all_books = result.scalars().all()  # N.B. This is not safe if db contains millions of entries!
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':

        title = request.form['title']
        author = request.form['author']
        rating = request.form['rating']

        if not title:
            flash('Title is required')
        if not author:
            flash('Author is required')
        if not rating:
            flash('Rating is required')
        else:
            # all_books.append({'title': title,
            #                   'author': author,
            #                   'rating': rating})
            # Adding new book sing SQLAlchemy instead:
            new_book = Books(title=title, author=author, rating=rating)
            db.session.add(new_book)
            db.session.commit()

            # print(all_books)
            return redirect(url_for('home'))

    return render_template('add.html')

# Used to debug where the database file went
# @app.route("/where")
# def where():
#     import os
#     return os.getcwd()

@app.route("/edit", methods=['GET', 'POST'])
def edit():
    id = request.args.get('id', type=int)  # Get the parameters from the requested URL so they can be used
    book = db.session.execute(db.select(Books).where(Books.id == id)).scalar()  # Grabbing data of one book based on id
    print("Book:", book)
    if request.method == 'POST':  # If user adds a rating and clicks on submit a POST request is sent and db updated
      rating = request.form['rating']
      if not rating:
        flash('Rating is required')
      print("New rating:", request.form['rating'])
      book.rating = float(request.form['rating'])  # Remember the type is float
      db.session.commit()
      return redirect(url_for('home'))  # Returning to index.html
    return render_template('edit.html', book=book)

@app.route("/delete", methods=['GET', 'POST'])
def delete():
    id = request.args.get('id', type=int)  # Get the parameters from the requested URL so they can be used
    if id is not None:
        book_to_delete = db.session.execute(db.select(Books).where(Books.id == id)).scalar()
        print("Book:", book_to_delete)
        db.session.delete(book_to_delete)
        db.session.commit()
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
