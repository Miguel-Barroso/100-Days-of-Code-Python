from flask import Flask, render_template, request
import requests
import sending_email

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
response = requests.get("https://api.npoint.io/2e36c349acc375705222")
response.raise_for_status()
posts = response.json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    error = None
    print(request.method)
    if request.method == "POST":
        form_submission = request.form
        print(form_submission)
        sending_email.send_email_notification(form_submission["name"], form_submission["email"],
                                              form_submission["phone"], form_submission["message"])
        # return "✅ Successfully sent your message!"
        return render_template("contact.html", error=error,
                               heading="✅ Successfully sent your message!")
    if request.method == "GET":
        return render_template("contact.html", error=error, heading="Contact Me")
    return None


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001, host="0.0.0.0")
