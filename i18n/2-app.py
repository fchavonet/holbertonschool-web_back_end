#!/usr/bin/env python3

"""
Basic Flask application with a single route.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


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


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)
babel.init_app(app, locale_selector=lambda: get_locale())


def get_locale() -> str:
    """
    Selects the best matching language from the request headers.

    Returns:
        A language code ("en" or "fr").
    """

    return request.accept_languages.best_match(app.config["LANGUAGES"])


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
