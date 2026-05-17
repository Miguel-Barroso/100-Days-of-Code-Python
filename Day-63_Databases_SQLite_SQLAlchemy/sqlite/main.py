import sqlite3  # Included in every Python installation

db = sqlite3.connect("books-collection.db")  # Instantiating a database (note how a .db file gets created when running)

cursor = db.cursor()  # Need a cursor to point to rows and columns in our db

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, "
#                "author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# Cursor created on line #5 and will do all the manipulations of the database
# .execute() Will tell the cursor to execute SQL query commands
# CREATE TABLE will create a new table in the db with the name anteceeding this command
# books is the name of the table
# id INTEGER creates a column with the name of id and of datatype integer.
# PRIMARY KEY sets this column as the primary identifier of the data in this table
# title creates a second column with the name title
# varchar(250) means a variable string of max 250 characters can be accepted by title
# NOT NULL UNIQUE means the data cannot be empty and every piece of data must be unique
# rating FLOAT NOT NULL means the ratings column accepts floats, and data cannot be empty.

cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()

# Note: if you wrote VALUE instead of VALUES you would get an error. Writing SQL commands directly is inefficient

