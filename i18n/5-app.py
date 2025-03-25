#!/usr/bin/env python3

"""
Basic Flask application with a single route.
"""

from flask import Flask, render_template, request, g
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
    # BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_locale():
    """
    # Selects the best matching language from the request headers.

    Returns:
        A language code ("en" or "fr").
    """

    user_locale = request.args.get("locale")

    if user_locale and user_locale in app.config["LANGUAGES"]:
        return user_locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user():
    """
    Gets a user from the login_as URL parameter.

    Returns:
        A user dictionary if found, otherwise None.
    """

    try:
        user_id = int(request.args.get("login_as", 0))
        return users.get(user_id)
    except Exception:
        return None


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)


@app.before_request
def before_request():
    """
    Executed before each request to set g.user if logged in.
    """

    g.user = get_user()


@app.route("/")
def index():
    """
    Renders the index page.

    Returns:
         Rendered HTML template.
    """

    return render_template("5-index.html")


if __name__ == "__main__":
    app.run()
