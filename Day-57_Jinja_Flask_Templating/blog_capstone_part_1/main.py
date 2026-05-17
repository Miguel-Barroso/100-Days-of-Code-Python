from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_posts():
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    response.raise_for_status()
    print(response)
    return response.json()

all_posts = get_posts()

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/blog/<int:num>')
def get_blog(num):
    print(num)
    print(type(num))
    return render_template('post.html', posts=all_posts, num=num)

if __name__ == "__main__":
    app.run(debug=True)
