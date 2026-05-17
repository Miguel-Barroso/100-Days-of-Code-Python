from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('miguel.html')

if __name__ == '__main__':
    app.run(debug=True)  # Refreshes the code when we make changes

# Note that the browser may cache static files
# To do a hard refresh, hold shift while clicking reload in the browser