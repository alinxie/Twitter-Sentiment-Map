import os
from flask import Flask, render_template, redirect, request, url_for
import twittery
import jinja2
import cf_deployment_tracker
import twittery
import json

cf_deployment_tracker.track()

app = Flask(__name__, template_folder='templates') #, static_folder='static'
PORT = int(os.getenv('PORT', 8000))

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        subject = request.form['subject']
        clusters = twittery.watson_clusters(str(subject))
        json_clusters = json.dumps(list(clusters.values()))
        return render_template("map.html", clusters = json_clusters)
    return render_template("index.html")



if __name__ == "__main__":
    app.run(host='0.0.0.0', port = PORT)
