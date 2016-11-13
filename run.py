import os
from flask import Flask, render_template, redirect, request
import jinja2
import cf_deployment_tracker

cf_deployment_tracker.track()

app = Flask(__name__, template_folder='static', static_url_path = '/static', static_folder='static')
PORT = int(os.getenv('PORT', 8000))
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = PORT)
