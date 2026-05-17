from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def receive_data():
    error = None
    if request.method == 'POST':
        form_submission = f"Name: {request.form['username']}, Password: {request.form['password']}"
        return f"<h1> {form_submission} </h1>"
    else:
        error = 'Form not submitted'
        return error


"""
NOTE: The action attribute of the form can be set to "/login" e.g.

    <form action="/login" method="post">

or it can be dynamically generated with url_for e.g.

    <form action="{{ url_for('receive_data') }}" method="post">

Depending on where your server is hosted, the "/login" path may change. So it's usually a better idea to use url_for 
to dynamically generate the url for a particular function in your Flask server.
"""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001, use_reloader=True)
