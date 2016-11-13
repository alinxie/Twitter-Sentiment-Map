import os
from flask import Flask, render_template, redirect, request, url_for
import twittery
import jinja2
import cf_deployment_tracker

cf_deployment_tracker.track()

app = Flask(__name__, template_folder='templates') #, static_folder='static'
PORT = int(os.getenv('PORT', 8000))

@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        subject = request.form['subject']
        return render_template("map.html")

    return render_template("index.html")


#To Run twitter queries after getting subject
def clusters():
    pass

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = PORT)
