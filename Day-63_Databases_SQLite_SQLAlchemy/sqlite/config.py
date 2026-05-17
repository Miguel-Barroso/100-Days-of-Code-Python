# Note: this is not used in this project but good practice henceforth

import os
# Allows us to traverse directories and files in the OS
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Gets the database path from the SQLAlchemy URI or defines a default app.db if not found
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, 'app.db')

