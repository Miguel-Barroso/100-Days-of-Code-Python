from flask import Flask
app = Flask(__name__)

# Custom decorators
def make_bold(function):

    def wrapper():
        return f"<b>{function()}</b>"

    return wrapper

# ✅ Rule of thumb: In a decorator, if the original function is supposed to return something meaningful,
# your wrapper almost always needs to return it (possibly modified).
# Otherwise, the return value gets lost and replaced by None, which can't be used by Flask.

def make_italic(function):

    def wrapper():
        return f"<em>{function()}</em>"

    return wrapper

def make_underlined(function):

    def wrapper():
        return f'<p style="text-decoration-line: underline;">{function()}</p>'

    return wrapper

@app.route('/')
@make_bold
@make_italic
@make_underlined
def hello_world():
    return "Hello, World!"

"""
The above is equivalent to the following:
def hello_world():
    return "Hello, World!"

hello_world = make_underlined(hello_world)
hello_world = make_italic(hello_world)
hello_world = make_bold(hello_world)
hello_world = app.route('/')(hello_world)

See how each function call is returned and used as the input for the next?
This way each wrapper function nests the functionality of the previous.
"""

if __name__ == '__main__':
    app.run(debug=True)