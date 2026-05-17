# This is made by chatGPT to illustrate how a user session would work using Flask and session cookies!
# The user is redirected to different routes depending on the flow, instead of everything getting rendered under /login
# Yet, outside users cannot just type /success to log in - they won't have a valid session cookie!
# Those would just get sent to the login form

import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, redirect, url_for, session
from forms import LoginForm
from flask_bootstrap import Bootstrap5

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == EMAIL and form.password.data == PASSWORD:
            session['logged_in'] = True  # ✅ mark user as logged in
            print(f"User {form.email.data} just logged in")
            return redirect(url_for('success'))
        else:
            return redirect(url_for('denied'))
    return render_template('login.html', form=form)


@app.route("/success")
def success():
    if not session.get('logged_in'):   # ✅ only allow if logged in
        return redirect(url_for('login'))
    return render_template('success.html')


@app.route("/denied")
def denied():
    return render_template('denied.html')


@app.route("/logout")
def logout():
    session.pop('logged_in', None)  # ✅ log out
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)