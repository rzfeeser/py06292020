#!/usr/bin/env python3
"""
Pull a basic template from templates/ and return to user
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)

# if user sends a GET to /
@app.route("/")
def index():
    return render_template("hellobasic.html") # this must appear in templates/

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

