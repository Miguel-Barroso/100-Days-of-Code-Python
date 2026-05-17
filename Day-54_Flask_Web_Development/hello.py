from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# In order to run this, we need to add an environment variable to this .venv
# Do this export FLASK_APP=hello.py