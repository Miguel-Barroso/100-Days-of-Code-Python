# @app.route("/form-entry", methods=["POST"])
# def receive_data():
#     error = None
#     if request.method == "POST":
#         form_submission = request.form
#         print(form_submission)
#         return "✅ Successfully sent your message!"
#     else:
#         error = "Form submission error!"
#         return error
#
# The below will get executed:
# <!-- Actually better with action="{{ url_for('receive_data') }}" -->
# This will not (Jinja comments):
# {# Actually better with action="{{ url_for('receive_data') }}" #}
# No need to include the html comment tags <!-- and -->