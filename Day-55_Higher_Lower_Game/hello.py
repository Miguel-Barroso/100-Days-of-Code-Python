from flask import Flask
app = Flask(__name__)

# Always good to have a route to the root
@app.route('/')
def hellow_world():
    return '<h1 style="text-align: center">Hello, World!</h1>'\
           '<p>This is a paragraph</p>'\
           '<p>This is also a paragraph</p>' \
           '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExN3Q5cjd0ZWQ3bTFmZ25ob3p6ZTVoMGRrb2JiaWNnN2NpODNwYmNvMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5yXllvXr83bY4/giphy.gif">'

# @app.route('/<username>')  # This route has a dynamic variable denoted by brackets, <name>
# def greet(name):
#     return f"Hello there {name}!"  # This will trip the debugger

# @app.route('/<name>')
# def greet(name):
#     return f"Hello there {name + 12}!"  # This will trip the debugger

# @app.route('/username/<name/1>')  # This will not work as routes default to strings
# def greet(name):
#     return f"Hello there {name}!"

# @app.route('/username/<path:name>')  # Forward slashes in variables need to be converted into a path
# def greet(name):
#     return f"Hello there {name}!"

@app.route("/username/<name>/<int:number>")
def greet(name, number):  # You accept both arguments in your function
    return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)  # Activates the auto-reloader so we don't have to stop and start the program

