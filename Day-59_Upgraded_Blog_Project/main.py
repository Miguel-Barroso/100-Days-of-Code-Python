from flask import Flask, render_template
import requests
from datetime import datetime

response = requests.get("https://api.npoint.io/2e36c349acc375705222")
response.raise_for_status()

all_posts = response.json()

app = Flask(__name__)

# Allows you to inject variables into documents without a route
@app.context_processor
def inject_now():
    return {'year': datetime.now().year}

@app.route('/')
def home():
    return render_template('index.html', posts=all_posts)

@app.route('/about')
def about():
    return render_template('about.html', posts=all_posts)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    # The following logic can change post.html content based on the requested post URL
    requested_post = None
    for blog_post in all_posts:
        if blog_post['id'] == post_id:
            requested_post = blog_post
    return render_template('post.html', blog_post=requested_post)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001, use_reloader=True)  # Broadcasts on local network
                                               # Never ever run this in production with debug mode on!