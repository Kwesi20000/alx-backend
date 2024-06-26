#!/usr/bin/env python3
"""
This is a Basic Flask app
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    """Index view"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
