#!/usr/bin/env python3

"""
Basic Flask application with a single route.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """
    Renders the index page with a "Hello world"" message.

    Returns:
        Rendered HTML template for the "root" route.
    """

    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
