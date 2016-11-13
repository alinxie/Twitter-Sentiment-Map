import os
from flask import Flask, render_template, redirect, request, url_for
import jinja2
import cf_deployment_tracker

cf_deployment_tracker.track()

app = Flask(__name__, template_folder='templates', static_url_path = '/static', static_folder='static')
PORT = int(os.getenv('PORT', 5000))
@app.route("/", methods=['GET', 'POST'])
def index():
    # Default value is america
    subject = "america"
    name = subject
    if request.method == 'POST':
        name = request.form['subject']
        subject = "https://twitter.com/hashtag/" + request.form['subject']
        print (subject)
        print (name)
        return render_template("index.html", subject=subject, name=name)

    return render_template("index.html", subject=subject, name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = PORT)
