import random

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"/>')


random_number = random.randint(0,9)
# To test the extreme cases
# random_number = 0
# random_number = 9
print(f"Random number: {random_number}")

# Variable URLs in route, also known as Dynamic Routing
@app.route('/<int:number>')
def guess(number):
    if number < random_number:
        return f'<h1 style="color: red">{number} is too low try again!</h1>' \
                f'<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif number == random_number:
        return f'<h1 style="color: green">{number} is correct, you found me!</h1>' \
               f'<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    else:
        return f'<h1 style="color: purple">{number} is too high try again!</h1>' \
               f'<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'


if __name__ == '__main__':
    app.run(debug=True)