import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, redirect
from forms import LoginForm
from flask_bootstrap import Bootstrap5

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
# app.secret_key = 'secret'  # This is how Angela wrote it

bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()  # Instantiates the form object
    if login_form.validate_on_submit():  # Checks if data was entered using a POST request and otherwise validated
        if login_form.email.data == EMAIL and login_form.password.data == PASSWORD:
            print(f"User {login_form.email.data} just logged in")
            return render_template('success.html')
        else:
            # return "Please check your login details and try again."
            return render_template('denied.html')
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
