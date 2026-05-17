import random, requests
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year = datetime.now().year
    ## Render template allows you to add keyword arguments to the page to be rendered
    return render_template('index.html', num=random_number, year=year)

@app.route('/guess/<name>')  # When visitor visits /guess/random_name that variable is sent to the guess() method
def guess(name):
    # Getting the gender of the name in the url i.e., /guess/miguel
    gender_response = requests.get(f'https://api.genderize.io/?name={name}')
    gender_response.raise_for_status()
    gender = gender_response.json()['gender']
    # Getting the predicted age of the name in the url
    age_response = requests.get(f'https://api.agify.io/?name={name}')
    age_response.raise_for_status()
    age = age_response.json()['age']
    return render_template('guess.html', name=name.capitalize(), gender=gender, age=age)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    blog_response.raise_for_status()
    print(blog_response)
    all_posts = blog_response.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)

# Note, you cannot have inline comments in the template using <!-- and -->
# At least not on the lines where you use {{ }} as Jinja2 is trying to evaluate those lines as Python code
# For multiple lines, use {% %} on for loops, if statements etc
# You need to end the for and ifs with {% endfor %}, {% endif %} etc