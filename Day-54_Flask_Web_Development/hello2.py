from flask import Flask

app = Flask(__name__)  # __name__ is a special variable in Python
                       # It can flag if the code is run as the main program
                       # As in a script for example, or as an imported module, etc.
                       # It is set by the Python interpreter at run time
                       # If instead the code is loaded as module (imported)
                       # then __name__ equals the name of the module (file-name)

print(__name__)

@app.route("/")  # This tells Flask where the root of the app lives
def hello_world():
    return "Hello, World!"  # Will render as html per default (inside the body tag)

if __name__ == "__main__":
    app.run()  # This code block will only execute if the script is run as main
                         # I.e., when run directly, the code will execute (will not enter debug mode per default but can be set with debug=True)
                         # This prevents running this script as part of production which otherwise would be dangerous
                         # as the debugger allows anyone with access to execute arbitrary code during run time
                         # It has the added benefit that you can stop the program with the stop-button in PyCharm
                         # instead of using Ctrl + C

# Running the code this way does not require us to add the environment variable as in the previous example (hello.py)
# as in export FLASK_APP=hello.py
# Though, this is not mentioned in the Flask quick start anymore?
# Apparently, from Flask 2.2 onwards (released in 2022), app discovery is done automatically
# and most people do not need to set any environment variables