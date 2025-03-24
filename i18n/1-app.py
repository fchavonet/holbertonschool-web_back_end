#!/usr/bin/env python3

"""
Basic Flask application with a single route.
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configuration class for the Flask app.

    Attributes:
        LANGUAGES: List of supported languages.
        BABEL_DEFAULT_LOCALE: Default language.
        BABEL_DEFAULT_TIMEZONE: Default timezone.
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/")
def index():
    """
    Renders the index page.

    Returns:
         Rendered HTML template.
    """

    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
