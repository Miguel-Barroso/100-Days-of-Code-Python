import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, request, redirect, url_for, flash

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

all_books = []

@app.route('/')
def home():
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
            all_books.append({'title': title,
                              'author': author,
                              'rating': rating})
            print(all_books)
            return redirect(url_for('home'))

    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)

